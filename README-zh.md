# AI 驱动的 Markdown 翻译器

🌍 [法语](README.md) | [英语](README-en.md) | [西班牙语](README-es.md) | [中文](README-zh.md) | [德语](README-de.md) | [日语](README-ja.md) | [韩语](README-ko.md) | [阿拉伯语](README-ar.md) | [印地语](README-hi.md) | [意大利语](README-it.md) | [荷兰语](README-nl.md) | [波兰语](README-pl.md) | [葡萄牙语](README-pt.md) | [罗马尼亚语](README-ro.md) | [瑞典语](README-sv.md)

<h4 align="center">📊 代码质量</h4>

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

使用 **OpenAI**、**Mistral AI**、**Claude（Anthropic）** 和 **Google Gemini** 的 Markdown 文件翻译器。

这个 Python 脚本将 Markdown 文件从源语言翻译为目标语言，同时保留格式、代码块和 front matter 元数据。

## 主要特性

- **多提供商**：支持 4 个 API（OpenAI、Mistral、Claude、Gemini）
- **2026 模型**：GPT-5.5、Claude Sonnet 4.6、Gemini 3.1 Pro
- **经济模式**：选项 `--eco`，可使用更快且更便宜的模型
- **单文件**：选项 `--file`，用于翻译单个文件
- **智能分段**：通过模型 token 限制处理长文本
- **代码保留**：代码块和内联代码（`` `...` ``）都会被保留
- **文件名**：选项 `--keep_filename`，保留原始名称
- **新闻模式**：选项 `--news`，用于保护英文引号并处理新闻文章中的语言旗帜
- **.env 配置**：支持用于 API 密钥的 `.env` 文件
- **翻译注释**：可在文档末尾添加可选注释

## 安装

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 质量工具（可选但推荐）

项目使用 [`pre-commit`](https://pre-commit.com) 来防止提交格式不正确、存在漏洞或包含机密的代码。安装：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

已启用的 hooks：ruff（lint+format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（复杂度）、detect-secrets（API 密钥）、mypy（渐进式类型检查）、Opengrep（SAST）、pip-audit（CVE 依赖）、unittest。详见 `CLAUDE.md` 的 _质量 / pre-commit_ 部分。

## 配置

在项目根目录创建一个 `.env` 文件，或定义环境变量：

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## 用法

### 翻译单个文件

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### 翻译目录

```bash
# Avec OpenAI (défaut: gpt-5.5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### 经济模式

使用更快且更便宜的模型（gpt-5.4-mini、claude-haiku、gemini-flash）：

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### 选项

| 选项                   | 描述                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | 要翻译的单个 Markdown 文件                                       |
| `--source_dir`           | 包含 Markdown 文件的源目录                        |
| `--target_dir`           | 翻译后文件的输出目录                          |
| `--source_lang`          | 源语言（默认：`fr`）                                             |
| `--target_lang`          | 目标语言（默认：`en`）                                              |
| `--model`                | 要使用的特定模型                                             |
| `--eco`                  | 使用经济型模型                                         |
| `--use_mistral`          | 使用 Mistral AI API                                                |
| `--use_claude`           | 使用 Claude API                                                    |
| `--use_gemini`           | 使用 Gemini API                                                    |
| `--force`                | 强制重新翻译                                                  |
| `--keep_filename`        | 保留原始文件名                                     |
| `--news`                 | 新闻模式：保护英文引号，按语言处理旗帜 |
| `--add_translation_note` | 添加翻译注释                                           |
| `--note_position`        | 注释位置：`top`、`bottom`（默认），或 `both`                |
| `--note_format`          | 注释格式：`legacy`（默认，粗体段落）或 `marker`       |
| `--include_model`        | 在输出文件中包含模型名称                       |

### 翻译注释：位置与格式

使用 `--add_translation_note`，翻译器可以将注释放在顶部、底部或两处，并且可以将其呈现为纯文本格式（向后兼容）或可由 Markdown 插件消费的 `marker` 格式。

**位置**（`--note_position`）：

- `bottom`（默认）：注释放在文件末尾，与历史行为一致。
- `top`：注释放在 **YAML frontmatter 之后**（Astro Content Collections、gray-matter 等的安全性）。
- `both`：注释放在顶部和底部（只需一次 LLM 调用，内容可重复用于两个位置）。

**格式**（`--note_format`）：

- `legacy`（默认）：粗体 `**...**` 段落——与 v1.8 的行为完全一致，逐字节一致。兼容 Hugo、GitHub、GitLab，以及任何 Markdown 渲染器。
- `marker`：不可见的 Markdown 链接引用定义 `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`，后接一个粗体 blockquote。可在 GitHub/GitLab 上原生读取，并可在构建时通过 Astro 端的 remark 插件生成样式化横幅（参见 jls42.org 博客）。

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

| 提供商 | 质量（默认）         | 经济型（`--eco`）            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **长篇翻译建议**：`--use_gemini`（默认 = `gemini-3.1-pro-preview` 质量，`--eco` = `gemini-3.1-flash-lite-preview`）在非拉丁脚本（PL、JA、ZH、AR、HI）的 Markdown 结构保留方面往往表现更好，尤其是在 `--news` 模式下，那里占位符的准确性尤为重要。为了向后兼容，OpenAI 仍为默认。

## 使用此脚本的项目

- **[jls42.org](https://jls42.org)** - 多语言个人博客（15 种语言）

## 作者

Julien LE SAUX
Email : contact@jls42.org

## 许可证

GNU GENERAL PUBLIC LICENSE 第 3 版。参见 [LICENSE](LICENSE)。

**使用 gpt-5.4-mini 将文章从法语翻译成中文。**
