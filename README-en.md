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

Translates Markdown files from one language to another while preserving their
structure: code blocks, inline code, URLs, anchors, tables, and front
matter. Nine ways to call a model—five APIs, two subscriptions with no
usage-based billing, and two routers—plus a published measurement of what each
model actually preserves.

## In Short

- **Nine provider paths**: OpenAI, Mistral, Claude, Gemini, and Grok APIs;
  ChatGPT (Codex) and Grok subscriptions with no usage-based billing; OpenCode
  routers (open source, free or local) and OpenRouter (more than 400 models).
- **No corrupted output because of a lost token**: code blocks, inline code,
  URLs, anchors, and references are replaced with tokens before the call and
  verified on return. If one is missing, the file is not written.
- **Long documents**: segmentation based on the model's context window.
- **`--news` mode**: protected English quotations and flags managed by
  language, for monitoring articles.
- **`--eco` mode**: faster and cheaper models.
- Optional **translation note**, at the top, bottom, or both.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 or newer. To install from the repository, see
[Contributing](#contributing).

## Configuration

Keys are read from three locations, from highest to lowest priority; each only
fills in values left empty by the preceding one.

|     | Where                                         | Purpose                              |
| --- | --------------------------------------------- | ------------------------------------ |
| 1   | Environment variables                         | CI, containers, one-off overrides    |
| 2   | `.env` in the current directory (or a parent) | a project-specific key               |
| 3   | `~/.config/aipmt/.env`                        | installed once, applies everywhere   |

```bash
mkdir -p ~/.config/aipmt
cat > ~/.config/aipmt/.env <<'EOF'
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
OPENROUTER_API_KEY=votre-clé-api-openrouter
EOF
chmod 600 ~/.config/aipmt/.env
```

`GEMINI_API_KEY` is accepted instead of `GOOGLE_API_KEY`. The user
file follows `XDG_CONFIG_HOME` (absolute path only) and `%APPDATA%`
on Windows. Without a key, the command lists all three locations.

**A project's `.env` cannot redirect calls.** It provides keys,
never a destination: all variables in `_BASE_URL`, `_API_BASE`, or
`_ENDPOINT`, proxies (`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`),
certificate stores (`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`,
`CURL_CA_BUNDLE`), and `XDG_CONFIG_HOME` / `APPDATA` are ignored there, with a
warning. A cloned repository must not be able to hijack your key. This
file is also read without interpolation: `NOM=${OPENAI_API_KEY}` does not copy
the key into it. Set these variables in the environment or in
`~/.config/aipmt/.env`.

Optional variables: `XAI_BASE_URL` (default `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (seconds per call, default 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(default 600), `GROK_BIN`, `GROK_HOME` (default `~/.grok`), `GROK_TIMEOUT`
(default 900), `GROK_TRANSLATE_SANDBOX`, `OPENCODE_BIN`, `OPENCODE_TIMEOUT`
(default 600), `OPENROUTER_BASE_URL` (`https://` required), `OPENROUTER_TIMEOUT`
(default 900), `OPENROUTER_PREFLIGHT_TIMEOUT` (default 30). Each is detailed
in its provider's section.

## Getting Started

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

Translating `document.md` into Spanish produces `document-es.md` in `--target_dir`;
with `--include_model`, `document-es-gpt-5.6-terra.md`. The extension always becomes
`.md`—`article.mdx` produces `article-en.md`—except with
`--keep_filename`, which preserves the original name. An existing translation
is skipped without `--force`.

Exit codes: `0` if everything succeeded or was skipped, `1` if any file
failed (listed on standard error), `2` if the configuration is at fault.
A failed file is never written, even if the write itself fails:
the content is written alongside it and then renamed. Simply run the command again.

## Which Model to Choose

Measured on two real documents, translated into the same fourteen languages by
each model. **The figure is the number of languages, out of fourteen, for which
the translation is written and nothing differs from the source.**

| Model                | How to access it                  | Dense monitoring article | This README  | What differs, and in how many languages                                                                                               |
| -------------------- | --------------------------------- | ------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | Google API key                    | ✅ 14/14                 | ⚠️ 13/14     | 1 language out of 14: one extra bold word (ja)                                                                                        |
| **GPT-5.6 Sol**      | ChatGPT subscription or OpenAI key | ✅ 14/14                | ⚠️ 12/14     | 2 languages out of 14: one fewer bold word (ar, ja)                                                                                   |
| **GLM-5.2**          | OpenRouter key                    | ✅ 14/14                 | ⚠️ 11/14     | 3 languages out of 14: one fewer bold word (hi, ja, ko)                                                                               |
| Claude Sonnet 5      | Anthropic API key                 | ⚠️ 11/14                 | ⚠️ 12/14     | 3 languages in the article: a code block appeared (es, de, hi); 2 in this README: a link without its markup (sv), a bold word (zh)     |
| Qwen 3.7 Flash       | OpenRouter key                    | ❌ 8/14                  | ⚠️ 10/14     | 1 language rejected for the article, 5 others differ; in this README, around forty words placed in `code` (ar)                 |
| Grok 4.6             | Grok subscription                 | ❌ 8/14                  | not rated    | 5 languages out of 14 rejected because inline code and URLs were not returned; Dutch differs throughout                              |
| GPT-OSS 20B          | local model (Ollama)              | ❌ 7/14                  | not remeasured | 4 languages out of 14 rejected: the model left French passages in them, and the safeguard stopped them                              |
| MiMo v2.5 (free)     | OpenCode Zen, no account required | ❌ 11/14                 | not remeasured | 1 language rejected; one section lost in Polish                                                                                     |
| Mistral Large        | Mistral API key                   | ❌ 5/14                  | ❌ 1/14      | **an entire section disappears**: 1 language in the article (hi), 3 in this README (ar, hi, ko)—plus 3 languages rejected for the article |
| DeepSeek V4 Flash    | OpenRouter key                    | ❌ 3/14                  | not remeasured | 10 languages out of 14 rejected; 37 minutes per language                                                                            |

|     | What the symbol means                                                                                                                                                                                  |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ✅  | all fourteen languages translated, with nothing differing from the source                                                                                                                              |
| ⚠️  | all fourteen languages translated; the differences are in **markup**—a bold word, an `code`, a link that loses its brackets. No text, URL, code block, or section is missing                    |
| ❌  | at least one language could not be translated—the file is rejected and not written—**or** content is missing from a written file                                                                       |

Key takeaways:

- **A rejected translation is not a damaged translation.** When a token is
  missing on return, the file is not written and the language counts as
  rejected. This is what happens to Grok on the article: four inline code
  elements and three URLs are lost in the very first segment, for all five
  non-Latin scripts.
- **This safety net does not cover headings, tables, front matter, or
  text.** A model that deletes a section returns a file that the tool writes
  without complaint—this is the case with Mistral. These elements cannot be
  replaced by a token, and the current safeguards do not check them;
  `scripts/compare_structure.py` detects a lost section, but only afterward.
- **Grok has no rating for this README**: its CLI session expired after twelve
  languages, eleven of which had no differences. An interrupted run is not rated.
- **Document density matters more than language.** Grok handles ordinary
  READMEs and falters on an article packed with links, including in
  Dutch.

Dates and documents: the “This README” column was measured on September 9, 2026,
using a frozen revision of this file (785 lines, 285 inline code elements, 89 table
lines), which has since been edited. The “Dense monitoring article” column comes from
the September 4 and 5 campaign on a 589-line article, except for the
Grok row, which was remeasured on September 9 using another edition of the same monitoring article. The
complete tables, timings, and protocol are in
[Detailed Measurements](#detailed-measurements).

## All Options

| Option                   | Description                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | Single Markdown file to translate (alternative to `--source_dir`)                                             |
| `--source_dir`           | Source directory containing Markdown files (default: `content/posts`)                                          |
| `--target_dir`           | Output directory for translated files (default: `traductions_en`)                                               |
| `--source_lang`           | Source language (default: `fr`)                                                                     |
| `--target_lang`           | Target language (default: `en`)                                                                     |
| `--model`           | Specific model to use                                                                                         |
| `--eco`           | Use economy models                                                                                            |
| `--use_mistral`           | Use the Mistral AI API                                                                                        |
| `--use_claude`           | Use the Claude API                                                                                            |
| `--use_gemini`           | Use the Gemini API                                                                                            |
| `--use_grok`           | Use the xAI API (Grok)—requires `XAI_API_KEY`                                                                |
| `--use_codex`           | Use the Codex CLI against the ChatGPT subscription quota                                                      |
| `--use_grok_cli`           | Use the Grok CLI against the Grok subscription quota                                                          |
| `--use_opencode`           | Use OpenCode (open source) with the provider configured in OpenCode; requires `--model provider/modèle`                  |
| `--use_openrouter`           | Use OpenRouter—requires `OPENROUTER_API_KEY` and `--model fournisseur/modèle`                                                     |
| `--force`           | Force retranslation                                                                                           |
| `--keep_filename`           | Preserve the original filename                                                                                |
| `--news`           | News mode: protects EN quotations and manages flags by language                                               |
| `--add_translation_note`           | Add a translation note                                                                                        |
| `--note_position`           | Note position: `top`, `bottom` (default), or `both`                                   |
| `--note_format`           | Note format: `legacy` (default, bold paragraph) or `marker`                                       |
| `--include_model`           | Include the model name in the output file                                                                     |
| `--reasoning_effort`           | GPT-5.x reasoning effort: `none`/`low`/`medium`/`high`/`xhigh`         |

The eight `--use_*` flags are mutually exclusive: combining two is
rejected.

## Providers

### Via API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` switches to each provider's economy tier.

| Provider   | Quality (default)                                     | Economy (`--eco`)   |
| ---------- | ----------------------------------------------------- | -------------------------- |
| OpenAI     | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                                       | `claude-haiku-4-5`            |
| Mistral    | `mistral-large-latest`                                       | `mistral-small-latest`            |
| Gemini     | `gemini-3.7-flash`                                       | `gemini-3.1-flash-lite`            |
| Codex      | `gpt-5.6-sol` (also `terra` and `luna` via `--model`) | `gpt-5.6-luna`            |
| Grok API   | `grok-4.6`                                       | `grok-4.3`            |
| Grok CLI   | `grok-4.6`                                       | `grok-4.5`            |
| OpenCode   | `--model provider/modèle` required                              | same—`--eco` has no effect |
| OpenRouter | `--model fournisseur/modèle` required                              | same—`--eco` has no effect |
### Using a ChatGPT subscription: `--use_codex`

Runs the official Codex CLI: translation is deducted from the ChatGPT
subscription quota, without an API key or usage-based billing.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- The binary is searched for in `CODEX_BIN`, then the `PATH`, then the
  `openai-codex-cli-bin` package. `~/.codex/auth.json` is never read.
- `OPENAI_API_KEY` and `CODEX_API_KEY` are removed from the subprocess
  environment: an existing key never causes a switch to the API.
- Each segment costs at least one “message” from the 5-hour window—two
  if validation fails and it is retried. As an estimate, OpenAI announces
  250–2,000 messages/5 h for `gpt-5.6-luna` (`--eco`) and
  10–100 for `gpt-5.6-sol` on a Plus plan.
- `--model gpt-5.6-terra` and `--model gpt-5.6-luna` also go through the
  subscription. A model the account is not entitled to use returns a 400 “model is
  not supported when using Codex with a ChatGPT account”.
- Slower than an API, and the gap grows with the document: on this README,
  a median of 6 min 46 s per language with `gpt-5.6-sol`, compared with 36 s for
  `gemini-3.7-flash`.
- Rejected in CI (`CI` or `GITHUB_ACTIONS` set): subscription authentication
  uses a personal session file, which does not belong on a shared
  runner.
- Variables: `CODEX_BIN`, `CODEX_TIMEOUT` (seconds per segment, default 600).

### Using a Grok subscription: `--use_grok_cli`

The same principle applies with the official Grok Build CLI, using a SuperGrok or
X Premium+ subscription.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Weaker isolation than Codex.** Grok's OS sandbox does not work
  on many recent Linux systems (AppArmor, container runtime
  sockets), and a profile that cannot be applied silently starts without
  confinement. The script therefore requests no profile by default, states this,
  and relies on the CLI's `--deny` rules, including the catch-all `*`—the only
  layer that refuses to start instead of silently removing protection.
  `GROK_TRANSLATE_SANDBOX=read-only` requires the OS sandbox, and startup
  fails if the machine cannot honor it.
- The quota is weekly, shared with Chat, Imagine, and Voice, and no
  command can read it: a batch may consume conversational usage
  without warning.
- Variables: `GROK_BIN`, `GROK_HOME` (CLI directory, default `~/.grok`),
  `GROK_TIMEOUT` (default 900), `GROK_TRANSLATE_SANDBOX`.

### Using the provider of your choice: `--use_opencode`

[OpenCode](https://opencode.ai) is an open-source (MIT) coding agent that
routes requests to the providers configured within it: API key, subscription,
OpenCode Zen gateway (free models, no account required), or local model. Two
paths were measured end-to-end here: Zen and Ollama.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur

# gratuit, sans compte ni clé — données utilisables pour l'entraînement
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en
# local, hors ligne
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de
# sur un abonnement déjà payé
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

`--model` is required: without it, OpenCode would fall back to a free model
whose conversations may be used for training, and that choice is not made on
your behalf.

Isolation on every call:

- an inline configuration, which takes precedence over yours, defines a `aipmt`
  agent for which all tools are denied (`permission: { "*": "deny" }`), session
  sharing is disabled, `--pure`, never `--auto`;
- a disposable, empty working directory, with `OPENCODE_DISABLE_PROJECT_CONFIG` and
  `OPENCODE_DISABLE_CLAUDE_CODE` set—without them, OpenCode injects the current directory's
  `AGENTS.md` and `~/.claude/CLAUDE.md` into the prompt. The global
  `~/.config/opencode/AGENTS.md` is still injected; OpenCode does not allow it
  to be excluded;
- output contract: exit code 0, no `error` event, no tool
  call, final step in `stop`, non-empty text, and the `aipmt` agent
  actually loaded—an unknown `--agent` does not cause OpenCode to fail; it
  silently falls back to the coding agent;
- no `aipmt` key is passed through, except `OPENCODE_API_KEY`, OpenCode's
  own key. Providers are configured in OpenCode, not in
  `aipmt`'s `.env`.

Things to know:

- Zen's free models change over time, have undocumented limits, and
  their conversations may be used for training: suitable for public
  documentation, not private content.
- A local model must provide at least 16k context tokens, since segments
  can contain up to 16,000 characters. Ollama often configures 4,096: use
  a `Modelfile` with `PARAMETER num_ctx 32768`.
- `--eco` has no effect; `--reasoning_effort` is passed unchanged as
  OpenCode's `--variant`.
- OpenCode logs every session in `~/.local/share/opencode/`.
- Variables: `OPENCODE_BIN` (otherwise the `PATH`, then `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (seconds per segment, default 600). `OPENCODE_CONFIG`
  is passed unchanged to OpenCode.

Example of a local model through Ollama, in `~/.config/opencode/opencode.json`:

```bash
ollama pull gpt-oss:20b
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": { "baseURL": "http://127.0.0.1:11434/v1" },
      "models": {
        "gpt-oss-20b-32k": {
          "name": "gpt-oss 20B (32k, sans réflexion)",
          "limit": { "context": 32768, "output": 8192 },
          "options": { "reasoningEffort": "none" }
        }
      }
    }
  }
}
```

`reasoningEffort: "none"` disables the reasoning that Ollama enables by default for these
models and that a Modelfile cannot disable. Measured on a six-word
sentence: 919 reasoning tokens and 68 seconds without the option, 9 tokens with it.

### Using more than 400 models: `--use_openrouter`

OpenRouter is a usage-based router, billed against a single credit balance, for
models hosted by third parties—including open Chinese models that no
other provider exposes here.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` is required. A preflight, run before any billing occurs, handles
two routing specifics:

- **The same model is served by dozens of hosts with different
  limits**—for `z-ai/glm-5.3-flash`, 23 hosts, including one capped at
  2,048 output tokens. The preflight reads `/api/v1/models/{modèle}/endpoints`,
  excludes hosts with fewer than 8,000 output tokens or degraded status, and
  pins the others with `allow_fallbacks: false`.
- **Reasoning is billed at the output rate**—107 tokens versus 2 for
  an “OK” response from `z-ai/glm-5.2`. It is disabled by default; models
  that require it receive the lowest effort they accept, since the catalog
  default may exhaust the output before the translation is complete.
  `--reasoning_effort` still takes precedence.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- The context window comes from the catalog. A model with fewer than 16,400 tokens is
  rejected before any call: 8,400 for the prompt and segment, with at least
  8,000 for output.
- A slug missing from the catalog, an unreachable catalog, or the absence
  of a host that meets the limit stops the command.
- `finish_reason=length` with empty output is a budget consumed by
  reasoning, not truncation: the message distinguishes between them.
- `--eco` has no effect.
- Variables: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (default `https://openrouter.ai/api/v1`, `https://`
  required), `OPENROUTER_TIMEOUT` (default 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (default 30).

### Translation note

`--add_translation_note` adds a note, in `bottom` (default), `top` (after the
front matter), or `both` (`--note_position`), using the `legacy` format (bold
paragraph, default) or `marker` (`--note_format`). The `marker` format is an
invisible Markdown reference definition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
followed by a bold citation: readable on GitHub and usable at build time by a
remark plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detailed measurements

All measurements are actual translations run with `aipmt`, into
fourteen languages: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Written** counts the files that passed the guards; **No
difference** counts those where `scripts/compare_structure.py` reports nothing—the same number of
sections, subheadings, links, distinct URLs, code blocks,
inline code spans, table rows, blockquotes, and bold words.

“No difference” means “nothing detected,” not “identical”: the comparator
counts elements without reading their content. It does not report a deleted
level-4 heading, replaced inline-code text, or a swapped
flag, and it does not assess the language.

### Dense monitoring article, `--news` mode

An edition of the [jls42.org AI monitoring digest](https://jls42.org/fr/news):
589 lines, 140 links, 21 sections, 3 protected English quotations. Campaign
run on September 4 and 5, 2026.

| Model                             | Access               | Written | No difference | Median/language |
| --------------------------------- | -------------------- | ------- | ------------- | --------------- |
| `gemini-3.7-flash`                | Google API           | 14/14   | ✅ **14/14**  | 1 min 18 s      |
| `gpt-5.6-sol` (`--use_codex`)     | ChatGPT subscription | 14/14   | ✅ **14/14**  | 11 min 28 s     |
| `z-ai/glm-5.2`                    | OpenRouter           | 14/14   | ✅ **14/14**  | 5 min 37 s      |
| `qwen/qwen3.8-flash`              | OpenRouter           | 14/14   | ✅ **14/14**  | 26 min 23 s     |
| `claude-sonnet-5`                 | Anthropic API        | 14/14   | ⚠️ 11/14      | 6 min 31 s      |
| `opencode/mimo-v2.5-free`         | OpenCode Zen         | 13/14   | ❌ 11/14      | 9 min 27 s      |
| `qwen/qwen3.7-flash`              | OpenRouter           | 13/14   | ❌ 8/14       | 10 min 09 s     |
| `ollama/gpt-oss-20b-32k`          | local                | 10/14   | ❌ 7/14       | 12 min 39 s     |
| `mistral-large-latest`            | Mistral API          | 11/14   | ❌ 5/14       | 5 min 32 s      |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter           | 4/14    | ❌ 3/14       | 37 min 27 s     |
| `grok-4.6` (`--use_grok_cli`)     | Grok subscription    | 1/14    | ❌ 1/14       | 23 min 11 s     |

Grok was measured again on September 9 using another edition of the same digest
(356 lines): 9 languages written out of 14, 8 with no difference. This is the figure
shown in the summary table. Three interrupted campaigns are not
listed: `qwen3.5-27b` (9 languages) and `kimi-k2.6` (4) due to insufficient credit,
and `z-ai/glm-5.3-flash`, whose two failures came from a reasoning setting
that the provider has since fixed. The OpenRouter rows were measured with the
router's default settings, before `--use_openrouter`; `z-ai/glm-5.2`,
measured again with the bundled provider, produces the same 14/14. The figures were
recalculated on September 10 with the current comparator: `qwen3.8-flash` and
`qwen3.7-flash` each gain one language compared with the first
publication; the others are unchanged.

### This project's README, standard Markdown

Revision frozen on September 9, 2026: 785 lines, 285 inline code spans, 40
block fences, 89 table rows. Four translations in parallel.

| Model                         | Written | No difference | Median/language | What differs                                                               |
| ----------------------------- | ------- | ------------- | --------------- | -------------------------------------------------------------------------- |
| `gemini-3.7-flash`            | 14/14   | ⚠️ 13/14      | 36 s            | one bold word (ja)                                                         |
| `claude-sonnet-5`             | 14/14   | ⚠️ 12/14      | 2 min 56 s      | one link (sv), one bold word (zh)                                          |
| `gpt-5.6-sol` (`--use_codex`) | 14/14   | ⚠️ 12/14      | 6 min 46 s      | one bold word (ar, ja)                                                     |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14   | ⚠️ 11/14      | 2 min 34 s      | one bold word (hi, ja, ko)                                                 |
| `qwen/qwen3.7-flash`          | 14/14   | ⚠️ 10/14      | 2 min 17 s      | 40 inline code spans added in Arabic; bold text (hi, ja, ko)               |
| `mistral-large-latest`        | 14/14   | ❌ 1/14       | 2 min 44 s      | one section lost (ar, hi, ko); code blocks added (ja, ko, ro, zh)          |

Two interrupted campaigns are not listed: Grok, whose CLI session expired
after twelve languages (eleven with no difference), and `qwen3.8-flash`, whose
host returned HTTP 429 after two. `opencode/mimo-v2.5-free` and `ollama/gpt-oss-20b-32k`
were not measured again on this revision; on the September 4 and 5 revision,
which was 277 lines shorter, each wrote 9 translations out of 14, including 7
and 1 with no difference.

### Four READMEs from well-known projects

FastAPI, Ollama, tldr-pages, and Vue.js, taken as-is from GitHub—documents
that are easier than the previous two. The campaign targeted the models
that struggled; Gemini serves as a point of comparison.

| Model                     | Scope                      | Written | No difference |
| ------------------------- | -------------------------- | ------- | ------------- |
| `gemini-3.7-flash`        | 4 projects × 14 languages   | 56/56   | ✅ **55/56**  |
| `opencode/mimo-v2.5-free` | 4 projects × 14 languages   | 55/56   | ❌ 47/56      |
| `grok-4.6` (subscription)   | 4 projects × ar, hi, ja, zh | 16/16   | ❌ 14/16      |
| `ollama/gpt-oss-20b-32k`  | 4 projects × ar, hi, ja, zh | 15/16   | ❌ 9/16       |

### What these measurements are not

- **Not an exhaustive ranking**: OpenRouter alone offers more than four hundred
  models; around fifteen were measured.
- **Indicative durations**: three to six translations ran in parallel depending on
  the campaign, and a provider's throughput varies throughout the day.
- **Time-specific observations**: models change under the same name, and your
  documents are not ours.

To repeat the measurement on your documents, using a frozen copy of the file:

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## Contributing

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

Both lines are required: without `pip install -e .`, `python -m aipmt`
returns `No module named aipmt`.

Quality tooling, optional but recommended:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

The repository's 28 translations (README and CHANGELOG, fourteen languages) are
regenerated with `./regen_translations.sh --force`—Codex and `gpt-5.6-sol` using the
ChatGPT subscription by default, four in parallel. `REGEN_PROVIDER` and
`REGEN_MODEL` change the path; a billed API (`openai`, `gemini`,
`grok`, `openrouter`) is rejected without `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` caps each job (600 s, 1,800 s on Codex). Tooling details
are in `CLAUDE.md`.

## Projects using this script

- **[jls42.org](https://jls42.org)**—a personal blog published in 15 languages. Its
  [daily AI monitoring digest](https://jls42.org/fr/news) is translated every day
  by this tool and serves as the reference document for the measurements above.

## Author

Julien LE SAUX
Email: contact@jls42.org

## License

GNU GENERAL PUBLIC LICENSE Version 3. See [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Disclaimer

This program is distributed **without any warranty**, under the terms of
sections 15 and 16 of GPL v3: provided “as is,” without warranty of
merchantability or fitness for a particular purpose, and its author cannot be
held liable for any damage resulting from its use. The license text
takes precedence over this summary.

- **Review before publishing.** The safeguards cover code blocks,
  inline code, URLs, anchors, and quotations in `--news` mode—not
  headings, tables, front matter, or the meaning of your sentences.
- **Your documents are sent to the selected provider**, under its terms
  of service and data policy. Some free models may reuse your
  conversations for training; a local model is the only option that keeps
  all data on your machine.
- **API calls are billed to you.** This program does not cap
  spending: a long document, a retry after failure, or a model that performs
  extensive reasoning costs more.
- **Published measurements are time-specific observations**, not guarantees.

The product and company names mentioned belong to their respective owners.
This project is not affiliated with any of them.

**Article translated from fr to en with gpt-5.6-sol.**
