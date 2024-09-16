### 更新日志

- **1.0** 初始版本 - 支持 OpenAI API
- **1.1** 添加对 Mistral IA API 的支持
- **1.2** 修复更新日志
- **1.3** 改进和新功能：
    - 改进代码块管理
    - 改进输出文件管理
    - 改进现有文件检测
    - 添加 `--force` 选项以强制翻译
    - 翻转输出文件名中的模型和语言
- **1.4** 新功能：
    - 支持 Anthropics 的 Claude API 进行翻译
    - 优化提示以提高清晰度和效率
    - 小调整以改善代码维护
- **1.5** 改进：
    - **更新默认的 API 密钥和模型：**
        - **OpenAI：** 更新 `DEFAULT_MODEL_OPENAI` 为 `"gpt-4o"`。
        - **Mistral AI：** 更新 `DEFAULT_MODEL_MISTRAL` 为 `"mistral-large-latest"`。
        - **Claude d'Anthropic：** 添加 `DEFAULT_ANTHROPIC_API_KEY` 并更新 `DEFAULT_MODEL_CLAUDE` 为 `"claude-3-5-sonnet-20240620"`。
    - **优化翻译提示：**
        - 直接翻译和翻译注释的提示已完善，以提高清晰度和效率，包括详细说明如何保留元数据和特定格式元素。
    - **代码重构：**
        - 用 `Mistral` 类替换 `MistralClient` 进行 Mistral AI 客户端初始化。
        - 重组导入以提高可读性和维护性。
        - 改进文本分割和代码块管理，以在翻译时保留原始格式。
    - **输出文件管理：**
        - 翻转输出文件名中的模型和语言（例如，`f"{base}-{args.target_lang}-{args.model}.md"`），以便于组织和搜索翻译。
    - **各种改进：**
        - 清理代码，删除不必要的空行。
        - 小调整以改善脚本的结构和可读性。

**此文件是使用 gpt-4o 模型从法语版本翻译成中文。有关翻译过程的更多信息，请参阅 https://gitlab.com/jls42/ai-powered-markdown-translator**

