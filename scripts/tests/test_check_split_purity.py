"""Le vérificateur de pureté du découpage doit MORDRE.

Un gate qu'on n'a jamais vu rouge ne prouve rien : chaque test ci-dessous
construit un petit paquet dans un dépôt git jetable, fige son snapshot, puis
introduit exactement une infraction et exige le refus. Le cas nominal (arbre
identique) reste vert, sinon le hook bloquerait tout commit.
"""

import contextlib
import io
import json
import os
import pathlib
import subprocess  # nosec B404 — `git init`/`git add` dans un répertoire temporaire
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import importlib.util

_SPEC = importlib.util.spec_from_file_location(
    "check_split_purity", ROOT / "scripts" / "check-split-purity.py"
)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError("scripts/check-split-purity.py introuvable ou sans chargeur")
purity = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(purity)

MODULE = '''"""Un module de démonstration."""
import os

ANSWER = 42


def alpha():
    return os.getcwd()  # nosec B000 — marqueur de démonstration


def beta(x):
    return x + ANSWER
'''


def _env_sans_git():
    """L'environnement, moins toute variable GIT_*. Poussé depuis un worktree
    lié, git exporte GIT_DIR à ses hooks — mesuré le 2026-09-27, et pas depuis
    le dépôt principal. Hérité par le hook pre-push qui lance ces tests, il
    faisait opérer `git init` et `git add` sur le VRAI dépôt, dont la
    configuration passait à `core.bare = true`."""
    return {name: value for name, value in os.environ.items() if not name.startswith("GIT_")}


def _git(cwd, *args):
    argv = ["git", *args]
    # nosemgrep
    subprocess.run(  # nosec B603 B607 # nosemgrep — git du PATH, argv littéral, dépôt jetable
        argv,  # nosemgrep
        cwd=cwd,
        env=_env_sans_git(),
        check=True,
        capture_output=True,
    )


class PurityCheckerBites(unittest.TestCase):
    def setUp(self):
        # Le vérificateur appelle lui aussi git (fichiers non suivis) : sans
        # GIT_* hérité, il lit le dépôt jetable et non celui du hook.
        environ = patch.dict(os.environ, _env_sans_git(), clear=True)
        environ.start()
        self.addCleanup(environ.stop)
        self._tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self._tmp.name)
        self.package = self.root / "src" / "aipmt"
        self.package.mkdir(parents=True)
        (self.package / "__init__.py").write_text('"""Paquet."""\n', encoding="utf-8")
        (self.package / "translate.py").write_text(MODULE, encoding="utf-8")
        for path in ("tests", "scripts/tests"):
            (self.root / path).mkdir(parents=True)
        _git(self.root, "init", "-q")
        _git(self.root, "add", "-A")
        self.snapshot = pathlib.Path("scripts/split-reference/ref.json")
        self.manifest = pathlib.Path("scripts/split-reference/manifest.json")
        self.assertEqual(self._run("--write-snapshot"), 0)
        _git(self.root, "add", "-A")

    def tearDown(self):
        self._tmp.cleanup()

    def test_a_hook_git_dir_never_reaches_git(self):
        """Un GIT_DIR hérité désigne ici un dépôt nu : s'il passait, `git
        status` y échouerait faute d'arbre de travail, comme le `git add` de
        ces tests a échoué dans le vrai dépôt après l'avoir rendu nu."""
        with tempfile.TemporaryDirectory() as leurre:
            _git(leurre, "init", "-q", "--bare")
            with patch.dict(os.environ, {"GIT_DIR": leurre}):
                _git(self.root, "status", "--porcelain")

    def _run(self, *extra):
        argv = [
            "--root",
            str(self.root),
            "--snapshot",
            str(self.snapshot),
            "--manifest",
            str(self.manifest),
            *extra,
        ]
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return purity.main(argv)

    def _write_translate(self, text):
        (self.package / "translate.py").write_text(text, encoding="utf-8")

    def test_unchanged_tree_is_green(self):
        self.assertEqual(self._run(), 0)

    def test_pure_move_to_another_module_is_green(self):
        # `beta` déménage tel quel : même AST, autre fichier — c'est le geste attendu.
        self._write_translate(MODULE.replace("\n\ndef beta(x):\n    return x + ANSWER\n", "\n"))
        (self.package / "other.py").write_text(
            "from .translate import ANSWER\n\n\ndef beta(x):\n    return x + ANSWER\n",
            encoding="utf-8",
        )
        _git(self.root, "add", "-A")
        self.assertEqual(self._run(), 0)

    def test_lost_symbol_is_red(self):
        self._write_translate(MODULE.replace("\n\ndef beta(x):\n    return x + ANSWER\n", "\n"))
        self.assertEqual(self._run(), 1)

    def test_modified_body_is_red_until_declared(self):
        self._write_translate(MODULE.replace("return x + ANSWER", "return x - ANSWER"))
        self.assertEqual(self._run(), 1)

    def test_undeclared_addition_is_red_and_declared_addition_is_green(self):
        self._write_translate(MODULE + "\n\ndef gamma():\n    return 1\n")
        self.assertEqual(self._run(), 1)
        nodes = purity.collect_nodes(self.package)
        gamma = next(node for node in nodes if node["name"] == "gamma")
        (self.root / self.manifest).write_text(
            json.dumps({"added": [{**gamma, "why": "test"}], "removed": [], "modified": []}),
            encoding="utf-8",
        )
        _git(self.root, "add", "-A")
        self.assertEqual(self._run(), 0)

    def test_duplicated_symbol_is_red(self):
        (self.package / "other.py").write_text(
            "def beta(x):\n    return x + ANSWER\n", encoding="utf-8"
        )
        _git(self.root, "add", "-A")
        self.assertEqual(self._run(), 1)

    def test_lost_security_marker_is_red(self):
        self._write_translate(MODULE.replace("  # nosec B000 — marqueur de démonstration", ""))
        self.assertEqual(self._run(), 1)

    def test_marqueur_reecrit_vert_seulement_si_le_remplacant_existe(self):
        """Un marqueur peut changer de ligne — la variable ouverte est renommée —
        sans que la suppression disparaisse. Déclaré, c'est vert ; déclaré vers
        une ligne qui n'existe pas, c'est rouge, sinon la déclaration
        suffirait à faire taire le contrôle."""
        ancien = "return os.getcwd()  # nosec B000 — marqueur de démonstration"
        nouveau = "return os.getcwdb()  # nosec B000 — marqueur de démonstration"
        self._write_translate(MODULE.replace(ancien, nouveau))
        self.assertEqual(self._run(), 1)

        reference = json.loads((self.root / self.snapshot).read_text(encoding="utf-8"))
        ancien_hash = next(node["hash"] for node in reference["nodes"] if node["name"] == "alpha")
        alpha = next(node for node in purity.collect_nodes(self.package) if node["name"] == "alpha")
        base = {
            "added": [],
            "removed": [],
            "modified": [
                {**alpha, "old_hash": ancien_hash, "new_hash": alpha["hash"], "why": "test"}
            ],
        }
        absent = dict(base, markers=[{"old": ancien, "new": "ligne inexistante", "why": "test"}])
        (self.root / self.manifest).write_text(json.dumps(absent), encoding="utf-8")
        _git(self.root, "add", "-A")
        self.assertEqual(self._run(), 1)

        correct = dict(base, markers=[{"old": ancien, "new": nouveau, "why": "test"}])
        (self.root / self.manifest).write_text(json.dumps(correct), encoding="utf-8")
        _git(self.root, "add", "-A")
        self.assertEqual(self._run(), 0)

    def test_une_reecriture_ne_peut_pas_retirer_la_suppression(self):
        """Déclarer `… # nosec B000` → la même ligne SANS le marqueur passait au
        vert : la déclaration suffisait alors à retirer une suppression, soit
        exactement ce que ce contrôle existe pour empêcher."""
        ancien = "return os.getcwd()  # nosec B000 — marqueur de démonstration"
        sans_marqueur = "return os.getcwd()"
        self._write_translate(MODULE.replace(ancien, sans_marqueur))

        reference = json.loads((self.root / self.snapshot).read_text(encoding="utf-8"))
        ancien_hash = next(node["hash"] for node in reference["nodes"] if node["name"] == "alpha")
        alpha = next(node for node in purity.collect_nodes(self.package) if node["name"] == "alpha")
        (self.root / self.manifest).write_text(
            json.dumps(
                {
                    "added": [],
                    "removed": [],
                    "modified": [
                        {**alpha, "old_hash": ancien_hash, "new_hash": alpha["hash"], "why": "test"}
                    ],
                    "markers": [{"old": ancien, "new": sans_marqueur, "why": "test"}],
                }
            ),
            encoding="utf-8",
        )
        _git(self.root, "add", "-A")
        self.assertEqual(self._run(), 1)

    def test_untracked_module_is_red(self):
        (self.package / "forgotten.py").write_text("", encoding="utf-8")
        self.assertEqual(self._run(), 1)

    def test_subprocess_import_without_nosec_is_red(self):
        (self.package / "runner.py").write_text("import subprocess\n", encoding="utf-8")
        _git(self.root, "add", "-A")
        self.assertEqual(self._run(), 1)


if __name__ == "__main__":
    unittest.main()
