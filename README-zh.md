# AI 驱动的 Markdown 翻译器

🌍 [法语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [英语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [西班牙语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [德语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [韩语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [阿拉伯语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [印地语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [意大利语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [荷兰语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [波兰语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [葡萄牙语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [罗马尼亚语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [瑞典语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 代码质量</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="质量门禁状态"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="安全评级"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="可靠性评级"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="可维护性评级"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="覆盖率"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="漏洞"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="缺陷"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="代码异味"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="重复行（%）"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="技术债务"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="代码行数"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy 徽章"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

一款使用 **OpenAI**、**Mistral AI**、**Claude (Anthropic)**、**Google Gemini** 和 **Grok (xAI)** 的 Markdown 文件翻译器——可通过 API、无需按量计费的 ChatGPT (Codex) 或 Grok 订阅额度，或者通过开源智能体 **OpenCode**，使用您选择的提供商：本地模型（Ollama）、免费服务、订阅服务（GitHub Copilot……）或密钥。

此 Python 脚本可将 Markdown 文件从源语言翻译成目标语言，同时保留格式、代码块和 front matter 元数据。

## 主要功能

- **多提供商**：5 种 API（OpenAI、Mistral、Claude、Gemini、Grok）+ 2 种基于订阅且无需按量计费的 CLI——Codex (ChatGPT) 和 Grok——以及可连接 OpenCode 中任意已配置提供商（包括本地模型）的 OpenCode（开源、MIT）
- **2026 年模型**：GPT-5.6 Terra、Claude Sonnet 5、Gemini 3.7 Flash
- **经济模式**：使用选项 `--eco` 调用速度更快、成本更低的模型
- **单文件**：使用选项 `--file` 翻译单个文件
- **智能分段**：根据各模型的 token 限制处理长文本
- **代码保留**：保留代码块和内联代码（`` `...` ``）
- **文件名**：使用选项 `--keep_filename` 保留原始名称
- **新闻模式**：使用选项 `--news` 保护英语引文并处理新闻文章中的旗帜符号
- **.env 配置**：支持通过文件 `.env` 配置 API 密钥
- **翻译说明**：可选择在文档末尾添加说明

## 安装

### 使用本工具

```bash
pip install ai-powered-markdown-translator
```

此后，命令 `aipmt` 可在任何位置使用。如果 Python 脚本目录不在您的 `PATH` 中，`python -m aipmt` 的作用完全相同。需要 Python 3.10 或更高版本。

若要与其他软件包隔离安装：

```bash
pipx install ai-powered-markdown-translator
```

### 为项目做贡献

进行开发仍需克隆仓库：测试、28 种翻译和全部质量工具都位于其中。

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` 是一份**完全锁定版本的 lock 文件**，精确反映经过测试的环境。`pyproject.toml` 中发布的版本范围有意设置得更宽：它们不会对您的其他软件包施加限制。

### 质量工具（可选但推荐）

本项目使用 [`pre-commit`](https://pre-commit.com) 防止提交格式错误、存在漏洞或包含秘密信息的代码。安装方式：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

已启用的 hooks：ruff（lint+format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（复杂度）、detect-secrets（API 密钥）、mypy（渐进式类型检查）、Opengrep（SAST）、pip-audit（依赖项 CVE）、unittest。详情请参阅 `CLAUDE.md` 的 _Quality / pre-commit_ 部分。

## 配置

密钥会在**三个位置**中查找，并按优先级从高到低排列。每个位置只会补充前一个位置中缺失的值。

|     | 位置                                          | 用途                                  |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 环境变量                                      | CI、容器、临时覆盖                    |
| 2   | 当前目录（或其父目录）中的 `.env`    | 项目专用密钥                          |
| 3   | `~/.config/aipmt/.env`                                | **只需安装一次，即可在所有位置使用**  |

执行 `pip install` 后，最简单的方式是使用第三个位置：

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

当变量指定绝对路径时，此文件遵循 `XDG_CONFIG_HOME`（否则按照规范要求忽略该变量）；在 Windows 下则遵循 `%APPDATA%`。

当仓库拥有自己的密钥时，第二个位置仍然有用：仓库根目录中的 `.env` 会优先于用户配置，但不会修改用户配置。环境中已定义的变量则优先于前两者：

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

如果未找到任何密钥，命令不会显示调用堆栈；它会列出这三个位置及其确切路径。

`GEMINI_API_KEY` 可作为 `GOOGLE_API_KEY` 的替代项（AI Studio 惯例）。可选变量：`XAI_BASE_URL`（xAI endpoint，默认值为 `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（每次 Anthropic 调用的秒数，默认值为 900）、`CODEX_BIN` / `CODEX_TIMEOUT`、`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`、`GROK_TRANSLATE_SANDBOX`（参阅 Grok CLI 部分）、`OPENCODE_BIN` / `OPENCODE_TIMEOUT`（参阅 OpenCode 部分）以及 `OPENROUTER_BASE_URL` / `OPENROUTER_TIMEOUT` / `OPENROUTER_PREFLIGHT_TIMEOUT`（参阅 OpenRouter 部分）。对于 `regen_translations.sh`：`REGEN_PROVIDER`（默认值为 `codex`，通过订阅使用）、`REGEN_MODEL`、`REGEN_ALLOW_PAID_API`（使用收费 API 时必须显式覆盖）以及 `REGEN_JOB_TIMEOUT`（每个任务的上限，默认 600 秒，Codex 上为 1,800 秒）。

## 使用方法

### 翻译单个文件

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### 翻译目录

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

### 使用 ChatGPT 订阅进行翻译（`--use_codex`）

此提供商不消耗任何 API 密钥：它以非交互模式驱动官方 Codex CLI，因此翻译用量会从已经付费的 ChatGPT 订阅（Plus、Pro、Business……）额度中扣除。这是 OpenAI 为此用途记录的唯一方式——`~/.codex/auth.json` 的 token 无法验证对 API Platform 的调用，而且本脚本根本不会读取它们。

**前提条件：**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

程序会按以下顺序查找二进制文件：变量 `CODEX_BIN`、`PATH`，然后是 Python 软件包 `openai-codex-cli-bin`。后者有意不包含在 `requirements.txt` 中：其大小约为 250 MB，若加入其中，会迫使所有用户安装这个仅供可选提供商使用的软件包。

**须知：**

- **不使用任何 API 密钥。** `OPENAI_API_KEY` 和 `CODEX_API_KEY` 会从子进程环境中移除，从而确保 `.env` 中存在的密钥绝不会导致翻译切换为按量计费。
- **一个分段 = 5 小时计划窗口中的一条“本地消息”。** 建议使用 `--eco`（模型 `gpt-5.6-luna`，Plus 计划每 5 小时 250–2,000 条消息），而非质量模型（`gpt-5.6-sol`，每 5 小时 10–100 条消息）。
- **比 API 调用更慢**：完整 README 约需 45 秒，而直接调用只需几秒。
- **在 CI 中禁用**（已定义 `CI` 或 `GITHUB_ACTIONS` 时）：订阅通过个人会话文件进行身份验证，将其放在共享 runner 上，等同于把一个可供其中运行的任何程序重复使用的身份凭据交给该 runner。此场景请使用 API 密钥。
- 环境变量：`CODEX_BIN`（二进制文件的显式路径）和 `CODEX_TIMEOUT`（每个分段的秒数，默认值为 `600`）。

### 使用 Grok 订阅进行翻译（`--use_grok_cli`）

原理与 `--use_codex` 相同，但使用官方 **Grok Build** CLI：翻译用量从 Grok 订阅（SuperGrok / X Premium+）中扣除，而不是按 token 计费。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**隔离——使用前请阅读。** 此提供商在结构上比 `--use_codex` **更弱**，这是有意接受的取舍：

- Codex 在 `--sandbox read-only` 中运行，这是由系统强制实施的边界。
- Grok sandbox 在许多较新的 Linux 设备上**无法生效**：自 Ubuntu 24.04 起，AppArmor 会阻止非特权 user namespace；如果 `/run/podman` 处于 `0700` 中，容器 runtime socket 的 deny-list 也会失效。而无法应用的**内置**配置会在**不受隔离的情况下静默启动**。
- 因此，脚本默认不请求任何配置，并且**绝不会静默回退**：它会显示警告。隔离依赖 CLI 的 `--deny` 规则（包括兜底规则 `*`），这是唯一经验证为 _fail-closed_ 的层——未知规则会导致启动被拒绝，而不是在不作说明的情况下移除保护。
- 若要**强制要求**操作系统 sandbox：`GROK_TRANSLATE_SANDBOX=read-only`。如果设备无法满足要求，启动将失败，这正是预期行为。

**额度**：Grok 的额度池按周计算，并与 Chat、Imagine 和 Voice **共享**，且没有任何命令能够查询额度。批量处理可能会消耗您的对话额度，却不会收到任何提示——因此并发数限制为 2，并会在 `regen_translations.sh` 中显示警告。

其他变量：`GROK_BIN`（二进制文件路径）、`GROK_TIMEOUT`（默认 900 秒）。

重新生成 28 种翻译：

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
### 使用 OpenCode 翻译，并可选择任意 provider（`--use_opencode`）

[OpenCode](https://opencode.ai) 是一个运行于终端中的**开源（MIT）**代码 agent。它不是模型 provider，而是一个**路由器**，负责连接您在 OpenCode 中配置的 provider：API key、订阅、OpenCode Zen 网关——它提供**无需账户**的免费模型——或**本地**模型。此 provider 以非交互模式驱动 `opencode run`，并将调用限制为单次往返，且不使用任何工具。

这里对其中两种方式进行了端到端测量：**Zen 网关**和本地 **Ollama**。OpenCode 宣布支持的其他方式（GitHub Copilot、LM Studio、llama.cpp）在设计上也应当能够工作，因为该 provider 只与 OpenCode 通信——但它们尚未经过验证，本 README 仅说明已经验证的内容。

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` 为**必填项**，格式为 `provider/modèle`。OpenCode 本身不是 provider，因此不会替您选择任何默认值：若使用其自身的回退机制，将会选择一个可能利用交互内容进行训练的免费模型。

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**隔离机制——脚本在每次调用时执行的操作：**

- 使用优先级高于您自身配置的内联配置（`OPENCODE_CONFIG_CONTENT`），定义一个 `aipmt` agent，并**拒绝其使用所有工具**（`permission: { "*": "deny" }`）：模型无法读取、写入或执行命令——实测中，它甚至不会尝试这样做。会话共享被禁用，`--pure` 会排除外部插件，而绝不会使用 `--auto`。
- 调用在一个**一次性空目录**中运行，并启用 `OPENCODE_DISABLE_PROJECT_CONFIG` 和 `OPENCODE_DISABLE_CLAUDE_CODE`：若不启用，OpenCode 会在每个 prompt 中注入当前目录的 `AGENTS.md` 以及您的 `~/.claude/CLAUDE.md`——实测中，放在 `AGENTS.md` 中的“每个回复都以 BANANA 结尾”指令会被应用于翻译。另一方面，`~/.config/opencode/AGENTS.md` 的全局规则仍然会被应用：OpenCode 不允许排除这些规则。
- 输出契约同时要求：退出码为 0、没有 `error` 事件、没有工具调用、最后一步以 `stop` 状态结束、文本非空，并且指定的 agent 确实已加载——未知的 `--agent` 不会导致 OpenCode 失败，它会**静默回退**到启用了工具的编码 agent。`exit 0` 在这里同样不能证明任何事情。
- **不会向子进程传递任何 aipmt key**（过滤方式与 Codex 和 Grok 相同），仅有一个明确指定的例外：OpenCode 自身的 key `OPENCODE_API_KEY`（Zen、Go）。各 provider 应在 OpenCode 中配置（`opencode auth login`、`opencode.json`），而不是在 aipmt 的 `.env` 中配置。

**注意事项：**

- **Zen 的免费模型是“stealth”模型或贡献者模型**，会不断变化，限制也没有文档说明，其交互内容可能被用于训练：非常适合公开文档，但应避免用于私密内容。实测：`opencode/mimo-v2.5-free` 可以单次完成本 README 的翻译；`opencode/big-pickle` 较慢，并且两个并发请求一直没有响应。
- **本地模型必须至少提供 16 k 上下文**——每个分段最多包含 16 000 个字符——而 Ollama 通常默认仅配置 4 096。使用 Ollama 时：创建带有 `PARAMETER num_ctx 32768` 的 `Modelfile`，然后运行 `ollama create`。质量取决于模型：在测试文件中，7B 模型颠倒了一个列表，并损坏了代码块的结束围栏，而网关模型则完整保留了所有结构。
- `--eco` 不起作用（模型由 `--model` 指定）；`--reasoning_effort` 会原样作为 OpenCode 的 `--variant` 传递，只有在模型支持时才应指定。
- OpenCode 会像记录任何其他 OpenCode 会话一样，将会话记录到其数据库（`~/.local/share/opencode/`）中。
- 环境变量：`OPENCODE_BIN`（显式指定二进制文件路径；否则依次使用 `PATH` 和 `~/.opencode/bin/opencode`）以及 `OPENCODE_TIMEOUT`（每个分段的超时秒数，默认为 `600`）。如果导出 `OPENCODE_CONFIG`，它也会生效。

**实测示例：通过 Ollama 使用本地模型**（RTX 3060 12 GB、62 GB RAM、Ollama 0.33.3）

```bash
curl -fsSL https://ollama.com/install.sh | sh   # conserve les modèles déjà téléchargés
ollama pull gpt-oss:20b                         # 13 Go, Apache 2.0 — le seul modèle local retenu ici

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

然后在 `~/.config/opencode/opencode.json` 中配置 provider：

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

`reasoningEffort: "none"` 并非无关紧要的细节：Ollama 默认会为这些模型启用推理，而 Modelfile 无法将其关闭。通过 OpenCode 实测：未使用该选项时，翻译“猫睡在地毯上”会消耗 919 个推理 token，并耗时 68 秒；启用后只需 9 个 token。

```bash
aipmt --use_opencode --model ollama/gpt-oss-20b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

对一篇真实的 589 行博客文章进行测试的结果（包含 140 个链接、21 个章节，以及由 `--news` 模式保护的 3 段英文引文），使用相同命令和三个模型：

| 模型                                     | 耗时         | 结构                                                       | 偏差                                                                                      |
| ---------------------------------------- | ------------ | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free`（Zen，免费） | 4 分 26 秒   | 与源文完全相同                                             | 无                                                                                        |
| `ollama/gemma4-12b-32k`（本地）       | 10 分 10 秒  | 链接、URL、表格、标签、粗体及内联代码均相同                | 虚构了一行引文（🇺🇸 + 改述），重复了一处署名                                                |
| `ollama/qwen3.5-9b-32k`（本地）       | 8 分 18 秒   | 链接、URL、表格及标签均相同                                | 虚构了一行引文，添加了少量粗体和内联代码，重新处理了一个分段                              |

此后，这两个本地模型均已被**淘汰**：每篇文章只要出现一次擅自改动，就足以使模型不适合用于公开发布的翻译。另有五个模型也因相同原因或超时而被淘汰（`gemma4:26b-a4b`、`qwen3.6:35b-a3b`、`ministral-3:14b`、`mistral-small3.2`、`hy-mt2:7b`）。只有 `gpt-oss:20b` 被保留——但即便是它，在处理内容密集的文章时也会遗留法语段落，参见推荐模型表。

本地翻译期间：GPU 使用率为 98%，功耗为 170 W；占用 10 GB VRAM（模型及 32 k token 缓存，没有任何内容卸载到 RAM）；Ollama 服务器使用 7 GB RAM。参数量为 90 亿至 120 亿的模型能够遵守结构，但每篇文章仍会有一次擅自改动，而网关模型一次也没有：发布前必须校对，或仅将其用于草稿。

### 通过 OpenRouter 翻译（`--use_openrouter`）

OpenRouter 是一个位于 400 多个第三方托管模型之前的**路由器**，按用量从统一额度中计费。只需一个 key，即可访问其他 provider 均未提供的模型，尤其是中国的开放模型。

```bash
# --model est OBLIGATOIRE : aucun défaut n'est choisi à votre place
aipmt --use_openrouter --model 'z-ai/glm-5.2' --file README.md \
  --target_dir . --source_lang fr --target_lang en
```

路由机制的两个特点决定了具体实现，而且两者均可通过测量验证：

- **同一模型由数十家具有不同上限的托管商提供。**对于 `z-ai/glm-5.3-flash`，共有 23 家托管商，其中一家将输出限制为 2 048 个 token：若不采取预防措施，23 次长篇翻译中会随机出现一次截断，这取决于路由结果，而且不会产生任何提示。预检会读取 `/api/v1/models/{modèle}/endpoints`，排除输出上限低于 8 000 个 token 或状态异常的托管商，然后通过 `allow_fallbacks: false` 固定使用其余托管商——否则路由器会再次转向已被排除的托管商。
- **推理按照输出费率计费。**在 `z-ai/glm-5.2` 上发送相同请求并得到“OK”回复：使用模型默认设置时产生 107 个 completion token，关闭推理后仅产生 2 个。因此，对于允许关闭推理的模型，默认会将其关闭。对于强制推理的模型——`reasoning.mandatory`，目录中 431 个模型里有 288 个——系统会使用它们声明可接受的**最低 effort**，而不是其默认设置：`z-ai/glm-5.3-flash` 的默认值为 `max`，它会在翻译完成前耗尽 32 768 个输出 token。提高 token 上限也无济于事，因为 effort 会按比例分配 token。`--reasoning_effort` 仍具有最高优先级；若对强制推理的模型使用 `none`，系统会报告错误，而不会绕过该设置。

预检采用 **fail-closed** 策略，并显示最终选择：

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

若 slug 不在目录中、目录无法访问，或没有托管商能够满足上限要求，命令会在产生任何费用之前停止。

其他要点：

- 上下文窗口来自目录，而不是某个常量：分段会真正根据它进行调整，包括上下文仅有 4 095 个 token 的模型。
- `--eco` 不起作用（模型由 `--model` 指定）。
- `finish_reason=length` 且输出为空并不表示发生截断，而是 token 预算被推理耗尽；错误消息会明确说明这一点，因为这两种情况需要采取相反的处理方式。
- 环境变量：`OPENROUTER_API_KEY`（key，可在 <https://openrouter.ai/keys> 获取）、`OPENROUTER_BASE_URL`（默认为 `https://openrouter.ai/api/v1`，且必须包含 `https://`）、`OPENROUTER_TIMEOUT`（每次调用的超时秒数，默认为 `900`）以及 `OPENROUTER_PREFLIGHT_TIMEOUT`（默认为 `30`）。

### 经济模式

使用速度更快、成本更低的模型（gpt-5.6-luna、claude-haiku-4-5、gemini-3.1-flash-lite）：

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### 选项

| 选项                     | 说明                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`          | 要翻译的单个 Markdown 文件                                                                                    |
| `--source_dir`          | 包含 Markdown 文件的源目录                                                                                    |
| `--target_dir`          | 翻译后文件的输出目录                                                                                          |
| `--source_lang`          | 源语言（默认为 `fr`）                                                                              |
| `--target_lang`          | 目标语言（默认为 `en`）                                                                            |
| `--model`          | 指定要使用的模型                                                                                              |
| `--eco`          | 使用经济型模型                                                                                                |
| `--use_mistral`          | 使用 Mistral AI API                                                                                           |
| `--use_claude`          | 使用 Claude API                                                                                               |
| `--use_gemini`          | 使用 Gemini API                                                                                               |
| `--use_codex`          | 使用 CLI Codex，并消耗 ChatGPT 订阅额度                                                                       |
| `--use_grok`          | 使用 xAI API（Grok）——需要 `XAI_API_KEY`                                                                    |
| `--use_openrouter`          | 使用 OpenRouter——需要 `OPENROUTER_API_KEY` 和 `--model fournisseur/modèle`                                                      |
| `--use_grok_cli`          | 使用 CLI Grok，并消耗 Grok 订阅额度                                                                           |
| `--use_opencode`          | 使用 OpenCode（开源）连接 OpenCode 中配置的 provider；必须指定 `--model provider/modèle`                                |
| `--force`          | 强制重新翻译                                                                                                  |
| `--keep_filename`          | 保留原始文件名                                                                                                |
| `--news`          | 新闻模式：保护英文引文，并按语言处理旗帜                                                                      |
| `--add_translation_note`          | 添加翻译说明                                                                                                  |
| `--note_position`          | 说明位置：`top`、`bottom`（默认）或 `both`                                          |
| `--note_format`          | 说明格式：`legacy`（默认，粗体段落）或 `marker`                                                 |
| `--include_model`          | 在输出文件中包含模型名称                                                                                      |
| `--reasoning_effort`          | GPT-5.x 推理 effort：`none`/`low`/`medium`/`high`/`xhigh`           |

> **七个 provider flag 互斥。**此前，同时使用两个 flag 会被静默接受，并解析为首个被检查的选项：原本要求使用订阅额度（`--use_codex`、`--use_grok_cli`）的翻译，可能在毫无警告的情况下转为按用量计费。现在，`argparse` 会拒绝这种组合。

### 翻译说明：位置与格式

使用 `--add_translation_note` 时，translator 可以将说明放在顶部、底部或两个位置，并可将其渲染为向后兼容的纯文本格式，或可供 Markdown 插件处理的 `marker` 格式。

**位置**（`--note_position`）：

- `bottom`（默认）：按照以往方式将说明放在文件末尾。
- `top`：将说明插入 **YAML frontmatter 之后**（兼容 Astro Content Collections、gray-matter 等）。
- `both`：同时在顶部和底部插入说明（只调用一次 LLM，两处位置复用相同内容）。

**格式**（`--note_format`）：

- `legacy`（默认）：粗体段落 `**...**`——行为与 v1.8 完全一致，逐字节相同。兼容 Hugo、GitHub、GitLab 以及所有 Markdown renderer。
- `marker`：不可见的 Markdown link reference definition（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），后接粗体 blockquote。可在 GitHub/GitLab 上直接阅读，也可在构建时由 Astro 端的 remark 插件处理，以生成样式化横幅（参见博客 jls42.org）。

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

### 默认模型（2026）

| Provider   | 质量模式（默认）                         | 经济模式（`--eco`）   |
| ---------- | ---------------------------------------- | ----------------------------- |
| OpenAI     | `gpt-5.6-terra`                          | `gpt-5.6-luna`                |
| Claude     | `claude-sonnet-5`                          | `claude-haiku-4-5`                |
| Mistral    | `mistral-large-latest`                          | `mistral-small-latest`                |
| Gemini     | `gemini-3.7-flash`                          | `gemini-3.1-flash-lite`                |
| Codex      | `gpt-5.6-sol`                          | `gpt-5.6-luna`                |
| Grok API   | `grok-4.6`                          | `grok-4.3`                |
| Grok CLI   | `grok-4.6`                          | `grok-4.5`                |
| OpenCode   | 必须指定 `--model provider/modèle`                 | 相同——`--eco` 不起作用 |
| OpenRouter | 必须指定 `--model fournisseur/modèle`                 | 相同——`--eco` 不起作用 |
## 哪些模型表现可靠

一个能很好翻译单个段落的模型，不一定能保留整篇文档的结构。这些数据来自**实际执行的翻译**，使用的是上文所示的命令，覆盖三组文档和十四种目标语言：en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi。

这里有两列数据，而且含义并不相同。**已写入**统计成功完成的翻译——脚本的静默失败防护检查允许文件通过。**无偏差**统计结构与源文档完全一致的翻译：章节、链接、URL、代码块与行内代码、表格、引用和标志均保持一致。

### 高密度博客文章，`--news` 模式

589 行、140 个链接、21 个章节、3 段受保护的英文引用。这是三份文档中要求最高的一份：`--news` 模式在 Markdown 结构约束之外，还增加了对标志和引用的约束。

| 模型                            | 访问方式              | 已写入 | 无偏差 | 每种语言中位耗时 |
| --------------------------------- | ------------------ | ------- | ---------- | -------------- |
| `gemini-3.7-flash`                | Google API         | 14/14   | **14/14**  | 1 分 18 秒     |
| `gpt-5.6-sol` (`--use_codex`)     | ChatGPT 订阅 | 14/14   | **14/14**  | 11 分 28 秒    |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14   | **14/14**  | 5 分 37 秒     |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14   | 13/14      | 26 分 23 秒    |
| `z-ai/glm-5.3-flash`              | OpenRouter         | 12/14   | 12/14      | 15 分 49 秒    |
| `qwen/qwen3.5-27b`                | OpenRouter         | 7/9     | 7/9        | 20 分 33 秒    |
| `claude-sonnet-5`                 | Anthropic API      | 14/14   | 11/14      | 6 分 31 秒     |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14   | 11/14      | 9 分 27 秒     |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14   | 7/14       | 10 分 09 秒    |
| `ollama/gpt-oss-20b-32k`          | 本地              | 10/14   | 7/14       | 12 分 39 秒    |
| `mistral-large-latest`            | Mistral API        | 11/14   | 5/14       | 5 分 32 秒     |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14    | 3/14       | 37 分 27 秒    |
| `grok-4.6` (`--use_grok_cli`)     | Grok 订阅    | 1/14    | 1/14       | 23 分 11 秒    |
| `moonshotai/kimi-k2.6`            | OpenRouter         | 1/4     | 1/4        | 23 分 00 秒    |

有两批测试因**额度不足而中断**，分母也反映了这一点：`qwen3.5-27b` 在完成九种语言后停止，`kimi-k2.6` 则在完成四种语言后停止——后者还经历了一次四十分钟超时和两次拒绝，每种语言的成本接近 0.33 美元。

关于 OpenRouter 的数据还需说明测试方法：这些数据是在 `--use_openrouter` 尚不存在时，使用**路由器默认设置**测得的。此后，`z-ai/glm-5.2` 使用随附的 provider 并关闭推理重新测试，仍得到了完全相同的 14/14。`z-ai/glm-5.3-flash` 曾因路由器默认输出预算耗尽而失败两次；现在，provider 会要求这些模型采用其可接受的最低推理强度，而针对出错语言的复核测试均已通过。

### 本项目的 README，标准 Markdown

508 行、219 处行内代码、40 个代码块围栏、45 行表格。这里没有使用 `--news` 模式：难点来自代码密度。

| 模型                        | 已写入 | 无偏差 | 每种语言中位耗时 |
| ----------------------------- | ------- | ---------- | -------------- |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14   | 11/14      | 1 分 22 秒     |
| `gemini-3.7-flash`            | 14/14   | 13/14      | 21 秒           |
| `gpt-5.6-sol` (`--use_codex`) | 14/14   | 12/14      | 2 分 04 秒     |
| `opencode/mimo-v2.5-free`     | 9/14    | 7/14       | 3 分 25 秒     |
| `ollama/gpt-oss-20b-32k`      | 9/14    | 1/14       | 3 分 38 秒     |

### 四个知名项目的 README

FastAPI、Ollama、tldr-pages 和 Vue.js，均直接取自 GitHub。这些文档比前两份**更容易**，表格也印证了这一点。

| 模型                    | 测试范围                  | 已写入 | 无偏差 |
| ------------------------- | -------------------------- | ------- | ---------- |
| `opencode/mimo-v2.5-free` | 4 个项目 × 14 种语言     | 55/56   | 47/56      |
| `grok-4.6`（订阅）   | 4 个项目 × ar、hi、ja、zh | 16/16   | 14/16      |
| `ollama/gpt-oss-20b-32k`  | 4 个项目 × ar、hi、ja、zh | 15/16   | 9/16       |

### 我们从中得到的结论

- **有三个模型在两份高密度文档中从未丢失信息**：`gemini-3.7-flash`、通过 ChatGPT 订阅使用的 `gpt-5.6-sol`，以及通过 OpenRouter 使用的 `z-ai/glm-5.2`。它们在标准模式下唯一的偏差，是一两种语言中漏掉了一对 `**`，从未漏掉 URL、代码块或引用。
- **决定性因素是文档密度，而不是 `--news` 模式。** 通过订阅使用的 Grok 在博客文章上 14 次失败了 13 次，却在 16 份公开 README 中成功完成了 14 份：其失败原因是处理长片段时脱离任务，这一点已通过复核测试确认——单独翻译该段落时结果正确。
- **非拉丁文字并不是预期中的分界线。** `gpt-oss` 在阿拉伯语、日语、波兰语**以及罗马尼亚语**中都留下了法语段落；Mistral 和 MiMo 则只在非拉丁文字中丢失行内代码。
- **关闭推理不会损害质量。** `z-ai/glm-5.2` 在两种条件下都完成了十四种语言且毫无偏差——先使用路由器默认启用的推理，再通过 `--use_openrouter` 将其关闭——但计费的输出 token 减少了十八倍。这项数据正是 provider 采用该默认设置的依据。
- **速度慢的模型并不意味着更可靠。** `deepseek-v4-flash-0731` 每种语言耗时 37 分钟，却只完成了 14 次翻译中的 4 次；`qwen3.8-flash` 耗时 26 分钟，结果接近完美；Gemini 仅用 1 分 18 秒便做到了零失误。

### 这张表不代表什么

- **这不是一份全面排名。** 仅 OpenRouter 就提供四百多个模型；此处测试了大约十五个。某个模型没有出现，并不说明其质量如何，只表示它尚未接受测试。
- **这些数据有明确日期**：2026 年 9 月 4 日和 5 日。同名模型会发生变化，托管方会调整量化方式和上限，而且每周都会发布新模型。
- **耗时不能用于排名。** 不同批次同时执行的翻译数量在 3 到 6 个之间，而且供应商的吞吐量会随一天中的时段变化。这些数据只能提供大致量级，不能用于直接比较。
- **结果既取决于模型，也取决于文档。** 同一个模型在一篇文章上成功完成十四种语言，却在这份 README 上只完成九种。您的文件与我们的不同。
- **正确的方法仍然是在您自己的环境中测量**：将您的一份文档翻译成目标语言，然后比较结构——章节数、链接数、不同 URL 的数量、代码块数、行内代码数和表格行数。这正是上述测试方案所做的事情，而且只需围绕 `aipmt` 编写一个循环即可完成。

## 使用此脚本的项目

- **[jls42.org](https://jls42.org)** - 多语言个人博客（15 种语言）

## 作者

Julien LE SAUX
电子邮件：contact@jls42.org

## 许可证

GNU GENERAL PUBLIC LICENSE 第 3 版。请参阅 [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)。

**使用 gpt-5.6-sol 将文章从法语翻译成中文。**
