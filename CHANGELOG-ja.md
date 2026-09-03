### 変更履歴

🌍 [フランス語](CHANGELOG.md) | [英語](CHANGELOG-en.md) | [スペイン語](CHANGELOG-es.md) | [中国語](CHANGELOG-zh.md) | [ドイツ語](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [韓国語](CHANGELOG-ko.md) | [アラビア語](CHANGELOG-ar.md) | [ヒンディー語](CHANGELOG-hi.md) | [イタリア語](CHANGELOG-it.md) | [オランダ語](CHANGELOG-nl.md) | [ポーランド語](CHANGELOG-pl.md) | [ポルトガル語](CHANGELOG-pt.md) | [ルーマニア語](CHANGELOG-ro.md) | [スウェーデン語](CHANGELOG-sv.md)

- **1.11.1** ドキュメント修正：README がようやく 7 つの provider 経路を記載（2026-09-03）：

  - **1.11.0 の PyPI ページには「4 APIs + Codex CLI」と記載されていた。** 実際のコードは 7 つを公開している — API 経由の OpenAI、Mistral、Claude、Gemini、Grok；従量課金なしのサブスクリプション経由の Codex (ChatGPT) と Grok。2 つの Grok モードは見出しと _Multi-Provider_ の箇条書きから抜けており、14 の翻訳でも誤りが繰り返されていた。パッケージの長い説明はバージョンごとに固定されるため、表示内容を修正するにはバージョン番号が必要だった。今回のリリースはそのためだけに存在する。**コード変更はない。**
  - `CLAUDE.md` は公開内容に合わせて更新されている：gate のカウンター（`--full` では 16、17）、有効な 11 個の workflow、`gh pr checks` に表示されない 2 つの Sonar/Codacy カウンター（hotspots、Codacy API）、1 つの `# nosemgrep` を `ruff-format` ごとに移動したこと、OIDC 交換に必要な GitHub environments、そして _pending publisher_ は名前を予約しないという事実。

- **1.11.0** PyPI で公開：リポジトリを clone せずに `pip install ai-powered-markdown-translator`、続いて `aipmt` を実行（2026-09-03）：

  - **単一ファイルのスクリプトがインストール可能なパッケージになった。** `translate.py` はルートから `src/aipmt/translate.py` へ移動し、console entry point `aipmt` と同等の `python -m aipmt` を備える。貢献するには clone したリポジトリが引き続き必要 — テスト、28 の翻訳、品質ツールがそこにある — しかし利用するだけなら不要になった。

    - **import 名は `aipmt` であり、決して `translate` ではない**。衝突は実際に発生し、しかも静かに起きるためだ。PyPI パッケージ `translate`（v3.8.1、最終 upload は 2026-07-06）は、同名のディレクトリをインストールする。venv で再現すると、ディレクトリがモジュールより優先され、`translate.main` が消え、entry point は `AttributeError` で壊れる — それでも `pip check` は「No broken requirements found」と rc=0 を返す。ユーザー側の単純な `pip install translate` だけで、診断可能な手がかりなしに CLI が壊れるところだった。実際の wheel で反証：パッケージの上に `pip install translate`、`aipmt --help` は前後とも rc=0、2 つの CLI は共存する。
    - **配布名は長く、コマンドは短く。** `ai-powered-markdown-translator` により PyPI 検索でパッケージを見つけられる；プロジェクトをすでに知っている人以外には略語だけでは見つけられず、今回の公開はまさに発見されることを目的としている。もっともらしい候補 2 つは検証により除外した：`ai-markdown-translator` は 2024 年から npm で同じ目的のツールに使用されており、このリポジトリより 17 か月前から存在する；`aimt` は `aim`（v3.29.1）と 1 文字違いで、同じ分野の現役パッケージ — 長期的な混同にとって最悪の構成だ。ついでに方法上の罠：`pypi.org/project/<nom>/` は bot 対策ページのため、どんな名前でも 200 を返す。信頼できるのは JSON API だけだ。
    - **フラットなパッケージではなく `src/` レイアウト。** フラットなパッケージならテストにある 6 つの `sys.path.insert(..., "..")` を維持できたが、まさにそれが欠陥だった：それらはパッケージではなくソースツリーを import するため、パッケージ化の誤りを隠してしまう。実際のコストは置換ルールを 1 つ追加することだけだった。

  - **キーをようやく一度だけ設定できるようになった。** インストール済み CLI には永続的な設定がなく、環境変数とカレントディレクトリの `.env` だけが残っていた。`find_dotenv` はシステムルートまで遡るため、**ホームディレクトリ配下で作業している場合**には `~/.env` を見つけられたが、別の場所で作業すると何も見つからなかった — カバレッジが設計上の選択ではなく、コマンドをどこから起動したかに依存していた。そのため 3 つ目の層として `~/.config/aipmt/.env` を既存の 2 つの層に追加した。

    - **優先順位をコードで固定しているわけではない**。`load_dotenv` のデフォルト値である `override=False` から導かれる：各層は前の層で空いているものだけを補う。そのため順序は環境変数 → プロジェクトの `.env` → ユーザー設定となる。これは構造ではなく挙動のテストで検証されている — 2 つの呼び出しの順序を逆にすると失敗し、3 つ目の層を削除しても失敗する。
    - **TOML ではなく `.env` 形式**を意図的に採用：`python-dotenv` はすでに依存関係にあり、構文は 15 個の README ですでに文書化され、同じファイルを 2 つのスコープで使える。依存関係も新しい構文もない。場所は `XDG_CONFIG_HOME` が **絶対パス**ならそれに従う — 相対値は無視するよう仕様で定められており、そうしないと設定場所が再びカレントディレクトリ依存になる — Windows では `APPDATA` を使う。
    - **2 つの選択肢を理由付きで除外した。** システムの keyring（`keyring`）はデスクトップではより安全だが、headless — サーバー、コンテナ、CI — では失敗する。これはバッチ翻訳そのものの利用場面であり、opt-in なら有力だがデフォルトには不適切だ。`--api-key` フラグではキーが shell の履歴に残り、`ps` から見えるようになる。
    - **キーがない場合、呼び出しの痕跡を表示しなくなった。** ユーザーには `site-packages` を指す Python のスタックと、「環境または .env」とだけ示すメッセージが表示され、後者をどこに作るのかは不明だった。現在は 3 つの場所を正確なパス付きで列挙し、コマンドは 2 で終了する。保護範囲は**意図的に狭い**：`except ValueError` は設定フェーズだけを対象とする。実行全体を包むと、翻訳中に発生した本当のバグを安心させるメッセージに変えてしまう — このリポジトリが追跡している失敗モードだ。これを禁止するため、`main()` のソースを読むテストがある。

  - **修正 — ユーザーの `.env` は、ツールをインストールすると無視されていた。** 引数なしの `load_dotenv()` はカレントディレクトリからではなく、呼び出し元ファイル、つまり `site-packages` から遡る。独自の `.env` を持つプロジェクトから実際の console entry point を起動して測定したところ、`find_dotenv()` は `''` を返し、キーは読み込まれなかった。一方、`find_dotenv(usecwd=True)` はそれを見つけた。ツールが clone したリポジトリからのみ実行されていた間は存在しなかったバグだが、公開後は常に発生し、正しい設定でも API キーが「不足している」ことだけが症状になるところだった。

  - **3 つの gate は、何も検証しなくなった状態でも green になっていた。** 意図的に移動の**前**に強化した：捕捉すべき変更の後に書かれたガードは何も証明しない。各 gate は元のリポジトリでは green になり、移行したコピーでは red になる — 2 方向とも測定している。

    - **Lizard は存在しないパスを何も言わず無視する**：rc=0、「0 file analyzed」。複雑度 gate は 158 関数 / 2247 nloc から 3 関数 / 34 nloc へ減り、出力は 0 バイトになっていた。現在のスコープは各エントリの存在を検証する配列になっている。
    - **存在しないモジュールに対する `coverage run --source=` は失敗しない**：stderr の警告だけで、unittest でも `coverage xml` でも rc=0、レポートも公開される — ただし 1453 から 141 statements に切り詰められていた。ほとんど分析されていないため、プロジェクトは健全に見えてしまう。2 つの下限でレポートを保護する：合計値と、測定された最大ファイル。
    - **翻訳の鮮度プローブは、呼び出し形式に対して構造的に盲目だった**：argparse の flags を基準にしており、まさにファイル名の変更では変わらない部分だった。再現結果：モジュールを移動しても、15 個の README は存在しないコマンドを記載したままなのに、判定は「古い翻訳なし」。そのため 7 番目のセクションで options ではなく**形式**を検証し、Lizard hook はスクリプトの実際のスコープと照合される — そのキー `files:` は一致しなくても pre-commit を失敗させず、**スキップ**させる。

  - **`requires-python = ">=3.10"` は主張ではなくなった。** `sonar-project.properties` は以前から 3.10-3.12 を告知していたが、開発環境には 3.12 しかなく、実際には一度も検証されていなかった — 公開によって明らかになる内部矛盾だった。現在はテスト workflow が 3.10、3.11、3.12 でスイートを実行し、公開上限を備えた**パッケージ**をインストールする。

  - **下限のみ、上限なし。** `requirements.txt` はテスト済み lock のまま、`[project.dependencies]` は公開契約となる：lock の正確なバージョンを公開すると、他のパッケージを持つすべてのユーザーと衝突する。`<N+1` の上限も設けない — リリース gate を major の遅れ全体で失敗させる `check-deps-fresh.sh` と正面から矛盾するためだ。下限の組み合わせで解決し、`openai==1.0.0` の反証は `ResolutionImpossible` で終了する。これはチェックが何でも受け入れるのではなく、区別していることを示す。さらに `pyproject.toml` のバージョンが CHANGELOG と異なることを禁止するガードもある：PyPI では同じバージョン番号を再利用できない。

  - **新しい venv で最初から最後まで検証済み**：`aipmt/*.py`、dist-info、ライセンスだけを含む約 70 Ko の wheel；22 flags で rc=0 の `aipmt --help`；「usage: \_\_main\_\_.py」ではなく「usage: aipmt」と表示する `python -m aipmt`；動作する `pipx` のインストール；そして何より、**任意のユーザーディレクトリから実行した実際の fr→en 翻訳**で、太字、リスト、inline code、リンク、URL が保持され、コードブロックは翻訳されないこと。移行前の 318 テストは、前後で 1 バイト単位まで同一の識別子リストのまま通過した — テストが無効化されていないことを証明するのは「OK」ではなく、これである。3 層設定用に 12 個が追加され、合計 330 になった。

- **1.10.0** `--use_codex` provider（ChatGPT サブスクリプションの quota）、SDK とモデルを更新、複数段落の news 引用を修正（2026-08-29）：

  - **セキュリティレビュー — PR が設けたものの、すべての箇所で維持できていなかった 2 つのガード：**

    - **Codex の preflight が `.env` 全体をバイナリに渡していた。** `_codex_preflight` は **`env=` なしで** `subprocess.run` を呼び出していた：サブプロセスは `os.environ` 全体、つまり `load_dotenv` が読み込んだ `.env` の完全な内容を継承していた。計測用の偽バイナリで測定すると、preflight に到達した秘密情報は **7 件** — 6 provider のキーと 1 つの `GITHUB_TOKEN` — だった。一方、対応する `_grok_preflight` は正しく `env=_grok_env()` を渡し、**0 件**だった。この不整合は PR 内部のものだった：数行先に、まさにこの不変条件を維持するための `_strip_secret_env` が存在していた。`_codex_env_base()` を抽出して両経路で共有し、修正後に測定すると両方とも秘密情報は 0 件になった。
    - **「`--deny` fail-closed」という性質は、使用された形式を網羅していなかった。** コメントは、未知の prefix のルールが起動を拒否することを根拠に Grok の隔離全体を正当化していた。`grok 1.0.13` で測定すると、この検証は**括弧付き形式に対してのみ**存在する：`--deny 'CeciNestPasUnOutil(*)'` は起動を拒否する（「unknown tool prefix」）一方、`--deny 'CeciNestPasUnOutil'` は黙って受け入れられる。ところが `GROK_DENY_RULES` は裸の名前だけを使用していた — xAI 側でツール名が変更されれば、OS sandbox がすでに適用されない環境で、測定されていた唯一の隔離層が何の通知もなく失われることになる。名前付きの 8 ルールは `Prefix(*)` を通過し、それぞれ CLI の既知の prefix であることを検証する；catch-all の `*` は唯一受け入れられるリテラル形式のままにした。検証されていない形式へ戻らないようテストで防止している。
    - **その他は問題なく検証済み**：コマンドインジェクションなし（どこでもリスト形式、`shell=True` は決して使わない。文書内容は stdin または `--prompt-file` 経由）、安全でないデシリアライズなし（型ガード付きの `json.loads` のみ）、7 つの payload で迂回なしのパス走査修正、そして `--deny '*'` が CLI によって実際に適用されること（workdir 外の読み取りで `DENY_ENFORCED` を確認）。
    - 上で追加した鮮度チェックも、その原則自体を迂回していた：PyPI リクエストに失敗したパッケージは黙ってスキップされ、gate は green になっていた。現在は実際に比較されたパッケージ数を数え、カバレッジが不完全なら失敗する。

  - **依存関係を更新し、遅れを再発させないための 2 つの仕組みを追加：**

    - **遅れは実際に存在し、長期化していた**：`openai` 2.54 → **3.6.0**、`anthropic` 0.125 → **1.2.0**、`certifi` 2024.8.30 → **2026.7.22** — すべての provider 呼び出しで TLS を検証するルート証明書ストアが 2 年遅れていた。原因は **`.github/dependabot.yml` が存在しなかった**こと。これがないと GitHub は _security updates_ だけを有効にし、Dependabot は CVE の対象になっている依存関係に対してしか PR を提案しない — そのため `urllib3` と `idna` は bump したのに、2 つの SDK は major version から取り残されていた。
    - **2 つの major は衝突せず共存する**。以前の推論では衝突が懸念されていたが、`openai` 3.x と `anthropic` 1.x は `httpx2` へ移行し、`mistralai` と `google-genai` は `httpx<1` に残る。しかしこれは別々の distribution である。実際にインストールして検証し、さらに **7 つの provider 経路をすべてエンドツーエンドでテスト**した — OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI、Grok CLI — 各出力で inline code とリンクを保持した。「HTTP stack を 2 つ避ける」は好みであって障害ではなく、測定によって決着した。
    - **`requirements.txt` は実際の環境を記述していなかった**：`google-auth`、`cryptography`、`opentelemetry` の stack は作業用 venv にインストールされていたのに、宣言されていなかった — そのため fresh install ではテスト対象を再現できなかった。逆に、`tokenizers`、`huggingface-hub`、`PyYAML` はそこに記載されていたが、何からも import も要求もされておらず、`mistralai` 1.x の残骸だった。ファイルは、直接依存関係だけから構築した venv の完全な closure として再生成された。`pip-audit` は新しい構成に既知の脆弱性がないことを報告している。
    - **`.github/dependabot.yml`**（新規）は、version、pip、github-actions の週次更新を有効にする。マイナーとパッチは 1 つの PR にまとめる — PR ごとに 1 つの patch bump では無視され続け、ノイズは更新の敵になるためだ；**major は分離**し、それぞれ実際の呼び出しによる検証を要求する。
    - **`scripts/check-deps-fresh.sh`**（新規、gate に接続済み）は、遅れをプロジェクトの判定に表示する：Dependabot は提案するだけで保証はせず、PR が積み重なることもある。major の遅れ → 失敗；minor → 警告。gate が常に赤だと最終的に無視されるためだ；PyPI に到達できない場合 → ローカルでは明示的に skip、**CI では fail-closed**。実行されていないチェックは成功ではない。両方向で検証済み：修正前の正確な状態（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`）を検出し、minor については警告だけを出す。

  - **この PR のレビューから生じた修正** — 5 人のレビューエージェントが diff を精査し、以下の項目はすべて修正前に**測定によって再現**された。そのうち 2 つは、この同じバージョンで上に導入された回帰だった。
- **回帰を修正 — `_NEWS_CITATION_REGEX` に指数バックトラッキングがあった。** 複数段落対応の修正で、繰り返し内に `(?:[ \t]*$|[ \t]+.*)` が導入されていた。`[ \t]+` と `.*` の間で空白を共有する方法が曖昧で、その曖昧さが反復のたびに増幅していた。パターンにマッチしない `>   texte` 行、つまり完全に合法な Markdown のインデントで測定したところ、修正前は**14行で2,589 ms**だったのに対し、修正後は0.04 msとなり、1行追加するごとに約9倍に増加していた。`--news` モードでは、長く不正な blockquote だけで翻訳がジョブのタイムアウトまで停止し、原因も特定できなかった。現在は繰り返しが行全体を一括で消費する（`\n^>(?![ \t]*—).*`）ため、反復ごとのマッチ方法が1つしか残らない。実際の231記事のコーパスで検証し、**捕捉結果に差異はゼロ**、同じ423件の引用、複数段落の14本文もすべて従来どおり展開されることを確認した。
    - **provider のフラグを2つ同時に指定すると、気付かないうちに従量課金になっていた。** `--use_codex --use_mistral` は受け付けられていた。`_select_provider_client` は最初に Mistral を検査し、`_resolve_provider` は明示的なブール値を優先するため、どちらも Mistral に収束していた。ユーザーはサブスクリプションの割り当てを求めていたのに従量課金となり、警告は一切表示されなかった。これはまさに `--use_codex` が防ぐために存在する障害モードである。現在、6つの provider フラグはすべて `add_mutually_exclusive_group` を通過する。**挙動の変更**：これまで暗黙に受け付けられていた、2つの provider を組み合わせたコマンドラインは、現在は `argument --use_mistral: not allowed with argument --use_codex` で失敗する。
    - **終了ゲートは、プローブがクラッシュしても成功になっていた。** `scripts/check-release-ready.sh` の13個の検証のうち4つが、「標準出力を捕捉し、空なら問題なしと判断する」というパターンに従い、終了コードを一度も確認していなかった。例外（ファイル名の変更、`FileNotFoundError`）は標準エラー出力に書き込まれ、標準出力は空のままになり、検証は「報告するものなし」と判断していた。これを防ぐために書かれたスクリプト自体に、「空の `exit 0` には証拠能力がない」という落とし穴が組み込まれていた。現在はヘルパー `probe()` が、終了コードが0であること**および**終了センチネルの存在を要求する。また、プローブは参照集合が空の場合に判断を下さない。空集合に対するアサーションは常に真だからである。実例として、上記の排他的グループを追加した結果、provider フラグは `*_group` オブジェクトを通るようになり、旧来の正規表現 `parser\.add_argument\(` はマッチしなくなった。その結果、**21個中6個のフラグ**が静かに検査範囲から外れ、ゲートは成功になっていた。
    - **シークレットのスキャンが6つ中4つの provider を見逃していた。** クラス `[A-Za-z0-9]` はハイフンを除外するため、`sk-proj-…`（現在の OpenAI 形式）と `sk-ant-api03-…` は2つ目のハイフンで失敗し、`AIza…` も対象外だった。パターンを拡張し、`.secrets.baseline` をスキャン対象から除外した。さらにガード `.env` は `git diff --cached` を照会していたが、これはインデックスしか見ないため、**すでにコミット済み**の最悪ケースである `.env` は決して表示されなかった。現在は `git ls-files` を照会する。
    - **Codex の「トークンのウォームアップ」は実際にはウォームアップではなかった。** 測定の結果、`codex login status` は `~/.codex/auth.json` にアクセスせず（mtime とサイズは不変）、ヘルプには「ログイン状態を表示」と記載されていた。一方、コメントはローテーションする使い捨てトークンでの同時更新リスクを無効化するため、「逐次的に1回」トークンを更新すると主張していた。宣言された保護機構は存在しなかった。現在、コメントはコードの実際の動作を説明しており、実際の対策は引き続き `max_jobs=4` である。さらに検査は、これまで無視していた `CODEX_BIN` に対応する。`codex` が `PATH` にない環境では「未認証」となっていたが、これは誤解を招く診断だった。
    - **`.env` がサブシェル内で読み込まれていた。** `detect_provider` はコマンド置換で呼び出されるため、そこでの export は外側に伝わらなかった。`.env` で定義された `GROK_BIN`、`GROK_HOME`、`REGEN_MODEL` は `main()` からの読み取りでは見えず、正しい設定でも「Grok バイナリが見つからない」と判断されていた。
    - **同時実行数が公表された上限を50%超えていた。** ガードが README/CHANGELOG のペアを起動した後に置かれていたため、測定されたピークは **`max_jobs=2` が3** だった。週間割り当てを Chat/Imagine/Voice と共有し、測定もできない Grok では、スクリプトが自らに課した上限が守られていなかった。最終カウントは表示されていたものの、28との比較は一度も行われておらず、ファイルの欠落が見逃されていた。
    - **Grok の出力契約：`stopReason` がない場合も、現在は失敗になる。** コードは、宣言された契約が `end_turn` を要求している箇所で「`end_turn` **または欠落**」を適用していた。フィールドのないペイロードや、CLI の更新でフィールド名が変更されたペイロードは、ガードを静かな no-op に変えていた。また `max_turn_requests` はレート制限として分類されなくなった。これはラウンド予算が尽きた状態であり、再試行しても90秒待った末に同じ結果になるためである。さらに `quota` はレート制限のマーカーから外れた。これは `_codex_is_rate_limited` の docstring がすでに説明していた理由を、Grok が適用していなかったためである。
    - **Gemini のフォールバックがモデル単位でメモ化された。** セグメントごとに `minimal` から再開していたが、デフォルトモデルはこれを拒否するため、通常経路ではセグメントごとに400の往復を行い、同じ警告を再表示していた。警告が何百回も繰り返されると読まれなくなる。それが警告を隠れ蓑に変える。
    - **その他**：CI での拒否メッセージが Codex 用にハードコードされており、`--use_grok_cli` のユーザーを `XAI_API_KEY` ではなく `OPENAI_API_KEY` に誘導していた。`provider.capitalize()` は「Grok_cli」と「Openai」を表示していた。サブプロセス基盤のコメントは「shim」を両方の CLI に一般化していたが、Grok のバイナリはネイティブ ELF である。正しい説明は「独自のサブプロセスを spawn するエージェント」である。`subprocess` に関する12件の SAST findings は、理由を添えて `# nosec` / `# nosemgrep` としてマークされている。`shell=True` のないリスト形式ではインジェクションが不可能であり、ドキュメントの内容が argv を通過することもない。
    - **エージェントのサブプロセスにシークレットが入ることはなくなった。** 名前を列挙した deny-list は、**課金**に関する不変条件（`OPENAI_API_KEY` のない Codex、`XAI_API_KEY` のない Grok）しか保護していなかった。測定の結果、さらに**7つのシークレット**が各サブプロセスに入っていた。Anthropic、Mistral、Google、Gemini のキー、もう一方の CLI のキー、そしてシークレットではないが通信を別経路へ向ける `OPENAI_BASE_URL` である。この2つの CLI は**エージェント**であり、Grok のエージェントは多くの Linux 環境で適用可能な OS サンドボックスなしに動作する。現在は名前の列挙ではなく、**名前のパターン**（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`）でフィルタリングする。これにより、このコードが把握していない変数をユーザーが `.env` に追加した場合も対象になる。CLI に必要なものはない。認証情報は `~/.codex` と `~/.grok` に保存され、環境変数には決して置かれない。強化された環境で両方の provider を使い、**実際に完了する翻訳**によって検証した。
    - **テスト**：新しい `tests/test_review_hardening.py` ファイル（21テスト）を追加し、provider フラグの排他性、`stopReason` 契約、news 正規表現の線形性、CI での拒否メッセージ、Gemini のメモ化、サブプロセス環境にシークレットが存在しないことを固定した。最後のアサーションは**汎用的**であり、どのリストにも記載されていないキーでも失敗する。一方、既存の消去テストは自身の定数を鏡写しにしたもので、自身のループの故障以外は検出できなかった。全体のテスト数は**311件**になった。

  - **2つの新しい Grok provider**：`--use_grok`（xAI API、`XAI_API_KEY` キー、従量課金）と `--use_grok_cli`（公式 Grok Build CLI、Grok サブスクリプションから差し引き — `--use_codex` と同じ方式）。
    - **API モード、約40行**：xAI のエンドポイントは OpenAI 互換であるため、クライアントと `_call_openai` はそのまま再利用し、変更するのは `base_url` だけである。必要な適応は1つだけで、それは全体に恩恵をもたらす。`finish_reason` が `end_turn` を受け付けるようになった。これは xAI が出力する形式であり、OpenAI は `stop` を出力する。モデルは `grok-4.6`（品質）と `grok-4.3`（エコノミー）。なお、Grok のエコノミーモデルはリポジトリ内で最も高価なままであり、100万トークンあたり $1.25/$2.50、`mistral-small-latest` は $0.15/$0.60 である。この provider は価格ではなく、モデルの多様性を理由に選ぶものだ。
    - **CLI モード**：Codex を踏襲しているが、実環境上の4つの相違点がある。プロンプトはファイルで渡す（`--prompt-file`。CLI は stdin を読まず、セグメントを argv に渡すと `ps` から見えてしまう）。出力は stdout 上の単一 JSON オブジェクトである（JSONL でも `-o` ファイルでもない）。サブスクリプションが公開するのは `grok-4.6` と `grok-4.5` だけである。また、サンドボックスは適用できない（下記参照）。サブプロセスの起動は `_codex_run_process` で Codex と共通化し、すでにテスト済みの Codex provider の残りには触れていない。
    - **測定結果：`exit 0` には証拠能力がない**：未認証でも CLI は **stdout** に `{"type":"error","message":"Not signed in."}` を書き、終了コードは **0** になる。拒否やラウンド超過も同じ挙動をする。そのため出力契約は4条件を同時に要求する。終了コードが0、エラーペイロードがない、`stopReason == end_turn`、そして空でないテキストである。preflight も同じ論理に従う。`grok models` は接続が切れていても0を返すため、stdout に「not authenticated」が存在する場合にのみ判断できる。
    - **隔離：非対称性を受け入れ、文書化した。** Codex が `--sandbox read-only` で動作するのに対し、最近の Linux 環境の多くでは Grok のサンドボックスを適用できない。`sudo` なしには回避できない、独立したシステム上の原因が2つある。Ubuntu 24.04 以降では AppArmor が非特権ユーザーネームスペースをブロックする（`bwrap: setting up uid map: Permission denied`。Grok 外でも再現）。また、`/run/podman` が `0700` の場合、コンテナランタイムソケットの deny-list が失敗する（resolver が回復できるのは `ErrorKind::NotFound` だけで、EACCES は致命的になる）。中心的な落とし穴は、適用できない**組み込み**プロファイルが、**隔離されていない状態で静かに起動する**ことだ。そのためスクリプトはデフォルトでプロファイルを要求せず、決して静かにフォールバックしない。stderr に警告を出す。保護は CLI の `--deny` ルール（catch-all の `*` を含む）に依存する。これは測定済みで唯一の _fail-closed_ 層であり、未知のプレフィックスを持つルールが起動を拒否させる。`GROK_TRANSLATE_SANDBOX=read-only` を使えばこれを必須にでき、その場合、マシンが適用できなければ起動は失敗する。
    - **ガードレール**：`XAI_API_KEY`、`GROK_API_KEY`、`GROK_SANDBOX` をサブプロセスの環境から削除する（キーがあると従量課金に切り替わり、継承された `GROK_SANDBOX` が適用不能なプロファイルを強制して誤解を招くメッセージを出す）。MCP/hooks/skills/agents のスイッチを無効化し、`--disable-web-search`、`--no-subagents`、`--no-plan`、使い捨ての workdir、CI での拒否、プロセスグループを強制終了するタイムアウト、レート制限時のバックオフを設定する。`--max-turns` は1ではなく6に固定する。ツールのターン後にカウンターが増分されるため、1では出力が切り詰められる。
    - **クォータ**：Grok のプールは週間単位で、**Chat、Imagine、Voice と共有**されており、これを公開するコマンドはない。`account/rateLimits/read` で消費量を算出できる Codex とは異なる。そのため `regen_translations.sh` は同時実行数を2に制限し、明示的に警告する。
    - **テスト**：新しい `tests/test_grok_provider.py` ファイル（24テスト）。全体のテスト数は**290件**になった。
  - **バグを修正 — EN の複数段落の引用が、`--news` モードでは一部しか保護されていなかった**：`_NEWS_CITATION_REGEX` は引用本文として、`>` 行が**連続する**並びしか受け付けていなかった。引用が複数の段落（`>` の空行で区切られる）にまたがると、最後の段落だけが捕捉されてプレースホルダーに置換され、それ以前の段落は LLM に送られて翻訳されていた。これは `--news` が保証するために存在する目的と正反対である。現在は繰り返しが内部の `>` 空行を受け入れ、貪欲でないマッチになった。そのため最初に見つかった空行ではなく、斜体行の直前にある `>` 空行で停止する。
    - **測定した規模**：実際の198記事のコーパスで、該当する引用は419件中11件だった。回帰はなく、新しい正規表現が捕捉する引用数は完全に同じで、複数段落の本文だけが拡張された（408本文は同一、11本文は拡張）。帰属行 `> — …` が本文に取り込まれることもない（lookahead は維持）。
    - **エンドツーエンドの証明**：69 KB の記事を ja/ar に翻訳して確認した。以前は引用の最初の段落が日本語で `> GLM-5.3がオープンウェイト化。` として出力され、アラビア語でも同様に翻訳されていたが、現在は `> GLM-5.3 is now open-weight.` のままになる。英語の引用行数は9行から10行に戻り、ソースと一致する。
    - なお、この欠陥は後段のバリデーターでは検出されなかった。バリデーターは引用の存在だけを確認し、完全であるかどうかは検査していない。
  - **デフォルト provider で測定した節約**：`_openai_extra_kwargs` は、モデル名が `gpt-5` で始まると、`--eco` であっても `reasoning_effort="medium"` を送信していた。10語の文を翻訳する `gpt-5.4-mini` で測定した結果、`medium` は推論トークン45、出力トークン65だったのに対し、`none` は0と14だった。推論は翻訳に何ももたらさず、各ファイルの各セグメントで課金されていた。デフォルトは `--eco` では `none` となり、それ以外では `medium` のままとなる。CLI で明示的に渡した値は引き続き優先される。`--reasoning_effort` は `low`/`medium`/`high` に加えて、`none` と `xhigh` も受け付けるようになった（すべてのモデルがすべての値を受け付けるわけではない。たとえば `gpt-5.4-mini` は `minimal` を拒否するが、既存のパラメーターなしリトライがこのケースを処理する）。
  - **SDK の更新と Gemini の移行**：`google-generativeai`（2025-11-30 にサポート終了、リポジトリはアーカイブ済み）を、統合 SDK **`google-genai`** に置き換えた。`genai.Client(api_key=...)`、続いて `client.models.generate_content(model=, contents=, config=)` を使用し、セグメントに連結する代わりにシステムプロンプトを `system_instruction` として渡す。`mistralai` は **2.9.4** に更新した（インポートは `from mistralai.client import Mistral` となり、旧形式は `ImportError` を発生させることを wheel 内で確認）。`anthropic` は **0.125.0**、`openai` は **2.54.0** とした。これは `httpx2` への移行前の最後のバージョンであり、venv 内に2つの HTTP スタックを共存させないためである。これに伴い `httpx` 0.28.1 と `pydantic` 2.13.5 の利用が可能になった。
  - **実際のテストで発見され、ドキュメントでは発見できなかった2つの回帰**：
    - `anthropic` 1.0 以降では、`max_tokens` が10分超を示唆する非ストリーミング呼び出し（`ValueError: Streaming is required...`）をクライアント側で拒否する。このガードレールは0.34.2にはなく、`max_tokens=32768` を指定した Claude の呼び出し全体を壊していた。明示的な `timeout`（デフォルト900秒の `CLAUDE_TIMEOUT`）を設定して修正した。これにより、完全な応答だけを利用する呼び出しがストリーミングへ切り替わることを避けられる。
    - `thinking_level="minimal"` は Gemini のカタログの一部のモデルでしか受け付けられない。`gemini-3.1-flash-lite` は対応するが、`gemini-3.7-flash` と `gemini-3.1-pro-preview` は400で拒否する。そのため `_gemini_generate_with_fallback` を導入した。これは `minimal` → `low` → thinking_config なしというフォールバックであり、既存の OpenAI フォールバックを踏襲する。最適化用パラメーターによって翻訳が失敗してはならない。
  - **デフォルトモデルを更新**し、それぞれ実際の呼び出しで検証した。OpenAI は `gpt-5.5` から **`gpt-5.6-terra`** へ（28件のバッチで−60%）、`gpt-5.4-mini` から **`gpt-5.6-luna`** へ（−73%）。Claude は `claude-sonnet-4-6` から **`claude-sonnet-5`** へ（より安価で新しい）、`claude-haiku-4-5-20251001` から **`claude-haiku-4-5`** へ（日時のない正規 ID）。Gemini は `gemini-3.1-pro-preview` から **`gemini-3.7-flash`** へ、`gemini-3.1-flash-lite-preview` から **`gemini-3.1-flash-lite`** へ（安定版で、`3.5-flash-lite` より安価）。
Mistralは変更されておらず、4つの中では`mistral-large-latest`が引き続き最もコストパフォーマンスに優れています。なお、`gemini-3.1-pro-preview`より新しいProシリーズのGeminiモデルは存在しません。2026年5月に発表されたGemini 3.5 Proはリリースされておらず、3.5/3.6/3.7のラインはFlash専用です。
  - **Geminiへの切り替え前に測定したA/Bテスト**：`README.md`を`gemini-3.1-pro-preview`で日本語に翻訳し、その後`gemini-3.7-flash`で翻訳。構造は完全に同一（21個のリスト、18個のコードブロック、13個のHTMLリンク、13個の画像、すべてのURLを保持）で、**48秒に対して8秒**でした。これら2つのモデルを翻訳や非ラテン文字のスクリプトで比較した公開ベンチマークは存在しないため、測定しなければ切り替えは単なる推測に基づくものでした。
  - **Claudeの応答ブロックのフィルタリング**：`_call_claude`は種類をフィルタリングせずに`block.text for block in response.content`していました。適応型推論モデル（Sonnet 5以降）は`thinking`ブロックを挿入しますが、これは`.text`ではなく`.thinking`を公開するため、翻訳は最初のセグメントで不透明な`AttributeError`に遭遇すると失敗していました。現在は`thinking`、`redacted_thinking`、`tool_use`、`tool_result`を除外しています（未知の種類でテキストを含むものにも対応できるよう、除外リスト方式）。テキストブロックが1つもない応答では、明示的なエラーが発生します。`thinking={"type": "disabled"}`は各呼び出しに渡されるようになりました。
  - **`MODEL_TOKEN_LIMITS`を再同期**：廃止日を過ぎたモデルを削除（`magistral-*`シリーズは2026-07-31、`gemini-2.0-*`は2026-06-01、`gemini-3-pro-preview`は2026-03-09に廃止、`claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。上限を修正：Mistralは128Kから**256K**へ（Large 3 / Small 4の生成）、Geminiは1 000 000から**1 048 576**へ（実際の入力上限）、`claude-opus-4-5`は200Kから**1M**へ、`gpt-5.6-*`ファミリーは400Kから**1.05M**へ。Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest`、`ministral-*`シリーズを追加。なお、これらの上限はあくまで目安であり、`translate()`が分割を`min(16000, limite)`に制限しています。

  - **Provider `--use_codex`**：公式Codex CLI（`codex exec`）を非対話モードで操作する5番目のプロバイダーです。従量課金のAPIを呼び出す代わりに、すでに支払い済みのChatGPTサブスクリプションのクォータから翻訳分が差し引かれます。これはOpenAIがこの用途向けに文書化している唯一の方法です。プラン別利用可能機能の一覧では、「Codex SDK、`codex exec`、and scriptable workflows」がPlus/Pro/Business/Enterpriseで利用可能とされています。一方、`~/.codex/auth.json`のトークンではPlatform APIへの呼び出しを認証できず、このスクリプトから読み取られることもありません（認証と更新は引き続きCLIが管理します）。
  - **pipでインストール可能なCodexバイナリ、npmだけではなく対応**：`_resolve_codex_binary()`はまず`CODEX_BIN`でバイナリを探し、次に`PATH`、その後OpenAIが公開している公式Pythonパッケージ **`openai-codex-cli-bin`**（SDK `openai-codex`の依存関係）を探します。したがってPythonプロジェクトでは、`--use_codex`を使用するためにnpmのグローバルインストールが不要になりました。パッケージは`requirements.txt`には追加していません。バイナリのサイズが約250 MBあり、オプションのプロバイダーのために全ユーザーへ強制することになるためです。エンドツーエンドで検証済みです。`codex`が`PATH`に存在しない状態でも、解決処理はパッケージ化されたバイナリを見つけ、完全な翻訳が6秒で完了しました。
  - **「サブスクリプションモード」の保証**：`OPENAI_API_KEY`と`CODEX_API_KEY`はサブプロセスの環境から削除されます。この保護がなければ、`.env`に存在するキーによってCodexが何の目に見える通知もなく従量課金へ切り替わる可能性があります。まさにこのプロバイダーが防ぐために存在する事態です。
  - **CLIの落とし穴をテストで固定**：
    - `codex exec`は、プロンプトを引数で渡した場合**でも**stdinを読み取ります。stdinを閉じないと、モデルを一度も呼び出さずにコマンドがタイムアウトまで待機します（再現結果：180秒後に終了コード124、0バイト）。そのため`communicate(input=...)`は必須です。
    - npmでインストールされる`codex`は、実際のRustバイナリを`spawn`するNodeのshimです。このバイナリはPythonプロセスの**孫プロセス**であり、`subprocess.run(timeout=)`の`SIGKILL`後も生存してクォータを消費し続ける可能性があります。そのため`Popen(start_new_session=True)`と`os.killpg`が必要です。
    - CLIは`turn.failed`を出力しながら終了コード0を返すことがあります。JSONL出力（`--json`）を終了コードに加えて検査し、終了コード0なのに`-o`がない場合は、空のセグメントを生成する代わりに明示的なエラーを発生させます。
  - **レート制限時のバックオフ**：CLIには内部リトライが実装されていません（`max_retries = 0`）。分類は部分文字列ではなくJSONペイロードの構造（`status: 429` / `error.type`）に基づいて行います。「quota」という語は、回復可能な429エラーにも`insufficient_quota`という恒久的なエラーにも現れるためです。
  - **CIガード**：`--use_codex`は、`CI`または`GITHUB_ACTIONS`が定義されている場合は拒否されます。サブスクリプション認証は共有ランナー向けに設計されておらず、OpenAIも公開リポジトリでこのワークフローを使用しないよう明示的に推奨しています。
  - **モデル**：`gpt-5.6-sol`（品質）と`gpt-5.6-luna`（`--eco`）。`gpt-5.6-*`ファミリーはCLIとPlatform APIで共通ですが、ChatGPTアカウントですべてを利用できるわけではありません。allowlistはローカル検証なしにサーバー側で適用され、通常と異なるモデルを指定すると警告が発生します。Plusプランでは、Lunaは5時間のウィンドウあたり250～2,000メッセージ、Solは10～100メッセージです。`--eco`があらゆるバッチ処理に推奨されるモードです。
  - **修正済みのバグ — 完全に成功しているのに`regen_translations.sh`がエラーになっていた**：`trap ... EXIT`は`failed_log`を参照していました。これは`main()`の`local`であり、trapが実行される時点では存在しません。`set -u`では、これにより`failed_log: unbound variable`が発生し、28件の翻訳が正しいにもかかわらずスクリプトが1で終了していました。その結果、最もコストの高い再生成直後の段階で`release.sh --auto`（`set -e`）が中断されていた可能性があります。変数をグローバルにし、trapではその存在を検査するようにしました。副次的な効果として、これまでこのエラーに隠されていた実際の翻訳失敗が、終了時の概要に再び表示されるようになりました。
  - **`REGEN_MODEL`**：`regen_translations.sh`の新しい環境変数で、プロバイダーのデフォルト設定より優先して特定のモデルを強制します。たとえば`REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`を指定すると、ボリューム重視の`--eco`ではなく、サブスクリプションのクォータで利用できる上位モデルを使って再生成できます。
  - **`regen_translations.sh`**：明示的なオプトインで`REGEN_PROVIDER=codex`を利用可能にします（ユーザーが知らないうちにサブスクリプションのクォータを消費しないよう、自動検出は行いません）。Codexの更新はローテーション式で一度しか使用できず、並行ジョブがセッション`codex login`を無効化するため、並列処理を開始する前にトークンを一度だけ順番に更新し、同時実行数を4に下げます。
  - **関連リファクタリング**：`_dispatch_provider_call`のパラメーター数を8個から6個に減らしました。`_resolve_provider()`によってプロバイダー名を返す方式にし、チェーン全体へ4番目のブール値を伝播させる必要をなくしました。`args`より明示的なブール値を優先することで、最小限の`Namespace`を指定して`translate(..., use_mistral=True)`を呼び出すテストとの互換性を維持しています。
  - **テスト**：新しいファイル`tests/test_codex_provider.py`（48テスト）で、argv、消去済み環境、前置き禁止契約、サイレント失敗、timeout/killpg、バックオフ、preflight、プロバイダー解決、Geminiの推論カスケード、Claudeブロックのフィルタリング、複数段落のニュース引用をカバーします。全体のテスト数は290件になりました。
  - **実環境での検証**：プロジェクトの`README.md`をCodexで**14言語**に翻訳した結果、参照翻訳と完全に同一の構造になりました（コードブロック14個、見出し24個、表の行25個、HTMLリンク13個、画像13個、URL19個、コードブロックは1文字単位で完全一致、プレースホルダーの残留ゼロ）。`--news`モードで69 KBのニュース記事を処理したところ、`gpt-5.6-luna`と`gpt-5.6-sol`の出力はいずれも、en/ja/arの下流アプリケーションバリデーターを通過しました。`account/rateLimits/read`で測定した消費量は、`--eco`モードで5時間ウィンドウのカウンターの丸め閾値未満（0%）に収まりました。

- **1.9.2** ニュース帰属URLの抽出修正：入れ子の括弧またはFR接頭辞（2026-05-11）：

  - **修正済みのバグ**：`_protect_news_quotes`における帰属URLの抽出では、`re.search(r"\((.+?)\)", attribution)`という正規表現（括弧間の遅延キャプチャ）を使用していました。`(relayé par [@user sur X](https://x.com/.../123))`のような帰属（入れ子の括弧：外側の`(`とMarkdownリンクの`]()`）では、キャプチャが最初に現れた`)`で停止し、文字列が途中で切れました。さらにFR接頭辞`relayé par [@user sur X](https://x.com/.../123`も含まれ（末尾の`)`なし）、`_validate_news_post`は翻訳後の出力からこの文字列を探すため、常に失敗していました。理由は2つあり、`)`が途中で切れていることと、「relayé par」が`relayed by`/`weitergeleitet von`/などに翻訳されることです。low → medium → high → gpt-5.5の完全なカスケードも通過できませんでした。
  - **修正**：正規表現を`re.search(r"\]\(([^)]+)\)", attribution)`に変更しました。Markdownリンクの`](url)`だけを対象にし、**純粋なURLだけ**（FR接頭辞や途中切れなし）をキャプチャします。翻訳中は`#URL{N}#`のプレースホルダーによって不変性が維持されます。問題の2つのパターンに対応します。
    - `(relayé par [@account sur X](url))` — 入れ子の括弧
    - `via [@source](url)`または`selon [@author](url)` — 外側の括弧なしのFR接頭辞
  - **テスト**：`test_silent_failure.py`の`TestNewsCitationExtraction`クラスに2件追加：
    - `test_extract_attribution_url_with_nested_parens`（Genspark CEO E2Bで実際に再現したバグと同じケース）
    - `test_extract_attribution_url_with_french_prefix`（`via`を含むバリエーション）
  - **未対応のカバレッジ**：`check-editorial-coverage.py`は編集上の構文を検証しますが、translatorによる翻訳可能性は検証しません。将来的な改善案（v1.9.2の範囲外）として、公開前にリスクのあるパターンを検出するため、dry-runで帰属抽出をシミュレートするチェックが考えられます。

- **1.9.1** 翻訳マーカー注記のCTAラベルをi18n化（2026-05-10）：

  - **修正済みのバグ**：翻訳済みファイル上部のマーカーバナーにあるCTAリンクの`[Voir le projet sur GitHub ↗]`が、`target_lang`に従わず、すべての対象言語で**フランス語のまま**になっていました。Python側でURLとリポジトリのslugを保持するために組み立てられており、LLMからは一度も見えないため、翻訳フェーズで修正できませんでした。これはv1.9で`marker`形式を追加して以来のサイレントなリグレッションでした。
  - **修正**：15言語のローカライズラベルを対応付ける新しい定数`_VIEW_PROJECT_LABELS`を追加しました。`_translation_note_invariants(target_lang)`と`_assemble_translation_note_paragraphs(phrase, target_lang)`が対象言語を渡すようになりました。未知の言語の場合は`fr`にフォールバックします（安全対策であり、KeyErrorを防止）。
  - **テスト**：`test_source_emits_three_paragraphs_repo_title_description_link`を調整（target_lang `ja` → 期待される日本語ラベル）。新しいテストを2件追加：`test_source_link_label_localized_per_target_lang`（ラテン文字、表意文字、アブジャドの各スクリプトを含む7言語でパラメーター化）と`test_source_link_label_falls_back_to_french_for_unknown_target`。合計は`test_translation_note_position.py`内の40テスト（38件から増加）になりました。
  - **後方互換性**：デフォルト値`target_lang="fr"`付きのシグネチャにより、`args.target_lang`を指定しない外部のプログラム呼び出しも変更なしで引き続き動作します。
- **1.9** サイレント失敗の修正 + 完全な品質ツールチェーン + 複数位置対応の翻訳注記（2026-05-07）：
  - **複数位置対応の翻訳注記 + 「embed card」形式マーカー**：
    - 新しい CLI オプション（追加機能、デフォルトは変更なし → **後方互換性あり**）：
      - `--note_position {top,bottom,both}`（デフォルト：`bottom`）：翻訳ファイルの上部、下部、または両方に注記を配置します。
      - `--note_format {legacy,marker}`（デフォルト：`legacy`）：
        - `legacy` は v1.8 の動作（太字の段落 `**…**`）を**バイト単位で完全に**再現します。
        - `marker` は、非表示の Markdown リンク参照定義（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）に続いて、「GitHub リポジトリ埋め込みカード」風の表示用に構造化された**3 段落の blockquote**を出力します。内容は、インラインコード内のプロジェクト名（`**\`ai-powered-markdown-translator\`\*\*`）、LLM が翻訳した説明、矢印が表示される CTA リンク（`[Voir le projet sur GitHub ↗](URL)`）です。remark プラグインでビルド時に利用できます（jls42.org のブログ → プラグイン `remark-translation-banner`）。
    - **LLM に送信されない不変要素**：リポジトリ名と GitHub URL は、説明文の翻訳後に Python 側で組み立てます。LLM がスラッグ `ai-powered-markdown-translator` や `https://github.com/jls42/...` を見ることはないため、renderer、エスケープ、scheme が変更されることはありません。
    - **frontmatter 対応の挿入**：`top` または `both` モードでは、注記を YAML frontmatter の**終了 `---` ブロックの後**に挿入します。ヘルパー `_split_frontmatter` はファイル先頭の `---\n…\n---\n` を検出して整合性を保持し、終了 fence のない未完了の frontmatter では **`RuntimeError` を送出**します（注記が誤った位置にある状態で書き込まず、ファイルは `failed_files` に送られます）。
    - **モデルの whitelist sanitizer**：`_sanitize_model` は `[A-Za-z0-9._:/-]` 以外のすべての文字を `_` に置換し、空の場合は `unknown` にフォールバックします。remark Astro プラグイン側のバリデーターと整合し、マーカー形式を壊す文字（空白、引用符、括弧、コンマなど）を無効化します。
    - **内部リファクタリング**：`_append_translation_note`（1 つの巨大な関数）から 7 つの純粋なヘルパー（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）へ変更しました。builder と composer を分離し（builder は区切り文字を含まない純粋なブロックを返し、composer は位置に応じて `\n\n` を適用）、生成処理とソースヘルパーは同じ 3 段落アセンブラーを共有します。
    - **`_quote_lines` による空行保持**：各行の先頭に `> ` を付け、空行を `>` のみに変換します。これにより mdast は blockquote 内の 3 つの段落（タイトル / 説明 / リンク）を、改行を含む 1 つの段落ではなく別々に認識できます。
    - **`_build_translation_note_block` による適応処理**：LLM が保持した段落数に応じて処理します（3 = 完全なカード形式、2 = 文 + リンク、1 = フォールバック）。1 段落のフォールバックでは、Markdown リンク `](` が検出された場合、`**...**` で囲まなくなりました（リンク周辺の `<strong>` の表示が不安定になるため）。
    - **後方互換性**：`_compose_with_notes` 側の `getattr(args, "note_position", "bottom")` と `getattr(args, "note_format", "legacy")` — これらの属性を持たない Namespace（既存テスト、外部のプログラム呼び出し）も変更なしで引き続き動作します。
  - **長い翻訳におけるサイレント失敗の修正**：
    - すべての provider（OpenAI、Mistral、Claude、Gemini）で翻訳後の言語を検証：決定論的レイヤー（元の抜粋が逐語的に再現されているか）+ 確率論的レイヤー（`langdetect`）
    - `finish_reason` / `stop_reason` の whitelist：whitelist 外の状態（truncation、content_filter など）では `RuntimeError` を送出
    - Claude の `max_tokens`：`4096` → `32768`（16k セグメントでの潜在的な truncation を回避し、FR→JA/ZH/KO/AR/HI の異なる文字体系に対応する余裕を確保）
    - 見出しを考慮した分割：セグメント後半では H2/H3 を優先し、各セグメントが完全な意味単位のセクションから始まるようにします。
    - エラーを exit code が非ゼロになるまで伝播：`translate_markdown_file` は型付きステータス `success` / `failure` / `skipped` を返し、少なくとも 1 ファイルが失敗した場合は `main()` `sys.exit(1)`（単一ファイルと batch の両方）
    - すべての provider に空コンテンツガード、元テキストと出力の妥当性比率（≥ 500 文字、< 5% は拒否）、コードプレースホルダー検証（`#CODEBLOCK`/`#INLINECODE`）、LLM 後の正規化（見出しに連結された区切り文字 / リンク）、`BadRequestError` による `reasoning_effort` なしの retry を追加
    - 依存関係 `langdetect==1.0.9` を追加
  - **pre-commit 品質ツール**（「完全な EurekAI 型」、14 hooks）：
    - Pre-commit：ruff（lint + format）、shellcheck、prettier（md/yaml/json）、detect-secrets（保護対象の API key 4 種）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（空白、EOF、large-files、shebangs など）
    - Pre-push：mypy（段階的な lax モード）、Opengrep SAST（translate.py + scripts/）、pip-audit（初期は reporting モード）、unittest discover（tests/ + scripts/tests/）
    - `scripts/` 内のローカル wrapper は `./venv/bin/python` を使用
    - `scripts/audit_verdict.py`：11 個の unittest で pip-audit の JSON を解析。jls42-astro の parser を Python に移植
    - 初期の ruff 違反 7 件を修正：B904（raise from）×2、B007（未使用の dirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizard は一時的に `translate.py` を除外（CCN 21～47 の関数が 4 つあり、リファクタリングを予定）— scripts/ では strict gate
  - **SonarCloud + 網羅的なカバレッジ**：
    - GitHub Actions workflow `SonarCloud`（sonarcloud.yml + sonar-project.properties）：push と pull-request のたびに解析し、`coverage.xml` で coverage を取得
    - README 上部に SonarCloud バッジ 11 個（Quality Gate、Security/Reliability/Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）
    - `tests/test_silent_failure.py`（`unittest` stdlib）：サイレント失敗のエラーチェーン 6 箇所をカバー
    - `tests/test_orchestration.py`（+79 tests）：`translate.py` のオーケストレーション層（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` TypeError + BadRequestError のフォールバック、o1-series の prompt format、`_validate_translation_output` の early-return 分岐）をカバー
    - `scripts/tests/test_audit_verdict.py`：`main()`（stdin/stdout）と `if __name__ == "__main__"` ブロックを subprocess 経由でカバー
    - **新規コードの Coverage**：75.5% → 約 98%（translate.py 98%、scripts/audit_verdict.py 97%）
  - **テスト**：`tests/test_translation_note_position.py` は位置 × 形式のマトリクス（E2E の `marker+top|bottom|both` と `legacy+top|bottom|both` を含む）、複数行の接頭辞付与、byte-for-byte の後方互換性（golden literal）、sanitizer、frontmatter の分割（終了 fence がない場合の raise を含む）、3 段落形式、2 段落フォールバック、1 段落 + Markdown リンクのガード、およびタイトルと URL が LLM に送信されないことを検証する重要なガード `TestLLMPayloadExcludesInvariants` をカバーします。**190 tests passed、リグレッション 0 件。**
  - ドキュメント：バッジ付きの `README.md`（FR + 14 翻訳）、`CLAUDE.md`（pre-commit workflow + 詳細な CI watch）、28 翻訳を再生成
- **1.8** `--news` モード + 2026 年モデルの更新（2026-03-17、tag `v1.8`）：
  - デフォルトモデルを更新（2026 年 3 月）：
    - OpenAI 品質：`gpt-5` → `gpt-5.4`
    - OpenAI 経済性：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 品質：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）、`gemini-3.1-pro-preview`（1M）の token 制限を追加
  - `--news` モードの初期実装：`#NEWSQUOTE\d+#` による EN 引用の保護、`LANG_FLAGS` のマッピング（15 言語）、対象言語ごとのフラグ管理
  - 復元前に news の placeholder を検証（リグレッション：LLM が placeholder を削除すると、引用のない出力がサイレントに生成されていた）
  - スクリプト `regen_translations.sh` を portable 化（絶対パス、pwd への依存なし）
  - README/CHANGELOG の language bars に Français リンクを追加し、28 翻訳を再生成
- **1.7** 新機能：
  - 翻訳時に元のファイル名を保持するオプション `--keep_filename`
  - API key を自動的に読み込む `.env` ファイルをサポート
  - **インラインコードの保持**：バッククォート（`` `...` ``）を翻訳中に保護するようになりました。
  - システムプロンプトを改善：
    - YAML frontmatter 内の引用符をより適切に処理
    - template 変数 `{variable}` を保護
    - 要求されていない翻訳者注記を禁止
  - jls42.org のブログ移行で 364 ファイルを正常にテスト
- **1.6** 新機能：
  - 翻訳用 Google Gemini API をサポート（`--use_gemini`）
  - 2026 年のデフォルトモデルを更新：
    - OpenAI：`gpt-5`（品質）、`gpt-5-mini`（経済性）
    - Claude：`claude-sonnet-4-5`（品質）、`claude-haiku-4-5`（経済性）
    - Gemini：`gemini-3-pro-preview`（品質）、`gemini-3-flash-preview`（経済性）
  - より高速で低コストのモデルを使用する経済モード（`--eco`）
  - ディレクトリを走査せずに単一ファイルを翻訳（`--file`）
  - 簡略化した新しい命名パターン：`{base}-{lang}.md`
  - モデル名を含む従来形式を保持するオプション `--include_model`
  - デフォルトの token 制限（128k）付きで、一覧にないモデルをサポート
  - README を 14 言語に翻訳
- **1.5** 改善：
  - **API key とデフォルトモデルを更新：**
    - **OpenAI：** `DEFAULT_MODEL_OPENAI` から `"gpt-4o"` に更新。
    - **Mistral AI：** `DEFAULT_MODEL_MISTRAL` から `"mistral-large-latest"` に更新。
    - **Anthropic の Claude：** `DEFAULT_ANTHROPIC_API_KEY` を追加し、`DEFAULT_MODEL_CLAUDE` から `"claude-3-5-sonnet-20240620"` に更新。
  - **翻訳 prompt を最適化：**
    - 直接翻訳と翻訳注記用の prompt を拡充し、明確性と効率を向上。metadata と固有のフォーマット要素を保持するための詳細な指示を含めました。
  - **コードをリファクタリング：**
    - Mistral AI client の初期化で `MistralClient` を `Mistral` クラスに置換。
    - 可読性と保守性を向上させるため import を再編成。
    - 翻訳時に元のフォーマットを保持するため、テキストの分割と code block の処理を改善。
  - **出力ファイルを管理：**
    - 出力ファイル名におけるモデルと言語の順序を反転（例：`f"{base}-{args.target_lang}-{args.model}.md"`）。翻訳の整理と検索が容易になりました。
  - **その他の改善：**
    - 不要な空行を削除してコードを整理。
    - script の構造と可読性を向上させる軽微な調整。
- **1.4** 新機能：
  - 翻訳用 Anthropic Claude API をサポート
  - 明確性と効率を高めるため prompt を最適化
  - コードの保守性を向上させる軽微な調整
- **1.3** 改善と新機能：
  - code block の処理を改善
  - 出力ファイルの処理を改善
  - 既存ファイルの検出を改善
  - 翻訳を強制するオプション `--force`
  - 出力ファイル名におけるモデルと言語の順序を反転
- **1.2** changelog の修正
- **1.1** Mistral AI API のサポートを追加
- **1.0** 初回リリース - OpenAI API をサポート

**gpt-5.6-lunaを使ってフランス語から日本語に翻訳された記事。**
