"""Contrat de la façade `aipmt.translate` après le découpage en modules.

Quatre propriétés, chacune née d'un mode de défaillance mesuré pendant le
découpage :

1. **L'ensemble exact des noms exposés.** Les 64 noms définis par le projet
   sans préfixe `_` dans l'ancien module unique restent accessibles, et RIEN
   d'autre : ni nom privé, ni SDK, ni module de la bibliothèque standard. Un
   nom privé ré-exporté laisserait un `patch("aipmt.translate._x")` réussir
   sans mordre ; un SDK ré-exporté (`OpenAI`) laisserait construire un vrai
   client derrière un patch posé au mauvais endroit.
2. **L'identité des alias.** Chaque nom de la façade EST l'objet de son module
   de définition. Plusieurs sont mutables (`MODEL_TOKEN_LIMITS`, que le
   provider OpenRouter écrit ; `LANG_FLAGS` ; `EXCLUDE_PATTERNS`) : une copie
   divergerait en silence.
3. **La configuration est chargée à l'import du paquet**, comme lorsque tout
   vivait dans un module : les constantes des providers lisent `os.getenv` au
   niveau module et doivent trouver `.env` déjà chargé.
4. **Aucun test ne patche la façade.** Neuf tests le faisaient sur des noms
   publics (`translate_markdown_file`, `translate_directory`) et restaient
   verts sans leur patch, parce que la fonction réelle rend « failure » sur
   un chemin inexistant — exactement la valeur attendue. Un patch vise le
   module qui CONSULTE le nom, jamais celui qui l'expose. Détection par AST :
   les formes à quotes simples, multilignes ou aliasées échappent à un grep.
"""

import ast
import os
import pathlib
import subprocess  # nosec B404 — relance l'interpréteur pour observer l'import du paquet
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import aipmt.translate as facade
from aipmt import cli, markdown, naming, news, pipeline, segmentation
from aipmt.providers import (
    anthropic,
    base,
    codex,
    gemini,
    grok,
    mistral,
    openai,
    opencode,
    openrouter,
)

ROOT = pathlib.Path(__file__).resolve().parents[1]

SUPPORTED = {
    "main",
    "translate",
    "segment_text",
    "translate_markdown_file",
    "translate_directory",
    "MODEL_TOKEN_LIMITS",
    "DEFAULT_TOKEN_LIMIT",
    "EXCLUDE_PATTERNS",
    "LANG_FLAGS",
}

# Les 64 noms sans `_` de l'ancien module, avec le module qui les définit.
ALIASES = {
    cli: {
        "DEFAULT_SOURCE_DIR",
        "DEFAULT_SOURCE_LANG",
        "DEFAULT_TARGET_DIR",
        "DEFAULT_TARGET_LANG",
        "main",
    },
    markdown: {"news_quote_placeholder", "news_quote_placeholder_regex"},
    naming: {"EXCLUDE_PATTERNS", "is_excluded"},
    news: {"LANG_FLAGS"},
    pipeline: {"translate", "translate_directory", "translate_markdown_file"},
    segmentation: {"DEFAULT_TOKEN_LIMIT", "MODEL_TOKEN_LIMITS", "segment_text"},
    anthropic: {
        "CLAUDE_MAX_TOKENS",
        "CLAUDE_TIMEOUT",
        "DEFAULT_ANTHROPIC_API_KEY",
        "DEFAULT_MODEL_CLAUDE",
        "ECO_MODEL_CLAUDE",
    },
    base: {"CODEX_TERM_GRACE"},
    codex: {
        "CODEX_AGENT_CONTRACT",
        "CODEX_MODEL_PREFIXES",
        "CODEX_STRIPPED_ENV_VARS",
        "CODEX_TIMEOUT",
        "DEFAULT_MODEL_CODEX",
        "ECO_MODEL_CODEX",
    },
    gemini: {"DEFAULT_GEMINI_API_KEY", "DEFAULT_MODEL_GEMINI", "ECO_MODEL_GEMINI"},
    grok: {
        "DEFAULT_MODEL_GROK",
        "DEFAULT_MODEL_GROK_CLI",
        "DEFAULT_XAI_API_KEY",
        "ECO_MODEL_GROK",
        "ECO_MODEL_GROK_CLI",
        "GROK_AGENT_CONTRACT",
        "GROK_DENY_RULES",
        "GROK_ENV_KILL_SWITCHES",
        "GROK_MAX_TURNS",
        "GROK_PROMPT_FILENAME",
        "GROK_SANDBOX_ENV_VAR",
        "GROK_STRIPPED_ENV_VARS",
        "GROK_TIMEOUT",
        "XAI_BASE_URL",
    },
    mistral: {"DEFAULT_MISTRAL_API_KEY", "DEFAULT_MODEL_MISTRAL", "ECO_MODEL_MISTRAL"},
    openai: {"DEFAULT_MODEL_OPENAI", "DEFAULT_OPENAI_API_KEY", "ECO_MODEL_OPENAI"},
    opencode: {
        "OPENCODE_AGENT_CONTRACT",
        "OPENCODE_AGENT_NAME",
        "OPENCODE_ENV_KILL_SWITCHES",
        "OPENCODE_KEPT_ENV_VARS",
        "OPENCODE_SESSION_TITLE",
        "OPENCODE_TIMEOUT",
    },
    openrouter: {
        "DEFAULT_OPENROUTER_API_KEY",
        "OPENROUTER_BASE_URL",
        "OPENROUTER_EFFORTS_CROISSANTS",
        "OPENROUTER_MAX_TOKENS",
        "OPENROUTER_MIN_COMPLETION_TOKENS",
        "OPENROUTER_PREFLIGHT_TIMEOUT",
        "OPENROUTER_TIMEOUT",
    },
}


class FacadeExposesExactlyTheHistoricalPublicNames(unittest.TestCase):
    def test_exact_set_of_public_attributes(self):
        expected = set().union(*ALIASES.values())
        self.assertEqual(len(expected), 64)
        actual = {name for name in dir(facade) if not name.startswith("_")}
        self.assertEqual(actual, expected)

    def test_all_lists_only_the_supported_api(self):
        self.assertEqual(set(facade.__all__), SUPPORTED)
        self.assertLessEqual(SUPPORTED, set().union(*ALIASES.values()))

    def test_no_private_sdk_or_stdlib_reexport(self):
        for name in (
            "OpenAI",
            "Mistral",
            "anthropic",
            "genai",
            "detect_langs",
            "os",
            "sys",
            "re",
            "subprocess",
            "argparse",
        ):
            self.assertFalse(hasattr(facade, name), name)
        self.assertFalse(any(n.startswith("_") and not n.startswith("__") for n in dir(facade)))

    def test_every_alias_is_the_same_object_as_its_definition(self):
        for module, names in ALIASES.items():
            for name in names:
                with self.subTest(name=name):
                    self.assertIs(getattr(facade, name), getattr(module, name))


class ConfigurationIsLoadedAtPackageImport(unittest.TestCase):
    def test_load_dotenv_runs_twice_when_the_package_is_imported(self):
        # Interpréteur neuf : `config` doit appeler load_dotenv (deux couches)
        # pendant `import aipmt`, avant que les providers lisent os.getenv.
        probe = (
            "import dotenv\n"
            "calls = []\n"
            "dotenv.load_dotenv = lambda *a, **k: calls.append(a)\n"
            "import aipmt\n"
            "print(len(calls))\n"
        )
        argv = [sys.executable, "-c", probe]
        env = {**os.environ, "PYTHONPATH": str(ROOT / "src")}
        # nosemgrep
        proc = subprocess.run(  # nosec B603 # nosemgrep — interpréteur courant, code littéral
            argv,  # nosemgrep
            capture_output=True,
            text=True,
            env=env,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(proc.stdout.strip(), "2")


class NoTestPatchesTheFacade(unittest.TestCase):
    """Un patch se pose sur le module qui consulte le nom. Jamais sur la façade."""

    FACADE = "aipmt.translate"

    @classmethod
    def _is_patch_call(cls, func):
        """`patch(...)`, `mock.patch(...)`, `patch.object(...)`, `patch.multiple(...)`
        et leurs formes préfixées — pas `patch.dict`, qui touche un objet partagé."""
        if isinstance(func, ast.Name):
            return func.id == "patch"
        if not isinstance(func, ast.Attribute):
            return False
        if func.attr == "patch":
            return True
        return func.attr in ("object", "multiple") and cls._is_patch_call(func.value)

    @classmethod
    def _facade_aliases(cls, tree):
        """Les noms locaux liés à la façade : `translate` par défaut, plus
        `import aipmt.translate as x` et `from aipmt import translate as x`."""
        names = {"translate"}
        for node in ast.walk(tree):
            names |= cls._aliases_bound_by(node)
        return names

    @classmethod
    def _aliases_bound_by(cls, node):
        if isinstance(node, ast.Import):
            return cls._aliases_from_import(node)
        if isinstance(node, ast.ImportFrom):
            return cls._aliases_from_import_from(node)
        return set()

    @classmethod
    def _aliases_from_import(cls, node):
        return {a.asname for a in node.names if a.name == cls.FACADE and a.asname}

    @staticmethod
    def _aliases_from_import_from(node):
        if node.module != "aipmt" or node.level:
            return set()
        return {a.asname or a.name for a in node.names if a.name == "translate"}

    @classmethod
    def _facade_target(cls, target, aliases):
        """La cible si elle désigne la façade, sinon None."""
        if isinstance(target, ast.Constant):
            return cls._facade_string(target.value)
        return cls._facade_attribute(target, aliases)

    @classmethod
    def _facade_string(cls, value):
        if isinstance(value, str) and (value == cls.FACADE or value.startswith(cls.FACADE + ".")):
            return value
        return None

    @classmethod
    def _facade_attribute(cls, target, aliases):
        dotted = ast.unparse(target)
        if dotted == cls.FACADE or dotted.startswith(cls.FACADE + "."):
            return dotted
        root = target
        while isinstance(root, ast.Attribute):
            root = root.value
        if isinstance(root, ast.Name) and root.id in aliases:
            return dotted
        return None

    @staticmethod
    def _first_target(call):
        """Premier argument positionnel, sinon le mot-clé `target=`."""
        if call.args:
            return call.args[0]
        return next((k.value for k in call.keywords if k.arg == "target"), None)

    @classmethod
    def _patch_targets(cls, path):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        aliases = cls._facade_aliases(tree)
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call) or not cls._is_patch_call(node.func):
                continue
            candidate = cls._first_target(node)
            target = None if candidate is None else cls._facade_target(candidate, aliases)
            if target is not None:
                yield node.lineno, target

    def test_no_patch_targets_the_facade(self):
        offenders = []
        for folder in ("tests", "scripts/tests"):
            for path in sorted((ROOT / folder).glob("*.py")):
                offenders += [
                    f"{path.relative_to(ROOT)}:{line} {target}"
                    for line, target in self._patch_targets(path)
                ]
        self.assertEqual(offenders, [])

    def test_the_detector_sees_every_form(self):
        """Mesuré avant durcissement : sur cinq formes, seule la chaîne
        `patch('aipmt.translate.x')` était vue ; `mock.patch.object`, un alias
        d'import, `target=` et `patch.multiple` passaient."""
        sample = (
            "from unittest import mock\n"
            "from unittest.mock import patch\n"
            "from aipmt import translate\n"
            "from aipmt import translate as t\n"
            "import aipmt.translate as facade\n"
            "import aipmt.translate\n"
            "patch('aipmt.translate.x')\n"
            'patch(\n    "aipmt.translate.y",\n)\n'
            "patch.object(translate, 'z')\n"
            "mock.patch('aipmt.translate.w')\n"
            "mock.patch.object(translate, 'v')\n"
            "patch.object(facade, 'u')\n"
            "patch.object(t, 's')\n"
            "patch.object(aipmt.translate, 'p')\n"
            "patch(target='aipmt.translate.r')\n"
            "patch.multiple(translate, q=1)\n"
            "patch.dict(translate.MODEL_TOKEN_LIMITS, {})\n"  # autorisé : objet partagé
            "patch('aipmt.cli.translate_markdown_file')\n"  # autorisé : le consommateur
        )
        with tempfile.TemporaryDirectory() as tmp:
            sample_path = pathlib.Path(tmp, "sonde.py")
            sample_path.write_text(sample, encoding="utf-8")
            found = [target for _, target in self._patch_targets(sample_path)]
        self.assertEqual(
            found,
            [
                "aipmt.translate.x",
                "aipmt.translate.y",
                "translate",
                "aipmt.translate.w",
                "translate",
                "facade",
                "t",
                "aipmt.translate",
                "aipmt.translate.r",
                "translate",
            ],
        )


if __name__ == "__main__":
    unittest.main()
