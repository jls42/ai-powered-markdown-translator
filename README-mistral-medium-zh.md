# AI 动力的 Markdown 翻译器，使用 OpenAI 和 Mistral AI

这个项目是一个高级 Python 脚本，使用 OpenAI API 或 Mistral AI API 将 Markdown 文件从源语言翻译成目标语言。它设计为灵活、易于使用，提供了添加翻译注释和支持多种语言和翻译模型等额外选项。

要查看演示和详细说明，请访问 [IA 翻译 Traduction jls42.org](https://jls42.org/posts/ia/automatisation-traduction-ia/) 或已翻译的版本：[英文](/traductions\_en/)，[西班牙文](/traductions\_en/) 和 [中文中文](/traductions\_zh/)。

## 主要特点

- **基于 AI 的翻译**：使用最新的 AI 技术翻译您的文档。
- **多语言支持**：使用不同的语言模型将您的文档翻译成多种语言。
- **智能分段**：通过自动化分段有效管理长文本。
- **翻译注释**：自动添加翻译注释以告知读者所使用的过程。
- **灵活和可扩展**：代码结构化以便于添加新功能。

## 先决条件

- Python 3.6 或更高版本。
- OpenAI 或 Mistral AI 的有效 API 密钥。

## 安装

1. 克隆 Git 仓库：
   ```
   git clone https://github.com/votre-repertoire/translate-markdown.git
   ```
2. 安装必要的依赖项：
   ```
   pip install -r requirements.txt
   ```

## 配置

在运行脚本之前配置您的环境：

- **OpenAI**：将 OpenAI API 密钥设置为环境变量：
  ```
  export OPENAI_API_KEY='votre-clé-api-openai'
  ```
- **Mistral AI**：将 Mistral AI API 密钥设置为环境变量：
  ```
  export MISTRAL_API_KEY='votre-clé-api-mistral'
  ```

## 使用方法

要翻译 Markdown 文件：

- **使用 OpenAI**：
  ```
  python translate.py --source_dir 'source/path' --target_dir 'target/path'
  ```
- **使用 Mistral AI**（和翻译注释选项）：
  ```
  python translate.py --use_mistral --source_dir 'source/path' --target_dir 'target/path' --model 'mistral-small' --add_translation_note
  ```

### 常见选项

- 指定模型、源语言和目标语言：
  ```
  python translate.py --source_dir 'source/path' --target_dir 'target/path' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
  ```

## 示例用法

- 示例翻译请求（将内容翻译成西班牙语）：
  ```
  python translate.py --source_dir content/ --target_dir content/traductions_es --target_lang es
  ```

## 许可

本项目根据 GNU GENERAL PUBLIC LICENSE Version 3，29 June 2007 授权。有关更多详细信息，请参阅 [LICENSE](LICENSE) 文件。

**这份文件已由模型 Mistral-medium 从法语版翻译。

Note: This sentence translated to Chinese states that 'This document has been translated from the French version by the Mistral-medium model.'

Confidence: 95%**

