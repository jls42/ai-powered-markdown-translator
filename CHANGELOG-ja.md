### 変更履歴

🌍 [Français](CHANGELOG.md) | [English](CHANGELOG-en.md) | [Español](CHANGELOG-es.md) | [中文](CHANGELOG-zh.md) | [Deutsch](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [한국어](CHANGELOG-ko.md) | [العربية](CHANGELOG-ar.md) | [हिन्दी](CHANGELOG-hi.md) | [Italiano](CHANGELOG-it.md) | [Nederlands](CHANGELOG-nl.md) | [Polski](CHANGELOG-pl.md) | [Português](CHANGELOG-pt.md) | [Română](CHANGELOG-ro.md) | [Svenska](CHANGELOG-sv.md)

- **1.11.0** PyPI への公開：`pip install ai-powered-markdown-translator` に続いて `aipmt` コマンドを実行すれば、リポジトリをクローンせずに利用可能（2026-08-31）：

  - **単一ファイルのスクリプトがインストール可能なパッケージになりました。** `translate.py` はルートから `src/aipmt/translate.py` に移動し、コンソールエントリーポイント `aipmt` と同等の `python -m aipmt` を追加しました。クローンしたリポジトリは、テスト、28 の翻訳、品質管理ツールが存在するため、コントリビュートには引き続き必要ですが、利用するだけなら不要です。

    - **インポート名は `aipmt` であり、`translate` では決してありません**。実際に、しかも静かに衝突するためです。PyPI パッケージ `translate`（v3.8.1、最終アップロード 2026-07-06）は、同名のディレクトリをインストールします。venv で再現すると、ディレクトリがモジュールより優先され、`translate.main` が消え、エントリーポイントが `AttributeError` で失敗します。その一方で `pip check` は rc=0 で「No broken requirements found」と応答します。ユーザー側の単純な `pip install translate` だけで、診断可能なエラーなしに CLI が壊れてしまいます。実際の wheel でも反証を確認しました：パッケージの上に `pip install translate`、前後とも `aipmt --help` は rc=0 で、両方の CLI が共存します。
    - **配布名は長く、コマンド名は短くしました。** `ai-powered-markdown-translator` なら PyPI 検索でパッケージを見つけられます。プロジェクトをあらかじめ知らない人には、略語だけでは見つけられません。今回の公開は、まさに見つけてもらうことが目的です。もっともらしい候補を 2 つ検証して除外しました：`ai-markdown-translator` は 2024 年以来、同じ目的のツールによって npm で使用済みで、このリポジトリより 17 か月前から存在します。また `aimt` は `aim`（v3.29.1）と 1 文字しか違わず、同じ分野で稼働中のパッケージです。継続的な混同を招く最悪の構成です。ついでに手法上の落とし穴もあります：`pypi.org/project/<nom>/` はどんな名前に対しても 200 を返します（ボット対策ページ）。信頼できるのは JSON API だけです。
    - **フラットなパッケージではなく `src/` レイアウトにしました。** フラットなパッケージならテストの 6 つの `sys.path.insert(..., "..")` を維持できましたが、まさにそれが問題です。これらはパッケージではなくソースツリーをインポートするため、パッケージ化のエラーが隠れてしまいます。実際のコストは、置換ルールが 1 つ増えることです。

  - **キーをようやく一度だけ設定できるようになりました。** インストールされた CLI には永続的な設定がなく、環境変数とカレントディレクトリの `.env` だけが利用されていました。`find_dotenv` はシステムルートまで遡るため、**ホームディレクトリ配下で作業している場合**には `~/.env` を見つけられましたが、それ以外の場所では何も見つけられませんでした。これは設計上の選択ではなく、コマンドをどこから実行するかに依存する動作です。そこで、既存の 2 層の下に 3 つ目の層、`~/.config/aipmt/.env` を追加しました。

    - **優先順位をコードに直接記述したのではなく、`load_dotenv` のデフォルト値である `override=False` から導きました**：各層は、前の層で空いたままになった値だけを補います。そのため順序は、環境変数 → プロジェクトの `.env` → ユーザー設定となります。これは構造ではなく動作のテストで検証しています。2 つの呼び出しの順序を逆にするとテストは失敗し、3 つ目の層を削除しても失敗します。
    - **意図的に TOML ではなく `.env` 形式にしました。** `python-dotenv` はすでに依存関係に含まれ、構文は 15 個の README に記載済みで、同じファイルを両方のスコープで利用できます。新しい依存関係も構文もありません。場所は `XDG_CONFIG_HOME` が**絶対パス**の場合に従います。仕様では相対値を無視するよう求めており、そうしなければ設定場所が再びカレントディレクトリに依存してしまうためです。Windows では `APPDATA` を使用します。
    - **2 つの選択肢を理由付きで却下しました。** システムのキーチェーン（`keyring`）はデスクトップではより安全ですが、ヘッドレス環境、つまりサーバー、コンテナ、CI では失敗します。これはバッチ翻訳そのものの利用ケースなので、オプトインには適していますが、デフォルトには不向きです。`--api-key` フラグではキーがシェル履歴に残り、`ps` から見えるようになります。
    - **キーがない場合、呼び出し元の痕跡を表示しなくなりました。** 以前はユーザーに `site-packages` を指す Python のスタックと、「環境または .env」とだけ記したメッセージが表示され、後者をどこに作ればよいか分かりませんでした。現在は 3 つの場所を正確なパス付きで列挙し、コマンドは 2 で終了します。保護範囲を**意図的に狭く**し、`except ValueError` は設定フェーズだけに適用しました。実行全体を包むと、翻訳中に発生した本当のバグが安心させるだけのメッセージに変わってしまいます。これはこのリポジトリが追跡している失敗モードです。これを禁止するため、`main()` のソースを読むテストを追加しました。

  - **修正 — ユーザーの `.env` は、ツールをインストールすると無視されていました。** 引数なしの `load_dotenv()` はカレントディレクトリからではなく、呼び出し元ファイル、つまり `site-packages` から遡ります。独自の `.env` を持つプロジェクトから実際のコンソールエントリーポイントを起動して測定したところ、`find_dotenv()` は `''` を返してキーを読み込みませんでした。一方、`find_dotenv(usecwd=True)` はキーを見つけました。ツールがクローンしたリポジトリからのみ実行されていた間は存在しなかったバグですが、公開後は常に発生し、正しい設定でも API キーが「不足している」とだけ表示されることになります。

  - **何も検証しなくなっていた 3 つのゲートを、再び機能するようにしました。** これらは移動前に意図的に強化しました。捕捉すべき変更の後に書かれた安全策には、何の証明力もありません。各ゲートは元のリポジトリでは成功し、移行済みコピーでは失敗します。両方向を測定しています。

    - **Lizard は存在しないパスを黙って無視します**：rc=0、「0 file analyzed」となります。複雑度ゲートは 158 関数 / 2247 nloc から、3 関数 / 34 nloc へと変わってしまい、出力は 0 バイトになります。現在はスコープを配列にし、各エントリの存在を検証しています。
    - **存在しないモジュールに対する `coverage run --source=` は失敗しません**：stderr に警告を出すだけで、unittest でも `coverage xml` でも rc=0 となり、レポートも公開されます。ただし 1453 から 141 statements へと大幅に欠落します。ほとんど分析されていないため、プロジェクトが健全に見えてしまいます。レポートを守るため、合計値と測定された最大ファイルという 2 つの下限を設けました。
    - **翻訳の鮮度プローブは、呼び出し形式に対して構造的に盲目です**：argparse のフラグを基準にしているため、ファイル名の変更では変わりません。実際に、モジュールを移動しても 15 個の README は存在しないコマンドを記載したままで、判定は「期限切れの翻訳なし」になりました。そのため 7 つ目のセクションではオプションではなく**形式**を検証します。また Lizard フックはスクリプトの実際のスコープと照合します。キー `files:` が一致しなくなっても pre-commit を失敗させず、**スキップ**させるためです。

  - **`requires-python = ">=3.10"` は主張ではなくなりました。** `sonar-project.properties` はすでに 3.10〜3.12 を宣言していましたが、開発環境には 3.12 しかなく、実際には一度も検証されていませんでした。公開すれば明らかになる内部矛盾です。現在はテストワークフローで 3.10、3.11、3.12 上のテストスイートを実行し、公開されている制約を持つ**パッケージ**をインストールします。

  - **下限のみで、上限は設けません。** `requirements.txt` はテスト済みの lock として残し、`[project.dependencies]` を公開契約にします。lock の正確なバージョンを公開すると、別のパッケージを使用しているすべてのユーザーと衝突するためです。`<N+1` の上限も設けません。これは、メジャーバージョンの遅れがあるとリリースゲートを失敗させる `check-deps-fresh.sh` と正面から矛盾するためです。下限の組み合わせで解決し、`openai==1.0.0` が `ResolutionImpossible` を返す反証によって、何でも受け入れるのではなく正しく判別していることを確認しました。さらに、`pyproject.toml` のバージョンが CHANGELOG のバージョンと異なることを禁止するガードも追加しました。PyPI では同じ番号を再利用できないためです。

  - **新しい venv で最初から最後まで検証しました**：69,768 バイトの wheel には `aipmt/*.py`、dist-info、ライセンスだけが含まれます。`aipmt --help` は 22 個のフラグ付きで rc=0、`python -m aipmt` は「usage: aipmt」と表示し、「usage: \_\_main\_\_.py」とは表示しません。`pipx` のインストールも機能しました。さらに重要なのは、**任意のユーザーディレクトリから実際に fr→en 翻訳**を行い、太字、リスト、インラインコード、リンク、URL を保持し、コードブロックを翻訳しなかったことです。移行前後で識別子のリストはバイト単位で完全に同一のまま、318 個のテストが成功しました。テストが無効化されていないことを証明するのは「OK」ではなく、これです。

- **1.10.0** `--use_codex` Provider（ChatGPT サブスクリプションのクォータ）、SDK とモデルの更新、複数段落の news 引用を修正（2026-08-29）：

  - **セキュリティレビュー — PR が設けたものの、すべての場所で維持できていなかった 2 つの安全策**：

    - **Codex の preflight が `.env` 全体をバイナリに渡していました。** `_codex_preflight` は **`env=` なしで** `subprocess.run` を呼び出していました。サブプロセスは `os.environ` 全体、つまり `load_dotenv` が読み込んだ `.env` の全内容を継承していました。計測用の偽バイナリで確認したところ、preflight に届いた秘密情報は **7 件**でした。6 つの provider のキーと 1 つの `GITHUB_TOKEN` です。一方、対応する `_grok_preflight` は正しく `env=_grok_env()` を渡し、**0 件**でした。この不整合は PR 内部に存在していました。すぐ近くにある `_strip_secret_env` は、まさにこの不変条件を守るためのものです。`_codex_env_base()` を抽出して両方の経路で共有し、修正後に両側とも秘密情報が 0 件であることを測定しました。
    - **「`--deny` fail-closed」という性質は、実際に使用された形式を対象にしていませんでした。** コメントでは、未知の接頭辞を持つルールが起動を拒否することを、Grok の隔離全体の根拠としていました。しかし `grok 1.0.13` で測定したところ、この検証は**括弧付き形式にしか存在しません**：`--deny 'CeciNestPasUnOutil(*)'` は「unknown tool prefix」として起動を拒否しますが、`--deny 'CeciNestPasUnOutil'` は黙って受け入れられます。ところが `GROK_DENY_RULES` は裸の名前だけを使用していました。そのため xAI 側でツール名が変更されると、測定済みの唯一の隔離層が何の通知もなく失われます。しかも、その環境では OS サンドボックスがすでに適用されていません。名前付きの 8 つのルールは `Prefix(*)` を通過し、それぞれ CLI の既知の接頭辞であることを検証します。catch-all の `*` は、唯一受け入れられるリテラル形式のまま残しました。検証されていない形式に戻ることを防ぐテストを追加しました。
    - **その他の点はクリーンであることを検証済みです**：コマンドインジェクションはありません（どこでもリスト形式を使用し、`shell=True` は決して使用せず、ドキュメント内容は stdin または `--prompt-file` で渡します）。安全でないデシリアライズもありません（`json.loads` のみを使用し、型ガード付き）。7 つのペイロードでパス横断の修正を検証し、回避策は見つかりませんでした。また `--deny '*'` が CLI によって実際に適用されていることも確認しました（workdir 外の読み取りで `DENY_ENFORCED` を観測）。
    - 上で追加した鮮度チェックも、途中で自分自身の原則を回避していました。PyPI リクエストに失敗したパッケージは黙ってスキップされ、ゲートが成功していました。現在は実際に比較されたパッケージ数を数え、網羅性が不十分な場合は失敗します。

  - **依存関係を更新し、遅延を再発させないための 2 つの安全網を追加しました**：

    - **遅延は現実のもので、長期化していました**：`openai` 2.54 → **3.6.0**、`anthropic` 0.125 → **1.2.0**、`certifi` 2024.8.30 → **2026.7.22**。これは、すべての provider 呼び出しで TLS を検証するルート証明書ストアが 2 年遅れていたことを意味します。原因は明確です：**`.github/dependabot.yml` が存在しませんでした**。このファイルがない場合、GitHub は _security updates_ だけを有効にし、Dependabot は CVE 対象の依存関係に対してのみ PR を提案します。そのため `urllib3` と `idna` は更新した一方で、2 つの SDK はメジャーバージョン 1 つ分遅れたままになっていました。
    - **2 つのメジャーバージョンは衝突せず共存します**。以前の推論では衝突が懸念されていましたが、実際には `openai` 3.x と `anthropic` 1.x は **`httpx2`** に移行し、`mistralai` と `google-genai` は `httpx<1` のままです。ただし、これは異なる配布物です。実際にインストールして検証し、さらに **7 つの provider 経路を最後までテスト**しました。OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI、Grok CLI のすべてで、各出力のインラインコードとリンクが保持されました。「HTTP スタックを 2 つ避ける」ことは好みであってブロッカーではなく、測定によって結論が出ました。
    - **`requirements.txt` は実際の環境を記述していませんでした**：`google-auth`、`cryptography`、`opentelemetry` のスタックは作業用 venv にインストールされていたにもかかわらず、宣言されていませんでした。そのため、新規インストールではテスト対象を再現できませんでした。一方、`tokenizers`、`huggingface-hub`、`PyYAML` は含まれていましたが、インポートも必要とされてもいませんでした。`mistralai` 1.x の残骸です。ファイルを、直接依存関係だけから構築した venv の完全な依存関係閉包として再生成しました。`pip-audit` は新しい構成に既知の脆弱性がないことを報告しています。
    - **`.github/dependabot.yml`**（新規）で、バージョン、pip、github-actions の週次更新を有効にしました。マイナー更新とパッチ更新は 1 つの PR にまとめます。パッチ更新を 1 件ずつ PR にすると無視されてしまい、ノイズは更新の敵だからです。**メジャー更新は分離**し、それぞれ実際の呼び出しによる検証を必須にします。
    - **`scripts/check-deps-fresh.sh`**（新規、ゲートに接続済み）により、遅延がプロジェクトの判定に現れるようになりました。Dependabot は提案するだけで保証はせず、PR が積み重なることもあります。メジャー更新の遅延は失敗、マイナー更新は警告とします。ゲートが常に赤だと、やがて無視されるためです。PyPI に到達できない場合は、ローカルでは明示的にスキップし、**CI では fail-closed** とします。実行されなかったチェックは成功ではないためです。両方向で検証しました。修正前の正確な状態（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`）を検出し、マイナー更新については警告だけを出します。

  - **この PR のレビューから得られた修正** — 5 人のレビュアーが diff を精査し、以下の項目はすべて修正前に**測定によって再現**されました。そのうち 2 件は、この同じバージョンで上記の変更によって導入されたリグレッションでした。
- **修正済みのリグレッション — `_NEWS_CITATION_REGEX` で指数バックトラッキングが発生していた。** 複数段落対応の修正で、繰り返し内に `(?:[ \t]*$|[ \t]+.*)` が導入されていた。`[ \t]+` と `.*` の間で空白を分配する方法が曖昧で、その曖昧さが反復のたびに増幅していた。パターンにマッチしない `>   texte` の行 — Markdown では完全に合法なインデント — で測定すると、修正前は **14 行で 2 589 ms**、修正後は 0.04 ms で、行を 1 行追加するごとに約 9 倍になっていた。`--news` モードでは、長く形式に適合しない blockquote だけで翻訳がジョブのタイムアウトまで停止し、原因も特定できなかった。現在は繰り返しが行全体を 1 回で消費する (`\n^>(?![ \t]*—).*`) ため、反復ごとのマッチ方法が 1 つしか残らない。実際の 231 記事のコーパスで検証し、キャプチャ結果に **差異はゼロ**、同じ 423 件の引用、複数段落の本文 14 件も引き続き拡張されることを確認した。
    - **provider フラグを 2 つ同時に指定すると、気付かないまま従量課金になっていた。** `--use_codex --use_mistral` は受け付けられていた。`_select_provider_client` は先に Mistral を検査し、`_resolve_provider` は明示的なブール値を優先していたため、どちらも Mistral に収束していた。ユーザーはサブスクリプションの割り当てを要求しているつもりでも、警告なしに従量課金になっていた。これはまさに `--use_codex` が防ぐために存在する障害モードである。現在、6 つの provider フラグはすべて `add_mutually_exclusive_group` を通る。**動作変更**：これまで黙って受け入れられていた 2 つの provider を組み合わせたコマンドラインは、現在 `argument --use_mistral: not allowed with argument --use_codex` で失敗する。
    - **プローブがクラッシュした際、作業終了ゲートが誤って成功していた。** `scripts/check-release-ready.sh` の 13 検査のうち 4 つが、終了コードを一度も確認せず「stdout をキャプチャし、空なら結論する」というパターンに従っていた。例外 (ファイルの改名、`FileNotFoundError`) は stderr に書き込まれ、stdout は空のままとなり、検査は「報告するものはない」と結論していた。それを防ぐために書かれたスクリプト自体の中で、「1 つの `exit 0` は何も証明しない」という落とし穴が再現されていた。現在は `probe()` ヘルパーが、終了コードが 0 であること **および** 終了センチネルの存在を要求する。また、プローブは目印の集合が空の場合に結論を出さない — 空集合に対するアサーションは常に真だからである。実証として、上記の排他的グループを追加したことで provider フラグは `*_group` オブジェクトを通るようになり、旧 `parser\.add_argument\(` 正規表現にはマッチしなくなった。**21 個中 6 個のフラグ**が黙って検査対象外となり、ゲートは成功していた。
    - **シークレットのスキャンが 6 つ中 4 つの provider を取り逃していた。** `[A-Za-z0-9]` クラスはハイフンを除外していた。`sk-proj-…` (現在の OpenAI 形式) と `sk-ant-api03-…` は 2 つ目のハイフンで失敗し、`AIza…` は対象外だった。パターンを拡張し、`.secrets.baseline` をスキャン対象から除外した。さらに `.env` のガードは `git diff --cached` を照会していたが、これはインデックスしか見ないため、最悪のケースである **すでにコミット済み**の `.env` は決して現れなかった。現在は `git ls-files` を照会する。
    - **Codex の「トークンのウォームアップ」はウォームアップではなかった。** 測定の結果、`codex login status` は `~/.codex/auth.json` に触れず (mtime とサイズは不変)、ヘルプには「ログイン状態を表示」と書かれていた。それにもかかわらずコメントは、ローテーションする使い捨てトークンでの同時 refresh のリスクを無効化するため、「1 回、順次」トークンを更新すると主張していた。説明された保護は存在しなかった。現在のコメントはコードの実際の動作を記述し、実際の対策は引き続き `max_jobs=4` である。さらに検査は、これまで無視していた `CODEX_BIN` に対応する。`codex` が `PATH` にないマシンでは「認証されていない」として失敗していたが、これは誤解を招く診断だった。
    - **`.env` がサブシェル内で読み込まれていた。** `detect_provider` はコマンド置換内で呼び出されるため、その export は上位に戻らなかった。`.env` で定義された `GROK_BIN`、`GROK_HOME`、`REGEN_MODEL` は `main()` から行う読み取りには見えず、正しい設定でも「Grok バイナリが見つからない」と結論されていた。
    - **並行実行数が公表された上限を 50% 超えていた。** ガードが README/CHANGELOG のペアを起動した後に置かれていたため、測定されたピークは **`max_jobs=2` が 3** だった。Chat/Imagine/Voice と週次割り当てを共有し、測定可能な割り当てがない Grok では、スクリプトが自らに課した上限が守られていなかった。最終カウントは表示されていたものの、28 と比較されていなかったため、ファイルの欠落が見過ごされていた。
    - **Grok の出力契約：`stopReason` がない場合も失敗になった。** コードは、告知された契約が `end_turn` を要求している箇所で「`end_turn` **または存在しない**」を適用していた。フィールドのない payload、または CLI の更新でフィールド名が変更された payload は、ガードを黙って no-op にしていた。また `max_turn_requests` はレート制限として分類されなくなった。これはラウンド予算が尽きた状態であり、再試行しても 90 秒待って同じ結果になるためである。さらに `quota` はレート制限マーカーから外れた。これは `_codex_is_rate_limited` の docstring がすでに述べていた理由を、Grok が適用していなかったためである。
    - **Gemini のカスケードをモデル単位でメモ化した。** 各セグメントで毎回 `minimal` から再開していたが、デフォルトモデルはそれを拒否する。そのため通常経路ではセグメントごとに 400 の往復が発生し、同じ警告が再出力されていた。警告が何百回も繰り返されると読まれなくなる — こうして警告はマスクになる。
    - **その他**：CI での拒否メッセージが Codex 用にハードコードされており、`--use_grok_cli` のユーザーを `XAI_API_KEY` ではなく `OPENAI_API_KEY` に誘導していた。`provider.capitalize()` は「Grok_cli」と「Openai」を表示していた。サブプロセス基盤のコメントは「shim」を両方の CLI に一般化していたが、Grok バイナリはネイティブ ELF である (正しい根拠は「独自のサブプロセスを spawn するエージェント」)。`subprocess` に関する SAST の 12 件の findings は、理由を付けて `# nosec` / `# nosemgrep` とマークされた。`shell=True` のないリスト形式ではインジェクションが不可能であり、文書の内容が argv を経由することもない。
    - **エージェントのサブプロセスにシークレットが入ることはなくなった。** 名前を列挙した deny-list は、**課金**の不変条件 ( `OPENAI_API_KEY` なしの Codex、`XAI_API_KEY` なしの Grok) しか保護していなかった。測定すると、さらに **7 つのシークレット**が各サブプロセスに入っていた。Anthropic、Mistral、Google、Gemini のキー、もう一方の CLI のキー、そしてシークレットではないがトラフィックをリダイレクトする `OPENAI_BASE_URL` である。この 2 つの CLI は **エージェント**であり、Grok の CLI は多くの Linux マシンで適用可能な OS サンドボックスなしに動作する。現在は名前のリストではなく、**名前のパターン** (`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`) によってフィルタリングするため、このコードが知らない変数をユーザーが `.env` に追加した場合も対象になる。CLI に必要なものはない。認証は `~/.codex` と `~/.grok` に存在し、環境変数には決して存在しない — 環境を強化した状態で、両 provider それぞれによる **実際の翻訳の成功**で検証した。
    - **テスト**：新しい `tests/test_review_hardening.py` ファイル (21 テスト) を追加し、provider フラグの排他性、`stopReason` 契約、news 正規表現の線形性、CI での拒否メッセージ、Gemini のメモ化、サブプロセス環境にシークレットがないことを固定した。最後のアサーションは **汎用的**であり、どのリストにも名前がないキーで失敗する。既存の除去テストは自身の定数を鏡写しにしたものだったため、自分のループの故障以外は何も検出できなかった。完全なスイートは **311 テスト**になった。

  - **2 つの新しい Grok provider**：`--use_grok` (xAI API、キー `XAI_API_KEY`、従量課金) と `--use_grok_cli` (公式 Grok Build CLI、Grok サブスクリプションから差し引き — `--use_codex` と同じ原則)。
    - **API モード、約 40 行**：xAI のエンドポイントは OpenAI と互換性があるため、クライアントと `_call_openai` をそのまま再利用し、変更するのは `base_url` だけである。必要だった適応は 1 つだけで、それは全体に恩恵をもたらす。`finish_reason` が `end_turn` (xAI が出力する形式。OpenAI は `stop` を出力する) も受け付けるようになった。モデルは `grok-4.6` (品質) と `grok-4.3` (エコノミー)。なお、Grok のエコノミーモデルはリポジトリ内で最も高価なままである — 100 万件あたり $1.25/$2.50、`mistral-small-latest` は $0.15/$0.60 — この provider は価格ではなくモデルの多様性を理由に選ぶものである。
    - **CLI モード**：Codex を基にしつつ、実環境上の 4 つの相違点がある。プロンプトはファイルで渡す (`--prompt-file`。CLI は stdin を読み取らず、セグメントを argv にすると `ps` から見えてしまう)。出力は stdout 上の単一の JSON オブジェクトである (JSONL でも `-o` ファイルでもない)。サブスクリプションが公開するのは `grok-4.6` と `grok-4.5` だけであり、サンドボックスは適用できない (以下を参照)。サブプロセス起動は Codex とともに `_codex_run_process` に切り出し、すでにテスト済みの Codex provider の残りには触れていない。
    - **測定の結果、`exit 0` は何も証明しない**：未認証の場合、CLI は **stdout** に `{"type":"error","message":"Not signed in."}` を終了コード **0** で書き込む。拒否やラウンド超過も同じように動作する。そのため出力契約では、終了コード 0、エラー payload がないこと、`stopReason == end_turn`、テキストが空でないことの 4 条件を同時に要求する。preflight も同じ考え方に従う。切断中でも `grok models` は 0 で終了するため、結論できるのは stdout に「not authenticated」が存在する場合だけである。
    - **隔離：非対称性を意図したものとして文書化した。** Codex が `--sandbox read-only` で動作する一方、多くの最近の Linux マシンでは Grok のサンドボックスを適用できない。`sudo` なしには回避できない、独立した 2 つのシステム上の原因がある。Ubuntu 24.04 以降では AppArmor が非特権 user namespace をブロックする (`bwrap: setting up uid map: Permission denied`。Grok 外でも再現)。また、コンテナランタイムのソケット deny-list は、`/run/podman` が `0700` の場合に失敗する (resolver が回復できるのは `ErrorKind::NotFound` だけで、EACCES は致命的になる)。中心的な落とし穴は、**組み込み**プロファイルを適用できない場合、**隔離されていない状態で黙って起動する**ことである。そのためスクリプトはデフォルトでプロファイルを要求せず、黙ってフォールバックすることもない — stderr に警告を出す。保護は CLI の `--deny` ルール (catch-all の `*` を含む) に依存する。これは測定済みで唯一の _fail-closed_ 層である (未知のプレフィックスを持つルールは起動を拒否させる)。`GROK_TRANSLATE_SANDBOX=read-only` を使えば必須にでき、その場合、マシンが適用できなければ起動に失敗する。
    - **ガードレール**：`XAI_API_KEY`、`GROK_API_KEY`、`GROK_SANDBOX` をサブプロセスの環境から除去する (キーが 1 つでもあれば従量課金に切り替わり、継承された `GROK_SANDBOX` が適用不能なプロファイルを強制して誤解を招くメッセージを出す)。MCP/hooks/skills/agents の切り替えを無効化し、`--disable-web-search`、`--no-subagents`、`--no-plan`、使い捨ての workdir、CI での拒否、プロセスグループを終了させるタイムアウト、レート制限時のバックオフも設定する。`--max-turns` は 1 ではなく 6 に設定する。カウンターはツールのターン後に増分されるため、1 では出力が切り詰められる。
    - **割り当て**：Grok のプールは週次で、**Chat、Imagine、Voice と共有**されている。また、Codex の `account/rateLimits/read` とは異なり、これを公開するコマンドはないため、消費量を数値化できない。したがって `regen_translations.sh` は並行実行を 2 に制限し、明示的に警告する。
    - **テスト**：新しい `tests/test_grok_provider.py` ファイル (24 テスト)。完全なスイートは **290 テスト**になった。
  - **修正済みのバグ — EN の複数段落引用が一部しか保護されていなかった (`--news` モード)**：`_NEWS_CITATION_REGEX` は引用本文として、`>` 行が **連続**する列しか受け付けていなかった。引用が複数段落にまたがり ( `>` の空行で区切られ)、前の段落は LLM に送られて翻訳され、最後の段落だけがキャプチャされてプレースホルダーに置換されていた。これは `--news` が保証するために存在する目的とは正反対である。現在は繰り返しが内部の `>` 空行を受け付け、非貪欲になったため、最初に見つかった空行ではなく、斜体行の前にある `>` 空行で停止する。
    - **測定した規模**：実際の 198 記事のコーパスで、該当する引用は 419 件中 11 件。リグレッションはない — 新しい正規表現がキャプチャする引用数はまったく同じで、複数段落の本文だけが拡張された (同一の本文 408 件、拡張された本文 11 件)。帰属行 `> — …` が本文に取り込まれることもない (先読みは維持)。
    - **エンドツーエンドの証明**：69 KB の記事を ja/ar に翻訳した結果、以前は日本語で `> GLM-5.3がオープンウェイト化。` として出力され、アラビア語でも同様に翻訳されていた引用の最初の段落が、現在は `> GLM-5.3 is now open-weight.` のまま保持される。英語の引用行数は 9 行から 10 行に戻り、ソースと一致した。
    - 注記：この不具合は後段のバリデーターでは検出されなかった。バリデーターは引用の存在は確認するが、完全性は確認していない。
  - **デフォルト provider で測定したコスト削減**：`_openai_extra_kwargs` は、モデル名が `gpt-5` で始まると、`--eco` でも `reasoning_effort="medium"` を送信していた。10 語の文を翻訳するために `gpt-5.4-mini` で測定すると、`medium` → reasoning token 45、出力 token 65。`none` → 0、14。推論は翻訳に何ももたらさず、各ファイルの各セグメントで課金されていた。デフォルトは `--eco` では `none` になり、それ以外では `medium` のままとなった。CLI で明示的に渡した値が引き続き優先される。`--reasoning_effort` は `low`/`medium`/`high` に加えて、`none` と `xhigh` も受け付けるようになった (すべてのモデルがすべてを受け付けるわけではない。例えば `minimal` は `gpt-5.4-mini` に拒否される — 既存のパラメーターなし retry がこのケースを処理する)。
  - **SDK の更新と Gemini の移行**：`google-generativeai` (サポート終了 2025-11-30、リポジトリはアーカイブ済み) を統合 SDK **`google-genai`** に置き換えた — `genai.Client(api_key=...)`、続いて `client.models.generate_content(model=, contents=, config=)`。システムプロンプトはセグメントに連結するのではなく、`system_instruction` として渡す。`mistralai` は **2.9.4** に更新 (import は `from mistralai.client import Mistral` になり、旧形式は `ImportError` を送出することを wheel で検証)。`anthropic` は **0.125.0**、`openai` は **2.54.0** に更新した。これは venv 内で 2 つの HTTP スタックを共存させないため、`httpx2` への切り替え前の最後のバージョンである。これに伴い `httpx` 0.28.1 と `pydantic` 2.13.5 の制約を解除した。
  - **文書ではなく実際のテストで捕捉した 2 つのリグレッション**：
    - `anthropic` 1.0 以降では、`max_tokens` が 10 分を超えることを示す `ValueError: Streaming is required...` を持つ、非ストリーミングのクライアント呼び出しを拒否する。このガードレールは 0.34.2 には存在せず、`max_tokens=32768` を使う Claude の呼び出しをすべて壊していた。明示的な `timeout` (`CLAUDE_TIMEOUT`、デフォルト 900 秒) によって修正した。これにより、完全な応答しか利用しない呼び出しをストリーミングへ切り替えずに済む。
    - `thinking_level="minimal"` は Gemini のカタログの一部でしか受け付けられない。`gemini-3.1-flash-lite` は対応するが、`gemini-3.7-flash` と `gemini-3.1-pro-preview` は 400 で拒否する。そのため `_gemini_generate_with_fallback` を導入した。これは `minimal` → `low` → thinking_config なしというカスケードで、既存の OpenAI フォールバックと同じ考え方である。最適化用パラメーターによって翻訳が失敗してはならない。
  - **デフォルトモデルを更新し、各モデルを実際の呼び出しで検証した**：OpenAI `gpt-5.5` → **`gpt-5.6-terra`** (28 件のバッチで −60%)、`gpt-5.4-mini` → **`gpt-5.6-luna`** (−73%)。Claude `claude-sonnet-4-6` → **`claude-sonnet-5`** (より安価で新しい)、`claude-haiku-4-5-20251001` → **`claude-haiku-4-5`** (日付なしの正規 ID)。Gemini `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**、`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`** (安定版で、`3.5-flash-lite` より安価)。
Mistralは変更されず、4つの中では`mistral-large-latest`が依然として最もコストパフォーマンスに優れています。なお、`gemini-3.1-pro-preview`より新しいProシリーズのGeminiモデルは存在しません。2026年5月に発表されたGemini 3.5 Proは実際にはリリースされておらず、3.5/3.6/3.7系列はFlash専用です。
  - **Geminiへ切り替える前に実測したA/Bテスト**：`README.md`を`gemini-3.1-pro-preview`、続いて`gemini-3.7-flash`で日本語に翻訳しました。構造は完全に同一（21個のリスト、18個のコードブロック、13個のHTMLリンク、13個の画像、すべてのURLを保持）で、所要時間は**8秒対48秒**でした。これら2モデルを翻訳または非ラテン文字スクリプトで比較した公開ベンチマークは存在しないため、切り替えを単なる推測に基づいて行うことはありませんでした。
  - **Claudeのレスポンスブロックのフィルタリング**：`_call_claude`は型をフィルタリングせずに`block.text for block in response.content`を実行していました。適応型推論モデル（Sonnet 5以降）は`thinking`ブロックを挿入しますが、そこに公開されるのは`.thinking`であり、`.text`ではありません。最初のセグメントで不透明な`AttributeError`に遭遇すると、翻訳が壊れていました。現在は`thinking`、`redacted_thinking`、`tool_use`、`tool_result`を除外しています（未知の型でテキストを含むものにも寛容であるための拒否リスト）。また、テキストブロックが1つもないレスポンスは明示的なエラーになります。`thinking={"type": "disabled"}`はすべての呼び出しで渡されます。
  - **`MODEL_TOKEN_LIMITS`を再同期**：廃止日を過ぎたモデルを削除しました（`magistral-*`系列は2026-07-31、`gemini-2.0-*`は2026-06-01、`gemini-3-pro-preview`は2026-03-09に廃止、`claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。上限を修正しました：Mistralは128Kから**256K**へ（Large 3 / Small 4世代）、Geminiは1,000,000から**1,048,576**へ（実際の入力上限）、`claude-opus-4-5`は200Kから**1M**へ、`gpt-5.6-*`ファミリーは400Kから**1.05M**へ変更しました。Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest`、`ministral-*`系列を追加しました。なお、これらの上限はあくまで目安であり、`translate()`が分割を`min(16000, limite)`に制限しています。

  - **Provider `--use_codex`**：公式Codex CLI（`codex exec`）を非対話モードで操作する5番目のproviderです。使用量に応じて課金されるAPIを呼び出す代わりに、すでに支払済みのChatGPTサブスクリプションのクォータから翻訳分が差し引かれます。この用途についてOpenAIが文書化している唯一の方法です。プラン別の利用可能機能一覧では、「Codex SDK、`codex exec`、and scriptable workflows」がPlus/Pro/Business/Enterpriseで利用可能とされています。一方、`~/.codex/auth.json`のトークンではPlatform APIの呼び出しを認証できません（このスクリプトが読み取ることもなく、認証と更新はCLIが引き続き管理します）。
  - **pipでインストール可能なCodexバイナリ、npmだけでなく対応**：`_resolve_codex_binary()`はまず`CODEX_BIN`でバイナリを探し、次に`PATH`、その後OpenAIが公開している公式Pythonパッケージ**`openai-codex-cli-bin`**（SDK `openai-codex`の依存関係）を探します。したがって、Pythonプロジェクトで`--use_codex`を使用するために、npmのグローバルインストールは不要になりました。このパッケージは`requirements.txt`には追加していません。バイナリのサイズは約250MBであり、オプションのproviderのために全ユーザーへ強制することになるためです。最初から最後まで検証済みです。`codex`が`PATH`に存在しない状態でも、パッケージ化されたバイナリが見つかり、完全な翻訳が6秒で完了しました。
  - **「サブスクリプションモード」の保証**：`OPENAI_API_KEY`と`CODEX_API_KEY`をサブプロセスの環境から削除します。この保護がなければ、`.env`に存在するキーによって、目に見える通知なしにCodexが従量課金へ切り替わる可能性があります。これはまさに、このproviderが防ぐために存在する事態です。
  - **CLIの落とし穴をテストで固定**：
    - `codex exec`は、プロンプトを引数で渡した場合**でも**stdinを読み取ります。stdinを閉じないと、モデルを呼び出さないままコマンドがタイムアウトまで待機します（再現結果：180秒後に終了コード124、0バイト）。そのため`communicate(input=...)`は必須です。
    - npmでインストールされる`codex`は、実際のRustバイナリを`spawn`するNode shimです。RustバイナリはPythonプロセスの**孫プロセス**となり、`SIGKILL`の`subprocess.run(timeout=)`後も生き残ってクォータを消費し続けます。そのため`Popen(start_new_session=True)`と`os.killpg`が必要です。
    - CLIは`turn.failed`を出力していても終了コード0になることがあります。JSONL出力（`--json`）を終了コードに加えて検査し、終了コード0なのに`-o`が存在しない場合は、空のセグメントを生成せず明示的なエラーを発生させます。
  - **レート制限時のバックオフ**：CLIには内部リトライが実装されていません（`max_retries = 0`）。分類は部分文字列ではなくJSONペイロードの構造（`status: 429` / `error.type`）に基づいて行います。「quota」という語は、回復可能な429にも`insufficient_quota`の恒久的エラーにも現れるためです。
  - **CIガード**：`--use_codex`は`CI`または`GITHUB_ACTIONS`が定義されている場合に拒否されます。サブスクリプション認証は共有runner向けに設計されておらず、OpenAIも公開リポジトリでこのワークフローを使用しないよう明示的に推奨しています。
  - **モデル**：`gpt-5.6-sol`（品質）と`gpt-5.6-luna`（`--eco`）。`gpt-5.6-*`ファミリーはCLIとPlatform APIで共通ですが、ChatGPTアカウントですべてを利用できるわけではありません。allowlistはサーバー側で適用され、ローカル検証は行わず、通常とは異なるモデルを指定すると警告が発生します。Plusプランでは、Lunaは5時間のウィンドウあたり250～2,000メッセージ、Solは10～100メッセージです。そのため、`--eco`がバッチ処理に推奨されるモードです。
  - **修正済みのバグ — `regen_translations.sh`が完全な成功にもかかわらずエラーになっていた**：`trap ... EXIT`は`failed_log`を参照していました。これは`main()`の`local`変数ですが、trapの実行時にはすでに存在しません。`set -u`では`failed_log: unbound variable`が発生し、28件の翻訳が正しかったにもかかわらずスクリプトが1で終了していました。これにより、最もコストのかかる再生成直後の段階で`release.sh --auto`（`set -e`）が中断されていた可能性があります。変数をグローバルにし、trapがその存在を検査するようにしました。副次的な効果として、それまでこのエラーに隠れていた本当の翻訳失敗が、終了時のサマリーに再び表示されるようになりました。
  - **`REGEN_MODEL`**：`regen_translations.sh`の新しい環境変数です。providerのデフォルトを上書きして特定のモデルを強制できます。たとえば`REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`を指定すると、量を重視した`--eco`モデルではなく、サブスクリプションのクォータ内で高品質モデルを使って再生成できます。
  - **`regen_translations.sh`**：明示的なオプトインで`REGEN_PROVIDER=codex`を利用できます（ユーザーが知らないうちにサブスクリプションのクォータを消費しないよう、自動検出は行いません）。トークンは並列処理を開始する前に1回だけ逐次更新します。Codexの更新はローテーション式で1回限りのため、並行ジョブは`codex login`セッションを無効化してしまいます。並行数は4に下げています。
  - **関連リファクタリング**：`_dispatch_provider_call`のパラメーターを8個から6個に減らしました。第4のbooleanをチェーン全体へ伝播させる代わりに、provider名を返す`_resolve_provider()`を使用しています。`args`より明示的なbooleanを優先することで、最小限の`Namespace`を指定して`translate(..., use_mistral=True)`を呼び出すテストを維持しています。
  - **テスト**：新しいファイル`tests/test_codex_provider.py`（48テスト）で、argv、環境変数の除去、前置き禁止契約、サイレント失敗、timeout/killpg、バックオフ、preflight、provider解決、Geminiの推論カスケード、Claudeのブロックフィルタリング、ニュースの複数段落引用をカバーします。全体のテスト数は290になりました。
  - **実際の検証**：プロジェクトの`README.md`をCodexで**14言語**に翻訳したところ、参照翻訳と完全に同一の構造になりました（コードブロック14個、見出し24個、表の行25行、HTMLリンク13個、画像13個、URL19個、コードブロックは文字単位で完全一致、プレースホルダーの残留ゼロ）。69KBのニュース記事を`--news`モードで処理した場合、`gpt-5.6-luna`と`gpt-5.6-sol`の出力はいずれも、en/ja/ar向けの下流アプリケーションバリデーターを通過しました。`account/rateLimits/read`で使用量を実測した結果、`--eco`モードではカウンターの丸め閾値未満（5時間ウィンドウの0%）に収まりました。

- **1.9.2** ネストした括弧またはFR接頭辞を含むニュース帰属URLの抽出を修正（2026-05-11）：

  - **修正済みのバグ**：`_protect_news_quotes`における帰属URLの抽出では、正規表現`re.search(r"\((.+?)\)", attribution)`（括弧間の遅延キャプチャ）を使用していました。`(relayé par [@user sur X](https://x.com/.../123))`のような帰属（`(`の外側の括弧と、Markdownリンクの`]()`によるネストした括弧）では、キャプチャが最初に現れる`)`で停止し、文字列が途中で切れてFR接頭辞も含まれていました：`relayé par [@user sur X](https://x.com/.../123`（末尾の`)`なし）。その結果、`_validate_news_post`はこの文字列を翻訳出力内で探して必ず失敗していました（理由は2つあり、`)`が途中で切れていることと、「relayé par」が翻訳されて`relayed by`/`weitergeleitet von`/…になることです）。low → medium → high → gpt-5.5の完全なカスケードも通過できませんでした。
  - **修正**：正規表現を`re.search(r"\]\(([^)]+)\)", attribution)`に変更しました。Markdownリンクの`](url)`のみを対象にし、**純粋なURLだけ**をキャプチャします（FR接頭辞や途中での切断なし）。翻訳中は`#URL{N}#`プレースホルダーによって不変性が維持されます。問題となる2つのパターンに対応しています：
    - `(relayé par [@account sur X](url))` — ネストした括弧
    - `via [@source](url)`または`selon [@author](url)` — 外側の括弧がないFR接頭辞
  - **テスト**：`test_silent_failure.py`の`TestNewsCitationExtraction`クラスに2件を追加しました：
    - `test_extract_attribution_url_with_nested_parens`（Genspark CEO E2Bで発生したバグを正確に再現したケース）
    - `test_extract_attribution_url_with_french_prefix`（`via`を含む変種）
  - **カバレッジの不足**：`check-editorial-coverage.py`は編集上の構文を検証しますが、translatorによる翻訳可能性は検証しません。将来的な改善案（v1.9.2の範囲外）は、公開前にリスクのあるパターンを検出できるよう、dry-runで帰属抽出をシミュレーションするチェックを追加することです。

- **1.9.1** 翻訳marker注記のCTAラベルのi18nを修正（2026-05-10）：

  - **修正済みのバグ**：翻訳ファイル上部のmarkerバナーにあるCTAリンクのラベル`[Voir le projet sur GitHub ↗]`が、`target_lang`に従わず、すべての対象言語で**フランス語のまま**になっていました。URLとリポジトリのslugを保持するためPython側で組み立てられており、LLMからは見えないため、翻訳フェーズで修正できませんでした。これはv1.9で`marker`形式を追加して以来のサイレントなリグレッションです。
  - **修正**：15言語のローカライズラベルを対応付ける新しい定数`_VIEW_PROJECT_LABELS`を追加しました。`_translation_note_invariants(target_lang)`と`_assemble_translation_note_paragraphs(phrase, target_lang)`が対象言語を渡すようになりました。未知の言語には`fr`へフォールバックします（安全対策であり、KeyErrorを防ぎます）。
  - **テスト**：`test_source_emits_three_paragraphs_repo_title_description_link`を調整しました（target_lang `ja` → 期待される日本語ラベル）。新たに2件のテストを追加しました：`test_source_link_label_localized_per_target_lang`（ラテン文字、表意文字、アブジャドの各スクリプトを含む7言語でパラメーター化）と`test_source_link_label_falls_back_to_french_for_unknown_target`。合計は`test_translation_note_position.py`内の40テスト（38件から増加）です。
  - **後方互換性**：デフォルト値`target_lang="fr"`を持つシグネチャにより、`args.target_lang`を渡さない外部のプログラム呼び出しも変更なしで動作します。
- **1.9** サイレント失敗の修正 + 完全な品質ツールチェーン + 複数位置翻訳ノート（2026-05-07）：
  - **複数位置翻訳ノート + 「embed card」形式マーカー**：
    - 新しい CLI オプション（追加機能、デフォルトは変更なし → **非破壊的**）：
      - `--note_position {top,bottom,both}`（デフォルト：`bottom`）：翻訳ファイルの上部、下部、または両方にノートを配置します。
      - `--note_format {legacy,marker}`（デフォルト：`legacy`）：
        - `legacy` は v1.8 の挙動（太字段落 `**…**`）を厳密に再現します（**byte-for-byte**）。
        - `marker` は、非表示の Markdown リンク参照定義（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）に続いて、**3段落の blockquote** を出力します。これは「GitHub repo embed card」形式のレンダリング用に構造化されており、インラインコード形式のプロジェクトタイトル（`**\`ai-powered-markdown-translator\`\*\*`）、LLM による翻訳済み説明、表示される矢印付き CTA リンク（`[Voir le projet sur GitHub ↗](URL)`）を含みます。remark プラグインでビルド時に利用できます（jls42.org のブログ → プラグイン `remark-translation-banner`）。
    - **LLM に送信されない不変要素**：リポジトリのタイトルと GitHub URL は説明文の翻訳後に Python 側で組み立てられます。LLM が slug `ai-powered-markdown-translator` や `https://github.com/jls42/...` を見ることはないため、renderer・大文字小文字・scheme が変更されることはありません。
    - **Frontmatter 対応の挿入**：`top` または `both` モードでは、ノートは YAML frontmatter の **閉じる `---` ブロックの後**に挿入されます。Helper `_split_frontmatter` はファイル先頭の `---\n…\n---\n` を検出して完全性を保持し、閉じる fence のない未完了の frontmatter では **`RuntimeError` を送出**します。この場合、ファイルは `failed_files` に戻され、ノートが誤った位置に置かれた状態では書き込まれません。
    - **モデル sanitizer の whitelist**：`_sanitize_model` は `[A-Za-z0-9._:/-]` 以外のすべての文字を `_` に置換し、空になった場合は `unknown` にフォールバックします。Astro の remark プラグイン側のバリデーターに合わせ、空白、引用符、括弧、コンマなど、マーカー形式を壊す文字を無効化します。
    - **内部リファクタリング**：`_append_translation_note`（1つの巨大な関数）を、7つの純粋な helper（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）に分割しました。builder と composer を分離し、builder は区切り文字のない純粋なブロックを返し、composer は位置に応じて `\n\n` を適用します。本番処理と source helper は同じ3段落アセンブラーを共有します。
    - **`_quote_lines` の空行保持**：各行の先頭に `> ` を付け、空行を `>` のみに変換します。これにより mdast は blockquote 内で、1つの改行を含む段落ではなく、3つの異なる段落（タイトル / 説明 / リンク）として認識できます。
    - **`_build_translation_note_block` の適応処理**：LLM が保持した段落数に応じて処理します（3 = 完全なカード形式、2 = 文 + リンク、1 = フォールバック）。1段落のフォールバックでは、Markdown リンク `](` が検出された場合、リンクを囲む `**...**` は使用しません（リンク周辺の `<strong>` のレンダリングが不安定になるため）。
    - **後方互換性**：`_compose_with_notes` 側の `getattr(args, "note_position", "bottom")` と `getattr(args, "note_format", "legacy")` により、これらの属性を持たない Namespace（既存テストや外部のプログラム呼び出し）も変更なしで動作します。
  - **長い翻訳におけるサイレント失敗の修正**：
    - すべての provider（OpenAI、Mistral、Claude、Gemini）で翻訳後の言語を検証：決定論的レイヤー（ソースの一部が逐語的に再現されているか）+ 確率論的レイヤー（`langdetect`）
    - `finish_reason` / `stop_reason` の whitelist：whitelist 外の状態（truncation、content_filter など）では `RuntimeError` を送出
    - Claude の `max_tokens`：`4096` → `32768`（16k セグメントでの潜在的な truncation を回避し、FR→JA/ZH/KO/AR/HI のスクリプト間変換に余裕を確保）
    - 見出し対応のセグメンテーション：セグメントの後半では H2/H3 を優先し、各セグメントが完全な意味単位のセクションから始まるようにします。
    - エラーを non-zero の exit code まで伝播：`translate_markdown_file` は型付きステータス `success` / `failure` / `skipped` を返し、少なくとも1ファイルが失敗した場合は `main()` `sys.exit(1)`（単一ファイルと batch の両方）
    - すべての provider に空コンテンツガード、ソース/出力の妥当性比率（500文字以上、5%未満は拒否）、code placeholder の検証（`#CODEBLOCK`/`#INLINECODE`）、LLM 後の正規化（区切り文字やリンクが見出しに連結された場合）、`BadRequestError` を除外した retry（`reasoning_effort`）
    - 依存関係 `langdetect==1.0.9` を追加
  - **pre-commit 品質ツール**（「完全な EurekAI 型」、14 hooks）：
    - Pre-commit：ruff（lint + format）、shellcheck、prettier（md/yaml/json）、detect-secrets（4つの API key を保護）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（空白、EOF、large-files、shebangs など）
    - Pre-push：mypy（段階的な lax モード）、Opengrep SAST（translate.py + scripts/）、pip-audit（初期は reporting モード）、unittest discover（tests/ + scripts/tests/）
    - `scripts/` 内のローカル wrapper は `./venv/bin/python` を使用
    - `scripts/audit_verdict.py`：pip-audit の JSON parser と11個の unittest を実装。jls42-astro の parser を Python に移植
    - 初期の ruff 違反7件を修正：B904（raise from）×2、B007（未使用の dirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）
    - Lizard は一時的に `translate.py` を除外（CCN 21〜47の関数が4つあり、リファクタリングを予定）— scripts/ では厳格な gate を適用
  - **SonarCloud + 網羅的なカバレッジ**：
    - GitHub Actions workflow `SonarCloud`（sonarcloud.yml + sonar-project.properties）：各 push と pull-request で分析し、`coverage.xml` によって coverage を取得
    - README 上部に SonarCloud のバッジ11個（Quality Gate、Security/Reliability/Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）
    - `tests/test_silent_failure.py`（`unittest` stdlib）：サイレント失敗のエラーチェーン6段階をカバー
    - `tests/test_orchestration.py`（+79 tests）：`translate.py` のオーケストレーション層（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` TypeError + BadRequestError fallbacks、o1-series prompt format、`_validate_translation_output` の early-return 分岐）をカバー
    - `scripts/tests/test_audit_verdict.py`：`main()`（stdin/stdout）と、subprocess 経由の `if __name__ == "__main__"` ブロックをカバー
    - **新規コードの Coverage**：75.5% → 約98%（translate.py 98%、scripts/audit_verdict.py 97%）
  - **テスト**：`tests/test_translation_note_position.py` は位置 × 形式のマトリックス（E2E の `marker+top|bottom|both` と `legacy+top|bottom|both` を含む）、複数行のプレフィックス付与、byte-for-byte の後方互換性（golden literal）、sanitizer、frontmatter の分割（閉じる fence がない場合の raise を含む）、3段落形式、2段落フォールバック、1段落 + Markdown リンクの guard、さらにタイトルと URL が決して LLM に送信されないことを検証する重要な `TestLLMPayloadExcludesInvariants` をカバーします。**190 tests pass、回帰0件。**
  - ドキュメント：`README.md`（フランス語 + 14翻訳、バッジ付き）、`CLAUDE.md`（pre-commit workflow + 詳細な CI watch）、28翻訳を再生成
- **1.8** `--news` モード + 2026年モデル更新（2026-03-17、tag `v1.8`）：
  - デフォルトモデルを更新（2026年3月）：
    - OpenAI 品質：`gpt-5` → `gpt-5.4`
    - OpenAI 経済性：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 品質：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）、`gemini-3.1-pro-preview`（1M）のトークン上限を追加
  - `--news` モードの初期実装：`#NEWSQUOTE\d+#` による英語引用の保護、`LANG_FLAGS` のマッピング（15言語）、対象言語ごとのフラグ管理
  - 復元前に news placeholder を検証（回帰：placeholder を削除した LLM が引用なしの出力をサイレントに生成）
  - スクリプト `regen_translations.sh` をポータブル化（絶対パスを使用し、pwd に依存しない）
  - README/CHANGELOG の language bar に Français リンクを追加し、28翻訳を再生成
- **1.7** 新機能：
  - 翻訳時に元のファイル名を保持するオプション `--keep_filename`
  - API key を自動的に読み込む `.env` ファイルをサポート
  - **inline code の保持**：バッククォート（`` `...` ``）を翻訳中に保護
  - システム prompt を改善：
    - YAML frontmatter 内の引用符をより適切に処理
    - template 変数 `{variable}` を保護
    - 要求されていない翻訳者ノートを禁止
  - jls42.org のブログ移行で364ファイルを正常にテスト
- **1.6** 新機能：
  - 翻訳用 Google Gemini API をサポート（`--use_gemini`）
  - 2026年のデフォルトモデルを更新：
    - OpenAI：`gpt-5`（品質）、`gpt-5-mini`（経済性）
    - Claude：`claude-sonnet-4-5`（品質）、`claude-haiku-4-5`（経済性）
    - Gemini：`gemini-3-pro-preview`（品質）、`gemini-3-flash-preview`（経済性）
  - より高速で低コストなモデルを使用する経済モード（`--eco`）
  - ディレクトリを走査せずに単一ファイルを翻訳（`--file`）
  - 新しい簡略化された命名パターン：`{base}-{lang}.md`
  - モデル名を含む旧形式を保持するオプション `--include_model`
  - デフォルトのトークン上限（128k）付きで、リストにないモデルをサポート
  - README を14言語に翻訳
- **1.5** 改善：
  - **API key とデフォルトモデルを更新：**
    - **OpenAI：** `DEFAULT_MODEL_OPENAI` から `"gpt-4o"` に更新。
    - **Mistral AI：** `DEFAULT_MODEL_MISTRAL` から `"mistral-large-latest"` に更新。
    - **Anthropic の Claude：** `DEFAULT_ANTHROPIC_API_KEY` を追加し、`DEFAULT_MODEL_CLAUDE` から `"claude-3-5-sonnet-20240620"` に更新。
  - **翻訳 prompt を最適化：**
    - 直接翻訳と翻訳ノート用の prompt を拡充し、メタデータや特定の書式要素の保持に関する詳細な指示を含めることで、明確さと効率を向上。
  - **コードをリファクタリング：**
    - Mistral AI クライアントの初期化で `MistralClient` を `Mistral` クラスに置換。
    - 可読性と保守性を向上させるため import を再編成。
    - テキストのセグメンテーションと code block の処理を改善し、翻訳時に元の書式を保持。
  - **出力ファイルを管理：**
    - 出力ファイル名におけるモデルと言語の順序を反転（例：`f"{base}-{args.target_lang}-{args.model}.md"`）。翻訳の整理と検索を容易に。
  - **その他の改善：**
    - 不要な空行を削除してコードを整理。
    - script の構造と可読性を向上させるため細かな調整。
- **1.4** 新機能：
  - 翻訳用 Anthropic Claude API をサポート
  - 明確さと効率を高めるため prompt を最適化
  - コードの保守性を向上させるため細かな調整
- **1.3** 改善と新機能：
  - code block の処理を改善
  - 出力ファイルの処理を改善
  - 既存ファイルの検出を改善
  - 翻訳を強制するオプション `--force`
  - 出力ファイル名におけるモデルと言語の順序を反転
- **1.2** changelog を修正
- **1.1** Mistral AI API のサポートを追加
- **1.0** 初期バージョン - OpenAI API をサポート。

**記事はgpt-5.6-lunaでフランス語から日本語に翻訳されました。**
