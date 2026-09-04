# AI-Powered Markdown Translator

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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

Markdown file translator using **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini**, and **Grok (xAI)** — via API, using the quota of a ChatGPT (Codex) or Grok subscription without pay-per-use billing, or through **OpenCode**, the open-source agent, to the provider of your choice: local model (Ollama), free, subscription (GitHub Copilot…), or key.

This Python script translates Markdown files from a source language into a target language while preserving formatting, code blocks, and front matter metadata.

## Main Features

- **Multi-Provider**: 5 APIs (OpenAI, Mistral, Claude, Gemini, Grok) + 2 subscription CLIs, without pay-per-use billing — Codex (ChatGPT) and Grok — + OpenCode (open source, MIT) to any provider configured in OpenCode, including a local model
- **2026 Models**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Economy Mode**: Option `--eco` to use faster and less expensive models
- **Single File**: Option `--file` to translate a single file
- **Smart Segmentation**: Handling long texts with per-model token limits
- **Code Preservation**: Code blocks AND inline code (`` `...` ``) are preserved
- **File Name**: Option `--keep_filename` to keep the original name
- **News Mode**: Option `--news` to protect English quotations and handle flags in news articles
- **.env Configuration**: Support for the `.env` file for API keys
- **Translation Note**: Optional addition of a note at the end of the document

## Installation

### To use the tool

```bash
pip install ai-powered-markdown-translator
```

The `aipmt` command is then available everywhere. If the Python scripts directory
is not in your `PATH`, `python -m aipmt` does exactly the same
thing. Python 3.10 or newer.

For an installation isolated from the rest of your packages:

```bash
pipx install ai-powered-markdown-translator
```

### To contribute to the project

The cloned repository remains necessary for development: this is where the tests,
the 28 translations, and all quality tooling live.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` is a **fully pinned lockfile**, an exact reflection of the
tested environment. The bounds published in `pyproject.toml` are
deliberately broader: they impose nothing on your other packages.

### Quality tooling (optional but recommended)

The project uses [`pre-commit`](https://pre-commit.com) to prevent committing poorly formatted, vulnerable, or secret-containing code. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Active hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexity), detect-secrets (API keys), mypy (progressive typing), Opengrep (SAST), pip-audit (CVE deps), unittest. See the `CLAUDE.md` _Quality / pre-commit_ section for details.

## Configuration

Keys are searched for in **three locations**, from highest to lowest priority.
Each one only fills in what the previous one leaves empty.

|     | Where                                            | For what                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Environment variables                     | CI, containers, one-off override |
| 2   | `.env` in the current directory (or a parent) | a key specific to a project            |
| 3   | `~/.config/aipmt/.env`                        | **installed once, works everywhere**   |

The simplest option after a `pip install` is the third:

```bash
mkdir -p ~/.config/aipmt
cat > ~/.config/aipmt/.env <<'EOF'
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
EOF
chmod 600 ~/.config/aipmt/.env
```

This file follows `XDG_CONFIG_HOME` when the variable designates an absolute path
(otherwise it is ignored, as prescribed by the specification), and `%APPDATA%`
on Windows.

The second remains useful when a repository has its own key: an `.env` at its root
then takes precedence over the user configuration, without modifying it. And a variable
already defined in the environment takes precedence over both:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

If no key is found, the command displays no call trace: it
lists the three locations with their exact paths.

`GEMINI_API_KEY` is accepted as an alternative to `GOOGLE_API_KEY` (AI
Studio convention). Optional variables: `XAI_BASE_URL` (xAI endpoint, default
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (seconds per Anthropic call, default
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (see the Grok CLI section), and `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (see the OpenCode section). For
`regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL`, and
`REGEN_JOB_TIMEOUT` (per-job limit, default 600 s).

## Usage

### Translate a single file

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Translate a directory

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
aipmt --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
aipmt --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
aipmt --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
aipmt --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
aipmt --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
aipmt --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
aipmt --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### Translate using a ChatGPT subscription (`--use_codex`)

This provider does not use any API key: it drives the official Codex CLI in
non-interactive mode, so the translation is deducted from the already-paid
ChatGPT subscription quota (Plus, Pro, Business…). This is the only route documented by
OpenAI for this use — `~/.codex/auth.json` tokens do not authenticate
calls to the Platform API, and are never read by this script anyway.

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

**Things to know:**

- **No API key is used.** `OPENAI_API_KEY` and `CODEX_API_KEY` are
  removed from the subprocess environment, ensuring that a key present in
  `.env` can never switch the translation to pay-per-use billing.
- **One segment = one “local message”** in the plan’s 5-hour window.
  Use `--eco` (model `gpt-5.6-luna`, 250–2,000 messages/5 h on Plus)
  rather than the quality model (`gpt-5.6-sol`, 10–100 messages/5 h).
- **Slower** than an API call: allow ~45 s for a complete README, compared with
  a few seconds directly.
- **Refused in CI** (`CI` or `GITHUB_ACTIONS` defined): subscription authentication
  is not intended for a shared runner, and OpenAI discourages this workflow on public
  repositories. Use an API key on this path.
- Environment variables: `CODEX_BIN` (explicit binary path) and
  `CODEX_TIMEOUT` (seconds per segment, default `600`).

### Translate using a Grok subscription (`--use_grok_cli`)

Same principle as `--use_codex`, with the official **Grok Build** CLI: the
translation is deducted from the Grok subscription (SuperGrok / X Premium+) instead
of being billed per token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Sandboxing — read before use.** This provider is structurally **weaker
than `--use_codex`, and this is intentional:

- Codex runs in `--sandbox read-only`, a boundary imposed by the system.
- Grok’s sandbox **cannot be applied** on many recent Linux systems: AppArmor blocks
  unprivileged user namespaces since Ubuntu 24.04, and the container runtime socket
  deny-list fails if `/run/podman` is `0700`. Yet an **integrated** profile
  that cannot be applied starts **unconfined, silently**.
- The script therefore requests no profile by default, and **never silently falls back**:
  it displays a warning. Sandboxing relies on the CLI’s `--deny` rules
  (including the `*` catch-all), the only _fail-closed_ layer measured
  — an unknown rule causes startup to be refused rather than removing protection
  without saying so.
- To **require** the OS sandbox: `GROK_TRANSLATE_SANDBOX=read-only`. Startup
  will fail if the machine cannot honor it, which is the intended
  behavior.

**Quota**: the Grok pool is **weekly and shared** with Chat, Imagine, and
Voice, and no command allows it to be read. A batch process can therefore consume
your conversational usage without anything indicating it — hence a concurrency limit
of 2 and a warning in `regen_translations.sh`.

Other variables: `GROK_BIN` (binary path), `GROK_TIMEOUT` (default 900 s).

To regenerate the 28 translations:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### Translate with OpenCode, to the provider of your choice (`--use_opencode`)

[OpenCode](https://opencode.ai) is an **open-source (MIT)** code agent in
the terminal. It is not a model provider but a **router** to those
you have configured in OpenCode itself: an API key, a subscription
(GitHub Copilot, ChatGPT, SuperGrok), the OpenCode Zen gateway — which serves free
models **without an account** — or a **local** model (Ollama, LM Studio,
llama.cpp). This provider drives `opencode run` in non-interactive mode and confines
the call to a single round trip, without any tool.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` is **mandatory**, in the `provider/modèle` format. OpenCode is not
a provider, and no default is chosen for you: its own fallback would be a free model
whose exchanges may be used for training.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Sandboxing — what the script does on every call:**

- An inline configuration (`OPENCODE_CONFIG_CONTENT`), taking priority over
  yours, defines an `aipmt` agent whose **all tools are denied**
  (`permission: { "*": "deny" }`): the model can neither read, write, nor
  run commands — measured, it does not even attempt to. Session sharing
  is disabled, `--pure` excludes external plugins, never `--auto`.
- The call runs in an **empty disposable directory**, with the `OPENCODE_DISABLE_PROJECT_CONFIG`
  and `OPENCODE_DISABLE_CLAUDE_CODE` switches: without
  them, OpenCode injects the current directory’s `AGENTS.md` into every prompt
  and your `~/.claude/CLAUDE.md` — measured, an instruction to “end every response
  with BANANA” placed in a `AGENTS.md` was applied to the translation. Global
  `~/.config/opencode/AGENTS.md` rules remain
  applied, however: OpenCode does not allow them to be excluded.
- The output contract requires all of the following: exit code 0, no
  `error` event, no tool call, a final step completed in `stop`, non-empty
  text, and the agent actually loaded — an unknown `--agent` does not cause
  OpenCode to fail; it **silently falls back** to the coding agent, with tools
  active. An `exit 0` does not prove anything here either.
- **No aipmt key is passed** to the subprocess (the same filtering as with Codex
  and Grok), with one named exception: `OPENCODE_API_KEY`, the OpenCode key itself
  (Zen, Go). Providers are configured in
  OpenCode (`opencode auth login`, `opencode.json`), not in aipmt’s
  `.env`.

**Things to know:**

- **Zen’s free models are “stealth” or contributor models**,
  changing, with undocumented limits, and their exchanges may be used for
  training: perfect for public documentation, best avoided for private content. Measured:
  `opencode/mimo-v2.5-free` translates this README in one
  pass; `opencode/big-pickle` is slower, and two simultaneous requests there
  remained unanswered.
- **A local model must provide at least 16k of context** — segments are up to
  16,000 characters — whereas Ollama often configures 4,096 by default. With Ollama:
  a `Modelfile` with `PARAMETER num_ctx 32768`, then
  `ollama create`. Quality depends on the model: a 7B model reversed a list and
  damaged a code block closing fence on a test file where a gateway model preserved
  everything.
- `--eco` has no effect (the model is the one from `--model`);
  `--reasoning_effort` is passed as-is as OpenCode’s `--variant`, and should only
  be requested if the model knows it.
- Sessions are logged by OpenCode in its database
  (`~/.local/share/opencode/`), like every OpenCode session.
- Environment variables: `OPENCODE_BIN` (explicit binary path,
  otherwise `PATH` then `~/.opencode/bin/opencode`) and `OPENCODE_TIMEOUT`
  (seconds per segment, default `600`). `OPENCODE_CONFIG` is honored if you
  export it.

### Economy mode

Uses faster and less expensive models (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### Options

| Option                   | Description                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Single Markdown file to translate                                                                            |
| `--source_dir`           | Source directory containing Markdown files                                                             |
| `--target_dir`           | Output directory for translated files                                                               |
| `--source_lang`          | Source language (default: `fr`)                                                                                  |
| `--target_lang`          | Target language (default: `en`)                                                                                   |
| `--model`                | Specific model to use                                                                                  |
| `--eco`                  | Use economical models                                                                              |
| `--use_mistral`          | Use the Mistral AI API                                                                                     |
| `--use_claude`           | Use the Claude API                                                                                         |
| `--use_gemini`           | Use the Gemini API                                                                                         |
| `--use_codex`            | Use the Codex CLI with the ChatGPT subscription quota                                                    |
| `--use_grok`             | Use the xAI (Grok) API — requires `XAI_API_KEY`                                                           |
| `--use_grok_cli`         | Use the Grok CLI with the Grok subscription quota                                                        |
| `--use_opencode`         | Use OpenCode (open source) with the provider configured in OpenCode; requires `--model provider/modèle` |
| `--force`                | Force retranslation                                                                                       |
| `--keep_filename`        | Preserve the original filename                                                                          |
| `--news`                 | News mode: protects EN quotations and handles language flags                                      |
| `--add_translation_note` | Add a translation note                                                                                |
| `--note_position`        | Note position: `top`, `bottom` (default), or `both`                                                     |
| `--note_format`          | Note format: `legacy` (default, bold paragraph) or `marker`                                            |
| `--include_model`        | Include the model name in the output file                                                            |
| `--reasoning_effort`     | GPT-5.x reasoning effort: `none`/`low`/`medium`/`high`/`xhigh`                                         |

> **The seven provider flags are mutually exclusive.** Combining two of them
> was previously silently accepted and resolved to the first one tested: a
> translation requested using subscription quota (`--use_codex`, `--use_grok_cli`)
> could therefore be billed at usage rates without any warning.
> `argparse` now rejects the combination.

### Translation note: positions and formats

With `--add_translation_note`, the translator can place the note at the top, bottom, or both locations, and render it either as plain text (backward-compatible) or as `marker` format consumable by a Markdown plugin.

**Position** (`--note_position`):

- `bottom` (default): note at the end of the file, as historically.
- `top`: note inserted **after the YAML frontmatter** (Astro Content Collections, gray-matter, etc. safety).
- `both`: note inserted at the top AND bottom (a single LLM call, with content reused for both placements).

**Format** (`--note_format`):

- `legacy` (default): bold paragraph `**...**` — behavior strictly identical to v1.8, byte-for-byte. Compatible with Hugo, GitHub, GitLab, and any Markdown renderer.
- `marker`: invisible Markdown link reference definition (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) followed by a bold blockquote. Natively readable on GitHub/GitLab, and usable at build time by an Astro-side remark plugin to produce a stylized banner (see the jls42.org blog).

```bash
# Compatibilité legacy (rien ne change vs v1.8)
aipmt --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### Default models (2026)

| Provider | Quality (default)                      | Economical (`--eco`)      |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI   | `gpt-5.6-terra`                       | `gpt-5.6-luna`            |
| Claude   | `claude-sonnet-5`                     | `claude-haiku-4-5`        |
| Mistral  | `mistral-large-latest`                | `mistral-small-latest`    |
| Gemini  | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite`   |
| Codex    | `gpt-5.6-sol`                         | `gpt-5.6-luna`            |
| Grok API | `grok-4.6`                            | `grok-4.3`                |
| Grok CLI | `grok-4.6`                            | `grok-4.5`                |
| OpenCode | `--model provider/modèle` required | same — `--eco` has no effect |

> **Long-form translation recommendation**: `--use_gemini` (default = `gemini-3.7-flash`) faithfully preserves Markdown structure for non-Latin scripts (PL, JA, ZH, AR, HI), including in `--news` mode where placeholder fidelity matters. Measured on this README translated into Japanese: structure identical to `gemini-3.1-pro-preview` (21 lists, 18 code blocks, 13 HTML links, 13 images, all URLs preserved) with ~6x less latency. OpenAI remains the default for backward compatibility.

## Projects using this script

- **[jls42.org](https://jls42.org)** - Multilingual personal blog (15 languages)

## Author

Julien LE SAUX
Email: contact@jls42.org

## License

GNU GENERAL PUBLIC LICENSE Version 3. See [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Article translated from French to English with gpt-5.6-luna.**
