"""Socle des CLI agentiques (`aipmt.providers.base`) : ce que la revue a mesuré.

1. Un SIGTERM reçu par ce processus pendant l'attente d'un CLI — le `timeout`
   de `regen_translations.sh`, un arrêt de conteneur — tuait Python sans
   exécuter aucune clause `except` ; l'agent, placé dans sa propre session par
   `start_new_session`, survivait et consommait son quota jusqu'au bout. Le
   pilote pose un gestionnaire qui tue le groupe avant de terminer avec le
   code conventionnel 143.
2. Le SIGKILL du groupe n'était envoyé que si le fils direct survivait au délai
   de grâce : un shim qui meurt proprement sur SIGTERM laissait vivre le
   petit-fils. Il est désormais systématique.
"""

from __future__ import annotations

import os
import pathlib
import signal
import subprocess  # nosec B404 — types d'exception seulement, aucun lancement
import sys
import tempfile
import threading
import time
import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from aipmt.providers import base


def _alive(pid):
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def _survivors(pids, seconds):
    """Les pids encore vivants après `seconds` au plus."""
    deadline = time.monotonic() + seconds
    alive = [pid for pid in pids if _alive(pid)]
    while alive and time.monotonic() < deadline:
        time.sleep(0.05)
        alive = [pid for pid in pids if _alive(pid)]
    return alive


def _ignore(*_):
    """Gestionnaire neutre : si le SIGTERM du test arrivait hors de la fenêtre
    surveillée, il ne doit pas tuer le lanceur de tests."""


class TestSigtermDuringWait(unittest.TestCase):
    def test_sigterm_kills_the_agent_group_then_exits_143(self):
        if threading.current_thread() is not threading.main_thread():
            self.skipTest("gestionnaire de signal : thread principal requis")
        original = signal.signal(signal.SIGTERM, _ignore)
        with tempfile.TemporaryDirectory() as tmp:
            pidfile = os.path.join(tmp, "pids")
            # L'agent ET son petit-fils ignorent SIGTERM : seul le SIGKILL du
            # groupe peut les arrêter — c'est précisément ce qu'on veut prouver.
            argv = ["sh", "-c", f'trap "" TERM; sleep 30 & echo $$ $! > {pidfile}; wait']
            timer = threading.Timer(0.8, os.kill, args=(os.getpid(), signal.SIGTERM))
            env = os.environ.copy()
            try:
                timer.start()
                with (
                    patch.object(base, "CODEX_TERM_GRACE", 0.5),
                    self.assertRaises(SystemExit) as ctx,
                ):
                    base._codex_run_process(argv, "", 30, env, "Codex", "m")
                # Le gestionnaire précédent est restauré dès la sortie du pilote.
                self.assertIs(signal.getsignal(signal.SIGTERM), _ignore)
            finally:
                timer.cancel()
                signal.signal(signal.SIGTERM, original)
            self.assertEqual(ctx.exception.code, 128 + signal.SIGTERM)
            pids = [int(x) for x in pathlib.Path(pidfile).read_text(encoding="utf-8").split()]
        self.assertEqual(len(pids), 2)
        self.assertEqual(_survivors(pids, 5), [], "agent encore vivant")

    def test_no_handler_is_installed_outside_the_main_thread(self):
        before = signal.getsignal(signal.SIGTERM)
        seen = {}

        def worker():
            with base._kill_group_on_sigterm({}):
                seen["inside"] = signal.getsignal(signal.SIGTERM)

        thread = threading.Thread(target=worker)
        thread.start()
        thread.join()
        self.assertIs(seen["inside"], before)


class TestPlatformWithoutProcessGroups(unittest.TestCase):
    """`os.killpg` n'existe pas sur Windows et `start_new_session` y est ignoré :
    sans garde, l'AttributeError traversait le `except TimeoutExpired` et le
    `with Popen` attendait ensuite un processus que personne n'avait tué, alors
    que le paquet se déclare « OS Independent »."""

    @staticmethod
    def _os_sans_groupes():
        """Le module `os` tel que le voit `base` sur une plateforme sans
        groupes de processus : `killpg` n'y existe pas."""
        return SimpleNamespace()

    def test_the_direct_child_is_still_killed(self):
        proc = MagicMock(pid=4242)
        # Le délai de grâce expire, puis `wait()` sans délai rend la main après
        # le kill — un `wait()` sans timeout bloque, il n'expire jamais.
        # TimeoutExpired est une classe d'exception construite pour une
        # doublure, pas un lancement de process.
        # nosemgrep
        expiration = subprocess.TimeoutExpired(cmd="doublure", timeout=1)  # nosemgrep
        proc.wait.side_effect = [expiration, 0]
        with patch.object(base, "os", self._os_sans_groupes()):
            base._codex_kill_group(proc)
        proc.terminate.assert_called_once()
        proc.kill.assert_called_once()

    def test_a_child_that_stops_on_terminate_is_not_killed(self):
        proc = MagicMock(pid=4242)
        proc.wait.return_value = 0
        with patch.object(base, "os", self._os_sans_groupes()):
            base._codex_kill_group(proc)
        proc.terminate.assert_called_once()
        proc.kill.assert_not_called()


class TestKillGroup(unittest.TestCase):
    def test_sigkill_always_follows_sigterm(self):
        proc = MagicMock(pid=4242)
        proc.wait.return_value = 0  # le fils direct meurt proprement sur SIGTERM
        with patch("os.getpgid", return_value=4242), patch("os.killpg") as killpg:
            base._codex_kill_group(proc)
        self.assertEqual(
            [c.args for c in killpg.call_args_list],
            [(4242, signal.SIGTERM), (4242, signal.SIGKILL)],
        )

    def test_a_group_already_dead_is_not_an_error(self):
        proc = MagicMock(pid=4242)
        proc.wait.return_value = 0
        with (
            patch("os.getpgid", return_value=4242),
            patch("os.killpg", side_effect=ProcessLookupError),
        ):
            base._codex_kill_group(proc)  # ne lève pas


if __name__ == "__main__":
    unittest.main()
