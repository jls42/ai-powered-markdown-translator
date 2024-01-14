'# 使用 OpenAI 和 Mistral AI 的 Markdown 翻译工具

本项目是一个 Python 脚本，使用 OpenAI 的 API 或 Mistral AI 的 API 来将源语言的 Markdown 文件翻译成目标语言。
更多信息请参见 [jls42.org 的人工智能翻译](https://jls42.org/posts/ia/automatisation-traduction-ia/)。

## 先决条件

使用此脚本需要：

- Python 3.6 或更高版本
- OpenAI 账号 avec API key，或者 Mistral AI 账号 with API key

## 安装

1. 将此存储库克隆到您的本地机器。
2. 使用 pip 安装所需的依赖项：

   ```bash
   pip install -r requirements.txt
   ```

## 使用

### 与 OpenAI 一起使用

要使用 OpenAI 与此脚本，首先需要在环境变量中定义您的 OpenAI API key：

   ```bash
   export OPENAI_API_KEY='您的 API key'
   ```

然后，可以使用以下命令运行脚本：

   ```bash
   python translate.py --source_dir '您的源目录' --target_dir '您的目标目录'
   ```

### 与 Mistral AI 一起使用

要使用 Mistral AI 与此脚本，首先需要在环境变量中定义您的 Mistral AI API key：

   ```bash
   export MISTRAL_API_KEY='您的 Mistral API key'
   ```

然后，使用 `--use_mistral` 选项运行脚本：

   ```bash
   python translate.py --use_mistral --source_dir '您的源目录' --target_dir '您的目标目录' --model 'mistral-small'
   ```

### 通用选项

您还可以指定要使用的模型，源语言和目标语言：

   ```bash
   python translate.py --source_dir '您的源目录' --target_dir '您的目标目录' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
   ```

## 用法示例

   ```bash
   #################################
   # 将 IA 的翻译请求发送到西班牙 #
   #################################
   jls42@Boo:~/blog/jls42$ python3 translate.py --source_dir content/ --target_dir content/traductions_es --target_lang es
   Processing file: content/posts/ia/stable-difusion-aws-ec2.md
   Translation completed in 33.19 seconds.
   File 'stable-difusion-aws-ec2.md' processed.
   # ... 其他输出结果 ...
   ```

## 许可

此项目已获 GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 的授权。
有关更多详细信息，请参阅文件 [LICENSE](LICENSE)。'

**这个文档是由 mistral-small 模型从法语博客版本翻译过来的。

(Note: The English translation of the text is: "This document has been translated from the French version of the blog by the mistral-small model.")**

