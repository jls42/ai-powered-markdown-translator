"""Permet `python -m aipmt`, strictement équivalent à la commande `aipmt`.

Les deux formes sont documentées côte à côte : `python -m` reste la seule
disponible quand le répertoire des scripts n'est pas dans le PATH, situation
courante sur une installation utilisateur.
"""

from .translate import main

if __name__ == "__main__":
    main()
