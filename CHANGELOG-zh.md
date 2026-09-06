### 更新日志

🌍 [法语](CHANGELOG.md) | [英语](CHANGELOG-en.md) | [西班牙语](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [德语](CHANGELOG-de.md) | [日语](CHANGELOG-ja.md) | [韩语](CHANGELOG-ko.md) | [阿拉伯语](CHANGELOG-ar.md) | [印地语](CHANGELOG-hi.md) | [意大利语](CHANGELOG-it.md) | [荷兰语](CHANGELOG-nl.md) | [波兰语](CHANGELOG-pl.md) | [葡萄牙语](CHANGELOG-pt.md) | [罗马尼亚语](CHANGELOG-ro.md) | [瑞典语](CHANGELOG-sv.md)

- **1.13.0** Provider `--use_openrouter`：通往约 430 个模型的付费路由器，其中包括中国的开放模型（2026-09-05）：

  - **第九条 Provider 路径，与第八条一同发布。** 1.12.0 未发布到 PyPI：OpenCode 和 OpenRouter 两个路由器将同时推出。[OpenRouter](https://openrouter.ai) 通过一个密钥即可访问其他 Provider 在这里均未提供的模型——Kimi、Qwen、DeepSeek、Z.ai——所有用量均从同一份余额中按量计费。由于 endpoint 与 OpenAI 兼容，因此使用与 xAI 相同的客户端；**这个 Provider 的全部区别都集中在预检上**，而其中每条规则都源自对 API 的实测。

  - **同一模型由数十家具有不同上限的托管商提供，而路由对此毫无感知。** 实测：`z-ai/glm-5.2` 有 33 家托管商，`z-ai/glm-5.3-flash` 有 23 家——其中一家最多只能输出 **2 048 tokens**。因此，一次长篇翻译会随机被分配给这 23 家中的某一家，并在没有任何提示的情况下遭到截断。预检读取 `/api/v1/models/{modèle}/endpoints`，排除输出上限低于 8 000 tokens、状态异常以及未声明任何上限的托管商，然后固定使用其余托管商。只有 `provider.only` 而**没有** `allow_fallbacks: false` 仅表示偏好：路由器仍会转向已被排除的托管商，固定路由也就失去了意义。如果没有任何托管商满足上限要求，命令便会停止：仍然继续翻译，就等于接受这项预检本来要阻止的静默截断。

  - **推理按输出费率计费，而且许多模型默认启用。** 在 `z-ai/glm-5.2` 上发送相同请求并得到“OK”响应：**采用模型默认设置时生成 107 tokens，关闭推理后仅为 2 tokens**。对于推理毫无帮助的翻译任务，这会使每个文件的每个分段产生 18 倍开销。因此默认关闭推理。431 个模型中有 **288 个强制启用推理**（`reasoning.mandatory`），它们会返回 `400 « Reasoning is mandatory for this endpoint and cannot be disabled »`：对于这些模型，不会发送任何参数，而不会猜测应使用何种 effort——effort 会分配 `max_tokens` 的一个**百分比**供推理优先消耗，因此随意选择一个值，只会转移出现空白页面的风险，而不会降低风险。

  - **强制推理的模型会收到它所接受的最低 effort，而这一决定来自实测。** 最初的选择是什么都不发送，以免替模型做出猜测。在 `z-ai/glm-5.3-flash` 上验证时，该模型在目录中的默认值为 `max`，这一选择导致输出在翻译完成前便于 **32 768 tokens 处被截断**——十四种语言中有两种丢失。提高总额度也无济于事：effort 会从中按比例分配，推理量也会随之增长。因此，Provider 会在预检时读取 `supported_efforts` 并请求最低值；如果目录未公布任何可用值，则回退到“不发送”。对出错语言进行反向验证后发现：它之前因额度耗尽而失败，现在能在 9 分钟内完成，且结构与源文件一致。

  - **上游托管商发生故障时，现在会明确指出其名称。** 路由器会将这种情况规范化为 `finish_reason=error`，并附带空的 `native_finish_reason`——已在两种语言上测量两次，每次都恰好为 750 秒。过去的通用消息会让人误以为文档或分段存在问题；现在它会说明故障发生在供应商一侧，并指出重试通常即可解决。

  - **`finish_reason=length` 且输出为空并不代表截断。** 这是推理在输出第一个有效字符前耗尽额度——实测为 15 850 个推理 tokens，仅产生 148 个有效 tokens。两种情况需要采取相反的措施：在前一种情况下，缩小分段毫无作用。消息现在会明确区分二者。另外两项防护也来自实测：上游托管商失败时，路由器会返回**状态码 200，但响应体中只有错误**（`choices[0]` 会抛出一个不透明的 `TypeError`，从而掩盖真正的消息）；上下文窗口则从目录读取并写入 `MODEL_TOKEN_LIMITS`——对于目录中的 44 个模型而言，`DEFAULT_TOKEN_LIMIT` 是错误的，其中两个模型的上限仅为 4 095 tokens。

  - **`--model fournisseur/modèle` 为必填项，并且在任何网络请求前都会验证其格式。** OpenRouter 并不是供应商：这一选择涉及价格、许可证和数据处理方式，不能代替用户做出。由于 slug 会插入预检 URL，因此验证并非单纯的易用性措施，而是防止注入路径的保护机制：两个路由器共用的带命名空间 regex 接受 `a/b/..`，因此会明确拒绝父级路径段。`--eco` 不会生效，并会明确说明这一点。

  - **修正了三处表述，其中一处原本是错误的。** OpenAI 对 `codex exec` 的警告针对的是在共享 runner 上注入个人会话文件，而不是仓库是否公开：README、CLAUDE.md 和代码此前都错误解读了该警告。OpenCode 的身份验证位置已在 1.18.27 中发生变化（现为 `opencode.db` 的 `credential` 表，而不再是 `auth.json`）；“这里从不读取它”这一不变量仍然成立，但原地址已经过时。最后，OpenCode 章节不再把从未验证过的路径描述为等价选项：Zen 网关和 Ollama 已完成端到端实测，而 GitHub Copilot、LM Studio 和 llama.cpp 尚未经过验证，README 现在会如实说明。

  - **开展了一轮测量，并在 README 中加入推荐模型表。** 在三组文档上执行了三百多次翻译，并翻译成十四种语言——一篇在 `--news` 模式下内容密集的博客文章、采用标准 Markdown 的本 README，以及从 GitHub 原样获取的四个知名项目 README。表格区分了过去容易混淆的两件事：翻译是否**成功完成**，以及其**结构是否与源文件一致**。在两份内容密集的文档上，有三个模型从未丢失任何信息：`gemini-3.7-flash`、通过 ChatGPT 订阅使用的 `gpt-5.6-sol`，以及通过 OpenRouter 使用的 `z-ai/glm-5.2`——它们仅在一两种语言中漏掉了一对 `**`。核心结论是：**决定性因素是文档密度，而不是 `--news` 模式**。通过订阅使用的 Grok 在博客文章上十四次有十三次失败，但在十六份公开 README 中成功完成了十四份；原因经反向验证，是处理长分段时出现偏离。该表格也附有自身的警告：它并不详尽，有明确的时效性，耗时不能作为排名依据，正确做法仍是在自己的文档上进行测量。

  - **结构比较器在发布数据前得到修正，因为它对非拉丁文字产生了两种误报。** URL 后若紧跟全角右括号 `）`，以 `)` 为终止条件的 regex 不会正确截断，因此即使 URL 相同，提取出的字符串也会不同；一段法语中占五行、中文中仅占三行的引用也会使按行计数出现下降。两项修正均通过反向验证：删除 URL、章节或内联代码仍然能够被检测到。若没有这些修正，Gemini 和 Codex 的公布结果会分别是十四种语言中十一种和十二种，而不是十三种和十二种。

  - **测试**：新增文件 `tests/test_openrouter_provider.py`（39 项测试）——模型验证与拒绝父级路径段、托管商固定路由（上限、状态、未声明上限、公共最低值）、`allow_fallbacks` 始终为 false、根据 `mandatory` 关闭或保留推理、完整输出契约（状态码 200 中的错误、没有 choice、区分空白页面与截断、异常的 `finish_reason`、空内容）、目录无法访问时预检采用 fail-closed、slug 缺失及无健康托管商、flag 互斥性以及文件名标签。完整测试套件现有 **427 项测试**。

- **1.12.0** Provider `--use_opencode`：通过开源 agent OpenCode 连接用户选择的供应商——本地模型、无需账户的免费模型、订阅或密钥（2026-09-04）：

  - **第八条 Provider 路径，其性质与前七条不同。** [OpenCode](https://opencode.ai)（MIT）不是模型供应商，而是一个通往用户在 OpenCode 中自行配置的供应商的_路由器_：API 密钥、订阅（GitHub Copilot、ChatGPT、SuperGrok）、提供**无需账户**的免费模型的 OpenCode Zen 网关，或**本地**模型（Ollama、LM Studio、llama.cpp）。脚本以非交互模式驱动 `opencode run`，方式与驱动 Codex 和 Grok 相同，并复用同一套子进程基础设施（独立进程组、超时时先执行 `SIGTERM` 再执行 `SIGKILL`、始终关闭 stdin、清理环境变量）。已通过**两次真实翻译**验证：其一是通过 `opencode/mimo-v2.5-free` 将整个 README 翻译成英语——耗时 49 秒，仅执行一轮，结构与源文件完全一致（32 个标题、26 个代码块闭合标记、18 个链接、37 个 URL、37 行表格、135 处内联代码）；其二是通过本地 `ollama/qwen2.5:7b` 翻译测试文件，完全无需密钥。

  - **`--model provider/modèle` 为必填项，而且这是一个明确选择。** 如果没有 `--model`，OpenCode 会回退到自身的默认值；在全新安装中，该默认值为 `opencode/big-pickle`，这是一个免费的“stealth”模型，其交互内容可能被用于训练——实测响应请求的正是该模型。代替用户静默做出这一选择，恰恰属于本仓库要追踪的隐形切换；因此错误消息会列出用于查看模型的命令（`opencode models`）和三个示例（本地、免费、订阅）。`--eco` 不会生效，并会明确说明这一点。只有在明确请求时，`--reasoning_effort` 才会原样作为 OpenCode 的 `--variant` 传入。

  - **隔离来自实测，而非假设。** 一份内联配置（`OPENCODE_CONFIG_CONTENT`，在 OpenCode 的合并顺序中位于最后，因此优先于用户配置但不会替换它）定义了一个 `aipmt` agent，并拒绝其使用所有工具（`permission: {"*": "deny"}`）：注册表甚至不再向模型提供这些工具；当要求它“列出文件并运行 `id`”时，它会回答自己没有工具。会话共享被禁用，外部插件被排除（`--pure`），且绝不使用 `--auto`；工作目录为空且用后即弃。两种静默注入也经过测量并被阻止：若没有 `OPENCODE_DISABLE_CLAUDE_CODE`，用户的 `~/.claude/CLAUDE.md` 会进入**每一个** prompt（简单输入一句“你好”时，输入量会从 186 tokens 增至 515 tokens）；若没有 `OPENCODE_DISABLE_PROJECT_CONFIG`，当前目录的 `AGENTS.md` 也会被注入——一条“每次回答都以 BANANA 结尾”的指令确实被应用到了翻译中。不过，全局 `~/.config/opencode/AGENTS.md` 仍会被注入：没有开关可以将其排除，而通过挪用 `XDG_CONFIG_HOME` 来绕过它，也会同时隐藏用户的供应商。因此选择记录这一限制，而不是拼凑变通方案。

  - **`exit 0` 不能证明任何事情；这是第三个 CLI，仍需遵循同样的防护思路——同时还有两个自身特有的陷阱。** 未知的 `--agent` 不会让 `opencode run` 失败：它只会在 stderr 上发出警告，然后**静默**回退到工具仍处于启用状态的编码 agent。如果内联配置未生效，翻译便会由一个能够写入文件的 agent 执行；因此，输出契约不仅要求不存在该消息，还会检查：返回码为 0、没有 `error` 事件、没有 `tool_use`、最后一个 `step_finish` 处于 `stop` 状态（`length` 表示响应被截断），且文本非空。第二个陷阱是 JSON 错误事件本身**不透明**——仅显示“Unexpected server error. Check server logs for details.”和一个简单引用——真正的原因（`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`、`ProviderAuthError` 等）只存在于日志中。因此需要 `--print-logs --log-level ERROR`，并从 stderr 读取 `error="…"` 字段，同时排除其后的 Bun 堆栈。这样，未知模型会在一秒内失败，并明确指出原因。`--title` 还顺带避免了一次额外的 LLM 调用：如果没有它，OpenCode 会额外在 `small_model` 上调用一轮来生成会话标题。

  - **密钥：采用与 Codex 和 Grok 相同的模式过滤，但有一个按名称指定的例外。** `OPENCODE_API_KEY` 会被保留：这是 OpenCode 自身的密钥（用于 Zen 网关和 Go 订阅），名称明确指向 OpenCode——它相当于 OpenCode 的 `auth.json`，既不是 aipmt 管理的密钥，也不可能由 aipmt 计费。供应商在 OpenCode 中配置（`opencode auth login`、`opencode.json`），而从不在 aipmt 的 `.env` 中配置；后者的任何密钥都不会进入子进程。与订阅型 CLI 不同，CI 中不会拒绝运行：在 runner 上使用 API 密钥或自托管模型都是合理用法。

  - **防路径遍历保护现在检查插值后的值，而不是原始值。** `provider/modèle` 包含一个 `/`，而 1.10.0 的保护会拒绝它——这一拒绝原本有充分理由，因为 `--model` 会被插入文件名 `--include_model`。现在，文件名标签会在执行任何插值前，将 `/`、`\` 和 `:` 替换为 `-`（`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`，因为 `:` 在 Windows 下非法），上游保护检查的也是这一标签：`../../evil` 会在目标目录下变为普通名称 `doc-en-..-..-evil.md`，只有 `..` 仍会被拒绝，`--target_lang ../x` 同样会被拒绝。`_ensure_within_directory` 范围保护仍作为第二层防线，保持不变。

  - **免费模型和本地模型，以及相关实测结果。** `opencode/mimo-v2.5-free` 翻译一个段落耗时 16 秒，翻译本 README 耗时 49 秒；`opencode/big-pickle` 翻译 200 个词耗时 40 秒，但两项并发请求持续 5 分钟仍无响应，而单独执行时均能完成；`opencode/nemotron-3.5-lightning-free` 在 3 分钟内没有返回任何内容。因此，`REGEN_PROVIDER=opencode` 要求必须使用 `REGEN_MODEL`，并行任务数为 **2 jobs**。在本地方面，Ollama 通常配置 4 096 tokens 的上下文，而分段最长可达 16 000 个字符：因此必须使用带 `PARAMETER num_ctx 32768` 的 `Modelfile`；质量则取决于模型——一个 7B 模型在测试文件中颠倒了一份列表，并破坏了代码块闭合标记，而网关模型则完整保留了所有内容。

  - **本仓库的翻译不再通过任何按量收费的 API。** 只要 `.env` 中存在密钥，`regen_translations.sh` 就会使用 OpenAI API，而 Codex 仅作为主动选择项。准备此版本时，实际发生的正是这种情况：28 份翻译都通过 OpenAI API 完成，随后印地语 CHANGELOG 又通过 Gemini API 完成，尽管 ChatGPT 订阅存在的目的正是避免按量付费。现已移除密钥自动检测：**默认使用 Codex，并采用 `gpt-5.6-sol`**，即质量模型；`openai`、`gemini` 和 `grok` 除了 `REGEN_PROVIDER` 外还要求提供 `REGEN_ALLOW_PAID_API=1`，这是一项明确命名的例外许可，确保规则在做出决定时真正生效；未知的 `REGEN_PROVIDER` 会直接失败，而不会回退到 API。十项测试固定了默认行为、拒绝逻辑和例外许可。本版本的 28 份翻译已全部通过 Codex 重新完成。

  - **rate limit 的 back-off 逻辑现已抽取为共用实现**（`_retry_on_rate_limit`）：Codex 和 Grok 的循环除标签外完全相同，如果再复制第三份，就会超过重复代码阈值。三个 CLI 错误均继承自同一个 `_CliCallError`；另有一项测试禁止其中任何一个脱离该继承体系，否则共享循环将无法再捕获它。
  - **测试**：新增文件 `tests/test_opencode_provider.py`（51 项测试）——完整输出契约、agent 回退、从日志读取原因、去重文本部分并忽略合成部分、超时终止进程组、针对 429 的退避机制、模型必填且经过验证、无密钥预检、二进制文件解析、dispatch 接线、文件名标签以及路径遍历反例测试。`tests/test_review_hardening.py` 将 flag 互斥性与无密钥要求扩展至新 provider。gate 现在要求记录 **22 个 flags** argparse。完整测试套件共 **382 项测试**。

- **1.11.1** 文档修复：README 终于列出了七条 provider 路径（2026-09-03）：

  - **1.11.0 的 PyPI 页面写的是“4 个 API + Codex CLI”。**代码实际提供七种方式——通过 API 使用 OpenAI、Mistral、Claude、Gemini 和 Grok；通过订阅使用 Codex（ChatGPT）和 Grok，不按用量计费。简介和 _Multi-Provider_ 条目中遗漏了两种 Grok 模式，14 个译本也重复了这一错误。由于软件包的长描述会按版本固定，要修正展示页面就必须发布新版本号：这正是此版本存在的唯一原因。**无代码变更。**
  - `CLAUDE.md` 已与发布所引入的内容保持一致：gate 计数器（16，`--full` 中为 17）、十一个活跃 workflow、`gh pr checks` 中不可见的两个 Sonar/Codacy 计数器（hotspots、Codacy API）、通过 `ruff-format` 移动一个 `# nosemgrep`、OIDC 交换所要求的 GitHub 环境，以及 _pending publisher_ 不会保留名称这一事实。

- **1.11.0** 发布至 PyPI：依次运行 `pip install ai-powered-markdown-translator` 和命令 `aipmt`，无需克隆仓库（2026-09-03）：

  - **单文件脚本变为可安装软件包。**`translate.py` 从根目录移至 `src/aipmt/translate.py`，并提供 console 入口点 `aipmt` 及其等效形式 `python -m aipmt`。参与贡献仍需克隆仓库——测试、28 个译本和质量工具都位于其中——但仅使用工具不再需要。

    - **import 名称为 `aipmt`，绝不能是 `translate`**，因为命名冲突确实存在且不会发出提示。PyPI 软件包 `translate`（v3.8.1，最后上传于 2026-07-06）会安装一个同名目录。在 venv 中复现：目录优先于模块，`translate.main` 消失，入口点在 `AttributeError` 处中断——而 `pip check` 返回“No broken requirements found”，rc=0。用户只需执行一次 `pip install translate`，就足以让 CLI 在没有可用诊断信息的情况下损坏。使用真实 wheel 进行反例验证：将 `pip install translate` 安装到该软件包之上，`aipmt --help` 在安装前后均为 rc=0，两套 CLI 可以共存。
    - **长 distribution 名称，短命令。**`ai-powered-markdown-translator` 使该软件包能够通过 PyPI 搜索找到；只使用缩写会让不了解项目的人无法发现它，而此次发布的目的正是让项目可被发现。经核查排除了两个看似合理的候选名称：`ai-markdown-translator` 自 2024 年起已被 npm 上一个用途相同的工具占用，比本仓库早 17 个月；而 `aimt` 与 `aim`（v3.29.1）仅差一个字母，后者还是同一领域的活跃软件包——这是最容易造成长期混淆的情况。另有一个方法陷阱：`pypi.org/project/<nom>/` 对任何名称都返回 200（反机器人页面），只有 JSON API 的结果可信。
    - **采用 `src/` layout，而不是扁平软件包。**扁平软件包本可保留测试中的六个 `sys.path.insert(..., "..")`，但这恰恰是缺陷所在：它们会 import 源码树而非软件包，从而掩盖任何打包错误。实际代价仅是增加一条替换规则。

  - **密钥终于可以一次配置、长期使用。**此前，已安装的 CLI 没有任何持久配置：只能使用环境变量和当前目录中的 `.env`。`find_dotenv` 确实会一路向上查找到系统根目录，因此**在个人目录下工作时**能够找到 `~/.env`，但在其他位置工作时则无法找到——这种覆盖范围取决于从哪里启动命令，而非设计选择。因此在现有两层配置之下增加第三层：`~/.config/aipmt/.env`。

    - **优先级并非硬编码**，而是由 `override=False` 推导得出，它是 `load_dotenv` 的默认值：每一层只填补上一层留下的空缺。因此顺序为环境变量 → 项目的 `.env` → 用户配置；这由行为测试而非结构测试验证——交换两个调用的顺序会导致测试失败，移除第三层也会失败。
    - **使用 `.env` 格式而非 TOML**，这是有意为之：`python-dotenv` 已经是依赖项，其语法已经记录在 15 份 README 中，而且同一个文件可用于两种作用域。无需引入新依赖或新语法。若 `XDG_CONFIG_HOME` 为**绝对路径**，配置位置将遵循它——规范要求忽略相对值，否则配置位置会再次取决于当前目录——Windows 下则使用 `APPDATA`。
    - **排除了两个选项，并给出了理由。**系统密钥环（`keyring`）在桌面设备上更安全，但会在 headless 环境中失败——服务器、容器、CI——而这恰恰是批量翻译的使用场景；它适合作为 opt-in 选项，却不适合作为默认值。`--api-key` flag 会让密钥进入 shell 历史记录，并在 `ps` 中可见。
    - **缺少密钥时不再显示调用栈。**此前用户会收到指向 `site-packages` 的 Python 堆栈，以及一条仅提到“环境或 .env”、却不说明应在哪里创建后者的消息。现在会列出三个位置及其确切路径，命令以状态码 2 退出。该保护措施被**刻意限定在很窄的范围内**：仅在配置阶段对 `except ValueError` 进行处理。若包裹整个执行过程，翻译期间出现的真实 bug 就会被转化为令人安心的消息——而这正是本仓库要追踪的故障模式。有一项测试会读取 `main()` 的源代码，以禁止这种做法。

  - **修复——工具安装后，用户的 `.env` 会被忽略。**不带参数的 `load_dotenv()` 不会从当前目录向上查找，而是从调用方文件开始，因此会从 `site-packages` 开始查找。通过从一个拥有自身 `.env` 的项目中启动真实 console 入口点进行测量：`find_dotenv()` 返回 `''`，密钥未被加载，而 `find_dotenv(usecwd=True)` 可以找到它。只要工具始终从克隆的仓库中运行，这个 bug 就不会出现；发布后它将成为系统性问题，唯一症状是在配置正确的情况下报告 API 密钥“缺失”。

  - **三个 gate 即使停止验证任何内容，也会显示绿色。**它们被有意安排在迁移**之前**加固：在变更之后才编写本应捕获该变更的保护措施，无法证明任何事情。每个 gate 在原始仓库上均为绿色，在迁移后的副本上均转为红色——两个方向都已测量。

    - **Lizard 会悄无声息地忽略不存在的路径**：rc=0，“0 file analyzed”。复杂度 gate 会从 158 个函数 / 2247 nloc 变为 3 个函数 / 34 nloc，并产生零字节输出。现在 scope 是一个数组，其中每个条目都会验证是否存在。
    - **对不存在的模块运行 `coverage run --source=` 不会失败**：仅在 stderr 发出警告，无论 unittest 还是 `coverage xml`，rc 都为 0，而且仍会发布报告——statements 从 1453 缩减至 141。项目看起来会很健康，只因几乎不再接受分析。报告现在由两个下限保护：总量，以及测得的最大文件。
    - **译本新鲜度探针在结构上无法感知调用形式**：它以 argparse flags 为锚点，而文件重命名恰好不会改变这些 flags。复现结果：模块已移动，15 份 README 仍记录一条不存在的命令，判定却是“没有过时译本”。因此新增第 7 个章节，用于验证调用**形式**而非选项；Lizard hook 也会与脚本的实际 scope 对照——当其键 `files:` 不再匹配时，不会让 pre-commit 失败，而是直接**跳过**。

  - **`requires-python = ">=3.10"` 不再只是一项声明。**`sonar-project.properties` 早已宣称支持 3.10–3.12，但从未实际运行过这些版本，开发机器上只有 3.12——这项内部矛盾会因发布而公开。现在测试 workflow 会在 3.10、3.11 和 3.12 上执行测试套件，并安装**软件包**，从而验证其公开版本边界。

  - **设置最低版本，不设上限。**`requirements.txt` 仍是经过测试的 lock，`[project.dependencies]` 则成为公开契约：若发布 lock 中的精确版本，会与所有同时使用其他软件包的用户产生冲突。也不设置 `<N+1` 上限——那会与 `check-deps-fresh.sh` 直接矛盾，后者会让 release gate 因任何主版本滞后而失败。这组最低版本可以成功解析，而反例 `openai==1.0.0` 的输出为 `ResolutionImpossible`，证明该检查具有判别能力，并非无条件接受所有情况。另有一项保护措施禁止 `pyproject.toml` 的版本与 CHANGELOG 中的版本不一致：PyPI 不允许重复使用版本号。

  - **已在全新 venv 中进行端到端验证**：约 70 Ko 的 wheel 仅包含 `aipmt/*.py`、dist-info 和许可证；`aipmt --help` 以 rc=0 结束并显示 22 个 flags；`python -m aipmt` 显示“usage: aipmt”而非“usage: \_\_main\_\_.py”；`pipx` 安装可用；最重要的是，**从任意用户目录完成了一次真实的 fr→en 翻译**，粗体、列表、inline code、链接和 URL 均得到保留，代码块未被翻译。迁移前的 318 项测试全部通过，且迁移前后的标识符列表逐字节完全一致——真正证明没有测试被停用的是这一点，而非“OK”；此外还为三层配置增加了十二项测试，总计 330 项。

- **1.10.0** Provider `--use_codex`（ChatGPT 订阅配额）、更新 SDK 和模型、修复多段落 news 引用（2026-08-29）：

  - **安全审查——PR 设置了两项保护措施，但并未在所有地方落实**：

    - **Codex 预检将整个 `.env` 传给了二进制文件。**`_codex_preflight` 调用 `subprocess.run` 时**没有使用 `env=`**：子进程继承完整的 `os.environ`，也就是 `load_dotenv` 加载的整个 `.env`。使用带检测功能的伪二进制文件测得：**七项密钥**进入了预检——六个 provider 的密钥加上一个 `GITHUB_TOKEN`——相比之下，对应的 `_grok_preflight` 正确传入了 `env=_grok_env()`，因此是**零项**。这是 PR 内部的不一致：就在几行之外，`_strip_secret_env` 的存在正是为了维持这一不变量。现在提取出一个 `_codex_env_base()` 供两条路径共享；修复后测量结果：两边均为 0 项密钥。
    - **“`--deny` fail-closed”属性并未覆盖实际使用的形式。**注释将整个 Grok 隔离设计的依据归结为：包含未知前缀的规则会导致启动被拒绝。在 `grok 1.0.13` 上测得，这项验证**仅适用于带括号的形式**：`--deny 'CeciNestPasUnOutil(*)'` 拒绝启动（“unknown tool prefix”），而 `--deny 'CeciNestPasUnOutil'` 会被静默接受。但 `GROK_DENY_RULES` 只使用裸名称——如果 xAI 侧重命名工具，那么在操作系统 sandbox 已不适用的机器上，唯一经过测量的隔离层就会在毫无提示的情况下失效。八条命名规则改用 `Prefix(*)`，每一条都经 CLI 验证为已知前缀；catch-all `*` 保持原来的字面形式，这是唯一可接受的形式。一项测试会阻止恢复为未经验证的形式。
    - **其他方面已验证无问题**：不存在命令注入（始终使用列表形式，从不使用 `shell=True`，文档内容通过 stdin 或 `--prompt-file` 传入），不存在不安全反序列化（仅使用 `json.loads`，并带有类型保护），路径遍历修复在七种 payload 上均未发现绕过方式，而且 CLI 确实应用了 `--deny '*'`（读取 workdir 外内容时观察到 `DENY_ENFORCED`）。
    - 此外，上文新增的新鲜度检查也绕过了自身原则：若某个软件包的 PyPI 请求失败，就会被静默跳过，gate 仍显示绿色。现在它会统计实际比较的软件包数量，并在覆盖不完整时失败。

  - **依赖已更新，并增加两道保护，避免再次长期滞后**：

    - **滞后确实存在且持续已久**：`openai` 2.54 → **3.6.0**，`anthropic` 0.125 → **1.2.0**，`certifi` 2024.8.30 → **2026.7.22**——也就是说，为所有 provider 调用验证 TLS 的根证书存储落后了两年。原因已经确认：**此前不存在 `.github/dependabot.yml`**。没有该文件，GitHub 只会启用 _security updates_，Dependabot 仅会针对受 CVE 影响的依赖提出 PR——这解释了为什么它更新了 `urllib3` 和 `idna`，却任由两个 SDK 落后一个主版本。
    - **两个主版本可以共存且不会冲突**，这与此前担忧的推断相反：`openai` 3.x 和 `anthropic` 1.x 迁移至 **`httpx2`**，而 `mistralai` 和 `google-genai` 仍使用 `httpx<1`，但它们是两个不同的 distribution。已通过真实安装验证，并进一步对 **7 条 provider 路径进行了端到端测试**——OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI 和 Grok CLI——每项输出中的 inline code 与链接均得到保留。“避免使用两套 HTTP stack”只是偏好，并非阻碍：测量结果已经作出裁决。
    - **`requirements.txt` 并未描述真实环境**：`google-auth`、`cryptography` 和 `opentelemetry` stack 已安装在工作 venv 中，却从未声明——因此全新安装无法复现测试环境。相反，`tokenizers`、`huggingface-hub` 和 `PyYAML` 被列在其中，却未被任何内容 import 或要求，它们是 `mistralai` 1.x 的残留项。现在该文件会被重新生成为一个仅从直接依赖构建的 venv 的完整闭包。`pip-audit` 未在新依赖集中发现任何已知漏洞。
    - **`.github/dependabot.yml`**（新增）启用 pip 和 github-actions 的每周版本更新。次版本与补丁版本合并到一个 PR 中——每次补丁升级都创建一个 PR，最终只会被忽略，而噪声正是更新的敌人；**主版本分别处理**，每个主版本都要求通过真实调用验证。
    - **`scripts/check-deps-fresh.sh`**（新增，已接入 gate）让项目判定能够显示依赖滞后：Dependabot 只会提出建议，无法提供保证，其 PR 也可能不断堆积。主版本滞后 → 失败；次版本滞后 → 警告，因为一个长期保持红色的 gate 最终会被忽略；PyPI 无法访问 → 本地明确 skip，**CI 中 fail-closed**，因为未执行的检查不等于成功。已在两个方向进行验证：它能够捕获修复前的确切状态（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`），而对次版本滞后只发出警告。

  - **本次 PR 审查产生的修复**——五个审查 agent 全面检查了 diff；以下各项在修复前都已**通过测量复现**，其中两项是同一版本前文引入的回归。
    - **已修复回归问题——`_NEWS_CITATION_REGEX` 存在指数级回溯。** 多段落修复在重复中引入了 `(?:[ \t]*$|[ \t]+.*)`：`[ \t]+` 与 `.*` 之间的空格分配存在歧义，而且这种歧义会随迭代不断倍增。在不匹配该模式的 `>   texte` 行——完全合法的 Markdown 缩进——上测得：**14 行耗时 2 589 ms**，修复后为 0.04 ms；每增加一行，耗时约放大 9 倍。在 `--news` 模式下，一段很长且不符合要求的 blockquote 就足以让翻译冻结，直至任务超时，而且无法确定原因。现在，每次重复都会一次性消费整行（`\n^>(?![ \t]*—).*`），因此每轮迭代只剩一种匹配方式。已在包含 231 篇文章的真实语料库上验证：捕获结果**零差异**，仍为 423 条引文，14 个多段落正文也仍然全部得到扩展。
    - **同时使用两个 provider flag 会在没有任何提示的情况下按用量计费。** `--use_codex --use_mistral` 会被接受；`_select_provider_client` 首先测试 Mistral，而 `_resolve_provider` 优先处理显式布尔值——两者最终都会选择 Mistral。因此，用户本想使用订阅额度，实际却被按用量收费，而且没有收到任何警告：这恰恰是 `--use_codex` 要防止的故障模式。现在，六个 provider flag 都通过一个 `add_mutually_exclusive_group` 处理。**行为变更**：过去会被静默接受的、同时组合两个 provider 的命令行现在会在 `argument --use_mistral: not allowed with argument --use_codex` 上失败。
    - **工作结束 gate 会在探针崩溃时错误变绿。** `scripts/check-release-ready.sh` 的十三项检查中有四项采用“捕获 stdout，若为空便下结论”的模式，却从不检查返回码：异常（文件被重命名、`FileNotFoundError`）会写入 stderr，使 stdout 保持为空，而检查则得出“一切正常”的结论。用于防止“一个 `exit 0` 什么也证明不了”这一陷阱的脚本，内部竟然重现了同一个陷阱。现在，helper `probe()` 会同时要求返回码为零**且**存在结束哨兵；当标记集合为空时，探针也会拒绝下结论——因为对空集合的断言永远为真。示例：加入上述互斥组后，provider flag 改为经由 `*_group` 对象传递，旧 regex `parser\.add_argument\(` 不再能够匹配；**二十一个 flag 中有六个**静默脱离检查范围，但 gate 仍然显示为绿色。
    - **secret 扫描遗漏了六个 provider 中的四个。** 字符类 `[A-Za-z0-9]` 排除了连字符：`sk-proj-…`（当前 OpenAI 格式）和 `sk-ant-api03-…` 都会在第二个连字符处中断，而 `AIza…` 完全没有被覆盖。现已扩展模式，并将 `.secrets.baseline` 排除在扫描之外。此外，防护 `.env` 查询的是 `git diff --cached`，它只能看到索引：一个**已经提交**的 `.env`——最糟糕的情况——永远不会出现在其中。现在它改为查询 `git ls-files`。
    - **Codex 的“token warm-up”其实并没有预热。** 实测显示：`codex login status` 不会触碰 `~/.codex/auth.json`（mtime 和大小均未改变），其帮助文本写的是“显示登录状态”。但注释却声称它会“依次执行一次”token 刷新，从而消除一次性轮换 token 并发刷新的风险。所宣称的保护实际上并不存在；现在注释会如实说明代码的行为，真正的应对措施仍然是 `max_jobs=4`。该检查现在还会遵循此前被忽略的 `CODEX_BIN`——在 `PATH` 中没有 `codex` 的工作站上，过去会因“未认证”而失败，给出误导性的诊断。
    - **`.env` 是在子 shell 中 source 的。** `detect_provider` 通过命令替换调用，因此其 export 无法传回父 shell：在 `.env` 中定义的 `GROK_BIN`、`GROK_HOME` 或 `REGEN_MODEL`，对 `main()` 中的读取操作仍然不可见，导致配置正确时也会得出“找不到 Grok 二进制文件”的结论。
    - **并发量比宣称的上限高出 50%。** 防护被放在 README/CHANGELOG 任务对启动之后：实测 `max_jobs=2` 的峰值为 **3**。Grok 的每周额度与 Chat/Imagine/Voice 共享且无法测量，因此脚本为自身设定的上限并未得到遵守。最终计数虽然会显示，却从不与 28 比较——缺失文件也不会被发现。
    - **Grok 输出契约：缺少 `stopReason` 现在会被视为失败。** 代码使用的是“`end_turn` **或缺失**”，而宣称的契约要求必须存在 `end_turn`。如果 payload 没有该字段——或 CLI 更新后重命名了该字段——防护就会静默变成 no-op。此外，`max_turn_requests` 不再归类为 rate limit（这是轮次预算耗尽：重试只会在额外等待 90 秒后得到同样结果），`quota` 也从 rate limit 标记中移除——原因正是 `_codex_is_rate_limited` 的 docstring 早已说明、但 Grok 此前没有执行的那一点。
    - **Gemini 级联现在按模型进行记忆化。** 它过去会在每个 segment 上都从 `minimal` 重新开始，而默认模型会拒绝该值：正常路径因此每个 segment 都要付出一次 400 往返，并重复打印同一条警告。一条重复数百次的 warning 最终不会再有人阅读——它就这样变成了遮蔽物。
    - **其他事项**：CI 中的拒绝消息被硬编码为 Codex，导致 `--use_grok_cli` 用户被引向 `OPENAI_API_KEY`，而不是 `XAI_API_KEY`；`provider.capitalize()` 显示为“Grok_cli”和“Openai”；子进程基础层的注释将“shim”泛化到了两个 CLI，但 Grok 二进制文件是原生 ELF（正确理由是“会生成自身子进程的 agent”）；`subprocess` 上的十二项 SAST finding 已标记为 `# nosec` / `# nosemgrep` 并附带理由，不含 `shell=True` 的列表形式使注入无法发生，文档内容也从不经由 argv 传递。
    - **任何 secret 都不再进入 agent 子进程。** 按名称维护的 deny-list 只保护了**计费**不变量（Codex 不含 `OPENAI_API_KEY`，Grok 不含 `XAI_API_KEY`）。实测显示：**另外七个 secret** 仍会进入每个子进程——Anthropic、Mistral、Google 和 Gemini 的 key、另一个 CLI 的 key，以及并非 secret、但会重定向流量的 `OPENAI_BASE_URL`。然而，这两个 CLI 都是 **agent**，而且 Grok agent 在许多 Linux 工作站上运行时没有可用的 OS sandbox。现在改为按**名称模式**（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`）过滤，而非使用名称列表；因此，即使用户在 `.env` 中添加了本代码并不认识的变量，也同样能够覆盖。这些变量都不是 CLI 所必需的：认证信息位于 `~/.codex` 和 `~/.grok` 中，从不存放在环境中——已通过在强化环境下分别使用两个 provider **实际完成翻译**进行验证。
    - **测试**：新增文件 `tests/test_review_hardening.py`（21 项测试），锁定 provider flag 的互斥性、`stopReason` 契约、news regex 的线性复杂度、CI 中的拒绝消息、Gemini 记忆化，以及子进程环境中不存在任何 secret。最后一项断言是**通用的**——它会因任何未被列表点名的 key 而失败——相比之下，现有的清除测试只是其常量的镜像，除了自身循环失效之外无法检测任何其他问题。完整测试套件现为 **311 项测试**。

  - **两个新的 Grok provider**：`--use_grok`（xAI API，key 为 `XAI_API_KEY`，按用量计费）和 `--use_grok_cli`（官方 Grok Build CLI，从 Grok 订阅额度中扣除——原理与 `--use_codex` 相同）。
    - **API 模式，约 40 行**：由于 xAI endpoint 与 OpenAI 兼容，client 和 `_call_openai` 均可原样复用，只有 `base_url` 会改变。唯一需要的适配也惠及所有 provider：`finish_reason` 现在接受 `end_turn`，这是 xAI 输出的形式，而 OpenAI 输出的是 `stop`。模型：`grok-4.6`（质量）和 `grok-4.3`（经济）。需要注意的是，Grok 的经济模型仍是仓库中最昂贵的——每百万 token 为 $1.25/$2.50，而 `mistral-small-latest` 为 $0.15/$0.60：选择这个 provider 是为了模型多样性，而不是价格。
    - **CLI 模式**：以 Codex 为蓝本，但有四项由实际情况决定的差异——prompt 通过文件传入（`--prompt-file`；CLI 不读取 stdin，而放入 argv 的 segment 会在 `ps` 中可见）、输出是 stdout 上的单个 JSON 对象（既不是 JSONL，也不是 `-o` 文件）、订阅只提供 `grok-4.6` 和 `grok-4.5`，并且无法应用 sandbox（见下文）。子进程启动逻辑与 Codex 一起提取到 `_codex_run_process` 中，未触及已经过测试的 Codex provider 其余部分。
    - **实测证明 `exit 0` 什么也证明不了**：未认证时，CLI 会将 `{"type":"error","message":"Not signed in."}` 写入 **stdout**，返回码却是 **0**。拒绝请求或轮次超限时也有相同行为。因此，输出契约要求同时满足四个条件：返回码为 0、没有错误 payload、存在 `stopReason == end_turn`，且文本非空。preflight 遵循相同逻辑：即使已断开连接，`grok models` 仍以 0 退出，只有 stdout 中出现“未认证”才能据此下结论。
    - **隔离：有意接受并记录的不对称性。** Codex 在 `--sandbox read-only` 中运行，而 Grok sandbox 在许多较新的 Linux 工作站上无法应用，原因是两个相互独立、且没有 `sudo` 就无法规避的系统限制：从 Ubuntu 24.04 起，AppArmor 会阻止非特权 user namespace（`bwrap: setting up uid map: Permission denied`，已在 Grok 之外复现）；当 `/run/podman` 位于 `0700` 中时，容器 runtime socket 的 deny-list 会失败（resolver 只捕获 `ErrorKind::NotFound`，EACCES 会成为致命错误）。核心陷阱是：无法应用的**内置**配置文件会**静默地以非隔离模式启动**。因此，脚本默认不会请求任何配置文件，也绝不会静默回退——它会在 stderr 上发出警告。保护依赖 CLI 的 `--deny` 规则，其中包括 catch-all `*`；这是唯一经实测为 _fail-closed_ 的层（带有未知前缀的规则会导致启动被拒绝）。`GROK_TRANSLATE_SANDBOX=read-only` 可用于强制要求 sandbox，此时若机器无法满足要求，启动就会失败。
    - **防护措施**：从子进程环境中移除 `XAI_API_KEY`、`GROK_API_KEY` 和 `GROK_SANDBOX`（key 会切换为按用量计费；继承的 `GROK_SANDBOX` 会强制应用不可用的配置文件，并给出误导性消息），禁用 MCP/hooks/skills/agents 开关，使用 `--disable-web-search`、`--no-subagents`、`--no-plan`、一次性 workdir、CI 拒绝机制、会终止 process group 的 timeout，以及针对 rate limit 的 back-off。`--max-turns` 被设为 6 而不是 1：计数器会在工具轮次之后递增，设为 1 会截断输出。
    - **额度**：Grok 额度池按周计算，并且**与 Chat、Imagine 和 Voice 共享**，也没有任何命令可以查询——这与 Codex 不同，后者可通过 `account/rateLimits/read` 量化消耗。因此，`regen_translations.sh` 将并发限制为 2，并明确发出警告。
    - **测试**：新增文件 `tests/test_grok_provider.py`（24 项测试）。完整测试套件现为 **290 项测试**。
  - **已修复 bug——多段落英文引文仅得到部分保护（`--news` 模式）**：`_NEWS_CITATION_REGEX` 只接受一系列**连续的** `>` 行作为引文正文。一旦引文跨越多个段落（由一个空 `>` 行分隔），就只会捕获最后一个段落并将其替换为 placeholder；前面的段落会被发送给 LLM 并在返回时被翻译——这与 `--news` 应当保证的行为完全相反。现在，重复可以接受内部的空 `>` 行，并改为非贪婪模式，以便在斜体行之前的空 `>` 处停止，而不是在遇到的第一个空行处停止。
    - **实测范围**：在包含 198 篇文章的真实语料库中，419 条引文里有 11 条受到影响。没有回归——新 regex 捕获的引文数量完全相同，只有多段落正文得到扩展（408 个正文相同，11 个得到扩展），归属行 `> — …` 仍然不可能被吸收到正文中（保留了 lookahead）。
    - **端到端证明**：在一篇 69 ko 的文章上进行 ja/ar 翻译时，一条引文的第一段过去会在日语中被译为 `> GLM-5.3がオープンウェイト化。`，在阿拉伯语中也同样被翻译；现在它会保持为 `> GLM-5.3 is now open-weight.`。英文引文行数从 9 恢复为 10，与源文一致。
    - 值得注意的是，下游 validator 未能检测到这个缺陷，因为它们只检查引文是否存在，而不检查引文是否完整。
  - **默认 provider 上经实测的成本节省**：只要模型名称以 `gpt-5` 开头，`_openai_extra_kwargs` 就会发送 `reasoning_effort="medium"`，即使在 `--eco` 中也是如此。在 `gpt-5.4-mini` 上翻译一个十词句子的测量结果：`medium` → 45 个 reasoning token 和 65 个输出 token；`none` → 0 和 14。reasoning 对翻译没有帮助，却会在每个文件的每个 segment 上产生费用。现在，`--eco` 中的默认值改为 `none`，其他情况下仍为 `medium`；通过 CLI 显式传入的值仍然优先。除 `low`/`medium`/`high` 外，`--reasoning_effort` 现在还接受 `none` 和 `xhigh`（并非所有模型都接受全部取值：例如 `gpt-5.4-mini` 会拒绝 `minimal`——现有的无参数重试机制会覆盖这种情况）。
  - **SDK 更新与 Gemini 迁移**：`google-generativeai`（支持已于 2025-11-30 结束，仓库已归档）被统一 SDK **`google-genai`** 取代——先 `genai.Client(api_key=...)`，再 `client.models.generate_content(model=, contents=, config=)`；system prompt 通过 `system_instruction` 传入，而不是与 segment 拼接。`mistralai` 升级到 **2.9.4**（import 改为 `from mistralai.client import Mistral`；旧写法会抛出 `ImportError`，已在 wheel 中验证），`anthropic` 升级到 **0.125.0**，`openai` 升级到 **2.54.0**——这些都是迁移到 `httpx2` 前的最新版本，以避免 venv 中并存两套 HTTP stack。因此，`httpx` 0.28.1 和 `pydantic` 2.13.5 也得以解除锁定。
  - **两个由真实测试而非文档捕获的回归问题**：
    - `anthropic` ≥ 1.0 会在 client 端拒绝非 streaming 调用，只要其 `max_tokens` 表明调用可能持续超过 10 分钟（`ValueError: Streaming is required...`）。这个保护在 0.34.2 中不存在，导致所有带 `max_tokens=32768` 的 Claude 调用都失败。现已通过显式设置 `timeout`（`CLAUDE_TIMEOUT`，默认 900 s）修复，从而避免为了只使用完整响应的调用切换到 streaming。
    - 只有部分 Gemini 模型接受 `thinking_level="minimal"`：`gemini-3.1-flash-lite` 支持它，而 `gemini-3.7-flash` 和 `gemini-3.1-pro-preview` 会以 400 拒绝。因此新增 `_gemini_generate_with_fallback`：按照已有 OpenAI fallback 的模式，依次尝试 `minimal` → `low` → 不使用 thinking_config——优化参数绝不能导致翻译失败。
  - **默认模型全面更新**，每个模型都已通过真实调用验证：OpenAI `gpt-5.5` → **`gpt-5.6-terra`**（28 个任务的 batch 成本降低 60%），`gpt-5.4-mini` → **`gpt-5.6-luna`**（降低 73%）；Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**（更便宜且更新），`claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（不含日期的规范 ID）；Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**，`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（稳定版本，且比 `3.5-flash-lite` 更便宜）。
 Mistral 保持不变，`mistral-large-latest` 仍是四者中性价比最高的。需要注意的是：不存在比 `gemini-3.1-pro-preview` 更新的 Pro 系列 Gemini 模型——2026 年 5 月公布的 Gemini 3.5 Pro 从未发布；3.5/3.6/3.7 系列仅有 Flash。
  - **切换 Gemini 前进行实测 A/B 测试**：使用 `gemini-3.1-pro-preview`、随后使用 `gemini-3.7-flash` 将 `README.md` 翻译成日语。结构完全相同（21 个列表、18 个代码块、13 个 HTML 链接、13 张图片，所有 URL 均保留），耗时分别为 **8 秒和 48 秒**。由于没有公开 benchmark 比较这两个模型在翻译或非拉丁文字方面的表现，否则此次切换只能基于简单推测。
  - **Claude 响应块过滤**：`_call_claude` 在未过滤类型的情况下执行 `block.text for block in response.content`。采用自适应推理的模型（Sonnet 5 及更高版本）会插入一个 `thinking` 块，该块暴露的是 `.thinking`，而非 `.text`——翻译会在首个分段遇到不透明的 `AttributeError` 时失败。现在会排除 `thinking`、`redacted_thinking`、`tool_use` 和 `tool_result` 块（采用排除列表，以便继续兼容携带文本的未知类型），而完全不含文本块的响应会抛出明确错误。每次调用都会传入 `thinking={"type": "disabled"}`。
  - **重新同步 `MODEL_TOKEN_LIMITS`**：移除退役日期已过的模型（`magistral-*` 系列于 2026-07-31 退役，`gemini-2.0-*` 于 2026-06-01 退役，`gemini-3-pro-preview` 于 2026-03-09 退役，以及 `claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。修正限制：Mistral 128K → **256K**（Large 3 / Small 4 代）、Gemini 1 000 000 → **1 048 576**（实际输入限制）、`claude-opus-4-5` 200K → **1M**、`gpt-5.6-*` 系列 400K → **1.05M**。新增 Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest` 和 `ministral-*` 系列。需要注意的是：这些限制仍仅供参考，因为 `translate()` 会将分段上限设为 `min(16000, limite)`。

  - **Provider `--use_codex`**：第五个 provider，通过非交互模式驱动 Codex 官方 CLI（`codex exec`），而不是调用按用量计费的 API。翻译用量从已付费的 ChatGPT 订阅配额中扣除。这是 OpenAI 针对此用途唯一有文档说明的方式：各方案的可用性矩阵将“Codex SDK、`codex exec` 和可脚本化工作流”列为 Plus/Pro/Business/Enterprise 可用功能，而 `~/.codex/auth.json` 的 token 无法验证对 API Platform 的调用（此脚本也绝不会读取它们——身份验证及其刷新仍由 CLI 管理）。
  - **Codex 二进制文件可通过 pip 安装，不再仅限 npm**：`_resolve_codex_binary()` 依次在 `CODEX_BIN`、`PATH`，以及 OpenAI 发布的官方 Python package **`openai-codex-cli-bin`** 中查找二进制文件（这是 `openai-codex` SDK 的依赖项）。因此，Python 项目使用 `--use_codex` 时不再需要全局安装 npm。该 package 未添加至 `requirements.txt`：二进制文件约为 250 MB，如果添加，所有用户都必须为一个可选 provider 安装它。已完成端到端验证：当 `codex` 不在 `PATH` 中时，解析过程能够找到打包的二进制文件，并在 6 秒内完成完整翻译。
  - **“订阅模式”保证**：从子进程环境中移除 `OPENAI_API_KEY` 和 `CODEX_API_KEY`。如果没有这层保护，`.env` 中存在的密钥可能会让 Codex 在没有任何可见提示的情况下切换到按用量计费——而避免这种情况正是此 provider 存在的意义。
  - **通过测试锁定 CLI 陷阱**：
    - 即使 prompt 已作为参数传入，`codex exec` 仍会读取 stdin：如果不关闭 stdin，命令会一直等待到超时，且永远不会调用模型（已复现：180 秒后以 124 退出，输出为零字节）。因此必须使用 `communicate(input=...)`。
    - 通过 npm 安装的 `codex` 是一个 Node shim，会通过 `spawn` 启动真正的 Rust 二进制文件：后者是 Python process 的**孙进程**，在对 `subprocess.run(timeout=)` 执行 `SIGKILL` 后仍会存活，并继续消耗配额。因此使用 `Popen(start_new_session=True)` + `os.killpg`。
    - CLI 可能以 0 退出，却仍发出 `turn.failed`：除了返回码外，还会检查 JSONL 输出（`--json`）；若返回码为 0 但缺少 `-o` 文件，则会抛出明确错误，而不是生成空分段。
  - **rate limit 的 back-off**：CLI 未实现任何内部 retry（`max_retries = 0`）。分类依据 JSON payload 的结构（`status: 429` / `error.type`），而不是子字符串——“quota”一词既会出现在可恢复的 429 中，也会出现在永久性的 `insufficient_quota` 中。
  - **CI 防护**：如果定义了 `CI` 或 `GITHUB_ACTIONS`，则拒绝 `--use_codex`。订阅身份验证不适用于共享 runner，而且 OpenAI 明确不建议在公共 repo 上使用此工作流。
  - **模型**：`gpt-5.6-sol`（质量）和 `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` 系列为 CLI 与 API Platform 共用，但 ChatGPT 账户并非对其中所有模型都有访问权限：allowlist 在服务器端应用，本地不会验证，使用非常规模型会触发警告。在 Plus 方案中，每个 5 小时窗口内，Luna 可提供 250–2 000 条消息，而 Sol 仅为 10–100 条：`--eco` 是所有批处理任务的推荐模式。
  - **已修复的 bug——`regen_translations.sh` 在完全成功后仍以错误退出**：`trap ... EXIT` 引用了 `failed_log`，它是 `main()` 的 `local` 变量，但在 trap 执行时已不存在。在 `set -u` 下，这会抛出 `failed_log: unbound variable`，导致脚本以 1 退出，尽管 28 项翻译均正确——这会在重新生成后的成本最高阶段中断 `release.sh --auto`（`set -e`）。该变量现已改为全局变量，trap 会检查其是否存在。一个有用的副作用是：此前被此错误掩盖的真正翻译失败，现在会重新显示在最终汇总中。
  - **`REGEN_MODEL`**：`regen_translations.sh` 的新环境变量，可覆盖 provider 的默认值并强制指定模型，例如使用 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`，以通过订阅配额中的高端模型重新生成，而不是使用面向吞吐量的 `--eco` 模型。
  - **`regen_translations.sh`**：`REGEN_PROVIDER=codex` 可通过显式 opt-in 启用（绝不自动检测，以免在用户不知情时消耗订阅配额）。在开启并行处理前，会先以串行方式刷新一次 token——因为 Codex refresh 采用轮换且只能使用一次，并发 job 会使 `codex login` session 失效——并发数也会降至 4。
  - **相关 refactor**：`_dispatch_provider_call` 通过返回 provider 名称的 `_resolve_provider()`，将参数从 8 个减少至 6 个，而不再把第四个布尔值传遍整个调用链。显式布尔值的优先级仍高于 `args`，以保留使用最小化 `Namespace` 调用 `translate(..., use_mistral=True)` 的测试。
  - **测试**：新增文件 `tests/test_codex_provider.py`（48 项测试），覆盖 argv、清理后的环境、禁止前言的契约、静默失败、timeout/killpg、back-off、preflight、provider 解析、Gemini 推理级联、Claude 块过滤，以及多段落 news 引用。完整测试套件共 290 项测试。
  - **实际验证**：通过 Codex 将项目的 `README.md` 翻译为 **14 种语言**后，其结构与参考译文完全相同（14 个代码块、24 个标题、25 行表格、13 个 HTML 链接、13 张图片、19 个 URL，代码块逐字符完全相同，placeholder 残留为零）。对于一篇 69 KB 的新闻文章，在 `--news` 模式下，`gpt-5.6-luna` 和 `gpt-5.6-sol` 的输出均能通过下游应用针对 en/ja/ar 的验证器。通过 `account/rateLimits/read` 测得的消耗：在 `--eco` 模式下仍低于计数器的舍入阈值（5 小时窗口的 0%）。

- **1.9.2** 修复包含嵌套括号或法语前缀的 news 归属 URL 提取（2026-05-11）：

  - **已修复的 bug**：`_protect_news_quotes` 中的归属 URL 提取使用正则表达式 `re.search(r"\((.+?)\)", attribution)`（括号之间的惰性捕获）。对于 `(relayé par [@user sur X](https://x.com/.../123))` 形式的归属信息（嵌套括号：外层 `(` + Markdown 链接的 `]()`），捕获会在遇到第一个 `)` 时停止 → 得到截断且包含法语前缀的字符串：`relayé par [@user sur X](https://x.com/.../123`（缺少末尾的 `)`）。结果是：`_validate_news_post` 会在译文中查找该字符串并必然失败（原因有二：`)` 被截断 +“转引自”被翻译为 `relayed by`/`weitergeleitet von`/……）。完整的 low → medium → high → gpt-5.5 级联均无法通过。
  - **修复**：正则表达式改为 `re.search(r"\]\(([^)]+)\)", attribution)`——专门匹配 Markdown 链接的 `](url)`，并且**只捕获纯 URL**（不含法语前缀，也不会截断）；翻译期间由 placeholder `#URL{N}#` 保持其不变。可稳健处理以下两种问题模式：
    - `(relayé par [@account sur X](url))`——嵌套括号
    - `via [@source](url)` 或 `selon [@author](url)`——不带外层括号的法语前缀
  - **测试**：在 `test_silent_failure.py` 的 `TestNewsCitationExtraction` 类中新增 2 项测试：
    - `test_extract_attribution_url_with_nested_parens`（精确复现 Genspark CEO E2B bug 的案例）
    - `test_extract_attribution_url_with_french_prefix`（带 `via` 的变体）
  - **覆盖缺口**：`check-editorial-coverage.py` 会验证编辑语法，但不会验证 translator 能否处理它。一个可能的改进（不在 v1.9.2 范围内）是添加一项检查，通过 dry-run 模拟归属信息提取，以便在发布**之前**检测高风险模式。

- **1.9.1** 修复翻译标记说明中 CTA 标签的 i18n（2026-05-10）：

  - **已修复的 bug**：翻译文件顶部标记横幅中 CTA 链接的 `[Voir le projet sur GitHub ↗]` 标签，在所有目标语言中都仍为**法语**，而没有跟随 `target_lang`。LLM 永远看不到它（它在 Python 端组装，以保留 repo 的 URL 和 slug），因此翻译阶段无法补救。自 v1.9 添加 `marker` 格式以来，这一直是一项静默回归。
  - **修复**：新增常量 `_VIEW_PROJECT_LABELS`，将 15 种语言映射到各自的本地化标签。`_translation_note_invariants(target_lang)` 和 `_assemble_translation_note_paragraphs(phrase, target_lang)` 现在会传递目标语言。如果语言未知，则 fallback 至 `fr`（用于保障安全，避免 KeyError）。
  - **测试**：调整 `test_source_emits_three_paragraphs_repo_title_description_link`（target_lang `ja` → 预期为日语标签）。新增 2 项测试：`test_source_link_label_localized_per_target_lang`（参数化覆盖 7 种语言，包括拉丁文字、表意文字和 abjad）和 `test_source_link_label_falls_back_to_french_for_unknown_target`。`test_translation_note_position.py` 中共 40 项测试（此前为 38 项）。
  - **向后兼容**：签名使用默认值 `target_lang="fr"`——未传入 `args.target_lang` 的外部程序调用方无需修改即可继续运行。
- **1.9** 修复静默失败 + 完整质量工具链 + 多位置翻译说明（2026-05-07）：
  - **多位置翻译说明 + “嵌入卡片”标记格式**：
    - 新增 CLI 选项（增量添加，默认值不变 → **非破坏性变更**）：
      - `--note_position {top,bottom,both}`（默认：`bottom`）：将说明放在译文文件顶部、底部或同时放在两处。
      - `--note_format {legacy,marker}`（默认：`legacy`）：
        - `legacy` 严格复现 v1.8 的行为（粗体段落 `**…**`），达到**逐字节一致**。
        - `marker` 输出一个不可见的 Markdown 链接引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），随后是一个结构化的**三段式引用块**，用于呈现类似“GitHub 仓库嵌入卡片”的效果：以内联代码显示项目标题（`**\`ai-powered-markdown-translator\`\*\*`）、由 LLM 翻译的描述，以及带可见箭头的行动号召链接（`[Voir le projet sur GitHub ↗](URL)`）。构建时可通过 remark 插件使用（参见 jls42.org 博客 → 插件 `remark-translation-banner`）。
    - **绝不发送给 LLM 的固定内容**：仓库标题和 GitHub URL 在描述性语句翻译完成后由 Python 端组装。LLM 永远看不到 slug `ai-powered-markdown-translator` 或 `https://github.com/jls42/...`，从而确保渲染方式、大小写和协议均不会被更改。
    - **识别 frontmatter 的插入方式**：在 `top` 或 `both` 模式下，说明会插入到 YAML frontmatter 的闭合 `---` 块**之后**（确保 Astro Content Collections / gray-matter 安全）。辅助函数 `_split_frontmatter` 检测文件开头的 `---\n…\n---\n` 并保持其完整性；若 frontmatter 已开启但没有闭合围栏，则**抛出 `RuntimeError`**（该文件会进入 `failed_files`，而不会因说明位置错误而被写入）。
    - **基于白名单的模型名称清理器**：`_sanitize_model` 将 `[A-Za-z0-9._:/-]` 范围之外的所有字符替换为 `_`，若结果为空则回退到 `unknown`。这与 Astro remark 插件端的验证器保持一致，并清除会破坏标记格式的字符（空格、引号、圆括号、逗号等）。
    - **内部重构**：`_append_translation_note`（1 个单体函数）→ 7 个纯辅助函数（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。构建器与组合器分离（构建器返回不含分隔符的纯块，组合器根据位置应用 `\n\n`）；生产代码与源辅助函数共用同一个三段式组装器。
    - **`_quote_lines` 保留空行**：为每一行添加 `> ` 前缀，并将空行转换为单独的 `>`。这样 mdast 就能在引用块中识别出 3 个独立段落（标题／描述／链接），而不是一个包含换行符的段落。
    - **自适应 `_build_translation_note_block`**：根据 LLM 保留的段落数量进行处理（3 = 完整卡片格式，2 = 语句 + 链接，1 = 回退方案）。当检测到 Markdown 链接 `](` 时，单段落回退方案**不再使用 `**...**` 包裹内容**（`<strong>` 包裹链接时渲染不稳定）。
    - **向后兼容**：`_compose_with_notes` 端使用 `getattr(args, "note_position", "bottom")` 和 `getattr(args, "note_format", "legacy")`——缺少这些属性的 Namespace（现有测试、外部编程调用）无需修改即可继续工作。
  - **修复长篇翻译的静默失败**：
    - 对所有提供商（OpenAI、Mistral、Claude、Gemini）执行译后语言验证：确定性层（在输出中发现源文原文片段）+ 概率层（`langdetect`）
    - `finish_reason` / `stop_reason` 白名单：对于白名单以外的任何状态（截断、content_filter 等）抛出 `RuntimeError`
    - Claude 的 `max_tokens`：`4096` → `32768`（避免 16k 分段发生隐性截断，并为法语到日语／中文／韩语／阿拉伯语／印地语的跨文字体系转换预留空间）
    - 识别标题的分段：优先选择分段后半部分的 H2/H3（使每个分段都从一个完整的语义章节开始）
    - 将错误传播至非零退出码：`translate_markdown_file` 返回类型化状态 `success` / `failure` / `skipped`；若至少一个文件失败，`main()` `sys.exit(1)`（单文件和批处理模式均适用）
    - 为所有提供商增加空内容防护、源文／输出合理性比率检查（源文 ≥ 500 个字符且输出少于其 5% 时拒绝）、代码占位符验证（`#CODEBLOCK`/`#INLINECODE`）、LLM 输出后规范化（修复与标题粘连的分隔符／链接），以及不使用 `reasoning_effort` 的 `BadRequestError` 重试
    - 新增依赖 `langdetect==1.0.9`
  - **pre-commit 质量工具链**（“完整 EurekAI 类型”，14 个钩子）：
    - Pre-commit：ruff（检查 + 格式化）、shellcheck、prettier（md/yaml/json）、detect-secrets（保护 4 个 API 密钥）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（空白字符、文件结尾、大文件、shebang 等）
    - Pre-push：mypy（渐进式宽松模式）、Opengrep SAST（translate.py + scripts/）、pip-audit（初始报告模式）、unittest discover（tests/ + scripts/tests/）
    - `scripts/` 中的本地包装器使用 `./venv/bin/python`
    - `scripts/audit_verdict.py`：pip-audit JSON 解析器，包含 11 个 unittest 测试，是从 jls42-astro 解析器适配而来的 Python 移植版
    - 修复了 7 个初始 ruff 违规项：B904（raise from）×2、B007（未使用的 dirs）、C408（字典字面量）、C419（列表推导式）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizard 暂时排除 `translate.py`（4 个函数的 CCN 为 21–47，已计划重构）——对 scripts/ 实施严格门禁
  - **SonarCloud + 全面覆盖率**：
    - GitHub Actions 工作流 `SonarCloud`（sonarcloud.yml + sonar-project.properties）：每次推送和拉取请求时运行分析，并通过 `coverage.xml` 获取覆盖率
    - README 顶部包含 11 个 SonarCloud 徽章（质量门禁、安全性／可靠性／可维护性评级、覆盖率、漏洞、缺陷、代码异味、重复行、技术债务、代码行数）
    - `tests/test_silent_failure.py`（`unittest` 标准库）：覆盖静默失败错误链的全部六个环节
    - `tests/test_orchestration.py`（新增 79 个测试）：覆盖 `translate.py` 的编排层（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` TypeError + BadRequestError 回退方案、o1 系列提示词格式、`_validate_translation_output` 的提前返回分支）
    - `scripts/tests/test_audit_verdict.py`：通过子进程覆盖 `main()`（stdin/stdout）和 `if __name__ == "__main__"` 块
    - **新代码覆盖率**：75.5% → 约 98%（translate.py 98%，scripts/audit_verdict.py 97%）
  - **测试**：`tests/test_translation_note_position.py` 覆盖位置 × 格式矩阵（包括端到端测试 `marker+top|bottom|both` 和 `legacy+top|bottom|both`）、多行前缀处理、逐字节向后兼容性（黄金字面量）、清理器、frontmatter 拆分（包括未闭合围栏时抛出异常）、三段式格式、两段式回退方案、单段落 + Markdown 链接防护，以及关键保护测试 `TestLLMPayloadExcludesInvariants`，用于断言标题和 URL 从不发送给 LLM。**190 个测试通过**，0 项回归。
  - 文档：`README.md`（法语 + 14 种译文）包含徽章，`CLAUDE.md`（pre-commit 工作流 + 详细的 CI 监视说明），重新生成了 28 份译文
- **1.8** `--news` 模式 + 2026 年模型升级（2026-03-17，标签 `v1.8`）：
  - 更新默认模型（2026 年 3 月）：
    - OpenAI 高质量模型：`gpt-5` → `gpt-5.4`
    - OpenAI 经济型模型：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 高质量模型：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - 新增 `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）和 `gemini-3.1-pro-preview`（1M）的 token 限制
  - 初始 `--news` 模式：使用 `#NEWSQUOTE\d+#` 占位符保护英文引文、`LANG_FLAGS` 映射（15 种语言）、按目标语言管理旗帜
  - 恢复前验证新闻占位符（回归问题：LLM 删除占位符时会静默生成不含引文的输出）
  - 使 `regen_translations.sh` 脚本可移植（使用绝对路径，不依赖当前工作目录）
  - 在 README/CHANGELOG 的语言栏中新增法语链接，重新生成了 28 份译文
- **1.7** 新增功能：
  - 新增 `--keep_filename` 选项，用于在翻译时保留原始文件名
  - 支持通过 `.env` 文件自动加载 API 密钥
  - **保留内联代码**：现在会在翻译期间保护反引号（`` `...` ``）
  - 改进系统提示词：
    - 更妥善地处理 YAML frontmatter 中的引号
    - 保护模板变量 `{variable}`
    - 禁止添加未经请求的译者说明
  - 已在 364 个文件上成功测试（jls42.org 博客迁移）
- **1.6** 新增功能：
  - 支持使用 Google Gemini API 进行翻译（`--use_gemini`）
  - 更新 2026 年默认模型：
    - OpenAI：`gpt-5`（高质量）、`gpt-5-mini`（经济型）
    - Claude：`claude-sonnet-4-5`（高质量）、`claude-haiku-4-5`（经济型）
    - Gemini：`gemini-3-pro-preview`（高质量）、`gemini-3-flash-preview`（经济型）
  - 新增经济模式（`--eco`），用于使用速度更快、成本更低的模型
  - 支持翻译单个文件（`--file`），无需遍历目录
  - 新的简化命名模式：`{base}-{lang}.md`
  - 新增 `--include_model` 选项，用于保留包含模型名称的旧格式
  - 支持未列出的模型，并采用默认 token 限制（128k）
  - README 已翻译成 14 种语言
- **1.5** 改进：
  - **更新 API 密钥和默认模型：**
    - **OpenAI：**从 `DEFAULT_MODEL_OPENAI` 更新至 `"gpt-4o"`。
    - **Mistral AI：**从 `DEFAULT_MODEL_MISTRAL` 更新至 `"mistral-large-latest"`。
    - **Anthropic Claude：**新增 `DEFAULT_ANTHROPIC_API_KEY`，并将 `DEFAULT_MODEL_CLAUDE` 更新至 `"claude-3-5-sonnet-20240620"`。
  - **优化翻译提示词：**
    - 丰富了直接翻译和翻译说明所使用的提示词，以提升清晰度和效率，其中包括有关保留元数据及特定格式元素的详细说明。
  - **代码重构：**
    - 使用 `Mistral` 类替代 `MistralClient`，以初始化 Mistral AI 客户端。
    - 重新组织导入，以提升可读性和可维护性。
    - 改进文本分段及代码块处理，以便在翻译过程中保留原始格式。
  - **输出文件管理：**
    - 对调输出文件名中的模型与语言顺序（例如 `f"{base}-{args.target_lang}-{args.model}.md"`），从而简化译文的组织与查找。
  - **其他改进：**
    - 删除无用空行以清理代码。
    - 进行细微调整，以改进脚本结构和可读性。
- **1.4** 新增功能：
  - 支持使用 Anthropic Claude API 进行翻译
  - 优化提示词，以进一步提升清晰度和效率
  - 进行细微调整，以提升代码可维护性
- **1.3** 改进与新增功能：
  - 改进代码块处理
  - 改进输出文件管理
  - 改进现有文件检测
  - 新增 `--force` 选项，用于强制执行翻译
  - 对调输出文件名中的模型与语言顺序
- **1.2** 修复更新日志
- **1.1** 新增对 Mistral AI API 的支持
- **1.0** 初始版本——支持 OpenAI API

**使用 gpt-5.6-sol 将文章从法语翻译成中文。**
