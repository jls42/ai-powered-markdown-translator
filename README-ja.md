# AIパワード Markdown翻訳ツール

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 コード品質</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Quality Gate Status"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Security Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Reliability Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Maintainability Rating"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Coverage"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilities"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Duplicated Lines (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technical Debt"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Lines of Code"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy Badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Markdownファイルをある言語から別の言語へと構造を維持しながら翻訳します：コードブロック、インラインコード、URL、アンカー、テーブル、フロントマター。モデルを呼び出す10種類の方法（5つのAPI、従量課金なしの3つのサブスクリプション、2つのルーター）と、各モデルが実際に何を維持できるかの公開測定結果。

## 概要

- **10種類のプロバイダーパス**：OpenAI、Mistral、Claude、Gemini、GrokのAPI；従量課金なしのChatGPT（Codex）、Grok、Google（Antigravity）サブスクリプション；OpenCode（オープンソース、無料またはローカル）およびOpenRouter（400以上のモデル）ルーター。
- **トークン欠落による破損なし**：コードブロック、インラインコード、URL、アンカー、引用は呼び出し前にトークンへ置き換えられ、復帰時に検証されます。1つでも欠けている場合、ファイルは書き込まれません。
- **長文ドキュメント**：モデルのコンテキストウィンドウに応じた分割処理。
- **`--news`モード**：英語の引用を保護し、言語ごとに国旗を処理（キュレーション／ニュース記事向け）。
- **`--eco`モード**：高速かつ低コストなモデル。
- **翻訳注記**（オプション）：上部、下部、またはその両方に配置可能。

## インストール

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10以降。リポジトリからインストールする場合は、[貢献方法](#貢献する)を参照してください。

## 設定

キーは優先度の高い順に3つの場所から読み込まれ、前の場所で設定されていない項目のみを後続の場所で補完します。

|     | 場所                                          | 用途                                  |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 環境変数                                      | CI、コンテナ、一時的な上書き          |
| 2   | カレントディレクトリ（または親ディレクトリ）の`.env` | プロジェクト固有のキー                |
| 3   | `~/.config/aipmt/.env`                        | 一度設定すれば全体に適用              |

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

`GOOGLE_API_KEY`の代わりに`GEMINI_API_KEY`も受け付けられます。ユーザー設定ファイルは`XDG_CONFIG_HOME`（絶対パスのみ）に従い、Windowsでは`%APPDATA%`に従います。キーが設定されていない場合、コマンドはこれら3つの場所を一覧表示します。

**プロジェクトの`.env`で呼び出し先をリダイレクトしたり、実行するプログラムを選択したりすることはできません。** 提供できるのはキーのみであり、接続先やバイナリを指定することはできません。`_BASE_URL`、`_API_BASE`, `_ENDPOINT`、`_BIN`で始まる変数（`CODEX_BIN`、`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`）、`GROK_HOME`、プロキシ（`HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY`）、証明書ストア（`SSL_CERT_FILE`、`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）、および`XDG_CONFIG_HOME` / `APPDATA`は警告とともに無視されます。クローンしたリポジトリによってキーを傍受されたり、初回の翻訳時に悪意あるプログラムを実行させられたりするのを防ぐためです。また、このファイルは変数展開なしで読み込まれるため、`NOM=${OPENAI_API_KEY}`によってキーがコピーされることもありません。これらの変数は環境変数または`~/.config/aipmt/.env`に設定してください。

オプションの変数：`XAI_BASE_URL`（デフォルト `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（1呼び出しあたりの秒数、デフォルト 900）、`CODEX_BIN`、`CODEX_TIMEOUT`（デフォルト 600）、`GROK_BIN`、`GROK_HOME`（デフォルト `~/.grok`）、`GROK_TIMEOUT`（デフォルト 900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（デフォルト 900）、`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（デフォルト 600）、`OPENROUTER_BASE_URL`（`https://`が必要）、`OPENROUTER_TIMEOUT`（デフォルト 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（デフォルト 30）。各変数の詳細は各プロバイダーのセクションで説明します。

## クイックスタート

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md`をスペイン語に翻訳すると、`--target_dir`内に`document-es.md`が生成されます。`--include_model`を指定した場合は`document-es-gpt-5.6-terra.md`となります。拡張子は元の名前を保持する`--keep_filename`を使用しない限り、常に`.md`になります（例：`article.mdx`は`article-en.md`になります）。既存の翻訳ファイルがある場合、`--force`を指定しない限りスキップされます。

終了コード：すべて成功またはスキップされた場合は`0`、失敗したファイルが残っている場合は`1`（標準エラー出力に一覧表示）、設定に問題がある場合は`2`。失敗したファイルが書き込まれることはありません。書き込み処理自体が失敗した場合でも、一時ファイルに書き出されてからリネームされるため安全です。再実行するだけで済みます。

## どのモデルを選ぶべきか

2つの実際のドキュメントを使用し、各モデルで同一の14言語に翻訳して測定しました。**数値は、14言語中、翻訳が出力され、かつ原文からの差異が一切なかった言語の数です。**

| モデル               | アクセス方法                      | 高密度のキュレーション記事 | このREADME   | 差異の内容と該当言語数                                                                                                                |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.8 Flash** | Googleサブスクリプション（Antigravity） | ✅ 14/14                | ✅ 14/14     | 両ドキュメントとも差異なし                                                                                                            |
| **Gemini 3.7 Flash** | Google APIキー                    | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語：太字が1単語多い（ja）                                                                                                  |
| **Gemini 3.7 Flash** | Googleサブスクリプション（Antigravity） | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語：太字が1単語少ない（ko）                                                                                                |
| **GPT-5.6 Sol**      | ChatGPTサブスクリプション、またはOpenAIキー | ✅ 14/14                | ⚠️ 12/14     | 14言語中2言語：太字が1単語少ない（ar、ja）                                                                                           |
| **GLM-5.2**          | OpenRouterキー                    | ✅ 14/14                | ⚠️ 11/14     | 14言語中3言語：太字が1単語少ない（hi、ja、ko）                                                                                        |
| Claude Sonnet 5      | Anthropic APIキー                 | ⚠️ 11/14                | ⚠️ 12/14     | 記事で3言語：余分なコードブロックが発生（es、de、hi）；このREADMEで2言語：リンクマークアップの欠落（sv）、太字が1単語（zh）         |
| Qwen 3.7 Flash       | OpenRouterキー                    | ❌ 8/14                 | ⚠️ 10/14     | 記事で1言語が拒絶、他5言語で乖離；このREADMEで約40単語が`code`化（ar）                                                        |
| Grok 4.6             | Grokサブスクリプション            | ❌ 8/14                 | 評価なし     | 14言語中5言語がインラインコードとURLの欠落により拒絶；オランダ語は全面的に乖離                                                        |
| GPT-OSS 20B          | ローカルモデル（Ollama）          | ❌ 7/14                 | 未再測定     | 14言語中4言語が拒絶：モデルがフランス語の文章を残したためガードにより遮断                                                             |
| MiMo v2.5（無料）    | OpenCode Zen、アカウント不要      | ❌ 11/14                | 未再測定     | 1言語が拒絶；ポーランド語で1セクションが消失                                                                                          |
| Mistral Large        | Mistral APIキー                   | ❌ 5/14                 | ❌ 1/14      | **セクション全体が消失**：記事で1言語（hi）、このREADMEで3言語（ar、hi、ko）— さらに記事で3言語が拒絶                                |
| DeepSeek V4 Flash    | OpenRouterキー                    | ❌ 3/14                 | 未再測定     | 14言語中10言語が拒絶；1言語あたり37分                                                                                                 |

|     | 記号の意味                                                                                                                                                                                            |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14言語すべてが翻訳され、原文との差異が一切ない                                                                                                                                                        |
| ⚠️  | 14言語すべてが翻訳されたが、差異は**マークアップ**のみ（太字の単語、`code`、角括弧が外れたリンクなど）。テキスト、URL、コードブロック、セクションの欠落は一切なし                            |
| ❌  | 少なくとも1言語が翻訳できなかった（ファイルが拒絶され書き込まれなかった）、**または**書き込まれたファイル内にコンテンツの欠落がある                                                                 |

留意すべきポイント：

- **拒絶された翻訳は、破損した翻訳ではありません。** 復帰時にトークンが欠落していた場合、ファイルは書き込まれず、その言語は拒絶としてカウントされます。これは記事の翻訳時にGrokで発生した現象です。5つの非ラテン文字言語において、第1セグメントから4つのインラインコードと3つのURLが失われました。
- **この安全ネットは、見出し、テーブル、フロントマター、本文テキストは対象外です。** セクションを丸ごと削除するモデルがあっても、ツールはそのままファイルを出力してしまいます（Mistralの事例）。これらはトークンによる置換ができず、現在のガードでは検査されません。`scripts/compare_structure.py`によって消失したセクションを検出できますが、事後検証となります。
- **このREADMEにおけるGrokの評価はありません**：12言語（うち11言語は差異なし）を処理した時点でCLIセッションが期限切れとなったためです。中断されたテストは評価対象外としています。
- **言語よりもドキュメントの密度が大きく影響します。** Grokは通常のREADMEであれば問題ありませんが、リンクが密集した記事では、オランダ語であっても破綻します。

測定日時と対象ドキュメント：「このREADME」列は、2026年9月9日に本ファイルのスナップショット版（785行、インラインコード285個、テーブル行89行、その後改訂あり）で測定されました。ただしAntigravityの2行については、9月26日に1.14.0とともに公開された短縮版（600行、インラインコード257個、テーブル行85行）で測定されています。「高密度のキュレーション記事」列は、9月4〜5日に実施された589行の記事に対するテスト結果です（Grokの行は9月9日に同キュレーションの別版で再測定、Antigravityの2行は9月26日に同一記事で測定）。
完全な表、所要時間、測定手順については[詳細な測定結果](#詳細な測定結果)を参照してください。

## すべてのオプション

| Option                   | 説明                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 翻訳する単一のMarkdownファイル（`--source_dir`の代替）                                                         |
| `--source_dir`           | Markdownファイルが含まれるソースディレクトリ（デフォルト: `content/posts`）                                   |
| `--target_dir`           | 翻訳済みファイルの出力先ディレクトリ（デフォルト: `traductions_en`）                                            |
| `--source_lang`          | ソース言語（デフォルト: `fr`）                                                                      |
| `--target_lang`          | ターゲット言語（デフォルト: `en`）                                                                  |
| `--model`                | 使用する特定のモデル                                                                                          |
| `--eco`                  | エコノミーモデルを使用                                                                                        |
| `--use_mistral`          | Mistral AI APIを使用                                                                                          |
| `--use_claude`           | Claude APIを使用                                                                                              |
| `--use_gemini`           | Gemini APIを使用                                                                                              |
| `--use_grok`             | xAI (Grok) APIを使用 — `XAI_API_KEY`が必要                                                                   |
| `--use_codex`            | ChatGPTサブスクリプション枠でCodex CLIを使用                                                                  |
| `--use_grok_cli`         | Grokサブスクリプション枠でGrok CLIを使用                                                                      |
| `--use_antigravity`      | Google AI ProまたはUltraサブスクリプション枠でAntigravity CLI（`agy`）を使用                          |
| `--use_opencode`         | OpenCode（オープンソース）経由で設定済みプロバイダーを使用；`--model provider/modèle`が必要                              |
| `--use_openrouter`       | OpenRouterを使用 — `OPENROUTER_API_KEY`と`--model fournisseur/modèle`が必要                                                       |
| `--force`                | 強制的に再翻訳                                                                                                |
| `--keep_filename`        | 元のファイル名を保持                                                                                          |
| `--news`                 | ニュースモード：英語の引用を保護し、言語ごとに国旗を処理                                                      |
| `--add_translation_note` | 翻訳注記を追加                                                                                                |
| `--note_position`        | 注記の位置：`top`、`bottom`（デフォルト）、または`both`                               |
| `--note_format`          | 注記の形式：`legacy`（デフォルト、太字の段落）または`marker`                                     |
| `--include_model`        | 出力ファイルにモデル名を含める                                                                                |
| `--reasoning_effort`     | GPT-5.xの推論エフォート：`none`/`low`/`medium`/`high`/`xhigh`    |

9つの`--use_*`フラグは相互に排他的です。2つ以上を組み合わせることはできません。

## プロバイダー

### API経由：OpenAI、Mistral、Claude、Gemini、Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` は各プロバイダーのエコノミープランに切り替えます。

| プロバイダー | 品質（デフォルト）                                    | エコノミー（`--eco`）     |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol`（`--model` 経由で `terra` および `luna` も可） | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| OpenCode    | `--model provider/modèle` 必須                 | 同左 — `--eco` は効果なし |
| OpenRouter  | `--model fournisseur/modèle` 必須              | 同左 — `--eco` は効果なし |

### ChatGPTサブスクリプション利用：`--use_codex`

公式の Codex CLI を制御します。翻訳は ChatGPT サブスクリプションのクォータから消費され、API キーや従量課金は不要です。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- バイナリは `CODEX_BIN`、次いで `PATH`、最後にパッケージ `openai-codex-cli-bin` の順で検索されます。`~/.codex/auth.json` は一切読み込まれません。
- `OPENAI_API_KEY` と `CODEX_API_KEY` はサブプロセスの環境変数から削除されます。キーが存在していても API に切り替わることはありません。
- 各セグメントは 5 時間枠の「メッセージ」を最低 1 回分消費します（検証に失敗して再試行された場合は 2 回分）。OpenAI の目安では、Plus プランにおいて `gpt-5.6-luna`（`--eco`）で 250〜2,000 メッセージ/5 時間、`gpt-5.6-sol` で 10〜100 メッセージとされています。
- `--model gpt-5.6-terra` および `--model gpt-5.6-luna` もサブスクリプションを経由します。アカウントに利用権限のないモデルを指定すると、400「model is not supported when using Codex with a ChatGPT account」が返されます。
- API よりも低速で、ドキュメントのサイズが大きくなるほどその差は広がります。この README では、中央値で `gpt-5.6-sol` が 1 言語あたり 6 分 46 秒であるのに対し、`gemini-3.7-flash` は 36 秒です。
- CI 環境（`CI` または `GITHUB_ACTIONS` が設定されている場合）では拒否されます。サブスクリプションの認証には個人用セッションファイルが使用され、共有ランナー上に配置すべきではないためです。
- 環境変数：`CODEX_BIN`、`CODEX_TIMEOUT`（セグメントあたりの秒数、デフォルトは 600）。

### Grokサブスクリプション利用：`--use_grok_cli`

SuperGrok または X Premium+ サブスクリプションを対象に、公式の Grok Build CLI を使用して同様の原理で動作します。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Codex よりも隔離（コンパインメント）が弱い。** Grok の OS サンドボックスは最近の多くの Linux 環境（AppArmor、コンテナランタイムソケットなど）では適用されず、適用できないプロファイルは通知なく非隔離のまま起動します。そのため、スクリプトはデフォルトでプロファイルを要求せず、それを通知した上で、CLI の `--deny` ルール（警告なしに保護を解除するのではなく起動を拒否する唯一のレイヤーであるキャッチオール `*` を含む）に依存します。`GROK_TRANSLATE_SANDBOX=read-only` は OS サンドボックスを要求し、マシンがこれに対応できない場合は起動に失敗します。
- クォータは週間単位で、Chat、Imagine、Voice と共有されており、これを確認するコマンドは存在しません。バッチ処理を実行すると、事前の通知なしに対話型の利用枠を消費してしまう可能性があります。
- 環境変数：`GROK_BIN`、`GROK_HOME`（CLI のディレクトリ、デフォルトは `~/.grok`）、`GROK_TIMEOUT`（デフォルトは 900）、`GROK_TRANSLATE_SANDBOX`。

### Googleサブスクリプション利用：`--use_antigravity`

Antigravity の公式 CLI である `agy` を使用して同様の原理で動作します。Google AI Pro または Ultra を契約している場合、トークン単位の課金ではなくサブスクリプションのクォータから翻訳が差し引かれます。このクォータを利用できる唯一の経路です。Gemini CLI は 2026 年 6 月 18 日以降これらのアカウントに対応しておらず（[アナウンス](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)）、Antigravity の SDK は API キーまたは Google Cloud プロジェクトしか受け付けません。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **有料経路は一切開放されません。** agy は環境変数から限定されたリスト（`PATH`、言語とタイムゾーン、ターミナル、ID、プロキシと証明書、セッションバス）のみを受け取り、キーは一切受け取りません。agy の環境変数のいくつかは通知なしに呼び出しを切り替えてしまうため（実測：ドキュメントをサードパーティのゲートウェイに送信するもの、課金対象の Google Cloud プロジェクトに送信するものなど）、拒否リスト方式では確認のたびに見落としが発生していました。すべてのセグメントの処理前に、クォータを消費しない `agy -p /config` を実行し、有料 AI クレジットが無効化され、API キーも Google Cloud プロジェクトも設定されていないことを確認する必要があります（設定が存在しない場合は拒否）。これらが確認できない場合、翻訳は実行されません。その後、各呼び出しのログでサブスクリプションであることが証明されなければならず（`authMethod=consumer`）、証明されない場合その応答は拒否されます。
- **隔離環境。** 各呼び出しはツールを持たない翻訳エージェントとともに、プライベートな使い捨てホームディレクトリで実行されます。既存の agy 設定、ルール、プラグイン、MCP サーバー、フックは読み込まれず、履歴にも何も追加されません。また、認証情報はキーチェーン内に保持され、aipmt が読み取ることは決してありません。エージェントが見つからない場合、agy は通知なしにコーディングエージェントとそのツールにフォールバックします。そのため、適切なエージェントであることを確認するログが丸ごと 1 行存在しなければならず（このメッセージを引用したドキュメントでは代用できません）、存在しない場合は拒否されます。
- **プラットフォーム**：Linux（キーチェーンを備えたセッション内：D-Bus セッションバス、Secret Service）。macOS は動作対象ですが、実測は行われていません。各呼び出しを分離する環境変数が agy で読み込まれない Windows、およびセッションバスのない Linux（SSH セッション、コンテナ、サーバーなど。agy はトークンを `~/.gemini` のファイルに保存しますが、分離によって隠蔽されます）では拒否されます。ログインコードを 1 分間待たされるのではなく、起動前に原因とともに拒否されます。
- **モデル**：`agy models` のモデル群です。Gemini は名前にエフォートが含まれます（`gemini-3.8-flash-medium` など）。サフィックスのない名前は呼び出し前に拒否され、`--reasoning_effort` は効果がありません。デフォルトは `gemini-3.8-flash-medium`、`--eco` 時は `gemini-3.7-flash-low` です。これらを決定した測定キャンペーンは[詳細な測定結果](#詳細な測定結果)に記載されています。Claude および GPT-OSS は独自のはるかに小さなクォータを持ち、実測では Flash の 0.05% に対し、呼び出しあたり 5 時間枠の約 1% を消費します。
- **クォータ**：グループごとに 5 時間枠と週間枠があり、トークンコストに比例します。筆者のアカウントでの測定値：ソース文字 100 万文字あたり、`gemini-3.8-flash-medium` で 5 時間枠の約 16 ポイント、`gemini-3.7-flash-medium` で 14 ポイント、低エフォートで 7〜8 ポイントです。したがって、40,000 文字の README であれば 0.5 ポイント強を消費します。週間リミットはプランによって異なります。再試行は agy が再試行可能と判定したものに従います。それ以外の場合、使い果たされた枠は再試行されず、`/usage` が表示するリセット時刻まで各ファイルを失敗させます。
- **API より低速**：測定用テキストの多い記事において、1 言語あたりの中央値は `gemini-3.8-flash-medium` で 3 分 59 秒、`gemini-3.7-flash-medium` で 3 分 14 秒でした。これに対し、API 経由の Gemini 3.7 Flash は 1 分 18 秒です。
- **中断**：Ctrl-C を押すかターミナルを閉じると、agy はクォータを消費し続けることなくコマンドとともに停止します。これは Codex、Grok CLI、OpenCode も同様です。`nohup` の下では、翻訳は継続します。
- CI 環境（`CI` または `GITHUB_ACTIONS` が設定されている場合）では拒否されます。認証情報が個人のキーチェーンに保持されるためです。ランナー上では `GOOGLE_API_KEY` とともに `--use_gemini` を使用してください。
- 環境変数：`AGY_BIN`（未設定時は `PATH`、次いで `~/.local/bin/agy`）、`AGY_TIMEOUT`（起動時間を含むセグメントあたりの秒数、デフォルトは 900）。

**利用規約：ご自身のアカウントの責任において使用してください。**
[Antigravity の利用規約](https://antigravity.google/terms)（第 6 条）およびその
[FAQ](https://antigravity.google/docs/faq/) では、Antigravity の認証情報を使用してサードパーティ製ソフトウェアからサービスにアクセスすること（Claude Code、OpenClaw、OpenCode が挙げられています）を禁止しており、アカウント停止の対象となります。aipmt はトークンを読み取ることも再利用することもありません。Google がスクリプトや CI 向けに文書化している[ヘッドレスモード](https://antigravity.google/docs/cli/headless/)で公式バイナリを起動します。Google のメンバーは、自身の作業のためにローカルスクリプトから `agy -p` を起動することを「標準的」と述べていますが（[公式フォーラム、2026年9月25日、法的拘束力のない回答](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）、本ツールのような配布ツールのケースについて確定した見解を示す公式文書はありません。

**公開ドキュメントのみを対象としてください。** 同規約の第 5 条によれば、やり取りの内容（プロンプト、応答、メタデータ）は、有料サブスクリプションを含め、Google の製品や機械学習の改善に使用される可能性があり、人手によるレビューを受ける場合があります。オプトアウトには `enableTelemetry` 設定を使用しますが、その効果は文書化されておらず、aipmt はこれを設定しません。また、通常の agy 設定は隔離環境には引き継がれません。機密情報は一切処理させないでください。

### 任意のプロバイダーへの接続：`--use_opencode`

[OpenCode](https://opencode.ai) は、内部で設定された各種プロバイダー（API キー、サブスクリプション、OpenCode Zen ゲートウェイ（アカウント不要の無料モデル）、ローカルモデルなど）へルーティングを行うオープンソース（MIT）のコードエージェントです。ここでは Zen と Ollama の 2 つの経路についてエンドツーエンドの実測を行いました。

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

`--model` は必須です。これが指定されない場合、OpenCode はやり取りが学習に使用される可能性のある無料モデルにフォールバックしますが、その選択をユーザーに無断で行うことはありません。

各呼び出し時の隔離環境：

- 独自設定よりも優先されるインライン設定により、すべてのツールが拒否されたエージェント `aipmt` を定義（`permission: { "*": "deny" }`）、セッション共有は無効化、`--pure`、`--auto` は決して行われません。
- 空の使い捨て作業ディレクトリを使用し、`OPENCODE_DISABLE_PROJECT_CONFIG` および `OPENCODE_DISABLE_CLAUDE_CODE` を設定します。これらがない場合、OpenCode はカレントディレクトリの `AGENTS.md` および `~/.claude/CLAUDE.md` をプロンプトに挿入します。グローバルの `~/.config/opencode/AGENTS.md` は引き続き挿入されます（OpenCode 側でこれを除外する手段が提供されていないため）。
- 出力契約：リターンコード 0、`error` イベントなし、ツールの呼び出しなし、最終ステップが `stop` であること、テキストが空でないこと、およびエージェント `aipmt` が実際に読み込まれていること（未知の `--agent` が指定されても OpenCode はエラーにならず、通知なくコーディングエージェントにフォールバックします）。
- OpenCode 自体のキーである `OPENCODE_API_KEY` を除き、`aipmt` のキーは一切渡されません。プロバイダーの設定は `aipmt` の `.env` ではなく、OpenCode 内で行います。

注意点：

- Zen の無料モデルは変動しやすく、制限も文書化されておらず、やり取りが学習に使用される可能性があります。プライベートなコンテンツではなく、公開ドキュメントにのみ使用してください。
- セグメントは最大 16,000 文字に達するため、ローカルモデルは少なくとも 16k トークンのコンテキストを提供する必要があります。Ollama は 4,096 に設定されていることが多いため、`PARAMETER num_ctx 32768` を指定した `Modelfile` を経由してください。
- `--eco` は効果がありません。`--reasoning_effort` は OpenCode の `--variant` としてそのまま渡されます。
- OpenCode は各セッションを `~/.local/share/opencode/` にログ記録します。
- 環境変数：`OPENCODE_BIN`（未設定時は `PATH`、次いで `~/.opencode/bin/opencode`）、`OPENCODE_TIMEOUT`（セグメントあたりの秒数、デフォルトは 600）。`OPENCODE_CONFIG` はそのまま OpenCode に渡されます。

Ollama 経由のローカルモデルの例（`~/.config/opencode/opencode.json` 内）：

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

`reasoningEffort: "none"` は、Ollama がこれらのモデルでデフォルトで有効にしている思考（シンキング）プロセスを停止します（Modelfile では無効化できません）。6 単語の文での実測値：オプションなしでは 919 トークンの思考と 68 秒、オプションありでは 9 トークンでした。

### 400以上のモデルへ：`--use_openrouter`

OpenRouter は、単一のクレジットでサードパーティがホストするモデル群（他プロバイダーでは提供されていないオープンな中国製モデルなどを含む）に対して従量課金でルーティングを行うサービスです。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` は必須です。課金が発生する前に実行されるプリフライト処理により、ルーティング特有の 2 つの問題に対処します。

- **同一モデルが異なる上限を持つ多数のホストによって提供されている** — `z-ai/glm-5.3-flash` では、23 のホストのうち 1 つは出力トークンが 2,048 に制限されています。プリフライトは `/api/v1/models/{modèle}/endpoints` を読み取り、出力トークンが 8,000 未満のホストやステータスが低下しているホストを除外し、その他のホストを `allow_fallbacks: false` で固定します。
- **推論思考は出力料金で課金される** — `z-ai/glm-5.2` の「OK」という応答に対して、通常 2 トークンのところ 107 トークン消費されます。デフォルトでこれは無効化されます。思考を必須とするモデルには受け付け可能な最低限のエフォートが設定されます（カタログのデフォルト値では翻訳完了前に出力枠を使い果たす恐れがあるため）。`--reasoning_effort` が引き続き優先されます。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- コンテキストウィンドウはカタログから取得されます。16,400 トークン未満のモデルは呼び出し前に拒否されます（プロンプトとセグメント用に 8,400、最小出力用に 8,000）。
- カタログに存在しないスラッグ、カタログに接続できない場合、または上限要件を満たすホストが存在しない場合、コマンドは停止します。
- 出力が空の `finish_reason=length` は、切り捨てではなく推論思考によってバジェットが消費されたことを意味します。メッセージ上でこれが区別されます。
- `--eco` は効果がありません。
- 環境変数：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>）、`OPENROUTER_BASE_URL`（デフォルトは `https://openrouter.ai/api/v1`、`https://` 必須）、`OPENROUTER_TIMEOUT`（デフォルトは 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（デフォルトは 30）。

### 翻訳注記

`--add_translation_note` は、`bottom`（デフォルト）、`top`（front matter の後）、または `both`（`--note_position`）に注記を追加します。フォーマットは `legacy`（太字の段落、デフォルト）または `marker`（`--note_format`）です。フォーマット `marker` は、不可視の Markdown 参照定義
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`
に太字の引用が続く形式です。GitHub 上で視認可能であり、ビルド時に remark プラグインで利用できます。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 詳細な測定結果

すべての測定は、`aipmt` を使用して 14 言語（en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi）へ実際に実行された翻訳に基づいています。
**書き出し成功（Écrites）** はガードを通過したファイル数をカウントし、**差異なし（Sans écart）** は `scripts/compare_structure.py` で何も検出されなかったもの（セクション数、サブタイトル数、リンク数、個別 URL 数、コードブロック数、インラインコード数、テーブル行数、引用ブロック数、太字単語数が同一であること）をカウントしています。

「差異なし」とは「何も検出されなかった」という意味であり、「完全に同一」を意味するものではありません。比較ツールは内容を読まずに要素の数をカウントします。削除されたレベル 4 の見出し、置き換えられたインラインコードのテキスト、入れ替わったフラグ、余計な括弧が付いてどこにもリンクしなくなった内部リンク（`[texte]((#ancre))`）などは検出されず、言語の妥当性を評価することもありません。

### 密度の高い動向調査記事、`--news` モード

[jls42.org の AI 動向調査](https://jls42.org/fr/news)の 1 エディション：
589行、140リンク、21セクション、3つの保護された英語引用。2026年9月4日および5日のテスト。

| モデル | アクセス方法 | 生成完了 | 差異なし | 中央値/言語 |
| --- | --- | --- | --- | --- |
| `gemini-3.7-flash` | Google API | 14/14 | ✅ **14/14** | 1分18秒 |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google サブスクリプション | 14/14 | ✅ **14/14** | 3分59秒 |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google サブスクリプション | 14/14 | ✅ **14/14** | 3分14秒 |
| `gpt-5.6-sol` (`--use_codex`) | ChatGPT サブスクリプション | 14/14 | ✅ **14/14** | 11分28秒 |
| `z-ai/glm-5.2` | OpenRouter | 14/14 | ✅ **14/14** | 5分37秒 |
| `qwen/qwen3.8-flash` | OpenRouter | 14/14 | ✅ **14/14** | 26分23秒 |
| `claude-sonnet-5` | Anthropic API | 14/14 | ⚠️ 11/14 | 6分31秒 |
| `opencode/mimo-v2.5-free` | OpenCode Zen | 13/14 | ❌ 11/14 | 9分27秒 |
| `qwen/qwen3.7-flash` | OpenRouter | 13/14 | ❌ 8/14 | 10分09秒 |
| `ollama/gpt-oss-20b-32k` | ローカル | 10/14 | ❌ 7/14 | 12分39秒 |
| `mistral-large-latest` | Mistral API | 11/14 | ❌ 5/14 | 5分32秒 |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter | 4/14 | ❌ 3/14 | 37分27秒 |
| `grok-4.6` (`--use_grok_cli`) | Grok サブスクリプション | 1/14 | ❌ 1/14 | 23分11秒 |

Grok は9月9日に同じ動向調査の別エディション（356行）で再測定されました：14言語中9言語生成、差異なしは8言語。冒頭の表に記載されているのはこの数値です。中断された3つのテストはカウントされていません：クレジット不足による `qwen3.5-27b`（9言語）および `kimi-k2.6`（4言語）、推論設定に起因する2件のエラーが発生した `z-ai/glm-5.3-flash`（プロバイダー側で修正対応中）。OpenRouter の行は、`--use_openrouter` 以前のルーターのデフォルト設定で測定されました。提供プロバイダーで再測定された `z-ai/glm-5.2` は、同様に 14/14 を記録しています。数値は9月10日に現在の比較ツールで再計算されました：最初の公開と比較して `qwen3.8-flash` と `qwen3.7-flash` がそれぞれ1言語増え、その他は変更ありません。

`--use_antigravity` の各行は9月26日に同一記事で、4並列翻訳で測定されました：午前に `gemini-3.7-flash-medium`、午後に `gemini-3.8-flash-medium`。英語では、それぞれがフラグを捏造することなく引用下の3行のフランス語訳を自身で削除し、英語の引用も損なわれませんでした。フォールバックのクリーンアップ処理は何も行う必要がありませんでした。`--eco`（`gemini-3.7-flash-low`）では、4言語のみ（en、ja、ar、hi）でテストされ、4言語中4言語生成、すべて差異なし、中央値は1分52秒でした。同日に動向調査のより新しいエディションである9月25日分（438行、英語引用2件）で `gemini-3.7-flash-medium` を用いてブログ外で翻訳した検証テストでは、14言語中14言語生成、すべて差異なし、言語あたり87〜128秒でした。

### このプロジェクトの README、標準 Markdown

2026年9月9日固定リビジョン：785行、インラインコード285個、コードブロック終了記号40個、表の行数89行。4並列翻訳。

| モデル | 生成完了 | 差異なし | 中央値/言語 | 相違点 |
| --- | --- | --- | --- | --- |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14 | ✅ 14/14 | 1分43秒 | なし |
| `gemini-3.7-flash` | 14/14 | ⚠️ 13/14 | 36秒 | 太字単語1つ (ja) |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14 | ⚠️ 13/14 | 1分22秒 | 太字単語1つ (ko) |
| `claude-sonnet-5` | 14/14 | ⚠️ 12/14 | 2分56秒 | リンク1つ (sv)、太字単語1つ (zh) |
| `gpt-5.6-sol` (`--use_codex`) | 14/14 | ⚠️ 12/14 | 6分46秒 | 太字単語1つ (ar, ja) |
| `z-ai/glm-5.2` (OpenRouter) | 14/14 | ⚠️ 11/14 | 2分34秒 | 太字単語1つ (hi, ja, ko) |
| `qwen/qwen3.7-flash` | 14/14 | ⚠️ 10/14 | 2分17秒 | アラビア語で40個のインラインコード追加、太字 (hi, ja, ko) |
| `mistral-large-latest` | 14/14 | ❌ 1/14 | 2分44秒 | セクション消失 (ar, hi, ko)、コードブロック追加 (ja, ko, ro, zh) |

中断された2つのテストは記載されていません：Grok（12言語後にCLIセッション期限切れ、差異なし11言語）、および `qwen3.8-flash`（2言語後にホスト元から HTTP 429）。`opencode/mimo-v2.5-free` と `ollama/gpt-oss-20b-32k` はこのリビジョンで再測定されていません。277行短かった9月4・5日のリビジョンでは、それぞれ14言語中9言語を生成し、差異なしはそれぞれ7言語と1言語でした。

`--use_antigravity` の行は固定リビジョンでは測定されておらず、9月26日に 1.14.0 とともに公開されたリビジョンで測定されました：600行、インラインコード257個、コードブロック終了記号30個、表の行数85行。185行短いため他の行と一対一で直接比較することはできませんが、Antigravity の2つの行同士は比較可能です。比較ツールがチェックしない内部リンクについて、`gemini-3.8-flash-medium` は14言語すべてで損なわれずに保持し、`gemini-3.7-flash-medium` はイタリア語で破損させました。

### 著名プロジェクトの4つの README

FastAPI、Ollama、tldr-pages、Vue.js。GitHub からそのまま取得したもので、先の2つよりも扱いやすいドキュメントです。このテストは苦戦しているモデルを対象としており、Gemini は比較基準として機能しています。

| モデル | 範囲 | 生成完了 | 差異なし |
| --- | --- | --- | --- |
| `gemini-3.7-flash` | 4プロジェクト × 14言語 | 56/56 | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4プロジェクト × 14言語 | 55/56 | ❌ 47/56 |
| `grok-4.6` (サブスクリプション) | 4プロジェクト × ar, hi, ja, zh | 16/16 | ❌ 14/16 |
| `ollama/gpt-oss-20b-32k` | 4プロジェクト × ar, hi, ja, zh | 15/16 | ❌ 9/16 |

### これらの測定に含まれない事項

- **網羅的なランキングではありません**：OpenRouter 単体でも400以上のモデルを提供しており、測定されたのは約15種類です。
- **所要時間は目安です**：テストによって3〜6並列翻訳で行われており、プロバイダーのスループットは時間帯によって変動します。
- **特定時点の観測結果です**：モデルは同じ名称のまま変更されることがあり、あなたのドキュメントは私たちのものとは異なります。

固定されたファイルのコピーを用いて、ご自身のドキュメントで測定を再実行する場合：

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## 貢献する

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

両方の行が必要です：`pip install -e .` がないと、`python -m aipmt` は `No module named aipmt` と返答します。

品質管理ツール（任意ですが推奨）：

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

リポジトリ内の28の翻訳（README と CHANGELOG、14言語）は `./regen_translations.sh --force` で再生成されます。デフォルトでは ChatGPT サブスクリプション上で Codex と `gpt-5.6-sol` を使用し、4並列で実行されます。`REGEN_PROVIDER` と `REGEN_MODEL` でパスを変更できます：`antigravity` はサブスクリプション（Google）のまま維持され、例外指定なしで実行可能です。課金制 API（`openai`、`gemini`、`grok`、`openrouter`）は `REGEN_ALLOW_PAID_API=1` なしでは拒否されます。`REGEN_JOB_TIMEOUT` は各ジョブの上限時間を設定します（600秒、Codex と Antigravity では 1,800秒）。ツールの詳細については `CLAUDE.md` を参照してください。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** — 15言語で公開されている個人ブログ。その[毎日の AI 動向調査](https://jls42.org/fr/news)はこのツールによって毎日翻訳されており、上記の測定における基準ドキュメントとして機能しています。

## 著者

Julien LE SAUX
メール: contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。[LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE) を参照してください。

## 免責事項

本プログラムは GPL v3 のセクション15および16の条件に基づき、**いかなる保証もなし**で配布されます。「現状有姿」で提供され、商品性または特定目的への適合性の保証はなく、その作成者は本プログラムの使用から生じるいかなる損害に対しても責任を負いません。この要約よりもライセンスの原文が優先されます。

- **公開前に確認してください。** 保護対象はコードブロック、インラインコード、URL、アンカー、および `--news` モードの引用です。見出し、表、front matter、文の意味そのものは保護されません。
- **ドキュメントは選択したプロバイダーに送信されます。** 各プロバイダーの利用規約およびデータポリシーが適用されます。一部の無料モデルはやり取りをモデルのトレーニングに再利用する場合があり、Antigravity の規約では、有料サブスクリプションであっても Google が再利用し、人間の手でレビューすることを許可しています。ローカルモデルは、マシン外にデータを一切送信しない唯一の方法です。
- **API 呼び出しには費用が発生します。** 本プログラムは支出を制限しません。長いドキュメント、失敗後のリトライ、あるいは深く推論を行うモデルほどコストが高くなります。
- **公開されている測定結果は特定時点の観測結果であり**、保証ではありません。

記載されている製品名および会社名は、それぞれの所有者に帰属します。本プロジェクトはいずれとも提携していません。

**gemini-3.8-flash-mediumでフランス語から日本語に翻訳された記事。**
