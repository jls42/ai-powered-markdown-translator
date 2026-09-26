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

Translates Markdown files from one language to another while preserving
structure: code blocks, inline code, URLs, anchors, tables, and front
matter. Eleven ways to call a model — five APIs, four subscriptions without
pay-per-use billing, two routers — and a published benchmark of what each
model actually preserves.

## At a Glance

- **Eleven provider paths**: OpenAI, Mistral, Claude, Gemini, and Grok APIs;
  ChatGPT (Codex), Grok, Google (Antigravity), and Claude (Claude
  Code) subscriptions without pay-per-use billing; OpenCode (open source, free or local) and OpenRouter
  (over 400 models) routers.
- **No corruption from a lost token**: code blocks, inline code,
  URLs, anchors, and blockquotes are replaced with tokens before the call and
  verified upon return. If one is missing, the file is not written.
- **Long documents**: chunking according to the model's window.
- **`--news` mode**: protected English quotes and flags handled per
  language, for tech watch digests.
- **`--eco` mode**: fast and cheaper models.
- **Optional translation note**, at the top, bottom, or both.

## Installation

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 or newer. To install from the repository, see
[Contributing](#contributing).

## Configuration

Keys are read from three locations, in order of priority; each only
fills what the previous leaves empty.

|     | Where                                         | What for                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Environment variables                         | CI, containers, one-off overrides     |
| 2   | `.env` in the current (or parent) directory | project-specific key                  |
| 3   | `~/.config/aipmt/.env`                        | installed once, applies everywhere    |

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

`GEMINI_API_KEY` is accepted in place of `GOOGLE_API_KEY`. The user
file follows `XDG_CONFIG_HOME` (absolute path only) and `%APPDATA%`
on Windows. Without a key, the command lists all three locations.

**A project's `.env` can neither redirect calls nor choose the executed
program.** It provides keys, never a destination or a binary: any
variable in `_BASE_URL`, `_API_BASE`, `_ENDPOINT`, or `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, proxies (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), certificate stores (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`), and `XDG_CONFIG_HOME` /
`APPDATA` are ignored with a warning. A cloned repository should not
be able to hijack your key or make you run its own program on the
first translation. This file is also read without interpolation:
`NOM=${OPENAI_API_KEY}` does not copy the key there. Set these variables in
the environment or in `~/.config/aipmt/.env`.

Optional variables: `XAI_BASE_URL` (default `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (seconds per call, default 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(default 600), `GROK_BIN`, `GROK_HOME` (default `~/.grok`), `GROK_TIMEOUT`
(default 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (default 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (default 600), `OPENROUTER_BASE_URL`
(`https://` required), `OPENROUTER_TIMEOUT` (default 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (default 30). Each is detailed in its
provider's section.

## Getting Started

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` translated to Spanish produces `document-es.md` in `--target_dir`;
with `--include_model`, `document-es-gpt-5.6-terra.md`. The extension always
becomes `.md` — `article.mdx` becomes `article-en.md` — except with
`--keep_filename`, which preserves the original name. An existing translation
is skipped without `--force`.

Exit codes: `0` if everything succeeded or was skipped, `1` if any file
failed (listed on stderr), `2` if configuration is at fault.
A failed file is never written, even if writing itself fails:
content is written alongside and then renamed. Rerunning is enough.

## Which Model to Choose

Measured on two real documents, translated into the same fourteen languages by
each model. **The number is the count of languages, out of fourteen, where the
translation is written and nothing differs from the source.**

| Model                | How to access it                  | Dense tech watch digest | This README  | What differs, and across how many languages                                                                                                                        |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash** | Google subscription (Antigravity) | ✅ 14/14                | ✅ 14/14     | nothing, on neither document                                                                                                                                       |
| **Gemini 3.7 Flash** | Google API key                    | ✅ 14/14                | ⚠️ 13/14     | 1 language out of 14: one extra bold word (ja)                                                                                                                     |
| **Gemini 3.7 Flash** | Google subscription (Antigravity) | ✅ 14/14                | ⚠️ 13/14     | 1 language out of 14: one fewer bold word (ko)                                                                                                                     |
| **GPT-5.6 Sol**      | ChatGPT subscription, or OpenAI key | ✅ 14/14              | ⚠️ 12/14     | 2 languages out of 14: one fewer bold word (ar, ja)                                                                                                                |
| **GLM-5.2**          | OpenRouter key                    | ✅ 14/14                | ⚠️ 11/14     | 3 languages out of 14: one fewer bold word (hi, ja, ko)                                                                                                            |
| Claude Sonnet 5      | Claude subscription (Claude Code) | ⚠️ 13/14                | ⚠️ 13/14     | 1 language out of 14 on the digest: one extra bold word (zh); 1 on this README: a table row stuck to the previous one, hidden from display (ar)                     |
| Claude Haiku 4.5     | Claude subscription (Claude Code) | ⚠️ 11/14                | ✅ 14/14     | 3 languages on the digest: a section heading turned into level 1 (en, pl, ro); on this README, nothing for the comparator, but internal links duplicated in English |
| Claude Sonnet 5      | Anthropic API key                 | ⚠️ 11/14                | ⚠️ 12/14     | 3 languages on the digest: an extra code block appeared (es, de, hi); 2 on this README: a link missing its markup (sv), one bold word (zh)                        |
| Qwen 3.7 Flash       | OpenRouter key                    | ❌ 8/14                 | ⚠️ 10/14     | 1 language rejected on the digest, 5 others deviate; on this README, about forty words wrapped in `code` (ar)                                              |
| Grok 4.6             | Grok subscription                 | ❌ 8/14                 | unrated      | 5 languages rejected out of 14, due to missing inline code and URLs; Dutch diverges completely                                                                     |
| GPT-OSS 20B          | local model (Ollama)              | ❌ 7/14                 | not re-measured | 4 languages rejected out of 14: the model left passages in French, safety guards caught them                                                                      |
| MiMo v2.5 (free)     | OpenCode Zen, without account     | ❌ 11/14                | not re-measured | 1 language rejected; one section lost in Polish                                                                                                                    |
| Mistral Large        | Mistral API key                   | ❌ 5/14                 | ❌ 1/14      | **an entire section disappears**: 1 language on the digest (hi), 3 on this README (ar, hi, ko) — and 3 languages rejected on the digest                             |
| DeepSeek V4 Flash    | OpenRouter key                    | ❌ 3/14                 | not re-measured | 10 languages rejected out of 14; 37 minutes per language                                                                                                          |
| Claude Opus 5.5      | Claude subscription (Claude Code) | ❌ 0/14                 | ✅ 14/14     | digest rejected in all 14 languages by Opus safety guardrails, because of a short biology blurb; nothing on this README                                            |

|     | What the symbol means                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | all fourteen languages translated, and nothing differs from the source                                                                                                                                |
| ⚠️  | all fourteen languages translated; what differs is **markup** — a bold word, an `code`, a link losing its brackets. No text, no URL, no code block, no section is missing                    |
| ❌  | at least one language could not be translated — the file is rejected, not written — **or** content is missing in a written file                                                                      |

Key takeaways:

- **A rejected translation is not a corrupted translation.** When a token
  is missing upon return, the file is not written and the language counts as
  rejected. This is what happens to Grok on the digest: four inline codes and
  three URLs lost in the very first chunk across the five non-Latin scripts.
- **A model can reject an entire document over a single sentence.** Opus 5.5
  translates this README without a single flaw, but fails completely on tech watch digests: its
  guardrails halt the response over a short biology item. The file is not
  written, and aipmt explains why.
- **This safety net does not cover headings, tables, front matter, or
  prose.** A model that drops a section returns a file that the tool writes
  without hesitation — this is the case with Mistral. These elements cannot be
  replaced by tokens, and current guards do not check them;
  `scripts/compare_structure.py` detects a lost section, but only after the fact.
- **Grok has no rating on this README**: its CLI session expired after twelve
  languages, eleven of which had no discrepancies. An interrupted run receives no rating.
- **Document density matters more than language.** Grok holds up on
  ordinary READMEs but stumbles on a link-heavy digest, even in
  Dutch.

Dates and documents: the "This README" column was measured on September 9, 2026
on a frozen revision of this file (785 lines, 285 inline codes, 89 table rows),
tweaked since — except for the Antigravity and Claude Code rows,
measured on September 26 on the revision published with 1.14.0, which is shorter
(600 lines, 257 inline codes, 85 table rows). The "Dense tech watch
digest" column comes from the September 4–5 benchmark run on a 589-line
article, except for the Grok row, remeasured on September 9 on another edition of the
same digest, and the Antigravity and Claude Code rows, measured on September 26
on the same article. Full tables, durations, and protocol can be found in
[Detailed benchmarks](#detailed-measurements).

## All options

| Option                   | Description                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Single Markdown file to translate (alternative to `--source_dir`)                                             |
| `--source_dir`           | Source directory containing Markdown files (default: `content/posts`)                                          |
| `--target_dir`           | Output directory for translated files (default: `traductions_en`)                                               |
| `--source_lang`          | Source language (default: `fr`)                                                                     |
| `--target_lang`          | Target language (default: `en`)                                                                     |
| `--model`                | Specific model to use                                                                                         |
| `--eco`                  | Use budget models                                                                                             |
| `--use_mistral`          | Use the Mistral AI API                                                                                        |
| `--use_claude`           | Use the Claude API                                                                                            |
| `--use_gemini`           | Use the Gemini API                                                                                            |
| `--use_grok`             | Use the xAI (Grok) API — requires `XAI_API_KEY`                                                              |
| `--use_codex`            | Use the Codex CLI via the ChatGPT subscription quota                                                          |
| `--use_grok_cli`         | Use the Grok CLI via the Grok subscription quota                                                              |
| `--use_antigravity`      | Use the Antigravity CLI (`agy`) via the Google AI Pro or Ultra subscription quota                    |
| `--use_claude_code`      | Use the Claude Code CLI (`claude -p`) via the Claude Pro or Max subscription quota                         |
| `--use_opencode`         | Use OpenCode (open source) with the provider configured in OpenCode; requires `--model provider/modèle`                 |
| `--use_openrouter`       | Use OpenRouter — requires `OPENROUTER_API_KEY` and `--model fournisseur/modèle`                                                   |
| `--force`                | Force re-translation                                                                                          |
| `--keep_filename`        | Preserve original file name                                                                                   |
| `--news`                 | News mode: protects EN quotes, handles flags by language                                                      |
| `--add_translation_note` | Add a translation note                                                                                        |
| `--note_position`        | Note position: `top`, `bottom` (default), or `both`                                    |
| `--note_format`          | Note format: `legacy` (default, bold paragraph) or `marker`                                   |
| `--include_model`        | Include model name in output file                                                                             |
| `--reasoning_effort`     | GPT-5.x reasoning effort: `none`/`low`/`medium`/`high`/`xhigh`   |

The nine `--use_*` flags are mutually exclusive: combining two of them is
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

| Provider    | Quality (default)                                     | Budget (`--eco`)          |
| ----------- | ----------------------------------------------------- | --------------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`                   |
| Claude      | `claude-sonnet-5`                                       | `claude-haiku-4-5`                   |
| Mistral     | `mistral-large-latest`                                       | `mistral-small-latest`                   |
| Gemini      | `gemini-3.7-flash`                                       | `gemini-3.1-flash-lite`                   |
| Codex       | `gpt-5.6-sol` (also `terra` and `luna` via `--model`) | `gpt-5.6-luna`                   |
| Grok API    | `grok-4.6`                                       | `grok-4.3`                   |
| Grok CLI    | `grok-4.6`                                       | `grok-4.5`                   |
| Antigravity | `gemini-3.8-flash-medium`                                       | `gemini-3.7-flash-low`                   |
| Claude Code | `sonnet`, effort `low`               | same — `--eco` has no effect |
| OpenCode    | `--model provider/modèle` required                              | same — `--eco` has no effect |
| OpenRouter  | `--model fournisseur/modèle` required                              | same — `--eco` has no effect |

### On the ChatGPT subscription: `--use_codex`

Drives the official Codex CLI: translation is deducted from the ChatGPT
subscription quota, with no API key or usage-based billing.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- The binary is looked up in `CODEX_BIN`, then `PATH`, then the `openai-codex-cli-bin`
  package. `~/.codex/auth.json` is never read.
- `OPENAI_API_KEY` and `CODEX_API_KEY` are removed from the subprocess
  environment: an existing key never triggers a switch to the API.
- Each segment costs at least one “message” from the 5-hour window — two
  if its validation fails and it is retried. As an estimate, OpenAI
  advertises 250–2,000 messages/5 h for `gpt-5.6-luna` (`--eco`) and
  10–100 for `gpt-5.6-sol` on a Plus plan.
- `--model gpt-5.6-terra` and `--model gpt-5.6-luna` also go through the
  subscription. A model the account is not entitled to returns a 400 “model is
  not supported when using Codex with a ChatGPT account”.
- Slower than an API, and the gap widens with document size: on this README,
  a median of 6 min 46 s per language with `gpt-5.6-sol`, compared to 36 s for
  `gemini-3.7-flash`.
- Rejected in CI (`CI` or `GITHUB_ACTIONS` set): the subscription authenticates
  via a personal session file, which has no place on a shared runner.
- Variables: `CODEX_BIN`, `CODEX_TIMEOUT` (seconds per segment, default 600).

### On the Grok subscription: `--use_grok_cli`

Same principle with the official Grok Build CLI, on the SuperGrok or
X Premium+ subscription.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Weaker sandboxing than Codex.** Grok's OS sandbox does not apply
  on many recent Linux machines (AppArmor, container runtime sockets), and a
  profile that cannot be applied silently starts unconfined. The script therefore
  does not request any profile by default, announces it, and relies on the CLI's
  `--deny` rules, including the `*` catch-all — the only layer
  that refuses to start rather than silently removing protection.
  `GROK_TRANSLATE_SANDBOX=read-only` enforces the OS sandbox, and startup fails if the machine
  cannot honor it.
- The quota is weekly, shared with Chat, Imagine, and Voice, and no command
  allows checking it: a batch can eat into conversational usage without
  warning.
- Variables: `GROK_BIN`, `GROK_HOME` (CLI directory, default `~/.grok`),
  `GROK_TIMEOUT` (default 900), `GROK_TRANSLATE_SANDBOX`.

### On the Google subscription: `--use_antigravity`

Same principle with `agy`, the official Antigravity CLI: for those paying
for Google AI Pro or Ultra, translation is deducted from the subscription quota
instead of being billed per token. This is the only path to this quota: Gemini CLI
no longer serves these accounts since June 18, 2026
([announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
and the Antigravity SDK only accepts an API key or a Google Cloud project.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **No paid path remains open.** agy receives only a restricted list of
  variables from your environment — `PATH`, language and time zone,
  terminal, identity, proxies and certificates, session bus — and no keys:
  several of its variables switch a call without displaying anything (measured:
  one sends the document to a third-party gateway, another to a billed Google
  Cloud project), and a deny list missed some with every review. Before any
  segment, `agy -p /config`, which costs no quota, must show paid AI credits
  disabled, with neither an API key nor a Google Cloud project — a missing
  setting counts as a rejection —, otherwise nothing is translated; the log for
  each call must then confirm the subscription (`authMethod=consumer`), otherwise the
  response is rejected.
- **Sandboxing.** Each call runs in a private, disposable personal directory,
  with a tool-less translation agent: your agy settings, rules, plugins, MCP
  servers, and hooks do not enter it, nothing is added to your history, and the
  login stays in the keyring, which aipmt never reads. A missing agent silently
  causes agy to fall back to its coding agent and tools: an entire line in the
  log must confirm the correct agent — a document quoting this message does not
  replace it —, otherwise it is rejected.
- **Platforms**: Linux, in a session that has a keyring (D-Bus session bus,
  Secret Service); macOS is supported, without having been benchmarked. Rejected
  on Windows, where agy does not read the variables that isolate each call, and
  on Linux without a session bus — SSH session, container, server: agy stores its
  token there in a file in `~/.gemini`, which isolation hides. Rejection
  occurs before any launch, along with its cause, instead of waiting a minute
  for a login code.
- **Models**: those from `agy models`. Gemini models include the effort in
  their name (`gemini-3.8-flash-medium`…): a name without a suffix is rejected before the
  call, and `--reasoning_effort` has no effect. Defaults to `gemini-3.8-flash-medium`, and
  `gemini-3.7-flash-low` in `--eco`; the test runs that established them are
  described in [Detailed benchmarks](#detailed-measurements). Claude and GPT-OSS have their
  own quota, which is much smaller: about 1% of the 5-hour window per measured
  call, compared to 0.05% with Flash.
- **Quota**: per group, a 5-hour window and a weekly window, prorated to token
  cost. Measured on the author's account: about 16 points of the 5-hour window per
  million source characters in `gemini-3.8-flash-medium`, 14 in `gemini-3.7-flash-medium`, and 7 to 8
  at low effort — a 40,000-character README therefore costs just over half a
  point. The weekly limit depends on the tier. Retries follow what agy declares
  retryable; otherwise, an exhausted window is never retried: it causes every
  file to fail until the reset displayed by `/usage`.
- **Slower than the API**: on the dense benchmarking article, a median of
  3 min 59 s per language in `gemini-3.8-flash-medium` and 3 min 14 s in
  `gemini-3.7-flash-medium`, compared to 1 min 18 s for Gemini 3.7 Flash via the API.
- **Interruption**: Ctrl-C, or closing the terminal, stops agy along with the
  command instead of letting it finish its turn on your quota; the same applies
  to Codex, Grok CLI, and OpenCode. Under `nohup`, translation continues.
- Rejected in CI (`CI` or `GITHUB_ACTIONS` set): the login resides in a
  personal keyring. On a runner, use `--use_gemini` with `GOOGLE_API_KEY`.
- Variables: `AGY_BIN` (otherwise `PATH`, then `~/.local/bin/agy`),
  `AGY_TIMEOUT` (seconds per segment, startup included, default 900).

**Terms of Service: your account is on the line.** The
[Antigravity terms of service](https://antigravity.google/terms) (section 6) and its
[FAQ](https://antigravity.google/docs/faq/) prohibit accessing the service via third-party software using
the Antigravity login — Claude Code, OpenClaw, and OpenCode are cited —, under
penalty of account suspension. aipmt neither reads nor reuses the token: it runs
the official binary in the [headless mode](https://antigravity.google/docs/cli/headless/) documented by Google for
scripts and CI. A Google employee considered it “standard” to launch
`agy -p` from a local script for one's own work
([official forum, September 25, 2026, non-binding answer](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
no official text addresses the case of a distributed tool like this one.

**Public documents only.** According to section 5 of the same terms, exchanges —
prompts, responses, metadata — may be used to improve Google's products and
machine learning and may be reviewed by humans, including for paid
subscriptions. Opting out requires the `enableTelemetry` setting, whose effect is
undocumented and which aipmt does not configure; your agy settings are not
carried over into its isolation. Do not pass anything confidential through it.

### On the Claude subscription: `--use_claude_code`

Same principle with `claude`, the official Claude Code CLI, in `-p` mode: for
those paying for Claude Pro or Max, translation is deducted from the
subscription quota instead of being billed per token. Not to be confused with
`--use_claude`, Anthropic's API, which is billed based on usage.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **No paid channel remains open, and each call proves it.** Claude
  Code receives only a closed list of variables from your environment — no
  API key, token, cloud provider, or marker from the Claude Code session
  from which aipmt was launched. Before the first segment, `claude auth status` must
  show the subscription connection, without a Console key, and `/usage`, which costs
  no quota, must attest to it; each call in turn attests to it in its
  initialization event, otherwise the response is rejected.
- **Disable "extra usage"** (claude.ai, Settings → Usage) so
  that zero euros holds: enabled, it takes over when a window is exhausted and
  bills without displaying an error. aipmt stops translation as soon as the
  quota report from a call flags it, but that call is already counted.
- **Quota shared with your Claude Code sessions.** Each call reports
  usage for the 5-hour and weekly windows; beyond 80%
  (`AIPMT_CLAUDE_MAX_UTILIZATION`), no further segments are launched, so as
  not to exhaust what serves your work.
- **Confinement.** Each call runs without tools, in a private,
  disposable directory, in zero-customization mode: neither your `CLAUDE.md`, nor your plugins,
  hooks, MCP servers, or settings are loaded, and nothing is retained from the
  session. Attachments are cut off: an `@chemin` in your document
  remains text and opens no file (measured).
- **Models**: `sonnet` by default, at effort `low`, and in `--eco` as well:
  `--eco` changes nothing along this path. Measured on the same documents, `haiku`
  is twice as slow — it reasons without any way to prevent it — for
  barely lower cost, and `opus` rejects biology content (next
  point). Both remain accessible via `--model`; these aliases follow the
  latest model in their family. `fable` and `[1m]` variants are rejected,
  because they fall back to paid credits. `--reasoning_effort` adjusts the effort,
  from which translation gains nothing: measured reasoning is virtually nil.
- **Opus rejects certain biology content.** Its guardrails are stricter
  than Sonnet's, and Anthropic's error message warns that they
  "can sometimes flag biology-research-adjacent work". Measured: a monitoring
  brief on 279 generated molecules caused the article to be rejected across all fourteen
  languages. Nothing is written: aipmt rejects the truncated response, identifies the
  guardrails, and suggests `--model sonnet`.
- Rejected in CI (`CI` or `GITHUB_ACTIONS` set) and under Windows (not measured).
- Variables: `AIPMT_CLAUDE_BIN` (otherwise the `PATH`, then `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (seconds per segment, default 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (default 0.8), `CLAUDE_CONFIG_DIR` (the Claude
  Code account, never taken from a project `.env`); working directories under
  `XDG_CACHE_HOME/aipmt/claude-code` (default `~/.cache`).

**Terms of Service: it is your account at stake.** The
[Claude Code legal page](https://code.claude.com/docs/en/legal-and-compliance)
does not prevent "an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription": this is what aipmt does, launching the
official binary and never reading the token. But Anthropic "does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users", prefers an API key for third-party
tools, "including open-source projects", and reserves the right to charge their
usage against paid credits
([Claude help](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
No text settles the case of a distributed tool launching the binary.

**Data**: on Free, Pro, and Max accounts, model training
also applies to Claude Code when privacy settings allow it
([data page](https://code.claude.com/docs/en/data-usage)). aipmt keeps
no local transcript (`--no-session-persistence`). Do not pass
anything confidential through it.

### To the provider of your choice: `--use_opencode`

[OpenCode](https://opencode.ai) is an open-source (MIT) code agent that
routes to the providers configured within it: API key, subscription,
OpenCode Zen gateway (free models, no account required), or local model. Two
paths were measured end-to-end here, Zen and Ollama.

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
whose exchanges can be used for training, and this choice is not made
for you.

Confinement on each call:

- an inline configuration, taking precedence over yours, defines an agent `aipmt`
  with all tools disabled (`permission: { "*": "deny" }`), session sharing
  disabled, `--pure`, never `--auto`;
- disposable, empty working directory, `OPENCODE_DISABLE_PROJECT_CONFIG` and
  `OPENCODE_DISABLE_CLAUDE_CODE` placed — without them, OpenCode injects the
  current directory's `AGENTS.md` and `~/.claude/CLAUDE.md` into the prompt. The
  global `~/.config/opencode/AGENTS.md` remains injected; OpenCode does not allow
  omitting it;
- output contract: exit code 0, no `error` event, no tool
  calls, last step in `stop`, non-empty text, and the `aipmt` agent
  actually loaded — an unknown `--agent` does not make OpenCode fail, it
  silently falls back to the coding agent;
- no `aipmt` key is passed, except `OPENCODE_API_KEY`, OpenCode's
  own key. Providers are configured in OpenCode, not in
  `aipmt`'s `.env`.

Good to know:

- Zen's free models are subject to change, with undocumented limits, and
  their exchanges may be used for training: suitable for public
  documentation, not for private content.
- A local model must offer at least 16k context tokens, as segments
  can be up to 16,000 characters. Ollama often configures 4,096: use
  a `Modelfile` with `PARAMETER num_ctx 32768`.
- `--eco` has no effect; `--reasoning_effort` is passed as-is as
  OpenCode's `--variant`.
- OpenCode logs each session in `~/.local/share/opencode/`.
- Variables: `OPENCODE_BIN` (otherwise the `PATH`, then `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (seconds per segment, default 600). `OPENCODE_CONFIG`
  is passed as-is to OpenCode.

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
models, which cannot be disabled via a Modelfile. Measured on a six-word
sentence: 919 thinking tokens and 68 seconds without the option, 9 tokens with it.

### To more than 400 models: `--use_openrouter`

OpenRouter is a usage-billed router, using unified credits, in front of
third-party hosted models — including open Chinese models that no
other provider exposes here.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` is mandatory. A preflight check, run before any billing, handles
two routing quirks:

- **The same model is served by dozens of hosts with different limits** — on `z-ai/glm-5.3-flash`, 23 hosts, one of which is capped at
  2,048 output tokens. The preflight check reads `/api/v1/models/{modèle}/endpoints`,
  filters out hosts with fewer than 8,000 output tokens or degraded status, and
  pins the others with `allow_fallbacks: false`.
- **Reasoning is billed at the output rate** — 107 tokens versus 2 on
  an "OK" response from `z-ai/glm-5.2`. It is disabled by default; models
  that require it receive the lowest effort they accept, as the catalog
  default could saturate the output before translation completes.
  `--reasoning_effort` still takes precedence.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- The context window comes from the catalog. A model under 16,400 tokens is
  rejected before any call: 8,400 for the prompt and segment, 8,000 output
  at minimum.
- A slug missing from the catalog, an unreachable catalog, or the absence
  of a host meeting the cap stops the command.
- `finish_reason=length` with empty output indicates a budget consumed by
  reasoning, not truncation: the message distinguishes between them.
- `--eco` has no effect.
- Variables: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (default `https://openrouter.ai/api/v1`, `https://`
  required), `OPENROUTER_TIMEOUT` (default 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (default 30).

### Translation note

`--add_translation_note` adds a note, at `bottom` (default), `top` (after the
front matter), or `both` (`--note_position`), formatted as `legacy` (bold
paragraph, default) or `marker` (`--note_format`). The `marker` format is an
invisible Markdown reference definition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
followed by a bold blockquote: readable on GitHub, usable at build time by a
remark plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detailed measurements

All measurements are actual translations performed with `aipmt`, into
fourteen languages: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Written** counts the files passed by the guards; **No
discrepancy** counts those where `scripts/compare_structure.py` finds nothing — same number of
sections, subheadings, links, distinct URLs, code blocks, inline
code, table rows, blockquotes, and bold words.

"No discrepancy" means "nothing detected", not "identical": the comparator
counts elements without reading their content. It does not flag a removed
level-4 heading, replaced inline code text, a swapped flag, or an internal
link rendered with an extra parenthesis,
`[texte]((#ancre))`, which no longer leads anywhere — and it does not judge the
language quality.

### Dense monitoring article, `--news` mode

An edition of the [jls42.org AI watch](https://jls42.org/fr/news):
589 lines, 140 links, 21 sections, 3 protected English quotes. Run on
September 4 and 5, 2026.

| Model                                           | Access             | Written | No discrepancy | Median/language |
| ----------------------------------------------- | ------------------ | ------- | -------------- | --------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14**   | 1 min 18 s      |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google subscription| 14/14   | ✅ **14/14**   | 3 min 59 s      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google subscription| 14/14   | ✅ **14/14**   | 3 min 14 s      |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT subscription | 14/14   | ✅ **14/14**   | 11 min 28 s     |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14**   | 5 min 37 s      |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14**   | 26 min 23 s     |
| `sonnet` (`--use_claude_code`)                  | Claude subscription| 14/14   | ⚠️ 13/14       | 6 min 49 s      |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14       | 6 min 31 s      |
| `haiku` (`--use_claude_code`)                   | Claude subscription| 14/14   | ⚠️ 11/14       | 15 min 54 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14       | 9 min 27 s      |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14        | 10 min 09 s     |
| `ollama/gpt-oss-20b-32k`                        | local              | 10/14   | ❌ 7/14        | 12 min 39 s     |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14        | 5 min 32 s      |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14        | 37 min 27 s     |
| `grok-4.6` (`--use_grok_cli`)                   | Grok subscription  | 1/14    | ❌ 1/14        | 23 min 11 s     |
| `opus` (`--use_claude_code`)                    | Claude subscription| 0/14    | ❌ 0/14        | —               |

Grok was remeasured on September 9 on another edition of the same watch
(356 lines): 9 languages written out of 14, 8 with no discrepancies. It is this figure
that appears in the top table. Three interrupted runs are not
listed: `qwen3.5-27b` (9 languages) and `kimi-k2.6` (4) due to lack of credits,
`z-ai/glm-5.3-flash`, whose two failures came from a reasoning setting
that the provider has since fixed. OpenRouter rows were measured using the
router's default settings, before `--use_openrouter`; `z-ai/glm-5.2`,
remeasured with the bundled provider, yields the same 14/14. Figures were
recalculated on September 10 with the current comparator: `qwen3.8-flash` and
`qwen3.7-flash` each gain one language compared to the initial
publication, while the others remain unchanged.

The `--use_antigravity` rows were measured on September 26 on the same
article, four translations in parallel: `gemini-3.7-flash-medium` in the morning,
`gemini-3.8-flash-medium` in the afternoon. In English, each model independently removed
the three French translation lines below the quotes, without inventing any
flags, and the English quotes remained intact: the fallback cleanup had
nothing to do. In `--eco` (`gemini-3.7-flash-low`), across four languages
only (en, ja, ar, hi): 4 written out of 4, all with no discrepancies, 1 min 52 s
median. Cross-check on the same day on a more recent edition of the watch,
that of September 25 (438 lines, 2 English quotes), translated outside the
blog using `gemini-3.7-flash-medium`: 14 written out of 14, all with no discrepancies, 87 to
128 s per language.

The `--use_claude_code` rows were measured on September 26 on the same
article, four translations in parallel, at effort `low`. With `sonnet`, the
English quotes are intact across all fourteen languages, and in English, the
model independently removed the French translation lines without inventing a
flag. `opus` wrote no language: in each, its guardrails
stopped the response at the final segment, due to a brief on 279 molecules
generated for a binding site. Sent alone, this brief is rejected under the
"bio" category; `sonnet` translated it everywhere. `haiku` writes
all fourteen languages; in three (en, pl, ro), a section title shifts from
level 2 to level 1. It reasons without any way to prevent it — 61% of
its output tokens —, resulting in more than double the time of `sonnet`.

### This Project's README, Standard Markdown

Frozen revision on September 9, 2026: 785 lines, 285 inline code snippets, 40
block fences, 89 table rows. Four parallel translations.

| Model                                           | Written | No divergence | Median/language | What differs                                                             |
| ----------------------------------------------- | ------- | ------------- | --------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14      | 1 min 43 s      | nothing                                                                  |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14      | 1 min 48 s      | nothing                                                                  |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14      | 4 min 02 s      | nothing for the comparator; internal links duplicated (en)              |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14      | 36 s            | one bold word (ja)                                                       |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14      | 1 min 22 s      | one bold word (ko)                                                       |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14      | 2 min 20 s      | one table row merged with the previous one (ar)                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14      | 2 min 56 s      | one link (sv), one bold word (zh)                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14      | 6 min 46 s      | one bold word (ar, ja)                                                   |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14      | 2 min 34 s      | one bold word (hi, ja, ko)                                               |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14      | 2 min 17 s      | 40 inline code snippets added in Arabic; bold (hi, ja, ko)               |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14       | 2 min 44 s      | one missing section (ar, hi, ko); code blocks added (ja, ko, ro, zh)    |

Two interrupted runs are not scored: Grok, CLI session expired after twelve
languages (eleven without divergence), and `qwen3.8-flash`, HTTP 429 from its
host after two. `opencode/mimo-v2.5-free` and `ollama/gpt-oss-20b-32k` were not remeasured on this
revision; on the September 4–5 revision, which was 277 lines shorter, they each
wrote 9 out of 14 translations, with 7 and 1 without divergence, respectively.

The `--use_antigravity` and `--use_claude_code` rows were not measured on the frozen
revision, but on September 26 on the version published with 1.14.0: 600 lines,
257 inline code snippets, 30 block fences, 85 table rows. Shorter by 185 lines,
it cannot be directly compared to the other rows; those specific rows, however,
can be compared with each other. Regarding internal links, which the comparator
does not check, `gemini-3.8-flash-medium` kept them intact across all fourteen languages,
`gemini-3.7-flash-medium` broke them in Italian; `sonnet` and `opus` kept
them intact everywhere, `haiku` duplicated them in English.

### Four READMEs from Well-Known Projects

FastAPI, Ollama, tldr-pages, and Vue.js, taken as-is from GitHub — easier
documents than the previous two. The benchmark targeted struggling models;
Gemini serves as a baseline comparison.

| Model                     | Scope                      | Written | No divergence |
| ------------------------- | -------------------------- | ------- | ------------- |
| `gemini-3.7-flash`        | 4 projects × 14 languages  | 56/56   | ✅ **55/56**  |
| `opencode/mimo-v2.5-free` | 4 projects × 14 languages  | 55/56   | ❌ 47/56      |
| `grok-4.6` (subscription) | 4 projects × ar, hi, ja, zh | 16/16   | ❌ 14/16      |
| `ollama/gpt-oss-20b-32k`  | 4 projects × ar, hi, ja, zh | 15/16   | ❌ 9/16       |

### What These Benchmarks Are Not

- **Not an exhaustive ranking**: OpenRouter alone offers over four hundred
  models; about fifteen were tested.
- **Indicative runtimes**: three to six parallel translations depending on the
  campaigns, and a provider's throughput varies throughout the day.
- **Point-in-time observations**: models evolve under the same name, and your
  documents are not ours.

To rerun the benchmark on your own documents, using a frozen copy of the file:

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

Both lines are required: without `pip install -e .`, `python -m aipmt` returns
`No module named aipmt`.

Quality tooling, optional but recommended:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

The repository's 28 translations (README and CHANGELOG, fourteen languages)
are regenerated with `./regen_translations.sh --force` — Codex and `gpt-5.6-sol` on the ChatGPT
subscription by default, four in parallel. `REGEN_PROVIDER` and `REGEN_MODEL`
change the path: `antigravity` remains on a subscription (Google's) and passes
without exemption; a billed API (`openai`, `gemini`,
`grok`, `openrouter`) is rejected without `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` caps each job (600 s, 1,800 s for Codex and Antigravity). Tooling
details can be found in `CLAUDE.md`.

## Projects Using This Script

- **[jls42.org](https://jls42.org)** — personal blog published in 15 languages. Its
  [daily AI watch](https://jls42.org/fr/news) is translated every day using this tool and serves
  as the benchmark document for the measurements above.

## Author

Julien LE SAUX
Email: contact@jls42.org

## License

GNU GENERAL PUBLIC LICENSE Version 3. See [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Disclaimer

This program is distributed **without any warranty**, under the terms of
sections 15 and 16 of the GPL v3: provided "as is", without warranty of
merchantability or fitness for a particular purpose, and its author cannot be
held liable for any damage resulting from its use. The text of the license
supersedes this summary.

- **Review before publishing.** Protections cover code blocks, inline code,
  URLs, anchors, and blockquotes in `--news` mode — not headings, tables,
  front matter, or the meaning of your sentences.
- **Your documents are sent to the chosen provider**, subject to their terms of
  service and privacy policy. Some free models may reuse your interactions for
  training, and Antigravity's terms allow Google to reuse them and have them
  reviewed by humans, even under a paid subscription; a local model is the only
  way to ensure that no data leaves your machine.
- **You are billed for API calls.** This program does not cap expenses: a long
  document, retries after failure, or a model that reasons heavily will cost
  more.
- **Published benchmarks are point-in-time observations**, not guarantees.

Product and company names mentioned belong to their respective owners. This
project is not affiliated with any of them.

**Article translated from French to English with gemini-3.8-flash-medium.**
