# AI-Powered Markdown 翻訳ツール

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

構造（コードブロック、インラインコード、URL、アンカー、表、フロントマター）を保持しながら、Markdownファイルをある言語から別の言語へと翻訳します。モデルの呼び出し方法は11通り（5つのAPI、従量課金なしの4つのサブスクリプション、2つのルーター）あり、各モデルが実際に何を保持できるかの測定結果も公開しています。

## 概要

- **11種類のプロバイダーパス**: OpenAI、Mistral、Claude、Gemini、GrokのAPI。従量課金なしのChatGPT (Codex)、Grok、Google (Antigravity)、Claude (Claude Code) のサブスクリプション。OpenCode (オープンソース、無料またはローカル) およびOpenRouter (400以上のモデル) のルーター。
- **トークンの欠落による破損なし**: コードブロック、インラインコード、URL、アンカー、引用は呼び出し前にトークンへ置き換えられ、戻り時に検証されます。1つでも欠落している場合、ファイルは書き込まれません。
- **長文ドキュメント**: モデルのコンテキストウィンドウに応じた分割処理。
- **`--news`モード**: 技術動向記事向けに、英語の引用を保護し、言語ごとにフラグを管理。
- **`--eco`モード**: 高速かつ低コストなモデル。
- オプションの**翻訳注記**: 上部、下部、またはその両方に配置可能。

## インストール

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10以降。リポジトリからのインストールについては、[貢献](#貢献)を参照してください。

## 設定

キーは優先度の高い順に3つの場所から読み込まれ、前の場所で設定されていない項目のみを補完します。

|     | 場所                                          | 用途                                  |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 環境変数                                      | CI、コンテナ、一時的な上書き          |
| 2   | カレントディレクトリ（または親ディレクトリ）の `.env` | プロジェクト固有のキー                |
| 3   | `~/.config/aipmt/.env`                                 | 一度設定すれば全体で有効              |

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

`GEMINI_API_KEY` は `GOOGLE_API_KEY` の代わりとして受け入れられます。ユーザー設定ファイルは、`XDG_CONFIG_HOME`（絶対パスのみ）およびWindowsでは `%APPDATA%` に従います。キーが見つからない場合、コマンドはこれら3つの場所を列挙します。

**プロジェクトの `.env` は、呼び出しのリダイレクトや実行プログラムの選択を行うことはできません。** これはキーを提供するのみで、送信先やバイナリを指定することはありません。`_BASE_URL`、`_API_BASE`, `_ENDPOINT`, `_BIN` (`CODEX_BIN`, `GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`)、`GROK_HOME`、プロキシ (`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`)、証明書ストア (`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`)、および `XDG_CONFIG_HOME` / `APPDATA` に該当する変数はすべて警告とともに対象外となります。クローンしたリポジトリがユーザーのキーを乗っ取ったり、最初の翻訳時に独自プログラムを実行させたりするのを防ぐためです。また、このファイルは変数展開を行わずに読み込まれるため、`NOM=${OPENAI_API_KEY}` によってキーがコピーされることもありません。これらの変数は環境変数または `~/.config/aipmt/.env` で設定してください。

オプションの変数: `XAI_BASE_URL` (デフォルト `https://api.x.ai/v1`)、`CLAUDE_TIMEOUT` (呼び出しあたりの秒数、デフォルト 900)、`CODEX_BIN`、`CODEX_TIMEOUT` (デフォルト 600)、`GROK_BIN`、`GROK_HOME` (デフォルト `~/.grok`)、`GROK_TIMEOUT` (デフォルト 900)、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT` (デフォルト 900)、`OPENCODE_BIN`、`OPENCODE_TIMEOUT` (デフォルト 600)、`OPENROUTER_BASE_URL` (`https://` が必須)、`OPENROUTER_TIMEOUT` (デフォルト 900)、`OPENROUTER_PREFLIGHT_TIMEOUT` (デフォルト 30)。それぞれプロバイダーのセクションで詳しく説明されています。

## クイックスタート

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` をスペイン語に翻訳すると、`--target_dir` 内に `document-es.md` が生成されます。`--include_model` を指定した場合は `document-es-gpt-5.6-terra.md` となります。元のファイル名を保持する `--keep_filename` を使用しない限り、拡張子は常に `.md` に統一されます（例: `article.mdx` は `article-en.md` になります）。既存の翻訳ファイルがある場合、`--force` が指定されていなければスキップされます。

終了コード: すべて成功またはスキップされた場合は `0`、失敗したファイルが残っている場合は `1`（標準エラー出力に一覧を表示）、設定に起因する問題の場合は `2`。書き込み処理自体が失敗した場合も含め、失敗したファイルが出力されることはありません。内容は一時ファイルとして別名で書き込まれた後にリネームされます。再実行するだけで回復します。

## どのモデルを選ぶべきか

2つの実際のドキュメントを用い、各モデルで同一の14言語に翻訳して測定しました。**数値は、14言語中、翻訳が出力され、かつ原文からの差異が一切生じなかった言語の数です。**

| モデル               | アクセス方法                      | 密度の高い技術動向記事 | このREADME    | 差異の内容および該当言語数                                                                                                          |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash** | Googleサブスクリプション (Antigravity) | ✅ 14/14                | ✅ 14/14     | 2つのドキュメントともに差異なし                                                                                                    |
| **Gemini 3.7 Flash** | Google APIキー                    | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語: 太字の単語が1つ増加 (ja)                                                                                            |
| **Gemini 3.7 Flash** | Googleサブスクリプション (Antigravity) | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語: 太字の単語が1つ減少 (ko)                                                                                            |
| **GPT-5.6 Sol**      | ChatGPTサブスクリプション、またはOpenAIキー | ✅ 14/14                | ⚠️ 12/14     | 14言語中2言語: 太字の単語が1つ減少 (ar, ja)                                                                                        |
| **GLM-5.2**          | OpenRouterキー                    | ✅ 14/14                | ⚠️ 11/14     | 14言語中3言語: 太字の単語が1つ減少 (hi, ja, ko)                                                                                    |
| Claude Sonnet 5      | Claudeサブスクリプション (Claude Code) | ⚠️ 13/14                | ⚠️ 13/14     | 記事では14言語中1言語: 太字の単語が1つ増加 (zh)。このREADMEでは1言語: 表の行が前の行と結合され表示されなくなる (ar)               |
| Claude Haiku 4.5     | Claudeサブスクリプション (Claude Code) | ⚠️ 11/14                | ✅ 14/14     | 記事では14言語中3言語: セクション見出しがレベル1に変更 (en, pl, ro)。このREADMEでは比較ツール上は差異なしだが内部リンクが英語で二重化 |
| Claude Sonnet 5      | Anthropic APIキー                 | ⚠️ 11/14                | ⚠️ 12/14     | 記事では14言語中3言語: コードブロックが余分に出現 (es, de, hi)。このREADMEでは2言語: マークアップが失われたリンク (sv)、太字の単語 (zh) |
| Qwen 3.7 Flash       | OpenRouterキー                    | ❌ 8/14                 | ⚠️ 10/14     | 記事では1言語が拒否、他5言語で差異。このREADMEでは約40単語が `code` 化 (ar)                                               |
| Grok 4.6             | Grokサブスクリプション            | ❌ 8/14                 | 測定なし     | 14言語中5言語が拒否（インラインコードとURLが出力されないため）。オランダ語は全体的に乖離                                          |
| GPT-OSS 20B          | ローカルモデル (Ollama)           | ❌ 7/14                 | 再測定なし   | 14言語中4言語が拒否: フランス語の文章が残存し、ガード機構によって停止                                                              |
| MiMo v2.5 (無料)     | OpenCode Zen（アカウント不要）    | ❌ 11/14                | 再測定なし   | 1言語が拒否。ポーランド語で1セクションが消失                                                                                       |
| Mistral Large        | Mistral APIキー                   | ❌ 5/14                 | ❌ 1/14      | **セクション全体が消失**: 記事で1言語 (hi)、このREADMEで3言語 (ar, hi, ko)。さらに記事では3言語が拒否                             |
| DeepSeek V4 Flash    | OpenRouterキー                    | ❌ 3/14                 | 再測定なし   | 14言語中10言語が拒否。1言語あたり37分を要する                                                                                      |
| Claude Opus 5.5      | Claudeサブスクリプション (Claude Code) | ❌ 0/14                 | ✅ 14/14     | 生物学関連の短いニュースによりOpusのガードレールが作動し、全14言語で記事が拒否。このREADMEでは差異なし                             |

|     | 記号の意味                                                                                                                                                                                            |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14言語すべてが翻訳され、原文との差異が一切ない                                                                                                                                                       |
| ⚠️  | 14言語すべてが翻訳されたが、差異は**マークアップ**のみ（太字の単語、`code`、角括弧が外れたリンクなど）。本文、URL、コードブロック、セクションの欠落は一切なし                               |
| ❌  | 少なくとも1つの言語で翻訳できなかった（ファイルが拒否され書き込まれなかった）、**または**書き込まれたファイル内でコンテンツの欠落がある                                                             |

重要なポイント:

- **拒否された翻訳は、破損した翻訳ではありません。** 返却時にトークンが不足している場合、ファイルは書き込まれず、その言語は拒否としてカウントされます。これは記事の翻訳においてGrokで発生した現象であり、非ラテン文字を使用する5言語において、最初のセグメントから4つのインラインコードと3つのURLが欠落していました。
- **1つの文章が原因でドキュメント全体が拒否されることがあります。** Opus 5.5 はこのREADMEを差異なく完璧に翻訳しますが、技術動向記事は1つも翻訳できませんでした。生物学の短いニュースに対してセーフティガードが応答を停止したためです。ファイルは書き込まれず、aipmt がその理由を通知します。
- **このセーフティネットは見出し、表、フロントマター、本文の欠落は検知しません。** セクションを丸ごと削除してしまうモデルがあっても、ツールはそのままファイルを出力してしまいます（Mistralがこれに該当します）。これらの要素はトークンへの置き換えができず、現在のガード機構では検査されません。`scripts/compare_structure.py` は消失したセクションを検出できますが、事後検知となります。
- **このREADMEにおけるGrokの評価はありません**: CLIセッションが12言語終了時点で期限切れとなったためです（うち11言語は差異なし）。中断されたキャンペーンは評価対象外としています。
- **言語の種類よりもドキュメントの密度が影響します。** Grokは一般的なREADMEであれば問題ありませんが、リンクが密集した記事ではオランダ語を含め脱落が発生します。

測定日時と対象ドキュメント：「このREADME」列は、2026年9月9日に本ファイルの固定リビジョン（785行、インラインコード285箇所、表89行。以降改訂あり）で測定されました。ただしAntigravityとClaude Codeの行は、1.14.0で公開されたより短いリビジョン（600行、インラインコード257箇所、表85行）を用いて9月26日に測定されています。「密度の高い技術動向記事」列は、9月4日〜5日に589行の記事を対象に実施したキャンペーンによるものです。ただしGrokの行は9月9日に同技術動向の別版で再測定され、AntigravityとClaude Codeの行は9月26日に同一記事で測定されました。完全な表、所要時間、測定手順については、[詳細な測定結果](#詳細な測定結果)を参照してください。

## すべてのオプション

| オプション               | 説明                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | 翻訳対象の単一Markdownファイル（`--source_dir`の代替）                                                         |
| `--source_dir`           | Markdownファイルが含まれるソースディレクトリ（デフォルト: `content/posts`）                                    |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ（デフォルト: `traductions_en`）                                               |
| `--source_lang`           | ソース言語（デフォルト: `fr`）                                                                       |
| `--target_lang`           | ターゲット言語（デフォルト: `en`）                                                                  |
| `--model`           | 使用する特定のモデル                                                                                          |
| `--eco`           | 経済的なモデルを使用                                                                                          |
| `--use_mistral`           | Mistral AI APIを使用                                                                                          |
| `--use_claude`           | Claude APIを使用                                                                                              |
| `--use_gemini`           | Gemini APIを使用                                                                                              |
| `--use_grok`           | xAI (Grok) APIを使用 — `XAI_API_KEY`が必要                                                                   |
| `--use_codex`           | ChatGPTサブスクリプションのクォータでCodex CLIを使用                                                          |
| `--use_grok_cli`           | GrokサブスクリプションのクォータでGrok CLIを使用                                                              |
| `--use_antigravity`           | Google AI ProまたはUltraサブスクリプションのクォータでAntigravity CLI（`agy`）を使用                 |
| `--use_claude_code`           | Claude ProまたはMaxサブスクリプションのクォータでClaude Code CLI（`claude -p`）を使用                     |
| `--use_opencode`           | OpenCodeで設定されたプロバイダーに向けてOpenCode（オープンソース）を使用。`--model provider/modèle`が必須                |
| `--use_openrouter`           | OpenRouterを使用 — `OPENROUTER_API_KEY`および`--model fournisseur/modèle`が必要                                                   |
| `--force`           | 再翻訳を強制                                                                                                  |
| `--keep_filename`           | 元のファイル名を保持                                                                                          |
| `--news`           | ニュースモード: 英語の引用を保護し、言語別の国旗を処理                                                        |
| `--add_translation_note`           | 翻訳ノートを追加                                                                                              |
| `--note_position`           | ノートの位置: `top`、`bottom`（デフォルト）、または`both`                              |
| `--note_format`           | ノートの形式: `legacy`（デフォルト、太字段落）または`marker`                                   |
| `--include_model`          | 出力ファイルにモデル名を含める                                                                                |
| `--reasoning_effort`          | GPT-5.xの推論エフォート: `none`/`low`/`medium`/`high`/`xhigh`    |

9つの`--use_*`フラグは相互に排他的です。2つを組み合わせると拒絶されます。

## プロバイダー

### API経由: OpenAI、Mistral、Claude、Gemini、Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco`は各プロバイダーのエコノミープラン（経済的ティア）に切り替えます。

| プロバイダー | 品質（デフォルト）                                    | エコノミー（`--eco`） |
| ------------ | ----------------------------------------------------- | ----------------------------- |
| OpenAI       | `gpt-5.6-terra`                                       | `gpt-5.6-luna`               |
| Claude       | `claude-sonnet-5`                                       | `claude-haiku-4-5`               |
| Mistral      | `mistral-large-latest`                                       | `mistral-small-latest`               |
| Gemini       | `gemini-3.7-flash`                                       | `gemini-3.1-flash-lite`               |
| Codex        | `gpt-5.6-sol`（`--model`により`terra`および`luna`も可） | `gpt-5.6-luna`               |
| Grok API     | `grok-4.6`                                       | `grok-4.3`               |
| Grok CLI     | `grok-4.6`                                       | `grok-4.5`               |
| Antigravity  | `gemini-3.8-flash-medium`                                       | `gemini-3.7-flash-low`               |
| Claude Code  | `sonnet`、エフォート`low`            | 同上 — `--eco`は無効  |
| OpenCode     | 必須の`--model provider/modèle`                                 | 同上 — `--eco`は無効  |
| OpenRouter   | 必須の`--model fournisseur/modèle`                                 | 同上 — `--eco`は無効  |

### ChatGPTサブスクリプション利用: `--use_codex`

公式のCodex CLIを制御します。APIキーや従量課金なしで、翻訳はChatGPTサブスクリプションのクォータから消費されます。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- バイナリは`CODEX_BIN`、次に`PATH`、その後にパッケージ`openai-codex-cli-bin`の順で検索されます。`~/.codex/auth.json`は一切読み取られません。
- サブプロセスの環境から`OPENAI_API_KEY`および`CODEX_API_KEY`は削除されます。キーが存在していてもAPIに切り替わることはありません。
- 各セグメントは5時間枠のうち少なくとも1「メッセージ」を消費します。検証に失敗して再試行された場合は2メッセージになります。OpenAIの目安発表によると、Plusプランでは`gpt-5.6-luna`（`--eco`）が250〜2,000メッセージ/5時間、`gpt-5.6-sol`が10〜100メッセージ/5時間です。
- `--model gpt-5.6-terra`および`--model gpt-5.6-luna`もサブスクリプション経由で渡されます。アカウントに権限のないモデルは400「model is not supported when using Codex with a ChatGPT account」を返します。
- APIよりも低速であり、ドキュメントが大きくなるほどその差は広がります。このREADMEの場合、`gemini-3.7-flash`の36秒に対し、`gpt-5.6-sol`では言語あたり中央値で6分46秒でした。
- CI環境（`CI`または`GITHUB_ACTIONS`が定義されている場合）では拒絶されます。サブスクリプションは個人のセッションファイルで認証されるため、共有ランナー上に置くべきではありません。
- 環境変数: `CODEX_BIN`、`CODEX_TIMEOUT`（セグメントあたりの秒数、デフォルト600）。

### Grokサブスクリプション利用: `--use_grok_cli`

SuperGrokまたはX Premium+のサブスクリプションで、公式のGrok Build CLIを使用する同様の仕組みです。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Codexよりも制限（隔離）が弱い点に注意。** GrokのOSサンドボックスは、最近の多くのLinux環境（AppArmor、コンテナランタイムソケット）では適用されず、適用できないプロファイルは警告なしに非サンドボックス状態で起動します。そのため、スクリプトはデフォルトでプロファイルを要求せず、それを通知した上で、CLIの`--deny`ルール（無言で保護を解除するのではなく起動を拒絶する唯一のレイヤーである包括ルール`*`を含む）に依存します。`GROK_TRANSLATE_SANDBOX=read-only`はOSサンドボックスを必須とし、マシンがそれに対応できない場合は起動が失敗します。
- クォータは週間単位でChat、Imagine、Voiceと共有されており、それを確認するコマンドはありません。バッチ処理により事前の警告なしに対話の利用枠が消費される可能性があります。
- 環境変数: `GROK_BIN`、`GROK_HOME`（CLIのディレクトリ、デフォルト`~/.grok`）、`GROK_TIMEOUT`（デフォルト900）、`GROK_TRANSLATE_SANDBOX`。

### Googleサブスクリプション利用: `--use_antigravity`

Antigravityの公式CLIである`agy`を使用する同様の仕組みです。Google AI ProまたはUltraの加入者の場合、トークン単位で課金される代わりに、翻訳はサブスクリプションのクォータから消費されます。これがこのクォータを利用する唯一の方法です。Gemini CLIは2026年6月18日以降これらのアカウントへの対応を停止しており（[告知](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)）、AntigravityのSDKはAPIキーまたはGoogle Cloudプロジェクトのみを受け付けます。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **有料経路は一切残されません。** agyがユーザーの環境から受け取る変数は、厳格に限定されたリスト（`PATH`、言語とタイムゾーン、ターミナル、ID、プロキシと証明書、セッションバス）のみであり、キーは一切渡されません。agyの変数のいくつかは表示なしに呼び出しを切り替えてしまうため（実測: ある変数はドキュメントをサードパーティのゲートウェイに送信し、別の変数は有料のGoogle Cloudプロジェクトに送信しました）、ブラックリスト形式では見落としが生じていました。いかなるセグメントの処理前にも、クォータを消費しない`agy -p /config`を実行し、有料AIクレジットが無効であり、APIキーもGoogle Cloudプロジェクトも存在しないことを確認する必要があります（設定が欠けている場合は拒絶されます）。そうでなければ何も翻訳されません。さらに、各呼び出しのログでサブスクリプションが証明される必要があり（`authMethod=consumer`）、そうでなければ応答は拒絶されます。
- **サンドボックス環境。** 各呼び出しはツールを持たない翻訳エージェントとともに、プライベートで使い捨てのホームディレクトリ内で実行されます。agyの設定、ルール、プラグイン、MCPサーバー、フックは持ち込まれず、履歴にも何も追加されません。また、ログイン情報はキーチェーン内に保持され、aipmtがそれを読み取ることは決してありません。エージェントが見つからない場合、agyは警告なしにコーディングエージェントとそのツールにフォールバックします。そのため、ログの1行全体で正しいエージェントが確認されなければならず（このメッセージを引用したドキュメントでは代用できません）、確認できなければ拒絶されます。
- **プラットフォーム**: キーチェーン（D-Busセッションバス、Secret Service）を備えたセッション下のLinux。macOSはサポートされていますが、測定は行われていません。Windows（agyが各呼び出しを分離する変数を読み取らないため）や、セッションバスのないLinux（SSHセッション、コンテナ、サーバー。agyはトークンを`~/.gemini`内のファイルに保存しますが、分離によって不可視になります）では拒絶されます。接続コードを1分待たされる代わりに、起動前に理由とともに拒絶されます。
- **モデル**: `agy models`のモデル。Geminiモデルはその名前にエフォートが含まれています（`gemini-3.8-flash-medium`…）。サフィックスのない名前は呼び出し前に拒絶され、`--reasoning_effort`は無効です。デフォルトは`gemini-3.8-flash-medium`で、`--eco`では`gemini-3.7-flash-low`になります。これらを決定したテストの詳細は[詳細な測定結果](#詳細な測定結果)に記載されています。ClaudeとGPT-OSSには独自のはるかに小さなクォータが設定されており、測定された1回の呼び出しにつきFlashの0.05%に対して5時間枠の約1%を消費します。
- **クォータ**: グループごとにトークンコストに比例した5時間枠および週間枠があります。作者のアカウントでの実測値: ソース100万文字あたり、`gemini-3.8-flash-medium`で5時間枠の約16ポイント、`gemini-3.7-flash-medium`で14ポイント、低エフォートで7〜8ポイントです。したがって、40,000文字のREADMEは約0.5ポイント強を消費します。週間リミットはプランのティアに依存します。再試行はagyがリトライ可能と宣言したものに従います。それ以外の場合、使い切った枠は決して再試行されず、`/usage`が表示するリセット時刻まで各ファイルを失敗させます。
- **APIよりも低速**: 密度の高い測定記事において、言語あたりの中央値は`gemini-3.8-flash-medium`で3分59秒、`gemini-3.7-flash-medium`で3分14秒でした（API経由のGemini 3.7 Flashは1分18秒）。
- **中断**: Ctrl-Cまたはターミナルを閉じると、クォータを消費して処理を完了させるのではなく、コマンドとともにagyを停止します。これはCodex、Grok CLI、OpenCodeでも同様です。`nohup`の下では、翻訳が継続します。
- CI環境（`CI`または`GITHUB_ACTIONS`が定義されている場合）では拒絶されます。ログイン情報は個人のキーチェーンに保持されます。ランナー上では`GOOGLE_API_KEY`を指定した`--use_gemini`を使用してください。
- 環境変数: `AGY_BIN`（未設定の場合は`PATH`、次に`~/.local/bin/agy`）、`AGY_TIMEOUT`（起動時間を含むセグメントあたりの秒数、デフォルト900）。

**利用規約: 自己責任での利用となります。** [Antigravityの利用規約](https://antigravity.google/terms)（第6項）およびその[FAQ](https://antigravity.google/docs/faq/)では、アカウント停止のペナルティを伴い、Antigravityのログイン情報を用いてサードパーティ製ソフトウェアから本サービスにアクセスすることを禁止しています（Claude Code、OpenClaw、OpenCodeが言及されています）。aipmtはトークンを読み取ったり再利用したりしません。GoogleがスクリプトやCI向けにドキュメント化している[ヘッドレスモード](https://antigravity.google/docs/cli/headless/)で公式バイナリを起動します。Googleのメンバーは、自身の作業のためにローカルスクリプトから`agy -p`を起動することを「標準的」と見なしています（[公式フォーラム、2026年9月25日、法的拘束力のない回答](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）。ただし、本ツールのように配布されるツールに関する明確な規定はありません。

**公開ドキュメント専用。** 同規約の第5項に基づき、有料サブスクリプションを含め、プロンプト、応答、メタデータなどのやり取りはGoogleの製品や機械学習の改善に使用されたり、人間によってレビューされたりする可能性があります。オプトアウトには効果が未文書化の`enableTelemetry`設定が必要ですが、aipmtはこれを設定しません。また、agyの通常の設定は分離環境には引き継がれません。機密情報は一切通さないでください。

### Claude サブスクリプション経由：`--use_claude_code`

Claude Code の公式 CLI である `claude` を `-p` モードで使用する場合も同じ原理です。Claude Pro または Max の有料ユーザーであれば、トークン単位で課金される代わりに、サブスクリプションの利用枠から翻訳が差し引かれます。従量課金制である Anthropic の API、`--use_claude` と混同しないようにしてください。

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **課金経路は一切開放されたままにならず、各呼び出しがそれを証明します。** Claude Code が環境から受け取るのは限定された変数リストのみであり、API キー、トークン、クラウドプロバイダー、aipmt を起動した Claude Code セッションの識別子などは含まれません。最初のセグメントの前に、`claude auth status` が Console キーのないサブスクリプション接続を表示しなければならず、利用枠を消費しない `/usage` がそれを証明する必要があります。各呼び出しも初期化イベントでそれを順次証明し、そうでなければ応答は拒否されます。
- **「追加利用（extra usage）」を無効化する**（claude.ai、設定 → 利用状況）：ゼロユーロを維持するためです。有効になっていると、利用枠の上限に達した際に引き継がれ、エラーを表示することなく課金されます。aipmt は、呼び出しの利用枠レポートがそれを検知するとすぐに翻訳を停止しますが、その呼び出し自体はすでにカウントされています。
- **Claude Code セッションとの利用枠の共有。** 各呼び出しは 5 時間および週単位のウィンドウの利用状況を報告します。80%（`AIPMT_CLAUDE_MAX_UTILIZATION`）を超えると、本来の作業に支障をきたさないよう、それ以上のセグメントは起動されません。
- **分離環境。** 各呼び出しはツールなしで、使い捨ての専用ディレクトリ内で、カスタマイズなしのモードで実行されます。ユーザーの `CLAUDE.md`、プラグイン、フック、MCP サーバー、設定は一切読み込まれず、セッションから何も保持されません。添付ファイルは遮断されます。ドキュメント内の `@chemin` はテキストのままであり、ファイルを開くことはありません（測定済み）。
- **モデル**：デフォルトは `sonnet`（effort は `low`）、`--eco` でも同様です。このパスでは `--eco` は何も変更しません。同一ドキュメントで測定したところ、`haiku` は阻止できない推論を行うため 2 倍遅く、コストもわずかに低い程度であり、`opus` は生物学関連のコンテンツを拒絶します（後述）。両モデルとも `--model` 経由でアクセス可能です。これらのエイリアスはそのファミリーの最新モデルに追従します。有料クレジットに切り替わってしまうため、`fable` および `[1m]` のバリアントは拒否されます。`--reasoning_effort` は effort を調整しますが、翻訳では何のメリットもなく、測定された推論はほぼゼロでした。
- **Opus は特定の生物学コンテンツを拒絶する。** そのガードレールは Sonnet よりも厳格であり、Anthropic のエラーメッセージでは「can sometimes flag biology-research-adjacent work（生物学研究関連の作業を誤検知することがある）」と警告されています。実測結果：生成された 279 個の分子に関するウォッチ記事の速報により、14 言語すべてで記事が拒否されました。何も書き込まれません。aipmt は切り詰められた応答を拒絶し、ガードレール名を提示して `--model sonnet` を推奨します。
- CI（`CI` または `GITHUB_ACTIONS` が定義されている場合）および Windows（未測定）では拒絶されます。
- 変数：`AIPMT_CLAUDE_BIN`（未指定時は `PATH`、次いで `~/.local/bin/claude`）、`AIPMT_CLAUDE_TIMEOUT`（セグメントあたりの秒数、デフォルトは 900）、`AIPMT_CLAUDE_MAX_UTILIZATION`（デフォルトは 0.8）、`CLAUDE_CONFIG_DIR`（Claude Code のアカウント、プロジェクトの `.env` から取得されることはありません）。作業ディレクトリは `XDG_CACHE_HOME/aipmt/claude-code` 配下（デフォルトは `~/.cache`）。

**利用規約：ご自身のアカウントが対象となります。**
[Claude Code の法的通知ページ](https://code.claude.com/docs/en/legal-and-compliance)
では、「an end user from signing in to the unmodified Claude Code binary with their own Claude subscription（エンドユーザーが自身の Claude サブスクリプションを使用して未改造の Claude Code バイナリにサインインすること）」を禁止していません。これは、公式バイナリを起動し、トークンを読み取らない aipmt が行っていることそのものです。しかし、Anthropic は「does not permit third-party developers […] to route requests through Free, Pro, or Max plan credentials on behalf of their users（サードパーティの開発者が […] ユーザーに代わって Free、Pro、または Max プランの認証情報を介してリクエストをルーティングすることを許可しない）」としており、「including open-source projects（オープンソースプロジェクトを含む）」サードパーティ製ツールには API キーを推奨し、その使用を有料クレジットに請求する権利を留保しています
（[Claude ヘルプ](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)）。
バイナリを起動する配布ツールについて、白黒をつけた明文規定はありません。

**データ**：Free、Pro、および Max アカウントでは、プライバシー設定で許可されている場合、モデルのトレーニングが Claude Code にも適用されます
（[データに関するページ](https://code.claude.com/docs/en/data-usage)）。aipmt はローカルの文字起こし（`--no-session-persistence`）を一切保持しません。機密情報は通さないようにしてください。

### 任意のプロバイダーへ：`--use_opencode`

[OpenCode](https://opencode.ai) はオープンソース（MIT）のコードエージェントであり、内部で設定されたプロバイダー（API キー、サブスクリプション、OpenCode Zen ゲートウェイ（アカウント不要の無料モデル）、ローカルモデルなど）へルーティングします。ここでは、Zen と Ollama の 2 つのルートがエンドツーエンドで測定されました。

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

`--model` は必須です。これがないと、OpenCode はやり取りがトレーニングに使用される可能性のある無料モデルにフォールバックしてしまい、その選択を勝手に行うことはありません。

各呼び出し時の分離環境：

- ユーザー設定よりも優先されるインライン設定により、すべてのツールが拒絶された（`permission: { "*": "deny" }`）エージェント `aipmt` を定義し、セッション共有は無効化、`--pure`、`--auto` は無効。
- 使い捨ての空の作業ディレクトリ、`OPENCODE_DISABLE_PROJECT_CONFIG` および `OPENCODE_DISABLE_CLAUDE_CODE` を配置。これらがないと、OpenCode はカレントディレクトリの `AGENTS.md` と `~/.claude/CLAUDE.md` をプロンプトに挿入してしまいます。グローバルな `~/.config/opencode/AGENTS.md` は引き続き挿入されます（OpenCode ではこれを除外できません）。
- 出力コントラクト：終了コード 0、`error` イベントなし、ツール呼び出しなし、最後のステップが `stop`、空でないテキスト、およびエージェント `aipmt` が実際に読み込まれていること。未知の `--agent` があっても OpenCode は失敗せず、コーディングエージェントにサイレントでフォールバックします。
- OpenCode 自体のキーである `OPENCODE_API_KEY` を除き、`aipmt` のキーは一切渡されません。プロバイダーは OpenCode 内で設定され、`aipmt` の `.env` 内では設定されません。

注意点：

- Zen の無料モデルは流動的で制限も文書化されておらず、やり取りがトレーニングに使用される可能性があります。公開ドキュメント向けであり、非公開コンテンツ向けではありません。
- セグメントは最大 16,000 文字になるため、ローカルモデルは少なくとも 16k トークンのコンテキストを提供する必要があります。Ollama はしばしば 4,096 に設定されるため、`PARAMETER num_ctx 32768` を指定した `Modelfile` を経由してください。
- `--eco` は効果がありません。`--reasoning_effort` はそのまま OpenCode の `--variant` として渡されます。
- OpenCode は各セッションを `~/.local/share/opencode/` にログ記録します。
- 変数：`OPENCODE_BIN`（未指定時は `PATH`、次いで `~/.opencode/bin/opencode`）、`OPENCODE_TIMEOUT`（セグメントあたりの秒数、デフォルトは 600）。`OPENCODE_CONFIG` はそのまま OpenCode に渡されます。

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

`reasoningEffort: "none"` は、Ollama がこれらのモデルでデフォルトで有効化し、Modelfile では無効化できない思考プロセスをオフにします。6 単語の文での実測値：オプションなしでは 919 トークンの思考と 68 秒、オプションありでは 9 トークンでした。

### 400 以上のモデルへ：`--use_openrouter`

OpenRouter は、単一のクレジットで従量課金されるルーターであり、サードパーティがホストするモデル（ここでは他のプロバイダーが提供していないオープンな中国製モデルを含む）の前面に位置します。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` は必須です。課金が発生する前に実行される事前チェックにより、ルーティングにおける 2 つの特異点が調整されます：

- **同一のモデルが、異なる上限を持つ多数のホストによって提供されている** — `z-ai/glm-5.3-flash` では 23 のホストがあり、そのうち 1 つは出力が 2,048 トークンに制限されています。事前チェックは `/api/v1/models/{modèle}/endpoints` を読み取り、出力が 8,000 トークン未満のホストやステータスが低下しているホストを除外した上で、`allow_fallbacks: false` で他のホストを固定します。
- **推論は出力料金で課金される** — `z-ai/glm-5.2` の「OK」応答において、2 トークンに対して 107 トークン消費されます。デフォルトでオフになっています。推論を必須とするモデルには、受け入れられる最も低い effort が割り当てられます。カタログのデフォルト値では、翻訳が完了する前に出力枠を使い切ってしまう可能性があるためです。`--reasoning_effort` が引き続き優先されます。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- コンテキストウィンドウはカタログから取得されます。呼び出しを行う前に、16,400 トークン未満のモデルは拒否されます（プロンプトとセグメント用に 8,400 トークン、最小出力用に 8,000 トークン）。
- カタログに存在しないスラッグ、カタログにアクセスできない場合、または上限を満たすホストが存在しない場合、コマンドは停止します。
- 出力が空の `finish_reason=length` は、切り詰めではなく推論によって予算が消費されたことを意味します。メッセージでこれが区別されます。
- `--eco` は効果がありません。
- 変数：`OPENROUTER_API_KEY` (<https://openrouter.ai/keys>)、`OPENROUTER_BASE_URL`（デフォルトは `https://openrouter.ai/api/v1`、`https://` が必須）、`OPENROUTER_TIMEOUT`（デフォルトは 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（デフォルトは 30）。

### 翻訳ノート

`--add_translation_note` は、`bottom`（デフォルト）、`top`（front matter の後）、または `both`（`--note_position`）に、`legacy`（太字の段落、デフォルト）または `marker`（`--note_format`）のフォーマットでノートを追加します。`marker` フォーマットは、非表示の Markdown 参照定義
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`
に太字の引用が続く構成となっており、GitHub 上で閲覧可能で、ビルド時に remark プラグインで利用できます。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 詳細な測定結果

すべての測定は、14 言語（en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi）に向けて `aipmt` で実際に実行された翻訳です。
**書き込み完了**はガードを通過したファイル数をカウントし、**差異なし**は `scripts/compare_structure.py` が何も検出しなかったもの（セクション数、小見出し数、リンク数、個別 URL 数、コードブロック数、インラインコード数、表の行数、引用ブロック数、太字単語数が同一であること）をカウントします。

「差異なし」は「何も検出されなかった」という意味であり、「同一である」という意味ではありません。比較ツールは内容を読まずに要素をカウントします。レベル 4 の見出しの削除、置き換えられたインラインコードのテキスト、入れ替わったフラグ、余分な括弧がレンダリングされてどこにも繋がらなくなった内部リンク（`[texte]((#ancre))`）などを検出することはなく、言語の質を判断することもありません。

### 密度の高いウォッチ記事、`--news` モード

[jls42.org の AI ウォッチ記事](https://jls42.org/fr/news)の 1 つのエディション：
589 行、140 リンク、21 セクション、保護された英語の引用 3 件。2026 年 9 月 4 日および 5 日の測定。

| モデル                                          | アクセス              | 書き込み完了 | 差異なし   | 中央値/言語 |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14** | 1 分 18 秒     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google サブスクリプション  | 14/14   | ✅ **14/14** | 3 分 59 秒     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google サブスクリプション  | 14/14   | ✅ **14/14** | 3 分 14 秒     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT サブスクリプション | 14/14   | ✅ **14/14** | 11 分 28 秒    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 分 37 秒     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 分 23 秒    |
| `sonnet` (`--use_claude_code`)                  | Claude サブスクリプション  | 14/14   | ⚠️ 13/14     | 6 分 49 秒     |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 分 31 秒     |
| `haiku` (`--use_claude_code`)                   | Claude サブスクリプション  | 14/14   | ⚠️ 11/14     | 15 分 54 秒    |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 分 27 秒     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 分 09 秒    |
| `ollama/gpt-oss-20b-32k`                        | ローカル              | 10/14   | ❌ 7/14      | 12 分 39 秒    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14      | 5 分 32 秒     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 分 27 秒    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok サブスクリプション    | 1/14    | ❌ 1/14      | 23 分 11 秒    |
| `opus` (`--use_claude_code`)                    | Claude サブスクリプション  | 0/14    | ❌ 0/14      | —              |

Grok は 9 月 9 日に同じウォッチ記事の別エディション（356 行）で再測定されました。14 言語中 9 言語が書き込まれ、差異なしは 8 言語でした。これが先頭の表に記載されている数値です。中断された 3 つの測定は記載されていません。クレジット不足による `qwen3.5-27b`（9 言語）および `kimi-k2.6`（4 言語）、そして 2 件の失敗がプロバイダー側で現在修正されている推論設定に起因していた `z-ai/glm-5.3-flash` です。OpenRouter の行は、`--use_openrouter` の前におけるルーターのデフォルト設定で測定されました。同梱プロバイダーで再測定された `z-ai/glm-5.2` は、同様に 14/14 の結果となっています。数値は 9 月 10 日に現行の比較ツールで再計算されました。初版公開時と比較して `qwen3.8-flash` と `qwen3.7-flash` はそれぞれ 1 言語増加し、その他は変更ありません。

`--use_antigravity` の行は、9 月 26 日に同一の記事を対象として 4 つの並列翻訳で測定されました（午前中に `gemini-3.7-flash-medium`、午後に `gemini-3.8-flash-medium`）。英語において、どちらもフラグを勝手に捏造することなく、引用の下にある 3 行のフランス語訳を自身で削除しており、英語の引用も完全なままでした。フォールバックのクリーンアップ処理は何も行う必要がありませんでした。`--eco`（`gemini-3.7-flash-low`）では、4 言語のみ（en、ja、ar、hi）で測定：4 言語すべて書き込み完了、全言語で差異なし、中央値 1 分 52 秒でした。同日、ウォッチ記事のより新しいエディションである 9 月 25 日分（438 行、英語の引用 2 件）で追試が行われ、ブログ外で `gemini-3.7-flash-medium` により翻訳されました：14 言語すべて書き込み完了、全言語で差異なし、1 言語あたり 87〜128 秒でした。

`--use_claude_code` の行は、9 月 26 日に同一の記事を対象として、4 つの並列翻訳、effort `low` で測定されました。`sonnet` では、14 言語すべてで英語の引用が無傷であり、英語ではモデル自身がフラグを捏造することなくフランス語の翻訳行を削除しました。`opus` はどの言語も書き込みできませんでした。結合部位用に生成された 279 個の分子に関する速報が原因で、各言語において最後のセグメントでガードレールによって応答が停止されたためです。この速報のみを単独で送信した場合、「bio」カテゴリを理由に拒否されます。`sonnet` はこれをすべて翻訳しました。`haiku` は 14 言語を書き込みましたが、3 言語（en、pl、ro）でセクションの見出しがレベル 2 からレベル 1 に変更されました。阻止できない推論を行い（出力トークンの 61%）、その結果 `sonnet` の 2 倍以上の時間を要しました。

### 本プロジェクトのREADME、標準Markdown

2026年9月9日時点の固定リビジョン：785行、インラインコード285個、コードブロックの閉じタグ40個、表の行数89行。4並列で翻訳。

| モデル                                          | 作成数 | 差分なし | 中央値/言語 | 差異の内容                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | なし                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | なし                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | 比較ツール上は差分なし。内部リンクの重複（en）                   |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | 太字が1語（ja）                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | 太字が1語（ko）                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | 表の行が前の行と結合（ar）                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | リンク1点（sv）、太字が1語（zh）                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | 太字が1語（ar、ja）                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | 太字が1語（hi、ja、ko）                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | アラビア語でインラインコードが40個追加、太字（hi、ja、ko）                   |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | セクションの欠落（ar、hi、ko）、コードブロックの追加（ja、ko、ro、zh） |

中断された2つの測定キャンペーンは記載していません。Grokは12言語の処理後にCLIセッションが期限切れとなり（うち11言語で差分なし）、`qwen3.8-flash`は2言語の処理後にホスト側からHTTP 429が返されました。`opencode/mimo-v2.5-free`および`ollama/gpt-oss-20b-32k`はこのリビジョンでは再測定していません。277行短かった9月4日〜5日のリビジョンでは、それぞれ14言語中9言語を作成し、差分なしはそれぞれ7言語と1言語でした。

`--use_antigravity`と`--use_claude_code`の行は、固定リビジョンではなく、9月26日に1.14.0と共に公開されたリビジョンで測定されました（600行、インラインコード257個、コードブロックの閉じタグ30個、表の行数85行）。185行短いため、他の行と1対1で直接比較することはできませんが、これら2つの行同士は比較可能です。比較ツールがチェックしない内部リンクについては、`gemini-3.8-flash-medium`は14言語すべてで損なわず保持し、`gemini-3.7-flash-medium`はイタリア語で破損させました。`sonnet`および`opus`はすべてにおいて損なわず保持し、`haiku`は英語で重複させました。

### 著名プロジェクトの4つのREADME

FastAPI、Ollama、tldr-pages、Vue.jsをGitHubからそのまま取得したもので、前の2つよりも平易なドキュメントです。この測定キャンペーンは苦戦しているモデルを対象としており、Geminiを比較の基準点として使用しています。

| モデル                    | 対象範囲                  | 作成数 | 差分なし   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4プロジェクト × 14言語     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4プロジェクト × 14言語     | 55/56   | ❌ 47/56     |
| `grok-4.6` (サブスクリプション)   | 4プロジェクト × ar、hi、ja、zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4プロジェクト × ar、hi、ja、zh | 15/16   | ❌ 9/16      |

### これらの測定結果が意味しないこと

- **網羅的なランキングではない**：OpenRouter単体でも400以上のモデルを提供しており、測定されたのはそのうち15程度にすぎません。
- **所要時間は目安**：キャンペーンに応じて3〜6並列で翻訳を行っており、プロバイダーのスループットは時間帯によって変動します。
- **特定時点での観測結果である**：同じ名称であってもモデルは変更され、また、対象ドキュメントも各自で異なります。

ご自身のドキュメントで、ファイルの固定コピーに対して測定を再現するには：

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

両行とも必要です。`pip install -e .`がないと、`python -m aipmt`は`No module named aipmt`と応答します。

品質の検証ツール（任意ですが推奨）：

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

リポジトリ内の28の翻訳（14言語のREADMEとCHANGELOG）は`./regen_translations.sh --force`で再生成されます。デフォルトではChatGPTサブスクリプション上のCodexおよび`gpt-5.6-sol`を使用し、4並列で実行されます。`REGEN_PROVIDER`と`REGEN_MODEL`でパスを変更できます。`antigravity`はGoogleのサブスクリプションを使用するため例外設定なしで実行できますが、従量課金制のAPI（`openai`、`gemini`、`grok`、`openrouter`）は`REGEN_ALLOW_PAID_API=1`がないと拒否されます。`REGEN_JOB_TIMEOUT`は各ジョブの上限時間を設定します（通常600秒、CodexおよびAntigravityでは1,800秒）。ツールの詳細は`CLAUDE.md`に記載されています。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** — 15言語で公開されている個人ブログ。その[毎日のAI動向ウォッチ](https://jls42.org/fr/news)はこのツールによって毎日翻訳されており、上記測定の参照ドキュメントとして使用されています。

## 著者

Julien LE SAUX
メール：contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。[LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)を参照してください。

## 免責事項

本プログラムは、GPL v3の第15条および第16条の条件に基づき、**いかなる保証もなく**配布されます。「現状のまま」提供され、商品性や特定目的への適合性の保証はなく、その作者は使用から生じたいかなる損害についても責任を負いません。この要約よりもライセンス本文が優先されます。

- **公開前に必ず見直してください。** 保護機能の対象となるのは、コードブロック、インラインコード、URL、アンカー、および`--news`モードの引用であり、見出し、表、フロントマター、文の意味は対象外です。
- **ドキュメントは選択したプロバイダーに送信されます**。そのプロバイダーの利用規約およびデータポリシーが適用されます。一部の無料モデルではやり取りがモデルの学習に再利用される場合があり、Antigravityの利用規約では有料サブスクリプションを含めGoogleがデータを再利用したり人間のレビュアーに閲覧させたりすることが許可されています。マシンからデータを一切出さない唯一の方法は、ローカルモデルを使用することです。
- **APIの呼び出し費用が発生します。** 本プログラムは支出の上限を設定しません。長文のドキュメント、失敗後のリトライ、あるいは推論量の多いモデルはより多くのコストがかかります。
- **公開されている測定結果は特定時点での観測値であり**、保証ではありません。

記載されている製品名および会社名は、それぞれの所有者に帰属します。本プロジェクトはいずれとも提携関係にありません。

**gemini-3.8-flash-mediumでフランス語から日本語に翻訳された記事。**
