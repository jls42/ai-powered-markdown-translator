### 更新日志

🌍 [法语](CHANGELOG.md) | [英语](CHANGELOG-en.md) | [西班牙语](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [德语](CHANGELOG-de.md) | [日语](CHANGELOG-ja.md) | [韩语](CHANGELOG-ko.md) | [阿拉伯语](CHANGELOG-ar.md) | [印地语](CHANGELOG-hi.md) | [意大利语](CHANGELOG-it.md) | [荷兰语](CHANGELOG-nl.md) | [波兰语](CHANGELOG-pl.md) | [葡萄牙语](CHANGELOG-pt.md) | [罗马尼亚语](CHANGELOG-ro.md) | [瑞典语](CHANGELOG-sv.md)

- **1.13.1** 依赖项新鲜度：滞后不再只是一个可能被忽略的警告（2026-09-09）：

  - **未被计数的警告就是会被错过的警告。** `check-deps-fresh.sh` 已连续数日提示 `openai` 和 `anthropic` 出现滞后，但关卡的摘要行只统计失败项：它显示“就绪：N 项检查通过”，尽管上方几行已经写明存在滞后。只看最后一行的人——而所有人都会这么做——根本无法得知此事。现在，判定结果会包含警告数量，并由专用计数器汇总警告，而不再随执行过程逐条打印。
  - **滞后提示现在附带发行说明。** 单凭版本号无法说明发生了哪些变化，而要求用户自行找到正确文件，恰恰是导致这一步被跳过的阻力。检查会显示每个滞后软件包的 CHANGELOG 地址，无论是主版本还是次版本，并说明原因：SDK 的一次次版本更新已经改动过本项目依赖的内容。
  - **`openai` 3.8.0 → 3.10.0，`anthropic` 1.3.0 → 1.4.0；锁定前已阅读发行说明。** OpenAI 方面，在此版本区间内只有一项行为变化——当数值型 `Retry-After` 标头超出浮点数范围时，不再回退到短暂的退避等待，而是直接返回原始错误且不重试——与本项目依赖的内容无关：模型对额外字段的容忍度保持不变，已在两个标签对应的代码中核实，因此 OpenRouter 添加到选项中的 `native_finish_reason` 和 `error` 仍可正常通过。Anthropic 方面，新增的保护机制会在 SDK 期待 `httpx2` 的位置收到 `httpx` 软件包对象时，通过明确的 `TypeError` 拒绝它；经核实，本项目只传递浮点数。两个版本中，拒绝执行时长超过十分钟的非流式调用这一规则逐字节完全一致：真正使其免受限制的是明确的 `timeout`，其 32 768 个 token 超过了 21 333 的阈值。
  - **已验证**：在升级后的版本上通过 502 + 31 项测试套件；`requirements.txt` 的闭合情况与已安装内容一致（41 个固定版本）；并分别通过 OpenAI 和 Claude SDK 进行了一次真实调用，对 `--news` 模式下的文档进行处理，所得结构与源文档一致。

- **1.13.0** Provider `--use_openrouter`：通往约 430 个模型的付费路由器，其中包括中国开源模型（2026-09-05）：

  - **第九条 provider 路径与第八条一同发布。** 1.12.0 未发布到 PyPI：OpenCode 和 OpenRouter 两个路由器将一同推出。[OpenRouter](https://openrouter.ai) 只需一个密钥，即可访问此处其他任何 provider 都未提供的模型——Kimi、Qwen、DeepSeek、Z.ai——并通过统一余额按用量计费。由于端点兼容 OpenAI，因此使用与 xAI 相同的客户端；**该 provider 的所有差异都集中在预检中**，而每一条规则都源自对 API 的实际测量。

  - **同一模型由数十家具有不同上限的托管商提供，而路由对此毫无感知。** 实测：`z-ai/glm-5.2` 有 33 家托管商，`z-ai/glm-5.3-flash` 有 23 家——其中一家将**输出限制为 2 048 个 token**。因此，使用后者进行长篇翻译时，会随机得到截断结果，且没有任何提示。预检会读取 `/api/v1/models/{modèle}/endpoints`，排除输出上限低于 8 000 个 token、状态异常以及未声明任何上限的托管商，然后固定使用其余托管商。仅有 `provider.only` 而**没有** `allow_fallbacks: false` 只代表一种偏好：路由器仍会转向已被排除的托管商，使固定选择失去意义。如果没有任何托管商满足上限要求，命令就会停止：继续翻译等同于接受静默截断，而这正是该预检机制要防止的问题。

  - **推理按输出费率计费，并且在许多模型上默认启用。** 对 `z-ai/glm-5.2` 使用同一请求，响应为“确定”：**采用模型默认设置时产生 107 个补全 token，关闭推理后只有 2 个**。推理对翻译毫无助益，却会让每个文件的每个分段都增加至 18 倍。因此，默认关闭推理。**431 个模型中有 288 个**强制启用推理（`reasoning.mandatory`），它们会返回 `400 « Reasoning is mandatory for this endpoint and cannot be disabled »`：对于这些模型，预检会读取其接受的推理强度，并请求最低值（见下一点）——推理强度会分配 `max_tokens` 的一个**百分比**，供推理优先消耗，因此随意选择一个值，只会转移出现空白输出的风险，而不会降低风险。

  - **强制推理的模型会收到其接受的最低推理强度，这一决定来自实际测量。** 最初的选择是什么都不发送，以免替模型作出猜测。在 `z-ai/glm-5.3-flash` 上测试后发现，该模型目录中的默认值为 `max`，这种选择会导致输出在翻译结束前**于 32 768 个 token 处被截断**——十四种语言中有两种丢失。提高总额度也无济于事：推理强度会按比例分配额度，因此推理消耗也会随之增长。于是，provider 会在预检时读取 `supported_efforts` 并请求最低值；如果目录未公布任何可用值，则回退为“不指定”。在出错语言上进行反证测试：它此前因额度耗尽而失败，现在可在 9 分钟内完成，且结构与源文档一致。

  - **上游托管商发生故障时，现在会明确指出其身份。** 路由器会将此情况规范化为 `finish_reason=error`，并附带空的 `native_finish_reason`——在两种语言上分别实测两次，均恰好发生于 750 秒。原先的通用消息会让人误以为文档或分段存在问题；现在，消息会明确说明故障发生在供应商一侧，而且通常只需重试即可解决。

  - **`finish_reason=length` 搭配空输出并不代表截断。** 这是因为在生成第一个有效字符之前，额度已被推理消耗殆尽——实测推理消耗 15 850 个 token，而有效输出仅 148 个。两种情况需要采取相反措施：在前一种情况下，缩小分段毫无作用。现在，消息会明确区分二者。另外两项保护机制同样来自实际测量：当上游托管商失败时，路由器会返回**状态码 200，但响应体只包含错误**（`choices[0]` 会抛出晦涩的 `TypeError`，从而掩盖原始消息）；此外，上下文窗口会从目录中读取并写入 `MODEL_TOKEN_LIMITS`——对目录中的 44 个模型而言，`DEFAULT_TOKEN_LIMIT` 是错误的，其中两个模型的上限仅为 4 095 个 token。

  - **`--model fournisseur/modèle` 是必填项，而且会在任何网络请求之前验证其格式。** OpenRouter 并非供应商：这一选择涉及价格、许可证和数据处理方式，不能替用户作出决定。由于 slug 会被插入预检 URL，验证并非只是改善易用性的礼节，而是防止路径注入的保护机制：两个路由器共用的带命名空间正则表达式会接受 `a/b/..`，因此必须明确拒绝父目录段。`--eco` 不起作用，并会明确说明这一点。

  - **修正了三处表述，其中一处原本是错误的。** OpenAI 关于 `codex exec` 的警告针对的是在共享 runner 上注入个人会话文件，而不是代码仓库的公开性质；README、CLAUDE.md 和代码中都误解并错误引用了这项警告。OpenCode 的身份验证存储位置在 1.18.27 中发生了变化（位于 `opencode.db` 的 `credential` 表，而不再是 `auth.json`）；“这里绝不会读取它”这一约束仍然成立，但此前给出的地址已经过时。最后，OpenCode 章节不再将未经验证的途径说成彼此等效：Zen 网关和 Ollama 已经过端到端实测，而 GitHub Copilot、LM Studio 和 llama.cpp 尚未测试，README 现在会明确说明这一点。

  - **开展了一轮测量，并在 README 中加入推荐模型表。** 针对三组文档执行了三百多次翻译——一篇采用 `--news` 模式、内容密集的博客文章，一份使用标准 Markdown 的 README，以及四份直接取自 GitHub 的知名项目 README——目标涵盖十四种语言。表格区分了两个过去常被混为一谈的概念：翻译是否**完成**，以及结果的**结构是否与源文档一致**。有三个模型在两份密集文档中从未丢失任何信息：`gemini-3.7-flash`、通过 ChatGPT 订阅使用的 `gpt-5.6-sol`，以及通过 OpenRouter 使用的 `z-ai/glm-5.2`——它们唯一的偏差，是在一两种语言中漏掉了一对 `**`。核心结论是：**真正具有区分度的因素是文档密度，而不是 `--news` 模式**：通过订阅使用的 Grok 在博客文章上十四次中失败十三次，却在十六份公开 README 中成功十四次；反证测试已确认，原因是处理长分段时发生偏离。表格自身也附有警告：它并不详尽，具有时效性，耗时不能用于排名，正确做法仍然是在自己的文档上进行测量。

  - **在公布数据前修复了结构比较器，因为它会在非拉丁文字中产生两种误报。** URL 后跟全角右括号 `）` 时，原有正则表达式只在 `)` 处停止，因而无法正确截断；于是，即使 URL 完全相同，提取出的字符串也会不同。此外，一段法语中占五行、中文中仅占三行的引用会破坏按行计数。两项修复均已通过反证验证：删除 URL、章节或行内代码仍会被检测到。若不修复，Gemini 和 Codex 公布的结果将分别是十四种语言中仅有十一种和十二种通过，而不是十三种和十二种。

  - **测试**：新增文件 `tests/test_openrouter_provider.py`（76 项测试）——模型验证及拒绝父目录段、固定托管商（上限、状态、未声明上限、共同最低值）、`allow_fallbacks` 始终为假、根据 `mandatory` 关闭或保留推理、完整输出契约（状态码 200 响应中的错误、没有选项、区分空白输出与截断、异常的 `finish_reason`、空内容）、目录不可访问时预检采用失败即关闭策略、slug 缺失以及没有健康托管商、标志互斥性与文件名标签。完整测试套件共计 **502 项测试**。
  - **重构：将单个 4 253 行的模块拆分为多个模块，不改变任何一行行为。** `src/aipmt/translate.py` 被拆分到 `config`、`markdown`、`segmentation`、`guards`、`placeholders`、`news`、`prompts`、`notes`、`naming`、`pipeline`、`cli` 和一个子包 `providers/` 中（每个 provider 一个模块，以 `base` 为基础，`registry` 负责解析和 dispatch）。每次移动都对应一个提交，并有机械化证据：验证器会将包中所有顶层节点的 AST 与参考 snapshot 比较，检查每个符号的位置、安全标记是否逐字保留，以及是否不存在未跟踪文件——这是临时工具，已在下一版本中移除。可见的变化如下：`aipmt.translate` 变为一个 façade，以对象身份不变的方式重新暴露该模块原先不带 `_` 前缀公开的 64 个名称（`__all__` 包含其中九个，即受支持的 API；其余均为兼容性 alias），并停止重新导出此前由 `import *` 收集的 29 个依赖项和标准库名称；不再支持直接执行该文件（`python src/aipmt/translate.py`）——`aipmt` 和 `python -m aipmt` 仍是两种受支持的形式；公共函数的 `__module__` 现在指向其定义模块；SDK 改为在加载 `.env` 之后导入，而非之前，目前没有已知影响。427 个测试连同其标识符完整保留，并迁移至它们实际测试的模块：此前通过 façade 进行 patch 的 91 处现在直接指向查询该名称的模块（经测量，其中两处即使不 patch 仍会通过）；另有七个契约测试锁定 façade；各项 gate 工具在首次移动之前便已重写，确保不会因停止检查而错误变绿——Lizard 的作用域改为目录并设下限，flag 从已构建的 parser 中读取，按包设置覆盖率下限，`release.sh` 列出受跟踪模块。
  - **修复（pull request 审查）**：当目录条目缺少 `context_length` 时，OpenRouter 会拒绝该条目，而不是把默认的 128 000 tokens 记录为实测值——后者还会同时关闭“模型未列出”警告；当 `finish_reason` 为 null（文档所述类型为 `string | null`）时，以托管方给出的原始原因为准，`max_tokens` 的值设为 `length`；如果错误由选项本身携带，则拒绝随附的部分内容，并使用与规范化上游故障相同的消息——汇集托管方详情、原始原因和建议。对于 `part: null` 事件，OpenCode 会返回其契约错误，而不是 `AttributeError`；如果 JSONL 流中有一行事件无法解析，也会拒绝整个流，而非接受部分文本。三个 agent CLI 在 agent 进程于调用期间收到 `SIGTERM` 时会终止其进程组——regen 的 `timeout` 之前会让 agent 继续存活并消耗配额——且进程组的 `SIGKILL` 始终遵循宽限期，即使 shim 正常退出，其孙进程也仍会存活。一对因拆分而分离的 `# fmt: off` / `# fmt: on` 已重新合并；`--reasoning_effort` 的帮助信息现在列出使用它的四个 provider。
  - **修复（第二轮审查）**：向 OpenRouter 请求的输出上限现在会预留 prompt 和 segment 占用的上下文空间——`context_length` 同时涵盖输入和补全；目录中有六个模型此前发出的请求甚至没有为输入留下空间。上下文过短时，会在产生任何费用之前拒绝请求。在不存在 POSIX 进程组的平台上，agent CLI 基础层现在会依次回退到 `terminate` 和 `kill`，不会再让 `AttributeError` 穿过 timeout 防护并导致等待持续下去。OpenCode 的 `429` 标记现在按数字查找，而非通过子字符串查找；此前像 `err_84290b` 这样的错误标识符会触发 90 秒 back-off，最终仍然失败。最后，preflight 现在会显示非标准的 OpenRouter endpoint：项目中的一个 `.env` 即可设置它，而随后发送的会是真实密钥。
  - **安全：项目中的 `.env` 再也无法重定向 API 调用。** `find_dotenv(usecwd=True)` 会从当前目录及其父目录查找文件：不可信的目录树——例如刚克隆的仓库——无需知道任何密钥，便可在其中设置 `OPENROUTER_BASE_URL`、`XAI_BASE_URL` 或 `OPENAI_BASE_URL`（后者由 SDK 自行读取），随后来自环境或用户配置的真实密钥就会被放入发往第三方服务器的 authorization header。过滤依据的是模式，而非列表：经检查已安装的 SDK，共有十二个 routing 变量会被读取，其中仅 Anthropic 客户端就读取六个——手写枚举会漏掉一半。因此，项目层会拒绝任何属于 `_BASE_URL`、`_API_BASE` 或 `_ENDPOINT` 的变量，以及 proxy 和证书存储变量（指向受控证书颁发机构，会使拦截器与真实服务器无法区分），还包括 `XDG_CONFIG_HOME` 和 `APPDATA`：设置后两者等同于决定哪个文件构成用户层，从而可绕过过滤器。这些变量仅能来自用户控制的两个层级：已导出的环境和 `~/.config/aipmt/.env`。此外，读取项目层时不进行插值：`load_dotenv` 默认会展开 `${VAR}`，而包含 `NOM_ANODIN=${OPENAI_API_KEY}` 的不可信 `.env` 会把真实密钥复制到一个基于模式的子进程过滤器无法识别的名称下——随后它便会进入 `codex exec` 的环境，违背已声明的不变量。最后，拒绝消息只显示变量名：形如 `https://${CLE}@hôte/` 的 URL 曾导致插值后的密钥泄漏到日志中，尽管该变量本身已被拒绝。拒绝信息会输出到 stderr，并说明处理方法——企业 relay 应在用户配置中声明。
  - **修复：为每次调用单独计算 OpenRouter 的输出 envelope。** `context_length` 同时涵盖输入和补全，而按拉丁文本校准的固定预留量无法提供任何上界：使用 tokenizer `o200k_base` 测得，16 000 个字符在法语中相当于 3 200 tokens，在日语中为 12 300，在 emoji 中则为 17 500。因此，预算取自实际发送的文本，并以其 UTF-8 字节数作为上界：对于任何使用字节融合的 tokenizer——字节级 BPE、带字节回退的 SentencePiece，目录使用的正是这些系列——每个 token 至少对应一个字节；而 OpenRouter 会路由至数十种未知 tokenizer，这是此处唯一可用的上界。任何平均比率都不适用——一个补充平面表意文字可低至每 token 1.33 字节，一个组合字符则可低至 1.00——现在输入与输出在构造上必然能同时容纳于窗口之中。对于所选模型而言过于密集的 segment，会在调用之前而非计费之后被拒绝。

- **1.12.0** Provider `--use_opencode`：通过开源 agent OpenCode 连接用户选择的供应方——本地模型、无需账户的免费模型、订阅或密钥（2026-09-04）：

  - **第八条 provider 路径，其性质不同于前七条。** [OpenCode](https://opencode.ai)（MIT）不是模型供应商，而是一个通向用户已在 OpenCode 中配置之供应方的_路由器_：API 密钥、订阅（GitHub Copilot、ChatGPT、SuperGrok）、OpenCode Zen gateway——提供**无需账户**的免费模型——或**本地**模型（Ollama、LM Studio、llama.cpp）。脚本以非交互模式驱动 `opencode run`，方式与驱动 Codex 和 Grok 相同，并复用同一套子进程基础设施（独立进程组、timeout 时先 `SIGTERM` 再 `SIGKILL`、始终关闭 stdin、净化环境）。已通过**两次真实翻译**验证：使用 `opencode/mimo-v2.5-free` 将整个 README 翻译为英语——耗时 49 秒、仅一轮、结构与源文件完全一致（32 个标题、26 个代码块结束标记、18 个链接、37 个 URL、37 行表格、135 处 inline code）——以及使用本地 `ollama/qwen2.5:7b` 翻译测试文件，全程无需任何密钥。

  - **`--model provider/modèle` 为必填项，而且这是有意为之。** 如果没有 `--model`，OpenCode 会回退到自己的默认值；在全新安装中，该默认值是 `opencode/big-pickle`，即一个免费的“stealth”模型，其交互内容可能用于训练——实测确实是这个模型进行了响应。替用户静默作出这种选择，恰恰是本仓库要追查的隐式切换；因此错误消息会列出用于查看模型的命令（`opencode models`）以及三个示例（本地、免费、订阅）。`--eco` 不起作用，并会明确说明。仅在用户明确要求时，才会将 `--reasoning_effort` 原样作为 OpenCode 的 `--variant` 传递。

  - **隔离经过测量，而非凭空假设。** inline 配置（`OPENCODE_CONFIG_CONTENT`，在 OpenCode 的合并顺序中位于最后，因此优先于用户配置但不会替换它）定义了一个名为 `aipmt` 的 agent，并拒绝所有工具（`permission: {"*": "deny"}`）：注册表甚至不再向模型提供这些工具；即使要求模型“列出文件并运行 `id`”，它也会回答自己没有工具。session sharing 已禁用，外部 plugin 已排除（`--pure`），绝不使用 `--auto`，工作目录为空且用后即弃。经测量发现并切断了两种静默注入：如果没有 `OPENCODE_DISABLE_CLAUDE_CODE`，用户的 `~/.claude/CLAUDE.md` 会进入**每个** prompt（仅一句“你好”的输入便从 186 tokens 增至 515 tokens）；如果没有 `OPENCODE_DISABLE_PROJECT_CONFIG`，当前目录的 `AGENTS.md` 也会进入——其中一条“每个回答都以 BANANA 结尾”的指令确实影响了翻译。全局 `~/.config/opencode/AGENTS.md` 仍会注入：没有任何开关能排除它，而通过挪用 `XDG_CONFIG_HOME` 来规避，还会同时隐藏用户的供应方。对此选择记录在文档中，而未采用临时拼凑方案。

  - **`exit 0` 证明不了任何事：第三个 CLI，仍需保持同样的警觉——并注意其特有的两个陷阱。** 未知的 `--agent` 不会让 `opencode run` 失败：它只在 stderr 上发出警告，随后**静默**回退到启用工具的 coding agent。如果 inline 配置未生效，翻译便会由一个具备写入能力的 agent 执行；因此输出契约除验证以下条件外，还会检查该消息不存在：返回码为 0、没有 `error` 事件、没有 `tool_use`、最后一个 `step_finish` 位于 `stop` 中（`length` 表示响应被截断）、文本非空。第二个陷阱是：错误的 JSON 事件是**不透明的**——“意外的服务器错误。详情请检查服务器日志。”，并且只有一个简单引用——真正的原因（`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`、`ProviderAuthError`……）仅存在于日志中。因此需要 `--print-logs --log-level ERROR`，并从 stderr 读取 `error="…"` 字段，同时忽略其后的 Bun trace。这样，未知模型会在一秒内失败，并明确指出原因。`--title` 还顺带避免了一次多余的 LLM 调用：若无该项，OpenCode 会在 `small_model` 上额外调用一轮来生成 session 标题。

  - **机密信息：采用与 Codex 和 Grok 相同的模式过滤，仅有一个具名例外。** 保留 `OPENCODE_API_KEY`：这是 OpenCode 自身的密钥（Zen gateway、Go 订阅），按其名称直接交给它——相当于它自己的 `auth.json`，既不是 aipmt 管理的密钥，也不可能由 aipmt 计费。供应方应在 OpenCode 中配置（`opencode auth login`、`opencode.json`），绝不在 aipmt 的 `.env` 中配置；aipmt 的任何密钥都不会进入子进程。与订阅型 CLI 不同，CI 中不会拒绝密钥：在 runner 上使用 API 密钥或自行托管的模型都属于合法用途。

  - **防路径穿越保护现在检查插值后的值，而非原始值。** `provider/modèle` 包含一个曾被 1.10.0 防护机制拒绝的 `/`——拒绝是合理的，因为 `--model` 会被插入文件名 `--include_model`。现在，文件名 label 会先将 `/`、`\` 和 `:` 替换为 `-`，然后才执行任何插值（`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`，因为 `:` 在 Windows 下非法）；上游防护检查的正是该 label：`../../evil` 会变成目标目录下的普通文件名 `doc-en-..-..-evil.md`，只有 `..` 仍会被拒绝，`--target_lang ../x` 也同样如此。`_ensure_within_directory` 的范围防护仍是第二层保障，保持不变。

  - **免费模型与本地模型，以及实际测量结果。** `opencode/mimo-v2.5-free` 翻译一个段落需要 16 秒，翻译此 README 需要 49 秒；`opencode/big-pickle` 翻译 200 个词需要 40 秒，而且两项并发请求持续 5 分钟仍无响应，而单独运行时均可完成；`opencode/nemotron-3.5-lightning-free` 在 3 分钟内没有任何响应。因此使用 `REGEN_PROVIDER=opencode` 时必须指定 `REGEN_MODEL`，并将并发量设为 **2 jobs**。本地方面，Ollama 经常将上下文配置为 4 096 tokens，而 segment 最长可达 16 000 个字符：必须使用带 `PARAMETER num_ctx 32768` 的 `Modelfile`；质量则取决于模型——在测试文件中，一个 7B 模型颠倒了列表顺序并损坏了代码块结束标记，而 gateway 模型完整保留了所有内容。

  - **本仓库的翻译从此绝不再通过按量计费的 API。** 只要 `.env` 中碰巧存在密钥，`regen_translations.sh` 就会使用 OpenAI API，而 Codex 仅作为 opt-in。准备本版本时恰好发生了这种情况：28 份翻译通过 OpenAI API 完成，之后印地语 CHANGELOG 又通过 Gemini API 完成，尽管 ChatGPT 订阅的存在正是为了避免按使用量付费。现已移除密钥自动检测：**默认使用 Codex，并指定 `gpt-5.6-sol`**，即质量模型；`openai`、`gemini` 和 `grok` 除 `REGEN_PROVIDER` 外还要求 `REGEN_ALLOW_PAID_API=1`，这是一个具名豁免，确保规则在作出决定时生效；未知的 `REGEN_PROVIDER` 会直接失败，而非回退到 API。十个测试锁定默认行为、拒绝机制和豁免机制。本版本的 28 份翻译均已通过 Codex 重新完成。

  - **rate limit 的 back-off 已抽取为共享实现**（`_retry_on_rate_limit`）：Codex 和 Grok 的循环除标签外完全相同，再复制第三份便会超过重复度阈值。三个 CLI 错误均继承自同一个 `_CliCallError`；有一个测试禁止三者中的任何一个脱离该继承关系，否则共享循环将无法再捕获它。

  - **测试**：新增文件 `tests/test_opencode_provider.py`（61 个测试）——完整输出契约、agent 回退、从日志读取原因、文本 part 去重并忽略合成 part、timeout 时终止进程组、429 back-off、模型必填与验证、无机密信息的 preflight、二进制文件解析、dispatch 接线、文件名 label 及路径穿越反例。`tests/test_review_hardening.py` 将 flag 互斥规则和无机密信息保障扩展到新 provider。gate 现在要求记录 **22 个** argparse flag。完整测试套件共 **382 个测试**。

- **1.11.1** 文档修复：README 终于列出了七条 provider 路径（2026-09-03）：
  - **1.11.0 的 PyPI 页面写着“4 个 API + Codex CLI”。** 代码实际上公开了七种方式——通过 API 使用 OpenAI、Mistral、Claude、Gemini 和 Grok；通过订阅使用 Codex (ChatGPT) 和 Grok，且不按用量计费。宣传语和 _Multi-Provider_ 条目中都遗漏了两种 Grok 模式，14 份翻译也重复了这一错误。由于软件包的长描述会随版本固定，要修正展示页面就必须使用新版本号：这正是此版本存在的唯一原因。**没有任何代码变更。**
  - `CLAUDE.md` 已与此次发布引入的内容保持一致：gate 计数器（16，在 `--full` 中为 17）、十一个活跃 workflow、`gh pr checks` 中不可见的两个 Sonar/Codacy 计数器（hotspots、Codacy API）、由 `ruff-format` 移动的一个 `# nosemgrep`、OIDC 交换所需的 GitHub 环境，以及 _pending publisher_ 不会预留名称这一事实。

- **1.11.0** 发布至 PyPI：`pip install ai-powered-markdown-translator`，然后执行命令 `aipmt`，无需克隆仓库（2026-09-03）：

  - **单文件脚本变成了可安装的软件包。** `translate.py` 从根目录移至 `src/aipmt/translate.py`，并提供控制台入口点 `aipmt` 及其等效形式 `python -m aipmt`。参与贡献仍需克隆仓库——测试、28 份翻译和质量工具都位于其中——但使用工具不再需要。

    - **导入名称是 `aipmt`，绝不能是 `translate`**，因为冲突真实存在且不会发出提示。PyPI 软件包 `translate`（v3.8.1，最后上传于 2026-07-06）会安装一个同名目录。在 venv 中复现：目录优先于模块，`translate.main` 消失，入口点在 `AttributeError` 处崩溃——而 `pip check` 仍以 rc=0 回答“No broken requirements found”。用户只要安装过 `pip install translate`，就足以让 CLI 损坏，且没有可用的诊断信息。使用真实 wheel 进行反向验证：在该软件包之上安装 `pip install translate`，`aipmt --help` 在安装前后均为 rc=0，两个 CLI 可以共存。
    - **较长的分发名称，较短的命令。** `ai-powered-markdown-translator` 让该软件包能通过 PyPI 搜索找到；仅使用缩写，会让原本不知道该项目的人无从发现，而此次发布的目的恰恰是让项目可被找到。经核查排除了两个看似合理的候选项：`ai-markdown-translator` 自 2024 年起已在 npm 上被一个用途相同的工具占用，比此仓库早 17 个月；而 `aimt` 与 `aim`（v3.29.1）仅相差一个字母，后者还是同一领域的活跃软件包——这是最容易造成长期混淆的情形。顺带一提，有一个方法上的陷阱：`pypi.org/project/<nom>/` 对任何名称都返回 200（反机器人页面），只有 JSON API 的结果可信。
    - **采用 `src/` 布局，而非扁平软件包。** 扁平软件包本可保留测试中的六个 `sys.path.insert(..., "..")`，但这恰恰是问题所在：它们会导入源代码树，而不是已安装的软件包，从而掩盖所有打包错误。实际代价：增加一条替换规则。

  - **密钥终于可以一次配置、长期使用。** 已安装的 CLI 过去没有任何持久配置：只能使用环境变量和当前目录中的 `.env`。`find_dotenv` 确实会一直向上查找到系统根目录，因此**在个人主目录下工作时**能够找到 `~/.env`，但在其他位置工作时什么也找不到——配置是否生效取决于从哪里启动命令，而非明确的设计选择。因此新增第三层：`~/.config/aipmt/.env`，优先级低于已有两层。

    - **优先级并非硬编码**，而是源自 `override=False`，即 `load_dotenv` 的默认值：每一层只填补上一层留下的空缺。因此顺序为环境变量 → 项目的 `.env` → 用户配置，并通过行为测试而非结构测试进行验证——调换两个调用的顺序会导致测试失败，移除第三层同样如此。
    - **刻意选择 `.env` 格式，而非 TOML**：`python-dotenv` 已经是依赖项，该语法已在 15 份 README 中记录，而且同一文件可用于两个作用域。没有新增依赖项，也没有新增语法。若 `XDG_CONFIG_HOME` 为**绝对路径**，则位置遵循其设置——规范要求忽略相对值，否则配置位置将再次取决于当前目录——Windows 下则使用 `APPDATA`。
    - **排除了两个选项，并说明原因。** 系统密钥环（`keyring`）在桌面工作站上更安全，但会在无头环境中失效——服务器、容器、CI——而这恰恰是批量翻译的使用场景；它适合作为可选功能，却不适合作为默认方案。使用 `--api-key` flag 会使密钥进入 shell 历史记录，并在 `ps` 中可见。
    - **没有密钥时，不再显示调用堆栈。** 用户此前会收到一个指向 `site-packages` 的 Python 堆栈，以及一条只提到“环境或 .env”、却没有说明应在哪里创建后者的消息。现在会列出三个位置及其准确路径，并以状态码 2 退出。这个防护网被**刻意限制在较窄范围内**：仅对配置阶段使用 `except ValueError`。若包裹整个执行过程，翻译期间发生的真实 bug 就会被伪装成令人安心的提示——这正是此仓库要追踪的故障模式。有一项测试会读取 `main()` 的源代码，以禁止这种做法。

  - **修复——工具安装后，用户的 `.env` 会被忽略。** 不带参数的 `load_dotenv()` 不会从当前目录向上查找，而会从调用方文件开始查找，因此实际从 `site-packages` 开始。使用真实控制台入口点进行测量：从一个拥有自身 `.env` 的项目启动时，`find_dotenv()` 返回 `''`，密钥不会被加载，而 `find_dotenv(usecwd=True)` 能够找到它。只要工具仅从克隆的仓库中运行，这个 bug 就不存在；发布后它会变成系统性问题，而唯一症状只是配置本来正确，却提示 API 密钥“缺失”。

  - **三个 gate 原本会在停止检查任何内容后仍显示绿色。** 它们被有意安排在移动之前加固：在变更完成后才编写、用于捕获该变更的防护措施并不能证明什么。每项检查在原始仓库上均为绿色，在迁移副本上则变为红色——两个方向都经过测量。

    - **Lizard 会悄无声息地忽略不存在的路径**：rc=0，并显示“0 file analyzed”。复杂度 gate 会从 158 个函数 / 2247 nloc 降至 3 个函数 / 34 nloc，输出文件则为零字节。现在 scope 是一个数组，其中每个条目都会验证是否存在。
    - **对不存在的模块运行 `coverage run --source=` 不会失败**：只在 stderr 发出警告，无论 unittest 还是 `coverage xml` 都返回 rc=0，并且照常发布报告——statements 数量从 1453 被削减到 141。项目之所以看起来健康，只是因为它几乎没有被分析。两个下限用于守护报告：总量，以及测得的最大文件。
    - **翻译新鲜度探针在结构上无法识别调用形式**：它锚定 argparse flag，而文件重命名恰好不会改变这些 flag。复现结果：模块已移动，15 份 README 仍记录着一条不存在的命令，结论却是“没有过期翻译”。因此新增第 7 个章节来检查调用形式而非选项，并将 Lizard hook 与脚本的实际 scope 进行比对——当它的键 `files:` 不再匹配时，不会让 pre-commit 失败，而是直接跳过该 hook。

  - **`requires-python = ">=3.10"` 不再只是一项未经验证的声明。** `sonar-project.properties` 早已宣称支持 3.10-3.12，但从未实际运行过这些版本，开发机器上只有 3.12——这一内部矛盾会随着发布而公之于众。现在有一个测试 workflow 会在 3.10、3.11 和 3.12 上运行测试套件，并安装软件包，从而验证其公开声明的版本范围。

  - **只设下限，不设上限。** `requirements.txt` 继续作为经过测试的 lock，`[project.dependencies]` 则成为公开契约：如果发布 lock 中的精确版本，会与所有安装了其他软件包的用户发生依赖冲突。同样不设置 `<N+1` 上限——那会与 `check-deps-fresh.sh` 直接矛盾，后者会在任何主版本落后时让发布 gate 失败。这组版本下限能够解析，而反向验证 `openai==1.0.0` 输出 `ResolutionImpossible`，证明该控制能够区分情况，而非全盘接受。此外还有一项防护，禁止 `pyproject.toml` 的版本与 CHANGELOG 中的版本不一致：PyPI 不允许重复使用版本号。

  - **已在全新的 venv 中完成端到端验证**：约 70 Ko 的 wheel 仅包含 `aipmt/*.py`、dist-info 和许可证；`aipmt --help` 以 rc=0 退出并包含 22 个 flag；`python -m aipmt` 显示“usage: aipmt”，而非“usage: \_\_main\_\_.py”；`pipx` 安装可正常使用；最重要的是，**从任意用户目录实际执行了一次 fr→en 翻译**，粗体、列表、内联代码、链接和 URL 均得到保留，代码块未被翻译。迁移前已有的 318 项测试全部通过，且迁移前后的标识符列表逐字节完全一致——证明没有任何测试被架空的是这一点，而不是“OK”；另外还新增了十二项三层配置测试，共计 330 项。

- **1.10.0** 新增 Provider `--use_codex`（ChatGPT 订阅配额），更新 SDK 和模型，修复多段落 news 引用（2026-08-29）：

  - **安全审查——PR 设置了两项防护措施，但并未在所有位置贯彻**：

    - **Codex 预检会将整个 `.env` 传给二进制文件。** `_codex_preflight` 调用 `subprocess.run` 时**没有使用 `env=`**：子进程继承完整的 `os.environ`，也就是由 `load_dotenv` 加载的全部 `.env`。使用插桩的伪二进制文件测量发现：**七个 secret** 会进入预检——六个 provider 的密钥加上一个 `GITHUB_TOKEN`——而对应的 `_grok_preflight` 路径则是**零个**，因为它正确传入了 `env=_grok_env()`。这是 PR 内部的不一致：几行之外的 `_strip_secret_env` 正是为了维持这一不变量而存在。现已提取出一个 `_codex_env_base()`，供两条路径共用；修复后的测量结果：两边均为 0 个 secret。
    - **“`--deny` fail-closed”属性并未覆盖实际使用的形式。** 注释为整个 Grok 限制措施所给出的理由是：带有未知前缀的规则会导致启动被拒绝。在 `grok 1.0.13` 上测量发现，这项验证**仅适用于带括号的形式**：`--deny 'CeciNestPasUnOutil(*)'` 会拒绝启动并提示“unknown tool prefix”，而 `--deny 'CeciNestPasUnOutil'` 会被静默接受。但 `GROK_DENY_RULES` 只使用裸名称——因此，如果 xAI 侧重命名工具，就会在毫无提示的情况下移除唯一经过验证的限制层，而该机器上本就不适用 OS sandbox。八条命名规则现已改为 `Prefix(*)`，每条都会验证是否为 CLI 已知前缀；catch-all `*` 保持其字面形式，因为只有这种形式会被接受。一项测试会阻止代码回退到未经验证的形式。
    - **其他方面已验证无误**：不存在命令注入（始终使用列表形式，从不使用 `shell=True`，文档内容通过 stdin 或 `--prompt-file` 传入），不存在不安全的反序列化（仅使用 `json.loads`，并带有类型防护），路径遍历修复在七个 payload 上均未发现绕过方式，并且 CLI 确实应用了 `--deny '*'`（在读取 workdir 外部内容时观察到 `DENY_ENFORCED`）。
    - 此外，前面新增的新鲜度检查绕过了它自己的原则：若某个软件包的 PyPI 请求失败，就会被静默跳过，gate 仍保持绿色。现在它会统计实际完成比较的软件包数量，并在覆盖不完整时失败。

  - **依赖项已更新，并新增两道防线，防止再次长期落后**：

    - **版本落后确实存在，而且持续已久**：`openai` 2.54 → **3.6.0**，`anthropic` 0.125 → **1.2.0**，`certifi` 2024.8.30 → **2026.7.22**——其中根证书存储落后了两年，而所有 provider 调用都依赖它验证 TLS。原因已经确定：**项目中不存在 `.github/dependabot.yml`**。缺少该文件时，GitHub 只会启用 _security updates_，而 Dependabot 仅会针对受 CVE 影响的依赖项提出 PR——这解释了为何它升级了 `urllib3` 和 `idna`，却任由两个 SDK 落后一个主版本。
    - **两个主版本可以共存且没有冲突**，与先前的推测相反：`openai` 3.x 和 `anthropic` 1.x 迁移至 **`httpx2`**，而 `mistralai` 和 `google-genai` 继续使用 `httpx<1`，但它们是两个不同的分发包。先通过真实安装验证，随后又对 **7 条 provider 路径进行了端到端测试**——OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI 和 Grok CLI——每项输出中的内联代码和链接均得到保留。“避免两套 HTTP 栈”只是一项偏好，并非阻碍：测量结果已经作出裁决。
    - **`requirements.txt` 并未描述真实环境**：`google-auth`、`cryptography` 和 `opentelemetry` 栈已安装在工作 venv 中，却从未声明——因此全新安装无法复现测试环境。相反，`tokenizers`、`huggingface-hub` 和 `PyYAML` 虽然列在其中，却没有被任何代码导入或要求，它们只是 `mistralai` 1.x 的遗留项。该文件现已重新生成，完整包含仅由直接依赖项构建的 venv 中的全部依赖闭包。`pip-audit` 未在新依赖集中发现任何已知漏洞。
    - **`.github/dependabot.yml`**（新增）启用 pip 和 github-actions 的每周版本更新。次版本和补丁版本合并到一个 PR 中——如果每个补丁升级都单独创建 PR，最终只会被忽略，而噪声正是及时更新的敌人；**主版本升级保持独立**，每项都需要通过真实调用验证。
    - **`scripts/check-deps-fresh.sh`**（新增，并接入 gate）让版本落后情况直接反映在项目结论中：Dependabot 只会提出建议，并不提供保证，其 PR 也可能不断堆积。主版本落后 → 失败；次版本落后 → 警告，因为长期处于红色的 gate 最终只会被忽略；PyPI 无法访问 → 本地明确跳过，**CI 中 fail-closed**，因为未执行的检查不等于成功。已从两个方向验证：它能准确捕获修复前的状态（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`），而对次版本落后只发出警告。

  - **本次 PR 审查产生的修复**——五个审查 agent 仔细检查了 diff；以下问题在修复前均已**通过测量复现**，其中两个还是同一版本前面部分引入的回归。
    - **已修复回归问题——`_NEWS_CITATION_REGEX` 存在指数级回溯。** 多段落修复在重复结构中引入了 `(?:[ \t]*$|[ \t]+.*)`：`[ \t]+` 与 `.*` 之间的空格归属存在歧义，而且这种歧义会随每次迭代成倍增加。在无法匹配该模式的 `>   texte` 行——完全合法的 Markdown 缩进——上测得：**14 行耗时 2 589 ms**，修复后为 0.04 ms，每增加一行耗时约增长 9 倍。在 `--news` 模式下，一段较长且不符合格式的块引用就足以让翻译卡死，直至任务超时，且无法识别原因。现在，重复结构会一次性消费整行（`\n^>(?![ \t]*—).*`），因此每次迭代只有一种匹配方式。已在包含 231 篇文章的真实语料库上验证：捕获结果**零差异**，仍为相同的 423 条引用，14 个多段落正文也仍然得到扩展。
    - **同时指定两个 provider flag 会在无提示的情况下按量计费。** `--use_codex --use_mistral` 会被接受；`_select_provider_client` 首先测试 Mistral，而 `_resolve_provider` 优先处理显式布尔值——两者最终都会选择 Mistral。因此，用户原本要求使用订阅配额，却在毫无警告的情况下被按量计费：这正是 `--use_codex` 存在的目的所要防止的故障模式。现在，六个 provider flag 都通过一个 `add_mutually_exclusive_group` 处理。**行为变更**：过去会被静默接受的双 provider 命令行组合，现在会在 `argument --use_mistral: not allowed with argument --use_codex` 处失败。
    - **工作结束门禁会在探针崩溃时错误地显示通过。** `scripts/check-release-ready.sh` 的十三项检查中有四项采用“捕获 stdout，若为空则下结论”的模式，却从不检查返回码：异常（文件被重命名、`FileNotFoundError`）会写入 stderr，使 stdout 保持为空，而检查却得出“没有问题”的结论。用于防止“一个 `exit 0` 什么也证明不了”这一陷阱的脚本，内部竟重现了同一陷阱。现在，辅助函数 `probe()` 同时要求返回码为零**并且**存在结束哨兵；探针也拒绝对空标记集合下结论——因为针对空集合的断言永远为真。演示：加入上述互斥组后，provider flag 改由 `*_group` 对象承载，旧正则 `parser\.add_argument\(` 不再匹配；**二十一个 flag 中有六个**被静默排除在检查范围外，而门禁仍显示通过。
    - **密钥扫描漏掉了六个 provider 中的四个。** 字符类 `[A-Za-z0-9]` 排除了连字符：`sk-proj-…`（当前 OpenAI 格式）和 `sk-ant-api03-…` 都会在第二个连字符处中断，而 `AIza…` 根本未被覆盖。现已扩展模式，并将 `.secrets.baseline` 排除在扫描之外。此外，`.env` 防护查询的是 `git diff --cached`，而它只能看到暂存区：一个**已经提交**的 `.env`——最糟糕的情况——永远不会出现在结果中。现在改为查询 `git ls-files`。
    - **Codex 的“令牌预热”实际上并未预热。** 实测表明：`codex login status` 不会触及 `~/.codex/auth.json`（修改时间和大小均未变化），其帮助文本写的是“显示登录状态”。然而注释却声称它会“执行一次且按顺序”刷新令牌，从而消除一次性轮换令牌并发刷新带来的风险。所宣称的保护并不存在；现在注释会准确描述代码的实际行为，而真正的防护仍是 `max_jobs=4`。此外，该检查现在会遵循此前被忽略的 `CODEX_BIN`——没有在 `PATH` 中配置 `codex` 的工作站，过去会因“未认证”而失败，给出误导性诊断。
    - **`.env` 是在子 shell 中加载的。** `detect_provider` 通过命令替换调用，因此其中导出的变量无法传回：在 `.env` 中定义的 `GROK_BIN`、`GROK_HOME` 或 `REGEN_MODEL`，对 `main()` 中执行的读取仍不可见，导致配置正确时也会得出“找不到 Grok 二进制文件”的结论。
    - **并发数比声明的上限高出 50%。** 防护放在 README/CHANGELOG 任务对启动之后：实测 `max_jobs=2` 的峰值为 **3**。Grok 的每周配额与 Chat/Imagine/Voice 共用且无法测量，因此脚本为自身设定的上限并未得到遵守。另一方面，最终计数只会显示，却从未与 28 比较——缺失文件不会被发现。
    - **Grok 输出契约：缺少 `stopReason` 现在会被视为失败。** 代码采用的是“`end_turn` **或不存在**”，而声明的契约要求 `end_turn`。如果 payload 中缺少该字段，或 CLI 更新后字段被重命名，防护就会静默失效。此外，`max_turn_requests` 不再被归类为速率限制（这是轮次预算耗尽：重试只会在付出 90 秒等待后得到相同结果），`quota` 也已从速率限制标记中移除——原因正是 `_codex_is_rate_limited` 的文档字符串早已说明、但 Grok 之前并未遵循的内容。
    - **Gemini 回退链现在按模型记忆结果。** 它过去会在每个分段都从 `minimal` 重新开始，尽管默认模型会拒绝该参数：正常路径因此会为每个分段额外付出一次 400 往返，并重复打印相同警告。重复数百次的警告最终会无人阅读——警告正是这样变成遮蔽物的。
    - **其他事项**：CI 中的拒绝消息被硬编码为 Codex，导致 `--use_grok_cli` 用户被引导至 `OPENAI_API_KEY`，而不是 `XAI_API_KEY`；`provider.capitalize()` 显示为“Grok_cli”和“Openai”；子进程基础层的注释将“shim”泛化到两个 CLI，但 Grok 二进制文件是原生 ELF（正确理由是“会生成自身子进程的代理”）；`subprocess` 上的十二项 SAST 发现已标记为 `# nosec` / `# nosemgrep` 并附有理由，因为不使用 `shell=True` 的列表形式使注入无法发生，而且文档内容从不通过 argv 传递。
    - **任何密钥都不再进入代理型子进程。** 按名称维护的拒绝列表只保护了**计费**不变量（Codex 不得包含 `OPENAI_API_KEY`，Grok 不得包含 `XAI_API_KEY`）。实测表明：每个子进程仍会接收到**另外七个密钥**——Anthropic、Mistral、Google 和 Gemini 的密钥、另一个 CLI 的密钥，以及 `OPENAI_BASE_URL`；后者并非密钥，却会改变流量的路由方向。而这两个 CLI 都是**代理**，且 Grok 代理在许多 Linux 工作站上运行时无法应用 OS sandbox。现在改为**按名称模式**过滤（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`），不再依赖名称列表，因此即便用户在自己的 `.env` 中添加代码未知的变量，也能得到覆盖。CLI 不需要其中任何变量：认证信息存放在 `~/.codex` 和 `~/.grok` 中，从不位于环境变量里——已通过两个 provider 分别在加固环境中完成**真实翻译**验证。
    - **测试**：新增文件 `tests/test_review_hardening.py`（21 项测试），锁定 provider flag 的互斥性、`stopReason` 契约、news 正则的线性复杂度、CI 拒绝消息、Gemini 记忆机制，以及子进程环境中不得存在任何密钥。最后这项断言是**通用的**——即使密钥未被任何列表命名，它也会失败——而原有的清除测试只是其常量的镜像，除了自身循环失效外无法检测任何问题。完整测试套件现有 **311 项测试**。

  - **两个新的 Grok provider**：`--use_grok`（xAI API，密钥 `XAI_API_KEY`，按量计费）和 `--use_grok_cli`（官方 Grok Build CLI，从 Grok 订阅额度中扣除——原理与 `--use_codex` 相同）。
    - **API 模式，约 40 行代码**：由于 xAI endpoint 与 OpenAI 兼容，客户端和 `_call_openai` 均按原样复用，只有 `base_url` 发生变化。只需一项适配，而且所有 provider 都能从中受益：`finish_reason` 现在接受 `end_turn`，这是 xAI 生成的格式，而 OpenAI 生成的是 `stop`。模型：`grok-4.6`（质量）和 `grok-4.3`（经济）。需要注意的是，Grok 的经济模型仍是仓库中最昂贵的——每百万 token 为 $1.25/$2.50，而 `mistral-small-latest` 为 $0.15/$0.60：选择该 provider 是为了模型多样性，而非价格。
    - **CLI 模式**：以 Codex 为基础，但根据实际情况存在四项必要差异——prompt 通过文件传递（`--prompt-file`，CLI 不读取 stdin，而放在 argv 中的分段会在 `ps` 中可见）；输出是 stdout 上的单个 JSON 对象（既不是 JSONL，也不是 `-o` 文件）；订阅仅提供 `grok-4.6` 和 `grok-4.5`；sandbox 无法应用（见下文）。子进程启动逻辑与 Codex 一同抽取至 `_codex_run_process`，未改动其余已经过测试的 Codex provider。
    - **实测表明，`exit 0` 什么也证明不了**：未认证时，CLI 会将 `{"type":"error","message":"Not signed in."}` 写入 **stdout**，返回码却是 **0**。请求被拒绝或轮次超限时行为也相同。因此，输出契约要求同时满足四个条件：返回码为 0、不存在错误 payload、`stopReason == end_turn`，且文本非空。预检遵循同样的逻辑：`grok models` 即使在已登出状态下也以 0 退出，只有 stdout 中出现“not authenticated”才能据此作出判断。
    - **隔离：明确接受并记录这种不对称性。** Codex 运行于 `--sandbox read-only` 中，而 Grok sandbox 在许多较新的 Linux 工作站上无法应用，原因是两个相互独立、且没有 `sudo` 就无法规避的系统问题：从 Ubuntu 24.04 起，AppArmor 会阻止非特权用户命名空间（`bwrap: setting up uid map: Permission denied`，已在 Grok 之外复现）；当 `/run/podman` 位于 `0700` 中时，容器运行时 socket 的拒绝列表会失败（resolver 仅捕获 `ErrorKind::NotFound`，EACCES 会成为致命错误）。核心陷阱在于：无法应用的**内置**配置文件会在无提示的情况下以非隔离模式启动。因此，脚本默认不请求任何配置文件，也绝不会静默回退——它会在 stderr 上发出警告。保护依赖 CLI 的 `--deny` 规则，其中包括兜底规则 `*`；这是唯一经实测为 _fail-closed_ 的层（带未知前缀的规则会使启动被拒绝）。可以使用 `GROK_TRANSLATE_SANDBOX=read-only` 强制要求隔离；此时如果机器无法满足要求，启动就会失败。
    - **防护措施**：从子进程环境中移除 `XAI_API_KEY`、`GROK_API_KEY` 和 `GROK_SANDBOX`（密钥会切换为按量计费；继承的 `GROK_SANDBOX` 会强制使用无法应用的配置文件，并产生误导性消息），禁用 MCP/hooks/skills/agents 开关，设置 `--disable-web-search`、`--no-subagents`、`--no-plan`，使用一次性 workdir，在 CI 中拒绝运行，超时时终止整个进程组，并在触发速率限制时执行退避。`--max-turns` 固定为 6，而不是 1：计数器会在工具轮次之后递增，设为 1 会截断输出。
    - **配额**：Grok 配额池按周计算，并且**与 Chat、Imagine 和 Voice 共用**，也没有任何命令能显示它——这与 Codex 不同，后者可通过 `account/rateLimits/read` 量化用量。因此，`regen_translations.sh` 将并发限制为 2，并明确发出警告。
    - **测试**：新增文件 `tests/test_grok_provider.py`（24 项测试）。完整测试套件现有 **290 项测试**。
  - **已修复 Bug——英文多段落引用仅得到部分保护（`--news` 模式）**：作为引用正文，`_NEWS_CITATION_REGEX` 只接受一系列**连续的** `>` 行。一旦一条引用跨越多个段落（段落间由空的 `>` 行分隔），就只有最后一个段落会被捕获并替换为占位符；之前的段落会被发送给 LLM，随后以翻译后的形式返回——这与 `--news` 所要保证的目标完全相反。现在，重复结构允许内部存在空的 `>` 行，并改为非贪婪匹配，从而在斜体行之前的空 `>` 处停止，而不是遇到第一个空行就停止。
    - **实测影响范围**：在包含 198 篇文章的真实语料库中，419 条引用里有 11 条受到影响。没有出现回归——新正则捕获的引用数量完全相同，只有多段落正文得到扩展（408 个正文保持不变，11 个得到扩展），归属行 `> — …` 仍不可能被吸收到正文中（保留了 lookahead）。
    - **端到端证明**：在一篇 69 ko 的文章上执行 ja/ar 翻译时，一条引用的第一段以前在日语中会被翻译成 `> GLM-5.3がオープンウェイト化。`，在阿拉伯语中也同样被翻译；现在则保持为 `> GLM-5.3 is now open-weight.`。英文引用行数从 9 恢复到 10，与源文一致。
    - 需要注意的是，下游验证器无法发现该缺陷，因为它们只检查引用是否存在，而不检查引用是否完整。
  - **默认 provider 的实测成本节省**：只要模型名称以 `gpt-5` 开头，`_openai_extra_kwargs` 就会发送 `reasoning_effort="medium"`，即使处于 `--eco` 模式也不例外。在 `gpt-5.4-mini` 上翻译一个十词句子的测量结果：`medium` → 45 个 reasoning token 和 65 个输出 token；`none` → 0 个和 14 个。推理对翻译毫无帮助，却会在每个文件的每个分段上产生费用。现在，`--eco` 模式下的默认值改为 `none`，其他情况下仍为 `medium`；通过 CLI 显式传入的值仍具有更高优先级。除 `low`/`medium`/`high` 外，`--reasoning_effort` 现在还接受 `none` 和 `xhigh`（并非所有模型都接受全部取值：例如 `gpt-5.4-mini` 会拒绝 `minimal`——现有的无参数重试机制会处理这种情况）。
  - **SDK 更新与 Gemini 迁移**：`google-generativeai`（支持已于 2025-11-30 终止，仓库已归档）被统一 SDK **`google-genai`** 取代——使用 `genai.Client(api_key=...)`，再调用 `client.models.generate_content(model=, contents=, config=)`，系统 prompt 通过 `system_instruction` 传递，而不是与分段拼接。`mistralai` 升级至 **2.9.4**（import 改为 `from mistralai.client import Mistral`；旧方式会抛出 `ImportError`，已在 wheel 中验证），`anthropic` 升级至 **0.125.0**，`openai` 升级至 **2.54.0**——这些都是迁移到 `httpx2` 之前的最新版本，以免 venv 中同时存在两套 HTTP 栈。`httpx` 0.28.1 和 `pydantic` 2.13.5 因此解除锁定。
  - **由真实测试而非文档捕获的两个回归问题**：
    - `anthropic` ≥ 1.0 会在客户端拒绝非流式调用，只要其 `max_tokens` 表明调用可能超过 10 分钟（`ValueError: Streaming is required...`）。该防护在 0.34.2 中并不存在，因此会破坏所有使用 `max_tokens=32768` 的 Claude 调用。现已通过显式设置 `timeout` 修复（`CLAUDE_TIMEOUT`，默认 900 s），从而避免为了只使用完整响应的调用而切换到流式模式。
    - 只有 Gemini 模型目录中的一部分模型接受 `thinking_level="minimal"`：`gemini-3.1-flash-lite` 支持它，而 `gemini-3.7-flash` 和 `gemini-3.1-pro-preview` 会返回 400 拒绝。因此引入 `_gemini_generate_with_fallback`，形成 `minimal` → `low` → 不使用 thinking_config 的回退链，沿用现有 OpenAI fallback 的模式——优化参数绝不能导致翻译失败。
  - **默认模型已更新**，每个模型均通过真实调用验证：OpenAI `gpt-5.5` → **`gpt-5.6-terra`**（28 个任务的 batch 成本降低 60%），`gpt-5.4-mini` → **`gpt-5.6-luna`**（降低 73%）；Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**（更便宜且更新），`claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（不含日期的规范 ID）；Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**，`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（稳定版本，且比 `3.5-flash-lite` 更便宜）。
 Mistral 保持不变，`mistral-large-latest` 仍是四者中性价比最高的。需要注意的是：不存在比 `gemini-3.1-pro-preview` 更新的 Gemini Pro 系列模型——2026 年 5 月发布的 Gemini 3.5 Pro 从未正式推出；3.5/3.6/3.7 系列仅有 Flash。
  - **切换 Gemini 前进行实测 A/B 测试**：使用 `gemini-3.1-pro-preview` 和 `gemini-3.7-flash` 将 `README.md` 翻译成日语。结构严格一致（21 个列表、18 个代码块、13 个 HTML 链接、13 张图片，所有 URL 均保留），耗时分别为 **8 秒和 48 秒**。由于没有任何公开 benchmark 比较这两个模型在翻译或非拉丁文字方面的表现，否则此次切换只能基于简单推测。
  - **Claude 响应块过滤**：`_call_claude` 在未过滤类型的情况下执行 `block.text for block in response.content`。采用自适应推理的模型（Sonnet 5 及更高版本）会插入一个 `thinking` 块，该块提供 `.thinking` 而非 `.text`——翻译会在第一个片段遇到不透明的 `AttributeError` 时失败。现在会排除 `thinking`、`redacted_thinking`、`tool_use` 和 `tool_result` 块（采用排除列表，以继续兼容携带文本的未知类型），如果响应中完全没有文本块，则抛出明确错误。每次调用都会传递 `thinking={"type": "disabled"}`。
  - **重新同步 `MODEL_TOKEN_LIMITS`**：移除退役日期已过的模型（`magistral-*` 系列于 2026-07-31 退役，`gemini-2.0-*` 于 2026-06-01 退役，`gemini-3-pro-preview` 于 2026-03-09 退役，以及 `claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。修正限制：Mistral 128K → **256K**（Large 3 / Small 4 代）、Gemini 1 000 000 → **1 048 576**（实际输入限制）、`claude-opus-4-5` 200K → **1M**、`gpt-5.6-*` 系列 400K → **1.05M**。新增 Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest` 和 `ministral-*` 系列。需要注意的是：这些限制仍仅供参考，因为 `translate()` 会将分段上限设为 `min(16000, limite)`。

  - **`--use_codex` provider**：第五个 provider，通过非交互模式驱动官方 Codex CLI（`codex exec`），而不是调用按用量计费的 API。翻译用量从已付费的 ChatGPT 订阅配额中扣除。这是 OpenAI 针对此用途记录的唯一方式：按套餐划分的可用性矩阵将“Codex SDK、`codex exec` 和可编程工作流”列为 Plus/Pro/Business/Enterprise 可用，而 `~/.codex/auth.json` 的 token 无法对 API Platform 调用进行身份验证（并且该脚本从不读取它们——身份验证及其刷新仍由 CLI 管理）。
  - **Codex 二进制文件可通过 pip 安装，不再仅限 npm**：`_resolve_codex_binary()` 依次在 `CODEX_BIN`、`PATH`，然后在 OpenAI 发布的官方 Python package **`openai-codex-cli-bin`** 中查找二进制文件（这是 `openai-codex` SDK 的依赖项）。因此，Python 项目无需再全局安装 npm 即可使用 `--use_codex`。该 package 未添加到 `requirements.txt`：二进制文件约为 250 MB，如果加入，就会迫使所有用户为一个可选 provider 安装它。已完成端到端验证：当 `codex` 不在 `PATH` 中时，解析过程能够找到 package 内的二进制文件，并在 6 秒内完成完整翻译。
  - **“订阅模式”保证**：从子进程环境中移除 `OPENAI_API_KEY` 和 `CODEX_API_KEY`。若没有此保护，`.env` 中存在的密钥可能会让 Codex 在没有任何可见提示的情况下切换为按用量计费——而该 provider 的存在正是为了避免这种情况。
  - **通过测试锁定 CLI 陷阱**：
    - 即使 prompt 已作为参数传入，`codex exec` **仍会**读取 stdin：如果不关闭 stdin，命令会一直等待到超时，且从不调用模型（复现结果：180 秒后以 exit 124 退出，零字节）。因此必须使用 `communicate(input=...)`。
    - 通过 npm 安装的 `codex` 是一个 Node shim，它通过 `spawn` 启动真正的 Rust 二进制文件：后者是 Python process 的**孙进程**，在 `subprocess.run(timeout=)` 执行 `SIGKILL` 后仍会存活，并继续消耗配额。因此需要 `Popen(start_new_session=True)` + `os.killpg`。
    - CLI 即使已经发出 `turn.failed`，仍可能以 0 退出：除返回码外，还会检查 JSONL 输出（`--json`）；如果返回码为 0 但缺少 `-o` 文件，则抛出明确错误，而不是生成空片段。
  - **rate limit 的 back-off**：CLI 未实现任何内部 retry（`max_retries = 0`）。分类依据 JSON payload 的结构（`status: 429` / `error.type`），而不是子字符串——“quota”一词既会出现在可恢复的 429 中，也会出现在永久性的 `insufficient_quota` 中。
  - **CI 防护**：如果定义了 `CI` 或 `GITHUB_ACTIONS`，则拒绝 `--use_codex`。订阅身份验证并非为共享 runner 设计，OpenAI 也明确不建议在公共仓库中使用此工作流。
  - **模型**：`gpt-5.6-sol`（质量）和 `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` 系列由 CLI 和 API Platform 共用，但 ChatGPT 账户并不拥有其中所有模型的使用权：allowlist 在服务器端应用，不进行本地验证，使用不常见的模型会触发警告。在 Plus 套餐中，每个 5 小时窗口内，Luna 可提供 250–2 000 条消息，而 Sol 仅为 10–100 条：对于所有批处理任务，推荐使用 `--eco` 模式。
  - **已修复 bug——`regen_translations.sh` 尽管完全成功却仍以错误退出**：`trap ... EXIT` 引用了 `failed_log`，后者是 `main()` 的一个 `local` 变量，在 trap 执行时已经不存在。在 `set -u` 下，这会引发 `failed_log: unbound variable`，使脚本在 28 个翻译均正确的情况下仍以 1 退出——这会导致 `release.sh --auto`（`set -e`）在重新生成后立即中断，而此时正处于成本最高的阶段。该变量现已改为全局变量，trap 会检查其是否存在。一个有益的副作用是：此前被此错误掩盖的真实翻译失败，现在会再次显示在最终摘要中。
  - **`REGEN_MODEL`**：`regen_translations.sh` 的新环境变量，可覆盖 provider 的默认值并强制指定模型，例如使用 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`，通过订阅配额中的高端模型重新生成，而不是使用面向吞吐量的 `--eco` 模型。
  - **`regen_translations.sh`**：`REGEN_PROVIDER=codex` 可通过明确选择启用（绝不自动检测，以免在用户不知情的情况下消耗订阅配额）。在开启并行处理前，会先以串行方式刷新一次 token——由于 Codex refresh 具有轮换性且只能使用一次，并发 job 会使 `codex login` session 失效——并发数会降至 4。
  - **相关 refactor**：`_dispatch_provider_call` 通过一个返回 provider 名称的 `_resolve_provider()`，将参数数量从 8 个减少至 6 个，不再让第四个布尔值贯穿整个调用链。显式布尔值的优先级仍高于 `args`，以保留那些使用最小化 `Namespace` 调用 `translate(..., use_mistral=True)` 的测试。
  - **测试**：新增文件 `tests/test_codex_provider.py`（48 项测试），涵盖 argv、净化后的环境、禁止前言的契约、静默失败、timeout/killpg、back-off、preflight、provider 解析、Gemini 推理级联、Claude 块过滤以及多段落新闻引用。完整测试套件共 290 项测试。
  - **实际验证**：通过 Codex 将项目的 `README.md` 翻译为 **14 种语言**，其结构与参考翻译严格一致（14 个代码块、24 个标题、25 行表格、13 个 HTML 链接、13 张图片、19 个 URL，代码块逐字符完全一致，placeholder 残留为零）。对于一篇 69 KB 的新闻文章，在 `--news` 模式下，`gpt-5.6-luna` 和 `gpt-5.6-sol` 的输出均通过了下游应用对 en/ja/ar 的验证。通过 `account/rateLimits/read` 测得的消耗量：在 `--eco` 模式下始终低于计数器的舍入阈值（5 小时窗口的 0%）。

- **1.9.2** 修复带嵌套括号或法语前缀的新闻归属 URL 提取问题（2026-05-11）：

  - **已修复 bug**：`_protect_news_quotes` 中的归属 URL 提取使用 regex `re.search(r"\((.+?)\)", attribution)`（对括号内内容进行惰性捕获）。对于 `(relayé par [@user sur X](https://x.com/.../123))` 形式的归属信息（嵌套括号：外层 `(` + Markdown link 的 `]()`），捕获会在遇到第一个 `)` 时停止 → 字符串被截断且包含法语前缀：`relayé par [@user sur X](https://x.com/.../123`（缺少末尾的 `)`）。结果：`_validate_news_post` 在翻译后的输出中查找该字符串时总会失败（原因有二：`)` 被截断 + “relayé par”被翻译为 `relayed by`/`weitergeleitet von`/……）。完整的 low → medium → high → gpt-5.5 级联流程均无法通过。
  - **修复**：regex 改为 `re.search(r"\]\(([^)]+)\)", attribution)`——专门匹配 Markdown link 的 `](url)`，并且**仅捕获纯 URL**（不含法语前缀，也不会截断）；在翻译过程中由 placeholder `#URL{N}#` 保持其不变。可稳健处理以下两种问题模式：
    - `(relayé par [@account sur X](url))`——嵌套括号
    - `via [@source](url)` 或 `selon [@author](url)`——没有外层括号的法语前缀
  - **测试**：在 `test_silent_failure.py` 的 `TestNewsCitationExtraction` 类中新增 2 项测试：
    - `test_extract_attribution_url_with_nested_parens`（准确复现 Genspark CEO E2B bug 的案例）
    - `test_extract_attribution_url_with_french_prefix`（使用 `via` 的变体）
  - **覆盖缺口**：`check-editorial-coverage.py` 会验证编辑语法，但不会验证 translator 是否能够处理。一个可能的改进（不在 v1.9.2 范围内）是添加一项检查，在 dry-run 中模拟归属信息提取，以便在发布**之前**检测高风险模式。

- **1.9.1** 修复翻译 marker 注释中 CTA 标签的 i18n 问题（2026-05-10）：

  - **已修复 bug**：翻译文件顶部 marker 横幅内 CTA 链接的 `[Voir le projet sur GitHub ↗]` 标签，在所有目标语言中都仍然是**法语**，而没有遵循 `target_lang`。LLM 永远看不到该标签（它由 Python 端组装，以保留 URL 和 repo slug），因此翻译阶段无法纠正。从 v1.9 添加 `marker` 格式以来，这一直是一个静默 regression。
  - **修复**：新增常量 `_VIEW_PROJECT_LABELS`，将 15 种语言映射至各自的本地化标签。`_translation_note_invariants(target_lang)` 和 `_assemble_translation_note_paragraphs(phrase, target_lang)` 现在会传递目标语言。如果语言未知，则 fallback 到 `fr`（确保安全，不会发生 KeyError）。
  - **测试**：调整 `test_source_emits_three_paragraphs_repo_title_description_link`（target_lang `ja` → 预期为日语标签）。新增 2 项测试：`test_source_link_label_localized_per_target_lang`（对 7 种语言进行参数化，涵盖拉丁文字、表意文字和 abjad）和 `test_source_link_label_falls_back_to_french_for_unknown_target`。总计：`test_translation_note_position.py` 中有 40 项测试（原为 38 项）。
  - **向后兼容**：签名带有默认值 `target_lang="fr"`——未提供 `args.target_lang` 的外部程序调用方无需修改即可继续使用。
- **1.9** 修复静默失败 + 完整质量工具链 + 多位置翻译注释（2026-05-07）：
  - **多位置翻译注释 + “嵌入卡片”标记格式**：
    - 新增 CLI 选项（增量添加，默认行为不变 → **非破坏性变更**）：
      - `--note_position {top,bottom,both}`（默认：`bottom`）：将注释放置在译文文件的顶部、底部或两处。
      - `--note_format {legacy,marker}`（默认：`legacy`）：
        - `legacy` 严格复现 v1.8 的行为（粗体段落 `**…**`），达到**逐字节一致**。
        - `marker` 输出一个不可见的 Markdown 链接引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），随后是结构化的**三段式块引用**，以呈现类似“GitHub 仓库嵌入卡片”的效果：使用行内代码显示项目标题（`**\`ai-powered-markdown-translator\`\*\*`）、由 LLM 翻译的描述，以及带可见箭头的 CTA 链接（`[Voir le projet sur GitHub ↗](URL)`）。构建时可由 remark 插件处理（参见 jls42.org 博客 → 插件 `remark-translation-banner`）。
    - **绝不发送给 LLM 的不变量**：仓库标题和 GitHub URL 在描述性语句翻译完成后由 Python 端组装。LLM 永远不会看到 slug `ai-powered-markdown-translator` 或 `https://github.com/jls42/...`，从而确保渲染方式、大小写和 scheme 均不会被更改。
    - **感知 frontmatter 的插入**：在 `top` 或 `both` 模式下，注释会插入到 YAML frontmatter 的结束 `---` 块**之后**（保障 Astro Content Collections / gray-matter 的安全性）。辅助函数 `_split_frontmatter` 检测文件开头的 `---\n…\n---\n` 并保持其完整性；如果 frontmatter 已开启但没有结束围栏，则**抛出 `RuntimeError`**（该文件会被列入 `failed_files`，而不会写入位置错误的注释）。
    - **基于白名单的模型名称清理器**：`_sanitize_model` 将 `[A-Za-z0-9._:/-]` 以外的所有字符替换为 `_`，为空时回退到 `unknown`。这与 Astro remark 插件端的验证器保持一致，并会中和可能破坏标记格式的字符（空格、引号、括号、逗号等）。
    - **内部重构**：`_append_translation_note`（1 个单体函数）→ 7 个纯辅助函数（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。构建器与组合器分离（构建器返回不含分隔符的纯块，组合器根据位置应用 `\n\n`）；生产代码和源码辅助函数共用同一个三段式组装器。
    - **`_quote_lines` 保留空行**：为每一行添加 `> ` 前缀，并将空行转换为单独的 `>`。这使 mdast 能够将块引用识别为三个独立段落（标题／描述／链接），而不是一个带换行的段落。
    - **自适应 `_build_translation_note_block`**：根据 LLM 保留的段落数量处理（3 = 完整卡片格式，2 = 语句 + 链接，1 = 回退格式）。检测到 Markdown 链接 `](` 时，单段落回退内容**不再用 `**...**` 包裹**，避免 `<strong>` 包裹链接时产生不稳定的渲染效果。
    - **向后兼容**：`_compose_with_notes` 中的 `getattr(args, "note_position", "bottom")` 和 `getattr(args, "note_format", "legacy")` 使用兼容处理——不含这些属性的 Namespace（现有测试、外部编程调用）无需修改即可继续工作。
  - **修复长篇翻译的静默失败**：
    - 对所有 provider（OpenAI、Mistral、Claude、Gemini）执行译后语言验证：确定性层（在输出中找到与源文逐字一致的片段）+ 概率层（`langdetect`）
    - `finish_reason`／`stop_reason` 白名单：任何不在白名单中的状态（截断、content_filter 等）均抛出 `RuntimeError`
    - Claude 的 `max_tokens`：`4096` → `32768`（避免 16k 分段出现潜在截断，并为 FR→JA/ZH/KO/AR/HI 的跨文字系统转换留出余量）
    - 感知标题的分段：优先选择分段后半部分的 H2/H3（使每个分段均从一个完整的语义章节开始）
    - 将错误传播至非零退出码：`translate_markdown_file` 返回类型化状态 `success`／`failure`／`skipped`；只要有一个文件失败，`main()` 就会执行 `sys.exit(1)`（单文件和批量模式均适用）
    - 为所有 provider 添加空内容防护、源文／译文比例合理性检查（源文 ≥ 500 个字符且译文不足其 5% 时拒绝）、代码占位符验证（`#CODEBLOCK`／`#INLINECODE`）、LLM 输出后规范化（修复与标题粘连的分隔符／链接），以及不使用 `reasoning_effort` 的 `BadRequestError` 重试
    - 新增依赖 `langdetect==1.0.9`
  - **pre-commit 质量工具链**（“完整 EurekAI 类型”，14 个钩子）：
    - Pre-commit：ruff（检查 + 格式化）、shellcheck、prettier（md/yaml/json）、detect-secrets（保护 4 个 API 密钥）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（空白字符、文件结尾、大文件、shebang 等）
    - Pre-push：mypy（渐进式宽松模式）、Opengrep SAST（translate.py + scripts/）、pip-audit（初期报告模式）、unittest discover（tests/ + scripts/tests/）
    - `scripts/` 中使用 `./venv/bin/python` 的本地包装器
    - `scripts/audit_verdict.py`：pip-audit JSON 解析器，包含 11 个 unittest；由 jls42-astro 解析器改写而成的 Python 版本
    - 修复了最初的 7 个 ruff 违规项：B904（raise from）×2、B007（未使用的 dirs）、C408（dict 字面量）、C419（列表推导式）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizard 暂时排除 `translate.py`（4 个函数的 CCN 为 21–47，计划重构）——对 scripts/ 实施严格门禁
  - **SonarCloud + 全面覆盖率**：
    - GitHub Actions 工作流 `SonarCloud`（sonarcloud.yml + sonar-project.properties）：每次 push 和 pull request 时进行分析，并通过 `coverage.xml` 生成覆盖率
    - README 顶部添加 11 个 SonarCloud 徽章（Quality Gate、Security/Reliability/Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）
    - `tests/test_silent_failure.py`（`unittest` 标准库）：覆盖静默失败错误链中的六个环节
    - `tests/test_orchestration.py`（新增 79 个测试）：覆盖 `translate.py` 的编排层（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` 的 TypeError + BadRequestError 回退、o1 系列提示词格式，以及 `_validate_translation_output` 的提前返回分支）
    - `scripts/tests/test_audit_verdict.py`：通过 subprocess 覆盖 `main()`（stdin/stdout）和 `if __name__ == "__main__"` 块
    - **新增代码覆盖率**：75.5% → 约 98%（translate.py 98%，scripts/audit_verdict.py 97%）
  - **测试**：`tests/test_translation_note_position.py` 覆盖位置 × 格式矩阵（包括端到端的 `marker+top|bottom|both` 和 `legacy+top|bottom|both`）、多行前缀处理、逐字节向后兼容性（黄金字面量）、清理器、frontmatter 拆分（包括未闭合围栏时抛出异常）、三段式格式、两段式回退、单段落 + Markdown 链接防护，以及一个关键保护测试 `TestLLMPayloadExcludesInvariants`，用于断言标题和 URL 永远不会发送给 LLM。**190 个测试通过**，零回归。
  - 文档：`README.md`（法语 + 14 种翻译），包含徽章；`CLAUDE.md`（pre-commit 工作流 + 详细的 CI 监控）；重新生成 28 种翻译
- **1.8** `--news` 模式 + 2026 年模型升级（2026-03-17，标签 `v1.8`）：
  - 更新默认模型（2026 年 3 月）：
    - OpenAI 高质量模型：`gpt-5` → `gpt-5.4`
    - OpenAI 经济型模型：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 高质量模型：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - 新增 `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）和 `gemini-3.1-pro-preview`（1M）的 token 限制
  - 初始 `--news` 模式：使用占位符 `#NEWSQUOTE\d+#` 保护英文引文、`LANG_FLAGS` 映射（15 种语言），并按目标语言处理旗帜
  - 恢复前验证新闻占位符（回归问题：LLM 删除占位符时，会静默生成缺失引文的输出）
  - 使脚本 `regen_translations.sh` 可移植（使用绝对路径，不依赖 pwd）
  - 在 README/CHANGELOG 的语言栏中新增法语链接，并重新生成 28 种翻译
- **1.7** 新功能：
  - 新增 `--keep_filename` 选项，在翻译时保留原始文件名
  - 支持通过 `.env` 文件自动加载 API 密钥
  - **保留行内代码**：翻译过程中现在会保护反引号（`` `...` ``）
  - 改进系统提示词：
    - 更好地处理 YAML frontmatter 中的引号
    - 保护模板变量 `{variable}`
    - 禁止添加未经要求的译者注
  - 已在 364 个文件上成功测试（jls42.org 博客迁移）
- **1.6** 新功能：
  - 支持使用 Google Gemini API 进行翻译（`--use_gemini`）
  - 更新 2026 年默认模型：
    - OpenAI：`gpt-5`（高质量）、`gpt-5-mini`（经济型）
    - Claude：`claude-sonnet-4-5`（高质量）、`claude-haiku-4-5`（经济型）
    - Gemini：`gemini-3-pro-preview`（高质量）、`gemini-3-flash-preview`（经济型）
  - 新增经济模式（`--eco`），可使用更快且成本更低的模型
  - 支持单文件翻译（`--file`），无需遍历目录
  - 新的简化命名模式：`{base}-{lang}.md`
  - 新增 `--include_model` 选项，以保留包含模型名称的旧格式
  - 支持未列出的模型，并使用默认 token 限制（128k）
  - README 已翻译为 14 种语言
- **1.5** 改进：
  - **更新 API 密钥和默认模型：**
    - **OpenAI：**从 `DEFAULT_MODEL_OPENAI` 更新至 `"gpt-4o"`。
    - **Mistral AI：**从 `DEFAULT_MODEL_MISTRAL` 更新至 `"mistral-large-latest"`。
    - **Anthropic Claude：**新增 `DEFAULT_ANTHROPIC_API_KEY`，并将 `DEFAULT_MODEL_CLAUDE` 更新至 `"claude-3-5-sonnet-20240620"`。
  - **优化翻译提示词：**
    - 丰富了直接翻译和翻译注释的提示词，使其更加清晰高效，其中包括有关保留元数据和特定格式元素的详细指令。
  - **代码重构：**
    - 使用 `Mistral` 类替换 `MistralClient`，以初始化 Mistral AI 客户端。
    - 重新组织 import，提高可读性和可维护性。
    - 改进文本分段和代码块处理，以在翻译过程中保留原始格式。
  - **输出文件管理：**
    - 在输出文件名中调换模型与语言的顺序（例如 `f"{base}-{args.target_lang}-{args.model}.md"`），从而便于组织和查找译文。
  - **其他改进：**
    - 删除不必要的空行以清理代码。
    - 进行小幅调整，以改进脚本的结构和可读性。
- **1.4** 新功能：
  - 支持使用 Anthropic Claude API 进行翻译
  - 优化提示词，以提高清晰度和效率
  - 进行小幅调整，以提高代码的可维护性
- **1.3** 改进与新功能：
  - 改进代码块处理
  - 改进输出文件管理
  - 改进现有文件检测
  - 新增 `--force` 选项以强制翻译
  - 在输出文件名中调换模型与语言的顺序
- **1.2** 修复更新日志
- **1.1** 新增 Mistral AI API 支持
- **1.0** 初始版本——支持 OpenAI API

**使用 gpt-5.6-sol 将文章从法语翻译成中文。**
