"""Façade de compatibilité du module historique `aipmt.translate`.

Jusqu'à la 1.13.0, toute la logique vivait dans ce seul fichier, publié tel
quel sur PyPI : `aipmt.translate` est donc un chemin d'import public de fait.
Le code est désormais réparti en modules (`segmentation`, `pipeline`, `cli`,
`providers/`…) et ce fichier n'en définit plus aucun : il ré-exporte, par
identité d'objet, chaque nom que le module exposait sans préfixe `_`.

Deux niveaux, volontairement distincts :

- `__all__` porte l'API SUPPORTÉE — les neuf noms documentés, que le projet
  s'engage à conserver ici ;
- les autres noms sont des ALIAS DE COMPATIBILITÉ : ils restent accessibles
  pour ne casser aucun import existant, sans être promus API publique. Leur
  définition vit dans leur module ; c'est là qu'il faut lire, et là qu'il
  faut patcher dans un test — jamais ici, un patch posé sur la façade ne
  touche pas le nom que le code consulte (`tests/test_facade_contract.py`
  l'interdit).

Aucun nom privé, aucun SDK, aucun module de la bibliothèque standard n'est
ré-exporté : les 29 ré-exports accidentels de l'ancien module unique ont
disparu avec lui. Le `__module__` des fonctions ré-exportées est celui de leur
module de définition.
"""

# --- API supportée --------------------------------------------------------
# --- Alias de compatibilité (non documentés, conservés) -------------------
from .cli import DEFAULT_SOURCE_DIR as DEFAULT_SOURCE_DIR
from .cli import DEFAULT_SOURCE_LANG as DEFAULT_SOURCE_LANG
from .cli import DEFAULT_TARGET_DIR as DEFAULT_TARGET_DIR
from .cli import DEFAULT_TARGET_LANG as DEFAULT_TARGET_LANG
from .cli import main as main
from .markdown import news_quote_placeholder as news_quote_placeholder
from .markdown import news_quote_placeholder_regex as news_quote_placeholder_regex
from .naming import EXCLUDE_PATTERNS as EXCLUDE_PATTERNS
from .naming import is_excluded as is_excluded
from .news import LANG_FLAGS as LANG_FLAGS
from .pipeline import translate as translate
from .pipeline import translate_directory as translate_directory
from .pipeline import translate_markdown_file as translate_markdown_file
from .providers.anthropic import CLAUDE_MAX_TOKENS as CLAUDE_MAX_TOKENS
from .providers.anthropic import CLAUDE_TIMEOUT as CLAUDE_TIMEOUT
from .providers.anthropic import DEFAULT_ANTHROPIC_API_KEY as DEFAULT_ANTHROPIC_API_KEY
from .providers.anthropic import DEFAULT_MODEL_CLAUDE as DEFAULT_MODEL_CLAUDE
from .providers.anthropic import ECO_MODEL_CLAUDE as ECO_MODEL_CLAUDE
from .providers.base import CODEX_TERM_GRACE as CODEX_TERM_GRACE
from .providers.codex import CODEX_AGENT_CONTRACT as CODEX_AGENT_CONTRACT
from .providers.codex import CODEX_MODEL_PREFIXES as CODEX_MODEL_PREFIXES
from .providers.codex import CODEX_STRIPPED_ENV_VARS as CODEX_STRIPPED_ENV_VARS
from .providers.codex import CODEX_TIMEOUT as CODEX_TIMEOUT
from .providers.codex import DEFAULT_MODEL_CODEX as DEFAULT_MODEL_CODEX
from .providers.codex import ECO_MODEL_CODEX as ECO_MODEL_CODEX
from .providers.gemini import DEFAULT_GEMINI_API_KEY as DEFAULT_GEMINI_API_KEY
from .providers.gemini import DEFAULT_MODEL_GEMINI as DEFAULT_MODEL_GEMINI
from .providers.gemini import ECO_MODEL_GEMINI as ECO_MODEL_GEMINI
from .providers.grok import DEFAULT_MODEL_GROK as DEFAULT_MODEL_GROK
from .providers.grok import DEFAULT_MODEL_GROK_CLI as DEFAULT_MODEL_GROK_CLI
from .providers.grok import DEFAULT_XAI_API_KEY as DEFAULT_XAI_API_KEY
from .providers.grok import ECO_MODEL_GROK as ECO_MODEL_GROK
from .providers.grok import ECO_MODEL_GROK_CLI as ECO_MODEL_GROK_CLI
from .providers.grok import GROK_AGENT_CONTRACT as GROK_AGENT_CONTRACT
from .providers.grok import GROK_DENY_RULES as GROK_DENY_RULES
from .providers.grok import GROK_ENV_KILL_SWITCHES as GROK_ENV_KILL_SWITCHES
from .providers.grok import GROK_MAX_TURNS as GROK_MAX_TURNS
from .providers.grok import GROK_PROMPT_FILENAME as GROK_PROMPT_FILENAME
from .providers.grok import GROK_SANDBOX_ENV_VAR as GROK_SANDBOX_ENV_VAR
from .providers.grok import GROK_STRIPPED_ENV_VARS as GROK_STRIPPED_ENV_VARS
from .providers.grok import GROK_TIMEOUT as GROK_TIMEOUT
from .providers.grok import XAI_BASE_URL as XAI_BASE_URL
from .providers.mistral import DEFAULT_MISTRAL_API_KEY as DEFAULT_MISTRAL_API_KEY
from .providers.mistral import DEFAULT_MODEL_MISTRAL as DEFAULT_MODEL_MISTRAL
from .providers.mistral import ECO_MODEL_MISTRAL as ECO_MODEL_MISTRAL
from .providers.openai import DEFAULT_MODEL_OPENAI as DEFAULT_MODEL_OPENAI
from .providers.openai import DEFAULT_OPENAI_API_KEY as DEFAULT_OPENAI_API_KEY
from .providers.openai import ECO_MODEL_OPENAI as ECO_MODEL_OPENAI
from .providers.opencode import OPENCODE_AGENT_CONTRACT as OPENCODE_AGENT_CONTRACT
from .providers.opencode import OPENCODE_AGENT_NAME as OPENCODE_AGENT_NAME
from .providers.opencode import OPENCODE_ENV_KILL_SWITCHES as OPENCODE_ENV_KILL_SWITCHES
from .providers.opencode import OPENCODE_KEPT_ENV_VARS as OPENCODE_KEPT_ENV_VARS
from .providers.opencode import OPENCODE_SESSION_TITLE as OPENCODE_SESSION_TITLE
from .providers.opencode import OPENCODE_TIMEOUT as OPENCODE_TIMEOUT
from .providers.openrouter import DEFAULT_OPENROUTER_API_KEY as DEFAULT_OPENROUTER_API_KEY
from .providers.openrouter import OPENROUTER_BASE_URL as OPENROUTER_BASE_URL
from .providers.openrouter import OPENROUTER_EFFORTS_CROISSANTS as OPENROUTER_EFFORTS_CROISSANTS
from .providers.openrouter import OPENROUTER_MAX_TOKENS as OPENROUTER_MAX_TOKENS
from .providers.openrouter import (
    OPENROUTER_MIN_COMPLETION_TOKENS as OPENROUTER_MIN_COMPLETION_TOKENS,
)
from .providers.openrouter import OPENROUTER_PREFLIGHT_TIMEOUT as OPENROUTER_PREFLIGHT_TIMEOUT
from .providers.openrouter import OPENROUTER_TIMEOUT as OPENROUTER_TIMEOUT
from .segmentation import DEFAULT_TOKEN_LIMIT as DEFAULT_TOKEN_LIMIT
from .segmentation import MODEL_TOKEN_LIMITS as MODEL_TOKEN_LIMITS
from .segmentation import segment_text as segment_text

__all__ = [
    "DEFAULT_TOKEN_LIMIT",
    "EXCLUDE_PATTERNS",
    "LANG_FLAGS",
    "MODEL_TOKEN_LIMITS",
    "main",
    "segment_text",
    "translate",
    "translate_directory",
    "translate_markdown_file",
]
