"""Couverture du provider OpenCode (agent open source, `opencode run`).

Les tests ne lancent jamais le vrai binaire : `subprocess.Popen` / `run` sont
mockés. Ils verrouillent les pièges mesurés en reconnaissance sur opencode
1.18.27 :

- un `--agent` inconnu ne fait PAS échouer la commande : avertissement sur
  stderr et repli silencieux sur l'agent par défaut — outils actifs, prompt de
  codage ;
- l'événement JSON d'erreur est opaque (« Unexpected server error », ref
  err_xxx) : la cause réelle ne vit que dans les logs `--print-logs` ;
- stdin est lu jusqu'à EOF et concaténé au message : il doit être fermé ;
- ~/.claude/CLAUDE.md et l'AGENTS.md du répertoire courant sont injectés dans
  chaque prompt tant que les interrupteurs ne sont pas posés ;
- aucune clé API ne doit fuiter dans l'environnement du sous-processus, à la
  seule exception d'OPENCODE_API_KEY, clé d'OpenCode lui-même.

Lancement : python -m unittest discover tests/ -v
"""

from __future__ import annotations

import io
import json
import os
import subprocess  # nosec B404 — la suite simule le CLI, elle n'en lance aucun
import sys
import unittest
from argparse import Namespace
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from aipmt import translate

# Valeur passée par référence : un littéral en face d'une clé *_API_KEY fait
# crier les scanners de secrets, alors qu'il ne s'agit que d'un jeton de test.
_MARQUEUR = "jeton-de-test"


def _args(**overrides):
    defaults = {
        "model": "ollama/qwen2.5:7b",
        "source_lang": "fr",
        "target_lang": "en",
        "news": False,
        "reasoning_effort": None,
        "eco": False,
    }
    defaults.update(overrides)
    return Namespace(**defaults)


def _client(**overrides):
    defaults = {"binary": "opencode", "timeout": 600}
    defaults.update(overrides)
    return translate._OpencodeClient(**defaults)


def _jsonl(*events):
    return "\n".join(json.dumps(e) for e in events) + "\n"


def _text_event(text, part_id="prt_1", **extra):
    part = {"id": part_id, "messageID": "msg_1", "type": "text", "text": text}
    part.update(extra)
    return {"type": "text", "sessionID": "ses_1", "part": part}


def _finish_event(reason="stop"):
    return {
        "type": "step_finish",
        "sessionID": "ses_1",
        "part": {
            "id": "prt_9",
            "type": "step-finish",
            "reason": reason,
            "tokens": {"total": 306, "input": 248, "output": 58, "reasoning": 0},
            "cost": 0,
        },
    }


_START = {"type": "step_start", "sessionID": "ses_1", "part": {"id": "prt_0", "type": "step-start"}}
_OK_EVENTS = _jsonl(_START, _text_event("Translated body"), _finish_event())
# Forme exacte mesurée : l'événement ne nomme pas la cause, seuls les logs le font.
_OPAQUE_ERROR = {
    "type": "error",
    "sessionID": "ses_1",
    "error": {
        "name": "UnknownError",
        "data": {"message": "Unexpected server error. Check server logs for details."},
    },
}
_LOG_CAUSE = (
    "timestamp=2026-09-04T09:45:33.621Z level=ERROR run=2ba6603f message=failed ref=err_e5f65b2b "
    'error="ProviderModelNotFoundError: Model not found: foo/bar. Did you mean: kimi?" '
    'cause="ProviderModelNotFoundError: Model not found: foo/bar\\n    at <anonymous>"\n'
)


class _FakePopen:
    def __init__(self, stdout=_OK_EVENTS, returncode=0, stderr="", timeout=False):
        self._stdout, self.returncode, self._stderr = stdout, returncode, stderr
        self._timeout = timeout
        self.argv = self.kwargs = self.communicate_kwargs = None
        self.pid = 4242

    def __call__(self, argv, **kwargs):
        self.argv, self.kwargs = argv, kwargs
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
        return self._stdout, self._stderr

    def wait(self, timeout=None):
        return self.returncode


class TestOpencodeCall(unittest.TestCase):
    def _run(self, fake, client=None, args=None, prompt="PROMPT SYSTÈME"):
        with patch.object(subprocess, "Popen", fake):
            return translate._call_opencode(client or _client(), args or _args(), prompt, "Segment")

    def test_nominal_returns_text_and_closes_stdin(self):
        fake = _FakePopen()
        self.assertEqual(self._run(fake), "Translated body")
        # stdin est lu jusqu'à EOF : `communicate(input=…)` le ferme toujours.
        self.assertEqual(fake.communicate_kwargs["input"], "Segment")
        self.assertIs(fake.kwargs["stdin"], subprocess.PIPE)
        self.assertTrue(fake.kwargs["start_new_session"])

    def test_argv_carries_confinement_flags_and_never_the_document(self):
        fake = _FakePopen()
        self._run(fake)
        argv = fake.argv
        self.assertEqual(argv[:2], ["opencode", "run"])
        for flag, value in (
            ("--format", "json"),
            ("--agent", translate.OPENCODE_AGENT_NAME),
            ("--model", "ollama/qwen2.5:7b"),
            ("--log-level", "ERROR"),
            ("--title", translate.OPENCODE_SESSION_TITLE),
        ):
            self.assertEqual(argv[argv.index(flag) + 1], value, flag)
        self.assertIn("--pure", argv)
        self.assertIn("--print-logs", argv)
        self.assertTrue(argv[argv.index("--dir") + 1].startswith(os.path.join("", "")))
        for forbidden in ("--auto", "--share", "--continue"):
            self.assertNotIn(forbidden, argv)
        self.assertNotIn("Segment", " ".join(argv))
        self.assertNotIn("PROMPT SYSTÈME", " ".join(argv))

    def test_variant_only_when_requested(self):
        fake = _FakePopen()
        self._run(fake)
        self.assertNotIn("--variant", fake.argv)
        fake = _FakePopen()
        self._run(fake, client=_client(variant="high"))
        self.assertEqual(fake.argv[fake.argv.index("--variant") + 1], "high")

    def test_inline_config_defines_a_toolless_agent(self):
        fake = _FakePopen()
        self._run(fake, prompt="Traduis vers l'anglais.")
        config = json.loads(fake.kwargs["env"]["OPENCODE_CONFIG_CONTENT"])
        self.assertEqual(config["permission"], {"*": "deny"})
        self.assertEqual(config["share"], "disabled")
        self.assertFalse(config["autoupdate"])
        agent = config["agent"][translate.OPENCODE_AGENT_NAME]
        self.assertEqual(agent["permission"], {"*": "deny"})
        self.assertEqual(agent["mode"], "primary")
        self.assertTrue(agent["prompt"].startswith("Traduis vers l'anglais."))
        self.assertIn("UNIQUEMENT", agent["prompt"])

    def test_env_carries_kill_switches(self):
        fake = _FakePopen()
        self._run(fake)
        for name, value in translate.OPENCODE_ENV_KILL_SWITCHES.items():
            self.assertEqual(fake.kwargs["env"].get(name), value, name)
        self.assertIn("OPENCODE_DISABLE_CLAUDE_CODE", translate.OPENCODE_ENV_KILL_SWITCHES)
        self.assertIn("OPENCODE_DISABLE_PROJECT_CONFIG", translate.OPENCODE_ENV_KILL_SWITCHES)

    def test_env_strips_api_keys_but_keeps_opencode_own_key(self):
        secrets = {
            "OPENAI_API_KEY": _MARQUEUR,
            "ANTHROPIC_API_KEY": _MARQUEUR,
            "XAI_API_KEY": _MARQUEUR,
            "HF_TOKEN": _MARQUEUR,
            "OPENAI_BASE_URL": "https://example.invalid/v1",
            "OPENCODE_API_KEY": _MARQUEUR,
        }
        with patch.dict(os.environ, secrets, clear=False):
            env = translate._opencode_env("PROMPT")
        leaked = sorted(name for name in secrets if name in env)
        self.assertEqual(leaked, ["OPENCODE_API_KEY"])
        self.assertEqual(env["OPENCODE_API_KEY"], _MARQUEUR)

    def test_opaque_error_event_is_completed_by_the_log_cause(self):
        fake = _FakePopen(stdout=_jsonl(_OPAQUE_ERROR), returncode=1, stderr=_LOG_CAUSE)
        with self.assertRaisesRegex(
            translate._OpencodeCallError, "ProviderModelNotFoundError"
        ) as cm:
            self._run(fake)
        self.assertIn("Model not found: foo/bar", str(cm.exception))
        # La trace Bun qui suit la cause n'est pas embarquée dans le message.
        self.assertNotIn("<anonymous>", str(cm.exception))

    def test_error_event_raises_even_with_exit_zero(self):
        fake = _FakePopen(stdout=_jsonl(_OPAQUE_ERROR, _text_event("partial")), returncode=0)
        with self.assertRaisesRegex(translate._OpencodeCallError, "OpenCode a échoué"):
            self._run(fake)

    def test_agent_fallback_warning_refuses_the_answer(self):
        stderr = '\x1b[93m! \x1b[0m agent "aipmt" not found. Falling back to default agent\n'
        fake = _FakePopen(stderr=stderr)
        with self.assertRaisesRegex(translate._OpencodeCallError, "n'a pas chargé l'agent"):
            self._run(fake)

    def test_tool_use_refuses_the_answer(self):
        tool = {
            "type": "tool_use",
            "sessionID": "ses_1",
            "part": {
                "id": "prt_5",
                "type": "tool",
                "tool": "bash",
                "state": {"status": "completed"},
            },
        }
        fake = _FakePopen(stdout=_jsonl(_START, tool, _text_event("t"), _finish_event()))
        with self.assertRaisesRegex(translate._OpencodeCallError, "appelé un outil .*bash"):
            self._run(fake)

    def test_missing_step_finish_refuses_the_answer(self):
        fake = _FakePopen(stdout=_jsonl(_START, _text_event("t")))
        with self.assertRaisesRegex(translate._OpencodeCallError, "aucun step_finish"):
            self._run(fake)

    def test_truncated_reason_refuses_the_answer(self):
        fake = _FakePopen(stdout=_jsonl(_START, _text_event("t"), _finish_event("length")))
        with self.assertRaisesRegex(translate._OpencodeCallError, "reason anormal='length'"):
            self._run(fake)

    def test_empty_text_refuses_the_answer(self):
        fake = _FakePopen(stdout=_jsonl(_START, _text_event("  \n"), _finish_event()))
        with self.assertRaisesRegex(translate._OpencodeCallError, "aucun texte"):
            self._run(fake)

    def test_no_text_event_at_all_refuses_the_answer(self):
        fake = _FakePopen(stdout=_jsonl(_START, _finish_event()))
        with self.assertRaisesRegex(translate._OpencodeCallError, "aucun texte"):
            self._run(fake)

    def test_nonzero_returncode_reports_the_log_cause(self):
        fake = _FakePopen(stdout="", returncode=1, stderr=_LOG_CAUSE)
        with self.assertRaisesRegex(
            translate._OpencodeCallError, "code 1.*ProviderModelNotFoundError"
        ):
            self._run(fake)

    def test_nonzero_returncode_without_logs_reports_stderr_tail(self):
        fake = _FakePopen(stdout="", returncode=3, stderr="ligne 1\nligne 2\nligne 3\nderniere")
        with self.assertRaisesRegex(translate._OpencodeCallError, "code 3.*derniere"):
            self._run(fake)

    def test_text_parts_are_joined_in_order_and_deduplicated(self):
        events = _jsonl(
            _START,
            _text_event("un", part_id="a"),
            _text_event("deux", part_id="b"),
            _text_event("un (réémis)", part_id="a"),
            _finish_event(),
        )
        self.assertEqual(self._run(_FakePopen(stdout=events)), "un (réémis)\ndeux")

    def test_synthetic_and_ignored_parts_are_not_the_model_output(self):
        events = _jsonl(
            _START,
            _text_event("injecté", part_id="s", synthetic=True),
            _text_event("réel", part_id="r"),
            _text_event("ignoré", part_id="i", ignored=True),
            _finish_event(),
        )
        self.assertEqual(self._run(_FakePopen(stdout=events)), "réel")

    def test_non_json_lines_are_ignored(self):
        events = "bannière\n" + _OK_EVENTS + "pas du json {\n"
        self.assertEqual(self._run(_FakePopen(stdout=events)), "Translated body")

    def test_timeout_kills_process_group_and_names_the_variable(self):
        fake = _FakePopen(timeout=True)
        client, args = _client(timeout=7), _args()
        with (
            patch.object(subprocess, "Popen", fake),
            patch.object(os, "getpgid", return_value=4242),
            patch.object(os, "killpg") as killpg,
            self.assertRaisesRegex(RuntimeError, "OPENCODE_TIMEOUT"),
        ):
            translate._call_opencode(client, args, "P", "S")
        killpg.assert_called()
        self.assertEqual(translate._CLI_TIMEOUT_ENV_VARS["OpenCode"], "OPENCODE_TIMEOUT")


class TestOpencodeRateLimitBackoff(unittest.TestCase):
    def _sequence(self, *fakes):
        calls = iter(fakes)

        def popen(argv, **kwargs):
            fake = next(calls)
            return fake(argv, **kwargs)

        return popen

    def test_429_status_is_retried_then_succeeds(self):
        error = {
            "type": "error",
            "sessionID": "ses_1",
            "error": {"name": "APIError", "data": {"message": "Too many", "statusCode": 429}},
        }
        popen = self._sequence(_FakePopen(stdout=_jsonl(error), returncode=1), _FakePopen())
        with (
            patch.object(subprocess, "Popen", popen),
            patch.object(translate.time, "sleep") as sleep,
            patch("sys.stderr", new_callable=io.StringIO),
        ):
            text = translate._call_opencode(_client(backoff_seconds=1.0), _args(), "P", "S")
        self.assertEqual(text, "Translated body")
        sleep.assert_called_once()

    def test_rate_limit_named_in_logs_is_retried(self):
        stderr = 'level=ERROR error="APIError: 429 Too Many Requests"\n'
        popen = self._sequence(_FakePopen(stdout="", returncode=1, stderr=stderr), _FakePopen())
        with (
            patch.object(subprocess, "Popen", popen),
            patch.object(translate.time, "sleep"),
            patch("sys.stderr", new_callable=io.StringIO),
        ):
            text = translate._call_opencode(_client(), _args(), "P", "S")
        self.assertEqual(text, "Translated body")

    def test_non_rate_limit_error_is_not_retried(self):
        client, args = _client(), _args()
        popen = self._sequence(
            _FakePopen(stdout=_jsonl(_OPAQUE_ERROR), returncode=1, stderr=_LOG_CAUSE)
        )
        with (
            patch.object(subprocess, "Popen", popen),
            patch.object(translate.time, "sleep") as sleep,
            self.assertRaises(translate._OpencodeCallError),
        ):
            translate._call_opencode(client, args, "P", "S")
        sleep.assert_not_called()

    def test_shared_backoff_covers_the_three_clis(self):
        """Le back-off est commun : les erreurs Codex et Grok doivent rester
        des `_CliCallError`, sinon la boucle partagée ne les verrait plus."""
        self.assertTrue(issubclass(translate._CodexCallError, translate._CliCallError))
        self.assertTrue(issubclass(translate._GrokCallError, translate._CliCallError))
        self.assertTrue(issubclass(translate._OpencodeCallError, translate._CliCallError))


class TestOpencodeInit(unittest.TestCase):
    def _preflight_ok(self):
        return patch.object(
            subprocess,
            "run",
            return_value=SimpleNamespace(returncode=0, stdout="1.18.27\n", stderr=""),
        )

    def test_model_is_required_and_the_message_says_how_to_list_them(self):
        args = _args(model=None)
        with self.assertRaisesRegex(ValueError, "exige --model") as cm:
            translate._init_opencode_client(args)
        self.assertIn("opencode models", str(cm.exception))
        self.assertIn("ollama/", str(cm.exception))

    def test_model_must_be_provider_slash_model(self):
        for bad in ("gpt-5", "/x", "a/", "-x/y", "a b/c"):
            args = _args(model=bad)
            with self.subTest(model=bad), self.assertRaisesRegex(ValueError, "invalide"):
                translate._init_opencode_client(args)

    def test_model_with_nested_slash_and_colon_is_accepted(self):
        with (
            patch.object(translate, "_resolve_opencode_binary", return_value="/bin/oc"),
            self._preflight_ok(),
        ):
            for good in (
                "ollama/qwen2.5:7b",
                "lmstudio/google/gemma-3n-e4b",
                "opencode/big-pickle",
            ):
                with self.subTest(model=good):
                    translate._init_opencode_client(_args(model=good))

    def test_eco_warns_that_it_has_no_effect(self):
        with (
            patch.object(translate, "_resolve_opencode_binary", return_value="/bin/oc"),
            self._preflight_ok(),
            patch("sys.stderr", new_callable=io.StringIO) as err,
        ):
            translate._init_opencode_client(_args(eco=True))
        self.assertIn("--eco est sans effet", err.getvalue())

    def test_variant_follows_explicit_reasoning_effort_only(self):
        with (
            patch.object(translate, "_resolve_opencode_binary", return_value="/bin/oc"),
            self._preflight_ok(),
        ):
            self.assertEqual(translate._init_opencode_client(_args()).variant, "")
            self.assertEqual(
                translate._init_opencode_client(_args(reasoning_effort="none")).variant, ""
            )
            self.assertEqual(
                translate._init_opencode_client(_args(reasoning_effort="high")).variant, "high"
            )

    def test_init_uses_resolved_binary_and_timeout(self):
        with (
            patch.object(translate, "_resolve_opencode_binary", return_value="/opt/oc"),
            self._preflight_ok(),
        ):
            client = translate._init_opencode_client(_args())
        self.assertEqual(client.binary, "/opt/oc")
        self.assertEqual(client.timeout, translate.OPENCODE_TIMEOUT)

    def test_not_refused_in_ci(self):
        """Contrairement aux CLI d'abonnement, OpenCode a des usages légitimes
        sur un runner (clé API, modèle local auto-hébergé)."""
        with (
            patch.dict(os.environ, {"CI": "1", "GITHUB_ACTIONS": "true"}, clear=False),
            patch.object(translate, "_resolve_opencode_binary", return_value="/bin/oc"),
            self._preflight_ok(),
        ):
            translate._init_opencode_client(_args())

    def test_preflight_rejects_missing_binary_and_names_install_paths(self):
        with self.assertRaisesRegex(ValueError, "introuvable") as cm:
            translate._opencode_preflight(None)
        for hint in ("opencode.ai/install", "npm install -g opencode-ai", "OPENCODE_BIN"):
            self.assertIn(hint, str(cm.exception))

    def test_preflight_rejects_failing_binary(self):
        failing = SimpleNamespace(returncode=1, stdout="", stderr="boom")
        with (
            patch.object(subprocess, "run", return_value=failing),
            self.assertRaisesRegex(ValueError, "a échoué .*boom"),
        ):
            translate._opencode_preflight("/bin/oc")

    def test_preflight_rejects_binary_without_version(self):
        odd = SimpleNamespace(returncode=0, stdout="usage: something", stderr="")
        with (
            patch.object(subprocess, "run", return_value=odd),
            self.assertRaisesRegex(ValueError, "a échoué"),
        ):
            translate._opencode_preflight("/bin/oc")

    def test_preflight_reports_unexecutable_binary(self):
        with (
            patch.object(subprocess, "run", side_effect=OSError("EACCES")),
            self.assertRaisesRegex(ValueError, "Impossible d'exécuter"),
        ):
            translate._opencode_preflight("/bin/oc")

    def test_preflight_environment_carries_no_secret(self):
        with (
            patch.dict(os.environ, {"OPENAI_API_KEY": _MARQUEUR}, clear=False),
            self._preflight_ok() as run,
        ):
            translate._opencode_preflight("/bin/oc")
        env = run.call_args.kwargs["env"]
        self.assertNotIn("OPENAI_API_KEY", env)
        self.assertEqual(run.call_args.args[0], ["/bin/oc", "--version"])


class TestOpencodeBinaryResolution(unittest.TestCase):
    def test_explicit_opencode_bin_wins(self):
        with (
            patch.dict(os.environ, {"OPENCODE_BIN": "/custom/oc"}, clear=False),
            patch.object(translate.shutil, "which", return_value=None),
            patch.object(translate.os.path, "isfile", return_value=True),
        ):
            self.assertEqual(translate._resolve_opencode_binary(), "/custom/oc")

    def test_path_used_when_no_explicit_bin(self):
        with (
            patch.dict(os.environ, {}, clear=False),
            patch.object(translate.shutil, "which", return_value="/usr/local/bin/opencode"),
        ):
            os.environ.pop("OPENCODE_BIN", None)
            self.assertEqual(translate._resolve_opencode_binary(), "/usr/local/bin/opencode")

    def test_falls_back_to_installer_location(self):
        home = os.path.join(os.path.expanduser("~"), ".opencode", "bin", "opencode")
        with (
            patch.dict(os.environ, {}, clear=False),
            patch.object(translate.shutil, "which", return_value=None),
            patch.object(translate.os.path, "isfile", side_effect=lambda p: p == home),
        ):
            os.environ.pop("OPENCODE_BIN", None)
            self.assertEqual(translate._resolve_opencode_binary(), home)

    def test_returns_none_when_nothing_available(self):
        with (
            patch.dict(os.environ, {}, clear=False),
            patch.object(translate.shutil, "which", return_value=None),
            patch.object(translate.os.path, "isfile", return_value=False),
        ):
            os.environ.pop("OPENCODE_BIN", None)
            self.assertIsNone(translate._resolve_opencode_binary())


class TestProviderWiring(unittest.TestCase):
    def test_resolve_provider_from_args(self):
        self.assertEqual(translate._resolve_provider(Namespace(use_opencode=True)), "opencode")

    def test_label(self):
        self.assertEqual(translate._PROVIDER_LABELS["opencode"], "OpenCode")

    def test_dispatch_routes_to_opencode(self):
        with patch.object(translate, "_call_opencode", return_value="ok") as call:
            text = translate._dispatch_provider_call("client", _args(), "P", "S", "opencode", False)
        self.assertEqual(text, "ok")
        call.assert_called_once_with("client", unittest.mock.ANY, "P", "S")

    def test_dispatch_empty_content_guard_names_opencode(self):
        args = _args()
        with (
            patch.object(translate, "_call_opencode", return_value="   "),
            self.assertRaisesRegex(RuntimeError, "OpenCode returned empty content"),
        ):
            translate._dispatch_provider_call("client", args, "P", "S", "opencode", False)

    def test_select_provider_client_routes_to_init(self):
        args = Namespace(
            use_mistral=False,
            use_claude=False,
            use_gemini=False,
            use_codex=False,
            use_grok_cli=False,
            use_grok=False,
            use_opencode=True,
        )
        with patch.object(translate, "_init_opencode_client", return_value="client") as init:
            self.assertEqual(translate._select_provider_client(args), "client")
        init.assert_called_once_with(args)

    def test_flag_is_in_the_exclusive_group(self):
        import argparse

        parser = argparse.ArgumentParser()
        translate._add_provider_args(parser)
        self.assertTrue(parser.parse_args(["--use_opencode"]).use_opencode)
        for other in ("--use_codex", "--use_mistral", "--use_grok_cli"):
            with self.subTest(other=other), self.assertRaises(SystemExit):
                parser.parse_args(["--use_opencode", other])


class TestModelFilenameLabel(unittest.TestCase):
    """`provider/modèle` dans un nom de fichier `--include_model` créerait un
    sous-répertoire, et `ollama/qwen2.5:7b` est illégal sous Windows."""

    def test_label_replaces_separators(self):
        self.assertEqual(translate._model_filename_label("ollama/qwen2.5:7b"), "ollama-qwen2.5-7b")
        self.assertEqual(translate._model_filename_label("gpt-5.4-mini"), "gpt-5.4-mini")
        self.assertEqual(translate._model_filename_label(None), "")

    def test_single_file_naming(self):
        args = Namespace(
            keep_filename=False,
            include_model=True,
            file="/src/article.md",
            target_lang="en",
            model="lmstudio/google/gemma-3n-e4b",
        )
        self.assertEqual(
            translate._resolve_single_output_filename(args),
            "article-en-lmstudio-google-gemma-3n-e4b.md",
        )

    def test_directory_naming(self):
        args = Namespace(
            keep_filename=False, include_model=True, target_lang="de", model="ollama/qwen2.5:7b"
        )
        self.assertEqual(
            translate._resolve_output_filename("doc.md", "doc", args), "doc-de-ollama-qwen2.5-7b.md"
        )

    def test_component_guard_accepts_provider_model_but_still_rejects_traversal(self):
        base = {"target_lang": "en", "source_lang": "fr"}
        translate._reject_path_separators_in_components(
            Namespace(model="ollama/qwen2.5:7b", **base)
        )
        for bad in ("..", "."):
            args = Namespace(model=bad, **base)
            with self.subTest(model=bad), self.assertRaisesRegex(ValueError, "--model"):
                translate._reject_path_separators_in_components(args)
        evasion = Namespace(model="ollama/x", target_lang="../../tmp/EVASION", source_lang="fr")
        with self.assertRaisesRegex(ValueError, "--target_lang"):
            translate._reject_path_separators_in_components(evasion)

    def test_traversal_through_model_stays_inside_target_dir(self):
        """Contre-épreuve de la seconde couche : même sans la garde amont, le
        libellé neutralise `../` et le chemin calculé reste sous la cible."""
        args = Namespace(
            keep_filename=False,
            include_model=True,
            file="/src/doc.md",
            target_lang="en",
            model="../../../tmp/EVASION",
        )
        name = translate._resolve_single_output_filename(args)
        self.assertEqual(name, "doc-en-..-..-..-tmp-EVASION.md")
        self.assertEqual(
            translate._ensure_within_directory("/out", os.path.join("/out", name)),
            os.path.join("/out", name),
        )


if __name__ == "__main__":
    unittest.main()
