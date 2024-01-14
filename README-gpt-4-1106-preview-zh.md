以下是用Markdown写成的README文件内容，用于您的翻译脚本：

# OpenAI Markdown翻译器

这个项目是一个Python脚本，它使用OpenAI的API来将Markdown文件从源语言翻译成目标语言。
更多关于[人工智能翻译 jls42.org](https://jls42.org/posts/ia/automatisation-traduction-ia/)的信息。

## 前提条件

要使用这个脚本，您需要：

- Python 3.6 或更高版本
- 一个带有API密钥的OpenAI账户

## 安装

1. 克隆此存储库到您的本地机器。
2. 使用pip安装所需依赖项：

```bash
pip install -r requirements.txt
```

## 使用方法

在使用这个脚本之前，您首先需要将您的OpenAI API密钥设为环境变量：

```bash
export OPENAI_API_KEY='votre-clé-api'
```


然后，您可以使用以下命令来运行脚本：

```bash
python translate.py --source_dir 'chemin/vers/votre/répertoire/source' --target_dir 'chemin/vers/votre/répertoire/cible'
```

您还可以指定模型、源语言和目标语言：

```bash
python translate.py --source_dir 'chemin/vers/votre/répertoire/source' --target_dir 'chemin/vers/votre/répertoire/cible' --model 'gpt-4-1106-preview' --source_lang 'fr' --target_lang 'en'
```

## 使用示例

```bash
################################################
# Demande de traduction à l'IA vers l'espagnol #
################################################
jls42@Boo:~/blog/jls42$ python3 translate.py --source_dir content/ --target_dir content/traductions_es --target_lang es
Traitement du fichier : content/posts/ia/stable-difusion-aws-ec2.md
Traduction terminée en 33.19 secondes.
Fichier 'stable-difusion-aws-ec2.md' traité.
Traitement du fichier : content/posts/ia/poc-openai-api-gpt4.md
Traduction terminée en 25.24 secondes.
Fichier 'poc-openai-api-gpt4.md' traité.
Traitement du fichier : content/posts/ia/poc-mistral-ai-mixtral.md
Traduction terminée en 58.78 secondes.
Fichier 'poc-mistral-ai-mixtral.md' traité.
Traitement du fichier : content/posts/raspberry-pi/installation-de-kubernetes-sur-raspberry-pi-via-ansible.md
Traduction terminée en 17.64 secondes.
Fichier 'installation-de-kubernetes-sur-raspberry-pi-via-ansible.md' traité.
Traitement du fichier : content/posts/raspberry-pi/installation-de-docker-sur-raspberry-pi-via-ansible.md
Traduction terminée en 19.60 secondes.
Fichier 'installation-de-docker-sur-raspberry-pi-via-ansible.md' traité.
Traitement du fichier : content/posts/raspberry-pi/initialisation-auto-de-raspbian-sur-raspberry-pi.md
Traduction terminée en 37.12 secondes.
Fichier 'initialisation-auto-de-raspbian-sur-raspberry-pi.md' traité.
Traitement du fichier : content/posts/blog/nouveau-theme-logo.md
Traduction terminée en 18.91 secondes.
Fichier 'nouveau-theme-logo.md' traité.
Traitement du fichier : content/posts/infrastructure/infrastruture-as-code-serverless-ha-jls42-org.md
Traduction terminée en 30.73 secondes.
Fichier 'infrastruture-as-code-serverless-ha-jls42-org.md' traité.
Traitement du fichier : content/mentions/mentions-legales.md
Traduction terminée en 13.14 secondes.
Fichier 'mentions-legales.md' traité.
Traitement du fichier : content/about/a-propos-du-blog-jls42.md
Traduction terminée en 11.24 secondes.
Fichier 'a-propos-du-blog-jls42.md' traité.
```

## 许可证

该项目在GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007下授权。更多详情见[LICENSE](LICENSE)文件。

**这份文档是由 gpt-4-1106-preview 模型从法语博客的版本翻译过来的。**

