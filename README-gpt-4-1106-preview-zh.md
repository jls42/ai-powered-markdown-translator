# 使用OpenAI和Mistral AI进行Markdown翻译的脚本

该项目是一个Python脚本，它使用OpenAI或Mistral AI的API来将Markdown文件从源语言翻译成目标语言。
更多信息请参见[人工智能翻译 jls42.org](https://jls42.org/posts/ia/automatisation-traduction-ia/)。

## 先决条件

要使用此脚本，您需要：

- Python 3.6 或更高版本
- 一个带有API密钥的OpenAI账户或一个带有API密钥的Mistral AI账户

## 安装

1. 克隆此仓库到您的本地机器。
2. 使用pip安装必要的依赖：

   ```bash
   pip install -r requirements.txt
   ```

## 使用

### 使用OpenAI

要使用OpenAI的脚本，您首先需要将您的OpenAI API密钥设置为环境变量：

   ```bash
   export OPENAI_API_KEY='您的api密钥'
   ```

然后，您可以使用以下命令运行脚本：

   ```bash
   python translate.py --source_dir '源目录/路径' --target_dir '目标目录/路径'
   ```

### 使用Mistral AI

要使用Mistral AI的脚本，您首先需要将您的Mistral AI API密钥设置为环境变量：

   ```bash
   export MISTRAL_API_KEY='您的mistral-api密钥'
   ```

然后，使用`--use_mistral`选项运行脚本：

   ```bash
   python translate.py --use_mistral --source_dir '源目录/路径' --target_dir '目标目录/路径' --model 'mistral-small'
   ```

### 通用选项

您还可以指定要使用的模型，源语言和目标语言：

   ```bash
   python translate.py --source_dir '源目录/路径' --target_dir '目标目录/路径' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
   ```

## 使用示例

   ```bash
   ################################################
   # 向人工智能请求翻译成西班牙语 #
   ################################################
   jls42@Boo:~/blog/jls42$ python3 translate.py --source_dir content/ --target_dir content/traductions_es --target_lang es
   处理文件：content/posts/ia/stable-difusion-aws-ec2.md
   翻译完成时间：33.19秒。
   文件'stable-difusion-aws-ec2.md'已处理。
   # ... 其他结果行 ...
   ```

## 许可证

该项目采用GNU GENERAL PUBLIC LICENSE 版本3，2007年6月29日。更多详细信息，请查阅 [LICENSE](LICENSE) 文件。

**此文件已由 gpt-4-1106-preview 模型从博客的法文版本翻译。**

