# AI 驱动的 Markdown 翻译器

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 代码质量</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Quality Gate 状态"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="安全评级"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="可靠性评级"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="可维护性评级"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="覆盖率"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="漏洞"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bug"></a>
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

将 Markdown 文件从一种语言翻译为另一种语言，同时保留其结构：代码块、行内代码、URL、锚点、表格和 front matter。提供 11 种模型调用方式——5 个 API、4 种无按量计费的订阅服务、2 个路由器——并公开发布了每个模型实际保留情况的评测数据。

## 概览

- **11 种 Provider 途径**：OpenAI、Mistral、Claude、Gemini 和 Grok API；无按量计费的 ChatGPT (Codex)、Grok、Google (Antigravity) 和 Claude (Claude Code) 订阅；OpenCode（开源、免费或本地）与 OpenRouter（400+ 个模型）路由器。
- **绝无因 Token 丢失导致的损坏**：代码块、行内代码、URL、锚点和引用在调用前会被替换为 Token，并在返回时进行校验。如果丢失任何一个，则不会写入文件。
- **长文档处理**：根据模型的上下文窗口自动分段。
- **`--news` 模式**：保护英文引用并按语言处理国旗图标，专为资讯速递文章设计。
- **`--eco` 模式**：调用速度更快且成本更低的模型。
- **可选的翻译附注**：可添加在顶部、底部或两处兼有。

## 安装

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 或更高版本。如需从仓库安装，请参阅[贡献指南](#贡献)。

## 配置

密钥从三个位置读取，按优先级从高到低排列；每个位置仅填充前一个位置未提供的值。

|     | 位置                                          | 用途                                  |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 环境变量                                      | CI、容器、临时覆盖                    |
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

支持使用 `GEMINI_API_KEY` 代替 `GOOGLE_API_KEY`。用户配置文件在 Windows 下遵循 `XDG_CONFIG_HOME`（仅限绝对路径）和 `%APPDATA%`。如果未找到密钥，该命令会列出这三个位置。

**项目中的 `.env` 既不能重定向调用，也不能指定执行的程序。** 它只提供密钥，绝不提供目标地址或二进制文件：任何以 `_BASE_URL`、`_API_BASE`、`_ENDPOINT` 或 `_BIN`（`CODEX_BIN`、`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`）、`GROK_HOME` 命名的变量、代理（`HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY`）、证书存储（`SSL_CERT_FILE`、`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）以及 `XDG_CONFIG_HOME` / `APPDATA` 均会被忽略并发出警告。克隆的仓库不应在首次翻译时窃取您的密钥，也不应诱使您运行其自带的程序。该文件读取时也不进行变量插值：`NOM=${OPENAI_API_KEY}` 不会在其中复制密钥。请将这些变量设置在环境中或 `~/.config/aipmt/.env` 中。

可选变量：`XAI_BASE_URL`（默认 `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（每次调用的秒数，默认 900）、`CODEX_BIN`、`CODEX_TIMEOUT`（默认 600）、`GROK_BIN`、`GROK_HOME`（默认 `~/.grok`）、`GROK_TIMEOUT`（默认 900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（默认 900）、`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（默认 600）、`OPENROUTER_BASE_URL`（需要 `https://`）、`OPENROUTER_TIMEOUT`（默认 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（默认 30）。每个变量均在其对应的 Provider 章节中详细说明。

## 快速上手

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

将 `document.md` 翻译为西班牙语会在 `--target_dir` 中生成 `document-es.md`；使用 `--include_model` 则生成 `document-es-gpt-5.6-terra.md`。扩展名始终变为 `.md`——`article.mdx` 会生成 `article-en.md`——除非使用 `--keep_filename` 保留原始名称。若未使用 `--force`，已存在的翻译将被跳过。

退出代码：若全部成功或跳过则为 `0`；若有文件失败则为 `1`（在标准错误输出中列出）；若由于配置问题则为 `2`。失败的文件绝不会被写入，即使写入过程本身出错也是如此：内容会先写入临时文件然后再重命名。只需重新运行即可。

## 模型选择建议

在两篇真实文档上进行了评测，每个模型均翻译为相同的 14 种语言。**数字表示在 14 种语言中，翻译成功写入且与源结构完全一致的语言数量。**

| 模型                  | 获取方式                          | 密集资讯文章            | 本 README    | 差异内容及涉及的语言数                                                                                                                                             |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google (Antigravity) 订阅         | ✅ 14/14                | ✅ 14/14     | 两篇文档均无任何差异                                                                                                                                               |
| **Claude Sonnet 5.5** | Anthropic API 密钥                | ✅ 14/14                | ✅ 14/14     | 两篇文档均无任何差异                                                                                                                                               |
| **Gemini 3.7 Flash**  | Google API 密钥                   | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种：多出一个粗体词 (ja)                                                                                                                           |
| **Gemini 3.7 Flash**  | Google (Antigravity) 订阅         | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种：缺少一个粗体词 (ko)                                                                                                                           |
| **GPT-5.6 Sol**       | ChatGPT 订阅或 OpenAI 密钥        | ✅ 14/14                | ⚠️ 12/14     | 14 种语言中有 2 种：缺少一个粗体词 (ar, ja)                                                                                                                       |
| **GLM-5.2**           | OpenRouter 密钥                   | ✅ 14/14                | ⚠️ 11/14     | 14 种语言中有 3 种：缺少一个粗体词 (hi, ja, ko)                                                                                                                   |
| Claude Sonnet 5       | Claude (Claude Code) 订阅         | ⚠️ 13/14                | ⚠️ 13/14     | 文章中有 1 种语言：多出一个粗体词 (zh)；本 README 中有 1 种语言：一行表格与上一行粘连，渲染时被隐藏 (ar)                                                           |
| Claude Haiku 4.5      | Claude (Claude Code) 订阅         | ⚠️ 11/14                | ✅ 14/14     | 文章中有 3 种语言：某个小节标题变成了 1 级标题 (en, pl, ro)；本 README 在对比工具中无差异，但内部链接被重复了一遍英文                                              |
| Claude Sonnet 5       | Anthropic API 密钥                | ⚠️ 11/14                | ⚠️ 12/14     | 文章中有 3 种语言：凭空出现了一个代码块 (es, de, hi)；本 README 中有 2 种语言：一个链接丢失了标记语法 (sv)，一个粗体词 (zh)                                       |
| Claude Haiku 4.5      | Anthropic API 密钥                | ⚠️ 7/14                 | ✅ 14/14     | 文章中有 7 种语言：某个小节标题变成了 1 级标题——日语版中仍保留为法语；本 README 无差异                                                                             |
| Claude Haiku 5.5      | Anthropic API 密钥                | ⚠️ 11/14                | ❌ 12/14     | 文章中有 3 种语言：小节标题层级改变或重复 (ja, ko, zh)；本 README 中有 2 种语言被拒，行内代码丢失 (ar, hi)                                                         |
| Qwen 3.7 Flash        | OpenRouter 密钥                   | ❌ 8/14                 | ⚠️ 10/14     | 文章中有 1 种语言被拒，另有 5 种出现偏差；本 README 中约有 40 个词被加上了 `code` (ar)                                                                     |
| Grok 4.6              | Grok 订阅                         | ❌ 8/14                 | 未评级       | 14 种语言中有 5 种被拒，原因是行内代码和 URL 未正确还原；荷兰语版本完全偏离                                                                                        |
| GPT-OSS 20B           | 本地模型 (Ollama)                 | ❌ 7/14                 | 未重测       | 14 种语言中有 4 种被拒：模型残留了法语段落，被保护机制拦截                                                                                                         |
| MiMo v2.5 (免费)      | OpenCode Zen，免账户              | ❌ 11/14                | 未重测       | 1 种语言被拒；波兰语版本丢失了一个小节                                                                                                                             |
| Mistral Large         | Mistral API 密钥                  | ❌ 5/14                 | ❌ 1/14      | **整节内容丢失**：文章中有 1 种语言 (hi)，本 README 中有 3 种语言 (ar, hi, ko)——且文章中有 3 种语言被拒                                                           |
| DeepSeek V4 Flash     | OpenRouter 密钥                   | ❌ 3/14                 | 未重测       | 14 种语言中有 10 种被拒；每种语言耗时 37 分钟                                                                                                                      |
| Claude Opus 5.5       | Claude (Claude Code) 订阅         | ❌ 0/14                 | ✅ 14/14     | 由于一条生物学简讯触发了 Opus 的安全防护机制，文章在所有 14 种语言中均被拒绝；本 README 无差异                                                                    |

|     | 符号含义                                                                                                                                                                              |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 全部 14 种语言均已翻译，且与源结构完全无差异                                                                                                                                          |
| ⚠️  | 全部 14 种语言均已翻译；差异仅限于**标记格式**——例如多出一个粗体词、一个 `code` 或某个链接丢失了方括号。文本、URL、代码块或章节均无任何遗漏                                   |
| ❌  | 至少有一种语言无法翻译（文件被拒绝且未写入），**或者**已写入的文件中存在内容缺失                                                                                                       |

要点总结：

- **被拒绝的翻译不等于损坏的翻译。** 当返回结果缺少 Token 时，文件不会被写入，该语言会被计为被拒绝。Grok 在测试文章中就是这种情况：在 5 种非拉丁脚本语言中，第一段就丢失了 4 处行内代码和 3 个 URL。
- **模型可能会因为一句话而拒绝整个文档。** Opus 5.5 翻译本 README 时分毫不差，但完全无法翻译技术资讯文章：其安全防护机制因一条生物学简讯而中断了响应。文件未被写入，且 aipmt 会给出具体原因。
- **此防护网并不覆盖标题、表格、front matter 或正文文本。** 如果模型删除了某个小节，工具依然会照常写入该文件——Mistral 就是这种情况。这些元素无法用 Token 替换，目前的防护机制也不会检查它们；`scripts/compare_structure.py` 可以在事后检测出缺失的小节。
- **Grok 在本 README 中未评级**：其 CLI 会话在处理完 12 种语言后超时过期，其中 11 种无任何差异。中断的评测不予评分。
- **文档的信息密度比目标语言更关键。** Grok 在普通 README 上表现良好，但在链接密集的文章中会出现掉链子现象，即便是荷兰语也是如此。

测试日期与文档：“本 README”列于 2026 年 9 月 9 日基于本文件的固定版本（785 行，285 处行内代码，89 行表格）进行测试，此后有所修改——除 Antigravity 和 Claude Code 行于 9 月 26 日基于随 1.14.0 发布的较短版本（600 行，257 处行内代码，85 行表格）进行测试，以及通过 API 调用的 Claude Sonnet 5.5、Haiku 5.5 和 Haiku 4.5 于 10 月 18 日基于相同版本进行测试。“密集资讯文章”列来自 9 月 4 日至 5 日对一篇 589 行文章的测试，除 Grok 行于 9 月 9 日在同系列资讯的另一期上重新测试，Antigravity 和 Claude Code 行于 9 月 26 日在同一文章上测试，以及上述三行 Claude 于 10 月 18 日测试。完整表格、耗时和测试协议请参阅[详细评测数据](#详细评测数据)。

## 所有选项

| 选项                     | 描述                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | 要翻译的单个 Markdown 文件（替代 `--source_dir`）                                                             |
| `--source_dir`           | 包含 Markdown 文件的源目录（默认：`content/posts`）                                                            |
| `--target_dir`           | 翻译文件的输出目录（默认：`traductions_en`）                                                                    |
| `--source_lang`           | 源语言（默认：`fr`）                                                                                |
| `--target_lang`           | 目标语言（默认：`en`）                                                                              |
| `--model`           | 要使用的特定模型                                                                                              |
| `--eco`           | 使用经济型模型                                                                                                |
| `--use_mistral`           | 使用 Mistral AI API                                                                                           |
| `--use_claude`           | 使用 Claude API                                                                                               |
| `--use_gemini`           | 使用 Gemini API                                                                                               |
| `--use_grok`           | 使用 xAI (Grok) API — 需要 `XAI_API_KEY`                                                                     |
| `--use_codex`           | 在 ChatGPT 订阅配额上使用 Codex CLI                                                                           |
| `--use_grok_cli`           | 在 Grok 订阅配额上使用 Grok CLI                                                                               |
| `--use_antigravity`           | 在 Google AI Pro 或 Ultra 订阅配额上使用 Antigravity CLI（`agy`）                                    |
| `--use_claude_code`           | 在 Claude Pro 或 Max 订阅配额上使用 Claude Code CLI（`claude -p`）                                         |
| `--use_opencode`           | 使用 OpenCode（开源）连接到 OpenCode 中配置的提供商；需要 `--model provider/modèle`                                      |
| `--use_openrouter`           | 使用 OpenRouter — 需要 `OPENROUTER_API_KEY` 和 `--model fournisseur/modèle`                                                       |
| `--force`           | 强制重新翻译                                                                                                  |
| `--keep_filename`           | 保留原始文件名                                                                                                |
| `--news`           | 新闻模式：保护英文引用，管理各语言国旗图标                                                                    |
| `--add_translation_note`           | 添加翻译说明                                                                                                  |
| `--note_position`           | 说明位置：`top`、`bottom`（默认）或 `both`                                             |
| `--note_format`           | 说明格式：`legacy`（默认，粗体段落）或 `marker`                                                 |
| `--include_model`          | 在输出文件中包含模型名称                                                                                      |
| `--reasoning_effort`          | GPT-5.x 推理力度：`none`/`low`/`medium`/`high`/`xhigh`             |

这九个 `--use_*` 标志互斥：组合其中任意两个将被拒绝。

## 提供商

### 通过 API：OpenAI、Mistral、Claude、Gemini、Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` 会切换到每个提供商的经济档次。

| 提供商      | 质量优先（默认）                                      | 经济型（`--eco`） |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`           |
| Claude      | `claude-sonnet-5-5`                                       | `claude-haiku-5-5`           |
| Mistral     | `mistral-large-latest`                                       | `mistral-small-latest`           |
| Gemini      | `gemini-3.7-flash`                                       | `gemini-3.1-flash-lite`           |
| Codex       | `gpt-5.6-sol`（也可通过 `--model` 使用 `terra` 和 `luna`） | `gpt-5.6-luna`           |
| Grok API    | `grok-4.6`                                       | `grok-4.3`           |
| Grok CLI    | `grok-4.6`                                       | `grok-4.5`           |
| Antigravity | `gemini-3.8-flash-medium`                                       | `gemini-3.7-flash-low`           |
| Claude Code | `sonnet`，思考力度 `low`             | 同上 — `--eco` 无效 |
| OpenCode    | 必须指定 `--model provider/modèle`                              | 同上 — `--eco` 无效 |
| OpenRouter  | 必须指定 `--model fournisseur/modèle`                              | 同上 — `--eco` 无效 |

### 使用 ChatGPT 订阅：`--use_codex`

调用官方 Codex CLI：翻译从 ChatGPT 订阅配额中扣除，无需 API 密钥或按量计费。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 在 `CODEX_BIN` 中查找二进制文件，然后是 `PATH`，最后是 `openai-codex-cli-bin` 包。绝不会读取 `~/.codex/auth.json`。
- `OPENAI_API_KEY` 和 `CODEX_API_KEY` 会从子进程环境中移除：即使存在密钥，也绝不会切换到 API。
- 每个分段至少消耗 5 小时窗口中的一条“消息”——若验证失败并重试则消耗两条。据 OpenAI 估计，Plus 计划下 `gpt-5.6-luna`（`--eco`）约为 250–2,000 条消息/5 小时，而 `gpt-5.6-sol` 约为 10–100 条。
- `--model gpt-5.6-terra` 和 `--model gpt-5.6-luna` 同样通过订阅执行。如果账户无权使用某个模型，将返回 400“model is not supported when using Codex with a ChatGPT account”。
- 比 API 慢，且差距随文档变大而增加：对于本 README，使用 `gpt-5.6-sol` 每种语言的中位时间为 6 分 46 秒，而 `gemini-3.7-flash` 仅需 36 秒。
- 在 CI 中被拒绝（已设置 `CI` 或 `GITHUB_ACTIONS`）：订阅通过个人会话文件进行身份验证，该文件不应出现在共享 runner 上。
- 环境变量：`CODEX_BIN`、`CODEX_TIMEOUT`（每段秒数，默认 600）。

### 使用 Grok 订阅：`--use_grok_cli`

使用官方 Grok Build CLI 时原理相同，基于 SuperGrok 或 X Premium+ 订阅。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **隔离性弱于 Codex。** Grok 的操作系统沙箱在许多较新的 Linux 设备上无法生效（AppArmor、容器运行时套接字），且无法生效的配置文件会在静默状态下以未隔离模式启动。因此，该脚本默认不请求任何配置文件，进行提示，并依赖 CLI 的 `--deny` 规则，其中包括全捕获规则 `*` —— 这是唯一一层会拒绝启动而不是在未通知的情况下直接移除保护的机制。`GROK_TRANSLATE_SANDBOX=read-only` 强制要求操作系统沙箱，若机器无法满足则启动失败。
- 配额按周计算，与 Chat、Imagine 和 Voice 共享，且没有任何命令可查询该配额：批量任务可能会在没有任何提醒的情况下消耗对话使用量。
- 环境变量：`GROK_BIN`、`GROK_HOME`（CLI 目录，默认 `~/.grok`）、`GROK_TIMEOUT`（默认 900）、`GROK_TRANSLATE_SANDBOX`。

### 使用 Google 订阅：`--use_antigravity`

使用 Antigravity 官方 CLI `agy` 时原理相同：对于订阅了 Google AI Pro 或 Ultra 的用户，翻译会从订阅配额中扣除，而不是按 token 计费。这是使用该配额的唯一途径：Gemini CLI 自 2026 年 6 月 18 日起不再支持这些账户（[公告](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)），且 Antigravity SDK 仅接受 API 密钥或 Google Cloud 项目。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **杜绝任何付费途径。** agy 从您的环境中仅接收白名单中的有限变量 —— `PATH`、语言和时区、终端、身份标识、代理与证书、会话总线 —— 绝不包含任何密钥：其部分变量会在不显示任何提示的情况下切换调用方式（实测：其中一个会将文档发送至第三方网关，另一个则发送至计费的 Google Cloud 项目），且黑名单机制在每次审查时总有遗漏。在处理任何分段之前，不消耗配额的 `agy -p /config` 必须显示付费 AI 额度已禁用，且无 API 密钥或 Google Cloud 项目 —— 缺少该设置即视为拒绝 —— 否则不进行任何翻译；随后每次调用的日志必须证实使用的是订阅配额（`authMethod=consumer`），否则响应将被拒绝。
- **隔离性。** 每次调用都在一个独立的临时主目录中运行，并配备一个不带工具的翻译代理：您的 agy 设置、规则、插件、MCP 服务器和钩子均不会带入其中，不会向您的历史记录添加任何内容，凭据保留在密钥环中，aipmt 绝不会读取该密钥环。如果未找到指定的代理，agy 会静默回退到其编码代理和工具：日志中必须包含确认正确代理的整行信息 —— 引用该消息的文档不能替代此日志验证 —— 否则将被拒绝。
- **支持平台**：Linux（需在具有密钥环的会话中，如 D-Bus 会话总线、Secret Service）；支持 macOS，但尚未经过实测。在 Windows 下会被拒绝，因为 agy 无法读取隔离每次调用的变量；在没有会话总线的 Linux 环境下也会被拒绝 —— 例如 SSH 会话、容器、服务器：agy 会在这些环境中将其令牌保存在 `~/.gemini` 文件中，而隔离机制会将其屏蔽。拒绝会在启动前发生并提示原因，无需等待一分钟以获取登录代码。
- **模型**：`agy models` 所提供的模型。Gemini 系列在名称中包含推理力度（`gemini-3.8-flash-medium`…）：不带后缀的名称在调用前会被拒绝，且 `--reasoning_effort` 无效。默认使用 `gemini-3.8-flash-medium`，在 `--eco` 模式下使用 `gemini-3.7-flash-low`；确定这些配置的测试系列在[详细评测](#详细评测数据)中进行了说明。Claude 和 GPT-OSS 拥有独立的配额，且额度小得多：实测每次调用约消耗 5 小时窗口的 1%，而 Flash 仅约 0.05%。
- **配额**：按组划分，包括 5 小时窗口和每周窗口，按 token 成本比例扣除。在作者账户上的实测结果：在 `gemini-3.8-flash-medium` 下每百万源字符约消耗 5 小时窗口的 16 个点，在 `gemini-3.7-flash-medium` 下为 14 个点，在低推理力度下为 7 至 8 个点 —— 因此一份 40,000 字符的 README 消耗略高于半个点。周限制则取决于订阅档次。重试机制遵循 agy 声明为可重试的情况；否则，已用尽的窗口绝不会重试：它会导致每个文件处理失败，直到 `/usage` 显示重置时间。
- **比 API 更慢**：在评测中使用的密集长文上，每种语言的中位时间为：`gemini-3.8-flash-medium` 下 3 分 59 秒，`gemini-3.7-flash-medium` 下 3 分 14 秒，相比之下通过 API 使用 Gemini 3.7 Flash 仅需 1 分 18 秒。
- **中断**：Ctrl-C 或关闭终端会连同命令一起终止 agy，而不是让它继续在您的配额上运行；Codex、Grok CLI 和 OpenCode 也是如此。在 `nohup` 下，翻译会继续进行。
- 在 CI 中被拒绝（已设置 `CI` 或 `GITHUB_ACTIONS`）：凭据保存在个人密钥环中。在 runner 上，请使用 `--use_gemini` 搭配 `GOOGLE_API_KEY`。
- 环境变量：`AGY_BIN`（若未设置则为 `PATH`，然后是 `~/.local/bin/agy`）、`AGY_TIMEOUT`（每段秒数，包含启动时间，默认 900）。

**使用条款：须自行承担账户风险。** [Antigravity 条款](https://antigravity.google/terms)（第 6 节）及其 [常见问题解答](https://antigravity.google/docs/faq/) 禁止使用第三方软件借助 Antigravity 登录凭据访问该服务 —— 其中提到了 Claude Code、OpenClaw 和 OpenCode —— 违者可能面临账户封禁。aipmt 既不读取也不复用该令牌：它仅在 Google 针对脚本和 CI 记录的 [无头模式 (headless)](https://antigravity.google/docs/cli/headless/) 下启动官方二进制文件。Google 团队的一位成员曾认为通过本地脚本启动 `agy -p` 用于个人工作属于“标准操作”（[官方论坛，2026 年 9 月 25 日，非合同性回复](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）；但尚无官方条款对类似本工具的分发形式做出明确裁定。

**仅限公开文档。** 根据相同条款的第 5 节，交互内容 —— 提示词、响应、元数据 —— 可能会用于改进 Google 的产品和机器学习，并可能会被人工审核（即使付费订阅也是如此）。退出该机制需要通过 `enableTelemetry` 设置，但其具体效果未有文档说明，且 aipmt 不会对其进行设置；您的 agy 设置也不会继承到其隔离环境中。请切勿传输任何机密内容。

### 关于 Claude 订阅：`--use_claude_code`

在使用 Claude Code 官方 CLI 的 `claude` 并处于 `-p` 模式下也是同样的原理：对于 Claude Pro 或 Max 付费用户，翻译直接扣除订阅额度，而不是按 token 计费。请勿将其与 Anthropic 的 `--use_claude` API 混淆，后者是按量计费的。

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **不保留任何付费途径，且每次调用都会进行验证。** Claude Code 仅从您的环境中接收一个受限的变量列表——既没有 API 密钥、令牌、云提供商配置，也没有发起 aipmt 的 Claude Code 会话标识。在第一个分段之前，`claude auth status` 必须显示订阅连接，且不含 Console 密钥，而无需消耗任何额度的 `/usage` 必须对此进行证实；每次调用随后都会在其初始化事件中证实这一点，否则响应将被拒绝。
- **请禁用“额外用量（extra usage）”**（claude.ai，设置 → 用量），以确保实现零花费：启用后，它会在窗口额度耗尽时自动接管并产生计费，且不显示任何错误。一旦调用的额度报告显示耗尽，aipmt 会立即停止翻译，但该次调用已被计入。
- **与您的 Claude Code 会话共享配额。** 每次调用都会报告 5 小时和周窗口的使用情况；超过 80%（`AIPMT_CLAUDE_MAX_UTILIZATION`）时，将不再启动后续分段，以避免耗尽您的工作配额。
- **环境隔离。** 每次调用均在不加载任何工具、独立的私有一次性目录中运行，处于无个性化模式：您的 `CLAUDE.md`、插件、hooks、MCP 服务器或自定义设置均不会被加载，会话也不会保留任何内容。附件功能已被切断：文档中的 `@chemin` 仍保持纯文本状态，不会打开任何文件（已实测）。
- **模型**：默认使用 `sonnet`，思考程度为 `low`，在 `--eco` 下亦是如此：`--eco` 在此路径上没有任何改变。在相同文档上的实测表明，`haiku` 耗时慢两倍——它会在无法阻止的情况下强制进行推理——而成本仅略微降低，且 `opus` 会拒绝生物学内容（见下一项）。两者均可通过 `--model` 访问；这些别名始终指向其家族的最新模型。`fable` 和 `[1m]` 变体会被拒绝，因为它们会转入付费点数计费。`--reasoning_effort` 用于调节思考程度，翻译从中获益微乎其微：实测推理几乎为零。
- **Opus 会拒绝某些生物学内容。** 它的安全防范机制比 Sonnet 更严格，Anthropic 的错误信息提示它们“有时可能会标记与生物学研究相关的工作（can sometimes flag biology-research-adjacent work）”。实测：一篇关于 279 个生成分子的技术简报导致该文章在全部 14 种语言中均被拒绝。未写入任何内容：aipmt 会拒绝被截断的响应，指出触发的安全机制并建议改用 `--model sonnet`。
- 在 CI 环境中被拒绝（定义了 `CI` 或 `GITHUB_ACTIONS`）以及在 Windows 下被拒绝（未实测）。
- 变量：`AIPMT_CLAUDE_BIN`（否则依次使用 `PATH`、`~/.local/bin/claude`）、`AIPMT_CLAUDE_TIMEOUT`（每分段秒数，默认 900）、`AIPMT_CLAUDE_MAX_UTILIZATION`（默认 0.8）、`CLAUDE_CONFIG_DIR`（Claude Code 账号，绝不从项目的 `.env` 获取）；工作目录位于 `XDG_CACHE_HOME/aipmt/claude-code`（默认 `~/.cache`）。

**使用条款：责任由您的账户承担。** [Claude Code 法律条款页面](https://code.claude.com/docs/en/legal-and-compliance)并不禁止“最终用户使用自己的 Claude 订阅登录未修改的 Claude Code 二进制文件（an end user from signing in to the unmodified Claude Code binary with their own Claude subscription）”：这正是 aipmt 的运行方式，它启动官方二进制文件且绝不读取令牌。但 Anthropic“不允许第三方开发者代表其用户通过 Free、Pro 或 Max 计划凭据路由请求（does not permit third-party developers […] to route requests through Free, Pro, or Max plan credentials on behalf of their users）”，倾向于让第三方工具“包括开源项目（including open-source projects）”使用 API 密钥，并保留将其用量计入付费点数的权利（[Claude 帮助中心](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)）。目前尚无条文明确界定分发调用官方二进制文件的工具这一情况。

**数据**：对于 Free、Pro 和 Max 账户，当隐私设置允许时，模型训练也适用于 Claude Code（[数据页面](https://code.claude.com/docs/en/data-usage)）。aipmt 不保留任何本地转录记录（`--no-session-persistence`）。请勿通过其传输任何机密内容。

### 连接到自选提供商：`--use_opencode`

[OpenCode](https://opencode.ai) 是一个开源（MIT）代码代理，可路由至其内部配置的提供商：API 密钥、订阅、OpenCode Zen 网关（免费模型，免账户）或本地模型。此处对两条途径进行了端到端实测：Zen 和 Ollama。

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

`--model` 为必填项：若无此项，OpenCode 将回退到免费模型，其交互内容可能被用于训练，而此选择不应擅自替您决定。

每次调用的隔离机制：

- 内联配置优先于您的本地配置，定义了一个所有工具均被拒绝（`permission: { "*": "deny" }`）的 `aipmt` 代理，会话共享已禁用，`--pure`，绝不使用 `--auto`；
- 使用一次性空工作目录，放置了 `OPENCODE_DISABLE_PROJECT_CONFIG` 和 `OPENCODE_DISABLE_CLAUDE_CODE`——若无这些文件，OpenCode 会将当前目录的 `AGENTS.md` 以及 `~/.claude/CLAUDE.md` 注入 prompt。全局 `~/.config/opencode/AGENTS.md` 仍会被注入，OpenCode 不支持将其排除；
- 输出契约：退出代码为 0，无 `error` 事件，无工具调用，最后一步为 `stop`，文本非空，且确实加载了 `aipmt` 代理——未知的 `--agent` 不会导致 OpenCode 报错，而是会静默回退到编码代理；
- 除 OpenCode 自身的密钥 `OPENCODE_API_KEY` 外，不传递任何 `aipmt` 密钥。提供商应在 OpenCode 中配置，而非在 `aipmt` 的 `.env` 中配置。

须知事项：

- Zen 的免费模型经常变动，限制未公开记录，且交互数据可能会用于训练：适用于公开文档，不适用于私有内容。
- 本地模型必须提供至少 16k token 的上下文，因为分段长度可达 16,000 字符。Ollama 通常默认配置为 4,096：请通过带有 `PARAMETER num_ctx 32768` 的 `Modelfile` 进行调整。
- `--eco` 无效；`--reasoning_effort` 会原样作为 OpenCode 的 `--variant` 传递。
- OpenCode 会将每个会话记录在 `~/.local/share/opencode/` 中。
- 变量：`OPENCODE_BIN`（否则依次使用 `PATH`、`~/.opencode/bin/opencode`）、`OPENCODE_TIMEOUT`（每分段秒数，默认 600）。`OPENCODE_CONFIG` 会原样传递给 OpenCode。

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

`reasoningEffort: "none"` 可以关闭 Ollama 在这些模型上默认启用的思考过程，而 Modelfile 无法将其禁用。在一段六个单词的短句上实测：不加该选项时消耗 919 个思考 token 和 68 秒，加上该选项后仅消耗 9 个 token。

### 连接到 400 多个模型：`--use_openrouter`

OpenRouter 是一个按量计费的路由服务，基于统一点数额度，连接由第三方托管的模型——包括此处的其他提供商均未接入的中国开源模型。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` 为必填项。在产生任何计费之前运行的预检（preflight）会处理该路由机制的两项特性：

- **同一模型由数十家上限各异的托管商提供**——在 `z-ai/glm-5.3-flash` 上，有 23 家托管商，其中一家输出上限仅为 2,048 token。预检会读取 `/api/v1/models/{modèle}/endpoints`，排除输出低于 8,000 token 或状态处于降级的托管商，并使用 `allow_fallbacks: false` 固定其余托管商。
- **推理按输出费率计费**——在 `z-ai/glm-5.2` 回复“OK”时消耗 107 个 token，而普通输出仅 2 个。推理功能默认关闭；强制启用推理的模型将设定为其允许的最低思考程度，因为目录默认值可能会在翻译完成前耗尽输出配额。`--reasoning_effort` 仍具有最高优先级。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- 上下文窗口取自目录数据。低于 16,400 token 的模型在调用前即被拒绝：prompt 和分段需要 8,400，输出至少需要 8,000。
- 目录中不存在的 slug、目录无法访问或没有满足上限要求的托管商均会中止命令。
- 输出为空的 `finish_reason=length` 表示预算被推理消耗殆尽，并非截断：错误信息对此有明确区分。
- `--eco` 无效。
- 变量：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>）、`OPENROUTER_BASE_URL`（默认 `https://openrouter.ai/api/v1`，必须为 `https://`）、`OPENROUTER_TIMEOUT`（默认 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（默认 30）。

### 翻译说明

`--add_translation_note` 会添加一条说明，位置可设为 `bottom`（默认）、`top`（位于 front matter 之后）或 `both`（`--note_position`），格式可设为 `legacy`（粗体段落，默认）或 `marker`（`--note_format`）。`marker` 格式是一个不可见的 Markdown 引用定义：`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`，后接粗体引用：既可在 GitHub 上直观阅读，也可在构建时由 remark 插件进行解析处理。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 详细评测数据

所有测量数据均来自使用 `aipmt` 实际执行的翻译，目标为十四种语言：en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi。**已写入**统计通过安全检查并成功生成的文件数；**无偏差**统计 `scripts/compare_structure.py` 未检测出任何差异的文件数——节数、子标题数、链接数、唯一下载 URL 数、代码块数、行内代码数、表格行数、引用块数和粗体词数完全一致。

“无偏差”仅代表“未检测到差异”，并不等同于“完全相同”：比对工具只统计元素数量而不读取其具体内容。它既不会报告某个 4 级标题被删除、行内代码文本被替换、标记互换，也不会发现内部链接多生成了一个括号（如 `[texte]((#ancre))` 导致链接失效）——并且它不评估语言质量。

### 密集技术资讯文章，模式 `--news`

选自 [jls42.org 的 AI 技术资讯](https://jls42.org/fr/news) 的一期内容：589 行，140 个链接，21 个小节，3 处受保护的英文引用。测试周期为 2026 年 9 月 4 日至 5 日。

| 模型 | 访问方式 | 已写入 | 无偏差 | 中位数/语言 |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
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
| `ollama/gpt-oss-20b-32k` | 本地 | 10/14 | ❌ 7/14 | 12 分 39 秒 |
| `mistral-large-latest` | Mistral API | 11/14 | ❌ 5/14 | 5 分 32 秒 |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter | 4/14 | ❌ 3/14 | 37 分 27 秒 |
| `grok-4.6` (`--use_grok_cli`) | Grok 订阅 | 1/14 | ❌ 1/14 | 23 分 11 秒 |
| `opus` (`--use_claude_code`) | Claude 订阅 | 0/14 | ❌ 0/14 | — |

9 月 9 日在同系列另一期简报（356 行）上对 Grok 进行了重新测试：14 种语言中写入 9 种，8 种无偏差。表头正是采用这一数据。未计入三次中断的测试：`qwen3.5-27b`（9 种语言）和 `kimi-k2.6`（4 种）因额度不足中断，`z-ai/glm-5.3-flash` 的两次失败则是由于推理设置问题，该问题随后已被提供商修复。OpenRouter 各项数据是在路由默认设置下测得的，早于 `--use_openrouter` 的引入；使用随附提供商重新测试的 `z-ai/glm-5.2` 同样交出了 14/14 的成绩。这些数据于 9 月 10 日使用当前的比对工具重新计算：`qwen3.8-flash` 和 `qwen3.7-flash` 较首次发布时各增加了一种达标语言，其他保持不变。

`--use_antigravity` 相关项目于 9 月 26 日在同一篇文章上进行了测试，四路并行翻译：上午测试 `gemini-3.7-flash-medium`，下午测试 `gemini-3.8-flash-medium`。在英文翻译中，两者均自行移除了引用下方的三行法文翻译，且未捏造任何标记，英文引用完好无损：回退清理机制无需介入。在 `--eco`（`gemini-3.7-flash-low`）模式下，仅针对四种语言（en、ja、ar、hi）测试：4 种全部成功写入，且全部无偏差，耗时中位数为 1 分 52 秒。同日针对 9 月 25 日更新的一期简报（438 行，2 处英文引用）进行了复测，在博客外部通过 `gemini-3.7-flash-medium` 进行翻译：14 种语言全部成功写入，全部无偏差，每种语言耗时 87 至 128 秒。

`--use_claude_code` 相关项目于 9 月 26 日在同一篇文章上进行了测试，四路并行翻译，思考程度设为 `low`。使用 `sonnet` 时，十四种语言中的英文引用均完好无损，且在英文翻译中，模型自行移除了法文翻译行，未捏造任何标记。`opus` 未能成功写入任何一种语言：在每种语言中，其安全机制均在最后一个分段截断了响应，原因是一则关于结合位点生成的 279 个分子的简报。单独发送该简报时，会被“生物（bio）”分类规则拦截拒绝；而 `sonnet` 在所有语言中均完成了翻译。`haiku` 写入了全部十四种语言；但在三种语言（en、pl、ro）中，有一个小节标题从 2 级变成了 1 级。它会在无法阻止的情况下进行推理——占其输出 token 的 61%——因此耗时比 `sonnet` 增加了一倍以上。

`claude-sonnet-5-5`、`claude-haiku-5-5` 和 `claude-haiku-4-5` 于 10 月 18 日通过 Anthropic API 在同一篇文章上进行了测试，每个模型四路并行翻译。Sonnet 5.5 不允许关闭其思考过程：aipmt 向其发送所允许的最低设置，其返回的响应中不包含任何思考过程。它在无偏差且无需重译分段的情况下完成了全部十四种语言的写入；在英文翻译中，它自行移除了法文翻译行，未捏造任何标记，各处的英文引用均完好无损。Haiku 5.5 在启用自适应思考模式下进行了测试：关闭思考时，它会残留大段法文未译，导致安全检查拒绝——14 种语言中仅成功写入 3 种。两个 Haiku 模型都在同一篇简报上出现问题：Haiku 5.5 在日语、韩语和中文中更改了标题级别或出现了标题重复，Haiku 4.5 在七种语言中将其升级为 1 级标题，并在日语中将其保留为法文。针对两篇文档的十四种语言翻译，Haiku 4.5 耗费 3.67 美元，Haiku 5.5 耗费 0.57 美元，Sonnet 5.5 耗费 9.21 美元。

### 本项目的 README，标准 Markdown

2026 年 9 月 9 日冻结版本：785 行，285 处行内代码，40 处代码块闭合标记，89 行表格。4 个并行翻译。

| 模型 | 已写入 | 无偏差 | 中位数/语言 | 差异内容 |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14 | ✅ 14/14 | 1 分 43 秒 | 无 |
| `opus` (`--use_claude_code`) | 14/14 | ✅ 14/14 | 1 分 48 秒 | 无 |
| `haiku` (`--use_claude_code`) | 14/14 | ✅ 14/14 | 4 分 02 秒 | 比较器无差异；内部链接重复（en） |
| `claude-sonnet-5-5` | 14/14 | ✅ 14/14 | 1 分 18 秒 | 无 |
| `claude-haiku-4-5` | 14/14 | ✅ 14/14 | 2 分 06 秒 | 无 |
| `gemini-3.7-flash` | 14/14 | ⚠️ 13/14 | 36 秒 | 粗体词（ja） |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14 | ⚠️ 13/14 | 1 分 22 秒 | 粗体词（ko） |
| `sonnet` (`--use_claude_code`) | 14/14 | ⚠️ 13/14 | 2 分 20 秒 | 表格中有一行与上一行粘连（ar） |
| `claude-sonnet-5` | 14/14 | ⚠️ 12/14 | 2 分 56 秒 | 链接（sv），粗体词（zh） |
| `gpt-5.6-sol` (`--use_codex`) | 14/14 | ⚠️ 12/14 | 6 分 46 秒 | 粗体词（ar, ja） |
| `z-ai/glm-5.2` (OpenRouter) | 14/14 | ⚠️ 11/14 | 2 分 34 秒 | 粗体词（hi, ja, ko） |
| `qwen/qwen3.7-flash` | 14/14 | ⚠️ 10/14 | 2 分 17 秒 | 阿拉伯语中添加了 40 处行内代码；粗体（hi, ja, ko） |
| `claude-haiku-5-5` | 12/14 | ❌ 12/14 | 1 分 14 秒 | 拒绝 2 种语言（ar, hi）：返回时丢失了行内代码 |
| `mistral-large-latest` | 14/14 | ❌ 1/14 | 2 分 44 秒 | 丢失一个章节（ar, hi, ko）；添加了代码块（ja, ko, ro, zh） |

两次中断的测试轮次未予计入：Grok 在完成十二种语言（十一种无偏差）后 CLI 会话超时；`qwen3.8-flash` 在完成两种语言后遭遇托管方的 HTTP 429。`opencode/mimo-v2.5-free` 和 `ollama/gpt-oss-20b-32k` 未在此版本上重新测试；在 9 月 4 日至 5 日少 277 行的版本上，它们各自在 14 个翻译中完成了 9 个，其中无偏差的分别为 7 个和 1 个。

涉及 `--use_antigravity` 和 `--use_claude_code` 的行并非在冻结版本上测得，而是在 9 月 26 日随 1.14.0 发布的版本上测得——而 `claude-sonnet-5-5`、`claude-haiku-5-5` 和 `claude-haiku-4-5` 对应的行则是在 10 月 18 日基于相同版本测得：600 行，257 处行内代码，30 处代码块闭合标记，85 行表格。该版本少了 185 行，不能直接与其他各行进行逐项比较；但这些行彼此之间具有可比性。关于比较器未校验的内部链接，`gemini-3.8-flash-medium` 在十四种语言中均保持完好，`gemini-3.7-flash-medium` 在意大利语中破坏了链接；`sonnet` 和 `opus` 在所有语言中均保持完好，`haiku` 在英语中重复了链接；`claude-sonnet-5-5` 和 `claude-haiku-4-5` 在十四种语言中均保持完好，`claude-haiku-5-5` 则在其生成的十二种语言中保持完好。

### 知名项目的四个 README

FastAPI、Ollama、tldr-pages 和 Vue.js，原样取自 GitHub——比前两份文档更容易。本轮测试针对的是表现欠佳的模型；Gemini 用作基准对照。

| 模型 | 范围 | 已写入 | 无偏差 |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash` | 4 个项目 × 14 种语言 | 56/56 | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 个项目 × 14 种语言 | 55/56 | ❌ 47/56 |
| `grok-4.6`（订阅） | 4 个项目 × ar, hi, ja, zh | 16/16 | ❌ 14/16 |
| `ollama/gpt-oss-20b-32k` | 4 个项目 × ar, hi, ja, zh | 15/16 | ❌ 9/16 |

### 这些测试所不能代表的

- **并非详尽的排名**：仅 OpenRouter 就提供了四百多个模型，此处仅测试了约十五个。
- **耗时仅供参考**：各轮次测试采用三到六个并行翻译，且服务商的吞吐速率在一天之中会有所波动。
- **带有时间局限性的观察**：同名模型会发生变化，且您的文档与我们的文档并不相同。

要在您自己的文档上使用文件的冻结副本重新进行测试：

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

这两行都是必需的：若没有 `pip install -e .`，`python -m aipmt` 会返回 `No module named aipmt`。

质量保证工具，可选但推荐：

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

仓库中的 28 个翻译（README 和 CHANGELOG，共十四种语言）可通过 `./regen_translations.sh --force` 重新生成——默认在 ChatGPT 订阅上使用 Codex 和 `gpt-5.6-sol`，4 个并行任务。`REGEN_PROVIDER` 和 `REGEN_MODEL` 可更改运行路径：`antigravity` 仍使用订阅（Google 订阅），无需特许即可执行；计费 API（`openai`、`gemini`、`grok`、`openrouter`）若没有 `REGEN_ALLOW_PAID_API=1` 则会被拒绝；`REGEN_JOB_TIMEOUT` 对每个任务设置时间上限（600 秒，在 Codex 和 Antigravity 上为 1 800 秒）。关于工具的详细说明见 `CLAUDE.md`。

## 使用此脚本的项目

- **[jls42.org](https://jls42.org)** — 以 15 种语言发布的个人博客。其[每日 AI 资讯跟踪](https://jls42.org/fr/news)每天都由该工具翻译，并作为上述测试的基准文档。

## 作者

Julien LE SAUX
电子邮箱：contact@jls42.org

## 许可证

GNU GENERAL PUBLIC LICENSE Version 3。参见 [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)。

## 免责声明

本程序按 GPL v3 第 15 条和第 16 条的条款发布，**不附带任何担保**：按“原样”提供，不包含适销性或特定用途适用性的担保，作者对因使用本程序而导致的任何损失概不负责。许可证正文效力优先于本概述。

- **发布前请仔细通读。** 保护机制涵盖代码块、行内代码、URL、锚点以及 `--news` 模式下的引用——但不涵盖标题、表格、front matter 或句子的含义。
- **您的文档会被发送至所选的服务商**，并遵循其使用条款与数据政策。某些免费模型可能会将您的交互数据用于模型训练，而 Antigravity 的条款允许 Google 复用这些数据并进行人工审核（即使付费订阅也是如此）；本地模型是唯一不让任何数据离开您机器的方式。
- **API 调用将向您收取费用。** 本程序不会对支出设定上限：长文档、失败重试或大量进行推理的模型均会产生更高费用。
- **发布的测试结果均为带有时间局限性的观察**，并非保证。

所提及的产品和公司名称均为其各自所有者的财产。本项目与其中任何一家均无关联。

**使用 gemini-3.8-flash-medium 从法语翻译成中文的文章。**
