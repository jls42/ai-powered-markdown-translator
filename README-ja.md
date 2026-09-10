# AI搭載Markdown翻訳ツール

🌍 [フランス語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [英語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [スペイン語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中国語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [ドイツ語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [韓国語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [アラビア語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [ヒンディー語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [イタリア語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [オランダ語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [ポーランド語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [ポルトガル語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [ルーマニア語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [スウェーデン語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 コード品質</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="品質ゲートの状態"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="セキュリティ評価"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="信頼性評価"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="保守性評価"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="カバレッジ"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="脆弱性"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="バグ"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="コードスメル"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="重複行（%）"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="技術的負債"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="コード行数"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacyバッジ"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

コードブロック、インラインコード、URL、アンカー、表、フロント
マターの構造を維持しながら、Markdownファイルをある言語から
別の言語へ翻訳します。モデルを呼び出す方法は9通りあり、5つのAPI、
従量課金なしの2つのサブスクリプション、2つのルーターに対応し、
各モデルが実際に何を維持できるかを示す公開測定結果もあります。

## 概要

- **9つのプロバイダー経路**：OpenAI、Mistral、Claude、Gemini、Grokの各API、
  従量課金なしのChatGPT（Codex）およびGrokサブスクリプション、
  OpenCode（オープンソース、無料またはローカル）とOpenRouter
  （400以上のモデル）のルーター。
- **トークン欠落による不正な出力を防止**：コードブロック、インラインコード、
  URL、アンカー、引用は、呼び出し前にトークンへ置き換えられ、
  応答後に検証されます。1つでも欠けていれば、ファイルは書き込まれません。
- **長文ドキュメント**：モデルのコンテキストウィンドウに応じて分割します。
- **`--news`モード**：英語の引用を保護し、言語別の
  フラグを処理するため、情報収集記事に適しています。
- **`--eco`モード**：高速で安価なモデルを使用します。
- 上部、下部、または両方に追加できる任意の**翻訳注記**。

## インストール

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10以降が必要です。リポジトリからインストールする場合は、
[コントリビューション](#コントリビューション)を参照してください。

## 設定

キーは優先度の高い順に3か所から読み込まれ、それぞれ前の場所で
未設定だった値だけを補完します。

|     | 場所                                            | 用途                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 環境変数                     | CI、コンテナ、一時的な上書き |
| 2   | 現在のディレクトリ（または親ディレクトリ）の`.env` | プロジェクト固有のキー            |
| 3   | `~/.config/aipmt/.env`                        | 一度設定すれば全体で有効       |

```bash
mkdir -p ~/.config/aipmt
cat > ~/.config/aipmt/.env <<'EOF'
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
OPENROUTER_API_KEY=votre-clé-api-openrouter
EOF
chmod 600 ~/.config/aipmt/.env
```

`GEMINI_API_KEY`は`GOOGLE_API_KEY`の代わりに使用できます。ユーザー
ファイルは`XDG_CONFIG_HOME`（絶対パスのみ）に従い、Windowsでは
`%APPDATA%`に従います。キーがない場合、コマンドは3つの場所を列挙します。

**プロジェクトの`.env`で呼び出し先を変更することはできません。**
提供できるのはキーだけで、接続先ではありません。`_BASE_URL`、
`_API_BASE`、`_ENDPOINT`の変数、プロキシ（`HTTP_PROXY`、
`HTTPS_PROXY`、`ALL_PROXY`）、証明書ストア（`SSL_CERT_FILE`、
`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）、および
`XDG_CONFIG_HOME` / `APPDATA`は警告とともに無視されます。
クローンしたリポジトリがユーザーのキーを別の場所へ送信できてはなりません。
また、このファイルは補間なしで読み込まれるため、`NOM=${OPENAI_API_KEY}`によって
キーが複製されることはありません。これらの変数は環境または
`~/.config/aipmt/.env`に設定してください。

任意の変数：`XAI_BASE_URL`（既定値`https://api.x.ai/v1`）、
`CLAUDE_TIMEOUT`（呼び出しごとの秒数、既定値900）、`CODEX_BIN`、
`CODEX_TIMEOUT`（既定値600）、`GROK_BIN`、`GROK_HOME`
（既定値`~/.grok`）、`GROK_TIMEOUT`（既定値900）、`GROK_TRANSLATE_SANDBOX`、
`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（既定値600）、`OPENROUTER_BASE_URL`
（`https://`が必要）、`OPENROUTER_TIMEOUT`（既定値900）、
`OPENROUTER_PREFLIGHT_TIMEOUT`（既定値30）。それぞれの詳細は、
該当するプロバイダーのセクションに記載されています。

## はじめに

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md`をスペイン語へ翻訳すると、`--target_dir`に
`document-es.md`が生成され、`--include_model`を指定した場合は
`document-es-gpt-5.6-terra.md`になります。拡張子は常に`.md`になります。
つまり`article.mdx`は`article-en.md`になります。ただし、
`--keep_filename`を指定すると元のファイル名が維持されます。
既存の翻訳は、`--force`を指定しない限りスキップされます。

終了コード：すべて成功またはスキップされた場合は`0`、
失敗したファイルが残っている場合は`1`（標準エラー出力に一覧を表示）、
設定に問題がある場合は`2`です。
書き込み処理自体が失敗した場合も、失敗したファイルが書き込まれることはありません。
内容はいったん隣接する場所へ書き込まれ、その後名前が変更されます。
再実行するだけで十分です。

## どのモデルを選ぶべきか

2つの実際のドキュメントを各モデルで同じ14言語へ翻訳して測定しました。
**数値は14言語のうち、翻訳が書き込まれ、かつソースとの差異が
一切なかった言語数です。**

| モデル               | アクセス方法                 | 高密度な情報収集記事 | このREADME    | 相違点と該当言語数                                                                                             |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | Google APIキー                    | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語：太字の単語が1つ多い（ja）                                                                                         |
| **GPT-5.6 Sol**      | ChatGPTサブスクリプションまたはOpenAIキー | ✅ 14/14                | ⚠️ 12/14     | 14言語中2言語：太字の単語が1つ少ない（ar、ja）                                                                                   |
| **GLM-5.2**          | OpenRouterキー                    | ✅ 14/14                | ⚠️ 11/14     | 14言語中3言語：太字の単語が1つ少ない（hi、ja、ko）                                                                               |
| Claude Sonnet 5      | Anthropic APIキー                 | ⚠️ 11/14                | ⚠️ 12/14     | 記事では3言語：コードブロックが出現（es、de、hi）。このREADMEでは2言語：マークアップのないリンク（sv）、太字の単語（zh） |
| Qwen 3.7 Flash       | OpenRouterキー                    | ❌ 8/14                 | ⚠️ 10/14     | 記事では1言語が拒否され、ほかの5言語に差異。このREADMEでは約40語が`code`になった（ar）                       |
| Grok 4.6             | Grokサブスクリプション                   | ❌ 8/14                 | 未評価     | インラインコードとURLが返されなかったため、14言語中5言語が拒否。オランダ語では全体に差異                                  |
| GPT-OSS 20B          | ローカルモデル（Ollama）             | ❌ 7/14                 | 再測定なし | 14言語中4言語が拒否：モデルがフランス語の文章を残していたため、ガードによって停止                                     |
| MiMo v2.5（無料）  | OpenCode Zen、アカウント不要         | ❌ 11/14                | 再測定なし | 1言語が拒否。ポーランド語では1セクションが欠落                                                                                     |
| Mistral Large        | Mistral APIキー                   | ❌ 5/14                 | ❌ 1/14      | **セクション全体が消失**：記事では1言語（hi）、このREADMEでは3言語（ar、hi、ko）。さらに記事では3言語が拒否   |
| DeepSeek V4 Flash    | OpenRouterキー                    | ❌ 3/14                 | 再測定なし | 14言語中10言語が拒否。1言語あたり37分                                                                                    |

|     | 記号の意味                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14言語すべてが翻訳され、ソースとの差異が一切ない                                                                                                                                       |
| ⚠️  | 14言語すべてが翻訳され、相違点は**マークアップ**のみ。太字の単語、`code`、角括弧が失われたリンクなど。テキスト、URL、コードブロック、セクションの欠落はない |
| ❌  | 少なくとも1言語を翻訳できず、ファイルが拒否されて書き込まれなかった、**または**書き込まれたファイルに内容の欠落がある                                                                      |

要点：

- **拒否された翻訳は、壊れた翻訳ではありません。** 応答でトークンが
  欠けている場合、ファイルは書き込まれず、その言語は拒否として数えられます。
  記事でGrokに起きたのがこれです。非ラテン文字を使う5言語では、
  最初のセグメントから4つのインラインコードと3つのURLが失われました。
- **このセーフティネットは、見出し、表、フロントマター、テキストには
  対応していません。** モデルがセクションを削除しても、ツールは
  何事もなくファイルを書き込みます。Mistralがその例です。これらの要素は
  トークンに置き換えられず、現在のガードでも検査されません。
  `scripts/compare_structure.py`は欠落したセクションを検出しますが、事後検出です。
- **GrokにはこのREADMEの評価がありません**：CLIセッションが12言語の
  処理後に期限切れとなり、そのうち11言語には差異がありませんでした。
  中断された測定には評価を付けません。
- **言語よりもドキュメントの密度が重要です。** Grokは一般的な
  READMEでは維持できますが、リンクの多い記事では破綻し、
  オランダ語でも同様です。

日付とドキュメント：「このREADME」列は、2026年9月9日にこのファイルの
固定リビジョン（785行、インラインコード285個、表89行）で測定され、
その後修正されています。「高密度な情報収集記事」列は、589行の記事を
対象に9月4日と5日に実施した測定結果です。ただしGrokの行は、
同じ情報収集記事の別版を使って9月9日に再測定したものです。
完全な表、所要時間、手順は
[詳細な測定結果](#詳細な計測結果)にあります。

## すべてのオプション

| オプション                   | 説明                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 翻訳する単一のMarkdownファイル（`--source_dir`の代替）                                             |
| `--source_dir`           | Markdownファイルを含むソースディレクトリ（既定値：`content/posts`）                                   |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ（既定値：`traductions_en`）                                    |
| `--source_lang`          | 翻訳元の言語（既定値：`fr`）                                                                                  |
| `--target_lang`          | 翻訳先の言語（既定値：`en`）                                                                                   |
| `--model`                | 使用する特定のモデル                                                                                  |
| `--eco`                  | 低価格モデルを使用                                                                              |
| `--use_mistral`          | Mistral AI APIを使用                                                                                     |
| `--use_claude`           | Claude APIを使用                                                                                         |
| `--use_gemini`           | Gemini APIを使用                                                                                         |
| `--use_grok`             | xAI API（Grok）を使用。`XAI_API_KEY`が必要                                                           |
| `--use_codex`            | ChatGPTサブスクリプションのクォータでCodex CLIを使用                                                    |
| `--use_grok_cli`         | GrokサブスクリプションのクォータでGrok CLIを使用                                                        |
| `--use_opencode`         | OpenCodeで設定されたプロバイダーにOpenCode（オープンソース）を使用。`--model provider/modèle`が必要 |
| `--use_openrouter`       | OpenRouterを使用。`OPENROUTER_API_KEY`と`--model fournisseur/modèle`が必要                          |
| `--force`                | 再翻訳を強制                                                                                       |
| `--keep_filename`        | 元のファイル名を維持                                                                          |
| `--news`                 | ニュースモード：英語の引用を保護し、言語別のフラグを処理                                      |
| `--add_translation_note` | 翻訳注記を追加                                                                                |
| `--note_position`        | 注記の位置：`top`、`bottom`（既定値）、または`both`                                                     |
| `--note_format`          | 注記の形式：`legacy`（既定値、太字の段落）または`marker`                                            |
| `--include_model`        | 出力ファイルにモデル名を含める                                                            |
| `--reasoning_effort`     | GPT-5.xの推論量：`none`/`low`/`medium`/`high`/`xhigh`                                         |

8つの`--use_*`フラグは相互排他的であり、2つを組み合わせると
拒否されます。

## プロバイダー

### API経由：OpenAI、Mistral、Claude、Gemini、Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco`を指定すると、各プロバイダーの低価格モデルへ切り替わります。

| プロバイダー   | 高品質（既定値）                                      | 低価格（`--eco`）      |
| ---------- | ----------------------------------------------------- | ------------------------- |
| OpenAI     | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral    | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini     | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex      | `gpt-5.6-sol`（`--model`で`terra`と`luna`も指定可能） | `gpt-5.6-luna`            |
| Grok API   | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI   | `grok-4.6`                                            | `grok-4.5`                |
| OpenCode   | `--model provider/modèle`が必須                 | 同じ。`--eco`は効果なし |
| OpenRouter | `--model fournisseur/modèle`が必須              | 同じ。`--eco`は効果なし |
### ChatGPT サブスクリプションの場合：`--use_codex`

公式 Codex CLI を操作します。翻訳は ChatGPT サブスクリプションの利用枠から差し引かれ、
API キーも従量課金も必要ありません。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- バイナリは `CODEX_BIN`、次に `PATH`、その後に package
  `openai-codex-cli-bin` の順で検索されます。`~/.codex/auth.json` は一切読み込まれません。
- `OPENAI_API_KEY` と `CODEX_API_KEY` はサブプロセスの環境から削除されます。
  キーが存在していても API に切り替わることはありません。
- 各セグメントは、5 時間枠の「メッセージ」を最低 1 件消費します。検証に失敗して
  再試行される場合は 2 件です。OpenAI は目安として、Plus プランでは
  `gpt-5.6-luna`（`--eco`）が 250～2,000 メッセージ/5 時間、
  `gpt-5.6-sol` が 10～100 メッセージ/5 時間と案内しています。
- `--model gpt-5.6-terra` と `--model gpt-5.6-luna` もサブスクリプションを経由します。
  アカウントで利用できないモデルを指定すると、400「model is not supported when
  using Codex with a ChatGPT account」が返されます。
- API より低速で、文書が長くなるほど差が広がります。この README では、
  `gpt-5.6-sol` の言語あたりの中央値が 6 分 46 秒だったのに対し、
  `gemini-3.7-flash` は 36 秒でした。
- CI（`CI` または `GITHUB_ACTIONS` が定義済み）では拒否されます。
  サブスクリプションは個人のセッションファイルで認証するため、共有 runner に
  置くべきではありません。
- 変数：`CODEX_BIN`、`CODEX_TIMEOUT`（セグメントあたりの秒数、デフォルト 600）。

### Grok サブスクリプションの場合：`--use_grok_cli`

SuperGrok または X Premium+ のサブスクリプションで、公式 Grok Build CLI を使う
同様の仕組みです。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **隔離は Codex より弱いです。** Grok の OS sandbox は、多くの最近の Linux 環境
  （AppArmor、コンテナ runtime socket）では適用されず、適用できない profile は
  警告なしに非隔離状態で起動します。そのため、この script はデフォルトでは
  profile を要求せず、その旨を通知したうえで、CLI の `--deny` 規則と、
  その catch-all である `*` に依存します。これは保護を黙って解除する
  のではなく、起動自体を拒否する唯一の層です。`GROK_TRANSLATE_SANDBOX=read-only` は OS sandbox を
  必須にし、マシンがそれに対応できない場合は起動に失敗します。
- 利用枠は週単位で、Chat、Imagine、Voice と共有されますが、確認するコマンドは
  ありません。バッチ処理が何の通知もなく会話用の利用枠を消費する可能性があります。
- 変数：`GROK_BIN`、`GROK_HOME`（CLI のディレクトリ、デフォルト
  `~/.grok`）、`GROK_TIMEOUT`（デフォルト 900）、`GROK_TRANSLATE_SANDBOX`。

### 任意の provider へ：`--use_opencode`

[OpenCode](https://opencode.ai) は、内部で設定された provider に処理を振り分けるオープンソース
（MIT）の code agent です。API キー、サブスクリプション、OpenCode Zen gateway
（アカウント不要の無料モデル）、またはローカルモデルを利用できます。ここでは Zen と
Ollama の 2 経路について、最初から最後まで計測しています。

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur

# gratuit, sans compte ni clé — données utilisables pour l'entraînement
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en
# local, hors ligne
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de
# sur un abonnement déjà payé
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

`--model` は必須です。指定しない場合、OpenCode はやり取りが学習に利用される
可能性のある無料モデルへフォールバックしますが、この選択を利用者に代わって行うことは
ありません。

呼び出しごとの隔離：

- 利用者自身の設定より優先される inline configuration により、すべての tool を
  拒否する（`permission: { "*": "deny" }`）agent `aipmt` を定義し、session sharing を
  無効化して `--pure` を使用し、`--auto` は決して使用しません。
- 使い捨ての空の作業ディレクトリを使用し、`OPENCODE_DISABLE_PROJECT_CONFIG` と `OPENCODE_DISABLE_CLAUDE_CODE` を
  設定します。これらがないと、OpenCode は現在のディレクトリの
  `AGENTS.md` と `~/.claude/CLAUDE.md` を prompt に挿入します。グローバルな
  `~/.config/opencode/AGENTS.md` は引き続き挿入され、OpenCode では除外できません。
- 出力契約は、終了 code 0、`error` event なし、tool call なし、最後の step が
  `stop`、空でないテキスト、かつ agent `aipmt` が実際に読み込まれて
  いることです。不明な `--agent` を指定しても OpenCode は失敗せず、警告なしに
  coding agent へフォールバックします。
- `OPENCODE_API_KEY`、すなわち OpenCode 自体のキーを除き、`aipmt` のキーは
  一切渡されません。provider は `aipmt` の `.env` ではなく、
  OpenCode 側で設定します。

注意事項：

- Zen の無料モデルは頻繁に変更され、制限も文書化されておらず、やり取りが学習に
  利用される可能性があります。公開文書には使えても、非公開コンテンツには適しません。
- セグメントは最大 16,000 文字になるため、ローカルモデルには最低 16 k tokens の
  context が必要です。Ollama では 4,096 に設定されていることが多いため、
  `PARAMETER num_ctx 32768` を指定した `Modelfile` を使用してください。
- `--eco` は効果がありません。`--reasoning_effort` は OpenCode の
  `--variant` としてそのまま渡されます。
- OpenCode は各 session を `~/.local/share/opencode/` に記録します。
- 変数：`OPENCODE_BIN`（未指定の場合は `PATH`、次に
  `~/.opencode/bin/opencode`）、`OPENCODE_TIMEOUT`（セグメントあたりの秒数、デフォルト 600）。
  `OPENCODE_CONFIG` はそのまま OpenCode に渡されます。

`~/.config/opencode/opencode.json` で Ollama 経由のローカルモデルを使う例：

```bash
ollama pull gpt-oss:20b
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": { "baseURL": "http://127.0.0.1:11434/v1" },
      "models": {
        "gpt-oss-20b-32k": {
          "name": "gpt-oss 20B (32k, sans réflexion)",
          "limit": { "context": 32768, "output": 8192 },
          "options": { "reasoningEffort": "none" }
        }
      }
    }
  }
}
```

`reasoningEffort: "none"` は、これらのモデルで Ollama がデフォルトで有効にし、
Modelfile では無効化できない推論を停止します。6 語の文で計測したところ、
このオプションなしでは推論に 919 tokens と 68 秒を要しましたが、ありでは
9 tokens でした。

### 400 を超えるモデルへ：`--use_openrouter`

OpenRouter は、1 つのクレジットから従量課金され、第三者がホストするモデルへ
処理を振り分ける router です。ここでは他のどの provider も提供していない中国の
オープンモデルも含まれます。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` は必須です。課金前に実行される preflight により、routing 固有の
2 つの点を処理します。

- **同じモデルが、上限の異なる数十の host から提供されます**。`z-ai/glm-5.3-flash` では
  23 の host があり、そのうち 1 つは出力が 2,048 tokens に制限されています。
  preflight は `/api/v1/models/{modèle}/endpoints` を読み取り、出力が 8,000 tokens 未満の host または
  状態が低下している host を除外し、残りを `allow_fallbacks: false` で固定します。
- **推論は出力料金で課金されます**。`z-ai/glm-5.2` の「OK」という応答では、
  出力 2 tokens に対して推論は 107 tokens でした。推論はデフォルトで無効です。
  推論を必須とするモデルには、そのモデルが受け付ける最低限の effort を指定します。
  カタログのデフォルトでは、翻訳が終わる前に出力上限へ達する可能性があるためです。
  `--reasoning_effort` が引き続き優先されます。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- context window はカタログから取得します。16,400 tokens 未満のモデルは呼び出し前に
  拒否されます。prompt とセグメントに 8,400、出力に最低 8,000 が必要です。
- カタログに存在しない slug、アクセス不能なカタログ、または上限を満たす host が
  存在しない場合、コマンドは停止します。
- `finish_reason=length` で出力が空の場合、truncation ではなく、推論によって予算が
  消費されたことを意味します。メッセージでは両者を区別します。
- `--eco` は効果がありません。
- 変数：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>）、
  `OPENROUTER_BASE_URL`（デフォルト `https://openrouter.ai/api/v1`、`https://` が必須）、
  `OPENROUTER_TIMEOUT`（デフォルト 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（デフォルト 30）。

### 翻訳注記

`--add_translation_note` は、`bottom`（デフォルト）、`top`
（front matter の後）、または `both`（`--note_position`）の位置に、
`legacy`（太字の段落、デフォルト）または `marker`
（`--note_format`）形式の注記を追加します。`marker` 形式は、
非表示の Markdown reference definition
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`
と、それに続く太字の引用です。GitHub 上で読めるほか、build 時に remark plugin で
利用できます。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 詳細な計測結果

すべての計測は `aipmt` で実際に実行した、en、es、de、it、pt、nl、pl、sv、
ro、ja、ko、zh、ar、hi の 14 言語への翻訳です。**書き込み済み**は guard を通過した
ファイル数、**差異なし**は `scripts/compare_structure.py` が何も検出しなかったファイル数です。
section、subtitle、link、異なる URL、code block、inline code、table row、
blockquote、太字語の数が同じであることを示します。

「差異なし」は「何も検出されなかった」という意味であり、「同一」という意味では
ありません。比較機能は要素の内容を読まずに数だけを比較します。レベル 4 の heading の
削除、inline code のテキストの置換、flag の入れ替わりは検出せず、言語の正しさも
判定しません。

### 情報量の多い技術動向記事、`--news` mode

[jls42.org の AI 技術動向](https://jls42.org/fr/news)のある版：
589 行、140 links、21 sections、保護された英語の引用 3 件。2026 年 9 月 4 日と
5 日に実施した campaign です。

| モデル                            | アクセス              | 書き込み済み | 差異なし     | 言語あたりの中央値 |
| --------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                | Google API         | 14/14   | ✅ **14/14** | 1 分 18 秒     |
| `gpt-5.6-sol` (`--use_codex`)     | ChatGPT サブスクリプション | 14/14   | ✅ **14/14** | 11 分 28 秒    |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14   | ✅ **14/14** | 5 分 37 秒     |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14   | ✅ **14/14** | 26 分 23 秒    |
| `claude-sonnet-5`                 | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 分 31 秒     |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 分 27 秒     |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14   | ❌ 8/14      | 10 分 09 秒    |
| `ollama/gpt-oss-20b-32k`          | ローカル              | 10/14   | ❌ 7/14      | 12 分 39 秒    |
| `mistral-large-latest`            | Mistral API        | 11/14   | ❌ 5/14      | 5 分 32 秒     |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14    | ❌ 3/14      | 37 分 27 秒    |
| `grok-4.6` (`--use_grok_cli`)     | Grok サブスクリプション    | 1/14    | ❌ 1/14      | 23 分 11 秒    |

Grok は 9 月 9 日に、同じ技術動向記事の別版（356 行）で再計測されました。14 言語中
9 言語が書き込まれ、そのうち 8 言語は差異なしでした。冒頭の表にはこの数値を掲載して
います。中断した 3 件の campaign は掲載していません。`qwen3.5-27b`（9 言語）と
`kimi-k2.6`（4 言語）はクレジット不足、`z-ai/glm-5.3-flash` の 2 件の失敗は
provider が現在修正中の推論設定が原因でした。OpenRouter の行は
`--use_openrouter` より前に、router のデフォルト設定で計測しました。提供時の provider
を使って再計測した `z-ai/glm-5.2` も、同じく 14/14 でした。数値は 9 月 10 日に
現在の比較機能で再計算されています。`qwen3.8-flash` と `qwen3.7-flash` は、
初回公開時よりそれぞれ 1 言語増え、その他は変更ありません。

### このプロジェクトの README、標準 Markdown

2026 年 9 月 9 日時点の固定 revision：785 行、285 inline codes、40 block fences、
89 table rows。4 件の翻訳を並列実行しました。

| モデル                        | 書き込み済み | 差異なし | 言語あたりの中央値 | 相違点                                                                   |
| ----------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.7-flash`            | 14/14   | ⚠️ 13/14   | 36 秒          | 太字語 1 個（ja）                                                        |
| `claude-sonnet-5`             | 14/14   | ⚠️ 12/14   | 2 分 56 秒     | link 1 件（sv）、太字語 1 個（zh）                                      |
| `gpt-5.6-sol` (`--use_codex`) | 14/14   | ⚠️ 12/14   | 6 分 46 秒     | 太字語 1 個（ar、ja）                                                    |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14   | ⚠️ 11/14   | 2 分 34 秒     | 太字語 1 個（hi、ja、ko）                                               |
| `qwen/qwen3.7-flash`          | 14/14   | ⚠️ 10/14   | 2 分 17 秒     | アラビア語で inline code を 40 個追加、太字（hi、ja、ko）               |
| `mistral-large-latest`        | 14/14   | ❌ 1/14    | 2 分 44 秒     | section 1 件の欠落（ar、hi、ko）、code block の追加（ja、ko、ro、zh）   |

中断した 2 件の campaign は掲載していません。Grok は 12 言語の後に CLI session が
期限切れとなりました（うち 11 言語は差異なし）。`qwen3.8-flash` は 2 言語の後に
host から HTTP 429 が返されました。`opencode/mimo-v2.5-free` と `ollama/gpt-oss-20b-32k` はこの
revision では再計測していません。277 行短い 9 月 4 日と 5 日の revision では、
それぞれ 14 言語中 9 言語を書き込み、差異なしはそれぞれ 7 言語と 1 言語でした。

### 有名プロジェクトの 4 つの README

FastAPI、Ollama、tldr-pages、Vue.js を GitHub 上の状態のまま使用しました。
直前の 2 文書より簡単な文書です。この campaign は苦戦したモデルを対象とし、
Gemini を比較基準として使用しました。

| モデル                    | 対象範囲                   | 書き込み済み | 差異なし     |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 プロジェクト × 14 言語     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 プロジェクト × 14 言語     | 55/56   | ❌ 47/56     |
| `grok-4.6` (サブスクリプション)   | 4 プロジェクト × ar、hi、ja、zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 プロジェクト × ar、hi、ja、zh | 15/16   | ❌ 9/16      |

### この計測結果が意味しないこと

- **網羅的なランキングではありません**：OpenRouter だけでも 400 を超えるモデルを
  提供しており、計測したのは約 15 モデルです。
- **所要時間は目安です**：campaign によって 3～6 件の翻訳を並列実行しており、
  provider のスループットは時間帯によって変動します。
- **特定時点での観測結果です**：同じ名前でもモデルは変化し、利用者の文書は
  私たちの文書とは異なります。

利用者自身の文書で再計測するには、ファイルの固定コピーに対して次を実行します。

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## コントリビューション

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

両方の行が必要です。`pip install -e .` がない場合、`python -m aipmt` は
`No module named aipmt` を返します。

品質管理用の tool は任意ですが、推奨します。

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

repository の 28 翻訳（README と CHANGELOG、それぞれ 14 言語）は、
`./regen_translations.sh --force` で再生成できます。デフォルトでは ChatGPT サブスクリプション上の
Codex と `gpt-5.6-sol` を使用し、4 件を並列実行します。`REGEN_PROVIDER` と
`REGEN_MODEL` で経路を変更できます。課金される API（`openai`、
`gemini`、`grok`、`openrouter`）は `REGEN_ALLOW_PAID_API=1` がないと
拒否されます。`REGEN_JOB_TIMEOUT` は各 job の上限時間を設定します（600 秒、Codex は
1,800 秒）。tool の詳細は `CLAUDE.md` にあります。

## この script を使用しているプロジェクト

- **[jls42.org](https://jls42.org)** — 15 言語で公開されている個人 blog です。
  [日刊 AI 技術動向](https://jls42.org/fr/news)はこの tool で毎日翻訳されており、
  上記の計測で基準文書として使用されています。

## 作者

Julien LE SAUX
メール：contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。[LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)を参照してください。

## 免責事項

このプログラムは、GPL v3 の第 15 条および第 16 条の規定に基づき、
**いかなる保証もなく**配布されます。「現状のまま」提供され、商品性または特定目的への
適合性を含む保証は一切なく、作者はその使用によって生じた損害について責任を負いません。
この要約よりライセンス本文が優先されます。

- **公開前に見直してください。** 保護対象は code block、inline code、URL、anchor、
  `--news` mode の引用です。heading、table、front matter、文意は保護されません。
- **文書は選択した provider に送信されます**。その利用規約とデータポリシーが
  適用されます。一部の無料モデルでは、やり取りが学習に再利用される可能性があります。
  マシンの外部へデータを一切送信しない唯一の方法は、ローカルモデルです。
- **API 呼び出しは課金されます。** このプログラムは支出額を制限しません。
  長い文書、失敗後の再試行、または推論量の多いモデルは、より多くの費用がかかります。
- **公開されている計測結果は特定時点での観測結果**であり、保証ではありません。

記載されている製品名および会社名は、それぞれの所有者に帰属します。
このプロジェクトはいずれの所有者とも提携していません。

**gpt-5.6-solを使用してフランス語から日本語に翻訳された記事。**
