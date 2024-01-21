# 使用 OpenAI 和 Mistral AI 的 AI 驱动 Markdown 翻译器

本项目是一个高级 Python 脚本，它使用 OpenAI 或 Mistral AI 的 API 来将 Markdown 文件从源语言翻译成目标语言。它设计得灵活且易于使用，提供了如添加翻译注释和支持多语言及多种翻译模型的额外选项。

要查看演示和详细说明，请访问 [Traduction IA jls42.org](https://jls42.org/posts/ia/automatisation-traduction-ia/) 或其翻译版本：[English](/traductions_en/)、[Español](/traductions_en/) 和 [中文](/traductions_zh/)。

## 主要特点

- **AI 驱动翻译**：使用最新的 AI 技术翻译您的文档。
- **多语言支持**：支持使用不同语言模型翻译文档到多种语言。
- **智能分段**：通过自动化分段有效管理较长文本。
- **翻译注释**：自动添加翻译注释以通知读者所使用的过程。
- **灵活且可扩展**：代码结构使得添加新功能变得容易。

## 先决条件

- Python 3.6 或更新版本。
- 有效的 OpenAI 或 Mistral AI API 密钥。

## 安装

1. 克隆 Git 仓库：
   ```
   git clone https://github.com/votre-repertoire/translate-markdown.git
   ```
2. 安装所需的依赖项：
   ```
   pip install -r requirements.txt
   ```

## 配置

在运行脚本之前，请配置您的环境：

- **OpenAI**：将您的 OpenAI API 密钥设置为环境变量：
  ```
  export OPENAI_API_KEY='votre-clé-api-openai'
  ```
- **Mistral AI**：将您的 Mistral AI API 密钥设置为环境变量：
  ```
  export MISTRAL_API_KEY='votre-clé-api-mistral'
  ```

## 使用方法

要翻译 Markdown 文件：

- **使用 OpenAI**：
  ```
  python translate.py --source_dir 'source/path' --target_dir 'target/path'
  ```
- **使用 Mistral AI**（并带有翻译注释选项）：
  ```
  python translate.py --use_mistral --source_dir 'source/path' --target_dir 'target/path' --model 'mistral-small' --add_translation_note
  ```

### 通用选项

- 指定模型、源语言和目标语言：
  ```
  python translate.py --source_dir 'source/path' --target_dir 'target/path' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
  ```

## 使用示例

- 西班牙语翻译请求的例子：
  ```
  python translate.py --source_dir content/ --target_dir content/traductions_es --target_lang es
  ```

## 许可证

本项目根据 GNU GENERAL PUBLIC LICENSE 版本 3，2007年6月29日许可。有关更多细节，请查看 [LICENSE](LICENSE) 文件。

**这份文件是由gpt-4-1106-preview模型从fr版本翻译而来。**

