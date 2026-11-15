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

在保持结构完整的前提下将 Markdown 文件从一种语言翻译为另一种语言：支持保留代码块、行内代码、URL、锚点、表格和 front matter。提供 11 种模型调用途径——5 个 API、4 种免按量计费的订阅服务、2 个路由器——并公开发布了每个模型实际结构保留能力的实测数据。

## 概览

- **11 种 Provider 路径**：OpenAI、Mistral、Claude、Gemini 和 Grok API；免按量计费的 ChatGPT (Codex)、Grok、Google (Antigravity) 和 Claude (Claude Code) 订阅；OpenCode（开源、免费或本地）和 OpenRouter（400 多个模型）路由器。
- **杜绝因 Token 丢失导致的格式损坏**：代码块、行内代码、URL、锚点和引用在调用前均会被替换为 Token，并在返回后进行验证。若缺失任何一个，都不会写入文件。
- **长篇文档**：根据模型的上下文窗口自动切分。
- **`--news` 模式**：保护英文引用并按语言管理国旗图标，专为技术资讯文章设计。
- **`--eco` 模式**：采用更快且成本更低的模型。
- **可选翻译附注**：可置于顶部、底部或同时置于两端。

## 安装

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

需要 Python 3.11 或更高版本。若要从仓库安装，请参阅[贡献](#贡献)。

## 配置

密钥按以下三个位置读取，优先级从高到低；后一位置仅填充前一位置未配置的项。

|     | 位置                                          | 用途                                  |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 环境变量                                      | CI、容器、临时覆盖                    |
| 2   | 当前目录（或父目录）的 `.env`          | 项目专用密钥                          |
| 3   | `~/.config/aipmt/.env`                                 | 一次安装，全局通用                    |

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

可使用 `GEMINI_API_KEY` 代替 `GOOGLE_API_KEY`。用户配置文件遵循 `XDG_CONFIG_HOME`（仅限绝对路径），在 Windows 下遵循 `%APPDATA%`。若未配置密钥，该命令会列出这三个位置。

**项目的 `.env` 既不能重定向调用，也不能指定执行的程序。** 它仅提供密钥，绝不提供目标地址或可执行文件：任何以 `_BASE_URL`、`_API_BASE`、`_ENDPOINT` 或 `_BIN`（`CODEX_BIN`、`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`）、`GROK_HOME` 命名的变量、代理（`HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY`）、证书库（`SSL_CERT_FILE`、`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）以及 `XDG_CONFIG_HOME` / `APPDATA` 均会被忽略并发出警告。克隆的仓库不应在初次翻译时窃取您的密钥，也不应诱使您运行其自身包含的程序。该文件读取时也不进行变量插值：`NOM=${OPENAI_API_KEY}` 不会在其中复制密钥。请将这些变量设置在环境中或置于 `~/.config/aipmt/.env` 中。

可选变量：`XAI_BASE_URL`（默认 `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（每次调用的超时秒数，默认 900）、`CODEX_BIN`、`CODEX_TIMEOUT`（默认 600）、`GROK_BIN`、`GROK_HOME`（默认 `~/.grok`）、`GROK_TIMEOUT`（默认 900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（默认 900）、`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（默认 600）、`OPENROUTER_BASE_URL`（必须指定 `https://`）、`OPENROUTER_TIMEOUT`（默认 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（默认 30）。各变量的详细说明请见对应 Provider 的章节。

## 快速入门

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

将 `document.md` 翻译为西班牙语会在 `--target_dir` 中生成 `document-es.md`；使用 `--include_model` 则生成 `document-es-gpt-6.1-terra.md`。扩展名始终变为 `.md`（例如 `article.mdx` 会生成 `article-en.md`），除非使用 `--keep_filename` 保留原文件名。如果未指定 `--force`，已存在的翻译将被跳过。

退出代码：全部成功或已跳过返回 `0`，若存在失败文件则返回 `1`（在标准错误输出中列出），若配置有误则返回 `2`。失败的文件绝不会被写入，即使写入过程本身出错也是如此：内容先写入临时文件然后再重命名。只需重新运行即可。

## 模型选择

基于两篇真实文档，由各个模型分别翻译为相同的 14 种语言进行评测。**数值表示在 14 种语言中，成功写入翻译且与源文档格式完全一致的语言数量。**

| 模型                  | 访问方式                          | 密集资讯文章            | 本 README    | 差异详情及涉及语言数量                                                                                                              |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.8 Flash**  | Google 订阅 (Antigravity)         | ✅ 14/14                | ✅ 14/14     | 两篇文档均无任何差异                                                                                                                |
| **Claude Sonnet 5.5** | Anthropic API 密钥                | ✅ 14/14                | ✅ 14/14     | 两篇文档均无任何差异                                                                                                                |
| **Gemini 3.7 Flash**  | Google API 密钥                   | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种出现差异：多了一个加粗词 (ja)                                                                                     |
| **Gemini 3.7 Flash**  | Google 订阅 (Antigravity)         | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种出现差异：少了一个加粗词 (ko)                                                                                     |
| **GPT-5.6 Sol**       | ChatGPT 订阅，或 OpenAI 密钥      | ✅ 14/14                | ⚠️ 12/14     | 14 种语言中有 2 种出现差异：少了一个加粗词 (ar, ja)                                                                                 |
| **GLM-5.2**           | OpenRouter 密钥                   | ✅ 14/14                | ⚠️ 11/14     | 14 种语言中有 3 种出现差异：少了一个加粗词 (hi, ja, ko)                                                                              |
| Claude Sonnet 5       | Claude 订阅 (Claude Code)         | ⚠️ 13/14                | ⚠️ 13/14     | 资讯文章 14 种中有 1 种出现差异：多了一个加粗词 (zh)；本 README 出现 1 种：表格行与上一行合并粘连导致显示异常 (ar)                   |
| Claude Haiku 4.5      | Claude 订阅 (Claude Code)         | ⚠️ 11/14                | ✅ 14/14     | 资讯文章 14 种中有 3 种出现差异：章节标题变成了 1 级标题 (en, pl, ro)；本 README 对比工具未报错，但内部链接在英文中重复             |
| Claude Sonnet 5       | Anthropic API 密钥                | ⚠️ 11/14                | ⚠️ 12/14     | 资讯文章 14 种中有 3 种出现差异：凭空出现代码块 (es, de, hi)；本 README 出现 2 种：链接丢失标记 (sv)、一个加粗词 (zh)               |
| Claude Haiku 4.5      | Anthropic API 密钥                | ⚠️ 7/14                 | ✅ 14/14     | 资讯文章 14 种中有 7 种出现差异：章节标题变成了 1 级标题——日文中仍保留法语；本 README 无差异                                        |
| Claude Haiku 5.5      | Anthropic API 密钥                | ⚠️ 11/14                | ❌ 12/14     | 资讯文章 14 种中有 3 种出现差异：章节标题层级变更或重复 (ja, ko, zh)；本 README 有 2 种语言被拒，行内代码丢失 (ar, hi)               |
| Qwen 3.7 Flash        | OpenRouter 密钥                   | ❌ 8/14                 | ⚠️ 10/14     | 资讯文章有 1 种语言被拒，另有 5 种出现偏差；本 README 中约有 40 个词被格式化为 `code` (ar)                                  |
| Grok 4.6              | Grok 订阅                         | ❌ 8/14                 | 未评测       | 14 种语言中有 5 种被拒（因行内代码和 URL 未正确返回）；荷兰语版本完全偏离                                                           |
| GPT-OSS 20B           | 本地模型 (Ollama)                 | ❌ 7/14                 | 未重新评测   | 14 种语言中有 4 种被拒：模型在其中残留了法语段落，被保护机制拦截                                                                    |
| MiMo v2.5 (免费版)    | OpenCode Zen，免登录              | ❌ 11/14                | 未重新评测   | 1 种语言被拒；波兰语版本丢失一个章节                                                                                                |
| Mistral Large         | Mistral API 密钥                  | ❌ 5/14                 | ❌ 1/14      | **丢失整个章节**：资讯文章有 1 种语言受影响 (hi)，本 README 有 3 种 (ar, hi, ko)——且资讯文章有 3 种语言被拒                          |
| DeepSeek V4 Flash     | OpenRouter 密钥                   | ❌ 3/14                 | 未重新评测   | 14 种语言中有 10 种被拒；每种语言耗时 37 分钟                                                                                       |
| Claude Opus 5.5       | Claude 订阅 (Claude Code)         | ❌ 0/14                 | ✅ 14/14     | 资讯文章由于一篇生物学简讯触发 Opus 安全护栏，导致全部 14 种语言被拒；本 README 无差异                                              |

|     | 符号含义                                                                                                                                                              |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14 种语言均成功翻译，且与源文档相比毫无差异                                                                                                                          |
| ⚠️  | 14 种语言均成功翻译；差异仅限于**标记样式**——多出一个加粗词、一个 `code`、或是链接丢失中括号等。文本内容、URL、代码块和章节均无缺失                          |
| ❌  | 至少有一种语言无法完成翻译——文件被拒绝写入，**或者**已写入的文件中存在内容缺失                                                                                       |

核心结论：

- **被拒绝翻译并不等于损坏的翻译。** 当返回内容缺少 Token 时，文件不会被写入，该语言会被计为被拒。这正是 Grok 在资讯文章上发生的情况：在 5 种非拉丁脚本语言中，第一段就丢失了 4 个行内代码和 3 个 URL。
- **模型可能因一句话而拒绝整个文档。** Opus 5.5 在翻译本 README 时毫无偏差，但无法翻译技术资讯文章：其安全护栏在一篇生物学简报处截断了响应。文件未被写入，且 aipmt 给出了原因。
- **此保护网不覆盖标题、表格、front matter 或正文文本。** 如果模型删除了某一章节，工具依然会照常写入生成的文件——Mistral 即是如此。这些元素无法替换为 Token，目前的保护机制不会检查它们；`scripts/compare_structure.py` 可以检测到章节丢失，但属于事后检测。
- **Grok 在本 README 上没有评分**：其 CLI 会话在翻译完成 12 种语言后超时（其中 11 种无偏差）。中断的测试不予计分。
- **文档的密集程度比目标语言更关键。** Grok 可以应对常规的 README，但在包含大量链接的文章中就会出错，即便荷兰语也是如此。

测试日期与文档说明：“本 README”列测试于 2026 年 9 月 9 日，基于本文件的固定版本（785 行，285 个行内代码，89 行表格），此后该版本有所更新——Antigravity 和 Claude Code 行除外，这两项于 9 月 26 日基于随 1.14.0 发布的较短版本进行了测试（600 行，257 个行内代码，85 行表格），以及通过 API 调用的 Claude Sonnet 5.5、Haiku 5.5 和 Haiku 4.5 行，于 10 月 18 日在同一版本上完成测试。“密集资讯文章”列源自 9 月 4 日至 5 日对一篇 589 行文章的测试，例外情况包括：Grok 行于 9 月 9 日在另一期同类资讯上重新测试；Antigravity 和 Claude Code 行于 9 月 26 日在同一文章上测试；上述三款 Claude 模型于 10 月 18 日测试。完整的表格、耗时和测试规范请参见[详细评估数据](#详细测试数据)。

## 所有选项

| 选项                     | 说明                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 要翻译的单个 Markdown 文件（`--source_dir` 的替代项）                                                         |
| `--source_dir`           | 包含 Markdown 文件的源目录（默认：`content/posts`）                                                            |
| `--target_dir`           | 翻译后文件的输出目录（默认：`traductions_en`）                                                                  |
| `--source_lang`          | 源语言（默认：`fr`）                                                                                |
| `--target_lang`          | 目标语言（默认：`en`）                                                                              |
| `--model`                | 要使用的特定模型                                                                                              |
| `--eco`                  | 使用经济型模型                                                                                                |
| `--use_mistral`          | 使用 Mistral AI API                                                                                           |
| `--use_claude`           | 使用 Claude API                                                                                               |
| `--use_gemini`           | 使用 Gemini API                                                                                               |
| `--use_grok`             | 使用 xAI (Grok) API — 需要 `XAI_API_KEY`                                                                     |
| `--use_codex`            | 使用 Codex CLI 消耗 ChatGPT 订阅配额                                                                          |
| `--use_grok_cli`         | 使用 Grok CLI 消耗 Grok 订阅配额                                                                              |
| `--use_antigravity`      | 使用 Antigravity CLI（`agy`）消耗 Google AI Pro 或 Ultra 订阅配额                                    |
| `--use_claude_code`      | 使用 Claude Code CLI（`claude -p`）消耗 Claude Pro 或 Max 订阅配额                                         |
| `--use_opencode`         | 使用 OpenCode（开源）连接其配置的提供商；需要 `--model provider/modèle`                                                  |
| `--use_openrouter`       | 使用 OpenRouter — 需要 `OPENROUTER_API_KEY` 与 `--model fournisseur/modèle`                                                       |
| `--force`                | 强制重新翻译                                                                                                  |
| `--keep_filename`        | 保留原始文件名                                                                                                |
| `--news`                 | 新闻模式：保护英文引用，按语言处理国旗                                                                        |
| `--add_translation_note` | 添加翻译说明                                                                                                  |
| `--note_position`        | 说明位置：`top`、`bottom`（默认）或 `both`                                            |
| `--note_format`          | 说明格式：`legacy`（默认，加粗段落）或 `marker`                                               |
| `--include_model`        | 在输出文件中包含模型名称                                                                                      |
| `--reasoning_effort`     | GPT-5.x 推理力度：`none`/`low`/`medium`/`high`/`xhigh`             |

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

`--eco` 可切换至各提供商的经济档次。

| 提供商      | 质量（默认）                                                         | 经济（`--eco`）   |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-6.1-terra`                                                      | `gpt-6-luna`           |
| Claude      | `claude-sonnet-5-5`                                                      | `claude-haiku-5-5`           |
| Mistral     | `mistral-large-latest`                                                      | `mistral-small-latest`           |
| Gemini      | `gemini-4-hydrogen`                                                      | `gemini-3.1-flash-lite`           |
| Codex       | `gpt-6.1-sol`（亦可通过 `--model` 使用 `gpt-5.6-sol`、`terra` 和 `luna`） | `gpt-5.6-luna`           |
| Grok API    | `grok-4.7`                                                      | `grok-4.3`           |
| Grok CLI    | `grok-4.7`                                                      | 同左 — `--eco` 无效 |
| Antigravity | `gemini-3.8-flash-medium`                                                      | `gemini-3.8-flash-low`           |
| Claude Code | `sonnet`，力度 `low`                                | 同左 — `--eco` 无效 |
| OpenCode    | 必须指定 `--model provider/modèle`                                             | 同左 — `--eco` 无效 |
| OpenRouter  | 必须指定 `--model fournisseur/modèle`                                             | 同左 — `--eco` 无效 |

默认设置紧跟各提供商在采用前经过测量的最新一代模型：OpenAI 为 GPT-6，Google 为 Gemini 4 Hydrogen，xAI 自 1.19.0 起为 Grok 4.7。先前的模型仍可通过 `--model` 接受（`gpt-5.6-terra`、`gemini-3.8-flash`、`grok-4.6`……），Google 的高端模型 Gemini 4 Argon 和 Carbon 亦同。aipmt 会自行调节 GPT 与 Grok 的推理力度，并在 `--eco` 中关闭，而 `--reasoning_effort` 可强制指定；Gemini 始终接收其支持的最低级别。
Gemini API 的暂时性故障（503、429、超时）会在 10 秒、20 秒和 40 秒后最多重试三次。未收到响应的尝试会在 5 分钟后放弃，然后同样重试：服务器无响应最多在约二十分钟内使该片段失败，而不会无限期阻塞。

### 使用 ChatGPT 订阅：`--use_codex`

调用官方 Codex CLI：翻译从 ChatGPT 订阅配额中扣除，无需 API 密钥或按用量计费。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 二进制文件优先在 `CODEX_BIN` 中查找，其次是 `PATH`，然后是 `openai-codex-cli-bin` 软件包。从不读取 `~/.codex/auth.json`。
- `OPENAI_API_KEY` 和 `CODEX_API_KEY` 会从子进程的环境中移除：即使存在密钥，也绝不会切换到 API。
- 每个片段至少消耗 5 小时窗口中的一条“消息”——若验证失败并重试则消耗两条。OpenAI 预估，Plus 计划下 `gpt-5.6-luna`（`--eco`）每 5 小时约为 250–2,000 条消息，`gpt-5.6-sol` 为 10–100 条。
- 1.16.3 之前的默认项 `--model gpt-5.6-sol`、`--model gpt-5.6-terra` 以及 `--model gpt-5.6-luna` 同样走订阅途径。
- 服务器返回 429 不会导致文件丢失：Codex 会自动重连，aipmt 会等待该轮结束，如果 429 最终仍未恢复，片段会在 30 秒后重试，继而在 60 秒后重试。账户无权使用的模型会返回 400 “model is not supported when using Codex with a ChatGPT account”。
- 比 API 更慢，且差距随文档变大而增加：在本 README 上，使用 `gpt-5.6-sol` 时每种语言的中位数耗时为 6 分 46 秒，而 `gemini-3.7-flash` 仅需 36 秒。
- 在 CI 中被拒绝（定义了 `CI` 或 `GITHUB_ACTIONS`）：订阅通过个人会话文件进行身份验证，绝不应放在共享 runner 上。
- 变量：`CODEX_BIN`、`CODEX_TIMEOUT`（每个片段的秒数，默认 600）。

### 使用 Grok 订阅：`--use_grok_cli`

原理相同，通过官方 Grok Build CLI 使用 SuperGrok 或 X Premium+ 订阅。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **隔离性弱于 Codex。** Grok 的操作系统沙箱在许多较新的 Linux 主机上无法生效（AppArmor、容器运行时套接字），无法生效的配置会在无提示的情况下以未隔离状态启动。因此，脚本默认不请求任何配置，对此给出提示，并依赖 CLI 的 `--deny` 规则，其中包括兜底规则 `*` ——这是唯一宁可拒绝启动也不在未告知情况下移除保护的层级。`GROK_TRANSLATE_SANDBOX=read-only` 要求使用操作系统沙箱，若机器无法满足则启动失败。
- 配额为每周额度，与 Chat、Imagine 和 Voice 共享，且没有任何命令可读取该配额：批量运行可能会在没有任何提示的情况下消耗对话用量。
- 变量：`GROK_BIN`、`GROK_HOME`（CLI 目录，默认 `~/.grok`）、`GROK_TIMEOUT`（默认 900）、`GROK_TRANSLATE_SANDBOX`。

### 使用 Google 订阅：`--use_antigravity`

原理相同，采用 Antigravity 的官方 CLI `agy`：对于购买了 Google AI Pro 或 Ultra 的用户，翻译从订阅配额中扣除，而非按 token 计费。这是使用此配额的唯一途径：Gemini CLI 自 2026 年 6 月 18 日起不再服务这些账户（[公告](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)），而 Antigravity 的 SDK 仅接受 API 密钥或 Google Cloud 项目。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **未保留任何付费通道。** agy 从您的环境中仅接收封闭的变量列表 — `PATH`、语言和时区、终端、身份、代理和证书、会话总线 — 且不含任何密钥：其多个变量会在没有任何显示的情况下切换调用（经测量：一个变量将文档发送到第三方网关，另一个发送到计费的 Google Cloud 项目），并且黑名单在每次审查时都会有所遗漏。在处理任何片段之前，不消耗任何配额的 `agy -p /config` 必须显示付费 AI 额度已禁用，且无 API 密钥或 Google Cloud 项目 — 缺少设置即视为拒绝 — 否则不进行任何翻译；随后每次调用的日志必须证实使用的是订阅（`authMethod=consumer`），否则响应将被拒绝。
- **隔离。** 每次调用都在一个私有的、一次性的个人目录中运行，并配合无工具的翻译代理：您的 agy 设置、规则、插件、MCP 服务器和钩子均不会进入其中，任何内容都不会添加到历史记录中，且连接保持在密钥环中，aipmt 绝不读取该密钥环。若找不到代理，agy 会静默回退到其编码代理和工具：日志中必须有一整行确认使用了正确的代理 — 引用此消息的文档不能替代该行 — 否则拒绝。
- **平台**：Linux，需在拥有密钥环的会话中（D-Bus 会话总线、Secret Service）；支持 macOS，但未经测量。在 Windows 下被拒绝，因为 agy 在该系统下不读取隔离每次调用的变量；在没有会话总线的 Linux 下（SSH 会话、容器、服务器）亦被拒绝：agy 会将其令牌存储在 `~/.gemini` 文件中，而隔离会遮蔽该文件。拒绝会在任何启动之前连同原因一起给出，无需等待连接代码一分钟。
- **模型**：`agy models` 中的模型。Gemini 的推理力度体现在其名称中（`gemini-3.8-flash-medium`……）：不带后缀的名称在调用前会被拒绝，且 `--reasoning_effort` 无效。自 agy 不再提供 Gemini 3.7 Flash 以来，默认为 `gemini-3.8-flash-medium`，在 `--eco` 中为 `gemini-3.8-flash-low`；确定默认值的测试活动已在[详细测量](#详细测试数据)中说明。Gemini 4 Hydrogen（`gemini-4-hydrogen-low`……）与 3.8 Flash 共享配额且消耗更多：在本 README 处于中等力度时消耗 5 小时窗口的 0.95 点，而后者为 0.32 点。Claude 和 GPT-OSS 拥有自己单独的、小得多的配额：测得每次调用约占 5 小时窗口的 1%，而 Flash 约为 0.05%。Gemini 4 Argon 拥有自己的每周配额：本 README 消耗其中的 1.35%。
- **配额**：按组划分，包括一个 5 小时窗口和一个每周窗口，按 token 成本比例计算。在作者账户上的测量结果：在 `gemini-3.8-flash-medium` 下每百万源字符约消耗 5 小时窗口的 16 点，`gemini-3.7-flash-medium` 下为 14 点，低力度下为 7 到 8 点 — 因此一篇 40,000 字符的 README 消耗略高于半点。每周上限则取决于订阅档次。重试遵循 agy 声明为可重试的情况；否则，耗尽的窗口绝不会重试：它会使每个文件失败，直到 `/usage` 显示重置。
- **比 API 更慢**：在密集的测试文章上，`gemini-3.8-flash-medium` 下每种语言的中位数耗时为 3 分 59 秒，`gemini-3.7-flash-medium` 下为 3 分 14 秒，而通过 API 使用 Gemini 3.7 Flash 仅需 1 分 18 秒。
- **中断**：Ctrl-C 或关闭终端会连同命令一起停止 agy，而不是让其继续在您的配额上完成该轮；Codex、Grok CLI 和 OpenCode 亦是如此。在 `nohup` 下，翻译会继续。
- 在 CI 中被拒绝（定义了 `CI` 或 `GITHUB_ACTIONS`）：连接保存在个人密钥环中。在 runner 上，请使用 `--use_gemini` 配合 `GOOGLE_API_KEY`。
- 变量：`AGY_BIN`（否则使用 `PATH`，然后是 `~/.local/bin/agy`）、`AGY_TIMEOUT`（每个片段的秒数，包括启动时间，默认 900）。

**使用条款：涉及您的个人账户。** [Antigravity 条款](https://antigravity.google/terms)（第 6 条）及其 [FAQ](https://antigravity.google/docs/faq/) 禁止使用 Antigravity 连接通过第三方软件访问该服务 — 其中列举了 Claude Code、OpenClaw 和 OpenCode — 违者可能导致账户被封禁。aipmt 既不读取也不复用令牌：它在 Google 为脚本和 CI 记录的[无头模式](https://antigravity.google/docs/cli/headless/)下启动官方二进制文件。一位 Google 成员曾认为从本地脚本启动 `agy -p` 处理个人工作是“标准的”（[官方论坛，2026 年 9 月 25 日，非合同性答复](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）；但没有任何文本对像本项目这样的分发工具做出明确裁决。

**仅限公开文档。** 根据相同条款的第 5 条，交互内容 — 提示词、响应、元数据 — 可用于改进 Google 的产品和机器学习，并可能由人工复核，付费订阅亦包含在内。退出需通过设置 `enableTelemetry`，其效果未有文档说明，且 aipmt 不会设置该项；您的 agy 设置不会随其隔离环境传递。请勿在此处理任何机密内容。

### 基于 Claude 订阅：`--use_claude_code`

通过 `claude`（Claude Code 的官方 CLI）在 `-p` 模式下也是同样的原理：对于 Claude Pro 或 Max 付费用户，翻译将从订阅配额中扣除，而不是按 token 计费。请勿与 `--use_claude`（Anthropic 的 API，按用量计费）混淆。

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **不留任何付费通道，且每次调用都会进行验证。** Claude Code 仅从您的环境中接收一份封闭的环境变量白名单——无 API 密钥、无 token、无云提供商，也不包含启动 aipmt 的 Claude Code 会话标记。在第一个分段之前，`claude auth status` 必须显示订阅连接（不含 Console 密钥），并且不消耗配额的 `/usage` 必须对此进行确认；随后每次调用也会在其初始化事件中进行确认，否则响应将被拒绝。
- **停用“额外用量（extra usage）”**（claude.ai，设置 → 用量），以确保实现零花费：若启用，它会在窗口耗尽时接替并产生费用且不显示错误。一旦调用的配额记录检测到超限，aipmt 会立即停止翻译，但该次调用已被计费。
- **与您的 Claude Code 会话共享配额。** 每次调用都会报告 5 小时及每周窗口的使用情况；超过 80%（`AIPMT_CLAUDE_MAX_UTILIZATION`）时，将不再启动任何后续分段，以免耗尽您日常工作所需的额度。
- **隔离环境。** 每次调用都在一个私有的临时目录中无工具运行，且处于无自定义模式：不会加载您的 `CLAUDE.md`、插件、hook、MCP 服务器或设置，会话中也不会保留任何内容。附件功能已被切断：文档中的 `@chemin` 仅保持为文本，不会打开任何文件（经实测）。
- **模型**：默认使用 `sonnet`，努力程度设为 `low`，在 `--eco` 中亦是如此：`--eco` 在该路径下没有任何影响。在相同文档上的实测显示，`haiku` 的速度慢了两倍——它在无法阻止的情况下进行推理——而成本仅略低一点，且 `opus` 会拒绝生物学内容（见下文）。两者仍可通过 `--model` 访问；这些别名始终指向其家族的最新模型。`fable` 和 `[1m]` 变体会被拒绝，因为它们会走付费点数。`--reasoning_effort` 用于调节努力程度，但翻译并不能从中获益：实测的推理消耗几乎为零。
- **Opus 会拒绝某些生物学内容。** 它的安全防护措施比 Sonnet 更严格，Anthropic 的错误信息也警告称其“can sometimes flag biology-research-adjacent work”。实测：一篇关于生成的 279 个分子的情报快讯导致该文章在所有 14 种语言中均被拒绝。未写入任何内容：aipmt 会拒绝被截断的响应，指出触发的安全机制并建议使用 `--model sonnet`。
- 在 CI 环境（设置了 `CI` 或 `GITHUB_ACTIONS`）和 Windows（未测试）下会被拒绝。
- 变量：`AIPMT_CLAUDE_BIN`（否则依次尝试 `PATH`，然后是 `~/.local/bin/claude`）、`AIPMT_CLAUDE_TIMEOUT`（每个分段的秒数，默认 900）、`AIPMT_CLAUDE_MAX_UTILIZATION`（默认 0.8）、`CLAUDE_CONFIG_DIR`（Claude Code 的账户，绝不会取自项目的 `.env`）；工作目录位于 `XDG_CACHE_HOME/aipmt/claude-code` 下（默认 `~/.cache`）。

**使用条款：涉及的是您自己的账户。** [Claude Code 法律条款页面](https://code.claude.com/docs/en/legal-and-compliance) 并未阻止“an end user from signing in to the unmodified Claude Code binary with their own Claude subscription”：aipmt 正是这么做的，它运行官方二进制文件且绝不读取 token。但 Anthropic“does not permit third-party developers […] to route requests through Free, Pro, or Max plan credentials on behalf of their users”，对第三方工具“including open-source projects”更倾向于使用 API 密钥，并保留将其用量计入付费点数的权利（[Claude 帮助中心](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)）。目前尚无明确条款定性分发给用户并由用户本地调用二进制文件的工具的情况。

**数据**：对于 Free、Pro 和 Max 账户，当隐私设置允许时，模型训练也适用于 Claude Code（[数据政策页面](https://code.claude.com/docs/en/data-usage)）。aipmt 不保留任何本地转录记录（`--no-session-persistence`）。请勿在此处理任何机密信息。

### 对接自定义提供商：`--use_opencode`

[OpenCode](https://opencode.ai) 是一个开源（MIT）代码 Agent，可路由至其内部配置的提供商：API 密钥、订阅、OpenCode Zen 网关（免账户的免费模型）或本地模型。此处对 Zen 和 Ollama 这两种途径进行了端到端实测。

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

`--model` 是必填项：如果没有它，OpenCode 将回退到免费模型，其交互数据可能被用于训练，而此选择不应由程序替您决定。

每次调用的隔离机制：

- 内联配置（优先级高于您的配置）定义了一个 `aipmt` Agent，其所有工具均被禁用（`permission: { "*": "deny" }`），会话共享已关闭，`--pure`，绝不使用 `--auto`；
- 临时的空工作目录，放置了 `OPENCODE_DISABLE_PROJECT_CONFIG` 和 `OPENCODE_DISABLE_CLAUDE_CODE`——若无这些文件，OpenCode 会在 prompt 中注入当前目录的 `AGENTS.md` 和 `~/.claude/CLAUDE.md`。全局 `~/.config/opencode/AGENTS.md` 仍会被注入，OpenCode 不允许将其排除；
- 输出约定：返回码为 0、无 `error` 事件、无工具调用、最后一步为 `stop`、文本非空，且 `aipmt` Agent 已切实加载——未知的 `--agent` 不会导致 OpenCode 报错，而是会静默回退到编码 Agent；
- 不传递任何 `aipmt` 密钥，除 OpenCode 本身的密钥 `OPENCODE_API_KEY` 外。提供商在 OpenCode 中进行配置，而不是在 `aipmt` 的 `.env` 中。

注意事项：

- Zen 的免费模型变动频繁，限制未作说明，且其对话内容可能用于训练：适用于公开文档，不适合私密内容。
- 本地模型必须提供至少 16k tokens 的上下文，因为每个分段最多可达 16,000 个字符。Ollama 通常仅配置 4,096：建议通过包含 `PARAMETER num_ctx 32768` 的 `Modelfile` 来调整。
- `--eco` 无效；`--reasoning_effort` 会作为 OpenCode 的 `--variant` 原样传递。
- OpenCode 会将每次会话记录到 `~/.local/share/opencode/` 中。
- 变量：`OPENCODE_BIN`（否则依次尝试 `PATH`，然后是 `~/.opencode/bin/opencode`）、`OPENCODE_TIMEOUT`（每个分段的秒数，默认 600）。`OPENCODE_CONFIG` 原样传递给 OpenCode。

在 `~/.config/opencode/opencode.json` 中通过 Ollama 使用本地模型的示例：

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

`reasoningEffort: "none"` 可关闭 Ollama 在这些模型上默认启用的思考过程（该设置无法通过 Modelfile 关闭）。在一句由六个词组成的短句上实测：未使用该选项时产生 919 个思考 token，耗时 68 秒；启用后仅产生 9 个 token。

### 连接 400 多个模型：`--use_openrouter`

OpenRouter 是一个按用量计费的路由服务，基于统一余额，对接第三方托管的模型——包括此处其他 provider 均未提供的中国开源模型。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` 是必填项。在产生任何计费之前执行的预检（preflight）会处理该路由机制的两个特性：

- **同一模型由数十个托管商提供，且上限各不相同**——在 `z-ai/glm-5.3-flash` 上有 23 个托管商，其中一家的输出上限仅为 2,048 个 token。预检会读取 `/api/v1/models/{modèle}/endpoints`，排除输出上限低于 8,000 token 或状态降级的托管商，并使用 `allow_fallbacks: false` 锁定其余托管商。
- **推理按输出费率计费**——在 `z-ai/glm-5.2` 上一条简单的“OK”回复就耗费了 107 个 token（正常仅需 2 个）。默认情况下它已被禁用；对于强制开启推理的模型，则传入其允许的最低努力程度，否则目录默认值可能会在翻译完成前耗尽输出上限。`--reasoning_effort` 仍具有最高优先级。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- 上下文窗口信息取自目录。在调用前，低于 16,400 token 的模型会被直接拒绝：8,400 用于 prompt 和分段，至少 8,000 用于输出。
- 若 slug 不在目录中、目录无法访问或没有满足上限要求的托管商，命令将终止。
- 输出为空的 `finish_reason=length` 代表预算被推理耗尽，而非截断：错误消息会对两者进行区分。
- `--eco` 无效。
- 变量：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>）、`OPENROUTER_BASE_URL`（默认 `https://openrouter.ai/api/v1`，要求 `https://`）、`OPENROUTER_TIMEOUT`（默认 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（默认 30）。

### 翻译附注

`--add_translation_note` 用于添加附注，位置可选 `bottom`（默认）、`top`（在 front matter 之后）或 `both`（`--note_position`），格式可选 `legacy`（加粗段落，默认）或 `marker`（`--note_format`）。`marker` 格式是一个不可见的 Markdown 引用定义 `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`，后跟一段加粗引用：在 GitHub 上清晰可读，并可在构建时由 remark 插件进行处理。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 详细测试数据

所有测试数据均为使用 `aipmt` 实际执行的翻译，覆盖 14 种语言：en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi。**已写入** 统计通过了校验检查的文件数量；**无偏差** 统计 `scripts/compare_structure.py` 未检测出任何差异的文件数量——具有相同数量的章节、小标题、链接、唯一定义的 URL、代码块、行内代码、表格行、引用块和加粗词语。

“无偏差”仅表示“未检测出异常”，并不等同于“完全一致”：比对工具只统计元素数量，不读取具体内容。它既不会报告某个四级标题被删、行内代码文本被替换、语言标签被对调，也不会报告内部链接多出一个括号导致链接失效（如 `[texte]((#ancre))`）——同时它也不评估语言翻译质量。

### 高信息密度情报文章，模式 `--news`

[jls42.org 的 AI 技术周报](https://jls42.org/fr/news) 某一期：589 行、140 个链接、21 个章节、3 处受保护的英文引用。测试时间为 2026 年 9 月 4 日至 5 日。

| 模型 | 接入方式 | 已写入 | 无偏差 | 每种语言中位数 |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash` | Google API | 14/14 | ✅ **14/14** | 1 min 18 s |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google 订阅 | 14/14 | ✅ **14/14** | 3 min 59 s |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google 订阅 | 14/14 | ✅ **14/14** | 3 min 14 s |
| `claude-sonnet-5-5` | Anthropic API | 14/14 | ✅ **14/14** | 3 min 37 s |
| `gpt-5.6-sol` (`--use_codex`) | ChatGPT 订阅 | 14/14 | ✅ **14/14** | 11 min 28 s |
| `z-ai/glm-5.2` | OpenRouter | 14/14 | ✅ **14/14** | 5 min 37 s |
| `qwen/qwen3.8-flash` | OpenRouter | 14/14 | ✅ **14/14** | 26 min 23 s |
| `sonnet` (`--use_claude_code`) | Claude 订阅 | 14/14 | ⚠️ 13/14 | 6 min 49 s |
| `claude-sonnet-5` | Anthropic API | 14/14 | ⚠️ 11/14 | 6 min 31 s |
| `haiku` (`--use_claude_code`) | Claude 订阅 | 14/14 | ⚠️ 11/14 | 15 min 54 s |
| `claude-haiku-5-5` | Anthropic API | 14/14 | ⚠️ 11/14 | 2 min 54 s |
| `claude-haiku-4-5` | Anthropic API | 14/14 | ⚠️ 7/14 | 6 min 00 s |
| `opencode/mimo-v2.5-free` | OpenCode Zen | 13/14 | ❌ 11/14 | 9 min 27 s |
| `qwen/qwen3.7-flash` | OpenRouter | 13/14 | ❌ 8/14 | 10 min 09 s |
| `ollama/gpt-oss-20b-32k` | 本地 | 10/14 | ❌ 7/14 | 12 min 39 s |
| `mistral-large-latest` | Mistral API | 11/14 | ❌ 5/14 | 5 min 32 s |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter | 4/14 | ❌ 3/14 | 37 min 27 s |
| `grok-4.6` (`--use_grok_cli`) | Grok 订阅 | 1/14 | ❌ 1/14 | 23 min 11 s |
| `opus` (`--use_claude_code`) | Claude 订阅 | 0/14 | ❌ 0/14 | — |

9 月 9 日在同一情报专栏的另一期（356 行）上对 Grok 进行了重新测试：14 种语言中成功写入 9 种，8 种无偏差。前文总表呈现的正是这一数据。有三次中断的测试未予记录：`qwen3.5-27b`（9 种语言）和 `kimi-k2.6`（4 种）因点数不足而中断；`z-ai/glm-5.3-flash` 的两次失败则是由于推理设置所致，该设置现已被 provider 修复。OpenRouter 相关行是在该路由器的默认设置下测得的，早于 `--use_openrouter`；使用随附 provider 重新测量的 `z-ai/glm-5.2` 同样取得了 14/14 的结果。各项数据已于 9 月 10 日使用当前的比对工具重新计算：与首次发布相比，`qwen3.8-flash` 和 `qwen3.7-flash` 各增加了一种语言，其余保持不变。

`--use_antigravity` 相关行于 9 月 26 日在同一篇文章上进行测试，采用四路并行翻译：上午测试 `gemini-3.7-flash-medium`，下午测试 `gemini-3.8-flash-medium`。在英文翻译中，两者均自行删除了引用下方的三行法文翻译，且未捏造任何语言标记，英文引用完好无损：后备清理机制无需介入。在 `--eco`（`gemini-3.7-flash-low`）下仅测试了四种语言（en、ja、ar、hi）：4 篇全部成功写入，且均无偏差，中位数耗时 1 分 52 秒。同日针对 9 月 25 日更新的一期情报（438 行，2 处英文引用）进行了复测，在博客之外由 `gemini-3.7-flash-medium` 翻译：14 篇全部成功写入，且均无偏差，每种语言耗时 87 至 128 秒。

`--use_claude_code` 相关行于 9 月 26 日在同一篇文章上测得，四路并行翻译，努力程度设为 `low`。使用 `sonnet` 时，英文引用在全部 14 种语言中均完好无损，且在英文翻译中，该模型自行移除了法文翻译内容，未捏造语言标记。`opus` 未能写入任何语言：在每种语言中，其安全机制均在最后一个分段中断了响应，原因是一则关于为结合位点生成的 279 个分子的快讯。该快讯单独发送时会因“生物”类标签被拒；而 `sonnet` 在所有语言中均完成了翻译。`haiku` 成功写入了全部 14 种语言；但在其中三种（en、pl、ro）中，有一个章节标题从二级变为了一级。它在无法阻止的情况下进行推理——占其输出 token 的 61%——因此耗时是 `sonnet` 的两倍以上。

`claude-sonnet-5-5`、`claude-haiku-5-5` 和 `claude-haiku-4-5` 相关行于 10 月 18 日通过 Anthropic API 在同一篇文章上测得，每个模型采用四路并行翻译。Sonnet 5.5 不允许关闭思考功能：aipmt 向其发送它所能接受的最低设置，且其最终响应中不包含任何思考过程。它在全部 14 种语言中均无偏差完成写入，且无需重新翻译任何分段；在英文中，它自行删除了法文翻译内容，未捏造语言标记，英文引用在所有语言中均完好无损。Haiku 5.5 在启用自适应思考模式下进行了测试：关闭思考时，它会留下大段未经翻译的法文段落，从而被校验机制拒绝——14 种语言中仅写入了 3 种。两款 Haiku 都在同一则快讯上遇到了障碍：Haiku 5.5 在日文、韩文和中文中修改了其标题级别或出现了重复标题；Haiku 4.5 在七种语言中将其升为一级标题，并在日文中保留了法文原文。在两篇文档的 14 种语言翻译中，Haiku 4.5 耗费 3.67 美元，Haiku 5.5 耗费 0.57 美元，Sonnet 5.5 耗费 9.21 美元。

### 本项目的 README，标准 Markdown

2026 年 9 月 9 日冻结的版本：785 行，285 个行内代码，40 个代码块闭合标签，89 行表格。4 个并发翻译。

| 模型                                            | 已写入 | 无差异 | 中位数/语言 | 差异内容                                                                 |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 分 43 秒     | 无                                                                       |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 分 48 秒     | 无                                                                       |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 分 02 秒     | 比较器无差异；内部链接重复 (en)                                          |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 分 18 秒     | 无                                                                       |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 分 06 秒     | 无                                                                       |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 秒           | 一个词加粗 (ja)                                                          |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 分 22 秒     | 一个词加粗 (ko)                                                          |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 分 20 秒     | 表格中一行与上一行粘连 (ar)                                             |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 分 56 秒     | 一个链接 (sv)，一个词加粗 (zh)                                           |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 分 46 秒     | 一个词加粗 (ar, ja)                                                      |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 分 34 秒     | 一个词加粗 (hi, ja, ko)                                                  |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 分 17 秒     | 阿拉伯语添加了 40 个行内代码；加粗 (hi, ja, ko)                          |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 分 14 秒     | 2 种语言被拒 (ar, hi)：返回时丢失行内代码                                |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 分 44 秒     | 丢失一个章节 (ar, hi, ko)；添加了代码块 (ja, ko, ro, zh)                 |

两项中断的测试未计入：Grok 在完成 12 种语言后 CLI 会话超时（其中 11 种无差异），以及 `qwen3.8-flash` 在完成 2 种语言后遭遇其托管服务商的 HTTP 429 错误。`opencode/mimo-v2.5-free` 和 `ollama/gpt-oss-20b-32k` 未在此版本上重新测试；在 9 月 4 日至 5 日少 277 行的版本中，它们各自在 14 种语言中写入了 9 篇翻译，分别有 7 篇和 1 篇无差异。

`--use_antigravity` 和 `--use_claude_code` 两行并非在冻结版本上测试，而是在 9 月 26 日随 1.14.0 发布版本上测试的——而 `claude-sonnet-5-5`、`claude-haiku-5-5` 和 `claude-haiku-4-5` 行则是在 10 月 18 日针对同一版本测试的：600 行，257 个行内代码，30 个代码块闭合标签，85 行表格。该版本少了 185 行，因此不能与其他行逐项对比；但这几行之间可以相互对比。在比较器未检查的内部链接方面，`gemini-3.8-flash-medium` 在全部 14 种语言中都保持完好，`gemini-3.7-flash-medium` 在意大利语中损坏；`sonnet` 和 `opus` 在所有语言中均保持完好，`haiku` 在英语中重复；`claude-sonnet-5-5` 和 `claude-haiku-4-5` 在全部 14 种语言中均保持完好，`claude-haiku-5-5` 在其写入的 12 种语言中保持完好。

### 4 个知名项目的 README

FastAPI、Ollama、tldr-pages 和 Vue.js，直接取自 GitHub——比前两个文档更简单。该轮测试针对表现欠佳的模型；Gemini 在此作为参照基准。

| 模型                    | 范围                       | 已写入 | 无差异       |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 个项目 × 14 种语言       | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 个项目 × 14 种语言       | 55/56   | ❌ 47/56     |
| `grok-4.6`（订阅）   | 4 个项目 × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 个项目 × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### 这些测试指标不是什么

- **并非详尽的排名**：仅 OpenRouter 就提供了 400 多个模型，此处仅测试了约 15 个。
- **仅供参考的时间**：各轮测试的并发翻译量为 3 到 6 个不等，且服务商的吞吐量在一天当中会有所波动。
- **具有时效性的观察**：同一名称下的模型会发生变动，且您的文档与我们的并不相同。

如需在您的文档上重现测试（针对文件的冻结副本）：

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

这两行都是必需的：没有 `pip install -e .`，`python -m aipmt` 会返回 `No module named aipmt`。

质量检测工具，可选但推荐使用：

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

仓库中的 28 个翻译（README 和 CHANGELOG，14 种语言）可通过 `./regen_translations.sh --force` 重新生成——默认使用 ChatGPT 订阅上的 Codex 和 `gpt-6.1-sol`，4 个并发。`REGEN_PROVIDER` 和 `REGEN_MODEL` 可更改路径：`antigravity` 同样使用订阅（Google 订阅），无需例外配置即可直接运行；计费 API（`openai`、`gemini`、`grok`、`openrouter`）若无 `REGEN_ALLOW_PAID_API=1` 则会被拒绝；`REGEN_JOB_TIMEOUT` 为每个任务设置上限（600 秒，Codex 和 Antigravity 为 1800 秒）。工具的详细信息请参阅 `CLAUDE.md`。

## 使用此脚本的项目

- **[jls42.org](https://jls42.org)** — 以 15 种语言发布的个人博客。其[每日 AI 资讯](https://jls42.org/fr/news)每天由该工具翻译，并作为上述测试的参考文档。

## 作者

Julien LE SAUX
电子邮箱：contact@jls42.org

## 许可证

GNU 通用公共许可证第 3 版（GNU GENERAL PUBLIC LICENSE Version 3）。详见 [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)。

## 免责声明

本程序在 GPL v3 第 15 条和第 16 条的条款下分发，**不作任何担保**：按“原样”提供，不提供适销性或特定用途适用性的担保，作者对因使用本程序而造成的任何损害概不负责。许可证文本优先于本摘要。

- **发布前请仔细通读。** 保护机制涵盖代码块、行内代码、URL、锚点以及 `--news` 模式下的引用——但不涵盖标题、表格、front matter 或句意。
- **您的文档将发送至所选的服务商**，并遵循其使用条款与数据政策。部分免费模型可能会将您的交互数据用于模型训练，而 Antigravity 的条款允许 Google 重复使用这些数据并让人工审查员进行查阅，即使付费订阅也是如此；本地模型是唯一完全不让任何数据离开您机器的方式。
- **API 调用按量计费。** 本程序不会对开销设置上限：长文档、失败重试或深度推理的模型都会产生更多费用。
- **发布的测试结果均为具有时效性的观察数据**，不作为保证。

文中所提及的产品和公司名称归其各自所有者所有。本项目与其中任何一家均无附属关系。

**使用 gemini-3.8-flash-medium 从法语翻译成中文的文章。**
