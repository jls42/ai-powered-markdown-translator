# AI-Powered Markdown Translator

🌍 [French](README.md) | [English](README-en.md) | [Spanish](README-es.md) | [Chinese](README-zh.md) | [German](README-de.md) | [Japanese](README-ja.md) | [Korean](README-ko.md) | [Arabic](README-ar.md) | [Hindi](README-hi.md) | [Italian](README-it.md) | [Dutch](README-nl.md) | [Polish](README-pl.md) | [Portuguese](README-pt.md) | [Romanian](README-ro.md) | [Swedish](README-sv.md)

<h4 align="center">📊 Code Quality</h4>

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

Markdown file translator using **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, and **Google Gemini**.

This Python script translates Markdown files from a source language to a target language while preserving formatting, code blocks, and front matter metadata.

## Key Features

- **Multi-Provider**: Support for 4 APIs (OpenAI, Mistral, Claude, Gemini) + the Codex CLI with a ChatGPT subscription
- **2026 Models**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Economy Mode**: `--eco` option to use faster, less expensive models
- **Single File**: `--file` option to translate a single file
- **Smart Segmentation**: Handles long texts with per-model token limits
- **Code Preservation**: Code blocks AND inline code (`` `...` ``) are preserved
- **File Name**: `--keep_filename` option to keep the original name
- **News Mode**: `--news` option to protect English quotations and handle flags in news articles
- **.env Configuration**: Support for the `.env` file for API keys
- **Translation Note**: Optionally adds a note at the end of the document

## Installation

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Quality Tooling (optional but recommended)

The project uses [`pre-commit`](https://pre-commit.com) to prevent committing poorly formatted, vulnerable code or code containing a secret. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Active hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexity), detect-secrets (API keys), mypy (progressive typing), Opengrep (SAST), pip-audit (dependency CVEs), unittest. See the _Quality / pre-commit_ section in `CLAUDE.md` for details.

## Configuration

Create a `.env` file at the project root or define the environment variables:

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

`GEMINI_API_KEY` is accepted as an alternative to `GOOGLE_API_KEY` (AI
Studio convention). Optional variables: `XAI_BASE_URL` (xAI endpoint, default
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (seconds per Anthropic call, default
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
and `GROK_TRANSLATE_SANDBOX` (see the Grok CLI section).

## Usage

### Translate a Single File

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Translate a Directory

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

### Translate Using Your ChatGPT Subscription (`--use_codex`)

This provider does not use any API key: it runs the official Codex CLI in
non-interactive mode, so translation usage is deducted from the quota of the
already-paid ChatGPT subscription (Plus, Pro, Business…). This is the only method
documented by OpenAI for this use case—the tokens from `~/.codex/auth.json` do not
authenticate Platform API calls and, in fact, are never read by this script.

**Prerequisites:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

The binary is searched for in this order: the `CODEX_BIN` variable, the `PATH`,
then the `openai-codex-cli-bin` Python package. The latter is deliberately
not included in `requirements.txt`: it weighs ~250 MB, which would be imposed on all
users for an optional provider.

**Important:**

- **No API key is used.** `OPENAI_API_KEY` and `CODEX_API_KEY` are
  removed from the subprocess environment, ensuring that a key
  present in `.env` will never cause the translation to switch to
  usage-based billing.
- **One segment = one “local message”** in the plan's 5-hour window.
  Use `--eco` (model `gpt-5.6-luna`, 250–2,000 messages/5 h on Plus)
  rather than the quality model (`gpt-5.6-sol`, 10–100 messages/5 h).
- **Slower** than an API call: expect ~45 s for a complete README, compared with
  a few seconds directly.
- **Rejected in CI** (`CI` or `GITHUB_ACTIONS` defined): subscription-based
  authentication is not intended for a shared runner, and OpenAI advises against
  this workflow on public repositories. Use an API key for this path.
- Environment variables: `CODEX_BIN` (explicit binary path) and
  `CODEX_TIMEOUT` (seconds per segment, default `600`).

### Translate Using Your Grok Subscription (`--use_grok_cli`)

The same principle as `--use_codex`, using the official **Grok Build** CLI:
translation usage is deducted from the Grok subscription (SuperGrok / X Premium+)
instead of being billed per token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Confinement—read before use.** This provider is structurally **weaker**
than `--use_codex`, and this is intentional:

- Codex runs in `--sandbox read-only`, a boundary enforced by the system.
- The Grok sandbox **cannot be applied** on many recent Linux systems:
  AppArmor has blocked unprivileged user namespaces since Ubuntu
  24.04, and the container runtime socket deny-list fails if
  `/run/podman` is set to `0700`. However, a **built-in** profile that cannot
  be applied starts **unconfined, silently**.
- The script therefore requests no profile by default and **never falls back
  silently**: it displays a warning. Confinement relies on the CLI's
  `--deny` rules (including the `*` catch-all), the only layer measured
  as _fail-closed_—an unknown rule prevents startup rather than
  removing protection without notice.
- To **require** the OS sandbox: `GROK_TRANSLATE_SANDBOX=read-only`.
  Startup will fail if the machine cannot honor it, which is the
  intended behavior.

**Quota**: the Grok pool is **weekly and shared** with Chat, Imagine, and
Voice, and no command can display it. Batch processing can therefore
eat into your conversational usage without any notification—hence
concurrency limited to 2 and a warning in `regen_translations.sh`.

Other variables: `GROK_BIN` (binary path), `GROK_TIMEOUT` (default 900 s).

To regenerate the 28 translations:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### Economy Mode

Uses faster, less expensive models (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Options

| Option                   | Description                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Single Markdown file to translate                                        |
| `--source_dir`           | Source directory containing Markdown files                               |
| `--target_dir`           | Output directory for translated files                                    |
| `--source_lang`          | Source language (default: `fr`)                                 |
| `--target_lang`          | Target language (default: `en`)                                 |
| `--model`                | Specific model to use                                                    |
| `--eco`                  | Use economy models                                                       |
| `--use_mistral`          | Use the Mistral AI API                                                    |
| `--use_claude`           | Use the Claude API                                                        |
| `--use_gemini`           | Use the Gemini API                                                        |
| `--use_codex`            | Use the Codex CLI with the ChatGPT subscription quota                     |
| `--use_grok`             | Use the xAI API (Grok)—requires `XAI_API_KEY`                             |
| `--use_grok_cli`         | Use the Grok CLI with the Grok subscription quota                         |
| `--force`                | Force retranslation                                                      |
| `--keep_filename`        | Keep the original file name                                               |
| `--news`                 | News mode: protects EN quotations, handles flags by language              |
| `--add_translation_note` | Add a translation note                                                     |
| `--note_position`        | Note position: `top`, `bottom` (default), or `both` |
| `--note_format`          | Note format: `legacy` (default, bold paragraph) or `marker`    |
| `--include_model`        | Include the model name in the output file                                 |
| `--reasoning_effort`     | GPT-5.x reasoning effort: `none`/`low`/`medium`/`high`/`xhigh` |

### Translation Note: Positions and Formats

With `--add_translation_note`, the translator can place the note at the top, at the bottom, or in both locations, and render it either as plain text format (backward-compatible) or as `marker` format consumable by a Markdown plugin.

**Position** (`--note_position`):

- `bottom` (default): note at the end of the file, as before.
- `top`: note inserted **after the YAML front matter** (safe for Astro Content Collections, gray-matter, etc.).
- `both`: note inserted at the top AND bottom (a single LLM call, with content reused for both placements).

**Format** (`--note_format`):

- `legacy` (default): bold paragraph `**...**`—behavior strictly identical to v1.8, byte-for-byte. Compatible with Hugo, GitHub, GitLab, and any Markdown renderer.
- `marker`: invisible Markdown link reference definition (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) followed by a bold blockquote. Natively readable on GitHub/GitLab and usable at build time by an Astro-side remark plugin to produce a styled banner (see the jls42.org blog).

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

### Default Models (2026)

| Provider | Quality (default)      | Economy (`--eco`) |
| -------- | ---------------------- | ------------------------ |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`           |
| Claude   | `claude-sonnet-5`        | `claude-haiku-4-5`           |
| Mistral  | `mistral-large-latest`        | `mistral-small-latest`          |
| Gemini   | `gemini-3.7-flash`       | `gemini-3.1-flash-lite`          |
| Codex    | `gpt-5.6-sol`       | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`       | `grok-4.3`          |
| Grok CLI | `grok-4.6`       | `grok-4.5`          |

> **Recommendation for long-form translations**: `--use_gemini` (default = `gemini-3.7-flash`) faithfully preserves Markdown structure for non-Latin scripts (PL, JA, ZH, AR, HI), including in `--news` mode where placeholder fidelity matters. Measured on this README translated into Japanese: structure identical to `gemini-3.1-pro-preview` (21 lists, 18 code blocks, 13 HTML links, 13 images, all URLs preserved) with ~6x lower latency. OpenAI remains the default for backward compatibility.

## Projects Using This Script

- **[jls42.org](https://jls42.org)** - Multilingual personal blog (15 languages)

## Author

Julien LE SAUX
Email: contact@jls42.org

## License

GNU GENERAL PUBLIC LICENSE Version 3. See [LICENSE](LICENSE).

**Article translated from fr to en with gpt-5.6-sol.**
