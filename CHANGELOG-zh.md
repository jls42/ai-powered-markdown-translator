### 更新日志

🌍 [法语](CHANGELOG.md) | [英语](CHANGELOG-en.md) | [西班牙语](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [德语](CHANGELOG-de.md) | [日语](CHANGELOG-ja.md) | [韩语](CHANGELOG-ko.md) | [阿拉伯语](CHANGELOG-ar.md) | [印地语](CHANGELOG-hi.md) | [意大利语](CHANGELOG-it.md) | [荷兰语](CHANGELOG-nl.md) | [波兰语](CHANGELOG-pl.md) | [葡萄牙语](CHANGELOG-pt.md) | [罗马尼亚语](CHANGELOG-ro.md) | [瑞典语](CHANGELOG-sv.md)

- **1.12.0** Provider `--use_opencode`：通过开源代理 OpenCode 使用用户所选的供应商——本地模型、无需账户的免费模型、订阅或密钥（2026-09-04）：

  - **第八条 provider 路径，其性质与前七条不同。** [OpenCode](https://opencode.ai)（MIT）不是模型供应商，而是一个_路由器_，负责连接用户在 OpenCode 本身配置的供应商：API 密钥、订阅（GitHub Copilot、ChatGPT、SuperGrok）、提供**无需账户**的免费模型的 OpenCode Zen 网关，或**本地**模型（Ollama、LM Studio、llama.cpp）。脚本以非交互模式驱动 `opencode run`，方式与驱动 Codex 和 Grok 相同，并复用同一套子进程基础设施（独立进程组、超时时先执行 `SIGTERM` 再执行 `SIGKILL`、始终关闭 stdin、清理环境）。已通过**两次真实翻译**验证：使用 `opencode/mimo-v2.5-free` 将整个 README 翻译为英语——49 秒、仅一轮、结构与源文件完全相同（32 个标题、26 个代码块闭合标记、18 个链接、37 个 URL、37 行表格、135 处行内代码）——以及使用 `ollama/qwen2.5:7b` 在本地、无需任何密钥翻译一个测试文件。

  - **`--model provider/modèle` 是必需的，而且这是刻意的选择。** 如果没有 `--model`，OpenCode 会回退到自身默认值；在全新安装中，该默认值为 `opencode/big-pickle`，这是一个免费的“隐形”模型，其交互内容可能用于训练——实测中，作出响应的正是该模型。替用户静默选择它，恰恰属于本仓库力图追踪的隐形切换；因此，错误消息会给出列出模型的命令（`opencode models`）以及三个示例（本地、免费、订阅）。`--eco` 不起作用，并会明确说明这一点。只有在用户明确要求时，`--reasoning_effort` 才会原样作为 OpenCode 的 `--variant` 传递。

  - **隔离经过实测，而非假定。** 一份内联配置（`OPENCODE_CONFIG_CONTENT`，在 OpenCode 合并顺序中位于最后，因此优先于用户配置，但不会替换它）定义了一个 `aipmt` 代理，并拒绝其使用所有工具（`permission: {"*": "deny"}`）：注册表甚至不再向模型提供这些工具；当被要求“列出文件并运行 `id`”时，模型会回答自己没有工具。会话共享已禁用，外部插件已排除（`--pure`），绝不使用 `--auto`，工作目录为空且用后即弃。实测发现并切断了两种静默注入：若没有 `OPENCODE_DISABLE_CLAUDE_CODE`，用户的 `~/.claude/CLAUDE.md` 会进入**每一个**提示词（简单一句“你好”的输入 token 从 186 增至 515）；若没有 `OPENCODE_DISABLE_PROJECT_CONFIG`，当前目录的 `AGENTS.md` 也会进入提示词——一条“每次回答都以 BANANA 结尾”的指令确实被应用到了翻译中。而全局 `~/.config/opencode/AGENTS.md` 仍会被注入：没有开关能排除它，若通过挪用 `XDG_CONFIG_HOME` 来绕过，还会一并隐藏用户的供应商。对此选择如实记录，而非草率拼补。

  - **`exit 0` 证明不了任何事：这是第三个 CLI，沿用相同的审慎原则——但它有两个特有陷阱。** 未知的 `--agent` 不会使 `opencode run` 失败：它只在 stderr 上发出警告，随后**静默**回退到启用了工具的编码代理。因此，如果内联配置未生效，翻译就会由一个能够写入文件的代理执行；所以输出契约除了检查是否不存在该消息，还会验证：返回码为 0、没有 `error` 事件、没有 `tool_use`、最后一个 `step_finish` 处于 `stop` 状态（`length` 表示响应被截断）、文本非空。第二个陷阱：错误 JSON 事件是**不透明的**——“意外的服务器错误。请检查服务器日志以了解详情。”，只附带一个简单引用——而真正的原因（`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`、`ProviderAuthError`……）只存在于日志中。因此需要 `--print-logs --log-level ERROR`，并读取 stderr 的 `error="…"` 字段，同时排除其后的 Bun 堆栈。这样，未知模型会在一秒内失败，并明确指出原因。`--title` 还顺带避免了一次多余的 LLM 调用：如果没有它，OpenCode 会在 `small_model` 上额外执行一轮来生成会话标题。

  - **密钥：采用与 Codex 和 Grok 相同的模式过滤，仅有一个具名例外。** 保留 `OPENCODE_API_KEY`：这是 OpenCode 自身的密钥（Zen 网关、Go 订阅），按名称指向 OpenCode——相当于它的 `auth.json`，既不是 aipmt 管理的密钥，也不可能由 aipmt 计费。供应商在 OpenCode 中配置（`opencode auth login`、`opencode.json`），绝不配置在 aipmt 的 `.env` 中；aipmt 的任何密钥都不会到达子进程。与订阅型 CLI 不同，CI 中不会拒绝此模式：在 runner 上使用 API 密钥或自托管模型都是合理用途。

  - **防路径穿越保护现在检查插值后的值，而非原始值。** `provider/modèle` 包含一个 `/`，1.10.0 的保护会拒绝它——这有其道理，因为 `--model` 会被插入文件名 `--include_model`。文件名标签现在会在任何插值发生前，将 `/`、`\` 和 `:` 替换为 `-`（`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`，因为 `:` 在 Windows 下非法），上游保护则检查这一标签：`../../evil` 会变成目标目录下的普通文件名 `doc-en-..-..-evil.md`；只有 `..` 仍会被拒绝，`--target_lang ../x` 也一样。`_ensure_within_directory` 范围保护仍作为未变的第二层防线。

  - **免费模型和本地模型，以及实测结果。** `opencode/mimo-v2.5-free` 翻译一个段落需要 16 秒，翻译此 README 需要 49 秒；`opencode/big-pickle` 翻译 200 个词需要 40 秒，两个并发请求在 5 分钟内都没有响应，而单独执行时各自都能完成；`opencode/nemotron-3.5-lightning-free` 在 3 分钟内没有任何响应。因此 `REGEN_PROVIDER=opencode` 要求必须提供 `REGEN_MODEL`，并采用 **2 个并行任务**。本地方面，Ollama 通常配置 4,096 个上下文 token，而分段最长可达 16,000 个字符：必须使用带 `PARAMETER num_ctx 32768` 的 `Modelfile`，翻译质量则取决于模型——在测试文件上，一个 7B 模型颠倒了列表，并破坏了一个代码块闭合标记，而网关模型完整保留了一切。

  - **本仓库的翻译从此绝不再通过按量计费的 API。** 只要 `.env` 中残留密钥，`regen_translations.sh` 就会使用 OpenAI API，而 Codex 仅作为显式选择。准备本版本时发生的情况正是如此：28 份翻译先通过 OpenAI API 执行，之后印地语 CHANGELOG 又通过 Gemini API 执行，尽管 ChatGPT 订阅的存在本就是为了避免按使用量付费。密钥自动检测现已移除：**默认使用 Codex，并采用 `gpt-5.6-sol`**，即质量模型；`openai`、`gemini` 和 `grok` 除了 `REGEN_PROVIDER` 外还要求 `REGEN_ALLOW_PAID_API=1`，这是一个具名豁免，使规则在作出选择时立即生效；未知的 `REGEN_PROVIDER` 会直接失败，而不会回退到 API。十项测试锁定了默认行为、拒绝机制和豁免机制。本版本的 28 份翻译均已通过 Codex 重新生成。

  - **针对 rate limit 的退避逻辑已抽取复用**（`_retry_on_rate_limit`）：Codex 和 Grok 的循环除标签外完全相同，若再复制第三份，就会越过重复代码阈值。三个 CLI 错误都派生自同一个 `_CliCallError`；一项测试禁止其中任何一个脱离该继承关系，否则共享循环将无法再捕获它。

  - **测试**：新增文件 `tests/test_opencode_provider.py`（51 项测试）——完整输出契约、代理回退、从日志读取原因、文本片段去重并忽略合成片段、超时终止进程组、针对 429 的退避、模型必填及验证、无密钥预检、二进制文件解析、分派接线、文件名标签及路径穿越反证。`tests/test_review_hardening.py` 将 flag 互斥检查及密钥隔离检查扩展至新 provider。gate 现在要求记录 **22 个 argparse flag**。完整测试套件共 **382 项测试**。

- **1.11.1** 文档修正：README 终于列出了七条 provider 路径（2026-09-03）：

  - **1.11.0 的 PyPI 页面写的是“4 个 API + Codex CLI”。** 实际代码提供七种路径——通过 API 使用 OpenAI、Mistral、Claude、Gemini 和 Grok；以及通过订阅使用 Codex（ChatGPT）和 Grok，不按使用量计费。简介和_多供应商_条目遗漏了两种 Grok 模式，14 份翻译也重复了这一错误。由于软件包的长描述在每个版本中固定不变，要修正展示页面就必须发布新版本号：这就是此版本存在的唯一原因。**没有代码变更。**
  - `CLAUDE.md` 已与发布时引入的内容对齐：gate 计数器（16，`--full` 中为 17）、十一个活跃 workflow、`gh pr checks` 中不可见的两个 Sonar/Codacy 计数器（hotspot、Codacy API）、通过 `ruff-format` 移动一个 `# nosemgrep`、OIDC 交换所需的 GitHub 环境，以及_pending publisher_不会保留名称这一事实。

- **1.11.0** 发布至 PyPI：先执行 `pip install ai-powered-markdown-translator`，随后执行命令 `aipmt`，无需克隆仓库（2026-09-03）：

  - **单文件脚本变为可安装的软件包。** `translate.py` 从根目录迁移至 `src/aipmt/translate.py`，并提供控制台入口点 `aipmt` 及其等效形式 `python -m aipmt`。贡献代码仍需克隆仓库——测试、28 份翻译和质量工具都位于其中——但使用工具不再需要克隆。

    - **导入名称是 `aipmt`，绝不能是 `translate`**，因为命名冲突真实存在且不会显式报错。PyPI 软件包 `translate`（v3.8.1，最后上传于 2026-07-06）会安装一个同名的目录。已在 venv 中复现：目录优先于模块，`translate.main` 消失，入口点因 `AttributeError` 而损坏——但 `pip check` 仍以 rc=0 回答“未发现损坏的依赖项”。用户只需执行一次简单的 `pip install translate`，就足以在没有可用诊断的情况下破坏 CLI。已用真实 wheel 完成反证：在该软件包之上安装 `pip install translate`，`aipmt --help` 在安装前后均为 rc=0，两个 CLI 可以共存。
    - **发行名称长，命令简短。** `ai-powered-markdown-translator` 使该软件包可通过 PyPI 搜索找到；如果只使用缩写，不了解该项目的人便无法找到它，而发布的目的正是让项目可被发现。经核查排除了两个看似合理的候选名称：`ai-markdown-translator` 自 2024 年起已在 npm 被一个用途相同的工具占用，比本仓库早 17 个月；`aimt` 与 `aim`（v3.29.1）仅相差一个字母，后者是同一领域的活跃软件包——这是最容易造成长期混淆的情况。顺带还有一个方法陷阱：`pypi.org/project/<nom>/` 对任何名称都会返回 200（反机器人页面），只有 JSON API 的结果可信。
    - **采用 `src/` 布局，而非扁平软件包。** 扁平软件包会保留测试中的六个 `sys.path.insert(..., "..")`，而这恰恰是问题所在：它们会导入源码树而不是已安装的软件包，从而掩盖任何打包错误。实际成本只是增加一条替换规则。

  - **密钥终于只需配置一次。** 已安装的 CLI 此前没有任何持久配置：只能使用环境变量或当前目录中的 `.env`。诚然，`find_dotenv` 会一直向上查找到系统根目录，因此在用户**位于个人目录之下工作时**，能够找到 `~/.env`；但在其他位置工作时则一无所获——覆盖范围取决于从何处启动命令，而非明确的设计选择。因此新增第三层配置：`~/.config/aipmt/.env`，其优先级低于现有两层。

    - **优先级并非硬编码**，而是来自 `load_dotenv` 的默认值 `override=False`：每一层只填补前一层留下的空值。因此顺序为环境变量 → 项目的 `.env` → 用户配置；这一点通过行为测试而非结构测试验证——交换两次调用的顺序会使测试失败，移除第三层也一样。
    - **刻意采用 `.env` 格式，而非 TOML**：`python-dotenv` 已经是依赖项，其语法已记录在 15 份 README 中，同一种文件也可用于两个作用域。无需新增依赖项或语法。若 `XDG_CONFIG_HOME` 为**绝对路径**，则配置位置遵循它——规范要求忽略相对值，否则配置位置将再次取决于当前目录——Windows 下则遵循 `APPDATA`。
    - **排除了两个选项，并说明原因。** 系统密钥链（`keyring`）在桌面设备上更安全，但在无界面环境中会失败——服务器、容器、CI——而这些恰恰是批量翻译的典型使用场景；它适合作为显式选择，却不适合作为默认方案。`--api-key` flag 会使密钥进入 shell 历史记录，并在 `ps` 中可见。
    - **缺少密钥时，不再显示调用堆栈。** 用户此前会收到一段指向 `site-packages` 的 Python 堆栈，以及一条只提到“环境或 .env”、却没有说明应在何处创建后者的消息。现在，消息会列出三个位置及其确切路径，命令以状态码 2 退出。保护网被**刻意限定在狭窄范围内**：仅在配置阶段的 `except ValueError`。若包裹整个执行过程，翻译期间发生的真实错误就会被转换成一条令人安心的消息——这正是本仓库力图追踪的故障模式。一项测试会读取 `main()` 的源码，以禁止这种做法。

  - **修复——工具安装后，用户的 `.env` 会被忽略。** 不带参数的 `load_dotenv()` 并非从当前目录向上查找，而是从调用方文件开始，因此会从 `site-packages` 开始。已使用真实控制台入口点进行实测：从拥有自身 `.env` 的项目中启动时，`find_dotenv()` 返回 `''`，密钥不会被加载；而 `find_dotenv(usecwd=True)` 则能找到它。只要工具仅从克隆的仓库中运行，该错误就不会出现；一旦发布，它就会成为系统性问题，唯一症状是在配置正确的情况下仍提示 API 密钥“缺失”。

  - **三个 gate 即使停止执行任何有效检查，也会显示绿色。** 它们已在迁移前刻意加固：若防护措施是在其应捕获的变更之后才编写，就无法证明任何事。每个 gate 在原始仓库上均为绿色，在迁移后的副本上则变为红色——两个方向都经过了实测。
    - **Lizard 会静默忽略不存在的路径**：rc=0，“已分析 0 个文件”。复杂度 gate 原本会从 158 个函数 / 2247 nloc 变成 3 个函数 / 34 nloc，并产生零字节输出。scope 现在是一个数组，其中每个条目都会经过存在性检查。
    - **对不存在的模块运行 `coverage run --source=` 不会失败**：仅在 stderr 中发出警告，无论 unittest 还是 `coverage xml` 都返回 rc=0，而且仍会发布报告——statements 从 1453 骤减至 141。项目会显得很健康，只因几乎已不再接受分析。报告现在由两个下限守护：总量，以及测得的最大文件。
    - **翻译新鲜度探针在结构上无法识别调用形式**：它以 argparse flags 为锚点，而文件重命名恰恰不会改变这些 flags。复现结果：模块被移动后，15 个 README 仍在记录一条已不存在的命令，判定却是“没有过期翻译”。因此，第 7 节现在验证的是调用形式而非选项，并将 Lizard hook 与脚本的实际 scope 进行比对——当其 `files:` 不再匹配时，不会使 pre-commit 失败，而会直接跳过它。

  - **`requires-python = ">=3.10"` 不再只是一项声明。** `sonar-project.properties` 早已宣称支持 3.10-3.12，但从未实际运行过这些版本，因为开发机上只有 3.12——这是一个发布后就会暴露的内部矛盾。现在，测试 workflow 会在 3.10、3.11 和 3.12 上运行测试套件，并安装完整 PAQUET，从而验证其公开版本边界。

  - **设定下限，不设上限。** `requirements.txt` 仍是经过测试的 lock，`[project.dependencies]` 则成为公开契约：若发布 lock 中的精确版本，所有还安装了其他包的用户都可能遭遇冲突。也不设置 `<N+1` 上限——这会与 `check-deps-fresh.sh` 正面冲突，因为后者会在任何主版本落后时让 release gate 失败。这组下限解决了问题，而反向测试 `openai==1.0.0` 返回 `ResolutionImpossible`，证明该检查能够做出区分，而非一概放行。此外，还有一道防护禁止 `pyproject.toml` 的版本与 CHANGELOG 中的版本不一致：PyPI 不允许重复使用版本号。

  - **已在全新 venv 中完成端到端验证**：约 70 Ko 的 wheel 仅包含 `aipmt/*.py`、dist-info 和许可证；`aipmt --help` 返回 rc=0，含 22 个 flags；`python -m aipmt` 显示“usage: aipmt”，而非“usage: \_\_main\_\_.py”；安装后的 `pipx` 可正常工作；最重要的是，**从任意用户目录完成了一次真实的 fr→en 翻译**，粗体、列表、inline code、链接和 URL 均得到保留，code block 未被翻译。迁移前的 318 项测试全部通过，且迁移前后的标识符列表逐字节一致——证明没有任何测试被停用的正是这一点，而不是“OK”；此外还为三层配置新增了十二项测试，总计 330 项。

- **1.10.0** Provider `--use_codex`（ChatGPT 订阅配额）、SDK 与模型更新、修复 news 多段落引用（2026-08-29）：

  - **安全审查——PR 设置了两道防护，却未能处处落实**：

    - **Codex preflight 将整个 `.env` 传给了二进制文件。** `_codex_preflight` 调用 `subprocess.run` 时**没有传入 `env=`**：子进程继承了完整的 `os.environ`，也就继承了由 `load_dotenv` 加载的全部 `.env`。使用带检测功能的伪二进制文件实测：**七项机密信息**进入了 preflight——六个 providers 的密钥，外加一个 `GITHUB_TOKEN`；相比之下，对应的 `_grok_preflight` 中有**零项**，因为它正确传入了 `env=_grok_env()`。这正是 PR 内部的不一致：几行之外的 `_strip_secret_env` 就是专门用于维持这一不变量的。现在提取出一个 `_codex_env_base()`，供两条路径共同使用；修复后测得：两边均为 0 项机密信息。
    - **“`--deny` fail-closed”属性并未覆盖实际使用的形式。** 注释以未知前缀的规则会导致启动被拒为依据，为整个 Grok 隔离机制提供合理性说明。在 `grok 1.0.13` 上实测发现，该验证**仅适用于带括号的形式**：`--deny 'CeciNestPasUnOutil(*)'` 会拒绝启动（“unknown tool prefix”），而 `--deny 'CeciNestPasUnOutil'` 则会被静默接受。但 `GROK_DENY_RULES` 使用的全是裸名称——因此，若 xAI 端重命名工具，在 OS sandbox 本就不生效的机器上，唯一经过实测的隔离层会在毫无提示的情况下被移除。八条具名规则现已改为 `Prefix(*)`，并逐一验证为 CLI 已知的前缀；catch-all `*` 仍保持其字面形式，因为只有这种形式会被接受。一项测试可防止退回未经验证的形式。
    - **其他方面验证无误**：不存在命令注入（始终使用列表形式，从不使用 `shell=True`，文档内容通过 stdin 或 `--prompt-file` 传入），不存在不安全的反序列化（仅使用 `json.loads`，并带有类型防护），对七种 payload 的测试均未发现可绕过路径遍历修复的方法，并且 CLI 确实应用了 `--deny '*'`（读取 workdir 外部内容时观察到 `DENY_ENFORCED`）。
    - 此外，上文新增的新鲜度检查还绕过了自身原则：当某个包的 PyPI 请求失败时，它会静默跳过该包，而 gate 仍为绿色。现在，它会统计实际完成比较的包，并在覆盖不完整时失败。

  - **依赖项已更新至当前水平，并增加两道防线以防再次长期落后**：

    - **落后是真实且长期存在的**：`openai` 2.54 → **3.6.0**，`anthropic` 0.125 → **1.2.0**，`certifi` 2024.8.30 → **2026.7.22**——也就是说，用于验证所有 providers TLS 调用的根证书存储落后了两年。原因已经查明：**此前并不存在 `.github/dependabot.yml`**。没有这个文件时，GitHub 只会启用 _安全更新_，Dependabot 也只会为受 CVE 影响的依赖项提出 PR——这就解释了为何它更新了 `urllib3` 和 `idna`，却任由两个 SDK 落后整整一个主版本。
    - **两个主版本可以共存而不发生冲突**，与此前的担忧相反：`openai` 3.x 和 `anthropic` 1.x 会迁移到 **`httpx2`**，而 `mistralai` 和 `google-genai` 仍使用 `httpx<1`，但它们是两个不同的 distributions。先通过真实安装进行验证，随后又对 **7 条 provider 路径进行了端到端测试**——OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI 和 Grok CLI——每条输出中的 inline code 和链接均得到保留。“避免两套 HTTP 栈”只是一项偏好，并非阻碍：实测结果已经给出结论。
    - **`requirements.txt` 并未描述真实环境**：`google-auth`、`cryptography` 和 `opentelemetry` 栈安装在工作 venv 中，却从未声明——因此，全新安装无法复现受测环境。相反，`tokenizers`、`huggingface-hub` 和 `PyYAML` 虽列在其中，却未被任何代码导入，也不是任何组件所需，它们是 `mistralai` 1.x 的遗留项。该文件现在根据仅含直接依赖项构建的 venv，重新生成为完整的依赖闭包。`pip-audit` 在这组新依赖项中未发现任何已知漏洞。
    - **`.github/dependabot.yml`**（新增）启用 pip 和 github-actions 的每周版本更新。次版本与修订版本更新合并为一个 PR——每个 patch bump 一个 PR 最终只会被忽略，而噪声是更新工作的敌人；**主版本单独处理**，每个都必须通过真实调用验证。
    - **`scripts/check-deps-fresh.sh`**（新增，已接入 gate）使依赖落后情况能够体现在项目判定中：Dependabot 只负责提出建议，并不提供保证，它的 PR 也可能不断堆积。主版本落后 → 失败；次版本落后 → 警告，因为长期保持红色的 gate 最终只会被忽略；PyPI 无法访问 → 本地明确 skip，**CI 中 fail-closed**，因为未执行的检查不等于成功。已从两个方向完成验证：它能捕获修复前的准确状态（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`），而对于次版本落后则只发出警告。

  - **本次 PR 审查产生的修复**——五个审查 agents 仔细检查了 diff；下列问题在修复前都已通过实测复现，其中两个是由本版本前文中的改动引入的回归。
    - **已修复回归问题——`_NEWS_CITATION_REGEX` 存在指数级回溯。** 多段落修复在重复结构中引入了 `(?:[ \t]*$|[ \t]+.*)`：`[ \t]+` 与 `.*` 之间的空格归属存在歧义，而且这种歧义会随每次迭代成倍增加。对不匹配该模式的 `>   texte` 行——完全合法的 Markdown 缩进——进行测量：**14 行耗时 2 589 ms**，修复后仅为 0.04 ms，每增加一行，耗时约增至 9 倍。在 `--news` 模式下，一段较长且不合规的 blockquote 就足以让翻译一直卡住，直至作业超时，而且无法识别原因。现在，每次重复都会一次性消费整行（`\n^>(?![ \t]*—).*`），因此每次迭代只有一种匹配方式。已在包含 231 篇文章的真实语料库上验证：捕获结果**零差异**，仍是相同的 423 条引文，14 个多段落正文也仍然全部扩展。
    - **同时使用两个 provider flag 会悄无声息地按量计费。** `--use_codex --use_mistral` 过去会被接受；`_select_provider_client` 首先检查 Mistral，`_resolve_provider` 则优先采用显式布尔值——两者最终都会选择 Mistral。因此，用户请求使用订阅配额，得到的却是按量计费，而且没有任何警告：这正是 `--use_codex` 本应防止的故障模式。现在，六个 provider flag 都通过一个 `add_mutually_exclusive_group` 处理。**行为变更**：过去会被静默接受的、组合使用两个 provider 的命令行，现在会在 `argument --use_mistral: not allowed with argument --use_codex` 处失败。
    - **工作结束 gate 会在其探针崩溃时变绿。** `scripts/check-release-ready.sh` 的十三项检查中，有四项采用“捕获 stdout，若为空则下结论”的模式，却从不检查返回码：异常（文件被重命名、`FileNotFoundError`）会写入 stderr，使 stdout 保持为空，而检查却得出“一切正常”的结论。用于防止“一个 `exit 0` 什么也证明不了”这一陷阱的脚本，内部又重现了同一个陷阱。现在，helper `probe()` 会同时要求返回码为零**并且**存在结束哨兵，而探针在标记集合为空时拒绝下结论——因为对空集合的断言永远为真。示例：加入上述互斥组后，provider flag 通过一个 `*_group` 对象传递，旧 regex `parser\.add_argument\(` 不再能够匹配它；**二十一个 flag 中有六个**悄无声息地脱离检查范围，而 gate 仍然为绿色。
    - **secret 扫描漏掉了六个 provider 中的四个。** 字符类 `[A-Za-z0-9]` 排除了连字符：`sk-proj-…`（当前 OpenAI 格式）和 `sk-ant-api03-…` 都会在第二个连字符处中断，而 `AIza…` 根本未被覆盖。现已扩展模式，并将 `.secrets.baseline` 排除在扫描之外。此外，守卫 `.env` 查询的是 `git diff --cached`，它只能看到索引：一个**已经提交**的 `.env`——最糟糕的情况——永远不会出现在其中。现在改为查询 `git ls-files`。
    - **Codex 的“token 预热”其实并没有预热。** 实测发现：`codex login status` 不会触碰 `~/.codex/auth.json`（mtime 和大小均未变化），其帮助信息写的是“显示登录状态”。但注释却声称它会“以串行方式执行一次”token 刷新，从而消除一次性轮换 token 并发刷新的风险。宣称的保护其实并不存在；现在注释准确说明了代码实际执行的操作，而真正的规避措施仍是 `max_jobs=4`。此外，该检查现在会遵循此前被忽略的 `CODEX_BIN`——对于 `PATH` 中不存在 `codex` 的工作站，过去会以“未认证”失败，给出误导性诊断。
    - **`.env` 在子 shell 中被 source。** `detect_provider` 通过命令替换调用，因此其中的 export 无法传回：在 `.env` 中定义的 `GROK_BIN`、`GROK_HOME` 或 `REGEN_MODEL`，对 `main()` 中执行的读取仍不可见，导致其在配置正确时也得出“找不到 Grok 二进制文件”的结论。
    - **并发量比宣称的上限高出 50%。** 守卫被放在 README/CHANGELOG 任务对启动之后：实测 `max_jobs=2` 的峰值为 **3**。对于每周配额与 Chat/Imagine/Voice 共享且无法测量的 Grok，脚本因此未能遵守自己设定的上限。至于最终计数，它虽然会显示出来，却从未与 28 比较——缺少文件也不会被发现。
    - **Grok 输出契约：现在缺少 `stopReason` 会被视为失败。** 代码原本在已声明的契约要求 `end_turn` 的位置使用“`end_turn` **或缺失**”。缺少该字段的 payload——或该字段因 CLI 更新而被重命名——会让守卫悄无声息地变成 no-op。此外，`max_turn_requests` 不再被归类为 rate limit（这是轮次预算已耗尽：重试只会在等待 90 秒后得到同一结果），`quota` 也从 rate limit 标记中移除——原因正是 `_codex_is_rate_limited` 的 docstring 早已说明、但 Grok 此前并未遵循的那一点。
    - **Gemini cascade 现在按模型 memoize。** 过去每个 segment 都会从 `minimal` 重新开始，即使默认模型会拒绝它：正常路径会为每个 segment 多付出一次 400 往返，并重复输出同一条警告。一条重复数百次的 warning 会无人再读——它就这样变成了掩蔽物。
    - **其他**：CI 中的拒绝消息被硬编码为 Codex，导致 `--use_grok_cli` 用户被引导至 `OPENAI_API_KEY`，而不是 `XAI_API_KEY`；`provider.capitalize()` 会显示“Grok_cli”和“Openai”；子进程基础层的注释把“shim”泛化到两个 CLI，但 Grok 二进制文件实际上是原生 ELF（正确理由是“会生成自身子进程的 agent”）；`subprocess` 上的十二项 SAST finding 已标记为 `# nosec` / `# nosemgrep` 并附有理由，因为不含 `shell=True` 的列表形式使注入无法发生，且文档内容从不通过 argv 传递。
    - **现在不会再有任何 secret 进入 agent 子进程。** 按名称设置的 deny-list 过去只保护**计费**不变量（Codex 不带 `OPENAI_API_KEY`，Grok 不带 `XAI_API_KEY`）。实测发现：每个子进程中仍会进入**另外七个 secret**——Anthropic、Mistral、Google 和 Gemini 的密钥、另一个 CLI 的密钥，以及并非 secret 但会改变流量去向的 `OPENAI_BASE_URL`。然而，这两个 CLI 都是 **agent**，而且 Grok agent 在许多 Linux 工作站上运行时没有可用的 OS sandbox。现在改为**按名称模式**过滤（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`），而不是使用按名称枚举的列表，因此也能覆盖用户在其 `.env` 中添加、但本代码并不知晓的变量。CLI 不需要其中任何一个变量：认证信息存放在 `~/.codex` 和 `~/.grok` 中，绝不会存放在环境中——已分别通过两个 provider 在加固后的环境中完成**真实翻译**并验证成功。
    - **测试**：新增文件 `tests/test_review_hardening.py`（21 个测试），用于锁定 provider flag 的互斥性、`stopReason` 契约、news regex 的线性复杂度、CI 拒绝消息、Gemini memoize，以及子进程环境中不存在任何 secret。最后一项断言是**通用的**——即便密钥未被任何列表点名，它仍会失败——而现有的清除测试只是其常量的镜像，除了自身循环失效外，无法检测任何其他问题。完整测试套件现有 **311 个测试**。

  - **两个新的 Grok provider**：`--use_grok`（xAI API，使用密钥 `XAI_API_KEY`，按量计费）和 `--use_grok_cli`（官方 Grok Build CLI，从 Grok 订阅中扣除——原理与 `--use_codex` 相同）。
    - **API 模式，约 40 行代码**：由于 xAI endpoint 与 OpenAI 兼容，client 和 `_call_openai` 均原样复用，只有 `base_url` 发生变化。仅需进行一项适配，而且所有 provider 都能受益：`finish_reason` 现在接受 `end_turn`，这是 xAI 输出的形式，而 OpenAI 输出的是 `stop`。模型：`grok-4.6`（质量）和 `grok-4.3`（经济）。需要注意的是，Grok 的经济模型仍是仓库中最昂贵的——每百万 token 为 $1.25/$2.50，而 `mistral-small-latest` 仅为 $0.15/$0.60：选择这个 provider 是为了模型多样性，而不是价格。
    - **CLI 模式**：以 Codex 为基础实现，但根据实际情况存在四处必要差异——prompt 通过文件传递（`--prompt-file`；该 CLI 不读取 stdin，而将一个 segment 放入 argv 会使其在 `ps` 中可见）、输出是 stdout 上的单个 JSON 对象（既不是 JSONL，也不是 `-o` 文件）、订阅仅提供 `grok-4.6` 和 `grok-4.5`，而且 sandbox 无法应用（见下文）。子进程启动逻辑与 Codex 一起抽取至 `_codex_run_process`，未改动其余已经过测试的 Codex provider。
    - **实测证明 `exit 0` 什么也不能说明**：在未认证状态下，CLI 会将 `{"type":"error","message":"Not signed in."}` 写入 **stdout**，同时返回码仍为 **0**。遭到拒绝或超出轮次限制时也同样如此。因此，输出契约要求同时满足四个条件：返回码为 0、不存在错误 payload、存在 `stopReason == end_turn`，并且文本非空。preflight 遵循同一逻辑：`grok models` 即使在未登录时也以 0 退出，只有 stdout 中出现“not authenticated”才能据此下结论。
    - **隔离：明确接受并记录这种不对称性。** Codex 运行于 `--sandbox read-only`，而 Grok sandbox 在许多较新的 Linux 工作站上无法应用，原因是两个相互独立、且没有 `sudo` 就无法规避的系统问题：从 Ubuntu 24.04 开始，AppArmor 会阻止非特权 user namespace（`bwrap: setting up uid map: Permission denied`，已在 Grok 之外复现）；当 `/run/podman` 处于 `0700` 状态时，容器 runtime socket 的 deny-list 会失败（resolver 只会捕获 `ErrorKind::NotFound`，EACCES 会成为致命错误）。核心陷阱在于：一个无法应用的**内置**配置文件会**悄无声息地以无隔离状态启动**。因此，脚本默认不请求任何配置文件，也绝不会静默回退——它会在 stderr 上发出警告。保护依赖于 CLI 的 `--deny` 规则，其中包括 catch-all `*`；这是唯一经测量会以 _fail-closed_ 方式运行的层（带有未知前缀的规则会导致启动被拒绝）。可通过 `GROK_TRANSLATE_SANDBOX=read-only` 强制要求该层；如果机器无法满足要求，启动就会失败。
    - **防护措施**：从子进程环境中移除 `XAI_API_KEY`、`GROK_API_KEY` 和 `GROK_SANDBOX`（密钥会使其切换为按量计费；继承的 `GROK_SANDBOX` 会强制应用一个不可用的配置文件，并显示误导性消息），禁用 MCP/hooks/skills/agents 开关，使用 `--disable-web-search`、`--no-subagents`、`--no-plan`、一次性 workdir、CI 拒绝机制、会终止整个 process group 的 timeout，以及针对 rate limit 的 back-off。`--max-turns` 被设为 6 而不是 1：计数器会在工具轮次结束后递增，设为 1 会截断输出。
    - **配额**：Grok 配额池按周计算，并且**与 Chat、Imagine 和 Voice 共享**，同时没有任何命令能够显示它——这与 Codex 不同，后者可通过 `account/rateLimits/read` 量化消耗。因此，`regen_translations.sh` 将并发限制为 2，并明确发出警告。
    - **测试**：新增文件 `tests/test_grok_provider.py`（24 个测试）。完整测试套件现有 **290 个测试**。
  - **已修复 Bug——英文多段落引文仅得到部分保护（`--news` 模式）**：`_NEWS_CITATION_REGEX` 只接受一系列**连续的** `>` 行作为引文正文。一旦引文跨越多个段落（中间由一个空的 `>` 行分隔），就只会捕获最后一段并将其替换为 placeholder；前面的段落会被发送给 LLM 并翻译后返回——这与 `--news` 存在的目的完全相反。现在，重复结构会接受内部空的 `>` 行，并改为非贪婪模式，以便在斜体行之前的那个空 `>` 处停止，而不是遇到第一个空行就停止。
    - **实测影响范围**：在包含 198 篇文章的真实语料库中，419 条引文里有 11 条受到影响。没有回归——新 regex 捕获的引文数量完全相同，只有多段落正文得到了扩展（408 个正文相同，11 个扩展），而署名行 `> — …` 仍然不可能被吸收到正文中（保留了 lookahead）。
    - **端到端证据**：在一篇 69 kB、翻译为 ja/ar 的文章中，一条引文的第一段过去会在日语中呈现为 `> GLM-5.3がオープンウェイト化。`，在阿拉伯语中也同样被翻译；现在则保持为 `> GLM-5.3 is now open-weight.`。英文引文的行数从 9 恢复到 10，与源文一致。
    - 需要注意的是，下游 validator 无法检测到这个缺陷，因为它们只检查引文是否存在，而不检查其内容是否完整。
  - **默认 provider 上经测量确认的成本节省**：只要模型名称以 `gpt-5` 开头，`_openai_extra_kwargs` 就会发送 `reasoning_effort="medium"`，即使处于 `--eco` 模式也不例外。使用 `gpt-5.4-mini` 翻译一个十词句子的测量结果：`medium` → 45 个 reasoning token 和 65 个输出 token；`none` → 0 和 14。reasoning 对翻译毫无帮助，却要为每个文件的每个 segment 付费。现在，在 `--eco` 中默认值改为 `none`，其他情况下仍为 `medium`；通过 CLI 显式传入的值仍具有最高优先级。除了 `low`/`medium`/`high` 外，`--reasoning_effort` 现在还接受 `none` 和 `xhigh`（并非所有模型都接受全部取值：例如 `minimal` 会被 `gpt-5.4-mini` 拒绝——现有的无参数重试机制会覆盖这种情况）。
  - **SDK 更新与 Gemini 迁移**：`google-generativeai`（支持已于 2025-11-30 结束，仓库已归档）被统一 SDK **`google-genai`** 取代——先使用 `genai.Client(api_key=...)`，再使用 `client.models.generate_content(model=, contents=, config=)`，system prompt 通过 `system_instruction` 传递，而不再与 segment 拼接。`mistralai` 升级到 **2.9.4**（import 改为 `from mistralai.client import Mistral`；旧形式会抛出 `ImportError`，已在 wheel 中验证），`anthropic` 升级到 **0.125.0**，`openai` 升级到 **2.54.0**——这些是在切换到 `httpx2` 之前的最后版本，避免在 venv 中同时保留两套 HTTP stack。`httpx` 0.28.1 和 `pydantic` 2.13.5 也因此解除版本锁定。
  - **两个由真实测试而非文档捕获的回归问题**：
    - `anthropic` ≥ 1.0 会在客户端拒绝非 streaming 调用，若其 `max_tokens` 显示该调用可能持续超过 10 分钟（`ValueError: Streaming is required...`）。这一防护在 0.34.2 中并不存在，并导致所有带 `max_tokens=32768` 的 Claude 调用失败。现已通过显式设置 `timeout`（`CLAUDE_TIMEOUT`，默认 900 秒）修复，从而避免为了一个只使用完整响应的调用切换到 streaming。
    - 只有部分 Gemini 模型目录接受 `thinking_level="minimal"`：`gemini-3.1-flash-lite` 支持它，而 `gemini-3.7-flash` 和 `gemini-3.1-pro-preview` 会以 400 拒绝。因此新增 `_gemini_generate_with_fallback`，形成 `minimal` → `low` → 不使用 thinking_config 的 cascade，其模式与现有 OpenAI fallback 相同——优化参数绝不能导致翻译失败。
  - **默认模型已更新**，每个模型都通过真实调用验证：OpenAI `gpt-5.5` → **`gpt-5.6-terra`**（28 个项目的 batch 成本降低 60%），`gpt-5.4-mini` → **`gpt-5.6-luna`**（降低 73%）；Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**（更便宜且更新），`claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（不含日期的规范 ID）；Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**，`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（稳定版本，且比 `3.5-flash-lite` 更便宜）。
 Mistral 保持不变，`mistral-large-latest` 仍是四者中性价比最高的。需要注意：不存在比 `gemini-3.1-pro-preview` 更新的 Gemini Pro 系列模型——2026 年 5 月宣布的 Gemini 3.5 Pro 从未发布；3.5/3.6/3.7 系列仅有 Flash。
  - **切换 Gemini 前进行实测 A/B 测试**：`README.md` 先后通过 `gemini-3.1-pro-preview` 和 `gemini-3.7-flash` 翻译成日语。结构严格一致（21 个列表、18 个代码块、13 个 HTML 链接、13 张图片，所有 URL 均得到保留），耗时分别为 **8 秒和 48 秒**。由于没有任何公开基准测试比较这两个模型在翻译或非拉丁文字方面的表现，否则此次切换只能基于简单推测。
  - **Claude 响应块过滤**：`_call_claude` 在不筛选类型的情况下执行 `block.text for block in response.content`。采用自适应推理的模型（Sonnet 5 及更高版本）会插入一个 `thinking` 块，该块提供 `.thinking` 而非 `.text`——翻译会在首个片段遇到不透明的 `AttributeError` 时失败。现在会排除 `thinking`、`redacted_thinking`、`tool_use` 和 `tool_result` 块（采用排除列表，以便仍能容忍携带文本的未知类型），而完全不含文本块的响应会引发明确错误。每次调用都会传入 `thinking={"type": "disabled"}`。
  - **重新同步 `MODEL_TOKEN_LIMITS`**：移除退役日期已过的模型（`magistral-*` 系列已于 2026-07-31 退役，`gemini-2.0-*` 于 2026-06-01 退役，`gemini-3-pro-preview` 于 2026-03-09 退役，以及 `claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。修正限制：Mistral 128K → **256K**（Large 3 / Small 4 代）、Gemini 1 000 000 → **1 048 576**（实际输入限制）、`claude-opus-4-5` 200K → **1M**、`gpt-5.6-*` 系列 400K → **1.05M**。新增 Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest` 和 `ministral-*` 系列。需要注意：这些限制仍仅供参考，因为 `translate()` 会将分段上限设为 `min(16000, limite)`。

  - **Provider `--use_codex`**：第五个 provider，通过非交互模式驱动官方 Codex CLI（`codex exec`），而不是调用按量计费的 API。翻译用量从已经付费的 ChatGPT 订阅配额中扣除。这是 OpenAI 针对此用途记录的唯一方式：各方案的可用性矩阵将“Codex SDK、`codex exec` 和可编写脚本的工作流”列为 Plus/Pro/Business/Enterprise 可用功能，而 `~/.codex/auth.json` 的 token 无法验证 API Platform 调用（此脚本也从不读取它们——身份验证及其刷新仍由 CLI 管理）。
  - **Codex 二进制文件可通过 pip 安装，不再仅限于 npm**：`_resolve_codex_binary()` 依次在 `CODEX_BIN`、`PATH`，然后在 OpenAI 发布的官方 Python 包 **`openai-codex-cli-bin`**（它是 `openai-codex` SDK 的依赖项）中查找二进制文件。因此，Python 项目无需再进行全局 npm 安装即可使用 `--use_codex`。该包未添加到 `requirements.txt`：二进制文件约为 250 MB，若加入其中，会迫使所有用户为一个可选 provider 安装它。已完成端到端验证：当 `codex` 不在 `PATH` 中时，解析流程能够找到打包的二进制文件，并在 6 秒内完成完整翻译。
  - **“订阅模式”保障**：从子进程环境中移除 `OPENAI_API_KEY` 和 `CODEX_API_KEY`。如果没有这层保护，`.env` 中存在的密钥可能会让 Codex 在没有任何可见提示的情况下切换到按量计费——而避免这种情况正是此 provider 存在的目的。
  - **通过测试锁定 CLI 陷阱**：
    - 即使提示词作为参数传入，`codex exec` 也会读取标准输入：如果不关闭标准输入，命令会一直等待到超时，且永远不会调用模型（复现结果：180 秒后以退出码 124 退出，输出零字节）。因此必须使用 `communicate(input=...)`。
    - 通过 npm 安装的 `codex` 是一个 Node 垫片，它通过 `spawn` 启动真正的 Rust 二进制文件：后者是 Python 进程的**孙进程**，会在对 `subprocess.run(timeout=)` 执行 `SIGKILL` 后继续存活，并持续消耗配额。因此需要 `Popen(start_new_session=True)` + `os.killpg`。
    - CLI 即使发出了 `turn.failed`，仍可能以退出码 0 结束：除了返回码，还会检查 JSONL 输出（`--json`）；若返回码为 0 但不存在 `-o` 文件，则会引发明确错误，而不是生成空片段。
  - **触发速率限制时进行退避**：CLI 未实现任何内部重试机制（`max_retries = 0`）。分类依据 JSON 载荷结构（`status: 429` / `error.type`），而非子字符串——“quota”一词既会出现在可恢复的 429 错误中，也会出现在永久性的 `insufficient_quota` 中。
  - **CI 防护**：如果定义了 `CI` 或 `GITHUB_ACTIONS`，则拒绝 `--use_codex`。订阅身份验证不适用于共享 runner，OpenAI 也明确不建议在公共仓库中采用此工作流。
  - **模型**：`gpt-5.6-sol`（质量）和 `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` 系列由 CLI 和 API Platform 共用，但 ChatGPT 账户无权使用其中所有模型：允许列表由服务器端执行，不进行本地验证，使用不常见的模型会触发警告。在 Plus 方案下，每个 5 小时窗口中，Luna 可提供 250–2 000 条消息，而 Sol 仅有 10–100 条：`--eco` 是所有批处理任务的推荐模式。
  - **已修复缺陷——`regen_translations.sh` 在完全成功后仍以错误退出**：`trap ... EXIT` 引用了 `failed_log`，后者是 `main()` 中的 `local` 变量，但 trap 执行时该变量已经不存在。在 `set -u` 下，这会引发 `failed_log: unbound variable`，导致脚本以状态码 1 退出，尽管 28 项翻译均正确完成——这会使 `release.sh --auto`（`set -e`）在重新生成后、也就是成本最高的阶段立即中断。该变量现已改为全局变量，trap 会检查它是否存在。一个有益的副作用是：此前被此错误掩盖的真实翻译失败，现在会再次显示在最终摘要中。
  - **`REGEN_MODEL`**：`regen_translations.sh` 新增的环境变量，可覆盖 provider 默认值并强制使用指定模型，例如使用 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`，以便通过订阅配额中的高端模型重新生成，而非使用面向大吞吐量的 `--eco` 模型。
  - **`regen_translations.sh`**：`REGEN_PROVIDER=codex` 可通过显式选择启用（绝不自动检测，以免在用户不知情的情况下消耗订阅配额）。在启用并行处理前，会先按顺序刷新一次 token——由于 Codex 的刷新机制采用轮换且只能使用一次，并发任务会使 `codex login` 会话失效——并发数也会降至 4。
  - **相关重构**：`_dispatch_provider_call` 通过返回 provider 名称的 `_resolve_provider()`，将参数数量从 8 个减少到 6 个，不再让第四个布尔值贯穿整个调用链。为保留调用 `translate(..., use_mistral=True)` 时仅提供最小 `Namespace` 的测试，显式布尔值仍优先于 `args`。
  - **测试**：新增文件 `tests/test_codex_provider.py`（48 项测试），覆盖 argv、清理后的环境、禁止前言的契约、静默失败、超时/killpg、退避、预检、provider 解析、Gemini 推理级联、Claude 块过滤和多段新闻引用。完整测试套件共 290 项测试。
  - **真实验证**：项目的 `README.md` 通过 Codex 翻译成 **14 种语言**后，其结构与参考译文严格一致（14 个代码块、24 个标题、25 行表格、13 个 HTML 链接、13 张图片、19 个 URL，代码块逐字符一致，placeholder 零残留）。对于一篇 69 KB 的新闻文章，在 `--news` 模式下，`gpt-5.6-luna` 和 `gpt-5.6-sol` 的输出均通过了下游应用针对 en/ja/ar 的验证器。通过 `account/rateLimits/read` 测得的消耗量：在 `--eco` 模式下始终低于计数器的舍入阈值（5 小时窗口的 0%）。

- **1.9.2** 修复带嵌套括号或法语前缀的新闻署名 URL 提取问题（2026-05-11）：

  - **已修复缺陷**：`_protect_news_quotes` 中的署名 URL 提取使用正则表达式 `re.search(r"\((.+?)\)", attribution)`（对括号内内容进行惰性捕获）。对于 `(relayé par [@user sur X](https://x.com/.../123))` 形式的署名（嵌套括号：外层 `(` + Markdown 链接中的 `]()`），捕获会在遇到第一个 `)` 时停止 → 字符串被截断且包含法语前缀：`relayé par [@user sur X](https://x.com/.../123`（缺少末尾的 `)`）。结果是：`_validate_news_post` 会在翻译输出中查找该字符串并必然失败（原因有二：`)` 被截断，且“relayé par”会被翻译成 `relayed by`/`weitergeleitet von`/……）。从 low → medium → high → gpt-5.5 的完整级联均无法通过。
  - **修复**：正则表达式改为 `re.search(r"\]\(([^)]+)\)", attribution)`——专门匹配 Markdown 链接中的 `](url)`，并且**仅捕获纯 URL**（不含法语前缀且不会截断）；翻译期间由 placeholder `#URL{N}#` 保持其不变。对以下两种问题模式均具有稳健性：
    - `(relayé par [@account sur X](url))`——嵌套括号
    - `via [@source](url)` 或 `selon [@author](url)`——不含外层括号的法语前缀
  - **测试**：在 `test_silent_failure.py` 的 `TestNewsCitationExtraction` 类中新增 2 项测试：
    - `test_extract_attribution_url_with_nested_parens`（精确复现 Genspark CEO E2B 缺陷的案例）
    - `test_extract_attribution_url_with_french_prefix`（包含 `via` 的变体）
  - **覆盖缺口**：`check-editorial-coverage.py` 会验证编辑语法，但不会验证 translator 是否能够翻译。一项可能的改进（不属于 v1.9.2 范围）是增加一个检查，通过 dry-run 模拟署名提取，以便在发布**之前**检测高风险模式。

- **1.9.1** 修复翻译标记注释中的 CTA 标签国际化问题（2026-05-10）：

  - **已修复缺陷**：翻译文件顶部标记横幅中 CTA 链接的 `[Voir le projet sur GitHub ↗]` 标签，在所有目标语言中仍然**使用法语**，而没有遵循 `target_lang`。LLM 从未看到它（它由 Python 端组装，以保留仓库的 URL 和 slug），因此翻译阶段无法补救。自 v1.9 加入 `marker` 格式以来，这一直是一个静默回归问题。
  - **修复**：新增常量 `_VIEW_PROJECT_LABELS`，将 15 种语言映射到各自的本地化标签。`_translation_note_invariants(target_lang)` 和 `_assemble_translation_note_paragraphs(phrase, target_lang)` 现在会传递目标语言。若语言未知，则回退到 `fr`（安全措施，避免 KeyError）。
  - **测试**：调整 `test_source_emits_three_paragraphs_repo_title_description_link`（目标语言 `ja` → 预期为日语标签）。新增 2 项测试：`test_source_link_label_localized_per_target_lang`（针对 7 种语言进行参数化，覆盖拉丁文字、表意文字和辅音音素文字）以及 `test_source_link_label_falls_back_to_french_for_unknown_target`。`test_translation_note_position.py` 中的测试总数为 40 项（此前为 38 项）。
  - **向后兼容性**：签名提供默认值 `target_lang="fr"`——未传入 `args.target_lang` 的外部程序调用方无需修改即可继续运行。
- **1.9** 修复静默失败问题 + 完整质量工具链 + 多位置翻译说明（2026-05-07）：
  - **多位置翻译说明 + “embed card”标记格式**：
    - 新增 CLI 选项（仅增补，默认行为不变 → **非破坏性变更**）：
      - `--note_position {top,bottom,both}`（默认值：`bottom`）：将说明放置在译文文件的顶部、底部或同时放置在两处。
      - `--note_format {legacy,marker}`（默认值：`legacy`）：
        - `legacy` 严格复现 v1.8 的行为（粗体段落 `**…**`），**逐字节完全一致**。
        - `marker` 会生成一个不可见的 Markdown 链接引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），后接一个结构化的**三段式 blockquote**，以呈现类似“GitHub 仓库嵌入卡片”的效果：使用行内代码显示项目标题（`**\`ai-powered-markdown-translator\`\*\*`）、由 LLM 翻译的描述，以及带可见箭头的 CTA 链接（`[Voir le projet sur GitHub ↗](URL)`）。构建时可由 remark 插件处理（参见 jls42.org 博客 → 插件 `remark-translation-banner`）。
    - **绝不发送给 LLM 的不变量**：仓库标题和 GitHub URL 会在描述性语句翻译完成后由 Python 端组装。LLM 永远不会看到 slug `ai-powered-markdown-translator` 或 `https://github.com/jls42/...`，从而确保 renderer、大小写或 scheme 均不会被修改。
    - **感知 frontmatter 的插入机制**：在 `top` 或 `both` 模式下，说明会插入到 YAML frontmatter 结束标记 `---` **之后**（确保兼容 Astro Content Collections / gray-matter）。辅助函数 `_split_frontmatter` 会检测文件开头的 `---\n…\n---\n` 并保持其完整性；如果 frontmatter 已开启但缺少结束 fence，则会**抛出 `RuntimeError`**（该文件会被列入 `failed_files`，而不会写入位置错误的说明）。
    - **基于白名单的模型名称 sanitizer**：`_sanitize_model` 会将 `[A-Za-z0-9._:/-]` 以外的所有字符替换为 `_`，为空时回退到 `unknown`。此规则与 Astro remark 插件端的验证器保持一致，并中和可能破坏标记格式的字符（空格、引号、括号、逗号等）。
    - **内部重构**：`_append_translation_note`（1 个单体函数）→ 7 个纯辅助函数（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。builder 与 composer 分离（builder 返回不含分隔符的纯块，composer 根据位置应用 `\n\n`）；生产代码和源辅助函数共用同一个三段式组装器。
    - **`_quote_lines` 保留空行**：为每一行添加 `> ` 前缀，并将空行转换为单独的 `>`。这样，mdast 会将 blockquote 识别为 3 个独立段落（标题／描述／链接），而非一个包含换行的段落。
    - **自适应 `_build_translation_note_block`**：根据 LLM 保留的段落数量处理（3 段 = 完整卡片格式，2 段 = 语句 + 链接，1 段 = 回退格式）。检测到 Markdown 链接 `](` 时，单段回退格式**不再使用 `**...**` 包裹**（在链接周围使用 `<strong>` 的渲染效果不稳定）。
    - **向后兼容**：在 `_compose_with_notes` 端使用 `getattr(args, "note_position", "bottom")` 和 `getattr(args, "note_format", "legacy")`——缺少这些属性的 Namespace（现有测试、外部程序化调用）无需修改即可继续运行。
  - **修复长文本翻译中的静默失败问题**：
    - 对所有 provider（OpenAI、Mistral、Claude、Gemini）执行译后语言验证：确定性层（在结果中逐字查找源文本片段）+ 概率性层（`langdetect`）
    - `finish_reason` / `stop_reason` 白名单：遇到白名单以外的任何状态（截断、content_filter 等）均抛出 `RuntimeError`
    - Claude 的 `max_tokens`：`4096` → `32768`（避免 16k 分段中的隐性截断，并为 FR→JA/ZH/KO/AR/HI 跨文字系统转换预留空间）
    - 感知 heading 的分段：优先选择分段后半部分的 H2/H3（使每个分段都从完整的语义章节开始）
    - 将错误传播至非零退出码：`translate_markdown_file` 返回类型化状态 `success` / `failure` / `skipped`；只要至少一个文件失败，`main()` 就会执行 `sys.exit(1)`（单文件与批处理均适用）
    - 所有 provider 均添加空内容 guard、源文本／输出合理性比例检查（源文本 ≥ 500 个字符且输出少于 5% 时拒绝）、代码 placeholder 验证（`#CODEBLOCK`/`#INLINECODE`）、LLM 后规范化处理（分隔符或链接与 heading 粘连），以及不使用 `reasoning_effort` 的 `BadRequestError` 重试
    - 新增依赖项 `langdetect==1.0.9`
  - **pre-commit 质量工具链**（“完整 EurekAI 类型”，14 个 hook）：
    - Pre-commit：ruff（lint + format）、shellcheck、prettier（md/yaml/json）、detect-secrets（保护 4 个 API key）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（空白字符、EOF、大文件、shebang 等）
    - Pre-push：mypy（渐进式宽松模式）、Opengrep SAST（translate.py + scripts/）、pip-audit（初始 reporting 模式）、unittest discover（tests/ + scripts/tests/）
    - `scripts/` 中使用 `./venv/bin/python` 的本地 wrapper
    - `scripts/audit_verdict.py`：包含 11 个 unittest 的 pip-audit JSON parser，是根据 jls42-astro parser 改写的 Python 移植版本
    - 修复了 7 个初始 ruff 违规：B904（raise from）×2、B007（未使用的 dirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizard 暂时排除 `translate.py`（4 个函数的 CCN 为 21–47，已计划重构）——对 scripts/ 实施严格 gate
  - **SonarCloud + 全面覆盖率**：
    - GitHub Actions 工作流 `SonarCloud`（sonarcloud.yml + sonar-project.properties）：每次 push 和 pull-request 时执行分析，通过 `coverage.xml` 获取 coverage
    - README 顶部添加 11 个 SonarCloud badge（Quality Gate、Security/Reliability/Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）
    - `tests/test_silent_failure.py`（`unittest` 标准库）：覆盖静默失败错误链的全部六个环节
    - `tests/test_orchestration.py`（新增 79 个测试）：覆盖 `translate.py` 的 orchestration 层（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` 的 TypeError + BadRequestError 回退逻辑、o1 系列 prompt 格式，以及 `_validate_translation_output` 的 early-return 分支）
    - `scripts/tests/test_audit_verdict.py`：通过 subprocess 覆盖 `main()`（stdin/stdout）和 `if __name__ == "__main__"` 块
    - **新代码覆盖率**：75.5% → 约 98%（translate.py 为 98%，scripts/audit_verdict.py 为 97%）
  - **测试**：`tests/test_translation_note_position.py` 覆盖位置 × 格式矩阵（包括端到端测试 `marker+top|bottom|both` 和 `legacy+top|bottom|both`）、多行前缀处理、逐字节向后兼容性（golden literal）、sanitizer、frontmatter 拆分（包括未闭合 fence 时抛出异常）、三段式格式、两段式回退格式、单段 + Markdown 链接 guard，以及关键防护测试 `TestLLMPayloadExcludesInvariants`，用于断言标题和 URL 绝不会发送给 LLM。**190 个测试全部通过**，0 个回归问题。
  - 文档：`README.md`（法语 + 14 种翻译），包含 badge；`CLAUDE.md`（pre-commit 工作流 + 详细 CI 监控说明）；重新生成 28 种翻译
- **1.8** `--news` 模式 + 2026 模型升级（2026-03-17，tag `v1.8`）：
  - 更新默认模型（2026 年 3 月）：
    - OpenAI 高质量：`gpt-5` → `gpt-5.4`
    - OpenAI 经济型：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 高质量：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - 新增 `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）和 `gemini-3.1-pro-preview`（1M）的 token 限制
  - 初始 `--news` 模式：使用 placeholder `#NEWSQUOTE\d+#` 保护英文引文，提供 `LANG_FLAGS` 映射（15 种语言），并根据目标语言处理旗帜
  - 在恢复 news placeholder 前进行验证（回归问题：LLM 删除 placeholder 时，会静默生成缺失引文的输出）
  - 将脚本 `regen_translations.sh` 改为可移植形式（使用绝对路径，不依赖 pwd）
  - 在 README/CHANGELOG 的语言栏中添加法语链接，并重新生成 28 种翻译
- **1.7** 新功能：
  - 新增 `--keep_filename` 选项，可在翻译时保留原始文件名
  - 支持通过 `.env` 文件自动加载 API key
  - **保留行内代码**：翻译期间现会保护反引号（`` `...` ``）中的内容
  - 改进系统 prompt：
    - 更好地处理 YAML frontmatter 中的引号
    - 保护 template 变量 `{variable}`
    - 禁止添加未经请求的译者注
  - 已在 364 个文件上成功测试（jls42.org 博客迁移）
- **1.6** 新功能：
  - 支持使用 Google Gemini API 进行翻译（`--use_gemini`）
  - 更新 2026 年默认模型：
    - OpenAI：`gpt-5`（高质量）、`gpt-5-mini`（经济型）
    - Claude：`claude-sonnet-4-5`（高质量）、`claude-haiku-4-5`（经济型）
    - Gemini：`gemini-3-pro-preview`（高质量）、`gemini-3-flash-preview`（经济型）
  - 经济模式（`--eco`），用于采用更快且成本更低的模型
  - 支持翻译单个文件（`--file`），无需遍历目录
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
    - 直接翻译和翻译说明所使用的 prompt 得到增强，以提升清晰度和效率，其中包含有关保留元数据及特定格式元素的详细指令。
  - **代码重构：**
    - 使用 `Mistral` 类替换 `MistralClient`，以初始化 Mistral AI 客户端。
    - 重新组织 import，以提高可读性和可维护性。
    - 改进文本分段和代码块处理，以在翻译期间保留原始格式。
  - **输出文件管理：**
    - 在输出文件名中对调模型和语言的位置（例如 `f"{base}-{args.target_lang}-{args.model}.md"`），从而更便于组织和查找译文。
  - **其他改进：**
    - 删除不必要的空行以清理代码。
    - 进行小幅调整，以改善脚本结构和可读性。
- **1.4** 新功能：
  - 支持使用 Anthropic Claude API 进行翻译
  - 优化 prompt，以提升清晰度和效率
  - 进行小幅调整，以提高代码可维护性
- **1.3** 改进与新功能：
  - 改进代码块处理
  - 改进输出文件管理
  - 改进现有文件检测
  - 新增 `--force` 选项，用于强制执行翻译
  - 在输出文件名中对调模型和语言的位置
- **1.2** 修复 changelog
- **1.1** 新增 Mistral AI API 支持
- **1.0** 初始版本——支持 OpenAI API

**使用 gpt-5.6-sol 将文章从法语翻译成中文。**
