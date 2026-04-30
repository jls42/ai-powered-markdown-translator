# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Claude Code Workflow

- **Commits**: Utiliser le skill `/helping-with-commits` pour tous les commits
- **Recherche web**: Utiliser l'agent `web-research-specialist:web-research-specialist` pour les recherches de documentation (évite de polluer le contexte principal)

## Quality / pre-commit (workflow)

Le projet utilise le framework [`pre-commit`](https://pre-commit.com) avec un setup "type EurekAI complet" (cf. `.pre-commit-config.yaml`). Tous les hooks tournent localement avant chaque commit (rapides) ou avant chaque push (lourds, réseau).

### Bootstrap (une fois après clone)

```bash
source venv/bin/activate
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks pre-commit (rapides)
pre-commit install --hook-type pre-push  # hooks pre-push (mypy, SAST, audit, tests)
```

Le premier `pre-commit run --all-files` télécharge les environnements des hooks (~1-2 min, en cache après).

### Hooks actifs

| Stage      | Hook                           | Rôle                                                                            |
| ---------- | ------------------------------ | ------------------------------------------------------------------------------- |
| pre-commit | shellcheck                     | Lint des `.sh` (release.sh, regen_translations.sh, scripts/)                    |
| pre-commit | ruff + ruff-format             | Lint + format Python (rapide, --fix automatique)                                |
| pre-commit | prettier                       | Format JSON/YAML/MD (28 traductions exclues)                                    |
| pre-commit | pre-commit-hooks v5            | Trailing-whitespace, EOF, check-yaml/toml, large-files, merge-conflict, shebang |
| pre-commit | detect-secrets                 | Détection de fuites d'API keys (4 providers utilisés)                           |
| pre-commit | check-complexity (Lizard)      | CCN <= 12, scope `scripts/` (translate.py exclu, refactor TODO)                 |
| pre-push   | mypy (lax)                     | Type-checking des fonctions déjà annotées (durcissement progressif)             |
| pre-push   | check-security-sast (Opengrep) | SAST sur translate.py + scripts/ (graceful skip si binaire absent)              |
| pre-push   | check-pip-audit                | Audit deps (mode reporting initial, durcir après bump)                          |
| pre-push   | unittest                       | Tests `tests/` + `scripts/tests/`                                               |

### Lancer manuellement

```bash
pre-commit run --all-files                         # tous les hooks pre-commit
pre-commit run --hook-stage pre-push --all-files   # tous les hooks pre-push
pre-commit run ruff --all-files                    # un hook précis
```

### Échappatoires (à utiliser sciemment)

```bash
git commit --no-verify   # skip les hooks pre-commit
git push --no-verify     # skip les hooks pre-push
```

### Stratégie mypy progressive

mypy est en mode **Lax** au démarrage (`disallow_untyped_defs = false`, `check_untyped_defs = false`). Concrètement, mypy ne vérifie que les fonctions déjà annotées avec des types ; les autres sont ignorées silencieusement.

Trajectoire :

1. **Phase 1 (actuel)** : mypy lax, 0 effort initial. Filet de sécurité quand on ajoute des annotations.
2. **Phase 2** : annoter les fonctions critiques de `translate.py` (`segment_text`, `translate`, `translate_markdown_file`). Bumper `check_untyped_defs = true`.
3. **Phase 3** : `disallow_untyped_defs = true` (mypy strict). Tout le code annoté.

### Lizard CCN — refactor planifié de translate.py

Le seuil est 12 (futur 8). 4 fonctions de `translate.py` dépassent : `translate` (CCN 25), `translate_markdown_file` (CCN 47), `translate_directory` (CCN 21), `main` (CCN 32). Le fichier est temporairement exclu de Lizard via `-x "translate.py"` dans `scripts/check-complexity.sh`. Le refactor est un travail dédié à mener dans une PR séparée ; le gate s'applique strictement aux nouveaux scripts pour empêcher la régression.

### Gestion du baseline detect-secrets

```bash
# Régénérer le baseline (après ajout de nouveaux fichiers, par exemple)
git ls-files --cached -z | xargs -0 detect-secrets scan \
  --exclude-files '(README|CHANGELOG)-[a-z]{2}\.md' \
  --exclude-files 'traductions_.*' \
  --exclude-files 'tests/fixtures/.*' \
  --exclude-files 'venv/.*' \
  --exclude-files '\.secrets\.baseline' \
  > .secrets.baseline

# Auditer manuellement les findings (interactif)
detect-secrets audit .secrets.baseline
```

Findings actuels (tous faux positifs attendus) : 4 placeholders `votre-cle-api-*-par-defaut` dans translate.py (OpenAI/Anthropic/Mistral/Google), 1 exemple dans README.md, 1 fixture dans tests/test_silent_failure.py. À auditer ponctuellement pour passer `is_secret: false`.

### Pré-requis lors du clone sur une autre machine

Les wrappers locaux (`scripts/run-*.sh`, `scripts/check-*.sh`) requièrent `./venv/bin/python`. Si le venv n'existe pas, ils renvoient un message explicite avec les commandes d'install. Sur CI ou autre poste de dev :

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

### Release / Tag workflow (2 phases)

Le script `release.sh` est conçu pour un workflow en **deux phases** : avant merge (prépare la MR sans tagger) et après merge (tag sur main + GitLab Release).

Quand l'utilisateur demande "release", "tag", "publie cette version" :

#### Phase 1 — Avant merge (depuis la branche feature)

```bash
./release.sh --auto
```

Effectue : pré-checks → tests `unittest` → régénération des 28 traductions (`--force`) → validation 28/28 → commit ciblé (jamais `git add -A`, `.gitignore` couvre `__pycache__/`, `venv/`, `.env`) → push branche → MR via `glab` (si auth OK).

**Pas de tag à ce stade.** Le tag est créé en phase 2 pour qu'il pointe sur le commit de merge dans `main` (pas sur la branche feature).

#### Phase 2 — Après merge MR

```bash
./release.sh --tag-only --yes
```

Effectue : checkout main → pull → vérifie cohérence CHANGELOG → tag annoté `v$VERSION` sur HEAD de main → push tag → GitLab Release via `glab` (si auth OK).

#### Variantes

- `--with-tag` : tag avant merge (workflow fast-forward / squash uniquement). À éviter si la MR génère un merge commit.
- `--local-only` : tout en local, pas de push (test/preview).
- `--dry-run` : simule sans rien toucher.
- `--no-mr` / `--no-gitlab-release` / `--no-push` : opt-out fins.

#### Gestion glab token

Le script vérifie l'auth glab en parsant la sortie de `glab api user` (le simple exit code de `glab auth status` n'est pas fiable : il retourne 0 même sur 401). Si le token est expiré :

- Warn + skip MR / GitLab Release
- Affiche les commandes manuelles
- Pour réauthentifier : `glab auth login`

#### Régénération seule (sans release)

```bash
./regen_translations.sh --force   # réécrit les 28 traductions
./regen_translations.sh           # skip celles qui existent déjà
```

## Project Overview

AI-powered Markdown translator that uses OpenAI, Mistral AI, Claude (Anthropic), and Google Gemini APIs to translate Markdown files while preserving formatting, code blocks, and front matter metadata.

## Commands

### Run a translation

```bash
# Activate virtual environment first
source venv/bin/activate

# Translate a single file
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'

# Translate a directory with OpenAI (default: gpt-5.5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Use economic models (--eco): gpt-5.4-mini, claude-haiku, gemini-flash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'

# Translate with Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Translate with Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Translate with Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Force retranslation of existing files
python translate.py --force --source_dir 'content/fr' --target_dir 'content/en'

# Add translation note at end of document
python translate.py --add_translation_note --source_dir 'content/fr' --target_dir 'content/en'

# News mode: protect EN quotes, manage flags per language
python translate.py --news --file 'article.md' --target_dir 'output/' --target_lang 'es'
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Architecture

**Single-file script**: `translate.py` contains all logic:

- **API clients**: OpenAI, Mistral, Claude (Anthropic), and Gemini are initialized based on CLI flags
- **Text segmentation**: `segment_text()` splits long documents at natural breakpoints (sentences, paragraphs, headers) respecting model token limits defined in `MODEL_TOKEN_LIMITS`
- **Code preservation**: Regex extracts fenced code blocks AND inline code (`` `...` ``) before translation, replaces with placeholders, restores after
- **News mode**: `--news` protects English quotes with `#NEWSQUOTE{n}#` placeholders, validates placeholder integrity before restoration, manages flag emojis per target language
- **Directory traversal**: `translate_directory()` walks source directory, skips patterns in `EXCLUDE_PATTERNS`, checks for existing translations

**Output naming**:

- Default: `{base}-{target_lang}.md` (e.g., `README-en.md`)
- With `--include_model`: `{base}-{target_lang}-{model}.md`
- With `--keep_filename`: original filename (for destination folder workflows)

## Environment Variables

Required API keys (set one based on which API you use). Use `.env` file or export:

- `OPENAI_API_KEY`
- `MISTRAL_API_KEY`
- `ANTHROPIC_API_KEY`
- `GOOGLE_API_KEY` (for Gemini)

## Recommended Usage

For batch translations (README, CHANGELOG, blog articles), use `--eco` mode:

```bash
python translate.py --file README.md --target_dir . --source_lang fr --target_lang en --eco --add_translation_note
```

This uses faster/cheaper models (gpt-5.4-mini) which are sufficient for documentation translation.

## Key Constants

- `EXCLUDE_PATTERNS`: Paths containing these strings are skipped (`traductions_`, `venv`, `PRIVACY.md`)
- `MODEL_TOKEN_LIMITS`: Dict mapping model names to max token limits for segmentation

### Default Models (2026)

| Provider | Quality (default)        | Economic (`--eco`)          |
| -------- | ------------------------ | --------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`              |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001` |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`      |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3-flash-preview`    |

> **Recommendation for long-form translations** : `--use_gemini` (default = `gemini-3.1-pro-preview` quality, `--eco` = `gemini-3-flash-preview`) tends to produce more reliable structure preservation on non-Latin scripts (PL, JA, ZH, AR, HI), particularly for `--news` mode where placeholder fidelity matters. OpenAI remains the default for backward compatibility.
