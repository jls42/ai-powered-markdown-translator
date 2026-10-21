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

import io
import json
import os
import signal
import subprocess  # nosec B404 — CLI simulés ; seul bash tourne, avec un faux grok
import sys
import tempfile
import unittest
from argparse import Namespace
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from aipmt.providers import grok, openai, registry

# Pid de faux processus au-delà du plus grand pid possible (pid_max vaut
# 4 194 304) : si un doublage de `os.getpgid` sautait un jour, le vrai
# `getpgid` échouerait avant tout `killpg`, au lieu de viser le groupe d'un
# vrai processus — les pid font le tour en quelques heures sur ce poste, et
# 4242 peut exister. Cf. l'incident kill(-1) du 2026-09-26 dans CLAUDE.md.
_PID_INEXISTANT = 2**22 + 4242


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
    return grok._GrokCliClient(**defaults)


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
        self.pid = _PID_INEXISTANT

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


class TestGrokCliCall(unittest.TestCase):
    def test_nominal_returns_text(self):
        fake = _FakePopen()
        with patch("subprocess.Popen", fake):
            out = grok._call_grok_cli(_client(), _args(), "PROMPT", "SEGMENT")
        self.assertEqual(out, "Translated body")
        self.assertTrue(fake.kwargs["start_new_session"])

    def test_prompt_goes_through_a_file_never_argv(self):
        """Un segment de 16 000 caractères en argv serait visible dans `ps` et
        flirterait avec ARG_MAX ; le CLI ne lit pas stdin."""
        fake = _FakePopen()
        with patch("subprocess.Popen", fake):
            grok._call_grok_cli(_client(), _args(), "PROMPT", "SECRET-SEGMENT")
        self.assertIn("--prompt-file", fake.argv)
        self.assertNotIn("SECRET-SEGMENT", " ".join(fake.argv))

    def test_argv_carries_deny_catch_all(self):
        """`--deny` est la seule couche fail-closed : la règle `*` doit y être."""
        fake = _FakePopen()
        client = _client()
        args = _args()
        with patch("subprocess.Popen", fake):
            grok._call_grok_cli(client, args, "PROMPT", "SEG")
        argv = fake.argv
        denied = [argv[i + 1] for i, a in enumerate(argv) if a == "--deny"]
        self.assertIn("*", denied)
        for tool in ("Bash", "Edit", "Write", "MCPTool"):
            self.assertIn(f"{tool}(*)", denied)
        self.assertIn("--disable-web-search", argv)
        self.assertIn("--no-subagents", argv)

    def test_named_deny_rules_use_the_validated_prefix_form(self):
        """Le nom nu n'est PAS validé par le CLI, la forme `Prefix(*)` l'est.

        Mesuré sur grok 1.0.13 : `--deny 'CeciNestPasUnOutil(*)'` refuse le
        démarrage (« unknown tool prefix »), tandis que le même nom sans
        parenthèses est accepté en silence. Avec des noms nus, un renommage
        d'outil côté xAI retirerait donc la protection sans aucun signal — sur
        un poste où le sandbox OS ne s'applique déjà pas. Ce test empêche un
        retour à la forme non validée.
        """
        named = [r for r in grok.GROK_DENY_RULES if r != "*"]
        self.assertTrue(named, "les règles nommées ne doivent pas disparaître")
        for rule in named:
            self.assertTrue(
                rule.endswith("(*)"),
                f"règle {rule!r} sous forme nue : le CLI ne la valide pas",
            )

    def test_no_sandbox_flag_unless_opted_in(self):
        """Un profil intégré qui ne peut pas s'appliquer démarre NON confiné en
        silence : on ne le demande donc jamais implicitement."""
        fake = _FakePopen()
        with patch("subprocess.Popen", fake):
            grok._call_grok_cli(_client(), _args(), "PROMPT", "SEG")
        self.assertNotIn("--sandbox", fake.argv)

    def test_sandbox_flag_present_when_opted_in(self):
        fake = _FakePopen()
        with patch("subprocess.Popen", fake):
            grok._call_grok_cli(_client(sandbox_profile="read-only"), _args(), "P", "S")
        self.assertEqual(fake.argv[fake.argv.index("--sandbox") + 1], "read-only")

    def test_env_strips_api_keys_and_inherited_sandbox(self):
        fake = _FakePopen()
        env = {"XAI_API_KEY": "xai-leak", "GROK_SANDBOX": "read-only", "PATH": "/usr/bin"}
        with (
            patch.dict(os.environ, env, clear=False),
            patch("subprocess.Popen", fake),
        ):
            grok._call_grok_cli(_client(), _args(), "PROMPT", "SEG")
        child = fake.kwargs["env"]
        self.assertNotIn("XAI_API_KEY", child)
        self.assertNotIn("GROK_SANDBOX", child)
        self.assertEqual(child["GROK_CLAUDE_MCPS_ENABLED"], "false")

    def test_error_payload_raises_despite_exit_zero(self):
        """Mesuré : non authentifié, le CLI écrit {"type":"error"} sur stdout
        et sort en 0."""
        payload = json.dumps({"type": "error", "message": "Not signed in."})
        client = _client()
        args = _args()
        with (
            patch("subprocess.Popen", _FakePopen(stdout=payload, returncode=0)),
            self.assertRaises(RuntimeError) as ctx,
        ):
            grok._call_grok_cli(client, args, "PROMPT", "SEG")
        self.assertIn("Not signed in", str(ctx.exception))

    def test_abnormal_stop_reason_raises(self):
        payload = json.dumps({"text": "partial", "stopReason": "cancelled"})
        client = _client()
        args = _args()
        with (
            patch("subprocess.Popen", _FakePopen(stdout=payload)),
            self.assertRaises(RuntimeError) as ctx,
        ):
            grok._call_grok_cli(client, args, "PROMPT", "SEG")
        self.assertIn("stopReason anormal", str(ctx.exception))

    def test_empty_text_raises(self):
        payload = json.dumps({"text": "", "stopReason": "end_turn"})
        client = _client()
        args = _args()
        with (
            patch("subprocess.Popen", _FakePopen(stdout=payload)),
            self.assertRaises(RuntimeError) as ctx,
        ):
            grok._call_grok_cli(client, args, "PROMPT", "SEG")
        self.assertIn("aucun texte", str(ctx.exception))

    def test_non_json_stdout_raises(self):
        client = _client()
        args = _args()
        with (
            patch("subprocess.Popen", _FakePopen(stdout="oops not json")),
            self.assertRaises(RuntimeError) as ctx,
        ):
            grok._call_grok_cli(client, args, "PROMPT", "SEG")
        self.assertIn("illisible", str(ctx.exception))

    def test_structured_output_takes_precedence(self):
        payload = json.dumps(
            {
                "text": "fallback",
                "structuredOutput": {"markdown": "# Titre"},
                "stopReason": "end_turn",
            }
        )
        with patch("subprocess.Popen", _FakePopen(stdout=payload)):
            out = grok._call_grok_cli(_client(), _args(), "PROMPT", "SEG")
        self.assertEqual(out, "# Titre")

    def test_timeout_kills_process_group(self):
        client = _client(timeout=42)
        args = _args()
        with (
            patch("subprocess.Popen", _FakePopen(timeout=True)),
            patch("os.getpgid", return_value=_PID_INEXISTANT),
            patch("os.killpg") as killpg,
            self.assertRaises(RuntimeError) as ctx,
        ):
            grok._call_grok_cli(client, args, "PROMPT", "SEG")
        self.assertIn("Grok CLI timeout après 42s", str(ctx.exception))
        self.assertEqual(
            [c.args for c in killpg.call_args_list],
            [(_PID_INEXISTANT, signal.SIGTERM), (_PID_INEXISTANT, signal.SIGKILL)],
        )

    def test_rate_limit_is_retried(self):
        payload = json.dumps({"type": "error", "message": "rate limit exceeded"})
        attempts = []

        def factory(argv, **kwargs):
            attempts.append(argv)
            stdout = payload if len(attempts) == 1 else _OK_PAYLOAD
            return _FakePopen(stdout=stdout)(argv, **kwargs)

        with (
            patch("subprocess.Popen", factory),
            patch("time.sleep") as sleep,
        ):
            out = grok._call_grok_cli(_client(), _args(), "PROMPT", "SEG")
        self.assertEqual(out, "Translated body")
        self.assertEqual(len(attempts), 2)
        sleep.assert_called_once()


class TestGrokCliInit(unittest.TestCase):
    def test_preflight_detects_unauthenticated_despite_exit_zero(self):
        """`grok models` sort en 0 même déconnecté : le code retour ne suffit
        pas. La déconnexion n'est retenue qu'à la seconde réponse."""
        result = MagicMock(returncode=0, stdout="You are not authenticated.\n", stderr="")
        with (
            patch("subprocess.run", return_value=result) as run,
            patch("time.sleep") as sleep,
            patch("sys.stderr", new_callable=io.StringIO),
            self.assertRaises(ValueError) as ctx,
        ):
            grok._grok_preflight("/usr/bin/grok")
        self.assertIn("grok login", str(ctx.exception))
        self.assertEqual(run.call_count, 2)
        sleep.assert_called_once_with(grok.GROK_AUTH_RECHECK_DELAY)

    def test_preflight_asks_again_before_concluding_to_a_disconnection(self):
        """Mesuré le 2026-10-19 : « not authenticated » au moment où le CLI
        rafraîchissait son jeton, et les appels suivants passés. Une seconde
        réponse authentifiée suffit : pas de `grok login` à conseiller."""
        deconnecte = MagicMock(returncode=0, stdout="You are not authenticated.\n", stderr="")
        connecte = MagicMock(returncode=0, stdout="You are logged in with grok.com.", stderr="")
        with (
            patch("subprocess.run", side_effect=[deconnecte, connecte]) as run,
            patch("time.sleep") as sleep,
            patch("sys.stderr", new_callable=io.StringIO) as capture,
        ):
            grok._grok_preflight("/usr/bin/grok")
        self.assertEqual(run.call_count, 2)
        sleep.assert_called_once_with(grok.GROK_AUTH_RECHECK_DELAY)
        self.assertIn("nouvelle vérification", capture.getvalue())

    def test_preflight_accepts_authenticated(self):
        result = MagicMock(returncode=0, stdout="You are logged in with grok.com.", stderr="")
        with patch("subprocess.run", return_value=result) as run, patch("time.sleep") as sleep:
            grok._grok_preflight("/usr/bin/grok")
        run.assert_called_once()
        sleep.assert_not_called()

    def test_preflight_failure_is_not_asked_again(self):
        """Seul « not authenticated » est reposé : un `grok models` en échec
        échoue tout de suite, avec son code."""
        result = MagicMock(returncode=2, stdout="", stderr="boom")
        with (
            patch("subprocess.run", return_value=result) as run,
            patch("time.sleep") as sleep,
            self.assertRaises(ValueError) as ctx,
        ):
            grok._grok_preflight("/usr/bin/grok")
        self.assertIn("a échoué (code 2)", str(ctx.exception))
        run.assert_called_once()
        sleep.assert_not_called()

    def test_preflight_rejects_missing_binary(self):
        with self.assertRaises(ValueError) as ctx:
            grok._grok_preflight(None)
        self.assertIn("introuvable", str(ctx.exception))

    def test_binary_falls_back_to_grok_home(self):
        with (
            patch.dict(os.environ, {}, clear=True),
            patch("shutil.which", return_value=None),
            patch("os.path.isfile", return_value=True),
        ):
            self.assertTrue(grok._resolve_grok_binary().endswith("/.grok/bin/grok"))

    def test_refuses_ci_environment(self):
        args = _args(model=None)
        with (
            patch.dict(os.environ, {"CI": "true"}, clear=False),
            self.assertRaises(ValueError) as ctx,
        ):
            grok._init_grok_cli_client(args)
        self.assertIn("--use_grok_cli", str(ctx.exception))

    def test_eco_uses_model_available_on_subscription(self):
        """`grok models` n'expose plus que grok-4.7 depuis le 2026-10-21 : 4.6
        et 4.5 y sont refusés, et grok-4.3, l'éco de l'API, n'y a jamais été."""
        with (
            patch("aipmt.providers.grok._grok_preflight") as fake_preflight,
            patch("aipmt.providers.grok._resolve_grok_binary", return_value="/usr/bin/grok"),
            patch.dict(os.environ, {"CI": "", "GITHUB_ACTIONS": ""}, clear=False),
        ):
            args = _args(model=None, eco=True)
            grok._init_grok_cli_client(args)
        self.assertEqual(args.model, grok.ECO_MODEL_GROK_CLI)
        self.assertEqual(args.model, "grok-4.7")
        # Un patch mort exécuterait un vrai `grok models` : l'appel du double est exigé.
        fake_preflight.assert_called_once()


class TestGrokApiMode(unittest.TestCase):
    def test_requires_api_key(self):
        args = _args(model=None)
        with patch.dict(os.environ, {}, clear=True), self.assertRaises(ValueError) as ctx:
            grok._init_grok_client(args)
        self.assertIn("XAI_API_KEY", str(ctx.exception))

    def test_uses_xai_base_url(self):
        env = {"XAI_API_KEY": "xai-fixture-key"}  # pragma: allowlist secret
        with (
            patch.dict(os.environ, env, clear=True),
            patch("aipmt.providers.grok.OpenAI") as client,
        ):
            grok._init_grok_client(_args(model=None))
        self.assertEqual(client.call_args.kwargs["base_url"], grok.XAI_BASE_URL)

    def test_end_turn_finish_reason_accepted(self):
        """xAI émet `end_turn` là où OpenAI émet `stop`."""
        response = MagicMock()
        response.choices = [MagicMock(finish_reason="end_turn")]
        response.choices[0].message.content = "Translated"
        client = MagicMock()
        client.chat.completions.create.return_value = response
        out = openai._call_openai(client, _args(), "PROMPT", "SEG", False)
        self.assertEqual(out, "Translated")

    def test_api_mode_routes_through_openai_call(self):
        with patch("aipmt.providers.registry._call_openai", return_value="ok") as call:
            out = registry._dispatch_provider_call(
                MagicMock(), _args(), "PROMPT", "SEG", "grok", False
            )
        self.assertEqual(out, "ok")
        call.assert_called_once()

    def test_provider_resolution(self):
        self.assertEqual(registry._resolve_provider(_args(use_grok=True)), "grok")
        self.assertEqual(registry._resolve_provider(_args(use_grok_cli=True)), "grok_cli")
        self.assertEqual(registry._resolve_provider(_args()), "openai")


_REGEN = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "regen_translations.sh"
)

# Faux grok : la n-ième ligne de reponses.txt au n-ième appel, compté dans
# `appels`. Jamais le vrai binaire.
_FAUX_GROK = """#!/usr/bin/env bash
ici="$(dirname "$0")"
n=$(( $(cat "$ici/appels" 2>/dev/null || echo 0) + 1 ))
echo "$n" > "$ici/appels"
sed -n "${n}p" "$ici/reponses.txt"
"""


def _verifier_session_grok(*reponses):
    """Source regen_translations.sh dans un sous-shell — le sourçage ne lance
    pas main() — et appelle check_grok_auth sur un faux grok qui rend
    `reponses` dans l'ordre ; `sleep` y devient une fonction qui note son
    argument. Renvoie (code, stderr, nombre d'appels au faux grok)."""
    with tempfile.TemporaryDirectory() as dossier:
        faux = os.path.join(dossier, "grok")
        with open(faux, "w", encoding="utf-8") as f:
            f.write(_FAUX_GROK)
        os.chmod(faux, 0o700)
        with open(os.path.join(dossier, "reponses.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(reponses) + "\n")
        script = f'source "{_REGEN}"; sleep() {{ echo "sleep $*" >&2; }}; check_grok_auth "{faux}"'
        argv = ["bash", "-c", script]
        # nosemgrep
        proc = subprocess.run(  # nosec B603 B607 # nosemgrep — bash local et faux grok
            argv,  # nosemgrep
            cwd=dossier,
            env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": dossier},
            capture_output=True,
            text=True,
            check=False,
            timeout=60,
        )
        with open(os.path.join(dossier, "appels"), encoding="utf-8") as f:
            appels = int(f.read().strip() or 0)
    return proc.returncode, proc.stderr, appels


class TestRegenGrokAuth(unittest.TestCase):
    """check_grok_auth() de regen_translations.sh : même seconde question que
    le préflight d'aipmt, sans quoi une campagne lancée sur un jeton expiré
    s'arrêtait sur « lancer 'grok login' » avant d'atteindre aipmt."""

    _DECONNECTE = "You are not authenticated."
    _CONNECTE = "You are logged in with grok.com."

    def test_logged_in_at_once(self):
        rc, stderr, appels = _verifier_session_grok(self._CONNECTE)
        self.assertEqual((rc, appels), (0, 1), stderr)
        self.assertNotIn("sleep", stderr)

    def test_asks_again_after_a_token_refresh(self):
        rc, stderr, appels = _verifier_session_grok(self._DECONNECTE, self._CONNECTE)
        self.assertEqual((rc, appels), (0, 2), stderr)
        self.assertIn("sleep 5", stderr)
        self.assertNotIn("grok login", stderr)

    def test_still_disconnected_asks_to_log_in(self):
        rc, stderr, appels = _verifier_session_grok(self._DECONNECTE, self._DECONNECTE)
        self.assertEqual((rc, appels), (1, 2), stderr)
        self.assertIn("lancer 'grok login'", stderr)


if __name__ == "__main__":
    unittest.main()
