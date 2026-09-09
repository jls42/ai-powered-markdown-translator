# AI-Powered Markdown Translator

🌍 [French](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Spanish](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Chinese](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [German](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japanese](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Korean](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Arabic](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italian](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Dutch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polish](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Portuguese](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Romanian](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Swedish](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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

Markdown file translator using **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini**, and **Grok (xAI)**—via API, through a ChatGPT (Codex) or Grok subscription quota with no usage-based billing, or through **OpenCode**, the open-source agent, with the provider of your choice: local model (Ollama), free, subscription-based (GitHub Copilot…), or API key.

This Python script translates Markdown files from a source language into a target language while preserving formatting, code blocks, and front matter metadata.

## Key Features

- **Multi-Provider**: 5 APIs (OpenAI, Mistral, Claude, Gemini, Grok) + 2 subscription-based CLIs with no usage-based billing—Codex (ChatGPT) and Grok—+ OpenCode (open source, MIT) with any provider configured in OpenCode, including a local model
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

### To use the tool

```bash
pip install ai-powered-markdown-translator
```

The `aipmt` command is then available everywhere. If Python's scripts directory
is not in your `PATH`, `python -m aipmt` does exactly the same
thing. Python 3.10 or newer.

For an installation isolated from the rest of your packages:

```bash
pipx install ai-powered-markdown-translator
```

### To contribute to the project

The cloned repository is still required for development: it contains the tests,
the 28 translations, and all the quality tooling.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` is a **fully pinned lock**, an exact snapshot of
the tested environment. The published constraints in `pyproject.toml` are
intentionally broader: they do not impose anything on your other packages.

### Quality tooling (optional but recommended)

The project uses [`pre-commit`](https://pre-commit.com) to prevent committing poorly formatted or vulnerable code, or code containing a secret. Installation:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Active hooks: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexity), detect-secrets (API keys), mypy (progressive typing), Opengrep (SAST), pip-audit (dependency CVEs), unittest. See the _Quality / pre-commit_ section of `CLAUDE.md` for details.

## Configuration

Keys are searched for in **three locations**, from highest to lowest priority.
Each one only fills in values left empty by the previous one.

|     | Where                                            | Purpose                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Environment variables                     | CI, containers, one-time overrides |
| 2   | `.env` in the current directory (or a parent) | a project-specific key            |
| 3   | `~/.config/aipmt/.env`                        | **installed once, applies everywhere**   |

The simplest option after a `pip install` is the third:

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

This file follows `XDG_CONFIG_HOME` when the variable specifies an absolute path
(otherwise it is ignored, as required by the specification), and `%APPDATA%`
on Windows.

The second remains useful when a repository has its own key: a `.env` at its root
then takes precedence over the user configuration without modifying it. And a
variable already defined in the environment takes precedence over both:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

If no key is found, the command does not display a call trace: it
lists the three locations with their exact paths.

`GEMINI_API_KEY` is accepted as an alternative to `GOOGLE_API_KEY` (AI
Studio convention). Optional variables: `XAI_BASE_URL` (xAI endpoint, default
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (seconds per Anthropic call, default
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (see the Grok CLI section), `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (see the OpenCode section), and `OPENROUTER_BASE_URL` /
`OPENROUTER_TIMEOUT` / `OPENROUTER_PREFLIGHT_TIMEOUT` (see the
OpenRouter section). For
`regen_translations.sh`: `REGEN_PROVIDER` (default `codex`, subscription-based),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (mandatory override for a billed API),
and `REGEN_JOB_TIMEOUT` (per-job limit, default 600 s, 1,800 s on Codex).

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

# Avec OpenRouter (routeur vers ~430 modèles ; --model obligatoire)
aipmt --use_openrouter --model 'z-ai/glm-5.2' --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### Translate using your ChatGPT subscription (`--use_codex`)

This provider does not use any API key: it drives the official Codex CLI in
non-interactive mode, so translation usage is deducted from the quota of the
already-paid ChatGPT subscription (Plus, Pro, Business…). This is the only method
documented by OpenAI for this use case—the tokens from `~/.codex/auth.json` do not
authenticate Platform API calls and are never read by this script.

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
  present in `.env` can never switch translation to usage-based
  billing.
- **One segment = one “local message”** in the plan's 5-hour window.
  Use `--eco` (model `gpt-5.6-luna`, 250–2,000 messages/5 h on Plus)
  rather than the quality model (`gpt-5.6-sol`, 10–100 messages/5 h).
- **Slower** than an API call: expect ~45 s for a complete README, compared with
  a few seconds directly.
- **Rejected in CI** (`CI` or `GITHUB_ACTIONS` defined): the subscription
  authenticates through a personal session file, and placing it on a shared runner
  amounts to storing a reusable identity there for anything running on it.
  Use an API key for this path.
- Environment variables: `CODEX_BIN` (explicit binary path) and
  `CODEX_TIMEOUT` (seconds per segment, default `600`).

### Translate using your Grok subscription (`--use_grok_cli`)

The same principle as `--use_codex`, using the official **Grok Build** CLI:
translation usage is deducted from the Grok subscription (SuperGrok / X Premium+)
instead of being billed per token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Containment—read before use.** This provider is structurally **weaker**
than `--use_codex`, and this is intentional:

- Codex runs in `--sandbox read-only`, a boundary enforced by the system.
- Grok's sandbox **cannot be applied** on many recent Linux
  systems: AppArmor has blocked unprivileged user namespaces since Ubuntu
  24.04, and the container runtime socket denylist fails if
  `/run/podman` is in `0700`. Yet a **built-in** profile that cannot
  be applied starts **unconfined, silently**.
- The script therefore requests no profile by default and **never falls back
  silently**: it displays a warning. Containment relies on the CLI's
  `--deny` rules (including the catch-all `*`), the only measured
  _fail-closed_ layer—an unknown rule prevents startup rather than
  removing protection without notice.
- To **require** the OS sandbox: `GROK_TRANSLATE_SANDBOX=read-only`.
  Startup will fail if the machine cannot honor it, which is the
  intended behavior.

**Quota**: the Grok pool is **weekly and shared** with Chat, Imagine, and
Voice, and no command can display it. Batch processing can therefore
reduce your conversational usage without any notification—hence
concurrency limited to 2 and a warning in `regen_translations.sh`.

Other variables: `GROK_BIN` (binary path), `GROK_TIMEOUT` (default 900 s).

To regenerate the 28 translations:

```bash
# Défaut : Codex sur l'abonnement ChatGPT, modèle qualité gpt-5.6-sol, 0 € à l'usage
./regen_translations.sh --force

# Le modèle éco de Codex, si le volume l'impose
REGEN_MODEL=gpt-5.6-luna ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Une API facturée (openai, gemini, grok, openrouter) est REFUSÉE sans cette dérogation nommée
REGEN_PROVIDER=openai REGEN_ALLOW_PAID_API=1 ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force

# Via OpenRouter : API facturée, donc dérogation ET modèle obligatoires
REGEN_PROVIDER=openrouter REGEN_ALLOW_PAID_API=1 REGEN_MODEL=z-ai/glm-5.2 ./regen_translations.sh --force
```
### Translate with OpenCode, using the provider of your choice (`--use_opencode`)

[OpenCode](https://opencode.ai) is an **open-source (MIT)** coding agent for the
terminal. It is not a model provider but a **router** to those
you have configured in OpenCode itself: an API key, a subscription,
the OpenCode Zen gateway—which serves free models **without an account**—or
a **local** model. This provider runs `opencode run` in non-interactive mode and
confines the call to a single round trip, without any tools.

Two of these routes have been measured end-to-end here: the **Zen gateway** and
local **Ollama**. The others advertised by OpenCode (GitHub Copilot, LM Studio,
llama.cpp) should work by design, since the provider only communicates
with OpenCode—but they have not been tested, and this README only states
what has been verified.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` is **required**, in `provider/modèle` format. OpenCode is not
a provider, and no default is selected on your behalf: its own fallback
would be a free model whose interactions may be used for training.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Confinement—what the script does on every call:**

- An inline configuration (`OPENCODE_CONFIG_CONTENT`), which takes precedence over
  yours, defines a `aipmt` agent whose **tools are all denied**
  (`permission: { "*": "deny" }`): the model cannot read, write, or
  run commands—and, when measured, it did not even try. Session sharing
  is disabled, `--pure` excludes external plugins, never `--auto`.
- The call runs in a **disposable, empty directory**, with the
  `OPENCODE_DISABLE_PROJECT_CONFIG` and `OPENCODE_DISABLE_CLAUDE_CODE` switches: without
  them, OpenCode injects the current directory's `AGENTS.md`
  and your `~/.claude/CLAUDE.md` into every prompt—when measured, an instruction to “end every response
  with BANANA” placed in a `AGENTS.md` was applied to the translation. The
  global `~/.config/opencode/AGENTS.md` rules, however, remain
  in effect: OpenCode does not allow them to be excluded.
- The output contract requires all of the following: exit code 0, no
  `error` event, no tool call, a final step completed with `stop`, non-empty
  text, and the agent actually loaded—an unknown `--agent` does not cause
  OpenCode to fail; it **silently falls back** to the coding agent, with tools
  enabled. A `exit 0` proves nothing here either.
- **No aipmt key is passed** to the subprocess (the same filtering
  as with Codex and Grok), with one named exception: `OPENCODE_API_KEY`,
  OpenCode's own key (Zen, Go). Providers are configured in
  OpenCode (`opencode auth login`, `opencode.json`), not in aipmt's `.env`.

**Good to know:**

- **Zen's free models are “stealth” or contributor models**,
  subject to change, with undocumented limits, and their interactions may be used for
  training: ideal for public documentation, but best avoided for
  private content. Measured: `opencode/mimo-v2.5-free` translates this README in a
  single pass; `opencode/big-pickle` is slower, and two simultaneous requests to it
  remained unanswered.
- **A local model must provide at least 16k context**—segments are
  up to 16,000 characters long—while Ollama often configures 4,096 by
  default. With Ollama: a `Modelfile` with `PARAMETER num_ctx 32768`, then
  `ollama create`. Quality depends on the model: a 7B reversed a list and
  damaged a code-block fence in a test file, whereas a gateway
  model preserved everything.
- `--eco` has no effect (the model is the one in `--model`);
  `--reasoning_effort` is passed through unchanged as OpenCode's `--variant` and should
  only be requested if the model recognizes it.
- Sessions are logged by OpenCode in its database
  (`~/.local/share/opencode/`), like any OpenCode session.
- Environment variables: `OPENCODE_BIN` (explicit binary path,
  otherwise `PATH` then `~/.opencode/bin/opencode`) and `OPENCODE_TIMEOUT`
  (seconds per segment, default `600`). If `OPENCODE_CONFIG` is
  exported, it is not read by `aipmt`: it is passed through unchanged to OpenCode, which honors it.

**Measured example: a local model via Ollama** (RTX 3060 12 GB, 62 GB RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # conserve les modèles déjà téléchargés
ollama pull gpt-oss:20b                         # 13 Go, Apache 2.0 — le seul modèle local retenu ici

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

Then the provider in `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` is not a minor detail: Ollama enables reasoning by
default on these models, and a Modelfile cannot disable it. Measured
through OpenCode: without the option, “The cat sleeps on the rug” costs 919 reasoning
tokens and 68 seconds; with it, 9 tokens.

```bash
aipmt --use_opencode --model ollama/gpt-oss-20b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Results on a real 589-line blog post (140 links, 21 sections,
3 English quotations protected by `--news` mode), same command, three
models:

| Model                                    | Duration     | Structure                                                  | Deviations                                                                                |
| ---------------------------------------- | ------------ | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, free) | 4 min 26 s  | identical to the source                                    | none                                                                                      |
| `ollama/gemma4-12b-32k` (local)          | 10 min 10 s | identical links, URLs, tables, tags, bold, and inline code | one fabricated quotation line (🇺🇸 + paraphrase), one duplicated attribution              |
| `ollama/qwen3.5-9b-32k` (local)          | 8 min 18 s  | identical links, URLs, tables, and tags                    | one fabricated quotation line, some added bold and inline code, one segment processed again |

These two local models have since been **discarded**: one liberty per article
is enough to disqualify a model for published translation. Five others were
discarded for the same reasons or for timing out (`gemma4:26b-a4b`,
`qwen3.6:35b-a3b`, `ministral-3:14b`, `mistral-small3.2`, `hy-mt2:7b`). Only
`gpt-oss:20b` was retained—and even it leaves passages in French in
a dense article; see the recommended-models table.

During local translation: GPU at 98% and 170 W, 10 GB of VRAM in use
(model and 32k-token cache, nothing offloaded to RAM), 7.5 GB of RAM for the
Ollama server. A model with 9 to 12 billion parameters preserves the
structure but takes one liberty per article, whereas the gateway model
took none: proofread before publication, or reserve it for drafts.

### Translate via OpenRouter (`--use_openrouter`)

OpenRouter is a **router** in front of more than 400 third-party-hosted models,
billed by usage against a single credit balance. With one key, it provides access to models
that none of the other providers expose, notably open Chinese models.

```bash
# --model est OBLIGATOIRE : aucun défaut n'est choisi à votre place
aipmt --use_openrouter --model 'z-ai/glm-5.2' --file README.md \
  --target_dir . --source_lang fr --target_lang en
```

Two routing characteristics shaped the implementation, and both are
measurable:

- **The same model is served by dozens of hosts with different
  limits.** For `z-ai/glm-5.3-flash`, there are 23 hosts, including one capped at
  2,048 output tokens: without precautions, one long translation out of 23 would be
  truncated, depending randomly on routing and without any signal. A preflight reads
  `/api/v1/models/{modèle}/endpoints`, excludes hosts with fewer than 8,000 output
  tokens or degraded status, then pins the others with
  `allow_fallbacks: false`—without it, the router would fall back to an
  excluded host.
- **Reasoning is billed at the output-token rate.** Same request on
  `z-ai/glm-5.2`, response “OK”: 107 completion tokens with the model's default,
  2 with reasoning disabled. It is therefore disabled by default for models
  that allow it. Those that require it—`reasoning.mandatory`, 288 of the catalog's 431
  models—receive the **lowest effort level they declare
  they accept**, rather than their default setting: `z-ai/glm-5.3-flash` defaults to
  `max`, and it exhausted all 32,768 output tokens before the
  translation ended. Increasing the allowance would not have helped, since effort allocates a
  percentage of it. `--reasoning_effort` still takes precedence, and `none` on a model
  that requires reasoning is reported rather than bypassed.

The preflight is **fail-closed** and displays what it selected:

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

A slug missing from the catalog, an unreachable catalog, or the absence of a host
meeting the limit stops the command before any billing occurs.

Other points:

- The context window comes from the catalog, not a constant: segmentation
  actually adapts to it, including for models with 4,095 tokens.
- `--eco` has no effect (the model is the one in `--model`).
- `finish_reason=length` with empty output is not truncation but a
  budget consumed by reasoning; the message says so, because the two
  cases require opposite actions.
- Environment variables: `OPENROUTER_API_KEY` (key, at
  <https://openrouter.ai/keys>), `OPENROUTER_BASE_URL` (default
  `https://openrouter.ai/api/v1`, `https://` required), `OPENROUTER_TIMEOUT`
  (seconds per call, default `900`), and `OPENROUTER_PREFLIGHT_TIMEOUT`
  (default `30`).

### Economy mode

Uses faster, less expensive models (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Options

| Option                   | Description                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Single Markdown file to translate                                                                             |
| `--source_dir`           | Source directory containing Markdown files                                                                    |
| `--target_dir`           | Output directory for translated files                                                                         |
| `--source_lang`          | Source language (default: `fr`)                                                                     |
| `--target_lang`          | Target language (default: `en`)                                                                     |
| `--model`                | Specific model to use                                                                                         |
| `--eco`                  | Use economy models                                                                                            |
| `--use_mistral`          | Use the Mistral AI API                                                                                        |
| `--use_claude`           | Use the Claude API                                                                                            |
| `--use_gemini`           | Use the Gemini API                                                                                            |
| `--use_codex`            | Use the Codex CLI against the ChatGPT subscription quota                                                      |
| `--use_grok`             | Use the xAI API (Grok)—requires `XAI_API_KEY`                                                               |
| `--use_openrouter`       | Use OpenRouter—requires `OPENROUTER_API_KEY` and `--model fournisseur/modèle`                                                       |
| `--use_grok_cli`         | Use the Grok CLI against the Grok subscription quota                                                          |
| `--use_opencode`         | Use OpenCode (open source) with the provider configured in OpenCode; requires `--model provider/modèle`                 |
| `--force`                | Force retranslation                                                                                           |
| `--keep_filename`        | Preserve the original filename                                                                                |
| `--news`                 | News mode: protects EN quotations and handles flags by language                                               |
| `--add_translation_note` | Add a translation note                                                                                        |
| `--note_position`        | Note position: `top`, `bottom` (default), or `both`                                 |
| `--note_format`          | Note format: `legacy` (default, bold paragraph) or `marker`                                     |
| `--include_model`        | Include the model name in the output file                                                                     |
| `--reasoning_effort`     | GPT-5.x reasoning effort: `none`/`low`/`medium`/`high`/`xhigh`    |

> **The eight provider flags are mutually exclusive.** Combining two
> was previously accepted silently and resolved to the first one checked: a
> translation requested against a subscription quota (`--use_codex`, `--use_grok_cli`)
> could therefore incur usage-based billing without any warning.
> `argparse` now rejects the combination.

### Translation note: positions and formats

With `--add_translation_note`, the translator can place the note at the top, at the bottom, or in both locations, and render it either as plain text (backward-compatible) or in a `marker` format consumable by a Markdown plugin.

**Position** (`--note_position`):

- `bottom` (default): note at the end of the file, as before.
- `top`: note inserted **after the YAML front matter** (safe for Astro Content Collections, gray-matter, etc.).
- `both`: note inserted at the top AND bottom (a single LLM call, with content reused for both placements).

**Format** (`--note_format`):

- `legacy` (default): bold paragraph `**...**`—behavior strictly identical to v1.8, byte-for-byte. Compatible with Hugo, GitHub, GitLab, and any Markdown renderer.
- `marker`: invisible Markdown link reference definition (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) followed by a bold blockquote. Natively readable on GitHub/GitLab and usable at build time by an Astro-side remark plugin to produce a styled banner (see the jls42.org blog).

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

| Provider   | Quality (default)                        | Economy (`--eco`) |
| ---------- | ---------------------------------------- | ------------------------- |
| OpenAI     | `gpt-5.6-terra`                          | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                        | `claude-haiku-4-5`        |
| Mistral    | `mistral-large-latest`                   | `mistral-small-latest`    |
| Gemini     | `gemini-3.7-flash`                       | `gemini-3.1-flash-lite`   |
| Codex      | `gpt-5.6-sol`                            | `gpt-5.6-luna`            |
| Grok API   | `grok-4.6`                               | `grok-4.3`                |
| Grok CLI   | `grok-4.6`                               | `grok-4.5`                |
| OpenCode   | `--model provider/modèle` required       | same—`--eco` has no effect |
| OpenRouter | `--model fournisseur/modèle` required | same—`--eco` has no effect |
## Which models hold up

A model that translates a paragraph well does not necessarily preserve the structure
of an entire document. These measurements come from **translations that were actually
run**, using the command shown above, on three document sets
and fourteen target languages: en, es, de, it, pt, nl, pl, sv, ro, ja,
ko, zh, ar, hi.

Two columns, and they do not mean the same thing. **Written** counts the
translations that complete successfully—the script's silent-failure safeguards
allow the file through. **Exact match** counts those whose structure is
identical to the source: same sections, same links, same URLs, same blocks and
inline code, same tables, same blockquotes, same flags.

### Dense blog post, `--news` mode

589 lines, 140 links, 21 sections, 3 protected English quotations. This is the
most demanding of the three documents: `--news` mode adds flag and quotation
constraints on top of the Markdown structure.

| Model                             | Access               | Written | Exact match | Median/language |
| --------------------------------- | -------------------- | ------- | ----------- | --------------- |
| `gemini-3.7-flash`                | Google API           | 14/14   | **14/14**   | 1 min 18 s      |
| `gpt-5.6-sol` (`--use_codex`)     | ChatGPT subscription | 14/14   | **14/14**   | 11 min 28 s     |
| `z-ai/glm-5.2`                    | OpenRouter           | 14/14   | **14/14**   | 5 min 37 s      |
| `qwen/qwen3.8-flash`              | OpenRouter           | 14/14   | 13/14       | 26 min 23 s     |
| `z-ai/glm-5.3-flash`              | OpenRouter           | 12/14   | 12/14       | 15 min 49 s     |
| `qwen/qwen3.5-27b`                | OpenRouter           | 7/9     | 7/9         | 20 min 33 s     |
| `claude-sonnet-5`                 | Anthropic API        | 14/14   | 11/14       | 6 min 31 s      |
| `opencode/mimo-v2.5-free`         | OpenCode Zen         | 13/14   | 11/14       | 9 min 27 s      |
| `qwen/qwen3.7-flash`              | OpenRouter           | 13/14   | 7/14        | 10 min 09 s     |
| `ollama/gpt-oss-20b-32k`          | local                | 10/14   | 7/14        | 12 min 39 s     |
| `mistral-large-latest`            | Mistral API          | 11/14   | 5/14        | 5 min 32 s      |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter           | 4/14    | 3/14        | 37 min 27 s     |
| `grok-4.6` (`--use_grok_cli`)     | Grok subscription    | 1/14    | 1/14        | 23 min 11 s     |
| `moonshotai/kimi-k2.6`            | OpenRouter           | 1/4     | 1/4         | 23 min 00 s     |

Two batches were **stopped due to insufficient credit**, as reflected in their
denominators: `qwen3.5-27b` stopped at nine languages, and `kimi-k2.6` at
four—the latter after a forty-minute timeout and two refusals, at nearly
$0.33 per language.

One methodological caveat regarding the OpenRouter rows: they were measured with
the router's **default settings**, before `--use_openrouter` existed.
`z-ai/glm-5.2` has since been measured again with the bundled provider and reasoning
disabled, producing exactly the same 14/14 result. `z-ai/glm-5.3-flash` failed twice
because the router's default output budget was exhausted; the provider now requests
the lowest reasoning effort these models accept, and retesting the affected
languages succeeds.

### This project's README, standard Markdown

508 lines, 219 inline code spans, 40 block fences, 45 table lines. There is no
`--news` mode here: the difficulty comes from the density of code.

| Model                         | Written | Exact match | Median/language |
| ----------------------------- | ------- | ----------- | --------------- |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14   | 11/14       | 1 min 22 s      |
| `gemini-3.7-flash`            | 14/14   | 13/14       | 21 s            |
| `gpt-5.6-sol` (`--use_codex`) | 14/14   | 12/14       | 2 min 04 s      |
| `opencode/mimo-v2.5-free`     | 9/14    | 7/14        | 3 min 25 s      |
| `ollama/gpt-oss-20b-32k`      | 9/14    | 1/14        | 3 min 38 s      |

### Four READMEs from well-known projects

FastAPI, Ollama, tldr-pages, and Vue.js, taken directly from GitHub. These documents
are **easier** than the previous two, as the table shows.

| Model                     | Scope                      | Written | Exact match |
| ------------------------- | -------------------------- | ------- | ----------- |
| `opencode/mimo-v2.5-free` | 4 projects × 14 languages     | 55/56   | 47/56       |
| `grok-4.6` (subscription)   | 4 projects × ar, hi, ja, zh | 16/16   | 14/16       |
| `ollama/gpt-oss-20b-32k`  | 4 projects × ar, hi, ja, zh | 15/16   | 9/16        |

### Key takeaways

- **Three models never lost any information** across the two dense documents:
  `gemini-3.7-flash`, `gpt-5.6-sol` through the ChatGPT subscription, and
  `z-ai/glm-5.2` through OpenRouter. Their only discrepancies in standard mode
  were a pair of `**` markers omitted in one or two languages, never a URL,
  code block, or quotation.
- **The differentiating factor is document density, not `--news` mode.**
  Grok through a subscription fails 13 times out of 14 on the blog post and
  succeeds on 14 public READMEs out of 16: its failure is caused by losing track
  in a long segment, as confirmed by retesting—the isolated passage is translated
  correctly.
- **Non-Latin scripts are not the dividing line one might expect.** `gpt-oss`
  leaves passages in French in Arabic, Japanese, Polish, **and Romanian**; Mistral
  and MiMo lose inline code only in non-Latin scripts.
- **Disabling reasoning does not reduce quality.** `z-ai/glm-5.2` completes
  fourteen languages without a single discrepancy under both conditions—with
  reasoning enabled by the router's default, then disabled through
  `--use_openrouter`—while using eighteen times fewer billed output tokens. This
  measurement justifies the provider's default setting.
- **A slow model is not necessarily a reliable model.** `deepseek-v4-flash-0731` takes 37
  minutes per language for 4 successful translations out of 14, `qwen3.8-flash`
  takes 26 minutes for an almost perfect result, and Gemini takes 1 minute 18
  seconds for a flawless result.

### What this table is not

- **This is not an exhaustive ranking.** OpenRouter alone offers more than four
  hundred models; around fifteen were measured here. A model's absence says
  nothing about its quality, only that it was not tested.
- **These measurements are dated**: September 4 and 5, 2026. Models change
  under the same name, hosting providers adjust quantization and limits, and
  new models are released every week.
- **The durations do not constitute a ranking.** Parallelism ranged from 3 to 6
  simultaneous translations depending on the test run, and a provider's throughput
  varies throughout the day. They provide an order of magnitude, not a comparison.
- **A result depends as much on the document as on the model.** The same model
  succeeds in fourteen languages on one article and nine on this README. Your files
  are not ours.
- **The right approach is still to measure on your own files**: translate one of
  your documents into your target languages, then compare the structure—the number
  of sections, links, distinct URLs, code blocks, inline code spans, and table
  lines. That is exactly what the protocol above does, and it fits into a single
  loop over `aipmt`.

## Projects using this script

- **[jls42.org](https://jls42.org)** - Multilingual personal blog (15 languages)

## Author

Julien LE SAUX
Email: contact@jls42.org

## License

GNU GENERAL PUBLIC LICENSE Version 3. See [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Article translated from fr to en with gpt-5.6-sol.**
