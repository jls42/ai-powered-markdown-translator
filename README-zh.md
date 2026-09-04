# AI 驱动的 Markdown 翻译器

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 代码质量</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="质量门状态"></a>
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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="重复代码行 (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="技术债务"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="代码行数"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy 徽章"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

使用 **OpenAI**、**Mistral AI**、**Claude (Anthropic)**、**Google Gemini** 和 **Grok (xAI)** 的 Markdown 文件翻译器——可通过 API、使用 ChatGPT (Codex) 或 Grok 订阅额度而无需按用量计费，或通过开源代理 **OpenCode**，连接到任意所选供应商：本地模型（Ollama）、免费服务、订阅服务（GitHub Copilot……）或 API 密钥。

此 Python 脚本可将 Markdown 文件从源语言翻译为目标语言，同时保留格式、代码块和 front matter 元数据。

## 主要特性

- **多供应商**：5 个 API（OpenAI、Mistral、Claude、Gemini、Grok）+ 2 个订阅制 CLI，无需按用量计费——Codex (ChatGPT) 和 Grok——以及 OpenCode（开源、MIT），可连接 OpenCode 中配置的任意供应商，包括本地模型
- **2026 年模型**：GPT-5.6 Terra、Claude Sonnet 5、Gemini 3.7 Flash
- **经济模式**：使用 `--eco` 选项，以调用更快速且成本更低的模型
- **单文件**：使用 `--file` 选项翻译单个文件
- **智能分段**：根据模型的令牌限制处理长文本
- **代码保留**：代码块和行内代码（`` `...` ``）都会保留
- **文件名**：使用 `--keep_filename` 选项保留原始文件名
- **新闻模式**：使用 `--news` 选项保护英文引语，并处理新闻文章中的旗帜
- **.env 配置**：支持使用 `.env` 文件存储 API 密钥
- **翻译说明**：可选地在文档末尾添加说明

## 安装

### 使用工具

```bash
pip install ai-powered-markdown-translator
```

随后即可在任何位置使用 `aipmt` 命令。如果 Python 脚本目录不在
你的 `PATH` 中，`python -m aipmt` 可实现完全相同的功能。需要 Python 3.10 或更高版本。

如需与其他软件包隔离安装：

```bash
pipx install ai-powered-markdown-translator
```

### 为项目贡献代码

开发时仍需克隆代码仓库：测试、28 种翻译以及所有质量工具都位于其中。

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` 是一个**完全固定版本的锁定文件**，准确反映经过测试的环境。
`pyproject.toml` 中发布的版本范围则有意设置得更宽：不会对你的其他软件包施加任何限制。

### 质量工具（可选但推荐）

项目使用 [`pre-commit`](https://pre-commit.com)，以防止提交格式错误、存在漏洞或包含机密信息的代码。安装：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

已启用的钩子：ruff（检查+格式化）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（复杂度）、detect-secrets（API 密钥）、mypy（渐进式类型检查）、Opengrep（SAST）、pip-audit（CVE 依赖项）、unittest。详情请参阅 `CLAUDE.md` 中的 _Quality / pre-commit_ 部分。

## 配置

密钥会按优先级从高到低在**三个位置**查找。
每个位置只会补充前一个位置未提供的内容。

|     | 位置                                            | 用途                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 环境变量                     | CI、容器、临时覆盖 |
| 2   | 当前目录（或父目录）中的 `.env` | 项目专用密钥            |
| 3   | `~/.config/aipmt/.env`                        | **安装一次，处处可用**   |

在执行 `pip install` 后，最简单的是使用第三种方式：

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

当变量指向绝对路径时，此文件遵循 `XDG_CONFIG_HOME`
（否则会按规范忽略该变量），Windows 下则遵循 `%APPDATA%`。

当某个代码仓库拥有自己的密钥时，第二种方式仍然很有用：根目录中的
`.env` 会优先于用户配置，而不会修改后者。已经在环境中定义的变量则优先于前两者：

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

如果找不到任何密钥，命令不会输出调用跟踪，而是列出三个位置及其确切路径。

`GEMINI_API_KEY` 可作为 `GOOGLE_API_KEY` 的替代项（AI
Studio 约定）。可选变量：`XAI_BASE_URL`（xAI 端点，默认值为
`https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（Anthropic 每次调用的秒数，默认
900）、`CODEX_BIN` / `CODEX_TIMEOUT`、`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`、
`GROK_TRANSLATE_SANDBOX`（参见 Grok CLI 部分）以及 `OPENCODE_BIN` /
`OPENCODE_TIMEOUT`（参见 OpenCode 部分）。对于
`regen_translations.sh`：`REGEN_PROVIDER`、`REGEN_MODEL` 和
`REGEN_JOB_TIMEOUT`（每个任务的上限，默认为 600 秒）。

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

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### 使用 ChatGPT 订阅额度翻译（`--use_codex`）

此供应商不会使用任何 API 密钥：它以非交互模式驱动官方 Codex CLI，因此翻译会计入已经付费的 ChatGPT 订阅额度（Plus、Pro、Business……）。这是 OpenAI 针对此用途记录在案的唯一方式——`~/.codex/auth.json` 的令牌无法验证 Platform API 调用，而且此脚本也从不读取这些令牌。

**前提条件：**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

二进制文件按以下顺序查找：变量 `CODEX_BIN`、`PATH`，
然后是 Python 软件包 `openai-codex-cli-bin`。后者不会被有意加入
`requirements.txt`：它约 250 MB，若加入其中，会让所有用户都必须安装一个可选供应商。

**须知：**

- **不会使用任何 API 密钥。** 子进程环境中的 `OPENAI_API_KEY` 和 `CODEX_API_KEY` 会被
  移除，从而确保即使 `.env` 中存在密钥，也绝不会让翻译切换为按用量计费。
- **一个分段 = 计划 5 小时窗口中的一条“本地消息”。**
  与质量模型（`gpt-5.6-sol`，Plus 每 5 小时 10–100 条消息）相比，
  应使用 `--eco`（模型 `gpt-5.6-luna`，Plus 每 5 小时 250–2,000 条消息）。
- **比 API 调用更慢**：完整 README 大约需要 45 秒，而直接调用只需几秒。
- **CI 中会被拒绝**（已定义 `CI` 或 `GITHUB_ACTIONS`）：订阅认证并非为共享 runner 设计，
  OpenAI 也不建议在公共代码仓库中使用此工作流。在此路径中应使用 API 密钥。
- 环境变量：`CODEX_BIN`（二进制文件的显式路径）和
  `CODEX_TIMEOUT`（每个分段的秒数，默认为 `600`）。

### 使用 Grok 订阅额度翻译（`--use_grok_cli`）

原理与 `--use_codex` 相同，但使用官方 **Grok Build** CLI：翻译会计入 Grok 订阅额度（SuperGrok / X Premium+），而不是按令牌收费。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**隔离——使用前请阅读。** 此供应商在结构上**弱于
`--use_codex`**，这是有意为之：

- Codex 在 `--sandbox read-only` 中运行，这是系统强制的边界。
- 在许多较新的 Linux 系统上，Grok 沙箱**无法生效**：Ubuntu 24.04 起，AppArmor 会阻止非特权用户命名空间；当 `/run/podman` 为 `0700` 时，容器运行时套接字的拒绝列表也会失败。而一个**内置**但无法生效的配置文件会**静默地以未隔离状态启动**。
- 因此脚本默认不请求任何配置文件，也**绝不会静默回退**：它会显示警告。隔离依赖 CLI 的
  `--deny` 规则（包括 catch-all `*`），这是唯一经过衡量的
  _fail-closed_ 层——未知规则会导致启动被拒绝，而不是在不告知用户的情况下移除保护。
- 如需**强制使用**操作系统沙箱：`GROK_TRANSLATE_SANDBOX=read-only`。如果机器无法满足该要求，
  启动将失败，这正是预期行为。

**额度**：Grok 额度池按**周计算，并与 Chat、Imagine 和
Voice 共享**，且没有任何命令可以读取额度。因此批量处理可能在没有任何提示的情况下消耗你的对话额度——这就是将并发限制为 2，并在 `regen_translations.sh` 中显示警告的原因。

其他变量：`GROK_BIN`（二进制文件路径）、`GROK_TIMEOUT`（默认 900 秒）。

重新生成 28 种翻译：

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### 使用 OpenCode 翻译到任意所选供应商（`--use_opencode`）

[OpenCode](https://opencode.ai) 是一个在终端中运行的**开源（MIT）**代码代理。它不是模型供应商，而是一个**路由器**，用于连接你在 OpenCode 本身中配置的供应商：API 密钥、订阅服务（GitHub Copilot、ChatGPT、SuperGrok）、OpenCode Zen 网关——它提供**无需账户**的免费模型——或**本地**模型（Ollama、LM Studio、llama.cpp）。此供应商以非交互模式驱动 `opencode run`，并将调用限制为单次往返，且不启用任何工具。

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

必须提供 `--model`，格式为 `provider/modèle`。OpenCode 并非供应商，
不会替你选择默认值：它自身的回退机制可能使用一个免费模型，而交互内容可能被用于训练。

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**隔离——脚本在每次调用时执行的操作：**

- 一个内联配置（`OPENCODE_CONFIG_CONTENT`）优先于你的配置，并定义了一个 `aipmt` 代理，
  **拒绝所有工具**（`permission: { "*": "deny" }`）：模型既不能读取、写入，也不能执行命令——经过测试，它甚至不会尝试这些操作。会话共享已禁用，`--pure` 会排除外部插件，绝不会使用 `--auto`。
- 调用会在一个**临时且空的目录**中运行，并使用 `OPENCODE_DISABLE_PROJECT_CONFIG` 和 `OPENCODE_DISABLE_CLAUDE_CODE` 开关：
  没有这些开关时，OpenCode 会将当前目录的 `AGENTS.md` 和你的 `~/.claude/CLAUDE.md` 注入每个提示词——经过测试，在 `AGENTS.md` 中放置“让每个回答都以 BANANA 结尾”的指令，会被应用到翻译中。不过，`~/.config/opencode/AGENTS.md` 的全局规则仍会生效：OpenCode 不允许将其排除。
- 输出契约同时要求：返回码为 0、没有 `error` 事件、没有工具调用、最后一步以 `stop` 完成、有非空文本，并且代理确实已加载——未知的 `--agent` 不会使 OpenCode 失败，而是**静默回退**到启用工具的编码代理。此处 `exit 0` 也无法证明任何事情。
- **不会向子进程传递任何 aipmt 密钥**（与 Codex 和 Grok 使用相同的过滤方式），唯一的命名例外是 `OPENCODE_API_KEY`，即 OpenCode 自身的密钥（Zen、Go）。供应商应在 OpenCode 中配置（`opencode auth login`、`opencode.json`），而不是在 aipmt 的 `.env` 中配置。

**须知：**

- Zen 的**免费模型属于“stealth”模型或贡献者模型**，会发生变化，限制也未公开；其交互内容可能被用于训练：非常适合公开文档，但应避免用于私人内容。实测：`opencode/mimo-v2.5-free` 一次即可翻译此 README；`opencode/big-pickle` 更慢，并且两次并发请求都没有响应。
- **本地模型至少需要提供 16 k 的上下文**——分段最长可达 16,000 个字符——而 Ollama 通常默认配置为 4,096。使用 Ollama 时：通过 `Modelfile` 配置
  `PARAMETER num_ctx 32768`，然后执行 `ollama create`。质量取决于模型：在某个测试文件中，7B 模型颠倒了列表，并破坏了代码块结束标记，而网关中的模型完整保留了所有内容。
- `--eco` 不会生效（模型由 `--model` 决定）；`--reasoning_effort` 会原样作为 OpenCode 的 `--variant` 传递，只有在模型了解该参数时才应请求。
- OpenCode 会像记录所有 OpenCode 会话一样，将会话记录在其数据库（`~/.local/share/opencode/`）中。
- 环境变量：`OPENCODE_BIN`（二进制文件的显式路径，否则依次使用 `PATH` 和 `~/.opencode/bin/opencode`）以及 `OPENCODE_TIMEOUT`
  （每个分段的秒数，默认为 `600`）。如果导出 `OPENCODE_CONFIG`，脚本会遵循其设置。

### 经济模式

使用更快速且成本更低的模型（gpt-5.6-luna、claude-haiku-4-5、gemini-3.1-flash-lite）：

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### 选项

| 选项 | 描述 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file` | 要翻译的单个 Markdown 文件 |
| `--source_dir` | 包含 Markdown 文件的源目录 |
| `--target_dir` | 已翻译文件的输出目录 |
| `--source_lang` | 源语言（默认：`fr`） |
| `--target_lang` | 目标语言（默认：`en`） |
| `--model` | 要使用的特定模型 |
| `--eco` | 使用经济型模型 |
| `--use_mistral` | 使用 Mistral AI API |
| `--use_claude` | 使用 Claude API |
| `--use_gemini` | 使用 Gemini API |
| `--use_codex` | 使用 ChatGPT 订阅配额中的 Codex CLI |
| `--use_grok` | 使用 xAI（Grok）API——需要 `XAI_API_KEY` |
| `--use_grok_cli` | 使用 Grok CLI 的 Grok 订阅配额 |
| `--use_opencode` | 使用 OpenCode，将请求发送至 OpenCode 中配置的提供商；需要 `--model provider/modèle` |
| `--force` | 强制重新翻译 |
| `--keep_filename` | 保留原始文件名 |
| `--news` | 新闻模式：保护英文引文，并按语言处理标志 |
| `--add_translation_note` | 添加翻译说明 |
| `--note_position` | 说明位置：`top`、`bottom`（默认）或 `both` |
| `--note_format` | 说明格式：`legacy`（默认，粗体段落）或 `marker` |
| `--include_model` | 在输出文件中包含模型名称 |
| `--reasoning_effort` | GPT-5.x 推理力度：`none`/`low`/`medium`/`high`/`xhigh` |

> **七个 provider 标志互斥。** 以前同时组合其中两个不会显示警告，并会解析为第一个被测试的标志：在订阅配额（`--use_codex`、`--use_grok_cli`）上请求的翻译可能因此转为按量计费，且完全不会发出警告。
> `argparse` 现在会拒绝这种组合。

### 翻译说明：位置与格式

使用 `--add_translation_note` 时，translator 可以将说明放在顶部、底部或顶部和底部，并可将其呈现为纯文本格式（向后兼容）或 Markdown 插件可使用的 `marker` 格式。

**位置**（`--note_position`）：

- `bottom`（默认）：将说明放在文件末尾，与历史行为一致。
- `top`：将说明插入 **YAML frontmatter 之后**（适用于 Astro Content Collections、gray-matter 等）。
- `both`：在顶部和底部都插入说明（仅调用一次 LLM，内容复用于两个位置）。

**格式**（`--note_format`）：

- `legacy`（默认）：粗体段落 `**...**`——与 v1.8 完全一致，逐字节兼容。兼容 Hugo、GitHub、GitLab 以及所有 Markdown 渲染器。
- `marker`：不可见的 Markdown 链接引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），后接粗体 blockquote。在 GitHub/GitLab 上可原生阅读，并可在构建时由 Astro 端的 remark 插件处理，以生成样式化横幅（参见 jls42.org 博客）。

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

| 提供商 | 质量（默认） | 经济型（`--eco`） |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI | `gpt-5.6-terra` | `gpt-5.6-luna` |
| Claude | `claude-sonnet-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3.7-flash` | `gemini-3.1-flash-lite` |
| Codex | `gpt-5.6-sol` | `gpt-5.6-luna` |
| Grok API | `grok-4.6` | `grok-4.3` |
| Grok CLI | `grok-4.6` | `grok-4.5` |
| OpenCode | 必须使用 `--model provider/modèle` | 同上——`--eco` 无效 |

> **长篇翻译建议**：`--use_gemini`（默认 = `gemini-3.7-flash`）能够忠实保留非拉丁文字脚本（PL、JA、ZH、AR、HI）中的 Markdown 结构，包括在 `--news` 模式下占位符准确性也得到保证。在此 README 的日文翻译上进行测量：结构与 `gemini-3.1-pro-preview` 完全一致（21 个列表、18 个代码块、13 个 HTML 链接、13 张图片，所有 URL 均得到保留），延迟却降低约 6 倍。OpenAI 仍作为默认选项，以保持向后兼容性。

## 使用此脚本的项目

- **[jls42.org](https://jls42.org)** - 多语言个人博客（15 种语言）

## 作者

Julien LE SAUX  
电子邮件：contact@jls42.org

## 许可证

GNU GENERAL PUBLIC LICENSE Version 3。参见 [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)。

**文章由 gpt-5.6-luna 从法语翻译成中文。**
