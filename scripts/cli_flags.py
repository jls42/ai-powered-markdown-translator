"""Flags argparse réels de la commande `aipmt`, lus sur le parser construit.

Les sondes de `check-release-ready.sh` lisaient les flags par regex sur les
`add_argument("--…")` de `src/aipmt/translate.py`. Une regex sur un chemin
codé en dur a deux angles morts : elle ne suit pas un découpage du module, et
elle ne voit pas un flag construit autrement qu'en littéral. Ici, c'est le
parser lui-même qui répond, où qu'il vive dans le paquet.

Le module qui construit le parser n'est pas nommé : après `import aipmt`,
exactement un module du paquet doit porter `_build_arg_parser`. Zéro, c'est
une sonde qui ne lit plus rien ; plusieurs, c'est une ambiguïté à trancher —
les deux sont des erreurs, jamais un ensemble vide silencieux.
"""

from __future__ import annotations

import argparse
import importlib
import sys


def cli_flags() -> set[str]:
    """Options longues (`--…`) déclarées par le parser, l'aide intégrée exclue."""
    sys.path.insert(0, "src")
    importlib.import_module("aipmt")
    builders = [
        module
        for name, module in list(sys.modules.items())
        if (name == "aipmt" or name.startswith("aipmt."))
        and callable(getattr(module, "_build_arg_parser", None))
    ]
    if len(builders) != 1:
        found = sorted(module.__name__ for module in builders)
        raise RuntimeError(
            f"{len(builders)} module(s) du paquet portent _build_arg_parser ({found}) — "
            "la sonde ne sait pas quel parser lire"
        )
    parser = builders[0]._build_arg_parser()
    return {
        option
        for action in parser._actions
        if not isinstance(action, argparse._HelpAction)
        for option in action.option_strings
        if option.startswith("--")
    }


if __name__ == "__main__":
    print("\n".join(sorted(cli_flags())))
