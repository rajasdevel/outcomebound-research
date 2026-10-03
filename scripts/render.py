#!/usr/bin/env python3
"""Render the generated parts of the research tree from the model cards and the placement data.

    python3 scripts/render.py [--root DIR]

What it renders:

  - the card block of each model file, between the card markers (`models/<maker>/<id>.md`);
  - the table of every model in models/README.md, between the models markers (with a Voice column);
  - the table of every provider in providers/README.md, between the providers markers;
  - applications/implementer-tiers.md, whole, from applications/implementer-tiers.json.

Text outside the markers is never touched. scripts/check.py fails when any of it differs from what
this script renders. A card that has no model file is skipped (check reports it), and a file that
exists but lacks its markers stops the run. It writes only inside the repository root and never
through a symbolic link: a link at any destination, or at a folder above it, stops it before
anything is written. Standard library only; consumers never run this.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import layout
import safefs

# The benchmarks a card block shows first, in this order, matched by name prefix; the card holds
# every other one and the block lists those after them.
KEY_BENCHMARKS = (
    "SWE-Bench Pro",
    "Terminal-Bench",
    "Artificial Analysis Intelligence Index",
    "Artificial Analysis Coding Agent Index",
    "METR",
)


def card_files(root: Path) -> list[tuple[str, dict[str, Any]]]:
    """Every card under models/<maker>/*.json as (path relative to root, card), sorted for rendering.

    A file that is not a JSON object raises ValueError naming the path; scripts/check.py reports
    that before it renders.
    """
    found: list[tuple[str, dict[str, Any]]] = []
    for path in sorted((root / layout.MODELS_DIR).glob("*/*.json")):
        name = path.relative_to(root).as_posix()
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            raise ValueError(f"{name}: not readable JSON: {error}") from error
        if not isinstance(data, dict):
            raise ValueError(f"{name}: not a JSON object")
        found.append((name, data))
    return sorted(found, key=lambda entry: _sort_key(entry[1]))


def load_cards(root: Path) -> list[dict[str, Any]]:
    return [card for _, card in card_files(root)]


def _sort_key(card: dict[str, Any]) -> tuple[str, str, str]:
    released = str(card.get("released") or "")
    # Newest first within a maker: invert the ISO date's digits.
    inverted = "".join(str(9 - int(c)) if c.isdigit() else c for c in released)
    return (str(card.get("maker", "")).casefold(), inverted, str(card.get("id", "")))


def _cell(text: object) -> str:
    """One table cell: a single line with pipes escaped."""
    return str(text).replace("\\", "\\\\").replace("|", "\\|").replace("\n", " ").strip()


def _tokens(value: object) -> str:
    if not isinstance(value, int) or isinstance(value, bool):
        return "unknown"
    if value >= 1_000_000 and value % 100_000 == 0:
        return f"{value / 1_000_000:g}M"
    if value % 1000 == 0:
        return f"{value // 1000}k"
    return f"{value:,}"


def _price(card: dict[str, Any]) -> str:
    pricing = card.get("pricing_usd_per_mtok")
    if not isinstance(pricing, dict):
        return "unknown"
    low, high = pricing.get("input"), pricing.get("output")
    if low is None or high is None:
        # A voice model is often priced per minute or per character: its notes say the unit.
        if card.get("voice") is not None and pricing.get("notes"):
            return f"unknown per Mtok; {pricing['notes']}"
        return "unknown"
    text = f"${low:g} in / ${high:g} out per Mtok"
    if pricing.get("cached_input") is not None:
        text += f"; cached input ${pricing['cached_input']:g}"
    if pricing.get("notes"):
        text += f"; {pricing['notes']}"
    return text


def _reasoning(card: dict[str, Any]) -> str:
    reasoning = card.get("reasoning")
    if not isinstance(reasoning, dict):
        return "unknown"
    control = str(reasoning.get("control") or "unknown")
    levels = reasoning.get("levels") or []
    text = control
    if levels:
        text += ": " + ", ".join(str(level) for level in levels)
    default = reasoning.get("default")
    if default:
        text += f" (default {default})"
    return text


def _voice_value(value: object) -> str:
    """One value of a card's `voice` object as a table cell: lists joined, nothing as unknown."""
    if isinstance(value, list):
        return ", ".join(str(v) for v in value) or "unknown"
    return "unknown" if value is None or value == "" else str(value)


# The rows a card block adds for a voice model, as (row name, key of the card's `voice` object).
VOICE_ROWS = (
    ("Voice duplex", "duplex"), ("Voice input audio", "input_audio"), ("Voice output audio", "output_audio"),
    ("Voices", "voices"), ("Voice languages", "languages"), ("Turn detection", "turn_detection"),
    ("Interruption", "interruption"), ("Voice latency", "latency"), ("Session limit", "session_limit"),
)


def _voice_rows(card: dict[str, Any]) -> list[tuple[str, object]]:
    voice = card.get("voice")
    if not isinstance(voice, dict):
        return []
    return [(name, _voice_value(voice.get(key))) for name, key in VOICE_ROWS]


def _voice_marker(card: dict[str, Any]) -> str:
    """The Voice cell of the models table: `-` for a text model, else the duplex mode."""
    voice = card.get("voice")
    if not isinstance(voice, dict):
        return "-"
    return {"full": "full-duplex voice", "half": "half-duplex voice", "none": "voice, no duplex"}.get(
        str(voice.get("duplex")), "voice"
    )


def _status(card: dict[str, Any]) -> str:
    """The status cell. A retirement date before the card's `checked` date had passed when the card
    was verified, so the cell says "retired <date>" instead of a date still to come."""
    status = str(card.get("status", "unknown"))
    retires = card.get("retires")
    if not retires:
        return status
    checked = card.get("checked")
    if isinstance(checked, str) and str(retires) < checked:
        return f"retired {retires}"
    return f"{status} (retires {retires})"


def _link(url: str, label: str) -> str:
    return f"[{label}]({url.replace('(', '%28').replace(')', '%29')})"


def _source_link(card: dict[str, Any], bench: dict[str, Any]) -> str:
    """A Markdown link to the card source a score rests on; empty when the card has none."""
    for source in card.get("sources") or []:
        if isinstance(source, dict) and source.get("id") == bench.get("source") and source.get("url"):
            return " " + _link(str(source["url"]), str(source["id"]))
    return ""


def _benchmark_text(card: dict[str, Any], bench: dict[str, Any]) -> str:
    detail = ", ".join(str(x) for x in (bench.get("setting"), bench.get("harness"), bench.get("measured_by")) if x)
    return f"{bench.get('name', '')}: {bench['score']}" + (f" ({detail})" if detail else "") + _source_link(card, bench)


def _scored(card: dict[str, Any]) -> list[dict[str, Any]]:
    return [b for b in card.get("benchmarks") or [] if isinstance(b, dict) and b.get("score") is not None]


def _key_benchmarks(card: dict[str, Any]) -> str:
    """Each key benchmark score with the full name the card gives it (version, subset or variant),
    the setting and harness it ran in, who measured it and the source it rests on. Two results
    that differ in any of these stay distinguishable: the name is never cut short."""
    parts = []
    for prefix in KEY_BENCHMARKS:
        for bench in _scored(card):
            if str(bench.get("name", "")).startswith(prefix):
                parts.append(_benchmark_text(card, bench))
    return "; ".join(parts) if parts else "none recorded"


def _other_benchmarks(card: dict[str, Any]) -> str:
    parts = [
        _benchmark_text(card, bench)
        for bench in _scored(card)
        if not str(bench.get("name", "")).startswith(KEY_BENCHMARKS)
    ]
    return "; ".join(parts) if parts else "none recorded"


def _oldest_checked(cards: list[dict[str, Any]]) -> str:
    dates = [str(c["checked"]) for c in cards if c.get("checked")]
    return min(dates) if dates else "none"


def _url_text(value: object) -> str:
    return _link(str(value), str(value).split("://", 1)[-1]) if isinstance(value, str) and value else "unknown"


# ---------------------------------------------------------------------------------------------
# The card block of a model file


def render_card_block(card: dict[str, Any]) -> str:
    """The lines between a model file's card markers, ending with a newline."""
    modalities = card.get("modalities")
    if isinstance(modalities, dict):
        mods = (
            f"input {', '.join(modalities.get('input') or []) or 'none'}; "
            f"output {', '.join(modalities.get('output') or []) or 'none'}"
        )
    else:
        mods = "unknown"
    guides = card.get("prompting_guides") or []
    unknown = card.get("unknown") or []
    context = _tokens(card.get("context_window"))
    max_output = _tokens(card.get("max_output"))
    rows = [
        ("Id", f"`{card.get('id')}`"),
        ("Maker", card.get("maker", "")),
        ("Class", card.get("class") or "unknown"),
        ("Generation", card.get("generation") or "unknown"),
        ("Released", card.get("released") or "unknown"),
        ("Status", _status(card)),
        ("Weights", card.get("weights") or "unknown"),
        ("Access", "; ".join(str(a) for a in card.get("access") or []) or "unknown"),
        ("Context window", context if context == "unknown" else f"{context} tokens"),
        ("Max output", max_output if max_output == "unknown" else f"{max_output} tokens"),
        ("Modalities", mods),
        *_voice_rows(card),
        ("Reasoning control", _reasoning(card)),
        ("Price", _price(card)),
        ("Key benchmarks", _key_benchmarks(card)),
        ("Other benchmarks", _other_benchmarks(card)),
        ("Prompting guides", "; ".join(_url_text(u) for u in guides) if guides else "unknown"),
        ("System card", _url_text(card.get("system_card"))),
        ("Model page", _url_text(card.get("model_page"))),
        ("Card checked", card.get("checked") or "unknown"),
        ("Not found", "; ".join(str(u) for u in unknown) if unknown else "nothing"),
    ]
    out = [
        f"<!-- Generated by scripts/render.py from {card.get('id')}.json; change the card and run `make render`. -->\n",
        "| Field | Value |\n",
        "| --- | --- |\n",
    ]
    out.extend(f"| {name} | {_cell(value)} |\n" for name, value in rows)
    return "".join(out)


def replace_block(text: str, begin: str, end: str, block: str, name: str) -> str:
    """The text with what lies between the one `begin` marker and the one `end` marker replaced by
    `block`; ValueError when the markers are not there exactly once, in that order."""
    if text.count(begin) != 1 or text.count(end) != 1 or text.index(begin) > text.index(end):
        raise ValueError(f"{name}: needs exactly one {begin} marker followed by one {end} marker")
    head, rest = text.split(begin, 1)
    return head + begin + "\n" + block + end + rest.split(end, 1)[1]


# ---------------------------------------------------------------------------------------------
# The two tables


def render_models_table(entries: list[tuple[str, dict[str, Any]]]) -> str:
    """The models table, rows for the (path of the card, card) pairs in the order given."""
    lines = [
        "| Model | Maker | Class | Generation | Status | Released | Voice | File |\n",
        "| --- | --- | --- | --- | --- | --- | --- | --- |\n",
    ]
    for path, card in entries:
        # The file sits next to its card; the link is relative to models/.
        target = path.removeprefix(layout.MODELS_DIR + "/").removesuffix(".json") + ".md"
        cells = [
            card.get("name", card.get("id")),
            card.get("maker", ""),
            card.get("class") or "unknown",
            card.get("generation") or "unknown",
            _status(card),
            card.get("released") or "unknown",
            _voice_marker(card),
            f"[{target}]({target})",
        ]
        lines.append("| " + " | ".join(_cell(c) for c in cells) + " |\n")
    if not entries:
        lines.append("\nNo model cards yet.\n")
    return "".join(lines)


def provider_files(root: Path) -> list[Path]:
    return sorted(
        p for p in (root / layout.PROVIDERS_DIR).glob("*.md")
        if p.relative_to(root).as_posix() != layout.PROVIDERS_README
    )


def provider_kind(text: str) -> str:
    """A provider file's kind: the frontmatter field `kind`, else the first line under the title,
    up to its first semicolon; `unknown` when neither is there."""
    parsed = layout.parse_frontmatter(text)
    if parsed is not None and isinstance(parsed[0].get("kind"), str) and parsed[0]["kind"]:
        return parsed[0]["kind"]
    body = parsed[1] if parsed is not None else text
    seen_title = False
    for line in body.split("\n"):
        if line.startswith("# "):
            seen_title = True
        elif seen_title and line.strip() and not line.startswith("#"):
            return line.split(";", 1)[0].strip().strip("*_ ") or "unknown"
    return "unknown"


def render_providers_table(rows: list[tuple[str, str, str]]) -> str:
    """The providers table for (file name, title, kind) triples: grouped by kind in the order of
    layout.PROVIDER_KINDS (an unlisted kind last), then by title."""

    def order(row: tuple[str, str, str]) -> tuple[int, str, str]:
        kind = row[2]
        index = layout.PROVIDER_KINDS.index(kind) if kind in layout.PROVIDER_KINDS else len(layout.PROVIDER_KINDS)
        return (index, row[1].casefold(), row[0])

    lines = ["| Provider | Kind | File |\n", "| --- | --- | --- |\n"]
    for name, title, kind in sorted(rows, key=order):
        lines.append("| " + " | ".join(_cell(c) for c in (title, kind, f"[{name}]({name})")) + " |\n")
    if not rows:
        lines.append("\nNo provider files yet.\n")
    return "".join(lines)


# ---------------------------------------------------------------------------------------------
# Implementer-tier placements (an application of the base files)

MATCHING_RULES = """\
## How a row is matched

- A row that names no effort covers every effort.
- A row that names "X and above" covers X and every effort above it, in the order of the model's
  `reasoning.levels` on its card.
- An effort below the lowest one a model's rows name takes the next tier down from that row
  (outcome to design, design to spec).
- A model with no card, a model with no row, and any quantisation below 4-bit take the spec tier
  (the default rule).
- A row holds in any harness unless its basis names one.
"""


def load_tiers(root: Path) -> dict[str, Any]:
    """The placement data, or an empty one when the file is not there (check.py reports that)."""
    path = root / layout.TIERS_JSON
    if not path.is_file():
        return {"version": 1, "placements": {}}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise ValueError(f"{layout.TIERS_JSON}: not readable JSON: {error}") from error
    if not isinstance(data, dict) or not isinstance(data.get("placements"), dict):
        raise ValueError(f"{layout.TIERS_JSON}: not an object with a `placements` object")
    return data


def render_tiers(cards: list[dict[str, Any]], tiers: dict[str, Any]) -> str:
    names = {str(c.get("id")): c.get("name", c.get("id")) for c in cards}
    order = [str(c.get("id")) for c in cards]
    placed = tiers.get("placements", {})
    ids = [i for i in order if i in placed] + sorted(i for i in placed if i not in names)
    head = (
        "---\n"
        f"last_checked: {_oldest_checked(cards)}\n"
        "volatility: VOLATILE (generated from the placement data and the model cards; a placement "
        "holds until a new release or a measurement changes it)\n"
        "sources: []\n"
        "generated: true\n"
        "---\n\n"
        "# Implementer tier placements\n\n"
        "Placements are one project's inference, not a ranking of models.\n\n"
        "Which tier of OutcomeBound's hand-off an implementer sits in, by model and effort. The three\n"
        "tiers are named by what the implementer is trusted to decide: outcome, design and spec. A\n"
        "placement is inferred from measured capability and recorded behaviour. One hand-off\n"
        "comparison has tested the tiers so far: entry E17 of OutcomeBound's evaluation record\n"
        "[ob-e17], 63 runs over three small tasks, 9 runs a cell, with one maker and one harness; the\n"
        "whole gain it found was one row of one ticket. Each row holds until a further comparison or a\n"
        "new release says otherwise.\n\n"
        "This is an application of the base files: it reads each model's card at\n"
        "`models/<maker>/<id>.json` (its `reasoning.levels` and `name`) and the model file beside it, and\n"
        "adds a judgement for one use. The file is generated by `scripts/render.py` from\n"
        "[implementer-tiers.json](implementer-tiers.json); change that file and run `make render`, never\n"
        "this one. A note here matters to a hand-off only; what holds for every use of a model is in\n"
        "its own file under [models/](../models/README.md).\n\n"
        + MATCHING_RULES
        + "\n## Placements\n\n"
        "| Model | Effort | Tier | Confidence | Basis | Notes that change a package |\n"
        "| --- | --- | --- | --- | --- | --- |\n"
    )
    rows = []
    for ident in ids:
        entry = placed.get(ident)
        if not isinstance(entry, dict):
            continue
        notes = "; ".join(str(n) for n in entry.get("notes") or [])
        for placement in entry.get("placements") or []:
            cells = [
                names.get(ident, ident),
                placement.get("effort") or "any",
                placement.get("tier", ""),
                placement.get("confidence", ""),
                entry.get("basis", ""),
                notes or "none recorded",
            ]
            rows.append("| " + " | ".join(_cell(c) for c in cells) + " |\n")
    if not rows:
        rows.append("\nNo placements yet; every model takes the spec tier.\n")
    return head + "".join(rows)


# ---------------------------------------------------------------------------------------------


def render_all(root: Path) -> dict[str, str]:
    """The generated text, keyed by repository-relative path. A file that holds hand-written text
    too (a model file, the two README tables) is read, and only the text between its markers
    changes; one that is not there is skipped, and one without its markers raises ValueError."""
    entries = card_files(root)
    cards = [card for _, card in entries]
    out: dict[str, str] = {}

    def read(rel: str) -> str | None:
        path = root / rel
        return path.read_text(encoding="utf-8") if path.is_file() else None

    for path, card in entries:
        rel = path.removesuffix(".json") + ".md"
        text = read(rel)
        if text is not None:
            out[rel] = replace_block(text, layout.CARD_BEGIN, layout.CARD_END, render_card_block(card), rel)
    text = read(layout.MODELS_README)
    if text is not None:
        out[layout.MODELS_README] = replace_block(
            text, layout.MODELS_BEGIN, layout.MODELS_END, render_models_table(entries), layout.MODELS_README
        )
    text = read(layout.PROVIDERS_README)
    if text is not None:
        rows = []
        for file in provider_files(root):
            body = file.read_text(encoding="utf-8")
            parsed = layout.parse_frontmatter(body)
            title = layout.title_of(parsed[1] if parsed else body) or file.stem
            rows.append((file.name, title, provider_kind(body)))
        out[layout.PROVIDERS_README] = replace_block(
            text, layout.PROVIDERS_BEGIN, layout.PROVIDERS_END, render_providers_table(rows), layout.PROVIDERS_README
        )
    out[layout.TIERS_MD] = render_tiers(cards, load_tiers(root))
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render the generated parts of the research tree.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args(argv)
    try:
        files = render_all(args.root)
    except ValueError as error:
        print(f"render: {error}", file=sys.stderr)
        return 1
    try:
        for rel in files:
            safefs.refuse_links(args.root, rel)
        changed = 0
        for rel, text in files.items():
            path = args.root / rel
            if path.is_file() and path.read_text(encoding="utf-8") == text:
                continue
            safefs.write_text(args.root, rel, text)
            changed += 1
        print(f"render: {len(files)} generated file(s) current, {changed} written")
    except OSError as error:
        print(f"render: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
