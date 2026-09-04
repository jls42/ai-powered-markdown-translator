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

使用 **OpenAI**、**Mistral AI**、**Claude (Anthropic)**、**Google Gemini** 和 **Grok (xAI)** 的 Markdown 文件翻译器——可通过 API 使用，也可使用 ChatGPT (Codex) 或 Grok 订阅额度而无需按用量计费，还可通过开源代理 **OpenCode** 连接您选择的提供商：本地模型（Ollama）、免费服务、订阅服务（GitHub Copilot……）或密钥。

此 Python 脚本可将 Markdown 文件从源语言翻译为目标语言，同时保留格式、代码块和 front matter 元数据。

## 主要特性

- **多提供商**：5 种 API（OpenAI、Mistral、Claude、Gemini、Grok）+ 2 种基于订阅且无需按用量计费的 CLI——Codex (ChatGPT) 和 Grok——以及可连接 OpenCode 中任意已配置提供商的 OpenCode（开源、MIT），包括本地模型
- **2026 年模型**：GPT-5.6 Terra、Claude Sonnet 5、Gemini 3.7 Flash
- **经济模式**：使用 `--eco` 选项调用速度更快、成本更低的模型
- **单文件**：使用 `--file` 选项翻译单个文件
- **智能分段**：根据各模型的 token 限制处理长文本
- **代码保留**：保留代码块和行内代码（`` `...` ``）
- **文件名**：使用 `--keep_filename` 选项保留原始名称
- **新闻模式**：使用 `--news` 选项保护英文引文，并处理新闻文章中的旗帜符号
- **.env 配置**：支持使用 `.env` 文件保存 API 密钥
- **翻译说明**：可选择在文档末尾添加说明

## 安装

### 使用工具

```bash
pip install ai-powered-markdown-translator
```

随后即可在任何位置使用 `aipmt` 命令。如果 Python 脚本目录不在您的 `PATH` 中，`python -m aipmt` 的作用完全相同。需要 Python 3.10 或更高版本。

如需与其他软件包隔离安装：

```bash
pipx install ai-powered-markdown-translator
```

### 为项目作贡献

进行开发仍需克隆仓库：测试、28 种翻译以及全部质量工具都存放于其中。

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` 是一个**所有版本均完全固定的锁定文件**，准确反映经过测试的环境。`pyproject.toml` 中发布的版本范围则有意设置得更宽：它们不会对您的其他软件包施加限制。

### 质量工具（可选但推荐）

项目使用 [`pre-commit`](https://pre-commit.com) 防止提交格式错误、存在漏洞或包含密钥的代码。安装方式：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

已启用的钩子：ruff（检查和格式化）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（复杂度）、detect-secrets（API 密钥）、mypy（渐进式类型检查）、Opengrep（SAST）、pip-audit（依赖项 CVE）、unittest。详情请参阅 `CLAUDE.md` 的 _质量 / pre-commit_ 部分。

## 配置

系统会按优先级从高到低在**三个位置**查找密钥。每个位置只补充上一个位置中缺少的值。

|     | 位置                                          | 用途                                  |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 环境变量                                      | CI、容器、临时覆盖                    |
| 2   | 当前目录（或其父目录）中的 `.env`    | 项目专用密钥                          |
| 3   | `~/.config/aipmt/.env`                                | **只需安装一次，处处生效**            |

执行 `pip install` 后，最简单的方式是使用第三个位置：

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

当变量指向绝对路径时，此文件遵循 `XDG_CONFIG_HOME`（否则按照规范要求忽略该变量），在 Windows 上则遵循 `%APPDATA%`。

当某个仓库拥有自己的密钥时，第二个位置仍然很有用：位于仓库根目录的 `.env` 会优先于用户配置，且不会修改用户配置。环境中已定义的变量则优先于前两者：

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

如果找不到任何密钥，命令不会显示调用堆栈，而是列出这三个位置及其确切路径。

`GEMINI_API_KEY` 可作为 `GOOGLE_API_KEY` 的替代项（AI Studio 惯例）。可选变量：`XAI_BASE_URL`（xAI 端点，默认值为 `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（每次 Anthropic 调用的秒数，默认值为 900）、`CODEX_BIN` / `CODEX_TIMEOUT`、`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`、`GROK_TRANSLATE_SANDBOX`（参阅 Grok CLI 部分）以及 `OPENCODE_BIN` / `OPENCODE_TIMEOUT`（参阅 OpenCode 部分）。对于 `regen_translations.sh`：`REGEN_PROVIDER`（默认值为 `codex`，使用订阅）、`REGEN_MODEL`、`REGEN_ALLOW_PAID_API`（使用计费 API 时必须显式覆盖）以及 `REGEN_JOB_TIMEOUT`（每个作业的上限，默认 600 秒，在 Codex 上为 1,800 秒）。

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

### 使用 ChatGPT 订阅翻译（`--use_codex`）

此提供商无需使用任何 API 密钥：它以非交互模式驱动官方 Codex CLI，因此翻译会计入已付费的 ChatGPT 订阅（Plus、Pro、Business……）额度。这是 OpenAI 为此用途记录在案的唯一方式——`~/.codex/auth.json` 的 token 无法验证对 API Platform 的调用，而且此脚本从不读取它们。

**前置条件：**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

系统按以下顺序查找二进制文件：变量 `CODEX_BIN`、`PATH`，然后是 Python 软件包 `openai-codex-cli-bin`。后者有意未包含在 `requirements.txt` 中：其大小约为 250 MB，而它只是一个可选提供商，不应强制所有用户安装。

**注意事项：**

- **不使用任何 API 密钥。** `OPENAI_API_KEY` 和 `CODEX_API_KEY` 会从子进程环境中移除，以确保 `.env` 中存在的密钥绝不会让翻译切换到按用量计费模式。
- **一个分段等于五小时窗口中的一条“本地消息”。** 应使用 `--eco`（模型 `gpt-5.6-luna`，Plus 订阅每 5 小时 250–2,000 条消息），而不是质量模型（`gpt-5.6-sol`，每 5 小时 10–100 条消息）。
- 比 API 直接调用**更慢**：完整翻译一份 README 约需 45 秒，而直接调用只需几秒。
- **在 CI 中拒绝运行**（定义了 `CI` 或 `GITHUB_ACTIONS` 时）：订阅身份验证并非为共享 runner 设计，OpenAI 也不建议在公共仓库中采用此工作流。此场景应使用 API 密钥。
- 环境变量：`CODEX_BIN`（二进制文件的明确路径）和 `CODEX_TIMEOUT`（每个分段的秒数，默认值为 `600`）。

### 使用 Grok 订阅翻译（`--use_grok_cli`）

原理与 `--use_codex` 相同，但使用官方 **Grok Build** CLI：翻译计入 Grok 订阅（SuperGrok / X Premium+）额度，而不是按 token 计费。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**隔离机制——使用前必读。** 此提供商在结构上比 `--use_codex` **更弱**，这是经过权衡后接受的设计：

- Codex 运行于 `--sandbox read-only` 中，这是系统强制实施的边界。
- Grok 的 sandbox 在许多较新的 Linux 设备上**无法应用**：自 Ubuntu 24.04 起，AppArmor 会阻止非特权 user namespace；如果 `/run/podman` 位于 `0700` 中，容器运行时 socket 的拒绝列表也会失效。而无法应用的**内置**配置文件会在**不受隔离的状态下静默启动**。
- 因此，脚本默认不请求任何配置文件，并且**绝不会静默回退**：它会显示警告。隔离依赖 CLI 的 `--deny` 规则（包括兜底规则 `*`），这是唯一经测量会以 _失败即关闭_ 方式工作的层——未知规则会导致启动被拒绝，而不是在不作提示的情况下移除保护。
- 如需**强制使用**操作系统 sandbox：`GROK_TRANSLATE_SANDBOX=read-only`。如果设备无法满足要求，启动将失败，这正是预期行为。

**额度**：Grok 额度池按周计算，并由 Chat、Imagine 和 Voice **共享**，且没有任何命令可以查询余额。因此，批量处理可能会在没有任何提示的情况下消耗您的对话额度——这也是并发数限制为 2，并在 `regen_translations.sh` 中显示警告的原因。

其他变量：`GROK_BIN`（二进制文件路径）、`GROK_TIMEOUT`（默认值为 900 秒）。

重新生成 28 种翻译：

```bash
# Défaut : Codex sur l'abonnement ChatGPT, modèle qualité gpt-5.6-sol, 0 € à l'usage
./regen_translations.sh --force

# Le modèle éco de Codex, si le volume l'impose
REGEN_MODEL=gpt-5.6-luna ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Une API facturée (openai, gemini, grok) est REFUSÉE sans cette dérogation nommée
REGEN_PROVIDER=openai REGEN_ALLOW_PAID_API=1 ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### 使用 OpenCode 连接自选提供商进行翻译（`--use_opencode`）

[OpenCode](https://opencode.ai) 是一个运行于终端中的**开源（MIT）**代码代理。它不是模型提供商，而是连接您在 OpenCode 中配置的模型的**路由器**：API 密钥、订阅服务（GitHub Copilot、ChatGPT、SuperGrok）、提供**无需账户**的免费模型的 OpenCode Zen 网关，或**本地**模型（Ollama、LM Studio、llama.cpp）。此提供商以非交互模式驱动 `opencode run`，将调用限制为一次往返，并禁用所有工具。

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` 为**必填项**，格式为 `provider/modèle`。OpenCode 并非提供商，因此不会代您选择默认值：其自身的回退项会是一个免费模型，而交互内容可能被用于训练。

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**隔离机制——脚本每次调用时执行的操作：**

- 优先级高于您自身配置的内联配置（`OPENCODE_CONFIG_CONTENT`）会定义一个 `aipmt` 代理，并**拒绝所有工具**（`permission: { "*": "deny" }`）：模型无法读取、写入或运行命令——实测中，它甚至不会尝试这些操作。会话共享已禁用，`--pure` 会排除外部插件，绝不使用 `--auto`。
- 调用会在一个**临时的空目录**中运行，并启用 `OPENCODE_DISABLE_PROJECT_CONFIG` 和 `OPENCODE_DISABLE_CLAUDE_CODE` 开关：如果不启用，OpenCode 会在每个提示词中注入当前目录的 `AGENTS.md` 和您的 `~/.claude/CLAUDE.md`——实测中，在 `AGENTS.md` 里加入“每条回复都以 BANANA 结尾”的指令后，该指令确实会应用于翻译。但 `~/.config/opencode/AGENTS.md` 的全局规则仍会生效：OpenCode 不允许将其排除。
- 输出契约同时要求：返回码为 0、没有 `error` 事件、没有工具调用、最后一步以 `stop` 状态结束、文本非空，并且已实际加载指定代理——未知的 `--agent` 不会使 OpenCode 报错，而会**静默回退**到启用工具的编码代理。`exit 0` 在此也无法证明任何事情。
- **aipmt 的任何密钥都不会传递**给子进程（过滤方式与 Codex 和 Grok 相同），只有一个明确列出的例外：OpenCode 自身的密钥 `OPENCODE_API_KEY`（Zen、Go）。提供商应在 OpenCode 中配置（`opencode auth login`、`opencode.json`），而不是在 aipmt 的 `.env` 中配置。

**注意事项：**

- **Zen 的免费模型属于“隐身”模型或贡献者模型**，会不断变化，且限制未公开；其交互内容可能被用于训练：非常适合公共文档，但应避免用于私密内容。实测：`opencode/mimo-v2.5-free` 可一次性翻译此 README；`opencode/big-pickle` 速度更慢，两个并发请求均持续无响应。
- **本地模型必须提供至少 16 k 的上下文**——每个分段最多包含 16,000 个字符——而 Ollama 通常默认仅配置 4,096。使用 Ollama 时：创建包含 `PARAMETER num_ctx 32768` 的 `Modelfile`，然后执行 `ollama create`。质量取决于模型：在测试文件上，7B 模型颠倒了一个列表并破坏了代码块的结束围栏，而网关模型完整保留了一切。
- `--eco` 不起作用（实际模型由 `--model` 指定）；`--reasoning_effort` 会原样作为 OpenCode 的 `--variant` 传递，仅应在模型支持时启用。
- 会话会像其他 OpenCode 会话一样，由 OpenCode 记录到其数据库（`~/.local/share/opencode/`）中。
- 环境变量：`OPENCODE_BIN`（二进制文件的明确路径；否则依次使用 `PATH` 和 `~/.opencode/bin/opencode`）以及 `OPENCODE_TIMEOUT`（每个分段的秒数，默认值为 `600`）。如果导出了 `OPENCODE_CONFIG`，它也会生效。

**实测示例：通过 Ollama 使用本地模型**（RTX 3060 12 GB、62 GB RAM、Ollama 0.33.3）

```bash
curl -fsSL https://ollama.com/install.sh | sh   # Ollama ≥ 0.30 pour gemma4 ; conserve les modèles déjà téléchargés
ollama pull gemma4:12b                          # 7,6 Go, Apache 2.0, 140+ langues
ollama pull qwen3.5:9b                          # 6,6 Go, Apache 2.0, 201 langues

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gemma4:12b\nPARAMETER num_ctx 32768\n' > gemma4-12b-32k.Modelfile
ollama create gemma4-12b-32k -f gemma4-12b-32k.Modelfile
```

然后在 `~/.config/opencode/opencode.json` 中配置提供商：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": { "baseURL": "http://127.0.0.1:11434/v1" },
      "models": {
        "gemma4-12b-32k": {
          "name": "Gemma 4 12B (32k, sans réflexion)",
          "limit": { "context": 32768, "output": 8192 },
          "options": { "reasoningEffort": "none" }
        }
      }
    }
  }
}
```

`reasoningEffort: "none"` 并非无关紧要的细节：Ollama 默认会为 Gemma 4 和 Qwen 3.5 启用推理，而 Modelfile 无法将其关闭。通过 OpenCode 实测：若不加此选项，翻译“猫睡在地毯上”会消耗 919 个推理 token 和 68 秒；启用后仅需 9 个 token。

```bash
aipmt --use_opencode --model ollama/gemma4-12b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

在一篇真实的 589 行博客文章上得到的结果（包含 140 个链接、21 个章节、3 段由 `--news` 模式保护的英文引文）；命令相同，使用三个模型：

| 模型                                     | 用时          | 结构                                                       | 差异                                                                                      |
| ---------------------------------------- | ------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free`（Zen，免费）             | 4 分 26 秒    | 与源文相同                                                 | 无                                                                                        |
| `ollama/gemma4-12b-32k`（本地）                  | 10 分 10 秒   | 链接、URL、表格、标签、粗体和行内代码均相同                | 虚构了一行引文（🇺🇸 + 意译），重复了一处署名                                             |
| `ollama/qwen3.5-9b-32k`（本地）                  | 8 分 18 秒    | 链接、URL、表格和标签均相同                                | 虚构了一行引文，添加了少量粗体和行内代码，重新处理了一个分段                              |

本地翻译期间：GPU 使用率为 98%，功耗为 170 W，占用 10 GB VRAM（模型和 32 k token 缓存，未向 RAM 卸载任何内容），Ollama 服务器占用 7.5 GB RAM。参数规模为 90 亿至 120 亿的模型能够遵守结构，但每篇文章往往会自行发挥一次，而网关模型没有任何自行发挥：发布前应进行审阅，或仅将其用于草稿。

### 经济模式

使用速度更快、成本更低的模型（gpt-5.6-luna、claude-haiku-4-5、gemini-3.1-flash-lite）：

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### 选项

| 选项                   | 说明                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 要翻译的单个 Markdown 文件                                                                            |
| `--source_dir`           | 包含 Markdown 文件的源目录                                                             |
| `--target_dir`           | 翻译后文件的输出目录                                                               |
| `--source_lang`          | 源语言（默认：`fr`）                                                                                  |
| `--target_lang`          | 目标语言（默认：`en`）                                                                                   |
| `--model`                | 要使用的特定模型                                                                                  |
| `--eco`                  | 使用经济型模型                                                                              |
| `--use_mistral`          | 使用 Mistral AI API                                                                                     |
| `--use_claude`           | 使用 Claude API                                                                                         |
| `--use_gemini`           | 使用 Gemini API                                                                                         |
| `--use_codex`            | 使用 ChatGPT 订阅配额运行 Codex CLI                                                    |
| `--use_grok`             | 使用 xAI API（Grok）——需要 `XAI_API_KEY`                                                           |
| `--use_grok_cli`         | 使用 Grok 订阅配额运行 Grok CLI                                                        |
| `--use_opencode`         | 使用 OpenCode（开源）连接到其中配置的提供商；需要 `--model provider/modèle` |
| `--force`                | 强制重新翻译                                                                                       |
| `--keep_filename`        | 保留原始文件名                                                                          |
| `--news`                 | 新闻模式：保护英文引文，并按语言处理旗帜                                      |
| `--add_translation_note` | 添加翻译说明                                                                                |
| `--note_position`        | 说明位置：`top`、`bottom`（默认）或 `both`                                                     |
| `--note_format`          | 说明格式：`legacy`（默认，粗体段落）或 `marker`                                            |
| `--include_model`        | 在输出文件中包含模型名称                                                            |
| `--reasoning_effort`     | GPT-5.x 推理强度：`none`/`low`/`medium`/`high`/`xhigh`                                         |

> **七个提供商标志互斥。** 过去同时使用两个标志会被静默接受，
> 并选用首个被检测的提供商：原本要求使用订阅配额的翻译（`--use_codex`、`--use_grok_cli`）
> 因此可能在没有任何警告的情况下转为按使用量计费。
> `argparse` 现在会拒绝这种组合。

### 翻译说明：位置与格式

使用 `--add_translation_note` 时，翻译器可以将说明置于顶部、底部或两处，并可将其呈现为向后兼容的纯文本格式，或可由 Markdown 插件处理的 `marker` 格式。

**位置**（`--note_position`）：

- `bottom`（默认）：与以往一样，将说明放在文件末尾。
- `top`：将说明插入 **YAML frontmatter 之后**（兼容 Astro Content Collections、gray-matter 等）。
- `both`：在顶部和底部都插入说明（仅调用一次 LLM，内容复用于两个位置）。

**格式**（`--note_format`）：

- `legacy`（默认）：粗体段落 `**...**`——与 v1.8 的行为严格逐字节一致。兼容 Hugo、GitHub、GitLab 及所有 Markdown 渲染器。
- `marker`：不可见的 Markdown 链接引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），后接粗体引用块。可在 GitHub/GitLab 上原生阅读，也可在 Astro 构建时由 remark 插件处理，以生成样式化横幅（参见博客 jls42.org）。

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

| 提供商 | 质量型（默认）                      | 经济型（`--eco`）      |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI   | `gpt-5.6-terra`                       | `gpt-5.6-luna`            |
| Claude   | `claude-sonnet-5`                     | `claude-haiku-4-5`        |
| Mistral  | `mistral-large-latest`                | `mistral-small-latest`    |
| Gemini   | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite`   |
| Codex    | `gpt-5.6-sol`                         | `gpt-5.6-luna`            |
| Grok API | `grok-4.6`                            | `grok-4.3`                |
| Grok CLI | `grok-4.6`                            | `grok-4.5`                |
| OpenCode | 必须指定 `--model provider/modèle` | 相同——`--eco` 不生效 |

> **长篇翻译建议**：`--use_gemini`（默认值为 `gemini-3.7-flash`）能够在非拉丁文字语言（PL、JA、ZH、AR、HI）中忠实保留 Markdown 结构，包括在占位符保真度至关重要的 `--news` 模式下。以此 README 的日语译本进行测试：其结构与 `gemini-3.1-pro-preview` 完全相同（21 个列表、18 个代码块、13 个 HTML 链接、13 张图片，所有 URL 均保持不变），而延迟约降低 6 倍。为保持向后兼容，OpenAI 仍为默认提供商。

## 使用此脚本的项目

- **[jls42.org](https://jls42.org)** - 多语言个人博客（15 种语言）

## 作者

Julien LE SAUX
电子邮箱：contact@jls42.org

## 许可证

GNU GENERAL PUBLIC LICENSE 第 3 版。参见 [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)。

**使用 gpt-5.6-sol 将文章从法语翻译成中文。**
