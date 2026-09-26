"""Couverture du provider Antigravity (CLI `agy` de Google, quota d'abonnement).

Les tests ne lancent JAMAIS le vrai binaire — installé sur le poste du
propriétaire, il consommerait le quota de l'abonnement. `subprocess.Popen` et
`subprocess.run` sont remplacés par des doubles dont chaque test vérifie qu'ils
ont servi, et le binaire des clients est un chemin inexistant : un patch qui ne
mordrait pas ferait échouer le lancement au lieu d'exécuter `agy`. Les seuls
sous-processus réels de la suite (bash pour `regen_translations.sh`,
l'interpréteur courant, et un faux `agy` en /bin/sh que le test écrit dans un
répertoire jetable) tournent sans le vrai `agy` atteignable.

Ils verrouillent ce qui a été mesuré sur agy 1.2.11 le 2026-09-26 :

- un agent introuvable ne fait PAS échouer `agy` : rc 0, status SUCCESS, et
  l'agent de codage (57 outils) répond à la place du traducteur, sans une trace
  sur stdout ni stderr — seul le journal (--log-file) le dit, et ses marqueurs
  ne valent que sur une ligne glog entière, qu'un document cité ne forme pas ;
- avec `-p`, agy ignore stdin ; sans lui, stdin n'étant pas un terminal, il lit
  le segment jusqu'à EOF — et un stdin vide ouvre l'interface interactive ;
- agy termine chaque réponse par un saut de ligne, que le segment en ait un ou
  non : la traduction rendue reprend la fin de ligne du segment ;
- la voie de facturation se lit dans le journal (`authMethod=consumer`) et dans
  `/config` (useG1Credits, modelProvider, gcp), jamais dans le code retour ;
- AGY_GATEWAY_URL, AGY_ADC_AUTH ou CLOUD_CODE_URL détournent l'appel vers une
  passerelle tierce ou un projet facturé, et le binaire en lit bien d'autres :
  l'environnement du sous-processus se réduit à une liste d'autorisation, et
  son HOME est privé, neuf à chaque appel, effacé ensuite ;
- sans bus de session D-Bus, agy ne joint pas le trousseau qui porte la
  connexion : l'initialisation refuse avant tout lancement.

Lancement : python -m unittest discover tests/ -v
"""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import re
import shlex
import shutil
import signal
import stat
import subprocess  # nosec B404 — doubles de Popen/run ; seuls bash, l'interpréteur et un faux agy tournent
import sys
import tempfile
import time
import unittest
from argparse import Namespace
from types import MappingProxyType, SimpleNamespace
from unittest.mock import MagicMock, patch

# Vise `src/` et non la racine : le test importe ainsi le PAQUET, pas
# l'arbre source, et une erreur d'empaquetage devient visible.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from aipmt.providers import antigravity, base, registry

_RACINE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_SRC = os.path.join(_RACINE, "src")
_REGEN = os.path.join(_RACINE, "regen_translations.sh")

# Chemin inexistant À DESSEIN : si un patch de Popen ou de run ne mordait pas,
# le lancement échouerait (FileNotFoundError) au lieu d'exécuter le vrai `agy`.
_BINAIRE = "/chemin/inexistant/agy-double-de-test"

# Valeur passée par référence : un littéral en face d'une clé *_API_KEY fait
# crier les scanners de secrets, alors qu'il ne s'agit que d'un jeton de test.
_MARQUEUR = "jeton-de-test"

_PROMPT = "PROMPT SYSTÈME : traduire du français vers l'anglais."
_SEGMENT = "Le chat dort sur le tapis."
# agy termine `response` par un saut de ligne, que le segment en ait un ou non
# (mesuré) ; la traduction rendue reprend la fin de ligne du segment, ici
# aucune.
_REPONSE = "The cat is sleeping on the rug.\n"
_TRADUCTION = "The cat is sleeping on the rug."
# Réponse partielle portée par le JSON d'un échec : elle ne doit jamais sortir.
_PARTIEL = "The cat is slee"

# Retire une clé de l'objet JSON simulé.
_ABSENT = object()

_FAUX_HOME = "/home/utilisateur-de-test"

# Pid des faux processus : au-delà de PID_MAX_LIMIT (2**22 sous Linux, 99 999
# sous macOS), aucun processus ne peut le porter. Si un chemin d'erreur
# atteignait `_codex_kill_group` sans que le test ait remplacé os.getpgid et
# os.killpg, getpgid échouerait (ESRCH) au lieu de désigner le groupe d'un vrai
# processus de l'utilisateur. Jamais un MagicMock : converti en 1, il a fait
# envoyer killpg(1, …), c'est-à-dire kill(-1, …), à toute la session.
_PID_INEXISTANT = 2**22 + 4242


# Effet des doubles de Popen et de run qui ne doivent JAMAIS servir. Un double
# nu, appelé par une régression, rend un faux processus dont le pid est un
# MagicMock — lu 1 par `__index__` — et `killpg(1)` vaut `kill(-1)` : le
# 2026-09-26, c'est ce chemin, ouvert par un mutant, qui a tué toute la
# session de l'utilisateur. Un appel imprévu échoue ici, avant tout processus.
_NE_DOIT_PAS_SERVIR = AssertionError("ce double ne doit jamais être appelé")

# Lu à l'import, dans l'environnement réel : `gettempdir()` garde sa première
# valeur en cache, et un test qui vide l'environnement ne doit pas déplacer le
# répertoire temporaire du reste de la suite.
_TMPDIR_REEL = tempfile.gettempdir()

# Hors CI : les runners posent CI=true, qui fait refuser toute initialisation.
_HORS_CI = {"CI": "", "GITHUB_ACTIONS": ""}

# Catalogue d'`agy models` relevé sur agy 1.2.11 le 2026-09-26 : l'effort de
# raisonnement fait partie de l'identifiant. À tenir à jour avec le catalogue.
_CATALOGUE_AGY = (
    "gemini-3.8-flash-high",
    "gemini-3.8-flash-medium",
    "gemini-3.8-flash-low",
    "gemini-3.7-flash-high",
    "gemini-3.7-flash-medium",
    "gemini-3.7-flash-low",
    "gemini-3.6-flash-high",
    "gemini-3.6-flash-medium",
    "gemini-3.6-flash-low",
    "gemini-3.1-pro-high",
    "gemini-3.1-pro-low",
    "claude-sonnet-4-6",
    "claude-opus-4-6-thinking",
    "gpt-oss-120b-medium",
)

# Ce qui passe : écrit en dur, et non relu dans le module — élargir la liste
# d'autorisation est une décision, qui doit faire échouer ces tests au lieu de
# les faire suivre. Un `env -i` réduit à ces variables s'authentifie (mesuré).
_ENV_TRANSMIS = {
    "PATH": "/usr/local/bin:/usr/bin:/bin",
    "LANG": "fr_FR.UTF-8",
    "LANGUAGE": "fr_FR:fr",
    # Toute la famille LC_, par préfixe.
    "LC_ALL": "fr_FR.UTF-8",
    "LC_MESSAGES": "fr_FR.UTF-8",
    "TZ": "Europe/Paris",
    "TERM": "xterm-256color",
    "USER": "utilisateur-de-test",
    "LOGNAME": "utilisateur-de-test",
    # C'est par le bus de session qu'agy atteint le trousseau, donc
    # l'abonnement (mesuré : bus masqué, agy attend 60 s puis échoue).
    "XDG_RUNTIME_DIR": "/run/user/4242",
    "DBUS_SESSION_BUS_ADDRESS": "unix:path=/run/user/4242/bus",
    # Proxies et certificats de la machine, dans les deux casses en usage.
    "HTTP_PROXY": "http://proxy.example.invalid:3128",
    "HTTPS_PROXY": "http://proxy.example.invalid:3128",
    "ALL_PROXY": "socks5://proxy.example.invalid:1080",
    "NO_PROXY": "localhost,127.0.0.1",
    "http_proxy": "http://proxy.example.invalid:3128",
    "https_proxy": "http://proxy.example.invalid:3128",
    "all_proxy": "socks5://proxy.example.invalid:1080",
    "no_proxy": "localhost,127.0.0.1",
    "SSL_CERT_FILE": "/etc/ssl/certs/ca-certificates.crt",
    "SSL_CERT_DIR": "/etc/ssl/certs",
}

# Tout le reste disparaît, y compris ce qu'aucune liste ne nomme.
_ENV_RETIRE = {
    # Détournements mesurés : passerelle tierce, projet Google Cloud facturé,
    # endpoint authentifié redirigé vers n'importe quelle URL.
    "AGY_GATEWAY_URL": "https://passerelle.example.invalid/v1",
    "AGY_ADC_AUTH": "true",
    "CLOUD_CODE_URL": "https://cloudcode.example.invalid",
    # Trouvées ensuite par une revue dans les chaînes du binaire, après
    # qu'une liste de refus les avait laissées passer.
    "AICODE_ENDPOINT_URL": "https://aicode.example.invalid",
    "UNLEASH_URL": "https://unleash.example.invalid/api",
    "GCE_METADATA_HOST": "metadata.example.invalid",
    "JETSKI_OAUTH_TOKEN": _MARQUEUR,
    # Mesuré : la valeur `1` est sans effet ; le module pose lui-même `true`.
    "AGY_CLI_DISABLE_AUTO_UPDATE": "1",
    "ANTIGRAVITY_CONFIG_DIR": "/srv/antigravity",
    "CLOUDSDK_CORE_PROJECT": "projet-facture",
    "GOOGLE_CLOUD_PROJECT": "projet-facture",
    "GOOGLE_APPLICATION_CREDENTIALS": "/chemin/vers/adc.json",
    "GEMINI_MODEL": "gemini-3.7-flash",
    "agy_gateway_url": "https://minuscules.example.invalid/v1",
    "OPENAI_BASE_URL": "https://relais.example.invalid/v1",
    # Aucun navigateur ne doit s'ouvrir depuis un job de traduction.
    "DISPLAY": ":0",
    "WAYLAND_DISPLAY": "wayland-0",
    "BROWSER": "/usr/bin/firefox",
    # Clés de tous les fournisseurs — et un nom au préfixe autorisé qui porte
    # un motif de secret : le filtrage des secrets passe APRÈS l'autorisation.
    "GOOGLE_API_KEY": _MARQUEUR,
    "GEMINI_API_KEY": _MARQUEUR,
    "OPENAI_API_KEY": _MARQUEUR,
    "ANTHROPIC_API_KEY": _MARQUEUR,
    "MISTRAL_API_KEY": _MARQUEUR,
    "XAI_API_KEY": _MARQUEUR,
    "OPENROUTER_API_KEY": _MARQUEUR,
    "OPENCODE_API_KEY": _MARQUEUR,
    "HF_TOKEN": _MARQUEUR,
    "LC_API_KEY": _MARQUEUR,
    # Chemins dérivés du HOME réel : ils ramèneraient agy dans les réglages et
    # l'historique de l'utilisateur.
    "XDG_CONFIG_HOME": f"{_FAUX_HOME}/.config",
    "XDG_DATA_HOME": f"{_FAUX_HOME}/.local/share",
    "XDG_CACHE_HOME": f"{_FAUX_HOME}/.cache",
    "XDG_STATE_HOME": f"{_FAUX_HOME}/.local/state",
    # Remplacés par le répertoire privé de l'appel.
    "HOME": _FAUX_HOME,
    "TMPDIR": _TMPDIR_REEL,
    "VARIABLE_QUE_PERSONNE_NE_NOMME": "valeur quelconque",
}

_ENV_UTILISATEUR = {**_ENV_TRANSMIS, **_ENV_RETIRE}

# Ce que voit agy, hors HOME et TMPDIR privés : la liste d'autorisation, et la
# mise à jour automatique coupée par la seule valeur qui la coupe.
_ENV_ATTENDU = {**_ENV_TRANSMIS, "AGY_CLI_DISABLE_AUTO_UPDATE": "true"}


def _args(**overrides):
    defaults = {
        "model": "gemini-3.7-flash-low",
        "source_lang": "fr",
        "target_lang": "en",
        "news": False,
        "reasoning_effort": None,
        "eco": False,
    }
    defaults.update(overrides)
    return Namespace(**defaults)


def _client(**overrides):
    defaults = {"binary": _BINAIRE, "timeout": 900, "backoff_seconds": 1.0}
    defaults.update(overrides)
    return antigravity._AntigravityClient(**defaults)


def _sortie(**champs):
    """L'objet JSON unique de `--output-format json` : SUCCESS et la réponse
    par défaut, chaque champ remplaçable ; `_ABSENT` retire la clé."""
    objet = {"status": "SUCCESS", "response": _REPONSE, **champs}
    return json.dumps({cle: valeur for cle, valeur in objet.items() if valeur is not _ABSENT})


# Lignes réelles du journal d'agy 1.2.11 (--log-file), relevées le 2026-09-26
# et reprises telles quelles, adresse du compte masquée. Format glog :
# sévérité et date, heure, fil, fichier:ligne. Une garde n'accepte son
# marqueur que sur une ligne entière de ce format.
_LIGNE_AGENT = {
    "true": "I0926 10:36:51.895710       1 conversation_manager.go:512] Starting new conversation (agent=true)",
    "false": "I0926 10:36:08.477937       1 conversation_manager.go:512] Starting new conversation (agent=false)",
}
_LIGNE_REPLI = 'W0926 10:30:43.128362       1 session.go:94] Agent "agent-inexistant" not found, falling back to default'
_LIGNE_ABONNEMENT = "I0926 10:36:47.628476       1 server_oauth.go:196] applyAuthResult: email=compte@example.com, authMethod=consumer, quotaProject="
# Relevée le même jour sur une sonde qui posait `modelProvider` et une clé
# factice : authentifié par clé API, l'adresse du compte y est vide.
_LIGNE_CLE_API = "I0926 10:37:30.080584       1 server_oauth.go:196] applyAuthResult: email=, authMethod=gemini_api_key, quotaProject="


def _ligne_auth(methode):
    """La ligne `applyAuthResult` réelle de `methode` : celle de l'abonnement,
    ou celle de la clé API, méthode substituée."""
    if methode == "consumer":
        return _LIGNE_ABONNEMENT
    return _LIGNE_CLE_API.replace("authMethod=gemini_api_key", f"authMethod={methode}")


def _echo(texte):
    """Entrée de l'utilisateur telle qu'agy la journalise, au format
    `HandleUserInput called with text: %q` relevé dans les chaînes du binaire
    (le fichier:ligne est illustratif). %q échappe les sauts de ligne : un
    document y tient sur une seule ligne, jamais en tête d'une autre."""
    return (
        "I0926 10:36:51.901233       1 store.go:271] HandleUserInput called with text: "
        + json.dumps(texte, ensure_ascii=False)
    )


def _journal(agent="true", auth="consumer", repli=False, echos=()):
    """Journal (--log-file) réduit aux lignes que lisent les gardes, dans
    l'ordre réel ; `None` retire la ligne correspondante, et `echos`
    s'insère entre l'authentification et la conversation."""
    lignes = [] if auth is None else [_ligne_auth(auth)]
    lignes.extend(echos)
    if repli:
        lignes.append(_LIGNE_REPLI)
    if agent is not None:
        lignes.append(_LIGNE_AGENT[agent])
    return "\n".join(lignes) + "\n"


_JOURNAL_OK = _journal()
# Le préflight n'ouvre aucune conversation : seule la ligne d'authentification.
_JOURNAL_PREFLIGHT = _journal(agent=None)
# Mesuré le 2026-09-26 : aucun crédit payant, aucune clé API, aucun projet.
_CONFIG_MESUREE = {"useG1Credits": False, "modelProvider": "", "gcp": None}

# Forme mesurée de la ligne d'échec structurée (sonde du 2026-09-26 : une clé
# API factice), reprise telle quelle. Les autres AGY_ERROR de ce fichier en
# reprennent les champs, avec des valeurs illustratives.
_AGY_ERROR_MESURE = (
    'AGY_ERROR: {"short_error":"agent executor error: generating and executing: Error 400, '
    "Message: API key not valid. Please pass a valid API key., Status: INVALID_ARGUMENT, "
    "Details: [map[@type:type.googleapis.com/google.rpc.ErrorInfo domain:googleapis.com "
    "metadata:map[service:generativelanguage.googleapis.com] reason:API_KEY_INVALID] "
    "map[@type:type.googleapis.com/google.rpc.LocalizedMessage locale:en-US message:API key "
    'not valid. Please pass a valid API key.]]","status":"INVALID_ARGUMENT","error_code":400,'
    '"code_kind":"http","retryable":false,"error_id":"3e7a7335-21d5-4f55-8c98-aa97201e0f10-1"}'
)


def _sortie_config(config):
    """Sortie JSON de `agy -p /config` : la configuration sous command.data."""
    return json.dumps({"command": {"data": {"config": config}}})


def _photographier(cwd, env):
    """État du répertoire privé AU MOMENT de l'appel : il aura disparu ensuite."""
    if cwd is None or not os.path.isdir(cwd):
        return None
    base_dir = os.path.dirname(cwd)
    fichiers = sorted(
        os.path.relpath(os.path.join(dossier, nom), cwd)
        for dossier, _sous_dossiers, noms in os.walk(cwd)
        for nom in noms
    )
    chemin_agent = os.path.join(cwd, ".agents", "agents", "aipmt.md")
    agent = None
    if os.path.isfile(chemin_agent):
        with open(chemin_agent, encoding="utf-8") as f:
            agent = f.read()
    env = env or {}
    return SimpleNamespace(
        base=base_dir,
        fichiers=fichiers,
        agent=agent,
        mode=stat.S_IMODE(os.stat(base_dir).st_mode),
        home_existe=os.path.isdir(env.get("HOME", "")),
        tmp_existe=os.path.isdir(env.get("TMPDIR", "")),
    )


def _frontmatter(texte):
    """(en-tête « clé: valeur », corps) d'un agent au format d'agy."""
    lignes = texte.split("\n")
    fin = lignes.index("---", 1)
    entete = dict(ligne.split(": ", 1) for ligne in lignes[1:fin])
    return entete, "\n".join(lignes[fin + 1 :])


def _env_sans_agy(dossier):
    """Environnement d'un sous-processus RÉEL de la suite (bash, interpréteur) :
    ni AGY_BIN, ni le PATH, ni HOME ne mènent au vrai `agy`. Aucun n'a de raison
    de le lancer ; s'il essayait, il échouerait au lieu de consommer du quota."""
    env = os.environ.copy()
    env["HOME"] = dossier
    env["AGY_BIN"] = os.path.join(dossier, "agy-absent")
    env["PATH"] = os.pathsep.join(
        d
        for d in env.get("PATH", "").split(os.pathsep)
        if d and not os.path.exists(os.path.join(d, "agy"))
    )
    return env


def _script_faux_agy(temoins):
    """Faux `agy` en /bin/sh, pour le seul test de bout en bout : il consigne
    son chemin d'appel, son répertoire de travail, stdin et son environnement
    dans les fichiers `temoins`, écrit un journal réel là où --log-file le
    demande, et répond en SUCCESS."""
    chemins = {nom: shlex.quote(chemin) for nom, chemin in temoins.items()}
    journal = " ".join(shlex.quote(ligne) for ligne in (_LIGNE_ABONNEMENT, _LIGNE_AGENT["true"]))
    return "\n".join(
        [
            "#!/bin/sh",
            'journal=""',
            'precedent=""',
            'for argument in "$@"; do',
            '  if [ "$precedent" = "--log-file" ]; then journal="$argument"; fi',
            '  precedent="$argument"',
            "done",
            f"printf '%s' \"$0\" > {chemins['argv0']}",
            f"pwd > {chemins['cwd']}",
            f"cat > {chemins['stdin']}",
            f"env > {chemins['env']}",
            f"printf '%s\\n' {journal} > \"$journal\"",
            f"printf '%s\\n' {shlex.quote(_sortie())}",
            "",
        ]
    )


class _FakePopen:
    """Double de `subprocess.Popen` qui joue agy : il relit dans argv le chemin
    de --log-file et y écrit le journal, comme le vrai binaire — ce qui vérifie
    au passage que le drapeau est passé —, et photographie le répertoire privé
    au moment de l'appel. `journal=None` : agy n'a rien écrit."""

    def __init__(self, stdout=None, returncode=0, stderr="", journal=_JOURNAL_OK, timeout=False):
        self._stdout = _sortie() if stdout is None else stdout
        self.returncode, self._stderr = returncode, stderr
        self._journal, self._timeout = journal, timeout
        self.calls = 0
        self.argv = self.kwargs = self.communicate_kwargs = self.photo = None
        self.pid = _PID_INEXISTANT

    def __call__(self, argv, **kwargs):
        self.calls += 1
        self.argv, self.kwargs = list(argv), kwargs
        self.photo = _photographier(kwargs.get("cwd"), kwargs.get("env"))
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
        if self._journal is not None:
            with open(self.argv[self.argv.index("--log-file") + 1], "w", encoding="utf-8") as f:
                f.write(self._journal)
        return self._stdout, self._stderr

    def wait(self, timeout=None):
        return self.returncode


class _Sequence:
    """Popen qui rejoue un double par tentative, dans l'ordre."""

    def __init__(self, *fakes):
        self._reste = list(fakes)
        self.joues = []

    @property
    def calls(self):
        return len(self.joues)

    def __call__(self, argv, **kwargs):
        if not self._reste:
            raise AssertionError("tentative de trop : aucun double prévu")
        fake = self._reste.pop(0)
        self.joues.append(fake)
        return fake(argv, **kwargs)


class _FakeRun:
    """Double de `subprocess.run` pour le préflight : `agy --version`, puis
    `agy -p /config`, dont il écrit le journal là où --log-file le demande.
    Toute autre commande fait échouer le test."""

    # Réponses d'agy 1.2.11 connecté à l'abonnement, chacune remplaçable par
    # mot-clé ; `config_stdout=None` : la sortie est tirée de `config`. En
    # lecture seule : un test ne peut pas changer le défaut des suivants.
    _REPONSES = MappingProxyType(
        {
            "version": "1.2.11\n",
            "version_rc": 0,
            "version_stderr": "",
            "config": _CONFIG_MESUREE,
            "config_stdout": None,
            "config_rc": 0,
            "config_stderr": "",
        }
    )

    def __init__(self, *, journal=_JOURNAL_PREFLIGHT, **reponses):
        inconnues = sorted(set(reponses) - set(self._REPONSES))
        if inconnues:
            # Une faute de frappe dans un test ne doit pas passer en silence
            # en laissant la valeur par défaut.
            raise TypeError(f"_FakeRun : réglages inconnus {inconnues}")
        reglages = {**self._REPONSES, **reponses}
        self.version = SimpleNamespace(
            returncode=reglages["version_rc"],
            stdout=reglages["version"],
            stderr=reglages["version_stderr"],
        )
        stdout = reglages["config_stdout"]
        if stdout is None:
            stdout = _sortie_config(reglages["config"])
        self.config = SimpleNamespace(
            returncode=reglages["config_rc"], stdout=stdout, stderr=reglages["config_stderr"]
        )
        self._journal = journal
        self.appels = []

    @property
    def calls(self):
        return len(self.appels)

    def __call__(self, argv, **kwargs):
        argv = list(argv)
        photo = _photographier(kwargs.get("cwd"), kwargs.get("env"))
        self.appels.append(SimpleNamespace(argv=argv, kwargs=kwargs, photo=photo))
        if argv[1:] == ["--version"]:
            return self.version
        if argv[1:3] == ["-p", "/config"]:
            if self._journal is not None:
                with open(argv[argv.index("--log-file") + 1], "w", encoding="utf-8") as f:
                    f.write(self._journal)
            return self.config
        raise AssertionError(f"commande de préflight inattendue : {argv!r}")


class _AgyTestCase(unittest.TestCase):
    """Socle : Popen et time.sleep remplacés, stderr capturé, et le nombre
    d'appels au double vérifié — un patch qui ne mord pas passerait sinon."""

    def _traduire(self, popen, appels=1, client=None, args=None, segment=_SEGMENT):
        with (
            patch.object(subprocess, "Popen", popen),
            patch.object(time, "sleep") as sommeil,
            patch("sys.stderr", new_callable=io.StringIO) as capture,
        ):
            self.faux_sommeil, self.stderr_capture = sommeil, capture
            try:
                return antigravity._call_antigravity(
                    client or _client(), args or _args(), _PROMPT, segment
                )
            finally:
                self.assertEqual(popen.calls, appels, "appels au double de Popen")

    def _assert_env_isole(self, env, photo):
        """Exactement la liste d'autorisation et la mise à jour coupée, plus
        HOME et TMPDIR privés, distincts, créés sous le répertoire de l'appel."""
        prives = {nom: env.get(nom) for nom in ("HOME", "TMPDIR")}
        self.assertEqual({nom: v for nom, v in env.items() if nom not in prives}, _ENV_ATTENDU)
        for nom, valeur in prives.items():
            self.assertTrue(valeur and valeur.startswith(photo.base + os.sep), f"{nom}={valeur}")
        self.assertNotEqual(prives["HOME"], prives["TMPDIR"])
        self.assertTrue(photo.home_existe)
        self.assertTrue(photo.tmp_existe)


class TestAntigravityInvocation(_AgyTestCase):
    def test_nominal_keeps_the_text_and_trims_only_the_final_newline(self):
        """Indentation de tête et lignes vides intérieures rendues telles
        quelles ; le saut de ligne qu'agy ajoute suit le segment, qui n'en a
        pas ici (cf. TestAntigravityLineEnding)."""
        reponse = "    code indenté\n\nThe cat is sleeping.\n"
        fake = _FakePopen(stdout=_sortie(response=reponse))
        self.assertEqual(self._traduire(fake), "    code indenté\n\nThe cat is sleeping.")
        self.faux_sommeil.assert_not_called()

    def test_segment_goes_through_stdin_in_its_own_session(self):
        fake = _FakePopen()
        self._traduire(fake, client=_client(timeout=321))
        self.assertEqual(fake.communicate_kwargs, {"input": _SEGMENT, "timeout": 321})
        self.assertIs(fake.kwargs["stdin"], subprocess.PIPE)
        self.assertTrue(fake.kwargs["start_new_session"])

    def test_argv_is_exactly_the_measured_invocation(self):
        """Tout drapeau ajouté est une décision, pas un détail : `-p` ferait
        ignorer stdin (mesuré), `--print-timeout` rendrait une sortie partielle
        en SUCCESS (mesuré)."""
        fake = _FakePopen()
        self._traduire(fake, args=_args(model="gemini-3.8-flash-low"))
        journal = fake.argv[fake.argv.index("--log-file") + 1]
        attendu = [
            _BINAIRE,
            "--output-format",
            "json",
            "--agent",
            "aipmt",
            "--disable-slash-commands",
            "--log-file",
            journal,
            "--model",
            "gemini-3.8-flash-low",
        ]
        self.assertEqual(fake.argv, attendu)
        self.assertEqual(os.path.dirname(journal), fake.photo.base)

    def test_argv_never_carries_print_mode_permission_bypass_or_text(self):
        fake = _FakePopen()
        self._traduire(fake)
        for interdit in ("-p", "--print-timeout", "--dangerously-skip-permissions"):
            with self.subTest(interdit=interdit):
                presents = [a for a in fake.argv if a == interdit or a.startswith(interdit + "=")]
                self.assertEqual(presents, [])
        ligne = " ".join(fake.argv)
        self.assertNotIn(_SEGMENT, ligne)
        self.assertNotIn(_PROMPT, ligne)

    def test_workdir_holds_only_the_toolless_agent(self):
        """Mesuré : ~800 tokens d'entrée au lieu de 12 400 avec l'agent par
        défaut ; `excludeDefaultComponents` seul laissait les hooks du
        workspace exécuter leurs commandes, `inheritCustomizations: false` les
        coupe."""
        fake = _FakePopen()
        self._traduire(fake)
        photo = fake.photo
        # agy cherche l'agent dans son répertoire de travail : sans `cwd`, il
        # tournerait dans celui de l'appelant, sans l'agent de traduction.
        self.assertIsNotNone(photo, "aucun répertoire de travail privé transmis à Popen (cwd)")
        self.assertEqual(photo.fichiers, [os.path.join(".agents", "agents", "aipmt.md")])
        self.assertTrue(photo.agent.startswith("---\n"))
        entete, corps = _frontmatter(photo.agent)
        self.assertTrue(entete.pop("description"))
        self.assertEqual(
            entete,
            {
                "name": "aipmt",
                "tools": "[]",
                "excludeDefaultComponents": "true",
                "inheritCustomizations": "false",
            },
        )
        contrat = antigravity.ANTIGRAVITY_AGENT_CONTRACT
        self.assertEqual(corps, f"# aipmt\n\n{_PROMPT}{contrat}\n")
        for consigne in ("aucun outil", "UNIQUEMENT", "JAMAIS une question"):
            self.assertIn(consigne, contrat)

    def test_environment_is_an_allowlist_and_home_is_private(self):
        """Seule la liste d'autorisation passe : une liste de refus oubliait, à
        chaque relecture, une variable qui détourne ou facture l'appel. Une
        variable que personne n'a nommée disparaît donc aussi."""
        fake = _FakePopen()
        with patch.dict(os.environ, _ENV_UTILISATEUR, clear=True):
            self._traduire(fake)
            apres = dict(os.environ)
        self._assert_env_isole(fake.kwargs["env"], fake.photo)
        # Le filtrage travaille sur une copie : le processus qui traduit garde
        # l'environnement de l'utilisateur, intact.
        self.assertEqual(apres, _ENV_UTILISATEUR)

    def test_allowlist_is_the_reviewed_one(self):
        """Tout ajout à la liste doit passer par ce test, écrit en dur : il
        nomme ce que la revue a accepté, rien de plus."""
        self.assertEqual(
            set(antigravity.ANTIGRAVITY_KEPT_ENV_VARS),
            {nom for nom in _ENV_TRANSMIS if not nom.startswith("LC_")},
        )
        self.assertEqual(antigravity.ANTIGRAVITY_KEPT_ENV_PREFIXES, ("LC_",))
        self.assertEqual(
            antigravity.ANTIGRAVITY_ENV_OVERRIDES, {"AGY_CLI_DISABLE_AUTO_UPDATE": "true"}
        )

    def test_leading_bang_at_or_slash_stays_text_to_translate(self):
        """Mesuré : sans --disable-slash-commands, « /help » s'exécutait à la
        place de la traduction. Le segment part tel quel, sur stdin."""
        for segment in ("/help", "!ls", "@README.md"):
            with self.subTest(segment=segment):
                fake = _FakePopen()
                self._traduire(fake, segment=segment)
                self.assertEqual(fake.communicate_kwargs["input"], segment)
                self.assertIn("--disable-slash-commands", fake.argv)
                self.assertNotIn(segment, fake.argv)


class TestAntigravityPrivateDirectory(_AgyTestCase):
    """Chaque appel laissait une conversation d'environ 200 Ko, texte traduit
    compris, dans l'historique d'agy de l'utilisateur : le répertoire privé est
    neuf, fermé (0700) et effacé, que l'appel réussisse ou non."""

    def test_fresh_0700_and_removed_after_success(self):
        avant = set(os.listdir(tempfile.gettempdir()))
        fake = _FakePopen()
        self._traduire(fake)
        base_dir = fake.photo.base
        self.assertNotIn(os.path.basename(base_dir), avant)
        self.assertTrue(os.path.basename(base_dir).startswith("translate-antigravity-"))
        self.assertEqual(fake.photo.mode, 0o700)
        self.assertFalse(os.path.exists(base_dir))

    def test_removed_after_every_kind_of_failure(self):
        echecs = {
            "code 3": _FakePopen(stdout=_sortie(status="ERROR"), returncode=3),
            "repli d'agent": _FakePopen(journal=_journal(agent="false", repli=True)),
            "clé API au journal": _FakePopen(journal=_journal(auth="gemini_api_key")),
            "réponse vide": _FakePopen(stdout=_sortie(response="")),
        }
        for nom, fake in echecs.items():
            with self.subTest(nom):
                with self.assertRaises(antigravity._AntigravityCallError):
                    self._traduire(fake)
                self.assertFalse(os.path.exists(fake.photo.base))

    def test_sandbox_is_removed_on_any_exception_and_log_is_left_to_agy(self):
        releve = SimpleNamespace()

        def echouer_dans_le_repertoire_prive():
            """Relève, DANS le répertoire privé, ce que le test vérifie ensuite
            hors de la portée d'assertRaises, puis lève l'échec simulé."""
            with antigravity._antigravity_sandbox(_PROMPT) as box:
                releve.base = os.path.dirname(box.work)
                releve.journal = box.log
                releve.journal_existe = os.path.exists(box.log)
                raise RuntimeError("échec simulé")

        with self.assertRaises(RuntimeError) as cm:
            echouer_dans_le_repertoire_prive()
        # L'échec remonté est bien celui levé dans le répertoire privé.
        self.assertEqual(str(cm.exception), "échec simulé")
        self.assertEqual(os.path.dirname(releve.journal), releve.base)
        self.assertFalse(releve.journal_existe)
        self.assertFalse(os.path.exists(releve.base))


class TestAntigravityOutputContract(_AgyTestCase):
    """Un code retour nul ne prouve rien : c'est l'objet JSON, `status`
    compris, puis le journal de l'appel qui font foi."""

    def test_failed_exits_never_return_the_partial_answer(self):
        cas = {
            "code 3, status ERROR": _FakePopen(
                stdout=_sortie(status="ERROR", response=_PARTIEL), returncode=3
            ),
            "code 3 malgré SUCCESS": _FakePopen(stdout=_sortie(response=_PARTIEL), returncode=3),
            "code 0, status ERROR": _FakePopen(stdout=_sortie(status="ERROR", response=_PARTIEL)),
            "code 0, status CANCELED": _FakePopen(
                stdout=_sortie(status="CANCELED", response=_PARTIEL)
            ),
            "code 0, status absent": _FakePopen(stdout=_sortie(status=_ABSENT, response=_PARTIEL)),
            "code 0, JSON non objet": _FakePopen(stdout=json.dumps(["SUCCESS"])),
            "code 0, stdout vide": _FakePopen(stdout=""),
        }
        for nom, fake in cas.items():
            with self.subTest(nom):
                with self.assertRaisesRegex(
                    antigravity._AntigravityCallError, "Antigravity CLI a échoué"
                ) as cm:
                    self._traduire(fake)
                self.assertNotIn(_PARTIEL, str(cm.exception))
                self.assertFalse(cm.exception.rate_limited)

    def test_interactive_ui_error_on_stdout_is_refused(self):
        """Mesuré : un stdin vide ouvre l'interface interactive, qui sort en 0
        avec une erreur non JSON sur stdout (forme illustrative ci-dessous)."""
        tui = "Error: could not open a new TTY: open /dev/tty: no such device or address\n"
        fake = _FakePopen(stdout=tui)
        with self.assertRaisesRegex(
            antigravity._AntigravityCallError, "code 0.*sortie illisible.*open a new TTY"
        ):
            self._traduire(fake)

    def test_failure_detail_goes_from_the_most_precise_to_the_vaguest(self):
        """Le détail clôt le message, seul : un code couleur ou un « } » écrits
        après l'objet AGY_ERROR n'y entrent pas."""
        agy_error = 'AGY_ERROR: {"code": "MODEL_ERROR", "message": "modèle indisponible"}'
        compacte = '{"code": "MODEL_ERROR", "message": "modèle indisponible"}'
        erreur = _sortie(status="ERROR", response=_PARTIEL)
        cas = (
            (
                "champ error du JSON",
                _sortie(status="ERROR", error="agent en panne"),
                agy_error,
                "agent en panne",
            ),
            ("ligne AGY_ERROR", erreur, f"avant\n{agy_error}\naprès\n", compacte),
            ("AGY_ERROR en couleur", erreur, f"\x1b[31m{agy_error}\x1b[0m\n", compacte),
            ("AGY_ERROR puis « } » parasite", erreur, f"{agy_error}\x1b[0m }}\n", compacte),
            (
                "AGY_ERROR illisible, rendu brut",
                erreur,
                "AGY_ERROR: {pas du json}\n",
                '{"message": "{pas du json}"}',
            ),
            (
                "fin de stderr",
                "",
                "ligne 1\nligne 2\nligne 3\ndernière\n",
                "ligne 2 | ligne 3 | dernière",
            ),
            ("aucun détail", erreur, "", "(aucun détail)"),
        )
        for nom, stdout, stderr, detail in cas:
            with self.subTest(nom):
                fake = _FakePopen(stdout=stdout, returncode=3, stderr=stderr)
                with self.assertRaises(antigravity._AntigravityCallError) as cm:
                    self._traduire(fake)
                message = str(cm.exception)
                self.assertTrue(message.endswith(f") : {detail}"), message)
                self.assertIn("code 3", message)
                self.assertNotIn(_PARTIEL, message)

    def test_rejected_argument_exit_1_is_reported_and_not_retried(self):
        """rc 1 : argument refusé, un modèle inconnu par exemple — sans repli
        silencieux sur un autre modèle depuis agy 1.1.2."""
        fake = _FakePopen(stdout="", returncode=1, stderr='Error: unknown model "gemini-9.9"\n')
        with self.assertRaisesRegex(
            antigravity._AntigravityCallError, 'code 1.*unknown model "gemini-9.9"'
        ):
            self._traduire(fake)
        self.faux_sommeil.assert_not_called()

    def test_success_carrying_a_suspect_key_is_refused(self):
        # Valeurs illustratives : seule leur présence non vide compte.
        cas = {
            "denied_actions": ([{"tool": "run_command"}], "le confinement n'a pas tenu"),
            "command": ({"name": "/help"}, "une commande slash a répondu"),
            "error": ("échec partiel", "une erreur accompagne le statut SUCCESS"),
        }
        for cle, (valeur, motif) in cas.items():
            with self.subTest(cle=cle):
                fake = _FakePopen(stdout=_sortie(response=_PARTIEL, **{cle: valeur}))
                with self.assertRaisesRegex(antigravity._AntigravityCallError, motif) as cm:
                    self._traduire(fake)
                self.assertNotIn(_PARTIEL, str(cm.exception))

    def test_empty_suspect_keys_are_not_a_refusal(self):
        """Seule une valeur non vide refuse : une clé présente mais vide ne
        porte ni action refusée, ni commande, ni erreur."""
        fake = _FakePopen(stdout=_sortie(denied_actions=[], command=None, error=""))
        self.assertEqual(self._traduire(fake), _TRADUCTION)

    def test_truncation_notes_on_stderr_refuse_a_success(self):
        # Formes illustratives : seule la sous-chaîne compte, casse ignorée.
        notes = {
            "print timeout": "Warning: Print Timeout reached, returning what was received",
            "no output produced": "no output produced (tool denied in headless mode)",
            "may be truncated": "Note: the response may be truncated",
        }
        for marqueur, stderr in notes.items():
            with self.subTest(marqueur):
                fake = _FakePopen(stdout=_sortie(response=_PARTIEL), stderr=stderr + "\n")
                with self.assertRaisesRegex(
                    antigravity._AntigravityCallError, f"« {marqueur} »"
                ) as cm:
                    self._traduire(fake)
                self.assertNotIn(_PARTIEL, str(cm.exception))

    def test_blank_or_missing_response_is_refused(self):
        for reponse in ("", " \n\t", None, 42, ["texte"], _ABSENT):
            with self.subTest(reponse=reponse):
                fake = _FakePopen(stdout=_sortie(response=reponse))
                with self.assertRaisesRegex(antigravity._AntigravityCallError, "aucun texte"):
                    self._traduire(fake)

    def test_agent_fallback_refuses_even_a_fluent_answer(self):
        """Mesuré : l'agent introuvable, agy est retombé sur son agent de codage
        (57 outils), rc 0 et status SUCCESS, et a répondu à « Le chat dort. »
        au lieu de le traduire. Seul le journal le disait."""
        conversation = "Chut, ne le réveillons pas ! Que puis-je faire pour vous ?\n"
        fake = _FakePopen(
            stdout=_sortie(response=conversation), journal=_journal(agent="false", repli=True)
        )
        with self.assertRaisesRegex(antigravity._AntigravityCallError, "agent de codage") as cm:
            self._traduire(fake, segment="Le chat dort.")
        self.assertNotIn("Chut", str(cm.exception))

    def test_fallback_line_wins_over_a_positive_marker(self):
        fake = _FakePopen(journal=_journal(agent="true", repli=True))
        with self.assertRaisesRegex(antigravity._AntigravityCallError, "agent de codage"):
            self._traduire(fake)

    def test_log_must_positively_confirm_the_translation_agent(self):
        """Le marqueur POSITIF est exigé (l'agent par défaut écrit agent=false) :
        un format de journal qui changerait ferait refuser la traduction au lieu
        de retirer la garde en silence."""
        cas = {
            "agent=false seul": _journal(agent="false"),
            "aucune conversation": _journal(agent=None),
            "journal vide": "",
            "journal absent": None,
        }
        for nom, journal in cas.items():
            with self.subTest(nom):
                fake = _FakePopen(journal=journal)
                with self.assertRaisesRegex(
                    antigravity._AntigravityCallError, "ne confirme pas le chargement"
                ):
                    self._traduire(fake)

    def test_log_must_attest_the_subscription(self):
        """Seules les méthodes autres que l'abonnement sont nommées : c'est
        elles qu'il faut aller corriger."""
        cas = {
            "clé API Gemini": (
                _journal(auth="gemini_api_key"),
                "authentifié en gemini_api_key et non",
            ),
            "abonnement et clé mêlés": (
                _journal(echos=[_ligne_auth("gemini_api_key")]),
                "authentifié en gemini_api_key et non",
            ),
            "aucune méthode": (_journal(auth=None), "ne dit pas par quel compte.*lancer `agy`"),
        }
        for nom, (journal, motif) in cas.items():
            with self.subTest(nom):
                fake = _FakePopen(journal=journal)
                with self.assertRaisesRegex(antigravity._AntigravityCallError, motif):
                    self._traduire(fake)

    def test_empty_segment_is_refused_before_any_launch(self):
        """Sans texte sur stdin, agy ouvrirait son interface interactive."""
        for segment in ("", "   \n\t"):
            with self.subTest(segment=segment):
                popen = MagicMock(name="Popen", side_effect=_NE_DOIT_PAS_SERVIR)
                client, args = _client(), _args()
                # Si la garde régressait, le processus rendu par ce Popen aurait
                # un MagicMock pour pid, converti en 1 : killpg(1, …) viserait
                # toute la session. getpgid et killpg restent donc remplacés.
                with (
                    patch.object(subprocess, "Popen", popen),
                    patch.object(time, "sleep") as sommeil,
                    patch.object(os, "getpgid", return_value=_PID_INEXISTANT) as getpgid,
                    patch.object(os, "killpg") as killpg,
                    self.assertRaisesRegex(antigravity._AntigravityCallError, "Segment vide"),
                ):
                    antigravity._call_antigravity(client, args, _PROMPT, segment)
                popen.assert_not_called()
                sommeil.assert_not_called()
                getpgid.assert_not_called()
                killpg.assert_not_called()


class TestAntigravityLogAnchoring(_AgyTestCase):
    """Un marqueur ne vaut que sur une ligne glog entière. La documentation
    d'aipmt cite ces messages, et agy journalise l'entrée de l'utilisateur : un
    document qui les contient ne doit ni confirmer l'agent ou l'abonnement, ni
    déclencher le refus de repli."""

    _AGENT_CHARGE = "Starting new conversation (agent=true)"
    _REPLI = 'Agent "aipmt" not found, falling back to default'

    def test_positive_marker_outside_a_glog_line_does_not_confirm(self):
        cas = {
            "écho d'un document": _journal(
                agent=None, echos=[_echo(f"Journal attendu :\n{self._AGENT_CHARGE}\n")]
            ),
            "écho, agent par défaut chargé": _journal(
                agent="false", echos=[_echo(self._AGENT_CHARGE)]
            ),
            "ligne brute": _journal(agent=None, echos=[self._AGENT_CHARGE]),
            "ancien préfixe illustratif": _journal(
                agent=None, echos=[f"2026-09-26T10:00:00Z INFO {self._AGENT_CHARGE}"]
            ),
            "marqueur suivi d'un texte": _journal(
                agent=None, echos=[f"{_LIGNE_AGENT['true']} (cité)"]
            ),
            "ligne glog indentée": _journal(agent=None, echos=[f"  {_LIGNE_AGENT['true']}"]),
        }
        for nom, journal in cas.items():
            with self.subTest(nom):
                fake = _FakePopen(journal=journal)
                with self.assertRaisesRegex(
                    antigravity._AntigravityCallError, "ne confirme pas le chargement"
                ):
                    self._traduire(fake)

    def test_fallback_text_outside_a_glog_line_does_not_refuse(self):
        """Faux positif évité : traduire un texte qui cite le repli ne doit pas
        faire croire à un repli."""
        cas = {
            "écho d'un document": _echo(f"En cas d'échec :\n{self._REPLI}\n"),
            "ligne brute": self._REPLI,
            "ligne de repli suivie d'un texte": f"{_LIGNE_REPLI} (cité)",
        }
        for nom, ligne in cas.items():
            with self.subTest(nom):
                fake = _FakePopen(journal=_journal(echos=[ligne]))
                self.assertEqual(self._traduire(fake), _TRADUCTION)

    def test_subscription_is_attested_only_by_the_apply_auth_result_line(self):
        abonnement = _LIGNE_ABONNEMENT.split("] ", 1)[1]
        cas = {
            "écho d'un document": _echo(abonnement),
            "ligne brute": abonnement,
            "autre ligne glog": "I0926 10:36:47.700112       1 session.go:120] session: authMethod=consumer",
        }
        for nom, ligne in cas.items():
            with self.subTest(nom):
                fake = _FakePopen(journal=_journal(auth=None, echos=[ligne]))
                with self.assertRaisesRegex(
                    antigravity._AntigravityCallError, "ne dit pas par quel compte"
                ):
                    self._traduire(fake)

    def test_any_other_auth_method_anywhere_is_refused(self):
        """À côté d'un `applyAuthResult` consumer, toute autre méthode écrite,
        où que ce soit, fait refuser : `auth_method=` figure aussi dans le
        binaire. Fermé à dessein, même sur un document qui la citerait."""
        cas = {
            "auth_method sur une ligne glog": (
                "I0926 10:36:47.700112       1 metrics.go:88] event: auth_method=gemini_api_key",
                "gemini_api_key",
            ),
            "authMethod dans un écho": (_echo("authMethod=gateway"), "gateway"),
            "casse relâchée, ligne brute": ("authmethod=gcp_adc", "gcp_adc"),
        }
        for nom, (ligne, methode) in cas.items():
            with self.subTest(nom):
                fake = _FakePopen(journal=_journal(echos=[ligne]))
                with self.assertRaisesRegex(
                    antigravity._AntigravityCallError,
                    f"authentifié en {methode} et non sur l'abonnement",
                ):
                    self._traduire(fake)

    def test_consumer_written_elsewhere_is_harmless(self):
        for ligne in (_echo("authMethod=consumer"), "auth_method=consumer"):
            with self.subTest(ligne=ligne):
                fake = _FakePopen(journal=_journal(echos=[ligne]))
                self.assertEqual(self._traduire(fake), _TRADUCTION)


class TestAntigravityLineEnding(_AgyTestCase):
    """agy termine chaque réponse par un saut de ligne, que le segment en ait
    un ou non (mesuré sur les quatorze modèles) : la réponse reprend la fin de
    ligne du SEGMENT. Joints par « \\n », les segments retrouvent la source à
    une coupure de titre ou de paragraphe, et une coupure de phrase ne coupe
    plus le paragraphe en deux."""

    def test_answer_takes_the_line_ending_of_the_segment(self):
        for segment, fin in (("Le chat dort.\n", "\n"), ("Le chat dort.", "")):
            for reponse in ("The cat sleeps.", "The cat sleeps.\n", "The cat sleeps.\n\n\n"):
                with self.subTest(segment=segment, reponse=reponse):
                    fake = _FakePopen(stdout=_sortie(response=reponse))
                    self.assertEqual(self._traduire(fake, segment=segment), "The cat sleeps." + fin)

    def test_only_final_newlines_are_rewritten(self):
        """Indentation de tête, lignes vides intérieures et saut de ligne forcé
        Markdown (deux espaces en fin de ligne) restent tels quels."""
        cas = (
            ("    code\n\nLe chat.\n", "    code\n\nThe cat.", "    code\n\nThe cat.\n"),
            ("Ligne forcée  \n", "Forced line  \n", "Forced line  \n"),
            ("Ligne forcée  ", "Forced line  \n\n", "Forced line  "),
        )
        for segment, reponse, attendu in cas:
            with self.subTest(segment=segment):
                fake = _FakePopen(stdout=_sortie(response=reponse))
                self.assertEqual(self._traduire(fake, segment=segment), attendu)


class TestAntigravityRetries(_AgyTestCase):
    def test_rate_limits_are_retried_in_a_fresh_private_dir(self):
        limites = {
            "429 comme nombre": {
                "stdout": _sortie(status="ERROR", response=_PARTIEL),
                "stderr": 'AGY_ERROR: {"status": 429}\n',
            },
            "rate limit": {"stdout": "", "stderr": "Error: Rate limit exceeded, retry later\n"},
            "too many requests": {"stdout": _sortie(status="ERROR", error="Too Many Requests")},
            "rate_limit": {
                "stdout": _sortie(status="ERROR"),
                "stderr": 'AGY_ERROR: {"reason": "RATE_LIMIT_EXCEEDED"}\n',
            },
            # agy dit lui-même l'échec réessayable : aucun marqueur n'est requis.
            "retryable: true, sans marqueur": {
                "stdout": _sortie(status="ERROR"),
                "stderr": 'AGY_ERROR: {"short_error":"The model is overloaded. Please try again later.","status":"UNAVAILABLE","error_code":503,"code_kind":"http","retryable":true}\n',
            },
            # Chez Google, une limite par minute porte aussi RESOURCE_EXHAUSTED.
            "retryable: true malgré RESOURCE_EXHAUSTED": {
                "stdout": "",
                "stderr": 'AGY_ERROR: {"short_error":"Too many requests per minute","status":"RESOURCE_EXHAUSTED","error_code":429,"code_kind":"http","retryable":true}\n',
            },
        }
        for nom, echec in limites.items():
            with self.subTest(nom):
                premier = _FakePopen(returncode=3, **echec)
                second = _FakePopen(stdout=_sortie(response="Second essai\n"))
                texte = self._traduire(_Sequence(premier, second), appels=2)
                self.assertEqual(texte, "Second essai")
                self.faux_sommeil.assert_called_once_with(1.0)
                self.assertIn(
                    "Antigravity rate limit (tentative 1/3)", self.stderr_capture.getvalue()
                )
                self.assertNotEqual(premier.photo.base, second.photo.base)
                self.assertFalse(os.path.exists(premier.photo.base))
                self.assertFalse(os.path.exists(second.photo.base))

    def test_quota_and_identifiers_are_not_rate_limits(self):
        """Une fenêtre de 5 heures épuisée ne se rend pas en 90 s : `quota` et
        tout texte d'épuisement coupent la relance, même avec un 429. Quand
        AGY_ERROR porte `retryable: false`, il décide seul, marqueurs compris ;
        et « 429 » noyé dans un identifiant n'est pas un statut HTTP."""
        cas = {
            "quota": ("", "Error: quota exceeded for the Gemini models, resets in 3h\n"),
            "RESOURCE_EXHAUSTED": ("", 'AGY_ERROR: {"status": "RESOURCE_EXHAUSTED"}\n'),
            "RESOURCE_EXHAUSTED et 429, sans retryable": (
                "",
                'AGY_ERROR: {"short_error":"You have exhausted your quota on this model.","status":"RESOURCE_EXHAUSTED","error_code":429,"code_kind":"http"}\n',
            ),
            "retryable: false malgré « rate limit » et 429": (
                "",
                'AGY_ERROR: {"short_error":"Rate limit exceeded","status":"UNAVAILABLE","error_code":429,"code_kind":"http","retryable":false}\n',
            ),
            "retryable: false malgré « Too Many Requests » dans le JSON": (
                _sortie(status="ERROR", error="Too Many Requests"),
                'AGY_ERROR: {"short_error":"Too Many Requests","status":"UNAVAILABLE","retryable":false}\n',
            ),
            "AGY_ERROR mesuré, clé refusée": ("", _AGY_ERROR_MESURE + "\n"),
            "identifiant": ("", "Error: request req_84291 failed (ref err_4290b)\n"),
        }
        for nom, (stdout, stderr) in cas.items():
            with self.subTest(nom):
                fake = _FakePopen(stdout=stdout, returncode=3, stderr=stderr)
                with self.assertRaises(antigravity._AntigravityCallError) as cm:
                    self._traduire(fake)
                self.assertFalse(cm.exception.rate_limited)
                self.faux_sommeil.assert_not_called()

    def test_gives_up_after_the_last_attempt(self):
        echecs = [
            _FakePopen(stdout="", returncode=3, stderr="HTTP 429 Too Many Requests\n")
            for _ in range(3)
        ]
        sequence = _Sequence(*echecs)
        with self.assertRaises(antigravity._AntigravityCallError) as cm:
            self._traduire(sequence, appels=3)
        self.assertTrue(cm.exception.rate_limited)
        self.assertEqual([c.args for c in self.faux_sommeil.call_args_list], [(1.0,), (2.0,)])

    def test_disconnected_session_asks_to_log_in_without_retry(self):
        cas = {
            "stderr": {
                "stdout": "",
                "returncode": 1,
                "stderr": "Authentication required: open the URL to sign in\n",
            },
            "champ error": {
                "stdout": _sortie(status="ERROR", error="Not logged in"),
                "returncode": 3,
            },
            "stdout illisible": {"stdout": "Authentication failed or timed out\n", "returncode": 1},
        }
        for nom, kwargs in cas.items():
            with self.subTest(nom):
                fake = _FakePopen(**kwargs)
                with self.assertRaises(antigravity._AntigravityCallError) as cm:
                    self._traduire(fake)
                message = str(cm.exception)
                self.assertIn("lancer `agy`", message)
                self.assertIn("se connecter", message)
                self.assertFalse(cm.exception.rate_limited)
                self.faux_sommeil.assert_not_called()

    def test_timeout_kills_the_group_and_names_agy_timeout(self):
        fake = _FakePopen(timeout=True)
        client = _client(timeout=7)
        with (
            patch.object(os, "getpgid", return_value=_PID_INEXISTANT) as getpgid,
            patch.object(os, "killpg") as killpg,
            self.assertRaises(RuntimeError) as cm,
        ):
            self._traduire(fake, client=client)
        self.assertIn("Antigravity CLI timeout après 7s", str(cm.exception))
        self.assertIn("AGY_TIMEOUT", str(cm.exception))
        getpgid.assert_called_once_with(fake.pid)
        self.assertEqual(
            [c.args for c in killpg.call_args_list],
            [(_PID_INEXISTANT, signal.SIGTERM), (_PID_INEXISTANT, signal.SIGKILL)],
        )
        self.assertEqual(fake.communicate_kwargs["timeout"], 7)
        self.assertFalse(os.path.exists(fake.photo.base))
        self.faux_sommeil.assert_not_called()

    def test_interruption_kills_the_group_and_removes_the_private_dir(self):
        """Ctrl-C ou SystemExit pendant une traduction : l'agent, dans sa
        propre session, ne reçoit pas le SIGINT du terminal. Son groupe est tué
        avant que l'interruption remonte, et le répertoire privé — journal
        compris — est effacé."""
        for interruption in (KeyboardInterrupt(), SystemExit(143)):
            with self.subTest(interruption=type(interruption).__name__):
                fake = _FakePopen()
                fake.communicate = MagicMock(side_effect=interruption)
                with (
                    patch.object(os, "getpgid", return_value=_PID_INEXISTANT) as getpgid,
                    patch.object(os, "killpg") as killpg,
                    self.assertRaises(type(interruption)),
                ):
                    self._traduire(fake)
                getpgid.assert_called_once_with(fake.pid)
                self.assertEqual(
                    [c.args for c in killpg.call_args_list],
                    [(_PID_INEXISTANT, signal.SIGTERM), (_PID_INEXISTANT, signal.SIGKILL)],
                )
                self.assertFalse(os.path.exists(fake.photo.base))
                self.faux_sommeil.assert_not_called()


class TestAntigravityRateLimitDetection(unittest.TestCase):
    def test_real_rate_limits_are_recognised(self):
        for texte in (
            "Rate limit exceeded",
            '{"reason": "RATE_LIMIT_EXCEEDED"}',
            "HTTP 429 Too Many Requests",
            "status 429: slow down",
            '{"code": 429}',
            "too many requests",
        ):
            with self.subTest(texte=texte):
                self.assertTrue(antigravity._antigravity_is_rate_limited(texte))

    def test_quota_exhaustion_and_429_inside_identifiers_are_not(self):
        for texte in (
            "Quota exceeded for this model",
            "RESOURCE_EXHAUSTED",
            "ref err_84290b",
            "request req_4291",
            "model foo429bar missing",
            "429TooMany",
            "error code 1429",
            "",
            None,
        ):
            with self.subTest(texte=texte):
                self.assertFalse(antigravity._antigravity_is_rate_limited(texte))

    def test_boolean_retryable_decides_alone(self):
        """C'est agy qui sait : `retryable` l'emporte sur tout marqueur."""
        cas = (
            ("", {"retryable": True}, True),
            ("Rate limit exceeded, HTTP 429", {"retryable": False}, False),
            ("quota exhausted", {"status": "RESOURCE_EXHAUSTED", "retryable": True}, True),
        )
        for texte, agy_error, attendu in cas:
            with self.subTest(texte=texte, agy_error=agy_error):
                self.assertIs(antigravity._antigravity_is_rate_limited(texte, agy_error), attendu)

    def test_non_boolean_retryable_leaves_it_to_the_markers(self):
        """Seul le booléen documenté décide : `"true"` ou `1` n'engagent pas
        une relance, `"false"` n'en empêche pas une."""
        cas = (
            ({"retryable": "true"}, False),
            ({"retryable": 1}, False),
            ({"retryable": None, "short_error": "Rate limit exceeded"}, True),
            ({"retryable": "false", "short_error": "Too many requests"}, True),
        )
        for agy_error, attendu in cas:
            with self.subTest(agy_error=agy_error):
                self.assertIs(antigravity._antigravity_is_rate_limited("", agy_error), attendu)

    def test_markers_are_also_looked_up_in_agy_error(self):
        for agy_error in (
            {"error_code": 429},
            {"short_error": "Rate limit exceeded"},
            {"reason": "RATE_LIMIT_EXCEEDED"},
        ):
            with self.subTest(agy_error=agy_error):
                self.assertIs(antigravity._antigravity_is_rate_limited("échec", agy_error), True)

    def test_exhaustion_anywhere_prevents_the_retry(self):
        cas = (
            ("HTTP 429 Too Many Requests", {"status": "RESOURCE_EXHAUSTED"}),
            ("You have exhausted your quota on this model. (429)", None),
            ("échec", {"short_error": "quota exhausted", "error_code": 429}),
        )
        for texte, agy_error in cas:
            with self.subTest(texte=texte, agy_error=agy_error):
                self.assertIs(antigravity._antigravity_is_rate_limited(texte, agy_error), False)


class TestAntigravityAgyError(unittest.TestCase):
    """La ligne `AGY_ERROR: {…}` de stderr (agy ≥ 1.2.6), lue par
    `raw_decode` : l'objet s'arrête là où il se termine."""

    def test_measured_line_is_decoded_then_compacted(self):
        stderr = f"error: agent executor error: API key not valid\n{_AGY_ERROR_MESURE}\n"
        data = antigravity._antigravity_agy_error_data(stderr)
        self.assertEqual((data["status"], data["error_code"]), ("INVALID_ARGUMENT", 400))
        self.assertIs(data["retryable"], False)
        compacte = antigravity._antigravity_agy_error(stderr)
        self.assertEqual(compacte, json.dumps(data, ensure_ascii=False)[:300])
        self.assertEqual(len(compacte), 300)

    def test_what_follows_the_object_is_left_out(self):
        """Une capture gourmande `\\{.*\\}` ramassait le code couleur et le
        « } » écrits après l'objet, puis échouait à le décoder."""
        attendu = {"status": "UNAVAILABLE", "retryable": True}
        for ligne in (
            'AGY_ERROR: {"status": "UNAVAILABLE", "retryable": true}\x1b[0m }',
            '\x1b[31mAGY_ERROR: {"status": "UNAVAILABLE", "retryable": true}\x1b[0m',
            'AGY_ERROR:{"status": "UNAVAILABLE", "retryable": true} }}',
        ):
            with self.subTest(ligne=ligne):
                stderr = f"avant\n{ligne}\naprès\n"
                self.assertEqual(antigravity._antigravity_agy_error_data(stderr), attendu)

    def test_unreadable_or_non_object_content_is_kept_raw(self):
        cas = {
            "AGY_ERROR: {pas du json}": {"message": "{pas du json}"},
            "AGY_ERROR: " + "x" * 400: {"message": "x" * 300},
            "AGY_ERROR: 42": {"message": "42"},
            'AGY_ERROR: "surcharge"': {"message": "surcharge"},
            "AGY_ERROR: [1, 2]": {"message": "[1, 2]"},
        }
        for ligne, attendu in cas.items():
            with self.subTest(ligne=ligne[:40]):
                self.assertEqual(antigravity._antigravity_agy_error_data(ligne + "\n"), attendu)

    def test_first_line_wins_and_absence_gives_nothing(self):
        stderr = 'AGY_ERROR: {"n": 1}\nAGY_ERROR: {"n": 2}\n'
        self.assertEqual(antigravity._antigravity_agy_error_data(stderr), {"n": 1})
        for stderr in ("", None, "error: sans ligne structurée\n", "AGY_ERROR sans deux-points\n"):
            with self.subTest(stderr=stderr):
                self.assertIsNone(antigravity._antigravity_agy_error_data(stderr))
                self.assertEqual(antigravity._antigravity_agy_error(stderr), "")


class TestAntigravityPreflight(_AgyTestCase):
    def _preflight(self, run):
        with patch.object(subprocess, "run", run):
            try:
                antigravity._antigravity_preflight(_BINAIRE)
            finally:
                self.assertGreaterEqual(run.calls, 1, "le double de subprocess.run n'a pas servi")

    def test_missing_binary_names_agy_bin_and_the_install_page(self):
        run = MagicMock(name="run", side_effect=_NE_DOIT_PAS_SERVIR)
        with patch.object(subprocess, "run", run), self.assertRaises(ValueError) as cm:
            antigravity._antigravity_preflight(None)
        for indice in ("introuvable", "AGY_BIN", "https://antigravity.google/docs/cli/install/"):
            self.assertIn(indice, str(cm.exception))
        run.assert_not_called()

    def test_measured_configuration_passes_with_two_isolated_checks(self):
        run = _FakeRun()
        with patch.dict(os.environ, _ENV_UTILISATEUR, clear=True):
            self._preflight(run)
        version, config = run.appels
        self.assertEqual(version.argv, [_BINAIRE, "--version"])
        journal = config.argv[config.argv.index("--log-file") + 1]
        self.assertEqual(
            config.argv,
            [_BINAIRE, "-p", "/config", "--output-format", "json", "--log-file", journal],
        )
        self.assertEqual(os.path.dirname(journal), config.photo.base)
        for appel in run.appels:
            with self.subTest(commande=appel.argv[1:3]):
                kwargs = appel.kwargs
                # Sans terminal de contrôle, une session déconnectée ne peut pas
                # y demander de code de connexion.
                self.assertTrue(kwargs["start_new_session"])
                self.assertEqual(kwargs["stdin"], subprocess.DEVNULL)
                self.assertTrue(kwargs["capture_output"])
                self.assertIs(kwargs["check"], False)
                self._assert_env_isole(kwargs["env"], appel.photo)
                self.assertEqual(appel.photo.mode, 0o700)
                self.assertEqual(appel.photo.fichiers, [])
                self.assertFalse(os.path.exists(appel.photo.base))

    def test_config_timeout_outlasts_the_login_wait(self):
        """Déconnecté, `agy -p /config` attend 60 s un code de connexion avant
        d'échouer : un plafond plus court changerait le message de connexion
        en timeout."""
        run = _FakeRun()
        self._preflight(run)
        self.assertGreater(run.appels[1].kwargs["timeout"], 60)

    def test_a_signal_during_a_check_cleans_the_private_dir(self):
        """Un SIGTERM ou un SIGHUP reçu pendant `agy --version` ou `/config` :
        le gestionnaire commun lève SystemExit, `subprocess.run` tuerait agy,
        et le répertoire privé — journal compris, qui porte l'adresse du
        compte — est effacé en remontant. Sans le correctif, Python mourait
        sans nettoyage. Le gestionnaire est APPELÉ, pas déclenché par un vrai
        signal : sans lui, un vrai SIGTERM tuerait le lanceur de tests."""
        signums = [signal.SIGTERM]
        if hasattr(signal, "SIGHUP") and signal.getsignal(signal.SIGHUP) is not signal.SIG_IGN:
            signums.append(signal.SIGHUP)
        for signum in signums:
            with self.subTest(signal=signum):
                avant = signal.getsignal(signum)
                repertoires = []

                def run(argv, _signum=signum, _vus=repertoires, **kwargs):
                    _vus.append(kwargs["cwd"])
                    gestionnaire = signal.getsignal(_signum)
                    self.assertTrue(callable(gestionnaire), "aucun gestionnaire posé")
                    gestionnaire(_signum, None)
                    raise AssertionError("le gestionnaire n'a pas interrompu le contrôle")

                with patch.object(subprocess, "run", run), self.assertRaises(SystemExit) as cm:
                    antigravity._antigravity_check_version(_BINAIRE)
                self.assertEqual(cm.exception.code, 128 + signum)
                self.assertEqual(len(repertoires), 1)
                self.assertFalse(
                    os.path.exists(os.path.dirname(repertoires[0])),
                    "répertoire privé resté sur le disque",
                )
                self.assertEqual(signal.getsignal(signum), avant)

    def test_version_reading_stays_linear_and_refuses_oversized_numbers(self):
        """`(\\d+)\\.(\\d+)\\.(\\d+)` non ancré retentait à chaque position d'une
        longue suite de chiffres : 1,7 s mesurée sur 20 000 chiffres (Sonar
        S8786). Bornée, la lecture reste immédiate, et un numéro trop long
        échoue en fermé au lieu d'être lu tronqué."""
        regex = antigravity._ANTIGRAVITY_VERSION_REGEX
        chiffres = "1" * 20_000
        debut = time.monotonic()
        trouve = regex.search(chiffres)
        duree = time.monotonic() - debut
        self.assertIsNone(trouve)
        self.assertLess(duree, 0.5)
        self.assertIsNone(regex.search("1234567890.1.1"))
        self.assertEqual(regex.search("agy 1.2.11 (linux/amd64)").groups(), ("1", "2", "11"))

    def test_versions_from_the_floor_up_are_accepted(self):
        # 1.10.0 : comparaison numérique, qu'une comparaison de chaînes inverserait.
        for version in ("1.2.11", "1.3.0", "1.10.0", "2.0.0", "agy 1.2.11 (linux/amd64)"):
            with self.subTest(version=version):
                run = _FakeRun(version=version + "\n")
                self._preflight(run)
                self.assertEqual(run.calls, 2)

    def test_versions_below_the_floor_are_refused_before_config(self):
        """Avant la 1.2.11, un agent de projet pouvait rester introuvable en
        mode headless — donc remplacé en silence par l'agent de codage."""
        for version in ("1.2.10", "1.1.2", "0.99.99"):
            with self.subTest(version=version):
                run = _FakeRun(version=version + "\n")
                with self.assertRaises(ValueError) as cm:
                    self._preflight(run)
                message = str(cm.exception)
                self.assertIn(f"agy {version} est trop ancien", message)
                self.assertIn("1.2.11", message)
                self.assertIn("agy update", message)
                self.assertEqual(run.calls, 1)

    def test_unreadable_or_failing_version_is_refused(self):
        cas = {
            "code 0 sans numéro": (
                _FakeRun(version="usage: agy [flags]\n"),
                r"a échoué \(code 0\)",
            ),
            "code non nul": (
                _FakeRun(version="", version_rc=2, version_stderr="boom\n"),
                r"a échoué \(code 2\) : boom",
            ),
        }
        for nom, (run, motif) in cas.items():
            with self.subTest(nom):
                with self.assertRaisesRegex(ValueError, motif):
                    self._preflight(run)
                self.assertEqual(run.calls, 1)

    def test_unexecutable_binary_is_reported(self):
        # TimeoutExpired est une classe d'exception, pas un lancement de process.
        # nosemgrep
        expiration = subprocess.TimeoutExpired(cmd=_BINAIRE, timeout=30)
        for erreur in (OSError("Permission denied"), expiration):
            with self.subTest(erreur=type(erreur).__name__):
                run = MagicMock(side_effect=erreur)
                with (
                    patch.object(subprocess, "run", run),
                    self.assertRaisesRegex(ValueError, "Impossible d'exécuter"),
                ):
                    antigravity._antigravity_preflight(_BINAIRE)
                run.assert_called_once()

    def test_paid_settings_are_refused_and_named(self):
        """Un réglage ABSENT compte comme un problème, pour chacun des trois :
        une version d'agy qui le renommerait ne doit pas faire passer un
        contrôle qui n'a rien vérifié. Pour useG1Credits, seul le booléen
        `false` passe ; pour gcp, seul `null`."""
        cas = {
            "crédits IA payants": ({"useG1Credits": True}, "useG1Credits=True : doit valoir false"),
            "crédits nuls": ({"useG1Credits": None}, "useG1Credits=None : doit valoir false"),
            "crédits à zéro": ({"useG1Credits": 0}, "useG1Credits=0 : doit valoir false"),
            "crédits en chaîne": (
                {"useG1Credits": "false"},
                "useG1Credits='false' : doit valoir false",
            ),
            "crédits absents": (
                {"useG1Credits": _ABSENT},
                "useG1Credits='(absent de /config)' : doit valoir false",
            ),
            "clé API": ({"modelProvider": "gemini"}, "modelProvider='gemini' : doit être vide"),
            "fournisseur absent": (
                {"modelProvider": _ABSENT},
                "modelProvider='(absent de /config)' : doit être vide",
            ),
            "projet Google Cloud": (
                {"gcp": {"project": "projet-facture"}},
                "gcp={'project': 'projet-facture'} : doit être nul",
            ),
            "projet vide": ({"gcp": {}}, "gcp={} : doit être nul"),
            "projet absent": ({"gcp": _ABSENT}, "gcp='(absent de /config)' : doit être nul"),
        }
        for nom, (reglage, attendu) in cas.items():
            with self.subTest(nom):
                config = {
                    cle: valeur
                    for cle, valeur in {**_CONFIG_MESUREE, **reglage}.items()
                    if valeur is not _ABSENT
                }
                run = _FakeRun(config=config)
                with self.assertRaises(ValueError) as cm:
                    self._preflight(run)
                message = str(cm.exception)
                self.assertIn("--use_antigravity refuse de traduire", message)
                self.assertIn(attendu, message)
                # Seul le réglage fautif : les deux autres, mesurés, passent.
                self.assertEqual(message.count("\n  - "), 1)
                self.assertEqual(run.calls, 2)

    def test_every_problem_is_listed_at_once(self):
        run = _FakeRun(
            config={"useG1Credits": True, "modelProvider": "gemini", "gcp": {"project": "p"}},
            journal=_journal(agent=None, auth="gemini_api_key"),
        )
        with self.assertRaises(ValueError) as cm:
            self._preflight(run)
        message = str(cm.exception)
        for attendu in (
            "useG1Credits=True",
            "modelProvider='gemini'",
            "gcp={'project': 'p'}",
            "gemini_api_key",
        ):
            self.assertIn(attendu, message)
        self.assertEqual(message.count("\n  - "), 4)

    def test_empty_config_names_each_missing_setting(self):
        run = _FakeRun(config={})
        with self.assertRaises(ValueError) as cm:
            self._preflight(run)
        message = str(cm.exception)
        self.assertEqual(message.count("(absent de /config)"), 3)
        self.assertEqual(message.count("\n  - "), 3)

    def test_preflight_log_must_attest_the_subscription(self):
        cas = {
            "clé API": (_journal(agent=None, auth="gemini_api_key"), "gemini_api_key"),
            "aucune méthode": (_journal(agent=None, auth=None), "ne dit pas par quel compte"),
            "journal absent": (None, "ne dit pas par quel compte"),
        }
        for nom, (journal, attendu) in cas.items():
            with self.subTest(nom):
                run = _FakeRun(journal=journal)
                with self.assertRaises(ValueError) as cm:
                    self._preflight(run)
                self.assertIn(attendu, str(cm.exception))
                self.assertIn("--use_antigravity refuse de traduire", str(cm.exception))

    def test_unreadable_config_is_refused(self):
        cas = {
            "stdout non JSON": _FakeRun(config_stdout="pas du json"),
            "JSON sans command": _FakeRun(config_stdout=json.dumps({"status": "SUCCESS"})),
            "config non objet": _FakeRun(config_stdout=_sortie_config("useG1Credits=false")),
            "code non nul malgré une config lisible": _FakeRun(config_rc=1),
        }
        for nom, run in cas.items():
            with (
                self.subTest(nom),
                self.assertRaisesRegex(ValueError, "Lecture de la configuration d'agy impossible"),
            ):
                self._preflight(run)

    def test_disconnected_session_in_preflight_says_to_log_in(self):
        """Le conseil nomme aussi le trousseau : sans lui, agy range son jeton
        dans un fichier de ~/.gemini que l'isolation masque."""
        cas = {
            "stderr": _FakeRun(
                config_rc=1, config_stdout="", config_stderr="Authentication required\n"
            ),
            "champ error": _FakeRun(
                config_rc=1, config_stdout=json.dumps({"error": "not logged in"})
            ),
        }
        for nom, run in cas.items():
            with self.subTest(nom):
                with self.assertRaises(ValueError) as cm:
                    self._preflight(run)
                self.assertEqual(str(cm.exception), antigravity.ANTIGRAVITY_LOGIN_HINT)
                for indice in ("lancer `agy`", "trousseau", "~/.gemini"):
                    self.assertIn(indice, str(cm.exception))


class TestAntigravityInit(unittest.TestCase):
    """Chaque initialisation neutralise la vérification de plateforme : les
    runners GitHub n'ont pas de bus de session, et sans ce patch le test
    serait vert ici et rouge en CI. Chaque test vérifie que le patch a mordu."""

    def _init(self, args, binaire=_BINAIRE):
        """Initialise hors CI, plateforme, binaire et préflight remplacés ;
        renvoie (client, stderr). Les trois doubles doivent avoir servi : un
        patch mort lancerait `agy --version` et `agy -p /config` pour de vrai."""
        with (
            patch.dict(os.environ, _HORS_CI),
            patch.object(antigravity, "_antigravity_check_platform") as plateforme,
            patch.object(
                antigravity, "_resolve_antigravity_binary", return_value=binaire
            ) as resoudre,
            patch.object(antigravity, "_antigravity_preflight") as preflight,
            patch("sys.stderr", new_callable=io.StringIO) as capture,
        ):
            client = antigravity._init_antigravity_client(args)
        plateforme.assert_called_once_with()
        resoudre.assert_called_once_with()
        preflight.assert_called_once_with(binaire)
        return client, capture.getvalue()

    def _refus(self, args, env=None, plateforme_consultee=True):
        """Initialisation qui doit échouer AVANT de chercher le binaire ; la
        plateforme n'est pas consultée quand la CI refuse la première."""
        with (
            patch.dict(os.environ, env or _HORS_CI),
            patch.object(antigravity, "_antigravity_check_platform") as plateforme,
            patch.object(
                antigravity, "_resolve_antigravity_binary", return_value=_BINAIRE
            ) as resoudre,
            patch.object(antigravity, "_antigravity_preflight") as preflight,
            patch("sys.stderr", new_callable=io.StringIO),
            self.assertRaises(ValueError) as cm,
        ):
            antigravity._init_antigravity_client(args)
        self.assertEqual(plateforme.call_count, 1 if plateforme_consultee else 0)
        resoudre.assert_not_called()
        preflight.assert_not_called()
        return str(cm.exception)

    def test_default_and_eco_models(self):
        args = _args(model=None)
        client, _ = self._init(args)
        self.assertEqual(args.model, antigravity.DEFAULT_MODEL_ANTIGRAVITY)
        self.assertEqual((client.binary, client.timeout), (_BINAIRE, antigravity.AGY_TIMEOUT))
        eco = _args(model=None, eco=True)
        self._init(eco)
        self.assertEqual(eco.model, antigravity.ECO_MODEL_ANTIGRAVITY)

    def test_defaults_are_the_campaign_choices(self):
        """Fixés par les mesures du 2026-09-26 : 3.8 Flash medium rend la même
        structure que 3.7 Flash medium pour un septième de quota en plus ;
        3.7 Flash low reste le palier éco, 3.8 low cassant des liens internes
        que 3.7 low laissait intacts. Les changer est une décision, pas un
        détail."""
        self.assertEqual(antigravity.DEFAULT_MODEL_ANTIGRAVITY, "gemini-3.8-flash-medium")
        self.assertEqual(antigravity.ECO_MODEL_ANTIGRAVITY, "gemini-3.7-flash-low")

    def test_defaults_are_catalogue_identifiers_on_the_gemini_quota(self):
        """Des identifiants d'`agy models`, effort compris, hors du petit quota
        « Claude and GPT models »."""
        for modele in (antigravity.DEFAULT_MODEL_ANTIGRAVITY, antigravity.ECO_MODEL_ANTIGRAVITY):
            with self.subTest(modele=modele):
                self.assertIn(modele, _CATALOGUE_AGY)
                _, avertissements = self._init(_args(model=modele))
                self.assertNotIn("Claude and GPT models", avertissements)

    def test_explicit_model_wins_over_eco(self):
        args = _args(model="gemini-3.1-pro-high", eco=True)
        self._init(args)
        self.assertEqual(args.model, "gemini-3.1-pro-high")

    def test_refused_in_ci_with_the_google_fallback(self):
        for env in ({"CI": "true", "GITHUB_ACTIONS": ""}, {"CI": "", "GITHUB_ACTIONS": "true"}):
            with self.subTest(env=env):
                message = self._refus(_args(model=None), env=env, plateforme_consultee=False)
                for attendu in ("--use_antigravity", "CI", "GOOGLE_API_KEY", "--use_gemini"):
                    self.assertIn(attendu, message)
                self.assertNotIn("OPENAI_API_KEY", message)
                self.assertNotIn("ChatGPT", message)

    def test_ci_refusal_comes_before_the_platform_check(self):
        """Sur un runner, sans bus de session par nature, c'est la CI qu'on
        nomme : la vraie vérification de plateforme n'interroge même pas le
        bus."""
        args = _args(model=None)
        with (
            patch.dict(os.environ, {"CI": "true", "GITHUB_ACTIONS": ""}),
            patch.object(sys, "platform", "linux"),
            patch.object(
                antigravity, "_antigravity_session_bus_reachable", return_value=False
            ) as bus,
            self.assertRaises(ValueError) as cm,
        ):
            antigravity._init_antigravity_client(args)
        self.assertIn("refusé en environnement CI", str(cm.exception))
        bus.assert_not_called()

    def test_platform_refusal_comes_before_any_binary_lookup_or_subprocess(self):
        cas = {
            "Windows": (
                (patch.object(os, "name", "nt"),),
                antigravity.ANTIGRAVITY_UNSUPPORTED_WINDOWS,
            ),
            "Linux sans bus de session": (
                (
                    patch.object(sys, "platform", "linux"),
                    patch.object(
                        antigravity, "_antigravity_session_bus_reachable", return_value=False
                    ),
                ),
                antigravity.ANTIGRAVITY_NO_SESSION_BUS,
            ),
        }
        for nom, (plateforme, attendu) in cas.items():
            with self.subTest(nom):
                run = MagicMock(name="run", side_effect=_NE_DOIT_PAS_SERVIR)
                popen = MagicMock(name="Popen", side_effect=_NE_DOIT_PAS_SERVIR)
                args = _args(model=None)
                with contextlib.ExitStack() as pile:
                    pile.enter_context(patch.dict(os.environ, _HORS_CI))
                    for simulation in plateforme:
                        pile.enter_context(simulation)
                    resoudre = pile.enter_context(
                        patch.object(antigravity, "_resolve_antigravity_binary")
                    )
                    pile.enter_context(patch.object(subprocess, "run", run))
                    pile.enter_context(patch.object(subprocess, "Popen", popen))
                    erreur = pile.enter_context(self.assertRaises(ValueError))
                    antigravity._init_antigravity_client(args)
                self.assertEqual(str(erreur.exception), attendu)
                resoudre.assert_not_called()
                run.assert_not_called()
                popen.assert_not_called()

    def test_malformed_model_is_refused_before_any_launch(self):
        """Une valeur commençant par « - » serait relue comme un drapeau par
        le parseur d'argv d'agy."""
        for modele in (
            "-gemini-3.7-flash-low",
            "--help",
            "google/gemini-3.7-flash-low",
            "gemini 3.7 flash",
            "../agy",
            "gemini-3.7-flash-low;ls",
        ):
            with self.subTest(modele=modele):
                message = self._refus(_args(model=modele))
                self.assertIn("invalide", message)
                self.assertIn("agy models", message)

    def test_base_name_without_effort_suggests_catalogue_identifiers(self):
        """agy refuse un nom de base : l'effort fait partie de l'identifiant.
        Les deux suggestions existent au catalogue — un Pro n'a pas d'effort
        `-medium`, qu'agy refuserait à son tour."""
        cas = {
            "gemini-3.7-flash": ("-medium", "-low"),
            "gemini-3.8-flash": ("-medium", "-low"),
            "gemini-3.6-flash": ("-medium", "-low"),
            "gemini-3.1-pro": ("-high", "-low"),
        }
        for modele, efforts in cas.items():
            with self.subTest(modele=modele):
                message = self._refus(_args(model=modele))
                self.assertIn("incomplet", message)
                suggestions = re.findall(re.escape(modele) + r"-[a-z]+", message)
                self.assertCountEqual(suggestions, [modele + effort for effort in efforts])
                for suggestion in suggestions:
                    self.assertIn(suggestion, _CATALOGUE_AGY)

    def test_every_catalogue_identifier_is_accepted(self):
        for modele in _CATALOGUE_AGY:
            with self.subTest(modele=modele):
                antigravity._antigravity_check_model(modele)

    def test_reasoning_effort_warns_that_it_has_no_effect(self):
        _, avertissements = self._init(_args(reasoning_effort="high"))
        self.assertIn("--reasoning_effort est sans effet", avertissements)
        _, avertissements = self._init(_args(reasoning_effort=None))
        self.assertNotIn("--reasoning_effort", avertissements)
        # Un Namespace construit à la main, sans l'attribut, ne casse rien.
        _, avertissements = self._init(Namespace(model="gemini-3.7-flash-low", eco=False))
        self.assertEqual(avertissements, "")

    def test_claude_and_gpt_models_warn_about_their_smaller_quota(self):
        """Mesuré : environ 1 % de la fenêtre de 5 heures par appel, contre
        0,05 % en Flash."""
        for modele in ("claude-sonnet-4-6", "claude-opus-4-6-thinking", "gpt-oss-120b-medium"):
            with self.subTest(modele=modele):
                _, avertissements = self._init(_args(model=modele))
                self.assertIn("Claude and GPT models", avertissements)
                self.assertIn(modele, avertissements)
        _, avertissements = self._init(_args(model="gemini-3.8-flash-low"))
        self.assertNotIn("Claude and GPT models", avertissements)

    def test_missing_binary_stops_before_any_subprocess(self):
        run = MagicMock(name="run", side_effect=_NE_DOIT_PAS_SERVIR)
        args = _args(model=None)
        with (
            patch.dict(os.environ, _HORS_CI),
            patch.object(antigravity, "_antigravity_check_platform") as plateforme,
            patch.object(antigravity, "_resolve_antigravity_binary", return_value=None) as resoudre,
            patch.object(subprocess, "run", run),
            self.assertRaisesRegex(ValueError, "introuvable"),
        ):
            antigravity._init_antigravity_client(args)
        plateforme.assert_called_once_with()
        resoudre.assert_called_once_with()
        run.assert_not_called()

    def test_init_runs_the_real_platform_check_and_preflight_against_doubles(self):
        """Chaîne complète init → plateforme → préflight → `subprocess.run` :
        seuls le binaire et la sonde du bus de session sont remplacés."""
        run = _FakeRun()
        with (
            patch.dict(os.environ, _HORS_CI),
            patch.object(sys, "platform", "linux"),
            patch.object(
                antigravity, "_antigravity_session_bus_reachable", return_value=True
            ) as bus,
            patch.object(antigravity, "_resolve_antigravity_binary", return_value=_BINAIRE),
            patch.object(subprocess, "run", run),
        ):
            client = antigravity._init_antigravity_client(_args(model=None))
        bus.assert_called_once_with()
        self.assertEqual(run.calls, 2)
        self.assertEqual(client.binary, _BINAIRE)


class TestAntigravityPlatform(unittest.TestCase):
    """Refus en fermé là où l'isolation ne tient pas, AVANT tout lancement
    d'agy. Sans bus de session, agy range son jeton dans un fichier de
    ~/.gemini que le HOME privé masque, et attend 60 s un code de connexion
    (mesuré) ; sous Windows, il ne lit ni HOME ni TMPDIR."""

    def _verifier(self, env, plateforme="linux"):
        """La vraie vérification sous `sys.platform` = `plateforme`, les deux
        variables du bus réduites à celles de `env` ; le refus, ou None."""
        with (
            patch.dict(os.environ, env),
            patch.object(sys, "platform", plateforme),
            patch.object(os, "name", "posix"),
        ):
            for nom in ("DBUS_SESSION_BUS_ADDRESS", "XDG_RUNTIME_DIR"):
                if nom not in env:
                    os.environ.pop(nom, None)
            try:
                antigravity._antigravity_check_platform()
            except ValueError as e:
                return str(e)
        return None

    def _sonder_defaut(self, env, present):
        """(joignable, chemins sondés) sans DBUS_SESSION_BUS_ADDRESS, l'uid
        fixé à 4242 et `os.path.exists` remplacé par un témoin."""
        sondes = []

        def existe(chemin):
            sondes.append(chemin)
            return present

        with (
            patch.dict(os.environ, env),
            patch.object(os, "getuid", return_value=4242, create=True),
            patch.object(os.path, "exists", existe),
        ):
            os.environ.pop("DBUS_SESSION_BUS_ADDRESS", None)
            if "XDG_RUNTIME_DIR" not in env:
                os.environ.pop("XDG_RUNTIME_DIR", None)
            return antigravity._antigravity_session_bus_reachable(), sondes

    def test_windows_is_refused_before_any_bus_probe(self):
        with (
            patch.object(os, "name", "nt"),
            patch.object(sys, "platform", "win32"),
            patch.object(
                antigravity, "_antigravity_session_bus_reachable", return_value=True
            ) as bus,
            self.assertRaises(ValueError) as cm,
        ):
            antigravity._antigravity_check_platform()
        message = str(cm.exception)
        self.assertEqual(message, antigravity.ANTIGRAVITY_UNSUPPORTED_WINDOWS)
        for indice in ("Windows", "HOME", "TMPDIR"):
            self.assertIn(indice, message)
        bus.assert_not_called()

    def test_linux_requires_a_session_bus(self):
        refus = antigravity.ANTIGRAVITY_NO_SESSION_BUS
        with tempfile.TemporaryDirectory() as runtime:
            sans_bus = {"XDG_RUNTIME_DIR": runtime}
            adresse = "unix:path=/run/user/4242/bus"
            cas = (
                ("ni adresse ni socket", sans_bus, refus),
                ("adresse vide", {**sans_bus, "DBUS_SESSION_BUS_ADDRESS": ""}, refus),
                ("adresse explicite", {**sans_bus, "DBUS_SESSION_BUS_ADDRESS": adresse}, None),
            )
            for nom, env, attendu in cas:
                with self.subTest(nom):
                    self.assertEqual(self._verifier(env), attendu)
            # Sans adresse, la socket par défaut suffit : c'est celle que la
            # bibliothèque D-Bus essaie (mesuré : un `env -i` s'authentifie).
            with open(os.path.join(runtime, "bus"), "w", encoding="utf-8"):
                pass
            self.assertIsNone(self._verifier(sans_bus))
        for indice in (
            "DBUS_SESSION_BUS_ADDRESS",
            "$XDG_RUNTIME_DIR/bus",
            "trousseau",
            "~/.gemini",
        ):
            self.assertIn(indice, refus)

    def test_without_xdg_runtime_dir_the_default_socket_is_probed(self):
        """Sans XDG_RUNTIME_DIR, ou vide : /run/user/<uid>/bus."""
        for env in ({}, {"XDG_RUNTIME_DIR": ""}):
            for present in (True, False):
                with self.subTest(env=env, present=present):
                    joignable, sondes = self._sonder_defaut(env, present)
                    self.assertIs(joignable, present)
                    self.assertEqual(sondes, ["/run/user/4242/bus"])

    def test_macos_passes_without_a_session_bus(self):
        """Pas de D-Bus sous macOS : le trousseau est celui du système, et la
        garde de facturation lit la configuration effective."""
        with (
            patch.object(os, "name", "posix"),
            patch.object(sys, "platform", "darwin"),
            patch.object(
                antigravity, "_antigravity_session_bus_reachable", return_value=False
            ) as bus,
        ):
            antigravity._antigravity_check_platform()
        bus.assert_not_called()


class TestAntigravityBinaryResolution(unittest.TestCase):
    """AGY_BIN, puis le PATH, puis ~/.local/bin/agy ; jamais `antigravity`,
    le lanceur de l'IDE, qui ouvrirait l'éditeur. Toujours un chemin absolu :
    l'appel tourne dans le répertoire privé."""

    def _resoudre(self, agy_bin=None, sur_path=None, fichiers=()):
        """(binaire résolu, noms demandés à `which`) ; `which` et `isfile`
        simulés, HOME fixé pour que ~/.local/bin/agy soit prévisible."""
        demandes = []
        sur_path = sur_path or {}

        def which(nom):
            demandes.append(nom)
            return sur_path.get(nom)

        with (
            patch.dict(os.environ, {"HOME": _FAUX_HOME}),
            patch.object(shutil, "which", which),
            patch.object(os.path, "isfile", lambda chemin: chemin in fichiers),
        ):
            os.environ.pop("AGY_BIN", None)
            if agy_bin is not None:
                os.environ["AGY_BIN"] = agy_bin
            resolu = antigravity._resolve_antigravity_binary()
        return resolu, demandes

    _LOCAL = os.path.join(_FAUX_HOME, ".local", "bin", "agy")

    def test_explicit_agy_bin_path_wins(self):
        resolu, demandes = self._resoudre(
            agy_bin="/opt/agy/agy", sur_path={"agy": "/usr/bin/agy"}, fichiers={"/opt/agy/agy"}
        )
        self.assertEqual(resolu, "/opt/agy/agy")
        self.assertEqual(demandes, ["/opt/agy/agy"])

    def test_explicit_agy_bin_name_is_looked_up_in_path(self):
        resolu, _ = self._resoudre(agy_bin="agy-beta", sur_path={"agy-beta": "/usr/bin/agy-beta"})
        self.assertEqual(resolu, "/usr/bin/agy-beta")

    def test_missing_explicit_agy_bin_is_not_silently_replaced(self):
        """Le choix explicite de l'utilisateur n'est pas remplacé par un autre
        binaire, même présent dans le PATH ou dans ~/.local/bin."""
        resolu, demandes = self._resoudre(
            agy_bin="/absent/agy", sur_path={"agy": "/usr/bin/agy"}, fichiers={self._LOCAL}
        )
        self.assertIsNone(resolu)
        self.assertEqual(demandes, ["/absent/agy"])

    def test_empty_agy_bin_counts_as_unset(self):
        resolu, _ = self._resoudre(agy_bin="", sur_path={"agy": "/usr/bin/agy"})
        self.assertEqual(resolu, "/usr/bin/agy")

    def test_path_is_used_without_agy_bin(self):
        resolu, demandes = self._resoudre(sur_path={"agy": "/usr/local/bin/agy"})
        self.assertEqual(resolu, "/usr/local/bin/agy")
        self.assertEqual(demandes, ["agy"])

    def test_falls_back_to_the_installer_location(self):
        resolu, _ = self._resoudre(fichiers={self._LOCAL})
        self.assertEqual(resolu, self._LOCAL)

    def test_returns_none_when_nothing_is_available(self):
        resolu, _ = self._resoudre()
        self.assertIsNone(resolu)

    def test_the_ide_launcher_is_never_used(self):
        resolu, demandes = self._resoudre(sur_path={"antigravity": "/usr/bin/antigravity"})
        self.assertIsNone(resolu)
        self.assertNotIn("antigravity", demandes)

    def test_relative_paths_are_made_absolute(self):
        """Relatif au répertoire courant de l'appelant, pas à celui de l'appel."""
        relatif = os.path.join("outils", "agy")
        cas = {
            "AGY_BIN relatif, fichier présent": {"agy_bin": relatif, "fichiers": {relatif}},
            "AGY_BIN relatif, rendu tel quel par which": {
                "agy_bin": relatif,
                "sur_path": {relatif: relatif},
            },
            "répertoire relatif dans le PATH": {"sur_path": {"agy": relatif}},
        }
        for nom, reglages in cas.items():
            with self.subTest(nom):
                resolu, _ = self._resoudre(**reglages)
                self.assertEqual(resolu, os.path.join(os.getcwd(), "outils", "agy"))

    @unittest.skipUnless(os.name == "posix", "le faux agy est un script /bin/sh")
    def test_relative_agy_bin_is_found_from_the_private_dir(self):
        """Bout en bout, vrai sous-processus et FAUX agy écrit par le test :
        AGY_BIN relatif au répertoire courant, appel exécuté dans le
        répertoire privé. Avec le chemin relatif, Popen y cherchait le binaire
        et levait FileNotFoundError."""
        with tempfile.TemporaryDirectory() as dossier:
            temoins = {nom: os.path.join(dossier, nom) for nom in ("argv0", "cwd", "stdin", "env")}
            faux = os.path.join(dossier, "outils", "agy")
            os.mkdir(os.path.dirname(faux))
            with open(faux, "w", encoding="utf-8") as f:
                f.write(_script_faux_agy(temoins))
            # Marqueur sur la ligne qui PRÉCÈDE l'appel : posé sur l'appel, ruff-format
            # l'emportait sur la parenthèse fermante, où il ne couvre plus rien.
            # nosemgrep: python.lang.security.audit.insecure-file-permissions.insecure-file-permissions — 0700, propriétaire seul : faux agy de test, répertoire privé
            os.chmod(faux, 0o700)
            precedent = os.getcwd()
            os.chdir(dossier)
            try:
                with (
                    patch.dict(os.environ, {"AGY_BIN": os.path.join("outils", "agy")}),
                    patch("sys.stderr", new_callable=io.StringIO),
                ):
                    binaire = antigravity._resolve_antigravity_binary()
                    texte = antigravity._call_antigravity(
                        _client(binary=binaire), _args(), _PROMPT, _SEGMENT
                    )
            finally:
                os.chdir(precedent)
            self.assertTrue(os.path.isabs(binaire))
            self.assertTrue(os.path.samefile(binaire, faux))
            lus = {}
            for nom, chemin in temoins.items():
                with open(chemin, encoding="utf-8") as f:
                    lus[nom] = f.read()
        self.assertEqual(texte, _TRADUCTION)
        self.assertEqual(lus["argv0"], binaire)
        self.assertEqual(lus["stdin"], _SEGMENT)
        travail = lus["cwd"].strip()
        prive = os.path.dirname(travail)
        self.assertEqual(os.path.basename(travail), "work")
        self.assertTrue(os.path.basename(prive).startswith("translate-antigravity-"))
        self.assertFalse(os.path.exists(prive))
        env = dict(ligne.split("=", 1) for ligne in lus["env"].splitlines() if "=" in ligne)
        self.assertNotIn("AGY_BIN", env)
        self.assertEqual(env["AGY_CLI_DISABLE_AUTO_UPDATE"], "true")
        self.assertEqual(os.path.realpath(os.path.dirname(env["HOME"])), os.path.realpath(prive))


class TestAntigravityWiring(unittest.TestCase):
    def test_resolution_and_label(self):
        args = Namespace(use_antigravity=True)
        self.assertEqual(registry._resolve_provider_from_args(args), "antigravity")
        self.assertEqual(registry._resolve_provider(args), "antigravity")
        self.assertEqual(registry._PROVIDER_LABELS["antigravity"], "Antigravity CLI")

    def test_dispatch_routes_to_call_antigravity(self):
        args = _args()
        with patch.object(registry, "_call_antigravity", return_value=_REPONSE) as appel:
            texte = registry._dispatch_provider_call("client", args, "P", "S", "antigravity", False)
        self.assertEqual(texte, _REPONSE)
        appel.assert_called_once_with("client", args, "P", "S")

    def test_empty_content_guard_names_antigravity(self):
        args = _args()
        with (
            patch.object(registry, "_call_antigravity", return_value=" \n") as appel,
            self.assertRaisesRegex(RuntimeError, "Antigravity CLI returned empty content"),
        ):
            registry._dispatch_provider_call("client", args, "P", "S", "antigravity", False)
        appel.assert_called_once()

    def test_select_provider_client_routes_to_init(self):
        args = Namespace(
            use_mistral=False, use_claude=False, use_gemini=False, use_antigravity=True
        )
        with patch.object(registry, "_init_antigravity_client", return_value="client") as init:
            self.assertEqual(registry._select_provider_client(args), "client")
        init.assert_called_once_with(args)

    def test_flag_is_in_the_exclusive_group(self):
        parser = argparse.ArgumentParser()
        registry._add_provider_args(parser)
        self.assertTrue(parser.parse_args(["--use_antigravity"]).use_antigravity)
        self.assertFalse(parser.parse_args([]).use_antigravity)
        for autre in ("--use_codex", "--use_gemini", "--use_grok_cli", "--use_opencode"):
            with (
                self.subTest(autre=autre),
                patch("sys.stderr", new_callable=io.StringIO),
                self.assertRaises(SystemExit),
            ):
                parser.parse_args(["--use_antigravity", autre])

    def test_shared_cli_plumbing(self):
        """Le back-off commun ne voit que les `_CliCallError`, et le message de
        timeout cite la variable propre à chaque CLI."""
        self.assertEqual(base._CLI_TIMEOUT_ENV_VARS["Antigravity"], "AGY_TIMEOUT")
        self.assertTrue(issubclass(antigravity._AntigravityCallError, base._CliCallError))
        self.assertIn("antigravity", registry._CLI_PROVIDERS)

    def test_unknown_cli_provider_raises_instead_of_using_another_subscription(self):
        args = _args()
        with (
            patch.object(registry, "_call_antigravity") as appel_agy,
            patch.object(registry, "_call_codex") as appel_codex,
            patch.object(registry, "_call_grok_cli") as appel_grok,
            patch.object(registry, "_call_opencode") as appel_opencode,
            self.assertRaisesRegex(ValueError, "provider CLI inconnu : 'antigravite'"),
        ):
            registry._call_cli_provider("client", args, "P", "S", "antigravite")
        for double in (appel_agy, appel_codex, appel_grok, appel_opencode):
            double.assert_not_called()


class TestRunProcessCwd(unittest.TestCase):
    """agy n'a pas d'option de répertoire de travail : il prend le sien pour
    racine d'espace de travail, et c'est là qu'il cherche l'agent."""

    def test_cwd_is_passed_to_popen(self):
        fake = _FakePopen(stdout="sortie", journal=None)
        with patch.object(subprocess, "Popen", fake):
            resultat = base._codex_run_process(
                [_BINAIRE], "entrée", 5, {"PATH": "/usr/bin"}, "Antigravity", "m", cwd="/prive"
            )
        self.assertEqual(fake.calls, 1)
        self.assertEqual(fake.kwargs["cwd"], "/prive")
        self.assertEqual(resultat, (0, "sortie", ""))
        self.assertEqual(fake.communicate_kwargs, {"input": "entrée", "timeout": 5})

    def test_cwd_defaults_to_none(self):
        fake = _FakePopen(stdout="sortie", journal=None)
        with patch.object(subprocess, "Popen", fake):
            base._codex_run_process([_BINAIRE], "", 5, {}, "Codex", "m")
        self.assertEqual(fake.calls, 1)
        self.assertIsNone(fake.kwargs.get("cwd"))


class TestAntigravityTimeoutSetting(unittest.TestCase):
    def test_default_is_900_seconds_and_agy_timeout_overrides_it(self):
        """900 s par segment, démarrage d'agy compris. La valeur est lue à
        l'import du module : d'où un interpréteur neuf, sans `.env` à portée."""
        sonde = (
            "import importlib, os\n"
            "from aipmt.providers import antigravity\n"
            "print(antigravity.AGY_TIMEOUT)\n"
            "os.environ['AGY_TIMEOUT'] = '42'\n"
            "print(importlib.reload(antigravity).AGY_TIMEOUT)\n"
        )
        with tempfile.TemporaryDirectory() as dossier:
            env = _env_sans_agy(dossier)
            env.pop("AGY_TIMEOUT", None)
            env.update(PYTHONPATH=_SRC, XDG_CONFIG_HOME=dossier)
            argv = [sys.executable, "-c", sonde]
            # nosemgrep
            proc = subprocess.run(  # nosec B603 # nosemgrep — interpréteur courant, code littéral
                argv,  # nosemgrep
                cwd=dossier,
                env=env,
                capture_output=True,
                text=True,
                check=False,
                timeout=120,
            )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(proc.stdout.split()[-2:], ["900", "42"])


def _detecter(exporte=None, contenu_env=None):
    """Source regen_translations.sh dans un sous-shell et appelle
    detect_provider, dans un répertoire jetable (son `.env` éventuel compris) ;
    le sourçage ne lance pas main(). Renvoie (stdout, stderr, code)."""
    with tempfile.TemporaryDirectory() as dossier:
        if contenu_env is not None:
            with open(os.path.join(dossier, ".env"), "w", encoding="utf-8") as f:
                f.write(contenu_env)
        env = _env_sans_agy(dossier)
        for nom in (
            "REGEN_PROVIDER",
            "REGEN_MODEL",
            "REGEN_ALLOW_PAID_API",
            "OPENAI_API_KEY",
            "GOOGLE_API_KEY",
            "GEMINI_API_KEY",
        ):
            env.pop(nom, None)
        env.update(exporte or {})
        argv = ["bash", "-c", f'source "{_REGEN}"; detect_provider']
        # nosemgrep
        proc = subprocess.run(  # nosec B603 B607 # nosemgrep — wrapper bash local, sans agy
            argv,  # nosemgrep
            cwd=dossier,
            env=env,
            capture_output=True,
            text=True,
            check=False,
            timeout=60,
        )
    return proc.stdout.strip(), proc.stderr.strip(), proc.returncode


class TestRegenAntigravity(unittest.TestCase):
    """detect_provider() de regen_translations.sh : Antigravity est un chemin
    d'abonnement, autorisé sans REGEN_ALLOW_PAID_API comme Codex et Grok CLI —
    sur demande seulement : le défaut reste Codex et gpt-5.6-sol, décision du
    propriétaire."""

    # Aucune n'est une vraie clé : elles prouvent que leur présence ne change rien.
    _FAUSSE_CLE = "fixture-fausse-cle-google-ne-pas-utiliser"

    def test_antigravity_is_a_subscription_path_without_waiver(self):
        # REGEN_ALLOW_PAID_API est retiré de l'environnement par _detecter.
        stdout, stderr, rc = _detecter({"REGEN_PROVIDER": "antigravity"})
        self.assertEqual((rc, stdout), (0, "--use_antigravity"), stderr)
        self.assertIn("abonnement Google", stderr)

    def test_google_keys_in_dotenv_change_nothing(self):
        contenu = f"GOOGLE_API_KEY={self._FAUSSE_CLE}\nGEMINI_API_KEY={self._FAUSSE_CLE}\n"
        stdout, stderr, rc = _detecter({"REGEN_PROVIDER": "antigravity"}, contenu)
        self.assertEqual((rc, stdout), (0, "--use_antigravity"), stderr)

    def test_the_default_stays_codex(self):
        stdout, stderr, rc = _detecter()
        self.assertEqual((rc, stdout), (0, "--use_codex"), stderr)


if __name__ == "__main__":
    unittest.main()
