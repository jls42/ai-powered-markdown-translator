"""Le vérificateur de pureté du découpage doit MORDRE.

Un gate qu'on n'a jamais vu rouge ne prouve rien : chaque test ci-dessous
construit un petit paquet dans un dépôt git jetable, fige son snapshot, puis
introduit exactement une infraction et exige le refus. Le cas nominal (arbre
identique) reste vert, sinon le hook bloquerait tout commit.
"""

import contextlib
import io
import json
import pathlib
import subprocess  # nosec B404 — `git init`/`git add` dans un répertoire temporaire
import sys
import tempfile
import unittest

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


def _git(cwd, *args):
    argv = ["git", *args]
    # nosemgrep
    subprocess.run(  # nosec B603 B607 # nosemgrep — git du PATH, argv littéral, dépôt jetable
        argv,  # nosemgrep
        cwd=cwd,
        check=True,
        capture_output=True,
    )


class PurityCheckerBites(unittest.TestCase):
    def setUp(self):
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

    def test_untracked_module_is_red(self):
        (self.package / "forgotten.py").write_text("", encoding="utf-8")
        self.assertEqual(self._run(), 1)

    def test_subprocess_import_without_nosec_is_red(self):
        (self.package / "runner.py").write_text("import subprocess\n", encoding="utf-8")
        _git(self.root, "add", "-A")
        self.assertEqual(self._run(), 1)


if __name__ == "__main__":
    unittest.main()
