"""Tests de régression pour le bug silent-failure sur traductions longues.

Couvre :
- Validation langue post-traduction (couche source-excerpt + couche langdetect)
- Propagation des erreurs jusqu'au statut "failure" et non-écriture du fichier de sortie
- Whitelist finish_reason / stop_reason
- Segmentation heading-aware (priorité H2/H3)
- Propagation jusqu'à sys.exit(1) côté CLI (single-file et directory)
- detect_provider() bash : auto-fallback OpenAI quand GOOGLE_API_KEY absent/placeholder

Lancement : python -m unittest discover tests/ -v
"""

import os
import subprocess  # nosec B404 — utilisé pour tester le CLI translate.py
import sys
import tempfile
import unittest
from argparse import Namespace
from unittest.mock import MagicMock, patch

# Permet d'importer translate.py depuis le parent
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import translate
from translate import segment_text, translate_markdown_file
from translate import translate as translate_fn

FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "fixtures", "long_fr_excerpt.txt")


def _fake_openai_env():
    """Env avec une clé non-placeholder. _init_openai_client refuse la chaîne
    DEFAULT_OPENAI_API_KEY pour empêcher un run silencieux contre l'API publique.
    """
    return {"OPENAI_API_KEY": "fixture-fake-key-not-placeholder"}  # pragma: allowlist secret


def _make_openai_response(content, finish_reason="stop"):
    """Construit un mock OpenAI response qui exposeresponse.choices[0].message.content
    et response.choices[0].finish_reason."""
    return MagicMock(
        choices=[
            MagicMock(
                message=MagicMock(content=content),
                finish_reason=finish_reason,
            )
        ]
    )


def _base_args(**overrides):
    """Namespace minimal pour translate(). Override pour ajouter des attributs si besoin."""
    defaults = {
        "model": "gpt-5.4-mini",
        "source_lang": "fr",
        "target_lang": "en",
        "news": False,
        "reasoning_effort": "medium",
    }
    defaults.update(overrides)
    return Namespace(**defaults)


def _long_en_translation(min_len=1200):
    """Traduction EN factice assez longue pour ne pas déclencher le ratio guard."""
    sentence = (
        "Artificial intelligence has transformed industrial operations, helping teams "
        "coordinate planning, monitor infrastructure, and improve decisions while "
        "preserving clear human oversight. "
    )
    repeat = (min_len // len(sentence)) + 1
    return sentence * repeat


def _run_markdown_file_translation(
    source_text,
    mock_response,
    *,
    target_lang="en",
    news=False,
    add_translation_note=False,
    ext="md",
):
    """Scaffolding partagé pour invoquer translate_markdown_file dans un tempdir.

    `mock_response` accepte un seul mock OpenAI ou une liste (pour side_effect).
    Retourne (status, output_text_or_None, dst_path).
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        src = os.path.join(tmpdir, f"input.{ext}")
        dst = os.path.join(tmpdir, f"input-{target_lang}.{ext}")
        with open(src, "w", encoding="utf-8") as f:
            f.write(source_text)

        mock_client = MagicMock()
        if isinstance(mock_response, list):
            mock_client.chat.completions.create.side_effect = mock_response
        else:
            mock_client.chat.completions.create.return_value = mock_response

        args = _base_args(
            source_dir=tmpdir,
            target_dir=tmpdir,
            target_lang=target_lang,
            news=news,
        )

        config = translate._TranslationConfig(
            client=mock_client,
            args=args,
            add_translation_note=add_translation_note,
            force=False,
        )
        status = translate_markdown_file(src, dst, config)

        output = None
        if os.path.exists(dst):
            with open(dst, encoding="utf-8") as f:
                output = f.read()
        return status, output, dst


class TestSilentFailure(unittest.TestCase):
    def test_silent_failure_raises_on_french_output(self):
        """Le 2e segment retourné en FR brut (verbatim source) doit lever RuntimeError.

        On utilise segment_text(long_fr_text, 16000)[1] pour reproduire exactement le bug
        observé : le modèle retourne le segment source FR au lieu de la traduction.
        Cela garantit que la couche 1 (source excerpt verbatim) déclenche déterministement.
        """
        with open(FIXTURE_PATH, encoding="utf-8") as f:
            long_fr_text = f.read()
        self.assertGreaterEqual(len(long_fr_text), 20000, "fixture trop courte")
        segments = segment_text(long_fr_text, 16000)
        self.assertGreaterEqual(len(segments), 2, "fixture devrait produire ≥ 2 segments")

        mock_client = MagicMock()
        # 1er segment: traduction EN plausible (>100 chars pour ne pas court-circuiter langdetect)
        # 2e segment: FR brut (retry inclus → 2 fois consécutives FR brut pour épuiser
        # le retry segment-level avant de propager la RuntimeError).
        en_translation = _long_en_translation()
        mock_client.chat.completions.create.side_effect = [
            _make_openai_response(en_translation),
            _make_openai_response(segments[1]),  # FR brut = bug reproduit (1ère tentative)
            _make_openai_response(segments[1]),  # FR brut (retry échoue aussi)
        ]

        args = _base_args()
        with self.assertRaisesRegex(
            RuntimeError, r"untranslated source excerpt|Output language mismatch"
        ):
            translate_fn(long_fr_text, mock_client, args)

    def test_silent_failure_propagates_to_cli_failure(self):
        """translate_markdown_file() doit retourner "failure" et NE PAS écrire le fichier
        quand translate() lève."""
        with open(FIXTURE_PATH, encoding="utf-8") as f:
            long_fr_text = f.read()
        segments = segment_text(long_fr_text, 16000)
        self.assertGreaterEqual(
            len(segments), 2, "fixture devrait produire ≥ 2 segments (sinon test vacuous)"
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            src = os.path.join(tmpdir, "input.md")
            dst = os.path.join(tmpdir, "input-en.md")
            with open(src, "w", encoding="utf-8") as f:
                f.write(long_fr_text)

            mock_client = MagicMock()
            # Fournir une réponse par segment + une 2e réponse FR brut pour le segment
            # fautif (retry segment-level fait 2 appels max sur celui-ci).
            responses = []
            for i, seg in enumerate(segments):
                if i == 1:
                    responses.append(_make_openai_response(seg))  # FR brut (tentative 1)
                    responses.append(_make_openai_response(seg))  # FR brut (retry échoue)
                else:
                    responses.append(_make_openai_response(_long_en_translation()))
            mock_client.chat.completions.create.side_effect = responses

            args = _base_args(source_dir=tmpdir, target_dir=tmpdir)
            config = translate._TranslationConfig(client=mock_client, args=args)
            status = translate_markdown_file(src, dst, config)
            self.assertEqual(status, "failure")
            self.assertFalse(
                os.path.exists(dst),
                "Le fichier de sortie ne doit PAS exister quand la traduction échoue",
            )

    def test_finish_reason_length_raises(self):
        """OpenAI finish_reason='length' (réponse tronquée) doit lever RuntimeError."""
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = _make_openai_response(
            "Some truncated translation",
            finish_reason="length",
        )
        args = _base_args()
        with self.assertRaisesRegex(RuntimeError, r"abnormal finish_reason"):
            translate_fn("Texte source court à traduire.", mock_client, args)

    def test_segment_text_prefers_h3_breakpoint(self):
        """segment_text doit préférer un H3 dans la 2nde moitié comme breakpoint
        plutôt que prendre la dernière fin de phrase. Reproduit la condition du bug
        observé (article 25-apr) où le 2e segment commençait par un H3 isolé."""
        # Construire un texte où un \n###  est placé à ~13k (dans 2nde moitié de 16k)
        prefix = "Texte introductif en français. " * 400  # ~12_400 chars
        # Padding pour atteindre ~13k juste avant le H3
        prefix = prefix + ". " * 50  # ~12_500 chars
        h3_section = "\n### Section avec heading H3\n\nContenu de la section H3 qui suit. " * 200
        text = prefix + h3_section
        self.assertGreater(len(text), 16000, "texte doit dépasser max_length")

        segments = segment_text(text, 16000)
        self.assertGreaterEqual(len(segments), 2)
        # Le 2nd segment doit commencer par "### " (préfixé par éventuels \n)
        self.assertTrue(
            segments[1].lstrip().startswith("### "),
            f"Le 2e segment devrait commencer par '### ', pas par: {segments[1][:80]!r}",
        )

    def test_main_exits_nonzero_on_failure_single_file(self):
        """main() avec --file doit sys.exit(1) quand translate_markdown_file retourne 'failure'."""
        with (
            patch.dict(os.environ, _fake_openai_env()),
            patch("translate.translate_markdown_file", return_value="failure"),
            patch("translate.OpenAI"),
            patch("os.path.isfile", return_value=True),
            patch("os.path.exists", return_value=True),
            patch(
                "sys.argv", ["translate.py", "--file", "/source/fake.md", "--target_dir", "/dest"]
            ),
        ):
            with self.assertRaises(SystemExit) as cm:
                translate.main()
            self.assertEqual(cm.exception.code, 1)

    def test_main_exits_nonzero_on_failure_directory(self):
        """main() avec --source_dir doit sys.exit(1) quand translate_directory rapporte
        au moins un fichier en échec."""
        with (
            patch.dict(os.environ, _fake_openai_env()),
            patch(
                "translate.translate_directory",
                return_value={"failed": ["a.md"], "skipped": []},
            ),
            patch("translate.OpenAI"),
            patch("os.path.isdir", return_value=True),
            patch("os.path.exists", return_value=True),
            patch(
                "sys.argv",
                [
                    "translate.py",
                    "--source_dir",
                    "/source/src",
                    "--target_dir",
                    "/source/dst",
                ],
            ),
        ):
            with self.assertRaises(SystemExit) as cm:
                translate.main()
            self.assertEqual(cm.exception.code, 1)

    def test_openai_reasoning_effort_is_configurable(self):
        """translate() doit transmettre l'effort demandé aux modèles GPT-5.x."""
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = _make_openai_response(
            "Short English translation."
        )
        args = _base_args(reasoning_effort="high")

        translate_fn("Texte source court à traduire.", mock_client, args)

        _, kwargs = mock_client.chat.completions.create.call_args
        self.assertEqual(kwargs["reasoning_effort"], "high")

    def test_generic_markdown_prompt_does_not_assume_blog_frontmatter(self):
        """Le prompt de base doit rester générique pour Markdown/frontmatter, sans
        supposer un schéma de blog title/description/locale obligatoire."""
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = _make_openai_response(
            "Short English translation."
        )
        args = _base_args()

        translate_fn("Document source court à traduire.", mock_client, args)

        messages = mock_client.chat.completions.create.call_args.kwargs["messages"]
        system_prompt = messages[0]["content"]
        self.assertIn("Translate this Markdown document", system_prompt)
        self.assertIn("human-readable prose string values", system_prompt)
        self.assertIn("For Markdown tables", system_prompt)
        self.assertIn("human-readable headers and cell labels", system_prompt)
        self.assertIn("do not add such a field if it is absent", system_prompt)
        self.assertNotIn("translate 'title' and 'description'", system_prompt)
        self.assertNotIn("change 'locale'", system_prompt)

    def test_markdown_contract_applies_to_non_news_translations(self):
        """Le contrat complétude/prose doit aussi couvrir les README non-news."""
        args = _base_args(news=False)
        system_prompt = translate._build_system_instructions(args, is_translation_note=False)

        self.assertIn("<markdown_translation_contract>", system_prompt)
        self.assertIn("Translate ALL prose into the target language", system_prompt)
        self.assertIn("EVERY prose paragraph has been translated", system_prompt)
        self.assertNotIn("<news_final_checks>", system_prompt)

    def test_news_prompt_combines_markdown_contract_and_news_checks(self):
        """Le mode --news garde le contrat markdown général + checks spécifiques news."""
        args = _base_args(news=True, target_lang="pl")
        system_prompt = translate._build_system_instructions(args, is_translation_note=False)

        self.assertIn("<markdown_translation_contract>", system_prompt)
        self.assertIn("Translate ALL prose into the target language", system_prompt)
        self.assertIn("<news_citation_contract", system_prompt)
        self.assertIn("<news_final_checks>", system_prompt)

    def test_news_xml_placeholder_restores_unquoted_quote(self):
        """Le mode --news protège aussi les citations EN sans guillemets et accepte
        la variante XML auto-formatée `<NEWSQUOTE id="0" />`."""
        source_news = """---
title: Test
locale: 'fr'
---

## Google TPU 8e génération

> A decade in the making, the chips for the agentic era have arrived.
>
> 🇫🇷 _Une décennie en gestation, les puces sont arrivées._
> — [@GoogleAI sur X](https://x.com/GoogleAI/status/1)
"""
        translated_news = """---
title: Test
locale: 'pl'
---

## Google TPU ósmej generacji

<NEWSQUOTE id="0" />
>
> 🇵🇱 _Powstające przez dekadę układy już nadeszły._
> — [@GoogleAI na X](#URL0#)
"""

        status, out, _ = _run_markdown_file_translation(
            source_news,
            _make_openai_response(translated_news),
            target_lang="pl",
            news=True,
            ext="mdx",
        )
        self.assertEqual(status, "success")
        self.assertIsNotNone(out)
        self.assertIn("> A decade in the making, the chips for the agentic era have arrived.", out)
        self.assertNotIn("<NEWSQUOTE", out)
        self.assertIn("🇵🇱", out)

    def test_news_xml_placeholder_restores_quote_without_attribution(self):
        """Les anciens articles news peuvent avoir une citation sans ligne `> — ...`."""
        source_news = """---
title: Test
locale: 'fr'
---

## Project Vend

> The gap between 'capable' and 'completely robust' remains wide.
>
> 🇫🇷 _L'écart entre « capable » et « complètement robuste » reste important._
"""
        translated_news = """---
title: Test
locale: 'pl'
---

## Project Vend

<NEWSQUOTE id="0"/>
>
> 🇵🇱 _Różnica między „zdolny” a „w pełni solidny” pozostaje duża._
"""

        status, out, _ = _run_markdown_file_translation(
            source_news,
            _make_openai_response(translated_news),
            target_lang="pl",
            news=True,
            ext="mdx",
        )
        self.assertEqual(status, "success")
        self.assertIsNotNone(out)
        self.assertIn("> The gap between 'capable' and 'completely robust' remains wide.", out)
        self.assertNotIn("<NEWSQUOTE", out)

    def test_news_missing_xml_placeholder_is_failure(self):
        """Un placeholder news supprimé par le modèle doit bloquer l'écriture."""
        source_news = """---
title: Test
locale: 'fr'
---

## Claude for Creative Work

> "Claude now connects to the tools creative professionals already use."
>
> 🇫🇷 _Claude se connecte désormais aux outils des professionnels créatifs._
> — [@claudeai sur X](https://x.com/claudeai/status/1)
"""
        translated_without_placeholder = """---
title: Test
locale: 'pl'
---

## Claude for Creative Work

> 🇵🇱 _Claude łączy się teraz z narzędziami profesjonalistów kreatywnych._
> — [@claudeai na X](https://x.com/claudeai/status/1)
"""

        status, out, dst = _run_markdown_file_translation(
            source_news,
            _make_openai_response(translated_without_placeholder),
            target_lang="pl",
            news=True,
            ext="mdx",
        )
        self.assertEqual(status, "failure")
        self.assertIsNone(out)
        self.assertFalse(os.path.exists(dst))

    def test_translation_note_ends_with_single_newline(self):
        """La note de traduction ne doit pas ajouter de ligne vide finale."""
        status, out, _ = _run_markdown_file_translation(
            "Contenu source.\n",
            [
                _make_openai_response("Translated content.\n"),
                _make_openai_response("This document was translated."),
            ],
            target_lang="en",
            add_translation_note=True,
        )
        self.assertEqual(status, "success")
        self.assertIsNotNone(out)
        self.assertTrue(out.endswith("**This document was translated.**\n"))
        self.assertFalse(out.endswith("\n\n"))


class TestSegmentBreakpointFallbacks(unittest.TestCase):
    """Couvre individuellement les branches de _find_segment_breakpoint :
    H2/H3 (déjà couvert par test_segment_text_prefers_h3_breakpoint),
    paragraphe (\\n\\n), heading bas niveau (\\n#), fin de phrase (. ),
    et hard-cut (max_length).
    """

    def test_breakpoint_paragraph(self):
        """Quand pas de H2/H3 mais un \\n\\n dans la 2nde moitié → coupure au paragraphe."""
        prefix = "Texte introductif. " * 600  # ~12k
        text = prefix + "\n\nNouveau paragraphe. " * 300  # > 16k
        self.assertGreater(len(text), 16000)
        segments = segment_text(text, 16000)
        self.assertGreaterEqual(len(segments), 2)
        # Le 2nd segment doit commencer par "\n" (newline structurant) ou par
        # le premier mot après le \n\n.
        self.assertTrue(
            segments[1].startswith("\n") or segments[1].startswith("Nouveau paragraphe"),
            f"Segment[1] inattendu: {segments[1][:80]!r}",
        )

    def test_breakpoint_low_level_heading(self):
        """Pas de H2/H3 ni de \\n\\n, mais un \\n#### dans la 2nde moitié → coupure heading bas niveau."""
        prefix = "Phrase. " * 1700  # ~13k, sans \n\n
        text = prefix + "\n#### Sous-section H4\nContenu H4. " * 100
        self.assertGreater(len(text), 16000)
        segments = segment_text(text, 16000)
        self.assertGreaterEqual(len(segments), 2)
        # La coupure tombe sur \n# (priorité 3) après le H4.
        self.assertIn("####", segments[1])

    def test_breakpoint_sentence_end(self):
        """Pas de heading ni \\n\\n, juste des phrases → coupure ". "."""
        # Texte d'un seul bloc, phrases séparées par ". " uniquement.
        text = "Une phrase courte. " * 1700  # ~32k, pas de newlines
        self.assertGreater(len(text), 16000)
        segments = segment_text(text, 16000)
        self.assertGreaterEqual(len(segments), 2)
        # Le 1er segment doit finir sur ". " (ou se terminer par le boundary
        # caractère après ". " selon l'index +1).
        self.assertTrue(
            segments[0].endswith(". ") or segments[0].endswith("."),
            f"Segment[0] inattendu (fin): {segments[0][-40:]!r}",
        )

    def test_breakpoint_hard_cut(self):
        """Pas de breakpoint sémantique du tout dans la 2nde moitié → hard-cut à max_length."""
        # 20k caractères contigus sans aucun séparateur exploitable.
        text = "x" * 20000
        segments = segment_text(text, 16000)
        self.assertEqual(len(segments), 2)
        self.assertEqual(len(segments[0]), 16000)
        self.assertEqual(segments[0] + segments[1], text)


class TestCodePlaceholders(unittest.TestCase):
    """Couvre le fenced regex strict (orphan non-greedy, lang hyphené) et la
    validation des placeholders de code (#CODEBLOCKn# / #INLINECODEn#).
    """

    def test_fenced_block_no_lang(self):
        """Fence sans info string ``` → doit être protégée."""
        content = "Texte\n\n```\ncode brut\n```\n\nSuite."
        protected, blocks, ph = translate._protect_code_blocks(content)
        self.assertEqual(len(blocks), 1)
        self.assertIn("#CODEBLOCK0#", protected)
        self.assertNotIn("code brut", protected)

    def test_fenced_block_hyphenated_lang(self):
        """Fence avec lang hyphené ```python-repl → doit être protégée."""
        content = "```python-repl\n>>> 1+1\n```"
        protected, blocks, ph = translate._protect_code_blocks(content)
        self.assertEqual(len(blocks), 1)
        self.assertIn("#CODEBLOCK0#", protected)

    def test_fenced_orphan_does_not_match(self):
        """Une fence ouverte sans fermeture ne doit pas être consommée greedy."""
        content = "Texte\n```\npas de fermeture"
        protected, blocks, _ = translate._protect_code_blocks(content)
        self.assertEqual(blocks, [])
        self.assertEqual(protected, content)

    def test_protect_restore_round_trip_identity(self):
        """protect → restore = identité sur les blocs protégés."""
        content = (
            "Intro.\n\n"
            "```python\nprint('hello')\n```\n\n"
            "Avec `inline_code` au milieu.\n\n"
            "```\nautre bloc\n```\n"
        )
        c1, blocks, b_ph = translate._protect_code_blocks(content)
        c2, inlines, i_ph = translate._protect_inline_code(c1)
        # Simule un LLM qui ne touche pas au texte (round-trip pur).
        restored = translate._restore_code(c2, inlines, i_ph, blocks, b_ph)
        self.assertEqual(restored, content)

    def test_double_backtick_inline_not_swallowed(self):
        """Backticks doubles ``foo`` ne doivent pas être pris pour inline-code single-tick."""
        content = "Voir ``literal`backtick`` dans la doc."
        _, inlines, _ = translate._protect_inline_code(content)
        # Le pattern actuel (?<!`)`...`(?!`) exclut les doubles → 0 match attendu.
        self.assertEqual(inlines, [])

    def test_placeholder_leftover_raises(self):
        """Un #CODEBLOCK0# qui n'a pas été restauré (mismatch d'index) doit lever."""
        text = "Translated text with leftover #CODEBLOCK7# that was never restored."
        with self.assertRaisesRegex(RuntimeError, r"non restauré|leftover|Placeholder"):
            translate._validate_no_code_placeholder_leftover(text)

    def test_placeholder_eaten_by_llm_raises(self):
        """Un placeholder #CODEBLOCK0# émis mais absent de la sortie du LLM doit lever."""
        text = "LLM output that lost the placeholder."
        with self.assertRaisesRegex(RuntimeError, r"manquant|Placeholder"):
            translate._validate_code_placeholders_present(text, ["#CODEBLOCK0#"], [])


class TestHeadingAnchors(unittest.TestCase):
    def test_github_slug_preserves_devanagari_marks(self):
        """Les matras Devanagari doivent survivre dans les slugs heading-derived."""
        self.assertEqual(translate._github_slug("विषय-सूची"), "विषय-सूची")
        self.assertEqual(translate._github_slug("इंस्टॉलेशन"), "इंस्टॉलेशन")
        self.assertEqual(translate._github_slug("TC (तकनीकी समिति)"), "tc-तकनीकी-समिति")

    def test_heading_anchor_restore_uses_devanagari_slug_with_marks(self):
        source_slugs = ["tc-technical-committee"]
        target_slugs = [translate._github_slug("TC (तकनीकी समिति)")]
        out = translate._restore_anchors(
            "[TC (तकनीकी समिति)]#ANCHOR0#",
            ["(#tc-technical-committee)"],
            ["#ANCHOR0#"],
            [{"type": "heading", "slug": "tc-technical-committee"}],
            source_slugs,
            target_slugs,
        )
        self.assertEqual(out, "[TC (तकनीकी समिति)](#tc-तकनीकी-समिति)")


class TestNewsPlaceholderValidator(unittest.TestCase):
    """_validate_news_placeholders_intact doit rejeter les sorties où le LLM a
    localisé / supprimé / renommé le placeholder XML, y compris en scripts non
    latins (CLAUDE.md flagge JA/ZH/AR/HI comme exact risk surface).
    """

    def test_chinese_localized_tag_rejected(self):
        """LLM remplace <NEWSQUOTE id="0"/> par <新闻引用 id="0"/> → doit lever."""
        bad = '<新闻引用 id="0"/>\n>\n> 🇨🇳 _十年磨一剑_\n'
        with self.assertRaisesRegex(RuntimeError, r"Placeholder.*manquant"):
            translate._validate_news_placeholders_intact(bad, n_quotes=1)

    def test_korean_localized_tag_rejected(self):
        bad = '<뉴스인용 id="0"/>\n>\n> 🇰🇷 _10년간의 작업._\n'
        with self.assertRaisesRegex(RuntimeError, r"Placeholder.*manquant"):
            translate._validate_news_placeholders_intact(bad, n_quotes=1)

    def test_japanese_deleted_placeholder_rejected(self):
        """Sortie JA sans aucun tag XML (LLM a remplacé par la quote traduite)."""
        bad = "> 🇯🇵 _十年の月日を経て._\n> — [@GoogleAI X上で](https://x.com/google)\n"
        with self.assertRaisesRegex(RuntimeError, r"Placeholder.*manquant"):
            translate._validate_news_placeholders_intact(bad, n_quotes=1)

    def test_arabic_correct_tag_passes(self):
        """Tag NEWSQUOTE correct dans une sortie AR doit passer."""
        good = '<NEWSQUOTE id="0"/>\n>\n> 🇸🇦 _عقد من العمل._\n'
        translate._validate_news_placeholders_intact(good, n_quotes=1)  # no raise

    def test_hindi_correct_tag_passes(self):
        good = '<NEWSQUOTE id="0"/>\n>\n> 🇮🇳 _एक दशक का काम._\n'
        translate._validate_news_placeholders_intact(good, n_quotes=1)  # no raise


class TestLangDetectLayer2(unittest.TestCase):
    """Couche 2 du validateur : si l'output ne matche aucune fenêtre source verbatim
    (couche 1) mais reste dans la langue source, langdetect doit déclencher.
    """

    def test_paraphrased_french_output_raises(self):
        """Texte paraphrasé en FR (pas de match verbatim avec le segment source)
        et langdetect détecte FR → doit lever 'Output language mismatch'."""
        # Segment source en FR
        source_segment = (
            "L'intelligence artificielle a profondément transformé le paysage industriel "
            "ces dernières années, modifiant la manière dont les entreprises conçoivent "
            "leurs produits et gèrent leurs chaînes d'approvisionnement."
        )
        # Output qui paraphrase en FR (pas de fenêtre source matchable mot-pour-mot,
        # mais clairement français pour langdetect, ≥ 100 chars).
        paraphrased_fr_output = (
            "Les algorithmes d'apprentissage automatique bouleversent le secteur "
            "manufacturier depuis une décennie. Beaucoup d'organisations adaptent "
            "leurs processus internes pour intégrer ces nouvelles capacités prédictives "
            "dans la prise de décision quotidienne et stratégique."
        )
        args = _base_args()
        with self.assertRaisesRegex(RuntimeError, r"Output language mismatch"):
            translate._validate_translation_output(
                source_segment, paraphrased_fr_output, args, is_translation_note=False
            )


class TestGenericBlockquoteValidation(unittest.TestCase):
    """Generic Markdown blockquotes are translatable prose.

    The news pipeline has special protected quote handling, but outside
    `--news`, leaving a long `>` quote verbatim is the same silent-failure
    surface as leaving a paragraph untranslated.
    """

    def test_generic_blockquote_passthrough_raises(self):
        source_segment = (
            "> The reason your React component is re-rendering is likely because "
            "you are creating a new object reference on each render cycle. "
            "When you pass an inline object as a prop, React shallow comparison "
            "sees it as a different object every time, which triggers a re-render."
        )
        args = _base_args(source_lang="en", target_lang="es", news=False)

        with self.assertRaisesRegex(RuntimeError, r"untranslated source excerpt"):
            translate._validate_translation_output(
                source_segment, source_segment, args, is_translation_note=False
            )

    def test_news_blockquotes_can_still_be_ignored(self):
        source_segment = (
            "> A decade in the making, the chips for the agentic era have arrived.\n"
            ">\n"
            "> 🇫🇷 _Une décennie en gestation, les puces sont arrivées._\n"
            "> — [@GoogleAI sur X](https://x.com/GoogleAI/status/1)"
        )

        windows = translate._extract_source_windows(source_segment, ignore_blockquotes=True)

        self.assertEqual(windows, [])


class TestHindiTechnicalReadmeValidation(unittest.TestCase):
    """HI README techniques restent souvent mixtes Hindi + latin technique."""

    def test_hindi_with_technical_latin_terms_bypasses_langdetect_false_positive(self):
        source_segment = (
            "This README explains installation, usage, benchmarks, and plugin behavior "
            "for multiple developer agents in a technical command-line workflow."
        )
        hindi_sentence = (
            "यह README स्थापना, उपयोग, बेंचमार्क और plugin behavior को समझाता है "
            "ताकि developer agents command line workflow में सही तरह से काम करें। "
        )
        translated = (
            '<p align="center">caveman</p>\n\n'
            + (hindi_sentence * 12)
            + " Claude Code Codex Gemini CLI Cursor Windsurf OpenAI GPT MCP plugin "
            + "install.sh README benchmarks evals useMemo React render tokens "
        )
        args = _base_args(source_lang="en", target_lang="hi", news=False)

        with patch("translate.detect_langs", return_value=[MagicMock(lang="en", prob=0.86)]):
            translate._validate_translation_output(
                source_segment, translated, args, is_translation_note=False
            )

    def test_hindi_header_only_still_fails_language_mismatch(self):
        source_segment = (
            "A technical paragraph about installation workflows and command line tools."
        )
        translated = (
            "<strong>स्थापना</strong>\n\n"
            "A rewritten English paragraph about setup workflows, benchmarks, plugins, "
            "agents, command line tools, and installation behavior."
        )
        args = _base_args(source_lang="en", target_lang="hi", news=False)

        with (
            patch(
                "translate.detect_langs",
                return_value=[MagicMock(lang="en", prob=0.95), MagicMock(lang="hi", prob=0.05)],
            ),
            self.assertRaisesRegex(RuntimeError, r"Output language mismatch"),
        ):
            translate._validate_translation_output(
                source_segment, translated, args, is_translation_note=False
            )


class TestMultiProviderStopReasons(unittest.TestCase):
    """Whitelist des finish_reason / stop_reason par provider — un mauvais signal
    abnormal doit lever pour TOUS les providers (anti-régression sur les copy-paste)."""

    def test_claude_abnormal_stop_reason_raises(self):
        client = MagicMock()
        client.messages.create.return_value = MagicMock(
            stop_reason="max_tokens",
            content=[MagicMock(text="truncated")],
        )
        args = _base_args(model="claude-haiku-4-5-20251001")
        with self.assertRaisesRegex(RuntimeError, r"Claude abnormal stop_reason"):
            translate._call_claude(client, args, "prompt", "segment")

    def test_mistral_abnormal_finish_reason_raises(self):
        client = MagicMock()
        client.chat.complete.return_value = MagicMock(
            choices=[MagicMock(finish_reason="length", message=MagicMock(content="x"))]
        )
        args = _base_args(model="mistral-small-latest")
        with self.assertRaisesRegex(RuntimeError, r"Mistral abnormal finish_reason"):
            translate._call_mistral(client, args, "prompt", "segment")

    def test_gemini_abnormal_finish_reason_raises(self):
        gen_model = MagicMock()
        gen_model.generate_content.return_value = MagicMock(
            candidates=[MagicMock(finish_reason="MAX_TOKENS")],
            text="truncated",
        )
        client = MagicMock()
        client.GenerativeModel.return_value = gen_model
        args = _base_args(model="gemini-3-flash-preview")
        with self.assertRaisesRegex(RuntimeError, r"Gemini abnormal finish_reason"):
            translate._call_gemini(client, args, "prompt", "segment")


class TestStructuralLineLanguageBar(unittest.TestCase):
    """Le validateur post-traduction extrait des "fenêtres source" et vérifie
    qu'elles n'apparaissent pas verbatim dans la sortie. Les barres de langues
    markdown (`[français](README.md) | [english](README-en.md) | ...`) ont
    leurs paths conservés à l'identique entre les langues par design — sans
    cette exception, le validateur leverait un faux positif systématique.
    """

    def test_language_bar_with_globe_emoji_is_structural(self):
        """README.md / CHANGELOG.md commencent par une ligne `🌍 [Français](...)`."""
        line = "🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md)"
        self.assertIsNotNone(translate._STRUCTURAL_LINE.match(line))

    def test_language_bar_without_emoji_is_structural(self):
        line = "[français](readme.md) | [english](readme-en.md) | [中文](readme-zh.md)"
        self.assertIsNotNone(translate._STRUCTURAL_LINE.match(line))

    def test_long_real_language_bar_is_structural(self):
        """La barre complète à 14 langues du README/CHANGELOG actuel."""
        line = (
            "🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | "
            "[中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md)"
        )
        self.assertIsNotNone(translate._STRUCTURAL_LINE.match(line))

    def test_blog_prose_with_two_links_is_NOT_structural(self):
        """La phrase `Voici les [docs](a.md) | [tutorial](b.md) à consulter.` du blog
        ne doit pas être prise pour une barre de langues : le `$` final du pattern
        empêche le faux positif quand il y a du texte après le dernier lien.
        """
        line = "Voici les [docs](a.md) | [tutorial](b.md) à consulter."
        self.assertIsNone(translate._STRUCTURAL_LINE.match(line))

    def test_single_link_is_NOT_structural(self):
        line = "Voir la [doc](docs.md) pour plus d'info."
        self.assertIsNone(translate._STRUCTURAL_LINE.match(line))

    def test_comma_separated_links_is_NOT_structural(self):
        """Séparateur autre que `|` → pas une barre de langues."""
        line = "Voir aussi : [a](a.md), [b](b.md)"
        self.assertIsNone(translate._STRUCTURAL_LINE.match(line))


class TestStructuralLineHTML(unittest.TestCase):
    """README HTML-style (cf. EurekAI) : `<p align="center">` et nav-bars HTML
    `<a href="X.md">🇬🇧 English</a> · <a href="Y.md">🇪🇸 Español</a>` ont leurs
    URLs et noms de langues conservés à l'identique source/cible — donc
    matcheraient verbatim dans la sortie sans cette exception structurelle."""

    def test_html_open_tag_alone_is_structural(self):
        for line in ('<p align="center">', "<p>", "<div class='hero'>", "<section>"):
            self.assertIsNotNone(translate._STRUCTURAL_LINE.match(line), line)

    def test_html_close_tag_alone_is_structural(self):
        for line in ("</p>", "</div>", "</section>"):
            self.assertIsNotNone(translate._STRUCTURAL_LINE.match(line), line)

    def test_html_self_closing_tag_alone_is_structural(self):
        for line in ("<br>", "<br/>", "<br />", "<hr>", '<img src="x.png" alt="y" />'):
            self.assertIsNotNone(translate._STRUCTURAL_LINE.match(line), line)

    def test_html_nav_bar_with_flags_is_structural(self):
        """Le bandeau language switcher EurekAI."""
        line = (
            '<a href="README-en.md">🇬🇧 English</a> · '
            '<a href="README-es.md">🇪🇸 Español</a> · '
            '<a href="README-pt.md">🇧🇷 Português</a><br>'
        )
        self.assertIsNotNone(translate._STRUCTURAL_LINE.match(line))

    def test_html_nav_bar_pipe_separator_is_structural(self):
        line = '<a href="a.md">A</a> | <a href="b.md">B</a> | <a href="c.md">C</a>'
        self.assertIsNotNone(translate._STRUCTURAL_LINE.match(line))

    def test_html_paragraph_with_strong_text_is_NOT_structural(self):
        """Une vraie phrase avec balises inline doit rester traduite (pas skip)."""
        line = "<strong>Transforme votre contenu en expérience interactive.</strong>"
        self.assertIsNone(translate._STRUCTURAL_LINE.match(line))


class TestLooksLikeProperNounList(unittest.TestCase):
    """Heuristique pour exclure les fenêtres dominées par des noms propres
    (marques/produits) du passthrough check : ces fenêtres restent identiques
    source/cible légitimement, donc un match n'indique PAS de silent-failure."""

    def test_product_name_list_is_proper_noun_dominated(self):
        # Cas réel rencontré sur le README de caveman (faux positif EN→ES/HI).
        window = (
            "* opencode, Roo, Amp, Goose, Kiro CLI, Augment, Aider Desk, "
            "Continue, Kilo, Junie (JetBrains), Trae"
        )
        self.assertTrue(translate._looks_like_proper_noun_list(window))

    def test_normal_french_prose_is_not_proper_noun_dominated(self):
        window = (
            "Le projet utilise une approche moderne pour la traduction "
            "automatique des documents techniques."
        )
        self.assertFalse(translate._looks_like_proper_noun_list(window))

    def test_normal_english_prose_with_acronyms_is_not_proper_noun_dominated(self):
        window = (
            "The API uses HTTP for communication and JSON for data exchange "
            "between the client and the server."
        )
        self.assertFalse(translate._looks_like_proper_noun_list(window))

    def test_short_window_under_5_words_is_not_filtered(self):
        # Sécurité : ne pas skip à tort des fenêtres trop courtes.
        window = "Mistral AI Service"
        self.assertFalse(translate._looks_like_proper_noun_list(window))

    def test_title_case_long_heading_is_not_filtered_at_70pct(self):
        # Title case 6 mots, mais "for" est lowercase → 5/6 = 83% — skip.
        # Avec des "and"/"the" intercalés, on tombe sous 70%.
        window = "Setup and the configuration of advanced features in production environments"
        self.assertFalse(translate._looks_like_proper_noun_list(window))


class TestExtractSourceWindowsStripsHTML(unittest.TestCase):
    """Le cleaning de fenêtre source doit strip les balises HTML inline
    (mais conserver le texte) pour éviter les faux positifs où des balises
    littérales (<strong>, <span>, etc.) restent identiques source/cible."""

    def test_html_inline_tags_are_stripped_text_kept(self):
        # On force une fenêtre ≥120 chars cleaned pour passer le filtre.
        prose = (
            "<strong>Phrase suffisamment longue pour passer le seuil de 120 "
            "caracteres apres avoir retire les balises HTML inline du texte "
            "source.</strong>"
        )
        windows = translate._extract_source_windows(prose)
        self.assertEqual(len(windows), 1)
        self.assertNotIn("<strong>", windows[0])
        self.assertNotIn("</strong>", windows[0])
        self.assertIn("Phrase suffisamment longue", windows[0])

    def test_html_only_paragraph_yields_no_window_after_strip(self):
        # Un paragraphe composé uniquement de balises HTML + URLs courtes
        # doit produire un cleaned trop court (<120 chars) → 0 fenêtre.
        prose = '<a href="README-en.md">English</a> · <a href="README-es.md">Español</a>'
        windows = translate._extract_source_windows(prose)
        self.assertEqual(windows, [])


REGEN_SCRIPT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "regen_translations.sh")
)


class TestDetectProvider(unittest.TestCase):
    """Teste detect_provider() de regen_translations.sh.

    Comportement : OpenAI gpt-5.4-mini par défaut. Fallback Gemini Flash si
    OPENAI_API_KEY absent/placeholder mais GOOGLE_API_KEY valide. Override
    explicite via REGEN_PROVIDER=openai|gemini.
    """

    def _run_detect(self, env_content=None, exported_env=None):
        """Source regen_translations.sh dans un répertoire temporaire et invoque detect_provider.
        Le sourçage ne lance pas main() grâce au check `BASH_SOURCE != $0`.

        Returns: (stdout, stderr, returncode)
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            if env_content is not None:
                with open(os.path.join(tmpdir, ".env"), "w", encoding="utf-8") as f:
                    f.write(env_content)

            wrapper = f'source "{REGEN_SCRIPT}"; detect_provider'

            env = os.environ.copy()
            # Baseline propre : retirer toutes les clés API du shell parent
            for var in ("OPENAI_API_KEY", "GOOGLE_API_KEY", "GEMINI_API_KEY", "REGEN_PROVIDER"):
                env.pop(var, None)
            if exported_env:
                env.update(exported_env)

            result = subprocess.run(  # nosec B603 B607 — test exécute un wrapper bash construit en local
                ["bash", "-c", wrapper],
                cwd=tmpdir,
                env=env,
                capture_output=True,
                text=True,
            )
            return result.stdout.strip(), result.stderr.strip(), result.returncode

    # Note: aucune des chaînes ci-dessous n'est une vraie clé. detect_provider()
    # ne valide pas le format, seulement non-vide ET != placeholders connus.
    _FAKE_OPENAI_KEY = "fixture-fake-openai-key-do-not-use-aaaaaaaaaaaaaaaa"
    _FAKE_GEMINI_KEY = "fixture-fake-gemini-key-do-not-use-bbbbbbbbbbbbbbbb"

    def test_no_env_file_no_keys_aborts(self):
        """Pas de .env, pas de clés exportées → exit 1 + ERROR sur stderr.

        Fail-closed plutôt qu'émettre `--eco` avec une clé placeholder : sinon
        les jobs en aval tomberaient en 401 silencieux et release.sh validerait
        '28 fichiers présents' contre des traductions stales.
        """
        stdout, stderr, rc = self._run_detect(env_content=None)
        self.assertEqual(rc, 1)
        self.assertEqual(stdout, "")
        self.assertIn("ERROR", stderr)

    def test_openai_key_picks_openai(self):
        """OPENAI_API_KEY valide dans .env → --eco (OpenAI gpt-5.4-mini par défaut)."""
        stdout, stderr, rc = self._run_detect(
            env_content=f"OPENAI_API_KEY={self._FAKE_OPENAI_KEY}\n"
        )
        self.assertEqual(rc, 0)
        self.assertEqual(stdout, "--eco")
        self.assertIn("OpenAI gpt-5.4-mini", stderr)

    def test_both_keys_prefers_openai(self):
        """OPENAI et GOOGLE valides → OpenAI par défaut (priorité OpenAI)."""
        stdout, stderr, rc = self._run_detect(
            env_content=(
                f"OPENAI_API_KEY={self._FAKE_OPENAI_KEY}\n"
                f"GOOGLE_API_KEY={self._FAKE_GEMINI_KEY}\n"
            )
        )
        self.assertEqual(rc, 0)
        self.assertEqual(stdout, "--eco")
        self.assertIn("OpenAI", stderr)

    def test_only_gemini_falls_back_to_gemini(self):
        """OPENAI absent mais GOOGLE valide → fallback Gemini Flash."""
        stdout, stderr, rc = self._run_detect(
            env_content=f"GOOGLE_API_KEY={self._FAKE_GEMINI_KEY}\n"
        )
        self.assertEqual(rc, 0)
        self.assertEqual(stdout, "--use_gemini --eco")
        self.assertIn("fallback Gemini", stderr)

    def test_both_placeholders_aborts(self):
        """Les deux clés en placeholder → exit 1 + ERROR (aucun flag bidon émis)."""
        stdout, stderr, rc = self._run_detect(
            env_content=(
                "OPENAI_API_KEY=votre-cle-api-openai-par-defaut\n"
                "GOOGLE_API_KEY=votre-cle-api-gemini-par-defaut\n"
            )
        )
        self.assertEqual(rc, 1)
        self.assertEqual(stdout, "")
        self.assertIn("ERROR", stderr)

    def test_regen_provider_override_openai(self):
        """REGEN_PROVIDER=openai force OpenAI même si seul Gemini est valide."""
        stdout, stderr, rc = self._run_detect(
            env_content=f"GOOGLE_API_KEY={self._FAKE_GEMINI_KEY}\n",
            exported_env={"REGEN_PROVIDER": "openai"},
        )
        self.assertEqual(rc, 0)
        self.assertEqual(stdout, "--eco")
        self.assertIn("REGEN_PROVIDER=openai", stderr)

    def test_regen_provider_override_gemini(self):
        """REGEN_PROVIDER=gemini force Gemini même si OpenAI est dispo."""
        stdout, stderr, rc = self._run_detect(
            env_content=f"OPENAI_API_KEY={self._FAKE_OPENAI_KEY}\n",
            exported_env={"REGEN_PROVIDER": "gemini"},
        )
        self.assertEqual(rc, 0)
        self.assertEqual(stdout, "--use_gemini --eco")
        self.assertIn("REGEN_PROVIDER=gemini", stderr)


class TestNewsPipelinePerProvider(unittest.TestCase):
    """Exerce translate_markdown_file end-to-end en mode --news pour
    Mistral / Claude / Gemini, afin qu'une régression provider-spécifique
    dans _translate_pipeline ou _validate_news_post soit attrapée.
    """

    SOURCE_NEWS = """---
title: Test
locale: 'fr'
---

## Section

> A decade in the making.
>
> 🇫🇷 _Une décennie en gestation._
> — [@GoogleAI sur X](https://x.com/GoogleAI/status/1)
"""

    # Pipeline protège l'URL d'attribution en `#URL0#` avant l'appel LLM,
    # donc le mock doit retourner avec le placeholder. Le pipeline le restaure
    # ensuite via `_restore_urls`.
    TRANSLATED_NEWS = """---
title: Test
locale: 'pl'
---

## Sekcja

<NEWSQUOTE id="0"/>
>
> 🇵🇱 _Dekada pracy._
> — [@GoogleAI na X](#URL0#)
"""

    def _run_with_provider(self, provider, mock_client_factory):
        with tempfile.TemporaryDirectory() as tmpdir:
            src = os.path.join(tmpdir, "input.md")
            dst = os.path.join(tmpdir, "input-pl.md")
            with open(src, "w", encoding="utf-8") as f:
                f.write(self.SOURCE_NEWS)
            args = _base_args(
                source_dir=tmpdir,
                target_dir=tmpdir,
                target_lang="pl",
                news=True,
                model={
                    "mistral": "mistral-small-latest",
                    "claude": "claude-haiku-4-5-20251001",
                    "gemini": "gemini-3-flash-preview",
                }[provider],
            )
            config = translate._TranslationConfig(
                client=mock_client_factory(),
                args=args,
                use_mistral=(provider == "mistral"),
                use_claude=(provider == "claude"),
                use_gemini=(provider == "gemini"),
                add_translation_note=False,
                force=False,
            )
            status = translate_markdown_file(src, dst, config)
            output = None
            if os.path.exists(dst):
                with open(dst, encoding="utf-8") as f:
                    output = f.read()
            return status, output

    def _mistral_client(self):
        client = MagicMock()
        client.chat.complete.return_value = MagicMock(
            choices=[
                MagicMock(
                    finish_reason="stop",
                    message=MagicMock(content=self.TRANSLATED_NEWS),
                )
            ]
        )
        return client

    def _claude_client(self):
        client = MagicMock()
        client.messages.create.return_value = MagicMock(
            stop_reason="end_turn",
            content=[MagicMock(text=self.TRANSLATED_NEWS)],
        )
        return client

    def _gemini_client(self):
        gen_model = MagicMock()
        gen_model.generate_content.return_value = MagicMock(
            candidates=[MagicMock(finish_reason="STOP")],
            text=self.TRANSLATED_NEWS,
        )
        client = MagicMock()
        client.GenerativeModel.return_value = gen_model
        return client

    def test_news_pipeline_mistral(self):
        status, out = self._run_with_provider("mistral", self._mistral_client)
        self.assertEqual(status, "success")
        self.assertIn("> A decade in the making.", out)
        self.assertNotIn("<NEWSQUOTE", out)
        self.assertIn("🇵🇱", out)

    def test_news_pipeline_claude(self):
        status, out = self._run_with_provider("claude", self._claude_client)
        self.assertEqual(status, "success")
        self.assertIn("> A decade in the making.", out)
        self.assertNotIn("<NEWSQUOTE", out)
        self.assertIn("🇵🇱", out)

    def test_news_pipeline_gemini(self):
        status, out = self._run_with_provider("gemini", self._gemini_client)
        self.assertEqual(status, "success")
        self.assertIn("> A decade in the making.", out)
        self.assertNotIn("<NEWSQUOTE", out)
        self.assertIn("🇵🇱", out)

    def test_news_pipeline_claude_missing_placeholder_fails(self):
        """Path Claude : un placeholder <NEWSQUOTE> manquant doit produire
        status=failure et aucun fichier écrit."""
        bad_translation = """---
title: Test
locale: 'pl'
---

## Sekcja

> 🇵🇱 _Dekada pracy._
> — [@GoogleAI na X](#URL0#)
"""
        client = MagicMock()
        client.messages.create.return_value = MagicMock(
            stop_reason="end_turn",
            content=[MagicMock(text=bad_translation)],
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            src = os.path.join(tmpdir, "input.md")
            dst = os.path.join(tmpdir, "input-pl.md")
            with open(src, "w", encoding="utf-8") as f:
                f.write(self.SOURCE_NEWS)
            args = _base_args(
                source_dir=tmpdir,
                target_dir=tmpdir,
                target_lang="pl",
                news=True,
                model="claude-haiku-4-5-20251001",
            )
            config = translate._TranslationConfig(
                client=client,
                args=args,
                use_mistral=False,
                use_claude=True,
                use_gemini=False,
                add_translation_note=False,
                force=False,
            )
            status = translate_markdown_file(src, dst, config)
            self.assertEqual(status, "failure")
            self.assertFalse(os.path.exists(dst))


class TestRestoreNewsQuotesCount(unittest.TestCase):
    """_restore_news_quotes raise si le placeholder a été restauré 0 ou >1 fois.

    Cas pathologique : le LLM duplique un placeholder XML dans sa sortie (rare
    mais observé sur cibles non-latines). Sans cette garde, la citation EN
    serait dupliquée silencieusement dans le fichier final.
    """

    def test_duplicate_placeholder_raises(self):
        translated = (
            '<NEWSQUOTE id="0"/>\n>\n> 🇵🇱 _trad._\n\n'
            '<NEWSQUOTE id="0"/>\n>\n> Doublon parasite.\n'
        )
        with self.assertRaisesRegex(RuntimeError, r"restauré 2 fois"):
            translate._restore_news_quotes(translated, ["> Quote source EN."])

    def test_zero_placeholder_raises(self):
        translated = "Sortie qui a perdu le placeholder.\n"
        with self.assertRaisesRegex(RuntimeError, r"restauré 0 fois"):
            translate._restore_news_quotes(translated, ["> Quote source EN."])

    def test_exactly_one_placeholder_passes(self):
        translated = '<NEWSQUOTE id="0"/>\n>\n> 🇵🇱 _trad._\n'
        out = translate._restore_news_quotes(translated, ["> Quote source EN."])
        self.assertIn("> Quote source EN.", out)
        self.assertNotIn("<NEWSQUOTE", out)


class TestValidateNewsPost(unittest.TestCase):
    """Couvre les branches post-restoration de _validate_news_post : citation EN
    brute, URL d'attribution, placeholder résiduel (XML et legacy #NEWSQUOTEn#).
    """

    def _args(self, target_lang="pl"):
        return _base_args(news=True, target_lang=target_lang)

    def test_raw_quote_missing_raises(self):
        translated = "Sortie sans la citation source.\n"
        with self.assertRaisesRegex(RuntimeError, r"citation EN brute non restaurée"):
            translate._validate_news_post(
                translated,
                original_quotes=["> A decade in the making."],
                attribution_urls=[],
                args=self._args(),
            )

    def test_attribution_url_missing_raises(self):
        translated = "> A decade in the making.\n> 🇵🇱 _trad_\n"
        with self.assertRaisesRegex(RuntimeError, r"URL d'attribution.*manquante"):
            translate._validate_news_post(
                translated,
                original_quotes=["> A decade in the making."],
                attribution_urls=["https://x.com/google"],
                args=self._args(),
            )

    def test_residual_xml_placeholder_raises(self):
        translated = "> A decade in the making.\n" "> 🇵🇱 _trad_\n" '<NEWSQUOTE id="1"/>\n'
        with self.assertRaisesRegex(RuntimeError, r"placeholder news résiduel"):
            translate._validate_news_post(
                translated,
                original_quotes=["> A decade in the making."],
                attribution_urls=[],
                args=self._args(),
            )

    def test_residual_legacy_placeholder_raises(self):
        translated = "> A decade in the making.\n" "> 🇵🇱 _trad_\n" "#NEWSQUOTE1#\n"
        with self.assertRaisesRegex(RuntimeError, r"placeholder news résiduel"):
            translate._validate_news_post(
                translated,
                original_quotes=["> A decade in the making."],
                attribution_urls=[],
                args=self._args(),
            )


class TestMainExitsOnRealSilentFailure(unittest.TestCase):
    """Test d'intégration : main() doit propager sys.exit(1) quand la chaîne RÉELLE
    de validation détecte un silent-failure dans translate_markdown_file. Les tests
    précédents (test_main_exits_nonzero_on_failure_*) mockent translate_markdown_file
    directement et n'exercent qu'une ligne de main() ; ce test ne mocke QUE le client
    OpenAI, ce qui garantit que toute la chaîne
    _dispatch_provider_call → _validate_translation_output → status=failure → sys.exit
    est réellement exercée.
    """

    def test_main_exits_nonzero_on_real_silent_failure_chain(self):
        with open(FIXTURE_PATH, encoding="utf-8") as f:
            long_fr_text = f.read()
        segments = segment_text(long_fr_text, 16000)
        self.assertGreaterEqual(len(segments), 2, "fixture devrait produire ≥ 2 segments")

        with tempfile.TemporaryDirectory() as tmpdir:
            src_path = os.path.join(tmpdir, "input.md")
            with open(src_path, "w", encoding="utf-8") as f:
                f.write(long_fr_text)

            responses = []
            for i, seg in enumerate(segments):
                if i == 1:
                    # FR brut → couche 1 (source excerpt verbatim) déclenche.
                    # Fournir 2 fois pour épuiser le retry segment-level (tentative 1 + retry).
                    responses.append(_make_openai_response(seg))
                    responses.append(_make_openai_response(seg))
                else:
                    responses.append(_make_openai_response(_long_en_translation()))
            mock_instance = MagicMock()
            mock_instance.chat.completions.create.side_effect = responses

            with (
                patch.dict(os.environ, _fake_openai_env()),
                patch("translate.OpenAI", return_value=mock_instance),
                patch(
                    "sys.argv",
                    ["translate.py", "--file", src_path, "--target_dir", tmpdir],
                ),
            ):
                with self.assertRaises(SystemExit) as cm:
                    translate.main()
                self.assertEqual(cm.exception.code, 1)

            dst = os.path.join(tmpdir, "input-en.md")
            self.assertFalse(
                os.path.exists(dst),
                "Le fichier de sortie ne doit PAS exister quand la chaîne réelle détecte "
                "le silent-failure",
            )


def _long_fr_block(min_len=2400):
    """Bloc FR factice ≥ 500 chars pour traverser le ratio guard et être détecté
    par langdetect comme étant en français."""
    sentence = (
        "L'intelligence artificielle a profondément transformé le paysage industriel "
        "ces dernières années, modifiant la manière dont les entreprises conçoivent "
        "leurs produits et gèrent leurs chaînes d'approvisionnement. "
    )
    repeat = (min_len // len(sentence)) + 1
    return sentence * repeat


class TestPerProviderSilentFailure(unittest.TestCase):
    """Couverture FR-passthrough end-to-end pour chaque provider, pas seulement OpenAI.
    Sans ces tests, une régression dans _dispatch_provider_call (ex: skip de
    _validate_translation_output pour Mistral/Claude/Gemini) ne serait pas détectée.
    """

    def test_silent_failure_raises_for_mistral(self):
        long_fr = _long_fr_block()
        mock_client = MagicMock()
        mock_client.chat.complete.return_value = MagicMock(
            choices=[MagicMock(finish_reason="stop", message=MagicMock(content=long_fr))]
        )
        args = _base_args(model="mistral-small-latest")
        with self.assertRaisesRegex(
            RuntimeError, r"untranslated source excerpt|Output language mismatch"
        ):
            translate_fn(long_fr, mock_client, args, use_mistral=True)

    def test_silent_failure_raises_for_claude(self):
        long_fr = _long_fr_block()
        mock_client = MagicMock()
        mock_client.messages.create.return_value = MagicMock(
            stop_reason="end_turn",
            content=[MagicMock(text=long_fr)],
        )
        args = _base_args(model="claude-haiku-4-5-20251001")
        with self.assertRaisesRegex(
            RuntimeError, r"untranslated source excerpt|Output language mismatch"
        ):
            translate_fn(long_fr, mock_client, args, use_claude=True)

    def test_silent_failure_raises_for_gemini(self):
        long_fr = _long_fr_block()
        gen_model = MagicMock()
        gen_model.generate_content.return_value = MagicMock(
            candidates=[MagicMock(finish_reason="STOP")],
            text=long_fr,
        )
        client = MagicMock()
        client.GenerativeModel.return_value = gen_model
        args = _base_args(model="gemini-3-flash-preview")
        with self.assertRaisesRegex(
            RuntimeError, r"untranslated source excerpt|Output language mismatch"
        ):
            translate_fn(long_fr, client, args, use_gemini=True)


class TestProviderEmptyContent(unittest.TestCase):
    """Empty-content guard du _dispatch_provider_call : un provider qui retourne
    une chaîne vide avec finish_reason='stop' doit lever, pas produire un fichier vide.
    """

    def test_openai_empty_content_raises(self):
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = _make_openai_response(
            "", finish_reason="stop"
        )
        args = _base_args()
        with self.assertRaisesRegex(RuntimeError, r"Openai returned empty content"):
            translate_fn("Some short source text.", mock_client, args)

    def test_mistral_empty_content_raises(self):
        mock_client = MagicMock()
        mock_client.chat.complete.return_value = MagicMock(
            choices=[MagicMock(finish_reason="stop", message=MagicMock(content=""))]
        )
        args = _base_args(model="mistral-small-latest")
        with self.assertRaisesRegex(RuntimeError, r"Mistral returned empty content"):
            translate_fn("Some short source text.", mock_client, args, use_mistral=True)

    def test_claude_empty_content_raises(self):
        mock_client = MagicMock()
        mock_client.messages.create.return_value = MagicMock(
            stop_reason="end_turn",
            content=[MagicMock(text="")],
        )
        args = _base_args(model="claude-haiku-4-5-20251001")
        with self.assertRaisesRegex(RuntimeError, r"Claude returned empty content"):
            translate_fn("Some short source text.", mock_client, args, use_claude=True)

    def test_gemini_empty_content_raises(self):
        gen_model = MagicMock()
        gen_model.generate_content.return_value = MagicMock(
            candidates=[MagicMock(finish_reason="STOP")],
            text="",
        )
        client = MagicMock()
        client.GenerativeModel.return_value = gen_model
        args = _base_args(model="gemini-3-flash-preview")
        with self.assertRaisesRegex(RuntimeError, r"Gemini returned empty content"):
            translate_fn("Some short source text.", client, args, use_gemini=True)


class TestSourceOutputRatio(unittest.TestCase):
    """Sanity ratio source/output : pour une source ≥ 500 chars, une sortie < 5%
    doit lever. Couvre les refus type 'OK' / 'Sorry, I can't do that' qui
    passent les checks finish_reason et langdetect (sortie courte = layer 2 skipped).
    """

    def test_short_refusal_for_long_source_raises(self):
        long_fr = _long_fr_block()  # ~2500 chars
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = _make_openai_response(
            "Sorry, I can't do that.",
            finish_reason="stop",
        )
        args = _base_args()
        with self.assertRaisesRegex(RuntimeError, r"Output suspiciously short for source"):
            translate_fn(long_fr, mock_client, args)

    def test_short_source_short_output_passes(self):
        """Sources < 500 chars : le ratio guard est désactivé (texte court → sortie
        proportionnellement courte est légitime)."""
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = _make_openai_response(
            "OK.", finish_reason="stop"
        )
        args = _base_args()
        # Pas d'exception attendue : la source est trop courte pour activer le guard.
        translate_fn("Texte source court à traduire.", mock_client, args)


class TestNewsCitationExtraction(unittest.TestCase):
    """Couvre _protect_news_quotes() et _NEWS_CITATION_REGEX directement, vs les
    tests end-to-end qui partent de contenu déjà protégé. Garants de non-régression
    sur l'attribution optionnelle et la capture multi-ligne d'un même bloc EN.
    """

    def _args(self):
        return _base_args(news=True)

    def test_extract_with_attribution(self):
        content = (
            "## Section\n\n"
            "> A decade in the making.\n"
            ">\n"
            "> 🇫🇷 _Une décennie en gestation._\n"
            "> — [@GoogleAI](https://x.com/g)\n"
        )
        protected, quotes, urls = translate._protect_news_quotes(content, self._args())
        self.assertIn('<NEWSQUOTE id="0"/>', protected)
        self.assertEqual(quotes, ["> A decade in the making."])
        self.assertEqual(urls, ["https://x.com/g"])

    def test_extract_without_attribution(self):
        content = "## Section\n\n" "> A short EN quote.\n" ">\n" "> 🇫🇷 _Une courte citation EN._\n"
        protected, quotes, urls = translate._protect_news_quotes(content, self._args())
        self.assertIn('<NEWSQUOTE id="0"/>', protected)
        self.assertEqual(quotes, ["> A short EN quote."])
        self.assertEqual(urls, [])

    def test_extract_multiline_en_quote(self):
        """Plusieurs lignes EN consécutives doivent être capturées dans un seul groupe.

        Sinon les lignes précédant la dernière passeraient en clair au LLM et seraient
        traduites, cassant le contrat de protection des citations EN."""
        content = (
            "## Section\n\n"
            "> First line of the EN quote.\n"
            "> Second line of the EN quote.\n"
            "> Third and final line.\n"
            ">\n"
            "> 🇫🇷 _Citation traduite multi-ligne._\n"
            "> — [@source](https://x.com/source)\n"
        )
        protected, quotes, urls = translate._protect_news_quotes(content, self._args())
        self.assertEqual(len(quotes), 1)
        # Les 3 lignes EN doivent être capturées intégralement dans le quote
        self.assertIn("First line of the EN quote.", quotes[0])
        self.assertIn("Second line of the EN quote.", quotes[0])
        self.assertIn("Third and final line.", quotes[0])
        # Et ne doivent PAS rester dans le contenu protégé envoyé au LLM
        self.assertNotIn("First line of the EN quote.", protected)
        self.assertNotIn("Second line of the EN quote.", protected)
        self.assertNotIn("Third and final line.", protected)

    def test_extract_consecutive_citations(self):
        content = (
            "## Sec 1\n\n"
            "> Quote A.\n"
            ">\n"
            "> 🇫🇷 _Citation A._\n"
            "> — [@a](https://x.com/a)\n\n"
            "## Sec 2\n\n"
            "> Quote B.\n"
            ">\n"
            "> 🇫🇷 _Citation B._\n"
            "> — [@b](https://x.com/b)\n"
        )
        protected, quotes, urls = translate._protect_news_quotes(content, self._args())
        self.assertEqual(len(quotes), 2)
        self.assertIn('<NEWSQUOTE id="0"/>', protected)
        self.assertIn('<NEWSQUOTE id="1"/>', protected)
        self.assertEqual(urls, ["https://x.com/a", "https://x.com/b"])

    def test_news_disabled_passthrough(self):
        content = "> Looks like a quote\n>\n> 🇫🇷 _trad_\n"
        args = _base_args(news=False)
        protected, quotes, urls = translate._protect_news_quotes(content, args)
        self.assertEqual(protected, content)
        self.assertEqual(quotes, [])
        self.assertEqual(urls, [])

    def test_extract_attribution_url_with_nested_parens(self):
        """Bug v1.9 (fixé en v1.9.2) : attribution avec markdown link entre
        parenthèses englobantes — typique `(relayé par [@account sur X](url))`.
        L'ancienne regex `\\((.+?)\\)` lazy capturait `relayé par [@account sur X](url`
        (sans `)` final + incluant préfixe FR), ce qui faisait échouer
        `_validate_news_post` car (a) chaîne tronquée, (b) "relayé par"
        traduit en target_lang.
        Le fix extrait UNIQUEMENT l'URL via `\\]\\(([^)]+)\\)` — invariant
        préservé par les placeholders #URL{N}# pendant la traduction.
        """
        content = (
            "## Section\n\n"
            "> A quote in EN.\n"
            ">\n"
            "> 🇫🇷 _Une citation en FR._\n"
            "> — Vasek Mlejnsky, CEO E2B (relayé par [@genspark_ai sur X](https://x.com/genspark_ai/status/2052602512360808652))\n"
        )
        protected, quotes, urls = translate._protect_news_quotes(content, self._args())
        self.assertEqual(quotes, ["> A quote in EN."])
        # Extraction propre : juste l'URL, sans préfixe FR ni `)` tronqué.
        self.assertEqual(urls, ["https://x.com/genspark_ai/status/2052602512360808652"])

    def test_extract_attribution_url_with_french_prefix(self):
        """Variante : préfixe FR (`via`, `selon`, etc.) sans parenthèses englobantes.
        L'extraction doit ignorer le préfixe et ne capturer que l'URL pure.
        """
        content = (
            "## Section\n\n"
            "> Quote.\n"
            ">\n"
            "> 🇫🇷 _Citation._\n"
            "> — via [@source officielle](https://example.com/post/42)\n"
        )
        protected, quotes, urls = translate._protect_news_quotes(content, self._args())
        self.assertEqual(urls, ["https://example.com/post/42"])


def _gemini_blocked_response():
    """Construit une réponse Gemini avec candidates valides mais .text qui raise
    (cas 'safety filter blocked' réel)."""
    response = MagicMock()
    response.candidates = [MagicMock(finish_reason="STOP")]
    type(response).text = property(
        lambda self: (_ for _ in ()).throw(ValueError("blocked by safety filter"))
    )
    return response


class TestGeminiEdgeCases(unittest.TestCase):
    """Couvre les branches non-trivial de _call_gemini : candidates vide,
    response.text qui raise (contenu bloqué par safety filters)."""

    def test_gemini_no_candidates_raises_with_prompt_feedback(self):
        """Réponse Gemini sans candidates = SAFETY/RECITATION/quota côté upstream.
        Le RuntimeError doit citer prompt_feedback pour rendre la cause actionnable
        au lieu d'un message générique 'blocked or empty'."""
        gen_model = MagicMock()
        feedback = MagicMock(block_reason="SAFETY")
        gen_model.generate_content.return_value = MagicMock(
            candidates=[],
            prompt_feedback=feedback,
        )
        client = MagicMock()
        client.GenerativeModel.return_value = gen_model
        args = _base_args(model="gemini-3-flash-preview")
        with self.assertRaisesRegex(RuntimeError, r"no candidates.*prompt_feedback"):
            translate._call_gemini(client, args, "prompt", "segment")

    def test_gemini_blocked_response_raises(self):
        gen_model = MagicMock()
        gen_model.generate_content.return_value = _gemini_blocked_response()
        client = MagicMock()
        client.GenerativeModel.return_value = gen_model
        args = _base_args(model="gemini-3-flash-preview")
        with self.assertRaisesRegex(RuntimeError, r"Gemini response has no text|blocked"):
            translate._call_gemini(client, args, "prompt", "segment")


class TestOpenAINoneContent(unittest.TestCase):
    """Garde explicite : SDK OpenAI peut renvoyer message.content=None quand
    la réponse contient uniquement un refusal ou des tool_calls. Sans la garde,
    .strip() lèverait un AttributeError opaque."""

    def test_openai_none_content_raises_with_refusal(self):
        message = MagicMock(content=None, refusal="I cannot translate this.", tool_calls=None)
        response = MagicMock(choices=[MagicMock(message=message, finish_reason="stop")])
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = response
        args = _base_args()
        with self.assertRaisesRegex(RuntimeError, r"message\.content=None.*refusal"):
            translate._call_openai(mock_client, args, "prompt", "segment", False)


class TestComposeWithNotesBottomTolerantToMalformedFM(unittest.TestCase):
    """Fix: _compose_with_notes ne doit parser le frontmatter que pour les
    layouts qui insèrent au-dessus du body. En mode `bottom`, un fichier avec
    `---` orphelin (sans fence de fermeture) ne doit PAS faire échouer la note."""

    def test_bottom_with_malformed_frontmatter_does_not_raise(self):
        content = "---\ntitle: oops\n# Body without closing fence\n"
        args = _base_args()
        args.note_position = "bottom"
        args.note_format = "legacy"
        out = translate._compose_with_notes(content, args, "Note traduite", "legacy")
        self.assertIn("**Note traduite**", out)
        self.assertTrue(out.endswith("\n"))

    def test_top_with_malformed_frontmatter_still_raises(self):
        content = "---\ntitle: oops\n# Body without closing fence\n"
        args = _base_args()
        args.note_position = "top"
        args.note_format = "legacy"
        with self.assertRaisesRegex(RuntimeError, r"malformed frontmatter"):
            translate._compose_with_notes(content, args, "Note traduite", "legacy")


if __name__ == "__main__":
    unittest.main()
