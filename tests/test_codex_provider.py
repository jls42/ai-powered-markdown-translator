"""Couverture du provider Codex (CLI officiel, quota d'abonnement ChatGPT).

Ces tests ne lancent jamais le vrai binaire : `subprocess.Popen` / `run` sont
mockés. Ils verrouillent les pièges identifiés en reconnaissance terrain sur le
CLI 0.149.1 — stdin qui doit être fermé, timeout qui doit tuer tout le groupe de
process, sortie vide malgré un code retour 0 — plus la garantie « mode
abonnement » : aucune clé API ne doit fuiter dans l'environnement du
sous-processus, sans quoi la traduction serait facturée à l'usage.

Lancement : python -m unittest discover tests/ -v
"""

from __future__ import annotations

import json
import os
import subprocess  # nosec B404 — la suite simule les CLI, elle n'en lance aucun
import sys
import types
import unittest
from argparse import Namespace
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

# Permet d'importer translate.py depuis le parent
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import translate


def _args(**overrides):
    defaults = {
        "model": "gpt-5.6-sol",
        "source_lang": "fr",
        "target_lang": "en",
        "news": False,
        "reasoning_effort": "medium",
        "eco": False,
    }
    defaults.update(overrides)
    return Namespace(**defaults)


def _client(**overrides):
    defaults = {"binary": "codex", "timeout": 600, "reasoning_effort": "medium"}
    defaults.update(overrides)
    return translate._CodexClient(**defaults)


def _jsonl(*events):
    return "\n".join(json.dumps(e) for e in events) + "\n"


_OK_EVENTS = _jsonl(
    {"type": "thread.started", "thread_id": "01a0"},
    {"type": "turn.started"},
    {"type": "item.completed", "item": {"type": "agent_message", "text": "ignored"}},
    {"type": "turn.completed", "usage": {"input_tokens": 15731}},
)


class _FakePopen:
    """Double de `subprocess.Popen` : écrit le message final là où `-o` le
    demande, en relisant l'argv — ce qui vérifie au passage que le flag est
    bien passé."""

    def __init__(self, final_message="Hello world", returncode=0, stdout=_OK_EVENTS, timeout=False):
        self.final_message = final_message
        self.returncode = returncode
        self._stdout = stdout
        self._timeout = timeout
        self.argv = None
        self.kwargs = None
        self.communicate_kwargs = None
        self.pid = 4242

    def __call__(self, argv, **kwargs):
        self.argv = argv
        self.kwargs = kwargs
        return self

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def communicate(self, **kwargs):
        self.communicate_kwargs = kwargs
        if self._timeout:
            # TimeoutExpired est une classe d'exception levée par un faux
            # Popen, pas un lancement de process.
            # nosemgrep
            raise subprocess.TimeoutExpired(cmd=self.argv, timeout=kwargs.get("timeout"))
        if self.final_message is not None:
            output_file = self.argv[self.argv.index("-o") + 1]
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(self.final_message)
        return self._stdout, "banner on stderr"

    def wait(self, timeout=None):
        return self.returncode


class TestCodexCall(unittest.TestCase):
    def test_nominal_returns_final_message_and_closes_stdin(self):
        """Chemin heureux + régression anti-hang : `codex exec` lit stdin même
        quand le prompt est en argv, donc `input=` doit toujours être fourni
        (sans quoi le CLI attend jusqu'au timeout sans appeler le modèle)."""
        fake = _FakePopen(final_message="Translated body")
        with patch("translate.subprocess.Popen", fake):
            out = translate._call_codex(_client(), _args(), "PROMPT", "SEGMENT")
        self.assertEqual(out, "Translated body")
        self.assertEqual(fake.communicate_kwargs["input"], "SEGMENT")
        self.assertTrue(fake.kwargs["start_new_session"])

    def test_argv_carries_safety_and_model_flags(self):
        fake = _FakePopen()
        with patch("translate.subprocess.Popen", fake):
            translate._call_codex(_client(reasoning_effort="low"), _args(), "PROMPT", "SEG")
        argv = fake.argv
        self.assertEqual(argv[:2], ["codex", "exec"])
        for flag in ("--sandbox", "--skip-git-repo-check", "--ephemeral", "--ignore-user-config"):
            self.assertIn(flag, argv)
        self.assertEqual(argv[argv.index("--sandbox") + 1], "read-only")
        self.assertEqual(argv[argv.index("-m") + 1], "gpt-5.6-sol")
        self.assertIn("model_reasoning_effort=low", argv)

    def test_prompt_carries_agent_contract(self):
        """Sans ce contrat, l'agent peut préfixer sa réponse d'un commentaire."""
        fake = _FakePopen()
        with patch("translate.subprocess.Popen", fake):
            translate._call_codex(_client(), _args(), "PROMPT", "SEG")
        self.assertTrue(fake.argv[2].startswith("PROMPT"))
        self.assertIn("Réponds UNIQUEMENT", fake.argv[2])

    def test_env_strips_api_keys(self):
        """Garantie « mode abonnement » : une clé API laissée dans l'env ferait
        basculer Codex en facturation à l'usage, ce que ce provider existe
        précisément pour éviter."""
        fake = _FakePopen()
        env = {"OPENAI_API_KEY": "sk-should-not-leak", "CODEX_API_KEY": "x", "PATH": "/usr/bin"}
        with patch.dict(os.environ, env, clear=False), patch("translate.subprocess.Popen", fake):
            translate._call_codex(_client(), _args(), "PROMPT", "SEG")
        child_env = fake.kwargs["env"]
        self.assertNotIn("OPENAI_API_KEY", child_env)
        self.assertNotIn("CODEX_API_KEY", child_env)
        self.assertIn("PATH", child_env)

    def test_missing_output_file_raises_instead_of_returning_empty(self):
        """Silent-failure guard : code retour 0 mais aucun message final."""
        fake = _FakePopen(final_message=None)
        client = _client()
        args = _args()
        with patch("translate.subprocess.Popen", fake), self.assertRaises(RuntimeError) as ctx:
            translate._call_codex(client, args, "PROMPT", "SEG")
        self.assertIn("sans écrire de message final", str(ctx.exception))

    def test_turn_failed_raises_even_with_returncode_zero(self):
        payload = json.dumps(
            {
                "type": "error",
                "status": 400,
                "error": {
                    "type": "invalid_request_error",
                    "message": "The 'gpt-5.4-mini' model is not supported when using Codex "
                    "with a ChatGPT account.",
                },
            }
        )
        stdout = _jsonl(
            {"type": "thread.started", "thread_id": "01a0"},
            {"type": "turn.failed", "error": {"message": payload}},
        )
        fake = _FakePopen(returncode=0, stdout=stdout)
        client = _client()
        args = _args()
        with patch("translate.subprocess.Popen", fake), self.assertRaises(RuntimeError) as ctx:
            translate._call_codex(client, args, "PROMPT", "SEG")
        self.assertIn("not supported when using Codex", str(ctx.exception))

    def test_nonzero_returncode_raises_with_stderr_tail(self):
        fake = _FakePopen(returncode=1, stdout="")
        client = _client()
        args = _args()
        with patch("translate.subprocess.Popen", fake), self.assertRaises(RuntimeError) as ctx:
            translate._call_codex(client, args, "PROMPT", "SEG")
        self.assertIn("code 1", str(ctx.exception))

    def test_timeout_kills_process_group(self):
        """Le `codex` de npm est un shim Node : le vrai binaire est un
        petit-fils qui survivrait à un kill du fils direct et continuerait à
        consommer du quota."""
        fake = _FakePopen(timeout=True)
        client = _client(timeout=42)
        args = _args()
        with (
            patch("translate.subprocess.Popen", fake),
            patch("translate.os.getpgid", return_value=4242),
            patch("translate.os.killpg") as killpg,
            self.assertRaises(RuntimeError) as ctx,
        ):
            translate._call_codex(client, args, "PROMPT", "SEG")
        self.assertIn("timeout après 42s", str(ctx.exception))
        killpg.assert_called_once()
        self.assertEqual(killpg.call_args[0][0], 4242)


class TestCodexRateLimitBackoff(unittest.TestCase):
    def test_rate_limit_is_retried_then_succeeds(self):
        payload = json.dumps({"type": "error", "status": 429, "error": {"message": "slow down"}})
        fail = _jsonl({"type": "turn.failed", "error": {"message": payload}})
        attempts = []

        def popen_factory(argv, **kwargs):
            attempts.append(argv)
            first = len(attempts) == 1
            fake = _FakePopen(stdout=fail if first else _OK_EVENTS, final_message="Done")
            return fake(argv, **kwargs)

        with (
            patch("translate.subprocess.Popen", popen_factory),
            patch("translate.time.sleep") as sleep,
        ):
            out = translate._call_codex(_client(), _args(), "PROMPT", "SEG")
        self.assertEqual(out, "Done")
        self.assertEqual(len(attempts), 2)
        sleep.assert_called_once()

    def test_non_rate_limit_error_is_not_retried(self):
        payload = json.dumps({"type": "error", "status": 400, "error": {"message": "bad model"}})
        stdout = _jsonl({"type": "turn.failed", "error": {"message": payload}})
        calls = []

        def popen_factory(argv, **kwargs):
            calls.append(argv)
            return _FakePopen(stdout=stdout)(argv, **kwargs)

        client = _client()
        args = _args()
        with (
            patch("translate.subprocess.Popen", popen_factory),
            self.assertRaises(RuntimeError),
        ):
            translate._call_codex(client, args, "PROMPT", "SEG")
        self.assertEqual(len(calls), 1)


class TestCodexInit(unittest.TestCase):
    def test_defaults_and_eco_models(self):
        with (
            patch("translate._codex_preflight"),
            patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}, clear=False),
        ):
            args = _args(model=None)
            translate._init_codex_client(args)
            self.assertEqual(args.model, translate.DEFAULT_MODEL_CODEX)

            eco = _args(model=None, eco=True)
            translate._init_codex_client(eco)
            self.assertEqual(eco.model, translate.ECO_MODEL_CODEX)

    def test_refuses_ci_environment(self):
        args = _args(model=None)
        with (
            patch.dict(os.environ, {"GITHUB_ACTIONS": "true"}, clear=False),
            self.assertRaises(ValueError) as ctx,
        ):
            translate._init_codex_client(args)
        self.assertIn("CI", str(ctx.exception))

    def test_preflight_rejects_missing_binary(self):
        """La détection du binaire vit dans `_resolve_codex_binary`, qui rend
        `None` quand aucune des trois sources n'aboutit ; le preflight n'a plus
        qu'à refuser cette valeur."""
        with self.assertRaises(ValueError) as ctx:
            translate._codex_preflight(None)
        self.assertIn("introuvable", str(ctx.exception))

    def test_preflight_reports_unexecutable_binary(self):
        with (
            patch("translate.subprocess.run", side_effect=OSError("Permission denied")),
            self.assertRaises(ValueError) as ctx,
        ):
            translate._codex_preflight("/pkg/bin/codex")
        self.assertIn("Permission denied", str(ctx.exception))

    def test_preflight_rejects_logged_out_cli(self):
        with (
            patch("translate.shutil.which", return_value="/usr/bin/codex"),
            patch("translate.subprocess.run", return_value=MagicMock(returncode=1)),
            self.assertRaises(ValueError) as ctx,
        ):
            translate._codex_preflight("codex")
        self.assertIn("codex login", str(ctx.exception))


class TestProviderResolution(unittest.TestCase):
    def test_explicit_booleans_win_over_args(self):
        """Plusieurs tests existants appellent translate(..., use_mistral=True)
        avec un Namespace dépourvu d'attributs use_* : la résolution doit rester
        tolérante."""
        self.assertEqual(translate._resolve_provider(_args(), use_mistral=True), "mistral")
        self.assertEqual(translate._resolve_provider(_args(), use_claude=True), "claude")
        self.assertEqual(translate._resolve_provider(_args(), use_gemini=True), "gemini")

    def test_args_without_use_codex_defaults_to_openai(self):
        self.assertEqual(translate._resolve_provider(_args()), "openai")

    def test_use_codex_from_args(self):
        self.assertEqual(translate._resolve_provider(_args(use_codex=True)), "codex")

    def test_select_provider_client_tolerates_missing_use_codex(self):
        args = _args(model=None, use_mistral=False, use_claude=False, use_gemini=False)
        with patch("translate._init_openai_client", return_value="openai-client") as init:
            self.assertEqual(translate._select_provider_client(args), "openai-client")
        init.assert_called_once()

    def test_dispatch_routes_to_codex(self):
        with patch("translate._call_codex", return_value="translated") as call:
            out = translate._dispatch_provider_call(
                _client(), _args(), "PROMPT", "SEG", "codex", False
            )
        self.assertEqual(out, "translated")
        call.assert_called_once()

    def test_dispatch_empty_content_guard_names_codex(self):
        client = _client()
        args = _args()
        with (
            patch("translate._call_codex", return_value="   "),
            self.assertRaises(RuntimeError) as ctx,
        ):
            translate._dispatch_provider_call(client, args, "PROMPT", "SEG", "codex", False)
        self.assertIn("Codex CLI returned empty content", str(ctx.exception))


class TestReasoningEffortResolution(unittest.TestCase):
    """Le défaut implicite `medium` coûtait 45 reasoning tokens par appel sur
    gpt-5.4-mini en mode --eco, pour une traduction où il n'apporte rien."""

    def test_eco_defaults_to_none(self):
        self.assertEqual(
            translate._resolve_reasoning_effort(Namespace(eco=True, reasoning_effort=None)),
            "none",
        )

    def test_non_eco_defaults_to_medium(self):
        self.assertEqual(
            translate._resolve_reasoning_effort(Namespace(eco=False, reasoning_effort=None)),
            "medium",
        )

    def test_explicit_value_wins_over_eco(self):
        self.assertEqual(
            translate._resolve_reasoning_effort(Namespace(eco=True, reasoning_effort="high")),
            "high",
        )

    def test_codex_eco_default_is_low_not_none(self):
        """`none` n'est pas une valeur connue de model_reasoning_effort côté CLI."""
        self.assertEqual(
            translate._resolve_reasoning_effort(
                Namespace(eco=True, reasoning_effort=None), eco_default="low"
            ),
            "low",
        )

    def test_openai_extra_kwargs_applies_eco_default(self):
        args = Namespace(model="gpt-5.4-mini", eco=True, reasoning_effort=None)
        self.assertEqual(translate._openai_extra_kwargs(args, False), {"reasoning_effort": "none"})

    def test_translation_note_never_pays_for_reasoning(self):
        args = Namespace(model="gpt-5.4-mini", eco=False, reasoning_effort=None)
        self.assertEqual(translate._openai_extra_kwargs(args, True), {})


class TestClaudeBlockFiltering(unittest.TestCase):
    """Les modèles à raisonnement intercalent un bloc `thinking` avant le bloc
    `text`. Un ThinkingBlock expose `.thinking`, pas `.text`."""

    @staticmethod
    def _block(btype, **fields):
        return SimpleNamespace(type=btype, **fields)

    def _response(self, *blocks):
        return SimpleNamespace(stop_reason="end_turn", content=list(blocks))

    def test_thinking_block_is_skipped(self):
        response = self._response(
            self._block("thinking", thinking="Le document parle de..."),
            self._block("text", text="Translated body"),
        )
        client = MagicMock()
        client.messages.create.return_value = response
        out = translate._call_claude(client, _args(model="claude-sonnet-5"), "PROMPT", "SEG")
        self.assertEqual(out, "Translated body")

    def test_multiple_text_blocks_keep_structure(self):
        response = self._response(
            self._block("text", text="# Title"),
            self._block("text", text="Body"),
        )
        client = MagicMock()
        client.messages.create.return_value = response
        out = translate._call_claude(client, _args(model="claude-sonnet-4-6"), "PROMPT", "SEG")
        self.assertEqual(out, "# Title\n\nBody")

    def test_no_text_block_raises_explicitly(self):
        response = self._response(self._block("thinking", thinking="..."))
        client = MagicMock()
        client.messages.create.return_value = response
        args = _args(model="claude-sonnet-5")
        with self.assertRaises(RuntimeError) as ctx:
            translate._call_claude(client, args, "PROMPT", "SEG")
        self.assertIn("aucun bloc de texte", str(ctx.exception))


class TestGeminiThinkingFallback(unittest.TestCase):
    """`thinking_level="minimal"` n'est accepté que par une partie du catalogue
    (flash-lite oui, 3.7-flash et 3.1-pro non, en 400). Un paramètre
    d'optimisation ne doit jamais faire échouer une traduction."""

    @staticmethod
    def _client_refusing(n_levels):
        """Client qui refuse les `n_levels` premiers niveaux de la cascade."""
        calls = []

        def generate_content(model, contents, config):
            calls.append(getattr(config, "thinking_config", None))
            if len(calls) <= n_levels:
                raise translate.genai_errors.ClientError(
                    400, {"error": {"message": "Thinking level MINIMAL is not supported"}}
                )
            return SimpleNamespace(
                candidates=[SimpleNamespace(finish_reason="STOP")], text="Translated"
            )

        client = MagicMock()
        client.models.generate_content = generate_content
        return client, calls

    def setUp(self):
        # Le niveau accepté est mémorisé au niveau du module pour éviter un
        # aller-retour 400 par segment en production. C'est un état global :
        # sans cette remise à zéro, un test qui a déjà fait accepter `low` sur
        # gemini-3.7-flash ferait sauter la cascade au test suivant.
        translate._GEMINI_ACCEPTED_THINKING_LEVEL.clear()

    def test_first_level_accepted_stops_cascade(self):
        client, calls = self._client_refusing(0)
        out = translate._call_gemini(client, _args(model="gemini-3.1-flash-lite"), "P", "SEG")
        self.assertEqual(out, "Translated")
        self.assertEqual(len(calls), 1)

    def test_falls_back_to_next_level(self):
        client, calls = self._client_refusing(1)
        out = translate._call_gemini(client, _args(model="gemini-3.7-flash"), "P", "SEG")
        self.assertEqual(out, "Translated")
        self.assertEqual(len(calls), 2)

    def test_last_level_sends_no_thinking_config(self):
        client, calls = self._client_refusing(2)
        out = translate._call_gemini(client, _args(model="gemini-3.7-flash"), "P", "SEG")
        self.assertEqual(out, "Translated")
        self.assertEqual(len(calls), 3)
        self.assertIsNone(calls[-1], "le dernier essai ne doit porter aucun thinking_config")

    def test_all_levels_refused_raises(self):
        client, _ = self._client_refusing(99)
        args = _args(model="gemini-3.7-flash")
        with self.assertRaises(RuntimeError) as ctx:
            translate._call_gemini(client, args, "P", "SEG")
        self.assertIn("refusé tous les niveaux", str(ctx.exception))

    def test_unrelated_client_error_is_not_retried(self):
        """Une erreur qui ne parle pas de thinking (quota, clé invalide) doit
        remonter telle quelle, sans consommer la cascade."""
        calls = []

        def generate_content(model, contents, config):
            calls.append(config)
            raise translate.genai_errors.ClientError(
                429, {"error": {"message": "Resource exhausted"}}
            )

        client = MagicMock()
        client.models.generate_content = generate_content
        args = _args(model="gemini-3.7-flash")
        with self.assertRaises(translate.genai_errors.ClientError):
            translate._call_gemini(client, args, "P", "SEG")
        self.assertEqual(len(calls), 1)

    def test_system_instruction_carries_the_prompt(self):
        client, _calls = self._client_refusing(0)
        captured = {}

        def generate_content(model, contents, config):
            captured["config"] = config
            captured["contents"] = contents
            return SimpleNamespace(
                candidates=[SimpleNamespace(finish_reason="STOP")], text="Translated"
            )

        client.models.generate_content = generate_content
        translate._call_gemini(client, _args(model="gemini-3.7-flash"), "PROMPT", "SEGMENT")
        self.assertEqual(captured["config"].system_instruction, "PROMPT")
        self.assertEqual(captured["contents"], "SEGMENT")


class TestNewsMultiParagraphQuotes(unittest.TestCase):
    """Une citation EN peut couvrir plusieurs paragraphes séparés par une ligne
    `>` vide. Avant correctif, seul le dernier était protégé : les précédents
    partaient au LLM et revenaient traduits, ce que --news doit empêcher.
    Mesuré sur le corpus réel du blog : 11 citations concernées sur 419."""

    SINGLE = (
        "> A decade in the making.\n"
        ">\n"
        "> 🇫🇷 _Une décennie en gestation._\n"
        "> — [@GoogleAI sur X](https://x.com/GoogleAI/status/1)\n"
    )
    MULTI = (
        "> GLM-5.3 is now open-weight.\n"
        ">\n"
        "> Our most capable model is now available to download.\n"
        ">\n"
        "> 🇫🇷 _GLM-5.3 est désormais à poids ouverts._\n"
        "> — [@Zai_org sur X](https://x.com/Zai_org/status/2)\n"
    )

    def _protect(self, content):
        return translate._protect_news_quotes(content, Namespace(news=True))

    def test_single_paragraph_unchanged(self):
        _, quotes, urls = self._protect(self.SINGLE)
        self.assertEqual(quotes, ["> A decade in the making."])
        self.assertEqual(urls, ["https://x.com/GoogleAI/status/1"])

    def test_multi_paragraph_body_fully_captured(self):
        _, quotes, urls = self._protect(self.MULTI)
        self.assertEqual(len(quotes), 1)
        self.assertIn("GLM-5.3 is now open-weight.", quotes[0])
        self.assertIn("Our most capable model", quotes[0])
        self.assertEqual(urls, ["https://x.com/Zai_org/status/2"])

    def test_multi_paragraph_leaves_no_english_in_translatable_text(self):
        """Le texte soumis au LLM ne doit plus contenir la citation EN."""
        protected, _, _ = self._protect(self.MULTI)
        self.assertNotIn("GLM-5.3 is now open-weight.", protected)
        self.assertNotIn("Our most capable model", protected)
        self.assertIn(translate.news_quote_placeholder(0), protected)

    def test_round_trip_restores_every_paragraph(self):
        protected, quotes, _ = self._protect(self.MULTI)
        restored = translate._restore_news_quotes(protected, quotes)
        self.assertIn("> GLM-5.3 is now open-weight.", restored)
        self.assertIn("> Our most capable model is now available to download.", restored)

    def test_attribution_line_never_absorbed_into_body(self):
        """Le lookahead doit empêcher la ligne `> — ...` d'entrer dans le corps."""
        _, quotes, _ = self._protect(self.MULTI)
        self.assertNotIn("— [@Zai_org", quotes[0])

    def test_two_adjacent_quotes_stay_separate(self):
        _, quotes, urls = self._protect(self.SINGLE + "\n" + self.MULTI)
        self.assertEqual(len(quotes), 2)
        self.assertEqual(len(urls), 2)


class TestCodexBinaryResolution(unittest.TestCase):
    """Le binaire peut venir de trois sources : CODEX_BIN, le PATH, ou le
    package Python officiel `openai-codex-cli-bin`. Cette dernière voie évite
    d'imposer une installation npm globale à un projet Python."""

    @staticmethod
    def _fake_package(path="/pkg/bin/codex"):
        module = types.ModuleType("codex_cli_bin")
        module.bundled_codex_path = lambda: path
        return module

    def test_explicit_codex_bin_wins(self):
        with (
            patch.dict(os.environ, {"CODEX_BIN": "/custom/codex"}, clear=False),
            patch("translate.shutil.which", side_effect=lambda b: b),
        ):
            self.assertEqual(translate._resolve_codex_binary(), "/custom/codex")

    def test_path_used_when_no_explicit_bin(self):
        with (
            patch.dict(os.environ, {}, clear=True),
            patch("translate.shutil.which", return_value="/usr/bin/codex"),
        ):
            self.assertEqual(translate._resolve_codex_binary(), "/usr/bin/codex")

    def test_falls_back_to_python_package(self):
        """Cas npm absent : le binaire installé par pip doit être trouvé."""
        with (
            patch.dict(os.environ, {}, clear=True),
            patch("translate.shutil.which", return_value=None),
            patch.dict(sys.modules, {"codex_cli_bin": self._fake_package()}),
        ):
            self.assertEqual(translate._resolve_codex_binary(), "/pkg/bin/codex")

    def test_returns_none_when_nothing_available(self):
        with (
            patch.dict(os.environ, {}, clear=True),
            patch("translate.shutil.which", return_value=None),
            patch.dict(sys.modules, {"codex_cli_bin": None}),
        ):
            self.assertIsNone(translate._resolve_codex_binary())

    def test_preflight_error_mentions_both_install_paths(self):
        with self.assertRaises(ValueError) as ctx:
            translate._codex_preflight(None)
        message = str(ctx.exception)
        self.assertIn("pip install openai-codex-cli-bin", message)
        self.assertIn("npm install -g @openai/codex", message)

    def test_init_uses_resolved_binary(self):
        with (
            patch("translate._resolve_codex_binary", return_value="/pkg/bin/codex"),
            patch("translate._codex_preflight"),
            patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}, clear=False),
        ):
            client = translate._init_codex_client(_args(model=None))
        self.assertEqual(client.binary, "/pkg/bin/codex")


if __name__ == "__main__":
    unittest.main()
