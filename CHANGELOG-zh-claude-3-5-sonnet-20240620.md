### 更新日志

- **1.0** 初始版本 - 支持OpenAI API
- **1.1** 添加Mistral IA API支持
- **1.2** 修复更新日志
- **1.3** 改进和新功能：
    - 改进代码块处理
    - 改进输出文件处理
    - 改进现有文件检测
    - `--force`选项强制翻译
    - 在输出文件名中反转模型和语言
- **1.4** 新功能：
    - 支持Anthropic的Claude API进行翻译
    - 优化提示以提高清晰度和效率
    - 小调整以改善代码维护
- **1.5** 改进：
    - **更新API密钥和默认模型：**
        - **OpenAI：** 将`DEFAULT_MODEL_OPENAI`更新为`"gpt-4o"`。
        - **Mistral AI：** 将`DEFAULT_MODEL_MISTRAL`更新为`"mistral-large-latest"`。
        - **Anthropic的Claude：** 添加`DEFAULT_ANTHROPIC_API_KEY`并将`DEFAULT_MODEL_CLAUDE`更新为`"claude-3-5-sonnet-20240620"`。
    - **优化翻译提示：**
        - 直接翻译和翻译注释的提示已得到改进，以提高清晰度和效率，包括关于保留元数据和特定格式元素的详细说明。
    - **代码重构：**
        - 用`Mistral`类替换`MistralClient`以初始化Mistral AI客户端。
        - 重新组织导入以提高可读性和可维护性。
        - 改进文本分段和代码块处理，以在翻译过程中保留原始格式。
    - **输出文件处理：**
        - 在输出文件名中反转模型和语言（例如，`f"{base}-{args.target_lang}-{args.model}.md"`），从而便于组织和搜索翻译。
    - **其他改进：**
        - 通过删除不必要的空行清理代码。
        - 对脚本结构和可读性进行小调整。

**本文档已使用claude-3-5-sonnet-20240620模型从fr版本翻译成zh语言。有关翻译过程的更多信息，请参阅https://gitlab.com/jls42/ai-powered-markdown-translator。**

