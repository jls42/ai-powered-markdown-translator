"""Couverture du provider Claude Code (CLI `claude -p`, quota d'abonnement Claude).

Les tests ne lancent JAMAIS le vrai binaire — installé sur le poste du
propriétaire, il consommerait le quota de l'abonnement, partagé avec ses
sessions Claude Code. `_codex_run_process` et `subprocess.run` sont remplacés
par des doubles, l'environnement est vidé (`patch.dict(os.environ, clear=True)`
— la suite peut tourner DANS une session Claude Code, qui exporte CLAUDECODE et
une quinzaine de marqueurs), HOME est temporaire, AIPMT_CLAUDE_BIN désigne un
chemin inexistant et le PATH ne contient aucun `claude`. Le seul sous-processus
réel est bash, pour `regen_translations.sh`, sans `claude` atteignable.

Ils verrouillent ce qui a été mesuré sur Claude Code 2.1.283 le 2026-09-26 :

- l'environnement du sous-processus est une liste d'autorisation : aucune clé,
  aucun fournisseur cloud, aucun marqueur de session ; sans
  CLAUDE_CODE_DISABLE_ATTACHMENTS, un `@chemin` du document devient une pièce
  jointe ;
- sous --disable-slash-commands, un message qui commence par `/` n'atteint pas
  le modèle (réponse synthétique en SUCCESS, zéro tour) : stdin est précédé
  d'un saut de ligne ;
- le flux stream-json atteste la voie de facturation (`apiKeySource: none`,
  `analytics_disabled`), le modèle réellement servi (`modelUsage`) et le quota
  (`rate_limit_event`, dont l'extra usage payant) ;
- `claude auth status --json` et `/usage` le disent aussi, sans tour de modèle.

Lancement : python -m unittest discover tests/ -v
"""

from __future__ import annotations

import contextlib
import io
import json
import os
import subprocess  # nosec B404 — doubles de run ; seul bash tourne, sans `claude` atteignable
import sys
import tempfile
import unittest
from argparse import Namespace
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from aipmt import cli, config
from aipmt.providers import base, claude_code, registry

_RACINE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_SRC = os.path.join(_RACINE, "src")
_REGEN = os.path.join(_RACINE, "regen_translations.sh")

# Chemin inexistant À DESSEIN : un patch qui ne mordrait pas ferait échouer le
# lancement au lieu d'exécuter le vrai `claude`.
_BINAIRE = "/chemin/inexistant/claude-double-de-test"

# Effet des doubles qui ne doivent JAMAIS servir : un appel imprévu échoue ici,
# avant tout processus (cf. CLAUDE.md, « Tests de signaux »).
_NE_DOIT_PAS_SERVIR = AssertionError("ce double ne doit jamais être appelé")

_TMPDIR_REEL = tempfile.gettempdir()
_VERSION = "2.1.283"
_MODELE_SONNET = "claude-sonnet-5"


def _args(**overrides):
    values = {"model": "sonnet", "eco": False, "reasoning_effort": None}
    values.update(overrides)
    return Namespace(**values)


def _client(**overrides):
    values = {"binary": _BINAIRE, "version": _VERSION, "config_dir": "/home/x/.claude"}
    values.update(overrides)
    return claude_code._ClaudeCodeClient(**values)


def _init(**overrides):
    """Événement d'initialisation tel que mesuré (p02), réduit aux clés lues."""
    event = {
        "type": "system",
        "subtype": "init",
        "model": _MODELE_SONNET,
        "apiKeySource": "none",  # pragma: allowlist secret
        "tools": [],
        "mcp_servers": [],
        "plugins": [{"name": "agents-md", "path": "builtin", "source": "agents-md@builtin"}],
        "skills": [],
        "slash_commands": [],
        "fast_mode_state": "off",
        "claude_code_version": _VERSION,
        "analytics_disabled": True,
    }
    event.update(overrides)
    return event


def _rate(**info):
    base_info = {
        "status": "allowed",
        "rateLimitType": "five_hour",
        "isUsingOverage": False,
        "unifiedWindows": {
            "five_hour": {"utilization": 0.1, "resetsAt": 111},
            "seven_day": {"utilization": 0.5, "resetsAt": 222},
        },
    }
    base_info.update(info)
    return {"type": "rate_limit_event", "rate_limit_info": base_info}


def _result(**overrides):
    event = {
        "type": "result",
        "subtype": "success",
        "is_error": False,
        "num_turns": 1,
        "stop_reason": "end_turn",
        "permission_denials": [],
        "modelUsage": {_MODELE_SONNET: {"inputTokens": 533, "outputTokens": 15}},
        "result": "The cat is sleeping on the rug.",
    }
    event.update(overrides)
    return event


def _flux(*events):
    return "\n".join(json.dumps(e) for e in events) + "\n"


def _flux_ok(**result_overrides):
    return _flux(
        _init(),
        _rate(),
        {"type": "assistant", "message": {"model": _MODELE_SONNET}},
        _result(**result_overrides),
    )


@contextlib.contextmanager
def _env_sans_claude(**extra):
    """Environnement vidé : HOME temporaire, binaire inexistant, PATH sans
    `claude`, hors CI. Rien de la session réelle n'y survit."""
    with tempfile.TemporaryDirectory(dir=_TMPDIR_REEL) as home:
        env = {
            "HOME": home,
            "PATH": "/chemin/inexistant/bin",
            "AIPMT_CLAUDE_BIN": _BINAIRE,
            "XDG_CACHE_HOME": os.path.join(home, "cache"),
        }
        env.update(extra)
        with patch.dict(os.environ, env, clear=True):
            yield home


class _CcTestCase(unittest.TestCase):
    def setUp(self):
        self._env = _env_sans_claude()
        self.home = self._env.__enter__()
        self.addCleanup(self._env.__exit__, None, None, None)


# --- Environnement --------------------------------------------------------------


class TestClaudeCodeEnvironment(unittest.TestCase):
    def test_only_the_allowlist_and_the_overrides_reach_the_cli(self):
        """Par ÉGALITÉ : tout ce qui n'est pas autorisé disparaît, dont les clés,
        les fournisseurs cloud et les quinze marqueurs de session mesurés."""
        hostile = {
            "PATH": "/usr/bin",
            "HOME": "/home/x",
            "LANG": "fr_FR.UTF-8",
            "LC_ALL": "fr_FR.UTF-8",
            "HTTPS_PROXY": "http://proxy:3128",
            "CLAUDE_CONFIG_DIR": "/home/x/.config/aipmt/claude",
            "ANTHROPIC_API_KEY": "sk-ant-test",  # pragma: allowlist secret
            "ANTHROPIC_AUTH_TOKEN": "bearer",  # pragma: allowlist secret  # nosec B105
            "ANTHROPIC_BASE_URL": "https://gateway.example",
            "ANTHROPIC_PROFILE": "work",
            "CLAUDE_CODE_OAUTH_TOKEN": "tok",  # pragma: allowlist secret  # nosec B105
            "CLAUDE_CODE_USE_BEDROCK": "1",
            "CLAUDE_CODE_USE_VERTEX": "1",
            "CLAUDE_CODE_RETRY_WATCHDOG": "1",
            "CLAUDE_CODE_EFFORT_LEVEL": "max",
            "CLAUDECODE": "1",
            "CLAUDE_CODE_SESSION_ID": "s",
            "CLAUDE_CODE_MESSAGING_SOCKET": "/run/x.sock",
            "CLAUDE_CODE_MESSAGING_TOKEN": "t",  # pragma: allowlist secret  # nosec B105
            "CLAUDE_CODE_CHILD_SESSION": "1",
            "CLAUDE_PID": "123",
            "CLAUDE_CODE_SIMPLE": "1",
            "AWS_PROFILE": "p",
            "NODE_OPTIONS": "--require /tmp/x.js",
        }
        with patch.dict(os.environ, hostile, clear=True):
            env = claude_code._claude_code_env()
        attendu = {
            "PATH": "/usr/bin",
            "HOME": "/home/x",
            "LANG": "fr_FR.UTF-8",
            "LC_ALL": "fr_FR.UTF-8",
            "HTTPS_PROXY": "http://proxy:3128",
            "CLAUDE_CONFIG_DIR": "/home/x/.config/aipmt/claude",
            **claude_code.CLAUDE_CODE_ENV_OVERRIDES,
        }
        self.assertEqual(env, attendu)

    def test_attachments_are_always_disabled(self):
        """Mesuré : sans cette variable, un `@chemin` du document devient une
        pièce jointe et le modèle rend `{"file_path": …}`."""
        self.assertEqual(
            claude_code.CLAUDE_CODE_ENV_OVERRIDES["CLAUDE_CODE_DISABLE_ATTACHMENTS"], "1"
        )

    def test_config_dir_follows_claude_config_dir(self):
        with patch.dict(os.environ, {"HOME": "/home/x"}, clear=True):
            self.assertEqual(claude_code._claude_code_config_dir(), "/home/x/.claude")
        with patch.dict(os.environ, {"HOME": "/home/x", "CLAUDE_CONFIG_DIR": "/c"}, clear=True):
            self.assertEqual(claude_code._claude_code_config_dir(), "/c")


class TestClaudeCodeWorkBase(unittest.TestCase):
    def test_under_an_absolute_xdg_cache_home_and_private(self):
        with tempfile.TemporaryDirectory(dir=_TMPDIR_REEL) as tmp:
            with patch.dict(
                os.environ, {"HOME": tmp, "XDG_CACHE_HOME": os.path.join(tmp, "c")}, clear=True
            ):
                base_dir = claude_code._claude_code_work_base()
            self.assertEqual(base_dir, os.path.join(tmp, "c", "aipmt", "claude-code"))
            self.assertEqual(os.stat(base_dir).st_mode & 0o777, 0o700)

    def test_a_relative_xdg_cache_home_is_ignored(self):
        with tempfile.TemporaryDirectory(dir=_TMPDIR_REEL) as tmp:
            with patch.dict(os.environ, {"HOME": tmp, "XDG_CACHE_HOME": "relatif"}, clear=True):
                base_dir = claude_code._claude_code_work_base()
            self.assertEqual(base_dir, os.path.join(tmp, ".cache", "aipmt", "claude-code"))


# --- Invocation -------------------------------------------------------------------


class TestClaudeCodeInvocation(unittest.TestCase):
    def test_argv_is_the_measured_contract_and_never_carries_the_segment(self):
        argv = claude_code._claude_code_argv(_client(), _args(model="opus"), "/p/prompt.txt")
        self.assertEqual(argv[:2], [_BINAIRE, "-p"])
        for flag in (
            "--safe-mode",
            "--restricted",
            "--strict-mcp-config",
            "--disable-slash-commands",
            "--no-session-persistence",
            "--include-hook-events",
            "--no-chrome",
        ):
            self.assertIn(flag, argv)
        self.assertEqual(argv[argv.index("--tools") + 1], "")
        self.assertEqual(argv[argv.index("--max-turns") + 1], "1")
        self.assertEqual(argv[argv.index("--permission-prompts") + 1], "none")
        self.assertEqual(argv[argv.index("--output-format") + 1], "stream-json")
        self.assertEqual(argv[argv.index("--system-prompt-file") + 1], "/p/prompt.txt")
        self.assertEqual(argv[argv.index("--model") + 1], "opus")
        self.assertEqual(argv[argv.index("--effort") + 1], "medium")
        settings = json.loads(argv[argv.index("--settings") + 1])
        self.assertEqual(
            settings, {"disableAllHooks": True, "crossSessionInbound": "refuse", "fastMode": False}
        )
        self.assertNotIn("--fallback-model", argv)
        self.assertNotIn("--dangerously-skip-permissions", argv)

    def test_effort_levels(self):
        cas = {
            (("sonnet", False, None)): "medium",
            (("sonnet", True, None)): "low",
            (("opus", False, "none")): "low",
            (("opus", False, "xhigh")): "xhigh",
            (("haiku", False, "high")): None,
        }
        for (model, eco, effort), attendu in cas.items():
            with self.subTest(model=model, eco=eco, effort=effort):
                self.assertEqual(
                    claude_code._claude_code_effort(
                        _args(model=model, eco=eco, reasoning_effort=effort)
                    ),
                    attendu,
                )

    def test_haiku_argv_has_no_effort(self):
        argv = claude_code._claude_code_argv(_client(), _args(model="haiku"), "/p")
        self.assertNotIn("--effort", argv)

    def test_stdin_is_prefixed_by_a_newline(self):
        """Mesuré : sans lui, `/usage` en tête de segment n'atteint pas le modèle."""
        self.assertEqual(
            claude_code._claude_code_stdin("/etc/hosts contient"), "\n/etc/hosts contient"
        )

    def test_edges_come_from_the_segment(self):
        cas = {
            ("Le chat.\n", "The cat."): "The cat.\n",
            ("Le chat.", "The cat.\n"): "The cat.",
            ("\n\nLe chat.\n\n", "\nThe cat.\n"): "\n\nThe cat.\n\n",
            ("| a |", "| b |\n"): "| b |",
        }
        for (segment, text), attendu in cas.items():
            with self.subTest(segment=segment):
                self.assertEqual(claude_code._claude_code_restore_edges(segment, text), attendu)


# --- Lecture du flux --------------------------------------------------------------


class TestClaudeCodeEvents(unittest.TestCase):
    def test_json_lines_blank_lines_and_unreadable_lines(self):
        events = claude_code._claude_code_events('{"type": "a"}\n\n pas du json\n[1, 2]\n')
        self.assertEqual(events[0], {"type": "a"})
        self.assertIn("_texte", events[1])
        self.assertIn("_texte", events[2])
        self.assertEqual(len(events), 3)

    def test_first_by_type_and_subtype(self):
        events = [{"type": "system", "subtype": "x"}, {"type": "system", "subtype": "init", "n": 1}]
        self.assertEqual(claude_code._claude_code_first(events, "system", "init")["n"], 1)
        self.assertIsNone(claude_code._claude_code_first(events, "result"))

    def test_error_text_prefers_result_then_errors_then_assistant_then_stderr(self):
        events = [{"type": "assistant", "error": "authentication_failed"}]
        texte = claude_code._claude_code_error_text(
            {"result": "Not logged in", "errors": ["e1"]}, events, "stderr"
        )
        self.assertEqual(texte, "Not logged in | e1 | authentication_failed")
        self.assertIn("rien", claude_code._claude_code_error_text(None, [], "ligne 1\nrien"))


class TestClaudeCodeFailureClassification(unittest.TestCase):
    def test_login_is_not_retried_and_names_the_login(self):
        err = claude_code._claude_code_failure("Not logged in · Please run /login", "sonnet")
        self.assertFalse(err.rate_limited)
        self.assertIn("/login", str(err))

    def test_a_reached_limit_is_never_retried(self):
        err = claude_code._claude_code_failure(
            "You've hit your weekly limit · resets Wed 6pm", "opus"
        )
        self.assertFalse(err.rate_limited)
        self.assertIn("Aucune relance", str(err))

    def test_throttles_and_the_refresh_lock_are_retried(self):
        for texte in (
            "API Error: Repeated 529 Overloaded errors",
            "rate_limit",
            "Could not refresh your login because another Claude Code process is refreshing it",
        ):
            with self.subTest(texte=texte):
                self.assertTrue(claude_code._claude_code_failure(texte, "sonnet").rate_limited)

    def test_anything_else_is_a_plain_failure(self):
        self.assertFalse(claude_code._claude_code_failure("boom", "sonnet").rate_limited)


# --- Contrat de sortie ------------------------------------------------------------


class TestClaudeCodeOutputContract(unittest.TestCase):
    def _check(self, stdout, returncode=0, stderr="", client=None, args=None):
        return claude_code._claude_code_check_output(
            returncode, stdout, stderr, client or _client(), args or _args()
        )

    def test_the_measured_success_stream_passes(self):
        self.assertEqual(self._check(_flux_ok()), "The cat is sleeping on the rug.")

    def test_windows_are_recorded(self):
        client = _client()
        self._check(_flux_ok(), client=client)
        self.assertEqual(client.windows, {"five_hour": (0.1, 111), "seven_day": (0.5, 222)})

    def test_non_zero_exit_missing_result_or_is_error_fail(self):
        for stdout, rc in (
            (_flux_ok(), 1),
            (_flux(_init(), _rate()), 0),
            (_flux(_init(), _result(is_error=True, result="Not logged in · Please run /login")), 0),
        ):
            with self.subTest(rc=rc), self.assertRaises(claude_code._ClaudeCodeCallError):
                self._check(stdout, returncode=rc)

    def test_init_missing_is_refused(self):
        stdout = _flux(_result())
        with self.assertRaisesRegex(claude_code._ClaudeCodeCallError, "initialisation absent"):
            self._check(stdout)

    def test_every_init_attestation_is_enforced(self):
        cas = {
            "apiKeySource": {"apiKeySource": "ANTHROPIC_API_KEY"},  # pragma: allowlist secret
            "apiKeySource absent": {"apiKeySource": None},
            "modèle annoncé": {"model": "claude-haiku-4-5"},
            "[1m]": {"model": "claude-sonnet-5[1m]"},
            "fast_mode_state": {"fast_mode_state": "on"},
            "analytics_disabled": {"analytics_disabled": False},
            "version": {"claude_code_version": "2.1.284"},
            "tools": {"tools": ["Bash"]},
            "mcp_servers": {"mcp_servers": [{"name": "x"}]},
            "skills": {"skills": ["s"]},
            "slash_commands": {"slash_commands": ["/x"]},
            "plugin": {"plugins": [{"name": "p", "path": "/home/x/.claude/plugins/p"}]},
            "plugins illisibles": {"plugins": "?"},
            "mémoire": {"memory_paths": ["/home/x/.claude/CLAUDE.md"]},
        }
        for nom, override in cas.items():
            init = _init(**override)
            if override.get("model", "").startswith("claude-haiku") or "[1m]" in override.get(
                "model", ""
            ):
                usage = {init["model"]: {}}
            else:
                usage = {_MODELE_SONNET: {}}
            stdout = _flux(init, _rate(), _result(modelUsage=usage))
            with self.subTest(nom=nom), self.assertRaises(claude_code._ClaudeCodeCallError):
                self._check(stdout)

    def test_a_missing_empty_list_counts_as_a_leak(self):
        init = _init()
        del init["tools"]
        self.assertIn("tools non vide", claude_code._claude_code_init_leaks(init))

    def test_every_result_attestation_is_enforced(self):
        cas = {
            "subtype": {"subtype": "error_max_turns"},
            "synthétique (zéro tour)": {"num_turns": 0, "modelUsage": {}},
            "tronqué": {"stop_reason": "max_tokens"},
            "refus d'outil": {"permission_denials": [{"tool_name": "Bash"}]},
            "repli de modèle": {"modelUsage": {_MODELE_SONNET: {}, "claude-opus-4-8": {}}},
            "texte vide": {"result": "  "},
            "texte absent": {"result": None},
        }
        for nom, override in cas.items():
            stdout = _flux(_init(), _rate(), _result(**override))
            with self.subTest(nom=nom), self.assertRaises(claude_code._ClaudeCodeCallError):
                self._check(stdout)

    def test_a_hook_event_or_an_unreadable_line_is_refused(self):
        for extra in ({"type": "hook_started", "hook_name": "SessionStart"}, None):
            flux = _flux(_init(), extra or {}, _result())
            if extra is None:
                flux = _flux(_init(), _result()) + "pas du json\n"
            with self.subTest(extra=extra), self.assertRaises(claude_code._ClaudeCodeCallError):
                self._check(flux)


class TestClaudeCodeQuota(unittest.TestCase):
    def test_extra_usage_stops_without_retry(self):
        for info in (
            {"isUsingOverage": True},
            {"overageInUse": True},
            {"rateLimitType": "overage"},
            {"rateLimitType": "seven_day_overage_included"},
            {"status": "rejected"},
        ):
            with self.subTest(info=info):
                event, client = _rate(**info), _client()
                with self.assertRaises(claude_code._ClaudeCodeCallError) as cm:
                    claude_code._claude_code_rate_limit(event, client, "opus")
                self.assertFalse(cm.exception.rate_limited)

    def test_windows_without_a_number_are_ignored(self):
        client = _client()
        event = _rate(unifiedWindows={"five_hour": {"utilization": "?"}, "seven_day": "x"})
        claude_code._claude_code_rate_limit(event, client, "opus")
        self.assertEqual(client.windows, {})

    def test_a_window_above_the_ceiling_blocks_the_next_segment(self):
        client = _client(windows={"seven_day": (0.99, 1790784000)})
        with self.assertRaisesRegex(claude_code._ClaudeCodeCallError, "seven_day"):
            claude_code._claude_code_check_quota(client, "opus")

    def test_below_the_ceiling_passes(self):
        claude_code._claude_code_check_quota(_client(windows={"five_hour": (0.2, 1)}), "opus")


# --- Appel ------------------------------------------------------------------------


class TestClaudeCodeAttempt(_CcTestCase):
    def test_blank_segment_is_refused_before_any_launch(self):
        client, args = _client(), _args()
        with (
            patch.object(claude_code, "_codex_run_process", side_effect=_NE_DOIT_PAS_SERVIR),
            self.assertRaisesRegex(claude_code._ClaudeCodeCallError, "Segment vide"),
        ):
            claude_code._claude_code_attempt(client, args, "P", " \n ")

    def test_quota_is_checked_before_any_launch(self):
        client, args = _client(windows={"seven_day": (0.95, 1)}), _args()
        with (
            patch.object(claude_code, "_codex_run_process", side_effect=_NE_DOIT_PAS_SERVIR),
            self.assertRaises(claude_code._ClaudeCodeCallError),
        ):
            claude_code._claude_code_attempt(client, args, "P", "Le chat.\n")

    def test_one_call_in_a_private_directory_then_erased(self):
        vus = {}

        def faux(argv, stdin, timeout, env, label, model, cwd=None):
            vus.update(argv=argv, stdin=stdin, env=env, cwd=cwd, label=label, model=model)
            prompt_path = argv[argv.index("--system-prompt-file") + 1]
            with open(prompt_path, encoding="utf-8") as f:
                vus["prompt"] = f.read()
            vus["mode"] = os.stat(cwd).st_mode & 0o777
            return 0, _flux_ok(result="The cat.\n"), ""

        with patch.object(claude_code, "_codex_run_process", side_effect=faux):
            texte = claude_code._claude_code_attempt(_client(), _args(), "SYSTEME", "Le chat.\n")
        self.assertEqual(texte, "The cat.\n")
        self.assertEqual(vus["stdin"], "\nLe chat.\n")
        self.assertEqual(vus["label"], "Claude Code")
        self.assertTrue(vus["prompt"].startswith("SYSTEME"))
        self.assertIn(claude_code.CLAUDE_CODE_AGENT_CONTRACT, vus["prompt"])
        self.assertEqual(vus["mode"], 0o700)
        self.assertFalse(os.path.exists(vus["cwd"]))
        self.assertEqual(vus["env"]["CLAUDE_CODE_DISABLE_ATTACHMENTS"], "1")
        self.assertNotIn("AIPMT_CLAUDE_BIN", vus["env"])

    def test_call_retries_a_throttle_then_succeeds(self):
        reponses = [(1, "", "API Error: Repeated 529 Overloaded errors"), (0, _flux_ok(), "")]
        with (
            patch.object(
                claude_code, "_codex_run_process", side_effect=lambda *a, **k: reponses.pop(0)
            ),
            patch.object(base.time, "sleep") as dort,
        ):
            texte = claude_code._call_claude_code(_client(), _args(), "P", "Le chat.")
        self.assertEqual(texte, "The cat is sleeping on the rug.")
        dort.assert_called_once_with(65.0)


# --- Préflight --------------------------------------------------------------------


def _completed(stdout="", returncode=0, stderr=""):
    """Résultat de `run` : seuls returncode, stdout et stderr sont lus."""
    return SimpleNamespace(returncode=returncode, stdout=stdout, stderr=stderr)


_AUTH_OK = {
    "loggedIn": True,
    "authMethod": "claude.ai",
    "apiProvider": "firstParty",
    "analyticsDisabled": True,
    "subscriptionType": "max",
    "email": "ne-doit-pas-sortir@example.com",
    "orgName": "org",
}


class TestClaudeCodeRunCheck(_CcTestCase):
    def test_same_environment_private_directory_own_session(self):
        with patch.object(claude_code.subprocess, "run", return_value=_completed("ok")) as run:
            claude_code._claude_code_run_check(_BINAIRE, ["--version"], timeout=30)
        (argv,), kwargs = run.call_args
        self.assertEqual(argv, [_BINAIRE, "--version"])
        self.assertTrue(kwargs["start_new_session"])
        self.assertEqual(kwargs["stdin"], subprocess.DEVNULL)
        self.assertEqual(kwargs["env"], claude_code._claude_code_env())
        self.assertFalse(os.path.exists(kwargs["cwd"]))

    def test_launch_failure_becomes_a_value_error(self):
        with (
            patch.object(claude_code.subprocess, "run", side_effect=OSError("introuvable")),
            self.assertRaisesRegex(ValueError, "Impossible d'exécuter"),
        ):
            claude_code._claude_code_run_check(_BINAIRE, ["--version"])


class TestClaudeCodePreflight(_CcTestCase):
    def _run(self, reponses):
        """Double de run qui rend, dans l'ordre, les réponses données."""
        return patch.object(claude_code.subprocess, "run", side_effect=list(reponses))

    def _auth(self, **overrides):
        status = dict(_AUTH_OK, configDirectory=os.path.join(self.home, ".claude"))
        status.update(overrides)
        return _completed(json.dumps({k: v for k, v in status.items() if v is not _SUPPRIME}))

    def test_version_parsing_and_floor(self):
        with self._run([_completed("2.1.283 (Claude Code)")]):
            self.assertEqual(claude_code._claude_code_check_version(_BINAIRE), "2.1.283")
        with (
            self._run([_completed("2.1.200 (Claude Code)")]),
            self.assertRaisesRegex(ValueError, "trop ancien"),
        ):
            claude_code._claude_code_check_version(_BINAIRE)
        with (
            self._run([_completed("", returncode=1, stderr="boom")]),
            self.assertRaisesRegex(ValueError, "a échoué"),
        ):
            claude_code._claude_code_check_version(_BINAIRE)

    def test_auth_status_ok(self):
        with self._run([self._auth()]):
            claude_code._claude_code_check_auth(_BINAIRE)

    def test_auth_status_unreadable_or_logged_out(self):
        with (
            self._run([_completed("pas du json", returncode=1)]),
            self.assertRaisesRegex(ValueError, "impossible"),
        ):
            claude_code._claude_code_check_auth(_BINAIRE)
        with self._run([self._auth(loggedIn=False)]), self.assertRaisesRegex(ValueError, "/login"):
            claude_code._claude_code_check_auth(_BINAIRE)

    def test_every_auth_problem_is_refused_without_showing_the_identity(self):
        cas = {
            "authMethod": {"authMethod": "oauth_token"},
            "apiProvider": {"apiProvider": "bedrock"},
            "analytics": {"analyticsDisabled": False},
            "team": {"subscriptionType": "team"},
            "plan absent": {"subscriptionType": None},
            "clé Console": {"apiKeySource": "/login managed key"},
            "répertoire": {"configDirectory": "/ailleurs"},
        }
        for nom, override in cas.items():
            with self.subTest(nom=nom), self._run([self._auth(**override)]):
                with self.assertRaises(ValueError) as cm:
                    claude_code._claude_code_check_auth(_BINAIRE)
                self.assertNotIn("ne-doit-pas-sortir", str(cm.exception))

    def test_usage_attests_the_subscription_without_a_model_turn(self):
        ok = {
            "num_turns": 0,
            "modelUsage": {},
            "result": "You are currently using your subscription to power it",
        }
        with self._run([_completed(json.dumps(ok))]):
            claude_code._claude_code_check_usage(_BINAIRE)
        for mauvais in (
            "pas du json",
            json.dumps(dict(ok, num_turns=1)),
            json.dumps(dict(ok, modelUsage={"m": {}})),
            json.dumps(dict(ok, result="You are using an API key")),
        ):
            with (
                self.subTest(mauvais=mauvais[:30]),
                self._run([_completed(mauvais)]),
                self.assertRaisesRegex(ValueError, "/usage"),
            ):
                claude_code._claude_code_check_usage(_BINAIRE)

    def test_preflight_order_and_refusals(self):
        with self.assertRaisesRegex(ValueError, "introuvable"):
            claude_code._claude_code_preflight(None)
        gere = lambda chemin: chemin.startswith("/etc/claude-code")  # noqa: E731
        with (
            patch.object(claude_code.os.path, "exists", side_effect=gere),
            patch.object(claude_code.subprocess, "run", side_effect=_NE_DOIT_PAS_SERVIR),
            self.assertRaisesRegex(ValueError, "Réglages gérés"),
        ):
            claude_code._claude_code_preflight(_BINAIRE)
        usage = {"num_turns": 0, "modelUsage": {}, "result": "using your subscription"}
        reponses = [
            _completed("2.1.283 (Claude Code)"),
            self._auth(),
            _completed(json.dumps(usage)),
        ]
        with patch.object(claude_code.os.path, "exists", return_value=False), self._run(reponses):
            self.assertEqual(claude_code._claude_code_preflight(_BINAIRE), "2.1.283")


_SUPPRIME = object()


class TestClaudeCodeBinaryResolution(_CcTestCase):
    def test_explicit_binary_missing_is_none(self):
        self.assertIsNone(claude_code._resolve_claude_code_binary())

    def test_explicit_binary_as_a_real_file_is_resolved(self):
        chemin = os.path.join(self.home, "claude")
        with open(chemin, "w") as f:
            f.write("")
        with patch.dict(os.environ, {"AIPMT_CLAUDE_BIN": chemin}):
            self.assertEqual(claude_code._resolve_claude_code_binary(), os.path.realpath(chemin))

    def test_path_then_local_bin(self):
        with patch.dict(os.environ, {"AIPMT_CLAUDE_BIN": ""}):
            self.assertIsNone(claude_code._resolve_claude_code_binary())
            local = os.path.join(self.home, ".local", "bin")
            os.makedirs(local)
            cible = os.path.join(self.home, "versions", "2.1.283")
            os.makedirs(os.path.dirname(cible))
            with open(cible, "w") as f:
                f.write("")
            os.symlink(cible, os.path.join(local, "claude"))
            self.assertEqual(claude_code._resolve_claude_code_binary(), os.path.realpath(cible))


# --- Initialisation -----------------------------------------------------------------


class TestClaudeCodeInit(_CcTestCase):
    def test_default_and_eco_models(self):
        with patch.object(claude_code, "_claude_code_preflight", return_value=_VERSION):
            args = _args(model=None)
            client = claude_code._init_claude_code_client(args)
            self.assertEqual(args.model, claude_code.DEFAULT_MODEL_CLAUDE_CODE)
            self.assertEqual(client.version, _VERSION)
            eco = _args(model=None, eco=True)
            claude_code._init_claude_code_client(eco)
            self.assertEqual(eco.model, claude_code.ECO_MODEL_CLAUDE_CODE)

    def test_refused_in_ci_before_any_launch(self):
        args = _args()
        with (
            patch.dict(os.environ, {"CI": "true"}),
            patch.object(claude_code, "_claude_code_preflight", side_effect=_NE_DOIT_PAS_SERVIR),
            self.assertRaisesRegex(ValueError, "ANTHROPIC_API_KEY"),
        ):
            claude_code._init_claude_code_client(args)

    def test_refused_on_windows(self):
        args = _args()
        with (
            patch.object(claude_code.os, "name", "nt"),
            patch.object(claude_code, "_claude_code_preflight", side_effect=_NE_DOIT_PAS_SERVIR),
            self.assertRaisesRegex(ValueError, "Windows"),
        ):
            claude_code._init_claude_code_client(args)

    def test_only_the_three_aliases_are_accepted(self):
        for model in ("fable", "best", "sonnet[1m]", "opusplan", "default", "claude-opus-5-5"):
            with self.subTest(model=model), self.assertRaisesRegex(ValueError, "non accepté"):
                claude_code._claude_code_check_model(model)
        for model in ("opus", "sonnet", "haiku"):
            claude_code._claude_code_check_model(model)

    def test_effort_warnings(self):
        for args, attendu in (
            (_args(model="haiku", reasoning_effort="high"), "sans effet"),
            (_args(reasoning_effort="none"), "« none »"),
        ):
            sortie = io.StringIO()
            with self.subTest(attendu=attendu), contextlib.redirect_stderr(sortie):
                claude_code._claude_code_warn_options(args)
            self.assertIn(attendu, sortie.getvalue())


# --- Câblage --------------------------------------------------------------------------


class TestClaudeCodeWiring(unittest.TestCase):
    def test_flag_label_timeout_and_ci_fallback(self):
        self.assertEqual(registry._PROVIDER_LABELS["claude_code"], "Claude Code CLI")
        self.assertIn("claude_code", registry._CLI_PROVIDERS)
        self.assertEqual(base._CLI_TIMEOUT_ENV_VARS["Claude Code"], "AIPMT_CLAUDE_TIMEOUT")
        self.assertEqual(base._CLI_PROVIDER_CI_FALLBACK["--use_claude_code"][2], "--use_claude")

    def test_the_help_contrasts_the_subscription_with_the_billed_api(self):
        aide = dict(registry._PROVIDER_FLAGS)["use_claude_code"]
        self.assertIn("--use_claude", aide)
        self.assertIn("abonnement", aide)

    def test_model_is_never_catalogued(self):
        self.assertTrue(cli._model_is_uncatalogued(Namespace(use_claude_code=True)))
        self.assertFalse(cli._model_is_uncatalogued(Namespace()))

    def test_a_project_env_cannot_choose_the_account_or_the_binary(self):
        for nom in ("CLAUDE_CONFIG_DIR", "NODE_EXTRA_CA_CERTS", "HOME", "AIPMT_CLAUDE_BIN"):
            with self.subTest(nom=nom):
                self.assertTrue(config._is_routing_variable(nom))


class TestRegenClaudeCode(unittest.TestCase):
    """detect_provider seul, dans bash, sans `claude` atteignable."""

    def _detect(self, **env):
        # argv court : la ligne reste sous 100 colonnes (cf. CLAUDE.md, nosemgrep).
        script = f"source {_REGEN} >/dev/null 2>&1; detect_provider"
        vide = {"PATH": "/usr/bin:/bin", "HOME": _TMPDIR_REEL, **env}
        argv = ["bash", "-c", script]
        # nosemgrep
        return subprocess.run(  # nosec B603 B607 # nosemgrep — bash local, script du dépôt
            argv,  # nosemgrep
            capture_output=True,
            text=True,
            env=vide,
            timeout=60,
            check=False,
        )

    def test_claude_code_is_a_subscription_without_derogation(self):
        sortie = self._detect(REGEN_PROVIDER="claude_code")
        self.assertEqual(sortie.returncode, 0, sortie.stderr)
        self.assertEqual(sortie.stdout.strip(), "--use_claude_code")
        self.assertIn("abonnement Claude", sortie.stderr)

    def test_the_unknown_provider_message_lists_it(self):
        sortie = self._detect(REGEN_PROVIDER="inconnu")
        self.assertNotEqual(sortie.returncode, 0)
        self.assertIn("claude_code", sortie.stderr)


if __name__ == "__main__":
    unittest.main()
