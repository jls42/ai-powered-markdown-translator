"""Couverture supplémentaire de la couche orchestration de translate.py.

Ces tests ciblent volontairement les helpers et branches non exercés par
test_silent_failure.py : provider init, sélection client, validation des
chemins d'entrée, parcours de répertoire, génération de noms de fichiers,
nettoyage news multi-cibles, retours 'skipped'/'failure' et chaîne main().

Lancement : python -m unittest discover tests/ -v
"""

from __future__ import annotations

import os
import sys
import tempfile
import unittest
from argparse import Namespace
from unittest.mock import MagicMock, patch

# Permet d'importer translate.py depuis le parent
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import translate

# Clé bidon non-placeholder pour traverser les gardes _init_*_client.
_FAKE_OPENAI_ENV = {"OPENAI_API_KEY": "fixture-openai-key"}  # pragma: allowlist secret
_FAKE_MISTRAL_ENV = {"MISTRAL_API_KEY": "fixture-mistral-key"}  # pragma: allowlist secret
_FAKE_CLAUDE_ENV = {"ANTHROPIC_API_KEY": "fixture-claude-key"}  # pragma: allowlist secret
_FAKE_GEMINI_ENV = {"GOOGLE_API_KEY": "fixture-gemini-key"}  # pragma: allowlist secret


def _base_args(**overrides):
    defaults = {
        "model": "gpt-5.4-mini",
        "source_lang": "fr",
        "target_lang": "en",
        "news": False,
        "reasoning_effort": "medium",
        "include_model": False,
        "keep_filename": False,
        "eco": False,
        "use_mistral": False,
        "use_claude": False,
        "use_gemini": False,
        "add_translation_note": False,
        "force": False,
        "file": None,
    }
    defaults.update(overrides)
    return Namespace(**defaults)


def _make_openai_response(content, finish_reason="stop"):
    return MagicMock(
        choices=[
            MagicMock(
                message=MagicMock(content=content),
                finish_reason=finish_reason,
            )
        ]
    )


class TestValidateTranslationOutputShortCircuits(unittest.TestCase):
    """Branches early-return de _validate_translation_output."""

    def test_same_source_and_target_lang_skips_validation(self):
        """source_lang == target_lang : pas de validation (passthrough légitime)."""
        segment = "Texte identique source = cible."
        args = _base_args(source_lang="fr", target_lang="fr")
        # Pas d'exception attendue même si translated == segment.
        translate._validate_translation_output(segment, segment, args, False)

    def test_empty_translation_skips_validation(self):
        """Une sortie vide après strip() est traitée plus haut (empty-content
        guard) ; ici on garantit que _validate_translation_output ne lève pas
        sur un blanc."""
        args = _base_args()
        translate._validate_translation_output("Source", "   \n  ", args, False)

    def test_translation_note_skips_validation(self):
        """is_translation_note=True : la note est forcément courte et peut
        ressembler au segment source — on ne valide pas."""
        args = _base_args()
        translate._validate_translation_output("Source", "Source", args, True)

    def test_langdetect_exception_does_not_raise(self):
        """Une LangDetectException sur la sortie doit écrire un warning sur
        stderr mais NE PAS lever (la couche source-excerpt reste seule garante)."""
        args = _base_args()
        # Sortie >= 100 chars pour atteindre la couche langdetect.
        translated = "1234567890" * 12  # 120 chars de chiffres → langdetect lève
        with patch(
            "translate.detect_langs", side_effect=translate.LangDetectException(0, "no features")
        ):
            translate._validate_translation_output("Source longue.", translated, args, False)


class TestResolveOutputFilename(unittest.TestCase):
    """Couvre les 3 branches de _resolve_output_filename."""

    def test_keep_filename(self):
        args = _base_args(keep_filename=True)
        self.assertEqual(
            translate._resolve_output_filename("README.md", "README", args), "README.md"
        )

    def test_include_model(self):
        args = _base_args(include_model=True, model="gpt-5.4-mini", target_lang="es")
        self.assertEqual(
            translate._resolve_output_filename("README.md", "README", args),
            "README-es-gpt-5.4-mini.md",
        )

    def test_default_target_lang_suffix(self):
        args = _base_args(target_lang="de")
        self.assertEqual(
            translate._resolve_output_filename("README.md", "README", args),
            "README-de.md",
        )


class TestResolveSingleOutputFilename(unittest.TestCase):
    def test_keep_filename(self):
        args = _base_args(keep_filename=True, file="/source/foo/article.mdx")
        self.assertEqual(translate._resolve_single_output_filename(args), "article.mdx")

    def test_include_model(self):
        args = _base_args(
            include_model=True,
            file="/source/foo/article.md",
            target_lang="ja",
            model="gpt-5.4-mini",
        )
        self.assertEqual(
            translate._resolve_single_output_filename(args), "article-ja-gpt-5.4-mini.md"
        )

    def test_default(self):
        args = _base_args(file="/source/foo/article.md", target_lang="pt")
        self.assertEqual(translate._resolve_single_output_filename(args), "article-pt.md")


class TestExcludePatterns(unittest.TestCase):
    def test_is_excluded_match(self):
        self.assertTrue(translate.is_excluded("/source/traductions_en/foo.md"))
        self.assertTrue(translate.is_excluded("/source/foo/PRIVACY.md"))
        self.assertTrue(translate.is_excluded("/source/venv/lib/foo.md"))

    def test_is_excluded_no_match(self):
        self.assertFalse(translate.is_excluded("/source/content/posts/foo.md"))

    def test_is_translatable_markdown_md(self):
        self.assertTrue(translate._is_translatable_markdown("article.md"))

    def test_is_translatable_markdown_mdx(self):
        self.assertTrue(translate._is_translatable_markdown("article.mdx"))

    def test_is_translatable_markdown_skips_excluded(self):
        self.assertFalse(translate._is_translatable_markdown("PRIVACY.md"))

    def test_is_translatable_markdown_rejects_other(self):
        self.assertFalse(translate._is_translatable_markdown("README.txt"))


class TestShouldSkipWalkDir(unittest.TestCase):
    def test_skip_excluded_root(self):
        self.assertTrue(
            translate._should_skip_walk_dir(
                "/source/foo/venv/lib", "/source/out", "out", "/source/foo"
            )
        )

    def test_skip_root_inside_output_dir(self):
        self.assertTrue(
            translate._should_skip_walk_dir("/source/out/sub", "/source/out", "out", "/source/in")
        )

    def test_skip_subdir_named_like_output(self):
        """Un sous-répertoire direct d'input qui a le même nom que le dossier
        de sortie doit être skippé pour éviter de lire les traductions."""
        self.assertTrue(
            translate._should_skip_walk_dir(
                "/source/in/out", "/source/elsewhere/out", "out", "/source/in"
            )
        )

    def test_dont_skip_unrelated_dir(self):
        self.assertFalse(
            translate._should_skip_walk_dir("/source/in/posts", "/source/out", "out", "/source/in")
        )


class TestExistingTranslationExists(unittest.TestCase):
    def test_keep_filename_check_path(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            existing = os.path.join(tmpdir, "README.md")
            open(existing, "w").close()
            args = _base_args(keep_filename=True, target_lang="en")
            self.assertTrue(
                translate._existing_translation_exists(existing, tmpdir, "README", args)
            )

    def test_keep_filename_no_match(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            args = _base_args(keep_filename=True, target_lang="en")
            self.assertFalse(
                translate._existing_translation_exists(
                    os.path.join(tmpdir, "missing.md"), tmpdir, "missing", args
                )
            )

    def test_glob_finds_existing_translation(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            existing = os.path.join(tmpdir, "README-en.md")
            open(existing, "w").close()
            args = _base_args(keep_filename=False, target_lang="en")
            self.assertTrue(
                translate._existing_translation_exists(
                    os.path.join(tmpdir, "README-en.md"), tmpdir, "README", args
                )
            )

    def test_glob_no_match(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            args = _base_args(keep_filename=False, target_lang="ja")
            self.assertFalse(
                translate._existing_translation_exists(
                    os.path.join(tmpdir, "README-ja.md"), tmpdir, "README", args
                )
            )


class TestRecordTranslationStatus(unittest.TestCase):
    def test_success_does_not_track(self):
        failed, skipped = [], []
        translate._record_translation_status("success", "f.md", "/abs/f.md", failed, skipped)
        self.assertEqual(failed, [])
        self.assertEqual(skipped, [])

    def test_skipped_appends_to_skipped(self):
        failed, skipped = [], []
        translate._record_translation_status("skipped", "f.md", "/abs/f.md", failed, skipped)
        self.assertEqual(failed, [])
        self.assertEqual(skipped, ["/abs/f.md"])

    def test_failure_appends_to_failed(self):
        failed, skipped = [], []
        translate._record_translation_status("failure", "f.md", "/abs/f.md", failed, skipped)
        self.assertEqual(failed, ["/abs/f.md"])
        self.assertEqual(skipped, [])

    def test_unexpected_status_default_fails(self):
        """Default-fail : tout statut hors {success, skipped, failure} doit être
        traité comme un échec (régression future)."""
        failed, skipped = [], []
        translate._record_translation_status("???", "f.md", "/abs/f.md", failed, skipped)
        self.assertEqual(failed, ["/abs/f.md"])
        self.assertEqual(skipped, [])


class TestWriteOutputFile(unittest.TestCase):
    def test_skipped_when_destination_exists_without_force(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            dst = os.path.join(tmpdir, "existing.md")
            with open(dst, "w") as f:
                f.write("ancien contenu")
            status = translate._write_output_file(
                dst, "nouveau", force=False, relative_output_path="rel/existing.md"
            )
            self.assertEqual(status, "skipped")
            with open(dst) as f:
                self.assertEqual(f.read(), "ancien contenu")

    def test_force_overwrites(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            dst = os.path.join(tmpdir, "existing.md")
            with open(dst, "w") as f:
                f.write("ancien contenu")
            status = translate._write_output_file(
                dst, "nouveau", force=True, relative_output_path="rel/existing.md"
            )
            self.assertEqual(status, "success")
            with open(dst) as f:
                self.assertEqual(f.read(), "nouveau")


class TestEmptyAndIOErrorPaths(unittest.TestCase):
    def test_empty_source_file_returns_skipped(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            src = os.path.join(tmpdir, "empty.md")
            open(src, "w").close()
            args = _base_args(source_dir=tmpdir, target_dir=tmpdir)
            status = translate.translate_markdown_file(
                src,
                os.path.join(tmpdir, "empty-en.md"),
                MagicMock(),
                args,
                False,
                False,
                False,
                False,
                False,
            )
            self.assertEqual(status, "skipped")

    def test_oserror_during_read_returns_failure(self):
        """Un OSError pendant l'ouverture du fichier doit retourner 'failure'
        et imprimer la trace sur stderr."""
        with tempfile.TemporaryDirectory() as tmpdir:
            src = os.path.join(tmpdir, "exists.md")
            with open(src, "w") as f:
                f.write("contenu source")
            args = _base_args(source_dir=tmpdir, target_dir=tmpdir)
            real_open = open

            def selective_open(path, *a, **kw):
                if path == src:
                    raise OSError("disk full")
                return real_open(path, *a, **kw)

            with patch("builtins.open", side_effect=selective_open):
                status = translate.translate_markdown_file(
                    src,
                    os.path.join(tmpdir, "exists-en.md"),
                    MagicMock(),
                    args,
                    False,
                    False,
                    False,
                    False,
                    False,
                )
            self.assertEqual(status, "failure")


class TestProcessOneMarkdownFileSkip(unittest.TestCase):
    """Si une traduction existe déjà sans --force, on n'appelle pas le client."""

    def test_existing_translation_skips_call(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            input_dir = os.path.join(tmpdir, "src")
            output_dir = os.path.join(tmpdir, "dst")
            os.makedirs(input_dir)
            os.makedirs(output_dir)
            src = os.path.join(input_dir, "article.md")
            with open(src, "w") as f:
                f.write("Bonjour.")
            # Préseed la sortie pour exercer la branche skip
            with open(os.path.join(output_dir, "article-en.md"), "w") as f:
                f.write("placeholder")

            args = _base_args(target_lang="en", source_dir=input_dir, target_dir=output_dir)
            failed, skipped = [], []
            mock_client = MagicMock()
            translate._process_one_markdown_file(
                "article.md",
                input_dir,
                input_dir,
                output_dir,
                mock_client,
                args,
                False,
                False,
                False,
                False,
                False,
                failed,
                skipped,
            )
            self.assertEqual(skipped, [src])
            self.assertEqual(failed, [])
            mock_client.chat.completions.create.assert_not_called()

    def test_force_overrides_existing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            input_dir = os.path.join(tmpdir, "src")
            output_dir = os.path.join(tmpdir, "dst")
            os.makedirs(input_dir)
            os.makedirs(output_dir)
            src = os.path.join(input_dir, "article.md")
            with open(src, "w") as f:
                f.write("Bonjour.")
            with open(os.path.join(output_dir, "article-en.md"), "w") as f:
                f.write("ancien")

            args = _base_args(target_lang="en", source_dir=input_dir, target_dir=output_dir)
            failed, skipped = [], []
            mock_client = MagicMock()
            mock_client.chat.completions.create.return_value = _make_openai_response("Hello.")
            translate._process_one_markdown_file(
                "article.md",
                input_dir,
                input_dir,
                output_dir,
                mock_client,
                args,
                False,
                False,
                False,
                False,
                force=True,
                failed_files=failed,
                skipped_files=skipped,
            )
            self.assertEqual(failed, [])
            self.assertEqual(skipped, [])
            with open(os.path.join(output_dir, "article-en.md")) as f:
                self.assertEqual(f.read(), "Hello.")


class TestTranslateDirectory(unittest.TestCase):
    def test_walks_and_translates_md_and_mdx(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            input_dir = os.path.join(tmpdir, "src")
            output_dir = os.path.join(tmpdir, "dst")
            os.makedirs(os.path.join(input_dir, "sub"))
            with open(os.path.join(input_dir, "a.md"), "w") as f:
                f.write("Bonjour A.")
            with open(os.path.join(input_dir, "sub", "b.mdx"), "w") as f:
                f.write("Bonjour B.")
            # Fichier non-markdown : skipped silently
            with open(os.path.join(input_dir, "ignored.txt"), "w") as f:
                f.write("Pas markdown.")

            mock_client = MagicMock()
            mock_client.chat.completions.create.return_value = _make_openai_response("Hello.")
            args = _base_args(target_lang="en", source_dir=input_dir, target_dir=output_dir)
            result = translate.translate_directory(
                input_dir,
                output_dir,
                mock_client,
                args,
                False,
                False,
                False,
                False,
                False,
            )
            self.assertEqual(result["failed"], [])
            self.assertTrue(os.path.exists(os.path.join(output_dir, "a-en.md")))
            # Sans --keep_filename, l'extension de sortie est forcée à .md
            self.assertTrue(os.path.exists(os.path.join(output_dir, "sub", "b-en.md")))

    def test_skips_excluded_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            input_dir = os.path.join(tmpdir, "src")
            output_dir = os.path.join(tmpdir, "dst")
            # Sous-dossier qui matche EXCLUDE_PATTERNS ("traductions_")
            os.makedirs(os.path.join(input_dir, "traductions_old"))
            with open(os.path.join(input_dir, "traductions_old", "skip.md"), "w") as f:
                f.write("ne doit pas être traduit")

            mock_client = MagicMock()
            args = _base_args(target_lang="en", source_dir=input_dir, target_dir=output_dir)
            translate.translate_directory(
                input_dir,
                output_dir,
                mock_client,
                args,
                False,
                False,
                False,
                False,
                False,
            )
            self.assertFalse(
                os.path.exists(os.path.join(output_dir, "traductions_old", "skip-en.md"))
            )
            mock_client.chat.completions.create.assert_not_called()


class TestValidateInputPaths(unittest.TestCase):
    def test_file_does_not_exist_raises(self):
        args = _base_args(file="/source/__inexistant_xyz_42.md", target_dir="/dest")
        with self.assertRaisesRegex(ValueError, "fichier spécifié n'existe pas"):
            translate._validate_input_paths(args)

    def test_source_dir_does_not_exist_raises(self):
        args = _base_args(file=None, source_dir="/source/__inexistant_xyz_42", target_dir="/dest")
        with self.assertRaisesRegex(ValueError, "répertoire source"):
            translate._validate_input_paths(args)

    def test_creates_target_dir_if_missing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            target = os.path.join(tmpdir, "new_target")
            args = _base_args(file=None, source_dir=tmpdir, target_dir=target)
            translate._validate_input_paths(args)
            self.assertTrue(os.path.isdir(target))


class TestProviderClientInit(unittest.TestCase):
    """Couvre _init_*_client : missing key + happy path."""

    def test_init_mistral_missing_key_raises(self):
        args = _base_args()
        with patch.dict(os.environ, {}, clear=True), self.assertRaisesRegex(ValueError, "Mistral"):
            translate._init_mistral_client(args)

    def test_init_mistral_happy_path(self):
        args = _base_args()
        with (
            patch.dict(os.environ, _FAKE_MISTRAL_ENV, clear=True),
            patch("translate.Mistral") as mock_cls,
        ):
            client = translate._init_mistral_client(args)
            mock_cls.assert_called_once_with(api_key=_FAKE_MISTRAL_ENV["MISTRAL_API_KEY"])
            self.assertIs(client, mock_cls.return_value)
        # eco override applique aussi le modèle économique
        args2 = _base_args(eco=True, model=None)
        with patch.dict(os.environ, _FAKE_MISTRAL_ENV, clear=True), patch("translate.Mistral"):
            translate._init_mistral_client(args2)
        self.assertEqual(args2.model, translate.ECO_MODEL_MISTRAL)

    def test_init_claude_missing_key_raises(self):
        args = _base_args()
        with patch.dict(os.environ, {}, clear=True), self.assertRaisesRegex(ValueError, "Claude"):
            translate._init_claude_client(args)

    def test_init_claude_happy_path(self):
        args = _base_args(model=None)
        with (
            patch.dict(os.environ, _FAKE_CLAUDE_ENV, clear=True),
            patch("translate.anthropic") as mock_anthropic,
        ):
            translate._init_claude_client(args)
            mock_anthropic.Anthropic.assert_called_once_with(
                api_key=_FAKE_CLAUDE_ENV["ANTHROPIC_API_KEY"]
            )
        self.assertEqual(args.model, translate.DEFAULT_MODEL_CLAUDE)

    def test_init_gemini_missing_key_raises(self):
        args = _base_args()
        with patch.dict(os.environ, {}, clear=True), self.assertRaisesRegex(ValueError, "Gemini"):
            translate._init_gemini_client(args)

    def test_init_gemini_accepts_GEMINI_API_KEY(self):
        """Le SDK accepte aussi GEMINI_API_KEY (convention AI Studio)."""
        gemini_env = {"GEMINI_API_KEY": "fixture-gemini-studio-key"}  # pragma: allowlist secret
        args = _base_args(model=None, eco=True)
        with (
            patch.dict(os.environ, gemini_env, clear=True),
            patch("translate.genai") as mock_genai,
        ):
            translate._init_gemini_client(args)
            mock_genai.configure.assert_called_once_with(api_key=gemini_env["GEMINI_API_KEY"])
        self.assertEqual(args.model, translate.ECO_MODEL_GEMINI)

    def test_init_openai_missing_key_raises(self):
        args = _base_args()
        with patch.dict(os.environ, {}, clear=True), self.assertRaisesRegex(ValueError, "OpenAI"):
            translate._init_openai_client(args)

    def test_init_openai_placeholder_key_raises(self):
        """Le placeholder de défaut doit être traité comme une clé absente."""
        args = _base_args()
        env = {"OPENAI_API_KEY": translate.DEFAULT_OPENAI_API_KEY}
        with patch.dict(os.environ, env, clear=True), self.assertRaisesRegex(ValueError, "OpenAI"):
            translate._init_openai_client(args)

    def test_init_openai_happy_path(self):
        args = _base_args(model=None)
        with (
            patch.dict(os.environ, _FAKE_OPENAI_ENV, clear=True),
            patch("translate.OpenAI") as mock_cls,
        ):
            translate._init_openai_client(args)
            mock_cls.assert_called_once_with(api_key=_FAKE_OPENAI_ENV["OPENAI_API_KEY"])
        self.assertEqual(args.model, translate.DEFAULT_MODEL_OPENAI)


class TestSelectProviderClient(unittest.TestCase):
    """Couvre les 4 branches de _select_provider_client."""

    def test_mistral_branch(self):
        args = _base_args(use_mistral=True, model=None)
        with (
            patch.dict(os.environ, _FAKE_MISTRAL_ENV, clear=True),
            patch("translate.Mistral") as mock_cls,
        ):
            translate._select_provider_client(args)
            mock_cls.assert_called_once()

    def test_claude_branch(self):
        args = _base_args(use_claude=True, model=None)
        with (
            patch.dict(os.environ, _FAKE_CLAUDE_ENV, clear=True),
            patch("translate.anthropic") as mock_anthropic,
        ):
            translate._select_provider_client(args)
            mock_anthropic.Anthropic.assert_called_once()

    def test_gemini_branch(self):
        args = _base_args(use_gemini=True, model=None)
        with (
            patch.dict(os.environ, _FAKE_GEMINI_ENV, clear=True),
            patch("translate.genai") as mock_genai,
        ):
            translate._select_provider_client(args)
            mock_genai.configure.assert_called_once()

    def test_openai_default_branch(self):
        args = _base_args(model=None)
        with (
            patch.dict(os.environ, _FAKE_OPENAI_ENV, clear=True),
            patch("translate.OpenAI") as mock_cls,
        ):
            translate._select_provider_client(args)
            mock_cls.assert_called_once()


class TestNewsRulesEnglish(unittest.TestCase):
    """Le prompt --news a une variante spécifique pour target_lang=en."""

    def test_news_addendum_en_uses_english_rules(self):
        args = _base_args(news=True, target_lang="en")
        addendum = translate._build_news_addendum(args)
        self.assertIn("placeholder_rule", addendum)
        # La variante EN ne doit pas mentionner de drapeau cible
        self.assertNotIn("Translate to fr", addendum)


class TestNormalizeCollapsedMarkdown(unittest.TestCase):
    def test_separator_collapse_is_split(self):
        out = translate._normalize_collapsed_markdown("--- ## Titre\n")
        self.assertEqual(out, "---\n\n## Titre\n")

    def test_link_collapse_with_heading_is_split(self):
        out = translate._normalize_collapsed_markdown("[texte](https://x.com) ## Titre\n")
        self.assertEqual(out, "[texte](https://x.com)\n\n## Titre\n")

    def test_no_collapse_passes_through(self):
        text = "## Titre\n\nParagraphe normal.\n"
        self.assertEqual(translate._normalize_collapsed_markdown(text), text)


class TestCleanupSourceFlag(unittest.TestCase):
    def test_no_news_passthrough(self):
        args = _base_args(news=False, source_lang="fr", target_lang="en")
        text = "> 🇫🇷 _trad_\n"
        self.assertEqual(translate._cleanup_source_flag(text, args), text)

    def test_target_en_removes_orphan_source_flag_line(self):
        """Quand cible=en, le bloc `> 🇫🇷 _trad_` orphelin doit être supprimé."""
        args = _base_args(news=True, source_lang="fr", target_lang="en")
        translated = (
            "> Some EN quote.\n"
            ">\n"
            "> 🇫🇷 _Citation traduite._\n"
            "> — [@source](https://x.com/s)\n"
        )
        out = translate._cleanup_source_flag(translated, args)
        self.assertNotIn("🇫🇷", out)
        self.assertIn("> Some EN quote.", out)

    def test_target_other_swaps_flag_in_quote_line(self):
        """Quand cible≠en, le drapeau source en début de ligne `> ` doit être
        remplacé par le drapeau cible."""
        args = _base_args(news=True, source_lang="fr", target_lang="es")
        translated = "> 🇫🇷 _Texto traducido._\n"
        out = translate._cleanup_source_flag(translated, args)
        self.assertIn("🇪🇸", out)
        self.assertNotIn("🇫🇷", out)

    def test_no_flag_in_content_passthrough(self):
        args = _base_args(news=True, source_lang="fr", target_lang="es")
        text = "> Aucun drapeau ici.\n"
        self.assertEqual(translate._cleanup_source_flag(text, args), text)


class TestValidateNewsPostFlags(unittest.TestCase):
    def test_en_target_with_other_flag_raises(self):
        with self.assertRaisesRegex(RuntimeError, "Drapeau .* trouvé"):
            translate._validate_news_flags_for_en("contenu avec 🇪🇸 drapeau")

    def test_other_target_wrong_flag_count_raises(self):
        args = _base_args(target_lang="es", source_lang="fr")
        # Aucune occurrence du drapeau cible alors qu'on attendait 1.
        with self.assertRaisesRegex(RuntimeError, "Drapeau .* trouvé 0 fois"):
            translate._validate_news_flags_for_other("contenu sans drapeau", args, 1)

    def test_other_target_residual_source_flag_raises(self):
        args = _base_args(target_lang="es", source_lang="fr")
        # Bon compte de drapeaux cibles, mais drapeau source résiduel.
        with self.assertRaisesRegex(RuntimeError, "Drapeau source .* encore présent"):
            translate._validate_news_flags_for_other("🇪🇸 drapeau cible et 🇫🇷 source", args, 1)

    def test_other_target_correct_state_passes(self):
        args = _base_args(target_lang="es", source_lang="fr")
        translate._validate_news_flags_for_other("Texte avec 🇪🇸 ok", args, 1)


class TestNormalizeCollapsedRaisesOnPersistence(unittest.TestCase):
    """Si la regex de normalisation rate (pattern édge-case), le validateur doit
    lever pour empêcher une sortie cassée."""

    def test_separator_with_tab_still_raises(self):
        # `--- \t##` : le tab n'est pas couvert par la substitution mais l'est
        # par le check final → on attend RuntimeError.
        text = "---\t## Titre\n"
        with self.assertRaisesRegex(RuntimeError, "séparateur markdown collé"):
            translate._normalize_collapsed_markdown(text)

    def test_link_with_tab_still_raises(self):
        text = "[t](https://x.com)\t## Titre\n"
        with self.assertRaisesRegex(RuntimeError, "lien markdown collé"):
            translate._normalize_collapsed_markdown(text)


class TestOpenAIO1Series(unittest.TestCase):
    """Les modèles o1/o1-mini/o1-preview ne supportent pas les system prompts :
    _build_openai_messages doit produire un seul message user concaténé."""

    def test_o1_single_user_message(self):
        args = _base_args(model="o1-mini")
        msgs = translate._build_openai_messages(args, "PROMPT", "SEGMENT")
        self.assertEqual(len(msgs), 1)
        self.assertEqual(msgs[0]["role"], "user")
        self.assertIn("PROMPT", msgs[0]["content"])
        self.assertIn("SEGMENT", msgs[0]["content"])

    def test_non_o1_uses_system_user_split(self):
        args = _base_args(model="gpt-5.4-mini")
        msgs = translate._build_openai_messages(args, "PROMPT", "SEGMENT")
        self.assertEqual(len(msgs), 2)
        self.assertEqual(msgs[0]["role"], "system")
        self.assertEqual(msgs[1]["role"], "user")


class TestOpenAIReasoningEffortFallbacks(unittest.TestCase):
    """Si le SDK local ou le serveur OpenAI rejette reasoning_effort, on retry sans."""

    def test_typeerror_retries_without_reasoning_effort(self):
        client = MagicMock()
        # 1er appel lève TypeError mentionnant reasoning_effort, 2e renvoie OK.
        ok_response = _make_openai_response("Translated")
        client.chat.completions.create.side_effect = [
            TypeError("got unexpected keyword 'reasoning_effort'"),
            ok_response,
        ]
        args = _base_args(model="gpt-5.4-mini")
        out = translate._openai_create_with_fallback(
            client, args, [{"role": "user", "content": "x"}], {"reasoning_effort": "medium"}
        )
        self.assertIs(out, ok_response)
        self.assertEqual(client.chat.completions.create.call_count, 2)

    def test_typeerror_unrelated_reraises(self):
        client = MagicMock()
        client.chat.completions.create.side_effect = TypeError("unrelated")
        args = _base_args(model="gpt-5.4-mini")
        with self.assertRaises(TypeError):
            translate._openai_create_with_fallback(
                client, args, [{"role": "user", "content": "x"}], {"reasoning_effort": "medium"}
            )

    def test_badrequest_retries_without_reasoning_effort(self):
        from openai import BadRequestError

        client = MagicMock()
        ok_response = _make_openai_response("Translated")
        bad_request = BadRequestError(
            message="model does not support reasoning_effort",
            response=MagicMock(status_code=400, request=MagicMock()),
            body=None,
        )
        client.chat.completions.create.side_effect = [bad_request, ok_response]
        args = _base_args(model="gpt-5.4-mini")
        out = translate._openai_create_with_fallback(
            client, args, [{"role": "user", "content": "x"}], {"reasoning_effort": "medium"}
        )
        self.assertIs(out, ok_response)
        self.assertEqual(client.chat.completions.create.call_count, 2)


class TestRunSingleAndDirectory(unittest.TestCase):
    """_run_single_file / _run_directory : couvre les chemins du retour failed_files."""

    def test_run_single_file_failure_listed(self):
        args = _base_args(file="/source/foo.md", target_dir="/dest")
        with patch("translate.translate_markdown_file", return_value="failure"):
            failed = translate._run_single_file(args, MagicMock())
        self.assertEqual(failed, ["/source/foo.md"])

    def test_run_single_file_success_empty(self):
        args = _base_args(file="/source/foo.md", target_dir="/dest")
        with patch("translate.translate_markdown_file", return_value="success"):
            failed = translate._run_single_file(args, MagicMock())
        self.assertEqual(failed, [])

    def test_run_single_file_skipped_empty(self):
        args = _base_args(file="/source/foo.md", target_dir="/dest")
        with patch("translate.translate_markdown_file", return_value="skipped"):
            failed = translate._run_single_file(args, MagicMock())
        self.assertEqual(failed, [])

    def test_run_directory_dict_with_failed(self):
        args = _base_args(source_dir="/source/src", target_dir="/source/dst")
        with patch(
            "translate.translate_directory",
            return_value={"failed": ["a.md"], "skipped": []},
        ):
            self.assertEqual(translate._run_directory(args, MagicMock()), ["a.md"])

    def test_run_directory_default_fail_on_malformed(self):
        """Default-fail : si translate_directory renvoie une dict mal formée
        (sans clé 'failed'), on traite comme un échec."""
        args = _base_args(source_dir="/source/src", target_dir="/source/dst")
        with patch("translate.translate_directory", return_value={"oops": []}):
            failed = translate._run_directory(args, MagicMock())
        self.assertTrue(failed)


class TestMainModelWarning(unittest.TestCase):
    """main() doit afficher un warning si --model n'est pas dans MODEL_TOKEN_LIMITS."""

    def test_unknown_model_prints_warning(self):
        with (
            patch.dict(os.environ, _FAKE_OPENAI_ENV),
            patch("translate.translate_markdown_file", return_value="success"),
            patch("translate.OpenAI"),
            patch("os.path.isfile", return_value=True),
            patch("os.path.exists", return_value=True),
            patch(
                "sys.argv",
                [
                    "translate.py",
                    "--file",
                    "/source/fake.md",
                    "--target_dir",
                    "/dest",
                    "--model",
                    "modele-inconnu-xyz",
                ],
            ),
            patch("builtins.print") as mock_print,
        ):
            translate.main()
        printed = " ".join(str(c) for c in mock_print.call_args_list)
        self.assertIn("modele-inconnu-xyz", printed)


class TestMainCleansUpMistralClient(unittest.TestCase):
    """main() supprime explicitement le client Mistral/Claude pour libérer le httpx
    pool. La branche est strictement défensive (TypeError catché)."""

    def test_mistral_branch_executes_del(self):
        with (
            patch.dict(os.environ, _FAKE_MISTRAL_ENV),
            patch("translate.translate_directory", return_value={"failed": [], "skipped": []}),
            patch("translate.Mistral"),
            patch("os.path.isdir", return_value=True),
            patch("os.path.exists", return_value=True),
            patch(
                "sys.argv",
                [
                    "translate.py",
                    "--use_mistral",
                    "--source_dir",
                    "/source/src",
                    "--target_dir",
                    "/source/dst",
                ],
            ),
        ):
            # Ne doit pas lever : la branche `del client` exécute proprement.
            translate.main()


class TestModuleEntrypoint(unittest.TestCase):
    """Couvre `if __name__ == '__main__': main()` (ligne ~1459) en exécutant
    le script avec une invocation rapide qui sort en erreur (validation paths)."""

    def test_module_entrypoint_invokes_main(self):
        import subprocess  # nosec B404 — test exécute translate.py CLI

        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        env = os.environ.copy()
        env["OPENAI_API_KEY"] = "fixture-openai-key-not-placeholder"  # pragma: allowlist secret
        proc = subprocess.run(  # nosec B603 — test exécute translate.py du repo via sys.executable
            [sys.executable, "translate.py", "--file", "/source/__inexistant_xyz_orchestration"],
            cwd=repo_root,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        # main() doit lever via _validate_input_paths (ValueError) → exit non-zéro.
        self.assertNotEqual(proc.returncode, 0)


if __name__ == "__main__":
    unittest.main()
