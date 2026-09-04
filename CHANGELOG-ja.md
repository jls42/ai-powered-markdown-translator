### 変更履歴

🌍 [Français](CHANGELOG.md) | [English](CHANGELOG-en.md) | [Español](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [Deutsch](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [한국어](CHANGELOG-ko.md) | [العربية](CHANGELOG-ar.md) | [हिन्दी](CHANGELOG-hi.md) | [Italiano](CHANGELOG-it.md) | [Nederlands](CHANGELOG-nl.md) | [Polski](CHANGELOG-pl.md) | [Português](CHANGELOG-pt.md) | [Română](CHANGELOG-ro.md) | [Svenska](CHANGELOG-sv.md)

- **1.12.0** Provider `--use_opencode`：オープンソースエージェントである OpenCode を、ユーザーが選んだ任意のプロバイダーへ接続 — ローカルモデル、アカウント不要の無料利用、サブスクリプション、またはキー（2026-09-04）：

  - **7つの先行プロバイダーとは性質の異なる、8番目の経路。** [OpenCode](https://opencode.ai)（MIT）はモデルプロバイダーではなく、ユーザーが OpenCode 自体で設定したプロバイダーへの _ルーター_ です：API キー、サブスクリプション（GitHub Copilot、ChatGPT、SuperGrok）、**アカウント不要**で無料モデルを提供する OpenCode Zen ゲートウェイ、または **ローカル**モデル（Ollama、LM Studio、llama.cpp）。このスクリプトは Codex や Grok と同様に、非対話モードで `opencode run` を制御し、同じサブプロセス基盤（専用プロセスグループ、タイムアウト時の `SIGTERM` に続く `SIGKILL`、常に閉じた stdin、不要な環境情報を除去）を再利用します。**2つの実際の翻訳**で検証済みです：`opencode/mimo-v2.5-free` によるこの README 全体の英訳 — 49秒、1回の処理、ソースファイルと同一の構造（見出し32個、コードブロック終了26個、リンク18個、URL37個、表の行37行、インラインコード135個）— と、キーを一切使わずローカルで `ollama/qwen2.5:7b` による試験ファイルの翻訳です。

  - **`--model provider/modèle` は必須であり、それは意図的な選択です。** `--model` がなければ、OpenCode は自身のデフォルトに戻ります。初期インストール時のデフォルトは `opencode/big-pickle` で、やり取りが学習に利用される可能性のある「ステルス」無料モデルです — 実測では、このモデルが応答しました。ユーザーの代わりにこれを黙って選ぶことは、このリポジトリが追跡している種類の不可視な切り替えそのものです。そのためエラーメッセージには、モデル一覧を表示するコマンド（`opencode models`）と、3つの例（ローカル、無料、サブスクリプション）が示されます。`--eco` は効果がなく、そのことを明示します。`--reasoning_effort` は明示的な要求があった場合に限り、OpenCode の `--variant` としてそのまま渡されます。

  - **想定ではなく、実測に基づく隔離。** インライン設定（`OPENCODE_CONFIG_CONTENT`。OpenCode のマージ順で最後になるため、ユーザーの設定を置き換えずに優先されます）は、`aipmt` エージェントを定義し、すべてのツールを拒否します（`permission: {"*": "deny"}`）：レジストリはツールをモデルに提示すらせず、「ファイルを一覧表示して `id` を実行して」と指示されたモデルは、ツールを持っていないと応答します。セッション共有は無効化され、外部プラグインは除外され（`--pure`）、`--auto` になることは決してありません。作業ディレクトリは一時的で空です。2つの黙示的な注入を実測して停止しました：`OPENCODE_DISABLE_CLAUDE_CODE` がないと、ユーザーの `~/.claude/CLAUDE.md` が**すべての**プロンプトに入ります（単純な「こんにちは」で入力515トークン、通常は186トークン）；`OPENCODE_DISABLE_PROJECT_CONFIG` がないと、現在のディレクトリの `AGENTS.md` も同様です — 「すべての回答を BANANA で終える」という指示が翻訳に適用されました。一方、グローバルな `~/.config/opencode/AGENTS.md` は引き続き注入されます：それを除外するスイッチはなく、迂回した `XDG_CONFIG_HOME` で回避するとユーザーのプロバイダーまで隠してしまいます。場当たり的に修正するのではなく、文書化しています。

  - **`exit 0` は何も証明しない。3つ目の CLI でも基本姿勢は同じ — ただし固有の落とし穴が2つあります。** 未知の `--agent` は `opencode run` を失敗させません：stderr に警告を出し、**黙って**コーディングエージェントへフォールバックして、ツールを有効にします。したがってインライン設定が反映されなければ、書き込み可能なエージェントで翻訳が実行されます。出力契約では、このメッセージがないことに加え、終了コード0、`error` イベントがないこと、`tool_use` がないこと、最後の `step_finish` が `stop` であること（`length` は途中で切れた応答）、空でないテキストを検証します。2つ目の落とし穴：エラーの JSON イベントは**不透明**です — 「Unexpected server error. Check server logs for details.」という単純な参照だけで、実際の原因（`ProviderModelNotFoundError: Model not found: foo/bar. Did you mean…`、`ProviderAuthError`…）はログにしか存在しません。そのため `--print-logs --log-level ERROR` と、Bun の後続トレースを除いた stderr の `error="…"` フィールドの読み取りが必要です。未知のモデルはこのように、原因を明示しながら1秒で失敗します。さらに `--title` により、不要な LLM 呼び出しも避けられます。これがないと、OpenCode は `small_model` への追加ターンでセッションタイトルを生成します。

  - **シークレット：Codex および Grok と同じパターンベースのフィルタリング。ただし名前付きの例外が1つあります。** `OPENCODE_API_KEY` は保持されます：これは OpenCode 自体のキー（Zen ゲートウェイ、Go サブスクリプション）であり、その名前で OpenCode に渡すものです — `auth.json` に相当し、aipmt が管理したり課金したりするキーではありません。プロバイダーは OpenCode（`opencode auth login`、`opencode.json`）で設定し、aipmt の `.env` では決して設定しません。aipmt のキーがサブプロセスに到達することもありません。サブスクリプション CLI とは異なり、CI で拒否することはありません：API キーやランナー上の自己ホストモデルは正当な用途です。

  - **ディレクトリトラバーサル対策の検査対象が、未加工の値ではなく補間後の値になりました。** `provider/modèle` には `/` が含まれており、1.10.0 の対策では拒否されていました — `--model` がファイル名 `--include_model` に補間されるため、これは正しい挙動です。ファイル名ラベルは、補間前に `/`、`\`、`:` を `-` に置き換えるようになりました（`ollama/qwen2.5:7b` → `ollama-qwen2.5-7b`。`:` は Windows では不正です）。上流の対策はこのラベルを検査します：`../../evil` はターゲット下で単純な名前 `doc-en-..-..-evil.md` になり、`..` 単体は引き続き拒否され、`--target_lang ../x` も拒否されます。境界対策 `_ensure_within_directory` は変更されず、2つ目の層として残ります。

  - **無料モデルとローカルモデルで実測されたこと。** `opencode/mimo-v2.5-free` は段落を16秒、この README を49秒で翻訳しました。`opencode/big-pickle` は200語に40秒かかり、単独ならそれぞれ成功する2つの同時リクエストは、5分間応答がありませんでした。`opencode/nemotron-3.5-lightning-free` は3分間何も返しませんでした。そのため `REGEN_PROVIDER=opencode` と、必須の `REGEN_MODEL`、並列 **2ジョブ**を採用しています。ローカル側では、Ollama がコンテキストを4,096トークンに設定することが多い一方、セグメントは最大16,000文字です。そのため `Modelfile` と `PARAMETER num_ctx 32768` が必要になります。品質はモデル次第です — 7B モデルは試験ファイルでリストの順序を逆にし、コードブロックの終了部分を壊しましたが、ゲートウェイのモデルはすべて保持しました。

  - **レート制限時のバックオフを共通化**（`_retry_on_rate_limit`）しました：Codex と Grok のループは名称以外同一であり、3つ目のコピーを追加すると重複閾値を超えていました。3つの CLI エラーは同じ `_CliCallError` から派生します。共有ループがそのエラーを認識できなくなるため、3つのうちいずれかがそこから外れることを禁止するテストを追加しました。

  - **テスト**：新しい `tests/test_opencode_provider.py` ファイル（51テスト）— 完全な出力契約、エージェントのフォールバック、ログからの原因読み取り、重複したテキスト部分の除去と合成部分の無視、プロセスグループを終了させるタイムアウト、429時のバックオフ、必須かつ検証済みのモデル、シークレットなしのプリフライト、バイナリ解決、ディスパッチの配線、ファイル名ラベル、トラバーサルの反証。`tests/test_review_hardening.py` は、新しいプロバイダーにもフラグの排他性とシークレット不在の検証を拡張します。ゲートが要求する、文書化された argparse フラグは**22個**になりました。全体で**382テスト**です。

- **1.11.1** ドキュメント修正：README がようやく7つのプロバイダー経路を告知（2026-09-03）：

  - **1.11.0 の PyPI ページには「4 APIs + Codex CLI」と書かれていました。** コードが公開するのは7つです — API 経由の OpenAI、Mistral、Claude、Gemini、Grok；従量課金なしのサブスクリプション経由の Codex（ChatGPT）と Grok。Grok の2つのモードが紹介文と _Multi-Provider_ の箇条書きから抜けており、14の翻訳も誤りを繰り返していました。パッケージの長い説明はバージョンごとに固定されるため、表示を修正するにはバージョン番号が必要でした。これがこのリリースの唯一の理由です。**コード変更はありません。**
  - `CLAUDE.md` は公開時に導入された内容と一致しています：ゲートのカウンター（16、`--full` では17）、アクティブな11のワークフロー、`gh pr checks` では見えない2つの Sonar/Codacy カウンター（ホットスポット、Codacy API）、`# nosemgrep` の `ruff-format` による移動、OIDC 交換に必要な GitHub 環境、そして _pending publisher_ は名前を予約しないという事実。

- **1.11.0** PyPI への公開：リポジトリをクローンせず、まず `pip install ai-powered-markdown-translator`、続いて `aipmt` を実行（2026-09-03）：

  - **単一ファイルのスクリプトがインストール可能なパッケージになりました。** `translate.py` はルートから `src/aipmt/translate.py` に移動し、コンソールエントリーポイント `aipmt` とその同等物 `python -m aipmt` を備えます。クローンしたリポジトリは貢献には引き続き必要です — テスト、28の翻訳、品質管理ツールがそこにあるためです — しかし利用するだけなら不要になりました。

    - **インポート名は `aipmt` であり、`translate` では決してありません**。衝突が実際に起き、しかも静かに発生するためです。PyPI パッケージ `translate`（v3.8.1、最終アップロード2026-07-06）は同名のディレクトリをインストールします。venv で再現すると、ディレクトリがモジュールより優先され、`translate.main` が消え、エントリーポイントが `AttributeError` で失敗します。それでも `pip check` は rc=0 で「No broken requirements found」と返します。ユーザー側の単純な `pip install translate` だけで、診断不能な状態で CLI が壊れてしまいます。実際の wheel でも反証済みです：パッケージの上に `pip install translate`、`aipmt --help` は前後とも rc=0 で、2つの CLI が共存します。
    - **長いディストリビューション名、短いコマンド名。** `ai-powered-markdown-translator` なら PyPI 検索でパッケージを見つけられます。略語だけでは、プロジェクトを既に知らない人には見つけられませんが、今回の公開はまさに発見されることを目的としています。妥当そうな候補2つは検証により除外しました：`ai-markdown-translator` は2024年から npm で同じ目的のツールに使用されており、このリポジトリより17か月先行しています。また `aimt` は `aim`（v3.29.1）と1文字違いで、同じ分野の現役パッケージです — 継続的な混同には最悪の構成です。ここで方法上の落とし穴もありました：`pypi.org/project/<nom>/` はボット対策ページのため、どの名前に対しても200を返します。信頼できるのは JSON API だけです。
    - **フラットなパッケージではなく `src/` レイアウト。** フラットなパッケージなら、テストにある6つの `sys.path.insert(..., "..")` を維持できました。しかし、それこそが問題です：それらはソースツリーをパッケージではなくインポートさせ、パッケージングのエラーを隠してしまいます。実際のコストは、置換ルールが1つ増えることです。

  - **キーをついに一度だけ設定できるようになりました。** インストールされた CLI には永続設定がなく、環境変数とカレントディレクトリの `.env` だけが利用可能でした。`find_dotenv` はシステムルートまで遡るため、**ホームディレクトリ配下で作業している場合**には `~/.env` を見つけられましたが、それ以外の場所では何も見つかりませんでした — カバレッジが設計上の選択ではなく、コマンドを起動した場所に依存していたのです。そこで3つ目の層として `~/.config/aipmt/.env` を、既存の2つの層の下に追加しました。

    - **優先順位をコードに直接記述したのではなく、`load_dotenv` のデフォルト値である `override=False` から導かれます**：各層は、前の層が空のまま残したものだけを補います。そのため順序は、環境変数 → プロジェクトの `.env` → ユーザー設定となります。これは構造ではなく動作テストで検証しています — 2つの呼び出しの順序を逆にすると失敗し、3つ目の層を削除しても失敗します。
    - **TOML ではなく `.env` 形式**を意図的に採用しました：`python-dotenv` はすでに依存関係にあり、構文は15の README ですでに文書化され、同じファイルを2つのスコープで使用できるためです。依存関係も新しい構文も増えません。場所は、`XDG_CONFIG_HOME` が**絶対パス**の場合はそれに従います — 仕様では相対値を無視するよう求めています。そうしなければ設定場所が再びカレントディレクトリ依存になるためです — Windows では `APPDATA` です。
    - **2つの選択肢を理由付きで除外しました。** システムキーチェーン（`keyring`）はデスクトップでは安全ですが、ヘッドレス環境 — サーバー、コンテナ、CI — では失敗します。これはバッチ翻訳そのものの用途です。オプトインの候補としては良いものの、デフォルトには不適切です。`--api-key` フラグはキーをシェル履歴に残し、`ps` に表示させてしまいます。
    - **キーがない場合、呼び出し元の痕跡を残さないようにしました。** ユーザーには `site-packages` を指す Python のスタックと、「環境または .env」とだけ記したメッセージが表示され、後者をどこに作るべきかは不明でした。現在は3つの場所を正確なパス付きで列挙し、コマンドは2で終了します。保護範囲を**意図的に狭く**しています：`except ValueError` は設定フェーズだけを対象にします。実行全体を包むと、翻訳中に発生した本当のバグを安心させるメッセージに変えてしまいます — このリポジトリが追跡している失敗モードです。これを禁止するため、`main()` のソースを読むテストを追加しました。

  - **修正 — ユーザーの `.env` は、ツールのインストール後に無視されていました。** 引数なしの `load_dotenv()` はカレントディレクトリからではなく、呼び出し元ファイルから遡ります。つまり `site-packages` からです。独自の `.env` を持つプロジェクトから実際のコンソールエントリーポイントを起動して測定した結果：`find_dotenv()` は `''` を返し、キーは読み込まれませんでした。一方、`find_dotenv(usecwd=True)` はそれを見つけました。ツールがクローンしたリポジトリからのみ実行されていた間は存在しなかったバグです。公開後は恒常的に発生し、正しい設定で API キーが「不足している」とだけ表示されるところでした。

  - **3つのゲートは、何も検証しなくなっていても成功していました。** そのため、移動の**前に**意図的に強化しました。捕捉すべき変更の後に書かれたガードレールは、何も証明しません。各ゲートは元のリポジトリでは成功し、移行後のコピーでは失敗します — 両方向を測定しています。

    - **Lizard は存在しないパスを黙って無視します**：rc=0、「0 file analyzed」。複雑度ゲートは158関数 / 2247 nloc から、3関数 / 34 nloc へと変化してしまい、出力は0バイトになります。現在はスコープを配列にし、各エントリの存在を検証します。
    - **存在しないモジュールに対する `coverage run --source=` は失敗しません**：stderr の警告だけで、unittest でも `coverage xml` でも rc=0、しかもレポートは公開されます — 1453件から141件のステートメントに縮小された状態で。ほとんど分析されなくなったため、プロジェクトは健全に見えてしまいます。レポートを守るため、合計値と、測定された最大ファイルという2つの下限を設けました。
    - **翻訳の鮮度プローブは、呼び出し形式に対して構造的に盲目です**：argparse フラグを基準にするため、まさにファイル名の変更では変化しない部分を見ています。再現すると、モジュールを移動しても15の README は存在しないコマンドを文書し続け、判定は「古い翻訳なし」になります。そのため7つ目のセクションではオプションではなく**形式**を検証し、Lizard フックはスクリプトの実際のスコープと照合されます。そのキー `files:` が一致しなくなっても pre-commit を失敗させず、**スキップ**させるためです。

  - **`requires-python = ">=3.10"` は主張ではなくなりました。** `sonar-project.properties` はすでに3.10-3.12を宣言していましたが、開発環境には3.12しかなく、実際には一度も実行されていませんでした — 公開によって明らかになる内部矛盾です。現在はテストワークフローが3.10、3.11、3.12でスイートを実行し、パッケージをインストールすることで、その公開されている対応範囲も検証します。
- **下限のみで、上限なし。** `requirements.txt` はテスト済みのロックのまま、`[project.dependencies]` は公開契約となる。ロックの正確なバージョンを公開すると、別のパッケージを使用するユーザーとの間で競合が発生するためである。`<N+1` の上限も設けない。これは、メジャーバージョンの遅れがあるとリリースゲートを失敗させる `check-deps-fresh.sh` と正面から矛盾する。下限の組み合わせで解決し、反証用の `openai==1.0.0` は `ResolutionImpossible` となるため、何でも受け入れているのではなく、制御が識別していることが証明される。さらに、`pyproject.toml` のバージョンが CHANGELOG のものと異なることを禁止するガードもある。PyPI では同じ番号の再利用が認められていないためである。

  - **新しい venv で最初から最後まで検証済み**：`aipmt/*.py`、dist-info、ライセンスだけを含む約 70 Ko の wheel；22 個のフラグを伴う `aipmt --help` rc=0；「usage: \_\_main\_\_.py」ではなく「usage: aipmt」と表示する `python -m aipmt`；動作する `pipx` のインストール；そして何より、**任意のユーザーディレクトリから実際に fr→en 翻訳**を実行し、太字、リスト、インラインコード、リンク、URL を保持し、コードブロックを翻訳しないこと。移行前の 318 テストは、前後で識別子のリストがバイト単位で完全に同一のまま通過した。テストを無効化していないことを証明するのは「OK」ではなく、これである。さらに、3 層構成用の 12 テストが加わり、合計 330 となった。

- **1.10.0** Provider `--use_codex`（ChatGPT サブスクリプションのクォータ）、SDK とモデルの更新、複数段落の news 引用の修正（2026-08-29）：

  - **セキュリティレビュー — PR が設けたものの、すべての箇所で維持できていなかった 2 つのガード：**

    - **Codex の事前チェックが `.env` 全体をバイナリに渡していた。** `_codex_preflight` は **`env=` なしで** `subprocess.run` を呼び出していたため、サブプロセスは `os.environ` 全体、つまり `load_dotenv` が読み込んだ `.env` の全内容を継承していた。計測用の偽バイナリで測定したところ、事前チェックに到達したシークレットは **7 個**、6 つの provider のキーと 1 つの `GITHUB_TOKEN` だった。一方、`env=_grok_env()` を正しく渡す対になる `_grok_preflight` では **0 個**だった。この不整合は PR 内部に存在していた。数行隣にある `_strip_secret_env` は、まさにこの不変条件を維持するためのものだからである。共通の `_codex_env_base()` を抽出して両方の経路で共有し、修正後に測定した結果、双方ともシークレットは 0 個となった。
    - **「`--deny` は fail-closed」という性質が、実際に使われている形式を対象としていなかった。** コメントでは、未知のプレフィックスを持つルールが起動を拒否することを、Grok の隔離全体の根拠としていた。`grok 1.0.13` で測定すると、この検証は **括弧付き形式に対してのみ**存在していた。`--deny 'CeciNestPasUnOutil(*)'` は「unknown tool prefix」として起動を拒否するが、`--deny 'CeciNestPasUnOutil'` は黙って受け入れられる。ところが `GROK_DENY_RULES` は裸の名前しか使用していなかったため、xAI 側でツール名が変更されると、測定済みの隔離層が何の通知もなく取り除かれてしまう。しかも OS のサンドボックスがすでに適用されない環境である。名前付きの 8 つのルールは `Prefix(*)` を通過し、それぞれ CLI の既知のプレフィックスであることを検証する。キャッチオールの `*` は、唯一受け入れられるリテラル形式のままとする。未検証の形式に戻ることを防ぐテストも追加した。
    - **その他の点はクリーンに検証済み**：コマンドインジェクションなし（どこでもリスト形式を使用し、`shell=True` は一切使わず、ドキュメントの内容は標準入力または `--prompt-file` 経由）；安全でないデシリアライゼーションなし（`json.loads` のみ、型ガード付き）；7 つのペイロードで迂回を見つけられなかったパストラバーサル修正；そして CLI によって `--deny '*'` が実際に適用されていること（workdir 外の読み取りで `DENY_ENFORCED` を確認）。
    - 上で追加した鮮度チェックも、その原則自体を迂回していた。PyPI へのリクエストが失敗したパッケージは黙ってスキップされ、ゲートは成功していた。現在は実際に比較されたパッケージ数を数え、対象範囲が不完全なら失敗する。

  - **依存関係を更新し、遅れの再発を防ぐ 2 つの仕組みを追加：**

    - **遅れは実際に存在し、長期間続いていた**：`openai` 2.54 → **3.6.0**、`anthropic` 0.125 → **1.2.0**、`certifi` 2024.8.30 → **2026.7.22**。これは、すべての provider 呼び出しの TLS を検証するルート証明書ストアが 2 年遅れていたことを意味する。原因は、**`.github/dependabot.yml` が存在しなかったこと**と特定された。このファイルがない場合、GitHub は _security updates_ だけを有効にし、Dependabot は CVE の対象となる依存関係に対してのみ PR を提案する。そのため `urllib3` と `idna` は更新した一方、2 つの SDK はメジャーバージョンをまたいで古いままになっていた。
    - **2 つのメジャーバージョンは競合せず共存する**。以前の推論が懸念していたこととは異なり、`openai` 3.x と `anthropic` 1.x は **`httpx2`** へ移行し、`mistralai` と `google-genai` は `httpx<1` のままだが、これは別々のディストリビューションである。実際のインストールで検証し、さらに **7 つの provider 経路をエンドツーエンドでテスト**した。OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI、Grok CLI のすべてで、各出力にインラインコードとリンクが保持された。「HTTP スタックを 2 つ避ける」は希望であってブロッカーではなく、測定によって決着した。
    - **`requirements.txt` は実際の環境を記述していなかった**：`google-auth`、`cryptography`、`opentelemetry` のスタックは作業用 venv にインストールされていたが、宣言されていなかった。そのため、新規インストールではテスト対象を再現できなかった。一方、`tokenizers`、`huggingface-hub`、`PyYAML` は venv に存在していたものの、何からも import も要求もされておらず、`mistralai` 1.x の残骸だった。ファイルは、直接依存関係だけから構築した venv の完全な閉包として再生成した。`pip-audit` は新しい構成に既知の脆弱性がないことを報告している。
    - **`.github/dependabot.yml`**（新規）は、バージョン更新、pip、github-actions の週次更新を有効にする。マイナーとパッチは 1 つの PR にまとめる。PR ごとにパッチ更新を 1 つだけ出すと無視され、ノイズは更新の敵になるためである。**メジャーは分離**し、それぞれ実際の呼び出しによる検証を必須とする。
    - **`scripts/check-deps-fresh.sh`**（新規、ゲートに接続済み）は、遅れをプロジェクトの判定に可視化する。Dependabot は提案するだけで保証はせず、PR が積み重なることもある。メジャーの遅れ → 失敗；マイナー → 警告。ゲートが常に赤だと無視されるためである。PyPI に到達できない場合は、ローカルでは明示的にスキップし、**CI では fail-closed** とする。実行されていないチェックは成功ではない。両方向で検証し、修正前の正確な状態（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`）を検出し、マイナーの場合は警告だけを出すことを確認した。

  - **この PR のレビューから生じた修正** — 5 つのレビューエージェントが差分を精査した。以下の項目はすべて修正前に**測定によって再現**され、そのうち 2 つは同じバージョンの上位部分で導入されたリグレッションだった。

    - **修正済みのリグレッション — `_NEWS_CITATION_REGEX` に指数バックトラッキングがあった。** 複数段落対応の修正で、繰り返しの中に `(?:[ \t]*$|[ \t]+.*)` が導入されていた。`[ \t]+` と `.*` の間で空白を共有するため曖昧性が生じ、その曖昧性が反復ごとに増幅していた。パターンに一致しない `>   texte` の行、つまり完全に合法な Markdown のインデントで測定したところ、**14 行で 2,589 ms** だったのに対し、修正後は 0.04 ms となり、1 行追加するごとに約 9 倍になっていた。`--news` モードでは、長くて規格に適合しない blockquote だけで翻訳がジョブのタイムアウトまで停止し、原因も特定できなかった。現在は繰り返しが行全体を一度に消費する（`\n^>(?![ \t]*—).*`）ため、反復ごとの一致方法が 1 つしかない。実際の 231 記事のコーパスで検証し、捕捉結果に**差分はゼロ**、引用は同じ 423 件、複数段落の本文 14 件も引き続き展開されることを確認した。
    - **2 つの provider フラグを同時に指定すると、黙って従量課金になっていた。** `--use_codex --use_mistral` は受け入れられ、`_select_provider_client` は最初に Mistral を検査し、`_resolve_provider` は明示的なブール値を優先するため、両方とも Mistral に収束していた。ユーザーはサブスクリプションのクォータを要求したつもりでも従量課金となり、警告は一切出なかった。これは `--use_codex` が防ぐために存在する、まさに想定された障害モードである。現在、6 つの provider フラグは `add_mutually_exclusive_group` を通過する。**動作変更**：これまで黙って受け入れられていた、2 つの provider を組み合わせたコマンドラインは、現在は `argument --use_mistral: not allowed with argument --use_codex` で失敗する。
    - **終了時ゲートは、プローブがクラッシュしても成功していた。** `scripts/check-release-ready.sh` の 13 個の検証のうち 4 つは、「標準出力を捕捉し、空なら結論する」というパターンに従い、終了コードを一度も確認していなかった。例外（ファイル名の変更、`FileNotFoundError`）が標準エラー出力に書き込まれると、標準出力は空のままとなり、検証は「報告すべきことはない」と結論していた。それを防ぐために書かれたスクリプト自身の内部で、「1 つの `exit 0` では何も証明できない」という落とし穴が再現されていた。現在はヘルパー `probe()` が終了コード 0 **と**終了センチネルの両方を要求し、プローブは手掛かりの集合が空の場合に結論を出さない。空集合に対するアサーションは常に真だからである。実証として、上記の排他的グループを追加した結果、provider フラグは `*_group` オブジェクトを通過するようになり、従来の正規表現 `parser\.add_argument\(` では一致しなくなった。**21 個中 6 個のフラグ**が黙って対象範囲から外れ、ゲートは成功していた。
    - **シークレットスキャンが 6 provider 中 4 provider を見逃していた。** `[A-Za-z0-9]` クラスはハイフンを除外するため、`sk-proj-…`（現在の OpenAI 形式）と `sk-ant-api03-…` は 2 つ目のハイフンで失敗し、`AIza…` は対象外だった。パターンを拡張し、`.secrets.baseline` をスキャンから除外した。さらに `.env` ガードは `git diff --cached` に問い合わせていたが、これはインデックスしか見ないため、**すでにコミット済み**の `.env`（最悪のケース）は一度も表示されなかった。現在は `git ls-files` に問い合わせる。
    - **Codex の「トークンのウォームアップ」はウォームアップではなかった。** 測定によると、`codex login status` は `~/.codex/auth.json` に触れず（mtime とサイズは不変）、ヘルプには「Show login status」と表示される。それにもかかわらずコメントは、トークンを「一度、逐次的に」更新し、使い捨てのローテーショントークンで同時 refresh が発生するリスクを無効化すると説明していた。宣言された保護は存在しなかった。現在のコメントはコードの動作を正しく説明し、実際の対策は `max_jobs=4` のままである。さらにチェックは、無視されていた `CODEX_BIN` に対応する。`codex` が `PATH` にないマシンでは「未認証」となっていたが、これは誤解を招く診断だった。
    - **`.env` はサブシェル内で読み込まれていた。** `detect_provider` はコマンド置換で呼び出されるため、その export は上位に伝播しない。`.env` で定義された `GROK_BIN`、`GROK_HOME`、`REGEN_MODEL` は、`main()` で行われた読み取りからは見えず、正しい構成であっても「Grok バイナリが見つからない」と結論されていた。
    - **同時実行数が宣言された上限を 50% 上回っていた。** ガードは README/CHANGELOG のペアを起動した後に置かれていたため、測定されたピークは **`max_jobs=2` が 3** だった。週間クォータを Chat/Imagine/Voice と共有し、測定できない Grok では、スクリプトが自らに課した上限が守られていなかった。最終カウントは表示されていたものの、28 と比較されていなかったため、ファイルが 1 つ欠けても見逃されていた。
    - **Grok の出力契約：`stopReason` がない場合も失敗とする。** コードは、契約で `end_turn` が要求されている箇所で「`end_turn` **または存在しない**」を適用していた。フィールドのないペイロード、または CLI の更新でフィールド名が変更されたペイロードにより、ガードは黙って no-op になっていた。また `max_turn_requests` は rate limit に分類しなくなった。これは使い果たされたのがターン予算であり、再試行しても結果は同じで 90 秒の待機だけが発生するためである。`quota` は rate limit のマーカーから外した。これは `_codex_is_rate_limited` の docstring がすでに説明していた理由を、Grok が適用していなかったためである。
    - **Gemini のカスケードはモデルごとにメモ化される。** 各セグメントで `minimal` から再開していたが、デフォルトモデルはそれを拒否する。そのため通常経路ではセグメントごとに 400 の往復を行い、同じ警告を再出力していた。警告は何百回も繰り返されると読まれなくなり、こうしてマスクになる。
    - **その他**：CI での拒否メッセージが Codex 用にハードコードされており、`--use_grok_cli` のユーザーを `XAI_API_KEY` ではなく `OPENAI_API_KEY` へ誘導していた；`provider.capitalize()` が「Grok_cli」と「Openai」と表示していた；サブプロセス基盤のコメントが、Grok バイナリはネイティブ ELF であるにもかかわらず、両 CLI に「shim」を一般化していた（正しい根拠は「独自のサブプロセスを spawn するエージェント」）；`subprocess` に関する SAST の 12 件の finding は、`# nosec` / `# nosemgrep` として根拠付きでマークされている。`shell=True` を使わないリスト形式によりインジェクションは不可能であり、ドキュメントの内容が argv を通ることもない。
    - **エージェントのサブプロセスにシークレットが入ることはなくなった。** 名前を列挙した deny-list が保護していたのは、**課金**の不変条件（`OPENAI_API_KEY` なしの Codex、`XAI_API_KEY` なしの Grok）だけだった。測定すると、さらに**7 個のシークレット**が各サブプロセスに入っていた。Anthropic、Mistral、Google、Gemini のキー、もう一方の CLI のキー、そしてシークレットではないがトラフィックを振り向ける `OPENAI_BASE_URL` である。これら 2 つの CLI は **エージェント**であり、Grok の CLI は多くの Linux 環境で適用可能な OS サンドボックスなしに動作する。現在は名前の列挙ではなく、**名前のパターン**（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`）でフィルタリングするため、コードが知らない変数をユーザーが `.env` に追加した場合も対象となる。CLI にこれらは不要である。認証情報は `~/.codex` と `~/.grok` に存在し、環境には決して置かれない。環境を強化した状態で両 provider を通じて**実際の翻訳を成功**させ、そのことを検証した。
    - **テスト**：新しい `tests/test_review_hardening.py` ファイル（21 テスト）で、provider フラグの排他性、`stopReason` 契約、news 正規表現の線形性、CI での拒否メッセージ、Gemini のメモ化、サブプロセス環境にシークレットが存在しないことを固定した。最後のアサーションは**汎用的**で、どのリストにも名前がないキーでも失敗する。一方、既存の expurgation テストは定数の鏡像であり、自分自身のループの故障以外は何も検出できなかった。完全なスイートは **311 テスト**となった。
- **Grokの新しい2つのプロバイダー**：`--use_grok`（xAI API、キー `XAI_API_KEY`、従量課金）と `--use_grok_cli`（公式Grok Build CLI、Grokサブスクリプションの利用枠を消費 — `--use_codex` と同じ仕組み）。
    - **APIモード、約40行**：xAIのエンドポイントはOpenAI互換のため、クライアントと `_call_openai` をそのまま再利用し、変更が必要なのは `base_url` だけです。必要だった適応は1つだけで、すべての利用先に恩恵があります：`finish_reason` は現在 `end_turn` も受け付けます。これは、OpenAIが `stop` を出力する箇所でxAIが出力する形式です。モデルは `grok-4.6`（品質重視）と `grok-4.3`（エコノミー）。なお、Grokのエコノミーモデルはリポジトリ内で依然として最も高価で、100万トークンあたり $1.25/$2.50、`mistral-small-latest` は $0.15/$0.60 です。このプロバイダーは価格ではなく、モデルの多様性を理由に選ぶものです。
    - **CLIモード**：Codexを踏襲していますが、実環境上の4つの相違点があります。プロンプトはファイル経由で渡します（`--prompt-file`、CLIはstdinを読み込まず、argvのセグメントは `ps` に露出するため）。出力はstdout上の単一のJSONオブジェクトです（JSONLでも `-o` ファイルでもありません）。サブスクリプションで利用できるのは `grok-4.6` と `grok-4.5` だけです。また、サンドボックスは適用できません（後述）。サブプロセスの起動はCodexと `_codex_run_process` に共通化し、すでにテスト済みのCodexプロバイダーの残りには手を加えていません。
    - **`exit 0` は何の証明にもならない、実測済み**：未認証でも、CLIは **stdout** に `{"type":"error","message":"Not signed in."}` を書き、終了コードは **0** になります。拒否やターン数超過も同じ挙動です。そのため、出力の契約には4つの条件が同時に必要です。終了コードが0、エラーペイロードがない、`stopReason == end_turn`、そしてテキストが空でないことです。プリフライトも同じ考え方で、オフラインでも `grok models` は0で終了します。判定できるのはstdoutに「not authenticated」が存在する場合だけです。
    - **隔離：非対称性を前提として文書化。** Codexが `--sandbox read-only` で動作する一方、Grokのサンドボックスは、`sudo` なしでは回避できない独立したシステム上の2つの原因により、最近の多くのLinux環境で適用できません。AppArmorはUbuntu 24.04以降、権限のないuser namespaceをブロックします（`bwrap: setting up uid map: Permission denied`、Grok以外でも再現）。また、コンテナランタイムのソケットdeny-listは、`/run/podman` が `0700` の場合に失敗します（resolverが復旧できるのは `ErrorKind::NotFound` だけで、EACCESは致命的になります）。核心となる落とし穴は、**組み込み**プロファイルを適用できない場合、**隔離されていない状態で黙って起動する**ことです。そのためスクリプトはデフォルトでプロファイルを要求せず、黙ってフォールバックすることもありません。stderrに警告を出します。保護はCLIの `--deny` ルール（catch-allの `*` を含む）に依存します。これは実測された唯一の _fail-closed_ 層であり、未知のプレフィックスを持つルールがあると起動を拒否します。`GROK_TRANSLATE_SANDBOX=read-only` を使えば必須化でき、その場合、マシンが適用できなければ起動に失敗します。
    - **安全策**：`XAI_API_KEY`、`GROK_API_KEY`、`GROK_SANDBOX` はサブプロセスの環境から削除されます（キーがあると従量課金に切り替わり、継承された `GROK_SANDBOX` は適用できないプロファイルを要求して誤解を招くメッセージを出すため）。MCP/hooks/skills/agentsのスイッチを無効化し、`--disable-web-search`、`--no-subagents`、`--no-plan`、使い捨てのworkdir、CI環境での拒否、プロセスグループを終了させるタイムアウト、rate limit時のバックオフを設定します。`--max-turns` は1ではなく6に設定します。カウンターはツール実行後にインクリメントされるため、1では出力が切り詰められます。
    - **クォータ**：Grokのプールは週単位で、**Chat、Imagine、Voiceと共有**され、これを公開するコマンドはありません。`account/rateLimits/read` で消費量を算出できるCodexとは異なります。そのため `regen_translations.sh` は同時実行数を2に制限し、明示的に警告します。
    - **テスト**：新しいファイル `tests/test_grok_provider.py`（24テスト）。完全なスイートは **290テスト**。
  - **修正済みのバグ — ENの複数段落引用が（`--news` モードで）部分的にしか保護されなかった**：`_NEWS_CITATION_REGEX` は、引用本文として `>` 行の **連続した**並びしか受け付けていませんでした。引用が複数の段落（`>` の空行で区切られる）にまたがると、最後の段落だけが捕捉されてプレースホルダーに置換され、それ以前の段落はLLMに送られて翻訳されていました。これは `--news` が保証するために存在する目的とは正反対です。繰り返し部分は現在、内部の `>` 空行を受け付け、貪欲でない形式になりました。これにより、最初に見つかった空行ではなく、斜体の行の前にある `>` 空行で停止します。
    - **実測した影響**：実際の198記事のコーパスでは、該当する引用は419件中11件でした。回帰はありません。新しい正規表現が捕捉する引用数は完全に同じで、複数段落の本文だけが拡張されました（408本文は同一、11本文は拡張）。帰属行 `> — …` は、lookaheadを維持しているため、引き続き本文に取り込まれません。
    - **エンドツーエンドの証明**：ja/arに翻訳した69 KBの記事で確認しました。以前は引用の最初の段落が日本語では `> GLM-5.3がオープンウェイト化。` として出力され、アラビア語でも同様に翻訳されていましたが、現在は `> GLM-5.3 is now open-weight.` のままです。英語の引用行数は9行から10行に戻り、原文と一致します。
    - なお、この欠陥は下流のバリデーターでは検出されませんでした。引用の存在は確認しても、完全性までは検査していないためです。
  - **デフォルトプロバイダーの実測によるコスト削減**：`_openai_extra_kwargs` は、モデル名が `gpt-5` で始まる場合、`reasoning_effort="medium"` を送信していました。`--eco` の場合も含まれます。10語の文を翻訳する `gpt-5.4-mini` で測定したところ、`medium` は推論トークン45、出力トークン65、`none` は0と14でした。推論は翻訳に何ももたらさず、各ファイルの各セグメントで課金されていました。デフォルトは `--eco` では `none` となり、それ以外では `medium` のままです。CLIで明示的に渡した値が引き続き優先されます。`--reasoning_effort` は現在、`low`/`medium`/`high` に加えて `none` と `xhigh` も受け付けます（すべてのモデルがすべてを受け付けるわけではありません。たとえば `minimal` は `gpt-5.4-mini` に拒否されますが、既存のパラメーターなしリトライがこのケースを処理します）。
  - **SDKの更新とGeminiの移行**：`google-generativeai`（サポート終了日は2025-11-30、リポジトリはアーカイブ済み）は、統合SDK **`google-genai`** に置き換えられました。`genai.Client(api_key=...)`、続いて `client.models.generate_content(model=, contents=, config=)` を使用し、システムプロンプトはセグメントに連結するのではなく `system_instruction` として渡します。`mistralai` は **2.9.4** に更新されました（インポートは `from mistralai.client import Mistral` になり、旧形式は `ImportError` を発生させることをwheelで確認済み）。`anthropic` は **0.125.0**、`openai` は **2.54.0** です。これは `httpx2` への切り替え前の最後のバージョンであり、venv内に2つのHTTPスタックを共存させないためです。その結果、`httpx` 0.28.1と `pydantic` 2.13.5 も利用可能になりました。
  - **ドキュメントではなく実際のテストで捕捉した2つの回帰**：
    - `anthropic` 1.0以降では、`max_tokens` が10分を超えることを示唆する非ストリーミング呼び出し（`ValueError: Streaming is required...`）をクライアント側で拒否します。この安全策は0.34.2にはなく、`max_tokens=32768` を伴うClaudeの呼び出しをすべて壊していました。明示的な `timeout`（`CLAUDE_TIMEOUT`、デフォルト900秒）で修正しました。これにより、完全な応答だけを利用する呼び出しがストリーミングへ切り替わるのを防ぎます。
    - `thinking_level="minimal"` はGeminiカタログの一部でしか受け付けられません。`gemini-3.1-flash-lite` は対応していますが、`gemini-3.7-flash` と `gemini-3.1-pro-preview` は400で拒否します。そのため `_gemini_generate_with_fallback` を導入し、`minimal` → `low` → thinking_configなしというカスケードにしました。これは既存のOpenAIフォールバックに倣ったもので、最適化パラメーターが翻訳を失敗させてはなりません。
  - **デフォルトモデルを刷新**し、それぞれ実際の呼び出しで検証：OpenAIは `gpt-5.5` → **`gpt-5.6-terra`**（28件のバッチで−60%）、`gpt-5.4-mini` → **`gpt-5.6-luna`**（−73%）。Claudeは `claude-sonnet-4-6` → **`claude-sonnet-5`**（より安価で新しい）と `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（日付なしの正規ID）。Geminiは `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**、`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（安定版で、`3.5-flash-lite` より安価）。Mistralは変更せず、`mistral-large-latest` は4つの中で依然として最良の価格性能比です。なお、`gemini-3.1-pro-preview` より新しいProクラスのGeminiモデルは存在しません。2026年5月に発表されたGemini 3.5 Proは実際にはリリースされておらず、3.5/3.6/3.7の系列はすべてFlash専用です。
  - **Gemini切り替え前に実施したA/B測定**：`README.md` を `gemini-3.1-pro-preview`、続いて `gemini-3.7-flash` で日本語に翻訳しました。構造は完全に同一でした（21リスト、18コードブロック、13 HTMLリンク、13画像、すべてのURLを保持）。所要時間は **48秒に対して8秒** でした。これら2モデルについて、翻訳や非ラテン文字のスクリプトを対象に比較した公開ベンチマークは存在しないため、測定がなければ単なる推測に基づく切り替えになっていました。
  - **Claudeのレスポンスブロックをフィルタリング**：`_call_claude` は型を確認せず `block.text for block in response.content` していました。適応型推論モデル（Sonnet 5以降）は `thinking` ブロックを挿入します。そこには `.thinking` が公開され、`.text` ではありません。これにより、最初のセグメントで不透明な `AttributeError` に遭遇すると翻訳が壊れていました。`thinking`、`redacted_thinking`、`tool_use`、`tool_result` のブロックは現在除外されます（未知の型がテキストを含む場合にも対応できるよう、除外リスト方式）。テキストブロックが1つもない応答では、明示的なエラーが発生します。`thinking={"type": "disabled"}` は各呼び出しに渡されるようになりました。
  - **`MODEL_TOKEN_LIMITS` を再同期**：提供終了日を過ぎたモデルを削除しました（`magistral-*` 系列は2026-07-31、`gemini-2.0-*` は2026-06-01、`gemini-3-pro-preview` は2026-03-09に終了。`claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514` も削除）。上限を修正：Mistralは128K → **256K**（Large 3 / Small 4の生成）、Geminiは1,000,000 → **1,048,576**（実際の入力上限）、`claude-opus-4-5` は200K → **1M**、`gpt-5.6-*` 系列は400K → **1.05M**。Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest`、`ministral-*` 系列を追加しました。なお、これらの上限はあくまで目安であり、`translate()` が分割単位を `min(16000, limite)` に制限しています。
- **Provider `--use_codex`**：公式 Codex CLI（`codex exec`）を非対話モードで制御する 5 番目の provider。使用量に応じて課金される API を呼び出す代わりに、すでに支払い済みの ChatGPT サブスクリプションのクォータから翻訳分が差し引かれます。この用途について OpenAI が文書化している唯一の方法です。プラン別の提供状況マトリクスでは、「Codex SDK、`codex exec`、and scriptable workflows」が Plus/Pro/Business/Enterprise で利用可能と記載されています。一方、`~/.codex/auth.json` のトークンでは Platform API の呼び出しを認証できず、このスクリプトから読み取られることもありません（認証とその更新は CLI が引き続き管理します）。
  - **pip でインストール可能な Codex バイナリ、npm だけではなくなった**：`_resolve_codex_binary()` はまず `CODEX_BIN` でバイナリを探し、次に `PATH`、その後 OpenAI が公開している公式 Python パッケージ **`openai-codex-cli-bin`**（SDK `openai-codex` の依存関係）を探します。そのため、Python プロジェクトで `--use_codex` を使用するために npm のグローバルインストールは不要になりました。パッケージは `requirements.txt` には追加されません。バイナリのサイズが約 250 MB あり、オプションの provider のために全ユーザーへ強制することになるためです。最初から最後まで検証済みです。`codex` が `PATH` に存在しない状態でも、パッケージ化されたバイナリが解決され、完全な翻訳が 6 秒で完了します。
  - **「サブスクリプションモード」の保証**：`OPENAI_API_KEY` と `CODEX_API_KEY` はサブプロセスの環境から削除されます。このガードがなければ、`.env` に存在するキーによって、目に見える通知なしに Codex が従量課金へ切り替わる可能性があります。これはまさに、この provider が防ぐために存在する事態です。
  - **CLI の落とし穴をテストで固定**：
    - `codex exec` は prompt が引数で渡されている場合でも stdin を**読み取ります**。stdin を閉じないと、モデルを一度も呼び出さないままコマンドがタイムアウトまで待機します（再現結果：180 秒後に exit 124、0 バイト）。したがって `communicate(input=...)` は必須です。
    - npm でインストールされる `codex` は、実際の Rust バイナリを `spawn` する Node の shim です。このバイナリは Python プロセスの**孫プロセス**であり、`SIGKILL` による `subprocess.run(timeout=)` 後も生き残って、クォータを消費し続けます。そのため `Popen(start_new_session=True)` と `os.killpg` が必要です。
    - CLI は `turn.failed` を出力していても終了コード 0 になることがあります。JSONL 出力（`--json`）を終了コードに加えて検査し、終了コードが 0 なのに `-o` がない場合は、空のセグメントを生成せず明示的なエラーを発生させます。
  - **レート制限時のバックオフ**：CLI は内部リトライ（`max_retries = 0`）を実装していません。分類は部分文字列ではなく JSON ペイロードの構造（`status: 429` / `error.type`）に基づいて行われます。「quota」という語は、回復可能な 429 と、確定的な `insufficient_quota` の両方に現れるためです。
  - **CI ガード**：`--use_codex` は `CI` または `GITHUB_ACTIONS` が定義されている場合は拒否されます。サブスクリプション認証は共有 runner 向けに設計されておらず、OpenAI も公開リポジトリでこのワークフローを使用しないよう明示的に推奨しています。
  - **モデル**：`gpt-5.6-sol`（品質重視）と `gpt-5.6-luna`（`--eco`）。`gpt-5.6-*` ファミリーは CLI と Platform API で共通ですが、ChatGPT アカウントですべてを利用できるわけではありません。allowlist はサーバー側で適用され、ローカル検証は行われず、通常とは異なるモデルを指定すると警告が発生します。Plus プランでは、Luna が 5 時間のウィンドウあたり 250〜2,000 メッセージ、Sol が 10〜100 メッセージであるため、`--eco` はあらゆるバッチ処理に推奨されるモードです。
  - **修正済みのバグ — 完全に成功していても `regen_translations.sh` がエラーになっていた**：`trap ... EXIT` は `failed_log` を参照していました。これは `main()` の `local` で、trap の実行時にはすでに存在しません。`set -u` では `failed_log: unbound variable` が発生し、28 件の翻訳が正しかったにもかかわらずスクリプトが 1 で終了していました。その結果、最もコストの高い再生成直後の段階で `release.sh --auto`（`set -e`）が中断されるところでした。変数をグローバルにし、trap がその存在を確認するようにしました。副次的な有用な効果として、これまでこのエラーに隠れていた本当の翻訳失敗が、終了時の要約に再び表示されます。
  - **`REGEN_MODEL`**：`regen_translations.sh` の新しい環境変数。provider のデフォルトを上書きして特定のモデルを強制します。たとえば `REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol` を指定すると、ボリューム重視の `--eco` ではなく、サブスクリプションのクォータで利用できる上位モデルを使って再生成できます。
  - **`regen_translations.sh`**：`REGEN_PROVIDER=codex` を明示的な opt-in で利用可能にしました（ユーザーが知らないうちにサブスクリプションのクォータを消費しないよう、自動検出は決して行いません）。トークンは並列処理を開始する前に 1 回だけ逐次的に更新されます。Codex の更新はローテーション式で一度しか使用できないため、並行ジョブでは `codex login` セッションが無効になります。並行数は 4 に抑えられます。
  - **関連するリファクタリング**：`_dispatch_provider_call` のパラメーター数を、provider 名を返す `_resolve_provider()` によって 8 個から 6 個へ減らしました。チェーン全体に 4 番目の boolean を伝播させる必要はありません。`translate(..., use_mistral=True)` を `Namespace` の最小構成で呼び出すテストを維持するため、明示的な boolean は `args` より優先されます。
  - **テスト**：新しいファイル `tests/test_codex_provider.py`（48 テスト）で、argv、不要な環境変数の除去、前置き禁止契約、サイレント失敗、timeout/killpg、バックオフ、preflight、provider 解決、Gemini の推論カスケード、Claude ブロックのフィルタリング、複数段落の news 引用をカバーします。テストスイート全体は 290 テストになりました。
  - **実環境での検証**：プロジェクトの `README.md` を Codex で**14 言語**に翻訳した結果、参照翻訳と厳密に同一の構造になりました（コードブロック 14 個、見出し 24 個、表の行 25 行、HTML リンク 13 個、画像 13 個、URL 19 個、コードブロックは文字単位で完全一致、placeholder の残留ゼロ）。`--news` モードで 69 KB のニュース記事を処理した場合、`gpt-5.6-luna` と `gpt-5.6-sol` は en/ja/ar の下流アプリケーションバリデーターをいずれも通過しました。`account/rateLimits/read` で測定した消費量は、`--eco` モードでカウンターの丸め閾値未満（5 時間ウィンドウの 0%）に収まりました。

- **1.9.2** ニュース帰属 URL の抽出を修正：入れ子の括弧または FR プレフィックスに対応（2026-05-11）：

  - **修正済みのバグ**：`_protect_news_quotes` における帰属 URL の抽出では、正規表現 `re.search(r"\((.+?)\)", attribution)`（括弧間の lazy capture）を使用していました。`(relayé par [@user sur X](https://x.com/.../123))` のような帰属（`(` の外側の括弧と、Markdown link の `]()` が入れ子になっている場合）では、キャプチャが最初に現れる `)` で止まり、文字列が途中で切れたうえ、FR プレフィックスも含まれていました：`relayé par [@user sur X](https://x.com/.../123`（末尾の `)` なし）。その結果、`_validate_news_post` は翻訳後の出力内でこの文字列を見つけようとして、常に失敗していました（理由は 2 つあります：`)` が途中で切れていることと、「relayé par」が翻訳によって `relayed by` / `weitergeleitet von` / ... になること）。low → medium → high → gpt-5.5 の完全なカスケードを通過できませんでした。
  - **修正**：正規表現を `re.search(r"\]\(([^)]+)\)", attribution)` に変更しました。これは Markdown link の `](url)` を特定して、**純粋な URL だけ**（FR プレフィックスや途中で切れた部分を除く）をキャプチャします。翻訳中は `#URL{N}#` の placeholder によって不変性が維持されます。問題の 2 パターンに対応しています：
    - `(relayé par [@account sur X](url))` — 入れ子の括弧
    - `via [@source](url)` または `selon [@author](url)` — 外側の括弧なしの FR プレフィックス
  - **テスト**：`test_silent_failure.py` の `TestNewsCitationExtraction` クラスに 2 件追加：
    - `test_extract_attribution_url_with_nested_parens`（Genspark CEO E2B で実際に再現したバグケース）
    - `test_extract_attribution_url_with_french_prefix`（`via` を使用する変種）
  - **未カバーの領域**：`check-editorial-coverage.py` は編集上の構文を検証しますが、translator による翻訳可能性は検証しません。今後の改善案（v1.9.2 の範囲外）として、公開前にリスクのあるパターンを検出できるよう、dry-run で帰属抽出をシミュレートするチェックが考えられます。

- **1.9.1** 翻訳 marker 注記の CTA ラベルの i18n を修正（2026-05-10）：

  - **修正済みのバグ**：翻訳済みファイル上部の marker バナーにある CTA リンクの `[Voir le projet sur GitHub ↗]` が、`target_lang` に従わず、すべての対象言語で**フランス語のまま**になっていました。URL とリポジトリの slug を保持するため Python 側で組み立てられており、LLM からは見えないため、翻訳フェーズで修正できませんでした。これは v1.9 で `marker` 形式を追加して以来、ひそかに発生していた回帰です。
  - **修正**：15 言語をローカライズされたラベルに対応付ける新しい定数 `_VIEW_PROJECT_LABELS` を追加しました。`_translation_note_invariants(target_lang)` と `_assemble_translation_note_paragraphs(phrase, target_lang)` が対象言語を伝播するようになりました。不明な言語の場合は `fr` にフォールバックします（安全対策であり、KeyError を防ぎます）。
  - **テスト**：`ja` の target_lang を `test_source_emits_three_paragraphs_repo_title_description_link` に調整し、日本語ラベルを期待するようにしました。新しいテストを 2 件追加：`test_source_link_label_localized_per_target_lang`（ラテン文字、表意文字、アブジャドの各文字体系を含む 7 言語でパラメーター化）と `test_source_link_label_falls_back_to_french_for_unknown_target`。合計は `test_translation_note_position.py` 内の 40 テストになりました（38 から増加）。
  - **後方互換性**：デフォルト値 `target_lang="fr"` を持つシグネチャにより、`args.target_lang` を指定しない外部のプログラム呼び出し元も変更なしで引き続き動作します。
- **1.9** サイレント失敗の修正 + 完全な品質ツール群 + 複数位置対応の翻訳ノート（2026-05-07）：
  - **複数位置対応の翻訳ノート + 「embed card」形式マーカー**：
    - 新しい CLI オプション（追加機能、デフォルトは変更なし → **破壊的変更なし**）：
      - `--note_position {top,bottom,both}`（デフォルト：`bottom`）：翻訳ファイルの上部、下部、または両方にノートを配置します。
      - `--note_format {legacy,marker}`（デフォルト：`legacy`）：
        - `legacy` は v1.8 の動作（太字段落 `**…**`）を **byte-for-byte** 厳密に再現します。
        - `marker` は、不可視の Markdown リンク参照定義（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）に続いて、**3 段落の blockquote** を出力します。これは「GitHub repo embed card」形式のレンダリング用に構成され、インラインコードのプロジェクトタイトル（`**\`ai-powered-markdown-translator\`\*\*`）、LLM による翻訳済みの説明、矢印を表示する CTA リンク（`[Voir le projet sur GitHub ↗](URL)`）で構成されます。remark プラグインによるビルド時の利用が可能です（jls42.org のブログ → プラグイン `remark-translation-banner`）。
    - **LLM に送信されない不変要素**：リポジトリタイトルと GitHub URL は説明文の翻訳後に Python 側で組み立てられます。LLM がスラッグ `ai-powered-markdown-translator` や `https://github.com/jls42/...` を見ることは決してなく、renderer、区切り文字、scheme が変更されることを防ぎます。
    - **Frontmatter 対応の挿入**：`top` または `both` モードでは、ノートは YAML frontmatter の **`---` 終了ブロックの後**に挿入されます（Astro Content Collections / gray-matter の安全性を確保）。Helper `_split_frontmatter` はファイル冒頭の `---\n…\n---\n` を検出して完全性を保持し、終了 fence のない未完了 frontmatter では **`RuntimeError` を送出**します。そのファイルは `failed_files` に回され、ノートが誤った位置に置かれた状態では書き込まれません。
    - **Whitelist モデル sanitizer**：`_sanitize_model` は `[A-Za-z0-9._:/-]` 以外のすべての文字を `_` に置換し、空の場合は `unknown` にフォールバックします。remark Astro プラグイン側のバリデーターに合わせ、マーカー形式を壊す文字（空白、引用符、括弧、コンマなど）を無効化します。
    - **内部リファクタリング**：`_append_translation_note`（1 つのモノリシックな関数）を 7 つの純粋な helper（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）に分割しました。builder と composer を分離し（builder は区切り文字のない純粋なブロックを返し、composer は位置に応じて `\n\n` を適用）、生成処理と source helper は同じ 3 段落アセンブラーを共有します。
    - **`_quote_lines` の空行保持**：各行の先頭に `> ` を付け、空行を `>` のみに変換します。これにより mdast は blockquote 内で、改行を含む 1 つの段落ではなく、3 つの異なる段落（タイトル / 説明 / リンク）として認識できます。
    - **`_build_translation_note_block` の適応処理**：LLM が保持した段落数に応じて処理します（3 = 完全なカード形式、2 = 文 + リンク、1 = フォールバック）。1 段落のフォールバックでは、Markdown リンク `](` が検出された場合、`<strong>` の周囲にリンクを置くとレンダリングが不安定になるため、もはや `**...**` で囲みません。
    - **後方互換性**：`_compose_with_notes` 側の `getattr(args, "note_position", "bottom")` と `getattr(args, "note_format", "legacy")` — これらの属性を持たない Namespace（既存テスト、外部のプログラム呼び出し）は、変更なしで引き続き動作します。
  - **長い翻訳におけるサイレント失敗の修正**：
    - すべての provider（OpenAI、Mistral、Claude、Gemini）で翻訳後の言語を検証：決定論的レイヤー（source の抜粋が逐語的に再現されているか）+ 確率論的レイヤー（`langdetect`）
    - `finish_reason` / `stop_reason` の whitelist：whitelist 外の状態（truncation、content_filter など）では `RuntimeError` を送出
    - Claude の `max_tokens`：`4096` → `32768`（16k セグメントでの潜在的な truncation を回避し、FR→JA/ZH/KO/AR/HI の異なるスクリプト間に余裕を確保）
    - 見出しを考慮した segmentation：セグメントの後半では H2/H3 を優先（各セグメントが意味的に完全なセクションから始まるようにする）
    - エラーを exit code が非ゼロになるまで伝播：`translate_markdown_file` は型付きステータス `success` / `failure` / `skipped` を返し、少なくとも 1 ファイルが失敗した場合は `main()` `sys.exit(1)`（単一ファイルおよび batch）
    - すべての provider に対する empty-content guard、source/output の sanity ratio（≥ 500 文字、< 5% = 拒否）、コード placeholder の検証（`#CODEBLOCK`/`#INLINECODE`）、LLM 後の正規化（見出しに連結された区切り文字 / リンク）、`BadRequestError` を `reasoning_effort` なしで retry
    - 依存関係 `langdetect==1.0.9` を追加
  - **pre-commit 品質ツール**（「完全な EurekAI 型」、14 hooks）：
    - Pre-commit：ruff（lint + format）、shellcheck、prettier（md/yaml/json）、detect-secrets（4 つの API key を保護）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（whitespace、EOF、large-files、shebangs など）
    - Pre-push：mypy（段階的な lax モード）、Opengrep SAST（translate.py + scripts/）、pip-audit（初期は reporting モード）、unittest discover（tests/ + scripts/tests/）
    - `scripts/` 内のローカル wrapper は `./venv/bin/python` を使用
    - `scripts/audit_verdict.py`：11 個の unittest による pip-audit の JSON parser、jls42-astro の parser を Python に移植
    - 初期の ruff 違反 7 件を修正：B904（raise from）×2、B007（unused dirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizard は一時的に `translate.py` を除外（CCN 21-47 の関数が 4 つあり、リファクタリングを予定）— scripts/ では strict gate
  - **SonarCloud + 完全なカバレッジ**：
    - GitHub Actions workflow `SonarCloud`（sonarcloud.yml + sonar-project.properties）：各 push と pull-request で解析、`coverage.xml` による coverage
    - README 上部に SonarCloud のバッジ 11 個（Quality Gate、Security/Reliability/Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）
    - `tests/test_silent_failure.py`（`unittest` stdlib）：サイレント失敗のエラーチェーン 6 箇所をカバー
    - `tests/test_orchestration.py`（+79 テスト）：`translate.py` の orchestration 層をカバー（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` TypeError + BadRequestError fallbacks、o1-series prompt format、`_validate_translation_output` の early-return 分岐）
    - `scripts/tests/test_audit_verdict.py`：`main()`（stdin/stdout）と `if __name__ == "__main__"` ブロックを subprocess 経由でカバー
    - **Coverage on new code**：75.5% → 約 98%（translate.py 98%、scripts/audit_verdict.py 97%）
  - **テスト**：`tests/test_translation_note_position.py` は位置 × 形式のマトリクス（E2E の `marker+top|bottom|both` と `legacy+top|bottom|both` を含む）、複数行の prefix 付与、byte-for-byte の後方互換性（golden literal）、sanitizer、frontmatter の分割（未終了 fence での raise を含む）、3 段落形式、2 段落フォールバック、1 段落 + Markdown リンクの guard、そしてタイトルと URL が決して LLM に送信されないことを検証する重要な安全策 `TestLLMPayloadExcludesInvariants` をカバーします。**190 テストが成功**、回帰 0 件。
  - ドキュメント：`README.md`（FR + 14 翻訳）にバッジ、`CLAUDE.md`（pre-commit workflow + 詳細な watch CI）、28 翻訳を再生成
- **1.8** `--news` モード + 2026 年モデル更新（2026-03-17、タグ `v1.8`）：
  - デフォルトモデルを更新（2026 年 3 月）：
    - OpenAI 品質向け：`gpt-5` → `gpt-5.4`
    - OpenAI 低コスト向け：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 品質向け：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）、`gemini-3.1-pro-preview`（1M）の token 上限を追加
  - 初期 `--news` モード：`#NEWSQUOTE\d+#` による英語引用の保護、`LANG_FLAGS`（15 言語）、対象言語ごとの flag 処理
  - 復元前に news placeholder を検証（回帰：placeholder を削除する LLM により、引用のない出力がサイレントに生成されていた）
  - `regen_translations.sh` スクリプトを portable 化（絶対パス、pwd への依存なし）
  - README / CHANGELOG の language bar にフランス語リンクを追加、28 翻訳を再生成
- **1.7** 新機能：
  - 翻訳時に元のファイル名を保持する `--keep_filename` オプション
  - API key を自動的に読み込む `.env` ファイルのサポート
  - **inline code の保持**：backtick（`` `...` ``）を翻訳中に保護
  - system prompt を改善：
    - YAML frontmatter 内の引用符をより適切に処理
    - template 変数 `{variable}` を保護
    - 要求されていない翻訳者ノートを禁止
  - jls42.org のブログ移行で 364 ファイルを正常にテスト
- **1.6** 新機能：
  - 翻訳用 Google Gemini API をサポート（`--use_gemini`）
  - 2026 年のデフォルトモデルを更新：
    - OpenAI：`gpt-5`（品質）、`gpt-5-mini`（低コスト）
    - Claude：`claude-sonnet-4-5`（品質）、`claude-haiku-4-5`（低コスト）
    - Gemini：`gemini-3-pro-preview`（品質）、`gemini-3-flash-preview`（低コスト）
  - より高速で低コストなモデルを使用する低コストモード（`--eco`）
  - ディレクトリを走査せずに単一ファイルを翻訳（`--file`）
  - 新しい簡略化された命名パターン：`{base}-{lang}.md`
  - モデル名を含む以前の形式を保持する `--include_model` オプション
  - 未登録モデルをデフォルトの token 上限（128k）付きでサポート
  - README を 14 言語に翻訳
- **1.5** 改善：
  - **API key とデフォルトモデルを更新：**
    - **OpenAI：** `DEFAULT_MODEL_OPENAI` から `"gpt-4o"` に更新。
    - **Mistral AI：** `DEFAULT_MODEL_MISTRAL` から `"mistral-large-latest"` に更新。
    - **Anthropic の Claude：** `DEFAULT_ANTHROPIC_API_KEY` を追加し、`DEFAULT_MODEL_CLAUDE` から `"claude-3-5-sonnet-20240620"` に更新。
  - **翻訳 prompt を最適化：**
    - 直接翻訳と翻訳ノート用の prompt を拡充し、明確性と効率性を向上。メタデータおよび特定の書式要素の保持に関する詳細な指示を追加。
  - **コードをリファクタリング：**
    - Mistral AI client の初期化で `MistralClient` を `Mistral` クラスに置換。
    - 可読性と保守性を高めるため import を再編成。
    - テキストの segmentation と code block の処理を改善し、翻訳中に元の書式を保持。
  - **出力ファイルを管理：**
    - 出力ファイル名におけるモデルと言語の順序を反転（例：`f"{base}-{args.target_lang}-{args.model}.md"`）。翻訳の整理と検索を容易にします。
  - **その他の改善：**
    - 不要な空行を削除してコードを整理。
    - script の構造と可読性を向上させるため、細かな調整を実施。
- **1.4** 新機能：
  - 翻訳用 Anthropic Claude API をサポート
  - 明確性と効率性を高めるため prompt を最適化
  - コードの保守性を向上させるため細かな調整を実施
- **1.3** 改善と新機能：
  - code block の処理を改善
  - 出力ファイルの処理を改善
  - 既存ファイルの検出を改善
  - 翻訳を強制する `--force` オプション
  - 出力ファイル名におけるモデルと言語の順序を反転
- **1.2** changelog を修正
- **1.1** Mistral AI API のサポートを追加
- **1.0** 初期バージョン — OpenAI API をサポート

**記事はgpt-5.6-lunaでフランス語から日本語に翻訳されました。**
