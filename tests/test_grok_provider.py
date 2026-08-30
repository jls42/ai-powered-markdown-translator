"""Couverture des deux providers Grok : API xAI et CLI Grok Build.

Les tests ne lancent jamais le vrai binaire. Ils verrouillent les pièges
mesurés en reconnaissance sur `grok` 1.0.13 :

- `exit 0` ne prouve rien : une erreur d'authentification, un refus ou un
  dépassement de tours sortent tous en 0 avec un JSON d'apparence normale ;
- le confinement repose sur les règles `--deny` (seule couche fail-closed
  mesurée), le sandbox OS étant inapplicable sur beaucoup de postes Linux ;
- aucune clé API ne doit fuiter dans l'environnement du sous-processus, sans
  quoi la traduction serait facturée à l'usage au lieu d'être décomptée de
  l'abonnement.

Lancement : python -m unittest discover tests/ -v
"""

from __future__ import annotations

import json
import os
import subprocess  # nosec B404 — la suite simule les CLI, elle n'en lance aucun
import sys
import unittest
from argparse import Namespace
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import translate


def _args(**overrides):
    defaults = {
        "model": "grok-4.6",
        "source_lang": "fr",
        "target_lang": "en",
        "news": False,
        "reasoning_effort": None,
        "eco": False,
    }
    defaults.update(overrides)
    return Namespace(**defaults)


def _client(**overrides):
    defaults = {"binary": "grok", "timeout": 900}
    defaults.update(overrides)
    return translate._GrokCliClient(**defaults)


_OK_PAYLOAD = json.dumps(
    {
        "text": "Translated body",
        "stopReason": "end_turn",
        "usage": {"input_tokens": 17777, "output_tokens": 94},
        "num_turns": 1,
    }
)


class _FakePopen:
    def __init__(self, stdout=_OK_PAYLOAD, returncode=0, stderr="", timeout=False):
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
            # nosemgrep: dangerous-subprocess-use — TimeoutExpired est une classe
            # d'exception levée par un faux Popen, pas un lancement de process.
            raise subprocess.TimeoutExpired(cmd=self.argv, timeout=kwargs.get("timeout"))
        return self._stdout, self._stderr

    def wait(self, timeout=None):
        return self.returncode


class TestGrokCliCall(unittest.TestCase):
    def test_nominal_returns_text(self):
        fake = _FakePopen()
        with patch("translate.subprocess.Popen", fake):
            out = translate._call_grok_cli(_client(), _args(), "PROMPT", "SEGMENT")
        self.assertEqual(out, "Translated body")
        self.assertTrue(fake.kwargs["start_new_session"])

    def test_prompt_goes_through_a_file_never_argv(self):
        """Un segment de 16 000 caractères en argv serait visible dans `ps` et
        flirterait avec ARG_MAX ; le CLI ne lit pas stdin."""
        fake = _FakePopen()
        with patch("translate.subprocess.Popen", fake):
            translate._call_grok_cli(_client(), _args(), "PROMPT", "SECRET-SEGMENT")
        self.assertIn("--prompt-file", fake.argv)
        self.assertNotIn("SECRET-SEGMENT", " ".join(fake.argv))

    def test_argv_carries_deny_catch_all(self):
        """`--deny` est la seule couche fail-closed : la règle `*` doit y être."""
        fake = _FakePopen()
        with patch("translate.subprocess.Popen", fake):
            translate._call_grok_cli(_client(), _args(), "PROMPT", "SEG")
        argv = fake.argv
        denied = [argv[i + 1] for i, a in enumerate(argv) if a == "--deny"]
        self.assertIn("*", denied)
        for tool in ("Bash", "Edit", "Write", "MCPTool"):
            self.assertIn(tool, denied)
        self.assertIn("--disable-web-search", argv)
        self.assertIn("--no-subagents", argv)

    def test_no_sandbox_flag_unless_opted_in(self):
        """Un profil intégré qui ne peut pas s'appliquer démarre NON confiné en
        silence : on ne le demande donc jamais implicitement."""
        fake = _FakePopen()
        with patch("translate.subprocess.Popen", fake):
            translate._call_grok_cli(_client(), _args(), "PROMPT", "SEG")
        self.assertNotIn("--sandbox", fake.argv)

    def test_sandbox_flag_present_when_opted_in(self):
        fake = _FakePopen()
        with patch("translate.subprocess.Popen", fake):
            translate._call_grok_cli(_client(sandbox_profile="read-only"), _args(), "P", "S")
        self.assertEqual(fake.argv[fake.argv.index("--sandbox") + 1], "read-only")

    def test_env_strips_api_keys_and_inherited_sandbox(self):
        fake = _FakePopen()
        env = {"XAI_API_KEY": "xai-leak", "GROK_SANDBOX": "read-only", "PATH": "/usr/bin"}
        with patch.dict(os.environ, env, clear=False), patch("translate.subprocess.Popen", fake):
            translate._call_grok_cli(_client(), _args(), "PROMPT", "SEG")
        child = fake.kwargs["env"]
        self.assertNotIn("XAI_API_KEY", child)
        self.assertNotIn("GROK_SANDBOX", child)
        self.assertEqual(child["GROK_CLAUDE_MCPS_ENABLED"], "false")

    def test_error_payload_raises_despite_exit_zero(self):
        """Mesuré : non authentifié, le CLI écrit {"type":"error"} sur stdout
        et sort en 0."""
        payload = json.dumps({"type": "error", "message": "Not signed in."})
        with (
            patch("translate.subprocess.Popen", _FakePopen(stdout=payload, returncode=0)),
            self.assertRaises(RuntimeError) as ctx,
        ):
            translate._call_grok_cli(_client(), _args(), "PROMPT", "SEG")
        self.assertIn("Not signed in", str(ctx.exception))

    def test_abnormal_stop_reason_raises(self):
        payload = json.dumps({"text": "partial", "stopReason": "cancelled"})
        with (
            patch("translate.subprocess.Popen", _FakePopen(stdout=payload)),
            self.assertRaises(RuntimeError) as ctx,
        ):
            translate._call_grok_cli(_client(), _args(), "PROMPT", "SEG")
        self.assertIn("stopReason anormal", str(ctx.exception))

    def test_empty_text_raises(self):
        payload = json.dumps({"text": "", "stopReason": "end_turn"})
        with (
            patch("translate.subprocess.Popen", _FakePopen(stdout=payload)),
            self.assertRaises(RuntimeError) as ctx,
        ):
            translate._call_grok_cli(_client(), _args(), "PROMPT", "SEG")
        self.assertIn("aucun texte", str(ctx.exception))

    def test_non_json_stdout_raises(self):
        with (
            patch("translate.subprocess.Popen", _FakePopen(stdout="oops not json")),
            self.assertRaises(RuntimeError) as ctx,
        ):
            translate._call_grok_cli(_client(), _args(), "PROMPT", "SEG")
        self.assertIn("illisible", str(ctx.exception))

    def test_structured_output_takes_precedence(self):
        payload = json.dumps(
            {
                "text": "fallback",
                "structuredOutput": {"markdown": "# Titre"},
                "stopReason": "end_turn",
            }
        )
        with patch("translate.subprocess.Popen", _FakePopen(stdout=payload)):
            out = translate._call_grok_cli(_client(), _args(), "PROMPT", "SEG")
        self.assertEqual(out, "# Titre")

    def test_timeout_kills_process_group(self):
        with (
            patch("translate.subprocess.Popen", _FakePopen(timeout=True)),
            patch("translate.os.getpgid", return_value=4242),
            patch("translate.os.killpg") as killpg,
            self.assertRaises(RuntimeError) as ctx,
        ):
            translate._call_grok_cli(_client(timeout=42), _args(), "PROMPT", "SEG")
        self.assertIn("Grok CLI timeout après 42s", str(ctx.exception))
        killpg.assert_called_once()

    def test_rate_limit_is_retried(self):
        payload = json.dumps({"type": "error", "message": "rate limit exceeded"})
        attempts = []

        def factory(argv, **kwargs):
            attempts.append(argv)
            stdout = payload if len(attempts) == 1 else _OK_PAYLOAD
            return _FakePopen(stdout=stdout)(argv, **kwargs)

        with patch("translate.subprocess.Popen", factory), patch("translate.time.sleep") as sleep:
            out = translate._call_grok_cli(_client(), _args(), "PROMPT", "SEG")
        self.assertEqual(out, "Translated body")
        self.assertEqual(len(attempts), 2)
        sleep.assert_called_once()


class TestGrokCliInit(unittest.TestCase):
    def test_preflight_detects_unauthenticated_despite_exit_zero(self):
        """`grok models` sort en 0 même déconnecté : le code retour ne suffit pas."""
        result = MagicMock(returncode=0, stdout="You are not authenticated.\n", stderr="")
        with (
            patch("translate.subprocess.run", return_value=result),
            self.assertRaises(ValueError) as ctx,
        ):
            translate._grok_preflight("/usr/bin/grok")
        self.assertIn("grok login", str(ctx.exception))

    def test_preflight_accepts_authenticated(self):
        result = MagicMock(returncode=0, stdout="You are logged in with grok.com.", stderr="")
        with patch("translate.subprocess.run", return_value=result):
            translate._grok_preflight("/usr/bin/grok")

    def test_preflight_rejects_missing_binary(self):
        with self.assertRaises(ValueError) as ctx:
            translate._grok_preflight(None)
        self.assertIn("introuvable", str(ctx.exception))

    def test_binary_falls_back_to_grok_home(self):
        with (
            patch.dict(os.environ, {}, clear=True),
            patch("translate.shutil.which", return_value=None),
            patch("translate.os.path.isfile", return_value=True),
        ):
            self.assertTrue(translate._resolve_grok_binary().endswith("/.grok/bin/grok"))

    def test_refuses_ci_environment(self):
        with (
            patch.dict(os.environ, {"CI": "true"}, clear=False),
            self.assertRaises(ValueError) as ctx,
        ):
            translate._init_grok_cli_client(_args(model=None))
        self.assertIn("--use_grok_cli", str(ctx.exception))

    def test_eco_uses_model_available_on_subscription(self):
        """`grok models` n'expose que 4.6 et 4.5 : grok-4.3 n'est pas disponible."""
        with (
            patch("translate._grok_preflight"),
            patch("translate._resolve_grok_binary", return_value="/usr/bin/grok"),
            patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}, clear=False),
        ):
            args = _args(model=None, eco=True)
            translate._init_grok_cli_client(args)
        self.assertEqual(args.model, translate.ECO_MODEL_GROK_CLI)
        self.assertEqual(args.model, "grok-4.5")


class TestGrokApiMode(unittest.TestCase):
    def test_requires_api_key(self):
        with patch.dict(os.environ, {}, clear=True), self.assertRaises(ValueError) as ctx:
            translate._init_grok_client(_args(model=None))
        self.assertIn("XAI_API_KEY", str(ctx.exception))

    def test_uses_xai_base_url(self):
        env = {"XAI_API_KEY": "xai-fixture-key"}  # pragma: allowlist secret
        with patch.dict(os.environ, env, clear=True), patch("translate.OpenAI") as client:
            translate._init_grok_client(_args(model=None))
        self.assertEqual(client.call_args.kwargs["base_url"], translate.XAI_BASE_URL)

    def test_end_turn_finish_reason_accepted(self):
        """xAI émet `end_turn` là où OpenAI émet `stop`."""
        response = MagicMock()
        response.choices = [MagicMock(finish_reason="end_turn")]
        response.choices[0].message.content = "Translated"
        client = MagicMock()
        client.chat.completions.create.return_value = response
        out = translate._call_openai(client, _args(), "PROMPT", "SEG", False)
        self.assertEqual(out, "Translated")

    def test_api_mode_routes_through_openai_call(self):
        with patch("translate._call_openai", return_value="ok") as call:
            out = translate._dispatch_provider_call(
                MagicMock(), _args(), "PROMPT", "SEG", "grok", False
            )
        self.assertEqual(out, "ok")
        call.assert_called_once()

    def test_provider_resolution(self):
        self.assertEqual(translate._resolve_provider(_args(use_grok=True)), "grok")
        self.assertEqual(translate._resolve_provider(_args(use_grok_cli=True)), "grok_cli")
        self.assertEqual(translate._resolve_provider(_args()), "openai")


if __name__ == "__main__":
    unittest.main()
