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

Translates Markdown files from one language to another while preserving structure:
code blocks, inline code, URLs, anchors, tables, and front matter. Eleven ways to
call a model — five APIs, four subscriptions without pay-per-use billing, two
routers — and a published benchmark of what each model truly preserves.

## Overview

- **Eleven provider paths**: OpenAI, Mistral, Claude, Gemini, and Grok APIs;
  ChatGPT (Codex), Grok, Google (Antigravity), and Claude (Claude Code) subscriptions
  without pay-per-use billing; OpenCode (open source, free or local) and OpenRouter
  (over 400 models) routers.
- **No corrupted output from dropped tokens**: code blocks, inline code,
  URLs, anchors, and blockquotes are replaced with tokens prior to the call and
  verified upon return. If any token is missing, the file is not written.
- **Long documents**: chunking according to the model's context window.
- **`--news` mode**: protected English quotes and flags handled per
  language, tailored for tech watch articles.
- **`--eco` mode**: fast and cost-effective models.
- **Optional translation note**: top, bottom, or both.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 or newer. To install from source, see
[Contributing](#contributing).

## Configuration

Keys are loaded from three locations, in order of priority; each source only
fills in values left unset by the preceding one.

|     | Where                                         | Purpose                               |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Environment variables                         | CI, containers, one-off overrides     |
| 2   | `.env` in current (or parent) directory | project-specific key                  |
| 3   | `~/.config/aipmt/.env`                                 | configured once, applies globally     |

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

`GEMINI_API_KEY` is accepted as an alternative to `GOOGLE_API_KEY`. The user
configuration file follows `XDG_CONFIG_HOME` (absolute path only) and `%APPDATA%`
on Windows. If no key is found, the command lists all three locations.

**A project-level `.env` cannot redirect requests or select the executed
program.** It only provides keys, never endpoints or binaries: any variable
matching `_BASE_URL`, `_API_BASE`, `_ENDPOINT`, or `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, proxies (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), certificate stores (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`), and `XDG_CONFIG_HOME` /
`APPDATA` are ignored with a warning. A cloned repository must not be able
to hijack your key or execute arbitrary local binaries upon the first translation.
This file is also parsed without variable expansion: `NOM=${OPENAI_API_KEY}` does not
copy keys here. Set these variables in your environment or in `~/.config/aipmt/.env`.

Optional variables: `XAI_BASE_URL` (default `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (timeout in seconds per call, default 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(default 600), `GROK_BIN`, `GROK_HOME` (default `~/.grok`), `GROK_TIMEOUT`
(default 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (default 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (default 600), `OPENROUTER_BASE_URL`
(`https://` required), `OPENROUTER_TIMEOUT` (default 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (default 30). Each variable is detailed in its
respective provider section.

## Getting Started

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

Translating `document.md` into Spanish outputs `document-es.md` in `--target_dir`;
with `--include_model`, `document-es-gpt-6.1-terra.md`. The file extension always becomes
`.md` — `article.mdx` becomes `article-en.md` — except when using
`--keep_filename`, which keeps the original filename. Existing translations are
skipped unless `--force` is passed.

Exit codes: `0` if everything succeeded or was skipped, `1` if any file
failed (failures listed on stderr), `2` on configuration errors.
A failed file is never written to disk, even if the write operation itself fails:
content is written to a temporary file and atomically renamed. Simply re-running the command resumes work.

## Choosing a Model

Benchmarked across two real-world documents translated into the same fourteen
languages by each model. **The score represents the number of languages out of
fourteen where the translation was written with zero differences from the source.**

| Model                 | Access Method                     | Dense Tech Watch Article | This README  | Differences Observed and Impacted Languages                                                                                                                         |
| --------------------- | --------------------------------- | ------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.8 Flash**  | Google subscription (Antigravity) | ✅ 14/14                 | ✅ 14/14     | none across both documents                                                                                                                                          |
| **Claude Sonnet 5.5** | Anthropic API key                 | ✅ 14/14                 | ✅ 14/14     | none across both documents                                                                                                                                          |
| **Gemini 3.7 Flash**  | Google API key                    | ✅ 14/14                 | ⚠️ 13/14     | 1/14 languages: an extra bold word (ja)                                                                                                                             |
| **Gemini 3.7 Flash**  | Google subscription (Antigravity) | ✅ 14/14                 | ⚠️ 13/14     | 1/14 languages: a missing bold word (ko)                                                                                                                            |
| **GPT-5.6 Sol**       | ChatGPT subscription or OpenAI key| ✅ 14/14                 | ⚠️ 12/14     | 2/14 languages: a missing bold word (ar, ja)                                                                                                                        |
| **GLM-5.2**           | OpenRouter key                    | ✅ 14/14                 | ⚠️ 11/14     | 3/14 languages: a missing bold word (hi, ja, ko)                                                                                                                    |
| Claude Sonnet 5       | Claude subscription (Claude Code) | ⚠️ 13/14                 | ⚠️ 13/14     | 1/14 languages on article: extra bold word (zh); 1 on README: table row merged into previous row, hidden from rendering (ar)                                         |
| Claude Haiku 4.5      | Claude subscription (Claude Code) | ⚠️ 11/14                 | ✅ 14/14     | 3 languages on article: section header promoted to level 1 (en, pl, ro); on README, diff-clean, but internal links duplicated in English                           |
| Claude Sonnet 5       | Anthropic API key                 | ⚠️ 11/14                 | ⚠️ 12/14     | 3 languages on article: phantom code block appeared (es, de, hi); 2 on README: link stripped of markdown syntax (sv), extra bold word (zh)                          |
| Claude Haiku 4.5      | Anthropic API key                 | ⚠️ 7/14                  | ✅ 14/14     | 7 languages on article: section header promoted to level 1 — untranslated French in Japanese; clean on README                                                       |
| Claude Haiku 5.5      | Anthropic API key                 | ⚠️ 11/14                 | ❌ 12/14     | 3 languages on article: header level altered or duplicated (ja, ko, zh); on README, 2 languages failed validation due to lost inline code (ar, hi)                  |
| Qwen 3.7 Flash        | OpenRouter key                    | ❌ 8/14                  | ⚠️ 10/14     | 1 language rejected on article, 5 diverged; on README, ~40 words incorrectly wrapped in `code` (ar)                                                        |
| Grok 4.6              | Grok subscription                 | ❌ 8/14                  | unrated      | 5/14 languages failed due to lost inline code and URLs; Dutch completely diverged                                                                                   |
| GPT-OSS 20B           | local model (Ollama)              | ❌ 7/14                  | not retested | 4/14 languages failed: untranslated French remained in output, caught by guardrails                                                                                 |
| MiMo v2.5 (free)      | OpenCode Zen, no account required  | ❌ 11/14                 | not retested | 1 language failed; an entire section dropped in Polish                                                                                                              |
| Mistral Large         | Mistral API key                   | ❌ 5/14                  | ❌ 1/14      | **an entire section vanished**: 1 language on article (hi), 3 on README (ar, hi, ko) — and 3 languages rejected on article                                           |
| DeepSeek V4 Flash     | OpenRouter key                    | ❌ 3/14                  | not retested | 10/14 languages failed; 37 minutes per language                                                                                                                     |
| Claude Opus 5.5       | Claude subscription (Claude Code) | ❌ 0/14                  | ✅ 14/14     | article blocked in all 14 languages by Opus safety filters triggered by a biology news item; zero differences on README                                              |

|     | Symbol Meaning                                                                                                                                                        |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | all fourteen languages translated with zero differences compared to the source                                                                                        |
| ⚠️  | all fourteen languages translated; discrepancies are strictly **formatting artifacts** — a bold word, a `code`, a link missing brackets. No text, URLs, code blocks, or sections missing |
| ❌  | at least one language failed translation (file rejected, not written) **or** content was dropped from an output file                                                 |

Key takeaways:

- **A rejected translation is not a corrupted translation.** If a token is
  missing from the output, the file is not written, and the language is marked
  as failed. This is what occurs with Grok on the article: four inline codes and
  three URLs were lost starting in the very first chunk across the five non-Latin scripts.
- **A model can reject an entire document over a single sentence.** Opus 5.5
  translates this README flawlessly, but fails completely on the tech watch article:
  safety filters halted generation due to a brief biology news item. The file was
  not written, and aipmt logs the reason.
- **This safety net does not protect headings, tables, front matter, or
  prose.** If a model drops an entire section, the tool writes the output file
  without flagging it — as observed with Mistral. These components cannot be replaced
  with tokens and are not monitored by current guardrails; `scripts/compare_structure.py` detects
  missing sections, but only after the fact.
- **Grok has no score for this README**: its CLI session timed out after twelve
  languages (eleven of which had zero differences). Incomplete benchmark runs are left unrated.
- **Document density matters more than target language.** Grok handles standard
  READMEs smoothly but breaks on link-heavy articles, even in Dutch.

Dates and source files: the "This README" benchmark was evaluated on September 9, 2026,
against a frozen revision of this document (785 lines, 285 inline code snippets, 89
table rows), edited since — except for the Antigravity and Claude Code rows,
evaluated on September 26 against the shorter revision released with 1.14.0
(600 lines, 257 inline code snippets, 85 table rows), and the Claude Sonnet 5.5,
Haiku 5.5, and Haiku 4.5 API rows, evaluated on October 18 against the same revision.
The "Dense Tech Watch Article" benchmark stems from the September 4–5 run on a
589-line article, except for Grok (reevaluated on September 9 on another edition
of the same watch), Antigravity and Claude Code (tested on September 26 on the
same article), and the three Claude models (October 18). Complete data tables,
timings, and test protocols can be found in [Detailed Benchmarks](#detailed-benchmarks).

## All Options

| Option                   | Description                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Single Markdown file to translate (alternative to `--source_dir`)                                             |
| `--source_dir`           | Source directory containing the Markdown files (default: `content/posts`)                                   |
| `--target_dir`           | Output directory for translated files (default: `traductions_en`)                                    |
| `--source_lang`          | Source language (default: `fr`)                                                                                  |
| `--target_lang`          | Target language (default: `en`)                                                                                   |
| `--model`                | Specific model to use                                                                                  |
| `--eco`                  | Use budget models                                                                              |
| `--use_mistral`          | Use the Mistral AI API                                                                                     |
| `--use_claude`           | Use the Claude API                                                                                         |
| `--use_gemini`           | Use the Gemini API                                                                                         |
| `--use_grok`             | Use the xAI (Grok) API — requires `XAI_API_KEY`                                                           |
| `--use_codex`            | Use the Codex CLI against the ChatGPT subscription quota                                                    |
| `--use_grok_cli`         | Use the Grok CLI against the Grok subscription quota                                                        |
| `--use_antigravity`      | Use the Antigravity CLI (`agy`) against the Google AI Pro or Ultra subscription quota                       |
| `--use_claude_code`      | Use the Claude Code CLI (`claude -p`) against the Claude Pro or Max subscription quota                      |
| `--use_opencode`         | Use OpenCode (open source) with the provider configured in OpenCode; requires `--model provider/modèle` |
| `--use_openrouter`       | Use OpenRouter — requires `OPENROUTER_API_KEY` and `--model fournisseur/modèle`                          |
| `--force`                | Force re-translation                                                                                       |
| `--keep_filename`        | Keep the original filename                                                                          |
| `--news`                 | News mode: protects EN quotes, handles per-language flags                                      |
| `--add_translation_note` | Add a translation note                                                                                |
| `--note_position`        | Note position: `top`, `bottom` (default), or `both`                                                     |
| `--note_format`          | Note format: `legacy` (default, bold paragraph) or `marker`                                            |
| `--include_model`        | Include model name in output file                                                            |
| `--reasoning_effort`     | GPT-5.x reasoning effort: `none`/`low`/`medium`/`high`/`xhigh`                                         |

The nine `--use_*` flags are mutually exclusive: combining two is
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

`--eco` switches to each provider's budget tier.

| Provider    | Quality (default)                                                     | Budget (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-6.1-terra`                                                      | `gpt-6-luna`              |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-4-hydrogen`                                                  | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (also `gpt-5.6-sol`, `terra` and `luna` via `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.7`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | ditto — `--eco` has no effect |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.8-flash-low`    |
| Claude Code | `sonnet`, effort `low`                                               | ditto — `--eco` has no effect |
| OpenCode    | `--model provider/modèle` required                                | ditto — `--eco` has no effect |
| OpenRouter  | `--model fournisseur/modèle` required                             | ditto — `--eco` has no effect |

Defaults follow the latest generation from each provider, benchmarked
before adoption: GPT-6 at OpenAI, Gemini 4 Hydrogen at Google,
Grok 4.7 at xAI since 1.19.0. Previous models remain supported
via `--model` (`gpt-5.6-terra`, `gemini-3.8-flash`, `grok-4.6`…), as do
Gemini 4 Argon and Carbon, Google's high-end models. aipmt manages
the reasoning effort of GPT and Grok models itself, disabled in `--eco`, and
`--reasoning_effort` forces it; a Gemini model always receives the lowest
level it supports.
A temporary failure of the Gemini API (503, 429, timeout) retries
the call up to three times, after 10, 20, then 40 seconds. An attempt
left without a response is aborted after 5 minutes, then retried in the same
way: an unresponsive server fails the segment in about twenty minutes
at most, rather than hanging indefinitely.

### On ChatGPT Subscription: `--use_codex`

Drives the official Codex CLI: translation is deducted from the ChatGPT
subscription quota, with no API key or usage-based billing.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- The binary is searched in `CODEX_BIN`, then `PATH`, then the package
  `openai-codex-cli-bin`. `~/.codex/auth.json` is never read.
- `OPENAI_API_KEY` and `CODEX_API_KEY` are removed from the subprocess
  environment: an existing key never triggers a switch to the API.
- Each segment costs at least one "message" from the 5-hour window — two
  if its validation fails and it is retried. OpenAI advertises, as an
  estimate, 250–2,000 messages/5 h for `gpt-5.6-luna` (`--eco`) and
  10–100 for `gpt-5.6-sol` on a Plus plan.
- `--model gpt-5.6-sol`, the default until 1.16.3, `--model gpt-5.6-terra`
  and `--model gpt-5.6-luna` also go through the subscription.
- A 429 from the server does not cause the file to be lost: Codex reconnects on its own,
  aipmt waits for the turn to end, and if the 429 persists, the segment
  restarts after 30, then 60 seconds. A model the account is not entitled to returns a 400 "model is
  not supported when using Codex with a ChatGPT account".
- Slower than an API, and the gap widens with document size: on this README,
  median of 6 min 46 s per language with `gpt-5.6-sol`, versus 36 s for
  `gemini-3.7-flash`.
- Rejected in CI (`CI` or `GITHUB_ACTIONS` defined): the subscription authenticates
  via a personal session file, which does not belong on a shared
  runner.
- Variables: `CODEX_BIN`, `CODEX_TIMEOUT` (seconds per segment, default 600).

### On Grok Subscription: `--use_grok_cli`

Same principle with the official Grok Build CLI, on a SuperGrok or
X Premium+ subscription.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Weaker containment than Codex.** Grok's OS sandbox does not apply
  on many recent Linux systems (AppArmor, container runtime sockets),
  and a profile that cannot be applied starts unconfined silently.
  The script therefore requests no profile by default, announces it, and
  relies on the CLI's `--deny` rules, including the `*` catch-all — the only
  layer that refuses to start rather than silently dropping protection.
  `GROK_TRANSLATE_SANDBOX=read-only` enforces the OS sandbox, and startup
  fails if the machine cannot honor it.
- The quota is weekly, shared with Chat, Imagine, and Voice, and no
  command allows checking it: a batch run can deplete conversational
  usage without warning.
- Variables: `GROK_BIN`, `GROK_HOME` (CLI directory, default `~/.grok`),
  `GROK_TIMEOUT` (default 900), `GROK_TRANSLATE_SANDBOX`.

### On Google Subscription: `--use_antigravity`

Same principle with `agy`, the official Antigravity CLI: for those paying for Google
AI Pro or Ultra, translation is deducted from the subscription quota instead
of being billed per token. This is the only path to this quota: Gemini CLI no
longer serves these accounts since June 18, 2026
([announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
and the Antigravity SDK only accepts an API key or a Google Cloud project.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **No paid paths remain open.** agy receives from your environment
  only a closed list of variables — `PATH`, language and timezone,
  terminal, identity, proxies and certificates, session bus — and no keys:
  several of its variables divert a call without displaying anything (measured:
  one sends the document to a third-party gateway, another to a billed Google
  Cloud project), and a denylist missed some on every review.
  Before any segment, `agy -p /config`, which costs no quota, must show
  paid AI credits disabled, with neither an API key nor a Google Cloud project — a
  missing setting counts as a rejection —, otherwise nothing is translated; the log of each
  call must then confirm the subscription (`authMethod=consumer`), otherwise the
  response is rejected.
- **Containment.** Each call runs in a private, disposable personal
  directory, with a tool-less translation agent: your agy settings, rules,
  plugins, MCP servers, and hooks do not enter it, nothing is added to your
  history, and the login session remains in the keyring, which aipmt never reads.
  A missing agent causes agy to fall back silently to its coding agent
  and its tools: an entire line in the log must confirm the right agent — a
  document quoting this message does not replace it —, otherwise it is rejected.
- **Platforms**: Linux, inside a session that has a keyring (D-Bus session bus,
  Secret Service); macOS is supported, but untested in benchmarks. Rejected
  on Windows, where agy does not read the variables that isolate each call, and
  on Linux without a session bus — SSH sessions, containers, servers: agy
  stores its token in a file inside `~/.gemini` there, which isolation hides.
  Rejection occurs before any launch, along with its reason, instead of a one-minute
  wait for a login code.
- **Models**: those of `agy models`. Gemini models include the effort level in their name
  (`gemini-3.8-flash-medium`…): a name without a suffix is rejected before the call,
  and `--reasoning_effort` has no effect. By default `gemini-3.8-flash-medium`,
  and `gemini-3.8-flash-low` in `--eco`, since agy no longer serves Gemini 3.7
  Flash; the benchmark campaign that established the default is
  described in [Detailed Benchmarks](#detailed-benchmarks). Gemini 4 Hydrogen
  (`gemini-4-hydrogen-low`…) shares the 3.8 Flash quota and consumes
  more of it: 0.95 points of the 5-hour window for this README at medium
  effort, compared to 0.32. Claude and GPT-OSS
  have their own, much smaller quota: about 1% of the 5-hour window
  per measured call, compared to 0.05% for Flash. Gemini 4 Argon has its
  own weekly quota: this README consumes 1.35% of it.
- **Quota**: per group, a 5-hour window and a weekly window, prorated
  by token cost. Measured on the author's account: about
  16 points of the 5-hour window per million source characters in
  `gemini-3.8-flash-medium`, 14 in `gemini-3.7-flash-medium`, and 7 to 8 at
  low effort — a 40,000-character README therefore costs just over half a
  point. The weekly limit depends on the tier. Retries follow
  what agy marks as retryable; otherwise, an exhausted window is never
  retried: it fails every file until the reset displayed by
  `/usage`.
- **Slower than the API**: on the dense benchmark article, median of 3 min 59 s per
  language in `gemini-3.8-flash-medium` and 3 min 14 s in
  `gemini-3.7-flash-medium`, versus 1 min 18 s for Gemini 3.7 Flash via the API.
- **Interruption**: Ctrl-C, or closing the terminal, stops agy along with the
  command instead of letting it finish its turn against your quota; the same
  applies to Codex, Grok CLI, and OpenCode. Under `nohup`, translation continues.
- Rejected in CI (`CI` or `GITHUB_ACTIONS` defined): the login session lives in a
  personal keyring. On a runner, use `--use_gemini` with `GOOGLE_API_KEY`.
- Variables: `AGY_BIN` (otherwise `PATH`, then `~/.local/bin/agy`),
  `AGY_TIMEOUT` (seconds per segment, including startup, default 900).

**Terms of Service: your own account is at stake.** Antigravity's
[Terms of Service](https://antigravity.google/terms) (section 6) and its
[FAQ](https://antigravity.google/docs/faq/) prohibit accessing the service
through third-party software using the Antigravity login — Claude Code,
OpenClaw, and OpenCode are cited —, under penalty of account suspension. aipmt
neither reads nor reuses the token: it runs the official binary in the
[headless mode](https://antigravity.google/docs/cli/headless/) that Google
documents for scripts and CI. A Google team member described running
`agy -p` from a local script for personal work as "standard"
([official forum, September 25, 2026, non-binding answer](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
no official text specifically addresses a distributed tool like this one.

**Public documents only.** According to section 5 of the same terms,
exchanges — prompts, responses, metadata — may be used to improve Google's
products and machine learning, and may be reviewed by
humans, even on paid subscriptions. Opting out requires the
`enableTelemetry` setting, whose effect is undocumented and which aipmt does not set; your agy
settings do not carry over into its isolation. Do not run anything confidential through it.

### On the Claude subscription: `--use_claude_code`

Same principle with `claude`, the official Claude Code CLI, in `-p` mode: for
whoever pays for Claude Pro or Max, the translation is deducted from the
subscription quota instead of being billed per token. Not to be confused with
`--use_claude`, Anthropic's API, billed on usage.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **No paid route remains open, and each call proves it.** Claude
  Code receives from your environment only a closed list of variables — no
  API key, no token, no cloud provider, nor any marker of the Claude Code session
  from which aipmt would be launched. Before the first segment, `claude auth status` must
  show the subscription connection, without a Console key, and `/usage`, which costs
  no quota, must attest to it; each call in turn attests to it in its
  initialization event, otherwise the response is rejected.
- **Disable "extra usage"** (claude.ai, Settings → Usage) so
  that the zero-euro guarantee holds: when enabled, it takes over when a window is exhausted and
  bills without displaying an error. aipmt stops the translation as soon as the quota
  report of a call indicates it, but that specific call is already billed.
- **Quota shared with your Claude Code sessions.** Each call reports
  the usage of the 5-hour and weekly windows; beyond 80%
  (`AIPMT_CLAUDE_MAX_UTILIZATION`), no further segment is launched, so as
  not to exhaust what serves your work.
- **Confinement.** Each call runs without tools, in a private and
  disposable directory, in personalization-free mode: neither your `CLAUDE.md`, nor your plugins,
  hooks, MCP servers, or settings are loaded, and nothing is retained from the
  session. Attachments are disabled: an `@chemin` in your document
  remains plain text and opens no file (benchmarked).
- **Models**: `sonnet` by default, at effort `low`, and in `--eco` as well:
  `--eco` makes no difference on this path. Benchmarked on the same documents, `haiku`
  is twice as slow — it reasons without any way to prevent it — for
  a barely lower cost, and `opus` rejects biology content (see next
  point). Both remain accessible via `--model`; these aliases follow the
  latest model of their family. `fable` and `[1m]` variants are rejected,
  because they route through paid credits. `--reasoning_effort` sets the effort,
  from which translation gains nothing: measured reasoning is negligible or zero.
- **Opus rejects certain biology content.** Its guardrails are
  stricter than Sonnet's, and Anthropic's error message warns that they
  "can sometimes flag biology-research-adjacent work". Benchmarked: a news
  brief about 279 generated molecules caused the article to be rejected across all fourteen
  languages. Nothing is written: aipmt rejects the truncated response, flags the
  guardrails, and recommends `--model sonnet`.
- Disallowed in CI (`CI` or `GITHUB_ACTIONS` set) and on Windows (untested).
- Variables: `AIPMT_CLAUDE_BIN` (otherwise `PATH`, then `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (seconds per segment, default 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (default 0.8), `CLAUDE_CONFIG_DIR` (Claude
  Code's account, never taken from a project `.env`); working directories under
  `XDG_CACHE_HOME/aipmt/claude-code` (default `~/.cache`).

**Terms of service: your account is on the line.** The
[Claude Code legal page](https://code.claude.com/docs/en/legal-and-compliance)
does not prevent "an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription": this is what aipmt does, launching the
official binary and never reading the token. But Anthropic "does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users", prefers the API key for third-party
tools, "including open-source projects", and reserves the right to bill their
usage against paid credits
([Claude Help Center](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
No text resolves the case of a distributed tool launching the binary.

**Data**: on Free, Pro, and Max accounts, model training
also applies to Claude Code when the privacy setting allows it
([data page](https://code.claude.com/docs/en/data-usage)). aipmt retains
no local transcript (`--no-session-persistence`). Do not pass
anything confidential through it.

### To the provider of your choice: `--use_opencode`

[OpenCode](https://opencode.ai) is an open-source coding agent (MIT) that
routes to providers configured within it: API key, subscription,
OpenCode Zen gateway (free models, no account required), or local model. Two
routes were benchmarked end-to-end here, Zen and Ollama.

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

`--model` is mandatory: without it, OpenCode would fall back to a free model
whose exchanges may be used for training, and that choice should not be made
for you.

Confinement on each call:

- an inline configuration, taking precedence over yours, defines a `aipmt` agent
  whose tools are all denied (`permission: { "*": "deny" }`), session sharing
  disabled, `--pure`, never `--auto`;
- disposable and empty working directory, with `OPENCODE_DISABLE_PROJECT_CONFIG` and
  `OPENCODE_DISABLE_CLAUDE_CODE` created — without them, OpenCode injects the current directory's
  `AGENTS.md` and `~/.claude/CLAUDE.md` into the prompt. The
  global `~/.config/opencode/AGENTS.md` remains injected; OpenCode does not allow
  excluding it;
- exit contract: exit code 0, no `error` event, no tool
  call, last step in `stop`, non-empty text, and the `aipmt` agent
  actually loaded — an unknown `--agent` does not cause OpenCode to fail, it
  silently falls back to the coding agent;
- no `aipmt` key is passed, except for `OPENCODE_API_KEY`, OpenCode's
  own key. Providers are configured in OpenCode, not in
  the `.env` of `aipmt`.

Good to know:

- Zen's free models are volatile, have undocumented limits, and
  their exchanges may be used for training: suitable for public documentation,
  not for private content.
- A local model must offer at least 16k context tokens, as segments
  reach up to 16,000 characters. Ollama often sets this to 4,096: use
  a `Modelfile` with `PARAMETER num_ctx 32768`.
- `--eco` has no effect; `--reasoning_effort` is passed as-is as
  OpenCode's `--variant`.
- OpenCode logs each session in `~/.local/share/opencode/`.
- Variables: `OPENCODE_BIN` (otherwise `PATH`, then `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (seconds per segment, default 600). `OPENCODE_CONFIG`
  passes as-is to OpenCode.

Example of a local model via Ollama, in `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` disables the thinking that Ollama enables by default on these
models, which a Modelfile cannot disable. Benchmarked on a six-word
sentence: 919 thinking tokens and 68 seconds without the option, 9 tokens with it.

### To more than 400 models: `--use_openrouter`

OpenRouter is a usage-billed router, using a single credit balance, in front of
models hosted by third parties — including open Chinese models that no
other provider exposes here.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` is mandatory. A preflight check, run before any billing occurs, addresses
two routing specificities:

- **The same model is served by dozens of hosters with varying
  caps** — on `z-ai/glm-5.3-flash`, 23 hosters, including one capped at
  2,048 output tokens. The preflight check inspects `/api/v1/models/{modèle}/endpoints`,
  discards hosters under 8,000 output tokens or with degraded status, and
  pins the remaining ones with `allow_fallbacks: false`.
- **Reasoning is billed at output rates** — 107 tokens versus 2 on
  an "OK" response from `z-ai/glm-5.2`. It is disabled by default; models
  that require it receive the lowest effort setting they accept, as the catalog's
  default could exhaust the output budget before translation finishes.
  `--reasoning_effort` retains precedence.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- The context window is fetched from the catalog. Any model under 16,400 tokens is
  rejected before any call: 8,400 for the prompt and segment, 8,000 minimum
  output.
- A slug missing from the catalog, an unreachable catalog, or the lack
  of a hoster supporting the ceiling will abort the command.
- `finish_reason=length` with an empty output is a budget exhausted by
  reasoning, not a truncation: the message distinguishes between the two.
- `--eco` has no effect.
- Variables: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (default `https://openrouter.ai/api/v1`, `https://`
  required), `OPENROUTER_TIMEOUT` (default 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (default 30).

### Translation note

`--add_translation_note` adds a note, at the `bottom` (default), `top` (after the
front matter), or `both` (`--note_position`), formatted as `legacy` (bold paragraph,
default) or `marker` (`--note_format`). The `marker` format is an
invisible Markdown reference definition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
followed by a bold blockquote: readable on GitHub, actionable at build time by a
remark plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detailed benchmarks

All benchmarks are actual translations run with `aipmt`, into
fourteen languages: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Written** counts the files passed by the guards; **Clean**
counts those where `scripts/compare_structure.py` reports no discrepancies — identical count of
sections, subheadings, links, distinct URLs, code blocks,
inline code, table rows, blockquotes, and bold words.

"Clean" means "nothing detected", not "identical": the comparison tool
counts structural elements without reading their content. It reports neither a deleted
level-4 heading, nor replaced text inside inline code, nor an inverted
flag, nor an internal link formatted with an extra parenthesis,
`[texte]((#ancre))`, which no longer leads anywhere — and it does not judge language
quality.

### Dense tech watch article, `--news` mode

An issue of the [AI watch on jls42.org](https://jls42.org/fr/news):
589 lines, 140 links, 21 sections, 3 protected English quotes. Test run
of September 4 and 5, 2026.

| Model                                           | Access             | Written | Clean        | Median/lang    |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google subscription | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google subscription | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `claude-sonnet-5-5`                             | Anthropic API      | 14/14   | ✅ **14/14** | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT subscription | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | Claude subscription | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | Claude subscription | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `claude-haiku-5-5`                              | Anthropic API      | 14/14   | ⚠️ 11/14     | 2 min 54 s     |
| `claude-haiku-4-5`                              | Anthropic API      | 14/14   | ⚠️ 7/14      | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | local              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok subscription  | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | Claude subscription | 0/14    | ❌ 0/14      | —              |

Grok was re-benchmarked on September 9 on another issue of the same watch
(356 lines): 9 languages written out of 14, 8 clean. This is the figure that
appears in the main table. Three interrupted runs are not
listed: `qwen3.5-27b` (9 languages) and `kimi-k2.6` (4) due to lack of credits,
`z-ai/glm-5.3-flash` whose two failures were caused by a reasoning setting
that the provider has since corrected. The OpenRouter rows were benchmarked with
the router's default settings, prior to `--use_openrouter`; `z-ai/glm-5.2`,
retested with the shipped provider, yields the same 14/14. Numbers were
recomputed on September 10 with the current comparator: `qwen3.8-flash` and
`qwen3.7-flash` each gain one language compared to the initial
publication; the others are unchanged.

The `--use_antigravity` rows were benchmarked on September 26 on the same
article, four translations in parallel: `gemini-3.7-flash-medium` in the morning,
`gemini-3.8-flash-medium` in the afternoon. In English, each model stripped out on its own
the three lines of French translation beneath the quotes, without hallucinating a
flag, and the English quotes remained untouched: fallback cleanup had
nothing to do. In `--eco` (`gemini-3.7-flash-low`), across only four languages
(en, ja, ar, hi): 4 written out of 4, all clean, 1 min 52 s
median. Cross-validation on the same day on a more recent issue of the watch,
the September 25 edition (438 lines, 2 English quotes), translated outside the
blog by `gemini-3.7-flash-medium`: 14 written out of 14, all clean, 87 to
128 s per language.

The `--use_claude_code` rows were benchmarked on September 26 on the same
article, four translations in parallel, at effort `low`. With `sonnet`, the
English quotes remained intact across all fourteen languages, and in English, the
model stripped out the French translation lines on its own, without hallucinating a
flag. `opus` wrote no language: in each, its guardrails
aborted the response at the last segment, due to a news brief about 279 molecules
generated for a binding site. Sent on its own, this brief was rejected under
the "bio" category; `sonnet` translated it everywhere. `haiku` wrote
all fourteen languages; in three (en, pl, ro), a section heading shifted from
level 2 to level 1. It reasons without any way to prevent it — 61% of
its output tokens —, hence taking more than double the time of `sonnet`.

The `claude-sonnet-5-5`, `claude-haiku-5-5`, and `claude-haiku-4-5` rows were
benchmarked on October 18 via the Anthropic API, on the same article, four
parallel translations per model. Sonnet 5.5 refuses having its thinking
disabled: aipmt sends it the lowest setting it accepts, and its
responses contain none. It wrote all fourteen languages clean without
retrying any segment; in English, it stripped out the French translation
lines on its own, without hallucinating a flag, and the English quotes remained
intact throughout. Haiku 5.5 was tested with adaptive thinking: with thinking
disabled, it left entire paragraphs in French, which the guard rejects —
3 languages written out of 14. Both Haiku models stumbled on the same brief: Haiku 5.5
alters its heading level or duplicates it in Japanese, Korean, and
Chinese; Haiku 4.5 sets it to level 1 in seven languages, leaving it in
French in Japanese. Haiku 4.5 cost $3.67 for both documents across all
fourteen languages, Haiku 5.5 $0.57, Sonnet 5.5 $9.21.

### README of this project, standard Markdown

Revision frozen on September 9, 2026: 785 lines, 285 inline codes, 40
block fences, 89 table rows. Four translations in parallel.

| Model                                          | Written | No deviation | Median/language | What differs                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | nothing                                                                  |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | nothing                                                                  |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | nothing for the comparator; duplicate internal links (en)                |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | nothing                                                                  |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | nothing                                                                  |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | one bold word (ja)                                                       |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | one bold word (ko)                                                       |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | one table row merged with the previous one (ar)                          |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | one link (sv), one bold word (zh)                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | one bold word (ar, ja)                                                   |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | one bold word (hi, ja, ko)                                               |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 40 inline codes added in Arabic; bold (hi, ja, ko)                       |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2 languages failed (ar, hi): inline codes lost in output                 |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | one section lost (ar, hi, ko); code blocks added (ja, ko, ro, zh)        |

Two interrupted runs are not listed: Grok, CLI session timed out
after twelve languages (eleven without deviation), and `qwen3.8-flash`, HTTP 429 from its
host after two. `opencode/mimo-v2.5-free` and `ollama/gpt-oss-20b-32k`
were not remeasured on this revision; on that of September 4 and 5,
277 lines shorter, they each wrote 9 translations out of 14, including 7
and 1 without deviation.

Rows `--use_antigravity` and `--use_claude_code` were not measured on
the frozen revision, but on September 26 on the one published with 1.14.0 — and
rows `claude-sonnet-5-5`, `claude-haiku-5-5`, and `claude-haiku-4-5` on October 18,
on the same: 600 lines, 257 inline codes, 30 block fences, 85
table rows. 185
lines shorter, it cannot be compared directly row-to-row with the others;
those rows, however, can be compared among themselves. Regarding internal links, which the
comparator does not check, `gemini-3.8-flash-medium` kept them intact in
all fourteen languages, `gemini-3.7-flash-medium` broke them in Italian;
`sonnet` and `opus` kept them intact everywhere, `haiku` duplicated them in
English; `claude-sonnet-5-5` and `claude-haiku-4-5` kept them intact in
all fourteen languages, `claude-haiku-5-5` in the twelve it wrote.

### Four READMEs from well-known projects

FastAPI, Ollama, tldr-pages, and Vue.js, taken as-is from GitHub — easier
documents than the previous two. The benchmark targeted struggling models;
Gemini serves as a baseline comparison point.

| Model                     | Scope                      | Written | No deviation |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 projects × 14 languages     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 projects × 14 languages     | 55/56   | ❌ 47/56     |
| `grok-4.6` (subscription)   | 4 projects × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 projects × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### What these measurements are not

- **Not an exhaustive benchmark**: OpenRouter alone offers over four hundred
  models; around fifteen were measured.
- **Indicative durations**: three to six translations in parallel depending
  on the runs, and a provider's throughput varies throughout the day.
- **Dated observations**: models change under the same name, and your
  documents are not ours.

To rerun the measurement on your documents, on a frozen copy of the file:

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
replies `No module named aipmt`.

Quality tooling, optional but recommended:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

The repository's 28 translations (README and CHANGELOG, fourteen languages) are
regenerated with `./regen_translations.sh --force` — Codex and `gpt-6.1-sol` via the
ChatGPT subscription by default, four in parallel. `REGEN_PROVIDER` and
`REGEN_MODEL` change the path: `antigravity` stays on a subscription, Google's,
and runs without exemption; a paid API (`openai`, `gemini`,
`grok`, `openrouter`) is rejected without `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` caps each job (600 s, 1,800 s on Codex and
Antigravity). Details about the tooling can be found in `CLAUDE.md`.

## Projects using this script

- **[jls42.org](https://jls42.org)** — personal blog published in 15 languages. Its
  [daily AI watch](https://jls42.org/fr/news) is translated every day
  by this tool, and serves as the reference document for the measurements above.

## Author

Julien LE SAUX
Email: contact@jls42.org

## License

GNU GENERAL PUBLIC LICENSE Version 3. See [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Disclaimer

This program is distributed **without any warranty**, under the terms of
sections 15 and 16 of the GPL v3: provided "as is", without warranty of merchantability
or fitness for a particular purpose, and its author cannot be
held liable for any damage resulting from its use. The license text
takes precedence over this summary.

- **Proofread before publishing.** Protections cover code blocks, inline
  code, URLs, anchors, and `--news` mode blockquotes — neither
  headings, tables, front matter, nor the meaning of your sentences.
- **Your documents are sent to the chosen provider**, under its terms of
  service and data policy. Some free models may
  reuse your interactions for training, and Antigravity's terms
  allow Google to reuse them and have them reviewed by humans,
  including with a paid subscription; a local model is the only way to ensure
  no data leaves your machine.
- **API calls are billed to you.** This program does not cap
  expenses: a long document, a retry after failure, or a model that reasons
  extensively will cost more.
- **Published measurements are dated observations**, not guarantees.

Product and company names mentioned belong to their respective
holders. This project is not affiliated with any of them.

**Article translated from fr to en with gemini-3.8-flash-medium.**
