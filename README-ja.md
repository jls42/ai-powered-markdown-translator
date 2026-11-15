# AI駆動Markdown翻訳ツール

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

コードブロック、インラインコード、URL、アンカー、表、front matterなどの構造を保持したまま、Markdownファイルをある言語から別の言語へと翻訳します。モデルの呼び出し方法は11通り（5つのAPI、従量課金なしの4つのサブスクリプション、2つのルーター）あり、各モデルが実際に何を保持できるかの測定結果も公開しています。

## 概要

- **11種類のプロバイダーパス**：OpenAI、Mistral、Claude、Gemini、GrokのAPI。従量課金なしのChatGPT（Codex）、Grok、Google（Antigravity）、Claude（Claude Code）サブスクリプション。OpenCode（オープンソース、無料またはローカル）およびOpenRouter（400以上のモデル）ルーター。
- **トークン欠落による破損を防止**：コードブロック、インラインコード、URL、アンカー、引用は呼び出し前にトークンへ置換され、応答時に検証されます。1つでも欠落している場合、ファイルは書き込まれません。
- **長文ドキュメント**：モデルのコンテキストウィンドウに応じてセグメント分割。
- **`--news`モード**：技術情報キュレーション記事向けに、英語の引用を保護し、言語ごとのフラグを管理。
- **`--eco`モード**：高速かつ低コストなモデルを使用。
- **翻訳メモ**：先頭、末尾、またはその両方にオプションで追加可能。

## インストール

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11以降。リポジトリからのインストール方法については、[貢献する](#貢献)を参照してください。

## 設定

キーは優先度の高い順に3つの場所から読み込まれ、前の場所で設定されていない項目のみが次の場所で補完されます。

|     | 場所                                          | 用途                                  |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 環境変数                                      | CI、コンテナ、一時的な上書き          |
| 2   | カレントディレクトリ（または親ディレクトリ）の `.env` | プロジェクト固有のキー                |
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

`GOOGLE_API_KEY` の代わりに `GEMINI_API_KEY` も受け入れられます。ユーザー設定ファイルは `XDG_CONFIG_HOME`（絶対パスのみ）およびWindowsでは `%APPDATA%` に従います。キーが存在しない場合、コマンドは3つの場所を一覧表示します。

**プロジェクトの `.env` では、呼び出し先のリダイレクトや実行プログラムの選択は行えません。** 設定できるのはキーのみであり、接続先やバイナリは指定できません。`_BASE_URL`、`_API_BASE`, `_ENDPOINT`、または `_BIN` で始まるすべての変数（`CODEX_BIN`、`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`）、`GROK_HOME`、プロキシ（`HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY`）、証明書ストア（`SSL_CERT_FILE`、`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）、および `XDG_CONFIG_HOME` / `APPDATA` は警告とともに対象外となります。クローンしたリポジトリによってキーが傍受されたり、初回の翻訳時に独自のプログラムを実行させられたりするのを防ぐためです。また、このファイルは変数展開を行わずに読み込まれるため、`NOM=${OPENAI_API_KEY}` でキーがコピーされることもありません。これらの変数は環境変数または `~/.config/aipmt/.env` で設定してください。

オプションの変数：`XAI_BASE_URL`（デフォルト `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（1呼び出しあたりの秒数、デフォルト 900）、`CODEX_BIN`、`CODEX_TIMEOUT`（デフォルト 600）、`GROK_BIN`、`GROK_HOME`（デフォルト `~/.grok`）、`GROK_TIMEOUT`（デフォルト 900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（デフォルト 900）、`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（デフォルト 600）、`OPENROUTER_BASE_URL`（`https://` 必須）、`OPENROUTER_TIMEOUT`（デフォルト 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（デフォルト 30）。各変数の詳細はプロバイダーごとのセクションで説明されています。

## はじめに

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` をスペイン語に翻訳すると、`--target_dir` 内に `document-es.md` が生成されます。`--include_model` を指定した場合は `document-es-gpt-6.1-terra.md` となります。元のファイル名を保持する `--keep_filename` を除き、拡張子は常に `.md` に変換されます（例：`article.mdx` は `article-en.md` になります）。すでに存在する翻訳は、`--force` が指定されていない限りスキップされます。

終了コード：すべて成功またはスキップされた場合は `0`、失敗したファイルが残っている場合は `1`（標準エラー出力に一覧表示）、設定に問題がある場合は `2` です。失敗したファイルが書き込まれることはなく、書き込み処理自体が失敗した場合でも同様です（内容は一時ファイルとして別名で書き込まれてからリネームされます）。再実行するだけで対応できます。

## どのモデルを選ぶべきか

実際の2つのドキュメントを使用し、各モデルで同一の14言語に翻訳して測定しました。**数値は、14言語中、翻訳が出力され、かつ原文からの差異が一切なかった言語の数です。**

| モデル                | アクセス方法                      | 密度の高い技術情報記事 | このREADME    | 差異の内容と該当言語数                                                                                                                                             |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google サブスクリプション (Antigravity)   | ✅ 14/14                | ✅ 14/14     | 両ドキュメントとも差異なし                                                                                                                                         |
| **Claude Sonnet 5.5** | Anthropic API キー                 | ✅ 14/14                | ✅ 14/14     | 両ドキュメントとも差異なし                                                                                                                                         |
| **Gemini 3.7 Flash**  | Google API キー                    | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語：太字が1語増加 (ja)                                                                                                                                  |
| **Gemini 3.7 Flash**  | Google サブスクリプション (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語：太字が1語減少 (ko)                                                                                                                                  |
| **GPT-5.6 Sol**       | ChatGPT サブスクリプション、または OpenAI キー | ✅ 14/14                | ⚠️ 12/14     | 14言語中2言語：太字が1語減少 (ar、ja)                                                                                                                             |
| **GLM-5.2**           | OpenRouter キー                    | ✅ 14/14                | ⚠️ 11/14     | 14言語中3言語：太字が1語減少 (hi、ja、ko)                                                                                                                          |
| Claude Sonnet 5       | Claude サブスクリプション (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 記事で14言語中1言語：太字が1語増加 (zh)；このREADMEで1言語：表の行が前の行と結合され表示が崩れる (ar)                                                             |
| Claude Haiku 4.5      | Claude サブスクリプション (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 記事で3言語：セクション見出しがレベル1に変更 (en、pl、ro)；このREADMEでは比較ツール上は差異なしだが、内部リンクが英語で重複                                        |
| Claude Sonnet 5       | Anthropic API キー                 | ⚠️ 11/14                | ⚠️ 12/14     | 記事で3言語：余分なコードブロックが出現 (es、de、hi)；このREADMEで2言語：リンク記法が欠落したリンク (sv)、太字が1語 (zh)                                         |
| Claude Haiku 4.5      | Anthropic API キー                 | ⚠️ 7/14                 | ✅ 14/14     | 記事で7言語：セクション見出しがレベル1に変更（日本語ではフランス語のまま残存）；このREADMEでは差異なし                                                           |
| Claude Haiku 5.5      | Anthropic API キー                 | ⚠️ 11/14                | ❌ 12/14     | 記事で3言語：セクション見出しのレベル変更または重複 (ja、ko、zh)；このREADMEで2言語拒否、インラインコードの欠落 (ar、hi)                                           |
| Qwen 3.7 Flash        | OpenRouter キー                    | ❌ 8/14                 | ⚠️ 10/14     | 記事で1言語拒否、他の5言語で乖離；このREADMEで約40語が `code` 化 (ar)                                                                                      |
| Grok 4.6              | Grok サブスクリプション                   | ❌ 8/14                 | 評価なし     | 14言語中5言語拒否（インラインコードとURLが出力されなかったため）；オランダ語で全面的な乖離                                                                        |
| GPT-OSS 20B           | ローカルモデル (Ollama)             | ❌ 7/14                 | 再測定なし | 14言語中4言語拒否：フランス語の文章がそのまま残ったためガード機能が停止                                                                                            |
| MiMo v2.5 (gratuit)   | OpenCode Zen、アカウント不要         | ❌ 11/14                | 再測定なし | 1言語拒否；ポーランド語で1セクションが消失                                                                                                                         |
| Mistral Large         | Mistral API キー                   | ❌ 5/14                 | ❌ 1/14      | **セクション全体が消失**：記事で1言語 (hi)、このREADMEで3言語 (ar、hi、ko) — さらに記事で3言語拒否                                                               |
| DeepSeek V4 Flash     | OpenRouter キー                    | ❌ 3/14                 | 再測定なし | 14言語中10言語拒否；1言語あたり37分                                                                                                                                |
| Claude Opus 5.5       | Claude サブスクリプション (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | 生物学の短いニュースが原因でOpusのガードレールに引っかかり、記事は14言語すべてで拒否；このREADMEでは差異なし                                                        |

|     | 記号の意味                                                                                                                                                                                           |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14言語すべてが翻訳され、原文からの差異が一切ない                                                                                                                                                     |
| ⚠️  | 14言語すべてが翻訳されたが、**マークアップ**に差異がある（太字の語、`code`、角括弧が欠落したリンクなど）。テキスト、URL、コードブロック、セクションの欠落はない                             |
| ❌  | 少なくとも1つの言語が翻訳できなかった（ファイルが拒否され書き込まれなかった）、**または**書き込まれたファイルにコンテンツの欠落がある                                                               |

留意すべきポイント：

- **拒否された翻訳は、破損した翻訳とは異なります。** 応答時にトークンが欠落していた場合、ファイルは書き込まれず、その言語は「拒否」としてカウントされます。これは記事のテストでGrokに起きた現象で、非ラテン文字を使用する5言語において、最初のセグメントから4つのインラインコードと3つのURLが消失しました。
- **モデルによっては、たった1文が原因でドキュメント全体を拒否することがあります。** Opus 5.5 はこのREADMEを一切の差異なく翻訳しますが、技術情報記事はまったく翻訳できません。生物学関連の短いニュースに対して安全ガードレールが働き、応答を停止してしまうためです。ファイルは書き込まれず、aipmtがその理由を表示します。
- **この保護機能は見出し、表、front matter、本文テキストには適用されません。** セクションを丸ごと削除してしまうモデルであっても、ツールはそのままファイルを出力してしまいます（Mistralがこれに該当します）。これらの要素はトークンに置き換えることができず、現在のガード機能では検査されません。`scripts/compare_structure.py` は消失したセクションを検出できますが、事後チェックとなります。
- **このREADMEにおけるGrokの評価はありません**：12言語を処理した時点でCLIセッションの有効期限が切れました（そのうち11言語は差異なし）。中断されたテストは評価対象外としています。
- **言語よりもドキュメントの密度が大きく影響します。** Grokは一般的なREADMEでは安定していますが、リンクが密集した記事ではオランダ語を含めて失敗します。

実施日とドキュメント：「このREADME」列は、2026年9月9日に本ファイルの固定リビジョン（785行、インラインコード285個、表89行。以降更新あり）で測定されました。ただし、AntigravityおよびClaude Codeの行は9月26日に1.14.0で公開された短いリビジョン（600行、インラインコード257個、表85行）で測定され、API経由のClaude Sonnet 5.5、Haiku 5.5、Haiku 4.5の行は10月18日に同一リビジョンで測定されました。「密度の高い技術情報記事」列は、9月4日〜5日に実施された589行の記事テストに基づきます。ただし、Grokの行は9月9日に同技術情報の別エディションで再測定され、AntigravityおよびClaude Codeの行は9月26日に同一記事で、Claudeの上記3モデルは10月18日に測定されました。詳細な表、所要時間、プロトコルについては[詳細な測定結果](#詳細な測定結果)を参照してください。

## すべてのオプション

| オプション               | 説明                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | 翻訳する単一のMarkdownファイル（`--source_dir`の代替）                                                         |
| `--source_dir`           | Markdownファイルを含むソースディレクトリ（デフォルト: `content/posts`）                                        |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ（デフォルト: `traductions_en`）                                              |
| `--source_lang`           | ソース言語（デフォルト: `fr`）                                                                      |
| `--target_lang`           | ターゲット言語（デフォルト: `en`）                                                                   |
| `--model`           | 使用する特定のモデル                                                                                          |
| `--eco`           | 低コストモデルを使用                                                                                          |
| `--use_mistral`           | Mistral AI APIを使用                                                                                          |
| `--use_claude`           | Claude APIを使用                                                                                              |
| `--use_gemini`           | Gemini APIを使用                                                                                              |
| `--use_grok`           | xAI (Grok) APIを使用 — `XAI_API_KEY`が必要                                                                   |
| `--use_codex`           | ChatGPTサブスクリプションのクォータでCodex CLIを使用                                                          |
| `--use_grok_cli`           | GrokサブスクリプションのクォータでGrok CLIを使用                                                              |
| `--use_antigravity`           | Google AI ProまたはUltraサブスクリプションのクォータでAntigravity CLI（`agy`）を使用                 |
| `--use_claude_code`           | Claude ProまたはMaxサブスクリプションのクォータでClaude Code CLI（`claude -p`）を使用                      |
| `--use_opencode`           | OpenCode（オープンソース）で設定されたプロバイダーを使用。`--model provider/modèle`が必要                                 |
| `--use_openrouter`           | OpenRouterを使用 — `OPENROUTER_API_KEY`および`--model fournisseur/modèle`が必要                                                    |
| `--force`           | 再翻訳を強制                                                                                                  |
| `--keep_filename`           | 元のファイル名を保持                                                                                          |
| `--news`           | ニュースモード: 英語の引用を保護し、言語別の国旗を処理                                                        |
| `--add_translation_note`           | 翻訳注記を追加                                                                                                |
| `--note_position`           | 注記の位置: `top`、`bottom`（デフォルト）、または`both`                                |
| `--note_format`           | 注記の形式: `legacy`（デフォルト、太字段落）または`marker`                                      |
| `--include_model`          | 出力ファイルにモデル名を含める                                                                                |
| `--reasoning_effort`          | GPT-5.xの推論エフォート: `none`/`low`/`medium`/`high`/`xhigh`     |

9つの`--use_*`フラグは相互に排他的です。2つを同時に指定することはできません。

## プロバイダー

### API経由: OpenAI、Mistral、Claude、Gemini、Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco`は各プロバイダーの低コスト層に切り替えます。

| プロバイダー | 高品質（デフォルト）                                                 | エコノミー（`--eco`）     |
| ------------ | -------------------------------------------------------------------- | --------------------------------- |
| OpenAI       | `gpt-6.1-terra`                                                      | `gpt-6-luna`                   |
| Claude       | `claude-sonnet-5-5`                                                      | `claude-haiku-5-5`                   |
| Mistral      | `mistral-large-latest`                                                      | `mistral-small-latest`                   |
| Gemini       | `gemini-4-hydrogen`                                                      | `gemini-3.1-flash-lite`                   |
| Codex        | `gpt-6.1-sol`（`--model`経由で`gpt-5.6-sol`、`terra`、`luna`も利用可能） | `gpt-6-luna`                   |
| Grok API     | `grok-4.7`                                                      | `grok-4.3`                   |
| Grok CLI     | `grok-4.7`                                                      | 同上 — `--eco`は効果なし  |
| Antigravity  | `gemini-3.8-flash-medium`                                                      | `gemini-3.8-flash-low`                   |
| Claude Code  | `sonnet`、エフォート `low`                          | 同上 — `--eco`は効果なし  |
| OpenCode     | `--model provider/modèle`必須                                                  | 同上 — `--eco`は効果なし  |
| OpenRouter   | `--model fournisseur/modèle`必須                                                  | 同上 — `--eco`は効果なし  |

デフォルト設定は各プロバイダーの最新世代に追従しており、採用前に測定が行われています。1.19.0以降、OpenAIのGPT-6、GoogleのGemini 4 Hydrogen、xAIのGrok 4.7が該当します。以前のモデル（`gpt-5.6-terra`、`gemini-3.8-flash`、`grok-4.6`…）や、GoogleのハイエンドモデルであるGemini 4 ArgonおよびCarbonも、`--model`で使用可能です。aipmtはGPTおよびGrokの推論エフォートを自動で調整し（`--eco`ではオフ）、`--reasoning_effort`で強制指定できます。Geminiには、常に受け付け可能な最低レベルが設定されます。
Gemini APIの一時的な障害（503、429、タイムアウト）が発生した場合、10秒、20秒、40秒の間隔を空けて最大3回まで再試行されます。応答のない試行は5分で中止され、同様に再試行されます。サーバーが無応答の場合でも、無期限にブロックされることなく、最大約20分でそのセグメントは失敗となります。

### ChatGPTサブスクリプション経由: `--use_codex`

公式のCodex CLIを制御します。翻訳はAPIキーや従量課金なしで、ChatGPTサブスクリプションのクォータから差し引かれます。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- バイナリは`CODEX_BIN`、次いで`PATH`、そしてパッケージ`openai-codex-cli-bin`の順で検索されます。`~/.codex/auth.json`は読み込まれません。
- サブプロセスの環境から`OPENAI_API_KEY`および`CODEX_API_KEY`が削除されるため、キーが存在していてもAPIに切り替わることはありません。
- 各セグメントは、5時間枠の「メッセージ」を少なくとも1回分消費します（検証に失敗して再試行された場合は2回分）。OpenAIの概算によると、Plusプランでは1.18.0までのエコモデルである`gpt-5.6-luna`で5時間あたり250〜2,000メッセージ、`gpt-5.6-sol`で10〜100メッセージとされています。
- 1.16.3までのデフォルトだった`--model gpt-5.6-sol`、ならびに`--model gpt-5.6-terra`と`--model gpt-5.6-luna`もサブスクリプション経由で動作します。
- サーバーから429が返されてもファイルが失われることはありません。Codexが自動的に再接続し、aipmtはターンの終了を待ちます。それでも429が解消されない場合、セグメントは30秒後、次いで60秒後に再試行されます。アカウントに権限のないモデルの場合は、400「model is not supported when using Codex with a ChatGPT account」が返されます。
- APIよりも低速で、ドキュメントが大きくなるほどその差は広がります。このREADMEの場合、`gpt-5.6-sol`での中央値は言語あたり6分46秒ですが、`gemini-3.7-flash`では36秒です。
- CIでは拒絶されます（`CI`または`GITHUB_ACTIONS`が設定されている場合）。サブスクリプションの認証には個人のセッションファイルが使われるため、共有ランナー上に配置すべきではないからです。
- 環境変数: `CODEX_BIN`、`CODEX_TIMEOUT`（セグメントあたりの秒数、デフォルトは600）。

### Grokサブスクリプション経由: `--use_grok_cli`

SuperGrokまたはX Premium+サブスクリプション上の公式Grok Build CLIでも同様の仕組みです。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Codexよりも制限が緩い隔離。** GrokのOSサンドボックスは、近年の多くのLinux環境（AppArmor、コンテナランタイムソケット）には適用されず、適用できないプロファイルは警告なしに非サンドボックス状態で起動します。そのため、スクリプトはデフォルトでプロファイルを要求せず、その旨を通知した上で、CLIの`--deny`ルール（キャッチオールである`*`を含む）に依存します。これは、無告知で保護を解除するのではなく起動を拒否する唯一のレイヤーです。`GROK_TRANSLATE_SANDBOX=read-only`はOSサンドボックスを必須とし、マシンがそれに対応できない場合は起動に失敗します。
- クォータは週間単位で、Chat、Imagine、Voiceと共有されており、それを確認するコマンドはありません。バッチ処理を実行すると、事前の警告なしに対話機能の利用枠を消費する可能性があります。
- 環境変数: `GROK_BIN`、`GROK_HOME`（CLIのディレクトリ、デフォルト: `~/.grok`）、`GROK_TIMEOUT`（デフォルト: 900）、`GROK_TRANSLATE_SANDBOX`。

### Googleサブスクリプション経由: `--use_antigravity`

Antigravityの公式CLIである`agy`でも同様の仕組みです。Google AI ProまたはUltraに加入している場合、翻訳はトークン単位で課金される代わりにサブスクリプションのクォータから差し引かれます。これがこのクォータを利用する唯一の手段です。Gemini CLIは2026年6月18日以降これらのアカウントへの対応を終了しており（[告知](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)）、AntigravityのSDKはAPIキーまたはGoogle Cloudプロジェクトしか受け付けません。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **有料経路はすべて遮断されています。** agyは環境変数から限定されたリスト（`PATH`、言語およびタイムゾーン、ターミナル、ID情報、プロキシおよび証明書、セッションバス）のみを受け取り、キーは一切受け取りません。agyの一部の変数は警告なく呼び出しを切り替えてしまうため（実測: ある変数はサードパーティのゲートウェイにドキュメントを送信し、別の変数は有料のGoogle Cloudプロジェクトに送信）、ブラックリスト方式では見落としが生じていました。いかなるセグメントの処理前にも、クォータを消費しない`agy -p /config`を実行し、有料のAIクレジットが無効化され、APIキーもGoogle Cloudプロジェクトも設定されていないことを確認する必要があります（設定が存在しない場合は拒絶）。これらが満たされない限り翻訳は行われません。さらに、各呼び出しのログでサブスクリプション（`authMethod=consumer`）が確認できなければ、応答は拒絶されます。
- **サンドボックス環境。** 各呼び出しはツールを持たない翻訳エージェントとともに、使い捨てのプライベートなホームディレクトリ内で実行されます。agyの設定、ルール、プラグイン、MCPサーバー、フックは読み込まれず、履歴にも何も追加されません。また、認証情報はキーチェーン内に保持され、aipmtがそれを読み取ることは決してありません。エージェントが見つからない場合、agyは警告なしにコーディングエージェントとそのツールにフォールバックします。そのため、ログの1行全体で正しいエージェントであることが確認されなければ（このメッセージを引用したドキュメントでは代用不可）、処理は拒絶されます。
- **プラットフォーム**: キーチェーン（D-Busセッションバス、Secret Service）を備えたセッション下のLinux。macOSも受け付けられますが、未測定です。各呼び出しを隔離する変数をagyが読み取らないWindowsや、セッションバスのないLinux（SSHセッション、コンテナ、サーバーなど）では拒絶されます（agyはトークンを`~/.gemini`内のファイルに保存しますが、隔離によってそれが見えなくなるため）。ログインコードを1分間待たされる代わりに、起動前に理由とともに拒絶されます。
- **モデル**: `agy models`で提供されているもの。Geminiモデルは名前にエフォートレベルが含まれており（`gemini-3.8-flash-medium`…）、サフィックスのない名前は呼び出し前に拒絶され、`--reasoning_effort`は効果がありません。agyがGemini 3.7 Flashの提供を終了して以来、デフォルトは`gemini-3.8-flash-medium`、`--eco`時は`gemini-3.8-flash-low`です。このデフォルトを決定した検証については[詳細な測定結果](#詳細な測定結果)に記載されています。Gemini 4 Hydrogen（`gemini-4-hydrogen-low`…）は3.8 Flashとクォータを共有しますが、消費量はより多くなります（このREADMEの場合、中エフォートで5時間枠の0.95ポイントを消費、Flashでは0.32）。ClaudeとGPT-OSSには独自の、はるかに小さなクォータが設定されており、測定された呼び出し1回につき5時間枠の約1%を消費します（Flashでは0.05%）。Gemini 4 Argonには独自の週間クォータがあり、このREADMEで1.35%を消費します。
- **クォータ**: グループごとにトークンコストに比例した5時間枠と週間枠があります。作者のアカウントでの測定では、ソース文字数100万文字あたり、`gemini-3.8-flash-medium`で5時間枠の約16ポイント、`gemini-3.7-flash-medium`で14ポイント、低エフォートで7〜8ポイントでした。したがって、40,000文字のREADMEは約0.5ポイント強を消費します。週間制限はプランのティアによって異なります。再試行はagyがリトライ可能と宣言したものに従います。それ以外の場合、枠が枯渇しても再試行されることはなく、`/usage`に表示されるリセット時刻まで各ファイルは失敗します。
- **APIよりも低速**: 測定用の高密度な記事において、言語あたりの中央値は`gemini-3.8-flash-medium`で3分59秒、`gemini-3.7-flash-medium`で3分14秒でした（API経由のGemini 3.7 Flashでは1分18秒）。
- **中断**: Ctrl-Cの入力やターミナルの終了によって、agyはコマンドとともに停止し、クォータを消費してターンを完了することはありません。これはCodex、Grok CLI、OpenCodeでも同様です。`nohup`下では、翻訳が継続されます。
- CIでは拒絶されます（`CI`または`GITHUB_ACTIONS`が設定されている場合）。認証情報は個人のキーチェーンに保持されるためです。ランナー上では、`GOOGLE_API_KEY`とともに`--use_gemini`を使用してください。
- 環境変数: `AGY_BIN`（未指定時は`PATH`、次いで`~/.local/bin/agy`）、`AGY_TIMEOUT`（起動時間を含むセグメントあたりの秒数、デフォルト: 900）。

**利用規約: 自己責任での利用となります。** [Antigravityの利用規約](https://antigravity.google/terms)（セクション6）およびその[FAQ](https://antigravity.google/docs/faq/)では、Antigravityの認証情報を用いてサードパーティ製ソフトウェア経由でサービスにアクセスすることを禁止しており（Claude Code、OpenClaw、OpenCodeが明記されています）、違反した場合はアカウント停止の対象となります。aipmtはトークンを読み取ったり再利用したりしません。GoogleがスクリプトやCI向けにドキュメント化している[ヘッドレスモード](https://antigravity.google/docs/cli/headless/)で公式バイナリを実行します。Googleの担当者は、自身の作業のためにローカルスクリプトから`agy -p`を起動することを「標準的」と見なしていますが（[公式フォーラム、2026年9月25日、法的拘束力のない回答](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）、本ツールのように配布されるツールに関する明確な規定はありません。

**公開ドキュメント専用。** 同規約のセクション5によると、有料サブスクリプションを含め、やり取り（プロンプト、応答、メタデータ）はGoogleの製品や機械学習の改善に利用され、人間のレビュアーによって確認される可能性があります。オプトアウトには設定`enableTelemetry`を使用しますが、その効果は文書化されておらず、aipmtがこれを設定することはありません。また、お客様独自のagy設定は隔離環境には引き継がれません。機密情報は絶対に処理させないでください。

### Claude サブスクリプションでの利用：`--use_claude_code`

Claude Code の公式 CLI である `claude` を `-p` モードで使用する場合も同じ原理です。Claude Pro または Max の有料プラン契約者の場合、翻訳はトークンごとに課金されるのではなく、サブスクリプションのクォータから差し引かれます。従量課金制である Anthropic の API `--use_claude` と混同しないようにしてください。

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **課金経路は一切開かれたままにならず、各呼び出しがそれを証明します。** Claude Code は環境から限定された変数のリストのみを受け取ります。API キー、トークン、クラウドプロバイダー、aipmt の起動元となった Claude Code セッションのマーカーなどは一切渡されません。最初のセグメントの前に、`claude auth status` は Console キーなしのサブスクリプション接続を表示する必要があり、クォータを消費しない `/usage` がそれを証明しなければなりません。各呼び出しも初期化イベントでそれを順次証明し、そうでなければ応答は拒否されます。
- **0 ユーロを維持するために「extra usage（追加利用）」を無効化してください**（claude.ai の 設定 → 使用状況）。有効になっていると、ウィンドウを使い果たした際に引き継がれ、エラーを表示せずに課金されます。aipmt は呼び出しのクォータレポートがそれを検知するとすぐに翻訳を停止しますが、その呼び出し自体はすでにカウントされています。
- **Claude Code セッションと共有されるクォータ。** 各呼び出しは、5時間ウィンドウおよび週間ウィンドウの使用状況を報告します。通常の作業に必要なクォータを枯渇させないよう、80%（`AIPMT_CLAUDE_MAX_UTILIZATION`）を超えるとセグメントはそれ以上起動されません。
- **隔離環境。** 各呼び出しはツールなしで、プライベートな使い捨てディレクトリ内にて、カスタマイズ無効モードで実行されます。ユーザーの `CLAUDE.md`、プラグイン、フック、MCP サーバー、設定は一切読み込まれず、セッションからも何も保持されません。添付ファイルは遮断されます。ドキュメント内の `@chemin` はテキストのままであり、ファイルを開くことはありません（測定済み）。
- **モデル**：デフォルトは `sonnet`、エフォートは `low`、また `--eco` でも同様です。このパスでは `--eco` は何も変更しません。同一ドキュメントでの測定では、`haiku` は防ぎようのない推論を行うため 2 倍遅く、コストの削減幅はごくわずかで、さらに `opus` は生物学関連のコンテンツを拒絶します（次の項目参照）。どちらも `--model` からアクセス可能です。これらのエイリアスはそのファミリーの最新モデルに追従します。有料クレジットを消費するため、`fable` および `[1m]` のバリアントは拒否されます。`--reasoning_effort` はエフォートを調整しますが、翻訳においてそこから得られるものはなく、測定された推論はゼロまたはほぼ皆無です。
- **Opus は特定の生物学コンテンツを拒絶します。** そのガードレールは Sonnet よりも厳格であり、Anthropic のエラーメッセージには「can sometimes flag biology-research-adjacent work（生物学研究に関連する研究にフラグを立てることがあります）」と警告されています。実測結果：生成された 279 種類の分子に関するウォッチ記事の短文により、14 言語すべてで記事が拒否されました。何も書き込まれません。aipmt は途切れた応答を拒絶し、ガードレールの名称を示して `--model sonnet` を推奨します。
- CI（`CI` または `GITHUB_ACTIONS` が定義されている場合）および Windows（未測定）では拒否されます。
- 変数：`AIPMT_CLAUDE_BIN`（なければ `PATH`、次いで `~/.local/bin/claude`）、`AIPMT_CLAUDE_TIMEOUT`（セグメントあたりの秒数、デフォルトは 900）、`AIPMT_CLAUDE_MAX_UTILIZATION`（デフォルトは 0.8）、`CLAUDE_CONFIG_DIR`（Claude Code のアカウント。プロジェクトの `.env` から取得されることはありません）。作業ディレクトリは `XDG_CACHE_HOME/aipmt/claude-code` 配下（デフォルトは `~/.cache`）。

**利用規約：責任はお客様のアカウントに帰属します。**
[Claude Code の法的ページ](https://code.claude.com/docs/en/legal-and-compliance)
では、「an end user from signing in to the unmodified Claude Code binary with their own Claude subscription（エンドユーザーが自身の Claude サブスクリプションを使用して未変更の Claude Code バイナリにサインインすること）」は禁じられていません。aipmt が行うのはまさにこれで、公式バイナリを起動し、トークンを読み取ることは決してありません。しかし Anthropic は、「does not permit third-party developers […] to route requests through Free, Pro, or Max plan credentials on behalf of their users（サードパーティ開発者がユーザーに代わって Free、Pro、または Max プランの認証情報を介してリクエストをルーティングすることを許可しない）」としており、「including open-source projects（オープンソースプロジェクトを含む）」サードパーティ製ツールには API キーの使用を優先し、それらの利用を有料クレジットから差し引く権利を留保しています
（[Claude ヘルプ](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)）。
バイナリを起動する配布ツールに関するケースを明文化した規定は存在しません。

**データ**：Free、Pro、および Max アカウントでは、プライバシー設定で許可されている場合、Claude Code にもモデルのトレーニングが適用されます
（[データに関するページ](https://code.claude.com/docs/en/data-usage)）。aipmt はローカルにトランスクリプトを一切保持しません（`--no-session-persistence`）。機密情報は通さないでください。

### 任意のプロバイダーへの接続：`--use_opencode`

[OpenCode](https://opencode.ai) は、内部で設定されたプロバイダー（API キー、サブスクリプション、アカウント不要の無料モデルを提供する OpenCode Zen ゲートウェイ、またはローカルモデル）へルーティングするオープンソース（MIT）のコードエージェントです。ここでは Zen と Ollama の 2 つのルートについてエンドツーエンドの測定を行いました。

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

`--model` は必須です。これがない場合、OpenCode はやり取りがトレーニングに使用される可能性がある無料モデルにフォールバックしてしまいますが、その選択を勝手に行うことはありません。

各呼び出し時の分離環境：

- ユーザー設定よりも優先されるインライン設定により、すべてのツールが拒否されたエージェント `aipmt` を定義（`permission: { "*": "deny" }`）、セッション共有は無効、`--pure`、`--auto` は設定しない。
- 使い捨ての空の作業ディレクトリに `OPENCODE_DISABLE_PROJECT_CONFIG` と `OPENCODE_DISABLE_CLAUDE_CODE` を配置。これらがないと、OpenCode はカレントディレクトリの `AGENTS.md` や `~/.claude/CLAUDE.md` をプロンプトに挿入してしまいます。グローバルの `~/.config/opencode/AGENTS.md` は引き続き挿入されますが、OpenCode ではこれを除外することができません。
- 出力契約：リターンコード 0、`error` イベントなし、ツール呼び出しなし、最終ステップが `stop`、テキストが空でないこと、そして `aipmt` エージェントが実際に読み込まれていること。未知の `--agent` を指定しても OpenCode は失敗せず、コーディングエージェントにサイレントでフォールバックしてしまいます。
- OpenCode 自体のキーである `OPENCODE_API_KEY` を除き、`aipmt` のキーは一切渡されません。プロバイダーの設定は `aipmt` の `.env` ではなく、OpenCode 内で行います。

知っておくべきこと：

- Zen の無料モデルは変動しやすく、制限も文書化されておらず、やり取りがトレーニングに使用される可能性があります。公開ドキュメント向けであり、プライベートなコンテンツには適しません。
- セグメントは最大 16,000 文字に達するため、ローカルモデルは少なくとも 16k トークンのコンテキストを提供する必要があります。Ollama は多くの場合 4,096 トークンに設定されているため、`PARAMETER num_ctx 32768` を指定した `Modelfile` を介してください。
- `--eco` は効果がありません。`--reasoning_effort` はそのまま OpenCode の `--variant` として渡されます。
- OpenCode は各セッションを `~/.local/share/opencode/` にログ記録します。
- 変数：`OPENCODE_BIN`（なければ `PATH`、次いで `~/.opencode/bin/opencode`）、`OPENCODE_TIMEOUT`（セグメントあたりの秒数、デフォルトは 600）。`OPENCODE_CONFIG` はそのまま OpenCode に渡されます。

`~/.config/opencode/opencode.json` における Ollama 経由のローカルモデルの例：

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

`reasoningEffort: "none"` は、Ollama がこれらのモデルでデフォルトで有効にしており、Modelfile では無効化できない思考プロセスの反映をオフにします。6単語の文での測定結果：オプションなしでは 919 トークンの思考と 68 秒、オプションありでは 9 トークンでした。

### 400 以上のモデルへの接続：`--use_openrouter`

OpenRouter は、単一のクレジットでサードパーティがホストするモデルの前に位置する従量課金制のルーターです。ここには、他のプロバイダーが提供していないオープンな中国製モデルなども含まれます。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` は必須です。課金が発生する前に実行される事前チェック（プリフライト）により、ルーティングにおける 2 つの特異点が調整されます：

- **同一のモデルが、上限の異なる数十のホストから提供されている点** — `z-ai/glm-5.3-flash` では 23 のホストが存在し、そのうち 1 つは出力が 2,048 トークンに制限されています。プリフライトは `/api/v1/models/{modèle}/endpoints` を読み込み、出力が 8,000 トークン未満のホストやステータスが低下しているホストを除外し、その他のホストを `allow_fallbacks: false` で固定します。
- **推論が出力レートで課金される点** — `z-ai/glm-5.2` の「OK」という応答に対して 2 トークンではなく 107 トークンが消費されます。デフォルトではオフになっています。推論を強制するモデルには、受け入れ可能な最も低いエフォートが渡されます。カタログのデフォルト値では翻訳が完了する前に出力が上限に達する可能性があるためです。`--reasoning_effort` が常に優先されます。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- コンテキストウィンドウはカタログから取得されます。プロンプトとセグメント用に 8,400 トークン、出力に最低 8,000 トークンが必要なため、16,400 トークン未満のモデルは呼び出し前に拒絶されます。
- カタログに存在しないスラッグ、カタログへの接続不能、または上限を満たすホストが存在しない場合、コマンドは停止します。
- 出力が空の `finish_reason=length` は、切り捨てではなく推論によって予算が消費されたことを意味します。メッセージでこれを区別します。
- `--eco` は効果がありません。
- 変数：`OPENROUTER_API_KEY` (<https://openrouter.ai/keys>)、`OPENROUTER_BASE_URL`（デフォルトは `https://openrouter.ai/api/v1`、`https://` は必須）、`OPENROUTER_TIMEOUT`（デフォルトは 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（デフォルトは 30）。

### 翻訳ノート

`--add_translation_note` は、`bottom`（デフォルト）、`top`（フロントマターの後）、または `both`（`--note_position`）に、`legacy`（太字の段落、デフォルト）または `marker`（`--note_format`）形式で注記を追加します。`marker` 形式は不可視の Markdown 参照定義
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`
に続き、太字の引用が付く形式です。GitHub 上で読みやすく、remark プラグインによるビルド時にも処理可能です。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 詳細な測定結果

すべての測定は、14 言語（en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi）に対して `aipmt` で実際に実行された翻訳に基づいています。
**書き込み完了**はガードを通過したファイル数をカウントし、**差異なし**は `scripts/compare_structure.py` で何も検出されなかったファイル数（セクション数、小見出し、リンク、個別 URL、コードブロック、インラインコード、表の行、ブロック引用、太字の単語数が同一であること）を示します。

「差異なし」とは「何も検出されなかった」という意味であり、「同一」という意味ではありません。比較ツールは内容を読み込まずに要素の数をカウントします。削除されたレベル 4 の見出し、置き換えられたインラインコードのテキスト、入れ替わった言語フラグ、どこにも繋がらなくなった余計な括弧を含む内部リンク `[texte]((#ancre))` などは報告されません。また、言語自体の品質を評価することもありません。

### 密度の高いウォッチ記事、`--news` モード

[jls42.org の AI ウォッチ記事](https://jls42.org/fr/news)の1号分：
589行、140リンク、21セクション、保護された英語の引用3箇所。2026年9月4日〜5日の測定キャンペーン。

| モデル                                          | アクセス方式       | 書き込み完了 | 差異なし     | 言語あたり中央値 |
| ----------------------------------------------- | ------------------ | ------------ | ------------ | ---------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14        | ✅ **14/14** | 1分18秒          |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google サブスク    | 14/14        | ✅ **14/14** | 3分59秒          |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google サブスク    | 14/14        | ✅ **14/14** | 3分14秒          |
| `claude-sonnet-5-5`                             | Anthropic API      | 14/14        | ✅ **14/14** | 3分37秒          |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT サブスク   | 14/14        | ✅ **14/14** | 11分28秒         |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14        | ✅ **14/14** | 5分37秒          |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14        | ✅ **14/14** | 26分23秒         |
| `sonnet` (`--use_claude_code`)                  | Claude サブスク    | 14/14        | ⚠️ 13/14     | 6分49秒          |
| `claude-sonnet-5`                               | Anthropic API      | 14/14        | ⚠️ 11/14     | 6分31秒          |
| `haiku` (`--use_claude_code`)                   | Claude サブスク    | 14/14        | ⚠️ 11/14     | 15分54秒         |
| `claude-haiku-5-5`                              | Anthropic API      | 14/14        | ⚠️ 11/14     | 2分54秒          |
| `claude-haiku-4-5`                              | Anthropic API      | 14/14        | ⚠️ 7/14      | 6分00秒          |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14        | ❌ 11/14     | 9分27秒          |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14        | ❌ 8/14      | 10分09秒         |
| `ollama/gpt-oss-20b-32k`                        | ローカル           | 10/14        | ❌ 7/14      | 12分39秒         |
| `mistral-large-latest`                          | Mistral API        | 11/14        | ❌ 5/14      | 5分32秒          |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14         | ❌ 3/14      | 37分27秒         |
| `grok-4.6` (`--use_grok_cli`)                   | Grok サブスク      | 1/14         | ❌ 1/14      | 23分11秒         |
| `opus` (`--use_claude_code`)                    | Claude サブスク    | 0/14         | ❌ 0/14      | —                |

Grok は 9月9日に同じウォッチの別の号（356行）で再測定されました：書き込み完了は 14言語中9言語、差異なしは8言語でした。冒頭の表に記載されているのはこの数値です。中断された3つのキャンペーンは記載されていません：クレジット不足による `qwen3.5-27b`（9言語）および `kimi-k2.6`（4言語）、そしてプロバイダーがその後修正した推論設定に起因する2件のエラーが発生した `z-ai/glm-5.3-flash` です。OpenRouter の行は、`--use_openrouter` 以前のルーターのデフォルト設定で測定されました。同梱プロバイダーで再測定された `z-ai/glm-5.2` は、同様に 14/14 の結果となっています。数値は 9月10日に現在の比較ツールを用いて再計算されました：初版公開時と比較して `qwen3.8-flash` と `qwen3.7-flash` がそれぞれ 1言語増えており、その他は変更ありません。

`--use_antigravity` の行は 9月26日に同一記事で、4並列翻訳として測定されました：午前中に `gemini-3.7-flash-medium`、午後に `gemini-3.8-flash-medium`。英語では、それぞれがフラグを捏造することなく引用文の下にある3行のフランス語訳を自ら削除し、英語の引用文はそのまま保持されました。フォールバックのクリーンアップ処理は何も行う必要がありませんでした。`--eco`（`gemini-3.7-flash-low`）では、わずか 4言語（en、ja、ar、hi）において：書き込み完了 4/4、すべて差異なし、中央値 1分52秒。同日、9月25日発行のより新しいウォッチ記事（438行、英語引用2箇所）を用いた追認テストを、ブログ外部で `gemini-3.7-flash-medium` により実施：書き込み完了 14/14、すべて差異なし、言語あたり 87〜128秒でした。

`--use_claude_code` の行は 9月26日に同一記事で、エフォート `low` にて 4並列翻訳として測定されました。`sonnet` では、14言語すべてで英語の引用が損なわれず、英語ではフラグを捏造することなくモデル自身がフランス語の翻訳行を削除しました。`opus` は1言語も書き込めませんでした。すべての言語において、結合部位用に生成された 279 個の分子に関する短いニュースが原因で、最後のセグメントでガードレールによって応答が停止されました。単体で送信した場合、このニュースは「バイオ」カテゴリに該当するとして拒否されますが、`sonnet` はすべて翻訳しました。`haiku` は 14言語すべてを書き込みました。3言語（en、pl、ro）でセクション見出しがレベル 2 からレベル 1 に変わりました。推論を防ぐことができず（出力トークンの 61%）、その結果 `sonnet` の 2倍以上の時間を要しました。

`claude-sonnet-5-5`、`claude-haiku-5-5`、および `claude-haiku-4-5` の行は、10月18日に Anthropic の API を使用して同一記事に対し、モデルごとに 4並列翻訳で測定されました。Sonnet 5.5 は思考プロセスの無効化を拒否するため、aipmt は受け入れ可能な最低設定を送信し、その応答には思考が含まれません。セグメントを再実行することなく、差異なしで 14言語を書き込みました。英語ではフラグを捏造することなく自らフランス語の翻訳行を削除し、英語の引用はすべての箇所で維持されました。Haiku 5.5 は適応的思考（adaptive thinking）を有効にして測定されました。思考を停止させるとフランス語の段落がそのまま残り、ガードにより拒絶され、書き込み完了は 14言語中3言語にとどまりました。両方の Haiku は同じ短いニュースでつまずいています。Haiku 5.5 は見出しレベルを変更するか、日本語・韓国語・中国語で二重化し、Haiku 4.5 は 7言語で見出しをレベル 1 に変更し、日本語ではフランス語のまま残しました。14言語の 2つのドキュメントにかかるコストは、Haiku 4.5 が 3.67 ドル、Haiku 5.5 が 0.57 ドル、Sonnet 5.5 が 9.21 ドルです。

### 本プロジェクトの README、標準 Markdown

2026年9月9日固定リビジョン：785行、インラインコード285個、コードブロック閉じタグ40個、表の行89行。4並行翻訳。

| モデル                                          | 生成数 | 差分なし   | 中央値/言語 | 差異内容                                                                 |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1分43秒        | なし                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1分48秒        | なし                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4分02秒        | 比較ツール上はなし；内部リンクの重複（en）                               |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1分18秒        | なし                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2分06秒        | なし                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36秒           | 太字の単語1つ（ja）                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1分22秒        | 太字の単語1つ（ko）                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2分20秒        | 表の行が前の行と結合（ar）                                               |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2分56秒        | リンク1つ（sv）、太字の単語1つ（zh）                                     |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6分46秒        | 太字の単語1つ（ar、ja）                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2分34秒        | 太字の単語1つ（hi、ja、ko）                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2分17秒        | アラビア語で40個のインラインコード追加；太字（hi、ja、ko）               |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1分14秒        | 2言語で拒絶（ar、hi）：戻り値でインラインコード欠落                      |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2分44秒        | セクション欠落1つ（ar、hi、ko）；コードブロック追加（ja、ko、ro、zh）   |

中断された2つのキャンペーンは記録されていません：Grok は12言語（うち11言語で差分なし）の後に CLI セッションが期限切れとなり、`qwen3.8-flash` は2言語の後にホスト事業者から HTTP 429 が返されました。`opencode/mimo-v2.5-free` と `ollama/gpt-oss-20b-32k` はこのリビジョンでは再計測されていません。277行短い9月4日・5日のリビジョンでは、それぞれ14言語中9件の翻訳を出力し、そのうち差分なしはそれぞれ7件と1件でした。

`--use_antigravity` および `--use_claude_code` の行は固定リビジョンではなく、9月26日に 1.14.0 とともに公開されたリビジョンで計測されました。また、`claude-sonnet-5-5`、`claude-haiku-5-5`、`claude-haiku-4-5` の行は10月18日に同じリビジョン（600行、インラインコード257個、コードブロック閉じタグ30個、表の行85行）で計測されました。185行短いため、他の行と単純に1対1で比較することはできませんが、これらの行同士は相互に比較可能です。比較ツールがチェックしない内部リンクについては、`gemini-3.8-flash-medium` は14言語すべてで損なわず保持し、`gemini-3.7-flash-medium` はイタリア語で破損させました。`sonnet` と `opus` はすべてで損なわず保持し、`haiku` は英語で重複させました。`claude-sonnet-5-5` と `claude-haiku-4-5` は14言語すべてで損なわず保持し、`claude-haiku-5-5` は出力した12言語で保持しました。

### 著名な4プロジェクトの README

GitHub からそのまま取得した FastAPI、Ollama、tldr-pages、Vue.js — 前述の2つよりも平易なドキュメントです。このキャンペーンは苦戦していたモデルを対象としており、Gemini を比較基準として使用しています。

| モデル                    | 対象範囲                   | 生成数  | 差分なし     |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4プロジェクト × 14言語     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4プロジェクト × 14言語     | 55/56   | ❌ 47/56     |
| `grok-4.6`（サブスクリプション）   | 4プロジェクト × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4プロジェクト × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### これらの測定値が意味しないこと

- **網羅的なランキングではない**：OpenRouter 単体でも400以上のモデルを提供しており、計測されたのは15種類程度です。
- **所要時間はあくまで目安**：キャンペーンによって3〜6件の並行翻訳を行っており、プロバイダーのスループットは時間帯によって変動します。
- **特定時点での観測結果である**：モデルは同名でも更新され、また皆様のドキュメントは本検証のものとは異なります。

ご自身のドキュメントで、ファイルの固定コピーに対して再計測を行うには：

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## 貢献

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

両方の行が必要です。`pip install -e .` がないと、`python -m aipmt` は `No module named aipmt` と応答します。

品質管理ツール（任意ですが推奨）：

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

リポジトリの28件の翻訳（README と CHANGELOG、14言語）は `./regen_translations.sh --force` で再生成されます。デフォルトでは ChatGPT サブスクリプション上で Codex と `gpt-6.1-sol` を使用し、4並行で実行されます。`REGEN_PROVIDER` と `REGEN_MODEL` は実行経路を変更します。`antigravity` は Google のサブスクリプションを利用し、例外指定なしで実行されます。従量課金 API（`openai`、`gemini`、`grok`、`openrouter`）は `REGEN_ALLOW_PAID_API=1` がなければ拒否されます。`REGEN_JOB_TIMEOUT` は各ジョブに上限時間を設定します（Codex および Antigravity では 600秒、1,800秒）。ツールの詳細は `CLAUDE.md` に記載されています。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** — 15言語で公開されている個人ブログ。その[毎日のAIウォッチ](https://jls42.org/fr/news)はこのツールによって毎日翻訳されており、上記の計測における参照ドキュメントとして使用されています。

## 著者

Julien LE SAUX  
メール: contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE バージョン 3。[LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE) を参照してください。

## 免責事項

本プログラムは、GPL v3 の第15条および第16条の条項に基づき、**いかなる保証もなく**配布されます。「現状有姿」で提供され、商品性または特定目的への適合性の保証はなく、その作者はいかなる使用に起因する損害に対しても責任を負いません。本要約よりもライセンス本文が優先されます。

- **公開前に確認してください。** 保護機能の対象はコードブロック、インラインコード、URL、アンカー、および `--news` モードの引用であり、見出し、表、フロントマター、文の意味は対象外です。
- **ドキュメントは選択したプロバイダーに送信され**、その利用規約およびデータポリシーの対象となります。一部の無料モデルはやり取りをトレーニングに再利用する場合があり、Antigravity の利用規約では有料サブスクリプションを含め、Google がそれらを再利用したり人間のレビュアーに閲覧させたりすることが許可されています。ローカルモデルのみが、お使いのマシンからデータを外部に送信しない唯一の方法です。
- **API 呼び出しには費用が発生します。** 本プログラムは利用料金に上限を設けません。長いドキュメント、失敗後のリトライ、あるいは推論量の多いモデルはコストが増加します。
- **公開されている測定結果は特定時点の観測記録であり**、保証ではありません。

記載されている製品名および会社名は、それぞれの所有者に帰属します。本プロジェクトはいずれとも提携していません。

**gemini-3.8-flash-mediumでフランス語から日本語に翻訳された記事。**
