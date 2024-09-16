# 使用 OpenAI、Mistral AI 和 Anthropi c的 Claude 的Markdown AI 泛译

该项目是一个高级 Python 脚本，使用 OpenAI、Mistral AI 或 Anthropi c 的 Claude API 将 Markdown 文件从源语言翻译成目标语言。它旨在灵活且易于使用，提供了诸如添加翻译注释、改进输出文件管理、检测现有文件以及支持多种语言和翻译模型的附加选项。

有关演示和详细说明，请访问 [jls42.org](https://jls42.org/) 或者翻译版本：[jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) 和 [jls42.org 中文](https://jls42.org/traductions_zh/)。

## 主要特征

- **AI 泛译**: 使用最新的 AI 技术通过 OpenAI、Mistral AI 或 Anthropi c 的 Claude 翻译您的文档。
- **多语言支持**: 在多种语言中翻译您的文档，并支持不同的语言模型。
- **智能分段**: 通过自动分段有效管理长文本。
- **翻译注释**: 自动添加翻译注释，通知读者所使用的翻译过程。
- **改进的输出文件管理**: 在启动翻译之前检查翻译是否已存在。
- **改进的现有文件检测**: 查找与原始文件基本名和目标语言匹配的文件。
- **灵活且可扩展**: 代码结构使其易于添加新功能。

## 先决条件

- Python 3.6 或更高版本。
- 有效的 OpenAI、Mistral AI 或 Anthropi c 的 Claude API 密钥。

## 安装

1. 克隆 Git 仓库:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. 安装必需的依赖项:
```
pip install -r requirements.txt
```

## 配置

通过设置所需的 API 密钥的环境变量配置您的环境：

- **OpenAI** :
    ```
    export OPENAI_API_KEY='votre-clé-api-openai'
    ```
- **Mistral AI** :
    ```
    export MISTRAL_API_KEY='votre-clé-api-mistral'
    ```
- **Claude d'Anthropic** :
    ```
    export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
    ```

## 使用

此脚本提供多个选项以自定义翻译过程:

### 通用选项

- `--source_dir` : 包含要翻译的 Markdown 文件的目录。
- `--target_dir` : 译后文件的输出目录。
- `--model` : 要使用的翻译 GPT 模型。默认模型取决于所选择的 API。
- `--source_lang` : 文档的源语言。尤其适用于翻译注释的添加。
- `--target_lang` : 翻译的目标语言。默认是英语。
- `--force` : 即使文件已有翻译，也强制启动新翻译。

### API 特定选项

- `--use_mistral` : 使用 Mistral AI 的 API 进行翻译。
- `--use_claude` : 使用 Anthropi c 的 Claude 的 API 进行翻译。
- `--add_translation_note` : 在翻译内容中添加说明翻译方法和所用工具的注释。

### 使用示例

- 使用 OpenAI 将法语翻译成英语，并添加翻译注释:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- 使用 Mistral AI 将法语翻译成西班牙语，不添加翻译注释 :
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## 作者

Julien LE SAUX  
邮箱: contact@jls42.org

## 许可证

该项目根据 GNU 通用公共许可证第 3 版 2007 年 6 月 29 日许可。详见 [LICENSE](LICENSE) 文件。

**该文档由fr版翻译成zh语言，使用的是gpt-4o模型。有关翻译过程的更多信息，请参阅：https://gitlab.com/jls42/ai-powered-markdown-translator**

