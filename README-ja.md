# AIパワード Markdown 翻訳ツール

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

Markdownファイルを構造（コードブロック、インラインコード、URL、アンカー、テーブル、フロントマター）を保持したまま別の言語に翻訳します。モデルを呼び出す10種類の方法（5つのAPI、従量課金なしの3つのサブスクリプション、2つのルーター）と、各モデルが実際に何を保持できるかについて公開されたベンチマークを提供します。

## 概要

- **10種類のプロバイダーパス**: OpenAI、Mistral、Claude、Gemini、GrokのAPI。従量課金なしのChatGPT (Codex)、Grok、Google (Antigravity)のサブスクリプション。OpenCode（オープンソース、無料またはローカル）およびOpenRouter（400以上のモデル）のルーター。
- **トークンの欠落による破損を防止**: コードブロック、インラインコード、URL、アンカー、引用は呼び出し前にトークンに置き換えられ、応答時に検証されます。1つでも欠落している場合、ファイルは書き込まれません。
- **長文ドキュメント**: モデルのコンテキストウィンドウに応じてセグメンテーション。
- **`--news` モード**: 情報収集・ニュース記事向けに、英語の引用を保護し、言語ごとにフラグを管理。
- **`--eco` モード**: 高速で安価なモデルを使用。
- **翻訳ノート**: オプションで先頭、末尾、またはその両方に追加可能。

## インストール

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10以降。リポジトリからのインストールについては、[貢献方法](#貢献する)を参照してください。

## 設定

キーは優先度の高い順に以下の3箇所から読み取られます。前の場所で設定されていない項目のみが次の場所で補完されます。

|     | 場所                                          | 用途                                  |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 環境変数                                      | CI、コンテナ、一時的な上書き          |
| 2   | カレント（または親）ディレクトリの `.env` | プロジェクト固有のキー                |
| 3   | `~/.config/aipmt/.env`                                 | 一度設定すればどこでも有効            |

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

`GOOGLE_API_KEY` の代わりに `GEMINI_API_KEY` も受け入れられます。ユーザーファイルは `XDG_CONFIG_HOME`（絶対パスのみ）に従い、Windowsでは `%APPDATA%` に従います。キーが見つからない場合、コマンドはこれら3つの場所を一覧表示します。

**プロジェクトの `.env` は、呼び出しをリダイレクトしたり、実行されるプログラムを選択したりすることはできません。** キーを提供するのみで、送信先やバイナリを指定することは決してありません。`_BASE_URL`、`_API_BASE`、`_ENDPOINT`、`_BIN`（`CODEX_BIN`、`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`）、`GROK_HOME`、プロキシ（`HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY`）、証明書ストア（`SSL_CERT_FILE`、`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）、および `XDG_CONFIG_HOME` / `APPDATA` の変数はすべて無視され、警告が表示されます。クローンしたリポジトリがキーを不正取得したり、初回翻訳時に独自のプログラムを実行させたりするのを防ぐためです。また、このファイルは変数展開なしで読み取られるため、`NOM=${OPENAI_API_KEY}` でキーが複製されることもありません。これらの変数は環境変数または `~/.config/aipmt/.env` で設定してください。

オプション変数: `XAI_BASE_URL`（デフォルト: `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（呼び出しあたりの秒数、デフォルト: 900）、`CODEX_BIN`、`CODEX_TIMEOUT`（デフォルト: 600）、`GROK_BIN`、`GROK_HOME`（デフォルト: `~/.grok`）、`GROK_TIMEOUT`（デフォルト: 900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（デフォルト: 900）、`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（デフォルト: 600）、`OPENROUTER_BASE_URL`（`https://` が必要）、`OPENROUTER_TIMEOUT`（デフォルト: 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（デフォルト: 30）。各変数の詳細は該当するプロバイダーのセクションに記載されています。

## はじめに

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` をスペイン語に翻訳すると `--target_dir` 内に `document-es.md` が生成されます。`--include_model` を指定すると `document-es-gpt-5.6-terra.md` になります。元のファイル名を保持する `--keep_filename` を除き、拡張子は常に `.md` になります（例: `article.mdx` は `article-en.md` になります）。既存の翻訳は `--force` が指定されていない限りスキップされます。

終了コード: すべて成功またはスキップされた場合は `0`、失敗したファイルがある場合は `1`（標準エラー出力にリスト表示）、設定に問題がある場合は `2`。失敗したファイルが書き込まれることはありません。書き込み自体が失敗した場合でも、内容は別の一時ファイルに書き込まれてからリネームされます。再実行するだけで対応できます。

## どのモデルを選ぶべきか

各モデルによって同じ14言語に翻訳された、2つの実際のドキュメントで測定されました。**数値は、14言語中、翻訳が出力され、かつ元の構造との差異が一切なかった言語の数です。**

| モデル               | アクセス方法                      | 密度の高い情報収集記事  | このREADME   | 差異の内容と該当言語数                                                                                                                |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | Google APIキー                    | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語: 太字が1単語多い (ja)                                                                                                   |
| **Gemini 3.7 Flash** | Googleサブスクリプション (Antigravity) | ✅ 14/14           | ⚠️ 13/14     | 14言語中1言語: 太字が1単語少ない (ko)                                                                                                  |
| **GPT-5.6 Sol**      | ChatGPTサブスクリプション、またはOpenAIキー | ✅ 14/14        | ⚠️ 12/14     | 14言語中2言語: 太字が1単語少ない (ar, ja)                                                                                              |
| **GLM-5.2**          | OpenRouterキー                    | ✅ 14/14                | ⚠️ 11/14     | 14言語中3言語: 太字が1単語少ない (hi, ja, ko)                                                                                          |
| Claude Sonnet 5      | Anthropic APIキー                 | ⚠️ 11/14                | ⚠️ 12/14     | 記事で3言語: コードブロックが余分に出現 (es, de, hi)。このREADMEで2言語: リンクのマークアップ欠落 (sv)、太字が1単語 (zh)               |
| Qwen 3.7 Flash       | OpenRouterキー                    | ❌ 8/14                 | ⚠️ 10/14     | 記事で1言語が拒否、他の5言語で差異あり。このREADMEで約40単語が `code` 化 (ar)                                                 |
| Grok 4.6             | Grokサブスクリプション            | ❌ 8/14                 | 評価なし     | 14言語中5言語が拒否（インラインコードとURLの未返却のため）。オランダ語は全面的に乖離                                                    |
| GPT-OSS 20B          | ローカルモデル (Ollama)           | ❌ 7/14                 | 再測定なし   | 14言語中4言語が拒否（フランス語の文節が残存し、ガード機構により停止）                                                                 |
| MiMo v2.5 (無料)     | OpenCode Zen（アカウント不要）    | ❌ 11/14                | 再測定なし   | 1言語が拒否。ポーランド語で1セクションが消失                                                                                         |
| Mistral Large        | Mistral APIキー                   | ❌ 5/14                 | ❌ 1/14      | **セクション全体が消失**: 記事で1言語 (hi)、このREADMEで3言語 (ar, hi, ko)。記事でさらに3言語が拒否                                    |
| DeepSeek V4 Flash    | OpenRouterキー                    | ❌ 3/14                 | 再測定なし   | 14言語中10言語が拒否。1言語あたり37分                                                                                                 |

|     | 記号の意味                                                                                                                                                            |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14言語すべてが翻訳され、元の構造と一切差異がない                                                                                                                      |
| ⚠️  | 14言語すべてが翻訳されたが、**マークアップ**に差異がある（太字が1単語、`code`、角括弧が失われたリンクなど）。テキスト、URL、コードブロック、セクションの欠落はない |
| ❌  | 少なくとも1つの言語で翻訳できなかった（ファイルが拒否され書き込まれなかった）、**または**書き込まれたファイルにコンテンツの欠落がある                                |

重要なポイント:

- **拒否された翻訳は、破損した翻訳ではありません。** 返答時にトークンが欠落している場合、ファイルは書き込まれず、その言語は拒否としてカウントされます。これは記事テストでのGrokに発生したもので、5つの非ラテン文字体系において最初のセグメントから4つのインラインコードと3つのURLが失われました。
- **このセーフティネットは、見出し、テーブル、フロントマター、本文の欠落はカバーしません。** セクションを削除するモデルが出力した場合、ツールはそのままファイルを書き込みます（Mistralのケース）。これらの要素はトークンに置き換えることができず、現在のガード機構では検査されません。`scripts/compare_structure.py` はセクションの消失を検出しますが、事後処理になります。
- **このREADMEにおけるGrokの評価はありません**: CLIセッションが12言語（うち11言語は差異なし）の処理後に期限切れとなったためです。中断されたテストは評価対象外としています。
- **言語よりもドキュメントの密度が影響します。** Grokは通常のREADMEでは問題ありませんが、オランダ語を含めリンクが密集した記事では破綻します。

実施日とドキュメント: 「このREADME」の列は、2026年9月9日に本ファイルの固定リビジョン（785行、インラインコード285個、テーブル89行、その後改訂）で測定されました。ただしAntigravityの行は、1.14.0で公開されたより短いリビジョン（600行、インラインコード257個、テーブル85行）で9月26日に測定されたものです。「密度の高い情報収集記事」の列は、589行の記事に対する9月4日〜5日のテストによるものです（Grokの行は9月9日に同ニュースレターの別版で再測定、Antigravityの行は9月26日に同記事で測定）。完全な表、所要時間、プロトコルは[詳細な測定結果](#詳細な測定結果)に記載されています。

## すべてのオプション

| オプション               | 説明                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | 翻訳する単一のMarkdownファイル（`--source_dir` の代替）                                                       |
| `--source_dir`           | Markdownファイルを含むソースディレクトリ（デフォルト: `content/posts`）                                        |
| `--target_dir`           | 翻訳済みファイルの出力先ディレクトリ（デフォルト: `traductions_en`）                                            |
| `--source_lang`           | 翻訳元言語（デフォルト: `fr`）                                                                      |
| `--target_lang`           | 翻訳先言語（デフォルト: `en`）                                                                      |
| `--model`           | 使用する特定のモデル                                                                                          |
| `--eco`           | 経済的なモデルを使用                                                                                          |
| `--use_mistral`           | Mistral AI APIを使用                                                                                          |
| `--use_claude`           | Claude APIを使用                                                                                              |
| `--use_gemini`           | Gemini APIを使用                                                                                              |
| `--use_grok`           | xAI (Grok) APIを使用 — `XAI_API_KEY` が必要                                                                 |
| `--use_codex`           | ChatGPTサブスクリプションのクォータでCodex CLIを使用                                                          |
| `--use_grok_cli`           | GrokサブスクリプションのクォータでGrok CLIを使用                                                              |
| `--use_antigravity`           | Google AI ProまたはUltraサブスクリプションのクォータでAntigravity CLI (`agy`) を使用                |
| `--use_opencode`           | OpenCode（オープンソース）を使用し、OpenCodeで設定されたプロバイダーへ接続。`--model provider/modèle` が必要             |
| `--use_openrouter`           | OpenRouterを使用 — `OPENROUTER_API_KEY` と `--model fournisseur/modèle` が必要                                                    |
| `--force`           | 強制的に再翻訳                                                                                                |
| `--keep_filename`           | 元のファイル名を保持                                                                                          |
| `--news`           | ニュースモード: 英語の引用を保護し、言語ごとにフラグを管理                                                    |
| `--add_translation_note`           | 翻訳ノートを追加                                                                                              |
| `--note_position`           | ノートの位置: `top`、`bottom`（デフォルト）、または `both`                            |
| `--note_format`           | ノートの形式: `legacy`（デフォルト、太字段落）または `marker`                                   |
| `--include_model`          | 出力ファイルにモデル名を含める                                                                                |
| `--reasoning_effort`          | GPT-5.x 推論エフォート: `none`/`low`/`medium`/`high`/`xhigh`       |

9つの `--use_*` フラグは相互に排他的です。2つ以上を組み合わせると拒否されます。

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

| プロバイダー | 品質（デフォルト）                                      | エコノミー (`--eco`)      |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5`                                     | `claude-haiku-4-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol`（`--model` 経由で `terra` および `luna` も可） | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.7-flash-medium`                             | `gemini-3.7-flash-low`    |
| OpenCode    | `--model provider/modèle` 必須                 | 同上 — `--eco` は効果なし |
| OpenRouter  | `--model fournisseur/modèle` 必須              | 同上 — `--eco` は効果なし |

### ChatGPT サブスクリプション経由：`--use_codex`

公式 Codex CLI を制御します。翻訳は API キーや従量課金なしで、ChatGPT サブスクリプションの利用枠から消費されます。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- バイナリは `CODEX_BIN`、続いて `PATH`、次に `openai-codex-cli-bin` パッケージの順で検索されます。`~/.codex/auth.json` は読み取られません。
- サブプロセスの環境変数から `OPENAI_API_KEY` と `CODEX_API_KEY` は削除されます。キーが存在していても API に切り替わることはありません。
- 各セグメントは5時間の枠から少なくとも1「メッセージ」を消費します（検証に失敗して再試行された場合は2メッセージ）。OpenAI の公表している目安では、Plus プランの場合、`gpt-5.6-luna`（`--eco`）で250〜2,000メッセージ/5時間、`gpt-5.6-sol` で10〜100メッセージ/5時間です。
- `--model gpt-5.6-terra` および `--model gpt-5.6-luna` もサブスクリプション経由で動作します。アカウントに対象権限がないモデルの場合は 400「model is not supported when using Codex with a ChatGPT account」が返されます。
- API よりも遅く、ドキュメントが長くなるほど差が開きます。本 README では、`gpt-5.6-sol` の場合の中央値で1言語あたり6分46秒、`gemini-3.7-flash` では36秒でした。
- CI では拒否されます（`CI` または `GITHUB_ACTIONS` が定義されている場合）。サブスクリプションは個人用のセッションファイルで認証されるため、共有ランナー上に置くべきではないからです。
- 環境変数：`CODEX_BIN`、`CODEX_TIMEOUT`（セグメントあたりの秒数、デフォルトは 600）。

### Grok サブスクリプション経由：`--use_grok_cli`

SuperGrok または X Premium+ サブスクリプション上で、公式 Grok Build CLI を使用する同様の仕組みです。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Codex よりも緩い分離。** Grok の OS サンドボックスは、近年の多くの Linux 環境（AppArmor、コンテナランタイムソケット）では適用できず、適用できないプロファイルは通知なく非制限のまま起動します。そのため、スクリプトはデフォルトでプロファイルを要求せず、それを通知した上で、CLI の `--deny` ルール（無言で保護を解除する代わりに起動を拒否する唯一のレイヤーである包括的ルール `*` を含む）に依存します。`GROK_TRANSLATE_SANDBOX=read-only` は OS サンドボックスを要求し、マシンがこれに対応できない場合は起動に失敗します。
- クォータは週間単位で Chat、Imagine、Voice と共有されており、これを確認するコマンドはありません。そのため、バッチ処理によって事前の通知なしに対話用の利用枠が消費される可能性があります。
- 環境変数：`GROK_BIN`、`GROK_HOME`（CLI のディレクトリ、デフォルトは `~/.grok`）、`GROK_TIMEOUT`（デフォルトは 900）、`GROK_TRANSLATE_SANDBOX`。

### Google サブスクリプション経由：`--use_antigravity`

Antigravity の公式 CLI である `agy` を使用する同様の仕組みです。Google AI Pro または Ultra の有料プランを利用している場合、翻訳はトークン課金ではなくサブスクリプションの利用枠から消費されます。Gemini CLI は2026年6月18日以降これらのアカウントをサポートしておらず（[告知](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)）、Antigravity の SDK は API キーまたは Google Cloud プロジェクトのみを受け付けるため、この利用枠を使用する唯一の方法となります。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **有料ルートは一切開いたままにされません。** agy は環境変数から限定されたリスト（`PATH`、言語とタイムゾーン、ターミナル、ID、プロキシと証明書、セッションバス）のみを受け取り、キーは一切受け取りません。いくつかの環境変数は画面に何も表示せずに呼び出しを切り替えてしまうため（検証済み：1つはドキュメントをサードパーティのゲートウェイに送信し、もう1つは課金対象の Google Cloud プロジェクトに送信します）、拒否リスト方式では見落としが生じていました。いかなるセグメントの処理前にも、クォータを消費しない `agy -p /config` によって、有料 AI クレジットが無効であり、API キーや Google Cloud プロジェクトが存在しないことを確認する必要があります（設定が存在しない場合は拒否）。そうでなければ翻訳は実行されません。その後、各呼び出しのログでサブスクリプション（`authMethod=consumer`）が証明されなければならず、そうでなければ応答は拒否されます。
- **分離。** 各呼び出しはツールのない翻訳エージェントとともに、使い捨てのプライベートな個別ディレクトリで実行されます。ユーザーの agy 設定、ルール、プラグイン、MCP サーバー、フックは読み込まれず、履歴にも何も追加されず、認証情報はキーリング内に保持され aipmt が読み取ることはありません。エージェントが見つからない場合、agy は通知なくコーディングエージェントとそのツールにフォールバックします。そのため、ログの1行全体で正しいエージェントが確認されなければなりません（ドキュメント内にそのメッセージが引用されているだけでは不十分です）。確認できない場合は拒否されます。
- **プラットフォーム**：Linux（キーリングが存在するセッション内：D-Bus セッションバス、Secret Service）。macOS もサポートされますが、計測は行われていません。Windows（agy が各呼び出しを分離する変数を読み取らないため）およびセッションバスのない Linux（SSH セッション、コンテナ、サーバー：agy がトークンを `~/.gemini` 内のファイルに保存し、分離によってそれが隠蔽されるため）では拒否されます。ログインコードの待機に1分待たされるのではなく、起動前に理由とともに即座に拒否されます。
- **モデル**：`agy models` のモデル。Gemini モデルは名前に思考レベル（effort）が含まれます（`gemini-3.7-flash-low` など）。サフィックスのない名前は呼び出し前に拒否され、`--reasoning_effort` は効果を持ちません。2つのデフォルト設定は、14言語にわたる検証によって決定されました（[詳細な測定結果](#詳細な測定結果) を参照）。Claude と GPT-OSS は独自のより小さなクォータを持ち、実測では Flash の 0.05% に対し、1回の呼び出しにつき5時間枠の約 1% を消費します。
- **クォータ**：グループごとに5時間枠と週間枠があり、トークンコストに比例して消費されます。著者のアカウントで32回の翻訳を実行して計測したところ、`gemini-3.7-flash-medium` で40,000文字の README に対して5時間枠の約0.5ポイントでした。週間制限はプランによって異なります。再試行は agy が再試行可能と判定したものに従います。それ以外の場合、使い切った枠に対して再試行は行われず、`/usage` に表示されるリセット時刻まで各ファイルは失敗します。
- **API よりも遅い**：詳細な測定結果の記事において、Gemini 3.7 Flash はサブスクリプション経由の場合の中央値で1言語あたり3分14秒、API 経由では1分18秒でした。
- **中断**：Ctrl-C またはターミナルの切断により、コマンドとともに agy も停止し、クォータを消費し続けるのを防ぎます。Codex、Grok CLI、OpenCode でも同様です。`nohup` 配下では翻訳は継続します。
- CI では拒否されます（`CI` または `GITHUB_ACTIONS` が定義されている場合）：認証情報は個人のキーリング内に存在します。ランナー上では `GOOGLE_API_KEY` を指定して `--use_gemini` を使用してください。
- 環境変数：`AGY_BIN`（設定されていない場合は `PATH`、続いて `~/.local/bin/agy`）、`AGY_TIMEOUT`（起動時間を含むセグメントあたりの秒数、デフォルトは 900）。

**利用規約：自己のアカウントの責任において使用してください。** [Antigravity 利用規約](https://antigravity.google/terms)（第6条）およびその [FAQ](https://antigravity.google/docs/faq/) では、Antigravity のログインを使用してサードパーティ製ソフトウェア（Claude Code、OpenClaw、OpenCode が例示されています）経由でサービスにアクセスすることを禁止しており、違反した場合はアカウント停止の対象となります。aipmt はトークンを読み取ったり再利用したりせず、Google がスクリプトや CI 向けに文書化している [ヘッドレスモード](https://antigravity.google/docs/cli/headless/) で公式バイナリを起動します。Google の担当者は自身の業務のためにローカルスクリプトから `agy -p` を起動することを「標準的」と判断していますが（[公式フォーラム、2026年9月25日、法的拘束力のない回答](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）、本ツールのように配布されるツールに関する明確な規定はありません。

**公開ドキュメント専用。** 同規約の第5条に基づき、やり取りの内容（プロンプト、応答、メタデータ）は、有料サブスクリプションを含め、Google の製品や機械学習の改善に使用されたり、人間によって確認されたりする場合があります。オプトアウトには効果が文書化されていない `enableTelemetry` の設定が必要ですが、aipmt はこれを設定しません。また、ユーザー独自の agy 設定は分離環境には引き継がれません。機密情報は一切通さないでください。

### 任意のプロバイダー向け：`--use_opencode`

[OpenCode](https://opencode.ai) は、内部で設定されたプロバイダー（API キー、サブスクリプション、アカウント不要の無料モデルを提供する OpenCode Zen ゲートウェイ、またはローカルモデル）へルーティングを行うオープンソース（MIT）のコードエージェントです。ここでは Zen と Ollama の2つの経路についてエンドツーエンドの計測を行いました。

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

`--model` は必須です。指定しない場合、OpenCode はやり取りが学習に使用される可能性がある無料モデルにフォールバックしますが、この選択が勝手に行われることはありません。

各呼び出しにおける分離：

- ユーザー設定より優先されるインライン設定により、すべてのツールが無効化された（`permission: { "*": "deny" }`）エージェント `aipmt` を定義し、セッション共有を無効化（`--pure`）、`--auto` は決して使用しません。
- 空の使い捨て作業ディレクトリを使用し、`OPENCODE_DISABLE_PROJECT_CONFIG` と `OPENCODE_DISABLE_CLAUDE_CODE` を設定します。これらがないと、OpenCode はカレントディレクトリの `AGENTS.md` や `~/.claude/CLAUDE.md` をプロンプトに注入してしまいます。グローバルの `~/.config/opencode/AGENTS.md` は注入されたままになりますが、OpenCode ではこれを除外できません。
- 出力規約：終了コード 0、`error` イベントなし、ツール呼び出しなし、最後のステップが `stop`、空でないテキスト、エージェント `aipmt` が実際にロードされていること（未知の `--agent` を指定しても OpenCode はエラーにならず、無言でコーディングエージェントにフォールバックします）。
- OpenCode 自体のキーである `OPENCODE_API_KEY` を除き、`aipmt` のキーは一切渡されません。プロバイダーの設定は `aipmt` の `.env` ではなく、OpenCode 内で行います。

注意事項：

- Zen の無料モデルは変更される可能性があり、制限も文書化されておらず、やり取りが学習に使用される場合があります。公開ドキュメント用であり、非公開コンテンツには適していません。
- ローカルモデルは少なくとも 16k トークンのコンテキストを提供する必要があります（セグメントは最大 16,000 文字になるため）。Ollama は多くの場合 4,096 に設定されているため、`PARAMETER num_ctx 32768` を指定した `Modelfile` を使用してください。
- `--eco` は効果がありません。`--reasoning_effort` は OpenCode の `--variant` としてそのまま渡されます。
- OpenCode は各セッションを `~/.local/share/opencode/` にログ記録します。
- 環境変数：`OPENCODE_BIN`（設定されていない場合は `PATH`、続いて `~/.opencode/bin/opencode`）、`OPENCODE_TIMEOUT`（セグメントあたりの秒数、デフォルトは 600）。`OPENCODE_CONFIG` はそのまま OpenCode に渡されます。

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

`reasoningEffort: "none"` は、Ollama がこれらのモデルでデフォルトで有効にし、Modelfile では無効化できない思考（reasoning）を無効化します。6単語の文での実測値：オプションなしでは 919 思考トークンで 68 秒、オプションありでは 9 トークンでした。

### 400以上のモデル向け：`--use_openrouter`

OpenRouter は、単一のクレジット残高から従量課金でサードパーティがホストするモデル（他では提供されていない中国発のオープンモデルを含む）を利用できるルーターです。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` は必須です。課金が発生する前に実行される事前チェック（プリフライト）により、ルーティングにおける2つの特性が処理されます：

- **同一モデルが上限の異なる数十のホストから提供されている** — `z-ai/glm-5.3-flash` では 23 のホストがあり、中には出力が 2,048 トークンに制限されているものもあります。事前チェックは `/api/v1/models/{modèle}/endpoints` を読み取り、出力が 8,000 トークン未満またはステータスが低下しているホストを除外し、それ以外のホストを `allow_fallbacks: false` で固定します。
- **思考（推論）は出力レートで課金される** — `z-ai/glm-5.2` の「OK」という応答に対して 2 トークンではなく 107 トークン消費されます。デフォルトでは無効化されています。思考を強制するモデルには許容される最低限の effort が設定されます（カタログのデフォルトでは翻訳完了前に出力を使い果たす可能性があるため）。`--reasoning_effort` が常に優先されます。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- コンテキストウィンドウはカタログから取得されます。16,400 トークン未満のモデルは呼び出し前に拒否されます（プロンプトとセグメント用に 8,400、最小出力用に 8,000）。
- カタログに存在しないスラッグ、カタログに接続できない場合、または上限を満たすホストが存在しない場合はコマンドが停止します。
- 出力が空の `finish_reason=length` は、切り捨てではなく思考によって予算を使い果たした状態であり、メッセージで区別されます。
- `--eco` は効果がありません。
- 環境変数：`OPENROUTER_API_KEY` (<https://openrouter.ai/keys>)、`OPENROUTER_BASE_URL`（デフォルトは `https://openrouter.ai/api/v1`、`https://` 必須）、`OPENROUTER_TIMEOUT`（デフォルトは 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（デフォルトは 30）。

### 翻訳メモ

`--add_translation_note` はメモを追加します。位置は `bottom`（デフォルト）、`top`（front matter の後）、または `both`（`--note_position`）から選択でき、フォーマットは `legacy`（太字の段落、デフォルト）または `marker`（`--note_format`）を指定できます。`marker` フォーマットは不可視の Markdown 参照定義 `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"` とそれに続く太字の引用で構成され、GitHub 上で閲覧可能であると同時に、remark プラグインによるビルド時の処理にも利用できます。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 詳細な測定結果

すべての測定値は、`aipmt` を使用して14言語（en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi）へ実際に実行された翻訳に基づいています。**書き込み済み（Écrites）**はガードチェックを通過したファイル数をカウントし、**差分なし（Sans écart）**は `scripts/compare_structure.py` で差異が検出されなかったファイル（セクション数、小見出し数、リンク数、個別 URL 数、コードブロック数、インラインコード数、テーブル行数、引用ブロック数、太字語数が同一）をカウントしています。

「差分なし」は「何も検出されなかった」ことを意味し、「完全に同一」を意味するわけではありません。比較ツールは内容を読み取ることなく要素の数をカウントします。削除されたレベル 4 の見出しや、置き換えられたインラインコードのテキスト、入れ替わったフラグなどを検出することはなく、言語の質を評価することもありません。

### 高密度な情報ウォッチ記事、`--news` モード

[jls42.org の AI 動向ウォッチ](https://jls42.org/fr/news)の 1 エディション：
589 行、140 個のリンク、21 セクション、3 件の保護された英語の引用。2026 年 9 月 4 日・5 日の計測キャンペーン。

| モデル                                          | アクセス              | 出力完了 | 差異なし   | 中央値/言語 |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14** | 1 分 18 秒     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google サブスクリプション  | 14/14   | ✅ **14/14** | 3 分 14 秒     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT サブスクリプション | 14/14   | ✅ **14/14** | 11 分 28 秒    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 分 37 秒     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 分 23 秒    |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 分 31 秒     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 分 27 秒     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 分 09 秒    |
| `ollama/gpt-oss-20b-32k`                        | ローカル              | 10/14   | ❌ 7/14      | 12 分 39 秒    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14      | 5 分 32 秒     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 分 27 秒    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok サブスクリプション    | 1/14    | ❌ 1/14      | 23 分 11 秒    |

Grok は 9 月 9 日に同じウォッチ記事の別エディション（356 行）で再計測されました。14 言語中 9 言語が出力され、8 言語で差異がありませんでした。冒頭の表に記載されているのはこの数値です。中断された 3 つのキャンペーンは記載されていません：クレジット不足による `qwen3.5-27b`（9 言語）および `kimi-k2.6`（4 言語）、プロバイダがその後修正した推論設定に 2 件の失敗の原因があった `z-ai/glm-5.3-flash`。OpenRouter の各行は `--use_openrouter` 前のルーターのデフォルト設定で計測されました。同梱のプロバイダで再計測された `z-ai/glm-5.2` は、同様に 14/14 を返しています。数値は 9 月 10 日に現在の比較ツールで再計算されました。初版公開時と比べて `qwen3.8-flash` と `qwen3.7-flash` がそれぞれ 1 言語獲得し、その他は変更ありません。

`--use_antigravity` の行は 9 月 26 日に同じ記事で並行して 4 つの翻訳を実行して計測されました。英語では、モデルはフラグを捏造することなく引用下の 3 行のフランス語翻訳を自ら削除し、英語の引用も損なわれませんでした。フォールバックのクリーンアップ処理は何も行う必要がありませんでした。`--eco`（`gemini-3.7-flash-low`）では、4 言語（en、ja、ar、hi）のみを対象に、4 言語中 4 言語を出力し、すべて差異なし、中央値 1 分 52 秒でした。

### 本プロジェクトの README、標準的な Markdown

2026 年 9 月 9 日に固定されたリビジョン：785 行、285 個のインラインコード、40 個のコードブロック閉じタグ、89 行のテーブル。並行して 4 つの翻訳を実行。

| モデル                                          | 出力完了 | 差異なし | 中央値/言語 | 相違点                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 秒           | 太字の単語 1 つ (ja)                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 分 22 秒     | 太字の単語 1 つ (ko)                                                      |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 分 56 秒     | リンク 1 つ (sv)、太字の単語 1 つ (zh)                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 分 46 秒     | 太字の単語 1 つ (ar, ja)                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 分 34 秒     | 太字の単語 1 つ (hi, ja, ko)                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 分 17 秒     | アラビア語で 40 個のインラインコード追加、太字 (hi, ja, ko)                   |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 分 44 秒     | セクションの欠落 1 箇所 (ar, hi, ko)、コードブロックの追加 (ja, ko, ro, zh) |

中断された 2 つのキャンペーンは記載されていません：12 言語（うち 11 言語は差異なし）の後に CLI セッションが期限切れとなった Grok、および 2 言語の後にホスト元から HTTP 429 を返された `qwen3.8-flash` です。`opencode/mimo-v2.5-free` と `ollama/gpt-oss-20b-32k` はこのリビジョンでは再計測されていません。277 行短い 9 月 4 日・5 日のリビジョンでは、それぞれ 14 言語中 9 言語の翻訳を出力し、差異がなかったのはそれぞれ 7 言語と 1 言語でした。

`--use_antigravity` の行は固定リビジョンではなく、9 月 26 日に 1.14.0 でリリースされたリビジョン（600 行、257 個のインラインコード、30 個のコードブロック閉じタグ、85 行のテーブル）で計測されました。185 行短いため、他の行と直接比較することはできません。

### 著名プロジェクトの 4 つの README

FastAPI、Ollama、tldr-pages、Vue.js を GitHub からそのまま取得したものです。これらは前の 2 つよりも容易なドキュメントです。この計測キャンペーンは困難を抱えるモデルを対象としており、Gemini は比較の基準点として使用されています。

| モデル                    | 範囲                  | 出力完了 | 差異なし   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 プロジェクト × 14 言語     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 プロジェクト × 14 言語     | 55/56   | ❌ 47/56     |
| `grok-4.6` (サブスクリプション)   | 4 プロジェクト × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 プロジェクト × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### これらの計測が意味しないこと

- **網羅的なランキングではない**：OpenRouter だけでも 400 以上のモデルが提供されていますが、計測されたのは 15 程度です。
- **所要時間はあくまで目安**：キャンペーンに応じて 3〜6 つの並行翻訳を行っており、プロバイダのスループットは時間帯によって変動します。
- **特定時点の観測結果である**：同じモデル名でも中身が変更されることがあり、皆様のドキュメントは今回のものとは異なります。

お持ちのドキュメントで、ファイルの固定コピーを使って測定を再現するには：

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

両方の行が必要です。`pip install -e .` がないと、`python -m aipmt` は `No module named aipmt` を返します。

品質関連ツール（オプションですが推奨）：

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

リポジトリ内の 28 件の翻訳（14 言語の README および CHANGELOG）は、`./regen_translations.sh --force` で再生成されます。デフォルトでは ChatGPT サブスクリプション上の Codex と `gpt-5.6-sol` を使用し、4 つ並行で実行されます。`REGEN_PROVIDER` と `REGEN_MODEL` で実行パスを変更できます。`antigravity` はサブスクリプション（Google のもの）にとどまり、例外設定なしでパスします。従量課金制 API（`openai`、`gemini`、`grok`、`openrouter`）は `REGEN_ALLOW_PAID_API=1` がないと拒否されます。`REGEN_JOB_TIMEOUT` は各ジョブの上限を設定します（通常 600 秒、Codex および Antigravity では 1,800 秒）。ツールの詳細は `CLAUDE.md` に記載されています。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** — 15 言語で公開されている個人ブログ。その[毎日の AI 動向ウォッチ](https://jls42.org/fr/news)はこのツールによって毎日翻訳されており、上記の計測における参照ドキュメントとして使用されています。

## 著者

Julien LE SAUX
メール：contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。[LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE) を参照してください。

## 免責事項

本プログラムは、GPL v3 の第 15 条および第 16 条の条件に基づき、**いかなる保証もなく**配布されます。商品性や特定目的への適合性の保証を含めず、「現状有姿」で提供され、その作者はいかなる使用に起因する損害に対しても責任を負いません。本要約よりもライセンス本文が優先されます。

- **公開前に必ず見直してください。** 保護の対象となるのは、コードブロック、インラインコード、URL、アンカー、および `--news` モードの引用です。見出し、テーブル、Front Matter、文の意味自体は保護対象ではありません。
- **ドキュメントは選択されたプロバイダに送信されます**。各プロバイダの利用規約およびデータポリシーに従います。一部の無料モデルはお客様のやり取りをトレーニングに再利用する場合があり、Antigravity の利用規約では有料サブスクリプションを含め、Google がデータを再利用したり人手によるレビューを行ったりすることが許可されています。ローカルモデルのみが、マシンから外部へデータを一切送信しない唯一の方法です。
- **API 呼び出しには料金が発生します。** 本プログラムは利用料金の上限を設定しません。長いドキュメント、失敗後のリトライ、あるいは推論量の多いモデルはコストが高くなります。
- **公開されている測定結果は特定時点の観測結果であり**、保証ではありません。

記載されている製品名および会社名は、それぞれの所有者に帰属します。本プロジェクトはいずれの企業とも提携していません。

**gemini-3.7-flash-mediumでフランス語から日本語に翻訳された記事。**
