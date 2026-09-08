### 更新日志

🌍 [法语](CHANGELOG.md) | [英语](CHANGELOG-en.md) | [西班牙语](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [德语](CHANGELOG-de.md) | [日语](CHANGELOG-ja.md) | [韩语](CHANGELOG-ko.md) | [阿拉伯语](CHANGELOG-ar.md) | [印地语](CHANGELOG-hi.md) | [意大利语](CHANGELOG-it.md) | [荷兰语](CHANGELOG-nl.md) | [波兰语](CHANGELOG-pl.md) | [葡萄牙语](CHANGELOG-pt.md) | [罗马尼亚语](CHANGELOG-ro.md) | [瑞典语](CHANGELOG-sv.md)

- **1.13.0** Provider `--use_openrouter`：一个付费路由器，可连接约 430 个模型，包括中国的开放模型（2026-09-05）：

  - **第九条 provider 路径，与第八条一同发布。** 1.12.0 未发布到 PyPI：OpenCode 和 OpenRouter 两个路由器同步推出。[OpenRouter](https://openrouter.ai) 只需一个密钥，即可使用其他 provider 在此均未提供的模型——Kimi、Qwen、DeepSeek、Z.ai——统一使用按量计费的余额。由于 endpoint 与 OpenAI 兼容，所用客户端与 xAI 相同；**这个 provider 的所有特殊之处都集中在一次预检中**，而其中每条规则都源自对 API 的实际测量。

  - **同一模型由数十家上游托管商提供，各自的上限不同，而路由对此并不知情。** 实测：`z-ai/glm-5.2` 有 33 家托管商，`z-ai/glm-5.3-flash` 有 23 家——其中一家将**输出限制为 2,048 tokens**。因此，在 23 家托管商之间随机路由时，长篇翻译会被截断，却不会发出任何信号。预检读取 `/api/v1/models/{modèle}/endpoints`，排除输出上限低于 8,000 tokens、状态异常或未声明任何上限的托管商，然后固定使用其余托管商。只有 `provider.only` 而**没有** `allow_fallbacks: false` 仅代表一种偏好：路由器仍会转回已被排除的托管商，使固定选择失去意义。如果没有任何托管商满足上限要求，命令将停止：仍然继续翻译，就等于接受这项预检本应阻止的静默截断。

  - **推理按输出费率计费，并且许多模型默认启用。** 对 `z-ai/glm-5.2` 发送同一请求并得到“确定”这一响应：**使用模型默认设置时产生 107 个 completion tokens，关闭推理后仅为 2 个**。翻译并不会从推理中获益，但每个文件的每个分段都会因此产生 18 倍开销。因此，默认关闭推理。**431 个模型中有 288 个**强制启用推理（`reasoning.mandatory`），它们会返回 `400 « Reasoning is mandatory for this endpoint and cannot be disabled »`：对于这些模型，预检会读取其接受的 effort，并请求最低级别（见下一项）——effort 会分配 **`max_tokens` 的一定比例**，并由推理优先消耗，因此随意选择一个值只会转移空白输出的风险，而不会降低它。

  - **强制推理的模型会收到其接受的最低 effort，这是由实测决定的。** 最初的选择是什么都不发送，以免替模型擅自决定。在 `z-ai/glm-5.3-flash` 上进行验证时，该模型在目录中的默认值为 `max`，这种做法会导致输出在翻译完成前**于 32,768 tokens 处被截断**——十四种语言中有两种丢失。扩大额度也无济于事：effort 会从中分配一定比例，推理也会随额度一同增长。因此，provider 在预检时读取 `supported_efforts` 并请求最低级别；若目录未公布任何可用级别，则回退为“无”。对出现问题的语言进行反向验证：此前因预算耗尽而失败，如今可在 9 分钟内完成，且结构与源文件完全一致。

  - **上游托管商发生故障时，现在会明确指出其名称。** 路由器将这种情况标准化为 `finish_reason=error`，其中 `native_finish_reason` 为空——在两种语言上分别实测过一次，两次都恰好发生于 750 秒。原来的通用消息会让人误以为文档或分段有问题；现在则会说明故障位于供应商侧，并提示重试通常即可解决。

  - **`finish_reason=length` 加上空输出并不表示截断。** 这意味着推理预算在生成第一个有效字符前就已耗尽——实测为 15,850 个推理 tokens，仅产生 148 个有效 tokens。这两种情况需要采取相反措施：在前一种情况下，缩小分段毫无用处。消息现已明确区分二者。另外两项防护也来自实测：上游托管商失败时，路由器会返回**状态码 200，但响应体中只有错误**（`choices[0]` 曾抛出不透明的 `TypeError`，掩盖了实际消息）；上下文窗口则从目录读取后写入 `MODEL_TOKEN_LIMITS`——目录中有 44 个模型的 `DEFAULT_TOKEN_LIMIT` 不正确，其中两个的上限仅为 4,095 tokens。

  - **`--model fournisseur/modèle` 为必填项，并且在进行任何网络请求前验证其格式。** OpenRouter 并非供应商：该选择涉及价格、许可证和数据处理方式，不能替用户作出。由于 slug 会被插入预检 URL，验证并非仅为改善易用性，而是防止向其中注入路径的防护措施：两个路由器共用的命名空间正则表达式接受 `a/b/..`，因此必须明确拒绝父目录段。`--eco` 不会生效，并会明确说明这一点。

  - **修正了三处表述，其中一处原本是错误的。** OpenAI 对 `codex exec` 的警告针对的是在共享 runner 上注入个人 session 文件，而不是仓库是否公开：README、CLAUDE.md 和代码此前都错误引用了这一警告。OpenCode 的身份验证位置在 1.18.27 中发生变化（现在是 `opencode.db` 的 `credential` 表，而不再是 `auth.json`）；“这里绝不会读取它”这一不变量仍然成立，但原地址已经过时。最后，OpenCode 章节不再将从未验证过的路径说成等价方案：Zen 网关和 Ollama 已完成端到端测量，而 GitHub Copilot、LM Studio 和 llama.cpp 尚未测量，README 现在会明确说明这一点。

  - **进行了一轮测量，并在 README 中加入推荐模型表。** 针对三组文档执行了三百多次翻译，目标涵盖十四种语言——一篇在 `--news` 模式下内容密集的博客文章、一份使用标准 Markdown 的本 README，以及四份从 GitHub 原样获取的知名项目 README。表格区分了此前常被混淆的两件事：翻译是否**完成**，以及其**结构是否与源文件一致**。三个模型在两份密集文档中从未丢失任何信息：`gemini-3.7-flash`、通过 ChatGPT 订阅使用的 `gpt-5.6-sol`，以及通过 OpenRouter 使用的 `z-ai/glm-5.2`——它们唯一的差异，是在一两种语言中漏掉了一对 `**`。核心结论是：**决定性因素是文档密度，而非 `--news` 模式**：通过订阅使用的 Grok 在博客文章上十四次失败十三次，却在十六份公开 README 中成功十四次；反向验证证实，其原因是在长分段上失去跟进能力。表格本身也附有警告：它并不详尽，结果具有时效性，耗时不能用于排名，正确做法仍是在自己的文档上进行测量。

  - **结构比较器在发布数据前得到修正，因为它会对非拉丁文字产生两种误报。** URL 后跟全角右括号 `）` 时，不会被止于 `)` 的正则表达式正确截断，导致提取出的字符串不同，尽管 URL 本身完全相同；法语中占五行、中文中仅占三行的引用也会让按行计数的结果下降。两项修正都经过反向验证：删除 URL、章节或行内代码仍能被检测到。若不修正，Gemini 和 Codex 公布的结果将分别是十四种语言中通过十一种和十二种，而不是十三种和十二种。

  - **测试**：新增文件 `tests/test_openrouter_provider.py`（60 项测试）——模型验证及父目录段拒绝、托管商固定选择（上限、状态、未声明上限、共同最低值）、`allow_fallbacks` 始终为 false、根据 `mandatory` 关闭或保留推理、完整输出契约（状态码 200 中的错误、没有 choice、区分空白输出与截断、异常的 `finish_reason`、空内容）、目录无法访问时预检采用失败即关闭策略、slug 缺失及没有健康托管商、flag 互斥性和文件名标签。完整测试套件现有 **473 项测试**。

  - **重构：将一个 4,253 行的单体模块拆分为多个模块，不改变任何一行行为。** `src/aipmt/translate.py` 被拆分到 `config`、`markdown`、`segmentation`、`guards`、`placeholders`、`news`、`prompts`、`notes`、`naming`、`pipeline`、`cli` 以及子包 `providers/` 中（每个 provider 一个模块，以 `base` 为基础，`registry` 负责解析和 dispatch）。每次移动都对应一个 commit，并由机械化方式证明其正确性：验证器会将包内所有顶层 AST 节点与参考 snapshot 比较，检查每个符号的位置、安全标记是否逐字保留，以及是否不存在未跟踪文件——这套临时工具将在下一版本中移除。可见的变化包括：`aipmt.translate` 变为一个 façade，并通过对象身份重新暴露原模块中无需 `_` 前缀即可访问的 64 个名称（其中 `__all__` 包含九个，即受支持的 API；其余为兼容性 alias），同时不再重新导出被 `import *` 顺带收集的 29 个依赖项和标准库名称；不再支持直接执行该文件（`python src/aipmt/translate.py`）——`aipmt` 和 `python -m aipmt` 仍是两种受支持的形式；公共函数的 `__module__` 现在指向其定义模块；SDK 改为在加载 `.env` 后导入，而不是之前导入，目前没有已知影响。427 项测试的标识符全部保留，并迁移到各自实际测试的模块：原先通过 façade 进行的 91 个 patch 现在指向真正查询相应名称的模块（实测其中两个即使没有 patch 仍会通过）；七项契约测试锁定 façade；gate 工具则在首次移动前完成重写，确保它们不会因停止检查而错误变绿——Lizard scope 改为带下限的目录范围、从已构建的 parser 读取 flags、按包设置覆盖率下限，并由 `release.sh` 枚举受跟踪模块。
  - **修复（pull request 审查）**：当目录条目缺少 `context_length` 时，OpenRouter 会拒绝该条目，而不再把默认的 128,000 tokens 记录为实测值——此前这还会导致“模型未列出”警告消失；当 `finish_reason` 为空（文档记录的类型为 `string | null`）时，以上游托管商提供的原始原因作为准确信息，其中 `max_tokens` 的值为 `length`。遇到 `part: null` 事件时，OpenCode 会返回其契约错误，而不是 `AttributeError`；如果 JSONL 流中有一行事件无法解析，也会拒绝整个流，而不是接受部分文本。三个 agent CLI 在调用期间收到 `SIGTERM` 时，都会终止 agent 的进程组——regen 的 `timeout` 曾使 agent 得以继续存活并消耗配额——并且进程组的 `SIGKILL` 始终遵循宽限期，因为正常退出的 shim 可能会留下仍在运行的孙进程。拆分过程中被分开的 `# fmt: off` / `# fmt: on` 对已重新合并；`--reasoning_effort` 的帮助信息现在会列出使用它的四个 provider。

- **1.12.0** Provider `--use_opencode`：通过开源 agent OpenCode 连接用户选择的供应商——本地模型、无需账户的免费模型、订阅或密钥（2026-09-04）：

  - **第八条 provider 路径，其性质不同于前七条。** [OpenCode](https://opencode.ai)（MIT）并非模型供应商，而是一个_路由器_，可连接用户在 OpenCode 中自行配置的服务：API key、订阅（GitHub Copilot、ChatGPT、SuperGrok）、OpenCode Zen 网关——它提供**无需账户**的免费模型——或**本地**模型（Ollama、LM Studio、llama.cpp）。该脚本以非交互模式驱动 `opencode run`，与驱动 Codex 和 Grok 的方式相同，并复用同一套子进程基础设施（独立进程组、超时后先执行 `SIGTERM` 再执行 `SIGKILL`、始终关闭 stdin、清理环境变量）。已通过**两次真实翻译**验证：使用 `opencode/mimo-v2.5-free` 将整个 README 翻译为英语——耗时 49 秒，仅一次 pass，结构与源文件一致（32 个标题、26 个代码结束标记、18 个链接、37 个 URL、37 行表格、135 处行内代码）——以及使用本地 `ollama/qwen2.5:7b` 翻译一个测试文件，全程无需任何密钥。

  - **`--model provider/modèle` 为必填项，而且这是一个明确选择。** 如果没有 `--model`，OpenCode 会回退到自己的默认模型；在全新安装中，该模型为 `opencode/big-pickle`，这是一个免费的“隐身”模型，其交互内容可能用于训练——实测响应的正是这个模型。替用户静默选择它，恰好就是本仓库致力于追踪的那类隐形切换；因此，错误消息会给出列出模型的命令（`opencode models`）和三个示例（本地、免费、订阅）。`--eco` 不会生效，并会明确说明这一点。仅在用户明确要求时，才会将 `--reasoning_effort` 原样作为 OpenCode 的 `--variant` 传递。

  - **隔离经过实测，而非想当然。** 一份内联配置（`OPENCODE_CONFIG_CONTENT`，在 OpenCode 的合并顺序中最后加载，因此优先于用户配置但不会替换它）定义了 agent `aipmt`，并拒绝所有工具（`permission: {"*": "deny"}`）：注册表甚至不会再向模型提供这些工具；当被要求“列出文件并运行 `id`”时，模型会回答自己没有工具。session 共享被禁用，外部 plugins 被排除（`--pure`），且绝不使用 `--auto`，工作目录则为空且用后即弃。两种静默注入已被实测并关闭：若没有 `OPENCODE_DISABLE_CLAUDE_CODE`，用户的 `~/.claude/CLAUDE.md` 会进入**每一个** prompt（仅发送一句“你好”时，输入 tokens 会从 186 增至 515）；若没有 `OPENCODE_DISABLE_PROJECT_CONFIG`，当前目录中的 `AGENTS.md` 也会被注入——其中一条“每个回答都必须以 BANANA 结尾”的指令确实被应用到了翻译中。全局 `~/.config/opencode/AGENTS.md` 仍会被注入：没有任何开关可以排除它，而通过挪用 `XDG_CONFIG_HOME` 绕过还会同时隐藏用户配置的供应商。因此选择如实记录，而不是拼凑规避方案。

  - **`exit 0` 不能证明任何事情，这是第三个 CLI，仍需保持同样的警觉——而且它还有两个特有陷阱。** 未知的 `--agent` 不会使 `opencode run` 失败：它只会在 stderr 上发出警告，然后**静默**回退到工具处于启用状态的编码 agent。如果内联配置未生效，翻译就会由一个能够写入文件的 agent 执行；因此，除以下条件外，输出契约还会验证不存在这条消息：返回码为 0、没有 `error` 事件、没有 `tool_use`、最后一个 `step_finish` 的状态为 `stop`（`length` 表示响应被截断）、文本非空。第二个陷阱是错误 JSON 事件完全**不透明**——只有“发生意外服务器错误，请查看服务器日志了解详情。”以及一个简单引用——而真正原因（`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`、`ProviderAuthError` 等）只存在于日志中。因此需要 `--print-logs --log-level ERROR`，并读取 stderr 的 `error="…"` 字段，同时排除紧随其后的 Bun trace。这样，遇到未知模型时会在一秒内失败，并明确指出原因。`--title` 还顺便避免了一次无关的 LLM 调用：如果没有它，OpenCode 会通过对 `small_model` 的额外一次交互生成 session 标题。
  - **机密信息：采用与 Codex 和 Grok 相同的模式过滤，但保留一个按名称指定的例外。** `OPENCODE_API_KEY` 会被保留：这是 OpenCode 自身的密钥（Zen 网关、Go 订阅），按名称提供给它——相当于它的 `auth.json`，并非由 aipmt 管理或计费的密钥。供应商应在 OpenCode 中配置（`opencode auth login`、`opencode.json`），绝不能在 aipmt 的 `.env` 中配置，其中的任何密钥都不会传入子进程。与订阅型 CLI 不同，CI 中不会拒绝密钥：在 runner 上使用 API 密钥或自托管模型都属于合法用途。

  - **防路径穿越保护现在检查插值后的值，而非原始值。** `provider/modèle` 包含一个会被 1.10.0 保护机制拒绝的 `/`——这是合理的，因为 `--model` 会被插入文件名 `--include_model`。文件名标签现在会先将 `/`、`\` 和 `:` 替换为 `-`，然后再进行任何插值（`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`，因为 `:` 在 Windows 下非法），上游保护机制检查的正是这个标签：`../../evil` 会变成目标目录下的简单名称 `doc-en-..-..-evil.md`，只有 `..` 仍会被拒绝，`--target_lang ../x` 亦然。`_ensure_within_directory` 范围保护仍作为第二层防线，保持不变。

  - **免费模型与本地模型，以及实测结果。** `opencode/mimo-v2.5-free` 翻译一个段落需 16 秒，翻译此 README 需 49 秒；`opencode/big-pickle` 处理 200 个单词需 40 秒，同时发出的两个请求在 5 分钟内均未响应，而单独发送时都能完成；`opencode/nemotron-3.5-lightning-free` 在 3 分钟内没有任何响应。因此使用 `REGEN_PROVIDER=opencode` 时必须设置 `REGEN_MODEL`，并且并行运行 **2 个作业**。本地方面，Ollama 通常将上下文配置为 4,096 个 token，而分段长度可达 16,000 个字符：因此必须使用带 `PARAMETER num_ctx 32768` 的 `Modelfile`，且质量取决于模型——在测试文件上，一个 7B 模型颠倒了列表并破坏了代码块的结束围栏，而网关模型完整保留了一切。

  - **此仓库的翻译现在绝不会再通过计费 API 完成。** 只要 `.env` 中留有密钥，`regen_translations.sh` 就会使用 OpenAI API，而 Codex 仅作为选择性启用项。准备此版本时正是如此：28 份翻译先被发送至 OpenAI API，随后印地语 CHANGELOG 又被发送至 Gemini API，尽管 ChatGPT 订阅的存在正是为了避免按量付费。现已取消密钥自动检测：**默认使用 Codex，并启用 `gpt-5.6-sol`**，即质量模型；`openai`、`gemini` 和 `grok` 除 `REGEN_PROVIDER` 外还要求提供 `REGEN_ALLOW_PAID_API=1`，这是一个具名豁免，以确保规则在作出决定时生效；未知的 `REGEN_PROVIDER` 会直接失败，而不是回退到 API。十项测试锁定了默认行为、拒绝行为和豁免机制。此版本的 28 份翻译均已通过 Codex 重新完成。

  - **速率限制的退避逻辑已提取为共享实现**（`_retry_on_rate_limit`）：Codex 与 Grok 的循环除标签外完全相同，再复制第三份就会超过重复阈值。三个 CLI 错误均派生自同一个 `_CliCallError`；有一项测试禁止其中任何一个脱离该继承体系，否则共享循环将无法再捕获它。

  - **测试**：新增文件 `tests/test_opencode_provider.py`（51 项测试）——完整输出契约、代理回退、从日志中读取原因、文本片段去重并忽略合成片段、超时终止进程组、429 退避、模型必填与验证、无机密信息的预检、二进制文件解析、分派接线、文件名标签及路径穿越反向验证。`tests/test_review_hardening.py` 将标志互斥性和无机密信息要求扩展至新 provider。gate 现在要求记录全部 **22 个 argparse 标志**。完整测试套件共 **382 项测试**。

- **1.11.1** 文档修复：README 终于列出了全部七种 provider 路径（2026-09-03）：

  - **1.11.0 的 PyPI 页面声称“4 个 API + Codex CLI”。** 代码实际提供七种路径——通过 API 使用 OpenAI、Mistral、Claude、Gemini 和 Grok；通过订阅使用 Codex（ChatGPT）和 Grok，无需按量付费。简介和 _多供应商_ 条目都遗漏了两种 Grok 模式，14 份翻译也重复了这一错误。由于软件包的长描述在每个版本中都是固定的，要修正展示页面就必须发布新版本号：这就是此版本存在的唯一原因。**没有任何代码变更。**
  - `CLAUDE.md` 已与发布流程引入的内容保持一致：gate 计数器（16，`--full` 中为 17）、十一个活跃 workflow、`gh pr checks` 中不可见的两个 Sonar/Codacy 计数器（hotspot、Codacy API）、通过 `ruff-format` 移动一个 `# nosemgrep`、OIDC 交换所要求的 GitHub environment，以及 _待处理发布者_ 不会保留名称这一事实。

- **1.11.0** 发布至 PyPI：先执行 `pip install ai-powered-markdown-translator`，再执行命令 `aipmt`，无需克隆仓库（2026-09-03）：

  - **单文件脚本成为可安装的软件包。** `translate.py` 从根目录迁移至 `src/aipmt/translate.py`，并提供控制台入口点 `aipmt` 及其等效形式 `python -m aipmt`。参与贡献时仍需克隆仓库——测试、28 份翻译和质量工具均位于其中——但使用时不再需要。

    - **导入名称为 `aipmt`，绝不能是 `translate`**，因为冲突真实存在且不会发出提示。PyPI 软件包 `translate`（v3.8.1，最后上传于 2026-07-06）会安装一个同名目录。在 venv 中复现：该目录优先于模块，`translate.main` 消失，入口点在 `AttributeError` 处崩溃——而 `pip check` 返回“No broken requirements found”，且 rc=0。用户只需安装一个 `pip install translate`，就足以让 CLI 在没有可用诊断信息的情况下损坏。使用真实 wheel 进行反向验证：在该软件包之上安装 `pip install translate`，`aipmt --help` 在安装前后均为 rc=0，两个 CLI 可以共存。
    - **发行版名称长，命令名称短。** `ai-powered-markdown-translator` 使软件包能够通过 PyPI 搜索找到；对于尚不了解项目的人，单独的缩写无法被发现，而此次发布的目的恰恰是让项目可被找到。经核查排除了两个看似合理的候选名称：`ai-markdown-translator` 自 2024 年起已在 npm 上被一个用途相同的工具占用，比本仓库早 17 个月；`aimt` 与 `aim`（v3.29.1）仅相差一个字母，而后者是同一领域中的活跃软件包——这是最容易造成长期混淆的情况。另有一个方法论陷阱：`pypi.org/project/<nom>/` 会对任何名称返回 200（反机器人页面），只有 JSON API 的结果可信。
    - **采用 `src/` 布局，而非扁平软件包。** 扁平软件包本可保留测试中的六个 `sys.path.insert(..., "..")`，而问题恰恰在此：它们会导入源码树，而不是软件包，从而掩盖任何打包错误。实际代价仅为增加一条替换规则。

  - **密钥终于可以一次配置、永久使用。** 已安装的 CLI 过去没有任何持久配置：只能使用环境变量和当前目录中的 `.env`。`find_dotenv` 确实会一直向上搜索到系统根目录，因此在**个人目录之下工作时**能找到 `~/.env`，但在其他位置工作时则一无所获——这种覆盖取决于从何处启动命令，而非设计选择。因此新增第三层：`~/.config/aipmt/.env`，位于现有两层之后。

    - **优先级并非硬编码**，而是由 `override=False` 推导而来，它是 `load_dotenv` 的默认值：每一层仅填补上一层留下的空缺。因此顺序为环境变量 → 项目的 `.env` → 用户配置，并通过行为测试而非结构测试验证——交换两次调用的顺序会导致测试失败，移除第三层也一样。
    - **采用 `.env` 格式，而非 TOML**，这是有意为之：`python-dotenv` 已经是依赖项，其语法已在 15 份 README 中记录，并且同一文件可用于两个作用域。无需新增依赖项或语法。位置遵循 `XDG_CONFIG_HOME`，前提是它为**绝对路径**——规范要求忽略相对值，否则配置位置将再次取决于当前目录——Windows 下则遵循 `APPDATA`。
    - **排除了两个选项，并说明了原因。** 系统密钥环（`keyring`）在桌面计算机上更安全，但在无头环境中会失败——服务器、容器、CI——而这恰恰是批量翻译的使用场景；它适合作为选择性启用项，却不适合作为默认方案。`--api-key` 标志会使密钥进入 shell 历史记录，并让它在 `ps` 中可见。
    - **缺少密钥时，不再显示调用栈。** 用户过去会收到一段指向 `site-packages` 的 Python 堆栈，以及一条只提到“环境或 .env”、却未说明应在何处创建后者的消息。现在消息会列出三个位置及其确切路径，命令以状态码 2 退出。该保护网被**刻意限制在狭窄范围内**：仅在配置阶段对 `except ValueError` 生效。若包裹整个执行流程，翻译过程中出现的真实错误就会被转换成令人安心的消息——这正是此仓库所追踪的故障模式。有一项测试会读取 `main()` 的源代码以禁止这种做法。

  - **修复——工具安装后会忽略用户的 `.env`。** 不带参数的 `load_dotenv()` 不会从当前目录向上搜索，而是从调用方文件开始，也就是 `site-packages`。使用真实控制台入口点在一个拥有自身 `.env` 的项目中运行后实测：`find_dotenv()` 返回 `''`，且密钥未加载，而 `find_dotenv(usecwd=True)` 可以找到它。只要工具仅从克隆的仓库中运行，此错误就不存在；发布后它将成为系统性问题，唯一症状是在配置正确时仍提示 API 密钥“缺失”。

  - **三个 gate 即使完全停止验证任何内容也会显示为绿色。** 它们被有意安排在迁移**之前**加强：在变更完成后才编写本应捕获该变更的保护措施，无法证明任何事情。每个 gate 在原始仓库中均为绿色，在迁移后的副本中则变为红色——两个方向都经过实测。

    - **Lizard 会悄无声息地忽略不存在的路径**：rc=0，并显示“0 file analyzed”。复杂度 gate 原本会从 158 个函数 / 2247 nloc 降至 3 个函数 / 34 nloc，输出文件大小为零字节。现在作用域是一个数组，其中每一项都必须验证存在。
    - **对不存在的模块运行 `coverage run --source=` 不会失败**：仅在 stderr 中发出警告，unittest 与 `coverage xml` 均返回 rc=0，而且仍会发布报告——从 1453 条 statement 骤减至 141 条。项目之所以看起来健康，只是因为几乎已不再接受分析。两个下限用于保护报告：总量和测得的最大文件。
    - **翻译新鲜度探针在结构上无法识别调用形式**：它以 argparse 标志为锚点，而文件重命名恰好不会改变这些标志。复现结果：模块已移动，15 份 README 仍记录一个不存在的命令，判定却是“没有过期翻译”。因此第 7 节检查调用形式而非选项，并将 Lizard hook 与脚本的实际作用域进行比对——当其键 `files:` 不再匹配时，不会使 pre-commit 失败，而是直接跳过该 hook。

  - **`requires-python = ">=3.10"` 不再只是一句声明。** `sonar-project.properties` 早已宣称支持 3.10–3.12，却从未实际测试过，因为开发计算机上只有 3.12——这一内部矛盾会因发布而公开。现在有一个测试 workflow 会在 3.10、3.11 和 3.12 上运行测试套件，并安装软件包，从而验证其公开版本边界。

  - **设置下限，不设置上限。** `requirements.txt` 仍是经过测试的锁定版本，`[project.dependencies]` 则成为公开契约：若将锁定文件中的确切版本公开，会与任何安装了其他软件包的用户环境产生冲突。同样不设置 `<N+1` 上限——这会与 `check-deps-fresh.sh` 正面冲突，后者会在主版本更新滞后时使 release gate 失败。这组下限可以成功解析，而反向验证 `openai==1.0.0` 会以 `ResolutionImpossible` 退出，证明该检查能够进行区分，并非无条件接受。此外还有一项保护措施，禁止 `pyproject.toml` 的版本与 CHANGELOG 中的版本不一致：PyPI 不允许重复使用版本号。

  - **已在全新的 venv 中完成端到端验证**：约 70 KB 的 wheel 仅包含 `aipmt/*.py`、dist-info 和许可证；`aipmt --help` 返回 rc=0，并显示 22 个标志；`python -m aipmt` 显示“usage: aipmt”，而非“usage: \_\_main\_\_.py”；`pipx` 安装可用；最重要的是，**从任意用户目录完成了一次真实的法语→英语翻译**，粗体、列表、行内代码、链接和 URL 均被保留，代码块未被翻译。迁移前的 318 项测试全部通过，且迁移前后的标识符列表逐字节完全一致——真正证明没有测试被禁用的是这一点，而非“OK”；另新增 12 项测试用于三层配置，总计 330 项。

- **1.10.0** 新增 provider `--use_codex`（ChatGPT 订阅配额），更新 SDK 和模型，并修复多段落新闻引用（2026-08-29）：

  - **安全审查——PR 设置了两项保护措施，却没有在所有位置落实**：
    - **Codex 预检会将整个 `.env` 传递给二进制文件。** `_codex_preflight` 调用 `subprocess.run` 时**没有传入 `env=`**：子进程继承了完整的 `os.environ`，因而也继承了由 `load_dotenv` 加载的全部 `.env`。使用经过插桩的伪二进制文件测得：**七个秘密信息**进入了预检——六个 provider 的密钥以及一个 `GITHUB_TOKEN`；而对应的 `_grok_preflight` 为**零**，因为它正确传入了 `env=_grok_env()`。这种不一致存在于 PR 内部：仅相隔几行的 `_strip_secret_env` 正是为维持这一不变量而存在。现已提取一个 `_codex_env_base()` 并由两条路径共享；修复后的测量结果：两侧均为 0 个秘密信息。
    - **“`--deny` 失败时关闭”这一属性并未覆盖实际使用的形式。** 注释将整个 Grok 隔离机制的合理性归因于：带未知前缀的规则会导致启动被拒绝。在 `grok 1.0.13` 上测得，这种验证**仅适用于带括号的形式**：`--deny 'CeciNestPasUnOutil(*)'` 会拒绝启动（“未知工具前缀”），而 `--deny 'CeciNestPasUnOutil'` 则会被静默接受。然而 `GROK_DENY_RULES` 只使用了裸名称——因此，若 xAI 端重命名工具，在操作系统 sandbox 本就不适用的机器上，唯一经过测量的隔离层就会在毫无提示的情况下被移除。八条具名规则现已改为 `Prefix(*)`，每条都被 CLI 验证为已知前缀；兜底规则 `*` 仍保留其字面形式，这是唯一被接受的形式。一项测试可防止退回未经验证的形式。
    - **其他方面均已确认无问题**：不存在命令注入（始终使用列表形式，从不使用 `shell=True`，文档内容通过 stdin 或 `--prompt-file` 传递）；不存在不安全的反序列化（仅使用 `json.loads`，且有类型保护）；路径遍历修复在七个恶意载荷上均未发现绕过方式；并且 `--deny '*'` 确实由 CLI 应用（在读取 workdir 之外的内容时观察到 `DENY_ENFORCED`）。
    - 上文新增的新鲜度检查顺带绕过了自身原则：当某个包的 PyPI 请求失败时，它会被静默跳过，gate 仍显示通过。现在它会统计实际完成比较的包，并在覆盖不完整时失败。

  - **依赖项已升级，并增加两道防线以避免再次落后**：

    - **依赖落后确实存在且持续已久**：`openai` 2.54 → **3.6.0**、`anthropic` 0.125 → **1.2.0**、`certifi` 2024.8.30 → **2026.7.22**——其中用于验证所有 provider TLS 调用的根证书存储落后了两年。已确认原因：**不存在 `.github/dependabot.yml`**。没有该文件，GitHub 只会启用安全更新，而 Dependabot 仅会为受到 CVE 影响的依赖提出 PR——这解释了为何它升级了 `urllib3` 和 `idna`，却任由两个 SDK 落后整整一个主版本。
    - **两个主版本可以共存且没有冲突**，与此前的推断相反：`openai` 3.x 和 `anthropic` 1.x 已迁移至 **`httpx2`**，而 `mistralai` 和 `google-genai` 仍使用 `httpx<1`，但它们是两个不同的发行包。先通过实际安装验证，随后又对 **7 条 provider 路径进行了端到端测试**——OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI 和 Grok CLI——每项输出中的内联代码和链接均得到保留。“避免两套 HTTP 栈”只是一种偏好，并非阻碍：测量结果已给出结论。
    - **`requirements.txt` 并未描述真实环境**：`google-auth`、`cryptography` 和 `opentelemetry` 栈安装在工作 venv 中，却从未声明——因此全新安装无法复现测试环境。相反，`tokenizers`、`huggingface-hub` 和 `PyYAML` 虽列于其中，却未被任何内容导入或需要，它们是 `mistralai` 1.x 的遗留项。该文件已重新生成，完整涵盖仅从直接依赖构建的 venv。`pip-audit` 未在新依赖集中发现任何已知漏洞。
    - **`.github/dependabot.yml`**（新增）启用每周版本更新，覆盖 pip 和 github-actions。次版本与补丁更新合并到一个 PR——每个补丁升级各开一个 PR 最终只会被忽略，而噪声正是更新的敌人；**主版本单独处理**，每个都要求通过真实调用验证。
    - **`scripts/check-deps-fresh.sh`**（新增，已接入 gate）让依赖落后情况直接体现在项目判定中：Dependabot 只会提出更新，并不提供保证，其 PR 也可能不断堆积。主版本落后 → 失败；次版本落后 → 警告，因为长期保持红色的 gate 最终会被忽略；PyPI 无法访问 → 本地明确跳过，**CI 中失败时关闭**，因为未执行的检查不等于成功。已从正反两方面验证：它能准确捕获修复前的状态（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`），而对于次版本落后只发出警告。

  - **本次 PR 审查产生的修复**——五个审查代理仔细检查了 diff；以下所有问题均在修复前通过测量**成功复现**，其中两个还是本版本上文引入的回归。

    - **已修复回归——`_NEWS_CITATION_REGEX` 存在指数级回溯。** 多段落修复在重复结构中引入了 `(?:[ \t]*$|[ \t]+.*)`：`[ \t]+` 与 `.*` 之间的空格归属存在歧义，且这种歧义会随迭代次数成倍增长。在无法匹配该模式的 `>   texte` 行——完全合法的 Markdown 缩进——上测得：**14 行耗时 2 589 毫秒**，修复后仅为 0.04 毫秒，每增加一行耗时约增长 9 倍。在 `--news` 模式下，一段很长但不合规的 blockquote 就足以让翻译冻结，直至作业超时，且无法识别原因。现在，每次重复都会一次性完整消费整行（`\n^>(?![ \t]*—).*`），因此每轮迭代只有一种匹配方式。已在包含 231 篇文章的真实语料库上验证：捕获结果**零差异**，仍为相同的 423 条引文，14 个多段落正文也仍然得到扩展。
    - **同时使用两个 provider flag 会静默产生按量计费。** `--use_codex --use_mistral` 原本会被接受；`_select_provider_client` 会优先检查 Mistral，`_resolve_provider` 则优先采用显式布尔值——两者最终都会选择 Mistral。因此，用户请求使用订阅额度，得到的却是按量计费，且没有任何警告：这正是 `--use_codex` 应当防止的故障模式。六个 provider flag 现在统一通过一个 `add_mutually_exclusive_group`。**行为变更**：此前会被静默接受的、同时指定两个 provider 的命令行，现在会在 `argument --use_mistral: not allowed with argument --use_codex` 上失败。
    - **工作结束 gate 在探针崩溃时仍会显示通过。** `scripts/check-release-ready.sh` 的十三项检查中有四项遵循“捕获 stdout，若为空则下结论”的模式，却从不检查返回码：异常（文件被重命名、`FileNotFoundError`）会写入 stderr，使 stdout 保持为空，于是检查得出“一切正常”的结论。“一个 `exit 0` 什么也证明不了”的陷阱，竟在专门用来防止它的脚本内部重现。现在，辅助函数 `probe()` 会同时要求返回码为零**且**存在结束哨兵；当标记集合为空时，探针也拒绝得出结论——因为对空集的断言始终为真。示例：新增上述互斥组后，provider flag 改由 `*_group` 对象处理，而旧正则表达式 `parser\.add_argument\(` 不再能匹配它；**二十一个 flag 中有六个**静默脱离检查范围，gate 仍显示通过。
    - **秘密信息扫描遗漏了六个 provider 中的四个。** 字符类 `[A-Za-z0-9]` 排除了连字符：`sk-proj-…`（当前 OpenAI 格式）和 `sk-ant-api03-…` 会在第二个连字符处中断，而 `AIza…` 根本未被覆盖。现已扩展模式，并将 `.secrets.baseline` 排除在扫描之外。此外，保护逻辑 `.env` 查询的是 `git diff --cached`，它只能看到暂存区：一个**已经提交**的 `.env`——最糟糕的情况——永远不会出现。现在改为查询 `git ls-files`。
    - **Codex 的“令牌预热”实际上并未预热。** 测量结果表明：`codex login status` 不会接触 `~/.codex/auth.json`（修改时间与大小均未变化），其帮助信息写的是“显示登录状态”。然而注释却声称它会“单次、顺序地”刷新令牌，从而消除一次性轮换令牌并发刷新的风险。所宣称的保护并不存在；注释现在准确描述代码实际行为，真正的防护仍是 `max_jobs=4`。此外，检查现在会遵循此前被忽略的 `CODEX_BIN`——在 `PATH` 中没有 `codex` 的机器原本会因“未认证”而失败，给出误导性诊断。
    - **`.env` 在子 shell 中被 source。** `detect_provider` 通过命令替换调用，因此其 export 无法传回父级：在 `.env` 中定义的 `GROK_BIN`、`GROK_HOME` 或 `REGEN_MODEL`，对于 `main()` 中的读取仍不可见，导致配置正确时也会得出“找不到 Grok 二进制文件”的结论。
    - **并发量比声明上限高出 50%。** 保护逻辑位于启动 README/CHANGELOG 任务对之后：实测 `max_jobs=2` 的峰值为 **3**。对于 Grok，其每周额度与 Chat/Imagine/Voice 共享且无法测量，因此脚本自行设定的上限并未得到遵守。此外，最终计数虽会显示，却从未与 28 比较——文件缺失也不会被发现。
    - **Grok 输出契约：缺少 `stopReason` 现在会被判定为失败。** 代码原本应用的是“`end_turn` **或不存在**”，而声明的契约要求 `end_turn`。若 payload 不含该字段，或 CLI 更新后重命名了该字段，保护逻辑就会静默变成空操作。此外，`max_turn_requests` 不再被归类为速率限制（这是轮次预算耗尽：重试只会在等待 90 秒后重现相同结果），`quota` 也已移出速率限制标记——原因正如 `_codex_is_rate_limited` 的 docstring 早已说明的那样，只是 Grok 此前并未遵循。
    - **Gemini 级联现在按模型进行记忆化。** 此前每个片段都会从 `minimal` 重新开始，尽管默认模型会拒绝它：正常路径中的每个片段都会额外付出一次 400 往返，并重复输出相同警告。警告重复数百次后便不再有人阅读——它就这样变成了遮蔽物。
    - **其他事项**：CI 中的拒绝消息被硬编码为 Codex，导致 `--use_grok_cli` 用户被引导至 `OPENAI_API_KEY`，而非 `XAI_API_KEY`；`provider.capitalize()` 显示为“Grok_cli”和“Openai”；子进程基础层的注释将“shim”笼统套用于两个 CLI，但 Grok 二进制文件是原生 ELF（正确理由是“会生成自身子进程的代理”）；`subprocess` 上的十二项 SAST 发现已标记为 `# nosec` / `# nosemgrep` 并附有理由，使用不含 `shell=True` 的列表形式使注入成为不可能，且文档内容从不通过 argv 传递。
    - **任何秘密信息都不再进入代理型子进程。** 基于名称的拒绝列表此前只保护**计费**不变量（Codex 不含 `OPENAI_API_KEY`，Grok 不含 `XAI_API_KEY`）。实测表明：**另外七个秘密信息**仍会进入每个子进程——Anthropic、Mistral、Google 和 Gemini 的密钥、另一个 CLI 的密钥，以及并非秘密信息但会重定向流量的 `OPENAI_BASE_URL`。然而这两个 CLI 都是**代理**，而 Grok 在许多 Linux 机器上运行时没有适用的操作系统 sandbox。现在改为**按名称模式**过滤（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`），而不是使用名称列表，因此也能覆盖用户在 `.env` 中添加、但代码并不知晓的变量。CLI 不需要这些变量：认证信息位于 `~/.codex` 和 `~/.grok` 中，从不依赖环境变量——已分别通过两个 provider 在强化环境下**成功完成真实翻译**来验证。
    - **测试**：新增文件 `tests/test_review_hardening.py`（21 项测试），用于锁定 provider flag 的互斥性、`stopReason` 契约、news 正则表达式的线性复杂度、CI 拒绝消息、Gemini 记忆化，以及子进程环境中不存在任何秘密信息。最后一项断言是**通用的**——即使密钥未被任何列表命名，它也会失败——而现有的清除测试只是其常量的镜像，除自身循环失效外无法检测任何其他问题。完整测试套件现有 **311 项测试**。
  - **两个新的 Grok provider**：`--use_grok`（xAI API，密钥 `XAI_API_KEY`，按用量计费）和 `--use_grok_cli`（官方 Grok Build CLI，从 Grok 订阅额度中扣除——原理与 `--use_codex` 相同）。
    - **API 模式，约 40 行**：由于 xAI endpoint 与 OpenAI 兼容，client 和 `_call_openai` 均可原样复用，只有 `base_url` 发生变化。仅需进行一项适配，而且所有 provider 都能从中受益：`finish_reason` 现在接受 `end_turn`，这是 xAI 输出的格式，而 OpenAI 输出的是 `stop`。模型：`grok-4.6`（质量）和 `grok-4.3`（经济）。需要注意的是，Grok 的经济模型仍是仓库中最昂贵的——每百万 token 为 $1.25/$2.50，而 `mistral-small-latest` 为 $0.15/$0.60：选择这个 provider 是为了模型多样性，而不是价格。
    - **CLI 模式**：以 Codex 为蓝本，但根据实际情况存在四项差异——prompt 通过文件传递（`--prompt-file`，CLI 不读取 stdin，而 argv 中的 segment 会在 `ps` 中可见）；输出是 stdout 上的单个 JSON 对象（既不是 JSONL，也不是 `-o` 文件）；订阅仅提供 `grok-4.6` 和 `grok-4.5`；sandbox 无法应用（见下文）。子进程启动逻辑与 Codex 一同提取至 `_codex_run_process`，未改动已经过测试的 Codex provider 其余部分。
    - **实测表明，`exit 0` 无法证明任何事情**：未认证时，CLI 会向 **stdout** 写入 `{"type":"error","message":"Not signed in."}`，且退出码为 **0**。请求被拒绝或超出轮数时行为也相同。因此，输出契约要求同时满足四个条件：退出码为 0、没有错误 payload、`stopReason == end_turn`，并且文本非空。preflight 遵循同样的逻辑：即使未登录，`grok models` 也会以 0 退出，只有 stdout 中出现“not authenticated”才能得出结论。
    - **隔离：接受并记录这种不对称性。** Codex 在 `--sandbox read-only` 中运行，而 Grok 的 sandbox 在许多较新的 Linux 机器上无法使用，原因是两个相互独立的系统问题，且在没有 `sudo` 的情况下无法绕过：从 Ubuntu 24.04 起，AppArmor 会阻止非特权 user namespace（`bwrap: setting up uid map: Permission denied`，已在 Grok 之外复现）；当 `/run/podman` 处于 `0700` 状态时，container runtime socket 的 deny-list 会失败（resolver 仅处理 `ErrorKind::NotFound`，EACCES 会成为致命错误）。核心陷阱在于：无法应用的**内置**配置文件会悄然以无隔离方式启动。因此，脚本默认不请求任何配置文件，也绝不会静默回退——它会在 stderr 上发出警告。保护依赖于 CLI 的 `--deny` 规则，其中包括 catch-all `*`；这是唯一经过实测的 _fail-closed_ 层（使用未知前缀的规则会导致启动被拒绝）。可以通过 `GROK_TRANSLATE_SANDBOX=read-only` 强制要求该层；如果机器无法满足要求，启动将失败。
    - **防护措施**：从子进程环境中移除 `XAI_API_KEY`、`GROK_API_KEY` 和 `GROK_SANDBOX`（密钥会切换为按用量计费；继承的 `GROK_SANDBOX` 会强制使用无法应用的配置文件，并给出误导性消息），禁用 MCP/hooks/skills/agents 开关，使用 `--disable-web-search`、`--no-subagents`、`--no-plan`、一次性 workdir，在 CI 中拒绝运行，timeout 时终止整个 process group，并在遇到 rate limit 时执行 back-off。`--max-turns` 设为 6 而不是 1：计数器会在工具轮次结束后递增，设为 1 会截断输出。
    - **配额**：Grok 的额度池按周计算，并且**与 Chat、Imagine 和 Voice 共享**，同时没有任何命令可以显示该额度——这与 Codex 不同，后者可通过 `account/rateLimits/read` 量化消耗。因此，`regen_translations.sh` 将并发限制为 2，并明确发出警告。
    - **测试**：新增文件 `tests/test_grok_provider.py`（24 个测试）。完整测试套件共 **290 个测试**。
  - **已修复的 bug——多段英文引用仅受到部分保护（`--news` 模式）**：`_NEWS_CITATION_REGEX` 仅接受**连续的** `>` 行序列作为引用正文。一旦引用包含多个段落（由空的 `>` 行分隔），就只有最后一个段落会被捕获并替换为 placeholder；前面的段落会被发送给 LLM 并在返回时遭到翻译——这与 `--news` 所要保证的目标完全相反。重复匹配现在允许内部出现空的 `>` 行，并改为非贪婪模式，以便在斜体行之前的空 `>` 处停止，而不是在遇到的第一个空行处停止。
    - 在包含 198 篇真实文章的语料库上**测得的影响范围**：419 条引用中有 11 条受到影响。没有回归——新 regex 捕获的引用数量完全相同，只有多段正文的覆盖范围有所扩展（408 个正文保持相同，11 个得到扩展），而归属信息行 `> — …` 仍不可能被吸收到正文中（保留了 lookahead）。
    - 对一篇 69 KB 的文章进行 ja/ar 翻译的**端到端证明**：某条引用的第一段此前在日语中被渲染为 `> GLM-5.3がオープンウェイト化。`，在阿拉伯语中也同样遭到翻译，现在则保持为 `> GLM-5.3 is now open-weight.`。英文引用行数从 9 恢复到 10，与源文一致。
    - 需要注意的是，下游 validator 无法发现这个缺陷，因为它们只检查引用是否存在，而不检查引用是否完整。
  - **默认 provider 上实测的成本节省**：只要模型名称以 `gpt-5` 开头，`_openai_extra_kwargs` 就会发送 `reasoning_effort="medium"`，包括在 `--eco` 中也是如此。使用 `gpt-5.4-mini` 翻译一个十词句子的测量结果：`medium` → 45 个 reasoning token 和 65 个输出 token；`none` → 0 和 14。reasoning 对翻译毫无帮助，却会在每个文件的每个 segment 上产生费用。在 `--eco` 中，默认值现改为 `none`，其他情况下仍为 `medium`；通过 CLI 显式传入的值仍具有最高优先级。除 `low`/`medium`/`high` 外，`--reasoning_effort` 现在也接受 `none` 和 `xhigh`（并非所有模型都接受全部取值：例如 `gpt-5.4-mini` 会拒绝 `minimal`——现有的无参数 retry 会处理这种情况）。
  - **SDK 更新和 Gemini 迁移**：`google-generativeai`（支持已于 2025-11-30 结束，仓库已归档）被统一 SDK **`google-genai`** 取代——先调用 `genai.Client(api_key=...)`，再调用 `client.models.generate_content(model=, contents=, config=)`，system prompt 通过 `system_instruction` 传递，而不再与 segment 拼接。`mistralai` 升级至 **2.9.4**（import 改为 `from mistralai.client import Mistral`；旧写法会抛出 `ImportError`，已在 wheel 中验证），`anthropic` 升级至 **0.125.0**，`openai` 升级至 **2.54.0**——这些都是切换到 `httpx2` 之前的最后版本，以避免 venv 中同时存在两套 HTTP stack。`httpx` 0.28.1 和 `pydantic` 2.13.5 因此也得以解除版本锁定。
  - **由真实测试而非文档发现的两项回归**：
    - `anthropic` ≥ 1.0 会在 client 端拒绝预计耗时超过 10 分钟的非 stream 调用，其判断依据是 `max_tokens`（`ValueError: Streaming is required...`）。0.34.2 中不存在这项防护，因此它会破坏所有使用 `max_tokens=32768` 的 Claude 调用。现已通过显式设置 `timeout`（`CLAUDE_TIMEOUT`，默认 900 秒）修复，从而无需为了仅使用完整响应的调用而切换到 streaming。
    - 只有部分 Gemini 模型接受 `thinking_level="minimal"`：`gemini-3.1-flash-lite` 支持它，而 `gemini-3.7-flash` 和 `gemini-3.1-pro-preview` 会以 400 拒绝。因此新增 `_gemini_generate_with_fallback`，按照现有 OpenAI fallback 的模式执行 `minimal` → `low` → 不使用 thinking_config 的级联回退——优化参数绝不能导致翻译失败。
  - **更新默认模型**，每个模型均通过真实调用验证：OpenAI `gpt-5.5` → **`gpt-5.6-terra`**（28 个项目的 batch 成本降低 60%），`gpt-5.4-mini` → **`gpt-5.6-luna`**（降低 73%）；Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**（更便宜且更新），`claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（不含日期的 canonical ID）；Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**，`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（稳定版本，并且比 `3.5-flash-lite` 更便宜）。Mistral 保持不变，`mistral-large-latest` 仍是四者中性价比最高的模型。需要注意的是，不存在比 `gemini-3.1-pro-preview` 更新的 Gemini Pro 系列模型——2026 年 5 月公布的 Gemini 3.5 Pro 从未发布；3.5/3.6/3.7 产品线全部为 Flash。
  - **切换 Gemini 前进行的实测 A/B 对比**：使用 `gemini-3.1-pro-preview` 和 `gemini-3.7-flash` 将 `README.md` 翻译成日语。结构完全相同（21 个列表、18 个代码块、13 个 HTML 链接、13 张图片，所有 URL 均得到保留），耗时分别为 **8 秒和 48 秒**。由于没有任何公开 benchmark 对这两个模型在翻译或非拉丁文字脚本方面进行比较，否则此次切换只能建立在简单推测之上。
  - **Claude 响应块过滤**：`_call_claude` 原先直接执行 `block.text for block in response.content`，未过滤类型。使用 adaptive reasoning 的模型（Sonnet 5 及更高版本）会插入 `thinking` 块，该块提供 `.thinking` 而不是 `.text`——翻译会在第一个 segment 处因不透明的 `AttributeError` 而失败。现在会排除 `thinking`、`redacted_thinking`、`tool_use` 和 `tool_result` 块（采用负面列表，以继续容忍携带文本的未知类型），没有任何文本块的响应会抛出明确错误。每次调用都会传递 `thinking={"type": "disabled"}`。
  - **重新同步 `MODEL_TOKEN_LIMITS`**：移除退役日期已过的模型（`magistral-*` 系列已于 2026-07-31 退役，`gemini-2.0-*` 已于 2026-06-01 退役，`gemini-3-pro-preview` 已于 2026-03-09 退役，以及 `claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。修正限制：Mistral 128K → **256K**（Large 3 / Small 4 代），Gemini 1 000 000 → **1 048 576**（真实 input 限制），`claude-opus-4-5` 200K → **1M**，`gpt-5.6-*` 系列 400K → **1.05M**。新增 Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest` 和 `ministral-*` 系列。需要注意的是，这些限制仍仅供参考，因为 `translate()` 会将 segmentation 上限设为 `min(16000, limite)`。
  - **Provider `--use_codex`**：第五个 provider，驱动官方 Codex CLI（`codex exec`）以非交互模式运行，而不是调用按用量计费的 API。翻译用量从已付费的 ChatGPT 订阅配额中扣除。这是 OpenAI 针对此用途记录的唯一方式：各套餐可用性矩阵将“Codex SDK、`codex exec` 和可编程工作流”列为 Plus/Pro/Business/Enterprise 可用功能，而 `~/.codex/auth.json` 的 token 无法认证 API Platform 调用（且此脚本从不读取它们——认证及其刷新仍由 CLI 管理）。
  - **可通过 pip 安装 Codex 二进制文件，不再仅限 npm**：`_resolve_codex_binary()` 会依次在 `CODEX_BIN`、`PATH`，以及 OpenAI 发布的官方 Python package **`openai-codex-cli-bin`**（即 SDK `openai-codex` 的依赖项）中查找二进制文件。因此，Python 项目无需再全局安装 npm 即可使用 `--use_codex`。该 package 未添加到 `requirements.txt`：二进制文件约为 250 MB，若添加，所有用户都必须为一个可选 provider 承担这部分体积。已完成端到端验证：当 `codex` 不在 `PATH` 中时，解析过程能够找到打包的二进制文件，并在 6 秒内完成整篇翻译。
  - **“订阅模式”保证**：从子进程环境中移除 `OPENAI_API_KEY` 和 `CODEX_API_KEY`。若没有此保护，`.env` 中存在的密钥可能会让 Codex 在没有任何可见提示的情况下切换到按用量计费——而避免这种情况正是此 provider 存在的目的。
  - **通过测试锁定 CLI 陷阱**：
    - 即使 prompt 已通过参数传入，`codex exec` **仍会**读取 stdin：若不关闭 stdin，命令会一直等待到超时，且永远不会调用模型（已复现：180 秒后以 exit 124 退出，零字节）。因此必须使用 `communicate(input=...)`。
    - 通过 npm 安装的 `codex` 是一个 Node shim，会用 `spawn` 启动真正的 Rust 二进制文件：后者是 Python process 的**孙进程**，在 `subprocess.run(timeout=)` 收到 `SIGKILL` 后仍会存活，并继续消耗配额。因此需要 `Popen(start_new_session=True)` + `os.killpg`。
    - CLI 可能在发出 `turn.failed` 的同时以 0 退出：除返回码外，还会检查 JSONL 输出（`--json`）；若返回码为 0 但缺少 `-o` 文件，则会抛出明确错误，而不是生成空 segment。
  - **rate limit back-off**：CLI 未实现任何内部 retry（`max_retries = 0`）。分类依据 JSON payload 的结构（`status: 429` / `error.type`），而非子字符串——“quota”一词既会出现在可恢复的 429 中，也会出现在永久性的 `insufficient_quota` 中。
  - **CI 保护**：若定义了 `CI` 或 `GITHUB_ACTIONS`，则拒绝 `--use_codex`。订阅认证并非为共享 runner 设计，OpenAI 也明确不建议在公共仓库中采用此工作流。
  - **模型**：`gpt-5.6-sol`（质量）和 `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` 系列同时用于 CLI 和 API Platform，但 ChatGPT 账户并非拥有其中所有模型的使用权限：allowlist 在服务端应用，不进行本地验证，使用不常见的模型会触发警告。在 Plus 套餐中，每个 5 小时窗口内，Luna 可提供 250–2,000 条消息，而 Sol 仅为 10–100 条：`--eco` 是所有批处理任务的推荐模式。
  - **已修复 Bug——`regen_translations.sh` 在完全成功后仍以错误退出**：`trap ... EXIT` 引用了 `failed_log`，它是 `main()` 的一个 `local` 变量，在 trap 执行时已不存在。在 `set -u` 下，这会引发 `failed_log: unbound variable`，导致脚本以 1 退出，尽管 28 项翻译均正确——这会让 `release.sh --auto`（`set -e`）在重新生成后、也就是成本最高的阶段立即中断。该变量现已改为全局变量，trap 会检查它是否存在。另一个有益的副作用是：此前被此错误掩盖的真实翻译失败，现在会重新显示在最终摘要中。
  - **`REGEN_MODEL`**：`regen_translations.sh` 新增的环境变量，可覆盖 provider 的默认值并强制指定模型，例如使用 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`，以便通过订阅配额中的高端模型重新生成，而不是使用面向大批量处理的 `--eco` 模型。
  - **`regen_translations.sh`**：`REGEN_PROVIDER=codex` 可通过明确选择启用（绝不自动检测，以免在用户不知情的情况下消耗订阅配额）。在启用并行处理前，会先按顺序刷新一次 token——由于 Codex refresh 采用轮换机制且只能使用一次，并发 job 会使 `codex login` session 失效——并将并发数降至 4。
  - **相关 refactor**：`_dispatch_provider_call` 通过返回 provider 名称的 `_resolve_provider()`，将参数数量从 8 个减少到 6 个，避免在整个调用链中传递第四个 boolean。显式 boolean 仍优先于 `args`，以保留那些使用最小化 `Namespace` 调用 `translate(..., use_mistral=True)` 的测试。
  - **测试**：新增文件 `tests/test_codex_provider.py`（48 项测试），覆盖 argv、清理后的环境、禁止前言契约、静默失败、timeout/killpg、back-off、preflight、provider 解析、Gemini 推理级别级联、Claude block 过滤，以及多段 news 引用。完整测试套件共 290 项测试。
  - **真实验证**：项目的 `README.md` 通过 Codex 翻译为 **14 种语言**后，其结构与参考翻译严格一致（14 个代码块、24 个标题、25 行表格、13 个 HTML 链接、13 张图片、19 个 URL；代码块逐字符完全一致，placeholder 零残留）。对于一篇 69 KB 的新闻文章，在 `--news` 模式下，`gpt-5.6-luna` 和 `gpt-5.6-sol` 的输出均通过下游应用验证器对 en/ja/ar 的验证。通过 `account/rateLimits/read` 测得的消耗在 `--eco` 模式下始终低于计数器的舍入阈值（5 小时窗口的 0%）。

- **1.9.2** 修复包含嵌套括号或 FR 前缀的 news 署名 URL 提取问题（2026-05-11）：

  - **已修复 Bug**：`_protect_news_quotes` 中的署名 URL 提取使用 regex `re.search(r"\((.+?)\)", attribution)`（括号之间的惰性捕获）。对于 `(relayé par [@user sur X](https://x.com/.../123))` 这类署名（嵌套括号：外层 `(` + markdown link 的 `]()`），捕获会在遇到第一个 `)` 时停止 → 得到被截断且包含 FR 前缀的字符串：`relayé par [@user sur X](https://x.com/.../123`（缺少结尾的 `)`）。结果是 `_validate_news_post` 在翻译输出中查找该字符串时始终失败（有两个原因：`)` 被截断 + “relayé par”被翻译为 `relayed by`/`weitergeleitet von`/……）。完整的 low → medium → high → gpt-5.5 级联均无法通过。
  - **修复**：regex 改为 `re.search(r"\]\(([^)]+)\)", attribution)`——专门匹配 markdown link 的 `](url)`，且**仅捕获纯 URL**（不包含 FR 前缀，也不会截断）；翻译期间通过 placeholder `#URL{N}#` 保持其不变。能够稳健处理以下两种问题模式：
    - `(relayé par [@account sur X](url))`——嵌套括号
    - `via [@source](url)` 或 `selon [@author](url)`——没有外层括号的 FR 前缀
  - **测试**：在 `test_silent_failure.py` 的 `TestNewsCitationExtraction` 类中新增 2 项测试：
    - `test_extract_attribution_url_with_nested_parens`（精确复现 Genspark CEO E2B Bug 的案例）
    - `test_extract_attribution_url_with_french_prefix`（包含 `via` 的变体）
  - **覆盖缺口**：`check-editorial-coverage.py` 会验证编辑语法，但不会验证 translator 是否能够处理。一个可能的改进方向（不在 v1.9.2 范围内）是增加检查，通过 dry-run 模拟署名提取，以便在发布**之前**检测高风险模式。

- **1.9.1** 修复翻译 marker 注释中 CTA label 的 i18n 问题（2026-05-10）：

  - **已修复 Bug**：翻译文件顶部 marker 横幅中 CTA 链接的 label `[Voir le projet sur GitHub ↗]` 对所有目标语言都仍为**法语**，而没有随 `target_lang` 变化。LLM 从未看到它（它由 Python 端组装，以保留 URL 和仓库 slug），因此翻译阶段无法补救。自 v1.9 添加 `marker` 格式以来，这一直是一个静默 regression。
  - **修复**：新增常量 `_VIEW_PROJECT_LABELS`，将 15 种语言映射到对应的本地化 label。`_translation_note_invariants(target_lang)` 和 `_assemble_translation_note_paragraphs(phrase, target_lang)` 现在会传递目标语言。若语言未知，则 fallback 到 `fr`（确保安全，避免 KeyError）。
  - **测试**：调整 `test_source_emits_three_paragraphs_repo_title_description_link`（target_lang `ja` → 预期为日语 label）。新增 2 项测试：`test_source_link_label_localized_per_target_lang`（以 7 种语言参数化，覆盖拉丁文字、表意文字和 abjad）以及 `test_source_link_label_falls_back_to_french_for_unknown_target`。`test_translation_note_position.py` 中现共有 40 项测试（此前为 38 项）。
  - **向后兼容性**：签名带有默认值 `target_lang="fr"`——未传入 `args.target_lang` 的外部编程调用方无需修改即可继续工作。
- **1.9** 修复静默失败 + 完整质量工具链 + 多位置翻译说明（2026-05-07）：
  - **多位置翻译说明 + “embed card”标记格式**：
    - 新增 CLI 选项（增量添加，默认值不变 → **非破坏性变更**）：
      - `--note_position {top,bottom,both}`（默认：`bottom`）：将说明放置在译文文件的顶部、底部或两处同时放置。
      - `--note_format {legacy,marker}`（默认：`legacy`）：
        - `legacy` 严格复现 v1.8 的行为（粗体段落 `**…**`），实现**逐字节一致**。
        - `marker` 输出一个不可见的 Markdown 链接引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），随后是结构化的**三段式 blockquote**，以呈现类似“GitHub 仓库嵌入卡片”的效果：使用行内代码显示项目标题（`**\`ai-powered-markdown-translator\`\*\*`）、由 LLM 翻译的描述，以及带可见箭头的 CTA 链接（`[Voir le projet sur GitHub ↗](URL)`）。构建时可由 remark 插件处理（参见 jls42.org 博客 → 插件 `remark-translation-banner`）。
    - **绝不发送给 LLM 的不变量**：仓库标题和 GitHub URL 在描述句翻译完成后由 Python 端组装。LLM 永远不会看到 slug `ai-powered-markdown-translator` 或 `https://github.com/jls42/...`，从而确保 renderer、大小写和 scheme 均不会被更改。
    - **感知 frontmatter 的插入机制**：在 `top` 或 `both` 模式下，说明会插入到 YAML frontmatter 的闭合 `---` 块**之后**（保障 Astro Content Collections / gray-matter 的安全性）。辅助函数 `_split_frontmatter` 检测文件开头的 `---\n…\n---\n` 并保持其完整性；如果 frontmatter 已开启但没有闭合 fence，则**抛出 `RuntimeError`**（文件会进入 `failed_files`，而不会因说明位置错误而被写入）。
    - **基于白名单的模型 sanitizer**：`_sanitize_model` 将 `[A-Za-z0-9._:/-]` 之外的所有字符替换为 `_`，为空时回退到 `unknown`。这与 Astro remark 插件端的验证器保持一致，并消除会破坏标记格式的字符（空格、引号、括号、逗号等）。
    - **内部重构**：`_append_translation_note`（一个单体函数）→ 7 个纯辅助函数（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。builder 与 composer 分离（builder 返回不含分隔符的纯块，composer 根据位置应用 `\n\n`）；生产代码与辅助函数源码共享同一个三段式组装器。
    - **`_quote_lines` 保留空行**：为每一行添加 `> ` 前缀，并将空行转换为单独的 `>`。这样 mdast 会将 blockquote 识别为三个独立段落（标题／描述／链接），而不是一个带换行符的段落。
    - **自适应 `_build_translation_note_block`**：根据 LLM 保留的段落数量处理（3 = 完整卡片格式，2 = 描述句 + 链接，1 = 回退格式）。当检测到 Markdown 链接 `](` 时，单段落回退格式**不再包裹于 `**...**` 中**（在链接周围渲染 `<strong>` 的效果不稳定）。
    - **向后兼容性**：`_compose_with_notes` 端使用 `getattr(args, "note_position", "bottom")` 和 `getattr(args, "note_format", "legacy")`——缺少这些属性的 Namespace（现有测试、外部编程调用）无需修改即可继续工作。
  - **修复长篇翻译中的静默失败**：
    - 对所有 provider（OpenAI、Mistral、Claude、Gemini）执行翻译后语言验证：确定性层（在输出中发现原文逐字片段）+ 概率层（`langdetect`）
    - `finish_reason` / `stop_reason` 白名单：任何不在白名单内的状态（截断、content_filter 等）均抛出 `RuntimeError`
    - Claude 的 `max_tokens`：`4096` → `32768`（避免 16k 分段发生隐性截断，并为 FR→JA/ZH/KO/AR/HI 的跨文字系统转换预留余量）
    - 感知 heading 的分段：优先选择分段后半部分的 H2/H3（使每个分段均以完整的语义章节开始）
    - 将错误传播至非零退出码：`translate_markdown_file` 返回类型化状态 `success` / `failure` / `skipped`；只要至少有一个文件失败，`main()` 即执行 `sys.exit(1)`（单文件和批处理均适用）
    - 为所有 provider 添加空内容防护、源文本／输出文本合理性比率检查（源文本 ≥ 500 个字符且输出少于其 5% 时拒绝）、代码占位符验证（`#CODEBLOCK`/`#INLINECODE`）、LLM 后规范化（修复与 heading 粘连的分隔符／链接），以及不带 `reasoning_effort` 的 `BadRequestError` 重试
    - 新增依赖 `langdetect==1.0.9`
  - **pre-commit 质量工具链**（“完整 EurekAI 类型”，14 个 hook）：
    - Pre-commit：ruff（lint + format）、shellcheck、prettier（md/yaml/json）、detect-secrets（保护 4 个 API key）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（空白字符、EOF、大文件、shebang 等）
    - Pre-push：mypy（渐进式宽松模式）、Opengrep SAST（translate.py + scripts/）、pip-audit（初始报告模式）、unittest discover（tests/ + scripts/tests/）
    - `scripts/` 中使用 `./venv/bin/python` 的本地 wrapper
    - `scripts/audit_verdict.py`：pip-audit JSON 解析器，包含 11 个 unittest，由 jls42-astro 解析器移植并适配 Python
    - 修复了最初的 7 个 ruff 违规：B904（raise from）×2、B007（未使用的 dirs）、C408（dict 字面量）、C419（list comprehension）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizard 暂时排除 `translate.py`（4 个函数的 CCN 为 21–47，已规划重构）——对 scripts/ 启用严格 gate
  - **SonarCloud + 全面覆盖率**：
    - GitHub Actions 工作流 `SonarCloud`（sonarcloud.yml + sonar-project.properties）：每次 push 和 pull request 时进行分析，并通过 `coverage.xml` 生成 coverage
    - README 顶部添加 11 个 SonarCloud 徽章（Quality Gate、Security/Reliability/Maintainability 评级、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）
    - `tests/test_silent_failure.py`（`unittest` 标准库）：覆盖静默失败错误链的六个环节
    - `tests/test_orchestration.py`（新增 79 个测试）：覆盖 `translate.py` 的 orchestration 层（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` TypeError + BadRequestError 回退、o1 系列 prompt 格式、`_validate_translation_output` 的 early-return 分支）
    - `scripts/tests/test_audit_verdict.py`：通过 subprocess 覆盖 `main()`（stdin/stdout）和 `if __name__ == "__main__"` 块
    - **新代码覆盖率**：75.5% → 约 98%（translate.py 为 98%，scripts/audit_verdict.py 为 97%）
  - **测试**：`tests/test_translation_note_position.py` 覆盖位置 × 格式矩阵（包括 E2E `marker+top|bottom|both` 和 `legacy+top|bottom|both`）、多行前缀处理、逐字节向后兼容性（golden 字面量）、sanitizer、frontmatter 拆分（包括 fence 未闭合时抛出异常）、三段式格式、两段式回退、单段落 + Markdown 链接防护，以及一个关键保护测试 `TestLLMPayloadExcludesInvariants`，用于断言标题和 URL 绝不会发送给 LLM。**190 个测试通过**，0 个回归。
  - 文档：`README.md`（法语 + 14 种译文）已添加徽章，`CLAUDE.md`（pre-commit 工作流 + 详细的 CI 监视说明），重新生成了 28 份译文
- **1.8** `--news` 模式 + 2026 模型升级（2026-03-17，标签 `v1.8`）：
  - 更新默认模型（2026 年 3 月）：
    - OpenAI 高质量：`gpt-5` → `gpt-5.4`
    - OpenAI 经济型：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 高质量：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - 为 `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）和 `gemini-3.1-pro-preview`（1M）添加 token 限制
  - 初始 `--news` 模式：使用占位符 `#NEWSQUOTE\d+#` 保护英文引用、`LANG_FLAGS` 映射（15 种语言）、按目标语言管理旗帜
  - 在恢复 news 占位符之前进行验证（回归问题：LLM 删除占位符时，会静默生成缺少引用的输出）
  - 使脚本 `regen_translations.sh` 可移植（使用绝对路径，不依赖 pwd）
  - 在 README/CHANGELOG 的语言栏中添加法语，并重新生成 28 份译文
- **1.7** 新功能：
  - 新增 `--keep_filename` 选项，在翻译时保留原始文件名
  - 支持通过 `.env` 文件自动加载 API key
  - **保留行内代码**：翻译期间现在会保护反引号（`` `...` ``）
  - 改进 system prompt：
    - 更妥善地处理 YAML frontmatter 中的引号
    - 保护模板变量 `{variable}`
    - 禁止添加未经请求的译者注
  - 已在 364 个文件上成功测试（jls42.org 博客迁移）
- **1.6** 新功能：
  - 支持使用 Google Gemini API 进行翻译（`--use_gemini`）
  - 更新 2026 年默认模型：
    - OpenAI：`gpt-5`（高质量）、`gpt-5-mini`（经济型）
    - Claude：`claude-sonnet-4-5`（高质量）、`claude-haiku-4-5`（经济型）
    - Gemini：`gemini-3-pro-preview`（高质量）、`gemini-3-flash-preview`（经济型）
  - 经济模式（`--eco`），用于采用速度更快、成本更低的模型
  - 支持翻译单个文件（`--file`），无需遍历目录
  - 新的简化命名模式：`{base}-{lang}.md`
  - 新增 `--include_model` 选项，以保留包含模型名称的旧格式
  - 支持未列出的模型，并使用默认 token 限制（128k）
  - README 已翻译为 14 种语言
- **1.5** 改进：
  - **更新 API key 和默认模型：**
    - **OpenAI：**从 `DEFAULT_MODEL_OPENAI` 更新为 `"gpt-4o"`。
    - **Mistral AI：**从 `DEFAULT_MODEL_MISTRAL` 更新为 `"mistral-large-latest"`。
    - **Anthropic Claude：**新增 `DEFAULT_ANTHROPIC_API_KEY`，并从 `DEFAULT_MODEL_CLAUDE` 更新为 `"claude-3-5-sonnet-20240620"`。
  - **优化翻译 prompt：**
    - 扩充了直接翻译和翻译说明所用的 prompt，以提升清晰度和效率，其中包括有关保留元数据及特定格式元素的详细指令。
  - **代码重构：**
    - 使用 `Mistral` 类替换 `MistralClient`，用于初始化 Mistral AI 客户端。
    - 重新组织 import，以提高可读性和可维护性。
    - 改进文本分段和代码块处理，以在翻译过程中保留原始格式。
  - **输出文件管理：**
    - 在输出文件名中调换模型和语言的位置（例如 `f"{base}-{args.target_lang}-{args.model}.md"`），以便组织和查找译文。
  - **其他改进：**
    - 删除无用空行以清理代码。
    - 进行细微调整，以改进脚本的结构和可读性。
- **1.4** 新功能：
  - 支持使用 Anthropic Claude API 进行翻译
  - 优化 prompt，以提高其清晰度和效率
  - 进行细微调整，以提高代码的可维护性
- **1.3** 改进与新功能：
  - 改进代码块处理
  - 改进输出文件管理
  - 改进现有文件检测
  - 新增 `--force` 选项以强制翻译
  - 在输出文件名中调换模型和语言的位置
- **1.2** 修复 changelog
- **1.1** 新增 Mistral AI API 支持
- **1.0** 初始版本——支持 OpenAI API

**使用 gpt-5.6-sol 将文章从法语翻译成中文。**
