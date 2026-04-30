# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Claude Code Workflow

- **Commits**: Utiliser le skill `/helping-with-commits` pour tous les commits
- **Recherche web**: Utiliser l'agent `web-research-specialist:web-research-specialist` pour les recherches de documentation (évite de polluer le contexte principal)

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

| Provider | Quality (default) | Economic (`--eco`) |
|----------|-------------------|-------------------|
| OpenAI | `gpt-5.5` | `gpt-5.4-mini` |
| Claude | `claude-sonnet-4-6` | `claude-haiku-4-5-20251001` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3.1-pro-preview` | `gemini-3-flash-preview` |

> **Recommendation for long-form translations** : `--use_gemini` (default = `gemini-3.1-pro-preview` quality, `--eco` = `gemini-3-flash-preview`) tends to produce more reliable structure preservation on non-Latin scripts (PL, JA, ZH, AR, HI), particularly for `--news` mode where placeholder fidelity matters. OpenAI remains the default for backward compatibility.
