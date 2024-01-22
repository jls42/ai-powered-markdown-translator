# OpenAI和Mistral AI驱动的Markdown翻译器

该项目是一个高级Python脚本，可以使用OpenAI API或Mistral AI API将Markdown文件从源语言翻译成目标语言。它的设计旨在灵活易用，提供了额外的选项，比如可以添加翻译注释，支持多种语言和翻译模型。

要观看演示和详细说明，请访问 [jls42.org](https://jls42.org/) 或其翻译版本：[jls42.org English](https://jls42.org/traductions_en/)、[jls42.org Español](https://jls42.org/traductions_en/)和 [jls42.org 中文](https://jls42.org/traductions_zh/)。

## 主要特性

- **AI驱动的翻译**：使用最新的AI技术翻译您的文件。
- **多语言支持**：支持使用不同语言模型翻译文件到多种语言。
- **智能分段**：通过自动化分段有效管理长文本。
- **翻译注释**：自动添加翻译注释，以通知读者所使用的过程。
- **灵活且可扩展**：代码结构设计得很好，可以方便地添加新功能。

## 预先要求

- Python 3.6或更高版本。
- 有效的OpenAI或Mistral AI API密钥。

## 安装

1. 克隆Git仓库：
   ```
   git clone https://github.com/votre-repertoire/translate-markdown.git
   ```
2. 安装所需依赖：
   ```
   pip install -r requirements.txt
   ```

## 配置

在启动脚本前，配置您的环境：

- **OpenAI**：将您的OpenAI API密钥设置为环境变量：
  ```
  export OPENAI_API_KEY='votre-clé-api-openai'
  ```
- **Mistral AI**：将您的Mistral AI API密钥设置为环境变量：
  ```
  export MISTRAL_API_KEY='votre-clé-api-mistral'
  ```

## 使用

翻译Markdown文件：

- **使用OpenAI**：
  ```
  python translate.py --source_dir 'source/path' --target_dir 'target/path'
  ```
- **使用Mistral AI**（并添加翻译注释）：
  ```
  python translate.py --use_mistral --source_dir 'source/path' --target_dir 'target/path' --model 'mistral-small' --add_translation_note
  ```

### 公共选项

- 指定模型、源语言和目标语言：
  ```
  python translate.py --source_dir 'source/path' --target_dir 'target/path' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
  ```

## 使用示例

- 请求翻译成西班牙语的示例：
  ```
  python translate.py --source_dir content/ --target_dir content/traductions_es --target_lang es
  ```

## 许可证

该项目在GNU通用公共许可证版本3下授权，2007年6月29日发布。更多详情请见 [LICENSE](LICENSE) 文件。

**这份文件是由gpt-4-1106-preview模型从法文版本翻译而来的。**

