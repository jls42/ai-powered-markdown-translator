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

from .translate import main

__all__ = ["main"]
