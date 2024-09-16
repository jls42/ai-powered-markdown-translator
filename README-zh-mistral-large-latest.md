# 由OpenAI、Mistral AI和Anthropic的Claude提供支持的Markdown翻译器

这个项目是一个高级的Python脚本，使用OpenAI、Mistral AI或Anthropic的Claude API将Markdown文件从源语言翻译成目标语言。它旨在灵活且易于使用，提供额外选项，如添加翻译说明、改进输出文件管理、检测现有文件和支持多种语言和翻译模型。

有关演示和详细说明，请访问[jls42.org](https://jls42.org/)或翻译版本：[jls42.org English](https://jls42.org/traductions_en/)，[jls42.org Español](https://jls42.org/traductions_es/)和[jls42.org 中文](https://jls42.org/traductions_zh/)。

## 主要特点

- **AI提供支持的翻译**：使用OpenAI、Mistral AI或Anthropic的Claude的最新AI技术翻译您的文档。
- **多语言支持**：使用不同的语言模型将文档翻译成多种语言。
- **智能分段**：通过自动分段有效地处理长文本。
- **翻译说明**：自动添加翻译说明，以告知读者所使用的过程。
- **改进的输出文件管理**：在启动翻译之前检查是否已存在翻译。
- **改进的现有文件检测**：查找与原始文件基名和目标语言匹配的文件。
- **灵活且可扩展**：代码结构允许轻松添加新功能。

## 先决条件

- Python 3.6或更高版本。
- OpenAI、Mistral AI或Anthropic的Claude的有效API密钥。

## 安装

1. 克隆Git仓库：
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. 安装必要的依赖项：
```
pip install -r requirements.txt
```

## 配置

通过设置所需API密钥的环境变量来配置您的环境：

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

## 使用

脚本提供了多个选项来自定义翻译过程：

### 常规选项

- `--source_dir`：包含要翻译的Markdown文件的目录。
- `--target_dir`：输出翻译文件的目录。
- `--model`：要使用的GPT翻译模型。默认模型取决于所选的API。
- `--source_lang`：文档的源语言。对于添加翻译说明尤为重要。
- `--target_lang`：翻译的目标语言。默认为英语。
- `--force`：即使文件已有翻译，也强制进行翻译。

### API特定选项

- `--use_mistral`：使用Mistral AI API进行翻译。
- `--use_claude`：使用Anthropic的Claude API进行翻译。
- `--add_translation_note`：在翻译内容中添加翻译说明，指定所使用的方法和工具。

### 使用示例

- 使用OpenAI从法语翻译成英语，并添加翻译说明：
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- 使用Mistral AI从法语翻译成西班牙语，不添加翻译说明：
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## 作者

Julien LE SAUX
Email：contact@jls42.org

## 许可证

本项目基于GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007。请参阅[LICENSE](LICENSE)文件以获取更多详细信息。

**Ce document a été traduit de la version fr vers la langue zh en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator**

