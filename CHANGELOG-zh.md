### 更新日志

🌍 [Français](CHANGELOG.md) | [English](CHANGELOG-en.md) | [Español](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [Deutsch](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [한국어](CHANGELOG-ko.md) | [العربية](CHANGELOG-ar.md) | [हिन्दी](CHANGELOG-hi.md) | [Italiano](CHANGELOG-it.md) | [Nederlands](CHANGELOG-nl.md) | [Polski](CHANGELOG-pl.md) | [Português](CHANGELOG-pt.md) | [Română](CHANGELOG-ro.md) | [Svenska](CHANGELOG-sv.md)

- **1.11.0** 发布至 PyPI：随后执行 `pip install ai-powered-markdown-translator` 和命令 `aipmt`，无需克隆仓库（2026-08-31）：

  - **单文件脚本变成了可安装软件包。** `translate.py` 从根目录移至 `src/aipmt/translate.py`，并提供控制台入口 `aipmt` 及其等价形式 `python -m aipmt`。克隆仓库仍是贡献所必需的——测试、28 种翻译和质量工具都在其中——但使用软件包不再需要克隆仓库。

    - **导入名称是 `aipmt`，绝不能是 `translate`**，因为冲突确实存在，而且不会显式报错。PyPI 软件包 `translate`（v3.8.1，最近一次上传于 2026-07-06）会安装同名的目录。在虚拟环境中重现时，目录会优先于模块，`translate.main` 消失，入口在 `AttributeError` 处崩溃——而 `pip check` 却返回“No broken requirements found”，rc=0。用户只需执行一个简单的 `pip install translate`，就足以在没有可用诊断的情况下破坏 CLI。使用真实 wheel 进行反证：在该软件包之上执行 `pip install translate`，`aipmt --help` 在前后均返回 rc=0，两个 CLI 可以共存。
    - **发行名称较长，命令名称较短。** `ai-powered-markdown-translator` 让软件包能够通过 PyPI 搜索找到；单独使用缩写时，不了解项目的人将无法找到它，而发布的目的正是让它可被发现。两个看似合理的候选名称经核查后被排除：`ai-markdown-translator` 自 2024 年起已被 npm 上一个用途相同的工具占用，且比本仓库早 17 个月；`aimt` 只比 `aim`（v3.29.1）少一个字母，而后者是同一领域中仍活跃的软件包——这是造成长期混淆的最糟糕配置。顺便说明一个方法陷阱：`pypi.org/project/<nom>/` 对任何名称都会返回 200（反机器人页面），只有 JSON API 才可信。
    - **采用 `src/` 布局，而不是扁平软件包。** 扁平软件包本可保留测试中的六个 `sys.path.insert(..., "..")`，但这恰恰是缺陷：它们会导入源代码树而不是软件包，从而掩盖任何打包错误。实际代价是增加一条替换规则。

  - **密钥终于可以一次性永久配置。** 已安装的 CLI 原本没有任何持久化配置：只剩环境变量和当前目录中的 `.env`。`find_dotenv` 确实会一直向上查找到系统根目录，因此**在个人目录下工作时**能够找到一个 `~/.env`，但在其他位置工作时什么也找不到——覆盖范围取决于从哪里执行命令，而不是设计选择。因此新增第三层：`~/.config/aipmt/.env`，位于已有两层之下。

    - **优先级并未硬编码**，而是由 `override=False`（`load_dotenv` 的默认值）自然决定：每一层只填补前一层留下的空缺。因此顺序为环境变量 → 项目的 `.env` → 用户配置；该顺序通过行为测试而非结构测试验证——调换前两个调用的顺序会导致测试失败，移除第三层也会失败。
    - **采用 `.env` 格式而非 TOML**，这是有意为之：`python-dotenv` 已经是依赖项，语法也已记录在 15 个 README 中，同一个文件还可用于两种作用域。不引入新的依赖或语法。存储位置遵循 `XDG_CONFIG_HOME`（如果它是**绝对路径**）——规范要求忽略相对值，否则配置位置又会取决于当前目录——Windows 下则使用 `APPDATA`。
    - **排除了两个选项，并说明原因。** 系统密钥环（`keyring`）在桌面电脑上更安全，但在无头环境——服务器、容器、CI——中会失败，而这正是批量翻译的使用场景；适合作为选择性启用方案，不适合作为默认方案。使用 `--api-key` 标志会使密钥落入 shell 历史，并显示在 `ps` 中。
    - **没有密钥时，不再留下调用堆栈。** 用户此前会看到指向 `site-packages` 的 Python 堆栈，以及一条提到“环境或 .env”却没有说明第二个位置应在哪里创建的消息。现在会列出三个位置及其精确路径，并以 2 退出。这个兜底范围是**有意保持狭窄的**：`except ValueError` 只包围配置阶段。包裹整个执行过程会把翻译期间真正发生的错误转换成令人安心的消息——这正是本仓库要追踪的故障模式。一个测试会读取 `main()` 的源代码以禁止这种做法。

  - **修复——安装工具后，用户的 `.env` 曾被忽略。** 不带参数的 `load_dotenv()` 并不是从当前目录向上查找，而是从调用方文件开始查找，也就是从 `site-packages` 开始。使用从拥有自身 `.env` 的项目目录中启动的真实控制台入口进行测量：`find_dotenv()` 返回 `''` 且不会加载密钥，而 `find_dotenv(usecwd=True)` 能够找到它。只要工具仅从克隆仓库中运行，这个错误就不会存在；发布后它会变成系统性问题，唯一症状是在正确配置下仍提示 API 密钥“缺失”。

  - **三个门禁在停止检查任何内容后仍会变绿。** 它们在移动之前就被有意加强：在变更之后才编写、声称用于捕获该变更的防护措施，不能证明任何事情。每个门禁在原始仓库上为绿色，在迁移副本上变为红色——两个方向都经过测量。

    - **Lizard 会无声地忽略不存在的路径**：rc=0，并显示“0 file analyzed”。复杂度门禁会从 158 个函数 / 2247 个 nloc 变成 3 个函数 / 34 个 nloc，同时输出零字节。现在作用域是一个数组，并会逐项验证每个条目确实存在。
    - **对不存在的模块执行 `coverage run --source=` 不会失败**：仅在 stderr 上发出警告，unittest 和 `coverage xml` 均返回 rc=0，报告仍会发布——但从 1453 个语句缩减为 141 个。项目看起来会很健康，因为几乎没有内容被分析。两个下限会保护报告：总数，以及测量结果最大的文件。
    - **翻译新鲜度探针在结构上无法感知调用形式的变化**：它依赖 argparse 标志，而文件重命名恰恰不会改变这些标志。重现结果如下：模块被移动，15 个 README 仍记录着一个不存在的命令，但结论却是“没有过时翻译”。因此新增第 7 个部分，检查的是**形式**而非选项；同时将 Lizard 钩子与脚本的实际作用域进行比对——当其 `files:` 不再匹配时，pre-commit 不会失败，而是**跳过**。

  - **`requires-python = ">=3.10"` 不再只是声明。** `sonar-project.properties` 早已宣称支持 3.10-3.12，但从未真正运行过这些版本，因为开发环境只有 3.12——这是一个会因发布而公开暴露的内部矛盾。现在新增测试工作流，在 3.10、3.11 和 3.12 上运行完整测试套件，并安装软件包，因此也会验证其公开依赖范围。

  - **只有最低版本限制，没有上限。** `requirements.txt` 仍是经过测试的锁定文件，`[project.dependencies]` 成为公开契约：发布锁定文件中的精确版本会与用户安装的其他软件包产生冲突。也不设置 `<N+1` 上限——它会与 `check-deps-fresh.sh` 直接矛盾，后者会在主要版本落后时让发布门禁失败。最低版本集合解决了这一问题；反证测试 `openai==1.0.0` 返回 `ResolutionImpossible`，证明检查能够区分情况，而不是接受所有内容。此外还有一项保护，禁止 `pyproject.toml` 的版本与 CHANGELOG 中的版本不一致：PyPI 不允许重复使用同一个版本号。

  - **在全新的虚拟环境中完成端到端验证**：69,768 字节的 wheel 只包含 `aipmt/*.py`、dist-info 和许可证；`aipmt --help` 返回 rc=0，并显示 22 个标志；`python -m aipmt` 显示“usage: aipmt”，而不是“usage: \_\_main\_\_.py”；安装后的 `pipx` 可以正常工作；最重要的是，**从任意用户目录执行真实的 fr→en 翻译**，粗体、列表、行内代码、链接和 URL 均得到保留，代码块未被翻译。迁移前后的 318 个测试均通过，且标识符列表逐字节完全一致——这才证明没有测试被禁用，而不是“OK”这个字样。

- **1.10.0** Provider `--use_codex`（ChatGPT 订阅配额）、SDK 和模型更新、修复多段新闻引用（2026-08-29）：

  - **安全审查——PR 提出的两个防护措施并未在所有路径上真正落实**：

    - **Codex 预检将整个 `.env` 传给了二进制程序。** `_codex_preflight` 调用 `subprocess.run` 时**没有 `env=`**：子进程继承了完整的 `os.environ`，也就是由 `load_dotenv` 加载的全部 `.env`。通过经过检测的伪二进制程序进行测量：预检收到了**七个秘密**——六个 provider 的密钥以及一个 `GITHUB_TOKEN`——而其对应的 `_grok_preflight` 则是**零个**，因为它正确传递了 `env=_grok_env()`。这是 PR 内部的不一致：`_strip_secret_env` 的存在正是为了维护这一不变量，而且就在几行之外。现在提取出一个 `_codex_env_base()`，由两条路径共享；修复后的测量结果为双方均传递 0 个秘密。
    - **“`--deny` fail-closed”这一属性并不涵盖实际采用的形式。** 注释以未知前缀规则会拒绝启动为由，解释了 Grok 的全部隔离措施。在 `grok 1.0.13` 上进行测量后发现，这种验证**仅适用于带括号的形式**：`--deny 'CeciNestPasUnOutil(*)'` 会拒绝启动（“unknown tool prefix”），而 `--deny 'CeciNestPasUnOutil'` 却会被静默接受。然而 `GROK_DENY_RULES` 只使用裸名称——因此 xAI 方面重命名工具后，会在完全没有信号的情况下移除唯一经过测量的隔离层，而此时操作系统沙箱本来就不适用。八条命名规则现在均通过 `Prefix(*)`，并逐一验证为 CLI 已知前缀；catch-all `*` 保持字面形式，这是唯一被接受的形式。一个测试防止未验证形式重新出现。
    - **其他方面已完成干净验证**：不存在命令注入（所有地方均使用列表形式，绝不使用 `shell=True`；文档内容通过 stdin 或 `--prompt-file` 传递），不存在不安全反序列化（仅使用 `json.loads`，并带有类型保护），路径遍历修复在七个有效负载上均未找到绕过方式，而且 `--deny '*'` 确实由 CLI 应用（在 workdir 外读取时观察到 `DENY_ENFORCED`）。
    - 上文新增的新鲜度检查顺便绕过了它自己的原则：当 PyPI 请求失败时，软件包会被静默跳过，门禁仍保持绿色。现在会统计实际完成比较的软件包数量，并在覆盖范围不完整时失败。

  - **依赖已升级，并增加两道防护以避免再次落后**：

    - **落后确实存在，而且持续了很久**：`openai` 从 2.54 升至 **3.6.0**，`anthropic` 从 0.125 升至 **1.2.0**，`certifi` 从 2024.8.30 升至 **2026.7.22**——也就是用于为所有 provider 调用验证 TLS 的根证书存储落后了两年。原因已确定：**不存在 `.github/dependabot.yml`**。没有这个文件时，GitHub 只启用 _security updates_，Dependabot 只有在某个依赖受到 CVE 影响时才会提出 PR——这解释了它为何升级了 `urllib3` 和 `idna`，却让两个 SDK 从一个主要版本落后到另一个主要版本。
    - **两个主要版本可以共存且不会冲突**，与此前推理所担心的情况相反：`openai` 3.x 和 `anthropic` 1.x 会迁移到 **`httpx2`**，而 `mistralai` 和 `google-genai` 仍使用 `httpx<1`，但它们是两个不同的发行版。通过实际安装验证后，又对**7 条 provider 路径进行了端到端测试**——OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI 和 Grok CLI——每条输出中的行内代码和链接均得到保留。“避免两套 HTTP 栈”只是偏好，并非阻塞条件：测量结果给出了结论。
    - **`requirements.txt` 并未描述真实环境**：`google-auth`、`cryptography` 以及 `opentelemetry` 栈都安装在工作虚拟环境中，却从未声明——因此全新安装无法复现实际测试内容。相反，`tokenizers`、`huggingface-hub` 和 `PyYAML` 虽然列在其中，却没有被任何内容导入或要求，是 `mistralai` 1.x 遗留下来的内容。该文件现已根据仅包含直接依赖构建的虚拟环境，重新生成完整闭包。`pip-audit` 未报告新依赖集合存在任何已知漏洞。
    - **新增 `.github/dependabot.yml`**，启用每周版本、pip 和 github-actions 更新。次要版本和补丁版本合并为一个 PR——每个 PR 只升级一个补丁版本最终会被忽略，而噪声是更新的敌人；**主要版本单独处理**，每个版本都要求通过真实调用进行验证。
    - **新增 `scripts/check-deps-fresh.sh`（已接入门禁）**，让项目结论明确显示落后情况：Dependabot 会提出建议，但不会保证更新，而且 PR 可能堆积。主要版本落后 → 失败；次要版本落后 → 警告，因为永久显示红色的门禁最终会被忽略；PyPI 无法访问 → 本地显式跳过，**CI 中 fail-closed**，未执行的检查不能算成功。两个方向均已验证：它能捕获修复前的准确状态（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`），并且对次要版本仅发出警告。

  - **本次 PR 审查产生的修复**——五名审查代理对差异进行了细致检查；以下各点在修复前均已通过**测量重现**，其中两项还是同一版本前文引入的回归。
- **已修复回归问题——`_NEWS_CITATION_REGEX` 存在指数级回溯。** 多段落修复将 `(?:[ \t]*$|[ \t]+.*)` 引入了重复结构：`[ \t]+` 与 `.*` 之间的空格共享存在歧义，而且这种歧义会随着迭代逐步放大。在不匹配该模式的 `>   texte` 行（完全合法的 Markdown 缩进）上测得：**14 行耗时 2 589 ms**，修复后为 0.04 ms，每增加一行，耗时约增加 9 倍。在 `--news` 模式下，一个很长且格式不符合要求的 blockquote 就足以让翻译卡住，直到作业超时，而且无法识别原因。现在重复结构会一次性消耗整行（`\n^>(?![ \t]*—).*`），因此每次迭代只有一种匹配方式。在包含 231 篇文章的真实语料上验证：**捕获结果零差异**，仍为 423 条引用，14 个多段落正文仍会被完整扩展。
    - **同时启用两个 provider flag 会静默地产生按量计费。** `--use_codex --use_mistral` 会被接受；`_select_provider_client` 优先测试 Mistral，`_resolve_provider` 则优先使用显式布尔值——两者最终都会指向 Mistral。因此用户本想使用订阅额度，却被按量计费，期间没有任何警告：这正是 `--use_codex` 用来防止的故障模式。现在，六个 provider flag 都会经过一个 `add_mutually_exclusive_group`。**行为变更**：此前同时包含两个 provider 的命令行会被静默接受，现在会在 `argument --use_mistral: not allowed with argument --use_codex` 上失败。
    - **工作结束门控在探针崩溃时仍会通过。** `scripts/check-release-ready.sh` 的十三项检查中，有四项遵循“捕获 stdout，若为空则得出结论”的模式，却从不检查返回码：异常（文件被重命名、`FileNotFoundError`）会写入 stderr，使 stdout 为空，检查便得出“没有需要报告的内容”。为防止该问题而编写的脚本内部又重现了“一个 `exit 0` 不能证明任何事情”的陷阱。现在，`probe()` 辅助函数同时要求返回码为零**且存在结束哨兵**；探针也拒绝在标记集合为空时得出结论——因为针对空集合的断言永远为真。证明如下：上文加入互斥组后，provider flag 通过一个 `*_group` 对象传递，而旧正则 `parser\.add_argument\(` 已无法匹配；二十一个 flag 中有 **六个** 静默脱离检查范围，门控却仍显示为绿色。
    - **密钥扫描漏掉了六个 provider 中的四个。** `[A-Za-z0-9]` 类排除了连字符：`sk-proj-…`（当前 OpenAI 格式）和 `sk-ant-api03-…` 会因第二个连字符而匹配失败，`AIza…` 也未被覆盖。现已扩大模式，并将 `.secrets.baseline` 排除在扫描之外。此外，`.env` 检查的是 `git diff --cached`，它只能看到索引：一个**已经提交**的 `.env`——最糟糕的情况——始终不会出现在其中。现在改为检查 `git ls-files`。
    - **Codex 的“token 预热”并不是真正的预热。** 测量表明：`codex login status` 不会触及 `~/.codex/auth.json`（mtime 和大小均未变化），其帮助文本写的是“显示登录状态”。然而注释却声称它会“按顺序执行一次” token 刷新，从而消除一次性轮换 token 的并发刷新风险。所宣称的保护并不存在；现在注释准确描述代码行为，真正的应对措施仍是 `max_jobs=4`。此外，检查现在遵循 `CODEX_BIN`，此前它会忽略该变量——未在 `PATH` 中配置 `codex` 的机器会因“未认证”而失败，导致诊断具有误导性。
    - **`.env` 在子 shell 中获取。** `detect_provider` 通过命令替换调用，因此它导出的变量不会传回：在 `.env` 中定义的 `GROK_BIN`、`GROK_HOME` 或 `REGEN_MODEL` 对 `main()` 中的读取不可见，后者会在配置正确时错误地得出“找不到 Grok 二进制文件”。
    - **并发量超过了所宣称上限的 50%。** 限制检查被放在 README/CHANGELOG 对启动之后：测得峰值为 **3 个 `max_jobs=2`**。对于 Grok，其每周额度与 Chat/Imagine/Voice 共享且无法测量，因此脚本自行施加的上限实际上没有得到遵守。最终计数虽会显示，却从未与 28 进行比较——缺少一个文件也不会被发现。
    - **Grok 输出契约：缺少 `stopReason` 现在会被视为失败。** 代码此前采用“`end_turn` **或缺失**”，而已公布的契约要求 `end_turn`。没有该字段的 payload，或 CLI 更新后将该字段重命名，都会让检查静默变成空操作。此外，`max_turn_requests` 不再被归类为速率限制（实际耗尽的是轮次预算；重试只会重现结果，却要付出 90 秒等待），而 `quota` 也不再输出速率限制标记——原因早已由 `_codex_is_rate_limited` 的文档字符串说明，只是 Grok 尚未执行。
    - **Gemini 级联现在按模型进行记忆化。** 它此前会在每个片段上从 `minimal` 重新开始，而默认模型会拒绝该配置：正常路径每个片段都会付出一次 400 往返，并重复打印相同警告。警告重复数百次后就不再有人阅读——这正是它变成掩护的方式。
    - **其他事项**：CI 中的拒绝消息被硬编码为 Codex，并将 `--use_grok_cli` 用户引导到 `OPENAI_API_KEY` 而不是 `XAI_API_KEY`；`provider.capitalize()` 显示“Grok_cli”和“Openai”；子进程基础设施的注释将“shim”泛化到两个 CLI，尽管 Grok 二进制是原生 ELF（正确的理由应是“会生成自身子进程的 agent”）；`subprocess` 上的十二个 SAST finding 已标记为 `# nosec` / `# nosemgrep` 并附带理由，缺少 `shell=True` 的列表形式使注入无法发生，而且文档内容从未经过 argv。
    - **不再有任何 secret 进入 agent 子进程。** 具名 deny-list 只保护了**计费**这一不变量（Codex 不带 `OPENAI_API_KEY`，Grok 不带 `XAI_API_KEY`）。测量表明：另外**七个 secret** 仍会进入每个子进程——Anthropic、Mistral、Google 和 Gemini 的密钥、另一个 CLI 的密钥，以及 `OPENAI_BASE_URL`；后者不是 secret，但会重新导向流量。然而这两个 CLI 都是**agent**，而 Grok CLI 在许多 Linux 机器上运行时没有可用的操作系统沙箱。现在改为按**变量名模式**过滤（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`），而不是使用具名列表，因此也能覆盖用户在 `.env` 中自行添加、但此代码并不知道的变量。CLI 不需要其中任何变量：认证保存在 `~/.codex` 和 `~/.grok` 中，从不依赖环境变量——已通过两个 provider 各自使用加固环境完成**真实翻译**进行验证。
    - **测试**：新增文件 `tests/test_review_hardening.py`（21 项测试），锁定 provider flag 的互斥性、`stopReason` 契约、news 正则的线性复杂度、CI 拒绝消息、Gemini 记忆化，以及子进程环境中不存在任何 secret。最后一项断言是**通用的**——即使出现列表中没有命名的密钥也会失败；而现有的清除测试只是其常量的镜像，除了检测自身循环的故障外无法发现任何问题。完整测试套件现为 **311 项测试**。

  - **新增两个 Grok provider**：`--use_grok`（xAI API，使用 `XAI_API_KEY` 密钥，按量计费）和 `--use_grok_cli`（官方 Grok Build CLI，从 Grok 订阅额度中扣除——原理与 `--use_codex` 相同）。
    - **API 模式，约 40 行**：由于 xAI endpoint 与 OpenAI 兼容，客户端和 `_call_openai` 可原样复用，只需更改 `base_url`。唯一必要的适配也惠及所有 provider：`finish_reason` 现在接受 `end_turn`，即 xAI 发送的形式，而 OpenAI 发送的是 `stop`。模型为：`grok-4.6`（质量）和 `grok-4.3`（经济）。需要注意，Grok 的经济模型仍是仓库中最昂贵的——每百万 token 为 $1.25/$2.50，而 `mistral-small-latest` 为 $0.15/$0.60：选择该 provider 是为了模型多样性，而不是价格。
    - **CLI 模式**：以 Codex 为模板，但有四项由实际情况强制产生的差异——prompt 通过文件传递（`--prompt-file`，CLI 不读取 stdin，片段若放入 argv 会出现在 `ps` 中）；输出是 stdout 上的单个 JSON 对象（既不是 JSONL，也不是 `-o` 文件）；订阅只公开 `grok-4.6` 和 `grok-4.5`；沙箱无法应用（见下文）。子进程启动已与 Codex 一起提取到 `_codex_run_process` 中，不影响已经过测试的 Codex provider 其余部分。
    - **实测表明，`exit 0` 毫无证明力**：未认证时，CLI 会将 `{"type":"error","message":"Not signed in."}` 写入**stdout**，且返回码为**0**。拒绝或轮次耗尽时行为也相同。因此输出契约要求四个条件同时满足：返回码为 0、不存在错误 payload、存在 `stopReason == end_turn`，以及文本非空。预检遵循同样逻辑：即使处于断开连接状态，`grok models` 也会以 0 退出，只有 stdout 中出现“not authenticated”才能得出结论。
    - **隔离：明确记录并接受不对称性。** Codex 运行在 `--sandbox read-only` 中，而 Grok 沙箱在许多较新的 Linux 机器上无法应用；原因有两个彼此独立、且没有 `sudo` 就无法绕过的系统限制：自 Ubuntu 24.04 起，AppArmor 会阻止非特权 user namespace（`bwrap: setting up uid map: Permission denied`，已在 Grok 之外复现）；当 `/run/podman` 为 `0700` 时，容器运行时套接字 deny-list 会失败（resolver 只会补救 `ErrorKind::NotFound`，EACCES 会变成致命错误）。核心陷阱是：无法应用的**集成式** profile 会**静默地以未隔离状态启动**。因此脚本默认不请求任何 profile，也绝不静默回退——它会在 stderr 上发出警告。保护依赖 CLI 的 `--deny` 规则，包括 catch-all `*`；这是唯一经过测量的 _fail-closed_ 层（未知前缀的规则会拒绝启动）。`GROK_TRANSLATE_SANDBOX=read-only` 可用于强制要求隔离；此时若机器无法满足要求，启动会失败。
    - **防护措施**：`XAI_API_KEY`、`GROK_API_KEY` 和 `GROK_SANDBOX` 会从子进程环境中移除（其中一个密钥会切换到按量计费；继承的 `GROK_SANDBOX` 会强制使用不适用的 profile，并产生误导性消息）；MCP/hooks/skills/agents 开关已禁用，`--disable-web-search`、`--no-subagents`、`--no-plan`、临时 workdir、CI 中的拒绝、会终止进程组的超时，以及速率限制退避均已启用。`--max-turns` 固定为 6，而不是 1：计数器会在工具轮次之后递增，设为 1 会截断输出。
    - **额度**：Grok 池按周计算，并**与 Chat、Imagine 和 Voice 共享**，且没有任何命令可以公开该额度——不同于 Codex，后者可通过 `account/rateLimits/read` 计算消耗。因此，`regen_translations.sh` 将并发限制为 2，并明确发出警告。
    - **测试**：新增文件 `tests/test_grok_provider.py`（24 项测试）。完整测试套件现为 **290 项测试**。
  - **已修复 bug——EN 多段落引用仅有部分受到保护（`--news` 模式）**：`_NEWS_CITATION_REGEX` 作为引用正文时，只接受一系列**连续**的 `>` 行。一旦引用跨越多个段落（由一行 `>` 空行分隔），只有最后一段会被捕获并替换为占位符；前面的段落则会发送给 LLM 并在返回时被翻译——这与 `--news` 所要保证的效果完全相反。现在重复结构接受内部的 `>` 空行，并改为非贪婪，从而会在位于斜体行之前的 `>` 空行处停止，而不是在遇到的第一处空行停止。
    - **实测影响**：在包含 198 篇文章的真实语料上，419 条引用中有 11 条受到影响。没有回归——新正则捕获的引用数量完全相同，只有多段落正文得到扩展（408 个正文保持不变，11 个得到扩展）；归属行 `> — …` 仍无法被吸收到正文中（lookahead 保留）。
    - **端到端证据**：在一篇 69 KB、被翻译成 ja/ar 的文章上，引用的第一段此前在日语中呈现为 `> GLM-5.3がオープンウェイト化。`，在阿拉伯语中也同样被翻译；现在则保持为 `> GLM-5.3 is now open-weight.`。英文引用行数从 9 恢复为 10，与源文档一致。
    - 需要注意：下游验证器不会检测到此缺陷，因为它们只检查引用是否存在，不检查引用是否完整。
  - **默认 provider 的实测节省**：只要模型以 `gpt-5` 开头，`_openai_extra_kwargs` 就会发送 `reasoning_effort="medium"`，包括在 `--eco` 中的情况。在 `gpt-5.4-mini` 上翻译一个十词句子的测量结果为：`medium` → 45 个 reasoning token 和 65 个输出 token；`none` → 0 和 14。推理对翻译没有帮助，却会在每个文件的每个片段上产生费用。现在默认值在 `--eco` 中变为 `none`，其他情况下仍为 `medium`；通过 CLI 显式传入的值仍具有优先级。`--reasoning_effort` 现在除 `low`/`medium`/`high` 外，还接受 `none` 和 `xhigh`（并非所有模型都接受这些值：例如 `minimal` 会被 `gpt-5.4-mini` 拒绝——现有的无参数重试会处理这种情况）。
  - **SDK 更新与 Gemini 迁移**：`google-generativeai`（支持已于 2025-11-30 结束，仓库已归档）替换为统一 SDK **`google-genai`**——先执行 `genai.Client(api_key=...)`，再执行 `client.models.generate_content(model=, contents=, config=)`；系统 prompt 通过 `system_instruction` 传入，而不再与片段拼接。`mistralai` 升级至 **2.9.4**（导入变为 `from mistralai.client import Mistral`；旧导入会抛出 `ImportError`，已在 wheel 中验证），`anthropic` 升级至 **0.125.0**，`openai` 升级至 **2.54.0**——这些是切换到 `httpx2` 前的最后版本，以避免在 venv 中同时存在两套 HTTP 栈。因此 `httpx` 0.28.1 和 `pydantic` 2.13.5 也随之解锁。
  - **两个由真实测试而非文档捕获的回归问题**：
    - `anthropic` ≥ 1.0 会在客户端拒绝非流式调用，前提是其 `max_tokens` 暗示请求可能超过 10 分钟（`ValueError: Streaming is required...`）。0.34.2 中不存在此防护，导致所有使用 `max_tokens=32768` 的 Claude 调用失败。现已通过显式 `timeout` 修复（`CLAUDE_TIMEOUT`，默认 900 秒），因此无需为只使用完整响应的调用切换到流式模式。
    - `thinking_level="minimal"` 只被 Gemini 模型目录中的一部分接受：`gemini-3.1-flash-lite` 支持它，而 `gemini-3.7-flash` 和 `gemini-3.1-pro-preview` 会以 400 拒绝。因此加入 `_gemini_generate_with_fallback`，采用 `minimal` → `low` → 不设置 thinking_config 的级联方式，仿照已有的 OpenAI 回退机制——优化参数绝不能导致翻译失败。
  - **更新默认模型**，每个模型都通过真实调用验证：OpenAI 从 `gpt-5.5` → **`gpt-5.6-terra`**（在包含 28 个批次的任务上降低 60%）以及从 `gpt-5.4-mini` → **`gpt-5.6-luna`**（降低 73%）；Claude 从 `claude-sonnet-4-6` → **`claude-sonnet-5`**（更便宜且更新）以及从 `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（不带日期的规范 ID）；Gemini 从 `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**，以及从 `gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（稳定版本，且比 `3.5-flash-lite` 更便宜）。
Mistral 保持不变，`mistral-large-latest` 仍然是四者中性价比最高的。需要注意的是，没有比 `gemini-3.1-pro-preview` 更新的 Gemini Pro 系列模型——2026 年 5 月宣布的 Gemini 3.5 Pro 从未发布；3.5/3.6/3.7 系列全部都是 Flash。
  - **切换到 Gemini 前进行了实测 A/B 对比**：使用 `gemini-3.1-pro-preview` 将 `README.md` 翻译成日语，然后使用 `gemini-3.7-flash`。结构完全一致（21 个列表、18 个代码块、13 个 HTML 链接、13 张图片，所有 URL 均保留），耗时**8 秒，而不是 48 秒**。由于没有公开基准比较这两个模型在翻译或非拉丁文字脚本方面的表现，否则这次切换只能建立在简单推测之上。
  - **过滤 Claude 响应块**：`_call_claude` 会在不筛选类型的情况下执行 `block.text for block in response.content`。自适应推理模型（Sonnet 5 及以后版本）会插入一个 `thinking` 块，其中公开的是 `.thinking`，而不是 `.text`——翻译会在第一个片段遇到不透明的 `AttributeError` 时崩溃。现在会排除 `thinking`、`redacted_thinking`、`tool_use` 和 `tool_result` 块（使用否定列表，以便对携带文本的未知类型保持宽容），如果响应中完全没有文本块，则会抛出明确错误。每次调用都会传入 `thinking={"type": "disabled"}`。
  - **重新同步 `MODEL_TOKEN_LIMITS`**：移除已过退役日期的模型（`magistral-*` 系列已于 2026-07-31 退役，`gemini-2.0-*` 于 2026-06-01，`gemini-3-pro-preview` 于 2026-03-09，以及 `claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。修正限制：Mistral 128K → **256K**（Large 3 / Small 4 系列），Gemini 1 000 000 → **1 048 576**（实际输入限制），`claude-opus-4-5` 200K → **1M**，`gpt-5.6-*` 系列 400K → **1.05M**。新增 Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest` 和 `ministral-*` 系列。需要注意：这些限制仍然只是参考值，因为 `translate()` 会将分段上限限制为 `min(16000, limite)`。

  - **Provider `--use_codex`**：第五个 provider，通过非交互模式驱动官方 Codex CLI（`codex exec`），而不是调用按使用量计费的 API。翻译消耗的是已经付费的 ChatGPT 订阅额度。这是 OpenAI 为此用途记录的唯一方式：计划可用性矩阵将「Codex SDK、`codex exec` 和可脚本化工作流」列为 Plus/Pro/Business/Enterprise 可用，而 `~/.codex/auth.json` 的 token 无法验证 Platform API 调用（本脚本也从不读取它们——身份验证及其刷新仍由 CLI 管理）。
  - **Codex 二进制文件现在可通过 pip 安装，不再只能通过 npm 安装**：`_resolve_codex_binary()` 会依次在 `CODEX_BIN`、`PATH`，然后是由 OpenAI 发布的官方 Python 包 **`openai-codex-cli-bin`** 中查找二进制文件（这是 `openai-codex` SDK 的依赖项）。因此，Python 项目不再需要全局安装 npm 即可使用 `--use_codex`。该包不会加入 `requirements.txt`：二进制文件约 250 MB，否则所有用户都会被强制安装一个可选 provider。已完成端到端验证：当 `codex` 不在 `PATH` 中时，解析过程能够找到打包的二进制文件，并在 6 秒内完成完整翻译。
  - **“订阅模式”保证**：`OPENAI_API_KEY` 和 `CODEX_API_KEY` 会从子进程环境中移除。没有这一保护，`.env` 中存在的密钥可能会让 Codex 切换到按使用量计费，且完全没有可见提示——这正是该 provider 要避免的情况。
  - **通过测试锁定 CLI 陷阱**：
    - `codex exec` 即使提示词通过参数传入，也会读取 stdin：如果不关闭 stdin，命令会一直等待直到超时，却始终不会调用模型（复现结果：180 秒后退出码为 124，输出 0 字节）。因此 `communicate(input=...)` 是强制要求。
    - 通过 npm 安装的 `codex` 是一个 Node shim，它会 `spawn` 真正的 Rust 二进制文件：后者是 Python 进程的**孙进程**，并且会在 `SIGKILL` 对 `subprocess.run(timeout=)` 执行后继续运行，从而持续消耗额度。因此需要 `Popen(start_new_session=True)` + `os.killpg`。
    - CLI 可能在输出 `turn.failed` 后仍以 0 退出：除了检查返回码，还会检查 JSONL 输出（`--json`）；如果返回码为 0 但缺少 `-o` 文件，则会抛出明确错误，而不是生成空片段。
  - **速率限制退避**：CLI 不实现内部重试（`max_retries = 0`）。分类依据 JSON payload 的结构（`status: 429` / `error.type`），而不是子字符串——“quota”一词既会出现在可恢复的 429 中，也会出现在不可恢复的 `insufficient_quota` 中。
  - **CI 防护**：如果定义了 `CI` 或 `GITHUB_ACTIONS`，则拒绝 `--use_codex`。订阅身份验证不适用于共享 runner，OpenAI 也明确不建议在公开仓库中使用此工作流。
  - **模型**：`gpt-5.6-sol`（质量）和 `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` 系列同时适用于 CLI 和 Platform API，但 ChatGPT 账户并不一定拥有全部权限：allowlist 在服务器端应用，不进行本地验证，使用异常模型时会触发警告。在 Plus 计划中，Luna 每个 5 小时窗口提供 250–2,000 条消息，而 Sol 提供 10–100 条：对于所有批处理，推荐使用 `--eco` 模式。
  - **已修复的 bug——`regen_translations.sh` 在完全成功后仍报错**：`trap ... EXIT` 引用了 `failed_log`，这是 `main()` 中的一个 `local` 变量，但 trap 执行时该变量已经不存在。在 `set -u` 下，这会抛出 `failed_log: unbound variable`，使脚本以 1 退出，尽管 28 个翻译均正确——这会在重新生成后、最昂贵的步骤中，刚好中断 `release.sh --auto`（`set -e`）。现在该变量改为全局变量，trap 会检查其是否存在。一个有用的副作用是：此前被此错误掩盖的真实翻译失败，如今会重新出现在最终摘要中。
  - **`REGEN_MODEL`**：来自 `regen_translations.sh` 的新环境变量，可覆盖 provider 的默认设置，强制使用指定模型，例如使用 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`，在订阅额度内通过高端模型重新生成，而不是使用面向吞吐量的 `--eco` 模型。
  - **`regen_translations.sh`**：`REGEN_PROVIDER=codex` 现可通过显式 opt-in 使用（绝不自动检测，以免在用户不知情的情况下消耗订阅额度）。在开启并行处理前，会先顺序刷新一次 token——Codex 刷新机制是轮换式且一次性的，并发任务会使 `codex login` 会话失效——并将并发数降至 4。
  - **相关重构**：`_dispatch_provider_call` 通过一个返回 provider 名称的 `_resolve_provider()`，将参数从 8 个减少到 6 个，而不是在整个调用链中传播第四个布尔值。为保留使用最小 `Namespace` 调用 `translate(..., use_mistral=True)` 的测试，显式布尔值仍优先于 `args`。
  - **测试**：新增文件 `tests/test_codex_provider.py`（48 个测试），覆盖 argv、清理后的环境、反前言契约、静默失败、timeout/killpg、退避、preflight、provider 解析、Gemini 推理级联、Claude 块过滤以及多段新闻引用。完整测试套件增至 290 个测试。
  - **实际验证**：通过 Codex 将项目的 `README.md` 翻译成**14 种语言**，所得结果与参考翻译的结构完全一致（14 个代码块、24 个标题、25 行表格、13 个 HTML 链接、13 张图片、19 个 URL，代码块逐字符一致，且没有任何 placeholder 残留）。对于一篇 69 KB 的新闻文章，在 `--news` 模式下，`gpt-5.6-luna` 和 `gpt-5.6-sol` 的输出均通过了下游应用验证器（en/ja/ar）。通过 `account/rateLimits/read` 测量的消耗保持在计数器舍入阈值以下（`--eco` 模式下 5 小时窗口为 0%）。

- **1.9.2** 修复带嵌套括号或 FR 前缀的新闻署名 URL 提取（2026-05-11）：

  - **已修复的 bug**：`_protect_news_quotes` 中的署名 URL 提取使用了正则表达式 `re.search(r"\((.+?)\)", attribution)`（括号之间的惰性捕获）。对于类似 `(relayé par [@user sur X](https://x.com/.../123))` 的署名（嵌套括号：外围的 `(` 加上 Markdown 链接中的 `]()`），捕获会在遇到第一个 `)` 时停止 → 字符串被截断，并包含 FR 前缀：`relayé par [@user sur X](https://x.com/.../123`（缺少末尾的 `)`）。结果是：`_validate_news_post` 会在翻译输出中查找该字符串，并始终失败（原因有两个：`)` 被截断，以及“relayé par”被翻译成 `relayed by`/`weitergeleitet von`/……）。完整的 low → medium → high → gpt-5.5 级联无法通过。
  - **修复**：正则表达式改为 `re.search(r"\]\(([^)]+)\)", attribution)`——专门定位 Markdown 链接中的 `](url)`，**仅捕获纯 URL**（不含 FR 前缀，也不截断），并通过翻译期间的 `#URL{N}#` placeholder 保持不变。能够稳健处理以下两种问题模式：
    - `(relayé par [@account sur X](url))` — 嵌套括号
    - `via [@source](url)` 或 `selon [@author](url)` — 没有外围括号的 FR 前缀
  - **测试**：在 `test_silent_failure.py` 的 `TestNewsCitationExtraction` 类中新增 2 个测试：
    - `test_extract_attribution_url_with_nested_parens`（复现的 Genspark CEO E2B 精确案例）
    - `test_extract_attribution_url_with_french_prefix`（带 `via` 的变体）
  - **覆盖缺口**：`check-editorial-coverage.py` 验证编辑语法，但不验证 translator 是否能够翻译。一个可能的改进（不在 v1.9.2 范围内）是增加检查，在发布前通过 dry-run 模拟署名提取，以检测有风险的模式。

- **1.9.1** 修复翻译 marker 注释中 CTA 标签的 i18n（2026-05-10）：

  - **已修复的 bug**：翻译文件顶部 marker 横幅中 CTA 链接的 `[Voir le projet sur GitHub ↗]`，对所有目标语言都保持**法语**，而不是遵循 `target_lang`。LLM 永远看不到它（由 Python 侧组装，以保留 URL 和仓库 slug），因此翻译阶段无法修正。自 v1.9 添加 `marker` 格式以来一直存在这一静默回归。
  - **修复**：新增 `_VIEW_PROJECT_LABELS` 常量，将 15 种语言映射到本地化标签。现在 `_translation_note_invariants(target_lang)` 和 `_assemble_translation_note_paragraphs(phrase, target_lang)` 会传递目标语言。未知语言时回退到 `fr`（安全处理，不会触发 KeyError）。
  - **测试**：调整 `test_source_emits_three_paragraphs_repo_title_description_link`（target_lang `ja` → 预期日语标签）。新增 2 个测试：`test_source_link_label_localized_per_target_lang`（参数化覆盖 7 种语言，包括拉丁、表意和辅音音素文字脚本）以及 `test_source_link_label_falls_back_to_french_for_unknown_target`。总计：`test_translation_note_position.py` 中有 40 个测试（原为 38 个）。
  - **向后兼容**：签名带有默认值 `target_lang="fr"`——没有 `args.target_lang` 的外部编程调用方仍可正常工作，无需修改。
- **1.9** 修复静默失败 + 完整质量工具链 + 多位置翻译备注（2026-05-07）：
  - **多位置翻译备注 + “embed card” 格式标记**：
    - 新增 CLI 选项（附加功能，默认值不变 → **不破坏兼容性**）：
      - `--note_position {top,bottom,both}`（默认值：`bottom`）：将备注放置在已翻译文件的顶部、底部，或两个位置。
      - `--note_format {legacy,marker}`（默认值：`legacy`）：
        - `legacy` 严格复现 v1.8 的行为（粗体段落 `**…**`），**逐字节一致**。
        - `marker` 输出一个不可见的 Markdown 链接引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），后接一个结构化的**三段式 blockquote**，用于呈现类似 “GitHub repo embed card” 的效果：以行内代码显示项目标题（`**\`ai-powered-markdown-translator\`\*\*`）、由 LLM 翻译的描述，以及带可见箭头的 CTA 链接（`[Voir le projet sur GitHub ↗](URL)`）。可由 remark 插件在构建时处理（参见 blog jls42.org → 插件 `remark-translation-banner`）。
    - **永不发送给 LLM 的不变量**：仓库标题和 GitHub URL 在描述句翻译完成后由 Python 端组装。LLM 永远看不到 slug `ai-powered-markdown-translator` 或 `https://github.com/jls42/...`，从而保证任何 renderer/case/scheme 都不会被修改。
    - **感知 frontmatter 的插入**：在 `top` 或 `both` 模式下，备注会插入到 YAML frontmatter 的**结束 `---` 块之后**（确保 Astro Content Collections / gray-matter 安全）。Helper `_split_frontmatter` 会检测文件开头的 `---\n…\n---\n` 并保持其完整性；若 frontmatter 已打开但没有闭合 fence，则**抛出 `RuntimeError`**（文件会进入 `failed_files`，而不会带着位置错误的备注写入）。
    - **模型 sanitizer 白名单**：`_sanitize_model` 将所有不属于 `[A-Za-z0-9._:/-]` 的字符替换为 `_`；若结果为空则回退到 `unknown`。这与 Astro remark 插件侧的验证器保持一致，并消除会破坏 marker 格式的字符（空格、引号、括号、逗号等）。
    - **内部重构**：`_append_translation_note`（1 个单体函数）→ 7 个纯 helper（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。Builder 与 composer 分离（builder 返回不带分隔符的纯块，composer 根据位置应用 `\n\n`）；生产代码和源代码 helper 共用同一个三段式组装器。
    - **`_quote_lines` 保留空行**：为每行添加 `> ` 前缀，将空行转换为仅含 `>` 的行。这样 mdast 能在 blockquote 中识别出三个不同的段落（标题 / 描述 / 链接），而不是一个带换行的单一段落。
    - **`_build_translation_note_block` 自适应**：根据 LLM 保留的段落数量处理（3 段 = 完整 card 格式，2 段 = 句子 + 链接，1 段 = 回退格式）。当检测到 Markdown 链接 `](` 时，单段回退格式**不再包裹在 `**...**` 中**（避免在链接周围使用 `<strong>` 导致脆弱的渲染）。
    - **向后兼容**：`getattr(args, "note_position", "bottom")` 和 `getattr(args, "note_format", "legacy")` 位于 `_compose_with_notes` 侧——没有这些属性的 Namespace（现有测试、外部程序化调用）无需修改即可继续工作。
  - **修复长文本翻译的静默失败**：
    - 所有 provider（OpenAI、Mistral、Claude、Gemini）均增加翻译后语言验证：确定性层（源文本片段逐字找回）+ 概率层（`langdetect`）。
    - `finish_reason` / `stop_reason` 白名单：任何不在白名单中的状态（截断、content_filter 等）均抛出 `RuntimeError`。
    - Claude 的 `max_tokens`：`4096` → `32768`（避免 16k 分段发生潜在截断，并为 FR→JA/ZH/KO/AR/HI 的跨文字体系转换预留余量）。
    - 感知标题的分段：在分段的后半部分优先放置 H2/H3（每个分段都从完整的语义章节开始）。
    - 错误传播至非零退出码：`translate_markdown_file` 返回类型化状态 `success` / `failure` / `skipped`；如果至少一个文件失败，`main()` `sys.exit(1)`（单文件和批处理均适用）。
    - 所有 provider 增加空内容防护、源文本/输出文本合理性比例检查（≥ 500 个字符时，< 5% 则拒绝）、代码占位符验证（`#CODEBLOCK`/`#INLINECODE`）、LLM 后规范化（修复粘连到标题的分隔符/链接）、`BadRequestError` 在不带 `reasoning_effort` 的情况下重试。
    - 新增依赖 `langdetect==1.0.9`。
  - **pre-commit 质量工具链**（“完整 EurekAI 类型”，14 个 hook）：
    - Pre-commit：ruff（lint+format）、shellcheck、prettier（md/yaml/json）、detect-secrets（保护 4 个 API key）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（空白字符、EOF、大文件、shebang 等）。
    - Pre-push：mypy（逐步启用的 lax 模式）、Opengrep SAST（translate.py + scripts/）、pip-audit（初始 reporting 模式）、unittest discover（tests/ + scripts/tests/）。
    - 位于 `scripts/` 的本地 wrapper 使用 `./venv/bin/python`。
    - `scripts/audit_verdict.py`：使用 11 个 unittest 测试解析 pip-audit JSON，这是 jls42-astro parser 的 Python 移植版。
    - 修复最初的 7 个 ruff 违规：B904（raise from）×2、B007（未使用的 dirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）。
    - Lizard 暂时排除 `translate.py`（4 个函数的 CCN 为 21-47，计划重构）——对 scripts/ 保持严格 gate。
  - **SonarCloud + 全面覆盖率**：
    - GitHub Actions 工作流 `SonarCloud`（sonarcloud.yml + sonar-project.properties）：每次 push 和 pull-request 都执行分析，覆盖率通过 `coverage.xml` 提供。
    - README 顶部新增 11 个 SonarCloud badge（Quality Gate、Security/Reliability/Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）。
    - `tests/test_silent_failure.py`（`unittest` stdlib）：覆盖 silent-failure 错误链的六个环节。
    - `tests/test_orchestration.py`（+79 个测试）：覆盖 `translate.py` 的编排层（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` TypeError + BadRequestError 回退、o1-series prompt 格式、`_validate_translation_output` 的 early-return 分支）。
    - `scripts/tests/test_audit_verdict.py`：通过 subprocess 覆盖 `main()`（stdin/stdout）以及 `if __name__ == "__main__"` 代码块。
    - **新代码覆盖率**：75.5% → 约 98%（translate.py 98%，scripts/audit_verdict.py 97%）。
  - **测试**：`tests/test_translation_note_position.py` 覆盖位置 × 格式矩阵（包括 E2E `marker+top|bottom|both` 和 `legacy+top|bottom|both`）、多行前缀、逐字节兼容性回归（golden literal）、sanitizer、frontmatter 拆分（包括未闭合 fence 时抛错）、三段式格式、两段式回退、单段 + Markdown 链接防护，以及关键防护测试 `TestLLMPayloadExcludesInvariants`，断言标题和 URL 永远不会发送给 LLM。**190 个测试通过**，无回归。
  - 文档：`README.md`（法语版 + 14 个翻译）含 badge，`CLAUDE.md`（详细的 pre-commit 工作流 + CI 监控），重新生成 28 个翻译。
- **1.8** `--news` 模式 + 2026 模型更新（2026-03-17，标签 `v1.8`）：
  - 更新默认模型（2026 年 3 月）：
    - OpenAI 质量版：`gpt-5` → `gpt-5.4`
    - OpenAI 经济版：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 质量版：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - 为 `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）和 `gemini-3.1-pro-preview`（1M）添加 token 限制。
  - 初始 `--news` 模式：使用占位符 `#NEWSQUOTE\d+#` 保护英文新闻引用，使用 `LANG_FLAGS` 映射（15 种语言），并处理目标语言的标志。
  - 恢复前验证新闻占位符（回归问题：LLM 删除占位符会静默地产生不含引用的输出）。
  - 使脚本 `regen_translations.sh` 具备可移植性（绝对路径，不依赖 pwd）。
  - 在 README/CHANGELOG 的语言栏中添加法语链接，重新生成 28 个翻译。
- **1.7** 新功能：
  - 提供 `--keep_filename` 选项，在翻译时保留原始文件名。
  - 支持 `.env` 文件，以自动加载 API key。
  - **保留行内代码**：反引号（`` `...` ``）现在会在翻译期间受到保护。
  - 改进系统 prompt：
    - 更好地处理 YAML frontmatter 中的引号。
    - 保护模板变量 `{variable}`。
    - 禁止未请求的译者备注。
  - 在 jls42.org 博客迁移中成功测试 364 个文件。
- **1.6** 新功能：
  - 支持 Google Gemini 翻译 API（`--use_gemini`）。
  - 更新 2026 年默认模型：
    - OpenAI：`gpt-5`（质量版）、`gpt-5-mini`（经济版）
    - Claude：`claude-sonnet-4-5`（质量版）、`claude-haiku-4-5`（经济版）
    - Gemini：`gemini-3-pro-preview`（质量版）、`gemini-3-flash-preview`（经济版）
  - 经济模式（`--eco`），用于使用更快且成本更低的模型。
  - 单文件翻译（`--file`），无需遍历目录。
  - 简化新的命名模式：`{base}-{lang}.md`。
  - 提供 `--include_model` 选项，以保留包含模型名称的旧格式。
  - 支持未列出的模型，默认 token 限制为 128k。
  - README 翻译为 14 种语言。
- **1.5** 改进：
  - **更新 API key 和默认模型：**
    - **OpenAI：** 从 `DEFAULT_MODEL_OPENAI` 更新为 `"gpt-4o"`。
    - **Mistral AI：** 从 `DEFAULT_MODEL_MISTRAL` 更新为 `"mistral-large-latest"`。
    - **Anthropic Claude：** 添加 `DEFAULT_ANTHROPIC_API_KEY`，并将 `DEFAULT_MODEL_CLAUDE` 更新为 `"claude-3-5-sonnet-20240620"`。
  - **优化翻译 prompt：**
    - 直接翻译和翻译备注所使用的 prompt 得到增强，以提高清晰度和效率，其中包括关于保留元数据以及特定格式元素的详细指令。
  - **代码重构：**
    - 使用 `Mistral` 类替换 `MistralClient`，用于初始化 Mistral AI 客户端。
    - 重新组织 import，以提高可读性和可维护性。
    - 改进文本分段和代码块处理，在翻译时保留原始格式。
  - **输出文件管理：**
    - 反转输出文件名中的模型和语言顺序（例如 `f"{base}-{args.target_lang}-{args.model}.md"`），从而便于组织和查找翻译。
  - **其他改进：**
    - 删除不必要的空行，清理代码。
    - 进行细微调整，以改善脚本的结构和可读性。
- **1.4** 新功能：
  - 支持 Anthropic Claude 翻译 API。
  - 优化 prompt，以提高清晰度和效率。
  - 进行细微调整，以改善代码维护。
- **1.3** 改进和新功能：
  - 改进代码块处理。
  - 改进输出文件处理。
  - 改进现有文件检测。
  - 提供 `--force` 选项以强制翻译。
  - 反转输出文件名中的模型和语言顺序。
- **1.2** 修复变更日志。
- **1.1** 新增 Mistral AI API 支持。
- **1.0** 初始版本——支持 OpenAI API。

**使用 gpt-5.6-luna 将文章从法语翻译成中文。**
