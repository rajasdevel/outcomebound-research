"""scripts/check.py: each check passes on a valid repository and fails, with a clear line, on a broken one."""

from __future__ import annotations

import copy
import datetime as dt
import json
import re
import tempfile
import unittest
from pathlib import Path

from tests.support import (
    FIXTURE_CARD,
    FIXTURE_VOICE,
    HERE,
    REPO,
    TODAY,
    build_repo,
    check,
    collect,
    doc_text,
    index_rows,
    layout,
    ledger_record,
    model_files,
    provider_file,
    refresh,
    render,
    run_check,
    voice_card,
    write,
)

CARD_PATH = "models/example-lab/example-model-1.json"
MODEL_PATH = "models/example-lab/example-model-1.md"
TIERS_PATH = "applications/implementer-tiers.json"


class RepoCase(unittest.TestCase):
    """A fresh valid repository in self.root for each test."""

    with_card = True

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = build_repo(Path(self._tmp.name), with_card=self.with_card)

    def verdicts(self, **kwargs: object) -> tuple[int, dict[str, str], list[str]]:
        code, lines = run_check(self.root, **kwargs)  # type: ignore[arg-type]
        verdict = {}
        for line in lines:
            match = re.match(r"(PASS|FAIL|UNVERIFIED) (\w+)", line)
            if match:
                verdict[match.group(2)] = match.group(1)
        return code, verdict, lines

    def assertFails(self, area: str, message: str) -> list[str]:
        code, verdict, lines = self.verdicts()
        self.assertEqual(code, 1, "\n".join(lines))
        self.assertEqual(verdict[area], "FAIL", "\n".join(lines))
        problems = [line.strip() for line in lines if line.startswith("  ") and not line.startswith("  stale")]
        self.assertTrue(any(message in p for p in problems), f"{message!r} not in {problems}")
        return problems

    def write_card(self, **changes: object) -> None:
        """Write the card as given, without rendering (the renderer cannot take a bad shape)."""
        card = copy.deepcopy(FIXTURE_CARD)
        card.update(changes)
        write(self.root, CARD_PATH, json.dumps(card, indent=2) + "\n")

    def set_card(self, **changes: object) -> None:
        card = copy.deepcopy(FIXTURE_CARD)
        card.update(changes)
        write(self.root, CARD_PATH, json.dumps(card, indent=2) + "\n")
        refresh(self.root)


class PassingRepositoryTest(RepoCase):
    def test_every_check_passes(self) -> None:
        code, verdict, lines = self.verdicts()
        self.assertEqual(code, 0, "\n".join(lines))
        self.assertEqual(
            verdict,
            {
                "frontmatter": "PASS", "ledgers": "PASS", "cards": "PASS", "models": "PASS", "providers": "PASS",
                "applications": "PASS", "generated": "PASS", "index": "PASS", "links": "PASS", "quotes": "PASS",
                "queue": "PASS", "symlinks": "PASS", "invisible": "PASS", "scrub": "UNVERIFIED", "pending": "PASS",
            },
        )

    def test_the_format_page_example_is_a_valid_card(self) -> None:
        text = (REPO / "models" / "FORMAT.md").read_text(encoding="utf-8")
        match = re.search(r"```json\n(.*?)\n```", text, re.DOTALL)
        self.assertIsNotNone(match)
        card = json.loads(match.group(1))  # type: ignore[union-attr]
        self.assertEqual(check.card_problems(card, card["id"], set(), TODAY), [])
        self.assertEqual(set(card), set(check.CARD_KEYS))

    def test_the_format_page_templates_hold_the_headings_the_check_enforces(self) -> None:
        text = (REPO / "models" / "FORMAT.md").read_text(encoding="utf-8")
        blocks = re.findall(r"```text\n(.*?)\n```", text, re.DOTALL)
        self.assertEqual(len(blocks), 2)
        found = [
            [(len(m.group(1)), m.group(2)) for m in (re.match(r"(#{2,3}) (.*)", line) for line in block.split("\n")) if m]
            for block in blocks
        ]
        self.assertEqual(found, [list(layout.MODEL_HEADINGS), list(layout.MAKER_HEADINGS)])

    def test_the_providers_page_template_holds_the_headings_the_check_enforces(self) -> None:
        text = (REPO / "providers" / "README.md").read_text(encoding="utf-8")
        block = re.search(r"```text\n(.*?)\n```", text, re.DOTALL).group(1)  # type: ignore[union-attr]
        found = [(2, m.group(1)) for m in (re.match(r"## (.*)", line) for line in block.split("\n")) if m]
        self.assertEqual(found, list(layout.PROVIDER_HEADINGS))
        for kind in layout.PROVIDER_KINDS:
            self.assertIn(f"| {kind} |", text)

    def test_the_fixture_card_is_valid(self) -> None:
        self.assertEqual(check.card_problems(FIXTURE_CARD, "example-model-1", set(), TODAY), [])


class EmptyRepositoryTest(RepoCase):
    with_card = False

    def test_no_cards_renders_empty_tables_and_passes(self) -> None:
        code, verdict, lines = self.verdicts()
        self.assertEqual(code, 0, "\n".join(lines))
        self.assertEqual(verdict["cards"], "PASS")
        self.assertIn("No model cards yet.", (self.root / "models/README.md").read_text(encoding="utf-8"))


class FrontmatterTest(RepoCase):
    def test_no_frontmatter(self) -> None:
        write(self.root, "practices/example.md", "# Example practice\n\nBody.\n")
        self.assertFails("frontmatter", "practices/example.md: no frontmatter")

    def test_undated_and_malformed_dates(self) -> None:
        for value in ("soon", "2026-13-40", "2026-10-1"):
            write(self.root, "practices/example.md", doc_text(checked=value))
            self.assertFails("frontmatter", "practices/example.md: last_checked is missing or not an ISO date")

    def test_a_date_in_the_future(self) -> None:
        write(self.root, "practices/example.md", doc_text(checked="2026-10-05"))
        self.assertFails("frontmatter", "last_checked 2026-10-05 is in the future")

    def test_tomorrow_is_allowed_for_a_time_zone_ahead_of_the_runner(self) -> None:
        write(self.root, "practices/example.md", doc_text(checked="2026-10-04"))
        refresh(self.root)
        self.assertEqual(self.verdicts()[1]["frontmatter"], "PASS")

    def test_last_checked_none_is_for_generated_files_only(self) -> None:
        write(self.root, "practices/example.md", doc_text(checked="none"))
        self.assertFails("frontmatter", "practices/example.md: last_checked is missing or not an ISO date")

    def test_volatility_must_start_with_a_class(self) -> None:
        write(self.root, "practices/example.md", doc_text(volatility="slow-moving"))
        self.assertFails("frontmatter", "volatility must start with STABLE, MONITOR or VOLATILE")

    def test_sources_are_required_and_must_be_urls(self) -> None:
        write(self.root, "practices/example.md", "---\nlast_checked: 2026-10-01\nvolatility: STABLE\n---\n\n# T\n")
        self.assertFails("frontmatter", "sources is missing")
        write(self.root, "practices/example.md", doc_text().replace("https://example.com/source", "a book"))
        self.assertFails("frontmatter", "does not start with an http(s) url")

    def test_a_source_may_carry_a_read_date_after_the_url(self) -> None:
        write(self.root, "practices/example.md", doc_text().replace("https://example.com/source", "https://example.com/s (2026-07-24)"))
        refresh(self.root)
        self.assertEqual(self.verdicts()[1]["frontmatter"], "PASS")

    def test_the_navigation_and_format_pages_need_no_frontmatter_and_every_other_page_does(self) -> None:
        for page in sorted(layout.PAGES):
            self.assertTrue((self.root / page).exists(), page)
        self.assertEqual(self.verdicts()[1]["frontmatter"], "PASS")
        write(self.root, "practices/cards/x.md", "# X\n\nNo frontmatter.\n")
        self.assertFails("frontmatter", "practices/cards/x.md: no frontmatter")
        (self.root / "practices/cards/x.md").unlink()
        write(self.root, "applications/other.md", "# Other\n")
        self.assertFails("frontmatter", "applications/other.md: no frontmatter")

    def test_a_model_file_and_a_maker_readme_need_frontmatter(self) -> None:
        write(self.root, MODEL_PATH, "# Example Model 1\n")
        self.assertFails("frontmatter", f"{MODEL_PATH}: no frontmatter")
        write(self.root, "models/example-lab/README.md", "# Maker\n")
        self.assertFails("frontmatter", "models/example-lab/README.md: no frontmatter")

    def test_a_title_is_required(self) -> None:
        write(self.root, "practices/example.md", doc_text().replace("# Example practice", "Example practice"))
        self.assertFails("frontmatter", "no `# ` title")


class LedgerTest(RepoCase):
    def ledger(self, name: str, *records: object) -> None:
        write(self.root, f"_evidence/{name}.jsonl", "".join(json.dumps(r) + "\n" for r in records))

    def test_a_quote_of_25_words_passes_and_26_fails(self) -> None:
        self.ledger("2026-09-25", ledger_record(quote=" ".join(["w"] * 25)))
        self.assertEqual(self.verdicts()[1]["ledgers"], "PASS")
        self.ledger("2026-09-25", ledger_record(quote=" ".join(["w"] * 26)))
        self.assertFails("ledgers", "_evidence/2026-09-25.jsonl:1 [example-1]: quote is 26 words, over 25")

    def test_required_fields_and_url(self) -> None:
        self.ledger("2026-09-25", ledger_record(url="ftp://example.com/x"))
        self.assertFails("ledgers", "url is missing or not an http(s) address")
        self.ledger("2026-09-25", {"id": "x-1", "kind": "practice", "claim": "c", "url": "https://example.com", "verification": "supported"})
        self.assertFails("ledgers", "quote is missing")
        self.ledger("2026-09-25", ledger_record(verification="maybe"))
        self.assertFails("ledgers", "verification is not supported or overstated")
        self.ledger("2026-09-25", ledger_record(kind="rumour"))
        self.assertFails("ledgers", "kind 'rumour' is not one of")
        self.ledger("2026-09-25", {"kind": "practice"})
        self.assertFails("ledgers", "id is missing or not text")

    def test_a_family_note_needs_no_url_or_quote(self) -> None:
        self.ledger("2026-09-25", {"id": "claude-trend", "kind": "family-note", "family": "claude", "claim": "A note."})
        self.assertEqual(self.verdicts()[1]["ledgers"], "PASS")

    def test_a_line_that_is_not_json(self) -> None:
        write(self.root, "_evidence/2026-09-25.jsonl", "{broken\n")
        self.assertFails("ledgers", "_evidence/2026-09-25.jsonl:1: not JSON")

    def test_an_id_repeated_in_one_file_fails(self) -> None:
        self.ledger("2026-09-25", ledger_record(), ledger_record())
        self.assertFails("ledgers", "id repeats within one file (first at line 1)")

    def test_a_declared_re_verification_repeat_passes(self) -> None:
        self.ledger("2026-09-25", ledger_record())
        self.ledger("2026-09-26", ledger_record(detail="Re-verified."))
        self.assertEqual(self.verdicts()[1]["ledgers"], "PASS")

    def test_a_repeat_with_another_url_is_not_a_re_verification(self) -> None:
        self.ledger("2026-09-25", ledger_record())
        self.ledger("2026-09-26", ledger_record(url="https://example.com/other"))
        self.assertFails("ledgers", "id repeats _evidence/2026-09-25.jsonl with another url")

    def test_a_repeat_twice_in_a_later_file_fails(self) -> None:
        self.ledger("2026-09-25", ledger_record())
        self.ledger("2026-09-26", ledger_record(), ledger_record())
        self.assertFails("ledgers", "_evidence/2026-09-26.jsonl:2 [example-1]: id repeats within one file (first at line 1)")

    def test_a_long_quotation_in_another_text_field_fails_and_a_short_one_passes(self) -> None:
        long = " ".join(["w"] * 26)
        self.ledger("2026-09-25", ledger_record(detail=f'The page says "{long}" and so on.'))
        self.assertFails("ledgers", "[example-1]: detail holds a quotation of 26 words, over 25")
        self.ledger("2026-09-25", ledger_record(claim=f"It says \u201c{long}\u201d."))
        self.assertFails("ledgers", "[example-1]: claim holds a quotation of 26 words")
        self.ledger("2026-09-25", ledger_record(detail='The page says "' + " ".join(["w"] * 25) + '" and so on.'))
        self.assertEqual(self.verdicts()[1]["ledgers"], "PASS")

    def test_a_long_quotation_in_any_quotation_style_fails(self) -> None:
        long = " ".join(["w"] * 26)
        styles = {
            "straight single": f"'{long}'",
            "curly single": f"\u2018{long}\u2019",
            "guillemets": f"\u00ab{long}\u00bb",
            "low-9 double": f"\u201e{long}\u201c",
            "corner brackets": f"\u300c{long}\u300d",
        }
        for name, quoted in styles.items():
            for field in ("claim", "detail", "original_claim"):
                with self.subTest(style=name, field=field):
                    self.ledger("2026-09-25", ledger_record(**{field: f"The source says {quoted} here."}))
                    self.assertFails("ledgers", f"[example-1]: {field} holds a quotation of 26 words, over 25")

    def test_a_straight_single_quoted_passage_over_the_limit_fails(self) -> None:
        claim = "The source ties this to Model A: '" + " ".join(["w"] * 35) + "' Its fix is to soften wording."
        self.ledger("2026-09-25", ledger_record(claim=claim))
        self.assertFails("ledgers", "claim holds a quotation of 35 words, over 25")

    def test_a_quotation_nested_in_a_list_or_an_object_field_is_found(self) -> None:
        long = " ".join(["w"] * 26)
        self.ledger("2026-09-25", ledger_record(notes=[{"text": f"see '{long}'"}]))
        self.assertFails("ledgers", "text holds a quotation of 26 words")

    def test_short_single_quotes_and_apostrophes_pass(self) -> None:
        text = (
            "It's the model's behaviour, the labs' view and don't forget 'a short phrase' or 'another one'. "
            + "word " * 40
            + "isn't a quotation."
        )
        self.ledger("2026-09-25", ledger_record(detail=text, claim="He said '" + " ".join(["w"] * 25) + "'."))
        self.assertEqual(self.verdicts()[1]["ledgers"], "PASS")

    def test_a_ledger_that_is_not_utf8_is_reported(self) -> None:
        (self.root / "_evidence" / "2026-09-26.jsonl").write_bytes(b'{"id": "\xff"}\n')
        self.assertFails("ledgers", "_evidence/2026-09-26.jsonl: cannot be read as UTF-8 text")

    def test_the_sources_file_must_be_json(self) -> None:
        write(self.root, "_evidence/2026-09-25-sources.json", "{")
        self.assertFails("ledgers", "_evidence/2026-09-25-sources.json: not JSON")


class CardTest(RepoCase):
    def problems(self, **changes: object) -> list[str]:
        card = copy.deepcopy(FIXTURE_CARD)
        card.update(changes)
        return check.card_problems(card, "example-model-1", set(), TODAY)

    def test_a_long_quotation_in_a_card_text_field_fails(self) -> None:
        long = " ".join(["w"] * 26)
        for field, change in (
            ("access", {"access": [f"It says '{long}'."]}),
            ("notes", {"pricing_usd_per_mtok": {"input": 1.0, "output": 2.0, "cached_input": None, "notes": f"Advice: \u201c{long}\u201d"}}),
            ("setting", {"benchmarks": [dict(FIXTURE_CARD["benchmarks"][0], setting=f'The doc says "{long}".')]}),
            ("unknown", {"unknown": FIXTURE_CARD["unknown"] + [f"\u00ab{long}\u00bb"]}),
        ):
            with self.subTest(field=field):
                self.assertTrue(any("holds a quotation of 26 words" in p for p in self.problems(**change)), field)
        self.assertEqual(self.problems(), [])
        short = " ".join(["w"] * 25)
        self.assertEqual(self.problems(access=[f"It says '{short}'."]), [])

    def test_a_card_may_not_cite_what_a_public_reader_cannot_reach(self) -> None:
        for phrase in (
            "From notes.md, unchanged.", "Kept from the library table.", "Left until a maintainer rules on it.",
            "The maintainers asked for this.", "A maintainer may prefer the lower row.", "Moved from tiers.md.",
            "Kept as the existing row.", "Taken from OutcomeBound's table.", "See [the notes](notes/plan.txt).",
        ):
            with self.subTest(phrase=phrase):
                unknown = FIXTURE_CARD["unknown"] + [f"model_page: {phrase}"]
                self.assertTrue(any("cannot reach" in p for p in self.problems(unknown=unknown)), phrase)
        self.assertEqual(self.problems(), [])

    def test_ordinary_wording_and_urls_are_not_unreachable(self) -> None:
        for phrase in (
            "The maintainers of the benchmark publish a table.", "See https://example.com/docs/guide.md for the guide.",
            "Read by a model through implementer-tiers.json.",
        ):
            with self.subTest(phrase=phrase):
                unknown = FIXTURE_CARD["unknown"] + [f"model_page: {phrase}"]
                self.assertEqual(self.problems(unknown=unknown), [])

    def test_a_md_name_or_link_in_a_card_must_resolve_in_the_repository(self) -> None:
        write(self.root, "practices/notes.md", doc_text(title="Notes"))
        refresh(self.root)
        self.set_card(unknown=FIXTURE_CARD["unknown"] + ["model_page: see notes.md and [the guide](../../practices/notes.md)"])
        self.assertEqual(self.verdicts()[1]["cards"], "PASS")
        self.set_card(unknown=FIXTURE_CARD["unknown"] + ["model_page: see missing.md"])
        self.assertFails("cards", "cites something a public reader cannot reach ('missing.md')")

    def test_a_source_quote_of_25_words_with_inner_quotes_passes(self) -> None:
        src = copy.deepcopy(FIXTURE_CARD["sources"])
        src[0]["quote"] = 'The page calls it "a good thing" ' + " ".join(["w"] * 15)
        self.assertEqual(self.problems(sources=src), [])

    def test_the_cards_check_names_the_file(self) -> None:
        self.set_card(status="live")
        self.assertFails("cards", f"{CARD_PATH}: status is not one of")

    def test_a_missing_key_and_an_unknown_key(self) -> None:
        card = copy.deepcopy(FIXTURE_CARD)
        del card["class"]
        card["extra"] = 1
        card["tier"] = {}
        self.assertEqual(
            check.card_problems(card, "example-model-1", set(), TODAY),
            ["unknown key(s): extra, tier", "missing key(s): class"],
        )

    def test_the_keys_of_the_v2_card_are_exactly_these(self) -> None:
        self.assertEqual(
            set(check.CARD_KEYS) - set(FIXTURE_CARD), set(), "the fixture lacks a key"
        )
        self.assertEqual(set(FIXTURE_CARD), set(check.CARD_KEYS))
        for removed in ("tier", "prompting", "quirks"):
            self.assertNotIn(removed, check.CARD_KEYS)
        for added in ("class", "generation", "prompting_guides", "system_card", "model_page"):
            self.assertIn(added, check.CARD_KEYS)

    def test_the_old_keys_are_refused(self) -> None:
        card = copy.deepcopy(FIXTURE_CARD)
        card["quirks"] = []
        self.assertIn("unknown key(s): quirks", check.card_problems(card, "example-model-1", set(), TODAY))

    def test_class_generation_and_the_three_links(self) -> None:
        self.assertIn("class is missing or empty", self.problems(**{"class": ""}))
        self.assertIn("generation is not text or null", self.problems(generation=1))
        self.assertIn("generation is not text or null", self.problems(generation=""))
        self.assertIn("system_card is not an http(s) address or null", self.problems(system_card="not a url"))
        self.assertIn("model_page is not an http(s) address or null", self.problems(model_page="ftp://x"))
        self.assertIn("prompting_guides is not a list of http(s) addresses", self.problems(prompting_guides="https://x"))
        self.assertIn("prompting_guides is not a list of http(s) addresses", self.problems(prompting_guides=["nope"]))
        self.assertEqual(self.problems(model_page="https://example.com/page", unknown=FIXTURE_CARD["unknown"][1:]), [])

    def test_a_link_or_generation_not_found_is_null_and_named_in_unknown(self) -> None:
        unknown = FIXTURE_CARD["unknown"]
        for key, value in (("system_card", None), ("prompting_guides", []), ("generation", None)):
            with self.subTest(key=key):
                self.assertIn(f"{key} is empty but `unknown` has no entry starting {key!r}", self.problems(**{key: value}))
                self.assertEqual(self.problems(**{key: value}, unknown=unknown + [f"{key}: not found"]), [])

    def test_enums(self) -> None:
        self.assertIn(
            "reasoning.control is not one of always-on, budget, effort, none, toggle",
            self.problems(reasoning={"control": "magic", "levels": [], "default": None}),
        )
        bad = copy.deepcopy(FIXTURE_CARD["benchmarks"])
        bad[0]["measured_by"] = "rumour"
        self.assertTrue(any("benchmarks[0].measured_by is not one of" in p for p in self.problems(benchmarks=bad)))
        src = copy.deepcopy(FIXTURE_CARD["sources"])
        src[0]["kind"] = "X"
        self.assertTrue(any("sources[0].kind is not one of M, L, P, A" in p for p in self.problems(sources=src)))
        self.assertTrue(any("weights is not" in p for p in self.problems(weights="open")))
        self.assertEqual(self.problems(weights="open (Apache-2.0)"), [])

    def test_dates(self) -> None:
        self.assertIn("released is not an ISO date", self.problems(released="Sept 2026"))
        self.assertIn("retires is not an ISO date", self.problems(retires="2027"))
        self.assertIn("checked is not an ISO date", self.problems(checked="2026-02-30"))
        self.assertIn("checked 2026-10-05 is in the future", self.problems(checked="2026-10-05"))
        self.assertEqual(self.problems(checked="2026-10-04"), [])
        src = copy.deepcopy(FIXTURE_CARD["sources"])
        src[0]["read"] = "2026-10-09"
        self.assertIn("sources[0].read 2026-10-09 is in the future", self.problems(sources=src))

    def test_numbers(self) -> None:
        self.assertIn("context_window is not a positive integer or null", self.problems(context_window="1M"))
        self.assertIn("max_output is not a positive integer or null", self.problems(max_output=0))
        self.assertIn(
            "pricing_usd_per_mtok.input is not a number or null",
            self.problems(pricing_usd_per_mtok={"input": "5", "output": 1, "cached_input": None, "notes": None}),
        )

    def test_the_id_must_match_the_file_name(self) -> None:
        card = copy.deepcopy(FIXTURE_CARD)
        self.assertEqual(check.card_problems(card, "other", set(), TODAY), ["id 'example-model-1' does not match the file name 'other'"])

    def test_every_source_id_cited_must_exist(self) -> None:
        bench = copy.deepcopy(FIXTURE_CARD["benchmarks"])
        bench[0]["source"] = "nowhere"
        self.assertIn("benchmarks[0].source 'nowhere' is not an id in sources", self.problems(benchmarks=bench))
        unknown = FIXTURE_CARD["unknown"] + ["model_page: see [ghost-1]"]
        self.assertIn("[ghost-1] is cited but is neither a source id of this card nor a ledger id", self.problems(unknown=unknown))
        card = copy.deepcopy(FIXTURE_CARD)
        card["unknown"] = unknown
        self.assertEqual(check.card_problems(card, "example-model-1", {"ghost-1"}, TODAY), [])
        card["unknown"] = FIXTURE_CARD["unknown"] + ["model_page: see [scale-swe-pro-v2]"]
        self.assertEqual(check.card_problems(card, "example-model-1", set(), TODAY), [])

    def test_a_ledger_id_is_found_in_the_evidence_files(self) -> None:
        self.set_card(unknown=FIXTURE_CARD["unknown"] + ["model_page: see [example-1]"])
        self.assertEqual(self.verdicts()[1]["cards"], "PASS")

    def test_source_ids_repeat_and_quotes_are_limited(self) -> None:
        src = copy.deepcopy(FIXTURE_CARD["sources"])
        src.append(copy.deepcopy(src[0]))
        self.assertIn("sources[1].id 'scale-swe-pro-v2' repeats", self.problems(sources=src))
        src = copy.deepcopy(FIXTURE_CARD["sources"])
        src[0]["quote"] = " ".join(["w"] * 26)
        self.assertIn("sources[0].quote is not text of at most 25 words", self.problems(sources=src))
        src[0]["quote"] = " ".join(["w"] * 25)
        self.assertEqual(self.problems(sources=src), [])

    def test_a_null_must_be_named_in_unknown(self) -> None:
        self.assertIn("max_output is empty but `unknown` has no entry starting 'max_output'", self.problems(max_output=None))
        self.assertEqual(self.problems(max_output=None, unknown=FIXTURE_CARD["unknown"] + ["max_output: not published by the maker"]), [])
        self.assertEqual(self.problems(retires=None), [], "retires alone may be empty without a word")
        self.assertIn(
            "a price is null but `unknown` has no entry starting 'pricing_usd_per_mtok'",
            self.problems(pricing_usd_per_mtok={"input": None, "output": 1.0, "cached_input": None, "notes": None}),
        )

    def test_every_key_benchmark_is_listed_or_named_in_unknown(self) -> None:
        unknown = [u for u in FIXTURE_CARD["unknown"] if not u.startswith("Artificial Analysis Coding")]
        self.assertIn("benchmark 'Artificial Analysis Coding Agent Index' is neither in `benchmarks` nor named in `unknown`", self.problems(unknown=unknown))
        bench = copy.deepcopy(FIXTURE_CARD["benchmarks"])
        bench.append({**bench[0], "name": "Artificial Analysis Coding Agent Index", "score": 60.0})
        self.assertEqual(self.problems(benchmarks=bench, unknown=unknown), [])

    def test_a_card_of_the_wrong_shape_is_reported_and_the_other_checks_still_run(self) -> None:
        self.write_card(access=5)
        code, verdict, lines = self.verdicts()
        self.assertEqual(code, 1, "\n".join(lines))
        self.assertEqual(verdict["cards"], "FAIL")
        self.assertEqual(verdict["generated"], "FAIL")
        self.assertIn("cannot render: TypeError", "\n".join(lines))
        self.assertEqual({verdict[a] for a in ("index", "links", "quotes", "queue")}, {"PASS"})
        self.write_card(unknown=5)
        self.assertEqual(self.verdicts()[1]["generated"], "FAIL")

    def test_effort_control_needs_levels(self) -> None:
        self.assertIn(
            "reasoning.control is effort but reasoning.levels is empty",
            self.problems(reasoning={"control": "effort", "levels": [], "default": None}, unknown=["x"]),
        )
        self.assertIn("reasoning.default is not one of reasoning.levels", self.problems(reasoning={"control": "effort", "levels": ["low"], "default": "max"}))

    def test_a_reasoning_value_not_found_is_null_and_named_in_unknown(self) -> None:
        unnamed = self.problems(reasoning={"control": None, "levels": [], "default": None}, unknown=["x"])
        self.assertTrue(any(p.startswith("reasoning.control is not one of") for p in unnamed))
        named = self.problems(
            reasoning={"control": None, "levels": [], "default": None}, unknown=["reasoning: not published"]
        )
        self.assertFalse(any(p.startswith("reasoning") for p in named))
        levels = self.problems(
            reasoning={"control": "effort", "levels": [], "default": None},
            unknown=["reasoning.levels: not published"],
        )
        self.assertNotIn("reasoning.control is effort but reasoning.levels is empty", levels)

    def voice_problems(self, **changes: object) -> list[str]:
        card = voice_card()
        card["voice"] = {**card["voice"], **changes}
        return check.card_problems(card, "example-voice-1", set(), TODAY)

    def test_a_text_model_has_voice_null_and_needs_no_unknown_entry(self) -> None:
        self.assertIsNone(FIXTURE_CARD["voice"])
        self.assertEqual(self.problems(), [])
        card = copy.deepcopy(FIXTURE_CARD)
        del card["voice"]
        self.assertEqual(check.card_problems(card, "example-model-1", set(), TODAY), ["missing key(s): voice"])

    def test_a_full_voice_object_is_valid(self) -> None:
        self.assertEqual(self.voice_problems(), [])
        self.assertEqual(check.card_problems(voice_card(), "example-voice-1", set(), TODAY), [])

    def test_the_voice_object_has_exactly_its_keys(self) -> None:
        shape = "voice is neither null nor an object with exactly " + ", ".join(check.VOICE_KEYS)
        for bad in ({}, "full", [], {**FIXTURE_VOICE, "extra": 1}, {k: v for k, v in FIXTURE_VOICE.items() if k != "latency"}):
            with self.subTest(voice=bad):
                self.assertEqual(self.problems(voice=bad), [shape])

    def test_voice_values_have_their_types(self) -> None:
        cases = {
            "duplex": (["simplex", 1, True], "voice.duplex is not one of full, half, none or null"),
            "voices": ([0, -3, True, 2.5, [1], ""], "voice.voices is not a positive integer, text or null"),
            "languages": (["en", [1], ["en", ""], {"en": 1}], "voice.languages is not a list of text or null"),
            "input_audio": ([5, True, "", ["pcm"]], "voice.input_audio is not text or null"),
            "latency": ([0.3, ""], "voice.latency is not text or null"),
        }
        for key, (values, message) in cases.items():
            for value in values:
                with self.subTest(key=key, value=value):
                    self.assertEqual(self.voice_problems(**{key: value}), [message])
        for value in ("full", "half", "none"):
            self.assertEqual(self.voice_problems(duplex=value), [])
        for value in (3, "custom cloning"):
            self.assertEqual(self.voice_problems(voices=value), [])

    def test_a_voice_value_not_found_is_null_and_named_in_unknown(self) -> None:
        for key, empty in (("latency", None), ("duplex", None), ("languages", []), ("voices", None)):
            with self.subTest(key=key):
                self.assertEqual(
                    self.voice_problems(**{key: empty}),
                    [f"voice.{key} is empty but `unknown` has no entry starting 'voice.{key}'"],
                )
                named = voice_card()
                named["voice"][key] = empty
                named["unknown"] = named["unknown"] + [f"voice.{key}: the maker publishes none"]
                self.assertEqual(check.card_problems(named, "example-voice-1", set(), TODAY), [])
        other = voice_card()
        other["voice"]["latency"] = None
        other["unknown"] = other["unknown"] + ["voice.session_limit: not published"]
        self.assertEqual(len(check.card_problems(other, "example-voice-1", set(), TODAY)), 1, "an entry names one key")

    def test_voice_text_is_held_to_the_quotation_and_citation_rules(self) -> None:
        long = " ".join(["w"] * 26)
        self.assertTrue(any("voice" in p or "interruption" in p for p in self.voice_problems(interruption=f'The guide says "{long}".')))
        self.assertIn("[nowhere-1] is cited but is neither a source id of this card nor a ledger id", self.voice_problems(latency="fast [nowhere-1]"))

    def test_a_per_minute_price_is_a_null_price_with_a_note_and_an_unknown_entry(self) -> None:
        pricing = {"input": None, "output": None, "cached_input": None, "notes": "billed per minute of audio, not per token"}
        card = voice_card(pricing_usd_per_mtok=pricing)
        self.assertIn(
            "a price is null but `unknown` has no entry starting 'pricing_usd_per_mtok'",
            check.card_problems(card, "example-voice-1", set(), TODAY),
        )
        card["unknown"] = card["unknown"] + ["pricing_usd_per_mtok: the unit differs, per minute"]
        self.assertEqual(check.card_problems(card, "example-voice-1", set(), TODAY), [])

    def test_a_card_in_the_wrong_place_and_a_card_that_is_not_json(self) -> None:
        write(self.root, "models/loose.json", "{}")
        self.assertFails("cards", "models/loose.json: a card lives at models/<maker>/<id>.json")
        (self.root / "models/loose.json").unlink()
        write(self.root, "models/example-lab/deeper/x.json", "{}")
        self.assertFails("cards", "models/example-lab/deeper/x.json: a card lives at models/<maker>/<id>.json")
        (self.root / "models/example-lab/deeper/x.json").unlink()
        write(self.root, "models/example-lab/bad.json", "{")
        self.assertFails("cards", "models/example-lab/bad.json: not JSON")


class ModelFilesTest(RepoCase):
    def test_a_card_without_its_model_file_and_a_model_file_without_its_card(self) -> None:
        (self.root / MODEL_PATH).unlink()
        self.assertFails("models", f"{CARD_PATH[:-5]}.json: no model file {MODEL_PATH}")
        model_files(self.root)
        (self.root / CARD_PATH).unlink()
        self.assertFails("models", f"{MODEL_PATH}: no card {CARD_PATH}")

    def test_every_heading_of_the_template_is_required_and_in_order(self) -> None:
        text = (self.root / MODEL_PATH).read_text(encoding="utf-8")
        for level, name in layout.MODEL_HEADINGS:
            with self.subTest(heading=name):
                heading = f"{'#' * level} {name}\n"
                write(self.root, MODEL_PATH, text.replace(heading, "", 1))
                self.assertFails("models", f"{MODEL_PATH}: heading `{'#' * level} {name}` is missing or out of order")
        swapped = text.replace("## Benchmarks\n", "## TMP\n").replace("## Open questions\n", "## Benchmarks\n").replace("## TMP\n", "## Open questions\n")
        write(self.root, MODEL_PATH, swapped)
        self.assertFails("models", f"{MODEL_PATH}: heading `## Open questions` is missing or out of order")

    def test_headings_in_a_fenced_block_do_not_count_and_extra_headings_are_allowed(self) -> None:
        text = (self.root / MODEL_PATH).read_text(encoding="utf-8")
        write(self.root, MODEL_PATH, text.replace("## Benchmarks\n", "```\n## Benchmarks\n```\n", 1))
        self.assertFails("models", "heading `## Benchmarks` is missing or out of order")
        write(self.root, MODEL_PATH, text.replace("## Open questions\n", "## An extra section\n\nWritten.\n\n## Open questions\n"))
        refresh(self.root)
        self.assertEqual(self.verdicts()[1]["models"], "PASS")

    def test_every_maker_folder_needs_a_readme_with_the_maker_headings(self) -> None:
        readme = self.root / "models/example-lab/README.md"
        text = readme.read_text(encoding="utf-8")
        readme.unlink()
        self.assertFails("models", "models/example-lab/README.md: missing; every maker folder has one")
        write(self.root, "models/example-lab/README.md", text.replace("## API surface\n", ""))
        self.assertFails("models", "models/example-lab/README.md: heading `## API surface` is missing or out of order")


class VoiceFilesTest(RepoCase):
    """An audio-output model file holds the voice subsection after the images and audio one, and no other does."""

    HEADING = f"### {layout.VOICE_HEADING[1]}\n"
    VOICE_PATH = "models/example-lab/example-voice-1.md"

    def add_voice_model(self, card: dict | None = None) -> None:
        model_files(self.root, card=card or voice_card())
        refresh(self.root)

    def test_a_voice_model_file_made_from_the_stub_passes(self) -> None:
        self.add_voice_model()
        code, verdict, lines = self.verdicts()
        self.assertEqual(code, 0, "\n".join(lines))
        self.assertEqual(verdict["models"], "PASS")

    def test_an_audio_output_file_without_the_subsection_fails(self) -> None:
        self.add_voice_model()
        text = (self.root / self.VOICE_PATH).read_text(encoding="utf-8")
        write(self.root, self.VOICE_PATH, text.replace(self.HEADING + f"\n{layout.PENDING}\n\n", "", 1).replace(self.HEADING, "", 1))
        self.assertFails("models", f"{self.VOICE_PATH}: heading `### {layout.VOICE_HEADING[1]}` is missing or out of order")

    def test_the_subsection_must_come_after_the_images_and_audio_subsection(self) -> None:
        self.add_voice_model()
        text = (self.root / self.VOICE_PATH).read_text(encoding="utf-8")
        images = "### Images, audio, other inputs\n"
        voice = self.HEADING
        swapped = text.replace(images, "### TMP\n").replace(voice, images).replace("### TMP\n", voice)
        write(self.root, self.VOICE_PATH, swapped)
        self.assertFails("models", "is missing or out of order")

    def test_the_subsection_before_the_sampling_subsection_is_required_not_later(self) -> None:
        self.add_voice_model()
        text = (self.root / self.VOICE_PATH).read_text(encoding="utf-8")
        sampling = "### Sampling and API parameters\n"
        write(self.root, self.VOICE_PATH, text.replace(self.HEADING, "", 1).replace(sampling, sampling + "\nWritten.\n\n" + self.HEADING, 1))
        self.assertFails("models", "is missing or out of order")

    def test_a_text_model_file_may_not_hold_the_subsection(self) -> None:
        text = (self.root / MODEL_PATH).read_text(encoding="utf-8")
        images = "### Images, audio, other inputs\n\nWritten.\n\n"
        self.assertIn(images, text)
        write(self.root, MODEL_PATH, text.replace(images, images + self.HEADING + "\nWritten.\n\n", 1))
        self.assertFails("models", f"{MODEL_PATH}: heading `### {layout.VOICE_HEADING[1]}` is only for a model whose card lists audio output")

    def test_the_rule_follows_the_card_not_the_file_name(self) -> None:
        self.add_voice_model()
        card = voice_card(modalities={"input": ["text", "audio"], "output": ["text"]})
        write(self.root, "models/example-lab/example-voice-1.json", json.dumps(card, indent=2) + "\n")
        refresh(self.root)
        self.assertFails("models", "is only for a model whose card lists audio output")

    def test_an_audio_entry_with_a_qualifier_counts(self) -> None:
        card = voice_card(modalities={"input": ["text"], "output": ["text", "audio (speech, limited)"]})
        model_files(self.root, card=card)
        text = (self.root / self.VOICE_PATH).read_text(encoding="utf-8")
        write(self.root, self.VOICE_PATH, text.replace(self.HEADING, "", 1))
        refresh(self.root)
        self.assertFails("models", f"{self.VOICE_PATH}: heading `### {layout.VOICE_HEADING[1]}` is missing")

    def test_a_card_that_cannot_be_read_does_not_hide_the_other_checks(self) -> None:
        write(self.root, "models/example-lab/bad.json", "{")
        write(self.root, "models/example-lab/bad.md", (self.root / MODEL_PATH).read_text(encoding="utf-8"))
        self.assertFails("cards", "models/example-lab/bad.json: not JSON")

    def test_the_format_page_documents_every_voice_key_and_the_subsection(self) -> None:
        text = (REPO / "models" / "FORMAT.md").read_text(encoding="utf-8")
        for key in check.VOICE_KEYS:
            self.assertIn(f"`{key}`", text, key)
        self.assertIn(f"### {layout.VOICE_HEADING[1]}", text)
        for mode in check.VOICE_DUPLEX:
            self.assertIn(f"`{mode}`", text)


class ProviderFilesTest(RepoCase):
    def test_the_readme_is_required(self) -> None:
        (self.root / "providers/README.md").unlink()
        self.assertFails("providers", "providers/README.md: missing")

    def test_a_kind_must_be_one_the_readme_lists(self) -> None:
        provider_file(self.root, kind="mystery")
        refresh(self.root)
        self.assertFails("providers", "providers/example-host.md: kind 'mystery' is not one of first-party lab API, cloud platform")

    def test_a_kind_may_come_from_the_first_line_under_the_title(self) -> None:
        text = (self.root / "providers/example-host.md").read_text(encoding="utf-8").replace("kind: inference host\n", "")
        write(self.root, "providers/example-host.md", text.replace("Written.", "inference host; one paragraph.", 1))
        refresh(self.root)
        self.assertEqual(self.verdicts()[1]["providers"], "PASS")

    def test_every_heading_of_the_provider_template_is_required(self) -> None:
        text = (self.root / "providers/example-host.md").read_text(encoding="utf-8")
        for level, name in layout.PROVIDER_HEADINGS:
            with self.subTest(heading=name):
                write(self.root, "providers/example-host.md", text.replace(f"{'#' * level} {name}\n", "", 1))
                self.assertFails("providers", f"providers/example-host.md: heading `{'#' * level} {name}` is missing or out of order")


class ApplicationsTest(RepoCase):
    def tiers(self, data: object) -> None:
        write(self.root, TIERS_PATH, json.dumps(data))

    def entry(self, **changes: object) -> dict:
        data = copy.deepcopy(json.loads((HERE / "fixtures" / "tiers.json").read_text(encoding="utf-8")))
        entry = data["placements"]["example-model-1"]
        entry.update(changes)
        return {"version": 1, "placements": {"example-model-1": entry}}

    def test_the_file_is_required_and_must_be_json_of_the_right_shape(self) -> None:
        (self.root / TIERS_PATH).unlink()
        self.assertFails("applications", f"{TIERS_PATH}: missing")
        write(self.root, TIERS_PATH, "{")
        self.assertFails("applications", f"{TIERS_PATH}: not JSON")
        for data in ([], {"version": 2, "placements": {}}, {"version": 1}, {"version": 1, "placements": [], "x": 1}):
            self.tiers(data)
            self.assertFails("applications", "needs exactly version (1) and placements (an object)")

    def test_every_model_named_has_a_card(self) -> None:
        data = self.entry()
        data["placements"]["ghost"] = data["placements"]["example-model-1"]
        self.tiers(data)
        self.assertFails("applications", f"{TIERS_PATH}: ghost: no card models/<maker>/ghost.json")

    def test_an_entry_has_exactly_placements_basis_and_notes(self) -> None:
        self.tiers({"version": 1, "placements": {"example-model-1": {"placements": [], "basis": "b"}}})
        self.assertFails("applications", "example-model-1: needs exactly placements, basis and notes")

    def test_placement_rows_are_checked(self) -> None:
        bad_rows = (
            ([], "placements is not a list with a row"),
            (["x"], "placements[0] needs exactly effort, tier and confidence"),
            ([{"effort": 1, "tier": "spec", "confidence": "low"}], "placements[0].effort is not text or null"),
            ([{"effort": None, "tier": "gold", "confidence": "low"}], "placements[0].tier is not one of outcome, design, spec"),
            ([{"effort": None, "tier": "spec", "confidence": "sure"}], "placements[0].confidence is not one of high, medium, low"),
        )
        for rows, message in bad_rows:
            with self.subTest(message=message):
                self.tiers(self.entry(placements=rows))
                self.assertFails("applications", message)

    def test_basis_and_notes_are_text(self) -> None:
        self.tiers(self.entry(basis=""))
        self.assertFails("applications", "basis is empty")
        self.tiers(self.entry(notes="n"))
        self.assertFails("applications", "notes is not a list of text")
        self.tiers(self.entry(notes=[""]))
        self.assertFails("applications", "notes is not a list of text")

    def test_a_long_quotation_and_an_unreachable_reference_fail(self) -> None:
        long = " ".join(["w"] * 26)
        self.tiers(self.entry(basis=f'The page says "{long}".'))
        self.assertFails("applications", "basis holds a quotation of 26 words, over 25")
        self.tiers(self.entry(notes=[f"It says “{long}”."]))
        self.assertFails("applications", "notes holds a quotation of 26 words, over 25")
        self.tiers(self.entry(basis="From notes.md, unchanged."))
        self.assertFails("applications", "basis cites something a public reader cannot reach ('notes.md')")
        self.tiers(self.entry(basis="Per [the format](../models/FORMAT.md)."))
        self.assertEqual(self.verdicts()[1]["applications"], "PASS")

    def test_a_cited_id_must_be_a_source_of_the_card_or_a_ledger_id(self) -> None:
        self.tiers(self.entry(basis="Because of [nowhere-2]."))
        self.assertFails("applications", "[nowhere-2] is cited but is neither a source id of the card nor a ledger id")
        self.tiers(self.entry(notes=["Seen in [example-1]."]))
        self.assertEqual(self.verdicts()[1]["applications"], "PASS")

    def test_a_valid_file_with_no_entries_passes(self) -> None:
        self.tiers({"version": 1, "placements": {}})
        refresh(self.root)
        self.assertEqual(self.verdicts()[1]["applications"], "PASS")


class PendingTest(RepoCase):
    def stub(self, rel: str = "practices/example.md") -> None:
        write(self.root, rel, doc_text(body=f"{layout.PENDING}\n"))
        refresh(self.root)

    def test_a_file_holding_the_placeholder_fails_and_is_named_with_its_count(self) -> None:
        write(self.root, "practices/example.md", doc_text(body=f"{layout.PENDING}\n\nText.\n\n{layout.PENDING}\n"))
        refresh(self.root)
        problems = self.assertFails("pending", "practices/example.md: 2 line(s) hold the placeholder")
        self.assertEqual(len(problems), 1)

    def test_a_stub_made_from_the_templates_fails_until_every_section_is_written(self) -> None:
        write(self.root, MODEL_PATH, layout.model_stub("Example Model 1", "2026-10-03", ["https://example.com/s"]))
        refresh(self.root)
        code, verdict, lines = self.verdicts()
        self.assertEqual(code, 1)
        self.assertEqual(verdict["pending"], "FAIL")
        self.assertTrue(any(f"{MODEL_PATH}: 16 line(s) hold the placeholder" in line for line in lines), lines)
        self.assertEqual({a: v for a, v in verdict.items() if v != "PASS"}, {"scrub": "UNVERIFIED", "pending": "FAIL"})

    def test_allow_pending_reports_unverified_and_runs_the_other_checks(self) -> None:
        self.stub()
        code, lines = run_check(self.root, allow_pending=True)
        self.assertEqual(code, 0, "\n".join(lines))
        text = "\n".join(lines)
        self.assertIn("UNVERIFIED pending: 1 file(s) still hold the placeholder", text)
        self.assertNotIn("FAIL", text)
        self.assertIn("PASS frontmatter", lines)

    def test_allow_pending_does_not_hide_another_failure(self) -> None:
        self.stub()
        write(self.root, "practices/other.md", "# No frontmatter\n")
        code, lines = run_check(self.root, allow_pending=True)
        self.assertEqual(code, 1)
        self.assertTrue(any(line.startswith("FAIL frontmatter") for line in lines))

    def test_no_placeholder_passes_with_or_without_the_flag(self) -> None:
        for flag in (False, True):
            code, lines = run_check(self.root, allow_pending=flag)
            self.assertEqual(code, 0)
            self.assertIn("PASS pending", lines)

    def test_a_long_list_is_cut_and_counted(self) -> None:
        for number in range(check.PENDING_LISTED + 3):
            write(self.root, f"practices/p{number}.md", doc_text(title=f"P{number}", body=f"{layout.PENDING}\n"))
        refresh(self.root)
        code, lines = run_check(self.root)
        self.assertEqual(code, 1)
        listed = [line for line in lines if line.startswith("  practices/p")]
        self.assertEqual(len(listed), check.PENDING_LISTED)
        self.assertIn("  ... and 3 more file(s)", lines)
        self.assertIn(f"FAIL pending: {check.PENDING_LISTED + 3} problem(s)", lines)

    def test_the_placeholder_is_found_in_any_file_that_can_be_published_but_not_in_the_workspace(self) -> None:
        write(self.root, ".agents/work/notes.md", layout.PENDING)
        self.assertEqual(self.verdicts()[1]["pending"], "PASS")
        write(self.root, "tests/example.txt", layout.PENDING)
        self.assertFails("pending", "tests/example.txt: 1 line(s) hold the placeholder")

    def test_the_scripts_and_tests_of_this_repository_do_not_hold_the_placeholder(self) -> None:
        for folder in ("scripts", "tests"):
            for path in (REPO / folder).rglob("*.py"):
                self.assertNotIn(layout.PENDING, path.read_text(encoding="utf-8"), str(path))


class ScopeListTest(RepoCase):
    def test_a_class_with_more_than_two_generations_is_printed_and_does_not_fail(self) -> None:
        for generation in ("2", "3"):
            card = copy.deepcopy(FIXTURE_CARD)
            card.update(id=f"example-model-{generation}", name=f"Example Model {generation}", generation=generation)
            model_files(self.root, card=card)
        refresh(self.root)
        code, lines = run_check(self.root)
        self.assertEqual(code, 0, "\n".join(lines))
        self.assertIn("scope (printed, not gated): 1 class(es) with more than two generations", lines)
        self.assertIn("  Example Lab Example Pro: 3 generations (1, 2, 3)", lines)

    def test_two_generations_and_unnumbered_cards_are_within_scope(self) -> None:
        card = copy.deepcopy(FIXTURE_CARD)
        card.update(id="example-model-2", name="Example Model 2", generation="2")
        model_files(self.root, card=card)
        card.update(id="example-model-3", name="Example Model 3", generation=None)
        model_files(self.root, card=card)
        self.assertEqual(check.scope_list(self.root), [])
        _, lines = run_check(self.root)
        self.assertIn("scope (printed, not gated): every class holds at most two generations", lines)


class GeneratedTest(RepoCase):
    def test_a_hand_edited_generated_file_fails(self) -> None:
        path = self.root / "applications/implementer-tiers.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nA hand edit.\n", encoding="utf-8")
        self.assertFails("generated", "applications/implementer-tiers.md: differs from what scripts/render.py renders; run `make render`")

    def test_a_hand_edit_inside_a_card_block_fails_and_one_outside_it_passes(self) -> None:
        path = self.root / MODEL_PATH
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("| Status | ga |", "| Status | retired |"), encoding="utf-8")
        self.assertFails("generated", f"{MODEL_PATH}: differs")
        path.write_text(text.replace("\n## Sources\n\nWritten.", "\n## Sources\n\nWritten by hand."), encoding="utf-8")
        self.assertEqual(self.verdicts()[1]["generated"], "PASS")

    def test_a_card_change_without_a_render_fails_in_the_block_and_in_the_table(self) -> None:
        card = copy.deepcopy(FIXTURE_CARD)
        card["name"] = "Renamed"
        card["released"] = "2026-09-02"
        write(self.root, CARD_PATH, json.dumps(card))
        problems = self.assertFails("generated", f"{MODEL_PATH}: differs")
        self.assertTrue(any(p.startswith("models/README.md: differs") for p in problems), problems)

    def test_a_missing_generated_file_fails(self) -> None:
        (self.root / "applications/implementer-tiers.md").unlink()
        self.assertFails("generated", "applications/implementer-tiers.md: missing; run `make render`")

    def test_a_file_without_its_markers_is_reported_not_raised(self) -> None:
        write(self.root, "models/README.md", "# Models\n")
        self.assertFails("generated", "cannot render: ValueError: models/README.md: needs exactly one")

    def test_a_provider_added_without_a_render_fails_in_the_table(self) -> None:
        provider_file(self.root, "second", "Second Host")
        self.assertFails("generated", "providers/README.md: differs")

    def test_a_placement_change_without_a_render_fails(self) -> None:
        data = json.loads((self.root / TIERS_PATH).read_text(encoding="utf-8"))
        data["placements"]["example-model-1"]["basis"] = "Another basis."
        write(self.root, TIERS_PATH, json.dumps(data))
        self.assertFails("generated", "applications/implementer-tiers.md: differs")


class IndexTest(RepoCase):
    def index(self) -> str:
        return (self.root / "INDEX.md").read_text(encoding="utf-8")

    def test_a_document_missing_from_the_index(self) -> None:
        write(self.root, "practices/new.md", doc_text(title="New practice"))
        self.assertFails("index", "INDEX.md: practices/new.md is not listed")

    def test_a_row_for_a_file_that_is_not_a_document(self) -> None:
        write(self.root, "INDEX.md", self.index() + "| [practices/ghost.md](practices/ghost.md) | G | S | 2026-10-01 | STABLE |\n")
        self.assertFails("index", "practices/ghost.md is not a research document")

    def test_a_row_for_a_navigation_or_format_page_is_not_a_document(self) -> None:
        for page in sorted(layout.PAGES):
            with self.subTest(page=page):
                write(self.root, "INDEX.md", self.index() + f"| [{page}]({page}) | F | S | 2026-10-01 | STABLE |\n")
                self.assertFails("index", f"{page} is not a research document")
                write(self.root, "INDEX.md", index_rows(self.root))

    def test_model_provider_and_application_documents_are_listed(self) -> None:
        text = self.index()
        for name in (MODEL_PATH, "models/example-lab/README.md", "providers/example-host.md", "applications/implementer-tiers.md"):
            self.assertIn(f"| [{name}]({name}) |", text)
            write(self.root, "INDEX.md", "\n".join(line for line in text.split("\n") if f"[{name}]" not in line))
            self.assertFails("index", f"INDEX.md: {name} is not listed")
            write(self.root, "INDEX.md", text)

    def test_stale_facts_in_a_row(self) -> None:
        text = self.index().replace("2026-10-01 | STABLE", "2026-09-01 | STABLE")
        write(self.root, "INDEX.md", text)
        self.assertFails("index", "practices/example.md last_checked is 2026-10-01, not 2026-09-01")
        write(self.root, "INDEX.md", self.index().replace("| STABLE |", "| VOLATILE |"))
        self.assertFails("index", "practices/example.md volatility class differs from its frontmatter")
        write(self.root, "INDEX.md", self.index().replace("| Example practice |", "| Another title |"))
        self.assertFails("index", "title differs from its `# ` title")

    def test_a_listing_twice_and_a_malformed_row(self) -> None:
        row = next(line for line in self.index().split("\n") if line.startswith("| [practices/example.md]"))
        write(self.root, "INDEX.md", self.index() + row + "\n")
        self.assertFails("index", "practices/example.md is listed twice")
        write(self.root, "INDEX.md", self.index().replace(row, "| [practices/example.md](practices/example.md) | only | three |"))
        self.assertFails("index", "a row is not `| [path](path) | title | scope | last_checked | volatility |`")

    def test_no_index_file(self) -> None:
        (self.root / "INDEX.md").unlink()
        self.assertFails("index", "INDEX.md: missing")


class LinkTest(RepoCase):
    def test_a_broken_relative_link(self) -> None:
        write(self.root, "practices/example.md", doc_text(body="See [it](missing.md).\n"))
        refresh(self.root)
        self.assertFails("links", "practices/example.md:10: link missing.md does not resolve")

    def test_links_that_resolve_pass(self) -> None:
        write(self.root, "practices/other.md", doc_text(title="Other"))
        write(self.root, "practices/example.md", doc_text(body="See [it](other.md#other), [up](../INDEX.md), [web](https://example.com/x) and [mail](mailto:a@b.c).\n"))
        refresh(self.root)
        self.assertEqual(self.verdicts()[1]["links"], "PASS")

    def test_an_anchor_that_names_no_heading(self) -> None:
        write(self.root, "practices/other.md", doc_text(title="Other"))
        write(self.root, "practices/example.md", doc_text(body="See [it](other.md#nowhere).\n"))
        refresh(self.root)
        self.assertFails("links", "link other.md#nowhere names a heading that does not exist")

    def test_github_heading_anchors(self) -> None:
        slugs = check.heading_slugs("# One Two\n\n## Key findings (STABLE)\n\n## `code` & more\n\n## Dup\n\n## Dup\n\n```\n# not a heading\n```\n")
        self.assertEqual(slugs, {"one-two", "key-findings-stable", "code--more", "dup", "dup-1"})

    def test_links_in_code_are_not_checked(self) -> None:
        write(self.root, "practices/example.md", doc_text(body="Use `[text](nowhere.md)` here.\n\n```\n[x](nope.md)\n```\n"))
        refresh(self.root)
        self.assertEqual(self.verdicts()[1]["links"], "PASS")

    def test_a_link_out_of_the_repository(self) -> None:
        write(self.root, "practices/example.md", doc_text(body="See [it](../../outside.md).\n"))
        refresh(self.root)
        self.assertFails("links", "leaves the repository")

    def test_files_outside_the_research_folders_are_checked(self) -> None:
        write(self.root, "README.md", "See [x](nope.md).\n")
        self.assertFails("links", "README.md:1: link nope.md does not resolve")

    def test_a_link_must_match_the_case_of_the_file_name(self) -> None:
        write(self.root, "practices/example.md", doc_text(body="See [up](../index.md).\n"))
        refresh(self.root)
        self.assertFails("links", "link ../index.md does not resolve")

    def test_hidden_folders_other_than_github_are_skipped(self) -> None:
        write(self.root, ".agents/notes.md", "See [x](nope.md).\n")
        write(self.root, "RESEARCH.md.orig", "[x](nope.md)")
        self.assertEqual(self.verdicts()[1]["links"], "PASS")
        write(self.root, ".github/PULL_REQUEST_TEMPLATE.md", "[x](nope.md)\n")
        self.assertFails("links", ".github/PULL_REQUEST_TEMPLATE.md:1")


class QuoteTest(RepoCase):
    def doc(self, quoted: str) -> None:
        write(self.root, "practices/example.md", doc_text(body=f'The page says "{quoted}" and nothing else.\n'))
        refresh(self.root)

    def test_25_words_pass_and_26_fail(self) -> None:
        self.doc(" ".join(["word"] * 25))
        self.assertEqual(self.verdicts()[1]["quotes"], "PASS")
        self.doc(" ".join(["word"] * 26))
        self.assertFails("quotes", "practices/example.md:10: quotation of 26 words, over 25")

    def test_curly_quotes_count_too(self) -> None:
        write(self.root, "practices/example.md", doc_text(body="It says “" + " ".join(["word"] * 30) + "”.\n"))
        refresh(self.root)
        self.assertFails("quotes", "quotation of 30 words")

    def test_a_quotation_over_several_lines_and_in_a_list_item(self) -> None:
        wrapped = "\n".join(" ".join(["word"] * 7) for _ in range(4))
        write(self.root, "practices/example.md", doc_text(body=f'- item "{wrapped}" end\n'))
        refresh(self.root)
        self.assertFails("quotes", "quotation of 28 words")

    def test_two_short_quotations_are_not_one_long_one(self) -> None:
        body = 'He said "' + " ".join(["a"] * 20) + '" and then "' + " ".join(["b"] * 20) + '" again.\n'
        write(self.root, "practices/example.md", doc_text(body=body))
        refresh(self.root)
        self.assertEqual(self.verdicts()[1]["quotes"], "PASS")

    def test_code_and_frontmatter_are_not_prose(self) -> None:
        long = '"' + " ".join(["w"] * 40) + '"'
        write(self.root, "practices/example.md", doc_text(body=f"Use `{long}` or\n\n```\n{long}\n```\n"))
        refresh(self.root)
        self.assertEqual(self.verdicts()[1]["quotes"], "PASS")

    def test_single_curly_quotes_and_a_possessive_closing_quote_count(self) -> None:
        long = " ".join(["word"] * 30)
        for body in (f"It says \u2018{long}\u2019 here.\n", f'The "{long}"s end.\n'):
            write(self.root, "practices/example.md", doc_text(body=body))
            refresh(self.root)
            self.assertFails("quotes", "quotation of 30 words")

    def test_other_quotation_mark_styles_count_too(self) -> None:
        long = " ".join(["word"] * 30)
        for quoted in (f"'{long}'", f"\u00ab{long}\u00bb", f"\u201e{long}\u201c", f"\u300c{long}\u300d"):
            with self.subTest(quoted=quoted[0]):
                write(self.root, "practices/example.md", doc_text(body=f"The page says {quoted} here.\n"))
                refresh(self.root)
                self.assertFails("quotes", "quotation of 30 words")

    def test_a_straight_single_quoted_passage_of_25_words_passes(self) -> None:
        write(self.root, "practices/example.md", doc_text(body="It says '" + " ".join(["word"] * 25) + "' here.\n"))
        refresh(self.root)
        self.assertEqual(self.verdicts()[1]["quotes"], "PASS")

    def test_a_long_blockquote_needs_a_bold_label(self) -> None:
        long = " ".join(["word"] * 30)
        write(self.root, "practices/example.md", doc_text(body=f"> {long}\n"))
        refresh(self.root)
        self.assertFails("quotes", "blockquote of 30 words, over 25, without a bold label")
        write(self.root, "practices/example.md", doc_text(body=f"> **Note.** {long}\n"))
        refresh(self.root)
        self.assertEqual(self.verdicts()[1]["quotes"], "PASS")
        write(self.root, "practices/example.md", doc_text(body="> " + " ".join(["word"] * 25) + "\n"))
        refresh(self.root)
        self.assertEqual(self.verdicts()[1]["quotes"], "PASS")

    def test_fenced_code_with_a_blank_line_is_not_prose(self) -> None:
        long = '"' + " ".join(["w"] * 40) + '"'
        write(self.root, "practices/example.md", doc_text(body=f"```\n{long}\n\n{long} [x](nope.md)\n```\n"))
        refresh(self.root)
        code, verdict, lines = self.verdicts()
        self.assertEqual((verdict["quotes"], verdict["links"]), ("PASS", "PASS"), "\n".join(lines))

    def test_apostrophes_do_not_pair_up(self) -> None:
        write(self.root, "practices/example.md", doc_text(body="It's a model's output, and the lab's " + "word " * 40 + "isn't a quotation.\n"))
        refresh(self.root)
        self.assertEqual(self.verdicts()[1]["quotes"], "PASS")
        write(self.root, "practices/example.md", doc_text(body="The \u2018model\u2019s output and the lab\u2019s " + "word " * 40 + "isn\u2019t a quotation.\n"))
        refresh(self.root)
        self.assertEqual(self.verdicts()[1]["quotes"], "PASS")


class QueueTest(RepoCase):
    GOOD = {
        "kind": "fact", "subject": "s", "claim": "A claim.", "url": "https://example.com/p",
        "observed_on": "2026-10-02", "version": 1,
    }

    def queue_file(self, name: str | None = None, **changes: object) -> str:
        data = dict(self.GOOD, collected_on="2026-10-03")
        data["sha256"] = check.collect.digest(str(data["claim"]), str(data["url"]))
        data.update(changes)
        name = name or f"20261003-{data['sha256']}.json"
        write(self.root, f"ingest/queue/{name}", json.dumps(data))
        return name

    def test_a_collected_finding_passes(self) -> None:
        self.queue_file()
        write(self.root, "ingest/queue/.gitkeep", "")
        self.assertEqual(self.verdicts()[1]["queue"], "PASS")

    def test_a_queue_name_must_carry_the_full_digest_of_the_finding(self) -> None:
        self.queue_file("20261003-aaaaaaaa.json")
        self.assertFails("queue", "ingest/queue/20261003-aaaaaaaa.json: a queue file is named <YYYYMMDD>-<64 hex digits")
        self.queue_file("20261003-" + "b" * 64 + ".json")
        self.assertFails("queue", "the name does not carry the digest of its claim and url")

    def test_a_recorded_digest_must_match_the_finding(self) -> None:
        self.queue_file(sha256="a" * 64, name="20261003-" + "a" * 64 + ".json")
        self.assertFails("queue", "sha256 is not the digest of its claim and url")

    def test_a_folder_in_the_queue_and_a_bad_seen_line_are_reported_not_raised(self) -> None:
        (self.root / "ingest/queue/folder").mkdir(parents=True)
        write(self.root, "ingest/seen.jsonl", '{"sha256": "' + "a" * 64 + '"}\n{broken\n{"sha256": "short"}\n')
        problems = self.assertFails("queue", "ingest/queue/folder: not a file")
        self.assertIn("ingest/seen.jsonl:2: not a JSON object with a \"sha256\"", problems)
        self.assertIn("ingest/seen.jsonl:3: sha256 is not 64 hex digits", problems)

    def test_a_malformed_queue_file_fails(self) -> None:
        write(self.root, "ingest/queue/x.json", json.dumps(dict(self.GOOD, kind="opinion")))
        self.assertFails("queue", "ingest/queue/x.json: kind is not one of fact, correction")
        write(self.root, "ingest/queue/x.json", "{")
        self.assertFails("queue", "ingest/queue/x.json:")


class ScrubTest(RepoCase):
    def test_a_hit_names_the_place_and_never_the_term(self) -> None:
        deny = self.root.parent / "deny.txt"
        deny.write_text("# private\nSecretClient\n", encoding="utf-8")
        write(self.root, "practices/example.md", doc_text(body="Seen at secretclient once.\n"))
        refresh(self.root)
        code, lines = run_check(self.root, denylist=deny)
        self.assertEqual(code, 1)
        text = "\n".join(lines)
        self.assertIn("FAIL scrub: 1 problem(s)", text)
        self.assertIn("practices/example.md:10: matches the local scrub list", text)
        self.assertNotIn("SecretClient", text)
        self.assertNotIn("secretclient", text.lower().replace("secretclient once", ""))

    def test_a_clean_tree_passes_with_a_denylist(self) -> None:
        deny = self.root.parent / "deny.txt"
        deny.write_text("SecretClient\n", encoding="utf-8")
        code, lines = run_check(self.root, denylist=deny)
        self.assertEqual(code, 0, "\n".join(lines))
        self.assertIn("PASS scrub", lines)

    def test_a_denylist_with_no_terms_says_so(self) -> None:
        deny = self.root.parent / "empty.txt"
        deny.write_text("# only a comment\n", encoding="utf-8")
        code, lines = run_check(self.root, denylist=deny)
        self.assertEqual(code, 0)
        self.assertTrue(any(line.startswith("UNVERIFIED scrub: no terms in") for line in lines))

    def test_no_denylist_is_unverified_not_a_failure(self) -> None:
        code, lines = run_check(self.root, denylist=self.root.parent / "absent.txt")
        self.assertEqual(code, 0)
        self.assertTrue(any(line.startswith("UNVERIFIED scrub: no local scrub list at") for line in lines))
        code, lines = run_check(self.root, denylist=None)
        self.assertEqual(code, 0)
        self.assertTrue(any(line.startswith("UNVERIFIED scrub: no local scrub list given") for line in lines))

    def test_the_agents_folder_and_git_are_not_scanned(self) -> None:
        deny = self.root.parent / "deny.txt"
        deny.write_text("SecretClient\n", encoding="utf-8")
        write(self.root, ".agents/work/notes.md", "SecretClient")
        write(self.root, ".git/config", "SecretClient")
        self.assertEqual(run_check(self.root, denylist=deny)[0], 0)

    def test_the_committed_agents_skills_are_scanned(self) -> None:
        deny = self.root.parent / "deny.txt"
        deny.write_text("SecretClient\n", encoding="utf-8")
        write(self.root, ".agents/skills/example/SKILL.md", "Seen at SecretClient.\n")
        code, lines = run_check(self.root, denylist=deny)
        self.assertEqual(code, 1, "\n".join(lines))
        self.assertIn(".agents/skills/example/SKILL.md:1: matches the local scrub list", "\n".join(lines))

    def test_a_linked_file_is_not_read(self) -> None:
        deny = self.root.parent / "deny.txt"
        deny.write_text("SecretClient\n", encoding="utf-8")
        outside = write(self.root.parent, "outside.md", "SecretClient\n")
        (self.root / "practices" / "linked.txt").symlink_to(outside)
        code, lines = run_check(self.root, denylist=deny)
        self.assertNotIn("matches the local scrub list", "\n".join(lines))
        self.assertIn("PASS scrub", lines)


class SymlinkTest(RepoCase):
    def test_a_linked_file_or_folder_fails_and_nothing_below_a_linked_folder_is_listed(self) -> None:
        outside = self.root.parent / "outside"
        write(outside, "a.txt", "text\n")
        (self.root / "practices" / "file-link.txt").symlink_to(outside / "a.txt")
        (self.root / "folder-link").symlink_to(outside, target_is_directory=True)
        problems = self.assertFails("symlinks", "practices/file-link.txt: a symbolic link")
        self.assertIn("folder-link: a symbolic link; commit the file itself", problems)
        self.assertFalse(any("folder-link/a.txt" in p for p in problems), problems)

    def test_a_link_in_the_ignored_workspace_is_not_judged(self) -> None:
        write(self.root, ".agents/work/a.txt", "text\n")
        (self.root / ".agents" / "work" / "link.txt").symlink_to(self.root / ".agents" / "work" / "a.txt")
        self.assertEqual(self.verdicts()[1]["symlinks"], "PASS")


class InvisibleTest(RepoCase):
    def test_each_invisible_class_fails_with_its_place_and_code_point(self) -> None:
        for code in (0x200B, 0x202E, 0x00AD, 0xFE0E, 0xFE00, 0xE0101, 0xE0041):
            with self.subTest(code=f"U+{code:04X}"):
                write(self.root, "practices/extra.txt", f"line one\nbefore{chr(code)}after\n")
                self.assertFails("invisible", f"practices/extra.txt:2: invisible or format character U+{code:04X}")

    def test_variation_selector_16_passes_only_after_an_emoji(self) -> None:
        write(self.root, "practices/extra.txt", "Warning \u26a0\ufe0f and keycap 1\ufe0f\u20e3 and \U0001f600\ufe0f\n")
        self.assertEqual(self.verdicts()[1]["invisible"], "PASS")
        write(self.root, "practices/extra.txt", "plain a\ufe0f text\n")
        self.assertFails("invisible", "practices/extra.txt:1: invisible or format character U+FE0F")
        write(self.root, "practices/extra.txt", "\ufe0f at the start\n")
        self.assertFails("invisible", "practices/extra.txt:1: invisible or format character U+FE0F")

    def test_an_escape_written_as_text_passes(self) -> None:
        write(self.root, "practices/extra.txt", "the JSON escape \\u200b is six characters of text\n")
        self.assertEqual(self.verdicts()[1]["invisible"], "PASS")


class StaleListTest(RepoCase):
    def test_stale_documents_and_cards_are_printed_and_do_not_fail(self) -> None:
        write(self.root, "practices/example.md", doc_text(checked="2026-01-01", volatility="VOLATILE (prices)"))
        refresh(self.root)
        code, lines = run_check(self.root)
        self.assertEqual(code, 0, "\n".join(lines))
        row = next(line for line in lines if line.startswith("  practices/example.md"))
        self.assertEqual(row, "  practices/example.md: checked 2026-01-01 (275 days ago), VOLATILE window 14 days, 261 over")
        self.assertIn("stale (printed, not gated): 1 past their window", lines)

    def test_windows_by_class(self) -> None:
        today = dt.date(2026, 10, 3)
        for klass, days in (("STABLE", 180), ("MONITOR", 30), ("VOLATILE", 14)):
            inside = (today - dt.timedelta(days=days)).isoformat()
            outside = (today - dt.timedelta(days=days + 1)).isoformat()
            write(self.root, "practices/example.md", doc_text(checked=inside, volatility=klass))
            self.assertEqual(check.stale_list(self.root, today), [], klass)
            write(self.root, "practices/example.md", doc_text(checked=outside, volatility=klass))
            self.assertEqual(len(check.stale_list(self.root, today)), 1, klass)

    def test_an_old_card_is_stale(self) -> None:
        self.set_card(checked="2026-09-01")
        lines = check.stale_list(self.root, TODAY)
        self.assertTrue(any(line.startswith(CARD_PATH) for line in lines), lines)

    def test_nothing_stale_says_so(self) -> None:
        _, lines = run_check(self.root)
        self.assertIn("stale (printed, not gated): none past their window", lines)

    def test_the_most_overdue_comes_first(self) -> None:
        write(self.root, "practices/a.md", doc_text(title="A", checked="2026-08-01", volatility="MONITOR"))
        write(self.root, "practices/b.md", doc_text(title="B", checked="2026-03-01", volatility="MONITOR"))
        rows = check.stale_list(self.root, TODAY)
        self.assertTrue(rows[0].startswith("practices/b.md"))


class HelpersTest(unittest.TestCase):
    def test_frontmatter_parser(self) -> None:
        data, body = check.parse_frontmatter("---\nlast_checked: 2026-10-01\nsources:\n  - https://a\n  - https://b\nempty: []\n---\n\n# T\n")  # type: ignore[misc]
        self.assertEqual(data, {"last_checked": "2026-10-01", "sources": ["https://a", "https://b"], "empty": []})
        self.assertEqual(check.title_of(body), "T")
        self.assertIsNone(check.parse_frontmatter("# no frontmatter\n"))

    def test_title_ignores_headings_in_code(self) -> None:
        self.assertEqual(check.title_of("```\n# not this\n```\n# This\n"), "This")

    def test_volatility_class(self) -> None:
        self.assertEqual(check.volatility_class("STABLE (x) / VOLATILE (y)"), "STABLE")
        self.assertIsNone(check.volatility_class("sometimes"))

    def test_main_runs_on_a_root_and_returns_the_exit_code(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = build_repo(Path(tmp))
            import contextlib
            import io

            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(check.main(["--root", str(root), "--today", "2026-10-03", "--denylist", str(root / "none")]), 0)
                write(root, "practices/example.md", "no frontmatter")
                self.assertEqual(check.main(["--root", str(root), "--today", "2026-10-03", "--denylist", str(root / "none")]), 1)

    def test_main_takes_allow_pending(self) -> None:
        import contextlib
        import io

        with tempfile.TemporaryDirectory() as tmp:
            root = build_repo(Path(tmp))
            write(root, "practices/example.md", doc_text(body=f"{layout.PENDING}\n"))
            refresh(root)
            args = ["--root", str(root), "--today", "2026-10-03", "--denylist", str(root / "none")]
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(check.main(args), 1)
                self.assertEqual(check.main(args + ["--allow-pending"]), 0)


if __name__ == "__main__":
    unittest.main()
