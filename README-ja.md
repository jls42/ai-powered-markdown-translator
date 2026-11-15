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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="重複行数（%）"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="技術的負債"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="コード行数"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacyバッジ"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Markdownファイルを、構造を保ちながら別の言語に翻訳します。
コードブロック、インラインコード、URL、アンカー、表、フロントマターを
維持します。モデルの呼び出し方法は11通り。5つのAPI、従量課金のない
4つのサブスクリプション、2つのルーターに対応し、各モデルが実際に
何を保持できるかを測定した結果も公開しています。

## 概要

- **11通りのプロバイダー接続方法**：OpenAI、Mistral、Claude、Gemini、GrokのAPI；
  従量課金のないChatGPT（Codex）、Grok、Google（Antigravity）、Claude（Claude
  Code）のサブスクリプション；OpenCode（オープンソース、無料またはローカル）とOpenRouter
  （400以上のモデル）のルーター。
- **トークンの欠落による破損を防止**：コードブロック、インラインコード、
  URL、アンカー、引用を呼び出し前にトークンに置き換え、
  応答後に検証します。1つでも欠けていれば、ファイルは書き込みません。
- **長い文書に対応**：モデルのコンテキストウィンドウに応じて分割します。
- **`--news`モード**：英語の引用を保護し、言語ごとにフラグを管理する、
  情報収集記事向けのモード。
- **`--eco`モード**：高速で安価なモデルを使用します。
- **翻訳注記**を任意で先頭、末尾、または両方に追加できます。

## インストール

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11以降が必要です。リポジトリからインストールする方法は、
[貢献方法](#貢献する)を参照してください。

## 設定

キーは次の3か所から優先順位の高い順に読み込まれます。各場所の設定は、
それより優先順位の高い場所で未設定の項目だけを補います。

|     | 場所                                            | 用途                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 環境変数                     | CI、コンテナー、一時的な上書き |
| 2   | 現在のディレクトリ（または親ディレクトリ）の`.env` | プロジェクト固有のキー            |
| 3   | `~/.config/aipmt/.env`                        | 一度設定すれば、どこでも有効       |

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

`GOOGLE_API_KEY`の代わりに`GEMINI_API_KEY`も使用できます。ユーザー設定ファイルは
`XDG_CONFIG_HOME`（絶対パスのみ）に従い、Windowsでは`%APPDATA%`に
従います。キーがない場合、コマンドは3つの場所を列挙します。

**プロジェクトの`.env`では、呼び出し先の変更も、実行するプログラムの
選択もできません。** 提供するのはキーだけであり、接続先やバイナリではありません。
`_BASE_URL`、`_API_BASE`、`_ENDPOINT`、`_BIN`に該当する変数（`CODEX_BIN`、
`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`）、`GROK_HOME`、プロキシ（`HTTP_PROXY`、
`HTTPS_PROXY`、`ALL_PROXY`）、証明書ストア（`SSL_CERT_FILE`、
`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）、`XDG_CONFIG_HOME` /
`APPDATA`はすべて、このファイル内では警告とともに無視されます。クローンした
リポジトリがキーを盗用したり、最初の翻訳時に独自のプログラムを実行させたり
できてはいけません。このファイルは変数展開なしで読み込まれるため、
`NOM=${OPENAI_API_KEY}`でキーがコピーされることもありません。これらの変数は
環境変数または`~/.config/aipmt/.env`に設定してください。

任意の変数：`XAI_BASE_URL`（既定値`https://api.x.ai/v1`）、
`CLAUDE_TIMEOUT`（呼び出しごとの秒数、既定値900）、`CODEX_BIN`、`CODEX_TIMEOUT`
（既定値600）、`GROK_BIN`、`GROK_HOME`（既定値`~/.grok`）、`GROK_TIMEOUT`
（既定値900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（既定値900）、
`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（既定値600）、`OPENROUTER_BASE_URL`
（`https://`が必須）、`OPENROUTER_TIMEOUT`（既定値900）、
`OPENROUTER_PREFLIGHT_TIMEOUT`（既定値30）。それぞれの詳細は、
対応するプロバイダーの節に記載しています。

## はじめに

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md`をスペイン語に翻訳すると、`--target_dir`に`document-es.md`が作成されます。
`--include_model`を指定すると、`document-es-gpt-5.6-terra.md`になります。拡張子は
常に`.md`になります。たとえば、`article.mdx`は`article-en.md`になります。ただし、
`--keep_filename`を指定すると元の名前が保持されます。既存の翻訳は、
`--force`がなければスキップされます。

終了コード：すべて成功またはスキップされた場合は`0`、失敗したファイルが
残っている場合は`1`（標準エラー出力に一覧を表示）、設定に問題がある場合は`2`です。
失敗したファイルは、書き込み自体が失敗した場合も含め、書き込まれません。
内容を隣接するファイルに書き込んでから名前を変更します。再実行するだけで再試行できます。

## モデルの選び方

実際の文書2つを、各モデルで同じ14言語に翻訳して測定しました。
**数値は14言語のうち、翻訳ファイルが書き込まれ、かつ原文との相違が
なかった言語の数です。**

| モデル                | 利用方法                 | 情報密度の高い情報収集記事 | このREADME    | 相違点と該当する言語数                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Googleサブスクリプション（Antigravity）   | ✅ 14/14                | ✅ 14/14     | 両方の文書で相違なし                                                                                                                                 |
| **Claude Sonnet 5.5** | AnthropicのAPIキー                 | ✅ 14/14                | ✅ 14/14     | 両方の文書で相違なし                                                                                                                                 |
| **Gemini 3.7 Flash**  | GoogleのAPIキー                    | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語：太字の単語が1つ増加（ja）                                                                                                                      |
| **Gemini 3.7 Flash**  | Googleサブスクリプション（Antigravity）   | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語：太字の単語が1つ減少（ko）                                                                                                                     |
| **GPT-5.6 Sol**       | ChatGPTサブスクリプション、またはOpenAIのキー | ✅ 14/14                | ⚠️ 12/14     | 14言語中2言語：太字の単語が1つ減少（ar, ja）                                                                                                                |
| **GLM-5.2**           | OpenRouterのキー                    | ✅ 14/14                | ⚠️ 11/14     | 14言語中3言語：太字の単語が1つ減少（hi, ja, ko）                                                                                                            |
| Claude Sonnet 5       | Claudeサブスクリプション（Claude Code）   | ⚠️ 13/14                | ⚠️ 13/14     | 記事では14言語中1言語：太字の単語が1つ増加（zh）；このREADMEでは1言語：表の行が前の行に連結され、表示されなくなった（ar）            |
| Claude Haiku 4.5      | Claudeサブスクリプション（Claude Code）   | ⚠️ 11/14                | ✅ 14/14     | 記事では3言語：節の見出しがレベル1に変更（en, pl, ro）；このREADMEでは比較ツール上の相違はないものの、内部リンクが英語でも重複して追加された |
| Claude Sonnet 5       | AnthropicのAPIキー                 | ⚠️ 11/14                | ⚠️ 12/14     | 記事では3言語：コードブロックが追加（es, de, hi）；このREADMEでは2言語：リンクのマークアップが欠落（sv）、単語の太字に相違（zh）                              |
| Claude Haiku 4.5      | AnthropicのAPIキー                 | ⚠️ 7/14                 | ✅ 14/14     | 記事では7言語：節の見出しがレベル1に変更され、日本語ではフランス語のまま残った；このREADMEでは相違なし                                              |
| Claude Haiku 5.5      | AnthropicのAPIキー                 | ⚠️ 11/14                | ❌ 12/14     | 記事では3言語：節の見出しのレベルが変更、または見出しが重複（ja, ko, zh）；このREADMEでは2言語でインラインコードが欠落したため出力を拒否（ar, hi）    |
| Qwen 3.7 Flash        | OpenRouterのキー                    | ❌ 8/14                 | ⚠️ 10/14     | 記事では1言語の出力を拒否し、ほかの5言語にも相違あり；このREADMEでは約40語が`code`で囲まれた（ar）                                                    |
| Grok 4.6              | Grokサブスクリプション                   | ❌ 8/14                 | 未評価     | インラインコードとURLが返されなかったため、14言語中5言語の出力を拒否；オランダ語では全体に相違あり                                                               |
| GPT-OSS 20B           | ローカルモデル（Ollama）             | ❌ 7/14                 | 未再測定 | 14言語中4言語の出力を拒否：フランス語のまま残った箇所があり、保護機能が出力を停止                                                                  |
| MiMo v2.5（無料）   | OpenCode Zen、アカウント不要         | ❌ 11/14                | 未再測定 | 1言語の出力を拒否；ポーランド語で節が1つ欠落                                                                                                                  |
| Mistral Large         | MistralのAPIキー                   | ❌ 5/14                 | ❌ 1/14      | **節全体が消失**：記事では1言語（hi）、このREADMEでは3言語（ar, hi, ko）で発生。さらに記事では3言語の出力を拒否                                |
| DeepSeek V4 Flash     | OpenRouterのキー                    | ❌ 3/14                 | 未再測定 | 14言語中10言語の出力を拒否；1言語あたり37分                                                                                                                 |
| Claude Opus 5.5       | Claudeサブスクリプション（Claude Code）   | ❌ 0/14                 | ✅ 14/14     | 生物学の短い記事が原因で、Opusのガードレールが14言語すべてで記事の翻訳を拒否；このREADMEでは相違なし                                               |

|     | 記号の意味                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14言語すべてを翻訳し、原文との相違なし                                                                                                                                       |
| ⚠️  | 14言語すべてを翻訳；相違は**マークアップ**のみ。単語の太字、`code`、角括弧が欠落したリンクなど。本文、URL、コードブロック、節の欠落はなし |
| ❌  | 少なくとも1言語で翻訳できず、ファイルの出力が拒否されて書き込まれなかった、**または**書き込まれたファイルに内容の欠落がある                                                                      |

結果から分かること：

- **出力を拒否された翻訳は、破損した翻訳ではありません。** 応答でトークンが
  欠けていれば、ファイルは書き込まれず、その言語は出力拒否として
  集計されます。記事でのGrokがその例です。非ラテン文字を使う5言語では、
  最初の分割部分からインラインコード4つとURL3つが欠落しました。
- **たった1文が原因で、モデルが文書全体の翻訳を拒否することがあります。** Opus 5.5は
  このREADMEを相違なく翻訳しますが、情報収集記事はどの言語でも翻訳できません。
  生物学の短い記事でガードレールが応答を停止するためです。ファイルは
  書き込まれず、aipmtが理由を表示します。
- **この保護機能は、見出し、表、フロントマター、本文を
  対象としていません。** モデルが節を削除しても、ツールは返されたファイルを
  そのまま書き込みます。Mistralがその例です。これらの要素は
  トークンに置き換えられず、現在の保護機能では検証されません。
  `scripts/compare_structure.py`は節の欠落を検出しますが、あくまで事後の検出です。
- **このREADMEについてGrokの評価はありません**：CLIセッションが12言語の
  処理後に期限切れとなり、そのうち11言語では相違がありませんでした。中断された測定は評価しません。
- **言語よりも文書の情報密度が重要です。** Grokは通常の
  READMEには対応できますが、リンクの多い記事ではオランダ語を含めて
  翻訳が崩れます。

測定日と文書：「このREADME」列は、2026年9月9日にこのファイルの
固定したリビジョン（785行、インラインコード285個、表89行）で測定しました。
ファイルはその後修正されています。ただし、AntigravityとClaude Codeの行は、
9月26日に1.14.0とともに公開された、より短いリビジョン
（600行、インラインコード257個、表85行）で測定しました。また、
API経由のClaude Sonnet 5.5、Haiku 5.5、Haiku 4.5の行は、10月18日に
同じリビジョンで測定しました。「情報密度の高い情報収集記事」列は、
9月4日と5日に589行の記事で実施した測定に基づきます。ただし、Grokの行は
9月9日に同じ情報収集記事の別の版で再測定し、Antigravityと
Claude Codeの行は9月26日に同じ記事で、これら3つのClaudeの行は
10月18日に測定しました。完全な表、所要時間、測定手順は
[詳細な測定結果](#詳細な測定結果)に記載しています。
## すべてのオプション

| オプション                   | 説明                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 翻訳する単一の Markdown ファイル（`--source_dir` の代わりに指定）                                             |
| `--source_dir`           | Markdown ファイルを含む入力ディレクトリ（既定値：`content/posts`）                                   |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ（既定値：`traductions_en`）                                    |
| `--source_lang`          | 原文の言語（既定値：`fr`）                                                                                  |
| `--target_lang`          | 翻訳先の言語（既定値：`en`）                                                                                   |
| `--model`                | 使用する特定のモデル                                                                                  |
| `--eco`                  | 低コストモデルを使用                                                                              |
| `--use_mistral`          | Mistral AI の API を使用                                                                                     |
| `--use_claude`           | Claude の API を使用                                                                                         |
| `--use_gemini`           | Gemini の API を使用                                                                                         |
| `--use_grok`             | xAI（Grok）の API を使用 — `XAI_API_KEY` が必要                                                           |
| `--use_codex`            | ChatGPT サブスクリプションの利用枠で Codex の CLI を使用                                                    |
| `--use_grok_cli`         | Grok サブスクリプションの利用枠で Grok の CLI を使用                                                        |
| `--use_antigravity`      | Google AI Pro または Ultra サブスクリプションの利用枠で Antigravity の CLI（`agy`）を使用                       |
| `--use_claude_code`      | Claude Pro または Max サブスクリプションの利用枠で Claude Code の CLI（`claude -p`）を使用                      |
| `--use_opencode`         | OpenCode（オープンソース）を使用し、OpenCode で設定したプロバイダーに接続；`--model provider/modèle` が必要 |
| `--use_openrouter`       | OpenRouter を使用 — `OPENROUTER_API_KEY` と `--model fournisseur/modèle` が必要                          |
| `--force`                | 再翻訳を強制                                                                                       |
| `--keep_filename`        | 元のファイル名を保持                                                                          |
| `--news`                 | ニュースモード：英語の引用を保護し、言語ごとのフラグを処理                                      |
| `--add_translation_note` | 翻訳注記を追加                                                                                |
| `--note_position`        | 注記の位置：`top`、`bottom`（既定値）、または `both`                                                     |
| `--note_format`          | 注記の形式：`legacy`（既定値、太字の段落）または `marker`                                            |
| `--include_model`        | 出力ファイル名にモデル名を含める                                                            |
| `--reasoning_effort`     | GPT-5.x の推論量：`none`/`low`/`medium`/`high`/`xhigh`                                         |

9 つの `--use_*` フラグは相互排他的です。2 つを組み合わせると
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

`--eco` は各プロバイダーの低コスト枠に切り替えます。

| プロバイダー    | 高品質（既定）                                                     | 低コスト（`--eco`）      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.8-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol`（`--model` で `gpt-5.6-sol`、`terra`、`luna` も指定可能） | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | 同じ — `--eco` は効果なし |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`、推論量 `low`                                               | 同じ — `--eco` は効果なし |
| OpenCode    | `--model provider/modèle` が必須                                | 同じ — `--eco` は効果なし |
| OpenRouter  | `--model fournisseur/modèle` が必須                             | 同じ — `--eco` は効果なし |

1.17.1 まで既定だった Gemini 3.7 Flash は非推奨になりました。Google は
代わりに Gemini 3.8 Flash を提供しており、`--model gemini-3.7-flash` も引き続き使用できます。
Gemini の API に一時的な障害（503、429、タイムアウト）が発生した場合、
10、20、40 秒待機して、最大 3 回呼び出しを再試行します。応答のない試行は
5 分で打ち切り、同様に再試行します。
このため、サーバーが応答しない場合でも無期限に停止することはなく、
長くても約 20 分でそのセグメントが失敗します。

### ChatGPT サブスクリプションでの利用：`--use_codex`

公式の Codex CLI を操作します。翻訳は ChatGPT サブスクリプションの
利用枠から差し引かれ、API キーや従量課金は不要です。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 実行ファイルは `CODEX_BIN`、`PATH`、パッケージ
  `openai-codex-cli-bin` の順に検索します。`~/.codex/auth.json` は一切読み取りません。
- `OPENAI_API_KEY` と `CODEX_API_KEY` はサブプロセスの環境から
  削除されます。キーが存在しても API に切り替わることはありません。
- 各セグメントは 5 時間の利用枠で少なくとも 1「メッセージ」を消費し、
  検証に失敗して再試行した場合は 2 メッセージを消費します。OpenAI が
  Plus プランについて公表している目安は、`gpt-5.6-luna`（`--eco`）で
  250-2 000 メッセージ/5 時間、`gpt-5.6-sol` で 10-100 メッセージです。
- 1.16.3 まで既定だった `--model gpt-5.6-sol`、`--model gpt-5.6-terra`、
  `--model gpt-5.6-luna` もサブスクリプション経由で利用できます。
- サーバーが 429 を返してもファイルは失われません。Codex が自動で再接続し、
  aipmt はターンの終了を待ちます。それでも最終的に 429 で終わった場合は、
  30 秒、続いて 60 秒待ってセグメントを再試行します。アカウントに利用権限のないモデルでは、
  400「ChatGPT アカウントで Codex を使用する場合、このモデルはサポートされていません」が返されます。
- API より遅く、文書が長くなるほど差が広がります。この README では、
  `gpt-5.6-sol` の言語あたりの中央値が 6 分 46 秒だったのに対し、
  `gemini-3.7-flash` は 36 秒でした。
- CI（`CI` または `GITHUB_ACTIONS` が設定されている場合）では拒否されます。
  サブスクリプションは個人用のセッションファイルで認証するため、
  共有ランナーに置くべきではないからです。
- 変数：`CODEX_BIN`、`CODEX_TIMEOUT`（セグメントあたりの秒数、既定値 600）。

### Grok サブスクリプションでの利用：`--use_grok_cli`

公式の Grok Build CLI を使い、SuperGrok または
X Premium+ サブスクリプションで同じ仕組みを利用できます。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **隔離は Codex より弱くなります。** Grok の OS サンドボックスは、
  最近の多くの Linux 環境では適用されず（AppArmor、コンテナーランタイムの
  ソケット）、適用できないプロファイルは警告なしに隔離されない状態で起動します。
  そのため、スクリプトは既定でプロファイルを要求せず、その旨を通知し、
  包括的な `*` を含む CLI の `--deny` ルールに依存します。
  これは、保護を黙って解除する代わりに起動を拒否する唯一の層です。
  `GROK_TRANSLATE_SANDBOX=read-only` は OS サンドボックスを必須にし、
  マシンで適用できなければ起動に失敗します。
- 利用枠は週単位で、Chat、Imagine、Voice と共有されます。
  残量を確認するコマンドはないため、バッチ処理によって会話用の利用枠が
  通知なく消費されることがあります。
- 変数：`GROK_BIN`、`GROK_HOME`（CLI のディレクトリ、既定値 `~/.grok`）、
  `GROK_TIMEOUT`（既定値 900）、`GROK_TRANSLATE_SANDBOX`。

### Google サブスクリプションでの利用：`--use_antigravity`

Antigravity の公式 CLI である `agy` でも同じ仕組みを利用できます。
Google AI Pro または Ultra の契約者は、トークン単位で課金される代わりに、
翻訳がサブスクリプションの利用枠から差し引かれます。この利用枠を使う方法は
これだけです。Gemini CLI は 2026 年 6 月 18 日以降、これらのアカウントに対応しておらず
（[告知](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)）、
Antigravity の SDK は API キーか Google Cloud プロジェクトしか受け付けません。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **従量課金に移行する経路を一切残しません。** agy に渡す環境変数は、
  `PATH`、言語とタイムゾーン、端末、ユーザー識別情報、プロキシと証明書、
  セッションバスという限定された許可リストだけで、キーは一切渡しません。
  agy の複数の変数は、通知せずに呼び出し先を切り替えます（実測では、
  ある変数は文書を第三者のゲートウェイに送信し、別の変数は課金対象の
  Google Cloud プロジェクトに送信しました）。拒否リスト方式では、
  見直すたびに漏れが見つかりました。各セグメントの処理前に、利用枠を消費しない
  `agy -p /config` で、有料の AI クレジットが無効になっており、
  API キーも Google Cloud プロジェクトも設定されていないことを確認する必要があります。
  設定がない場合も拒否とし、条件を満たさなければ翻訳は行いません。
  さらに、各呼び出しのログでサブスクリプションの利用（`authMethod=consumer`）が
  証明されなければ、応答を拒否します。
- **隔離。** 各呼び出しは、ツールを持たない翻訳エージェントを使い、
  非公開の使い捨てホームディレクトリで実行されます。ユーザーの agy の設定、ルール、
  プラグイン、MCP サーバー、フックは持ち込まれず、履歴にも何も追加されません。
  ログイン情報はキーリングに残り、aipmt が読み取ることはありません。
  エージェントが見つからないと、agy は警告せずにコーディングエージェントと
  そのツールに切り替わります。そのため、ログの行全体で正しいエージェントを確認する
  必要があります。文書中にこのメッセージが引用されていても代用にはならず、
  確認できなければ拒否します。
- **プラットフォーム**：キーリング（D-Bus セッションバス、Secret Service）がある
  セッション内の Linux。macOS も使用可能ですが、実測はしていません。
  Windows では、各呼び出しを隔離する環境変数を agy が読み取らないため拒否されます。
  セッションバスのない Linux（SSH セッション、コンテナー、サーバー）でも拒否されます。
  その環境では agy がトークンを `~/.gemini` 内のファイルに保存し、
  隔離によってそのファイルが見えなくなるためです。ログインコードを待って 1 分経つ前に、
  起動前の段階で理由とともに拒否します。
- **モデル**：`agy models` のモデルです。Gemini は名前に推論量を含みます
  （`gemini-3.8-flash-medium` など）。接尾辞のない名前は呼び出し前に拒否され、
  `--reasoning_effort` は効果がありません。既定は `gemini-3.8-flash-medium`、
  `--eco` では `gemini-3.7-flash-low` です。これらの選定に用いた測定は
  [詳細な測定結果](#詳細な測定結果)で説明しています。Claude と GPT-OSS には
  独自の利用枠があり、はるかに小さくなっています。実測では 1 回の呼び出しで
  5 時間枠の約 1 % を消費し、Flash の 0.05 % と差があります。
- **利用枠**：グループごとに 5 時間枠と週単位の枠があり、
  トークンコストに比例して消費されます。著者のアカウントでの実測では、
  原文 100 万文字あたりの 5 時間枠の消費は `gemini-3.8-flash-medium` で約 16 ポイント、
  `gemini-3.7-flash-medium` で 14 ポイント、低い推論量では 7～8 ポイントでした。
  したがって、40 000 文字の README は半ポイント強を消費します。
  一方、週単位の上限はプランによって異なります。再試行は agy が再試行可能と
  判定した場合に従います。それ以外の場合、使い切った利用枠で再試行することはありません。
  `/usage` に表示されるリセット時刻まで、各ファイルの処理が失敗します。
- **API より低速**：測定に使用した情報密度の高い記事では、言語あたりの中央値が
  `gemini-3.8-flash-medium` で 3 分 59 秒、
  `gemini-3.7-flash-medium` で 3 分 14 秒でした。一方、API 経由の Gemini 3.7 Flash は 1 分 18 秒でした。
- **中断**：Ctrl-C や端末を閉じる操作で、コマンドとともに agy も停止します。
  利用枠を消費しながらターンを完了するまで動作し続けることはありません。
  Codex、Grok CLI、OpenCode も同様です。`nohup` では翻訳が継続します。
- CI（`CI` または `GITHUB_ACTIONS` が設定されている場合）では拒否されます。
  ログイン情報が個人用キーリングに保存されるためです。ランナーでは、
  `--use_gemini` を `GOOGLE_API_KEY` とともに使用してください。
- 変数：`AGY_BIN`（未指定なら `PATH`、続いて `~/.local/bin/agy`）、
  `AGY_TIMEOUT`（起動時間を含むセグメントあたりの秒数、既定値 900）。

**利用規約：責任を負うのはご自身のアカウントです。**
[Antigravity の利用規約](https://antigravity.google/terms)（第 6 条）と
[よくある質問](https://antigravity.google/docs/faq/)では、Antigravity のログイン情報を使って
第三者のソフトウェアからサービスにアクセスすることを禁じており、
Claude Code、OpenClaw、OpenCode が例示されています。違反するとアカウントが
停止される可能性があります。aipmt はトークンを読み取ったり再利用したりせず、
Google がスクリプトや CI 向けに文書化している
[ヘッドレスモード](https://antigravity.google/docs/cli/headless/)で公式の実行ファイルを起動します。
Google のメンバーは、自分の作業のためにローカルスクリプトから
`agy -p` を起動することを「標準的」と評価しています
（[公式フォーラム、2026 年 9 月 25 日、契約上の効力を持たない回答](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）。
ただし、このように配布されるツールの扱いを明確に判断できる文書はありません。

**公開文書のみを対象にしてください。** 同じ利用規約の第 5 条によると、
やり取り（プロンプト、応答、メタデータ）は、有料サブスクリプションでも
Google の製品や機械学習の改善に使用され、人間が確認する場合があります。
対象から外すには `enableTelemetry` の設定を使いますが、その効果は文書化されておらず、
aipmt はこの設定を行いません。ユーザーの agy の設定は隔離環境に引き継がれません。
機密情報は一切送信しないでください。
### Claude サブスクリプションでの利用：`--use_claude_code`

Claude Code の公式 CLI である `claude` を `-p` モードで使う場合も、原理は同じです。
Claude Pro または Max の利用者は、翻訳がトークン単位で課金される代わりに、
サブスクリプションの割り当てから差し引かれます。
従量課金の Anthropic API である `--use_claude` とは異なります。

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **有料の経路はすべて閉じられ、各呼び出しでそれを確認します。** Claude
  Code に環境から渡されるのは、限定された変数の一覧だけです。
  API キー、トークン、クラウドプロバイダー、aipmt の起動元となる Claude Code
  セッションの識別情報は渡されません。最初のセグメントの前に、`claude auth status` が
  Console キーを使わないサブスクリプション接続を示し、割り当てを
  消費しない `/usage` がそれを証明する必要があります。各呼び出しでも
  初期化イベントで同じことを確認できなければ、応答を拒否します。
- **「追加使用」を無効にしてください**（claude.ai、設定 → 使用量）。
  これで費用をゼロユーロに保てます。有効にすると、利用枠を使い切った際に
  自動的に切り替わり、エラーを表示せずに課金されます。aipmt は呼び出しの
  割り当てレポートにその状況が示された時点で翻訳を停止しますが、その呼び出し分はすでに計上されています。
- **割り当ては Claude Code セッションと共有されます。** 各呼び出しは、
  5 時間枠と週間枠の使用量を報告します。80 %
  （`AIPMT_CLAUDE_MAX_UTILIZATION`）を超えると、仕事に必要な枠を使い切らないように、
  追加のセグメントを開始しません。
- **隔離。** 各呼び出しは、ツールなしで、非公開の使い捨てディレクトリ内で、
  カスタマイズを無効にして実行されます。`CLAUDE.md`、プラグイン、
  フック、MCP サーバー、設定は読み込まれず、セッションの情報も保存されません。
  添付ファイルも無効です。文書内の `@chemin` はテキストのままで、
  ファイルを開きません（実測済み）。
- **モデル**：既定は `sonnet`、推論の強度は `low` で、`--eco` でも同じです。
  この経路では `--eco` は影響しません。同じ文書で測定したところ、`haiku` は
  2 倍遅く、推論を止められない一方で、費用はわずかに低い程度でした。
  `opus` は生物学の内容を拒否します（次の項目を参照）。
  どちらも `--model` から利用できます。これらの別名は、
  各系列の最新モデルに追従します。`fable` と `[1m]` の派生版は、
  有料クレジットに切り替わるため拒否されます。`--reasoning_effort` は推論の強度を設定しますが、
  翻訳には効果がなく、測定された推論量はゼロか、ほぼゼロでした。
- **Opus は一部の生物学コンテンツを拒否します。** 安全措置が
  Sonnet より厳しく、Anthropic のエラーメッセージにも、
  「生物学研究に関連する作業が検出対象になることがある」と記されています。
  実測では、生成された 279 種の分子に関する短いニュース記事が原因で、
  14 言語すべてで記事が拒否されました。ファイルは書き込まれません。
  aipmt は途中で切れた応答を拒否し、安全措置が原因であることを示して `--model sonnet` を勧めます。
- CI（`CI` または `GITHUB_ACTIONS` が設定されている場合）および Windows では拒否されます（未測定）。
- 変数：`AIPMT_CLAUDE_BIN`（未設定なら `PATH`、次に `~/.local/bin/claude`）、
  `AIPMT_CLAUDE_TIMEOUT`（セグメントあたりの秒数、既定値 900）、
  `AIPMT_CLAUDE_MAX_UTILIZATION`（既定値 0.8）、`CLAUDE_CONFIG_DIR`（Claude Code の
  アカウント。プロジェクトの `.env` からは取得しません）。作業ディレクトリは
  `XDG_CACHE_HOME/aipmt/claude-code` の下に置かれます（既定値 `~/.cache`）。

**利用規約：責任を負うのはご自身のアカウントです。**
[Claude Code の法的事項のページ](https://code.claude.com/docs/en/legal-and-compliance)では、
「エンドユーザーが、自分の Claude サブスクリプションを使って、改変されていない
Claude Code のバイナリにログインすること」は禁じていません。aipmt が行うのはまさにこれで、
公式バイナリを起動し、トークンを読み取ることはありません。ただし Anthropic は、
「第三者の開発者が［…］利用者に代わって Free、Pro、Max プランの認証情報を使って
リクエストを中継することを認めない」としており、
「オープンソースプロジェクトを含む」第三者のツールには API キーの使用を推奨し、
その使用量を有料クレジットから差し引く権利を留保しています
（[Claude ヘルプ](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)）。
配布されたツールがバイナリを起動する場合について、明確に判断を示す文書はありません。

**データ**：Free、Pro、Max アカウントでは、プライバシー設定で許可している場合、
Claude Code のデータもモデルの学習に使用されます
（[データに関するページ](https://code.claude.com/docs/en/data-usage)）。aipmt は
ローカルに会話記録を保存しません（`--no-session-persistence`）。
機密情報を送信しないでください。

### 好みのプロバイダーへの接続：`--use_opencode`

[OpenCode](https://opencode.ai) は、内部に設定されたプロバイダーへ
接続するオープンソースのコーディングエージェント（MIT）です。API キー、サブスクリプション、
OpenCode Zen ゲートウェイ（無料モデル、アカウント不要）、ローカルモデルを利用できます。
ここでは Zen と Ollama の 2 つの経路を、最初から最後まで測定しました。

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

`--model` は必須です。指定しないと、OpenCode はやり取りが学習に
使用される可能性のある無料モデルに切り替わってしまいます。
その選択を利用者に代わって行うことはしません。

各呼び出しでの隔離：

- 利用者の設定より優先されるインライン設定で、すべてのツールを拒否する
  （`permission: { "*": "deny" }`）エージェント `aipmt` を定義します。セッション共有は無効、
  `--pure` を使用し、`--auto` は使用しません。
- 空の使い捨て作業ディレクトリを用意し、`OPENCODE_DISABLE_PROJECT_CONFIG` と
  `OPENCODE_DISABLE_CLAUDE_CODE` を設定します。これらがないと、OpenCode は現在の
  ディレクトリの `AGENTS.md` と `~/.claude/CLAUDE.md` をプロンプトに挿入します。
  グローバルな `~/.config/opencode/AGENTS.md` は挿入されたままです。OpenCode には、
  これを除外する機能がありません。
- 出力の条件：終了コード 0、`error` イベントなし、ツール呼び出しなし、
  最後のステップが `stop`、テキストが空でないこと、エージェント `aipmt` が
  実際に読み込まれていること。不明な `--agent` を指定しても OpenCode は失敗せず、
  コーディングエージェントへ無言で切り替わります。
- `aipmt` のキーは一切渡しません。ただし、OpenCode 自体のキーである
  `OPENCODE_API_KEY` は例外です。プロバイダーは OpenCode 内で設定し、
  `aipmt` の `.env` では設定しません。

注意点：

- Zen の無料モデルは入れ替わり、制限も公開されていません。
  やり取りが学習に使用される可能性もあります。公開文書向けであり、非公開の内容には適しません。
- ローカルモデルには、少なくとも 16 k トークンのコンテキストが必要です。
  セグメントは最大 16 000 文字になるためです。Ollama では 4 096 に設定されていることが多いため、
  `PARAMETER num_ctx 32768` を指定した `Modelfile` を使用してください。
- `--eco` は影響しません。`--reasoning_effort` は、そのまま
  OpenCode の `--variant` として渡されます。
- OpenCode は各セッションを `~/.local/share/opencode/` に記録します。
- 変数：`OPENCODE_BIN`（未設定なら `PATH`、次に `~/.opencode/bin/opencode`）、
  `OPENCODE_TIMEOUT`（セグメントあたりの秒数、既定値 600）。`OPENCODE_CONFIG` は
  そのまま OpenCode に渡されます。

`~/.config/opencode/opencode.json` での、Ollama を介したローカルモデルの例：

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

`reasoningEffort: "none"` は、Ollama がこれらのモデルで既定で有効にする推論を
無効にします。これは Modelfile では無効にできません。6 語の文で測定したところ、
このオプションなしでは推論に 919 トークンと 68 秒を費やし、指定した場合は 9 トークンでした。

### 400 を超えるモデルへの接続：`--use_openrouter`

OpenRouter は、単一のクレジット残高で従量課金されるルーターで、
第三者がホストするモデルに接続します。ここで扱うほかのプロバイダーでは
提供されていない、中国のオープンモデルも含まれます。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` は必須です。課金が発生する前に事前確認を実行し、
ルーティングに特有の 2 点に対応します。

- **同じモデルでも、上限の異なる数十のホスティング事業者から提供されます。**
  `z-ai/glm-5.3-flash` では 23 社あり、そのうち 1 社は出力が
  2 048 トークンに制限されています。事前確認では `/api/v1/models/{modèle}/endpoints` を読み取り、
  出力上限が 8 000 トークン未満の事業者や稼働状況が悪化している事業者を除外し、
  残りを `allow_fallbacks: false` で固定します。
- **推論は出力と同じ料金で課金されます。** `z-ai/glm-5.2` の
  「OK」という応答では、2 トークンに対して 107 トークンでした。推論は既定で無効にします。
  推論を必須とするモデルには、そのモデルが受け付ける最小の強度を指定します。
  カタログの既定値では、翻訳が終わる前に出力枠を使い切る可能性があるためです。
  `--reasoning_effort` が優先されます。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- コンテキスト枠はカタログから取得します。16 400 トークン未満のモデルは、
  呼び出し前に拒否されます。プロンプトとセグメントに 8 400、
  出力に最低 8 000 が必要です。
- スラッグがカタログにない場合、カタログに接続できない場合、
  または必要な上限を満たすホスティング事業者がない場合は、コマンドを停止します。
- `finish_reason=length` で出力が空の場合は、推論が予算を使い切ったのであり、
  出力の切り詰めではありません。メッセージで区別します。
- `--eco` は影響しません。
- 変数：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>）、
  `OPENROUTER_BASE_URL`（既定値 `https://openrouter.ai/api/v1`、`https://`
  必須）、`OPENROUTER_TIMEOUT`（既定値 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`
  （既定値 30）。

### 翻訳注記

`--add_translation_note` は、`bottom`（既定）、`top`（フロントマターの後）、
または `both`（`--note_position`）に注記を追加します。形式は `legacy`（太字の
段落、既定）または `marker`（`--note_format`）です。`marker` 形式は、
表示されない Markdown の参照定義
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`
に続けて、太字の引用を配置します。GitHub で読むことができ、
ビルド時には remark プラグインで利用できます。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 詳細な測定結果

測定はすべて `aipmt` で実際に翻訳を実行したもので、
対象は 14 言語です：en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi。
**書き込み済み**は検査を通過したファイル数、**差異なし**は
`scripts/compare_structure.py` が何も検出しなかったファイル数です。セクション、小見出し、
リンク、重複を除いた URL、コードブロック、インラインコード、
表の行、引用ブロック、太字の語の数が同じであることを確認します。

「差異なし」は「何も検出されなかった」という意味であり、「同一」という意味ではありません。
比較ツールは内容を読まずに要素を数えます。レベル 4 の見出しの削除、
インラインコードのテキストの置き換え、旗の変更、
閉じ括弧が 1 つ多くなって機能しなくなった内部リンク
`[texte]((#ancre))` は検出しません。
また、言語の適否も判定しません。

### 情報量の多い動向記事、`--news` モード

[jls42.org の AI 動向記事](https://jls42.org/fr/news)の 1 回分：
589 行、140 リンク、21 セクション、保護された英語の引用 3 件。
2026 年 9 月 4 日と 5 日に測定しました。

| モデル                                          | アクセス方法              | 書き込み済み | 差異なし   | 言語あたりの中央値 |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | Google API         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google サブスクリプション  | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google サブスクリプション  | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `claude-sonnet-5-5`                             | Anthropic API      | 14/14   | ✅ **14/14** | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | ChatGPT サブスクリプション | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | Claude サブスクリプション  | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | Anthropic API      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | Claude サブスクリプション  | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `claude-haiku-5-5`                              | Anthropic API      | 14/14   | ⚠️ 11/14     | 2 min 54 s     |
| `claude-haiku-4-5`                              | Anthropic API      | 14/14   | ⚠️ 7/14      | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | ローカル              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | Mistral API        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | Grok サブスクリプション    | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | Claude サブスクリプション  | 0/14    | ❌ 0/14      | —              |

Grok は 9 月 9 日に、同じ動向記事の別の回（356 行）で再測定しました。
14 言語中 9 言語を書き込み、8 言語は差異なしでした。
冒頭の表にはこの数値を掲載しています。中断した 3 回の測定は記載していません。
`qwen3.5-27b`（9 言語）と `kimi-k2.6`（4 言語）はクレジット不足、
`z-ai/glm-5.3-flash` の 2 件の失敗は、その後プロバイダー側で修正された
推論設定が原因でした。OpenRouter の各行は、
`--use_openrouter` 導入前のルーターの既定設定で測定しています。`z-ai/glm-5.2` は、
同梱のプロバイダーで再測定しても同じ 14/14 でした。数値は 9 月 10 日に
現在の比較ツールで再計算しました。`qwen3.8-flash` と
`qwen3.7-flash` は初回公開時よりそれぞれ 1 言語増え、ほかは変わっていません。

`--use_antigravity` の各行は、9 月 26 日に同じ記事で、
4 件の翻訳を並列実行して測定しました。午前に `gemini-3.7-flash-medium`、
午後に `gemini-3.8-flash-medium` を測定しています。英語では、どちらも引用の下にある
フランス語訳の 3 行を自ら削除し、旗を勝手に追加することもなく、
英語の引用はそのまま保たれました。代替の後処理で修正する必要はありませんでした。
`--eco`（`gemini-3.7-flash-low`）では、4 言語のみ
（en、ja、ar、hi）を測定し、4 言語中 4 言語を書き込み、すべて差異なし、
中央値は 1 分 52 秒でした。同日、より新しい 9 月 25 日の動向記事
（438 行、英語の引用 2 件）を使って追加検証し、
`gemini-3.7-flash-medium` でブログ外に翻訳しました。14 言語中 14 言語を書き込み、
すべて差異なし、所要時間は 1 言語あたり 87～128 秒でした。

`--use_claude_code` の各行は、9 月 26 日に同じ記事で、
4 件の翻訳を並列実行し、推論の強度を `low` にして測定しました。
`sonnet` では、14 言語すべてで英語の引用がそのまま保たれ、
英語ではモデルがフランス語訳の行を自ら削除し、旗を勝手に追加することもありませんでした。
`opus` は、どの言語も書き込めませんでした。いずれも、結合部位に対して
生成された 279 種の分子に関する短い記事が原因で、
最後のセグメントで安全措置が応答を停止しました。この短い記事を単独で送っても、
「生物」カテゴリーとして拒否されます。`sonnet` はすべての言語に翻訳しました。
`haiku` は 14 言語を書き込みましたが、3 言語（en、pl、ro）で
セクション見出しがレベル 2 からレベル 1 に変わりました。推論を止めることができず、
出力トークンの 61 % を推論に使うため、`sonnet` の 2 倍以上の時間がかかりました。

`claude-sonnet-5-5`、`claude-haiku-5-5`、`claude-haiku-4-5` の各行は、
10 月 18 日に Anthropic API を使い、同じ記事で、
モデルごとに 4 件の翻訳を並列実行して測定しました。Sonnet 5.5 は
推論の無効化を受け付けません。aipmt は受け付けられる最小の設定を送信し、
応答には推論が一切含まれていません。セグメントの再処理なしで、
14 言語すべてを差異なく書き込みました。英語ではフランス語訳の行を自ら削除し、
旗を勝手に追加することもなく、英語の引用はすべての言語でそのまま保たれました。
Haiku 5.5 は適応型推論を使って測定しました。推論を無効にすると、
段落全体がフランス語のまま残り、検査で拒否されたためです。
その場合、書き込めたのは 14 言語中 3 言語でした。2 つの Haiku は同じ短い記事で問題を起こしました。
Haiku 5.5 は日本語、韓国語、中国語で見出しのレベルを変えるか重複させ、
Haiku 4.5 は 7 言語でレベル 1 に変え、日本語ではフランス語のまま残しました。
2 つの文書を 14 言語に翻訳する費用は、Haiku 4.5 が 3,67 $、
Haiku 5.5 が 0,57 $、Sonnet 5.5 が 9,21 $ でした。
### このプロジェクトのREADME、標準Markdown

2026年9月9日に固定した改訂版：785行、インラインコード285個、ブロックの
閉じ区切り40個、表89行。4件の翻訳を並列実行。

| モデル                                          | 作成済み | 差異なし | 言語ごとの中央値 | 相違点                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | なし                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | なし                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | 比較ツール上はなし；内部リンクが二重化（en）                   |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | なし                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | なし                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | 太字の単語1個（ja）                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | 太字の単語1個（ko）                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | 表の1行が直前の行と結合（ar）                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | リンク1個（sv）、太字の単語1個（zh）                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | 太字の単語1個（ar, ja）                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | 太字の単語1個（hi, ja, ko）                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | アラビア語でインラインコード40個が追加；太字（hi, ja, ko）                   |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2言語が拒否された（ar, hi）：返却結果でインラインコードが欠落        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | 1節が欠落（ar, hi, ko）；コードブロックが追加（ja, ko, ro, zh） |

途中で中断した2回の測定は評価に含めていません。Grokは12言語の後にCLIセッションが
期限切れとなり（うち11言語は差異なし）、`qwen3.8-flash`は2言語の後に
ホスティング事業者からHTTP 429が返されました。`opencode/mimo-v2.5-free`と`ollama/gpt-oss-20b-32k`は
この改訂版では再測定していません。277行短い9月4日と5日の改訂版では、
それぞれ14件中9件の翻訳を作成し、差異がなかったのはそれぞれ7件と
1件でした。

`--use_antigravity`と`--use_claude_code`の行は、固定した改訂版ではなく、
1.14.0とともに公開された改訂版で9月26日に測定しました。また、
`claude-sonnet-5-5`、`claude-haiku-5-5`、`claude-haiku-4-5`の行は10月18日に
同じ改訂版で測定しました。600行、インラインコード257個、ブロックの閉じ区切り30個、
表85行です。
185行短いため、他の行とは項目ごとに直接比較できませんが、
これらの行同士は比較できます。比較ツールが検査しない内部リンクについては、
`gemini-3.8-flash-medium`は14言語すべてでそのまま保持し、
`gemini-3.7-flash-medium`はイタリア語でリンクを壊しました。
`sonnet`と`opus`はすべてでそのまま保持し、`haiku`は
英語で二重化しました。`claude-sonnet-5-5`と`claude-haiku-4-5`は
14言語すべてでそのまま保持し、`claude-haiku-5-5`は作成した12言語すべてで保持しました。

### 著名なプロジェクト4件のREADME

FastAPI、Ollama、tldr-pages、Vue.jsをGitHubからそのまま取得しました。
これらは前の2つよりも容易な文書です。この測定は苦戦していたモデルを
対象とし、Geminiを比較の基準としています。

| モデル                    | 対象範囲                  | 作成済み | 差異なし   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4プロジェクト × 14言語     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4プロジェクト × 14言語     | 55/56   | ❌ 47/56     |
| `grok-4.6`（サブスクリプション）   | 4プロジェクト × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4プロジェクト × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### これらの測定に当てはまらないこと

- **網羅的なランキングではありません**：OpenRouterだけでも400を超える
  モデルが提供されていますが、測定したのは約15モデルです。
- **所要時間は目安です**：測定ごとに3〜6件の翻訳を並列実行しており、
  プロバイダーの処理速度も時間帯によって変動します。
- **特定時点の観測結果です**：モデルは同じ名前のまま変わることがあり、
  皆さんの文書は私たちの文書とは異なります。

ご自身の文書で再測定するには、ファイルの内容を固定したコピーで実行してください。

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

この2行は両方必要です。`pip install -e .`がないと、`python -m aipmt`は
`No module named aipmt`と応答します。

品質管理ツールは任意ですが、使用を推奨します。

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

リポジトリ内の28件の翻訳（READMEとCHANGELOG、14言語）は
`./regen_translations.sh --force`で再生成できます。既定ではChatGPTのサブスクリプションで
Codexと`gpt-6.1-sol`を使用し、4件を並列実行します。`REGEN_PROVIDER`と
`REGEN_MODEL`は実行経路を変更します。`antigravity`は引き続きサブスクリプションを
使用しますが、Googleのものになり、例外指定なしで実行できます。従量課金のAPI（`openai`、`gemini`、
`grok`、`openrouter`）は`REGEN_ALLOW_PAID_API=1`がないと拒否されます。
`REGEN_JOB_TIMEOUT`は各ジョブの上限時間を設定します（600 s、Codexと
Antigravityでは1 800 s）。ツールの詳細は`CLAUDE.md`にあります。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** — 15言語で公開している個人ブログ。
  [毎日のAI動向情報](https://jls42.org/fr/news)は、このツールで毎日翻訳しており、
  上記の測定の基準文書として使用しています。

## 著者

Julien LE SAUX
メール：contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE バージョン3。[ライセンス](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)をご覧ください。

## 注意事項

このプログラムは、GPL v3の第15条および第16条の規定に従い、
**一切の保証なし**で配布されます。「現状のまま」提供され、商品性および
特定目的への適合性について保証せず、使用によって生じた損害について
著者は責任を負いません。この要約よりもライセンス本文が
優先されます。

- **公開前に読み直してください。** 保護の対象はコードブロック、
  インラインコード、URL、アンカー、および`--news`モードの引用です。
  見出し、表、フロントマター、文の意味は対象外です。
- **文書は選択したプロバイダーに送信され**、その利用規約と
  データポリシーが適用されます。一部の無料モデルは、やり取りを
  学習に再利用することがあります。また、Antigravityの規約では、有料
  サブスクリプションも含め、Googleによる再利用や人による確認が認められています。
  データを一切端末の外に出さない唯一の方法は、ローカルモデルを使用することです。
- **API呼び出しの料金は利用者に請求されます。** このプログラムには
  支出の上限設定がありません。長い文書、失敗後の再試行、推論を多く行う
  モデルの使用では、費用が増えます。
- **公開している測定値は特定時点の観測結果であり**、保証ではありません。

記載されている製品名および会社名は、それぞれの権利者に帰属します。
このプロジェクトは、それらのいずれとも提携していません。

**gpt-6.1-solでフランス語から日本語に翻訳された記事。**
