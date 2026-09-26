# AI 驱动的 Markdown 翻译器

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 代码质量</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="质量门状态"></a>
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

在保留结构的同时将 Markdown 文件从一种语言翻译为另一种语言：支持代码块、行内代码、URL、锚点、表格和 front matter。提供十种模型调用方式——五个 API、三个无按量计费的订阅、两个路由网关——并发布了各模型实际保留效果的测试指标。

## 概览

- **十种提供商路径**：OpenAI、Mistral、Claude、Gemini 和 Grok API；无需按量计费的 ChatGPT (Codex)、Grok 和 Google (Antigravity) 订阅；OpenCode（开源、免费或本地）与 OpenRouter（400 多个模型）路由网关。
- **绝不因标记丢失而出错**：代码块、行内代码、URL、锚点和引用在调用前均会被替换为占位标记并在返回时进行校验。只要缺少一个，文件就不会被写入。
- **长篇文档**：根据模型的上下文窗口进行分段。
- **`--news` 模式**：保护英文引用并按语言管理国旗标识，专为资讯类文章设计。
- **`--eco` 模式**：调用速度更快且更经济的模型。
- **可选的翻译附注**：可在顶部、底部或两处同时添加。

## 安装

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

需要 Python 3.10 或更高版本。如需从仓库安装，请参阅[贡献](#贡献)。

## 配置

程序会从三个位置读取密钥，优先级从高到低；后一位置仅补充前一位置未设置的内容。

|     | 位置                                          | 用途                                  |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 环境变量                                      | CI、容器、临时覆盖                    |
| 2   | 当前目录（或父目录）中的 `.env`        | 项目专属密钥                          |
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

可使用 `GEMINI_API_KEY` 代替 `GOOGLE_API_KEY`。用户配置文件遵循 `XDG_CONFIG_HOME`（仅限绝对路径），在 Windows 下遵循 `%APPDATA%`。如果未找到密钥，该命令会列出这三个位置。

**项目中的 `.env` 既不能重定向调用，也不能指定执行的程序。** 它仅用于提供密钥，绝不提供目标地址或可执行程序：任何以 `_BASE_URL`、`_API_BASE`、`_ENDPOINT` 或 `_BIN` 开头的变量（`CODEX_BIN`、`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`）、`GROK_HOME`、代理变量（`HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY`）、证书存储路径（`SSL_CERT_FILE`、`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）以及 `XDG_CONFIG_HOME` / `APPDATA` 在其中都会被忽略，并输出警告。克隆的仓库不应在首次翻译时窃取您的密钥，或诱导您运行其自带的程序。此文件读取时也不进行变量插值：`NOM=${OPENAI_API_KEY}` 不会在此处复制密钥。请将这些变量配置在环境变量或 `~/.config/aipmt/.env` 中。

可选变量：`XAI_BASE_URL`（默认 `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（每次调用秒数，默认 900）、`CODEX_BIN`、`CODEX_TIMEOUT`（默认 600）、`GROK_BIN`、`GROK_HOME`（默认 `~/.grok`）、`GROK_TIMEOUT`（默认 900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（默认 900）、`OPENCODE_BIN`, `OPENCODE_TIMEOUT`（默认 600）、`OPENROUTER_BASE_URL`（必须设置 `https://`）、`OPENROUTER_TIMEOUT`（默认 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（默认 30）。各变量的详细说明见其对应提供商的小节。

## 快速入门

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

将 `document.md` 翻译为西班牙语会在 `--target_dir` 中生成 `document-es.md`；使用 `--include_model` 时，会生成 `document-es-gpt-5.6-terra.md`。文件扩展名始终会转为 `.md`——`article.mdx` 会生成 `article-en.md`——除非使用 `--keep_filename`，该参数会保留原始文件名。若不带 `--force`，已存在的翻译将被跳过。

退出码：全部成功或跳过返回 `0`；若有文件处理失败返回 `1`（错误输出中会列出）；若由配置问题引起则返回 `2`。失败的文件绝不会被写入，即使在写入操作本身发生异常时也是如此：内容先写入临时文件，然后再重命名。只需重新运行即可。

## 如何选择模型

使用各模型对两份真实文档分别翻译至相同的 14 种语言进行了评测。**数值表示在 14 种语言中，翻译成功写入且与原文相比毫无偏差的语言数量。**

| 模型                 | 访问方式                          | 密集资讯文章            | 本 README    | 差异内容及涉及语言数                                                                                  |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ----------------------------------------------------------------------------------------------------- |
| **Gemini 3.8 Flash** | Google 订阅 (Antigravity)         | ✅ 14/14                | ✅ 14/14     | 两份文档均无任何差异                                                                                  |
| **Gemini 3.7 Flash** | Google API 密钥                   | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种：多出一个粗体词 (ja)                                                               |
| **Gemini 3.7 Flash** | Google 订阅 (Antigravity)         | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种：少了一个粗体词 (ko)                                                               |
| **GPT-5.6 Sol**      | ChatGPT 订阅或 OpenAI 密钥        | ✅ 14/14                | ⚠️ 12/14     | 14 种语言中有 2 种：少了一个粗体词 (ar, ja)                                                           |
| **GLM-5.2**          | OpenRouter 密钥                   | ✅ 14/14                | ⚠️ 11/14     | 14 种语言中有 3 种：少了一个粗体词 (hi, ja, ko)                                                       |
| Claude Sonnet 5      | Anthropic API 密钥                | ⚠️ 11/14                | ⚠️ 12/14     | 资讯文章中有 3 种语言：多出一个代码块 (es, de, hi)；本 README 中有 2 种：一个链接丢失标记 (sv)，一个粗体词 (zh) |
| Qwen 3.7 Flash       | OpenRouter 密钥                   | ❌ 8/14                 | ⚠️ 10/14     | 资讯文章中有 1 种语言被拒，另有 5 种出现偏差；本 README 中约有 40 个词被标记为 `code` (ar)    |
| Grok 4.6             | Grok 订阅                         | ❌ 8/14                 | 未评分       | 14 种语言中有 5 种因未返回行内代码和 URL 而被拒；荷兰语全篇出现偏差                                   |
| GPT-OSS 20B          | 本地模型 (Ollama)                 | ❌ 7/14                 | 未重新测试   | 14 种语言中有 4 种被拒：模型在其中残留了法语段落，被保护机制拦截                                      |
| MiMo v2.5 (免费)     | OpenCode Zen，无需账户            | ❌ 11/14                | 未重新测试   | 1 种语言被拒；波兰语丢失了一个小节                                                                    |
| Mistral Large        | Mistral API 密钥                  | ❌ 5/14                 | ❌ 1/14      | **整节内容丢失**：资讯文章中有 1 种语言 (hi)，本 README 中有 3 种 (ar, hi, ko)——且资讯文章中有 3 种语言被拒 |
| DeepSeek V4 Flash    | OpenRouter 密钥                   | ❌ 3/14                 | 未重新测试   | 14 种语言中有 10 种被拒；每种语言耗时 37 分钟                                                         |

|     | 符号含义                                                                                                                                                              |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14 种语言全部翻译完成，且与源内容完全一致                                                                                                                             |
| ⚠️  | 14 种语言全部翻译完成；差异仅在于**标记格式**——例如多出一个粗体词、`code`、或是链接丢失了方括号。没有缺失任何正文文本、URL、代码块或小节                    |
| ❌  | 至少有一种语言未能翻译完成——文件被拒、未写入——**或**已写入的文件中存在内容缺失                                                                                       |

核心结论：

- **被拒的翻译并不等于损坏的翻译。** 当返回内容缺少标记时，文件不会被写入，该语言会被计为被拒。Grok 在测试资讯文章时就遇到了这种情况：在 5 种非拉丁字母语言中，第一段就丢失了 4 个行内代码和 3 个 URL。
- **这层防护网并不覆盖标题、表格、front matter 或正文文本。** 如果模型删除了某个小节，工具仍会直接写入该文件——Mistral 就是如此。这些元素无法用标记替换，目前的保护机制也未对其进行拦截；`scripts/compare_structure.py` 可以在事后检测到小节丢失。
- **Grok 在本 README 上没有评分**：其 CLI 会话在处理了 12 种语言后超时，其中 11 种无偏差。未完成全部测试的不予评分。
- **文档的密度比语言更关键。** Grok 能够应对普通的 README，但在包含大量链接的文章上则会崩溃，即便是荷兰语也是如此。

测试日期与文档说明：“本 README”列于 2026 年 9 月 9 日基于本文件的固定版本（785 行，285 个行内代码，89 行表格）进行测试，此后有所修改——Antigravity 的两行除外，后者于 9 月 26 日在随 1.14.0 发布的较短版本（600 行，257 个行内代码，85 行表格）上测试。“密集资讯文章”列来自 9 月 4 日至 5 日对一篇 589 行文章的测试，Grok 一行除外（于 9 月 9 日在该资讯的另一期上重新测试），以及 Antigravity 的两行（于 9 月 26 日在同一篇文章上测试）。
完整表格、耗时和测试方案详见[详细评估](#详细测定数据)。

## 所有选项

| 选项                     | 说明                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | 要翻译的单个 Markdown 文件（可替代 `--source_dir`）                                                           |
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
| `--use_codex`           | 使用 ChatGPT 订阅配额的 Codex CLI                                                                             |
| `--use_grok_cli`           | 使用 Grok 订阅配额的 Grok CLI                                                                                 |
| `--use_antigravity`           | 使用 Google AI Pro 或 Ultra 订阅配额的 Antigravity CLI (`agy`)                                       |
| `--use_opencode`           | 使用 OpenCode（开源）连接到 OpenCode 中配置的提供商；需要 `--model provider/modèle`                                      |
| `--use_openrouter`           | 使用 OpenRouter — 需要 `OPENROUTER_API_KEY` 和 `--model fournisseur/modèle`                                                       |
| `--force`           | 强制重新翻译                                                                                                  |
| `--keep_filename`           | 保留原始文件名                                                                                                |
| `--news`           | 新闻模式：保护英文引用，按语言管理国旗                                                                        |
| `--add_translation_note`           | 添加翻译附注                                                                                                  |
| `--note_position`           | 附注位置：`top`、`bottom`（默认）或 `both`                                             |
| `--note_format`           | 附注格式：`legacy`（默认，粗体段落）或 `marker`                                                  |
| `--include_model`          | 在输出文件中包含模型名称                                                                                      |
| `--reasoning_effort`          | GPT-5.x 推理强度：`none`/`low`/`medium`/`high`/`xhigh`             |

这九个 `--use_*` 标志互斥：同时组合使用两个将被拒绝。

## 提供商

### 通过 API：OpenAI、Mistral、Claude、Gemini、Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` 切换至各提供商的经济档。

| Provider    | 质量（默认）                                         | 经济档 (`--eco`) |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol`（亦可通过 `--model` 使用 `terra` 和 `luna`） | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| OpenCode    | 必须指定 `--model provider/modèle`                 | 同前 — `--eco` 无效 |
| OpenRouter  | 必须指定 `--model fournisseur/modèle`              | 同前 — `--eco` 无效 |

### 基于 ChatGPT 订阅：`--use_codex`

调用官方 Codex CLI：翻译计入 ChatGPT 订阅配额，无需 API 密钥或按量计费。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 二进制文件会依次在 `CODEX_BIN`、`PATH` 以及 `openai-codex-cli-bin` 软件包中查找。绝不会读取 `~/.codex/auth.json`。
- `OPENAI_API_KEY` 和 `CODEX_API_KEY` 会从子进程环境中移除：即使存在密钥，也绝不会切换到 API。
- 每个分段至少消耗 5 小时窗口内的 1 条“消息”——若验证失败并重试则消耗 2 条。作为估算参考，OpenAI 针对 Plus 方案公布的数据为：`gpt-5.6-luna`（`--eco`）每 5 小时 250–2,000 条消息，`gpt-5.6-sol` 为 10–100 条。
- `--model gpt-5.6-terra` 和 `--model gpt-5.6-luna` 同样走订阅通道。账户无权使用的模型会返回 400 错误“model is not supported when using Codex with a ChatGPT account”。
- 速度比 API 慢，且文档越大差距越明显：在此 README 上，使用 `gpt-5.6-sol` 每种语言的中位耗时为 6 分 46 秒，而 `gemini-3.7-flash` 仅需 36 秒。
- 在 CI 中被拒绝（已定义 `CI` 或 `GITHUB_ACTIONS`）：订阅通过个人会话文件认证，该文件不应存放在共享 runner 上。
- 变量：`CODEX_BIN`、`CODEX_TIMEOUT`（每个分段的秒数，默认 600）。

### 基于 Grok 订阅：`--use_grok_cli`

借助官方 Grok Build CLI 实现相同原理，基于 SuperGrok 或 X Premium+ 订阅。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **隔离强度低于 Codex。** Grok 的操作系统沙箱在许多较新的 Linux 主机上无法生效（由于 AppArmor、容器运行时套接字），且无法生效的配置文件会以未受隔离状态静默启动。因此脚本默认不请求任何配置文件，并对此进行提示，转而依赖 CLI 的 `--deny` 规则（包括全捕获规则 `*`）——这是唯一一层宁可拒绝启动也不会静默移除保护的防护。`GROK_TRANSLATE_SANDBOX=read-only` 强制要求操作系统沙箱，若机器无法支持则启动失败。
- 配额按周计算，与 Chat、Imagine 和 Voice 共享，且没有任何命令可查询该配额：一次批量处理可能会在毫无预警的情况下消耗对话使用量。
- 变量：`GROK_BIN`、`GROK_HOME`（CLI 目录，默认 `~/.grok`）、`GROK_TIMEOUT`（默认 900）、`GROK_TRANSLATE_SANDBOX`。

### 基于 Google 订阅：`--use_antigravity`

借助 Antigravity 官方 CLI `agy` 实现相同原理：对于订购了 Google AI Pro 或 Ultra 的用户，翻译将从订阅配额中扣除，而非按 token 计费。这是使用该配额的唯一途径：Gemini CLI 自 2026 年 6 月 18 日起不再支持这些账户（[公告](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)），且 Antigravity 的 SDK 仅接受 API 密钥或 Google Cloud 项目。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **未保留任何付费通道。** agy 从您的环境中仅接收一份受限的变量列表——`PATH`、语言与时区、终端、身份标识、代理与证书、会话总线——且不包含任何密钥：其多个变量可在无任何提示的情况下切换调用方式（实测：其中一个会将文档发送至第三方网关，另一个则发送至计费的 Google Cloud 项目），而黑名单过滤在每次代码审查时总会有遗漏。在处理任何分段前，不消耗配额的 `agy -p /config` 必须显示付费 AI 额度已禁用，且无 API 密钥及 Google Cloud 项目——若缺少设置则视为拒绝——否则不执行任何翻译；随后每次调用的日志必须证实使用的是订阅通道（`authMethod=consumer`），否则响应将被拒绝。
- **隔离防护。** 每次调用都在一个私有且一次性的用户目录中运行，并使用无任何工具的翻译智能体：您的 agy 设置、规则、插件、MCP 服务器及挂钩均不会传入，不会向您的历史记录添加任何内容，且登录凭据保留在密钥环中，aipmt 绝不读取。若找不到指定智能体，agy 会静默回退至其编码智能体及其工具：日志中必须有整行内容确认使用了正确的智能体——文档中引用该消息不算数——否则将被拒绝。
- **支持平台**：Linux（需在拥有密钥环的会话中，即 D-Bus 会话总线、Secret Service）；支持 macOS，但尚未在此平台实测。Windows 下拒绝执行（agy 不会读取用于隔离各次调用的变量），无会话总线的 Linux 下亦拒绝执行（如 SSH 会话、容器、服务器：agy 会将其令牌存储在 `~/.gemini` 文件中，而隔离机制会将其隐藏）。拒绝提示会在启动前连同原因直接给出，无需等待一分钟登录代码。
- **模型**：`agy models` 中的模型。Gemini 系列在名称中体现思考力度（`gemini-3.8-flash-medium`…）：不带后缀的名称在调用前即被拒绝，且 `--reasoning_effort` 无效。默认使用 `gemini-3.8-flash-medium`，并在 `--eco` 下使用 `gemini-3.7-flash-low`；确定这些配置的评测活动见 [详细测定数据](#详细测定数据)。Claude 与 GPT-OSS 拥有独立且小得多的配额：每次实测调用约占 5 小时窗口的 1%，而 Flash 仅约 0.05%。
- **配额**：按组划分，设有 5 小时窗口和周窗口，按 token 消耗比例折算。在作者账户上的实测结果：`gemini-3.8-flash-medium` 下每百万源字符消耗 5 小时窗口约 16 点，`gemini-3.7-flash-medium` 下约 14 点，低思考力度下为 7 至 8 点——因此一份 40,000 字符的 README 消耗略高于半点。周限额则取决于订阅档位。重试遵循 agy 声明的可重试状态；否则，配额用尽的窗口绝不会重试：直到 `/usage` 显示重置之前，每个文件都会失败。
- **速度慢于 API**：在用于测试的高密度文章上，使用 `gemini-3.8-flash-medium` 每种语言的中位耗时为 3 分 59 秒，`gemini-3.7-flash-medium` 为 3 分 14 秒，而通过 API 调用 Gemini 3.7 Flash 仅需 1 分 18 秒。
- **中断**：Ctrl-C 或关闭终端会连同命令一起终止 agy，而不是让它继续消耗您的配额完成本轮操作；Codex、Grok CLI 和 OpenCode 亦是如此。但在 `nohup` 下，翻译会继续进行。
- 在 CI 中被拒绝（已定义 `CI` 或 `GITHUB_ACTIONS`）：登录凭据保存在个人密钥环中。在 runner 上，请使用 `--use_gemini` 搭配 `GOOGLE_API_KEY`。
- 变量：`AGY_BIN`（否则依次使用 `PATH`、`~/.local/bin/agy`），`AGY_TIMEOUT`（每个分段的秒数，包含启动时间，默认 900）。

**使用条款：由您自行承担账户责任。** [Antigravity 服务条款](https://antigravity.google/terms)（第 6 条）及其 [常见问题](https://antigravity.google/docs/faq/) 禁止通过第三方软件利用 Antigravity 登录凭据访问该服务（其中点名提到了 Claude Code、OpenClaw 和 OpenCode），违者可能导致账户被封禁。aipmt 既不读取也不重用令牌：它只是在 Google 针对脚本和 CI 文档化说明的 [无头模式](https://antigravity.google/docs/cli/headless/) 下运行官方二进制文件。Google 员工曾表示，在本地脚本中为自己的工作运行 `agy -p` 是“标准做法”（[官方论坛，2026 年 9 月 25 日，非合约答复](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）；但没有任何官方文件对像本项目这样分发的工具作出明确界定。

**仅限公开文档。** 根据上述条款第 5 条，所有交互内容——包括提示词、响应和元数据——均可能用于改进 Google 的产品和机器学习，并可能由人工审查，即便付费订阅亦是如此。选择退出需要通过设置 `enableTelemetry`（其效果未见文档说明），aipmt 不会设置该项；并且您现有的 agy 设置不会带入隔离环境中。请切勿在此传入任何机密内容。

### 接入自选提供商：`--use_opencode`

[OpenCode](https://opencode.ai) 是一款开源代码智能体（MIT 协议），可路由至其内部配置的提供商：API 密钥、订阅、OpenCode Zen 网关（免费模型，无需账户）或本地模型。在此对 Zen 和 Ollama 两种途径进行了端到端实测。

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

必须指定 `--model`：否则 OpenCode 会回退到免费模型，其交互内容可能会被用于模型训练，而这一决定不应代您做出。

每次调用的隔离措施：

- 内联配置（优先级高于您的配置）定义了一个 `aipmt` 智能体，禁用其所有工具（`permission: { "*": "deny" }`），关闭会话共享，启用 `--pure`，绝不使用 `--auto`；
- 使用干净的一次性工作目录，并设置 `OPENCODE_DISABLE_PROJECT_CONFIG` 和 `OPENCODE_DISABLE_CLAUDE_CODE`——若不设置，OpenCode 会将当前目录的 `AGENTS.md` 和 `~/.claude/CLAUDE.md` 注入提示词中。全局 `~/.config/opencode/AGENTS.md` 仍会被注入，OpenCode 不支持将其排除；
- 输出约定：返回码为 0、无 `error` 事件、无工具调用、最后一步为 `stop`、文本非空，且确实加载了智能体 `aipmt`——未知的 `--agent` 不会使 OpenCode 报错退出，而是会静默回退至编码智能体；
- 除 OpenCode 自身的密钥 `OPENCODE_API_KEY` 外，不传递任何 `aipmt` 密钥。提供商应在 OpenCode 中配置，而非在 `aipmt` 的 `.env` 中配置。

注意事项：

- Zen 的免费模型多变且限制未公开，其交互内容可能会被用于训练：仅适用于公开文档，切勿用于私密内容。
- 本地模型必须提供至少 16k token 的上下文，因为每个分段最多可达 16,000 个字符。Ollama 通常仅配置 4,096：请通过包含 `PARAMETER num_ctx 32768` 的 `Modelfile` 进行调整。
- `--eco` 无效；`--reasoning_effort` 会原样作为 OpenCode 的 `--variant` 传递。
- OpenCode 会将每个会话记录在 `~/.local/share/opencode/` 中。
- 变量：`OPENCODE_BIN`（否则依次使用 `PATH`、`~/.opencode/bin/opencode`），`OPENCODE_TIMEOUT`（每个分段的秒数，默认 600）。`OPENCODE_CONFIG` 原样传递给 OpenCode。

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

`reasoningEffort: "none"` 可关闭 Ollama 默认在这些模型上启用的思考过程（Modelfile 无法将其关闭）。在包含六个单词的句子上实测：未加该选项时思考消耗 919 个 token 且耗时 68 秒，加上该选项后仅消耗 9 个 token。

### 接入 400 多个模型：`--use_openrouter`

OpenRouter 是一个按用量计费的统合路由网关，使用单一账户额度，可访问第三方托管的模型——包括本工具其他提供商均未接入的中国开源模型。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

必须指定 `--model`。在产生任何计费前执行的预检会处理该路由机制的两项特性：

- **同一模型由数十家托管商提供，且输出上限各不相同**——以 `z-ai/glm-5.3-flash` 为例，23 家托管商中有一家的输出上限仅为 2,048 个 token。预检会读取 `/api/v1/models/{modèle}/endpoints`，剔除输出上限低于 8,000 token 或处于降级状态的托管商，并使用 `allow_fallbacks: false` 固定其余托管商。
- **推理按输出定价计费**——在 `z-ai/glm-5.2` 回复“OK”的测试中，思考消耗 107 个 token，而实际输出仅 2 个。推理默认被关闭；对于强制要求推理的模型，则设置为其允许的最低思考力度，因为目录默认值可能会在翻译完成前耗尽输出上限。`--reasoning_effort` 仍具最高优先级。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- 上下文窗口大小取自模型目录。低于 16,400 token 的模型在调用前即被拒绝：提示词与分段需 8,400 token，输出至少需 8,000 token。
- 若标识符（slug）不在目录中、目录无法访问，或没有满足上限要求的托管商，命令将终止执行。
- 若出现 `finish_reason=length` 且输出为空，表明额度已被推理耗尽，而非内容被截断：提示信息对此进行了区分。
- `--eco` 无效。
- 变量：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>）、`OPENROUTER_BASE_URL`（默认 `https://openrouter.ai/api/v1`，需指定 `https://`）、`OPENROUTER_TIMEOUT`（默认 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（默认 30）。

### 翻译附注

`--add_translation_note` 可添加附注，位置可选 `bottom`（默认）、`top`（位于 front matter 之后）或 `both`（`--note_position`），格式可选 `legacy`（加粗段落，默认）或 `marker`（`--note_format`）。`marker` 格式是一个不可见的 Markdown 引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），后接一段加粗引用块：在 GitHub 上直观可读，亦可在构建时由 remark 插件进行解析处理。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 详细测定数据

所有测定数据均为使用 `aipmt` 实际执行的翻译，覆盖十四种语言：en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi。**已写入**统计通过守卫检查的文件数；**无差异**统计 `scripts/compare_structure.py` 未发现任何异常的文件数——即章节数、副标题数、链接数、不同 URL 数、代码块数、行内代码数、表格行数、引用块数及加粗词数完全一致。

“无差异”代表“未检测出异常”，并不等于“完全一致”：比对工具仅统计元素数量，不读取其内容。它既不会报告被删除的 4 级标题，也不会报告行内代码文本被替换、命令行标志被调换，或是因多出一个括号而失效的内部链接（`[texte]((#ancre))`）——更不会对语言质量作出评判。

### 密集追踪文章，`--news` 模式

[jls42.org 的 AI 追踪](https://jls42.org/fr/news)某一期：
589 行、140 个链接、21 个章节、3 处受保护的英文引用。测试于
2026 年 9 月 4 日至 5 日进行。

| 模型                                          | 接入方式           | 已写入  | 无偏差       | 中位数/语言    |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google 订阅        | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google 订阅        | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT 订阅       | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | 本地               | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok 订阅          | 1/14    | ❌ 1/14      | 23 min 11 s    |

Grok 于 9 月 9 日在同类追踪的另一期（356 行）上重新进行了测试：
14 种语言中写入 9 种，8 种无偏差。榜首表格中显示的就是这个数据。
三场中断的测试未计入：`qwen3.5-27b`（9 种语言）和 `kimi-k2.6`（4 种）
因额度不足而中断，`z-ai/glm-5.3-flash` 的两次失败源于推理设置，
提供商此后已对此进行修复。OpenRouter 各项是在路由器的默认设置下测得的，
在 `--use_openrouter` 之前；使用自带提供商重新测试的 `z-ai/glm-5.2`
同样给出了 14/14 的结果。各项数据于 9 月 10 日使用当前的对比工具
重新计算：`qwen3.8-flash` 与 `qwen3.7-flash` 较初次发布各增加了一种语言，
其余保持不变。

`--use_antigravity` 相关测试于 9 月 26 日针对同一篇文章进行，
采用四路并行翻译：上午测试 `gemini-3.7-flash-medium`，下午测试 `gemini-3.8-flash-medium`。
在英文翻译中，两者都自行去除了引用下方的三行法文翻译，且未捏造任何标记，
英文引用也完好无损：后备清理程序无需执行任何操作。在 `--eco`
（`gemini-3.7-flash-low`）中，仅针对四种语言（en、ja、ar、hi）测试：4 种全部写入，
且均无偏差，中位数时间为 1 min 52 s。同日针对更新的一期追踪（9 月 25 日，
438 行，2 处英文引用）进行了复测，由 `gemini-3.7-flash-medium` 在博客之外
进行翻译：14 种全部写入，均无偏差，每种语言耗时 87 至 128 s。

### 本项目的 README，标准 Markdown

2026 年 9 月 9 日定稿版本：785 行，285 处行内代码，40 个代码块闭合标签，
89 行表格。四路并行翻译。

| 模型                                            | 已写入  | 无偏差   | 中位数/语言    | 差异项                                                                   |
| ----------------------------------------------- | ------- | -------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14 | 1 min 43 s     | 无                                                                       |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14 | 36 s           | 一个加粗词（ja）                                                         |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14 | 1 min 22 s     | 一个加粗词（ko）                                                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14 | 2 min 56 s     | 一个链接（sv），一个加粗词（zh）                                         |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14 | 6 min 46 s     | 一个加粗词（ar、ja）                                                     |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14 | 2 min 34 s     | 一个加粗词（hi、ja、ko）                                                 |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14 | 2 min 17 s     | 阿拉伯语增加了 40 处行内代码；加粗（hi、ja、ko）                         |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14  | 2 min 44 s     | 遗失一个章节（ar、hi、ko）；增加了代码块（ja、ko、ro、zh）                |

两场中断的测试未计入：Grok 在完成十二种语言（十一种无偏差）后 CLI 会话过期；
`qwen3.8-flash` 在完成两种语言后收到其托管服务商的 HTTP 429。`opencode/mimo-v2.5-free`
和 `ollama/gpt-oss-20b-32k` 未在此版本上重新测试；在 9 月 4 日至 5 日的版本（短 277 行）中，
它们各自在 14 种翻译中写入了 9 种，其中分别有 7 种和 1 种无偏差。

`--use_antigravity` 各项并未在定稿版本上进行测试，而是在 9 月 26 日随 1.14.0 发布的版本上测试：
600 行、257 处行内代码、30 个代码块闭合标签、85 行表格。该版本缩短了 185 行，
无法与其他各项进行逐项对比；但两项 Antigravity 之间可以相互对比。
在对比工具不检查的内部链接方面，`gemini-3.8-flash-medium` 在全部十四种语言中都保持了完整，
而 `gemini-3.7-flash-medium` 在意大利语中出现了损坏。

### 四个知名项目的 README

FastAPI、Ollama、tldr-pages 和 Vue.js，直接取自 GitHub——比前两个文档更简单。
该测试主要针对表现吃力的模型；Gemini 在此作为参照基准。

| 模型                       | 范围                       | 已写入  | 无偏差       |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 个项目 × 14 种语言       | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 个项目 × 14 种语言       | 55/56   | ❌ 47/56     |
| `grok-4.6`（订阅）   | 4 个项目 × ar、hi、ja、zh  | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 个项目 × ar、hi、ja、zh  | 15/16   | ❌ 9/16      |

### 这些测量不是什么

- **并非详尽的排名**：仅 OpenRouter 就提供了四百多种模型，这里仅测试了约十五种。
- **仅供参考的耗时**：各轮测试并行翻译数量为三到六路不等，且提供商的吞吐量在一天当中会有所波动。
- **具有时效性的观察结果**：同名模型也会发生变动，且您的文档与我们的文档并不相同。

若要在您自己的文档上重新进行测试（针对文件的固定副本）：

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

这两行都是必需的：若缺少 `pip install -e .`，`python -m aipmt` 会返回 `No module named aipmt`。

质量工具链，可选但推荐：

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

仓库中的 28 个翻译文件（README 和 CHANGELOG，十四种语言）可通过 `./regen_translations.sh --force`
重新生成——默认使用 ChatGPT 订阅运行 Codex 和 `gpt-5.6-sol`，四路并行。
`REGEN_PROVIDER` 和 `REGEN_MODEL` 可更改路径：`antigravity` 依然走订阅模式（Google 订阅），
无需特许即可通过；按量计费的 API（`openai`、`gemini`、`grok`、
`openrouter`）在未指定 `REGEN_ALLOW_PAID_API=1` 时会被拒绝；`REGEN_JOB_TIMEOUT` 会对每个作业设置时间上限
（一般为 600 s，Codex 和 Antigravity 为 1 800 s）。工具链的详细说明参见 `CLAUDE.md`。

## 使用此脚本的项目

- **[jls42.org](https://jls42.org)** — 以 15 种语言发布的个人博客。其
  [每日 AI 资讯追踪](https://jls42.org/fr/news)每天都由此工具翻译，
  并作为上述测量的参考文档。

## 作者

Julien LE SAUX
邮箱：contact@jls42.org

## 许可证

GNU GENERAL PUBLIC LICENSE Version 3。参见 [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)。

## 免责声明

本程序在分发时**不作任何保证**，依据 GPL v3 第 15 条和第 16 条的条款：
按“原样”提供，不包含适销性或特定用途适用性的明示或暗示保证，
作者对因使用本程序而造成的任何损失不承担责任。具体以许可证正文为准，
本摘要仅供参考。

- **发布前请仔细通读复核。** 保护机制覆盖代码块、行内代码、URL、锚点以及
  `--news` 模式下的引用——但不涵盖标题、表格、front matter，也不保证句意表达。
- **您的文档会被发送至所选提供商**，受其使用条款和数据政策的约束。部分免费模型可能会将您的交互数据用于模型训练，
  而 Antigravity 的条款允许 Google 复用这些数据并交由人工审核（即使付费订阅也是如此）；
  本地模型是唯一能确保数据不离开您本机的途径。
- **API 调用会产生费用。** 本程序不设开销上限：文档篇幅长、失败重试或推理较多的模型都会增加费用。
- **公布的测量结果仅为特定时间点的观察记录**，并非保证。

文中所提及的产品和公司名称归其各自所有者所有。本项目与其中任何一家均无关联。

**使用 gemini-3.8-flash-medium 从法语翻译为中文的文章。**
