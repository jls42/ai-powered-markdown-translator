# AI 驱动的 Markdown 翻译器

🌍 [法语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [英语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [西班牙语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [德语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [韩语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [阿拉伯语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [印地语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [意大利语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [荷兰语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [波兰语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [葡萄牙语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [罗马尼亚语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [瑞典语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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

使用 **OpenAI**、**Mistral AI**、**Claude (Anthropic)** 和 **Google Gemini** 的 Markdown 文件翻译器。

此 Python 脚本可将 Markdown 文件从源语言翻译为目标语言，同时保留格式、代码块和 front matter 元数据。

## 主要特性

- **多 Provider**：支持 4 个 API（OpenAI、Mistral、Claude、Gemini）以及 ChatGPT 订阅附带的 Codex CLI
- **2026 年模型**：GPT-5.6 Terra、Claude Sonnet 5、Gemini 3.7 Flash
- **经济模式**：使用 `--eco` 选项来使用更快速且成本更低的模型
- **单文件**：使用 `--file` 选项来翻译单个文件
- **智能分段**：根据模型的 token 限制处理长文本
- **代码保留**：代码块和行内代码（`` `...` ``）均会保留
- **文件名**：使用 `--keep_filename` 选项来保留原始名称
- **News 模式**：使用 `--news` 保护英文引文，并处理新闻文章中的旗帜
- **.env 配置**：支持使用 `.env` 文件保存 API 密钥
- **翻译注释**：可选择在文档末尾添加注释

## 安装

### 使用工具

```bash
pip install ai-powered-markdown-translator
```

此时，命令 `aipmt` 已可在任何位置使用。如果 Python 脚本目录不在
`PATH` 中，`python -m aipmt` 可实现完全相同的功能。需要 Python 3.10 或更高版本。

若要与其他软件包隔离安装：

```bash
pipx install ai-powered-markdown-translator
```

### 为项目贡献代码

要进行开发，仍然需要克隆仓库：测试、28 种翻译和所有质量工具都位于其中。

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` 是一个**完全锁定版本的 lock 文件**，准确反映了经过测试的环境。
`pyproject.toml` 中公布的版本范围则有意设置得更宽：不会对你的其他软件包施加任何限制。

### 质量工具（可选但推荐）

项目使用 [`pre-commit`](https://pre-commit.com) 来防止提交格式错误、存在漏洞或包含机密信息的代码。安装方式：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

启用的 Hooks：ruff（lint+format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（复杂度）、detect-secrets（API 密钥）、mypy（渐进式类型检查）、Opengrep（SAST）、pip-audit（CVE 依赖项）、unittest。详情请参阅 `CLAUDE.md` 中的 _Quality / pre-commit_ 部分。

## 配置

在**运行命令的目录中**创建 `.env` 文件（程序会先在此处查找，然后查找父目录），或者
定义环境变量：

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

`GEMINI_API_KEY` 可作为 `GOOGLE_API_KEY` 的替代项（AI
Studio 约定）。可选变量：`XAI_BASE_URL`（xAI 端点，默认值为
`https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（每次 Anthropic 调用的秒数，默认值为
900）、`CODEX_BIN` / `CODEX_TIMEOUT`、`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`，
以及 `GROK_TRANSLATE_SANDBOX`（请参阅 Grok CLI 部分）。对于
`regen_translations.sh`：`REGEN_PROVIDER`、`REGEN_MODEL` 和
`REGEN_JOB_TIMEOUT`（每个任务的上限，默认值为 600 秒）。

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

此 Provider 不消耗任何 API 密钥：它以非交互模式驱动官方 Codex CLI，因此翻译消耗的是已付费的
ChatGPT 订阅（Plus、Pro、Business……）配额。这是 OpenAI 针对该用途记录的唯一方式——
`~/.codex/auth.json` 的 token 无法认证 Platform API 的调用，而且此脚本也从不读取它们。

**前提条件：**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

程序会按以下顺序查找二进制文件：变量 `CODEX_BIN`、`PATH`，
然后是 Python 软件包 `openai-codex-cli-bin`。后者不会被有意加入 `requirements.txt`：
它约占 250 MB，否则所有用户都必须为一个可选 Provider 承担这部分开销。

**须知：**

- **不会使用任何 API 密钥。** 子进程环境中的 `OPENAI_API_KEY` 和 `CODEX_API_KEY` 会被
  移除，因此可以确保即使 `.env` 中存在密钥，也绝不会使翻译切换为按使用量计费。
- **一个分段 = 5 小时计划窗口中的一条“本地消息”。**
  使用 `--eco`（模型 `gpt-5.6-luna`，Plus 每 5 小时可使用 250–2,000 条消息），
  而不是质量模型（`gpt-5.6-sol`，每 5 小时 10–100 条消息）。
- **比 API 调用更慢**：完整 README 约需 45 秒，而直接调用只需几秒。
- **CI 中会被拒绝**（已定义 `CI` 或 `GITHUB_ACTIONS`）：订阅认证并非为共享 runner
  设计，且 OpenAI 不建议在公共仓库中采用此工作流。在此路径上应使用 API 密钥。
- 环境变量：`CODEX_BIN`（二进制文件的显式路径）和
  `CODEX_TIMEOUT`（每个分段的秒数，默认值为 `600`）。

### 使用 Grok 订阅翻译（`--use_grok_cli`）

原理与 `--use_codex` 相同，但使用官方 **Grok Build** CLI：
翻译消耗的是 Grok 订阅（SuperGrok / X Premium+）配额，而不是按 token 计费。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**隔离机制——使用前请阅读。** 此 Provider 在结构上**弱于
`--use_codex`**，这是有意为之：

- Codex 在 `--sandbox read-only` 中运行，这是系统强制规定的边界。
- 在许多较新的 Linux 工作站上，Grok 沙箱**无法生效**：自 Ubuntu
  24.04 起，AppArmor 会阻止非特权 user namespaces；当 `/run/podman` 为
  `0700` 时，容器运行时套接字的拒绝列表也会失效。而且，无法生效的**内置**配置文件会
  **静默地以未隔离状态**启动。
- 因此脚本默认不请求任何配置文件，也绝不会**静默回退**：它会显示警告。隔离依赖 CLI 的
  `--deny` 规则（包括 catch-all `*`），这是唯一经过测量的
  _fail-closed_ 层——未知规则会拒绝启动，而不是不告知用户便移除保护。
- 若要**强制启用**操作系统沙箱：`GROK_TRANSLATE_SANDBOX=read-only`。如果机器无法满足该要求，启动将失败，
  这正是预期行为。

**配额**：Grok 池按**周计算并与 Chat、Imagine 和 Voice 共享**，且没有任何命令可以读取其使用情况。
因此，批处理可能在没有任何提示的情况下消耗你的对话配额——这也是将并发限制为 2，并在
`regen_translations.sh` 中显示警告的原因。

其他变量：`GROK_BIN`（二进制文件路径）、`GROK_TIMEOUT`（默认值为 900 秒）。

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

| 选项 | 描述 |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file` | 要翻译的单个 Markdown 文件 |
| `--source_dir` | 包含 Markdown 文件的源目录 |
| `--target_dir` | 已翻译文件的输出目录 |
| `--source_lang` | 源语言（默认值：`fr`） |
| `--target_lang` | 目标语言（默认值：`en`） |
| `--model` | 要使用的特定模型 |
| `--eco` | 使用经济型模型 |
| `--use_mistral` | 使用 Mistral AI API |
| `--use_claude` | 使用 Claude API |
| `--use_gemini` | 使用 Gemini API |
| `--use_codex` | 使用 ChatGPT 订阅配额中的 Codex CLI |
| `--use_grok` | 使用 xAI (Grok) API——需要 `XAI_API_KEY` |
| `--use_grok_cli` | 使用 Grok 订阅配额中的 Grok CLI |
| `--force` | 强制重新翻译 |
| `--keep_filename` | 保留原始文件名 |
| `--news` | 新闻模式：保护英文引文，并按语言处理旗帜 |
| `--add_translation_note` | 添加翻译注释 |
| `--note_position` | 注释位置：`top`、`bottom`（默认值）或 `both` |
| `--note_format` | 注释格式：`legacy`（默认值，加粗段落）或 `marker` |
| `--include_model` | 在输出文件中包含模型名称 |
| `--reasoning_effort` | GPT-5.x 推理力度：`none`/`low`/`medium`/`high`/`xhigh` |

> **六个 Provider 标志互相排斥。** 过去同时组合两个标志会被静默接受，并解析为第一个经过测试的选项：
> 请求使用订阅配额进行翻译（`--use_codex`、`--use_grok_cli`）时，可能因此在没有任何警告的情况下切换为按使用量计费。
> `argparse` 现在会拒绝这种组合。

### 翻译注释：位置和格式

使用 `--add_translation_note` 时，translator 可以将注释放置在顶部、底部或两处，并将其生成为纯文本格式（向后兼容），或生成为可供 Markdown 插件使用的 `marker` 格式。

**位置**（`--note_position`）：

- `bottom`（默认值）：注释放在文件末尾，与历史行为一致。
- `top`：注释插入 **YAML frontmatter 之后**（适用于 Astro Content Collections、gray-matter 等）。
- `both`：注释放在顶部和底部（只调用一次 LLM，内容复用于两个位置）。

**格式**（`--note_format`）：

- `legacy`（默认值）：加粗段落 `**...**`——与 v1.8 严格一致，逐字节兼容。兼容 Hugo、GitHub、GitLab 以及所有 Markdown 渲染器。
- `marker`：不可见的 Markdown 链接引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），后接加粗 blockquote。可在 GitHub/GitLab 上原生阅读，也可在构建时由 Astro 端的 remark 插件处理，以生成样式化横幅（参见 jls42.org 博客）。

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

| Provider | 质量（默认值） | 经济型（`--eco`） |
| -------- | ---------------------- | ----------------------- |
| OpenAI | `gpt-5.6-terra` | `gpt-5.6-luna` |
| Claude | `claude-sonnet-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3.7-flash` | `gemini-3.1-flash-lite` |
| Codex | `gpt-5.6-sol` | `gpt-5.6-luna` |
| Grok API | `grok-4.6` | `grok-4.3` |
| Grok CLI | `grok-4.6` | `grok-4.5` |

> **长篇翻译建议**：`--use_gemini`（默认值 = `gemini-3.7-flash`）能够忠实保留非拉丁文字脚本（PL、JA、ZH、AR、HI）中的 Markdown 结构，包括在 `--news` 模式下也能保留占位符的准确性。在这份翻译成日语的 README 上进行测量：结构与 `gemini-3.1-pro-preview` 完全一致（21 个列表、18 个代码块、13 个 HTML 链接、13 张图片，所有 URL 均已保留），延迟约降低 6 倍。为保持向后兼容，OpenAI 仍是默认选项。

## 使用此脚本的项目

- **[jls42.org](https://jls42.org)** - 多语言个人博客（15 种语言）

## 作者

Julien LE SAUX
电子邮件：contact@jls42.org

## 许可证

GNU GENERAL PUBLIC LICENSE Version 3。请参阅 [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)。

**使用 gpt-5.6-luna 将文章从法语翻译成中文。**
