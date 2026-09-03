### 更新日志

🌍 [法语](CHANGELOG.md) | [英语](CHANGELOG-en.md) | [西班牙语](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [德语](CHANGELOG-de.md) | [日语](CHANGELOG-ja.md) | [韩语](CHANGELOG-ko.md) | [阿拉伯语](CHANGELOG-ar.md) | [印地语](CHANGELOG-hi.md) | [意大利语](CHANGELOG-it.md) | [荷兰语](CHANGELOG-nl.md) | [波兰语](CHANGELOG-pl.md) | [葡萄牙语](CHANGELOG-pt.md) | [罗马尼亚语](CHANGELOG-ro.md) | [瑞典语](CHANGELOG-sv.md)

- **1.11.1** 文档修正：README 终于列出了七条 provider 路径（2026-09-03）：

  - **1.11.0 的 PyPI 页面写着“4 个 API + Codex CLI”。** 代码实际提供七条路径——通过 API 使用 OpenAI、Mistral、Claude、Gemini 和 Grok；通过订阅使用 Codex（ChatGPT）和 Grok，不按用量计费。简介和 _Multi-Provider_ 项目符号中遗漏了两种 Grok 模式，14 个翻译也重复了这一错误。由于软件包的长描述会按版本固定，修正展示页面必须发布新版本：这就是本版本存在的唯一原因。**代码没有任何变更。**
  - `CLAUDE.md` 已与发布内容保持一致：gate 计数器（`--full` 中为 16、17）、11 个活跃工作流、`gh pr checks` 中不可见的两个 Sonar/Codacy 计数器（hotspots、Codacy API）、每个 `ruff-format` 移动一个 `# nosemgrep`、OIDC 交换所需的 GitHub 环境，以及_pending publisher_ 不会预留名称这一事实。

- **1.11.0** 发布到 PyPI：`pip install ai-powered-markdown-translator`，然后执行命令 `aipmt`，无需克隆仓库（2026-09-03）：

  - **单文件脚本变成了可安装的软件包。** `translate.py` 从根目录移至 `src/aipmt/translate.py`，并提供控制台入口 `aipmt` 及其等价形式 `python -m aipmt`。克隆仓库仍是贡献所必需的——测试、28 个翻译和质量工具都在那里——但使用软件包不再需要克隆仓库。

    - **导入名称是 `aipmt`，绝不能是 `translate`**，因为名称冲突确实存在且不会显式报错。PyPI 软件包 `translate`（v3.8.1，最后上传于 2026-07-06）会安装同名目录。在 venv 中复现：目录优先于模块，`translate.main` 消失，入口在 `AttributeError` 处崩溃——而 `pip check` 却返回“未发现损坏的依赖”，rc=0。用户只需执行一个简单的 `pip install translate`，就足以在没有可用诊断的情况下破坏 CLI。使用真实 wheel 进行反向验证：在该软件包之上执行 `pip install translate`，`aipmt --help` 在前后均为 rc=0，两个 CLI 可以共存。
    - **发行名称较长，命令较短。** `ai-powered-markdown-translator` 能让软件包通过 PyPI 搜索找到；单独使用缩写会让不了解项目的人无法找到它，而发布的目的正是让项目能够被发现。两个看似合理的候选名称经核验后被排除：`ai-markdown-translator` 自 2024 年起已被 npm 上一个用途相同的工具占用，比本仓库早 17 个月；`aimt` 与 `aim`（v3.29.1）只差一个字母，而后者是同一领域的活跃软件包——这是造成长期混淆的最糟糕配置。顺带指出一个方法陷阱：`pypi.org/project/<nom>/` 对任何名称都会返回 200（反爬页面），只有 JSON API 才可信。
    - **采用 `src/` 布局，而不是扁平软件包。** 扁平软件包会保留测试中的六个 `sys.path.insert(..., "..")`，而这恰恰是缺陷：它们会导入源代码树而不是软件包，从而掩盖任何打包错误。实际代价是增加一条替换规则。

  - **密钥终于可以一次配置、长期使用。** 已安装的 CLI 没有持久配置：只剩环境变量和当前目录中的 `.env`。`find_dotenv` 确实会一直向上查找到系统根目录，因此**当在用户主目录下工作时**能够找到 `~/.env`，但在其他位置工作时则什么也找不到——覆盖范围取决于从哪里启动命令，而不是设计选择。因此新增第三层：`~/.config/aipmt/.env`，位于现有两层之下。

    - **优先级不是硬编码的**，而是由 `load_dotenv` 的默认值 `override=False` 决定：每一层只填补前一层留下的空缺。因此顺序为环境变量 → 项目的 `.env` → 用户配置，并通过行为测试而不是结构测试进行验证——调换前两个调用的顺序会导致测试失败，删除第三层也会失败。
    - **采用 `.env` 格式，而不是 TOML**，这是有意为之：`python-dotenv` 已是现有依赖，语法已记录在 15 个 README 中，同一个文件也可服务于两种作用域。不引入新的依赖或语法。位置遵循 `XDG_CONFIG_HOME`（前提是它是**绝对路径**）——规范要求忽略相对值，否则配置位置会再次取决于当前目录——Windows 下则使用 `APPDATA`。
    - **排除了两个选项，并说明原因。** 系统钥匙串（`keyring`）在桌面计算机上更安全，但在无头环境——服务器、容器、CI——中会失败，而这正是批量翻译的使用场景；适合作为 opt-in 方案，却不适合作为默认方案。使用 `--api-key` 标志会让密钥进入 shell 历史记录，并在 `ps` 中可见。
    - **没有密钥时，不再显示调用堆栈。** 用户此前会收到指向 `site-packages` 的 Python 堆栈，以及只提到“环境或 .env”却没有说明第二个文件应在哪里创建的消息。现在会列出三个位置及其准确路径，命令以 2 退出。这个保护范围是**有意保持狭窄的**：`except ValueError` 只作用于配置阶段。包裹整个执行过程会把翻译期间真正发生的 bug 变成令人安心的消息——这正是本仓库追踪的故障模式。一个测试读取 `main()` 的源代码以禁止这种做法。

  - **修正——安装工具后，用户的 `.env` 曾被忽略。** 不带参数的 `load_dotenv()` 不会从当前目录向上查找，而是从调用文件查找，也就是从 `site-packages` 查找。使用真实的控制台入口进行测量：从一个拥有自身 `.env` 的项目启动时，`find_dotenv()` 返回 `''`，密钥不会被加载；而 `find_dotenv(usecwd=True)` 能找到它。只要工具还仅从克隆的仓库中运行，这个 bug 就不存在；发布后它会变成系统性问题，唯一症状是配置正确却提示 API 密钥“缺失”。

  - **三个 gate 会在停止检查任何内容后仍然通过。** 它们在移动之前就被有意加固：在变更之后才编写、用来捕获该变更的防护措施无法证明任何事情。每个 gate 在原始仓库上通过，在迁移副本上失败——两个方向都进行了测量。

    - **Lizard 会悄悄忽略不存在的路径**：rc=0，并输出“0 file analyzed”。复杂度 gate 会从 158 个函数 / 2247 个 nloc 变成 3 个函数 / 34 个 nloc，且输出为零字节。现在 scope 是一个数组，并逐项验证每个条目确实存在。
    - **对不存在的模块执行 `coverage run --source=` 不会失败**：只在 stderr 输出警告，unittest 和 `coverage xml` 均为 rc=0，报告仍会发布——但从 1453 个 statements 缩减为 141 个。项目会显得健康，只因为几乎没有被分析。两个下限现在保护报告：总数下限，以及测量结果最大的文件下限。
    - **翻译新鲜度探测器在结构上无法识别调用形式的变化**：它依赖 argparse flags，而文件重命名恰恰不会改变这些 flags。复现结果是：模块被移动，15 个 README 仍记录着不存在的命令，但结论却是“没有过期翻译”。因此新增第 7 个部分，检查的是调用**形式**而不是选项；Lizard hook 也会对照脚本的真实 scope——当其 `files:` 不再匹配时，不会让 pre-commit 失败，而是让它**跳过**。

  - **`requires-python = ">=3.10"` 不再只是一个声明。** `sonar-project.properties` 早已声称支持 3.10–3.12，但从未真正运行过，因为开发环境只有 3.12——这是一个会因发布而公开暴露的内部矛盾。现在新增测试工作流，分别在 3.10、3.11 和 3.12 上运行完整测试套件，并安装软件包，从而验证其公开依赖边界。

  - **只有最低版本限制，不设置上限。** `requirements.txt` 仍是经过测试的 lock，`[project.dependencies]` 则成为公共契约：发布 lock 中的精确版本会与拥有其他软件包的用户产生冲突。`<N+1` 也不设置上限——那会与 `check-deps-fresh.sh` 直接冲突，后者会在 major 版本有任何延迟时让发布 gate 失败。最低版本集合可以解决这一问题；反向验证中，`openai==1.0.0` 以 `ResolutionImpossible` 退出，证明检查能够区分情况，而不是一律接受。此外还增加了保护措施，禁止 `pyproject.toml` 的版本与 CHANGELOG 中的版本不一致：PyPI 不允许重新使用同一个版本号。

  - **在全新的 venv 中完成端到端验证**：约 70 KB 的 wheel 只包含 `aipmt/*.py`、dist-info 和许可证；`aipmt --help` 以 rc=0 返回并显示 22 个 flags；`python -m aipmt` 显示“用法：aipmt”，而不是“用法：\_\_main\_\_.py”；`pipx` 安装后正常工作；最重要的是，**从任意用户目录执行一次真实的 fr→en 翻译**，粗体、列表、内联代码、链接和 URL 均得到保留，代码块未被翻译。迁移前的 318 个测试全部通过，前后标识符列表逐字节一致——这才证明没有测试被禁用，而不是那个“OK”；此外新增 12 个三层配置测试，总数达到 330 个。

- **1.10.0** Provider `--use_codex`（ChatGPT 订阅配额）、SDK 和模型更新、修复多段 news 引用（2026-08-29）：

  - **安全审查——PR 提出了两个防护措施，却没有在所有地方落实：**

    - **Codex 预检将整个 `.env` 传给了二进制文件。** `_codex_preflight` 调用 `subprocess.run` 时**没有 `env=`**：子进程继承了完整的 `os.environ`，也就是 `load_dotenv` 加载的全部 `.env`。使用经过检测的伪二进制文件进行测量：有**七个密钥**到达预检——六个 provider 的密钥以及一个 `GITHUB_TOKEN`——而对应的 `_grok_preflight` 则为**零个**，因为它正确传递了 `env=_grok_env()`。这是 PR 内部的不一致：`_strip_secret_env` 正是为了维护这一不变量而存在，且就在几行之外。现在提取出一个 `_codex_env_base()`，供两条路径共享；修复后测量结果为：两侧均为 0 个密钥。
    - **“`--deny` fail-closed”这一属性没有覆盖实际采用的形式。** 注释以未知前缀规则会拒绝启动为依据，为整个 Grok 隔离机制辩护。但在 `grok 1.0.13` 上测量发现，该验证**仅适用于带括号的形式**：`--deny 'CeciNestPasUnOutil(*)'` 会拒绝启动（“unknown tool prefix”），而 `--deny 'CeciNestPasUnOutil'` 会被静默接受。然而 `GROK_DENY_RULES` 只使用裸名称——因此，如果 xAI 侧重命名工具，就会移除唯一经过测量的隔离层，且完全没有信号；在这种情况下，OS sandbox 本来也不适用。八条命名规则会传入 `Prefix(*)`，并逐一验证为 CLI 已知前缀；catch-all `*` 保持字面形式，这是唯一被接受的形式。一个测试防止恢复未验证的形式。
    - **其他方面均已完成干净验证**：不存在命令注入（所有地方都使用列表形式，从不使用 `shell=True`；文档内容通过 stdin 或 `--prompt-file` 传入），不存在不安全反序列化（仅使用 `json.loads`，并带类型保护），路径遍历修复在七组载荷上均未发现绕过方式，并且 `--deny '*'` 确实由 CLI 应用（在 workdir 外读取时观察到 `DENY_ENFORCED`）。
    - 上文新增的新鲜度检查也顺带绕过了自身的原则：当 PyPI 请求失败时，软件包会被静默跳过，gate 仍然通过。现在会统计实际完成比较的软件包数量，并在覆盖不完整时失败。

  - **依赖已升级，并增加两道防护以避免再次延迟：**

    - **延迟确实存在且持续时间很长**：`openai` 从 2.54 → **3.6.0**，`anthropic` 从 0.125 → **1.2.0**，`certifi` 从 2024.8.30 → **2026.7.22**——这意味着验证所有 provider 调用 TLS 的根证书存储延迟了两年。原因已确认：**不存在 `.github/dependabot.yml`**。没有该文件时，GitHub 只会启用 _security updates_，Dependabot 也只会为受 CVE 影响的依赖提出 PR——这解释了为什么它更新了 `urllib3` 和 `idna`，却让两个 SDK 从 major 版本上落后。
    - **两个 major 版本可以无冲突共存**，与先前推理担心的情况相反：`openai` 3.x 和 `anthropic` 1.x 会迁移到 **`httpx2`**，而 `mistralai` 和 `google-genai` 仍停留在 `httpx<1`，但它们是两个不同的发行版。通过真实安装验证，随后对**七条 provider 路径进行了端到端测试**——OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI 和 Grok CLI——每条输出中的内联代码和链接均得到保留。“避免两套 HTTP 栈”只是偏好，而非阻塞条件：测量结果作出了决定。
    - **`requirements.txt` 并未描述真实环境**：`google-auth`、`cryptography` 和 `opentelemetry` 栈都安装在工作 venv 中，却从未声明——因此全新安装无法复现实际测试环境。相反，`tokenizers`、`huggingface-hub` 和 `PyYAML` 出现在其中，却没有被任何代码导入或要求，是 `mistralai` 1.x 遗留下来的内容。该文件现已根据仅包含直接依赖构建的 venv，重新生成完整依赖闭包。`pip-audit` 未报告新依赖集合中的任何已知漏洞。
    - **`.github/dependabot.yml`**（新增）启用每周版本、pip 和 github-actions 更新。次要版本和修订版本合并到同一个 PR 中——每个 PR 只更新一个 patch 往往会被忽略，而噪声是更新的敌人；**major 版本单独处理**，每个版本都要求通过真实调用进行验证。
    - **`scripts/check-deps-fresh.sh`**（新增，并接入 gate）让延迟直接体现在项目结论中：Dependabot 会提出建议，但不会保证执行，而且 PR 可能堆积。major 版本延迟 → 失败；minor 版本延迟 → 警告，因为一个永久为红的 gate 最终会被忽略；无法访问 PyPI → 本地显式跳过，**CI 中 fail-closed**，未执行的检查不能算成功。两个方向均已验证：它能捕获修复前的精确状态（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`），并且只对 minor 版本发出警告。

  - **本次 PR 审查产生的修正**——五名审查代理彻底检查了 diff；以下问题在修正前均已通过测量**复现**，其中两个是同一版本前文引入的回归。
- **已修复回归问题——`_NEWS_CITATION_REGEX` 存在指数级回溯。** 多段落修复在重复部分引入了 `(?:[ \t]*$|[ \t]+.*)`：`[ \t]+` 与 `.*` 之间的空格共享存在歧义，而这种歧义会在每次迭代中不断倍增。在不匹配该模式的 `>   texte` 行——完全合法的 Markdown 缩进——上测得：**14 行耗时 2,589 ms**，修复后为 0.04 ms；每增加一行，耗时约增加 9 倍。在 `--news` 模式下，一段很长且不符合规范的 blockquote 就足以让翻译冻结，直到任务超时，且没有可识别的原因。现在重复部分一次性消耗整行（`\n^>(?![ \t]*—).*`），因此每次迭代只有一种匹配方式。在包含 231 篇真实文章的语料库上验证：**捕获结果零差异**，仍为 423 条引用，14 个多段落正文也都继续被完整展开。
    - **同时启用两个 provider flag 时会被静默按用量计费。** `--use_codex --use_mistral` 会被接受；`_select_provider_client` 优先测试 Mistral，`_resolve_provider` 优先处理显式布尔值——两者最终都会选择 Mistral。因此用户本想使用订阅额度，却遭遇了按用量计费，而且完全没有警告：这正是 `--use_codex` 存在的目的，用来防止这种故障模式。现在六个 provider flag 都通过一个 `add_mutually_exclusive_group` 处理。**行为变更**：同时指定两个 provider 的命令行过去会被静默接受，现在会在 `argument --use_mistral: not allowed with argument --use_codex` 上失败。
    - **工作结束门禁在探针崩溃时仍会通过。** `scripts/check-release-ready.sh` 的十三项检查中有四项遵循“捕获 stdout，若为空则得出结论”的模式，却从不检查返回码：异常（文件被重命名、`FileNotFoundError`）会写入 stderr，使 stdout 为空，检查便得出“没有需要报告的内容”。为了防止这一问题而编写的脚本内部，竟再次出现了“一个 `exit 0` 什么也证明不了”的陷阱。现在 helper `probe()` 同时要求返回码为零 **以及结束哨兵**，探针也拒绝在标记集合为空时得出结论——对空集合的断言永远为真。演示如下：上文加入独占组后，provider flag 通过一个 `*_group` 对象传递，而旧的正则表达式 `parser\.add_argument\(` 已无法匹配；**21 个 flag 中有 6 个**静默脱离检查范围，门禁却显示为绿色。
    - **秘密扫描漏掉了六个 provider 中的四个。** `[A-Za-z0-9]` 类排除了连字符：`sk-proj-…`（当前 OpenAI 格式）和 `sk-ant-api03-…` 会在第二个连字符处失败，而 `AIza…` 未被覆盖。现在已扩展模式，并将 `.secrets.baseline` 排除在扫描之外。此外，`.env` 询问的是 `git diff --cached`，它只能看到索引：一个**已经提交**的 `.env`——最糟糕的情况——从未出现在其中。现在改为询问 `git ls-files`。
    - **Codex 的“token 预热”并不是真正的预热。** 测量结果显示：`codex login status` 不会触碰 `~/.codex/auth.json`（mtime 和大小均未改变），其帮助信息写的是“显示登录状态”。然而注释却声称会“按顺序执行一次” token 刷新，从而消除一次性轮换 token 的并发刷新风险。所宣称的保护并不存在；现在注释只描述代码实际执行的内容，真正的防护仍是 `max_jobs=4`。该检查还会遵循 `CODEX_BIN`，此前却忽略了它——没有 `codex` 的机器在 `PATH` 中会因“未认证”而失败，导致诊断具有误导性。
    - **`.env` 在子 shell 中被加载。** `detect_provider` 通过命令替换调用，因此其中的导出变量无法传回：在 `.env` 中定义的 `GROK_BIN`、`GROK_HOME` 或 `REGEN_MODEL`，对 `main()` 中的读取仍不可见，后者便会在配置正确时错误地得出“找不到 Grok 二进制文件”。
    - **并发量比公布的上限高出 50%。** 保护逻辑位于 README/CHANGELOG 配对启动之后；测得峰值为 **`max_jobs=2` 进程 3 个**。对于 Grok，其每周额度与 Chat/Imagine/Voice 共享且无法测量，因此脚本为自己设定的上限并未得到遵守。最终计数虽然会显示，却从未与 28 比较——缺少一个文件也不会被发现。
    - **Grok 输出契约：缺少 `stopReason` 现在会失败。** 代码此前使用“`end_turn` **或缺失**”，而已公布的契约要求 `end_turn`。没有该字段的 payload，或该字段因 CLI 更新而被重命名，都会使保护逻辑静默失效。此外，`max_turn_requests` 不再被归类为 rate limit（耗尽的是轮次预算：重试只会得到相同结果，却要付出 90 秒等待），而 `quota` 也不再输出 rate limit 标记——原因早已由 `_codex_is_rate_limited` 的 docstring 阐明，只是 Grok 尚未遵循。
    - **Gemini 级联现在按模型进行记忆化。** 它在每个片段都从 `minimal` 重新开始，而默认模型会拒绝该选项：正常路径为每个片段付出一次 400 往返，并重复打印同一警告。警告重复数百次后就不再有人阅读——这正是它变成掩盖问题的面具的方式。
    - **其他事项**：CI 中的拒绝消息被硬编码为 Codex 相关内容，会将 `--use_grok_cli` 用户引导至 `OPENAI_API_KEY`，而不是 `XAI_API_KEY`；`provider.capitalize()` 显示为“Grok_cli”和“Openai”；子进程基础设施的注释将“shim”泛化到两个 CLI，尽管 Grok 二进制是原生 ELF（正确理由应为“会自行生成子进程的 agent”）；`subprocess` 上的十二项 SAST finding 已标记为 `# nosec` / `# nosemgrep` 并附带说明，无 `shell=True` 的列表形式使注入无法发生，且文档内容从未经由 argv 传递。
    - **agent 子进程不再接收任何秘密。** 具名 deny-list 只保护了**计费**这一不变量（Codex 不带 `OPENAI_API_KEY`，Grok 不带 `XAI_API_KEY`）。测量显示：**另外七个秘密**仍会进入每个子进程——Anthropic、Mistral、Google 和 Gemini 的密钥、另一个 CLI 的密钥，以及 `OPENAI_BASE_URL`；后者不是秘密，但会重新导向流量。然而这两个 CLI 都是 **agent**，而 Grok 在许多 Linux 机器上运行时没有适用的 OS sandbox。现在改为**按名称模式**过滤（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`），而非使用具名列表，因此也能覆盖用户在 `.env` 中添加、但代码并不知道的变量。CLI 无需其中任何变量：认证保存在 `~/.codex` 和 `~/.grok` 中，从不放在环境中——已通过两个 provider 各自完成一次**真实且成功的翻译**，并验证加固后的环境。
    - **测试**：新增文件 `tests/test_review_hardening.py`（21 项测试），锁定 provider flag 的互斥性、`stopReason` 契约、news 正则表达式的线性特性、CI 拒绝消息、Gemini 记忆化，以及子进程环境中不存在任何秘密。最后一项断言是**通用的**——遇到任何列表中未命名的密钥都会失败；而现有的清除测试只是其常量的镜像，只能检测自身循环的故障。完整测试套件现为 **311 项测试**。

  - **新增两个 Grok provider**：`--use_grok`（xAI API，密钥为 `XAI_API_KEY`，按用量计费）和 `--use_grok_cli`（官方 Grok Build CLI，从 Grok 订阅中扣除额度——原理与 `--use_codex` 相同）。
    - **API 模式，约 40 行**：由于 xAI endpoint 与 OpenAI 兼容，客户端和 `_call_openai` 原样复用，只需更改 `base_url`。只需一次适配，而且所有 provider 都能受益：`finish_reason` 现在接受 `end_turn`，即 xAI 输出的形式，而 OpenAI 输出的是 `stop`。模型：`grok-4.6`（质量）和 `grok-4.3`（经济）。需要注意的是，Grok 的经济模型仍是仓库中最贵的——每百万 token 为 $1.25/$2.50，而 `mistral-small-latest` 为 $0.15/$0.60：选择该 provider 是为了模型多样性，而不是价格。
    - **CLI 模式**：以 Codex 为基础，但因实际情况必须存在四点差异——提示词通过文件传入（`--prompt-file`；CLI 不读取 stdin，而将片段放在 argv 中会暴露于 `ps`），输出是 stdout 上的单个 JSON 对象（既不是 JSONL，也不是 `-o` 文件），订阅只公开 `grok-4.6` 和 `grok-4.5`，且 sandbox 无法应用（见下文）。子进程启动逻辑与 Codex 一起提取到 `_codex_run_process` 中，不触碰已经测试过的 Codex provider 其余部分。
    - **实测表明，`exit 0` 什么也证明不了**：未认证时，CLI 会在 **stdout** 中输出 `{"type":"error","message":"Not signed in."}`，且返回码为 **0**。拒绝或轮次耗尽时行为也相同。因此输出契约要求四个条件同时满足：返回码为 0、没有错误 payload、存在 `stopReason == end_turn`，以及文本非空。预检遵循相同逻辑：即使处于断开连接状态，`grok models` 也会以 0 退出，只有 stdout 中出现“未认证”才能得出结论。
    - **隔离：明确记录并接受这种不对称性。** Codex 在 `--sandbox read-only` 中运行，而 Grok 的 sandbox 在许多近期 Linux 机器上无法应用；原因有两个彼此独立的系统限制，若没有 `sudo` 就无法绕过：自 Ubuntu 24.04 起，AppArmor 会阻止非特权 user namespace（`bwrap: setting up uid map: Permission denied`，已在 Grok 之外复现）；当 `/run/podman` 处于 `0700` 时，容器运行时 socket 的 deny-list 会失败（resolver 只会回退处理 `ErrorKind::NotFound`，EACCES 会变成致命错误）。核心陷阱是：无法应用的**集成式** profile 会**静默地以未隔离状态启动**。因此脚本默认不请求任何 profile，也绝不静默回退——它会在 stderr 上发出警告。保护依赖 CLI 的 `--deny` 规则，包括 catch-all `*`；这是唯一经过测量的 _fail-closed_ 层（未知前缀的规则会拒绝启动）。`GROK_TRANSLATE_SANDBOX=read-only` 允许强制要求隔离，此时如果机器无法满足，启动就会失败。
    - **防护措施**：`XAI_API_KEY`、`GROK_API_KEY` 和 `GROK_SANDBOX` 会从子进程环境中移除（某个密钥会切换到按用量计费；继承的 `GROK_SANDBOX` 会强制使用不适用的 profile，并产生误导性消息），MCP/hooks/skills/agents 开关均已禁用，`--disable-web-search`、`--no-subagents`、`--no-plan`、临时 workdir、CI 中拒绝、会终止进程组的超时，以及 rate limit 退避机制均已启用。`--max-turns` 被设为 6 而不是 1：计数器会在工具轮次之后递增，设为 1 会截断输出。
    - **额度**：Grok 额度按周计算，并且**与 Chat、Imagine 和 Voice 共享**，没有任何命令会公开该额度——不同于 Codex，后者可通过 `account/rateLimits/read` 计算消耗。因此 `regen_translations.sh` 将并发限制为 2，并明确发出警告。
    - **测试**：新增文件 `tests/test_grok_provider.py`（24 项测试）。完整测试套件现为 **290 项测试**。
  - **已修复 bug——EN 多段落引用仅在 `--news` 模式下得到部分保护**：`_NEWS_CITATION_REGEX` 作为引用正文，只接受一串**连续**的 `>` 行。一旦引用跨越多个段落（由一行 `>` 空行分隔），只有最后一个段落会被捕获并替换为占位符；前面的段落会发送给 LLM 并返回翻译结果——这恰好违背了 `--news` 存在所要保证的目标。现在重复部分接受内部的 `>` 空行，并改为非贪婪匹配，从而会在斜体行之前的 `>` 空行处停止，而不是在遇到第一个空行时停止。
    - **实测规模**：在包含 198 篇真实文章的语料库中，419 条引用里有 11 条受到影响。没有发生回归——新的正则表达式捕获的引用数量完全相同，只是多段落正文得到了扩展（408 个正文不变，11 个正文扩展），归属行 `> — …` 仍无法被吸收到正文中（lookahead 保留）。
    - **端到端证据**：在一篇 69 KB、翻译为 ja/ar 的文章上，引用的第一段此前在日语中被渲染为 `> GLM-5.3がオープンウェイト化。`，在阿拉伯语中也同样被翻译；现在则仍保持为 `> GLM-5.3 is now open-weight.`。英文引用行数从 9 恢复为 10，与源文档一致。
    - 需要注意：下游验证器不会检测到这一缺陷，因为它们只检查引用是否存在，不检查引用是否完整。
  - **默认 provider 上的实测节省**：只要模型以 `gpt-5` 开头，`_openai_extra_kwargs` 就会发送 `reasoning_effort="medium"`，包括 `--eco`。在 `gpt-5.4-mini` 上翻译一句十词句子的测量结果：`medium` → 45 个 reasoning token 和 65 个输出 token；`none` → 0 和 14。推理对翻译没有帮助，却会在每个文件的每个片段上产生费用。现在默认值在 `--eco` 中变为 `none`，其他情况下仍为 `medium`；通过 CLI 显式传入的值仍具有优先级。`--reasoning_effort` 现在除 `low`/`medium`/`high` 外，还接受 `none` 和 `xhigh`（并非所有模型都接受这些值：例如 `gpt-5.4-mini` 会拒绝 `minimal`——现有的不带参数重试机制可以覆盖这种情况）。
  - **SDK 更新与 Gemini 迁移**：`google-generativeai`（支持已于 2025-11-30 结束，仓库已归档）被统一 SDK **`google-genai`** 替代——先使用 `genai.Client(api_key=...)`，再使用 `client.models.generate_content(model=, contents=, config=)`，系统提示词通过 `system_instruction` 传入，而不是与片段拼接。`mistralai` 升级至 **2.9.4**（导入改为 `from mistralai.client import Mistral`；旧导入会抛出 `ImportError`，已在 wheel 中验证），`anthropic` 升级至 **0.125.0**，`openai` 升级至 **2.54.0**——这是切换到 `httpx2` 前的最后版本，以避免 venv 中并存两套 HTTP 栈。`httpx` 0.28.1 和 `pydantic` 2.13.5 也因此解除阻塞。
  - **两个由真实测试而非文档捕获的回归**：
    - `anthropic` ≥ 1.0 会在客户端拒绝非流式调用，只要其 `max_tokens` 预示调用时间超过 10 分钟（`ValueError: Streaming is required...`）。0.34.2 中不存在这一保护，导致所有带有 `max_tokens=32768` 的 Claude 调用失败。现已通过显式的 `timeout` 修复（`CLAUDE_TIMEOUT`，默认为 900 秒），这样对于只需要完整响应的调用，不必切换到 streaming。
    - `thinking_level="minimal"` 仅被 Gemini 模型目录中的一部分接受：`gemini-3.1-flash-lite` 支持它，而 `gemini-3.7-flash` 和 `gemini-3.1-pro-preview` 会返回 400 拒绝。因此加入 `_gemini_generate_with_fallback`，级联顺序为 `minimal` → `low` → 不设置 thinking_config，仿照现有的 OpenAI fallback——优化参数绝不能导致翻译失败。
  - **更新默认模型**，每个模型都通过真实调用验证：OpenAI `gpt-5.5` → **`gpt-5.6-terra`**（批量处理 28 个项目时降低 60%），以及 `gpt-5.4-mini` → **`gpt-5.6-luna`**（降低 73%）；Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**（更便宜且更新）以及 `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（不带日期的规范 ID）；Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**，以及 `gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（稳定版本，且比 `3.5-flash-lite` 更便宜）。
Mistral 保持不变，`mistral-large-latest` 仍是四者中性价比最高的。需要注意的是：不存在比 `gemini-3.1-pro-preview` 更新的 Gemini Pro 系列模型——2026 年 5 月宣布的 Gemini 3.5 Pro 从未发布；3.5/3.6/3.7 系列完全属于 Flash。
  - **切换 Gemini 前已完成 A/B 测试**：使用 `gemini-3.1-pro-preview`，再通过 `gemini-3.7-flash` 将 `README.md` 翻译成日语。结构完全一致（21 个列表、18 个代码块、13 个 HTML 链接、13 张图片，所有 URL 均得到保留），耗时为 **8 秒，而非 48 秒**。由于没有公开基准测试比较这两个模型在翻译或非拉丁文字脚本方面的表现，否则这次切换只能建立在简单推测之上。
  - **过滤 Claude 响应块**：`_call_claude` 在不筛选类型的情况下执行 `block.text for block in response.content`。自适应推理模型（Sonnet 5 及更高版本）会插入一个 `thinking` 块，其中暴露的是 `.thinking`，而不是 `.text`——翻译会在第一个片段遇到不透明的 `AttributeError` 时崩溃。现在会排除 `thinking`、`redacted_thinking`、`tool_use` 和 `tool_result` 块（采用黑名单，以便对携带文本的未知类型保持宽容），如果响应中完全没有文本块，则会抛出明确错误。每次调用都会传递 `thinking={"type": "disabled"}`。
  - **重新同步 `MODEL_TOKEN_LIMITS`**：删除撤回日期已过的模型（`magistral-*` 系列于 2026-07-31 撤回，`gemini-2.0-*` 于 2026-06-01 撤回，`gemini-3-pro-preview` 于 2026-03-09 撤回，以及 `claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。修正限制：Mistral 128K → **256K**（Large 3 / Small 4 一代），Gemini 1 000 000 → **1 048 576**（实际输入限制），`claude-opus-4-5` 200K → **1M**，`gpt-5.6-*` 系列 400K → **1.05M**。新增 Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest` 以及 `ministral-*` 系列。需要注意的是，这些限制仍为参考值，因为 `translate()` 将分段上限限制为 `min(16000, limite)`。

  - **Provider `--use_codex`**：第五个 provider，通过非交互模式下的官方 Codex CLI（`codex exec`）运行，而不是调用按使用量计费的 API。翻译消耗的是已经支付的 ChatGPT 订阅配额。这是 OpenAI 针对该用途唯一有文档说明的方式：按套餐划分的可用性矩阵将“Codex SDK、`codex exec` 和可脚本化工作流”列为 Plus/Pro/Business/Enterprise 可用，而 `~/.codex/auth.json` 的令牌无法验证 Platform API 调用（并且该脚本从不读取它们——身份验证及其刷新仍由 CLI 管理）。
  - **Codex 二进制文件现在可通过 pip 安装，不再只能通过 npm 安装**：`_resolve_codex_binary()` 会先在 `CODEX_BIN` 中查找二进制文件，然后查找 `PATH`，最后查找由 OpenAI 发布的官方 Python 包 **`openai-codex-cli-bin`**（这是 `openai-codex` SDK 的依赖项）。因此，Python 项目不再需要全局安装 npm，即可使用 `--use_codex`。该包不会加入 `requirements.txt`：二进制文件约 250 MB，这会迫使所有用户为一个可选 provider 承担这项依赖。端到端验证结果：当 `codex` 不在 `PATH` 中时，解析会找到打包的二进制文件，并在 6 秒内完成完整翻译。
  - **“订阅模式”保障**：`OPENAI_API_KEY` 和 `CODEX_API_KEY` 会从子进程环境中移除。没有这项保护，`.env` 中存在的密钥可能会让 Codex 切换到按使用量计费模式，且完全没有可见提示——这正是该 provider 要避免的情况。
  - **CLI 陷阱已通过测试锁定**：
    - `codex exec` 即使提示词作为参数传入，也会读取标准输入：如果不关闭标准输入，该命令会一直等待直到超时，且从未调用模型（已复现：180 秒后退出码为 124，输出 0 字节）。因此必须使用 `communicate(input=...)`。
    - 通过 npm 安装的 `codex` 是一个 Node shim，它会 `spawn` 真正的 Rust 二进制文件：后者是 Python 进程的**孙进程**，并且会在 `SIGKILL` 之后继续运行，在 `subprocess.run(timeout=)` 时仍会消耗配额。因此需要 `Popen(start_new_session=True)` + `os.killpg`。
    - CLI 可能在输出 `turn.failed` 的同时仍以 0 退出：除返回码外，还会检查 JSONL 输出（`--json`）；如果返回码为 0 但缺少 `-o` 文件，则会抛出明确错误，而不是生成空片段。
  - **速率限制退避**：CLI 不实现内部重试（`max_retries = 0`）。分类依据 JSON 载荷结构（`status: 429` / `error.type`），而不是子字符串——“quota”一词既可能出现在可恢复的 429 错误中，也可能出现在不可恢复的 `insufficient_quota` 中。
  - **CI 保护**：如果定义了 `CI` 或 `GITHUB_ACTIONS`，则拒绝使用 `--use_codex`。订阅身份验证不适用于共享 runner，且 OpenAI 明确不建议在公共仓库中采用这种工作流。
  - **模型**：`gpt-5.6-sol`（质量）和 `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` 系列同时用于 CLI 和 Platform API，但 ChatGPT 账户并非对其中所有模型都有权限：allowlist 在服务器端应用，不进行本地验证，使用异常模型时会触发警告。在 Plus 套餐下，Luna 每个 5 小时窗口提供 250–2,000 条消息，而 Sol 仅提供 10–100 条：对于任何批处理，推荐使用 `--eco` 模式。
  - **已修复的 bug——`regen_translations.sh` 在完全成功后仍报告错误**：`trap ... EXIT` 引用了 `failed_log`，这是 `main()` 中的一个 `local`，在 trap 执行时已不存在。在 `set -u` 下，这会抛出 `failed_log: unbound variable`，使脚本以 1 退出，尽管 28 个翻译均正确——这会在重新生成之后、最耗时的步骤中断 `release.sh --auto`（`set -e`）。现在该变量变为全局变量，trap 会检查其是否存在。一个有用的副作用是：此前被该错误掩盖的真实翻译失败会重新显示在最终摘要中。
  - **`REGEN_MODEL`**：`regen_translations.sh` 的新环境变量，可强制指定模型，覆盖 provider 的默认模型，例如使用 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`，在订阅配额内通过高端模型重新生成，而不是使用面向批量处理的 `--eco` 模型。
  - **`regen_translations.sh`**：`REGEN_PROVIDER=codex` 可通过显式 opt-in 使用（绝不自动检测，以免在用户不知情的情况下消耗订阅配额）。在开启并行处理前，会先顺序刷新一次令牌——Codex 刷新机制具有轮换性且令牌只能使用一次，并发任务会使 `codex login` 会话失效——并将并发数降至 4。
  - **相关重构**：`_dispatch_provider_call` 通过一个返回 provider 名称的 `_resolve_provider()` 从 8 个参数减少至 6 个参数，而不是在整条调用链中传递第四个布尔值。为保留使用最小 `Namespace` 调用 `translate(..., use_mistral=True)` 的测试，显式布尔值仍优先于 `args`。
  - **测试**：新增文件 `tests/test_codex_provider.py`（48 个测试），覆盖 argv、清理后的环境、反前言契约、静默失败、超时/killpg、退避、预检、provider 解析、Gemini 推理级联、Claude 块过滤以及多段新闻引用。完整测试套件现有 290 个测试。
  - **实际验证**：通过 Codex 将项目的 `README.md` 翻译成**14 种语言**后，结构与参考翻译完全一致（14 个代码块、24 个标题、25 行表格、13 个 HTML 链接、13 张图片、19 个 URL，代码块逐字符一致，且没有残留 placeholder）。对于一篇 69 KB 的新闻文章，在 `--news` 模式下，`gpt-5.6-luna` 和 `gpt-5.6-sol` 的输出均通过了下游应用验证器（en/ja/ar）。通过 `account/rateLimits/read` 测得的消耗仍低于计数器的舍入阈值（5 小时窗口的 0%），使用的是 `--eco` 模式。

- **1.9.2** 修复带嵌套括号或法语前缀的新闻归属 URL 提取（2026-05-11）：

  - **已修复的 bug**：`_protect_news_quotes` 中的归属 URL 提取使用了正则表达式 `re.search(r"\((.+?)\)", attribution)`（括号之间的惰性捕获）。对于类似 `(relayé par [@user sur X](https://x.com/.../123))` 的归属信息（嵌套括号：外层的 `(` 加上 Markdown link 的 `]()`），捕获会在遇到第一个 `)` 时停止 → 字符串被截断，并包含法语前缀：`relayé par [@user sur X](https://x.com/.../123`（缺少末尾的 `)`）。结果是：`_validate_news_post` 会在翻译输出中查找该字符串，并始终失败（两个原因：`)` 被截断，以及“relayé par”被翻译成 `relayed by`/`weitergeleitet von`/……）。完整的 low → medium → high → gpt-5.5 级联无法通过。
  - **修复**：正则表达式改为 `re.search(r"\]\(([^)]+)\)", attribution)`——专门定位 Markdown link 的 `](url)`，只捕获**纯 URL**（不含法语前缀，也不被截断），并通过翻译期间的 `#URL{N}#` placeholder 保持不变。对以下两种问题模式均具有鲁棒性：
    - `(relayé par [@account sur X](url))` ——嵌套括号
    - `via [@source](url)` 或 `selon [@author](url)` ——没有外层括号的法语前缀
  - **测试**：在 `test_silent_failure.py` 的 `TestNewsCitationExtraction` 类中新增 2 个测试：
    - `test_extract_attribution_url_with_nested_parens`（精确复现 Genspark CEO E2B bug 的案例）
    - `test_extract_attribution_url_with_french_prefix`（带有 `via` 的变体）
  - **覆盖缺口**：`check-editorial-coverage.py` 验证编辑语法，但不验证 translator 是否能够翻译。一个可能的改进（不在 v1.9.2 范围内）是在发布前增加一项检查，通过 dry-run 模拟归属信息提取，以检测存在风险的模式。

- **1.9.1** 修复翻译 marker 注释中 CTA 标签的 i18n（2026-05-10）：

  - **已修复的 bug**：已翻译文件顶部 marker 横幅中的 CTA 链接标签 `[Voir le projet sur GitHub ↗]` 对所有目标语言仍然**使用法语**，而不是跟随 `target_lang`。LLM 从未看到该标签（它由 Python 端组装，以保留 URL 和仓库 slug），因此翻译阶段无法修正。自 v1.9 添加 `marker` 格式以来一直存在这一静默回归。
  - **修复**：新增常量 `_VIEW_PROJECT_LABELS`，将 15 种语言映射到本地化标签。`_translation_note_invariants(target_lang)` 和 `_assemble_translation_note_paragraphs(phrase, target_lang)` 现在会传递目标语言。未知语言时回退到 `fr`（安全处理，不会触发 KeyError）。
  - **测试**：调整 `test_source_emits_three_paragraphs_repo_title_description_link`（target_lang `ja` → 预期日语标签）。新增 2 个测试：`test_source_link_label_localized_per_target_lang`（针对 7 种语言参数化，覆盖拉丁文字、表意文字和 abjad 文字）以及 `test_source_link_label_falls_back_to_french_for_unknown_target`。总计：`test_translation_note_position.py` 中有 40 个测试（原为 38 个）。
  - **向后兼容**：使用默认值 `target_lang="fr"` 的签名——不传递 `args.target_lang` 的外部程序调用方仍可继续运行，无需修改。
- **1.9** 修复静默失败 + 完整质量工具链 + 多位置翻译说明（2026-05-07）：
  - **多位置翻译说明 + “embed card”格式标记**：
    - 新增 CLI 选项（附加功能，默认值不变 → **不破坏兼容性**）：
      - `--note_position {top,bottom,both}`（默认值：`bottom`）：将说明放置在已翻译文件的顶部、底部，或两个位置。
      - `--note_format {legacy,marker}`（默认值：`legacy`）：
        - `legacy` 严格复现 v1.8 行为（粗体段落 `**…**`），**逐字节一致**。
        - `marker` 输出一个不可见的 Markdown 链接引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），随后输出一个结构化的**三段式引用块**，用于呈现类似“GitHub repo embed card”的效果：项目标题使用行内代码（`**\`ai-powered-markdown-translator\`\*\*`）、由 LLM 翻译的描述，以及带可见箭头的 CTA 链接（`[Voir le projet sur GitHub ↗](URL)`）。可由 remark 插件在构建时处理（参见 blog jls42.org → 插件 `remark-translation-banner`）。
    - **绝不发送给 LLM 的不变量**：仓库标题和 GitHub URL 在描述句翻译完成后由 Python 端组装。LLM 永远不会看到 slug `ai-powered-markdown-translator` 或 `https://github.com/jls42/...`，从而确保任何 renderer、转义符或 scheme 都不会被改动。
    - **识别 frontmatter 的插入**：在 `top` 或 `both` 模式下，说明会插入在 YAML frontmatter 的**结束 `---` 块**之后（确保 Astro Content Collections / gray-matter 安全）。Helper `_split_frontmatter` 会检测文件开头的 `---\n…\n---\n` 并保持其完整性；对于已打开但没有结束 fence 的 frontmatter，**抛出 `RuntimeError`**（文件会进入 `failed_files`，而不会带着位置错误的说明写入）。
    - **模型 sanitizer 白名单**：`_sanitize_model` 会将所有不属于 `[A-Za-z0-9._:/-]` 的字符替换为 `_`；若结果为空则回退到 `unknown`。这与 Astro remark 插件侧的验证器保持一致，并会消除可能破坏标记格式的字符（空格、引号、括号、逗号等）。
    - **内部重构**：`_append_translation_note`（1 个单体函数）→ 7 个纯 helper（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。Builder 与 composer 分离（builder 返回不带分隔符的纯块，composer 根据位置应用 `\n\n`）；生产代码和源代码 helper 共用同一个三段式组装器。
    - **`_quote_lines` 保留空行**：为每行添加前缀 `> `，将空行转换为仅包含 `>` 的行。这样 mdast 能在引用块中识别出 3 个不同的段落（标题 / 描述 / 链接），而不是将其视为包含换行的单个段落。
    - **`_build_translation_note_block` 自适应**：根据 LLM 保留的段落数量进行处理（3 段 = 完整卡片格式，2 段 = 句子 + 链接，1 段 = 回退格式）。当检测到 Markdown 链接 `](` 时，单段回退格式不再包裹在 `**...**` 中（因为在链接周围使用 `<strong>` 的渲染不稳定）。
    - **向后兼容**：`getattr(args, "note_position", "bottom")` 和 `getattr(args, "note_format", "legacy")` 位于 `_compose_with_notes` 一侧——没有这些属性的 Namespace（现有测试、外部程序化调用）仍可无需修改地运行。
  - **修复长文本翻译的静默失败**：
    - 所有 provider（OpenAI、Mistral、Claude、Gemini）均增加翻译后语言验证：确定性层（逐字检索源文本片段）+ 概率性层（`langdetect`）。
    - 白名单 `finish_reason` / `stop_reason`：任何不在白名单内的状态（截断、content_filter 等）都会抛出 `RuntimeError`。
    - `max_tokens` Claude：`4096` → `32768`（避免 16k 分段出现潜在截断，并为 FR→JA/ZH/KO/AR/HI 的跨文字系统转换保留余量）。
    - 识别标题的分段：在分段的后半部分优先放置 H2/H3（每个分段都从一个完整的语义章节开始）。
    - 错误传播至非零退出码：`translate_markdown_file` 返回类型化状态 `success` / `failure` / `skipped`；如果至少有一个文件失败，`main()` `sys.exit(1)`（单文件和批处理均适用）。
    - 所有 provider 增加空内容保护、源文/输出文合理比例检查（≥ 500 个字符，< 5% 则拒绝）、代码占位符验证（`#CODEBLOCK`/`#INLINECODE`）、LLM 后标准化（修复粘连在标题上的分隔符/链接）、`BadRequestError` 不带 `reasoning_effort` 的重试。
    - 新增依赖 `langdetect==1.0.9`。
  - **提交前质量工具链**（“完整的 EurekAI 类型”工具链，14 个 hook）：
    - Pre-commit：ruff（lint + format）、shellcheck、prettier（md/yaml/json）、detect-secrets（保护 4 个 API key）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（空白字符、文件末尾、超大文件、shebang 等）。
    - Pre-push：mypy（逐步推进的 lax 模式）、Opengrep SAST（translate.py + scripts/）、pip-audit（初始 reporting 模式）、unittest discover（tests/ + scripts/tests/）。
    - `scripts/` 中的本地 wrapper 使用 `./venv/bin/python`。
    - `scripts/audit_verdict.py`：使用 11 个 unittest 测试解析 pip-audit JSON，这是 jls42-astro parser 的 Python 移植版本。
    - 修复最初的 7 个 ruff 违规：B904（raise from）×2、B007（未使用的 dirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）。
    - Lizard 暂时排除 `translate.py`（4 个函数的 CCN 为 21–47，计划重构）——对 scripts/ 实施严格 gate。
  - **SonarCloud + 全面覆盖率**：
    - GitHub Actions 工作流 `SonarCloud`（sonarcloud.yml + sonar-project.properties）：每次 push 和 pull-request 都进行分析，通过 `coverage.xml` 统计覆盖率。
    - README 顶部新增 11 个 SonarCloud 徽章（Quality Gate、Security/Reliability/Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）。
    - `tests/test_silent_failure.py`（`unittest` 标准库）：覆盖静默失败错误链的六个环节。
    - `tests/test_orchestration.py`（+79 个测试）：覆盖 `translate.py` 的编排层（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` TypeError + BadRequestError 回退、o1-series prompt 格式、`_validate_translation_output` 的提前返回分支）。
    - `scripts/tests/test_audit_verdict.py`：通过 subprocess 覆盖 `main()`（stdin/stdout）以及 `if __name__ == "__main__"` 代码块。
    - **新代码覆盖率**：75.5% → 约 98%（translate.py 98%，scripts/audit_verdict.py 97%）。
  - **测试**：`tests/test_translation_note_position.py` 覆盖位置 × 格式矩阵（包括 E2E `marker+top|bottom|both` 和 `legacy+top|bottom|both`）、多行前缀、逐字节向后兼容（golden literal）、sanitizer、frontmatter 拆分（包括未闭合 fence 时的 raise）、三段式格式、两段式回退、单段 + Markdown 链接保护，以及一个关键防护 `TestLLMPayloadExcludesInvariants`，断言标题和 URL 永远不会发送给 LLM。**190 个测试通过**，0 个回归。
  - 文档：`README.md`（法语 + 14 种翻译，含徽章）、`CLAUDE.md`（详细的 pre-commit 工作流 + CI 监控）、重新生成 28 种翻译。
- **1.8** `--news` 模式 + 2026 年模型升级（2026-03-17，标签 `v1.8`）：
  - 默认模型已更新（2026 年 3 月）：
    - OpenAI 高质量：`gpt-5` → `gpt-5.4`
    - OpenAI 经济型：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 高质量：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - 为 `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）和 `gemini-3.1-pro-preview`（1M）添加 token 限制。
  - 初始 `--news` 模式：使用占位符 `#NEWSQUOTE\d+#` 保护英文引用，提供 `LANG_FLAGS` 映射（15 种语言），并处理目标语言标志。
  - 恢复前验证 news 占位符（回归问题：LLM 删除占位符会静默地产生没有引用的输出）。
  - 使脚本 `regen_translations.sh` 具备可移植性（绝对路径，不依赖 pwd）。
  - 在 README/CHANGELOG 的语言栏中添加法语链接，重新生成 28 种翻译。
- **1.7** 新功能：
  - 添加选项 `--keep_filename`，在翻译时保留原始文件名。
  - 支持文件 `.env`，自动加载 API key。
  - **保留行内代码**：反引号（`` `...` ``）现在会在翻译期间受到保护。
  - 改进系统 prompt：
    - 更好地处理 YAML frontmatter 中的引号。
    - 保护模板变量 `{variable}`。
    - 禁止未请求的译者注释。
  - 在 blog jls42.org 迁移中成功测试 364 个文件。
- **1.6** 新功能：
  - 支持 Google Gemini API 进行翻译（`--use_gemini`）。
  - 更新 2026 年默认模型：
    - OpenAI：`gpt-5`（高质量）、`gpt-5-mini`（经济型）
    - Claude：`claude-sonnet-4-5`（高质量）、`claude-haiku-4-5`（经济型）
    - Gemini：`gemini-3-pro-preview`（高质量）、`gemini-3-flash-preview`（经济型）
  - 经济模式（`--eco`），用于使用更快速、成本更低的模型。
  - 单文件翻译（`--file`），无需遍历目录。
  - 新的简化命名模式：`{base}-{lang}.md`。
  - 添加选项 `--include_model`，以保留包含模型名称的旧格式。
  - 支持未列出的模型，并默认使用 token 限制（128k）。
  - README 翻译成 14 种语言。
- **1.5** 改进：
  - **API key 和默认模型更新：**
    - **OpenAI：** 从 `DEFAULT_MODEL_OPENAI` 更新至 `"gpt-4o"`。
    - **Mistral AI：** 从 `DEFAULT_MODEL_MISTRAL` 更新至 `"mistral-large-latest"`。
    - **Anthropic Claude：** 添加 `DEFAULT_ANTHROPIC_API_KEY`，并将 `DEFAULT_MODEL_CLAUDE` 更新至 `"claude-3-5-sonnet-20240620"`。
  - **翻译 prompt 优化：**
    - 直接翻译和翻译说明所使用的 prompt 得到增强，以提升清晰度和效率，其中包括关于保留元数据及特定格式元素的详细指令。
  - **代码重构：**
    - 用类 `Mistral` 替换 `MistralClient`，用于初始化 Mistral AI 客户端。
    - 重新组织导入，以提升可读性和可维护性。
    - 改进文本分段和代码块处理，在翻译期间保留原始格式。
  - **输出文件管理：**
    - 调换输出文件名中的模型和语言顺序（例如 `f"{base}-{args.target_lang}-{args.model}.md"`），便于组织和查找翻译。
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
  - 添加选项 `--force` 以强制翻译。
  - 调换输出文件名中的模型和语言顺序。
- **1.2** 修复变更日志。
- **1.1** 添加 Mistral AI API 支持。
- **1.0** 初始版本——支持 OpenAI API。

**使用 gpt-5.6-luna 将文章从法语翻译成中文。**
