# AI駆動 Markdown翻訳ツール

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

構造（コードブロック、インラインコード、URL、アンカー、表、front matter）を保持したまま、Markdownファイルをある言語から別の言語へと翻訳します。モデルの呼び出し方法は11通り（5つのAPI、従量課金なしの4つのサブスクリプション、2つのルーター）あり、各モデルが実際に何を保持できるかの測定結果も公開しています。

## 概要

- **11種類のプロバイダーパス**: OpenAI、Mistral、Claude、Gemini、GrokのAPI。従量課金なしのChatGPT (Codex)、Grok、Google (Antigravity)、Claude (Claude Code) サブスクリプション。OpenCode (オープンソース、無料またはローカル) およびOpenRouter (400以上のモデル) のルーター。
- **トークン欠落による破損を防止**: コードブロック、インラインコード、URL、アンカー、引用文は呼び出し前にトークンへ置換され、応答時に検証されます。1つでも欠落している場合、ファイルは書き込まれません。
- **長文ドキュメント対応**: モデルのコンテキストウィンドウに応じた自動分割。
- **`--news` モード**: 技術動向記事向けに、英語の引用文を保護し、言語ごとにフラグを管理。
- **`--eco` モード**: 高速かつ低コストなモデルを使用。
- **翻訳注記（任意）**: ドキュメント上部、下部、またはその両方に配置可能。

## インストール

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10以降が必要です。リポジトリからのインストールについては、[貢献する](#貢献)を参照してください。

## 設定

キーは優先度の高い順に3つの場所から読み取られ、先行する設定で未定義の項目のみを後続が補完します。

|     | 場所                                          | 用途                                  |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 環境変数                                      | CI、コンテナ、一時的な上書き          |
| 2   | カレントディレクトリ（または親ディレクトリ）の `.env` | プロジェクト固有のキー                |
| 3   | `~/.config/aipmt/.env`                                 | 一度設定すれば全体に適用              |

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

`GOOGLE_API_KEY` の代わりに `GEMINI_API_KEY` も使用できます。ユーザーファイルは、Windowsでは `XDG_CONFIG_HOME`（絶対パスのみ）および `%APPDATA%` に従います。キーが見つからない場合、コマンドは3つの場所をすべて列挙します。

**プロジェクトの `.env` では、呼び出し先のリダイレクトや実行プログラムの選択は行えません。** 提供できるのはキーのみであり、宛先やバイナリは指定できません。`_BASE_URL`、`_API_BASE`, `_ENDPOINT`、`_BIN` (`CODEX_BIN`、`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`)、`GROK_HOME`、プロキシ (`HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY`)、証明書ストア (`SSL_CERT_FILE`、`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`)、および `XDG_CONFIG_HOME` / `APPDATA` に該当する変数はすべて警告とともに対象外となります。クローンしたリポジトリによってキーが盗用されたり、最初の翻訳実行時に独自のプログラムを起動させられたりするのを防ぐためです。また、このファイルは変数展開を行わずに読み取られるため、`NOM=${OPENAI_API_KEY}` と記述してもキーはコピーされません。これらの変数は環境変数または `~/.config/aipmt/.env` に設定してください。

任意の変数: `XAI_BASE_URL`（デフォルトは `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（1呼び出しあたりの秒数、デフォルトは900）、`CODEX_BIN`、`CODEX_TIMEOUT`（デフォルトは600）、`GROK_BIN`、`GROK_HOME`（デフォルトは `~/.grok`）、`GROK_TIMEOUT`（デフォルトは900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（デフォルトは900）、`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（デフォルトは600）、`OPENROUTER_BASE_URL`（`https://` が必要）、`OPENROUTER_TIMEOUT`（デフォルトは900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（デフォルトは30）。各変数の詳細はプロバイダーごとのセクションに記載されています。

## クイックスタート

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` をスペイン語に翻訳すると、`--target_dir` 内に `document-es.md` が生成されます。`--include_model` を指定した場合は `document-es-gpt-5.6-terra.md` となります。元の名前を維持する `--keep_filename` を使用しない限り、拡張子は常に `.md` に変換されます（例: `article.mdx` は `article-en.md` になります）。既存の翻訳ファイルがある場合、`--force` が指定されていなければスキップされます。

終了コード: すべて成功またはスキップされた場合は `0`、失敗したファイルが残っている場合は `1`（標準エラー出力にリスト表示）、設定に起因する問題がある場合は `2`。書き込み処理自体が失敗した場合も含め、失敗したファイルが出力されることはありません。コンテンツは一時ファイルに書き込まれた後でリネームされます。そのため、単純に再実行するだけで問題ありません。

## 推奨モデルの選び方

実際の2つのドキュメントを用い、各モデルで同一の14言語に翻訳して検証しました。**数値は、14言語中、翻訳ファイルが正常に出力され、元の構造から一切乖離がなかった言語の数を示します。**

| モデル               | アクセス方法                      | 高密度な技術動向記事    | このREADME   | 乖離の内容および該当言語数                                                                                                          |
| -------------------- | --------------------------------- | ----------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.8 Flash** | Google サブスクリプション (Antigravity) | ✅ 14/14                | ✅ 14/14     | 両ドキュメントとも差異なし                                                                                                          |
| **Gemini 3.7 Flash** | Google APIキー                    | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語: 太字の単語が1つ増加 (ja)                                                                                            |
| **Gemini 3.7 Flash** | Google サブスクリプション (Antigravity) | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語: 太字の単語が1つ減少 (ko)                                                                                            |
| **GPT-5.6 Sol**      | ChatGPT サブスクリプション、またはOpenAIキー | ✅ 14/14                | ⚠️ 12/14     | 14言語中2言語: 太字の単語が1つ減少 (ar, ja)                                                                                        |
| **GLM-5.2**          | OpenRouterキー                    | ✅ 14/14                | ⚠️ 11/14     | 14言語中3言語: 太字の単語が1つ減少 (hi, ja, ko)                                                                                    |
| Claude Sonnet 5      | Claude サブスクリプション (Claude Code) | ⚠️ 13/14                | ⚠️ 13/14     | 記事では14言語中1言語で太字が1つ増加 (zh)；READMEでは1言語で表の行が直前の行と連結され非表示化 (ar)                                  |
| Claude Haiku 4.5     | Claude サブスクリプション (Claude Code) | ⚠️ 11/14                | ✅ 14/14     | 記事では3言語でセクション見出しがレベル1に変更 (en, pl, ro)；READMEでは比較ツール上は差分なしだが内部リンクが英語で重複            |
| Claude Sonnet 5      | Anthropic APIキー                 | ⚠️ 11/14                | ⚠️ 12/14     | 記事では3言語でコードブロックが余分に出現 (es, de, hi)；READMEでは2言語でリンクのマークアップ欠落 (sv)、太字単語の増加 (zh)        |
| Qwen 3.7 Flash       | OpenRouterキー                    | ❌ 8/14                 | ⚠️ 10/14     | 記事では1言語が拒絶され他に5言語で乖離；READMEでは約40単語が `code` 化 (ar)                                                 |
| Grok 4.6             | Grok サブスクリプション           | ❌ 8/14                 | 未測定       | インラインコードやURLの出力欠落により14言語中5言語が拒絶；オランダ語は全体的に乖離                                                  |
| GPT-OSS 20B          | ローカルモデル (Ollama)           | ❌ 7/14                 | 再測定なし   | 14言語中4言語が拒絶: モデルがフランス語の原文を残したため、ガードにより処理を中断                                                  |
| MiMo v2.5 (無料)     | OpenCode Zen (アカウント不要)     | ❌ 11/14                | 再測定なし   | 1言語が拒絶；ポーランド語で1セクションが欠落                                                                                        |
| Mistral Large        | Mistral APIキー                   | ❌ 5/14                 | ❌ 1/14      | **セクション全体が消失**: 記事で1言語 (hi)、READMEで3言語 (ar, hi, ko) — さらに記事では3言語が拒絶                                 |
| DeepSeek V4 Flash    | OpenRouterキー                    | ❌ 3/14                 | 再測定なし   | 14言語中10言語が拒絶；1言語あたり37分を要した                                                                                       |
| Claude Opus 5.5      | Claude サブスクリプション (Claude Code) | ❌ 0/14                 | ✅ 14/14     | 生物学関連の短いニュース記事にOpusのセーフティガードが反応し、全14言語で記事が拒絶；READMEでは差異なし                              |

|     | 記号の意味                                                                                                                                                                                            |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14言語すべてが翻訳され、元のドキュメント構造と完全一致している                                                                                                                                        |
| ⚠️  | 14言語すべてが翻訳されたが、**マークアップ**に軽微な差異がある（太字の増減、`code` の扱い、リンクの角括弧の脱落など）。テキスト、URL、コードブロック、セクションの欠落はない                 |
| ❌  | 少なくとも1言語の翻訳に失敗した（ファイルが拒絶され書き込まれなかった）、**または**書き込まれたファイル内でコンテンツの欠落が発生した                                                                |

結果から読み取れる重要なポイント：

- **「拒絶された翻訳」は「破損した翻訳」ではありません。** 応答時にトークンが欠落している場合、ファイルは書き出されず、その言語は拒絶としてカウントされます。記事におけるGrokのケースがこれに該当し、非ラテン文字圏の5言語において、最初のセグメントから4つのインラインコードと3つのURLが消失しました。
- **モデルは、たった1文が原因でドキュメント全体を拒絶することがあります。** Opus 5.5はこのREADMEを完全に翻訳しますが、技術動向記事は一切翻訳できませんでした。生物学に関する短い記事に対してセーフティ機能が働き、出力を停止させたためです。この場合もファイルは書き込まれず、aipmtがその理由を出力します。
- **このセーフティネットは見出し、表、front matter、一般テキストは保護しません。** モデルがセクション全体を削除した場合でも、ツールはそのままファイルを出力してしまいます（Mistralがこの挙動を示しました）。これらの要素はトークン置換が不可能であり、現在のガード機構では検知できません。`scripts/compare_structure.py` を使えば事後的に欠落セクションを検出できます。
- **GrokのREADMEに対する評価がない理由**: 12言語（うち11言語は差異なし）を処理した時点でCLIセッションの有効期限が切れました。途中で中断されたテストは評価対象外としています。
- **言語の違いよりもドキュメントの密度が影響します。** Grokは通常のREADMEであれば問題なく処理できますが、オランダ語を含め、リンクが密に配置された記事では処理に失敗します。

測定日時および対象ドキュメント：「このREADME」の列は、2026年9月9日に本ファイルの固定リビジョン（785行、インラインコード285個、表89行。以降改訂あり）を対象に測定されました。ただしAntigravityとClaude Codeの行は、9月26日に1.14.0で公開された短縮版リビジョン（600行、インラインコード257個、表85行）で測定されています。「高密度な技術動向記事」の列は、9月4日〜5日に実施された589行の記事に対するテスト結果です。ただしGrokの行は9月9日に同連載の別号で再測定され、AntigravityとClaude Codeの行は9月26日に同一記事で測定されています。完全な一覧表、所要時間、検証プロトコルについては[詳細な測定結果](#詳細な測定結果)を参照してください。

## すべてのオプション

| オプション               | 説明                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 翻訳する単一のMarkdownファイル（`--source_dir`の代替）                                                        |
| `--source_dir`           | Markdownファイルを含むソースディレクトリ（デフォルト: `content/posts`）                                      |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ（デフォルト: `traductions_en`）                                              |
| `--source_lang`          | 翻訳元言語（デフォルト: `fr`）                                                                      |
| `--target_lang`          | 翻訳先言語（デフォルト: `en`）                                                                      |
| `--model`                | 使用する特定のモデル                                                                                          |
| `--eco`                  | 経済的なモデルを使用                                                                                          |
| `--use_mistral`          | Mistral AI APIを使用                                                                                          |
| `--use_claude`           | Claude APIを使用                                                                                              |
| `--use_gemini`           | Gemini APIを使用                                                                                              |
| `--use_grok`             | xAI (Grok) APIを使用 — `XAI_API_KEY`が必要                                                                   |
| `--use_codex`            | ChatGPTサブスクリプションの枠でCodex CLIを使用                                                                |
| `--use_grok_cli`         | Grokサブスクリプションの枠でGrok CLIを使用                                                                    |
| `--use_antigravity`      | Google AI ProまたはUltraサブスクリプションの枠でAntigravity CLI（`agy`）を使用                       |
| `--use_claude_code`      | Claude ProまたはMaxサブスクリプションの枠でClaude Code CLI（`claude -p`）を使用                            |
| `--use_opencode`         | OpenCodeで設定されたプロバイダーに対してOpenCode（オープンソース）を使用。`--model provider/modèle`が必要               |
| `--use_openrouter`       | OpenRouterを使用 — `OPENROUTER_API_KEY`および`--model fournisseur/modèle`が必要                                                   |
| `--force`                | 強制的に再翻訳                                                                                                |
| `--keep_filename`        | 元のファイル名を維持                                                                                          |
| `--news`                 | ニュースモード: 英語の引用を保護し、言語ごとのフラグを管理                                                    |
| `--add_translation_note` | 翻訳注記を追加                                                                                                |
| `--note_position`        | 注記の位置: `top`、`bottom`（デフォルト）、または`both`                                |
| `--note_format`          | 注記のフォーマット: `legacy`（デフォルト、太字落段）または`marker`                              |
| `--include_model`        | 出力ファイルにモデル名を含める                                                                                |
| `--reasoning_effort`     | GPT-5.x推論エフォート: `none`/`low`/`medium`/`high`/`xhigh`        |

9つの`--use_*`フラグは相互排他的です。2つを組み合わせることは拒否されます。

## プロバイダー

### API経由: OpenAI、Mistral、Claude、Gemini、Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco`は各プロバイダーのエコノミープランに切り替えます。

| プロバイダー | 品質（デフォルト）                                    | エコノミー (`--eco`) |
| ------------ | ----------------------------------------------------- | ---------------------------- |
| OpenAI       | `gpt-5.6-terra`                                       | `gpt-5.6-luna`              |
| Claude       | `claude-sonnet-5`                                       | `claude-haiku-4-5`              |
| Mistral      | `mistral-large-latest`                                       | `mistral-small-latest`              |
| Gemini       | `gemini-3.7-flash`                                       | `gemini-3.1-flash-lite`              |
| Codex        | `gpt-5.6-sol`（`--model`により`terra`および`luna`も可） | `gpt-5.6-luna`              |
| Grok API     | `grok-4.6`                                       | `grok-4.3`              |
| Grok CLI     | `grok-4.6`                                       | `grok-4.5`              |
| Antigravity  | `gemini-3.8-flash-medium`                                       | `gemini-3.7-flash-low`              |
| Claude Code  | `sonnet`、エフォート `low`            | 同上 — `--eco`は無効 |
| OpenCode     | `--model provider/modèle` 必須                                  | 同上 — `--eco`は無効 |
| OpenRouter   | `--model fournisseur/modèle` 必須                                  | 同上 — `--eco`は無効 |

### ChatGPTサブスクリプション経由: `--use_codex`

公式のCodex CLIを制御します。翻訳はChatGPTサブスクリプションのクォータから差し引かれ、APIキーや従量課金は不要です。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- バイナリは`CODEX_BIN`、次に`PATH`、その後に`openai-codex-cli-bin`パッケージから検索されます。`~/.codex/auth.json`は読み込まれません。
- `OPENAI_API_KEY`および`CODEX_API_KEY`はサブプロセスの環境変数から削除されます。キーが存在していてもAPIに切り替わることはありません。
- 各セグメントは5時間のウィンドウから少なくとも1「メッセージ」を消費します。検証に失敗して再試行された場合は2メッセージになります。OpenAIの目安発表によると、Plusプランでは`gpt-5.6-luna`（`--eco`）で5時間あたり250〜2,000メッセージ、`gpt-5.6-sol`で10〜100メッセージです。
- `--model gpt-5.6-terra`および`--model gpt-5.6-luna`もサブスクリプション経由で使用可能です。アカウントに対象権限がないモデルを指定すると、400「model is not supported when using Codex with a ChatGPT account」エラーが返されます。
- APIよりも遅く、ドキュメントが長くなるほどその差は広がります。本READMEの場合、中央値で`gpt-5.6-sol`では言語ごとに6分46秒かかるのに対し、`gemini-3.7-flash`では36秒でした。
- CI環境（`CI`または`GITHUB_ACTIONS`が定義されている場合）では拒否されます。サブスクリプションの認証には個人のセッションファイルが使用されるため、共有ランナーに配置すべきではありません。
- 環境変数: `CODEX_BIN`、`CODEX_TIMEOUT`（セグメントあたりの秒数、デフォルト600）。

### Grokサブスクリプション経由: `--use_grok_cli`

SuperGrokまたはX Premium+のサブスクリプション枠を利用して、公式のGrok Build CLIでも同様の原理で動作します。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Codexよりも制約が緩いサンドボックス。** GrokのOSサンドボックスは、近年の多くのLinuxマシン（AppArmor、コンテナランタイムソケット）には適用されず、適用できないプロファイルは警告なしに非隔離状態で起動します。そのため、スクリプトはデフォルトでプロファイルを要求せず、それを通知した上で、CLIの`--deny`ルール（黙って保護を外すのではなく起動を拒否する唯一の層であるキャッチオール`*`を含む）に依存します。`GROK_TRANSLATE_SANDBOX=read-only`はOSサンドボックスを要求し、マシンがこれに対応できない場合は起動に失敗します。
- クォータは週間単位でChat、Imagine、Voiceと共有されており、確認するコマンドもありません。そのため、バッチ処理により予告なく会話利用の枠が消費される可能性があります。
- 環境変数: `GROK_BIN`、`GROK_HOME`（CLIディレクトリ、デフォルト`~/.grok`）、`GROK_TIMEOUT`（デフォルト900）、`GROK_TRANSLATE_SANDBOX`。

### Googleサブスクリプション経由: `--use_antigravity`

Antigravity公式CLIである`agy`でも同様の原理です。Google AI ProまたはUltraの加入者は、トークン単位の従量課金ではなく、サブスクリプションのクォータから翻訳分が差し引かれます。このクォータを利用する唯一の方法です。Gemini CLIは2026年6月18日以降これらのアカウントをサポートしなくなり（[発表](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)）、Antigravity SDKはAPIキーまたはGoogle Cloudプロジェクトのみを受け付けます。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **有料経路はすべて遮断されます。** agyは環境変数から限定されたリスト（`PATH`、言語とタイムゾーン、ターミナル、ID、プロキシと証明書、セッションバス）のみを受け取り、キーは一切受け取りません。表示なしに呼び出しを切り替えてしまう変数が複数存在し（実測: ドキュメントをサードパーティのゲートウェイに送信するものや、課金対象のGoogle Cloudプロジェクトに送信するものなど）、拒否リストでは見直すたびに見落としが生じていました。各セグメントの前に、クォータを消費しない`agy -p /config`を実行して、有料AIクレジットが無効化されており、APIキーやGoogle Cloudプロジェクトが存在しないことを確認する必要があります（設定が存在しない場合は拒否）。そうでなければ何も翻訳されません。その後の各呼び出しのログでサブスクリプション（`authMethod=consumer`）が証明される必要があり、証明されない場合は応答が拒否されます。
- **サンドボックス化（隔離）。** 各呼び出しはツールを持たない翻訳エージェントとともに、使い捨てのプライベートなホームディレクトリで実行されます。agyの設定、ルール、プラグイン、MCPサーバー、フックは持ち込まれず、履歴にも何も追加されません。また、認証情報はキーチェーン内に保持され、aipmtがそれを読み取ることはありません。エージェントが見つからない場合、agyは警告なしにコーディングエージェントとそのツールにフォールバックします。そのため、ログの1行全体で正しいエージェントが確認されなければなりません（ドキュメント内にそのメッセージの引用があっても代替にはなりません）。確認できなければ拒否されます。
- **プラットフォーム**: キーチェーン（D-Busセッションバス、Secret Service）を備えたセッション内のLinux。macOSも受け入れられますが、実測は行われていません。各呼び出しを分離する変数をagyが読み取らないWindowsや、セッションバスのないLinux（SSHセッション、コンテナ、サーバーなど。agyはトークンを`~/.gemini`内のファイルに保存し、分離によってそれが隠蔽されます）では拒否されます。ログインコードの入力を1分待たされるのではなく、起動前に理由とともに拒否されます。
- **モデル**: `agy models`のもの。Geminiモデルは名前にエフォートが含まれています（`gemini-3.8-flash-medium`など）。サフィックスのない名前は呼び出し前に拒否され、`--reasoning_effort`は効果がありません。デフォルトは`gemini-3.8-flash-medium`で、`--eco`では`gemini-3.7-flash-low`になります。これらを決定したテストについては[詳細な測定結果](#詳細な測定結果)に記載されています。ClaudeとGPT-OSSには独自のはるかに小さなクォータがあり、測定された呼び出しではFlashの0.05%に対して5時間ウィンドウの約1%を消費します。
- **クォータ**: グループごとに5時間ウィンドウと週間ウィンドウがあり、トークンコストに比例します。作者のアカウントでの測定では、`gemini-3.8-flash-medium`でソース文字数100万文字あたり5時間ウィンドウの約16ポイント、`gemini-3.7-flash-medium`で14ポイント、低エフォートでは7〜8ポイントでした。したがって、4万文字のREADMEは約0.5ポイント強を消費します。週間制限はプランによって異なります。再試行はagyがリトライ可能と宣言したものに従います。それ以外の場合、使い果たされたウィンドウに対して再試行は行われず、`/usage`が表示するリセット時刻まで各ファイルが失敗します。
- **APIよりも低速**: 密度の高い測定記事において、中央値で`gemini-3.8-flash-medium`で言語あたり3分59秒、`gemini-3.7-flash-medium`で3分14秒かかり、API経由のGemini 3.7 Flashの1分18秒と対照的です。
- **中断**: Ctrl-Cやターミナルの終了によって、クォータを消費し続けることなくコマンドとともにagyが停止します。Codex、Grok CLI、OpenCodeでも同様です。`nohup`の下では翻訳が継続します。
- CI環境（`CI`または`GITHUB_ACTIONS`が定義されている場合）では拒否されます。認証情報は個人のキーチェーンに保持されます。ランナーでは`GOOGLE_API_KEY`を指定した`--use_gemini`を使用してください。
- 環境変数: `AGY_BIN`（未設定の場合は`PATH`、次に`~/.local/bin/agy`）、`AGY_TIMEOUT`（起動を含むセグメントあたりの秒数、デフォルト900）。

**利用規約: 自己責任での利用となります。** [Antigravityの利用規約](https://antigravity.google/terms)（セクション6）およびその[FAQ](https://antigravity.google/docs/faq/)では、Antigravityの認証情報を利用してサードパーティ製ソフトウェアからサービスにアクセスすることが禁じられており（Claude Code、OpenClaw、OpenCodeが挙げられています）、アカウント停止の対象となります。aipmtはトークンを読み取ったり再利用したりしません。GoogleがスクリプトやCI向けに文書化している[ヘッドレスモード](https://antigravity.google/docs/cli/headless/)で公式バイナリを起動します。Googleの担当者は、自身の作業のためにローカルスクリプトから`agy -p`を起動することを「標準的」と見なしていますが（[公式フォーラム、2026年9月25日、法的拘束力のない回答](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）、本ツールのように配布されるツールのケースについては公式見解が確定していません。

**公開ドキュメントのみ。** 同規約のセクション5によれば、有料サブスクリプションを含め、プロンプト、応答、メタデータなどのやり取りはGoogleの製品や機械学習の改善に使用されたり、人間によってレビューされたりする可能性があります。除外設定は`enableTelemetry`設定で行いますが、その効果は文書化されておらず、aipmtはこれを設定しません。また、agyの設定は分離環境には引き継がれません。機密情報は一切通さないでください。

### Claude サブスクリプション経由：`--use_claude_code`

Claude Code の公式 CLI である `claude` を `-p` モードで使用する場合も同じ原理です。Claude Pro または Max の有料ユーザーであれば、翻訳はトークン単位で課金されるのではなく、サブスクリプションのクォータから差し引かれます。従量課金制である Anthropic の API、`--use_claude` と混同しないでください。

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **有料経路は一切開放されず、各呼び出しがそれを証明します。** Claude
  Code はご使用の環境から限定された変数のリストのみを受け取ります。API
  キー、トークン、クラウドプロバイダー、aipmt が起動された Claude Code
  セッションのマーカーなどは含まれません。最初のセグメントの前に、`claude auth status` が
  Console キーなしでのサブスクリプション接続を表示する必要があり、クォータを消費しない
  `/usage` がそれを証明しなければなりません。各呼び出しも初期化イベントで順次それを証明し、
  そうでなければ応答は拒否されます。
- **ゼロユーロ（無料枠内）を維持するために「extra usage」を無効化してください**
  （claude.ai の「Settings」→「Usage」）。有効になっていると、利用枠の上限に達した際に
  エラーを表示することなく引き継がれ、課金が発生します。aipmt は呼び出しのクォータレポートが
  それを検知すると直ちに翻訳を停止しますが、その呼び出し自体はすでにカウントされています。
- **Claude Code セッションと共有されるクォータ。** 各呼び出しは 5 時間枠および
  週間枠の使用状況を報告します。通常の作業用枠を使い果たさないよう、80%
  （`AIPMT_CLAUDE_MAX_UTILIZATION`）を超えるとそれ以上のセグメントは開始されません。
- **隔離（Confinement）。** 各呼び出しはツールなしで、使い捨ての専用プライベート
  ディレクトリ内にてカスタマイズ無効モードで実行されます。`CLAUDE.md` や
  プラグイン、フック、MCP サーバー、設定は一切読み込まれず、セッションの内容も
  保持されません。添付ファイル機能は遮断されており、ドキュメント内の `@chemin` は
  単なるテキストのままであり、ファイルが開かれることはありません（測定済み）。
- **モデル**：デフォルトは `sonnet` で、エフォートは `low`、`--eco` でも
  同様です。このパスでは `--eco` を指定しても何も変わりません。同一ドキュメントで
  測定したところ、`haiku` は阻止できない推論を行うため 2 倍遅く、コストも
  わずかに低い程度にとどまり、`opus` は生物学関連のコンテンツを拒絶します（後述）。
  どちらも `--model` からアクセス可能です。これらのエイリアスはそのファミリーの最新モデルに
  追従します。有料クレジット扱いとなるため、`fable` および `[1m]` のバリアントは
  拒否されます。`--reasoning_effort` はエフォートを調整しますが、翻訳においてメリットはなく、
  測定された推論はゼロまたはほぼ皆無です。
- **Opus は特定の生物学コンテンツを拒否します。** そのガードレールは Sonnet よりも
  厳格であり、Anthropic のエラーメッセージでも「can sometimes flag biology-research-adjacent work」
  と警告されています。実測結果：生成された 279 個の分子に関するウォッチ記事において、
  全 14 言語で記事が拒否されました。何も書き込まれず、aipmt は中断された応答を拒否し、
  ガードレールの名称を示して `--model sonnet` の使用を推奨します。
- CI（`CI` または `GITHUB_ACTIONS` が定義されている環境）および Windows（未測定）では拒否されます。
- 変数：`AIPMT_CLAUDE_BIN`（未指定時は `PATH`、次いで `~/.local/bin/claude`）、
  `AIPMT_CLAUDE_TIMEOUT`（セグメントあたりの秒数、デフォルトは 900）、
  `AIPMT_CLAUDE_MAX_UTILIZATION`（デフォルトは 0.8）、`CLAUDE_CONFIG_DIR`（Claude Code
  のアカウント。プロジェクトの `.env` から取得されることはありません）。作業ディレクトリは
  `XDG_CACHE_HOME/aipmt/claude-code` 配下（デフォルトは `~/.cache`）。

**利用規約：お客様自身のアカウントが対象となります。**
[Claude Code の法的ページ](https://code.claude.com/docs/en/legal-and-compliance)
では、「an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription（エンドユーザーが自身の Claude サブスクリプションを使用して未改変の Claude Code バイナリにサインインすること）」は
禁止されていません。公式バイナリを起動し、トークンを一切読み取らない aipmt の動作はこれに該当します。
しかし、Anthropic は「does not permit third-party developers […] to route requests through Free, Pro, or Max plan credentials on behalf of their users（サードパーティ開発者がユーザーに代わって Free、Pro、または Max プランの認証情報を介してリクエストをルーティングすること）」を認めておらず、「including open-source projects（オープンソースプロジェクトを含む）」サードパーティ製ツールには API キーの使用を推奨しており、有料クレジットからその利用分を差し引く権利を留保しています
（[Claude ヘルプ](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)）。
バイナリを起動する配布ツールに関する明確な規定は存在しません。

**データ**：Free、Pro、および Max アカウントでは、プライバシー設定で許可されている場合、
モデルのトレーニングが Claude Code にも適用されます
（[データに関するページ](https://code.claude.com/docs/en/data-usage)）。aipmt は
ローカルのトランスクリプションを一切保持しません（`--no-session-persistence`）。機密情報は
一切通さないでください。

### 任意のプロバイダー経由：`--use_opencode`

[OpenCode](https://opencode.ai) は、内部で設定されたプロバイダー（API キー、サブスクリプション、
OpenCode Zen ゲートウェイ（アカウント不要の無料モデル）、またはローカルモデル）へとルーティングする
オープンソース（MIT）のコードエージェントです。ここでは Zen と Ollama の 2 つのルートについて、
エンドツーエンドで測定を行いました。

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

`--model` の指定は必須です。これがない場合、OpenCode はやり取りがトレーニングに
使用される可能性のある無料モデルにフォールバックしてしまいますが、その選択をユーザーに
無断で行うことはありません。

各呼び出し時の隔離処理：

- インライン設定（ユーザー設定より優先）により、すべてのツールが拒絶されたエージェント `aipmt`
  （`permission: { "*": "deny" }`）を定義し、セッション共有は無効化、`--pure`、`--auto` は
  決して使用しません。
- 使い捨ての空の作業ディレクトリを使用し、`OPENCODE_DISABLE_PROJECT_CONFIG` と `OPENCODE_DISABLE_CLAUDE_CODE` を配置します。
  これらがない場合、OpenCode はカレントディレクトリの `AGENTS.md` および `~/.claude/CLAUDE.md` を
  プロンプトに挿入します。グローバルの `~/.config/opencode/AGENTS.md` は挿入されたままとなりますが、
  OpenCode 側でこれを除外する手段は提供されていません。
- 出力コントラクト：終了コード 0、`error` イベントなし、ツール呼び出しなし、最終ステップが
  `stop` であること、テキストが空でないこと、およびエージェント `aipmt` が実際に
  読み込まれていること（未知の `--agent` を指定しても OpenCode はエラーにならず、
  コーディングエージェントにサイレントにフォールバックします）。
- OpenCode 自体のキーである `OPENCODE_API_KEY` を除き、`aipmt` のキーは一切送信されません。
  プロバイダーの設定は `aipmt` の `.env` ではなく、OpenCode 内で行います。

注意点：

- Zen の無料モデルは変更されやすく、制限も文書化されておらず、やり取りがトレーニングに
  使用される可能性があります。公開ドキュメント向けであり、非公開コンテンツには適しません。
- セグメントは最大 16,000 文字に達するため、ローカルモデルには少なくとも 16k トークンの
  コンテキストウィンドウが必要です。Ollama では 4,096 に設定されることが多いため、
  `PARAMETER num_ctx 32768` を指定した `Modelfile` を介して設定してください。
- `--eco` は効果がありません。`--reasoning_effort` は OpenCode の `--variant` として
  そのまま渡されます。
- OpenCode は各セッションを `~/.local/share/opencode/` にログ出力します。
- 変数：`OPENCODE_BIN`（未指定時は `PATH`、次いで `~/.opencode/bin/opencode`）、
  `OPENCODE_TIMEOUT`（セグメントあたりの秒数、デフォルトは 600）。`OPENCODE_CONFIG` は
  OpenCode にそのまま渡されます。

`~/.config/opencode/opencode.json` 内で Ollama を経由したローカルモデルの例：

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

`reasoningEffort: "none"` は、Ollama がこれらのモデルでデフォルトで有効にし、Modelfile では無効化できない
思考（thinking）プロセスを停止します。6 語の文で測定したところ、このオプションなしでは
919 トークンの思考と 68 秒を要したのに対し、オプションありでは 9 トークンで済みました。

### 400 以上のモデルへ：`--use_openrouter`

OpenRouter は、サードパーティがホストするモデル（他のどのプロバイダーもここでは提供していない
中国のオープンモデルを含む）を対象に、単一のクレジットで従量課金されるルーターです。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` は必須です。課金が発生する前に実行されるプリフライト処理により、
ルーティングにおける 2 つの特異点が調整されます：

- **同一モデルが、異なる上限を持つ多数のホストによって提供されています**。`z-ai/glm-5.3-flash` では
  23 のホストがあり、そのうちの 1 つは出力が 2,048 トークンに制限されています。プリフライトは
  `/api/v1/models/{modèle}/endpoints` を読み取り、出力が 8,000 トークン未満のホストやステータスが低下している
  ホストを除外し、残りのホストを `allow_fallbacks: false` で固定します。
- **推論（reasoning）は出力レートで課金されます**。`z-ai/glm-5.2` の「OK」という返答に対し、
  2 トークンではなく 107 トークンが消費されます。これはデフォルトでオフになっています。思考を
  強制するモデルには、受け入れ可能な最低限のエフォートが設定されます。カタログのデフォルト値では
  翻訳完了前に出力を使い果たしてしまう可能性があるためです。ただし、`--reasoning_effort` の指定が
  常に優先されます。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- コンテキストウィンドウはカタログから取得されます。呼び出しの前に、16,400 トークン未満の
  モデルは拒否されます（プロンプトとセグメント用に 8,400、出力用に最低 8,000）。
- カタログに存在しないスラッグ、カタログにアクセスできない場合、または上限を満たすホストが
  存在しない場合は、コマンドが停止します。
- 出力が空の `finish_reason=length` は推論によって予算を使い果たした状態であり、切り捨てではありません。
  メッセージで区別されます。
- `--eco` は効果がありません。
- 変数：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>）、
  `OPENROUTER_BASE_URL`（デフォルトは `https://openrouter.ai/api/v1`、`https://` が
  必要）、`OPENROUTER_TIMEOUT`（デフォルトは 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`
  （デフォルトは 30）。

### 翻訳注記

`--add_translation_note` は、`bottom`（デフォルト）、`top`（front matter の直後）、
または `both`（`--note_position`）の位置に、`legacy`（太字段落、デフォルト）または
`marker`（`--note_format`）形式で注記を追加します。`marker` 形式は、非表示の
Markdown 参照定義 `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"` と、それに続く太字の引用文で構成されます。
GitHub 上で閲覧可能であり、ビルド時に remark プラグインで利用できます。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 詳細な測定結果

すべての測定は、`aipmt` を使用して 14 言語（en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi）へ
実際に実行された翻訳に基づいています。**書き込み完了**はガードを通過したファイル数をカウントし、
**差異なし**は `scripts/compare_structure.py` が何も問題を検出しなかったファイル数（セクション数、小見出し数、
リンク数、ユニーク URL 数、コードブロック数、インラインコード数、表の行数、引用ブロック数、太字の単語数が
完全に一致）を示します。

「差異なし」は「何も検出されなかった」ことを意味し、「同一」を意味するわけではありません。コンパレータは
内容を読み取ることなく要素の数をカウントします。削除されたレベル 4 の見出しや、置き換えられた
インラインコードのテキスト、入れ替わった国旗フラグ、余計な括弧がついてリンク切れになった内部リンク
（`[texte]((#ancre))` など）は検出されず、言語としての妥当性も判定されません。

### 密度の高いウォッチ記事、`--news` モード

[jls42.org の AI ウォッチ記事](https://jls42.org/fr/news)の 1 エディション：
589 行、140 リンク、21 セクション、保護された 3 つの英語引用文。2026 年 9 月 4 日および 5 日の測定。

| モデル | アクセス方法 | 書き込み完了 | 差異なし | 中央値/言語 |
| --- | --- | --- | --- | --- |
| `gemini-3.7-flash` | Google API | 14/14 | ✅ **14/14** | 1 分 18 秒 |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google サブスクリプション | 14/14 | ✅ **14/14** | 3 分 59 秒 |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google サブスクリプション | 14/14 | ✅ **14/14** | 3 分 14 秒 |
| `gpt-5.6-sol` (`--use_codex`) | ChatGPT サブスクリプション | 14/14 | ✅ **14/14** | 11 分 28 秒 |
| `z-ai/glm-5.2` | OpenRouter | 14/14 | ✅ **14/14** | 5 分 37 秒 |
| `qwen/qwen3.8-flash` | OpenRouter | 14/14 | ✅ **14/14** | 26 分 23 秒 |
| `sonnet` (`--use_claude_code`) | Claude サブスクリプション | 14/14 | ⚠️ 13/14 | 6 分 49 秒 |
| `claude-sonnet-5` | Anthropic API | 14/14 | ⚠️ 11/14 | 6 分 31 秒 |
| `haiku` (`--use_claude_code`) | Claude サブスクリプション | 14/14 | ⚠️ 11/14 | 15 分 54 秒 |
| `opencode/mimo-v2.5-free` | OpenCode Zen | 13/14 | ❌ 11/14 | 9 分 27 秒 |
| `qwen/qwen3.7-flash` | OpenRouter | 13/14 | ❌ 8/14 | 10 分 09 秒 |
| `ollama/gpt-oss-20b-32k` | ローカル | 10/14 | ❌ 7/14 | 12 分 39 秒 |
| `mistral-large-latest` | Mistral API | 11/14 | ❌ 5/14 | 5 分 32 秒 |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter | 4/14 | ❌ 3/14 | 37 分 27 秒 |
| `grok-4.6` (`--use_grok_cli`) | Grok サブスクリプション | 1/14 | ❌ 1/14 | 23 分 11 秒 |
| `opus` (`--use_claude_code`) | Claude サブスクリプション | 0/14 | ❌ 0/14 | — |

Grok は 9 月 9 日に同じウォッチの別エディション（356 行）で再測定されました：14 言語中 9 言語が書き込まれ、
8 言語で差異なしとなりました。冒頭の表にあるのはこの数値です。中断された 3 つの実行は記載されていません：
クレジット不足による `qwen3.5-27b`（9 言語）および `kimi-k2.6`（4 言語）、そして
2 回の失敗が推論設定に起因していた `z-ai/glm-5.3-flash`（プロバイダー側で修正済み）です。
OpenRouter の行は、`--use_openrouter` の導入前、ルーターのデフォルト設定で測定されました。
提供されたプロバイダーで再測定した `z-ai/glm-5.2` は、同様に 14/14 を達成しています。
数値は 9 月 10 日に現在のコンパレータで再計算されました。初版の公開時と比較して
`qwen3.8-flash` と `qwen3.7-flash` がそれぞれ 1 言語ずつスコアを伸ばし、その他は変更ありません。

`--use_antigravity` の行は、9 月 26 日に同一記事にて 4 並列翻訳で測定されました（午前中に
`gemini-3.7-flash-medium`、午後に `gemini-3.8-flash-medium`）。英語では、両者ともに引用文の下にあった
3 行のフランス語訳を国旗記号を捏造することなく自ら削除し、英語の引用文も無傷でした。
フォールバックのクリーンアップ処理は何も行う必要がありませんでした。`--eco`
（`gemini-3.7-flash-low`）では、4 言語のみ（en、ja、ar、hi）で実施され、4/4 すべて書き込み完了、
すべて差異なし、中央値は 1 分 52 秒でした。同日、より新しいエディションである 9 月 25 日分
（438 行、英語引用 2 件）を用いてブログ外で `gemini-3.7-flash-medium` による検証テストを実施したところ、
14/14 すべて書き込み完了、すべて差異なし、1 言語あたり 87〜128 秒でした。

`--use_claude_code` の行は、9 月 26 日に同一記事にて 4 並列翻訳、エフォート `low` で
測定されました。`sonnet` では、14 言語すべてで英語の引用文が無傷であり、英語への翻訳時にも
モデル自らフランス語訳の行を削除し、国旗記号を捏造することもありませんでした。`opus` は
どの言語も書き込みできませんでした。結合部位向けに生成された 279 個の分子に関する短いニュースが
原因で、全言語において最終セグメントでガードレールにより応答が停止されました。この短いニュース単体を
送信したところ、「bio」カテゴリに該当するとして拒否されました。一方、`sonnet` はすべての言語で
翻訳に成功しました。`haiku` は 14 言語すべてを書き込みましたが、3 言語（en、pl、ro）において
セクションの見出しがレベル 2 からレベル 1 に変更されました。このモデルは強制的に思考を行い（出力トークンの
61% を占める）、それを停止する手段がないため、処理時間は `sonnet` の 2 倍以上となりました。

### 本プロジェクトのREADME、標準Markdown

2026年9月9日時点の固定リビジョン：785行、インラインコード285個、コードブロック終了部40個、表の行89行。4並行で翻訳。

| モデル                                          | 生成数 | 差分なし   | 中央値/言語 | 相違点                                                                   |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1分43秒        | なし                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1分48秒        | なし                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4分02秒        | 比較ツール上はなし；内部リンクの重複（en）                               |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36秒           | 1単語が太字（ja）                                                        |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1分22秒        | 1単語が太字（ko）                                                        |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2分20秒        | 表の行が前の行と結合（ar）                                               |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2分56秒        | リンク1件（sv）、1単語が太字（zh）                                       |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6分46秒        | 1単語が太字（ar、ja）                                                    |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2分34秒        | 1単語が太字（hi、ja、ko）                                                |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2分17秒        | アラビア語で40個のインラインコード追加；太字（hi、ja、ko）                |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2分44秒        | セクション欠落（ar、hi、ko）；コードブロック追加（ja、ko、ro、zh）        |

中断された2つの検証は記載していません：Grok（12言語後にCLIセッション期限切れ、うち11言語で差分なし）および `qwen3.8-flash`（2言語後にホスト側からHTTP 429が返却）。`opencode/mimo-v2.5-free` と `ollama/gpt-oss-20b-32k` はこのリビジョンでは再計測していません。277行短かった9月4〜5日のリビジョンでは、それぞれ14言語中9言語を出力し、差分なしはそれぞれ7言語と1言語でした。

行 `--use_antigravity` および `--use_claude_code` は、固定リビジョンではなく9月26日に1.14.0とともに公開されたリビジョンで計測されました（600行、インラインコード257個、コードブロック終了部30個、表の行85行）。185行短いため、他の行と1対1で単純比較することはできませんが、これらの行同士は比較可能です。比較ツールがチェックしない内部リンクについては、`gemini-3.8-flash-medium` は全14言語でそのまま維持し、`gemini-3.7-flash-medium` はイタリア語で破損させました。`sonnet` と `opus` はすべての言語で無傷のまま維持し、`haiku` は英語で重複させました。

### 著名な4プロジェクトのREADME

GitHubからそのまま取得したFastAPI、Ollama、tldr-pages、Vue.js — 前述の2つよりも平易なドキュメントです。この検証は苦戦しているモデルを対象としており、Geminiを比較基準として使用しています。

| モデル                    | 対象範囲                   | 生成数  | 差分なし     |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4プロジェクト × 14言語     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4プロジェクト × 14言語     | 55/56   | ❌ 47/56     |
| `grok-4.6` (サブスクリプション) | 4プロジェクト × ar、hi、ja、zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4プロジェクト × ar、hi、ja、zh | 15/16   | ❌ 9/16      |

### これらの計測結果が意味しないこと

- **網羅的なランキングではない**：OpenRouter単体でも400以上のモデルを提供しており、測定したのはそのうち約15モデルです。
- **所要時間はあくまで目安**：検証ごとに3〜6並行で翻訳を行っており、プロバイダーのスループットも時間帯によって変動します。
- **特定時点での観測結果であること**：同じモデル名でも中身が変更されることがあり、また皆さんのドキュメントは本検証のものとは異なります。

お手元のドキュメントで計測を再現するには、ファイルの固定コピーに対して以下を実行します：

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

この2行はいずれも必須です。`pip install -e .` がないと、`python -m aipmt` は `No module named aipmt` を返します。

品質管理ツール（任意ですが推奨）：

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

リポジトリの28件の翻訳（READMEおよびCHANGELOG、14言語）は `./regen_translations.sh --force` で再生成されます — デフォルトではChatGPTサブスクリプション上のCodexおよび `gpt-5.6-sol` を使用し、4並行で実行されます。`REGEN_PROVIDER` と `REGEN_MODEL` はパスを変更します：`antigravity` はサブスクリプション（Googleのもの）に留まり、オーバーライドなしで実行されます。従量課金API（`openai`、`gemini`、`grok`、`openrouter`）は `REGEN_ALLOW_PAID_API=1` がなければ拒絶されます。`REGEN_JOB_TIMEOUT` は各ジョブの上限時間を設定します（通常600秒、CodexおよびAntigravityでは1,800秒）。ツールの詳細は `CLAUDE.md` に記載されています。

## 本スクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** — 15言語で公開されている個人ブログ。その[毎日のAIウォッチ](https://jls42.org/fr/news)はこのツールによって毎日翻訳されており、上記の計測における参照ドキュメントとして使用されています。

## 著者

Julien LE SAUX
メール : contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。[LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE) を参照してください。

## 免責事項

本プログラムは、GPL v3の第15条および第16条の規定に基づき、**いかなる保証もなしに**配布されます。「現状有姿」で提供され、商品性や特定目的への適合性の保証はなく、その作者は使用から生じたいかなる損害に対しても責任を負いません。ライセンス本文が本要約に優先します。

- **公開前に再確認してください。** 保護機能の対象はコードブロック、インラインコード、URL、アンカー、および `--news` モードの引用です — 見出し、表、フロントマター、文の意味は対象外です。
- **ドキュメントは選択したプロバイダーに送信されます**。各プロバイダーの利用規約およびデータポリシーが適用されます。一部の無料モデルはやり取りを学習に再利用する場合があり、Antigravityの利用規約では有料サブスクリプションであってもGoogleによる再利用や人間によるレビューが許可されています。マシンからデータを一切外部に出さない唯一の方法は、ローカルモデルを使用することです。
- **API呼び出しには料金が発生します。** 本プログラムは利用料金に上限を設けません。ドキュメントが長い場合、失敗後の再試行、推論を多く行うモデルでは、コストが増加します。
- **公開されている計測結果は特定時点の観測結果であり**、保証ではありません。

記載されている製品名および会社名は、それぞれの所有者に帰属します。本プロジェクトはいかなる企業とも提携していません。

**gemini-3.8-flash-mediumでフランス語から日本語に翻訳された記事。**
