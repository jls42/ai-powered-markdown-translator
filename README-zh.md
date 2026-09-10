# AI 驱动的 Markdown 翻译器

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="错误"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="代码异味"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="重复行（%）"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="技术债务"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="代码行数"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy 徽章"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

在不同语言之间翻译 Markdown 文件，同时保留其结构：代码块、行内代码、URL、锚点、表格和 front matter。共有九种调用模型的方式——五种 API、两种不按用量计费的订阅方式、两种路由器——并提供公开测量结果，展示每个模型实际能够保留哪些内容。

## 概览

- **九种 provider 路径**：OpenAI、Mistral、Claude、Gemini 和 Grok API；不按用量计费的 ChatGPT（Codex）与 Grok 订阅；路由器 OpenCode（开源、免费或本地）和 OpenRouter（超过 400 个模型）。
- **不会因丢失 token 而产生错误内容**：代码块、行内代码、URL、锚点和引用在调用前会被替换为 token，并在返回后进行验证。如果缺少任何一个，文件就不会被写入。
- **长文档**：根据模型的上下文窗口进行分段。
- **`--news` 模式**：保护英语引文，并按语言处理旗帜，适用于资讯监测文章。
- **`--eco` 模式**：使用速度更快、价格更低的模型。
- 可选的**翻译说明**，可置于顶部、底部或两处同时添加。

## 安装

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

需要 Python 3.10 或更高版本。若要从仓库安装，请参阅[参与贡献](#参与贡献)。

## 配置

密钥会从三个位置读取，优先级从高到低；每个位置只补充前一个位置中缺失的值。

|     | 位置                                            | 用途                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 环境变量                     | CI、容器、临时覆盖 |
| 2   | 当前目录（或其父目录）中的 `.env` | 项目专用密钥            |
| 3   | `~/.config/aipmt/.env`                        | 一次安装，全局有效       |

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

可以使用 `GEMINI_API_KEY` 代替 `GOOGLE_API_KEY`。用户文件遵循 `XDG_CONFIG_HOME`（仅限绝对路径），在 Windows 下则遵循 `%APPDATA%`。如果没有密钥，命令会列出这三个位置。

**项目中的 `.env` 不能重定向调用。**它只提供密钥，绝不提供目标地址：其中任何 `_BASE_URL`、`_API_BASE` 或 `_ENDPOINT` 变量、代理设置（`HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY`）、证书存储设置（`SSL_CERT_FILE`、`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）以及 `XDG_CONFIG_HOME` / `APPDATA` 都会被忽略，并显示警告。克隆下来的仓库不应能够劫持您的密钥。读取此文件时也不会进行插值：`NOM=${OPENAI_API_KEY}` 不会在其中复制密钥。请在环境变量或 `~/.config/aipmt/.env` 中设置这些变量。

可选变量：`XAI_BASE_URL`（默认值为 `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（每次调用的秒数，默认值为 900）、`CODEX_BIN`、`CODEX_TIMEOUT`（默认值为 600）、`GROK_BIN`、`GROK_HOME`（默认值为 `~/.grok`）、`GROK_TIMEOUT`（默认值为 900）、`GROK_TRANSLATE_SANDBOX`、`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（默认值为 600）、`OPENROUTER_BASE_URL`（要求设置 `https://`）、`OPENROUTER_TIMEOUT`（默认值为 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（默认值为 30）。每个变量都在其 provider 对应的章节中有详细说明。

## 快速入门

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

使用 `document.md` 翻译为西班牙语时，会在 `--target_dir` 中生成 `document-es.md`；使用 `--include_model` 时，则生成 `document-es-gpt-5.6-terra.md`。扩展名始终变为 `.md`——`article.mdx` 会生成 `article-en.md`——但使用 `--keep_filename` 时会保留原始文件名。若翻译已存在，在未指定 `--force` 时会跳过。

退出代码：如果所有文件均已成功处理或跳过，则为 `0`；如果仍有文件失败，则为 `1`（失败列表会输出到标准错误）；如果是配置问题，则为 `2`。失败的文件绝不会被写入，即使写入操作本身失败也是如此：内容会先写入旁边的临时文件，再进行重命名。重新运行即可。

## 如何选择模型

测量基于两个真实文档，每个模型都将它们翻译成相同的十四种语言。**数值表示在十四种语言中，有多少种语言的译文被成功写入，且与源文档相比没有任何结构差异。**

| 模型               | 访问方式                 | 高密度资讯监测文章 | 本 README    | 差异及受影响的语言数量                                                                                             |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | Google API 密钥                    | ✅ 14/14                | ⚠️ 13/14     | 14 种语言中有 1 种：多了一个粗体词语（ja）                                                                                         |
| **GPT-5.6 Sol**      | ChatGPT 订阅或 OpenAI 密钥 | ✅ 14/14                | ⚠️ 12/14     | 14 种语言中有 2 种：少了一个粗体词语（ar、ja）                                                                                   |
| **GLM-5.2**          | OpenRouter 密钥                    | ✅ 14/14                | ⚠️ 11/14     | 14 种语言中有 3 种：少了一个粗体词语（hi、ja、ko）                                                                               |
| Claude Sonnet 5      | Anthropic API 密钥                 | ⚠️ 11/14                | ⚠️ 12/14     | 文章中有 3 种语言：出现了一个额外代码块（es、de、hi）；本 README 中有 2 种：一个链接缺少标记（sv），一个词语变为粗体（zh） |
| Qwen 3.7 Flash       | OpenRouter 密钥                    | ❌ 8/14                 | ⚠️ 10/14     | 文章中有 1 种语言被拒绝，另外 5 种存在差异；本 README 中约有四十个词语被放入 `code`（ar）                       |
| Grok 4.6             | Grok 订阅                   | ❌ 8/14                 | 未评分     | 14 种语言中有 5 种因未返回行内代码和 URL 而被拒绝；荷兰语版本整体存在差异                                  |
| GPT-OSS 20B          | 本地模型（Ollama）             | ❌ 7/14                 | 未重新测量 | 14 种语言中有 4 种被拒绝：模型在其中遗留了法语段落，防护机制将其拦截                                     |
| MiMo v2.5（免费）  | OpenCode Zen，无需账户         | ❌ 11/14                | 未重新测量 | 1 种语言被拒绝；波兰语版本丢失了一个章节                                                                                     |
| Mistral Large        | Mistral API 密钥                   | ❌ 5/14                 | ❌ 1/14      | **整个章节消失**：文章中有 1 种语言（hi），本 README 中有 3 种（ar、hi、ko）——此外文章中还有 3 种语言被拒绝   |
| DeepSeek V4 Flash    | OpenRouter 密钥                    | ❌ 3/14                 | 未重新测量 | 14 种语言中有 10 种被拒绝；每种语言耗时 37 分钟                                                                                    |

|     | 符号含义                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 十四种语言全部成功翻译，且与源文档相比没有任何差异                                                                                                                                       |
| ⚠️  | 十四种语言全部成功翻译；差异仅限于**标记**——一个粗体词语、一个 `code`，或一个丢失方括号的链接。没有缺少任何文本、URL、代码块或章节 |
| ❌  | 至少有一种语言无法翻译——文件被拒绝且不会写入——**或者**已写入的文件中缺少内容                                                                      |

需要注意：

- **被拒绝的翻译不等同于损坏的翻译。**当返回结果缺少 token 时，文件不会被写入，该语言会被计为拒绝。这正是 Grok 处理该文章时发生的情况：在五种非拉丁文字语言中，第一个分段就丢失了四处行内代码和三个 URL。
- **这道安全网不涵盖标题、表格、front matter 或正文。**如果模型删除了一个章节，工具仍会毫无异议地写入文件——Mistral 就出现了这种情况。这些元素无法用 token 替换，当前的防护机制也不会检查它们；`scripts/compare_structure.py` 可以检测丢失的章节，但只能事后发现。
- **Grok 在本 README 上没有评分**：其 CLI 会话在完成十二种语言后过期，其中十一种没有差异。中断的测试不予评分。
- **文档密度比语言更重要。**Grok 能够处理普通 README，但在链接密集的文章上会失效，荷兰语也不例外。

日期与文档：“本 README”列于 2026 年 9 月 9 日基于本文件的一个固定修订版本进行测量（785 行、285 处行内代码、89 行表格），之后文件又经过修改。“高密度资讯监测文章”列来自 9 月 4 日和 5 日进行的测试，所用文章共 589 行；Grok 一行除外，它于 9 月 9 日使用同一份资讯监测文章的另一个版本重新测量。完整表格、耗时和测试协议请参阅[详细测量结果](#详细测量结果)。

## 所有选项

| 选项                   | 说明                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 要翻译的单个 Markdown 文件（作为 `--source_dir` 的替代方式）                                             |
| `--source_dir`           | 包含 Markdown 文件的源目录（默认值：`content/posts`）                                   |
| `--target_dir`           | 翻译文件的输出目录（默认值：`traductions_en`）                                    |
| `--source_lang`          | 源语言（默认值：`fr`）                                                                                  |
| `--target_lang`          | 目标语言（默认值：`en`）                                                                                   |
| `--model`                | 指定要使用的模型                                                                                  |
| `--eco`                  | 使用经济型模型                                                                              |
| `--use_mistral`          | 使用 Mistral AI API                                                                                     |
| `--use_claude`           | 使用 Claude API                                                                                         |
| `--use_gemini`           | 使用 Gemini API                                                                                         |
| `--use_grok`             | 使用 xAI API（Grok）——需要 `XAI_API_KEY`                                                           |
| `--use_codex`            | 使用 Codex CLI，并计入 ChatGPT 订阅配额                                                    |
| `--use_grok_cli`         | 使用 Grok CLI，并计入 Grok 订阅配额                                                        |
| `--use_opencode`         | 使用 OpenCode（开源）连接至 OpenCode 中配置的 provider；需要 `--model provider/modèle` |
| `--use_openrouter`       | 使用 OpenRouter——需要 `OPENROUTER_API_KEY` 和 `--model fournisseur/modèle`                          |
| `--force`                | 强制重新翻译                                                                                       |
| `--keep_filename`        | 保留原始文件名                                                                          |
| `--news`                 | 新闻模式：保护英语引文，按语言处理旗帜                                      |
| `--add_translation_note` | 添加翻译说明                                                                                |
| `--note_position`        | 说明位置：`top`、`bottom`（默认值）或 `both`                                                     |
| `--note_format`          | 说明格式：`legacy`（默认值，粗体段落）或 `marker`                                            |
| `--include_model`        | 在输出文件中包含模型名称                                                            |
| `--reasoning_effort`     | GPT-5.x 推理强度：`none`/`low`/`medium`/`high`/`xhigh`                                         |

八个 `--use_*` flag 互斥：同时使用两个会被拒绝。

## Providers

### 通过 API：OpenAI、Mistral、Claude、Gemini、Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` 会切换到各 provider 的经济档位。

| Provider   | 质量型（默认）                                      | 经济型（`--eco`）      |
| ---------- | ----------------------------------------------------- | ------------------------- |
| OpenAI     | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral    | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini     | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex      | `gpt-5.6-sol`（也可通过 `--model` 使用 `terra` 和 `luna`） | `gpt-5.6-luna`            |
| Grok API   | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI   | `grok-4.6`                                            | `grok-4.5`                |
| OpenCode   | 必须指定 `--model provider/modèle`                 | 相同——`--eco` 无效 |
| OpenRouter | 必须指定 `--model fournisseur/modèle`              | 相同——`--eco` 无效 |
### 关于 ChatGPT 订阅：`--use_codex`

驱动官方 Codex CLI：翻译用量从 ChatGPT 订阅配额中扣除，无需 API 密钥，也不按用量计费。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 依次在 `CODEX_BIN`、`PATH` 和 package `openai-codex-cli-bin` 中查找二进制文件。绝不会读取 `~/.codex/auth.json`。
- 从子进程环境中移除 `OPENAI_API_KEY` 和 `CODEX_API_KEY`：即使存在密钥，也绝不会切换到 API。
- 每个分段至少会消耗 5 小时窗口中的一条“消息”；如果验证失败并重试，则消耗两条。据 OpenAI 估计，Plus 方案中的 `gpt-5.6-luna`（`--eco`）每 5 h 可使用 250-2 000 条消息，`gpt-5.6-sol` 可使用 10-100 条。
- `--model gpt-5.6-terra` 和 `--model gpt-5.6-luna` 也通过订阅运行。如果账户无权使用某个模型，则会返回 400：“model is not supported when using Codex with a ChatGPT account”。
- 比 API 更慢，而且文档越长，差距越大：在此 README 上，`gpt-5.6-sol` 的每种语言耗时中位数为 6 min 46 s，而 `gemini-3.7-flash` 为 36 s。
- 在 CI 中拒绝运行（定义了 `CI` 或 `GITHUB_ACTIONS`）：订阅通过个人会话文件进行身份验证，该文件不应出现在共享 runner 上。
- 变量：`CODEX_BIN`、`CODEX_TIMEOUT`（每个分段的秒数，默认 600）。

### 关于 Grok 订阅：`--use_grok_cli`

原理相同，使用官方 Grok Build CLI，并通过 SuperGrok 或 X Premium+ 订阅运行。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **隔离性弱于 Codex。** Grok 的 OS sandbox 在许多较新的 Linux 工作站上并不适用（AppArmor、容器 runtime socket）；如果某个 profile 无法应用，它会静默地以非隔离方式启动。因此，脚本默认不请求任何 profile，并会明确提示这一点；它依赖 CLI 的 `--deny` 规则，包括 catch-all `*`——这是唯一会拒绝启动、而不是悄悄移除保护的层。`GROK_TRANSLATE_SANDBOX=read-only` 强制要求 OS sandbox；如果机器无法满足要求，启动就会失败。
- 配额按周计算，并与 Chat、Imagine 和 Voice 共享，而且没有任何命令可以读取配额：一个批次可能在没有提示的情况下消耗对话用量。
- 变量：`GROK_BIN`、`GROK_HOME`（CLI 目录，默认 `~/.grok`）、`GROK_TIMEOUT`（默认 900）、`GROK_TRANSLATE_SANDBOX`。

### 使用自选供应商：`--use_opencode`

[OpenCode](https://opencode.ai) 是一个开源（MIT）的代码 agent，可路由至其中已配置的供应商：API 密钥、订阅、OpenCode Zen 网关（免费模型，无需账户）或本地模型。这里对 Zen 和 Ollama 两种路径进行了端到端测量。

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

`--model` 为必填项：如果缺少它，OpenCode 会回退到一个可能将交互内容用于训练的免费模型；脚本不会替您做出这一选择。

每次调用都会进行隔离：

- 一个优先于您自身配置的 inline 配置定义了 agent `aipmt`，拒绝其所有工具（`permission: { "*": "deny" }`），禁用会话共享，使用 `--pure`，绝不使用 `--auto`；
- 使用一次性空白工作目录，并设置 `OPENCODE_DISABLE_PROJECT_CONFIG` 和 `OPENCODE_DISABLE_CLAUDE_CODE`——如果不设置，OpenCode 会把当前目录的 `AGENTS.md` 和 `~/.claude/CLAUDE.md` 注入 prompt。全局 `~/.config/opencode/AGENTS.md` 仍会被注入，因为 OpenCode 不允许将其排除；
- 输出契约：返回码为 0、没有 `error` 事件、没有工具调用、最后一步处于 `stop`、文本非空，并且确实加载了 agent `aipmt`——未知的 `--agent` 不会使 OpenCode 失败，而是会静默回退到编码 agent；
- 不传递任何 `aipmt` 密钥，唯一例外是 OpenCode 自身的密钥 `OPENCODE_API_KEY`。供应商在 OpenCode 中配置，而不是在 `aipmt` 的 `.env` 中配置。

须知：

- Zen 的免费模型会发生变化，其限制没有文档说明，且交互内容可能被用于训练：适合公开文档，不适合私密内容。
- 本地模型必须至少提供 16 k tokens 的上下文，因为分段最长可达 16 000 个字符。Ollama 通常将其配置为 4 096：请使用带有 `PARAMETER num_ctx 32768` 的 `Modelfile`。
- `--eco` 不起作用；`--reasoning_effort` 会原样作为 OpenCode 的 `--variant` 传递。
- OpenCode 会将每个会话记录在 `~/.local/share/opencode/` 中。
- 变量：`OPENCODE_BIN`（否则依次使用 `PATH`、`~/.opencode/bin/opencode`）、`OPENCODE_TIMEOUT`（每个分段的秒数，默认 600）。`OPENCODE_CONFIG` 会原样传递给 OpenCode。

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

`reasoningEffort: "none"` 会关闭 Ollama 默认在这些模型上启用、且无法通过 Modelfile 禁用的推理。对一个六词句子的测量结果：不使用该选项时产生 919 个推理 tokens，耗时 68 s；使用后仅产生 9 个 tokens。

### 使用 400 多个模型：`--use_openrouter`

OpenRouter 是一个按用量从统一余额扣费的路由器，连接由第三方托管的模型——其中包括其他供应商在此均未提供的中国开源模型。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` 为必填项。在产生任何费用前执行的 preflight 会处理路由中的两个特殊问题：

- **同一个模型由数十家具有不同上限的托管商提供**——对于 `z-ai/glm-5.3-flash`，共有 23 家托管商，其中一家将输出限制为 2 048 tokens。preflight 会读取 `/api/v1/models/{modèle}/endpoints`，排除输出低于 8 000 tokens 或状态异常的托管商，并通过 `allow_fallbacks: false` 固定其余托管商。
- **推理按输出费率计费**——对于 `z-ai/glm-5.2` 的一个“OK”响应，推理 tokens 为 107，而正文仅为 2。默认关闭推理；对于强制启用推理的模型，则使用其可接受的最低 effort，因为目录中的默认设置可能会在翻译完成前耗尽输出额度。`--reasoning_effort` 仍具有最高优先级。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- 上下文窗口取自目录。低于 16 400 tokens 的模型会在任何调用前被拒绝：prompt 和分段需要 8 400，输出至少需要 8 000。
- 如果 slug 不在目录中、目录无法访问，或没有托管商能满足上限要求，命令都会停止。
- `finish_reason=length` 且输出为空，表示预算被推理消耗，而不是发生了截断：消息会区分这两种情况。
- `--eco` 不起作用。
- 变量：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>）、`OPENROUTER_BASE_URL`（默认 `https://openrouter.ai/api/v1`，要求 `https://`）、`OPENROUTER_TIMEOUT`（默认 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（默认 30）。

### 翻译说明

`--add_translation_note` 会添加一条说明，可放在 `bottom`（默认）、`top`（front matter 之后）或 `both`（`--note_position`），格式可为 `legacy`（粗体段落，默认）或 `marker`（`--note_format`）。`marker` 格式是一个不可见的 Markdown 引用定义：
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`，
后接粗体引用：在 GitHub 上可读，也可在构建时由 remark plugin 处理。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 详细测量结果

所有测量均为使用 `aipmt` 实际执行的翻译，目标为十四种语言：en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi。**已写入**是指通过防护检查的文件；**无差异**是指 `scripts/compare_structure.py` 未发现任何差异的文件——章节、副标题、链接、不同 URL、代码块、inline code、表格行、引用块和粗体词的数量均相同。

“无差异”表示“未检测到差异”，而不是“完全相同”：比较器只统计元素，不读取其内容。它既不会报告被删除的四级标题、被替换的 inline code 文本或被调换的旗帜，也不会判断语言是否正确。

### 信息密集型监测文章，`--news` 模式

[jls42.org 的 AI 监测](https://jls42.org/fr/news)一期内容：589 行、140 个链接、21 个章节、3 条受保护的英文引用。测量于 2026 年 9 月 4 日和 5 日进行。

| 模型                              | 访问方式          | 已写入 | 无差异       | 每种语言耗时中位数 |
| --------------------------------- | ----------------- | ------ | ------------ | ------------------ |
| `gemini-3.7-flash`                   | Google API        | 14/14  | ✅ **14/14** | 1 min 18 s         |
| `gpt-5.6-sol`（`--use_codex`） | ChatGPT 订阅      | 14/14  | ✅ **14/14** | 11 min 28 s        |
| `z-ai/glm-5.2`                   | OpenRouter        | 14/14  | ✅ **14/14** | 5 min 37 s         |
| `qwen/qwen3.8-flash`                   | OpenRouter        | 14/14  | ✅ **14/14** | 26 min 23 s        |
| `claude-sonnet-5`                   | Anthropic API     | 14/14  | ⚠️ 11/14     | 6 min 31 s         |
| `opencode/mimo-v2.5-free`                   | OpenCode Zen      | 13/14  | ❌ 11/14     | 9 min 27 s         |
| `qwen/qwen3.7-flash`                   | OpenRouter        | 13/14  | ❌ 8/14      | 10 min 09 s        |
| `ollama/gpt-oss-20b-32k`                   | 本地              | 10/14  | ❌ 7/14      | 12 min 39 s        |
| `mistral-large-latest`                   | Mistral API       | 11/14  | ❌ 5/14      | 5 min 32 s         |
| `deepseek/deepseek-v4-flash-0731`                   | OpenRouter        | 4/14   | ❌ 3/14      | 37 min 27 s        |
| `grok-4.6`（`--use_grok_cli`） | Grok 订阅         | 1/14   | ❌ 1/14      | 23 min 11 s        |

9 月 9 日，使用同一监测内容的另一期版本（356 行）重新测量了 Grok：14 种语言中写入了 9 种，8 种无差异。总表采用的就是这一数据。三次中断的测量未列出：`qwen3.5-27b`（9 种语言）和 `kimi-k2.6`（4 种）因余额不足而中断；`z-ai/glm-5.3-flash` 的两次失败源自 provider 此后已修正的推理设置。OpenRouter 各行使用路由器在 `--use_openrouter` 之前的默认设置进行测量；使用随附 provider 重新测量的 `z-ai/glm-5.2` 同样达到 14/14。数据已于 9 月 10 日使用当前比较器重新计算：与首次发布相比，`qwen3.8-flash` 和 `qwen3.7-flash` 各增加一种语言，其余保持不变。

### 本项目的 README，标准 Markdown

固定于 2026 年 9 月 9 日的版本：785 行、285 个 inline code、40 个代码块围栏、89 行表格。并行执行四个翻译任务。

| 模型                              | 已写入 | 无差异    | 每种语言耗时中位数 | 差异内容                                              |
| --------------------------------- | ------ | --------- | ------------------ | ----------------------------------------------------- |
| `gemini-3.7-flash`                   | 14/14  | ⚠️ 13/14  | 36 s               | 一个粗体词（ja）                                      |
| `claude-sonnet-5`                   | 14/14  | ⚠️ 12/14  | 2 min 56 s         | 一个链接（sv）、一个粗体词（zh）                      |
| `gpt-5.6-sol`（`--use_codex`） | 14/14  | ⚠️ 12/14  | 6 min 46 s         | 一个粗体词（ar、ja）                                  |
| `z-ai/glm-5.2`（OpenRouter）     | 14/14  | ⚠️ 11/14  | 2 min 34 s         | 一个粗体词（hi、ja、ko）                              |
| `qwen/qwen3.7-flash`                   | 14/14  | ⚠️ 10/14  | 2 min 17 s         | 阿拉伯语中新增 40 个 inline code；粗体（hi、ja、ko） |
| `mistral-large-latest`                   | 14/14  | ❌ 1/14   | 2 min 44 s         | 丢失一个章节（ar、hi、ko）；新增代码块（ja、ko、ro、zh） |

两次中断的测量未列出：Grok 的 CLI 会话在完成十二种语言后过期（其中十一种无差异）；`qwen3.8-flash` 则在完成两种语言后收到托管商的 HTTP 429。`opencode/mimo-v2.5-free` 和 `ollama/gpt-oss-20b-32k` 未在此版本上重新测量；在 9 月 4 日和 5 日那个少 277 行的版本上，两者在 14 种语言中都写入了 9 种，其中无差异的分别为 7 种和 1 种。

### 四个知名项目的 README

FastAPI、Ollama、tldr-pages 和 Vue.js，直接取自 GitHub——这些文档比前两个更容易。该轮测量主要针对表现不佳的模型；Gemini 用作对照。

| 模型                            | 范围                     | 已写入 | 无差异       |
| ------------------------------- | ------------------------ | ------ | ------------ |
| `gemini-3.7-flash`                 | 4 个项目 × 14 种语言     | 56/56  | ✅ **55/56** |
| `opencode/mimo-v2.5-free`                 | 4 个项目 × 14 种语言     | 55/56  | ❌ 47/56     |
| `grok-4.6`（订阅）         | 4 个项目 × ar、hi、ja、zh | 16/16  | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`                 | 4 个项目 × ar、hi、ja、zh | 15/16  | ❌ 9/16      |

### 这些测量不代表什么

- **不是详尽排名**：仅 OpenRouter 就提供四百多个模型，其中只测量了约十五个。
- **耗时仅供参考**：各轮测量并行执行三到六个翻译任务，而且供应商的吞吐量会随一天中的时段变化。
- **是特定时间点的观察结果**：同名模型也会发生变化，而且您的文档与我们的文档不同。

要在您自己的文档上重新测量，请使用文件的固定副本：

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

这两行都是必需的：如果没有 `pip install -e .`，`python -m aipmt` 会响应 `No module named aipmt`。

可选但推荐的质量工具：

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

仓库中的 28 个翻译文件（README 和 CHANGELOG，各十四种语言）可通过 `./regen_translations.sh --force` 重新生成——默认使用 ChatGPT 订阅中的 Codex 和 `gpt-5.6-sol`，并行执行四个任务。`REGEN_PROVIDER` 和 `REGEN_MODEL` 可更改路径；如果未提供 `REGEN_ALLOW_PAID_API=1`，则拒绝使用付费 API（`openai`、`gemini`、`grok`、`openrouter`）；`REGEN_JOB_TIMEOUT` 限制每个 job 的最长时间（600 s，Codex 为 1 800 s）。工具详情见 `CLAUDE.md`。

## 使用此脚本的项目

- **[jls42.org](https://jls42.org)**——以 15 种语言发布的个人博客。其[每日 AI 监测](https://jls42.org/fr/news)每天都由此工具翻译，并作为上述测量的参考文档。

## 作者

Julien LE SAUX  
电子邮箱：contact@jls42.org

## 许可证

GNU GENERAL PUBLIC LICENSE Version 3。参见 [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)。

## 免责声明

本程序按照 GPL v3 第 15 节和第 16 节的条款分发，**不提供任何保证**：按“原样”提供，不保证适销性或特定用途适用性，其作者不对使用本程序造成的任何损害承担责任。许可证正文优先于本摘要。

- **发布前请仔细校对。** 保护机制涵盖代码块、inline code、URL、锚点以及 `--news` 模式中的引用——不涵盖标题、表格、front matter，也不保证句子含义。
- **您的文档会被发送至所选供应商**，并受其使用条款和数据政策约束。某些免费模型可能会将您的交互内容用于训练；只有本地模型能确保数据完全不离开您的机器。
- **API 调用会向您收费。** 本程序不会限制支出：长文档、失败后恢复处理或大量推理的模型都会产生更高费用。
- **已发布的测量结果只是特定时间点的观察结果**，并非保证。

文中提及的产品和公司名称归其各自所有者所有。本项目与其中任何一方均无关联。

**文章已使用 gpt-5.6-sol 从法语翻译成中文。**
