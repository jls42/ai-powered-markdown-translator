### 变更日志

🌍 [Français](CHANGELOG.md) | [English](CHANGELOG-en.md) | [Español](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [Deutsch](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [한국어](CHANGELOG-ko.md) | [العربية](CHANGELOG-ar.md) | [हिन्दी](CHANGELOG-hi.md) | [Italiano](CHANGELOG-it.md) | [Nederlands](CHANGELOG-nl.md) | [Polski](CHANGELOG-pl.md) | [Português](CHANGELOG-pt.md) | [Română](CHANGELOG-ro.md) | [Svenska](CHANGELOG-sv.md)

- **1.12.0** Provider `--use_opencode`：OpenCode，这个开源代理，可连接到用户选择的提供商——本地模型、无需账户即可免费使用、订阅服务或密钥（2026-09-04）：

  - **第八条 provider 路径，与前七条性质不同。** [OpenCode](https://opencode.ai)（MIT）不是模型提供商，而是一个 _路由器_，用于连接用户在 OpenCode 中自行配置的提供商：API 密钥、订阅服务（GitHub Copilot、ChatGPT、SuperGrok）、OpenCode Zen 网关——提供**无需账户**的免费模型——或**本地**模型（Ollama、LM Studio、llama.cpp）。该脚本以非交互模式驱动 `opencode run`，就像驱动 Codex 和 Grok 一样，并复用相同的子进程基础设施（独立进程组、超时后执行 `SIGTERM` 再执行 `SIGKILL`、始终关闭 stdin、清理后的环境）。已通过**两次真实翻译**验证：使用 `opencode/mimo-v2.5-free` 将整个 README 翻译成英语——49 秒、单次处理、结构与源文件一致（32 个标题、26 个代码块结束标记、18 个链接、37 个 URL、37 行表格、135 个行内代码）——以及使用 `ollama/qwen2.5:7b` 在本地翻译一个测试文件，全程无需任何密钥。

  - **`--model provider/modèle` 是必需的，这是有意为之。** 如果没有 `--model`，OpenCode 会退回自身的默认设置；在全新安装中，该设置是 `opencode/big-pickle`，一种免费的“stealth”模型，其交互内容可能被用于训练——实际测量表明，正是该模型作出了回答。静默地替用户选择它，恰好属于本仓库所要防范的那种不可见切换；因此错误消息会列出用于显示模型的命令（`opencode models`）以及三个示例（本地、免费、订阅）。`--eco` 不产生任何效果，并会明确说明这一点。只有在明确请求时，`--reasoning_effort` 才会原样作为 OpenCode 的 `--variant` 传递。

  - **经过测量的隔离，而非想当然的隔离。** 内联配置（`OPENCODE_CONFIG_CONTENT`，在 OpenCode 的合并顺序中最后出现，因此优先于用户配置但不会替换它）定义了一个 `aipmt` 代理，并拒绝其所有工具（`permission: {"*": "deny"}`）：注册表甚至不会再向模型提供这些工具；当被要求“列出文件并运行 `id`”时，模型会回答自己没有工具。会话共享已禁用，外部插件已排除（`--pure`），绝不会使用 `--auto`，工作目录为一次性且空的目录。已测量并切断两种静默注入：没有 `OPENCODE_DISABLE_CLAUDE_CODE` 时，用户的 `~/.claude/CLAUDE.md` 会进入**每个**提示词（对于简单的“你好”，输入从 186 个 token 增至 515 个）；没有 `OPENCODE_DISABLE_PROJECT_CONFIG` 时，当前目录的 `AGENTS.md` 也会被注入——“每次回答都以 BANANA 结尾”的指令曾实际影响翻译。全局 `~/.config/opencode/AGENTS.md` 仍会被注入：没有任何开关可以将其排除，而通过篡改后的 `XDG_CONFIG_HOME` 绕过它也会同时隐藏用户的提供商。对此进行记录，而不是临时拼凑。

  - **`exit 0` 并不能证明任何事情，这是第三个 CLI，仍需遵循相同原则——但它有两个特有陷阱。** 未知的 `--agent` 不会导致 `opencode run` 失败：它只会在 stderr 上发出警告，并**静默**退回编码代理，且工具处于启用状态。如果内联配置未被采用，翻译就会由一个能够写入文件的代理执行；因此输出契约除了检查返回码为 0、没有 `error` 事件、没有 `tool_use`、最后一个 `step_finish` 为 `stop`（`length` 表示截断的响应）、文本非空之外，还会验证不存在这条消息。第二个陷阱：错误 JSON 事件是**不透明的**——“Unexpected server error. Check server logs for details.”，只带有一个简单引用——而真正的原因（`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`、`ProviderAuthError`……）只存在于日志中。因此需要使用 `--print-logs --log-level ERROR` 并读取 stderr 的 `error="…"` 字段，同时排除其后的 Bun 跟踪信息。这样，未知模型会在一秒内失败，并明确指出原因。`--title` 还可避免一次多余的 LLM 调用：没有它时，OpenCode 会在 `small_model` 上额外执行一轮，为会话生成标题。

  - **密钥：与 Codex 和 Grok 使用相同的模式过滤，仅有一个具名例外。** `OPENCODE_API_KEY` 会被保留：它是 OpenCode 自身的密钥（Zen 网关、Go 订阅），通过名称传递给 OpenCode——相当于它的 `auth.json`，不是 aipmt 管理或能够计费的密钥。提供商在 OpenCode 中配置（`opencode auth login`、`opencode.json`），绝不会配置在 aipmt 的 `.env` 中，aipmt 的任何密钥都不会到达子进程。与订阅 CLI 不同，CI 中不会拒绝：运行器上的 API 密钥或自托管模型都是合法用法。

  - **防遍历保护现在检查插值后的值，而不是原始值。** `provider/modèle` 包含一个 `/`，1.10.0 中的保护会拒绝它——这是合理的，因为 `--model` 会被插入文件名 `--include_model` 中。现在，文件名标签会在任何插值之前将 `/`、`\` 和 `:` 替换为 `-`（`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`，其中 `:` 在 Windows 下非法），上游保护检查的也是这个标签：在目标路径下，`../../evil` 变成简单的名称 `doc-en-..-..-evil.md`，只有 `..` 仍会被拒绝，`--target_lang ../x` 也同样会被拒绝。范围保护 `_ensure_within_directory` 仍是第二层，保持不变。

  - **免费模型和本地模型：测量结果。** `opencode/mimo-v2.5-free` 用时 16 秒翻译一个段落、49 秒翻译整个 README；`opencode/big-pickle` 翻译 200 个词需要 40 秒，而两个并发请求在单独请求都能完成的情况下，持续 5 分钟仍无响应；`opencode/nemotron-3.5-lightning-free` 在 3 分钟内没有任何响应。因此使用 `REGEN_PROVIDER=opencode`，强制要求 `REGEN_MODEL`，并行执行 **2 个任务**。在本地方面，Ollama 通常将上下文设置为 4,096 个 token，而分段最长可达 16,000 个字符：因此必须使用带有 `PARAMETER num_ctx 32768` 的 `Modelfile`，质量则取决于模型——测试文件中，一个 7B 模型颠倒了列表并破坏了代码块结束标记，而网关模型完整保留了所有内容。

  - **速率限制退避已被提取复用**（`_retry_on_rate_limit`）：Codex 和 Grok 的循环除了文案不同外完全相同，再复制第三份就会超过重复代码阈值。三个 CLI 错误都来自同一个 `_CliCallError`；有一项测试禁止其中任何一个脱离该抽象，否则共享循环将无法再捕获它。

  - **测试**：新增文件 `tests/test_opencode_provider.py`（51 项测试）——完整输出契约、代理回退、从日志读取原因、去重文本片段并忽略合成片段、超时终止进程组、429 退避、模型必需且经过验证、无密钥预检、二进制文件解析、分发连接、文件名标签以及遍历反例。`tests/test_review_hardening.py` 将 flags 的互斥性和无密钥检查扩展到新的 provider。质量门现在要求记录在案的 **22 个 argparse flags**。完整测试套件共 **382 项测试**。

- **1.11.1** 文档修复：README 终于列出了七条 provider 路径（2026-09-03）：

  - **1.11.0 的 PyPI 页面写着“4 APIs + Codex CLI”。** 代码实际提供七种方式——通过 API 使用 OpenAI、Mistral、Claude、Gemini 和 Grok；通过订阅使用 Codex（ChatGPT）和 Grok，不按使用量计费。Grok 的两种模式遗漏在简介和 _Multi-Provider_ 项目中，14 种翻译也重复了这一错误。由于软件包的长描述会按版本固定，修正展示页面必须使用新的版本号：这就是本版本存在的唯一原因。**没有代码变更。**
  - `CLAUDE.md` 已与发布内容保持一致：质量门计数器（16、`--full` 中的 17）、11 个活动工作流、`gh pr checks` 中不可见的两个 Sonar/Codacy 计数器（hotspots、Codacy API）、通过 `ruff-format` 移动一个 `# nosemgrep`、OIDC 交换所需的 GitHub 环境，以及 _pending publisher_ 不会占用名称这一事实。

- **1.11.0** 发布到 PyPI：先执行 `pip install ai-powered-markdown-translator`，再执行命令 `aipmt`，无需克隆仓库（2026-09-03）：

  - **单文件脚本变成可安装的软件包。** `translate.py` 从根目录移至 `src/aipmt/translate.py`，并提供控制台入口 `aipmt` 及等效的 `python -m aipmt`。克隆仓库仍是贡献所必需的——测试、28 种翻译和质量工具都在那里——但使用该工具时不再需要克隆仓库。

    - **导入名称是 `aipmt`，绝不能是 `translate`**，因为冲突真实存在且不会显式报错。PyPI 软件包 `translate`（v3.8.1，最近一次上传于 2026-07-06）会安装一个同名目录。在 venv 中复现后发现：目录会优先于模块，`translate.main` 消失，入口在 `AttributeError` 处崩溃——而 `pip check` 却以 rc=0 返回“No broken requirements found”。用户只需执行一次简单的 `pip install translate`，就足以在没有可用诊断的情况下破坏 CLI。针对实际 wheel 的反向验证：在软件包之上执行 `pip install translate`，前后 `aipmt --help` 均为 rc=0，两个 CLI 可以共存。
    - **发行名称较长，命令名称较短。** `ai-powered-markdown-translator` 使软件包能够通过 PyPI 搜索找到；如果只使用缩写，那么不了解项目的人将无法找到它，而该发布的目标正是让项目可被发现。两个看似合理的候选名称已通过验证排除：`ai-markdown-translator` 自 2024 年起已被 npm 上一个用途相同的工具占用，该工具比本仓库早 17 个月；`aimt` 与 `aim`（v3.29.1）只差一个字母，后者是同一领域中仍活跃的软件包——这是造成长期混淆的最糟糕配置。顺带说明一个方法论陷阱：`pypi.org/project/<nom>/` 对任何名称都会返回 200（反爬页面），只有 JSON API 才可信。
    - **采用 `src/` 布局，而不是扁平软件包。** 扁平软件包会保留测试中的六个 `sys.path.insert(..., "..")`，这恰恰是缺陷：它们会导入源代码树而不是软件包，从而掩盖任何打包错误。实际代价是增加一条替换规则。

  - **密钥终于可以一次配置、长期使用。** 安装后的 CLI 原本没有任何持久配置：只有环境变量和当前目录中的 `.env`。`find_dotenv` 确实会一路向上查找到系统根目录，因此**当在用户主目录下工作时**可以找到 `~/.env`，但在其他位置工作时什么也找不到——覆盖范围取决于从哪里运行命令，而不是设计选择。因此新增第三层：`~/.config/aipmt/.env`，位于原有两层之下。

    - **优先级并未硬编码**，而是由 `load_dotenv` 的默认值 `override=False` 推导而来：每一层只填充前一层留下的空缺。因此顺序为：环境变量 → 项目的 `.env` → 用户配置；该顺序通过行为测试而非结构测试验证——交换两个调用的顺序会导致测试失败，移除第三层也会失败。
    - **采用 `.env` 格式，而不是 TOML**，这是有意的：`python-dotenv` 已经是依赖项，语法已在 15 个 README 中记录，同一个文件也可用于两种作用域。不引入新的依赖或语法。位置遵循 `XDG_CONFIG_HOME`（前提是它是**绝对路径**）——规范要求忽略相对值，否则配置位置又会取决于当前目录——Windows 下则使用 `APPDATA`。
    - **排除了两个选项，并说明原因。** 系统密钥环（`keyring`）在桌面电脑上更安全，但在无头环境中会失败——服务器、容器、CI——而这正是批量翻译的使用场景；适合作为 opt-in，不适合作为默认方案。`--api-key` flag 会使密钥进入 shell 历史记录，并在 `ps` 中可见。
    - **没有密钥时，不再留下调用堆栈。** 用户之前会看到指向 `site-packages` 的 Python 调用堆栈，以及一条提到“环境或 .env”却没有说明第二个文件应在哪里创建的消息。现在会列出三个位置及其精确路径，并以状态码 2 退出。这个保护范围**刻意保持狭窄**：`except ValueError` 只作用于配置阶段。包住整个执行过程会把翻译期间真正发生的错误变成令人安心的消息——这正是本仓库要防范的失败模式。一项测试会读取 `main()` 的源代码来禁止这种做法。

  - **修复——安装工具后，用户的 `.env` 曾被忽略。** 不带参数的 `load_dotenv()` 并不会从当前目录向上查找，而是从**调用方文件**开始，因此从 `site-packages` 开始。通过一个从拥有自身 `.env` 的项目目录启动的真实控制台入口进行测量：`find_dotenv()` 返回 `''`，密钥未被加载；而 `find_dotenv(usecwd=True)` 可以找到它。只要工具仍从克隆的仓库中运行，这个 bug 就不存在；发布后它会变成系统性问题，唯一症状是在配置正确时仍显示 API 密钥“缺失”。

  - **三个质量门在停止检查任何内容后仍会变绿。** 它们在移动之前就已被有意加固：在变更之后才编写、声称能够捕获该变更的防护措施并不能证明任何事情。每个质量门在原始仓库上为绿色，在迁移副本上转为红色——两个方向都经过测量。

    - **Lizard 会默默忽略不存在的路径**：rc=0，并显示“0 file analyzed”。复杂度质量门会从 158 个函数 / 2247 个 nloc 变成 3 个函数 / 34 个 nloc，同时输出为零字节。现在 scope 是一个数组，每个条目都会检查其是否存在。
    - **对不存在模块执行 `coverage run --source=` 不会失败**：只有 stderr 上的警告；unittest 和 `coverage xml` 的 rc 都为 0，报告仍会发布——但从 1453 个 statements 缩减为 141 个。项目会显得健康，只因为几乎没有内容被分析。两个下限保护报告：总数，以及测量结果最大的文件。
    - **翻译新鲜度探针在结构上无法感知调用形式**：它锚定在 argparse flags 上，而文件重命名恰好不会改变这些 flags。复现结果是：模块被移动，15 个 README 仍在记录一个不存在的命令，但结论却是“没有过期翻译”。因此新增第 7 个部分，检查的是调用**形式**而非选项；同时让 Lizard hook 对照脚本的实际 scope——当其 `files:` 不再匹配时，不会让 pre-commit 失败，而是让它**跳过**。

  - **`requires-python = ">=3.10"` 不再只是声明。** `sonar-project.properties` 早已宣称支持 3.10-3.12，但从未真正运行过，因为开发机只有 3.12——这是一个会在发布后公开暴露的内部矛盾。现在新增测试工作流，在 3.10、3.11 和 3.12 上运行完整测试套件，并安装软件包本身，因此也会验证其公开支持范围。
- **下限，无上限。** `requirements.txt` 仍是经过测试的锁定文件，`[project.dependencies]` 成为公共契约：发布锁定文件中的精确版本会与任何安装了其他软件包的用户发生冲突。同样不设置 `<N+1` 上限——它会与 `check-deps-fresh.sh` 直接矛盾，后者会让任何主版本延迟都导致发布门禁失败。下限集合解决了这一问题，而反向测试 `openai==1.0.0` 输出 `ResolutionImpossible`，证明控制逻辑会进行区分，而不是全部接受。此外还有保护措施，禁止 `pyproject.toml` 的版本与 CHANGELOG 中的版本不一致：PyPI 不允许重复使用同一个版本号。

  - **在全新的 venv 中完成端到端验证**：约 70 Ko 的 wheel 只包含 `aipmt/*.py`、dist-info 和许可证；`aipmt --help` 返回 rc=0，并带有 22 个 flags；`python -m aipmt` 显示“usage: aipmt”，而不是“usage: \_\_main\_\_.py”；安装后的 `pipx` 可正常工作；最重要的是，**从任意用户目录执行真实的 fr→en 翻译**，粗体、列表、内联代码、链接和 URL 均得到保留，代码块未被翻译。迁移前的 318 个测试全部通过，迁移前后标识符列表逐字节完全一致——这才证明没有测试被禁用，而不是那个“OK”；此外还为三层配置新增 12 个测试，总数达到 330 个。

- **1.10.0** Provider `--use_codex`（ChatGPT 订阅配额）、SDK 和模型更新、修复多段 news 引用（2026-08-29）：

  - **安全审查——PR 添加了两个防护措施，却没有在所有地方贯彻**：

    - **Codex 预检将整个 `.env` 传递给二进制程序。** `_codex_preflight` 调用 `subprocess.run` 时**没有 `env=`**：子进程继承了完整的 `os.environ`，也就是由 `load_dotenv` 加载的全部 `.env`。使用经过插桩的伪二进制程序测量后发现：预检会接触到**七个 secret**——六个 provider 的密钥以及一个 `GITHUB_TOKEN`；而其对应的 `_grok_preflight` 则为**零个**，因为它正确地传入了 `env=_grok_env()`。这是 PR 内部的不一致：几行之外就有 `_strip_secret_env`，它正是用于维护这一不变量的。现在提取并由两条路径共享一个 `_codex_env_base()`；修复后测量结果为：两边均为 0 个 secret。
    - **“`--deny` fail-closed”这一属性并未覆盖实际采用的形式。** 注释以“未知前缀规则会拒绝启动”为由，说明了 Grok 的全部隔离机制。但在 `grok 1.0.13` 上测量发现，这项验证**仅适用于带括号的形式**：`--deny 'CeciNestPasUnOutil(*)'` 会拒绝启动（“unknown tool prefix”），而 `--deny 'CeciNestPasUnOutil'` 则会被静默接受。然而 `GROK_DENY_RULES` 只使用了裸名称——因此，如果 xAI 一侧重命名工具，唯一经过测量的隔离层就会在毫无提示的情况下被移除，而此时操作系统 sandbox 本来就不适用。八条具名规则现在以 `Prefix(*)` 通过，每条都已验证为 CLI 的已知前缀；catch-all `*` 保持字面形式，这是唯一被接受的形式。一个测试可防止退回未经验证的形式。
    - **其他方面已完成干净验证**：不存在命令注入（处处使用列表形式，从不使用 `shell=True`；文档内容通过 stdin 或 `--prompt-file` 传递），不存在不安全反序列化（仅使用 `json.loads`，并带有类型保护），路径遍历修复在七组 payload 上均未发现绕过方式，并且 `--deny '*'` 确实由 CLI 应用（在 workdir 外读取时观察到 `DENY_ENFORCED`）。
    - 上文新增的新鲜度检查顺带绕过了自身原则：当某个软件包的 PyPI 请求失败时，它会被静默跳过，门禁仍显示绿色。现在会统计实际完成比较的软件包数量，并在覆盖范围不完整时失败。

  - **依赖已升级，并加入两道防线以防止延迟再次发生**：

    - **延迟确实存在且持续时间很长**：`openai` 从 2.54 → **3.6.0**，`anthropic` 从 0.125 → **1.2.0**，`certifi` 从 2024.8.30 → **2026.7.22**——负责验证所有 provider TLS 调用的根证书存储落后了两年。原因已确定：**不存在 `.github/dependabot.yml`**。没有该文件时，GitHub 只启用 _security updates_，Dependabot 只有在依赖受到 CVE 影响时才会提出 PR——这解释了它为何升级了 `urllib3` 和 `idna`，却任由两个 SDK 偏离一个主版本。
    - **两个主版本可以无冲突共存**，与先前推理所担心的情况不同：`openai` 3.x 和 `anthropic` 1.x 迁移到 **`httpx2`**，而 `mistralai` 和 `google-genai` 仍使用 `httpx<1`；但它们是两个不同的发行版。通过实际安装验证后，又对 **7 条 provider 路径进行了端到端测试**——OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI 和 Grok CLI——每条输出中的内联代码和链接均得到保留。“避免两套 HTTP 栈”只是偏好，不是阻塞条件：测量结果已经作出判断。
    - **`requirements.txt` 并未描述真实环境**：`google-auth`、`cryptography` 和 `opentelemetry` 栈安装在工作 venv 中，却从未被声明，因此全新安装无法复现实际测试环境。相反，`tokenizers`、`huggingface-hub` 和 `PyYAML` 出现在其中，却没有被任何代码导入或要求，是 `mistralai` 1.x 遗留下来的内容。该文件已根据仅包含直接依赖构建的 venv，重新生成其完整闭包。`pip-audit` 未在新的依赖集合中报告任何已知漏洞。
    - 新增的 **`.github/dependabot.yml`** 启用每周版本更新、pip 更新和 github-actions 更新。次要版本和修订版本合并到一个 PR 中——每个 PR 只升级一个补丁版本最终会被忽略，而噪音是更新的敌人；**主版本分开处理**，每个主版本都要求通过真实调用进行验证。
    - 新增的 **`scripts/check-deps-fresh.sh`（已接入门禁）** 会让延迟直接反映在项目判定中：Dependabot 只负责提出建议，并不提供保证，而且它的 PR 可能不断堆积。主版本延迟 → 失败；次要版本 → 警告，因为长期保持红色的门禁最终会被忽略；PyPI 无法访问 → 本地明确跳过，**CI 中 fail-closed**，未执行的检查不能算成功。两个方向均已验证：它能捕获修复前的确切状态（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`），并且对次要版本只发出警告。

  - **本次 PR 审查产生的修复**——五名审查 agent 仔细检查了 diff；以下问题全部在修复前通过**实际测量复现**，其中两个还是同一版本前文引入的回归。

    - **已修复回归——`_NEWS_CITATION_REGEX` 存在指数级回溯。** 多段落修复在重复结构中引入了 `(?:[ \t]*$|[ \t]+.*)`：`[ \t]+` 与 `.*` 之间的空格共享存在歧义，而且这种歧义会随着迭代次数增加而成倍放大。在不匹配该模式的 `>   texte` 行上进行测量——这些是完全合法的 Markdown 缩进——结果为：**14 行耗时 2,589 ms**，修复后为 0.04 ms，每增加一行，耗时约增加 9 倍。在 `--news` 模式下，一个很长且不符合格式的 blockquote 就足以让翻译冻结，直到作业超时，而且没有可识别的原因。现在重复结构一次性消耗整行（`\n^>(?![ \t]*—).*`），因此每次迭代只剩一种匹配方式。在包含 231 篇文章的真实语料上验证：捕获结果**零差异**，仍是 423 条引用，14 个多段落正文仍会被展开。
    - **同时设置两个 provider flags 时会静默按量计费。** `--use_codex --use_mistral` 会被接受；`_select_provider_client` 优先测试 Mistral，`_resolve_provider` 又优先使用显式布尔值——两者最终都指向 Mistral。因此用户请求的是订阅配额，却得到了按量计费，期间没有任何警告：这正是 `--use_codex` 旨在阻止的故障模式。现在六个 provider flags 都经过一个 `add_mutually_exclusive_group`。**行为发生变化**：同时组合两个 provider 的命令行现在会在 `argument --use_mistral: not allowed with argument --use_codex` 上失败，而此前会被静默接受。
    - **工作结束门禁在探针崩溃时仍会显示绿色。** `scripts/check-release-ready.sh` 的十三项检查中，有四项遵循“捕获 stdout，若为空则得出结论”的模式，却从不检查返回码：异常（文件被重命名、`FileNotFoundError`）会写入 stderr，使 stdout 为空，检查便得出“没有需要报告的内容”。为防止这种情况而编写的脚本内部，反而复现了“一个 `exit 0` 什么也不能证明”的陷阱。现在 helper `probe()` 同时要求返回码为零**并且存在结束哨兵**，探针也拒绝在标记集合为空时作出结论——因为对空集合的断言永远为真。证明如下：上文添加互斥组后，provider flags 通过了一个 `*_group` 对象，而旧正则 `parser\.add_argument\(` 已无法匹配；**21 个 flags 中有 6 个**静默脱离了检查范围，门禁仍显示绿色。
    - **secret 扫描漏掉了六个 provider 中的四个。** `[A-Za-z0-9]` 类别排除了连字符：`sk-proj-…`（当前 OpenAI 格式）和 `sk-ant-api03-…` 会因第二个连字符而匹配失败，`AIza…` 也未被覆盖。现在扩大模式，并将 `.secrets.baseline` 排除在扫描之外。此外，`.env` 查询的是 `git diff --cached`，它只能查看索引：一个**已经提交**的 `.env`——最糟糕的情况——根本不会出现在其中。现在改为查询 `git ls-files`。
    - **Codex 的“token 预热”并不是预热。** 测量结果显示：`codex login status` 不会触碰 `~/.codex/auth.json`（mtime 和大小均未改变），其帮助信息写的是“Show login status”。然而注释却声称会“按顺序执行一次” token 刷新，从而消除一次性轮换 token 的并发刷新风险。所声称的保护并不存在；现在注释如实描述代码行为，真正的解决方案仍是 `max_jobs=4`。此外，检查现在遵循 `CODEX_BIN`；此前它会忽略该项——没有 `codex` 的机器在 `PATH` 中会因“未认证”而失败，导致诊断具有误导性。
    - **`.env` 在子 shell 中被加载。** `detect_provider` 通过命令替换调用，因此它导出的变量不会向上层传递：在 `.env` 中定义的 `GROK_BIN`、`GROK_HOME` 或 `REGEN_MODEL`，在 `main()` 中执行的读取操作都不可见，最终即使配置正确，也会得出“找不到 Grok 二进制程序”的结论。
    - **并发量比声明的上限高出 50%。** 保护措施被放在 README/CHANGELOG 对启动之后：测得 `max_jobs=2` 的峰值为 **3**。对于 Grok，其每周配额与 Chat/Imagine/Voice 共享且无法测量，因此脚本为自己设定的上限并未得到遵守。最终计数虽会被显示，却从未与 28 进行比较——缺失一个文件也不会被发现。
    - **Grok 输出契约：缺少 `stopReason` 现在会失败。** 代码此前使用“`end_turn` **或缺失**”，而已声明的契约要求 `end_turn`。没有该字段，或 CLI 更新后重命名该字段，都会让保护措施静默变成空操作。此外，`max_turn_requests` 不再被归类为 rate limit（耗尽的是轮次预算：重试只会重复结果，却要付出 90 秒等待），而 `quota` 会移出 rate limit 标记——原因早已由 `_codex_is_rate_limited` 的 docstring 说明，但 Grok 此前没有遵循。
    - **Gemini 的级联按模型进行记忆化。** 它在每个 segment 都从 `minimal` 重新开始，而默认模型会拒绝该请求：正常路径每个 segment 都要付出一次 400 往返，并重复打印相同警告。警告重复数百次后就不再有人阅读——这正是它变成掩护的方式。
    - **其他事项**：CI 中的拒绝消息被硬编码为 Codex，并将 `--use_grok_cli` 用户指向 `OPENAI_API_KEY` 而不是 `XAI_API_KEY`；`provider.capitalize()` 显示“Grok_cli”和“Openai”；子进程基础设施的注释将“shim”泛化到两个 CLI，然而 Grok 二进制是原生 ELF（正确的理由应是“会自行生成子进程的 agent”）；`subprocess` 上的 12 个 SAST findings 已标记为 `# nosec` / `# nosemgrep` 并附带理由，使用不含 `shell=True` 的列表形式使注入不可能发生，且文档内容从未经过 argv。
    - **不再有任何 secret 进入 agent 子进程。** 具名 deny-list 只保护了**计费**不变量（Codex 不含 `OPENAI_API_KEY`，Grok 不含 `XAI_API_KEY`）。测量结果显示：每个子进程仍会接收到另外**七个 secret**——Anthropic、Mistral、Google 和 Gemini 的密钥、另一个 CLI 的密钥，以及 `OPENAI_BASE_URL`；后者不是 secret，但会重新导向流量。然而这两个 CLI 都是 **agent**，而 Grok CLI 在许多 Linux 机器上运行时没有适用的操作系统 sandbox。现在按**名称模式**进行过滤（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`），而不是使用具名列表，因此也能覆盖用户在 `.env` 中添加、但这段代码并不知道的变量。CLI 不需要其中任何变量：身份验证保存在 `~/.codex` 和 `~/.grok` 中，从不放在环境中——通过在环境加固后，分别经由两个 provider 完成真实翻译进行了验证。
    - **测试**：新增文件 `tests/test_review_hardening.py`（21 个测试），锁定 provider flags 的互斥性、`stopReason` 契约、news 正则的线性复杂度、CI 中的拒绝消息、Gemini 记忆化，以及子进程环境中不存在任何 secret。最后一项断言是**通用的**——即使某个密钥未被任何列表列出，也会触发失败；而现有的清除测试只是其常量的镜像，只能检测自身循环是否失效。完整测试套件达到 **311 个测试**。
- **两个新的 Grok provider**：`--use_grok`（xAI API，密钥 `XAI_API_KEY`，按用量计费）和 `--use_grok_cli`（官方 Grok Build CLI，从 Grok 订阅中扣除——原理与 `--use_codex` 相同）。
    - **API 模式，约 40 行**：由于 xAI endpoint 兼容 OpenAI，客户端和 `_call_openai` 可原样复用，只需更改 `base_url`。只需一次适配，且所有场景都能受益：`finish_reason` 现在也接受 `end_turn`，即 xAI 发出的形式，而 OpenAI 发出的是 `stop`。模型：`grok-4.6`（高质量）和 `grok-4.3`（经济型）。需要注意的是，Grok 的经济型模型仍是仓库中最贵的——每百万 token 为 $1.25/$2.50，而 `mistral-small-latest` 为 $0.15/$0.60：选择此 provider 是为了模型多样性，而不是价格。
    - **CLI 模式**：以 Codex 为模板，但有四项由实际环境决定的差异——prompt 通过文件传入（`--prompt-file`；CLI 不读取 stdin，而作为 argv 传入的片段会出现在 `ps` 中），stdout 上输出单个 JSON 对象（既不是 JSONL，也不是 `-o` 文件），订阅只提供 `grok-4.6` 和 `grok-4.5`，并且 sandbox 无法应用（见下文）。子进程启动逻辑与 Codex 一起提取到 `_codex_run_process` 中，不触及已经过测试的 Codex provider 其余部分。
    - **`exit 0` 不能证明任何事情，已实测**：未认证时，CLI 会在 **stdout** 写入 `{"type":"error","message":"Not signed in."}`，退出码为 **0**。拒绝或轮数耗尽时行为也相同。因此，输出契约要求四项条件同时满足：退出码为 0、不存在错误 payload、`stopReason == end_turn`，以及非空文本。预检遵循相同逻辑：即使断开连接，`grok models` 也会以 0 退出，只有 stdout 中出现 “not authenticated” 才能得出结论。
    - **隔离：有意为之且已记录。** Codex 在 `--sandbox read-only` 中运行，而 Grok 的 sandbox 在许多较新的 Linux 主机上无法应用，原因是两个彼此独立、若不使用 `sudo` 就无法绕过的系统问题：自 Ubuntu 24.04 起，AppArmor 会阻止非特权 user namespace（`bwrap: setting up uid map: Permission denied`，在 Grok 之外也可复现）；当 `/run/podman` 处于 `0700` 时，容器运行时 socket 的 deny-list 会失败（resolver 只能补救 `ErrorKind::NotFound`，EACCES 会变成致命错误）。核心陷阱是：无法应用的**内置** profile 会导致程序**静默地以未隔离状态启动**。因此，脚本默认不请求任何 profile，也绝不会静默回退——它会在 stderr 上发出警告。保护依赖 CLI 的 `--deny` 规则，包括 catch-all `*`；这是唯一经过实测的 _fail-closed_ 层（未知前缀的规则会拒绝启动）。`GROK_TRANSLATE_SANDBOX=read-only` 可用于强制要求隔离；此时如果机器无法满足要求，启动会失败。
    - **安全措施**：`XAI_API_KEY`、`GROK_API_KEY` 和 `GROK_SANDBOX` 会从子进程环境中移除（其中一个密钥会切换为按用量计费；继承的 `GROK_SANDBOX` 会强制使用不适用的 profile，并显示误导性消息），MCP/hooks/skills/agents 开关已禁用，`--disable-web-search`、`--no-subagents`、`--no-plan`，使用临时 workdir，在 CI 中拒绝运行，超时会终止整个进程组，并在 rate limit 时采用退避。`--max-turns` 固定为 6，而不是 1：计数器会在工具轮次之后递增，设为 1 会截断输出。
    - **配额**：Grok pool 按周计算，并且**与 Chat、Imagine 和 Voice 共享**，没有任何命令可以显示该配额——不同于 Codex，后者的 `account/rateLimits/read` 可以量化消费量。因此，`regen_translations.sh` 将并发限制为 2，并明确发出警告。
    - **测试**：新增文件 `tests/test_grok_provider.py`（24 个测试）。完整测试套件共 **290 个测试**。
  - **已修复 bug——多段落 EN 引用仅被部分保护（`--news` 模式）**：`_NEWS_CITATION_REGEX` 作为引用正文只接受一系列**连续**的 `>` 行。一旦引用跨越多个段落（由一行 `>` 空行分隔），就只有最后一段会被捕获并替换为 placeholder；前面的段落会发送给 LLM 并被翻译——这与 `--news` 旨在保证的行为完全相反。现在，该重复模式接受内部的 `>` 空行，并改为非贪婪匹配，从而在位于斜体行之前的 `>` 空行处停止，而不是在遇到第一个空行时停止。
    - **实测规模**：在包含 198 篇文章的真实语料库中，有 419 个引用，其中 11 个受到影响。没有回归——新 regex 捕获的引用数量完全相同，只扩展了多段落正文（408 个正文不变，11 个正文扩展），而署名行 `> — …` 仍无法被吸收到正文中（lookahead 保留）。
    - **端到端证据**：在一篇 69 KB、翻译成 ja/ar 的文章上测试：引用中原先在日语中呈现为 `> GLM-5.3がオープンウェイト化。`、在阿拉伯语中也同样被翻译的第一段，现在保持为 `> GLM-5.3 is now open-weight.`。英文引用行数从 9 恢复为 10，与源文档一致。
    - 需要注意：该缺陷未被下游验证器发现，因为验证器只检查引用是否存在，不检查引用是否完整。
  - **默认 provider 的实测节省**：`_openai_extra_kwargs` 会在模型名称以 `gpt-5` 开头时发送 `reasoning_effort="medium"`，包括在 `--eco` 中。使用 `gpt-5.4-mini` 翻译一个十词句子的测量结果：`medium` → 45 个 reasoning tokens 和 65 个输出 token；`none` → 0 和 14。推理对翻译没有帮助，却会在每个文件的每个片段上产生费用。默认值现在在 `--eco` 中为 `none`，其他情况下仍为 `medium`；CLI 中显式传入的值仍具有优先级。`--reasoning_effort` 现在除了 `low`/`medium`/`high` 外，还接受 `none` 和 `xhigh`（并非所有模型都接受这些值：例如 `minimal` 会被 `gpt-5.4-mini` 拒绝——现有的无参数重试机制会处理这种情况）。
  - **SDK 更新与 Gemini 迁移**：`google-generativeai`（支持于 2025-11-30 结束，仓库已归档）由统一 SDK **`google-genai`** 替代——先使用 `genai.Client(api_key=...)`，再使用 `client.models.generate_content(model=, contents=, config=)`；系统 prompt 改为通过 `system_instruction` 传入，而不是与片段拼接。`mistralai` 升级到 **2.9.4**（导入变为 `from mistralai.client import Mistral`；旧导入会抛出 `ImportError`，已在 wheel 中验证），`anthropic` 升级到 **0.125.0**，`openai` 升级到 **2.54.0**——这是切换到 `httpx2` 之前的最后版本，以避免 venv 中共存两套 HTTP 栈。`httpx` 0.28.1 和 `pydantic` 2.13.5 也因此解除阻塞。
  - **两个由真实测试而非文档捕获的回归问题**：
    - `anthropic` ≥ 1.0 会在客户端拒绝非流式调用：其 `max_tokens` 预示请求可能超过 10 分钟（`ValueError: Streaming is required...`）。0.34.2 中不存在此安全检查，因此所有使用 `max_tokens=32768` 的 Claude 调用都会失败。现已通过显式 `timeout` 修复（`CLAUDE_TIMEOUT`，默认 900 秒），避免对只需要完整响应的调用切换到 streaming。
    - `thinking_level="minimal"` 仅被 Gemini 模型目录中的一部分接受：`gemini-3.1-flash-lite` 支持它，而 `gemini-3.7-flash` 和 `gemini-3.1-pro-preview` 会返回 400 拒绝。因此加入 `_gemini_generate_with_fallback`，形成 `minimal` → `low` → 不设置 thinking_config 的级联，仿照现有的 OpenAI fallback——优化参数绝不能导致翻译失败。
  - **更新默认模型**，每个模型都通过真实调用验证：OpenAI `gpt-5.5` → **`gpt-5.6-terra`**（在包含 28 个批次的测试中降低 60%）以及 `gpt-5.4-mini` → **`gpt-5.6-luna`**（降低 73%）；Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**（价格更低且更新）以及 `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（不带日期的规范 ID）；Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**，以及 `gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（稳定版本，且比 `3.5-flash-lite` 更便宜）。Mistral 不变，`mistral-large-latest` 仍是四者中性价比最高的模型。需要注意：不存在比 `gemini-3.1-pro-preview` 更新的 Gemini Pro 系列模型——2026 年 5 月宣布的 Gemini 3.5 Pro 从未发布；3.5/3.6/3.7 系列全部属于 Flash。
  - **切换 Gemini 前进行 A/B 实测**：使用 `gemini-3.1-pro-preview` 将 `README.md` 翻译成日语，然后使用 `gemini-3.7-flash`。结构完全一致（21 个列表、18 个代码块、13 个 HTML 链接、13 张图片，所有 URL 均保留），耗时为 **8 秒，而不是 48 秒**。由于没有公开 benchmark 比较这两个模型在翻译或非拉丁脚本上的表现，否则这次切换只能建立在简单推测之上。
  - **Claude 响应块过滤**：`_call_claude` 会在不筛选类型的情况下执行 `block.text for block in response.content`。自适应推理模型（Sonnet 5 及更高版本）会插入一个 `thinking` 块，其中暴露的是 `.thinking` 而不是 `.text`——翻译会在第一个片段遇到不透明的 `AttributeError` 时失败。现在会排除 `thinking`、`redacted_thinking`、`tool_use` 和 `tool_result`（采用否定列表，以便对携带文本的未知类型保持兼容），如果响应中完全没有文本块，则抛出明确错误。`thinking={"type": "disabled"}` 会在每次调用时传入。
  - **`MODEL_TOKEN_LIMITS` 已重新同步**：移除已过退役日期的模型（`magistral-*` 系列于 2026-07-31 退役，`gemini-2.0-*` 于 2026-06-01，`gemini-3-pro-preview` 于 2026-03-09，以及 `claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。修正上下文限制：Mistral 128K → **256K**（Large 3 / Small 4 生成），Gemini 1 000 000 → **1 048 576**（实际 input 限制），`claude-opus-4-5` 200K → **1M**，`gpt-5.6-*` 系列 400K → **1.05M**。新增 Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest` 以及 `ministral-*` 系列。需要注意：这些限制仍是参考值，`translate()` 会将分段上限设为 `min(16000, limite)`。
- **提供商 `--use_codex`**：第五个提供商，通过非交互模式驱动官方 Codex CLI（`codex exec`），而不是调用按使用量计费的 API。翻译消耗的是已经支付的 ChatGPT 订阅额度。这是 OpenAI 为此用途记录的唯一途径：按套餐划分的可用性矩阵将“Codex SDK、`codex exec` 和可脚本化工作流”列为 Plus/Pro/Business/Enterprise 可用，而 `~/.codex/auth.json` 的令牌无法认证 Platform API 调用（此脚本也从不读取它们——认证及其刷新仍由 CLI 管理）。
  - **可通过 pip 安装 Codex 二进制文件，不再只能通过 npm 安装**：`_resolve_codex_binary()` 会先在 `CODEX_BIN` 中查找二进制文件，然后查找 `PATH`，最后查找由 OpenAI 发布的官方 Python 包 **`openai-codex-cli-bin`**（这是 `openai-codex` SDK 的依赖项）。因此，Python 项目不再需要全局安装 npm 即可使用 `--use_codex`。该包不会添加到 `requirements.txt`：二进制文件约 250 MB，否则所有用户都会被迫安装一个可选提供商。端到端验证结果：在 `PATH` 中不存在 `codex` 时，解析仍能找到打包的二进制文件，并在 6 秒内完成完整翻译。
  - **“订阅模式”保证**：`OPENAI_API_KEY` 和 `CODEX_API_KEY` 会从子进程环境中移除。如果没有这层保护，`.env` 中存在的密钥可能会让 Codex 切换到按使用量计费模式，且完全没有可见提示——这正是该提供商要避免的情况。
  - **CLI 陷阱已由测试锁定**：
    - 即使提示词作为参数传入，`codex exec` 仍会读取标准输入：如果不关闭标准输入，命令会一直等待直到超时，且从未调用模型（复现结果：180 秒后退出码为 124，输出 0 字节）。因此必须使用 `communicate(input=...)`。
    - 通过 npm 安装的 `codex` 是一个 Node shim，它会 `spawn` 真正的 Rust 二进制文件：后者是 Python 进程的**孙进程**，会在 `subprocess.run(timeout=)` 的 `SIGKILL` 之后继续存活，并持续消耗额度。因此需要 `Popen(start_new_session=True)` + `os.killpg`。
    - CLI 可能在输出 `turn.failed` 的同时以 0 退出：除返回码外，还会检查 JSONL 输出（`--json`）；如果返回码为 0 但缺少 `-o` 文件，则会抛出明确错误，而不是生成空片段。
  - **速率限制退避**：CLI 不实现内部重试（`max_retries = 0`）。分类依据是 JSON 负载结构（`status: 429` / `error.type`），而不是子字符串——“quota”一词既可能出现在可恢复的 429 错误中，也可能出现在不可恢复的 `insufficient_quota` 中。
  - **CI 防护**：如果定义了 `CI` 或 `GITHUB_ACTIONS`，则会拒绝 `--use_codex`。订阅认证不适用于共享 runner，OpenAI 也明确不建议在公共仓库上采用此工作流。
  - **模型**：`gpt-5.6-sol`（质量）和 `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` 系列由 CLI 和 Platform API 共用，但 ChatGPT 账户并不一定有权使用其中所有模型：允许列表由服务器端执行，本地不做验证，使用不常见的模型会触发警告。在 Plus 套餐中，Luna 每个 5 小时窗口提供 250–2,000 条消息，而 Sol 提供 10–100 条：对于任何批处理，推荐使用 `--eco` 模式。
  - **已修复的错误——`regen_translations.sh` 在完全成功后仍会报错**：`trap ... EXIT` 引用了 `failed_log`，这是 `main()` 中的一个 `local` 变量，而该变量在 trap 执行时已经不存在。在 `set -u` 下，这会抛出 `failed_log: unbound variable`，使脚本以 1 退出，尽管 28 个翻译都正确——这会在重新生成后、最昂贵的步骤中，立即中断 `release.sh --auto`（`set -e`）。现在该变量变为全局变量，trap 会先检查其是否存在。另一个有用的副作用是：此前被该错误掩盖的真实翻译失败，如今会重新显示在末尾摘要中。
  - **`REGEN_MODEL`**：`regen_translations.sh` 的新环境变量，可强制指定模型，覆盖提供商默认值，例如使用 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`，在订阅额度内以高端模型重新生成，而不是使用面向大批量处理的 `--eco` 模型。
  - **`regen_translations.sh`**：`REGEN_PROVIDER=codex` 现可通过明确选择启用（从不自动检测，以免在用户不知情的情况下消耗订阅额度）。令牌会在开启并行处理前按顺序刷新一次——由于 Codex 刷新令牌具有轮换性且只能使用一次，并发任务会使 `codex login` 会话失效——并将并发数降至 4。
  - **相关重构**：`_dispatch_provider_call` 通过一个返回提供商名称的 `_resolve_provider()` 从 8 个参数减少到 6 个参数，而不是在整个调用链中传递第四个布尔值。显式布尔值仍优先于 `args`，以保持调用 `translate(..., use_mistral=True)` 且仅传入最小 `Namespace` 的测试正常工作。
  - **测试**：新增文件 `tests/test_codex_provider.py`（48 个测试），覆盖 argv、清理后的环境、反前导内容契约、静默失败、超时/killpg、退避、预检、提供商解析、Gemini 推理级联、Claude 区块过滤以及多段新闻引用。完整测试套件共 290 个测试。
  - **真实验证**：通过 Codex 将项目的 `README.md` 翻译成**14 种语言**后，与参考翻译相比结构完全一致（14 个代码块、24 个标题、25 个表格行、13 个 HTML 链接、13 张图片、19 个 URL，代码块逐字符一致，且没有残留占位符）。对于一篇 69 KB 的新闻文章，在 `--news` 模式下，`gpt-5.6-luna` 和 `gpt-5.6-sol` 的输出均通过了下游应用验证器（en/ja/ar）。通过 `account/rateLimits/read` 测得的消耗保持在计数器的四舍五入阈值以内（`--eco` 模式下 5 小时窗口为 0%）。

- **1.9.2** 修复带嵌套括号或 FR 前缀的新闻归属 URL 提取（2026-05-11）：

  - **已修复的错误**：`_protect_news_quotes` 中的归属 URL 提取使用了正则表达式 `re.search(r"\((.+?)\)", attribution)`（括号内的惰性捕获）。对于类似 `(relayé par [@user sur X](https://x.com/.../123))` 的归属内容（嵌套括号：外层的 `(` + Markdown 链接中的 `]()`），捕获会在遇到第一个 `)` 时停止，导致字符串被截断，并包含 FR 前缀：`relayé par [@user sur X](https://x.com/.../123`（缺少末尾的 `)`）。结果是：`_validate_news_post` 会在翻译后的输出中查找该字符串并始终失败（有两个原因：`)` 被截断，以及“relayé par”被翻译成 `relayed by`/`weitergeleitet von`/……）。完整的 low → medium → high → gpt-5.5 级联无法通过。
  - **修复**：正则表达式改为 `re.search(r"\]\(([^)]+)\)", attribution)`——专门定位 Markdown 链接中的 `](url)`，仅捕获**纯 URL**（不含 FR 前缀，也不截断），并通过翻译过程中的 `#URL{N}#` 占位符保持不变。能够稳健处理以下两种问题模式：
    - `(relayé par [@account sur X](url))`——嵌套括号
    - `via [@source](url)` 或 `selon [@author](url)`——没有外层括号的 FR 前缀
  - **测试**：在 `test_silent_failure.py` 的 `TestNewsCitationExtraction` 类中新增 2 个测试：
    - `test_extract_attribution_url_with_nested_parens`（精确复现 Genspark CEO E2B 的错误案例）
    - `test_extract_attribution_url_with_french_prefix`（带 `via` 的变体）
  - **覆盖缺口**：`check-editorial-coverage.py` 会验证编辑语法，但不会验证其能否被 translator 翻译。一个可能的改进方向（不属于 v1.9.2 范围）是在发布前增加检查，通过 dry-run 模拟归属提取，以检测存在风险的模式。

- **1.9.1** 修复翻译 marker 注释中的 CTA 标签国际化（2026-05-10）：

  - **已修复的错误**：翻译文件顶部 marker 横幅中 CTA 链接的 `[Voir le projet sur GitHub ↗]` 标签在所有目标语言中仍然是**法语**，而不是跟随 `target_lang`。LLM 永远看不到该标签（它由 Python 侧组装，以保留 URL 和仓库 slug），因此翻译阶段无法修正它。自 v1.9 添加 `marker` 格式以来一直存在这一静默回归。
  - **修复**：新增 `_VIEW_PROJECT_LABELS` 常量，将 15 种语言映射到本地化标签。`_translation_note_invariants(target_lang)` 和 `_assemble_translation_note_paragraphs(phrase, target_lang)` 现在会传递目标语言。如果语言未知，则回退到 `fr`（安全处理，避免 KeyError）。
  - **测试**：调整 `test_source_emits_three_paragraphs_repo_title_description_link`（target_lang `ja` → 预期为日语标签）。新增 2 个测试：`test_source_link_label_localized_per_target_lang`（参数化覆盖 7 种语言，包括拉丁文字、表意文字和辅音音素文字）以及 `test_source_link_label_falls_back_to_french_for_unknown_target`。总计：`test_translation_note_position.py` 中有 40 个测试（原为 38 个）。
  - **向后兼容**：签名带有默认值 `target_lang="fr"`——不传入 `args.target_lang` 的外部程序调用方无需修改即可继续工作。
- **1.9** 修复静默失败 + 完整质量工具链 + 多位置翻译注释（2026-05-07）：
  - **多位置翻译注释 + “embed card”格式标记**：
    - 新增 CLI 选项（附加功能，默认值不变 → **不破坏兼容性**）：
      - `--note_position {top,bottom,both}`（默认值：`bottom`）：将注释放置在翻译文件顶部、底部，或同时放置在两处。
      - `--note_format {legacy,marker}`（默认值：`legacy`）：
        - `legacy` 严格复现 v1.8 的行为（粗体段落 `**…**`），**逐字节一致**。
        - `marker` 输出一个不可见的 Markdown 链接引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），随后输出一个结构化的**三段式 blockquote**，用于呈现类似“GitHub repo embed card”的效果：以行内代码显示项目标题（`**\`ai-powered-markdown-translator\`\*\*`）、由 LLM 翻译的描述，以及带可见箭头的 CTA 链接（`[Voir le projet sur GitHub ↗](URL)`）。可由 remark 插件在构建时处理（参见 blog jls42.org → 插件 `remark-translation-banner`）。
    - **绝不发送给 LLM 的不变量**：仓库标题和 GitHub URL 会在描述句翻译完成后由 Python 端组装。LLM 永远看不到 slug `ai-powered-markdown-translator` 或 `https://github.com/jls42/...`，从而确保任何 renderer、斜杠或 scheme 都不会被改动。
    - **感知 Frontmatter 的插入**：在 `top` 或 `both` 模式下，注释会插入在 YAML frontmatter 的**结束块 `---` 之后**（确保 Astro Content Collections / gray-matter 安全）。Helper `_split_frontmatter` 会检测文件开头的 `---\n…\n---\n` 并保持其完整性；如果 frontmatter 已打开但没有关闭 fence，则**抛出 `RuntimeError`**（文件会进入 `failed_files`，而不是带着位置错误的注释写入）。
    - **模型 sanitizer 白名单**：`_sanitize_model` 会将所有不属于 `[A-Za-z0-9._:/-]` 的字符替换为 `_`；如果结果为空，则使用回退值 `unknown`。这与 Astro remark 插件侧的验证器保持一致，并会消除可能破坏标记格式的字符（空格、引号、括号、逗号等）。
    - **内部重构**：将 `_append_translation_note`（1 个单体函数）拆分为 7 个纯 helper（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。Builder 与 composer 分离（builder 返回不含分隔符的纯区块，composer 根据位置应用 `\n\n`）；生产代码和源 helper 共用同一个三段式组装器。
    - **`_quote_lines` 保留空行**：为每一行添加 `> ` 前缀，将空行转换为仅包含 `>` 的行。这样 mdast 能在 blockquote 中识别出 3 个不同的段落（标题 / 描述 / 链接），而不是包含换行符的单个段落。
    - **`_build_translation_note_block` 自适应**：根据 LLM 保留的段落数量进行处理（3 段 = 完整 card 格式，2 段 = 句子 + 链接，1 段 = 回退方案）。当检测到 Markdown 链接 `](` 时，单段回退方案不再用 `**...**` 包裹链接（避免 `<strong>` 包裹链接时产生脆弱的渲染效果）。
    - **向后兼容**：`getattr(args, "note_position", "bottom")` 和 `getattr(args, "note_format", "legacy")` 位于 `_compose_with_notes` 侧——不具备这些属性的 Namespace（现有测试、外部程序化调用）仍可无需修改地继续工作。
  - **修复长篇翻译的静默失败**：
    - 所有 provider（OpenAI、Mistral、Claude、Gemini）均加入翻译后语言验证：确定性层（逐字检索到源文片段）+ 概率性层（`langdetect`）。
    - 白名单 `finish_reason` / `stop_reason`：任何不在白名单内的状态（truncation、content_filter 等）都会触发 `RuntimeError`。
    - Claude 的 `max_tokens`：从 `4096` → `32768`（避免 16k 分段出现潜在截断，并为 FR→JA/ZH/KO/AR/HI 跨文字体系翻译保留余量）。
    - 感知标题的分段：在分段后半部分优先处理 H2/H3（每个分段都从完整的语义章节开始）。
    - 错误传播直至非零退出码：`translate_markdown_file` 返回类型化状态 `success` / `failure` / `skipped`；如果至少有一个文件失败，`main()` `sys.exit(1)`（单文件和批处理均适用）。
    - 所有 provider 均加入空内容保护、源文/输出文合理比例检查（≥ 500 个字符，< 5% = 拒绝）、代码占位符验证（`#CODEBLOCK`/`#INLINECODE`）、LLM 后规范化（修复与标题粘连的分隔符/链接），以及不带 `reasoning_effort` 的 `BadRequestError` 重试。
    - 新增依赖 `langdetect==1.0.9`。
  - **pre-commit 质量工具链**（“完整 EurekAI 类型”，14 个 hook）：
    - Pre-commit：ruff（lint+format）、shellcheck、prettier（md/yaml/json）、detect-secrets（保护 4 个 API key）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（空白字符、EOF、大文件、shebang 等）。
    - Pre-push：mypy（渐进式 lax 模式）、Opengrep SAST（translate.py + scripts/）、pip-audit（初始 reporting 模式）、unittest discover（tests/ + scripts/tests/）。
    - `scripts/` 中的本地 wrapper 使用 `./venv/bin/python`。
    - `scripts/audit_verdict.py`：使用 11 个 unittest 测试解析 pip-audit JSON，是 jls42-astro parser 的 Python 移植版。
    - 修复最初的 7 个 ruff 违规：B904（raise from）×2、B007（未使用的 dirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）。
    - Lizard 暂时排除 `translate.py`（4 个函数的 CCN 为 21-47，已计划重构）——对 scripts/ 启用严格 gate。
  - **SonarCloud + 完整覆盖率**：
    - GitHub Actions 工作流 `SonarCloud`（sonarcloud.yml + sonar-project.properties）：每次 push 和 pull-request 均执行分析，覆盖率通过 `coverage.xml` 获取。
    - README 顶部新增 11 个 SonarCloud 徽章（Quality Gate、Security/Reliability/Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）。
    - `tests/test_silent_failure.py`（`unittest` stdlib）：覆盖静默失败错误链的六个环节。
    - `tests/test_orchestration.py`（+79 个测试）：覆盖 `translate.py` 的编排层（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` TypeError + BadRequestError 回退、o1-series prompt 格式、`_validate_translation_output` 的 early-return 分支）。
    - `scripts/tests/test_audit_verdict.py`：通过 subprocess 覆盖 `main()`（stdin/stdout）以及 `if __name__ == "__main__"` 区块。
    - **新代码覆盖率**：75.5% → 约 98%（translate.py 98%，scripts/audit_verdict.py 97%）。
  - **测试**：`tests/test_translation_note_position.py` 覆盖位置 × 格式矩阵（包括 E2E `marker+top|bottom|both` 和 `legacy+top|bottom|both`）、多行前缀处理、逐字节向后兼容（golden literal）、sanitizer、frontmatter 分割（包括未闭合 fence 时抛出异常）、三段式格式、两段式回退、单段 + Markdown 链接保护，以及一个关键防护测试 `TestLLMPayloadExcludesInvariants`，断言标题和 URL 永远不会发送给 LLM。**190 个测试通过**，0 个回归。
  - 文档：`README.md`（法语 + 14 种翻译）带徽章，`CLAUDE.md`（pre-commit 工作流 + 详细的 CI 监控），重新生成 28 种翻译。
- **1.8** `--news` 模式 + 2026 模型升级（2026-03-17，标签 `v1.8`）：
  - 默认模型已更新（2026 年 3 月）：
    - OpenAI 质量型：`gpt-5` → `gpt-5.4`
    - OpenAI 经济型：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 质量型：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - 为 `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）和 `gemini-3.1-pro-preview`（1M）新增 token 限制。
  - 初始 `--news` 模式：使用占位符 `#NEWSQUOTE\d+#` 保护英文引用，`LANG_FLAGS` 映射（15 种语言），并处理目标语言的标志。
  - 恢复前验证 news 占位符（回归问题：删除占位符的 LLM 会静默地产生不带引用的输出）。
  - 使脚本 `regen_translations.sh` 具备可移植性（绝对路径，不依赖 pwd）。
  - 在 README/CHANGELOG 的语言栏中加入法语链接，重新生成 28 种翻译。
- **1.7** 新功能：
  - 新增选项 `--keep_filename`，在翻译时保留原始文件名。
  - 支持通过 `.env` 文件自动加载 API key。
  - **保留行内代码**：反引号（`` `...` ``）现在会在翻译期间受到保护。
  - 改进系统 prompt：
    - 更好地处理 YAML frontmatter 中的引号。
    - 保护模板变量 `{variable}`。
    - 禁止未请求的翻译注释。
  - 已在 364 个文件上成功测试（jls42.org 博客迁移）。
- **1.6** 新功能：
  - 支持 Google Gemini API 进行翻译（`--use_gemini`）。
  - 更新 2026 年默认模型：
    - OpenAI：`gpt-5`（质量型）、`gpt-5-mini`（经济型）
    - Claude：`claude-sonnet-4-5`（质量型）、`claude-haiku-4-5`（经济型）
    - Gemini：`gemini-3-pro-preview`（质量型）、`gemini-3-flash-preview`（经济型）
  - 经济模式（`--eco`），用于使用更快且成本更低的模型。
  - 单文件翻译（`--file`），无需遍历目录。
  - 新的简化命名模式：`{base}-{lang}.md`。
  - 新增选项 `--include_model`，用于保留包含模型名称的旧格式。
  - 支持未列出的模型，并默认设置 token 限制（128k）。
  - README 已翻译为 14 种语言。
- **1.5** 改进：
  - **API key 和默认模型更新：**
    - **OpenAI：** 从 `DEFAULT_MODEL_OPENAI` 更新为 `"gpt-4o"`。
    - **Mistral AI：** 从 `DEFAULT_MODEL_MISTRAL` 更新为 `"mistral-large-latest"`。
    - **Anthropic Claude：** 新增 `DEFAULT_ANTHROPIC_API_KEY`，并将 `DEFAULT_MODEL_CLAUDE` 更新为 `"claude-3-5-sonnet-20240620"`。
  - **翻译 prompt 优化：**
    - 直接翻译和翻译注释的 prompt 得到丰富，以提升清晰度和效率，其中包括关于保留元数据及特定格式元素的详细指令。
  - **代码重构：**
    - 用 `Mistral` 类替换 `MistralClient`，用于初始化 Mistral AI 客户端。
    - 重新组织导入，以提高可读性和可维护性。
    - 改进文本分段和代码块处理，在翻译过程中保留原始格式。
  - **输出文件管理：**
    - 反转输出文件名中的模型和语言顺序（例如 `f"{base}-{args.target_lang}-{args.model}.md"`），从而便于组织和查找翻译。
  - **其他改进：**
    - 删除不必要的空行，清理代码。
    - 进行细微调整，以改善脚本的结构和可读性。
- **1.4** 新功能：
  - 支持 Anthropic Claude API 进行翻译。
  - 优化 prompt，以提升清晰度和效率。
  - 进行细微调整，以改善代码维护。
- **1.3** 改进和新功能：
  - 改进代码块处理。
  - 改进输出文件处理。
  - 改进现有文件检测。
  - 新增选项 `--force`，用于强制翻译。
  - 反转输出文件名中的模型和语言顺序。
- **1.2** 修复变更日志。
- **1.1** 新增 Mistral AI API 支持。
- **1.0** 初始版本——支持 OpenAI API。

**使用 gpt-5.6-luna 将文章从法语翻译成中文。**
