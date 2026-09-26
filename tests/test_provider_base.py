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
3. Un SIGHUP — terminal fermé, session SSH coupée — tuait Python de la même
   façon, sans nettoyage : l'agent continuait, et le répertoire privé
   d'Antigravity restait sur le disque, journal compris. Il est traité comme
   SIGTERM et sort en 129, sauf s'il est ignoré (`nohup`), choix de
   l'utilisateur que le pilote respecte.
4. Ctrl-C ou SystemExit pendant l'attente : l'agent, dans sa propre session,
   ne reçoit pas le SIGINT du terminal, et `Popen.__exit__` ne l'attend que
   0,25 s avant de rendre la main. Il survivait, et consommait son quota pour
   un résultat jeté. Le pilote tue le groupe avant de laisser remonter
   l'exception.
"""

from __future__ import annotations

import contextlib
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

# Pid de faux processus au-delà du plus grand pid possible (pid_max vaut
# 4 194 304) : si un doublage de `os.getpgid` sautait un jour, le vrai
# `getpgid` échouerait avant tout `killpg`, au lieu de viser le groupe d'un
# vrai processus — les pid font le tour en quelques heures sur ce poste, et
# 4242 peut exister. Cf. l'incident kill(-1) du 2026-09-26 dans CLAUDE.md.
_PID_INEXISTANT = 2**22 + 4242


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


@contextlib.contextmanager
def _disposition(signum, handler):
    """`handler` sur `signum` le temps du bloc, puis la disposition d'origine
    (SIG_DFL si elle avait été posée hors de Python)."""
    original = signal.signal(signum, handler)
    try:
        yield
    finally:
        signal.signal(signum, signal.SIG_DFL if original is None else original)


# Agent factice des tests de signal réels : un sous-processus Python inoffensif,
# jamais un vrai CLI. Il ignore SIGTERM, lance un petit-fils qui dort et qui en
# hérite — une disposition SIG_IGN traverse fork et exec —, écrit les deux pids
# d'un bloc (`os.replace`), puis attend. Seul le SIGKILL du groupe peut les
# arrêter : c'est précisément ce qu'il faut prouver.
_AGENT_QUI_DORT = """
import os, signal, subprocess, sys
signal.signal(signal.SIGTERM, signal.SIG_IGN)
petit_fils = subprocess.Popen([sys.executable, "-I", "-c", "import time; time.sleep(30)"])
provisoire = sys.argv[1] + ".tmp"
with open(provisoire, "w", encoding="utf-8") as f:
    f.write(f"{os.getpid()} {petit_fils.pid}")
os.replace(provisoire, sys.argv[1])
petit_fils.wait()
"""


def _signal_when_ready(pidfile, signum, stop):
    """Envoie `signum` à CE processus dès que l'agent factice a écrit ses deux
    pids, pas avant : l'agent et son petit-fils démarrent chacun un
    interpréteur, et un délai fixe trop court ferait tomber le signal pendant
    le lancement, avant l'attente qu'on veut éprouver."""
    while not stop.wait(0.02):
        if os.path.exists(pidfile):
            os.kill(os.getpid(), signum)
            return


def _interrupt_a_real_agent(test, signum, expected):
    """Lance l'agent factice par le vrai pilote, lui envoie `signum` pendant
    l'attente, et renvoie (exception remontée, pids, survivants). Délai de
    grâce réduit à 0,5 s ; timeout de 10 s, pour qu'une régression échoue vite
    au lieu d'attendre la fin du sommeil. Un survivant — donc un test rouge —
    est tué ici : il ne doit pas dormir 30 s de plus."""
    with tempfile.TemporaryDirectory() as tmp:
        pidfile = os.path.join(tmp, "pids")
        argv = [sys.executable, "-I", "-c", _AGENT_QUI_DORT, pidfile]
        stop = threading.Event()
        signaleur = threading.Thread(target=_signal_when_ready, args=(pidfile, signum, stop))
        signaleur.start()
        try:
            with (
                patch.object(base, "CODEX_TERM_GRACE", 0.5),
                test.assertRaises(expected) as ctx,
            ):
                base._codex_run_process(argv, "", 10, os.environ.copy(), "Codex", "m")
        finally:
            stop.set()
            signaleur.join()
        pids = [int(x) for x in pathlib.Path(pidfile).read_text(encoding="utf-8").split()]
    survivants = _survivors(pids, 5)
    for pid in survivants:
        with contextlib.suppress(OSError):
            os.kill(pid, signal.SIGKILL)
    return ctx.exception, pids, survivants


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
        """Hors du thread principal, `signal.signal` lèverait ValueError : le
        pilote n'y pose rien, ni pour SIGTERM ni pour SIGHUP. Une exception
        dans le thread laisserait `seen` vide, et le test rouge."""
        signums = [signal.SIGTERM]
        if hasattr(signal, "SIGHUP"):  # absent sous Windows
            signums.append(signal.SIGHUP)
        before = {signum: signal.getsignal(signum) for signum in signums}
        seen = {}

        def worker():
            with base._kill_group_on_sigterm({}):
                seen.update({signum: signal.getsignal(signum) for signum in signums})

        thread = threading.Thread(target=worker)
        thread.start()
        thread.join()
        self.assertEqual(seen, before)


@unittest.skipUnless(hasattr(signal, "SIGHUP"), "SIGHUP n'existe pas sous Windows")
class TestSighupDuringWait(unittest.TestCase):
    def test_sighup_kills_the_agent_group_then_exits_129(self):
        if threading.current_thread() is not threading.main_thread():
            self.skipTest("gestionnaire de signal : thread principal requis")
        # `_ignore` en filet : un SIGHUP tombé hors de la fenêtre surveillée ne
        # doit pas tuer le lanceur de tests. Ce n'est pas SIG_IGN, que le
        # pilote respecterait en ne posant rien.
        with _disposition(signal.SIGHUP, _ignore):
            exc, pids, survivants = _interrupt_a_real_agent(self, signal.SIGHUP, SystemExit)
            # Le gestionnaire précédent est restauré dès la sortie du pilote.
            self.assertIs(signal.getsignal(signal.SIGHUP), _ignore)
        self.assertEqual(exc.code, 128 + signal.SIGHUP)
        self.assertEqual(len(pids), 2)
        self.assertEqual(survivants, [], "agent encore vivant après SIGHUP")


@unittest.skipUnless(hasattr(signal, "SIGHUP"), "SIGHUP n'existe pas sous Windows")
class TestHandlersInstalledForTheWait(unittest.TestCase):
    """Ce que le pilote pose pendant l'attente, et ce qu'il laisse derrière lui."""

    def setUp(self):
        if threading.current_thread() is not threading.main_thread():
            self.skipTest("gestionnaire de signal : thread principal requis")

    def _seen(self, sighup):
        """((SIGTERM, SIGHUP) pendant l'attente, puis après), SIGTERM réglé à
        `_ignore` et SIGHUP à `sighup` avant d'entrer."""
        with _disposition(signal.SIGTERM, _ignore), _disposition(signal.SIGHUP, sighup):
            with base._kill_group_on_sigterm({}):
                pendant = (signal.getsignal(signal.SIGTERM), signal.getsignal(signal.SIGHUP))
            apres = (signal.getsignal(signal.SIGTERM), signal.getsignal(signal.SIGHUP))
        return pendant, apres

    def test_sigterm_and_sighup_share_the_handler_then_are_restored(self):
        (term, hup), apres = self._seen(sighup=_ignore)
        self.assertTrue(callable(term))
        self.assertIsNot(term, _ignore)
        self.assertIs(hup, term)
        self.assertEqual(apres, (_ignore, _ignore))

    def test_an_ignored_sighup_is_left_alone(self):
        """Lancée par `nohup`, la traduction doit survivre à la fermeture du
        terminal : c'est le choix de l'utilisateur, le pilote n'y touche pas.
        SIGTERM reste couvert."""
        (term, hup), apres = self._seen(sighup=signal.SIG_IGN)
        self.assertIsNot(term, _ignore)
        self.assertIs(hup, signal.SIG_IGN)
        self.assertEqual(apres, (_ignore, signal.SIG_IGN))

    def test_a_handler_set_outside_python_is_restored_as_default(self):
        """`signal.signal` rend None quand le gestionnaire en place est inconnu
        de Python — posé par du code C, un hôte qui embarque l'interpréteur.
        Le reposer tel quel lève TypeError (« signal handler must be
        signal.SIG_IGN, signal.SIG_DFL, or a callable object »), dans le
        `finally`, par-dessus l'exception en cours : le pilote remet SIG_DFL.
        Ce None ne se fabrique pas en Python pur, d'où la doublure de
        `signal.signal`, dont les appels sont relevés sans rien poser."""
        poses = []

        def faux_signal(signum, handler):
            poses.append((signum, handler))
            return None if signum == signal.SIGHUP else _ignore

        with (
            _disposition(signal.SIGHUP, _ignore),
            patch.object(base.signal, "signal", side_effect=faux_signal),
            base._kill_group_on_sigterm({}),
        ):
            pass
        self.assertEqual(len(poses), 4, poses)
        self.assertEqual(poses[2:], [(signal.SIGTERM, _ignore), (signal.SIGHUP, signal.SIG_DFL)])


class TestInterruptDuringWait(unittest.TestCase):
    """Ctrl-C ou SystemExit pendant l'attente : le groupe est tué — SIGTERM,
    délai de grâce, SIGKILL, comme au timeout — puis l'exception remonte telle
    quelle, sans être convertie."""

    def _interrupted(self, exc):
        """(exception remontée, appels à `killpg`) quand `exc` tombe pendant
        `communicate`. Popen et killpg sont doublés : rien n'est lancé."""
        proc = MagicMock(pid=_PID_INEXISTANT)
        proc.communicate.side_effect = exc
        proc.wait.return_value = 0
        popen = MagicMock()
        popen.return_value.__enter__.return_value = proc
        with (
            patch.object(base.subprocess, "Popen", popen),
            patch("os.getpgid", return_value=_PID_INEXISTANT),
            patch("os.killpg") as killpg,
            self.assertRaises(type(exc)) as ctx,
        ):
            base._codex_run_process(["cli"], "S", 5, {}, "Codex", "m")
        return ctx.exception, [c.args for c in killpg.call_args_list]

    def test_keyboard_interrupt_kills_the_group_then_propagates(self):
        interruption = KeyboardInterrupt()
        remontee, killpg = self._interrupted(interruption)
        self.assertIs(remontee, interruption)
        self.assertEqual(
            killpg, [(_PID_INEXISTANT, signal.SIGTERM), (_PID_INEXISTANT, signal.SIGKILL)]
        )

    def test_system_exit_kills_the_group_then_propagates(self):
        sortie = SystemExit(3)
        remontee, killpg = self._interrupted(sortie)
        self.assertIs(remontee, sortie)
        self.assertEqual(remontee.code, 3)
        self.assertEqual(
            killpg, [(_PID_INEXISTANT, signal.SIGTERM), (_PID_INEXISTANT, signal.SIGKILL)]
        )

    @unittest.skipUnless(os.name == "posix", "groupes de processus : POSIX seulement")
    def test_ctrl_c_leaves_no_agent_behind(self):
        """Le même Ctrl-C sur un vrai sous-processus. Le SIGINT n'est envoyé
        qu'à ce processus, comme le terminal l'envoie à son groupe de premier
        plan, dont l'agent n'est pas. `default_int_handler` est posé le temps
        du test : c'est celui de Python par défaut, et un lanceur `--catch` en
        pose un autre, qui ne lèverait pas KeyboardInterrupt."""
        if threading.current_thread() is not threading.main_thread():
            self.skipTest("gestionnaire de signal : thread principal requis")
        with _disposition(signal.SIGINT, signal.default_int_handler):
            exc, pids, survivants = _interrupt_a_real_agent(self, signal.SIGINT, KeyboardInterrupt)
        self.assertIsInstance(exc, KeyboardInterrupt)
        self.assertEqual(len(pids), 2)
        self.assertEqual(survivants, [], "agent encore vivant après Ctrl-C")


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
        proc = MagicMock(pid=_PID_INEXISTANT)
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
        proc = MagicMock(pid=_PID_INEXISTANT)
        proc.wait.return_value = 0
        with patch.object(base, "os", self._os_sans_groupes()):
            base._codex_kill_group(proc)
        proc.terminate.assert_called_once()
        proc.kill.assert_not_called()


class TestWorkingDirectory(unittest.TestCase):
    """agy n'a aucune option de répertoire de travail : il prend le sien pour
    racine d'espace de travail, et c'est là qu'il cherche l'agent de
    traduction. Sans `cwd`, il le chercherait dans le répertoire courant de
    l'utilisateur et retomberait sur son agent de codage (mesuré sur un agent
    introuvable : rc 0, status SUCCESS, 57 outils) — la garde du journal
    refuserait alors chaque segment. Codex, Grok et OpenCode fixent le leur
    par une option (`--cd`, `--cwd`, `--dir`) et n'en passent pas : pour eux,
    rien ne doit changer."""

    def _popen_kwargs(self, **extra):
        """Les arguments nommés reçus par `Popen`, qui ne lance rien ici."""
        proc = MagicMock(returncode=0)
        proc.communicate.return_value = ("sortie", "")
        popen = MagicMock()
        popen.return_value.__enter__.return_value = proc
        with patch.object(base.subprocess, "Popen", popen):
            result = base._codex_run_process(["cli"], "S", 5, {}, "Antigravity", "m", **extra)
        popen.assert_called_once()
        proc.communicate.assert_called_once_with(input="S", timeout=5)
        self.assertEqual(result, (0, "sortie", ""))
        return popen.call_args.kwargs

    def test_cwd_reaches_popen(self):
        kwargs = self._popen_kwargs(cwd="/chemin/factice/work")
        self.assertEqual(kwargs["cwd"], "/chemin/factice/work")

    def test_cwd_defaults_to_none(self):
        self.assertIsNone(self._popen_kwargs()["cwd"])


class TestKillGroupNeverTargetsTheWholeSession(unittest.TestCase):
    """Sous Linux, killpg(1, sig) vaut kill(-1, sig) : le signal part vers TOUS
    les processus de l'utilisateur. Le 2026-09-26, un test passait un faux
    processus au pid MagicMock — que Python convertit en 1 par `__index__` —
    sans doubler `os.killpg`, et a tué la session graphique entière. Le pilote
    refuse désormais de viser le groupe 1 ou son propre groupe, et ne tue alors
    que le fils direct. `os.killpg` est TOUJOURS doublé ici : ces tests ne
    doivent jamais pouvoir envoyer un vrai signal de groupe."""

    def _kill(self, proc, getpgid=None):
        """(appels à killpg, proc) pour `_codex_kill_group(proc)`, killpg doublé.
        `getpgid=None` laisse le vrai `os.getpgid` répondre."""
        with contextlib.ExitStack() as pile:
            killpg = pile.enter_context(patch("os.killpg"))
            if getpgid is not None:
                pile.enter_context(patch("os.getpgid", return_value=getpgid))
            base._codex_kill_group(proc)
        return [c.args for c in killpg.call_args_list], proc

    def test_a_magicmock_pid_reads_as_1_and_is_never_signalled(self):
        # Sans doublure de getpgid : MagicMock.__index__ vaut 1, et le vrai
        # os.getpgid(1) rend 1 — exactement le chemin de l'incident.
        appels, proc = self._kill(MagicMock())
        self.assertEqual(appels, [])
        proc.terminate.assert_called_once()

    def test_group_1_or_below_is_never_signalled(self):
        for pgid in (1, 0, -1):
            with self.subTest(pgid=pgid):
                appels, proc = self._kill(MagicMock(pid=_PID_INEXISTANT), getpgid=pgid)
                self.assertEqual(appels, [])
                proc.terminate.assert_called_once()

    def test_our_own_group_is_never_signalled(self):
        appels, proc = self._kill(MagicMock(pid=_PID_INEXISTANT), getpgid=os.getpgrp())
        self.assertEqual(appels, [])
        proc.terminate.assert_called_once()

    def test_a_pid_that_is_not_a_strict_int_above_1_is_never_signalled(self):
        """`type(pid) is int` et non `isinstance` : True est un int pour
        isinstance, et vaut 1. Un pid de chaîne ou de flottant n'est pas non
        plus un pid ; `getpgid` rendrait le même pid pour qu'aucun autre
        garde-fou ne prenne le relais."""
        for pid in (True, 1, 0, -1, "4243", 4243.0):
            with self.subTest(pid=pid):
                appels, proc = self._kill(MagicMock(pid=pid), getpgid=pid)
                self.assertEqual(appels, [])
                proc.terminate.assert_called_once()

    def test_a_group_other_than_the_agent_pid_is_never_signalled(self):
        """Lancé avec start_new_session, l'agent est chef de son groupe : un
        getpgid qui rend autre chose que son pid désigne le groupe d'un autre."""
        appels, proc = self._kill(MagicMock(pid=_PID_INEXISTANT), getpgid=_PID_INEXISTANT + 1)
        self.assertEqual(appels, [])
        proc.terminate.assert_called_once()

    def test_the_agent_group_is_still_signalled(self):
        appels, _proc = self._kill(MagicMock(pid=_PID_INEXISTANT), getpgid=_PID_INEXISTANT)
        self.assertEqual(
            appels, [(_PID_INEXISTANT, signal.SIGTERM), (_PID_INEXISTANT, signal.SIGKILL)]
        )


class TestKillGroup(unittest.TestCase):
    def test_sigkill_always_follows_sigterm(self):
        proc = MagicMock(pid=_PID_INEXISTANT)
        proc.wait.return_value = 0  # le fils direct meurt proprement sur SIGTERM
        with patch("os.getpgid", return_value=_PID_INEXISTANT), patch("os.killpg") as killpg:
            base._codex_kill_group(proc)
        self.assertEqual(
            [c.args for c in killpg.call_args_list],
            [(_PID_INEXISTANT, signal.SIGTERM), (_PID_INEXISTANT, signal.SIGKILL)],
        )

    def test_a_group_already_dead_is_not_an_error(self):
        proc = MagicMock(pid=_PID_INEXISTANT)
        proc.wait.return_value = 0
        with (
            patch("os.getpgid", return_value=_PID_INEXISTANT),
            patch("os.killpg", side_effect=ProcessLookupError),
        ):
            base._codex_kill_group(proc)  # ne lève pas


if __name__ == "__main__":
    unittest.main()
