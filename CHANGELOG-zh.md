### 更新日志

🌍 [法语](CHANGELOG.md) | [英语](CHANGELOG-en.md) | [西班牙语](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [德语](CHANGELOG-de.md) | [日语](CHANGELOG-ja.md) | [韩语](CHANGELOG-ko.md) | [阿拉伯语](CHANGELOG-ar.md) | [印地语](CHANGELOG-hi.md) | [意大利语](CHANGELOG-it.md) | [荷兰语](CHANGELOG-nl.md) | [波兰语](CHANGELOG-pl.md) | [葡萄牙语](CHANGELOG-pt.md) | [罗马尼亚语](CHANGELOG-ro.md) | [瑞典语](CHANGELOG-sv.md)

- **1.14.0** README 顶部新增兼容性表格，以及作为其依据的测量活动（2026-09-09）：

  - **README 顶部以法语给出各模型的结论。** 三百多份翻译原本埋在文档中部，分散在三个必须交叉阅读的表格中。新表格为每个模型用一行给出结论，尤其明确指出差异所在：例如“阿拉伯语和日语中各漏掉一个粗体词”，而不是一个比率。比较器在两个内容密集的文档中未检测到三个模型存在任何差异——通过 ChatGPT 订阅使用的 `gemini-3.7-flash`、`gpt-5.6-sol`，以及通过 OpenRouter 使用的 `z-ai/glm-5.2`。
  - **重新测量了 176 份翻译。** 原始测量日期为 9 月 4 日，针对的是此后已发生大量变化的 README。八个模型在当前 README 上重新测量，两个模型以 `--news` 模式在一篇博客监测文章上重新测量，一个模型则在四个公开 README 上测量——FastAPI、Ollama、tldr-pages 和 Vue.js。有三个结果值得记录：Mistral 在阿拉伯语、印地语和韩语中丢失了**整个章节标题**，而 pipeline 的任何 guard 都没有发现——标题无法替换为 token，目前翻译期间也没有任何机制检查它，尽管比较器事后能够检测到；Grok 在一篇监测文章的五种语言上失败，第一个 segment 就丢失了四处 inline code 和三个 URL，而处理 README 时却能正常完成；Gemini 在四个公开 README 的 56 份翻译中，有 55 份未出现差异。
  - **结构比较器加入仓库。** README 将该协议描述为评判模型的正确方式——“比较章节、链接、不同 URL、代码块的数量”——却没有提供工具。`scripts/compare_structure.py` 正是生成这些表格的工具，并有十一个测试证明它能检测 URL、代码块、章节、inline code、表格行和引用的丢失。它包含两项使非拉丁文字检查变得可靠的修正：后接全角右括号的 URL 不再被视为不同 URL，较短的中文引用也不再被视为引用丢失。
  - **发布前后均检查软件包。** 测试套件在源代码上运行并保持通过，但发布的软件包仍可能损坏——例如 setuptools 配置中漏掉一个模块，导致 entry point 无法解析。`scripts/check-package-smoke.sh --wheel` 构建 wheel，将其安装到仓库外的一次性 venv，检查其中是否仅包含该软件包、两种执行形式是否都能响应、所有模块是否均可导入，随后翻译一个真实文档并比较其结构。`--pypi` 从 index 执行相同检查：只有这种验证能够证明发布出去的确实是这些字节，而 PyPI 永远不允许重新发布同一版本。`--full` gate 执行其中的离线部分，不调用模型，也不产生费用。
  - **修正了 README 中的七项陈述，每项都在改写前完成复现。** “不会有任何错误内容写入磁盘”这一说法并不属实：模型若删除章节或修改 front matter 日期，pipeline 仍会返回状态 `success` 并写入文件，这已通过模拟响应复现。README 现在会说明 token 保护的内容——代码块、inline code、URL、锚点、引用——以及 pipeline guard 当前未检查的内容。“无差异”并不意味着“完全相同”：比较器只统计元素而不读取其内容，既不会报告四级标题被删除，也不会报告 inline code 文本被替换，亦不会报告 flag 被调换——这三种情况均已实测；由于比较器根本没有 flag 计数器，“相同 flag”的表述已被移除。贡献者安装流程无法生成可用工具：`pip install -r requirements.txt` 仅安装依赖项，`python -m aipmt` 会返回 `No module named aipmt`，并且缺少 `pip install -e .`——`pre-commit` 的安装行也同样缺失，而它不在两个依赖文件中的任何一个里。关于 OpenRouter 小 context 的承诺与代码行为恰好相反：context window 低于 **16 400 tokens** 的模型会在任何调用发生前被拒绝，这一点已分别在 4 095、8 192 和 16 384 上测得。用于防止项目中的 `.env` 重定向 API 调用的过滤器此前从未记录在文档中；现在已经补充说明，并列出涉及的变量。最后还有两处数字：顶部表格中 Grok 的一个单元格来自 9 月 9 日的测量活动，但其所在列标注的是 9 月 4 日；归因于 Gemini 的“一处链接损坏”也与测量结果相反——它把三个裸 URL 转换成链接，并未丢失任何 URL。

  - **写入失败不再在磁盘上留下截断的翻译。** `open(cible, "w")` 会先截断文件再填充内容：写入过程中若发生错误——例如磁盘已满——便会留下不完整的目标文件。复现结果如下：写入八个字节，返回状态 `failure`，随后再次运行时发现该文件，返回 `skipped` 并保留它。一次失败就这样变成了不再有任何机制报告的截断翻译，而退出码仍为 0。现在，内容会先写入同一目录中的临时文件——`os.replace` 只有在同一文件系统内才具备原子性——随后再重命名；如果写入失败，包括遭到中断时，临时文件都会被删除。该临时文件由 `mkstemp` 创建；review 表明，可预测的文件名只会转移问题：若在 `cible.md.aipmt-tmp` 预先放置 symbolic link，翻译内容就会被写入它指向的文件、越过输出目录，同时仍返回 `success`；若两个进程同时处理同一目标，它们会共用该名称，第二个进程会在第一个仍向同一 inode 写入时执行重命名——目标被报告为成功，内容却相互混合（实测为 `BBBAAAAA`，而非 `BBBBBBBB`）。`mkstemp` 以唯一名称在 `O_CREAT | O_EXCL` 中创建文件，从而解决这两个问题。替换前会明确继承现有目标文件的权限：`mkstemp` 创建的文件权限为 0600；否则，刻意设为 0600 的目标会变成 0664，而由 Web server 提供、权限为 0644 的目标则会变得不可读。八个测试锁定了整套行为，对代码进行两种 mutation 都会使测试失败。

  - **纯净度 manifest 可以声明经过改写的 suppression marker。** 检查要求参考版本中每一行包含的 `# nosec`、`# nosemgrep` 或 `NOSONAR` 都必须逐字保留。然而，将写入操作移至临时文件会改变已打开变量的名称：Sonar suppression 仍然相同，但所在行发生了变化。manifest 的 `markers` 类别会声明 `old` → `new` 这一对应关系及其原因。它有两个条件，其中第二个来自一次 review：替代行必须存在，**并且必须包含与原始行相同的 suppression**。如果没有此条件，声明 `value = 1  # NOSONAR` → `value = 1` 也能通过，因此仅凭一项声明便足以移除 marker——而该检查的目的恰恰是防止这种情况。未声明的消失仍会被拒绝。

  - **两次测量活动因模型之外的原因中断，因此从表格中移除。** Grok 在处理此 README 的十二种语言后丢失了 CLI session——其中两种语言在四秒内被拒绝，并未调用模型——而 `qwen3.8-flash` 在完成两种语言后遭到其上游托管方的 HTTP 429 限流。中断的测量活动不应评分：它们要么完整重做，要么完全不做。同时，“本项目 README”表格中的耗时已根据 9 月 9 日的测量活动重新校准——原数据来自一个 508 行的 revision，而本次实测版本有 785 行；`gpt-5.6-sol` 原标注为 2 分 04 秒，实际测量结果为 6 分 46 秒。

  - **README 已重新编排：从 1 007 行缩减至 600 行，并按读者的阅读顺序组织。** 内容依次为工具的作用、安装、配置、入门，然后是兼容性表格——放在安装之后，此时读者已知道自己要运行什么——再到选项、每个 provider 各自的章节、详细测量数据，最后是如何贡献。测量活动的叙述、测量过程中的轶事以及章节间的重复内容均已删除；保留的每个数字都与表格一致，每项行为说明也都与当前版本的代码相符。此次改版的过程记录仍保留在 git 历史中。

  - **顶部表格现在会说明每项差异涉及多少种语言。** 此前表格先写“✅ 14 种语言”，相邻列却写“一个粗体词”——没有说明这适用于一种语言还是全部十四种。读者无法判断，而且在测量结果本来良好的地方造成了不佳印象：在此 README 上，Gemini 的十四种语言中只有一种多出一个粗体词，Sol 有两种，GLM 有三种。现在，每个单元格都会标明涉及的语言数量及具体语言；结论列中的数字也用一句话明确定义——在十四种语言中，成功写出翻译且没有任何差异的语言数量——并通过图例说明三个符号的含义。分类方式由项目所有者决定：✅ 没有任何差异；⚠️ 全部内容均已翻译，仅 markup 发生变化，没有内容缺失；❌ 至少一种语言遭到拒绝，或已写入的文件中缺少内容。

  - **文章的整个测量活动已使用当前比较器重新计算。** 有两个数字是在比较器修正非拉丁文字处理之前发布的，因此被计入了并不存在的差异：`qwen3.8-flash` 从十三种无差异语言变为十四种，`qwen3.7-flash` 从七种变为八种。关于 `gpt-oss` 的段落也同时得到修正：其中残留法语的片段从未进入交付文件，未翻译片段 guard 拒绝了涉及的四种语言——这是“模型被我们拦下”与“模型从检查中漏过”的区别，README 现在明确指出了这一点。

  - **README 末尾新增免责声明。** GPL v3 的第 15 和第 16 节已经排除所有担保，但没有人会在安装工具前先阅读许可证。因此，现在明确说明四点：自动翻译在发布前必须人工校对，因为 guard 既不覆盖标题、表格和 front matter，也不验证语义；翻译的文档会发送给所选 provider，并受其自身条款约束，部分免费模型可能复用交互内容——只有本地模型能确保数据不外流；API 调用会产生费用，程序不会设置支出上限；发布的测量结果是特定日期的观察记录，而不是保证。

  - **整个 `gpt-5.6-*` 系列都可通过 ChatGPT 订阅使用**，已完成实测：`--model gpt-5.6-terra` 通过 Codex 提供的模型与 API 默认提供的模型相同。默认模型仍为 `gpt-5.6-sol`，它是唯一在内容密集文档的十四种语言上均未测得内容丢失的模型，本仓库也由它翻译。

- **1.13.1** 依赖项新鲜度：滞后不再只是一个可能被忽略的警告（2026-09-09）：

  - **未被计数的警告就是容易错过的警告。** `check-deps-fresh.sh` 已连续数日提示 `openai` 和 `anthropic` 出现滞后，但 gate 的汇总行只统计失败：即使上方几行已经写明存在滞后，最后仍显示“就绪：N 项检查通过”。只阅读最后一行的人——而所有人通常都会这么做——无从知晓这一情况。现在，结论会包含警告数量，并由专用计数器统一统计，不再在执行过程中零散打印。
  - **滞后提示会附带 release notes。** 版本号本身无法说明变更内容，而要求使用者自己找到正确文件，正是导致该步骤被跳过的摩擦。检查现在会显示每个滞后软件包的 CHANGELOG 地址，无论 major 还是 minor 版本均如此，并解释原因：某个 SDK 的 minor 版本此前已经修改过本项目依赖的内容。
  - **`openai` 3.8.0 → 3.10.0，`anthropic` 1.3.0 → 1.4.0；固定版本前已阅读 release notes。** OpenAI 方面，该版本区间内只有一项行为变化——当数字形式的 `Retry-After` header 超出 floating-point 范围时，不再退回到较短的 backoff，而是直接返回原始错误且不重试——本项目依赖的行为均未改变：模型对额外字段的容忍性没有变化，这一点已在两个 tag 的代码中验证，因此 OpenRouter 添加到 choice 中的 `native_finish_reason` 和 `error` 仍可正常通过。Anthropic 方面，新增 guard 会在 SDK 期望 `httpx2` 时，对来自 `httpx` 软件包的对象明确抛出 `TypeError`；经检查，本项目仅传递 floating-point。两版之间，拒绝持续超过十分钟的非 streaming 调用这一规则逐字节完全相同：真正使其豁免的是显式的 `timeout`，其 32 768 tokens 超过了 21 333 的阈值。
  - **已验证**：在升级后的版本上运行 502 + 31 项测试套件；`requirements.txt` 的 closure 与已安装内容一致（41 个 pin）；并通过 SDK 分别对 OpenAI 和 Claude 进行一次真实调用，在 `--news` 模式下处理文档，所得结构与源文档相同。

- **1.13.0** Provider `--use_openrouter`：通往约 430 个模型的付费 router，其中包括中国开源模型（2026-09-05）：

  - **第九条 provider 路径与第八条一同发布。** 1.12.0 未发布至 PyPI：OpenCode 与 OpenRouter 两个 router 同时推出。[OpenRouter](https://openrouter.ai) 只需一个 key，即可访问其他 provider 在此均未提供的模型——Kimi、Qwen、DeepSeek、Z.ai——费用从统一 credit 中按使用量扣除。由于 endpoint 与 OpenAI 兼容，所用 client 与 xAI 相同；**这个 provider 的全部差异都集中在一个 preflight 中**，其中每条规则都来自 API 实测。

  - **同一模型由数十个具有不同上限的托管方提供，而 routing 对此毫无感知。** 实测：`z-ai/glm-5.2` 有 33 个托管方，`z-ai/glm-5.3-flash` 有 23 个——其中一个的**输出上限仅为 2 048 tokens**。因此，长篇翻译可能随机落到这 23 个托管方中的某一个并被截断，却没有任何提示。preflight 会读取 `/api/v1/models/{modèle}/endpoints`，排除输出上限低于 8 000 tokens、状态 degraded 或未声明任何上限的托管方，然后 pin 其余托管方。`provider.only` 如果**没有** `allow_fallbacks: false`，就只是一项 preference：router 仍会转向已排除的托管方，使 pin 完全失去意义。如果没有任何托管方满足上限要求，命令就会停止：继续翻译等同于接受该 preflight 正是为了避免的静默截断。

  - **reasoning 按输出费率计费，并且在许多模型上默认启用。** 对 `z-ai/glm-5.2` 发送相同请求并得到“OK”响应：**采用模型默认设置时使用 107 个 completion tokens，关闭 reasoning 后仅使用 2 个**。对于 reasoning 毫无帮助的翻译任务，这会使每个文件的每个 segment 成本增加至 18 倍。因此默认关闭 reasoning。**431 个模型中有 288 个**强制启用 reasoning（`reasoning.mandatory`），它们会返回 `400 « Reasoning is mandatory for this endpoint and cannot be disabled »`：对于这些模型，preflight 会读取可接受的 effort，并请求最低值（见下一条）——effort 会分配 `max_tokens` 的一个**百分比**，由 reasoning 优先消耗，因此随意选择数值只会转移出现空白页面的风险，而不会降低风险。
  - **强制推理的模型会采用其所接受的最低推理强度，而这是由测量结果决定的。** 最初的选择是什么都不发送，以免替模型作出猜测。在 `z-ai/glm-5.3-flash` 上测试后发现，其目录默认值为 `max`，这种选择会导致输出在翻译完成前被**截断于 32,768 tokens**——十四种语言中有两种丢失。提高上限也不会改变结果：推理强度会从中分配一定比例，推理量也会随之增长。因此，provider 会在预检阶段读取 `supported_efforts` 并请求最低值；如果目录未公布任何可用值，则回退为“无”。对出错语言的反向验证表明：它之前因预算耗尽而失败，现在可在 9 分钟内完成，且结构与源文件完全一致。

  - **上游托管服务故障现在有了明确名称。** 路由器将此情况规范化为 `finish_reason=error`，同时将 `native_finish_reason` 置空——在两种语言上分别测量两次，均恰好为 750 秒。原先的通用消息会让人去文档或分段中查找问题；现在则明确指出故障位于供应商一侧，并说明重试通常即可解决。

  - **`finish_reason=length` 且输出为空并非截断。** 这是推理在生成第一个有效字符前耗尽了预算——测得推理使用了 15,850 tokens，而有效输出仅为 148 tokens。这两种情况需要采取相反措施：在第一种情况下，缩小分段大小毫无作用。消息现在会明确区分二者。另有两项防护来自实测：上游托管服务失败时，路由器会返回**状态码 200，但响应体仅包含错误**（`choices[0]` 曾抛出不透明的 `TypeError`，遮蔽了原始消息）；上下文窗口会从目录读取并写入 `MODEL_TOKEN_LIMITS`——`DEFAULT_TOKEN_LIMIT` 对目录中的 44 个模型而言是错误的，其中两个模型的上限仅为 4,095 tokens。

  - **`--model fournisseur/modèle` 为必填项，并且其格式会在任何网络请求前完成验证。** OpenRouter 不是供应商：该选择涉及价格、许可和数据处理方式，不能代替用户作出。由于 slug 会被插入预检 URL，验证并非出于易用性考虑，而是防止路径注入的防护措施：两个路由器共用的带命名空间正则表达式接受 `a/b/..`，因此必须明确拒绝父目录段。`--eco` 不生效，并会明确说明这一点。

  - **修正了三处表述，其中一处原本存在事实错误。** OpenAI 对 `codex exec` 的警告针对的是在共享 runner 上注入个人会话文件，而不是仓库是否公开：README、CLAUDE.md 和代码此前都对其作了错误引用。OpenCode 的身份验证位置在 1.18.27 中发生了变化（位于 `opencode.db` 的 `credential` 表中，而不再是 `auth.json`）；“此处从不读取”的不变量仍然成立，但地址已过时。最后，OpenCode 章节不再把从未验证过的途径描述为等价选项：Zen 网关和 Ollama 已完成端到端测量，而 GitHub Copilot、LM Studio 和 llama.cpp 尚未验证，README 现在会如实说明。

  - **开展了一轮测量，并在 README 中加入推荐模型表格。** 针对三组文档执行了三百多次翻译——一篇采用 `--news` 模式、内容密集的博客文章，这份使用标准 Markdown 的 README，以及四份从 GitHub 原样取得的知名项目 README——目标涵盖十四种语言。表格区分了此前混为一谈的两件事：能够**完成**的翻译，以及**结构与源文件完全一致**的翻译。在两份密集文档上，有三个模型从未丢失任何信息：`gemini-3.7-flash`、通过 ChatGPT 订阅使用的 `gpt-5.6-sol`，以及通过 OpenRouter 使用的 `z-ai/glm-5.2`——它们仅有的差异，是一两种语言中有一对 `**` 未被保留。核心结论是：**决定性因素是文档密度，而不是 `--news` 模式**：通过订阅使用的 Grok 在博客文章上十四次中失败十三次，但在十六份公共 README 中成功十四次；反向验证确认，原因是处理长分段时发生脱离。表格自带警告：结果并不详尽，具有时效性，耗时不能用于排名，正确做法仍是在自己的文档上进行测量。

  - **结构比较器在发布数据前得到修正，因为它对非拉丁文字产生了两类误报。** URL 后跟全角右括号 `）` 时，原正则表达式只在 `)` 处停止，无法正确截断，因此即使 URL 相同，提取出的字符串也会不同；法语中占五行的引用在中文中只占三行，也会导致逐行计数下降。两项修正均通过反向验证：删除 URL、章节或行内代码仍会被检测到。如果没有这些修正，Gemini 和 Codex 公布的结果将分别是十四种语言中仅十一种和十二种通过，而不是十三种和十二种。

  - **测试**：新增文件 `tests/test_openrouter_provider.py`（76 项测试）——模型验证与父目录段拒绝、托管服务筛选（上限、状态、未声明上限、共同最低值）、`allow_fallbacks` 始终为假、根据 `mandatory` 截断或保留推理、完整输出契约（200 响应中的错误、无选项、区分空白页面与截断、异常的 `finish_reason`、空内容）、目录无法访问时预检以失败关闭、缺少 slug 以及没有健康托管服务、标志互斥性与文件名标签。完整测试套件达到 **502 项测试**。

  - **重构：将 4,253 行的单一模块拆分为多个模块，不改变任何一行行为。** `src/aipmt/translate.py` 被拆分为 `config`、`markdown`、`segmentation`、`guards`、`placeholders`、`news`、`prompts`、`notes`、`naming`、`pipeline`、`cli`，以及子包 `providers/`（每个 provider 一个模块，以 `base` 为基础层，由 `registry` 负责解析与分派）。每次移动都对应一个提交，并由机械化验证提供证据：验证器将包中所有顶层节点的 AST 与参考快照进行比较，检查每个符号的位置、安全标记是否逐字保留，以及是否不存在未跟踪文件——该临时工具已在下一版本中移除。可见变化包括：`aipmt.translate` 成为门面，并以对象身份不变的方式重新暴露原模块中无需 `_` 前缀即可访问的 64 个名称（其中 `__all__` 包含九个，即受支持的 API；其余为兼容别名），且不再重新导出由 `import *` 收集的 29 个依赖项和标准库名称；不再支持直接执行该文件（`python src/aipmt/translate.py`）——`aipmt` 和 `python -m aipmt` 仍是两种受支持形式；公共函数的 `__module__` 现在指向其定义模块；SDK 改为在加载 `.env` 后导入，而不再提前导入，目前未发现影响。427 项测试的标识符均保持不变，并迁移至其实际测试的模块：91 个原先通过门面进行的 patch 现在直接指向读取相应名称的模块（实测其中两个即使不 patch 也仍会通过）；七项契约测试锁定门面行为；gate 工具在首次移动前就已重写，确保任何检查都不会因停止验证而错误转绿——Lizard 范围改为带下限的目录、从已构建的 parser 读取标志、按包设置覆盖率下限，并由 `release.sh` 枚举受跟踪模块。
  - **修复（pull request 审查）**：OpenRouter 现在会拒绝缺少 `context_length` 的目录条目，不再把默认的 128,000 tokens 记录为测量值——此前这也会让“模型未列出”警告失效；当 `finish_reason` 为空时（记录于 `string | null` 的类型），以托管服务的原始原因作为依据，`max_tokens` 的值为 `length`；如果错误由选项本身携带，则拒绝随附的部分内容，并使用与规范化上游故障相同的消息——其中同时包含托管服务详情、原始原因和建议。遇到 `part: null` 事件时，OpenCode 会返回其契约错误，而不是 `AttributeError`；对于某一事件行无法解析的 JSONL 流，也会拒绝整个响应，而不是接受部分文本。三个 agentic CLI 在调用期间收到 `SIGTERM` 时，都会终止 agent 所在的进程组——regen 的 `timeout` 曾让 agent 继续存活并消耗配额——而进程组的 `SIGKILL` 始终遵循宽限期，即使 shim 正常退出，其子孙进程仍会存活。拆分过程中被分开的 `# fmt: off` / `# fmt: on` 对已重新合并；`--reasoning_effort` 的帮助文本会列出使用它的四个 provider。
  - **修复（第二次复审）**：向 OpenRouter 请求的输出上限现在会为 prompt 和分段占用的上下文预留空间——`context_length` 同时覆盖输入和补全，而目录中的六个模型此前会在完全没有输入空间的情况下发出请求；上下文过短时会在产生任何费用前拒绝请求。在不支持 POSIX 进程组的环境中，agentic CLI 基础层会依次回退到 `terminate` 和 `kill`，避免 `AttributeError` 穿过超时防护并导致等待持续下去。OpenCode 的 `429` 标记现在按数值查找，而不再按子字符串匹配；此前像 `err_84290b` 这样的错误标识符会触发 90 秒退避，最终仍然失败。最后，预检阶段会显示非规范的 OpenRouter endpoint：项目中的一个 `.env` 即可设置它，而后续实际发送的正是真实密钥。
  - **安全性：项目级 `.env` 不再能够重定向 API 调用。** `find_dotenv(usecwd=True)` 会从当前目录及其父目录查找文件：不可信目录树——例如刚克隆的仓库——可以在不知道任何密钥的情况下放置 `OPENROUTER_BASE_URL`、`XAI_BASE_URL` 或 `OPENAI_BASE_URL`（后者由 SDK 自行读取），随后来自环境变量或用户配置的真实密钥就会被发送到第三方服务器的授权标头中。过滤基于模式而非列表：对已安装 SDK 的盘点发现，它们会读取十二个路由变量，其中仅 Anthropic 客户端就读取六个——手工枚举会漏掉一半。因此，项目层会拒绝所有属于 `_BASE_URL`、`_API_BASE` 或 `_ENDPOINT` 的变量，以及代理和证书存储变量（指向受控证书颁发机构，会使拦截者与真实服务器无法区分），同时还会拒绝 `XDG_CONFIG_HOME` 和 `APPDATA`：设置它们相当于决定哪个文件构成用户层，从而绕过过滤。这些变量仅允许来自用户可控的两个层级：已导出的环境变量和 `~/.config/aipmt/.env`。此外，读取项目层时不会进行插值：`load_dotenv` 默认会展开 `${VAR}`，而一个包含 `NOM_ANODIN=${OPENAI_API_KEY}` 的不可信 `.env` 会把真实密钥复制到一个子进程模式过滤无法识别的名称下——随后它便会进入 `codex exec` 的环境，违背已声明的不变量。最后，拒绝消息只显示变量名：形如 `https://${CLE}@hôte/` 的 URL 会让插值后的密钥泄漏到日志中，即使该变量本身已被拒绝。拒绝信息会写入 stderr，并附带操作指引——企业中继应在用户配置中声明。
  - **修复：OpenRouter 的输出预算现在按每次调用计算。** `context_length` 同时覆盖输入和补全，而针对拉丁文本校准的固定预留量无法提供可靠上限：使用 `o200k_base` tokenizer 测量，16,000 个字符在法语中相当于 3,200 tokens，在日语中为 12,300 tokens，在 emoji 中则为 17,500 tokens。因此，预算会根据实际发送的文本计算，并以其 UTF-8 字节数作为上界：对于所有采用字节融合的 tokenizer——字节级 BPE、带字节回退的 SentencePiece，也就是目录中使用的各类 tokenizer——一个 token 至少对应一个字节；而在这里，OpenRouter 会路由到数十种未知 tokenizer，这是唯一可用的上界。任何平均比例都不适用——补充平面中的一个表意文字可降至每 token 1.33 字节，而组合字符可降至 1.00 字节——现在输入与输出在构造上就能保证共同落入上下文窗口。若分段对所选模型而言过于密集，请求会在调用前而非计费后被拒绝。

- **1.12.0** Provider `--use_opencode`：OpenCode——通过这个开源 agent 连接用户选择的供应商，可使用本地模型、无需账户的免费模型、订阅或密钥（2026-09-04）：

  - **第八条 provider 路径，其性质不同于前七条。** [OpenCode](https://opencode.ai)（MIT）不是模型供应商，而是通往用户已在 OpenCode 中配置的模型的_路由器_：API 密钥、订阅（GitHub Copilot、ChatGPT、SuperGrok）、OpenCode Zen 网关——提供**无需账户**的免费模型——或**本地**模型（Ollama、LM Studio、llama.cpp）。脚本以非交互模式驱动 `opencode run`，方式与驱动 Codex 和 Grok 相同，并复用同一套子进程基础设施（独立进程组、超时时先执行 `SIGTERM` 再执行 `SIGKILL`、始终关闭 stdin、清理环境变量）。已通过**两次真实翻译**验证：使用 `opencode/mimo-v2.5-free` 将整份 README 翻译为英文——耗时 49 秒，仅一次处理，结构与源文件完全一致（32 个标题、26 个代码块结束标记、18 个链接、37 个 URL、37 行表格、135 处行内代码）——以及通过本地 `ollama/qwen2.5:7b` 翻译一个测试文件，全程无需任何密钥。

  - **`--model provider/modèle` 为必填项，而且这是一个需要用户作出的选择。** 如果没有 `--model`，OpenCode 会回退到自身默认值；在全新安装中，该默认值是 `opencode/big-pickle`，这是一个免费的“stealth”模型，其交互内容可能被用于训练——实测响应的正是该模型。替用户静默选择它，恰恰属于本仓库要追踪的不可见切换；因此错误消息会列出用于查看模型的命令（`opencode models`），以及三个示例（本地、免费、订阅）。`--eco` 不生效，并会明确说明这一点。只有在用户明确要求时，`--reasoning_effort` 才会原样作为 OpenCode 的 `--variant` 传递。

  - **隔离以测量为依据，而非凭空假定。** 内联配置（`OPENCODE_CONFIG_CONTENT`，在 OpenCode 合并顺序中位于最后，因此优先于用户配置但不会替换它）定义了一个名为 `aipmt` 的 agent，并拒绝所有工具（`permission: {"*": "deny"}`）：注册表甚至不会再把工具提供给模型；当要求模型“列出文件并运行 `id`”时，它会回答自己没有工具。会话共享已禁用，外部插件已排除（`--pure`），绝不使用 `--auto`，工作目录为一次性空目录。实测发现并切断了两种静默注入：没有 `OPENCODE_DISABLE_CLAUDE_CODE` 时，用户的 `~/.claude/CLAUDE.md` 会进入**每个** prompt（仅一句“你好”的输入就从 186 tokens 增至 515 tokens）；没有 `OPENCODE_DISABLE_PROJECT_CONFIG` 时，当前目录中的 `AGENTS.md` 也会被注入——其中一条“每个回答都以 BANANA 结尾”的指令确实影响了翻译。全局 `~/.config/opencode/AGENTS.md` 仍会注入：没有开关可以排除它，而借助被挪作他用的 `XDG_CONFIG_HOME` 绕过它，也会同时隐藏用户的供应商配置。因此选择如实记录，而不是勉强拼凑。
  - **`exit 0` 什么也证明不了：第三个 CLI，同样的反应方式——但它有两个特有的陷阱。** 未知的 `--agent` 不会导致 `opencode run` 失败：stderr 会发出警告，并**静默**回退到启用了工具的编码 agent。因此，如果内联配置未生效，翻译就会由能够写入的 agent 执行；除以下条件外，输出契约还会验证不存在该消息：返回码为 0、没有 `error` 事件、没有 `tool_use`、最后一个 `step_finish` 位于 `stop` 中（`length` 表示响应被截断）、文本非空。第二个陷阱：错误 JSON 事件是**不透明的**——“意外的服务器错误。请查看服务器日志了解详情。”，只附带一个简单引用——而真正的原因（`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`、`ProviderAuthError`……）仅存在于日志中。因此需要 `--print-logs --log-level ERROR`，并读取 stderr 的 `error="…"` 字段，同时忽略其后的 Bun 堆栈。这样，未知模型会在一秒内失败，并明确指出原因。顺便一提，`--title` 可避免一次无关的 LLM 调用：若没有它，OpenCode 会通过在 `small_model` 上额外执行一轮来生成会话标题。

  - **Secrets：采用与 Codex 和 Grok 相同的模式过滤，只有一个明确命名的例外。** `OPENCODE_API_KEY` 会被保留：这是 OpenCode 自身的密钥（Zen 网关、Go 订阅），按名称传递给它——相当于它的 `auth.json`，而不是 aipmt 会管理或能够计费的密钥。provider 在 OpenCode 中配置（`opencode auth login`、`opencode.json`），绝不在 aipmt 的 `.env` 中配置；aipmt 的任何密钥都不会传入子进程。与订阅型 CLI 不同，CI 中不会拒绝此类配置：在 runner 上使用 API 密钥或自托管模型都是合理用法。

  - **防路径穿越保护现在检查插值后的值，而不是原始值。** `provider/modèle` 包含一个会被 1.10.0 版保护机制拒绝的 `/`——这是有道理的，因为 `--model` 会被插入文件名 `--include_model`。文件名标签现在会在任何插值发生前，将 `/`、`\` 和 `:` 替换为 `-`（`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`，因为 `:` 在 Windows 下非法），而上游保护机制会检查这个标签：`../../evil` 会成为目标目录下的普通名称 `doc-en-..-..-evil.md`，只有 `..` 仍会被拒绝，`--target_lang ../x` 也会被拒绝。范围保护 `_ensure_within_directory` 仍作为未变的第二层防护。

  - **免费模型和本地模型：实际测量结果。** `opencode/mimo-v2.5-free` 翻译一个段落需 16 秒，翻译此 README 需 49 秒；`opencode/big-pickle` 翻译 200 个词需 40 秒，两项并发请求持续 5 分钟都没有响应，而单独执行时各自都能完成；`opencode/nemotron-3.5-lightning-free` 在 3 分钟内没有任何响应。因此采用 `REGEN_PROVIDER=opencode`，必须搭配 `REGEN_MODEL`，并行运行 **2 个 job**。本地方面，Ollama 通常配置 4,096 个上下文 token，而分段最多可达 16,000 个字符：必须使用带 `PARAMETER num_ctx 32768` 的 `Modelfile`；质量则取决于模型——在测试文件中，7B 模型颠倒了一个列表并破坏了代码块的结束围栏，而网关模型完整保留了一切。

  - **此仓库的翻译不再通过任何收费 API。** 只要 `.env` 中存在密钥，`regen_translations.sh` 就会使用 OpenAI API，而 Codex 仅作为主动选择项。准备此版本时发生的情况正是如此：28 份翻译使用了 OpenAI API，随后印地语 CHANGELOG 又使用了 Gemini API，尽管 ChatGPT 订阅存在的目的正是避免按量付费。密钥自动检测现已移除：**默认使用 Codex，并搭配 `gpt-5.6-sol`**，即高质量模型；`openai`、`gemini` 和 `grok` 除 `REGEN_PROVIDER` 外还要求提供 `REGEN_ALLOW_PAID_API=1`，这是一个明确命名的豁免，以便规则在作出决定时生效；未知的 `REGEN_PROVIDER` 会直接失败，而不会回退到 API。十项测试锁定了默认行为、拒绝逻辑和豁免机制。此版本的 28 份翻译均已通过 Codex 重新生成。

  - **rate limit 的 back-off 逻辑已统一提取**（`_retry_on_rate_limit`）：Codex 与 Grok 的循环除了标签外完全相同，再复制第三份就会超过重复阈值。三个 CLI 错误都派生自同一个 `_CliCallError`；一项测试禁止其中任何一个脱离该继承关系，否则共享循环将无法再捕获它。

  - **测试**：新增文件 `tests/test_opencode_provider.py`（61 项测试）——完整输出契约、agent 回退、从日志读取原因、文本分片去重并忽略合成分片、timeout 终止进程组、429 back-off、模型必填及验证、无 secret 的 preflight、二进制解析、dispatch 接线、文件名标签和路径穿越反向验证。`tests/test_review_hardening.py` 将 flag 互斥性和无 secret 要求扩展到新 provider。gate 现在要求记录全部 **22 个 argparse flag**。完整测试套件共 **382 项测试**。

- **1.11.1** 文档修正：README 终于列出了全部七条 provider 路径（2026-09-03）：

  - **1.11.0 的 PyPI 页面写的是“4 个 API + Codex CLI”。** 实际代码公开了七种方式——通过 API 使用 OpenAI、Mistral、Claude、Gemini 和 Grok；以及通过订阅使用 Codex（ChatGPT）和 Grok，不按用量计费。简介和 _多 Provider_ 条目中都遗漏了两种 Grok 模式，14 份翻译也重复了这一错误。由于包的长描述在每个版本发布后便固定不变，修正展示页面必须发布新版本号：这就是此版本存在的唯一原因。**没有代码变更。**
  - `CLAUDE.md` 已与此次发布引入的内容保持一致：gate 计数器（16，`--full` 中为 17）、十一个启用的 workflow、`gh pr checks` 中不可见的两个 Sonar/Codacy 计数器（hotspots、Codacy API）、由 `ruff-format` 导致的一个 `# nosemgrep` 迁移、OIDC 交换所要求的 GitHub environment，以及 _待处理 publisher_ 不会保留名称这一事实。

- **1.11.0** 发布到 PyPI：`pip install ai-powered-markdown-translator`，然后运行命令 `aipmt`，无需克隆仓库（2026-09-03）：

  - **单文件脚本变成了可安装的包。** `translate.py` 从根目录移至 `src/aipmt/translate.py`，并提供 console 入口点 `aipmt` 及其等价形式 `python -m aipmt`。参与贡献仍需克隆仓库——测试、28 份翻译和质量工具都位于其中——但使用时不再需要。

    - **import 名称是 `aipmt`，绝不能是 `translate`**，因为该冲突真实存在且不会发出提示。PyPI 包 `translate`（v3.8.1，最后上传于 2026-07-06）会安装一个同名目录。在 venv 中复现：目录优先于模块，`translate.main` 消失，入口点在 `AttributeError` 处损坏——而 `pip check` 返回“未发现损坏的依赖要求”，rc=0。用户仅需安装一次 `pip install translate`，就足以让 CLI 损坏，且没有可用的诊断信息。使用真实 wheel 进行反向验证：将 `pip install translate` 安装在该包之上，`aipmt --help` 在前后两次检查中均为 rc=0，两个 CLI 可以共存。
    - **发行名称长，命令短。** `ai-powered-markdown-translator` 使该包可通过 PyPI 搜索找到；只有缩写的话，不了解该项目的人根本无法找到它，而发布的目的恰恰是让人发现它。经核查排除了两个看似合理的候选名称：`ai-markdown-translator` 自 2024 年起已在 npm 上被一个用途相同的工具占用，比此仓库早 17 个月；而 `aimt` 与 `aim`（v3.29.1）仅相差一个字母，后者是同一领域的活跃包——这是最容易造成长期混淆的情况。顺带提醒一个方法陷阱：`pypi.org/project/<nom>/` 对任何名称都会返回 200（反机器人页面），只有 JSON API 的结果可信。
    - **采用 `src/` layout，而不是扁平包。** 扁平包本可保留测试中的六个 `sys.path.insert(..., "..")`，而问题恰恰就在这里：它们会导入源码树而不是安装后的包，从而掩盖任何打包错误。实际代价只是增加一条替换规则。

  - **密钥终于可以一次配置、永久使用。** 安装后的 CLI 此前没有任何持久配置方式：只能使用环境变量和当前目录的 `.env`。`find_dotenv` 的确会一直向上搜索到系统根目录，因此**当工作目录位于个人目录之下时**能够找到 `~/.env`，但从其他位置工作时便什么也找不到——这种覆盖取决于命令从何处启动，而不是设计上的明确选择。因此新增第三层：`~/.config/aipmt/.env`，优先级低于现有两层。

    - **优先级没有显式编码**，而是来自 `override=False`，即 `load_dotenv` 的默认值：每一层只填补前一层留下的空值。因此顺序为环境变量 → 项目的 `.env` → 用户配置；测试验证的是行为而非结构——交换两次调用的顺序会使测试失败，移除第三层也会失败。
    - **采用 `.env` 格式，而不是 TOML**，这是有意为之：`python-dotenv` 已经是依赖项，相关语法已记录在 15 份 README 中，而且同一个文件可同时用于两种作用域。没有新增依赖或语法。若 `XDG_CONFIG_HOME` 是**绝对路径**，配置位置会遵循它——规范要求忽略相对值，否则配置位置将再次取决于当前目录——Windows 下则使用 `APPDATA`。
    - **排除了两个选项，并明确记录原因。** 系统密钥环（`keyring`）在桌面计算机上更安全，但在 headless 环境中会失败——服务器、容器、CI——而这些恰恰是批量翻译的使用场景；它适合作为主动选择项，却不适合作为默认值。`--api-key` flag 会让密钥进入 shell 历史记录，并使其在 `ps` 中可见。
    - **缺少密钥时，不再显示调用堆栈。** 用户以前会收到指向 `site-packages` 的 Python 堆栈，以及一条仅提到“环境或 .env”却未说明应在哪里创建后者的消息。现在消息会列出三个位置及其准确路径，命令以状态码 2 退出。该防护网被**刻意限制在狭窄范围内**：仅在配置阶段的 `except ValueError`。若包裹整个执行过程，翻译期间出现的真实 bug 就会被转化成令人安心的提示——这正是此仓库要追查的失败模式。一项测试会读取 `main()` 的源码，以禁止这种做法。

  - **修正——工具安装后，用户的 `.env` 会被忽略。** 不带参数的 `load_dotenv()` 并非从当前目录向上搜索，而是从调用它的文件开始，因此会从 `site-packages` 开始搜索。已使用真实 console 入口点进行测量：从一个拥有自身 `.env` 的项目中启动时，`find_dotenv()` 返回 `''`，且密钥未被加载，而 `find_dotenv(usecwd=True)` 可以找到它。只要工具仅从克隆的仓库中运行，此 bug 就不会出现；发布后它将变成系统性问题，唯一症状是在配置正确的情况下仍提示 API 密钥“缺失”。

  - **三个 gate 即使完全停止检查任何内容，也会显示绿色。** 它们已在迁移**之前**刻意加固：在变更之后才编写本应捕获该变更的防护措施，不能证明任何事情。每个 gate 在原始仓库上都为绿色，在迁移后的副本上都会转为红色——两个方向均经过测量。

    - **Lizard 会静默忽略不存在的路径**：rc=0，并显示“分析了 0 个文件”。复杂度 gate 会从 158 个函数 / 2247 nloc 降至 3 个函数 / 34 nloc，输出文件大小为零字节。scope 现在是一个数组，其中每个条目都会验证是否存在。
    - **对不存在的模块运行 `coverage run --source=` 不会失败**：仅在 stderr 发出警告，无论 unittest 还是 `coverage xml` 都返回 rc=0，并且仍会发布报告——statements 从 1453 减少到 141。项目会因为几乎不再受到分析而显得健康。报告现在受两个下限保护：总量，以及测得的最大文件。
    - **翻译新鲜度探针在结构上无法感知调用形式**：它锚定 argparse flag，而重命名文件恰好不会改变这些 flag。复现结果：模块已移动，15 份 README 仍记录着一条不存在的命令，判定却是“没有过期翻译”。因此，第 7 节会验证调用**形式**而非选项；Lizard hook 也会与脚本的真实 scope 对照——当其键 `files:` 不再匹配时，不会导致 pre-commit 失败，而是直接**跳过**。

  - **`requires-python = ">=3.10"` 不再只是一句声明。** `sonar-project.properties` 早已宣称支持 3.10-3.12，却从未实际测试过，因为开发机器上只有 3.12——这是一个内部矛盾，发布后便会公开暴露。现在测试 workflow 会在 3.10、3.11 和 3.12 上运行测试套件，并安装实际的**包**，从而验证其公开版本边界。

  - **只有下限，没有上限。** `requirements.txt` 仍是经过测试的 lock，`[project.dependencies]` 则成为公开契约：若发布 lock 中的精确版本，所有安装了其他包的用户都可能遇到冲突。也不设置 `<N+1` 上限——它会与 `check-deps-fresh.sh` 正面冲突，后者会在任何主版本更新延迟时让 release gate 失败。这组下限可以正常解析，而反向验证 `openai==1.0.0` 会以 `ResolutionImpossible` 退出，证明该检查具有区分能力，并非全盘接受。此外还有一项保护，禁止 `pyproject.toml` 的版本与 CHANGELOG 中的版本不一致：PyPI 不允许重复使用版本号。

  - **已在全新 venv 中进行端到端验证**：约 70 Ko 的 wheel 仅包含 `aipmt/*.py`、dist-info 和许可证；`aipmt --help` 以 rc=0 退出并显示 22 个 flag；`python -m aipmt` 显示“用法：aipmt”，而不是“用法：\_\_main\_\_.py”；`pipx` 安装可正常工作；最重要的是，已从任意用户目录完成**一次真实的法语→英语翻译**，粗体、列表、内联代码、链接和 URL 均得以保留，代码块未被翻译。迁移前的 318 项测试全部通过，且迁移前后的标识符列表逐字节一致——证明没有任何测试被禁用的是这一点，而不是“OK”；另新增 12 项测试来验证三层配置，总计 330 项。

- **1.10.0** 新增 provider `--use_codex`（ChatGPT 订阅配额），更新 SDK 和模型，修正多段落新闻引用（2026-08-29）：

  - **安全审查——PR 设置了两项防护措施，但并未在所有位置贯彻执行**：
    - **Codex 预检会将整个 `.env` 传递给二进制文件。** `_codex_preflight` 调用 `subprocess.run` 时**没有传入 `env=`**：子进程继承了完整的 `os.environ`，因而也继承了由 `load_dotenv` 加载的全部 `.env`。使用插桩的模拟二进制文件测得：**七个秘密信息**进入了预检——六个 provider 的密钥外加一个 `GITHUB_TOKEN`——而其对应的 `_grok_preflight` 中为**零**，后者正确传入了 `env=_grok_env()`。这种不一致存在于 PR 内部：就在相隔几行的位置，`_strip_secret_env` 正是为了维持这一不变量而存在。现在会提取一个 `_codex_env_base()` 并由两条路径共享；修复后测得：两边均为 0 个秘密信息。
    - **“`--deny` 失败时关闭”这一属性并未覆盖实际使用的形式。** 注释将整个 Grok 限制机制建立在如下事实之上：具有未知前缀的规则会导致启动被拒绝。在 `grok 1.0.13` 上测得，这项验证**只适用于带括号的形式**：`--deny 'CeciNestPasUnOutil(*)'` 会拒绝启动（“未知工具前缀”），而 `--deny 'CeciNestPasUnOutil'` 会被静默接受。但 `GROK_DENY_RULES` 只使用了裸名称——因此，如果 xAI 端重命名工具，在操作系统 sandbox 已经不适用的机器上，唯一经过实测的限制层就会在毫无提示的情况下被移除。八条具名规则现已改为 `Prefix(*)`，每条都会被验证为 CLI 已知前缀；兜底规则 `*` 保持字面形式，这是唯一受支持的形式。一项测试可防止重新使用未经验证的形式。
    - **其余方面已验证无误**：不存在命令注入（各处均使用列表形式，从不使用 `shell=True`，文档内容通过 stdin 或 `--prompt-file` 传递），不存在不安全的反序列化（仅使用 `json.loads`，并带有类型防护），路径遍历修复在七个载荷上均未发现绕过方式，并且 CLI 确实应用了 `--deny '*'`（读取工作目录之外的内容时观察到 `DENY_ENFORCED`）。
    - 上文新增的新鲜度检查顺带绕过了自己的原则：当某个软件包的 PyPI 请求失败时，它会被静默跳过，gate 仍显示通过。现在它会统计实际完成比较的软件包，并在覆盖不完整时失败。

  - **依赖项已升级，并设置两道防线以防再次滞后**：

    - **滞后是真实且长期的**：`openai` 2.54 → **3.6.0**，`anthropic` 0.125 → **1.2.0**，`certifi` 2024.8.30 → **2026.7.22**——也就是说，用于验证所有 provider TLS 调用的根证书库落后了两年。原因已经确定：**此前不存在 `.github/dependabot.yml`**。没有该文件时，GitHub 只会启用_安全更新_，Dependabot 也只会针对受 CVE 影响的依赖项提出 PR——这解释了它为何升级了 `urllib3` 和 `idna`，却任由两个 SDK 跨越一个主版本持续落后。
    - **两个主版本可以无冲突地共存**，与先前推断的担忧相反：`openai` 3.x 和 `anthropic` 1.x 会迁移至 **`httpx2`**，而 `mistralai` 和 `google-genai` 仍保留在 `httpx<1`，但它们是两个不同的发行包。通过真实安装验证后，又对 **7 条 provider 路径进行了端到端测试**——OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI 和 Grok CLI——每项输出中的内联代码和链接均得到保留。“避免两套 HTTP 栈”只是一项偏好，并非阻塞因素：实测结果已作出裁决。
    - **`requirements.txt` 并未描述真实环境**：`google-auth`、`cryptography` 和 `opentelemetry` 栈都安装在工作 venv 中，却从未声明——因此，全新安装无法复现被测试的环境。相反，`tokenizers`、`huggingface-hub` 和 `PyYAML` 虽列于其中，却既未被导入，也不为任何内容所需，它们是 `mistralai` 1.x 的遗留项。该文件已根据仅由直接依赖构建的 venv 完整依赖闭包重新生成。`pip-audit` 未在新依赖集中发现任何已知漏洞。
    - **`.github/dependabot.yml`**（新增）启用每周版本更新，涵盖 pip 和 github-actions。次版本和补丁更新合并为一个 PR——每次只提交一个补丁升级的 PR 最终会被忽略，而噪声正是更新的敌人；**主版本更新则分别提交**，每项都必须通过真实调用验证。
    - **`scripts/check-deps-fresh.sh`**（新增，已接入 gate）让滞后情况直接体现在项目判定中：Dependabot 只负责提出更新，不能提供保证，而且它的 PR 可能不断堆积。主版本滞后 → 失败；次版本滞后 → 警告，因为长期处于红色的 gate 最终会被忽略；PyPI 无法访问 → 本地明确跳过，**CI 中则失败关闭**，因为未执行的检查不等于成功。已从正反两方面验证：它可以捕获修复前的准确状态（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`），而对于次版本滞后只会发出警告。

  - **本次 PR 审查产生的修复**——五个审查 agent 对差异进行了全面检查；以下问题在修复前均已通过实测**复现**，其中两个是本版本前文所引入的回归。

    - **已修复回归——`_NEWS_CITATION_REGEX` 存在指数级回溯。** 多段落修复在重复结构中引入了 `(?:[ \t]*$|[ \t]+.*)`：`[ \t]+` 与 `.*` 对空格的分配存在歧义，而且这种歧义会随迭代次数增加而成倍增长。在无法匹配该模式的 `>   texte` 行——完全合法的 Markdown 缩进——上测得：**14 行耗时 2,589 毫秒**，修复后为 0.04 毫秒，每增加一行耗时约乘以 9。在 `--news` 模式下，一个不符合要求的长 blockquote 足以让翻译卡死，直到任务超时，且无法确定原因。现在重复结构会一次性消费整行（`\n^>(?![ \t]*—).*`），使每次迭代只剩一种匹配方式。已在包含 231 篇文章的真实语料库上验证：捕获结果**零差异**，仍为 423 条引文，14 个多段落正文也依然全部扩展。
    - **同时使用两个 provider flag 会在静默状态下产生按量计费。** `--use_codex --use_mistral` 此前会被接受；`_select_provider_client` 首先检查 Mistral，`_resolve_provider` 则优先处理显式布尔值——两者最终都会选择 Mistral。因此，用户原本请求使用订阅配额，却在没有任何警告的情况下收到按量计费：这正是 `--use_codex` 旨在防止的故障模式。六个 provider flag 现在全部通过一个 `add_mutually_exclusive_group` 处理。**行为变更**：此前会被静默接受的同时指定两个 provider 的命令行，现在会在 `argument --use_mistral: not allowed with argument --use_codex` 上失败。
    - **收尾 gate 在探针崩溃时仍会显示通过。** `scripts/check-release-ready.sh` 的十三项检查中有四项采用“捕获 stdout，若为空则下结论”的模式，却从不检查返回码：异常（文件被重命名、`FileNotFoundError`）会写入 stderr，使 stdout 保持为空，而检查则判定“没有问题”。为防止“一个 `exit 0` 什么也证明不了”这一陷阱而编写的脚本，内部却再次陷入了同一陷阱。现在，辅助函数 `probe()` 会同时要求返回码为零**且**存在结束哨兵，探针也会拒绝对空标记集合下结论——因为针对空集合的断言永远为真。演示结果：加入上述互斥组后，provider flag 会通过一个 `*_group` 对象，而旧正则表达式 `parser\.add_argument\(` 不再与其匹配；**二十一个 flag 中有六个**被静默排除在检查范围之外，gate 却仍显示通过。
    - **秘密信息扫描漏掉了六个 provider 中的四个。** 字符类 `[A-Za-z0-9]` 排除了连字符：`sk-proj-…`（当前 OpenAI 格式）和 `sk-ant-api03-…` 都会在第二个连字符处中断，而 `AIza…` 根本未被覆盖。模式现已扩展，`.secrets.baseline` 则被排除在扫描范围之外。此外，防护 `.env` 查询的是 `git diff --cached`，它只能看到索引：一个**已经提交**的 `.env`——最糟糕的情况——永远不会出现在其中。现在它改为查询 `git ls-files`。
    - **Codex 的“token 预热”其实并未预热。** 实测显示：`codex login status` 不会触及 `~/.codex/auth.json`（修改时间和大小均未变化），其帮助信息写的是“显示登录状态”。然而，注释却声称它会“单次、顺序地”刷新 token，从而消除一次性轮换 token 并发刷新带来的风险。所宣称的保护并不存在；现在注释会如实描述代码行为，真正的应对措施仍是 `max_jobs=4`。此外，检查现在会遵循此前被忽略的 `CODEX_BIN`——在 `PATH` 中没有 `codex` 的机器上，此前会以“未认证”失败，造成误导性诊断。
    - **`.env` 在子 shell 中被载入。** `detect_provider` 通过命令替换调用，因此其中的 export 无法传回：在 `.env` 中定义的 `GROK_BIN`、`GROK_HOME` 或 `REGEN_MODEL`，对 `main()` 中执行的读取仍不可见，后者会在配置正确的情况下错误地判定“找不到 Grok 二进制文件”。
    - **并发量比声明的上限高出 50%。** 防护被放在启动 README/CHANGELOG 任务对之后：`max_jobs=2` 的实测峰值为 **3**。对于每周配额与 Chat/Imagine/Voice 共享且无法测量的 Grok，脚本设定的上限因此并未得到遵守。最终计数虽然会显示，却从未与 28 进行比较——缺少文件也不会被发现。
    - **Grok 输出契约：缺少 `stopReason` 现在会导致失败。** 代码此前应用的是“`end_turn` **或缺失**”，而已声明的契约要求 `end_turn`。如果载荷中没有该字段——或者 CLI 更新将该字段重命名——防护就会静默变成空操作。此外，`max_turn_requests` 不再归类为速率限制（这是轮次数预算耗尽：重试只会复现相同结果，却要付出 90 秒等待），`quota` 也从速率限制标记中移除——原因早已写在 `_codex_is_rate_limited` 的文档字符串中，只是 Grok 此前并未遵循。
    - **Gemini 级联会按模型进行记忆化。** 它此前会在每个分段都从 `minimal` 重新开始，尽管默认模型会拒绝该请求：正常路径因此会为每个分段付出一次 400 往返，并重复打印相同警告。重复数百次的警告不会再有人阅读——它正是这样变成遮蔽物的。
    - **其他修复**：CI 中的拒绝消息被硬编码为 Codex，导致 `--use_grok_cli` 的用户被引导至 `OPENAI_API_KEY`，而不是 `XAI_API_KEY`；`provider.capitalize()` 显示为“Grok_cli”和“Openai”；子进程基础设施的注释将“shim”错误地泛化到两个 CLI，实际上 Grok 二进制文件是原生 ELF（正确理由是“会生成自身子进程的 agent”）；`subprocess` 上的十二项 SAST 发现已标记为 `# nosec` / `# nosemgrep` 并附有理由，使用不带 `shell=True` 的列表形式使注入不可能发生，且文档内容从不通过 argv 传递。
    - **秘密信息不再进入 agent 子进程。** 基于名称的 deny-list 此前只保护**计费**不变量（Codex 不含 `OPENAI_API_KEY`，Grok 不含 `XAI_API_KEY`）。实测显示：每个子进程中仍会进入**另外七个秘密信息**——Anthropic、Mistral、Google 和 Gemini 的密钥、另一个 CLI 的密钥，以及 `OPENAI_BASE_URL`；后者虽不是秘密信息，却会改变流量路由。但这两个 CLI 都是 **agent**，而 Grok 在许多 Linux 机器上运行时没有适用的操作系统 sandbox。现在会按**名称模式**进行过滤（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`），而不是使用具名列表，因此也能覆盖用户在 `.env` 中自行添加、但代码并不知晓的变量。CLI 不需要其中任何变量：认证信息存放在 `~/.codex` 和 `~/.grok` 中，从不存放于环境中——已通过在强化环境下分别使用两个 provider **实际完成翻译**验证。
    - **测试**：新增文件 `tests/test_review_hardening.py`（21 项测试），用于锁定 provider flag 的互斥性、`stopReason` 契约、新闻正则表达式的线性复杂度、CI 拒绝消息、Gemini 记忆化，以及子进程环境中不存在任何秘密信息。最后这项断言是**通用的**——即使密钥未被任何列表命名，它也会失败——而现有的清除测试只是其常量的镜像，除自身循环故障外无法检测任何其他问题。完整测试套件现为 **311 项测试**。
  - **两个新的 Grok provider**：`--use_grok`（xAI API，密钥为 `XAI_API_KEY`，按用量计费）和 `--use_grok_cli`（官方 Grok Build CLI，从 Grok 订阅额度中扣除——原理与 `--use_codex` 相同）。
    - **API 模式，约 40 行**：由于 xAI endpoint 与 OpenAI 兼容，client 和 `_call_openai` 均可原样复用，只有 `base_url` 需要更改。仅需一项适配，而且所有 provider 都能受益：`finish_reason` 现在接受 `end_turn`，这是 xAI 输出的格式，而 OpenAI 输出的是 `stop`。模型：`grok-4.6`（高质量）和 `grok-4.3`（经济型）。需要注意的是，Grok 的经济型模型仍是仓库中最昂贵的——每百万 token 为 $1.25/$2.50，而 `mistral-small-latest` 为 $0.15/$0.60：选择此 provider 是为了模型多样性，而不是价格。
    - **CLI 模式**：以 Codex 为蓝本，但根据实际情况存在四点差异——prompt 通过文件传递（`--prompt-file`，CLI 不读取 stdin，而 argv 中的 segment 会暴露在 `ps` 中）；输出是 stdout 上的单个 JSON 对象（既不是 JSONL，也不是 `-o` 文件）；订阅仅提供 `grok-4.6` 和 `grok-4.5`；sandbox 无法应用（见下文）。子进程启动逻辑与 Codex 一并提取到 `_codex_run_process` 中，未触及已经过测试的 Codex provider 其余部分。
    - **`exit 0` 并不能证明任何事情，这是实测结论**：未认证时，CLI 会将 `{"type":"error","message":"Not signed in."}` 写入 **stdout**，而返回码仍为 **0**。请求被拒绝或超出轮次限制时表现相同。因此，输出契约要求同时满足四个条件：返回码为 0、没有错误 payload、`stopReason == end_turn`，并且文本非空。preflight 遵循同样的逻辑：即使未登录，`grok models` 也会以 0 退出，只有 stdout 中出现“not authenticated”才能据此判定。
    - **隔离：有意采用并明确记录的不对称设计。** Codex 在 `--sandbox read-only` 中运行，而 Grok 的 sandbox 在许多较新的 Linux 工作站上无法应用，原因来自两个彼此独立的系统限制，若无 `sudo` 则无法规避：自 Ubuntu 24.04 起，AppArmor 会阻止非特权 user namespace（`bwrap: setting up uid map: Permission denied`，已在 Grok 之外复现）；当 `/run/podman` 处于 `0700` 状态时，容器 runtime socket 的 deny-list 会失败（resolver 只会捕获 `ErrorKind::NotFound`，EACCES 会成为致命错误）。核心陷阱是：无法应用的**内置** profile 会悄无声息地以无隔离方式启动。因此，脚本默认不请求任何 profile，也绝不会静默回退——它会在 stderr 上发出警告。防护依赖 CLI 的 `--deny` 规则，其中包括 catch-all `*`；这是唯一经过实测的 _fail-closed_ 层（规则使用未知前缀时会拒绝启动）。可通过 `GROK_TRANSLATE_SANDBOX=read-only` 强制要求该层；若机器无法满足要求，启动就会失败。
    - **防护措施**：从子进程环境中移除 `XAI_API_KEY`、`GROK_API_KEY` 和 `GROK_SANDBOX`（密钥会切换为按用量计费；继承的 `GROK_SANDBOX` 会强制使用无法应用的 profile，并显示具有误导性的消息）；禁用 MCP/hooks/skills/agents 开关；使用 `--disable-web-search`、`--no-subagents`、`--no-plan`、一次性 workdir；拒绝在 CI 中运行；timeout 会终止整个 process group；遇到 rate limit 时执行 back-off。`--max-turns` 被设为 6 而不是 1：计数器会在工具轮次之后递增，设为 1 会截断输出。
    - **配额**：Grok 的额度池按周计算，并且**与 Chat、Imagine 和 Voice 共享**，没有任何命令可以显示该额度——Codex 则可通过 `account/rateLimits/read` 量化消耗。因此，`regen_translations.sh` 将并发数限制为 2，并明确发出警告。
    - **测试**：新增文件 `tests/test_grok_provider.py`（24 项测试）。完整测试套件共 **290 项测试**。
  - **已修复的 bug——多段落英文引文仅有一部分受到保护（`--news` 模式）**：`_NEWS_CITATION_REGEX` 仅接受一系列**连续的** `>` 行作为引文正文。一旦引文跨越多个段落（段落间由一个空的 `>` 行分隔），就只有最后一段会被捕获并替换为 placeholder；此前的段落会被送入 LLM 并以译文返回——这与 `--news` 的保障目标恰好相反。重复模式现在接受内部的空 `>` 行，并改为非贪婪匹配，从而在斜体行之前的空 `>` 处停止，而不是在遇到的第一个空行处停止。
    - **实测影响范围**：在包含 198 篇文章的真实语料库中，419 条引文里有 11 条受到影响。没有出现回归——新 regex 捕获的引文数量完全相同，只有多段落正文的范围得到扩展（408 个正文保持一致，11 个扩展）；归属说明行 `> — …` 仍不会被吸收到正文中（保留了 lookahead）。
    - **端到端证据**：对一篇 69 ko 的文章进行 ja/ar 翻译时，引文的第一段此前在日语中会变成 `> GLM-5.3がオープンウェイト化。`，在阿拉伯语中也同样会被翻译；现在则保持为 `> GLM-5.3 is now open-weight.`。英文引文行数从 9 恢复到 10，与源文一致。
    - 需要注意的是，此缺陷未被下游 validator 检测到，因为它们只验证引文是否存在，并不检查引文是否完整。
  - **默认 provider 的实测成本节省**：只要模型名称以 `gpt-5` 开头，`_openai_extra_kwargs` 就会发送 `reasoning_effort="medium"`，包括在 `--eco` 中。使用 `gpt-5.4-mini` 翻译一个由十个单词组成的句子的测量结果：`medium` → 45 个 reasoning token 和 65 个输出 token；`none` → 0 和 14。reasoning 对翻译毫无帮助，却会在每个文件的每个 segment 上产生费用。现在，在 `--eco` 中默认值改为 `none`，其他情况下仍为 `medium`；通过 CLI 显式传入的值仍具有更高优先级。除 `low`/`medium`/`high` 外，`--reasoning_effort` 现在也接受 `none` 和 `xhigh`（并非所有模型都接受全部取值：例如 `gpt-5.4-mini` 会拒绝 `minimal`——现有的不带该参数重试机制可处理这种情况）。
  - **SDK 更新与 Gemini 迁移**：`google-generativeai`（支持已于 2025-11-30 结束，仓库已归档）由统一 SDK **`google-genai`** 替代——先 `genai.Client(api_key=...)`，再 `client.models.generate_content(model=, contents=, config=)`；system prompt 通过 `system_instruction` 传递，不再与 segment 拼接。`mistralai` 升级至 **2.9.4**（import 改为 `from mistralai.client import Mistral`；旧写法会抛出 `ImportError`，已在 wheel 中验证），`anthropic` 升级至 **0.125.0**，`openai` 升级至 **2.54.0**——这些是切换到 `httpx2` 之前的最后版本，以避免 venv 中同时存在两套 HTTP stack。`httpx` 0.28.1 和 `pydantic` 2.13.5 也因此解除版本锁定。
  - **由真实测试而非文档发现的两个回归**：
    - `anthropic` ≥ 1.0 会在 client 端拒绝 `max_tokens` 预示时长超过 10 分钟的非 streaming 调用（`ValueError: Streaming is required...`）。0.34.2 中没有这项防护，它会导致所有使用 `max_tokens=32768` 的 Claude 调用失败。通过显式设置 `timeout`（`CLAUDE_TIMEOUT`，默认 900 s）修复，因此无须为了仅使用完整响应的调用切换到 streaming。
    - 只有 Gemini catalogue 中的部分模型接受 `thinking_level="minimal"`：`gemini-3.1-flash-lite` 支持它，`gemini-3.7-flash` 和 `gemini-3.1-pro-preview` 则以 400 拒绝。因此新增 `_gemini_generate_with_fallback`，采用 `minimal` → `low` → 不设置 thinking_config 的级联策略，仿照已有的 OpenAI fallback——优化参数绝不能导致翻译失败。
  - **更新默认模型**，每个模型均通过真实调用验证：OpenAI `gpt-5.5` → **`gpt-5.6-terra`**（在 28 个项目的 batch 上减少 60%）及 `gpt-5.4-mini` → **`gpt-5.6-luna`**（减少 73%）；Claude `claude-sonnet-4-6` → **`claude-sonnet-5`**（价格更低且更新）及 `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（不带日期的规范 ID）；Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`** 及 `gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（稳定版本，且比 `3.5-flash-lite` 更便宜）。Mistral 保持不变，`mistral-large-latest` 仍是四者中性价比最高的模型。需要注意的是，没有比 `gemini-3.1-pro-preview` 更新的 Gemini Pro 系列模型——2026 年 5 月发布消息的 Gemini 3.5 Pro 从未推出；3.5/3.6/3.7 系列均仅有 Flash。
  - **切换 Gemini 前进行的实测 A/B**：分别使用 `gemini-3.1-pro-preview` 和 `gemini-3.7-flash` 将 `README.md` 翻译成日语。结构完全相同（21 个列表、18 个代码块、13 个 HTML 链接、13 张图片，所有 URL 均得到保留），耗时为 **8 s 对 48 s**。由于没有公开 benchmark 比较这两个模型在翻译或非拉丁文字方面的表现，否则此次切换只能基于简单推测。
  - **Claude 响应块过滤**：`_call_claude` 会执行 `block.text for block in response.content`，但不筛选类型。采用 adaptive reasoning 的模型（Sonnet 5 及更高版本）会插入一个 `thinking` 块，该块提供 `.thinking` 而不是 `.text`——翻译会在第一个 segment 就因不透明的 `AttributeError` 而中断。现在会排除 `thinking`、`redacted_thinking`、`tool_use` 和 `tool_result` 块（采用负面列表，以继续容忍携带文本的未知类型）；若响应中没有任何文本块，则会抛出明确错误。每次调用都会传入 `thinking={"type": "disabled"}`。
  - **重新同步 `MODEL_TOKEN_LIMITS`**：移除下线日期已过的模型（`magistral-*` 系列于 2026-07-31 下线，`gemini-2.0-*` 于 2026-06-01 下线，`gemini-3-pro-preview` 于 2026-03-09 下线，以及 `claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。修正限制：Mistral 128K → **256K**（Large 3 / Small 4 世代），Gemini 1 000 000 → **1 048 576**（实际 input 限制），`claude-opus-4-5` 200K → **1M**，`gpt-5.6-*` 系列 400K → **1.05M**。新增 Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest` 和 `ministral-*` 系列。需要注意的是，这些限制仍仅供参考，因为 `translate()` 会将 segmentation 上限设为 `min(16000, limite)`。
  - **Provider `--use_codex`**：第五个 provider，用于以非交互模式驱动官方 Codex CLI（`codex exec`），而不是调用按用量计费的 API。翻译用量将从已付费的 ChatGPT 订阅配额中扣除。这是 OpenAI 为此用途记录的唯一途径：各套餐的可用性矩阵将“Codex SDK、`codex exec` 和可编程工作流”列为 Plus/Pro/Business/Enterprise 可用功能，而 `~/.codex/auth.json` 的 token 无法对 API Platform 调用进行身份验证（且本脚本从不读取这些 token——身份验证及其刷新仍由 CLI 管理）。
  - **Codex 二进制文件现在可通过 pip 安装，不再仅限 npm**：`_resolve_codex_binary()` 会依次在 `CODEX_BIN`、`PATH`，然后在 OpenAI 发布的官方 Python 包 **`openai-codex-cli-bin`** 中查找二进制文件（这是 `openai-codex` SDK 的依赖项）。因此，Python 项目使用 `--use_codex` 时不再需要全局安装 npm。该包未被添加到 `requirements.txt`：二进制文件约为 250 MB，若添加，所有用户都将被迫安装它，而它只是可选 provider。已完成端到端验证：当 `codex` 不在 `PATH` 中时，解析流程能够找到打包的二进制文件，并在 6 秒内完成完整翻译。
  - **“订阅模式”保证**：从子进程环境中移除 `OPENAI_API_KEY` 和 `CODEX_API_KEY`。如果没有这项保护，`.env` 中存在的密钥可能会让 Codex 在没有任何可见提示的情况下切换为按用量计费——而避免这种情况正是该 provider 存在的目的。
  - **通过测试锁定 CLI 陷阱**：
    - 即使 prompt 已作为参数传入，`codex exec` **仍会**读取 stdin：如果不关闭 stdin，命令会一直等待到超时，且从不调用模型（已复现：180 秒后以 124 退出，输出为零字节）。因此，`communicate(input=...)` 必不可少。
    - 通过 npm 安装的 `codex` 是一个 Node shim，它会通过 `spawn` 启动真正的 Rust 二进制文件：后者是 Python 进程的**孙进程**，会在 `subprocess.run(timeout=)` 执行 `SIGKILL` 后继续存活并消耗配额。因此需要 `Popen(start_new_session=True)` + `os.killpg`。
    - CLI 可能在发出 `turn.failed` 的同时仍以 0 退出：除返回码外，还会检查 JSONL 输出（`--json`）；如果返回码为 0 却缺少 `-o` 文件，则会抛出明确错误，而不是生成空片段。
  - **rate limit 的 back-off**：CLI 未实现任何内部 retry（`max_retries = 0`）。分类基于 JSON payload 的结构（`status: 429` / `error.type`），而不是子字符串——“quota”一词既可能出现在可恢复的 429 中，也可能出现在永久性的 `insufficient_quota` 中。
  - **CI 防护**：如果定义了 `CI` 或 `GITHUB_ACTIONS`，则拒绝 `--use_codex`。订阅身份验证并非为共享 runner 设计，OpenAI 也明确不建议在公共仓库中使用此工作流。
  - **模型**：`gpt-5.6-sol`（质量）和 `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` 系列由 CLI 和 API Platform 共用，但 ChatGPT 账户并非有权使用其中全部模型：allowlist 在服务器端应用，不进行本地验证，使用不常见的模型会触发警告。在 Plus 套餐中，每个 5 小时窗口内，Luna 可提供 250–2,000 条消息，而 Sol 仅为 10–100 条：`--eco` 是所有批处理任务的推荐模式。
  - **已修复 Bug——`regen_translations.sh` 在完全成功后仍以错误退出**：`trap ... EXIT` 引用了 `failed_log`，后者是 `main()` 中的 `local` 变量，在 trap 执行时已不存在。在 `set -u` 下，这会引发 `failed_log: unbound variable`，导致脚本以 1 退出，尽管全部 28 项翻译均正确——这会在成本最高的重新生成步骤完成后，立即中断 `release.sh --auto`（`set -e`）。该变量现已改为全局变量，trap 会检查其是否存在。一个有益的副作用是：此前被该错误掩盖的真实翻译失败，现在会重新显示在最终汇总中。
  - **`REGEN_MODEL`**：`regen_translations.sh` 的新环境变量，可强制指定模型并覆盖 provider 的默认模型，例如使用 `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`，通过订阅配额中的高端模型重新生成，而不是使用面向吞吐量的 `--eco` 模型。
  - **`regen_translations.sh`**：`REGEN_PROVIDER=codex` 现可通过明确的 opt-in 启用（绝不自动检测，以免在用户不知情的情况下消耗订阅配额）。在启动并行任务前，会先以串行方式刷新一次 token——由于 Codex refresh 具有轮换性且只能使用一次，并发 job 会使 `codex login` session 失效——并发数也会降至 4。
  - **相关重构**：`_dispatch_provider_call` 的参数由 8 个减少到 6 个，改为通过返回 provider 名称的 `_resolve_provider()` 实现，而不再在整条调用链中传递第四个布尔值。显式布尔值的优先级仍高于 `args`，以保留使用最小化 `Namespace` 调用 `translate(..., use_mistral=True)` 的测试。
  - **测试**：新增文件 `tests/test_codex_provider.py`（48 项测试），覆盖 argv、净化后的环境、禁止前言的契约、静默失败、timeout/killpg、back-off、preflight、provider 解析、Gemini 推理级联、Claude 区块过滤以及多段落新闻引用。完整测试套件共 290 项测试。
  - **实际验证**：项目的 `README.md` 通过 Codex 翻译为**14 种语言**后，其结构与参考翻译严格一致（14 个代码块、24 个标题、25 行表格、13 个 HTML 链接、13 张图片、19 个 URL；代码块逐字符完全相同，placeholder 残留为零）。对于一篇 69 KB 的新闻文章，在 `--news` 模式下，`gpt-5.6-luna` 和 `gpt-5.6-sol` 的输出均通过了下游应用针对 en/ja/ar 的验证器。通过 `account/rateLimits/read` 测得的消耗量：在 `--eco` 模式下始终低于计数器的舍入阈值（5 小时窗口的 0%）。

- **1.9.2** 修复带嵌套括号或法语前缀的新闻署名 URL 提取问题（2026-05-11）：

  - **已修复 Bug**：`_protect_news_quotes` 中的署名 URL 提取使用正则表达式 `re.search(r"\((.+?)\)", attribution)`（括号之间的惰性捕获）。对于 `(relayé par [@user sur X](https://x.com/.../123))` 形式的署名（嵌套括号：外层 `(` + Markdown 链接的 `]()`），捕获会在遇到第一个 `)` 时停止 → 得到被截断且包含法语前缀的字符串：`relayé par [@user sur X](https://x.com/.../123`（缺少末尾的 `)`）。结果是：`_validate_news_post` 会在翻译后的输出中查找该字符串并必然失败（原因有二：`)` 被截断 + “relayé par”会被翻译成 `relayed by`/`weitergeleitet von`/……）。完整的 low → medium → high → gpt-5.5 级联均无法通过。
  - **修复**：正则表达式改为 `re.search(r"\]\(([^)]+)\)", attribution)`——专门匹配 Markdown 链接中的 `](url)`，并且**仅捕获纯 URL**（不含法语前缀，也不会截断）；翻译期间由 placeholder `#URL{N}#` 保持其不变。可稳健处理以下两种问题模式：
    - `(relayé par [@account sur X](url))`——嵌套括号
    - `via [@source](url)` 或 `selon [@author](url)`——不带外层括号的法语前缀
  - **测试**：在 `test_silent_failure.py` 的 `TestNewsCitationExtraction` 类中新增 2 项测试：
    - `test_extract_attribution_url_with_nested_parens`（精确复现 Genspark CEO E2B Bug 的案例）
    - `test_extract_attribution_url_with_french_prefix`（包含 `via` 的变体）
  - **覆盖缺口**：`check-editorial-coverage.py` 会验证编辑语法，但不会验证 translator 是否能够正确翻译。一个可行的改进方向（超出 v1.9.2 范围）是添加一项检查，通过 dry-run 模拟署名提取，以便在发布**之前**检测高风险模式。

- **1.9.1** 修复翻译标记说明中 CTA 标签的 i18n 问题（2026-05-10）：

  - **已修复 Bug**：翻译文件顶部 marker 横幅中 CTA 链接的 `[Voir le projet sur GitHub ↗]` 标签，对所有目标语言都仍然**显示为法语**，而不是遵循 `target_lang`。LLM 永远看不到该标签（它由 Python 端组装，以保留仓库的 URL 和 slug），因此翻译阶段无法补救。自 v1.9 引入 `marker` 格式以来，这一直是一项静默回归。
  - **修复**：新增常量 `_VIEW_PROJECT_LABELS`，将 15 种语言映射到各自的本地化标签。`_translation_note_invariants(target_lang)` 和 `_assemble_translation_note_paragraphs(phrase, target_lang)` 现在会传递目标语言。如果语言未知，则 fallback 到 `fr`（确保安全，避免 KeyError）。
  - **测试**：调整 `test_source_emits_three_paragraphs_repo_title_description_link`（目标语言 `ja` → 预期为日语标签）。新增 2 项测试：`test_source_link_label_localized_per_target_lang`（对 7 种语言进行参数化测试，覆盖拉丁字母、表意文字和辅音音素文字）以及 `test_source_link_label_falls_back_to_french_for_unknown_target`。`test_translation_note_position.py` 中共计 40 项测试（原为 38 项）。
  - **向后兼容**：签名使用默认值 `target_lang="fr"`——未提供 `args.target_lang` 的外部编程调用方无需修改即可继续工作。
- **1.9** 修复静默失败 + 完整质量工具链 + 多位置翻译说明（2026-05-07）：
  - **多位置翻译说明 + “embed card”标记格式**：
    - 新增 CLI 选项（增量添加，默认行为不变 → **非破坏性变更**）：
      - `--note_position {top,bottom,both}`（默认：`bottom`）：将说明放置在译文文件顶部、底部或同时放在两处。
      - `--note_format {legacy,marker}`（默认：`legacy`）：
        - `legacy` 严格复现 v1.8 的行为（粗体段落 `**…**`），达到**逐字节一致**。
        - `marker` 输出一条不可见的 Markdown 链接引用定义（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`），随后是一个结构化的**三段式引用块**，以呈现类似“GitHub 仓库嵌入卡片”的效果：使用行内代码显示项目标题（`**\`ai-powered-markdown-translator\`\*\*`）、由 LLM 翻译的描述，以及带有可见箭头的 CTA 链接（`[Voir le projet sur GitHub ↗](URL)`）。构建时可通过 remark 插件处理（参见 jls42.org 博客 → 插件 `remark-translation-banner`）。
    - **绝不发送给 LLM 的不变量**：仓库标题和 GitHub URL 在描述性语句翻译完成后由 Python 端组装。LLM 永远不会看到 slug `ai-powered-markdown-translator` 或 `https://github.com/jls42/...`，从而保证渲染器、大小写及协议均不会被修改。
    - **感知 frontmatter 的插入机制**：在 `top` 或 `both` 模式下，说明会插入到 YAML frontmatter 的结束 `---` 块**之后**（确保兼容 Astro Content Collections / gray-matter）。辅助函数 `_split_frontmatter` 检测文件开头的 `---\n…\n---\n` 并保持其完整性；若 frontmatter 已开启但没有结束围栏，则**抛出 `RuntimeError`**（该文件会被记录到 `failed_files`，而不会写入位置错误的说明）。
    - **模型名称白名单清理器**：`_sanitize_model` 将 `[A-Za-z0-9._:/-]` 范围之外的所有字符替换为 `_`，为空时回退到 `unknown`。这与 Astro remark 插件端的验证器保持一致，并消除可能破坏标记格式的字符（空格、引号、括号、逗号等）。
    - **内部重构**：`_append_translation_note`（1 个单体函数）→ 7 个纯辅助函数（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。构建器与组合器分离（构建器返回不含分隔符的纯块，组合器根据位置应用 `\n\n`）；生产代码与源辅助函数共用同一个三段式组装器。
    - **`_quote_lines` 保留空行**：为每一行添加 `> ` 前缀，并将空行转换为单独的 `>`。这使 mdast 能在引用块中识别三个独立段落（标题／描述／链接），而不是一个带换行符的单一段落。
    - **自适应 `_build_translation_note_block`**：根据 LLM 保留的段落数量进行处理（3 段 = 完整卡片格式，2 段 = 语句 + 链接，1 段 = 回退模式）。当检测到 Markdown 链接 `](` 时，单段回退模式**不再用 `**...**` 包裹内容**（在链接周围使用 `<strong>` 的渲染效果不稳定）。
    - **向后兼容**：在 `_compose_with_notes` 端使用 `getattr(args, "note_position", "bottom")` 和 `getattr(args, "note_format", "legacy")`——不包含这些属性的 Namespace（现有测试、外部程序化调用）无需修改即可继续运行。
  - **修复长文本翻译中的静默失败**：
    - 对所有提供商（OpenAI、Mistral、Claude、Gemini）执行译后语言验证：确定性层（检查是否逐字出现源文本片段）+ 概率性层（`langdetect`）
    - `finish_reason` / `stop_reason` 白名单：遇到白名单之外的任何状态（截断、content_filter 等）时抛出 `RuntimeError`
    - `max_tokens` Claude：`4096` → `32768`（避免 16k 分段出现潜在截断，并为 FR→JA/ZH/KO/AR/HI 的跨文字系统转换预留空间）
    - 感知标题的分段：优先选择分段后半部分的 H2/H3（使每个分段都从完整的语义章节开始）
    - 将错误传播至非零退出码：`translate_markdown_file` 返回类型化状态 `success` / `failure` / `skipped`；只要至少一个文件失败，`main()` 就会 `sys.exit(1)`（适用于单文件与批处理）
    - 为所有提供商添加空内容防护、源文本／输出合理性比例检查（源文本 ≥ 500 个字符且输出不足 5% 时拒绝）、代码占位符验证（`#CODEBLOCK`/`#INLINECODE`）、LLM 后规范化（修复与标题粘连的分隔符／链接），以及不带 `reasoning_effort` 的 `BadRequestError` 重试
    - 新增依赖 `langdetect==1.0.9`
  - **pre-commit 质量工具链**（“完整 EurekAI 类型”，14 个钩子）：
    - Pre-commit：ruff（检查与格式化）、shellcheck、prettier（md/yaml/json）、detect-secrets（保护 4 个 API 密钥）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（空白字符、文件结尾、大文件、shebang 等）
    - Pre-push：mypy（渐进式宽松模式）、Opengrep SAST（translate.py + scripts/）、pip-audit（初始报告模式）、unittest discover（tests/ + scripts/tests/）
    - `scripts/` 中的本地包装器使用 `./venv/bin/python`
    - `scripts/audit_verdict.py`：pip-audit JSON 解析器，包含 11 个 unittest；是针对 Python 改写的 jls42-astro 解析器版本
    - 修复了 7 个初始 ruff 违规：B904（raise from）×2、B007（未使用的 dirs）、C408（字典字面量）、C419（列表推导式）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizard 暂时排除 `translate.py`（4 个函数的 CCN 为 21–47，已计划重构）——对 scripts/ 实施严格门禁
  - **SonarCloud + 全面覆盖率**：
    - GitHub Actions 工作流 `SonarCloud`（sonarcloud.yml + sonar-project.properties）：每次推送和 pull request 时进行分析，并通过 `coverage.xml` 生成覆盖率
    - README 顶部新增 11 个 SonarCloud 徽章（Quality Gate、Security/Reliability/Maintainability 评级、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）
    - `tests/test_silent_failure.py`（`unittest` 标准库）：覆盖静默失败错误链的六个环节
    - `tests/test_orchestration.py`（新增 79 项测试）：覆盖 `translate.py` 的编排层（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` TypeError + BadRequestError 回退、o1 系列提示词格式，以及 `_validate_translation_output` 的提前返回分支）
    - `scripts/tests/test_audit_verdict.py`：通过子进程覆盖 `main()`（stdin/stdout）和 `if __name__ == "__main__"` 块
    - **新代码覆盖率**：75.5% → 约 98%（translate.py 为 98%，scripts/audit_verdict.py 为 97%）
  - **测试**：`tests/test_translation_note_position.py` 覆盖位置 × 格式矩阵（包括端到端测试 `marker+top|bottom|both` 和 `legacy+top|bottom|both`）、多行前缀处理、逐字节向后兼容性（黄金字面量）、清理器、frontmatter 拆分（包括未关闭围栏时抛出异常）、三段式格式、两段式回退、单段 + Markdown 链接防护，以及关键保护测试 `TestLLMPayloadExcludesInvariants`，用于断言标题和 URL 绝不会发送给 LLM。**190 项测试通过**，0 项回归。
  - 文档：`README.md`（法语 + 14 种翻译），包含徽章；`CLAUDE.md`（pre-commit 工作流 + 详细的 CI 监控说明）；重新生成 28 份翻译
- **1.8** `--news` 模式 + 2026 模型升级（2026-03-17，标签 `v1.8`）：
  - 更新默认模型（2026 年 3 月）：
    - OpenAI 高质量模式：`gpt-5` → `gpt-5.4`
    - OpenAI 经济模式：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 高质量模式：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - 为 `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）和 `gemini-3.1-pro-preview`（1M）新增 token 限制
  - 初始 `--news` 模式：使用占位符 `#NEWSQUOTE\d+#` 保护英文引文、`LANG_FLAGS` 映射（15 种语言）、按目标语言管理标志
  - 在恢复之前验证新闻占位符（回归问题：LLM 删除占位符时会静默生成缺少引文的输出）
  - 使脚本 `regen_translations.sh` 可移植（使用绝对路径，不依赖 pwd）
  - 在 README/CHANGELOG 的语言栏中添加法语链接，并重新生成 28 份翻译
- **1.7** 新增功能：
  - 新增 `--keep_filename` 选项，可在翻译时保留原始文件名
  - 支持通过 `.env` 文件自动加载 API 密钥
  - **保留行内代码**：翻译期间现在会保护反引号（`` `...` ``）
  - 改进系统提示词：
    - 更好地处理 YAML frontmatter 中的引号
    - 保护模板变量 `{variable}`
    - 禁止添加未经请求的译者说明
  - 已在 364 个文件上成功测试（jls42.org 博客迁移）
- **1.6** 新增功能：
  - 支持使用 Google Gemini API 进行翻译（`--use_gemini`）
  - 更新 2026 年默认模型：
    - OpenAI：`gpt-5`（高质量）、`gpt-5-mini`（经济）
    - Claude：`claude-sonnet-4-5`（高质量）、`claude-haiku-4-5`（经济）
    - Gemini：`gemini-3-pro-preview`（高质量）、`gemini-3-flash-preview`（经济）
  - 经济模式（`--eco`），用于采用速度更快、成本更低的模型
  - 单文件翻译（`--file`），无需遍历目录
  - 新的简化命名模式：`{base}-{lang}.md`
  - 新增 `--include_model` 选项，用于保留包含模型名称的旧格式
  - 支持未列出的模型，并采用默认 token 限制（128k）
  - README 已翻译成 14 种语言
- **1.5** 改进：
  - **更新 API 密钥和默认模型：**
    - **OpenAI：** 从 `DEFAULT_MODEL_OPENAI` 更新至 `"gpt-4o"`。
    - **Mistral AI：** 从 `DEFAULT_MODEL_MISTRAL` 更新至 `"mistral-large-latest"`。
    - **Anthropic Claude：** 新增 `DEFAULT_ANTHROPIC_API_KEY`，并将 `DEFAULT_MODEL_CLAUDE` 更新至 `"claude-3-5-sonnet-20240620"`。
  - **优化翻译提示词：**
    - 丰富了直接翻译和翻译说明所用的提示词，以提升清晰度和效率，其中包括有关保留元数据及特定格式元素的详细指令。
  - **代码重构：**
    - 使用 `Mistral` 类替代 `MistralClient`，以初始化 Mistral AI 客户端。
    - 重新组织 import，以提高可读性和可维护性。
    - 改进文本分段和代码块处理，以便在翻译时保留原始格式。
  - **输出文件管理：**
    - 在输出文件名中对调模型和语言的位置（例如 `f"{base}-{args.target_lang}-{args.model}.md"`），从而更便于整理和查找翻译。
  - **其他改进：**
    - 删除不必要的空行以清理代码。
    - 进行细微调整，以改进脚本结构和可读性。
- **1.4** 新增功能：
  - 支持使用 Anthropic Claude API 进行翻译
  - 优化提示词，以提升清晰度和效率
  - 进行细微调整，以提高代码可维护性
- **1.3** 改进与新增功能：
  - 改进代码块处理
  - 改进输出文件管理
  - 改进现有文件检测
  - 新增 `--force` 选项以强制翻译
  - 在输出文件名中对调模型和语言的位置
- **1.2** 修复变更日志
- **1.1** 新增 Mistral AI API 支持
- **1.0** 初始版本——支持 OpenAI API

**使用 gpt-5.6-sol 将文章从法语翻译成中文。**
