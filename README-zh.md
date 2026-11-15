# 人工智能驱动的 Markdown 翻译器

🌍 [法语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [英语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [西班牙语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [德语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [韩语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [阿拉伯语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [印地语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [意大利语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [荷兰语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [波兰语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [葡萄牙语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [罗马尼亚语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [瑞典语](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 代码质量</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="质量门禁状态"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="安全性评级"></a>
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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="重复行比例 (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="技术债务"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="代码行数"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy 徽章"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

将 Markdown 文件从一种语言翻译为另一种语言，同时保留其
结构：代码块、行内代码、URL、锚点、表格和前置
元数据。提供十一种模型调用方式——五种 API、四种不按用量
计费的订阅、两种路由服务——并公开测量结果，展示每个
模型实际保留了哪些内容。

## 概览

- **十一种提供商接入途径**：OpenAI、Mistral、Claude、Gemini 和 Grok API；
  不按用量计费的 ChatGPT（Codex）、Grok、Google（Antigravity）和 Claude（Claude
  Code）订阅；OpenCode（开源、免费或本地运行）和 OpenRouter
  （超过 400 个模型）路由服务。
- **避免因标记丢失而产生错误**：代码块、行内代码、
  URL、锚点和引文会在调用前替换为标记，并在
  返回后进行检查。只要缺少一个标记，就不会写入文件。
- **长文档**：根据模型的上下文窗口分段。
- **`--news` 模式**：保护英文引文，并按语言处理
  旗帜，适用于资讯文章。
- **`--eco` 模式**：使用速度更快、费用更低的模型。
- 可选的**翻译说明**，可置于顶部、底部或两处。

## 安装

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

需要 Python 3.11 或更新版本。从仓库安装的方法见
[贡献指南](#参与贡献)。

## 配置

密钥从以下三个位置读取，优先级从高到低；每个位置
只补充前一个位置未提供的值。

|     | 位置                                            | 用途                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 环境变量                     | CI、容器、临时覆盖 |
| 2   | 当前目录（或父目录）中的 `.env` | 项目专用密钥            |
| 3   | `~/.config/aipmt/.env`                        | 配置一次，处处可用       |

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

可以使用 `GEMINI_API_KEY` 代替 `GOOGLE_API_KEY`。用户
配置文件遵循 `XDG_CONFIG_HOME`（仅限绝对路径），在 Windows 下遵循 `%APPDATA%`。
没有密钥时，命令会列出这三个位置。

**项目的 `.env` 既不能重定向调用，也不能选择
执行的程序。** 它只提供密钥，不提供目标地址或可执行文件：其中所有
属于 `_BASE_URL`、`_API_BASE`、`_ENDPOINT` 或 `_BIN` 的变量（`CODEX_BIN`、
`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`）、`GROK_HOME`、代理（`HTTP_PROXY`、
`HTTPS_PROXY`、`ALL_PROXY`）、证书存储（`SSL_CERT_FILE`、
`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）以及 `XDG_CONFIG_HOME` /
`APPDATA` 都会被忽略，并发出警告。克隆的仓库不应
能够窃取您的密钥，也不应在首次翻译时让您运行
它自己的程序。读取此文件时也不会进行变量插值：
`NOM=${OPENAI_API_KEY}` 不会在其中复制密钥。请将这些变量设置在
环境中或 `~/.config/aipmt/.env` 中。

可选变量：`XAI_BASE_URL`（默认值 `https://api.x.ai/v1`）、
`CLAUDE_TIMEOUT`（每次调用的秒数，默认值 900）、`CODEX_BIN`、`CODEX_TIMEOUT`
（默认值 600）、`GROK_BIN`、`GROK_HOME`（默认值 `~/.grok`）、`GROK_TIMEOUT`
（默认值 900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（默认值 900）、
`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（默认值 600）、`OPENROUTER_BASE_URL`
（必须提供 `https://`）、`OPENROUTER_TIMEOUT`（默认值 900）、
`OPENROUTER_PREFLIGHT_TIMEOUT`（默认值 30）。各变量的详细说明见
对应提供商的章节。

## 快速入门

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

将 `document.md` 翻译成西班牙语，会在 `--target_dir` 中生成 `document-es.md`；
使用 `--include_model` 时，则生成 `document-es-gpt-5.6-terra.md`。扩展名
始终变为 `.md`——`article.mdx` 会变为 `article-en.md`——但使用
`--keep_filename` 时会保留原文件名。已有的译文
会被跳过，除非使用 `--force`。

退出码：`0` 表示全部成功或已跳过，`1` 表示仍有文件
失败（列表输出到标准错误），`2` 表示配置有问题。
失败的文件绝不会被写入，即使失败发生在写入过程本身：
内容会先写入旁边的临时文件，再重命名。重新运行即可。

## 如何选择模型

测试使用两份真实文档，每个模型都将其翻译为相同的十四种语言。
**数字表示十四种语言中，译文成功写入且
与源文档相比没有任何差异的语言数量。**

| 模型                | 接入方式                 | 内容密集的资讯文章 | 本 README    | 差异内容及涉及的语言数量                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google 订阅（Antigravity）   | ✅ 14/14                | ✅ 14/14     | 两份文档均无差异                                                                                                                                 |
| **Claude Sonnet 5.5** | Anthropic API 密钥                 | ✅ 14/14                | ✅ 14/14     | 两份文档均无差异                                                                                                                                 |
| **Gemini 3.7 Flash**  | Google API 密钥                    | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种：多了一个加粗词（ja）                                                                                                                      |
| **Gemini 3.7 Flash**  | Google 订阅（Antigravity）   | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种：少了一个加粗词（ko）                                                                                                                     |
| **GPT-5.6 Sol**       | ChatGPT 订阅或 OpenAI 密钥 | ✅ 14/14                | ⚠️ 12/14     | 14 种语言中有 2 种：少了一个加粗词（ar、ja）                                                                                                                |
| **GLM-5.2**           | OpenRouter 密钥                    | ✅ 14/14                | ⚠️ 11/14     | 14 种语言中有 3 种：少了一个加粗词（hi、ja、ko）                                                                                                            |
| Claude Sonnet 5       | Claude 订阅（Claude Code）   | ⚠️ 13/14                | ⚠️ 13/14     | 文章的 14 种语言中有 1 种：多了一个加粗词（zh）；本 README 中有 1 种：一行表格粘连到上一行，显示时被隐藏（ar）            |
| Claude Haiku 4.5      | Claude 订阅（Claude Code）   | ⚠️ 11/14                | ✅ 14/14     | 文章中有 3 种语言：一个章节标题变成一级标题（en、pl、ro）；本 README 的比较工具未发现差异，但内部链接重复出现了英文版本 |
| Claude Sonnet 5       | Anthropic API 密钥                 | ⚠️ 11/14                | ⚠️ 12/14     | 文章中有 3 种语言：多出一个代码块（es、de、hi）；本 README 中有 2 种：一个链接丢失标记（sv）、一个词被加粗（zh）                              |
| Claude Haiku 4.5      | Anthropic API 密钥                 | ⚠️ 7/14                 | ✅ 14/14     | 文章中有 7 种语言：一个章节标题变成一级标题——日语版本中该标题仍为法语；本 README 无差异                                              |
| Claude Haiku 5.5      | Anthropic API 密钥                 | ⚠️ 11/14                | ❌ 12/14     | 文章中有 3 种语言：一个章节标题改变层级或重复出现（ja、ko、zh）；本 README 中有 2 种语言被拒绝，原因是行内代码丢失（ar、hi）    |
| Qwen 3.7 Flash        | OpenRouter 密钥                    | ❌ 8/14                 | ⚠️ 10/14     | 文章中有 1 种语言被拒绝，另有 5 种存在差异；本 README 中约四十个词被设为 `code`（ar）                                                    |
| Grok 4.6              | Grok 订阅                   | ❌ 8/14                 | 未评分     | 14 种语言中有 5 种因未返回行内代码和 URL 而被拒绝；荷兰语版本各方面都有差异                                                               |
| GPT-OSS 20B           | 本地模型（Ollama）             | ❌ 7/14                 | 未重新测量 | 14 种语言中有 4 种被拒绝：模型保留了法语段落，被检查机制拦截                                                                  |
| MiMo v2.5（免费）   | OpenCode Zen，无需账户         | ❌ 11/14                | 未重新测量 | 1 种语言被拒绝；波兰语版本丢失一个章节                                                                                                                  |
| Mistral Large         | Mistral API 密钥                   | ❌ 5/14                 | ❌ 1/14      | **整个章节消失**：文章中有 1 种语言（hi），本 README 中有 3 种（ar、hi、ko）——此外，文章还有 3 种语言被拒绝                                |
| DeepSeek V4 Flash     | OpenRouter 密钥                    | ❌ 3/14                 | 未重新测量 | 14 种语言中有 10 种被拒绝；每种语言耗时 37 分钟                                                                                                                 |
| Claude Opus 5.5       | Claude 订阅（Claude Code）   | ❌ 0/14                 | ✅ 14/14     | 由于一则生物学短讯，Opus 的安全防护机制拒绝了文章的全部 14 种语言翻译；本 README 无差异                                               |

|     | 符号含义                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 十四种语言全部完成翻译，且与源文档相比没有任何差异                                                                                                                                       |
| ⚠️  | 十四种语言全部完成翻译；差异仅涉及**标记格式**——一个加粗词、一个 `code`、一个丢失方括号的链接。没有缺失任何文本、URL、代码块或章节 |
| ❌  | 至少有一种语言无法完成翻译——文件被拒绝写入——**或者**已写入的文件缺少内容                                                                      |

需要了解的要点：

- **翻译被拒绝并不意味着译文受损。** 如果返回结果中
  缺少标记，就不会写入文件，该语言会被计为
  拒绝。Grok 翻译文章时就出现了这种情况：在五种非拉丁文字的语言中，
  第一个分段就丢失了四处行内代码和
  三个 URL。
- **模型可能因为一句话而拒绝整份文档。** Opus 5.5
  翻译本 README 时没有任何差异，却无法翻译任何资讯文章：
  它的安全防护机制会因一则生物学短讯而中止响应。文件不会
  被写入，aipmt 会说明原因。
- **这层保护不涵盖标题、表格、前置元数据或
  文本。** 如果模型删除一个章节，工具仍会照常写入
  文件——Mistral 就出现了这种情况。这些元素无法
  用标记替换，当前的检查机制也不会检查它们；
  `scripts/compare_structure.py` 能检测出章节丢失，但只能在事后发现。
- **Grok 在本 README 上没有评分**：它的 CLI 会话在完成十二种
  语言后过期，其中十一种没有差异。中断的测试不予评分。
- **文档密度比语言更重要。** Grok 能处理
  普通 README，但面对链接密集的文章就会失常，
  荷兰语也不例外。

日期和文档：“本 README”列于 2026 年 9 月 9 日
使用本文件的固定修订版进行测量（785 行、285 处行内代码、89 行
表格），此后文件有所修改——但 Antigravity 和 Claude Code 各行除外，
它们于 9 月 26 日使用随 1.14.0 发布的较短修订版
进行测量（600 行、257 处行内代码、85 行表格）；通过 API 调用的 Claude
Sonnet 5.5、Haiku 5.5 和 Haiku 4.5 各行则于 10 月 18 日使用
同一修订版进行测量。“内容密集的资讯文章”列来自
9 月 4 日和 5 日对一篇 589 行文章的测试，但 Grok 行除外，
它于 9 月 9 日使用同一资讯系列的另一期文章重新测量；Antigravity 和
Claude Code 各行于 9 月 26 日使用同一篇文章测量，这三行
Claude 则于 10 月 18 日测量。完整表格、耗时和测试方法见
[详细测量结果](#详细测量结果)。
## 所有选项

| 选项                   | 说明                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 要翻译的单个 Markdown 文件（替代 `--source_dir`）                                             |
| `--source_dir`           | 包含 Markdown 文件的源目录（默认：`content/posts`）                                   |
| `--target_dir`           | 译文文件的输出目录（默认：`traductions_en`）                                    |
| `--source_lang`          | 源语言（默认：`fr`）                                                                                  |
| `--target_lang`          | 目标语言（默认：`en`）                                                                                   |
| `--model`                | 指定要使用的模型                                                                                  |
| `--eco`                  | 使用经济型模型                                                                              |
| `--use_mistral`          | 使用 Mistral AI API                                                                                     |
| `--use_claude`           | 使用 Claude API                                                                                         |
| `--use_gemini`           | 使用 Gemini API                                                                                         |
| `--use_grok`             | 使用 xAI（Grok）API — 需要 `XAI_API_KEY`                                                           |
| `--use_codex`            | 使用 Codex CLI，消耗 ChatGPT 订阅配额                                                    |
| `--use_grok_cli`         | 使用 Grok CLI，消耗 Grok 订阅配额                                                        |
| `--use_antigravity`      | 使用 Antigravity CLI（`agy`），消耗 Google AI Pro 或 Ultra 订阅配额                       |
| `--use_claude_code`      | 使用 Claude Code CLI（`claude -p`），消耗 Claude Pro 或 Max 订阅配额                      |
| `--use_opencode`         | 使用开源的 OpenCode，连接到 OpenCode 中配置的提供商；需要 `--model provider/modèle` |
| `--use_openrouter`       | 使用 OpenRouter — 需要 `OPENROUTER_API_KEY` 和 `--model fournisseur/modèle`                          |
| `--force`                | 强制重新翻译                                                                                       |
| `--keep_filename`        | 保留原始文件名                                                                          |
| `--news`                 | 新闻模式：保护英文引文，按语言管理标志                                      |
| `--add_translation_note` | 添加翻译说明                                                                                |
| `--note_position`        | 说明位置：`top`、`bottom`（默认）或 `both`                                                     |
| `--note_format`          | 说明格式：`legacy`（默认，加粗段落）或 `marker`                                            |
| `--include_model`        | 在输出文件中包含模型名称                                                            |
| `--reasoning_effort`     | GPT-5.x 推理强度：`none`/`low`/`medium`/`high`/`xhigh`                                         |

这九个 `--use_*` 标志互斥：同时使用其中两个会被
拒绝。

## 提供商

### 通过 API：OpenAI、Mistral、Claude、Gemini、Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` 会切换到各提供商的经济档位。

| 提供商    | 高质量（默认）                                                     | 经济型（`--eco`）      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.8-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol`（也可通过 `--model` 使用 `gpt-5.6-sol`、`terra` 和 `luna`） | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | 相同 — `--eco` 无效 |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`，推理强度为 `low`                                               | 相同 — `--eco` 无效 |
| OpenCode    | 必须指定 `--model provider/modèle`                                | 相同 — `--eco` 无效 |
| OpenRouter  | 必须指定 `--model fournisseur/modèle`                             | 相同 — `--eco` 无效 |

截至 1.17.1 版本一直作为默认模型的 Gemini 3.7 Flash 已弃用：Google 改为提供
Gemini 3.8 Flash，但仍接受 `--model gemini-3.7-flash`。
Gemini API 出现临时故障（503、429、超时）时，会在
10、20、40 秒后重试调用，最多三次。一次尝试
若始终未收到响应，会在 5 分钟后放弃，再按同样方式重试：
因此，即使服务器毫无响应，该分段也会在大约二十分钟内
失败，而不会无限期阻塞。

### 使用 ChatGPT 订阅：`--use_codex`

调用官方 Codex CLI：翻译消耗
ChatGPT 订阅配额，无需 API 密钥，也不按用量计费。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 依次在 `CODEX_BIN`、`PATH` 和
  `openai-codex-cli-bin` 软件包中查找可执行文件。绝不读取 `~/.codex/auth.json`。
- 从子进程环境中移除 `OPENAI_API_KEY` 和 `CODEX_API_KEY`：
  即使存在密钥，也绝不会切换到 API。
- 每个分段至少消耗 5 小时窗口内的一条“消息”；
  如果验证失败并重试，则消耗两条。OpenAI 提供的估算为：
  Plus 套餐下，`gpt-5.6-luna`（`--eco`）每 5 小时可用 250-2 000 条消息，
  `gpt-5.6-sol` 可用 10-100 条。
- 截至 1.16.3 版本一直作为默认模型的 `--model gpt-5.6-sol`，以及 `--model gpt-5.6-terra`
  和 `--model gpt-5.6-luna`，也通过订阅使用。
- 服务器返回 429 不会导致文件丢失：Codex 会自行重新连接，
  aipmt 会等待本轮结束；如果最终仍返回 429，该分段
  会在 30 秒、60 秒后重试。若账户无权使用某个模型，则返回 400，提示
  “使用 ChatGPT 账户运行 Codex 时不支持此模型”。
- 比 API 更慢，且文档越长，差距越大：对于此 README，
  使用 `gpt-5.6-sol` 时，每种语言的耗时中位数为 6 分 46 秒，
  而 `gemini-3.7-flash` 为 36 秒。
- 禁止在 CI 中使用（已定义 `CI` 或 `GITHUB_ACTIONS`）：订阅通过
  个人会话文件进行身份验证，该文件不应放在共享的
  运行器上。
- 变量：`CODEX_BIN`、`CODEX_TIMEOUT`（每个分段的秒数，默认 600）。

### 使用 Grok 订阅：`--use_grok_cli`

原理相同，使用官方 Grok Build CLI，消耗 SuperGrok 或
X Premium+ 订阅配额。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **隔离能力弱于 Codex。** Grok 的操作系统沙箱在
  许多较新的 Linux 电脑上无法生效（AppArmor、容器运行时
  套接字），无法应用的配置会静默启动为不受隔离的状态。
  因此，脚本默认不请求任何配置，并会明确提示，
  转而依靠 CLI 的 `--deny` 规则，包括兜底规则 `*` — 这是唯一
  会拒绝启动，而不是悄悄移除保护的防护层。
  `GROK_TRANSLATE_SANDBOX=read-only` 强制要求操作系统沙箱；如果机器无法满足要求，
  启动就会失败。
- 配额按周计算，与 Chat、Imagine 和 Voice 共享，且没有
  命令可以查询：批量翻译可能在没有提示的情况下
  占用对话配额。
- 变量：`GROK_BIN`、`GROK_HOME`（CLI 目录，默认 `~/.grok`）、
  `GROK_TIMEOUT`（默认 900）、`GROK_TRANSLATE_SANDBOX`。

### 使用 Google 订阅：`--use_antigravity`

原理相同，使用 Antigravity 官方 CLI `agy`：对于订阅 Google
AI Pro 或 Ultra 的用户，翻译消耗订阅配额，
而不是按 token 计费。这是使用该配额的唯一途径：自 2026 年 6 月 18 日起，
Gemini CLI 已不再为这些账户提供服务
（[公告](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)），
而 Antigravity SDK 仅接受 API 密钥或 Google Cloud 项目。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **不保留任何付费调用途径。** agy 仅从您的环境中接收
  一组固定的变量 — `PATH`、语言和时区、
  终端、身份、代理和证书、会话总线 — 不接收任何密钥：
  它的多个变量会在没有任何提示的情况下改变调用途径（实测：
  其中一个会将文档发送到第三方网关，另一个会发送到
  计费的 Google Cloud 项目），而使用排除列表时，每次复查都会发现遗漏。
  在处理任何分段之前，不消耗配额的 `agy -p /config` 必须显示
  付费人工智能点数已停用，且没有 API 密钥或 Google Cloud 项目 —
  缺少设置也视为拒绝条件 — 否则不进行任何翻译；随后，每次调用的日志
  都必须证明使用了订阅（`authMethod=consumer`），否则
  拒绝接受响应。
- **隔离。** 每次调用都在私有、临时的个人目录中运行，
  使用没有工具的翻译代理：您的 agy 设置、规则、
  插件、MCP 服务器和钩子均不会进入其中，也不会向您的
  历史记录添加内容；登录信息始终保留在钥匙串中，aipmt 从不读取。
  找不到指定代理时，agy 会静默退回到其编程代理
  及其工具：必须有一整行日志确认使用了正确的代理 —
  文档中引用该消息不能替代这条日志 — 否则拒绝处理。
- **平台**：Linux，且会话中有钥匙串（D-Bus 会话总线、
  Secret Service）；也允许 macOS，但尚未在其上实测。禁止
  在 Windows 上使用，因为 agy 在该平台上不读取用于隔离各次调用的变量；
  也禁止在没有会话总线的 Linux 环境中使用 — 如 SSH 会话、容器、服务器：
  agy 会将令牌存储在 `~/.gemini` 中的文件里，而隔离会隐藏该文件。
  程序会在启动前拒绝运行并说明原因，而不是先等待一分钟
  登录验证码。
- **模型**：使用 `agy models` 中的模型。Gemini 的名称中包含推理强度
  （`gemini-3.8-flash-medium` 等）：不带后缀的名称会在调用前被拒绝，
  `--reasoning_effort` 无效。默认使用 `gemini-3.8-flash-medium`，
  在 `--eco` 模式下使用 `gemini-3.7-flash-low`；确定这些默认值的测试
  见[详细测量](#详细测量结果)。Claude 和 GPT-OSS
  各自拥有小得多的独立配额：实测每次调用约消耗
  5 小时窗口配额的 1 %，而 Flash 为 0,05 %。
- **配额**：每组都有一个 5 小时窗口和一个每周窗口，
  按 token 成本比例扣减。在作者账户上实测：每百万源字符，
  `gemini-3.8-flash-medium` 约消耗 5 小时窗口配额的
  16 个百分点，`gemini-3.7-flash-medium` 为 14 个百分点，
  低推理强度为 7 至 8 个百分点 — 因此，一份 40 000 字符的 README
  会消耗略高于半个百分点。每周上限则取决于订阅档位。重试遵循
  agy 声明的可重试条件；如果没有此类声明，配额窗口耗尽后绝不
  重试：每个文件都会失败，直到 `/usage` 显示的
  重置时间。
- **比 API 更慢**：对于测量中使用的内容密集文章，每种语言的
  耗时中位数为：`gemini-3.8-flash-medium` 下 3 分 59 秒，
  `gemini-3.7-flash-medium` 下 3 分 14 秒，而通过 API 使用 Gemini 3.7 Flash 为 1 分 18 秒。
- **中断**：按 Ctrl-C 或关闭终端，会随命令一起停止 agy，
  避免它继续消耗您的配额完成本轮；Codex、Grok CLI 和 OpenCode
  也采用相同行为。在 `nohup` 下，翻译会继续。
- 禁止在 CI 中使用（已定义 `CI` 或 `GITHUB_ACTIONS`）：登录信息保存在
  个人钥匙串中。在运行器上，请使用 `--use_gemini` 配合 `GOOGLE_API_KEY`。
- 变量：`AGY_BIN`（否则依次查找 `PATH`、`~/.local/bin/agy`）、
  `AGY_TIMEOUT`（每个分段的秒数，包含启动时间，默认 900）。

**使用条款：责任由您的账户承担。**
[Antigravity 使用条款](https://antigravity.google/terms)（第 6 节）及其
[常见问题](https://antigravity.google/docs/faq/)禁止通过第三方软件
使用 Antigravity 登录信息访问服务 — 其中明确提到了 Claude Code、
OpenClaw 和 OpenCode — 违者可能导致账户被停用。aipmt
既不读取也不复用令牌：它通过 Google 为脚本和 CI
记录的[无界面模式](https://antigravity.google/docs/cli/headless/)
启动官方可执行文件。一位 Google 成员认为，从本地脚本中运行
`agy -p` 来完成自己的工作属于“标准”用法
（[官方论坛，2026 年 9 月 25 日，不具合同效力的回复](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）；
但没有任何文本明确界定像本工具这样对外分发的工具是否属于此情形。

**仅限公开文档。** 根据同一条款的第 5 节，
交互内容 — 提示词、响应、元数据 — 可能被用于改进
Google 产品和机器学习，也可能由人工
审阅，付费订阅同样如此。退出此用途需要通过
`enableTelemetry` 设置，其效果没有文档说明，aipmt 也不会设置它；您的
agy 设置不会带入隔离环境。请勿通过此途径处理任何机密内容。
### 使用 Claude 订阅：`--use_claude_code`

`claude` 是 Claude Code 的官方 CLI，在 `-p` 模式下也遵循相同原则：对于
付费使用 Claude Pro 或 Max 的用户，翻译会消耗订阅配额，
而不是按 token 计费。请勿将其与
按用量计费的 Anthropic API `--use_claude` 混淆。

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **所有付费通道均已关闭，每次调用都会验证这一点。** Claude
  Code 只能从环境中接收一组封闭的变量列表，其中既没有
  API 密钥、令牌、云服务提供商，也没有启动 aipmt 的 Claude Code
  会话标记。在处理第一个片段之前，`claude auth status` 必须
  显示通过订阅登录，且没有 Console 密钥；不消耗任何配额的 `/usage`
  必须确认这一点；此后每次调用也会在初始化事件中确认，
  否则响应会被拒绝。
- **关闭“额外用量”**（claude.ai，设置 → 用量），才能
  保持零欧元费用：开启后，它会在某个时间窗口的配额耗尽时接管，
  并在不显示错误的情况下收费。一旦某次调用的配额报告表明出现这种情况，aipmt 就会停止翻译，
  但该次调用已经计费。
- **配额与您的 Claude Code 会话共享。** 每次调用都会报告
  5 小时窗口和每周窗口的使用情况；超过 80 %
  （`AIPMT_CLAUDE_MAX_UTILIZATION`）后，就不会再启动新的片段，以免
  耗尽您工作所需的配额。
- **隔离。** 每次调用都在一个私有的临时目录中运行，
  不使用工具，并采用不加载自定义配置的模式：不会加载您的 `CLAUDE.md`、插件、
  hooks、MCP 服务器或设置，也不会保留任何
  会话内容。附件功能已关闭：文档中的 `@chemin`
  仍然只是文本，不会打开任何文件（已经实测）。
- **模型**：默认为 `sonnet`，推理强度为 `low`，在 `--eco` 下也一样：
  `--eco` 对这条路径没有影响。在相同文档上的实测表明，`haiku`
  的耗时是其两倍——它会进行推理，而且无法禁止——
  费用却仅略低一些；`opus` 则会拒绝生物学内容（见
  下一项）。两者仍可通过 `--model` 使用；这些别名会跟随
  各自系列的最新模型。`fable` 和 `[1m]` 变体会被拒绝，
  因为它们会转而消耗付费额度。`--reasoning_effort` 用于设置推理强度，
  但翻译并不能从中获益：实测推理量为零或接近零。
- **Opus 会拒绝某些生物学内容。** 它的安全防护比
  Sonnet 更严格，Anthropic 的错误消息也提醒，这些防护
  “有时会将与生物学研究相关的工作标记出来”。实测中，一则关于
  279 个生成分子的动态简讯导致整篇文章在十四种
  语言中均被拒绝。不会写入任何内容：aipmt 会拒绝被截断的响应，说明是
  安全防护所致，并建议使用 `--model sonnet`。
- 在 CI 中（设置了 `CI` 或 `GITHUB_ACTIONS`）以及 Windows 下会被拒绝（未实测）。
- 变量：`AIPMT_CLAUDE_BIN`（否则依次使用 `PATH`、`~/.local/bin/claude`）、
  `AIPMT_CLAUDE_TIMEOUT`（每个片段的秒数，默认 900）、
  `AIPMT_CLAUDE_MAX_UTILIZATION`（默认 0.8）、`CLAUDE_CONFIG_DIR`（Claude Code
  的账户，绝不从项目的 `.env` 中获取）；工作目录位于
  `XDG_CACHE_HOME/aipmt/claude-code` 下（默认 `~/.cache`）。

**使用条款：责任由您的账户承担。**
[Claude Code 法律条款页面](https://code.claude.com/docs/en/legal-and-compliance)
并未禁止“最终用户使用自己的 Claude 订阅登录未经修改的 Claude Code 二进制程序”：
aipmt 正是这样做的，它启动官方
二进制程序，而且从不读取令牌。但 Anthropic “不允许
第三方开发者……代表用户通过 Free、Pro 或 Max 套餐的
凭据转发请求”，倾向于要求第三方工具使用 API 密钥，
“包括开源项目”，并保留将其
用量从付费额度中扣除的权利
（[Claude 帮助](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)）。
对于分发给用户、通过启动二进制程序来运行的工具，目前没有任何条文作出明确判断。

**数据**：对于 Free、Pro 和 Max 账户，如果隐私设置允许，
Claude Code 的数据也会用于模型训练
（[数据页面](https://code.claude.com/docs/en/data-usage)）。aipmt 不会保留
任何本地对话记录（`--no-session-persistence`）。请勿通过它处理
任何机密内容。

### 使用自行选择的服务提供商：`--use_opencode`

[OpenCode](https://opencode.ai) 是一个开源编程代理（MIT），
会将请求路由到其内部配置的服务提供商：API 密钥、订阅、
OpenCode Zen 网关（免费模型，无需账户）或本地模型。这里
对 Zen 和 Ollama 两条路径进行了端到端实测。

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

必须设置 `--model`：否则，OpenCode 会回退到一个免费模型，
而与该模型的交互可能用于训练；这个选择
不会替您作出。

每次调用均采取以下隔离措施：

- 使用优先于您自身配置的内联配置，定义一个 `aipmt` 代理，
  禁用其全部工具（`permission: { "*": "deny" }`），关闭会话
  共享，设置 `--pure`，绝不使用 `--auto`；
- 使用空的临时工作目录，并设置 `OPENCODE_DISABLE_PROJECT_CONFIG` 和
  `OPENCODE_DISABLE_CLAUDE_CODE`——如果没有它们，OpenCode 会将
  当前目录的 `AGENTS.md` 和 `~/.claude/CLAUDE.md` 注入提示词。
  全局 `~/.config/opencode/AGENTS.md` 仍会被注入，OpenCode 不允许
  将其排除；
- 输出约束：退出码为 0，没有 `error` 事件，没有
  工具调用，最后一步为 `stop`，文本非空，而且实际加载了 `aipmt`
  代理——未知的 `--agent` 不会导致 OpenCode 失败，
  它会静默回退到编程代理；
- 不传递任何 `aipmt` 密钥，唯一例外是 `OPENCODE_API_KEY`，即
  OpenCode 自身的密钥。服务提供商在 OpenCode 中配置，而不是在
  `aipmt` 的 `.env` 中配置。

注意事项：

- Zen 的免费模型会发生变化，限制未公开，
  与模型的交互可能用于训练：适合公开文档，
  不适合私人内容。
- 本地模型必须至少提供 16 k tokens 的上下文，因为片段
  最长可达 16 000 个字符。Ollama 通常配置为 4 096：需要
  通过带有 `PARAMETER num_ctx 32768` 的 `Modelfile` 来调整。
- `--eco` 不起作用；`--reasoning_effort` 会原样作为
  OpenCode 的 `--variant` 传递。
- OpenCode 会将每个会话记录到 `~/.local/share/opencode/`。
- 变量：`OPENCODE_BIN`（否则依次使用 `PATH`、`~/.opencode/bin/opencode`）、
  `OPENCODE_TIMEOUT`（每个片段的秒数，默认 600）。`OPENCODE_CONFIG`
  会原样传递给 OpenCode。

通过 Ollama 使用本地模型的示例，在 `~/.config/opencode/opencode.json` 中：

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

`reasoningEffort: "none"` 会关闭 Ollama 默认对这些模型启用的
思考功能，而 Modelfile 无法将其关闭。对一个
六词句子的实测结果：不加该选项时消耗 919 个推理 token、耗时 68 秒，加入后为 9 个 token。

### 使用超过 400 个模型：`--use_openrouter`

OpenRouter 是一个按用量计费的路由服务，通过统一额度访问
第三方托管的模型，其中包括这里其他
服务提供商均未提供的中国开放模型。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

必须设置 `--model`。在产生任何费用之前执行的预检会处理
路由的两个特殊情况：

- **同一个模型由数十家托管商提供，各自上限
  不同**——`z-ai/glm-5.3-flash` 有 23 家托管商，其中一家将输出限制为
  2 048 tokens。预检会读取 `/api/v1/models/{modèle}/endpoints`，
  排除输出上限低于 8 000 tokens 或状态异常的托管商，
  并通过 `allow_fallbacks: false` 固定使用其余托管商。
- **推理按输出费率计费**——`z-ai/glm-5.2` 的一个
  “OK”响应，开启推理时消耗 107 个 token，关闭时为 2 个。默认关闭推理；对于
  强制推理的模型，会设置为其接受的最低强度，因为目录中的
  默认设置可能在翻译完成前耗尽输出预算。
  `--reasoning_effort` 始终优先。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- 上下文窗口大小来自目录。低于 16 400 tokens 的模型
  会在任何调用之前被拒绝：提示词和片段需要 8 400，
  输出至少需要 8 000。
- 如果目录中没有对应的标识名、无法访问目录，或者没有
  满足上限要求的托管商，命令就会停止。
- `finish_reason=length` 且输出为空，表示预算已被
  推理耗尽，而不是输出截断：消息会区分这两种情况。
- `--eco` 不起作用。
- 变量：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>）、
  `OPENROUTER_BASE_URL`（默认 `https://openrouter.ai/api/v1`，必须设置 `https://`）、
  `OPENROUTER_TIMEOUT`（默认 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`
  （默认 30）。

### 翻译说明

`--add_translation_note` 会在 `bottom`（默认）、`top`（前置元数据
之后）或 `both`（`--note_position`）处添加一条说明，格式为 `legacy`（加粗
段落，默认）或 `marker`（`--note_format`）。`marker` 格式是一个
不可见的 Markdown 引用定义，
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`，
后接一段加粗引用：在 GitHub 上可读，也可在构建时通过
remark 插件处理。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 详细测量结果

所有测量均为使用 `aipmt` 实际执行的翻译，目标为
十四种语言：en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi。
**已写入**统计通过防护检查并写入的文件；**无
差异**统计 `scripts/compare_structure.py` 未发现问题的文件——其中
章节、小标题、链接、不同 URL、代码块、
内联代码、表格行、引用块和加粗词语的数量均相同。

“无差异”表示“未检测到问题”，并不表示“完全一致”：比较器
只统计元素，不读取其内容。它不会报告被删除的
四级标题、被替换的内联代码文本、被更换的旗帜，
也不会报告多了一个括号而无法跳转的内部链接，
例如 `[texte]((#ancre))`——它也不会评判
语言。

### 内容密集的动态文章，`--news` 模式

一期 [jls42.org 人工智能动态](https://jls42.org/fr/news)：
589 行、140 个链接、21 个章节、3 段受保护的英文引用。测试于
2026 年 9 月 4 日和 5 日进行。

| 模型                                          | 访问方式              | 已写入 | 无差异   | 每种语言耗时中位数 |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google 订阅  | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google 订阅  | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `claude-sonnet-5-5`                             | Anthropic API      | 14/14   | ✅ **14/14** | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT 订阅 | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | Claude 订阅  | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | Claude 订阅  | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `claude-haiku-5-5`                              | Anthropic API      | 14/14   | ⚠️ 11/14     | 2 min 54 s     |
| `claude-haiku-4-5`                              | Anthropic API      | 14/14   | ⚠️ 7/14      | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | 本地              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok 订阅    | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | Claude 订阅  | 0/14    | ❌ 0/14      | —              |

9 月 9 日使用同一动态的另一期
（356 行）重新测量了 Grok：14 种语言中有 9 种写入，8 种无差异。开头
表格中采用的就是这一数据。三次中断的测试未计入：
`qwen3.5-27b`（9 种语言）和 `kimi-k2.6`（4 种）因额度不足而中断，
`z-ai/glm-5.3-flash` 的两次失败则源于推理设置，
服务提供商此后已对此进行修正。OpenRouter 各行是在
`--use_openrouter` 引入之前，使用路由器默认设置测量的；`z-ai/glm-5.2`
使用随软件提供的服务提供商实现重新测量，结果仍为 14/14。9 月 10 日使用
当前比较器重新计算了数据：`qwen3.8-flash` 和
`qwen3.7-flash` 相比首次发布各增加了一种语言，
其余数据不变。

`--use_antigravity` 各行于 9 月 26 日使用同一篇
文章测量，同时并行执行四种语言的翻译：上午测量 `gemini-3.7-flash-medium`，
下午测量 `gemini-3.8-flash-medium`。翻译成英文时，两者都自行删除了
引用下方的三行法语译文，没有凭空添加旗帜，
英文引用也保持完整：备用清理步骤无需
处理任何内容。在 `--eco`（`gemini-3.7-flash-low`）下，仅测量了
四种语言（en、ja、ar、hi）：4 种全部写入，全部无差异，耗时中位数为
1 min 52 s。同一天还使用较新一期动态进行了复核，
即 9 月 25 日的一期（438 行、2 段英文引用），通过 `gemini-3.7-flash-medium`
在博客之外进行翻译：14 种全部写入，全部无差异，每种语言耗时 87 至
128 s。

`--use_claude_code` 各行于 9 月 26 日使用同一篇
文章测量，同时并行执行四种语言的翻译，推理强度为 `low`。使用 `sonnet` 时，
十四种语言中的英文引用均保持完整；翻译成英文时，
模型自行删除了法语译文行，没有凭空添加
旗帜。`opus` 未写入任何语言：每种语言的响应
都在最后一个片段被安全防护中止，原因是一则关于为某个结合位点
生成 279 个分子的简讯。单独发送时，这则简讯
会因属于“生物学”类别而被拒绝；`sonnet` 则在所有语言中都完成了翻译。`haiku` 写入了
十四种语言；其中三种（en、pl、ro）的一个章节标题从
二级变成了一级。它会进行推理，而且无法禁止——推理占其
输出 token 的 61 %——因此耗时超过 `sonnet` 的两倍。

`claude-sonnet-5-5`、`claude-haiku-5-5` 和 `claude-haiku-4-5` 各行
于 10 月 18 日通过 Anthropic API 使用同一篇文章测量，
每个模型同时并行执行四种语言的翻译。Sonnet 5.5 不允许关闭
思考：aipmt 会向它发送其接受的最低设置，而其
响应中不含任何思考内容。它写入了十四种语言，全部无差异，也
未重试任何片段；翻译成英文时，它自行删除了
法语译文行，没有凭空添加旗帜，而且所有语言中的英文引用均保持
完整。Haiku 5.5 测量时启用了自适应思考：关闭思考后，
它会留下整段法语，因而被防护检查拒绝——
14 种语言中仅写入 3 种。两个 Haiku 都在同一则简讯上遇到了问题：Haiku 5.5
在日语、韩语和中文中改变了标题层级或重复生成了标题，
Haiku 4.5 则在七种语言中将标题改为一级，并在日语中将其保留为
法语。将两份文档翻译成十四种语言，Haiku 4.5 的费用为
3,67 $，Haiku 5.5 为 0,57 $，Sonnet 5.5 为 9,21 $。
### 本项目的 README，标准 Markdown

版本冻结于 2026 年 9 月 9 日：785 行，285 处行内代码，40 个
代码块围栏，89 行表格。四份翻译并行进行。

| 模型                                          | 已完成 | 无差异 | 每种语言的中位耗时 | 差异                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | 无                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | 无                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | 比较器未发现差异；内部链接重复（en）                   |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | 无                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | 无                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | 一个加粗词（ja）                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | 一个加粗词（ko）                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | 一行表格与上一行粘连（ar）                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | 一个链接（sv），一个加粗词（zh）                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | 一个加粗词（ar, ja）                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | 一个加粗词（hi, ja, ko）                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 阿拉伯语中新增了 40 处行内代码；加粗（hi, ja, ko）                   |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2 种语言被拒绝（ar, hi）：返回结果丢失了行内代码        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | 丢失一个章节（ar, hi, ko）；新增代码块（ja, ko, ro, zh） |

两轮中断的测试未计入评分：Grok 的 CLI 会话在完成十二种语言后过期
（其中十一种无差异），而 `qwen3.8-flash` 在完成两种语言后，
其托管服务商返回了 HTTP 429。`opencode/mimo-v2.5-free` 和 `ollama/gpt-oss-20b-32k`
未在此版本上重新测量；在 9 月 4 日和 5 日所用的版本上，
文档少了 277 行，它们各完成了 14 种语言中的 9 份翻译，其中分别有 7 份
和 1 份无差异。

`--use_antigravity` 和 `--use_claude_code` 这两行并非在
冻结版本上测量，而是在 9 月 26 日使用随 1.14.0 发布的版本测量的——
`claude-sonnet-5-5`、`claude-haiku-5-5` 和 `claude-haiku-4-5` 这几行则于 10 月 18 日
在同一版本上测量：600 行，257 处行内代码，30 个代码块围栏，85
行表格。该版本
少了 185 行，因此无法与其他行逐项比较；
但这几行之间可以相互比较。对于比较器不检查的内部链接，
`gemini-3.8-flash-medium` 在十四种语言中均完整保留，
`gemini-3.7-flash-medium` 在意大利语中破坏了链接；
`sonnet` 和 `opus` 在所有语言中均完整保留，`haiku` 在
英语中将链接重复了一遍；`claude-sonnet-5-5` 和 `claude-haiku-4-5` 在
十四种语言中均完整保留，`claude-haiku-5-5` 在其完成的十二种语言中也均完整保留。

### 四个知名项目的 README

FastAPI、Ollama、tldr-pages 和 Vue.js，直接取自 GitHub，未作改动——这些
文档比前两份更容易处理。本轮测试针对
表现欠佳的模型；Gemini 在此作为比较基准。

| 模型                    | 范围                  | 已完成 | 无差异   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 个项目 × 14 种语言     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 个项目 × 14 种语言     | 55/56   | ❌ 47/56     |
| `grok-4.6`（订阅）   | 4 个项目 × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 个项目 × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### 这些测量不代表什么

- **并非全面排名**：仅 OpenRouter 就提供四百多个
  模型，而本次只测量了约十五个。
- **耗时仅供参考**：各轮测试并行进行三到六份翻译，
  而供应商的吞吐量在一天内也会变化。
- **仅反映特定日期的观察结果**：模型可能在名称不变的情况下更新，而且您的
  文档与我们的不同。

要使用您的文档重新测量，请针对文件的冻结副本运行：

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## 参与贡献

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

这两行都必不可少：没有 `pip install -e .`，`python -m aipmt`
会返回 `No module named aipmt`。

质量工具，可选但建议使用：

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

仓库中的 28 份翻译（README 和 CHANGELOG，各十四种语言）可通过
`./regen_translations.sh --force` 重新生成——默认使用 ChatGPT 订阅中的 Codex 和 `gpt-6.1-sol`，
四份并行。`REGEN_PROVIDER` 和
`REGEN_MODEL` 可切换调用方式：`antigravity` 仍使用订阅，即
Google 的订阅，无需例外许可即可运行；按量收费的 API（`openai`、`gemini`、
`grok`、`openrouter`）在未指定 `REGEN_ALLOW_PAID_API=1` 时会被拒绝；
`REGEN_JOB_TIMEOUT` 限制每个任务的运行时间（600 s，Codex 和
Antigravity 为 1 800 s）。工具的详细说明见 `CLAUDE.md`。

## 使用此脚本的项目

- **[jls42.org](https://jls42.org)** — 以 15 种语言发布的个人博客。其
  [每日人工智能动态](https://jls42.org/fr/news)每天由此工具
  翻译，并作为上述测量的参考文档。

## 作者

Julien LE SAUX
电子邮件：contact@jls42.org

## 许可证

GNU 通用公共许可证第 3 版。参见 [许可证](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)。

## 免责声明

本程序按照 GPL v3 第 15 和第 16 节的规定，
**不提供任何担保**：按“原样”提供，不保证适销性
或对特定用途的适用性，作者亦不对
因使用本程序而造成的损害承担责任。许可证
正文优先于本摘要。

- **发布前请审阅。** 保护机制涵盖代码块、
  行内代码、URL、锚点以及 `--news` 模式中的引用——不涵盖
  标题、表格、前置元数据或句子的含义。
- **您的文档会发送给所选供应商**，并受其使用条款
  和数据政策约束。某些免费模型可能
  将您的对话用于训练，而 Antigravity 的条款
  允许 Google 重复使用这些对话并交由人工审阅，
  付费订阅也不例外；只有本地模型才能确保
  数据完全不离开您的机器。
- **API 调用费用由您承担。** 本程序不设
  支出上限：长文档、失败后重试或大量推理的模型
  都会产生更高费用。
- **已发布的测量结果仅反映特定日期的观察情况**，并非保证。

文中提及的产品和公司名称归各自
所有者所有。本项目与其中任何一方均无关联。

**文章由 gpt-6.1-sol 从法语翻译为中文。**
