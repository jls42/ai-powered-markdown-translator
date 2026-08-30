"""Garde-fous ajoutés à la suite de la revue de la PR v1.10.0.

Chaque test verrouille un défaut qui a été **mesuré**, pas supposé, et dont la
particularité commune est de ne produire aucun signal :

- deux flags provider simultanés étaient acceptés en silence et faisaient
  basculer une traduction demandée sur quota d'abonnement vers une facturation
  à l'usage ;
- un `stopReason` absent du payload Grok faisait sauter la vérification du
  contrat de sortie au lieu de la faire échouer ;
- la regex de protection des citations `--news` avait un backtracking
  exponentiel sur du Markdown légal (`>   texte`), mesuré à 2,6 s sur 14 lignes.

Lancement : python -m unittest discover tests/ -v
"""

from __future__ import annotations

import os
import sys
import tempfile
import time
import unittest
from argparse import Namespace
from types import SimpleNamespace
from typing import ClassVar
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import translate


class TestProviderFlagsAreMutuallyExclusive(unittest.TestCase):
    """`--use_codex --use_mistral` était accepté et résolvait vers Mistral.

    L'utilisateur demandait explicitement son quota d'abonnement et obtenait une
    facturation à l'usage, sans avertissement — exactement le mode de
    défaillance que `--use_codex` existe pour empêcher. La précédence divergeait
    en plus entre `_select_provider_client` (Mistral testé en premier) et
    `_resolve_provider` (booléens explicites prioritaires).
    """

    def _parser(self):
        import argparse

        parser = argparse.ArgumentParser()
        translate._add_provider_args(parser)
        return parser

    def test_two_provider_flags_are_refused(self):
        parser = self._parser()
        for pair in (
            ["--use_codex", "--use_mistral"],
            ["--use_codex", "--use_claude"],
            ["--use_grok", "--use_grok_cli"],
            ["--use_gemini", "--use_grok"],
        ):
            with self.subTest(pair=pair), self.assertRaises(SystemExit):
                parser.parse_args(pair)

    def test_single_provider_flag_still_accepted(self):
        parser = self._parser()
        for flag in (
            "--use_mistral",
            "--use_claude",
            "--use_gemini",
            "--use_grok",
            "--use_grok_cli",
            "--use_codex",
        ):
            with self.subTest(flag=flag):
                args = parser.parse_args([flag])
                self.assertTrue(getattr(args, flag.lstrip("-")))

    def test_no_provider_flag_defaults_to_openai(self):
        args = self._parser().parse_args([])
        self.assertEqual(translate._resolve_provider(args), "openai")


class TestGrokStopReasonIsMandatory(unittest.TestCase):
    """Le contrat annoncé exige `stopReason == end_turn`.

    Le code appliquait « `end_turn` OU absent » : un payload sans le champ — ou
    dont le champ aurait été renommé par une mise à jour du CLI — transformait
    la garde en no-op, et une réponse tronquée sur dépassement de tours serait
    partie sur disque.
    """

    def _args(self):
        return Namespace(model="grok-4.6")

    def test_missing_stop_reason_is_refused(self):
        args = self._args()
        with self.assertRaises(translate._GrokCallError) as ctx:
            translate._grok_check_payload({"text": "trad"}, args)
        self.assertIn("stopReason", str(ctx.exception))

    def test_renamed_stop_reason_field_is_refused(self):
        payload = {"type": "result", "text": "trad", "stop_reason": "max_turn_requests"}
        args = self._args()
        with self.assertRaises(translate._GrokCallError):
            translate._grok_check_payload(payload, args)

    def test_null_stop_reason_is_refused(self):
        args = self._args()
        with self.assertRaises(translate._GrokCallError):
            translate._grok_check_payload({"text": "t", "stopReason": None}, args)

    def test_end_turn_still_accepted(self):
        translate._grok_check_payload({"text": "t", "stopReason": "end_turn"}, self._args())

    def test_turn_budget_exhaustion_is_not_a_rate_limit(self):
        """`max_turn_requests` = budget de tours épuisé, pas un rate limit.

        Le classer récupérable faisait attendre 90 s de back-off avant de
        rejouer à l'identique une erreur déterministe (`--max-turns` inchangé).
        """
        args = self._args()
        with self.assertRaises(translate._GrokCallError) as ctx:
            translate._grok_check_payload({"text": "t", "stopReason": "max_turn_requests"}, args)
        self.assertFalse(ctx.exception.rate_limited)

    def test_quota_marker_is_not_treated_as_rate_limit(self):
        """« quota exhausted » est définitif, contrairement à un 429.

        C'est la règle que le docstring de `_codex_is_rate_limited` énonce déjà ;
        elle vaut aussi pour Grok.
        """
        payload = {"type": "error", "message": "quota exhausted, upgrade your plan"}
        args = self._args()
        with self.assertRaises(translate._GrokCallError) as ctx:
            translate._grok_check_payload(payload, args)
        self.assertFalse(ctx.exception.rate_limited)

    def test_real_rate_limit_is_still_retryable(self):
        payload = {"type": "error", "message": "429 Too Many Requests — rate limit reached"}
        args = self._args()
        with self.assertRaises(translate._GrokCallError) as ctx:
            translate._grok_check_payload(payload, args)
        self.assertTrue(ctx.exception.rate_limited)


class TestNewsCitationRegexIsLinear(unittest.TestCase):
    """Le fix multi-paragraphes avait introduit un backtracking exponentiel.

    La répétition contenait `(?:[ \\t]*$|[ \\t]+.*)`, dont le partage des espaces
    entre `[ \\t]+` et `.*` est ambigu ; multipliée d'une itération à l'autre,
    l'ambiguïté explosait. Mesuré sur des lignes `>   texte` — de l'indentation
    Markdown parfaitement légale — qui ne matchent pas le motif : 2,6 s pour 14
    lignes, avec un facteur ~9 par ligne ajoutée. En mode `--news`, un
    blockquote long et non conforme suffisait donc à figer la traduction
    jusqu'au timeout, sans cause identifiable.
    """

    # Généreux d'un facteur ~100 par rapport au temps mesuré (~0,1 ms) : le
    # seuil doit distinguer linéaire d'exponentiel, pas mesurer une machine.
    BUDGET_SECONDS = 1.0

    def _elapsed(self, text):
        start = time.perf_counter()
        translate._NEWS_CITATION_REGEX.search(text)
        return time.perf_counter() - start

    def test_indented_quote_lines_stay_linear(self):
        text = "\n".join([">   ligne indentee"] * 40) + "\nfin"
        self.assertLess(self._elapsed(text), self.BUDGET_SECONDS)

    def test_trailing_whitespace_lines_stay_linear(self):
        text = "\n".join(["> ligne avec espaces  "] * 40) + "\nfin"
        self.assertLess(self._elapsed(text), self.BUDGET_SECONDS)

    def test_long_ordinary_blockquote_stays_linear(self):
        text = "\n".join(["> ligne de citation normale"] * 400) + "\nfin"
        self.assertLess(self._elapsed(text), self.BUDGET_SECONDS)

    def test_multi_paragraph_capture_is_preserved(self):
        """Le correctif de performance ne doit rien changer au comportement."""
        text = (
            "> Premier paragraphe EN.\n"
            ">\n"
            "> Second paragraphe EN.\n"
            ">\n"
            "> 🇫🇷 _La traduction._\n"
            "> — [@source](https://x.com/source/1)"
        )
        match = translate._NEWS_CITATION_REGEX.search(text)
        self.assertIsNotNone(match)
        body = match.group(1)
        self.assertIn("Premier paragraphe EN.", body)
        self.assertIn("Second paragraphe EN.", body)
        self.assertNotIn("— [@source]", body)

    def test_attribution_line_is_never_absorbed_into_body(self):
        text = "> EN quote.\n>\n> 🇫🇷 _Trad._\n> — [@a](https://x.com/a/1)"
        match = translate._NEWS_CITATION_REGEX.search(text)
        self.assertIsNotNone(match)
        self.assertNotIn("—", match.group(1))
        self.assertEqual(match.group(3), "> — [@a](https://x.com/a/1)")


class TestCiRejectionNamesTheRightProvider(unittest.TestCase):
    """Le message de refus en CI était codé en dur pour Codex.

    Un utilisateur de `--use_grok_cli` lisait « L'auth d'abonnement ChatGPT » et
    se voyait orienté vers `OPENAI_API_KEY`, alors que son repli est
    `XAI_API_KEY` / `--use_grok`.
    """

    def test_grok_cli_rejection_points_to_xai(self):
        with (
            patch.dict(os.environ, {"CI": "1"}, clear=False),
            self.assertRaises(ValueError) as ctx,
        ):
            translate._codex_reject_ci_environment(flag="--use_grok_cli")
        message = str(ctx.exception)
        self.assertIn("XAI_API_KEY", message)
        self.assertNotIn("OPENAI_API_KEY", message)

    def test_codex_rejection_still_points_to_openai(self):
        with (
            patch.dict(os.environ, {"CI": "1"}, clear=False),
            self.assertRaises(ValueError) as ctx,
        ):
            translate._codex_reject_ci_environment(flag="--use_codex")
        self.assertIn("OPENAI_API_KEY", str(ctx.exception))


class TestGeminiThinkingLevelIsMemoized(unittest.TestCase):
    """La cascade repartait de `minimal` à chaque segment.

    Le modèle par défaut (`gemini-3.7-flash`) refuse `minimal` : le chemin
    nominal payait donc un aller-retour 400 par segment de chaque fichier, et
    réimprimait le même avertissement. Un warning répété des centaines de fois
    cesse d'être lu — c'est ainsi qu'il devient un masque.
    """

    def setUp(self):
        translate._GEMINI_ACCEPTED_THINKING_LEVEL.clear()

    def tearDown(self):
        translate._GEMINI_ACCEPTED_THINKING_LEVEL.clear()

    def _client_refusing_first(self, calls):
        def generate_content(model, contents, config):
            raw = getattr(getattr(config, "thinking_config", None), "thinking_level", None)
            # Le SDK convertit la chaîne en enum ThinkingLevel : on normalise
            # pour que l'assertion porte sur le niveau, pas sur sa représentation.
            level = str(getattr(raw, "value", raw)).lower() if raw is not None else None
            calls.append(level)
            if level == "minimal":
                raise translate.genai_errors.ClientError(
                    400, {"error": {"message": "Thinking level MINIMAL is not supported"}}
                )
            return SimpleNamespace(
                candidates=[SimpleNamespace(finish_reason="STOP")], text="Translated"
            )

        client = MagicMock()
        client.models.generate_content = generate_content
        return client

    def test_second_segment_skips_the_refused_level(self):
        calls: list = []
        client = self._client_refusing_first(calls)
        args = Namespace(model="gemini-3.7-flash", target_lang="en", source_lang="fr")

        translate._call_gemini(client, args, "P", "SEGMENT 1")
        self.assertEqual(calls, ["minimal", "low"], "le 1er segment descend la cascade")

        translate._call_gemini(client, args, "P", "SEGMENT 2")
        self.assertEqual(
            calls,
            ["minimal", "low", "low"],
            "le 2e segment doit repartir du niveau accepté, sans re-tenter 'minimal'",
        )


# Valeur factice partagée par le jeu de variables du test ci-dessous.
_MARQUEUR = "valeur-de-test-sans-signification"


class TestNoSecretReachesTheAgenticSubprocess(unittest.TestCase):
    """Les deny-lists nominatives ne protégeaient que la facturation.

    Mesuré avant correction : Codex et Grok recevaient chacun **sept** secrets
    dans leur environnement — les clés Anthropic, Mistral, Google, Gemini,
    celle de l'autre CLI, et `OPENAI_BASE_URL`. L'invariant strict tenait
    (Codex sans OPENAI_API_KEY, Grok sans XAI_API_KEY), mais ces deux CLI sont
    des agents, et celui de Grok tourne sans sandbox OS applicable sur beaucoup
    de postes Linux.

    L'assertion est **générique** et non un miroir de la constante : elle
    échouerait sur une clé qu'aucune deny-list ne nomme, ce qui est précisément
    le cas qu'une liste nominative ne peut pas couvrir.
    """

    # Valeur passée par référence et non en littéral : un littéral en face
    # d'une clé nommée *_PASSWORD / *_SECRET fait crier les scanners de
    # secrets, alors qu'il ne s'agit que d'un jeton de test.
    SECRETS: ClassVar[dict[str, str]] = {
        "OPENAI_API_KEY": _MARQUEUR,
        "CODEX_API_KEY": _MARQUEUR,
        "ANTHROPIC_API_KEY": _MARQUEUR,
        "MISTRAL_API_KEY": _MARQUEUR,
        "GOOGLE_API_KEY": _MARQUEUR,
        "GEMINI_API_KEY": _MARQUEUR,
        "XAI_API_KEY": _MARQUEUR,
        "GROK_API_KEY": _MARQUEUR,
        "OPENAI_BASE_URL": "https://example.invalid/v1",
        # Variables qu'aucune deny-list du projet ne nomme : c'est le cœur du
        # test, une liste nominative les laisserait toutes passer.
        "HF_TOKEN": _MARQUEUR,
        "SOME_VENDOR_SECRET": _MARQUEUR,
        "DB_PASSWORD": _MARQUEUR,
        "AWS_CREDENTIALS": _MARQUEUR,
    }

    def _leaked(self, env):
        return sorted(name for name in self.SECRETS if name in env)

    def test_codex_subprocess_receives_no_secret(self):
        with patch.dict(os.environ, self.SECRETS, clear=False):
            env = translate._codex_env(translate._CodexClient(binary="/bin/true"))
        self.assertEqual(self._leaked(env), [])

    def test_grok_subprocess_receives_no_secret(self):
        with patch.dict(os.environ, self.SECRETS, clear=False):
            env = translate._grok_env()
        self.assertEqual(self._leaked(env), [])

    def test_variables_needed_by_the_cli_survive(self):
        """Un filtrage trop large casserait les deux CLI.

        Vérifié aussi par un appel réel : traduction complète aboutie via Codex
        et via Grok CLI avec cet environnement.
        """
        with patch.dict(os.environ, {"PATH": "/usr/bin", "HOME": "/home/u"}, clear=False):
            for env in (
                translate._codex_env(translate._CodexClient(binary="/bin/true")),
                translate._grok_env(),
            ):
                self.assertEqual(env.get("PATH"), "/usr/bin")
                self.assertEqual(env.get("HOME"), "/home/u")


class TestOutputPathCannotEscapeTargetDir(unittest.TestCase):
    """`--target_lang` était interpolé sans contrôle dans le nom de sortie.

    Mesuré avant correction, avec --target_dir out/ :
        --target_lang '../../../../../../tmp/EVASION'
          → nom calculé : doc-../../../../../../tmp/EVASION.md
          → écriture    : /tmp/EVASION.md

    En mode répertoire, `os.makedirs` s'exécute AVANT le premier appel au
    modèle : l'arborescence hors périmètre était donc créée même quand la
    traduction échouait ensuite. Signalé par SonarCloud (pythonsecurity:S8707),
    et confirmé sur le vrai chemin de code — ce n'était pas un faux positif.
    """

    def _args(self, **over):
        base = {
            "target_lang": "en",
            "source_lang": "fr",
            "model": "gpt-5.6-luna",
            "file": "doc.md",
            "target_dir": "/tmp/out",
            "keep_filename": False,
            "include_model": False,
        }
        base.update(over)
        return Namespace(**base)

    def test_path_separator_in_target_lang_is_refused(self):
        args = self._args(target_lang="../../../tmp/evasion")
        with self.assertRaises(ValueError) as ctx:
            translate._reject_path_separators_in_components(args)
        self.assertIn("target_lang", str(ctx.exception))

    def test_path_separator_in_model_is_refused(self):
        args = self._args(model="../../evil")
        with self.assertRaises(ValueError) as ctx:
            translate._reject_path_separators_in_components(args)
        self.assertIn("model", str(ctx.exception))

    def test_bare_dotdot_is_refused(self):
        args = self._args(target_lang="..")
        with self.assertRaises(ValueError):
            translate._reject_path_separators_in_components(args)

    def test_ordinary_values_pass(self):
        translate._reject_path_separators_in_components(self._args())
        translate._reject_path_separators_in_components(self._args(target_lang="zh-Hant"))

    def test_perimeter_guard_accepts_paths_inside(self):
        with tempfile.TemporaryDirectory() as base:
            inside = os.path.join(base, "sub", "doc-en.md")
            self.assertEqual(
                translate._ensure_within_directory(base, inside),
                os.path.realpath(inside),
            )

    def test_perimeter_guard_refuses_escape(self):
        """Seconde couche, indépendante du contrôle des composants.

        Elle attrape tout chemin calculé sortant du périmètre, quelle qu'en
        soit l'origine — un futur composant interpolé, un refactor du calcul.
        """
        with tempfile.TemporaryDirectory() as base:
            outside = os.path.join(base, "..", "EVADE.md")
            with self.assertRaises(ValueError) as ctx:
                translate._ensure_within_directory(base, outside)
        self.assertIn("sort du répertoire cible", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
