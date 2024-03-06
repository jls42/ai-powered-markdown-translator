# 由OpenAI、Mistral AI和Anthropic的Claude提供支持的Markdown AI翻译器

这个项目是一个高级Python脚本，使用OpenAI、Mistral AI或Anthropic的Claude API将Markdown文件从源语言翻译成目标语言。它设计为灵活且易于使用，提供额外的选项，如添加翻译说明、增强的输出文件管理、现有文件检测以及对多种语言和翻译模型的支持。

要获得演示和详细说明，请访问[jls42.org](https://jls42.org/)或其翻译版本：[jls42.org English](https://jls42.org/traductions_en/)、[jls42.org Español](https://jls42.org/traductions_es/)和[jls42.org 中文](https://jls42.org/traductions_zh/)。

## 主要特点

- **AI驱动翻译**：使用OpenAI、Mistral AI或Anthropic的Claude的最新AI技术翻译您的文档。
- **多语言支持**：使用对不同语言模型的支持将您的文档翻译成多种语言。
- **智能分段**：通过自动分段有效地处理长文本。
- **翻译说明**：自动添加翻译说明以告知读者使用的过程。
- **增强的输出文件管理**：在启动翻译之前检查是否已存在翻译。
- **增强的现有文件检测**：搜索与原始文件的基本名称和目标语言匹配的文件。
- **灵活且可扩展**：代码结构允许轻松添加新功能。

## 先决条件

- Python 3.6或更高版本。
- OpenAI、Mistral AI或Anthropic的Claude的有效API密钥。

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

通过设置必要API密钥的环境变量来配置您的环境：

- **OpenAI**：
    ```
    export OPENAI_API_KEY='votre-clé-api-openai'
    ```
- **Mistral AI**：
    ```
    export MISTRAL_API_KEY='votre-clé-api-mistral'
    ```
- **Anthropic的Claude**：
    ```
    export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
    ```

## 使用

该脚本提供了几个选项来自定义翻译过程：

### 常规选项

- `--source_dir`：包含要翻译的Markdown文件的目录。
- `--target_dir`：已翻译文件的输出目录。
- `--model`：要使用的GPT翻译模型。默认模型取决于所选的API。
- `--source_lang`：文档的源语言。这对于添加翻译说明尤其重要。
- `--target_lang`：翻译的目标语言。默认为英语。
- `--force`：即使文件已存在翻译，也强制进行翻译。

### API特定选项

- `--use_mistral`：使用Mistral AI API进行翻译。
- `--use_claude`：使用Anthropic的Claude API进行翻译。
- `--add_translation_note`：在翻译后的内容中添加翻译说明，指定使用的方法和工具。

### 使用示例

- 使用OpenAI将法语翻译成英语，并添加翻译说明：
    ```
    python translate.py --use_openai --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- 使用Mistral AI将法语翻译成西班牙语，不添加翻译说明：
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## 作者

Julien LE SAUX  
电子邮件：contact@jls42.org

## 许可证

本项目获得GNU通用公共许可证第3版（2007年6月29日）的许可。有关更多详细信息，请参阅[LICENSE](LICENSE)文件。

**该文件使用 claude-3-opus-20240229 模型从 fr 版本翻译为 zh 语言。有关翻译过程的更多信息，请访问 https://gitlab.com/jls42/ai-powered-markdown-translator**

