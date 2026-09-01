"""Résolution des clés d'API en trois couches, et lisibilité de l'échec.

Une CLI installée n'a pas le même contexte qu'un script lancé depuis son dépôt.
Deux défauts en découlaient, tous deux mesurés avant correction :

1. Il n'existait aucune configuration PERSISTANTE. Restaient la variable
   d'environnement et le `.env` du répertoire courant. `find_dotenv` remonte
   certes jusqu'à la racine du système et trouvait un `~/.env` quand on
   travaillait sous son répertoire personnel — mais rien quand on travaillait
   ailleurs. Cette couverture dépendait de l'endroit d'où l'on lançait la
   commande.
2. Sans clé, l'utilisateur recevait une TRACE D'APPEL Python pointant vers
   `site-packages`, un endroit où il n'a rien à faire, et le message ne disait
   pas où créer le fichier manquant.
"""

from __future__ import annotations

import inspect
import os
import subprocess  # nosec B404 — exerce le point d'entrée réel, cf. TestMissingKeyIsNotATraceback
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

# Vise `src/` et non la racine : le test importe ainsi le PAQUET, pas
# l'arbre source, et une erreur d'empaquetage devient visible.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from aipmt import translate

SRC_ROOT = Path(__file__).resolve().parents[1] / "src"


class TestUserConfigPathFollowsOsConvention(unittest.TestCase):
    """L'emplacement ne doit dépendre que de l'OS et de son environnement."""

    def test_absolute_xdg_config_home_is_honoured(self) -> None:
        with patch.dict(os.environ, {"XDG_CONFIG_HOME": "/opt/conf"}, clear=False):
            self.assertEqual(translate._user_config_path(), "/opt/conf/aipmt/.env")

    def test_relative_xdg_config_home_is_ignored(self) -> None:
        """La spécification XDG impose un chemin absolu et dit d'ignorer sinon.

        Sans ce contrôle, un `XDG_CONFIG_HOME` relatif ferait dépendre
        l'emplacement de la configuration du répertoire courant — exactement le
        défaut que cette couche existe pour supprimer.
        """
        with patch.dict(os.environ, {"XDG_CONFIG_HOME": "relatif/conf"}, clear=False):
            path = translate._user_config_path()
        self.assertTrue(os.path.isabs(path), f"{path!r} devrait être absolu")
        self.assertNotIn("relatif", path)
        self.assertTrue(path.endswith(os.path.join(".config", "aipmt", ".env")))

    def test_falls_back_to_dot_config_when_unset(self) -> None:
        env = {k: v for k, v in os.environ.items() if k != "XDG_CONFIG_HOME"}
        with patch.dict(os.environ, env, clear=True):
            path = translate._user_config_path()
        self.assertTrue(path.endswith(os.path.join(".config", "aipmt", ".env")))

    def test_windows_uses_appdata(self) -> None:
        with (
            patch.object(os, "name", "nt"),
            patch.dict(os.environ, {"APPDATA": r"C:\Users\x\AppData\Roaming"}, clear=False),
        ):
            path = translate._user_config_path()
        self.assertIn("AppData", path)
        self.assertTrue(path.endswith(os.path.join("aipmt", ".env")))


class TestThreeLayerPriority(unittest.TestCase):
    """L'ordre des couches est le cœur du contrat : env > projet > utilisateur.

    Il n'est pas codé explicitement — il découle de `override=False`, valeur par
    défaut de `load_dotenv`. Ces tests vérifient le COMPORTEMENT, pas la
    présence des deux appels : une inversion de leur ordre les ferait échouer.
    """

    VAR = "AIPMT_TEST_LAYER_KEY"

    def _run_layers(self, project_value=None, user_value=None, env_value=None):
        """Construit les trois couches puis renvoie ce que voit le module."""
        with tempfile.TemporaryDirectory() as project, tempfile.TemporaryDirectory() as config:
            if project_value is not None:
                Path(project, ".env").write_text(f"{self.VAR}={project_value}\n", encoding="utf-8")
            user_env = Path(config, "aipmt", ".env")
            if user_value is not None:
                user_env.parent.mkdir(parents=True)
                user_env.write_text(f"{self.VAR}={user_value}\n", encoding="utf-8")

            overrides = {"XDG_CONFIG_HOME": config}
            if env_value is not None:
                overrides[self.VAR] = env_value

            previous = os.getcwd()
            try:
                os.chdir(project)
                with patch.dict(os.environ, overrides, clear=False):
                    if env_value is None:
                        os.environ.pop(self.VAR, None)
                    translate._load_configuration()
                    return os.environ.get(self.VAR)
            finally:
                os.chdir(previous)
                os.environ.pop(self.VAR, None)

    def test_environment_wins_over_both_files(self) -> None:
        self.assertEqual(
            self._run_layers(project_value="projet", user_value="utilisateur", env_value="env"),
            "env",
        )

    def test_project_wins_over_user_config(self) -> None:
        self.assertEqual(
            self._run_layers(project_value="projet", user_value="utilisateur"), "projet"
        )

    def test_user_config_applies_when_nothing_else_defines_it(self) -> None:
        """La raison d'être de la troisième couche."""
        self.assertEqual(self._run_layers(user_value="utilisateur"), "utilisateur")

    def test_absent_everywhere_stays_absent(self) -> None:
        """Contre-épreuve : sans elle, les trois tests ci-dessus passeraient
        aussi sur une implémentation qui inventerait une valeur."""
        self.assertIsNone(self._run_layers())


class TestMissingKeyMessageIsActionable(unittest.TestCase):
    """Le message doit MONTRER les emplacements, pas seulement les nommer."""

    def test_message_names_the_three_locations(self) -> None:
        message = translate._missing_key_message("OpenAI", ["OPENAI_API_KEY"])
        self.assertIn("OPENAI_API_KEY", message)
        self.assertIn(os.path.join(os.getcwd(), ".env"), message)
        self.assertIn(translate._user_config_path(), message)

    def test_every_provider_message_shows_the_user_config_path(self) -> None:
        """Aucun provider ne doit garder l'ancien message tronqué."""
        args = type("Args", (), {"model": None, "eco": True})
        initialisers = (
            translate._init_openai_client,
            translate._init_claude_client,
            translate._init_mistral_client,
            translate._init_gemini_client,
            translate._init_grok_client,
        )
        # Liste EXPLICITE plutôt que dérivée de `os.environ` : la seconde
        # dépendrait de ce que la machine a chargé, donc le test ne prouverait
        # pas la même chose ici et en CI.
        key_vars = (
            "OPENAI_API_KEY",
            "ANTHROPIC_API_KEY",
            "MISTRAL_API_KEY",
            "GOOGLE_API_KEY",
            "GEMINI_API_KEY",
            "XAI_API_KEY",
        )
        without_keys = {k: v for k, v in os.environ.items() if k not in key_vars}
        for initialiser in initialisers:
            with (
                self.subTest(initialiser.__name__),
                patch.dict(os.environ, without_keys, clear=True),
            ):
                with self.assertRaises(ValueError) as raised:
                    initialiser(args())
                self.assertIn(translate._user_config_path(), str(raised.exception))


class TestMissingKeyIsNotATraceback(unittest.TestCase):
    """Une erreur de configuration ne doit pas ressembler à un plantage.

    Vérifié sur le VRAI point d'entrée : `main()` est ce qu'appelle la commande
    installée, et c'est là que la trace d'appel apparaissait.
    """

    def test_cli_exits_cleanly_without_any_key(self) -> None:
        with tempfile.TemporaryDirectory() as workdir:
            Path(workdir, "d.md").write_text("# T\n\ntexte\n", encoding="utf-8")
            env = {
                k: v
                for k, v in os.environ.items()
                if not k.endswith("API_KEY") and k != "XDG_CONFIG_HOME"
            }
            env["PYTHONPATH"] = str(SRC_ROOT)
            # Répertoire de configuration vide et non inexistant : on veut
            # prouver l'absence de clé, pas un chemin cassé.
            env["XDG_CONFIG_HOME"] = workdir
            argv = [sys.executable, "-m", "aipmt", "--file", "d.md", "--target_dir", "."]
            # nosemgrep
            proc = subprocess.run(  # nosec B603 # nosemgrep — CLI du repo via sys.executable
                argv,  # nosemgrep
                cwd=workdir,
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(proc.returncode, 2, f"stderr:\n{proc.stderr}")
        self.assertNotIn("Traceback", proc.stderr)
        self.assertNotIn("site-packages", proc.stderr)
        self.assertIn("OPENAI_API_KEY", proc.stderr)
        self.assertIn(os.path.join("aipmt", ".env"), proc.stderr)

    def test_real_bugs_keep_their_traceback(self) -> None:
        """Garde-fou du garde-fou : le filet est étroit à dessein.

        Si `main()` attrapait toute exception, un vrai bug survenu pendant la
        traduction deviendrait un message rassurant — le mode de défaillance
        que ce dépôt traque. Seule la phase de configuration est enveloppée.
        """
        body = inspect.getsource(translate.main)
        self.assertIn("except ValueError", body)
        self.assertNotIn("except Exception", body)
        self.assertNotIn("except:", body)


if __name__ == "__main__":
    unittest.main()
