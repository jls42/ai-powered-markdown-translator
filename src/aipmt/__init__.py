"""AI-Powered Markdown Translator — traduit du Markdown en préservant la mise en forme.

Le paquet est découpé par responsabilité : `config` (clés et `.env`),
`markdown` (lexique partagé), `segmentation`, `guards` (gardes de sortie),
`placeholders`, `news` (mode `--news`), `prompts`, `notes`, `naming`,
`pipeline` (traduction d'un texte, d'un fichier, d'un répertoire), `cli`
(ligne de commande) et le sous-paquet `providers/` (un module par chemin
d'appel, `base` en socle, `registry` pour la résolution et le dispatch).
`translate` est une façade de compatibilité : les noms que le module unique
d'origine exposait y restent accessibles, par identité.

Ce paquet n'expose que le point d'entrée cité par `[project.scripts]`.

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
from .cli import main

__all__ = ["main"]
