# AI-Powered Markdown 翻译器

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 代码质量</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="质量门禁状态"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="安全评级"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="可靠性评级"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="可维护性评级"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="覆盖率"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="漏洞"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="缺陷"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="代码异味"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="重复行 (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="技术债务"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="代码行数"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy 徽章"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

将 Markdown 文件从一种语言翻译为另一种语言，同时完整保留其结构：代码块、行内代码、URL、锚点、表格和 front matter。提供 11 种模型调用途径——5 个 API、4 个非按量计费的订阅服务、2 个路由服务——并公开发布了每个模型实际保留程度的基准测评。

## 概述

- **11 条 Provider 接入途径**：OpenAI、Mistral、Claude、Gemini 和 Grok API；ChatGPT (Codex)、Grok、Google (Antigravity) 以及 Claude (Claude Code) 非按量计费订阅；OpenCode（开源、免费或本地）与 OpenRouter（超过 400 个模型）路由服务。
- **绝不因丢失 Token 而导致内容损坏**：代码块、行内代码、URL、锚点和引用在调用前会被替换为占位 Token，并在返回时进行校验。如果缺失任何一个，则不会写入文件。
- **长文档处理**：根据模型的上下文窗口进行自动分块。
- **`--news` 模式**：保护英文引用并按语言处理国旗图标，专为行业资讯和技术动态类文章设计。
- **`--eco` 模式**：使用更快、成本更低的模型。
- **可选的翻译附注**：可添加在顶部、底部或两者兼有。

## 安装

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 或更高版本。若要从仓库安装，请参阅[贡献指南](#贡献)。

## 配置

密钥按优先级从高到低从以下三个位置读取；后级仅补充前级未设置的项。

|     | 位置                                          | 适用场景                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 环境变量                                      | CI、容器、临时单次覆盖                |
| 2   | 当前目录（或父目录）中的 `.env`        | 项目专属密钥                          |
| 3   | `~/.config/aipmt/.env`                                 | 一次安装，全局生效                    |

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

可以使用 `GEMINI_API_KEY` 代替 `GOOGLE_API_KEY`。用户配置文件遵循 `XDG_CONFIG_HOME`（仅限绝对路径），在 Windows 下遵循 `%APPDATA%`。如果未提供密钥，该命令会列出这三个位置。

**项目的 `.env` 既不能重定向请求，也不能指定执行的程序。** 它只提供密钥，绝不提供目标地址或可执行文件：任何以 `_BASE_URL`、`_API_BASE`、`_ENDPOINT` 或 `_BIN` 开头的变量（`CODEX_BIN`、`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`）、`GROK_HOME`、代理（`HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY`）、证书存储（`SSL_CERT_FILE`、`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）以及 `XDG_CONFIG_HOME` / `APPDATA` 都会被忽略并发出警告。克隆的仓库绝不能窃取您的密钥，也不能在首次翻译时诱使您运行其自带的程序。该文件读取时也不进行变量插值：`NOM=${OPENAI_API_KEY}` 不会在此处复制密钥。请将这些变量设置在环境变量中或置于 `~/.config/aipmt/.env` 中。

可选变量：`XAI_BASE_URL`（默认 `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（每次调用的秒数，默认 900）、`CODEX_BIN`、`CODEX_TIMEOUT`（默认 600）、`GROK_BIN`、`GROK_HOME`（默认 `~/.grok`）、`GROK_TIMEOUT`（默认 900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（默认 900）、`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（默认 600）、`OPENROUTER_BASE_URL`（必须指定 `https://`）、`OPENROUTER_TIMEOUT`（默认 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（默认 30）。每个变量均在其对应的 Provider 章节中详细说明。

## 快速上手

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

将 `document.md` 翻译为西班牙语会在 `--target_dir` 中生成 `document-es.md`；使用 `--include_model` 则生成 `document-es-gpt-5.6-terra.md`。扩展名始终会转换为 `.md`——`article.mdx` 会生成 `article-en.md`——除非使用 `--keep_filename` 保留原始名称。如果未指定 `--force`，已存在的翻译将被跳过。

退出代码：若全部成功或被跳过则为 `0`，若有文件失败则为 `1`（在标准错误输出中列出清单），若配置存在问题则为 `2`。失败的文件绝不会被写入，即使写入过程本身出错也是如此：内容会先写入临时文件然后再重命名。只需重新运行即可。

## 如何选择模型

基于两份真实文档进行测试，每个模型均将其翻译为相同的 14 种语言。**数字表示在全部 14 种语言中，翻译成功写入且与原文结构毫无偏差的语言数量。**

| 模型                 | 访问方式                          | 密集型资讯文章          | 本 README    | 差异情况及受影响的语言数量                                                                                                         |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.8 Flash** | Google 订阅 (Antigravity)         | ✅ 14/14                | ✅ 14/14     | 两份文档均毫无偏差                                                                                                                 |
| **Gemini 3.7 Flash** | Google API 密钥                   | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种：多出一个加粗词 (ja)                                                                                            |
| **Gemini 3.7 Flash** | Google 订阅 (Antigravity)         | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种：少了一个加粗词 (ko)                                                                                            |
| **GPT-5.6 Sol**      | ChatGPT 订阅或 OpenAI 密钥        | ✅ 14/14                | ⚠️ 12/14     | 14 种语言中有 2 种：少了一个加粗词 (ar, ja)                                                                                        |
| **GLM-5.2**          | OpenRouter 密钥                   | ✅ 14/14                | ⚠️ 11/14     | 14 种语言中有 3 种：少了一个加粗词 (hi, ja, ko)                                                                                    |
| Claude Sonnet 5      | Claude 订阅 (Claude Code)         | ⚠️ 13/14                | ⚠️ 13/14     | 资讯文章 14 种语言中有 1 种：多出一个加粗词 (zh)；本 README 中有 1 种：表格行与上一行粘连，导致渲染时被隐藏 (ar)                  |
| Claude Haiku 4.5     | Claude 订阅 (Claude Code)         | ⚠️ 11/14                | ✅ 14/14     | 资讯文章 14 种语言中有 3 种：某个小节标题被提升为 1 级 (en, pl, ro)；本 README 中对比工具未见异常，但内部链接在英语中被重复       |
| Claude Sonnet 5      | Anthropic API 密钥                | ⚠️ 11/14                | ⚠️ 12/14     | 资讯文章 14 种语言中有 3 种：多出一个代码块 (es, de, hi)；本 README 中有 2 种：一个链接丢失了标记 (sv)，一个词被加粗 (zh)         |
| Qwen 3.7 Flash       | OpenRouter 密钥                   | ❌ 8/14                 | ⚠️ 10/14     | 资讯文章有 1 种语言被拒，另有 5 种出现偏差；本 README 中有约 40 个词被放入 `code` (ar)                                     |
| Grok 4.6             | Grok 订阅                         | ❌ 8/14                 | 未评级       | 14 种语言中有 5 种被拒（因行内代码与 URL 未还原）；荷兰语则完全偏离                                                                |
| GPT-OSS 20B          | 本地模型 (Ollama)                 | ❌ 7/14                 | 未重新测评   | 14 种语言中有 4 种被拒：模型残留了法语段落，被保护校验拦截                                                                         |
| MiMo v2.5 (免费)     | OpenCode Zen（免账户）            | ❌ 11/14                | 未重新测评   | 1 种语言被拒；波兰语丢失了一个章节                                                                                                 |
| Mistral Large        | Mistral API 密钥                  | ❌ 5/14                 | ❌ 1/14      | **整节内容丢失**：资讯文章中有 1 种语言 (hi)，本 README 中有 3 种语言 (ar, hi, ko)——且资讯文章中有 3 种语言被拒                   |
| DeepSeek V4 Flash    | OpenRouter 密钥                   | ❌ 3/14                 | 未重新测评   | 14 种语言中有 10 种被拒；每种语言耗时 37 分钟                                                                                      |
| Claude Opus 5.5      | Claude 订阅 (Claude Code)         | ❌ 0/14                 | ✅ 14/14     | 资讯文章因一篇生物学简讯触发 Opus 安全护栏而在全部 14 种语言中均被拒；本 README 则毫无偏差                                         |

|     | 符号含义                                                                                                                                                                                              |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14 种语言全部完成翻译，且与原文相比毫无偏差                                                                                                                                                          |
| ⚠️  | 14 种语言全部完成翻译；差异仅限于**标记格式**——多出或少了一个加粗词、一个 `code`、链接丢失方括号等。没有缺失任何文本、URL、代码块或章节                                                   |
| ❌  | 至少有一种语言无法完成翻译——文件被拒，未写入——**或者**已写入的文件中缺失了内容                                                                                                                       |

核心要点：

- **被拒绝的翻译并不等同于损坏的翻译。** 当返回结果中缺失 Token 时，文件不会被写入，该语言会被计为被拒绝。这正是 Grok 在资讯文章中遇到的情况：在 5 种非拉丁文字语言中，仅第一个分块就丢失了 4 处行内代码和 3 个 URL。
- **模型可能仅仅因为一句话而拒绝整个文档。** Opus 5.5 翻译本 README 时毫厘不差，但面对资讯文章却全部失败：其安全机制在遇到一篇生物学简讯时强行中断了响应。文件未被写入，且 aipmt 会给出具体原因。
- **这一安全网未覆盖标题、表格、front matter 以及正文文本。** 如果模型删除了某个章节，工具仍会照常写入文件——Mistral 就是这种情况。这些元素无法替换为占位 Token，当前的安全校验也不会拦截它们；`scripts/compare_structure.py` 可以检测到缺失的章节，但属于事后检测。
- **Grok 在本 README 中未评级**：其 CLI 会话在处理完 12 种语言后过期（其中 11 种毫无偏差）。中断的评测不计入成绩。
- **文档的密集程度比目标语言更具决定性。** Grok 可以稳定处理普通的 README，但在包含大量链接的文章中就会崩溃，即使在荷兰语翻译中也是如此。

测试日期与文档：“本 README”一栏测于 2026 年 9 月 9 日，基于本文件当时的一个固定版本（785 行，285 处行内代码，89 行表格），此后该版本有所修改——但 Antigravity 和 Claude Code 两行除外，它们测于 9 月 26 日，基于随 1.14.0 发布的较短版本（600 行，257 处行内代码，85 行表格）。“密集型资讯文章”一栏来自 9 月 4 日至 5 日对一篇 589 行文章的评测，但 Grok 行除外（于 9 月 9 日在同类资讯的另一期上重新测定），以及 Antigravity 和 Claude Code 行（于 9 月 26 日在同一文章上测定）。完整表格、耗时和测试协议请参阅[详细测评数据](#详细评测数据)。

## 所有选项

| 选项                     | 说明                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 要翻译的单个 Markdown 文件（`--source_dir` 的替代项）                                                         |
| `--source_dir`           | 包含 Markdown 文件的源目录（默认：`content/posts`）                                                            |
| `--target_dir`           | 已翻译文件的输出目录（默认：`traductions_en`）                                                                  |
| `--source_lang`          | 源语言（默认：`fr`）                                                                                |
| `--target_lang`          | 目标语言（默认：`en`）                                                                              |
| `--model`                | 要使用的特定模型                                                                                              |
| `--eco`                  | 使用经济型模型                                                                                                |
| `--use_mistral`          | 使用 Mistral AI API                                                                                           |
| `--use_claude`           | 使用 Claude API                                                                                               |
| `--use_gemini`           | 使用 Gemini API                                                                                               |
| `--use_grok`             | 使用 xAI (Grok) API —— 需要 `XAI_API_KEY`                                                                    |
| `--use_codex`            | 使用 Codex CLI 并消耗 ChatGPT 订阅配额                                                                        |
| `--use_grok_cli`         | 使用 Grok CLI 并消耗 Grok 订阅配额                                                                            |
| `--use_antigravity`      | 使用 Antigravity CLI（`agy`）并消耗 Google AI Pro 或 Ultra 订阅配额                                  |
| `--use_claude_code`      | 使用 Claude Code CLI（`claude -p`）并消耗 Claude Pro 或 Max 订阅配额                                        |
| `--use_opencode`         | 使用 OpenCode（开源）连接至在 OpenCode 中配置的提供商；需要 `--model provider/modèle`                                    |
| `--use_openrouter`       | 使用 OpenRouter —— 需要 `OPENROUTER_API_KEY` 和 `--model fournisseur/modèle`                                                      |
| `--force`                | 强制重新翻译                                                                                                  |
| `--keep_filename`        | 保留原始文件名                                                                                                |
| `--news`                 | 新闻模式：保护英文引用，按语言处理国旗/标志                                                                   |
| `--add_translation_note` | 添加翻译说明                                                                                                  |
| `--note_position`        | 说明位置：`top`、`bottom`（默认）或 `both`                                             |
| `--note_format`          | 说明格式：`legacy`（默认，粗体段落）或 `marker`                                                 |
| `--include_model`        | 在输出文件中包含模型名称                                                                                      |
| `--reasoning_effort`     | GPT-5.x 推理力度：`none`/`low`/`medium`/`high`/`xhigh`              |

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

`--eco` 会切换至每个提供商的经济型层级。

| 提供商      | 质量（默认）                                          | 经济型（`--eco`） |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol`（亦可通过 `--model` 指定 `terra` 与 `luna`） | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`，力度 `low`                                | 同上 —— `--eco` 无效 |
| OpenCode    | 必需 `--model provider/modèle`                 | 同上 —— `--eco` 无效 |
| OpenRouter  | 必需 `--model fournisseur/modèle`              | 同上 —— `--eco` 无效 |

### 使用 ChatGPT 订阅：`--use_codex`

调用官方 Codex CLI：翻译将从 ChatGPT 订阅配额中扣除，无需 API 密钥或按用量计费。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 二进制文件会依次在 `CODEX_BIN`、`PATH`、以及 `openai-codex-cli-bin` 包中查找。从不读取 `~/.codex/auth.json`。
- `OPENAI_API_KEY` 和 `CODEX_API_KEY` 会从子进程环境中移除：即使存在密钥也不会切换到 API。
- 每个分段在 5 小时窗口期内至少消耗 1 条“消息”——若验证失败并重试，则消耗 2 条。OpenAI 给出的预估参考值为：Plus 方案下 `gpt-5.6-luna`（`--eco`）为 250–2,000 条消息/5 小时，`gpt-5.6-sol` 为 10–100 条。
- `--model gpt-5.6-terra` 和 `--model gpt-5.6-luna` 同样通过订阅进行。使用账户无权访问的模型会返回 400 “model is not supported when using Codex with a ChatGPT account”。
- 比 API 更慢，且差距随文档大小而增加：在本 README 上，使用 `gpt-5.6-sol` 每种语言的中位数耗时为 6 分 46 秒，而 `gemini-3.7-flash` 仅需 36 秒。
- 在 CI 中被拒绝（定义了 `CI` 或 `GITHUB_ACTIONS`）：订阅通过个人会话文件进行身份验证，绝不应出现在共享 runner 上。
- 环境变量：`CODEX_BIN`、`CODEX_TIMEOUT`（每个分段的秒数，默认 600）。

### 使用 Grok 订阅：`--use_grok_cli`

使用官方 Grok Build CLI，基于 SuperGrok 或 X Premium+ 订阅，原理相同。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **隔离性弱于 Codex。** Grok 的操作系统沙箱在许多较新的 Linux 设备上无法生效（AppArmor、容器运行时套接字），而无法应用的配置集会在静默状态下以未隔离方式启动。因此该脚本默认不请求任何配置集，并对此作出提示，转而依赖 CLI 的 `--deny` 规则（包括兜底的 `*`）——这是唯一一层宁可拒绝启动也不会隐瞒撤销防护的机制。`GROK_TRANSLATE_SANDBOX=read-only` 则强制要求操作系统沙箱，若机器无法满足该要求则启动失败。
- 配额为每周配额，与 Chat、Imagine 和 Voice 共享，且没有任何命令可以读取该配额：批量任务可能会在没有任何提醒的情况下消耗对话用量。
- 环境变量：`GROK_BIN`、`GROK_HOME`（CLI 目录，默认 `~/.grok`）、`GROK_TIMEOUT`（默认 900）、`GROK_TRANSLATE_SANDBOX`。

### 使用 Google 订阅：`--use_antigravity`

使用 Antigravity 官方 CLI `agy`，原理相同：对于订阅了 Google AI Pro 或 Ultra 的用户，翻译将从订阅配额中扣除，而不是按 token 计费。这是使用该配额的唯一途径：自 2026 年 6 月 18 日起，Gemini CLI 已不再服务这些账户（[公告](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)），且 Antigravity SDK 仅接受 API 密钥或 Google Cloud 项目。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **不留任何付费途径。** agy 仅从您的环境中接收一份封闭的环境变量白名单——`PATH`、语言和时区、终端、身份标识、代理与证书、会话总线——且不包含任何密钥：其多个变量会在不显示任何提示的情况下切换调用（实测：其中一个会将文档发送至第三方网关，另一个则发送至计费的 Google Cloud 项目），而黑名单机制每次复核都会有所遗漏。在处理任何分段前，不消耗任何配额的 `agy -p /config` 必须显示付费 AI 积分已禁用，且没有 API 密钥或 Google Cloud 项目——设置项缺失即视作拒绝——否则不翻译任何内容；随后的每次调用日志还必须证明使用了订阅（`authMethod=consumer`），否则响应将被拒绝。
- **隔离机制。** 每次调用都在一个私有且一次性的主目录中运行，并配备一个不带工具的翻译代理：您原有的 agy 设置、规则、插件、MCP 服务器和钩子均不会带入其中，任何内容都不会写入您的历史记录，登录凭据保留在密钥环中，aipmt 从不读取。若找不到代理，agy 会隐匿回退到其编程代理及工具：日志中必须有一整行明确确认使用了正确的代理——文档中引用该消息无法替代这一确认——否则拒绝执行。
- **支持平台**：Linux，运行在拥有密钥环的会话中（D-Bus 会话总线、Secret Service）；支持 macOS，但未经实测。在 Windows 下会被拒绝，因为 agy 不会读取用于隔离各次调用的变量；在没有会话总线的 Linux 下（SSH 会话、容器、服务器）也会被拒绝：agy 会将令牌存放在 `~/.gemini` 的文件中，而隔离机制会将其屏蔽。拒绝会在启动前发生并附带原因，而不是等待一分钟去接收登录码。
- **模型**：`agy models` 中的模型。Gemini 模型在名称中体现力度（`gemini-3.8-flash-medium`…）：无后缀的名称将在调用前被拒绝，且 `--reasoning_effort` 无效。默认 `gemini-3.8-flash-medium`，在 `--eco` 下为 `gemini-3.7-flash-low`；确定这些配置的评测活动已在[详细评测](#详细评测数据)中说明。Claude 和 GPT-OSS 拥有各自独立且小得多的配额：每次实测调用约占 5 小时窗口的 1%，而 Flash 仅约占 0.05%。
- **配额**：按组划分，设有 5 小时窗口期和每周窗口期，按 token 成本比例折算。在作者账户上的实测为：在 `gemini-3.8-flash-medium` 下，源文本每百万字符消耗约 16 点 5 小时窗口额度，`gemini-3.7-flash-medium` 约 14 点，低力度下为 7 至 8 点——因此一个 40,000 字符的 README 消耗略高于半点。每周上限则取决于套餐层级。重试遵循 agy 声明为可重试的情况；否则，耗尽的窗口绝不会重试：它会导致每个文件均执行失败，直至 `/usage` 显示的重置时间。
- **比 API 更慢**：在测试所用的高密度评测文章上，以中位数计，`gemini-3.8-flash-medium` 每种语言耗时 3 分 59 秒，`gemini-3.7-flash-medium` 耗时 3 分 14 秒，而 Gemini 3.7 Flash 通过 API 仅需 1 分 18 秒。
- **中断**：Ctrl-C 或关闭终端会连同命令一起终止 agy，而不是任其继续运行耗尽您的配额；Codex、Grok CLI 和 OpenCode 亦是如此。在 `nohup` 下，翻译将继续进行。
- 在 CI 中被拒绝（定义了 `CI` 或 `GITHUB_ACTIONS`）：登录凭据保存在个人密钥环中。在 runner 上，请结合 `GOOGLE_API_KEY` 使用 `--use_gemini`。
- 环境变量：`AGY_BIN`（否则依次查找 `PATH`、`~/.local/bin/agy`）、`AGY_TIMEOUT`（每个分段的秒数，包含启动时间，默认 900）。

**服务条款：由此产生的后果由您的个人账户承担。** [Antigravity 服务条款](https://antigravity.google/terms)（第 6 节）及其 [FAQ](https://antigravity.google/docs/faq/) 禁止通过第三方软件利用 Antigravity 登录凭据访问该服务——其中明确提及了 Claude Code、OpenClaw 和 OpenCode——违者可能面临账户封禁。aipmt 既不读取也不复用该令牌：它仅在 Google 针对脚本和 CI 所记载的[无头模式（headless）](https://antigravity.google/docs/cli/headless/)下启动官方二进制文件。Google 的一名成员曾表示，在本地脚本中为个人工作启动 `agy -p` 属于“标准用法”（[官方论坛，2026 年 9 月 25 日，非约束性回复](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）；但目前尚无明确条款定性此类公开发布的工具。

**仅限公开文档。** 根据相同条款的第 5 节，交互内容（提示词、回复、元数据）可能会被用于改进 Google 的产品和机器学习，并可能接受人工审查，即使是付费订阅亦不例外。退出该机制需通过 `enableTelemetry` 设置，但其具体效果未有文档说明，且 aipmt 不会设置该项；您原有的 agy 设置在隔离环境中也不会生效。切勿用其处理任何机密内容。

### 在 Claude 订阅上：`--use_claude_code`

使用 Claude Code 的官方 CLI `claude` 在 `-p` 模式下也是同样的原理：对于付费订阅 Claude Pro 或 Max 的用户，翻译会从订阅配额中扣除，而不是按 token 计费。请勿将其与 Anthropic 按使用量计费的 API `--use_claude` 混淆。

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **不保留任何付费途径，且每次调用都会进行验证。** Claude Code 仅从您的环境中接收一份受限的变量列表——既没有 API 密钥、令牌、云提供商，也没有可能启动 aipmt 的 Claude Code 会话标记。在第一个分段之前，`claude auth status` 必须显示订阅连接（不含 Console 密钥），而无需消耗任何配额的 `/usage` 必须对此进行证实；每次调用随后都会在其初始化事件中证实这一点，否则响应将被拒绝。
- **停用“额外用量”（extra usage）**（claude.ai，设置 → 使用量），以确保实现零费用：一旦启用，它会在窗口用尽时接管并计费，且不会显示任何错误。一旦某次调用的配额记录检测到该情况，aipmt 就会停止翻译，但该次调用已被计费。
- **与您的 Claude Code 会话共享配额。** 每次调用都会报告 5 小时窗口和周窗口的使用情况；超过 80%（`AIPMT_CLAUDE_MAX_UTILIZATION`）后，将不再启动任何分段，以免耗尽用于您日常工作的配额。
- **隔离运行。** 每次调用都在没有工具的情况下、在私有且一次性的目录中以无自定义模式运行：既不会加载您的 `CLAUDE.md`，也不会加载您的插件、钩子（hooks）、MCP 服务器或设置，会话内容也不会保留。附件已被切断：文档中的 `@chemin` 仍保留为纯文本，不会打开任何文件（经实测）。
- **模型**：默认使用 `sonnet`，努力程度为 `low`，在 `--eco` 下亦然：在此路径上 `--eco` 不会产生任何改变。在相同文档上的测试显示，`haiku` 速度慢了一倍——它会在无法阻止的情况下进行推理——而成本仅略低一点，且 `opus` 会拒绝生物学内容（见下文）。两者仍可通过 `--model` 访问；这些别名始终指向其家族的最新模型。`fable` 及 `[1m]` 变体均被拒绝，因为它们会转为付费积分计费。`--reasoning_effort` 用于调节努力程度，但翻译从中毫无获益：测得的推理开销几乎为零。
- **Opus 会拒绝某些生物学内容。** 其安全护栏比 Sonnet 更严格，Anthropic 的错误信息警告称它们“can sometimes flag biology-research-adjacent work”。实测表明：一篇关于生成的 279 个分子的简报导致该文章在所有 14 种语言中均被拒绝。没有写入任何内容：aipmt 会拒绝被截断的响应，指出安全护栏问题并建议使用 `--model sonnet`。
- 在 CI 中被拒绝（定义了 `CI` 或 `GITHUB_ACTIONS`）以及在 Windows 下被拒绝（未测试）。
- 变量：`AIPMT_CLAUDE_BIN`（否则使用 `PATH`，然后是 `~/.local/bin/claude`）、`AIPMT_CLAUDE_TIMEOUT`（每个分段的秒数，默认 900）、`AIPMT_CLAUDE_MAX_UTILIZATION`（默认 0.8）、`CLAUDE_CONFIG_DIR`（Claude Code 的账户，绝不从项目的 `.env` 中获取）；工作目录位于 `XDG_CACHE_HOME/aipmt/claude-code` 下（默认 `~/.cache`）。

**使用条款：涉及的是您自己的账户。** Claude Code 的[法律条款页面](https://code.claude.com/docs/en/legal-and-compliance)并不阻止“an end user from signing in to the unmodified Claude Code binary with their own Claude subscription”：aipmt 正是这样做的，它启动官方二进制文件且绝不读取令牌。但 Anthropic“does not permit third-party developers […] to route requests through Free, Pro, or Max plan credentials on behalf of their users”，对第三方工具（“including open-source projects”）倾向于使用 API 密钥，并保留从付费积分中扣除其使用量的权利（[Claude 帮助](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)）。目前没有任何文本明确界定分发启动该二进制文件的工具这一情况。

**数据**：在 Free、Pro 和 Max 账户上，当隐私设置允许时，模型训练也适用于 Claude Code（[数据页面](https://code.claude.com/docs/en/data-usage)）。aipmt 不保留任何本地转录记录（`--no-session-persistence`）。请勿在其中传输任何机密内容。

### 接入自选提供商：`--use_opencode`

[OpenCode](https://opencode.ai) 是一个开源代码智能体（MIT），可路由到其内部配置的提供商：API 密钥、订阅、OpenCode Zen 网关（免费模型，无需账户）或本地模型。此处对 Zen 和 Ollama 两种途径进行了端到端实测。

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

`--model` 是必填项：缺少它，OpenCode 将回退到免费模型，其交互内容可能被用于训练，而此选择不应由他人代您决定。

每次调用的隔离机制：

- 内联配置优先于您的配置，定义了一个所有工具均被拒绝（`permission: { "*": "deny" }`）的智能体 `aipmt`，会话共享已禁用，`--pure`，绝不使用 `--auto`；
- 临时且空置的工作目录，放置了 `OPENCODE_DISABLE_PROJECT_CONFIG` 和 `OPENCODE_DISABLE_CLAUDE_CODE`——没有它们，OpenCode 会在 prompt 中注入当前目录的 `AGENTS.md` 和 `~/.claude/CLAUDE.md`。全局 `~/.config/opencode/AGENTS.md` 仍会被注入，OpenCode 不支持将其排除；
- 输出契约：返回码 0、无 `error` 事件、无工具调用、最后一步为 `stop`、文本非空，且智能体 `aipmt` 已成功加载——未知的 `--agent` 不会导致 OpenCode 报错失败，而是会静默回退到编码智能体；
- 除了 OpenCode 自身的密钥 `OPENCODE_API_KEY` 外，不传递任何 `aipmt` 密钥。提供商应在 OpenCode 中配置，而不是在 `aipmt` 的 `.env` 中配置。

须知：

- Zen 的免费模型变化频繁，限制未作说明，且交互内容可能被用于训练：适用于公开文档，不适用于私密内容。
- 本地模型必须提供至少 16k token 的上下文，因为分段最长可达 16,000 个字符。Ollama 通常默认配置为 4,096：请通过带有 `PARAMETER num_ctx 32768` 的 `Modelfile` 进行配置。
- `--eco` 无效；`--reasoning_effort` 作为 OpenCode 的 `--variant` 原样传递。
- OpenCode 会将每个会话记录在 `~/.local/share/opencode/` 中。
- 变量：`OPENCODE_BIN`（否则使用 `PATH`，然后是 `~/.opencode/bin/opencode`）、`OPENCODE_TIMEOUT`（每个分段的秒数，默认 600）。`OPENCODE_CONFIG` 原样传递给 OpenCode。

通过 Ollama 使用本地模型的示例，位于 `~/.config/opencode/opencode.json`：

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

`reasoningEffort: "none"` 会关闭 Ollama 默认在这些模型上启用的思考，而 Modelfile 无法将其禁用。在一个六个单词的句子上的实测结果：不带该选项时有 919 个思考 token 耗时 68 秒，带该选项时仅 9 个 token。

### 接入超过 400 种模型：`--use_openrouter`

OpenRouter 是一个按使用量计费的路由平台，使用统一积分，聚合了由第三方托管的模型——其中包括此处其他提供商未提供的中国开源模型。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` 是必填项。在产生任何计费之前执行的预检，会处理该路由机制的两大特性：

- **同一模型由数十家具有不同上限的托管商提供服务**——在 `z-ai/glm-5.3-flash` 上，有 23 家托管商，其中一家输出上限仅为 2,048 个 token。预检会读取 `/api/v1/models/{modèle}/endpoints`，排除输出上限低于 8,000 个 token 或状态降级的托管商，并使用 `allow_fallbacks: false` 固定其他托管商。
- **推理按输出费率计费**——在 `z-ai/glm-5.2` 的“OK”回复中，推理消耗了 107 个 token，而实际输出仅 2 个。推理默认被关闭；强制启用推理的模型将接收其允许的最低努力程度，因为目录默认值可能会在翻译完成前耗尽输出配额。`--reasoning_effort` 仍具有最高优先级。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- 上下文窗口取自目录。在执行任何调用之前，低于 16,400 个 token 的模型将被拒绝：prompt 和分段需要 8,400 个，输出至少需要 8,000 个。
- 目录中不存在 slug、无法访问目录或缺少满足上限要求的托管商，都会中止命令。
- 伴随空输出的 `finish_reason=length` 是因推理耗尽了预算，而非截断：报错信息对此进行了区分。
- `--eco` 无效。
- 变量：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>）、`OPENROUTER_BASE_URL`（默认 `https://openrouter.ai/api/v1`，要求 `https://`）、`OPENROUTER_TIMEOUT`（默认 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（默认 30）。

### 翻译说明

`--add_translation_note` 会添加一条说明，位置可设为 `bottom`（默认）、`top`（位于 front matter 之后）或 `both`（`--note_position`），格式可采用 `legacy`（加粗段落，默认）或 `marker`（`--note_format`）。`marker` 格式是一段不可见的 Markdown 引用定义：
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`，
后跟一段加粗引用：在 GitHub 上清晰可读，在构建时可供 remark 插件使用。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 详细评测数据

所有评测均为使用 `aipmt` 实际执行的翻译，覆盖 14 种语言：en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi。**已写入**统计守卫机制放行的文件数；**无差异**统计 `scripts/compare_structure.py` 未发现任何差异的文件数——章节数、小标题数、链接数、独立 URL 数、代码块数、行内代码数、表格行数、引用块数和加粗词数均完全一致。

“无差异”意味着“未检测到问题”，而非“完全相同”：比较工具仅统计元素数量，不读取其内容。它不会报告 4 级标题被删除、行内代码文本被替换、语言标签被调换，也不会报告内部链接因多渲染了一个括号（`[texte]((#ancre))`）而失效的情况——同时它也不会评判语言质量。

### 密集型资讯文章，`--news` 模式

[jls42.org AI 资讯](https://jls42.org/fr/news)的一期内容：589 行、140 个链接、21 个章节、3 处受保护的英文引用。测试时间为 2026 年 9 月 4 日和 5 日。

| 模型                                            | 接入方式           | 已写入  | 无差异       | 中位数/语言    |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google 订阅        | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google 订阅        | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT 订阅       | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | Claude 订阅        | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | Claude 订阅        | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | 本地               | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok 订阅          | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | Claude 订阅        | 0/14    | ❌ 0/14      | —              |

Grok 于 9 月 9 日在同一资讯的另一期（356 行）上进行了重新测试：14 种语言中写入 9 种，8 种无差异。顶部的汇总表格中采用的正是这一数据。未计入三次中断的测试：`qwen3.5-27b`（9 种语言）和 `kimi-k2.6`（4 种）因积分不足而中断，`z-ai/glm-5.3-flash` 的两次失败源于推理设置问题，该提供商此后已对此修复。OpenRouter 各行是在路由器的默认设置下测量的，早于 `--use_openrouter`；使用随附提供商重新测试的 `z-ai/glm-5.2` 同样达到了 14/14。数据于 9 月 10 日使用当前的比对工具重新计算：与首次发布相比，`qwen3.8-flash` 和 `qwen3.7-flash` 各增加了一种语言，其他保持不变。

`--use_antigravity` 的数据于 9 月 26 日在同一文章上测得，进行了四次并行翻译：上午为 `gemini-3.7-flash-medium`，下午为 `gemini-3.8-flash-medium`。在英语中，两者均自行删除了引用下方的三行法语翻译，且未捏造任何语言标签，英文引用保持原样：后备清理程序无需执行任何操作。在 `--eco`（`gemini-3.7-flash-low`）下，仅测试了四种语言（en、ja、ar、hi）：4 种全部写入，全部无差异，中位时间为 1 min 52 s。同一天在较新的一期资讯（9 月 25 日，438 行，2 处英文引用）上进行了复验，由 `gemini-3.7-flash-medium` 在博客外进行翻译：14 种全部写入，全部无差异，每种语言用时 87 至 128 s。

`--use_claude_code` 的数据于 9 月 26 日在同一文章上测得，进行了四次并行翻译，努力程度为 `low`。使用 `sonnet` 时，英文引用在所有 14 种语言中均完好无损，且在英语翻译中，该模型自行删除了法语翻译行，未捏造任何语言标签。`opus` 未能写入任何语言：在每种语言中，其安全护栏均在最后一个分段中止了响应，原因是一篇关于为结合位点生成的 279 个分子的简报。单独发送该简报时，它会因属于“bio”类别而被拒绝；而 `sonnet` 在所有语言中均完成了翻译。`haiku` 写入了所有 14 种语言；但在其中三种（en、pl、ro）中，有一个章节标题从 2 级变成了 1 级。它会在无法阻止的情况下进行推理——占其输出 token 的 61%——因此耗时达到了 `sonnet` 的两倍以上。

### 本项目 README，标准 Markdown

2026 年 9 月 9 日冻结版本：785 行，285 个行内代码，40 个代码块闭合标记，89 行表格。4 个并行翻译。

| 模型                                            | 已写入 | 无偏差     | 中位数/语言 | 差异说明                                                                 |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 分 43 秒     | 无                                                                       |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 分 48 秒     | 无                                                                       |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 分 02 秒     | 对比器检测无差异；内部链接重复 (en)                                      |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 秒          | 一个加粗词 (ja)                                                          |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 分 22 秒     | 一个加粗词 (ko)                                                          |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 分 20 秒     | 一行表格与上一行粘连 (ar)                                                |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 分 56 秒     | 一个链接 (sv)，一个加粗词 (zh)                                           |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 分 46 秒     | 一个加粗词 (ar, ja)                                                      |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 分 34 秒     | 一个加粗词 (hi, ja, ko)                                                  |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 分 17 秒     | 阿拉伯语中增加了 40 个行内代码；加粗 (hi, ja, ko)                        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 分 44 秒     | 丢失一个章节 (ar, hi, ko)；添加了代码块 (ja, ko, ro, zh)                 |

两次中断的评测未计入：Grok 在完成 12 种语言后 CLI 会话过期（其中 11 种无偏差），以及 `qwen3.8-flash` 在完成 2 种语言后遭遇托管商的 HTTP 429。`opencode/mimo-v2.5-free` 与 `ollama/gpt-oss-20b-32k` 未在此版本上重新测试；在 9 月 4 日至 5 日的版本（缩短了 277 行）中，它们各自写入了 14 种语言中的 9 种，其中分别有 7 种和 1 种无偏差。

`--use_antigravity` 与 `--use_claude_code` 行未在冻结版本上测试，而是在 9 月 26 日随 1.14.0 发布的版本上测试的：600 行，257 个行内代码，30 个代码块闭合标记，85 行表格。该版本缩短了 185 行，不能直接与其他行逐项对比；但这两行之间可以相互对比。在对比器不校验的内部链接方面，`gemini-3.8-flash-medium` 在 14 种语言中均保持完好，`gemini-3.7-flash-medium` 在意大利语中损坏；`sonnet` 和 `opus` 在所有语言中均保持完好，`haiku` 在英语中出现了重复。

### 四个知名项目的 README

FastAPI、Ollama、tldr-pages 和 Vue.js，直接取自 GitHub——比前两份文档更简单。本轮测试针对表现欠佳的模型；Gemini 用作基准参考。

| 模型                      | 范围                       | 已写入  | 无偏差       |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 个项目 × 14 种语言       | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 个项目 × 14 种语言       | 55/56   | ❌ 47/56     |
| `grok-4.6` (订阅版)    | 4 个项目 × ar, hi, ja, zh  | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 个项目 × ar, hi, ja, zh  | 15/16   | ❌ 9/16      |

### 这些测试不是什么

- **并非详尽的排名**：仅 OpenRouter 就提供了四百多个模型，此处仅测试了约十五个。
- **仅供参考的耗时**：根据评测批次不同，采用三到六个并行翻译，且服务商的吞吐速率在一天中会有所波动。
- **特定日期的观察结果**：模型即使同名也会更新迭代，且您的文档与我们的并不相同。

若要在您自己的文档上使用文件的冻结副本复现测试：

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

两行都是必需的：如果没有 `pip install -e .`，`python -m aipmt` 会返回 `No module named aipmt`。

质量工具链（可选但推荐）：

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

仓库中的 28 个翻译（README 和 CHANGELOG，14 种语言）可通过 `./regen_translations.sh --force` 重新生成——默认使用 ChatGPT 订阅上的 Codex 和 `gpt-5.6-sol`，4 个并行。`REGEN_PROVIDER` 和 `REGEN_MODEL` 可更改路径：`antigravity` 仍使用订阅（Google 订阅），且无需特殊授权即可通过；计费 API（`openai`、`gemini`、`grok`、`openrouter`）若无 `REGEN_ALLOW_PAID_API=1` 则会被拒绝；`REGEN_JOB_TIMEOUT` 限制每个任务的上限（Codex 和 Antigravity 上为 600 秒、1 800 秒）。工具链的详细信息请参见 `CLAUDE.md`。

## 使用此脚本的项目

- **[jls42.org](https://jls42.org)**——以 15 种语言发布的个人博客。其[每日 AI 资讯](https://jls42.org/fr/news)每天都由本工具翻译，并作为上述测试的基准文档。

## 作者

Julien LE SAUX
邮箱：contact@jls42.org

## 许可证

GNU GENERAL PUBLIC LICENSE Version 3。参见 [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)。

## 免责声明

本程序**不提供任何担保**分发，遵循 GPL v3 第 15 和 16 条的规定：按“原样”提供，不提供适销性或特定用途适用性的担保，作者对因使用本程序而造成的任何损害概不负责。许可证文本优先于本简要说明。

- **发布前请校对。** 保护机制涵盖代码块、行内代码、URL、锚点以及 `--news` 模式下的引用——但不涵盖标题、表格、front matter 或句子的含义。
- **您的文档将被发送至所选的服务商**，遵循其使用条款和数据政策。某些免费模型可能会将您的交互用于训练，而 Antigravity 的条款允许 Google 重复使用这些数据并让人工审阅（包括付费订阅）；本地模型是确保任何数据都不离开您机器的唯一途径。
- **API 调用会产生费用。** 本程序不设费用上限：长文档、失败重试或推理较多的模型会消耗更多费用。
- **所公布的测试结果均为特定日期的观察记录**，而非保证。

文中所提及的产品和公司名称归其各自所有者所有。本项目与其中任何一家均无关联。

**使用 gemini-3.8-flash-medium 从法语翻译成中文的文章。**
