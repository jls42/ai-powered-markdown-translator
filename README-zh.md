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

使用 **OpenAI**、**Mistral AI**、**Claude (Anthropic)** 和 **Google Gemini** 翻译 Markdown 文件。

此 Python 脚本可将 Markdown 文件从源语言翻译为目标语言，同时保留格式、代码块和 front matter 元数据。

## 主要特性

- **多 Provider**：支持 4 个 API（OpenAI、Mistral、Claude、Gemini）以及 ChatGPT 订阅中的 Codex CLI
- **2026 年模型**：GPT-5.6 Terra、Claude Sonnet 5、Gemini 3.7 Flash
- **经济模式**：使用 `--eco` 选项，以使用更快速且成本更低的模型
- **单文件**：使用 `--file` 选项翻译单个文件
- **智能分段**：根据模型的 token 限制处理长文本
- **代码保留**：代码块和行内代码（`` `...` ``）都会被保留
- **文件名**：使用 `--keep_filename` 选项保留原始文件名
- **新闻模式**：使用 `--news` 选项保护英文引文，并处理新闻文章中的语言标志
- **.env 配置**：支持使用 `.env` 文件存放 API 密钥
- **翻译备注**：可选择在文档末尾添加备注

## 安装

### 使用工具

```bash
pip install ai-powered-markdown-translator
```

随后即可在任何位置使用 `aipmt` 命令。如果 Python
脚本目录不在你的 `PATH` 中，`python -m aipmt` 可执行完全相同的操作。
需要 Python 3.10 或更高版本。

如需与其他软件包隔离安装：

```bash
pipx install ai-powered-markdown-translator
```

### 为项目贡献

开发仍需要克隆代码仓库：测试、28 种翻译以及所有质量工具都位于其中。

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` 是一个**完全锁定版本的 lock 文件**，准确反映经过测试的环境。
`pyproject.toml` 中发布的版本范围则有意设置得更宽：不会对你的其他软件包施加任何限制。

### 质量工具（可选但推荐）

项目使用 [`pre-commit`](https://pre-commit.com)，防止提交格式错误、存在漏洞或包含密钥的代码。安装：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

已启用的 Hook：ruff（lint+format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（复杂度）、detect-secrets（API 密钥）、mypy（渐进式类型检查）、Opengrep（SAST）、pip-audit（CVE 依赖项）、unittest。详情请参阅 `CLAUDE.md` 中的 _Quality / pre-commit_ 部分。

## 配置

密钥会按优先级从高到低在**三个位置**查找。
每个位置只会补充前一个位置未提供的内容。

|     | 位置                                            | 用途                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 环境变量                     | CI、容器、临时覆盖 |
| 2   | 当前目录（或父目录）中的 `.env` | 项目专用密钥            |
| 3   | `~/.config/aipmt/.env`                        | **安装一次，处处可用**   |

执行 `pip install` 后，最简单的方式是使用第三种：

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

当变量指定绝对路径时，此文件会遵循 `XDG_CONFIG_HOME`（否则会被忽略，正如规范所规定），
在 Windows 下则遵循 `%APPDATA%`。

当某个代码仓库有自己的密钥时，第二种方式仍然很有用：根目录中的 `.env`
会优先于用户配置，且不会修改用户配置。而已经在环境中定义的变量优先级高于前两者：

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

如果找不到任何密钥，命令不会输出调用堆栈，而是列出三个位置及其确切路径。

除 `GOOGLE_API_KEY` 外，也接受 `GEMINI_API_KEY`（AI Studio 约定）。
可选变量：`XAI_BASE_URL`（xAI 端点，默认为 `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`
（Anthropic 每次调用的秒数，默认为 900）、`CODEX_BIN` / `CODEX_TIMEOUT`、
`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`，以及 `GROK_TRANSLATE_SANDBOX`（参见 Grok CLI 部分）。
对于 `regen_translations.sh`：`REGEN_PROVIDER`、`REGEN_MODEL` 和 `REGEN_JOB_TIMEOUT`
（每个任务的上限，默认为 600 秒）。

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
```

### 使用 ChatGPT 订阅翻译（`--use_codex`）

此 Provider 不使用任何 API 密钥：它以非交互模式驱动官方 Codex CLI，
因此翻译消耗的是已支付的 ChatGPT 订阅（Plus、Pro、Business……）配额。
这是 OpenAI 针对此用途记录在案的唯一方式——`~/.codex/auth.json` 的 token
无法验证 Platform API 的调用，而且此脚本也从不读取这些 token。

**前提条件：**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

二进制文件按以下顺序查找：`CODEX_BIN` 变量、`PATH`，
然后是 Python 软件包 `openai-codex-cli-bin`。后者不会被有意加入 `requirements.txt`：
它约占 250 MB，否则所有用户都会被迫为可选 Provider 安装它。

**须知：**

- **不会使用任何 API 密钥。** 子进程环境会移除 `OPENAI_API_KEY` 和 `CODEX_API_KEY`，
  从而确保即使 `.env` 中存在密钥，也绝不会使翻译切换为按使用量计费。
- **一个分段 = 5 小时套餐窗口中的一条“本地消息”。**
  使用 `--eco`（模型 `gpt-5.6-luna`，Plus 套餐每 5 小时 250–2,000 条消息），
  而不是质量模型（`gpt-5.6-sol`，每 5 小时 10–100 条消息）。
- **速度更慢**于 API 调用：完整 README 约需 45 秒，而直接调用只需几秒。
- **CI 中会被拒绝**（已定义 `CI` 或 `GITHUB_ACTIONS`）：
  订阅认证并非为共享 Runner 设计，OpenAI 也不建议在公共代码仓库上使用此工作流。
  在此路径中应使用 API 密钥。
- 环境变量：`CODEX_BIN`（二进制文件的显式路径）和 `CODEX_TIMEOUT`
  （每个分段的秒数，默认为 `600`）。

### 使用 Grok 订阅翻译（`--use_grok_cli`）

原理与 `--use_codex` 相同，但使用官方 **Grok Build** CLI：
翻译消耗的是 Grok 订阅（SuperGrok / X Premium+）配额，而不是按 token 计费。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**隔离——使用前请阅读。** 此 Provider 在结构上**弱于 `--use_codex`**，这是有意为之：

- Codex 在 `--sandbox read-only` 中运行，这是系统强制规定的边界。
- 在许多较新的 Linux 主机上，Grok 沙箱**无法生效**：自 Ubuntu 24.04 起，
  AppArmor 会阻止非特权用户命名空间；当 `/run/podman` 为 `0700` 时，
  容器运行时套接字的拒绝列表也会失败。而无法生效的**内置**配置文件会**静默地**
  以未隔离状态启动。
- 因此脚本默认不请求任何配置文件，也绝不会静默回退：它会显示警告。
  隔离依赖 CLI 的 `--deny` 规则（包括 catch-all `*`），
  这是唯一经过测量的 _fail-closed_ 层——未知规则会拒绝启动，而不是不告知用户便移除保护。
- 如需**强制**使用操作系统沙箱：`GROK_TRANSLATE_SANDBOX=read-only`。
  如果机器无法满足该要求，启动将失败，这正是预期行为。

**配额**：Grok 配额池按**周**计算，并与 Chat、Imagine 和 Voice 共享，
且没有任何命令可以读取配额。因此批处理可能在无人提示的情况下消耗你的对话配额——
这就是并发限制为 2，并在 `regen_translations.sh` 中显示警告的原因。

其他变量：`GROK_BIN`（二进制文件路径）、`GROK_TIMEOUT`（默认为 900 秒）。

重新生成 28 种翻译：

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### 经济模式

使用更快速且成本更低的模型（gpt-5.6-luna、claude-haiku-4-5、gemini-3.1-flash-lite）：

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### 选项

| 选项                   | 描述                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | 要翻译的单个 Markdown 文件                                       |
| `--source_dir`           | 包含 Markdown 文件的源目录                        |
| `--target_dir`           | 已翻译文件的输出目录                          |
| `--source_lang`          | 源语言（默认为：`fr`）                                             |
| `--target_lang`          | 目标语言（默认为：`en`）                                              |
| `--model`                | 要使用的特定模型                                             |
| `--eco`                  | 使用经济型模型                                         |
| `--use_mistral`          | 使用 Mistral AI API                                                |
| `--use_claude`           | 使用 Claude API                                                    |
| `--use_gemini`           | 使用 Gemini API                                                    |
| `--use_codex`            | 使用 ChatGPT 订阅配额中的 Codex CLI               |
| `--use_grok`             | 使用 xAI API（Grok）——需要 `XAI_API_KEY`                      |
| `--use_grok_cli`         | 使用 Grok 订阅配额中的 Grok CLI                   |
| `--force`                | 强制重新翻译                                                  |
| `--keep_filename`        | 保留原始文件名                                     |
| `--news`                 | 新闻模式：保护英文引文，按语言处理标志 |
| `--add_translation_note` | 添加翻译备注                                           |
| `--note_position`        | 备注位置：`top`、`bottom`（默认）或 `both`                |
| `--note_format`          | 备注格式：`legacy`（默认，加粗段落）或 `marker`       |
| `--include_model`        | 在输出文件中包含模型名称                       |
| `--reasoning_effort`     | GPT-5.x 推理力度：`none`/`low`/`medium`/`high`/`xhigh`    |

> **六个 Provider 标志互斥。** 过去同时组合两个标志会被静默接受，并解析为第一个检测到的标志：
> 请求使用订阅配额（`--use_codex`、`--use_grok_cli`）的翻译，
> 可能因此转为按使用量计费，而且不会发出任何警告。
> `argparse` 现在会拒绝这种组合。

### 翻译备注：位置和格式

使用 `--add_translation_note` 时，translator 可以将备注放在顶部、底部或两处，
并可将其呈现为简单文本格式（向后兼容），或呈现为 Markdown 插件可使用的 `marker` 格式。

**位置**（`--note_position`）：

- `bottom`（默认）：将备注放在文件末尾，与历史行为一致。
- `top`：将备注插入 **YAML frontmatter 之后**（适用于 Astro Content Collections、gray-matter 等）。
- `both`：同时插入顶部和底部（只调用一次 LLM，内容复用于两个位置）。

**格式**（`--note_format`）：

- `legacy`（默认）：加粗段落 `**...**`——与 v1.8 的行为严格一致，逐字节兼容。
  兼容 Hugo、GitHub、GitLab 以及所有 Markdown 渲染器。
- `marker`：不可见的 Markdown 链接引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），
  后接加粗引用块。在 GitHub/GitLab 上可原生阅读，并可由 Astro 侧的 remark 插件
  在构建时处理，以生成样式化横幅（参见 jls42.org 博客）。

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

### 默认模型（2026 年）

| Provider | 质量（默认）       | 经济型（`--eco`）    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **长篇翻译建议**：`--use_gemini`（默认值 = `gemini-3.7-flash`）能够忠实保留非拉丁文字脚本（PL、JA、ZH、AR、HI）中的 Markdown 结构，
> 即使在 `--news` 模式下，依赖占位符的准确性也能得到保证。
> 在这份日文翻译的 README 上测得：结构与 `gemini-3.1-pro-preview` 完全相同（21 个列表、18 个代码块、13 个 HTML 链接、13 张图片，所有 URL 均保留），
> 延迟却降低约 6 倍。为保持向后兼容，OpenAI 仍是默认选项。

## 使用此脚本的项目

- **[jls42.org](https://jls42.org)** - 多语言个人博客（15 种语言）

## 作者

Julien LE SAUX
邮箱：contact@jls42.org

## 许可证

GNU GENERAL PUBLIC LICENSE Version 3。参见 [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)。

**文章由 gpt-5.6-luna 从法语翻译成中文。**
