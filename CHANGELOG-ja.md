### 変更履歴

🌍 [フランス語](CHANGELOG.md) | [英語](CHANGELOG-en.md) | [スペイン語](CHANGELOG-es.md) | [中国語](CHANGELOG-zh.md) | [ドイツ語](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [韓国語](CHANGELOG-ko.md) | [アラビア語](CHANGELOG-ar.md) | [ヒンディー語](CHANGELOG-hi.md) | [イタリア語](CHANGELOG-it.md) | [オランダ語](CHANGELOG-nl.md) | [ポーランド語](CHANGELOG-pl.md) | [ポルトガル語](CHANGELOG-pt.md) | [ルーマニア語](CHANGELOG-ro.md) | [スウェーデン語](CHANGELOG-sv.md)

- **1.13.0** provider `--use_openrouter`：中国製オープンモデルを含む約430モデルへの有料ルーター（2026-09-05）：

  - **8番目と同時に提供される、9番目のprovider経路。** 1.12.0はPyPIで公開されませんでした。OpenCodeとOpenRouterの2つのルーターを同時にリリースします。[OpenRouter](https://openrouter.ai)では、ほかのどのproviderもここでは提供していないKimi、Qwen、DeepSeek、Z.aiなどのモデルへ、従量課金される単一のクレジットと1つのキーでアクセスできます。endpointはOpenAI互換なので、clientはxAIと同じです。**このproviderを区別する要素はすべてpreflightに集約されており、その各ルールはAPIでの測定結果に基づいています。**

  - **同一モデルが上限の異なる数十のホスティング事業者から提供されていますが、ルーティングはそれを考慮しません。** 測定結果：`z-ai/glm-5.2`では33事業者、`z-ai/glm-5.3-flash`では23事業者で、そのうち1事業者の**出力上限は2,048 tokens**でした。そのため、23事業者のいずれかへ送られる長文翻訳は、何の通知もなく無作為に途中で切れていました。preflightは`/api/v1/models/{modèle}/endpoints`を読み取り、出力上限が8,000 tokens未満の事業者、ステータスが低下している事業者、上限を申告していない事業者を除外して、残りを固定します。`allow_fallbacks: false`を伴わない`provider.only`は単なる優先指定です。ルーターは除外した事業者へ戻るため、固定は無意味になります。上限を満たす事業者がなければ、コマンドは停止します。それでも翻訳を続けることは、このpreflightが防ぐために存在する無通知の切り捨てを受け入れるのと同じだからです。

  - **推論は出力と同じ料金で課金され、多くのモデルで既定で有効です。** `z-ai/glm-5.2`へ同じリクエストを送り、応答を「OK」とした場合、**モデルの既定設定ではcompletionが107 tokens、推論を無効にすると2 tokens**でした。推論が何の役にも立たない翻訳では、各ファイルの各segmentで18倍の差になります。そのため、既定では無効にしています。推論を必須とする**431モデル中288モデル**（`reasoning.mandatory`）は`400 « Reasoning is mandatory for this endpoint and cannot be disabled »`と応答します。これらについては、preflightが受け入れ可能なeffortを読み取り、最も低いものを要求します（次項）。effortは、推論が最初に消費する**`max_tokens`の割合**を割り当てるため、値を無作為に選ぶと、空白ページになるリスクを減らすのではなく移動させるだけです。

  - **推論を必須とするモデルには、そのモデルが受け入れる最小のeffortを指定します。これは測定に基づく決定です。** 当初は、モデルに代わって推測しないよう、何も送信しない方針でした。catalogの既定値が`max`である`z-ai/glm-5.3-flash`で検証したところ、この方針では翻訳完了前に出力が**32,768 tokensで切り捨てられ**、14言語中2言語が失われました。envelopeを増やしても変わりません。effortがその一定割合を割り当てるため、推論もenvelopeとともに増えるからです。そのためproviderはpreflightで`supported_efforts`を読み取り、最小値を要求します。catalogに利用可能な値が示されていない場合は「指定なし」へfallbackします。問題が起きた言語で反証したところ、以前はbudget枯渇で失敗していましたが、現在はソースと同一の構造を保ったまま9分で完了します。

  - **上流ホスティング事業者の障害に、その名前が表示されるようになりました。** ルーターはこのケースを、`native_finish_reason`がnullの`finish_reason=error`へ正規化します。2言語で2回測定したところ、いずれも正確に750秒でした。従来の一般的なメッセージでは、文書や分割方法の不具合を探すことになっていました。今後は障害がprovider側にあり、多くの場合は再試行で解決すると伝えます。

  - **出力が空の`finish_reason=length`は切り捨てではありません。** これは最初の有用な文字が出る前に、推論がbudgetを使い切った状態です。測定では、有用な148 tokensに対して推論が15,850 tokensでした。この2つのケースでは必要な対処が逆になります。前者ではsegmentを小さくしても意味がありません。メッセージで両者を明確に区別するようにしました。測定結果から、さらに2つのguardを追加しました。上流ホスティング事業者が失敗した際、ルーターが**エラーだけを含むbodyを200で返す**場合があり（`choices[0]`はメッセージを覆い隠す不透明な`TypeError`を発生させていました）、またcontext windowをcatalogから読み取って`MODEL_TOKEN_LIMITS`へ記録するようにしました。catalog内の44モデルでは`DEFAULT_TOKEN_LIMIT`が誤っており、そのうち2モデルの上限は4,095 tokensです。

  - **`--model fournisseur/modèle`は必須であり、その形式はネットワークへ接続する前に検証されます。** OpenRouterは単なる供給元ではありません。この選択には価格、ライセンス、データ処理が関わるため、ユーザーに代わって決めることはできません。slugはpreflightのURLへ挿入されるため、検証は単なる使いやすさへの配慮ではなく、pathの挿入を防ぐguardです。2つのルーターで共通のnamespace付きregexは`a/b/..`を受け入れるため、親segmentを明示的に拒否します。`--eco`は効果がなく、その旨を通知します。

  - **3つの表現を修正し、そのうち1つは誤りでした。** `codex exec`に関するOpenAIの警告は、共有runnerへ個人のsessionファイルを挿入することを対象としており、repositoryが公開されていることを問題にしたものではありません。README、CLAUDE.md、codeでは意味を取り違えて引用されていました。OpenCodeの認証情報の保存場所は1.18.27で変更され、`auth.json`ではなく`opencode.db`の`credential` tableになりました。「ここでは決して読み取らない」という不変条件は正しいままでしたが、場所の記載が古くなっていました。最後に、OpenCodeのsectionでは、検証されていない経路を同等のものとして紹介しないようにしました。Zen gatewayとOllamaはend-to-endで測定済みですが、GitHub Copilot、LM Studio、llama.cppは未測定であり、READMEにもそのように記載しています。

  - **測定キャンペーンと、README内の推奨モデル一覧表。** 3種類の文書セットを14言語へ翻訳し、300回を超える翻訳を実行しました。`--news`モードの情報密度が高いblog記事、このREADMEの標準Markdown、そしてGitHub上の著名なprojectからそのまま取得した4つのREADMEです。この表では、これまで混同されていた2つの要素を区別しています。翻訳が**完了する**ことと、翻訳後の**構造がソースと同一である**ことです。情報密度の高い2文書で一度も情報を失わなかったモデルは3つでした。`gemini-3.7-flash`、ChatGPT subscriptionの`gpt-5.6-sol`、OpenRouter経由の`z-ai/glm-5.2`です。唯一の差異は、1言語または2言語で`**`の対が1組再現されなかったことです。中心的な結論は、**差を生む要因が`--news`モードではなく、文書の情報密度である**ということです。subscription経由のGrokはblog記事では14回中13回失敗した一方、公開READMEでは16回中14回成功しました。原因は長いsegmentでの脱落であり、反証によって確認済みです。表自体にも注意事項があります。網羅的ではなく、特定時点の結果であり、所要時間は順位を示すものではありません。最善の方法は、引き続き自分の文書で測定することです。

  - **構造比較器が非ラテン文字体系で2件のfalse positiveを生じさせていたため、数値の公開前に修正しました。** URLの後ろに全角閉じ括弧`）`が続く場合、`)`で停止するregexではURLが正しく切り離されず、URL自体は同一でも抽出された文字列が異なっていました。また、フランス語では5行の引用が中国語では3行に収まり、行単位の集計値が減少していました。両方の修正は反証で検証済みです。URL、section、inline codeのいずれかを削除すれば、引き続き検出されます。この修正がなければ、GeminiとCodexの結果は14言語中それぞれ13言語と12言語ではなく、どちらも11言語として公開されていたはずです。

  - **テスト**：新規ファイル`tests/test_openrouter_provider.py`（76 tests）— modelの検証と親segmentの拒否、ホスティング事業者の固定（上限、ステータス、未申告の上限、共通の最小値）、常にfalseとなる`allow_fallbacks`、`mandatory`に応じた推論の無効化または維持、完全な出力contract（200内のエラー、choiceなし、空白ページと切り捨ての区別、異常な`finish_reason`、null content）、catalogへ接続できない場合のfail-closed preflight、slug欠落と正常なホスティング事業者の不在、flagの排他性、filename label。全suiteは**502 tests**です。

  - **refactor：4,253行の単一moduleを、挙動を一行も変更せず複数moduleへ分割しました。** `src/aipmt/translate.py`を`config`、`markdown`、`segmentation`、`guards`、`placeholders`、`news`、`prompts`、`notes`、`naming`、`pipeline`、`cli`、およびsubpackage `providers/`へ分割しました（providerごとに1 module、基盤として`base`、解決とdispatchに`registry`）。各移動は個別のcommitであり、機械的に検証されています。verifierはpackage内のすべてのtop-level nodeのASTをreference snapshotと比較し、各symbolの配置、安全性markerがverbatimで残っていること、untracked fileがないことを確認します。この一時的なtoolingは次のversionで削除されました。目に見える変更点として、`aipmt.translate`はfacadeとなり、従来moduleが`_` prefixなしで公開していた64個の名前をobject identityを保ったまま再公開します（`__all__`には、そのうちsupport対象APIの9個があります。残りは互換性aliasです）。また、`import *`がまとめて拾っていたdependencyおよびstandard libraryの29個の名前は再exportしなくなりました。ファイルの直接実行（`python src/aipmt/translate.py`）は廃止され、`aipmt`と`python -m aipmt`が引き続きsupport対象の2形式です。public functionの`__module__`は、それぞれの定義moduleを示します。SDKは`.env`の読み込み後にimportされるようになりましたが、既知の影響はありません。427 testsはidentifierまでそのまま維持し、対象moduleへ移行しました。facade経由だった91個のpatchは、名前を参照するmoduleを直接対象とするようになりました（そのうち2個はpatchがなくてもgreenのままだったことを測定済みです）。7個のcontract testでfacadeを固定し、検証をやめたことでgateがgreenになることを防ぐため、gate toolingは最初の移動より前に書き直しました。directory単位かつfloor付きのLizard scope、構築済みparserからのflag読み取り、package単位のcoverage floor、tracked moduleを列挙する`release.sh`が含まれます。
  - **修正（pull requestレビュー）**：OpenRouterは`context_length`のないcatalog entryを拒否し、128,000 tokensという既定値を測定値として記録しないようになりました。この誤った記録によって、「modelが一覧にない」という警告まで表示されなくなっていました。また、`finish_reason`がnullの場合（文書化されたtypeは`string | null`）、`max_tokens`が`length`となるため、ホスティング事業者のraw reasonを正とします。choice自体に含まれるエラーは、同時に添えられたpartial contentを拒否し、正規化された上流障害と同じメッセージを表示します。ホスティング事業者の詳細、raw reason、助言を1つにまとめています。OpenCodeは`part: null` eventに対して`AttributeError`ではなくcontract errorを返し、eventの1行が読み取れないJSONL streamはpartial textを受け入れず拒否します。3つのagentic CLIは、呼び出し中にprocessが`SIGTERM`を受け取った場合、agentのprocess groupを終了します。regenの`timeout`ではagentが生き残ってquotaを消費し続けていました。また、groupの`SIGKILL`は常にgrace periodに従い、正常終了するshimがgrandchildを生存させることはありません。分割によって離れていた`# fmt: off`と`# fmt: on`の対を再結合しました。`--reasoning_effort`のhelpには、それを使用する4つのproviderを明記しています。
  - **修正（2回目のレビュー）**：OpenRouterへ要求する出力上限で、promptとsegmentがcontext内で占める分を確保するようになりました。`context_length`は入力とcompletionの**両方**を対象としており、catalog内の6モデルでは入力を収める余地がないままrequestが送信されていました。contextが短すぎる場合は、課金前に拒否します。agentic CLIの基盤は、POSIX process groupが存在しない環境では`terminate`、続いて`kill`へfallbackし、`AttributeError`をtimeout guardから通過させて待機が長引くことを防ぎます。OpenCodeの`429` markerはsubstringではなく数値として検索されるようになり、`err_84290b`のようなerror identifierによって、結局失敗する前に90秒のback-offが発生することはなくなりました。最後に、canonicalでないOpenRouter endpointをpreflightで表示します。projectの`.env`だけでendpointを設定でき、その後は実際のキーがそこへ送信されるためです。
  - **セキュリティ：projectの`.env`からAPI callをredirectできないようにしました。** `find_dotenv(usecwd=True)`はcurrent directoryとそのparentからファイルを検索します。そのため、信頼できないdirectory tree、たとえばcloneしたばかりのrepositoryに、キーを一切知らなくても`OPENROUTER_BASE_URL`、`XAI_BASE_URL`、または`OPENAI_BASE_URL`（最後のものはSDK自体が読み取ります）を配置でき、environmentまたはuser configurationから取得した実際のキーが第三者serverのauthorization headerへ送信される可能性がありました。filterはリストではなくPATTERNに基づきます。インストール済みSDKを調査すると、12個のrouting variableが読み取られており、そのうち6個はAnthropic clientだけで使用されていました。手作業の列挙では半分を見落としていたはずです。そのため、project layerでは、`_BASE_URL`、`_API_BASE`、`_ENDPOINT`に一致するすべてのvariable、proxy、certificate store（管理下にある認証局を指定すると、interceptorを正規serverと区別できなくなります）、さらに`XDG_CONFIG_HOME`と`APPDATA`を拒否します。これらの指定は、どのファイルをuser layerとするかを決めることに等しく、filterを迂回できるためです。これらのvariableは、ユーザーが管理する2つのlayer、export済みenvironmentと`~/.config/aipmt/.env`からのみ受け入れます。さらに、project layerはinterpolation**なし**で読み取ります。`load_dotenv`は既定で`${VAR}`を展開するため、`NOM_ANODIN=${OPENAI_API_KEY}`を含む信頼できない`.env`が、subprocessのpattern-based filterでは認識されない名前へ実際のキーを複製できました。そのキーは`codex exec`のenvironmentへ入り、明示された不変条件に反していました。最後に、拒否時にはvariable名だけを表示します。`https://${CLE}@hôte/`形式のURLでは、拒否しているにもかかわらず、interpolateされたキーがlogへ漏れていました。拒否はstderrへ出力され、対処方法も示します。企業用relayはuser configurationで指定します。
  - **修正：OpenRouterの出力envelopeをcallごとに計算します。** `context_length`は入力とcompletionの**両方**を対象とするため、ラテン文字textを基準に調整された固定reserveでは何も保証できません。`o200k_base` tokenizerで測定すると、16,000文字はフランス語で3,200 tokens、日本語で12,300 tokens、emojiで17,500 tokensでした。そのためbudgetは実際に送信するtextから算出し、そのUTF-8 byte数で上方補正します。catalogで使用されるbyte-fusion tokenizer、すなわちbyte-level BPEやbyte fallback付きSentencePieceでは、1 tokenは少なくとも1 byteに相当します。OpenRouterが未知の数十種類のtokenizerへrouteするこの環境では、これが利用可能な唯一の上方補正です。平均ratioは使用できませんでした。追加面のideographでは1 tokenあたり1.33 bytesまで下がり、combining characterでは1.00 byteになります。これにより、入力と出力の合計が構造上必ずwindow内に収まるようになりました。選択したmodelに対してsegmentの密度が高すぎる場合は、課金後ではなくcall前に拒否します。

- **1.12.0** provider `--use_opencode`：オープンソースagentのOpenCodeから、任意のproviderへ接続—local model、アカウント不要の無料利用、subscription、またはキー（2026-09-04）：
  - **最初の7つとは性質の異なる、8番目のprovider経路。** [OpenCode](https://opencode.ai)（MIT）はモデルproviderではなく、ユーザーがOpenCode自体に設定したものへの_ルーター_である。対象はAPIキー、サブスクリプション（GitHub Copilot、ChatGPT、SuperGrok）、**アカウント不要**で無料モデルを提供するOpenCode Zenゲートウェイ、または**ローカル**モデル（Ollama、LM Studio、llama.cpp）。スクリプトはCodexやGrokと同様に、非対話モードで`opencode run`を制御し、同じサブプロセス基盤（専用process group、timeout時に`SIGTERM`、続いて`SIGKILL`、stdinは常に閉じ、環境変数を除去）を再利用する。**2件の実際の翻訳**で検証済み。このREADME全体を`opencode/mimo-v2.5-free`で英語化し、49秒、1回の処理で、ソースファイルと同一の構造（見出し32件、コード終了記号26件、リンク18件、URL 37件、表37行、inline code 135件）を維持したほか、テストファイルを`ollama/qwen2.5:7b`で、ローカルかつキーなしで翻訳した。

  - **`--model provider/modèle`は必須であり、これは意図的な選択である。** `--model`がない場合、OpenCodeは自身のデフォルトへフォールバックする。新規インストール時のデフォルトは`opencode/big-pickle`で、やり取りが学習に使用される可能性のある無料の「stealth」モデルである。実測でも、このモデルが応答した。ユーザーに代わって暗黙にこれを選ぶことは、このリポジトリが追跡する見えない切り替えそのものになる。そのためエラーメッセージには、モデル一覧を表示するコマンド（`opencode models`）と、ローカル、無料、サブスクリプションの3例を明記している。`--eco`は効果がなく、その旨を通知する。`--reasoning_effort`は、明示的に要求された場合に限り、OpenCodeの`--variant`としてそのまま渡される。

  - **想定ではなく、実測された隔離。** inline設定（`OPENCODE_CONFIG_CONTENT`。OpenCodeのマージ順で最後に位置するため、ユーザー設定を置換せずに優先される）では、すべてのツールを拒否する（`permission: {"*": "deny"}`）agent `aipmt`を定義する。registryからモデルへのツール提示自体がなくなり、「ファイルを一覧表示して`id`を実行せよ」と命じても、ツールがないと応答する。session共有を無効化し、外部pluginを除外し（`--pure`）、`--auto`は一切使用せず、作業ディレクトリは使い捨ての空ディレクトリとする。暗黙に行われる2種類の注入を実測し、遮断した。`OPENCODE_DISABLE_CLAUDE_CODE`がないと、ユーザーの`~/.claude/CLAUDE.md`が**すべての**promptに入り、単純な「こんにちは」だけでも入力が186 tokensではなく515 tokensになる。`OPENCODE_DISABLE_PROJECT_CONFIG`がない場合は、カレントディレクトリの`AGENTS.md`も入る。「各応答の末尾をBANANAにせよ」という指示が翻訳に適用された。globalの`~/.config/opencode/AGENTS.md`は引き続き注入される。これを除外するswitchはなく、転用した`XDG_CONFIG_HOME`で回避するとユーザーのproviderまで隠れてしまう。場当たり的に細工せず、この制約を文書化した。

  - **`exit 0`は何も証明しない。3つ目のCLIにも同じ慎重さが必要であり、さらに固有の罠が2つある。** 未知の`--agent`でも`opencode run`は失敗しない。stderrに警告を出し、ツールが有効なcoding agentへ**暗黙に**フォールバックする。inline設定が反映されていなければ、翻訳は書き込み可能なagentで実行されてしまう。そのため出力contractでは、このメッセージがないことに加え、終了コードが0、`error`イベントなし、`tool_use`なし、最後の`step_finish`が`stop`であること（`length`は応答が切り詰められている）、テキストが空でないことを検証する。2つ目の罠は、エラーのJSONイベントが**不透明**なことだ。単なる参照情報とともに「予期しないサーバーエラーです。詳細はサーバーログを確認してください。」としか表示されず、実際の原因（`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`、`ProviderAuthError`など）はログにしか存在しない。このため`--print-logs --log-level ERROR`を使用し、その後に続くBunのtraceを除外してstderrの`error="…"`フィールドを読む。これにより未知のモデルは、原因を明示して1秒で失敗する。さらに`--title`は不要なLLM呼び出しを回避する。これがないとOpenCodeは`small_model`に対する追加の1回のturnでsessionタイトルを生成する。

  - **secret：CodexおよびGrokと同じパターンベースのフィルタリングを行うが、明示的な例外が1つある。** `OPENCODE_API_KEY`は保持される。これはOpenCode自身のキー（Zenゲートウェイ、Goサブスクリプション）であり、名称どおりOpenCode宛てのものだ。OpenCodeの`auth.json`に相当し、aipmtが管理または課金できるキーではない。providerはOpenCode内（`opencode auth login`、`opencode.json`）で設定し、aipmtの`.env`では一切設定しないため、aipmt側のキーがサブプロセスに届くことはない。サブスクリプション型CLIとは異なり、CIでは拒否しない。runner上でAPIキーやself-hostedモデルを使用することは正当なユースケースだからである。

  - **traversal防止guardは、raw値ではなくinterpolate後の値を検査するようになった。** `provider/modèle`には、1.10.0のguardが拒否していた`/`が含まれる。この拒否自体は妥当で、`--model`がファイル名`--include_model`へinterpolateされるためである。ファイル名labelでは、interpolate前に`/`、`\`、`:`を`-`へ置換するようになった（`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`。`:`はWindowsでは不正）。上流のguardはこのlabelを検査する。その結果、`../../evil`は出力先配下の単純な名前`doc-en-..-..-evil.md`となり、`..`単体は引き続き拒否され、`--target_lang ../x`も拒否される。scope guardの`_ensure_within_directory`は、変更なく第2層として維持される。

  - **無料モデルとローカルモデルの実測結果。** `opencode/mimo-v2.5-free`は1段落を16秒、このREADMEを49秒で翻訳する。`opencode/big-pickle`は200語に40秒かかり、同時に送った2件のリクエストは、それぞれ単独なら完了するにもかかわらず、5分間応答がなかった。`opencode/nemotron-3.5-lightning-free`は3分間まったく応答しなかった。このため`REGEN_PROVIDER=opencode`では`REGEN_MODEL`を必須とし、並列数を**2 jobs**としている。ローカル側では、segmentが最大16,000文字ある一方、Ollamaのcontextは4,096 tokensに設定されていることが多い。そのため`PARAMETER num_ctx 32768`を指定した`Modelfile`が必要であり、品質はモデルに依存する。テストファイルでは、7Bモデルがリストの順序を逆転させ、コードブロックの終了記号を壊した一方、ゲートウェイのモデルはすべてを保持した。

  - **このリポジトリの翻訳が、従量課金APIを経由することは今後一切ない。** `regen_translations.sh`は、`.env`にキーが残っているだけでOpenAI APIを使用し、Codexはopt-inにすぎなかった。このversionの準備中にも、まさにそれが起きた。28件の翻訳がOpenAI APIへ送られ、その後Hindi版CHANGELOGがGemini APIへ送られた。ChatGPTサブスクリプションは、まさに従量課金を避けるために存在するにもかかわらずである。キーの自動検出は廃止する。**デフォルトは品質重視モデルを指定したCodex、すなわち`gpt-5.6-sol`**となる。`openai`、`gemini`、`grok`には、`REGEN_PROVIDER`に加えて`REGEN_ALLOW_PAID_API=1`が必要になる。これは、判断時点で規則が確実に適用されるよう明示的に名付けた例外許可である。未知の`REGEN_PROVIDER`はAPIへフォールバックせず失敗する。10件のテストで、デフォルト、拒否、例外許可を固定した。このversionの28件の翻訳はCodexでやり直した。

  - **rate limit時のback-offを共通化**した（`_retry_on_rate_limit`）。CodexとGrokのloopはlabel以外が同一であり、3つ目のコピーを追加すると重複の閾値を超えてしまうためである。3種類のCLIエラーは同じ`_CliCallError`を継承する。いずれかがこの継承から外れると共有loopで検知できなくなるため、それを禁止するテストを追加した。

  - **テスト**：新規ファイル`tests/test_opencode_provider.py`（61 tests）。完全な出力contract、agentのフォールバック、ログからの原因取得、重複したtext partの排除とsynthetic partの無視、timeout時のprocess group終了、429へのback-off、モデルの必須化と検証、secretなしのpreflight、binary解決、dispatch配線、ファイル名label、traversalの反証を対象とする。`tests/test_review_hardening.py`では、flagの排他性とsecret不在の検証を新しいproviderへ拡張した。gateは現在、文書化されたargparseの**22 flags**を要求する。全suiteは**382 tests**。

- **1.11.1** ドキュメント修正：READMEがようやく7つのprovider経路を明記（2026-09-03）：

  - **1.11.0のPyPIページには「4 APIs + Codex CLI」と記載されていた。** 実際のコードでは7つを提供する。API経由のOpenAI、Mistral、Claude、Gemini、Grokに加え、従量課金なしでサブスクリプションを利用するCodex（ChatGPT）とGrokである。冒頭文と_Multi-Provider_の箇条書きにはGrokの2モードが欠けており、14件の翻訳でも誤りが繰り返されていた。packageのlong descriptionはversionごとに固定されるため、公開ページを修正するには新しいversion番号が必要だった。これが今回のversionの唯一の存在理由である。**コード変更はない。**
  - `CLAUDE.md`を公開時に導入された内容と一致させた。gateのcounter（`--full`では16、17）、稼働中の11 workflows、`gh pr checks`には表示されないSonar/Codacyの2つのcounter（hotspots、Codacy API）、`ruff-format`による`# nosemgrep`の移動、OIDC交換に必要なGitHub environments、そして_pending publisher_は名前を予約しないという事実を反映した。

- **1.11.0** PyPIへの公開：リポジトリをcloneせず、`pip install ai-powered-markdown-translator`に続いて`aipmt`を実行（2026-09-03）：

  - **単一ファイルのスクリプトがinstall可能なpackageになった。** `translate.py`をrootから`src/aipmt/translate.py`へ移動し、console entry point `aipmt`と、それに相当する`python -m aipmt`を提供した。貢献するには引き続きリポジトリのcloneが必要である。tests、28件の翻訳、品質管理toolingがそこに含まれるためだ。ただし、利用するだけなら不要になった。

    - **import名は`aipmt`であり、決して`translate`ではない。** 実際に発生し、しかも表面化しない衝突があるためだ。PyPI package `translate`（v3.8.1、最終upload 2026-07-06）は同名のディレクトリをinstallする。venv内で再現したところ、ディレクトリがmoduleより優先され、`translate.main`が消え、entry pointは`AttributeError`で壊れた。それでも`pip check`は「壊れた依存関係は見つかりませんでした」と応答し、rc=0となる。ユーザーが単に`pip install translate`を持っているだけで、利用可能な診断情報もなくCLIが壊れる状況だった。実際のwheelによる反証では、そのpackageの上に`pip install translate`を重ね、前後どちらも`aipmt --help`がrc=0となり、2つのCLIが共存することを確認した。
    - **長いdistribution名、短いcommand。** `ai-powered-markdown-translator`により、packageをPyPI検索で見つけられる。略語だけでは、そのprojectをすでに知っている人以外は検索できず、公開の目的はまさに発見可能にすることだからである。有力な候補2つは確認のうえ除外した。`ai-markdown-translator`は、同じ目的のtoolによって2024年からnpm上で使用済みであり、このリポジトリより17か月先行している。`aimt`は、同じ分野で現在も活動中のpackage `aim`（v3.29.1）と1文字しか違わず、長期的な混同を招く最悪の条件だった。確認方法にも罠がある。`pypi.org/project/<nom>/`はどの名前でも200を返すbot対策ページであり、信頼できるのはJSON APIだけである。
    - **flat packageではなく`src/` layout。** flat packageならtests内の6つの`sys.path.insert(..., "..")`を保持できたが、それこそが問題だった。それらはpackageではなくsource treeをimportするため、packagingの誤りがすべて隠れてしまう。実際のコストは、置換規則が1つ増えるだけである。

  - **キーをようやく一度だけ設定すれば済むようになった。** install済みCLIには永続的な設定手段がなかった。残されていたのは環境変数とカレントディレクトリの`.env`だけである。確かに`find_dotenv`はsystem rootまで遡るため、**home directory配下で作業している場合**には`~/.env`を見つけられた。しかし、それ以外の場所で作業すると何も見つからない。つまり設定の有効範囲が設計上の選択ではなく、commandの実行場所に依存していた。そこで既存の2層の下に、第3層として`~/.config/aipmt/.env`を追加した。

    - **優先順位は明示的なコードではなく**、`load_dotenv`のデフォルト値である`override=False`から生じる。各層は、前の層で空のまま残された値だけを補う。このため優先順位は、環境変数 → projectの`.env` → ユーザー設定となる。これは構造ではなく**動作**のテストで検証しており、2つの呼び出し順を逆にしても、第3層を削除しても失敗する。
    - **意図的にTOMLではなく`.env`形式を採用した。** `python-dotenv`はすでに依存関係に含まれ、その構文は15件のREADMEですでに文書化され、同じファイルを両方のscopeで利用できる。新しい依存関係も構文も増えない。保存場所は、`XDG_CONFIG_HOME`が**absolute**である場合に限りそれに従い、Windowsでは`APPDATA`に従う。仕様上、relative値は無視する必要がある。そうしなければ設定場所が再びカレントディレクトリ依存になるためである。
    - **2つの選択肢を理由とともに除外した。** system keyring（`keyring`）はdesktop環境ではより安全だが、headless環境、すなわちserver、container、CIでは失敗する。これは一括翻訳そのもののユースケースであるため、opt-inには適していてもデフォルトには適さない。`--api-key` flagを使うとキーがshell historyに残り、`ps`から見えるようになる。
    - **キーがない場合、call traceを表示しなくなった。** 従来は`site-packages`を指すPython stack traceと、「環境または.env」とだけ述べ、後者をどこに作成すべきか示さないメッセージが表示されていた。現在は3つの保存場所と、それぞれの正確なpathを列挙し、commandは終了コード2で終了する。防護範囲は**意図的に狭く**、設定段階のみを`except ValueError`で囲む。実行全体を包むと、翻訳中に発生した本物のbugまで安心感を与えるメッセージへ変換してしまう。このリポジトリが追跡する失敗形態そのものである。`main()`のsourceを読み、その実装を禁止するテストを追加した。

  - **修正 — toolをinstallするとユーザーの`.env`が無視されていた。** 引数なしの`load_dotenv()`はカレントディレクトリからではなく、呼び出し元ファイル、つまり`site-packages`から上へ遡る。独自の`.env`を持つprojectから実際のconsole entry pointを起動して測定したところ、`find_dotenv()`は`''`を返してキーを読み込まず、`find_dotenv(usecwd=True)`ならキーを見つけた。toolをclone済みリポジトリからしか実行していなかった間は存在しなかったbugだが、公開後には必ず発生し、正しい設定でもAPIキーが「不足」しているように見えることだけが症状になっていた。

  - **3つのgateは、何も検証しなくなったにもかかわらずgreenになっていた可能性がある。** 意図的に、移動より**前に**それらを強化した。捕捉対象の変更後に書かれたguardでは何も証明できないためである。各gateは元のリポジトリではgreenとなり、移行済みのコピーではredになる。両方向を実測した。

    - **Lizardは存在しないpathを何も言わず無視する**。rc=0で「0 file analyzed」となる。complexity gateは、158 functions / 2247 nlocから3 functions / 34 nlocへ減少し、出力は0 bytesになっていたはずである。現在scopeは配列となり、各entryの存在を検証する。
    - **存在しないmoduleに対する`coverage run --source=`は失敗しない**。unittestでも`coverage xml`でもstderrへの警告だけでrc=0となり、reportもそのまま公開される。statementsは1453から141へ削減され、ほとんど解析されていないためにprojectが健全に見えてしまう。reportはtotalと測定された最大ファイルという2つの下限でguardする。
    - **翻訳のfreshness probeは、構造上、呼び出し形式を認識できない**。argparse flagsを基準にしているが、ファイル名を変更してもflagsは変わらないためである。再現では、moduleを移動し、15件のREADMEが存在しないcommandを記載したままでも、判定は「古い翻訳なし」だった。このため第7のsectionではoptionsではなく**形式**を検証し、Lizard hookをscriptの実際のscopeと照合する。そのkeyである`files:`は、一致しなくてもpre-commitを失敗させず、hookを**スキップ**させるためである。
  - **`requires-python = ">=3.10"` は主張であることをやめました。** `sonar-project.properties` は、これまで一度も実際に検証されていないにもかかわらず、すでに 3.10～3.12 を掲げていました。開発環境には 3.12 しかなく、公開すれば露呈していた内部矛盾です。現在はテスト workflow が 3.10、3.11、3.12 で一式を実行し、パッケージ自体をインストールすることで、公開されているバージョン境界も検証します。

  - **下限のみ、上限なし。** `requirements.txt` はテスト済みの lock のまま維持し、`[project.dependencies]` を公開契約とします。lock の正確なバージョンを公開すると、ほかのパッケージも利用するすべてのユーザー環境で競合が発生するためです。`<N+1` の上限も設けません。これは、メジャーバージョンの遅れがあると release gate を失敗させる `check-deps-fresh.sh` と真っ向から矛盾します。設定した下限の組み合わせでは解決に成功し、反証ケース `openai==1.0.0` は `ResolutionImpossible` で終了します。つまり、このチェックはすべてを受け入れるのではなく、適切に判別できています。さらに、`pyproject.toml` のバージョンが CHANGELOG のバージョンと食い違うことを防ぐガードも追加しました。PyPI では同じバージョン番号を再利用できません。

  - **新しい venv でエンドツーエンド検証済み**：約 70 Ko の wheel に含まれるのは `aipmt/*.py`、dist-info、ライセンスのみです。`aipmt --help` は 22 個の flag で rc=0、`python -m aipmt` は「usage: \_\_main\_\_.py」ではなく「usage: aipmt」と表示し、`pipx` によるインストールも正常に動作します。そして何より、**任意のユーザーディレクトリから実際に fr→en 翻訳を実行**し、太字、リスト、inline code、リンク、URL が保持され、code block が翻訳されないことを確認しました。移行前から存在する 318 件のテストは、前後で byte 単位まで同一の識別子リストを保ったまますべて成功しています。テストが無効化されていないことを証明するのは「OK」ではなく、この一致です。さらに三層構成向けの 12 件が加わり、合計 330 件です。

- **1.10.0** `--use_codex` provider（ChatGPT サブスクリプション枠）、SDK と model の更新、複数段落にまたがる news 引用の修正（2026-08-29）：

  - **セキュリティレビュー — PR で掲げながら、すべての箇所では守られていなかった二つの防護策**：

    - **Codex の preflight は `.env` 全体を binary に渡していました。** `_codex_preflight` は **`env=` なしで** `subprocess.run` を呼び出していました。このため subprocess は `os.environ` 全体、つまり `load_dotenv` が読み込んだ `.env` の全内容を継承していました。計測用の偽 binary で確認すると、preflight には六つの provider の key と `GITHUB_TOKEN` 一つを合わせた **七つの secret** が到達していました。一方、対応する `_grok_preflight` は正しく `env=_grok_env()` を渡しており、到達した secret は **ゼロ**でした。これは PR 内部の不整合です。わずか数行先にある `_strip_secret_env` は、まさにこの invariant を守るために存在します。`_codex_env_base()` を切り出して両方の経路で共有するようにしました。修正後の計測結果は、どちらも secret が 0 件です。
    - **「`--deny` fail-closed」という性質は、実際に使われていた形式を対象としていませんでした。** コメントでは、未知の prefix を持つ rule が起動を拒否させるため、Grok の confinement 全体が成立すると説明していました。しかし `grok 1.0.13` で計測すると、この検証が存在するのは **括弧付き形式だけ**です。`--deny 'CeciNestPasUnOutil(*)'` は起動を拒否します（「unknown tool prefix」）が、`--deny 'CeciNestPasUnOutil'` は何も警告せず受け入れられます。ところが `GROK_DENY_RULES` が使っていたのは裸の名前だけでした。そのため xAI 側で tool 名が変更されると、OS sandbox がそもそも適用されない環境で、計測済みの唯一の confinement 層が何の通知もなく失われる可能性がありました。名前付きの八つの rule を `Prefix(*)` に変更し、それぞれが CLI の既知の prefix として検証されるようにしました。catch-all の `*` は、唯一受け入れられる literal 形式のままです。検証されない形式への逆戻りはテストで防止します。
    - **そのほかの点も問題がないことを確認済み**：command injection はありません（常に list 形式で、`shell=True` は一切使わず、文書内容は stdin または `--prompt-file` 経由）。安全でない deserialization もありません（`json.loads` のみを使用し、型ガード付き）。path traversal 修正について七つの payload で回避方法が見つからないことを確認し、`--deny '*'` が CLI に実際に適用されることも確認しました（workdir 外を読み取ろうとした際に `DENY_ENFORCED` を観測）。
    - 上で追加した鮮度チェックは、ついでに自らの原則を回避していました。PyPI への request が失敗したパッケージを黙って飛ばし、gate を green にしていたのです。現在は実際に比較したパッケージ数を数え、coverage が不完全なら失敗します。

  - **依存関係を最新水準へ更新し、遅れの再発を防ぐ二つの安全策を追加**：

    - **遅れは実在し、長期間に及んでいました**：`openai` 2.54 → **3.6.0**、`anthropic` 0.125 → **1.2.0**、`certifi` 2024.8.30 → **2026.7.22**。すべての provider 呼び出しで TLS を検証するルート証明書ストアは、二年遅れていました。特定された原因は、**`.github/dependabot.yml` が存在しなかったこと**です。このファイルがない場合、GitHub が有効にするのは _security updates_ だけであり、Dependabot が PR を提案するのも CVE の対象となった依存関係だけです。`urllib3` と `idna` は更新された一方で、二つの SDK がメジャーバージョン一つ分も遅れたままになった理由はこれです。
    - **以前の推論で懸念されていたのとは異なり、二つのメジャーバージョンは競合せず共存します**。`openai` 3.x と `anthropic` 1.x は **`httpx2`** に移行しますが、`mistralai` と `google-genai` は `httpx<1` に残ります。ただし、これらは別々の distribution です。実際のインストールで確認した後、OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI、Grok CLI という **七つの provider 経路をエンドツーエンドで検証**し、各出力で inline code とリンクが保持されることを確認しました。「二つの HTTP stack を避ける」というのは選好であって blocker ではなく、計測によって決着しました。
    - **`requirements.txt` は実際の環境を表していませんでした**。`google-auth`、`cryptography`、`opentelemetry` stack は、宣言されていないにもかかわらず作業用 venv にインストールされていました。そのため、新規インストールではテスト対象の環境を再現できませんでした。反対に `tokenizers`、`huggingface-hub`、`PyYAML` は、どこからも import も要求もされていないのに記載されていました。`mistralai` 1.x の残骸です。このファイルを、直接依存関係のみから構築した venv の完全な closure として再生成しました。`pip-audit` では、新しい組み合わせに既知の脆弱性は検出されません。
    - **`.github/dependabot.yml`**（新規）は、pip と github-actions の週次バージョン更新を有効にします。minor と patch は一つの PR にまとめます。patch bump ごとに PR を作ると、いずれ無視されるようになり、noise は更新の敵になるためです。**major は個別**にし、それぞれ実際の呼び出しによる検証を必須とします。
    - **`scripts/check-deps-fresh.sh`**（新規、gate に接続）は、遅れをプロジェクトの verdict に可視化します。Dependabot は提案するだけで保証はせず、その PR が積み上がることもあります。major の遅れは失敗、minor は警告とします。常に赤い gate は、いずれ無視されるためです。PyPI に接続できない場合、local では明示的に skip し、**CI では fail-closed** とします。実行されなかったチェックは成功ではありません。両方向で検証済みです。修正前の正確な状態（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`）は検出し、minor の遅れなら警告だけにとどめます。

  - **この PR のレビューから生まれた修正** — 五つのレビュー agent が diff を精査しました。以下の項目はすべて、修正前に**計測によって再現**しています。そのうち二件は、この同じバージョンの上記変更で導入された regression でした。

    - **regression 修正 — `_NEWS_CITATION_REGEX` に指数的 backtracking がありました。** 複数段落対応の修正で、繰り返し内に `(?:[ \t]*$|[ \t]+.*)` が導入されていました。`[ \t]+` と `.*` の間で空白をどう分配するかが曖昧で、その曖昧さが反復のたびに増幅していました。pattern に match しない、完全に正当な Markdown indentation である `>   texte` の行を使って計測すると、**14 行で 2 589 ms**かかりました。修正後は 0.04 ms で、行を一つ追加するごとに約 9 倍になる挙動も解消しました。`--news` mode では、長くて形式に合わない blockquote 一つで、原因を特定できないまま job timeout まで翻訳が停止し得ました。現在は繰り返しが一行全体を一まとまりとして消費するため（`\n^>(?![ \t]*—).*`）、各反復で match 方法が一つしかありません。実際の 231 記事からなる corpus で検証し、capture の差異は **ゼロ**、引用は同じ 423 件で、複数段落の 14 本の本文も引き続き拡張されています。
    - **二つの provider flag を同時に指定すると、黙って従量課金されていました。** `--use_codex --use_mistral` は受け入れられていました。`_select_provider_client` は Mistral を先に検査し、`_resolve_provider` は明示された boolean を優先するため、どちらも Mistral に収束していました。つまりユーザーはサブスクリプション枠を指定したのに、何の警告もなく従量課金を受けていました。これはまさに `--use_codex` が防ぐために存在する failure mode です。六つの provider flag は、現在すべて `add_mutually_exclusive_group` を通ります。**動作変更**：これまで黙って受け入れられていた、二つの provider を組み合わせた command line は、今後 `argument --use_mistral: not allowed with argument --use_codex` で失敗します。
    - **作業終了時の gate は、probe が crash しても green になっていました。** `scripts/check-release-ready.sh` の 13 個の検証のうち四つは、「stdout を取得し、空なら結論を出す」という pattern に従い、return code を一切確認していませんでした。例外（ファイル名変更、`FileNotFoundError`）は stderr に書き込み、stdout を空のままにするため、検証は「問題なし」と結論づけていました。「`exit 0` は何も証明しない」という罠が、それを防ぐために書かれた script 内部で再現されていたのです。現在は helper `probe()` が return code 0 **かつ**終了 sentinel の存在を必須とし、probe は目印の集合が空なら結論を出しません。空集合に対する assertion は常に true だからです。実証例として、上記の排他的 group を追加したことで provider flag が `*_group` object を通るようになり、古い regex `parser\.add_argument\(` では match しなくなりました。その結果、**21 個中六つの flag** が黙って検査範囲から外れていたのに、gate は green のままでした。
    - **secret scan は六つの provider のうち四つを見逃していました。** character class `[A-Za-z0-9]` はハイフンを除外します。そのため、`sk-proj-…`（現在の OpenAI 形式）と `sk-ant-api03-…` は二つ目のハイフンで途切れ、`AIza…` は対象に含まれていませんでした。pattern を拡張し、`.secrets.baseline` は scan 対象から除外しました。また、ガード `.env` は `git diff --cached` を照会していましたが、これは index しか見ません。そのため、最悪のケースである、**すでに commit 済み**の `.env` は一切表示されませんでした。現在は `git ls-files` を照会します。
    - **Codex の「token warm-up」は warm-up ではありませんでした。** 計測すると `codex login status` は `~/.codex/auth.json` に触れず、mtime も size も変化しません。その help には「Show login status」とあります。それにもかかわらずコメントでは、token を「一度、逐次的に」更新し、一回限りの rotating token に対する並行 refresh の危険を無効化すると主張していました。説明されていた保護は存在しません。現在、コメントは code が実際に行うことを説明し、本当の対策は引き続き `max_jobs=4` です。また、このチェックは以前無視していた `CODEX_BIN` を尊重するようになりました。`PATH` に `codex` がない環境では「未認証」として失敗し、誤った診断を出していました。
    - **`.env` は subshell 内で source されていました。** `detect_provider` は command substitution 内で呼ばれるため、その export は親 shell に反映されませんでした。`.env` で定義した `GROK_BIN`、`GROK_HOME`、`REGEN_MODEL` は `main()` 内の参照から見えず、正しい設定でも「Grok binary が見つからない」と結論づけていました。
    - **並行数が公称上限を 50 % 超えていました。** README/CHANGELOG のペアを起動した後にガードが置かれていたため、`max_jobs=2` に対する実測 peak は **3** でした。週次 quota が Chat/Imagine/Voice と共有され、計測もできない Grok では、script が自ら定めた上限すら守れていなかったことになります。また、最終 count は表示されるだけで、28 との比較は一度も行われていませんでした。そのためファイルが一つ欠けても見逃されていました。
    - **Grok の出力契約：`stopReason` が存在しない場合も、現在は失敗します。** 公表された契約では `end_turn` が必要なのに、code は「`end_turn` **または不在**」を適用していました。そのため、この field のない payload や CLI 更新で field 名が変更された payload によって、ガードが黙って no-op になっていました。また、`max_turn_requests` は rate limit に分類されなくなりました。これは turn budget の枯渇であり、retry しても 90 秒待たされた後に同じ結果になるためです。`quota` も rate limit marker から外しました。`_codex_is_rate_limited` の docstring がすでに述べていた理由を、Grok だけが適用していなかったためです。
    - **Gemini の cascade は model ごとに memoize されるようになりました。** 以前は segment ごとに `minimal` から再開していましたが、default model はこれを拒否します。そのため通常経路でも、segment ごとに 400 の往復が発生し、同じ警告が繰り返し表示されていました。何百回も繰り返される warning は読まれなくなります。そうして warning は mask へ変わります。
    - **その他**：CI での拒否メッセージは Codex 向けに hard-code され、`--use_grok_cli` のユーザーを `XAI_API_KEY` ではなく `OPENAI_API_KEY` へ誘導していました。`provider.capitalize()` は「Grok_cli」と「Openai」と表示していました。subprocess 基盤のコメントは、両 CLI に「shim」という説明を一般化していましたが、Grok binary は native ELF です。正しい根拠は「独自の subprocess を spawn する agent」です。`subprocess` に関する 12 件の SAST finding は、根拠を添えて `# nosec` / `# nosemgrep` としてマークしました。`shell=True` を使わない list 形式なので injection は不可能であり、文書内容が argv を通ることもありません。
    - **agent 型 subprocess に secret が一切入らなくなりました。** 名前を列挙した deny-list が守っていたのは、**課金**に関する invariant だけでした（Codex には `OPENAI_API_KEY` を渡さず、Grok には `XAI_API_KEY` を渡さない）。計測すると、それでも各 subprocess には **さらに七つの secret** が入っていました。Anthropic、Mistral、Google、Gemini の key、もう一方の CLI の key、そして secret ではないものの通信先を変更する `OPENAI_BASE_URL` です。しかし、この二つの CLI は **agent** であり、Grok の agent は多くの Linux 環境で適用可能な OS sandbox なしに動作します。現在の filter は名前の列挙ではなく、**名前の pattern**（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`）に基づきます。このため、この code が知らない変数をユーザーが `.env` に追加した場合も対象になります。どの変数も CLI には不要です。認証情報は `~/.codex` と `~/.grok` にあり、environment にはありません。hardening 済みの environment で、両 provider を使った**実際の翻訳が正常に完了**することを確認しました。
    - **テスト**：新しいファイル `tests/test_review_hardening.py`（21 tests）で、provider flag の排他性、`stopReason` の契約、news regex の線形性、CI での拒否メッセージ、Gemini の memoization、subprocess environment に secret が一切存在しないことを固定しました。最後の assertion は**汎用的**であり、どの list にも名前が載っていない key でも失敗します。一方、既存の削除テストは自身の定数を写しただけで、自身の loop の故障以外を検出できませんでした。全 test suite は **311 tests** です。
  - **2つの新しいGrokプロバイダー**：`--use_grok`（xAI API、キーは`XAI_API_KEY`、従量課金）と`--use_grok_cli`（公式Grok Build CLI、Grokサブスクリプションの利用枠から差し引かれる――`--use_codex`と同じ仕組み）。
    - **APIモード、約40行**：xAIのエンドポイントはOpenAI互換であるため、クライアントと`_call_openai`はそのまま再利用され、変更されるのは`base_url`のみ。必要だった適応は1つだけで、すべてに恩恵がある。`finish_reason`が、OpenAIが`stop`を出力する箇所でxAIが出力する形式`end_turn`も受け入れるようになった。モデル：`grok-4.6`（高品質）と`grok-4.3`（低コスト）。なお、Grokの低コストモデルは依然としてリポジトリ内で最も高価で、100万トークン当たり$1.25/$2.50であるのに対し、`mistral-small-latest`は$0.15/$0.60である。このプロバイダーを選ぶ理由はモデルの多様性であり、価格ではない。
    - **CLIモード**：Codexを基にしているが、実環境によって課された4つの相違点がある――プロンプトはファイル経由で渡される（`--prompt-file`。CLIはstdinを読み取らず、argv内のセグメントは`ps`から見えてしまう）、出力はstdout上の単一のJSONオブジェクトである（JSONLでも`-o`ファイルでもない）、サブスクリプションで利用できるのは`grok-4.6`と`grok-4.5`のみ、そしてsandboxは適用できない（以下を参照）。サブプロセスの起動処理は`_codex_run_process`でCodexと共通化されており、すでにテスト済みのCodexプロバイダーのその他の部分には手を加えていない。
    - **`exit 0`は何の証明にもならないことを実測**：未認証の場合、CLIは**stdout**に`{"type":"error","message":"Not signed in."}`を書き込み、終了コード**0**を返す。拒否やターン数超過でも同様に動作する。したがって、出力契約では4つの条件を同時に満たす必要がある。終了コードが0、エラーペイロードがない、`stopReason == end_turn`、そしてテキストが空でないこと。事前チェックも同じ論理に従う。`grok models`はログアウト状態でも0で終了し、stdoutに「not authenticated」が存在する場合にのみ未認証と判断できる。
    - **隔離：意図的かつ文書化された非対称性。** Codexが`--sandbox read-only`で動作する一方、Grokのsandboxは、多くの新しいLinux環境では適用できない。これは、`sudo`なしでは回避できない2つの独立したシステム上の原因による。Ubuntu 24.04以降ではAppArmorが非特権user namespaceをブロックする（`bwrap: setting up uid map: Permission denied`。Grok外でも再現済み）。また、`/run/podman`が`0700`の場合、コンテナランタイムsocketのdeny-listが失敗する（resolverが補足するのは`ErrorKind::NotFound`のみで、EACCESは致命的となる）。最大の落とし穴は、適用できない**組み込み**プロファイルを指定すると、**隔離されていない状態で黙って起動する**ことだ。そのため、スクリプトはデフォルトでプロファイルを要求せず、黙ってフォールバックすることもなく、stderrに警告を出す。保護はCLIの`--deny`ルールに依存し、包括的な`*`も含まれる。実測で確認された唯一の_フェイルクローズ_層であり、未知の接頭辞を持つルールが1つでもあると起動を拒否する。`GROK_TRANSLATE_SANDBOX=read-only`でこの隔離を必須にでき、その場合、マシンが要件を満たせなければ起動は失敗する。
    - **安全策**：`XAI_API_KEY`、`GROK_API_KEY`、`GROK_SANDBOX`はサブプロセスの環境から除去される（キーがあると従量課金に切り替わり、継承された`GROK_SANDBOX`があると、誤解を招くメッセージとともに適用不能なプロファイルを強制してしまう）。MCP/hooks/skills/agentsの切り替え機能を無効化し、`--disable-web-search`、`--no-subagents`、`--no-plan`、使い捨ての作業ディレクトリ、CI環境での拒否、プロセスグループを終了するtimeout、rate limit時のback-offも備える。`--max-turns`は1ではなく6に設定されている。カウンターはツールターンの後に増加するため、1では出力が途中で切れてしまう。
    - **割り当て量**：Grokのプールは週単位で、**Chat、Imagine、Voiceと共有**されるうえ、これを表示するコマンドはない。`account/rateLimits/read`で消費量を数値化できるCodexとは対照的である。そのため、`regen_translations.sh`は並行数を2に制限し、明示的に警告する。
    - **テスト**：新しいファイル`tests/test_grok_provider.py`（24テスト）。全体で**290テスト**。
  - **修正されたバグ――英語の複数段落からなる引用が一部しか保護されていなかった（`--news`モード）**：`_NEWS_CITATION_REGEX`は、引用本文として**連続する**`>`行だけを受け入れていた。引用が複数の段落にまたがると（空の`>`行で区切られている）、最後の段落だけが取得されてplaceholderに置換され、それ以前の段落はLLMに送られて翻訳されていた。これは、`--news`が保証するために存在する動作と正反対だった。繰り返し部分が内部の空の`>`行も受け入れるようになり、さらに非貪欲となったことで、最初に現れる空行ではなく、斜体行の直前にある空の`>`行で停止する。
    - **実測された規模**：実際の198記事のcorpusでは、419件の引用のうち11件が該当した。回帰はない。新しいregexが取得する引用数は完全に同じで、複数段落の本文だけが拡張される（408件の本文は同一、11件は拡張）。また、帰属表示行`> — …`は、維持されたlookaheadにより、引き続き本文へ取り込まれることはない。
    - **end-to-endでの証明**：69 koの記事をja/arへ翻訳したところ、以前は日本語で`> GLM-5.3がオープンウェイト化。`となり、アラビア語でも同様に翻訳されていた引用の第1段落が、今では`> GLM-5.3 is now open-weight.`のまま維持される。英語の引用行数は9から10に戻り、原文と一致した。
    - なお、この不具合は下流のvalidatorでは検出されなかった。validatorは引用の存在を確認するだけで、完全であるかどうかは検証していなかったためである。
  - **デフォルトプロバイダーで実測された節約効果**：`_openai_extra_kwargs`は、モデル名が`gpt-5`で始まる場合、`--eco`でも`reasoning_effort="medium"`を送信していた。10語の文を翻訳する`gpt-5.4-mini`での測定結果：`medium`ではreasoning tokenが45、出力tokenが65、`none`ではそれぞれ0と14だった。翻訳に推論は何ももたらさず、すべてのファイルのすべてのセグメントで料金が発生していた。デフォルトは`--eco`では`none`となり、それ以外では引き続き`medium`となる。CLIで明示的に渡された値は引き続き優先される。`--reasoning_effort`は、`low`/`medium`/`high`に加えて、`none`と`xhigh`も受け入れるようになった（すべての値がすべてのモデルで受け入れられるわけではない。たとえば`minimal`は`gpt-5.4-mini`で拒否されるが、既存のパラメーターなしでのretryがこのケースを処理する）。
  - **SDKの更新とGeminiの移行**：`google-generativeai`（2025-11-30にサポート終了、リポジトリはarchive済み）は、統合SDK **`google-genai`**に置き換えられた。`genai.Client(api_key=...)`の後に`client.models.generate_content(model=, contents=, config=)`を使用し、システムプロンプトはセグメントへ連結する代わりに`system_instruction`で渡される。`mistralai`は**2.9.4**へ更新（importは`from mistralai.client import Mistral`となる。旧形式では`ImportError`が発生することをwheel内で確認済み）、`anthropic`は**0.125.0**、`openai`は**2.54.0**へ更新された。これらは`httpx2`への切り替え前の最終バージョンであり、venv内に2つのHTTPスタックを共存させないためである。これに伴い、`httpx` 0.28.1と`pydantic` 2.13.5も制約が解除された。
  - **ドキュメントではなく実際のテストで捕捉された2つの回帰**：
    - `anthropic` ≥ 1.0は、`max_tokens`から10分を超えると予想される非streaming呼び出しをクライアント側で拒否する（`ValueError: Streaming is required...`）。この安全策は0.34.2には存在せず、`max_tokens=32768`を伴うすべてのClaude呼び出しを壊していた。明示的な`timeout`（`CLAUDE_TIMEOUT`、デフォルト900 s）によって修正し、完全な応答だけを利用する呼び出しをstreamingへ切り替えずに済むようにした。
    - `thinking_level="minimal"`を受け入れるのはGeminiカタログの一部だけである。`gemini-3.1-flash-lite`は対応するが、`gemini-3.7-flash`と`gemini-3.1-pro-preview`は400で拒否する。そのため、OpenAIにすでに存在するfallbackを手本として、`_gemini_generate_with_fallback`に`minimal` → `low` → thinking_configなし、という段階的なfallbackを実装した。最適化パラメーターによって翻訳が失敗してはならない。
  - **デフォルトモデルを刷新**し、それぞれ実際の呼び出しで検証済み：OpenAIは`gpt-5.5` → **`gpt-5.6-terra`**（28件のbatchで−60 %）、`gpt-5.4-mini` → **`gpt-5.6-luna`**（−73 %）。Claudeは`claude-sonnet-4-6` → **`claude-sonnet-5`**（より安価で新しい）、`claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（日付なしの正式ID）。Geminiは`gemini-3.1-pro-preview` → **`gemini-3.7-flash`**、`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（安定版で、`3.5-flash-lite`より安価）。Mistralは変更されず、`mistral-large-latest`が4つの中で最高の費用対効果を維持している。なお、`gemini-3.1-pro-preview`より新しいPro系列のGeminiモデルは存在しない。2026年5月に発表されたGemini 3.5 Proは結局リリースされず、3.5/3.6/3.7系列はすべてFlash専用である。
  - **Gemini切り替え前に実測したA/B比較**：`README.md`を`gemini-3.1-pro-preview`、次に`gemini-3.7-flash`で日本語へ翻訳した。構造は完全に同一（リスト21件、コードブロック18件、HTMLリンク13件、画像13件、すべてのURLを維持）で、所要時間は**48 sに対して8 s**だった。翻訳や非ラテン文字のscriptについてこの2つのモデルを比較した公開benchmarkは存在しないため、この切り替えは、そうでなければ単なる推測に基づくものとなるところだった。
  - **Claude応答ブロックのフィルタリング**：`_call_claude`は種類をフィルタリングせずに`block.text for block in response.content`を実行していた。適応的推論を備えたモデル（Sonnet 5以降）は`thinking`ブロックを挿入するが、そこでは`.text`ではなく`.thinking`が公開されるため、最初のセグメントで不透明な`AttributeError`により翻訳が失敗するはずだった。`thinking`、`redacted_thinking`、`tool_use`、`tool_result`の各ブロックは除外されるようになった（テキストを持つ未知の種類に対する許容性を維持するためのnegative list）。また、テキストブロックが1つもない応答では明示的なエラーが発生する。`thinking={"type": "disabled"}`は各呼び出しに渡される。
  - **`MODEL_TOKEN_LIMITS`を再同期**：廃止日を過ぎたモデルを削除（`magistral-*`系列は2026-07-31に廃止、`gemini-2.0-*`は2026-06-01、`gemini-3-pro-preview`は2026-03-09、ならびに`claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。上限値を修正：Mistral 128K → **256K**（Large 3 / Small 4世代）、Gemini 1 000 000 → **1 048 576**（実際のinput上限）、`claude-opus-4-5` 200K → **1M**、`gpt-5.6-*`系列400K → **1,05M**。Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest`、`ministral-*`系列を追加。なお、これらの上限値は引き続き目安であり、`translate()`がセグメント分割を`min(16000, limite)`に制限している。
  - **プロバイダー `--use_codex`**：従量課金の API を呼び出す代わりに、公式 Codex CLI（`codex exec`）を非対話モードで駆動する5番目のプロバイダー。翻訳には、すでに支払い済みの ChatGPT サブスクリプションの割り当てが使用される。この用途について OpenAI が文書化している唯一の方法である。プラン別の利用可否一覧では、「Codex SDK、`codex exec`、およびスクリプト化可能なワークフロー」が Plus/Pro/Business/Enterprise で利用可能とされている一方、`~/.codex/auth.json` のトークンでは API Platform の呼び出しを認証できない（また、このスクリプトが読み取ることも一切なく、認証とその更新は引き続き CLI が管理する）。
  - **npm だけでなく pip でもインストール可能な Codex バイナリ**：`_resolve_codex_binary()` は、`CODEX_BIN`、次に `PATH`、その後に OpenAI が公開している公式 Python パッケージ **`openai-codex-cli-bin`**（`openai-codex` SDK の依存関係）内のバイナリを検索する。したがって、Python プロジェクトで `--use_codex` を使用するために、npm のグローバルインストールは不要になった。このパッケージは `requirements.txt` には追加されていない。バイナリのサイズが約250 MBあり、任意のプロバイダーのために全ユーザーへ負担させることになるためである。エンドツーエンドで検証済み：`codex` が `PATH` に存在しない状態でも、解決処理によってパッケージ化されたバイナリが見つかり、完全な翻訳が6秒で完了する。
  - **「サブスクリプションモード」の保証**：`OPENAI_API_KEY` と `CODEX_API_KEY` はサブプロセスの環境から削除される。この保護がなければ、`.env` に存在するキーによって、目に見える通知が一切ないまま Codex が従量課金へ切り替わる可能性がある。これはまさに、このプロバイダーが回避するために存在する事態である。
  - **テストで固定された CLI の落とし穴**：
    - プロンプトを引数で渡した場合でも、`codex exec` は stdin を読み取る。stdin を閉じないと、コマンドはモデルを一度も呼び出さないままタイムアウトまで待機する（再現結果：180秒後に終了コード124、出力0バイト）。したがって、`communicate(input=...)` は必須である。
    - npm でインストールされた `codex` は、本物の Rust バイナリを `spawn` する Node シムである。このバイナリは Python プロセスの**孫プロセス**であり、`subprocess.run(timeout=)` の `SIGKILL` 後も生き残って割り当てを消費し続ける可能性がある。そのため、`Popen(start_new_session=True)` と `os.killpg` を使用する。
    - CLI は `turn.failed` を出力していても終了コード0で終了する場合がある。戻りコードに加えて JSONL 出力（`--json`）も検査し、終了コードが0でも `-o` ファイルが存在しなければ、空のセグメントを生成する代わりに明示的なエラーを発生させる。
  - **rate limit 時の back-off**：CLI には内部 retry が実装されていない（`max_retries = 0`）。分類は部分文字列ではなく、JSON ペイロードの構造（`status: 429` / `error.type`）に基づいて行う。「quota」という語は、回復可能な429と恒久的な `insufficient_quota` の両方に現れるためである。
  - **CI の保護**：`CI` または `GITHUB_ACTIONS` が定義されている場合、`--use_codex` は拒否される。サブスクリプション認証は共有 runner 向けではなく、OpenAI も公開リポジトリでこのワークフローを使用しないよう明示的に推奨している。
  - **モデル**：`gpt-5.6-sol`（品質）と `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` ファミリーは CLI と API Platform で共通だが、ChatGPT アカウントですべてを利用できるわけではない。allowlist はローカル検証なしでサーバー側に適用され、通常とは異なるモデルを指定すると警告が表示される。Plus プランでは、5時間のウィンドウあたり Sol が10～100メッセージであるのに対し、Luna は250～2,000メッセージを利用できるため、あらゆるバッチ処理には `--eco` が推奨モードである。
  - **修正済みのバグ — 完全に成功しても `regen_translations.sh` がエラー終了していた**：`trap ... EXIT` は、`main()` の `local` 変数である `failed_log` を参照していたが、この変数は trap の実行時にはすでに存在しない。`set -u` では `failed_log: unbound variable` が発生し、28件の翻訳がすべて正しくてもスクリプトが終了コード1で終了していた。その結果、再生成直後の最もコストが高い段階で `release.sh --auto`（`set -e`）が中断される可能性があった。変数をグローバルに変更し、trap でその存在を確認するようにした。有用な副作用として、これまでこのエラーに隠されていた実際の翻訳失敗が、終了時の要約で再び確認できるようになった。
  - **`REGEN_MODEL`**：プロバイダーのデフォルトより優先して特定のモデルを強制する、`regen_translations.sh` の新しい環境変数。たとえば、処理量重視の `--eco` モデルではなく、サブスクリプション割り当て内の最上位モデルで再生成するには `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol` を指定する。
  - **`regen_translations.sh`**：明示的な opt-in で利用可能な `REGEN_PROVIDER=codex`（ユーザーに知られないままサブスクリプション割り当てを消費しないよう、自動検出は一切しない）。並列処理を開始する前に、トークンを逐次的に一度更新する。Codex の更新トークンはローテーション式かつ一度限りの使用であり、並行 job があると `codex login` セッションが無効化されるためである。また、同時実行数は4に引き下げられる。
  - **関連するリファクタリング**：`_dispatch_provider_call` は、処理チェーン全体へ4つ目の真偽値を伝播させる代わりに、プロバイダー名を返す `_resolve_provider()` を使用することで、引数を8個から6個に削減した。`Namespace` が最小限の状態で `translate(..., use_mistral=True)` を呼び出すテストを維持するため、明示的な真偽値は引き続き `args` より優先される。
  - **テスト**：新しいファイル `tests/test_codex_provider.py`（48件のテスト）で、argv、不要情報を除去した環境、前置き禁止契約、無言の失敗、timeout/killpg、back-off、preflight、プロバイダー解決、Gemini の reasoning cascade、Claude のブロックフィルタリング、複数段落の news 引用を網羅。全テストスイートは290件。
  - **実環境での検証**：プロジェクトの `README.md` を Codex で**14言語**に翻訳した結果、参照翻訳と構造が完全に一致した（コードブロック14個、見出し24個、表25行、HTML リンク13個、画像13個、URL 19個、コードブロックは文字単位で完全一致、プレースホルダーの残留ゼロ）。`--news` モードで69 KBのニュース記事を処理したところ、`gpt-5.6-luna` と `gpt-5.6-sol` の両出力が、en/ja/ar について後続のアプリケーション検証を通過した。`account/rateLimits/read` で測定した消費量は、`--eco` モードにおいてカウンターの丸めしきい値未満（5時間ウィンドウの0％）にとどまった。

- **1.9.2** 入れ子の括弧または FR 接頭辞を含む news 帰属 URL の抽出を修正（2026-05-11）：

  - **修正済みのバグ**：`_protect_news_quotes` における帰属 URL の抽出では、正規表現 `re.search(r"\((.+?)\)", attribution)`（括弧間の最短一致キャプチャ）を使用していた。`(relayé par [@user sur X](https://x.com/.../123))` のような帰属表記（入れ子の括弧：外側の `(` と Markdown リンクの `]()`）では、最初に現れる `)` でキャプチャが終了し、FR 接頭辞を含む切り詰められた文字列 `relayé par [@user sur X](https://x.com/.../123`（末尾の `)` なし）になっていた。その結果、`_validate_news_post` は翻訳後の出力からこの文字列を検索して常に失敗していた（理由は2つあり、`)` が切り詰められていることと、「relayé par」が `relayed by`/`weitergeleitet von`/… に翻訳されることである）。low → medium → high → gpt-5.5 の完全な cascade でも通過できなかった。
  - **修正**：正規表現を `re.search(r"\]\(([^)]+)\)", attribution)` に変更した。Markdown リンクの `](url)` を明確に対象とし、FR 接頭辞や切り詰めを含まない**純粋な URL のみ**をキャプチャする。翻訳中はプレースホルダー `#URL{N}#` によって不変性が保たれる。問題となった次の2種類のパターンに対応する：
    - `(relayé par [@account sur X](url))` — 入れ子の括弧
    - `via [@source](url)` または `selon [@author](url)` — 外側の括弧がない FR 接頭辞
  - **テスト**：`test_silent_failure.py` の `TestNewsCitationExtraction` クラスに2件追加：
    - `test_extract_attribution_url_with_nested_parens`（Genspark CEO E2B のバグをそのまま再現したケース）
    - `test_extract_attribution_url_with_french_prefix`（`via` を含む派生形）
  - **網羅範囲の不足**：`check-editorial-coverage.py` は編集上の構文を検証するが、translator で翻訳可能かどうかは検証しない。今後の改善案（v1.9.2 の対象外）として、帰属情報の抽出を dry-run でシミュレートし、公開**前**にリスクのあるパターンを検出するチェックが考えられる。

- **1.9.1** 翻訳 marker 注記内の CTA ラベルの i18n を修正（2026-05-10）：

  - **修正済みのバグ**：翻訳済みファイル上部の marker バナーにある CTA リンクのラベル `[Voir le projet sur GitHub ↗]` が、`target_lang` に従わず、すべての対象言語で**フランス語のまま**残っていた。このラベルは LLM には一切渡されず（URL とリポジトリの slug を保持するため Python 側で組み立てられる）、翻訳段階では修正できなかった。v1.9 で `marker` 形式を追加して以降の無音の回帰だった。
  - **修正**：15言語を各言語のローカライズ済みラベルに対応付ける新しい定数 `_VIEW_PROJECT_LABELS` を追加。`_translation_note_invariants(target_lang)` と `_assemble_translation_note_paragraphs(phrase, target_lang)` は対象言語も伝播するようになった。言語が不明な場合は `fr` にフォールバックする（安全対策であり、KeyError は発生しない）。
  - **テスト**：`test_source_emits_three_paragraphs_repo_title_description_link` を調整（対象言語 `ja` → 期待される日本語ラベル）。新しいテストを2件追加：`test_source_link_label_localized_per_target_lang`（ラテン文字、表意文字、アブジャドの各文字体系を含む7言語でパラメーター化）と `test_source_link_label_falls_back_to_french_for_unknown_target`。合計：`test_translation_note_position.py` に40件のテスト（従来は38件）。
  - **後方互換性**：デフォルト値 `target_lang="fr"` を持つシグネチャにより、`args.target_lang` を指定しない外部のプログラム呼び出し元も、変更なしで引き続き動作する。
- **1.9** サイレント障害の修正 + 包括的な品質ツール + 複数位置対応の翻訳注記（2026-05-07）：
  - **複数位置対応の翻訳注記 + 「embed card」マーカー形式**：
    - 新しい CLI オプション（追加のみ、デフォルトは変更なし → **破壊的変更なし**）：
      - `--note_position {top,bottom,both}`（デフォルト：`bottom`）：翻訳済みファイルの先頭、末尾、または両方に注記を配置します。
      - `--note_format {legacy,marker}`（デフォルト：`legacy`）：
        - `legacy` は v1.8 の動作（太字段落 `**…**`）を **byte-for-byte** で厳密に再現します。
        - `marker` は、非表示の Markdown link reference definition（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）に続けて、「GitHub repo embed card」風の表示になるよう構成された **3段落の blockquote** を出力します。内容は、inline code 形式のプロジェクトタイトル（`**\`ai-powered-markdown-translator\`\*\*`）、LLM によって翻訳された説明、表示される矢印付きの CTA リンク（`[Voir le projet sur GitHub ↗](URL)`）です。ビルド時に remark plugin で処理できます（jls42.org のブログ → plugin `remark-translation-banner` を参照）。
    - **LLM に決して送信されない不変要素**：リポジトリタイトルと GitHub URL は、説明文の翻訳後に Python 側で組み立てられます。LLM が slug `ai-powered-markdown-translator` や `https://github.com/jls42/...` を目にすることはなく、renderer・大文字小文字・scheme が一切変更されないことを保証します。
    - **frontmatter 対応の挿入**：`top` または `both` モードでは、注記は YAML frontmatter を閉じる `---` ブロックの**後**に挿入されます（Astro Content Collections / gray-matter の安全性を確保）。helper `_split_frontmatter` はファイル先頭の `---\n…\n---\n` を検出して整合性を保ちます。閉じる fence がない未完了の frontmatter では **`RuntimeError` を送出**し、誤った位置に注記を書き込まず、そのファイルを `failed_files` に含めます。
    - **ホワイトリスト方式のモデル sanitizer**：`_sanitize_model` は `[A-Za-z0-9._:/-]` に含まれない文字をすべて `_` に置換し、空の場合は `unknown` にフォールバックします。Astro の remark plugin 側の validator と整合させ、マーカー形式を壊す文字（空白、引用符、括弧、カンマなど）を無害化します。
    - **内部 refactor**：`_append_translation_note`（1つのモノリシック関数）→ 7つの純粋 helper（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。builder と composer を分離し（builder は区切りなしの純粋なブロックを返し、composer は位置に応じて `\n\n` を適用）、本番処理と helper のソースが同じ3段落 assembler を共有します。
    - **空行を保持する `_quote_lines`**：各行の先頭に `> ` を付け、空行は `>` のみに変換します。これにより mdast は、改行を含む単一段落ではなく、blockquote 内の3つの独立した段落（タイトル／説明／リンク）として認識できます。
    - **適応型 `_build_translation_note_block`**：LLM が保持した段落数に応じて処理します（3 = 完全な card 形式、2 = 文 + リンク、1 = fallback）。Markdown リンク `](` が検出された場合、1段落 fallback は**今後 `**...**` で囲みません**（リンクを `<strong>` で囲むと表示が不安定になるため）。
    - **後方互換性**：`_compose_with_notes` 側の `getattr(args, "note_position", "bottom")` と `getattr(args, "note_format", "legacy")` により、これらの属性を持たない Namespace（既存テスト、外部からのプログラム呼び出し）も変更なしで引き続き動作します。
  - **長文翻訳におけるサイレント障害の修正**：
    - すべての provider（OpenAI、Mistral、Claude、Gemini）で翻訳後の言語を検証：決定論的レイヤー（ソースの抜粋がそのまま残っていないかを検出）+ 確率的レイヤー（`langdetect`）
    - `finish_reason` / `stop_reason` のホワイトリスト：ホワイトリスト外の状態（truncation、content_filter など）ではすべて `RuntimeError` を送出
    - Claude の `max_tokens`：`4096` → `32768`（16k segment で潜在的な truncation を回避し、FR→JA/ZH/KO/AR/HI の cross-script 変換に余裕を確保）
    - heading 対応の segmentation：segment の後半にある H2/H3 を優先（各 segment が意味的に完全な section から始まるようにする）
    - 非ゼロの exit code までエラーを伝播：`translate_markdown_file` は型付きステータス `success` / `failure` / `skipped` を返し、1ファイルでも失敗した場合は `main()` が `sys.exit(1)`（single-file と batch の両方）
    - すべての provider に empty-content guard、ソース／出力の妥当性比率（500文字以上で、5%未満なら拒否）、コード placeholder の検証（`#CODEBLOCK`/`#INLINECODE`）、LLM 処理後の正規化（heading に連結された区切り／リンク）、`reasoning_effort` を使用しない `BadRequestError` retry を追加
    - 依存関係 `langdetect==1.0.9` を追加
  - **pre-commit 品質ツール**（「完全な EurekAI 型」、14 hooks）：
    - Pre-commit：ruff（lint+format）、shellcheck、prettier（md/yaml/json）、detect-secrets（4つの API key を保護）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（whitespace、EOF、large-files、shebangs など）
    - Pre-push：mypy（段階的な lax mode）、Opengrep SAST（translate.py + scripts/）、pip-audit（初期 reporting mode）、unittest discover（tests/ + scripts/tests/）
    - `./venv/bin/python` を使用するローカル wrapper を `scripts/` に配置
    - `scripts/audit_verdict.py`：11件の unittest を備えた pip-audit 用 JSON parser。jls42-astro の parser を Python に移植して調整
    - 初期の ruff 違反7件を修正：B904（raise from）×2、B007（未使用の dirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizard は一時的に `translate.py` を除外（CCN 21～47 の関数が4つあり、refactor を予定）— scripts/ には厳格な gate を適用
  - **SonarCloud + 包括的な coverage**：
    - GitHub Actions workflow `SonarCloud`（sonarcloud.yml + sonar-project.properties）：push と pull-request のたびに解析し、`coverage.xml` で coverage を取得
    - README 上部に11個の SonarCloud badge（Quality Gate、Security/Reliability/Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）
    - `tests/test_silent_failure.py`（`unittest` stdlib）：サイレント障害のエラーチェーンを構成する6つの段階を網羅
    - `tests/test_orchestration.py`（+79 tests）：`translate.py` の orchestration layer（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` の TypeError + BadRequestError fallback、o1-series prompt format、`_validate_translation_output` の early-return branch）を網羅
    - `scripts/tests/test_audit_verdict.py`：`main()`（stdin/stdout）と `if __name__ == "__main__"` ブロックを subprocess 経由で網羅
    - **新規コードの coverage**：75.5% → 約98%（translate.py 98%、scripts/audit_verdict.py 97%）
  - **テスト**：`tests/test_translation_note_position.py` は position × format の組み合わせ（E2E の `marker+top|bottom|both` と `legacy+top|bottom|both` を含む）、複数行の prefix 付与、byte-for-byte の後方互換性（golden literal）、sanitizer、frontmatter の split（閉じられていない fence での raise を含む）、3段落形式、2段落 fallback、1段落 + Markdown リンクの guard、およびタイトルと URL が LLM に決して送信されないことを assert する重要な安全策 `TestLLMPayloadExcludesInvariants` を網羅します。**190 tests pass**、regression は0件です。
  - ドキュメント：`README.md`（フランス語 + 14翻訳）に badge を追加、`CLAUDE.md`（pre-commit workflow + 詳細な CI watch）、28翻訳を再生成
- **1.8** `--news` モード + 2026年モデルへの bump（2026-03-17、tag `v1.8`）：
  - デフォルトモデルを更新（2026年3月）：
    - OpenAI 品質重視：`gpt-5` → `gpt-5.4`
    - OpenAI 経済重視：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 品質重視：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）および `gemini-3.1-pro-preview`（1M）の token limit を追加
  - 初期 `--news` モード：placeholder `#NEWSQUOTE\d+#` による英語引用の保護、mapping `LANG_FLAGS`（15言語）、対象言語別の flag 管理
  - 復元前に news placeholder を検証（regression：LLM が placeholder を削除した場合、引用のない出力が気付かれずに生成されていた）
  - script `regen_translations.sh` を portable 化（絶対パスを使用し、pwd への依存なし）
  - README/CHANGELOG の language bar にフランス語へのリンクを追加し、28翻訳を再生成
- **1.7** 新機能：
  - 翻訳時に元のファイル名を保持する `--keep_filename` オプション
  - API key を自動的に読み込む `.env` ファイルのサポート
  - **inline code の保持**：backtick（`` `...` ``）が翻訳中に保護されるようになりました
  - system prompt を改善：
    - YAML frontmatter 内の引用符処理を改善
    - template 変数 `{variable}` を保護
    - 要求されていない翻訳者注記を禁止
  - 364ファイルでのテストに成功（jls42.org ブログの migration）
- **1.6** 新機能：
  - 翻訳用 Google Gemini API のサポート（`--use_gemini`）
  - デフォルトモデルを2026年版に更新：
    - OpenAI：`gpt-5`（品質重視）、`gpt-5-mini`（経済重視）
    - Claude：`claude-sonnet-4-5`（品質重視）、`claude-haiku-4-5`（経済重視）
    - Gemini：`gemini-3-pro-preview`（品質重視）、`gemini-3-flash-preview`（経済重視）
  - より高速で低コストなモデルを使用する経済モード（`--eco`）
  - ディレクトリを走査せずに単一ファイルを翻訳（`--file`）
  - 新しい簡略化された命名 pattern：`{base}-{lang}.md`
  - モデル名を含む旧形式を維持する `--include_model` オプション
  - 一覧にないモデルをデフォルトの token limit（128k）でサポート
  - README を14言語に翻訳
- **1.5** 改善：
  - **API key とデフォルトモデルの更新：**
    - **OpenAI：** `DEFAULT_MODEL_OPENAI` から `"gpt-4o"` に更新。
    - **Mistral AI：** `DEFAULT_MODEL_MISTRAL` から `"mistral-large-latest"` に更新。
    - **Anthropic Claude：** `DEFAULT_ANTHROPIC_API_KEY` を追加し、`DEFAULT_MODEL_CLAUDE` から `"claude-3-5-sonnet-20240620"` に更新。
  - **翻訳 prompt の最適化：**
    - 直接翻訳および翻訳注記用の prompt を拡充し、明確さと効率を向上させました。metadata と特定の formatting 要素を保持するための詳細な指示も含まれています。
  - **コードの refactor：**
    - Mistral AI client の初期化で `MistralClient` を `Mistral` class に置き換え。
    - 可読性と保守性を向上させるため import を再編成。
    - 翻訳時に元の formatting を保持するため、テキストの segmentation と code block の処理を改善。
  - **出力ファイルの管理：**
    - 出力ファイル名内のモデルと言語の順序を入れ替え（例：`f"{base}-{args.target_lang}-{args.model}.md"`）、翻訳の整理と検索を容易にしました。
  - **その他の改善：**
    - 不要な空行を削除してコードを整理。
    - script の構造と可読性を向上させるための軽微な調整。
- **1.4** 新機能：
  - 翻訳用 Anthropic Claude API のサポート
  - 明確さと効率を高めるため prompt を最適化
  - コードの保守性を向上させるための軽微な調整
- **1.3** 改善と新機能：
  - code block の処理を改善
  - 出力ファイルの管理を改善
  - 既存ファイルの検出を改善
  - 翻訳を強制する `--force` オプション
  - 出力ファイル名内のモデルと言語の順序を入れ替え
- **1.2** changelog の修正
- **1.1** Mistral AI API のサポートを追加
- **1.0** 初期 version - OpenAI API のサポート

**gpt-5.6-solでフランス語から日本語に翻訳された記事。**
