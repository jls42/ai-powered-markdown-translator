# AI-Powered Markdown Translator

🌍 [French](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Spanish](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Chinese](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [German](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japanese](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Korean](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Arabic](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italian](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Dutch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polish](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portuguese](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Romanian](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Swedish](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Code quality</h4>

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
matter. Eleven ways to call a model — five APIs, four subscriptions without
usage-based billing, two routers — and published measurements of what each
model actually preserves.

## At a glance

- **Eleven provider paths**: OpenAI, Mistral, Claude, Gemini, and Grok APIs;
  ChatGPT (Codex), Grok, Google (Antigravity), and Claude (Claude
  Code) subscriptions without usage-based billing; OpenCode routers (open source, free or local) and OpenRouter
  (over 400 models).
- **No broken output from a lost token**: code blocks, inline code,
  URLs, anchors, and quotes are replaced with tokens before the call and
  checked on return. If one is missing, the file is not written.
- **Long documents**: chunking based on the model's context window.
- **`--news` mode**: protected English quotes and language-specific
  flags, for news roundup articles.
- **`--eco` mode**: faster, cheaper models.
- Optional **translation note**, at the top, bottom, or both.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 or later. To install from the repository, see
[Contributing](#contributing).

## Configuration

Keys are read from three locations, in descending priority; each only
fills in what the previous one left empty.

|     | Where                                            | What for                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Environment variables                     | CI, containers, one-off overrides |
| 2   | `.env` in the current directory (or a parent) | a project-specific key            |
| 3   | `~/.config/aipmt/.env`                        | set up once, applies everywhere       |

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

`GEMINI_API_KEY` is accepted in place of `GOOGLE_API_KEY`. The
user file follows `XDG_CONFIG_HOME` (absolute paths only) and `%APPDATA%`
on Windows. Without a key, the command lists all three locations.

**A project's `.env` can neither redirect calls nor choose the program
to run.** It supplies keys, never a destination or a binary: any
variable ending in `_BASE_URL`, `_API_BASE`, `_ENDPOINT`, or `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, proxies (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), certificate stores (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`), and `XDG_CONFIG_HOME` /
`APPDATA` are ignored there, with a warning. A cloned repository must not
be able to hijack your key or make you run its own program on the
first translation. This file is also read without interpolation:
`NOM=${OPENAI_API_KEY}` does not copy the key into it. Set these variables in
the environment or in `~/.config/aipmt/.env`.

Optional variables: `XAI_BASE_URL` (default `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (seconds per call, default 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(default 600), `GROK_BIN`, `GROK_HOME` (default `~/.grok`), `GROK_TIMEOUT`
(default 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (default 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (default 600), `OPENROUTER_BASE_URL`
(`https://` required), `OPENROUTER_TIMEOUT` (default 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (default 30). Each is detailed in its
provider's section.

## Getting started

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` translated into Spanish produces `document-es.md` in `--target_dir`;
with `--include_model`, `document-es-gpt-5.6-terra.md`. The extension always becomes
`.md` — `article.mdx` produces `article-en.md` — except with
`--keep_filename`, which keeps the original name. An existing translation
is skipped without `--force`.

Exit codes: `0` if everything succeeded or was skipped, `1` if any file
failed (listed on standard error), `2` if configuration is the cause.
A failed file is never written, even if writing itself fails:
the content is written alongside it, then renamed. Just rerun.

## Which model to choose

Measured on two real documents, translated into the same fourteen languages by
each model. **The figure is the number of languages, out of fourteen, in which the
translation is written and nothing differs from the source.**

| Model                | How to access it                 | Dense news roundup article | This README    | What differs, and in how many languages                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google subscription (Antigravity)   | ✅ 14/14                | ✅ 14/14     | nothing, in either document                                                                                                                                 |
| **Claude Sonnet 5.5** | Anthropic API key                 | ✅ 14/14                | ✅ 14/14     | nothing, in either document                                                                                                                                 |
| **Gemini 3.7 Flash**  | Google API key                    | ✅ 14/14                | ⚠️ 13/14     | 1 language out of 14: one extra bold word (ja)                                                                                                                      |
| **Gemini 3.7 Flash**  | Google subscription (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 language out of 14: one fewer bold word (ko)                                                                                                                     |
| **GPT-5.6 Sol**       | ChatGPT subscription, or OpenAI key | ✅ 14/14                | ⚠️ 12/14     | 2 languages out of 14: one fewer bold word (ar, ja)                                                                                                                |
| **GLM-5.2**           | OpenRouter key                    | ✅ 14/14                | ⚠️ 11/14     | 3 languages out of 14: one fewer bold word (hi, ja, ko)                                                                                                            |
| Claude Sonnet 5       | Claude subscription (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 1 language out of 14 on the article: one extra bold word (zh); 1 on this README: a table row joined to the previous one, hidden when rendered (ar)            |
| Claude Haiku 4.5      | Claude subscription (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 3 languages on the article: a section heading changed to level 1 (en, pl, ro); on this README, nothing detected by the comparator, but internal links duplicated in English |
| Claude Sonnet 5       | Anthropic API key                 | ⚠️ 11/14                | ⚠️ 12/14     | 3 languages on the article: an added code block (es, de, hi); 2 on this README: a link without its markup (sv), a bold word (zh)                              |
| Claude Haiku 4.5      | Anthropic API key                 | ⚠️ 7/14                 | ✅ 14/14     | 7 languages on the article: a section heading changed to level 1 — in Japanese, left in French; nothing on this README                                              |
| Claude Haiku 5.5      | Anthropic API key                 | ⚠️ 11/14                | ❌ 12/14     | 3 languages on the article: a section heading changed level or was duplicated (ja, ko, zh); on this README, 2 languages rejected, with inline code lost (ar, hi)    |
| Qwen 3.7 Flash        | OpenRouter key                    | ❌ 8/14                 | ⚠️ 10/14     | 1 language rejected on the article, 5 others diverge; on this README, around forty words placed in `code` (ar)                                                    |
| Grok 4.6              | Grok subscription                   | ❌ 8/14                 | not scored     | 5 languages rejected out of 14 because inline code and URLs were not returned; Dutch diverges throughout                                                               |
| GPT-OSS 20B           | local model (Ollama)             | ❌ 7/14                 | not remeasured | 4 languages rejected out of 14: the model left passages in French, and the guard stopped them                                                                  |
| MiMo v2.5 (free)   | OpenCode Zen, no account         | ❌ 11/14                | not remeasured | 1 language rejected; a section lost in Polish                                                                                                                  |
| Mistral Large         | Mistral API key                   | ❌ 5/14                 | ❌ 1/14      | **an entire section disappears**: 1 language on the article (hi), 3 on this README (ar, hi, ko) — and 3 languages rejected on the article                                |
| DeepSeek V4 Flash     | OpenRouter key                    | ❌ 3/14                 | not remeasured | 10 languages rejected out of 14; 37 minutes per language                                                                                                                 |
| Claude Opus 5.5       | Claude subscription (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | the article rejected in all 14 languages by Opus's guardrails because of a short biology item; nothing on this README                                               |

|     | What the symbol means                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | all fourteen languages translated, with nothing differing from the source                                                                                                                                       |
| ⚠️  | all fourteen languages translated; the differences are **markup** — a bold word, an `code`, a link losing its brackets. No text, URLs, code blocks, or sections are missing |
| ❌  | at least one language could not be translated — the file is rejected, not written — **or** content is missing from a written file                                                                      |

What to take away:

- **A rejected translation is not a damaged translation.** When a token
  is missing from the response, the file is not written and the language counts as
  rejected. This is what happens to Grok on the article: four inline code spans and
  three URLs lost in the very first chunk, across all five non-Latin scripts.
- **A model can reject an entire document over a single sentence.** Opus 5.5
  translates this README without a single discrepancy, but no news roundup articles: its
  guardrails stop the response over a short biology item. The file is not
  written, and aipmt explains why.
- **This safety net does not cover headings, tables, front matter, or
  text.** A model that deletes a section returns a file that the tool writes
  without complaint — as happens with Mistral. These elements cannot be
  replaced with a token, and the current guards do not check them;
  `scripts/compare_structure.py` detects a lost section, but only afterward.
- **Grok has no score on this README**: its CLI session expired after twelve
  languages, eleven of them without discrepancies. An interrupted run cannot be scored.
- **Document density matters more than language.** Grok handles
  ordinary READMEs and struggles with a link-heavy article, even in
  Dutch.

Dates and documents: the “This README” column was measured on September 9, 2026
using a frozen revision of this file (785 lines, 285 inline code spans, 89 table
rows), edited since then — except for the Antigravity and Claude Code rows,
measured on September 26 using the shorter revision published with 1.14.0
(600 lines, 257 inline code spans, 85 table rows), and the Claude
Sonnet 5.5, Haiku 5.5, and Haiku 4.5 API rows, measured on October 18 using the
same revision. The “Dense news roundup article” column comes from the September
4–5 run on a 589-line article, except for the Grok row, remeasured on
September 9 using another edition of the same roundup, the Antigravity and
Claude Code rows, measured on September 26 using the same article, and those three
Claude rows, on October 18. The full tables, timings, and protocol are
in [Detailed measurements](#detailed-measurements).
## All options

| Option                   | Description                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Single Markdown file to translate (alternative to `--source_dir`)                                             |
| `--source_dir`           | Source directory containing Markdown files (default: `content/posts`)                                   |
| `--target_dir`           | Output directory for translated files (default: `traductions_en`)                                    |
| `--source_lang`          | Source language (default: `fr`)                                                                                  |
| `--target_lang`          | Target language (default: `en`)                                                                                   |
| `--model`                | Specific model to use                                                                                  |
| `--eco`                  | Use budget models                                                                              |
| `--use_mistral`          | Use the Mistral AI API                                                                                     |
| `--use_claude`           | Use the Claude API                                                                                         |
| `--use_gemini`           | Use the Gemini API                                                                                         |
| `--use_grok`             | Use the xAI (Grok) API — requires `XAI_API_KEY`                                                           |
| `--use_codex`            | Use the Codex CLI with the ChatGPT subscription quota                                                    |
| `--use_grok_cli`         | Use the Grok CLI with the Grok subscription quota                                                        |
| `--use_antigravity`      | Use the Antigravity CLI (`agy`) with the Google AI Pro or Ultra subscription quota                       |
| `--use_claude_code`      | Use the Claude Code CLI (`claude -p`) with the Claude Pro or Max subscription quota                      |
| `--use_opencode`         | Use OpenCode (open source) with the provider configured in OpenCode; requires `--model provider/modèle` |
| `--use_openrouter`       | Use OpenRouter — requires `OPENROUTER_API_KEY` and `--model fournisseur/modèle`                          |
| `--force`                | Force retranslation                                                                                       |
| `--keep_filename`        | Keep the original filename                                                                          |
| `--news`                 | News mode: protects EN quotes, manages flags by language                                      |
| `--add_translation_note` | Add a translation note                                                                                |
| `--note_position`        | Note position: `top`, `bottom` (default), or `both`                                                     |
| `--note_format`          | Note format: `legacy` (default, bold paragraph) or `marker`                                            |
| `--include_model`        | Include the model name in the output file                                                            |
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
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (also `gpt-5.6-sol`, `terra` and `luna` via `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                                           | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, effort `low`                                               | same — `--eco` has no effect |
| OpenCode    | `--model provider/modèle` required                                | same — `--eco` has no effect |
| OpenRouter  | `--model fournisseur/modèle` required                             | same — `--eco` has no effect |

### With the ChatGPT subscription: `--use_codex`

Drives the official Codex CLI: translation counts against the
ChatGPT subscription quota, with no API key or usage-based billing.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- The binary is looked up in `CODEX_BIN`, then `PATH`, then the
  `openai-codex-cli-bin` package. `~/.codex/auth.json` is never read.
- `OPENAI_API_KEY` and `CODEX_API_KEY` are removed from the subprocess
  environment: an existing key never causes a switch to the API.
- Each segment costs at least one “message” from the 5-hour window — two
  if validation fails and it is retried. OpenAI gives an
  estimate of 250-2 000 messages/5 h for `gpt-5.6-luna` (`--eco`) and
  10-100 for `gpt-5.6-sol` on a Plus plan.
- `--model gpt-5.6-sol`, the default through 1.16.3, `--model gpt-5.6-terra`
  and `--model gpt-5.6-luna` also use the subscription.
- A server 429 does not cause the file to be lost: Codex reconnects automatically,
  aipmt waits for the turn to finish, and if the 429 persists, the segment
  is retried after 30 and then 60 seconds. A model the account cannot access returns a 400 “model is
  not supported when using Codex with a ChatGPT account”.
- Slower than an API, with the gap growing with document length: on this README,
  a median of 6 min 46 s per language with `gpt-5.6-sol`, versus 36 s for
  `gemini-3.7-flash`.
- Rejected in CI (`CI` or `GITHUB_ACTIONS` set): the subscription authenticates
  through a personal session file, which does not belong on a shared
  runner.
- Variables: `CODEX_BIN`, `CODEX_TIMEOUT` (seconds per segment, default 600).

### With the Grok subscription: `--use_grok_cli`

The same principle with the official Grok Build CLI, using the SuperGrok or
X Premium+ subscription.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Weaker confinement than Codex.** Grok's OS sandbox does not apply
  on many recent Linux machines (AppArmor, container runtime
  sockets), and a profile that cannot be applied silently starts without
  confinement. The script therefore requests no profile by default, announces this, and
  relies on the CLI's `--deny` rules, including the `*` catch-all — the only
  layer that refuses to start rather than silently removing
  protection. `GROK_TRANSLATE_SANDBOX=read-only` requires the OS sandbox, and startup
  fails if the machine cannot provide it.
- The quota is weekly, shared with Chat, Imagine and Voice, and no
  command can read it: a batch can eat into conversational usage
  without any indication.
- Variables: `GROK_BIN`, `GROK_HOME` (CLI directory, default `~/.grok`),
  `GROK_TIMEOUT` (default 900), `GROK_TRANSLATE_SANDBOX`.

### With the Google subscription: `--use_antigravity`

The same principle with `agy`, the official Antigravity CLI: for Google
AI Pro or Ultra subscribers, translation counts against the subscription quota instead
of being billed per token. This is the only route to this quota: Gemini CLI has
no longer served these accounts since June 18, 2026
([announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
and the Antigravity SDK only accepts an API key or a Google Cloud project.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **No paid route remains open.** agy receives only an allowlist of variables
  from your environment — `PATH`, language and timezone,
  terminal, identity, proxies and certificates, session bus — and no keys:
  several of its variables silently redirect a call (measured:
  one sends the document to a third-party gateway, another to a billed
  Google Cloud project), and a denylist missed some on every review.
  Before any segment, `agy -p /config`, which uses no quota, must show
  paid AI credits disabled, with no API key or Google Cloud project — a
  missing setting means rejection — otherwise nothing is translated; the log for each
  call must then confirm subscription use (`authMethod=consumer`), otherwise the
  response is rejected.
- **Confinement.** Each call runs in a private, disposable home
  directory, with a translation agent that has no tools: your agy settings, rules,
  plugins, MCP servers and hooks do not enter it, nothing is added to your
  history, and the login stays in the keyring, which aipmt never reads.
  A missing agent makes agy silently fall back to its coding agent
  and tools: a full log line must confirm the correct agent — a
  document quoting this message does not count — otherwise the call is rejected.
- **Platforms**: Linux, in a session with a keyring (D-Bus session
  bus, Secret Service); macOS is accepted, without having been measured there. Rejected
  on Windows, where agy does not read the variables that isolate each call, and
  on Linux without a session bus — SSH session, container, server: agy
  stores its token in a file under `~/.gemini`, which isolation hides. The
  rejection happens before any launch, with its reason, instead of a minute
  spent waiting for a login code.
- **Models**: those from `agy models`. Gemini models include the effort in their names
  (`gemini-3.8-flash-medium`…): a name without a suffix is rejected before the call,
  and `--reasoning_effort` has no effect. The default is `gemini-3.8-flash-medium`,
  and `gemini-3.7-flash-low` with `--eco`; the campaigns used to select them are
  described in [Detailed measurements](#detailed-measurements). Claude and GPT-OSS
  have their own, much smaller quota: around 1 % of the
  5-hour window per measured call, versus 0,05 % with Flash.
- **Quota**: per group, a 5-hour window and a weekly window,
  proportional to token cost. Measured on the author's account: around
  16 points of the 5-hour window per million source characters with
  `gemini-3.8-flash-medium`, 14 with `gemini-3.7-flash-medium` and 7 to 8 at
  low effort — a 40 000-character README therefore costs just over
  half a point. The weekly limit depends on the tier. Retries follow
  what agy declares retryable; otherwise, an exhausted window is never
  retried: it causes every file to fail until the reset
  shown by `/usage`.
- **Slower than the API**: on the dense article used for measurements, a median of 3 min 59 s per
  language with `gemini-3.8-flash-medium` and 3 min 14 s with
  `gemini-3.7-flash-medium`, versus 1 min 18 s for Gemini 3.7 Flash via the API.
- **Interruption**: Ctrl-C, or closing a terminal, stops agy along with the
  command instead of letting it finish its turn using your quota; the same applies to
  Codex, Grok CLI and OpenCode. Under `nohup`, translation continues.
- Rejected in CI (`CI` or `GITHUB_ACTIONS` set): the login lives in a
  personal keyring. On a runner, use `--use_gemini` with `GOOGLE_API_KEY`.
- Variables: `AGY_BIN` (otherwise `PATH`, then `~/.local/bin/agy`),
  `AGY_TIMEOUT` (seconds per segment, including startup, default 900).

**Terms of use: your account is at stake.** The
[Antigravity terms](https://antigravity.google/terms) (section 6) and its
[FAQ](https://antigravity.google/docs/faq/) prohibit accessing the service
through third-party software using the Antigravity login — Claude Code,
OpenClaw and OpenCode are named — under penalty of account suspension. aipmt
neither reads nor reuses the token: it launches the official binary in the
[headless mode](https://antigravity.google/docs/cli/headless/) that Google
documents for scripts and CI. A Google member described launching `agy -p`
from a local script for one's own work as “standard”
([official forum, September 25, 2026, non-binding response](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
no text settles the case of a distributed tool like this one.

**Public documents only.** Under section 5 of the same terms,
exchanges — prompts, responses, metadata — may be used to improve
Google's products and machine learning and be reviewed by
humans, including with a paid subscription. Opting out requires the
`enableTelemetry` setting, whose effect is undocumented and which aipmt does not set; your agy
settings do not carry over into its isolated environment. Do not send anything confidential through it.
### With a Claude subscription: `--use_claude_code`

The same principle applies to `claude`, the official Claude Code CLI, in `-p` mode: for
Claude Pro or Max subscribers, translation counts against the
subscription quota instead of being billed per token. Not to be confused with
`--use_claude`, Anthropic's API, billed by usage.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **No paid route remains open, and every call proves it.** Claude
  Code receives only a fixed list of variables from your environment — no
  API key, token, cloud provider, or marker of the Claude Code session
  from which aipmt might be launched. Before the first segment, `claude auth status` must
  show the subscription login, without a Console key, and `/usage`, which consumes
  no quota, must confirm it; each call confirms it in turn in its
  initialization event, otherwise the response is rejected.
- **Disable “extra usage”** (claude.ai, Settings → Usage) to
  keep the cost at zero euros: when enabled, it takes over once a usage window is exhausted and
  bills without displaying an error. aipmt stops translating as soon as a call's
  quota report indicates this, but that call has already been counted.
- **Quota shared with your Claude Code sessions.** Each call reports
  usage for the 5-hour and weekly windows; above 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`), no further segments are launched, to avoid
  exhausting what you need for your work.
- **Isolation.** Each call runs without tools, in a private,
  disposable directory, with customization disabled: neither your `CLAUDE.md` nor your plugins,
  hooks, MCP servers, or settings are loaded, and nothing from the
  session is retained. Attachments are disabled: an `@chemin` in your document
  remains text and opens no files (verified by measurement).
- **Models**: `sonnet` by default, at `low` effort, including in `--eco`:
  `--eco` has no effect on this route. Measured on the same documents, `haiku`
  is twice as slow — it reasons with no way to prevent it — for
  barely any cost savings, and `opus` refuses biology content (next
  point). Both remain accessible through `--model`; these aliases track the
  latest model in their family. `fable` and `[1m]` variants are rejected,
  because they use paid credits. `--reasoning_effort` sets the effort,
  which offers no benefit for translation: measured reasoning is zero or nearly so.
- **Opus refuses some biology content.** Its safeguards are
  stricter than Sonnet's, and Anthropic's error message warns that they
  “can sometimes flag biology-research-adjacent work”. Measured result: a news
  brief about 279 generated molecules caused the article to be refused in all fourteen
  languages. Nothing is written: aipmt rejects the interrupted response, identifies the
  safeguards, and recommends `--model sonnet`.
- Rejected in CI (`CI` or `GITHUB_ACTIONS` set) and on Windows (not measured).
- Variables: `AIPMT_CLAUDE_BIN` (otherwise `PATH`, then `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (seconds per segment, default 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (default 0.8), `CLAUDE_CONFIG_DIR` (the
  Claude Code account, never taken from a project's `.env`); working directories under
  `XDG_CACHE_HOME/aipmt/claude-code` (default `~/.cache`).

**Terms of use: your account is on the line.** The
[Claude Code legal page](https://code.claude.com/docs/en/legal-and-compliance)
does not prevent “an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription”: that is what aipmt does, launching the
official binary and never reading the token. But Anthropic “does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users”, prefers API keys for third-party
tools, “including open-source projects”, and reserves the right to charge their
usage against paid credits
([Claude help](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
No text settles the case of a distributed tool that launches the binary.

**Data**: on Free, Pro, and Max accounts, model training
also applies to Claude Code when the privacy setting allows it
([data page](https://code.claude.com/docs/en/data-usage)). aipmt retains
no local transcript (`--no-session-persistence`). Do not send
anything confidential through it.

### To the provider of your choice: `--use_opencode`

[OpenCode](https://opencode.ai) is an open source coding agent (MIT) that
routes to providers configured within it: API key, subscription,
OpenCode Zen gateway (free models, no account), or local model. Two
routes were measured end to end here, Zen and Ollama.

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
whose exchanges may be used for training, and that choice is not made
on your behalf.

Isolation on every call:

- an inline configuration, which takes precedence over yours, defines an `aipmt` agent
  with all tools denied (`permission: { "*": "deny" }`), session
  sharing disabled, `--pure`, never `--auto`;
- an empty, disposable working directory, with `OPENCODE_DISABLE_PROJECT_CONFIG` and
  `OPENCODE_DISABLE_CLAUDE_CODE` set — without them, OpenCode injects the current
  directory's `AGENTS.md` and `~/.claude/CLAUDE.md` into the prompt. The
  global `~/.config/opencode/AGENTS.md` is still injected; OpenCode provides no way
  to exclude it;
- output contract: exit code 0, no `error` event, no
  tool calls, final step in `stop`, nonempty text, and the `aipmt` agent
  actually loaded — an unknown `--agent` does not cause OpenCode to fail;
  it silently falls back to the coding agent;
- no `aipmt` key is passed through, except `OPENCODE_API_KEY`, OpenCode's
  own key. Providers are configured in OpenCode, not in
  `aipmt`'s `.env`.

Things to know:

- Zen's free models change, have undocumented limits, and
  their exchanges may be used for training: suitable for public
  documentation, not private content.
- A local model must provide at least 16 k tokens of context, as segments
  can contain up to 16 000 characters. Ollama often configures 4 096: use
  a `Modelfile` with `PARAMETER num_ctx 32768`.
- `--eco` has no effect; `--reasoning_effort` is passed through unchanged as
  OpenCode's `--variant`.
- OpenCode logs every session in `~/.local/share/opencode/`.
- Variables: `OPENCODE_BIN` (otherwise `PATH`, then `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (seconds per segment, default 600). `OPENCODE_CONFIG`
  is passed through unchanged to OpenCode.

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
models, which a Modelfile cannot disable. Measured on a
six-word sentence: 919 thinking tokens and 68 seconds without the option, 9 tokens with it.

### To more than 400 models: `--use_openrouter`

OpenRouter is a router billed by usage, drawing from a single credit balance, for
models hosted by third parties — including open Chinese models that no
other provider exposes here.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` is required. A preflight check, run before any billing, handles
two routing peculiarities:

- **The same model is served by dozens of hosts with different
  limits** — for `z-ai/glm-5.3-flash`, 23 hosts, including one capped at
  2 048 output tokens. The preflight reads `/api/v1/models/{modèle}/endpoints`,
  excludes hosts below 8 000 output tokens or with degraded status, and
  pins the others with `allow_fallbacks: false`.
- **Reasoning is billed at the output rate** — 107 tokens versus 2 for
  an “OK” response from `z-ai/glm-5.2`. It is disabled by default; models
  that require it receive the lowest effort they accept, as the catalog's
  default can exhaust the output budget before the translation ends.
  `--reasoning_effort` still takes precedence.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- The context window comes from the catalog. A model below 16 400 tokens is
  rejected before any call: 8 400 for the prompt and segment, at least 8 000
  for output.
- A slug missing from the catalog, an unreachable catalog, or the absence
  of a host meeting the limit stops the command.
- `finish_reason=length` with empty output means the budget was consumed by
  reasoning, rather than truncation: the message makes the distinction.
- `--eco` has no effect.
- Variables: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (default `https://openrouter.ai/api/v1`, `https://`
  required), `OPENROUTER_TIMEOUT` (default 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (default 30).

### Translation note

`--add_translation_note` adds a note, at `bottom` (default), `top` (after the
front matter), or `both` (`--note_position`), in `legacy` format (bold
paragraph, default) or `marker` (`--note_format`). The `marker` format is an
invisible Markdown reference definition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
followed by a bold quotation: readable on GitHub and usable at build time by a
remark plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detailed measurements

All measurements are translations actually run with `aipmt`, into
fourteen languages: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Written** counts files accepted by the guards; **No
differences** counts those where `scripts/compare_structure.py` detects nothing — the same number of
sections, subheadings, links, distinct URLs, code blocks,
inline code spans, table rows, blockquotes, and bold words.

“No differences” means “nothing detected”, not “identical”: the comparator
counts elements without reading their content. It does not flag a deleted
level 4 heading, replaced inline code text, a swapped
flag, or an internal link rendered with an extra parenthesis,
`[texte]((#ancre))`, that no longer leads anywhere — and it does not assess the
language.

### Dense news roundup article, `--news` mode

An edition of the [jls42.org AI news roundup](https://jls42.org/fr/news):
589 lines, 140 links, 21 sections, 3 protected English quotations. Test campaign
on September 4 and 5, 2026.

| Model                                          | Access              | Written | No differences   | Median/language |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google subscription  | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google subscription  | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `claude-sonnet-5-5`                             | Anthropic API      | 14/14   | ✅ **14/14** | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT subscription | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | Claude subscription  | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | Claude subscription  | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `claude-haiku-5-5`                              | Anthropic API      | 14/14   | ⚠️ 11/14     | 2 min 54 s     |
| `claude-haiku-4-5`                              | Anthropic API      | 14/14   | ⚠️ 7/14      | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | local              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok subscription    | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | Claude subscription  | 0/14    | ❌ 0/14      | —              |

Grok was measured again on September 9 using another edition of the same roundup
(356 lines): 9 languages written out of 14, 8 with no differences. That is the figure
shown in the opening table. Three interrupted test campaigns are not
listed: `qwen3.5-27b` (9 languages) and `kimi-k2.6` (4) due to insufficient credit,
and `z-ai/glm-5.3-flash`, whose two failures came from a reasoning setting
that the provider has since corrected. The OpenRouter rows were measured with
the router's default settings, before `--use_openrouter`; `z-ai/glm-5.2`,
measured again with the shipped provider, returns the same 14/14. The figures were
recalculated on September 10 with the current comparator: `qwen3.8-flash` and
`qwen3.7-flash` each gain one language compared with the initial
publication; the others are unchanged.

The `--use_antigravity` rows were measured on September 26 using the same
article, with four translations in parallel: `gemini-3.7-flash-medium` in the morning,
`gemini-3.8-flash-medium` in the afternoon. In English, each removed
the three French translation lines beneath the quotations on its own, without inventing a
flag, and the English quotations remain intact: fallback cleanup had
nothing to do. In `--eco` (`gemini-3.7-flash-low`), for just four languages
(en, ja, ar, hi): 4 written out of 4, all with no differences, with a median of
1 min 52 s. A cross-check that same day used a more recent edition of the roundup,
dated September 25 (438 lines, 2 English quotations), translated outside the
blog by `gemini-3.7-flash-medium`: 14 written out of 14, all with no differences, 87 to
128 s per language.

The `--use_claude_code` rows were measured on September 26 using the same
article, with four translations in parallel, at `low` effort. With `sonnet`, the
English quotations remain intact in all fourteen languages and, in English, the
model removed the French translation lines on its own, without inventing a
flag. `opus` wrote no languages: in each one, its safeguards
stopped the response at the final segment because of a brief about 279 molecules
generated for a binding site. Sent alone, this brief is rejected
under the “bio” category; `sonnet` translated it in every language. `haiku` writes
all fourteen languages; in three (en, pl, ro), a section heading changes from
level 2 to level 1. It reasons with no way to prevent it — 61 % of
its output tokens — resulting in more than twice the time taken by `sonnet`.

The `claude-sonnet-5-5`, `claude-haiku-5-5`, and `claude-haiku-4-5` rows were
measured on October 18 through Anthropic's API, using the same article, with four
translations in parallel per model. Sonnet 5.5 refuses to have its
thinking disabled: aipmt sends it the lowest setting it accepts, and its
responses contain none. It writes all fourteen languages with no differences and without
retrying a segment; in English, it removed the French translation
lines on its own, without inventing a flag, and the English quotations remain
intact everywhere. Haiku 5.5 is measured with adaptive thinking: with thinking
disabled, it left entire paragraphs in French, which the guard rejects —
3 languages written out of 14. Both Haiku models stumble on the same brief: Haiku 5.5
changes its heading level or duplicates it in Japanese, Korean, and
Chinese; Haiku 4.5 changes it to level 1 in seven languages and leaves it
in French in Japanese. Haiku 4.5 costs $3.67 for both documents in all
fourteen languages, Haiku 5.5 $0.57, and Sonnet 5.5 $9.21.
### This project's README, standard Markdown

Revision frozen on September 9, 2026: 785 lines, 285 inline code spans, 40
block fences, 89 table rows. Four translations in parallel.

| Model                                          | Written | No discrepancies | Median/language | What differs                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | nothing                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | nothing                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | nothing detected by the comparator; duplicated internal links (en)                   |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | nothing                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | nothing                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | one bold word (ja)                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | one bold word (ko)                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | one table row joined to the previous one (ar)                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | one link (sv), one bold word (zh)                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | one bold word (ar, ja)                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | one bold word (hi, ja, ko)                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 40 inline code spans added in Arabic; bold (hi, ja, ko)                   |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2 languages rejected (ar, hi): inline code spans lost in the returned output        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | one section lost (ar, hi, ko); code blocks added (ja, ko, ro, zh) |

Two interrupted runs are not scored: Grok, whose CLI session expired
after twelve languages (eleven with no discrepancies), and `qwen3.8-flash`, which received HTTP 429 from its
hosting provider after two. `opencode/mimo-v2.5-free` and `ollama/gpt-oss-20b-32k`
were not measured again on this revision; on the September 4 and 5 revision,
which was 277 lines shorter, each wrote 9 translations out of 14, with 7
and 1 showing no discrepancies, respectively.

The `--use_antigravity` and `--use_claude_code` rows were not measured on
the frozen revision, but on September 26 using the one published with 1.14.0 — and
the `claude-sonnet-5-5`, `claude-haiku-5-5` and `claude-haiku-4-5` rows on October 18,
using that same revision: 600 lines, 257 inline code spans, 30 block fences, 85
table rows. At
185 lines shorter, it cannot be compared directly with the other rows;
these rows can, however, be compared with each other. As for internal links, which the
comparator does not check, `gemini-3.8-flash-medium` kept them intact in
all fourteen languages, while `gemini-3.7-flash-medium` broke them in Italian;
`sonnet` and `opus` kept them intact everywhere, while `haiku` duplicated them in
English; `claude-sonnet-5-5` and `claude-haiku-4-5` kept them intact in
all fourteen languages, and `claude-haiku-5-5` in the twelve it wrote.

### Four READMEs from well-known projects

FastAPI, Ollama, tldr-pages and Vue.js, taken as-is from GitHub —
documents that are easier than the previous two. The run targeted models
that struggled; Gemini serves as a point of comparison.

| Model                    | Scope                  | Written | No discrepancies   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 projects × 14 languages     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 projects × 14 languages     | 55/56   | ❌ 47/56     |
| `grok-4.6` (subscription)   | 4 projects × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 projects × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### What these measurements are not

- **Not an exhaustive ranking**: OpenRouter alone offers over four hundred
  models; around fifteen were measured.
- **Indicative durations**: three to six translations in parallel depending on
  the run, and a provider's throughput varies throughout the day.
- **Dated observations**: models change under the same name, and your
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
responds with `No module named aipmt`.

Quality tooling, optional but recommended:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

The repository's 28 translations (README and CHANGELOG, fourteen languages) are
regenerated with `./regen_translations.sh --force` — Codex and `gpt-6.1-sol` using
the ChatGPT subscription by default, four in parallel. `REGEN_PROVIDER` and
`REGEN_MODEL` change the route: `antigravity` still uses a subscription,
Google's, and is allowed without an override; a billed API (`openai`, `gemini`,
`grok`, `openrouter`) is rejected without `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` caps each job (600 s, 1 800 s on Codex and
Antigravity). Tooling details are in `CLAUDE.md`.

## Projects using this script

- **[jls42.org](https://jls42.org)** — a personal blog published in 15 languages. Its
  [daily AI news roundup](https://jls42.org/fr/news) is translated every day
  by this tool and serves as a reference document for the measurements above.

## Author

Julien LE SAUX
Email: contact@jls42.org

## License

GNU GENERAL PUBLIC LICENSE Version 3. See [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Disclaimer

This program is distributed **without any warranty**, under the terms of
sections 15 and 16 of the GPL v3: provided “as is,” without any warranty of
merchantability or fitness for a particular purpose, and its author cannot be
held liable for damage resulting from its use. The license text
takes precedence over this summary.

- **Review before publishing.** The safeguards cover code blocks,
  inline code, URLs, anchors and quotations in `--news` mode — they do not cover
  headings, tables, front matter or the meaning of your sentences.
- **Your documents are sent to the chosen provider**, under its terms
  of use and data policy. Some free models may
  reuse your conversations for training, and Antigravity's terms
  allow Google to reuse them and have humans review them,
  even with a paid subscription; a local model is the only option that keeps
  all data on your machine.
- **You are billed for API calls.** This program does not cap
  spending: a long document, a retry after a failure or a model that reasons
  extensively costs more.
- **The published measurements are dated observations**, not guarantees.

The product and company names mentioned belong to their respective
owners. This project is not affiliated with any of them.

**Article translated from fr to en with gpt-6.1-sol.**
