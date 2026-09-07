"""AI-Powered Markdown Translator — traduit du Markdown en préservant la mise en forme.

Toute la logique vit dans `aipmt.translate`, qui reste un module unique. Ce
paquet n'expose que le point d'entrée cité par `[project.scripts]`.

Le nom `aipmt` n'est pas une coquetterie d'acronyme : publier ce module en
top-level `translate` l'aurait mis en collision avec le paquet PyPI `translate`
(v3.8.1, activement maintenu), qui installe un RÉPERTOIRE du même nom. Reproduit
dans un venv : le répertoire gagne, `translate.main` disparaît, le point
d'entrée casse sur `AttributeError` — et `pip check` répond « No broken
requirements found ». Une casse silencieuse qu'un utilisateur déclencherait par
un simple `pip install translate`.
"""

# `config` en PREMIER, et explicitement : il charge les trois couches de
# configuration à l'import, et les modules providers lisent `os.getenv` au
# niveau module. Tout import d'un sous-module exécute ce fichier d'abord, ce
# qui fait de cette ligne la garantie d'ordre — pas une convention.
from . import config  # noqa: F401
from .translate import main

__all__ = ["main"]
