"""Provider OpenRouter : un routeur payant devant ~430 modèles hébergés par des tiers.

Tout ce qui distingue ce provider tient dans un préflight mesuré sur l'API :
épinglage des hébergeurs dont le plafond de sortie tient la traduction,
raisonnement coupé quand le modèle le permet et plus bas effort accepté sinon,
fenêtre de contexte lue au catalogue et inscrite dans `MODEL_TOKEN_LIMITS`.
"""

import json
import os
import sys
import urllib.request
from dataclasses import dataclass

from openai import OpenAI

from ..config import _missing_key_message
from ..segmentation import DEFAULT_TOKEN_LIMIT, MODEL_TOKEN_LIMITS
from .base import _NAMESPACED_MODEL_REGEX, _reason_name
from .openai import _build_openai_messages

DEFAULT_OPENROUTER_API_KEY = "votre-cle-api-openrouter-par-defaut"  # pragma: allowlist secret


# --- Provider OpenRouter (routeur, facturé à l'usage) -----------------------
# Endpoint compatible OpenAI lui aussi ; ce qui change est en amont de
# l'appel, dans le préflight qui épingle les hébergeurs (cf. _openrouter_pin).
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"


OPENROUTER_TIMEOUT = float(os.getenv("OPENROUTER_TIMEOUT", "900"))


OPENROUTER_PREFLIGHT_TIMEOUT = float(os.getenv("OPENROUTER_PREFLIGHT_TIMEOUT", "30"))


# Plancher de sortie exigé d'un hébergeur. 8 000 tokens couvrent largement un
# segment de 16 000 tokens d'entrée traduit ; le seuil sert à écarter les
# hébergeurs à 2 048 qui tronqueraient sans le dire, pas à dimensionner.
OPENROUTER_MIN_COMPLETION_TOKENS = 8000


# Enveloppe demandée. Généreuse à dessein : sur un modèle qui impose le
# raisonnement, celui-ci se sert en premier dans cette enveloppe.
OPENROUTER_MAX_TOKENS = 32768


# Efforts de raisonnement du moins au plus coûteux, tels que le catalogue les
# nomme. L'ordre sert à choisir le PLUS BAS que le modèle accepte quand il
# impose de raisonner : mesuré sur z-ai/glm-5.3-flash, dont le défaut est
# `max`, laisser ce défaut sature les 32 768 tokens de sortie AVANT la fin de
# la traduction — l'effort alloue un pourcentage de l'enveloppe, et augmenter
# l'enveloppe augmente le raisonnement d'autant.
OPENROUTER_EFFORTS_CROISSANTS = ("minimal", "low", "medium", "high", "xhigh", "max")


# --- Provider OpenRouter (routeur multi-fournisseurs, facturé à l'usage) -----
#
# OpenRouter n'est pas un fournisseur, c'est un routeur devant ~430 modèles
# hébergés par des tiers. Deux mesures dictent tout ce qui suit.
#
# 1. Un même slug est servi par des dizaines d'hébergeurs aux plafonds
#    différents. Sur `z-ai/glm-5.3-flash` : 23 hébergeurs, dont un plafonné à
#    2 048 tokens de sortie. Sans épinglage, une traduction longue sur 23
#    partait tronquée, au hasard du routage et sans le moindre signal. D'où le
#    préflight, qui est fail-closed : pas de catalogue, pas de traduction.
# 2. Le raisonnement est facturé au tarif de sortie. Même requête sur
#    `z-ai/glm-5.2`, réponse « OK » : 107 tokens de complétion au défaut du
#    modèle, 2 avec le raisonnement coupé. Un facteur 18 sur chaque segment de
#    chaque fichier, pour une tâche à laquelle le raisonnement n'apporte rien.
def _openrouter_http_get(base_url, path):
    """GET JSON sur l'API OpenRouter. Le catalogue est public : pas de clé ici,
    donc rien à fuiter si l'URL de base est détournée.

    `urllib` plutôt que `httpx` : le préflight tient en deux GET, et déclarer
    une dépendance directe de plus n'aurait acheté que du bruit."""
    base = os.getenv("OPENROUTER_BASE_URL", OPENROUTER_BASE_URL) if base_url is None else base_url
    if not base.startswith("https://"):
        raise ValueError(f"OPENROUTER_BASE_URL doit commencer par https:// (reçu {base!r})")
    url = f"{base.rstrip('/')}/{path.lstrip('/')}"
    # Le marqueur est SUR la ligne de l'appel : bandit ne le lit pas une ligne
    # plus haut, contrairement à semgrep. Le délai est sorti en variable courte
    # pour que ruff-format ne puisse pas scinder la ligne et emporter le
    # marqueur ailleurs — le même piège avait déjà défait un `# nosemgrep`.
    delai = OPENROUTER_PREFLIGHT_TIMEOUT
    try:
        with urllib.request.urlopen(url, timeout=delai) as reponse:  # nosec B310 — https vérifié
            return json.loads(reponse.read().decode("utf-8"))
    except (OSError, ValueError) as e:
        raise ValueError(f"Préflight OpenRouter injoignable ({url}) : {e}") from e


def _openrouter_catalog_entry(base_url, model):
    """Fiche catalogue du modèle demandé.

    Fail-closed : un slug absent du catalogue est une faute de frappe, pas un
    modèle à tenter quand même. Le laisser passer produirait un 400 opaque au
    milieu d'un lot de fichiers, après la première facturation."""
    payload = _openrouter_http_get(base_url, "models")
    for entry in payload.get("data") or []:
        if entry.get("id") == model:
            return entry
    raise ValueError(
        f"Modèle OpenRouter inconnu : {model!r}. Catalogue sur "
        "https://openrouter.ai/models, au format « fournisseur/modèle »."
    )


def _openrouter_endpoints(base_url, model):
    payload = _openrouter_http_get(base_url, f"models/{model}/endpoints")
    return (payload.get("data") or {}).get("endpoints") or []


def _openrouter_pin(endpoints):
    """Hébergeurs retenus, et plafond de sortie commun à ceux-là.

    Deux filtres, tous deux mesurés. Un `status` négatif marque un hébergeur
    que le routeur lui-même déprioritise (3 sur 23 pour glm-5.3-flash). Un
    plafond de sortie sous OPENROUTER_MIN_COMPLETION_TOKENS tronque une
    traduction longue en silence — c'est le défaut que le préflight existe pour
    empêcher. Un plafond non déclaré (`None`) est un inconnu, donc écarté :
    l'objet de cette fonction est justement de ne rien laisser au hasard."""
    usable = [
        e
        for e in endpoints
        if (e.get("status") or 0) >= 0
        and (e.get("max_completion_tokens") or 0) >= OPENROUTER_MIN_COMPLETION_TOKENS
    ]
    tags = tuple(e["tag"] for e in usable if e.get("tag"))
    ceiling = min((e["max_completion_tokens"] for e in usable), default=0)
    return tags, ceiling


@dataclass
class _OpenRouterClient:
    """Client OpenRouter : le client OpenAI, plus ce que le préflight a mesuré.

    Ces trois champs ne sont pas des préférences, ce sont des contraintes lues
    sur le catalogue au démarrage — la liste d'hébergeurs dont aucun ne
    tronque, le plafond de sortie qu'ils tiennent tous, et le fait que le
    modèle impose ou non de raisonner."""

    client: object
    providers: tuple = ()
    max_tokens: int = OPENROUTER_MAX_TOKENS
    reasoning_mandatory: bool = False
    supported_efforts: tuple = ()


def _openrouter_reasoning(client, args):
    """Bloc `reasoning` de la requête, ou `None` pour n'en envoyer aucun.

    Par défaut le raisonnement est COUPÉ quand le modèle le permet : mesuré sur
    z-ai/glm-5.2, la même réponse coûte 2 tokens de complétion au lieu de 107.
    Quand le modèle l'impose, on n'envoie rien plutôt que de deviner un effort —
    l'effort alloue un pourcentage de `max_tokens` et le raisonnement se sert en
    premier, si bien qu'une valeur choisie au hasard déplace le risque de page
    blanche au lieu de le réduire."""
    effort = getattr(args, "reasoning_effort", None)
    if effort not in (None, "none"):
        return {"effort": effort}
    if not client.reasoning_mandatory:
        return {"enabled": False}
    plus_bas = _openrouter_lowest_effort(client.supported_efforts)
    return {"effort": plus_bas} if plus_bas else None


def _openrouter_lowest_effort(supported):
    """Le plus bas effort que le modèle déclare accepter, ou `None`.

    Mesuré : laisser son défaut à un modèle qui impose le raisonnement — `max`
    pour z-ai/glm-5.3-flash — fait dépasser l'enveloppe de sortie AVANT la fin
    de la traduction, et l'erreur est alors une troncature, pas une page
    blanche. Augmenter `max_tokens` n'y changerait rien : l'effort alloue un
    pourcentage de cette enveloppe, le raisonnement grandit avec elle."""
    connus = [e for e in OPENROUTER_EFFORTS_CROISSANTS if e in (supported or ())]
    return connus[0] if connus else None


def _openrouter_reasoning_label(client, args):
    """Décrit le raisonnement tel qu'il sera ENVOYÉ. Le dériver de
    `mandatory` seul annonçait « coupé » alors qu'un `--reasoning_effort`
    explicite partait dans la requête."""
    reasoning = _openrouter_reasoning(client, args)
    if reasoning is None:
        return "imposé par le modèle, à son réglage par défaut"
    if reasoning.get("enabled") is False:
        return "coupé"
    # Un effort non demandé par l'utilisateur a été choisi ici : le dire, sinon
    # le message laisse croire qu'il vient de la ligne de commande.
    demande = getattr(args, "reasoning_effort", None)
    origine = (
        "" if demande and demande != "none" else " (imposé par le modèle, le plus bas accepté)"
    )
    return f"effort {reasoning['effort']!r}{origine}"


def _openrouter_extra_body(client, args):
    """`allow_fallbacks: false` est indispensable : sans lui, `only` n'est
    qu'une préférence et le routeur repart vers un hébergeur écarté, ce qui vide
    le préflight de son sens."""
    body = {"provider": {"only": list(client.providers), "allow_fallbacks": False}}
    reasoning = _openrouter_reasoning(client, args)
    if reasoning is not None:
        body["reasoning"] = reasoning
    return body


def _openrouter_first_choice(response, args):
    """Premier choix de la réponse, ou une erreur qui nomme la vraie cause.

    OpenRouter répond 200 avec un corps qui ne porte qu'une erreur quand
    l'hébergeur amont échoue. Sans cette garde, `choices[0]` levait un
    TypeError opaque qui masquait le message du routeur."""
    error = getattr(response, "error", None) or (
        response.get("error") if isinstance(response, dict) else None
    )
    if error:
        raise RuntimeError(f"OpenRouter a répondu une erreur (model={args.model}) : {error}")
    choices = getattr(response, "choices", None)
    if not choices:
        raise RuntimeError(
            f"OpenRouter n'a renvoyé aucun choix (model={args.model}) — "
            "réponse sans contenu ni erreur exploitable"
        )
    return choices[0]


def _openrouter_check_finish(choice, client, args, content):
    """Contrat de sortie : distingue la page blanche de la vraie troncature.

    `finish_reason=length` avec un texte vide n'est pas une traduction trop
    longue, c'est le budget de sortie consommé par le raisonnement avant le
    premier caractère utile — mesuré à 15 850 tokens de raisonnement pour 148
    utiles. Les deux cas demandent des gestes opposés, les confondre envoie
    l'utilisateur réduire une taille de segment qui n'est pas en cause."""
    finish = _reason_name(choice.finish_reason)
    native = _reason_name(getattr(choice, "native_finish_reason", None))
    if finish == "length":
        if not content:
            raise RuntimeError(
                f"OpenRouter : budget de sortie ({client.max_tokens} tokens) consommé par le "
                f"raisonnement avant tout texte (model={args.model}). Relancer à l'identique "
                "ne changera rien : couper le raisonnement, ou choisir un modèle qui ne l'impose pas."
            )
        raise RuntimeError(
            f"OpenRouter : sortie tronquée à {client.max_tokens} tokens "
            f"(model={args.model}, finish_reason=length)"
        )
    # `error` est la valeur que le routeur NORMALISE quand l'hébergeur amont
    # échoue en cours de génération. Mesuré sur z-ai/glm-5.3-flash : deux
    # segments coupés à 750 s exactement, `native_finish_reason` à None. Le dire
    # évite de chercher un défaut dans le document ou dans le découpage.
    if finish == "error":
        raise RuntimeError(
            f"OpenRouter : l'hébergeur a interrompu la génération (model={args.model}, "
            f"finish_reason=error, natif={native!r}). Panne côté fournisseur, pas côté "
            "document : réessayer, ou restreindre les hébergeurs retenus."
        )
    # `end_turn` est la forme émise par certains hébergeurs là où OpenAI émet
    # `stop` ; `native_finish_reason` porte la valeur non normalisée de l'amont.
    if finish not in ("stop", "STOP", "end_turn", None):
        raise RuntimeError(
            f"OpenRouter finish_reason anormal={finish!r} (natif={native!r}, model={args.model})"
        )


def _call_openrouter(client, args, prompt, segment):
    messages = _build_openai_messages(args, prompt, segment)
    response = client.client.chat.completions.create(
        model=args.model,
        messages=messages,
        max_tokens=client.max_tokens,
        extra_body=_openrouter_extra_body(client, args),
    )
    choice = _openrouter_first_choice(response, args)
    content = (getattr(choice.message, "content", None) or "").strip()
    _openrouter_check_finish(choice, client, args, content)
    if not content:
        raise RuntimeError(
            f"OpenRouter returned empty content (model={args.model}, "
            f"finish_reason={_reason_name(choice.finish_reason)!r})"
        )
    return content


def _openrouter_validate_model(model):
    """Valide la FORME du slug avant tout appel réseau.

    Ce slug est interpolé dans l'URL de préflight : la validation n'est pas une
    politesse d'ergonomie mais la garde qui empêche d'y injecter un chemin. La
    regex commune aux deux providers namespacés accepte `a/b/..`, d'où le refus
    explicite du segment parent."""
    if not model:
        raise ValueError(
            "--use_openrouter exige --model au format fournisseur/modèle. OpenRouter "
            "n'est pas un fournisseur mais un routeur vers ~430 modèles tiers, et "
            "aucun défaut n'est choisi à votre place — le choix engage le prix, la "
            "licence et le traitement de vos données.\n"
            "  Catalogue : https://openrouter.ai/models\n"
            "  Exemples : --model z-ai/glm-5.2, --model qwen/qwen3.8-flash"
        )
    if not _NAMESPACED_MODEL_REGEX.match(model) or ".." in model.split("/"):
        raise ValueError(
            f"Modèle OpenRouter invalide : {model!r}. Attendu fournisseur/modèle, "
            "ex. z-ai/glm-5.2 (catalogue : https://openrouter.ai/models)."
        )


def _init_openrouter_client(args):
    """Provider OpenRouter. L'appel est compatible OpenAI ; ce qui distingue ce
    provider tient dans le préflight, dont le résultat est affiché parce qu'il
    engage la dépense et la fidélité de la sortie."""
    _openrouter_validate_model(args.model)
    api_key = os.getenv("OPENROUTER_API_KEY", DEFAULT_OPENROUTER_API_KEY)
    if not api_key or api_key == DEFAULT_OPENROUTER_API_KEY:
        raise ValueError(
            _missing_key_message(
                "OpenRouter",
                ["OPENROUTER_API_KEY"],
                hint=" Clé à obtenir sur openrouter.ai/keys.",
            )
        )
    if args.eco:
        print(
            "⚠ --eco est sans effet avec --use_openrouter : le modèle est celui de --model.",
            file=sys.stderr,
        )
    base_url = os.getenv("OPENROUTER_BASE_URL", OPENROUTER_BASE_URL)
    entry = _openrouter_catalog_entry(base_url, args.model)
    endpoints = _openrouter_endpoints(base_url, args.model)
    providers, ceiling = _openrouter_pin(endpoints)
    if not providers:
        raise ValueError(
            f"Aucun hébergeur utilisable pour {args.model!r} : {len(endpoints)} évalué(s), "
            f"aucun ne déclare au moins {OPENROUTER_MIN_COMPLETION_TOKENS} tokens de sortie "
            "avec un statut sain. Traduire ici reviendrait à accepter une troncature "
            "silencieuse — choisir un autre modèle."
        )
    # Le catalogue connaît la vraie fenêtre : la renseigner évite que la
    # segmentation retombe sur DEFAULT_TOKEN_LIMIT, faux pour 44 des 431
    # modèles — dont deux plafonnés à 4 095 tokens.
    context_length = int(entry.get("context_length") or DEFAULT_TOKEN_LIMIT)
    MODEL_TOKEN_LIMITS[args.model] = context_length
    reasoning = entry.get("reasoning") or {}
    mandatory = bool(reasoning.get("mandatory"))
    client = _OpenRouterClient(
        client=OpenAI(api_key=api_key, base_url=base_url, timeout=OPENROUTER_TIMEOUT),
        providers=providers,
        max_tokens=min(OPENROUTER_MAX_TOKENS, ceiling),
        reasoning_mandatory=mandatory,
        supported_efforts=tuple(reasoning.get("supported_efforts") or ()),
    )
    if mandatory and getattr(args, "reasoning_effort", None) == "none":
        print(
            f"⚠ --reasoning_effort=none ignoré : {args.model} impose le raisonnement "
            "(reasoning.mandatory sur le catalogue OpenRouter)",
            file=sys.stderr,
        )
    print(
        f"→ OpenRouter : {len(providers)} hébergeur(s) épinglé(s) sur {len(endpoints)}, "
        f"contexte {context_length} tokens, sortie plafonnée à {client.max_tokens}, "
        f"raisonnement {_openrouter_reasoning_label(client, args)}"
    )
    return client
