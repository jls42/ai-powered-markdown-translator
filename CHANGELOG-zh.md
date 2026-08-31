### 变更日志

🌍 [法语](CHANGELOG.md) | [英语](CHANGELOG-en.md) | [西班牙语](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [德语](CHANGELOG-de.md) | [日语](CHANGELOG-ja.md) | [韩语](CHANGELOG-ko.md) | [阿拉伯语](CHANGELOG-ar.md) | [印地语](CHANGELOG-hi.md) | [意大利语](CHANGELOG-it.md) | [荷兰语](CHANGELOG-nl.md) | [波兰语](CHANGELOG-pl.md) | [葡萄牙语](CHANGELOG-pt.md) | [罗马尼亚语](CHANGELOG-ro.md) | [瑞典语](CHANGELOG-sv.md)

- **1.11.0** 发布到 PyPI：先执行 `pip install ai-powered-markdown-translator`，再执行命令 `aipmt`，无需克隆仓库（2026-08-31）：

  - **单文件脚本变成可安装软件包。** `translate.py` 从根目录移至 `src/aipmt/translate.py`，并提供控制台入口 `aipmt` 及其等价形式 `python -m aipmt`。克隆的仓库仍是贡献所必需的——测试、28 种翻译和质量工具都在那里——但使用工具时不再需要。

    - **导入名称是 `aipmt`，绝不是 `translate`**，因为冲突确实存在，而且不会显式报错。PyPI 软件包 `translate`（v3.8.1，最近一次上传于 2026-07-06）会安装同名目录。在虚拟环境中复现：目录优先于模块，`translate.main` 消失，入口在 `AttributeError` 处崩溃——而 `pip check` 却返回“No broken requirements found”，rc=0。用户只需执行一次简单的 `pip install translate`，就足以在没有可用诊断的情况下破坏 CLI。使用真实 wheel 进行反证：在该软件包之上执行 `pip install translate`，前后均为 `aipmt --help` rc=0，两个 CLI 可以共存。
    - **发行名称较长，命令名称较短。** `ai-powered-markdown-translator` 让软件包能够通过 PyPI 搜索找到；仅使用缩写会让不了解项目的人无法搜索到，而发布的目的正是让项目能够被找到。两个看似合理的候选名称经核验后被排除：`ai-markdown-translator` 自 2024 年起已被 npm 上一个用途相同的工具占用，该工具比本仓库早 17 个月；而 `aimt` 只比 `aim`（v3.29.1）多或少一个字母，后者是同一领域中仍在活跃维护的软件包——这是最容易造成长期混淆的配置。顺带说明一个方法陷阱：`pypi.org/project/<nom>/` 对任何名称都返回 200（反机器人页面），只有 JSON API 的结果才可信。
    - **采用 `src/` 布局，而不是扁平软件包。** 扁平软件包会保留测试中的六个 `sys.path.insert(..., "..")`，而这正是缺陷所在：它们会导入源代码树而不是软件包，从而掩盖任何打包错误。实际代价只是增加一条替换规则。

  - **修复——工具安装后，用户的 `.env` 会被忽略。** 不带参数的 `load_dotenv()` 不是从当前目录向上查找，而是从调用方文件所在位置开始，因此会从 `site-packages` 开始查找。使用从一个拥有自身 `.env` 的项目中启动的真实控制台入口进行测量：`find_dotenv()` 返回 `''`，且密钥未被加载；而 `find_dotenv(usecwd=True)` 能找到该密钥。只要工具还仅从克隆的仓库中运行，这个错误就不会出现；发布后它会变成系统性问题，唯一症状是在配置正确时提示 API 密钥“缺失”。

  - **三个门禁在停止检查任何内容后本会全部变绿。** 它们在移动之前就被有意加固：在变更之后才编写、且本应捕获该变更的防护措施，无法证明任何事情。每个门禁在原始仓库上为绿色，在迁移副本上则变为红色——两个方向都经过测量。

    - **Lizard 会无声地忽略不存在的路径**：rc=0，并输出“0 file analyzed”。复杂度门禁会从 158 个函数 / 2247 个 nloc 变成 3 个函数 / 34 个 nloc，并且输出为零字节。现在 scope 是一个数组，每个条目都会检查其是否存在。
    - **对不存在的模块执行 `coverage run --source=` 不会失败**：仅在 stderr 上发出警告，unittest 和 `coverage xml` 都返回 rc=0，报告仍会发布——但从 1453 个语句缩减到 141 个。项目看起来会很健康，因为几乎没有内容被分析。两个下限用于守住报告：总数下限，以及所测量最大文件的下限。
    - **翻译新鲜度探针在结构上无法感知调用形式**：它依赖 argparse 标志，而文件重命名恰恰不会改变这些标志。复现结果：模块被移动，但 15 个 README 仍记录着一个不存在的命令，判定为“没有过期翻译”。因此新增第 7 个部分，检查的是调用形式而不是选项；同时让 Lizard hook 面向脚本的真实 scope——其 `files:` 在不再匹配时不会让 pre-commit 失败，而是直接跳过它。

  - **`requires-python = ">=3.10"` 不再只是一项声明。** `sonar-project.properties` 早已声明支持 3.10-3.12，但从未真正运行过这些版本，因为开发机只有 3.12——这是一个会因发布而公开的内部矛盾。现在有一个测试工作流会在 3.10、3.11 和 3.12 上运行完整测试套件，并安装软件包，因此也会验证其公开依赖范围。

  - **设置最低版本，不设上限。** `requirements.txt` 仍是经过测试的锁定版本，`[project.dependencies]` 则成为公开契约：发布锁定文件中的精确版本会与拥有其他软件包的用户产生冲突。同样不设置 `<N+1` 上限——这会与 `check-deps-fresh.sh` 直接矛盾，后者会让任何主版本落后都触发发布门禁失败。最低版本集合可以解决这一问题，而反证 `openai==1.0.0` 会输出 `ResolutionImpossible`，证明该检查能够区分情况，而不是一概接受。此外还有一项保护措施，禁止 `pyproject.toml` 的版本与 CHANGELOG 中的版本不一致：PyPI 不允许重复使用同一个版本号。

  - **在全新的虚拟环境中完成端到端验证**：大小为 69 768 字节的 wheel 只包含 `aipmt/*.py`、dist-info 和许可证；`aipmt --help` 返回 rc=0，并显示 22 个标志；`python -m aipmt` 显示“usage: aipmt”，而不是“usage: \_\_main\_\_.py”；安装后的 `pipx` 正常工作；最重要的是，**从任意用户目录执行一次真实的 fr→en 翻译**，粗体、列表、内联代码、链接和 URL 均得到保留，代码块未被翻译。318 项测试通过，迁移前后标识符列表逐字节完全一致——这才证明没有测试被禁用，而不是那句“OK”。

- **1.10.0** Provider `--use_codex`（ChatGPT 订阅配额）、更新 SDK 和模型、修复多段新闻引用（2026-08-29）：

  - **安全审查——PR 设置了两道防护措施，却没有在所有路径上真正落实**：

    - **Codex 预检会把整个 `.env` 传给二进制程序。** `_codex_preflight` 调用 `subprocess.run` 时**没有 `env=`**：子进程继承了完整的 `os.environ`，也就是由 `load_dotenv` 加载的全部 `.env`。使用经过检测的假二进制程序进行测量：预检接收到**七个秘密**——六个 provider 的密钥以及一个 `GITHUB_TOKEN`；而对应的 `_grok_preflight` 则为**零个**，因为它正确传递了 `env=_grok_env()`。这一不一致存在于 PR 内部：`_strip_secret_env` 的存在正是为了维护这一不变量，而且就在几行之外。现在抽取出一个 `_codex_env_base()`，由两条路径共享；修复后的测量结果：两侧均为 0 个秘密。
    - **“`--deny` fail-closed”的属性并未覆盖实际使用的形式。** 注释以“未知前缀规则会拒绝启动”为理由，说明了 Grok 的全部隔离措施。在 `grok 1.0.13` 上测量后发现，该验证**仅适用于带括号的形式**：`--deny 'CeciNestPasUnOutil(*)'` 会拒绝启动（“unknown tool prefix”），而 `--deny 'CeciNestPasUnOutil'` 会被静默接受。然而 `GROK_DENY_RULES` 只使用裸名称——因此，如果 xAI 侧重命名工具，就会在没有任何信号的情况下移除唯一经过测量的隔离层，而此时操作系统沙箱本身已经不适用。八条命名规则都改为 `Prefix(*)`，并逐条验证为 CLI 已知前缀；catch-all `*` 保持字面形式，这是唯一被接受的形式。一个测试会阻止未经验证的形式再次出现。
    - **其他方面也已完成清洁验证**：不存在命令注入（所有地方都使用列表形式，从不使用 `shell=True`；文档内容通过 stdin 或 `--prompt-file` 传递），不存在不安全反序列化（仅使用 `json.loads`，并带有类型保护），路径遍历修复在七个有效载荷上均未发现绕过方式，并且 `--deny '*'` 确实由 CLI 应用（在一次越过工作目录的读取中观察到 `DENY_ENFORCED`）。
    - 前文新增的新鲜度检查顺便绕过了自身原则：当 PyPI 请求失败时，软件包会被静默跳过，门禁仍显示绿色。现在它会统计实际完成比较的软件包数量，并在覆盖范围不完整时失败。

  - **依赖已升级，并增加两道防护以防止延迟再次发生**：

    - **延迟真实存在且持续时间很长**：`openai` 从 2.54 升至 **3.6.0**，`anthropic` 从 0.125 升至 **1.2.0**，`certifi` 从 2024.8.30 升至 **2026.7.22**——这意味着用于验证所有 provider TLS 连接的根证书存储落后了两年。原因已经确认：**此前不存在 `.github/dependabot.yml`**。没有该文件时，GitHub 只会启用 _security updates_，Dependabot 只会为受 CVE 影响的依赖提出 PR——这解释了为什么它升级了 `urllib3` 和 `idna`，却让两个 SDK 从一个主版本落后到另一个主版本。
    - **两个主版本可以共存且不会冲突**，与先前推理所担心的情况相反：`openai` 3.x 和 `anthropic` 1.x 会迁移到 **`httpx2`**，而 `mistralai` 和 `google-genai` 仍使用 `httpx<1`，但它们是两个不同的发行版。通过实际安装验证后，又对 **7 条 provider 路径进行了端到端测试**——OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI 和 Grok CLI——每个输出中的内联代码和链接都得到保留。“避免使用两套 HTTP 栈”只是偏好，并非阻塞条件：测量结果给出了明确答案。
    - **`requirements.txt` 并未描述真实环境**：`google-auth`、`cryptography` 和 `opentelemetry` 栈都安装在工作虚拟环境中，却从未声明，因此全新安装无法复现实际测试内容。相反，`tokenizers`、`huggingface-hub` 和 `PyYAML` 出现在其中，却没有被任何代码导入或要求，是 `mistralai` 1.x 遗留下来的内容。该文件已根据仅包含直接依赖的虚拟环境重新生成，成为完整闭包。`pip-audit` 未报告新依赖集合中的任何已知漏洞。
    - **`.github/dependabot.yml`**（新增）启用每周版本更新、pip 和 github-actions。次要版本和补丁版本合并到一个 PR 中——每个 PR 只包含一次补丁升级最终会被忽略，而噪声是更新的敌人；**主版本单独处理**，每个主版本都要求通过真实调用进行验证。
    - **`scripts/check-deps-fresh.sh`**（新增并接入门禁）让延迟反映在项目判定中：Dependabot 负责提出建议，但不保证更新，而且 PR 可能会堆积。主版本延迟 → 失败；次要版本延迟 → 警告，因为长期保持红色的门禁最终会被忽略；PyPI 无法访问 → 本地显式跳过，**CI 中 fail-closed**，未执行的检查不能算成功。两个方向都已验证：它能捕获修复前的准确状态（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`），并且对次要版本只发出警告。

  - **本次 PR 审查产生的修复**——五名审查代理仔细检查了差异；以下各项在修复前都已通过测量**复现**，其中两项还是本版本前文引入的回归问题。
- **已修复回归问题——`_NEWS_CITATION_REGEX` 存在指数级回溯。** 多段落修复将 `(?:[ \t]*$|[ \t]+.*)` 引入了重复部分：`[ \t]+` 与 `.*` 之间的空格共享存在歧义，而这种歧义会在每次迭代中不断放大。在不匹配该模式的 `>   texte` 行上进行测量——这些是完全合法的 Markdown 缩进行——结果为 **14 行耗时 2 589 ms**，修复后为 0.04 ms，每增加一行耗时约增加 9 倍。在 `--news` 模式下，一段很长且格式不合规的 blockquote 就足以让翻译卡住，直到任务超时，而且没有可识别的原因。现在，重复部分会一次性消耗整行（`\n^>(?![ \t]*—).*`），因此每次迭代只剩一种匹配方式。在包含 231 篇文章的真实语料上验证：**捕获结果零差异**，仍为 423 条引用，14 个多段落正文也都保持扩展。
    - **同时指定两个 provider flags 时会静默按使用量计费。** `--use_codex --use_mistral` 会被接受；`_select_provider_client` 先测试 Mistral，`_resolve_provider` 则优先处理显式布尔值——两者都会收敛到 Mistral。因此，用户本想使用订阅配额，却得到了按使用量计费，整个过程没有任何警告：这正是 `--use_codex` 存在的目的——防止这种故障模式。现在，六个 provider flags 都通过一个 `add_mutually_exclusive_group`。**行为变更**：此前会被静默接受的、同时组合两个 provider 的命令行，现在会在 `argument --use_mistral: not allowed with argument --use_codex` 上失败。
    - **工作结束 gate 会在探测失败时错误地变绿。** `scripts/check-release-ready.sh` 的十三项检查中有四项遵循“捕获 stdout，若为空则得出结论”的模式，却从不检查返回码：异常（文件被重命名、`FileNotFoundError`）会写入 stderr，使 stdout 保持为空，检查于是得出“没有需要报告的内容”。为防止该问题而编写的脚本内部又重现了“一个 `exit 0` 什么也不能证明”的陷阱。现在，`probe()` helper 同时要求返回码为零**且**存在结束哨兵；探测也拒绝在标记集合为空时得出结论——因为关于空集合的断言总是真的。示例：上方新增的互斥组使 provider flags 通过一个 `*_group` 对象传递，而旧的正则表达式 `parser\.add_argument\(` 已无法匹配；**21 个 flags 中有 6 个**静默脱离了检查范围，gate 仍显示为绿色。
    - **秘密扫描漏掉了六个 provider 中的四个。** `[A-Za-z0-9]` 类排除了连字符：`sk-proj-…`（当前 OpenAI 格式）和 `sk-ant-api03-…` 会在第二个连字符处失败，`AIza…` 也未被覆盖。模式已扩展，并将 `.secrets.baseline` 排除在扫描之外。此外，`.env` 检查的是 `git diff --cached`，它只能查看索引：一个**已经提交**的 `.env`——最糟糕的情况——根本不会出现在其中。现在改为检查 `git ls-files`。
    - **Codex 的“令牌预热”并不是预热。** 测量表明：`codex login status` 不会触碰 `~/.codex/auth.json`（mtime 和大小均未改变），其帮助信息写的是“显示登录状态”。然而注释却声称它会“按顺序执行一次”令牌刷新，从而消除一次性轮换令牌发生并发刷新的风险。所宣称的保护并不存在；现在注释会如实描述代码行为，真正的应对措施仍然是 `max_jobs=4`。此外，检查现在遵守 `CODEX_BIN`，此前它会忽略该项——没有 `codex` 的机器在 `PATH` 中会因“未认证”而失败，导致诊断具有误导性。
    - **`.env` 在子 shell 中被加载。** `detect_provider` 通过命令替换调用，因此其 exports 不会向上传递：在 `.env` 中定义的 `GROK_BIN`、`GROK_HOME` 或 `REGEN_MODEL` 对 `main()` 中执行的读取不可见，于是即使配置正确，也会得出“找不到 Grok 二进制”的结论。
    - **并发量比声明的上限高出 50%。** 守卫位于 README/CHANGELOG 这对任务启动之后；实测峰值为 **`max_jobs=2` 的 3 个**。对于 Grok，其每周配额与 Chat/Imagine/Voice 共享且无法测量，因此脚本自行施加的上限并未得到遵守。最终计数虽然会显示，却从未与 28 比较——缺失一个文件也不会被发现。
    - **Grok 输出契约：缺少 `stopReason` 现在会判定失败。** 代码在此处应用了“`end_turn` **或缺失**”，而声明的契约要求 `end_turn`。没有该字段的 payload——或该字段因 CLI 更新而被重命名——都会让守卫静默变成空操作。此外，`max_turn_requests` 不再被归类为 rate limit（耗尽的是轮次预算：重试只会重复结果，却要付出 90 秒等待），`quota` 也不再输出 rate limit 标记——原因已经在 `_codex_is_rate_limited` 的 docstring 中说明，只是 Grok 尚未执行。
    - **Gemini cascade 按模型进行记忆化。** 它会在每个 segment 上从 `minimal` 重新开始，而默认模型会拒绝该设置：正常路径每个 segment 都要付出一次 400 往返，并重复打印相同的警告。警告重复数百次后就不再有人阅读——这正是它变成遮蔽物的方式。
    - **其他事项**：CI 中的拒绝消息被硬编码为 Codex 的消息，会将 `--use_grok_cli` 用户引导至 `OPENAI_API_KEY`，而不是 `XAI_API_KEY`；`provider.capitalize()` 显示为“Grok_cli”和“Openai”；子进程基础设施的注释将“shim”泛化为两个 CLI，尽管 Grok 二进制是原生 ELF（正确的理由是“会自行生成子进程的 agent”）；`subprocess` 上的十二条 SAST findings 已标记为 `# nosec` / `# nosemgrep` 并附带理由，缺少 `shell=True` 的列表形式使注入不可能发生，且文档内容从未经过 argv。
    - **不再有任何秘密进入 agent 子进程。** 按名称列出的 deny-list 只保护了**计费**不变量（没有 `OPENAI_API_KEY` 的 Codex、没有 `XAI_API_KEY` 的 Grok）。测量显示：**另外七个秘密**仍会进入每个子进程——Anthropic、Mistral、Google 和 Gemini 的密钥、另一个 CLI 的密钥，以及 `OPENAI_BASE_URL`；后者不是秘密，却会重新定向流量。而这两个 CLI 都是 **agent**，Grok CLI 在许多 Linux 机器上运行时没有可用的 OS sandbox。现在改为按**名称模式**过滤（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`），而不是使用名称列表，因此也能覆盖用户在 `.env` 中添加、而这段代码事先并不知道的变量。CLI 不需要其中任何变量：身份验证保存在 `~/.codex` 和 `~/.grok` 中，从不依赖环境——已通过两个 provider 在加固环境中完成**真实翻译**进行验证。
    - **测试**：新增 `tests/test_review_hardening.py` 文件（21 个测试），锁定 provider flags 的互斥性、`stopReason` 契约、news 正则表达式的线性性能、CI 拒绝消息、Gemini 记忆化，以及子进程环境中不存在任何秘密。最后一项断言是**通用的**——遇到任何列表中未命名的密钥都会失败；而现有的清除测试只是其常量的镜像，除了检测自身循环的故障外无法发现其他问题。完整测试套件达到 **311 个测试**。

  - **新增两个 Grok provider**：`--use_grok`（xAI API，使用 `XAI_API_KEY` 密钥，按使用量计费）和 `--use_grok_cli`（官方 Grok Build CLI，从 Grok 订阅中扣除——原理与 `--use_codex` 相同）。
    - **API 模式，约 40 行**：由于 xAI endpoint 兼容 OpenAI，客户端和 `_call_openai` 原样复用，只需更改 `base_url`。只需进行一项适配，而且所有 provider 都能受益：`finish_reason` 现在接受 `end_turn`，这是 xAI 输出的形式，而 OpenAI 输出 `stop`。模型：`grok-4.6`（质量）和 `grok-4.3`（经济）。需要注意，Grok 的经济模型仍是仓库中最昂贵的——每百万输入/输出分别为 $1.25/$2.50，而 `mistral-small-latest` 为 $0.15/$0.60：选择该 provider 是为了模型多样性，而不是价格。
    - **CLI 模式**：仿照 Codex，但受实际情况影响存在四项差异——prompt 通过文件传递（`--prompt-file`，CLI 不读取 stdin，将 segment 放入 argv 会使其出现在 `ps` 中），输出是 stdout 上的单个 JSON 对象（既不是 JSONL，也不是 `-o` 文件），订阅只暴露 `grok-4.6` 和 `grok-4.5`，并且 sandbox 无法应用（见下文）。子进程启动逻辑与 Codex 一起抽取到 `_codex_run_process` 中，不触碰已经过测试的 Codex provider 其余部分。
    - **实测表明，`exit 0` 什么也不能证明**：未认证时，CLI 会在 **stdout** 中写入 `{"type":"error","message":"Not signed in."}`，返回码却为 **0**。拒绝或轮次耗尽时行为也相同。因此，输出契约要求四个条件同时满足：返回码为 0、没有错误 payload、存在 `stopReason == end_turn`，并且文本非空。预检遵循相同逻辑：即使断开连接，`grok models` 也会以 0 退出，只有 stdout 中出现“未认证”才能得出结论。
    - **隔离：明确记录并接受这种不对称性。** Codex 在 `--sandbox read-only` 中运行，而 Grok sandbox 在许多近期 Linux 机器上无法应用；原因有两个彼此独立的系统问题，若没有 `sudo` 就无法绕过：自 Ubuntu 24.04 起，AppArmor 会阻止非特权 user namespaces（`bwrap: setting up uid map: Permission denied`，在 Grok 之外也已复现）；当 `/run/podman` 处于 `0700` 时，容器运行时 socket 的 deny-list 会失败（resolver 只能补救 `ErrorKind::NotFound`，EACCES 会变成致命错误）。核心陷阱是：无法应用的**内置** profile 会**静默地以未隔离状态启动**。因此，脚本默认不请求任何 profile，也绝不会静默回退——它会在 stderr 上发出警告。保护依赖 CLI 的 `--deny` 规则，包括 catch-all `*`；这是唯一经过测量的 _fail-closed_ 层（未知前缀的规则会拒绝启动）。`GROK_TRANSLATE_SANDBOX=read-only` 允许强制要求隔离，此时如果机器无法满足要求，启动就会失败。
    - **防护措施**：`XAI_API_KEY`、`GROK_API_KEY` 和 `GROK_SANDBOX` 会从子进程环境中移除（其中一个密钥会使计费切换为按使用量；继承的 `GROK_SANDBOX` 会强制使用无法应用的 profile，并产生误导性消息）；MCP/hooks/skills/agents 开关已禁用，`--disable-web-search`、`--no-subagents`、`--no-plan`、一次性 workdir、CI 中拒绝、会终止进程组的 timeout，以及 rate limit 时的 back-off。`--max-turns` 固定为 6，而不是 1：计数器会在工具轮次结束后递增，设置为 1 会截断输出。
    - **配额**：Grok pool 按周计算，并且**与 Chat、Imagine 和 Voice 共享**，任何命令都不会公开该配额——不同于 Codex，后者可以通过 `account/rateLimits/read` 计算消耗量。因此，`regen_translations.sh` 将并发限制为 2，并明确发出警告。
    - **测试**：新增 `tests/test_grok_provider.py` 文件（24 个测试）。完整测试套件达到 **290 个测试**。
  - **已修复 bug——多段落 EN 引用仅在部分情况下受到保护（`--news` 模式）**：`_NEWS_CITATION_REGEX` 作为引用正文，只接受一组彼此**连续**的 `>` 行。一旦引用跨越多个段落（由一条 `>` 空行分隔），只有最后一段会被捕获并替换为占位符；之前的段落会发送给 LLM 并以翻译后的形式返回——这恰好与 `--news` 要保证的目标相反。现在，重复部分接受内部的 `>` 空行，并改为非贪婪模式，从而在引用前的 `>` 空行处停止，而不是在遇到的第一处空行处停止。
    - **实测规模**：在包含 198 篇文章的真实语料上，419 条引用中有 11 条受到影响。没有回归——新正则表达式捕获的引用数量完全相同，只扩展了多段落正文（408 个正文不变，11 个扩展），归属行 `> — …` 仍无法被吸收到正文中（保留了 lookahead）。
    - **端到端证据**：在一篇 69 KB、翻译为 ja/ar 的文章上验证：引用此前的第一段会在日语中呈现为 `> GLM-5.3がオープンウェイト化。`，阿拉伯语中也同样被翻译；现在则保持为 `> GLM-5.3 is now open-weight.`。英文引用行数从 9 恢复为 10，与源文档一致。
    - 需要注意：下游验证器不会检测到这一缺陷，因为它们只检查引用是否存在，不检查引用是否完整。
  - **默认 provider 的实测节省**：`_openai_extra_kwargs` 会在模型名称以 `gpt-5` 开头时发送 `reasoning_effort="medium"`，包括在 `--eco` 中的情况。对 `gpt-5.4-mini` 进行测量：翻译一个十词句子时，`medium` → 45 个 reasoning tokens 和 65 个输出 tokens；`none` → 0 和 14。推理对翻译没有帮助，却会在每个文件的每个 segment 上产生费用。现在默认值在 `--eco` 中变为 `none`，其他情况下仍为 `medium`；通过 CLI 显式传入的值仍具有优先级。`--reasoning_effort` 现在除 `low`/`medium`/`high` 外，还接受 `none` 和 `xhigh`（并非所有模型都接受这些值：例如 `minimal` 会被 `gpt-5.4-mini` 拒绝——现有的不带参数重试机制可以处理这种情况）。
  - **SDK 更新与 Gemini 迁移**：`google-generativeai`（支持已于 2025-11-30 结束，仓库已归档）被统一 SDK **`google-genai`** 替代——先使用 `genai.Client(api_key=...)`，再使用 `client.models.generate_content(model=, contents=, config=)`；系统 prompt 改为通过 `system_instruction` 传递，而不是与 segment 拼接。`mistralai` 升级至 **2.9.4**（导入变为 `from mistralai.client import Mistral`；旧导入会抛出 `ImportError`，已在 wheel 中验证），`anthropic` 升级至 **0.125.0**，`openai` 升级至 **2.54.0**——这些是切换到 `httpx2` 前的最后版本，以避免在 venv 中共存两套 HTTP 栈。`httpx` 0.28.1 和 `pydantic` 2.13.5 也因此解除限制。
  - **两个由真实测试而非文档捕获的回归问题**：
    - `anthropic` ≥ 1.0 会在客户端拒绝非流式调用，只要其 `max_tokens` 预示着请求可能超过 10 分钟（`ValueError: Streaming is required...`）。该保护在 0.34.2 中不存在，并导致所有使用 `max_tokens=32768` 的 Claude 调用失败。已通过显式设置 `timeout` 修复（`CLAUDE_TIMEOUT`，默认 900 秒），从而避免为只使用完整响应的调用切换到 streaming。
    - `thinking_level="minimal"` 仅被 Gemini 模型目录的一部分接受：`gemini-3.1-flash-lite` 支持它，而 `gemini-3.7-flash` 和 `gemini-3.1-pro-preview` 会以 400 拒绝。因此采用 `_gemini_generate_with_fallback`：`minimal` → `low` → 不使用 thinking_config，仿照已有的 OpenAI fallback——优化参数绝不能导致翻译失败。
  - **更新默认模型**，每个模型都经过真实调用验证：OpenAI `gpt-5.5` → **`gpt-5.6-terra`**（在包含 28 个项目的批次上降低 60%）以及 `gpt-5.4-mini` → **`gpt-5.6-luna`**（降低 73%）；Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**（更便宜且更新）以及 `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（不带日期的规范 ID）；Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**，以及 `gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（稳定版本，且比 `3.5-flash-lite` 更便宜）。
Mistral 保持不变，`mistral-large-latest` 仍然是四者中性价比最高的。需要注意：不存在比 `gemini-3.1-pro-preview` 更新的 Gemini Pro 系列模型——2026 年 5 月宣布的 Gemini 3.5 Pro 从未发布；3.5/3.6/3.7 系列完全属于 Flash。
  - **切换 Gemini 前进行实测 A/B 对比**：使用 `README.md`，先通过 `gemini-3.1-pro-preview` 翻译成日语，再通过 `gemini-3.7-flash` 翻译。结构严格一致（21 个列表、18 个代码块、13 个 HTML 链接、13 张图片，所有 URL 均得到保留），耗时为 **8 秒，而非 48 秒**。由于没有公开基准测试比较这两个模型在翻译或非拉丁文字脚本方面的表现，否则切换只能建立在简单假设之上。
  - **过滤 Claude 响应块**：`_call_claude` 会在不筛选类型的情况下执行 `block.text for block in response.content`。自适应推理模型（Sonnet 5 及更高版本）会插入一个 `thinking` 块，其中公开的是 `.thinking`，而不是 `.text`——翻译在第一个片段遇到不透明的 `AttributeError` 时就会失败。现在会排除 `thinking`、`redacted_thinking`、`tool_use` 和 `tool_result` 块（采用否定列表，以便对承载文本的未知类型保持兼容），而完全没有文本块的响应会抛出明确错误。每次调用都会传入 `thinking={"type": "disabled"}`。
  - **重新同步 `MODEL_TOKEN_LIMITS`**：移除退出日期已过的模型（`magistral-*` 系列于 2026-07-31 退役，`gemini-2.0-*` 于 2026-06-01，`gemini-3-pro-preview` 于 2026-03-09，以及 `claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。修正限制：Mistral 128K → **256K**（Large 3 / Small 4 系列），Gemini 1 000 000 → **1 048 576**（实际输入限制），`claude-opus-4-5` 200K → **1M**，`gpt-5.6-*` 系列 400K → **1.05M**。新增 Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest` 和 `ministral-*` 系列。需要注意：这些限制仍仅供参考，`translate()` 会将分段上限设为 `min(16000, limite)`。

  - **Provider `--use_codex`**：第五个 provider，通过非交互模式驱动官方 Codex CLI（`codex exec`），而不是调用按使用量计费的 API。翻译消耗的是已经支付的 ChatGPT 订阅配额。这是 OpenAI 针对该用途记录在案的唯一途径：按套餐划分的可用性矩阵将“Codex SDK、`codex exec` and scriptable workflows”列为 Plus/Pro/Business/Enterprise 可用，而 `~/.codex/auth.json` 的令牌无法验证 Platform API 调用（本脚本也从不读取它们——身份验证及其刷新仍由 CLI 管理）。
  - **Codex 二进制文件现在既可通过 pip 安装，也不再仅限于 npm**：`_resolve_codex_binary()` 会先在 `CODEX_BIN` 中查找二进制文件，然后查找 `PATH`，最后查找由 OpenAI 发布的官方 Python 包 **`openai-codex-cli-bin`**（这是 `openai-codex` SDK 的依赖项）。因此，Python 项目不再需要全局安装 npm 即可使用 `--use_codex`。该包不会加入 `requirements.txt`：二进制文件约 250 MB，这会迫使所有用户为一个可选 provider 承担额外依赖。已完成端到端验证：当 `codex` 不在 `PATH` 中时，解析会找到打包的二进制文件，并在 6 秒内完成整篇翻译。
  - **“订阅模式”保证**：`OPENAI_API_KEY` 和 `CODEX_API_KEY` 会从子进程环境中移除。没有这项保护，`.env` 中存在的密钥可能会让 Codex 在没有任何可见提示的情况下切换到按使用量计费模式——而这正是该 provider 存在要避免的情况。
  - **通过测试锁定 CLI 陷阱**：
    - `codex exec` **即使**提示词作为参数传入，也会读取 stdin：如果不关闭 stdin，命令会一直等待直到超时，却始终不会调用模型（复现结果：180 秒后退出码 124，零字节）。因此必须使用 `communicate(input=...)`。
    - 通过 npm 安装的 `codex` 是一个 Node shim，它会 `spawn` 真正的 Rust 二进制文件：后者是 Python 进程的**孙进程**，会在 `SIGKILL` 结束 `subprocess.run(timeout=)` 后继续运行并消耗配额。因此需要 `Popen(start_new_session=True)` + `os.killpg`。
    - CLI 可能在输出 `turn.failed` 的同时以 0 退出：除返回码外，还会检查 JSONL 输出（`--json`）；如果返回码为 0 但缺少 `-o` 文件，则会抛出明确错误，而不是生成空片段。
  - **速率限制退避**：CLI 不实现内部重试（`max_retries = 0`）。分类依据 JSON payload 的结构（`status: 429` / `error.type`），而不是子字符串——“quota”一词既可能出现在可恢复的 429 中，也可能出现在不可恢复的 `insufficient_quota` 中。
  - **CI 防护**：如果定义了 `CI` 或 `GITHUB_ACTIONS`，则拒绝 `--use_codex`。订阅身份验证不适用于共享 runner，且 OpenAI 明确不建议在公共仓库中采用此工作流。
  - **模型**：`gpt-5.6-sol`（质量）和 `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` 系列同时用于 CLI 和 Platform API，但 ChatGPT 账户并不一定有权使用其中所有模型：allowlist 在服务器端应用，不进行本地验证，使用异常模型时会触发警告。在 Plus 套餐上，Luna 每 5 小时窗口提供 250–2,000 条消息，而 Sol 提供 10–100 条：`--eco` 是所有批处理的推荐模式。
  - **已修复的 Bug——`regen_translations.sh` 在完全成功后仍报告错误**：`trap ... EXIT` 引用了 `failed_log`，这是 `main()` 的一个 `local`，但在 trap 执行时已经不存在。在 `set -u` 下，这会抛出 `failed_log: unbound variable`，使脚本以 1 退出，尽管 28 个翻译均正确——这会在重新生成后、最耗时的步骤中立即中断 `release.sh --auto`（`set -e`）。现在该变量变为全局变量，trap 会检查其是否存在。一个有用的副作用是：此前被此错误掩盖的真正翻译失败，会再次显示在最终摘要中。
  - **`REGEN_MODEL`**：`regen_translations.sh` 的新环境变量，可覆盖 provider 的默认设置，强制使用指定模型，例如使用 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`，在订阅配额允许的高端模型上重新生成，而不是使用面向高吞吐量的 `--eco` 模型。
  - **`regen_translations.sh`**：`REGEN_PROVIDER=codex` 可通过显式 opt-in 使用（绝不自动检测，以免在用户不知情的情况下消耗订阅配额）。令牌会在开启并行处理前按顺序刷新一次——Codex 刷新机制具有轮换性且只能使用一次，并发任务会使 `codex login` 会话失效——并发数降至 4。
  - **相关重构**：`_dispatch_provider_call` 通过一个 `_resolve_provider()` 从 8 个参数减少到 6 个参数；该 `_resolve_provider()` 返回 provider 名称，而不是在整条调用链中传递第四个布尔值。显式布尔值仍优先于 `args`，以保留使用最小 `Namespace` 调用 `translate(..., use_mistral=True)` 的测试。
  - **测试**：新增文件 `tests/test_codex_provider.py`（48 个测试），覆盖 argv、清理后的环境、反前导内容契约、静默失败、timeout/killpg、退避、preflight、provider 解析、Gemini 推理级联、Claude 块过滤以及多段新闻引文。完整测试套件增至 290 个测试。
  - **真实验证**：通过 Codex 将项目的 `README.md` 翻译成**14 种语言**，结果与参考翻译严格保持相同结构（14 个代码块、24 个标题、25 个表格行、13 个 HTML 链接、13 张图片、19 个 URL，代码块逐字符一致，且没有任何 placeholder 残留）。对于一篇 69 KB 的新闻文章，在 `--news` 模式下，`gpt-5.6-luna` 和 `gpt-5.6-sol` 的输出在 en/ja/ar 上均通过下游应用验证器。通过 `account/rateLimits/read` 测得的消耗：在 `--eco` 模式下仍低于计数器的四舍五入阈值（5 小时窗口的 0%）。

- **1.9.2** 修复带嵌套括号或 FR 前缀的新闻归属 URL 提取（2026-05-11）：

  - **已修复的 Bug**：`_protect_news_quotes` 中的归属 URL 提取使用了正则表达式 `re.search(r"\((.+?)\)", attribution)`（括号之间的惰性捕获）。对于类似 `(relayé par [@user sur X](https://x.com/.../123))` 的归属内容（存在嵌套括号：外层的 `(` 加上 Markdown 链接中的 `]()`），捕获会在遇到第一个 `)` 时停止 → 字符串被截断，并且包含 FR 前缀：`relayé par [@user sur X](https://x.com/.../123`（缺少末尾的 `)`）。结果是：`_validate_news_post` 在翻译输出中查找该字符串时始终失败（原因有二：`)` 被截断，以及“relayé par”被翻译为 `relayed by`/`weitergeleitet von`/……）。完整的 low → medium → high → gpt-5.5 级联无法通过。
  - **修复**：正则表达式改为 `re.search(r"\]\(([^)]+)\)", attribution)`——专门定位 Markdown 链接中的 `](url)`，**仅捕获纯 URL**（不含 FR 前缀，也不会被截断）；翻译期间通过 `#URL{N}#` placeholder 保持不变。对两种问题模式均有效：
    - `(relayé par [@account sur X](url))`——嵌套括号
    - `via [@source](url)` 或 `selon [@author](url)`——没有外层括号的 FR 前缀
  - **测试**：在 `test_silent_failure.py` 类 `TestNewsCitationExtraction` 中新增 2 个测试：
    - `test_extract_attribution_url_with_nested_parens`（精确复现 Genspark CEO E2B 的 Bug）
    - `test_extract_attribution_url_with_french_prefix`（包含 `via` 的变体）
  - **覆盖缺口**：`check-editorial-coverage.py` 验证编辑语法，但不验证 translator 是否能够翻译。一个可能的改进（超出 v1.9.2 范围）是增加检查，在发布前通过 dry-run 模拟归属提取，以检测存在风险的模式。

- **1.9.1** 修复翻译 marker 备注中的 CTA 标签国际化（2026-05-10）：

  - **已修复的 Bug**：已翻译文件顶部 marker 横幅中 CTA 链接的 `[Voir le projet sur GitHub ↗]` 标签对所有目标语言仍然**是法语**，而不是跟随 `target_lang`。LLM 从未看到该标签（它由 Python 侧组装，以保留 URL 和仓库 slug），因此翻译阶段无法修复它。这是 v1.9 添加 `marker` 格式后产生的静默回归。
  - **修复**：新增常量 `_VIEW_PROJECT_LABELS`，将 15 种语言映射到本地化标签。`_translation_note_invariants(target_lang)` 和 `_assemble_translation_note_paragraphs(phrase, target_lang)` 现在会传递目标语言。语言未知时回退到 `fr`（出于安全考虑，避免 KeyError）。
  - **测试**：调整 `test_source_emits_three_paragraphs_repo_title_description_link`（target_lang `ja` → 预期日语标签）。新增 2 个测试：`test_source_link_label_localized_per_target_lang`（参数化覆盖 7 种语言，包括拉丁、表意和辅音音素文字脚本）以及 `test_source_link_label_falls_back_to_french_for_unknown_target`。总计：`test_translation_note_position.py` 中有 40 个测试（原为 38 个）。
  - **向后兼容**：签名使用默认值 `target_lang="fr"`——外部以编程方式调用且不提供 `args.target_lang` 的调用方无需修改即可继续工作。
- **1.9** 修复静默失败 + 完整质量工具链 + 多位置翻译注释（2026-05-07）：
  - **多位置翻译注释 + “embed card”格式标记**：
    - 新增 CLI 选项（附加功能，默认值不变 → **不破坏兼容性**）：
      - `--note_position {top,bottom,both}`（默认：`bottom`）：将注释放置在已翻译文件的顶部、底部，或两个位置。
      - `--note_format {legacy,marker}`（默认：`legacy`）：
        - `legacy` 严格复现 v1.8 的行为（加粗段落 `**…**`），**逐字节一致**。
        - `marker` 输出不可见的 Markdown 链接引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），后跟结构化的**三段式 blockquote**，用于呈现类似 “GitHub repo embed card” 的效果：使用行内代码显示项目名称（`**\`ai-powered-markdown-translator\`\*\*`）、由 LLM 翻译的描述，以及带可见箭头的 CTA 链接（`[Voir le projet sur GitHub ↗](URL)`）。可由 remark 插件在构建时处理（参见 blog jls42.org → 插件 `remark-translation-banner`）。
    - **绝不发送给 LLM 的不变量**：仓库标题和 GitHub URL 在描述句翻译完成后由 Python 侧拼接。LLM 永远看不到 slug `ai-powered-markdown-translator` 或 `https://github.com/jls42/...`，从而确保任何 renderer/case/scheme 都不会被修改。
    - **感知 frontmatter 的插入**：在 `top` 或 `both` 模式下，注释会插入到 YAML frontmatter 的**结束 `---` 块之后**（确保 Astro Content Collections / gray-matter 安全）。Helper `_split_frontmatter` 会检测文件开头的 `---\n…\n---\n` 并保持其完整性；如果 frontmatter 已开启但没有关闭 fence，则**抛出 `RuntimeError`**（文件会进入 `failed_files`，而不是以位置错误的注释写入）。
    - **模型 sanitizer 白名单**：`_sanitize_model` 会将所有不属于 `[A-Za-z0-9._:/-]` 的字符替换为 `_`；如果结果为空，则使用 fallback `unknown`。该规则与 Astro remark 插件侧的验证器一致，并会中和可能破坏 marker 格式的字符（空格、引号、括号、逗号等）。
    - **内部重构**：将 `_append_translation_note`（1 个单体函数）改为 7 个纯 helper（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。Builder/composer 分离（builder 返回不带分隔符的纯代码块，composer 根据位置应用 `\n\n`）；生产代码和源 helper 共用同一个三段式组装器。
    - **`_quote_lines` 保留空行**：为每一行添加 `> ` 前缀，将空行转换为仅包含 `>` 的行。这样 mdast 能在 blockquote 中识别出 3 个不同段落（标题 / 描述 / 链接），而不是包含换行的单个段落。
    - **`_build_translation_note_block` 自适应**：根据 LLM 保留的段落数量调整格式（3 段 = 完整 card 格式，2 段 = 句子 + 链接，1 段 = fallback）。当检测到 Markdown 链接 `](` 时，单段 fallback **不再用 `**...**` 包裹**（避免在链接周围使用 `<strong>` 导致脆弱的渲染结果）。
    - **向后兼容**：`getattr(args, "note_position", "bottom")` 和 `getattr(args, "note_format", "legacy")` 位于 `_compose_with_notes` 一侧——不包含这些属性的 Namespace（现有测试、外部程序化调用）无需修改即可继续工作。
  - **修复长篇翻译的静默失败**：
    - 所有 provider（OpenAI、Mistral、Claude、Gemini）均增加翻译后语言验证：确定性层（逐字匹配找回源文本片段）+ 概率性层（`langdetect`）。
    - 白名单 `finish_reason` / `stop_reason`：任何不在白名单中的状态（truncation、content_filter 等）都会触发 `RuntimeError`。
    - `max_tokens` Claude：将 `4096` → `32768`（避免 16k 片段发生潜在截断，并为 FR→JA/ZH/KO/AR/HI 跨文字体系转换保留余量）。
    - 感知标题的分段：在片段的后半部分优先放置 H2/H3（每个片段都从一个完整的语义章节开始）。
    - 错误传播至非零退出码：`translate_markdown_file` 返回类型化状态 `success` / `failure` / `skipped`；如果至少有一个文件失败，`main()` `sys.exit(1)`（单文件和批处理模式均适用）。
    - 所有 provider 均增加空内容保护、源文/输出文合理比例检查（≥ 500 个字符，< 5% = 拒绝）、代码占位符验证（`#CODEBLOCK`/`#INLINECODE`）、LLM 后规范化（修复粘连到标题的分隔符/链接）、`BadRequestError` 不带 `reasoning_effort` 的重试。
    - 新增依赖 `langdetect==1.0.9`。
  - **提交前质量工具链**（“完整 EurekAI 类型”，14 个 hooks）：
    - Pre-commit：ruff（lint+format）、shellcheck、prettier（md/yaml/json）、detect-secrets（保护 4 个 API key）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（空白字符、EOF、大文件、shebang 等）。
    - Pre-push：mypy（逐步采用 lax 模式）、Opengrep SAST（translate.py + scripts/）、pip-audit（初始 reporting 模式）、unittest discover（tests/ + scripts/tests/）。
    - 本地 wrapper 位于 `scripts/`，使用 `./venv/bin/python`。
    - `scripts/audit_verdict.py`：包含 11 个 unittest 的 pip-audit JSON parser，采用从 jls42-astro parser 移植并适配 Python 的版本。
    - 修复最初的 7 个 ruff 违规：B904（raise from）×2、B007（未使用的 dirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）。
    - Lizard 暂时排除 `translate.py`（4 个函数的 CCN 为 21–47，计划重构）——对 scripts/ 启用严格 gate。
  - **SonarCloud + 全面覆盖率**：
    - GitHub Actions 工作流 `SonarCloud`（sonarcloud.yml + sonar-project.properties）：每次 push 和 pull-request 都进行分析，通过 `coverage.xml` 获取覆盖率。
    - README 顶部新增 11 个 SonarCloud 徽章（Quality Gate、Security/Reliability/Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）。
    - `tests/test_silent_failure.py`（`unittest` stdlib）：覆盖静默失败错误链的六个环节。
    - `tests/test_orchestration.py`（+79 个测试）：覆盖 `translate.py` 的编排层（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` TypeError + BadRequestError fallback、o1-series prompt 格式、`_validate_translation_output` 的 early-return 分支）。
    - `scripts/tests/test_audit_verdict.py`：通过 subprocess 覆盖 `main()`（stdin/stdout）以及 `if __name__ == "__main__"` 代码块。
    - **新代码覆盖率**：75.5% → 约 98%（translate.py 98%，scripts/audit_verdict.py 97%）。
  - **测试**：`tests/test_translation_note_position.py` 覆盖位置 × 格式矩阵（包括 E2E `marker+top|bottom|both` 和 `legacy+top|bottom|both`）、多行前缀、逐字节向后兼容（golden literal）、sanitizer、frontmatter 拆分（包括未闭合 fence 时抛出异常）、三段式格式、两段式 fallback、单段 + Markdown 链接保护，以及关键防护测试 `TestLLMPayloadExcludesInvariants`，断言标题和 URL 永远不会发送给 LLM。**190 个测试通过，0 回归。**
  - 文档：`README.md`（法语 + 14 种翻译）包含徽章，`CLAUDE.md`（pre-commit 工作流 + 详细 CI 监控），重新生成 28 种翻译。
- **1.8** `--news` 模式 + 2026 年模型升级（2026-03-17，标签 `v1.8`）：
  - 默认模型已更新（2026 年 3 月）：
    - OpenAI 高质量：`gpt-5` → `gpt-5.4`
    - OpenAI 经济型：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 高质量：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - 为 `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）和 `gemini-3.1-pro-preview`（1M）添加 token 限制。
  - 初始 `--news` 模式：使用占位符 `#NEWSQUOTE\d+#` 保护英文引用，提供 `LANG_FLAGS` 映射（15 种语言），并处理目标语言标志。
  - 恢复前验证 news 占位符（修复回归问题：LLM 删除占位符会静默地产生无引用输出）。
  - 使脚本 `regen_translations.sh` 具备可移植性（使用绝对路径，不依赖 pwd）。
  - 在 README/CHANGELOG 的语言栏中添加 Français 链接，重新生成 28 种翻译。
- **1.7** 新功能：
  - 新增 `--keep_filename` 选项，在翻译时保留原始文件名。
  - 支持 `.env` 文件，以自动加载 API key。
  - **保留行内代码**：反引号（`` `...` ``）现在会在翻译期间受到保护。
  - 改进系统 prompt：
    - 更好地处理 YAML frontmatter 中的引号。
    - 保护模板变量 `{variable}`。
    - 禁止未被要求的译者注释。
  - 在博客 jls42.org 迁移中成功测试了 364 个文件。
- **1.6** 新功能：
  - 支持 Google Gemini API 进行翻译（`--use_gemini`）。
  - 更新 2026 年默认模型：
    - OpenAI：`gpt-5`（高质量）、`gpt-5-mini`（经济型）
    - Claude：`claude-sonnet-4-5`（高质量）、`claude-haiku-4-5`（经济型）
    - Gemini：`gemini-3-pro-preview`（高质量）、`gemini-3-flash-preview`（经济型）
  - 经济模式（`--eco`），用于使用更快速且成本更低的模型。
  - 单文件翻译（`--file`），无需遍历目录。
  - 新的简化命名模式：`{base}-{lang}.md`。
  - 新增 `--include_model` 选项，以保留带模型名称的旧格式。
  - 支持未列出的模型，默认 token 限制为 128k。
  - README 已翻译成 14 种语言。
- **1.5** 改进：
  - **API key 和默认模型更新：**
    - **OpenAI：** 将 `DEFAULT_MODEL_OPENAI` 更新为 `"gpt-4o"`。
    - **Mistral AI：** 将 `DEFAULT_MODEL_MISTRAL` 更新为 `"mistral-large-latest"`。
    - **Anthropic Claude：** 新增 `DEFAULT_ANTHROPIC_API_KEY`，并将 `DEFAULT_MODEL_CLAUDE` 更新为 `"claude-3-5-sonnet-20240620"`。
  - **翻译 prompt 优化：**
    - 直接翻译和翻译注释所使用的 prompt 得到扩充，以提高清晰度和效率，其中包括关于保留元数据及特定格式元素的详细指令。
  - **代码重构：**
    - 使用 `Mistral` 类替代 `MistralClient`，用于初始化 Mistral AI 客户端。
    - 重新组织 imports，以提升可读性和可维护性。
    - 改进文本分段和代码块处理，在翻译过程中保留原始格式。
  - **输出文件管理：**
    - 反转输出文件名中的模型和语言顺序（例如 `f"{base}-{args.target_lang}-{args.model}.md"`），从而更便于组织和查找翻译文件。
  - **其他改进：**
    - 清理代码，删除不必要的空行。
    - 进行小幅调整，以改善脚本的结构和可读性。
- **1.4** 新功能：
  - 支持 Anthropic Claude API 进行翻译。
  - 优化 prompt，以提高清晰度和效率。
  - 进行小幅调整，以改善代码维护性。
- **1.3** 改进与新功能：
  - 改进代码块处理。
  - 改进输出文件处理。
  - 改进现有文件检测。
  - 新增 `--force` 选项以强制翻译。
  - 反转输出文件名中的模型和语言顺序。
- **1.2** 修复 changelog。
- **1.1** 新增 Mistral IA API 支持。
- **1.0** 初始版本——支持 OpenAI API。

**使用 gpt-5.6-luna 将文章从法语翻译成中文。**
