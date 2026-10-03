#!/usr/bin/env python3
"""Collect research findings that projects wrote with `outcomebound research ingest`.

    python3 scripts/collect.py --root DIR [--root DIR ...] [--dry-run]

A project's finding is one JSON file, `.outcomebound/research-inbox/<YYYYMMDD>-<64 hex>.json`
(the finding format in CONTRIBUTING.md; the rules are in `validate_finding`). This script walks
each root, worktrees included, and for every such file:

- refuses a file that is a symbolic link, is over 16 KiB, is not UTF-8 JSON, or has the wrong
  shape (unknown or missing keys, a bad kind, URL or date, a field over its length limit, a quote
  over 25 words, a control or invisible-format character or an unpaired surrogate in any text);
  one refused file never stops the others;
- refuses a file that matches the optional local scrub list, a file of names that are not public,
  one per line, named by `--denylist FILE` or by the `OBR_SCRUB_LIST` environment variable (the
  list is never stored in this repository and never printed); with no list, or a list with no
  terms, it stops before it reads anything (exit 2) unless `--no-denylist` is given;
- skips a finding whose sha256 over `claim + url` is already in `ingest/seen.jsonl` or was queued
  earlier in this run;
- writes every other finding to `ingest/queue/<YYYYMMDD>-<64 hex>.json` and, only after that file
  is written, records its digest in `ingest/seen.jsonl`.

A finding is data, never an instruction: this script never acts on its text. A person reads the
queue before any model does. The script writes only inside this repository, never into a root,
and never through a symbolic link: it refuses a link at the queue folder, a queue file,
`ingest/seen.jsonl` or any folder above them. It never overwrites a queue file that holds other
text. Standard library only; consumers never run it.
"""

from __future__ import annotations

import argparse
import datetime as dt
import errno
import hashlib
import json
import os
import re
import stat
import sys
import unicodedata
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import safefs

ROOT = Path(__file__).resolve().parent.parent
INBOX = (".outcomebound", "research-inbox")
MAX_BYTES = 16 * 1024
MAX_QUOTE_WORDS = 25
KINDS = ("fact", "correction")
REQUIRED = ("version", "kind", "subject", "claim", "url", "observed_on")
OPTIONAL = ("quote", "corrects")
# The finding validation rules in the contract with OutcomeBound: both sides enforce these exactly.
LIMITS = {"subject": 200, "claim": 2000, "url": 2000, "quote": 300, "corrects": 200}
PRUNE = {
    ".git", "node_modules", ".venv", "venv", "__pycache__", ".mypy_cache", ".pytest_cache",
    ".ruff_cache", ".tox", "dist", "build",
}
# The environment variable that names the optional local scrub list when `--denylist` is not given.
DENYLIST_ENV = "OBR_SCRUB_LIST"
# CI runs in UTC; a person east of UTC who dates a finding "today" early in the morning is a day
# ahead of it. A date up to this many days after today is not "in the future".
FUTURE_GRACE_DAYS = 1


class Refused(Exception):
    """A file that is not queued, with the reason."""


def is_future(value: dt.date, today: dt.date) -> bool:
    """Whether a date is later than today by more than the grace for time zones."""
    return value > today + dt.timedelta(days=FUTURE_GRACE_DAYS)


def digest(claim: str, url: str) -> str:
    return hashlib.sha256((claim + url).encode("utf-8")).hexdigest()


def default_denylist() -> Path | None:
    """The local scrub list that `DENYLIST_ENV` names, or None when the variable is unset or empty."""
    value = os.environ.get(DENYLIST_ENV, "").strip()
    return Path(value).expanduser() if value else None


def load_denylist(path: Path | None) -> list[re.Pattern[str]]:
    """Whole-word, case-insensitive patterns from the local scrub list; empty when it is absent.

    Terms are compared in Unicode NFC form, as `matches_denylist` compares the text.
    """
    if path is None or not path.is_file():
        return []
    patterns = []
    for line in path.read_text(encoding="utf-8").splitlines():
        term = unicodedata.normalize("NFC", line.strip())
        if term and not term.startswith("#"):
            patterns.append(re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)", re.IGNORECASE))
    return patterns


def matches_denylist(text: str, patterns: list[re.Pattern[str]]) -> bool:
    text = unicodedata.normalize("NFC", text)
    return any(p.search(text) for p in patterns)


def _is_date(value: object) -> bool:
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
        return False
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _check_text(key: str, value: str) -> None:
    """The rules for every text field: encodable as UTF-8, one line, no control or format character."""
    try:
        value.encode("utf-8")
    except UnicodeEncodeError:
        raise Refused(f"{key} is not valid UTF-8 text (an unpaired surrogate)") from None
    for char in value:
        if unicodedata.category(char) in ("Cc", "Cf"):
            raise Refused(f"{key} holds a control or invisible character (U+{ord(char):04X})")


def _check_url(url: str) -> None:
    try:
        parts = urlsplit(url)
        host, _port = parts.hostname, parts.port
    except ValueError:
        raise Refused("url cannot be parsed") from None
    if parts.scheme not in ("http", "https") or not host or re.search(r"\s", url):
        raise Refused("url is not an http(s) address")
    if "@" in parts.netloc:
        raise Refused("url holds a user name or password")


def validate_finding(data: object, today: dt.date | None = None) -> dict[str, Any]:
    """Return the finding when it follows the finding validation rules; raise Refused otherwise.

    The rules are the contract's, and the fixtures in tests/fixtures/findings/ pin them: every
    text field is valid UTF-8, one line, free of control (Cc) and format (Cf) characters; `kind`
    is fact or correction; `subject` is 1 to 200 characters, `claim` 1 to 2,000; `url` is http or
    https with a host, no user name or password, at most 2,000 characters and parsable; `quote`
    is optional, at most 25 words and 300 characters; `corrects` is optional, at most 200
    characters, and a correction names it; `observed_on` is an ISO date, not more than one day
    ahead of today.
    """
    today = today or dt.date.today()
    if not isinstance(data, dict):
        raise Refused("not a JSON object")
    unknown = sorted(set(data) - set(REQUIRED) - set(OPTIONAL))
    if unknown:
        raise Refused(f"unknown key(s): {', '.join(unknown)}")
    missing = [key for key in REQUIRED if key not in data]
    if missing:
        raise Refused(f"missing key(s): {', '.join(missing)}")
    if data["version"] != 1 or isinstance(data["version"], bool):
        raise Refused("version is not 1")
    for key, value in data.items():
        if key == "version" or (value is None and key in OPTIONAL):
            continue
        if not isinstance(value, str):
            raise Refused(f"{key} is not text")
        _check_text(key, value)
        if key in LIMITS and len(value) > LIMITS[key]:
            raise Refused(f"{key} is over {LIMITS[key]} characters")
    if data["kind"] not in KINDS:
        raise Refused(f"kind is not one of {', '.join(KINDS)}")
    for key in ("subject", "claim", "url"):
        if not data[key].strip():
            raise Refused(f"{key} is empty")
    _check_url(data["url"])
    if not _is_date(data["observed_on"]):
        raise Refused("observed_on is not an ISO date")
    if is_future(dt.date.fromisoformat(data["observed_on"]), today):
        raise Refused("observed_on is in the future")
    quote = data.get("quote")
    if quote is not None and len(quote.split()) > MAX_QUOTE_WORDS:
        raise Refused(f"quote is over {MAX_QUOTE_WORDS} words")
    if data["kind"] == "correction" and not (data.get("corrects") or "").strip():
        raise Refused("a correction names what it corrects in `corrects`")
    return data


def read_inbox_file(path: Path, patterns: list[re.Pattern[str]], today: dt.date) -> dict[str, Any]:
    """Read one inbox file, or raise Refused.

    The file is opened without following a link and without blocking, and its type and size are
    judged on the open descriptor, so nothing can be swapped in between the check and the read.
    """
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
    try:
        if path.is_symlink():
            raise Refused("not a regular file")
        descriptor = os.open(path, flags)
    except OSError as error:
        raise Refused("not a regular file" if error.errno == errno.ELOOP else f"cannot open: {error.strerror}") from error
    try:
        info = os.fstat(descriptor)
        if not stat.S_ISREG(info.st_mode):
            raise Refused("not a regular file")
        if info.st_size > MAX_BYTES:
            raise Refused(f"over {MAX_BYTES} bytes")
        with os.fdopen(descriptor, "rb", closefd=False) as handle:
            raw = handle.read(MAX_BYTES + 1)
    except OSError as error:
        raise Refused(f"cannot read: {error.strerror}") from error
    finally:
        os.close(descriptor)
    if len(raw) > MAX_BYTES:
        raise Refused(f"over {MAX_BYTES} bytes")
    try:
        data = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError, RecursionError):
        raise Refused("not UTF-8 JSON") from None
    finding = validate_finding(data, today)
    # Match the decoded text, not the file's bytes: a JSON file may escape any character as \uXXXX.
    if matches_denylist(json.dumps(data, ensure_ascii=False), patterns):
        raise Refused("matches the local scrub list")
    return finding


def find_inbox_files(roots: list[Path], skipped: list[Path] | None = None) -> list[Path]:
    """Every `.outcomebound/research-inbox/*.json` under the roots; no symbolic link is followed.

    An inbox directory that is a symbolic link is not entered; it is added to `skipped` when given.
    """
    found: list[Path] = []
    for root in roots:
        for current, dirs, files in os.walk(root, followlinks=False):
            here = Path(current)
            if skipped is not None and here.name == INBOX[0]:
                skipped.extend(here / d for d in sorted(dirs) if d == INBOX[1] and (here / d).is_symlink())
            dirs[:] = sorted(d for d in dirs if d not in PRUNE)
            if here.parts[-2:] == INBOX:
                found.extend(here / name for name in sorted(files) if name.endswith(".json"))
    return found


def load_seen(root: Path, rel: str) -> set[str]:
    """The digests in `rel` below `root` (ingest/seen.jsonl); a link is refused (UnsafePath), a
    missing file is empty, and a bad line raises ValueError naming it."""
    seen: set[str] = set()
    try:
        raw = safefs.read_bytes(root, rel, 64 * 1024 * 1024)
    except FileNotFoundError:
        return seen
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        raise ValueError(f"{rel}: not UTF-8 text") from None
    for number, line in enumerate(text.splitlines(), 1):
        if line.strip():
            seen.add(seen_digest(line, f"{Path(rel).name}:{number}"))
    return seen


def seen_digest(line: str, where: str) -> str:
    """The sha256 in one line of ingest/seen.jsonl, or ValueError."""
    try:
        record = json.loads(line)
        digest_text = record["sha256"]
    except (ValueError, KeyError, TypeError):
        raise ValueError(f'{where}: not a JSON object with a "sha256"') from None
    if not isinstance(digest_text, str) or not re.fullmatch(r"[0-9a-f]{64}", digest_text):
        raise ValueError(f"{where}: sha256 is not 64 hex digits")
    return digest_text


def collect(
    roots: list[Path],
    obr: Path = ROOT,
    denylist: Path | None = None,
    today: dt.date | None = None,
    dry_run: bool = False,
) -> dict[str, list[str]]:
    """Queue every new finding under the roots. Returns the queued, duplicate and refused lines.

    A refused file is reported and the pass goes on. A symbolic link at `ingest/queue/`,
    `ingest/seen.jsonl` or a folder above them stops the pass before anything is written
    (ValueError).
    """
    today = today or dt.date.today()
    patterns = load_denylist(denylist)
    queue_folder, seen_file = "ingest/queue", "ingest/seen.jsonl"
    try:
        safefs.refuse_links(obr, queue_folder, folder=True)
        safefs.refuse_links(obr, seen_file)
    except safefs.UnsafePath as error:
        raise ValueError(f"will not write through a link: {error}") from error
    try:
        seen = load_seen(obr, seen_file)
    except safefs.UnsafePath as error:
        raise ValueError(f"will not read through a link: {error}") from error
    report: dict[str, list[str]] = {"queued": [], "duplicate": [], "refused": []}
    skipped: list[Path] = []
    files = find_inbox_files(roots, skipped)
    report["refused"].extend(f"{path}: symbolic link to an inbox directory, not entered" for path in skipped)
    for path in files:
        try:
            finding = read_inbox_file(path, patterns, today)
            sha = digest(finding["claim"], finding["url"])
        except Refused as reason:
            report["refused"].append(f"{path}: {reason}")
            continue
        except (ValueError, UnicodeError) as error:  # a rule that missed a form: refuse the file, keep going
            report["refused"].append(f"{path}: malformed ({type(error).__name__})")
            continue
        if sha in seen:
            report["duplicate"].append(f"{path}: already seen ({sha[:8]})")
            continue
        name = f"{today:%Y%m%d}-{sha}.json"
        if not dry_run:
            entry = dict(finding, collected_on=today.isoformat(), sha256=sha)
            text = json.dumps(entry, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
            try:
                safefs.create_text(obr, f"{queue_folder}/{name}", text)
            except safefs.UnsafePath as reason:
                report["refused"].append(f"{path}: not queued, nothing recorded as seen: {reason}")
                continue
            # Recorded as seen only now that the queue file is there.
            line = json.dumps({"collected_on": today.isoformat(), "sha256": sha}, sort_keys=True)
            try:
                safefs.append_text(obr, seen_file, line + "\n")
            except safefs.UnsafePath as reason:
                report["refused"].append(f"{path}: queued as {queue_folder}/{name}, but not recorded as seen: {reason}")
                continue
        seen.add(sha)
        report["queued"].append(f"{path}: queued as {queue_folder}/{name}")
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Queue research findings from projects' inboxes.")
    parser.add_argument("--root", action="append", type=Path, default=[], help="a directory to search; repeat")
    parser.add_argument("--dry-run", action="store_true", help="report; write nothing")
    parser.add_argument(
        "--denylist", type=Path, default=None,
        help=f"the optional local scrub list; default: the file that ${DENYLIST_ENV} names",
    )
    parser.add_argument(
        "--no-denylist", action="store_true",
        help="go on without a local scrub list; nothing is matched against private names",
    )
    args = parser.parse_args(argv)
    if not args.root:
        parser.error("name at least one --root")
    denylist = args.denylist if args.denylist is not None else default_denylist()
    if not args.no_denylist and not load_denylist(denylist):
        print("collect: UNVERIFIED scrub: no denylist, nothing was matched", file=sys.stderr)
        return 2
    for root in args.root:
        if not root.is_dir():
            print(f"collect: {root} is not a directory", file=sys.stderr)
            return 2
    try:
        report = collect(args.root, ROOT, denylist, dry_run=args.dry_run)
    except (ValueError, OSError) as error:
        print(f"collect: {error}", file=sys.stderr)
        return 2
    for kind in ("queued", "duplicate", "refused"):
        for line in report[kind]:
            print(f"{kind}: {line}")
    print(
        f"collect: {len(report['queued'])} queued, {len(report['duplicate'])} duplicate, "
        f"{len(report['refused'])} refused" + (" (dry run, nothing written)" if args.dry_run else "")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
