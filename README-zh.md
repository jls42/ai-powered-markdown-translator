# AI 驱动的 Markdown 翻译器

🌍 [英语](README-en.md) | [西班牙语](README-es.md) | [中文](README-zh.md) | [德语](README-de.md) | [日语](README-ja.md) | [韩语](README-ko.md) | [阿拉伯语](README-ar.md) | [印地语](README-hi.md) | [意大利语](README-it.md) | [荷兰语](README-nl.md) | [波兰语](README-pl.md) | [葡萄牙语](README-pt.md) | [罗马尼亚语](README-ro.md) | [瑞典语](README-sv.md)

使用 **OpenAI**、**Mistral AI**、**Claude（Anthropic）** 和 **Google Gemini** 的 Markdown 文件翻译器。

该 Python 脚本将 Markdown 文件从源语言翻译为目标语言，同时保留格式、代码块和 front matter 元数据。

## 主要功能

- **多提供者**：支持 4 个 API（OpenAI、Mistral、Claude、Gemini）
- **2026 年模型**：GPT-5、Claude Sonnet 4.5、Gemini 3 Pro
- **经济模式**：选项 `--eco`，用于使用更快、成本更低的模型
- **单文件**：选项 `--file`，用于翻译单个文件
- **智能分段**：处理长文本并根据模型的 token 限制进行分割
- **保留代码**：代码块和内联代码（`` `...` ``）均会被保留
- **文件名**：选项 `--keep_filename`，用于保留原始文件名
- **.env 配置**：支持使用 `.env` 文件来存放 API 密钥
- **翻译备注**：可选地在文档末尾添加备注

## 安装

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## 配置

在项目根目录创建一个 `.env` 文件，或设置环境变量：

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## 使用

### 翻译单个文件

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### 翻译目录

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

使用更快且成本更低的模型（gpt-5-mini、claude-haiku、gemini-flash）：

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### 选项

| 选项 | 描述 |
|--------|-------------|
| `--file` | 要翻译的单个 Markdown 文件 |
| `--source_dir` | 包含 Markdown 文件的源目录 |
| `--target_dir` | 翻译后文件的输出目录 |
| `--source_lang` | 源语言（默认：`fr`） |
| `--target_lang` | 目标语言（默认：`en`） |
| `--model` | 指定使用的模型 |
| `--eco` | 使用经济型模型 |
| `--use_mistral` | 使用 Mistral AI API |
| `--use_claude` | 使用 Claude API |
| `--use_gemini` | 使用 Gemini API |
| `--force` | 强制重新翻译 |
| `--keep_filename` | 保留原始文件名 |
| `--add_translation_note` | 添加翻译备注 |
| `--include_model` | 在输出文件中包含模型名称 |

### 默认模型（2026）

| 提供者 | 质量（默认） | 经济型（`--eco`） |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## 使用该脚本的项目

- **[jls42.org](https://jls42.org)** - 个人博客，翻译为 15 种语言

## 作者

Julien LE SAUX  
电子邮件：contact@jls42.org

## 许可

GNU 通用公共许可证 第 3 版。参见 [许可证](LICENSE)。

**本文件已使用 gpt-5-mini 模型将法语（fr）版本翻译为中文（zh）。有关翻译过程的更多信息，请参见 https://gitlab.com/jls42/ai-powered-markdown-translator**

