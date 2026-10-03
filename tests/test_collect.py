"""scripts/collect.py: what is refused, deduplicated and queued."""

from __future__ import annotations

import contextlib
import datetime as dt
import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tests.support import HERE, TODAY, collect, write

FIXTURES = HERE / "fixtures" / "findings"

GOOD = {
    "version": 1,
    "kind": "fact",
    "subject": "claude-opus-5-5",
    "claim": "The model accepts an effort setting of xhigh.",
    "url": "https://example.com/page",
    "quote": "effort of xhigh",
    "observed_on": "2026-10-02",
}
INBOX = ".outcomebound/research-inbox"


def finding(**changes: object) -> dict:
    data = dict(GOOD)
    data.update(changes)
    return {k: v for k, v in data.items() if v is not ...}


def refusal(data: object) -> str:
    try:
        collect.validate_finding(data, TODAY)
    except collect.Refused as reason:
        return str(reason)
    raise AssertionError("not refused")


class FindingValidationTest(unittest.TestCase):
    def test_a_good_finding_passes_with_and_without_optional_keys(self) -> None:
        self.assertEqual(collect.validate_finding(finding(), TODAY)["kind"], "fact")
        bare = finding(quote=...)
        self.assertNotIn("quote", collect.validate_finding(bare, TODAY))
        self.assertEqual(collect.validate_finding(finding(quote=None), TODAY)["quote"], None)

    def test_a_correction_must_name_what_it_corrects(self) -> None:
        self.assertEqual(refusal(finding(kind="correction")), "a correction names what it corrects in `corrects`")
        ok = finding(kind="correction", corrects="anthropic-17")
        self.assertEqual(collect.validate_finding(ok, TODAY)["corrects"], "anthropic-17")

    def test_refusals_say_why(self) -> None:
        self.assertEqual(refusal([1]), "not a JSON object")
        self.assertEqual(refusal(finding(extra="x")), "unknown key(s): extra")
        self.assertEqual(refusal(finding(url=...)), "missing key(s): url")
        self.assertEqual(refusal(finding(version=2)), "version is not 1")
        self.assertEqual(refusal(finding(kind="opinion")), "kind is not one of fact, correction")
        self.assertEqual(refusal(finding(claim=7)), "claim is not text")
        self.assertEqual(refusal(finding(claim="   ")), "claim is empty")
        self.assertEqual(refusal(finding(url="javascript:alert(1)")), "url is not an http(s) address")
        self.assertEqual(refusal(finding(url="https://a b.example")), "url is not an http(s) address")
        self.assertEqual(refusal(finding(observed_on="2026-13-01")), "observed_on is not an ISO date")
        self.assertEqual(refusal(finding(observed_on="2026-10-05")), "observed_on is in the future")
        self.assertEqual(collect.validate_finding(finding(observed_on="2026-10-04"), TODAY)["observed_on"], "2026-10-04")
        self.assertEqual(refusal(finding(claim="x" * 2001)), "claim is over 2000 characters")
        self.assertEqual(collect.validate_finding(finding(claim="x" * 2000), TODAY)["claim"], "x" * 2000)

    def test_the_quote_limit_is_25_words(self) -> None:
        self.assertIsNotNone(collect.validate_finding(finding(quote=" ".join(["w"] * 25)), TODAY))
        self.assertEqual(refusal(finding(quote=" ".join(["w"] * 26))), "quote is over 25 words")

    def test_control_and_invisible_characters_are_refused(self) -> None:
        self.assertIn("control or invisible character (U+000A)", refusal(finding(claim="two\nlines")))
        self.assertIn("(U+200B)", refusal(finding(claim="zero\u200bwidth")))
        self.assertIn("(U+E0041)", refusal(finding(claim="tag\U000e0041char")))
        self.assertIn("(U+202E)", refusal(finding(subject="rtl\u202eoverride")))


class SharedFixturesTest(unittest.TestCase):
    """Every case in tests/fixtures/findings/ gets the verdict its expect file names."""

    def cases(self) -> list[Path]:
        return sorted(FIXTURES.glob("*.expect.json"))

    def test_there_are_enough_cases_and_each_has_a_finding_file(self) -> None:
        cases = self.cases()
        self.assertGreaterEqual(len(cases), 25)
        for expect in cases:
            self.assertTrue((FIXTURES / expect.name.replace(".expect.json", ".json")).is_file(), expect.name)

    def test_every_case_gets_its_verdict(self) -> None:
        for expect_path in self.cases():
            name = expect_path.name.replace(".expect.json", "")
            expect = json.loads(expect_path.read_text(encoding="utf-8"))
            data = json.loads((FIXTURES / f"{name}.json").read_text(encoding="utf-8"))
            today = dt.date.fromisoformat(expect["today"])
            with self.subTest(case=name):
                try:
                    collect.validate_finding(data, today)
                    verdict = "accept"
                except collect.Refused:
                    verdict = "refuse"
                self.assertEqual(verdict, expect["verdict"], expect["rule"])

    def test_the_cases_cover_every_rule_on_both_sides_of_its_boundary(self) -> None:
        by_rule: dict[str, set[str]] = {}
        for expect_path in self.cases():
            expect = json.loads(expect_path.read_text(encoding="utf-8"))
            by_rule.setdefault(expect["rule"], set()).add(expect["verdict"])
        for rule in (
            "subject-length", "claim-length", "url-length", "quote-words", "quote-characters",
            "corrects-length", "date-future", "url-scheme", "corrects",
        ):
            self.assertEqual(by_rule.get(rule), {"accept", "refuse"}, rule)
        for rule in (
            "kind", "url-host", "url-userinfo", "url-parsable", "url-space", "date-format",
            "text-one-line", "text-control", "text-format", "text-utf8", "shape",
        ):
            self.assertEqual(by_rule.get(rule), {"refuse"}, rule)

    def test_every_accepted_case_serialises_to_a_file_the_reader_takes(self) -> None:
        for expect_path in self.cases():
            expect = json.loads(expect_path.read_text(encoding="utf-8"))
            if expect["verdict"] != "accept":
                continue
            name = expect_path.name.replace(".expect.json", "")
            data = json.loads((FIXTURES / f"{name}.json").read_text(encoding="utf-8"))
            raw = json.dumps(data, sort_keys=True, ensure_ascii=False, indent=2) + "\n"
            self.assertLessEqual(len(raw.encode("utf-8")), collect.MAX_BYTES, name)


class CollectTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp = Path(self._tmp.name)
        self.obr = self.tmp / "obr"
        self.obr.mkdir()
        self.projects = self.tmp / "projects"
        self.projects.mkdir()

    def inbox(self, project: str, name: str, data: object, raw: str | None = None) -> Path:
        text = raw if raw is not None else json.dumps(data, sort_keys=True)
        return write(self.projects, f"{project}/{INBOX}/{name}", text)

    def collect(self, **kwargs: object) -> dict[str, list[str]]:
        defaults: dict = {"obr": self.obr, "denylist": None, "today": TODAY}
        defaults.update(kwargs)
        return collect.collect([self.projects], **defaults)

    def queued_files(self) -> list[Path]:
        return sorted((self.obr / "ingest" / "queue").glob("*.json"))

    def test_a_finding_is_queued_with_its_digest_and_recorded_as_seen(self) -> None:
        self.inbox("alpha", "20261002-aaaaaaaa.json", GOOD)
        report = self.collect()
        self.assertEqual(len(report["queued"]), 1)
        sha = collect.digest(GOOD["claim"], GOOD["url"])
        (queued,) = self.queued_files()
        self.assertEqual(queued.name, f"20261003-{sha}.json")
        entry = json.loads(queued.read_text(encoding="utf-8"))
        self.assertEqual(entry["sha256"], sha)
        self.assertEqual(entry["collected_on"], "2026-10-03")
        self.assertEqual({k: v for k, v in entry.items() if k not in ("sha256", "collected_on")}, GOOD)
        seen = (self.obr / "ingest" / "seen.jsonl").read_text(encoding="utf-8").strip().split("\n")
        self.assertEqual([json.loads(line)["sha256"] for line in seen], [sha])

    def test_the_digest_is_sha256_of_claim_then_url(self) -> None:
        import hashlib

        self.assertEqual(collect.digest("c", "u"), hashlib.sha256(b"cu").hexdigest())

    def test_a_worktree_is_searched_and_the_same_finding_twice_is_one(self) -> None:
        self.inbox("alpha", "20261002-aaaaaaaa.json", GOOD)
        self.inbox("alpha/.agents/worktrees/task", "20261002-aaaaaaaa.json", GOOD)
        report = self.collect()
        self.assertEqual((len(report["queued"]), len(report["duplicate"])), (1, 1))
        self.assertEqual(len(self.queued_files()), 1)

    def test_a_second_run_finds_only_duplicates(self) -> None:
        self.inbox("alpha", "20261002-aaaaaaaa.json", GOOD)
        self.collect()
        report = self.collect()
        self.assertEqual((len(report["queued"]), len(report["duplicate"])), (0, 1))
        self.assertEqual(len((self.obr / "ingest" / "seen.jsonl").read_text(encoding="utf-8").strip().split("\n")), 1)

    def test_a_removed_queue_entry_is_not_queued_again(self) -> None:
        self.inbox("alpha", "20261002-aaaaaaaa.json", GOOD)
        self.collect()
        self.queued_files()[0].unlink()
        self.collect()
        self.assertEqual(self.queued_files(), [])

    def test_refusals(self) -> None:
        self.inbox("a", "1.json", None, raw="not json")
        self.inbox("b", "2.json", None, raw=json.dumps(GOOD) + " " * 17000)
        self.inbox("c", "3.json", finding(kind="opinion"))
        (self.projects / "d" / INBOX).mkdir(parents=True)
        (self.projects / "d" / INBOX / "4.json").write_bytes(b'{"claim": "\xff\xfe"}')
        (self.projects / "e" / INBOX).mkdir(parents=True)
        target = self.tmp / "outside.json"
        target.write_text(json.dumps(GOOD), encoding="utf-8")
        os.symlink(target, self.projects / "e" / INBOX / "5.json")
        report = self.collect()
        self.assertEqual(report["queued"], [])
        reasons = sorted(line.split(": ", 1)[1] for line in report["refused"])
        self.assertEqual(
            reasons,
            sorted(["not UTF-8 JSON", "over 16384 bytes", "kind is not one of fact, correction", "not UTF-8 JSON", "not a regular file"]),
        )
        self.assertEqual(self.queued_files(), [])

    def test_a_non_json_name_in_the_inbox_is_ignored(self) -> None:
        write(self.projects, f"a/{INBOX}/notes.txt", "x")
        self.assertEqual(self.collect(), {"queued": [], "duplicate": [], "refused": []})

    def test_inboxes_elsewhere_are_not_read(self) -> None:
        write(self.projects, "a/node_modules/pkg/.outcomebound/research-inbox/1.json", json.dumps(GOOD))
        write(self.projects, "a/other/research-inbox/1.json", json.dumps(GOOD))
        self.assertEqual(self.collect()["queued"], [])

    def test_the_denylist_refuses_without_naming_the_term(self) -> None:
        deny = self.tmp / "deny.txt"
        deny.write_text("# private names\n\nAcme Corp\n", encoding="utf-8")
        self.inbox("a", "1.json", finding(claim="We saw this at acme corp last week."))
        self.inbox("b", "2.json", finding(claim="Acme Corporation-like words are not a whole-word match."))
        report = self.collect(denylist=deny)
        self.assertEqual(len(report["refused"]), 1)
        self.assertTrue(report["refused"][0].endswith("matches the local scrub list"))
        self.assertNotIn("Acme", "".join(report["refused"]))
        self.assertEqual(len(report["queued"]), 1)

    def test_the_denylist_matches_the_decoded_text_and_any_unicode_form(self) -> None:
        deny = self.tmp / "deny.txt"
        deny.write_text("M\u00fcller GmbH\n", encoding="utf-8")
        escaped = json.dumps(finding(claim="Seen at M\u00fcller GmbH."), ensure_ascii=True)
        self.assertIn("\\u00fc", escaped)
        self.inbox("a", "1.json", None, raw=escaped)
        decomposed = json.dumps(finding(claim="Seen at Mu\u0308ller GmbH again."), ensure_ascii=False)
        self.inbox("b", "2.json", None, raw=decomposed)
        report = self.collect(denylist=deny)
        self.assertEqual((len(report["refused"]), len(report["queued"])), (2, 0))

    @unittest.skipUnless(hasattr(os, "mkfifo"), "needs named pipes")
    def test_a_named_pipe_is_refused_without_blocking(self) -> None:
        (self.projects / "a" / INBOX).mkdir(parents=True)
        os.mkfifo(self.projects / "a" / INBOX / "1.json")
        report = self.collect()
        self.assertEqual([line.split(": ", 1)[1] for line in report["refused"]], ["not a regular file"])

    def test_a_symbolic_link_to_an_inbox_directory_is_reported(self) -> None:
        real = self.tmp / "elsewhere"
        write(real, "1.json", json.dumps(GOOD))
        (self.projects / "a" / ".outcomebound").mkdir(parents=True)
        os.symlink(real, self.projects / "a" / INBOX)
        report = self.collect()
        self.assertEqual(report["queued"], [])
        self.assertEqual(len(report["refused"]), 1)
        self.assertIn("symbolic link to an inbox directory", report["refused"][0])

    def test_a_bad_line_in_seen_jsonl_is_an_error_with_its_line_number(self) -> None:
        write(self.obr, "ingest/seen.jsonl", "{broken\n")
        self.inbox("a", "1.json", GOOD)
        with self.assertRaisesRegex(ValueError, r"seen.jsonl:1: not a JSON object"):
            self.collect()

    def test_a_missing_denylist_applies_nothing(self) -> None:
        self.inbox("a", "1.json", GOOD)
        self.assertEqual(len(self.collect(denylist=self.tmp / "absent.txt")["queued"]), 1)

    def test_dry_run_writes_nothing(self) -> None:
        self.inbox("a", "1.json", GOOD)
        report = self.collect(dry_run=True)
        self.assertEqual(len(report["queued"]), 1)
        self.assertFalse((self.obr / "ingest").exists())

    def test_nothing_is_written_into_the_project(self) -> None:
        path = self.inbox("a", "1.json", GOOD)
        before = path.read_bytes()
        self.collect()
        self.assertEqual(path.read_bytes(), before)
        self.assertEqual(sorted(p.name for p in path.parent.iterdir()), ["1.json"])


class CollectSafetyTest(unittest.TestCase):
    """Queue names, collisions, malformed files and links."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp = Path(self._tmp.name)
        self.obr = self.tmp / "obr"
        self.obr.mkdir()
        self.projects = self.tmp / "projects"
        self.projects.mkdir()
        self.outside = self.tmp / "outside"
        self.outside.mkdir()

    def inbox(self, name: str, data: object = None, raw: str | None = None, project: str = "a") -> Path:
        text = raw if raw is not None else json.dumps(data, sort_keys=True)
        return write(self.projects, f"{project}/{INBOX}/{name}", text)

    def collect(self, **kwargs: object) -> dict[str, list[str]]:
        defaults: dict = {"obr": self.obr, "denylist": None, "today": TODAY}
        defaults.update(kwargs)
        return collect.collect([self.projects], **defaults)

    def queue(self) -> Path:
        return self.obr / "ingest" / "queue"

    def seen_digests(self) -> list[str]:
        path = self.obr / "ingest" / "seen.jsonl"
        if not path.exists():
            return []
        return [json.loads(line)["sha256"] for line in path.read_text(encoding="utf-8").splitlines()]

    # Queue names

    def test_two_findings_whose_digests_share_eight_digits_get_two_files(self) -> None:
        # These two claims share their first eight hex digits (9856a06c) with the same url.
        first = finding(claim="synthetic observation 7770", url="https://example.org/source")
        second = finding(claim="synthetic observation 12127", url="https://example.org/source")
        one, two = (collect.digest(f["claim"], f["url"]) for f in (first, second))
        self.assertEqual(one[:8], two[:8])
        self.assertNotEqual(one, two)
        self.inbox("1.json", first)
        self.inbox("2.json", second)
        report = self.collect()
        self.assertEqual(len(report["queued"]), 2)
        self.assertEqual(sorted(p.name for p in self.queue().glob("*.json")), sorted([f"20261003-{one}.json", f"20261003-{two}.json"]))
        self.assertEqual(sorted(self.seen_digests()), sorted([one, two]))

    def test_a_queue_file_with_other_content_is_never_overwritten(self) -> None:
        data = finding()
        sha = collect.digest(data["claim"], data["url"])
        planted = write(self.obr, f"ingest/queue/20261003-{sha}.json", "something else\n")
        self.inbox("1.json", data)
        report = self.collect()
        self.assertEqual(report["queued"], [])
        self.assertEqual(len(report["refused"]), 1)
        self.assertIn("different content", report["refused"][0])
        self.assertEqual(planted.read_text(encoding="utf-8"), "something else\n")
        self.assertEqual(self.seen_digests(), [])

    def test_a_queue_file_with_the_same_content_is_kept_and_recorded(self) -> None:
        self.inbox("1.json", finding())
        self.collect()
        (self.obr / "ingest" / "seen.jsonl").unlink()  # a run that stopped before it was recorded
        report = self.collect()
        self.assertEqual((len(report["queued"]), len(report["refused"])), (1, 0))
        self.assertEqual(len(self.seen_digests()), 1)
        self.assertEqual(len(list(self.queue().glob("*.json"))), 1)

    def test_a_finding_is_recorded_as_seen_only_after_its_file_is_written(self) -> None:
        self.inbox("1.json", finding())
        order: list[str] = []
        real_create, real_append = collect.safefs.create_text, collect.safefs.append_text

        def create(*args: object, **kwargs: object) -> bool:
            order.append("queue")
            return real_create(*args, **kwargs)

        def append(*args: object, **kwargs: object) -> None:
            order.append("seen")
            real_append(*args, **kwargs)

        with mock.patch.object(collect.safefs, "create_text", create), mock.patch.object(collect.safefs, "append_text", append):
            self.collect()
        self.assertEqual(order, ["queue", "seen"])

    # Malformed findings

    def test_a_malformed_url_or_text_is_refused_and_collection_goes_on(self) -> None:
        self.inbox("1.json", finding(url="https://[invalid"))
        self.inbox("2.json", None, raw='{"version": 1, "kind": "fact", "subject": "s", "claim": "bad \\ud800 text", '
                   '"url": "https://example.com/p", "observed_on": "2026-10-02"}')
        self.inbox("3.json", None, raw="[" * 9000)
        self.inbox("4.json", finding(claim="A good finding that comes last."))
        report = self.collect()
        self.assertEqual(len(report["queued"]), 1)
        self.assertEqual(len(report["refused"]), 3)
        reasons = " | ".join(report["refused"])
        self.assertIn("url cannot be parsed", reasons)
        self.assertIn("unpaired surrogate", reasons)
        self.assertEqual(len(self.seen_digests()), 1)
        self.assertEqual(len(list(self.queue().glob("*.json"))), 1)

    def test_the_validator_refuses_what_it_cannot_encode_or_parse(self) -> None:
        self.assertEqual(refusal(finding(claim="a \ud800 b")), "claim is not valid UTF-8 text (an unpaired surrogate)")
        self.assertEqual(refusal(finding(url="https://[invalid")), "url cannot be parsed")
        self.assertEqual(refusal(finding(url="https://user:pw@example.com/")), "url holds a user name or password")
        self.assertEqual(refusal(finding(url="https://example.com/" + "a" * 2000)), "url is over 2000 characters")
        self.assertIn("(U+200B)", refusal(finding(subject="zero\u200bwidth")))
        self.assertEqual(refusal(finding(quote="a" * 301)), "quote is over 300 characters")

    # Links

    def test_a_linked_queue_folder_stops_the_pass_before_any_write(self) -> None:
        (self.obr / "ingest").mkdir()
        os.symlink(self.outside, self.obr / "ingest" / "queue")
        self.inbox("1.json", finding())
        with self.assertRaisesRegex(ValueError, "will not write through a link"):
            self.collect()
        self.assertEqual(list(self.outside.iterdir()), [])
        self.assertEqual(self.seen_digests(), [])

    def test_a_linked_ingest_folder_stops_the_pass_before_any_write(self) -> None:
        os.symlink(self.outside, self.obr / "ingest")
        self.inbox("1.json", finding())
        with self.assertRaisesRegex(ValueError, "will not write through a link"):
            self.collect()
        self.assertEqual(list(self.outside.iterdir()), [])

    def test_a_linked_seen_file_is_refused_and_its_target_is_left_alone(self) -> None:
        target = self.outside / "target.txt"
        target.write_text("keep me\n", encoding="utf-8")
        (self.obr / "ingest").mkdir()
        os.symlink(target, self.obr / "ingest" / "seen.jsonl")
        self.inbox("1.json", finding())
        with self.assertRaisesRegex(ValueError, "will not write through a link"):
            self.collect()
        self.assertEqual(target.read_text(encoding="utf-8"), "keep me\n")
        self.assertFalse(self.queue().exists())

    def test_a_dry_run_also_refuses_a_linked_seen_file(self) -> None:
        (self.obr / "ingest").mkdir()
        os.symlink(self.outside / "elsewhere", self.obr / "ingest" / "seen.jsonl")
        with self.assertRaisesRegex(ValueError, "will not write through a link"):
            self.collect(dry_run=True)

    def test_a_linked_queue_file_is_refused_and_its_target_is_left_alone(self) -> None:
        data = finding()
        sha = collect.digest(data["claim"], data["url"])
        target = self.outside / "target.txt"
        target.write_text("keep me\n", encoding="utf-8")
        self.queue().mkdir(parents=True)
        os.symlink(target, self.queue() / f"20261003-{sha}.json")
        self.inbox("1.json", data)
        report = self.collect()
        self.assertEqual(report["queued"], [])
        self.assertEqual(len(report["refused"]), 1)
        self.assertEqual(target.read_text(encoding="utf-8"), "keep me\n")
        self.assertEqual(self.seen_digests(), [])

    def test_a_dangling_link_at_the_queue_file_is_refused_too(self) -> None:
        data = finding()
        sha = collect.digest(data["claim"], data["url"])
        self.queue().mkdir(parents=True)
        os.symlink(self.outside / "not-yet", self.queue() / f"20261003-{sha}.json")
        self.inbox("1.json", data)
        report = self.collect()
        self.assertEqual(len(report["refused"]), 1)
        self.assertFalse((self.outside / "not-yet").exists())

    def test_a_link_swapped_in_after_the_checks_is_still_not_followed(self) -> None:
        target = self.outside / "target.txt"
        target.write_text("keep me\n", encoding="utf-8")
        self.inbox("1.json", finding())
        real = collect.load_seen

        def swap(root: Path, rel: str) -> set[str]:
            result = real(root, rel)  # the checks have passed; now put a link in the way
            (root / "ingest").mkdir(exist_ok=True)
            os.symlink(target, root / "ingest" / "seen.jsonl")
            return result

        with mock.patch.object(collect, "load_seen", swap):
            report = self.collect()
        self.assertEqual(target.read_text(encoding="utf-8"), "keep me\n")
        self.assertEqual(report["queued"], [])
        self.assertIn("not recorded as seen", report["refused"][0])


class MainTest(unittest.TestCase):
    def run_main(self, *args: str) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            try:
                code = collect.main(list(args))
            except SystemExit as stop:
                code = int(stop.code or 0)
        return code, out.getvalue()

    def test_no_root_is_a_usage_error(self) -> None:
        self.assertEqual(self.run_main()[0], 2)

    def test_a_root_that_is_not_a_directory_exits_2(self) -> None:
        self.assertEqual(self.run_main("--root", "/no/such/dir")[0], 2)

    def test_a_bad_seen_file_exits_2(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            obr = Path(tmp) / "obr"
            write(obr, "ingest/seen.jsonl", "{broken\n")
            write(Path(tmp), f"p/{INBOX}/1.json", json.dumps(finding(observed_on=dt.date.today().isoformat())))
            with mock.patch.object(collect, "ROOT", obr):
                code, _ = self.run_main("--root", str(Path(tmp) / "p"), "--dry-run", "--no-denylist")
        self.assertEqual(code, 2)

    def test_dry_run_prints_the_summary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            write(Path(tmp), f"p/{INBOX}/1.json", json.dumps(finding(observed_on=dt.date.today().isoformat())))
            code, out = self.run_main("--root", tmp, "--dry-run", "--no-denylist")
        self.assertEqual(code, 0)
        self.assertIn("collect: 1 queued, 0 duplicate, 0 refused (dry run, nothing written)", out)

    def run_main_err(self, *args: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = collect.main(list(args))
        return code, out.getvalue(), err.getvalue()

    def test_a_missing_or_empty_denylist_stops_before_anything_is_read(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            obr = Path(tmp) / "obr"
            obr.mkdir()
            write(Path(tmp), f"p/{INBOX}/1.json", json.dumps(finding(observed_on=dt.date.today().isoformat())))
            empty = write(Path(tmp), "empty.txt", "# only a comment\n")
            with mock.patch.object(collect, "ROOT", obr), mock.patch.dict(os.environ, {collect.DENYLIST_ENV: ""}):
                for given in (["--denylist", os.path.join(tmp, "absent.txt")], ["--denylist", str(empty)], []):
                    with self.subTest(given=given):
                        code, out, err = self.run_main_err("--root", str(Path(tmp) / "p"), *given)
                        self.assertEqual(code, 2)
                        self.assertEqual(err, "collect: UNVERIFIED scrub: no denylist, nothing was matched\n")
                        self.assertEqual(out, "")
            self.assertFalse((obr / "ingest").exists())

    def test_the_environment_variable_names_the_denylist(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            write(Path(tmp), f"p/{INBOX}/1.json", json.dumps(finding(observed_on=dt.date.today().isoformat())))
            deny = write(Path(tmp), "deny.txt", "SomeClient\n")
            with mock.patch.dict(os.environ, {collect.DENYLIST_ENV: str(deny)}):
                self.assertEqual(collect.default_denylist(), deny)
                code, out = self.run_main("--root", str(Path(tmp) / "p"), "--dry-run")
            self.assertEqual(code, 0)
            self.assertIn("collect: 1 queued", out)


if __name__ == "__main__":
    unittest.main()
