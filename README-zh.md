# AI 驱动的 Markdown 翻译器

🌍 [法语](README.md) | [英语](README-en.md) | [西班牙语](README-es.md) | [中文](README-zh.md) | [德语](README-de.md) | [日语](README-ja.md) | [韩语](README-ko.md) | [阿拉伯语](README-ar.md) | [印地语](README-hi.md) | [意大利语](README-it.md) | [荷兰语](README-nl.md) | [波兰语](README-pl.md) | [葡萄牙语](README-pt.md) | [罗马尼亚语](README-ro.md) | [瑞典语](README-sv.md)

<h4 align="center">📊 代码质量</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="质量门禁状态"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="安全性评级"></a>
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

使用 **OpenAI**、**Mistral AI**、**Claude (Anthropic)** 和 **Google Gemini** 的 Markdown 文件翻译器。

此 Python 脚本可将 Markdown 文件从源语言翻译为目标语言，同时保留格式、代码块和 front matter 元数据。

## 主要功能

- **多 Provider 支持**：支持 4 种 API（OpenAI、Mistral、Claude、Gemini）以及通过 ChatGPT 订阅使用 Codex CLI
- **2026 年模型**：GPT-5.6 Terra、Claude Sonnet 5、Gemini 3.7 Flash
- **经济模式**：使用 `--eco` 选项调用速度更快、成本更低的模型
- **单文件模式**：使用 `--file` 选项翻译单个文件
- **智能分段**：根据各模型的 token 限制处理长文本
- **代码保留**：保留代码块和行内代码（`` `...` ``）
- **文件名保留**：使用 `--keep_filename` 选项保留原始文件名
- **新闻模式**：使用 `--news` 选项保护英语引文，并处理新闻文章中的旗帜
- **.env 配置**：支持使用 `.env` 文件配置 API 密钥
- **翻译说明**：可选择在文档末尾添加说明

## 安装

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 质量工具（可选但推荐）

项目使用 [`pre-commit`](https://pre-commit.com) 防止提交格式不正确、存在漏洞或包含密钥的代码。安装方式：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

已启用的 hooks：ruff（lint+format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（复杂度）、detect-secrets（API 密钥）、mypy（渐进式类型检查）、Opengrep（SAST）、pip-audit（依赖项 CVE）、unittest。详情请参阅 `CLAUDE.md` 的 _质量 / pre-commit_ 部分。

## 配置

在项目根目录创建 `.env` 文件，或设置环境变量：

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

可使用 `GEMINI_API_KEY` 代替 `GOOGLE_API_KEY`（AI Studio 惯例）。可选变量：`XAI_BASE_URL`（xAI endpoint，默认值为 `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（每次 Anthropic 调用的秒数，默认值为 900）、`CODEX_BIN` / `CODEX_TIMEOUT`、`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`，以及 `GROK_TRANSLATE_SANDBOX`（参阅 Grok CLI 部分）。对于 `regen_translations.sh`：`REGEN_PROVIDER`、`REGEN_MODEL` 和 `REGEN_JOB_TIMEOUT`（每个 job 的上限，默认值为 600 秒）。

## 使用方法

### 翻译单个文件

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### 翻译目录

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
python translate.py --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
python translate.py --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
python translate.py --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### 使用 ChatGPT 订阅进行翻译（`--use_codex`）

此 provider 不使用任何 API 密钥：它以非交互模式驱动官方 Codex CLI，因此翻译会从已付费的 ChatGPT 订阅（Plus、Pro、Business……）配额中扣除。这是 OpenAI 针对此用途记录的唯一方式——`~/.codex/auth.json` 的 token 无法对 API Platform 调用进行身份验证，而且此脚本也从不读取它们。

**前置要求：**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

二进制文件按以下顺序查找：变量 `CODEX_BIN`、`PATH`，然后是 Python package `openai-codex-cli-bin`。后者有意未列入 `requirements.txt`：其大小约为 250 MB，如果加入其中，所有用户都必须安装这个可选 provider 的依赖。

**注意事项：**

- **不使用任何 API 密钥。** `OPENAI_API_KEY` 和 `CODEX_API_KEY` 会从子进程环境中移除，从而确保 `.env` 中存在的密钥绝不会导致翻译切换为按量计费。
- **一个分段 = 5 小时计划窗口中的一条“本地消息”。** 建议使用 `--eco`（模型 `gpt-5.6-luna`，Plus 每 5 小时可用 250–2 000 条消息），而不是质量模型（`gpt-5.6-sol`，每 5 小时可用 10–100 条消息）。
- **比 API 调用更慢**：完整翻译一个 README 约需 45 秒，而直接调用 API 只需几秒。
- **在 CI 中会被拒绝**（定义了 `CI` 或 `GITHUB_ACTIONS`）：订阅身份验证并非为共享 runner 设计，OpenAI 也不建议在公共仓库中使用此 workflow。此场景请使用 API 密钥。
- 环境变量：`CODEX_BIN`（二进制文件的明确路径）和 `CODEX_TIMEOUT`（每个分段的秒数，默认值为 `600`）。

### 使用 Grok 订阅进行翻译（`--use_grok_cli`）

原理与 `--use_codex` 相同，但使用官方 **Grok Build** CLI：翻译会从 Grok 订阅（SuperGrok / X Premium+）配额中扣除，而不是按 token 计费。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**隔离——使用前请阅读。** 此 provider 在结构上比 `--use_codex` **更弱**，这是经过权衡后接受的：

- Codex 在 `--sandbox read-only` 中运行，这是由系统强制实施的边界。
- Grok 的 sandbox 在许多较新的 Linux 工作站上**无法应用**：自 Ubuntu 24.04 起，AppArmor 会阻止非特权 user namespace；如果 `/run/podman` 位于 `0700` 中，容器 runtime socket 的 deny-list 也会失效。而一个无法应用的**内置** profile 会在**不受隔离的情况下静默启动**。
- 因此，脚本默认不请求任何 profile，并且**绝不会静默降级**：它会显示警告。隔离依赖 CLI 的 `--deny` 规则（包括兜底规则 `*`），这是唯一经测量具有 _fail-closed_ 特性的保护层——遇到未知规则时会拒绝启动，而不是在不作提示的情况下移除保护。
- 如需**强制要求**操作系统 sandbox，请使用 `GROK_TRANSLATE_SANDBOX=read-only`。如果机器无法满足要求，启动将失败，这正是预期行为。

**配额**：Grok 配额池以**每周为周期，并由 Chat、Imagine 和 Voice 共享**，且没有任何命令可以读取其余量。因此，批量处理可能会消耗你的对话配额，而系统不会发出任何提示——这也是并发限制为 2，并在 `regen_translations.sh` 中显示警告的原因。

其他变量：`GROK_BIN`（二进制文件路径）、`GROK_TIMEOUT`（默认值为 900 秒）。

如需重新生成 28 种翻译：

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### 经济模式

使用速度更快、成本更低的模型（gpt-5.6-luna、claude-haiku-4-5、gemini-3.1-flash-lite）：

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### 选项

| 选项                     | 说明                                                                     |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | 要翻译的单个 Markdown 文件                                               |
| `--source_dir`           | 包含 Markdown 文件的源目录                                               |
| `--target_dir`           | 翻译文件的输出目录                                                       |
| `--source_lang`          | 源语言（默认值：`fr`）                                         |
| `--target_lang`          | 目标语言（默认值：`en`）                                       |
| `--model`                | 要使用的特定模型                                                         |
| `--eco`                  | 使用经济型模型                                                           |
| `--use_mistral`          | 使用 Mistral AI API                                                      |
| `--use_claude`           | 使用 Claude API                                                          |
| `--use_gemini`           | 使用 Gemini API                                                          |
| `--use_codex`            | 使用 Codex CLI 和 ChatGPT 订阅配额                                       |
| `--use_grok`             | 使用 xAI API（Grok）——需要 `XAI_API_KEY`                                |
| `--use_grok_cli`         | 使用 Grok CLI 和 Grok 订阅配额                                           |
| `--force`                | 强制重新翻译                                                             |
| `--keep_filename`        | 保留原始文件名                                                           |
| `--news`                 | 新闻模式：保护英语引文，并按语言处理旗帜                                 |
| `--add_translation_note` | 添加翻译说明                                                             |
| `--note_position`        | 说明位置：`top`、`bottom`（默认）或 `both`         |
| `--note_format`          | 说明格式：`legacy`（默认，粗体段落）或 `marker`               |
| `--include_model`        | 在输出文件中包含模型名称                                                 |
| `--reasoning_effort`     | GPT-5.x 推理强度：`none`/`low`/`medium`/`high`/`xhigh` |

> **六个 provider flag 互斥。** 以前可以静默组合其中两个，并解析为第一个被检测的选项：原本要求使用订阅配额（`--use_codex`、`--use_grok_cli`）的翻译可能因此在没有任何警告的情况下变成按量计费。
> `argparse` 现在会拒绝这种组合。

### 翻译说明：位置与格式

使用 `--add_translation_note` 时，translator 可以将说明放在顶部、底部或同时放在两处，并以向后兼容的纯文本格式或可由 Markdown plugin 处理的 `marker` 格式呈现。

**位置**（`--note_position`）：

- `bottom`（默认）：与以往一样，将说明放在文件末尾。
- `top`：将说明插入 **YAML frontmatter 之后**（兼容 Astro Content Collections、gray-matter 等）。
- `both`：在顶部和底部都插入说明（仅调用一次 LLM，两处复用相同内容）。

**格式**（`--note_format`）：

- `legacy`（默认）：粗体段落 `**...**`——其行为与 v1.8 严格一致，达到逐字节相同。兼容 Hugo、GitHub、GitLab 以及所有 Markdown renderer。
- `marker`：不可见的 Markdown link reference definition（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），后接粗体 blockquote。可在 GitHub/GitLab 上原生阅读，也可在 Astro 构建时由 remark plugin 处理，以生成样式化横幅（参见博客 jls42.org）。

```bash
# Compatibilité legacy (rien ne change vs v1.8)
python translate.py --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### 默认模型（2026）

| Provider | 质量型（默认）         | 经济型（`--eco`） |
| -------- | ---------------------- | ------------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`           |
| Claude   | `claude-sonnet-5`        | `claude-haiku-4-5`           |
| Mistral  | `mistral-large-latest`        | `mistral-small-latest`           |
| Gemini   | `gemini-3.7-flash`        | `gemini-3.1-flash-lite`           |
| Codex    | `gpt-5.6-sol`        | `gpt-5.6-luna`           |
| Grok API | `grok-4.6`        | `grok-4.3`           |
| Grok CLI | `grok-4.6`        | `grok-4.5`           |

> **长篇翻译建议**：`--use_gemini`（默认值为 `gemini-3.7-flash`）能在非拉丁文字（PL、JA、ZH、AR、HI）中忠实保留 Markdown 结构，包括在占位符保真度至关重要的 `--news` 模式下。通过将此 README 翻译为日语进行测量：其结构与 `gemini-3.1-pro-preview` 完全相同（21 个列表、18 个代码块、13 个 HTML 链接、13 张图片，所有 URL 均得以保留），而延迟约降低至六分之一。为了向后兼容，OpenAI 仍为默认选项。

## 使用此脚本的项目

- **[jls42.org](https://jls42.org)** - 多语言个人博客（15 种语言）

## 作者

Julien LE SAUX
电子邮件：contact@jls42.org

## 许可证

GNU GENERAL PUBLIC LICENSE 第 3 版。参阅 [LICENSE](LICENSE)。

**使用 gpt-5.6-sol 将文章从法语翻译成中文。**
