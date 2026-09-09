### 変更履歴

🌍 [フランス語](CHANGELOG.md) | [英語](CHANGELOG-en.md) | [スペイン語](CHANGELOG-es.md) | [中国語](CHANGELOG-zh.md) | [ドイツ語](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [韓国語](CHANGELOG-ko.md) | [アラビア語](CHANGELOG-ar.md) | [ヒンディー語](CHANGELOG-hi.md) | [イタリア語](CHANGELOG-it.md) | [オランダ語](CHANGELOG-nl.md) | [ポーランド語](CHANGELOG-pl.md) | [ポルトガル語](CHANGELOG-pt.md) | [ルーマニア語](CHANGELOG-ro.md) | [スウェーデン語](CHANGELOG-sv.md)

- **1.13.1** 依存関係の鮮度：遅れを読み飛ばせる警告では済ませない（2026-09-09）：

  - **カウントされない警告は見落とされる警告である。** `check-deps-fresh.sh` は数日前から `openai` と `anthropic` の遅れを通知していたが、ゲートの要約行は失敗しか数えていなかったため、数行上に遅れが記載されているにもかかわらず「準備完了：N 件のチェックが成功」と表示されていた。最後の行を読む人には――そして誰もがそうする――知る術がなかった。現在は判定に警告数が含まれ、逐次表示する代わりに専用カウンターで集計される。
  - **遅れにはリリースノートが添えられる。** バージョン番号だけでは何が変わったのか分からず、適切なファイルを自分で探す手間こそが、この確認手順を飛ばす原因になる。チェックでは、遅れている各パッケージについて、メジャーかマイナーかを問わず CHANGELOG のアドレスとその理由を表示する。SDK のマイナー更新でも、このプロジェクトが依存する要素がすでに変更されたことがあるためだ。
  - **`openai` 3.8.0 → 3.10.0 および `anthropic` 1.3.0 → 1.4.0。固定前にリリースノートを確認済み。** OpenAI 側では、この範囲における動作変更は一つだけだった。数値の `Retry-After` ヘッダーが浮動小数点数の範囲を超えた場合、短いバックオフへのフォールバックは行われず、再試行せずに元のエラーが返されるようになった。このプロジェクトが依存する部分には変更がない。追加フィールドに対するモデルの許容性も変わっておらず、両方のタグのコードで確認済みであるため、OpenRouter が選択肢に追加する `native_finish_reason` と `error` は引き続き受け入れられる。Anthropic 側では、SDK が `httpx2` を期待する箇所に `httpx` パッケージのオブジェクトを渡すと、明示的な `TypeError` で拒否する新しいガードが追加された。このプロジェクトが渡すのは浮動小数点数だけであることを確認済み。10 分を超える非ストリーミング呼び出しを拒否する規則は、両バージョン間でバイト単位に同一である。免除を可能にするのは明示的な `timeout` であり、その 32,768 tokens はしきい値の 21,333 を上回る。
  - **検証済み**：更新後のバージョンで 502 件＋31 件のテストスイート、インストール済み環境と一致する `requirements.txt` の閉包（41 件の固定）、および各 SDK――OpenAI と Claude――で `--news` モードの文書を実際に一度ずつ呼び出し、ソースと同一の構造であることを確認。

- **1.13.0** Provider `--use_openrouter`：中国製のオープンモデルを含む約430モデルへ接続する従量課金ルーター（2026-09-05）：

  - **9 番目の provider 経路を、8 番目と同時に提供。** 1.12.0 は PyPI で公開されなかったため、OpenCode と OpenRouter の両ルーターを同時にリリースする。[OpenRouter](https://openrouter.ai) では、ここにあるほかの provider が提供していないモデル――Kimi、Qwen、DeepSeek、Z.ai――に、使用量に応じて課金される単一のクレジットと一つのキーでアクセスできる。endpoint は OpenAI 互換であるため、クライアントは xAI と同じである。**この provider を区別するものはすべてプリフライトに集約されており、その各規則は API での測定結果に基づいている。**

  - **同じモデルが上限の異なる数十社のホスティング事業者から提供される一方、ルーティングはその違いを認識しない。** 測定結果：`z-ai/glm-5.2` には 33 社、`z-ai/glm-5.3-flash` には 23 社のホスティング事業者があり、そのうち一社は**出力が 2,048 tokens に制限**されている。そのため 23 社を対象とする長文翻訳は、何の通知もなくランダムに切り詰められていた。プリフライトは `/api/v1/models/{modèle}/endpoints` を読み取り、出力上限が 8,000 tokens 未満の事業者、ステータスが低下している事業者、上限を申告していない事業者を除外して、残りを固定する。`allow_fallbacks: false` **なし**の `provider.only` は単なる優先指定にすぎないため、ルーターは除外した事業者へ再び振り分け、固定は無意味になる。上限を満たす事業者が一社もなければ、コマンドは停止する。それでも翻訳を続けることは、このプリフライトが防ぐために存在する無通知の切り詰めを受け入れることになる。

  - **推論は出力と同じ料金で課金され、多くのモデルでデフォルトで有効になっている。** `z-ai/glm-5.2` に同じリクエストを送り、応答を「OK」とした場合、**モデルのデフォルトでは completion が 107 tokens、推論を無効にすると 2 tokens** だった。推論が何ももたらさない翻訳では、各ファイルの各セグメントで 18 倍の差になる。そのため、デフォルトでは無効にしている。推論を必須とする **431 モデル中 288 モデル**（`reasoning.mandatory`）は `400 « Reasoning is mandatory for this endpoint and cannot be disabled »` を返すため、それらについてはプリフライトで許容される effort を読み取り、最低値を要求する（次項）。effort は推論が最初に消費する **`max_tokens` の割合**を割り当てるため、値を無作為に選ぶと、空白出力のリスクを軽減するどころか移動させるだけになる。

  - **推論を必須とするモデルには、許容される最低の effort を指定する。この判断は測定に基づいている。** 当初は、モデルに代わって推測しないよう、何も送信しない方針だった。カタログ上のデフォルトが `max` である `z-ai/glm-5.3-flash` で検証したところ、この方針では翻訳が終わる前に出力が **32,768 tokens で切り詰められ**、14 言語中 2 言語が失われた。上限枠を増やしても解決しない。effort はその一定割合を割り当てるため、枠とともに推論も増えるからだ。そのため provider はプリフライトで `supported_efforts` を読み取り、最低値を要求する。カタログに利用可能な値が示されていない場合は「指定なし」にフォールバックする。問題が起きた言語で反証テストを行ったところ、以前は予算枯渇で失敗していたが、現在は 9 分で完了し、構造もソースと同一になった。

  - **上流ホスティング事業者の障害に、その事業者名が表示されるようになった。** ルーターはこのケースを、`native_finish_reason` が null の `finish_reason=error` として正規化する。2 言語で 2 回測定し、いずれも正確に 750 秒だった。従来の汎用メッセージでは、文書や分割方法に不具合があるかのように調査させていたが、現在は障害が供給元側にあり、再試行だけで解決することが多いと伝える。

  - **出力が空の `finish_reason=length` は切り詰めではない。** 最初の有用な文字が生成される前に、推論が予算を使い切った状態である。測定では、有用な 148 tokens に対して推論が 15,850 tokens だった。この二つのケースでは必要な対処が正反対であり、前者ではセグメントサイズを小さくしても意味がない。メッセージは両者を明示的に区別する。ほかにも、測定に基づく二つのガードを追加した。上流ホスティング事業者が失敗した場合、ルーターは**エラーのみを含む本文とともに 200 を返す**（`choices[0]` はメッセージを隠す不透明な `TypeError` を送出していた）。また、context window をカタログから読み取って `MODEL_TOKEN_LIMITS` に設定する。`DEFAULT_TOKEN_LIMIT` は、4,095 tokens に制限された二つを含むカタログ上の 44 モデルで誤っている。

  - **`--model fournisseur/modèle` は必須であり、その形式はネットワークへ接続する前に検証される。** OpenRouter は単なる供給元ではない。選択には価格、ライセンス、データ処理が関わるため、ユーザーに代わって決めることはできない。slug はプリフライト URL に補間されるため、検証は単なる使いやすさへの配慮ではなく、パスの注入を防ぐガードである。両ルーターで共通する namespace 付き regex は `a/b/..` を受け入れるため、親セグメントを明示的に拒否する。`--eco` は効果がなく、その旨を通知する。

  - **三つの記述を修正し、そのうち一つは誤りだった。** `codex exec` に関する OpenAI の警告は、共有 runner に個人のセッションファイルを注入することを対象としたものであり、リポジトリが公開されていることを問題としていたわけではない。README、CLAUDE.md、コードでは文脈を誤って引用していた。OpenCode の認証情報の保存場所は 1.18.27 で変更され、`auth.json` ではなく `opencode.db` の `credential` テーブルになった。「ここでは決して読み取られない」という不変条件は正しかったが、保存場所の記載が古くなっていた。最後に、OpenCode のセクションでは、検証されていない経路を同等のものとして示さないようにした。Zen gateway と Ollama は最初から最後まで測定済みだが、GitHub Copilot、LM Studio、llama.cpp は未測定であり、README にもそのように明記した。

  - **大規模な測定と、README に推奨モデル一覧を追加。** 3 種類の文書セット――`--news` モードの密度の高いブログ記事、標準 Markdown のこの README、GitHub からそのまま取得した著名プロジェクト四つの README――を 14 言語に翻訳し、300 回を超える翻訳を実行した。表では、これまで混同されていた二つの観点を区別している。翻訳が**完了する**ことと、その**構造がソースと同一**であることだ。二つの高密度文書で一度も情報を失わなかったモデルは三つだった。`gemini-3.7-flash`、ChatGPT サブスクリプション経由の `gpt-5.6-sol`、OpenRouter 経由の `z-ai/glm-5.2` である。差異は、1～2 言語で一組の `**` が反映されなかったことだけだった。中心的な結論は、**差を生む要因は文書の密度であり、`--news` モードではない**ということだ。サブスクリプション経由の Grok はブログ記事では 14 回中 13 回失敗した一方、公開 README では 16 回中 14 回成功した。原因は長いセグメントでの脱落であり、反証テストで確認済みである。表には独自の注意書きもある。網羅的ではなく、特定時点の結果であり、所要時間は順位を示すものではない。適切な手順は、引き続き自身の文書で測定することである。

  - **数値を公開する前に構造比較器を修正した。非ラテン文字の表記で二つの偽陽性が発生していたためだ。** URL の直後に全角の閉じ括弧 `）` が続く場合、`)` で止まる regex では切り離されず、URL 自体は同一でも抽出文字列が異なっていた。また、フランス語では 5 行の引用が中国語では 3 行に収まるため、行単位のカウントが減少していた。両方の修正を反証テストで検証し、URL、セクション、inline code のいずれかを削除すれば引き続き検出されることを確認した。この修正がなければ、Gemini と Codex はそれぞれ 14 言語中 13 言語、12 言語ではなく、どちらも 11 言語として公開されていた。

  - **テスト**：新規ファイル `tests/test_openrouter_provider.py`（76 件のテスト）――モデルの検証と親セグメントの拒否、ホスティング事業者の固定（上限、ステータス、上限未申告、共通最小値）、`allow_fallbacks` が常に false であること、`mandatory` に応じた推論の無効化または維持、完全な出力契約（200 応答内のエラー、選択肢なし、空白出力と切り詰めの区別、異常な `finish_reason`、null の内容）、カタログへ接続不能な場合のプリフライトの fail-closed、slug の欠落と正常なホスティング事業者の不在、flag の排他性、ファイル名のラベル。全スイートで **502 件のテスト**。
  - **リファクタリング：4,253行の単一モジュールを、動作を一行も変更せずに複数のモジュールへ分割。** `src/aipmt/translate.py` を `config`、`markdown`、`segmentation`、`guards`、`placeholders`、`news`、`prompts`、`notes`、`naming`、`pipeline`、`cli`、およびサブパッケージ `providers/`（providerごとに1モジュール、基盤として `base`、解決とdispatch用に `registry`）へ分割した。各移動は、その正当性を機械的に証明するcommitになっている。検証ツールは、パッケージ内の全トップレベルノードのASTを基準snapshotと比較し、各symbolの配置、セキュリティマーカーが一字一句そのまま残っていること、未追跡ファイルがないことを確認する。この一時的なツールは次のversionで削除された。目に見える変更点は次のとおり。`aipmt.translate` は、以前のモジュールが `_` 接頭辞なしで公開していた64個の名前を、同一オブジェクトとして再公開するfaçadeになった（`__all__` がそのうち9個を担い、これがサポート対象のAPIである。残りは互換性alias）。また、`import *` が拾っていた依存関係および標準ライブラリの29個の名前は再exportしなくなった。ファイルの直接実行（`python src/aipmt/translate.py`）は廃止され、`aipmt` と `python -m aipmt` の2形式のみが引き続きサポートされる。公開関数の `__module__` は、それぞれの定義元モジュールを指す。SDKは `.env` の読み込み後にimportされるようになり、以前のように読み込み前には行われないが、既知の影響はない。427件のtestは識別子までそのまま維持され、実際に検証するモジュールへ移された。façade経由だった91件のpatchは、名前を参照するモジュールを直接対象とするようになった（そのうち2件はpatchがなくても成功することを測定済み）。7件のcontract testがfaçadeを固定し、gate用ツールは最初の移動より前に書き直されたため、検証をやめることで誤って成功することはない。具体的には、Lizardのscopeを下限付きのディレクトリ単位とし、構築済みparserからflagsを読み取り、パッケージ単位のcoverage下限を設け、`release.sh` が追跡対象モジュールを列挙する。
  - **修正（pull requestレビュー）**：OpenRouterは、`context_length` のないcatalog項目に128,000 tokensという既定値を測定値として記録せず、拒否するようになった。これまでは、それによって「一覧にないモデル」という警告まで消えていた。また、`finish_reason` がnull（文書化された型は `string | null`）の場合は、ホスティング事業者からの生の理由を正とし、`max_tokens` は `length` となる。選択肢自体にerrorが含まれる場合は、それに付随する部分的な内容を拒否し、正規化された上流障害と同じmessage、すなわちホスティング事業者の詳細、生の理由、助言をまとめて表示する。OpenCodeは、`part: null` eventに対して `AttributeError` ではなくcontract errorを返し、event行を解読できないJSONL streamについては、部分的なtextを受け入れず拒否する。3つのエージェント型CLIは、呼び出し中にagent processが `SIGTERM` を受け取った場合、そのagentのgroupを終了する。regen側の `timeout` ではagentが生き残ってquotaを消費し続けていた。また、groupの `SIGKILL` は常に猶予時間に従うため、正常終了するshimが孫processを生存させることはない。分割によって切り離されていた `# fmt: off` / `# fmt: on` の組を再結合した。`--reasoning_effort` のhelpには、それを利用する4つのproviderが明記される。
  - **修正（2回目のレビュー）**：OpenRouterへ要求する出力上限は、promptとsegmentが占めるcontext分を差し引くようになった。`context_length` は入力と補完の両方を含むが、catalog内の6モデルでは、入力用の余地がないままrequestが送信されていた。contextが短すぎる場合は、課金前に拒否される。エージェント型CLIの基盤は、POSIX process groupが存在しない環境では `terminate`、次いで `kill` にフォールバックし、`AttributeError` がtimeout guardをすり抜けて待機が長引くことを防ぐ。OpenCodeの `429` markerはsubstringではなく数値として検索されるようになった。以前は `err_84290b` のようなerror identifierでも発火し、90秒間back-offした末に結局失敗していた。最後に、非canonicalなOpenRouter endpointをpreflightで表示するようになった。projectの `.env` だけで設定でき、その後実際のkeyがそこへ送信されるためである。
  - **セキュリティ：projectの `.env` からAPI呼び出しを転送できないようにした。** `find_dotenv(usecwd=True)` は現在のディレクトリとその親からファイルを探す。このため、信頼できないディレクトリ階層、たとえばcloneしたばかりのリポジトリが、keyを一切知らなくても `OPENROUTER_BASE_URL`、`XAI_BASE_URL`、または `OPENAI_BASE_URL`（最後のものはSDK自身が読み取る）を配置でき、環境またはユーザー設定から得た本物のkeyが、その後第三者serverのauthorization headerへ送信される可能性があった。filterはリストではなくパターンに基づく。インストール済みSDKを調査した結果、12個のrouting variableが読み取られ、そのうち6個はAnthropic clientだけが使用していた。手作業の列挙では半分を見落としていただろう。そのため、project layerでは、`_BASE_URL`、`_API_BASE`、`_ENDPOINT` に該当するすべてのvariable、proxy、証明書store（制御下にある認証局を指定すると、interceptorを本物のserverと区別できなくなる）、さらに `XDG_CONFIG_HOME` と `APPDATA` を拒否する。後者を設定できると、どのファイルをuser layerとするか決定でき、filterを迂回できるためである。これらのvariableは、ユーザーが制御する2つのlayer、すなわちexport済み環境と `~/.config/aipmt/.env` からのみ受け入れる。さらにproject layerは補間なしで読み込まれる。`load_dotenv` は既定で `${VAR}` を展開するため、`NOM_ANODIN=${OPENAI_API_KEY}` を含む信頼できない `.env` が、本物のkeyをsubprocess向けパターンfilterで検知されない名前へコピーできた。それが `codex exec` の環境へ入り、明示した不変条件に違反していた。また、拒否時にはvariable名だけを表示する。`https://${CLE}@hôte/` 形式のURLでは、拒否しているにもかかわらず、補間されたkeyがlogへ漏れていたためである。拒否はstderrに出力され、対処方法も示される。企業用relayはユーザー設定で宣言する。
  - **修正：OpenRouterの出力枠を呼び出しごとに計算。** `context_length` は入力と補完の両方を含み、ラテン文字textを基準に調整した固定reserveでは上限を保証できない。`o200k_base` tokenizerで測定すると、16,000文字はフランス語で3,200 tokens、日本語で12,300 tokens、絵文字で17,500 tokensになる。そのためbudgetは実際に送信するtextから算出し、そのUTF-8 byte数で上方補正する。catalogで使用される各family、すなわちbyte単位BPEやbyte fallback付きSentencePieceなど、あらゆるbyte fusion tokenizerでは1 tokenが少なくとも1 byteに相当する。OpenRouterが未知の数十種類のtokenizerへrouteするこの場面で利用できる上方補正は、これだけである。平均比率はどれも適さなかった。追加面の表意文字では1 tokenあたり1.33 bytes、結合文字では1.00 byteまで下がるためである。これにより、入力と出力は構造上必ずwindow内に収まる。選択したモデルに対してsegmentが密すぎる場合は、課金後ではなく呼び出し前に拒否される。

- **1.12.0** Provider `--use_opencode`：open source agentのOpenCodeから、ユーザーが選択したproviderへ接続可能に。local model、アカウント不要の無料モデル、subscription、またはkeyに対応（2026-09-04）：

  - **従来の7つとは性質の異なる、8番目のprovider経路。** [OpenCode](https://opencode.ai)（MIT）はモデルproviderではなく、ユーザーがOpenCode自体に設定した接続先へ送る_routeur_である。接続先にはAPI key、subscription（GitHub Copilot、ChatGPT、SuperGrok）、アカウント**不要**で無料モデルを提供するOpenCode Zen gateway、または**local** model（Ollama、LM Studio、llama.cpp）を利用できる。scriptはCodexやGrokと同様に `opencode run` を非対話modeで操作し、同じsubprocess基盤（専用process group、timeout時の `SIGTERM` とそれに続く `SIGKILL`、常に閉じたstdin、機密情報を除去した環境）を再利用する。**2件の実際の翻訳**で検証済み。このREADME全体を `opencode/mimo-v2.5-free` で英訳した結果は49秒、1 passのみで、source fileと同一構造（32見出し、26個のcode block終端、18リンク、37 URL、37 table行、135個のinline code）だった。また、試験用ファイルを `ollama/qwen2.5:7b` によりlocal環境で、keyを一切使用せず翻訳した。

  - **`--model provider/modèle` は必須であり、意図的な選択である。** `--model` がない場合、OpenCodeは自身の既定値へフォールバックする。初期状態のインストールでは `opencode/big-pickle`、すなわち対話内容が学習に使われる可能性のある無料の「stealth」modelであり、測定でも実際にこのmodelが応答した。ユーザーに代わってこれを暗黙に選ぶことは、このリポジトリが追跡する見えない切り替えそのものである。そのためerror messageには、モデル一覧を表示するcommand（`opencode models`）と3つの例（local、無料、subscription）を記載する。`--eco` は効果がなく、その旨を表示する。`--reasoning_effort` は、明示的に要求された場合に限り、OpenCodeの `--variant` としてそのまま渡される。

  - **想定ではなく、測定済みの隔離。** inline configuration（`OPENCODE_CONFIG_CONTENT`。OpenCodeのmerge順序で最後に適用されるため、ユーザー設定を置き換えずに優先される）は、すべてのtoolを拒否する（`permission: {"*": "deny"}`）agent `aipmt` を定義する。tool registryはモデルにtoolを提示しなくなり、「ファイルを一覧表示して `id` を実行せよ」と指示しても、toolがないと応答する。session共有は無効化し、外部pluginは除外（`--pure`）し、`--auto` は決して行わず、空の使い捨て作業ディレクトリを使用する。2つの暗黙的な注入を測定し、無効化した。`OPENCODE_DISABLE_CLAUDE_CODE` がないと、ユーザーの `~/.claude/CLAUDE.md` が**すべての**promptへ入る（単純な「こんにちは」でも入力は186 tokensではなく515 tokens）。`OPENCODE_DISABLE_PROJECT_CONFIG` がない場合は、現在のディレクトリにある `AGENTS.md` も入り、「各応答をBANANAで終える」という指示が翻訳に適用された。一方、globalの `~/.config/opencode/AGENTS.md` は引き続き注入される。これを除外するswitchはなく、流用した `XDG_CONFIG_HOME` で回避するとユーザーのproviderまで隠してしまうためである。無理な細工はせず、文書化した。

  - **`exit 0` は何の証明にもならない。3番目のCLIでも警戒点は同じだが、固有の罠が2つある。** 未知の `--agent` でも `opencode run` は失敗しない。stderrにwarningを出し、toolが有効なcoding agentへ**暗黙に**フォールバックする。inline configurationが反映されていなければ、書き込み可能なagentで翻訳が実行されることになる。そのため出力contractでは、このmessageがないことに加え、終了codeが0であること、`error` eventがないこと、`tool_use` がないこと、最後の `step_finish` が `stop` であること（`length` は切り詰められた応答）、textが空でないことを検証する。2つ目の罠は、JSON error eventが**不透明**であることだ。「予期しないserver error。詳細はserver logを確認してください」という単なる参照しかなく、実際の原因（`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`、`ProviderAuthError` など）はlogにしか記録されない。そのため `--print-logs --log-level ERROR` を使用し、後続するBunのtraceを除外してstderrの `error="…"` fieldを読み取る。これにより未知のモデルは、原因を明示して1秒で失敗する。さらに `--title` により、余分なLLM呼び出しも回避する。これがないとOpenCodeは `small_model` に対する追加の1 turnでsession titleを生成する。

  - **secret：CodexおよびGrokと同じパターンfilterを使用するが、明示的な例外が1つある。** `OPENCODE_API_KEY` は維持する。これはOpenCode自身のkey（Zen gateway、Go subscription）であり、その名前によってOpenCode宛てである。つまりOpenCodeの `auth.json` に相当し、aipmtが管理したり課金したりするkeyではない。providerはOpenCode内（`opencode auth login`、`opencode.json`）で設定し、aipmtの `.env` では決して設定しないため、aipmtのkeyがsubprocessへ届くことはない。subscription型CLIとは異なり、CIでは拒否しない。runner上のAPI keyやself-hosted modelは正当な用途だからである。

  - **path traversal防止guardは、生の値ではなく補間後の値を検査するようになった。** `provider/modèle` には `/` が含まれ、1.10.0のguardはそれを拒否していた。`--model` がファイル名 `--include_model` に補間されるため、この判断自体は正しかった。ファイル名labelは、あらゆる補間より前に `/`、`\`、`:` を `-` へ置き換えるようになった（`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`。`:` はWindowsでは不正）。上流guardはこのlabelを検査する。`../../evil` はtarget配下の単純な名前 `doc-en-..-..-evil.md` となり、`..` だけが引き続き拒否され、`--target_lang ../x` も拒否される。`_ensure_within_directory` のscope guardは、変更のない第2層として残る。

  - **無料モデルとlocal modelの測定結果。** `opencode/mimo-v2.5-free` は1段落を16秒、このREADMEを49秒で翻訳する。`opencode/big-pickle` は200語に40秒かかり、2件を同時にrequestすると、それぞれ単独なら完了するにもかかわらず5分間応答がなかった。`opencode/nemotron-3.5-lightning-free` は3分間何も応答しなかった。このため `REGEN_PROVIDER=opencode` では `REGEN_MODEL` を必須とし、並列数を**2 jobs**とした。local側では、Ollamaはcontextを4,096 tokensに設定することが多い一方、segmentは最大16,000文字になるため、`PARAMETER num_ctx 32768` を指定した `Modelfile` が必要になる。品質はモデル次第であり、7B modelは試験用ファイルでlistの順序を逆転させ、code blockの終端を壊したが、gateway modelはすべて保持した。

  - **このリポジトリの翻訳では、有料APIを二度と使用しない。** `regen_translations.sh` は `.env` にkeyが残っているだけでOpenAI APIを使用し、Codexはopt-inにすぎなかった。このversionの準備中にも、まさにそれが起きた。ChatGPT subscriptionが従量課金を避けるために存在するにもかかわらず、28件の翻訳がOpenAI APIへ送られ、その後ヒンディー語版CHANGELOGがGemini APIへ送られた。keyの自動検出を廃止し、**Codexを既定値とし、品質重視の `gpt-5.6-sol` を使用する**。`openai`、`gemini`、`grok` では `REGEN_PROVIDER` に加えて `REGEN_ALLOW_PAID_API=1` が必要になる。これは判断時点で規則が確実に適用されるよう命名された例外である。未知の `REGEN_PROVIDER` はAPIへフォールバックせず失敗する。10件のtestで既定値、拒否、例外を固定した。このversionの28件の翻訳はCodexでやり直した。

  - **rate limit時のback-offを共通化**（`_retry_on_rate_limit`）。CodexとGrokのloopはlabel以外が同一で、3つ目を複製すると重複の閾値を超えるところだった。3つのCLI errorは共通の `_CliCallError` を継承する。3つのいずれかがこの継承から外れることをtestで禁止している。外れると共有loopがそのerrorを検知できなくなるためである。

  - **Test**：新規ファイル `tests/test_opencode_provider.py`（61 tests）。完全な出力contract、agentのフォールバック、logからの原因取得、重複text partの除去とsynthetic partの無視、process groupを終了するtimeout、429でのback-off、必須モデルとその検証、secretを含まないpreflight、binaryの解決、dispatchの配線、ファイル名label、path traversalの反証を検証する。`tests/test_review_hardening.py` はflagsの排他性とsecret不在の検証を新providerへ拡張する。gateは、文書化されたargparseの**22 flags**を必須とするようになった。全suiteは**382 tests**。

- **1.11.1** 文書修正：READMEに7つのprovider経路をようやく明記（2026-09-03）：
  - **1.11.0 の PyPI ページには「4つの API + Codex CLI」と記載されていました。** コードでは7つが提供されています。API 経由の OpenAI、Mistral、Claude、Gemini、Grok、そして従量課金なしのサブスクリプション経由の Codex（ChatGPT）と Grok です。2つの Grok モードが紹介文と _Multi-Provider_ の箇条書きから漏れており、14の翻訳でも同じ誤りが繰り返されていました。パッケージの長い説明はバージョンごとに固定されるため、公開ページを修正するには新しいバージョン番号が必要でした。これが今回のリリースの唯一の理由です。**コード変更はありません。**
  - `CLAUDE.md` は、リリースで導入された内容に合わせて更新されました。gate のカウンター（16、`--full` では17）、稼働中の11の workflow、`gh pr checks` では見えない2つの Sonar/Codacy カウンター（hotspots、Codacy API）、`ruff-format` による `# nosemgrep` の移動、OIDC 交換に必要な GitHub environments、そして _pending publisher_ は名前を予約しないという事実です。

- **1.11.0** PyPI で公開：リポジトリを clone せず、`pip install ai-powered-markdown-translator` の後にコマンド `aipmt`（2026-09-03）：

  - **単一ファイルのスクリプトがインストール可能なパッケージになりました。** `translate.py` はルートから `src/aipmt/translate.py` に移動し、console entry point `aipmt` と、それに相当する `python -m aipmt` が追加されました。貢献するには引き続きリポジトリの clone が必要です。テスト、28の翻訳、品質管理ツールはそこにあります。しかし、利用するだけなら不要になりました。

    - **import 名は `aipmt` であり、決して `translate` ではありません。** 実際に衝突し、しかも通知されないためです。PyPI パッケージ `translate`（v3.8.1、最終 upload は2026-07-06）は、同名のディレクトリをインストールします。venv で再現すると、ディレクトリが module より優先され、`translate.main` が見えなくなり、entry point は `AttributeError` で壊れます。それでも `pip check` は「No broken requirements found」と応答し、rc=0 になります。ユーザー側に単純な `pip install translate` があるだけで、有用な診断なしに CLI が壊れるところでした。実際の wheel による反証では、そのパッケージの上に `pip install translate` を配置しても、`aipmt --help` は前後とも rc=0 となり、両方の CLI が共存します。
    - **distribution 名は長く、コマンド名は短く。** `ai-powered-markdown-translator` により、PyPI 検索でパッケージを見つけられます。略語だけでは、すでにプロジェクトを知っている人にしか見つけられませんが、今回の公開はまさに新たに見つけてもらうことを目的としています。もっともらしい候補を2つ、検証のうえで除外しました。`ai-markdown-translator` は、同じ目的のツールによって2024年から npm で使用済みであり、このリポジトリより17か月先行しています。また、`aimt` は、同じ分野で稼働中のパッケージ `aim`（v3.29.1）と1文字しか違いません。長期的な混同を招く最悪の構成です。なお、手法上の落とし穴があります。`pypi.org/project/<nom>/` はどの名前でも200を返すため（bot 対策ページ）、信頼できるのは JSON API だけです。
    - **フラットなパッケージではなく `src/` layout。** フラットなパッケージなら、テスト内の6つの `sys.path.insert(..., "..")` を維持できました。しかし、それこそが問題です。それらはパッケージではなくソースツリーを import するため、パッケージングのあらゆる不具合を隠してしまいます。実際のコストは、置換ルールが1つ増えるだけです。

  - **キーを一度設定すれば、以後ずっと使えるようになりました。** インストール済みの CLI には永続的な設定が一切なく、環境変数と現在のディレクトリにある `.env` しか使えませんでした。確かに `find_dotenv` はシステムのルートまで遡るため、**ホームディレクトリ配下で作業している場合**は `~/.env` を見つけられましたが、それ以外の場所では何も見つかりませんでした。コマンドをどこから実行したかによって利用可否が決まる状態であり、設計上の選択ではありません。そこで、既存の2層の下に第3層として `~/.config/aipmt/.env` を追加しました。

    - **優先順位はコードで個別に指定されていません。** `load_dotenv` のデフォルト値である `override=False` から自然に決まります。各層は、前の層で空のままだった値だけを補います。このため、環境変数 → プロジェクトの `.env` → ユーザー設定という順になります。これは構造ではなく動作のテストで検証されています。2つの呼び出し順を逆にしても、第3層を削除しても、テストは失敗します。
    - **TOML ではなく `.env` 形式**を意図的に採用しました。`python-dotenv` はすでに依存関係に含まれ、その構文は15の README ですでに説明されており、同じファイルを両方の scope で使用できます。新しい依存関係も構文もありません。場所は、`XDG_CONFIG_HOME` が**絶対パス**の場合はそれに従い、Windows では `APPDATA` に従います。仕様上、相対値は無視する必要があります。そうしなければ、設定の場所が再び現在のディレクトリに左右されるためです。
    - **2つの選択肢を理由とともに除外しました。** システム keyring（`keyring`）は desktop 環境ではより安全ですが、headless 環境、つまり server、container、CI では機能しません。これは一括翻訳という用途そのものです。opt-in の候補としては適切ですが、デフォルトには不適切です。`--api-key` flag を使うと、キーが shell history に残り、`ps` でも見えてしまいます。
    - **キーがない場合、call trace は表示されなくなりました。** 以前は、`site-packages` を指す Python の stack trace と、「環境または .env」を挙げるだけで後者をどこに作成すべきか説明しないメッセージが表示されていました。現在は、3つの場所が正確なパスとともに列挙され、コマンドは終了コード2で終了します。安全網の範囲は**意図的に狭く**、設定フェーズだけを対象とする `except ValueError` です。実行全体を包むと、翻訳中に発生した本物の bug まで安心させるようなメッセージに変えてしまいます。まさに、このリポジトリが追跡している障害モードです。これを防ぐため、テストが `main()` のソースを読み取ります。

  - **修正 — ツールをインストールすると、ユーザーの `.env` が無視されていました。** 引数なしの `load_dotenv()` は現在のディレクトリからではなく、呼び出し元ファイル、つまり `site-packages` から遡ります。独自の `.env` を持つプロジェクトから実際の console entry point を起動して測定したところ、`find_dotenv()` は `''` を返してキーを読み込まない一方、`find_dotenv(usecwd=True)` はキーを見つけました。この bug は、ツールが clone 済みリポジトリからのみ実行されていた間は存在しませんでした。しかし公開後は必ず発生し、正しい設定にもかかわらず API キーが「見つからない」という症状だけが現れるところでした。

  - **3つの gate は、何も検証しなくなったにもかかわらず緑になるところでした。** 移動の前に意図的に強化しました。検出すべき変更の後に書かれた安全策では、何も証明できないためです。各 gate は元のリポジトリでは緑になり、移行済みのコピーでは赤になります。両方向を測定しています。

    - **Lizard は存在しないパスを何も言わず無視します**。rc=0 で、「0 file analyzed」となります。complexity gate は、158 functions / 2247 nloc から3 functions / 34 nloc に減り、出力は0 byte になるところでした。現在の scope は配列であり、各 entry の存在が検証されます。
    - **存在しない module に対する `coverage run --source=` は失敗しません**。stderr に警告が出るだけで、unittest でも `coverage xml` でも rc=0 となり、欠落した report がそのまま公開されます。statements は1453から141に減ります。ほぼ何も分析されていないために、プロジェクトが健全に見えるところでした。report は、合計値と測定対象で最大のファイルという2つの下限で保護されます。
    - **翻訳の鮮度を確認する probe は、呼び出し形式を構造的に認識できません**。argparse の flags を基準にしており、ファイル名の変更ではそこが変わらないためです。再現では、module を移動し、15の README が存在しないコマンドを引き続き説明していても、「古い翻訳なし」と判定されました。そこで、第7の section は options ではなく呼び出し形式を検証し、Lizard hook はスクリプトの実際の scope と照合されます。その key である `files:` は、一致しなくなっても pre-commit を失敗させず、hook をスキップさせるためです。

  - **`requires-python = ">=3.10"` は単なる主張ではなくなりました。** `sonar-project.properties` はすでに3.10～3.12を掲げていましたが、開発環境には3.12しかなく、一度も他のバージョンで実行されていませんでした。公開すれば表面化する内部矛盾です。現在は test workflow が3.10、3.11、3.12で suite を実行し、パッケージ自体をインストールすることで公開された version bounds も検証します。

  - **下限のみで、上限はありません。** `requirements.txt` はテスト済みの lock のまま、`[project.dependencies]` は公開 contract になります。lock の正確なバージョンを公開すれば、ほかのパッケージも利用している全ユーザーで競合が発生します。`<N+1` の上限もありません。上限を設定すると、major version の遅れがあるたびに release gate を失敗させる `check-deps-fresh.sh` と正面から矛盾するためです。この下限の組み合わせは resolve でき、反証用の `openai==1.0.0` は `ResolutionImpossible` で終了します。つまり、この検査は何でも受け入れるのではなく、正しく判別しています。さらに、`pyproject.toml` の version が CHANGELOG の version と異なることを禁止する guard もあります。PyPI では version 番号を再利用できないためです。

  - **新しい venv で端から端まで検証済みです**。約70 KB の wheel には `aipmt/*.py`、dist-info、license だけが含まれ、`aipmt --help` は22個の flags で rc=0、`python -m aipmt` は「usage: \_\_main\_\_.py」ではなく「usage: aipmt」を表示し、`pipx` によるインストールも機能します。そして何より、**任意のユーザーディレクトリから実際に fr→en 翻訳**を実行し、太字、リスト、inline code、link、URL が維持され、code block が翻訳されないことを確認しました。移行前からある318件のテストは、前後で byte 単位まで同一の identifier リストを保ったまま合格します。単なる「OK」ではなく、これによってテストが一つも無効化されていないことが証明されます。3層設定用の12件が追加され、合計330件です。

- **1.10.0** `--use_codex` provider（ChatGPT サブスクリプション枠）、SDK と model の更新、複数段落にまたがる news 引用の修正（2026-08-29）：

  - **security review — PR で設けられていたものの、すべての箇所では守られていなかった2つの安全策**：

    - **Codex の preflight は `.env` 全体を binary に渡していました。** `_codex_preflight` は **`env=` なしで** `subprocess.run` を呼び出していました。このため subprocess は `os.environ` 全体、つまり `load_dotenv` が読み込んだ `.env` の全内容を継承していました。計測機能を組み込んだ偽の binary で測定すると、**7つの secret**、すなわち6つの provider のキーと1つの `GITHUB_TOKEN` が preflight に到達していました。一方、対応する `_grok_preflight` は `env=_grok_env()` を正しく渡しており、到達した secret は**ゼロ**でした。これは PR 内部の不整合です。わずか数行先にある `_strip_secret_env` は、まさにこの invariant を維持するために存在します。`_codex_env_base()` を抽出して両方の経路で共有しました。修正後の測定では、どちらも secret は0件です。
    - **「`--deny` fail-closed」という性質は、実際に使われていた形式を対象としていませんでした。** コメントでは、未知の prefix を持つルールによって起動が拒否されることを、Grok の隔離全体の根拠としていました。`grok 1.0.13` で測定すると、この validation は**括弧付きの形式にしか存在しません**。`--deny 'CeciNestPasUnOutil(*)'` は起動を拒否します（「unknown tool prefix」）が、`--deny 'CeciNestPasUnOutil'` は無言で受け入れられます。ところが、`GROK_DENY_RULES` は裸の名前しか使っていませんでした。このため、xAI 側で tool 名が変更されると、OS sandbox がすでに適用されていない環境で、測定済みの唯一の隔離層が何の通知もなく消える可能性がありました。名前付きの8つのルールを `Prefix(*)` に変更し、それぞれが CLI に認識される prefix であることを検証しました。catch-all の `*` は、受理される唯一の形式である literal のままです。テストにより、未検証の形式へ戻ることを防ぎます。
    - **それ以外は安全であることを確認済みです**。command injection はなく（全箇所で list 形式を使用し、`shell=True` は一度も使用せず、document の内容は stdin または `--prompt-file` 経由）、安全でない deserialization もなく（`json.loads` のみを type guard 付きで使用）、path traversal の修正について7つの payload で bypass は見つからず、`--deny '*'` が CLI によって実際に適用されています（workdir 外の読み取りで `DENY_ENFORCED` を確認）。
    - また、上で追加された鮮度チェックは、それ自身の原則を迂回していました。PyPI query に失敗したパッケージを無言でスキップし、gate が緑になっていたためです。現在は実際に比較したパッケージ数を数え、coverage が不完全なら失敗します。

  - **依存関係を最新化し、遅れの再発を防ぐ2つの安全網を追加しました**：

    - **遅れは現実のもので、長期にわたっていました**。`openai` は2.54から**3.6.0**へ、`anthropic` は0.125から**1.2.0**へ、`certifi` は2024.8.30から**2026.7.22**へ更新されました。すべての provider 呼び出しで TLS を検証する root certificate store が2年間遅れていたことになります。原因も特定しました。**`.github/dependabot.yml` が存在しなかった**ためです。このファイルがなければ、GitHub は _security updates_ しか有効にせず、Dependabot が PR を提案するのは CVE の対象となった依存関係だけです。これにより、`urllib3` と `idna` は bump された一方で、2つの SDK が major version 1つ分遅れたままだった理由を説明できます。
    - **以前の検討で懸念されていたのとは異なり、2つの major version は競合せず共存します**。`openai` 3.x と `anthropic` 1.x は **`httpx2`** に移行しますが、`mistralai` と `google-genai` は引き続き `httpx<1` を使用します。ただし、これらは別々の distribution です。実際にインストールしたうえで、**7つすべての provider 経路を端から端までテスト**して確認しました。対象は OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI、Grok CLI で、各出力で inline code と link が維持されました。「HTTP stack を2つ持たない」というのは好みであって、blocker ではありませんでした。測定によって決着しています。
    - **`requirements.txt` は実際の環境を表していませんでした**。`google-auth`、`cryptography`、`opentelemetry` stack は作業用 venv にインストールされていましたが、一度も宣言されていませんでした。そのため、新規インストールではテスト対象の環境を再現できませんでした。逆に、`tokenizers`、`huggingface-hub`、`PyYAML` は、何からも import も要求もされていないのに記載されていました。`mistralai` 1.x の名残です。このファイルは、直接依存関係だけから構築した venv の完全な closure として再生成されました。新しい組み合わせに対して `pip-audit` が報告する既知の脆弱性はありません。
    - **`.github/dependabot.yml`**（新規）は、pip と github-actions の週次 version update を有効にします。minor と patch は1つの PR にまとめます。patch bump ごとに PR を作ると最終的に無視され、noise は更新の敵になるためです。**major は個別**にし、それぞれ実際の呼び出しによる validation を必須とします。
    - **`scripts/check-deps-fresh.sh`**（新規、gate に接続）は、遅れをプロジェクトの verdict に反映します。Dependabot は提案するだけで保証はせず、その PR は積み上がる可能性があります。major の遅れは失敗、minor は警告とします。常に赤い gate は最終的に無視されるためです。PyPI に接続できない場合、local では明示的に skip し、**CI では fail-closed** になります。実行されなかった検査は成功ではありません。修正前の正確な状態（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`）を検出し、minor の遅れでは警告だけになることを、両方向で確認しました。

  - **この PR の review から得られた修正** — 5つの review agent が diff を精査しました。以下の各点は修正前にすべて**測定によって再現**されており、そのうち2つは、この同じ version 内の前段で導入された regression でした。
    - **修正されたリグレッション — `_NEWS_CITATION_REGEX` で指数関数的なバックトラッキングが発生していました。** 複数段落対応の修正によって、繰り返し内に `(?:[ \t]*$|[ \t]+.*)` が導入されていました。`[ \t]+` と `.*` の間で空白をどちらが受け持つかが曖昧であり、この曖昧さが反復ごとに増幅していました。パターンに一致しない、完全に正当な Markdown インデントである `>   texte` 行を使って計測したところ、**14 行で 2,589 ms** かかっていたのに対し、修正後は 0.04 ms となり、行を 1 つ追加するごとに約 9 倍増加していました。`--news` モードでは、長く不適合な blockquote が 1 つあるだけで、原因を特定できないままジョブがタイムアウトするまで翻訳が停止していました。現在は、繰り返しが行全体をひとかたまりとして消費するため（`\n^>(?![ \t]*—).*`）、各反復で一致する方法は 1 通りしかありません。実際の 231 記事のコーパスで検証済みです。キャプチャの差異は**ゼロ**で、引用は同じ 423 件、複数段落の 14 本の本文もすべて引き続き拡張されています。
    - **2 つの provider flag を同時に指定すると、黙って従量課金されていました。** `--use_codex --use_mistral` は受け付けられていました。`_select_provider_client` は Mistral を最初に検査し、`_resolve_provider` は明示的な boolean を優先するため、どちらも Mistral に収束していました。そのため、ユーザーはサブスクリプション枠の利用を要求したにもかかわらず、何の警告もなく従量課金されていました。これはまさに、`--use_codex` が防ぐために存在する障害モードです。現在、6 個すべての provider flag が 1 つの `add_mutually_exclusive_group` を経由します。**動作変更**：これまで黙って受け付けられていた、2 つの provider を組み合わせたコマンドラインは、今後 `argument --use_mistral: not allowed with argument --use_codex` で失敗します。
    - **作業完了 gate は、その probe がクラッシュしたときにも正常判定になっていました。** `scripts/check-release-ready.sh` の 13 個の検査のうち 4 個は、「stdout を取得し、空なら結論を出す」というパターンに従い、終了コードを一度も確認していませんでした。例外（ファイル名の変更、`FileNotFoundError`）は stderr に書き込み、stdout を空のままにするため、検査は「問題なし」と結論づけていました。「`exit 0` だけでは何も証明できない」という罠が、それを防ぐために書かれたスクリプト内で再現されていたのです。現在は、helper `probe()` が終了コード 0 **かつ**終了 sentinel を必須とし、probe は基準の集合が空の場合には結論を出しません。空集合に対する assertion は常に真になるためです。実例として、上記の排他的グループを追加したことで provider flag が `*_group` オブジェクトを経由するようになり、旧 regex `parser\.add_argument\(` では一致しなくなりました。その結果、**21 個中 6 個の flag** が黙って検査範囲から外れていたにもかかわらず、gate は正常判定になっていました。
    - **secret scan は 6 つの provider のうち 4 つを見逃していました。** 文字クラス `[A-Za-z0-9]` はハイフンを除外しているため、`sk-proj-…`（現在の OpenAI 形式）と `sk-ant-api03-…` は 2 番目のハイフンで途切れ、`AIza…` は対象外でした。パターンを拡張し、`.secrets.baseline` は scan から除外しました。また、guard `.env` は index だけを見る `git diff --cached` を照会していたため、最悪のケースである**すでに commit 済み**の `.env` は一切表示されませんでした。現在は `git ls-files` を照会します。
    - **Codex の「token warm-up」は、実際には warm-up ではありませんでした。** 計測の結果、`codex login status` は `~/.codex/auth.json` に触れず、mtime とサイズも変化しません。その help には「ログイン状態を表示」と記載されています。それにもかかわらず、コメントでは token を「一度、逐次的に」更新し、1 回限りのローテーション token に対する同時 refresh のリスクを無効化すると説明していました。宣言されていた保護機能は存在しませんでした。現在、コメントはコードが実際に行うことを記述しており、本当の対策は引き続き `max_jobs=4` です。また、この検査は、以前無視していた `CODEX_BIN` も尊重するようになりました。`PATH` 内に `codex` がない端末では「未認証」として失敗し、誤解を招く診断になっていました。
    - **`.env` はサブシェル内で source されていました。** `detect_provider` はコマンド置換内で呼び出されるため、その export は呼び出し元に反映されませんでした。したがって、`.env` で定義された `GROK_BIN`、`GROK_HOME`、または `REGEN_MODEL` は、`main()` 内の読み取りから見えないままであり、正しい設定でも「Grok バイナリが見つからない」と結論づけていました。
    - **並行数が公称上限を 50% 超過していました。** guard が README/CHANGELOG のペアを起動した後に配置されていたため、`max_jobs=2` に対して計測されたピークは **3** でした。週次 quota が Chat/Imagine/Voice と共有され、計測もできない Grok では、スクリプト自身が課した上限すら守られていませんでした。一方、最終件数は表示されるだけで、28 と比較されることはなく、ファイルが欠けていても検知されませんでした。
    - **Grok の出力契約：`stopReason` が欠けている場合、今後は失敗となります。** 公表されている契約では `end_turn` が必須なのに、コードは「`end_turn` **または欠落**」を適用していました。このフィールドがない payload、または CLI の更新によってフィールド名が変更された payload では、guard が黙って no-op になっていました。また、`max_turn_requests` は rate limit に分類されなくなりました。これは turn budget の枯渇であり、再試行しても同じ結果が再現され、90 秒の待機コストがかかるためです。さらに、`quota` は rate limit marker から除外されました。`_codex_is_rate_limited` の docstring にすでに記載されていた理由を、Grok が適用していなかったためです。
    - **Gemini の cascade はモデルごとに memoize されるようになりました。** デフォルトモデルは `minimal` を拒否するにもかかわらず、各 segment で毎回そこから再開していました。そのため、通常経路でも segment ごとに 400 の往復コストが発生し、同じ警告が繰り返し表示されていました。何百回も繰り返される warning は読まれなくなり、やがて重要な情報を覆い隠すものになります。
    - **その他**：CI での拒否メッセージは Codex 用にハードコードされており、`--use_grok_cli` のユーザーを `XAI_API_KEY` ではなく `OPENAI_API_KEY` に誘導していました。`provider.capitalize()` は「Grok_cli」と「Openai」を表示していました。サブプロセス基盤のコメントは「shim」を両方の CLI に一般化していましたが、Grok バイナリはネイティブ ELF です。正しい理由は「自身のサブプロセスを spawn する agent」です。`subprocess` に関する 12 件の SAST finding は、根拠付きで `# nosec` / `# nosemgrep` として記録されています。`shell=True` を使用しない list 形式では injection は不可能であり、文書内容が argv を経由することもありません。
    - **agent サブプロセスに secret が一切渡らなくなりました。** 名前を列挙する deny-list が保護していたのは、**課金**に関する invariant（`OPENAI_API_KEY` なしの Codex、`XAI_API_KEY` なしの Grok）だけでした。計測の結果、**さらに 7 つの secret** が各サブプロセスに渡っていました。Anthropic、Mistral、Google、Gemini の key、もう一方の CLI の key、そして secret ではないものの通信先を変更する `OPENAI_BASE_URL` です。しかし、この 2 つの CLI は**agent**であり、Grok のものは多くの Linux 端末で適用可能な OS sandbox なしに動作します。現在は名前の列挙ではなく、**名前のパターン**（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`）によって filtering するため、このコードが認識していない、ユーザーが `.env` に追加した変数も対象になります。CLI に必要なものは 1 つもありません。認証情報は `~/.codex` と `~/.grok` にあり、環境変数には存在しません。これは、強化された環境で両方の provider をそれぞれ使用し、**実際の翻訳を正常に完了**させて検証済みです。
    - **テスト**：新しいファイル `tests/test_review_hardening.py`（21 テスト）で、provider flag の排他性、`stopReason` の契約、news regex の線形性、CI での拒否メッセージ、Gemini の memoization、サブプロセス環境に secret が一切存在しないことを固定しました。最後の assertion は**汎用的**であり、どの list にも名前がない key に対しても失敗します。一方、既存の除去テストは自身の定数を写しただけであり、自身の loop の故障以外は検出できませんでした。全 suite は **311 テスト**です。

  - **2 つの新しい Grok provider**：`--use_grok`（xAI API、key は `XAI_API_KEY`、従量課金）と `--use_grok_cli`（公式 Grok Build CLI、Grok サブスクリプションから消費。`--use_codex` と同じ仕組み）。
    - **API モード、約 40 行**：xAI endpoint は OpenAI 互換なので、client と `_call_openai` をそのまま再利用し、変更されるのは `base_url` だけです。必要だった変更は 1 つだけで、すべてに恩恵があります。OpenAI が `stop` を返す箇所で xAI が返す形式 `end_turn` を、`finish_reason` が受け付けるようになりました。モデル：`grok-4.6`（品質重視）と `grok-4.3`（eco）。なお、Grok の eco は依然としてこの repository で最も高価です。100 万 token あたり $1.25/$2.50 で、`mistral-small-latest` の $0.15/$0.60 と対照的です。この provider は価格ではなく、モデルの多様性を目的に選ぶものです。
    - **CLI モード**：Codex を踏襲していますが、実環境によって課された 4 つの相違点があります。prompt はファイル経由で渡します（`--prompt-file`。CLI は stdin を読まず、segment を argv に入れると `ps` に表示されます）。出力は stdout 上の単一 JSON オブジェクトです（JSONL でも `-o` ファイルでもありません）。サブスクリプションで利用可能なのは `grok-4.6` と `grok-4.5` だけです。また、sandbox は適用できません（後述）。サブプロセスの起動処理は Codex とともに `_codex_run_process` に共通化され、すでにテスト済みの Codex provider の他の部分には触れていません。
    - **計測により、`exit 0` だけでは何も証明できないことを確認**：未認証の場合、CLI は終了コード **0** で `{"type":"error","message":"Not signed in."}` を **stdout** に書き込みます。拒否や turn 超過でも同じ挙動です。したがって出力契約では、終了コード 0、error payload がないこと、`stopReason == end_turn`、空でないテキストという 4 条件を同時に満たす必要があります。preflight も同じ論理に従います。`grok models` はログアウト状態でも 0 で終了するため、stdout に「未認証」が含まれている場合にのみ判断できます。
    - **confinement：意図的に採用し、文書化した非対称性。** Codex は `--sandbox read-only` で動作しますが、Grok の sandbox は、`sudo` なしでは回避できない独立した 2 つのシステム上の理由により、多くの新しい Linux 端末で適用できません。Ubuntu 24.04 以降では AppArmor が非特権 user namespace を遮断し（`bwrap: setting up uid map: Permission denied`、Grok 以外でも再現）、`/run/podman` が `0700` の場合は container runtime socket の deny-list が失敗します（resolver が捕捉するのは `ErrorKind::NotFound` だけで、EACCES は fatal になります）。中心的な落とし穴は、適用できない**組み込み** profile が、黙って非 confinement 状態で起動することです。そのため、スクリプトはデフォルトで profile を一切要求せず、黙って fallback することもありません。stderr に警告を出します。保護は CLI の `--deny` rule に依存し、catch-all の `*` も含まれます。これは、計測上 _fail-closed_ となる唯一の layer です（未知の prefix を持つ rule があると起動を拒否します）。`GROK_TRANSLATE_SANDBOX=read-only` でこの保護を必須にでき、その場合、端末が要件を満たせなければ起動に失敗します。
    - **guardrail**：`XAI_API_KEY`、`GROK_API_KEY`、`GROK_SANDBOX` はサブプロセスの環境から削除されます。key があると従量課金に切り替わり、継承された `GROK_SANDBOX` は適用不能な profile を強制して、誤解を招くメッセージを表示するためです。MCP/hooks/skills/agents の switch は無効化され、`--disable-web-search`、`--no-subagents`、`--no-plan`、使い捨て workdir、CI での拒否、process group を終了する timeout、rate limit 時の back-off を使用します。`--max-turns` は 1 ではなく 6 に設定されています。counter は tool turn の後で増加するため、1 では出力が途中で切断されます。
    - **quota**：Grok の pool は週次で、**Chat、Imagine、Voice と共有**されます。また、Codex では `account/rateLimits/read` によって消費量を数値化できますが、Grok にはそれを公開する command がありません。そのため、`regen_translations.sh` は並行数を 2 に制限し、明示的に警告します。
    - **テスト**：新しいファイル `tests/test_grok_provider.py`（24 テスト）。全 suite は **290 テスト**です。
  - **修正されたバグ — 複数段落にわたる英語引用の一部しか保護されていませんでした（`--news` モード）**：`_NEWS_CITATION_REGEX` が引用本文として受け付けていたのは、`>` 行が**連続**して並ぶ場合だけでした。引用が複数の段落にまたがると（空の `>` 行で区切られると）、最後の段落だけが取得されて placeholder に置換され、それより前の段落は LLM に送られて翻訳されていました。これは、`--news` が保証するために存在するものと正反対の動作です。現在は繰り返しが内部の空の `>` 行を受け入れ、non-greedy になったため、最初に見つかった空行ではなく、斜体行の前にある空の `>` で停止します。
    - **実測された規模**：実際の 198 記事のコーパスでは、419 件の引用中 11 件が該当しました。リグレッションはありません。新しい regex が取得する引用数はまったく同じで、複数段落の本文だけが拡張されています（408 本の本文は同一、11 本が拡張）。帰属行 `> — …` が本文に取り込まれることも引き続きありません（lookahead を維持）。
    - **end-to-end の証明**：69 kB の記事を ja/ar に翻訳したところ、以前は日本語で `> GLM-5.3がオープンウェイト化。` とレンダリングされ、アラビア語でも同様に翻訳されていた引用の最初の段落が、今後は `> GLM-5.3 is now open-weight.` のまま維持されます。英語引用の行数は 9 から 10 に戻り、source と一致します。
    - なお、この不具合は後段の validator では検出されませんでした。validator は引用の存在を確認するだけで、完全性までは検査しないためです。
  - **デフォルト provider で実測された節約**：モデル名が `gpt-5` で始まると、`_openai_extra_kwargs` は `--eco` の場合も含めて `reasoning_effort="medium"` を送信していました。10 単語の文を翻訳する `gpt-5.4-mini` での計測結果は、`medium` では reasoning token が 45、出力 token が 65、`none` ではそれぞれ 0 と 14 でした。翻訳に reasoning は何の価値も付加せず、全ファイルの全 segment で課金されていました。デフォルトは `--eco` では `none`、それ以外では引き続き `medium` となります。CLI で明示的に渡された値は引き続き優先されます。`--reasoning_effort` は、`low`/`medium`/`high` に加えて `none` と `xhigh` も受け付けるようになりました。すべての値をすべてのモデルが受け付けるわけではありません。たとえば `minimal` は `gpt-5.4-mini` に拒否されますが、既存のパラメータなし retry がこのケースを処理します。
  - **SDK の更新と Gemini の移行**：`google-generativeai`（2025-11-30 にサポート終了、repository は archive 済み）は、統合 SDK **`google-genai`** に置き換えられました。`genai.Client(api_key=...)` の後に `client.models.generate_content(model=, contents=, config=)` を使用し、system prompt は segment に連結せず `system_instruction` で渡します。`mistralai` は **2.9.4** に更新され（import は `from mistralai.client import Mistral` になり、旧形式は `ImportError` を発生させることを wheel 内で確認済み）、`anthropic` は **0.125.0**、`openai` は **2.54.0** に更新されました。これらは `httpx2` への切り替え前の最終バージョンで、venv 内に 2 つの HTTP stack を共存させないためです。これに伴い、`httpx` 0.28.1 と `pydantic` 2.13.5 の固定も解除しました。
  - **文書ではなく実際のテストで発見された 2 つのリグレッション**：
    - `anthropic` ≥ 1.0 は、`max_tokens` から 10 分を超える可能性があると判断される non-streaming 呼び出しを client 側で拒否します（`ValueError: Streaming is required...`）。この guardrail は 0.34.2 には存在せず、`max_tokens=32768` を使用するすべての Claude 呼び出しを壊していました。明示的な `timeout`（`CLAUDE_TIMEOUT`、デフォルト 900 秒）で修正しました。これにより、完全な応答だけを使用する呼び出しを streaming に切り替えずに済みます。
    - `thinking_level="minimal"` が受け付けられるのは Gemini catalog の一部だけです。`gemini-3.1-flash-lite` は対応していますが、`gemini-3.7-flash` と `gemini-3.1-pro-preview` は 400 で拒否します。そのため、`_gemini_generate_with_fallback` は既存の OpenAI fallback と同様に、`minimal` → `low` → thinking_config なし、という cascade を使用します。最適化パラメータが原因で翻訳を失敗させてはならないためです。
  - **デフォルトモデルを刷新**し、それぞれ実際の呼び出しで検証しました。OpenAI は `gpt-5.5` → **`gpt-5.6-terra`**（28 件の batch で −60%）、`gpt-5.4-mini` → **`gpt-5.6-luna`**（−73%）。Claude は `claude-sonnet-4-6` → **`claude-sonnet-5`**（より安価で新しい）、`claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（日付なしの canonical ID）。Gemini は `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**、`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（stable version で、`3.5-flash-lite` より安価）です。
 Mistral は変更なしで、`mistral-large-latest` が引き続き4つの中で最もコストパフォーマンスに優れています。注意点：`gemini-3.1-pro-preview` より新しい Pro クラスの Gemini モデルは存在しません。2026年5月に発表された Gemini 3.5 Pro は結局リリースされず、3.5/3.6/3.7 系列は Flash のみです。
  - **Gemini 切り替え前の実測 A/B テスト**：`README.md` を `gemini-3.1-pro-preview`、続いて `gemini-3.7-flash` で日本語に翻訳しました。構造は完全に同一（リスト21個、コードブロック18個、HTML リンク13個、画像13個、すべての URL を保持）で、所要時間は **48秒に対して8秒**でした。この2つのモデルについて翻訳または非ラテン文字スクリプトを比較した公開ベンチマークが存在しないため、そうでなければ切り替えは単なる推測に基づくものになっていました。
  - **Claude 応答ブロックのフィルタリング**：`_call_claude` は種類をフィルタリングせずに `block.text for block in response.content` を行っていました。適応的推論モデル（Sonnet 5 以降）は `thinking` ブロックを挟み込みますが、これは `.text` ではなく `.thinking` を公開するため、最初のセグメントで不透明な `AttributeError` に遭遇すると翻訳が壊れていました。今後は `thinking`、`redacted_thinking`、`tool_use`、`tool_result` の各ブロックを除外し（テキストを含む未知の種類を許容できるよう、除外リスト方式）、テキストブロックがまったくない応答では明示的なエラーを発生させます。各呼び出しには `thinking={"type": "disabled"}` が渡されます。
  - **`MODEL_TOKEN_LIMITS` を再同期**：廃止日を過ぎたモデル（2026-07-31に廃止された `magistral-*` 系列、2026-06-01の `gemini-2.0-*`、2026-03-09の `gemini-3-pro-preview`、`claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）を削除しました。上限を修正：Mistral 128K → **256K**（Large 3 / Small 4 世代）、Gemini 1,000,000 → **1,048,576**（実際の入力上限）、`claude-opus-4-5` 200K → **1M**、`gpt-5.6-*` ファミリー 400K → **1.05M**。Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest`、`ministral-*` 系列を追加しました。注意点：これらの上限は引き続き目安であり、`translate()` によって分割処理は `min(16000, limite)` に制限されます。

  - **Provider `--use_codex`**：従量課金 API を呼び出す代わりに、公式 Codex CLI（`codex exec`）を非対話モードで操作する5番目の provider です。翻訳の利用量は、すでに支払い済みの ChatGPT サブスクリプション枠から差し引かれます。これは、この用途について OpenAI が文書化している唯一の方法です。プラン別の利用可否一覧では「Codex SDK、`codex exec`、およびスクリプト化可能なワークフロー」が Plus/Pro/Business/Enterprise で利用可能とされています。一方、`~/.codex/auth.json` のトークンでは API Platform の呼び出しを認証できません（また、このスクリプトがそれらを読み取ることもありません。認証と更新は引き続き CLI が管理します）。
  - **Codex バイナリを npm だけでなく pip でもインストール可能に**：`_resolve_codex_binary()` は、`CODEX_BIN`、次に `PATH`、その後に OpenAI が公開している公式 Python パッケージ **`openai-codex-cli-bin`**（`openai-codex` SDK の依存関係）内のバイナリを検索します。これにより、Python プロジェクトで `--use_codex` を利用するために npm のグローバルインストールは不要になりました。このパッケージは `requirements.txt` には追加していません。バイナリのサイズが約250 MBあり、任意利用の provider のために全ユーザーへ負担させることになるためです。エンドツーエンドで検証済みです。`PATH` に `codex` が存在しない状態でも、解決処理が同梱バイナリを見つけ、完全な翻訳が6秒で完了します。
  - **「サブスクリプションモード」の保証**：`OPENAI_API_KEY` と `CODEX_API_KEY` はサブプロセスの環境から削除されます。この保護がない場合、`.env` に存在するキーによって、目に見える通知なしに Codex が従量課金へ切り替わる可能性があります。まさにそれを避けるために、この provider が存在します。
  - **テストで固定された CLI の落とし穴**：
    - `codex exec` は、プロンプトを引数として渡した場合でも stdin を読み取ります。stdin を閉じないと、モデルを一度も呼び出さないままコマンドがタイムアウトまで待機します（再現結果：180秒後に終了コード124、出力0バイト）。そのため `communicate(input=...)` は必須です。
    - npm でインストールされた `codex` は、実際の Rust バイナリを `spawn` する Node の shim です。このバイナリは Python プロセスの**孫プロセス**であり、`subprocess.run(timeout=)` の `SIGKILL` 後も生き残ってクォータを消費し続ける可能性があります。このため `Popen(start_new_session=True)` と `os.killpg` を使用します。
    - CLI は `turn.failed` を出力していても終了コード0で終了する場合があります。戻り値だけでなく JSONL 出力（`--json`）も検査し、終了コード0で `-o` ファイルが存在しない場合は、空のセグメントを生成せず明示的なエラーを発生させます。
  - **レート制限時のバックオフ**：CLI は内部で再試行を一切行いません（`max_retries = 0`）。分類は部分文字列ではなく JSON ペイロードの構造（`status: 429` / `error.type`）に基づいて行います。「quota」という語は、回復可能な429と恒久的な `insufficient_quota` の両方に現れるためです。
  - **CI 保護**：`CI` または `GITHUB_ACTIONS` が定義されている場合、`--use_codex` は拒否されます。サブスクリプション認証は共有 runner での利用を想定しておらず、OpenAI も公開リポジトリでこのワークフローを明示的に非推奨としています。
  - **モデル**：`gpt-5.6-sol`（品質）と `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` ファミリーは CLI と API Platform で共通ですが、ChatGPT アカウントですべてを利用できるわけではありません。許可リストはサーバー側で適用され、ローカル検証は行われず、一般的でないモデルを指定すると警告が表示されます。Plus プランでは、5時間の時間枠あたり Sol が10～100メッセージなのに対し、Luna は250～2,000メッセージを利用できます。そのため、あらゆるバッチ処理では `--eco` が推奨モードです。
  - **修正済みのバグ — `regen_translations.sh` が完全に成功してもエラー終了していた問題**：`trap ... EXIT` は、`main()` の `local` 変数である `failed_log` を参照していましたが、trap の実行時点ではこの変数はすでに存在しません。`set -u` では `failed_log: unbound variable` が発生し、28件の翻訳がすべて正しいにもかかわらず、スクリプトが終了コード1で終了していました。これにより、再生成直後の最もコストが高い段階で `release.sh --auto`（`set -e`）が中断される可能性がありました。変数をグローバルに変更し、trap でその存在を確認するようにしました。有用な副作用として、従来このエラーに隠されていた実際の翻訳失敗が、終了時の要約で再び確認できるようになりました。
  - **`REGEN_MODEL`**：`regen_translations.sh` の新しい環境変数です。provider のデフォルトより優先して特定のモデルを強制します。たとえば `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol` を指定すると、処理量重視の `--eco` モデルではなく、サブスクリプション枠内の上位モデルで再生成できます。
  - **`regen_translations.sh`**：`REGEN_PROVIDER=codex` を明示的な選択によって利用可能にしました（ユーザーが知らないうちにサブスクリプション枠を消費しないよう、自動検出は一切行いません）。並列処理を開始する前に、トークンを逐次的に一度だけ更新します。Codex の更新トークンはローテーション方式かつ一度しか使えず、ジョブを並行実行すると `codex login` セッションが無効になるためです。また、並行数は4に引き下げられます。
  - **関連するリファクタリング**：チェーン全体に4つ目の真偽値を伝播させる代わりに、provider 名を返す `_resolve_provider()` を使用し、`_dispatch_provider_call` の引数を8個から6個に削減しました。最小限の `Namespace` で `translate(..., use_mistral=True)` を呼び出すテストを維持するため、明示的な真偽値は引き続き `args` より優先されます。
  - **テスト**：新しいファイル `tests/test_codex_provider.py`（48件のテスト）で、argv、除去済み環境、前置き禁止の契約、無言の失敗、タイムアウト／killpg、バックオフ、事前確認、provider 解決、Gemini の推論フォールバック、Claude ブロックのフィルタリング、複数段落にまたがるニュース引用を網羅しています。テストスイート全体は290件です。
  - **実環境での検証**：プロジェクトの `README.md` を Codex で**14言語**に翻訳した結果、参照翻訳と完全に同一の構造になりました（コードブロック14個、見出し24個、表25行、HTML リンク13個、画像13個、URL 19個、コードブロックは文字単位で完全一致、プレースホルダーの残留ゼロ）。`--news` モードで69 KBのニュース記事を処理したところ、`gpt-5.6-luna` と `gpt-5.6-sol` の両出力が、en/ja/ar のすべてで後段のアプリケーション検証を通過しました。`account/rateLimits/read` で測定した消費量は、`--eco` モードにおいてカウンターの丸めしきい値未満（5時間枠の0%）に収まりました。

- **1.9.2** 入れ子の括弧またはフランス語接頭辞を含むニュース帰属 URL の抽出を修正（2026-05-11）：

  - **修正済みのバグ**：`_protect_news_quotes` における帰属 URL の抽出では、正規表現 `re.search(r"\((.+?)\)", attribution)`（括弧内の最短一致キャプチャ）を使用していました。`(relayé par [@user sur X](https://x.com/.../123))` のような帰属表記（入れ子の括弧：外側の `(` と Markdown リンクの `]()`）では、最初に現れた `)` でキャプチャが終了し、フランス語接頭辞を含む切り詰められた文字列 `relayé par [@user sur X](https://x.com/.../123`（末尾の `)` なし）になっていました。その結果、`_validate_news_post` が翻訳後の出力からこの文字列を探して必ず失敗していました（理由は2つあり、`)` が切り詰められていることと、「relayé par」が `relayed by`／`weitergeleitet von`／……へ翻訳されることです）。low → medium → high → gpt-5.5 のフォールバック全体が通過できませんでした。
  - **修正**：正規表現を `re.search(r"\]\(([^)]+)\)", attribution)` に変更しました。Markdown リンクの `](url)` を明確に対象とし、フランス語接頭辞や切り詰めを含まない**純粋な URL のみ**をキャプチャします。これは翻訳中にプレースホルダー `#URL{N}#` によって不変に保たれます。問題となっていた次の2パターンに対応します：
    - `(relayé par [@account sur X](url))` — 入れ子の括弧
    - `via [@source](url)` または `selon [@author](url)` — 外側の括弧がないフランス語接頭辞
  - **テスト**：`test_silent_failure.py` の `TestNewsCitationExtraction` クラスに2件追加：
    - `test_extract_attribution_url_with_nested_parens`（Genspark CEO E2B のバグを正確に再現したケース）
    - `test_extract_attribution_url_with_french_prefix`（`via` を含む派生ケース）
  - **カバレッジ上の不足**：`check-editorial-coverage.py` は編集上の構文を検証しますが、translator で翻訳可能かどうかは検証しません。今後考えられる改善（v1.9.2 の対象外）は、dry-run で帰属情報の抽出をシミュレートし、公開**前**に危険なパターンを検出するチェックです。

- **1.9.1** 翻訳注記 marker 内の CTA ラベルの i18n を修正（2026-05-10）：

  - **修正済みのバグ**：翻訳済みファイルの先頭にある marker バナー内の CTA リンクラベル `[Voir le projet sur GitHub ↗]` が、`target_lang` に従わず、すべての対象言語で**フランス語のまま**残っていました。このラベルは LLM には一切渡されず（URL とリポジトリの slug を保持するため Python 側で組み立てられる）、翻訳フェーズで修正できませんでした。v1.9 で `marker` 形式を追加して以来の、気づきにくいリグレッションです。
  - **修正**：15言語を各言語のローカライズ済みラベルへ対応付ける新しい定数 `_VIEW_PROJECT_LABELS` を追加しました。`_translation_note_invariants(target_lang)` と `_assemble_translation_note_paragraphs(phrase, target_lang)` は、対象言語も伝播するようになりました。言語が不明な場合は `fr` にフォールバックします（安全策であり、KeyError は発生しません）。
  - **テスト**：`test_source_emits_three_paragraphs_repo_title_description_link` を調整（対象言語 `ja` → 期待される日本語ラベル）。新しいテストを2件追加：`test_source_link_label_localized_per_target_lang`（ラテン文字、表意文字、アブジャドを含む7言語でパラメーター化）と `test_source_link_label_falls_back_to_french_for_unknown_target`。合計：`test_translation_note_position.py` に40件のテスト（従来は38件）。
  - **後方互換性**：デフォルト値 `target_lang="fr"` を持つシグネチャのため、`args.target_lang` を指定しない外部のプログラム呼び出し元も変更なしで引き続き動作します。
- **1.9** サイレント障害の修正＋包括的な品質ツール群＋複数位置対応の翻訳注記（2026-05-07）：
  - **複数位置対応の翻訳注記＋「embed card」マーカー形式**：
    - 新しい CLI オプション（追加のみ、デフォルトは変更なし → **非破壊的**）：
      - `--note_position {top,bottom,both}`（デフォルト：`bottom`）：翻訳済みファイルの先頭、末尾、または両方に注記を配置します。
      - `--note_format {legacy,marker}`（デフォルト：`legacy`）：
        - `legacy` は v1.8 の動作（太字段落 `**…**`）を **バイト単位で完全に**再現します。
        - `marker` は、非表示の Markdown リンク参照定義（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）に続けて、「GitHub リポジトリ埋め込みカード」風の表示向けに構造化された **3 段落の blockquote** を出力します。内容は、インラインコード形式のプロジェクト名（`**\`ai-powered-markdown-translator\`\*\*`）、LLM によって翻訳された説明、および矢印を表示する CTA リンク（`[Voir le projet sur GitHub ↗](URL)`）です。ビルド時に remark プラグインで利用できます（jls42.org のブログ → プラグイン `remark-translation-banner` を参照）。
    - **LLM に決して送信されない不変要素**：リポジトリ名と GitHub URL は、説明文の翻訳後に Python 側で組み立てられます。LLM がスラッグ `ai-powered-markdown-translator` や `https://github.com/jls42/...` を見ることはないため、レンダラー、文字の大小、スキームが変更されることはありません。
    - **frontmatter 対応の挿入**：`top` または `both` モードでは、注記は YAML frontmatter を閉じる `---` ブロックの**後**に挿入されます（Astro Content Collections／gray-matter に対する安全性を確保）。ヘルパー `_split_frontmatter` はファイル先頭の `---\n…\n---\n` を検出し、その完全性を維持します。終了 fence のない未完の frontmatter では **`RuntimeError` を送出**し、誤った位置に注記を書き込む代わりに、そのファイルを `failed_files` に記録します。
    - **ホワイトリスト方式のモデル名 sanitizer**：`_sanitize_model` は `[A-Za-z0-9._:/-]` に含まれない文字をすべて `_` に置換し、空になった場合は `unknown` を使用します。Astro の remark プラグイン側のバリデーターと整合し、マーカー形式を壊す文字（空白、引用符、丸括弧、コンマなど）を無害化します。
    - **内部リファクタリング**：`_append_translation_note`（単一のモノリシック関数）→ 7 個の純粋ヘルパー（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。ビルダーとコンポーザーを分離しました（ビルダーは区切りなしの純粋なブロックを返し、コンポーザーが位置に応じて `\n\n` を適用）。本番処理とソース用ヘルパーは、同じ 3 段落アセンブラーを共有します。
    - **空行を維持する `_quote_lines`**：各行の先頭に `> ` を付け、空行は `>` のみの行に変換します。これにより mdast は、blockquote を改行付きの単一段落ではなく、3 つの独立した段落（タイトル／説明／リンク）として認識できます。
    - **適応型 `_build_translation_note_block`**：LLM が保持した段落数に応じて処理します（3＝完全なカード形式、2＝文＋リンク、1＝フォールバック）。Markdown リンク `](` が検出された場合、1 段落のフォールバックでは**リンクを `**...**` で囲まなくなりました**（リンクを `<strong>` で囲むと表示が不安定になるため）。
    - **後方互換性**：`_compose_with_notes` 側で `getattr(args, "note_position", "bottom")` と `getattr(args, "note_format", "legacy")` を使用します。これらの属性を持たない Namespace（既存テスト、外部からのプログラム呼び出し）も、変更なしで引き続き動作します。
  - **長文翻訳におけるサイレント障害の修正**：
    - すべてのプロバイダー（OpenAI、Mistral、Claude、Gemini）で翻訳後の言語を検証：決定論的レイヤー（ソースの抜粋がそのまま残っていないかを検出）＋確率論的レイヤー（`langdetect`）
    - `finish_reason`／`stop_reason` のホワイトリスト：ホワイトリスト外の状態（切り捨て、content_filter など）では必ず `RuntimeError` を送出
    - Claude の `max_tokens`：`4096` → `32768`（16k セグメントで潜在的な切り捨てを防止し、FR→JA/ZH/KO/AR/HI の文字体系間変換に余裕を確保）
    - 見出しを考慮した分割：セグメント後半の H2/H3 を優先し、各セグメントが意味的に完全なセクションから始まるようにしました
    - 非ゼロの終了コードまでエラーを伝播：`translate_markdown_file` は型付きステータス `success`／`failure`／`skipped` を返し、単一ファイル処理とバッチ処理のどちらでも、1 ファイル以上失敗した場合は `main()` が `sys.exit(1)` を返します
    - すべてのプロバイダーに空コンテンツガードを追加し、ソース／出力比率を検査（500 文字以上で 5% 未満なら拒否）、コード用プレースホルダーを検証（`#CODEBLOCK`／`#INLINECODE`）、LLM 処理後に正規化（見出しに連結された区切り／リンク）、`BadRequestError` を使わず `reasoning_effort` で再試行
    - 依存関係 `langdetect==1.0.9` を追加
  - **pre-commit 品質ツール群**（「完全な EurekAI 方式」、14 個のフック）：
    - Pre-commit：ruff（lint＋format）、shellcheck、prettier（md/yaml/json）、detect-secrets（4 個の API キーを保護）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（空白、EOF、大容量ファイル、shebang など）
    - Pre-push：mypy（段階的な緩和モード）、Opengrep SAST（translate.py＋scripts/）、pip-audit（初期レポートモード）、unittest discover（tests/＋scripts/tests/）
    - `./venv/bin/python` を使用するローカルラッパーを `scripts/` に配置
    - `scripts/audit_verdict.py`：11 個の unittest を備えた pip-audit JSON パーサー。jls42-astro のパーサーを Python に移植
    - 初期の ruff 違反 7 件を修正：B904（raise from）×2、B007（未使用の dirs）、C408（dict リテラル）、C419（リスト内包表記）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizard では `translate.py` を一時的に除外（CCN 21～47 の関数が 4 個あり、リファクタリングを予定）。scripts/ には厳格なゲートを適用
  - **SonarCloud＋包括的なカバレッジ**：
    - GitHub Actions ワークフロー `SonarCloud`（sonarcloud.yml＋sonar-project.properties）：push および pull-request ごとに分析し、`coverage.xml` でカバレッジを取得
    - README 上部に 11 個の SonarCloud バッジ（Quality Gate、Security／Reliability／Maintainability 評価、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）
    - `tests/test_silent_failure.py`（標準ライブラリの `unittest`）：サイレント障害のエラーチェーンを構成する 6 つの要素を網羅
    - `tests/test_orchestration.py`（テストを 79 件追加）：`translate.py` のオーケストレーション層を網羅（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` の TypeError＋BadRequestError フォールバック、o1 シリーズのプロンプト形式、`_validate_translation_output` の早期 return 分岐）
    - `scripts/tests/test_audit_verdict.py`：`main()`（stdin/stdout）と `if __name__ == "__main__"` ブロックを subprocess 経由でカバー
    - **新規コードのカバレッジ**：75.5% → 約 98%（translate.py 98%、scripts/audit_verdict.py 97%）
  - **テスト**：`tests/test_translation_note_position.py` は、位置×形式の組み合わせ（E2E の `marker+top|bottom|both` と `legacy+top|bottom|both` を含む）、複数行への接頭辞付与、バイト単位の後方互換性（固定リテラル）、sanitizer、frontmatter の分割（閉じられていない fence での例外送出を含む）、3 段落形式、2 段落フォールバック、1 段落＋Markdown リンクのガード、さらにタイトルと URL が LLM に決して送信されないことを検証する重要な安全策 `TestLLMPayloadExcludesInvariants` を網羅しています。**190 件のテストが成功**し、回帰は 0 件です。
  - ドキュメント：`README.md`（フランス語＋14 言語の翻訳）にバッジを追加、`CLAUDE.md`（pre-commit ワークフロー＋詳細な CI 監視）、28 件の翻訳を再生成
- **1.8** `--news` モード＋2026 年モデルへの更新（2026-03-17、タグ `v1.8`）：
  - デフォルトモデルを更新（2026 年 3 月）：
    - OpenAI 高品質：`gpt-5` → `gpt-5.4`
    - OpenAI 低コスト：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 高品質：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）、`gemini-3.1-pro-preview`（1M）のトークン上限を追加
  - 初期版 `--news` モード：プレースホルダー `#NEWSQUOTE\d+#` による英語引用文の保護、`LANG_FLAGS` のマッピング（15 言語）、対象言語ごとのフラグ管理
  - 復元前にニュース用プレースホルダーを検証（回帰：LLM がプレースホルダーを削除すると、引用のない出力が警告なしで生成されていました）
  - スクリプト `regen_translations.sh` を可搬化（絶対パスを使用し、pwd に依存しない）
  - README／CHANGELOG の言語バーにフランス語リンクを追加し、28 件の翻訳を再生成
- **1.7** 新機能：
  - 翻訳時に元のファイル名を保持する `--keep_filename` オプション
  - API キーを自動的に読み込む `.env` ファイルをサポート
  - **インラインコードの保持**：翻訳中にバッククォート（`` `...` ``）が保護されるようになりました
  - システムプロンプトを改善：
    - YAML frontmatter 内の引用符処理を改善
    - テンプレート変数 `{variable}` を保護
    - 要求されていない翻訳者注記を禁止
  - 364 ファイルでのテストに成功（jls42.org ブログの移行）
- **1.6** 新機能：
  - 翻訳用 Google Gemini API をサポート（`--use_gemini`）
  - 2026 年のデフォルトモデルに更新：
    - OpenAI：`gpt-5`（高品質）、`gpt-5-mini`（低コスト）
    - Claude：`claude-sonnet-4-5`（高品質）、`claude-haiku-4-5`（低コスト）
    - Gemini：`gemini-3-pro-preview`（高品質）、`gemini-3-flash-preview`（低コスト）
  - より高速で低コストなモデルを使用する低コストモード（`--eco`）
  - ディレクトリを走査せずに単一ファイルを翻訳（`--file`）
  - 新しい簡略化された命名パターン：`{base}-{lang}.md`
  - モデル名を含む従来の形式を保持する `--include_model` オプション
  - 一覧にないモデルをデフォルトのトークン上限（128k）でサポート
  - README を 14 言語に翻訳
- **1.5** 改善：
  - **API キーとデフォルトモデルの更新：**
    - **OpenAI：** `DEFAULT_MODEL_OPENAI` から `"gpt-4o"` に更新。
    - **Mistral AI：** `DEFAULT_MODEL_MISTRAL` から `"mistral-large-latest"` に更新。
    - **Anthropic Claude：** `DEFAULT_ANTHROPIC_API_KEY` を追加し、`DEFAULT_MODEL_CLAUDE` から `"claude-3-5-sonnet-20240620"` に更新。
  - **翻訳プロンプトの最適化：**
    - 直接翻訳と翻訳注記用のプロンプトをより明確かつ効率的にし、メタデータや特定の書式要素を保持するための詳細な指示を追加しました。
  - **コードのリファクタリング：**
    - Mistral AI クライアントの初期化で `MistralClient` を `Mistral` クラスに置き換えました。
    - 可読性と保守性を高めるため、import を再編成しました。
    - 翻訳時に元の書式を保持できるよう、テキストの分割とコードブロックの処理を改善しました。
  - **出力ファイルの管理：**
    - 出力ファイル名内のモデル名と言語の順序を入れ替え（例：`f"{base}-{args.target_lang}-{args.model}.md"`）、翻訳の整理と検索を容易にしました。
  - **その他の改善：**
    - 不要な空行を削除してコードを整理しました。
    - スクリプトの構造と可読性を高めるため、細かな調整を行いました。
- **1.4** 新機能：
  - 翻訳用 Anthropic Claude API をサポート
  - 明確性と効率性を高めるためプロンプトを最適化
  - コードの保守性を高めるための細かな調整
- **1.3** 改善と新機能：
  - コードブロックの処理を改善
  - 出力ファイルの管理を改善
  - 既存ファイルの検出を改善
  - 翻訳を強制する `--force` オプション
  - 出力ファイル名内のモデル名と言語の順序を入れ替え
- **1.2** changelog を修正
- **1.1** Mistral AI API のサポートを追加
- **1.0** 初期バージョン - OpenAI API をサポート

**gpt-5.6-solを使用してフランス語から日本語に翻訳された記事。**
