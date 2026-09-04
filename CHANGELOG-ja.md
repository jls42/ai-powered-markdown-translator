### 変更履歴

🌍 [フランス語](CHANGELOG.md) | [英語](CHANGELOG-en.md) | [スペイン語](CHANGELOG-es.md) | [中国語](CHANGELOG-zh.md) | [ドイツ語](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [韓国語](CHANGELOG-ko.md) | [アラビア語](CHANGELOG-ar.md) | [ヒンディー語](CHANGELOG-hi.md) | [イタリア語](CHANGELOG-it.md) | [オランダ語](CHANGELOG-nl.md) | [ポーランド語](CHANGELOG-pl.md) | [ポルトガル語](CHANGELOG-pt.md) | [ルーマニア語](CHANGELOG-ro.md) | [スウェーデン語](CHANGELOG-sv.md)

- **1.12.0** Provider `--use_opencode`：オープンソースエージェント OpenCode から、ユーザーが選択したプロバイダーへ――ローカルモデル、アカウント不要の無料モデル、サブスクリプション、またはキー（2026-09-04）：

  - **最初の7つとは性質が異なる、8番目のプロバイダーパス。** [OpenCode](https://opencode.ai)（MIT）はモデルプロバイダーではなく、ユーザーが OpenCode 自体に設定した接続先への_ルーター_である。接続先には、API キー、サブスクリプション（GitHub Copilot、ChatGPT、SuperGrok）、**アカウント不要**の無料モデルを提供する OpenCode Zen ゲートウェイ、または**ローカル**モデル（Ollama、LM Studio、llama.cpp）が含まれる。スクリプトは Codex や Grok と同様に `opencode run` を非対話モードで制御し、同じサブプロセス基盤（専用プロセスグループ、タイムアウト時に `SIGTERM`、続いて `SIGKILL`、stdin は常に閉じ、環境を除去）を再利用する。**2件の実際の翻訳**で検証済み：`opencode/mimo-v2.5-free` を使用したこの README 全体の英訳――49秒、1回のパス、ソースファイルと同一の構造（見出し32個、コードブロックの閉じ記号26個、リンク18個、URL 37個、表37行、インラインコード135個）――および `ollama/qwen2.5:7b` を使用した、キーを一切使わないローカルでのテストファイル翻訳。

  - **`--model provider/modèle` は必須であり、これは意図的な選択である。** `--model` がない場合、OpenCode は自身のデフォルトへフォールバックする。新規インストール時のデフォルトは `opencode/big-pickle` であり、やり取りが学習に使用される可能性のある無料の「ステルス」モデルである。実測でも、このモデルが応答した。ユーザーに代わって暗黙にこれを選択することは、このリポジトリが追跡している見えない切り替えそのものになる。そのため、エラーメッセージにはモデル一覧を表示するコマンド（`opencode models`）と、ローカル、無料、サブスクリプションの3例を明記している。`--eco` は効果がなく、その旨を伝える。`--reasoning_effort` は、明示的に要求された場合に限り、OpenCode の `--variant` としてそのまま渡される。

  - **隔離は推測ではなく実測済み。** インライン設定（`OPENCODE_CONFIG_CONTENT`、OpenCode のマージ順で最後に位置するため、ユーザー設定を置き換えずに優先される）では、すべてのツールを拒否する（`permission: {"*": "deny"}`）エージェント `aipmt` を定義する。レジストリはツールをモデルに提示すらしなくなり、「ファイルを一覧表示して `id` を実行せよ」と命じられても、モデルはツールを持っていないと応答する。セッション共有は無効化し、外部プラグインは除外（`--pure`）、`--auto` は決して使用せず、作業ディレクトリは使い捨てかつ空である。2件の暗黙の注入を実測し、遮断した。`OPENCODE_DISABLE_CLAUDE_CODE` がないと、ユーザーの `~/.claude/CLAUDE.md` が**すべての**プロンプトに入り（単純な「こんにちは」でも入力トークンは186ではなく515）、`OPENCODE_DISABLE_PROJECT_CONFIG` がないと、カレントディレクトリの `AGENTS.md` も入る。「各応答の末尾を BANANA にせよ」という指示が翻訳に適用された。グローバルな `~/.config/opencode/AGENTS.md` は引き続き注入される。これを除外する切り替えはなく、`XDG_CONFIG_HOME` を転用して回避すれば、ユーザーのプロバイダーまで隠れてしまう。場当たり的に細工せず、文書化した。

  - **`exit 0` は何の証明にもならない。3つ目の CLI にも同じ原則を適用しつつ、固有の落とし穴を2つ処理した。** 未知の `--agent` を指定しても `opencode run` は失敗しない。stderr に警告を出し、ツールが有効なコーディングエージェントへ**暗黙に**フォールバックする。インライン設定が反映されなければ、翻訳は書き込み可能なエージェントで開始されてしまう。そのため出力契約では、終了コードが0であること、`error` イベントがないこと、`tool_use` がないこと、最後の `step_finish` が `stop` であること（`length` は打ち切られた応答）、テキストが空でないことに加え、このメッセージが存在しないことも検証する。2つ目の落とし穴は、エラーの JSON イベントが**不透明**であることだ。「予期しないサーバーエラーです。詳細はサーバーログを確認してください。」という単純な参照しか示されず、実際の原因（`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`、`ProviderAuthError` など）はログにしか記録されない。そこで `--print-logs --log-level ERROR` を使用し、その後に続く Bun のトレースを除外して stderr の `error="…"` フィールドを読み取る。これにより未知のモデルは、原因を明示して1秒で失敗する。さらに `--title` により、余分な LLM 呼び出しも回避する。これがない場合、OpenCode は `small_model` に追加でもう1回問い合わせ、セッションタイトルを生成する。

  - **シークレット：Codex および Grok と同じパターンベースのフィルタリングを行うが、名前を指定した例外が1つある。** `OPENCODE_API_KEY` は保持される。これは OpenCode 自身のキー（Zen ゲートウェイ、Go サブスクリプション）であり、名前どおり OpenCode に渡されるものだ。OpenCode の `auth.json` に相当し、aipmt が管理したり課金したりできるキーではない。プロバイダーは OpenCode 内（`opencode auth login`、`opencode.json`）で設定し、aipmt の `.env` では決して設定しないため、aipmt のキーがサブプロセスへ到達することはない。サブスクリプション型 CLI とは異なり、CI では拒否しない。ランナー上で API キーやセルフホストモデルを使用するのは正当な用途である。

  - **パストラバーサル防止ガードは、生の値ではなく補間後の値を検査するようになった。** `provider/modèle` には `/` が含まれており、1.10.0 のガードはこれを拒否していた。`--model` がファイル名 `--include_model` に補間されるため、その判断自体は正しかった。ファイル名ラベルでは、補間前に `/`、`\`、`:` を `-` に置換するようになった（`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`。`:` は Windows では不正）。上流のガードはこのラベルを検査する。`../../evil` は対象ディレクトリ配下の単純な名前 `doc-en-..-..-evil.md` となり、`..` 単独は引き続き拒否され、`--target_lang ../x` も拒否される。範囲を検査する `_ensure_within_directory` ガードは、第2層として変更なく維持される。

  - **無料モデルとローカルモデルについて実測した結果。** `opencode/mimo-v2.5-free` は1段落を16秒、この README を49秒で翻訳する。`opencode/big-pickle` は200語に40秒かかり、個別なら完了する2件のリクエストを同時に送ると、5分間応答がなかった。`opencode/nemotron-3.5-lightning-free` は3分待っても何も応答しなかった。このため `REGEN_PROVIDER=opencode` では `REGEN_MODEL` を必須とし、並列実行は**2ジョブ**にしている。ローカル側では、Ollama のコンテキストが4,096トークンに設定されることが多い一方、セグメントは最大16,000文字になるため、`PARAMETER num_ctx 32768` を指定した `Modelfile` が必要である。品質はモデル次第で、7B モデルはテストファイル内のリストを逆順にし、コードブロックの閉じ記号を壊したが、ゲートウェイのモデルはすべてを保持した。

  - **このリポジトリの翻訳に、従量課金 API が使われることは今後一切ない。** `regen_translations.sh` は `.env` にキーが残っていれば即座に OpenAI API を使用し、Codex は明示的に選択した場合にしか使わなかった。このバージョンの準備中、まさにそれが起きた。28件の翻訳が OpenAI API へ送られ、その後ヒンディー語版 CHANGELOG は Gemini API へ送られた。利用量に応じた料金を避けるために ChatGPT サブスクリプションが存在するにもかかわらず、である。キーの自動検出を廃止した。**デフォルトは品質重視モデルの `gpt-5.6-sol` を使用する Codex** となる。`openai`、`gemini`、`grok` には `REGEN_PROVIDER` に加えて `REGEN_ALLOW_PAID_API=1` が必要になる。これは判断時点で規則が確実に適用されるよう明示的に命名した例外である。未知の `REGEN_PROVIDER` は API にフォールバックせず失敗する。10件のテストで、デフォルト、拒否、例外を固定している。このバージョンの28件の翻訳は Codex を使用してやり直した。

  - **レート制限時のバックオフを共通化した**（`_retry_on_rate_limit`）。Codex と Grok のループは、表示文言を除けば同一であり、3つ目を複製すれば重複判定のしきい値を超えるところだった。3種類の CLI エラーは共通の `_CliCallError` を継承する。いずれかがこの継承関係から外れると共有ループで検出できなくなるため、それを禁止するテストを追加した。

  - **テスト**：新規ファイル `tests/test_opencode_provider.py`（51件のテスト）――完全な出力契約、エージェントのフォールバック、ログからの原因取得、重複テキストパートの排除と合成パートの無視、タイムアウト時のプロセスグループ終了、429時のバックオフ、モデルの必須化と検証、シークレットを使わないプリフライト、バイナリ解決、ディスパッチ接続、ファイル名ラベル、パストラバーサルの反証テスト。`tests/test_review_hardening.py` では、フラグの排他性とシークレット不在の検証を新しいプロバイダーにも拡張した。ゲートは、文書化された argparse の**22個のフラグ**を要求するようになった。全テストは**382件**。

- **1.11.1** ドキュメント修正：README で7つのプロバイダーパスをようやく明記（2026-09-03）：

  - **1.11.0 の PyPI ページには「4つの API + Codex CLI」と記載されていた。** 実際のコードが提供するのは7つである。API 経由の OpenAI、Mistral、Claude、Gemini、Grok、そして従量課金なしでサブスクリプションを利用する Codex（ChatGPT）と Grok だ。冒頭文と _Multi-Provider_ の項目から2つの Grok モードが抜けており、14言語の翻訳でも同じ誤りが繰り返されていた。パッケージの長い説明文はバージョンごとに固定されるため、公開ページを修正するには新しいバージョン番号が必要だった。それがこのリリースの唯一の理由である。**コードの変更はない。**
  - `CLAUDE.md` を、公開時に導入された内容と一致させた。ゲートのカウンター（16、`--full` では17）、有効な11個のワークフロー、`gh pr checks` からは見えない2個の Sonar/Codacy カウンター（ホットスポット、Codacy API）、`ruff-format` による `# nosemgrep` の移動、OIDC 交換に必要な GitHub 環境、そして_保留中のパブリッシャー_は名前を予約しないという事実を反映している。

- **1.11.0** PyPI で公開：リポジトリをクローンせず、`pip install ai-powered-markdown-translator` に続いてコマンド `aipmt` を実行（2026-09-03）：

  - **単一ファイルのスクリプトがインストール可能なパッケージになった。** `translate.py` をルートから `src/aipmt/translate.py` へ移動し、コンソールエントリーポイント `aipmt` と、それに相当する `python -m aipmt` を追加した。コントリビューションには引き続きリポジトリのクローンが必要である。テスト、28言語の翻訳、品質管理ツールはそこに含まれている。しかし、利用するだけならクローンは不要になった。

    - **import 名は `aipmt` であり、決して `translate` ではない。** 実際に衝突が発生し、しかも暗黙だからである。PyPI パッケージ `translate`（v3.8.1、最終アップロード 2026-07-06）は、同名のディレクトリをインストールする。venv 内で再現したところ、ディレクトリがモジュールより優先され、`translate.main` が消え、エントリーポイントは `AttributeError` で壊れた。それでも `pip check` は「壊れた依存関係は見つかりませんでした」と応答し、rc=0 となる。ユーザー環境に単純な `pip install translate` が存在するだけで、有用な診断なしに CLI が壊れるところだった。実際の wheel を使った反証テストでは、そのパッケージの上に `pip install translate` をインストールし、前後とも `aipmt --help` が rc=0 となり、2つの CLI が共存することを確認した。
    - **配布名は長く、コマンドは短く。** `ai-powered-markdown-translator` により、PyPI 検索でパッケージを見つけられるようになる。略称だけでは、プロジェクトをすでに知っている人にしか見つけられないが、公開の目的はまさに新たに見つけてもらうことにある。もっともらしい候補を2つ、検証のうえで除外した。`ai-markdown-translator` は、同じ目的を持ち、このリポジトリより17か月古いツールによって2024年から npm 上で使用済みである。また、`aimt` は同じ分野で活動中のパッケージ `aim`（v3.29.1）と1文字しか違わず、長期的な混同を招く最悪の条件だった。検証方法にも落とし穴がある。`pypi.org/project/<nom>/` はどの名前でも200を返すボット対策ページであり、信頼できるのは JSON API だけである。
    - **フラットなパッケージではなく `src/` レイアウト。** フラットなパッケージなら、テストにある6個の `sys.path.insert(..., "..")` を維持できたが、そこにこそ問題がある。それらはパッケージではなくソースツリーを import するため、パッケージングのあらゆる誤りを覆い隠してしまう。実際のコストは、置換規則が1つ増えるだけである。

  - **キーを一度設定すれば済むようになった。** インストールされた CLI には永続的な設定がまったくなく、環境変数とカレントディレクトリの `.env` しか選択肢がなかった。確かに `find_dotenv` はシステムのルートまで遡るため、個人ディレクトリ配下で作業していれば `~/.env` を検出したが、別の場所で作業すると何も見つからなかった。これは設計上の選択ではなく、コマンドを実行した場所に左右される適用範囲だった。そこで既存の2層の下に、第3層として `~/.config/aipmt/.env` を追加した。

    - **優先順位はコードで明示していない。** `load_dotenv` のデフォルト値である `override=False` から自然に決まる。各層は、前の層で空のままだった値だけを補完する。その結果、環境変数 → プロジェクトの `.env` → ユーザー設定という順序になる。これは構造ではなく動作テストで検証しており、2つの呼び出しの順序を逆にしても、第3層を削除してもテストが失敗する。
    - **TOML ではなく `.env` 形式**を意図的に採用した。`python-dotenv` はすでに依存関係に含まれ、その構文は15個の README ですでに文書化されており、同じファイルを両方のスコープで使用できる。新しい依存関係も構文も増えない。保存場所は、`XDG_CONFIG_HOME` が**絶対パス**の場合にそれに従う。仕様では相対値を無視するよう求めている。そうしなければ、設定場所が再びカレントディレクトリに左右されるからである。Windows では `APPDATA` に従う。
    - **2つの選択肢を理由とともに除外した。** システムのキーチェーン（`keyring`）はデスクトップ環境ではより安全だが、ヘッドレス環境――サーバー、コンテナ、CI――では機能しない。つまり、バッチ翻訳という主要な用途に合わない。明示的な選択肢としては適切だが、デフォルトには不向きである。`--api-key` フラグでは、キーがシェル履歴に残り、`ps` から見えるようになってしまう。
    - **キーがない場合、呼び出しトレースを表示しなくなった。** 以前は `site-packages` を指す Python スタックトレースと、「環境または .env」とだけ述べ、後者をどこに作成すべきか示さないメッセージが表示されていた。現在は3つの保存場所を正確なパスとともに列挙し、コマンドは終了コード2で終了する。セーフティネットの範囲は**意図的に狭い**。設定フェーズだけを `except ValueError` で囲む。実行全体を包めば、翻訳中に発生した本物のバグまで安心させるようなメッセージに変換されてしまう。このリポジトリが追跡している障害形態そのものである。これを禁止するため、テストで `main()` のソースを読み取っている。

  - **修正――ツールをインストールすると、ユーザーの `.env` が無視されていた。** 引数なしの `load_dotenv()` はカレントディレクトリからではなく、呼び出し元ファイル、つまり `site-packages` から上へ探索する。独自の `.env` を持つプロジェクトから実際のコンソールエントリーポイントを起動して測定したところ、`find_dotenv()` は `''` を返してキーを読み込まなかったが、`find_dotenv(usecwd=True)` はキーを検出した。ツールがクローン済みリポジトリ内からしか実行されていなかった間は存在しなかった不具合だが、公開後は常に発生し、設定が正しいにもかかわらず API キーが「見つからない」ことだけが症状になるところだった。

  - **3つのゲートは、何も検証しなくなっても成功表示になり得た。** 意図的に、移動の**前に**厳格化した。検出対象の変更後に書かれたガードでは、何も証明できないからである。各ゲートは元のリポジトリでは成功し、移行したコピーでは失敗する。両方向を実測済みである。
    - **Lizard は存在しないパスを何も通知せず無視する**：rc=0、「0 file analyzed」。複雑度ゲートの対象が 158 関数 / 2247 nloc から 3 関数 / 34 nloc に減少し、出力はゼロバイトになっていた可能性がある。スコープは現在、各エントリの存在が確認される配列になっている。
    - **存在しないモジュールに対する `coverage run --source=` は失敗しない**：警告は stderr にのみ出力され、unittest でも `coverage xml` でも rc=0 となり、レポートもそのまま公開されるが、対象は 1453 statements から 141 statements に激減する。ほぼ何も解析されていないため、プロジェクトが健全に見えていた可能性がある。レポートを保護するため、合計値と測定対象の最大ファイルという 2 つの下限を設けた。
    - **翻訳の鮮度プローブは、呼び出し形式を構造的に検出できない**：このプローブは argparse のフラグを基準にしており、ファイル名を変更してもそこは変わらない。再現結果：モジュールを移動しても、15 個の README は依然として存在しないコマンドを記載していたが、判定は「古い翻訳なし」となった。そのため、第 7 セクションではオプションではなく形式を検証し、Lizard フックをスクリプトの実際のスコープと照合するようにした。その `files:` キーは、一致しなくなっても pre-commit を失敗させず、フックをスキップさせるためである。

  - **`requires-python = ">=3.10"` は単なる主張ではなくなった。** `sonar-project.properties` は以前から 3.10～3.12 を掲げていたが、開発環境には 3.12 しかなく、実際には一度も検証されていなかった。公開すれば、この内部矛盾まで公になるところだった。現在はテストワークフローで 3.10、3.11、3.12 のすべてに対してスイートを実行し、パッケージ自体をインストールすることで、公開されるバージョン境界も検証している。

  - **下限のみで、上限は設けない。** `requirements.txt` は引き続きテスト済みのロックであり、`[project.dependencies]` は公開契約になる。ロックの正確なバージョンを公開すると、ほかのパッケージも使用する利用者の環境で競合を引き起こすためである。`<N+1` の上限も設けない。そうすると、メジャーバージョンへの追随遅延があるたびにリリースゲートを失敗させる `check-deps-fresh.sh` と真っ向から矛盾する。下限の組み合わせで解決し、反証テスト `openai==1.0.0` は `ResolutionImpossible` で終了するため、この検査が何でも受け入れるのではなく、正しく識別していることも証明されている。さらに、`pyproject.toml` のバージョンと CHANGELOG のバージョンが食い違うことをガードで禁止している。PyPI では同じバージョン番号を再利用できないためである。

  - **新規 venv でエンドツーエンド検証済み**：約 70 Ko の wheel には `aipmt/*.py`、dist-info、ライセンスのみが含まれる。`aipmt --help` は 22 個のフラグで rc=0。`python -m aipmt` は「usage: \_\_main\_\_.py」ではなく「usage: aipmt」と表示する。`pipx` によるインストールも正常に機能する。そして何より、**任意のユーザーディレクトリから実際に fr→en 翻訳を実行**し、太字、リスト、インラインコード、リンク、URL が保持され、コードブロックが翻訳されないことを確認した。移行前から存在する 318 件のテストは、前後の識別子一覧がバイト単位で完全に一致した状態ですべて合格している。テストが無効化されていないことを証明するのは「OK」ではなく、この一致である。さらに 3 層構成用のテストが 12 件追加され、合計 330 件となった。

- **1.10.0** Provider `--use_codex`（ChatGPT サブスクリプションのクォータ）、SDK とモデルの更新、複数段落にまたがる news 引用の修正（2026-08-29）：

  - **セキュリティレビュー — PR で導入されたものの、すべての箇所では守られていなかった 2 つの安全策**：

    - **Codex のプリフライトは `.env` 全体をバイナリへ渡していた。** `_codex_preflight` は `subprocess.run` を **`env=` なしで**呼び出していた。そのため、サブプロセスは `os.environ` 全体、つまり `load_dotenv` が読み込んだ `.env` の全内容を継承していた。計測用の偽バイナリで確認したところ、**7 個のシークレット**、すなわち 6 つの provider のキーと 1 つの `GITHUB_TOKEN` がプリフライトに到達していた。一方、対応する `_grok_preflight` は正しく `env=_grok_env()` を渡しており、到達したシークレットは **ゼロ**だった。この不整合は PR 内部に存在していた。数行先にある `_strip_secret_env` は、まさにこの不変条件を守るためのものである。`_codex_env_base()` を抽出して両方の経路で共有するようにした。修正後の測定結果は、両側ともシークレット 0 件である。
    - **「`--deny` はフェイルクローズである」という性質は、実際に使用されていた形式には当てはまらなかった。** コメントでは、不明な接頭辞を持つルールが起動を拒否させることを根拠に、Grok の隔離全体を正当化していた。`grok 1.0.13` で測定したところ、この検証が存在するのは **括弧付き形式のみ**だった。`--deny 'CeciNestPasUnOutil(*)'` は起動を拒否する（「unknown tool prefix」）一方、`--deny 'CeciNestPasUnOutil'` は何の通知もなく受け入れられる。ところが、`GROK_DENY_RULES` は裸の名前しか使用していなかった。そのため、xAI 側でツール名が変更されると、OS sandbox がすでに適用されない環境において、測定済みの唯一の隔離層が何の通知もなく失われる可能性があった。名前付きの 8 つのルールを `Prefix(*)` に変更し、それぞれが CLI の既知の接頭辞として検証されるようにした。包括ルール `*` は、唯一受け入れられるリテラル形式のまま維持する。検証されない形式への逆戻りをテストで防止している。
    - **そのほかの点も問題がないことを確認済み**：コマンドインジェクションはなく（全箇所でリスト形式を使用し、`shell=True` は一度も使用せず、文書内容は stdin または `--prompt-file` 経由）、安全でないデシリアライズもない（`json.loads` のみを型ガード付きで使用）。パストラバーサル修正については 7 種類のペイロードで回避方法が見つからず、`--deny '*'` が CLI によって実際に適用されることも確認した（workdir 外の読み取りで `DENY_ENFORCED` を観測）。
    - 前述の鮮度チェックは、ついでに自身の原則も迂回していた。PyPI へのリクエストが失敗したパッケージを何も通知せずスキップし、ゲートを成功扱いにしていた。現在は実際に比較したパッケージ数を数え、網羅率が不完全なら失敗する。

  - **依存関係を最新化し、再び更新が滞らないように 2 つの安全網を追加**：

    - **遅延は現実に存在し、長期間続いていた**：`openai` 2.54 → **3.6.0**、`anthropic` 0.125 → **1.2.0**、`certifi` 2024.8.30 → **2026.7.22**。すべての provider 呼び出しにおける TLS 検証用のルート証明書ストアが 2 年遅れていたことになる。特定された原因は、**`.github/dependabot.yml` が存在しなかったこと**である。このファイルがない場合、GitHub が有効にするのは _セキュリティ更新_ のみであり、Dependabot は CVE の対象となる依存関係に対してしか PR を提案しない。これにより、`urllib3` と `idna` は更新された一方、2 つの SDK がメジャーバージョン単位で遅れたままになっていた理由が説明できる。
    - **以前の推論で懸念されていたのとは異なり、2 つのメジャーバージョンは競合せず共存する**：`openai` 3.x と `anthropic` 1.x は **`httpx2`** に移行する一方、`mistralai` と `google-genai` は `httpx<1` を引き続き使用するが、これらは別々のディストリビューションである。実際のインストールで確認し、さらに **7 つの provider 経路をエンドツーエンドでテスト**した。対象は OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI、Grok CLI であり、各出力でインラインコードとリンクが保持された。「HTTP スタックを 2 つにしない」というのは好みであって、阻害要因ではなかった。測定によって決着がついた。
    - **`requirements.txt` は実際の環境を表していなかった**：`google-auth`、`cryptography`、`opentelemetry` スタックは作業用 venv にインストールされていたが、一度も宣言されていなかった。そのため、新規インストールではテスト環境を再現できなかった。反対に、`tokenizers`、`huggingface-hub`、`PyYAML` は、どこからもインポートも要求もされていないにもかかわらず記載されており、`mistralai` 1.x の残骸だった。このファイルは、直接依存関係のみから構築した venv の完全な依存関係閉包として再生成された。新しい依存関係セットでは、`pip-audit` により既知の脆弱性は検出されていない。
    - **`.github/dependabot.yml`**（新規）は、pip と github-actions のバージョンを毎週更新する。マイナー更新とパッチ更新は 1 件の PR にまとめる。パッチ更新ごとに PR を作成すると、いずれ無視されるようになり、過剰な通知は更新の妨げになるためである。**メジャー更新は個別**とし、それぞれ実際の呼び出しによる検証を必須とする。
    - **`scripts/check-deps-fresh.sh`**（新規、ゲートに接続済み）は、更新の遅れをプロジェクトの判定結果に表出させる。Dependabot は提案するだけで保証はせず、その PR が積み上がる可能性もある。メジャーバージョンの遅れは失敗、マイナーバージョンの遅れは警告とする。常時赤いゲートはいずれ無視されるためである。PyPI に接続できない場合、ローカルでは明示的にスキップし、**CI ではフェイルクローズ**にする。実行されなかった検査は成功ではない。修正前の状態そのもの（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`）を検出し、マイナーバージョンの遅れでは警告だけになることを両方向で確認した。

  - **この PR のレビューから生まれた修正** — 5 つのレビューエージェントが差分を詳細に精査した。以下の各項目はすべて、修正前に**測定によって再現**され、そのうち 2 件は同じバージョンの前段で導入されたリグレッションだった。
    - **回帰修正 — `_NEWS_CITATION_REGEX` で指数的バックトラッキングが発生していました。** 複数段落対応の修正により、繰り返し内へ `(?:[ \t]*$|[ \t]+.*)` が導入されていました。`[ \t]+` と `.*` の間で空白の分担が曖昧になり、その曖昧さが反復のたびに増大していました。パターンに一致しない、完全に正当な Markdown インデントである `>   texte` の行を使って計測したところ、**14 行で 2,589 ms**、修正後は 0.04 ms で、行を追加するごとに約 9 倍増加していました。`--news` モードでは、長く不適合な blockquote が 1 つあるだけで、原因を特定できないままジョブの timeout まで翻訳が停止していました。現在は繰り返しが行全体を一続きで消費するため（`\n^>(?![ \t]*—).*`）、各反復で一致方法が 1 つしか残りません。実際の 231 記事の corpus で検証済みです。capture の差異は**ゼロ**、引用は同じ 423 件で、14 件の複数段落本文は引き続き拡張されています。
    - **2 つの provider flag を同時に指定すると、警告なく従量課金されていました。** `--use_codex --use_mistral` は受け入れられていました。`_select_provider_client` は最初に Mistral を確認し、`_resolve_provider` は明示的な boolean を優先するため、どちらも Mistral に収束していました。そのためユーザーは subscription quota の利用を要求しているにもかかわらず、何の警告もなく従量課金されていました。これはまさに `--use_codex` が防止するために存在する障害モードです。6 つの provider flag は、すべて `add_mutually_exclusive_group` を経由するようになりました。**動作変更**：従来は警告なく受け入れられていた、2 つの provider を組み合わせたコマンドラインが、今後は `argument --use_mistral: not allowed with argument --use_codex` で失敗します。
    - **作業完了 gate は、probe が異常終了しても green になっていました。** `scripts/check-release-ready.sh` の 13 件の検証のうち 4 件は、「stdout を取得し、空なら結論を出す」というパターンに従い、return code を一度も確認していませんでした。例外（ファイル名の変更、`FileNotFoundError`）は stderr に書き込み、stdout を空のままにしたため、検証は「問題なし」と結論づけていました。「`exit 0` だけでは何も証明できない」という罠が、それを防ぐために書かれた script 内で再現されていたのです。現在は helper `probe()` が、return code が 0 であること**および**終了 sentinel の両方を必須とし、probe は目印の集合が空の場合には結論を出しません。空集合に対する assertion は常に真になるためです。実証例として、上記の排他的 group を追加すると provider flag が `*_group` object を経由するようになり、従来の regex `parser\.add_argument\(` では一致しなくなりました。その結果、**21 flag 中 6 flag** が警告なく対象範囲から外れても、gate は green のままでした。
    - **secret scan は 6 provider 中 4 provider を見逃していました。** character class `[A-Za-z0-9]` はハイフンを除外していたため、`sk-proj-…`（現在の OpenAI 形式）と `sk-ant-api03-…` は 2 つ目のハイフンで途切れ、`AIza…` は対象外でした。パターンを拡張し、`.secrets.baseline` は scan から除外しました。さらに guard `.env` は `git diff --cached` を照会していましたが、これは index しか参照しません。そのため、最悪のケースである**すでに commit 済み**の `.env` は一切表示されませんでした。現在は `git ls-files` を照会します。
    - **Codex の「token warm-up」は warm-up ではありませんでした。** 計測の結果、`codex login status` は `~/.codex/auth.json` に触れておらず、mtime とサイズも変化しませんでした。また、その help には「Show login status」と記載されています。それにもかかわらず、comment では token を「一度だけ、逐次的に」refresh し、1 回限りの rotating token に対する同時 refresh のリスクを無効化すると説明していました。宣言されていた保護は存在しなかったため、comment は現在、code が実際に行うことを記述しています。実際の対策は引き続き `max_jobs=4` です。また、この check は以前無視していた `CODEX_BIN` も尊重するようになりました。`PATH` に `codex` がない端末では、「未認証」という誤解を招く診断で失敗していました。
    - **`.env` は subshell 内で source されていました。** `detect_provider` は command substitution 内で呼び出されるため、その export は親 shell に反映されません。その結果、`.env` で定義された `GROK_BIN`、`GROK_HOME`、`REGEN_MODEL` は、`main()` 内での読み取りから見えず、正しい設定でも「Grok binary が見つからない」と結論づけていました。
    - **同時実行数が公称上限を 50% 超えていました。** guard は README/CHANGELOG の組を起動した後に配置されていたため、`max_jobs=2` に対して計測された peak は **3** でした。週次 quota が Chat/Imagine/Voice と共有され、計測できない Grok では、script が自ら課した上限を守れていませんでした。また、最終的な件数は表示されるだけで、28 と比較されることはなく、ファイルが欠落しても見逃されていました。
    - **Grok の出力 contract：`stopReason` がなければ、今後は失敗します。** 公表されている contract が `end_turn` を要求しているにもかかわらず、code は「`end_turn` **または欠落**」を適用していました。field のない payload、または CLI の更新で field 名が変更された payload により、guard が警告なく no-op になっていました。また、`max_turn_requests` は rate limit として分類されなくなりました。これは turn budget の枯渇であり、retry しても 90 秒待った末に同じ結果を再現するためです。さらに `quota` は rate limit marker から除外されました。`_codex_is_rate_limited` の docstring がすでに示していた理由を、Grok 側では適用していなかったためです。
    - **Gemini cascade は model ごとに memoize されるようになりました。** 従来は segment ごとに `minimal` から再開していましたが、default model はこれを拒否します。そのため通常経路でも segment ごとに 400 の往復が発生し、同じ警告を繰り返し表示していました。何百回も繰り返される warning は読まれなくなり、やがて情報を覆い隠すものになります。
    - **その他**：CI での拒否 message は Codex 用に hard-code されており、`--use_grok_cli` のユーザーを `XAI_API_KEY` ではなく `OPENAI_API_KEY` へ誘導していました。`provider.capitalize()` は「Grok_cli」と「Openai」を表示していました。subprocess 基盤の comment は「shim」を両方の CLI に一般化していましたが、Grok binary は native ELF です。正しい理由は「独自の subprocess を spawn する agent」です。`subprocess` に関する 12 件の SAST finding は、根拠とともに `# nosec` / `# nosemgrep` として記録しました。`shell=True` を使用しない list 形式のため injection は不可能であり、document の内容が argv を通過することもありません。
    - **agentic subprocess に secret が入ることはなくなりました。** 名前を列挙する deny-list は、**課金**に関する invariant（`OPENAI_API_KEY` なしの Codex、`XAI_API_KEY` なしの Grok）しか保護していませんでした。計測すると、**ほかに 7 つの secret** が各 subprocess に入っていました。Anthropic、Mistral、Google、Gemini の key、もう一方の CLI の key、そして secret ではないものの traffic の送信先を変える `OPENAI_BASE_URL` です。しかし、この 2 つの CLI は**agent**であり、Grok は多くの Linux 端末で適用可能な OS sandbox なしに動作します。現在の filter は名前の列挙ではなく、**名前のパターン**（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`）に基づきます。そのため、この code が把握していなくても、ユーザーが `.env` に追加した variable まで対象になります。これらはどれも CLI には不要です。認証情報は `~/.codex` と `~/.grok` にあり、environment には存在しません。強化した environment で両 provider をそれぞれ使用し、**実際の翻訳が正常に完了すること**を確認済みです。
    - **テスト**：新しいファイル `tests/test_review_hardening.py`（21 tests）により、provider flag の排他性、`stopReason` contract、news regex の線形性、CI での拒否 message、Gemini の memoization、および subprocess environment に secret が一切存在しないことを固定しました。最後の assertion は**汎用的**であり、どの list にも記載されていない key でも失敗します。一方、既存の除去テストは自身の constant を鏡写しにしたもので、自身の loop の故障以外は何も検出できませんでした。完全な suite は **311 tests** です。

  - **2 つの新しい Grok provider**：`--use_grok`（xAI API、key は `XAI_API_KEY`、従量課金）と `--use_grok_cli`（公式 Grok Build CLI、Grok subscription から消費。`--use_codex` と同じ原則）です。
    - **API mode、約 40 行**：xAI endpoint は OpenAI 互換のため、client と `_call_openai` はそのまま再利用し、変更されるのは `base_url` だけです。必要だった変更は 1 点だけで、すべての provider に恩恵があります。`finish_reason` は、OpenAI が `stop` を返す箇所で xAI が返す形式 `end_turn` も受け入れるようになりました。model は `grok-4.6`（品質）と `grok-4.3`（エコ）です。ただし Grok のエコ model は repository 内で依然として最も高価で、100 万 token あたり $1.25/$2.50、`mistral-small-latest` は $0.15/$0.60 です。この provider は価格ではなく、model の多様性を目的に選択するものです。
    - **CLI mode**：Codex を基にしていますが、実環境上必要な 4 つの相違点があります。prompt はファイルで渡します（`--prompt-file`。CLI は stdin を読み取らず、segment を argv に入れると `ps` に表示されるため）。出力は stdout 上の単一 JSON object です（JSONL でも `-o` ファイルでもありません）。subscription で利用できるのは `grok-4.6` と `grok-4.5` だけです。また、sandbox は適用できません（下記参照）。subprocess 起動処理は Codex とともに `_codex_run_process` へ共通化し、すでにテスト済みの Codex provider の残りの部分には触れていません。
    - **`exit 0` は何も証明しないことを計測で確認**：未認証でも、CLI は return code **0** で `{"type":"error","message":"Not signed in."}` を **stdout** に書き込みます。拒否や turn 超過でも同様です。そのため出力 contract では、return code が 0、error payload がない、`stopReason == end_turn` がある、text が空でない、という 4 条件を同時に満たす必要があります。preflight も同じ論理に従います。`grok models` は logout 状態でも 0 で終了し、stdout に「not authenticated」が存在する場合にのみ未認証と判断できます。
    - **confinement：非対称性を意図的に採用し、文書化しました。** Codex は `--sandbox read-only` で動作しますが、Grok の sandbox は、`sudo` なしには回避できない 2 つの独立した system 上の理由により、近年の多くの Linux 端末では適用できません。Ubuntu 24.04 以降では AppArmor が非特権 user namespace を阻止し（`bwrap: setting up uid map: Permission denied`、Grok 外でも再現）、container runtime socket の deny-list は `/run/podman` が `0700` の場合に失敗します（resolver が回復できるのは `ErrorKind::NotFound` だけで、EACCES は fatal になります）。中心的な罠は、適用できない**組み込み** profile が、警告なく非 confinement 状態で起動することです。そのため script は default では profile を一切要求せず、警告なく fallback することもありません。stderr に警告を表示します。保護は CLI の `--deny` rule に依存し、catch-all の `*` も含みます。これは計測上、唯一の _fail-closed_ layer です（未知の prefix を持つ rule があると起動を拒否します）。`GROK_TRANSLATE_SANDBOX=read-only` を使用すると sandbox を必須にでき、その場合、端末が要件を満たせなければ起動に失敗します。
    - **guardrail**：`XAI_API_KEY`、`GROK_API_KEY`、`GROK_SANDBOX` は subprocess environment から除去されます（key があると従量課金へ切り替わり、継承された `GROK_SANDBOX` は適用不能な profile を誤解を招く message とともに強制するためです）。MCP/hooks/skills/agents の switch は無効化し、`--disable-web-search`、`--no-subagents`、`--no-plan`、使い捨て workdir、CI での拒否、process group を終了する timeout、rate limit 時の back-off を備えています。`--max-turns` は 1 ではなく 6 に固定しています。counter は tool turn の後に increment されるため、1 では出力が途中で切り捨てられます。
    - **quota**：Grok の pool は週次で、**Chat、Imagine、Voice と共有**されます。また、それを表示する command はありません。`account/rateLimits/read` により消費量を算出できる Codex とは異なります。そのため `regen_translations.sh` は同時実行数を 2 に制限し、明示的に警告します。
    - **テスト**：新しいファイル `tests/test_grok_provider.py`（24 tests）。完全な suite は **290 tests** です。
  - **バグ修正 — 複数段落にわたる英語の引用が一部しか保護されていませんでした（`--news` mode）**：`_NEWS_CITATION_REGEX` は引用本文として、**連続する** `>` 行だけを受け入れていました。引用が複数の段落にまたがる場合（空の `>` 行で区切られる場合）、最後の段落だけが capture されて placeholder に置き換えられ、それ以前の段落は LLM に送られて翻訳されていました。これは `--news` が保証するために存在する動作と正反対です。現在、繰り返しは内部の空の `>` 行を受け入れ、non-greedy になりました。これにより、最初に現れる空行ではなく、italic 行の直前にある空の `>` で停止します。
    - **計測した規模**：実際の 198 記事の corpus では、419 件中 11 件の引用が該当しました。回帰はありません。新しい regex が capture する引用数はまったく同じで、複数段落の本文だけが拡張されています（408 本文は同一、11 本文が拡張）。attribution 行 `> — …` は、保持された lookahead により引き続き本文へ取り込まれません。
    - **end-to-end の証明**：69 ko の記事を ja/ar に翻訳しました。以前は引用の最初の段落が日本語では `> GLM-5.3がオープンウェイト化。` となり、アラビア語でも同様に翻訳されていましたが、今後は `> GLM-5.3 is now open-weight.` のまま保持されます。英語の引用行数は 9 から 10 に戻り、source と一致します。
    - なお、この不具合は downstream validator では検出されませんでした。validator は引用の存在を確認するだけで、完全性までは確認していなかったためです。
  - **default provider で計測された節約**：model 名が `gpt-5` で始まる場合、`_openai_extra_kwargs` は `--eco` でも `reasoning_effort="medium"` を送信していました。10 語の文を翻訳する `gpt-5.4-mini` で計測すると、`medium` では reasoning token が 45、出力 token が 65 でしたが、`none` では 0 と 14 でした。翻訳に reasoning は何も寄与せず、各ファイルの各 segment で費用が発生していました。default は `--eco` では `none`、それ以外では引き続き `medium` になります。CLI で明示的に渡された値は、引き続き優先されます。`--reasoning_effort` は `low`/`medium`/`high` に加えて、`none` と `xhigh` も受け入れるようになりました。すべての model がすべての値を受け入れるわけではありません。たとえば `minimal` は `gpt-5.4-mini` に拒否されますが、既存の parameter なし retry がこの場合に対応します。
  - **SDK の更新と Gemini migration**：`google-generativeai`（support は 2025-11-30 に終了し、repository は archive 済み）を、統合 SDK **`google-genai`** に置き換えました。`genai.Client(api_key=...)`、次いで `client.models.generate_content(model=, contents=, config=)` を使用し、system prompt は segment に連結せず `system_instruction` として渡します。`mistralai` は **2.9.4** へ更新しました（import は `from mistralai.client import Mistral` になります。旧形式は `ImportError` を送出することを wheel 内で確認済みです）。`anthropic` は **0.125.0**、`openai` は **2.54.0** へ更新しました。venv 内に 2 つの HTTP stack を共存させないため、いずれも `httpx2` への移行前の最終 version です。これに伴い、`httpx` 0.28.1 と `pydantic` 2.13.5 の固定も解除しました。
  - **document ではなく実際のテストで検出された 2 つの回帰**：
    - `anthropic` ≥ 1.0 は、`max_tokens` から 10 分超と予測される非 stream call を client 側で拒否します（`ValueError: Streaming is required...`）。この guardrail は 0.34.2 には存在せず、`max_tokens=32768` を使うすべての Claude call を破壊していました。明示的な `timeout`（`CLAUDE_TIMEOUT`、default 900 s）で修正しました。これにより、完全な response だけを利用する call を streaming に切り替えずに済みます。
    - `thinking_level="minimal"` を受け入れるのは Gemini catalog の一部だけです。`gemini-3.1-flash-lite` は対応していますが、`gemini-3.7-flash` と `gemini-3.1-pro-preview` は 400 で拒否します。そのため `_gemini_generate_with_fallback` として、既存の OpenAI fallback と同様に `minimal` → `low` → thinking_config なし、という cascade を導入しました。最適化 parameter が原因で翻訳を失敗させてはならないためです。
  - **default model を刷新**し、すべて実際の call で検証しました。OpenAI は `gpt-5.5` → **`gpt-5.6-terra`**（28 件の batch で −60%）、`gpt-5.4-mini` → **`gpt-5.6-luna`**（−73%）。Claude は `claude-sonnet-4-6` → **`claude-sonnet-5`**（より安価で新しい）、`claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（日付なしの canonical ID）。Gemini は `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**、`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（stable version で、`3.5-flash-lite` より安価）です。
 Mistral は変更なしで、4つの中では引き続き `mistral-large-latest` が最もコストパフォーマンスに優れています。注意：`gemini-3.1-pro-preview` より新しい Pro クラスの Gemini モデルは存在しません。2026年5月に発表された Gemini 3.5 Pro は結局リリースされず、3.5/3.6/3.7 系列は Flash 専用です。
  - **Gemini 切り替え前に測定した A/B テスト**：`README.md` を `gemini-3.1-pro-preview`、次に `gemini-3.7-flash` で日本語に翻訳。構造は完全に同一（リスト21件、コードブロック18個、HTML リンク13件、画像13点、すべての URL を保持）で、所要時間は **48秒に対して8秒** でした。この2つのモデルについて翻訳または非ラテン文字の処理能力を比較した公開ベンチマークはなく、切り替えはそうでなければ単なる推測に基づくものになるところでした。
  - **Claude 応答ブロックのフィルタリング**：`_call_claude` は型をフィルタリングせずに `block.text for block in response.content` を実行していました。適応的推論モデル（Sonnet 5 以降）は `thinking` ブロックを挟みますが、これは `.text` ではなく `.thinking` を公開するため、最初のセグメントで不透明な `AttributeError` が発生し、翻訳が失敗していました。現在は `thinking`、`redacted_thinking`、`tool_use`、`tool_result` ブロックを除外しています（テキストを保持する未知の型を許容するため、除外リスト方式を採用）。また、テキストブロックを1つも含まない応答では明示的なエラーが発生します。各呼び出しに `thinking={"type": "disabled"}` が渡されるようになりました。
  - **`MODEL_TOKEN_LIMITS` を再同期**：廃止日を過ぎたモデルを削除（`magistral-*` 系列は2026-07-31に廃止、`gemini-2.0-*` は2026-06-01、`gemini-3-pro-preview` は2026-03-09、ならびに `claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。上限を修正：Mistral 128K → **256K**（Large 3 / Small 4 世代）、Gemini 1 000 000 → **1 048 576**（実際の入力上限）、`claude-opus-4-5` 200K → **1M**、`gpt-5.6-*` 系列 400K → **1.05M**。Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest`、`ministral-*` 系列を追加。注意：`translate()` が分割処理を `min(16000, limite)` に制限しているため、これらの上限は引き続き参考値です。

  - **Provider `--use_codex`**：使用量課金の API を呼び出す代わりに、公式 Codex CLI（`codex exec`）を非対話モードで操作する5つ目の Provider。翻訳の使用量は、すでに支払い済みの ChatGPT サブスクリプション枠から差し引かれます。これは OpenAI がこの用途向けに文書化している唯一の方法です。プラン別の提供状況表では、「Codex SDK、`codex exec`、およびスクリプト化可能なワークフロー」が Plus/Pro/Business/Enterprise で利用可能と記載されています。一方、`~/.codex/auth.json` のトークンでは API Platform の呼び出しを認証できません（また、このスクリプトがそれらを読み取ることもありません。認証と更新は引き続き CLI が管理します）。
  - **Codex バイナリを npm だけでなく pip でもインストール可能に**：`_resolve_codex_binary()` は、`CODEX_BIN`、次に `PATH`、その後 OpenAI が公開する公式 Python パッケージ **`openai-codex-cli-bin`**（`openai-codex` SDK の依存関係）からバイナリを探します。したがって、Python プロジェクトで `--use_codex` を使用するために、npm のグローバルインストールは不要になりました。このパッケージは `requirements.txt` には追加していません。バイナリのサイズが約250 MBあり、任意の Provider のためにすべてのユーザーへ負担させることになるためです。エンドツーエンドで検証済みです。`codex` が `PATH` に存在しない状態でも、解決処理はパッケージ内のバイナリを見つけ、完全な翻訳が6秒で完了します。
  - **「サブスクリプションモード」の保証**：`OPENAI_API_KEY` と `CODEX_API_KEY` はサブプロセスの環境から削除されます。この保護がない場合、`.env` に存在するキーによって、目に見える通知なしに Codex が使用量課金へ切り替わる可能性があります。これはまさに、この Provider が回避するために存在する事態です。
  - **CLI の落とし穴をテストで封じ込め**：
    - `codex exec` は、プロンプトを引数として渡した場合でも stdin を**読み取ります**。stdin を閉じないと、モデルを一度も呼び出さないままコマンドがタイムアウトまで待機します（再現結果：180秒後に終了コード124、出力0バイト）。したがって、`communicate(input=...)` は必須です。
    - npm でインストールされた `codex` は、実際の Rust バイナリを `spawn` する Node の shim です。このバイナリは Python プロセスの**孫プロセス**であり、`subprocess.run(timeout=)` の `SIGKILL` 後も生き残り、そのままクォータを消費し続ける可能性があります。そのため `Popen(start_new_session=True)` と `os.killpg` を使用しています。
    - CLI は `turn.failed` を出力していても、終了コード0で終了することがあります。戻り値コードに加えて JSONL 出力（`--json`）も検査し、終了コードが0でも `-o` ファイルが存在しない場合は、空のセグメントを生成せず明示的なエラーを発生させます。
  - **レート制限時のバックオフ**：CLI は内部でリトライを一切実装していません（`max_retries = 0`）。分類は部分文字列ではなく、JSON ペイロードの構造（`status: 429` / `error.type`）に基づいて行います。「quota」という単語は、回復可能な 429 にも恒久的な `insufficient_quota` にも現れるためです。
  - **CI の保護**：`CI` または `GITHUB_ACTIONS` が定義されている場合、`--use_codex` は拒否されます。サブスクリプションによる認証は共有 Runner 向けではなく、OpenAI も公開リポジトリでこのワークフローを使用しないよう明示的に推奨しています。
  - **モデル**：`gpt-5.6-sol`（品質重視）と `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` 系列は CLI と API Platform で共通ですが、ChatGPT アカウントですべてを利用できるわけではありません。許可リストはローカル検証なしでサーバー側に適用され、一般的でないモデルを指定すると警告が表示されます。Plus プランでは、5時間の枠ごとに Sol が10～100メッセージであるのに対し、Luna は250～2,000メッセージを利用できます。あらゆるバッチ処理には `--eco` が推奨モードです。
  - **修正したバグ — `regen_translations.sh` が完全に成功してもエラー終了していた問題**：`trap ... EXIT` は、`main()` の `local` 変数 `failed_log` を参照していましたが、trap の実行時点ではこの変数はすでに存在しません。`set -u` 環境では、これにより `failed_log: unbound variable` が発生し、28件の翻訳がすべて正しく完了していてもスクリプトが終了コード1で終了していました。その結果、最もコストのかかる再生成直後の段階で `release.sh --auto`（`set -e`）が中断される可能性がありました。変数をグローバルに変更し、trap でその存在を確認するようにしました。有益な副作用として、従来このエラーによって隠されていた実際の翻訳エラーが、終了時の概要に再び表示されるようになりました。
  - **`REGEN_MODEL`**：`regen_translations.sh` の新しい環境変数で、Provider のデフォルトより優先して特定のモデルを強制します。たとえば、処理量重視の `--eco` モデルではなく、サブスクリプション枠の最上位モデルで再生成するために `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol` を指定できます。
  - **`regen_translations.sh`**：明示的なオプトインで `REGEN_PROVIDER=codex` を利用できます（ユーザーに知らせずサブスクリプション枠を消費しないよう、自動検出は一切行いません）。並列処理を開始する前に、トークンを逐次的に一度だけ更新します。Codex の更新トークンはローテーション方式かつ一度限りの使用であるため、ジョブを並行実行すると `codex login` セッションが無効になります。また、並列数は4に引き下げられます。
  - **関連するリファクタリング**：`_dispatch_provider_call` は、処理チェーン全体に4つ目のブール値を伝播させる代わりに、Provider 名を返す `_resolve_provider()` を使用することで、引数を8個から6個に削減しました。最小限の `Namespace` で `translate(..., use_mistral=True)` を呼び出すテストを維持するため、明示的なブール値は引き続き `args` より優先されます。
  - **テスト**：新規ファイル `tests/test_codex_provider.py`（48テスト）で、argv、除外処理済みの環境、前置き禁止契約、無言の失敗、タイムアウトと killpg、バックオフ、事前検査、Provider 解決、Gemini の推論カスケード、Claude のブロックフィルタリング、複数段落のニュース引用を網羅。テストスイート全体で290件です。
  - **実環境での検証**：プロジェクトの `README.md` を Codex で**14言語**に翻訳した結果、参照翻訳と完全に同一の構造になりました（コードブロック14個、見出し24個、表25行、HTML リンク13件、画像13点、URL 19件、コードブロックは文字単位で同一、プレースホルダーの残留ゼロ）。`--news` モードで69 KBのニュース記事を処理したところ、`gpt-5.6-luna` と `gpt-5.6-sol` の出力は、en/ja/ar のすべてで後段のアプリケーション検証を通過しました。`account/rateLimits/read` で測定した消費量は、`--eco` モードで計数器の丸めしきい値未満（5時間枠の0%）に収まりました。

- **1.9.2** 入れ子の括弧またはフランス語接頭辞を含むニュース帰属表示の URL 抽出を修正（2026-05-11）：

  - **修正したバグ**：`_protect_news_quotes` における帰属表示 URL の抽出には、正規表現 `re.search(r"\((.+?)\)", attribution)`（括弧内の遅延キャプチャ）が使われていました。`(relayé par [@user sur X](https://x.com/.../123))` のような帰属表示（入れ子の括弧：外側の `(` と Markdown リンクの `]()`）では、最初に現れた `)` でキャプチャが終了し、文字列が途中で切れ、さらにフランス語接頭辞を含む `relayé par [@user sur X](https://x.com/.../123`（末尾の `)` なし）になっていました。その結果、`_validate_news_post` が翻訳後の出力からこの文字列を探して必ず失敗していました（理由は2つあり、`)` が途中で切れていることと、「relayé par」が `relayed by`/`weitergeleitet von`/… に翻訳されることです）。low → medium → high → gpt-5.5 のカスケード全体が通過できませんでした。
  - **修正**：正規表現を `re.search(r"\]\(([^)]+)\)", attribution)` に変更しました。Markdown リンクの `](url)` を明確に対象とし、**純粋な URL のみ**をキャプチャします（フランス語接頭辞も途中での切断もなし）。翻訳中はプレースホルダー `#URL{N}#` によって不変性が維持されます。問題となっていた次の2つのパターンに対応します：
    - `(relayé par [@account sur X](url))` — 入れ子の括弧
    - `via [@source](url)` または `selon [@author](url)` — 外側の括弧がないフランス語接頭辞
  - **テスト**：`test_silent_failure.py` の `TestNewsCitationExtraction` クラスに2件追加：
    - `test_extract_attribution_url_with_nested_parens`（Genspark CEO E2B のバグを正確に再現したケース）
    - `test_extract_attribution_url_with_french_prefix`（`via` を使用するバリエーション）
  - **カバレッジの不足**：`check-editorial-coverage.py` は編集上の構文を検証しますが、translator で翻訳可能かどうかは検証しません。今後の改善案（v1.9.2 の対象外）として、公開**前**にリスクのあるパターンを検出するため、ドライランで帰属表示の抽出をシミュレートするチェックが考えられます。

- **1.9.1** 翻訳マーカーノート内の CTA ラベルの i18n を修正（2026-05-10）：

  - **修正したバグ**：翻訳済みファイルの上部にあるマーカーバナー内の CTA リンクラベル `[Voir le projet sur GitHub ↗]` が、`target_lang` に従わず、すべての対象言語で**フランス語のまま**になっていました。LLM がこのラベルを見ることはありません（URL とリポジトリの slug を保持するため Python 側で組み立てられます）。そのため、翻訳フェーズで修正することもできませんでした。v1.9 で `marker` 形式を追加して以来の無言のリグレッションです。
  - **修正**：15言語を各言語のローカライズ済みラベルに対応付ける新しい定数 `_VIEW_PROJECT_LABELS` を追加しました。`_translation_note_invariants(target_lang)` と `_assemble_translation_note_paragraphs(phrase, target_lang)` が対象言語を伝播するようになりました。言語が不明な場合は `fr` にフォールバックします（安全対策として KeyError を回避）。
  - **テスト**：`test_source_emits_three_paragraphs_repo_title_description_link` を調整（対象言語 `ja` → 期待される日本語ラベル）。新規テストを2件追加：`test_source_link_label_localized_per_target_lang`（ラテン文字、表意文字、アブジャドを網羅する7言語をパラメーター化）と `test_source_link_label_falls_back_to_french_for_unknown_target`。合計：`test_translation_note_position.py` で40テスト（従来は38）。
  - **後方互換性**：デフォルト値 `target_lang="fr"` を持つシグネチャーにより、`args.target_lang` を指定しない外部のプログラム呼び出し元も変更なしで引き続き動作します。
- **1.9** サイレント障害の修正 + 包括的な品質ツール群 + 複数位置対応の翻訳注記（2026-05-07）：
  - **複数位置対応の翻訳注記 + 「埋め込みカード」マーカー形式**：
    - 新しい CLI オプション（追加のみ、デフォルトは変更なし → **非破壊的**）：
      - `--note_position {top,bottom,both}`（デフォルト：`bottom`）：翻訳済みファイルの上部、下部、または両方に注記を配置します。
      - `--note_format {legacy,marker}`（デフォルト：`legacy`）：
        - `legacy` は v1.8 の動作（太字段落 `**…**`）を**バイト単位で完全に**再現します。
        - `marker` は、非表示の Markdown リンク参照定義（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）に続けて、「GitHub リポジトリ埋め込みカード」風の表示になるよう構成された**3 段落の blockquote**を出力します。内容は、インラインコード内のプロジェクト名（`**\`ai-powered-markdown-translator\`\*\*`）、LLM が翻訳した説明、表示される矢印付きの CTA リンク（`[Voir le projet sur GitHub ↗](URL)`）です。ビルド時に remark プラグインで利用できます（jls42.org のブログ → `remark-translation-banner` プラグインを参照）。
    - **LLM には決して送信されない不変要素**：リポジトリ名と GitHub URL は、説明文の翻訳後に Python 側で組み立てられます。LLM がスラッグ `ai-powered-markdown-translator` や `https://github.com/jls42/...` を見ることはないため、レンダラー、大文字・小文字、スキームのいずれも変更されません。
    - **frontmatter 対応の挿入**：`top` または `both` モードでは、注記は YAML frontmatter の終了 `---` ブロックの**後**に挿入されます（Astro Content Collections / gray-matter の安全性を確保）。ヘルパー `_split_frontmatter` はファイル先頭の `---\n…\n---\n` を検出して完全性を維持します。終了 fence のない未完了の frontmatter では **`RuntimeError` を送出**し、誤った位置に注記を書き込む代わりに、そのファイルを `failed_files` に記録します。
    - **ホワイトリスト方式のモデル名サニタイザー**：`_sanitize_model` は `[A-Za-z0-9._:/-]` に含まれない文字をすべて `_` に置換し、空の場合は `unknown` にフォールバックします。Astro の remark プラグイン側のバリデーターと整合し、マーカー形式を壊す文字（空白、引用符、括弧、コンマなど）を無害化します。
    - **内部リファクタリング**：`_append_translation_note`（1 個のモノリシックな関数）→ 7 個の純粋ヘルパー（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）。ビルダーとコンポーザーを分離し、ビルダーは区切りなしの純粋なブロックを返し、コンポーザーは位置に応じて `\n\n` を適用します。本番処理とソース用ヘルパーは、同じ 3 段落アセンブラーを共有します。
    - **空行を保持する `_quote_lines`**：各行に `> ` を付け、空行は `>` のみに変換します。これにより mdast は、blockquote を改行付きの単一段落ではなく、3 個の異なる段落（タイトル／説明／リンク）として認識できます。
    - **適応型 `_build_translation_note_block`**：LLM が保持した段落数に応じて処理します（3 = 完全なカード形式、2 = 文 + リンク、1 = フォールバック）。Markdown リンク `](` が検出された場合、1 段落のフォールバックでは**リンクを `**...**` で囲まなくなりました**（リンクの周囲に `<strong>` を置くと表示が不安定になるため）。
    - **後方互換性**：`_compose_with_notes` 側で `getattr(args, "note_position", "bottom")` と `getattr(args, "note_format", "legacy")` を使用します。これらの属性を持たない Namespace（既存テスト、外部からのプログラム呼び出し）も変更なしで引き続き動作します。
  - **長文翻訳におけるサイレント障害の修正**：
    - すべてのプロバイダー（OpenAI、Mistral、Claude、Gemini）で翻訳後の言語を検証：決定論的レイヤー（原文の完全一致箇所を検出）+ 確率的レイヤー（`langdetect`）
    - `finish_reason` / `stop_reason` のホワイトリスト：ホワイトリスト外の状態（切り詰め、content_filter など）では必ず `RuntimeError` を送出
    - Claude の `max_tokens`：`4096` → `32768`（16k セグメントで潜在的に発生する切り詰めを回避し、FR→JA/ZH/KO/AR/HI のスクリプト間変換に余裕を確保）
    - 見出し対応のセグメンテーション：セグメント後半の H2/H3 を優先し、各セグメントが意味的に完全なセクションから始まるように変更
    - 非ゼロの終了コードまでエラーを伝播：`translate_markdown_file` は型付きステータス `success` / `failure` / `skipped` を返し、少なくとも 1 ファイルが失敗した場合は `main()` が `sys.exit(1)` を返します（単一ファイルとバッチの両方）
    - すべてのプロバイダーに空コンテンツのガード、原文／出力比率の妥当性検査（500 文字以上で 5% 未満なら拒否）、コード用プレースホルダーの検証（`#CODEBLOCK`/`#INLINECODE`）、LLM 後の正規化（見出しに連結した区切り／リンク）、`reasoning_effort` なしでの `BadRequestError` 再試行を追加
    - 依存関係 `langdetect==1.0.9` を追加
  - **pre-commit 品質ツール群**（「完全な EurekAI 方式」、14 個のフック）：
    - Pre-commit：ruff（lint + format）、shellcheck、prettier（md/yaml/json）、detect-secrets（4 個の API キーを保護）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（空白、EOF、大容量ファイル、shebang など）
    - Pre-push：mypy（段階的な lax モード）、Opengrep SAST（translate.py + scripts/）、pip-audit（初期はレポートモード）、unittest discover（tests/ + scripts/tests/）
    - `./venv/bin/python` を使用するローカルラッパーを `scripts/` に配置
    - `scripts/audit_verdict.py`：11 個の unittest を備えた pip-audit JSON パーサー。jls42-astro のパーサーを Python に移植
    - 初期の ruff 違反 7 件を修正：B904（raise from）×2、B007（未使用の dirs）、C408（dict リテラル）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizard は `translate.py` を一時的に除外（CCN 21～47 の関数が 4 個あり、リファクタリングを予定）。scripts/ には厳格なゲートを適用
  - **SonarCloud + 包括的なカバレッジ**：
    - GitHub Actions ワークフロー `SonarCloud`（sonarcloud.yml + sonar-project.properties）：push と pull-request のたびに分析し、`coverage.xml` でカバレッジを取得
    - README 上部に SonarCloud バッジを 11 個追加（Quality Gate、Security/Reliability/Maintainability の評価、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）
    - `tests/test_silent_failure.py`（`unittest` 標準ライブラリ）：サイレント障害のエラーチェーンを構成する 6 段階を網羅
    - `tests/test_orchestration.py`（テストを 79 件追加）：`translate.py` のオーケストレーション層（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` の TypeError + BadRequestError フォールバック、o1 系列のプロンプト形式、`_validate_translation_output` の早期リターン分岐）を網羅
    - `scripts/tests/test_audit_verdict.py`：`main()`（stdin/stdout）と `if __name__ == "__main__"` ブロックを subprocess 経由でカバー
    - **新規コードのカバレッジ**：75.5% → 約 98%（translate.py 98%、scripts/audit_verdict.py 97%）
  - **テスト**：`tests/test_translation_note_position.py` は位置 × 形式のマトリックス（E2E の `marker+top|bottom|both` と `legacy+top|bottom|both` を含む）、複数行への接頭辞付加、バイト単位で完全一致する後方互換性（固定リテラル）、サニタイザー、frontmatter の分割（未終了の fence での送出を含む）、3 段落形式、2 段落フォールバック、1 段落 + Markdown リンクのガード、およびタイトルと URL が LLM に決して送信されないことを検証する重要なガード `TestLLMPayloadExcludesInvariants` を網羅します。**190 件のテストが成功**し、リグレッションは 0 件です。
  - ドキュメント：`README.md`（フランス語 + 14 言語の翻訳）にバッジを追加、`CLAUDE.md`（pre-commit ワークフロー + CI 監視の詳細）、28 言語の翻訳を再生成
- **1.8** `--news` モード + 2026 年モデルへの更新（2026-03-17、タグ `v1.8`）：
  - デフォルトモデルを更新（2026 年 3 月）：
    - OpenAI 高品質：`gpt-5` → `gpt-5.4`
    - OpenAI 低コスト：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 高品質：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）、および `gemini-3.1-pro-preview`（1M）のトークン上限を追加
  - 初期 `--news` モード：プレースホルダー `#NEWSQUOTE\d+#` による英語の引用保護、`LANG_FLAGS` のマッピング（15 言語）、対象言語別のフラグ管理
  - 復元前に news プレースホルダーを検証（リグレッション：LLM がプレースホルダーを削除すると、引用のない出力が気づかれないまま生成されていました）
  - スクリプト `regen_translations.sh` をポータブル化（絶対パスを使用し、pwd に依存しない）
  - README/CHANGELOG の言語バーにフランス語へのリンクを追加し、28 言語の翻訳を再生成
- **1.7** 新機能：
  - 翻訳時に元のファイル名を維持する `--keep_filename` オプション
  - API キーを自動的に読み込む `.env` ファイルのサポート
  - **インラインコードの保持**：バッククォート（`` `...` ``）が翻訳中に保護されるようになりました
  - システムプロンプトを改善：
    - YAML frontmatter 内の引用符処理を改善
    - テンプレート変数 `{variable}` を保護
    - 要求されていない翻訳者注記を禁止
  - 364 ファイルでテストに成功（jls42.org ブログの移行）
- **1.6** 新機能：
  - 翻訳用 Google Gemini API のサポート（`--use_gemini`）
  - デフォルトモデルを 2026 年版に更新：
    - OpenAI：`gpt-5`（高品質）、`gpt-5-mini`（低コスト）
    - Claude：`claude-sonnet-4-5`（高品質）、`claude-haiku-4-5`（低コスト）
    - Gemini：`gemini-3-pro-preview`（高品質）、`gemini-3-flash-preview`（低コスト）
  - より高速で低コストなモデルを使用する低コストモード（`--eco`）
  - ディレクトリを走査せずに単一ファイルを翻訳（`--file`）
  - 新しい簡素な命名パターン：`{base}-{lang}.md`
  - モデル名を含む従来形式を維持する `--include_model` オプション
  - 一覧にないモデルをデフォルトのトークン上限（128k）でサポート
  - README を 14 言語に翻訳
- **1.5** 改善：
  - **API キーとデフォルトモデルの更新：**
    - **OpenAI：** `DEFAULT_MODEL_OPENAI` から `"gpt-4o"` に更新。
    - **Mistral AI：** `DEFAULT_MODEL_MISTRAL` から `"mistral-large-latest"` に更新。
    - **Anthropic Claude：** `DEFAULT_ANTHROPIC_API_KEY` を追加し、`DEFAULT_MODEL_CLAUDE` から `"claude-3-5-sonnet-20240620"` に更新。
  - **翻訳プロンプトの最適化：**
    - 直接翻訳と翻訳注記のプロンプトを拡充して明確性と効率性を高め、メタデータや特定の書式要素を保持するための詳細な指示を追加しました。
  - **コードのリファクタリング：**
    - Mistral AI クライアントの初期化で `MistralClient` を `Mistral` クラスに置き換えました。
    - 可読性と保守性を高めるため、import を再編成しました。
    - 翻訳時に元の書式を保持できるよう、テキストのセグメンテーションとコードブロックの処理を改善しました。
  - **出力ファイルの管理：**
    - 出力ファイル名内のモデルと言語の順序を入れ替え（例：`f"{base}-{args.target_lang}-{args.model}.md"`）、翻訳ファイルの整理と検索を容易にしました。
  - **その他の改善：**
    - 不要な空行を削除してコードを整理しました。
    - スクリプトの構造と可読性を高めるため、軽微な調整を行いました。
- **1.4** 新機能：
  - 翻訳用 Anthropic Claude API のサポート
  - 明確性と効率性を高めるためのプロンプト最適化
  - コードの保守性を高めるための軽微な調整
- **1.3** 改善と新機能：
  - コードブロックの処理を改善
  - 出力ファイルの管理を改善
  - 既存ファイルの検出を改善
  - 翻訳を強制する `--force` オプション
  - 出力ファイル名内のモデルと言語の順序を入れ替え
- **1.2** changelog の修正
- **1.1** Mistral AI API のサポートを追加
- **1.0** 初期バージョン - OpenAI API をサポート

**gpt-5.6-solでフランス語から日本語に翻訳された記事。**
