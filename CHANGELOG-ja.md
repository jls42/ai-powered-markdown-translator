### 変更履歴

🌍 [フランス語](CHANGELOG.md) | [英語](CHANGELOG-en.md) | [スペイン語](CHANGELOG-es.md) | [中国語](CHANGELOG-zh.md) | [ドイツ語](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [韓国語](CHANGELOG-ko.md) | [アラビア語](CHANGELOG-ar.md) | [ヒンディー語](CHANGELOG-hi.md) | [イタリア語](CHANGELOG-it.md) | [オランダ語](CHANGELOG-nl.md) | [ポーランド語](CHANGELOG-pl.md) | [ポルトガル語](CHANGELOG-pt.md) | [ルーマニア語](CHANGELOG-ro.md) | [スウェーデン語](CHANGELOG-sv.md)

- **1.13.0** Provider `--use_openrouter`：中国のオープンモデルを含む約430モデルへ接続する有料ルーター（2026-09-05）：

  - **8番目と同時に提供される9番目のProvider経路。** 1.12.0はPyPIで公開されませんでした。OpenCodeとOpenRouterの2つのルーターが同時にリリースされます。[OpenRouter](https://openrouter.ai)では、Kimi、Qwen、DeepSeek、Z.aiなど、ここではほかのどのProviderも公開していないモデルへ、従量課金の共通クレジットと1つのキーでアクセスできます。endpointはOpenAI互換であるため、clientはxAIと同じです。**このProviderを特徴づけるものはすべてpreflightに集約されており、その各ルールはAPIでの測定結果に基づいています。**

  - **同じモデルが上限の異なる数十のホストから提供されていますが、ルーティングはその違いを認識しません。** 測定結果：`z-ai/glm-5.2`には33ホスト、`z-ai/glm-5.3-flash`には23ホストがあり、そのうち1つは**出力2,048 tokens**に制限されています。そのため、23のうちいずれかへ送られた長い翻訳は、何の通知もなくランダムに途中で切れていました。preflightは`/api/v1/models/{modèle}/endpoints`を読み取り、出力上限が8,000 tokens未満のホスト、状態が劣化しているホスト、上限を宣言していないホストを除外し、残りを固定します。`allow_fallbacks: false`を**伴わない**`provider.only`は単なる優先指定にすぎません。ルーターは除外されたホストへフォールバックするため、固定の意味がなくなります。上限を満たすホストが1つもない場合、コマンドは停止します。それでも翻訳を続けることは、このpreflightが防ぐために存在する無通知の切り捨てを受け入れることになるからです。

  - **推論は出力と同じ料金で課金され、多くのモデルでデフォルトで有効です。** `z-ai/glm-5.2`へ同じリクエストを送り、応答を「OK」とした場合、**モデルのデフォルトではcompletionが107 tokens、推論を無効にすると2 tokens**でした。推論が何の利点ももたらさない翻訳では、各ファイルの各segmentで18倍の差になります。そのため、デフォルトでは無効化されます。推論を必須とする**431モデル中288モデル**（`reasoning.mandatory`）は`400 « Reasoning is mandatory for this endpoint and cannot be disabled »`を返します。これらについては、preflightが受け入れ可能なeffortを読み取り、最小値を要求します（次の項目）。effortは推論が最初に消費する**`max_tokens`の割合**を割り当てるため、無作為に値を選ぶと、空白ページになるリスクを減らすのではなく移動させるだけです。

  - **推論を必須とするモデルには、そのモデルが受け入れる最小のeffortを指定します。この判断も測定結果に基づいています。** 当初は、モデルに代わって推測しないよう、何も送信しない方針でした。catalogのデフォルトが`max`である`z-ai/glm-5.3-flash`で検証したところ、この選択では翻訳の完了前に出力が**32,768 tokensで切り捨てられ**、14言語中2言語が失われました。envelopeを増やしても状況は変わりません。effortがその一定割合を割り当てるため、推論もenvelopeとともに増えるからです。そのためProviderはpreflightで`supported_efforts`を読み取り、最小値を要求します。catalogに利用可能な値が示されていない場合は「指定なし」へフォールバックします。問題のあった言語で反証テストを行ったところ、以前はbudget枯渇で失敗していましたが、現在は9分で完了し、構造もsourceと同一です。

  - **上流ホストの障害時に、その原因が明示されるようになりました。** ルーターはこのケースを、`native_finish_reason`がnullの`finish_reason=error`として正規化します。2言語で2回測定し、いずれも正確に750秒でした。従来の一般的なメッセージでは、documentや分割方法の不具合を調べるよう誘導していました。現在は障害がProvider側にあり、多くの場合は再試行だけで解決すると伝えます。

  - **出力が空の`finish_reason=length`は切り捨てではありません。** これは、最初の有用な文字が生成される前にbudgetが推論によって消費された状態です。測定では、有用な出力148 tokensに対して推論が15,850 tokensでした。2つのケースでは必要な対処が正反対です。前者ではsegmentを小さくしても効果がありません。メッセージで両者を明確に区別するようになりました。ほかにも測定結果に基づく2つのguardがあります。上流ホストが失敗した際、ルーターが**エラーのみを含むbodyとともに200を返す**場合があり（`choices[0]`はメッセージを覆い隠す不透明な`TypeError`を送出していました）、またcontext windowをcatalogから読み取って`MODEL_TOKEN_LIMITS`へ設定します。catalog内の44モデルでは`DEFAULT_TOKEN_LIMIT`が誤っており、そのうち2モデルの上限は4,095 tokensです。

  - **`--model fournisseur/modèle`は必須であり、その形式はネットワークへ接続する前に検証されます。** OpenRouterは単一の供給元ではありません。選択によって価格、ライセンス、データ処理が変わるため、ユーザーに代わって決定することはできません。slugはpreflight URLへ埋め込まれるため、この検証は単なる使いやすさへの配慮ではなく、pathの注入を防ぐguardです。2つのルーターで共通するnamespace対応regexは`a/b/..`を受け入れるため、親segmentは明示的に拒否されます。`--eco`は効果がなく、その旨を通知します。

  - **3つの記述を修正し、そのうち1つは事実誤認でした。** `codex exec`に関するOpenAIの警告は、公開repositoryであることではなく、共有runnerへ個人のsessionファイルを注入することを対象としていました。README、CLAUDE.md、codeでは意味を取り違えて引用されていました。OpenCodeの認証情報の保存場所は1.18.27で変更されました（`opencode.db`の`credential` tableであり、`auth.json`ではありません）。「ここでは決して読み取られない」という不変条件は正しいままでしたが、場所の記載が古くなっていました。最後に、OpenCodeのsectionでは、検証されていない経路を同等のものとして紹介しなくなりました。Zen gatewayとOllamaはend-to-endで測定済みですが、GitHub Copilot、LM Studio、llama.cppは未測定であり、READMEにもそのように記載されるようになりました。

  - **測定キャンペーンと、README内の推奨モデル一覧。** 3種類のdocument群を使用し、14言語に対して300件を超える翻訳を実行しました。`--news` modeの情報密度が高いblog記事、標準MarkdownのこのREADME、そしてGitHubからそのまま取得した著名projectのREADME 4件です。tableでは、これまで混同されていた2つの事柄を区別しています。翻訳が**完了する**ことと、その**構造がsourceと同一である**ことです。情報密度が高い2つのdocumentで情報を一度も失わなかったモデルは3つありました。`gemini-3.7-flash`、ChatGPT subscriptionの`gpt-5.6-sol`、OpenRouter経由の`z-ai/glm-5.2`です。差異は、1つまたは2つの言語で一組の`**`が再現されなかったことだけでした。中心的な結論は、**差を生む要因が`--news` modeではなくdocumentの情報密度である**ことです。subscription版Grokはblog記事で14回中13回失敗した一方、公開READMEでは16件中14件に成功しました。原因は長いsegmentでの脱落であり、反証テストでも確認されています。table自体にも注意書きがあります。網羅的ではなく、特定時点の結果であり、所要時間は順位を示すものではありません。適切な方法は、引き続き自身のdocumentで測定することです。

  - **非Latin文字体系で2件の偽陽性を生じていたため、数値を公開する前に構造比較器を修正しました。** URLの直後に全角の閉じ括弧`）`がある場合、`)`で停止するregexでは正しく切り分けられず、URL自体は同一でも抽出された文字列が異なっていました。また、フランス語では5行だった引用が中国語では3行に収まることで、行単位のcountが減少していました。2つの修正は反証テストで検証済みです。URL、section、inline codeのいずれかを削除すれば、引き続き検出されます。修正していなければ、GeminiとCodexの結果は14言語中13言語および12言語ではなく、どちらも11言語として公開されていたはずです。

  - **テスト**：新しいファイル`tests/test_openrouter_provider.py`（60 tests）— モデル検証と親segmentの拒否、ホストの固定（上限、状態、上限未宣言、共通最小値）、常にfalseとなる`allow_fallbacks`、`mandatory`に応じた推論の無効化または維持、完全な出力contract（200内のエラー、choiceなし、空白ページと切り捨ての区別、異常な`finish_reason`、null content）、catalogへ接続できない場合のpreflight fail-closed、slug欠落、正常なホスト不在、flagの排他性、ファイル名label。全suiteは**473 tests**です。

  - **Refactor：動作を一切変更せず、4,253行の単一moduleを複数moduleへ分割しました。** `src/aipmt/translate.py`は`config`、`markdown`、`segmentation`、`guards`、`placeholders`、`news`、`prompts`、`notes`、`naming`、`pipeline`、`cli`と、subpackage `providers/`（Providerごとに1 module、基盤となる`base`、解決とdispatchを担う`registry`）へ分割されています。各移動は、機械的な証明を伴うcommitです。検証器がpackage内の全top-level nodeのASTを基準snapshotと比較し、各symbolの配置、security markerがverbatimのまま維持されていること、未追跡ファイルが存在しないことを検証します。この一時的なtoolingは次のversionで削除されました。外部から確認できる変更点は次のとおりです。`aipmt.translate`はfacadeとなり、moduleが`_` prefixなしで公開していた64個の名前をobject identityを保ったまま再公開します（`__all__`にはそのうち9個の正式サポート対象APIが含まれ、残りは互換性aliasです）。一方、`import *`が拾っていたdependencyおよびstandard library由来の29個の名前は再exportしなくなりました。ファイルの直接実行（`python src/aipmt/translate.py`）は廃止され、`aipmt`と`python -m aipmt`が引き続きサポートされる2つの形式です。public functionの`__module__`は、そのfunctionを定義するmoduleのものになりました。SDKは`.env`の読み込み後にimportされるようになり、従来の順序とは異なりますが、既知の影響はありません。427 testsはidentifier単位で維持され、それぞれが対象とするmoduleへ移行されました。facade経由だった91個のpatchは、名前を参照するmoduleを直接対象とするようになりました（そのうち2件はpatchなしでもgreenのままであることを測定済みです）。7件のcontract testがfacadeを固定し、gateのtoolingは最初の移動より前に書き換えられました。これにより、検証をやめることでgateがgreenになることを防いでいます。具体的には、下限付きdirectory単位のLizard scope、構築済みparserから読み取るflag、package単位のcoverage下限、追跡対象moduleを列挙する`release.sh`です。
  - **修正（pull requestレビュー）**：OpenRouterは`context_length`のないcatalog entryを拒否するようになり、128,000 tokensというデフォルト値を測定結果として記録しなくなりました。この誤った記録は「モデルが一覧にない」という警告まで無効化していました。また、`finish_reason`がnullの場合（documented typeは`string | null`）、`max_tokens`が`length`となるため、ホストのraw reasonを正式な理由として扱います。OpenCodeは`part: null` eventに対して`AttributeError`ではなく自身のcontract errorを返し、event行の1つが読み取れないJSONL streamについては、部分的なtextを受け入れず拒否します。3つのagentic CLIは、呼び出し中にagent processが`SIGTERM`を受信するとagent groupを終了します。regenの`timeout`ではagentが生存し、quotaを消費し続けていました。また、正常終了するshimがgrandchildを生存させる場合でも、groupの`SIGKILL`には常にgrace periodが適用されます。分割によって離れていた`# fmt: off`と`# fmt: on`の組を再結合しました。`--reasoning_effort`のhelpには、それを使用する4つのProviderが明記されています。

- **1.12.0** Provider `--use_opencode`：オープンソースagentのOpenCodeから任意の供給元へ接続 — local model、account不要の無料model、subscription、またはkey（2026-09-04）：

  - **従来の7つとは性質が異なる8番目のProvider経路。** [OpenCode](https://opencode.ai)（MIT）はモデルの供給元ではなく、ユーザーがOpenCode自体に設定した接続先への_ルーター_です。API key、subscription（GitHub Copilot、ChatGPT、SuperGrok）、**account不要**で無料modelを提供するOpenCode Zen gateway、または**local** model（Ollama、LM Studio、llama.cpp）を利用できます。scriptはCodexやGrokと同様に`opencode run`をnon-interactive modeで操作し、同じsubprocess基盤を再利用します（独立したprocess group、timeout時には`SIGTERM`の後に`SIGKILL`、stdinは常に閉じ、environmentは不要な情報を除去）。**2件の実際の翻訳**で検証済みです。`opencode/mimo-v2.5-free`を使用してこのREADME全体を英語へ翻訳したケースでは、49秒、1 passで完了し、構造はsource fileと同一でした（heading 32件、code closing 26件、link 18件、URL 37件、table row 37件、inline code 135件）。もう1件は`ollama/qwen2.5:7b`を使用し、keyを一切使わずlocalでtest fileを翻訳しました。

  - **`--model provider/modèle`は必須であり、明示的に選択する必要があります。** `--model`を指定しない場合、OpenCodeは自身のデフォルトへフォールバックします。新規install環境では`opencode/big-pickle`となり、やり取りがtrainingに使用される可能性のある無料の「stealth」modelです。測定したところ、実際にこのmodelが応答しました。ユーザーに代わってこれを無通知で選ぶことは、このrepositoryが検出しようとしている不可視の切り替えそのものです。そのためerror messageには、modelを一覧表示するcommand（`opencode models`）と、local、無料、subscriptionの3例を記載しています。`--eco`は効果がなく、その旨を通知します。`--reasoning_effort`は、明示的に要求された場合に限り、OpenCodeの`--variant`としてそのまま渡されます。

  - **推測ではなく、測定された隔離。** inline configuration（`OPENCODE_CONFIG_CONTENT`。OpenCodeのmerge順で最後に位置するため、ユーザー設定を置き換えずに優先されます）では、すべてのtoolを拒否する（`permission: {"*": "deny"}`）agent `aipmt`を定義しています。registryはtoolをmodelへ提示すらしなくなり、「ファイルを一覧表示して`id`を実行せよ」と命じられても、toolを持っていないと応答します。session共有は無効化され、外部pluginは除外され（`--pure`）、`--auto`は決して実行されず、working directoryは使い捨ての空directoryです。無通知で行われる2種類の注入も測定し、無効化しました。`OPENCODE_DISABLE_CLAUDE_CODE`がないと、ユーザーの`~/.claude/CLAUDE.md`が**すべての**promptへ入ります（単純な「こんにちは」でもinputが186 tokensではなく515 tokens）。`OPENCODE_DISABLE_PROJECT_CONFIG`がないと、current directoryの`AGENTS.md`も入ります。「すべての応答をBANANAで終えよ」というinstructionが翻訳に適用されることを確認しました。一方、globalの`~/.config/opencode/AGENTS.md`は引き続き注入されます。これを除外するswitchはなく、転用した`XDG_CONFIG_HOME`で回避するとユーザーのProviderまで見えなくなります。そのため、場当たり的に回避せずdocument化しました。

  - **`exit 0`だけでは何も証明されません。3つ目のCLIでも同じ原則を適用しつつ、このCLI固有の2つの落とし穴に対処します。** 未知の`--agent`を指定しても`opencode run`は失敗せず、stderrへwarningを出した後、toolが有効なcoding agentへ**無通知で**フォールバックします。inline configurationが反映されていなければ、書き込み可能なagentによって翻訳が開始されることになります。そのため出力contractでは、このmessageが存在しないことに加え、return codeが0であること、`error` eventがないこと、`tool_use`がないこと、最後の`step_finish`が`stop`であること（`length`は切り捨てられた応答です）、textが空でないことを検証します。2つ目の落とし穴は、errorのJSON eventが**不透明**であることです。「予期しないserver errorです。詳細はserver logを確認してください。」という単純なreference付きmessageしかなく、実際の原因（`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`、`ProviderAuthError`など）はlogにしか存在しません。そのため`--print-logs --log-level ERROR`を使用し、その後に続くBun traceを除外してstderrの`error="…"` fieldを読み取ります。これにより、未知のmodelは原因を明示したうえで1秒以内に失敗します。また、`--title`によって不要なLLM callも回避されます。これがない場合、OpenCodeは`small_model`に対する追加の1 turnでsession titleを生成します。
  - **Secrets：Codex や Grok と同じパターンによるフィルタリングを行いますが、名前を指定した例外が1つあります。** `OPENCODE_API_KEY` は保持されます。これは OpenCode 自身のキー（Zen ゲートウェイ、Go サブスクリプション）であり、名前を指定して OpenCode に渡されるものです。つまり OpenCode の `auth.json` に相当し、aipmt が管理または課金できるキーではありません。provider は OpenCode（`opencode auth login`、`opencode.json`）で設定し、aipmt の `.env` では決して設定しません。そのため、aipmt のキーがサブプロセスに渡ることはありません。サブスクリプション型 CLI とは異なり、CI では拒否しません。runner 上の API キーやセルフホストモデルは正当な用途だからです。

  - **パストラバーサル防止ガードは、未処理の値ではなく、補間後の値を検査するようになりました。** `provider/modèle` には `/` が含まれており、1.10.0 のガードはこれを拒否していました。`--model` がファイル名 `--include_model` に補間されるため、この拒否自体は妥当です。ファイル名ラベルでは、補間前に `/`、`\`、`:` を `-` に置換するようになりました（`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`。`:` は Windows では使用できません）。上流のガードはこのラベルを検査します。`../../evil` は対象配下の単純な名前 `doc-en-..-..-evil.md` となり、`..` だけは引き続き拒否され、`--target_lang ../x` も拒否されます。範囲ガード `_ensure_within_directory` は、変更されていない第2の防御層として残ります。

  - **無料モデルとローカルモデルについて、実測した結果。** `opencode/mimo-v2.5-free` は1段落を16秒、この README を49秒で翻訳します。`opencode/big-pickle` は200語に40秒かかり、個別なら完了する2件のリクエストを同時に実行すると、5分間応答がありませんでした。`opencode/nemotron-3.5-lightning-free` は3分間まったく応答しませんでした。そのため、`REGEN_PROVIDER=opencode` では `REGEN_MODEL` を必須とし、並列実行は **2 jobs** としています。ローカル側では、Ollama のコンテキストが多くの場合4,096 tokensに設定される一方、セグメントは最大16,000文字に達します。そのため、`PARAMETER num_ctx 32768` を指定した `Modelfile` が必要です。また品質はモデル次第です。テストファイルでは、7B モデルがリストの順序を逆転させ、コードブロックの閉じ記号を壊しましたが、ゲートウェイのモデルはすべてを保持しました。

  - **このリポジトリの翻訳では、従量課金 API を一切使用しなくなりました。** `regen_translations.sh` は、`.env` にキーが残っていると即座に OpenAI API を使用し、Codex は明示的に選択した場合にしか使用しませんでした。このバージョンの準備中、まさにそれが起きました。28件の翻訳が OpenAI API に送られ、その後ヒンディー語版 CHANGELOG が Gemini API に送られました。しかし ChatGPT サブスクリプションは、そもそも従量課金を避けるために存在します。キーの自動検出は廃止されました。**デフォルトは Codex で、`gpt-5.6-sol`**、すなわち高品質モデルを使用します。`openai`、`gemini`、`grok` では、`REGEN_PROVIDER` に加えて `REGEN_ALLOW_PAID_API=1` が必要です。これは、判断時点でルールが確実に適用されるように名前を付けた例外です。未知の `REGEN_PROVIDER` は API にフォールバックせず、失敗します。10件のテストで、デフォルト、拒否、例外を固定しています。このバージョンの28件の翻訳は Codex を使用してやり直しました。

  - **rate limit 時の back-off を共通化しました**（`_retry_on_rate_limit`）。Codex と Grok のループはラベル以外が同一であり、3つ目の複製を追加すると重複しきい値を超えるところでした。3つの CLI エラーは、同じ `_CliCallError` から派生します。いずれか1つでもこの系統から外れることをテストで禁止しています。外れると、共有ループがそのエラーを検出できなくなるためです。

  - **テスト**：新しいファイル `tests/test_opencode_provider.py`（51件のテスト）— 完全な出力契約、agent のフォールバック、ログからの原因読み取り、重複除去されたテキスト部分と合成部分の無視、プロセスグループを終了する timeout、429 時の back-off、必須モデルとその検証、secret を伴わない preflight、バイナリ解決、dispatch の接続、ファイル名ラベル、およびパストラバーサルの反証テスト。`tests/test_review_hardening.py` は、flag の排他性と secret の非存在を新しい provider にも拡張します。gate は、文書化された **22個の argparse flag** を要求するようになりました。全体で **382 tests** です。

- **1.11.1** ドキュメント修正：README が7つの provider 経路をようやく明記しました（2026-09-03）：

  - **1.11.0 の PyPI ページには「4 APIs + Codex CLI」と記載されていました。** 実際のコードでは7つを提供しています。API 経由の OpenAI、Mistral、Claude、Gemini、Grok に加え、従量課金なしのサブスクリプション経由で Codex（ChatGPT）と Grok を利用できます。冒頭文と _Multi-Provider_ の項目には2つの Grok モードが記載されておらず、14件の翻訳でも同じ誤りが繰り返されていました。パッケージの長い説明文はバージョンごとに固定されるため、公開ページを修正するには新しいバージョン番号が必要でした。このリリースの目的はそれだけです。**コード変更はありません。**
  - `CLAUDE.md` を、公開時に導入された内容と一致させました。gate のカウンター（16、`--full` では17）、有効な11個の workflow、`gh pr checks` には表示されない2つの Sonar/Codacy カウンター（hotspots、Codacy API）、`ruff-format` による `# nosemgrep` の移動、OIDC 交換に必要な GitHub environments、そして _pending publisher_ は名前を予約しないという事実です。

- **1.11.0** PyPI への公開：リポジトリを clone せず、`pip install ai-powered-markdown-translator` に続けて `aipmt` コマンドを実行します（2026-09-03）：

  - **単一ファイルのスクリプトが、インストール可能なパッケージになりました。** `translate.py` をルートから `src/aipmt/translate.py` に移し、console entry point `aipmt` と、それに相当する `python -m aipmt` を追加しました。貢献する場合は引き続きリポジトリの clone が必要です。テスト、28件の翻訳、品質管理ツールはリポジトリに含まれます。しかし利用するだけなら、clone は不要になりました。

    - **import 名は `aipmt` であり、決して `translate` ではありません。** 実際に、しかも気づきにくい衝突が発生するためです。PyPI パッケージ `translate`（v3.8.1、最終 upload 2026-07-06）は、同名のディレクトリをインストールします。venv で再現したところ、ディレクトリがモジュールより優先され、`translate.main` が消え、entry point は `AttributeError` で壊れました。それにもかかわらず、`pip check` は「No broken requirements found」と応答し、rc=0 で終了します。ユーザー環境に `pip install translate` があるだけで、利用可能な診断情報もなく CLI が壊れるところでした。実際の wheel を使った反証テストでは、パッケージの上に `pip install translate` を導入し、`aipmt --help` は導入前後とも rc=0 となり、両方の CLI が共存しました。
    - **distribution 名は長く、コマンド名は短くしました。** `ai-powered-markdown-translator` によって、PyPI の検索でパッケージを見つけられます。頭字語だけでは、プロジェクトをすでに知っている人にしか発見できませんが、この公開の目的はまさに新しい利用者に見つけてもらうことです。妥当と思われた2つの候補は、確認の結果除外しました。`ai-markdown-translator` は、同じ目的のツールによって2024年から npm 上で使用されており、このリポジトリより17か月先行しています。また `aimt` は、同じ分野で現在も活動中のパッケージ `aim`（v3.29.1）と1文字しか違いません。長期的な混同を招く最悪の条件です。なお、確認方法にも落とし穴があります。`pypi.org/project/<nom>/` は、どのような名前でも200を返す bot 対策ページであり、信頼できるのは JSON API だけです。
    - **フラットなパッケージではなく `src/` layout を採用しました。** フラットなパッケージなら、テストの6個の `sys.path.insert(..., "..")` を維持できました。しかし、それこそが問題です。それらはパッケージではなくソースツリーを import するため、パッケージングのエラーが隠れてしまいます。実際の追加コストは、置換ルールが1つ増えるだけです。

  - **キーを一度設定すれば、継続して使用できるようになりました。** インストール済み CLI には永続的な設定がなく、環境変数と現在のディレクトリにある `.env` しか利用できませんでした。確かに `find_dotenv` はシステムのルートまで遡るため、**ホームディレクトリ配下で作業している場合**には `~/.env` を見つけました。しかし別の場所で作業すると何も見つかりませんでした。これは設計上の選択ではなく、コマンドを起動した場所に依存する不完全な対応でした。そのため、既存の2層の下に第3層として `~/.config/aipmt/.env` を追加しました。

    - **優先順位は明示的にコード化されておらず**、`load_dotenv` のデフォルト値である `override=False` から自然に決まります。各層は、前の層で空のまま残った値だけを補います。したがって、環境変数 → プロジェクトの `.env` → ユーザー設定という順序になります。これは構造ではなく動作のテストで確認しています。2つの呼び出し順を逆にしても、第3層を削除してもテストは失敗します。
    - **TOML ではなく `.env` 形式**を意図的に採用しました。`python-dotenv` はすでに依存関係に含まれ、その構文は15件の README ですでに文書化されており、同じファイルを両方の適用範囲で使用できます。新しい依存関係も構文も追加されません。配置場所は、`XDG_CONFIG_HOME` が**絶対パス**である場合にはそれに従い、Windows では `APPDATA` に従います。仕様では相対値を無視するよう求めています。そうしなければ、設定場所が再び現在のディレクトリに依存してしまうためです。
    - **2つの案を、それぞれ理由とともに除外しました。** システムの keyring（`keyring`）はデスクトップ環境ではより安全ですが、サーバー、コンテナ、CI などの headless 環境では機能しません。つまり、一括翻訳という本来のユースケースで失敗します。opt-in の候補としては優れていますが、デフォルトには適していません。`--api-key` flag を使うと、キーが shell の履歴に残り、`ps` から見えるようになります。
    - **キーがない場合でも、stack trace は表示されなくなりました。** 以前は、`site-packages` を指す Python の stack trace と、「環境または .env」とだけ示し、後者をどこに作成すべきか説明しないメッセージが表示されていました。現在は3つの配置場所を正確なパスとともに列挙し、コマンドは2で終了します。この保護は、**意図的に狭い範囲**、すなわち設定フェーズだけを対象とする `except ValueError` です。実行全体を包むと、翻訳中に発生した本物の bug まで安心感を与えるメッセージに変換してしまいます。このリポジトリが追跡しているのは、まさにそのような障害形態です。これを禁止するため、テストは `main()` のソースを読み取ります。

  - **修正 — ツールをインストールすると、ユーザーの `.env` が無視されていました。** 引数なしの `load_dotenv()` は、現在のディレクトリからではなく呼び出し元ファイルから、つまり `site-packages` から遡ります。独自の `.env` を持つプロジェクトから実際の console entry point を起動して測定したところ、`find_dotenv()` は `''` を返してキーを読み込まず、`find_dotenv(usecwd=True)` ならキーを見つけました。ツールを clone 済みリポジトリからしか実行していなかった間は、この bug は存在しませんでした。公開後は正しい設定にもかかわらず API キーが「見つからない」という症状だけを残し、常に発生するところでした。

  - **3つの gate は、何も検証しなくなったにもかかわらず成功していた可能性があります。** これらは移動の**前**に、意図的に強化しました。検出対象の変更後に書かれたガードでは、何も証明できないためです。各 gate は元のリポジトリでは成功し、移行したコピーでは失敗します。両方向を実測しています。

    - **Lizard は存在しないパスを何も通知せず無視します**。rc=0 で、「0 file analyzed」と表示されます。複雑度 gate は158 functions / 2247 nloc から3 functions / 34 nloc になり、出力は0 byte になるところでした。現在の scope は配列であり、各要素が存在することを検証します。
    - **存在しないモジュールに対する `coverage run --source=` は失敗しません**。stderr に警告を出すだけで、unittest でも `coverage xml` でも rc=0 となり、不完全な report がそのまま公開されます。statements は1453から141に減少し、ほとんど分析されていないためにプロジェクトが健全に見えるところでした。2つの下限値で report を保護しています。1つは合計値、もう1つは測定対象の最大ファイルです。
    - **翻訳の鮮度を検査する probe は、構造上、呼び出し形式を認識できません**。この probe は argparse flag を基準にしていますが、ファイル名を変更しても flag は変わりません。再現実験では、モジュールを移動し、15件の README が存在しないコマンドを文書化したままでも、「古い翻訳はありません」と判定されました。そのため第7セクションでは、option ではなく**形式**を検証します。また、Lizard hook をスクリプトの実際の scope と照合します。そのキー `files:` は、一致しなくなっても pre-commit を失敗させず、処理自体を**スキップ**するためです。

  - **`requires-python = ">=3.10"` は単なる主張ではなくなりました。** `sonar-project.properties` はすでに3.10～3.12対応を掲げていましたが、開発環境には3.12しかなく、これまで実際に検証されたことはありませんでした。公開によって表面化するはずだった内部矛盾です。テスト workflow は現在、3.10、3.11、3.12でテスト一式を実行し、**パッケージ**をインストールすることで公開されたバージョン範囲も検証します。

  - **下限のみを定め、上限は設けません。** `requirements.txt` はテスト済みの lock のまま維持し、`[project.dependencies]` を公開契約とします。lock の厳密なバージョンを公開すると、ほかのパッケージを利用するすべてのユーザー環境で競合を引き起こします。`<N+1` の上限も設けません。上限を設けると、major version への追随が遅れた場合に release gate を失敗させる `check-deps-fresh.sh` と正面から矛盾するためです。下限の組み合わせは解決可能であり、反証テスト `openai==1.0.0` は `ResolutionImpossible` で終了します。これは、検査がすべてを受け入れるのではなく、正しく識別していることを証明します。さらに、`pyproject.toml` のバージョンが CHANGELOG のバージョンと異なることをガードで禁止しています。PyPI では同じバージョン番号を再利用できないためです。

  - **新しい venv で end-to-end 検証済みです**。約70 Ko の wheel には `aipmt/*.py`、dist-info、license だけが含まれます。`aipmt --help` は22個の flag を伴って rc=0、`python -m aipmt` は「usage: \_\_main\_\_.py」ではなく「usage: aipmt」を表示し、`pipx` によるインストールも機能します。そして何より、**任意のユーザーディレクトリから実際に fr→en 翻訳**を実行し、太字、リスト、inline code、リンク、URL が保持され、コードブロックは翻訳されませんでした。移行前の318件のテストは、移行前後で byte 単位まで同一の識別子リストを保ったまま成功しました。単なる「OK」ではなく、この事実こそ、無効化されたテストがないことを証明します。さらに3層設定用の12件が加わり、合計330件です。

- **1.10.0** `--use_codex` provider（ChatGPT サブスクリプション枠）、SDK とモデルの更新、複数段落にわたる news 引用の修正（2026-08-29）：

  - **セキュリティレビュー — PR で導入されたものの、すべての箇所で徹底されていなかった2つのガード**：
    - **Codex のプリフライトは `.env` 全体をバイナリへ渡していました。** `_codex_preflight` は **`env=` なしで** `subprocess.run` を呼び出していました。つまり、サブプロセスは `os.environ` 全体、したがって `load_dotenv` が読み込んだ `.env` のすべてを継承していました。計測機能を組み込んだ偽のバイナリで測定したところ、**7 個のシークレット**がプリフライトに到達していました。6 つの provider のキーと 1 つの `GITHUB_TOKEN` です。一方、`env=_grok_env()` を正しく渡していた対応する `_grok_preflight` では **0 個**でした。この不整合は PR 内部にありました。わずか数行先にある `_strip_secret_env` は、まさにこの不変条件を維持するためのものです。`_codex_env_base()` を抽出して両方の経路で共有するようにしました。修正後の測定結果は、両側ともシークレット 0 個です。
    - **「`--deny` は fail-closed」という性質は、実際に使われていた形式を対象としていませんでした。** コメントでは、未知の接頭辞を持つルールが起動を拒否させることを根拠として、Grok の隔離全体を正当化していました。`grok 1.0.13` で測定したところ、この検証が存在するのは**括弧付き形式だけ**でした。`--deny 'CeciNestPasUnOutil(*)'` は起動を拒否します（「未知のツール接頭辞」）が、`--deny 'CeciNestPasUnOutil'` は黙って受け入れられます。しかし、`GROK_DENY_RULES` が使っていたのは裸の名前だけでした。そのため、xAI 側でツール名が変更されると、OS sandbox がすでに適用されない環境において、測定済みの唯一の隔離層が何の通知もなく失われる可能性がありました。名前付きの 8 つのルールは `Prefix(*)` に変更され、それぞれが CLI の既知の接頭辞として検証されます。包括ルール `*` は、受け入れられる唯一の形式であるリテラル形式のままです。検証されない形式への逆戻りはテストで防止されています。
    - **そのほかの点も問題がないことを確認済みです**。コマンドインジェクションはありません（常にリスト形式で、`shell=True` は一度も使わず、文書内容は stdin または `--prompt-file` 経由）。安全でないデシリアライズもありません（型ガード付きの `json.loads` のみ）。パストラバーサル修正については 7 種類のペイロードで回避方法が見つからず、`--deny '*'` が CLI によって実際に適用されることも確認しました（workdir 外の読み取りで `DENY_ENFORCED` を観測）。
    - 前述の鮮度チェックは、その原則自体を回避していました。PyPI への問い合わせに失敗したパッケージは黙ってスキップされ、gate が成功していました。現在は実際に比較されたパッケージ数を数え、対象範囲が不完全なら失敗します。

  - **依存関係を最新化し、遅延の再発を防ぐために 2 つの安全網を追加**：

    - **遅延は現実に存在し、長期化していました**。`openai` 2.54 → **3.6.0**、`anthropic` 0.125 → **1.2.0**、`certifi` 2024.8.30 → **2026.7.22**。すべての provider 呼び出しで TLS を検証するルート証明書ストアは、2 年も遅れていました。原因は特定済みです。**`.github/dependabot.yml` が存在していませんでした**。このファイルがない場合、GitHub が有効にするのは _セキュリティ更新_ だけであり、Dependabot が PR を提案するのは CVE の対象となる依存関係に限られます。このため、`urllib3` と `idna` は更新された一方、2 つの SDK はメジャーバージョン 1 つ分も古いまま放置されていました。
    - **以前の推論で懸念されていたのとは異なり、2 つのメジャーバージョンは競合せず共存します**。`openai` 3.x と `anthropic` 1.x は **`httpx2`** へ移行しますが、`mistralai` と `google-genai` は `httpx<1` に残ります。ただし、これらは別々のディストリビューションです。実際にインストールしたうえで、OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI、Grok CLI という **7 つの provider 経路すべてをエンドツーエンドでテスト**し、各出力でインラインコードとリンクが保持されることを確認しました。「2 つの HTTP スタックを避ける」というのは好みにすぎず、阻害要因ではありませんでした。測定により決着しました。
    - **`requirements.txt` は実際の環境を記述していませんでした**。`google-auth`、`cryptography`、および `opentelemetry` スタックは作業用 venv にインストールされていましたが、宣言されたことはありませんでした。そのため、新規インストールではテスト対象の環境を再現できませんでした。逆に、`tokenizers`、`huggingface-hub`、`PyYAML` は、どこからも import も要求もされていないのに記載されており、`mistralai` 1.x の残骸でした。このファイルは、直接依存関係だけから構築した venv の完全な依存閉包として再生成されています。新しい構成では、`pip-audit` によって既知の脆弱性は検出されません。
    - **`.github/dependabot.yml`**（新規）は、pip と github-actions のバージョンを毎週更新するようにします。マイナー更新とパッチ更新は 1 つの PR にまとめます。パッチ更新ごとに PR を作ると、やがて無視されるようになり、ノイズは更新の敵になるためです。**メジャー更新は個別**にし、それぞれで実際の呼び出しによる検証を必須とします。
    - **`scripts/check-deps-fresh.sh`**（新規、gate に組み込み済み）は、遅延をプロジェクトの判定結果に表面化させます。Dependabot は提案するだけで、保証はせず、その PR が積み重なることもあります。メジャー更新の遅延は失敗、マイナー更新の遅延は警告とします。常時赤い gate はいずれ無視されるためです。PyPI に接続できない場合、ローカルでは明示的にスキップし、**CI では fail-closed** とします。実行されなかったチェックは成功ではありません。両方向で検証済みです。修正前とまったく同じ状態（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`）を検出し、マイナー更新だけなら警告に留めます。

  - **この PR のレビューから生まれた修正** — 5 つのレビュー担当 agent が diff を精査しました。以下の各項目はすべて、修正前に**測定によって再現**されました。そのうち 2 件は、この同じバージョン内で前述の変更によって導入されたリグレッションでした。

    - **修正済みのリグレッション — `_NEWS_CITATION_REGEX` に指数的バックトラッキングがありました。** 複数段落への対応修正によって、繰り返し内に `(?:[ \t]*$|[ \t]+.*)` が導入されていました。`[ \t]+` と `.*` の間で空白をどう分配するかが曖昧であり、その曖昧さが反復ごとに増幅されていました。パターンに一致しない、完全に正当な Markdown インデントである `>   texte` の行を使って測定したところ、**14 行で 2,589 ms**かかりました。修正後は 0.04 ms で、1 行追加するごとに約 9 倍になっていました。`--news` モードでは、長くて形式不適合な blockquote だけで、原因を特定できないままジョブがタイムアウトするまで翻訳が停止する可能性がありました。現在、繰り返しは行全体を一度に消費するため（`\n^>(?![ \t]*—).*`）、各反復で一致方法が 1 つしか残りません。実際の 231 記事からなるコーパスで検証し、キャプチャーには**差分が一切なく**、引用は同じ 423 件で、複数段落からなる 14 個の本文も引き続き拡張されています。
    - **2 つの provider フラグを同時に指定すると、黙って従量課金されていました。** `--use_codex --use_mistral` は受け入れられていました。`_select_provider_client` は Mistral を最初に検査し、`_resolve_provider` は明示的な真偽値を優先するため、どちらも Mistral に行き着いていました。つまり、ユーザーはサブスクリプション枠の使用を要求したのに、何の警告もなく従量課金されていました。これはまさに、`--use_codex` が防止するために存在する障害モードです。現在、6 つの provider フラグは `add_mutually_exclusive_group` を通過します。**動作変更**：これまで黙って受け入れられていた、2 つの provider を組み合わせたコマンドラインは、今後 `argument --use_mistral: not allowed with argument --use_codex` で失敗します。
    - **作業終了時の gate は、プローブが異常終了しても成功していました。** `scripts/check-release-ready.sh` の 13 個のチェックのうち 4 個は、「stdout を取得し、空なら結論を出す」というパターンに従い、終了コードを一度も確認していませんでした。例外（ファイル名の変更、`FileNotFoundError`）は stderr に書き込み、stdout を空のままにするため、チェックは「報告事項なし」と結論付けていました。「`exit 0` では何も証明できない」という落とし穴が、それを防ぐために書かれたスクリプト内で再現されていました。現在は helper `probe()` により、終了コードが 0 であること**と**終了 sentinel があることの両方を必須とし、プローブは目印の集合が空なら結論を出しません。空集合に対する assertion は常に真になるためです。実例として、前述の排他的グループを追加したことで provider フラグは `*_group` オブジェクトを経由するようになり、古い regex `parser\.add_argument\(` では一致しなくなりました。その結果、**21 個中 6 個のフラグ**が黙って対象範囲外になっていましたが、gate は成功していました。
    - **シークレットスキャンは 6 つの provider のうち 4 つを見逃していました。** クラス `[A-Za-z0-9]` はハイフンを除外します。`sk-proj-…`（現在の OpenAI 形式）と `sk-ant-api03-…` は 2 つ目のハイフンで途切れ、`AIza…` は対象外でした。パターンを拡張し、`.secrets.baseline` はスキャンから除外しました。また、ガード `.env` は `git diff --cached` を照会していましたが、これは index しか見ません。そのため、最悪のケースである、**すでに commit 済み**の `.env` は決して表示されませんでした。現在は `git ls-files` を照会します。
    - **Codex の「トークンのウォームアップ」は、実際にはウォームアップではありませんでした。** 測定の結果、`codex login status` は `~/.codex/auth.json` に触れず、mtime もサイズも変化しませんでした。また、そのヘルプには「ログイン状態を表示」とあります。それにもかかわらず、コメントではトークンを「一度、逐次的に」更新し、1 回限りのローテーション式トークンに対する同時更新のリスクを無効化すると主張していました。説明されていた保護は存在していませんでした。現在、コメントはコードが実際に行うことを記述しており、本当の対策は引き続き `max_jobs=4` です。さらに、このチェックは以前無視していた `CODEX_BIN` を尊重するようになりました。`PATH` に `codex` がない環境では「未認証」で失敗し、誤解を招く診断になっていました。
    - **`.env` はサブシェル内で source されていました。** `detect_provider` はコマンド置換内で呼び出されるため、その export は親側へ反映されませんでした。その結果、`.env` で定義された `GROK_BIN`、`GROK_HOME`、`REGEN_MODEL` は、`main()` 内の読み取りから見えないままで、正しい設定にもかかわらず「Grok バイナリが見つからない」と結論付けられていました。
    - **並行数が公称上限を 50% 超えていました。** ガードが README/CHANGELOG の組を起動した後に配置されていたため、`max_jobs=2` ではピークが **3** になることが測定されました。週次 quota が Chat/Imagine/Voice と共有され、測定できない Grok では、スクリプトが自ら課した上限を守れていませんでした。また、最終カウントは表示されるだけで、28 と比較されたことがありませんでした。そのため、ファイルが欠けていても見逃されていました。
    - **Grok の出力契約：`stopReason` がなければ失敗するようになりました。** 公表された契約では `end_turn` が必須であるにもかかわらず、コードは「`end_turn` **または不在**」を適用していました。フィールドのない payload、あるいは CLI 更新でフィールド名が変更された payload によって、ガードが黙って no-op になっていました。また、`max_turn_requests` は rate limit として分類されなくなりました。これはターン予算の枯渇であり、再試行しても同じ結果を再現し、90 秒の待ち時間がかかるだけだからです。さらに、`quota` は rate limit のマーカーから除外されました。その理由は、`_codex_is_rate_limited` の docstring にすでに記載されていたものの、Grok には適用されていませんでした。
    - **Gemini の cascade はモデルごとに memoize されます。** 既定モデルでは拒否されるにもかかわらず、各 segment で `minimal` から再開していました。そのため、通常経路でも segment ごとに 400 の往復コストが発生し、同じ警告が繰り返し表示されていました。何百回も繰り返される warning は読まれなくなります。そうして、本来の問題を覆い隠すものになります。
    - **その他**：CI での拒否メッセージは Codex 用にハードコードされており、`--use_grok_cli` のユーザーを `XAI_API_KEY` ではなく `OPENAI_API_KEY` へ誘導していました。`provider.capitalize()` は「Grok_cli」と「Openai」を表示していました。サブプロセス基盤のコメントは「shim」を両方の CLI に一般化していましたが、Grok バイナリはネイティブ ELF です。正しい根拠は「自身のサブプロセスを spawn する agent」です。`subprocess` に関する 12 件の SAST finding は、理由を添えて `# nosec` / `# nosemgrep` として記録されています。`shell=True` を使わないリスト形式によりインジェクションは不可能であり、文書内容が argv を経由することもありません。
    - **agent 型サブプロセスにシークレットが一切入らなくなりました。** 名前を列挙した deny-list が保護していたのは、**課金**の不変条件だけでした（`OPENAI_API_KEY` なしの Codex、`XAI_API_KEY` なしの Grok）。測定すると、**ほかの 7 個のシークレット**が依然として各サブプロセスに入っていました。Anthropic、Mistral、Google、Gemini のキー、もう一方の CLI のキー、そしてシークレットではないもののトラフィックの向き先を変更する `OPENAI_BASE_URL` です。しかし、この 2 つの CLI は **agent** であり、Grok は多くの Linux 環境で適用可能な OS sandbox なしに動作します。現在、フィルタリングは名前の列挙ではなく、**名前のパターン**（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`）に基づいています。そのため、このコードが知らなくても、ユーザーが `.env` に追加した変数も対象になります。CLI はこれらを一切必要としません。認証情報は `~/.codex` と `~/.grok` にあり、環境変数には決して置かれません。強化された環境で両方の provider をそれぞれ使い、**実際の翻訳が正常に完了すること**を確認しました。
    - **テスト**：新しいファイル `tests/test_review_hardening.py`（21 テスト）により、provider フラグの排他性、`stopReason` の契約、ニュース用 regex の線形性、CI での拒否メッセージ、Gemini の memoize、サブプロセス環境にシークレットが一切含まれないことを固定しました。最後の assertion は**汎用的**で、どのリストにも名前がないキーでも失敗します。一方、既存の削除テストは自身の定数を映しただけで、自分自身のループ故障以外は検出できませんでした。テストスイート全体は **311 テスト**です。
  - **2つの新しい Grok プロバイダー**：`--use_grok`（xAI API、キー `XAI_API_KEY`、従量課金）と `--use_grok_cli`（公式 Grok Build CLI、Grok サブスクリプションの利用枠から差し引き — `--use_codex` と同じ仕組み）。
    - **API モード、約40行**：xAI のエンドポイントは OpenAI 互換のため、クライアントと `_call_openai` はそのまま再利用され、変更されるのは `base_url` だけ。必要だった適応は1つだけで、すべてに恩恵がある：`finish_reason` は、OpenAI が `stop` を返す箇所で xAI が返す形式 `end_turn` も受け付けるようになった。モデル：`grok-4.6`（高品質）と `grok-4.3`（低コスト）。なお、Grok の低コストモデルもリポジトリ内では最も高価で、100万トークン当たり $1.25/$2.50、対する `mistral-small-latest` は $0.15/$0.60。このプロバイダーを選ぶ理由はモデルの多様性であり、価格ではない。
    - **CLI モード**：Codex を踏襲しつつ、実環境上避けられない4つの相違点がある — プロンプトはファイル経由で渡す（`--prompt-file`。CLI は stdin を読み取らず、argv 内のセグメントは `ps` から見えてしまう）、出力は stdout 上の単一 JSON オブジェクト（JSONL でも `-o` ファイルでもない）、サブスクリプションで利用できるのは `grok-4.6` と `grok-4.5` のみ、そして sandbox は適用できない（後述）。サブプロセスの起動処理は `_codex_run_process` で Codex と共通化し、すでにテスト済みの Codex プロバイダーのその他の部分には手を加えていない。
    - **`exit 0` だけでは何も証明できないことを実測**：未認証の場合でも、CLI は終了コード **0** で **stdout** に `{"type":"error","message":"Not signed in."}` を出力する。拒否やターン数超過も同様に動作する。そのため、出力契約では4つの条件を同時に満たす必要がある：終了コードが 0、エラーペイロードがない、`stopReason == end_turn`、かつテキストが空でないこと。事前確認も同じ論理に従う：未接続でも `grok models` は 0 で終了し、stdout に「not authenticated」が含まれる場合にのみ未認証と判断できる。
    - **隔離：非対称性を意図的に採用し、文書化。** Codex が `--sandbox read-only` で動作する一方、Grok の sandbox は、`sudo` なしでは回避できない独立した2つのシステム上の理由により、最近の多くの Linux 環境では適用できない：Ubuntu 24.04 以降では AppArmor が非特権ユーザー名前空間をブロックし（`bwrap: setting up uid map: Permission denied`、Grok 外でも再現）、さらに `/run/podman` が `0700` の場合、コンテナランタイムソケットの拒否リストが失敗する（resolver が補足するのは `ErrorKind::NotFound` のみで、EACCES は致命的になる）。中心的な落とし穴：適用できない**組み込み**プロファイルを指定すると、**隔離されない状態で黙って起動する**。そのため、スクリプトはデフォルトでプロファイルを一切要求せず、黙ってフォールバックすることもなく、stderr に警告を出す。保護は CLI の `--deny` ルールに依存し、包括的な `*` も含まれる。これは実測で _fail-closed_ となる唯一の層である（未知の接頭辞を持つルールが1つでもあると起動を拒否する）。`GROK_TRANSLATE_SANDBOX=read-only` でこれを必須化でき、その場合、マシンが要件を満たせなければ起動に失敗する。
    - **安全策**：`XAI_API_KEY`、`GROK_API_KEY`、`GROK_SANDBOX` はサブプロセスの環境から削除される（キーがあると従量課金へ切り替わり、継承された `GROK_SANDBOX` は適用不能なプロファイルを誤解を招くメッセージとともに強制してしまう）。MCP/hooks/skills/agents のスイッチは無効化され、`--disable-web-search`、`--no-subagents`、`--no-plan`、使い捨ての作業ディレクトリ、CI での拒否、プロセスグループを終了するタイムアウト、レート制限時のバックオフを適用する。`--max-turns` は 1 ではなく 6 に固定されている：カウンターはツール実行ターンの後に増加するため、1では出力が途中で切れてしまう。
    - **利用枠**：Grok のプールは週単位で、**Chat、Imagine、Voice と共有**されるうえ、その量を表示するコマンドは存在しない。一方、Codex では `account/rateLimits/read` により消費量を算出できる。そのため、`regen_translations.sh` は同時実行数を2に制限し、明示的に警告する。
    - **テスト**：新しいファイル `tests/test_grok_provider.py`（24件のテスト）。全テストスイートは **290件**。
  - **バグ修正 — 複数段落にまたがる英語の引用が一部しか保護されていなかった（`--news` モード）**：`_NEWS_CITATION_REGEX` は引用本文として、**連続する** `>` 行の並びしか受け付けていなかった。引用が複数の段落にまたがると（空の `>` 行で区切られる）、最後の段落だけが取得されてプレースホルダーに置換され、それ以前の段落は LLM に送られて翻訳されていた。これは `--news` が保証するために存在する目的と正反対だった。繰り返し部分は、内部にある空の `>` 行も受け付けるようになり、さらに非貪欲となったことで、最初に見つかった空行ではなく、斜体行の直前にある空の `>` で停止するようになった。
    - **実データで測定した影響範囲**：198記事の実コーパスでは、419件中11件の引用が該当。回帰はない — 新しい正規表現が取得する引用数はまったく同じで、複数段落の本文だけが拡張された（408件の本文は同一、11件は拡張）。また、帰属を示す `> — …` 行は引き続き本文に取り込まれない（lookahead を維持）。
    - **エンドツーエンドでの実証**：69 KB の記事を日本語とアラビア語に翻訳。以前は引用の第1段落が日本語では `> GLM-5.3がオープンウェイト化。` となり、アラビア語でも同様に翻訳されていたが、現在は `> GLM-5.3 is now open-weight.` のまま維持される。英語の引用行数も9行から10行に戻り、原文と一致した。
    - なお、この不具合は後段の検証処理では検出されなかった。検証処理は引用の存在を確認するものの、完全性までは確認していないためである。
  - **デフォルトプロバイダーで実測したコスト削減**：`_openai_extra_kwargs` はモデル名が `gpt-5` で始まる場合、`--eco` でも常に `reasoning_effort="medium"` を送信していた。`gpt-5.4-mini` で10語の文を翻訳して測定した結果：`medium` → reasoning token が45、出力トークンが65、`none` → それぞれ0と14。翻訳に推論は何の価値ももたらさず、しかも全ファイルの全セグメントで課金されていた。デフォルトは `--eco` では `none`、それ以外では引き続き `medium` となる。CLI で明示的に渡された値が引き続き優先される。`--reasoning_effort` は `low`/`medium`/`high` に加えて、`none` と `xhigh` も受け付けるようになった（すべての値がすべてのモデルで受け付けられるわけではない。たとえば `minimal` は `gpt-5.4-mini` に拒否されるが、既存のパラメーターなしでの再試行がこのケースを処理する）。
  - **SDK の更新と Gemini の移行**：`google-generativeai`（サポートは 2025-11-30 に終了し、リポジトリはアーカイブ済み）を統合 SDK **`google-genai`** に置き換えた — `genai.Client(api_key=...)`、続いて `client.models.generate_content(model=, contents=, config=)` を使用し、システムプロンプトはセグメントへ連結する代わりに `system_instruction` で渡す。`mistralai` は **2.9.4** に更新（import は `from mistralai.client import Mistral` となる。旧形式は `ImportError` を発生させることを wheel 内で確認済み）、`anthropic` は **0.125.0**、`openai` は **2.54.0** に更新 — venv 内で2つの HTTP スタックを共存させないため、`httpx2` へ移行する直前の最終バージョンを採用した。これに伴い、`httpx` 0.28.1 と `pydantic` 2.13.5 の固定も解除した。
  - **ドキュメントではなく実際のテストで検出した2つの回帰**：
    - `anthropic` ≥ 1.0 は、`max_tokens` から10分を超えると予測される非ストリーミング呼び出しをクライアント側で拒否する（`ValueError: Streaming is required...`）。この安全策は 0.34.2 にはなく、`max_tokens=32768` を使うすべての Claude 呼び出しを壊していた。明示的な `timeout`（`CLAUDE_TIMEOUT`、デフォルト900秒）で修正した。これにより、完全な応答だけを利用する呼び出しをストリーミングへ切り替えずに済む。
    - `thinking_level="minimal"` を受け付けるのは Gemini カタログの一部だけである：`gemini-3.1-flash-lite` は対応するが、`gemini-3.7-flash` と `gemini-3.1-pro-preview` は 400 で拒否する。そのため `_gemini_generate_with_fallback` を導入し、既存の OpenAI フォールバックを模した `minimal` → `low` → thinking_config なし、という段階的フォールバックを行う。最適化用パラメーターが原因で翻訳を失敗させてはならない。
  - **デフォルトモデルを刷新**し、それぞれ実際の呼び出しで検証：OpenAI は `gpt-5.5` → **`gpt-5.6-terra`**（28件のバッチで −60%）、`gpt-5.4-mini` → **`gpt-5.6-luna`**（−73%）。Claude は `claude-sonnet-4-6` → **`claude-sonnet-5`**（より安価で新しい）、`claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（日付なしの正規 ID）。Gemini は `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**、`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（安定版であり、`3.5-flash-lite` より安価）。Mistral は変更せず、`mistral-large-latest` が4つの中で最良の費用対効果を維持している。なお、`gemini-3.1-pro-preview` より新しい Pro 系の Gemini モデルは存在しない。2026年5月に発表された Gemini 3.5 Pro は結局リリースされず、3.5/3.6/3.7 系列はすべて Flash のみである。
  - **Gemini の切り替え前に実測した A/B 比較**：`README.md` を `gemini-3.1-pro-preview`、次に `gemini-3.7-flash` で日本語へ翻訳。構造は完全に同一（リスト21件、コードブロック18件、HTML リンク13件、画像13件、すべての URL を維持）で、所要時間は **48秒に対して8秒**。この2モデルについて翻訳や非ラテン文字のスクリプトを比較した公開ベンチマークが存在しないため、この測定がなければ切り替えは単なる推測に基づくものとなっていた。
  - **Claude の応答ブロックをフィルタリング**：`_call_claude` は型をフィルタリングせずに `block.text for block in response.content` を実行していた。適応的推論モデル（Sonnet 5 以降）は `thinking` ブロックを途中に挿入する。このブロックが公開するのは `.thinking` であり、`.text` ではないため、翻訳は最初のセグメントで不透明な `AttributeError` により失敗していた。`thinking`、`redacted_thinking`、`tool_use`、`tool_result` の各ブロックを除外するようになった（テキストを保持する未知の型に対する寛容性を保つため、除外リストを採用）。テキストブロックが1つもない応答では明示的なエラーを発生させる。各呼び出しには `thinking={"type": "disabled"}` を渡す。
  - **`MODEL_TOKEN_LIMITS` を再同期**：廃止日を過ぎたモデルを削除（`magistral-*` 系列は 2026-07-31、`gemini-2.0-*` は 2026-06-01、`gemini-3-pro-preview` は 2026-03-09 に廃止、ならびに `claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。上限値を修正：Mistral 128K → **256K**（Large 3 / Small 4 世代）、Gemini 1 000 000 → **1 048 576**（実際の入力上限）、`claude-opus-4-5` 200K → **1M**、`gpt-5.6-*` 系列 400K → **1.05M**。Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest`、`ministral-*` 系列を追加。なお、これらの上限値は引き続き目安であり、`translate()` がセグメント分割を `min(16000, limite)` に制限している。
  - **Provider `--use_codex`**：従量課金の API を呼び出す代わりに、公式 Codex CLI（`codex exec`）を非対話モードで操作する5番目の provider。翻訳分は、すでに支払い済みの ChatGPT サブスクリプション枠から差し引かれる。この用途について OpenAI が文書化している唯一の方法であり、プラン別の利用可否表では「Codex SDK、`codex exec`、およびスクリプト化可能なワークフロー」が Plus/Pro/Business/Enterprise で利用可能と記載されている。一方、`~/.codex/auth.json` の token は API Platform への呼び出しを認証しない（また、このスクリプトから読み取られることもなく、認証とその refresh は引き続き CLI が管理する）。
  - **Codex バイナリを npm だけでなく pip でもインストール可能に**：`_resolve_codex_binary()` は、`CODEX_BIN`、次に `PATH`、その後 OpenAI が公開する公式 Python package **`openai-codex-cli-bin`**（SDK `openai-codex` の依存関係）の順にバイナリを検索する。したがって、Python プロジェクトで `--use_codex` を使用するために、npm のグローバルインストールは不要になった。この package は `requirements.txt` には追加されていない。バイナリのサイズが約250 MBあり、任意選択の provider のために全ユーザーへ負担させることになるためである。エンドツーエンドで検証済み：`codex` が `PATH` に存在しない状態でも、解決処理が package 内のバイナリを検出し、完全な翻訳が6秒で完了する。
  - **「サブスクリプションモード」の保証**：`OPENAI_API_KEY` と `CODEX_API_KEY` はサブプロセスの環境から削除される。この保護がないと、`.env` に存在するキーによって、目に見える通知が一切ないまま Codex が従量課金へ切り替わる可能性がある。これはまさに、この provider が回避するために存在する事態である。
  - **テストで封じ込めた CLI の落とし穴**：
    - `codex exec` は、prompt が引数として渡された場合でも stdin を**読み取る**。stdin を閉じなければ、コマンドはモデルを一度も呼び出さずに timeout まで待機する（再現結果：180秒後に exit 124、0 byte）。したがって、`communicate(input=...)` は必須である。
    - npm でインストールされた `codex` は、実際の Rust バイナリを `spawn` する Node shim である。このバイナリは Python process の**孫 process**であり、`subprocess.run(timeout=)` の `SIGKILL` 後も生き残り、そのまま quota を消費し続ける可能性がある。そのため、`Popen(start_new_session=True)` + `os.killpg` を使用する。
    - CLI は `turn.failed` を出力していても、終了コード0で終了する場合がある。return code に加えて JSONL 出力（`--json`）も検査し、終了コードが0でも `-o` ファイルが存在しない場合は、空の segment を生成せず明示的なエラーを送出する。
  - **rate limit 時の back-off**：CLI には内部 retry が実装されていない（`max_retries = 0`）。分類は部分文字列ではなく、JSON payload の構造（`status: 429` / `error.type`）に基づいて行う。「quota」という語は、回復可能な429にも、恒久的な `insufficient_quota` にも現れるためである。
  - **CI 保護**：`CI` または `GITHUB_ACTIONS` が定義されている場合、`--use_codex` は拒否される。サブスクリプションによる認証は共有 runner 向けではなく、OpenAI も公開 repository でこの workflow を使用しないよう明示的に推奨している。
  - **モデル**：`gpt-5.6-sol`（品質）と `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` family は CLI と API Platform に共通するが、ChatGPT account ですべてを利用できるわけではない。allowlist はローカルでの検証なしに server 側で適用され、通常と異なるモデルを指定すると警告が表示される。Plus plan では、5時間の window あたり Sol が10～100 messages であるのに対し、Luna は250～2,000 messages を利用できるため、あらゆる batch 処理には `--eco` が推奨モードである。
  - **修正済みの bug — 完全に成功していても `regen_translations.sh` がエラー終了していた**：`trap ... EXIT` は、`main()` の `local` 変数である `failed_log` を参照していたが、この変数は trap の実行時点ではすでに存在しない。`set -u` では `failed_log: unbound variable` が発生し、28件の翻訳がすべて正しくても script が終了コード1で終了していた。これにより、再生成直後の最もコストが高い段階で `release.sh --auto`（`set -e`）が中断される可能性があった。変数を global に変更し、trap でその存在を確認するようにした。有用な副作用として、これまでこのエラーに隠されていた実際の翻訳失敗が、終了時の summary に再び表示されるようになった。
  - **`REGEN_MODEL`**：`regen_translations.sh` の新しい環境変数。provider のデフォルトより優先して特定のモデルを強制する。たとえば、volume 重視の `--eco` モデルではなく、サブスクリプション quota の上位モデルで再生成する場合は `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol` を指定する。
  - **`regen_translations.sh`**：明示的な opt-in で `REGEN_PROVIDER=codex` を利用可能（ユーザーが知らないうちにサブスクリプション quota を消費しないよう、自動検出は行わない）。並列処理を開始する前に token を逐次的に一度 refresh する。Codex の refresh は rotation 方式かつ一度しか使用できないため、job を並行実行すると `codex login` session が無効になるためである。また、並行数は4に抑えられる。
  - **関連する refactor**：`_dispatch_provider_call` は、chain 全体に4番目の boolean を伝播する代わりに、provider 名を返す `_resolve_provider()` を使用することで、parameter 数を8個から6個に削減した。最小限の `Namespace` で `translate(..., use_mistral=True)` を呼び出す test を維持するため、明示的な boolean は引き続き `args` より優先される。
  - **テスト**：新しいファイル `tests/test_codex_provider.py`（48 tests）で、argv、不要な値を除去した環境、前置き禁止 contract、silent failure、timeout/killpg、back-off、preflight、provider 解決、Gemini の reasoning cascade、Claude block の filtering、複数 paragraph にまたがる news citation を網羅。test suite 全体は290 tests。
  - **実環境での検証**：プロジェクトの `README.md` を Codex で**14言語**に翻訳した結果、参照翻訳と完全に同一の構造になった（code block 14個、見出し24個、table 25行、HTML link 13個、画像13個、URL 19個、code block は文字単位で完全一致、placeholder の残留は0件）。69 KBの news article を `--news` モードで処理したところ、`gpt-5.6-luna` と `gpt-5.6-sol` の出力はいずれも、en/ja/ar について後段の application validator を通過した。`account/rateLimits/read` で測定した消費量は、`--eco` モードで計数器の丸め閾値未満（5時間 window の0%）に収まった。

- **1.9.2** 入れ子の括弧またはフランス語の prefix を含む news attribution URL の抽出を修正（2026-05-11）：

  - **修正済みの bug**：`_protect_news_quotes` での attribution URL 抽出には、regex `re.search(r"\((.+?)\)", attribution)`（括弧間の lazy capture）が使用されていた。`(relayé par [@user sur X](https://x.com/.../123))` のような attribution（入れ子の括弧：外側の `(` + Markdown link の `]()`）では、最初に現れた `)` で capture が終了し、フランス語の prefix を含む切り詰められた文字列 `relayé par [@user sur X](https://x.com/.../123`（末尾の `)` なし）になっていた。その結果、`_validate_news_post` は翻訳済み出力からこの文字列を検索して必ず失敗していた（理由は2つあり、`)` が切り詰められていることと、「relayé par」が `relayed by`/`weitergeleitet von`/…に翻訳されること）。low → medium → high → gpt-5.5 の cascade 全体でも通過できなかった。
  - **修正**：regex を `re.search(r"\]\(([^)]+)\)", attribution)` に変更。Markdown link の `](url)` を明示的に対象とし、フランス語の prefix や切り詰めを含まない**純粋な URL のみ**を capture する。この不変性は翻訳中、placeholder `#URL{N}#` によって維持される。問題となる次の2つの pattern に対応：
    - `(relayé par [@account sur X](url))` — 入れ子の括弧
    - `via [@source](url)` または `selon [@author](url)` — 外側の括弧がないフランス語の prefix
  - **テスト**：`test_silent_failure.py` の class `TestNewsCitationExtraction` に2件追加：
    - `test_extract_attribution_url_with_nested_parens`（Genspark CEO E2B の bug を正確に再現したケース）
    - `test_extract_attribution_url_with_french_prefix`（`via` を使用した variant）
  - **網羅性の不足**：`check-editorial-coverage.py` は編集上の構文を検証するが、translator で翻訳可能かどうかは検証しない。将来的な改善案（v1.9.2 の scope 外）として、dry-run で attribution 抽出をシミュレートし、公開**前**にリスクのある pattern を検出する check が考えられる。

- **1.9.1** 翻訳 marker の note にある CTA label の i18n を修正（2026-05-10）：

  - **修正済みの bug**：翻訳済みファイル上部の marker banner にある CTA link の label `[Voir le projet sur GitHub ↗]` が、`target_lang` に従わず、すべての target language で**フランス語のまま**になっていた。LLM がこの label を認識することはない（URL と repository の slug を保持するため Python 側で組み立てられる）ため、翻訳 phase では修正できなかった。v1.9 で `marker` format を追加して以来の silent regression。
  - **修正**：15言語を各 locale の label に mapping する新しい constant `_VIEW_PROJECT_LABELS` を追加。`_translation_note_invariants(target_lang)` と `_assemble_translation_note_paragraphs(phrase, target_lang)` が target language を伝播するようになった。言語が不明な場合は `fr` に fallback（安全策であり、KeyError は発生しない）。
  - **テスト**：`test_source_emits_three_paragraphs_repo_title_description_link` を調整（target_lang `ja` → 期待される日本語 label）。新たに2 tests を追加：`test_source_link_label_localized_per_target_lang`（Latin script、表意文字、abjad を網羅する7言語で parameterize）と `test_source_link_label_falls_back_to_french_for_unknown_target`。合計：`test_translation_note_position.py` は38件から40 tests に増加。
  - **後方互換性**：default `target_lang="fr"` を持つ signature。`args.target_lang` を渡さない外部の programmatic caller も、変更なしで引き続き動作する。
- **1.9** サイレント障害の修正 + 包括的な品質ツール群 + 複数位置対応の翻訳注記（2026-05-07）：
  - **複数位置対応の翻訳注記 + 「embed card」マーカー形式**：
    - 新しいCLIオプション（追加のみ、デフォルトは変更なし → **破壊的変更なし**）：
      - `--note_position {top,bottom,both}`（デフォルト：`bottom`）：翻訳済みファイルの先頭、末尾、またはその両方に注記を配置します。
      - `--note_format {legacy,marker}`（デフォルト：`legacy`）：
        - `legacy` はv1.8の動作（太字段落 `**…**`）を**バイト単位で完全に**再現します。
        - `marker` は、非表示のMarkdownリンク参照定義（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）に続いて、「GitHubリポジトリのembed card」形式でレンダリングできるよう構造化された**3段落のblockquote**を出力します。内容は、インラインコード形式のプロジェクト名（`**\`ai-powered-markdown-translator\`\*\*`）、LLMによって翻訳された説明、および矢印が表示されるCTAリンク（`[Voir le projet sur GitHub ↗](URL)`）です。ビルド時にremarkプラグインで利用できます（jls42.orgブログ → `remark-translation-banner`プラグインを参照）。
    - **LLMには決して送信されない不変要素**：リポジトリ名とGitHub URLは、説明文の翻訳後にPython側で組み立てられます。LLMがslug `ai-powered-markdown-translator` や `https://github.com/jls42/...` を目にすることはないため、レンダラー、文字の大小、schemeが変更されないことを保証します。
    - **frontmatter対応の挿入**：`top` または `both` モードでは、注記はYAML frontmatterを閉じる `---` ブロックの**後**に挿入されます（Astro Content Collections／gray-matterの安全性を確保）。ヘルパー `_split_frontmatter` はファイル先頭の `---\n…\n---\n` を検出して完全性を維持します。終了fenceのない開いたfrontmatterでは **`RuntimeError` を送出**し、誤った位置に注記を付けてファイルを書き込む代わりに、そのファイルを `failed_files` に記録します。
    - **ホワイトリスト方式のモデル名sanitizer**：`_sanitize_model` は `[A-Za-z0-9._:/-]` に含まれないすべての文字を `_` に置換し、空になった場合は `unknown` を使用します。Astroのremarkプラグイン側のvalidatorと整合させ、マーカー形式を壊す文字（空白、引用符、括弧、カンマなど）を無害化します。
    - **内部refactor**：`_append_translation_note`（1個のモノリシック関数）→ 7個の純粋ヘルパー（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。builderとcomposerを分離しました（builderは区切りなしの純粋なブロックを返し、composerは位置に応じて `\n\n` を適用）。本番処理とソース用ヘルパーは、同じ3段落assemblerを共有します。
    - **空行を保持する `_quote_lines`**：各行に `> ` を付加し、空行は `>` のみに変換します。これによりmdastは、blockquoteを改行付きの単一段落ではなく、3つの独立した段落（タイトル／説明／リンク）として認識できます。
    - **適応型 `_build_translation_note_block`**：LLMが保持した段落数に応じて処理します（3＝完全なcard形式、2＝文章 + リンク、1＝fallback）。1段落のfallbackでは、Markdownリンク `](` が検出された場合、**`**...**` で囲まなくなりました**（リンクの周囲に `<strong>` を配置するとレンダリングが不安定になるため）。
    - **後方互換性**：`_compose_with_notes` 側では `getattr(args, "note_position", "bottom")` と `getattr(args, "note_format", "legacy")` を使用します。これらの属性を持たないNamespace（既存のテストや外部からのプログラム呼び出し）も変更なしで引き続き動作します。
  - **長文翻訳におけるサイレント障害の修正**：
    - すべてのprovider（OpenAI、Mistral、Claude、Gemini）で翻訳後の言語を検証：決定論的レイヤー（ソースの抜粋がそのまま残っていないかを検出）+ 確率論的レイヤー（`langdetect`）
    - `finish_reason`／`stop_reason`のホワイトリスト：ホワイトリスト外のあらゆる状態（truncation、content_filterなど）で `RuntimeError` を送出
    - `max_tokens` Claude：`4096` → `32768`（16kのsegmentで潜在的なtruncationを回避し、FR→JA/ZH/KO/AR/HIのcross-script変換に余裕を確保）
    - heading対応のsegmentation：segment後半のH2/H3を優先（各segmentが意味的に完全なsectionから始まるように調整）
    - 非ゼロのexit codeまでエラーを伝播：`translate_markdown_file` は型付きstatus `success`／`failure`／`skipped` を返し、単一ファイル処理とbatch処理のいずれでも、1ファイル以上が失敗した場合は `main()` が `sys.exit(1)` を返します
    - すべてのproviderに対する空content guard、ソース／出力のsanity ratio（500文字以上で5%未満なら拒否）、コードplaceholderの検証（`#CODEBLOCK`／`#INLINECODE`）、LLM処理後の正規化（区切りやリンクがheadingに連結する問題）、`reasoning_effort` を使用しない `BadRequestError` retry
    - 依存関係 `langdetect==1.0.9` を追加
  - **pre-commit品質ツール群**（「完全なEurekAI方式」、14個のhook）：
    - Pre-commit：ruff（lint＋format）、shellcheck、prettier（md/yaml/json）、detect-secrets（4個のAPI keyを保護）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（whitespace、EOF、large-files、shebangなど）
    - Pre-push：mypy（段階的なlaxモード）、Opengrep SAST（translate.py + scripts/）、pip-audit（初期reportingモード）、unittest discover（tests/ + scripts/tests/）
    - `./venv/bin/python` を使用するローカルwrapperを `scripts/` に配置
    - `scripts/audit_verdict.py`：11個のunittestを備えたpip-audit用JSON parserで、jls42-astroのparserをPythonへ移植
    - 初期のruff違反7件を修正：B904（raise from）×2、B007（未使用のdirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizardでは `translate.py` を一時的に除外（CCN 21～47の関数が4個あり、refactorを計画済み）。scripts/には厳格なgateを適用
  - **SonarCloud + 包括的なcoverage**：
    - GitHub Actions workflow `SonarCloud`（sonarcloud.yml + sonar-project.properties）：pushおよびpull-requestのたびに分析し、`coverage.xml` でcoverageを取得
    - README上部に11個のSonarCloud badge（Quality Gate、Security／Reliability／Maintainability rating、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）
    - `tests/test_silent_failure.py`（`unittest` stdlib）：サイレント障害のerror chainを構成する6つのlinkを網羅
    - `tests/test_orchestration.py`（+79テスト）：`translate.py` のorchestration layerを網羅（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` TypeError + BadRequestErrorのfallback、o1-seriesのprompt形式、`_validate_translation_output` のearly-return branch）
    - `scripts/tests/test_audit_verdict.py`：`main()`（stdin/stdout）と `if __name__ == "__main__"` ブロックをsubprocess経由でcoverage対象化
    - **新規コードのcoverage**：75.5% → 約98%（translate.py 98%、scripts/audit_verdict.py 97%）
  - **テスト**：`tests/test_translation_note_position.py` は位置 × 形式のmatrix（E2E `marker+top|bottom|both` および `legacy+top|bottom|both` を含む）、複数行へのprefix付加、バイト単位の後方互換性（golden literal）、sanitizer、frontmatterのsplit（閉じられていないfenceでのraiseを含む）、3段落形式、2段落fallback、1段落 + Markdownリンクのguard、およびタイトルとURLがLLMへ一切送信されないことをassertする重要なguard `TestLLMPayloadExcludesInvariants` を網羅します。**190件のテストが成功**し、regressionは0件です。
  - ドキュメント：`README.md`（フランス語 + 14翻訳）にbadgeを追加、`CLAUDE.md`（pre-commit workflow + 詳細なCI監視）、28翻訳を再生成
- **1.8** `--news` モード + 2026年モデルへの更新（2026-03-17、tag `v1.8`）：
  - デフォルトモデルを更新（2026年3月）：
    - OpenAI高品質：`gpt-5` → `gpt-5.4`
    - OpenAI低コスト：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini高品質：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）、`gemini-3.1-pro-preview`（1M）のtoken上限を追加
  - 初期 `--news` モード：placeholder `#NEWSQUOTE\d+#` による英語引用の保護、`LANG_FLAGS` mapping（15言語）、対象言語別のflag管理
  - 復元前にnews placeholderを検証（regression：LLMがplaceholderを削除すると、引用のない出力がサイレントに生成されていた問題）
  - `regen_translations.sh` scriptをportable化（絶対pathを使用し、pwdへの依存を排除）
  - README／CHANGELOGのlanguage barにフランス語へのリンクを追加し、28翻訳を再生成
- **1.7** 新機能：
  - 翻訳時に元のファイル名を維持する `--keep_filename` オプション
  - API keyを自動的に読み込む `.env` ファイルのsupport
  - **inline codeの保持**：翻訳中にbacktick（`` `...` ``）も保護されるようになりました
  - system promptの改善：
    - YAML frontmatter内の引用符処理を改善
    - template variable `{variable}` を保護
    - 要求されていない翻訳者注記を禁止
  - 364ファイルでテストに成功（jls42.orgブログのmigration）
- **1.6** 新機能：
  - 翻訳用Google Gemini APIのsupport（`--use_gemini`）
  - 2026年版デフォルトモデルへの更新：
    - OpenAI：`gpt-5`（高品質）、`gpt-5-mini`（低コスト）
    - Claude：`claude-sonnet-4-5`（高品質）、`claude-haiku-4-5`（低コスト）
    - Gemini：`gemini-3-pro-preview`（高品質）、`gemini-3-flash-preview`（低コスト）
  - より高速で低コストなモデルを使用する低コストモード（`--eco`）
  - ディレクトリを走査せずに単一ファイルを翻訳（`--file`）
  - 新しい簡略化された命名pattern：`{base}-{lang}.md`
  - モデル名を含む従来形式を維持する `--include_model` オプション
  - 一覧にないモデルをデフォルトのtoken上限（128k）でsupport
  - READMEを14言語に翻訳
- **1.5** 改善：
  - **API keyとデフォルトモデルの更新：**
    - **OpenAI：** `DEFAULT_MODEL_OPENAI` から `"gpt-4o"` へ更新。
    - **Mistral AI：** `DEFAULT_MODEL_MISTRAL` から `"mistral-large-latest"` へ更新。
    - **Anthropic Claude：** `DEFAULT_ANTHROPIC_API_KEY` を追加し、`DEFAULT_MODEL_CLAUDE` から `"claude-3-5-sonnet-20240620"` へ更新。
  - **翻訳promptの最適化：**
    - 直接翻訳および翻訳注記用のpromptを拡充して、より明確かつ効率的にしました。metadataや特定のformatting要素を保持するための詳細な指示も含まれています。
  - **コードのrefactor：**
    - Mistral AI clientの初期化で `MistralClient` を `Mistral` classに置き換えました。
    - 可読性と保守性を向上させるため、importを再編成しました。
    - 翻訳時に元のformattingを保持できるよう、テキストのsegmentationとcode blockの処理を改善しました。
  - **出力ファイルの管理：**
    - 出力ファイル名内のモデルと言語の順序を入れ替え（例：`f"{base}-{args.target_lang}-{args.model}.md"`）、翻訳の整理と検索を容易にしました。
  - **その他の改善：**
    - 不要な空行を削除してコードを整理しました。
    - scriptの構造と可読性を向上させるため、軽微な調整を行いました。
- **1.4** 新機能：
  - 翻訳用Anthropic Claude APIのsupport
  - 明確さと効率を高めるためのprompt最適化
  - コードの保守性を向上させるための軽微な調整
- **1.3** 改善と新機能：
  - code block処理を改善
  - 出力ファイル管理を改善
  - 既存ファイルの検出を改善
  - 翻訳を強制する `--force` オプション
  - 出力ファイル名内のモデルと言語の順序を入れ替え
- **1.2** changelogを修正
- **1.1** Mistral AI APIのsupportを追加
- **1.0** 初期version - OpenAI APIをsupport

**gpt-5.6-solでフランス語から日本語に翻訳された記事。**
