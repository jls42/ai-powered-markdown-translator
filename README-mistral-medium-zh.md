AI-Powered Markdown Translator with OpenAI and Mistral AI

This project is an advanced Python script that uses the OpenAI or Mistral AI API to translate Markdown files from a source language to a target language. It is designed to be flexible and easy to use, offering additional options such as adding a translation note and support for multiple languages and translation models.

For a demonstration and detailed explanations, visit [jls42.org](https://jls42.org/) or in translated version: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_en/) and [jls42.org 中文中文](https://jls42.org/traductions_zh/).

## Main Features

- **AI-Powered Translation**: Use the latest AI technologies for your document translation.
- **Multilingual Support**: Translate your documents into multiple languages with support for different language models.
- **Smart Segmentation**: Manage long texts efficiently thanks to automated segmentation.
- **Translation Note**: Add automatically a translation note to inform readers about the process used.
- **Flexible and Extensible**: The code is structured to allow easy addition of new features.

## Prerequisites

- Python 3.6 or later.
- A valid API key for OpenAI or Mistral AI.

## Installation

1. Clone the Git repository:
   ```
   git clone https://github.com/your-repository/translate-markdown.git
   ```
2. Install the necessary dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Before launching the script, configure your environment:

- **OpenAI**: Set your OpenAI API key as an environment variable:
  ```
  export OPENAI_API_KEY='your-openai-api-key'
  ```
- **Mistral AI**: Set your Mistral AI API key as an environment variable:
  ```
  export MISTRAL_API_KEY='your-mistral-api-key'
  ```

## Usage

To translate Markdown files:

- **With OpenAI**:
  ```
  python translate.py --source_dir 'source/path' --target_dir 'target/path'
  ```
- **With Mistral AI** (and translation note option):
  ```
  python translate.py --use_mistral --source_dir 'source/path' --target_dir 'target/path' --model 'mistral-small' --add_translation_note
  ```

### Common Options

- Specify the model, source language, and target language:
  ```
  python translate.py --source_dir 'source/path' --target_dir 'target/path' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
  ```

## Examples

- Example of Spanish translation request:
  ```
  python translate.py --source_dir content/ --target_dir content/traductions_es --target_lang es
  ```

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. See the file [LICENSE](LICENSE) for more details.

---

AI强力Markdown翻译器与OpenAI和Mistral AI

这个项目是一个高级Python脚本，利用OpenAI或Mistral AI API将Markdown文件从源语言翻译成目标语言。它旨在灵活且易于使用，并提供添加翻译注释和支持多种语言和翻译模型等额外选项。

有关演示和详细说明，请访问[jls42.org](https://jls42.org/)或翻译版本：[jls42.org English](https://jls42.org/traductions_en/)，[jls42.org Español](https://jls42.org/traductions_en/) 和[jls42.org 中文中文](https://jls42.org/traductions_zh/)。

## 主要特点

- **基于AI的翻译**：使用最新的AI技术进行您的文档翻译。
- **多语言支持**：使用不同语言模型支持将您的文档翻译成多种语言。
- **智能分段**：通过自动分段有效管理长文本。
- **翻译注释**：自动添加翻译注释以告知读者使用的过程。
- **灵活性和可扩展性**：代码结构易于添加新功能。

## 先决条件

- Python 3.6或更高版本。
- OpenAI或Mistral AI的有效API密钥。

## 安装

1. 克隆Git存储库：
   ```
   git clone https://github.com/your-repository/translate-markdown.git
   ```
2. 安装必要的依赖项：
   ```
   pip install -r requirements.txt
   ```

## 配置

启动脚本之前配置您的环境：

- **OpenAI**：将OpenAI API密钥设置为环境变量：
  ```
  export OPENAI_API_KEY='your-openai-api-key'
  ```
- **Mistral AI**：将Mistral AI API密钥设置为环境变量：
  ```
  export MISTRAL_API_KEY='your-mistral-api-key'
  ```

## 使用方法

要翻译Markdown文件：

- **使用OpenAI**：
  ```
  python translate.py --source_dir 'source/path' --target_dir 'target/path'
  ```
- **使用Mistral AI**（和翻译注释选项）：
  ```
  python translate.py --use_mistral --source_dir 'source/path' --target_dir 'target/path' --model 'mistral-small' --add_translation_note
  ```

### 常见选项

- 指定模型、源语言和目标语言：
  ```
  python translate.py --source_dir 'source/path' --target_dir 'target/path' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
  ```

## 示例

- 请求西班牙语翻译的示例：
  ```
  python translate.py --source_dir content/ --target_dir content/traductions_es --target_lang es
  ```

## 许可证

本项目根据GNU GENERAL PUBLIC LICENSE Version 3，2007年6月29日发行。有关更多详细信息，请参阅[LICENSE](LICENSE)文件。

**这份文件已由模型 mistral-medium 从法文版翻译。

Note: The literal translation of "Ce document a été traduit..." is "这份文件已被翻译...", but in Chinese, it's more common to use the passive construction "已经被..." to express that something has been done to the subject, rather than using the passive voice "被翻译的文件".

Also, "la version fr" can be translated as "法文版" (French version) in this context. The word "fr" is often used as an abbreviation for "français" (French) in digital contexts.

Finally, "le modèle mistral-medium" can be translated as "模型 mistral-medium" (Mistral-medium model) in Chinese, as "le" can be omitted when referring to a model or a system.**

