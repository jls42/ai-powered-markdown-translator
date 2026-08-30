# Traducteur de Markdown AI-Powered

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

<h4 align="center">📊 Qualité du code</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Quality Gate Status"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Security Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Reliability Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Maintainability Rating"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Coverage"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilities"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Duplicated Lines (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technical Debt"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Lines of Code"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy Badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Traducteur de fichiers Markdown utilisant **OpenAI**, **Mistral AI**, **Claude (Anthropic)** et **Google Gemini**.

Ce script Python traduit des fichiers Markdown d'une langue source vers une langue cible tout en préservant le formatage, les blocs de code et les métadonnées front matter.

## Caractéristiques Principales

- **Multi-Provider**: Support de 4 APIs (OpenAI, Mistral, Claude, Gemini) + le CLI Codex sur abonnement ChatGPT
- **Modèles 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Mode Économique**: Option `--eco` pour utiliser des modèles plus rapides et moins coûteux
- **Fichier Unique**: Option `--file` pour traduire un seul fichier
- **Segmentation Intelligente**: Gestion des textes longs avec limites de tokens par modèle
- **Préservation du Code**: Les blocs de code ET le code inline (`` `...` ``) sont préservés
- **Nom de Fichier**: Option `--keep_filename` pour conserver le nom original
- **Mode News**: Option `--news` pour protéger les citations anglaises et gérer les drapeaux dans les articles d'actualité
- **Configuration .env**: Support du fichier `.env` pour les clés API
- **Note de Traduction**: Ajout optionnel d'une note en fin de document

## Installation

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Outillage qualité (optionnel mais recommandé)

Le projet utilise [`pre-commit`](https://pre-commit.com) pour empêcher de committer du code mal formaté, vulnérable ou contenant un secret. Installation :

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hooks actifs : ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexité), detect-secrets (clés API), mypy (typage progressif), Opengrep (SAST), pip-audit (CVE deps), unittest. Voir `CLAUDE.md` section _Quality / pre-commit_ pour les détails.

## Configuration

Créez un fichier `.env` à la racine du projet ou définissez les variables d'environnement :

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

`GEMINI_API_KEY` est accepté comme alternative à `GOOGLE_API_KEY` (convention AI
Studio). Variables optionnelles : `XAI_BASE_URL` (endpoint xAI, défaut
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (secondes par appel Anthropic, défaut
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
et `GROK_TRANSLATE_SANDBOX` (voir la section Grok CLI).

## Utilisation

### Traduire un fichier unique

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traduire un répertoire

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
python translate.py --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
python translate.py --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
python translate.py --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### Traduire sur son abonnement ChatGPT (`--use_codex`)

Ce provider ne consomme aucune clé API : il pilote le CLI Codex officiel en mode
non-interactif, donc la traduction est décomptée du quota de l'abonnement
ChatGPT (Plus, Pro, Business…) déjà payé. C'est la seule voie documentée par
OpenAI pour cet usage — les tokens de `~/.codex/auth.json` n'authentifient pas
les appels à l'API Platform, et ne sont d'ailleurs jamais lus par ce script.

**Prérequis :**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

Le binaire est cherché dans cet ordre : la variable `CODEX_BIN`, le `PATH`,
puis le package Python `openai-codex-cli-bin`. Ce dernier n'est volontairement
pas dans `requirements.txt` : il pèse ~250 Mo, ce qui serait imposé à tous les
utilisateurs pour un provider optionnel.

**À savoir :**

- **Aucune clé API n'est utilisée.** `OPENAI_API_KEY` et `CODEX_API_KEY` sont
  retirées de l'environnement du sous-processus, ce qui garantit qu'une clé
  présente dans `.env` ne fera jamais basculer la traduction en facturation à
  l'usage.
- **Un segment = un « message local »** de la fenêtre de 5 heures du plan.
  Utiliser `--eco` (modèle `gpt-5.6-luna`, 250-2 000 messages/5 h sur Plus)
  plutôt que le modèle qualité (`gpt-5.6-sol`, 10-100 messages/5 h).
- **Plus lent** qu'un appel API : compter ~45 s pour un README complet, contre
  quelques secondes en direct.
- **Refusé en CI** (`CI` ou `GITHUB_ACTIONS` défini) : l'authentification par
  abonnement n'est pas prévue pour un runner partagé, et OpenAI déconseille ce
  workflow sur les dépôts publics. Utiliser une clé API sur ce chemin.
- Variables d'environnement : `CODEX_BIN` (chemin explicite du binaire) et
  `CODEX_TIMEOUT` (secondes par segment, défaut `600`).

### Traduire sur son abonnement Grok (`--use_grok_cli`)

Même principe que `--use_codex`, avec le CLI officiel **Grok Build** : la
traduction est décomptée de l'abonnement Grok (SuperGrok / X Premium+) au lieu
d'être facturée au token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Confinement — à lire avant usage.** Ce provider est structurellement **plus
faible** que `--use_codex`, et c'est assumé :

- Codex tourne en `--sandbox read-only`, une frontière imposée par le système.
- Le sandbox de Grok **ne peut pas s'appliquer** sur beaucoup de postes Linux
  récents : AppArmor bloque les user namespaces non privilégiés depuis Ubuntu
  24.04, et la deny-list des sockets de runtime conteneur échoue si
  `/run/podman` est en `0700`. Or un profil **intégré** qui ne peut pas
  s'appliquer démarre **non confiné, en silence**.
- Le script ne demande donc aucun profil par défaut, et **ne retombe jamais
  silencieusement** : il affiche un avertissement. Le confinement repose sur les
  règles `--deny` du CLI (dont le catch-all `*`), la seule couche mesurée
  _fail-closed_ — une règle inconnue fait refuser le démarrage plutôt que de
  retirer la protection sans le dire.
- Pour **exiger** le sandbox OS : `GROK_TRANSLATE_SANDBOX=read-only`. Le
  démarrage échouera si la machine ne peut pas l'honorer, ce qui est le
  comportement voulu.

**Quota** : le pool Grok est **hebdomadaire et partagé** avec Chat, Imagine et
Voice, et aucune commande ne permet de le lire. Un traitement par lot peut donc
entamer ton usage conversationnel sans que rien ne le signale — d'où une
concurrence limitée à 2 et un avertissement dans `regen_translations.sh`.

Autres variables : `GROK_BIN` (chemin du binaire), `GROK_TIMEOUT` (défaut 900 s).

Pour la régénération des 28 traductions :

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### Mode économique

Utilise des modèles plus rapides et moins coûteux (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Options

| Option                   | Description                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Fichier Markdown unique à traduire                                       |
| `--source_dir`           | Répertoire source contenant les fichiers Markdown                        |
| `--target_dir`           | Répertoire de sortie pour les fichiers traduits                          |
| `--source_lang`          | Langue source (défaut: `fr`)                                             |
| `--target_lang`          | Langue cible (défaut: `en`)                                              |
| `--model`                | Modèle spécifique à utiliser                                             |
| `--eco`                  | Utiliser les modèles économiques                                         |
| `--use_mistral`          | Utiliser l'API Mistral AI                                                |
| `--use_claude`           | Utiliser l'API Claude                                                    |
| `--use_gemini`           | Utiliser l'API Gemini                                                    |
| `--use_codex`            | Utiliser le CLI Codex sur le quota de l'abonnement ChatGPT               |
| `--use_grok`             | Utiliser l'API xAI (Grok) — nécessite `XAI_API_KEY`                      |
| `--use_grok_cli`         | Utiliser le CLI Grok sur le quota de l'abonnement Grok                   |
| `--force`                | Forcer la re-traduction                                                  |
| `--keep_filename`        | Conserver le nom de fichier original                                     |
| `--news`                 | Mode actualités : protège les citations EN, gère les drapeaux par langue |
| `--add_translation_note` | Ajouter une note de traduction                                           |
| `--note_position`        | Position de la note : `top`, `bottom` (défaut), ou `both`                |
| `--note_format`          | Format de la note : `legacy` (défaut, paragraphe gras) ou `marker`       |
| `--include_model`        | Inclure le nom du modèle dans le fichier de sortie                       |
| `--reasoning_effort`     | Effort de raisonnement GPT-5.x : `none`/`low`/`medium`/`high`/`xhigh`    |

### Note de traduction : positions et formats

Avec `--add_translation_note`, le translator peut placer la note en haut, en bas, ou aux deux endroits, et la rendre soit en format texte simple (rétrocompatible) soit en format `marker` consommable par un plugin Markdown.

**Position** (`--note_position`) :

- `bottom` (défaut) : note en fin de fichier, comme historiquement.
- `top` : note insérée **après le frontmatter YAML** (sécurité Astro Content Collections, gray-matter, etc.).
- `both` : note insérée en haut ET en bas (un seul appel LLM, contenu réutilisé pour les deux placements).

**Format** (`--note_format`) :

- `legacy` (défaut) : paragraphe gras `**...**` — comportement strictement identique à v1.8, byte-for-byte. Compatible avec Hugo, GitHub, GitLab, et tout renderer Markdown.
- `marker` : link reference definition Markdown invisible (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) suivie d'un blockquote en gras. Lisible nativement sur GitHub/GitLab, et exploitable au build par un plugin remark côté Astro pour produire une bannière stylisée (cf. blog jls42.org).

```bash
# Compatibilité legacy (rien ne change vs v1.8)
python translate.py --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### Modèles par défaut (2026)

| Provider | Qualité (défaut)       | Économique (`--eco`)    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **Recommandation traductions long-form** : `--use_gemini` (défaut = `gemini-3.7-flash`) préserve fidèlement la structure markdown sur les scripts non-latins (PL, JA, ZH, AR, HI), y compris en mode `--news` où la fidélité des placeholders compte. Mesuré sur ce README traduit en japonais : structure identique à `gemini-3.1-pro-preview` (21 listes, 18 blocs de code, 13 liens HTML, 13 images, toutes les URLs préservées) pour ~6x moins de latence. OpenAI reste le défaut pour la rétrocompatibilité.

## Projets utilisant ce script

- **[jls42.org](https://jls42.org)** - Blog personnel multilingue (15 langues)

## Auteur

Julien LE SAUX
Email : contact@jls42.org

## Licence

GNU GENERAL PUBLIC LICENSE Version 3. Voir [LICENSE](LICENSE).
