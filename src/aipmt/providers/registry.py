"""Résolution, sélection et dispatch des providers.

Un provider est identifié par une clé (`codex`, `grok_cli`…) résolue depuis les
flags ; à chaque clé correspondent un libellé, un constructeur de client et un
appel de traduction. Les cinq fonctions de ce module sont déplacées telles
quelles depuis le module principal : leurs chaînes if/elif restent le contrat
observable (précédence, libellés, ordre de l'aide) jusqu'à ce qu'un registre
déclaratif les remplace, dans un changement nommé comme tel.
"""

from .anthropic import _call_claude, _init_claude_client
from .codex import _call_codex, _init_codex_client
from .gemini import _call_gemini, _init_gemini_client
from .grok import _call_grok_cli, _init_grok_cli_client, _init_grok_client
from .mistral import _call_mistral, _init_mistral_client
from .openai import _call_openai, _init_openai_client
from .opencode import _call_opencode, _init_opencode_client
from .openrouter import _call_openrouter, _init_openrouter_client


def _resolve_provider(args, use_mistral=False, use_claude=False, use_gemini=False):
    """Nom du provider à utiliser. Les booléens explicites priment (plusieurs
    tests appellent `translate(..., use_mistral=True)` avec un Namespace qui
    n'a aucun attribut `use_*`), `args` ne sert que de repli."""
    if use_mistral:
        return "mistral"
    if use_claude:
        return "claude"
    if use_gemini:
        return "gemini"
    if getattr(args, "use_codex", False):
        return "codex"
    if getattr(args, "use_grok_cli", False):
        return "grok_cli"
    if getattr(args, "use_grok", False):
        return "grok"
    if getattr(args, "use_opencode", False):
        return "opencode"
    if getattr(args, "use_openrouter", False):
        return "openrouter"
    return "openai"


# `provider` sert de clé de dispatch, pas de libellé : `.capitalize()` affichait
# « Grok_cli » et « Openai » à l'utilisateur.
_PROVIDER_LABELS = {
    "openai": "OpenAI",
    "mistral": "Mistral",
    "claude": "Claude",
    "gemini": "Gemini",
    "codex": "Codex CLI",
    "grok": "Grok (API xAI)",
    "grok_cli": "Grok CLI",
    "opencode": "OpenCode",
    "openrouter": "OpenRouter",
}


def _dispatch_provider_call(client, args, prompt, segment, provider, is_translation_note):
    if provider == "mistral":
        text = _call_mistral(client, args, prompt, segment)
    elif provider == "claude":
        text = _call_claude(client, args, prompt, segment)
    elif provider == "gemini":
        text = _call_gemini(client, args, prompt, segment)
    elif provider == "codex":
        text = _call_codex(client, args, prompt, segment)
    elif provider == "grok_cli":
        text = _call_grok_cli(client, args, prompt, segment)
    elif provider == "opencode":
        text = _call_opencode(client, args, prompt, segment)
    elif provider == "openrouter":
        text = _call_openrouter(client, args, prompt, segment)
    else:
        # `grok` (API xAI) inclus : endpoint compatible OpenAI, donc même appel.
        text = _call_openai(client, args, prompt, segment, is_translation_note)
    # Empty-content guard : un provider qui retourne "" avec finish_reason="stop"
    # produirait sinon un fichier vide marqué success.
    if not text.strip():
        raise RuntimeError(
            f"{_PROVIDER_LABELS[provider]} returned empty content (model={args.model})"
        )
    return text


def _add_provider_args(parser):
    parser.add_argument(
        "--model",
        type=str,
        help=(
            "Modèle à utiliser pour la traduction ; la valeur par défaut dépend du "
            "provider sélectionné. Obligatoire avec --use_opencode et "
            "--use_openrouter, au format provider/modèle (liste : "
            "`opencode models`, https://openrouter.ai/models)"
        ),
    )
    # Groupe exclusif : deux flags provider simultanés étaient acceptés en
    # silence, et la précédence divergeait entre _select_provider_client (qui
    # teste Mistral en premier) et _resolve_provider (qui donne priorité aux
    # booléens explicites). `--use_codex --use_mistral` instanciait donc un
    # client Mistral ET dispatchait vers Mistral : la traduction partait en
    # facturation à l'usage alors que l'utilisateur avait demandé son quota
    # d'abonnement — exactement ce que --use_codex existe pour empêcher, et
    # sans le moindre avertissement. argparse refuse désormais la combinaison.
    provider_group = parser.add_mutually_exclusive_group()
    provider_group.add_argument(
        "--use_mistral", action="store_true", help="Utiliser l'API Mistral AI pour la traduction"
    )
    provider_group.add_argument(
        "--use_claude",
        action="store_true",
        help="Utiliser l'API Claude d'Anthropic pour la traduction",
    )
    provider_group.add_argument(
        "--use_gemini",
        action="store_true",
        help="Utiliser l'API Gemini de Google pour la traduction",
    )
    provider_group.add_argument(
        "--use_grok",
        action="store_true",
        help="Utiliser l'API xAI (Grok) — nécessite XAI_API_KEY, facturé à l'usage",
    )
    provider_group.add_argument(
        "--use_grok_cli",
        action="store_true",
        help=(
            "Utiliser le CLI Grok sur le quota de l'abonnement Grok "
            "(nécessite `grok login` ; confinement plus faible que --use_codex)"
        ),
    )
    provider_group.add_argument(
        "--use_codex",
        action="store_true",
        help=(
            "Utiliser le CLI Codex sur le quota de l'abonnement ChatGPT "
            "(aucune facturation à l'usage ; nécessite `codex login`)"
        ),
    )
    provider_group.add_argument(
        "--use_opencode",
        action="store_true",
        help=(
            "Utiliser OpenCode (agent open source) vers le fournisseur configuré "
            "dans OpenCode — modèle local, gratuit, abonnement ou clé ; exige "
            "--model provider/modèle"
        ),
    )
    provider_group.add_argument(
        "--use_openrouter",
        action="store_true",
        help=(
            "Utiliser OpenRouter (routeur vers ~430 modèles) — nécessite "
            "OPENROUTER_API_KEY, facturé à l'usage ; exige --model fournisseur/modèle"
        ),
    )
    parser.add_argument(
        "--eco",
        action="store_true",
        help="Utiliser les modèles économiques (mini/flash) au lieu des modèles qualité",
    )
    parser.add_argument(
        "--reasoning_effort",
        choices=("none", "low", "medium", "high", "xhigh"),
        default=None,
        help=(
            "Effort de raisonnement OpenAI GPT-5.x. Par défaut : 'none' avec "
            "--eco (le raisonnement n'apporte rien à une traduction et double "
            "les tokens de sortie), 'medium' sinon. Toutes les valeurs ne sont "
            "pas acceptées par tous les modèles ; un refus déclenche un retry "
            "sans le paramètre."
        ),
    )


def _select_provider_client(args):
    if args.use_mistral:
        return _init_mistral_client(args)
    if args.use_claude:
        return _init_claude_client(args)
    if args.use_gemini:
        return _init_gemini_client(args)
    if getattr(args, "use_codex", False):
        return _init_codex_client(args)
    if getattr(args, "use_grok_cli", False):
        return _init_grok_cli_client(args)
    if getattr(args, "use_grok", False):
        return _init_grok_client(args)
    if getattr(args, "use_opencode", False):
        return _init_opencode_client(args)
    if getattr(args, "use_openrouter", False):
        return _init_openrouter_client(args)
    return _init_openai_client(args)
