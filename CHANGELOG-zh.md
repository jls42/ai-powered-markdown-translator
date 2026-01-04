### 更新日志

🌍 [英文](CHANGELOG-en.md) | [西班牙语](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [德语](CHANGELOG-de.md) | [日语](CHANGELOG-ja.md) | [韩语](CHANGELOG-ko.md) | [阿拉伯语](CHANGELOG-ar.md) | [印地语](CHANGELOG-hi.md) | [意大利语](CHANGELOG-it.md) | [荷兰语](CHANGELOG-nl.md) | [波兰语](CHANGELOG-pl.md) | [葡萄牙语](CHANGELOG-pt.md) | [罗马尼亚语](CHANGELOG-ro.md) | [瑞典语](CHANGELOG-sv.md)

- **1.7** 新功能：
    - 选项 `--keep_filename`，用于在翻译时保留原始文件名
    - 支持文件 `.env`，用于自动加载 API 密钥
    - **保留行内代码**：反引号（`` `...` ``）现在在翻译时受到保护
    - 系统提示词改进：
        - 更好地处理 YAML frontmatter 中的引号
        - 保护模板变量 `{variable}`
        - 禁止未请求的译者注释
    - 在 364 个文件上成功测试（迁移博客 jls42.org）
- **1.6** 新功能：
    - 支持 Google Gemini API 进行翻译（`--use_gemini`）
    - 2026 年默认模型更新：
        - OpenAI：`gpt-5`（质量），`gpt-5-mini`（经济）
        - Claude：`claude-sonnet-4-5`（质量），`claude-haiku-4-5`（经济）
        - Gemini：`gemini-3-pro-preview`（质量），`gemini-3-flash-preview`（经济）
    - 经济模式（`--eco`），用于使用更快且更便宜的模型
    - 单文件翻译（`--file`），无需遍历目录
    - 新的简化命名模式：`{base}-{lang}.md`
    - 选项 `--include_model`，用于保留包含模型名称的旧格式
    - 支持未列出的模型，默认 token 限制为（128k）
    - README 已翻译为 14 种语言
- **1.5** 改进：
    - **更新 API 密钥和默认模型：**
        - **OpenAI：** 将 `DEFAULT_MODEL_OPENAI` 更新为 `"gpt-4o"`。
        - **Mistral AI：** 将 `DEFAULT_MODEL_MISTRAL` 更新为 `"mistral-large-latest"`。
        - **Anthropic 的 Claude：** 添加了 `DEFAULT_ANTHROPIC_API_KEY` 并将 `DEFAULT_MODEL_CLAUDE` 更新为 `"claude-3-5-sonnet-20240620"`。
    - **优化翻译提示词：**
        - 用于直接翻译和翻译注释的提示词已增强，以提高清晰度和效率，包含关于保留元数据和特定格式元素的详细指示。
    - **代码重构：**
        - 将 `MistralClient` 替换为类 `Mistral` 用于初始化 Mistral AI 客户端。
        - 重组导入以提高可读性和维护性。
        - 改进文本分段和代码块处理，以在翻译时保留原始格式。
    - **输出文件管理：**
        - 在输出文件名中将模型和语言颠倒（例如，`f"{base}-{args.target_lang}-{args.model}.md"`），从而便于组织和查找翻译。
    - **其他改进：**
        - 通过删除不必要的空行清理代码。
        - 进行小幅调整以改善脚本结构和可读性。
- **1.4** 新功能：
    - 支持 Anthropic 的 Claude API 进行翻译
    - 优化提示词以提高清晰度和效率
    - 若干小调整以改进代码维护性
- **1.3** 改进与新功能：
    - 改进的代码块处理
    - 改进的输出文件管理
    - 改进的现有文件检测
    - 选项 `--force` 用于强制翻译
    - 在输出文件名中颠倒模型和语言
- **1.2** 修复更新日志
- **1.1** 添加对 Mistral AI API 的支持
- **1.0** 初始版本 - 支持 OpenAI API

**本文件已使用 gpt-5-mini 模型将法语（fr）版本翻译为中文（zh）。有关翻译过程的更多信息，请参阅 https://gitlab.com/jls42/ai-powered-markdown-translator**

