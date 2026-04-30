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

import translate  # noqa: E402
from translate import segment_text, translate as translate_fn, translate_markdown_file  # noqa: E402


FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "fixtures", "long_fr_excerpt.txt")


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
    defaults = dict(
        model="gpt-5.4-mini",
        source_lang="fr",
        target_lang="en",
        news=False,
        reasoning_effort="medium",
    )
    defaults.update(overrides)
    return Namespace(**defaults)


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
                    responses.append(_make_openai_response(
                        "Translated content placeholder. " * 20
                    ))
            mock_client.chat.completions.create.side_effect = responses

            args = _base_args(source_dir=tmpdir, target_dir=tmpdir)
            status = translate_markdown_file(
                src, dst, mock_client, args,
                use_mistral=False, use_claude=False, use_gemini=False,
                add_translation_note=False, force=False,
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
        with patch("translate.translate_markdown_file", return_value="failure"), \
             patch("translate.OpenAI"), \
             patch("os.path.isfile", return_value=True), \
             patch("os.path.exists", return_value=True), \
             patch("sys.argv", ["translate.py", "--file", "/tmp/fake.md", "--target_dir", "/tmp"]):
            with self.assertRaises(SystemExit) as cm:
                translate.main()
            self.assertEqual(cm.exception.code, 1)

    def test_main_exits_nonzero_on_failure_directory(self):
        """main() avec --source_dir doit sys.exit(1) quand translate_directory rapporte
        au moins un fichier en échec."""
        with patch(
            "translate.translate_directory",
            return_value={"failed": ["a.md"], "skipped": []},
        ), \
             patch("translate.OpenAI"), \
             patch("os.path.isdir", return_value=True), \
             patch("os.path.exists", return_value=True), \
             patch("sys.argv", [
                 "translate.py", "--source_dir", "/tmp/src", "--target_dir", "/tmp/dst",
             ]):
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

        with tempfile.TemporaryDirectory() as tmpdir:
            src = os.path.join(tmpdir, "input.mdx")
            dst = os.path.join(tmpdir, "input-pl.mdx")
            with open(src, "w", encoding="utf-8") as f:
                f.write(source_news)

            mock_client = MagicMock()
            mock_client.chat.completions.create.return_value = _make_openai_response(
                translated_news
            )
            args = _base_args(
                source_dir=tmpdir,
                target_dir=tmpdir,
                target_lang="pl",
                news=True,
            )

            status = translate_markdown_file(
                src, dst, mock_client, args,
                use_mistral=False, use_claude=False, use_gemini=False,
                add_translation_note=False, force=False,
            )

            self.assertEqual(status, "success")
            with open(dst, encoding="utf-8") as f:
                out = f.read()
            self.assertIn("> A decade in the making, the chips for the agentic era have arrived.", out)
            self.assertNotIn("<NEWSQUOTE", out)
            self.assertIn("🇵🇱", out)

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

        with tempfile.TemporaryDirectory() as tmpdir:
            src = os.path.join(tmpdir, "input.mdx")
            dst = os.path.join(tmpdir, "input-pl.mdx")
            with open(src, "w", encoding="utf-8") as f:
                f.write(source_news)

            mock_client = MagicMock()
            mock_client.chat.completions.create.return_value = _make_openai_response(
                translated_without_placeholder
            )
            args = _base_args(
                source_dir=tmpdir,
                target_dir=tmpdir,
                target_lang="pl",
                news=True,
            )

            status = translate_markdown_file(
                src, dst, mock_client, args,
                use_mistral=False, use_claude=False, use_gemini=False,
                add_translation_note=False, force=False,
            )

            self.assertEqual(status, "failure")
            self.assertFalse(os.path.exists(dst))

REGEN_SCRIPT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "regen_translations.sh")
)


class TestDetectProvider(unittest.TestCase):
    """Teste detect_provider() de regen_translations.sh dans 4 conditions :
    1. .env absent → fallback OpenAI
    2. .env avec placeholder → fallback OpenAI
    3. .env avec vraie clé GOOGLE → Gemini
    4. Variable exportée GOOGLE_API_KEY pré-source → Gemini
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
            env.pop("GOOGLE_API_KEY", None)  # baseline propre
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

    def test_no_env_file_falls_back_to_openai(self):
        """Cas 1 : pas de .env, pas de GOOGLE_API_KEY exportée → --eco (OpenAI)"""
        stdout, stderr, rc = self._run_detect(env_content=None)
        self.assertEqual(rc, 0)
        self.assertEqual(stdout, "--eco")
        self.assertIn("WARNING", stderr)
        self.assertIn("fallback OpenAI", stderr)

    def test_placeholder_in_env_falls_back_to_openai(self):
        """Cas 2 : .env avec placeholder exact → --eco (OpenAI)"""
        stdout, stderr, rc = self._run_detect(
            env_content="GOOGLE_API_KEY=votre-cle-api-gemini-par-defaut\n"
        )
        self.assertEqual(rc, 0)
        self.assertEqual(stdout, "--eco")
        self.assertIn("WARNING", stderr)

    # Note: aucune des chaînes ci-dessous n'est une vraie clé. detect_provider()
    # ne valide pas le format, seulement non-vide ET != placeholders connus. On
    # évite délibérément le préfixe officiel "AIzaSy" pour ne pas déclencher de
    # secret scanner sur la fixture (la fonction n'en a pas besoin).
    _FAKE_KEY_FILE = "fixture-fake-key-not-real-do-not-use-aaaaaaaaaaaaaaaa"
    _FAKE_KEY_EXPORT = "fixture-fake-key-from-exported-env-do-not-use-bbbbbbb"

    def test_real_key_in_env_picks_gemini(self):
        """Cas 3 : .env avec une chaîne non-placeholder → --use_gemini --eco"""
        stdout, stderr, rc = self._run_detect(
            env_content=f"GOOGLE_API_KEY={self._FAKE_KEY_FILE}\n"
        )
        self.assertEqual(rc, 0)
        self.assertEqual(stdout, "--use_gemini --eco")
        self.assertIn("Gemini Flash détecté", stderr)

    def test_exported_env_var_picks_gemini(self):
        """Cas 4 : pas de .env, mais GOOGLE_API_KEY exportée non-placeholder → --use_gemini --eco"""
        stdout, stderr, rc = self._run_detect(
            env_content=None,
            exported_env={"GOOGLE_API_KEY": self._FAKE_KEY_EXPORT},
        )
        self.assertEqual(rc, 0)
        self.assertEqual(stdout, "--use_gemini --eco")
        self.assertIn("Gemini Flash détecté", stderr)


if __name__ == "__main__":
    unittest.main()
