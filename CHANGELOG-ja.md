### 変更履歴

🌍 [フランス語](CHANGELOG.md) | [英語](CHANGELOG-en.md) | [スペイン語](CHANGELOG-es.md) | [中国語](CHANGELOG-zh.md) | [ドイツ語](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [韓国語](CHANGELOG-ko.md) | [アラビア語](CHANGELOG-ar.md) | [ヒンディー語](CHANGELOG-hi.md) | [イタリア語](CHANGELOG-it.md) | [オランダ語](CHANGELOG-nl.md) | [ポーランド語](CHANGELOG-pl.md) | [ポルトガル語](CHANGELOG-pt.md) | [ルーマニア語](CHANGELOG-ro.md) | [スウェーデン語](CHANGELOG-sv.md)

- **1.13.0** Provider `--use_openrouter`：中国のオープンモデルを含む約430モデルへの有料ルーター（2026-09-05）：

  - **8番目と同時に提供される9番目のProvider経路。** 1.12.0はPyPIでは公開されておらず、OpenCodeとOpenRouterの2つのルーターが同時にリリースされます。[OpenRouter](https://openrouter.ai)では、ほかのどのProviderもここでは提供していないKimi、Qwen、DeepSeek、Z.aiなどのモデルへ、従量課金される単一のクレジットと1つのキーでアクセスできます。endpointはOpenAI互換なので、clientはxAIと同じです。**このProviderを区別する要素はすべてpreflightに集約されており、その各ルールはAPIでの測定結果に基づいています。**

  - **同じモデルが上限の異なる数十のホストから提供されますが、routingはその違いを認識しません。** 測定結果：`z-ai/glm-5.2`では33ホスト、`z-ai/glm-5.3-flash`では23ホストで、そのうち1つは**出力2,048 tokens**が上限でした。このため、23のうちいずれかへ送られた長文翻訳は、何の通知もなく無作為に切り詰められていました。preflightは`/api/v1/models/{modèle}/endpoints`を読み取り、出力上限が8,000 tokens未満のホスト、状態が劣化しているホスト、上限を宣言していないホストを除外し、残りを固定します。`allow_fallbacks: false`を**伴わない**`provider.only`は単なる優先指定にすぎません。ルーターは除外されたホストへ戻るため、固定は無意味になります。上限を満たすホストがなければ、コマンドは停止します。それでも翻訳を続行することは、このpreflightが防止するために存在する無通知の切り詰めを受け入れることになるためです。

  - **推論は出力と同じ料金で課金され、多くのモデルでデフォルトで有効です。** `z-ai/glm-5.2`に同じリクエストを送り、「OK」と応答させた結果、**モデルのデフォルトではcompletionが107 tokens、推論を無効にすると2 tokens**でした。推論が何の価値も加えない翻訳では、各ファイルの各segmentで18倍の差になります。そのため、デフォルトでは無効にしています。推論を必須とする**431モデル中288モデル**（`reasoning.mandatory`）は`400 « Reasoning is mandatory for this endpoint and cannot be disabled »`と応答します。これらには、推測したeffortを送る代わりに何も送信しません。effortは**`max_tokens`の一定割合**を割り当て、推論がそれを先に消費するため、無作為に選んだ値では空白ページのリスクを減らせず、別の位置へ移すだけだからです。

  - **推論を必須とするモデルには、そのモデルが受け入れる最低のeffortを送信します。これは測定によって決定されました。** 当初は、モデルに代わって推測しないよう、何も送らない方針でした。catalogueのデフォルトが`max`である`z-ai/glm-5.3-flash`で検証したところ、この方針では翻訳の完了前に出力が**32,768 tokensで切り詰められ**、14言語中2言語が失われました。枠を増やしても結果は変わりません。effortがその一定割合を割り当てるため、推論も枠とともに増えるからです。そのためProviderはpreflightで`supported_efforts`を読み取り、最低値を要求します。catalogueに利用可能な値が示されていない場合は「何も送らない」方式へフォールバックします。問題が起きた言語で反証テストを行ったところ、以前はbudget枯渇で失敗していましたが、現在はソースと同一の構造を保ち、9分で成功します。

  - **上流ホストの障害で、原因となったホスト名が示されるようになりました。** ルーターはこのケースを、`native_finish_reason`がnullの`finish_reason=error`として正規化します。2言語で2回測定し、どちらも正確に750秒でした。従来の一般的なメッセージでは、文書や分割方法の不具合を探すことになっていましたが、現在は障害が供給元側にあり、多くの場合は再試行で解決すると伝えます。

  - **出力が空の`finish_reason=length`は切り詰めではありません。** これは最初の有用な文字を生成する前に、推論がbudgetを使い切った状態です。測定では、有用な148 tokensに対して推論が15,850 tokensでした。2つのケースでは必要な対処が正反対であり、前者ではsegmentのサイズを小さくしても効果がありません。メッセージで両者を明確に区別するようになりました。測定結果に基づく保護機能がほかにも2つあります。上流ホストが失敗すると、ルーターは**エラーだけを含むbodyとともに200を返す**ことがあり（`choices[0]`はメッセージを隠す不透明な`TypeError`を送出していました）、context windowはcatalogueから読み取って`MODEL_TOKEN_LIMITS`へ設定されます。`DEFAULT_TOKEN_LIMIT`はcatalogue内の44モデルで誤っており、そのうち2モデルの上限は4,095 tokensです。

  - **`--model fournisseur/modèle`は必須であり、その形式はnetworkへ接続する前に検証されます。** OpenRouterは供給元ではありません。この選択は価格、ライセンス、データ処理に関わるため、ユーザーに代わって行うものではありません。slugはpreflightのURLに挿入されるため、検証は単なる使いやすさへの配慮ではなく、pathの注入を防ぐための保護です。2つのルーターで共通するnamespace付きregexは`a/b/..`を受け入れるため、親segmentは明示的に拒否されます。`--eco`は効果がないことも明記します。

  - **3つの記述を修正し、そのうち1つは誤りでした。** `codex exec`に関するOpenAIの警告は、公開repositoryであることではなく、共有runnerへ個人用sessionファイルを注入することを対象としていました。README、CLAUDE.md、codeでは意味を取り違えて引用されていました。OpenCodeの認証情報の保存場所は1.18.27で変更され、`opencode.db`の`credential` tableになりました。従来の`auth.json`ではありません。「ここでは決して読み取られない」という不変条件は正しいままでしたが、保存場所の記載が古くなっていました。最後に、OpenCodeのsectionでは、検証されていない経路を同等のものとして提示しなくなりました。Zen gatewayとOllamaはend-to-endで測定済みですが、GitHub Copilot、LM Studio、llama.cppは未測定であり、READMEにもそのように明記されています。

  - **測定キャンペーンと、README内の推奨モデル一覧表。** 3種類の文書セットを14言語へ翻訳し、300件を超える翻訳を実行しました。`--news` modeの情報密度が高いブログ記事、標準MarkdownのこのREADME、GitHubからそのまま取得した著名プロジェクトのREADME 4件です。表では、これまで混同されていた2点を区別しています。翻訳が**完了する**ことと、翻訳後の**構造がソースと同一である**ことです。情報密度が高い2文書のいずれでも情報を一切失わなかったモデルは3つです。`gemini-3.7-flash`、ChatGPT subscription経由の`gpt-5.6-sol`、OpenRouter経由の`z-ai/glm-5.2`で、唯一の相違は1～2言語で`**`の対が保持されなかったことです。中心的な知見は、**識別要因が`--news` modeではなく、文書の情報密度である**ことです。subscription経由のGrokはブログ記事で14回中13回失敗する一方、公開READMEでは16回中14回成功しました。原因は長いsegmentでの脱落であり、反証テストでも確認されています。表には固有の注意事項も記載されています。網羅的ではなく、特定時点の結果であり、所要時間は順位を示すものではありません。最善の方法は、引き続き自身の文書で測定することです。

  - **構造比較機能は、非ラテン文字で2件の偽陽性を生んでいたため、数値を公開する前に修正されました。** 全角の閉じ括弧が続くURL `）`は、`)`で停止するregexでは正しく区切られず、URL自体は同一なのに抽出された文字列が異なっていました。また、フランス語では5行になる引用が中国語では3行に収まることで、行単位のカウントが減少していました。2つの修正はいずれも反証テストで検証され、URL、section、inline codeのいずれかを削除した場合は引き続き検出されます。修正しなければ、GeminiとCodexの結果は14言語中それぞれ13言語と12言語ではなく、どちらも11言語として公開されるところでした。

  - **テスト**：新しいファイル`tests/test_openrouter_provider.py`（39 tests）— モデルの検証と親segmentの拒否、ホストの固定（上限、状態、上限未宣言、共通の最低値）、常にfalseの`allow_fallbacks`、`mandatory`に応じた推論の無効化または維持、完全な出力contract（200内のエラー、選択肢なし、切り詰めと区別される空白ページ、異常な`finish_reason`、nullの内容）、到達不能なcatalogue、欠落したslug、正常なホストの不在に対するpreflightのfail-closed、flagの排他性、ファイル名labelを対象とします。全suiteは**427 tests**です。

  - **Refactor：4,253行の単一moduleを、動作を1行も変更せず複数のmoduleへ分割。** `src/aipmt/translate.py`は`config`、`markdown`、`segmentation`、`guards`、`placeholders`、`news`、`prompts`、`notes`、`naming`、`pipeline`、`cli`、およびsubpackage `providers/`へ分割されます（Providerごとに1 module、基盤となる`base`、解決とdispatchを担う`registry`）。各移動は、機械的な証明を伴うcommitです。検証ツールはpackage内のすべてのトップレベルnodeのASTを基準snapshotと比較し、各symbolの配置、安全性markerがverbatimで保持されていること、未追跡ファイルがないことを検証します。この一時的なツールは次のversionで削除されました。目に見える変更点は次のとおりです。`aipmt.translate`は、従来のmoduleが`_` prefixなしで公開していた64個の名前を、object identityを保ったまま再公開するfaçadeになります（`__all__`に含まれる9個がサポート対象APIで、それ以外は互換性aliasです）。また、`import *`が拾っていたdependencyおよび標準libraryの29個の名前は再exportしなくなります。ファイルの直接実行（`python src/aipmt/translate.py`）は廃止され、`aipmt`と`python -m aipmt`が引き続きサポートされる2つの形式です。public関数の`__module__`は定義元moduleのものになります。SDKは`.env`の読み込み後にimportされ、以前のように先にはimportされませんが、既知の影響はありません。427 testsはidentifierまでそのまま維持され、実際に検証するmoduleへ移行されました。façade経由だった91個のpatchは、該当する名前を参照するmoduleを直接対象とするようになりました（そのうち9個はpatchがなくてもgreenのままだったことを測定済みです）。7件のcontract testがfaçadeを固定し、gate用ツールは最初の移動より前に書き直され、検証を停止したことでgreenになることがないようにしました。具体的には、下限付きのdirectory単位のLizard scope、構築済みparserから読み取るflags、package単位のcoverage下限、追跡対象moduleを列挙する`release.sh`です。

- **1.12.0** Provider `--use_opencode`：open source agentのOpenCodeを、ユーザーが選択した供給元へ接続 — local model、アカウント不要の無料モデル、subscription、またはキー（2026-09-04）：

  - **最初の7つとは性質が異なる、8番目のProvider経路。** [OpenCode](https://opencode.ai)（MIT）はモデルの供給元ではなく、ユーザーがOpenCode自体に設定した供給元へ接続する_ルーター_です。APIキー、subscription（GitHub Copilot、ChatGPT、SuperGrok）、**アカウント不要**の無料モデルを提供するOpenCode Zen gateway、または**local** model（Ollama、LM Studio、llama.cpp）を利用できます。scriptはCodexやGrokと同じく、`opencode run`を非対話modeで操作し、同一のsubprocess基盤（独立したprocess group、timeout時の`SIGTERM`とそれに続く`SIGKILL`、常に閉じたstdin、機密情報を除去したenvironment）を再利用します。**2件の実際の翻訳**で検証済みです。`opencode/mimo-v2.5-free`経由でこのREADME全体を英語へ翻訳した結果は49秒、1 passで、ソースファイルと同一の構造でした（32 headings、26 code closings、18 links、37 URL、37 table rows、135 inline codes）。また、`ollama/qwen2.5:7b`経由でテストファイルをlocalに、キーを一切使わず翻訳しました。

  - **`--model provider/modèle`は必須であり、明示的に選択するものです。** `--model`がない場合、OpenCodeは自身のデフォルトへフォールバックします。新規installationでは`opencode/big-pickle`であり、やり取りがtrainingに利用される可能性がある無料の「stealth」モデルです。実測でも、このモデルが応答しました。ユーザーに代わってこれを暗黙に選択することは、このrepositoryが追跡する見えない切り替えそのものです。そのためerror messageには、モデル一覧を表示するcommand（`opencode models`）と、local、無料、subscriptionの3つの例が示されます。`--eco`は効果がないことも明記します。`--reasoning_effort`は明示的に要求された場合のみ、OpenCodeの`--variant`としてそのまま渡されます。

  - **推測ではなく、測定済みのconfinement。** inline configuration（`OPENCODE_CONFIG_CONTENT`、OpenCodeのmerge順で最後に位置するため、ユーザー設定を置き換えることなく優先されます）は、すべてのtoolを拒否する（`permission: {"*": "deny"}`）agent `aipmt`を定義します。registryはtoolをモデルへ提示しなくなるため、「ファイルを一覧表示して`id`を実行せよ」と命じられても、toolがないと応答します。session sharingは無効化され、外部pluginsは除外され（`--pure`）、`--auto`は決して使用せず、作業directoryには使い捨ての空directoryを使用します。無通知で行われる2つの注入を測定し、無効化しました。`OPENCODE_DISABLE_CLAUDE_CODE`がないと、ユーザーの`~/.claude/CLAUDE.md`が**すべての**promptへ入ります（単純な「こんにちは」でもinputが186 tokensではなく515 tokens）。`OPENCODE_DISABLE_PROJECT_CONFIG`がないと、current directoryの`AGENTS.md`も入ります。「各応答の末尾をBANANAで終える」という指示が翻訳に適用されたことを確認しました。一方、globalの`~/.config/opencode/AGENTS.md`は引き続き注入されます。これを除外するswitchはなく、転用した`XDG_CONFIG_HOME`で回避すると、ユーザーのProviderも隠れてしまいます。小手先の回避策を講じる代わりに、文書化しました。

  - **`exit 0`だけでは何も証明できません。3つ目のCLIでも同じ注意が必要で、さらに固有の落とし穴が2つあります。** 未知の`--agent`でも`opencode run`は失敗しません。stderrにwarningを出し、toolが有効なcoding agentへ**無通知で**フォールバックします。inline configurationが反映されていなければ、書き込み可能なagentで翻訳が始まることになります。そのため出力contractでは、return codeが0であること、`error` eventがないこと、`tool_use`がないこと、最後の`step_finish`が`stop`であること（`length`は切り詰められた応答です）、textが空でないことに加え、このメッセージがないことも検証します。2つ目の落とし穴は、errorのJSON eventが**不透明**なことです。「予期しないserver errorが発生しました。詳細はserver logsを確認してください。」という単なる参照しかなく、実際の原因（`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`、`ProviderAuthError`など）はlogsにしか存在しません。そのため`--print-logs --log-level ERROR`を使用し、後続のBun traceを除いて、stderrの`error="…"` fieldを読み取ります。これにより未知のモデルは1秒で失敗し、その原因も示されます。`--title`は、不要なLLM callも防ぎます。これがなければ、OpenCodeは`small_model`への追加の1 turnによってsession titleを生成します。

  - **Secrets：CodexおよびGrokと同じpattern filterを使用しますが、明示的な例外が1つあります。** `OPENCODE_API_KEY`は保持されます。これはOpenCode自体のキー（Zen gateway、Go subscription）であり、その名前どおりOpenCodeへ送られます。OpenCodeの`auth.json`に相当するもので、aipmtが管理したり課金したりするキーではありません。ProviderはOpenCode内（`opencode auth login`、`opencode.json`）で設定し、aipmtの`.env`では決して設定しません。aipmt側のキーは1つもsubprocessへ到達しません。subscription用CLIとは異なり、CIでは拒否しません。runner上でAPIキーまたはself-hosted modelを使用することは正当な用途だからです。

  - **path traversal防止機能は、raw valueではなく、挿入されるvalueを検査するようになりました。** `provider/modèle`には、1.10.0の保護機能が拒否していた`/`が含まれます。`--model`がファイル名`--include_model`へ挿入されるため、この拒否自体は正当でした。ファイル名labelは、挿入前に`/`、`\`、`:`を`-`へ置換するようになり（`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`、`:`はWindowsでは不正です）、上流の保護機能はこのlabelを検査します。`../../evil`はtarget配下の単純な名前`doc-en-..-..-evil.md`になり、`..`だけは引き続き拒否され、`--target_lang ../x`も拒否されます。scope保護の`_ensure_within_directory`は変更されず、第2の防御層として維持されます。
  - **無料モデルとローカルモデル、および測定結果。** `opencode/mimo-v2.5-free` は1段落を16秒、この README を49秒で翻訳する。`opencode/big-pickle` は200語に40秒かかり、個別には完了する2つのリクエストを同時に送ると、5分間応答がなかった。`opencode/nemotron-3.5-lightning-free` は3分間まったく応答しなかった。そのため、`REGEN_PROVIDER=opencode` では `REGEN_MODEL` を必須とし、並列実行を **2ジョブ** に制限した。ローカル側では、セグメントが最大16,000文字である一方、Ollama はコンテキストを4,096 tokensに設定することが多い。このため、`PARAMETER num_ctx 32768` を指定した `Modelfile` が必須となる。また、品質はモデル次第であり、試験用ファイルでは7Bモデルがリストの順序を逆転させ、コードブロックの閉じ区切りを壊したのに対し、ゲートウェイのモデルはすべてを維持した。

  - **このリポジトリの翻訳が、従量課金 API を経由することは今後一切ない。** `regen_translations.sh` は、`.env` にキーが存在すると即座に OpenAI API を使用し、Codex は明示的に選択した場合にしか使わなかった。まさにこのバージョンの準備中にそれが起きた。28件の翻訳は OpenAI API に送られ、その後、ヒンディー語の CHANGELOG は Gemini API に送られた。しかし、ChatGPT サブスクリプションは、そもそも従量課金を避けるために存在する。キーの自動検出を廃止し、**Codex をデフォルトとして `gpt-5.6-sol`**、すなわち高品質モデルを使用する。`openai`、`gemini`、`grok` では、`REGEN_PROVIDER` に加えて `REGEN_ALLOW_PAID_API=1` が必要になる。これは、決定時に規則が確実に適用されるよう明示的に名付けられた例外である。不明な `REGEN_PROVIDER` は API にフォールバックせず失敗する。10件のテストで、デフォルト、拒否、例外を固定した。このバージョンの28件の翻訳は Codex 経由でやり直した。

  - **rate limit に対する back-off を共通化**（`_retry_on_rate_limit`）した。Codex と Grok のループはラベル以外が同一であり、3つ目のコピーを追加すると重複のしきい値を超えるところだった。3つの CLI エラーは、共通の `_CliCallError` から派生する。いずれかがそこから外れることをテストで禁止しており、外れれば共有ループで検出できなくなる。

  - **テスト**：新規ファイル `tests/test_opencode_provider.py`（51件のテスト）— 完全な出力契約、agent のフォールバック、ログから読み取る原因、重複除去されたテキスト部分と無視される合成部分、process group を終了させる timeout、429に対する back-off、必須かつ検証済みのモデル、secret を使わない preflight、binary の解決、dispatch の接続、ファイル名ラベル、パストラバーサルの反証テスト。`tests/test_review_hardening.py` は、flag の排他性と secret 不在の検証を新しい provider にも拡張する。gate では、文書化された argparse の **22個の flag** が必要になった。全体で **382件のテスト**。

- **1.11.1** ドキュメント修正：README に7つの provider 経路を明記（2026-09-03）：

  - **1.11.0の PyPI ページには「4 APIs + Codex CLI」と記載されていた。** コードでは7つを提供している。OpenAI、Mistral、Claude、Gemini、Grok は API 経由、Codex（ChatGPT）と Grok はサブスクリプション経由で、従量課金はない。紹介文と _Multi-Provider_ の項目から2つの Grok モードが抜けており、14言語の翻訳でも同じ誤りが繰り返されていた。パッケージの詳細説明はバージョンごとに固定されるため、公開ページを修正するには新しいバージョン番号が必要だった。これがこのバージョンの唯一の存在理由である。**コード変更はない。**
  - `CLAUDE.md` を、公開時に導入された内容と整合させた。gate のカウンター（16、`--full` では17）、稼働中の11個の workflow、`gh pr checks` には表示されない2つの Sonar/Codacy カウンター（hotspots、Codacy API）、`ruff-format` による `# nosemgrep` の移動、OIDC 交換に必要な GitHub environments、そして _pending publisher_ は名前を予約しないという事実である。

- **1.11.0** PyPI で公開：リポジトリを clone せずに `pip install ai-powered-markdown-translator`、続いてコマンド `aipmt`（2026-09-03）：

  - **単一ファイルのスクリプトをインストール可能なパッケージに変更。** `translate.py` をルートから `src/aipmt/translate.py` に移動し、console entry point `aipmt` と、それに相当する `python -m aipmt` を追加した。貢献するには clone 済みリポジトリが引き続き必要である。テスト、28言語の翻訳、品質管理ツールはそこに含まれる。ただし、利用するだけなら不要になった。

    - **import 名は `aipmt` であり、決して `translate` ではない。** 実際に衝突し、しかも警告されないためである。PyPI パッケージ `translate`（v3.8.1、最終 upload 2026-07-06）は、同名のディレクトリをインストールする。venv で再現したところ、ディレクトリが module より優先され、`translate.main` が消え、entry point は `AttributeError` で壊れる。それでも `pip check` は「No broken requirements found」と応答し、rc=0となる。ユーザーが単に `pip install translate` をインストールしただけで、有用な診断もなく CLI が壊れ得た。実際の wheel による反証テストでは、パッケージの上から `pip install translate` をインストールし、前後とも `aipmt --help` は rc=0となり、両方の CLI が共存した。
    - **長い distribution 名、短いコマンド。** `ai-powered-markdown-translator` により PyPI 検索でパッケージを見つけられる。頭字語だけでは、すでにプロジェクトを知っている人以外には発見できないが、公開の目的はまさに見つけてもらうことにある。有力だった2つの候補は、確認の結果除外した。`ai-markdown-translator` は、同じ用途のツールによって2024年から npm で使用済みであり、このリポジトリより17か月古い。また、`aimt` は、同じ分野で活発に開発されているパッケージ `aim`（v3.29.1）と1文字しか違わず、長期的な混同を招く最悪の条件だった。なお、調査方法にも落とし穴がある。`pypi.org/project/<nom>/` はどのような名前にも200を返す anti-bot ページであり、信頼できるのは JSON API のみである。
    - **フラットなパッケージではなく `src/` layout。** フラットなパッケージならテスト内の6個の `sys.path.insert(..., "..")` を維持できたが、まさにそれが問題である。それらはパッケージではなくソースツリーを import するため、パッケージングの誤りをすべて隠してしまう。実際のコストは、置換規則が1つ増えるだけである。

  - **キーを一度設定すれば永続的に使えるようになった。** インストール済み CLI には永続的な設定がなく、環境変数と現在のディレクトリにある `.env` しか選択肢がなかった。`find_dotenv` は確かにシステムのルートまで遡るため、**ホームディレクトリ配下で作業している場合**は `~/.env` を見つけられたが、それ以外の場所で作業すると何も見つからなかった。これは設計上の選択ではなく、コマンドを実行した場所に左右される適用範囲だった。そこで、既存の2層の下に第3層として `~/.config/aipmt/.env` を追加した。

    - **優先順位は明示的に実装されているのではなく**、`load_dotenv` のデフォルト値である `override=False` によって生じる。各層は、前の層で空のままだった値だけを補う。したがって、環境変数 → プロジェクトの `.env` → ユーザー設定という順序になる。これは構造ではなく挙動のテストで検証している。2つの呼び出し順を逆にしても、第3層を削除しても失敗する。
    - **TOML ではなく `.env` 形式**を意図的に採用した。`python-dotenv` はすでに依存関係に含まれ、構文も15個の README ですでに文書化されており、同じファイルを両方のスコープで利用できる。新しい依存関係も構文も増えない。場所は、`XDG_CONFIG_HOME` が**絶対パス**の場合はそれに従い、Windows では `APPDATA` に従う。仕様上、相対値は無視する必要がある。そうしなければ、設定場所が再び現在のディレクトリに左右されるためである。
    - **2つの選択肢を、その理由とともに除外した。** システムの keyring（`keyring`）はデスクトップ環境ではより安全だが、headless 環境、すなわち server、container、CI では機能しない。これはまさに一括翻訳のユースケースである。明示的に選択できる機能としては有力だが、デフォルトには適さない。`--api-key` flag を使うと、キーが shell history に残り、`ps` からも見えてしまう。
    - **キーがない場合も stack trace を表示しなくなった。** 以前は、ユーザーに `site-packages` を指す Python の stack trace と、「環境または .env」とだけ述べ、後者をどこに作成すべきか示さないメッセージが表示されていた。現在は、3つの場所を正確なパス付きで列挙し、コマンドは2で終了する。例外処理の範囲は**意図的に狭く**、設定フェーズだけを `except ValueError` で囲んでいる。実行全体を囲むと、翻訳中に発生した本物のバグまで安心感を与えるメッセージに変えてしまう。このリポジトリが追跡しているのは、まさにその失敗形態である。テストでは `main()` のソースを読み、それを禁止している。

  - **修正 — ツールをインストールすると、ユーザーの `.env` が無視されていた。** 引数なしの `load_dotenv()` は現在のディレクトリからではなく、呼び出し元ファイル、つまり `site-packages` から遡る。独自の `.env` を持つプロジェクトから実際の console entry point を実行して測定したところ、`find_dotenv()` は `''` を返してキーを読み込まないが、`find_dotenv(usecwd=True)` なら見つけられた。ツールが clone 済みリポジトリからしか実行されていなかった間は、このバグは存在しなかった。公開後は常に発生し、正しく設定しているにもかかわらず API キーが「見つからない」という症状しか現れないところだった。

  - **3つの gate は、何も検証しなくなっても成功していた。** 移動よりも**前に**意図的に強化した。検出対象の変更後に作成された保護策では、何も証明できないためである。それぞれが元のリポジトリでは成功し、移行済みコピーでは失敗することを、両方向で測定した。

    - **Lizard は存在しないパスを黙って無視する**。rc=0で、「0 file analyzed」となる。複雑度 gate は、出力が0バイトのまま、158 functions / 2247 nloc から3 functions / 34 nloc に減るところだった。現在、scope は配列であり、各要素の存在を検証する。
    - **存在しない module に対する `coverage run --source=` は失敗しない**。stderr に警告するだけで、unittest でも `coverage xml` でも rc=0となり、不完全な report まで公開される。statements は1453から141に減り、ほぼ何も分析されていないのに健全なプロジェクトに見えてしまうところだった。2つの下限で report を保護する。全体の値と、測定対象で最大のファイルの値である。
    - **翻訳の鮮度を調べる probe は、呼び出し形式を構造上検出できない**。argparse の flag を基準にしているが、ファイル名を変更してもそれらは変わらない。再現したところ、module を移動し、15個の README が存在しないコマンドを記載したままでも、判定は「古い翻訳なし」となった。そのため、第7セクションでは option ではなく**形式**を検証し、Lizard hook をスクリプトの実際の scope と照合する。`files:` キーは一致しなくなっても pre-commit を失敗させず、単に**スキップ**させてしまうためである。

  - **`requires-python = ">=3.10"` を単なる宣言ではなくした。** `sonar-project.properties` は、これまで一度も検証されていないにもかかわらず、すでに3.10～3.12を掲げていた。開発環境には3.12しかなく、公開すればこの内部矛盾が表面化するところだった。現在はテスト workflow が3.10、3.11、3.12で test suite を実行し、**パッケージ**をインストールすることで公開上の version bounds も検証する。

  - **下限のみで、上限なし。** `requirements.txt` はテスト済みの lock のままとし、`[project.dependencies]` を公開契約とする。lock の正確な version を公開すると、ほかのパッケージを使用しているすべてのユーザー環境で競合を招く。`<N+1` の上限も設けない。major version への追随が遅れると release gate を失敗させる `check-deps-fresh.sh` と、真っ向から矛盾するためである。下限の組み合わせは解決され、反証テスト `openai==1.0.0` は `ResolutionImpossible` で終了する。これは、検査が何でも受け入れるのではなく、正しく識別している証拠である。また、`pyproject.toml` の version が CHANGELOG の version と異なることを guard で禁止している。PyPI では version 番号を再利用できないためである。

  - **新しい venv で end-to-end 検証済み**：約70 Koの wheel には `aipmt/*.py`、dist-info、license のみが含まれる。`aipmt --help` は22個の flag を表示して rc=0、`python -m aipmt` は「usage: \_\_main\_\_.py」ではなく「usage: aipmt」を表示し、`pipx` によるインストールも機能する。そして何より、**任意のユーザーディレクトリから実際に fr→en 翻訳**を行い、太字、リスト、inline code、リンク、URL が維持され、code block は翻訳されなかった。移行前から存在する318件のテストは、移行前後で byte 単位まで同一の識別子リストを使って成功する。テストが無効化されていないことを証明するのは、この一致であって「OK」ではない。さらに3層設定のテストを12件追加し、合計330件となった。

- **1.10.0** `--use_codex` provider（ChatGPT サブスクリプションの quota）、SDK とモデルの更新、複数段落にわたる news 引用の修正（2026-08-29）：

  - **セキュリティレビュー — PR で導入されたものの、すべての箇所で守られていなかった2つの guardrail**：

    - **Codex の preflight は `.env` 全体を binary に渡していた。** `_codex_preflight` は **`env=` を指定せずに** `subprocess.run` を呼び出していた。subprocess は `os.environ` 全体、したがって `load_dotenv` が読み込んだ `.env` の全内容を継承していた。計測機能を組み込んだ偽の binary で測定すると、**7個の secret**、すなわち6つの provider のキーと `GITHUB_TOKEN` が preflight に渡っていた。一方、対応する `_grok_preflight` では `env=_grok_env()` を正しく渡しており、secret は**ゼロ**だった。これは PR 内部の不整合である。わずか数行先にある `_strip_secret_env` は、まさにこの invariant を守るために存在している。`_codex_env_base()` を抽出して両経路で共有した。修正後の測定では、どちらも secret は0件だった。
    - **「`--deny` fail-closed」という性質は、実際に使用された形式には適用されなかった。** コメントでは、不明な prefix の規則が起動を拒否することを、Grok の confinement 全体の根拠としていた。`grok 1.0.13` で測定したところ、この検証は**括弧付き形式にしか存在しない**。`--deny 'CeciNestPasUnOutil(*)'` は起動を拒否する（「unknown tool prefix」）一方、`--deny 'CeciNestPasUnOutil'` は黙って受け入れられる。しかし、`GROK_DENY_RULES` では括弧なしの名前しか使っていなかった。したがって、xAI 側で tool 名が変更されると、OS sandbox がすでに適用されていない端末上で、唯一測定済みの confinement 層が何の通知もなく消失するところだった。名前付きの8つの規則を `Prefix(*)` に変更し、それぞれを CLI の既知の prefix として検証する。catch-all の `*` は、唯一受け入れられる literal 形式のままとする。検証されない形式への回帰をテストで防止した。
    - **そのほかは問題がないことを確認済み**：command injection はなく（全箇所がリスト形式で、`shell=True` は一切使用せず、文書内容は stdin または `--prompt-file` 経由）、unsafe deserialization もなく（`json.loads` のみを型 guard 付きで使用）、7種類の payload によるパストラバーサル修正の回避も見つからず、`--deny '*'` が CLI によって実際に適用されることも確認した（workdir 外の読み取りで `DENY_ENFORCED` を観測）。
    - また、上で追加した鮮度チェックは、付随的に自身の原則を回避していた。PyPI へのリクエストが失敗したパッケージを黙ってスキップし、gate を成功させていた。現在は、実際に比較されたパッケージ数を数え、coverage が不完全なら失敗する。

  - **依存関係を最新化し、遅れの再発を防ぐ2つのセーフティネットを追加**：
    - **遅延は現実のものであり、長期化していました**：`openai` 2.54 → **3.6.0**、`anthropic` 0.125 → **1.2.0**、`certifi` 2024.8.30 → **2026.7.22** — つまり、すべての provider 呼び出しの TLS を検証するルート証明書ストアが2年遅れていました。特定された原因：**`.github/dependabot.yml` が存在しませんでした**。このファイルがなければ、GitHub が有効にするのは _security updates_ のみであり、Dependabot が PR を提案するのは CVE の対象となった依存関係だけです。そのため、`urllib3` と `idna` は更新された一方で、2つの SDK がメジャーバージョン単位で遅れたままになっていました。
    - **2つのメジャーバージョンは競合せず共存します**。これは以前の推論で懸念されていたこととは異なります。`openai` 3.x と `anthropic` 1.x は **`httpx2`** へ移行しますが、`mistralai` と `google-genai` は `httpx<1` のままです。しかし、これらは別々のディストリビューションです。実際にインストールしたうえで、さらに **7つの provider 経路をエンドツーエンドでテスト**して確認しました。対象は OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI、Grok CLI で、各出力内のインラインコードとリンクも保持されています。「2つの HTTP スタックを避ける」ことは選好にすぎず、障害ではありませんでした。測定によって決着しました。
    - **`requirements.txt` は実際の環境を表していませんでした**：`google-auth`、`cryptography`、および `opentelemetry` スタックは、宣言されないまま作業用 venv にインストールされていました。そのため、新規インストールではテスト対象の環境を再現できませんでした。反対に、`tokenizers`、`huggingface-hub`、`PyYAML` は、どこからも import も要求もされていないのに記載されており、`mistralai` 1.x の残骸でした。このファイルは、直接依存関係のみから構築した venv の完全な依存関係クロージャーとして再生成されています。`pip-audit` では、新しい依存関係セットに既知の脆弱性は報告されていません。
    - **`.github/dependabot.yml`**（新規）は、pip と github-actions のバージョン更新を毎週実行するようにします。マイナー更新とパッチ更新は1つの PR にまとめます。パッチ更新ごとに PR を作ると最終的に無視されるようになり、ノイズは更新の敵だからです。**メジャー更新は個別**とし、それぞれ実際の呼び出しによる検証を必須とします。
    - **`scripts/check-deps-fresh.sh`**（新規、gate に接続済み）は、遅延をプロジェクトの判定結果に反映します。Dependabot は提案するだけで、保証はせず、その PR が積み上がることもあります。メジャーバージョンの遅延 → 失敗、マイナーバージョンの遅延 → 警告とします。常に赤い gate は最終的に無視されるからです。PyPI に接続できない場合 → ローカルでは明示的にスキップし、**CI では fail-closed** とします。実行されなかったチェックは成功ではありません。両方向で検証済みです。修正前の状態（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`）を正確に検出し、マイナーバージョンの遅延については警告だけに留めます。

  - **この PR のレビューから生まれた修正** — 5つのレビューエージェントが diff を徹底的に精査しました。以下の各点はすべて、修正前に**測定によって再現**されており、そのうち2件はこの同じバージョン内で前段の変更によって導入されたリグレッションでした。

    - **修正済みのリグレッション — `_NEWS_CITATION_REGEX` に指数的バックトラッキングがありました。** 複数段落への対応では、繰り返し内に `(?:[ \t]*$|[ \t]+.*)` が導入されていました。`[ \t]+` と `.*` の間で空白の割り当てが曖昧になり、その曖昧さが反復のたびに増幅されます。このパターンにマッチしない `>   texte` 行（完全に正当な Markdown のインデント）で測定したところ、**14行で2,589 ms** だったのに対し、修正後は0.04 msとなり、行を1つ追加するごとに約9倍に増加していました。`--news` モードでは、長くて形式に適合しない blockquote が1つあるだけで、原因を特定できないままジョブのタイムアウトまで翻訳が停止していました。現在は繰り返しが行全体を一括で消費するため（`\n^>(?![ \t]*—).*`）、各反復でマッチする方法は1つしかありません。231記事の実コーパスで検証済みです。キャプチャの差分は**ゼロ**で、引用は同じ423件、複数段落の本文14件も引き続き拡張されています。
    - **2つの provider フラグを同時に指定すると、警告なしに従量課金されていました。** `--use_codex --use_mistral` は受け入れられていました。`_select_provider_client` は Mistral を最初に検査し、`_resolve_provider` は明示的な boolean を優先するため、どちらも Mistral に収束していました。つまりユーザーはサブスクリプションの割り当てを要求したのに、何の警告もなく従量課金されていました。これはまさに `--use_codex` が防止するために存在する障害モードです。現在、6つの provider フラグはすべて `add_mutually_exclusive_group` を経由します。**動作変更**：これまで暗黙に受け入れられていた、2つの provider を組み合わせたコマンドラインは、今後 `argument --use_mistral: not allowed with argument --use_codex` で失敗します。
    - **作業終了時の gate は、プローブがクラッシュしても緑になっていました。** `scripts/check-release-ready.sh` の13個の検査のうち4個が、「stdout を取得し、空なら結論を出す」というパターンに従い、終了コードを一切確認していませんでした。例外（ファイル名の変更、`FileNotFoundError`）は stderr に出力し、stdout を空のままにするため、検査は「問題なし」と結論づけていました。「`exit 0` では何も証明できない」という罠が、それを防ぐために書かれたスクリプト内で再現されていたのです。現在は helper `probe()` が、終了コード0**かつ**終了センチネルを必須とし、プローブは目印の集合が空の場合には結論を出しません。空集合に対するアサーションは常に真になるからです。実証例：上記の排他的グループを追加したことで、provider フラグは `*_group` オブジェクトを経由するようになり、以前の regex `parser\.add_argument\(` ではマッチしなくなりました。その結果、**21個中6個のフラグ**が暗黙に対象外となっていたにもかかわらず、gate は緑でした。
    - **シークレットスキャンは6つの provider のうち4つを見落としていました。** 文字クラス `[A-Za-z0-9]` はハイフンを除外しています。`sk-proj-…`（現在の OpenAI 形式）と `sk-ant-api03-…` は2つ目のハイフンで途切れ、`AIza…` は対象になっていませんでした。パターンを拡張し、`.secrets.baseline` はスキャン対象外としました。また、ガード `.env` は `git diff --cached` を照会していましたが、これはインデックスしか参照しません。そのため、最悪のケースである**すでにコミット済み**の `.env` は決して検出されませんでした。現在は `git ls-files` を照会します。
    - **Codex の「トークンのウォームアップ」はウォームアップになっていませんでした。** 測定の結果、`codex login status` は `~/.codex/auth.json` にアクセスしておらず（mtime とサイズは不変）、そのヘルプには「ログイン状態を表示」と記載されています。しかしコメントでは、トークンを「一度だけ、逐次的に」更新し、1回限り使用できるローテーション型トークンでの同時更新リスクを無効化すると主張していました。記載されていた保護は存在していませんでした。現在のコメントはコードが実際に行うことを説明しており、本当の対策は引き続き `max_jobs=4` です。さらに、このチェックは以前無視していた `CODEX_BIN` を尊重するようになりました。`codex` が `PATH` にない環境では「未認証」として失敗し、誤解を招く診断になっていました。
    - **`.env` はサブシェル内で source されていました。** `detect_provider` はコマンド置換内で呼び出されるため、その export は親シェルに反映されませんでした。`.env` で定義された `GROK_BIN`、`GROK_HOME`、`REGEN_MODEL` は、`main()` 内での読み取りから見えないままとなり、正しい設定でも「Grok バイナリが見つからない」と結論づけていました。
    - **同時実行数は公称上限を50%超えていました。** ガードは README/CHANGELOG のペアを起動した後に配置されていました。`max_jobs=2` で測定されたピークは **3** です。週次割り当てが Chat/Imagine/Voice と共有され、測定不能な Grok では、スクリプトが自ら課した上限が守られていませんでした。また、最終的な件数は表示されるだけで28と比較されておらず、ファイルが欠けていても見過ごされていました。
    - **Grok の出力契約：`stopReason` が存在しない場合、今後は失敗します。** 公表された契約では `end_turn` が必須であるにもかかわらず、コードは「`end_turn` **または存在しない**」を適用していました。このフィールドのない payload、または CLI の更新でフィールド名が変更された payload によって、ガードが暗黙に no-op になっていました。さらに、`max_turn_requests` は rate limit に分類されなくなりました。これはターンの予算を使い切った状態であり、再試行しても90秒の待機時間を費やして同じ結果になるためです。また、`quota` を rate limit のマーカーから除外しました。その理由は、`_codex_is_rate_limited` の docstring にすでに記載されていたにもかかわらず、Grok には適用されていませんでした。
    - **Gemini のフォールバックはモデルごとにメモ化されます。** デフォルトモデルが拒否するにもかかわらず、セグメントごとに `minimal` からやり直していました。そのため、通常の経路でもセグメントごとに400の往復コストが発生し、同じ警告が再表示されていました。何百回も繰り返される warning は読まれなくなります。こうして警告は覆い隠すものへと変わります。
    - **その他**：CI での拒否メッセージが Codex 向けにハードコードされており、`--use_grok_cli` のユーザーを `XAI_API_KEY` ではなく `OPENAI_API_KEY` へ誘導していました。`provider.capitalize()` は「Grok_cli」と「Openai」と表示していました。サブプロセス基盤のコメントは「shim」を両方の CLI に一般化していましたが、Grok バイナリはネイティブ ELF です。正しい根拠は「独自のサブプロセスを spawn するエージェント」です。`subprocess` に関する12件の SAST finding は、根拠とともに `# nosec` / `# nosemgrep` としてマークされています。`shell=True` を使わないリスト形式ではインジェクションは不可能であり、文書の内容が argv を経由することもありません。
    - **エージェント型サブプロセスには、今後シークレットが一切渡されません。** 名前を列挙した deny-list が保護していたのは、**課金**の不変条件（`OPENAI_API_KEY` のない Codex、`XAI_API_KEY` のない Grok）だけでした。測定の結果、**ほかに7つのシークレット**が各サブプロセスへ渡されていました。Anthropic、Mistral、Google、Gemini のキー、もう一方の CLI のキー、さらにシークレットではないものの通信先を変更する `OPENAI_BASE_URL` です。しかし、この2つの CLI は**エージェント**であり、Grok のものは多くの Linux 環境で適用可能な OS sandbox なしに動作します。現在、フィルタリングは名前の列挙ではなく、**名前のパターン**（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`）に基づいて行われます。これにより、このコードが知らなくても、ユーザーが `.env` に追加した変数も対象になります。これらはどれも CLI には必要ありません。認証情報は `~/.codex` と `~/.grok` に保存され、環境変数には決して置かれません。強化された環境で両方の provider をそれぞれ使用し、**実際に翻訳を正常完了**させて検証済みです。
    - **テスト**：新しいファイル `tests/test_review_hardening.py`（21テスト）で、provider フラグの排他性、`stopReason` の契約、news regex の線形性、CI での拒否メッセージ、Gemini のメモ化、サブプロセス環境にシークレットが一切存在しないことを固定しています。最後のアサーションは**汎用的**であり、どのリストにも名前がないキーでも失敗します。一方、既存の除去テストは自身の定数を写しただけのもので、自身のループの故障以外は検出できませんでした。完全なテストスイートは**311テスト**です。
  - **2つの新しいGrok provider**：`--use_grok`（xAI API、キーは`XAI_API_KEY`、従量課金）と`--use_grok_cli`（公式Grok Build CLI、Grokサブスクリプション枠から消費――`--use_codex`と同じ仕組み）。
    - **APIモード、約40行**：xAIのendpointはOpenAI互換のため、clientと`_call_openai`はそのまま再利用され、変更されるのは`base_url`だけです。必要だった調整は1つだけで、すべてに恩恵があります。`finish_reason`が、OpenAIでは`stop`が出力される箇所でxAIが出力する形式`end_turn`にも対応するようになりました。モデル：`grok-4.6`（品質重視）と`grok-4.3`（エコ）。なお、Grokのエコモデルは依然としてリポジトリ内で最も高価です。100万トークン当たり$1.25/$2.50で、`mistral-small-latest`の$0.15/$0.60に対して大幅に高く、このproviderを選ぶ理由は価格ではなくモデルの多様性です。
    - **CLIモード**：Codexを踏襲しつつ、実環境によって避けられない4つの相違点があります。promptはファイル経由で渡されます（`--prompt-file`。CLIはstdinを読み取らず、argv内のsegmentは`ps`から見えてしまうため）。出力はstdout上の単一のJSON objectです（JSONLでも`-o`ファイルでもありません）。サブスクリプションで利用できるのは`grok-4.6`と`grok-4.5`だけであり、sandboxは適用できません（後述）。subprocessの起動処理は`_codex_run_process`でCodexと共通化され、すでにテスト済みのCodex providerの残りの部分には手を加えていません。
    - **`exit 0`だけでは何も証明できないことを実測**：未認証の場合でも、CLIは**stdout**に`{"type":"error","message":"Not signed in."}`を書き込み、終了コード**0**を返します。拒否やターン上限超過も同様に動作します。したがって、出力contractでは4つの条件を同時に満たす必要があります。終了コードが0、error payloadがない、`stopReason == end_turn`、そしてtextが空でないことです。preflightも同じロジックに従います。`grok models`はログアウト状態でも0で終了し、stdoutに「not authenticated」が含まれている場合にのみ未認証と判断できます。
    - **隔離：非対称性を意図的に採用し、文書化。** Codexが`--sandbox read-only`で動作する一方、Grokのsandboxは近年の多くのLinux環境で適用できません。これは、`sudo`なしでは回避不能な、互いに独立した2つのsystem上の原因によります。Ubuntu 24.04以降ではAppArmorが非特権user namespaceをブロックし（`bwrap: setting up uid map: Permission denied`、Grok外でも再現）、container runtime socketのdeny-listは`/run/podman`が`0700`の場合に失敗します（resolverが補足するのは`ErrorKind::NotFound`だけで、EACCESは致命的になります）。最大の落とし穴は、適用できない**組み込み**profileを指定すると、**何の通知もなく非隔離状態で起動する**ことです。そのためscriptはdefaultではprofileを要求せず、黙ってfallbackすることもなく、stderrに警告を出します。保護はCLIの`--deny`ルールに依存し、catch-allの`*`も含まれます。これは実測済みの唯一の_fail-closed_層です（未知のprefixを持つルールがあると起動を拒否します）。`GROK_TRANSLATE_SANDBOX=read-only`で隔離を必須にでき、その場合、マシンが要件を満たせなければ起動に失敗します。
    - **安全対策**：`XAI_API_KEY`、`GROK_API_KEY`、`GROK_SANDBOX`はsubprocessのenvironmentから削除されます（キーがあると従量課金へ切り替わり、継承された`GROK_SANDBOX`は、誤解を招くmessageとともに適用不能なprofileを強制するため）。MCP/hooks/skills/agentsのswitchは無効化され、`--disable-web-search`、`--no-subagents`、`--no-plan`、使い捨てworkdir、CI環境での拒否、process groupを終了させるtimeout、rate limit発生時のback-offも適用されます。`--max-turns`は1ではなく6に設定されています。counterはtoolターンの後にincrementされるため、1では出力が途中で切れてしまいます。
    - **quota**：Grokのpoolは週単位で、**Chat、Imagine、Voiceと共有**されます。また、それを表示するcommandはありません。これは、`account/rateLimits/read`で消費量を数値化できるCodexとは対照的です。そのため`regen_translations.sh`は並行数を2に制限し、明示的に警告します。
    - **テスト**：新しいファイル`tests/test_grok_provider.py`（24テスト）。全suiteは**290テスト**。
  - **修正済みのbug――英語の複数段落からなる引用が一部しか保護されていなかった（`--news`モード）**：`_NEWS_CITATION_REGEX`は引用本文として、**連続する**`>`行だけを受け入れていました。引用が複数の段落にまたがる場合（空の`>`行で区切られる場合）、最後の段落だけが取得されてplaceholderに置換され、それ以前の段落はLLMへ送られて翻訳されていました。これは、`--news`が保証するために存在する動作と正反対です。繰り返し部分は内部の空の`>`行を許容するようになり、さらにnon-greedy化されました。これにより、最初に見つかった空行ではなく、斜体行の直前にある空の`>`で停止します。
    - **実測した規模**：実際の198記事からなるcorpusでは、419件中11件の引用が該当しました。regressionはありません。新しいregexが取得する引用数は完全に同じで、複数段落の本文だけが拡張されています（408件の本文は同一、11件は拡張）。帰属を示す`> — …`行も、維持されたlookaheadにより、引き続き本文へ取り込まれることはありません。
    - **end-to-endでの証明**：69 koの記事をja/arへ翻訳したところ、以前は日本語で`> GLM-5.3がオープンウェイト化。`となり、アラビア語でも同様に翻訳されていた引用の最初の段落が、現在は`> GLM-5.3 is now open-weight.`のまま維持されます。英語の引用行数は9行から10行へ戻り、sourceと一致しました。
    - なお、この不具合は下流のvalidatorでは検出されていませんでした。validatorは引用の存在を確認しますが、引用が完全かどうかまでは確認しないためです。
  - **default providerで実測されたコスト削減**：`_openai_extra_kwargs`は、モデル名が`gpt-5`で始まる場合、`--eco`でも常に`reasoning_effort="medium"`を送信していました。`gpt-5.4-mini`で10語の文を翻訳して測定した結果、`medium`ではreasoning tokenが45、出力tokenが65だったのに対し、`none`ではそれぞれ0と14でした。翻訳にreasoningは何も寄与せず、各ファイルの各segmentで料金が発生していました。defaultは`--eco`では`none`となり、それ以外では引き続き`medium`です。CLIで明示的に渡された値が引き続き優先されます。`--reasoning_effort`は`low`/`medium`/`high`に加え、`none`と`xhigh`にも対応しました（すべての値がすべてのモデルで受け入れられるわけではありません。たとえば`minimal`は`gpt-5.4-mini`に拒否されますが、既存のparameterなしでのretryがこのケースに対応します）。
  - **SDKの更新とGeminiのmigration**：`google-generativeai`（supportは2025-11-30に終了し、repositoryはarchive済み）は、統合SDK **`google-genai`**に置き換えられました。`genai.Client(api_key=...)`、続いて`client.models.generate_content(model=, contents=, config=)`を使用し、system promptはsegmentに連結する代わりに`system_instruction`として渡されます。`mistralai`は**2.9.4**へ更新されました（importは`from mistralai.client import Mistral`となり、旧形式では`ImportError`が発生することをwheel内で確認済み）。`anthropic`は**0.125.0**、`openai`は**2.54.0**へ更新されました。これらは`httpx2`への移行前の最終versionであり、venv内に2つのHTTP stackを共存させないためです。これに伴い、`httpx` 0.28.1と`pydantic` 2.13.5の固定も解除されました。
  - **文書ではなく実際のテストで捕捉された2つのregression**：
    - `anthropic` ≥ 1.0は、`max_tokens`から10分を超えると予想される非streaming callをclient側で拒否します（`ValueError: Streaming is required...`）。この安全機構は0.34.2には存在せず、`max_tokens=32768`を指定したすべてのClaude callを壊していました。明示的な`timeout`（`CLAUDE_TIMEOUT`、defaultは900 s）で修正し、完全なresponseだけを利用するcallをstreamingへ切り替えずに済むようにしました。
    - `thinking_level="minimal"`を受け入れるのはGemini catalogの一部だけです。`gemini-3.1-flash-lite`は対応していますが、`gemini-3.7-flash`と`gemini-3.1-pro-preview`は400で拒否します。このため`_gemini_generate_with_fallback`では、既存のOpenAI fallbackにならい、`minimal` → `low` → thinking_configなし、というcascadeを採用しています。最適化parameterが原因で翻訳全体が失敗してはなりません。
  - **defaultモデルを刷新**し、それぞれ実際のcallで検証しました。OpenAIは`gpt-5.5` → **`gpt-5.6-terra`**（28件のbatchで−60 %）、`gpt-5.4-mini` → **`gpt-5.6-luna`**（−73 %）。Claudeは`claude-sonnet-4-6` → **`claude-sonnet-5`**（より安価で新しい）、`claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（日付なしのcanonical ID）。Geminiは`gemini-3.1-pro-preview` → **`gemini-3.7-flash`**、`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（stable versionで、`3.5-flash-lite`より安価）。Mistralは変更なく、`mistral-large-latest`が4つの中で引き続き最も優れた費用対効果を示します。なお、`gemini-3.1-pro-preview`より新しいProクラスのGeminiモデルは存在しません。2026年5月に発表されたGemini 3.5 Proは結局releaseされず、3.5/3.6/3.7系列はすべてFlash専用です。
  - **Gemini切り替え前に実測したA/B比較**：`README.md`を`gemini-3.1-pro-preview`と`gemini-3.7-flash`でそれぞれ日本語へ翻訳しました。構造は完全に同一で（21個のlist、18個のcode block、13個のHTML link、13個のimage、すべてのURLを維持）、所要時間は**48 sに対して8 s**でした。この2モデルを翻訳や非Latin scriptで比較した公開benchmarkが存在しないため、この測定がなければ切り替えは単なる推測に基づくものになるところでした。
  - **Claudeのresponse blockをfiltering**：`_call_claude`はtypeをfilteringせずに`block.text for block in response.content`を実行していました。adaptive reasoningモデル（Sonnet 5以降）は`thinking` blockを途中に挿入します。このblockが公開するのは`.text`ではなく`.thinking`であるため、最初のsegmentで不透明な`AttributeError`が発生し、翻訳が壊れる可能性がありました。`thinking`、`redacted_thinking`、`tool_use`、`tool_result`のblockは除外されるようになりました（textを持つ未知のtypeを許容し続けるためnegative listを採用）。text blockが1つもないresponseでは、明示的なerrorが発生します。`thinking={"type": "disabled"}`は各callへ渡されます。
  - **`MODEL_TOKEN_LIMITS`を再同期**：廃止日を過ぎたモデルを削除しました（`magistral-*`系列は2026-07-31に廃止、`gemini-2.0-*`は2026-06-01、`gemini-3-pro-preview`は2026-03-09、ならびに`claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。上限値を修正しました。Mistralは128K → **256K**（Large 3 / Small 4世代）、Geminiは1 000 000 → **1 048 576**（実際のinput上限）、`claude-opus-4-5`は200K → **1M**、`gpt-5.6-*`系列は400K → **1,05M**。Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest`、`ministral-*`系列を追加しました。なお、これらの上限値は引き続き参考値であり、`translate()`によってsegmentationは`min(16000, limite)`に制限されます。
  - **Provider `--use_codex`**：従量課金 API を呼び出す代わりに、公式 Codex CLI（`codex exec`）を非対話モードで操作する5番目の provider。翻訳には、すでに支払い済みの ChatGPT サブスクリプション枠が使用される。この用途について OpenAI が文書化している唯一の方法であり、プラン別の利用可否表では「Codex SDK、`codex exec`、およびスクリプト化可能なワークフロー」が Plus/Pro/Business/Enterprise で利用可能と記載されている。一方、`~/.codex/auth.json` のトークンでは API Platform の呼び出しを認証できない（また、このスクリプトがそれを読み取ることもない。認証とその更新は引き続き CLI が管理する）。
  - **npm だけでなく pip でもインストール可能な Codex バイナリ**：`_resolve_codex_binary()` は、まず `CODEX_BIN`、次に `PATH`、その後 OpenAI が公開する公式 Python パッケージ **`openai-codex-cli-bin`**（`openai-codex` SDK の依存関係）からバイナリを検索する。そのため、Python プロジェクトで `--use_codex` を使用する際に、グローバルな npm インストールは不要になった。このパッケージは `requirements.txt` には追加されていない。バイナリのサイズが約250 MBあり、任意選択の provider のために全ユーザーへ負担させることになるためである。エンドツーエンドで検証済み：`codex` が `PATH` に存在しない状態でも、解決処理によってパッケージ内のバイナリが検出され、完全な翻訳が6秒で完了する。
  - **「サブスクリプションモード」の保証**：`OPENAI_API_KEY` と `CODEX_API_KEY` はサブプロセスの環境から削除される。この保護がなければ、`.env` に存在するキーによって、目に見える通知なしに Codex が従量課金へ切り替わる可能性がある。これはまさに、この provider が回避するために存在する事態である。
  - **テストで固定された CLI の落とし穴**：
    - `codex exec` は、プロンプトが引数として渡された場合でも stdin を読み取る。stdin を閉じないと、コマンドはモデルを一度も呼び出さないままタイムアウトまで待機する（再現結果：180秒後に終了コード124、出力0バイト）。したがって、`communicate(input=...)` は必須である。
    - npm でインストールされた `codex` は、実際の Rust バイナリを `spawn` する Node shim である。このバイナリは Python プロセスの**孫プロセス**であり、`subprocess.run(timeout=)` に対する `SIGKILL` 後も生き残り、クォータを消費し続ける可能性がある。そのため、`Popen(start_new_session=True)` と `os.killpg` を使用する。
    - CLI は `turn.failed` を出力していても終了コード0で終了する場合がある。戻りコードに加えて JSONL 出力（`--json`）も検査し、終了コードが0でも `-o` ファイルが存在しない場合は、空のセグメントを生成せず明示的なエラーを発生させる。
  - **レート制限時のバックオフ**：CLI は内部リトライを一切実装していない（`max_retries = 0`）。分類は部分文字列ではなく、JSON payload の構造（`status: 429` / `error.type`）に基づいて行われる。「quota」という単語は、回復可能な429にも恒久的な `insufficient_quota` にも出現するためである。
  - **CI 保護**：`CI` または `GITHUB_ACTIONS` が定義されている場合、`--use_codex` は拒否される。サブスクリプション認証は共有 runner 向けではなく、OpenAI も公開リポジトリでこのワークフローを使用しないよう明示的に推奨している。
  - **モデル**：`gpt-5.6-sol`（品質）と `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` ファミリーは CLI と API Platform で共通だが、ChatGPT アカウントですべてを利用できるわけではない。allowlist はローカル検証なしでサーバー側に適用され、通常とは異なるモデルを指定すると警告が表示される。Plus プランでは、5時間枠あたり Sol が10～100メッセージであるのに対し、Luna は250～2,000メッセージを利用できるため、あらゆるバッチ処理には `--eco` モードを推奨する。
  - **修正済みのバグ — `regen_translations.sh` が完全な成功後にもエラー終了していた**：`trap ... EXIT` は、trap 実行時にはすでに存在しない `main()` の `local` 変数 `failed_log` を参照していた。`set -u` では、これによって `failed_log: unbound variable` が発生し、28件の翻訳がすべて正しいにもかかわらずスクリプトが終了コード1で終了していた。その結果、最もコストの高い再生成直後の段階で `release.sh --auto`（`set -e`）が中断される可能性があった。変数をグローバルに変更し、trap でその存在を検査するようにした。有用な副作用として、これまでこのエラーに隠されていた実際の翻訳失敗が、終了時の概要に再び表示されるようになった。
  - **`REGEN_MODEL`**：provider の既定値より優先して特定のモデルを強制する `regen_translations.sh` の新しい環境変数。たとえば `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol` を指定すると、処理量重視の `--eco` モデルではなく、サブスクリプション枠の上位モデルで再生成できる。
  - **`regen_translations.sh`**：明示的な任意選択として利用可能な `REGEN_PROVIDER=codex`（ユーザーが知らないうちにサブスクリプション枠を消費しないよう、自動検出は一切行わない）。並列処理を開始する前に、トークンを逐次的に一度だけ更新する。Codex の refresh はローテーション式かつ一度限り使用可能であるため、並行 job があると `codex login` セッションが無効になるためである。また、並行数は4に抑えられる。
  - **関連するリファクタリング**：`_dispatch_provider_call` は、処理チェーン全体に4番目の真偽値を伝播させる代わりに、provider 名を返す `_resolve_provider()` を使用することで、引数を8個から6個に削減した。最小限の `Namespace` で `translate(..., use_mistral=True)` を呼び出すテストを維持するため、明示的な真偽値は引き続き `args` より優先される。
  - **テスト**：新しいファイル `tests/test_codex_provider.py`（48テスト）で、argv、不要な値を除去した環境、前置き禁止の契約、無言の失敗、timeout/killpg、バックオフ、preflight、provider 解決、Gemini の推論カスケード、Claude ブロックのフィルタリング、および複数段落のニュース引用を網羅。テストスイート全体は290テスト。
  - **実環境での検証**：プロジェクトの `README.md` を Codex で**14言語**に翻訳した結果、参照翻訳と構造が完全に一致した（コードブロック14個、見出し24個、表25行、HTML リンク13個、画像13個、URL 19個、コードブロックは文字単位で同一、placeholder の残留ゼロ）。69 KBのニュース記事を `--news` モードで処理したところ、`gpt-5.6-luna` と `gpt-5.6-sol` の両出力が、en/ja/ar について後段のアプリケーション検証を通過した。`account/rateLimits/read` で測定した消費量は、`--eco` モードではカウンターの丸めしきい値未満（5時間枠の0%）にとどまった。

- **1.9.2** 入れ子の括弧またはフランス語接頭辞を含むニュース帰属 URL の抽出を修正（2026-05-11）：

  - **修正済みのバグ**：`_protect_news_quotes` における帰属 URL の抽出では、正規表現 `re.search(r"\((.+?)\)", attribution)`（括弧内の遅延キャプチャ）を使用していた。`(relayé par [@user sur X](https://x.com/.../123))` のような帰属表記（入れ子の括弧：外側の `(` と Markdown リンクの `]()`）では、最初に現れた `)` でキャプチャが終了し、フランス語接頭辞を含む切り詰められた文字列 `relayé par [@user sur X](https://x.com/.../123`（末尾の `)` なし）が生成されていた。その結果、`_validate_news_post` は翻訳済み出力内でこの文字列を検索して必ず失敗していた（理由は2つあり、`)` が切り詰められていることと、「relayé par」が `relayed by`/`weitergeleitet von`/… に翻訳されること）。low → medium → high → gpt-5.5 の完全なカスケードでも通過できなかった。
  - **修正**：正規表現を `re.search(r"\]\(([^)]+)\)", attribution)` に変更した。Markdown リンクの `](url)` を明確に対象とし、フランス語接頭辞や切り詰めを含まない**純粋な URL のみ**をキャプチャする。翻訳中も `#URL{N}#` placeholder によって不変性が維持される。問題となっていた次の2パターンに対応する：
    - `(relayé par [@account sur X](url))` — 入れ子の括弧
    - `via [@source](url)` または `selon [@author](url)` — 外側の括弧がないフランス語接頭辞
  - **テスト**：`test_silent_failure.py` の `TestNewsCitationExtraction` クラスに2件追加：
    - `test_extract_attribution_url_with_nested_parens`（Genspark CEO E2B のバグを正確に再現したケース）
    - `test_extract_attribution_url_with_french_prefix`（`via` を含む変種）
  - **カバレッジ上の不足**：`check-editorial-coverage.py` は編集上の構文を検証するが、translator による翻訳可能性は検証しない。将来的な改善案（v1.9.2 のスコープ外）として、公開**前**に危険なパターンを検出できるよう、dry-run で帰属情報の抽出をシミュレートする検査が考えられる。

- **1.9.1** 翻訳注記 marker 内の CTA ラベルの i18n を修正（2026-05-10）：

  - **修正済みのバグ**：翻訳済みファイル上部の marker バナーにある CTA リンクのラベル `[Voir le projet sur GitHub ↗]` が、`target_lang` に従わず、すべての対象言語で**フランス語のまま**になっていた。これは LLM には一切渡されず（URL とリポジトリの slug を保持するため Python 側で組み立てられる）、翻訳フェーズでは修正できなかった。v1.9 で `marker` 形式を追加して以降の無言のリグレッションである。
  - **修正**：15言語をそれぞれのローカライズ済みラベルへ対応付ける新しい定数 `_VIEW_PROJECT_LABELS` を追加。`_translation_note_invariants(target_lang)` と `_assemble_translation_note_paragraphs(phrase, target_lang)` が対象言語を伝播するようになった。言語が不明な場合は `fr` へフォールバックする（安全対策であり、KeyError は発生しない）。
  - **テスト**：`test_source_emits_three_paragraphs_repo_title_description_link` を調整（対象言語 `ja` → 期待される日本語ラベル）。新しいテストを2件追加：`test_source_link_label_localized_per_target_lang`（ラテン文字、表意文字、アブジャドの各文字体系を含む7言語でパラメータ化）と `test_source_link_label_falls_back_to_french_for_unknown_target`。`test_translation_note_position.py` のテスト総数は38件から40件になった。
  - **後方互換性**：既定値付きのシグネチャ `target_lang="fr"` により、`args.target_lang` を指定しない外部のプログラム呼び出し元も変更なしで引き続き動作する。
- **1.9** サイレント障害の修正 + 包括的な品質ツール + 複数位置対応の翻訳注記（2026-05-07）：
  - **複数位置対応の翻訳注記 + 「embed card」マーカー形式**：
    - 新しいCLIオプション（追加のみ、デフォルトは変更なし → **破壊的変更なし**）：
      - `--note_position {top,bottom,both}`（デフォルト：`bottom`）：翻訳済みファイルの先頭、末尾、または両方に注記を配置します。
      - `--note_format {legacy,marker}`（デフォルト：`legacy`）：
        - `legacy` はv1.8の動作（太字の段落 `**…**`）を**バイト単位で完全に**再現します。
        - `marker` は、非表示のMarkdownリンク参照定義（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）に続けて、「GitHubリポジトリ埋め込みカード」風の表示向けに構造化された**3段落のblockquote**を出力します。内容は、インラインコードによるプロジェクト名（`**\`ai-powered-markdown-translator\`\*\*`）、LLMによって翻訳された説明、表示される矢印付きのCTAリンク（`[Voir le projet sur GitHub ↗](URL)`）です。ビルド時にremarkプラグインから利用できます（jls42.orgのブログ → `remark-translation-banner` プラグインを参照）。
    - **LLMには一切送信されない不変要素**：リポジトリ名とGitHub URLは、説明文の翻訳後にPython側で組み立てられます。LLMが `ai-powered-markdown-translator` や `https://github.com/jls42/...` を目にすることはないため、レンダラー、大文字・小文字、スキームのいずれも変更されないことが保証されます。
    - **frontmatter対応の挿入**：`top` または `both` モードでは、注記はYAML frontmatterを閉じる `---` ブロックの**後**に挿入されます（Astro Content Collections／gray-matterへの安全対策）。ヘルパー `_split_frontmatter` はファイル先頭の `---\n…\n---\n` を検出して、その完全性を維持します。終了fenceのない未閉鎖のfrontmatterでは**`RuntimeError` を送出**し、誤った位置に注記を書き込む代わりに、そのファイルを `failed_files` に報告します。
    - **ホワイトリスト方式のモデル名サニタイザー**：`_sanitize_model` は `[A-Za-z0-9._:/-]` 以外のすべての文字を `_` に置換し、空になった場合は `unknown` にフォールバックします。Astroのremarkプラグイン側のバリデーターと整合し、マーカー形式を壊す文字（空白、引用符、括弧、カンマなど）を無害化します。
    - **内部リファクタリング**：`_append_translation_note`（1つのモノリシックな関数）→ 7個の純粋ヘルパー（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。builderとcomposerを分離し、builderは区切りなしの純粋なブロックを返し、composerは位置に応じて `\n\n` を適用します。本番処理とsource用ヘルパーは、同じ3段落アセンブラーを共有します。
    - **空行を保持する `_quote_lines`**：各行の先頭に `> ` を付け、空行は `>` のみの行へ変換します。これによりmdastは、blockquoteを改行付きの単一段落ではなく、3つの独立した段落（タイトル／説明／リンク）として認識できます。
    - **適応型 `_build_translation_note_block`**：LLMが保持した段落数に応じて処理します（3段落＝完全なカード形式、2段落＝文 + リンク、1段落＝フォールバック）。1段落のフォールバックでは、Markdownリンク `](` が検出された場合、リンクを囲む `<strong>` の表示が不安定になるため、**`**...**` で囲まなくなりました**。
    - **後方互換性**：`_compose_with_notes` 側では `getattr(args, "note_position", "bottom")` と `getattr(args, "note_format", "legacy")` を使用します。これらの属性を持たないNamespace（既存のテストや外部からのプログラムによる呼び出し）も、変更なしで引き続き動作します。
  - **長文翻訳におけるサイレント障害の修正**：
    - すべてのprovider（OpenAI、Mistral、Claude、Gemini）で翻訳後の言語を検証：決定論的レイヤー（原文の逐語的な残存を検出）+ 確率的レイヤー（`langdetect`）
    - `finish_reason`／`stop_reason` のホワイトリスト：ホワイトリスト外のすべての状態（truncation、content_filterなど）で `RuntimeError` を送出
    - Claudeの `max_tokens`：`4096` → `32768`（16kセグメントで潜在的なtruncationを回避し、FR→JA/ZH/KO/AR/HIのスクリプト間変換に余裕を確保）
    - 見出しを考慮したセグメンテーション：セグメント後半のH2/H3を優先（各セグメントが意味的に完全なセクションから始まるようにします）
    - ゼロ以外のexit codeまでエラーを伝播：`translate_markdown_file` は型付きステータス `success`／`failure`／`skipped` を返し、1つでもファイルが失敗した場合、`main()` は `sys.exit(1)` を返します（単一ファイルとbatchの両方）
    - すべてのproviderに空コンテンツguard、原文／出力の健全性比率（500文字以上の場合、5%未満は拒否）、コードplaceholderの検証（`#CODEBLOCK`／`#INLINECODE`）、LLM処理後の正規化（見出しに連結された区切り／リンク）、`reasoning_effort` を使用しない `BadRequestError` retryを追加
    - 依存関係 `langdetect==1.0.9` を追加
  - **pre-commit品質ツール**（「完全版EurekAI方式」、14個のhook）：
    - Pre-commit：ruff（lint + format）、shellcheck、prettier（md/yaml/json）、detect-secrets（4個のAPI keyを保護）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（whitespace、EOF、large-files、shebangsなど）
    - Pre-push：mypy（段階的なlaxモード）、Opengrep SAST（translate.py + scripts/）、pip-audit（初期reportingモード）、unittest discover（tests/ + scripts/tests/）
    - `./venv/bin/python` を使用するローカルwrapperを `scripts/` に配置
    - `scripts/audit_verdict.py`：11件のunittestを備えたpip-audit用JSON parserで、jls42-astroのparserをPythonへ移植
    - 初期のruff違反7件を修正：B904（raise from）×2、B007（未使用のdirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizardでは一時的に `translate.py` を除外（CCN 21～47の関数が4個あり、リファクタリングを計画済み）— scripts/には厳格なgateを適用
  - **SonarCloud + 包括的なカバレッジ**：
    - GitHub Actionsワークフロー `SonarCloud`（sonarcloud.yml + sonar-project.properties）：pushおよびpull-requestのたびに分析し、`coverage.xml` でcoverageを取得
    - README上部に11個のSonarCloud badge（Quality Gate、Security／Reliability／Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）
    - `tests/test_silent_failure.py`（stdlibの `unittest`）：サイレント障害のエラーチェーンを構成する6つの連結部分をカバー
    - `tests/test_orchestration.py`（+79件のテスト）：`translate.py` のオーケストレーション層（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` のTypeError + BadRequestErrorフォールバック、o1-seriesのprompt形式、`_validate_translation_output` のearly-return分岐）をカバー
    - `scripts/tests/test_audit_verdict.py`：`main()`（stdin/stdout）と `if __name__ == "__main__"` ブロックをsubprocess経由でカバー
    - **新規コードのcoverage**：75.5% → 約98%（translate.py 98%、scripts/audit_verdict.py 97%）
  - **テスト**：`tests/test_translation_note_position.py` は位置 × 形式のマトリクス（E2Eの `marker+top|bottom|both` と `legacy+top|bottom|both` を含む）、複数行への接頭辞付加、バイト単位の後方互換性（golden literal）、sanitizer、frontmatterの分割（未閉鎖のfenceでの送出を含む）、3段落形式、2段落フォールバック、1段落 + Markdownリンクのguard、さらにタイトルとURLがLLMへ決して送信されないことをassertする重要な安全策 `TestLLMPayloadExcludesInvariants` をカバーします。**190件のテストが成功**し、リグレッションは0件です。
  - ドキュメント：`README.md`（フランス語 + 14言語への翻訳）にbadgeを追加、`CLAUDE.md`（pre-commitワークフロー + 詳細なCI監視）、28件の翻訳を再生成
- **1.8** `--news` モード + 2026年モデルへの更新（2026-03-17、tag `v1.8`）：
  - デフォルトモデルを更新（2026年3月）：
    - OpenAI高品質：`gpt-5` → `gpt-5.4`
    - OpenAI低コスト：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini高品質：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）および `gemini-3.1-pro-preview`（1M）のtoken上限を追加
  - 初期 `--news` モード：placeholder `#NEWSQUOTE\d+#` による英語引用の保護、`LANG_FLAGS` のmapping（15言語）、対象言語ごとのフラグ管理
  - 復元前にnews placeholderを検証（リグレッション：LLMがplaceholderを削除すると、引用のない出力がサイレントに生成されていました）
  - `regen_translations.sh` スクリプトをポータブル化（絶対パスを使用し、pwdへの依存を解消）
  - README／CHANGELOGのlanguage barにフランス語へのリンクを追加し、28件の翻訳を再生成
- **1.7** 新機能：
  - 翻訳時に元のファイル名を保持する `--keep_filename` オプション
  - API keyを自動的に読み込む `.env` ファイルのサポート
  - **インラインコードの保持**：翻訳中にbacktick（`` `...` ``）が保護されるようになりました
  - system promptの改善：
    - YAML frontmatter内の引用符をより適切に処理
    - template変数 `{variable}` を保護
    - 要求されていない翻訳者注記を禁止
  - 364ファイルで正常にテスト済み（jls42.orgブログの移行）
- **1.6** 新機能：
  - 翻訳用Google Gemini APIのサポート（`--use_gemini`）
  - 2026年のデフォルトモデルへ更新：
    - OpenAI：`gpt-5`（高品質）、`gpt-5-mini`（低コスト）
    - Claude：`claude-sonnet-4-5`（高品質）、`claude-haiku-4-5`（低コスト）
    - Gemini：`gemini-3-pro-preview`（高品質）、`gemini-3-flash-preview`（低コスト）
  - より高速で低コストなモデルを使用する低コストモード（`--eco`）
  - ディレクトリを走査せずに単一ファイルを翻訳（`--file`）
  - 新しい簡略化された命名パターン：`{base}-{lang}.md`
  - モデル名を含む従来の形式を保持する `--include_model` オプション
  - 一覧にないモデルをデフォルトのtoken上限（128k）でサポート
  - READMEを14言語に翻訳
- **1.5** 改善：
  - **API keyとデフォルトモデルの更新：**
    - **OpenAI：** `DEFAULT_MODEL_OPENAI` から `"gpt-4o"` へ更新。
    - **Mistral AI：** `DEFAULT_MODEL_MISTRAL` から `"mistral-large-latest"` へ更新。
    - **Anthropic Claude：** `DEFAULT_ANTHROPIC_API_KEY` を追加し、`DEFAULT_MODEL_CLAUDE` から `"claude-3-5-sonnet-20240620"` へ更新。
  - **翻訳promptの最適化：**
    - 直接翻訳と翻訳注記用のpromptを拡充して明瞭性と効率性を高め、メタデータと特定の書式要素を保持するための詳細な指示を追加しました。
  - **コードのリファクタリング：**
    - Mistral AI clientの初期化で `MistralClient` を `Mistral` classに置き換えました。
    - 可読性と保守性を高めるためにimportを再編成しました。
    - 翻訳時に元の書式を保持できるよう、テキストのセグメンテーションとコードブロックの処理を改善しました。
  - **出力ファイルの管理：**
    - 出力ファイル名におけるモデルと言語の順序を入れ替え（例：`f"{base}-{args.target_lang}-{args.model}.md"`）、翻訳の整理と検索を容易にしました。
  - **その他の改善：**
    - 不要な空行を削除してコードを整理しました。
    - スクリプトの構造と可読性を向上させるために軽微な調整を行いました。
- **1.4** 新機能：
  - 翻訳用Anthropic Claude APIのサポート
  - 明瞭性と効率性を高めるためのprompt最適化
  - コードの保守性を向上させるための軽微な調整
- **1.3** 改善と新機能：
  - コードブロック処理の改善
  - 出力ファイル管理の改善
  - 既存ファイル検出の改善
  - 翻訳を強制する `--force` オプション
  - 出力ファイル名におけるモデルと言語の順序を入れ替え
- **1.2** changelogの修正
- **1.1** Mistral AI APIのサポートを追加
- **1.0** 初期バージョン - OpenAI APIをサポート

**gpt-5.6-solを使用してフランス語から日本語に翻訳された記事。**
