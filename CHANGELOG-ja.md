### 変更履歴

🌍 [フランス語](CHANGELOG.md) | [英語](CHANGELOG-en.md) | [スペイン語](CHANGELOG-es.md) | [中国語](CHANGELOG-zh.md) | [ドイツ語](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [韓国語](CHANGELOG-ko.md) | [アラビア語](CHANGELOG-ar.md) | [ヒンディー語](CHANGELOG-hi.md) | [イタリア語](CHANGELOG-it.md) | [オランダ語](CHANGELOG-nl.md) | [ポーランド語](CHANGELOG-pl.md) | [ポルトガル語](CHANGELOG-pt.md) | [ルーマニア語](CHANGELOG-ro.md) | [スウェーデン語](CHANGELOG-sv.md)

- **1.13.0** プロバイダー `--use_openrouter`：中国のオープンモデルを含む約430モデルへの有料ルーター（2026-09-05）：

  - **8番目と同時に提供される、9番目のプロバイダー経路。** 1.12.0 は PyPI では公開されませんでした。OpenCode と OpenRouter の2つのルーターは同時にリリースされます。[OpenRouter](https://openrouter.ai) は、ここでは他のどのプロバイダーも提供していないモデル（Kimi、Qwen、DeepSeek、Z.ai）へ、従量課金される単一のクレジットと1つのキーでアクセスできるようにします。エンドポイントは OpenAI 互換であるため、クライアントは xAI と同じです。**このプロバイダーを区別するすべての要素はプリフライトに集約されており、その各ルールは API での測定に基づいています。**

  - **同じモデルが異なる上限を持つ数十のホストから提供されますが、ルーティングはその違いを認識しません。** 測定結果：`z-ai/glm-5.2` には33ホスト、`z-ai/glm-5.3-flash` には23ホストがあり、そのうち1つは**出力2,048トークン**に制限されています。そのため、23のうち無作為に選ばれたホスト上で長文翻訳が実行されると、何の通知もなく途中で切れていました。プリフライトは `/api/v1/models/{modèle}/endpoints` を読み、出力上限が8,000トークン未満のホスト、状態が劣化しているホスト、上限を宣言していないホストを除外し、残りを固定します。`allow_fallbacks: false` **なしの** `provider.only` は単なる優先指定にすぎません。ルーターは除外したホストへフォールバックするため、固定には何の意味もなくなります。上限を満たすホストが1つもない場合、コマンドは停止します。それでも翻訳を続けることは、このプリフライトが防ぐために存在する無言の切り捨てを容認することになるからです。

  - **推論は出力料金で課金され、多くのモデルでデフォルトで有効です。** `z-ai/glm-5.2` に同じリクエストを送り、応答を「OK」とした場合、**モデルのデフォルトでは完了に107トークン、推論を無効にすると2トークン**でした。推論が何の役にも立たない翻訳では、各ファイルの各セグメントで18倍の差になります。そのため、デフォルトでは無効にしています。推論を必須とする**431モデル中288モデル**（`reasoning.mandatory`）は `400 « Reasoning is mandatory for this endpoint and cannot be disabled »` を返します。これらには推測した effort を送らず、何も送りません。effort は推論が最初に消費する **`max_tokens` の割合**を割り当てるため、無作為に選んだ値では、空白ページになるリスクを減らすのではなく移動させるだけだからです。

  - **推論を必須とするモデルには、そのモデルが受け入れる最小の effort を送ります。これは測定に基づく判断です。** 当初はモデルに代わって推測しないよう、何も送らない方針でした。カタログのデフォルトが `max` である `z-ai/glm-5.3-flash` で検証すると、この方針では翻訳が終わる前に出力が**32,768トークンで切り捨てられ**、14言語中2言語が失われました。上限枠を増やしても結果は変わりません。effort はその一定割合を割り当て、上限枠とともに推論も増えるからです。そのため、プロバイダーはプリフライトで `supported_efforts` を読み、最小値を要求します。カタログに利用可能な値が示されていない場合は「何も送らない」にフォールバックします。問題が発生した言語での対照試験では、以前は予算の枯渇によって失敗していましたが、現在はソースと同一の構造を保ったまま9分で完了します。

  - **上流ホストの障害について、今ではその原因を明示します。** ルーターは、この事象を `native_finish_reason` が null の `finish_reason=error` として正規化します。2つの言語で2回測定したところ、いずれも正確に750秒でした。従来の一般的なメッセージでは、文書や分割方法の不具合を探すよう誘導していましたが、現在は障害がプロバイダー側にあり、再試行だけで解決する場合が多いことを伝えます。

  - **空の出力を伴う `finish_reason=length` は切り捨てではありません。** これは、最初の有用な文字が出力される前に推論が予算を使い果たした状態です。測定では、有用な148トークンに対して推論に15,850トークンが使われました。この2つの事象には正反対の対応が必要です。前者ではセグメントのサイズを小さくしても役に立ちません。メッセージでは両者を明確に区別しています。さらに、測定結果に基づく2つの保護機構があります。上流ホストが失敗した場合、ルーターが**エラーだけを含む本文とともに200を返す**ことがあり（`choices[0]` はメッセージを隠す不透明な `TypeError` を送出していました）、またコンテキストウィンドウをカタログから読み取って `MODEL_TOKEN_LIMITS` に設定します。カタログ内の44モデルでは `DEFAULT_TOKEN_LIMIT` が誤りであり、そのうち2モデルは4,095トークンに制限されています。

  - **`--model fournisseur/modèle` は必須で、その形式はネットワークアクセス前に検証されます。** OpenRouter は単なる供給元ではありません。選択は価格、ライセンス、データ処理に関わるため、ユーザーに代わって決定することはできません。slug はプリフライト URL に埋め込まれるため、検証は使いやすさのための配慮ではなく、パスの挿入を防ぐ保護機構です。2つのルーターで共通の名前空間付き正規表現は `a/b/..` を受け入れるため、親セグメントは明示的に拒否されます。`--eco` は効果がなく、その旨を通知します。

  - **3つの記述を修正し、そのうち1つは誤りでした。** `codex exec` に関する OpenAI の警告は、公開リポジトリであることではなく、共有 runner に個人用セッションファイルを注入することを対象としていました。README、CLAUDE.md、コードでは逆の意味で引用されていました。OpenCode の認証情報の場所は 1.18.27 で変更され、`auth.json` ではなく `opencode.db` の `credential` テーブルになりました。「ここでは決して読み取られない」という不変条件は正しいままでしたが、参照先が古くなっていました。最後に、OpenCode の節では、検証されていない経路を同等のものとして提示しないようにしました。Zen ゲートウェイと Ollama はエンドツーエンドで測定済みですが、GitHub Copilot、LM Studio、llama.cpp は未測定であり、README でもそのように記載しています。

  - **測定キャンペーンと、README の推奨モデル一覧表。** 3種類の文書セットに対して、14言語への翻訳を300件以上実行しました。`--news` モードの高密度なブログ記事、標準 Markdown のこの README、そして GitHub からそのまま取得した著名プロジェクトの4つの README です。表では、これまで混同されていた2つの点を区別しています。翻訳が**完了する**ことと、その**構造がソースと同一である**ことです。2つの高密度文書で一度も情報を失わなかったモデルは3つありました。`gemini-3.7-flash`、ChatGPT サブスクリプションの `gpt-5.6-sol`、OpenRouter 経由の `z-ai/glm-5.2` です。唯一の差異は、1つか2つの言語で一対の `**` が再現されなかったことです。中心的な知見は、**判別要因は文書の密度であり、`--news` モードではない**ということです。サブスクリプション版 Grok はブログ記事では14回中13回失敗した一方、公開 README では16回中14回成功しました。原因は長いセグメントでの脱落であり、対照試験でも確認されています。表には独自の注意書きがあります。網羅的ではなく、日付時点の情報であり、所要時間は順位を示すものではありません。最善の方法は、引き続き自分の文書で測定することです。

  - **構造比較ツールは、非ラテン文字で2件の偽陽性を生じていたため、数値を公開する前に修正しました。** 全角閉じ括弧が後ろに続く URL `）` は、`)` で止まる正規表現では区切られず、URL は同一でも抽出された文字列が異なっていました。また、フランス語で5行の引用が中国語では3行に収まることで、行単位の件数が減少していました。両方の修正は対照試験で検証されており、URL、セクション、インラインコードを削除すれば、引き続き検出されます。この修正がなければ、Gemini と Codex は14言語中それぞれ13言語と12言語ではなく、11言語として公開されていたはずです。

  - **テスト**：新しいファイル `tests/test_openrouter_provider.py`（39テスト）— モデルの検証と親セグメントの拒否、ホストの固定（上限、状態、未宣言の上限、共通の最小値）、`allow_fallbacks` が常に false であること、`mandatory` に応じた推論の無効化または維持、完全な出力契約（200内のエラー、選択肢なし、空白ページと切り捨ての区別、異常な `finish_reason`、null の内容）、カタログに到達できない場合のプリフライトのフェイルクローズ、slug の欠落と正常なホストの不在、フラグの排他性、ファイル名ラベル。全テストスイートは**427テスト**です。

- **1.12.0** プロバイダー `--use_opencode`：オープンソースのエージェント OpenCode から任意のプロバイダーへ—ローカルモデル、アカウント不要の無料モデル、サブスクリプション、またはキー（2026-09-04）：

  - **先行する7つとは性質が異なる、8番目のプロバイダー経路。** [OpenCode](https://opencode.ai)（MIT）はモデルのプロバイダーではなく、ユーザーが OpenCode 自体に設定したものへの_ルーター_です。API キー、サブスクリプション（GitHub Copilot、ChatGPT、SuperGrok）、**アカウント不要**の無料モデルを提供する OpenCode Zen ゲートウェイ、または**ローカル**モデル（Ollama、LM Studio、llama.cpp）を利用できます。スクリプトは Codex や Grok と同様に `opencode run` を非対話モードで制御し、同じサブプロセス基盤（専用プロセスグループ、タイムアウト時の `SIGTERM` とそれに続く `SIGKILL`、常に閉じられた stdin、不要なものを除去した環境）を再利用します。**2件の実際の翻訳**で検証済みです。`opencode/mimo-v2.5-free` によるこの README 全体の英訳は49秒、1回の処理で完了し、ソースファイルと同一の構造（32見出し、26コード終了、18リンク、37 URL、37表行、135インラインコード）を維持しました。また、`ollama/qwen2.5:7b` によるテストファイルの翻訳は、キーを一切使わずローカルで実行しました。

  - **`--model provider/modèle` は必須であり、これは意図的な選択です。** `--model` がなければ、OpenCode は自身のデフォルトへフォールバックします。新規インストール時のデフォルトは `opencode/big-pickle` であり、やり取りがトレーニングに利用される可能性がある無料の「stealth」モデルです。測定でも、実際にこのモデルが応答しました。ユーザーに代わってこれを無言で選択することは、このリポジトリが追跡している見えない切り替えそのものです。そのため、エラーメッセージにはモデルを一覧表示するコマンド（`opencode models`）と3つの例（ローカル、無料、サブスクリプション）を記載しています。`--eco` は効果がなく、その旨を通知します。`--reasoning_effort` は、明示的に要求された場合に限り、OpenCode の `--variant` としてそのまま渡されます。

  - **推測ではなく、測定された隔離。** インライン設定（`OPENCODE_CONFIG_CONTENT`。OpenCode のマージ順で最後に位置するため、ユーザー設定を置換せずに優先されます）は、すべてのツールを拒否する（`permission: {"*": "deny"}`）エージェント `aipmt` を定義します。レジストリはモデルにツールを提示すらしなくなるため、「ファイルを一覧表示して `id` を実行する」よう命じても、モデルはツールがないと応答します。セッション共有は無効、外部プラグインは除外（`--pure`）、`--auto` は決して使わず、作業ディレクトリは使い捨てで空です。2つの無言の注入を測定し、遮断しました。`OPENCODE_DISABLE_CLAUDE_CODE` がなければ、ユーザーの `~/.claude/CLAUDE.md` が**すべての**プロンプトに入ります（単純な「こんにちは」でも入力が186トークンではなく515トークン）。`OPENCODE_DISABLE_PROJECT_CONFIG` がなければ、現在のディレクトリの `AGENTS.md` も入ります。「すべての応答を BANANA で終える」という指示が翻訳に適用されました。一方、グローバルな `~/.config/opencode/AGENTS.md` は引き続き注入されます。これを除外する切り替えはなく、転用した `XDG_CONFIG_HOME` で回避すると、ユーザーのプロバイダーまで隠してしまいます。そのため、場当たり的な回避策ではなく、文書化しました。

  - **`exit 0` は何も証明しません。3つ目の CLI でも同じ慎重さが必要であり、これ固有の落とし穴が2つあります。** 未知の `--agent` でも `opencode run` は失敗しません。stderr に警告を出し、ツールが有効なコーディングエージェントへ**無言で**フォールバックします。インライン設定が反映されなければ、書き込み可能なエージェントで翻訳が実行されることになります。そのため、出力契約では、このメッセージが存在しないことに加えて、終了コードが0であること、`error` イベントがないこと、`tool_use` がないこと、最後の `step_finish` が `stop` であること（`length` は切り捨てられた応答です）、テキストが空でないことを検証します。2つ目の落とし穴は、エラーの JSON イベントが**不透明**であることです。「予期しないサーバーエラーです。詳細はサーバーログを確認してください。」という単なる参照付きのメッセージであり、実際の原因（`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`、`ProviderAuthError` など）はログにしかありません。そのため、`--print-logs --log-level ERROR` と、後続の Bun トレースを除いた stderr の `error="…"` フィールドの読み取りが必要です。これにより、未知のモデルは原因を明示して1秒で失敗します。さらに `--title` は、余計な LLM 呼び出しを防ぎます。これがない場合、OpenCode は `small_model` への追加の1ターンでセッションタイトルを生成します。

  - **シークレット：Codex および Grok と同じパターンによるフィルタリングを行いますが、名前を指定した例外が1つあります。** `OPENCODE_API_KEY` は保持されます。これは OpenCode 自体のキー（Zen ゲートウェイ、Go サブスクリプション）であり、その名前を持つ OpenCode に渡されるものです。OpenCode の `auth.json` に相当し、aipmt が管理または課金できるキーではありません。プロバイダーは OpenCode 内（`opencode auth login`、`opencode.json`）で設定され、aipmt の `.env` では設定されません。aipmt のキーがサブプロセスへ届くことはありません。サブスクリプション型 CLI とは異なり、CI では拒否しません。runner 上の API キーやセルフホストモデルは正当な用途だからです。

  - **トラバーサル防止機構は、元の値ではなく埋め込み後の値を検査するようになりました。** `provider/modèle` には `/` が含まれており、1.10.0 の保護機構はこれを拒否していました。`--model` がファイル名 `--include_model` に埋め込まれていたため、その判断は正当でした。ファイル名ラベルは、埋め込み前に `/`、`\`、`:` を `-` に置換するようになりました（`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`。`:` は Windows では不正です）。上流の保護機構はこのラベルを検査します。`../../evil` は対象配下の単純な名前 `doc-en-..-..-evil.md` になり、`..` 単独の場合は引き続き拒否され、`--target_lang ../x` も拒否されます。スコープ保護機構 `_ensure_within_directory` は第2層として変更なく維持されます。

  - **無料モデルとローカルモデルについて測定した結果。** `opencode/mimo-v2.5-free` は1段落を16秒、この README を49秒で翻訳します。`opencode/big-pickle` は200語に40秒かかり、単独ではそれぞれ完了する一方、2件の同時リクエストでは5分間応答がありませんでした。`opencode/nemotron-3.5-lightning-free` は3分間何も応答しませんでした。そのため、`REGEN_PROVIDER=opencode` では `REGEN_MODEL` が必須で、並列実行は**2ジョブ**です。ローカル側では、セグメントが最大16,000文字であるのに対して、Ollama のコンテキストは4,096トークンに設定されていることがよくあります。そのため、`PARAMETER num_ctx 32768` を指定した `Modelfile` が必要であり、品質はモデル次第です。テストファイルでは、7B モデルがリストの順序を逆にし、コードブロックの終了を壊しましたが、ゲートウェイのモデルはすべてを保持しました。

  - **このリポジトリの翻訳では、有料 API を一切使用しなくなりました。** `regen_translations.sh` は、`.env` にキーが残っていると直ちに OpenAI API を使用し、Codex はオプトインとしてしか扱っていませんでした。このバージョンの準備中に、まさにそれが起きました。ChatGPT サブスクリプションは従量課金を避けるために存在するにもかかわらず、28件の翻訳が OpenAI API に送られ、その後ヒンディー語の CHANGELOG が Gemini API に送られました。キーの自動検出は廃止されました。**品質モデルの `gpt-5.6-sol` を使用する Codex がデフォルト**です。`openai`、`gemini`、`grok` では、`REGEN_PROVIDER` に加えて `REGEN_ALLOW_PAID_API=1` が必要です。これは、判断時にルールが確実に適用されるよう名前を付けた例外です。未知の `REGEN_PROVIDER` は API にフォールバックせず失敗します。10件のテストで、デフォルト、拒否、例外を固定しています。このバージョンの28件の翻訳は Codex 経由で再実行されました。

  - **rate limit に対する back-off を共通化しました**（`_retry_on_rate_limit`）。Codex と Grok のループはラベル以外が同一であり、3つ目のコピーを作ると重複のしきい値を超えるところでした。3つの CLI エラーは共通の `_CliCallError` を継承します。いずれか1つでもそこから外れると共通ループで検出できなくなるため、テストで禁止しています。
  - **テスト**：新規ファイル `tests/test_opencode_provider.py`（51テスト）— 完全な出力契約、agent のフォールバック、ログからの原因読み取り、重複したテキストパートと合成パートの無視、process group を終了させる timeout、429時の back-off、必須かつ検証済みのモデル、secret を含まない preflight、binary の解決、dispatch の配線、ファイル名ラベル、パストラバーサルの反証テスト。`tests/test_review_hardening.py` は、flag の排他性と secret 不在の検証を新しい provider にも拡張。gate は現在、文書化された **22個の flag** を argparse に要求。完全なスイートは **382テスト**。

- **1.11.1** ドキュメント修正：README がついに7つの provider 経路を記載（2026-09-03）：

  - **1.11.0 の PyPI ページには「4つの API + Codex CLI」と記載されていた。** 実際のコードが提供するのは7つで、API 経由の OpenAI、Mistral、Claude、Gemini、Grok、および従量課金なしのサブスクリプション経由の Codex（ChatGPT）と Grok。冒頭文と _Multi-Provider_ の箇条書きには2つの Grok モードが欠けており、14の翻訳でも同じ誤りが繰り返されていた。パッケージの長い説明文はバージョンごとに固定されるため、公開ページを修正するには新しいバージョン番号が必要だった。これがこのバージョンの唯一の目的。**コード変更なし。**
  - `CLAUDE.md` をリリースで導入された内容に整合：gate のカウンター（16、`--full` では17）、有効な11の workflow、`gh pr checks` では見えない2つの Sonar/Codacy カウンター（hotspot、Codacy API）、`ruff-format` による `# nosemgrep` の移動、OIDC 交換に必要な GitHub environment、そして _pending publisher_ は名前を予約しないという事実。

- **1.11.0** PyPI で公開：リポジトリを clone せずに `pip install ai-powered-markdown-translator`、続いてコマンド `aipmt`（2026-09-03）：

  - **単一ファイルのスクリプトがインストール可能なパッケージに。** `translate.py` をルートから `src/aipmt/translate.py` に移動し、console entry point `aipmt` と、それに相当する `python -m aipmt` を提供。貢献するには引き続きリポジトリの clone が必要で、テスト、28の翻訳、品質ツールはそこに含まれるが、利用するだけなら不要になった。

    - **import 名は常に `aipmt` であり、決して `translate` ではない。** 実在し、しかも無言で発生する衝突を避けるためである。PyPI パッケージ `translate`（v3.8.1、最終 upload 2026-07-06）は、同名のディレクトリをインストールする。venv で再現すると、ディレクトリが module より優先され、`translate.main` が消え、entry point は `AttributeError` で壊れる。それでも `pip check` は「No broken requirements found」と応答し、rc=0 となる。ユーザーが単に `pip install translate` を実行しただけで、利用可能な診断もなく CLI が壊れ得た。実際の wheel による反証テストでは、既存パッケージの上から `pip install translate` を導入し、前後とも `aipmt --help` は rc=0、両方の CLI が共存する。
    - **長い distribution 名、短いコマンド。** `ai-powered-markdown-translator` により、PyPI 検索でパッケージを見つけられる。略称だけでは、すでにプロジェクトを知っている人以外には発見できず、公開の目的はまさに見つけてもらうことにある。妥当に見える2つの候補は検証の結果除外した。`ai-markdown-translator` は、同じ用途のツールによって2024年から npm で使用済みで、このリポジトリより17か月古い。また `aimt` は、同じ分野で現在も活動中のパッケージ `aim`（v3.29.1）と1文字しか違わず、長期的な混同を招く最悪の条件だった。検証方法にも落とし穴がある。`pypi.org/project/<nom>/` はどの名前に対しても200を返す anti-bot ページであり、信頼できるのは JSON API だけである。
    - **フラットなパッケージではなく `src/` layout。** フラットなパッケージならテスト内の6つの `sys.path.insert(..., "..")` を維持できたが、まさにそれが問題だった。パッケージではなくソースツリーを import するため、パッケージングの誤りがすべて隠れてしまう。実際のコストは、置換ルールが1つ増えるだけである。

  - **キーをついに一度設定するだけで済むように。** インストール済み CLI には永続的な設定がなく、環境変数と現在のディレクトリにある `.env` しか選択肢がなかった。確かに `find_dotenv` はシステムのルートまで遡るため、**ホームディレクトリ配下で作業している場合**には `~/.env` を見つけたが、それ以外の場所では何も見つからなかった。つまり、設定範囲が設計上の選択ではなく、コマンドを実行した場所に依存していた。そこで既存の2層の下に、第3層として `~/.config/aipmt/.env` を追加。

    - **優先順位は明示的に実装されておらず**、`load_dotenv` のデフォルト値である `override=False` から自然に決まる。各層は、前の層で空のまま残った値だけを補う。その結果、環境変数 → プロジェクトの `.env` → ユーザー設定という順序になる。これは構造ではなく挙動のテストで検証されており、2つの呼び出し順を逆にしても、第3層を削除しても失敗する。
    - 意図的に **TOML ではなく `.env` 形式**を採用。`python-dotenv` はすでに依存関係に含まれ、その構文は15の README ですでに文書化されており、同じファイルを両方のスコープで使用できる。新しい依存関係も構文も追加しない。場所は、`XDG_CONFIG_HOME` が**絶対パス**の場合はそれに従い、Windows では `APPDATA` に従う。仕様では相対値を無視するよう求めている。そうしなければ、設定場所が再び現在のディレクトリに依存してしまうためである。
    - **2つの選択肢を理由付きで除外。** システムの keyring（`keyring`）はデスクトップではより安全だが、server、container、CI といった headless 環境では失敗する。これはまさに一括翻訳の用途である。opt-in の候補としては適切だが、デフォルトには不向き。`--api-key` flag を使うとキーが shell history に残り、`ps` から見えてしまう。
    - **キーがない場合も stack trace を表示しない。** 以前は `site-packages` を指す Python の stack trace と、「環境または .env」とだけ述べ、後者をどこに作成すべきか示さないメッセージが表示されていた。現在は3つの場所を正確なパス付きで列挙し、コマンドは終了コード2で終了する。安全策は**意図的に狭く**、設定フェーズだけを対象とする `except ValueError` である。実行全体を包むと、翻訳中に生じた本物の bug が安心させるようなメッセージに変換されてしまう。これはこのリポジトリが防ごうとしている失敗モードである。テストは `main()` のソースを読み、この実装を禁止している。

  - **修正 — ツールをインストールすると、ユーザーの `.env` が無視されていた。** 引数なしの `load_dotenv()` は現在のディレクトリから遡るのではなく、呼び出し元ファイル、つまり `site-packages` から遡る。独自の `.env` を持つプロジェクトから実際の console entry point を実行して測定すると、`find_dotenv()` は `''` を返し、キーを読み込まない一方、`find_dotenv(usecwd=True)` なら見つけられる。この bug は、ツールが clone 済みリポジトリ内からしか実行されていなかった間は存在しなかった。公開後は正しい設定であるにもかかわらず API キーが「見つからない」という症状だけを示し、恒常的に発生するところだった。

  - **3つの gate は、何も検証しなくなっても緑になり得た。** 移動の**前に**意図的に強化した。捕捉対象の変更後に書かれた安全策だけでは何も証明できないためである。各 gate は元のリポジトリでは緑になり、移行済みコピーでは赤になる。両方向を測定済み。

    - **Lizard は存在しないパスを黙って無視する**：rc=0、「0 file analyzed」。complexity gate は158 functions / 2247 nloc から3 functions / 34 nloc に減り、出力は0 byte になっても通過していた。現在、scope は配列であり、各 entry の存在を確認する。
    - **存在しない module に対する `coverage run --source=` は失敗しない**：stderr の警告だけで、unittest でも `coverage xml` でも rc=0。しかも report は公開され、statements は1453から141へ欠落していた。ほとんど分析されていないために、プロジェクトが健全に見えてしまうところだった。2つの下限で report を保護する。全体の値と、測定対象となった最大ファイルの値である。
    - **翻訳の鮮度 probe は、呼び出し形式を構造上検出できない**：argparse の flag を基準にしているが、ファイル名を変更してもそこは変わらない。再現結果では、module を移動し、15の README が存在しないコマンドを文書化したままでも、判定は「古い翻訳なし」だった。そのため第7セクションでは option ではなく**形式**を検証し、Lizard hook をスクリプトの実際の scope と照合する。キー `files:` は一致しなくなっても pre-commit を失敗させず、処理自体を**スキップ**させるためである。

  - **`requires-python = ">=3.10"` は単なる主張ではなくなった。** 開発環境には3.12しかなく、一度も検証されていなかったにもかかわらず、`sonar-project.properties` はすでに3.10～3.12を掲げていた。公開すれば表面化する内部矛盾だった。現在は test workflow が3.10、3.11、3.12でスイートを実行し、**パッケージ**をインストールすることで公開されているバージョン範囲も検証する。

  - **下限のみで上限なし。** `requirements.txt` はテスト済み lock のまま、`[project.dependencies]` を公開契約とする。lock の厳密なバージョンを公開すれば、ほかのパッケージも使うすべてのユーザー環境で衝突が起きる。`<N+1` の上限も設けない。major version の遅れがあれば release gate を失敗させる `check-deps-fresh.sh` と真っ向から矛盾するためである。下限の組み合わせは解決可能であり、反証テスト `openai==1.0.0` は `ResolutionImpossible` で終了する。これは検証がすべてを無条件に受け入れるのではなく、正しく判別していることを示す。さらに、`pyproject.toml` の version と CHANGELOG の version が不一致になることを guard が禁止している。PyPI では同じ番号を再利用できないためである。

  - **新規 venv で end-to-end 検証済み**：約70 Ko の wheel には `aipmt/*.py`、dist-info、license のみが含まれる。`aipmt --help` は22の flag を伴って rc=0。`python -m aipmt` は「usage: \_\_main\_\_.py」ではなく「usage: aipmt」と表示。`pipx` のインストールも正常。そして何より、**任意のユーザーディレクトリから実際に fr→en 翻訳を実行**し、太字、リスト、inline code、link、URL が保持され、code block は翻訳されなかった。移行前の318テストは、前後で byte 単位まで同一の identifier リストを保ったまま合格した。テストが無効化されていないことを証明するのは「OK」ではなく、この一致である。さらに3層設定用の12テストを追加し、合計330となった。

- **1.10.0** `--use_codex` provider（ChatGPT サブスクリプション枠）、SDK とモデルの更新、複数段落にまたがる news 引用の修正（2026-08-29）：

  - **セキュリティレビュー — PR が掲げながら、すべての箇所では守れていなかった2つの安全策**：

    - **Codex の preflight は `.env` 全体を binary に渡していた。** `_codex_preflight` は **`env=` なしで** `subprocess.run` を呼び出していた。subprocess が `os.environ` 全体、つまり `load_dotenv` によって読み込まれた `.env` のすべてを継承していた。計測機能を持たせた偽の binary で測定すると、6つの provider のキーと1つの `GITHUB_TOKEN`、合計**7つの secret**が preflight に到達していた。一方、対応する `_grok_preflight` は正しく `env=_grok_env()` を渡しており、到達した secret は**ゼロ**だった。これは PR 内部の不整合である。まさにこの invariant を維持するための `_strip_secret_env` が、わずか数行先に存在している。`_codex_env_base()` を抽出して両方の経路で共有。修正後の測定では、どちらも secret は0。
    - **「`--deny` は fail-closed」という性質は、実際に使用された形式には適用されていなかった。** コメントでは、未知の prefix を持つルールなら起動を拒否することを Grok の隔離全体の根拠としていた。`grok 1.0.13` で測定すると、この検証は**括弧付き形式のみ**に存在する。`--deny 'CeciNestPasUnOutil(*)'` は起動を拒否する（「unknown tool prefix」）一方、`--deny 'CeciNestPasUnOutil'` は黙って受け入れられる。しかし `GROK_DENY_RULES` が使用していたのは裸の名前だけだった。そのため、xAI 側でツール名が変更されると、OS sandbox がすでに適用されない環境で、測定済みの唯一の隔離層が何の通知もなく消えるところだった。名前付きの8つのルールを `Prefix(*)` に変更し、それぞれを CLI が認識する prefix として検証。catch-all の `*` は、唯一受け入れられる literal 形式のまま維持する。テストにより、未検証形式への逆戻りを防止。
    - **そのほかは問題がないことを確認済み**：command injection なし（常に list 形式で、`shell=True` は未使用。document の内容は stdin または `--prompt-file` 経由）、unsafe な deserialization なし（type guard 付きの `json.loads` のみ）、7つの payload による path traversal 修正の回避も確認されず、`--deny '*'` が CLI によって実際に適用されることも確認（workdir 外の読み取りで `DENY_ENFORCED` を観測）。
    - 前述の鮮度チェックも、自らの原則を回避していた。PyPI request が失敗したパッケージを黙ってスキップし、gate は緑になっていた。現在は実際に比較したパッケージ数を数え、coverage が不完全なら失敗する。

  - **依存関係を最新化し、遅れの再発を防ぐ2つの安全策を追加**：

    - **遅れは実在し、長期に及んでいた**：`openai` 2.54 → **3.6.0**、`anthropic` 0.125 → **1.2.0**、`certifi` 2024.8.30 → **2026.7.22**。すべての provider 呼び出しで TLS を検証する root certificate store は2年遅れていた。特定された原因は、**`.github/dependabot.yml` が存在しなかったこと**。このファイルがなければ GitHub が有効にするのは _security updates_ だけであり、Dependabot が PR を提案するのは CVE の対象となった依存関係だけである。これにより、`urllib3` と `idna` は更新された一方、2つの SDK が major version 1つ分遅れたままだった理由を説明できる。
    - **以前の推論で懸念されていたのとは異なり、2つの major version は衝突せず共存する**：`openai` 3.x と `anthropic` 1.x は **`httpx2`** に移行する一方、`mistralai` と `google-genai` は `httpx<1` のままだが、これらは別々の distribution である。実際にインストールして確認し、さらに OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI、Grok CLI の**7つの provider 経路を end-to-end でテスト**。すべての出力で inline code と link が保持された。「2つの HTTP stack を避ける」は好みにすぎず、障害ではなかった。測定によって決着した。
    - **`requirements.txt` は実環境を表していなかった**：`google-auth`、`cryptography`、`opentelemetry` stack は宣言されていないにもかかわらず作業用 venv にインストールされており、新規インストールではテスト対象の環境を再現できなかった。逆に `tokenizers`、`huggingface-hub`、`PyYAML` は、どこからも import も要求もされていないのに記載されていた。`mistralai` 1.x の残骸である。ファイルは、直接依存関係だけから構築した venv の完全な推移的依存関係として再生成。`pip-audit` は新しい組み合わせに既知の脆弱性を報告していない。
    - **`.github/dependabot.yml`**（新規）は pip と github-actions の週次 version update を有効化。minor と patch は1つの PR にまとめる。patch update ごとに PR を作ると無視されるようになり、ノイズは更新の敵だからである。**major は個別**とし、それぞれ実際の呼び出しによる検証を必須とする。
    - **`scripts/check-deps-fresh.sh`**（新規、gate に組み込み）は、遅れをプロジェクトの判定に反映する。Dependabot は提案するだけで保証はせず、その PR は蓄積し得る。major の遅れは失敗、minor は警告とする。常時赤い gate はやがて無視されるためである。PyPI に接続できない場合はローカルでは明示的に skip、**CI では fail-closed**。実行されなかったチェックは成功ではない。両方向で検証済み。修正前そのものの状態（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`）を捕捉し、minor の遅れでは警告だけに留まる。

  - **この PR のレビューから得られた修正** — 5つの review agent が diff を精査。以下のすべての項目は修正前に**測定によって再現**され、そのうち2つは同じバージョンの前段で導入された regression だった。
    - **修正済みのリグレッション — `_NEWS_CITATION_REGEX` で指数関数的バックトラッキングが発生していた。** 複数段落対応の修正によって繰り返し内に `(?:[ \t]*$|[ \t]+.*)` が導入され、`[ \t]+` と `.*` の間で空白の割り当てが曖昧になり、その曖昧さが反復ごとに増幅していた。パターンに一致しない、Markdown として完全に正当なインデントである `>   texte` の行を使って計測したところ、**14 行で 2,589 ms**だったのに対し、修正後は 0.04 ms で、1 行追加するごとに約 9 倍になっていた。`--news` モードでは、長く不適合な blockquote が 1 つあるだけで、原因を特定できないままジョブのタイムアウトまで翻訳が停止していた。繰り返しは今後、行全体をひとかたまりとして消費するため（`\n^>(?![ \t]*—).*`）、反復ごとの一致方法は 1 通りしか残らない。実際の 231 記事のコーパスで検証済み：キャプチャの差異は**ゼロ**、引用は同じ 423 件で、14 件の複数段落本文も引き続き拡張されている。
    - **2 つの provider フラグを同時に指定すると、警告なく従量課金になっていた。** `--use_codex --use_mistral` は受理されていた。`_select_provider_client` は Mistral を最初に検査し、`_resolve_provider` は明示的なブール値を優先するため、どちらも Mistral に収束していた。そのためユーザーはサブスクリプション枠の利用を要求しているのに、何の警告もなく従量課金されていた。これはまさに `--use_codex` が防ぐために存在する障害モードである。6 つの provider フラグは今後、すべて `add_mutually_exclusive_group` を経由する。**動作変更**：従来は暗黙に受理されていた 2 つの provider を組み合わせたコマンドラインは、今後 `argument --use_mistral: not allowed with argument --use_codex` で失敗する。
    - **作業完了 gate は、probe がクラッシュしても成功状態になっていた。** `scripts/check-release-ready.sh` にある 13 個の検証のうち 4 個は、終了コードをまったく確認せず、「stdout を取得し、空なら結論を出す」というパターンに従っていた。例外（ファイル名の変更、`FileNotFoundError`）は stderr に書き込み、stdout を空のままにするため、検証は「問題なし」と結論づけていた。それを防ぐためのスクリプト内で、「`exit 0` は何も証明しない」という罠が再現されていた。今後は helper `probe()` が終了コード 0 **かつ**終了 sentinel を必須とし、probe は目印の集合が空なら結論を出さない。空集合に対する assertion は常に真になるためである。実証：上記の排他的グループを追加したことで provider フラグが `*_group` オブジェクトを経由するようになり、旧 regex `parser\.add_argument\(` は一致しなくなった。その結果、**21 フラグ中 6 個**が暗黙に対象外となっていたにもかかわらず、gate は成功状態になっていた。
    - **secret scan は 6 provider 中 4 つを見逃していた。** 文字クラス `[A-Za-z0-9]` はハイフンを除外しているため、`sk-proj-…`（現在の OpenAI 形式）と `sk-ant-api03-…` は 2 番目のハイフンで途切れ、`AIza…` は対象に含まれていなかった。パターンを拡張し、`.secrets.baseline` は scan から除外した。また、guard `.env` は `git diff --cached` を照会していたが、これは index しか参照しないため、最悪のケースである**すでにコミット済み**の `.env` は決して表示されなかった。今後は `git ls-files` を照会する。
    - **Codex の「token warm-up」は warm-up になっていなかった。** 計測の結果、`codex login status` は `~/.codex/auth.json` に変更を加えず（mtime とサイズは不変）、help にも「ログイン状態を表示」と記載されている。それにもかかわらず、コメントでは token を「1 回、逐次的に」refresh し、1 回限り使用できる rotating token に対する並行 refresh のリスクを無効化すると主張していた。説明されていた保護は存在しなかったため、コメントは今後、コードが実際に行うことを記述し、本当の対策は引き続き `max_jobs=4` である。さらに、この確認処理は従来無視していた `CODEX_BIN` を尊重するようになった。`PATH` に `codex` がない環境では「未認証」で失敗し、誤解を招く診断になっていた。
    - **`.env` は subshell 内で source されていた。** `detect_provider` は command substitution 内で呼び出されるため、その export は呼び出し元に伝播していなかった。その結果、`.env` で定義された `GROK_BIN`、`GROK_HOME`、`REGEN_MODEL` は `main()` 内の読み取りから見えず、正しい設定でも「Grok バイナリが見つからない」と結論づけていた。
    - **並行数が公称上限を 50% 超過していた。** guard が README/CHANGELOG のペアを起動した後に配置されていたため、`max_jobs=2` に対する実測ピークは **3** だった。週次 quota が Chat/Imagine/Voice と共有され、計測できない Grok では、スクリプトが自ら課した上限すら守られていなかった。また、最終カウントは表示されるだけで 28 と比較されておらず、ファイルが欠けていても見逃されていた。
    - **Grok の出力 contract：`stopReason` がなければ今後は失敗となる。** 公表された contract が `end_turn` を要求している箇所で、コードは「`end_turn` **または不在**」を適用していた。該当 field のない payload や、CLI の更新で field 名が変更された payload では、guard が暗黙の no-op になっていた。また、`max_turn_requests` は rate limit に分類されなくなった。これは turn budget の枯渇であり、retry しても 90 秒待った末に同じ結果が再現されるためである。さらに `quota` は rate limit marker から除外された。その理由は `_codex_is_rate_limited` の docstring にすでに記載されていたが、Grok には適用されていなかった。
    - **Gemini cascade はモデルごとに memoize される。** デフォルトモデルが拒否するにもかかわらず、segment ごとに `minimal` からやり直していたため、通常経路で segment ごとに 400 の round-trip が発生し、同じ警告が繰り返し表示されていた。何百回も繰り返される warning は読まれなくなる。そうして warning は情報を覆い隠すものになる。
    - **その他**：CI の拒否メッセージが Codex 用にハードコードされており、`--use_grok_cli` のユーザーを `XAI_API_KEY` ではなく `OPENAI_API_KEY` に誘導していた。`provider.capitalize()` は「Grok_cli」と「Openai」を表示していた。subprocess 基盤のコメントでは「shim」を両方の CLI に一般化していたが、Grok バイナリはネイティブ ELF であり、正しい根拠は「独自の subprocess を spawn する agent」である。`subprocess` に関する 12 件の SAST finding は、`shell=True` を伴わない list 形式によって injection が不可能であり、document の内容が argv を経由することもないという根拠を添えて、`# nosec` / `# nosemgrep` としてマークされた。
    - **agentic subprocess に secret が渡されることは今後一切ない。** 名前を列挙する deny-list が保護していたのは、**課金**に関する不変条件（`OPENAI_API_KEY` のない Codex、`XAI_API_KEY` のない Grok）だけだった。計測すると、Anthropic、Mistral、Google、Gemini のキー、もう一方の CLI のキー、そして secret ではないものの通信先を変更する `OPENAI_BASE_URL` という、**ほかの 7 つの secret** が各 subprocess に渡されていた。しかし、この 2 つの CLI は**agent**であり、Grok は多くの Linux 環境で適用可能な OS sandbox なしに動作する。今後は名前の列挙ではなく、**名前のパターン**（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`）で filter するため、このコードが認識していない、ユーザーが `.env` に追加した変数も対象になる。CLI に必要な変数は 1 つもない。認証情報は `~/.codex` と `~/.grok` にあり、環境変数には存在しない。強化された環境を使い、両 provider でそれぞれ**実際の翻訳を正常完了**させて検証済み。
    - **テスト**：新しいファイル `tests/test_review_hardening.py`（21 tests）で、provider フラグの排他性、`stopReason` contract、news regex の線形性、CI の拒否メッセージ、Gemini の memoization、subprocess 環境に secret が一切存在しないことを固定した。最後の assertion は**汎用的**で、どの list にも名前がないキーでも失敗する。既存の除去テストは定数の鏡像にすぎず、自身の loop の故障以外は何も検出できなかった。全 suite は **311 tests**。

  - **新しい 2 つの Grok provider**：`--use_grok`（xAI API、キー `XAI_API_KEY`、従量課金）と `--use_grok_cli`（公式 Grok Build CLI、Grok サブスクリプションから消費される。`--use_codex` と同じ原則）。
    - **API モード、約 40 行**：xAI endpoint は OpenAI 互換なので、client と `_call_openai` をそのまま再利用し、変更されるのは `base_url` だけである。必要だった調整は 1 つだけで、すべての provider に恩恵がある。`finish_reason` は今後、OpenAI が `stop` を返す箇所で xAI が返す形式 `end_turn` も受理する。モデル：`grok-4.6`（品質）と `grok-4.3`（eco）。なお、Grok の eco は依然としてリポジトリ内で最も高価で、100 万 tokens 当たり $1.25/$2.50 なのに対し、`mistral-small-latest` は $0.15/$0.60 である。この provider は価格ではなく、モデルの多様性を目的に選択するものだ。
    - **CLI モード**：Codex を基礎としつつ、実環境から課された 4 つの相違点がある。prompt はファイルで渡す（`--prompt-file`。CLI は stdin を読まず、segment を argv に入れると `ps` から見える）。出力は stdout 上の単一 JSON object である（JSONL でも `-o` ファイルでもない）。サブスクリプションで利用できるのは `grok-4.6` と `grok-4.5` だけで、sandbox は適用できない（以下を参照）。subprocess の起動処理は `_codex_run_process` で Codex と共通化し、すでにテスト済みの Codex provider の残りの部分には触れていない。
    - **`exit 0` は何も証明しないことを実測で確認**：未認証の場合、CLI は終了コード **0** で `{"type":"error","message":"Not signed in."}` を **stdout** に書き込む。拒否や turn 超過でも同様に動作する。そのため、出力 contract は 4 条件を同時に要求する。終了コード 0、error payload がないこと、`stopReason == end_turn`、空でない text である。preflight も同じ論理に従う。`grok models` はログアウト状態でも 0 で終了するため、stdout に「not authenticated」が存在する場合にのみ未認証と結論づけられる。
    - **confinement：非対称性を意図的に採用し、文書化した。** Codex は `--sandbox read-only` で動作する一方、Grok の sandbox は、`sudo` なしには回避できない独立した 2 つのシステム上の理由により、多くの最近の Linux 環境で適用できない。Ubuntu 24.04 以降では AppArmor が非特権 user namespace を遮断し（`bwrap: setting up uid map: Permission denied`、Grok 外でも再現済み）、`/run/podman` が `0700` の場合は container runtime socket の deny-list が失敗する（resolver が捕捉するのは `ErrorKind::NotFound` だけで、EACCES は致命的になる）。中心的な落とし穴は、適用できない**組み込み** profile が、**暗黙に confinement なしで起動する**ことだ。そのためスクリプトはデフォルトで profile を要求せず、暗黙の fallback も一切行わず、stderr に警告する。保護は CLI の `--deny` rule に依存し、catch-all の `*` も含まれる。これは _fail-closed_ であることが実測された唯一の層である（未知の prefix を持つ rule があると起動を拒否する）。`GROK_TRANSLATE_SANDBOX=read-only` を使えば sandbox を必須にでき、その場合、マシンが要件を満たせなければ起動に失敗する。
    - **guardrail**：`XAI_API_KEY`、`GROK_API_KEY`、`GROK_SANDBOX` は subprocess の環境から除去される。キーがあると従量課金に切り替わり、継承された `GROK_SANDBOX` は適用不能な profile を誤解を招くメッセージとともに強制するためである。MCP/hooks/skills/agents の switch は無効化され、`--disable-web-search`、`--no-subagents`、`--no-plan`、使い捨て workdir、CI での拒否、process group を kill する timeout、rate limit 時の back-off を採用した。`--max-turns` は 1 ではなく 6 に固定される。counter は tool turn の後に増加するため、1 にすると出力が途中で切れる。
    - **quota**：Grok の pool は週次で、**Chat、Imagine、Voice と共有**されており、これを表示する command は存在しない。`account/rateLimits/read` で消費量を数値化できる Codex とは異なる。そのため `regen_translations.sh` は並行数を 2 に制限し、明示的に警告する。
    - **テスト**：新しいファイル `tests/test_grok_provider.py`（24 tests）。全 suite は **290 tests**。
  - **修正済みのバグ — 複数段落の英語引用は一部しか保護されていなかった（`--news` モード）**：`_NEWS_CITATION_REGEX` は引用本文として、**連続する** `>` 行の並びしか受理していなかった。引用が複数の段落にまたがると（空の `>` 行で区切られる）、最後の段落だけがキャプチャされて placeholder に置換され、それ以前の段落は LLM に送られて翻訳されていた。これは `--news` が保証するために存在する動作と正反対だった。繰り返しは今後、内部の空の `>` 行を受理し、非貪欲になるため、最初に現れる空行ではなく、斜体行の前にある空の `>` で停止する。
    - **実測した規模**：実際の 198 記事のコーパスでは、419 件の引用中 11 件が該当した。リグレッションはない。新しい regex がキャプチャする引用数は完全に同じで、拡張されるのは複数段落の本文だけである（408 本文は同一、11 本文は拡張）。attribution 行 `> — …` は引き続き本文に取り込まれない（lookahead を維持）。
    - **end-to-end の証明**：69 ko の記事を ja/ar に翻訳したところ、引用の第 1 段落は以前、日本語では `> GLM-5.3がオープンウェイト化。` となり、アラビア語でも同様に翻訳されていたが、今後は `> GLM-5.3 is now open-weight.` のまま維持される。英語の引用行数は 9 から 10 に戻り、source と一致した。
    - なお、この欠陥は下流の validator では検出されなかった。validator は引用の存在を確認するだけで、完全性までは確認していなかったためである。
  - **デフォルト provider での実測済みの節約**：モデル名が `gpt-5` で始まると、`--eco` の場合も含めて `_openai_extra_kwargs` は `reasoning_effort="medium"` を送信していた。10 語の文を翻訳するために `gpt-5.4-mini` で計測した結果、`medium` は reasoning tokens 45 と出力 tokens 65、`none` はそれぞれ 0 と 14 だった。翻訳に reasoning の利点はなく、各ファイルの各 segment で費用が発生していた。デフォルト値は `--eco` では `none`、それ以外では引き続き `medium` となる。CLI で明示的に渡した値が引き続き優先される。`--reasoning_effort` は今後、`low`/`medium`/`high` に加えて `none` と `xhigh` も受理する。ただし、すべての値がすべてのモデルで受理されるわけではない。たとえば `minimal` は `gpt-5.4-mini` に拒否されるが、既存のパラメータなし retry がこの場合をカバーする。
  - **SDK の更新と Gemini の migration**：`google-generativeai`（2025-11-30 にサポート終了、リポジトリは archive 済み）を統合 SDK **`google-genai`** に置き換えた。`genai.Client(api_key=...)`、次に `client.models.generate_content(model=, contents=, config=)` を使用し、system prompt は segment に連結せず `system_instruction` として渡す。`mistralai` は **2.9.4** に更新され（import は `from mistralai.client import Mistral` になり、旧形式は `ImportError` を発生させることを wheel 内で確認済み）、`anthropic` は **0.125.0**、`openai` は **2.54.0** に更新された。venv 内に 2 つの HTTP stack を共存させないため、`httpx2` への移行前の最終版を採用している。これに伴い、`httpx` 0.28.1 と `pydantic` 2.13.5 の固定も解除した。
  - **文書ではなく実際のテストで捕捉した 2 つのリグレッション**：
    - `anthropic` ≥ 1.0 は、`max_tokens` から 10 分超の所要時間が予測される非 stream 呼び出しを client 側で拒否する（`ValueError: Streaming is required...`）。この guardrail は 0.34.2 には存在せず、`max_tokens=32768` を使うすべての Claude 呼び出しを壊していた。明示的な `timeout`（`CLAUDE_TIMEOUT`、デフォルト 900 s）で修正した。これにより、完全な応答だけを利用する呼び出しを streaming に切り替えずに済む。
    - `thinking_level="minimal"` を受理するのは Gemini カタログの一部だけである。`gemini-3.1-flash-lite` はサポートするが、`gemini-3.7-flash` と `gemini-3.1-pro-preview` は 400 で拒否する。そのため `_gemini_generate_with_fallback` として、既存の OpenAI fallback と同様に `minimal` → `low` → thinking_config なし、という cascade を採用した。最適化用パラメータが原因で翻訳に失敗してはならない。
  - **デフォルトモデルを刷新**し、それぞれ実際の呼び出しで検証した：OpenAI は `gpt-5.5` → **`gpt-5.6-terra`**（28 件の batch で −60%）、`gpt-5.4-mini` → **`gpt-5.6-luna`**（−73%）。Claude は `claude-sonnet-4-6` → **`claude-sonnet-5`**（より安価で新しい）、`claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（日付なしの canonical ID）。Gemini は `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**、`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（stable version で、`3.5-flash-lite` より安価）。
 Mistral は変更なしで、`mistral-large-latest` が引き続き4つの中で最もコストパフォーマンスに優れています。注：`gemini-3.1-pro-preview` より新しい Pro 系の Gemini モデルは存在しません。2026年5月に発表された Gemini 3.5 Pro は結局リリースされず、3.5/3.6/3.7 系列は Flash 専用です。
  - **Gemini 切り替え前の実測 A/B テスト**：`README.md` を `gemini-3.1-pro-preview`、続いて `gemini-3.7-flash` で日本語に翻訳。構造は完全に同一（リスト21個、コードブロック18個、HTML リンク13個、画像13個、すべての URL を維持）で、所要時間は **48秒に対して8秒** でした。この2つのモデルを翻訳または非ラテン文字の処理について比較する公開ベンチマークは存在しないため、この切り替えは実測がなければ単なる推測に基づくものとなっていました。
  - **Claude のレスポンスブロックのフィルタリング**：`_call_claude` は型をフィルタリングせずに `block.text for block in response.content` を実行していました。適応的推論モデル（Sonnet 5 以降）は `thinking` ブロックを挿入しますが、これは `.text` ではなく `.thinking` を公開するため、最初のセグメントで不透明な `AttributeError` が発生し、翻訳が失敗していました。今後は `thinking`、`redacted_thinking`、`tool_use`、`tool_result` の各ブロックを除外し（テキストを含む未知の型を許容するための除外リスト方式）、テキストブロックをまったく含まないレスポンスでは明示的なエラーを発生させます。各呼び出しには `thinking={"type": "disabled"}` が渡されます。
  - **`MODEL_TOKEN_LIMITS` を再同期**：廃止日を過ぎたモデル（2026-07-31 に廃止された `magistral-*` 系列、2026-06-01 の `gemini-2.0-*`、2026-03-09 の `gemini-3-pro-preview`、`claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）を削除しました。上限を修正：Mistral は 128K → **256K**（Large 3 / Small 4 世代）、Gemini は 1 000 000 → **1 048 576**（実際の入力上限）、`claude-opus-4-5` は 200K → **1M**、`gpt-5.6-*` 系列は 400K → **1.05M**。Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest`、`ministral-*` 系列を追加しました。注：これらの上限はあくまで目安であり、`translate()` によるセグメント分割の上限は `min(16000, limite)` です。

  - **Provider `--use_codex`**：使用量に応じて課金される API を呼び出す代わりに、公式 Codex CLI（`codex exec`）を非対話モードで操作する5つ目の provider です。翻訳の利用量は、すでに支払い済みの ChatGPT サブスクリプション枠から差し引かれます。これは、この用途について OpenAI が文書化している唯一の方法です。プラン別の利用可否表では、「Codex SDK、`codex exec`、およびスクリプト化可能なワークフロー」が Plus/Pro/Business/Enterprise で利用可能とされています。一方、`~/.codex/auth.json` のトークンでは API Platform の呼び出しを認証できません（また、このスクリプトがそれを読み取ることもありません。認証と更新は引き続き CLI が管理します）。
  - **Codex バイナリを npm だけでなく pip でもインストール可能に**：`_resolve_codex_binary()` は `CODEX_BIN`、次に `PATH`、最後に OpenAI が公開する公式 Python パッケージ **`openai-codex-cli-bin`**（`openai-codex` SDK の依存関係）からバイナリを検索します。したがって、Python プロジェクトで `--use_codex` を使用するために npm のグローバルインストールは不要になりました。このパッケージは `requirements.txt` には追加していません。バイナリは約250 MBあり、任意の provider のために全ユーザーへ強制することになるためです。エンドツーエンドで検証済みです。`codex` が `PATH` に存在しない状態でも、パッケージ同梱のバイナリが解決され、完全な翻訳が6秒で完了します。
  - **「サブスクリプションモード」の保証**：`OPENAI_API_KEY` と `CODEX_API_KEY` をサブプロセスの環境から除外します。この保護がないと、`.env` に存在するキーによって、目に見える通知なしに Codex が従量課金へ切り替わる可能性があります。これはまさに、この provider が回避するために存在する事態です。
  - **CLI の落とし穴をテストで固定**：
    - `codex exec` は、プロンプトを引数として渡した場合でも stdin を読み取ります。stdin を閉じなければ、コマンドはモデルを一度も呼び出さないままタイムアウトまで待機します（再現結果：180秒後に終了コード124、出力0バイト）。したがって `communicate(input=...)` は必須です。
    - npm でインストールされた `codex` は、実際の Rust バイナリを `spawn` する Node のシムです。このバイナリは Python プロセスの**孫プロセス**であり、`subprocess.run(timeout=)` の `SIGKILL` 後も残存し、そのまま利用枠を消費し続ける可能性があります。そのため `Popen(start_new_session=True)` と `os.killpg` を使用します。
    - CLI は `turn.failed` を出力していても終了コード0で終了することがあります。戻り値だけでなく JSONL 出力（`--json`）も検査し、終了コード0にもかかわらず `-o` ファイルが存在しない場合は、空のセグメントを生成せず明示的なエラーを発生させます。
  - **レート制限時のバックオフ**：CLI には内部リトライが実装されていません（`max_retries = 0`）。分類は部分文字列ではなく、JSON ペイロードの構造（`status: 429` / `error.type`）に基づいて行います。「quota」という語は、回復可能な 429 と恒久的な `insufficient_quota` の両方に現れるためです。
  - **CI の保護**：`CI` または `GITHUB_ACTIONS` が定義されている場合、`--use_codex` を拒否します。サブスクリプション認証は共有 runner での使用を想定しておらず、OpenAI も公開リポジトリでこのワークフローを使用しないよう明示的に推奨しています。
  - **モデル**：`gpt-5.6-sol`（品質重視）と `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` 系列は CLI と API Platform に共通ですが、ChatGPT アカウントですべてを利用できるわけではありません。許可リストはローカル検証なしにサーバー側で適用され、一般的でないモデルを指定すると警告が発生します。Plus プランでは、5時間の時間枠あたり Sol が10～100メッセージであるのに対し、Luna は250～2,000メッセージを利用できます。したがって、あらゆる一括処理では `--eco` が推奨モードです。
  - **修正済みの不具合 — `regen_translations.sh` が完全成功後もエラー終了していた問題**：`trap ... EXIT` は `failed_log` を参照していましたが、これは `main()` の `local` 変数であり、トラップ実行時にはすでに存在しません。`set -u` のもとでは `failed_log: unbound variable` が発生し、28件の翻訳がすべて正しく完了していたにもかかわらず、スクリプトは終了コード1で終了していました。その結果、再生成直後の最もコストがかかる段階で `release.sh --auto`（`set -e`）が中断される可能性がありました。変数をグローバル化し、トラップがその存在を確認するようにしました。有用な副作用として、これまでこのエラーに隠されていた実際の翻訳失敗が、終了時の概要に再び表示されるようになりました。
  - **`REGEN_MODEL`**：`regen_translations.sh` の新しい環境変数です。provider のデフォルトよりも特定のモデルを優先して強制します。たとえば、処理量重視の `--eco` モデルではなく、サブスクリプション枠の上位モデルで再生成するために `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol` を指定できます。
  - **`regen_translations.sh`**：`REGEN_PROVIDER=codex` を明示的なオプトインで利用可能にしました（ユーザーが気づかないうちにサブスクリプション枠を消費しないよう、自動検出は一切行いません）。並列処理を開始する前に、トークンを逐次的に1回だけ更新します。Codex の更新トークンはローテーション式かつ一度限りの使用であるため、ジョブを並行実行すると `codex login` セッションが無効になります。また、並行数は4に抑えます。
  - **関連するリファクタリング**：`_dispatch_provider_call` は、処理チェーン全体に4つ目の真偽値を渡す代わりに provider 名を返す `_resolve_provider()` を使用し、引数を8個から6個へ削減しました。最小限の `Namespace` で `translate(..., use_mistral=True)` を呼び出すテストを維持するため、明示的な真偽値は引き続き `args` より優先されます。
  - **テスト**：新しいファイル `tests/test_codex_provider.py`（48件のテスト）で、argv、除外処理済みの環境、前置き禁止の規約、無言の失敗、タイムアウト／killpg、バックオフ、事前確認、provider の解決、Gemini の推論カスケード、Claude のブロックフィルタリング、複数段落のニュース引用を網羅します。テストスイート全体で290件です。
  - **実環境での検証**：プロジェクトの `README.md` を Codex で**14言語**に翻訳した結果、参照翻訳と完全に同一の構造になりました（コードブロック14個、見出し24個、表の行25行、HTML リンク13個、画像13個、URL 19個、コードブロックは文字単位で完全一致、プレースホルダーの残留なし）。69 KB のニュース記事を `--news` モードで処理したところ、`gpt-5.6-luna` と `gpt-5.6-sol` の出力はいずれも en/ja/ar で後段のアプリケーション検証に合格しました。`account/rateLimits/read` で測定した消費量は、`--eco` モードでカウンターの丸めしきい値未満（5時間枠の0％）に収まりました。

- **1.9.2** 入れ子の括弧またはフランス語接頭辞を含むニュース帰属 URL の抽出を修正（2026-05-11）：

  - **修正済みの不具合**：`_protect_news_quotes` の帰属 URL 抽出では、正規表現 `re.search(r"\((.+?)\)", attribution)`（括弧内を遅延キャプチャ）を使用していました。`(relayé par [@user sur X](https://x.com/.../123))` のような帰属表記（入れ子の括弧：外側の `(` と Markdown リンクの `]()`）では、最初に現れた `)` でキャプチャが終了し、フランス語接頭辞を含む途中で切れた文字列 `relayé par [@user sur X](https://x.com/.../123`（末尾の `)` なし）になっていました。その結果、`_validate_news_post` は翻訳後の出力からこの文字列を探して毎回失敗していました。理由は、`)` が途中で切れていることと、「relayé par」が `relayed by`／`weitergeleitet von`／その他へ翻訳されることの2つです。low → medium → high → gpt-5.5 のカスケード全体でも通過できませんでした。
  - **修正**：正規表現を `re.search(r"\]\(([^)]+)\)", attribution)` に変更しました。Markdown リンクの `](url)` を明確に対象とし、フランス語接頭辞や切り捨てを含まない**純粋な URL のみ**をキャプチャします。翻訳中は `#URL{N}#` プレースホルダーによって不変性が維持されます。問題となっていた以下の2パターンに対応します：
    - `(relayé par [@account sur X](url))` — 入れ子の括弧
    - `via [@source](url)` または `selon [@author](url)` — 外側の括弧を伴わないフランス語接頭辞
  - **テスト**：`test_silent_failure.py` の `TestNewsCitationExtraction` クラスに2件追加：
    - `test_extract_attribution_url_with_nested_parens`（Genspark CEO E2B の不具合を正確に再現したケース）
    - `test_extract_attribution_url_with_french_prefix`（`via` を含む派生ケース）
  - **カバレッジ上の不足**：`check-editorial-coverage.py` は編集上の構文を検証しますが、翻訳処理が可能かどうかは検証しません。将来的な改善案（v1.9.2 の対象外）として、帰属情報の抽出をドライランでシミュレーションし、公開**前**にリスクのあるパターンを検出するチェックが考えられます。

- **1.9.1** 翻訳マーカーノート内の CTA ラベルの国際化を修正（2026-05-10）：

  - **修正済みの不具合**：翻訳済みファイル上部のマーカーバナーにある CTA リンクのラベル `[Voir le projet sur GitHub ↗]` が、`target_lang` に従わず、すべての対象言語で**フランス語のまま**になっていました。この部分は URL とリポジトリの slug を維持するため Python 側で組み立てられており、LLM には一切渡されないため、翻訳フェーズで修正できませんでした。v1.9 で `marker` 形式を追加して以降、気づかれないまま続いていたリグレッションです。
  - **修正**：15言語を各ローカライズ済みラベルに対応付ける新しい定数 `_VIEW_PROJECT_LABELS` を追加しました。`_translation_note_invariants(target_lang)` と `_assemble_translation_note_paragraphs(phrase, target_lang)` は対象言語も渡すようになりました。言語が不明な場合は `fr` にフォールバックします（安全策として KeyError を防止）。
  - **テスト**：`test_source_emits_three_paragraphs_repo_title_description_link` を調整（対象言語 `ja` → 期待される日本語ラベル）。新たに2件のテストを追加：`test_source_link_label_localized_per_target_lang`（ラテン文字、表意文字、アブジャドを含む7言語でパラメーター化）と `test_source_link_label_falls_back_to_french_for_unknown_target`。`test_translation_note_position.py` のテストは合計40件（従来は38件）。
  - **後方互換性**：デフォルト値 `target_lang="fr"` を持つシグネチャにより、`args.target_lang` を指定しない外部のプログラム呼び出し元も変更なしで引き続き動作します。
- **1.9** サイレント障害の修正 + 包括的な品質ツール + 複数位置対応の翻訳注記（2026-05-07）：
  - **複数位置対応の翻訳注記 + 「embed card」マーカーフォーマット**：
    - 新しいCLIオプション（追加のみ、デフォルトは変更なし → **破壊的変更なし**）：
      - `--note_position {top,bottom,both}`（デフォルト：`bottom`）：翻訳済みファイルの上部、下部、または両方に注記を配置します。
      - `--note_format {legacy,marker}`（デフォルト：`legacy`）：
        - `legacy` はv1.8の動作（太字段落 `**…**`）を**バイト単位で完全に**再現します。
        - `marker` は、非表示のMarkdownリンク参照定義（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）に続いて、「GitHubリポジトリ埋め込みカード」風の表示向けに構造化された**3段落のblockquote**を出力します。内容は、インラインコード内のプロジェクト名（`**\`ai-powered-markdown-translator\`\*\*`）、LLMによって翻訳された説明、および矢印が表示されるCTAリンク（`[Voir le projet sur GitHub ↗](URL)`）です。ビルド時にremarkプラグインから利用できます（jls42.orgのブログ → `remark-translation-banner`プラグインを参照）。
    - **LLMには一切送信されない不変要素**：リポジトリ名とGitHub URLは、説明文の翻訳後にPython側で組み立てられます。LLMがスラッグ `ai-powered-markdown-translator` や `https://github.com/jls42/...` を目にすることはないため、レンダラー、大文字・小文字、スキームが変更されることはありません。
    - **frontmatter対応の挿入**：`top` または `both` モードでは、注記はYAML frontmatterの終了用 `---` ブロックの**後**に挿入されます（Astro Content Collections／gray-matterへの安全対策）。ヘルパー `_split_frontmatter` はファイル先頭の `---\n…\n---\n` を検出して、その完全性を維持します。終了fenceのない未終了frontmatterでは**`RuntimeError`を送出**します（誤った位置に注記を付けて書き込む代わりに、そのファイルが `failed_files` に記録されます）。
    - **ホワイトリスト方式のモデル名サニタイザー**：`_sanitize_model` は `[A-Za-z0-9._:/-]` に含まれない文字をすべて `_` に置換し、空の場合は `unknown` にフォールバックします。Astroのremarkプラグイン側バリデーターと整合させ、マーカーフォーマットを壊す文字（空白、引用符、括弧、カンマなど）を無害化します。
    - **内部リファクタリング**：`_append_translation_note`（単一のモノリシック関数）→ 7個の純粋ヘルパー（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。ビルダーとコンポーザーを分離しました（ビルダーは区切りなしの純粋なブロックを返し、コンポーザーは位置に応じて `\n\n` を適用）。本番処理とソース側ヘルパーは、同じ3段落アセンブラーを共有します。
    - **空行を維持する `_quote_lines`**：各行の先頭に `> ` を付け、空行は `>` だけの行に変換します。これによりmdastは、blockquoteを改行入りの単一段落ではなく、3つの独立した段落（タイトル／説明／リンク）として認識できます。
    - **適応型 `_build_translation_note_block`**：LLMが維持した段落数に応じて処理します（3段落＝完全なカード形式、2段落＝文 + リンク、1段落＝フォールバック）。1段落のフォールバックでは、Markdownリンク `](` が検出された場合、リンクを囲む `<strong>` の表示が不安定になるため、**`**...**`で囲まなくなりました**。
    - **後方互換性**：`_compose_with_notes` 側で `getattr(args, "note_position", "bottom")` と `getattr(args, "note_format", "legacy")` を使用します。これらの属性を持たないNamespace（既存テスト、外部からのプログラム呼び出し）も変更なしで引き続き動作します。
  - **長文翻訳におけるサイレント障害の修正**：
    - すべてのプロバイダー（OpenAI、Mistral、Claude、Gemini）で翻訳後の言語を検証：決定論的レイヤー（ソースの抜粋がそのまま見つかるか）+ 確率的レイヤー（`langdetect`）
    - `finish_reason`／`stop_reason` のホワイトリスト：ホワイトリスト外の状態（truncation、content_filterなど）では必ず `RuntimeError` を送出
    - Claudeの `max_tokens`：`4096` → `32768`（16kセグメントで潜在的なtruncationを回避し、FR→JA/ZH/KO/AR/HIのスクリプト間変換に余裕を確保）
    - 見出し対応のセグメンテーション：セグメント後半のH2/H3を優先（各セグメントが意味的に完全なセクションから開始）
    - エラーをゼロ以外の終了コードまで伝播：`translate_markdown_file` は型付きステータス `success`／`failure`／`skipped` を返し、1ファイルでも失敗した場合は `main()` が `sys.exit(1)`（単一ファイルとバッチの両方）
    - すべてのプロバイダーに空コンテンツガード、ソース／出力比率の健全性検査（500文字以上で5%未満なら拒否）、コード用placeholderの検証（`#CODEBLOCK`／`#INLINECODE`）、LLM処理後の正規化（見出しに連結した区切り／リンク）、`reasoning_effort` なしでの `BadRequestError` retryを追加
    - 依存関係 `langdetect==1.0.9` を追加
  - **pre-commit品質ツール**（「完全なEurekAI方式」、14個のhook）：
    - Pre-commit：ruff（lint + format）、shellcheck、prettier（md/yaml/json）、detect-secrets（4つのAPI keyを保護）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（空白、EOF、大容量ファイル、shebangなど）
    - Pre-push：mypy（段階的なlaxモード）、Opengrep SAST（translate.py + scripts/）、pip-audit（初期はreportingモード）、unittest discover（tests/ + scripts/tests/）
    - `./venv/bin/python` を使用するローカルwrapperを `scripts/` に配置
    - `scripts/audit_verdict.py`：11件のunittestを備えたpip-audit用JSONパーサー。jls42-astroのパーサーをPythonへ移植
    - 初期のruff違反7件を修正：B904（raise from）×2、B007（未使用のdirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizardでは `translate.py` を一時的に除外（CCN 21～47の関数が4個あり、リファクタリングを予定）— scripts/には厳格なgateを適用
  - **SonarCloud + 包括的なカバレッジ**：
    - GitHub Actionsワークフロー `SonarCloud`（sonarcloud.yml + sonar-project.properties）：pushおよびpull requestのたびに分析し、`coverage.xml` でcoverageを取得
    - README上部に11個のSonarCloud badge（Quality Gate、Security／Reliability／Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）
    - `tests/test_silent_failure.py`（stdlibの `unittest`）：サイレント障害のエラーチェーンを構成する6段階を網羅
    - `tests/test_orchestration.py`（+79テスト）：`translate.py` のオーケストレーション層（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` のTypeError + BadRequestErrorフォールバック、o1シリーズのpromptフォーマット、`_validate_translation_output` のearly-return分岐）を網羅
    - `scripts/tests/test_audit_verdict.py`：`main()`（stdin/stdout）および `if __name__ == "__main__"` ブロックをsubprocess経由でカバー
    - **新規コードのcoverage**：75.5% → 約98%（translate.pyは98%、scripts/audit_verdict.pyは97%）
  - **テスト**：`tests/test_translation_note_position.py` は位置 × フォーマットのマトリクス（E2Eの `marker+top|bottom|both` と `legacy+top|bottom|both` を含む）、複数行へのprefix付与、バイト単位の後方互換性（golden literal）、サニタイザー、frontmatterの分割（未終了fenceでのraiseを含む）、3段落形式、2段落フォールバック、1段落 + Markdownリンクのガード、およびタイトルとURLがLLMへ一切送信されないことをassertする重要な安全策 `TestLLMPayloadExcludesInvariants` を網羅しています。**190件のテストに合格**、回帰0件。
  - ドキュメント：`README.md`（フランス語 + 14言語への翻訳、badge付き）、`CLAUDE.md`（pre-commitワークフロー + CI監視の詳細）、28件の翻訳を再生成
- **1.8** `--news` モード + 2026年モデルへの更新（2026-03-17、tag `v1.8`）：
  - デフォルトモデルを更新（2026年3月）：
    - OpenAI高品質：`gpt-5` → `gpt-5.4`
    - OpenAI低コスト：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini高品質：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）および `gemini-3.1-pro-preview`（1M）のtoken上限を追加
  - 初期 `--news` モード：`#NEWSQUOTE\d+#` placeholderによる英語引用の保護、`LANG_FLAGS` mapping（15言語）、対象言語別のflag管理
  - 復元前にnews用placeholderを検証（回帰：LLMがplaceholderを削除した場合、引用のない出力が気付かれずに生成されていた）
  - `regen_translations.sh` scriptをポータブル化（絶対pathを使用し、pwdに依存しない）
  - README／CHANGELOGのlanguage barにフランス語リンクを追加し、28件の翻訳を再生成
- **1.7** 新機能：
  - 翻訳時に元のファイル名を維持する `--keep_filename` オプション
  - API keyを自動的に読み込む `.env` ファイルのサポート
  - **インラインコードの保持**：翻訳中にbacktick（`` `...` ``）が保護されるようになりました
  - system promptを改善：
    - YAML frontmatter内の引用符をより適切に処理
    - template変数 `{variable}` を保護
    - 要求されていない翻訳者注記を禁止
  - 364ファイルで動作確認済み（jls42.orgブログの移行）
- **1.6** 新機能：
  - 翻訳用Google Gemini APIのサポート（`--use_gemini`）
  - デフォルトモデルを2026年版へ更新：
    - OpenAI：`gpt-5`（高品質）、`gpt-5-mini`（低コスト）
    - Claude：`claude-sonnet-4-5`（高品質）、`claude-haiku-4-5`（低コスト）
    - Gemini：`gemini-3-pro-preview`（高品質）、`gemini-3-flash-preview`（低コスト）
  - より高速かつ低コストなモデルを使用する低コストモード（`--eco`）
  - ディレクトリを走査せずに単一ファイルを翻訳（`--file`）
  - 新しい簡略化された命名pattern：`{base}-{lang}.md`
  - モデル名を含む従来の形式を維持する `--include_model` オプション
  - 一覧にないモデルをデフォルトのtoken上限（128k）でサポート
  - READMEを14言語へ翻訳
- **1.5** 改善：
  - **API keyおよびデフォルトモデルの更新：**
    - **OpenAI：** `DEFAULT_MODEL_OPENAI` から `"gpt-4o"` へ更新。
    - **Mistral AI：** `DEFAULT_MODEL_MISTRAL` から `"mistral-large-latest"` へ更新。
    - **Anthropic Claude：** `DEFAULT_ANTHROPIC_API_KEY` を追加し、`DEFAULT_MODEL_CLAUDE` から `"claude-3-5-sonnet-20240620"` へ更新。
  - **翻訳promptの最適化：**
    - 直接翻訳および翻訳注記用のpromptを拡充し、明確さと効率を向上させました。metadataや特定のformat要素を保持するための詳細な指示も含まれます。
  - **コードのリファクタリング：**
    - Mistral AI clientの初期化で `MistralClient` を `Mistral` classに置き換えました。
    - 可読性と保守性を高めるためにimportを再編成しました。
    - 翻訳時に元のformatを維持するため、テキストのセグメンテーションとコードブロックの処理を改善しました。
  - **出力ファイルの管理：**
    - 出力ファイル名内のモデルと言語の順序を入れ替え（例：`f"{base}-{args.target_lang}-{args.model}.md"`）、翻訳の整理と検索を容易にしました。
  - **その他の改善：**
    - 不要な空行を削除してコードを整理しました。
    - scriptの構造と可読性を向上させるための軽微な調整を行いました。
- **1.4** 新機能：
  - 翻訳用Anthropic Claude APIのサポート
  - 明確さと効率を高めるためのprompt最適化
  - コードの保守性を向上させる軽微な調整
- **1.3** 改善および新機能：
  - コードブロック処理の改善
  - 出力ファイル管理の改善
  - 既存ファイル検出の改善
  - 翻訳を強制する `--force` オプション
  - 出力ファイル名内のモデルと言語の順序を入れ替え
- **1.2** changelogの修正
- **1.1** Mistral AI APIのサポートを追加
- **1.0** 初期バージョン - OpenAI APIをサポート

**gpt-5.6-solでフランス語から日本語に翻訳された記事。**
