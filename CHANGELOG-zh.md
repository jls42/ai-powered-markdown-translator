### 更新日志

🌍 [法语](CHANGELOG.md) | [英语](CHANGELOG-en.md) | [西班牙语](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [德语](CHANGELOG-de.md) | [日语](CHANGELOG-ja.md) | [韩语](CHANGELOG-ko.md) | [阿拉伯语](CHANGELOG-ar.md) | [印地语](CHANGELOG-hi.md) | [意大利语](CHANGELOG-it.md) | [荷兰语](CHANGELOG-nl.md) | [波兰语](CHANGELOG-pl.md) | [葡萄牙语](CHANGELOG-pt.md) | [罗马尼亚语](CHANGELOG-ro.md) | [瑞典语](CHANGELOG-sv.md)

- **1.13.0** Provider `--use_openrouter`：通往约 430 个模型的付费路由器，其中包括开放的中国模型（2026-09-05）：

  - **第九条 provider 路径，与第八条一同发布。** 1.12.0 未发布到 PyPI：OpenCode 和 OpenRouter 两个路由器一同推出。[OpenRouter](https://openrouter.ai) 只需一个密钥，即可访问此处其他任何 provider 均未提供的模型——Kimi、Qwen、DeepSeek、Z.ai——并通过统一额度按用量计费。由于 endpoint 与 OpenAI 兼容，使用的客户端与 xAI 相同；**这个 provider 的全部差异都集中在一次预检中**，其每条规则均源自对 API 的实测。

  - **同一个模型由数十家限额各异的托管商提供，而路由对此毫无感知。** 实测：`z-ai/glm-5.2` 有 33 家托管商，`z-ai/glm-5.3-flash` 有 23 家——其中一家将**输出限制为 2,048 个 token**。因此，一次长篇翻译会随机被分配到这 23 家之一，并在没有任何提示的情况下遭到截断。预检会读取 `/api/v1/models/{modèle}/endpoints`，排除输出上限低于 8,000 个 token、状态异常或未声明任何上限的托管商，然后锁定其余托管商。仅使用 `provider.only` 而**不使用** `allow_fallbacks: false` 只代表一种偏好：路由器仍会转向已排除的托管商，锁定也就失去意义。如果没有任何托管商满足上限要求，命令便会停止：仍然继续翻译，就等于接受这项预检原本要防止的静默截断。

  - **推理按输出费率计费，而且许多模型默认启用推理。** 在 `z-ai/glm-5.2` 上使用同一个请求，响应为“确定”：**采用模型默认设置时产生 107 个补全 token，关闭推理后则为 2 个**。对于推理毫无帮助的翻译任务，这会让每个文件的每个分段成本相差 18 倍。因此，推理默认关闭。431 个模型中有 **288 个强制启用推理**（`reasoning.mandatory`），并会返回 `400 « Reasoning is mandatory for this endpoint and cannot be disabled »`：对于这些模型，预检会读取其接受的推理强度并请求最低值（见下一项）——推理强度会分配 **`max_tokens` 的一定百分比**，且推理会优先消耗这部分额度，所以随意选择一个值只会转移产生空白页面的风险，而非降低风险。

  - **强制启用推理的模型会收到其接受的最低推理强度，而这一决定来自实测。** 最初的选择是什么都不发送，以免替模型擅自猜测。在 `z-ai/glm-5.3-flash` 上进行的验证表明，该模型在目录中的默认值为 `max`；这一选择会使输出在翻译结束前**于 32,768 个 token 处被截断**——十四种语言中有两种丢失。增大额度也无济于事：推理强度会按百分比分配额度，推理量也会随之增长。因此，provider 会在预检时读取 `supported_efforts` 并请求最低值；若目录未公布任何可用值，则回退为“不指定”。对出错语言进行反向验证：此前它因额度耗尽而失败，如今可在 9 分钟内完成，且结构与源文档完全相同。

  - **上游托管商发生故障时，现在会明确指出其名称。** 路由器会将这种情况规范化为 `finish_reason=error`，同时 `native_finish_reason` 为空——在两种语言上各实测一次，均恰好发生于 750 秒。原来的通用消息会让人误以为文档或分段存在问题；现在它会明确说明故障位于供应商一侧，而且重试通常即可解决。

  - **`finish_reason=length` 搭配空输出并不代表截断。** 这表示额度在生成第一个有效字符之前就已被推理耗尽——实测为 15,850 个推理 token，仅产生 148 个有效 token。这两种情况需要采取相反的措施：在前一种情况下，缩小分段毫无作用。消息现在会明确区分二者。另外两项保护措施同样来自实测：上游托管商失败时，路由器会返回**状态码 200，但响应体中只有错误信息**（`choices[0]` 会抛出晦涩的 `TypeError`，从而掩盖原始消息）；上下文窗口则从目录中读取并写入 `MODEL_TOKEN_LIMITS`——目录中有 44 个模型的 `DEFAULT_TOKEN_LIMIT` 值不正确，其中两个模型的上限仅为 4,095 个 token。

  - **`--model fournisseur/modèle` 为必填项，而且会在任何网络访问之前验证其格式。** OpenRouter 并非供应商：模型选择涉及价格、许可和数据处理方式，不能代替用户作出决定。由于 slug 会插入预检 URL，因此验证并非单纯的易用性考虑，而是防止向其中注入路径的保护措施：两个路由器共用的带命名空间正则表达式接受 `a/b/..`，因此会明确拒绝父目录段。`--eco` 不起作用，而且会明确告知这一点。

  - **修正了三处表述，其中一处原本错误。** OpenAI 关于 `codex exec` 的警告针对的是在共享 runner 上注入个人会话文件，并非代码仓库是否公开；README、CLAUDE.md 和代码此前均对此作了错误引用。OpenCode 的身份验证位置在 1.18.27 中发生了变化（现为 `opencode.db` 中的 `credential` 表，而不再是 `auth.json`）；“这里永远不会读取它”这一不变条件仍然成立，只是地址已经过时。最后，OpenCode 章节不再把从未经过验证的路径描述为等价选项：Zen 网关和 Ollama 已完成端到端实测，而 GitHub Copilot、LM Studio 和 llama.cpp 尚未实测，README 现在会明确说明这一点。

  - **开展了一轮实测，并在 README 中加入了推荐模型表。** 针对三组文档执行了三百多次翻译——一篇在 `--news` 模式下内容密集的博客文章、采用标准 Markdown 的本 README，以及四个直接取自 GitHub 的知名项目 README——目标涵盖十四种语言。表格区分了此前常被混淆的两件事：翻译是否**完成**，以及其**结构是否与源文档完全相同**。三个模型在两份密集文档中从未丢失任何信息：`gemini-3.7-flash`、通过 ChatGPT 订阅使用的 `gpt-5.6-sol`，以及通过 OpenRouter 使用的 `z-ai/glm-5.2`——它们唯一的偏差，是在一两种语言中漏掉了一对 `**`。核心结论是：**决定性因素是文档密度，而非 `--news` 模式**。通过订阅使用的 Grok 在博客文章上十四次中失败十三次，却在十六次公开 README 翻译中成功十四次；反向验证表明，原因是处理长分段时出现偏离。表格自身也附有警告：结果并不完整，且具有时效性；耗时不能用于排名，正确做法仍是在自己的文档上进行实测。

  - **结构比较器在发布数据前得到修正，因为它会对非拉丁文字产生两种误报。** URL 后跟一个全角右括号 `）` 时，原先止于 `)` 的正则表达式无法正确截断；即使 URL 完全相同，提取出的字符串也会有所不同。另一个问题是，法语中占五行的引用在中文中可能只占三行，导致按行计数减少。这两项修正均通过反向验证：删除 URL、章节或行内代码仍然会被检测到。如果不修正，Gemini 和 Codex 公布的结果将分别是十四种语言中十一种和十二种，而非十三种和十二种。

  - **测试**：新增文件 `tests/test_openrouter_provider.py`（76 项测试）——模型验证及父目录段拒绝、托管商锁定（上限、状态、未声明上限、共同最低值）、`allow_fallbacks` 始终为假、根据 `mandatory` 关闭或保留推理、完整输出契约（状态码 200 中的错误、没有选项、区分空白页面与截断、异常的 `finish_reason`、空内容）、目录无法访问时预检以关闭状态失败、缺少 slug 以及没有健康托管商、flag 互斥性和文件名标签。完整测试套件现有 **502 项测试**。

  - **重构：将单个 4,253 行模块拆分为多个模块，不改变任何一行行为。** `src/aipmt/translate.py` 被拆分为 `config`、`markdown`、`segmentation`、`guards`、`placeholders`、`news`、`prompts`、`notes`、`naming`、`pipeline`、`cli` 以及子包 `providers/`（每个 provider 一个模块，以 `base` 为基础，`registry` 负责解析与分派）。每次移动都对应一个提交，并有机械化证据：验证器会把包中所有顶层 AST 节点与参考快照进行比较，检查每个符号的位置、安全标记是否逐字保留，以及是否不存在未跟踪文件——这些临时工具会在下一版本中移除。可见的变化包括：`aipmt.translate` 变为一个门面，以对象身份不变的方式重新导出原模块未带 `_` 前缀的 64 个名称（`__all__` 包含其中九个，即受支持的 API；其余为兼容性别名），并停止重新导出被 `import *` 顺带收集的 29 个依赖项和标准库名称；不再支持直接执行该文件（`python src/aipmt/translate.py`）——`aipmt` 和 `python -m aipmt` 仍是两种受支持的形式；公共函数的 `__module__` 现在指向其定义模块；SDK 改为在加载 `.env` 后导入，而不再提前导入，目前未发现影响。427 项测试的标识符全部保留，并迁移至其实际测试的模块：此前通过门面执行的 91 个 patch 现在改为指向实际查找相应名称的模块（实测其中两个即使没有对应 patch 也仍会通过）；另有七项契约测试锁定门面行为。各项 gate 的工具在第一次移动之前便已重写，确保它们不会因为停止检查而误报通过——Lizard 的作用域改为目录并设定下限、从构建出的 parser 读取 flag、按包设置覆盖率下限，`release.sh` 则枚举受跟踪模块。
  - **修复（pull request 审查）**：若 OpenRouter 的目录记录不含 `context_length`，则直接拒绝，而不再把默认的 128,000 个 token 写成实测值——这一做法此前还会一并关闭“模型未列出”警告；当 `finish_reason` 为空时（文档记录的类型为 `string | null`），以托管商的原始原因作为依据，因为 `max_tokens` 的值为 `length`。如果选项自身携带错误，则拒绝与之同时出现的部分内容，并采用与规范化上游故障相同的消息——其中同时包含托管商详情、原始原因和建议。OpenCode 遇到 `part: null` 事件时会返回自身的契约错误，而非 `AttributeError`；若 JSONL 流中存在无法解析的事件行，则拒绝整个流，而非接受部分文本。当三个代理式 CLI 进程在调用期间收到 `SIGTERM` 时，会终止代理的整个进程组——regen 的 `timeout` 此前会让代理继续存活并消耗额度——而且进程组的 `SIGKILL` 始终遵循宽限期，即便 shim 正常退出，其孙进程仍可能存活。拆分过程中分离的一对 `# fmt: off` / `# fmt: on` 已重新合并；`--reasoning_effort` 的帮助信息现在会列出使用它的四个 provider。
  - **修复（第二轮审查）**：向 OpenRouter 请求的输出上限现在会预留 prompt 和分段所占用的上下文空间——`context_length` 同时覆盖输入和补全，而目录中有六个模型此前会在没有输入空间的情况下发送请求；上下文过短时会在产生任何费用之前拒绝请求。在不存在 POSIX 进程组的平台上，代理式 CLI 的基础层会依次回退到 `terminate` 和 `kill`，避免让 `AttributeError` 穿过超时保护并导致等待继续延长。现在会把 OpenCode 的 `429` 标记作为数字查找，而非进行子字符串匹配；此前像 `err_84290b` 这样的错误标识符会触发 90 秒退避，最终却仍然失败。最后，预检会显示非规范的 OpenRouter endpoint：项目中的一个 `.env` 就足以设置该值，而随后发送的会是真实密钥。
  - **安全性：项目中的 `.env` 无法再重定向 API 调用。** `find_dotenv(usecwd=True)` 会从当前目录及其父目录中查找文件：不可信的目录树——例如刚克隆的代码仓库——可以在其中设置 `OPENROUTER_BASE_URL`、`XAI_BASE_URL` 或 `OPENAI_BASE_URL`（最后一个由 SDK 自行读取），无需知道任何密钥；随后，来自环境或用户配置的真实密钥便会被放入发送给第三方服务器的授权标头。过滤采用模式而非列表：对已安装 SDK 的调查表明，它们会读取十二个路由变量，仅 Anthropic 客户端就会读取其中六个——手工编写的枚举会漏掉一半。因此，项目层中的所有 `_BASE_URL`、`_API_BASE` 或 `_ENDPOINT` 变量、代理和证书存储设置（指向受控的证书颁发机构，会使拦截器看起来与真实服务器无异），以及 `XDG_CONFIG_HOME` 和 `APPDATA` 都会被拒绝：设置后两项等同于决定哪个文件构成用户层，从而可绕过过滤器。这些变量仅可来自用户控制的两个层级：已导出的环境和 `~/.config/aipmt/.env`。此外，读取项目层时不会进行插值：`load_dotenv` 默认会展开 `${VAR}`，而包含 `NOM_ANODIN=${OPENAI_API_KEY}` 的不可信 `.env` 会把真实密钥复制到一个子进程模式过滤无法识别的名称下——随后，该密钥便会进入 `codex exec` 的环境，违反已声明的不变条件。最后，拒绝消息只显示变量名称：形如 `https://${CLE}@hôte/` 的 URL 会把插值后的密钥泄露到日志中，即便该变量最终遭到拒绝。拒绝信息会输出到 stderr，并说明处理方式——企业中继应在用户配置中声明。
  - **修复：OpenRouter 的输出额度现在按每次调用计算。** `context_length` 同时覆盖输入和补全，而按拉丁文本校准的固定预留量无法提供任何保证：使用 `o200k_base` tokenizer 实测，16,000 个字符在法语中相当于 3,200 个 token，在日语中为 12,300 个，在 emoji 中则为 17,500 个。因此，额度会根据实际发送的文本计算，并以其 UTF-8 字节数作为上界：对于所有采用字节合并的 tokenizer——字节级 BPE、带字节回退的 SentencePiece，以及目录所使用的各类方案——一个 token 至少对应一个字节；在 OpenRouter 会路由到数十种未知 tokenizer 的情况下，这是此处唯一可用的上界估算。任何平均比例都不适用——一个辅助平面表意文字可低至每个 token 1.33 字节，一个组合字符则可低至 1.00 字节——如今输入与输出在设计上都能容纳于上下文窗口中。若某个分段对所选模型而言过于密集，请求会在调用之前被拒绝，而不是在产生费用之后才失败。

- **1.12.0** Provider `--use_opencode`：通过开源代理 OpenCode 连接用户选择的供应商——本地模型、无需账户的免费服务、订阅或密钥（2026-09-04）：
  - **第八条 provider 路径，其性质与前七条不同。** [OpenCode](https://opencode.ai)（MIT）并不是模型供应商，而是一个通往用户已在 OpenCode 中配置的模型的_路由器_：API key、订阅（GitHub Copilot、ChatGPT、SuperGrok）、提供**无需账户**的免费模型的 OpenCode Zen 网关，或**本地**模型（Ollama、LM Studio、llama.cpp）。脚本以非交互模式驱动 `opencode run`，如同驱动 Codex 和 Grok 一样，并复用同一套子进程基础设施（独立进程组、超时时先执行 `SIGTERM` 再执行 `SIGKILL`、始终关闭 stdin、清理环境变量）。已通过**两次真实翻译**验证：使用 `opencode/mimo-v2.5-free` 将整个 README 翻译成英文——耗时 49 秒，仅一轮处理，结构与源文件完全一致（32 个标题、26 个代码块闭合标记、18 个链接、37 个 URL、37 行表格、135 段 inline code）——以及使用 `ollama/qwen2.5:7b` 在本地且完全不使用任何密钥翻译测试文件。

  - **`--model provider/modèle` 是必填项，这是有意为之。** 如果没有 `--model`，OpenCode 会退回自身的默认值；在全新安装中，该默认值是 `opencode/big-pickle`，即免费的“stealth”模型，其交互内容可能被用于训练——实际测量表明，作出响应的正是这个模型。静默地替用户做出这一选择，恰恰属于本仓库所追查的隐形切换；因此错误消息会明确指出用于列出模型的命令（`opencode models`），并给出三个示例（本地、免费、订阅）。`--eco` 不起作用，并会明确说明这一点。只有在明确请求时，`--reasoning_effort` 才会原样作为 OpenCode 的 `--variant` 传递。

  - **隔离以实测为准，而非凭空假定。** 一份 inline 配置（`OPENCODE_CONFIG_CONTENT`，在 OpenCode 的合并顺序中位于最后，因此优先于用户配置但不会替换它）定义了一个 `aipmt` agent，并拒绝其使用所有工具（`permission: {"*": "deny"}`）：注册表甚至不再向模型提供这些工具；当要求它“列出文件并运行 `id`”时，它会回答自己没有工具。session 共享已禁用，外部 plugins 已排除（`--pure`），绝不使用 `--auto`，工作目录临时创建且为空。经测量发现并切断了两种静默注入：如果没有 `OPENCODE_DISABLE_CLAUDE_CODE`，用户的 `~/.claude/CLAUDE.md` 会进入**每一个** prompt（仅一句“你好”的输入就从 186 tokens 增至 515 tokens）；如果没有 `OPENCODE_DISABLE_PROJECT_CONFIG`，当前目录中的 `AGENTS.md` 也会被注入——其中一条“每次回答都以 BANANA 结尾”的指令确实被应用到了翻译中。全局 `~/.config/opencode/AGENTS.md` 仍会被注入：没有开关可以排除它，而通过挪用 `XDG_CONFIG_HOME` 来绕过它，也会同时隐藏用户的供应商。对此选择如实记录，而不是拼凑变通方案。

  - **`exit 0` 证明不了任何事情；面对第三套 CLI，仍采用同样的防范方式——同时处理它特有的两个陷阱。** 未知的 `--agent` 不会让 `opencode run` 失败：它只在 stderr 上发出警告，然后**静默**回退到启用了工具的 coding agent。因此，如果 inline 配置未被采用，翻译就会由一个具备写入能力的 agent 执行；所以输出契约除验证以下条件外，还会检查该消息不存在：返回码为 0、没有 `error` 事件、没有 `tool_use`、最后一个 `step_finish` 为 `stop`（`length` 表示响应被截断）、文本非空。第二个陷阱：错误 JSON 事件是**不透明的**——只有“Unexpected server error. Check server logs for details.”和一条简单引用——真正的原因（`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`、`ProviderAuthError`……）只存在于日志中。因此要使用 `--print-logs --log-level ERROR` 并读取 stderr 的 `error="…"` 字段，同时忽略其后的 Bun trace。这样，未知模型会在一秒内失败，并明确指出原因。`--title` 还顺带避免了一次无关的 LLM 调用：如果没有它，OpenCode 会通过在 `small_model` 上额外执行一轮来生成 session 标题。

  - **Secrets：采用与 Codex 和 Grok 相同的模式过滤，仅有一个具名例外。** `OPENCODE_API_KEY` 会被保留：这是 OpenCode 自身的密钥（Zen 网关、Go 订阅），按名称指定给 OpenCode——它相当于其 `auth.json`，并非由 aipmt 管理或可能计费的密钥。供应商在 OpenCode 中配置（`opencode auth login`、`opencode.json`），绝不在 aipmt 的 `.env` 中配置，因此 aipmt 的任何密钥都不会到达子进程。与订阅型 CLI 不同，CI 中不会拒绝这种用法：在 runner 上使用 API key 或自托管模型都是合法场景。

  - **防路径穿越保护现在检查插值后的值，而不是原始值。** `provider/modèle` 包含一个会被 1.10.0 的保护机制拒绝的 `/`——这在当时是合理的，因为 `--model` 会被插入文件名 `--include_model`。现在，文件名标签会在任何插值发生前，将 `/`、`\` 和 `:` 替换为 `-`（`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`，因为 `:` 在 Windows 下非法），上游保护机制检查的也是这个标签：`../../evil` 会在目标目录下变成普通文件名 `doc-en-..-..-evil.md`，只有 `..` 仍会被拒绝，`--target_lang ../x` 也一样。`_ensure_within_directory` 的范围保护仍作为第二层防线，保持不变。

  - **免费模型与本地模型的实测结果。** `opencode/mimo-v2.5-free` 翻译一个段落需 16 秒，翻译此 README 需 49 秒；`opencode/big-pickle` 翻译 200 个词需 40 秒，而且两次并发请求持续 5 分钟都没有响应，而单独执行时每次都能完成；`opencode/nemotron-3.5-lightning-free` 在 3 分钟内没有任何响应。因此，`REGEN_PROVIDER=opencode` 必须配合 `REGEN_MODEL` 使用，并行数为 **2 jobs**。本地方面，Ollama 经常将上下文配置为 4,096 tokens，而分段最长可达 16,000 个字符：必须将 `Modelfile` 与 `PARAMETER num_ctx 32768` 配合使用；质量则取决于模型——在测试文件上，一个 7B 模型颠倒了列表顺序并破坏了一个代码块闭合标记，而网关模型完整保留了所有内容。

  - **本仓库的翻译从此绝不会再通过计费 API。** 只要 `.env` 中遗留了密钥，`regen_translations.sh` 就会选择 OpenAI API，而 Codex 仅作为 opt-in。准备此版本时发生的正是这种情况：28 份翻译先通过 OpenAI API 完成，随后印地语 CHANGELOG 又通过 Gemini API 完成，尽管 ChatGPT 订阅存在的意义正是避免按量付费。现已移除密钥自动检测：**默认使用 Codex，并配合 `gpt-5.6-sol`**，即质量模型；`openai`、`gemini` 和 `grok` 除 `REGEN_PROVIDER` 外还要求提供 `REGEN_ALLOW_PAID_API=1`，以具名例外的形式确保规则在作出决定时立即生效；未知的 `REGEN_PROVIDER` 会直接失败，而不是回退到 API。十项测试锁定了默认行为、拒绝行为和例外行为。此版本的 28 份翻译已全部通过 Codex 重新完成。

  - **rate limit 的 back-off 已抽取为公共实现**（`_retry_on_rate_limit`）：Codex 与 Grok 的循环除标签外完全相同，再复制第三份就会超过重复率阈值。三个 CLI 错误都派生自同一个 `_CliCallError`；一项测试禁止其中任何一个脱离该继承关系，否则共享循环将无法再捕获它。

  - **测试**：新增文件 `tests/test_opencode_provider.py`（61 项测试）——完整输出契约、agent 回退、从日志读取原因、文本 part 去重并忽略合成 part、超时时终止进程组、429 back-off、模型必填及验证、无 secret 的 preflight、二进制解析、dispatch 接线、文件名标签与路径穿越反证。`tests/test_review_hardening.py` 将 flags 互斥性和无 secrets 要求扩展到新 provider。gate 现在要求记录 **22 个 flags** argparse。完整测试套件共 **382 项测试**。

- **1.11.1** 文档修正：README 终于说明了七条 provider 路径（2026-09-03）：

  - **1.11.0 的 PyPI 页面写的是“4 APIs + Codex CLI”。** 代码实际提供七条路径——通过 API 使用 OpenAI、Mistral、Claude、Gemini 和 Grok；通过订阅使用 Codex（ChatGPT）和 Grok，不按量计费。开篇介绍和 _Multi-Provider_ 条目都遗漏了两种 Grok 模式，14 份翻译也重复了这一错误。由于 package 的长描述在每个版本发布后即固定不变，要修正展示页面就必须更新版本号：这正是此版本存在的唯一原因。**没有任何代码变更。**
  - `CLAUDE.md` 已与发布引入的内容保持一致：gate 计数器（16，`--full` 中为 17）、十一个启用的 workflows、`gh pr checks` 中不可见的两个 Sonar/Codacy 计数器（hotspots、Codacy API）、由 `ruff-format` 导致的 `# nosemgrep` 移动、OIDC 交换所要求的 GitHub environments，以及 _pending publisher_ 不会保留名称这一事实。

- **1.11.0** 发布至 PyPI：先执行 `pip install ai-powered-markdown-translator`，再执行命令 `aipmt`，无需克隆仓库（2026-09-03）：

  - **单文件脚本变为可安装 package。** `translate.py` 从根目录移至 `src/aipmt/translate.py`，并提供 console 入口点 `aipmt` 及其等价形式 `python -m aipmt`。参与贡献仍需克隆仓库——测试、28 份翻译及质量工具都位于其中——但使用时不再需要。

    - **import 名称是 `aipmt`，绝不能是 `translate`**，因为冲突真实存在且不会发出提示。PyPI package `translate`（v3.8.1，最近一次上传于 2026-07-06）会安装一个同名目录。已在 venv 中复现：目录优先于 module，`translate.main` 消失，入口点在 `AttributeError` 处崩溃——而 `pip check` 仍以 rc=0 回答“No broken requirements found”。用户仅仅执行一次 `pip install translate`，就足以在没有可用诊断信息的情况下破坏 CLI。对真实 wheel 的反证结果：在该 package 之上安装 `pip install translate`，`aipmt --help` 在安装前后均为 rc=0，两套 CLI 可以共存。
    - **distribution 名称较长，命令较短。** `ai-powered-markdown-translator` 让 package 可通过 PyPI 搜索找到；对于尚不了解该项目的人来说，单独使用缩写根本无法找到，而此次发布的目标恰恰是让它能够被发现。经核查后排除了两个看似合理的候选：`ai-markdown-translator` 自 2024 年起已被 npm 上一个用途相同的工具占用，比本仓库早 17 个月；`aimt` 与 `aim`（v3.29.1）仅差一个字母，后者还是同一领域的活跃 package——这是最容易造成长期混淆的组合。顺带一提，这里还有一个方法上的陷阱：`pypi.org/project/<nom>/` 会对任何名称返回 200（反机器人页面），只有 JSON API 的结果可信。
    - **采用 `src/` layout，而不是扁平 package。** 扁平 package 本可保留测试中的六处 `sys.path.insert(..., "..")`，而这恰恰是其缺陷：它们会 import 源码树而不是实际 package，从而掩盖任何打包错误。实际代价只是增加一条替换规则。

  - **密钥终于只需配置一次。** 已安装的 CLI 原本没有任何持久化配置：只能依赖环境变量和当前目录中的 `.env`。`find_dotenv` 确实会一直向上查找到系统根目录，因此**在个人目录下工作时**能找到 `~/.env`，但在其他位置工作时就无法找到——这种覆盖取决于从哪里启动命令，而不是有意的设计选择。因此新增第三层：`~/.config/aipmt/.env`，其优先级低于现有两层。

    - **优先级并非硬编码**，而是由 `override=False` 推导而来，即 `load_dotenv` 的默认值：每一层只填补前一层留下的空缺。因此顺序为环境变量 → 项目的 `.env` → 用户配置；这一点通过行为测试而非结构测试验证——交换两次调用的顺序会使测试失败，移除第三层也一样。
    - **有意选择 `.env` 格式，而不是 TOML**：`python-dotenv` 已经是 dependency，该语法已在 15 份 README 中记录，同一文件也可同时用于两个作用域。无需新增 dependency 或语法。路径会遵循 `XDG_CONFIG_HOME`，前提是其值为**绝对路径**——规范要求忽略相对值，否则配置位置将再次取决于当前目录——Windows 下则使用 `APPDATA`。
    - **另有两个方案被排除，并有明确原因。** 系统 keyring（`keyring`）在桌面设备上更安全，却会在 headless 环境中失败——服务器、容器、CI——而这些恰恰是批量翻译的典型使用场景；它适合作为 opt-in，却不适合作为默认值。`--api-key` flag 会让密钥进入 shell 历史记录，并使其在 `ps` 中可见。
    - **缺少密钥时不再显示调用栈。** 用户以前会收到一段指向 `site-packages` 的 Python stack，以及一条只提到“环境或 .env”却不说明第二项应创建在哪里的消息。现在，它会列出三个位置及各自的准确路径，并以状态码 2 退出。这个保护网被**刻意限制在很窄的范围内**：仅在配置阶段对 `except ValueError` 生效。若包裹整个执行过程，翻译期间发生的真实 bug 就会被转换成令人安心的提示——这正是本仓库所追查的故障模式。一项测试会读取 `main()` 的源码，以禁止这种做法。

  - **修复——工具安装后会忽略用户的 `.env`。** 不带参数的 `load_dotenv()` 并不会从当前目录向上查找，而是从调用方文件开始，因此会从 `site-packages` 开始。已使用真实 console 入口点从一个拥有自身 `.env` 的项目中启动并完成实测：`find_dotenv()` 返回 `''`，密钥没有加载，而 `find_dotenv(usecwd=True)` 可以找到它。只要工具仍仅从克隆的仓库中运行，这个 bug 就不存在；发布后它会成为系统性问题，而唯一症状是在配置正确的情况下提示 API key“缺失”。

  - **三个 gates 原本会在完全停止检查的情况下仍显示为绿色。** 它们被有意安排在移动前加固：在变更发生后才编写本应捕获该变更的保护机制，并不能证明任何事情。每项保护在原始仓库中均为绿色，而在迁移后的副本中都会变为红色——两个方向都经过了实测。

    - **Lizard 会悄无声息地忽略不存在的路径**：rc=0，并显示“0 file analyzed”。复杂度 gate 原本会从 158 个函数 / 2247 nloc 变为 3 个函数 / 34 nloc，同时生成零字节输出。现在 scope 是一个数组，其中每个条目都会检查是否存在。
    - **对不存在的 module 执行 `coverage run --source=` 不会失败**：只在 stderr 发出警告，无论 unittest 还是 `coverage xml` 都返回 rc=0，并且仍会发布报告——statements 数从 1453 减至 141。项目会因为几乎不再被分析而显得健康。报告现由两个下限守护：总量和测得的最大文件。
    - **翻译新鲜度探针在结构上无法识别调用形式**：它以 argparse flags 为锚点，而文件重命名恰好不会改变这些 flags。复现结果：module 已移动，15 份 README 仍记录着一条不存在的命令，判定结果却是“没有过期翻译”。因此，第 7 节会检查调用**形式**而不是选项，Lizard hook 也会与脚本的实际 scope 对照——当其 key `files:` 不再匹配时，pre-commit 不会失败，而是会直接跳过该 hook。
  - **`requires-python = ">=3.10"` 不再只是一项声明。** `sonar-project.properties` 早已声明支持 3.10-3.12，却从未实际运行过这些版本，因为开发工作站上只有 3.12——这是一个内部矛盾，发布后便会暴露。现在，测试 workflow 会在 3.10、3.11 和 3.12 上运行测试套件，并安装软件包，从而验证其公开版本边界。

  - **设定下限，不设上限。** `requirements.txt` 仍是经过测试的 lock，`[project.dependencies]` 则成为公开契约：若发布 lock 中的确切版本，任何同时使用其他软件包的用户都可能遭遇冲突。也不设置 `<N+1` 上限——它会与 `check-deps-fresh.sh` 直接矛盾，后者会在任何主版本落后时让 release gate 失败。这组最低版本能够成功解析，而反向验证 `openai==1.0.0` 会以 `ResolutionImpossible` 退出，证明该检查确实能够作出区分，而非一概接受。此外，还有一项保护禁止 `pyproject.toml` 的版本与 CHANGELOG 中的版本不一致：PyPI 不允许重复使用版本号。

  - **已在全新 venv 中进行端到端验证**：约 70 Ko 的 wheel 仅包含 `aipmt/*.py`、dist-info 和许可证；`aipmt --help` 返回 rc=0，并包含 22 个 flags；`python -m aipmt` 显示“usage: aipmt”，而不是“usage: \_\_main\_\_.py”；通过 `pipx` 安装后可正常运行；最重要的是，**从任意用户目录实际完成了 fr→en 翻译**，粗体、列表、内联代码、链接和 URL 均得到保留，代码块未被翻译。迁移前已有的 318 项测试全部通过，且迁移前后的标识符列表逐字节完全相同——证明没有任何测试被禁用的是这一点，而不是“OK”；另为三层配置新增十二项测试，总计 330 项。

- **1.10.0** `--use_codex` Provider（使用 ChatGPT 订阅配额）、SDK 与模型更新，以及 news 多段落引用修复（2026-08-29）：

  - **安全审查——PR 设置了两项保护措施，却没有在所有路径上真正落实**：

    - **Codex preflight 将整个 `.env` 都传给了二进制文件。** `_codex_preflight` 调用 `subprocess.run` 时**没有传入 `env=`**：子进程继承了完整的 `os.environ`，也就是 `load_dotenv` 所加载的全部 `.env`。通过带检测功能的伪二进制文件测得：**七项秘密信息**进入了 preflight——六个 provider 的密钥加一个 `GITHUB_TOKEN`——而其对应路径 `_grok_preflight` 中则为**零项**，因为后者确实传入了 `env=_grok_env()`。这是 PR 内部的不一致：相距仅几行的 `_strip_secret_env` 正是为了维持这一不变量而存在。现已抽取共享的 `_codex_env_base()`，供两条路径共同使用；修复后的测量结果为：两边均有 0 项秘密信息。
    - **“`--deny` fail-closed”属性并未涵盖实际采用的写法。** 注释将整个 Grok 隔离机制的合理性建立在这一点上：带有未知前缀的规则会导致程序拒绝启动。在 `grok 1.0.13` 上实测发现，此验证**仅适用于带括号的写法**：`--deny 'CeciNestPasUnOutil(*)'` 会拒绝启动（“unknown tool prefix”），而 `--deny 'CeciNestPasUnOutil'` 则会被静默接受。然而 `GROK_DENY_RULES` 只使用了裸名称——因此，如果 xAI 侧重命名工具，在本就无法应用 OS sandbox 的工作站上，唯一经过实测的隔离层会被移除，却不产生任何信号。八条具名规则现已改为 `Prefix(*)`，每条都作为 CLI 已知前缀进行验证；catch-all 规则 `*` 保持原有字面形式，这是唯一被接受的写法。另有测试防止退回未经验证的形式。
    - **其余部分也已完整验证**：不存在命令注入（始终使用列表形式，从不使用 `shell=True`，文档内容通过 stdin 或 `--prompt-file` 传递）；不存在不安全的反序列化（仅使用 `json.loads`，并带有类型保护）；在七种恶意载荷上均未发现路径遍历修复的绕过方法；而且 CLI 确实应用了 `--deny '*'`（在读取 workdir 之外的文件时观察到 `DENY_ENFORCED`）。
    - 此外，上文新增的新鲜度检查绕过了自身原则：如果某个软件包的 PyPI 请求失败，它会被静默跳过，gate 仍保持绿色。现在，它会统计实际完成比较的软件包数量，并在覆盖不完整时失败。

  - **依赖项已更新至当前水平，并增加两道防线，避免再次长期落后**：

    - **落后情况真实且持续已久**：`openai` 从 2.54 升至 **3.6.0**，`anthropic` 从 0.125 升至 **1.2.0**，`certifi` 从 2024.8.30 升至 **2026.7.22**——也就是说，用于验证所有 provider TLS 调用的根证书存储落后了两年。已确认原因：**项目中根本没有 `.github/dependabot.yml`**。缺少该文件时，GitHub 只会启用 _security updates_，且 Dependabot 仅会针对受 CVE 影响的依赖提出 PR——这解释了为何它更新了 `urllib3` 和 `idna`，却任由两个 SDK 落后整整一个主版本。
    - **两个主版本可以共存且不会冲突**，这与此前的推断相反：`openai` 3.x 和 `anthropic` 1.x 已迁移到 **`httpx2`**，而 `mistralai` 和 `google-genai` 仍使用 `httpx<1`，但它们是两个不同的发行包。先通过实际安装验证，随后又对 **7 条 provider 路径进行了端到端测试**——OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI 和 Grok CLI——每项输出中的内联代码和链接都得到保留。“避免两套 HTTP 栈”只是一项偏好，并非阻碍：实测结果已经给出定论。
    - **`requirements.txt` 未能描述真实环境**：`google-auth`、`cryptography` 和 `opentelemetry` 栈安装在工作 venv 中，却从未被声明——因此，全新安装无法复现测试环境。反过来，`tokenizers`、`huggingface-hub` 和 `PyYAML` 虽列在其中，却没有被任何代码导入或需要，它们只是 `mistralai` 1.x 遗留的残余。该文件现已重新生成，内容是仅从直接依赖构建的 venv 的完整依赖闭包。`pip-audit` 未在新依赖集中发现任何已知漏洞。
    - **`.github/dependabot.yml`**（新增）启用每周版本更新，覆盖 pip 和 github-actions。次版本与补丁版本更新合并到一个 PR 中——每个补丁更新都单独提出 PR，最终只会被忽略，而噪声正是更新工作的敌人；**主版本更新则各自独立**，且每项都必须通过真实调用进行验证。
    - **`scripts/check-deps-fresh.sh`**（新增，已接入 gate）让依赖落后状态直接反映在项目判定结果中：Dependabot 只能提出更新，无法保证更新完成，其 PR 也可能不断堆积。主版本落后 → 失败；次版本落后 → 警告，因为长期保持红色的 gate 最终会被忽略；PyPI 无法访问 → 本地明确 skip，**CI 中 fail-closed**，因为没有执行的检查不能视为成功。已从正反两面完成验证：它能够捕获修复前的确切状态（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`），而对次版本落后仅发出警告。

  - **本次 PR 审查产生的修复**——五个审查 agent 对 diff 进行了全面检查；以下所有问题在修复前都已通过实测复现，其中两个还是本版本前文所引入的回归。

    - **已修复的回归——`_NEWS_CITATION_REGEX` 存在指数级回溯。** 多段落修复在重复结构中引入了 `(?:[ \t]*$|[ \t]+.*)`：`[ \t]+` 与 `.*` 之间的空格归属存在歧义，而这种歧义会随着迭代次数增加而成倍增长。对无法匹配该模式的 `>   texte` 行进行测量——这些是完全合法的 Markdown 缩进——结果为：**14 行耗时 2 589 ms**，修复后仅为 0.04 ms，每增加一行，耗时约增长 9 倍。在 `--news` 模式下，一段较长但不符合格式的 blockquote 就足以让翻译冻结，直至 job 超时，且无法识别原因。现在，重复结构会一次性消费整行（`\n^>(?![ \t]*—).*`），使每次迭代只有一种匹配方式。已在包含 231 篇文章的真实语料库上验证：捕获结果**零差异**，仍为相同的 423 条引用，14 个多段落正文也仍然得到完整扩展。
    - **同时使用两个 provider flag 会静默产生按量计费。** `--use_codex --use_mistral` 会被接受；`_select_provider_client` 首先检测 Mistral，而 `_resolve_provider` 优先采用显式布尔值——两条路径最终都会选择 Mistral。因此，用户明明请求使用订阅配额，最终却被按量收费，而且没有任何警告：这正是 `--use_codex` 旨在防止的故障模式。现在，六个 provider flag 都会经过 `add_mutually_exclusive_group`。**行为变更**：此前会被静默接受的双 provider 命令行组合，现在会在 `argument --use_mistral: not allowed with argument --use_codex` 处失败。
    - **收尾 gate 在探针崩溃时仍显示绿色。** `scripts/check-release-ready.sh` 的十三项检查中，有四项采用“捕获 stdout，若为空则得出结论”的模式，却从不检查返回码：发生异常时（文件重命名、`FileNotFoundError`），错误写入 stderr，stdout 保持为空，于是检查得出“没有问题”的结论。用于防止“一个 `exit 0` 什么都不能证明”这一陷阱的脚本，自己却重现了同一陷阱。现在，辅助函数 `probe()` 会同时要求返回码为零且存在结束哨兵；如果标记集合为空，探针也会拒绝得出结论——因为对空集合的断言永远为真。演示结果：加入上述互斥组后，provider flag 会经过 `*_group` 对象，原有正则 `parser\.add_argument\(` 不再能够匹配；**二十一个 flag 中有六个**静默脱离检查范围，而 gate 仍显示绿色。
    - **秘密信息扫描漏掉了六个 provider 中的四个。** 字符类 `[A-Za-z0-9]` 不包含连字符：`sk-proj-…`（OpenAI 当前格式）和 `sk-ant-api03-…` 都会在第二个连字符处中断，而 `AIza…` 完全未被覆盖。现已扩展匹配模式，并将 `.secrets.baseline` 排除在扫描之外。此外，保护项 `.env` 查询的是 `git diff --cached`，而它只能看到 index：一个**已经提交**的 `.env`——最糟糕的情况——永远不会出现在结果中。现在，它改为查询 `git ls-files`。
    - **Codex 的“token warm-up”实际上并没有预热 token。** 实测发现：`codex login status` 不会触碰 `~/.codex/auth.json`（mtime 和大小均保持不变），其帮助文本写的是“Show login status”。然而，注释声称它会“按顺序执行一次”token 刷新，从而消除一次性轮换 token 并发刷新带来的风险。所宣称的保护并不存在；现在注释会如实描述代码行为，而真正的防护仍是 `max_jobs=4`。该检查现在还会遵循此前被忽略的 `CODEX_BIN`——没有把 `codex` 加入 `PATH` 的工作站此前会收到“未认证”的失败信息，这是误导性的诊断。
    - **`.env` 是在子 shell 中被 source 的。** `detect_provider` 通过命令替换调用，因此其中的 export 不会传播到父环境：在 `.env` 中定义的 `GROK_BIN`、`GROK_HOME` 或 `REGEN_MODEL` 对 `main()` 中的读取仍不可见，导致配置正确时也被判定为“找不到 Grok 二进制文件”。
    - **并发量比宣称的上限高出 50%。** 保护检查被放在 README/CHANGELOG 任务对启动之后：实测 `max_jobs=2` 的峰值为 **3**。对于 Grok，其每周配额与 Chat/Imagine/Voice 共享且无法测量，因此脚本设定的自我约束上限实际上没有得到遵守。至于最终计数，它虽然会显示，却从未与 28 比较——即便缺少文件也不会被发现。
    - **Grok 输出契约：缺少 `stopReason` 现在会被视为失败。** 此前代码采用“`end_turn` **或缺失**”的逻辑，而公开契约要求必须存在 `end_turn`。若 payload 缺少该字段——或者 CLI 更新后重命名了该字段——保护机制就会静默退化为 no-op。此外，`max_turn_requests` 不再被归类为 rate limit（它表示交互轮次预算已耗尽：重试只会在等待 90 秒后得到同样结果），`quota` 也已从 rate limit 标记中移除——原因正是 `_codex_is_rate_limited` 的 docstring 早已说明、但 Grok 此前没有落实的那一点。
    - **Gemini 级联现在按模型记忆结果。** 此前每个 segment 都会从 `minimal` 重新开始，但默认模型会拒绝它：正常路径因此每个 segment 都要承担一次 400 往返，并重复打印相同警告。一个重复数百次的 warning 最终将无人阅读——它就是这样变成遮蔽物的。
    - **其他事项**：CI 中的拒绝消息被硬编码为 Codex，会把使用 `--use_grok_cli` 的用户引导到 `OPENAI_API_KEY`，而不是 `XAI_API_KEY`；`provider.capitalize()` 显示的是“Grok_cli”和“Openai”；子进程基础层的注释将“shim”理由泛化到两个 CLI，但 Grok 二进制文件其实是原生 ELF（正确理由是“会生成自身子进程的 agent”）；`subprocess` 上的十二项 SAST finding 已标记为 `# nosec` / `# nosemgrep` 并附理由，使用不含 `shell=True` 的列表形式使注入无法发生，且文档内容从不通过 argv 传递。
    - **现在不再有任何秘密信息进入 agent 子进程。** 基于名称的 deny-list 只保护了**计费**不变量（Codex 不含 `OPENAI_API_KEY`，Grok 不含 `XAI_API_KEY`）。实测发现：**另外七项秘密信息**仍会进入每个子进程——Anthropic、Mistral、Google 和 Gemini 的密钥、另一个 CLI 的密钥，以及 `OPENAI_BASE_URL`；后者虽不是秘密信息，却可以重定向流量。然而，这两个 CLI 都是 **agent**，且 Grok agent 在许多 Linux 工作站上运行时无法应用 OS sandbox。现在，过滤依据改为**名称模式**（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`），不再依赖具名列表，因此也能覆盖用户在 `.env` 中自行添加、而代码并不知道的变量。CLI 不需要其中任何变量：认证信息位于 `~/.codex` 和 `~/.grok`，从不存放在环境变量中——已通过两个 provider 分别在强化环境下**实际完成翻译**予以验证。
    - **测试**：新增文件 `tests/test_review_hardening.py`（21 项测试），用于锁定 provider flag 的互斥性、`stopReason` 契约、news 正则表达式的线性复杂度、CI 拒绝消息、Gemini 记忆机制，以及子进程环境中不存在任何秘密信息。最后一项断言是**通用的**——即使密钥未被任何列表点名，它也会失败——而现有的清除测试只是其常量的镜像，除了检测自身循环失效外，无法发现任何其他问题。完整测试套件共 **311 项测试**。
  - **两个新的 Grok provider**：`--use_grok`（xAI API，密钥 `XAI_API_KEY`，按用量计费）和 `--use_grok_cli`（官方 Grok Build CLI，从 Grok 订阅额度中扣除——原理与 `--use_codex` 相同）。
    - **API 模式，约 40 行**：由于 xAI endpoint 与 OpenAI 兼容，client 和 `_call_openai` 均可原样复用，只有 `base_url` 需要更改。只需进行一处适配，而且所有 provider 都能从中受益：`finish_reason` 现在接受 `end_turn`，这是 xAI 输出的形式，而 OpenAI 输出的是 `stop`。模型：`grok-4.6`（质量）和 `grok-4.3`（经济）。需要注意的是，Grok 的经济模型仍然是仓库中最昂贵的——每百万 token 为 $1.25/$2.50，而 `mistral-small-latest` 为 $0.15/$0.60：选择这个 provider 是为了模型多样性，而不是价格。
    - **CLI 模式**：以 Codex 为蓝本，但存在四项由实际情况决定的差异——prompt 通过文件传递（`--prompt-file`，CLI 不读取 stdin，而 argv 中的片段会显示在 `ps` 中）；输出是 stdout 上的单个 JSON 对象（既不是 JSONL，也不是 `-o` 文件）；订阅只提供 `grok-4.6` 和 `grok-4.5`；sandbox 无法应用（见下文）。子进程启动逻辑与 Codex 一同提取到 `_codex_run_process` 中，未改动其余已经过测试的 Codex provider。
    - **经实测，`exit 0` 不能证明任何事情**：未认证时，CLI 会将 `{"type":"error","message":"Not signed in."}` 写入 **stdout**，且退出码为 **0**。请求被拒绝或超出轮次限制时也是如此。因此，输出契约要求同时满足四个条件：退出码为 0、没有错误 payload、`stopReason == end_turn`，且文本非空。preflight 遵循相同逻辑：即使未登录，`grok models` 也会以 0 退出，只有 stdout 中出现“未认证”字样才能据此判断。
    - **隔离：有意采用并明确记录的不对称设计。** Codex 运行于 `--sandbox read-only`，但 Grok 的 sandbox 在许多较新的 Linux 工作站上无法应用，原因是两个彼此独立的系统问题，若没有 `sudo` 就无法绕过：自 Ubuntu 24.04 起，AppArmor 会阻止非特权 user namespace（`bwrap: setting up uid map: Permission denied`，已在 Grok 之外复现）；当 `/run/podman` 处于 `0700` 状态时，容器 runtime socket 的 deny-list 会失败（resolver 只会捕获 `ErrorKind::NotFound`，EACCES 会成为致命错误）。核心陷阱是：无法应用的**内置** profile 会在不受隔离的情况下静默启动。因此，脚本默认不请求任何 profile，也绝不会静默回退——它会在 stderr 上发出警告。保护依赖于 CLI 的 `--deny` 规则，其中包括 catch-all `*`，这是经测量唯一具备 _fail-closed_ 特性的层（使用未知前缀的规则会导致启动被拒绝）。`GROK_TRANSLATE_SANDBOX=read-only` 可用于强制要求该保护；如果机器无法满足要求，启动就会失败。
    - **防护措施**：从子进程环境中移除 `XAI_API_KEY`、`GROK_API_KEY` 和 `GROK_SANDBOX`（密钥会切换为按用量计费；继承的 `GROK_SANDBOX` 会强制使用无法应用的 profile，并给出误导性消息），禁用 MCP/hooks/skills/agents 开关，并设置 `--disable-web-search`、`--no-subagents`、`--no-plan`、一次性 workdir、CI 环境拒绝运行、超时后终止整个进程组，以及针对 rate limit 的 back-off。`--max-turns` 被设为 6 而不是 1：计数器会在工具轮次结束后递增，设为 1 会截断输出。
    - **配额**：Grok pool 按周计算，并且**与 Chat、Imagine 和 Voice 共享**，没有任何命令可以显示配额——Codex 则可通过 `account/rateLimits/read` 量化消耗。因此，`regen_translations.sh` 将并发限制为 2，并明确发出警告。
    - **测试**：新增文件 `tests/test_grok_provider.py`（24 项测试）。完整测试套件共 **290 项测试**。
  - **已修复的 bug——多段落英文引文仅得到部分保护（`--news` 模式）**：`_NEWS_CITATION_REGEX` 只接受一串**连续的** `>` 行作为引文正文。一旦引文包含多个段落（由一个空的 `>` 行分隔），就只会捕获最后一个段落并将其替换为 placeholder；之前的段落会被发送给 LLM 并在返回时遭到翻译——这与 `--news` 所要保证的效果完全相反。现在，重复模式会接受内部的空 `>` 行，并改为非贪婪匹配，从而在斜体行之前的空 `>` 处停止，而不是在遇到第一个空行时停止。
    - **实测影响范围**：在包含 198 篇文章的真实语料库中，419 条引文里有 11 条受到影响。没有出现回归——新 regex 捕获的引文数量完全相同，只有多段落正文得到了扩展（408 个正文保持不变，11 个得到扩展），且归属说明行 `> — …` 仍然不会被吸收到正文中（保留了 lookahead）。
    - **端到端验证**：在一篇以 ja/ar 翻译的 69 KB 文章中，某条引文的第一段此前在日文中被译为 `> GLM-5.3がオープンウェイト化。`，在阿拉伯文中也同样遭到翻译；现在则会保留为 `> GLM-5.3 is now open-weight.`。英文引文行数从 9 恢复到 10，与源文一致。
    - 需要注意的是，下游 validator 未检测出这一缺陷，因为它们只检查引文是否存在，而不检查其是否完整。
  - **默认 provider 的实测成本节省**：只要模型名以 `gpt-5` 开头，`_openai_extra_kwargs` 就会发送 `reasoning_effort="medium"`，即使处于 `--eco` 也是如此。使用 `gpt-5.4-mini` 翻译一个十词句子的测量结果：`medium` → 45 个 reasoning token 和 65 个输出 token；`none` → 0 和 14。reasoning 对翻译没有任何帮助，却在每个文件的每个片段上产生费用。现在，`--eco` 中的默认值改为 `none`，其他情况下仍为 `medium`；通过 CLI 显式传入的值仍然优先。除了 `low`/`medium`/`high`，`--reasoning_effort` 现在还接受 `none` 和 `xhigh`（并非所有模型都接受全部取值：例如 `gpt-5.4-mini` 会拒绝 `minimal`——现有的不带参数重试机制可处理这种情况）。
  - **SDK 更新与 Gemini 迁移**：`google-generativeai`（支持已于 2025-11-30 结束，仓库已归档）被统一 SDK **`google-genai`** 取代——先执行 `genai.Client(api_key=...)`，再执行 `client.models.generate_content(model=, contents=, config=)`；system prompt 通过 `system_instruction` 传递，不再与片段拼接。`mistralai` 升级到 **2.9.4**（import 改为 `from mistralai.client import Mistral`；旧版会抛出 `ImportError`，已在 wheel 中验证），`anthropic` 升级到 **0.125.0**，`openai` 升级到 **2.54.0**——这些都是切换到 `httpx2` 之前的最新版本，以免 venv 中同时存在两套 HTTP stack。`httpx` 0.28.1 和 `pydantic` 2.13.5 也因此解除版本锁定。
  - **两项由真实测试而非文档发现的回归**：
    - `anthropic` ≥ 1.0 会在 client 端拒绝非 streaming 调用，只要其 `max_tokens` 预示请求可能持续超过 10 分钟（`ValueError: Streaming is required...`）。0.34.2 中不存在这项防护，它会导致使用 `max_tokens=32768` 的所有 Claude 调用失败。已通过显式设置 `timeout` 修复（`CLAUDE_TIMEOUT`，默认 900 秒），从而无需为了一个只使用完整响应的调用而切换到 streaming。
    - 只有部分 Gemini 模型接受 `thinking_level="minimal"`：`gemini-3.1-flash-lite` 支持它，而 `gemini-3.7-flash` 和 `gemini-3.1-pro-preview` 会以 400 拒绝。因此新增 `_gemini_generate_with_fallback`，按 `minimal` → `low` → 不使用 thinking_config 的顺序级联回退，其模式与已有的 OpenAI fallback 相同——优化参数绝不能导致翻译失败。
  - **默认模型已更新**，每个模型都通过真实调用验证：OpenAI `gpt-5.5` → **`gpt-5.6-terra`**（在一批 28 个项目中降低 60%）和 `gpt-5.4-mini` → **`gpt-5.6-luna`**（降低 73%）；Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**（更便宜且更新）和 `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（不含日期的规范 ID）；Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**，`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（稳定版本，且比 `3.5-flash-lite` 更便宜）。Mistral 保持不变，`mistral-large-latest` 仍是四者中性价比最高的模型。需要注意的是，没有比 `gemini-3.1-pro-preview` 更新的 Gemini Pro 系列模型——2026 年 5 月宣布的 Gemini 3.5 Pro 从未发布；3.5/3.6/3.7 产品线只有 Flash。
  - **切换 Gemini 前进行的实测 A/B**：使用 `gemini-3.1-pro-preview` 和 `gemini-3.7-flash`，通过 `README.md` 将内容翻译为日文。结构完全一致（21 个列表、18 个代码块、13 个 HTML 链接、13 张图片，所有 URL 均得到保留），耗时为 **8 秒对 48 秒**。由于没有任何公开 benchmark 比较这两个模型在翻译或非拉丁文字脚本方面的表现，否则此次切换只能建立在单纯的推测之上。
  - **Claude 响应块过滤**：`_call_claude` 直接执行 `block.text for block in response.content`，没有过滤类型。采用自适应 reasoning 的模型（Sonnet 5 及更高版本）会插入 `thinking` 块，其中提供的是 `.thinking`，而不是 `.text`——翻译会在第一个片段因不透明的 `AttributeError` 而失败。现在会排除 `thinking`、`redacted_thinking`、`tool_use` 和 `tool_result` 块（使用负面列表，以便继续容忍携带文本的未知类型），如果响应完全不含文本块，则会抛出明确错误。每次调用都会传入 `thinking={"type": "disabled"}`。
  - **`MODEL_TOKEN_LIMITS` 已重新同步**：删除退役日期已过的模型（`magistral-*` 系列于 2026-07-31 退役，`gemini-2.0-*` 于 2026-06-01 退役，`gemini-3-pro-preview` 于 2026-03-09 退役，以及 `claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。修正限制：Mistral 128K → **256K**（Large 3 / Small 4 代）、Gemini 1 000 000 → **1 048 576**（实际 input 限制）、`claude-opus-4-5` 200K → **1M**、`gpt-5.6-*` 系列 400K → **1.05M**。新增 Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest` 和 `ministral-*` 系列。需要注意的是，这些限制仍仅供参考，因为 `translate()` 会将分段上限设为 `min(16000, limite)`。
  - **Provider `--use_codex`**：第五个 provider，用于以非交互模式驱动官方 Codex CLI（`codex exec`），而不是调用按用量计费的 API。翻译消耗的是已付费 ChatGPT 订阅的配额。这是 OpenAI 针对此用途提供的唯一文档化途径：各套餐可用性矩阵将“Codex SDK、`codex exec` 和可编程工作流”列为 Plus/Pro/Business/Enterprise 可用功能，而 `~/.codex/auth.json` 的 token 无法验证对 API Platform 的调用（并且此脚本从不读取它们——身份验证及其刷新仍由 CLI 管理）。
  - **可通过 pip 安装 Codex 二进制文件，不再仅限 npm**：`_resolve_codex_binary()` 依次在 `CODEX_BIN`、`PATH`，然后在 OpenAI 发布的官方 Python 包 **`openai-codex-cli-bin`**（即 `openai-codex` SDK 的依赖项）中查找二进制文件。因此，Python 项目不再需要全局安装 npm 即可使用 `--use_codex`。该包未添加到 `requirements.txt`：二进制文件约为 250 MB，如果添加，所有用户都会被迫安装它，而它仅供可选 provider 使用。已完成端到端验证：当 `codex` 不在 `PATH` 中时，解析过程会找到打包的二进制文件，并在 6 秒内完成完整翻译。
  - **“订阅模式”保证**：从子进程环境中移除 `OPENAI_API_KEY` 和 `CODEX_API_KEY`。如果没有这项保护，`.env` 中存在的密钥可能会让 Codex 在没有任何可见提示的情况下切换为按用量计费——而这个 provider 正是为了避免这种情况。
  - **通过测试锁定 CLI 陷阱**：
    - 即使 prompt 作为参数传入，`codex exec` **仍会**读取 stdin：如果不关闭 stdin，命令会一直等待到超时，且永远不会调用模型（复现结果：180 秒后以 124 退出，输出为零字节）。因此必须使用 `communicate(input=...)`。
    - 通过 npm 安装的 `codex` 是一个 Node shim，它会通过 `spawn` 启动真正的 Rust 二进制文件：后者是 Python 进程的**孙进程**，会在对 `subprocess.run(timeout=)` 执行 `SIGKILL` 后继续存活，并继续消耗配额。因此需要 `Popen(start_new_session=True)` + `os.killpg`。
    - CLI 可能在已输出 `turn.failed` 的情况下仍以 0 退出：除返回码外，还会检查 JSONL 输出（`--json`）；如果返回码为 0 但缺少 `-o` 文件，则抛出明确错误，而不是生成空分段。
  - **rate limit 退避**：CLI 未实现任何内部 retry（`max_retries = 0`）。分类基于 JSON payload 的结构（`status: 429` / `error.type`），而不是子字符串——因为“quota”一词既可能出现在可恢复的 429 中，也可能出现在永久性的 `insufficient_quota` 中。
  - **CI 保护**：如果定义了 `CI` 或 `GITHUB_ACTIONS`，则拒绝 `--use_codex`。订阅身份验证并非为共享 runner 设计，OpenAI 也明确不建议在公共仓库中采用此工作流。
  - **模型**：`gpt-5.6-sol`（质量）和 `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` 系列由 CLI 和 API Platform 共用，但 ChatGPT 账户并不一定有权使用其中所有模型：allowlist 在服务器端应用，本地不进行验证，使用不常见的模型会触发警告。在 Plus 套餐中，Luna 每个 5 小时窗口可提供 250–2,000 条消息，而 Sol 为 10–100 条：`--eco` 是所有批处理任务的推荐模式。
  - **已修复 Bug——`regen_translations.sh` 在完全成功后仍以错误退出**：`trap ... EXIT` 引用了 `failed_log`，它是 `main()` 的一个 `local` 变量，但在 trap 执行时已不存在。在 `set -u` 下，这会引发 `failed_log: unbound variable`，导致脚本以 1 退出，尽管 28 项翻译全部正确——这会在重新生成后最耗费资源的阶段直接中断 `release.sh --auto`（`set -e`）。该变量现改为全局变量，trap 会检查它是否存在。一个有益的副作用是：此前被此错误掩盖的真实翻译失败，现在会重新显示在最终摘要中。
  - **`REGEN_MODEL`**：`regen_translations.sh` 的新环境变量，可强制指定模型并覆盖 provider 的默认值，例如使用 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`，以便通过订阅配额中的高端模型重新生成，而不是使用面向高吞吐量的 `--eco` 模型。
  - **`regen_translations.sh`**：`REGEN_PROVIDER=codex` 可通过显式 opt-in 启用（绝不自动检测，以免在用户不知情的情况下消耗订阅配额）。在开启并行处理前，会先按顺序刷新一次 token——因为 Codex refresh 是轮换且一次性的，并发 job 会使 `codex login` session 失效——并发数同时降至 4。
  - **相关重构**：`_dispatch_provider_call` 通过返回 provider 名称的 `_resolve_provider()`，将参数数量从 8 个减少到 6 个，不再在整个调用链中传递第四个布尔值。显式布尔值的优先级仍高于 `args`，以保留使用最小化 `Namespace` 调用 `translate(..., use_mistral=True)` 的测试。
  - **测试**：新增文件 `tests/test_codex_provider.py`（48 项测试），覆盖 argv、清理后的环境、禁止前言的契约、静默失败、timeout/killpg、退避、preflight、provider 解析、Gemini 推理级联、Claude 块过滤以及多段落 news 引用。完整测试套件共 290 项测试。
  - **实际验证**：通过 Codex 将项目的 `README.md` 翻译为**14 种语言**后，其结构与参考翻译严格一致（14 个代码块、24 个标题、25 行表格、13 个 HTML 链接、13 张图片、19 个 URL，代码块逐字符完全相同，placeholder 残留为零）。对于一篇 69 KB 的新闻文章，在 `--news` 模式下，`gpt-5.6-luna` 和 `gpt-5.6-sol` 的输出均通过 en/ja/ar 下游应用验证器。通过 `account/rateLimits/read` 测得的消耗仍低于计数器的舍入阈值（在 `--eco` 模式下占 5 小时窗口的 0%）。

- **1.9.2** 修复带嵌套括号或法语前缀的 news 归属 URL 提取问题（2026-05-11）：

  - **已修复 Bug**：`_protect_news_quotes` 中的归属 URL 提取使用正则表达式 `re.search(r"\((.+?)\)", attribution)`（对括号之间的内容进行惰性捕获）。对于 `(relayé par [@user sur X](https://x.com/.../123))` 形式的归属信息（嵌套括号：外层 `(` + Markdown 链接的 `]()`），捕获会在遇到第一个 `)` 时停止 → 得到被截断且包含法语前缀的字符串：`relayé par [@user sur X](https://x.com/.../123`（缺少末尾的 `)`）。结果是：`_validate_news_post` 会在翻译后的输出中查找该字符串并必然失败（原因有两个：`)` 被截断 + “relayé par”会被翻译成 `relayed by`/`weitergeleitet von`/……）。从 low → medium → high → gpt-5.5 的完整级联均无法通过。
  - **修复**：正则表达式改为 `re.search(r"\]\(([^)]+)\)", attribution)`——专门匹配 Markdown 链接中的 `](url)`，并且**仅捕获纯 URL**（不含法语前缀，也不截断），翻译过程中由 placeholder `#URL{N}#` 保持不变。可稳健处理以下两种问题模式：
    - `(relayé par [@account sur X](url))`——嵌套括号
    - `via [@source](url)` 或 `selon [@author](url)`——不带外层括号的法语前缀
  - **测试**：在 `test_silent_failure.py` 文件的 `TestNewsCitationExtraction` 类中新增 2 项测试：
    - `test_extract_attribution_url_with_nested_parens`（精确复现 Genspark CEO E2B Bug 的案例）
    - `test_extract_attribution_url_with_french_prefix`（包含 `via` 的变体）
  - **覆盖缺口**：`check-editorial-coverage.py` 会验证编辑语法，但不会验证 translator 是否能够处理该语法。一项可能的改进（不在 v1.9.2 范围内）是增加一项检查，通过 dry-run 模拟归属信息提取，从而在发布**之前**检测高风险模式。

- **1.9.1** 修复翻译 marker 说明中 CTA 标签的 i18n 问题（2026-05-10）：

  - **已修复 Bug**：在翻译文件顶部的 marker 横幅中，CTA 链接的 `[Voir le projet sur GitHub ↗]` 标签对所有目标语言都仍为**法语**，而不是随 `target_lang` 变化。LLM 永远看不到它（它由 Python 端组装，以保留仓库 URL 和 slug），因此翻译阶段无法补救。此静默回归自 v1.9 添加 `marker` 格式以来一直存在。
  - **修复**：新增常量 `_VIEW_PROJECT_LABELS`，将 15 种语言映射到各自的本地化标签。`_translation_note_invariants(target_lang)` 和 `_assemble_translation_note_paragraphs(phrase, target_lang)` 现在会传递目标语言。如果语言未知，则回退到 `fr`（确保安全，不会出现 KeyError）。
  - **测试**：调整 `test_source_emits_three_paragraphs_repo_title_description_link`（target_lang `ja` → 预期为日语标签）。新增 2 项测试：`test_source_link_label_localized_per_target_lang`（对涵盖拉丁文字、表意文字和辅音音素文字的 7 种语言进行参数化测试）以及 `test_source_link_label_falls_back_to_french_for_unknown_target`。总计：`test_translation_note_position.py` 中包含 40 项测试（此前为 38 项）。
  - **向后兼容**：签名包含默认值 `target_lang="fr"`——未提供 `args.target_lang` 的外部程序化调用方无需修改即可继续运行。
- **1.9** 修复静默失败 + 完整质量工具链 + 多位置翻译注释（2026-05-07）：
  - **多位置翻译注释 + “embed card”标记格式**：
    - 新增 CLI 选项（仅增量添加，默认行为不变 → **非破坏性变更**）：
      - `--note_position {top,bottom,both}`（默认：`bottom`）：将注释放置在已翻译文件的顶部、底部或同时放置在两处。
      - `--note_format {legacy,marker}`（默认：`legacy`）：
        - `legacy` 严格复现 v1.8 的行为（粗体段落 `**…**`），做到**逐字节一致**。
        - `marker` 输出一条不可见的 Markdown 链接引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），随后是一个结构化的 **3 段落 blockquote**，以实现类似“GitHub 仓库 embed card”的渲染效果：使用行内代码显示项目标题（`**\`ai-powered-markdown-translator\`\*\*`）、由 LLM 翻译的描述，以及带有可见箭头的 CTA 链接（`[Voir le projet sur GitHub ↗](URL)`）。构建时可由 remark 插件处理（参见 jls42.org 博客 → 插件 `remark-translation-banner`）。
    - **绝不发送给 LLM 的不变量**：仓库标题和 GitHub URL 在描述性句子翻译完成后由 Python 端组装。LLM 永远不会看到 slug `ai-powered-markdown-translator` 或 `https://github.com/jls42/...`，从而确保 renderer、大小写或 scheme 均不会被更改。
    - **感知 frontmatter 的插入机制**：在 `top` 或 `both` 模式下，注释会插入到 YAML frontmatter 的闭合 `---` 块**之后**（确保 Astro Content Collections / gray-matter 的安全性）。辅助函数 `_split_frontmatter` 会检测文件开头的 `---\n…\n---\n` 并保持其完整性；如果 frontmatter 已打开但没有闭合 fence，则会**抛出 `RuntimeError`**（文件会进入 `failed_files`，而不会写入位置错误的注释）。
    - **模型白名单 sanitizer**：`_sanitize_model` 将 `[A-Za-z0-9._:/-]` 之外的所有字符替换为 `_`，若结果为空则回退到 `unknown`。这与 Astro remark 插件端的验证器保持一致，并消除会破坏标记格式的字符（空格、引号、括号、逗号等）。
    - **内部重构**：`_append_translation_note`（1 个单体函数）→ 7 个纯辅助函数（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。builder 与 composer 分离（builder 返回不含分隔符的纯块，composer 根据位置应用 `\n\n`）；生产代码与源辅助函数共用同一个 3 段落组装器。
    - **保留空行的 `_quote_lines`**：为每一行添加 `> ` 前缀，并将空行转换为单独的 `>`。这使 mdast 能够在 blockquote 中识别出 3 个独立段落（标题 / 描述 / 链接），而不是一个仅含换行的段落。
    - **自适应 `_build_translation_note_block`**：根据 LLM 保留的段落数量处理（3 = 完整 card 格式，2 = 句子 + 链接，1 = 回退模式）。当检测到 Markdown 链接 `](` 时，单段落回退模式**不再使用 `**...**` 包裹内容**（在链接外使用 `<strong>` 的渲染不稳定）。
    - **向后兼容**：在 `_compose_with_notes` 端使用 `getattr(args, "note_position", "bottom")` 和 `getattr(args, "note_format", "legacy")`——缺少这些属性的 Namespace（现有测试、外部程序化调用）无需修改即可继续运行。
  - **修复长篇翻译的静默失败**：
    - 对所有 provider（OpenAI、Mistral、Claude、Gemini）执行翻译后语言验证：确定性层（逐字查找源文本片段）+ 概率性层（`langdetect`）
    - `finish_reason` / `stop_reason` 白名单：对于白名单之外的任何状态（truncation、content_filter 等）抛出 `RuntimeError`
    - Claude 的 `max_tokens`：`4096` → `32768`（避免 16k 分段出现隐性 truncation，为 FR→JA/ZH/KO/AR/HI 跨文字系统翻译预留空间）
    - 感知 heading 的分段：优先选择分段后半部分的 H2/H3（每个分段都从一个完整的语义章节开始）
    - 将错误传播至非零 exit code：`translate_markdown_file` 返回类型化状态 `success` / `failure` / `skipped`；只要至少一个文件失败，`main()` 就会 `sys.exit(1)`（单文件和 batch 均适用）
    - 所有 provider 均添加空内容保护、源文本/输出合理性比例检查（源文本 ≥ 500 个字符且输出不足 5% 时拒绝）、代码 placeholder 验证（`#CODEBLOCK`/`#INLINECODE`）、LLM 后规范化（修复与 heading 粘连的分隔符/链接），以及不使用 `reasoning_effort` 的 `BadRequestError` 重试
    - 新增依赖 `langdetect==1.0.9`
  - **pre-commit 质量工具链**（“完整 EurekAI 类型”，14 个 hook）：
    - Pre-commit：ruff（lint+format）、shellcheck、prettier（md/yaml/json）、detect-secrets（保护 4 个 API key）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（空白字符、EOF、大文件、shebang 等）
    - Pre-push：mypy（渐进式宽松模式）、Opengrep SAST（translate.py + scripts/）、pip-audit（初始报告模式）、unittest discover（tests/ + scripts/tests/）
    - `scripts/` 中使用 `./venv/bin/python` 的本地 wrapper
    - `scripts/audit_verdict.py`：pip-audit JSON parser，包含 11 个 unittest；由 jls42-astro 的 parser 改写而成的 Python 版本
    - 修复了 7 个初始 ruff 违规：B904（raise from）×2、B007（未使用的 dirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizard 暂时排除 `translate.py`（4 个函数的 CCN 为 21-47，已计划重构）——对 scripts/ 实施严格 gate
  - **SonarCloud + 全面覆盖率**：
    - GitHub Actions workflow `SonarCloud`（sonarcloud.yml + sonar-project.properties）：每次 push 和 pull-request 时执行分析，通过 `coverage.xml` 获取 coverage
    - README 顶部新增 11 个 SonarCloud badge（Quality Gate、Security/Reliability/Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）
    - `tests/test_silent_failure.py`（`unittest` 标准库）：覆盖静默失败错误链的六个环节
    - `tests/test_orchestration.py`（新增 79 个测试）：覆盖 `translate.py` 的 orchestration 层（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` TypeError + BadRequestError 回退、o1 系列 prompt 格式、`_validate_translation_output` 的 early-return 分支）
    - `scripts/tests/test_audit_verdict.py`：通过 subprocess 覆盖 `main()`（stdin/stdout）和 `if __name__ == "__main__"` 块
    - **新代码覆盖率**：75.5% → ~98%（translate.py 98%，scripts/audit_verdict.py 97%）
  - **测试**：`tests/test_translation_note_position.py` 覆盖位置 × 格式矩阵（包括 E2E `marker+top|bottom|both` 和 `legacy+top|bottom|both`）、多行前缀处理、逐字节向后兼容性（golden literal）、sanitizer、frontmatter 拆分（包括未闭合 fence 时抛出异常）、3 段落格式、2 段落回退、单段落 + Markdown 链接保护，以及关键防护测试 `TestLLMPayloadExcludesInvariants`，该测试断言标题和 URL 绝不会发送给 LLM。**190 个测试通过**，0 项回归。
  - 文档：`README.md`（法语 + 14 种翻译）含 badge、`CLAUDE.md`（pre-commit workflow + 详细 CI 监控），重新生成 28 种翻译
- **1.8** `--news` 模式 + 2026 模型升级（2026-03-17，tag `v1.8`）：
  - 更新默认模型（2026 年 3 月）：
    - OpenAI 高质量：`gpt-5` → `gpt-5.4`
    - OpenAI 经济型：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 高质量：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - 新增 `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）和 `gemini-3.1-pro-preview`（1M）的 token 限制
  - 初始 `--news` 模式：使用 placeholder `#NEWSQUOTE\d+#` 保护英文引用、`LANG_FLAGS` mapping（15 种语言）、按目标语言管理 flag
  - 恢复前验证 news placeholder（回归问题：LLM 删除 placeholder 时，会静默生成缺少引用的输出）
  - 使脚本 `regen_translations.sh` 可移植（绝对路径，不依赖 pwd）
  - 在 README/CHANGELOG 的语言栏中新增法语，并重新生成 28 种翻译
- **1.7** 新增功能：
  - 新增 `--keep_filename` 选项，在翻译时保留原始文件名
  - 支持通过 `.env` 文件自动加载 API key
  - **保留行内代码**：现在会在翻译期间保护反引号（`` `...` ``）
  - 改进 system prompt：
    - 更妥善地处理 YAML frontmatter 中的引号
    - 保护 template 变量 `{variable}`
    - 禁止添加未经请求的译者注释
  - 已在 364 个文件上成功测试（jls42.org 博客迁移）
- **1.6** 新增功能：
  - 支持使用 Google Gemini API 进行翻译（`--use_gemini`）
  - 更新 2026 年默认模型：
    - OpenAI：`gpt-5`（高质量）、`gpt-5-mini`（经济型）
    - Claude：`claude-sonnet-4-5`（高质量）、`claude-haiku-4-5`（经济型）
    - Gemini：`gemini-3-pro-preview`（高质量）、`gemini-3-flash-preview`（经济型）
  - 经济模式（`--eco`），用于采用速度更快、成本更低的模型
  - 翻译单个文件（`--file`），无需遍历目录
  - 新的简化命名 pattern：`{base}-{lang}.md`
  - 新增 `--include_model` 选项，以保留包含模型名称的旧格式
  - 支持未列出的模型，并使用默认 token 限制（128k）
  - README 已翻译为 14 种语言
- **1.5** 改进：
  - **更新 API key 和默认模型：**
    - **OpenAI：** 从 `DEFAULT_MODEL_OPENAI` 更新至 `"gpt-4o"`。
    - **Mistral AI：** 从 `DEFAULT_MODEL_MISTRAL` 更新至 `"mistral-large-latest"`。
    - **Anthropic Claude：** 新增 `DEFAULT_ANTHROPIC_API_KEY`，并将 `DEFAULT_MODEL_CLAUDE` 更新至 `"claude-3-5-sonnet-20240620"`。
  - **优化翻译 prompt：**
    - 丰富了直接翻译和翻译注释所使用的 prompt，以提高清晰度和效率，其中包括关于保留元数据及特定格式元素的详细指令。
  - **代码重构：**
    - 使用 `Mistral` 类替换 `MistralClient`，以初始化 Mistral AI client。
    - 重新组织 import，以提高可读性和可维护性。
    - 改进文本分段和代码块处理，以在翻译期间保留原始格式。
  - **输出文件管理：**
    - 交换输出文件名中的模型与语言顺序（例如 `f"{base}-{args.target_lang}-{args.model}.md"`），从而更便于组织和查找翻译。
  - **其他改进：**
    - 删除不必要的空行以清理代码。
    - 进行细微调整，以改善脚本结构和可读性。
- **1.4** 新增功能：
  - 支持使用 Anthropic Claude API 进行翻译
  - 优化 prompt，以提高清晰度和效率
  - 进行细微调整，以改善代码可维护性
- **1.3** 改进和新增功能：
  - 改进代码块处理
  - 改进输出文件管理
  - 改进现有文件检测
  - 新增 `--force` 选项，用于强制翻译
  - 交换输出文件名中的模型与语言顺序
- **1.2** 修复 changelog
- **1.1** 新增 Mistral AI API 支持
- **1.0** 初始版本——支持 OpenAI API

**使用 gpt-5.6-sol 将文章从法语翻译成中文。**
