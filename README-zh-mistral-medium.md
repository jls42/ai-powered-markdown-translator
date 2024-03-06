'# AI-Powered Markdown Translator with OpenAI, Mistral AI, and Claude from Anthropic

This project is an advanced Python script that uses OpenAI, Mistral AI, or Claude's API from Anthropic to translate Markdown files from a source language to a target language. It is designed to be flexible and easy to use, offering additional options such as adding a translation note, enhanced file output management, detection of existing files, and support for multiple languages and translation models.

For a demonstration and detailed explanations, visit [jls42.org](https://jls42.org/) or in translated version: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) and [jls42.org 中文](https://jls42.org/traductions_zh/).

## Main Features

- **AI-Powered Translation**: Use the latest AI technologies for document translation with OpenAI, Mistral AI, or Claude from Anthropic.
- **Multilingual Support**: Translate your documents into several languages with support for different language models.
- **Smart Segmentation**: Manage long texts efficiently through automatic segmentation.
- **Translation Note**: Add automatically a translation note to inform readers about the process used.
- **Enhanced Output File Management**: Check if a translation already exists before launching the translation.
- **Improved Existing File Detection**: Search for corresponding files based on the original file name and target language.
- **Flexible and Extensible**: The code is structured to allow easy addition of new features.

## Prerequisites

- Python 3.6 or later.
- A valid API key for OpenAI, Mistral AI, or Claude from Anthropic.

## Installation

1. Clone the Git repository:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. Install the necessary dependencies:
```
pip install -r requirements.txt
```

## Configuration

Configure your environment by defining the environment variables for the necessary API keys:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='your-openai-api-key'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='your-mistral-api-key'
    ```
- **Claude from Anthropic**:
    ```
    export ANTHROPIC_API_KEY='your-anthropic-api-key'
    ```

## Usage

The script offers several options to customize the translation process:

### General Options

- `--source_dir`: Directory containing the Markdown files to translate.
- `--target_dir`: Output directory for translated files.
- `--model`: GPT translation model to use. The default model depends on the selected API.
- `--source_lang`: Source language of documents. Important notably for adding translation notes.
- `--target_lang`: Target language for translation. Default is English.
- `--force`: Force translation even if a translation already exists for the file.

### API-Specific Options

- `--use_mistral`: Use the Mistral AI API for translation.
- `--use_claude`: Use the Claude API from Anthropic for translation.
- `--add_translation_note`: Add a translation note to the translated content, specifying the method and tools used.

### Usage Examples

- Translate from French to English with OpenAI, adding a translation note:
    ```
    python translate.py --use_openai --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Translate from French to Spanish with Mistral AI, without a translation note:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## Author

Julien LE SAUX
Email: [contact@jls42.org](mailto:contact@jls42.org)

## License

This project is licensed under GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. See the [LICENSE](LICENSE) file for more details.'

  ## 主要特点

- **基于AI的翻译**：使用OpenAI、Mistral AI或Anthropic的Claude等最新AI技术进行文档翻译。
- **多语言支持**：支持多种语言模型，将您的文档翻译成多种语言。
- **智能分段**：通过自动分段有效管理长文本。
- **翻译注释**：自动向翻译内容添加翻译注释，告知读者所使用的过程。
- **增强输出文件管理**：在启动翻译之前，检查是否已存在翻译。
- **改进现有文件检测**：根据原始文件名和目标语言搜索相应文件。
- **灵活可扩展**：代码结构设计为允许轻松添加新功能。

## 先决条件

- Python 3.6或更高版本。
- OpenAI、Mistral AI或Anthropic的Claude等有效API密钥。

## 安装

1. 克隆Git存储库：
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. 安装必要的依赖项：
```
pip install -r requirements.txt
```

## 配置

通过定义必要API密钥的环境变量来配置您的环境：

- **OpenAI**：
    ```
    export OPENAI_API_KEY='您的OpenAI API密钥'
    ```
- **Mistral AI**：
    ```
    export MISTRAL_API_KEY='您的Mistral API密钥'
    ```
- **Anthropic的Claude**：
    ```
    export ANTHROPIC_API_KEY='您的Anthropic API密钥'
    ```

## 使用方法

脚本提供多个选项来自定义翻译过程：

### 常规选项

- `--source_dir`：包含要翻译的Markdown文件的目录。
- `--target_dir`：翻译文件的输出目录。
- `--model`：要使用的GPT翻译模型。默认模型取决于所选API。
- `--source_lang`：文档的源语言。特别是在添加翻译注释时重要。
- `--target_lang`：翻译的目标语言。默认为英语。
- `--force`：即使文件已存在翻译，也强制进行翻译。

### API特定选项

- `--use_mistral`：使用Mistral AI API进行翻译。
- `--use_claude`：使用Anthropic的Claude API进行翻译。
- `--add_translation_note`：向翻译内容添加翻译注释，指定所使用的方法和工具。

### 使用示例

- 使用OpenAI翻译自法语到英语，添加翻译注释：
    ```
    python translate.py --use_openai --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- 使用Mistral AI翻译自法语到西班牙语，没有翻译注释：
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## 作者

Julien LE SAUX
电子邮件：[contact@jls42.org](mailto:contact@jls42.org)

## 许可证

本项目根据GNU GENERAL PUBLIC LICENSE版本3，2007年6月29日发布。有关更多详细信息，请参阅[LICENSE](LICENSE)文件。'

**本文由 fr 版本翻译成 zh 语言，使用了 mistral-medium 模型。有关翻译过程的更多信息，请参阅 <https://gitlab.com/jls42/ai-powered-markdown-translator>**

