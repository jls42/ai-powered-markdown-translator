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
import subprocess
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
    """Env dict avec une clé bidon (non-placeholder) pour traverser la garde du
    fix C1 — _init_openai_client refuse désormais la chaîne DEFAULT_OPENAI_API_KEY.
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

        status = translate_markdown_file(
            src,
            dst,
            mock_client,
            args,
            use_mistral=False,
            use_claude=False,
            use_gemini=False,
            add_translation_note=add_translation_note,
            force=False,
        )

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
        en_translation = (
            "Artificial intelligence has profoundly transformed the industrial landscape "
            "over the past decade, changing how companies design their products, manage "
            "their supply chains, and interact with their customers. This evolution, long "
            "confined to research laboratories, now flows through the most everyday "
            "decision-making processes."
        )
        mock_client.chat.completions.create.side_effect = [
            _make_openai_response(en_translation),
            _make_openai_response(segments[1]),  # FR brut = bug reproduit
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
            # Fournir une réponse par segment (sinon StopIteration masque le test)
            responses = []
            for i, seg in enumerate(segments):
                if i == 1:
                    responses.append(_make_openai_response(seg))  # FR brut
                else:
                    responses.append(_make_openai_response("Translated content placeholder. " * 20))
            mock_client.chat.completions.create.side_effect = responses

            args = _base_args(source_dir=tmpdir, target_dir=tmpdir)
            status = translate_markdown_file(
                src,
                dst,
                mock_client,
                args,
                use_mistral=False,
                use_claude=False,
                use_gemini=False,
                add_translation_note=False,
                force=False,
            )
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
        # Clé bidon pour traverser la garde du fix C1 (_init_openai_client
        # refuse désormais la chaîne placeholder DEFAULT_OPENAI_API_KEY).
        with (
            patch.dict(os.environ, _fake_openai_env()),
            patch("translate.translate_markdown_file", return_value="failure"),
            patch("translate.OpenAI"),
            patch("os.path.isfile", return_value=True),
            patch("os.path.exists", return_value=True),
            patch("sys.argv", ["translate.py", "--file", "/tmp/fake.md", "--target_dir", "/tmp"]),
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
                    "/tmp/src",
                    "--target_dir",
                    "/tmp/dst",
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
> — [@GoogleAI na X](https://x.com/GoogleAI/status/1)
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
    """Couvre la régression du commit a3c35fc (fenced regex hardening) et la
    nouvelle validation des placeholders de code (#CODEBLOCKn# / #INLINECODEn#).
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

            result = subprocess.run(
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

        L'ancien comportement (échouer silencieusement avec --eco + placeholder)
        ré-introduisait précisément la classe de silent-failure que cette branche
        corrige : les jobs en aval tombaient en 401 et release.sh validait
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


if __name__ == "__main__":
    unittest.main()
