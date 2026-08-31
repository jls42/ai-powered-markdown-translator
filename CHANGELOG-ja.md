### 変更履歴

🌍 [フランス語](CHANGELOG.md) | [英語](CHANGELOG-en.md) | [スペイン語](CHANGELOG-es.md) | [中国語](CHANGELOG-zh.md) | [ドイツ語](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [韓国語](CHANGELOG-ko.md) | [アラビア語](CHANGELOG-ar.md) | [ヒンディー語](CHANGELOG-hi.md) | [イタリア語](CHANGELOG-it.md) | [オランダ語](CHANGELOG-nl.md) | [ポーランド語](CHANGELOG-pl.md) | [ポルトガル語](CHANGELOG-pt.md) | [ルーマニア語](CHANGELOG-ro.md) | [スウェーデン語](CHANGELOG-sv.md)

- **1.11.0** PyPI で公開：リポジトリをクローンせずに `pip install ai-powered-markdown-translator`、続いて `aipmt` を実行可能（2026-08-31）：

  - **単一ファイルのスクリプトがインストール可能なパッケージになりました。** `translate.py` はルートから `src/aipmt/translate.py` に移動し、コンソールエントリーポイント `aipmt` と同等の `python -m aipmt` を追加しました。貢献するには引き続きクローンしたリポジトリが必要です — テスト、28 の翻訳、品質管理ツールがそこに存在するためです — しかし、利用するだけなら不要になりました。

    - **インポート名は `aipmt` であり、`translate` では決してありません**。この衝突は実際に発生し、しかも静かに起きるためです。PyPI パッケージ `translate`（v3.8.1、最終アップロードは 2026-07-06）は同名のディレクトリをインストールします。venv で再現すると、ディレクトリがモジュールより優先され、`translate.main` が消え、エントリーポイントが `AttributeError` で失敗します — そして `pip check` は「壊れた要件は見つかりませんでした」と rc=0 で応答します。ユーザー側で単純に `pip install translate` するだけで、診断不能なまま CLI が壊れるところでした。実際の wheel で反証も確認しました：パッケージの上に `pip install translate` を実行しても、前後とも `aipmt --help` は rc=0 で、両方の CLI が共存します。
    - **配布名は長く、コマンド名は短く。** `ai-powered-markdown-translator` なら PyPI 検索でパッケージを見つけられます。プロジェクトをすでに知っている人でなければ単独の略語は見つけられないため、今回の公開はまさに「見つけてもらう」ことを目的としています。もっともらしい候補を 2 つ検証して除外しました：`ai-markdown-translator` は 2024 年以来、同じ目的のツールによって npm で使用済みで、このリポジトリより 17 か月先行しています。また `aimt` は `aim`（v3.29.1）と 1 文字違いで、同じ分野の稼働中パッケージです — 永続的な混同を招く最悪の構成です。ここで方法上の落とし穴も判明しました：`pypi.org/project/<nom>/` はボット対策ページのため、どんな名前に対しても 200 を返します。信頼できるのは JSON API だけです。
    - **フラットパッケージではなく `src/` レイアウト。** フラットパッケージならテストにある 6 つの `sys.path.insert(..., "..")` を維持できましたが、それこそが問題です。これらはソースツリーをパッケージより先にインポートするため、パッケージ化の誤りを隠してしまいます。実際のコストは置換ルールが 1 つ増えるだけです。

  - **修正 — ツールのインストール後、ユーザーの `.env` が無視されていました。** 引数なしの `load_dotenv()` はカレントディレクトリから遡るのではなく、呼び出し元ファイルから遡るため、`site-packages` を起点にしていました。独自の `.env` を持つプロジェクトから実際のコンソールエントリーポイントを起動して測定したところ、`find_dotenv()` は `''` を返してキーを読み込めませんでしたが、`find_dotenv(usecwd=True)` なら見つけられました。ツールがクローンしたリポジトリからのみ実行されていた間は存在しなかったバグですが、公開後は常に発生し、正しい設定で API キーが「見つからない」という症状だけが現れるところでした。

  - **何も検証しなくなっていたら、3 つのゲートがグリーンになっていました。** これらは移動前に、意図的に強化しました。捕捉すべき変更の後で書かれた防護策では、何も証明できないためです。元のリポジトリではそれぞれグリーンになり、移行済みコピーではレッドになります — 両方向を測定しています。

    - **Lizard は存在しないパスを何も言わずに無視します**：rc=0、「0 file analyzed」。複雑度ゲートは 158 関数 / 2247 nloc から 3 関数 / 34 nloc へ変わり、出力は 0 バイトになっていたはずです。現在はスコープを配列として扱い、各エントリの存在を検証しています。
    - **存在しないモジュールに対する `coverage run --source=` は失敗しません**：stderr の警告だけで、unittest でも `coverage xml` でも rc=0 となり、レポートはそれでも公開されます — 1453 から 141 statements に削減された状態で。ほとんど分析されなくなっていたため、プロジェクトは健全に見えてしまいます。レポートを守る下限を 2 つ設けました：合計値と、測定対象となった最大ファイルです。
    - **翻訳の鮮度を調べるプローブは、呼び出し形式に対して構造的に盲目です**：argparse のフラグを基準にしており、まさにファイル名の変更では変わらない部分です。再現すると、モジュールを移動しても、15 個の README が存在しないコマンドを記載したままなのに、判定は「期限切れの翻訳なし」になります。そのため 7 番目のセクションではオプションではなく形式を検証し、Lizard フックはスクリプトの実際のスコープと照合されます — その `files:` キーが一致しなくても pre-commit を失敗させず、スキップさせます。

  - **`requires-python = ">=3.10"` はもはや主張ではありません。** `sonar-project.properties` はすでに 3.10-3.12 を宣言していましたが、開発環境には 3.12 しかなく、実際には一度も実行されていませんでした — 公開によって明らかになる内部矛盾です。現在はテストワークフローが 3.10、3.11、3.12 でスイートを実行し、パッケージをインストールすることで公開されている対応範囲も検証します。

  - **下限のみ、上限なし。** `requirements.txt` はテスト対象のロックとして残し、`[project.dependencies]` は公開契約になります。ロックの正確なバージョンを公開すると、別のパッケージを使用するすべてのユーザーと衝突するためです。`<N+1` の上限も設けません — これは、メジャーバージョンの遅延をすべてリリースゲートで失敗させる `check-deps-fresh.sh` と正面から矛盾するためです。下限の組み合わせで解決し、反証として `openai==1.0.0` は `ResolutionImpossible` で終了します。これにより、チェックが何でも受け入れるのではなく、正しく区別していることが証明されます。さらに、`pyproject.toml` のバージョンが CHANGELOG のものと異なることを禁止する防護策も追加しました。PyPI では同じ番号を再利用できないためです。

  - **新しい venv で最初から最後まで検証済み**：69,768 バイトの wheel に含まれるのは `aipmt/*.py`、dist-info、ライセンスだけです；`aipmt --help` は 22 個のフラグで rc=0；`python -m aipmt` は「usage: \_\_main\_\_.py」ではなく「usage: aipmt」を表示；`pipx` のインストールは正常に機能；そして何より、**任意のユーザーディレクトリから実際に fr→en 翻訳**を行い、太字、リスト、インラインコード、リンク、URL を保持し、コードブロックは翻訳しませんでした。318 個のテストは、移行前後でバイト単位まで同一の識別子リストを使って通過しています。テストが無効化されていないことを証明するのは「OK」ではなく、これです。

- **1.10.0** `--use_codex` プロバイダー（ChatGPT サブスクリプションのクォータ）、SDK とモデルを更新、複数段落のニュース引用を修正（2026-08-29）：

  - **セキュリティレビュー — PR が設置したものの、すべての箇所で維持できていなかった 2 つの防護策**：

    - **Codex の preflight が `.env` 全体をバイナリに渡していました。** `_codex_preflight` は **`env=` なしで** `subprocess.run` を呼び出していました。サブプロセスは `os.environ` 全体、つまり `load_dotenv` が読み込んだ `.env` の全内容を継承していたのです。計測用の偽バイナリで測定したところ、preflight に到達した秘密情報は **7 個** — 6 つのプロバイダーのキーと 1 つの `GITHUB_TOKEN` — でした。一方、対応する `_grok_preflight` では **0 個**でした。こちらは正しく `env=_grok_env()` を渡していました。この不整合は PR 内部のものでした：数行先に、まさにこの不変条件を維持するための `_strip_secret_env` が存在していたためです。`_codex_env_base()` を抽出して両方の経路で共有し、修正後に両側とも秘密情報が 0 個であることを測定しました。
    - **「`--deny` fail-closed」という性質は、実際に使われた形式を対象としていませんでした。** コメントでは、未知のプレフィックスを持つルールが起動を拒否することを、Grok の隔離全体の根拠としていました。`grok 1.0.13` で測定すると、この検証は **括弧付き形式に対してのみ**存在します：`--deny 'CeciNestPasUnOutil(*)'` は「unknown tool prefix」として起動を拒否しますが、`--deny 'CeciNestPasUnOutil'` は黙って受け入れられます。しかし `GROK_DENY_RULES` が使用していたのは裸の名前だけでした。したがって xAI 側でツール名が変更されると、OS サンドボックスがすでに適用されない環境で、測定済みの唯一の隔離層が何の通知もなく失われることになります。8 つの名前付きルールは `Prefix(*)` を通過し、それぞれ CLI の既知のプレフィックスであることを検証しています。catch-all の `*` は、唯一受け入れられるリテラル形式のまま残しました。検証されていない形式に戻らないよう、テストも追加しました。
    - **その他の検証は問題ありませんでした**：コマンドインジェクションなし（常にリスト形式で、`shell=True` は一切使用せず、ドキュメントの内容は stdin または `--prompt-file` 経由）、安全でないデシリアライゼーションなし（`json.loads` のみ、型チェック付き）、7 つのペイロードでパス走査の回避がないことを修正済み、そして `--deny '*'` が CLI によって実際に適用されること（workdir 外の読み取りで `DENY_ENFORCED` を確認）。
    - 上で追加した鮮度チェックも、その原則自体を回避していました。PyPI リクエストが失敗したパッケージは黙ってスキップされ、ゲートはグリーンになっていたのです。現在は実際に比較されたパッケージ数を数え、カバレッジが不完全なら失敗します。

  - **依存関係を更新し、遅延を再発させないための 2 つの網も追加**：

    - **遅延は実際に存在し、長期化していました**：`openai` 2.54 → **3.6.0**、`anthropic` 0.125 → **1.2.0**、`certifi` 2024.8.30 → **2026.7.22** — すべてのプロバイダー呼び出しで TLS を検証するルート証明書ストアが 2 年遅れていました。原因は **`.github/dependabot.yml` が存在しなかったこと**です。このファイルがないと、GitHub は _security updates_ だけを有効にし、Dependabot は CVE の対象となる依存関係に対してのみ PR を提案します。そのため `urllib3` と `idna` は更新した一方で、2 つの SDK がメジャーバージョン単位で古いままになっていました。
    - **2 つのメジャーバージョンは衝突せず共存します**。以前の推論では衝突が懸念されていましたが、`openai` 3.x と `anthropic` 1.x は `httpx2` に移行し、`mistralai` と `google-genai` は `httpx<1` に残ります。しかし、これは異なる 2 つのディストリビューションです。実際にインストールして確認し、さらに **7 つのプロバイダー経路を最初から最後までテスト**しました — OpenAI、Claude、Mistral、Gemini、Grok API、Codex CLI、Grok CLI — 各出力でインラインコードとリンクを保持しています。「HTTP スタックを 2 つ避ける」は好みであって阻害要因ではなく、測定によって結論が出ました。
    - **`requirements.txt` は実際の環境を記述していませんでした**：`google-auth`、`cryptography`、`opentelemetry` スタックは作業用 venv にインストールされていたものの、宣言されていませんでした。そのため、新規インストールではテスト対象の状態を再現できませんでした。逆に、`tokenizers`、`huggingface-hub`、`PyYAML` は記載されていましたが、どこからもインポートも要求もされておらず、`mistralai` 1.x の残骸でした。ファイルを、直接依存関係だけから構築した venv の完全な依存関係閉包として再生成しました。`pip-audit` は新しい構成に既知の脆弱性がないことを報告しています。
    - **`.github/dependabot.yml`**（新規）は、バージョン、pip、github-actions の週次更新を有効にします。マイナーとパッチは 1 つの PR にまとめます。パッチごとに PR を作ると無視され、ノイズは更新の敵になるためです。**メジャーは分離**し、それぞれ実際の呼び出しによる検証を必須とします。
    - **`scripts/check-deps-fresh.sh`**（新規、ゲートに接続済み）は、遅延をプロジェクトの判定に反映します。Dependabot は提案するだけで保証はせず、PR が積み重なることもあります。メジャーの遅延 → 失敗；マイナー → 警告。常に赤いゲートは最終的に無視されるためです。PyPI に接続できない場合 → ローカルでは明示的にスキップし、**CI では fail-closed**。実行されていないチェックは成功ではないためです。両方向で検証しました：修正前の正確な状態（`openai 2.54.0→3.6.0`、`certifi 2024.8.30→2026.7.22`）を検出し、マイナーの場合は警告だけを出します。

  - **この PR のレビューから生まれた修正** — 5 つのレビューエージェントが差分を精査しました。以下の項目はすべて、修正前に **測定によって再現**され、そのうち 2 つはこの同じバージョンで上記の変更によって導入されたリグレッションでした。
- **修正済みのリグレッション — `_NEWS_CITATION_REGEX` には指数バックトラッキングがあった。** 複数段落対応の修正で、繰り返し内に `(?:[ \t]*$|[ \t]+.*)` が導入されていた。`[ \t]+` と `.*` の間の空白の共有が曖昧で、その曖昧さが反復ごとに増幅していた。パターンにマッチしない `>   texte` の行 — 完全に合法な Markdown のインデント — で測定したところ、修正前は**14行で2,589 ms**だったのに対し、修正後は0.04 msとなり、1行追加するごとに約9倍の係数が生じていた。`--news` モードでは、長く規格に適合しない blockquote だけで翻訳がジョブのタイムアウトまで停止し、原因も特定できなかった。現在は繰り返しが行全体を一括で消費する（`\n^>(?![ \t]*—).*`）ため、反復ごとのマッチ方法が1通りしかない。実際の231記事のコーパスで検証した結果、キャプチャの差異は**ゼロ**で、同じ423件の引用が得られ、複数段落の本文14件も引き続き拡張された。
    - **2つの provider フラグを同時に指定すると、気付かないまま従量課金になっていた。** `--use_codex --use_mistral` は受け入れられていた。`_select_provider_client` は最初に Mistral を検査し、`_resolve_provider` は明示的な真偽値を優先するため、どちらも Mistral に収束していた。ユーザーはサブスクリプションの割り当てを求めていたにもかかわらず、警告を一切受けずに従量課金されていた。これはまさに `--use_codex` が防ぐために存在する障害モードである。現在、6つの provider フラグは `add_mutually_exclusive_group` を通る。**動作変更**：これまで黙って受け入れられていた2つの provider を組み合わせたコマンドラインは、現在は `argument --use_mistral: not allowed with argument --use_codex` で失敗する。
    - **プローブがクラッシュすると、作業完了ゲートが緑になっていた。** `scripts/check-release-ready.sh` の13個の検査のうち4個は、「stdout を捕捉し、空なら結論を出す」というパターンに従い、終了コードを一度も確認していなかった。例外（ファイルのリネーム、`FileNotFoundError`）が stderr に書き込まれて stdout が空になると、検査は「報告すべきものはない」と結論していた。それを防ぐために書かれたスクリプト内で、「1つの `exit 0` は何も証明しない」という落とし穴が再現されていた。現在はヘルパー `probe()` が、ゼロの終了コード**と**終了センチネルの両方を必須とし、プローブは参照点の集合が空の場合に結論を出さない。空集合に対するアサーションは常に真だからである。実例として、上記の排他的グループを追加したことで、provider フラグは `*_group` オブジェクトを通るようになり、旧来の正規表現 `parser\.add_argument\(` ではマッチしなくなった。その結果、21個中**6個のフラグ**が黙って対象範囲から外れ、ゲートは緑になっていた。
    - **シークレットのスキャンが6つ中4つの provider を見逃していた。** `[A-Za-z0-9]` クラスはハイフンを除外するため、`sk-proj-…`（現在の OpenAI 形式）と `sk-ant-api03-…` は2つ目のハイフンで失敗し、`AIza…` は対象外だった。パターンを拡張し、`.secrets.baseline` をスキャン対象から除外した。さらにガード `.env` は `git diff --cached` を照会していたが、これはインデックスしか見ないため、最悪のケースである**すでにコミット済み**の `.env` は決して現れなかった。現在は `git ls-files` を照会する。
    - **Codex の「トークンのウォームアップ」はウォームアップではなかった。** 測定の結果、`codex login status` は `~/.codex/auth.json` に触れず（mtime とサイズは変化せず）、そのヘルプには「Show login status」と書かれていた。しかしコメントは、ローテーションする単回使用トークンに対する同時 refresh のリスクを無効化するため、「一度、逐次的に」トークンを更新すると主張していた。宣言されていた保護は存在しなかった。現在、コメントはコードの実際の動作を説明しており、実際の対策は引き続き `max_jobs=4` である。さらに検査は、無視していた `CODEX_BIN` にも対応する。`codex` が `PATH` にないマシンでは、「未認証」で失敗していたが、これは誤解を招く診断だった。
    - **`.env` はサブシェル内で読み込まれていた。** `detect_provider` はコマンド置換で呼び出されるため、その export は上位に戻らなかった。したがって、`GROK_BIN`、`GROK_HOME`、`REGEN_MODEL` のいずれかが `.env` で定義されていても、`main()` で行われる読み取りからは見えず、正しい設定であっても「Grok バイナリが見つからない」と結論されていた。
    - **同時実行数が告知された上限を50%超えていた。** ガードが README/CHANGELOG のペアを起動した後に置かれていたため、測定されたピークは **`max_jobs=2` が3** だった。Chat/Imagine/Voice と週次の割り当てを共有し、測定可能な上限がない Grok では、スクリプトが設定する上限が守られていなかった。最終カウントは表示されていたものの、28と比較されていなかったため、ファイルが1つ欠けても見逃されていた。
    - **Grok の出力契約：`stopReason` がない場合も失敗になった。** コードは、契約で要求されている `end_turn` の代わりに「`end_turn` **または存在しない**」を適用していた。フィールドのない payload、または CLI の更新でフィールド名が変更された payload によって、ガードは黙って no-op になっていた。また、`max_turn_requests` は rate limit に分類されなくなった（使い切られたのはターンの予算であり、再試行しても90秒待ったうえで同じ結果になるため）。`quota` は rate limit のマーカーから外れた。これは `_codex_is_rate_limited` の docstring がすでに説明していた理由を、Grok が適用していなかったためである。
    - **Gemini のフォールバック連鎖をモデル単位でメモ化した。** セグメントごとに `minimal` から再開していたが、デフォルトモデルはそれを拒否するため、通常経路ではセグメントごとに400の往復を行い、同じ警告を再表示していた。警告が何百回も繰り返されると読まれなくなる — それがマスクになる仕組みである。
    - **その他**：CI での拒否メッセージが Codex 用にハードコードされており、`--use_grok_cli` のユーザーを `XAI_API_KEY` ではなく `OPENAI_API_KEY` へ誘導していた。`provider.capitalize()` は「Grok_cli」と「Openai」を表示していた。サブプロセス基盤のコメントは「shim」を2つの CLI に一般化していたが、Grok バイナリはネイティブ ELF である（正しい理由は「独自のサブプロセスを spawn する agent」）。`subprocess` に関する12件の SAST findings は、理由を添えて `# nosec` / `# nosemgrep` とマークされた。`shell=True` のないリスト形式ではインジェクションが不可能であり、ドキュメントの内容が argv を通過することもない。
    - **agent のサブプロセスにシークレットが入ることはなくなった。** 名前を列挙した deny-list が保護していたのは、**課金**の不変条件（`OPENAI_API_KEY` のない Codex、`XAI_API_KEY` のない Grok）だけだった。測定の結果、さらに**7つのシークレット**が各サブプロセスに入っていた。Anthropic、Mistral、Google、Gemini のキー、もう一方の CLI のキー、そしてシークレットではないがトラフィックを転送する `OPENAI_BASE_URL` である。これら2つの CLI は**agent**であり、Grok は多くの Linux マシンで適用可能な OS sandbox なしに動作する。現在は名前の列挙ではなく、**名前のパターン**（`API_KEY`、`_TOKEN`、`SECRET`、`PASSWORD`、`CREDENTIALS`）によってフィルタリングするため、コードが認識していない環境変数をユーザーが `.env` に追加した場合も対象になる。CLI にこれらは不要である。認証は `~/.codex` と `~/.grok` に存在し、環境変数には決して置かれない。環境を強化した状態で、2つの provider それぞれを使った**実際に成功する翻訳**によって検証済みである。
    - **テスト**：`tests/test_review_hardening.py`（21テスト）を新規作成し、provider フラグの排他性、`stopReason` 契約、news 正規表現の線形性、CI での拒否メッセージ、Gemini のメモ化、サブプロセス環境にシークレットが一切ないことを固定した。最後のアサーションは**汎用的**であり、どのリストにも名前がないキーでも失敗する。一方、既存の消去テストは定数の鏡写しであり、自身のループの障害以外は検出できなかった。完全なスイートは**311テスト**になった。

  - **2つの新しい Grok provider**：`--use_grok`（xAI API、キー `XAI_API_KEY`、従量課金）と `--use_grok_cli`（公式 Grok Build CLI、Grok サブスクリプションから差し引き — `--use_codex` と同じ原理）。
    - **API モード、約40行**：xAI の endpoint は OpenAI 互換なので、クライアントと `_call_openai` をそのまま再利用し、変更するのは `base_url` だけである。必要な適応は1つだけで、それはすべての provider に恩恵をもたらす。`finish_reason` が `end_turn` も受け入れるようになった。これは xAI が出力する形式であり、OpenAI は `stop` を出力する。モデルは `grok-4.6`（品質）と `grok-4.3`（エコ）。なお、Grok のエコモデルはリポジトリ内で最も高価なままである。100万トークンあたり $1.25/$2.50 で、`mistral-small-latest` の $0.15/$0.60 と比較すると高い。この provider は価格ではなく、モデルの多様性を理由に選ぶものである。
    - **CLI モード**：Codex を手本にしつつ、実環境上の理由で4つの相違がある。prompt はファイルで渡す（`--prompt-file`。CLI は stdin を読み込まず、セグメントを argv にすると `ps` から見えてしまう）、出力は stdout 上の単一 JSON オブジェクトである（JSONL でも `-o` ファイルでもない）、サブスクリプションが公開するのは `grok-4.6` と `grok-4.5` だけであり、sandbox は適用できない（以下を参照）。サブプロセスの起動は `_codex_run_process` で Codex と共通化し、すでにテスト済みの Codex provider の残りには触れていない。
    - **`exit 0` は何も証明しない。実測済みである。** 未認証の場合、CLI は **stdout** に `{"type":"error","message":"Not signed in."}` を書き、終了コードは**0**になる。拒否やターン超過も同じように動作する。そのため出力契約では、終了コード0、エラー payload がないこと、`stopReason == end_turn`、空でないテキストの4条件を同時に要求する。preflight も同じ考え方に従う。`grok models` は切断中でも0で終了するため、stdout に「not authenticated」が存在する場合のみ結論を出せる。
    - **隔離：非対称性を受け入れ、文書化した。** Codex が `--sandbox read-only` で動作する一方、Grok の sandbox は、`sudo` なしでは多くの最新 Linux マシンに適用できない。原因は独立した2つのシステム上の問題で、回避不能である。Ubuntu 24.04 以降では AppArmor が特権のない user namespace をブロックする（`bwrap: setting up uid map: Permission denied`。Grok 外でも再現可能）。また、コンテナ runtime socket の deny-list は、`/run/podman` が `0700` の場合に失敗する（resolver が回復させるのは `ErrorKind::NotFound` だけで、EACCES は致命的になる）。中心的な落とし穴は、適用できない**組み込み**プロファイルが、**隔離されていない状態で黙って起動する**ことである。そのためスクリプトはデフォルトでプロファイルを要求せず、決して黙ってフォールバックしない — stderr に警告する。保護は CLI の `--deny` ルール（catch-all の `*` を含む）に依存する。これは測定済みで唯一の _fail-closed_ 層であり、未知のプレフィックスを持つルールがあると起動を拒否する。`GROK_TRANSLATE_SANDBOX=read-only` を使えばこれを必須にでき、その場合、マシンが適用できなければ起動に失敗する。
    - **ガード**：`XAI_API_KEY`、`GROK_API_KEY`、`GROK_SANDBOX` をサブプロセスの環境から削除する（キーがあると従量課金に切り替わり、継承された `GROK_SANDBOX` が適用不能なプロファイルを強制し、誤解を招くメッセージを出す）。MCP/hooks/skills/agents のスイッチを無効化し、`--disable-web-search`、`--no-subagents`、`--no-plan`、使い捨ての workdir、CI での拒否、プロセスグループを終了させる timeout、rate limit 時の back-off を設定する。`--max-turns` は1ではなく6に固定する。ツールのターンの後にカウンターが増分されるため、1では出力が切り詰められるからである。
    - **Quota**：Grok の pool は週次で、**Chat、Imagine、Voice と共有**されており、それを公開するコマンドはない。`account/rateLimits/read` によって消費量を数値化できる Codex とは異なる。そのため `regen_translations.sh` は同時実行数を2に制限し、明示的に警告する。
    - **テスト**：`tests/test_grok_provider.py`（24テスト）を新規作成した。完全なスイートは**290テスト**になった。
  - **修正済みのバグ — EN の複数段落引用が一部しか保護されていなかった（`--news` モード）**：`_NEWS_CITATION_REGEX` は引用本文として、`>` の行が**連続**する列だけを受け入れていた。引用が複数段落（`>` の空行で区切られる）にまたがると、最後の段落だけがキャプチャされて placeholder に置換され、前の段落は LLM に送られて翻訳されていた。これは `--news` が保証するために存在する目的と完全に逆である。現在は繰り返しが内部の `>` の空行を受け入れ、非貪欲になったため、最初に見つかった空行ではなく、斜体の行の前にある `>` の空行で停止する。
    - **測定した規模**：実際の198記事のコーパスで、該当する引用は419件中11件だった。リグレッションはない。新しい正規表現はまったく同じ数の引用をキャプチャし、複数段落の本文だけが拡張された（408件は同一、11件が拡張）。帰属行 `> — …` が本文に取り込まれることもない（lookahead は維持）。
    - **エンドツーエンドの証明**：ja/ar に翻訳した69 KBの記事で、以前は日本語で `> GLM-5.3がオープンウェイト化。` と出力され、アラビア語でも同様に翻訳されていた引用の最初の段落が、現在は `> GLM-5.3 is now open-weight.` のままになった。英語の引用行数は9行から10行に戻り、ソースと一致する。
    - 注：この欠陥は下流のバリデーターでは検出されなかった。引用の存在は確認していたが、完全であるかどうかは確認していなかった。
  - **デフォルト provider で測定した節約**：`_openai_extra_kwargs` は、モデルが `gpt-5` で始まると、`--eco` の場合も含めて、すぐに `reasoning_effort="medium"` を送信していた。10語の文を翻訳するための `gpt-5.4-mini` で測定した結果、`medium` は reasoning token 45、出力トークン65だったのに対し、`none` は0と14だった。推論は翻訳に何ももたらさず、各ファイルの各セグメントで課金されていた。デフォルトは `--eco` では `none` になり、それ以外では `medium` のままとなる。CLI で明示的に渡された値は引き続き優先される。`--reasoning_effort` は `low`/`medium`/`high` に加えて、`none` と `xhigh` も受け入れるようになった（すべてのモデルがすべてを受け入れるわけではない。例えば `minimal` は `gpt-5.4-mini` に拒否されるが、既存のパラメーターなし retry がこのケースを処理する）。
  - **SDK の更新と Gemini の移行**：`google-generativeai`（サポート終了日は2025-11-30、リポジトリはアーカイブ済み）を、統合 SDK **`google-genai`** に置き換えた。`genai.Client(api_key=...)`、続いて `client.models.generate_content(model=, contents=, config=)` を使用し、システム prompt はセグメントに連結するのではなく `system_instruction` として渡す。`mistralai` は **2.9.4** になった（import は `from mistralai.client import Mistral` となり、旧形式は `ImportError` を発生させることを wheel で検証済み）。`anthropic` は **0.125.0**、`openai` は **2.54.0** となった。これは `httpx2` への切り替え前の最後のバージョンであり、venv 内に2つの HTTP スタックを共存させないためである。その結果、`httpx` 0.28.1 と `pydantic` 2.13.5 も利用可能になった。
  - **実際のテストで検出され、ドキュメントでは検出されなかった2つのリグレッション**：
    - `anthropic` 1.0以上では、`max_tokens` から10分を超えることが予想される、非ストリーミングのクライアント呼び出しを拒否する（`ValueError: Streaming is required...`）。このガードは0.34.2には存在せず、`max_tokens=32768` を使うすべての Claude 呼び出しを壊していた。明示的な `timeout`（デフォルト900秒の `CLAUDE_TIMEOUT`）で修正した。完全な応答だけを利用する呼び出しをストリーミングに切り替えずに済む。
    - `thinking_level="minimal"` は Gemini のカタログの一部のモデルでしか受け入れられない。`gemini-3.1-flash-lite` は対応するが、`gemini-3.7-flash` と `gemini-3.1-pro-preview` は400で拒否する。そのため `_gemini_generate_with_fallback` を導入した。これは `minimal` → `low` → thinking_config なしというフォールバック連鎖で、すでに存在する OpenAI のフォールバックをモデルにしている。最適化用のパラメーターによって翻訳が失敗してはならない。
  - **デフォルトモデルを更新し、それぞれ実際の呼び出しで検証した**：OpenAI は `gpt-5.5` → **`gpt-5.6-terra`**（28件のバッチで−60%）、`gpt-5.4-mini` → **`gpt-5.6-luna`**（−73%）。Claude は `claude-sonnet-4-6` → **`claude-sonnet-5`**（より安価で新しい）および `claude-haiku-4-5-20251001` → **`claude-haiku-4-5`**（日付のない正規 ID）。Gemini は `gemini-3.1-pro-preview` → **`gemini-3.7-flash`**、`gemini-3.1-flash-lite-preview` → **`gemini-3.1-flash-lite`**（安定版で、`3.5-flash-lite` より安価）。
Mistralは変更されず、4つの中で引き続き`mistral-large-latest`が最もコストパフォーマンスに優れています。なお、`gemini-3.1-pro-preview`より新しいProラインのGeminiモデルは存在しません。2026年5月に発表されたGemini 3.5 Proは発売されず、3.5/3.6/3.7ラインはFlash専用です。
  - **Geminiへ切り替える前に測定したA/Bテスト**：`README.md`を`gemini-3.1-pro-preview`で日本語に翻訳し、その後`gemini-3.7-flash`を実行。構造は完全に同一（21個のリスト、18個のコードブロック、13個のHTMLリンク、13個の画像、すべてのURLを保持）で、**48秒に対して8秒**でした。これら2モデルを翻訳または非ラテン文字スクリプトで比較する公開ベンチマークは存在しないため、そうでなければ切り替えは単なる推測に基づくものになっていました。
  - **Claudeの応答ブロックのフィルタリング**：`_call_claude`は型をフィルタリングせずに`block.text for block in response.content`していました。適応型推論モデル（Sonnet 5以降）は`thinking`ブロックを挿入します。このブロックは`.thinking`を公開し、`.text`は公開しないため、最初のセグメントで不透明な`AttributeError`に遭遇すると翻訳が壊れていました。現在は`thinking`、`redacted_thinking`、`tool_use`、`tool_result`を除外しています（未知の型でテキストを含むものにも対応できるよう、除外リスト方式を採用）。テキストブロックが1つもない応答では、明示的なエラーが発生します。`thinking={"type": "disabled"}`は各呼び出しに渡されます。
  - **`MODEL_TOKEN_LIMITS`を再同期**：廃止日を過ぎたモデルを削除（`magistral-*`ファミリーは2026-07-31、`gemini-2.0-*`は2026-06-01、`gemini-3-pro-preview`は2026-03-09に廃止、`claude-3-5-sonnet-20240620`、`claude-3-7-sonnet-20250219`、`claude-opus-4-1-20250805`、`claude-sonnet-4-20250514`）。上限を修正：Mistral 128K → **256K**（Large 3 / Small 4世代）、Gemini 1 000 000 → **1 048 576**（実際の入力上限）、`claude-opus-4-5` 200K → **1M**、`gpt-5.6-*`ファミリー 400K → **1.05M**。Claude 5（`claude-sonnet-5`、`claude-opus-5`、`claude-fable-5`）、`claude-opus-4-8`、Gemini 3.5/3.6/3.7、`mistral-medium-latest`、`ministral-*`ファミリーを追加。なお、これらの上限はあくまで目安であり、`translate()`は分割を`min(16000, limite)`に制限しています。

  - **Provider `--use_codex`**：公式Codex CLI（`codex exec`）を非対話モードで制御する5番目のprovider。従量課金APIを呼び出す代わりに、すでに支払い済みのChatGPTサブスクリプションのクォータから翻訳分が差し引かれます。これがOpenAIがこの用途について文書化している唯一の方法です。プラン別利用可能機能の一覧では、「Codex SDK、`codex exec`、and scriptable workflows」がPlus/Pro/Business/Enterpriseで利用可能とされています。一方、`~/.codex/auth.json`のトークンではPlatform APIの呼び出しを認証できず、このスクリプトが読み取ることもありません（認証と更新はCLIが引き続き管理します）。
  - **Codexバイナリをnpmだけでなくpipでもインストール可能に**：`_resolve_codex_binary()`はまず`CODEX_BIN`でバイナリを探し、次に`PATH`、その後OpenAIが公開する公式Pythonパッケージ **`openai-codex-cli-bin`**（`openai-codex` SDKの依存関係）を探します。そのため、Pythonプロジェクトで`--use_codex`を使うためにnpmのグローバルインストールは不要になりました。パッケージは`requirements.txt`には追加していません。バイナリのサイズが約250 MBあり、任意のproviderのために全ユーザーへ強制することになるためです。最初から最後まで検証済みです。`codex`が`PATH`に存在しない状態で、パッケージ化されたバイナリが解決され、完全な翻訳が6秒で完了しました。
  - **「サブスクリプションモード」の保証**：`OPENAI_API_KEY`と`CODEX_API_KEY`をサブプロセスの環境から削除します。この保護がなければ、`.env`に存在するキーによってCodexが目に見える通知なしに従量課金へ切り替わる可能性があります。まさにそれを防ぐためにこのproviderが存在します。
  - **CLIの落とし穴をテストで固定**：
    - `codex exec`は、プロンプトを引数で渡した場合**でも**stdinを読み取ります。stdinを閉じないと、モデルを一度も呼び出さないままコマンドがタイムアウトまで待機します（再現結果：180秒後にexit 124、0バイト）。そのため`communicate(input=...)`は必須です。
    - npmでインストールされる`codex`は、実際のRustバイナリを`spawn`するNode shimです。このバイナリはPythonプロセスの**孫プロセス**であり、`SIGKILL`の`subprocess.run(timeout=)`後も存続してクォータを消費し続けます。そのため`Popen(start_new_session=True)` + `os.killpg`が必要です。
    - CLIは`turn.failed`を出力していても終了コード0になることがあります。JSONL出力（`--json`）を終了コードに加えて検査し、終了コード0なのに`-o`がない場合は、空のセグメントを生成せず明示的なエラーを発生させます。
  - **レート制限時のバックオフ**：CLIには内部リトライが実装されていません（`max_retries = 0`）。分類は部分文字列ではなくJSONペイロードの構造（`status: 429` / `error.type`）に基づきます。「quota」という語は、回復可能な429と、回復不能な`insufficient_quota`の両方に現れるためです。
  - **CIガード**：`--use_codex`は`CI`または`GITHUB_ACTIONS`が定義されている場合に拒否されます。サブスクリプション認証は共有runner向けに想定されておらず、OpenAIも公開リポジトリでこのワークフローを使わないよう明示的に推奨しています。
  - **モデル**：`gpt-5.6-sol`（品質）と`gpt-5.6-luna`（`--eco`）。`gpt-5.6-*`ファミリーはCLIとPlatform APIに共通ですが、ChatGPTアカウントですべてを利用できるわけではありません。allowlistはサーバー側で適用され、ローカル検証は行われないため、通常とは異なるモデルを指定すると警告が発生します。Plusプランでは、Lunaは5時間のウィンドウあたり250～2,000メッセージ、Solは10～100メッセージです。そのため、`--eco`はあらゆるバッチ処理に推奨されるモードです。
  - **修正済みのバグ — 完全に成功していたにもかかわらず`regen_translations.sh`がエラーを返していた**：`trap ... EXIT`は`failed_log`を参照していました。これは`main()`の`local`で、trapの実行時にはもう存在しません。`set -u`では、これにより`failed_log: unbound variable`が発生し、28件の翻訳が正しかったにもかかわらずスクリプトが1で終了していました。その場合、最もコストの高い再生成直後の段階で`release.sh --auto`（`set -e`）が中断されていました。変数をグローバルにし、trapがその存在を検査するようにしました。副次的な効果として、これまでこのエラーに隠れていた実際の翻訳失敗が、終了時の概要に再び表示されるようになりました。
  - **`REGEN_MODEL`**：`regen_translations.sh`の新しい環境変数。providerのデフォルトを上書きして特定のモデルを強制します。たとえば`REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol`を指定すると、ボリューム重視の`--eco`ではなく、サブスクリプションのクォータで利用できる上位モデルを使って再生成できます。
  - **`regen_translations.sh`**：明示的なopt-inで`REGEN_PROVIDER=codex`を利用可能にしました（ユーザーに知られないままサブスクリプションのクォータを消費しないよう、自動検出は一切行いません）。Codexの更新はローテーション式かつ1回限りであり、並行ジョブがセッション`codex login`を無効化するため、並列処理を開始する前にトークンを1回だけ順番に更新し、同時実行数を4に制限します。
  - **関連するリファクタリング**：`_dispatch_provider_call`の引数を8個から6個に削減しました。第4のブール値をチェーン全体に伝播させる代わりに、provider名を返す`_resolve_provider()`を使用します。`args`よりも明示的なブール値を優先し、最小限の`Namespace`で`translate(..., use_mistral=True)`を呼び出すテストを維持します。
  - **テスト**：新しいファイル`tests/test_codex_provider.py`（48テスト）で、argv、環境変数の除去、前置き禁止契約、サイレント失敗、timeout/killpg、バックオフ、preflight、provider解決、Geminiの推論カスケード、Claudeブロックのフィルタリング、ニュースの複数段落引用を網羅。全体のテスト数は290件になりました。
  - **実環境での検証**：プロジェクトの`README.md`をCodexで**14言語**に翻訳した結果、参照翻訳と完全に同一の構造（14個のコードブロック、24個の見出し、25行の表、13個のHTMLリンク、13個の画像、19個のURL、文字単位で完全に同一のコードブロック、プレースホルダーの残留ゼロ）になりました。`--news`モードの69 KBのニュース記事では、`gpt-5.6-luna`と`gpt-5.6-sol`の出力が、en/ja/arの下流アプリケーションバリデーターをいずれも通過しました。`account/rateLimits/read`で測定した消費量は、`--eco`モードで5時間ウィンドウのカウンターの丸めしきい値未満（0%）に収まりました。

- **1.9.2** ネストした括弧またはFRプレフィックスを含むニュース帰属URL抽出を修正（2026-05-11）：

  - **修正済みのバグ**：`_protect_news_quotes`における帰属URLの抽出では、`re.search(r"\((.+?)\)", attribution)`という正規表現（括弧間の遅延キャプチャ）を使用していました。`(relayé par [@user sur X](https://x.com/.../123))`のような帰属（ネストした括弧：外側の`(`とmarkdown linkの`]()`）では、キャプチャが最初に現れる`)`で停止し、文字列が切り詰められ、FRプレフィックスも含まれていました：`relayé par [@user sur X](https://x.com/.../123`（末尾の`)`なし）。その結果、`_validate_news_post`は翻訳出力内でこの文字列を探して常に失敗していました（理由は2つあり、`)`が切り詰められていることと、「relayé par」が翻訳によって`relayed by`/`weitergeleitet von`/…になることです）。low → medium → high → gpt-5.5の完全なカスケードを通過できませんでした。
  - **修正**：正規表現を`re.search(r"\]\(([^)]+)\)", attribution)`に変更しました。markdown linkの`](url)`のみを対象とし、**純粋なURLだけ**をキャプチャします（FRプレフィックスや切り詰めを含まない）。この不変条件は、翻訳中に`#URL{N}#`プレースホルダーによって保持されます。問題となる2つのパターンに対応しています。
    - `(relayé par [@account sur X](url))` — ネストした括弧
    - `via [@source](url)`または`selon [@author](url)` — 外側の括弧を持たないFRプレフィックス
  - **テスト**：`test_silent_failure.py`の`TestNewsCitationExtraction`クラスに2件追加：
    - `test_extract_attribution_url_with_nested_parens`（Genspark CEO E2Bで再現した正確なケース）
    - `test_extract_attribution_url_with_french_prefix`（`via`を含むバリエーション）
  - **カバレッジの不足**：`check-editorial-coverage.py`は編集上の構文を検証しますが、translatorによる翻訳可能性は検証しません。将来的な改善案（v1.9.2の対象外）は、公開前にリスクのあるパターンを検出するため、dry-runで帰属抽出をシミュレートするチェックを追加することです。

- **1.9.1** 翻訳marker注記内のCTAラベルのi18nを修正（2026-05-10）：

  - **修正済みのバグ**：翻訳済みファイル上部のmarkerバナーにあるCTAリンクの`[Voir le projet sur GitHub ↗]`が、`target_lang`に従わず、すべての対象言語で**フランス語のまま**になっていました。URLとリポジトリのslugを保持するためにPython側で組み立てられており、LLMからは見えないため、翻訳フェーズで修正できませんでした。これはv1.9で`marker`形式を追加して以来の、静かな回帰でした。
  - **修正**：15言語をローカライズされたラベルに対応付ける新しい定数`_VIEW_PROJECT_LABELS`を追加しました。`_translation_note_invariants(target_lang)`と`_assemble_translation_note_paragraphs(phrase, target_lang)`が対象言語を渡すようになりました。未知の言語の場合は`fr`にフォールバックします（安全対策であり、KeyErrorを発生させません）。
  - **テスト**：`test_source_emits_three_paragraphs_repo_title_description_link`を調整（target_lang `ja` → 日本語の期待ラベル）。新しいテストを2件追加：`test_source_link_label_localized_per_target_lang`（ラテン文字、表意文字、アブジャドの各スクリプトを含む7言語でパラメータ化）と`test_source_link_label_falls_back_to_french_for_unknown_target`。合計：`test_translation_note_position.py`内のテストは40件（38件から増加）。
  - **Backward-compat**：デフォルト値`target_lang="fr"`を持つシグネチャにより、`args.target_lang`なしで外部からプログラム的に呼び出している場合も変更なしで動作します。
- **1.9** サイレント失敗の修正＋完全な品質ツールセット＋複数位置対応の翻訳メモ（2026-05-07）：
  - **複数位置対応の翻訳メモ＋「embed card」形式マーカー**：
    - 新しい CLI オプション（追加機能、デフォルトは変更なし → **後方互換性あり**）：
      - `--note_position {top,bottom,both}`（デフォルト：`bottom`）：翻訳ファイルの上部、下部、または両方にメモを配置。
      - `--note_format {legacy,marker}`（デフォルト：`legacy`）：
        - `legacy` は v1.8 の挙動（太字段落 `**…**`）を **byte-for-byte** で厳密に再現。
        - `marker` は、不可視の Markdown リンク参照定義（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）に続いて、**3 段落の blockquote** を出力。これは「GitHub repo embed card」形式のレンダリング用に構造化され、インラインコードのプロジェクト名（`**\`ai-powered-markdown-translator\`\*\*`）、LLM が翻訳した説明、矢印を表示する CTA リンク（`[Voir le projet sur GitHub ↗](URL)`）で構成される。remark プラグインによるビルド時の処理に利用可能（jls42.org のブログ → プラグイン `remark-translation-banner`）。
    - **LLM に送信されない不変値**：リポジトリ名と GitHub URL は説明文の翻訳後に Python 側で組み立てる。LLM が slug `ai-powered-markdown-translator` や `https://github.com/jls42/...` を見ることは決してなく、renderer、slash、scheme が変更されないことを保証。
    - **Frontmatter 対応の挿入**：`top` または `both` モードでは、メモを YAML frontmatter の **終了 `---` ブロックの後**に挿入（Astro Content Collections / gray-matter の安全性を確保）。Helper `_split_frontmatter` はファイル先頭の `---\n…\n---\n` を検出して完全性を保持し、終了 fence のない未完了 frontmatter に対しては **`RuntimeError` を送出**（ファイルは誤った位置にメモを付けて書き込まれる代わりに `failed_files` に戻される）。
    - **モデルの whitelist sanitizer**：`_sanitize_model` は `[A-Za-z0-9._:/-]` に含まれないすべての文字を `_` に置き換え、空の場合は `unknown` にフォールバック。Astro の remark プラグイン側 validator に合わせ、marker 形式を壊す文字（空白、引用符、括弧、コンマなど）を無効化。
    - **内部リファクタリング**：`_append_translation_note`（1 つの巨大な関数）を 7 つの純粋な helper（`_translation_note_invariants`、`_build_translation_note_phrase`、`_assemble_translation_note_paragraphs`、`_build_translation_note_source`、`_sanitize_model`、`_quote_lines`、`_split_frontmatter`、`_build_translation_note_block`、`_compose_with_notes`）に分割。builder と composer を分離（builder は区切りなしの純粋なブロックを返し、composer は位置に応じて `\n\n` を適用）。生成側と source helper は同じ 3 段落 assembler を共有。
    - **`_quote_lines` による空行保持**：各行の先頭に `> ` を付加し、空行を `>` のみに変換。これにより mdast は blockquote 内で、改行を含む 1 つの段落ではなく、3 つの個別段落（タイトル／説明／リンク）として認識可能。
    - **適応型 `_build_translation_note_block`**：LLM が保持した段落数に応じて処理（3 = 完全な card 形式、2 = 文＋リンク、1 = フォールバック）。1 段落のフォールバックでは、Markdown リンク `](` が検出された場合、`<strong>` の周囲での脆弱なレンダリングを避けるため、`**...**` で囲まなくなった。
    - **後方互換性**：`_compose_with_notes` 側の `getattr(args, "note_position", "bottom")` と `getattr(args, "note_format", "legacy")` — これらの属性を持たない Namespace（既存テスト、外部のプログラム呼び出し）も変更なしで引き続き動作。
  - **長い翻訳におけるサイレント失敗の修正**：
    - すべての provider（OpenAI、Mistral、Claude、Gemini）で翻訳後の言語検証を実施：決定論的レイヤー（原文の抜粋が逐語的に再現されているか）＋確率論的レイヤー（`langdetect`）。
    - `finish_reason` / `stop_reason` の whitelist：whitelist 外の状態（truncation、content_filter など）では `RuntimeError` を送出。
    - Claude の `max_tokens`：`4096` → `32768`（16k セグメントでの潜在的な truncation を回避し、FR→JA/ZH/KO/AR/HI の script 横断に余裕を確保）。
    - heading 対応のセグメンテーション：セグメント後半では H2/H3 を優先（各セグメントが意味的に完全なセクションから開始）。
    - エラーを exit code が非ゼロになるまで伝播：`translate_markdown_file` は `success` / `failure` / `skipped` の型付きステータスを返し、少なくとも 1 ファイルが失敗した場合は `main()` `sys.exit(1)`（単一ファイルと batch の両方）。
    - すべての provider に対する空コンテンツ guard、source/output の妥当性比率（≥ 500 chars、< 5% は拒否）、コード placeholder の検証（`#CODEBLOCK`/`#INLINECODE`）、LLM 後の正規化（heading に連結された区切り／リンク）、`BadRequestError` は `reasoning_effort` なしで retry。
    - 依存関係 `langdetect==1.0.9` を追加。
  - **pre-commit の品質ツールセット**（「完全な EurekAI 型」、14 hooks）：
    - Pre-commit：ruff（lint＋format）、shellcheck、prettier（md/yaml/json）、detect-secrets（4 つの API key を保護）、Lizard（CCN ≤ 12）、pre-commit-hooks v5（whitespace、EOF、large-files、shebangs など）。
    - Pre-push：mypy（段階的な lax モード）、Opengrep SAST（translate.py＋scripts/）、pip-audit（初期は reporting モード）、unittest discover（tests/＋scripts/tests/）。
    - `scripts/` 内のローカル wrapper は `./venv/bin/python` を使用。
    - `scripts/audit_verdict.py`：11 個の unittest を備えた pip-audit JSON parser。jls42-astro の parser を Python に移植したもの。
    - 初期の ruff 違反 7 件を修正：B904（raise from）×2、B007（未使用の dirs）、C408（dict literal）、C419（list-comp）、SIM105（contextlib.suppress）、SIM110（any()）。
    - Lizard は一時的に `translate.py` を除外（CCN 21～47 の関数が 4 つあり、リファクタリングを計画中）— scripts/ には strict gate を適用。
  - **SonarCloud＋包括的なカバレッジ**：
    - GitHub Actions workflow `SonarCloud`（sonarcloud.yml＋sonar-project.properties）：push と pull-request のたびに解析、`coverage.xml` による coverage。
    - README 上部に SonarCloud の badge を 11 個追加（Quality Gate、Security/Reliability/Maintainability ratings、Coverage、Vulnerabilities、Bugs、Code Smells、Duplicated Lines、Technical Debt、Lines of Code）。
    - `tests/test_silent_failure.py`（`unittest` stdlib）：サイレント失敗のエラーチェーン 6 つの接続点をカバー。
    - `tests/test_orchestration.py`（＋79 テスト）：`translate.py` の orchestration 層をカバー（`_resolve_*_filename`、`_existing_translation_exists`、`_record_translation_status`、`_write_output_file`、`translate_directory`、`_validate_input_paths`、`_init_*_client`、`_select_provider_client`、`_normalize_collapsed_markdown`、`_cleanup_source_flag`、`_validate_news_flags_*`、`_openai_create_with_fallback` TypeError＋BadRequestError の fallback、o1-series prompt format、`_validate_translation_output` の early-return 分岐）。
    - `scripts/tests/test_audit_verdict.py`：`main()`（stdin/stdout）と、subprocess 経由の `if __name__ == "__main__"` ブロックをカバー。
    - **新規コードの Coverage**：75.5% → 約 98%（translate.py 98%、scripts/audit_verdict.py 97%）。
  - **テスト**：`tests/test_translation_note_position.py` は位置×形式のマトリクス（E2E の `marker+top|bottom|both` と `legacy+top|bottom|both` を含む）、複数行の prefix 付加、byte-for-byte の後方互換性（golden literal）、sanitizer、frontmatter の分割（未終了 fence での raise を含む）、3 段落形式、2 段落の fallback、1 段落＋Markdown リンクの guard、さらにタイトルと URL が LLM に送信されないことを assert する重要な安全策 `TestLLMPayloadExcludesInvariants` をカバー。**190 テスト成功、リグレッション 0 件。**
  - ドキュメント：badge 付きの `README.md`（FR＋14 翻訳）、`CLAUDE.md`（pre-commit workflow＋詳細な CI watch）、28 翻訳を再生成。
- **1.8** `--news` モード＋2026 年モデルの更新（2026-03-17、tag `v1.8`）：
  - デフォルトモデルを更新（2026 年 3 月）：
    - OpenAI 品質：`gpt-5` → `gpt-5.4`
    - OpenAI 経済性：`gpt-5-mini` → `gpt-5.4-mini`
    - Gemini 品質：`gemini-3-pro-preview` → `gemini-3.1-pro-preview`
  - `gpt-5.4`、`gpt-5.4-mini`、`gpt-5.4-nano`（400k）、`gemini-3.1-pro-preview`（1M）の token 上限を追加。
  - `--news` モードの初期実装：`#NEWSQUOTE\d+#` による EN 引用の保護、`LANG_FLAGS` の mapping（15 言語）、対象言語ごとのフラグ管理。
  - 復元前に news placeholder を検証（リグレッション：LLM が placeholder を削除すると、引用のない出力がサイレントに生成されていた）。
  - `regen_translations.sh` スクリプトを portable 化（絶対パス、pwd への依存なし）。
  - README/CHANGELOG の language bar に Français リンクを追加、28 翻訳を再生成。
- **1.7** 新機能：
  - 翻訳時に元のファイル名を保持するオプション `--keep_filename`。
  - API key を自動的に読み込む `.env` ファイルをサポート。
  - **インラインコードの保持**：backtick（`` `...` ``）を翻訳中に保護。
  - system prompt を改善：
    - YAML frontmatter 内の引用符をより適切に処理。
    - template 変数 `{variable}` を保護。
    - 要求されていない翻訳者メモを禁止。
  - jls42.org のブログ移行で 364 ファイルを正常にテスト。
- **1.6** 新機能：
  - 翻訳用 Google Gemini API をサポート（`--use_gemini`）。
  - 2026 年のデフォルトモデルを更新：
    - OpenAI：`gpt-5`（品質）、`gpt-5-mini`（経済性）
    - Claude：`claude-sonnet-4-5`（品質）、`claude-haiku-4-5`（経済性）
    - Gemini：`gemini-3-pro-preview`（品質）、`gemini-3-flash-preview`（経済性）
  - より高速で低コストなモデルを使用する経済モード（`--eco`）。
  - ディレクトリを走査せずに単一ファイルを翻訳（`--file`）。
  - 新しい簡略化された命名パターン：`{base}-{lang}.md`。
  - モデル名を含む従来形式を保持するオプション `--include_model`。
  - token 上限（128k）がデフォルトで設定された未掲載モデルをサポート。
  - README を 14 言語に翻訳。
- **1.5** 改善：
  - **API key とデフォルトモデルを更新：**
    - **OpenAI：** `DEFAULT_MODEL_OPENAI` から `"gpt-4o"` に更新。
    - **Mistral AI：** `DEFAULT_MODEL_MISTRAL` から `"mistral-large-latest"` に更新。
    - **Anthropic の Claude：** `DEFAULT_ANTHROPIC_API_KEY` を追加し、`DEFAULT_MODEL_CLAUDE` から `"claude-3-5-sonnet-20240620"` に更新。
  - **翻訳 prompt を最適化：**
    - 直接翻訳と翻訳メモの prompt を拡充し、明確性と効率を向上。metadata の保持や、特定の formatting 要素に関する詳細な指示を追加。
  - **コードをリファクタリング：**
    - Mistral AI client の初期化において、`MistralClient` を `Mistral` クラスに置換。
    - 可読性と保守性を向上させるため import を再編成。
    - 原文の formatting を保持できるよう、テキストの segmentation と code block の処理を改善。
  - **出力ファイルの管理：**
    - 出力ファイル名における model と言語の順序を反転（例：`f"{base}-{args.target_lang}-{args.model}.md"`）。翻訳の整理と検索を容易にした。
  - **その他の改善：**
    - 不要な空行を削除してコードを整理。
    - script の構造と可読性を向上させるため軽微な調整を実施。
- **1.4** 新機能：
  - 翻訳用 Anthropic の Claude API をサポート。
  - 明確性と効率を高めるため prompt を最適化。
  - コードの保守性を向上させるため軽微な調整を実施。
- **1.3** 改善と新機能：
  - code block の処理を改善。
  - 出力ファイルの処理を改善。
  - 既存ファイルの検出を改善。
  - 翻訳を強制するオプション `--force`。
  - 出力ファイル名における model と言語の順序を反転。
- **1.2** changelog の修正。
- **1.1** Mistral AI API のサポートを追加。
- **1.0** 初期バージョン — OpenAI API をサポート。

**gpt-5.6-lunaを使ってフランス語から日本語に翻訳された記事。**
