#!/usr/bin/env python3
"""Check the research repository. Exit 1 on any failure.

    python3 scripts/check.py [--root DIR] [--today YYYY-MM-DD] [--denylist FILE] [--allow-pending]

`--denylist` names the optional local scrub list, a file of names that are not public, one per line,
kept outside this repository; without it, the file that the OBR_SCRUB_LIST environment variable
names is used.

Checks, each printed as one PASS, FAIL or UNVERIFIED line, with one line per problem above it:

  frontmatter   every research document has a dated `last_checked`, a `volatility` and `sources`
  ledgers       every _evidence/*.jsonl record has its required fields, an http(s) url, a quote of
                at most 25 words and no longer quotation in any other text field; ids are unique except
                a later file that repeats an id, with the same url, to re-verify it
  cards         every models/<maker>/<id>.json matches models/FORMAT.md, and holds no quotation over 25
                words in any text field
  models        each card has its model file and each model file its card; each model file, and each
                maker's README, holds every heading of its template in order; a model file holds the voice
                subsection when its card lists audio output, and only then
  providers     providers/README.md exists; each provider file holds every heading of the provider
                template in order and names a known kind
  applications  applications/implementer-tiers.json is well formed, names only models that have a card
                and cites only source ids a reader can reach
                (cards and applications also fail on text that points at something a public reader cannot
                reach: a private ruling or table, or a link or `.md` name that does not resolve here)
  generated     the card blocks, the models and providers tables and applications/implementer-tiers.md
                equal what scripts/render.py renders
  index         INDEX.md lists every research document, and nothing else, with its current facts
  links         every relative link in a Markdown file resolves, anchors included
  quotes        no quotation in prose runs over 25 words, in any quotation-mark style, and no unmarked
                blockquote does
  queue         every file in ingest/queue/ is a well-formed finding named <YYYYMMDD>-<64 hex digits>.json
                after the sha256 of its claim and url; ingest/seen.jsonl is well formed
  symlinks      no file that can be published is a symbolic link (Git can commit one); the other
                checks that read every such file skip links
  invisible     no file that can be published holds an invisible or format character: Unicode category
                Cf, a variation selector (U+FE00-FE0F, U+E0100-E01EF) or a tag character (U+E0000-E007F);
                U+FE0F is allowed directly after an emoji
  scrub         no term of the optional local scrub list appears anywhere (UNVERIFIED when there is no list)
  pending       no file holds the placeholder line a stub keeps in each section nobody has written
                (with --allow-pending this is UNVERIFIED, not FAIL, so a writer can run the other checks
                while stubs remain)

It then prints, without failing on it, the documents and cards whose check date is older than the
window for their volatility, and the model classes that hold cards of more than two generations.
Standard library only; consumers never run this.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import posixpath
import re
import unicodedata
import sys
from pathlib import Path
from typing import Any, Callable

sys.path.insert(0, str(Path(__file__).resolve().parent))
import collect  # noqa: E402
import layout  # noqa: E402
import render  # noqa: E402

RESEARCH_DIRS = ("models", "harnesses", "providers", "practices", "applications")
VOLATILITY_WINDOWS = {"STABLE": 180, "MONITOR": 30, "VOLATILE": 14}  # days
MAX_QUOTE_WORDS = 25
LEDGER_KINDS = {"practice", "finding", "generation", "family-note"}
LEDGER_VERDICTS = {"supported", "overstated"}
LEDGER_EVIDENCE = {"measured", "lab-guidance", "practitioner-consensus", "anecdote", "standards", "forecast", "own-result"}
CARD_KEYS = (
    "id", "name", "maker", "family", "class", "generation", "released", "status", "retires", "weights",
    "access", "context_window", "max_output", "modalities", "voice", "reasoning", "pricing_usd_per_mtok",
    "benchmarks", "prompting_guides", "system_card", "model_page", "sources", "checked", "unknown",
)
# The keys of a card's `voice` object, and the values `duplex` may take.
VOICE_KEYS = (
    "duplex", "input_audio", "output_audio", "voices", "languages", "turn_detection", "interruption",
    "latency", "session_limit",
)
VOICE_DUPLEX = {"full", "half", "none"}
CARD_STATUS = {"ga", "preview", "deprecated", "retiring"}
CARD_CONTROL = {"effort", "budget", "toggle", "always-on", "none"}
CARD_MEASURED_BY = {"independent", "maker", "third-party-vendor"}
CARD_TIERS = {"outcome", "design", "spec"}
CARD_CONFIDENCE = {"high", "medium", "low"}
CARD_SOURCE_KINDS = {"M", "L", "P", "A"}
# Top-level card keys whose null or empty value needs no entry in `unknown`: a card with no retirement
# announced, and a text model's `voice`.
CARD_MAY_BE_EMPTY = {"retires", "voice"}

Problems = list[str]

# Wording that points a reader at something a public reader cannot reach: a file that is not in this
# repository, a table kept elsewhere, or a ruling that is not recorded in it. A card or the placement
# data that rests on evidence cites that evidence, or says "inferred". `unresolved_references` adds
# any link or `.md` name that does not resolve in the repository.
UNREACHABLE = re.compile(
    r"(?<![\w-])tiers\.md|\blibrary's (?:table|placement)|the library table|needs the maintainer"
    r"|\bmaintainers?(?:'s|')?(?:\s+\w+){0,3}?\s+(?:rul(?:e[sd]?|ings?)|asks?|asked|prefer\w*)\b"
    r"|\bexisting row\b|\bOutcomeBound's (?:row|table)\b",
    re.IGNORECASE,
)
# A `.md` name in text (a path or a bare file name, URLs left out), and the target of a Markdown link.
MD_NAME = re.compile(r"(?<![\w./:-])((?:\.\./|[\w-]+/)*[\w.-]+\.md)(?![\w-])")
TEXT_LINK = re.compile(r"\]\(\s*<?([^)>\s]+)>?\)")


# ---------------------------------------------------------------------------------------------
# Shared readers


def is_date(value: object) -> bool:
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
        return False
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def words(text: str) -> int:
    """The rule's word count: whitespace-separated tokens."""
    return len(text.split())


def rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def research_docs(root: Path) -> list[Path]:
    """Every Markdown document under the research folders except the navigation and format pages
    (layout.PAGES), which carry no frontmatter and no row in INDEX.md."""
    found = []
    for folder in RESEARCH_DIRS:
        found.extend(p for p in (root / folder).rglob("*.md") if rel(root, p) not in layout.PAGES)
    return sorted(found)


def markdown_files(root: Path) -> list[Path]:
    """Every Markdown file in the repository, hidden folders other than .github left out."""
    found = []
    for path in root.rglob("*.md"):
        parts = path.relative_to(root).parts
        if any(p.startswith(".") and p != ".github" for p in parts[:-1]) or path.name.endswith(".orig"):
            continue
        found.append(path)
    return sorted(found)


parse_frontmatter = layout.parse_frontmatter
title_of = layout.title_of


def volatility_class(value: str) -> str | None:
    word = value.split()[0].strip("(:;,") if value.split() else ""
    return word if word in VOLATILITY_WINDOWS else None


# ---------------------------------------------------------------------------------------------
# Checks


def check_frontmatter(root: Path, today: dt.date) -> Problems:
    problems = []
    for path in research_docs(root):
        name = rel(root, path)
        parsed = parse_frontmatter(path.read_text(encoding="utf-8"))
        if parsed is None:
            problems.append(f"{name}: no frontmatter")
            continue
        data, body = parsed
        generated = data.get("generated") == "true"
        checked = data.get("last_checked")
        if generated and checked == "none":
            pass
        elif not is_date(checked):
            problems.append(f"{name}: last_checked is missing or not an ISO date")
        elif collect.is_future(dt.date.fromisoformat(str(checked)), today):
            problems.append(f"{name}: last_checked {checked} is in the future")
        volatility = data.get("volatility")
        if not isinstance(volatility, str) or volatility_class(volatility) is None:
            problems.append(f"{name}: volatility must start with STABLE, MONITOR or VOLATILE")
        sources = data.get("sources")
        if not isinstance(sources, list):
            problems.append(f"{name}: sources is missing")
        elif not sources and not generated:
            problems.append(f"{name}: sources is empty")
        else:
            problems.extend(f"{name}: source {s!r} does not start with an http(s) url" for s in sources if not re.match(r"https?://\S+", s))
        if not title_of(body):
            problems.append(f"{name}: no `# ` title")
    return problems


def ledger_files(root: Path) -> list[Path]:
    return sorted((root / "_evidence").glob("*.jsonl"))


def ledger_records(root: Path) -> tuple[list[tuple[str, int, dict[str, Any]]], Problems]:
    """Every record as (file, line, record), and the problems reading them."""
    records: list[tuple[str, int, dict[str, Any]]] = []
    problems: Problems = []
    for path in ledger_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as error:
            problems.append(f"{rel(root, path)}: cannot be read as UTF-8 text: {getattr(error, 'strerror', None) or error}")
            continue
        for number, line in enumerate(text.split("\n"), 1):
            if not line.strip():
                continue
            where = f"{rel(root, path)}:{number}"
            try:
                record = json.loads(line)
            except ValueError:
                problems.append(f"{where}: not JSON")
                continue
            if not isinstance(record, dict):
                problems.append(f"{where}: not a JSON object")
                continue
            records.append((rel(root, path), number, record))
    return records, problems


def check_ledgers(root: Path) -> Problems:
    records, problems = ledger_records(root)
    for path in sorted((root / "_evidence").glob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except ValueError:
            problems.append(f"{rel(root, path)}: not JSON")
    first_seen: dict[str, tuple[str, int, str | None]] = {}
    lines_in_file: dict[str, dict[str, int]] = {}  # id -> file -> first line there
    for file, number, record in records:
        where = f"{file}:{number}"
        ident = record.get("id")
        if not isinstance(ident, str) or not ident.strip():
            problems.append(f"{where}: id is missing or not text")
            continue
        for key in ("kind", "claim"):
            if not isinstance(record.get(key), str) or not record[key].strip():
                problems.append(f"{where} [{ident}]: {key} is missing or empty")
        kind = record.get("kind")
        if kind is not None and kind not in LEDGER_KINDS:
            problems.append(f"{where} [{ident}]: kind {kind!r} is not one of {', '.join(sorted(LEDGER_KINDS))}")
        if kind != "family-note":
            url = record.get("url")
            if not isinstance(url, str) or not re.match(r"https?://\S+$", url):
                problems.append(f"{where} [{ident}]: url is missing or not an http(s) address")
            if "quote" not in record:
                problems.append(f"{where} [{ident}]: quote is missing")
            if record.get("verification") not in LEDGER_VERDICTS:
                problems.append(f"{where} [{ident}]: verification is not supported or overstated")
            if "evidence" in record and record["evidence"] not in LEDGER_EVIDENCE:
                problems.append(f"{where} [{ident}]: evidence {record['evidence']!r} is not an evidence class")
        quote = record.get("quote")
        if quote is not None:
            if not isinstance(quote, str):
                problems.append(f"{where} [{ident}]: quote is not text")
            elif words(quote) > MAX_QUOTE_WORDS:
                problems.append(f"{where} [{ident}]: quote is {words(quote)} words, over {MAX_QUOTE_WORDS}")
        for key, text in _text_fields(record):
            if key == "quote":
                continue
            for count, shown in long_quotations(text):
                problems.append(f"{where} [{ident}]: {key} holds a quotation of {count} words, over {MAX_QUOTE_WORDS}: {shown[:50]}...")
        previous = first_seen.get(ident)
        if previous is None:
            first_seen[ident] = (file, number, record.get("url"))
            lines_in_file[ident] = {file: number}
        elif file in lines_in_file[ident]:
            problems.append(f"{where} [{ident}]: id repeats within one file (first at line {lines_in_file[ident][file]})")
        elif previous[2] != record.get("url"):
            problems.append(f"{where} [{ident}]: id repeats {previous[0]} with another url, so it is not a re-verification")
        else:
            lines_in_file[ident][file] = number
    return problems


def _text_fields(value: object, key: str = "") -> list[tuple[str, str]]:
    """Every string in a record, with the name of the field that holds it."""
    if isinstance(value, str):
        return [(key, value)]
    if isinstance(value, dict):
        return [pair for k, v in value.items() for pair in _text_fields(v, str(k))]
    if isinstance(value, list):
        return [pair for item in value for pair in _text_fields(item, key)]
    return []


Resolver = Callable[[str], bool]


def repo_paths(root: Path) -> set[str]:
    """Every file and folder in the repository, relative to root, `.git` and caches left out."""
    found: set[str] = set()
    for path in root.rglob("*"):
        parts = path.relative_to(root).parts
        if parts[:1] != (".git",) and "__pycache__" not in parts:
            found.add("/".join(parts))
    return found


def repo_resolver(paths: set[str], base: str) -> Resolver:
    """Whether a path named in text found in the folder `base` (relative to root) resolves among
    `paths`: as a path from `base` or from the root, or, for a bare file name, as the name of any
    file here. An anchor after `#` is ignored."""
    names = {posixpath.basename(p) for p in paths}

    def resolves(target: str) -> bool:
        target = target.split("#", 1)[0].rstrip("/")
        if not target:
            return True
        joined = posixpath.normpath(posixpath.join(base, target))
        return joined in paths or posixpath.normpath(target) in paths or ("/" not in target and target in names)

    return resolves


def unresolved_references(text: str, resolves: Resolver | None) -> list[str]:
    """Each link target (not a URL) and each `.md` name in the text that does not resolve; with no
    resolver (no repository), every one."""
    found: list[str] = []
    targets = [m for m in TEXT_LINK.findall(text) if not re.match(r"[A-Za-z][A-Za-z0-9+.-]*:", m)]
    for target in targets + MD_NAME.findall(text):
        if target not in found and (resolves is None or not resolves(target)):
            found.append(target)
    return found


def unreachable(text: str, resolves: Resolver | None) -> list[str]:
    """What the text points at that a public reader cannot reach, each as it is written."""
    hits = [m.group(0) for m in UNREACHABLE.finditer(text)]
    return hits + [r for r in unresolved_references(text, resolves) if not any(r in h for h in hits)]


def ledger_ids(root: Path) -> set[str]:
    records, _ = ledger_records(root)
    return {r["id"] for _, _, r in records if isinstance(r.get("id"), str)}


CITATION = re.compile(r"\[([a-z][a-z0-9]*(?:[-.][a-z0-9]+)+)\]")


def _nonempty_text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _is_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def card_problems(
    card: object, expected_id: str, known_ids: set[str], today: dt.date, resolves: Resolver | None = None,
) -> Problems:
    """Problems with one card against models/FORMAT.md; empty when it is valid. `resolves` judges a
    link or `.md` name in the card's text; without it, no such name resolves."""
    if not isinstance(card, dict):
        return ["not a JSON object"]
    problems: Problems = []
    extra = sorted(set(card) - set(CARD_KEYS))
    missing = [k for k in CARD_KEYS if k not in card]
    if extra:
        problems.append(f"unknown key(s): {', '.join(extra)}")
    if missing:
        problems.append(f"missing key(s): {', '.join(missing)}")
    if missing:
        return problems

    def bad(message: str) -> None:
        problems.append(message)

    def date_ok(key: str, value: object, nullable: bool = False, past: bool = False) -> None:
        if value is None and nullable:
            return
        if not is_date(value):
            bad(f"{key} is not an ISO date")
        elif past and collect.is_future(dt.date.fromisoformat(str(value)), today):
            bad(f"{key} {value} is in the future")

    if card["id"] != expected_id:
        bad(f"id {card['id']!r} does not match the file name {expected_id!r}")
    for key in ("name", "maker", "family", "class"):
        if not _nonempty_text(card[key]):
            bad(f"{key} is missing or empty")
    date_ok("released", card["released"], nullable=True)
    if card["status"] not in CARD_STATUS:
        bad(f"status is not one of {', '.join(sorted(CARD_STATUS))}")
    date_ok("retires", card["retires"], nullable=True)
    weights = card["weights"]
    if weights is not None and not (weights == "closed" or (isinstance(weights, str) and re.fullmatch(r"open \(.+\)", weights))):
        bad('weights is not "closed" or "open (<licence>)"')
    if not isinstance(card["access"], list) or not all(_nonempty_text(a) for a in card["access"]):
        bad("access is not a list of text")
    for key in ("context_window", "max_output"):
        value = card[key]
        if value is not None and not (isinstance(value, int) and not isinstance(value, bool) and value > 0):
            bad(f"{key} is not a positive integer or null")
    modalities = card["modalities"]
    if modalities is not None and not (
        isinstance(modalities, dict)
        and set(modalities) == {"input", "output"}
        and all(isinstance(v, list) and all(_nonempty_text(x) for x in v) for v in modalities.values())
    ):
        bad("modalities is not {input: [...], output: [...]}")
    voice = card["voice"]
    if voice is not None:
        problems.extend(_voice_problems(voice, card["unknown"]))
    reasoning = card["reasoning"]
    if reasoning is not None:
        if not (isinstance(reasoning, dict) and set(reasoning) == {"control", "levels", "default"}):
            bad("reasoning needs exactly control, levels and default")
        else:
            # A value not found is null (or empty) and named in `unknown` (FORMAT.md).
            named = [u for u in card["unknown"] if isinstance(u, str) and u.startswith("reasoning")] if isinstance(card["unknown"], list) else []
            if reasoning["control"] not in CARD_CONTROL and not (reasoning["control"] is None and named):
                bad(f"reasoning.control is not one of {', '.join(sorted(CARD_CONTROL))}")
            levels = reasoning["levels"]
            if not isinstance(levels, list) or not all(_nonempty_text(x) for x in levels):
                bad("reasoning.levels is not a list of text")
            elif reasoning["control"] == "effort" and not levels and not named:
                bad("reasoning.control is effort but reasoning.levels is empty")
            default = reasoning["default"]
            if default is not None and (not isinstance(levels, list) or default not in levels):
                bad("reasoning.default is not one of reasoning.levels")
    pricing = card["pricing_usd_per_mtok"]
    if pricing is not None:
        if not (isinstance(pricing, dict) and set(pricing) == {"input", "output", "cached_input", "notes"}):
            bad("pricing_usd_per_mtok needs exactly input, output, cached_input and notes")
        else:
            for key in ("input", "output", "cached_input"):
                if pricing[key] is not None and not (_is_number(pricing[key]) and pricing[key] >= 0):
                    bad(f"pricing_usd_per_mtok.{key} is not a number or null")
            if pricing["notes"] is not None and not isinstance(pricing["notes"], str):
                bad("pricing_usd_per_mtok.notes is not text or null")
    source_ids: set[str] = set()
    sources = card["sources"]
    if not isinstance(sources, list):
        bad("sources is not a list")
        sources = []
    for index, source in enumerate(sources):
        label = f"sources[{index}]"
        if not (isinstance(source, dict) and set(source) == {"id", "url", "read", "kind", "quote"}):
            bad(f"{label} needs exactly id, url, read, kind and quote")
            continue
        if not _nonempty_text(source["id"]):
            bad(f"{label}.id is empty")
        elif source["id"] in source_ids:
            bad(f"{label}.id {source['id']!r} repeats")
        else:
            source_ids.add(source["id"])
        if not (isinstance(source["url"], str) and re.match(r"https?://\S+$", source["url"])):
            bad(f"{label}.url is not an http(s) address")
        date_ok(f"{label}.read", source["read"], past=True)
        if source["kind"] not in CARD_SOURCE_KINDS:
            bad(f"{label}.kind is not one of M, L, P, A")
        quote = source["quote"]
        if quote is not None and (not isinstance(quote, str) or words(quote) > MAX_QUOTE_WORDS):
            bad(f"{label}.quote is not text of at most {MAX_QUOTE_WORDS} words")
    benchmarks = card["benchmarks"]
    if not isinstance(benchmarks, list):
        bad("benchmarks is not a list")
        benchmarks = []
    for index, bench in enumerate(benchmarks):
        label = f"benchmarks[{index}]"
        if not (isinstance(bench, dict) and set(bench) == {"name", "score", "setting", "harness", "measured_by", "source", "read"}):
            bad(f"{label} needs exactly name, score, setting, harness, measured_by, source and read")
            continue
        if not _nonempty_text(bench["name"]):
            bad(f"{label}.name is empty")
        if not _is_number(bench["score"]):
            bad(f"{label}.score is not a number")
        if bench["measured_by"] not in CARD_MEASURED_BY:
            bad(f"{label}.measured_by is not one of {', '.join(sorted(CARD_MEASURED_BY))}")
        if bench["source"] not in source_ids:
            bad(f"{label}.source {bench['source']!r} is not an id in sources")
        date_ok(f"{label}.read", bench["read"], past=True)
    for key in ("system_card", "model_page"):
        value = card[key]
        if value is not None and not (isinstance(value, str) and re.match(r"https?://\S+$", value)):
            bad(f"{key} is not an http(s) address or null")
    guides = card["prompting_guides"]
    if not isinstance(guides, list) or not all(isinstance(g, str) and re.match(r"https?://\S+$", g) for g in guides):
        bad("prompting_guides is not a list of http(s) addresses")
    generation = card["generation"]
    if generation is not None and not _nonempty_text(generation):
        bad("generation is not text or null")
    date_ok("checked", card["checked"], past=True)
    unknown = card["unknown"]
    if not isinstance(unknown, list) or not all(_nonempty_text(x) for x in unknown):
        bad("unknown is not a list of text")
        unknown = []
    named = {u.split(":")[0].split(".")[0].strip() for u in unknown}
    for prefix in render.KEY_BENCHMARKS:
        tried = any(isinstance(b, dict) and str(b.get("name", "")).startswith(prefix) for b in benchmarks)
        if not tried and not any(u.startswith(prefix) for u in unknown):
            bad(f"benchmark {prefix!r} is neither in `benchmarks` nor named in `unknown`")
    for key in CARD_KEYS:
        value = card[key]
        if key in CARD_MAY_BE_EMPTY or key == "unknown" or not (value is None or value == []):
            continue
        if key not in named:
            bad(f"{key} is empty but `unknown` has no entry starting {key!r}")
    if isinstance(pricing, dict) and (pricing.get("input") is None or pricing.get("output") is None):
        if "pricing_usd_per_mtok" not in named:
            bad("a price is null but `unknown` has no entry starting 'pricing_usd_per_mtok'")
    for key, text in _text_fields(card):
        if key == "quote":  # a source's quote is checked above, and may hold inner quotation marks
            continue
        for count, shown in long_quotations(text):
            bad(f"{key} holds a quotation of {count} words, over {MAX_QUOTE_WORDS}: {shown[:50]}...")
        for hit in unreachable(text, resolves):
            bad(f"{key} cites something a public reader cannot reach ({hit!r}): cite the evidence or say it is inferred")
    for _, text in _text_fields({k: v for k, v in card.items() if k != "sources"}):
        for ident in CITATION.findall(text):
            if ident not in source_ids and ident not in known_ids:
                bad(f"[{ident}] is cited but is neither a source id of this card nor a ledger id")
    return problems


def _voice_problems(voice: object, unknown: object) -> Problems:
    """Problems with a card's `voice` object (models/FORMAT.md): its keys, each value's type, and an
    `unknown` entry starting `voice.<key>` for each value that is null or empty."""
    if not (isinstance(voice, dict) and set(voice) == set(VOICE_KEYS)):
        return [f"voice is neither null nor an object with exactly {', '.join(VOICE_KEYS)}"]
    problems: Problems = []
    entries = [u for u in unknown if isinstance(u, str)] if isinstance(unknown, list) else []
    for key in VOICE_KEYS:
        value = voice[key]
        label = f"voice.{key}"
        if value is None or value == []:
            if not any(u.startswith(label) for u in entries):
                problems.append(f"{label} is empty but `unknown` has no entry starting {label!r}")
        elif key == "duplex":
            if value not in VOICE_DUPLEX:
                problems.append(f"{label} is not one of {', '.join(sorted(VOICE_DUPLEX))} or null")
        elif key == "voices":
            if not (_nonempty_text(value) or (isinstance(value, int) and not isinstance(value, bool) and value > 0)):
                problems.append(f"{label} is not a positive integer, text or null")
        elif key == "languages":
            if not (isinstance(value, list) and all(_nonempty_text(x) for x in value)):
                problems.append(f"{label} is not a list of text or null")
        elif not _nonempty_text(value):
            problems.append(f"{label} is not text or null")
    return problems


def check_cards(root: Path, today: dt.date) -> Problems:
    problems: Problems = []
    base = root / layout.MODELS_DIR
    known = ledger_ids(root)
    paths = repo_paths(root)
    resolvers: dict[str, Resolver] = {}
    for path in sorted(base.rglob("*.json")):
        name = rel(root, path)
        if len(path.relative_to(base).parts) != 2:
            problems.append(f"{name}: a card lives at models/<maker>/<id>.json")
            continue
        try:
            card = json.loads(path.read_text(encoding="utf-8"))
        except ValueError:
            problems.append(f"{name}: not JSON")
            continue
        folder = rel(root, path.parent)
        if folder not in resolvers:
            resolvers[folder] = repo_resolver(paths, folder)
        resolves = resolvers[folder]
        problems.extend(f"{name}: {p}" for p in card_problems(card, path.stem, known, today, resolves))
    return problems


def check_models(root: Path) -> Problems:
    """Each card and its model file come as a pair, and each model file and maker README holds
    every heading of its template."""
    problems: Problems = []
    base = root / layout.MODELS_DIR
    cards = {rel(root, p)[: -len(".json")] for p in base.glob("*/*.json")}
    files = {rel(root, p)[: -len(".md")] for p in base.glob("*/*.md") if p.name != "README.md"}
    for stem in sorted(cards - files):
        problems.append(f"{stem}.json: no model file {stem}.md")
    for stem in sorted(files - cards):
        problems.append(f"{stem}.md: no card {stem}.json")
    for stem in sorted(files):
        voice = _has_audio_output(root / f"{stem}.json")
        _headings(root, f"{stem}.md", layout.model_headings(voice), problems)
        if not voice and (3, layout.VOICE_HEADING[1]) in layout.headings((root / f"{stem}.md").read_text(encoding="utf-8")):
            problems.append(f"{stem}.md: heading `### {layout.VOICE_HEADING[1]}` is only for a model whose card lists audio output")
    for maker in sorted({Path(stem).parent.as_posix() for stem in cards | files}):
        readme = f"{maker}/README.md"
        if not (root / readme).is_file():
            problems.append(f"{readme}: missing; every maker folder has one")
        else:
            _headings(root, readme, layout.MAKER_HEADINGS, problems)
    return problems


def _has_audio_output(card_path: Path) -> bool:
    """Whether the card at this path lists audio among its outputs; false when it is missing or
    unreadable, which the cards check reports."""
    try:
        return layout.has_audio_output(json.loads(card_path.read_text(encoding="utf-8")))
    except (OSError, ValueError):
        return False


def _headings(root: Path, name: str, wanted: tuple[tuple[int, str], ...], problems: Problems) -> None:
    text = (root / name).read_text(encoding="utf-8")
    problems.extend(f"{name}: heading `{h}` is missing or out of order" for h in layout.missing_headings(text, wanted))


def check_providers(root: Path) -> Problems:
    problems: Problems = []
    if not (root / layout.PROVIDERS_README).is_file():
        problems.append(f"{layout.PROVIDERS_README}: missing")
    for path in render.provider_files(root):
        name = rel(root, path)
        text = path.read_text(encoding="utf-8")
        kind = render.provider_kind(text)
        if kind not in layout.PROVIDER_KINDS:
            problems.append(f"{name}: kind {kind!r} is not one of {', '.join(layout.PROVIDER_KINDS)}")
        _headings(root, name, layout.PROVIDER_HEADINGS, problems)
    return problems


def check_applications(root: Path) -> Problems:
    """applications/implementer-tiers.json: its shape, that each model has a card, and that the
    text cites only source ids of that card or ledger ids."""
    name = layout.TIERS_JSON
    path = root / name
    if not path.is_file():
        return [f"{name}: missing"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except ValueError:
        return [f"{name}: not JSON"]
    if not (isinstance(data, dict) and set(data) == {"version", "placements"} and data["version"] == 1
            and isinstance(data["placements"], dict)):
        return [f"{name}: needs exactly version (1) and placements (an object)"]
    problems: Problems = []
    cards: dict[str, dict[str, Any]] = {}
    for path_ in sorted((root / layout.MODELS_DIR).glob("*/*.json")):
        try:
            card = json.loads(path_.read_text(encoding="utf-8"))
        except ValueError:
            continue  # the cards check reports it
        if isinstance(card, dict):
            cards[path_.stem] = card
    known = ledger_ids(root)
    resolves = repo_resolver(repo_paths(root), layout.APPLICATIONS_DIR)
    for ident, entry in data["placements"].items():
        where = f"{name}: {ident}"
        if ident not in cards:
            problems.append(f"{where}: no card models/<maker>/{ident}.json")
        if not (isinstance(entry, dict) and set(entry) == {"placements", "basis", "notes"}):
            problems.append(f"{where}: needs exactly placements, basis and notes")
            continue
        if not isinstance(entry["placements"], list) or not entry["placements"]:
            problems.append(f"{where}: placements is not a list with a row; a model with none takes the spec tier by the default rule")
        else:
            for index, placement in enumerate(entry["placements"]):
                label = f"{where}: placements[{index}]"
                if not (isinstance(placement, dict) and set(placement) == {"effort", "tier", "confidence"}):
                    problems.append(f"{label} needs exactly effort, tier and confidence")
                    continue
                if placement["effort"] is not None and not _nonempty_text(placement["effort"]):
                    problems.append(f"{label}.effort is not text or null")
                if placement["tier"] not in CARD_TIERS:
                    problems.append(f"{label}.tier is not one of outcome, design, spec")
                if placement["confidence"] not in CARD_CONFIDENCE:
                    problems.append(f"{label}.confidence is not one of high, medium, low")
        if not _nonempty_text(entry["basis"]):
            problems.append(f"{where}: basis is empty; say why, citing source ids or saying it is inferred")
        if not isinstance(entry["notes"], list) or not all(_nonempty_text(n) for n in entry["notes"]):
            problems.append(f"{where}: notes is not a list of text")
            continue
        source_ids = {s.get("id") for s in cards.get(ident, {}).get("sources", []) if isinstance(s, dict)}
        for key, text in _text_fields({"basis": entry["basis"], "notes": entry["notes"]}):
            for count, shown in long_quotations(text):
                problems.append(f"{where}: {key} holds a quotation of {count} words, over {MAX_QUOTE_WORDS}: {shown[:50]}...")
            for hit in unreachable(text, resolves):
                problems.append(f"{where}: {key} cites something a public reader cannot reach ({hit!r}): cite the evidence or say it is inferred")
            for cited in CITATION.findall(text):
                if cited not in source_ids and cited not in known:
                    problems.append(f"{where}: [{cited}] is cited but is neither a source id of the card nor a ledger id")
    return problems


def check_generated(root: Path) -> Problems:
    try:
        wanted = render.render_all(root)
    except Exception as error:  # a card of the wrong shape: report it, and let the other checks run
        return [f"cannot render: {type(error).__name__}: {error}"]
    problems = []
    for name, text in wanted.items():
        path = root / name
        if not path.is_file():
            problems.append(f"{name}: missing; run `make render`")
        elif path.read_text(encoding="utf-8") != text:
            problems.append(f"{name}: differs from what scripts/render.py renders; run `make render`")
    return problems


INDEX_ROW = re.compile(r"^\| \[([^\]]+)\]\(([^)]+)\) \| (.*) \| (.*) \| (.*) \| (.*) \|$")


def check_index(root: Path) -> Problems:
    index = root / "INDEX.md"
    if not index.is_file():
        return ["INDEX.md: missing"]
    docs = {rel(root, p): p for p in research_docs(root)}
    listed: dict[str, list[str]] = {}
    problems = []
    for number, line in enumerate(index.read_text(encoding="utf-8").split("\n"), 1):
        if not line.startswith("| ["):
            continue
        match = INDEX_ROW.match(line)
        if not match:
            problems.append(f"INDEX.md:{number}: a row is not `| [path](path) | title | scope | last_checked | volatility |`")
            continue
        label, target, title, scope, checked, volatility = match.groups()
        if label != target:
            problems.append(f"INDEX.md:{number}: link text {label!r} is not its target {target!r}")
        if target in listed:
            problems.append(f"INDEX.md:{number}: {target} is listed twice")
        listed[target] = [title, scope, checked, volatility]
        if target not in docs:
            problems.append(f"INDEX.md:{number}: {target} is not a research document")
            continue
        parsed = parse_frontmatter(docs[target].read_text(encoding="utf-8"))
        if parsed is None:
            continue  # the frontmatter check reports it
        data, body = parsed
        if title != (title_of(body) or ""):
            problems.append(f"INDEX.md:{number}: {target} title differs from its `# ` title")
        if not scope.strip():
            problems.append(f"INDEX.md:{number}: {target} has no scope")
        if checked != data.get("last_checked"):
            problems.append(f"INDEX.md:{number}: {target} last_checked is {data.get('last_checked')}, not {checked}")
        if volatility != volatility_class(str(data.get("volatility", ""))):
            problems.append(f"INDEX.md:{number}: {target} volatility class differs from its frontmatter")
    problems.extend(f"INDEX.md: {name} is not listed" for name in sorted(set(docs) - set(listed)))
    return problems


LINK = re.compile(r"(?<!\\)!?\[(?:[^\]\\]|\\.)*\]\(\s*<?([^)>\s]+)>?(?:\s+\"[^\"]*\")?\s*\)")


CODE_SPAN = re.compile(r"(?<!\\)`([^`\n]*(?:\n(?!\s*\n)[^`\n]*)*)`")


def strip_code(text: str, keep_spans: bool = True) -> str:
    """The text with fenced blocks blanked and inline code spans reduced to their content, or
    removed when keep_spans is false. Line numbers do not move."""
    out, in_fence = [], False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append("")
        else:
            out.append("" if in_fence else line)
    joined = "\n".join(out)
    if keep_spans:
        return CODE_SPAN.sub(lambda m: m.group(1).replace('"', ""), joined)
    return CODE_SPAN.sub(lambda m: "\n" * m.group(1).count("\n"), joined)


def heading_slugs(text: str) -> set[str]:
    """The anchors GitHub gives the headings of a Markdown file."""
    slugs: set[str] = set()
    counts: dict[str, int] = {}
    in_fence = False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        match = None if in_fence else re.match(r"#{1,6}\s+(.*?)\s*#*\s*$", line)
        if not match:
            continue
        heading = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", match.group(1))
        heading = re.sub(r"[`*]", "", heading).lower()
        slug = re.sub(r"[^\w\- ]", "", heading).replace(" ", "-")
        n = counts.get(slug, 0)
        counts[slug] = n + 1
        slugs.add(slug if n == 0 else f"{slug}-{n}")
    return slugs


def exists_exact(root: Path, destination: Path) -> bool:
    """Whether the path exists with the letter case it is written in, as on GitHub and Linux; a
    case-insensitive file system, such as the default on macOS, would accept a different case."""
    current = root
    for part in destination.relative_to(root).parts:
        try:
            if part not in os.listdir(current):
                return False
        except OSError:
            return False
        current = current / part
    return True


def check_links(root: Path) -> Problems:
    problems = []
    slug_cache: dict[Path, set[str]] = {}
    for path in markdown_files(root):
        text = path.read_text(encoding="utf-8")
        for number, line in enumerate(strip_code(text, keep_spans=False).split("\n"), 1):
            for match in LINK.finditer(line):
                target = match.group(1)
                if re.match(r"[A-Za-z][A-Za-z0-9+.-]*:", target):
                    continue
                file_part, _, anchor = target.partition("#")
                destination = path if not file_part else (path.parent / file_part).resolve()
                where = f"{rel(root, path)}:{number}"
                try:
                    destination.relative_to(root.resolve())
                except ValueError:
                    problems.append(f"{where}: link {target} leaves the repository")
                    continue
                if not exists_exact(root.resolve(), destination):
                    problems.append(f"{where}: link {target} does not resolve")
                elif anchor and destination.suffix == ".md":
                    if destination not in slug_cache:
                        slug_cache[destination] = heading_slugs(destination.read_text(encoding="utf-8"))
                    if anchor.lower() not in slug_cache[destination]:
                        problems.append(f"{where}: link {target} names a heading that does not exist")
    return problems


LIST_ITEM = re.compile(r"^\s*([-*+]|\d+[.)])\s")
# A quotation is text between quotation marks of any common style:
#   straight double quotes (a closing one may carry one letter, a possessive s),
#   curly double quotes, curly single quotes, straight single quotes, guillemets, low-9 double
#   quotes (German) and corner brackets.
# An opening straight single quote must not follow a letter or digit and a closing one must not
# precede one, so an apostrophe inside a word ("model's", "don't") never opens or closes a
# quotation. A curly single quote closes only where it is not an apostrophe inside a word.
QUOTED = re.compile(
    r"(?<![\w\"])\"(?=\S)(.+?)(?<=\S)\"(?!\"|\w\w)"
    r"|\u201c([^\u201d]+)\u201d"
    r"|\u2018(.+?)\u2019(?!\w)"
    r"|(?<![\w'])'(?=\S)(.+?)(?<=\S)'(?![\w'])"
    r"|\u00ab([^\u00bb]+)\u00bb"
    r"|\u201e([^\u201c\u201d]+)[\u201c\u201d]"
    r"|\u300c([^\u300d]+)\u300d"
)


def prose_segments(text: str) -> list[tuple[int, str]]:
    """(first line number, text) for each paragraph, list item and table row outside code."""
    body = strip_code(re.sub(r"\A---\n.*?\n---\n", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.DOTALL))
    segments: list[tuple[int, str]] = []
    current: list[str] = []
    start = 0
    for number, line in enumerate(body.split("\n"), 1):
        if not line.strip() or line.startswith(("|", "#")) or LIST_ITEM.match(line):
            if current:
                segments.append((start, " ".join(current)))
                current = []
            if line.strip() and not line.startswith("#"):
                current, start = [line.strip()], number
            continue
        if not current:
            start = number
        current.append(line.strip())
    if current:
        segments.append((start, " ".join(current)))
    return segments


def long_quotations(text: str) -> list[tuple[int, str]]:
    """(word count, text) of each quotation in the text that is over the limit."""
    found = []
    for match in QUOTED.finditer(text):
        quoted = next(group for group in match.groups() if group)
        if words(quoted) > MAX_QUOTE_WORDS:
            found.append((words(quoted), quoted))
    return found


def check_quotes(root: Path) -> Problems:
    problems = []
    for path in markdown_files(root):
        for number, segment in prose_segments(path.read_text(encoding="utf-8")):
            where = f"{rel(root, path)}:{number}"
            for count, quoted in long_quotations(segment):
                problems.append(f"{where}: quotation of {count} words, over {MAX_QUOTE_WORDS}: {quoted[:50]}...")
            # A verbatim excerpt set as a blockquote may carry no quotation marks. A banner or note
            # of our own starts with a bold label; any other blockquote is held to the limit too.
            if segment.startswith(">") and not segment.startswith("> **"):
                count = len([token for token in segment.split() if token != ">"])
                if count > MAX_QUOTE_WORDS:
                    problems.append(f"{where}: blockquote of {count} words, over {MAX_QUOTE_WORDS}, without a bold label: paraphrase it or start it with one")
    return problems


QUEUE_NAME = re.compile(r"([0-9]{8})-([0-9a-f]{64})\.json")


def check_queue(root: Path, today: dt.date) -> Problems:
    problems = []
    queue = root / "ingest" / "queue"
    for path in sorted(queue.glob("*")) if queue.is_dir() else []:
        if path.name == ".gitkeep":
            continue
        if not path.is_file():
            problems.append(f"{rel(root, path)}: not a file; the queue holds only finding files")
            continue
        named = QUEUE_NAME.fullmatch(path.name)
        if not named:
            problems.append(f"{rel(root, path)}: a queue file is named <YYYYMMDD>-<64 hex digits of the sha256>.json")
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                recorded = data.get("sha256")
                data = {k: v for k, v in data.items() if k not in ("collected_on", "sha256")}
            collect.validate_finding(data, today)
            expected = collect.digest(data["claim"], data["url"])
            if recorded != expected:
                problems.append(f"{rel(root, path)}: sha256 is not the digest of its claim and url")
            elif named and named.group(2) != expected:
                problems.append(f"{rel(root, path)}: the name does not carry the digest of its claim and url")
        except (collect.Refused, ValueError) as reason:
            problems.append(f"{rel(root, path)}: {reason}")
        except OSError as error:
            problems.append(f"{rel(root, path)}: cannot be read: {error.strerror}")
    seen = root / "ingest" / "seen.jsonl"
    if seen.is_file():
        try:
            lines = seen.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError) as error:
            problems.append(f"ingest/seen.jsonl: cannot be read as UTF-8 text: {getattr(error, 'strerror', None) or error}")
            lines = []
        for number, line in enumerate(lines, 1):
            if line.strip():
                try:
                    collect.seen_digest(line, f"ingest/seen.jsonl:{number}")
                except ValueError as reason:
                    problems.append(str(reason))
    return problems


def scrub_targets(root: Path) -> list[Path]:
    """Every file that can be published, and every symbolic link (Git can commit one): `.agents/`
    is the ignored workspace, except `.agents/skills/`, which is committed. Nothing below a linked
    folder is listed; the link itself is."""
    skip = {".git", "__pycache__", "node_modules", ".venv"}
    found = []
    for path in root.rglob("*"):
        parts = path.relative_to(root).parts
        if parts[:1] == (".agents",) and parts[1:2] != ("skills",):
            continue
        if set(parts) & skip or any((root.joinpath(*parts[:n])).is_symlink() for n in range(1, len(parts))):
            continue
        if path.is_symlink() or path.is_file():
            found.append(path)
    return sorted(found)


def published_texts(root: Path) -> list[tuple[Path, str]]:
    """(path, text) of each file that can be published and reads as UTF-8; links are skipped (the
    symlinks check reports them)."""
    found = []
    for path in scrub_targets(root):
        if path.is_symlink():
            continue
        try:
            found.append((path, path.read_text(encoding="utf-8")))
        except (UnicodeDecodeError, OSError):
            continue
    return found


def check_symlinks(root: Path) -> Problems:
    return [f"{rel(root, path)}: a symbolic link; commit the file itself" for path in scrub_targets(root) if path.is_symlink()]


def _is_emoji(char: str) -> bool:
    """Whether a variation selector 16 (U+FE0F) after this character asks for an emoji: a symbol
    (category So), or a keycap base."""
    return unicodedata.category(char) == "So" or char in "#*0123456789"


def invisible_chars(text: str) -> list[tuple[int, int]]:
    """(line number, code point) of each invisible or format character in the text: category Cf,
    a variation selector (U+FE00-FE0F, U+E0100-E01EF) or a tag character (U+E0000-E007F). U+FE0F
    directly after an emoji is allowed."""
    found = []
    for number, line in enumerate(text.split("\n"), 1):
        for index, char in enumerate(line):
            code = ord(char)
            if code == 0xFE0F and index > 0 and _is_emoji(line[index - 1]):
                continue
            if (
                unicodedata.category(char) == "Cf"
                or 0xFE00 <= code <= 0xFE0F
                or 0xE0100 <= code <= 0xE01EF
                or 0xE0000 <= code <= 0xE007F
            ):
                found.append((number, code))
    return found


def check_invisible(root: Path) -> Problems:
    return [
        f"{rel(root, path)}:{number}: invisible or format character U+{code:04X}"
        for path, text in published_texts(root)
        for number, code in invisible_chars(text)
    ]


def check_scrub(root: Path, denylist: Path | None) -> Problems | None:
    """None when there is no local scrub list to apply; the hits otherwise (file and line, never the
    term)."""
    patterns = collect.load_denylist(denylist)
    if not patterns:
        return None
    problems = []
    for path, text in published_texts(root):
        for number, line in enumerate(text.split("\n"), 1):
            if collect.matches_denylist(line, patterns):
                problems.append(f"{rel(root, path)}:{number}: matches the local scrub list")
    return problems


PENDING_LISTED = 20  # files named in the output before the rest is counted


def check_pending(root: Path) -> Problems:
    """One line for each file that still holds the stub placeholder, with how many lines hold it."""
    problems = []
    for path, text in published_texts(root):
        count = sum(1 for line in text.split("\n") if layout.PENDING in line)
        if count:
            problems.append(f"{rel(root, path)}: {count} line(s) hold the placeholder")
    return problems


def scope_list(root: Path) -> list[str]:
    """Model classes with cards of more than two generations (FORMAT.md keeps two). Printed, not gated."""
    generations: dict[tuple[str, str], set[str]] = {}
    for path in sorted((root / layout.MODELS_DIR).glob("*/*.json")):
        try:
            card = json.loads(path.read_text(encoding="utf-8"))
        except ValueError:
            continue
        if isinstance(card, dict) and isinstance(card.get("class"), str) and isinstance(card.get("generation"), str):
            generations.setdefault((str(card.get("maker")), card["class"]), set()).add(card["generation"])
    return [
        f"{maker} {klass}: {len(found)} generations ({', '.join(sorted(found))})"
        for (maker, klass), found in sorted(generations.items())
        if len(found) > 2
    ]


def stale_list(root: Path, today: dt.date) -> list[str]:
    """Documents and cards past the window for their volatility, oldest first. Printed, not gated."""
    rows: list[tuple[int, str]] = []
    for path in research_docs(root):
        parsed = parse_frontmatter(path.read_text(encoding="utf-8"))
        if not parsed or not is_date(parsed[0].get("last_checked")):
            continue
        klass = volatility_class(str(parsed[0].get("volatility", "")))
        if klass is None:
            continue
        rows.append(_stale_row(rel(root, path), str(parsed[0]["last_checked"]), klass, today))
    for path in sorted((root / layout.MODELS_DIR).glob("*/*.json")):
        try:
            card = json.loads(path.read_text(encoding="utf-8"))
        except ValueError:
            continue
        if isinstance(card, dict) and is_date(card.get("checked")):
            rows.append(_stale_row(rel(root, path), card["checked"], "VOLATILE", today))
    return [text for over, text in sorted(rows, reverse=True) if over > 0]


def _stale_row(name: str, checked: str, klass: str, today: dt.date) -> tuple[int, str]:
    age = (today - dt.date.fromisoformat(checked)).days
    over = age - VOLATILITY_WINDOWS[klass]
    return over, f"{name}: checked {checked} ({age} days ago), {klass} window {VOLATILITY_WINDOWS[klass]} days, {over} over"


# ---------------------------------------------------------------------------------------------


def run(
    root: Path,
    today: dt.date,
    denylist: Path | None,
    out: Callable[[str], None] = print,
    allow_pending: bool = False,
) -> int:
    failures = 0
    areas: list[tuple[str, Callable[[], Problems | None]]] = [
        ("frontmatter", lambda: check_frontmatter(root, today)),
        ("ledgers", lambda: check_ledgers(root)),
        ("cards", lambda: check_cards(root, today)),
        ("models", lambda: check_models(root)),
        ("providers", lambda: check_providers(root)),
        ("applications", lambda: check_applications(root)),
        ("generated", lambda: check_generated(root)),
        ("index", lambda: check_index(root)),
        ("links", lambda: check_links(root)),
        ("quotes", lambda: check_quotes(root)),
        ("queue", lambda: check_queue(root, today)),
        ("symlinks", lambda: check_symlinks(root)),
        ("invisible", lambda: check_invisible(root)),
        ("scrub", lambda: check_scrub(root, denylist)),
        ("pending", lambda: check_pending(root)),
    ]
    for name, check in areas:
        problems = check()
        if problems is None:
            if denylist is None:
                reason = f"no local scrub list given (--denylist, or the {collect.DENYLIST_ENV} environment variable)"
            elif denylist.is_file():
                reason = f"no terms in {denylist}"
            else:
                reason = f"no local scrub list at {denylist}"
            out(f"UNVERIFIED {name}: {reason}; nothing was matched")
        elif name == "pending" and problems and allow_pending:
            out(f"UNVERIFIED pending: {len(problems)} file(s) still hold the placeholder; --allow-pending was given, so this is not a failure, and nothing here may ship")
        elif problems:
            shown = problems[:PENDING_LISTED] if name == "pending" else problems
            for problem in shown:
                out(f"  {problem}")
            if len(shown) < len(problems):
                out(f"  ... and {len(problems) - len(shown)} more file(s)")
            out(f"FAIL {name}: {len(problems)} problem(s)")
            failures += 1
        else:
            out(f"PASS {name}")
    stale = stale_list(root, today)
    out(f"stale (printed, not gated): {len(stale)} past their window" if stale else "stale (printed, not gated): none past their window")
    for row in stale:
        out(f"  {row}")
    wide = scope_list(root)
    out(f"scope (printed, not gated): {len(wide)} class(es) with more than two generations" if wide else "scope (printed, not gated): every class holds at most two generations")
    for row in wide:
        out(f"  {row}")
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check the research repository.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--today", type=dt.date.fromisoformat, default=None, help="the date to judge by (YYYY-MM-DD)")
    parser.add_argument(
        "--denylist", type=Path, default=None,
        help=f"the optional local scrub list; default: the file that ${collect.DENYLIST_ENV} names",
    )
    parser.add_argument(
        "--allow-pending", action="store_true",
        help="report files that still hold the stub placeholder as UNVERIFIED instead of FAIL, to run the other checks while stubs remain",
    )
    args = parser.parse_args(argv)
    denylist = args.denylist if args.denylist is not None else collect.default_denylist()
    return run(args.root.resolve(), args.today or dt.date.today(), denylist, allow_pending=args.allow_pending)


if __name__ == "__main__":
    sys.exit(main())
