# AI 驱动的 Markdown 翻译器

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 代码质量</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Quality Gate Status"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Security Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Reliability Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Maintainability Rating"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Coverage"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilities"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Duplicated Lines (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technical Debt"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Lines of Code"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy Badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

在保留结构的前提下跨语言翻译 Markdown 文件：保留代码块、行内代码、URL、锚点、表格和 front matter。提供 11 种模型调用方式——5 种 API、4 种免按量计费的订阅服务、2 种路由服务——并公开了每个模型实际保留效果的评测数据。

## 概览

- **11 种 Provider 接入路径**：OpenAI、Mistral、Claude、Gemini 和 Grok 的 API；ChatGPT (Codex)、Grok、Google (Antigravity) 和 Claude (Claude Code) 的免按量计费订阅；OpenCode（开源、免费或本地）与 OpenRouter（400 多种模型）路由服务。
- **杜绝因 Token 丢失导致的损坏**：代码块、行内代码、URL、锚点和引用在调用前均被替换为标记，返回时进行严格核对。只要缺失一个标记，就不会写入文件。
- **长文档支持**：根据模型上下文窗口自动进行分段。
- **`--news` 模式**：受保护的英文引文并按目标语言管理国旗图标，专为行业资讯/技术周报文章设计。
- **`--eco` 模式**：选用更快速且成本更低的模型。
- **可选翻译声明**：可放置在顶部、底部或同时放置。

## 安装

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

需要 Python 3.11 或更高版本。若要从仓库安装，请参阅[参与贡献](#贡献)。

## 配置

程序会从三个位置按优先级由高到低读取密钥；每个位置仅补充前序位置未提供的值。

|     | 位置                                          | 适用场景                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 环境变量                                      | CI、容器、临时覆盖                    |
| 2   | 当前目录（或父目录）下的 `.env`         | 项目专属密钥                          |
| 3   | `~/.config/aipmt/.env`                                 | 一次配置，全局生效                    |

```bash
mkdir -p ~/.config/aipmt
cat > ~/.config/aipmt/.env <<'EOF'
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
OPENROUTER_API_KEY=votre-clé-api-openrouter
EOF
chmod 600 ~/.config/aipmt/.env
```

支持使用 `GEMINI_API_KEY` 代替 `GOOGLE_API_KEY`。用户配置文件在 Linux/macOS 下遵循 `XDG_CONFIG_HOME`（仅支持绝对路径），在 Windows 下遵循 `%APPDATA%`。如果未提供密钥，命令将列出这三个配置位置。

**项目内的 `.env` 既不能重定向请求调用，也不能指定执行的程序。** 它仅用于提供密钥，绝不能包含请求目标地址或二进制程序：任何以 `_BASE_URL`、`_API_BASE`、`_ENDPOINT` 或 `_BIN` 开头的变量（`CODEX_BIN`、`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`）、`GROK_HOME`、代理变量（`HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY`）、证书存储路径（`SSL_CERT_FILE`、`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）以及 `XDG_CONFIG_HOME` / `APPDATA` 都会被忽略并给出警告。克隆的项目仓库绝不能窃取您的密钥，也不能在您首次执行翻译时诱导运行其自带的程序。此文件读取时亦不进行插值替换：`NOM=${OPENAI_API_KEY}` 不会在其中复制密钥。请将这些变量配置在环境变量或 `~/.config/aipmt/.env` 中。

可选变量：`XAI_BASE_URL`（默认 `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（每次调用超时秒数，默认 900）、`CODEX_BIN`、`CODEX_TIMEOUT`（默认 600）、`GROK_BIN`、`GROK_HOME`（默认 `~/.grok`）、`GROK_TIMEOUT`（默认 900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（默认 900）、`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（默认 600）、`OPENROUTER_BASE_URL`（需 `https://`）、`OPENROUTER_TIMEOUT`（默认 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（默认 30）。各变量详细信息请参见对应 Provider 的说明章节。

## 快速入门

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

将 `document.md` 翻译为西班牙语后，将在 `--target_dir` 中生成 `document-es.md`；使用 `--include_model` 参数时则生成 `document-es-gpt-6.1-terra.md`。扩展名始终转换为 `.md`（例如 `article.mdx` 会生成 `article-en.md`）——除非指定 `--keep_filename`，此时将保留原始文件名。若不添加 `--force` 参数，已存在的翻译将被自动跳过。

退出代码：全部成功或已跳过时返回 `0`；若有文件翻译失败则返回 `1`（并在标准错误中列出）；配置错误时返回 `2`。失败的文件绝不会被写入，即使在写入阶段发生错误亦是如此：内容会先写入临时文件然后再进行重命名。直接重新运行即可。

## 模型选择指南

以下是在两篇真实文档上测试的数据，每个模型分别翻译成相同的 14 种语言。**数值代表在 14 种语言中，成功写入翻译且与源文档完全一致的语言数量。**

| 模型                  | 访问途径                          | 高密度技术资讯文章      | 本 README    | 差异内容及涉及语言数                                                                                                               |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.8 Flash**  | Google 订阅 (Antigravity)         | ✅ 14/14                | ✅ 14/14     | 两篇文档在所有语言中均无差异                                                                                                       |
| **Claude Sonnet 5.5** | Anthropic API 密钥                | ✅ 14/14                | ✅ 14/14     | 两篇文档在所有语言中均无差异                                                                                                       |
| **Gemini 3.7 Flash**  | Google API 密钥                   | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种：多出一个加粗词 (ja)                                                                                           |
| **Gemini 3.7 Flash**  | Google 订阅 (Antigravity)         | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种：少了一个加粗词 (ko)                                                                                           |
| **GPT-5.6 Sol**       | ChatGPT 订阅或 OpenAI 密钥        | ✅ 14/14                | ⚠️ 12/14     | 14 种语言中有 2 种：少了一个加粗词 (ar, ja)                                                                                        |
| **GLM-5.2**           | OpenRouter 密钥                   | ✅ 14/14                | ⚠️ 11/14     | 14 种语言中有 3 种：少了一个加粗词 (hi, ja, ko)                                                                                    |
| Claude Sonnet 5       | Claude 订阅 (Claude Code)         | ⚠️ 13/14                | ⚠️ 13/14     | 资讯文章 14 种语言中有 1 种：多出一个加粗词 (zh)；本 README 有 1 种：表格行与上一行粘连，导致渲染隐藏 (ar)                        |
| Claude Haiku 4.5      | Claude 订阅 (Claude Code)         | ⚠️ 11/14                | ✅ 14/14     | 资讯文章中有 3 种语言：某一节标题变成了 1 级标题 (en, pl, ro)；本 README 中校验完全一致，但内部链接在英文版中重复出现              |
| Claude Sonnet 5       | Anthropic API 密钥                | ⚠️ 11/14                | ⚠️ 12/14     | 资讯文章中有 3 种语言多出了代码块 (es, de, hi)；本 README 中有 2 种语言：链接缺少标记 (sv)、多出一个加粗词 (zh)                   |
| Claude Haiku 4.5      | Anthropic API 密钥                | ⚠️ 7/14                 | ✅ 14/14     | 资讯文章中有 7 种语言：某一节标题变成了 1 级标题（日语版中甚至保留了法语原文）；本 README 中完全无差异                             |
| Claude Haiku 5.5      | Anthropic API 密钥                | ⚠️ 11/14                | ❌ 12/14     | 资讯文章中有 3 种语言标题级别变更或重复 (ja, ko, zh)；本 README 中 2 种语言被拒，行内代码丢失 (ar, hi)                             |
| Qwen 3.7 Flash        | OpenRouter 密钥                   | ❌ 8/14                 | ⚠️ 10/14     | 资讯文章有 1 种语言被拒，另外 5 种出现偏差；本 README 中约有 40 个词被误加上了 `code` (ar)                                  |
| Grok 4.6              | Grok 订阅                         | ❌ 8/14                 | 未评测       | 14 种语言中有 5 种因未能完整返回行内代码和 URL 而被拒；荷兰语版在所有方面均产生脱节偏差                                            |
| GPT-OSS 20B           | 本地模型 (Ollama)                 | ❌ 7/14                 | 未重新评测   | 14 种语言中有 4 种被拒：模型在译文中残留了法语片段，被防护机制拦截                                                                 |
| MiMo v2.5 (免费)      | OpenCode Zen，免账户              | ❌ 11/14                | 未重新评测   | 1 种语言被拒；波兰语版丢失了一整个章节                                                                                             |
| Mistral Large         | Mistral API 密钥                  | ❌ 5/14                 | ❌ 1/14      | **丢失了整整一个章节**：资讯文章中有 1 种语言丢失 (hi)，本 README 中有 3 种语言丢失 (ar, hi, ko)——资讯文章另有 3 种语言被拒         |
| DeepSeek V4 Flash     | OpenRouter 密钥                   | ❌ 3/14                 | 未重新评测   | 14 种语言中有 10 种被拒；每种语言耗时 37 分钟                                                                                      |
| Claude Opus 5.5       | Claude 订阅 (Claude Code)         | ❌ 0/14                 | ✅ 14/14     | 资讯文章因一条生物学科普简讯触发 Opus 安全护栏，导致 14 种语言全部被拒；本 README 中完全无差异                                     |

|     | 符号含义                                                                                                                                                                                              |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14 种语言全部完成翻译，且结构与源文档完全一致                                                                                                                                                         |
| ⚠️  | 14 种语言全部完成翻译；存在的差异仅为**标记细节**——例如多出/少了一个加粗词、一个 `code`、或是链接丢失了中括号。没有任何正文文本、URL、代码块或章节发生丢失                                    |
| ❌  | 至少有一种语言未能完成翻译（文件被拒，未写入），**或者**已写入的文件中存在内容缺失                                                                                                                     |

核心要点分析：

- **被拒绝的翻译并不等同于损坏的翻译。** 当返回结果缺少标记时，文件不会被写入，该语言会被计为被拒。Grok 在资讯文章测试中即属此类：在 5 种非拉丁脚本语言中，仅第一个分段就丢失了 4 个行内代码和 3 个 URL。
- **模型可能仅因一句话而拒绝整个文档。** Opus 5.5 翻译本 README 时分毫不差，但翻译资讯文章时却全军覆没：其安全护栏机制因一条生物学简讯中断了响应。文件没有被写入，且 aipmt 会明确说明原因。
- **该安全网无法覆盖标题、表格、front matter 或正文文本。** 如果模型删除了某个章节，工具会照常写入该文件——Mistral 便出现了这种情况。这些元素无法使用标记进行简单替换，当前防护机制也未对其进行核查；`scripts/compare_structure.py` 可以在事后检测出丢失的章节，但无法在写入前拦截。
- **Grok 在本 README 上暂无评分**：其 CLI 会话在翻译完成 12 种语言（其中 11 种无差异）后过期中断。中断的测试不予计分。
- **文档的密度比目标语言更具挑战性。** Grok 处理普通的 README 游刃有余，但在面对包含大量链接的高密度资讯文章时则会出现掉链子的情况，哪怕是翻译为荷兰语也是如此。

测试日期与文档说明：“本 README”列评测于 2026 年 9 月 9 日，基于本文件的固定版本（785 行，285 处行内代码，89 行表格，此后该文件有修改）——但 Antigravity 和 Claude Code 评测于 9 月 26 日，基于随 1.14.0 发布的较短版本（600 行，257 处行内代码，85 行表格）；Claude Sonnet 5.5、Haiku 5.5 和 Haiku 4.5 API 则于 10 月 18 日基于相同版本进行评测。“高密度技术资讯文章”列源自 9 月 4 日至 5 日对一篇 589 行文章的测试，其中 Grok 于 9 月 9 日在另一期同类资讯文章上重新测试，Antigravity 和 Claude Code 于 9 月 26 日在同一文章上测试，上述三款 Claude 模型则于 10 月 18 日测试。完整的测试表格、耗时和测试规范请参见[详细评测数据](#详细评测指标)。

## 所有选项

| 选项                     | 说明                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | 要翻译的单个 Markdown 文件（替代 `--source_dir`）                                                             |
| `--source_dir`           | 包含 Markdown 文件的源目录（默认：`content/posts`）                                                            |
| `--target_dir`           | 翻译后文件的输出目录（默认：`traductions_en`）                                                                  |
| `--source_lang`           | 源语言（默认：`fr`）                                                                                |
| `--target_lang`           | 目标语言（默认：`en`）                                                                              |
| `--model`           | 要使用的特定模型                                                                                              |
| `--eco`           | 使用经济型模型                                                                                                |
| `--use_mistral`           | 使用 Mistral AI API                                                                                           |
| `--use_claude`           | 使用 Claude API                                                                                               |
| `--use_gemini`           | 使用 Gemini API                                                                                               |
| `--use_grok`           | 使用 xAI (Grok) API —— 需要 `XAI_API_KEY`                                                                    |
| `--use_codex`           | 使用 ChatGPT 订阅配额运行 Codex CLI                                                                           |
| `--use_grok_cli`           | 使用 Grok 订阅配额运行 Grok CLI                                                                               |
| `--use_antigravity`           | 使用 Google AI Pro 或 Ultra 订阅配额运行 Antigravity CLI（`agy`）                                   |
| `--use_claude_code`           | 使用 Claude Pro 或 Max 订阅配额运行 Claude Code CLI（`claude -p`）                                         |
| `--use_opencode`           | 使用 OpenCode（开源）连接其配置的提供商；需要 `--model provider/modèle`                                                  |
| `--use_openrouter`           | 使用 OpenRouter —— 需要 `OPENROUTER_API_KEY` 和 `--model fournisseur/modèle`                                                      |
| `--force`           | 强制重新翻译                                                                                                  |
| `--keep_filename`           | 保留原始文件名                                                                                                |
| `--news`           | 新闻模式：保护英文引用，按语言处理国旗/标志                                                                   |
| `--add_translation_note`           | 添加翻译附注                                                                                                  |
| `--note_position`           | 附注位置：`top`、`bottom`（默认）或 `both`                                             |
| `--note_format`           | 附注格式：`legacy`（默认，粗体段落）或 `marker`                                                 |
| `--include_model`          | 在输出文件中包含模型名称                                                                                      |
| `--reasoning_effort`          | GPT-5.x 推理力度：`none`/`low`/`medium`/`high`/`xhigh`              |

这九个 `--use_*` 标志互斥：同时组合两个将被拒绝。

## 提供商

### 通过 API：OpenAI、Mistral、Claude、Gemini、Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` 切换至各提供商的经济型层级。

| 提供商      | 高质量（默认）                                                       | 经济型（`--eco`） |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-6.1-terra`                                                      | `gpt-6-luna`           |
| Claude      | `claude-sonnet-5-5`                                                      | `claude-haiku-5-5`           |
| Mistral     | `mistral-large-latest`                                                      | `mistral-small-latest`           |
| Gemini      | `gemini-4-hydrogen`                                                      | `gemini-3.1-flash-lite`           |
| Codex       | `gpt-6.1-sol`（亦可通过 `--model` 使用 `gpt-5.6-sol`、`terra` 和 `luna`） | `gpt-6-luna`           |
| Grok API    | `grok-4.7`                                                      | `grok-4.3`           |
| Grok CLI    | `grok-4.7`                                                      | 同上 —— `--eco` 无效 |
| Antigravity | `gemini-3.8-flash-medium`                                                      | `gemini-3.8-flash-low`           |
| Claude Code | `sonnet`，推理力度 `low`                            | 同上 —— `--eco` 无效 |
| OpenCode    | 必须指定 `--model provider/modèle`                                             | 同上 —— `--eco` 无效 |
| OpenRouter  | 必须指定 `--model fournisseur/modèle`                                             | 同上 —— `--eco` 无效 |

默认值跟随各提供商的最新一代模型，并在采用前经过实测评估：OpenAI 的 GPT-6、Google 的 Gemini 4 Hydrogen，以及自 1.19.0 起 xAI 的 Grok 4.7。先前的模型仍可通过 `--model` 接受（`gpt-5.6-terra`、`gemini-3.8-flash`、`grok-4.6`……），Google 的高端模型 Gemini 4 Argon 和 Carbon 亦同。aipmt 会自行调节 GPT 和 Grok 的推理力度，在 `--eco` 下关闭，而 `--reasoning_effort` 则会强制指定；Gemini 则始终接收其所能接受的最低级别。
Gemini API 的临时故障（503、429、超时）最多会重试调用三次，间隔分别为 10 秒、20 秒和 40 秒。无响应的尝试会在 5 分钟后放弃，并按同样方式重试：服务器无响应最多在 20 分钟左右导致该分段失败，而不会无限期挂起。

### 使用 ChatGPT 订阅：`--use_codex`

调用官方 Codex CLI：翻译计入 ChatGPT 订阅配额，无需 API 密钥或按用量计费。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 二进制文件会依次在 `CODEX_BIN`、`PATH` 以及 `openai-codex-cli-bin` 软件包中查找。从不读取 `~/.codex/auth.json`。
- `OPENAI_API_KEY` 和 `CODEX_API_KEY` 会从子进程环境中移除：即使存在密钥，也绝不会切换到 API。
- 每个分段至少消耗 5 小时窗口内的 1 次“消息”——若验证失败并重试则消耗 2 次。据 OpenAI 估计，Plus 计划下 `gpt-5.6-luna`（1.18.0 之前的经济型模型）约为 250–2,000 条消息/5 小时，`gpt-5.6-sol` 约为 10–100 条。
- `--model gpt-5.6-sol`（1.16.3 之前的默认值）、`--model gpt-5.6-terra` 和 `--model gpt-5.6-luna` 同样可通过订阅使用。
- 服务器返回 429 不会导致文件丢失：Codex 会自动重连，aipmt 会等待该轮结束，若 429 仍未解决，分段将在 30 秒和 60 秒后重试。账户无权使用的模型会返回 400 “model is not supported when using Codex with a ChatGPT account”。
- 速度慢于 API，且差距随文档变大而增加：对于此 README，使用 `gpt-5.6-sol` 每种语言的中位时间为 6 分 46 秒，而 `gemini-3.7-flash` 为 36 秒。
- 在 CI 环境中被拒绝（设置了 `CI` 或 `GITHUB_ACTIONS`）：订阅通过个人会话文件认证，不应放在共享 Runner 上。
- 环境变量：`CODEX_BIN`、`CODEX_TIMEOUT`（每分段秒数，默认 600）。

### 使用 Grok 订阅：`--use_grok_cli`

官方 Grok Build CLI 亦同，基于 SuperGrok 或 X Premium+ 订阅。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **隔离性弱于 Codex。** Grok 的操作系统沙箱在许多较新的 Linux 主机上无法应用（AppArmor、容器运行时套接字），且无法应用的配置文件会默默以未隔离状态启动。因此，脚本默认不请求任何配置文件，并对此发出提示，而是依赖 CLI 的 `--deny` 规则（包括捕获所有项的 `*`）——这是唯一宁可拒绝启动也不静默移除保护的层级。`GROK_TRANSLATE_SANDBOX=read-only` 强制要求操作系统沙箱，若机器无法满足则启动失败。
- 配额按周计算，与 Chat、Imagine 和 Voice 共享，且没有任何命令可查询该配额：批量运行可能会在没有任何提示的情况下消耗对话配额。
- 环境变量：`GROK_BIN`、`GROK_HOME`（CLI 目录，默认 `~/.grok`）、`GROK_TIMEOUT`（默认 900）、`GROK_TRANSLATE_SANDBOX`。

### 使用 Google 订阅：`--use_antigravity`

Antigravity 官方 CLI `agy` 也是同样原理：对于购买了 Google AI Pro 或 Ultra 的用户，翻译会从订阅配额中扣除，而非按 Token 计费。这是使用该配额的唯一途径：Gemini CLI 自 2026 年 6 月 18 日起不再服务这些账户（[公告](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)），而 Antigravity 的 SDK 仅接受 API 密钥或 Google Cloud 项目。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **不保留任何付费通道。** agy 从您的环境中仅接收一份受限的白名单变量——`PATH`、语言和时区、终端、身份标识、代理与证书、会话总线——而不包含任何密钥：其多个变量可在不显示任何内容的情况下改变调用路由（实测：一个将文档发送到第三方网关，另一个发送到计费的 Google Cloud 项目），且黑名单机制在每次审查时总有遗漏。在处理任何分段前，不消耗任何配额的 `agy -p /config` 必须显示付费 AI 额度已禁用，且无 API 密钥或 Google Cloud 项目——设置缺失即视作拒绝——否则不翻译任何内容；随后每次调用的日志必须证实订阅状态（`authMethod=consumer`），否则响应将被拒绝。
- **隔离保护。** 每次调用都在一个私有的临时个人目录中运行，并使用无工具的翻译代理：您的 agy 设置、规则、插件、MCP 服务器和钩子均不会进入其中，任何内容都不会添加到历史记录中，且登录信息保留在密钥环中，aipmt 绝不读取它。找不到代理会导致 agy 静默回退到其编程代理及工具：日志必须有一整行确认使用了正确的代理——文档中引用此消息并不能代替该日志——否则予以拒绝。
- **平台**：Linux，处于具有密钥环的会话中（D-Bus 会话总线、Secret Service）；支持 macOS，但尚未在此平台上进行实测。Windows 下被拒绝，因为 agy 在该系统下不读取隔离每次调用的变量；在没有会话总线的 Linux 环境下（SSH 会话、容器、服务器）亦被拒绝：agy 会将令牌存放在 `~/.gemini` 的文件中，而隔离机制会将其屏蔽。拒绝提示会在启动前伴随原因给出，无需等待一分钟登录代码。
- **模型**：`agy models` 中的模型。Gemini 模型在名称中包含推理力度（`gemini-3.8-flash-medium`……）：不带后缀的名称会在调用前被拒绝，且 `--reasoning_effort` 无效。由于 agy 不再提供 Gemini 3.7 Flash，默认使用 `gemini-3.8-flash-medium`，在 `--eco` 下使用 `gemini-3.8-flash-low`；确定默认值的测试过程见[详细评测](#详细评测指标)。Gemini 4 Hydrogen（`gemini-4-hydrogen-low`……）与 3.8 Flash 共享配额且消耗更多：本 README 在中等推理力度下消耗 5 小时窗口的 0.95 点，而后者为 0.32 点。Claude 和 GPT-OSS 拥有独立的配额且小得多：实测每次调用约消耗 5 小时窗口的 1%，而 Flash 约为 0.05%。Gemini 4 Argon 有其专属的周配额：本 README 消耗其中的 1.35%。
- **配额**：按组划分 5 小时窗口和周窗口，按 Token 成本比例折算。在作者账户上的实测数据：在 `gemini-3.8-flash-medium` 下每百万源字符消耗 5 小时窗口约 16 点，`gemini-3.7-flash-medium` 下约 14 点，低推理力度下约 7 到 8 点——因此一份 40,000 字符的 README 消耗略高于半个点。周限制则取决于订阅层级。重试机制遵循 agy 声明的可重试状态；否则，耗尽的窗口绝不会自动重试：它会使每个文件失败，直到 `/usage` 显示重置。
- **比 API 更慢**：在评测的长篇密集文章上，每种语言的中位时间在 `gemini-3.8-flash-medium` 下为 3 分 59 秒，在 `gemini-3.7-flash-medium` 下为 3 分 14 秒，而 Gemini 3.7 Flash 通过 API 仅需 1 分 18 秒。
- **中断**：Ctrl-C 或关闭终端会连同命令一同停止 agy，而不会让它在后台继续消耗您的配额完成该轮；Codex、Grok CLI 和 OpenCode 亦同。在 `nohup` 下，翻译会继续进行。
- 在 CI 环境中被拒绝（设置了 `CI` 或 `GITHUB_ACTIONS`）：登录凭据保存在个人密钥环中。在 Runner 上，请结合 `GOOGLE_API_KEY` 使用 `--use_gemini`。
- 环境变量：`AGY_BIN`（否则使用 `PATH`，然后是 `~/.local/bin/agy`）、`AGY_TIMEOUT`（每分段秒数，含启动时间，默认 900）。

**服务条款：由此产生的一切风险由您的账户承担。** [Antigravity 服务条款](https://antigravity.google/terms)（第 6 条）及其 [常见问题解答](https://antigravity.google/docs/faq/) 禁止通过 Antigravity 登录凭证使用第三方软件访问该服务——其中明确提及了 Claude Code、OpenClaw 和 OpenCode——违者可能被暂停账户。aipmt 既不读取也不复用令牌：它只是在 Google 针对脚本和 CI 记录的 [无头模式（headless）](https://antigravity.google/docs/cli/headless/) 下运行官方二进制文件。Google 团队成员曾认为通过本地脚本为个人工作运行 `agy -p` 是“标准的”（[官方论坛，2026 年 9 月 25 日，非约束性回复](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）；但尚无明确条款定性此类分发工具的情况。

**仅限公开文档。** 根据相同条款的第 5 条，所有交互内容——提示词、回复、元数据——都可能用于改进 Google 的产品和机器学习，并可能由人工审查，即使是付费订阅亦如此。退出该机制需要通过未有官方文档说明效果的设置项 `enableTelemetry`，aipmt 并不会设置此项；且您的 agy 设置不会同步到隔离环境中。切勿在此传入任何机密内容。

### 使用 Claude 订阅：`--use_claude_code`

原理与 `claude`（Claude Code 的官方 CLI，处于 `-p` 模式）相同：对于支付 Claude Pro 或 Max 订阅费用的用户，翻译将从订阅额度中扣除，而不是按 Token 计费。请勿将其与 Anthropic 的 API `--use_claude` 混淆，后者是按量计费的。

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **不保留任何付费途径，且每次调用均可证明这一点。** Claude Code 仅从您的环境中接收一个受限的变量列表——既没有 API 密钥、Token，也没有云提供商信息，更没有发起 aipmt 的 Claude Code 会话标记。在第一个分段之前，`claude auth status` 必须显示订阅连接（不含 Console 密钥），并且无需消耗任何额度的 `/usage` 必须证明这一点；随后的每次调用也会在其初始化事件中依次进行证明，否则响应将被拒绝。
- **停用“额外用量”（extra usage）**（claude.ai，设置 → 用量），以确保实现零花费：启用后，它会在窗口耗尽时接管并计费，且不显示任何错误。aipmt 会在某次调用的额度报告显示耗尽时立即停止翻译，但该次调用已被计入。
- **与您的 Claude Code 会话共享配额。** 每次调用都会报告 5 小时窗口和每周窗口的使用情况；一旦超过 80%（`AIPMT_CLAUDE_MAX_UTILIZATION`），将不再发起新的分段，以免耗尽用于您日常工作的额度。
- **隔离沙箱。** 每次调用均在无工具、私有且一次性的目录中以无个性化模式运行：既不加载您的 `CLAUDE.md`，也不加载您的插件、钩子、MCP 服务器或设置，且会话不保留任何内容。附件已被切断：文档中的 `@chemin` 仅作为普通文本保留，不会打开任何文件（经实测）。
- **模型**：默认使用 `sonnet`，采用 `low` 思考力度，在 `--eco` 下也是如此：`--eco` 在此路径上没有任何影响。在相同文档上的实测表明，`haiku` 慢了两倍——它会在无法阻止的情况下进行推理——而成本几乎没有降低，且 `opus` 会拒绝生物学内容（见下一项）。两者均可通过 `--model` 访问；这些别名始终跟踪其家族的最新模型。`fable` 以及 `[1m]` 变体会被拒绝，因为它们会计入付费积分。`--reasoning_effort` 用于调整思考力度，而翻译完全无法从中获益：经测算其实际推理量几乎为零。
- **Opus 会拒绝某些生物学内容。** 它的安全防护措施比 Sonnet 更严格，Anthropic 的错误信息警告称其“can sometimes flag biology-research-adjacent work”（有时可能会标记与生物研究相关的工作）。实测显示：一篇关于 279 个生成分子的监测简报导致该文章在所有 14 种语言中均被拒绝。未写入任何内容：aipmt 会拒绝被截断的响应，指出触发了防护机制，并建议改用 `--model sonnet`。
- 在 CI 环境中（设置了 `CI` 或 `GITHUB_ACTIONS`）以及 Windows 下（未测试）会被拒绝。
- 变量：`AIPMT_CLAUDE_BIN`（否则使用 `PATH`，然后是 `~/.local/bin/claude`）、`AIPMT_CLAUDE_TIMEOUT`（每段秒数，默认 900）、`AIPMT_CLAUDE_MAX_UTILIZATION`（默认 0.8）、`CLAUDE_CONFIG_DIR`（Claude Code 的账户，绝不从项目的 `.env` 中获取）；工作目录位于 `XDG_CACHE_HOME/aipmt/claude-code` 下（默认 `~/.cache`）。

**使用条款：责任由您的账户承担。** [Claude Code 法律页面](https://code.claude.com/docs/en/legal-and-compliance)并不阻止“最终用户使用自己的 Claude 订阅登录未修改的 Claude Code 二进制文件”（an end user from signing in to the unmodified Claude Code binary with their own Claude subscription）：这正是 aipmt 的做法，它直接运行官方二进制文件，并且绝不读取 Token。但 Anthropic“不允许第三方开发者代其用户通过 Free、Pro 或 Max 计划凭据路由请求”（does not permit third-party developers […] to route requests through Free, Pro, or Max plan credentials on behalf of their users），更倾向于第三方工具（包括开源项目）使用 API 密钥，并保留将其使用计入付费积分的权利（[Claude 帮助中心](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)）。目前尚无明确条款定性分发直接调用该二进制文件的工具这一情况。

**数据**：对于 Free、Pro 和 Max 账户，当隐私设置允许时，模型训练同样适用于 Claude Code（[数据政策页面](https://code.claude.com/docs/en/data-usage)）。aipmt 不保留任何本地转录记录（`--no-session-persistence`）。请勿在此处理任何机密内容。

### 连接自选提供商：`--use_opencode`

[OpenCode](https://opencode.ai) 是一个开源（MIT）代码 Agent，可路由至其内部配置的提供商：API 密钥、订阅、OpenCode Zen 网关（免账户的免费模型）或本地模型。此处对 Zen 和 Ollama 两种途径进行了端到端实测。

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur

# gratuit, sans compte ni clé — données utilisables pour l'entraînement
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en
# local, hors ligne
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de
# sur un abonnement déjà payé
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

`--model` 为必填项：若不指定，OpenCode 将回退到免费模型，其交互内容可能会被用于训练，而此项选择不应代您决定。

每次调用的隔离机制：

- 内联配置优先于您的本地配置，定义了一个所有工具均被禁用的 Agent `aipmt`（`permission: { "*": "deny" }`），会话共享已禁用，`--pure`，绝不使用 `--auto`；
- 放置了 `OPENCODE_DISABLE_PROJECT_CONFIG` 与 `OPENCODE_DISABLE_CLAUDE_CODE` 的空一次性工作目录——若缺少它们，OpenCode 会将当前目录的 `AGENTS.md` 和 `~/.claude/CLAUDE.md` 注入提示词中。全局 `~/.config/opencode/AGENTS.md` 仍会被注入，OpenCode 无法将其排除；
- 输出契约：退出代码为 0、无 `error` 事件、无工具调用、最后一步为 `stop`、文本非空，且确实加载了 Agent `aipmt`——未知的 `--agent` 不会使 OpenCode 报错退出，而是会静默回退至代码编写 Agent；
- 除 OpenCode 本身的密钥 `OPENCODE_API_KEY` 外，不传递任何 `aipmt` 密钥。提供商在 OpenCode 内部配置，而非在 `aipmt` 的 `.env` 中配置。

注意事项：

- Zen 的免费模型经常变动，限制未公开记录，且其交互可能会用于训练：仅适用于公开文档，不适合私有内容。
- 本地模型必须提供至少 16k Token 的上下文，因为每个分段最多可达 16,000 个字符。Ollama 通常默认配置为 4,096：可通过带有 `PARAMETER num_ctx 32768` 的 `Modelfile` 进行调整。
- `--eco` 无效；`--reasoning_effort` 会按原样作为 OpenCode 的 `--variant` 传递。
- OpenCode 会将每次会话记录在 `~/.local/share/opencode/` 中。
- 变量：`OPENCODE_BIN`（否则使用 `PATH`，然后是 `~/.opencode/bin/opencode`）、`OPENCODE_TIMEOUT`（每段秒数，默认 600）。`OPENCODE_CONFIG` 原样传递给 OpenCode。

通过 Ollama 使用本地模型的示例，位于 `~/.config/opencode/opencode.json` 中：

```bash
ollama pull gpt-oss:20b
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": { "baseURL": "http://127.0.0.1:11434/v1" },
      "models": {
        "gpt-oss-20b-32k": {
          "name": "gpt-oss 20B (32k, sans réflexion)",
          "limit": { "context": 32768, "output": 8192 },
          "options": { "reasoningEffort": "none" }
        }
      }
    }
  }
}
```

`reasoningEffort: "none"` 可关闭 Ollama 在这些模型上默认启用的思考过程，而 Modelfile 无法将其禁用。在一段六个单词的短句上实测：未加该选项时包含 919 个思考 Token，耗时 68 秒；加上后仅消耗 9 个 Token。

### 连接 400 多个模型：`--use_openrouter`

OpenRouter 是一个按量计费的路由服务，基于统一积分池，代理第三方托管的各种模型——包括此处无其他 Provider 提供的中国开源模型。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` 为必填项。在产生任何费用前执行的预检（preflight）可处理该路由的两个特殊问题：

- **同一模型由数十家托管商提供，其上限各不相同**——在 `z-ai/glm-5.3-flash` 上有 23 家托管商，其中一家的输出上限仅为 2,048 Token。预检会读取 `/api/v1/models/{modèle}/endpoints`，排除输出低于 8,000 Token 或处于降级状态的托管商，并使用 `allow_fallbacks: false` 固定其余托管商。
- **推理按输出费率计费**——在 `z-ai/glm-5.2` 回复一个“OK”时，计费 Token 为 107 个，而普通回复仅需 2 个。推理默认关闭；强制要求推理的模型将被设定为其允许的最低思考力度，因为目录默认值可能会在翻译完成前耗尽输出限额。`--reasoning_effort` 仍然拥有优先权。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- 上下文窗口来源于目录。在发起任何调用之前，上下文低于 16,400 Token 的模型将被拒绝：提示词与分段需要 8,400 Token，输出至少需要 8,000 Token。
- 目录中不存在的 Slug、无法访问目录或没有符合上限要求的托管商，均会中止命令执行。
- 带有空输出的 `finish_reason=length` 表示预算被推理耗尽，而非内容截断：错误信息会对二者进行区分。
- `--eco` 无效。
- 变量：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>）、`OPENROUTER_BASE_URL`（默认 `https://openrouter.ai/api/v1`，必须提供 `https://`）、`OPENROUTER_TIMEOUT`（默认 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（默认 30）。

### 翻译说明

`--add_translation_note` 可添加一段说明，位置可选 `bottom`（默认）、`top`（位于 front matter 之后）或 `both`（`--note_position`），格式可选 `legacy`（加粗段落，默认）或 `marker`（`--note_format`）。`marker` 格式是一个隐式的 Markdown 引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），后接一段加粗引用：在 GitHub 上清晰可读，且在构建时可被 remark 插件解析利用。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 详细评测指标

所有评测数据均来自使用 `aipmt` 实际执行的翻译，目标为 14 种语言：en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi。
**已写入**统计了通过防护检查的文件数；**零偏差**统计了 `scripts/compare_structure.py` 未检出任何差异的文件数——即章节数、小标题数、链接数、独立 URL 数、代码块数、行内代码数、表格行数、引用块数和加粗词数完全一致。

“零偏差”表示“未检测到差异”，并不等同于“完全一致”：比对工具仅统计元素数量，不读取其内容。它不会标出被删除的 4 级标题、被替换的行内代码文本、被调换的国旗标识，也不会发现内部链接末尾多出的右括号（例如导致链接失效的 `[texte]((#ancre))`）——并且它不评估语言质量。

### 密集型资讯监测文章，`--news` 模式

来自 [jls42.org 的 AI 资讯监测](https://jls42.org/fr/news)的一期内容：589 行，140 个链接，21 个章节，3 处受保护的英文引用。测试时间为 2026 年 9 月 4 日至 5 日。

| 模型 | 接入方式 | 已写入 | 零偏差 | 中位数/语言 |
| --- | --- | --- | --- | --- |
| `gemini-3.7-flash` | Google API | 14/14 | ✅ **14/14** | 1 分 18 秒 |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google 订阅 | 14/14 | ✅ **14/14** | 3 分 59 秒 |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google 订阅 | 14/14 | ✅ **14/14** | 3 分 14 秒 |
| `claude-sonnet-5-5` | Anthropic API | 14/14 | ✅ **14/14** | 3 分 37 秒 |
| `gpt-5.6-sol` (`--use_codex`) | ChatGPT 订阅 | 14/14 | ✅ **14/14** | 11 分 28 秒 |
| `z-ai/glm-5.2` | OpenRouter | 14/14 | ✅ **14/14** | 5 分 37 秒 |
| `qwen/qwen3.8-flash` | OpenRouter | 14/14 | ✅ **14/14** | 26 分 23 秒 |
| `sonnet` (`--use_claude_code`) | Claude 订阅 | 14/14 | ⚠️ 13/14 | 6 分 49 秒 |
| `claude-sonnet-5` | Anthropic API | 14/14 | ⚠️ 11/14 | 6 分 31 秒 |
| `haiku` (`--use_claude_code`) | Claude 订阅 | 14/14 | ⚠️ 11/14 | 15 分 54 秒 |
| `claude-haiku-5-5` | Anthropic API | 14/14 | ⚠️ 11/14 | 2 分 54 秒 |
| `claude-haiku-4-5` | Anthropic API | 14/14 | ⚠️ 7/14 | 6 分 00 秒 |
| `opencode/mimo-v2.5-free` | OpenCode Zen | 13/14 | ❌ 11/14 | 9 分 27 秒 |
| `qwen/qwen3.7-flash` | OpenRouter | 13/14 | ❌ 8/14 | 10 分 09 秒 |
| `ollama/gpt-oss-20b-32k` | 本地运行 | 10/14 | ❌ 7/14 | 12 分 39 秒 |
| `mistral-large-latest` | Mistral API | 11/14 | ❌ 5/14 | 5 分 32 秒 |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter | 4/14 | ❌ 3/14 | 37 分 27 秒 |
| `grok-4.6` (`--use_grok_cli`) | Grok 订阅 | 1/14 | ❌ 1/14 | 23 分 11 秒 |
| `opus` (`--use_claude_code`) | Claude 订阅 | 0/14 | ❌ 0/14 | — |

Grok 于 9 月 9 日在同系列监测的另一期文章（356 行）上重新进行了测试：14 种语言中写入 9 种，8 种零偏差。主表中展示的即为此数据。三组中断的测试未计入在内：`qwen3.5-27b`（9 种语言）和 `kimi-k2.6`（4 种语言）因额度耗尽而中断，`z-ai/glm-5.3-flash` 的两次失败则是由于推理设置导致，该问题随后已由 Provider 修复。OpenRouter 各行数据是在路由默认设置下测得的，早于 `--use_openrouter`；使用交付的 Provider 重新测试的 `z-ai/glm-5.2` 同样取得了 14/14 的成绩。数据于 9 月 10 日使用当前的比对工具重新计算：与首次发布相比，`qwen3.8-flash` 和 `qwen3.7-flash` 各增加了一种完全匹配的语言，其他保持不变。

`--use_antigravity` 相关行于 9 月 26 日在同一文章上测得，采用了四路并发翻译：上午测试 `gemini-3.7-flash-medium`，下午测试 `gemini-3.8-flash-medium`。在英语翻译中，两者均自行删除了引用下方的三行法语译文，没有凭空生成国旗符号，且英文引用完好无损：无需后备清理介入。在 `--eco`（`gemini-3.7-flash-low`）上，仅在四种语言（en、ja、ar、hi）中进行测试：4 种全部成功写入，且均为零偏差，中位时间为 1 分 52 秒。同日针对该监测专栏更新的一期（9 月 25 日，438 行，2 处英文引用）进行了复测，在博客之外使用 `gemini-3.7-flash-medium` 翻译：14 种语言全部成功写入且均为零偏差，每种语言耗时 87 至 128 秒。

`--use_claude_code` 相关行于 9 月 26 日在同一文章上以 `low` 思考力度、四路并发测试测得。使用 `sonnet` 时，十四种语言中的英文引用均完好无损，且在英语版本中，模型自行去除了法语译文行，未编造国旗。`opus` 未成功写入任何语言：在每种语言中，其安全防护机制都在最后一个分段中断了响应，原因是一篇涉及针对结合位点生成 279 个分子的简报。单独发送该简报时，会被归入“生物”类别而拒绝；`sonnet` 则在所有语言中顺利完成了翻译。`haiku` 成功写入了十四种语言；但在其中三种语言（en、pl、ro）中，有一个章节标题从 2 级变成了 1 级。它会在无法阻止的情况下进行推理——占其输出 Token 的 61%——导致其耗时达到 `sonnet` 的两倍以上。

`claude-sonnet-5-5`、`claude-haiku-5-5` 和 `claude-haiku-4-5` 诸行于 10 月 18 日通过 Anthropic API 在同一文章上测得，每个模型采用四路并发翻译。Sonnet 5.5 不允许关闭思考功能：aipmt 向其发送了它所能接受的最低设置，其响应中完全不包含思考内容。它在没有重新处理任何分段的情况下实现了十四种语言零偏差写入；在英语版本中，它自行去除了法语译文行且未虚构国旗，英文引用在所有版本中均完好无损。Haiku 5.5 在启用自适应思考模式下进行了测试：关闭思考后，它留下了整段的法语未翻译，被防护机制拦截——14 种语言中仅写入了 3 种。两个 Haiku 模型都在同一篇简报上出现异常：Haiku 5.5 在日语、韩语和中文中修改了其标题级别或出现重复，Haiku 4.5 在七种语言中将其升至 1 级标题，并在日语中将其保留为法语。在十四种语言中翻译这两篇文档，Haiku 4.5 耗资 3.67 美元，Haiku 5.5 耗资 0.57 美元，Sonnet 5.5 耗资 9.21 美元。

### 本项目的 README，标准 Markdown

2026 年 9 月 9 日冻结版本：785 行，285 处行内代码，40 处代码块闭合，89 行表格。4 路并行翻译。

| 模型 | 已写入 | 无偏差 | 中位数/语言 | 差异之处 |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 分 43 秒 | 无 |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 分 48 秒 | 无 |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 分 02 秒 | 比较器无异常；内部链接重复 (en) |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 分 18 秒 | 无 |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 分 06 秒 | 无 |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 秒 | 一个词加粗 (ja) |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 分 22 秒 | 一个词加粗 (ko) |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 分 20 秒 | 一行表格与上一行相连 (ar) |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 分 56 秒 | 一个链接 (sv)，一个词加粗 (zh) |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 分 46 秒 | 一个词加粗 (ar, ja) |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 分 34 秒 | 一个词加粗 (hi, ja, ko) |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 分 17 秒 | 阿拉伯语中增加了 40 处行内代码；加粗 (hi, ja, ko) |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 分 14 秒 | 2 种语言被拒绝 (ar, hi)：返回时丢失行内代码 |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 分 44 秒 | 丢失一个章节 (ar, hi, ko)；增加了代码块 (ja, ko, ro, zh) |

两次中断的评测未记入成绩：Grok，CLI 会话在 12 种语言后超时（11 种无偏差）；以及 `qwen3.8-flash`，在两种语言后其托管商返回 HTTP 429。`opencode/mimo-v2.5-free` 和 `ollama/gpt-oss-20b-32k` 未在此版本上重新评测；在 9 月 4 日和 5 日的版本（少 277 行）中，它们各自在 14 种语言中写入了 9 篇翻译，其中分别有 7 篇和 1 篇无偏差。

`--use_antigravity` 和 `--use_claude_code` 行未在冻结版本上测量，而是在 9 月 26 日随 1.14.0 发布的版本上测得——且 `claude-sonnet-5-5`、`claude-haiku-5-5` 和 `claude-haiku-4-5` 行于 10 月 18 日在同一版本上测得：600 行，257 处行内代码，30 处代码块闭合，85 行表格。该版本少了 185 行，不能与其他行进行逐项比较；但这些行之间可以相互比较。对于比较器不进行检查的内部链接，`gemini-3.8-flash-medium` 在全部 14 种语言中保持完好，`gemini-3.7-flash-medium` 在意大利语中损坏；`sonnet` 和 `opus` 在所有语言中保持完好，`haiku` 在英语中重复；`claude-sonnet-5-5` 和 `claude-haiku-4-5` 在全部 14 种语言中保持完好，`claude-haiku-5-5` 在其写入的 12 种语言中保持完好。

### 知名项目的四个 README

FastAPI、Ollama、tldr-pages 和 Vue.js，直接取自 GitHub——比前两个文档更简单。该测试轮次针对表现吃力的模型；Gemini 在此作为比较基准。

| 模型 | 范围 | 已写入 | 无偏差 |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 个项目 × 14 种语言 | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 个项目 × 14 种语言 | 55/56   | ❌ 47/56     |
| `grok-4.6` (订阅) | 4 个项目 × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 个项目 × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### 这些测试不是什么

- **并非详尽的排行榜**：仅 OpenRouter 就提供了四百多个模型，此处仅测试了约十五个。
- **仅供参考的时间**：根据测试批次不同，采用 3 到 6 路并行翻译，且服务商的吞吐量在一天中会有所波动。
- **带有时效性的观察**：同名模型会发生变化，且您的文档与我们的不同。

若要在您自己的文档上重新进行测试（使用该文件的冻结副本）：

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## 贡献

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

两行都是必需的：没有 `pip install -e .`，`python -m aipmt` 会响应 `No module named aipmt`。

质量工具，可选但推荐：

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

仓库的 28 个翻译（README 和 CHANGELOG，14 种语言）可通过 `./regen_translations.sh --force` 重新生成——默认使用 ChatGPT 订阅下的 Codex 和 `gpt-6.1-sol`，4 路并行。`REGEN_PROVIDER` 和 `REGEN_MODEL` 会改变路径：`antigravity` 仍保留在订阅上（Google 订阅），且无需特许即可通过；按量计费的 API（`openai`、`gemini`、`grok`、`openrouter`）在没有 `REGEN_ALLOW_PAID_API=1` 的情况下会被拒绝；`REGEN_JOB_TIMEOUT` 会限制每个作业的最大时长（600 秒，Codex 和 Antigravity 为 1800 秒）。工具的详细信息见 `CLAUDE.md`。

## 使用此脚本的项目

- **[jls42.org](https://jls42.org)** —— 发布为 15 种语言的个人博客。其[每日 AI 资讯跟踪](https://jls42.org/fr/news)每天由该工具翻译，并作为上述测试的基准文档。

## 作者

Julien LE SAUX
电子邮箱：contact@jls42.org

## 许可证

GNU GENERAL PUBLIC LICENSE Version 3。请参见 [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)。

## 免责声明

本程序根据 GPL v3 第 15 条和第 16 条的条款**不提供任何保证**：按“原样”提供，不包含适销性或特定用途适用性的默示保证，且其作者对因使用本程序而造成的任何损害概不负责。许可证全文优先于本摘要。

- **发布前请仔细校对。** 保护机制覆盖了代码块、行内代码、URL、锚点以及 `--news` 模式下的引用——但不涵盖标题、表格、front matter，也不涵盖您句子的含义。
- **您的文档将被发送至所选的服务商**，并遵循其使用条款和数据政策。某些免费模型可能会将您的交流内容重用于模型训练，而 Antigravity 的条款允许 Google 重用并在人工审查下查阅这些内容（包括付费订阅在内）；本地模型是确保任何数据都不离开您机器的唯一途径。
- **API 调用会产生费用。** 本程序不限制支出：长篇文档、失败重试或深度思考推理的模型都会消耗更多费用。
- **已发布的测试数据仅为带有时效性的观察记录**，而非保证。

文中所提及的产品和公司名称归其各自所有者所有。本项目与其中任何一方均无附属关系。

**使用 gemini-3.8-flash-medium 从法语翻译为中文的文章。**
