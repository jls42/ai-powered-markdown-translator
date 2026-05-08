"""Tests pour les options --note_position et --note_format de la note de traduction.

Couvre :
- Rétrocompat byte-for-byte du défaut (legacy + bottom) avec v1.9.
- Helpers purs : _build_translation_note_block, _compose_with_notes,
  _split_frontmatter, _sanitize_model.
- Format marker : link reference definition + blockquote en gras, multi-ligne.
- Insertion top/both APRÈS le frontmatter YAML (Astro Content Collections).
- Format du marker conforme au regex canonique.

Lancement : python -m unittest tests.test_translation_note_position -v
"""

import os
import sys
import tempfile
import unittest
from argparse import Namespace
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import translate
from translate import (
    _append_translation_note,
    _build_translation_note_block,
    _build_translation_note_source,
    _compose_with_notes,
    _quote_lines,
    _sanitize_model,
    _split_frontmatter,
    translate_markdown_file,
)


def _args(**overrides):
    defaults = {
        "model": "gpt-5-mini",
        "source_lang": "fr",
        "target_lang": "en",
        "news": False,
        "reasoning_effort": "medium",
        "note_position": "bottom",
        "note_format": "legacy",
    }
    defaults.update(overrides)
    return Namespace(**defaults)


def _make_openai_response(content):
    return MagicMock(choices=[MagicMock(message=MagicMock(content=content), finish_reason="stop")])


class TestBuildBlock(unittest.TestCase):
    def test_build_block_legacy_is_pure_strong(self):
        args = _args()
        out = _build_translation_note_block(args, "Translated note.", "bottom", "legacy")
        self.assertEqual(out, "**Translated note.**")

    def test_build_block_marker_top_is_pure_no_newlines_around(self):
        args = _args()
        out = _build_translation_note_block(args, "Translated note.", "top", "marker")
        self.assertFalse(out.startswith("\n"))
        self.assertFalse(out.endswith("\n"))
        self.assertTrue(out.startswith("[ai-translation-note-top]: <> "))

    def test_build_block_marker_wraps_translation_in_bold(self):
        args = _args()
        out = _build_translation_note_block(args, "Translated note.", "top", "marker")
        self.assertIn("> **Translated note.**", out)

    def test_marker_format_regex(self):
        args = _args(model="gpt-5-mini")
        out = _build_translation_note_block(args, "x", "top", "marker")
        first_line = out.splitlines()[0]
        pattern = (
            r"^\[ai-translation-note-(top|bottom)\]: <> "
            r'"v=1 source=[a-z]{2,3}(-[A-Z]{2})? target=[a-z]{2,3}(-[A-Z]{2})? '
            r'model=\S+ date=\d{4}-\d{2}-\d{2}"$'
        )
        self.assertRegex(first_line, pattern)

    def test_multiline_llm_output_is_quoted_per_line_with_bold_wrap(self):
        args = _args()
        multi = "Line one of the translation.\nLine two with details."
        out = _build_translation_note_block(args, multi, "top", "marker")
        lines = out.splitlines()
        self.assertEqual(lines[0][:5], "[ai-t")
        self.assertEqual(lines[1], "")
        self.assertEqual(lines[2], "> **Line one of the translation.")
        self.assertEqual(lines[3], "> Line two with details.**")


class TestCompose(unittest.TestCase):
    def test_compose_top_marker(self):
        args = _args(note_position="top", note_format="marker")
        content = "# Article\n\nBody text.\n"
        out = _compose_with_notes(content, args, "Translated note.", "marker")
        self.assertTrue(out.startswith("[ai-translation-note-top]: <> "))
        self.assertIn("# Article", out)
        self.assertIn("Body text.", out)

    def test_compose_bottom_marker(self):
        args = _args(note_position="bottom", note_format="marker")
        content = "# Article\n\nBody text.\n"
        out = _compose_with_notes(content, args, "Translated note.", "marker")
        self.assertTrue(out.startswith("# Article"))
        self.assertIn("[ai-translation-note-bottom]: <> ", out)
        self.assertTrue(out.rstrip("\n").endswith("**"))

    def test_compose_both_marker(self):
        args = _args(note_position="both", note_format="marker")
        content = "# Article\n\nBody text.\n"
        out = _compose_with_notes(content, args, "Translated note.", "marker")
        self.assertIn("[ai-translation-note-top]: <> ", out)
        self.assertIn("[ai-translation-note-bottom]: <> ", out)
        # Top placement comes before bottom placement in the output
        self.assertLess(
            out.index("ai-translation-note-top"),
            out.index("ai-translation-note-bottom"),
        )

    def test_compose_top_marker_preserves_frontmatter_first(self):
        args = _args(note_position="top", note_format="marker")
        content = "---\ntitle: Test\nlocale: en\n---\n\n# Article\n\nBody.\n"
        out = _compose_with_notes(content, args, "Translated note.", "marker")
        self.assertTrue(out.startswith("---\n"))
        self.assertIn("\n---\n\n[ai-translation-note-top]", out)
        self.assertIn("Body.", out)

    def test_compose_both_marker_preserves_frontmatter_and_appends_bottom(self):
        args = _args(note_position="both", note_format="marker")
        content = "---\ntitle: Test\n---\n\nBody.\n"
        out = _compose_with_notes(content, args, "Translated note.", "marker")
        self.assertTrue(out.startswith("---\n"))
        self.assertIn("\n---\n\n[ai-translation-note-top]", out)
        self.assertIn("[ai-translation-note-bottom]", out)
        self.assertTrue(out.endswith("**\n"))


class TestSanitizer(unittest.TestCase):
    def test_sanitize_model_simple_alphanum(self):
        self.assertEqual(_sanitize_model("gpt-5-mini"), "gpt-5-mini")

    def test_sanitize_model_with_parentheses(self):
        self.assertEqual(_sanitize_model("gpt-4 (turbo)"), "gpt-4_turbo")

    def test_sanitize_model_keeps_slash_dot_underscore_colon(self):
        self.assertEqual(_sanitize_model("claude/4-haiku.20251001"), "claude/4-haiku.20251001")
        self.assertEqual(_sanitize_model("model:v2"), "model:v2")

    def test_sanitize_model_collapses_unwanted_to_underscore(self):
        self.assertEqual(_sanitize_model("a b c"), "a_b_c")

    def test_sanitize_model_strips_leading_trailing_underscore(self):
        self.assertEqual(_sanitize_model("(gpt)"), "gpt")

    def test_sanitize_model_fallback_unknown(self):
        self.assertEqual(_sanitize_model("!!!"), "unknown")
        self.assertEqual(_sanitize_model(""), "unknown")


class TestSplitFrontmatter(unittest.TestCase):
    def test_no_frontmatter_returns_empty_and_original(self):
        fm, body = _split_frontmatter("Just markdown.\n\nMore text.\n")
        self.assertEqual(fm, "")
        self.assertEqual(body, "Just markdown.\n\nMore text.\n")

    def test_clean_frontmatter_split(self):
        fm, body = _split_frontmatter("---\ntitle: X\nlocale: fr\n---\n\nBody.\n")
        self.assertEqual(fm, "---\ntitle: X\nlocale: fr\n---")
        self.assertEqual(body, "Body.\n")

    def test_malformed_frontmatter_no_close_raises(self):
        with self.assertRaises(RuntimeError) as cm:
            _split_frontmatter("---\ntitle: X\nNo close marker\n")
        self.assertIn("malformed frontmatter", str(cm.exception))


class TestQuoteLines(unittest.TestCase):
    def test_single_line(self):
        self.assertEqual(_quote_lines("hello world"), "> hello world")

    def test_multi_line(self):
        self.assertEqual(_quote_lines("a\nb\nc"), "> a\n> b\n> c")

    def test_preserves_blank_lines_as_quoted(self):
        # Empty lines become bare ">" so mdast sees two distinct paragraphs.
        self.assertEqual(_quote_lines("a\n\nb"), "> a\n>\n> b")
        self.assertEqual(_quote_lines("a\n\n\nb"), "> a\n>\n>\n> b")


class TestSourceBuilder(unittest.TestCase):
    def test_source_emits_three_paragraphs_repo_title_description_link(self):
        args = _args(source_lang="fr", target_lang="ja", model="gpt-5-mini")
        out = _build_translation_note_source(args)
        parts = out.split("\n\n")
        self.assertEqual(len(parts), 3)
        # Structure : titre repo | phrase | lien
        self.assertEqual(parts[0], "**`ai-powered-markdown-translator`**")
        self.assertRegex(
            parts[1],
            r"^Article traduit du \S+ vers le \S+ avec \S+\.$",
        )
        self.assertEqual(
            parts[2],
            "[Voir le projet sur GitHub ↗](https://github.com/jls42/ai-powered-markdown-translator)",
        )

    def test_source_paragraphs_are_blank_line_separated(self):
        """The blank lines between title/description/link enable the CSS grid layout."""
        args = _args(source_lang="fr", target_lang="en", model="gpt-5-mini")
        out = _build_translation_note_source(args)
        # Exactly 2 blank-line separators (3 paragraphs)
        self.assertEqual(out.count("\n\n"), 2)


class TestMarkerBlockThreeParagraphs(unittest.TestCase):
    """Quand le LLM préserve les 3 paragraphes (titre + desc + lien), le builder
    les garde intacts sans wrap supplémentaire (le titre porte déjà ses propres
    `**...**`).
    """

    def test_marker_block_preserves_three_paragraphs_intact(self):
        args = _args()
        translated = (
            "**`ai-powered-markdown-translator`**\n\n"
            "Description traduite.\n\n"
            "[See the project on GitHub ↗](https://example.com)"
        )
        out = _build_translation_note_block(args, translated, "top", "marker")
        self.assertIn("> **`ai-powered-markdown-translator`**", out)
        self.assertIn("> Description traduite.", out)
        self.assertIn("> [See the project on GitHub ↗](https://example.com)", out)
        # Title is NOT double-wrapped in extra **
        self.assertNotIn("**\\*\\*", out)


class TestMarkerSplitsSentenceAndLink(unittest.TestCase):
    """Quand le LLM préserve la ligne vide entre phrase et lien, le builder
    wrap UNIQUEMENT la phrase en gras (le lien reste hors du <strong>).
    """

    def test_marker_block_splits_sentence_and_link(self):
        args = _args()
        # Translated note where LLM preserved the blank line separator
        translated = "Translated.\n\n[See the project](https://example.com)"
        out = _build_translation_note_block(args, translated, "top", "marker")
        self.assertIn("> **Translated.**", out)
        # Link must NOT be inside the bold wrapper
        self.assertNotIn("**[See the project]", out)
        self.assertIn("> [See the project](https://example.com)", out)
        # Blank quoted line between the two
        self.assertRegex(out, r"\*\*Translated\.\*\*\n>\s*\n> \[See the project\]")

    def test_marker_block_fallback_when_no_blank_line(self):
        """If the LLM collapses to a single paragraph, fall back to single-bold."""
        args = _args()
        translated = "Translated note with link inline https://example.com"
        out = _build_translation_note_block(args, translated, "top", "marker")
        self.assertIn(f"> **{translated}**", out)

    def test_marker_block_single_paragraph_with_markdown_link_is_not_bolded(self):
        """Wrapping a Markdown link in `**...**` breaks rendering in some
        renderers — keep the raw form when a link is detected."""
        args = _args()
        translated = "See [the project](https://example.com) for details."
        out = _build_translation_note_block(args, translated, "top", "marker")
        self.assertIn(f"> {translated}", out)
        self.assertNotIn(f"**{translated}**", out)


class TestRetrocompatByteForByte(unittest.TestCase):
    """Le défaut (legacy + bottom) doit reproduire EXACTEMENT le format v1.9."""

    def test_default_no_args_legacy_unchanged_byte_for_byte(self):
        args = _args(note_position="bottom", note_format="legacy")
        out = _compose_with_notes(
            "Contenu traduit final.\n", args, "This document was translated.", "legacy"
        )
        # Forme exacte v1.9 — figée comme golden literal (un refactor de
        # spacing doit échouer, pas re-mimer l'implémentation actuelle).
        self.assertEqual(out, "Contenu traduit final.\n\n**This document was translated.**\n")

    def test_namespace_without_new_attrs_uses_defaults(self):
        """Un Namespace sans note_position / note_format doit retomber sur bottom + legacy."""
        args = Namespace(
            model="gpt-5-mini",
            source_lang="fr",
            target_lang="en",
            news=False,
            reasoning_effort="medium",
        )
        # No note_position, no note_format on args
        content = "Body.\n"
        out = _compose_with_notes(content, args, "Translated.", "legacy")
        self.assertEqual(out, "Body.\n\n**Translated.**\n")


class TestIntegrationWithMarkdownFile(unittest.TestCase):
    """End-to-end via translate_markdown_file avec mock LLM."""

    def _run(self, source_text, mock_responses, args_overrides):
        with tempfile.TemporaryDirectory() as tmpdir:
            src = os.path.join(tmpdir, "input.mdx")
            dst = os.path.join(tmpdir, "input-en.mdx")
            with open(src, "w", encoding="utf-8") as f:
                f.write(source_text)
            mock_client = MagicMock()
            mock_client.chat.completions.create.side_effect = mock_responses
            args = _args(source_dir=tmpdir, target_dir=tmpdir, **args_overrides)
            config = translate._TranslationConfig(
                client=mock_client,
                args=args,
                add_translation_note=True,
                force=False,
            )
            status = translate_markdown_file(src, dst, config)
            output = None
            if os.path.exists(dst):
                with open(dst, encoding="utf-8") as f:
                    output = f.read()
            return status, output

    def test_e2e_marker_top_with_frontmatter(self):
        source = "---\ntitle: Test\n---\n\n# Article\n\nBody.\n"
        translated_body = "---\ntitle: Test\n---\n\n# Article\n\nBody.\n"
        translated_note = "This document was translated from fr to en using gpt-5-mini."
        status, out = self._run(
            source,
            [_make_openai_response(translated_body), _make_openai_response(translated_note)],
            {"note_position": "top", "note_format": "marker"},
        )
        self.assertEqual(status, "success")
        self.assertTrue(out.startswith("---\n"))
        self.assertIn("\n---\n\n[ai-translation-note-top]", out)
        self.assertIn("Body.", out)

    def test_e2e_marker_bottom_no_frontmatter(self):
        source = "# Article\n\nBody.\n"
        status, out = self._run(
            source,
            [_make_openai_response(source), _make_openai_response("Phrase.")],
            {"note_position": "bottom", "note_format": "marker"},
        )
        self.assertEqual(status, "success")
        self.assertTrue(out.startswith("# Article"))
        self.assertIn("[ai-translation-note-bottom]", out)
        self.assertNotIn("[ai-translation-note-top]", out)

    def test_e2e_marker_both_no_frontmatter(self):
        source = "# Article\n\nBody.\n"
        status, out = self._run(
            source,
            [_make_openai_response(source), _make_openai_response("Phrase.")],
            {"note_position": "both", "note_format": "marker"},
        )
        self.assertEqual(status, "success")
        self.assertLess(out.index("[ai-translation-note-top]"), out.index("# Article"))
        self.assertLess(out.index("# Article"), out.index("[ai-translation-note-bottom]"))

    def test_e2e_legacy_top_no_frontmatter(self):
        source = "# Article\n\nBody.\n"
        status, out = self._run(
            source,
            [_make_openai_response(source), _make_openai_response("Translated note.")],
            {"note_position": "top", "note_format": "legacy"},
        )
        self.assertEqual(status, "success")
        # Format legacy : pas de marker definition, juste un paragraphe **bold**
        self.assertNotIn("[ai-translation-note-", out)
        self.assertTrue(out.startswith("**Translated note.**\n\n"))

    def test_e2e_legacy_both_with_frontmatter(self):
        source = "---\ntitle: T\n---\n\nBody.\n"
        status, out = self._run(
            source,
            [_make_openai_response(source), _make_openai_response("TN.")],
            {"note_position": "both", "note_format": "legacy"},
        )
        self.assertEqual(status, "success")
        # Frontmatter d'abord, puis note top, puis body, puis note bottom
        self.assertTrue(out.startswith("---\ntitle: T\n---\n\n**TN.**\n\nBody."))
        self.assertTrue(out.endswith("**TN.**\n"))


class TestComposeUnknownPosition(unittest.TestCase):
    def test_unknown_position_raises_value_error(self):
        args = _args(note_position="middle", note_format="marker")
        with self.assertRaises(ValueError) as cm:
            _compose_with_notes("Body.\n", args, "Translated.", "marker")
        self.assertIn("middle", str(cm.exception))


class TestLLMPayloadExcludesInvariants(unittest.TestCase):
    """Garde-fou du commit 5a29002 : le titre repo et l'URL GitHub ne doivent
    JAMAIS être envoyés au LLM (sinon il peut les mutiler : slug, casse,
    backticks, scheme). Sans ce test, un revert qui re-route titre+URL via
    `translate()` passerait toutes les autres assertions silencieusement.
    """

    INVARIANT_TITLE_FRAGMENT = "ai-powered-markdown-translator"
    INVARIANT_URL_FRAGMENT = "github.com/jls42"

    def _capture_payload(self, args_overrides):
        args = _args(**args_overrides)
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = _make_openai_response("Phrase traduite.")
        result = _append_translation_note(
            "Body.\n", mock_client, args, use_mistral=False, use_claude=False, use_gemini=False
        )
        # Concatène tous les contenus envoyés au LLM (system + user)
        sent = ""
        for call in mock_client.chat.completions.create.call_args_list:
            for msg in call.kwargs["messages"]:
                sent += msg["content"] + "\n"
        return sent, result

    def test_marker_format_does_not_send_title_or_url(self):
        sent, result = self._capture_payload({"note_format": "marker"})
        self.assertNotIn(self.INVARIANT_TITLE_FRAGMENT, sent)
        self.assertNotIn(self.INVARIANT_URL_FRAGMENT, sent)
        # Round-trip : titre + URL DOIVENT apparaître dans la sortie composée
        self.assertIn(f"`{self.INVARIANT_TITLE_FRAGMENT}`", result)
        self.assertIn(self.INVARIANT_URL_FRAGMENT, result)

    def test_legacy_format_does_not_send_title_or_url(self):
        sent, _ = self._capture_payload({"note_format": "legacy"})
        self.assertNotIn(self.INVARIANT_TITLE_FRAGMENT, sent)
        self.assertNotIn(self.INVARIANT_URL_FRAGMENT, sent)


if __name__ == "__main__":
    unittest.main()
