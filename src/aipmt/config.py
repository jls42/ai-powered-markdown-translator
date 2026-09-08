"""Résolution de la configuration : clés API et emplacement du `.env` utilisateur.

Trois couches, de la plus prioritaire à la moindre : variables d'environnement,
`.env` du projet (répertoire courant ou parents), configuration utilisateur
persistante (`~/.config/aipmt/.env`, `XDG_CONFIG_HOME` s'il est absolu,
`APPDATA` sous Windows). La priorité n'est pas codée : elle découle de
`override=False`, valeur par défaut de `load_dotenv`.

Ce module est importé EN PREMIER par `aipmt/__init__.py`, et il charge les
couches à l'import : les constantes des providers lues par `os.getenv` au
niveau module (`CODEX_TIMEOUT`, `OPENROUTER_TIMEOUT`…) trouvent ainsi le `.env`
déjà chargé, comme lorsque tout vivait dans un seul module.
"""

import os
import sys

from dotenv import find_dotenv, load_dotenv

# Variables qui décident OÙ part une clé d'API. Le `.env` du projet est cherché
# depuis le répertoire courant et ses parents : une arborescence non fiable —
# un dépôt qu'on vient de cloner — peut donc en poser une, et la vraie clé,
# venue de l'environnement ou de la configuration utilisateur, partirait
# ensuite dans l'en-tête d'autorisation d'un serveur tiers. Ces variables-là ne
# sont acceptées que des deux couches que l'utilisateur contrôle vraiment.
#
# `OPENAI_BASE_URL` est lue par le SDK lui-même, pas par ce paquet : la retirer
# de l'environnement est le seul moyen de l'empêcher d'agir.
_ENDPOINT_VARIABLES = ("OPENAI_BASE_URL", "OPENROUTER_BASE_URL", "XAI_BASE_URL")


def _user_config_path():
    """Fichier de configuration utilisateur, à l'emplacement conventionnel de l'OS.

    C'est la couche « installé une fois, marche partout » : sans elle, une CLI
    installée n'a que la variable d'environnement et le `.env` du répertoire
    courant — donc rien de persistant hors d'un projet donné.

    `find_dotenv` remonte certes jusqu'à la racine du système et trouverait un
    `~/.env` quand on travaille sous son répertoire personnel — mais pas quand
    on travaille ailleurs. Cette couverture accidentelle dépend de l'endroit
    d'où l'on lance la commande ; celle-ci n'en dépend pas.
    """
    if os.name == "nt":
        base = os.getenv("APPDATA") or os.path.join(os.path.expanduser("~"), "AppData", "Roaming")
    else:
        # La spécification XDG impose un chemin ABSOLU et demande d'ignorer la
        # variable sinon. Sans ce contrôle, un `XDG_CONFIG_HOME` relatif ferait
        # dépendre l'emplacement de la configuration du répertoire courant —
        # exactement le défaut qu'on corrige ici.
        base = os.getenv("XDG_CONFIG_HOME") or ""
        if not os.path.isabs(base):
            base = os.path.join(os.path.expanduser("~"), ".config")
    return os.path.join(base, "aipmt", ".env")


def _load_configuration():
    """Charge les clés selon TROIS couches, de la plus prioritaire à la moindre.

    1. variables d'environnement déjà définies — CI, conteneurs, override ponctuel
    2. `.env` du projet, cherché depuis le répertoire courant puis les parents
    3. `_user_config_path()`, la configuration utilisateur persistante

    La priorité n'est pas codée : elle découle de `override=False`, valeur par
    défaut de `load_dotenv`, qui ne remplace jamais une variable déjà définie.
    Chaque couche ne fait donc que combler ce que la précédente a laissé vide.

    `usecwd=True` est indispensable à la couche 2 : sans lui, `find_dotenv`
    remonte depuis le fichier APPELANT — donc depuis site-packages une fois
    l'outil installé — et ignore en silence le `.env` du répertoire de travail.
    Mesuré sur un point d'entrée console réel : `find_dotenv()` renvoie `''` là
    où `find_dotenv(usecwd=True)` trouve le fichier. Depuis le dépôt cloné, les
    deux formes donnent le même résultat, ce qui explique que le défaut soit
    resté invisible tant que l'outil n'était pas installable.

    Exception à la couche 2 : elle ne peut pas poser d'URL d'endpoint. Voir
    `_ENDPOINT_VARIABLES` — un `.env` de projet qui redirige les appels
    détournerait une clé qu'il ne connaît pas.
    """
    deja_definies = {name for name in _ENDPOINT_VARIABLES if name in os.environ}
    load_dotenv(find_dotenv(usecwd=True))
    _drop_project_endpoints(deja_definies)
    load_dotenv(_user_config_path())


def _drop_project_endpoints(deja_definies):
    """Retire les URL d'endpoint que le `.env` du projet vient de poser.

    Appelée ENTRE les deux couches : ce qui vient d'apparaître ne peut venir
    que du projet, et la configuration utilisateur pourra encore fournir la
    sienne juste après. Le refus est dit sur stderr — silencieux, il ferait
    chercher pourquoi un relais légitime n'est pas pris en compte."""
    for name in _ENDPOINT_VARIABLES:
        if name in deja_definies or name not in os.environ:
            continue
        valeur = os.environ.pop(name)
        print(
            f"⚠ {name}={valeur} ignoré : un .env de projet ne peut pas rediriger les "
            "appels d'API, sinon un répertoire non fiable détournerait votre clé. "
            f"L'exporter dans l'environnement, ou le mettre dans {_user_config_path()}.",
            file=sys.stderr,
        )


_load_configuration()


def _missing_key_message(provider, variables, hint=""):
    """Message d'absence de clé qui dit OÙ mettre la clé, chemin exact compris.

    Le message précédent — « Définir X dans l'environnement ou .env » — était
    exact et inexploitable : quelqu'un qui vient d'installer l'outil n'a ni
    l'un ni l'autre, et rien ne lui disait où créer le second ni qu'une
    configuration utilisateur existait. Une erreur de configuration doit
    montrer l'emplacement, pas le nommer.
    """
    names = " ou ".join(variables)
    return (
        f"Clé API {provider} non spécifiée.{hint}\n"
        f"Définir {names} à l'un de ces trois endroits, du plus prioritaire au moindre :\n"
        f"  1. variable d'environnement  →  export {variables[0]}=votre-cle\n"
        f"  2. .env du projet            →  {os.path.join(os.getcwd(), '.env')}\n"
        f"  3. configuration utilisateur →  {_user_config_path()}\n"
        f"     (vaut pour toutes vos sessions ; créer le répertoire si besoin)"
    )
