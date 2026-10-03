"""Helpers shared by the tests: the scripts on the import path and a minimal valid repository."""

from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(REPO / "scripts"))

import check  # noqa: E402
import collect  # noqa: E402
import layout  # noqa: E402
import render  # noqa: E402
import safefs  # noqa: E402

TODAY = dt.date(2026, 10, 3)
FIXTURE_CARD = json.loads((HERE / "fixtures" / "card.json").read_text(encoding="utf-8"))
FIXTURE_VOICE = {
    "duplex": "full",
    "input_audio": "16-bit PCM, 16 kHz",
    "output_audio": "16-bit PCM, 24 kHz",
    "voices": 8,
    "languages": ["en", "de"],
    "turn_detection": "server-side voice activity detection with a silence setting",
    "interruption": "the user can cut in, and the model stops at once",
    "latency": "about 300 ms to first audio [scale-swe-pro-v2]",
    "session_limit": "30 minutes",
}


def voice_card(**changes: object) -> dict:
    """The fixture card as a voice model: audio among the outputs and a full `voice` object."""
    card = json.loads(json.dumps(FIXTURE_CARD))
    card.update({"id": "example-voice-1", "name": "Example Voice 1", "voice": dict(FIXTURE_VOICE)})
    card["modalities"] = {"input": ["text", "audio"], "output": ["text", "audio"]}
    card.update(changes)
    return card


def write(root: Path, rel: str, text: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def doc_text(title: str = "Example practice", checked: str = "2026-10-01", volatility: str = "STABLE (a test)", body: str = "Body.\n") -> str:
    return (
        f"---\nlast_checked: {checked}\nvolatility: {volatility}\nsources:\n  - https://example.com/source\n---\n\n"
        f"# {title}\n\n{body}"
    )


def ledger_record(ident: str = "example-1", **changes: object) -> dict[str, object]:
    record: dict[str, object] = {
        "id": ident,
        "kind": "practice",
        "claim": "A claim in our words.",
        "quote": "a short quotation",
        "url": "https://example.com/source",
        "verification": "supported",
        "evidence": "lab-guidance",
    }
    record.update(changes)
    return record


def index_rows(root: Path) -> str:
    """A correct INDEX.md for the research documents under root."""
    rows = []
    for path in check.research_docs(root):
        data, body = check.parse_frontmatter(path.read_text(encoding="utf-8")) or ({}, "")
        name = check.rel(root, path)
        klass = check.volatility_class(str(data["volatility"]))
        rows.append(f"| [{name}]({name}) | {check.title_of(body)} | Scope of {name} | {data['last_checked']} | {klass} |")
    return "# Index\n\n| Document | Title | Scope | Last checked | Volatility |\n| --- | --- | --- | --- | --- |\n" + "\n".join(rows) + "\n"


def refresh(root: Path) -> None:
    """Render the generated parts and rewrite INDEX.md to match what is under root."""
    for rel, text in render.render_all(root).items():
        write(root, rel, text)
    write(root, "INDEX.md", index_rows(root))


def written(text: str) -> str:
    """A stub with every section written: the placeholder replaced by a line of text."""
    return text.replace(layout.PENDING, "Written.")


def model_files(root: Path, maker: str = "example-lab", card: dict | None = None) -> None:
    """The card, the model file and the maker README of one model, every section written."""
    card = card or FIXTURE_CARD
    write(root, f"models/{maker}/{card['id']}.json", json.dumps(card, indent=2) + "\n")
    write(root, f"models/{maker}/{card['id']}.md", written(layout.model_stub(card["name"], "2026-10-03", ["https://example.com/s"], voice=layout.has_audio_output(card))))
    if not (root / "models" / maker / "README.md").exists():
        write(root, f"models/{maker}/README.md", written(layout.maker_stub("Example Lab models", "2026-10-03", ["https://example.com/s"])))


def provider_file(root: Path, ident: str = "example-host", title: str = "Example Host", kind: str = "inference host") -> None:
    write(root, f"providers/{ident}.md", written(layout.provider_stub(title, kind, "2026-10-03", ["https://example.com/s"])))


def build_repo(root: Path, with_card: bool = True) -> Path:
    """A minimal repository on which every check passes."""
    write(root, "practices/example.md", doc_text())
    write(root, "models/FORMAT.md", "# Model card format\n")
    write(root, layout.MODELS_README, f"# Models\n\n{layout.MODELS_BEGIN}\n{layout.MODELS_END}\n")
    write(root, layout.PROVIDERS_README, f"# Providers\n\n{layout.PROVIDERS_BEGIN}\n{layout.PROVIDERS_END}\n")
    write(root, "applications/README.md", "# Applications\n")
    write(root, layout.TIERS_JSON, (HERE / "fixtures" / "tiers.json").read_text(encoding="utf-8"))
    write(root, "_evidence/2026-09-25.jsonl", json.dumps(ledger_record()) + "\n")
    provider_file(root)
    if with_card:
        model_files(root)
    else:
        write(root, layout.TIERS_JSON, json.dumps({"version": 1, "placements": {}}) + "\n")
    refresh(root)
    return root


def run_check(root: Path, denylist: Path | None = None, today: dt.date = TODAY, allow_pending: bool = False) -> tuple[int, list[str]]:
    lines: list[str] = []
    code = check.run(root, today, denylist, out=lines.append, allow_pending=allow_pending)
    return code, lines
