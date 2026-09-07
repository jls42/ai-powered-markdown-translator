### 更新日志

🌍 [法语](CHANGELOG.md) | [英语](CHANGELOG-en.md) | [西班牙语](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [德语](CHANGELOG-de.md) | [日语](CHANGELOG-ja.md) | [韩语](CHANGELOG-ko.md) | [阿拉伯语](CHANGELOG-ar.md) | [印地语](CHANGELOG-hi.md) | [意大利语](CHANGELOG-it.md) | [荷兰语](CHANGELOG-nl.md) | [波兰语](CHANGELOG-pl.md) | [葡萄牙语](CHANGELOG-pt.md) | [罗马尼亚语](CHANGELOG-ro.md) | [瑞典语](CHANGELOG-sv.md)

- **1.13.0** Provider `--use_openrouter`：通往约 430 个模型的付费路由器，其中包括中国的开放模型（2026-09-05）：

  - **第九条 provider 路径，与第八条一同发布。** 1.12.0 未发布到 PyPI：OpenCode 和 OpenRouter 两个路由器将同时推出。[OpenRouter](https://openrouter.ai) 只需一个密钥，即可访问此处其他任何 provider 都未提供的模型——Kimi、Qwen、DeepSeek、Z.ai——统一使用按量计费的额度。由于 endpoint 与 OpenAI 兼容，因此使用与 xAI 相同的客户端；**这个 provider 的全部区别都集中在一次 preflight 中**，其每条规则均源自对 API 的实测。

  - **同一个模型由数十家具有不同上限的托管商提供，而路由对此一无所知。** 实测：`z-ai/glm-5.2` 有 33 家托管商，`z-ai/glm-5.3-flash` 有 23 家——其中一家将**输出限制为 2,048 tokens**。因此，一次长篇翻译在这 23 家之间随机路由时会遭到截断，却不会发出任何信号。preflight 读取 `/api/v1/models/{modèle}/endpoints`，排除输出不足 8,000 tokens、状态异常或未声明任何上限的托管商，然后锁定其余托管商。仅有 `provider.only` 而**没有** `allow_fallbacks: false` 只表示偏好：路由器仍会转向已排除的托管商，使锁定失去意义。如果没有任何托管商满足上限，命令就会停止：继续翻译等同于接受这项 preflight 本来要防止的静默截断。

  - **推理按输出费率计费，而且许多模型默认启用。** 在 `z-ai/glm-5.2` 上发送相同请求并得到“OK”响应：**采用模型默认设置时用了 107 个 completion tokens，关闭推理后仅用了 2 个**。推理对翻译毫无帮助，却会让每个文件的每个分段都产生 18 倍开销。因此默认将其关闭。**431 个模型中有 288 个**强制启用推理（`reasoning.mandatory`），它们会返回 `400 « Reasoning is mandatory for this endpoint and cannot be disabled »`：对于这些模型，不会发送任何参数，以免臆测 effort——effort 会分配 `max_tokens` 的一个**百分比**，并优先供推理消耗，因此随意选择一个值只会转移空白页面的风险，而不会降低风险。

  - **强制推理的模型会收到它所接受的最低 effort，这是由实测决定的。** 最初选择不发送任何参数，以免替模型作出臆测。在 `z-ai/glm-5.3-flash` 上验证后发现，其目录默认值为 `max`，这一选择会导致输出在翻译完成前**于 32,768 tokens 处截断**——十四种语言中有两种丢失。增大总额度也无济于事：effort 会从中分配一个百分比，而推理消耗也会随之增长。因此，provider 会在 preflight 中读取 `supported_efforts` 并请求最低值；如果目录未提供可用值，则退回到“不发送任何参数”。针对出错语言的反向验证表明：此前它会因预算耗尽而失败，如今可在 9 分钟内完成，且结构与源文件完全相同。

  - **上游托管商故障现在会明确指出责任方。** 路由器会将这种情况规范化为 `finish_reason=error`，并附带空的 `native_finish_reason`——已在两种语言上分别实测两次，每次都恰好发生于 750 秒。原先的通用消息会让人误以为文档或分段存在问题；现在它会说明故障位于供应商一侧，而且重试通常即可解决。

  - **`finish_reason=length` 且输出为空并不代表截断。** 这表示推理在产生第一个有效字符前就耗尽了预算——实测为 15,850 个推理 tokens，而有效内容仅有 148 个。两种情况需要采取完全相反的措施：对于前者，减小分段大小毫无作用。消息现在会明确区分两者。另外两项保护同样来自实测：上游托管商失败时，路由器会返回**状态码 200，但响应体中只有错误**（`choices[0]` 会抛出不透明的 `TypeError`，掩盖真正消息）；上下文窗口则从目录读取并写入 `MODEL_TOKEN_LIMITS`——目录中有 44 个模型的 `DEFAULT_TOKEN_LIMIT` 不正确，其中两个模型的上限仅为 4,095 tokens。

  - **`--model fournisseur/modèle` 为必填项，并且在进行任何网络访问前验证其格式。** OpenRouter 不是供应商：这一选择会影响价格、许可和数据处理方式，不能替用户作出。由于 slug 会插入 preflight URL，因此验证并非单纯的易用性措施，而是阻止路径注入的保护机制：两个路由器共用的带 namespace regex 接受 `a/b/..`，所以必须明确拒绝父目录分段。`--eco` 不起作用，并会明确说明这一点。

  - **修正了三处表述，其中一处原本是错误的。** OpenAI 关于 `codex exec` 的警告针对的是在共享 runner 上注入个人 session 文件，而不是仓库是否公开：README、CLAUDE.md 和代码此前都误解了这段引述。OpenCode 的认证位置在 1.18.27 中发生了变化（位于 `opencode.db` 的 `credential` 表中，而不再是 `auth.json`）；“此处绝不会读取它”这一不变量仍然成立，但地址已经过时。最后，OpenCode 章节不再把从未验证过的路径描述为等价方案：Zen 网关和 Ollama 已完成端到端实测，GitHub Copilot、LM Studio 和 llama.cpp 尚未实测，README 现在会如实说明。

  - **开展了一轮测量，并在 README 中加入推荐模型表格。** 针对三组文档执行了三百多次翻译，目标涵盖十四种语言：一篇采用 `--news` 模式、内容密集的博客文章；使用标准 Markdown 的本 README；以及四个直接取自 GitHub 的知名项目 README。表格区分了此前容易混淆的两个概念：翻译是否**成功完成**，以及翻译后的**结构是否与源文件完全相同**。有三个模型在两份密集文档中从未丢失任何信息：`gemini-3.7-flash`、通过 ChatGPT 订阅使用的 `gpt-5.6-sol`，以及通过 OpenRouter 使用的 `z-ai/glm-5.2`——它们唯一的偏差，是在一两种语言中漏掉了一对 `**`。核心结论是：**真正具有区分度的因素是文档密度，而不是 `--news` 模式**。通过订阅使用的 Grok 在博客文章上十四次中失败十三次，却在十六个公开 README 中成功十四次；反向验证确认，原因是长分段导致模型失去连贯性。表格也附带自身的警告：它并不全面，数据具有时效性，耗时不能用于排名，正确做法仍是在自己的文档上进行测量。

  - **结构比较器在发布数据前得到修正，因为它对非拉丁文字产生了两种误报。** 当 URL 后跟全角右括号 `）` 时，以 `)` 为终止位置的 regex 无法正确截断，导致提取出的字符串不同，尽管 URL 本身完全相同；一段法语中占五行、中文中仅占三行的引用也会使逐行计数下降。两项修正均通过反向验证：删除 URL、章节或 inline code 仍会被检测到。如果没有这些修正，Gemini 和 Codex 的结果会被公布为十四种语言中分别只有十一种和十二种通过，而非十三种和十二种。

  - **测试**：新增文件 `tests/test_openrouter_provider.py`（39 项测试）——模型验证与父目录分段拒绝、托管商锁定（上限、状态、未声明上限、共同最低值）、`allow_fallbacks` 始终为 false、根据 `mandatory` 关闭或保留推理、完整输出契约（状态码 200 中的错误、没有 choice、区分空白页面与截断、异常的 `finish_reason`、空内容）、目录无法访问时 preflight 采用 fail-closed、slug 缺失及没有健康托管商、flag 互斥性和文件名标签。完整测试套件现有 **427 项测试**。

  - **重构：将 4,253 行的单一模块拆分为多个模块，不改变任何一行业务行为。** `src/aipmt/translate.py` 被拆分到 `config`、`markdown`、`segmentation`、`guards`、`placeholders`、`news`、`prompts`、`notes`、`naming`、`pipeline`、`cli` 和子包 `providers/` 中（每个 provider 一个模块，以 `base` 为基础，`registry` 用于解析和 dispatch）。每次移动都是一个 commit，并提供机械式证明：验证器将包内所有顶层节点的 AST 与参考 snapshot 比较，检查每个符号的位置、安全标记是否逐字保留，以及是否不存在未跟踪文件——这套临时工具会在下一版本中移除。可见变化包括：`aipmt.translate` 变为 facade，以对象身份不变的方式重新导出原模块中不带 `_` 前缀的 64 个名称（其中 `__all__` 包含九个受支持的 API，其余为兼容性 alias），并停止重新导出由 `import *` 收集的 29 个依赖项和标准库名称；不再支持直接执行文件（`python src/aipmt/translate.py`）——`aipmt` 和 `python -m aipmt` 仍是两种受支持的形式；公共函数的 `__module__` 现在指向其定义模块；SDK 会在加载 `.env` 后导入，而非之前导入，目前未发现任何影响。427 项测试的标识符全部保留，并迁移到它们实际测试的模块：原先通过 facade 完成的 91 个 patch 现在指向读取相应名称的模块（经实测，其中九个即使缺少 patch 仍会通过）；七项契约测试用于锁定 facade；gate 工具也在首次移动前完成重写，确保它们不会因停止检查而错误变绿——Lizard scope 改为带下限的目录，flag 从已构建的 parser 中读取，覆盖率下限按包计算，`release.sh` 会枚举已跟踪模块。

- **1.12.0** Provider `--use_opencode`：通过开源 agent OpenCode 连接用户选择的供应商——本地模型、免账户免费模型、订阅或密钥（2026-09-04）：

  - **第八条 provider 路径，其性质与前七条不同。** [OpenCode](https://opencode.ai)（MIT）并非模型供应商，而是一个_路由器_，用于连接用户在 OpenCode 中自行配置的服务：API key、订阅（GitHub Copilot、ChatGPT、SuperGrok）、提供**无需账户**的免费模型的 OpenCode Zen 网关，或**本地**模型（Ollama、LM Studio、llama.cpp）。脚本像控制 Codex 和 Grok 一样，以非交互模式控制 `opencode run`，并复用相同的子进程基础设施（独立 process group，超时后依次发送 `SIGTERM` 和 `SIGKILL`，始终关闭 stdin，并清理环境变量）。已通过**两次真实翻译**验证：使用 `opencode/mimo-v2.5-free` 将整个 README 翻译成英语——耗时 49 秒，仅需一次处理，结构与源文件完全相同（32 个标题、26 个代码块结束标记、18 个链接、37 个 URL、37 行表格、135 处 inline code）；以及通过本地 `ollama/qwen2.5:7b` 翻译一个测试文件，全程无需任何密钥。

  - **`--model provider/modèle` 为必填项，而且这是一个必须明确作出的选择。** 如果没有 `--model`，OpenCode 会回退到自身的默认模型；在全新安装中，该模型为 `opencode/big-pickle`，这是一款免费的“stealth”模型，其交互内容可能用于训练——实测确认，作出响应的正是这个模型。替用户静默作出这种选择，恰恰是本仓库致力于追踪的隐式切换；因此，错误消息会指出用于列出模型的命令（`opencode models`），并给出三个示例（本地、免费、订阅）。`--eco` 不起作用，并会明确说明这一点。仅在用户明确请求时，`--reasoning_effort` 才会原样作为 OpenCode 的 `--variant` 传递。

  - **隔离经过实测，而非想当然。** inline 配置（`OPENCODE_CONFIG_CONTENT`，在 OpenCode 合并顺序中位于最后，因此优先于用户配置但不会替换它）定义了一个拒绝所有工具的 agent `aipmt`（`permission: {"*": "deny"}`）：注册表甚至不再向模型提供这些工具，因此即使要求它“列出文件并运行 `id`”，它也会回答自己没有工具。session 共享被禁用，外部插件被排除（`--pure`），绝不使用 `--auto`，工作目录为空且用后即弃。实测发现并阻止了两种静默注入：如果没有 `OPENCODE_DISABLE_CLAUDE_CODE`，用户的 `~/.claude/CLAUDE.md` 会进入**每一个** prompt（仅输入一句“你好”时，输入量会从 186 tokens 增至 515 tokens）；如果没有 `OPENCODE_DISABLE_PROJECT_CONFIG`，当前目录中的 `AGENTS.md` 也会被注入——其中一条“每个回答都以 BANANA 结尾”的指令确实影响了翻译。全局 `~/.config/opencode/AGENTS.md` 仍会被注入：目前没有任何开关可以排除它，而通过挪用 `XDG_CONFIG_HOME` 来绕过还会一并隐藏用户配置的供应商。因此选择如实记录，而非临时拼凑规避方案。

  - **`exit 0` 不能证明任何事情；这是第三个 CLI，仍需遵循相同的防范原则——同时还存在两个特有陷阱。** 未知的 `--agent` 不会使 `opencode run` 失败：它只会在 stderr 上发出警告，然后**静默**回退到启用了工具的 coding agent。如果 inline 配置未生效，翻译就会由能够写入文件的 agent 执行；因此，输出契约除检查以下条件外，还会验证不存在该消息：返回码为 0、没有 `error` 事件、没有 `tool_use`、最后一个 `step_finish` 位于 `stop` 中（`length` 表示响应被截断）、文本非空。第二个陷阱是，JSON 错误事件是**不透明的**——“发生意外服务器错误，请查看服务器日志了解详情。”，仅附带一个引用——真正原因（`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`、`ProviderAuthError` 等）只存在于日志中。因此需要使用 `--print-logs --log-level ERROR`，并读取 stderr 中的 `error="…"` 字段，同时排除紧随其后的 Bun trace。这样一来，未知模型会在一秒内失败，并明确指出原因。`--title` 还避免了一次多余的 LLM 调用：如果没有它，OpenCode 会通过在 `small_model` 上额外执行一轮来生成 session 标题。

  - **密钥：采用与 Codex 和 Grok 相同的模式过滤，但有一个明确列名的例外。** 保留 `OPENCODE_API_KEY`：这是 OpenCode 自身的密钥（用于 Zen 网关和 Go 订阅），按名称直接交给 OpenCode——相当于它的 `auth.json`，既不是 aipmt 管理的密钥，也不可能由 aipmt 计费。供应商在 OpenCode 中配置（`opencode auth login`、`opencode.json`），绝不会配置在 aipmt 的 `.env` 中，因此 aipmt 的任何密钥都不会进入子进程。与订阅型 CLI 不同，CI 中不作拒绝：在 runner 上使用 API key 或自托管模型都属于合法用途。

  - **防路径穿越保护现在检查插值后的值，而不是原始值。** `provider/modèle` 包含一个会被 1.10.0 保护机制拒绝的 `/`——这是合理的，因为 `--model` 会被插入文件名 `--include_model`。文件名标签现在会在任何插值发生前，将 `/`、`\` 和 `:` 替换为 `-`（`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`，因为 `:` 在 Windows 下非法），上游保护机制则检查这一标签：`../../evil` 在目标目录下会变成普通文件名 `doc-en-..-..-evil.md`，仅 `..` 仍会被拒绝，`--target_lang ../x` 也同样被拒绝。作用域保护 `_ensure_within_directory` 仍作为第二层防护，保持不变。
  - **免费模型和本地模型，以及实际测量结果。** `opencode/mimo-v2.5-free` 翻译一个段落需要 16 秒，翻译此 README 需要 49 秒；`opencode/big-pickle` 处理 200 个单词需要 40 秒，而且两个并发请求在 5 分钟内始终没有响应，而单独请求时都能完成；`opencode/nemotron-3.5-lightning-free` 在 3 分钟内没有任何响应。因此必须使用带 `REGEN_MODEL` 的 `REGEN_PROVIDER=opencode`，并行运行 **2 个任务**。本地方面，Ollama 通常将上下文配置为 4,096 tokens，而分段最长可达 16,000 个字符：因此必须使用带 `PARAMETER num_ctx 32768` 的 `Modelfile`，且质量取决于模型——在测试文件中，一个 7B 模型颠倒了列表并破坏了代码块的结束围栏，而网关模型完整保留了所有内容。

  - **此仓库的翻译今后绝不会再通过计费 API。** 只要 `.env` 中留有密钥，`regen_translations.sh` 就会使用 OpenAI API，而 Codex 仅作为显式启用选项。这正是准备此版本时发生的情况：28 份翻译先通过 OpenAI API 完成，随后印地语 CHANGELOG 又通过 Gemini API 完成，尽管 ChatGPT 订阅存在的目的正是避免按用量付费。密钥自动检测已被移除：**Codex 是默认选项，并使用 `gpt-5.6-sol`**，即质量模型；`openai`、`gemini` 和 `grok` 除 `REGEN_PROVIDER` 外还必须指定 `REGEN_ALLOW_PAID_API=1`，这是一项具名豁免，确保规则在做出选择时生效；未知的 `REGEN_PROVIDER` 会失败，而不会回退到 API。十项测试锁定了默认行为、拒绝机制和豁免机制。此版本的 28 份翻译均已通过 Codex 重新完成。

  - **rate limit 的 back-off 已提取为共享逻辑**（`_retry_on_rate_limit`）：Codex 和 Grok 的循环除了标签外完全相同，再复制第三份就会超过重复代码阈值。三个 CLI 错误均继承自同一个 `_CliCallError`；一项测试禁止其中任何一个脱离该继承关系，否则共享循环将无法再捕获它。

  - **测试**：新增文件 `tests/test_opencode_provider.py`（51 项测试）——完整输出契约、agent 回退、从日志读取原因、文本分片去重并忽略合成分片、timeout 终止进程组、429 back-off、模型必填且经过验证、无 secret 的 preflight、二进制文件解析、dispatch 接线、文件名标签以及路径遍历反证。`tests/test_review_hardening.py` 将 flags 互斥性和无 secret 要求扩展到新 provider。gate 现在要求记录 **22 个 flags** argparse。完整测试套件达到 **382 项测试**。

- **1.11.1** 文档修正：README 终于列出了全部七条 provider 路径（2026-09-03）：

  - **1.11.0 的 PyPI 页面写的是“4 个 API + Codex CLI”。** 代码实际提供七条路径——通过 API 使用 OpenAI、Mistral、Claude、Gemini 和 Grok；通过订阅使用 Codex（ChatGPT）和 Grok，无需按用量付费。简介和 _Multi-Provider_ 条目中遗漏了两种 Grok 模式，14 份翻译也重复了这一错误。由于软件包的长描述在每个版本中都是固定的，修正展示页面必须发布新版本号：这就是此版本存在的唯一原因。**没有代码变更。**
  - `CLAUDE.md` 已与发布时引入的内容对齐：gate 计数器（16，`--full` 中为 17）、十一个活跃 workflow、`gh pr checks` 中不可见的两个 Sonar/Codacy 计数器（hotspots、Codacy API）、通过 `ruff-format` 移动一个 `# nosemgrep`、OIDC 交换所要求的 GitHub 环境，以及 _pending publisher_ 不会预留名称这一事实。

- **1.11.0** 发布到 PyPI：先执行 `pip install ai-powered-markdown-translator`，再执行命令 `aipmt`，无需克隆仓库（2026-09-03）：

  - **单文件脚本变为可安装软件包。** `translate.py` 从根目录移动到 `src/aipmt/translate.py`，并提供控制台入口点 `aipmt` 及其等价形式 `python -m aipmt`。参与贡献仍需克隆仓库——测试、28 份翻译和质量工具都位于其中——但使用工具不再需要。

    - **导入名称是 `aipmt`，绝不能是 `translate`**，因为冲突真实存在且不会发出提示。PyPI 软件包 `translate`（v3.8.1，最近一次上传于 2026-07-06）会安装一个同名目录。已在 venv 中复现：该目录优先于模块，`translate.main` 消失，入口点在 `AttributeError` 处中断——而 `pip check` 返回“No broken requirements found”，rc=0。用户只需执行一次 `pip install translate`，就足以在没有可用诊断信息的情况下破坏 CLI。使用真实 wheel 进行反证：在该软件包之上安装 `pip install translate`，安装前后 `aipmt --help` 均为 rc=0，两个 CLI 可以共存。
    - **发行名称长，命令短。** `ai-powered-markdown-translator` 使软件包能通过 PyPI 搜索找到；对于尚不了解该项目的人来说，单独的缩写无法被发现，而此次发布的目的恰恰是让项目可被找到。经核查排除了两个看似合理的候选名称：`ai-markdown-translator` 自 2024 年起已在 npm 上被一个用途相同的工具占用，比此仓库早 17 个月；`aimt` 与 `aim`（v3.29.1）仅差一个字母，后者是同一领域的活跃软件包——这是最容易造成长期混淆的情况。这里还有一个方法上的陷阱：`pypi.org/project/<nom>/` 对任何名称都返回 200（反机器人页面），只有 JSON API 的结果可信。
    - **采用 `src/` layout，而非扁平软件包。** 扁平软件包本可保留测试中的六个 `sys.path.insert(..., "..")`，但这恰恰是问题所在：它们会导入源码树而不是已安装软件包，从而掩盖所有打包错误。实际代价只是一条额外的替换规则。

  - **密钥终于可以一次配置、长期使用。** 已安装的 CLI 此前没有任何持久配置：只能使用环境变量和当前目录中的 `.env`。`find_dotenv` 的确会一直向上查找到系统根目录，因此在个人目录下工作时能够找到 `~/.env`，但在其他位置工作时便找不到——这种覆盖取决于从哪里启动命令，而非设计选择。因此新增第三层：`~/.config/aipmt/.env`，优先级低于现有两层。

    - **优先级并非硬编码**，而是源自 `override=False`，即 `load_dotenv` 的默认值：每一层只填补上一层留下的空值。因此顺序为环境变量 → 项目的 `.env` → 用户配置，并通过行为测试而非结构测试验证——交换两个调用的顺序会使测试失败，移除第三层同样如此。
    - **采用 `.env` 格式而非 TOML**，这是有意为之：`python-dotenv` 已经是依赖项，该语法已经在 15 份 README 中记录，而且同一文件可用于两个作用域。不引入任何新依赖或新语法。在非 Windows 系统中，如果 `XDG_CONFIG_HOME` 是**绝对路径**，则配置位置遵循该变量——规范要求忽略相对值，否则配置位置将再次取决于当前目录——而 Windows 下则遵循 `APPDATA`。
    - **排除了两个选项，并说明了原因。** 系统密钥环（`keyring`）在桌面设备上更安全，但在 headless 环境——服务器、容器、CI——中会失败，而这些恰恰是批量翻译的典型使用场景；它适合作为显式启用选项，却不适合作为默认值。`--api-key` flag 会让密钥进入 shell 历史记录，并使其在 `ps` 中可见。
    - **没有密钥时，不再显示调用栈。** 用户此前会看到指向 `site-packages` 的 Python 调用栈，以及一条只提到“环境变量或 .env”、却不说明应在何处创建后者的消息。现在消息会列出三个位置及其准确路径，并让命令以状态码 2 退出。这个保护网被**刻意限定得很窄**：仅在配置阶段对 `except ValueError` 进行处理。包裹整个执行过程会把翻译期间出现的真实 bug 转化为令人安心的消息——而这正是此仓库要追踪的失效模式。一项测试会读取 `main()` 的源代码以禁止这种做法。

  - **修正——工具安装后，用户的 `.env` 会被忽略。** 不带参数的 `load_dotenv()` 不会从当前目录向上查找，而是从调用方文件，即 `site-packages` 开始查找。已使用真实控制台入口点进行测量：从拥有自身 `.env` 的项目中启动时，`find_dotenv()` 返回 `''`，密钥不会被加载，而 `find_dotenv(usecwd=True)` 能找到它。只要工具仅从克隆的仓库中运行，这个 bug 就不存在；发布后它会成为系统性问题，唯一症状是在配置正确的情况下仍提示 API 密钥“缺失”。

  - **三个 gate 即使已经完全停止检查，也会显示为绿色。** 它们被刻意安排在迁移之前加固：在某项变更之后才编写用于捕获该变更问题的保护措施，无法证明任何事情。每个 gate 在原始仓库中均为绿色，在迁移后的副本上则转为红色——两个方向都经过测量。

    - **Lizard 会悄无声息地忽略不存在的路径**：rc=0，“0 file analyzed”。复杂度 gate 将从 158 个函数 / 2247 nloc 降至 3 个函数 / 34 nloc，输出文件大小为零字节。现在 scope 是一个数组，其中每个条目都会检查是否存在。
    - **对不存在的模块运行 `coverage run --source=` 不会失败**：只有 stderr 警告，无论 unittest 还是 `coverage xml` 都返回 rc=0，并且仍会发布报告——statements 从 1453 被削减到 141。项目看起来会很健康，仅仅因为几乎没有被分析。现在通过两个下限保护报告：总量，以及测得的最大文件。
    - **翻译新鲜度探针在结构上无法识别调用形式**：它锚定 argparse flags，而文件重命名不会改变这些 flags。复现结果：模块已移动，15 份 README 仍记录着不存在的命令，判定却是“没有过期翻译”。因此新增第 7 个部分，用于检查调用形式而非选项；同时将 Lizard hook 与脚本的真实 scope 进行比对——当其键 `files:` 不再匹配时，pre-commit 不会失败，而是直接跳过它。
 
  - **`requires-python = ">=3.10"` 不再只是一项未经验证的声明。** `sonar-project.properties` 已经宣称支持 3.10-3.12，但此前从未实际运行过这些版本，开发机器上只有 3.12——这是一个会被发布公之于众的内部矛盾。现在有一个测试 workflow 会在 3.10、3.11 和 3.12 上运行测试套件，并安装软件包，从而同时验证其公开版本边界。

  - **设置下限，不设上限。** `requirements.txt` 继续作为经过测试的 lock，`[project.dependencies]` 则成为公开契约：若将 lock 中的确切版本直接发布，会与所有还安装了其他软件包的用户环境发生冲突。也不设置 `<N+1` 上限——否则会与 `check-deps-fresh.sh` 直接矛盾，后者会在任何 major 版本滞后时让 release gate 失败。这组下限能够正确解析，而反证 `openai==1.0.0` 会输出 `ResolutionImpossible`，证明检查具有判别能力，并非无条件接受所有结果。此外，还有一项保护措施禁止 `pyproject.toml` 的版本与 CHANGELOG 中的版本不一致：PyPI 不允许重复使用版本号。

  - **已在全新 venv 中完成端到端验证**：约 70 Ko 的 wheel 仅包含 `aipmt/*.py`、dist-info 和许可证；`aipmt --help` 返回 rc=0，并显示 22 个 flags；`python -m aipmt` 显示“usage: aipmt”而非“usage: \_\_main\_\_.py”；`pipx` 安装可正常使用；最重要的是，**从任意用户目录实际完成了一次 fr→en 翻译**，粗体、列表、inline code、链接和 URL 均被保留，代码块未被翻译。迁移前的 318 项测试全部通过，且迁移前后的标识符列表逐字节完全相同——证明没有测试被禁用的是这一点，而非“OK”；另新增 12 项测试覆盖三层配置，总计 330 项。

- **1.10.0** `--use_codex` Provider（ChatGPT 订阅配额）、SDK 和模型更新、修正多段落 news 引用（2026-08-29）：

  - **安全审查——PR 设置了两项保护措施，却未能在所有位置落实**：

    - **Codex preflight 将整个 `.env` 传给了二进制文件。** `_codex_preflight` 调用 `subprocess.run` 时**没有指定 `env=`**：子进程继承了完整的 `os.environ`，因此也继承了由 `load_dotenv` 加载的整个 `.env`。通过带检测功能的伪二进制文件测得：**七个 secret** 进入了 preflight——六个 provider 的密钥，外加一个 `GITHUB_TOKEN`——相比之下，其对应的 `_grok_preflight` 为**零个**，因为后者正确传入了 `env=_grok_env()`。这是 PR 内部的不一致：几行之外的 `_strip_secret_env` 正是为了维持这一 invariant 而存在。现在已提取一个 `_codex_env_base()`，供两条路径共享；修正后的测量结果：两侧均为 0 个 secret。
    - **“`--deny` fail-closed”这一属性未覆盖实际采用的形式。** 注释将整个 Grok 隔离机制建立在这样一个事实之上：带有未知前缀的规则会导致启动被拒绝。对 `grok 1.0.13` 的测量表明，这种验证**仅适用于带括号的形式**：`--deny 'CeciNestPasUnOutil(*)'` 会拒绝启动（“unknown tool prefix”），而 `--deny 'CeciNestPasUnOutil'` 会被静默接受。然而 `GROK_DENY_RULES` 使用的全是裸名称——因此，如果 xAI 一侧重命名工具，在 OS sandbox 已经不适用的机器上，唯一经过验证的隔离层就会毫无提示地被移除。八条具名规则已改为 `Prefix(*)`，CLI 会验证每一条都是已知前缀；catch-all `*` 仍保留唯一可接受的字面形式。一项测试会阻止退回未经验证的形式。
    - **其余方面已验证无问题**：不存在命令注入（始终使用列表形式，从不使用 `shell=True`，文档内容通过 stdin 或 `--prompt-file` 传入），不存在不安全的反序列化（仅使用 `json.loads`，并有类型保护），七个 payload 均未发现路径遍历修正的绕过方式，且 `--deny '*'` 确实由 CLI 应用（在读取 workdir 之外的内容时观察到 `DENY_ENFORCED`）。
    - 此外，前文新增的新鲜度检查违背了自身原则：当某个软件包的 PyPI 请求失败时，它会被静默跳过，而 gate 仍为绿色。现在它会统计实际完成比较的软件包数量，并在覆盖不完整时失败。

  - **依赖项已更新，并新增两道保护网以防再次滞后**：
    - **版本滞后确实存在且长期持续**：`openai` 2.54 → **3.6.0**，`anthropic` 0.125 → **1.2.0**，`certifi` 2024.8.30 → **2026.7.22**——用于验证所有 provider 调用之 TLS 的根证书存储落后了两年。已确定原因：**不存在 `.github/dependabot.yml`**。没有此文件，GitHub 只会启用 _安全更新_，而 Dependabot 仅会为受到 CVE 影响的依赖项提交 PR——这解释了为何它升级了 `urllib3` 和 `idna`，却放任两个 SDK 落后一个主版本。
    - **两个主版本可以共存且互不冲突**，这与此前的推断相反：`openai` 3.x 和 `anthropic` 1.x 会迁移至 **`httpx2`**，而 `mistralai` 和 `google-genai` 仍使用 `httpx<1`，但它们是两个不同的发行包。先通过实际安装验证，随后对 **7 条 provider 路径进行了端到端测试**——OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI 和 Grok CLI——每份输出中的内联代码和链接均得到保留。“避免两套 HTTP 栈”只是一项偏好，并非阻碍：实测结果已经给出定论。
    - **`requirements.txt` 并未描述真实环境**：`google-auth`、`cryptography` 和 `opentelemetry` 栈已安装在工作 venv 中，却从未声明——因此全新安装无法复现被测试的环境。相反，`tokenizers`、`huggingface-hub` 和 `PyYAML` 虽列于其中，却未被导入，也不为任何组件所需，它们是 `mistralai` 1.x 的遗留项。该文件现已重新生成，完整锁定仅由直接依赖项构建的 venv。`pip-audit` 未在新依赖集中发现任何已知漏洞。
    - **`.github/dependabot.yml`**（新增）启用每周版本更新，覆盖 pip 和 github-actions。次版本与补丁版本合并到一个 PR 中——每个补丁升级都单独提交 PR，最终只会被忽略，而噪声是更新的敌人；**主版本分别提交**，每个都必须通过真实调用进行验证。
    - **`scripts/check-deps-fresh.sh`**（新增，已接入 gate）使版本滞后直接体现在项目判定结果中：Dependabot 只负责提出更新，无法提供保证，其 PR 也可能不断堆积。主版本滞后 → 失败；次版本滞后 → 警告，因为长期保持红色的 gate 最终会被忽略；PyPI 无法访问 → 本地明确跳过，**CI 中则采用失败关闭策略**，未执行的检查不能视为成功。已从正反两方面验证：它能准确捕获修复前的状态（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`），而对次版本滞后仅发出警告。

  - **本次 PR 审查产生的修复**——五个审查 agent 对 diff 进行了彻底检查；下列问题在修复前均已通过实测复现，其中两个是同一版本前文引入的回归。

    - **已修复回归——`_NEWS_CITATION_REGEX` 曾存在指数级回溯。** 多段落修复在重复结构中引入了 `(?:[ \t]*$|[ \t]+.*)`：`[ \t]+` 与 `.*` 对空格的划分存在歧义，并且这种歧义会随着迭代不断倍增。使用无法匹配该模式的 `>   texte` 行进行测量——这是完全合法的 Markdown 缩进：**14 行耗时 2,589 毫秒**，修复后仅需 0.04 毫秒，每增加一行，耗时约扩大 9 倍。在 `--news` 模式下，一段很长且不符合格式的 blockquote 足以让翻译冻结，直至作业超时，而且无法识别原因。现在，重复结构会一次性完整消费整行（`\n^>(?![ \t]*—).*`），使每次迭代只有一种匹配方式。已在包含 231 篇文章的真实语料库上验证：捕获结果**零差异**，仍为 423 处引用，14 个多段落正文仍能正常扩展。
    - **同时指定两个 provider flag 会在无提示的情况下产生按量计费。** `--use_codex --use_mistral` 会被接受；`_select_provider_client` 优先测试 Mistral，而 `_resolve_provider` 优先采用显式布尔值——两者最终都会选择 Mistral。因此，用户请求使用订阅额度，却在没有任何警告的情况下遭到按量计费：这正是 `--use_codex` 要防止的故障模式。六个 provider flag 现在统一通过 `add_mutually_exclusive_group` 处理。**行为变更**：此前会被静默接受的同时指定两个 provider 的命令行，现在会在 `argument --use_mistral: not allowed with argument --use_codex` 上失败。
    - **工作结束 gate 会在探针崩溃时错误显示为通过。** `scripts/check-release-ready.sh` 的十三项检查中，有四项遵循“捕获 stdout，若为空则作出结论”的模式，却从不检查返回码：异常（文件改名、`FileNotFoundError`）会写入 stderr，使 stdout 保持为空，而检查则得出“没有问题”的结论。用于防止“一个 `exit 0` 什么也证明不了”这一陷阱的脚本，内部却重现了同一个陷阱。现在，辅助函数 `probe()` 会同时要求返回码为零**并且**存在结束哨兵；探针也拒绝基于空的标记集合得出结论——因为对空集合的断言永远为真。实例证明：新增上述互斥组后，provider flag 改由 `*_group` 对象处理，旧正则表达式 `parser\.add_argument\(` 不再能够匹配；**二十一个 flag 中有六个**悄然脱离检查范围，而 gate 仍显示为通过。
    - **secret 扫描漏掉了六个 provider 中的四个。** 字符类 `[A-Za-z0-9]` 不包含连字符：`sk-proj-…`（OpenAI 当前格式）和 `sk-ant-api03-…` 会在第二个连字符处中断，而 `AIza…` 完全不在覆盖范围内。模式现已扩展，并将 `.secrets.baseline` 排除在扫描之外。此外，保护检查 `.env` 查询的是 `git diff --cached`，它只能看到暂存区：一个**已经提交**的 `.env`——最糟糕的情况——永远不会出现在其中。现在改为查询 `git ls-files`。
    - **Codex 的“token 预热”并不是真正的预热。** 实测显示：`codex login status` 不会触碰 `~/.codex/auth.json`（mtime 和大小均未变化），其帮助文本写的是“显示登录状态”。然而，注释却声称它会“按顺序执行一次”token 刷新，从而消除一次性轮换 token 被并发刷新的风险。所宣称的保护实际上并不存在；现在，注释已准确描述代码的实际行为，真正的应对措施仍是 `max_jobs=4`。此外，该检查现已遵循此前被忽略的 `CODEX_BIN`——在 `PATH` 中没有 `codex` 的工作站上，过去会报“未认证”，这一诊断具有误导性。
    - **`.env` 曾在子 shell 中被加载。** `detect_provider` 通过命令替换调用，因此其 export 无法传回父 shell：在 `.env` 中定义的 `GROK_BIN`、`GROK_HOME` 或 `REGEN_MODEL` 对 `main()` 中执行的读取仍不可见，导致配置正确时也会得出“找不到 Grok 二进制文件”的结论。
    - **并发量比声明的上限高出 50%。** 限制检查位于启动 README/CHANGELOG 任务对之后：实测 `max_jobs=2` 的峰值为 **3**。对于 Grok，其每周配额与 Chat/Imagine/Voice 共享且无法测量，因此脚本并未遵守其自行设定的上限。此外，最终计数虽然会显示，却从未与 28 比较——缺少文件也不会被发现。
    - **Grok 输出契约：缺少 `stopReason` 现在会导致失败。** 在已声明的契约要求 `end_turn` 的位置，代码实际采用的是“`end_turn` **或不存在**”。不包含该字段的 payload——或 CLI 更新后字段被重命名——会使保护检查悄然变成 no-op。此外，`max_turn_requests` 不再归类为 rate limit（这是轮次预算已耗尽：重试只会在付出 90 秒等待后得到相同结果），`quota` 也已从 rate limit 标记中移除——原因正如 `_codex_is_rate_limited` 的 docstring 早已说明的那样，只是 Grok 此前并未遵循。
    - **Gemini 级联现在按模型进行记忆化。** 它此前会在每个 segment 上重新从 `minimal` 开始，尽管默认模型会拒绝该请求：常规路径会为每个 segment 多付出一次 400 往返，并重复打印同一条警告。一条重复数百次的 warning 最终不会再有人阅读——它也就这样变成了遮蔽物。
    - **其他修复**：CI 中的拒绝消息曾为 Codex 硬编码，导致 `--use_grok_cli` 用户被引导至 `OPENAI_API_KEY`，而不是 `XAI_API_KEY`；`provider.capitalize()` 显示为“Grok_cli”和“Openai”；子进程基础设施的注释曾将“shim”泛化至两个 CLI，但 Grok 二进制文件是原生 ELF（正确理由是“会生成自身子进程的 agent”）；`subprocess` 上的十二项 SAST finding 已标记为 `# nosec` / `# nosemgrep` 并附有理由，因为不含 `shell=True` 的列表形式使注入无法发生，而且文档内容从不经由 argv 传递。
    - **任何 secret 都不再进入 agent 子进程。** 按名称列举的 deny-list 只保护了**计费**不变量（Codex 不含 `OPENAI_API_KEY`，Grok 不含 `XAI_API_KEY`）。实测显示：**另外七个 secret** 仍会进入每个子进程——Anthropic、Mistral、Google 和 Gemini 的密钥、另一个 CLI 的密钥，以及 `OPENAI_BASE_URL`；后者不是 secret，但会改变流量路由。然而，这两个 CLI 都是 **agent**，并且 Grok agent 在许多 Linux 工作站上运行时无法应用 OS sandbox。现在改为**按名称模式**过滤（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`），而非按名称列表过滤，因此也能覆盖用户在 `.env` 中自行添加、此代码并不知晓的变量。CLI 不需要其中任何一个：认证信息存放在 `~/.codex` 和 `~/.grok` 中，从不位于环境变量内——已分别通过两个 provider 在强化后的环境中**成功完成真实翻译**予以验证。
    - **测试**：新增文件 `tests/test_review_hardening.py`（21 项测试），用于锁定 provider flag 的互斥性、`stopReason` 契约、news 正则表达式的线性复杂度、CI 中的拒绝消息、Gemini 记忆化，以及子进程环境中不存在任何 secret。最后一项断言是**通用的**——即使密钥未出现在任何列表中，它也会失败——而现有的清除测试只是其常量的镜像，除了自身循环失效外，无法检测任何其他问题。完整测试套件现有 **311 项测试**。
  - **两个新的 Grok provider**：`--use_grok`（xAI API，密钥为 `XAI_API_KEY`，按使用量计费）和 `--use_grok_cli`（官方 Grok Build CLI，从 Grok 订阅额度中扣除——原理与 `--use_codex` 相同）。
    - **API 模式，约 40 行代码**：由于 xAI endpoint 与 OpenAI 兼容，client 和 `_call_openai` 均可原样复用，只有 `base_url` 发生变化。仅需进行一项适配，且所有 provider 都能从中受益：`finish_reason` 现在也接受 `end_turn`，这是 xAI 输出的形式，而 OpenAI 输出的是 `stop`。模型：`grok-4.6`（高质量）和 `grok-4.3`（经济型）。需要注意的是，Grok 的经济型模型仍是仓库中最贵的——每百万 token 为 $1.25/$2.50，而 `mistral-small-latest` 为 $0.15/$0.60：选择这个 provider 是为了模型多样性，而非价格。
    - **CLI 模式**：以 Codex 为蓝本，但受实际条件限制存在四处差异——prompt 通过文件传入（`--prompt-file`，CLI 不读取 stdin，而 argv 中的 segment 会在 `ps` 中可见）；输出是 stdout 上的单个 JSON object（既不是 JSONL，也不是 `-o` 文件）；订阅仅提供 `grok-4.6` 和 `grok-4.5`；sandbox 无法应用（见下文）。子进程启动逻辑与 Codex 一同抽取至 `_codex_run_process`，未改动已经过测试的 Codex provider 其余部分。
    - **`exit 0` 什么也证明不了，已有实测**：未认证时，CLI 会将 `{"type":"error","message":"Not signed in."}` 写入 **stdout**，且返回码为 **0**。请求被拒绝或超出轮次时也具有相同行为。因此，输出契约要求同时满足四个条件：返回码为 0、不含 error payload、`stopReason == end_turn`，以及文本非空。preflight 遵循相同逻辑：即使未登录，`grok models` 也以 0 退出，只有 stdout 中出现“not authenticated”才能据此判定。
    - **隔离：有意采用且已记录的不对称设计。** Codex 在 `--sandbox read-only` 中运行，而 Grok 的 sandbox 在许多较新的 Linux 设备上无法应用，原因是两个相互独立的系统问题，若无 `sudo` 均无法绕过：从 Ubuntu 24.04 开始，AppArmor 会阻止非特权 user namespace（`bwrap: setting up uid map: Permission denied`，已在 Grok 外复现）；当 `/run/podman` 处于 `0700` 状态时，container runtime socket 的 deny-list 会失败（resolver 仅能捕获 `ErrorKind::NotFound`，EACCES 会成为致命错误）。核心陷阱在于：无法应用的**内置**配置会在无任何提示的情况下以非隔离方式启动。因此，脚本默认不请求任何配置，也绝不会静默回退——它会在 stderr 上发出警告。防护依赖 CLI 的 `--deny` 规则，其中包括 catch-all `*`；这是唯一经实测为 _fail-closed_ 的层级（使用未知前缀的规则会导致启动被拒绝）。可通过 `GROK_TRANSLATE_SANDBOX=read-only` 强制要求启用该层级，此时若设备无法满足要求，启动便会失败。
    - **防护措施**：从子进程环境中移除 `XAI_API_KEY`、`GROK_API_KEY` 和 `GROK_SANDBOX`（密钥会切换为按使用量计费；继承的 `GROK_SANDBOX` 会强制使用无法应用的配置，并给出误导性消息），禁用 MCP/hooks/skills/agents 开关，设置 `--disable-web-search`、`--no-subagents`、`--no-plan`，使用一次性 workdir，在 CI 中拒绝运行，timeout 时终止整个 process group，并在触发 rate limit 时执行 back-off。`--max-turns` 被设为 6 而非 1：计数器会在 tool round 后递增，设为 1 会截断输出。
    - **额度**：Grok 的额度池按周计算，并且**与 Chat、Imagine 和 Voice 共享**，也没有任何命令可显示该额度——Codex 则可通过 `account/rateLimits/read` 量化消耗。因此，`regen_translations.sh` 将并发数限制为 2，并明确发出警告。
    - **测试**：新增文件 `tests/test_grok_provider.py`（24 项测试）。完整测试套件现有 **290 项测试**。
  - **已修复的 bug——英文多段落引用仅得到部分保护（`--news` 模式）**：`_NEWS_CITATION_REGEX` 只接受一连串**连续的** `>` 行作为引用正文。一旦引用跨越多个段落（段落间由一行空的 `>` 分隔），便只有最后一个段落会被捕获并替换为 placeholder；前面的段落会被发送给 LLM，并以翻译后的形式返回——这与 `--news` 要保证的行为完全相反。现在，重复匹配会接受内部空白的 `>` 行，并改为非贪婪模式，从而在斜体行之前的空 `>` 处停止，而不是遇到第一个空行就停止。
    - **实测影响范围**：在包含 198 篇文章的真实 corpus 中，共有 419 处引用，其中 11 处受影响。没有任何回归——新 regex 捕获的引用数量完全相同，仅多段落正文的范围有所扩展（408 个正文保持一致，11 个得到扩展），且 attribution 行 `> — …` 仍不可能被并入正文（保留了 lookahead）。
    - **端到端证明**：对一篇 69 KB 的文章进行日语和阿拉伯语翻译时，某处引用的第一段此前在日语中被输出为 `> GLM-5.3がオープンウェイト化。`，在阿拉伯语中也同样被翻译；现在则会保持为 `> GLM-5.3 is now open-weight.`。英文引用行数从 9 恢复为 10，与源文一致。
    - 需要注意的是，下游 validator 未能发现这一缺陷，因为它们只检查引用是否存在，而不检查引用是否完整。
  - **默认 provider 的实测成本节省**：只要模型名称以 `gpt-5` 开头，`_openai_extra_kwargs` 就会发送 `reasoning_effort="medium"`，包括在 `--eco` 中也是如此。使用 `gpt-5.4-mini` 翻译一个十词句子的实测结果：`medium` → 45 个 reasoning token 和 65 个输出 token；`none` → 0 个和 14 个。reasoning 对翻译毫无帮助，却在每个文件的每个 segment 上产生费用。现在，`--eco` 中的默认值改为 `none`，其他情况下仍为 `medium`；通过 CLI 显式传入的值仍具有更高优先级。除 `low`/`medium`/`high` 外，`--reasoning_effort` 现在还接受 `none` 和 `xhigh`（并非所有模型都接受全部取值：例如 `gpt-5.4-mini` 会拒绝 `minimal`——现有的无参数 retry 会处理这种情况）。
  - **SDK 更新与 Gemini 迁移**：`google-generativeai`（支持已于 2025-11-30 结束，仓库也已归档）被统一 SDK **`google-genai`** 取代——先调用 `genai.Client(api_key=...)`，再调用 `client.models.generate_content(model=, contents=, config=)`；system prompt 通过 `system_instruction` 传递，不再与 segment 拼接。`mistralai` 升级至 **2.9.4**（import 改为 `from mistralai.client import Mistral`；旧方式会引发 `ImportError`，已在 wheel 中验证），`anthropic` 升级至 **0.125.0**，`openai` 升级至 **2.54.0**——这些都是切换到 `httpx2` 前的最后版本，以避免 venv 中并存两套 HTTP stack。因此，`httpx` 0.28.1 和 `pydantic` 2.13.5 也已解除锁定。
  - **两个由真实测试而非文档发现的回归**：
    - `anthropic` ≥ 1.0 会在 client 侧拒绝非 streaming 调用，只要其 `max_tokens` 预示执行时间将超过 10 分钟（`ValueError: Streaming is required...`）。该防护在 0.34.2 中不存在，会导致使用 `max_tokens=32768` 的所有 Claude 调用失败。现已通过显式设置 `timeout`（`CLAUDE_TIMEOUT`，默认 900 秒）修复，从而无需为了只使用完整 response 的调用而切换到 streaming。
    - 仅部分 Gemini 模型接受 `thinking_level="minimal"`：`gemini-3.1-flash-lite` 支持它，而 `gemini-3.7-flash` 和 `gemini-3.1-pro-preview` 会以 400 拒绝。因此加入 `_gemini_generate_with_fallback`，采用 `minimal` → `low` → 不使用 thinking_config 的逐级 fallback，仿照现有的 OpenAI fallback——优化参数绝不能导致翻译失败。
  - **更新默认模型**，每个模型均已通过真实调用验证：OpenAI `gpt-5.5` → **`gpt-5.6-terra`**（在一批 28 个任务中成本降低 60%），`gpt-5.4-mini` → **`gpt-5.6-luna`**（降低 73%）；Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**（更便宜且更新），`claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（不含日期的规范 ID）；Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**，`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（稳定版本，且比 `3.5-flash-lite` 更便宜）。Mistral 保持不变，`mistral-large-latest` 仍是四者中性价比最高的模型。需要注意的是，不存在比 `gemini-3.1-pro-preview` 更新的 Gemini Pro 系列模型——Gemini 3.5 Pro 于 2026 年 5 月公布，但从未发布；3.5/3.6/3.7 系列全部为 Flash。
  - **切换 Gemini 前进行的实测 A/B 对比**：使用 `gemini-3.1-pro-preview` 和 `gemini-3.7-flash` 将 `README.md` 翻译为日语。结构完全一致（21 个列表、18 个代码块、13 个 HTML link、13 张 image，所有 URL 均得到保留），耗时分别为 **8 秒和 48 秒**。由于没有任何公开 benchmark 对比这两个模型在翻译或非拉丁文字方面的表现，否则此次切换只能依据简单推测。
  - **Claude response block 过滤**：`_call_claude` 原先直接执行 `block.text for block in response.content`，而不筛选类型。采用 adaptive reasoning 的模型（Sonnet 5 及更高版本）会插入 `thinking` block，该 block 提供 `.thinking` 而非 `.text`——翻译会在第一个 segment 遭遇不透明的 `AttributeError` 时失败。现在会排除 `thinking`、`redacted_thinking`、`tool_use` 和 `tool_result` block（使用 deny-list，以继续兼容携带文本的未知类型），且当 response 不包含任何 text block 时会引发明确错误。每次调用都会传入 `thinking={"type": "disabled"}`。
  - **`MODEL_TOKEN_LIMITS` 已重新同步**：移除退役日期已过的模型（`magistral-*` 系列于 2026-07-31 退役，`gemini-2.0-*` 于 2026-06-01 退役，`gemini-3-pro-preview` 于 2026-03-09 退役，以及 `claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。修正限制：Mistral 128K → **256K**（Large 3 / Small 4 代），Gemini 1 000 000 → **1 048 576**（实际 input limit），`claude-opus-4-5` 200K → **1M**，`gpt-5.6-*` 系列 400K → **1.05M**。新增 Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest` 和 `ministral-*` 系列。需要注意的是，这些限制仍仅供参考，因为 `translate()` 会将 segmentation 上限设为 `min(16000, limite)`。
  - **Provider `--use_codex`**：第五个 provider，用于以非交互模式驱动官方 Codex CLI（`codex exec`），而非调用按用量计费的 API。翻译用量从已付费的 ChatGPT 订阅配额中扣除。这是 OpenAI 针对此用途提供的唯一有文档说明的途径：各套餐可用性矩阵将“Codex SDK、`codex exec` 和可脚本化工作流”列为 Plus/Pro/Business/Enterprise 可用功能，而 `~/.codex/auth.json` 的 token 无法用于验证 API Platform 调用（且此脚本从不读取它们——身份验证及其刷新仍由 CLI 管理）。
  - **Codex 二进制文件现可通过 pip 安装，不再仅限 npm**：`_resolve_codex_binary()` 依次在 `CODEX_BIN`、`PATH`，然后在 OpenAI 发布的官方 Python package **`openai-codex-cli-bin`** 中查找二进制文件（它是 SDK `openai-codex` 的依赖项）。因此，Python 项目无需全局安装 npm 即可使用 `--use_codex`。该 package 未添加到 `requirements.txt`：二进制文件约为 250 MB，若添加则所有用户都必须承受这一开销，而它仅用于可选 provider。已完成端到端验证：当 `codex` 不在 `PATH` 中时，解析过程会找到打包的二进制文件，并在 6 秒内完成完整翻译。
  - **“订阅模式”保证**：从子进程环境中移除 `OPENAI_API_KEY` 和 `CODEX_API_KEY`。若无此保护，`.env` 中存在的 key 可能会在没有任何明显提示的情况下使 Codex 切换到按用量计费——而此 provider 的存在正是为了避免这种情况。
  - **通过测试锁定 CLI 陷阱**：
    - 即使 prompt 已作为参数传入，`codex exec` **仍会**读取 stdin：若不关闭 stdin，命令会一直等待到超时，且从不调用模型（复现结果：180 秒后以 exit 124 退出，零字节）。因此必须使用 `communicate(input=...)`。
    - 通过 npm 安装的 `codex` 是一个 Node shim，它通过 `spawn` 启动真正的 Rust 二进制文件：该文件是 Python process 的**孙进程**，会在 `subprocess.run(timeout=)` 执行 `SIGKILL` 后继续存活并消耗配额。因此需要 `Popen(start_new_session=True)` + `os.killpg`。
    - CLI 可能以 0 退出，同时却已发出 `turn.failed`：除返回码外，还会检查 JSONL 输出（`--json`）；若返回码为 0 但缺少 `-o` 文件，则会抛出明确错误，而不是生成空 segment。
  - **rate limit 的 back-off**：CLI 未实现任何内部 retry（`max_retries = 0`）。分类依据 JSON payload 的结构（`status: 429` / `error.type`），而非子字符串——“quota”一词既可能出现在可恢复的 429 中，也可能出现在永久性的 `insufficient_quota` 中。
  - **CI 保护**：如果定义了 `CI` 或 `GITHUB_ACTIONS`，则拒绝 `--use_codex`。订阅身份验证并非为共享 runner 设计，OpenAI 也明确不建议在公共 repository 中使用此工作流。
  - **模型**：`gpt-5.6-sol`（质量）和 `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` 系列由 CLI 和 API Platform 共用，但 ChatGPT 账户并非有权使用其中所有模型：allowlist 在服务器端应用，不进行本地验证，使用非常规模型会触发警告。在 Plus 套餐中，每个 5 小时窗口内，Luna 可提供 250–2,000 条消息，而 Sol 仅为 10–100 条：`--eco` 是所有批处理任务的推荐模式。
  - **已修复的 bug——`regen_translations.sh` 在完全成功后仍以错误退出**：`trap ... EXIT` 引用了 `failed_log`，这是 `main()` 中的 `local` 变量，在 trap 执行时已不存在。在 `set -u` 下，这会引发 `failed_log: unbound variable`，导致脚本以 1 退出，即使全部 28 个翻译都正确——这会使 `release.sh --auto`（`set -e`）在重新生成后、也就是成本最高的阶段立即中断。该变量现已改为全局变量，trap 会检查它是否存在。一个有益的副作用是：此前被此错误掩盖的真正翻译失败，现在会重新显示在最终汇总中。
  - **`REGEN_MODEL`**：`regen_translations.sh` 的新环境变量，可强制使用指定模型并覆盖 provider 的默认值；例如使用 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`，即可通过订阅配额中的高端模型重新生成，而不是使用偏重处理量的 `--eco` 模型。
  - **`regen_translations.sh`**：`REGEN_PROVIDER=codex` 可通过显式 opt-in 启用（绝不会自动检测，以免在用户不知情的情况下消耗订阅配额）。在开启并行处理前，会先按顺序刷新一次 token——由于 Codex refresh 采用轮换机制且只能使用一次，并发 job 会使 `codex login` session 失效——并将并发数降至 4。
  - **相关重构**：`_dispatch_provider_call` 通过返回 provider 名称的 `_resolve_provider()`，将参数数量从 8 个减至 6 个，不再在整个调用链中传递第四个 boolean。显式 boolean 的优先级仍高于 `args`，以保留那些使用最简 `Namespace` 调用 `translate(..., use_mistral=True)` 的测试。
  - **测试**：新增文件 `tests/test_codex_provider.py`（48 个测试），覆盖 argv、清理后的环境、禁止前言的约定、静默失败、timeout/killpg、back-off、preflight、provider 解析、Gemini 推理级联、Claude block 过滤以及多段落新闻引用。完整测试套件共 290 个测试。
  - **实际验证**：项目的 `README.md` 通过 Codex 翻译成全部 **14 种语言**后，其结构与参考翻译严格一致（14 个代码块、24 个标题、25 行表格、13 个 HTML 链接、13 张图片、19 个 URL；代码块逐字符一致，placeholder 零残留）。对于一篇 69 KB 的新闻文章，在 `--news` 模式下，`gpt-5.6-luna` 和 `gpt-5.6-sol` 的输出均通过了 en/ja/ar 下游应用验证器。通过 `account/rateLimits/read` 测得的消耗量：在 `--eco` 模式下始终低于计数器的舍入阈值（5 小时窗口的 0%）。

- **1.9.2** 修复带嵌套括号或 FR 前缀的新闻归属 URL 提取问题（2026-05-11）：

  - **已修复的 bug**：`_protect_news_quotes` 中的归属 URL 提取使用正则表达式 `re.search(r"\((.+?)\)", attribution)`（括号之间的 lazy capture）。对于 `(relayé par [@user sur X](https://x.com/.../123))` 形式的归属信息（嵌套括号：外层 `(` + Markdown link 的 `]()`），捕获会在遇到第一个 `)` 时停止，从而得到截断且包含 FR 前缀的字符串：`relayé par [@user sur X](https://x.com/.../123`（缺少末尾的 `)`）。后果是：`_validate_news_post` 会在翻译后的输出中查找此字符串，并且总是失败（有两个原因：`)` 被截断，且“relayé par”会被翻译为 `relayed by`/`weitergeleitet von`/……）。完整的 low → medium → high → gpt-5.5 级联均无法通过。
  - **修复**：正则表达式改为 `re.search(r"\]\(([^)]+)\)", attribution)`——专门匹配 Markdown link 的 `](url)`，且**仅捕获纯 URL**（不含 FR 前缀，也不会截断）；翻译过程中由 placeholder `#URL{N}#` 保持其不变。该修复可稳健处理两种问题模式：
    - `(relayé par [@account sur X](url))`——嵌套括号
    - `via [@source](url)` 或 `selon [@author](url)`——无外层括号的 FR 前缀
  - **测试**：在 `test_silent_failure.py` 的 `TestNewsCitationExtraction` class 中新增 2 个测试：
    - `test_extract_attribution_url_with_nested_parens`（精确复现 Genspark CEO E2B bug 的案例）
    - `test_extract_attribution_url_with_french_prefix`（使用 `via` 的变体）
  - **覆盖缺口**：`check-editorial-coverage.py` 会验证编辑语法，但不会验证 translator 是否能够处理。一个可能的改进（不在 v1.9.2 的 scope 内）是添加检查，通过 dry-run 模拟归属信息提取，在发布**之前**检测高风险模式。

- **1.9.1** 修复翻译标记说明中 CTA label 的 i18n 问题（2026-05-10）：

  - **已修复的 bug**：翻译文件顶部 marker 横幅中的 CTA 链接 label `[Voir le projet sur GitHub ↗]` 对所有目标语言都仍为**法语**，而没有遵循 `target_lang`。LLM 从未看到该内容（它由 Python 端组装，以保留 repository 的 URL 和 slug），因此翻译阶段无法补救。自 v1.9 添加 `marker` 格式以来，这一直是一个静默 regression。
  - **修复**：新增常量 `_VIEW_PROJECT_LABELS`，将 15 种语言映射到各自的本地化 label。`_translation_note_invariants(target_lang)` 和 `_assemble_translation_note_paragraphs(phrase, target_lang)` 现在会传递目标语言。若语言未知，则 fallback 到 `fr`（确保安全，避免 KeyError）。
  - **测试**：调整 `test_source_emits_three_paragraphs_repo_title_description_link`（target_lang `ja` → 预期为日语 label）。新增 2 个测试：`test_source_link_label_localized_per_target_lang`（对覆盖 Latin、表意文字和 abjad script 的 7 种语言进行参数化测试）和 `test_source_link_label_falls_back_to_french_for_unknown_target`。`test_translation_note_position.py` 中共计 40 个测试（原为 38 个）。
  - **向后兼容性**：使用默认值 `target_lang="fr"` 的 signature——未传入 `args.target_lang` 的外部程序调用方无需修改即可继续工作。
- **1.9** 修复静默失败 + 完整质量工具链 + 多位置翻译说明（2026-05-07）：
  - **多位置翻译说明 + “embed card”标记格式**：
    - 新增 CLI 选项（仅作增量添加，默认行为不变 → **非破坏性变更**）：
      - `--note_position {top,bottom,both}`（默认：`bottom`）：将说明放置在译文文件顶部、底部或同时放在两处。
      - `--note_format {legacy,marker}`（默认：`legacy`）：
        - `legacy` 严格复现 v1.8 的行为（粗体段落 `**…**`），实现**逐字节一致**。
        - `marker` 输出一条不可见的 Markdown 链接引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），随后是一个结构化的**三段式 blockquote**，以呈现类似“GitHub 仓库嵌入卡片”的效果：使用行内代码显示项目标题（`**\`ai-powered-markdown-translator\`\*\*`）、由 LLM 翻译的描述，以及带有可见箭头的 CTA 链接（`[Voir le projet sur GitHub ↗](URL)`）。构建时可由 remark 插件处理（参见 jls42.org 博客 → 插件 `remark-translation-banner`）。
    - **绝不发送给 LLM 的不变量**：仓库标题和 GitHub URL 在描述语句翻译完成后由 Python 端组装。LLM 永远不会看到 slug `ai-powered-markdown-translator` 或 `https://github.com/jls42/...`，从而保证 renderer、大小写和 scheme 均不会被修改。
    - **感知 frontmatter 的插入方式**：在 `top` 或 `both` 模式下，说明会插入到 YAML frontmatter 的闭合 `---` 块**之后**（保障 Astro Content Collections / gray-matter 的安全性）。辅助函数 `_split_frontmatter` 会检测文件开头的 `---\n…\n---\n` 并保持其完整性；若 frontmatter 已开启但缺少闭合 fence，则会**抛出 `RuntimeError`**（该文件会被记录到 `failed_files`，而不会在说明位置错误的情况下写入）。
    - **模型白名单 sanitizer**：`_sanitize_model` 将 `[A-Za-z0-9._:/-]` 之外的所有字符替换为 `_`；若结果为空，则回退到 `unknown`。此规则与 Astro remark 插件端的验证器保持一致，并会清除可能破坏标记格式的字符（空格、引号、括号、逗号等）。
    - **内部重构**：`_append_translation_note`（一个单体函数）→ 7 个纯辅助函数（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。builder 与 composer 已分离（builder 返回不含分隔符的纯块，composer 根据位置应用 `\n\n`）；生产代码与源辅助函数共用同一个三段式组装器。
    - **`_quote_lines` 保留空行**：为每行添加 `> ` 前缀，并将空行转换为单独的 `>`。这样 mdast 会将 blockquote 识别为三个独立段落（标题／描述／链接），而不是带有换行符的单个段落。
    - **自适应 `_build_translation_note_block`**：根据 LLM 保留的段落数量进行处理（3 = 完整卡片格式，2 = 语句 + 链接，1 = 回退格式）。当检测到 Markdown 链接 `](` 时，单段落回退格式**不再使用 `**...**` 包裹**（使用 `<strong>` 包裹链接时渲染不稳定）。
    - **向后兼容**：`_compose_with_notes` 端的 `getattr(args, "note_position", "bottom")` 和 `getattr(args, "note_format", "legacy")`——不含这些属性的 Namespace（现有测试、外部程序化调用）无需修改即可继续运行。
  - **修复长文本翻译的静默失败**：
    - 在所有 provider（OpenAI、Mistral、Claude、Gemini）上执行译后语言验证：确定性层（在输出中发现原文逐字片段）+ 概率层（`langdetect`）
    - `finish_reason` / `stop_reason` 白名单：遇到白名单之外的任何状态（truncation、content_filter 等）均抛出 `RuntimeError`
    - Claude 的 `max_tokens`：`4096` → `32768`（避免 16k 分段发生隐性截断，并为 FR→JA/ZH/KO/AR/HI 跨文字系统转换预留余量）
    - 感知 heading 的分段：优先选择分段后半部分的 H2/H3（使每个分段都从完整的语义章节开始）
    - 错误一直传播至非零退出码：`translate_markdown_file` 返回类型化状态 `success` / `failure` / `skipped`；如果至少一个文件失败，`main()` 会执行 `sys.exit(1)`（单文件与批处理均适用）
    - 所有 provider 均增加空内容防护、源文本／输出文本合理比例检查（≥ 500 个字符且低于 5% 时拒绝）、代码占位符验证（`#CODEBLOCK`/`#INLINECODE`）、LLM 后规范化（修复与 heading 粘连的分隔符／链接），以及不使用 `reasoning_effort` 的 `BadRequestError` 重试
    - 新增依赖 `langdetect==1.0.9`
  - **pre-commit 质量工具链**（“完整 EurekAI 类型”，14 个 hook）：
    - Pre-commit：ruff（lint + format）、shellcheck、prettier（md/yaml/json）、detect-secrets（保护 4 个 API key）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（whitespace、EOF、large-files、shebangs 等）
    - Pre-push：mypy（渐进式宽松模式）、Opengrep SAST（translate.py + scripts/）、pip-audit（初始 reporting 模式）、unittest discover（tests/ + scripts/tests/）
    - `scripts/` 中使用 `./venv/bin/python` 的本地 wrapper
    - `scripts/audit_verdict.py`：pip-audit JSON parser，包含 11 个 unittest；由 jls42-astro 的 parser 移植并适配 Python
    - 修复了最初的 7 个 ruff 违规项：B904（raise from）×2、B007（未使用的 dirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizard 暂时排除 `translate.py`（4 个函数的 CCN 为 21–47，已计划重构）——对 scripts/ 实施严格 gate
  - **SonarCloud + 全面覆盖率**：
    - GitHub Actions workflow `SonarCloud`（sonarcloud.yml + sonar-project.properties）：每次 push 和 pull-request 时进行分析，并通过 `coverage.xml` 收集 coverage
    - README 顶部新增 11 个 SonarCloud badge（Quality Gate、Security/Reliability/Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）
    - `tests/test_silent_failure.py`（`unittest` 标准库）：覆盖静默失败错误链中的六个环节
    - `tests/test_orchestration.py`（新增 79 个测试）：覆盖 `translate.py` 的 orchestration 层（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` TypeError + BadRequestError 回退、o1 系列 prompt 格式、`_validate_translation_output` 的 early-return 分支）
    - `scripts/tests/test_audit_verdict.py`：通过 subprocess 覆盖 `main()`（stdin/stdout）和 `if __name__ == "__main__"` 块
    - **新代码覆盖率**：75.5% → 约 98%（translate.py 为 98%，scripts/audit_verdict.py 为 97%）
  - **测试**：`tests/test_translation_note_position.py` 覆盖位置 × 格式矩阵（包括 E2E `marker+top|bottom|both` 和 `legacy+top|bottom|both`）、多行前缀处理、逐字节向后兼容性（golden literal）、sanitizer、frontmatter 拆分（包括 fence 未闭合时抛出异常）、三段式格式、双段落回退格式、单段落 + Markdown 链接防护，以及一个关键保护测试 `TestLLMPayloadExcludesInvariants`，用于断言标题和 URL 绝不会发送给 LLM。**190 个测试通过**，无回归。
  - 文档：`README.md`（法语 + 14 种译文），包含 badge；`CLAUDE.md`（pre-commit workflow + 详细 CI 监控）；重新生成 28 份译文
- **1.8** `--news` 模式 + 2026 年模型升级（2026-03-17，tag `v1.8`）：
  - 更新默认模型（2026 年 3 月）：
    - OpenAI 高质量模式：`gpt-5` → `gpt-5.4`
    - OpenAI 经济模式：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 高质量模式：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - 新增 `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）和 `gemini-3.1-pro-preview`（1M）的 token 限制
  - 初始 `--news` 模式：使用占位符 `#NEWSQUOTE\d+#` 保护英文引文、`LANG_FLAGS` 映射（15 种语言），并根据目标语言管理标记
  - 在恢复 news 占位符前进行验证（回归问题：LLM 删除占位符时，会静默生成缺少引文的输出）
  - 将 `regen_translations.sh` 脚本改为可移植形式（使用绝对路径，不依赖 pwd）
  - 在 README/CHANGELOG 的语言栏中添加法语链接，重新生成 28 份译文
- **1.7** 新功能：
  - 新增 `--keep_filename` 选项，用于在翻译时保留原始文件名
  - 支持通过 `.env` 文件自动加载 API key
  - **保留行内代码**：翻译期间现会保护反引号（`` `...` ``）
  - 改进 system prompt：
    - 更妥善地处理 YAML frontmatter 中的引号
    - 保护 template 变量 `{variable}`
    - 禁止添加未经请求的译者说明
  - 已成功在 364 个文件上完成测试（jls42.org 博客迁移）
- **1.6** 新功能：
  - 支持使用 Google Gemini API 进行翻译（`--use_gemini`）
  - 更新 2026 年默认模型：
    - OpenAI：`gpt-5`（高质量）、`gpt-5-mini`（经济）
    - Claude：`claude-sonnet-4-5`（高质量）、`claude-haiku-4-5`（经济）
    - Gemini：`gemini-3-pro-preview`（高质量）、`gemini-3-flash-preview`（经济）
  - 经济模式（`--eco`），用于采用速度更快、成本更低的模型
  - 单文件翻译（`--file`），无需遍历目录
  - 新的简化命名模式：`{base}-{lang}.md`
  - 新增 `--include_model` 选项，用于保留包含模型名称的旧格式
  - 支持未列出的模型，并使用默认 token 限制（128k）
  - README 已翻译为 14 种语言
- **1.5** 改进：
  - **更新 API key 和默认模型：**
    - **OpenAI：**从 `DEFAULT_MODEL_OPENAI` 更新至 `"gpt-4o"`。
    - **Mistral AI：**从 `DEFAULT_MODEL_MISTRAL` 更新至 `"mistral-large-latest"`。
    - **Anthropic Claude：**新增 `DEFAULT_ANTHROPIC_API_KEY`，并从 `DEFAULT_MODEL_CLAUDE` 更新至 `"claude-3-5-sonnet-20240620"`。
  - **优化翻译 prompt：**
    - 丰富了直接翻译和翻译说明所用的 prompt，以提升清晰度和效率，其中包括有关保留元数据及特定格式元素的详细指令。
  - **代码重构：**
    - 使用 `Mistral` 类替换 `MistralClient`，用于初始化 Mistral AI client。
    - 重新组织 import，以提升可读性和可维护性。
    - 改进文本分段和代码块处理，以便在翻译期间保留原始格式。
  - **输出文件管理：**
    - 调换输出文件名中模型与语言的顺序（例如 `f"{base}-{args.target_lang}-{args.model}.md"`），从而更便于组织和查找译文。
  - **其他改进：**
    - 清理代码，移除不必要的空行。
    - 进行细微调整，以改善脚本的结构和可读性。
- **1.4** 新功能：
  - 支持使用 Anthropic Claude API 进行翻译
  - 优化 prompt，以提升清晰度和效率
  - 进行细微调整，以提升代码的可维护性
- **1.3** 改进与新功能：
  - 改进代码块处理
  - 改进输出文件管理
  - 改进现有文件检测
  - 新增 `--force` 选项，用于强制翻译
  - 调换输出文件名中模型与语言的顺序
- **1.2** 修复 changelog
- **1.1** 新增 Mistral AI API 支持
- **1.0** 初始版本——支持 OpenAI API

**使用 gpt-5.6-sol 将文章从法语翻译成中文。**
