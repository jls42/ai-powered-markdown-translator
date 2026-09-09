"""Contrat du registre des providers après sa scission pour Codacy.

Les chaînes if/elif de `_resolve_provider`, `_dispatch_provider_call` et
`_select_provider_client` ont été coupées en deux pour tenir sous la complexité
que Codacy tolère (CCN 8), et les huit flags exclusifs sont désormais décrits
une fois. Ce que ces tests verrouillent, c'est ce que la scission ne devait pas
changer : l'ORDRE d'évaluation des flags — la précédence est un contrat
observable, cf. `TestProviderFlagsAreMutuallyExclusive` — et le routage de
chaque clé vers son constructeur et son appel.
"""

from __future__ import annotations

import argparse
import os
import sys
import unittest
from argparse import Namespace
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from aipmt.providers import registry

# Ordre d'évaluation, du plus prioritaire au moins. Pour `_select_provider_client`
# les trois premiers sont des attributs obligatoires du Namespace et les suivants
# sont lus par getattr ; `_resolve_provider` reçoit les trois premiers en
# paramètres nommés et ne lit le Namespace que pour les suivants.
CHAIN = (
    ("use_mistral", "mistral"),
    ("use_claude", "claude"),
    ("use_gemini", "gemini"),
    ("use_codex", "codex"),
    ("use_grok_cli", "grok_cli"),
    ("use_grok", "grok"),
    ("use_opencode", "opencode"),
    ("use_openrouter", "openrouter"),
)
# Ordre de l'aide (`--help`), distinct de l'ordre de précédence : le groupe
# exclusif rend la différence sans conséquence en ligne de commande.
HELP_ORDER = (
    "use_mistral",
    "use_claude",
    "use_gemini",
    "use_grok",
    "use_grok_cli",
    "use_codex",
    "use_opencode",
    "use_openrouter",
)
INITS = {
    "mistral": "_init_mistral_client",
    "claude": "_init_claude_client",
    "gemini": "_init_gemini_client",
    "codex": "_init_codex_client",
    "grok_cli": "_init_grok_cli_client",
    "grok": "_init_grok_client",
    "opencode": "_init_opencode_client",
    "openrouter": "_init_openrouter_client",
    "openai": "_init_openai_client",
}
CALLS = {
    "mistral": "_call_mistral",
    "claude": "_call_claude",
    "gemini": "_call_gemini",
    "codex": "_call_codex",
    "grok_cli": "_call_grok_cli",
    "opencode": "_call_opencode",
    "openrouter": "_call_openrouter",
    "grok": "_call_openai",
    "openai": "_call_openai",
}


def _namespace_from(index):
    """Namespace où les flags à partir de `index` dans CHAIN sont levés, les
    précédents baissés : le provider attendu est celui de `index`."""
    return Namespace(**{flag: position >= index for position, (flag, _) in enumerate(CHAIN)})


class TestPrecedenceSurvivesTheSplit(unittest.TestCase):
    def test_explicit_booleans_still_win(self):
        every_flag = _namespace_from(0)
        self.assertEqual(registry._resolve_provider(every_flag, use_gemini=True), "gemini")
        self.assertEqual(registry._resolve_provider(every_flag), "codex")

    def test_resolve_follows_the_chain(self):
        for index, (_, expected) in enumerate(CHAIN[3:], start=3):
            with self.subTest(expected=expected):
                self.assertEqual(registry._resolve_provider(_namespace_from(index)), expected)
        self.assertEqual(registry._resolve_provider(_namespace_from(len(CHAIN))), "openai")

    def test_select_client_follows_the_chain(self):
        fakes = {name: MagicMock(return_value=key) for key, name in INITS.items()}
        expected_keys = [key for _, key in CHAIN] + ["openai"]
        with patch.multiple(registry, **fakes):
            for index, expected in enumerate(expected_keys):
                with self.subTest(expected=expected):
                    args = _namespace_from(index)
                    self.assertEqual(registry._select_provider_client(args), expected)
                    fakes[INITS[expected]].assert_called_with(args)

    def test_dispatch_routes_every_key(self):
        fakes = {name: MagicMock(return_value=f"{name}:ok") for name in set(CALLS.values())}
        args = Namespace(model="m")
        with patch.multiple(registry, **fakes):
            for key, name in CALLS.items():
                with self.subTest(key=key):
                    out = registry._dispatch_provider_call("client", args, "P", "S", key, True)
                    self.assertEqual(out, f"{name}:ok")
                    if name == "_call_openai":
                        # Seul appel à recevoir le drapeau de note de traduction.
                        fakes[name].assert_called_with("client", args, "P", "S", True)
                    else:
                        fakes[name].assert_called_with("client", args, "P", "S")


class TestProviderFlagsDeclaredOnce(unittest.TestCase):
    def _parser(self):
        parser = argparse.ArgumentParser()
        registry._add_provider_args(parser)
        return parser

    def test_the_eight_flags_form_one_exclusive_group_in_help_order(self):
        parser = self._parser()
        # argparse n'expose pas la composition d'un groupe : attributs privés,
        # stables depuis Python 2.7, seule façon de lire l'ORDRE du groupe.
        groups = parser._mutually_exclusive_groups
        self.assertEqual(len(groups), 1)
        self.assertEqual(
            [action.option_strings for action in groups[0]._group_actions],
            [[f"--{flag}"] for flag in HELP_ORDER],
        )
        self.assertEqual(set(HELP_ORDER), {flag for flag, _ in CHAIN})

    def test_every_flag_is_a_store_true_off_by_default(self):
        parser = self._parser()
        for flag, _ in CHAIN:
            with self.subTest(flag=flag):
                self.assertFalse(getattr(parser.parse_args([]), flag))
                self.assertTrue(getattr(parser.parse_args([f"--{flag}"]), flag))

    def test_model_eco_and_reasoning_effort_stay_outside_the_group(self):
        args = self._parser().parse_args(["--model", "x/y", "--eco", "--reasoning_effort", "low"])
        self.assertEqual((args.model, args.eco, args.reasoning_effort), ("x/y", True, "low"))


if __name__ == "__main__":
    unittest.main()
