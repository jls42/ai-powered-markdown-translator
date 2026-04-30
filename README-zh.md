# AI 驱动的 Markdown 翻译器

🌍 [法语](README.md) | [英语](README-en.md) | [西班牙语](README-es.md) | [中文](README-zh.md) | [德语](README-de.md) | [日语](README-ja.md) | [韩语](README-ko.md) | [阿拉伯语](README-ar.md) | [印地语](README-hi.md) | [意大利语](README-it.md) | [荷兰语](README-nl.md) | [波兰语](README-pl.md) | [葡萄牙语](README-pt.md) | [罗马尼亚语](README-ro.md) | [瑞典语](README-sv.md)

使用 **OpenAI**、**Mistral AI**、**Claude（Anthropic）** 和 **Google Gemini** 的 Markdown 文件翻译器。

这个 Python 脚本将 Markdown 文件从源语言翻译为目标语言，同时保留格式、代码块和 front matter 元数据。

## 主要特性

- **多提供方**：支持 4 个 API（OpenAI、Mistral、Claude、Gemini）
- **2026 模型**：GPT-5.5、Claude Sonnet 4.6、Gemini 3.1 Pro
- **经济模式**：选项 `--eco`，使用更快且更便宜的模型
- **单文件**：选项 `--file`，用于翻译单个文件
- **智能分段**：处理带有模型 token 限制的长文本
- **代码保留**：代码块和内联代码（`` `...` ``）都会被保留
- **文件名**：选项 `--keep_filename`，保留原始名称
- **新闻模式**：选项 `--news`，用于保护英文引文并处理新闻文章中的语言旗帜
- **.env 配置**：支持用于 API 密钥的 `.env` 文件
- **翻译说明**：可选地在文档末尾添加说明

## 安装

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 质量工具（可选但推荐）

该项目使用 [`pre-commit`](https://pre-commit.com) 来防止提交格式错误、存在漏洞或包含机密的代码。安装：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

已启用的 hooks：ruff（lint+格式化）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（复杂度）、detect-secrets（API 密钥）、mypy（渐进式类型检查）、Opengrep（SAST）、pip-audit（CVE 依赖）、unittest。详情见 `CLAUDE.md` 的 _Quality / pre-commit_ 部分。

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

## 使用方法

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
| `--target_dir`           | 已翻译文件的输出目录                          |
| `--source_lang`          | 源语言（默认：`fr`）                                             |
| `--target_lang`          | 目标语言（默认：`en`）                                              |
| `--model`                | 要使用的特定模型                                             |
| `--eco`                  | 使用经济型模型                                         |
| `--use_mistral`          | 使用 Mistral AI API                                                |
| `--use_claude`           | 使用 Claude API                                                    |
| `--use_gemini`           | 使用 Gemini API                                                    |
| `--force`                | 强制重新翻译                                                  |
| `--keep_filename`        | 保留原始文件名                                     |
| `--news`                 | 新闻模式：保护英文引文，按语言处理旗帜 |
| `--add_translation_note` | 添加翻译说明                                           |
| `--include_model`        | 在输出文件中包含模型名称                       |

### 默认模型（2026）

| 提供方 | 质量（默认）         | 经济型（`--eco`）     |
| -------- | ------------------------ | ------------------------ |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`           |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5`       |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`   |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3-flash-preview` |

> **长篇翻译建议**：`--use_gemini`（默认 = `gemini-3.1-pro-preview` 质量，`--eco` = `gemini-3-flash-preview`）在非拉丁脚本（PL、JA、ZH、AR、HI）的脚本上往往能更好地保留 markdown 结构，尤其是在 `--news` 模式下，因为此时占位符的准确性很重要。为了向后兼容，OpenAI 仍然是默认选项。

## 使用该脚本的项目

- **[jls42.org](https://jls42.org)** - 多语言个人博客（15 种语言）

## 作者

Julien LE SAUX
电子邮件：contact@jls42.org

## 许可证

GNU GENERAL PUBLIC LICENSE Version 3。见 [LICENSE](LICENSE)。

**本文档已使用模型 gpt-5.4-mini 从 fr 版本翻译为 zh 语言。有关翻译过程的更多信息，请参阅 https://gitlab.com/jls42/ai-powered-markdown-translator**

