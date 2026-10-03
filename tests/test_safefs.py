"""scripts/safefs.py: writes below a root that never follow a symbolic link."""

from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from tests.support import safefs


class SafeFsTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name) / "root"
        self.root.mkdir()
        self.outside = Path(self._tmp.name) / "outside"
        self.outside.mkdir()

    def test_write_text_creates_folders_and_replaces_a_longer_file(self) -> None:
        safefs.write_text(self.root, "a/b/c.txt", "a long first text\n")
        safefs.write_text(self.root, "a/b/c.txt", "short\n")
        self.assertEqual((self.root / "a/b/c.txt").read_text(encoding="utf-8"), "short\n")

    def test_create_text_writes_once_accepts_the_same_text_and_refuses_other_text(self) -> None:
        self.assertTrue(safefs.create_text(self.root, "q/x.json", "one\n"))
        self.assertFalse(safefs.create_text(self.root, "q/x.json", "one\n"))
        with self.assertRaisesRegex(safefs.UnsafePath, "different content"):
            safefs.create_text(self.root, "q/x.json", "two\n")
        self.assertEqual((self.root / "q/x.json").read_text(encoding="utf-8"), "one\n")

    def test_append_text_adds_to_the_end(self) -> None:
        safefs.append_text(self.root, "log/seen.jsonl", "a\n")
        safefs.append_text(self.root, "log/seen.jsonl", "b\n")
        self.assertEqual((self.root / "log/seen.jsonl").read_text(encoding="utf-8"), "a\nb\n")

    def test_a_linked_file_is_refused_by_every_writer_and_the_reader(self) -> None:
        target = self.outside / "t.txt"
        target.write_text("keep\n", encoding="utf-8")
        os.symlink(target, self.root / "link.txt")
        for action in (
            lambda: safefs.write_text(self.root, "link.txt", "x"),
            lambda: safefs.create_text(self.root, "link.txt", "x"),
            lambda: safefs.append_text(self.root, "link.txt", "x"),
            lambda: safefs.read_bytes(self.root, "link.txt", 10),
            lambda: safefs.refuse_links(self.root, "link.txt"),
        ):
            with self.assertRaises(safefs.UnsafePath):
                action()
        self.assertEqual(target.read_text(encoding="utf-8"), "keep\n")

    def test_a_linked_folder_anywhere_above_is_refused(self) -> None:
        os.symlink(self.outside, self.root / "dir")
        for rel in ("dir/f.txt", "dir/deeper/f.txt"):
            with self.assertRaises(safefs.UnsafePath):
                safefs.write_text(self.root, rel, "x")
            with self.assertRaises(safefs.UnsafePath):
                safefs.refuse_links(self.root, rel)
        self.assertEqual(list(self.outside.iterdir()), [])

    def test_a_folder_where_a_file_goes_and_a_file_where_a_folder_goes_are_refused(self) -> None:
        (self.root / "d").mkdir()
        (self.root / "f").write_text("x", encoding="utf-8")
        with self.assertRaises(OSError):
            safefs.write_text(self.root, "d", "x")
        with self.assertRaises(safefs.UnsafePath):
            safefs.write_text(self.root, "f/g.txt", "x")
        with self.assertRaises(safefs.UnsafePath):
            safefs.refuse_links(self.root, "f/g.txt")

    def test_refuse_links_allows_missing_steps_and_plain_ones(self) -> None:
        safefs.refuse_links(self.root, "a/b/c.txt")
        (self.root / "a").mkdir()
        (self.root / "a/c.txt").write_text("x", encoding="utf-8")
        safefs.refuse_links(self.root, "a/c.txt")
        safefs.refuse_links(self.root, "a", folder=True)

    def test_paths_that_leave_the_root_are_refused(self) -> None:
        for rel in ("../x", "a/../x", "/abs", ""):
            with self.subTest(rel=rel), self.assertRaises(safefs.UnsafePath):
                safefs.write_text(self.root, rel, "x")

    @unittest.skipUnless(hasattr(os, "mkfifo"), "needs named pipes")
    def test_a_named_pipe_is_refused_without_blocking(self) -> None:
        os.mkfifo(self.root / "pipe")
        with self.assertRaises(OSError):
            safefs.write_text(self.root, "pipe", "x")
        with self.assertRaises(safefs.UnsafePath):
            safefs.refuse_links(self.root, "pipe")

    def test_a_root_reached_through_a_link_is_trusted(self) -> None:
        link = Path(self._tmp.name) / "rootlink"
        os.symlink(self.root, link)
        safefs.write_text(link, "f.txt", "x")
        self.assertEqual((self.root / "f.txt").read_text(encoding="utf-8"), "x")


if __name__ == "__main__":
    unittest.main()
