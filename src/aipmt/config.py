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

# Variables qui décident OÙ part une requête, ou par quel chemin. Le `.env` du
# projet est cherché depuis le répertoire courant et ses parents : une
# arborescence non fiable — un dépôt qu'on vient de cloner — peut donc en poser
# une sans connaître aucune clé, et la vraie clé, venue de l'environnement ou
# de la configuration utilisateur, partirait ensuite dans l'en-tête
# d'autorisation d'un serveur tiers. Elles ne sont acceptées que des deux
# couches que l'utilisateur contrôle vraiment.
#
# Par MOTIF et non par liste nominative, pour la raison qui vaut déjà pour les
# secrets dans `providers/base.py` : l'énumération ne tient pas. Recensé sur
# les SDK installés, douze variables de routage sont lues, dont six par le seul
# client Anthropic (`ANTHROPIC_BASE_URL`, `…_VERTEX_BASE_URL`, `…_FOUNDRY_…`) ;
# une liste écrite à la main en aurait oublié la moitié, et un SDK mis à jour
# en ajoute sans prévenir.
_ROUTING_SUFFIXES = ("_BASE_URL", "_API_BASE", "_ENDPOINT")
# Nommées, celles qui ne suivent aucun motif :
#  - proxies : httpx les lit tout seul (`trust_env`) et route tout le trafic ;
#  - magasins de certificats : les pointer sur une AC contrôlée rend un
#    intercepteur indiscernable d'un vrai serveur ;
#  - emplacement de la configuration utilisateur : le poser, c'est décider
#    quel fichier constitue la couche 3, donc contourner ce filtre par la bande.
_ROUTING_NAMES = (
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
    "SSL_CERT_FILE",
    "SSL_CERT_DIR",
    "REQUESTS_CA_BUNDLE",
    "CURL_CA_BUNDLE",
    "XDG_CONFIG_HOME",
    "APPDATA",
)


def _is_routing_variable(name):
    """Vrai si `name` peut détourner ou intercepter une requête."""
    majuscule = name.upper()
    return majuscule in _ROUTING_NAMES or majuscule.endswith(_ROUTING_SUFFIXES)


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

    Exception à la couche 2 : elle ne peut poser aucune variable de routage,
    cf. `_is_routing_variable` — un `.env` de projet qui redirige les appels
    détournerait une clé qu'il ne connaît pas.

    Le contournement que cela ferme, reproduit en processus neuf : le projet
    posait `XDG_CONFIG_HOME` vers un répertoire qu'il contrôle, dont
    l'`aipmt/.env` fournissait ensuite l'URL hostile — le filtre était
    contourné par la couche 3 elle-même. La variable fait donc partie des
    variables de routage, et le chemin est en outre résolu AVANT la lecture du
    projet : le filtre suffit à fermer le trou, mais l'ordre garantit que le
    message d'avertissement nomme la VRAIE configuration utilisateur et non
    celle que le projet aurait désignée.
    """
    user_path = _user_config_path()
    avant = {name for name in os.environ if _is_routing_variable(name)}
    load_dotenv(find_dotenv(usecwd=True))
    _drop_project_routing(avant, user_path)
    load_dotenv(user_path)


def _drop_project_routing(avant, user_path):
    """Retire les variables de routage que le `.env` du projet vient de poser.

    Appelée ENTRE les deux couches : ce qui vient d'apparaître ne peut venir
    que du projet, et la configuration utilisateur pourra encore fournir la
    sienne juste après. Le refus est dit sur stderr — silencieux, il ferait
    chercher pourquoi un relais légitime n'est pas pris en compte."""
    for name in [n for n in os.environ if _is_routing_variable(n) and n not in avant]:
        valeur = os.environ.pop(name)
        print(
            f"⚠ {name}={valeur} ignoré : un .env de projet ne peut pas rediriger les "
            "appels d'API, sinon un répertoire non fiable détournerait votre clé. "
            f"L'exporter dans l'environnement, ou le mettre dans {user_path}.",
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
