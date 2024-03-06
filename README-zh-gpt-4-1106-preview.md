# AI-Powered的Markdown翻译器，支持OpenAI、Mistral AI和Anthropic的Claude

这个项目是一个高级Python脚本，它使用OpenAI、Mistral AI或Anthropic的Claude的API来将Markdown文件从源语言翻译成目标语言。它旨在灵活易用，并提供额外选项，如添加翻译说明、改进输出文件管理、检测现有文件，以及支持多种语言和翻译模型。

要获得演示和详细说明，请访问[jls42.org](https://jls42.org/)或翻译版本：[jls42.org English](https://jls42.org/traductions_en/)、[jls42.org Español](https://jls42.org/traductions_es/)和[jls42.org 中文](https://jls42.org/traductions_zh/)。

## 主要特点

- **AI-Powered翻译**：使用OpenAI、Mistral AI或Anthropic的Claude的最新人工智能技术翻译您的文件。
- **多语言支持**：使用不同的语言模型翻译您的文件至多种语言。
- **智能分段**：通过自动化分段有效管理长文本。
- **翻译备注**：自动添加翻译笔记以告知读者使用的过程。
- **改进的输出文件管理**：在开始翻译之前检查是否已经存在翻译。
- **改进的现有文件检测**：搜寻与原始文件基础名称和目标语言相对应的文件。
- **灵活和可扩展**：代码结构设计为易于添加新特性。

## 先决条件

- Python 3.6或更高版本。
- 有效的OpenAI、Mistral AI或Anthropic的Claude API密钥。

## 安装

1. 克隆Git仓库：
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. 安装所需的依赖：
```
pip install -r requirements.txt
```

## 配置

通过设置环境变量来配置您的环境，以获取所需的API密钥：

- **OpenAI**：
    ```
    export OPENAI_API_KEY='您的openai-api密钥'
    ```
- **Mistral AI**：
    ```
    export MISTRAL_API_KEY='您的mistral-api密钥'
    ```
- **Claude d'Anthropic**：
    ```
    export ANTHROPIC_API_KEY='您的anthropic-api密钥'
    ```

## 使用

该脚本提供多个选项以自定义翻译过程：

### 通用选项

- `--source_dir`：包含Markdown文件以供翻译的目录。
- `--target_dir`：翻译文件的输出目录。
- `--model`：要使用的GPT翻译模型。默认模型取决于所选API。
- `--source_lang`：文档的源语言。特别是对于添加翻译注释很重要。
- `--target_lang`：翻译的目标语言。默认是英语。
- `--force`：即使文件的翻译已经存在也强制翻译。

### 特定API选项

- `--use_mistral`：使用Mistral AI的API进行翻译。
- `--use_claude`：使用Anthropic的Claude API进行翻译。
- `--add_translation_note`：在翻译内容中添加翻译注释，指明所使用的方法和工具。

### 使用示例

- 使用OpenAI将法语翻译成英语，并添加翻译注释：
    ```
    python translate.py --use_openai --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- 使用Mistral AI将法语翻译成西班牙语，不添加翻译注释：
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## 作者

Julien LE SAUX  
电子邮件：contact@jls42.org

## 许可证

本项目根据GNU GENERAL PUBLIC LICENSE版本3，2007年6月29日授权。有关更多细节，请查看[LICENSE](LICENSE)文件。

**此文档已使用模型 gpt-4-1106-preview 从 fr 版本翻译成 zh 语言。有关翻译过程的更多信息，请访问 https://gitlab.com/jls42/ai-powered-markdown-translator**

