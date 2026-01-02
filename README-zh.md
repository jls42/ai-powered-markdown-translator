# AI 驱动的 Markdown 翻译器

🌍 [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

使用 **OpenAI**、**Mistral AI**、**Claude（Anthropic）** 和 **Google Gemini** 的 Markdown 文件翻译器。

此 Python 脚本将 Markdown 文件从源语言翻译为目标语言，同时保留格式、代码块和前置元数据。

## 主要特性

- **多提供商**：支持 4 个 API（OpenAI、Mistral、Claude、Gemini）
- **2026 年模型**：GPT-5、Claude Sonnet 4.5、Gemini 3 Pro
- **经济模式**：选项 `--eco` 可使用更快且更低成本的模型
- **单文件**：选项 `--file` 用于仅翻译一个文件
- **智能分段**：根据各模型的 token 限制处理长文本
- **代码保留**：代码块不会被翻译
- **翻译注释**：可选在文档末尾添加一条注释

## 安装

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## 配置

为要使用的 API 设置环境变量：

```bash
export OPENAI_API_KEY='votre-clé-api-openai'
export MISTRAL_API_KEY='votre-clé-api-mistral'
export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
export GOOGLE_API_KEY='votre-clé-api-google'
```

## 用法

### 翻译单个文件

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### 翻译一个目录

```bash
# Avec OpenAI (défaut: gpt-5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### 经济模式

使用更快且更低成本的模型（gpt-5-mini、claude-haiku、gemini-flash）：

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### 选项

| 选项 | 描述 |
|--------|-------------|
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
| `--force` | 强制重新翻译 |
| `--add_translation_note` | 添加翻译注释 |

### 默认模型（2026）

| 提供商 | 质量（默认） | 经济型（`--eco`） |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## 作者

Julien LE SAUX
Email : contact@jls42.org

## 许可证

GNU 通用公共许可证 第 3 版。参见 [LICENSE](LICENSE)。