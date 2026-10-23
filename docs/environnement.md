# Environment Variables

Les clés sont résolues en **trois couches**, de la plus prioritaire à la moindre :
variable d'environnement → `.env` du répertoire courant (ou d'un parent) →
`~/.config/aipmt/.env`. La priorité n'est pas codée : elle découle de
`override=False`, valeur par défaut de `load_dotenv`, chaque couche ne comblant
que ce que la précédente a laissé vide (`_load_configuration`).

La troisième couche existe parce qu'une CLI installée n'en avait aucune de
persistante. `find_dotenv` remonte jusqu'à la racine du système et trouvait donc
un `~/.env` **quand on travaillait sous son répertoire personnel**, mais rien
ailleurs — une couverture qui dépendait de l'endroit d'où l'on lançait la
commande. `_user_config_path()` suit `XDG_CONFIG_HOME` s'il est ABSOLU (la
spécification demande d'ignorer une valeur relative, sans quoi l'emplacement
redeviendrait fonction du répertoire courant) et `APPDATA` sous Windows.

**La couche projet ne fournit que des clés.** Le `.env` est cherché depuis le
répertoire courant et ses parents : un dépôt qu'on vient de cloner peut en
poser un. `_drop_project_routing`, appelée entre la couche projet et la couche
utilisateur, retire ce que le projet vient de poser parmi les variables qui
décident où part une requête ou quel programme s'exécute
(`_is_routing_variable`, casse ignorée) : tout nom en `_BASE_URL`, `_API_BASE`,
`_ENDPOINT` ou `_BIN` — un MOTIF, parce que douze variables de routage ont été
recensées dans les SDK installés, dont six pour le seul client Anthropic —,
plus `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`, `SSL_CERT_FILE`, `SSL_CERT_DIR`,
`REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`, `XDG_CONFIG_HOME`, `APPDATA` et
`GROK_HOME`. `_BIN` et `GROK_HOME` depuis la 1.15.0 : `CODEX_BIN`, `GROK_BIN`,
`OPENCODE_BIN`, `AGY_BIN` et `$GROK_HOME/bin/grok` désignent le binaire que la
traduction EXÉCUTE, avec les droits de l'utilisateur — posés par le `.env` d'un
dépôt cloné, ils faisaient lancer un fichier de ce dépôt. Toutes restent
acceptées de l'environnement exporté et de `~/.config/aipmt/.env`. Chaque refus
est dit sur stderr par son NOM seul : une valeur `https://${CLE}@hôte/` ferait
fuir la clé dans les journaux. La couche projet est en outre lue sans
interpolation (`interpolate=False`) : `NOM_ANODIN=${OPENAI_API_KEY}` y
recopiait la vraie clé sous un nom que le filtrage par motif des
sous-processus ne reconnaît pas. `regen_translations.sh` exporte le `.env` de
CE dépôt (`set -a`) avant d'appeler aipmt : ses variables y arrivent donc par
l'environnement, que le filtre ne touche pas — voulu, c'est le dépôt du
propriétaire, et le script lit lui-même `GROK_BIN` et `AGY_BIN` pour ses
contrôles préalables.

Le trousseau système (`keyring`) a été écarté comme défaut : il échoue en
headless — serveur, conteneur, CI — c'est-à-dire le cas d'usage même d'une
traduction par lot. Un flag `--api-key` l'a été aussi : la clé atterrirait dans
l'historique du shell et serait visible dans `ps`.

Sans clé, `main()` n'affiche plus de trace d'appel. Le filet est **étroit à
dessein** : `except ValueError` sur la seule phase de configuration. Envelopper
toute l'exécution transformerait un vrai bug survenu pendant la traduction en
message rassurant, exactement le mode de défaillance que ce dépôt traque.

Required API keys (set one based on which API you use). Use `.env` file or export:

- `OPENAI_API_KEY`
- `MISTRAL_API_KEY`
- `ANTHROPIC_API_KEY`
- `GOOGLE_API_KEY` (for Gemini)
- `XAI_API_KEY` (for Grok via the xAI API)
- `GEMINI_API_KEY` accepted as an alternative to `GOOGLE_API_KEY`
- `OPENROUTER_API_KEY` (for OpenRouter, `--use_openrouter`)

Optional: `XAI_BASE_URL`, `CLAUDE_TIMEOUT` (default 900s), `CODEX_BIN`,
`CODEX_TIMEOUT`, `GROK_BIN`, `GROK_HOME`, `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (défaut 900 s par segment,
démarrage compris), `OPENCODE_BIN`, `OPENCODE_TIMEOUT` (défaut 600 s),
`OPENROUTER_BASE_URL` (https exigé), `OPENROUTER_TIMEOUT` (défaut 900 s),
`OPENROUTER_PREFLIGHT_TIMEOUT` (défaut 30 s),
`REGEN_PROVIDER`, `REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (dérogation, cf. `docs/traductions.md`),
`REGEN_JOB_TIMEOUT` (plafond par job du regen : 600 s, 1 800 s sur Codex, Antigravity et Claude Code),
`AIPMT_CLAUDE_BIN`, `AIPMT_CLAUDE_TIMEOUT` (défaut 900 s), `AIPMT_CLAUDE_MAX_UTILIZATION`
(défaut 0,8), `CLAUDE_CONFIG_DIR` (compte de Claude Code, filtré de la couche projet),
`XDG_CACHE_HOME` (répertoires de travail de Claude Code),
`XDG_CONFIG_HOME` et `APPDATA` (emplacement de la configuration utilisateur).
