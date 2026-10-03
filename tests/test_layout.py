"""scripts/layout.py: the headings, the document readers and the stubs the other scripts rely on."""

from __future__ import annotations

import unittest

from tests.support import REPO, layout


class HeadingsTest(unittest.TestCase):
    def test_headings_are_read_outside_fenced_code_only(self) -> None:
        text = "# Title\n\n## One\n\n```\n## Not this\n```\n\n### Two ###\n\n#### Three\n"
        self.assertEqual(layout.headings(text), [(2, "One"), (3, "Two"), (4, "Three")])

    def test_missing_headings_names_what_is_absent_or_out_of_order(self) -> None:
        wanted = ((2, "A"), (2, "B"), (3, "C"))
        self.assertEqual(layout.missing_headings("## A\n## B\n### C\n", wanted), [])
        self.assertEqual(layout.missing_headings("## A\n## X\n## B\n### Y\n### C\n", wanted), [])
        self.assertEqual(layout.missing_headings("## A\n### C\n", wanted), ["## B"])
        self.assertEqual(layout.missing_headings("## B\n## A\n### C\n", wanted), ["## B"])
        self.assertEqual(layout.missing_headings("## A\n## B\n## C\n", wanted), ["### C"])
        self.assertEqual(layout.missing_headings("", wanted), ["## A", "## B", "### C"])

    def test_the_template_headings_are_unique_within_each_template(self) -> None:
        for template in (layout.MODEL_HEADINGS, layout.MAKER_HEADINGS, layout.PROVIDER_HEADINGS):
            self.assertEqual(len(template), len(set(template)))


class VoiceHeadingTest(unittest.TestCase):
    def test_audio_output_is_the_word_audio_alone_or_with_a_qualifier(self) -> None:
        def card(output: object) -> dict:
            return {"modalities": {"input": ["text"], "output": output}}

        self.assertTrue(layout.has_audio_output(card(["text", "audio"])))
        self.assertTrue(layout.has_audio_output(card(["Audio (speech only)"])))
        self.assertFalse(layout.has_audio_output(card(["text", "image"])))
        self.assertFalse(layout.has_audio_output(card(["audio-description"])), "a different word is not audio")
        self.assertFalse(layout.has_audio_output({"modalities": {"input": ["audio"], "output": ["text"]}}))
        for other in (None, [], {}, {"modalities": None}, {"modalities": {"output": "audio"}}):
            self.assertFalse(layout.has_audio_output(other))

    def test_the_voice_subsection_follows_the_images_and_audio_subsection(self) -> None:
        plain = layout.model_headings()
        self.assertEqual(plain, layout.MODEL_HEADINGS)
        voice = list(layout.model_headings(voice=True))
        self.assertEqual(len(voice), len(plain) + 1)
        index = voice.index((3, "Images, audio, other inputs"))
        self.assertEqual(voice[index + 1], layout.VOICE_HEADING)
        self.assertEqual(layout.VOICE_HEADING, (3, "Voice: turn-taking, interruption and speech style"))
        self.assertEqual([h for h in voice if h != layout.VOICE_HEADING], list(plain))

    def test_a_voice_stub_holds_the_subsection_and_a_plain_stub_does_not(self) -> None:
        plain = layout.model_stub("Example", "2026-10-03", ["https://example.com/a"])
        voice = layout.model_stub("Example", "2026-10-03", ["https://example.com/a"], voice=True)
        self.assertNotIn(layout.VOICE_HEADING, layout.headings(plain))
        self.assertEqual(layout.missing_headings(voice, layout.model_headings(voice=True)), [])
        self.assertEqual(voice.count(layout.PENDING), plain.count(layout.PENDING) + 1)


class StubTest(unittest.TestCase):
    def test_a_model_stub_holds_every_heading_in_order_and_an_empty_card_block(self) -> None:
        text = layout.model_stub("Example", "2026-10-03", ["https://example.com/a", "https://example.com/b"])
        self.assertEqual(layout.missing_headings(text, layout.MODEL_HEADINGS), [])
        self.assertIn(f"{layout.CARD_BEGIN}\n{layout.CARD_END}\n", text)
        data, body = layout.parse_frontmatter(text)  # type: ignore[misc]
        self.assertEqual(data["sources"], ["https://example.com/a", "https://example.com/b"])
        self.assertEqual(data["last_checked"], "2026-10-03")
        self.assertEqual(layout.title_of(body), "Example")
        # The introduction and every section but the glance and the parent of the topics hold the placeholder.
        self.assertEqual(text.count(layout.PENDING), 1 + len(layout.MODEL_HEADINGS) - 2)
        self.assertTrue(text.endswith("\n") and not text.endswith("\n\n"))

    def test_a_maker_stub_and_a_provider_stub_hold_their_headings_and_the_placeholder_in_each(self) -> None:
        maker = layout.maker_stub("Maker", "2026-10-03", ["https://example.com/a"])
        self.assertEqual(layout.missing_headings(maker, layout.MAKER_HEADINGS), [])
        self.assertEqual(maker.count(layout.PENDING), 1 + len(layout.MAKER_HEADINGS))
        provider = layout.provider_stub("Host", "local runtime", "2026-10-03", ["https://example.com/a"])
        self.assertEqual(layout.missing_headings(provider, layout.PROVIDER_HEADINGS), [])
        self.assertEqual(provider.count(layout.PENDING), 1 + len(layout.PROVIDER_HEADINGS))
        data, _ = layout.parse_frontmatter(provider)  # type: ignore[misc]
        self.assertEqual(data["kind"], "local runtime")

    def test_the_placeholder_is_not_spelled_out_in_any_script(self) -> None:
        self.assertEqual(layout.PENDING, "PENDING-" + "STUB")
        for path in (REPO / "scripts").glob("*.py"):
            self.assertNotIn(layout.PENDING, path.read_text(encoding="utf-8"), str(path))

    def test_the_provider_kinds_are_the_five_the_design_names(self) -> None:
        self.assertEqual(
            layout.PROVIDER_KINDS,
            ("first-party lab API", "cloud platform", "router or gateway", "inference host", "local runtime"),
        )


if __name__ == "__main__":
    unittest.main()
