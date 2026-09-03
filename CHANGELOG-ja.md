### 変更履歴

🌍 [Français](CHANGELOG.md) | [English](CHANGELOG-en.md) | [Español](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [Deutsch](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [한국어](CHANGELOG-ko.md) | [العربية](CHANGELOG-ar.md) | [हिन्दी](CHANGELOG-hi.md) | [Italiano](CHANGELOG-it.md) | [Nederlands](CHANGELOG-nl.md) | [Polski](CHANGELOG-pl.md) | [Português](CHANGELOG-pt.md) | [Română](CHANGELOG-ro.md) | [Svenska](CHANGELOG-sv.md)

- **1.11.0** PyPI で公開：`pip install ai-powered-markdown-translator` の後に `aipmt` コマンドを実行すれば、リポジトリをクローンせずに利用可能（2026-09-03）：

  - **単一ファイルのスクリプトがインストール可能なパッケージになりました。** `translate.py` はルートから `src/aipmt/translate.py` に移され、コンソールエントリーポイント `aipmt` と、その同等の `python -m aipmt` が追加されました。クローンしたリポジトリは貢献のためには引き続き必要です — テスト、28 の翻訳、品質ツールがそこに含まれています — しかし利用するためには不要になりました。

    - **インポート名は `aipmt` であり、決して `translate` ではありません**。この衝突は実際に発生し、しかも静かに起こるためです。PyPI パッケージ `translate`（v3.8.1、最終アップロード 2026-07-06）は、同名のディレクトリをインストールします。venv で再現すると、ディレクトリがモジュールより優先され、`translate.main` が消え、エントリーポイントは `AttributeError` で失敗します — そして `pip check` は rc=0 で「No broken requirements found」と返します。ユーザー側で単純に `pip install translate` を実行するだけでも、診断手段なしに CLI が壊れる可能性がありました。実際の wheel で反証確認：パッケージの上に `pip install translate` を実行しても、前後とも `aipmt --help` は rc=0 で、2 つの CLI は共存します。
    - **配布名は長く、コマンド名は短くしました。** `ai-powered-markdown-translator` により、PyPI 検索でパッケージを見つけられます。プロジェクトを事前に知らない人には略語だけでは見つけられず、今回の公開はまさに見つけてもらうことを目的としています。候補として妥当だった 2 つは検証により除外しました：`ai-markdown-translator` は 2024 年から npm で同じ対象のツールに使用されており、このリポジトリより 17 か月先行しています。また `aimt` は `aim`（v3.29.1）と 1 文字違いで、同じ分野の現役パッケージです — 長期的な混同を招く最悪の構成です。ここで方法上の落とし穴も判明しました：`pypi.org/project/<nom>/` はボット対策ページのため、どんな名前にも 200 を返します。信頼できるのは JSON API だけです。
    - **フラットなパッケージではなく `src/` レイアウトにしました。** フラットなパッケージなら、テストにある 6 つの `sys.path.insert(..., "..")` を維持できましたが、まさにそれが問題です。それらはパッケージではなくソースツリーをインポートするため、パッケージ化の誤りを隠してしまいます。実際のコストは、置換ルールが 1 つ増えることです。

  - **キーを一度設定すれば済むようになりました。** インストール済み CLI には永続的な設定がなく、環境変数とカレントディレクトリの `.env` だけが残っていました。`find_dotenv` はシステムルートまで遡るため、**ホームディレクトリ配下で作業している場合**には `~/.env` を見つけられましたが、別の場所では何も見つかりませんでした — コマンドをどこから起動するかに依存する動作であり、設計上の選択ではありませんでした。そのため、既存の 2 層の下に第 3 層として `~/.config/aipmt/.env` を追加しました。

    - **優先順位は明示的にコード化されていません**。`load_dotenv` のデフォルト値である `override=False` から導かれます：各層は、前の層が空のまま残したものだけを補います。そのため順序は、環境変数 → プロジェクトの `.env` → ユーザー設定となります。これは構造ではなく動作のテストで検証しています — 2 つの呼び出しの順序を逆にすると失敗し、第 3 層を削除しても失敗します。
    - **意図的に TOML ではなく `.env` 形式にしました**：`python-dotenv` はすでに依存関係に含まれ、構文は 15 個の README ですでに文書化されており、同じファイルを両方のスコープで使用できます。依存関係も新しい構文も増えません。配置は、`XDG_CONFIG_HOME` が**絶対パス**ならそれに従います — 仕様では相対値を無視するよう求めており、そうしないと設定の場所が再びカレントディレクトリ依存になるためです — Windows では `APPDATA` になります。
    - **除外した 2 つの選択肢と、その理由。** システムのキーチェーン（`keyring`）はデスクトップではより安全ですが、headless — サーバー、コンテナ、CI — では失敗します。これはバッチ翻訳そのものの利用場面です。オプトインなら有力ですが、デフォルトには不適切です。`--api-key` フラグではキーがシェル履歴に残り、`ps` に表示されてしまいます。
    - **キーがない場合、呼び出し履歴を表示しなくなりました。** ユーザーには `site-packages` を指す Python のスタックトレースと、「環境または .env」とだけ示すメッセージが表示され、後者をどこに作るべきかは説明されていませんでした。現在は 3 つの場所を正確なパス付きで列挙し、コマンドは 2 で終了します。保護範囲を**意図的に狭く**しています：`except ValueError` は設定フェーズだけに適用されます。実行全体を包むと、翻訳中に発生した本当のバグが安心させるだけのメッセージに変わってしまいます — これはこのリポジトリが追跡している障害モードです。`main()` のソースを読むテストで、このことを禁止しています。

  - **修正 — インストール後、ユーザーの `.env` が無視されていました。** 引数なしの `load_dotenv()` はカレントディレクトリからではなく、呼び出し元ファイル、つまり `site-packages` から遡ります。独自の `.env` を持つプロジェクトから実際のコンソールエントリーポイントを起動して測定したところ、`find_dotenv()` は `''` を返してキーを読み込まず、`find_dotenv(usecwd=True)` なら読み込みました。ツールがクローンしたリポジトリからのみ実行されていた間は存在しなかったバグですが、公開後は常に発生し、正しい設定にもかかわらず API キーが「不足している」とだけ表示されることになっていました。

  - **何も検証しなくなっても、3 つのゲートが成功してしまう状態でした。** 意図的に移動**前**に強化しました：検出すべき変更の後に書かれたガードは、何も証明しません。元のリポジトリではそれぞれ成功し、移行済みコピーでは失敗します — 両方向を測定しています。

    - **Lizard は存在しないパスを何も言わずに無視します**：rc=0、「0 file analyzed」。複雑度ゲートは 158 関数 / 2247 nloc から 3 関数 / 34 nloc へ変わり、出力は 0 バイトになります。現在はスコープを配列にし、各エントリの存在を検証しています。
    - **存在しないモジュールに対する `coverage run --source=` は失敗しません**：stderr の警告だけで、unittest でも `coverage xml` でも rc=0 となり、レポートは公開されます — ただし 1453 から 141 statements に縮小されています。ほとんど分析されなくなったため、プロジェクトは健全に見えてしまいます。レポートを守る下限を 2 つ設けました：合計値と、測定対象となった最大ファイルです。
    - **翻訳の鮮度プローブは、起動形式に対して構造的に盲目です**：argparse のフラグを基準にしており、ファイル名の変更では変わらないものを見ています。再現すると、モジュールを移動しても 15 個の README は存在しないコマンドを文書化したままで、判定は「古い翻訳なし」になります。そのため第 7 セクションではオプションではなく**形式**を検証し、Lizard フックをスクリプトの実際のスコープと照合します。そのキー `files:` が一致しなくなっても pre-commit を失敗させず、**スキップ**させます。

  - **`requires-python = ">=3.10"` は主張ではなくなりました。** `sonar-project.properties` はすでに 3.10〜3.12 を宣言していましたが、開発環境には 3.12 しかなく、実際には何も検証されていませんでした。公開すれば内部矛盾が明らかになります。現在はテストワークフローで 3.10、3.11、3.12 上のテストスイートを実行し、公開されている制約を持つ**パッケージ**をインストールします。

  - **下限のみ設定し、上限は設けません。** `requirements.txt` はテスト対象の lock のまま、`[project.dependencies]` は公開契約になります。lock の正確なバージョンを公開すると、別のパッケージを使用しているユーザーとの競合を招くためです。`<N+1` の上限も設けません — これは、メジャーバージョンの遅れがあるとリリースゲートを失敗させる `check-deps-fresh.sh` と正面から矛盾するためです。下限の組み合わせで解決し、反証確認では `openai==1.0.0` が `ResolutionImpossible` で終了しました。これは検査が何でも受け入れるのではなく、区別していることを証明します。さらに、`pyproject.toml` のバージョンが CHANGELOG のものと異なることを禁止するガードも設けました。PyPI では同じ番号を再利用できないためです。

  - **新しい venv で最初から最後まで検証済みです**：`aipmt/*.py`、dist-info、ライセンスだけを含む約 70 Ko の wheel；`aipmt --help` は 22 個のフラグ付きで rc=0；`python -m aipmt` は「usage: aipmt」と表示し、「usage: \_\_main\_\_.py」ではありません；`pipx` のインストールは正常に動作します。そして何より、**任意のユーザーディレクトリから実際に fr→en 翻訳**を実行し、太字、リスト、インラインコード、リンク、URL を保持し、コードブロックは翻訳されないことを確認しました。移行前に存在した 318 テストは、前後でバイト単位まで同一の識別子一覧とともにすべて成功しました — テストが無効化されていないことを証明するのは「OK」ではなく、この事実です。さらに 3 層構成の設定用テストを 12 件追加し、合計 330 件になりました。

- **1.10.0** Provider `--use_codex`（ChatGPT サブスクリプションのクォータ）、SDK とモデルの更新、複数段落の news 引用を修正（2026-08-29）：

  - **セキュリティレビュー — PR が設けたものの、すべての箇所で維持できていなかった 2 つのガード：**

    - **Codex の preflight が `.env` 全体をバイナリに渡していました。** `_codex_preflight` は **`env=` なしで** `subprocess.run` を呼び出していました：サブプロセスは `os.environ` 全体を継承し、`load_dotenv` が読み込んだ `.env` のすべてが渡されます。計測用の偽バイナリで測定した結果、preflight には **7 つの秘密情報** — 6 つの provider のキーと 1 つの `GITHUB_TOKEN` — が届いていました。一方、対応する `_grok_preflight` は正しく `env=_grok_env()` を渡しており、**0 件**でした。この不整合は PR 内部のものでした：数行先にある `_strip_secret_env` は、まさにこの不変条件を維持するために存在します。`_codex_env_base()` を抽出して両方の経路で共有し、修正後に測定した結果、両方とも秘密情報は 0 件でした。
    - **「`--deny` fail-closed」という性質は、使用されていた形式を対象としていませんでした。** コメントでは、未知のプレフィックスを持つルールが起動を拒否することを、Grok の隔離全体の根拠としていました。`grok 1.0.13` で測定すると、この検証は**括弧付き形式に対してのみ**存在します：`--deny 'CeciNestPasUnOutil(*)'` は「unknown tool prefix」として起動を拒否しますが、`--deny 'CeciNestPasUnOutil'` は黙って受け入れられます。一方、`GROK_DENY_RULES` は裸の名前だけを使用していました。そのため xAI 側でツール名が変更されると、測定済みの唯一の隔離層が何の兆候もなく失われることになります。しかも、その環境では OS sandbox がすでに適用されません。名前付きの 8 ルールは `Prefix(*)` を通過し、それぞれ CLI の既知のプレフィックスであることを検証します。catch-all の `*` は、唯一受け入れられるリテラル形式のまま残しました。テストにより、未検証形式への回帰を防ぎます。
    - **その他についてはクリーンであることを検証済みです**：コマンドインジェクションなし（常にリスト形式で、`shell=True` は決して使用せず、ドキュメント内容は stdin または `--prompt-file` 経由）、安全でないデシリアライズなし（`json.loads` のみ、型ガード付き）、7 つのペイロードでパストラバーサルの修正に回避策がないことを確認し、`--deny '*'` が CLI によって実際に適用されることも確認しました（workdir 外の読み取りで `DENY_ENFORCED` を観測）。
    - 上で追加した鮮度チェックは、その過程で自身の原則を回避していました。PyPI リクエストに失敗したパッケージを黙ってスキップし、ゲートが成功していたのです。現在は実際に比較されたパッケージ数を数え、網羅性が不足している場合は失敗します。

  - **依存関係を更新し、遅延の再発を防ぐ 2 つの仕組みを追加しました。**

    - **遅延は実際に存在し、長期化していました**：`openai` 2.54 → **3.6.0**、`anthropic` 0.125 → **1.2.0**、`certifi` 2024.8.30 → **2026.7.22** — すべての provider 呼び出しで TLS を検証するルート証明書ストアが 2 年遅れていました。原因は **`.github/dependabot.yml` が存在しなかったこと**です。このファイルがない場合、GitHub は _security updates_ のみを有効にし、Dependabot は CVE の対象になった依存関係に対してのみ PR を提案します。そのため `urllib3` と `idna` は bump された一方、2 つの SDK はメジャーバージョン 1 つ分遅れたままになっていました。
    - **2 つのメジャーバージョンは競合せず共存します**。以前の推論では競合が懸念されていましたが、`openai` 3.x と `anthropic` 1.x は **`httpx2`** に移行し、`mistralai` と `google-genai` は `httpx<1` に残ります。しかし、これは異なるディストリビューションです。実際のインストールで確認し、さらに **7 つの provider 経路を最後までテスト**しました — OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI、Grok CLI — 各出力でインラインコードとリンクが保持されました。「HTTP スタックを 2 つ避ける」ことは好みであり、阻害要因ではありませんでした。測定によって結論が出ました。
    - **`requirements.txt` は実際の環境を記述していませんでした**：`google-auth`、`cryptography`、`opentelemetry` のスタックは作業用 venv にインストールされていましたが、宣言されていませんでした。そのため、新規インストールではテスト対象の状態を再現できませんでした。逆に、`tokenizers`、`huggingface-hub`、`PyYAML` はそこに含まれていましたが、何からもインポートも要求もされておらず、`mistralai` 1.x の残骸でした。ファイルを、直接依存関係だけから構築した venv の完全な閉包として再生成しました。`pip-audit` は新しい構成で既知の脆弱性を報告しません。
    - 新規の **`.github/dependabot.yml`** で、バージョン、pip、github-actions の週次更新を有効にしました。マイナー更新とパッチ更新は 1 つの PR にまとめます — パッチごとに PR を作ると無視され、ノイズは更新の敵になるためです。**メジャー更新は分離**し、それぞれ実際の呼び出しによる検証を要求します。
    - 新規でゲートに接続した **`scripts/check-deps-fresh.sh`** により、遅延がプロジェクトの判定に表示されます。Dependabot は提案するだけで保証はせず、PR が積み重なることもあります。メジャーの遅延 → 失敗；マイナー → 警告。ゲートが常に赤だと無視されるためです。PyPI に接続できない場合 → ローカルでは明示的にスキップし、**CI では fail-closed**。実行されなかったチェックは成功ではありません。両方向で検証済みです：修正前の正確な状態（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`）を検出し、マイナー更新については警告にとどまります。

  - **この PR のレビューから生じた修正** — 5 人のレビューエージェントが diff を徹底的に精査しました。以下の項目はすべて、修正前に**測定によって再現**され、そのうち 2 つは同じバージョンの上記変更で導入された回帰でした。
- **修正済みのリグレッション — `_NEWS_CITATION_REGEX` には指数バックトラッキングがあった。** 複数段落対応の修正で、繰り返し内に `(?:[ \t]*$|[ \t]+.*)` が導入されていた。`[ \t]+` と `.*` の間で空白を共有する方法が曖昧で、その曖昧さが反復ごとに増幅していた。パターンにマッチしない、合法な Markdown インデントである `>   texte` の行で測定したところ、修正前は **14 行で 2 589 ms**、修正後は 0.04 ms で、1 行追加するごとに約 9 倍になっていた。`--news` モードでは、長く不正な blockquote だけで翻訳がジョブのタイムアウトまで停止し、原因も特定できなかった。現在は繰り返しが行全体を一括で消費する (`\n^>(?![ \t]*—).*`) ため、反復ごとのマッチ方法が 1 通りしかない。実際の 231 記事のコーパスで検証し、**捕捉結果の差異はゼロ**、同じ 423 件の引用、複数段落の本文 14 件も引き続き展開されることを確認した。
    - **2 つの provider フラグを同時に指定すると、気付かないまま従量課金になっていた。** `--use_codex --use_mistral` は受け付けられていた。`_select_provider_client` はまず Mistral を検査し、`_resolve_provider` は明示的な boolean を優先するため、どちらも Mistral に収束していた。ユーザーはサブスクリプションの割り当てを求めていたのに従量課金になり、警告は一切表示されなかった。これは、まさに `--use_codex` が防ぐために存在する障害モードだった。現在は 6 つの provider フラグすべてが `add_mutually_exclusive_group` を通る。**動作変更**：これまで黙って受け付けられていた、2 つの provider を組み合わせたコマンドラインは、現在は `argument --use_mistral: not allowed with argument --use_codex` で失敗する。
    - **プローブがクラッシュした際、作業完了ゲートが緑になっていた。** `scripts/check-release-ready.sh` の 13 検査のうち 4 つが、「stdout を捕捉し、空なら結論を出す」というパターンに従い、終了コードを一度も確認していなかった。例外 (ファイルの名前変更、`FileNotFoundError`) は stderr に出力され、stdout は空のままとなり、検査は「報告すべきことはない」と結論していた。「1 つの `exit 0` では何も証明できない」という落とし穴が、それを防ぐために書かれたスクリプト内部で再現されていた。現在は `probe()` ヘルパーが、ゼロの終了コード **および** 終了センチネルを要求する。またプローブは、空の目印集合に基づく結論を拒否する。空集合に対するアサーションは常に真だからである。実例として、上記の排他的グループを追加した結果、provider フラグは `*_group` オブジェクトを通るようになり、旧来の正規表現 `parser\.add_argument\(` にはマッチしなくなった。**21 個中 6 個のフラグ**が黙って対象範囲から外れ、ゲートは緑になっていた。
    - **シークレットスキャンが 6 provider 中 4 provider を見逃していた。** `[A-Za-z0-9]` クラスはハイフンを除外するため、`sk-proj-…` (現在の OpenAI 形式) と `sk-ant-api03-…` は 2 つ目のハイフンで失敗し、`AIza…` は対象になっていなかった。パターンを拡張し、`.secrets.baseline` をスキャン対象から除外した。さらに `.env` のガードは `git diff --cached` を照会していたが、これはインデックスしか見ない。**すでにコミット済みの** `.env`、つまり最悪のケースは、そこには決して現れなかった。現在は `git ls-files` を照会する。
    - **Codex の「トークンのウォームアップ」はウォームアップではなかった。** 測定の結果、`codex login status` は `~/.codex/auth.json` に触れず (mtime とサイズは不変)、ヘルプには「ログイン状態を表示」と書かれていた。しかしコメントは、ローテーションする使い捨てトークンに対する同時 refresh のリスクを無効化するため、「一度、逐次的に」トークンを更新すると主張していた。宣言されていた保護は存在せず、現在のコメントはコードの実際の動作を記述している。実際の対策は引き続き `max_jobs=4` である。さらに検査は、無視されていた `CODEX_BIN` にも従うようになった。`codex` が `PATH` にないマシンでは「未認証」として失敗していたが、これは誤解を招く診断だった。
    - **`.env` がサブシェル内で source されていた。** `detect_provider` はコマンド置換で呼び出されるため、その export は上位に戻らなかった。`.env` で定義された `GROK_BIN`、`GROK_HOME`、`REGEN_MODEL` は `main()` で行われる読み取りから見えず、正しい設定でも「Grok バイナリが見つからない」と結論されていた。
    - **同時実行数が公称上限を 50% 超えていた。** ガードが README/CHANGELOG のペアを起動した後に置かれていたため、測定されたピークは **`max_jobs=2` が 3** だった。Chat/Imagine/Voice と週次割り当てを共有し、測定もできない Grok では、スクリプトが自らに課す上限が守られていなかった。最終カウントも表示されるだけで 28 と比較されておらず、ファイルが 1 つ欠けても見逃されていた。
    - **Grok の出力契約：`stopReason` がない場合も失敗になった。** コードは、契約で要求されている `end_turn` の代わりに「`end_turn` **または存在しない**」を適用していた。フィールドのない payload、または CLI の更新でフィールド名が変更された payload は、ガードを黙って no-op にしていた。また `max_turn_requests` は rate limit として分類されなくなった。これはターン予算が尽きた状態であり、再試行しても結果は変わらず、90 秒の待機だけが発生するためである。さらに `quota` は rate limit のマーカーから外れた。これは `_codex_is_rate_limited` の docstring がすでに説明していた理由を、Grok が適用していなかったためである。
    - **Gemini のカスケードをモデル単位でメモ化した。** 各セグメントで `minimal` から再開していたが、デフォルトモデルはそれを拒否するため、通常経路ではセグメントごとに 400 の往復を行い、同じ警告を再表示していた。警告が何百回も繰り返されると読まれなくなる。それがマスクになる仕組みである。
    - **その他**：CI での拒否メッセージが Codex 用にハードコードされており、`--use_grok_cli` のユーザーを `XAI_API_KEY` ではなく `OPENAI_API_KEY` に誘導していた。`provider.capitalize()` は「Grok_cli」と「Openai」を表示していた。サブプロセス基盤のコメントは、Grok バイナリがネイティブ ELF であるにもかかわらず、両方の CLI に「shim」を一般化していた。正しい根拠は「独自のサブプロセスを spawn する agent」である。`subprocess` に関する SAST の 12 件の finding は、根拠付きで `# nosec` / `# nosemgrep` とマークした。`shell=True` のないリスト形式ではインジェクションが不可能であり、ドキュメントの内容が argv を通ることもない。
    - **agent のサブプロセスにシークレットが入らなくなった。** 名前を列挙した deny-list が保護していたのは、**課金**の不変条件 (Codex は `OPENAI_API_KEY` なし、Grok は `XAI_API_KEY` なし) だけだった。測定の結果、さらに **7 個のシークレット**が各サブプロセスに入っていた。Anthropic、Mistral、Google、Gemini のキー、もう一方の CLI のキー、そしてシークレットではないがトラフィックを再ルーティングする `OPENAI_BASE_URL` である。この 2 つの CLI は **agent** であり、Grok の CLI は多くの Linux マシンで適用可能な OS sandbox なしに動作する。現在は名前の列挙ではなく、**名前のパターン** (`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`) でフィルタリングするため、コードが把握していない変数をユーザーが `.env` に追加した場合も対象になる。CLI にこれらは不要である。認証は `~/.codex` と `~/.grok` にあり、環境変数には決して存在しない。環境を強化した状態で両 provider を使った **実際の翻訳を最後まで完了**させて検証した。
    - **テスト**：`tests/test_review_hardening.py` (21 テスト) を新設し、provider フラグの排他性、`stopReason` 契約、news 正規表現の線形性、CI での拒否メッセージ、Gemini のメモ化、サブプロセス環境にシークレットが存在しないことを固定した。最後のアサーションは **汎用的**であり、どのリストにも名前のないキーがあれば失敗する。既存の除去テストは定数の鏡像であり、自分自身のループの故障以外は何も検出できなかった。全体のテスト数は **311 テスト**になった。

  - **2 つの新しい Grok provider**：`--use_grok` (xAI API、キー `XAI_API_KEY`、従量課金) と `--use_grok_cli` (公式 Grok Build CLI、Grok サブスクリプションから差し引き — `--use_codex` と同じ原理)。
    - **API モード、約 40 行**：xAI の endpoint は OpenAI 互換なので、client と `_call_openai` はそのまま再利用し、変更するのは `base_url` だけである。必要だった適応は 1 つだけで、しかも全体に恩恵がある。`finish_reason` が `end_turn` を受け付けるようになった。これは xAI が出力する形式であり、OpenAI は `stop` を出力する。モデルは `grok-4.6` (品質重視) と `grok-4.3` (エコノミー) である。なお、Grok のエコノミーモデルはリポジトリ内で最も高価なままで、100 万トークンあたり $1.25/$2.50、`mistral-small-latest` は $0.15/$0.60 である。この provider は価格ではなく、モデルの多様性を理由に選ぶものである。
    - **CLI モード**：Codex を基にしつつ、実環境によって 4 つの相違点が必要になった。prompt はファイルで渡す (`--prompt-file`。CLI は stdin を読まず、argv にセグメントを入れると `ps` から見えてしまう)。出力は stdout 上の単一 JSON オブジェクトである (JSONL でも `-o` ファイルでもない)。サブスクリプションが公開するのは `grok-4.6` と `grok-4.5` だけであり、sandbox は適用できない (下記参照)。サブプロセスの起動は `_codex_run_process` で Codex と共通化したが、すでにテスト済みの Codex provider の残りには触れていない。
    - **`exit 0` は何も証明しないことを測定で確認**：未認証の場合、CLI は `{"type":"error","message":"Not signed in."}` を **stdout** に書き、終了コードは **0** になる。拒否やターン超過も同じように振る舞う。そのため出力契約は、終了コード 0、エラー payload がないこと、`stopReason == end_turn`、空でないテキストという 4 条件を同時に要求する。preflight も同じ考え方に従う。`grok models` は切断状態でも 0 で終了するため、判断できるのは stdout に「not authenticated」が存在する場合だけである。
    - **隔離：非対称性を受け入れ、文書化した。** Codex が `--sandbox read-only` で動作する一方、多くの最近の Linux マシンでは Grok の sandbox を適用できない。`sudo` なしには回避できない、独立した 2 つのシステム上の原因がある。Ubuntu 24.04 以降では AppArmor が非特権 user namespace をブロックする (`bwrap: setting up uid map: Permission denied`。Grok 以外でも再現)。また、`/run/podman` が `0700` の場合、コンテナ runtime socket の deny-list が失敗する (resolver が取り戻せるのは `ErrorKind::NotFound` だけで、EACCES は致命的になる)。中心的な落とし穴は、**統合された** profile を適用できない場合に、**隔離されていない状態で黙って起動する**ことだ。したがってスクリプトはデフォルトで profile を要求せず、黙ってフォールバックもしない。stderr に警告を出す。保護は CLI の `--deny` ルールに依存し、catch-all の `*` も含める。これは測定済みの唯一の _fail-closed_ 層であり、未知の prefix を持つルールがあると起動を拒否する。`GROK_TRANSLATE_SANDBOX=read-only` を使えば必須にでき、その場合、マシンが適用できなければ起動に失敗する。
    - **安全策**：`XAI_API_KEY`、`GROK_API_KEY`、`GROK_SANDBOX` はサブプロセスの環境から除去する (キーがあれば従量課金に切り替わり、継承された `GROK_SANDBOX` が適用不能な profile を強制して誤解を招くメッセージを出す)。MCP/hooks/skills/agents のスイッチを無効化し、`--disable-web-search`、`--no-subagents`、`--no-plan`、使い捨ての workdir、CI での拒否、プロセスグループを終了させる timeout、rate limit 時の back-off を設定する。`--max-turns` は 1 ではなく 6 に設定する。カウンターはツールのターン後に増加するため、1 では出力が切り詰められる。
    - **Quota**：Grok の pool は週次で、**Chat、Imagine、Voice と共有**されており、それを公開するコマンドはない。`account/rateLimits/read` で消費量を算出できる Codex とは異なる。したがって `regen_translations.sh` は同時実行数を 2 に制限し、明示的に警告する。
    - **テスト**：`tests/test_grok_provider.py` (24 テスト) を新設した。全体のテスト数は **290 テスト**になった。
  - **修正済みのバグ — EN の複数段落引用が一部しか保護されていなかった (`--news` モード)**：`_NEWS_CITATION_REGEX` は引用本文として、`>` の行が **連続して**並ぶ場合しか受け付けていなかった。引用が複数段落にまたがり、その間に `>` の空行があると、最後の段落だけが捕捉されて placeholder に置換され、それ以前の段落は LLM に渡されて翻訳されていた。これは `--news` が保証するために存在する目的とは正反対である。現在は繰り返しが内部の `>` の空行を受け付け、非貪欲になった。そのため最初に出会う空行ではなく、斜体行の前にある `>` の空行で停止する。
    - **規模を実測**：実際の 198 記事のコーパスで、419 件中 11 件の引用が該当した。リグレッションはなく、新しい正規表現が捕捉する引用数は完全に同じで、複数段落の本文だけが拡張された (同一の本文 408 件、拡張された本文 11 件)。帰属行 `> — …` は引き続き本文に取り込まれない (lookahead を維持)。
    - **エンドツーエンドの証明**：69 KB の記事を ja/ar に翻訳したところ、以前は日本語で `> GLM-5.3がオープンウェイト化。` として出力され、アラビア語でも同様に翻訳されていた引用の第 1 段落が、現在は `> GLM-5.3 is now open-weight.` のままになった。英語引用行の数は 9 行から 10 行に戻り、ソースと一致した。
    - 注：この不具合は下流の validator では検出されなかった。validator は引用が存在することだけを確認し、完全であるかどうかは確認していなかった。
  - **デフォルト provider で測定したコスト削減**：`_openai_extra_kwargs` は、モデル名が `gpt-5` で始まると、`--eco` であっても `reasoning_effort="medium"` を送信していた。10 語の文を翻訳する `gpt-5.4-mini` で測定した結果、`medium` → reasoning token 45、出力 token 65、`none` → 0 と 14 だった。推論は翻訳に何ももたらさず、各ファイルの各セグメントで課金されていた。デフォルトは `--eco` では `none` になり、それ以外では `medium` のままとなった。CLI で明示的に渡された値が引き続き優先される。`--reasoning_effort` は `low`/`medium`/`high` に加えて、`none` と `xhigh` も受け付けるようになった (すべてのモデルがすべてを受け付けるわけではない。たとえば `minimal` は `gpt-5.4-mini` に拒否されるが、既存のパラメーターなし retry がこのケースを処理する)。
  - **SDK の更新と Gemini の移行**：`google-generativeai` (サポート終了日は 2025-11-30、リポジトリはアーカイブ済み) を、統合 SDK **`google-genai`** に置き換えた。`genai.Client(api_key=...)`、続いて `client.models.generate_content(model=, contents=, config=)` を使用し、システム prompt はセグメントに連結するのではなく `system_instruction` として渡す。`mistralai` は **2.9.4** に更新 (import は `from mistralai.client import Mistral` になり、旧来のものは `ImportError` を発生させることを wheel 内で確認)、`anthropic` は **0.125.0**、`openai` は **2.54.0** とした。これは `httpx2` への切り替え前の最後のバージョンであり、venv 内に 2 つの HTTP stack を共存させないためである。その結果、`httpx` 0.28.1 と `pydantic` 2.13.5 も解放された。
  - **実際のテストで検出され、ドキュメントでは検出されなかった 2 つのリグレッション**：
    - `anthropic` 1.0 以降では、`max_tokens` が 10 分を超える可能性を示す、非ストリーミングの呼び出しを client 側で拒否する (`ValueError: Streaming is required...`)。この安全策は 0.34.2 にはなく、`max_tokens=32768` を使う Claude の呼び出しをすべて壊していた。明示的な `timeout` (`CLAUDE_TIMEOUT`、デフォルト 900 秒) で修正した。これにより、完全な応答だけを利用する呼び出しがストリーミングへ切り替わるのを避けられる。
    - `thinking_level="minimal"` は Gemini のカタログの一部でしか受け付けられない。`gemini-3.1-flash-lite` は対応するが、`gemini-3.7-flash` と `gemini-3.1-pro-preview` は 400 で拒否する。そのため `_gemini_generate_with_fallback` を導入した。これは `minimal` → `low` → thinking_config なしというカスケードで、既存の OpenAI fallback と同じ考え方である。最適化用パラメーターによって翻訳が失敗してはならない。
  - **デフォルトモデルを更新し、それぞれ実際の呼び出しで検証**：OpenAI は `gpt-5.5` → **`gpt-5.6-terra`** (28 件の batch で −60%)、`gpt-5.4-mini` → **`gpt-5.6-luna`** (−73%)。Claude は `claude-sonnet-4-6` → **`claude-sonnet-5`** (より安価で新しい) と `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`** (日付なしの canonical ID)。Gemini は `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**、`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`** (安定版で、`3.5-flash-lite` より安価)。
Mistralは変更せず、`mistral-large-latest`が4つの中で引き続き最もコストパフォーマンスに優れている。なお、`gemini-3.1-pro-preview`より新しいProシリーズのGeminiモデルは存在しない。2026年5月に発表されたGemini 3.5 Proはリリースされておらず、3.5/3.6/3.7の系列はFlash専用である。
  - **Geminiに切り替える前にA/B測定**：`README.md`を`gemini-3.1-pro-preview`で日本語に翻訳し、その後`gemini-3.7-flash`で翻訳した。構造は完全に同一（リスト21個、コードブロック18個、HTMLリンク13個、画像13個、すべてのURLを保持）で、**48秒に対して8秒**だった。翻訳や非ラテン文字スクリプトについて、この2モデルを比較した公開ベンチマークは存在しないため、測定しなければ切り替えは単なる推測に基づくものになっていた。
  - **Claudeの応答ブロックをフィルタリング**：`_call_claude`は型をフィルタリングせずに`block.text for block in response.content`していた。適応型推論モデル（Sonnet 5以降）は`thinking`ブロックを挿入する。このブロックが公開するのは`.thinking`であり、`.text`ではないため、最初のセグメントで不透明な`AttributeError`に遭遇すると翻訳が壊れていた。`thinking`、`redacted_thinking`、`tool_use`、`tool_result`のブロックは現在除外されている（未知のテキスト保持型にも寛容でいられるよう、除外リスト方式）。テキストブロックが1つもない応答では、明示的なエラーが発生する。`thinking={"type": "disabled"}`は各呼び出しに渡されるようになった。
  - **`MODEL_TOKEN_LIMITS`を再同期**：廃止日を過ぎたモデルを削除した（`magistral-*`系列は2026-07-31、`gemini-2.0-*`は2026-06-01、`gemini-3-pro-preview`は2026-03-09に廃止、`claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。上限を修正：Mistralは128Kから**256K**（Large 3 / Small 4世代）、Geminiは1 000 000から**1 048 576**（実際の入力上限）、`claude-opus-4-5`は200Kから**1M**、`gpt-5.6-*`ファミリーは400Kから**1,05M**。Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest`、`ministral-*`系列を追加した。なお、これらの上限はあくまで目安であり、`translate()`は分割を`min(16000, limite)`に制限している。

  - **Provider `--use_codex`**：公式Codex CLI（`codex exec`）を非対話モードで操作する5番目のプロバイダー。従量課金のAPIを呼び出す代わりに、すでに支払い済みのChatGPTサブスクリプションのクォータから翻訳分が差し引かれる。この用途についてOpenAIが文書化している唯一の方法である。プラン別提供状況の一覧では、Plus/Pro/Business/Enterpriseで「Codex SDK、`codex exec`、and scriptable workflows」が利用可能とされている。一方、`~/.codex/auth.json`のトークンではPlatform API呼び出しを認証できず、このスクリプトから読み取られることもない（認証とその更新は引き続きCLIが管理する）。
  - **pipでインストール可能なCodexバイナリ、npmだけではなく対応**：`_resolve_codex_binary()`はまず`CODEX_BIN`でバイナリを探し、次に`PATH`、その後OpenAIが公開している公式Pythonパッケージ **`openai-codex-cli-bin`**（SDK `openai-codex`の依存関係）を探す。これにより、Pythonプロジェクトで`--use_codex`を利用するためにnpmのグローバルインストールが不要になった。このパッケージは`requirements.txt`には追加されていない。バイナリのサイズが約250 MBあり、オプションのプロバイダーのために全ユーザーへ強制することになるためである。最初から最後まで検証済み：`codex`が`PATH`にない状態でも、解決処理はパッケージ化されたバイナリを見つけ、完全な翻訳が6秒で完了した。
  - **「サブスクリプションモード」の保証**：`OPENAI_API_KEY`と`CODEX_API_KEY`をサブプロセスの環境から削除する。この保護がなければ、`.env`に存在するキーによってCodexが従量課金へ切り替わっても、目に見える通知が一切ない可能性がある。これはまさに、このプロバイダーが防ぐために存在する事態である。
  - **CLIの落とし穴をテストで固定**：
    - `codex exec`は、プロンプトを引数で渡した場合**でも**stdinを読み取る。stdinを閉じないと、モデルを一度も呼び出さないままコマンドがタイムアウトまで待機する（再現結果：180秒後に終了コード124、0バイト）。したがって`communicate(input=...)`は必須である。
    - npmでインストールされる`codex`は、実際のRustバイナリを`spawn`するNodeのshimである。このバイナリはPythonプロセスの**孫プロセス**であり、`SIGKILL`の`subprocess.run(timeout=)`後も生存してクォータを消費し続ける可能性がある。そのため`Popen(start_new_session=True)`と`os.killpg`が必要になる。
    - CLIは`turn.failed`を出力していても終了コード0を返すことがある。JSONL出力（`--json`）を終了コードに加えて検査し、終了コード0なのに`-o`がない場合は、空のセグメントを生成せず明示的なエラーを発生させる。
  - **レート制限時のバックオフ**：CLIは内部リトライを実装していない（`max_retries = 0`）。分類は部分文字列ではなくJSONペイロードの構造（`status: 429` / `error.type`）に基づいて行う。「quota」という語は、回復可能な429エラーにも`insufficient_quota`にも現れるためである。
  - **CIガード**：`--use_codex`は、`CI`または`GITHUB_ACTIONS`が定義されている場合に拒否される。サブスクリプション認証は共有ランナー向けに想定されておらず、OpenAIも公開リポジトリでのこのワークフローを明確に推奨していない。
  - **モデル**：`gpt-5.6-sol`（品質）と`gpt-5.6-luna`（`--eco`）。`gpt-5.6-*`ファミリーはCLIとPlatform APIで共通だが、ChatGPTアカウントですべて利用できるわけではない。allowlistはローカル検証なしにサーバー側で適用され、通常と異なるモデルを指定すると警告が発生する。Plusプランでは、Lunaは5時間のウィンドウごとに250～2,000メッセージ、Solは10～100メッセージである。そのため、`--eco`はあらゆるバッチ処理に推奨されるモードである。
  - **修正済みのバグ — 完全に成功しているのに`regen_translations.sh`がエラーになっていた**：`trap ... EXIT`が`failed_log`を参照していた。これは`main()`の`local`変数であり、trapの実行時にはすでに存在しない。`set -u`では`failed_log: unbound variable`が発生し、28件の翻訳が正しかったにもかかわらずスクリプトが1で終了していた。これにより、最もコストの高い再生成直後の段階で`release.sh --auto`（`set -e`）が中断されるところだった。変数をグローバルにし、trapがその存在を検査するようにした。副次的な効果として、これまでこのエラーに隠れていた実際の翻訳失敗が、終了時の要約に再び表示されるようになった。
  - **`REGEN_MODEL`**：`regen_translations.sh`の新しい環境変数。プロバイダーのデフォルトを上書きして特定のモデルを強制できる。たとえば`REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`を指定すると、ボリューム重視の`--eco`ではなく、サブスクリプションのクォータで利用できる上位モデルを使って再生成できる。
  - **`regen_translations.sh`**：`REGEN_PROVIDER=codex`を明示的なオプトインで利用可能にした（ユーザーに知らせずサブスクリプションのクォータを消費しないよう、自動検出は行わない）。トークンは並列処理を開始する前に一度だけ逐次更新する。Codexの更新はローテーション式で一度しか使えないため、並行ジョブがセッション`codex login`を無効化してしまうからである。並列度は4に下げた。
  - **関連するリファクタリング**：`_dispatch_provider_call`の引数を8個から6個に減らした。プロバイダー名を返す`_resolve_provider()`を使い、4番目のブール値をチェーン全体に伝播させる方式をやめた。明示的なブール値は`args`より優先されるため、`Namespace`だけを使って`translate(..., use_mistral=True)`を呼び出すテストも維持できる。
  - **テスト**：新しい`tests/test_codex_provider.py`ファイル（48テスト）で、argv、環境変数の除去、前置き禁止契約、サイレント失敗、timeout/killpg、バックオフ、preflight、プロバイダー解決、Geminiの推論カスケード、Claudeのブロックフィルタリング、複数段落のニュース引用をカバーした。全体のテスト数は290になった。
  - **実環境での検証**：プロジェクトの`README.md`をCodexで**14言語**に翻訳した結果、参照翻訳と完全に同一の構造になった（コードブロック14個、見出し24個、表の行25行、HTMLリンク13個、画像13個、URL19個、コードブロックは1文字単位で完全一致、プレースホルダーの残留ゼロ）。`--news`モードで69 KBのニュース記事を処理した場合、`gpt-5.6-luna`と`gpt-5.6-sol`の出力はいずれも、後段のアプリケーションバリデーターをen/ja/arで通過した。`account/rateLimits/read`で測定した消費量は、`--eco`モードで5時間ウィンドウのカウンターの丸め閾値未満（0%）に収まった。

- **1.9.2** 括弧の入れ子またはFR接頭辞を含むニュース帰属URL抽出を修正（2026-05-11）：

  - **修正済みのバグ**：`_protect_news_quotes`における帰属URLの抽出は、正規表現`re.search(r"\((.+?)\)", attribution)`（括弧間を遅延キャプチャ）を使用していた。`(relayé par [@user sur X](https://x.com/.../123))`のような帰属（入れ子になった括弧：外側の`(`とMarkdownリンクの`]()`）では、キャプチャが最初に現れる`)`で停止し、文字列が途中で切れてFR接頭辞も含まれていた：`relayé par [@user sur X](https://x.com/.../123`（末尾の`)`なし）。その結果、`_validate_news_post`はこの文字列を翻訳済み出力内で探して必ず失敗していた（理由は2つ：`)`が途中で切れていることと、「relayé par」が`relayed by`/`weitergeleitet von`/...に翻訳されること）。low → medium → high → gpt-5.5の完全なカスケードを通過できなかった。
  - **修正**：正規表現を`re.search(r"\]\(([^)]+)\)", attribution)`に変更した。これはMarkdownリンクの`](url)`のみを特定して、**純粋なURLだけ**（FR接頭辞や途中切れなし）をキャプチャする。翻訳中は`#URL{N}#`のプレースホルダーによって不変性が保たれる。問題となる2つのパターンに対応する：
    - `(relayé par [@account sur X](url))` — 括弧の入れ子
    - `via [@source](url)`または`selon [@author](url)` — 外側の括弧なしのFR接頭辞
  - **テスト**：`test_silent_failure.py`の`TestNewsCitationExtraction`クラスに2件追加：
    - `test_extract_attribution_url_with_nested_parens`（Genspark CEO E2Bで再現したバグと完全に同じケース）
    - `test_extract_attribution_url_with_french_prefix`（`via`を含むバリエーション）
  - **カバレッジ上の不足**：`check-editorial-coverage.py`は編集上の構文を検証するが、translatorによる翻訳可能性は検証しない。今後の改善案（v1.9.2の対象外）は、公開前にリスクのあるパターンを検出できるよう、dry-runで帰属抽出をシミュレートするチェックを追加することである。

- **1.9.1** 翻訳マーカー注記内のCTAラベルのi18nを修正（2026-05-10）：

  - **修正済みのバグ**：翻訳済みファイル上部のマーカーバナーにあるCTAリンクの`[Voir le projet sur GitHub ↗]`ラベルが、`target_lang`に従わず、すべての対象言語で**フランス語のまま**になっていた。リポジトリのURLとslugを保持するためPython側で組み立てられており、LLMが一度も参照しないため、翻訳フェーズで修正できなかった。v1.9で`marker`形式を追加して以来、静かに発生していたリグレッションである。
  - **修正**：15言語のローカライズラベルを対応付ける新しい定数`_VIEW_PROJECT_LABELS`を追加した。`_translation_note_invariants(target_lang)`と`_assemble_translation_note_paragraphs(phrase, target_lang)`が対象言語を渡すようになった。未知の言語の場合は`fr`にフォールバックする（安全対策であり、KeyErrorを防ぐ）。
  - **テスト**：`test_source_emits_three_paragraphs_repo_title_description_link`を調整（target_lang `ja` → 日本語の期待ラベル）。新しいテストを2件追加：`test_source_link_label_localized_per_target_lang`（ラテン文字、表意文字、アブジャドの各スクリプトを含む7言語でパラメーター化）と`test_source_link_label_falls_back_to_french_for_unknown_target`。合計で`test_translation_note_position.py`のテストは38件から40件になった。
  - **後方互換性**：デフォルト値`target_lang="fr"`付きのシグネチャにしたため、`args.target_lang`なしで`target_lang="fr"`を呼び出す外部のプログラム利用者も変更なしで動作し続ける。
- **1.9** サイレント失敗の修正＋完全な品質ツール群＋複数位置翻訳ノート（2026-05-07）：
  - **複数位置翻訳ノート＋「embed card」形式マーカー**：
    - 新しい CLI オプション（追加機能、デフォルトは変更なし → **非破壊的**）：
      - `--note_position {top,bottom,both}`（デフォルト：`bottom`）：翻訳ファイルの上部、下部、または両方にノートを配置。
      - `--note_format {legacy,marker}`（デフォルト：`legacy`）：
        - `legacy` は v1.8 の動作（太字段落 `**…**`）を **byte-for-byte** で厳密に再現。
        - `marker` は非表示の Markdown リンク参照定義（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）に続けて、「GitHub repo embed card」形式でレンダリングするための、3 段落構成の **blockquote** を出力：インラインコードのプロジェクト名（`**\`ai-powered-markdown-translator\`\*\*`）、LLM が翻訳した説明、矢印を表示する CTA リンク（`[Voir le projet sur GitHub ↗](URL)`）。remark プラグインでビルド時に利用可能（jls42.org のブログ → プラグイン `remark-translation-banner`）。
    - **LLM に送信しない不変値**：リポジトリ名と GitHub URL は説明文の翻訳後に Python 側で組み立てる。LLM が slug `ai-powered-markdown-translator` や `https://github.com/jls42/...` を見ることはないため、renderer、スラッシュ、scheme が変更されることを防止。
    - **Frontmatter 対応の挿入**：`top` または `both` モードでは、ノートを YAML frontmatter の終了用 `---` ブロックの**後**に挿入（Astro Content Collections / gray-matter の安全性を確保）。Helper `_split_frontmatter` はファイル先頭の `---\n…\n---\n` を検出し、その完全性を保持。終了 fence のない未完了 frontmatter では **`RuntimeError` を送出**（ノートの位置が不正なまま書き込まず、ファイルを `failed_files` に送る）。
    - **モデル用 whitelist sanitizer**：`_sanitize_model` は `[A-Za-z0-9._:/-]` 外のすべての文字を `_` に置換し、空の場合は `unknown` にフォールバック。remark Astro プラグイン側のバリデーターと整合し、マーカー形式を壊す文字（空白、引用符、括弧、カンマなど）を無効化。
    - **内部リファクタリング**：`_append_translation_note`（1 つの巨大な関数）から、7 つの純粋な helper（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）へ変更。builder と composer を分離（builder は区切り文字のない純粋なブロックを返し、composer が位置に応じて `\n\n` を適用）。生成処理と helper のソースは同じ 3 段落アセンブラを共有。
    - **`_quote_lines` による空行保持**：各行の先頭に `> ` を付け、空行は `>` のみに変換。これにより mdast は blockquote 内で、改行を含む 1 つの段落ではなく、3 つの独立した段落（タイトル／説明／リンク）として認識。
    - **`_build_translation_note_block` の適応処理**：LLM が保持した段落数に応じて処理（3 = 完全な card 形式、2 = 文＋リンク、1 = フォールバック）。1 段落のフォールバックでは、Markdown リンク `](` が検出された場合に `**...**` で囲まなくなった（リンク周辺の `<strong>` はレンダリングが不安定なため）。
    - **後方互換性**：`_compose_with_notes` 側の `getattr(args, "note_position", "bottom")` と `getattr(args, "note_format", "legacy")` — これらの属性を持たない Namespace（既存テスト、外部のプログラム呼び出し）は変更なしで引き続き動作。
  - **長い翻訳におけるサイレント失敗の修正**：
    - すべての provider（OpenAI、Mistral、Claude、Gemini）で翻訳後の言語を検証：決定論的レイヤー（ソースの抜粋が逐語的に再現されているか）＋確率的レイヤー（`langdetect`）。
    - `finish_reason` / `stop_reason` の whitelist：whitelist 外の状態（truncation、content_filter など）では `RuntimeError` を送出。
    - `max_tokens` Claude：`4096` → `32768`（16k セグメントでの潜在的な truncation を回避し、FR→JA/ZH/KO/AR/HI のスクリプト間変換に余裕を確保）。
    - 見出し対応のセグメンテーション：セグメントの後半では H2/H3 を優先（各セグメントが意味的に完全なセクションから開始）。
    - エラーを終了コードが非ゼロになるまで伝播：`translate_markdown_file` は型付きステータス `success` / `failure` / `skipped` を返し、少なくとも 1 ファイルが失敗した場合は `main()` `sys.exit(1)`（単一ファイルとバッチの両方）。
    - すべての provider に対する空コンテンツガード、ソース／出力の妥当性比率（500 文字以上、5% 未満は拒否）、コード placeholder の検証（`#CODEBLOCK`/`#INLINECODE`）、LLM 後の正規化（区切り文字／リンクが見出しに連結される問題）、`BadRequestError` は `reasoning_effort` なしで retry。
    - 依存関係 `langdetect==1.0.9` を追加。
  - **pre-commit 品質ツール**（「完全な EurekAI 型」、14 hooks）：
    - Pre-commit：ruff（lint＋format）、shellcheck、prettier（md/yaml/json）、detect-secrets（保護対象の API key 4 種）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（空白、EOF、large-files、shebangs など）。
    - Pre-push：mypy（段階的な lax モード）、Opengrep SAST（translate.py＋scripts/）、pip-audit（初期は reporting モード）、unittest discover（tests/＋scripts/tests/）。
    - `scripts/` 内のローカル wrapper は `./venv/bin/python` を使用。
    - `scripts/audit_verdict.py`：11 個の unittest で pip-audit の JSON parser を検証。jls42-astro の parser を Python に移植。
    - 初期の ruff 違反 7 件を修正：B904（raise from）×2、B007（未使用の dirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）。
    - Lizard は一時的に `translate.py` を除外（CCN 21〜47 の関数が 4 つあり、リファクタリングを計画中）— scripts/ では gate を厳格に適用。
  - **SonarCloud＋網羅的カバレッジ**：
    - GitHub Actions workflow `SonarCloud`（sonarcloud.yml＋sonar-project.properties）：各 push と pull-request で解析、`coverage.xml` による coverage。
    - README 上部に SonarCloud の badge 11 個（Quality Gate、Security/Reliability/Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）。
    - `tests/test_silent_failure.py`（`unittest` stdlib）：サイレント失敗のエラーチェーン 6 段階をカバー。
    - `tests/test_orchestration.py`（＋79 テスト）：`translate.py` のオーケストレーション層（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` TypeError＋BadRequestError のフォールバック、o1-series の prompt 形式、`_validate_translation_output` の early-return 分岐）をカバー。
    - `scripts/tests/test_audit_verdict.py`：`main()`（stdin/stdout）と、subprocess 経由の `if __name__ == "__main__"` ブロックをカバー。
    - **新規コードの Coverage**：75.5% → 約 98%（translate.py 98%、scripts/audit_verdict.py 97%）。
  - **テスト**：`tests/test_translation_note_position.py` は位置 × 形式のマトリクス（E2E の `marker+top|bottom|both` と `legacy+top|bottom|both` を含む）、複数行の prefix 付与、byte-for-byte の後方互換性（golden literal）、sanitizer、frontmatter の分割（未終了 fence での raise を含む）、3 段落形式、2 段落のフォールバック、1 段落＋Markdown リンクの guard、そしてタイトルと URL が LLM に送信されないことを assert する重要なガード `TestLLMPayloadExcludesInvariants` をカバー。**190 テストが pass、リグレッション 0。**
  - ドキュメント：badge 付きの `README.md`（FR＋14 翻訳）、`CLAUDE.md`（pre-commit workflow＋詳細な CI watch）、28 翻訳を再生成。
- **1.8** `--news` モード＋2026 年モデルの更新（2026-03-17、tag `v1.8`）：
  - デフォルトモデルを更新（2026 年 3 月）：
    - OpenAI 品質：`gpt-5` → `gpt-5.4`
    - OpenAI 経済：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 品質：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）、`gemini-3.1-pro-preview`（1M）の token limit を追加。
  - 初期の `--news` モード：placeholder `#NEWSQUOTE\d+#` による EN 引用の保護、`LANG_FLAGS`（15 言語）、対象言語ごとのフラグ管理。
  - 復元前にニュース placeholder を検証（リグレッション：placeholder を削除する LLM により、引用のない出力がサイレントに生成されていた）。
  - Script `regen_translations.sh` を portable 化（絶対パス、pwd への依存なし）。
  - README/CHANGELOG の language bar に Français リンクを追加、28 翻訳を再生成。
- **1.7** 新機能：
  - 翻訳時に元のファイル名を保持するオプション `--keep_filename`。
  - API key を自動的に読み込む `.env` ファイルをサポート。
  - **インラインコードの保持**：バッククォート（`` `...` ``）を翻訳中に保護。
  - システム prompt を改善：
    - YAML frontmatter 内の引用符をより適切に処理。
    - template 変数 `{variable}` を保護。
    - 要求されていない翻訳者ノートを禁止。
  - jls42.org の blog 移行で 364 ファイルを正常にテスト。
- **1.6** 新機能：
  - 翻訳用 Google Gemini API をサポート（`--use_gemini`）。
  - 2026 年のデフォルトモデルを更新：
    - OpenAI：`gpt-5`（品質）、`gpt-5-mini`（経済）
    - Claude：`claude-sonnet-4-5`（品質）、`claude-haiku-4-5`（経済）
    - Gemini：`gemini-3-pro-preview`（品質）、`gemini-3-flash-preview`（経済）
  - より高速で低コストなモデルを使用する経済モード（`--eco`）。
  - ディレクトリを走査せずに単一ファイルを翻訳する機能（`--file`）。
  - 簡略化された新しい命名パターン：`{base}-{lang}.md`。
  - モデル名を含む旧形式を保持するオプション `--include_model`。
  - token limit（デフォルト 128k）付きで未掲載モデルをサポート。
  - README を 14 言語に翻訳。
- **1.5** 改善：
  - **API key とデフォルトモデルを更新：**
    - **OpenAI：** `DEFAULT_MODEL_OPENAI` から `"gpt-4o"` へ更新。
    - **Mistral AI：** `DEFAULT_MODEL_MISTRAL` から `"mistral-large-latest"` へ更新。
    - **Anthropic の Claude：** `DEFAULT_ANTHROPIC_API_KEY` を追加し、`DEFAULT_MODEL_CLAUDE` から `"claude-3-5-sonnet-20240620"` へ更新。
  - **翻訳 prompt を最適化：**
    - 直接翻訳と翻訳ノート用の prompt を拡充し、明確性と効率を向上。メタデータや特定の書式要素の保持に関する詳細な指示を追加。
  - **コードをリファクタリング：**
    - Mistral AI client の初期化で `MistralClient` をクラス `Mistral` に置換。
    - 可読性と保守性を向上するため import を再編成。
    - 翻訳時に元の書式を保持できるよう、テキストのセグメンテーションとコードブロックの処理を改善。
  - **出力ファイルを管理：**
    - 出力ファイル名におけるモデルと言語の順序を反転（例：`f"{base}-{args.target_lang}-{args.model}.md"`）。翻訳の整理と検索を容易に。
  - **その他の改善：**
    - 不要な空行を削除してコードを整理。
    - script の構造と可読性を向上するため、軽微な調整を実施。
- **1.4** 新機能：
  - 翻訳用 Anthropic Claude API をサポート。
  - 明確性と効率を高めるため prompt を最適化。
  - コードの保守性を向上するため軽微な調整を実施。
- **1.3** 改善と新機能：
  - コードブロックの処理を改善。
  - 出力ファイルの処理を改善。
  - 既存ファイルの検出を改善。
  - 翻訳を強制するオプション `--force`。
  - 出力ファイル名におけるモデルと言語の順序を反転。
- **1.2** changelog の修正。
- **1.1** Mistral AI API のサポートを追加。
- **1.0** 初期バージョン — OpenAI API をサポート。

**GPT-5.6-lunaでフランス語から日本語に翻訳された記事。**
