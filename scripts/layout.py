"""The shared parts of the layout: file locations, the headings every file must have, the way
a document's frontmatter and headings are read, and the text of a new (stub) file.

`render.py` writes into the generated blocks, `check.py` enforces the headings and the placeholder
rule, and the tests build small repositories from the stubs. models/FORMAT.md and
providers/README.md describe the same headings in prose; a test compares them with this file.
Standard library only; consumers never run this.
"""

from __future__ import annotations

import re
from typing import Any

# The line a stub holds in each section that nobody has written yet. `make check` fails while any
# file holds it. It is built from two pieces so that this file, which names it, does not hold it.
PENDING = "PENDING-" + "STUB"

MODELS_DIR = "models"
PROVIDERS_DIR = "providers"
APPLICATIONS_DIR = "applications"

MODELS_README = "models/README.md"
PROVIDERS_README = "providers/README.md"
TIERS_JSON = "applications/implementer-tiers.json"
TIERS_MD = "applications/implementer-tiers.md"

CARD_BEGIN = "<!-- card:begin -->"
CARD_END = "<!-- card:end -->"
MODELS_BEGIN = "<!-- models:begin -->"
MODELS_END = "<!-- models:end -->"
PROVIDERS_BEGIN = "<!-- providers:begin -->"
PROVIDERS_END = "<!-- providers:end -->"

# Navigation and format pages: Markdown under a research folder that is not a research document, so
# it has no frontmatter and no row in INDEX.md.
PAGES = frozenset({
    "models/FORMAT.md", "models/README.md", "providers/README.md", "applications/README.md",
})

# Every heading a file of each kind holds, in this order, as (level, text). A file may add headings
# of its own below these; it may not leave one out or move one.
MODEL_HEADINGS: tuple[tuple[int, str], ...] = (
    (2, "At a glance"),
    (2, "How to instruct it"),
    (3, "Setting up the prompt"),
    (3, "Reasoning and effort"),
    (3, "Output: format, length, tone"),
    (3, "Tools and agents"),
    (3, "Coding"),
    (3, "Long context and retrieval"),
    (3, "Structured output"),
    (3, "Images, audio, other inputs"),
    (3, "Sampling and API parameters"),
    (3, "Migrating from the previous generation"),
    (2, "What the system card reports"),
    (2, "Behaviour observed in practice"),
    (2, "Benchmarks"),
    (2, "Open questions"),
    (2, "Sources"),
)
# The subsection a model file adds, right after "Images, audio, other inputs", when its card lists
# audio among the outputs; a file whose card does not must not hold it.
VOICE_HEADING: tuple[int, str] = (3, "Voice: turn-taking, interruption and speech style")
MAKER_HEADINGS: tuple[tuple[int, str], ...] = (
    (2, "Models and lineage"),
    (2, "API surface"),
    (2, "Prompting guides"),
    (2, "System-card practice"),
    (2, "Family-wide behaviour"),
    (2, "Open questions"),
    (2, "Sources"),
)
PROVIDER_HEADINGS: tuple[tuple[int, str], ...] = (
    (2, "Models offered"),
    (2, "API surface"),
    (2, "Feature parity"),
    (2, "Pricing"),
    (2, "Limits and data"),
    (2, "Notes for agents and harnesses"),
    (2, "Sources"),
)
PROVIDER_KINDS = (
    "first-party lab API",
    "cloud platform",
    "router or gateway",
    "inference host",
    "local runtime",
)



def has_audio_output(card: Any) -> bool:
    """Whether the card's `modalities.output` names audio: an entry that is the word `audio`, alone or
    followed by a qualifier in parentheses or after a space."""
    modalities = card.get("modalities") if isinstance(card, dict) else None
    output = modalities.get("output") if isinstance(modalities, dict) else None
    return isinstance(output, list) and any(
        isinstance(entry, str) and re.match(r"audio(?![\w-])", entry.strip(), re.IGNORECASE) for entry in output
    )


def model_headings(voice: bool = False) -> tuple[tuple[int, str], ...]:
    """The headings of a model file in order; with `voice`, the voice subsection after the one on
    images, audio and other inputs."""
    if not voice:
        return MODEL_HEADINGS
    out: list[tuple[int, str]] = []
    for heading in MODEL_HEADINGS:
        out.append(heading)
        if heading == (3, "Images, audio, other inputs"):
            out.append(VOICE_HEADING)
    return tuple(out)


MODEL_VOLATILITY = "VOLATILE (a model's prices, limits, defaults and guidance change at each release)"
MAKER_VOLATILITY = "MONITOR (lineage, guides and API behaviour change at each release)"
PROVIDER_VOLATILITY = "VOLATILE (a provider's catalogue, prices, limits and feature support change often)"


# ---------------------------------------------------------------------------------------------
# Reading a document


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str] | None:
    """The frontmatter's `key: value` and `key:` plus `- item` lines, and the body after it."""
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None
    data: dict[str, Any] = {}
    key = None
    for line in match.group(1).split("\n"):
        item = re.match(r"\s+-\s+(.*)", line)
        if item and key is not None and isinstance(data.get(key), list):
            data[key].append(item.group(1).strip())
            continue
        pair = re.match(r"([A-Za-z_][\w-]*):\s*(.*)", line)
        if not pair:
            continue
        key, value = pair.group(1), pair.group(2).strip()
        data[key] = [] if value in ("", "[]") else value
    return data, text[match.end():]


def title_of(body: str) -> str | None:
    in_fence = False
    for line in body.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence and line.startswith("# "):
            return line[2:].strip()
    return None


def headings(text: str) -> list[tuple[int, str]]:
    """Every `##` to `######` heading of the text outside fenced code, as (level, text)."""
    found = []
    in_fence = False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        match = None if in_fence else re.match(r"(#{2,6})\s+(.*?)\s*#*\s*$", line)
        if match:
            found.append((len(match.group(1)), match.group(2)))
    return found


def missing_headings(text: str, wanted: tuple[tuple[int, str], ...]) -> list[str]:
    """The wanted headings the text lacks or holds out of order, each as `## Heading`."""
    actual = headings(text)
    position = 0
    missing = []
    for level, name in wanted:
        try:
            position = actual.index((level, name), position) + 1
        except ValueError:
            missing.append(f"{'#' * level} {name}")
    return missing


# ---------------------------------------------------------------------------------------------
# New files: every section present, each holding the placeholder until it is written


def _frontmatter(last_checked: str, volatility: str, sources: list[str], kind: str | None = None) -> str:
    lines = ["---", f"last_checked: {last_checked}", f"volatility: {volatility}"]
    if kind:
        lines.append(f"kind: {kind}")
    lines.append("sources:")
    lines.extend(f"  - {url}" for url in sources)
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def _sections(headings_: tuple[tuple[int, str], ...], skip: frozenset[str] = frozenset()) -> str:
    parts = []
    for level, name in headings_:
        parts.append(f"{'#' * level} {name}\n\n")
        if name not in skip:
            parts.append(f"{PENDING}\n\n")
    return "".join(parts)


def model_stub(name: str, last_checked: str, sources: list[str], voice: bool = False) -> str:
    """A model file with every heading, the empty card block and the placeholder in each section.
    `scripts/render.py` fills the block. With `voice`, the file also has the voice subsection."""
    body = f"# {name}\n\n{PENDING}\n\n"
    for level, heading in model_headings(voice):
        body += f"{'#' * level} {heading}\n\n"
        if heading == "At a glance":
            body += f"{CARD_BEGIN}\n{CARD_END}\n\n"
        elif heading != "How to instruct it":
            body += f"{PENDING}\n\n"
    return _frontmatter(last_checked, MODEL_VOLATILITY, sources) + body.rstrip("\n") + "\n"


def maker_stub(title: str, last_checked: str, sources: list[str]) -> str:
    return (
        _frontmatter(last_checked, MAKER_VOLATILITY, sources)
        + f"# {title}\n\n{PENDING}\n\n"
        + _sections(MAKER_HEADINGS).rstrip("\n")
        + "\n"
    )


def provider_stub(title: str, kind: str, last_checked: str, sources: list[str]) -> str:
    return (
        _frontmatter(last_checked, PROVIDER_VOLATILITY, sources, kind)
        + f"# {title}\n\n{PENDING}\n\n"
        + _sections(PROVIDER_HEADINGS).rstrip("\n")
        + "\n"
    )
