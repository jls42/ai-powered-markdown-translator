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
matter. Ten ways to call a model—five APIs, three subscriptions without
pay-per-use billing, two routers—and a published benchmark of what each
model actually preserves.

## At a Glance

- **Ten provider pathways**: OpenAI, Mistral, Claude, Gemini, and Grok APIs;
  ChatGPT (Codex), Grok, and Google (Antigravity) subscriptions without pay-per-use
  billing; OpenCode (open source, free or local) and OpenRouter
  (over 400 models) routers.
- **Nothing corrupted by a lost token**: code blocks, inline code,
  URLs, anchors, and blockquotes are replaced with tokens before the call and
  verified upon return. If even one is missing, the file is not written.
- **Long documents**: chunking according to the model's context window.
- **`--news` mode**: English quotes protected and flags handled per
  language, for tech watch articles.
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

Keys are read from three locations, in descending order of priority; each only
fills in what the previous one left unset.

|     | Where                                         | What for                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Environment variables                         | CI, containers, one-off overrides     |
| 2   | `.env` in current directory (or parent)| a project-specific key                |
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
on Windows. Without a key, the command lists the three locations.

**A project's `.env` can neither redirect calls nor select the executed
program.** It provides keys, never an endpoint or a binary: any
variable ending in `_BASE_URL`, `_API_BASE`, `_ENDPOINT`, or `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, proxies (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), certificate stores (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`), and `XDG_CONFIG_HOME` /
`APPDATA` are ignored there, with a warning. A cloned repository must not
be able to hijack your key or trick you into running its own binary on the
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

`document.md` translated to Spanish yields `document-es.md` in `--target_dir`;
with `--include_model`, `document-es-gpt-5.6-terra.md`. The extension always
becomes `.md`—`article.mdx` yields `article-en.md`—except with
`--keep_filename`, which keeps the original name. An existing translation
is skipped without `--force`.

Exit codes: `0` if everything succeeded or was skipped, `1` if any file
failed (listed on standard error), `2` if configuration is at fault.
A failed file is never written, even if writing itself fails:
content is written nearby and then renamed. Re-running is sufficient.

## Which Model to Choose

Measured across two real-world documents, translated into the same fourteen languages by
each model. **The number represents the count of languages, out of fourteen, where the
translation is written and nothing differs from the source.**

| Model                | How to access it                  | Dense tech watch article| This README | What differs, and across how many languages                                                                                           |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.8 Flash** | Google subscription (Antigravity) | ✅ 14/14                | ✅ 14/14     | nothing, on either document                                                                                                           |
| **Gemini 3.7 Flash** | Google API key                    | ✅ 14/14                | ⚠️ 13/14     | 1 language out of 14: one extra bold word (ja)                                                                                        |
| **Gemini 3.7 Flash** | Google subscription (Antigravity) | ✅ 14/14                | ⚠️ 13/14     | 1 language out of 14: one fewer bold word (ko)                                                                                        |
| **GPT-5.6 Sol**      | ChatGPT subscription, or OpenAI key| ✅ 14/14               | ⚠️ 12/14     | 2 languages out of 14: one fewer bold word (ar, ja)                                                                                   |
| **GLM-5.2**          | OpenRouter key                    | ✅ 14/14                | ⚠️ 11/14     | 3 languages out of 14: one fewer bold word (hi, ja, ko)                                                                               |
| Claude Sonnet 5      | Anthropic API key                 | ⚠️ 11/14                | ⚠️ 12/14     | 3 languages on the article: an extraneous code block appeared (es, de, hi); 2 on this README: a link missing its markup (sv), one bold word (zh) |
| Qwen 3.7 Flash       | OpenRouter key                    | ❌ 8/14                 | ⚠️ 10/14     | 1 language rejected on the article, 5 others deviate; on this README, around forty words placed in `code` (ar)                 |
| Grok 4.6             | Grok subscription                 | ❌ 8/14                 | not rated    | 5 languages rejected out of 14, due to missing inline code and URLs; Dutch diverges completely                                       |
| GPT-OSS 20B          | local model (Ollama)              | ❌ 7/14                 | not remeasured| 4 languages rejected out of 14: the model left passages in French, stopped by guardrails                                              |
| MiMo v2.5 (free)     | OpenCode Zen, no account          | ❌ 11/14                | not remeasured| 1 language rejected; one missing section in Polish                                                                                    |
| Mistral Large        | Mistral API key                   | ❌ 5/14                 | ❌ 1/14      | **an entire section disappears**: 1 language on the article (hi), 3 on this README (ar, hi, ko)—and 3 languages rejected on the article|
| DeepSeek V4 Flash    | OpenRouter key                    | ❌ 3/14                 | not remeasured| 10 languages rejected out of 14; 37 minutes per language                                                                             |

|     | What the symbol means                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | all fourteen languages translated, and nothing differs from the source                                                                                                                                |
| ⚠️  | all fourteen languages translated; what differs is **markup**—a bold word, an `code`, a link losing its brackets. No text, URL, code block, or section is missing                           |
| ❌  | at least one language could not be translated—the file was rejected, not written—**or** content is missing in a written file                                                                         |

Key takeaways:

- **A rejected translation is not a corrupted translation.** When a token
  is missing upon return, the file is not written, and the language counts as
  rejected. This is what happens to Grok on the article: four inline code snippets and
  three URLs lost in the very first chunk across the five non-Latin scripts.
- **This safety net does not cover headings, tables, front matter, or
  text.** A model that drops a section produces a file that the tool writes
  without hesitation—this is the case with Mistral. These elements cannot be
  replaced by tokens, and current guardrails do not check them;
  `scripts/compare_structure.py` detects a missing section, but only after the fact.
- **Grok has no rating on this README**: its CLI session expired after twelve
  languages, eleven of which had no discrepancies. An interrupted run is not rated.
- **Document density matters more than the language.** Grok holds up on
  standard READMEs but falters on an article heavily packed with links, including
  in Dutch.

Dates and documents: the "This README" column was measured on September 9, 2026,
against a frozen revision of this file (785 lines, 285 inline code snippets, 89 table
rows), updated since—except for the two Antigravity rows, measured on
September 26 against the revision published with 1.14.0, which was shorter (600 lines,
257 inline code snippets, 85 table rows). The "Dense tech watch article"
column comes from the September 4–5 run on a 589-line article,
except for the Grok row, remeasured on September 9 on another edition of the same
watch, and the two Antigravity rows, measured on September 26 on the same
article.
Full tables, run times, and methodology can be found in
[Detailed Benchmarks](#detailed-measurements).

## All Options

| Option                   | Description                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Single Markdown file to translate (alternative to `--source_dir`)                                             |
| `--source_dir`           | Source directory containing Markdown files (default: `content/posts`)                                         |
| `--target_dir`           | Output directory for translated files (default: `traductions_en`)                                              |
| `--source_lang`          | Source language (default: `fr`)                                                                     |
| `--target_lang`          | Target language (default: `en`)                                                                     |
| `--model`                | Specific model to use                                                                                         |
| `--eco`                  | Use budget models                                                                                             |
| `--use_mistral`          | Use Mistral AI API                                                                                            |
| `--use_claude`           | Use Claude API                                                                                                |
| `--use_gemini`           | Use Gemini API                                                                                                |
| `--use_grok`             | Use xAI (Grok) API — requires `XAI_API_KEY`                                                                  |
| `--use_codex`            | Use Codex CLI against ChatGPT subscription quota                                                              |
| `--use_grok_cli`         | Use Grok CLI against Grok subscription quota                                                                  |
| `--use_antigravity`      | Use Antigravity CLI (`agy`) against Google AI Pro or Ultra subscription quota                        |
| `--use_opencode`         | Use OpenCode (open source) routed to the provider configured in OpenCode; requires `--model provider/modèle`             |
| `--use_openrouter`       | Use OpenRouter — requires `OPENROUTER_API_KEY` and `--model fournisseur/modèle`                                                  |
| `--force`                | Force re-translation                                                                                          |
| `--keep_filename`        | Preserve original filename                                                                                    |
| `--news`                 | News/tech watch mode: protects EN quotes, handles flags per language                                          |
| `--add_translation_note` | Add translation note                                                                                          |
| `--note_position`        | Note position: `top`, `bottom` (default), or `both`                                    |
| `--note_format`          | Note format: `legacy` (default, bold paragraph) or `marker`                                       |
| `--include_model`        | Include model name in output file                                                                             |
| `--reasoning_effort`     | GPT-5.x reasoning effort: `none`/`low`/`medium`/`high`/`xhigh`    |

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

| Provider    | Quality (default)                                     | Budget (`--eco`)  |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol` (also `terra` and `luna` via `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| OpenCode    | `--model provider/modèle` required                    | same — `--eco` has no effect |
| OpenRouter  | `--model fournisseur/modèle` required                 | same — `--eco` has no effect |

### On the ChatGPT subscription: `--use_codex`

Drives the official Codex CLI: translation is counted against your ChatGPT
subscription quota, with no API key or usage-based billing.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- The binary is looked up in `CODEX_BIN`, then `PATH`, then the
  `openai-codex-cli-bin` package. `~/.codex/auth.json` is never read.
- `OPENAI_API_KEY` and `CODEX_API_KEY` are removed from the subprocess
  environment: an existing key never causes a switch to the API.
- Each segment costs at least one "message" in the 5-hour window — two if its
  validation fails and it is retried. OpenAI provides an estimate of
  250–2,000 messages/5 h for `gpt-5.6-luna` (`--eco`) and 10–100 for
  `gpt-5.6-sol` on a Plus plan.
- `--model gpt-5.6-terra` and `--model gpt-5.6-luna` also go through the subscription. A model
  not entitled to the account returns a 400 "model is not supported when using
  Codex with a ChatGPT account".
- Slower than an API, and the gap widens with document size: on this README,
  a median of 6 min 46 s per language with `gpt-5.6-sol`, compared to 36 s for
  `gemini-3.7-flash`.
- Rejected in CI (`CI` or `GITHUB_ACTIONS` set): the subscription
  authenticates via a personal session file, which does not belong on a shared
  runner.
- Variables: `CODEX_BIN`, `CODEX_TIMEOUT` (seconds per segment, default 600).

### On the Grok subscription: `--use_grok_cli`

Same principle with the official Grok Build CLI, using a SuperGrok or
X Premium+ subscription.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Weaker confinement than Codex.** Grok's OS sandbox does not apply on many
  recent Linux machines (AppArmor, container runtime sockets), and a profile
  that cannot be applied silently starts unconfined. The script therefore does
  not request any profile by default, announces it, and relies on the CLI's
  `--deny` rules, including the catch-all `*` — the only
  layer that refuses to start rather than silently dropping protection.
  `GROK_TRANSLATE_SANDBOX=read-only` enforces the OS sandbox, and startup fails if the machine
  cannot honor it.
- The quota is weekly, shared with Chat, Imagine, and Voice, and no command
  allows checking it: a batch may consume conversational usage without warning.
- Variables: `GROK_BIN`, `GROK_HOME` (CLI directory, default `~/.grok`),
  `GROK_TIMEOUT` (default 900), `GROK_TRANSLATE_SANDBOX`.

### On the Google subscription: `--use_antigravity`

Same principle with `agy`, the official Antigravity CLI: for those who pay
for Google AI Pro or Ultra, translation is deducted from the subscription quota
instead of being billed per token. This is the only path to this quota: Gemini
CLI has no longer served these accounts since June 18, 2026
([announcement](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
and the Antigravity SDK only accepts an API key or a Google Cloud project.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **No paid path remains open.** agy receives from your environment only an
  allowlist of variables — `PATH`, language and timezone, terminal,
  identity, proxies and certificates, session bus — and no keys: several of its
  variables switch a call without displaying anything (measured: one sends the
  document to a third-party gateway, another to a billed Google Cloud project),
  and a deny list missed some on every review. Before any segment,
  `agy -p /config`, which costs zero quota, must show paid AI credits disabled,
  without an API key or Google Cloud project — a missing setting counts as a
  rejection —, otherwise nothing is translated; the log for each call must then
  confirm the subscription (`authMethod=consumer`), otherwise the response is rejected.
- **Confinement.** Each call runs in a private, disposable personal directory,
  with a tool-less translation agent: your agy settings, rules, plugins, MCP
  servers, and hooks do not enter it, nothing is added to your history, and the
  login session remains in the keyring, which aipmt never reads. A missing agent
  silently causes agy to fall back to its coding agent and its tools: an entire
  log line must confirm the correct agent — a document quoting this message
  does not replace it —, otherwise it is rejected.
- **Platforms**: Linux, inside a session with a keyring (D-Bus session bus,
  Secret Service); macOS is supported, but has not been benchmarked. Rejected on
  Windows, where agy does not read the variables that isolate each call, and on
  Linux without a session bus — SSH session, container, server: agy stores its
  token in a `~/.gemini` file there, which isolation hides. The refusal occurs
  prior to launch, explaining the cause, instead of waiting a minute for a
  login code.
- **Models**: those from `agy models`. Gemini models include the effort level
  in their name (`gemini-3.8-flash-medium`...): a name without a suffix is rejected prior
  to the call, and `--reasoning_effort` has no effect. Defaults to `gemini-3.8-flash-medium`,
  and `gemini-3.7-flash-low` in `--eco`; the evaluation runs that determined
  them are described in [Detailed measurements](#detailed-measurements). Claude and GPT-OSS
  have their own quota, which is much smaller: about 1% of the 5-hour window
  per measured call, compared to 0.05% for Flash.
- **Quota**: per group, a 5-hour window and a weekly window, proportional to
  token cost. Measured on the author's account: approximately 16 points of the
  5-hour window per million source characters in `gemini-3.8-flash-medium`, 14 in
  `gemini-3.7-flash-medium`, and 7 to 8 at low effort — a 40,000-character README
  therefore costs just over half a point. The weekly limit depends on the tier.
  Retries follow what agy reports as retryable; otherwise, an exhausted window
  is never retried: it fails every file until the reset displayed by
  `/usage`.
- **Slower than the API**: on the dense benchmark article, a median of 3 min 59 s
  per language in `gemini-3.8-flash-medium` and 3 min 14 s in `gemini-3.7-flash-medium`, compared to
  1 min 18 s for Gemini 3.7 Flash via the API.
- **Interruption**: Ctrl-C, or a closed terminal, stops agy along with the
  command instead of letting it finish its turn on your quota; the same applies
  to Codex, Grok CLI, and OpenCode. Under `nohup`, translation continues.
- Rejected in CI (`CI` or `GITHUB_ACTIONS` set): the login session
  lives in a personal keyring. On a runner, use `--use_gemini` with
  `GOOGLE_API_KEY`.
- Variables: `AGY_BIN` (otherwise `PATH`, then `~/.local/bin/agy`),
  `AGY_TIMEOUT` (seconds per segment including startup, default 900).

**Terms of Service: your account is on the line.** The
[Antigravity Terms](https://antigravity.google/terms) (Section 6) and its
[FAQ](https://antigravity.google/docs/faq/) prohibit accessing the service via
third-party software using the Antigravity login — Claude Code, OpenClaw, and
OpenCode are cited —, under penalty of account suspension. aipmt neither reads
nor reuses the token: it runs the official binary in the
[headless mode](https://antigravity.google/docs/cli/headless/) documented by Google for
scripting and CI. A Google staff member deemed running `agy -p` from a
local script for one's own work "standard"
([official forum, September 25, 2026, non-contractual reply](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
no documentation definitively settles the case of a distributed tool like this
one.

**Public documents only.** Under Section 5 of the same terms, interactions —
prompts, responses, metadata — may be used to improve Google products and
machine learning and may be reviewed by humans, including for paid
subscriptions. Opting out requires the `enableTelemetry` setting, whose effect is
undocumented and which aipmt does not set; your agy settings do not carry over
into its isolation. Do not pass anything confidential through it.

### To the provider of your choice: `--use_opencode`

[OpenCode](https://opencode.ai) is an open-source (MIT) coding agent
that routes to providers configured within it: API key, subscription, OpenCode
Zen gateway (free models, no account required), or local model. Two paths were
tested end-to-end here: Zen and Ollama.

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

`--model` is required: without it, OpenCode would fall back to a free
model whose exchanges may be used for training, and that choice is not made for
you.

Confinement on each call:

- an inline configuration, taking precedence over yours, defines a
  `aipmt` agent with all tools denied (`permission: { "*": "deny" }`), session
  sharing disabled, `--pure`, never `--auto`;
- disposable and empty working directory, `OPENCODE_DISABLE_PROJECT_CONFIG` and `OPENCODE_DISABLE_CLAUDE_CODE`
  set — without them, OpenCode injects the current directory's `AGENTS.md`
  and `~/.claude/CLAUDE.md` into the prompt. The global `~/.config/opencode/AGENTS.md` is still
  injected, as OpenCode does not allow excluding it;
- exit contract: exit code 0, no `error` event, no tool calls, final step
  in `stop`, non-empty text, and the `aipmt` agent actually
  loaded — an unknown `--agent` does not fail OpenCode, it silently falls
  back to the coding agent;
- no `aipmt` key is passed, except `OPENCODE_API_KEY`, the OpenCode key
  itself. Providers are configured in OpenCode, not in the `.env` of
  `aipmt`.

Good to know:

- Zen's free models are subject to change, with undocumented limits, and their
  interactions may be used for training: suitable for public documentation, not
  for private content.
- A local model must offer at least 16k context tokens, as segments can be up
  to 16,000 characters. Ollama often configures 4,096: use a `Modelfile`
  with `PARAMETER num_ctx 32768`.
- `--eco` has no effect; `--reasoning_effort` is passed as-is as OpenCode's
  `--variant`.
- OpenCode logs each session in `~/.local/share/opencode/`.
- Variables: `OPENCODE_BIN` (otherwise `PATH`, then `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (seconds per segment, default 600). `OPENCODE_CONFIG` is passed
  as-is to OpenCode.

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
models, which a Modelfile cannot disable. Measured on a six-word sentence:
919 thinking tokens and 68 seconds without the option, 9 tokens with.

### Accessing over 400 models: `--use_openrouter`

OpenRouter is a usage-billed router, using a single credit balance, fronting
models hosted by third parties — including open Chinese models that no other
provider exposes here.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` is required. A preflight check, run before any billing, handles
two routing specificities:

- **The same model is served by dozens of providers with different limits** — on
  `z-ai/glm-5.3-flash`, 23 providers, one of which is capped at 2,048 output tokens.
  The preflight check reads `/api/v1/models/{modèle}/endpoints`, discards providers with under 8,000
  output tokens or degraded status, and pins the rest with `allow_fallbacks: false`.
- **Reasoning is billed at the output rate** — 107 tokens versus 2 on an "OK"
  response from `z-ai/glm-5.2`. It is disabled by default; models that require
  it receive the lowest effort level they accept, as the catalog default could
  saturate the output before the translation completes. `--reasoning_effort` remains
  top priority.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- The context window comes from the catalog. A model under 16,400 tokens is
  rejected prior to any call: 8,400 for the prompt and segment, 8,000 output
  tokens minimum.
- A slug missing from the catalog, an unreachable catalog, or the lack of a
  provider meeting the output limit stops the command.
- `finish_reason=length` with empty output indicates a budget consumed by reasoning,
  not truncation: the message distinguishes this.
- `--eco` has no effect.
- Variables: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (default `https://openrouter.ai/api/v1`, `https://`
  required), `OPENROUTER_TIMEOUT` (default 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (default 30).

### Translation note

`--add_translation_note` adds a note at the `bottom` (default), `top`
(after front matter), or `both` (`--note_position`), formatted as
`legacy` (bold paragraph, default) or `marker` (`--note_format`).
The `marker` format is an invisible Markdown reference definition,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
followed by a bold blockquote: readable on GitHub, usable at build time by a
remark plugin.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Detailed measurements

All measurements are actual translations run with `aipmt` into fourteen
languages: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi. **Written**
counts files that passed guardrails; **No deviation** counts those where
`scripts/compare_structure.py` detects nothing — same number of sections, subheadings, links,
distinct URLs, code blocks, inline code, table rows, blockquotes, and bold words.

"No deviation" means "nothing detected", not "identical": the comparator
counts elements without reading their content. It does not flag a deleted
level-4 heading, replaced inline code text, a swapped flag, or an internal link
rendered with an extra parenthesis, `[texte]((#ancre))`, which no longer leads
anywhere — and it does not judge language quality.

### Dense tech watch post, `--news` mode

An issue of the [AI watch on jls42.org](https://jls42.org/fr/news):
589 lines, 140 links, 21 sections, 3 protected English quotes. Campaign
of September 4 and 5, 2026.

| Model                                           | Access              | Written | No discrepancies | Median/language |
| ----------------------------------------------- | ------------------- | ------- | ---------------- | --------------- |
| `gemini-3.7-flash`                              | Google API          | 14/14   | ✅ **14/14**     | 1 min 18 s      |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google subscription | 14/14   | ✅ **14/14**     | 3 min 59 s      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google subscription | 14/14   | ✅ **14/14**     | 3 min 14 s      |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT subscription| 14/14   | ✅ **14/14**     | 11 min 28 s     |
| `z-ai/glm-5.2`                                  | OpenRouter          | 14/14   | ✅ **14/14**     | 5 min 37 s      |
| `qwen/qwen3.8-flash`                            | OpenRouter          | 14/14   | ✅ **14/14**     | 26 min 23 s     |
| `claude-sonnet-5`                               | Anthropic API       | 14/14   | ⚠️ 11/14         | 6 min 31 s      |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen        | 13/14   | ❌ 11/14         | 9 min 27 s      |
| `qwen/qwen3.7-flash`                            | OpenRouter          | 13/14   | ❌ 8/14          | 10 min 09 s     |
| `ollama/gpt-oss-20b-32k`                        | local               | 10/14   | ❌ 7/14          | 12 min 39 s     |
| `mistral-large-latest`                          | Mistral API         | 11/14   | ❌ 5/14          | 5 min 32 s      |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter          | 4/14    | ❌ 3/14          | 37 min 27 s     |
| `grok-4.6` (`--use_grok_cli`)                   | Grok subscription   | 1/14    | ❌ 1/14          | 23 min 11 s     |

Grok was remeasured on September 9 on another edition of the same watch
(356 lines): 9 languages written out of 14, 8 with no discrepancies. It is this figure that
appears in the top table. Three interrupted campaigns are not
listed: `qwen3.5-27b` (9 languages) and `kimi-k2.6` (4) due to lack of credits,
`z-ai/glm-5.3-flash` whose two failures stemmed from a reasoning setting
that the provider has since corrected. The OpenRouter rows were measured with
the router's default settings, before `--use_openrouter`; `z-ai/glm-5.2`,
remeasured with the bundled provider, yields the same 14/14. The figures were
recalculated on September 10 with the current comparator: `qwen3.8-flash` and
`qwen3.7-flash` each gain one language compared to the initial
publication, the others remain unchanged.

The `--use_antigravity` rows were measured on September 26 on the same
article, four translations in parallel: `gemini-3.7-flash-medium` in the morning,
`gemini-3.8-flash-medium` in the afternoon. In English, each independently removed
the three lines of French translation under the quotes, without inventing flags,
and the English quotes remained intact: the fallback cleanup had
nothing to do. In `--eco` (`gemini-3.7-flash-low`), on four languages
only (en, ja, ar, hi): 4 written out of 4, all with no discrepancies, 1 min 52 s
median. Cross-check on the same day on a more recent edition of the watch,
that of September 25 (438 lines, 2 English quotes), translated outside the
blog by `gemini-3.7-flash-medium`: 14 written out of 14, all with no discrepancies, 87 to
128 s per language.

### README of this project, standard Markdown

Revision frozen on September 9, 2026: 785 lines, 285 inline code spans, 40
block closings, 89 table rows. Four translations in parallel.

| Model                                           | Written | No discrepancies | Median/language | What differs                                                             |
| ----------------------------------------------- | ------- | ---------------- | --------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14         | 1 min 43 s      | nothing                                                                  |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14         | 36 s            | a bold word (ja)                                                         |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14         | 1 min 22 s      | a bold word (ko)                                                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14         | 2 min 56 s      | a link (sv), a bold word (zh)                                            |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14         | 6 min 46 s      | a bold word (ar, ja)                                                     |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14         | 2 min 34 s      | a bold word (hi, ja, ko)                                                 |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14         | 2 min 17 s      | 40 inline code spans added in Arabic; bold (hi, ja, ko)                   |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14          | 2 min 44 s      | one missing section (ar, hi, ko); code blocks added (ja, ko, ro, zh)     |

Two interrupted campaigns are not listed: Grok, CLI session expired
after twelve languages (eleven with no discrepancies), and `qwen3.8-flash`, HTTP 429 from its
host after two. `opencode/mimo-v2.5-free` and `ollama/gpt-oss-20b-32k`
were not remeasured on this revision; on the September 4 and 5 revision,
277 lines shorter, they each wrote 9 translations out of 14, including 7
and 1 with no discrepancies.

The `--use_antigravity` rows were not measured on the frozen revision,
but on September 26 on the one published with 1.14.0: 600 lines, 257 inline
code spans, 30 block closings, 85 table rows. Shorter by 185
lines, it cannot be compared like-for-like with the other rows; the two
Antigravity rows, however, can be compared with each other. On internal links,
which the comparator does not check, `gemini-3.8-flash-medium` kept them
intact in all fourteen languages, while `gemini-3.7-flash-medium` broke them in
Italian.

### Four READMEs from well-known projects

FastAPI, Ollama, tldr-pages, and Vue.js, taken as-is from GitHub — easier
documents than the previous two. The campaign targeted struggling
models; Gemini serves as a benchmark point.

| Model                         | Scope                       | Written | No discrepancies |
| ----------------------------- | --------------------------- | ------- | ---------------- |
| `gemini-3.7-flash`            | 4 projects × 14 languages   | 56/56   | ✅ **55/56**     |
| `opencode/mimo-v2.5-free`     | 4 projects × 14 languages   | 55/56   | ❌ 47/56         |
| `grok-4.6` (subscription)| 4 projects × ar, hi, ja, zh | 16/16   | ❌ 14/16         |
| `ollama/gpt-oss-20b-32k`      | 4 projects × ar, hi, ja, zh | 15/16   | ❌ 9/16          |

### What these measurements are not

- **Not an exhaustive ranking**: OpenRouter alone offers over four hundred
  models, about fifteen were measured.
- **Indicative durations**: from three to six translations in parallel depending
  on the campaigns, and a provider's throughput varies throughout the day.
- **Time-bound observations**: models change under the same name, and your
  documents are not ours.

To rerun the benchmark on your documents, on a frozen copy of the file:

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

Both lines are necessary: without `pip install -e .`, `python -m aipmt`
responds with `No module named aipmt`.

Quality tooling, optional but recommended:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

The repository's 28 translations (README and CHANGELOG, fourteen languages)
are regenerated with `./regen_translations.sh --force` — Codex and `gpt-5.6-sol` on
the ChatGPT subscription by default, four in parallel. `REGEN_PROVIDER` and
`REGEN_MODEL` change the path: `antigravity` remains on a subscription, Google's,
and runs without exemption; a billed API (`openai`, `gemini`,
`grok`, `openrouter`) is rejected without `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` caps each job (600 s, 1,800 s on Codex and
Antigravity). Tooling details can be found in `CLAUDE.md`.

## Projects using this script

- **[jls42.org](https://jls42.org)** — personal blog published in 15 languages. Its
  [daily AI watch](https://jls42.org/fr/news) is translated daily
  by this tool, and serves as the reference document for the measurements above.

## Author

Julien LE SAUX
Email: contact@jls42.org

## License

GNU GENERAL PUBLIC LICENSE Version 3. See [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Disclaimer

This program is distributed **without any warranty**, under the terms of
sections 15 and 16 of the GPL v3: provided "as is", without warranty of
merchantability or fitness for a particular purpose, and its author cannot be
held liable for any damages resulting from its use. The text of the
license takes precedence over this summary.

- **Proofread before publishing.** Protections cover code blocks, inline
  code, URLs, anchors, and quotes in `--news` mode — neither
  headings, nor tables, nor front matter, nor the meaning of your sentences.
- **Your documents are sent to the chosen provider**, under its terms of
  service and data policy. Some free models may reuse your interactions
  for training, and Antigravity's terms allow Google to reuse them and have
  them reviewed by humans, paid subscriptions included; a local model is the only
  way that ensures no data leaves your machine.
- **API calls are billed to you.** This program does not cap expenses:
  a long document, a retry after failure, or a model that reasons heavily
  will cost more.
- **The published measurements are time-bound observations**, not guarantees.

Product and company names mentioned belong to their respective owners.
This project is not affiliated with any of them.

**Article translated from French to English with gemini-3.8-flash-medium.**
