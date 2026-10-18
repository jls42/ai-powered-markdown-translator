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

コードブロック、インラインコード、URL、アンカー、表、front
matterの構造を維持したまま、Markdownファイルをある言語から別の言語へ
翻訳します。モデルを呼び出す方法は11種類です。5つのAPI、従量課金なしの
4つのサブスクリプション、2つのルーターに対応し、各モデルが実際に
何を維持できるかを測定した結果も公開しています。

## 概要

- **11種類のプロバイダー経路**：OpenAI、Mistral、Claude、Gemini、GrokのAPI。
  従量課金なしのChatGPT（Codex）、Grok、Google（Antigravity）、Claude（Claude
  Code）のサブスクリプション。さらに、OpenCode（オープンソース、無料またはローカル）とOpenRouter
  （400以上のモデル）のルーター。
- **トークンの欠落による不正な出力を防止**：コードブロック、インラインコード、
  URL、アンカー、引用は呼び出し前にトークンへ置き換えられ、
  応答後に検証されます。1つでも欠けていれば、ファイルは書き込まれません。
- **長い文書**：モデルのコンテキストウィンドウに応じて分割します。
- **`--news`モード**：技術動向記事向けに英語の引用を保護し、
  言語ごとにフラグを処理します。
- **`--eco`モード**：高速で安価なモデルを使用します。
- 上部、下部、または両方に配置できる、任意の**翻訳注記**。

## インストール

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10以降が必要です。リポジトリからインストールする方法は、
[コントリビューション](#コントリビューション)を参照してください。

## 設定

キーは優先度の高い順に3か所から読み込まれます。各場所では、
それ以前の場所で未設定の項目だけが補完されます。

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

`GOOGLE_API_KEY`の代わりに`GEMINI_API_KEY`も使用できます。ユーザーファイルは
`XDG_CONFIG_HOME`（絶対パスのみ）に従い、Windowsでは`%APPDATA%`にも
従います。キーがない場合、コマンドは3つの場所を一覧表示します。

**プロジェクトの`.env`は、呼び出し先を変更することも、
実行するプログラムを選択することもできません。** このファイルが提供するのは
キーだけであり、接続先やバイナリではありません。`_BASE_URL`、`_API_BASE`、
`_ENDPOINT`、`_BIN`（`CODEX_BIN`、`GROK_BIN`、
`OPENCODE_BIN`、`AGY_BIN`）で終わる変数、`GROK_HOME`、プロキシ
（`HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY`）、証明書ストア
（`SSL_CERT_FILE`、`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）、
および`XDG_CONFIG_HOME` / `APPDATA`は警告とともに無視されます。
クローンしたリポジトリがキーを横取りしたり、最初の翻訳時にそのリポジトリ独自の
プログラムを実行させたりすることはできません。このファイルは変数展開なしでも
読み込まれるため、`NOM=${OPENAI_API_KEY}`によってキーが複製されることもありません。
これらの変数は環境または`~/.config/aipmt/.env`に設定してください。

任意の変数：`XAI_BASE_URL`（デフォルトは`https://api.x.ai/v1`）、
`CLAUDE_TIMEOUT`（1回の呼び出しあたりの秒数、デフォルトは900）、`CODEX_BIN`、`CODEX_TIMEOUT`
（デフォルトは600）、`GROK_BIN`、`GROK_HOME`（デフォルトは`~/.grok`）、`GROK_TIMEOUT`
（デフォルトは900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（デフォルトは900）、
`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（デフォルトは600）、`OPENROUTER_BASE_URL`
（`https://`が必須）、`OPENROUTER_TIMEOUT`（デフォルトは900）、
`OPENROUTER_PREFLIGHT_TIMEOUT`（デフォルトは30）。各変数の詳細は、
対応するプロバイダーのセクションに記載されています。

## はじめに

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md`をスペイン語に翻訳すると、`--target_dir`内に`document-es.md`が生成され、
`--include_model`を指定した場合は`document-es-gpt-5.6-terra.md`になります。拡張子は常に
`.md`になります。たとえば`article.mdx`は`article-en.md`になります。ただし、
`--keep_filename`を使用すると元の名前が維持されます。翻訳がすでに存在する場合は、
`--force`を指定しない限りスキップされます。

終了コード：すべて成功またはスキップされた場合は`0`、失敗したファイルが
残っている場合は`1`（標準エラー出力に一覧表示）、設定に問題がある場合は
`2`です。書き込み処理自体が失敗した場合も含め、失敗したファイルが
書き込まれることはありません。内容は隣接する一時ファイルに書き込まれてから
名前が変更されます。再実行するだけで構いません。

## どのモデルを選ぶべきか

実際の2つの文書を、各モデルで同じ14言語に翻訳して測定しました。
**数値は14言語のうち、翻訳が書き込まれ、かつソースとの差異が
まったくなかった言語の数です。**

| モデル                | 利用方法                 | 情報密度の高い技術動向記事 | このREADME    | 相違点と、影響した言語数                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Googleサブスクリプション（Antigravity）   | ✅ 14/14                | ✅ 14/14     | 両方の文書とも相違なし                                                                                                                                 |
| **Claude Sonnet 5.5** | Anthropic APIキー                 | ✅ 14/14                | ✅ 14/14     | 両方の文書とも相違なし                                                                                                                                 |
| **Gemini 3.7 Flash**  | Google APIキー                    | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語：太字の単語が1つ増加（ja）                                                                                                                      |
| **Gemini 3.7 Flash**  | Googleサブスクリプション（Antigravity）   | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語：太字の単語が1つ減少（ko）                                                                                                                     |
| **GPT-5.6 Sol**       | ChatGPTサブスクリプション、またはOpenAIキー | ✅ 14/14                | ⚠️ 12/14     | 14言語中2言語：太字の単語が1つ減少（ar、ja）                                                                                                                |
| **GLM-5.2**           | OpenRouterキー                    | ✅ 14/14                | ⚠️ 11/14     | 14言語中3言語：太字の単語が1つ減少（hi、ja、ko）                                                                                                            |
| Claude Sonnet 5       | Claudeサブスクリプション（Claude Code）   | ⚠️ 13/14                | ⚠️ 13/14     | 記事では14言語中1言語：太字の単語が1つ増加（zh）。このREADMEでは1言語：表の1行が前の行に結合され、表示上は見えなくなった（ar）            |
| Claude Haiku 4.5      | Claudeサブスクリプション（Claude Code）   | ⚠️ 11/14                | ✅ 14/14     | 記事では3言語：セクション見出しがレベル1になった（en、pl、ro）。このREADMEでは比較ツール上の相違はないが、英語の内部リンクが重複 |
| Claude Sonnet 5       | Anthropic APIキー                 | ⚠️ 11/14                | ⚠️ 12/14     | 記事では3言語：コードブロックが出現（es、de、hi）。このREADMEでは2言語：リンクのマークアップが消失（sv）、単語が太字化（zh）                              |
| Claude Haiku 4.5      | Anthropic APIキー                 | ⚠️ 7/14                 | ✅ 14/14     | 記事では7言語：セクション見出しがレベル1になり、日本語ではフランス語のまま残った。このREADMEでは相違なし                                              |
| Claude Haiku 5.5      | Anthropic APIキー                 | ⚠️ 11/14                | ❌ 12/14     | 記事では3言語：セクション見出しのレベル変更または重複（ja、ko、zh）。このREADMEでは2言語が拒否され、インラインコードが消失（ar、hi）    |
| Qwen 3.7 Flash        | OpenRouterキー                    | ❌ 8/14                 | ⚠️ 10/14     | 記事では1言語が拒否され、ほかの5言語に相違。このREADMEでは約40語が`code`に変換された（ar）                                                    |
| Grok 4.6              | Grokサブスクリプション                   | ❌ 8/14                 | 未評価     | 14言語中5言語が、インラインコードとURLが返されなかったため拒否。オランダ語では全体にわたって相違                                                               |
| GPT-OSS 20B           | ローカルモデル（Ollama）             | ❌ 7/14                 | 再測定なし | 14言語中4言語が拒否：モデルがフランス語の文章を残したため、ガードが処理を停止                                                                  |
| MiMo v2.5（無料）   | OpenCode Zen、アカウント不要         | ❌ 11/14                | 再測定なし | 1言語が拒否。ポーランド語で1セクションが消失                                                                                                                  |
| Mistral Large         | Mistral APIキー                   | ❌ 5/14                 | ❌ 1/14      | **セクション全体が消失**：記事では1言語（hi）、このREADMEでは3言語（ar、hi、ko）。さらに記事では3言語が拒否                                |
| DeepSeek V4 Flash     | OpenRouterキー                    | ❌ 3/14                 | 再測定なし | 14言語中10言語が拒否。1言語あたり37分                                                                                                                 |
| Claude Opus 5.5       | Claudeサブスクリプション（Claude Code）   | ❌ 0/14                 | ✅ 14/14     | 生物学に関する短い記事が原因で、Opusのガードレールにより14言語すべての記事が拒否。このREADMEでは相違なし                                               |

|     | 記号の意味                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14言語すべてが翻訳され、ソースとの差異なし                                                                                                                                       |
| ⚠️  | 14言語すべてが翻訳されたが、**マークアップ**に相違あり。太字の単語、`code`、角括弧が消えたリンクなど。テキスト、URL、コードブロック、セクションの欠落はなし |
| ❌  | 少なくとも1言語を翻訳できず、ファイルが拒否されて書き込まれなかった、**または**書き込まれたファイルに内容の欠落あり                                                                      |

ここから得られる要点：

- **拒否された翻訳は、壊れた翻訳ではありません。** 応答でトークンが
  欠けている場合、ファイルは書き込まれず、その言語は拒否として数えられます。
  記事でGrokに起きたのがこのケースです。非ラテン文字を使用する5言語では、
  最初のセグメントから4つのインラインコードと3つのURLが失われました。
- **モデルは、たった1文を理由に文書全体を拒否することがあります。** Opus 5.5は
  このREADMEを相違なく翻訳しますが、技術動向記事は1つも翻訳できません。
  生物学に関する短い記事でガードレールが応答を停止するためです。ファイルは
  書き込まれず、aipmtが理由を示します。
- **この安全策では、見出し、表、front matter、テキストは保護されません。**
  セクションを削除するモデルは、ツールが問題なく書き込んでしまうファイルを
  返します。Mistralがその例です。これらの要素はトークンで置き換えられず、
  現在のガードでも検査されません。`scripts/compare_structure.py`は失われたセクションを
  検出しますが、それは処理後です。
- **このREADMEにはGrokの評価がありません**：CLIセッションが12言語の処理後に
  期限切れとなりました。そのうち11言語には相違がありませんでした。中断された
  測定には評価を付けません。
- **言語よりも文書の情報密度が重要です。** Grokは一般的なREADMEでは
  問題なく動作しますが、オランダ語を含め、リンクの多い記事では処理に失敗します。

日付と文書：「このREADME」列は、2026年9月9日にこのファイルの固定リビジョン
（785行、285個のインラインコード、89行の表）を使って測定されました。その後、
このファイルには修正が加えられています。ただし、AntigravityとClaude Codeの行は、
9月26日に1.14.0とともに公開された、より短いリビジョン（600行、257個の
インラインコード、85行の表）で測定され、Claude Sonnet 5.5、Haiku 5.5、
API経由のHaiku 4.5の行は、10月18日に同じリビジョンで測定されました。
「情報密度の高い技術動向記事」列は、589行の記事を対象に9月4日と5日に実施した
測定結果です。ただし、Grokの行は9月9日に同じ技術動向記事の別版で再測定され、
AntigravityとClaude Codeの行は9月26日に同じ記事で、これら3つのClaudeの行は
10月18日に測定されました。完全な表、処理時間、測定手順については、
[詳細な測定結果](#詳細な測定結果)を参照してください。
## すべてのオプション

| オプション                   | 説明                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 翻訳する単一の Markdown ファイル（`--source_dir` の代替）                                             |
| `--source_dir`           | Markdown ファイルを含むソースディレクトリ（既定値：`content/posts`）                                   |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ（既定値：`traductions_en`）                                    |
| `--source_lang`          | ソース言語（既定値：`fr`）                                                                                  |
| `--target_lang`          | ターゲット言語（既定値：`en`）                                                                                   |
| `--model`                | 使用する特定のモデル                                                                                  |
| `--eco`                  | 低コストモデルを使用                                                                              |
| `--use_mistral`          | Mistral AI API を使用                                                                                     |
| `--use_claude`           | Claude API を使用                                                                                         |
| `--use_gemini`           | Gemini API を使用                                                                                         |
| `--use_grok`             | xAI（Grok）API を使用 — `XAI_API_KEY` が必要                                                           |
| `--use_codex`            | ChatGPT サブスクリプションのクォータで Codex CLI を使用                                                    |
| `--use_grok_cli`         | Grok サブスクリプションのクォータで Grok CLI を使用                                                        |
| `--use_antigravity`      | Google AI Pro または Ultra サブスクリプションのクォータで Antigravity CLI（`agy`）を使用                       |
| `--use_claude_code`      | Claude Pro または Max サブスクリプションのクォータで Claude Code CLI（`claude -p`）を使用                      |
| `--use_opencode`         | OpenCode で設定されたプロバイダーに対して OpenCode（オープンソース）を使用；`--model provider/modèle` が必要 |
| `--use_openrouter`       | OpenRouter を使用 — `OPENROUTER_API_KEY` と `--model fournisseur/modèle` が必要                          |
| `--force`                | 再翻訳を強制                                                                                       |
| `--keep_filename`        | 元のファイル名を維持                                                                          |
| `--news`                 | ニュースモード：英語の引用を保護し、言語別のフラグを処理                                      |
| `--add_translation_note` | 翻訳注記を追加                                                                                |
| `--note_position`        | 注記の位置：`top`、`bottom`（既定値）、または `both`                                                     |
| `--note_format`          | 注記の形式：`legacy`（既定値、太字の段落）または `marker`                                            |
| `--include_model`        | 出力ファイルにモデル名を含める                                                            |
| `--reasoning_effort`     | GPT-5.x の推論努力：`none`/`low`/`medium`/`high`/`xhigh`                                         |

9 個の `--use_*` フラグは相互排他的です。2 つを組み合わせると
拒否されます。

## プロバイダー

### API 経由：OpenAI、Mistral、Claude、Gemini、Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` は各プロバイダーを低コスト階層へ切り替えます。

| プロバイダー    | 品質（既定値）                                      | 低コスト（`--eco`）      |
| ----------- | ----------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                   | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                    | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-5.6-sol`（`--model` により `terra` と `luna` も使用可能） | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                            | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                            | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                             | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`、推論努力 `low`                                | 同じ — `--eco` は効果なし |
| OpenCode    | `--model provider/modèle` が必須                 | 同じ — `--eco` は効果なし |
| OpenRouter  | `--model fournisseur/modèle` が必須              | 同じ — `--eco` は効果なし |

### ChatGPT サブスクリプション経由：`--use_codex`

公式 Codex CLI を制御します。翻訳は API キーや従量課金なしで、
ChatGPT サブスクリプションのクォータから差し引かれます。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- バイナリは `CODEX_BIN`、次に `PATH`、最後にパッケージ
  `openai-codex-cli-bin` の順で検索されます。`~/.codex/auth.json` は一切読み取られません。
- `OPENAI_API_KEY` と `CODEX_API_KEY` はサブプロセスの環境から
  削除されます。キーが存在していても API に切り替わることはありません。
- 各セグメントは 5 時間枠の「メッセージ」を最低 1 件消費します。検証に失敗して
  再試行された場合は 2 件です。OpenAI の推定では、Plus プランにおいて
  `gpt-5.6-luna`（`--eco`）では 250～2,000 メッセージ/5 時間、
  `gpt-5.6-sol` では 10～100 メッセージです。
- `--model gpt-5.6-terra` と `--model gpt-5.6-luna` も
  サブスクリプションを経由します。アカウントに利用権限のないモデルを指定すると、
  400「model is not supported when using Codex with a ChatGPT account」が返されます。
- API より低速で、文書が長くなるほど差が広がります。この README では、
  `gpt-5.6-sol` の言語ごとの中央値が 6 分 46 秒だったのに対し、
  `gemini-3.7-flash` では 36 秒でした。
- CI（`CI` または `GITHUB_ACTIONS` が定義されている場合）では拒否されます。サブスクリプションの認証には
  個人用セッションファイルが使用されるため、共有 runner に置くべきではありません。
- 変数：`CODEX_BIN`、`CODEX_TIMEOUT`（セグメントごとの秒数、既定値 600）。

### Grok サブスクリプション経由：`--use_grok_cli`

SuperGrok または X Premium+ サブスクリプションで、公式 Grok Build CLI を使用する
同様の仕組みです。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Codex より弱い隔離。** Grok の OS sandbox は、最近の多くの Linux 環境
  （AppArmor、コンテナのランタイムソケット）では適用されず、適用できない
  プロファイルが指定されると、通知なしで隔離されずに起動します。そのため、
  スクリプトは既定でプロファイルを要求せず、その旨を通知したうえで、
  CLI の `--deny` ルールに依存します。これには包括的な `*` も含まれ、
  保護を黙って解除するのではなく起動を拒否する唯一の層となります。
  `GROK_TRANSLATE_SANDBOX=read-only` は OS sandbox を必須とし、マシンがその要件を満たせない場合は
  起動に失敗します。
- クォータは週単位で、Chat、Imagine、Voice と共有されます。また、それを
  確認するコマンドはありません。したがって、バッチ処理が通知なしに
  会話用の利用枠を消費する可能性があります。
- 変数：`GROK_BIN`、`GROK_HOME`（CLI ディレクトリ、既定値 `~/.grok`）、
  `GROK_TIMEOUT`（既定値 900）、`GROK_TRANSLATE_SANDBOX`。

### Google サブスクリプション経由：`--use_antigravity`

公式 Antigravity CLI である `agy` を使用する同様の仕組みです。Google
AI Pro または Ultra の契約者は、トークン単位で課金される代わりに、翻訳が
サブスクリプションのクォータから差し引かれます。このクォータを利用できる経路は
これだけです。Gemini CLI は 2026 年 6 月 18 日以降、これらのアカウントを
サポートしておらず
（[発表](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)）、
Antigravity SDK は API キーまたは Google Cloud プロジェクトのみを受け付けます。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **有料経路は一切開放されません。** agy に環境から渡されるのは、
  `PATH`、言語とタイムゾーン、ターミナル、ID、プロキシと証明書、
  セッションバスという限定された変数リストだけであり、キーは一切渡されません。
  agy の複数の変数は、何も表示せずに呼び出し先を切り替えます（実測では、
  ある変数は文書を第三者のゲートウェイへ送り、別の変数は課金対象の
  Google Cloud プロジェクトへ送りました）。拒否リスト方式では、見直すたびに
  漏れが見つかっていました。各セグメントの処理前に、クォータを一切消費しない
  `agy -p /config` が、有料の AI クレジットが無効で、API キーも
  Google Cloud プロジェクトもないことを示す必要があります。設定が存在しない場合も
  拒否されます。この条件を満たさなければ何も翻訳されません。その後、各呼び出しの
  ログがサブスクリプションの使用（`authMethod=consumer`）を証明しなければ、
  応答は拒否されます。
- **隔離。** 各呼び出しは、ツールを持たない翻訳エージェントとともに、
  非公開で使い捨てのホームディレクトリ内で実行されます。利用者の設定、ルール、
  プラグイン、MCP サーバー、agy のフックはそこに持ち込まれず、履歴にも
  何も追加されません。接続情報はキーチェーンに残り、aipmt が読み取ることは
  ありません。エージェントが見つからない場合、agy は通知なしでコーディング用
  エージェントとそのツールへフォールバックします。そのため、ログの 1 行全体が
  正しいエージェントを確認していなければ拒否されます。このメッセージを引用する
  文書を使って確認の代わりにすることはできません。
- **プラットフォーム**：キーチェーン（D-Bus セッションバス、Secret Service）を
  利用できるセッション上の Linux。macOS も許可されますが、実測はされていません。
  Windows では、agy が各呼び出しを隔離する変数を読み取らないため拒否されます。
  セッションバスのない Linux、つまり SSH セッション、コンテナ、サーバーでも
  拒否されます。この環境では agy がトークンを `~/.gemini` のファイルに保存しますが、
  そのファイルは隔離によって見えなくなります。接続コードを 1 分待ってからではなく、
  起動前に理由とともに拒否されます。
- **モデル**：`agy models` のモデル。Gemini は名前に推論努力を含みます
  （`gemini-3.8-flash-medium` など）。接尾辞のない名前は呼び出し前に拒否され、
  `--reasoning_effort` は効果がありません。既定では `gemini-3.8-flash-medium`、
  `--eco` では `gemini-3.7-flash-low` です。これらを決定した検証は
  [詳細な測定](#詳細な測定結果)で説明しています。Claude と GPT-OSS には
  独自のクォータがあり、はるかに小さくなっています。実測では 1 回の呼び出しで
  5 時間枠の約 1％を消費するのに対し、Flash では 0.05％です。
- **クォータ**：グループごとに、5 時間枠と週単位の枠があり、トークンコストに
  比例して消費されます。著者のアカウントでの実測では、ソース文字 100 万字あたり、
  5 時間枠の約 16 ポイントを `gemini-3.8-flash-medium`、14 ポイントを
  `gemini-3.7-flash-medium`、7～8 ポイントを低い推論努力で消費しました。したがって、
  40,000 文字の README の消費は 0.5 ポイントを少し超える程度です。一方、
  週単位の上限は階層によって異なります。再試行は agy が再試行可能と判断した場合に
  行われます。それ以外では、枠を使い切っても決して再試行されず、
  `/usage` に表示されるリセット時刻まで、すべてのファイルが失敗します。
- **API より低速**：測定用の情報量が多い記事では、言語ごとの中央値が
  `gemini-3.8-flash-medium` で 3 分 59 秒、`gemini-3.7-flash-medium` で 3 分 14 秒だったのに対し、
  API 経由の Gemini 3.7 Flash では 1 分 18 秒でした。
- **中断**：Ctrl-C またはターミナルを閉じると、agy がクォータを消費して処理を
  完了するまで放置せず、コマンドとともに停止します。Codex、Grok CLI、OpenCode も
  同様です。`nohup` では翻訳が継続します。
- CI（`CI` または `GITHUB_ACTIONS` が定義されている場合）では拒否されます。接続情報は個人用
  キーチェーン内に保存されるためです。runner では `--use_gemini` と `GOOGLE_API_KEY` を使用します。
- 変数：`AGY_BIN`（未指定の場合は `PATH`、次に `~/.local/bin/agy`）、
  `AGY_TIMEOUT`（起動時間を含むセグメントごとの秒数、既定値 900）。

**利用規約：責任を負うのは利用者自身のアカウントです。**
[Antigravity の利用規約](https://antigravity.google/terms)（第 6 節）と
その [FAQ](https://antigravity.google/docs/faq/) は、Antigravity の接続情報を使用して
第三者製ソフトウェアからサービスへアクセスすることを禁止しており、
違反するとアカウントが停止される可能性があります。Claude Code、
OpenClaw、OpenCode が具体例として挙げられています。aipmt はトークンを
読み取ることも再利用することもなく、Google がスクリプトと CI 向けに
文書化している [headless モード](https://antigravity.google/docs/cli/headless/)で
公式バイナリを起動します。Google のメンバーは、個人の作業のために
ローカルスクリプトから `agy -p` を起動することを「標準的」だと述べています
（[公式フォーラム、2026 年 9 月 25 日、契約上の効力を持たない回答](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）。
ただし、本ツールのような配布ソフトウェアについて明確に判断した文書はありません。

**公開文書のみに使用してください。** 同じ利用規約の第 5 節によれば、
やり取りの内容（プロンプト、応答、メタデータ）は、有料サブスクリプションを
含め、Google の製品や機械学習の改善に利用され、人間が確認する場合があります。
オプトアウトには `enableTelemetry` という設定を使用しますが、その効果は
文書化されておらず、aipmt はこの設定を行いません。また、利用者の agy 設定は
隔離環境へ引き継がれません。機密情報は決して渡さないでください。
### Claude サブスクリプションについて：`--use_claude_code`

同じ原則が、Claude Code の公式 CLI である `claude` を `-p` モードで使用する場合にも適用されます。Claude Pro または Max の契約者は、翻訳がトークン単位で課金される代わりに、サブスクリプションのクォータから差し引かれます。従量課金制の Anthropic API である `--use_claude` と混同しないでください。

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **有料経路は一切開いたままにならず、各呼び出しがそれを証明します。** Claude Code が環境から受け取るのは、限定された変数の一覧だけです。API キー、トークン、クラウドプロバイダー、aipmt の起動元となる Claude Code セッションのマーカーはいずれも渡されません。最初のセグメントの前に、`claude auth status` が Console キーなしのサブスクリプション接続を示し、クォータを一切消費しない `/usage` がそれを証明する必要があります。さらに各呼び出しも初期化イベントで同じことを証明しなければならず、そうでない場合は応答が拒否されます。
- **「extra usage」を無効にしてください**（claude.ai の「設定」→「使用量」）。これにより費用をゼロに保てます。有効な場合、利用枠を使い切るとエラーを表示せずに引き継ぎ、課金されます。aipmt は呼び出しのクォータ明細にそれが示されると翻訳を停止しますが、その呼び出し自体はすでに計上されています。
- **Claude Code セッションと共有されるクォータ。** 各呼び出しは、5 時間枠および週間枠の使用量を報告します。80%（`AIPMT_CLAUDE_MAX_UTILIZATION`）を超えると、作業に使う分を使い切らないよう、それ以上のセグメントは開始されません。
- **隔離。** 各呼び出しはツールなしで、非公開の使い捨てディレクトリ内において、カスタマイズなしのモードで実行されます。`CLAUDE.md`、プラグイン、hooks、MCP サーバー、設定はいずれも読み込まれず、セッションの内容は何も保存されません。添付ファイルは無効です。文書内の `@chemin` はテキストのままで、ファイルを開くことはありません（実測済み）。
- **モデル**：デフォルトは `sonnet`、effort は `low` で、`--eco` でも同様です。この経路では `--eco` を指定しても何も変わりません。同じ文書で測定したところ、`haiku` は停止できない推論を行うため、費用がわずかに安いだけで速度は 2 倍遅く、`opus` は生物学に関する内容を拒否します（次項）。どちらも `--model` から引き続き利用でき、これらの alias は各ファミリーの最新モデルを参照します。`fable` と `[1m]` の各バリアントは有料クレジットを使用するため拒否されます。`--reasoning_effort` は effort を設定しますが、翻訳には効果がありません。測定された推論量はゼロか、ほぼゼロです。
- **Opus は一部の生物学関連コンテンツを拒否します。** そのガードレールは Sonnet より厳しく、Anthropic のエラーメッセージでは「生物学研究に近接する作業が誤って検出される場合がある」と警告されます。実測では、生成された 279 個の分子に関する短い監視記事が原因で、14 言語すべてにおいて記事が拒否されました。何も書き込まれません。aipmt は途切れた応答を拒否し、ガードレールが原因であることを明示して `--model sonnet` を推奨します。
- CI（`CI` または `GITHUB_ACTIONS` が定義されている場合）および Windows（未測定）では拒否されます。
- 変数：`AIPMT_CLAUDE_BIN`（未指定の場合は `PATH`、次に `~/.local/bin/claude`）、`AIPMT_CLAUDE_TIMEOUT`（セグメントごとの秒数、デフォルトは 900）、`AIPMT_CLAUDE_MAX_UTILIZATION`（デフォルトは 0.8）、`CLAUDE_CONFIG_DIR`（Claude Code のアカウント。プロジェクトの `.env` から取得されることはありません）。作業ディレクトリは `XDG_CACHE_HOME/aipmt/claude-code` 配下（デフォルトは `~/.cache`）です。

**利用規約：責任を負うのはご自身のアカウントです。** [Claude Code の法的情報ページ](https://code.claude.com/docs/en/legal-and-compliance)では、「エンドユーザーが自身の Claude サブスクリプションを使用して、改変されていない Claude Code バイナリにサインインすること」は妨げられていません。aipmt はまさにこれを行い、公式バイナリを起動し、トークンを読み取ることはありません。しかし Anthropic は、「サードパーティーの開発者がユーザーに代わって Free、Pro、または Max プランの認証情報を介してリクエストを中継すること」を認めておらず、「オープンソースプロジェクトを含む」サードパーティーツールには API キーを推奨し、その使用量を有料クレジットから差し引く権利を留保しています（[Claude のヘルプ](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)）。配布されたツールがバイナリを起動するケースについて明確に判断した文書はありません。

**データ**：Free、Pro、Max アカウントでは、プライバシー設定で許可されている場合、Claude Code もモデルの学習対象になります（[データに関するページ](https://code.claude.com/docs/en/data-usage)）。aipmt はローカルにトランスクリプトを一切保存しません（`--no-session-persistence`）。機密情報を処理させないでください。

### 任意のプロバイダーへ：`--use_opencode`

[OpenCode](https://opencode.ai) は、内部で設定されたプロバイダーへ処理を振り分けるオープンソース（MIT）のコーディングエージェントです。API キー、サブスクリプション、OpenCode Zen ゲートウェイ（アカウント不要の無料モデル）、またはローカルモデルを使用できます。ここでは Zen と Ollama の 2 経路をエンドツーエンドで測定しました。

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

`--model` は必須です。指定しなければ、OpenCode は対話内容が学習に使用される可能性のある無料モデルへフォールバックします。この選択が自動的に代行されることはありません。

各呼び出しは次のように隔離されます。

- ユーザー設定より優先される inline 設定により、すべてのツールが拒否された（`permission: { "*": "deny" }`）`aipmt` エージェントを定義し、セッション共有を無効化して `--pure` を使用し、`--auto` は決して使用しません。
- 空の使い捨て作業ディレクトリを使用し、`OPENCODE_DISABLE_PROJECT_CONFIG` と `OPENCODE_DISABLE_CLAUDE_CODE` を設定します。これらがない場合、OpenCode は現在のディレクトリの `AGENTS.md` と `~/.claude/CLAUDE.md` を prompt に注入します。グローバルな `~/.config/opencode/AGENTS.md` は引き続き注入され、OpenCode では除外できません。
- 出力契約では、終了コードが 0、`error` イベントがなく、ツール呼び出しもなく、最後のステップが `stop` で、テキストが空でなく、`aipmt` エージェントが実際に読み込まれていることが求められます。未知の `--agent` を指定しても OpenCode は失敗せず、通知なしにコーディングエージェントへフォールバックします。
- OpenCode 自体のキーである `OPENCODE_API_KEY` を除き、`aipmt` のキーは一切渡されません。プロバイダーは OpenCode 内で設定するものであり、`aipmt` の `.env` では設定しません。

留意事項：

- Zen の無料モデルは入れ替わる可能性があり、上限も文書化されておらず、対話内容が学習に使用される場合があります。公開文書には使えますが、非公開コンテンツには使用しないでください。
- セグメントは最大 16,000 文字になるため、ローカルモデルには少なくとも 16k tokens のコンテキストが必要です。Ollama では 4,096 に設定されることが多いため、`PARAMETER num_ctx 32768` を指定した `Modelfile` を使用してください。
- `--eco` は効果がありません。`--reasoning_effort` は OpenCode の `--variant` としてそのまま渡されます。
- OpenCode は各セッションを `~/.local/share/opencode/` に記録します。
- 変数：`OPENCODE_BIN`（未指定の場合は `PATH`、次に `~/.opencode/bin/opencode`）、`OPENCODE_TIMEOUT`（セグメントごとの秒数、デフォルトは 600）。`OPENCODE_CONFIG` はそのまま OpenCode に渡されます。

Ollama 経由でローカルモデルを使用する例（`~/.config/opencode/opencode.json` 内）：

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

`reasoningEffort: "none"` は、Ollama がこれらのモデルでデフォルトで有効にし、Modelfile では無効にできない推論を停止します。6 語の文で測定したところ、このオプションなしでは 919 tokens の推論と 68 秒を要しましたが、指定した場合は 9 tokens でした。

### 400 を超えるモデルへ：`--use_openrouter`

OpenRouter は、サードパーティーがホストするモデルの前段に置かれる従量課金制のルーターで、共通のクレジットを使用します。ここで他のどの provider も提供していない、中国製のオープンモデルも含まれます。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` は必須です。課金前に実行される preflight が、ルーティングに関する 2 つの特性を処理します。

- **同じモデルが、上限の異なる数十のホスティング事業者から提供されています。** `z-ai/glm-5.3-flash` では 23 の事業者があり、そのうち 1 つは出力が 2,048 tokens に制限されています。preflight は `/api/v1/models/{modèle}/endpoints` を読み、出力上限が 8,000 tokens 未満、または状態が低下している事業者を除外し、残りを `allow_fallbacks: false` で固定します。
- **推論は出力と同じ料金で課金されます。** `z-ai/glm-5.2` による「OK」という応答では、出力が 2 tokens なのに対し、推論は 107 tokens でした。推論はデフォルトで無効です。推論を必須とするモデルには、受け入れ可能な最低 effort が設定されます。カタログのデフォルト設定では、翻訳が終わる前に出力枠を使い切る可能性があるためです。`--reasoning_effort` は引き続き優先されます。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- コンテキストウィンドウはカタログから取得されます。16,400 tokens 未満のモデルは呼び出し前に拒否されます。prompt とセグメントに 8,400、出力に最低 8,000 が必要です。
- カタログに存在しない slug、到達不能なカタログ、または上限を満たすホスティング事業者がない場合は、コマンドが停止します。
- 出力が空の `finish_reason=length` は、切り詰めではなく、推論によって予算を消費した状態です。メッセージでは両者が区別されます。
- `--eco` は効果がありません。
- 変数：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>）、`OPENROUTER_BASE_URL`（デフォルトは `https://openrouter.ai/api/v1`、`https://` が必須）、`OPENROUTER_TIMEOUT`（デフォルトは 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（デフォルトは 30）。

### 翻訳注記

`--add_translation_note` は、`bottom`（デフォルト）、`top`（front matter の後）、または `both`（`--note_position`）に注記を追加します。形式は `legacy`（太字の段落、デフォルト）または `marker`（`--note_format`）です。`marker` 形式は、非表示の Markdown 参照定義である `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"` に続けて、太字の引用を配置します。GitHub 上で読めるほか、ビルド時に remark プラグインから利用できます。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 詳細な測定結果

すべての測定では、`aipmt` を使って実際に 14 言語（en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi）へ翻訳しました。**書き込み済み**はガードを通過してファイルが書き込まれた数、**差異なし**は `scripts/compare_structure.py` が何も検出しなかった数です。つまり、セクション、見出し、リンク、異なる URL、コードブロック、inline code、表の行、引用ブロック、太字語句の数が同じだったことを示します。

「差異なし」とは「何も検出されなかった」という意味であり、「同一」という意味ではありません。比較ツールは要素の内容を読まず、数だけを数えます。そのため、レベル 4 の見出しの削除、inline code のテキストの置き換え、旗の入れ替わり、余分な括弧によってリンク先を失った内部リンク `[texte]((#ancre))` のいずれも検出せず、言語の適否も判断しません。

### 情報量の多い監視記事、`--news` モード

[jls42.org の AI ウォッチ](https://jls42.org/fr/news)の一版です。589 行、140 リンク、21 セクション、保護された英語の引用 3 件を含みます。測定期間は 2026 年 9 月 4 日と 5 日です。

| モデル                                          | アクセス              | 書き込み済み | 差異なし   | 言語ごとの中央値 |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14** | 1 分 18 秒     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google サブスクリプション  | 14/14   | ✅ **14/14** | 3 分 59 秒     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google サブスクリプション  | 14/14   | ✅ **14/14** | 3 分 14 秒     |
| `claude-sonnet-5-5`                             | Anthropic API      | 14/14   | ✅ **14/14** | 3 分 37 秒     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT サブスクリプション | 14/14   | ✅ **14/14** | 11 分 28 秒    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 分 37 秒     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 分 23 秒    |
| `sonnet` (`--use_claude_code`)                  | Claude サブスクリプション  | 14/14   | ⚠️ 13/14     | 6 分 49 秒     |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 分 31 秒     |
| `haiku` (`--use_claude_code`)                   | Claude サブスクリプション  | 14/14   | ⚠️ 11/14     | 15 分 54 秒    |
| `claude-haiku-5-5`                              | Anthropic API      | 14/14   | ⚠️ 11/14     | 2 分 54 秒     |
| `claude-haiku-4-5`                              | Anthropic API      | 14/14   | ⚠️ 7/14      | 6 分 00 秒     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 分 27 秒     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 分 09 秒    |
| `ollama/gpt-oss-20b-32k`                        | ローカル              | 10/14   | ❌ 7/14      | 12 分 39 秒    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14      | 5 分 32 秒     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 分 27 秒    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok サブスクリプション    | 1/14    | ❌ 1/14      | 23 分 11 秒    |
| `opus` (`--use_claude_code`)                    | Claude サブスクリプション  | 0/14    | ❌ 0/14      | —              |

Grok は 9 月 9 日に同じウォッチの別版（356 行）で再測定され、14 言語中 9 言語が書き込まれ、そのうち 8 言語で差異がありませんでした。冒頭の表にはこの数値を掲載しています。中断された 3 回の測定は記載していません。`qwen3.5-27b`（9 言語）と `kimi-k2.6`（4 言語）はクレジット不足、`z-ai/glm-5.3-flash` の 2 回の失敗は provider が現在修正中の推論設定が原因でした。OpenRouter の行は `--use_openrouter` より前に、ルーターのデフォルト設定で測定しました。同梱の provider で再測定した `z-ai/glm-5.2` も同じ 14/14 になりました。数値は 9 月 10 日に現在の比較ツールで再計算され、`qwen3.8-flash` と `qwen3.7-flash` は初回公開時よりそれぞれ 1 言語増え、その他は変わっていません。

`--use_antigravity` の各行は、9 月 26 日に同じ記事を使い、4 件の翻訳を並列実行して測定しました。午前は `gemini-3.7-flash-medium`、午後は `gemini-3.8-flash-medium` です。英語では、どちらも引用の下にあるフランス語訳の 3 行を自ら削除し、旗を捏造することもなく、英語の引用もそのままでした。フォールバックのクリーンアップ処理は何もする必要がありませんでした。`--eco`（`gemini-3.7-flash-low`）では、4 言語のみ（en、ja、ar、hi）を測定し、4 言語すべてが書き込まれ、すべて差異なし、中央値は 1 分 52 秒でした。同日、より新しい 9 月 25 日版のウォッチ（438 行、英語の引用 2 件）でも対照試験を行い、ブログ外で `gemini-3.7-flash-medium` により翻訳しました。14 言語すべてが書き込まれ、すべて差異なし、1 言語あたり 87～128 秒でした。

`--use_claude_code` の各行は、9 月 26 日に同じ記事を使い、`low` の effort で 4 件の翻訳を並列実行して測定しました。`sonnet` では、14 言語すべてで英語の引用がそのまま維持され、英語ではモデルがフランス語訳の行を自ら削除し、旗を捏造することもありませんでした。`opus` はどの言語も書き込みませんでした。各言語で、結合部位向けに生成された 279 個の分子に関する短い記事が原因となり、最後のセグメントでガードレールが応答を停止したためです。この短い記事だけを送信しても、「bio」カテゴリとして拒否されました。`sonnet` はすべての言語で翻訳できました。`haiku` は 14 言語すべてを書き込みましたが、そのうち 3 言語（en、pl、ro）ではセクション見出しがレベル 2 からレベル 1 に変わりました。停止できない推論を行い、出力 tokens の 61% が推論に使われたため、`sonnet` の 2 倍を超える時間がかかりました。

`claude-sonnet-5-5`、`claude-haiku-5-5`、`claude-haiku-4-5` の各行は、10 月 18 日に Anthropic API を使い、同じ記事についてモデルごとに 4 件の翻訳を並列実行して測定しました。Sonnet 5.5 は推論を無効にする設定を拒否するため、aipmt は受け入れ可能な最低設定を送信しますが、その応答には推論が含まれていません。14 言語すべてを差異なしで書き込み、セグメントの再処理もありませんでした。英語ではフランス語訳の行を自ら削除し、旗を捏造することもなく、英語の引用はすべての言語でそのまま維持されました。Haiku 5.5 は adaptive thinking を使って測定しました。推論を無効にすると段落全体がフランス語のまま残り、ガードに拒否されたため、14 言語中 3 言語しか書き込まれませんでした。2 つの Haiku は同じ短い記事で問題を起こしました。Haiku 5.5 は日本語、韓国語、中国語でその見出しのレベルを変更するか重複させ、Haiku 4.5 は 7 言語でレベル 1 に変更し、日本語ではフランス語のまま残しました。2 文書を 14 言語へ翻訳する費用は、Haiku 4.5 が 3.67 ドル、Haiku 5.5 が 0.57 ドル、Sonnet 5.5 が 9.21 ドルでした。
### このプロジェクトの README、標準 Markdown

2026年9月9日に固定したリビジョン：785行、インラインコード285個、ブロック終端40個、表89行。4件の翻訳を並列実行。

| モデル                                          | 生成数 | 差異なし | 言語別中央値 | 相違点                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1分43秒     | なし                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1分48秒     | なし                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4分02秒     | 比較ツール上はなし；内部リンクが重複（en）                   |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1分18秒     | なし                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2分06秒     | なし                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36秒           | 太字の単語が1つ（ja）                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1分22秒     | 太字の単語が1つ（ko）                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2分20秒     | 表の1行が前の行に連結（ar）                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2分56秒     | リンクが1つ（sv）、太字の単語が1つ（zh）                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6分46秒     | 太字の単語が1つ（ar、ja）                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2分34秒     | 太字の単語が1つ（hi、ja、ko）                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2分17秒     | アラビア語でインラインコード40個を追加；太字（hi、ja、ko）                   |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1分14秒     | 2言語を拒否（ar、hi）：応答時にインラインコードが消失        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2分44秒     | セクションが1つ消失（ar、hi、ko）；コードブロックを追加（ja、ko、ro、zh） |

中断された2回の実行は評価に含めていない：Grok は12言語の処理後に CLI セッションが期限切れ（うち11言語は差異なし）、`qwen3.8-flash` は2言語の処理後にホスティング事業者から HTTP 429 が返された。`opencode/mimo-v2.5-free` と `ollama/gpt-oss-20b-32k` は、このリビジョンでは再測定していない；277行短い9月4日および5日のリビジョンでは、それぞれ14言語中9言語の翻訳を生成し、そのうち差異なしはそれぞれ7言語と1言語だった。

`--use_antigravity` と `--use_claude_code` の行は、固定したリビジョンでは測定しておらず、1.14.0 とともに公開されたリビジョンで9月26日に測定した。また、`claude-sonnet-5-5`、`claude-haiku-5-5`、`claude-haiku-4-5` の行は、同じリビジョンで10月18日に測定した：600行、インラインコード257個、ブロック終端30個、表85行。185行短いため、ほかの行とは項目ごとに比較できないが、これらの行同士は比較できる。比較ツールが検査しない内部リンクについては、`gemini-3.8-flash-medium` は14言語すべてでリンクをそのまま維持し、`gemini-3.7-flash-medium` はイタリア語でリンクを壊した；`sonnet` と `opus` はすべての言語でリンクをそのまま維持し、`haiku` は英語でリンクを重複させた；`claude-sonnet-5-5` と `claude-haiku-4-5` は14言語すべてでリンクをそのまま維持し、`claude-haiku-5-5` は生成した12言語すべてでリンクをそのまま維持した。

### 著名な4プロジェクトの README

FastAPI、Ollama、tldr-pages、Vue.js を GitHub からそのまま取得した。前述の2文書よりも簡単な文書である。この実行では、苦戦したモデルを対象とし、Gemini を比較基準として使用した。

| モデル                    | 対象範囲                  | 生成数 | 差異なし   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4プロジェクト × 14言語     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4プロジェクト × 14言語     | 55/56   | ❌ 47/56     |
| `grok-4.6`（サブスクリプション）   | 4プロジェクト × ar、hi、ja、zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4プロジェクト × ar、hi、ja、zh | 15/16   | ❌ 9/16      |

### これらの測定値が意味しないこと

- **網羅的なランキングではない**：OpenRouter だけでも400を超えるモデルを提供しているが、測定したのは約15モデルである。
- **所要時間は目安にすぎない**：実行によって3件から6件の翻訳を並列処理しており、プロバイダーの処理速度も時間帯によって変動する。
- **特定時点での観測結果である**：モデルは同じ名前のまま変更されることがあり、あなたの文書は私たちの文書とは異なる。

あなたの文書で測定を再現するには、ファイルの固定コピー上で次を実行する：

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

この2行はいずれも必要である：`pip install -e .` がない場合、`python -m aipmt` は `No module named aipmt` と応答する。

品質管理用ツール。任意だが推奨：

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

リポジトリ内の28件の翻訳（README と CHANGELOG、14言語）は、`./regen_translations.sh --force` で再生成できる。デフォルトの ChatGPT サブスクリプション上で Codex と `gpt-5.6-sol` を使用し、4件を並列実行する。`REGEN_PROVIDER` と `REGEN_MODEL` は経路を変更する：`antigravity` は Google のサブスクリプションを引き続き利用し、例外指定なしで処理される；課金対象の API（`openai`、`gemini`、`grok`、`openrouter`）は `REGEN_ALLOW_PAID_API=1` がなければ拒否される；`REGEN_JOB_TIMEOUT` は各ジョブの上限時間を設定する（600秒、Codex と Antigravity では1,800秒）。ツールの詳細は `CLAUDE.md` に記載されている。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** — 15言語で公開されている個人ブログ。その[毎日の AI ウォッチ](https://jls42.org/fr/news)は、このツールで毎日翻訳され、上記の測定における基準文書として使用されている。

## 著者

Julien LE SAUX  
メール：contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。[LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)を参照。

## 免責事項

このプログラムは、GPL v3 の第15条および第16条の規定に基づき、**いかなる保証もなく**配布される。「現状のまま」提供され、商品性または特定目的への適合性について一切保証されず、使用により生じたいかなる損害についても作者は責任を負わない。本要約よりライセンス本文が優先される。

- **公開前に必ず確認すること。** 保護の対象は、コードブロック、インラインコード、URL、アンカー、および `--news` モードの引用であり、見出し、表、front matter、文章の意味は対象外である。
- **文書は、選択したプロバイダーに送信される。** その利用規約およびデータポリシーが適用される。一部の無料モデルでは、やり取りが学習に再利用される場合がある。また、Antigravity の規約では、有料サブスクリプションを含め、Google がそれらを再利用し、人間による確認を行うことが認められている。データを端末の外部へ一切送信しない唯一の方法は、ローカルモデルを使用することである。
- **API 呼び出しには料金が発生する。** このプログラムは支出額に上限を設けない。長い文書、失敗後の再実行、または推論量の多いモデルほど費用が高くなる。
- **公開されている測定値は特定時点での観測結果であり**、保証ではない。

記載されている製品名および企業名は、それぞれの権利所有者に帰属する。このプロジェクトは、それらのいずれとも提携していない。

**gpt-5.6-solでフランス語から日本語に翻訳された記事。**
