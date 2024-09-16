# 基于OpenAI、Mistral AI和Anthropic的Claude的AI驱动Markdown翻译器

这个项目是一个高级Python脚本,使用OpenAI、Mistral AI或Anthropic的Claude API将Markdown文件从源语言翻译成目标语言。它设计得灵活易用,提供了额外的选项,如添加翻译说明、改进的输出文件管理、现有文件检测,以及支持多种语言和翻译模型。

如需演示和详细说明,请访问[jls42.org](https://jls42.org/)或翻译版本:[jls42.org English](https://jls42.org/traductions_en/)、[jls42.org Español](https://jls42.org/traductions_es/)和[jls42.org 中文](https://jls42.org/traductions_zh/)。

## 主要特点

- **AI驱动翻译**:使用OpenAI、Mistral AI或Anthropic的Claude的最新AI技术翻译您的文档。
- **多语言支持**:使用不同的语言模型将文档翻译成多种语言。
- **智能分段**:通过自动分段有效处理长文本。
- **翻译说明**:自动添加翻译说明,告知读者所使用的过程。
- **改进的输出文件管理**:在开始翻译前检查翻译是否已存在。
- **改进的现有文件检测**:搜索与原始文件基本名称和目标语言相匹配的文件。
- **灵活可扩展**:代码结构便于添加新功能。

## 先决条件

- Python 3.6或更高版本。
- OpenAI、Mistral AI或Anthropic的Claude的有效API密钥。

## 安装

1. 克隆Git存储库:
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. 安装必要的依赖项:
```
pip install -r requirements.txt
```

## 配置

通过设置必要的API密钥的环境变量来配置您的环境:

- **OpenAI**:
    ```
    export OPENAI_API_KEY='your-openai-api-key'
    ```
- **Mistral AI**:
    ```
    export MISTRAL_API_KEY='your-mistral-api-key'
    ```
- **Anthropic的Claude**:
    ```
    export ANTHROPIC_API_KEY='your-anthropic-api-key'
    ```

## 使用

该脚本提供了几个选项来自定义翻译过程:

### 通用选项

- `--source_dir`:包含要翻译的Markdown文件的目录。
- `--target_dir`:翻译文件的输出目录。
- `--model`:要使用的GPT翻译模型。默认模型取决于所选的API。
- `--source_lang`:文档的源语言。特别重要,尤其是在添加翻译说明时。
- `--target_lang`:翻译的目标语言。默认为英语。
- `--force`:即使文件已有翻译,也强制翻译。

### 特定API选项

- `--use_mistral`:使用Mistral AI API进行翻译。
- `--use_claude`:使用Anthropic的Claude API进行翻译。
- `--add_translation_note`:在翻译内容中添加翻译说明,指定使用的方法和工具。

### 使用示例

- 使用OpenAI从法语翻译成英语,添加翻译说明:
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- 使用Mistral AI从法语翻译成西班牙语,不添加翻译说明:
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## 作者

Julien LE SAUX
电子邮件:contact@jls42.org

## 许可

本项目采用GNU通用公共许可证第3版,2007年6月29日。有关详细信息,请参阅[LICENSE](LICENSE)文件。

**本文档已从fr版本使用claude-3-5-sonnet-20240620模型翻译成zh语言。有关翻译过程的更多信息，请访问https://gitlab.com/jls42/ai-powered-markdown-translator。**

