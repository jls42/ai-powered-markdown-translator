### 变更日志

- **1.0** 初始版本 - 支持OpenAI API
- **1.1** 添加对Mistral AI API的支持
- **1.2** 修复变更日志
- **1.3** 改进和新功能：
    - 改进代码块管理
    - 改进输出文件管理
    - 改进现有文件检测
    - 添加 `--force` 选项以强制翻译
    - 在输出文件名中反转模型和语言
- **1.4** 新增功能：
    - 支持Anthropic的Claude API进行翻译
    - 优化提示以提高清晰度和效率
    - 进行小调整以改进代码维护
- **1.5** 改进：
    - **更新API密钥和默认模型：**
        - **OpenAI：** 将 `DEFAULT_MODEL_OPENAI` 更新为 `"gpt-4o"`。
        - **Mistral AI：** 将 `DEFAULT_MODEL_MISTRAL` 更新为 `"mistral-large-latest"`。
        - **Anthropic的Claude：** 添加 `DEFAULT_ANTHROPIC_API_KEY` 并将 `DEFAULT_MODEL_CLAUDE` 更新为 `"claude-3-5-sonnet-20240620"`。
    - **优化翻译提示：**
        - 为直接翻译和翻译笔记的提示进行了丰富，以提高清晰度和效率，包括关于保留元数据和特定格式元素的详细说明。
    - **重构代码：**
        - 用 `Mistral` 类替换 `MistralClient` 以初始化Mistral AI客户端。
        - 重新组织导入以提高可读性和维护性。
        - 改进文本分段和代码块管理，以在翻译时保留原始格式。
    - **管理输出文件：**
        - 在输出文件名中反转模型和语言（例如，`f"{base}-{args.target_lang}-{args.model}.md"`），从而方便组织和查找翻译。
    - **其他改进：**
        - 删除不必要的空行以清理代码。
        - 进行小调整以改进脚本的结构和可读性。

**Ce document a été traduit de la version fr vers la langue zh en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator.**

