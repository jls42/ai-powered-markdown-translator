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

在保留结构的同时将 Markdown 文件从一种语言翻译为另一种语言：代码块、行内代码、URL、锚点、表格和 front matter。调用模型的十种途径——五种 API、三种无按量计费的订阅、两种路由器——以及各模型实际保留效果的已公布测试基准。

## 概览

- **十种 Provider 途径**：OpenAI、Mistral、Claude、Gemini 和 Grok API；无需按量计费的 ChatGPT (Codex)、Grok 和 Google (Antigravity) 订阅；OpenCode（开源、免费或本地）和 OpenRouter（超过 400 个模型）路由器。
- **杜绝因标记丢失造成的错误**：代码块、行内代码、URL、锚点和引用在调用前均会被替换为标记，并在返回时进行校验。如果丢失任何一个标记，则不会写入该文件。
- **长文档支持**：根据模型的上下文窗口进行分段。
- **`--news` 模式**：保护英文引用，并按语言处理旗帜图标，适用于动态资讯类文章。
- **`--eco` 模式**：使用更快且成本更低的模型。
- 可选的**翻译附注**，可置于顶部、底部或同时置于两处。

## 安装

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 或更高版本。如需从代码仓库安装，请参见[贡献](#贡献)。

## 配置

密钥会从三个位置按优先级从高到低依次读取；后序位置仅补充前序位置中未设置的项。

|     | 位置                                          | 用途                                  |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 环境变量                                      | CI、容器、临时覆盖                    |
| 2   | 当前目录（或父目录）下的 `.env`        | 针对特定项目的密钥                    |
| 3   | `~/.config/aipmt/.env`                                 | 一次性全局配置，对所有项目生效        |

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

支持使用 `GEMINI_API_KEY` 代替 `GOOGLE_API_KEY`。用户配置文件遵循 `XDG_CONFIG_HOME`（仅限绝对路径），在 Windows 下遵循 `%APPDATA%`。如果未提供密钥，该命令会列出这三个位置。

**项目的 `.env` 既不能重定向调用，也不能选择执行的程序。** 它仅用于提供密钥，绝不提供目标地址或可执行程序：任何以 `_BASE_URL`、`_API_BASE`、`_ENDPOINT` 或 `_BIN` 开头的变量（`CODEX_BIN`、`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`）、`GROK_HOME`、代理（`HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY`）、证书存储（`SSL_CERT_FILE`、`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）以及 `XDG_CONFIG_HOME` / `APPDATA` 在其中均会被忽略并发出警告。克隆的仓库绝不能窃取您的密钥，也不能在首次翻译时诱使您运行其自带的程序。该文件的读取也不支持变量插值：`NOM=${OPENAI_API_KEY}` 不会在其中复制密钥。请将这些变量设置在环境变量中或 `~/.config/aipmt/.env` 中。

可选变量：`XAI_BASE_URL`（默认 `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（每次调用秒数，默认 900）、`CODEX_BIN`、`CODEX_TIMEOUT`（默认 600）、`GROK_BIN`、`GROK_HOME`（默认 `~/.grok`）、`GROK_TIMEOUT`（默认 900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（默认 900）、`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（默认 600）、`OPENROUTER_BASE_URL`（需要 `https://`）、`OPENROUTER_TIMEOUT`（默认 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（默认 30）。每个变量均在其对应的 provider 章节中有详细说明。

## 快速上手

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

将 `document.md` 翻译为西班牙语后，将在 `--target_dir` 中生成 `document-es.md`；使用 `--include_model` 时则生成 `document-es-gpt-5.6-terra.md`。扩展名始终会转换为 `.md`（例如 `article.mdx` 会生成 `article-en.md`），除非使用了 `--keep_filename` 保留原始文件名。若未指定 `--force`，已存在的翻译将被跳过。

退出代码：全部成功或跳过时为 `0`；若有文件处理失败则为 `1`（在标准错误输出中列出清单）；配置问题时为 `2`。失败的文件绝不会被写入，即使写入过程本身发生故障也是如此：内容先写入临时文件然后再重命名。只需重新运行即可。

## 如何选择模型

基于两份真实文档进行测试，每个模型均翻译为相同的十四种语言。**数字表示在十四种语言中，翻译成功写入且与源结构完全一致的语言数量。**

| 模型                 | 访问方式                          | 密集资讯文章            | 本 README    | 差异情况及涉及语言数                                                                                  |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ----------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | Google API 密钥                   | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种：多出一个加粗词（ja）                                                              |
| **Gemini 3.7 Flash** | Google 订阅 (Antigravity)         | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种：少了一个加粗词（ko）                                                             |
| **GPT-5.6 Sol**      | ChatGPT 订阅或 OpenAI 密钥        | ✅ 14/14                | ⚠️ 12/14     | 14 种语言中有 2 种：少了一个加粗词（ar、ja）                                                          |
| **GLM-5.2**          | OpenRouter 密钥                   | ✅ 14/14                | ⚠️ 11/14     | 14 种语言中有 3 种：少了一个加粗词（hi、ja、ko）                                                      |
| Claude Sonnet 5      | Anthropic API 密钥                | ⚠️ 11/14                | ⚠️ 12/14     | 资讯文章中有 3 种语言：多出一个代码块（es、de、hi）；本 README 中有 2 种：链接丢失标记（sv）、一个词加粗（zh） |
| Qwen 3.7 Flash       | OpenRouter 密钥                   | ❌ 8/14                 | ⚠️ 10/14     | 资讯文章中有 1 种语言被拒，另有 5 种存在偏差；本 README 中约有四十个词被置于 `code`（ar）     |
| Grok 4.6             | Grok 订阅                         | ❌ 8/14                 | 未评分       | 14 种语言中有 5 种被拒（因行内代码和 URL 未能正确返回）；荷兰语翻译完全偏离                           |
| GPT-OSS 20B          | 本地模型 (Ollama)                 | ❌ 7/14                 | 未重测       | 14 种语言中有 4 种被拒：模型残留法语段落，被保护机制拦截                                              |
| MiMo v2.5 (免费)     | OpenCode Zen（免账户）            | ❌ 11/14                | 未重测       | 1 种语言被拒；波兰语丢失一个章节                                                                      |
| Mistral Large        | Mistral API 密钥                  | ❌ 5/14                 | ❌ 1/14      | **整整丢失一个章节**：资讯文章中有 1 种（hi），本 README 中有 3 种（ar、hi、ko）——且资讯文章中有 3 种语言被拒 |
| DeepSeek V4 Flash    | OpenRouter 密钥                   | ❌ 3/14                 | 未重测       | 14 种语言中有 10 种被拒；每种语言耗时 37 分钟                                                         |

|     | 符号含义                                                                                                                                                              |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 十四种语言全部完成翻译，且与源文件毫无差异                                                                                                                            |
| ⚠️  | 十四种语言全部完成翻译；差异仅限于**标记格式**——如某个词加粗、多出一个 `code`、链接丢失方括号等。没有缺失任何文本、URL、代码块或章节                         |
| ❌  | 至少有一种语言未能成功翻译（文件被拒绝且未写入），**或**已写入的文件中存在内容缺失                                                                                    |

核心要点：

- **被拒绝的翻译不等同于损坏的翻译。** 当返回内容缺少标记时，文件不会被写入，该语言将被计为“被拒绝”。这正是 Grok 在资讯文章中出现的情况：在五种非拉丁字母语言中，仅第一段就丢失了四个行内代码和三个 URL。
- **该安全网并不涵盖标题、表格、front matter 或正文文本。** 如果模型删除了某个章节，本工具仍会直接写入该文件——Mistral 就是这种情况。这些元素无法用标记替换，目前的保护机制也不会对它们进行检查；`scripts/compare_structure.py` 可以在事后检测出丢失的章节。
- **Grok 在本 README 中未予评分**：其 CLI 会话在处理完十二种语言后过期（其中十一种无偏差）。中断的测试不予评分。
- **文档的密集程度比目标语言更关键。** Grok 在常规 README 上表现良好，但在包含大量链接的文章中则会出现偏差，即便是荷兰语也是如此。

日期与文档说明：“本 README”列于 2026 年 9 月 9 日基于本文件的固定版本（785 行、285 个行内代码、89 行表格）进行测试（此后有所修改）——但 Antigravity 行除外，其于 9 月 26 日基于随 1.14.0 发布的较短版本（600 行、257 个行内代码、85 行表格）进行测试。“密集资讯文章”列来自 9 月 4 日至 5 日针对一篇 589 行文章的测试，但 Grok 行除外（于 9 月 9 日在同一资讯的另一版本上重新测试），以及 Antigravity 行（于 9 月 26 日在同一文章上测试）。完整表格、耗时和测试协议请参阅[详细测试数据](#详细评测)。

## 完整选项

| 选项                     | 描述                                                                                                          |
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
| `--use_grok`           | 使用 xAI (Grok) API — 需要 `XAI_API_KEY`                                                                     |
| `--use_codex`           | 使用 ChatGPT 订阅额度的 Codex CLI                                                                             |
| `--use_grok_cli`           | 使用 Grok 订阅额度的 Grok CLI                                                                                 |
| `--use_antigravity`           | 使用 Google AI Pro 或 Ultra 订阅额度的 Antigravity CLI (`agy`)                                       |
| `--use_opencode`           | 使用 OpenCode（开源）连接到 OpenCode 中配置的提供商；需要 `--model provider/modèle`                                      |
| `--use_openrouter`           | 使用 OpenRouter — 需要 `OPENROUTER_API_KEY` 和 `--model fournisseur/modèle`                                                       |
| `--force`           | 强制重新翻译                                                                                                  |
| `--keep_filename`           | 保留原始文件名                                                                                                |
| `--news`           | 新闻模式：保护英文引用，按语言处理旗帜图标                                                                    |
| `--add_translation_note`           | 添加翻译附注                                                                                                  |
| `--note_position`           | 附注位置：`top`、`bottom`（默认）或 `both`                                             |
| `--note_format`           | 附注格式：`legacy`（默认，粗体段落）或 `marker`                                                  |
| `--include_model`          | 在输出文件中包含模型名称                                                                                      |
| `--reasoning_effort`          | GPT-5.x 推理力度：`none`/`low`/`medium`/`high`/`xhigh`               |

这九个 `--use_*` 标志是互斥的：同时组合使用两个标志将被拒绝。

## 提供商

### 通过 API：OpenAI、Mistral、Claude、Gemini、Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` 切换至各个供应商的经济档位。

| 供应商 | 质量优先（默认） | 经济档 (`--eco`) |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol`（亦可通过 `--model` 使用 `terra` 和 `luna`） | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.7-flash-medium`                             | `gemini-3.7-flash-low`    |
| OpenCode    | 必需 `--model provider/modèle`                 | 同前 — `--eco` 无效 |
| OpenRouter  | 必需 `--model fournisseur/modèle`              | 同前 — `--eco` 无效 |

### 使用 ChatGPT 订阅：`--use_codex`

调用官方 Codex CLI：翻译将从 ChatGPT 订阅配额中扣除，无需 API 密钥，亦无按量计费。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 优先在 `CODEX_BIN` 中查找二进制文件，其次是 `PATH`，最后是 `openai-codex-cli-bin` 软件包。从不读取 `~/.codex/auth.json`。
- `OPENAI_API_KEY` 和 `CODEX_API_KEY` 会从子进程环境中移除：即使存在密钥，也绝不会切换到 API。
- 每个片段至少消耗 5 小时窗口内的 1 条“消息”——若验证失败并重试，则消耗 2 条。OpenAI 给出的 Plus 方案预估额度为：`gpt-5.6-luna`（`--eco`）每 5 小时 250–2,000 条消息，`gpt-5.6-sol` 为 10–100 条。
- `--model gpt-5.6-terra` 和 `--model gpt-5.6-luna` 同样走订阅通道。若账户无权访问某个模型，则会返回 400 错误：“model is not supported when using Codex with a ChatGPT account”。
- 比 API 慢，且差距随文档增大而扩大：就本 README 而言，使用 `gpt-5.6-sol` 每种语言的中位数耗时为 6 分 46 秒，而 `gemini-3.7-flash` 仅需 36 秒。
- CI 环境中拒绝执行（定义了 `CI` 或 `GITHUB_ACTIONS`）：订阅通过个人会话文件进行身份验证，该文件不应出现在共享 runner 上。
- 环境变量：`CODEX_BIN`、`CODEX_TIMEOUT`（每片段秒数，默认 600）。

### 使用 Grok 订阅：`--use_grok_cli`

原理相同，基于官方 Grok Build CLI，使用 SuperGrok 或 X Premium+ 订阅。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **隔离强度低于 Codex。** Grok 的操作系统沙盒在许多较新的 Linux 设备上无法应用（AppArmor、容器运行时套接字），且无法应用的配置文件会在无沙盒隔离的情况下静默启动。因此脚本默认不请求任何配置文件，进行提示，并依赖 CLI 的 `--deny` 规则（包括全捕获规则 `*`）——这是唯一一层会在无法生效时拒绝启动、而不是静默撤除保护的机制。`GROK_TRANSLATE_SANDBOX=read-only` 强制要求操作系统沙盒，若机器无法满足则启动失败。
- 配额为按周计算，与 Chat、Imagine 和 Voice 共享，且没有任何命令可以查询配额：批量运行可能会在没有任何提示的情况下消耗对话额度。
- 环境变量：`GROK_BIN`、`GROK_HOME`（CLI 目录，默认 `~/.grok`）、`GROK_TIMEOUT`（默认 900）、`GROK_TRANSLATE_SANDBOX`。

### 使用 Google 订阅：`--use_antigravity`

原理相同，使用 Antigravity 官方 CLI `agy`：对于购买了 Google AI Pro 或 Ultra 的用户，翻译将从订阅配额中扣除，而非按 Token 计费。这是使用该配额的唯一途径：Gemini CLI 自 2026 年 6 月 18 日起不再支持此类账户（[公告](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)），且 Antigravity SDK 仅接受 API 密钥或 Google Cloud 项目。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **未保留任何付费通道。** agy 从您的环境中仅接收一份受限的环境变量白名单——`PATH`、语言与时区、终端、身份、代理与证书、会话总线——而不包含任何密钥：其多个变量可在不显示任何提示的情况下切换调用方式（实测：其中一个会将文档发送至第三方网关，另一个则发送至计费的 Google Cloud 项目），而黑名单机制在每次审查时都会有遗漏。在处理任何片段之前，不消耗任何配额的 `agy -p /config` 必须显示付费 AI 额度已禁用，且无 API 密钥和 Google Cloud 项目——缺少配置即视为拒绝——否则不进行任何翻译；随后每次调用的日志必须证实使用的是订阅通道（`authMethod=consumer`），否则响应将被拒绝。
- **隔离保护。** 每次调用都在一个独立的、一次性私有主目录中运行，并配备一个无工具的翻译 agent：您的 agy 设置、规则、插件、MCP 服务器及 hook 均不会传入，不会在历史记录中添加任何内容，且登录凭据保留在密钥环中（aipmt 绝不读取）。若未找到指定 agent，agy 会静默回退至其编码 agent 及其工具：因此日志中必须有整行明确确认使用了正确的 agent（文档中引用该消息不算数），否则予以拒绝。
- **支持平台**：Linux（需在具有密钥环的会话中：D-Bus 会话总线、Secret Service）；支持 macOS（未做测试衡量）。在 Windows 下拒绝运行（agy 无法读取隔离每次调用的变量），在无会话总线的 Linux 下（SSH 会话、容器、服务器）亦拒绝运行：此时 agy 会将其令牌存放在 `~/.gemini` 的文件中，而隔离机制会将其屏蔽。拒绝提示会在启动前明确给出原因，无需等待一分钟的登录验证码超时。
- **模型**：即 `agy models` 中的模型。Gemini 模型的思考量（effort）体现在其名称中（`gemini-3.7-flash-low`…）：无后缀的名称将在调用前被拒绝，且 `--reasoning_effort` 无效。这两个默认值已通过涵盖 14 种语言的测试轮次确定（参见[详细评测](#详细评测)）。Claude 与 GPT-OSS 拥有独立的配额，且配额小得多：实测每次调用约消耗 5 小时窗口的 1%，而 Flash 仅约 0.05%。
- **配额**：按组划分，设有 5 小时窗口和每周窗口，按 Token 消耗成本等比扣除。根据作者账户上 32 次翻译测试的实测数据：使用 `gemini-3.7-flash-medium` 翻译一个 40,000 字符的 README 约消耗 5 小时窗口的半个百分点（0.5%）；每周上限则取决于订阅级别。重试遵循 agy 声明为可重试的情况；否则，耗尽的窗口绝不会重试：所有文件均会失败，直到 `/usage` 显示的重置时间到达。
- **速度慢于 API**：在密集的评测长文上，通过订阅使用 Gemini 3.7 Flash 每种语言的中位数耗时为 3 分 14 秒，而通过 API 仅需 1 分 18 秒。
- **中断**：Ctrl-C 或关闭终端会随命令一同停止 agy，避免其继续消耗您的配额；Codex、Grok CLI 和 OpenCode 亦同。在 `nohup` 下，翻译将继续进行。
- CI 环境中拒绝执行（定义了 `CI` 或 `GITHUB_ACTIONS`）：登录状态保存在个人密钥环中。在 runner 上，请配合 `GOOGLE_API_KEY` 使用 `--use_gemini`。
- 环境变量：`AGY_BIN`（其次为 `PATH`，然后是 `~/.local/bin/agy`）、`AGY_TIMEOUT`（每片段秒数，含启动时间，默认 900）。

**使用条款：责任由您的账户承担。** [Antigravity 服务条款](https://antigravity.google/terms)（第 6 节）及其 [常见问题解答](https://antigravity.google/docs/faq/) 禁止通过第三方软件利用 Antigravity 登录状态访问该服务（其中点名了 Claude Code、OpenClaw 和 OpenCode），违者可能会被封禁账户。aipmt 既不读取也不复用令牌：它仅在 Google 为脚本和 CI 所记录的 [无头模式 (headless mode)](https://antigravity.google/docs/cli/headless/) 下运行官方二进制文件。Google 员工曾表示在本地脚本中运行 `agy -p` 进行个人工作属于“标准做法”（[官方论坛，2026 年 9 月 25 日，非约束性答复](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）；但目前尚无明确条款定性本工具这类分发式工具。

**仅限公开文档。** 根据相同条款的第 5 节，交互内容（提示词、回复、元数据）可能用于改进 Google 产品及机器学习，并可能由人工审核，即使付费订阅也不例外。退出机制需通过效果未明确记录的 `enableTelemetry` 设置，而 aipmt 不会设置此项；您自身的 agy 设置也不会带入隔离环境中。切勿在此通道中处理任何涉密内容。

### 接入自选供应商：`--use_opencode`

[OpenCode](https://opencode.ai) 是一个开源（MIT）代码 agent，可路由至其内部配置的供应商：API 密钥、订阅、OpenCode Zen 网关（免账户的免费模型）或本地模型。此处对 Zen 和 Ollama 这两条路径进行了端到端评测。

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

`--model` 是必需的：若无此参数，OpenCode 将回退至交互内容可能用于模型训练的免费模型，本工具不会替您做出此项选择。

每次调用的隔离保护：

- 内联配置优先级高于您的配置，定义了一个禁用所有工具（`permission: { "*": "deny" }`）的 `aipmt` agent，已关闭会话共享，`--pure`，从不使用 `--auto`；
- 一次性空工作目录，设置了 `OPENCODE_DISABLE_PROJECT_CONFIG` 与 `OPENCODE_DISABLE_CLAUDE_CODE`——若不设置，OpenCode 会将当前目录的 `AGENTS.md` 和 `~/.claude/CLAUDE.md` 注入提示词中。全局 `~/.config/opencode/AGENTS.md` 仍会被注入，OpenCode 不支持将其排除；
- 输出契约：返回码 0、无 `error` 事件、无工具调用、最后一步为 `stop`、文本非空且确实加载了 `aipmt` agent——未知的 `--agent` 不会使 OpenCode 报错，而是会静默回退到编码 agent；
- 除 OpenCode 自身的密钥 `OPENCODE_API_KEY` 外，不传递任何 `aipmt` 密钥。供应商应在 OpenCode 内部配置，而非在 `aipmt` 的 `.env` 中配置。

注意事项：

- Zen 的免费模型经常变动，限制未公开，且交互内容可能用于模型训练：适用于公开文档，不适用于私有内容。
- 本地模型必须提供至少 16k Token 的上下文，因为片段最长可达 16,000 字符。Ollama 通常仅配置 4,096：请通过带有 `PARAMETER num_ctx 32768` 的 `Modelfile` 进行配置。
- `--eco` 无效；`--reasoning_effort` 会作为 OpenCode 的 `--variant` 原样传递。
- OpenCode 会将每次会话记录在 `~/.local/share/opencode/` 中。
- 环境变量：`OPENCODE_BIN`（其次为 `PATH`, 然后是 `~/.opencode/bin/opencode`）、`OPENCODE_TIMEOUT`（每片段秒数，默认 600）。`OPENCODE_CONFIG` 会原样传递给 OpenCode。

通过 Ollama 使用本地模型的示例（位于 `~/.config/opencode/opencode.json`）：

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

`reasoningEffort: "none"` 关闭了 Ollama 默认在这些模型上启用的思考过程（该设置无法通过 Modelfile 禁用）。在一句 6 个单词的句子上实测：未加该选项时消耗 919 个思考 Token 和 68 秒，加上后仅消耗 9 个 Token。

### 接入 400+ 款模型：`--use_openrouter`

OpenRouter 是一个按量计费的路由服务，基于统一余额访问第三方托管的模型——包括此处其他供应商均未提供的中国开源模型。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` 是必需的。在产生任何计费前执行的预检（preflight）会处理路由的两个特性：

- **同一模型由数十家上限各异的托管商提供**——以 `z-ai/glm-5.3-flash` 为例，23 家托管商中有一家的输出上限仅为 2,048 Token。预检会读取 `/api/v1/models/{modèle}/endpoints`，排除输出低于 8,000 Token 或状态降级的托管商，并通过 `allow_fallbacks: false` 固定其他托管商。
- **推理按输出费率计费**——在 `z-ai/glm-5.2` 回复“OK”时，产生 107 个 Token，而原本只需 2 个。默认情况下已关闭推理；对于强制开启推理的模型，则传入其允许的最低思考量（effort），因为目录默认值可能会在翻译完成前耗尽输出限额。`--reasoning_effort` 仍具最高优先级。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- 上下文窗口大小取自目录。上下文低于 16,400 Token 的模型会在调用前被拒绝：提示词与片段占 8,400，输出至少需要 8,000。
- 若标识符（slug）不在目录中、目录无法访问，或没有满足上限要求的托管商，命令将终止执行。
- `finish_reason=length` 且输出为空表示预算被推理消耗殆尽，而非被截断：错误消息对此作了区分。
- `--eco` 无效。
- 环境变量：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>）、`OPENROUTER_BASE_URL`（默认 `https://openrouter.ai/api/v1`，需为 `https://`）、`OPENROUTER_TIMEOUT`（默认 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（默认 30）。

### 翻译说明

`--add_translation_note` 会添加一条说明，位置可选 `bottom`（默认）、`top`（位于 front matter 之后）或 `both`（`--note_position`），格式可选 `legacy`（粗体段落，默认）或 `marker`（`--note_format`）。`marker` 格式是一段不可见的 Markdown 引用定义 `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`，后跟一段粗体引用：在 GitHub 上正常可读，且可在构建时供 remark 插件利用。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 详细评测

所有评测数据均通过 `aipmt` 实际执行翻译得出，目标语言涵盖 14 种：en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi。**已写入**统计通过守卫检查的文件数；**无差异**统计 `scripts/compare_structure.py` 未发现任何差异的文件数——即章节数、副标题数、链接数、不同 URL 数、代码块数、行内代码数、表格行数、引用块数及粗体字数均完全一致。

“无差异”意为“未检测到差异”，并不等同于“完全一致”：比较工具仅统计元素数量而不读取其内容。它既不会报告被删除的 4 级标题，也不会报告被替换的行内代码文本或被互换的标志，更不会对语言质量进行评估。

### 密集资讯文章，`--news` 模式

[jls42.org 的 AI 资讯](https://jls42.org/fr/news) 中的一期：
589 行，140 个链接，21 个章节，3 处受保护的英文引用。2026 年 9 月 4 日至 5 日的测试。

| 模型                                            | 接入方式           | 已写入  | 无偏差       | 中位数/语言    |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14** | 1 分 18 秒     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google 订阅        | 14/14   | ✅ **14/14** | 3 分 14 秒     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT 订阅       | 14/14   | ✅ **14/14** | 11 分 28 秒    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 分 37 秒     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 分 23 秒    |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 分 31 秒     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 分 27 秒     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 分 09 秒    |
| `ollama/gpt-oss-20b-32k`                        | 本地               | 10/14   | ❌ 7/14      | 12 分 39 秒    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14      | 5 分 32 秒     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 分 27 秒    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok 订阅          | 1/14    | ❌ 1/14      | 23 分 11 秒    |

9 月 9 日在同一资讯的另一期（356 行）上重新测量了 Grok：14 种语言中写入 9 种，8 种无偏差。正是这个数字显示在主表中。三场中断的测试未予记录：`qwen3.5-27b`（9 种语言）和 `kimi-k2.6`（4 种）因额度不足中断，`z-ai/glm-5.3-flash` 的两次失败源于提供商后来修复的推理设置。OpenRouter 相关行是在路由器的默认设置下测量的，早于 `--use_openrouter`；使用随附提供商重新测量的 `z-ai/glm-5.2` 同样达到了 14/14。9 月 10 日使用当前比较工具重新计算了数据：与首次发布相比，`qwen3.8-flash` 和 `qwen3.7-flash` 各增加了一种语言，其余保持不变。

`--use_antigravity` 行于 9 月 26 日在同一篇文章上进行了测试，4 个并发翻译。在英语翻译中，该模型自行移除了引用下方的三行法语翻译，没有捏造标记，并且英文引用保持完好：兜底清理机制无需执行任何操作。在 `--eco`（`gemini-3.7-flash-low`）中，仅针对四种语言（en、ja、ar、hi）：4/4 写入，全部无偏差，中位数时间 1 分 52 秒。

### 本项目的 README，标准 Markdown

2026 年 9 月 9 日冻结的版本：785 行，285 处行内代码，40 处代码块闭合，89 行表格。4 个并发翻译。

| 模型                                            | 已写入  | 无偏差     | 中位数/语言    | 差异内容                                                                 |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 秒          | 一个加粗词 (ja)                                                          |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 分 22 秒     | 一个加粗词 (ko)                                                          |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 分 56 秒     | 一个链接 (sv)，一个加粗词 (zh)                                           |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 分 46 秒     | 一个加粗词 (ar, ja)                                                      |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 分 34 秒     | 一个加粗词 (hi, ja, ko)                                                  |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 分 17 秒     | 阿拉伯语中增加了 40 处行内代码；加粗 (hi, ja, ko)                        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 分 44 秒     | 丢失一个章节 (ar, hi, ko)；增加了代码块 (ja, ko, ro, zh)                 |

两场中断的测试未予记录：Grok 在完成 12 种语言后 CLI 会话过期（11 种无偏差），以及 `qwen3.8-flash` 在完成 2 种后收到其托管服务商的 HTTP 429 错误。`opencode/mimo-v2.5-free` 和 `ollama/gpt-oss-20b-32k` 未在此版本上重新测量；在 9 月 4 日至 5 日少 277 行的版本上，它们各自在 14 种翻译中写入了 9 种，分别有 7 种和 1 种无偏差。

`--use_antigravity` 行未在冻结版本上测量，而是在 9 月 26 日随 1.14.0 发布的版本上测量的：600 行，257 处行内代码，30 处代码块闭合，85 行表格。由于短了 185 行，它无法与其他行直接进行逐项对比。

### 四个知名项目的 README

FastAPI、Ollama、tldr-pages 和 Vue.js，原样取自 GitHub —— 比前两个文档更容易。该测试针对表现吃力的模型；Gemini 在此用作对照参考。

| 模型                       | 范围                       | 已写入  | 无偏差       |
| -------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 个项目 × 14 种语言       | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 个项目 × 14 种语言       | 55/56   | ❌ 47/56     |
| `grok-4.6`（订阅）    | 4 个项目 × ar, hi, ja, zh  | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 个项目 × ar, hi, ja, zh  | 15/16   | ❌ 9/16      |

### 这些测试数据不是什么

- **不是详尽的排名**：仅 OpenRouter 就提供 400 多个模型，这里仅测试了约 15 个。
- **仅为参考耗时**：根据测试批次不同，并发翻译数为 3 到 6 个，且供应商的吞吐速率在一天中会有所波动。
- **具有时效性的观察结果**：同名模型可能会发生变动，且您的文档与我们的文档并不相同。

如需在您自己的文档（文件的冻结副本）上重新进行测量：

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

这两行都是必需的：如果没有 `pip install -e .`，`python -m aipmt` 将返回 `No module named aipmt`。

质量工具链（可选但推荐）：

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

仓库中的 28 个翻译（README 和 CHANGELOG，14 种语言）可通过 `./regen_translations.sh --force` 重新生成 —— 默认使用 ChatGPT 订阅上的 Codex 和 `gpt-5.6-sol`，4 个并发。`REGEN_PROVIDER` 和 `REGEN_MODEL` 可更改路径：`antigravity` 仍然使用订阅（Google 订阅），无需额外授权即可通过；按量计费的 API（`openai`、`gemini`、`grok`、`openrouter`）若无 `REGEN_ALLOW_PAID_API=1` 将被拒绝；`REGEN_JOB_TIMEOUT` 限制每个任务的时长（默认 600 秒，Codex 和 Antigravity 为 1800 秒）。工具链的详细信息参见 `CLAUDE.md`。

## 使用此脚本的项目

- **[jls42.org](https://jls42.org)** —— 以 15 种语言发布的个人博客。其[每日 AI 资讯](https://jls42.org/fr/news)每天都由此工具翻译，并作为上述测试的基准参考文档。

## 作者

Julien LE SAUX
邮箱：contact@jls42.org

## 许可证

GNU 通用公共许可证第 3 版（GNU GENERAL PUBLIC LICENSE Version 3）。参见 [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)。

## 免责声明

本程序**不作任何保证**分发，依据 GPL v3 第 15 和 16 条的条款：按“原样”提供，不作任何适销性或特定用途适用性的保证，其作者不对因使用本程序而造成的任何损害承担责任。许可证全文优先于本摘要。

- **发布前请务必校对。** 保护机制涵盖代码块、行内代码、URL、锚点以及 `--news` 模式下的引用 —— 但不涵盖标题、表格、front matter 或句子的含义。
- **您的文档会被发送至所选提供商**，遵循其使用条款和数据政策。某些免费模型可能会将您的交互数据重用于模型训练，而 Antigravity 的条款允许 Google 重用这些数据并进行人工审核（即使是付费订阅亦然）；本地模型是确保没有任何数据离开您本机的唯一途径。
- **API 调用将向您收取费用。** 本程序不设费用上限：较长的文档、失败重试或推理较多的模型都会产生更高的成本。
- **发布的测试数据仅为特定时期的观察结果**，并非绝对保证。

文中提及的产品和公司名称均属于其各自所有者。本项目与其中任何一家均无关联。

**使用 gemini-3.7-flash-medium 从法语翻译至中文的文章。**
