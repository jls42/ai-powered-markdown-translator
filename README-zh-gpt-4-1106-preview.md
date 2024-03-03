# OpenAI和Mistral AI驱动的Markdown翻译器

这个项目是一个高级Python脚本，它使用OpenAI API或Mistral AI API来将Markdown文件从源语言翻译成目标语言。它旨在灵活且易于使用，提供诸如添加翻译注释、改进的输出文件管理、现有文件检测以及支持多种语言和翻译模型的额外选项。

想要演示和详细说明，请访问[jls42.org](https://jls42.org/)或翻译版本：[jls42.org English](https://jls42.org/traductions_en/)、[jls42.org Español](https://jls42.org/traductions_en/)和[jls42.org 中文](https://jls42.org/traductions_zh/)。

## 主要特点

- **AI驱动翻译**：使用最新的AI技术翻译您的文件。
- **多语言支持**：支持多种语言的文件翻译和不同语言模型。
- **智能分段**：通过自动化分段有效管理长文本。
- **翻译注记**：自动添加翻译注记，以告知读者所使用的过程。
- **改进的输出文件管理**：在开始翻译前检查是否已存在翻译。
- **提升的现有文件检测**：搜索与原始文件基本名称和目标语言相匹配的文件。
- **灵活和可扩展**：代码结构使得添加新功能变得更加容易。

## 先决条件

- Python 3.6或更高版本。
- 有效的OpenAI或Mistral AI API密钥。

## 安装

1. 克隆Git仓库：
```
git clone https://github.com/votre-repertoire/translate-markdown.git
```
2. 安装必要的依赖：
```
pip install -r requirements.txt
```

## 配置

在启动脚本之前，请设置您的环境：

- **OpenAI**：将您的OpenAI API密钥设置为环境变量：
```
export OPENAI_API_KEY='votre-clé-api-openai'
```
- **Mistral AI**：将您的Mistral AI API密钥设置为环境变量：
```
export MISTRAL_API_KEY='votre-clé-api-mistral'
```

## 使用

要翻译Markdown文件：

- **使用OpenAI**：
```
python translate.py --source_dir 'source/path' --target_dir 'target/path'
```
- **使用Mistral AI**（和翻译注记选项）：
```
python translate.py --use_mistral --source_dir 'source/path' --target_dir 'target/path' --model 'mistral-small' --add_translation_note
```

### 常用选项

- 指定模型、源语言和目标语言：
```
python translate.py --source_dir 'source/path' --target_dir 'target/path' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
```

### 新选项

- 即使已存在翻译也强制翻译：
```
python translate.py --source_dir 'source/path' --target_dir 'target/path' --force
```

## 使用示例

- 西班牙语翻译请求示例：
```
python translate.py --source_dir content/ --target_dir content/traductions_es --target_lang es
```


## 作者

Julien LE SAUX  
电子邮件：contact@jls42.org


## 许可证

该项目基于GNU通用公共许可证版本3，2007年6月29日。有关更多详细信息，请参见[LICENSE](LICENSE)文件。

**这个文件已经从fr版本翻译成zh语言，使用的是gpt-4-1106-preview模型。要了解更多关于翻译过程的信息，请访问 https://gitlab.com/jls42/ai-powered-markdown-translator**

