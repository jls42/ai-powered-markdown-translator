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

在语言之间翻译 Markdown 文件，同时保持结构完整：代码块、行内代码、URL、锚点、表格和 front matter。提供 11 种模型调用方式——5 种 API、4 种无按量计费的订阅服务、2 种路由器——以及关于各模型实际保留效果的公开发布测试结果。

## 概览

- **11 种 Provider 途径**：OpenAI、Mistral、Claude、Gemini 和 Grok API；无按量计费的 ChatGPT (Codex)、Grok、Google (Antigravity) 和 Claude (Claude Code) 订阅；OpenCode 路由器（开源、免费或本地）以及 OpenRouter（超过 400 种模型）。
- **绝不会因标记丢失而产生错误**：代码块、行内代码、URL、锚点和引用在调用前都会被替换为占位标记，并在返回时进行校验。如果缺少任何一个标记，则不会写入文件。
- **长篇文档**：根据模型的上下文窗口进行切分。
- **`--news` 模式**：保护英文引用并按语言处理国旗图标，适用于资讯追踪文章。
- **`--eco` 模式**：使用更快且成本更低的模型。
- **可选的翻译注记**：可置于顶部、底部或同时置于两端。

## 安装

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 或更高版本。如需从代码仓库安装，请参阅[贡献](#贡献)。

## 配置

密钥按优先级从高到低在三个位置读取；后级仅补充前级未设置的项。

|     | 读取位置                                      | 适用场景                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 环境变量                                      | CI、容器、临时覆盖                    |
| 2   | 当前目录（或父目录）中的 `.env`        | 针对特定项目的密钥                    |
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

可以使用 `GEMINI_API_KEY` 代替 `GOOGLE_API_KEY`。用户配置文件遵循 `XDG_CONFIG_HOME`（仅限绝对路径），在 Windows 下遵循 `%APPDATA%`。如果未找到密钥，该命令会列出这三个位置。

**项目的 `.env` 既不能重定向请求，也不能选择执行的程序。** 它仅用于提供密钥，绝不提供目标地址或可执行文件：任何形如 `_BASE_URL`、`_API_BASE`、`_ENDPOINT` 或 `_BIN`（`CODEX_BIN`、`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`）、`GROK_HOME`、代理（`HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY`）、证书存储（`SSL_CERT_FILE`、`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）以及 `XDG_CONFIG_HOME` / `APPDATA` 的变量在其中都会被忽略，并发出警告。克隆的代码仓库绝不能窃取您的密钥，也不能在首次翻译时诱使您运行其自带的程序。该文件读取时也不会进行变量插值：`NOM=${OPENAI_API_KEY}` 不会在其中复制密钥。请将这些变量设置在环境变量中或 `~/.config/aipmt/.env` 中。

可选变量：`XAI_BASE_URL`（默认 `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（每次调用的秒数，默认 900）、`CODEX_BIN`、`CODEX_TIMEOUT`（默认 600）、`GROK_BIN`、`GROK_HOME`（默认 `~/.grok`）、`GROK_TIMEOUT`（默认 900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（默认 900）、`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（默认 600）、`OPENROUTER_BASE_URL`（要求 `https://`）、`OPENROUTER_TIMEOUT`（默认 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（默认 30）。各变量的详细信息请参阅其对应 provider 的章节。

## 快速入门

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

将 `document.md` 翻译为西班牙语会在 `--target_dir` 中生成 `document-es.md`；使用 `--include_model` 则生成 `document-es-gpt-5.6-terra.md`。扩展名始终变为 `.md`——`article.mdx` 会生成 `article-en.md`——除非使用 `--keep_filename`，它会保留原始文件名。若未使用 `--force`，已存在的翻译将被跳过。

退出代码：若全部成功或被跳过则为 `0`；若有文件失败则为 `1`（失败列表输出至标准错误）；若配置有问题则为 `2`。失败的文件绝不会被写入，即使写入过程本身出错也是如此：内容先写入临时文件然后再重命名。只需重新运行即可。

## 如何选择模型

基于两份真实文档进行测试，每个模型均翻译为相同的 14 种语言。**其中的数字表示 14 种语言中成功写入翻译且与源文档结构完全无差异的语言数量。**

| 模型                 | 获取/接入方式                     | 密集的资讯追踪文章      | 本 README    | 差异内容及涉及的语言数量                                                                                                            |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.8 Flash** | Google 订阅 (Antigravity)         | ✅ 14/14                | ✅ 14/14     | 无差异，两份文档均无差异                                                                                                            |
| **Gemini 3.7 Flash** | Google API 密钥                   | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种：多出一个粗体词 (ja)                                                                                             |
| **Gemini 3.7 Flash** | Google 订阅 (Antigravity)         | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种：少了一个粗体词 (ko)                                                                                             |
| **GPT-5.6 Sol**      | ChatGPT 订阅或 OpenAI 密钥        | ✅ 14/14                | ⚠️ 12/14     | 14 种语言中有 2 种：少了一个粗体词 (ar, ja)                                                                                         |
| **GLM-5.2**          | OpenRouter 密钥                   | ✅ 14/14                | ⚠️ 11/14     | 14 种语言中有 3 种：少了一个粗体词 (hi, ja, ko)                                                                                     |
| Claude Sonnet 5      | Claude 订阅 (Claude Code)         | ⚠️ 13/14                | ⚠️ 13/14     | 资讯文章中有 1/14 种：多出一个粗体词 (zh)；本 README 中有 1 种：表格行与上一行粘连，在显示时被隐藏 (ar)                             |
| Claude Haiku 4.5     | Claude 订阅 (Claude Code)         | ⚠️ 11/14                | ✅ 14/14     | 资讯文章中有 3 种：某个节标题变成了 1 级标题 (en, pl, ro)；在本 README 中对比工具未见异常，但内部链接被重复成了英文                |
| Claude Sonnet 5      | Anthropic API 密钥                | ⚠️ 11/14                | ⚠️ 12/14     | 资讯文章中有 3 种：多出一个代码块 (es, de, hi)；本 README 中有 2 种：链接丢失了标记符号 (sv)，一个粗体词 (zh)                       |
| Qwen 3.7 Flash       | OpenRouter 密钥                   | ❌ 8/14                 | ⚠️ 10/14     | 资讯文章中有 1 种被拒绝，另有 5 种存在偏差；本 README 中约有 40 个词被标记为 `code` (ar)                                    |
| Grok 4.6             | Grok 订阅                         | ❌ 8/14                 | 未评测       | 14 种语言中有 5 种被拒绝，因未还原行内代码和 URL；荷兰语整体存在偏差                                                                |
| GPT-OSS 20B          | 本地模型 (Ollama)                 | ❌ 7/14                 | 未重新测试   | 14 种语言中有 4 种被拒绝：模型在其中遗留了法语句子，被校验机制拦截                                                                  |
| MiMo v2.5（免费）    | OpenCode Zen，无需账户            | ❌ 11/14                | 未重新测试   | 1 种语言被拒绝；波兰语丢失了一个章节                                                                                                |
| Mistral Large        | Mistral API 密钥                  | ❌ 5/14                 | ❌ 1/14      | **整节内容丢失**：资讯文章中有 1 种 (hi)，本 README 中有 3 种 (ar, hi, ko)——且资讯文章中有 3 种被拒绝                               |
| DeepSeek V4 Flash    | OpenRouter 密钥                   | ❌ 3/14                 | 未重新测试   | 14 种语言中有 10 种被拒绝；每种语言耗时 37 分钟                                                                                     |
| Claude Opus 5.5      | Claude 订阅 (Claude Code)         | ❌ 0/14                 | ✅ 14/14     | 资讯文章由于一段生物学快讯触发 Opus 安全护栏而在 14 种语言中全部被拒绝；本 README 完全无异常                                        |

|     | 符号含义                                                                                                                              |
| --- | ------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14 种语言均已翻译，且与源文档完全无差异                                                                                               |
| ⚠️  | 14 种语言均已翻译；差异仅限于**标记格式**——如一个粗体词、一个 `code`、一个链接丢失括号。没有任何文本、URL、代码块或章节缺失 |
| ❌  | 至少有一种语言无法完成翻译——文件被拒绝，未写入——**或者**已写入的文件中存在内容缺失                                                    |

核心结论：

- **被拒绝的翻译不等同于损坏的翻译。** 当返回内容缺少标记时，文件不会被写入，该语言会被计为被拒绝。这正是 Grok 在资讯文章中遇到的情况：在 5 种非拉丁语系中，仅第一个分段就丢失了 4 处行内代码和 3 个 URL。
- **模型可能仅仅因为一句话就拒绝整篇文档。** Opus 5.5 翻译本 README 时毫无偏差，但在资讯追踪文章中却全军覆没：它的安全护栏因一条生物学简讯而中断了响应。文件未被写入，且 aipmt 会给出原因。
- **该安全网并不覆盖标题、表格、front matter 或正文文本。** 如果模型删除了某个章节并返回文件，工具仍会照常写入——Mistral 就是这种情况。这些元素无法用占位标记替换，当前的安全防护也无法校验它们；`scripts/compare_structure.py` 可以检测到丢失的章节，但属于事后检测。
- **Grok 在本 README 中未给出评分**：它的 CLI 会话在完成 12 种语言后过期（其中 11 种无偏差）。中断的测试不予评分。
- **文档的密集程度比语言种类更关键。** Grok 在普通的 README 上表现稳定，但在包含大量链接的文章中就会崩溃，即使是荷兰语也是如此。

日期与文档说明：“本 README”列测试于 2026 年 9 月 9 日，测试对象为该文件的一个固定版本（785 行、285 处行内代码、89 行表格），此后经过修改——但 Antigravity 和 Claude Code 行除外，它们于 9 月 26 日在随 1.14.0 发布的较短版本（600 行、257 处行内代码、85 行表格）上进行了测试。“密集的资讯追踪文章”列源自 9 月 4 日至 5 日对一篇 589 行文章的测试，但 Grok 行除外（于 9 月 9 日在同类资讯文章的另一期上重新测试），以及 Antigravity 和 Claude Code 行（于 9 月 26 日在同一篇文章上测试）。完整表格、耗时和测试协议请参阅[详细评测数据](#详细测量数据)。

## 所有选项

| 选项                     | 描述                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | 要翻译的单个 Markdown 文件（`--source_dir` 的替代项）                                                         |
| `--source_dir`           | 包含 Markdown 文件的源目录（默认：`content/posts`）                                                            |
| `--target_dir`           | 已翻译文件的输出目录（默认：`traductions_en`）                                                                 |
| `--source_lang`           | 源语言（默认：`fr`）                                                                                |
| `--target_lang`           | 目标语言（默认：`en`）                                                                              |
| `--model`           | 要使用的特定模型                                                                                              |
| `--eco`           | 使用经济型模型                                                                                                |
| `--use_mistral`           | 使用 Mistral AI API                                                                                           |
| `--use_claude`           | 使用 Claude API                                                                                               |
| `--use_gemini`           | 使用 Gemini API                                                                                               |
| `--use_grok`           | 使用 xAI (Grok) API — 需要 `XAI_API_KEY`                                                                     |
| `--use_codex`           | 在 ChatGPT 订阅配额下使用 Codex CLI                                                                           |
| `--use_grok_cli`           | 在 Grok 订阅配额下使用 Grok CLI                                                                               |
| `--use_antigravity`           | 在 Google AI Pro 或 Ultra 订阅配额下使用 Antigravity CLI（`agy`）                                    |
| `--use_claude_code`           | 在 Claude Pro 或 Max 订阅配额下使用 Claude Code CLI（`claude -p`）                                         |
| `--use_opencode`           | 使用 OpenCode（开源）连接到 OpenCode 中配置的提供商；需要 `--model provider/modèle`                                      |
| `--use_openrouter`           | 使用 OpenRouter — 需要 `OPENROUTER_API_KEY` 和 `--model fournisseur/modèle`                                                       |
| `--force`           | 强制重新翻译                                                                                                  |
| `--keep_filename`           | 保留原始文件名                                                                                                |
| `--news`           | 新闻模式：保护英文引用，按语言处理标志                                                                        |
| `--add_translation_note`           | 添加翻译说明                                                                                                  |
| `--note_position`           | 说明位置：`top`、`bottom`（默认）或 `both`                                             |
| `--note_format`           | 说明格式：`legacy`（默认，粗体段落）或 `marker`                                                 |
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

`--eco` 可切换至各提供商的经济档次。

| 提供商      | 质量（默认）                                          | 经济型 (`--eco`)          |
| ----------- | ----------------------------------------------------- | --------------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`                   |
| Claude      | `claude-sonnet-5`                                       | `claude-haiku-4-5`                   |
| Mistral     | `mistral-large-latest`                                       | `mistral-small-latest`                   |
| Gemini      | `gemini-3.7-flash`                                       | `gemini-3.1-flash-lite`                   |
| Codex       | `gpt-5.6-sol`（亦可通过 `--model` 使用 `terra` 和 `luna`） | `gpt-5.6-luna`                   |
| Grok API    | `grok-4.6`                                       | `grok-4.3`                   |
| Grok CLI    | `grok-4.6`                                       | `grok-4.5`                   |
| Antigravity | `gemini-3.8-flash-medium`                                       | `gemini-3.7-flash-low`                   |
| Claude Code | `sonnet`，思考力度 `low`             | 同上 — `--eco` 无效       |
| OpenCode    | 必需 `--model provider/modèle`                                  | 同上 — `--eco` 无效       |
| OpenRouter  | 必需 `--model fournisseur/modèle`                                  | 同上 — `--eco` 无效       |

### 使用 ChatGPT 订阅：`--use_codex`

驱动官方 Codex CLI：翻译将计入 ChatGPT 订阅配额，无需 API 密钥或按用量计费。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 二进制文件首先在 `CODEX_BIN` 中查找，然后是 `PATH`，最后是 `openai-codex-cli-bin` 软件包。绝不会读取 `~/.codex/auth.json`。
- `OPENAI_API_KEY` 和 `CODEX_API_KEY` 会从子进程的环境中移除：即使存在密钥也绝不会切换到 API。
- 每个分段至少消耗 5 小时窗口内的 1 条“消息” — 如果验证失败并重试，则消耗 2 条。OpenAI 公布的预估值为：Plus 方案下 `gpt-5.6-luna`（`--eco`）为 250–2,000 条消息/5 小时，`gpt-5.6-sol` 为 10–100 条。
- `--model gpt-5.6-terra` 和 `--model gpt-5.6-luna` 也使用订阅。如果账户无权使用某个模型，将返回 400“model is not supported when using Codex with a ChatGPT account”。
- 比 API 慢，且差距随着文档增大而拉大：在此 README 上，使用 `gpt-5.6-sol` 时每种语言的中位数耗时为 6 分 46 秒，而 `gemini-3.7-flash` 仅需 36 秒。
- 在 CI 中被拒绝（定义了 `CI` 或 `GITHUB_ACTIONS`）：订阅通过个人会话文件进行身份验证，该文件不应出现在共享 runner 上。
- 环境变量：`CODEX_BIN`、`CODEX_TIMEOUT`（每个分段的秒数，默认 600）。

### 使用 Grok 订阅：`--use_grok_cli`

官方 Grok Build CLI 也是同样原理，基于 SuperGrok 或 X Premium+ 订阅。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **隔离性弱于 Codex。** Grok 的操作系统沙箱在许多较新的 Linux 设备上无法生效（AppArmor、容器运行时套接字），而无法应用的配置集会在静默状态下以未隔离方式启动。因此脚本默认不请求任何配置集，并对此作出提示，转而依赖 CLI 的 `--deny` 规则，其中包括通配规则 `*` — 这是唯一一层宁可拒绝启动也不会悄悄移除保护的防线。`GROK_TRANSLATE_SANDBOX=read-only` 强制要求操作系统沙箱，若机器无法满足则启动失败。
- 配额为每周计算，与 Chat、Imagine 和 Voice 共享，且没有任何命令可以读取该配额：批量任务可能会在没有任何提醒的情况下消耗对话用量。
- 环境变量：`GROK_BIN`、`GROK_HOME`（CLI 目录，默认 `~/.grok`）、`GROK_TIMEOUT`（默认 900）、`GROK_TRANSLATE_SANDBOX`。

### 使用 Google 订阅：`--use_antigravity`

Antigravity 的官方 CLI `agy` 也是同样原理：对于购买了 Google AI Pro 或 Ultra 的用户，翻译将计入订阅配额，而不是按 token 计费。这是使用该配额的唯一途径：Gemini CLI 自 2026 年 6 月 18 日起不再向这些账户提供服务（[公告](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)），而 Antigravity SDK 仅接受 API 密钥或 Google Cloud 项目。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **不保留任何付费途径。** agy 从您的环境中仅接收一份严格受限的变量白名单 — `PATH`、语言和时区、终端、身份、代理和证书、会话总线 — 且不包含任何密钥：其多个变量会在没有任何提示的情况下使调用产生变动（经实测：其中一个会将文档发送至第三方网关，另一个会发送至计费的 Google Cloud 项目），而黑名单机制每次复查都会发现遗漏。在处理任何分段之前，不消耗任何配额的 `agy -p /config` 必须显示付费 AI 积分已禁用，且没有 API 密钥或 Google Cloud 项目 — 缺少相关设置即视为拒绝 — 否则不会翻译任何内容；随后每次调用的日志都必须证明属于订阅（`authMethod=consumer`），否则响应将被拒绝。
- **隔离。** 每次调用都在一个私有的、一次性的个人目录中运行，并使用无工具的翻译智能体：您的 agy 设置、规则、插件、MCP 服务器和钩子均不会进入其中，任何内容都不会添加到您的历史记录中，登录凭据保留在密钥环中，aipmt 绝不会读取它。如果找不到智能体，agy 会在静默状态下回退到其编码智能体和工具：日志中必须有整行内容确认使用了正确的智能体 — 引用该消息的文档不能作为替代 — 否则将被拒绝。
- **平台**：Linux，需在拥有密钥环的会话中运行（D-Bus 会话总线，Secret Service）；支持 macOS，但尚未在此平台上进行实测。在 Windows 上被拒绝，因为 agy 在该系统上不读取隔离每次调用的变量；在没有会话总线的 Linux（SSH 会话、容器、服务器）上也被拒绝：agy 在这些环境下会将令牌保存在 `~/.gemini` 文件中，而隔离机制会将其隐藏。拒绝判定会在启动前给出并附带原因，而不是等待一分钟连接码。
- **模型**：`agy models` 中的模型。Gemini 在其名称中包含思考力度（`gemini-3.8-flash-medium`……）：没有后缀的名称在调用前会被拒绝，且 `--reasoning_effort` 无效。默认使用 `gemini-3.8-flash-medium`，`--eco` 下使用 `gemini-3.7-flash-low`；确定这些配置的测试批次在[详细实测](#详细测量数据)中进行了描述。Claude 和 GPT-OSS 拥有各自独立且小得多的配额：经测算每次调用约占 5 小时窗口的 1%，而 Flash 仅占 0.05%。
- **配额**：按组划分，包含一个 5 小时窗口和一个每周窗口，按 token 成本折算。根据作者账户的实测：在 `gemini-3.8-flash-medium` 下每百万源字符约消耗 5 小时窗口的 16 点，`gemini-3.7-flash-medium` 下为 14 点，低思考力度下为 7 到 8 点 — 因此一份 40,000 字符的 README 消耗略高于半点。每周上限则取决于订阅级别。重试遵循 agy 声明为可重试的状态；否则，耗尽的窗口绝不会重试：它会使每个文件失败，直到 `/usage` 显示重置。
- **比 API 慢**：在测试用的大篇幅密集文章上，`gemini-3.8-flash-medium` 每种语言的中位时间为 3 分 59 秒，`gemini-3.7-flash-medium` 为 3 分 14 秒，而 Gemini 3.7 Flash 通过 API 仅需 1 分 18 秒。
- **中断**：Ctrl-C 或关闭终端会连同命令一起停止 agy，而不是让它继续消耗您的配额完成本轮；Codex、Grok CLI 和 OpenCode 也是如此。在 `nohup` 下，翻译将继续进行。
- 在 CI 中被拒绝（定义了 `CI` 或 `GITHUB_ACTIONS`）：登录凭据保存在个人密钥环中。在 runner 上，请使用带有 `GOOGLE_API_KEY` 的 `--use_gemini`。
- 环境变量：`AGY_BIN`（否则使用 `PATH`，然后是 `~/.local/bin/agy`）、`AGY_TIMEOUT`（每个分段的秒数，包含启动时间，默认 900）。

**服务条款：风险由您的账户承担。** [Antigravity 服务条款](https://antigravity.google/terms)（第 6 条）及其 [FAQ](https://antigravity.google/docs/faq/) 禁止通过第三方软件利用 Antigravity 登录凭据访问该服务 — 其中明确提到了 Claude Code、OpenClaw 和 OpenCode — 否则可能导致账户被暂停。aipmt 既不读取也不重用令牌：它是在 Google 针对脚本和 CI 文档说明的[无头模式](https://antigravity.google/docs/cli/headless/)下启动官方二进制文件。Google 员工曾认为从本地脚本启动 `agy -p` 进行个人工作属于“标准用法”（[官方论坛，2026 年 9 月 25 日，非合同回复](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）；但尚无条文明确裁定像本工具这样公开发布的工具的情况。

**仅限公开文档。** 根据相同条款的第 5 条，交互内容（提示词、回复、元数据）可能会用于改进 Google 的产品和机器学习，并可能会有人工审核，即使是付费订阅也包含在内。退订需通过设置 `enableTelemetry`，其效果未有文档记载，且 aipmt 不会设置该选项；您的 agy 设置也不会带入其隔离环境中。切勿在此传输任何机密内容。

### 通过 Claude 订阅：`--use_claude_code`

官方 Claude Code CLI 的 `claude` 也是同样的原理，在 `-p` 模式下：对于支付了 Claude Pro 或 Max 的用户，翻译会从订阅配额中扣除，而不是按 token 计费。请勿将其与 Anthropic 按使用量计费的 API `--use_claude` 混淆。

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **不保留任何付费途径，且每次调用都会进行验证。** Claude Code 仅从您的环境中接收一个封闭的变量列表——既没有 API 密钥、令牌、云提供商，也没有启动 aipmt 的 Claude Code 会话的标记。在第一个片段之前，`claude auth status` 必须显示订阅连接且不带 Console 密钥，并且不消耗任何配额的 `/usage` 必须对此进行证明；每次调用又会在其初始化事件中对此予以证明，否则响应将被拒绝。
- **停用“额外用量（extra usage）”**（claude.ai，设置 → 用量），以确保保持零费用：一旦启用，它会在窗口用尽后接替并直接计费，而不显示任何错误。一旦调用的配额读数提示该情况，aipmt 会立即停止翻译，但该次调用已被计费。
- **与您的 Claude Code 会话共享配额。** 每次调用都会报告 5 小时及每周窗口的用量；一旦超过 80%（`AIPMT_CLAUDE_MAX_UTILIZATION`），将不再启动更多片段，以免耗尽您日常工作所需的额度。
- **隔离沙箱。** 每次调用都在没有工具的情况下运行，置于一个私有且一次性的目录中，处于无自定义模式：您的 `CLAUDE.md`、插件、钩子、MCP 服务器或个性化设置均不会加载，会话也不会保留任何内容。附件已被切断：文档中的 `@chemin` 仍保持纯文本状态，不会打开任何文件（经实测）。
- **模型**：默认使用 `sonnet`，effort 为 `low`，在 `--eco` 下亦是如此：在此路径下 `--eco` 不会产生任何改变。在相同文档上的实测显示，`haiku` 慢了两倍——它会强制进行推理而无法阻止——且成本几乎没有降低，而 `opus` 则会拒绝生物学相关的内容（见下一点）。两者均可通过 `--model` 访问；这些别名始终指向其家族的最新模型。`fable` 和 `[1m]` 变体均被拒绝，因为它们会走付费额度。`--reasoning_effort` 可调节推理投入（effort），但翻译根本无法从中获益：实测的推理消耗几乎为零。
- **Opus 会拒绝部分生物学内容。** 其安全护栏比 Sonnet 更严格，Anthropic 的错误提示中警告称它们“有时可能会标记邻近生物学研究的工作（can sometimes flag biology-research-adjacent work）”。实测表明：一篇关于生成的 279 种分子的监测简讯导致该文章在全部 14 种语言中均被拒绝。未写入任何内容：aipmt 拒绝了被截断的响应，指出护栏原因并建议使用 `--model sonnet`。
- 在 CI 环境中（设置了 `CI` 或 `GITHUB_ACTIONS`）以及 Windows 系统下被拒绝（未实测）。
- 环境变量：`AIPMT_CLAUDE_BIN`（否则使用 `PATH`，然后是 `~/.local/bin/claude`），`AIPMT_CLAUDE_TIMEOUT`（每个片段的秒数，默认 900），`AIPMT_CLAUDE_MAX_UTILIZATION`（默认 0.8），`CLAUDE_CONFIG_DIR`（Claude Code 的账户，绝不会从项目的 `.env` 中获取）；工作目录位于 `XDG_CACHE_HOME/aipmt/claude-code` 下（默认 `~/.cache`）。

**使用条款：由您自己的账户承担责任。**
[Claude Code 的法律页面](https://code.claude.com/docs/en/legal-and-compliance)
并不禁止“终端用户使用其自有的 Claude 订阅登录未修改的 Claude Code 二进制程序”：这正是 aipmt 的做法，它启动官方二进制程序且绝不读取令牌。但 Anthropic“不允许第三方开发者 […] 代表其用户通过 Free、Pro 或 Max 方案的凭据来路由请求”，更倾向于第三方工具“包括开源项目”使用 API 密钥，并保留将其使用量从付费额度中扣除的权利（[Claude 帮助中心](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)）。
目前尚无文本明确判定分发启动该二进制程序的工具属于何种情况。

**数据**：对于 Free、Pro 和 Max 账户，当隐私设置允许时，模型训练也适用于 Claude Code（[数据页面](https://code.claude.com/docs/en/data-usage)）。aipmt 不保留任何本地转录记录（`--no-session-persistence`）。请勿在此传输任何机密内容。

### 接入自选提供商：`--use_opencode`

[OpenCode](https://opencode.ai) 是一个开源（MIT）代码 Agent，可路由至其内部配置的提供商：API 密钥、订阅、OpenCode Zen 网关（免账户的免费模型）或本地模型。此处对两条路径进行了端到端实测：Zen 和 Ollama。

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

`--model` 是必填项：缺少它，OpenCode 将回退到免费模型，而这些交互可能会被用于训练，且此项选择不应代您决定。

每次调用的隔离环境：

- 内联配置优先于您的本地配置，定义了一个所有工具均被禁用的 `aipmt` Agent（`permission: { "*": "deny" }`），已禁用会话共享，`--pure`，绝不使用 `--auto`；
- 一次性且为空的工作目录，放置了 `OPENCODE_DISABLE_PROJECT_CONFIG` 和 `OPENCODE_DISABLE_CLAUDE_CODE`——没有它们，OpenCode 会将当前目录的 `AGENTS.md` 和 `~/.claude/CLAUDE.md` 注入提示词中。全局 `~/.config/opencode/AGENTS.md` 仍会被注入，OpenCode 无法将其屏蔽；
- 输出契约：返回码为 0，无 `error` 事件，无工具调用，最后一步为 `stop`，文本非空，且 `aipmt` Agent 已实际加载——未知的 `--agent` 不会导致 OpenCode 报错，而是会静默回退到编码 Agent；
- 不传递任何 `aipmt` 密钥，但 OpenCode 本身的密钥 `OPENCODE_API_KEY` 除外。提供商在 OpenCode 中进行配置，而不是在 `aipmt` 的 `.env` 中配置。

须知事项：

- Zen 的免费模型经常变动，限制未予公开记录，且其对话内容可能用于模型训练：适用于公开文档，不适合私密内容。
- 本地模型必须提供至少 16k token 的上下文，因为片段最大可达 16,000 个字符。Ollama 通常默认配置 4,096：请通过带有 `PARAMETER num_ctx 32768` 的 `Modelfile` 来指定。
- `--eco` 无效；`--reasoning_effort` 作为 OpenCode 的 `--variant` 原样传递。
- OpenCode 会将每个会话记录在 `~/.local/share/opencode/` 中。
- 环境变量：`OPENCODE_BIN`（否则使用 `PATH`，然后是 `~/.opencode/bin/opencode`），`OPENCODE_TIMEOUT`（每个片段的秒数，默认 600）。`OPENCODE_CONFIG` 原样传递给 OpenCode。

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

`reasoningEffort: "none"` 关闭了 Ollama 默认在这些模型上开启的思考过程，而 Modelfile 无法将其禁用。在包含六个单词的句子上实测：未带此选项时消耗了 919 个思考 token 且耗时 68 秒，带上此选项仅消耗 9 个 token。

### 接入 400 多个模型：`--use_openrouter`

OpenRouter 是一个按用量计费的路由服务，基于统一充值额度，面向第三方托管的模型——包括没有任何其他提供商在此提供的中国开源模型。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` 是必填项。在产生任何计费之前运行的预检（preflight）会处理该路由机制的两项特性：

- **同一个模型由数十家托管商提供，其上限各不相同**——针对 `z-ai/glm-5.3-flash`，有 23 家托管商，其中一家的输出上限仅为 2,048 个 token。预检会读取 `/api/v1/models/{modèle}/endpoints`，排除输出低于 8,000 个 token 或状态降级的托管商，并使用 `allow_fallbacks: false` 固定其余提供商。
- **推理按输出费率计费**——在 `z-ai/glm-5.2` 的一条“OK”响应中，相比 2 个常规 token，它消耗了 107 个思考 token。默认情况下思考已被关闭；强制要求思考的模型将设置为其接受的最低 effort，因为产品目录的默认值可能会在翻译完成前耗尽输出空间。`--reasoning_effort` 始终优先。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- 上下文窗口取自产品目录。低于 16,400 token 的模型在发起任何调用之前即被拒绝：8,400 token 留给提示词和片段，输出至少预留 8,000 token。
- 目录中不存在的标识、无法访问目录或缺少满足上限的托管商都会终止命令。
- 输出为空的 `finish_reason=length` 表示预算已被推理消耗完毕，而非被截断：错误消息会对两者进行区分。
- `--eco` 无效。
- 环境变量：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>），`OPENROUTER_BASE_URL`（默认 `https://openrouter.ai/api/v1`，必须提供 `https://`），`OPENROUTER_TIMEOUT`（默认 900），`OPENROUTER_PREFLIGHT_TIMEOUT`（默认 30）。

### 翻译说明

`--add_translation_note` 会添加一条说明，位置可选 `bottom`（默认）、`top`（在 front matter 之后）或 `both`（`--note_position`），格式可选 `legacy`（粗体段落，默认）或 `marker`（`--note_format`）。`marker` 格式是一个不可见的 Markdown 引用定义：
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`，
后接一段粗体引用：在 GitHub 上可直接阅读，在构建时可供 remark 插件调用。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 详细测量数据

所有测量均为实际使用 `aipmt` 执行的翻译，目标为 14 种语言：en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi。
**已写入**统计了安全检查放行的文件数；**无差异**统计了 `scripts/compare_structure.py` 未检测出任何异常的文件数——具有相同数量的章节、子标题、链接、独立 URL、代码块、行内代码、表格行、引用块和粗体词。

“无差异”意味着“未检测到问题”，而非“完全相同”：对比工具只统计元素数量而不读取其内容。它既不会报告被删除的 4 级标题，也不会报告被替换的行内代码文本，不会检测被互换的标志，也不会发现内部链接因带有多余括号 `[texte]((#ancre))` 而失效——同时它也不评估语言质量。

### 高密度技术监测文章，模式 `--news`

来自 [jls42.org AI 监测](https://jls42.org/fr/news) 的一期内容：589 行、140 个链接、21 个章节、3 处受保护的英文引用。测试周期为 2026 年 9 月 4 日至 5 日。

| 模型 | 访问方式 | 已写入 | 无差异 | 中位数/语言 |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash` | Google API | 14/14 | ✅ **14/14** | 1 分 18 秒 |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google 订阅 | 14/14 | ✅ **14/14** | 3 分 59 秒 |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google 订阅 | 14/14 | ✅ **14/14** | 3 分 14 秒 |
| `gpt-5.6-sol` (`--use_codex`) | ChatGPT 订阅 | 14/14 | ✅ **14/14** | 11 分 28 秒 |
| `z-ai/glm-5.2` | OpenRouter | 14/14 | ✅ **14/14** | 5 分 37 秒 |
| `qwen/qwen3.8-flash` | OpenRouter | 14/14 | ✅ **14/14** | 26 分 23 秒 |
| `sonnet` (`--use_claude_code`) | Claude 订阅 | 14/14 | ⚠️ 13/14 | 6 分 49 秒 |
| `claude-sonnet-5` | Anthropic API | 14/14 | ⚠️ 11/14 | 6 分 31 秒 |
| `haiku` (`--use_claude_code`) | Claude 订阅 | 14/14 | ⚠️ 11/14 | 15 分 54 秒 |
| `opencode/mimo-v2.5-free` | OpenCode Zen | 13/14 | ❌ 11/14 | 9 分 27 秒 |
| `qwen/qwen3.7-flash` | OpenRouter | 13/14 | ❌ 8/14 | 10 分 09 秒 |
| `ollama/gpt-oss-20b-32k` | 本地 | 10/14 | ❌ 7/14 | 12 分 39 秒 |
| `mistral-large-latest` | Mistral API | 11/14 | ❌ 5/14 | 5 分 32 秒 |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter | 4/14 | ❌ 3/14 | 37 分 27 秒 |
| `grok-4.6` (`--use_grok_cli`) | Grok 订阅 | 1/14 | ❌ 1/14 | 23 分 11 秒 |
| `opus` (`--use_claude_code`) | Claude 订阅 | 0/14 | ❌ 0/14 | — |

9 月 9 日对 Grok 在同一监测专栏的另一期内容（356 行）上进行了重新测量：14 种语言中成功写入 9 种，8 种无差异。表头展示的正是此数据。三组因额度不足而中断的测试未计入其中：`qwen3.5-27b`（9 种语言）和 `kimi-k2.6`（4 种），以及 `z-ai/glm-5.3-flash`（其两次失败源于推理设置，提供商此后已将其修正）。OpenRouter 相关行是在采用 `--use_openrouter` 之前、按路由器的默认设置进行测量的；使用附带的提供商重新测量的 `z-ai/glm-5.2` 同样达到了 14/14。9 月 10 日使用当前对比工具重新计算了这些数据：相比首次发布，`qwen3.8-flash` 和 `qwen3.7-flash` 各增加了一种语言，其余保持不变。

`--use_antigravity` 相关行于 9 月 26 日在同一文章上进行了测量，采用四路并发翻译：上午为 `gemini-3.7-flash-medium`，下午为 `gemini-3.8-flash-medium`。在英语翻译中，两者均自行删除了引用下方的三行法语翻译，且未捏造任何标志，英文引用保持原样：后备清理步骤无需做任何处理。在 `--eco`（`gemini-3.7-flash-low`）模式下，仅针对四种语言（en、ja、ar、hi）测试：4 种全部成功写入，且均无差异，中位时间为 1 分 52 秒。同日对 9 月 25 日更新的一期监测文章（438 行，2 处英文引用）进行了复测，在博客外部通过 `gemini-3.7-flash-medium` 进行翻译：14 种语言全部成功写入，且均无差异，每种语言耗时 87 至 128 秒。

`--use_claude_code` 相关行于 9 月 26 日在同一文章上进行了测量，采用四路并发翻译，推理投入为 `low`。使用 `sonnet` 时，英文引用在 14 种语言中均完好无损，且在英语翻译中，模型自行去除了法语翻译行，未编造标志。`opus` 未能写入任何语言：在每种语言中，其护栏机制都在最后一个片段终止了响应，原因是一篇关于为结合位点生成的 279 种分子的简讯。单独发送时，该简讯会因被归入“生物（bio）”分类而被拒绝；而 `sonnet` 在所有语言中均完成了翻译。`haiku` 成功写入了全部 14 种语言；但在三种语言（en、pl、ro）中，有一个章节标题从 2 级变成了 1 级。它会强制进行无法阻止的思考过程——占其输出 token 的 61%——因此耗时达到了 `sonnet` 的两倍以上。

### 本项目的 README，标准 Markdown

定稿于 2026 年 9 月 9 日的修订版本：785 行、285 处行内代码、40 处代码块闭合标记、89 行表格。4 组并行翻译。

| 模型 | 已写入 | 无偏差 | 中位数/语言 | 差异内容 |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | 无 |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | 无 |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | 比对工具未检出差异；内部链接重复 (en) |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | 一个加粗词 (ja) |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | 一个加粗词 (ko) |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | 一行表格与前一行粘连 (ar) |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | 一个链接 (sv)，一个加粗词 (zh) |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | 一个加粗词 (ar, ja) |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | 一个加粗词 (hi, ja, ko) |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 阿拉伯语添加了 40 处行内代码；加粗 (hi, ja, ko) |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | 丢失一个章节 (ar, hi, ko)；添加了代码块 (ja, ko, ro, zh) |

有两组中断的测试未计入：Grok，在完成 12 种语言（其中 11 种无偏差）后 CLI 会话超时；以及 `qwen3.8-flash`，在完成两笔后收到服务商返回的 HTTP 429。`opencode/mimo-v2.5-free` 与 `ollama/gpt-oss-20b-32k` 未在此修订版本上重新测试；在 9 月 4 日至 5 日的修订版本（少了 277 行）中，它们各自成功写入 14 种语言中的 9 种翻译，其中分别有 7 种和 1 种无偏差。

`--use_antigravity` 和 `--use_claude_code` 所在的行并未在该定稿版本上进行测试，而是在 9 月 26 日随 1.14.0 发布的版本上测得：600 行、257 处行内代码、30 处代码块闭合标记、85 行表格。该版本少了 185 行，无法与其他各行逐项对比；不过这两行之间可以相互对比。在比对工具未检查的内部链接方面，`gemini-3.8-flash-medium` 在所有 14 种语言中均保持完好，`gemini-3.7-flash-medium` 在意大利语中损坏了链接；`sonnet` 和 `opus` 在所有语言中均保持完好，`haiku` 在英语中重复了链接。

### 四个知名项目的 README

FastAPI、Ollama、tldr-pages 和 Vue.js，直接取自 GitHub——这些文档比前两个要简单。该测试主要针对遇到困难的模型；Gemini 在此作为参考基准。

| 模型 | 范围 | 已写入 | 无偏差 |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 个项目 × 14 种语言 | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 个项目 × 14 种语言 | 55/56   | ❌ 47/56     |
| `grok-4.6` (订阅版)   | 4 个项目 × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 个项目 × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### 这些测试不是什么

- **并非详尽的排行榜**：仅 OpenRouter 就提供了四百多个模型，此处仅测试了约十五个。
- **耗时仅供参考**：各轮测试采用 3 到 6 组并行翻译，且服务商的吞吐量在一天中会有所波动。
- **特定时点的观察结果**：同名模型可能会发生更新，而且您的文档与我们的文档也不尽相同。

若要在您的文档上复现测试，请使用文件的定稿副本：

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

这两行都是必需的：如果没有 `pip install -e .`，`python -m aipmt` 会返回 `No module named aipmt`。

质量控制工具（可选但推荐）：

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

仓库中的 28 个翻译文件（README 和 CHANGELOG，共 14 种语言）可通过 `./regen_translations.sh --force` 重新生成——默认使用 ChatGPT 订阅上的 Codex 和 `gpt-5.6-sol`，4 组并行。`REGEN_PROVIDER` 和 `REGEN_MODEL` 用于更改路径：`antigravity` 仍然使用订阅模式（Google 订阅），无需额外授权即可通过；按量计费的 API（`openai`、`gemini`、`grok`、`openrouter`）若无 `REGEN_ALLOW_PAID_API=1` 则会被拒绝；`REGEN_JOB_TIMEOUT` 对每个任务设置上限（通常为 600 s，Codex 和 Antigravity 为 1 800 s）。工具的详细说明见 `CLAUDE.md`。

## 使用此脚本的项目

- **[jls42.org](https://jls42.org)** ——以 15 种语言发布的个人博客。其[每日 AI 动态速递](https://jls42.org/fr/news)每天都由该工具翻译，并作为上述测试的基准参考文档。

## 作者

Julien LE SAUX
电子邮箱：contact@jls42.org

## 许可证

GNU GENERAL PUBLIC LICENSE Version 3。参见 [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)。

## 免责声明

本程序**不附带任何保证**进行分发，遵循 GPL v3 第 15 条和第 16 条的规定：按“原样”提供，不提供任何适销性或特定用途适用性的担保，作者对因使用本程序而造成的任何损失不承担责任。具体以许可证全文为准，此概述仅供参考。

- **发布前请仔细核对。** 保护机制涵盖代码块、行内代码、URL、锚点以及 `--news` 模式下的引用——但不涵盖标题、表格、front matter 或语句的原意。
- **您的文档将发送至所选的服务商**，并受其使用条款和数据政策的约束。部分免费模型可能会将您的交互数据用于模型训练，而 Antigravity 的条款允许 Google 重复使用这些数据并让人工进行审查（即便使用付费订阅也是如此）；本地模型是确保任何数据都不离开您机器的唯一途径。
- **API 调用会产生费用。** 本程序不对支出设置上限：长文档、失败后重试或具备深度推理能力的模型都会产生更多费用。
- **所公布的测试数据仅为特定时点的观察结果**，不作为保证。

所提及的产品和公司名称均为其各自所有者的财产。本项目与其中任何一方均无关联。

**使用 gemini-3.8-flash-medium 从法语翻译成中文的文章。**
