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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="コードの臭い"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="重複行 (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="技術的負債"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="コード行数"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacyバッジ"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Markdownファイルを、コードブロック、インラインコード、URL、アンカー、
表、フロントマターの構造を保ちながら、ある言語から別の言語へ翻訳します。
モデルの呼び出し方法は11通り。5つのAPI、従量課金なしの4つのサブスクリプション、
2つのルーターに対応し、各モデルが実際に何を保持できるかを測定して公開しています。

## 概要

- **11通りのプロバイダー経路**：OpenAI、Mistral、Claude、Gemini、GrokのAPI；
  従量課金なしのChatGPT（Codex）、Grok、Google（Antigravity）、Claude（Claude
  Code）のサブスクリプション；OpenCode（オープンソース、無料またはローカル）とOpenRouter
  （400以上のモデル）のルーター。
- **トークンの欠落による破損を防止**：コードブロック、インラインコード、
  URL、アンカー、引用は、呼び出し前にトークンへ置き換え、
  応答後に検証します。1つでも欠けていれば、ファイルは書き込みません。
- **長い文書に対応**：モデルのコンテキストウィンドウに応じて分割します。
- **`--news`モード**：情報収集記事向けに、英語の引用を保護し、
  言語ごとにフラグを管理します。
- **`--eco`モード**：高速で低コストのモデルを使用します。
- **翻訳注記**を任意で冒頭、末尾、または両方に追加できます。

## インストール

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10以降が必要です。リポジトリからインストールする場合は、
[貢献方法](#貢献)を参照してください。

## 設定

キーは、優先度の高い順に3か所から読み込みます。それぞれ、
それ以前の場所で設定されていない値だけを補います。

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
`XDG_CONFIG_HOME`（絶対パスのみ）に従い、Windowsでは`%APPDATA%`に従います。
キーがない場合、コマンドはこの3か所を列挙します。

**プロジェクトの`.env`では、呼び出し先の変更も、実行するプログラムの選択も
できません。** 提供するのはキーだけで、接続先や実行ファイルは指定できません。
`_BASE_URL`、`_API_BASE`、`_ENDPOINT`、`_BIN`に該当する変数（`CODEX_BIN`、
`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`）、`GROK_HOME`、プロキシ（`HTTP_PROXY`、
`HTTPS_PROXY`、`ALL_PROXY`）、証明書ストア（`SSL_CERT_FILE`、
`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）、`XDG_CONFIG_HOME` /
`APPDATA`は、このファイルでは警告とともに無視されます。クローンしたリポジトリが
キーを別の場所へ送信したり、最初の翻訳時に独自のプログラムを実行させたりできてはいけません。
このファイルは変数展開なしで読み込まれます。
`NOM=${OPENAI_API_KEY}`でキーがコピーされることはありません。これらの変数は、
環境変数または`~/.config/aipmt/.env`に設定してください。

任意の変数：`XAI_BASE_URL`（既定値`https://api.x.ai/v1`）、
`CLAUDE_TIMEOUT`（呼び出しごとの秒数、既定値900）、`CODEX_BIN`、`CODEX_TIMEOUT`
（既定値600）、`GROK_BIN`、`GROK_HOME`（既定値`~/.grok`）、`GROK_TIMEOUT`
（既定値900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（既定値900）、
`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（既定値600）、`OPENROUTER_BASE_URL`
（`https://`が必須）、`OPENROUTER_TIMEOUT`（既定値900）、
`OPENROUTER_PREFLIGHT_TIMEOUT`（既定値30）。各変数の詳細は、
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

`document.md`をスペイン語に翻訳すると、`--target_dir`内に`document-es.md`が生成されます。
`--include_model`を指定すると、`document-es-gpt-5.6-terra.md`になります。拡張子は
常に`.md`になります。たとえば`article.mdx`は`article-en.md`になりますが、
`--keep_filename`を指定した場合は元のファイル名を保持します。既存の翻訳は、
`--force`を指定しない限りスキップします。

終了コード：すべて成功またはスキップされた場合は`0`、失敗したファイルが残っている場合は
`1`（標準エラー出力に一覧を表示）、設定に問題がある場合は`2`です。
失敗したファイルは書き込みません。書き込み自体が失敗した場合も同様です。
内容は別ファイルに書き込んでから名前を変更します。再実行するだけで対応できます。

## どのモデルを選ぶか

実際の文書2つを、各モデルで同じ14言語へ翻訳して測定しました。
**数値は、14言語のうち、翻訳ファイルが書き込まれ、
原文との差異がなかった言語の数です。**

| モデル                | 利用方法                 | 情報密度の高い情報収集記事 | このREADME    | 差異の内容と該当する言語数                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Googleサブスクリプション（Antigravity）   | ✅ 14/14                | ✅ 14/14     | 両方の文書で差異なし                                                                                                                                 |
| **Claude Sonnet 5.5** | Anthropic APIキー                 | ✅ 14/14                | ✅ 14/14     | 両方の文書で差異なし                                                                                                                                 |
| **Gemini 3.7 Flash**  | Google APIキー                    | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語：太字の単語が1つ増加（ja）                                                                                                                      |
| **Gemini 3.7 Flash**  | Googleサブスクリプション（Antigravity）   | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語：太字の単語が1つ減少（ko）                                                                                                                     |
| **GPT-5.6 Sol**       | ChatGPTサブスクリプション、またはOpenAIキー | ✅ 14/14                | ⚠️ 12/14     | 14言語中2言語：太字の単語が1つ減少（ar, ja）                                                                                                                |
| **GLM-5.2**           | OpenRouterキー                    | ✅ 14/14                | ⚠️ 11/14     | 14言語中3言語：太字の単語が1つ減少（hi, ja, ko）                                                                                                            |
| Claude Sonnet 5       | Claudeサブスクリプション（Claude Code）   | ⚠️ 13/14                | ⚠️ 13/14     | 記事では14言語中1言語：太字の単語が1つ増加（zh）；このREADMEでは1言語：表の行が前の行に連結され、表示されなくなった（ar）            |
| Claude Haiku 4.5      | Claudeサブスクリプション（Claude Code）   | ⚠️ 11/14                | ✅ 14/14     | 記事では3言語：節の見出しがレベル1に変更（en, pl, ro）；このREADMEでは比較ツール上の差異はないが、内部リンクが英語でも重複して追加された |
| Claude Sonnet 5       | Anthropic APIキー                 | ⚠️ 11/14                | ⚠️ 12/14     | 記事では3言語：コードブロックが出現（es, de, hi）；このREADMEでは2言語：リンクのマークアップが欠落（sv）、単語が太字化（zh）                              |
| Claude Haiku 4.5      | Anthropic APIキー                 | ⚠️ 7/14                 | ✅ 14/14     | 記事では7言語：節の見出しがレベル1に変更され、日本語ではフランス語のまま残った；このREADMEでは差異なし                                              |
| Claude Haiku 5.5      | Anthropic APIキー                 | ⚠️ 11/14                | ❌ 12/14     | 記事では3言語：節の見出しのレベルが変更、または見出しが重複（ja, ko, zh）；このREADMEでは2言語でインラインコードが欠落し、出力を拒否（ar, hi）    |
| Qwen 3.7 Flash        | OpenRouterキー                    | ❌ 8/14                 | ⚠️ 10/14     | 記事では1言語で出力を拒否し、ほかの5言語で差異あり；このREADMEでは約40語が`code`化（ar）                                                    |
| Grok 4.6              | Grokサブスクリプション                   | ❌ 8/14                 | 未評価     | インラインコードとURLが返されず、14言語中5言語で出力を拒否；オランダ語では全体に差異あり                                                               |
| GPT-OSS 20B           | ローカルモデル（Ollama）             | ❌ 7/14                 | 未再測定 | 14言語中4言語で出力を拒否：フランス語の文章が残っていたため、保護機能が出力を停止                                                                  |
| MiMo v2.5（無料）   | OpenCode Zen、アカウント不要         | ❌ 11/14                | 未再測定 | 1言語で出力を拒否；ポーランド語で節が1つ欠落                                                                                                                  |
| Mistral Large         | Mistral APIキー                   | ❌ 5/14                 | ❌ 1/14      | **節全体が消失**：記事で1言語（hi）、このREADMEで3言語（ar, hi, ko）。さらに記事で3言語の出力を拒否                                |
| DeepSeek V4 Flash     | OpenRouterキー                    | ❌ 3/14                 | 未再測定 | 14言語中10言語で出力を拒否；1言語あたり37分                                                                                                                 |
| Claude Opus 5.5       | Claudeサブスクリプション（Claude Code）   | ❌ 0/14                 | ✅ 14/14     | 生物学の短い記事が原因で、Opusの保護機能が全14言語で記事の翻訳を拒否；このREADMEでは差異なし                                               |

|     | 記号の意味                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 全14言語の翻訳に成功し、原文との差異なし                                                                                                                                       |
| ⚠️  | 全14言語の翻訳に成功；差異は**マークアップ**のみ。単語の太字化、`code`、リンクの角括弧の欠落など。本文、URL、コードブロック、節の欠落はない |
| ❌  | 少なくとも1言語で翻訳できず、ファイルの出力が拒否されて書き込まれなかった、**または**書き込まれたファイルで内容が欠落                                                                      |

ここから分かること：

- **出力を拒否された翻訳は、破損した翻訳ではありません。** 応答にトークンが
  欠けている場合、ファイルは書き込まれず、その言語は
  拒否として数えます。記事でのGrokがこれに該当します。非ラテン文字を使う5言語で、
  最初の分割部分からインラインコード4つとURL3つが欠落しました。
- **モデルは、たった1文を理由に文書全体の翻訳を拒否することがあります。** Opus 5.5は
  このREADMEを差異なく翻訳しますが、情報収集記事は翻訳できません。
  生物学の短い記事で保護機能が応答を停止するためです。ファイルは
  書き込まれず、aipmtが理由を表示します。
- **この保護機能は、見出し、表、フロントマター、
  本文を対象としていません。** モデルが節を削除しても、ツールはそのファイルを
  問題なく書き込んでしまいます。Mistralがこれに該当します。これらの要素は
  トークンに置き換えられず、現在の保護機能では検査していません。
  `scripts/compare_structure.py`は節の欠落を検出しますが、事後の検出です。
- **このREADMEでのGrokは未評価です**：12言語の処理後にCLIセッションが期限切れとなり、
  そのうち11言語には差異がありませんでした。途中で中断された測定には評価を付けません。
- **言語よりも文書の情報密度が重要です。** Grokは一般的な
  READMEには対応できますが、リンクが多い記事では、オランダ語でも
  うまく処理できなくなります。

測定日と文書：「このREADME」列は、2026年9月9日に
このファイルの固定版（785行、インラインコード285個、表89行）で測定しました。
その後、ファイルには修正が加わっています。ただし、AntigravityとClaude Codeの行は、
9月26日に1.14.0とともに公開された、より短い版
（600行、インラインコード257個、表85行）で測定しました。また、API経由のClaude
Sonnet 5.5、Haiku 5.5、Haiku 4.5の行は、10月18日に
同じ版で測定しました。「情報密度の高い情報収集記事」列は、
9月4日と5日に589行の記事で行った測定に基づきます。ただし、Grokの行は
9月9日に同じ情報収集記事の別の版で再測定し、Antigravityと
Claude Codeの行は9月26日に同じ記事で測定しました。前述のClaudeの3行は
10月18日に測定しました。完全な表、所要時間、測定手順は
[詳細な測定結果](#詳細な測定結果)に記載しています。
## すべてのオプション

| オプション                   | 説明                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 翻訳する単一の Markdown ファイル（`--source_dir` の代替）                                             |
| `--source_dir`           | Markdown ファイルを含むソースディレクトリ（既定値: `content/posts`）                                   |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ（既定値: `traductions_en`）                                    |
| `--source_lang`          | 翻訳元の言語（既定値: `fr`）                                                                                  |
| `--target_lang`          | 翻訳先の言語（既定値: `en`）                                                                                   |
| `--model`                | 使用するモデルを指定                                                                                  |
| `--eco`                  | 低コストモデルを使用                                                                              |
| `--use_mistral`          | Mistral AI API を使用                                                                                     |
| `--use_claude`           | Claude API を使用                                                                                         |
| `--use_gemini`           | Gemini API を使用                                                                                         |
| `--use_grok`             | xAI（Grok）API を使用 — `XAI_API_KEY` が必要                                                           |
| `--use_codex`            | ChatGPT サブスクリプションの利用枠で Codex CLI を使用                                                    |
| `--use_grok_cli`         | Grok サブスクリプションの利用枠で Grok CLI を使用                                                        |
| `--use_antigravity`      | Google AI Pro または Ultra サブスクリプションの利用枠で Antigravity CLI（`agy`）を使用                       |
| `--use_claude_code`      | Claude Pro または Max サブスクリプションの利用枠で Claude Code CLI（`claude -p`）を使用                      |
| `--use_opencode`         | OpenCode（オープンソース）で設定済みのプロバイダーに接続して OpenCode を使用。`--model provider/modèle` が必要 |
| `--use_openrouter`       | OpenRouter を使用 — `OPENROUTER_API_KEY` と `--model fournisseur/modèle` が必要                          |
| `--force`                | 再翻訳を強制                                                                                       |
| `--keep_filename`        | 元のファイル名を保持                                                                          |
| `--news`                 | ニュースモード：英語の引用を保護し、言語ごとのフラグを管理                                      |
| `--add_translation_note` | 翻訳注記を追加                                                                                |
| `--note_position`        | 注記の位置：`top`、`bottom`（既定値）、または `both`                                                     |
| `--note_format`          | 注記の形式：`legacy`（既定値、太字の段落）または `marker`                                            |
| `--include_model`        | 出力ファイルにモデル名を含める                                                            |
| `--reasoning_effort`     | GPT-5.x の推論の強度：`none`/`low`/`medium`/`high`/`xhigh`                                         |

9 個の `--use_*` フラグは相互排他的です。2 個を組み合わせると
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

`--eco` は各プロバイダーの低コストモデルに切り替えます。

| プロバイダー    | 高品質（既定値）                                                     | 低コスト（`--eco`）      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol`（`--model` により `gpt-5.6-sol`、`terra`、`luna` も使用可能） | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                                           | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`、推論の強度 `low`                                               | 同左 — `--eco` は無効 |
| OpenCode    | `--model provider/modèle` が必須                                | 同左 — `--eco` は無効 |
| OpenRouter  | `--model fournisseur/modèle` が必須                             | 同左 — `--eco` は無効 |

### ChatGPT サブスクリプション経由：`--use_codex`

公式の Codex CLI を操作します。翻訳は ChatGPT サブスクリプションの
利用枠から差し引かれ、API キーや従量課金は不要です。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 実行ファイルは `CODEX_BIN`、次に `PATH`、最後にパッケージ
  `openai-codex-cli-bin` の順で検索されます。`~/.codex/auth.json` は一切読み込まれません。
- `OPENAI_API_KEY` と `CODEX_API_KEY` は子プロセスの環境から
  除去されます。キーが存在しても API に切り替わることはありません。
- 各セグメントは 5 時間の利用枠の「メッセージ」を最低 1 件消費します。検証に
  失敗して再試行される場合は 2 件です。OpenAI の推定では、
  Plus プランの場合、`gpt-5.6-luna`（`--eco`）は 5 時間あたり 250-2 000 件、
  `gpt-5.6-sol` は 10-100 件です。
- 1.16.3 までの既定値だった `--model gpt-5.6-sol`、`--model gpt-5.6-terra`、
  `--model gpt-5.6-luna` もサブスクリプション経由で利用できます。
- サーバーが 429 を返してもファイルは失われません。Codex は自動で再接続し、
  aipmt はターンの終了を待ちます。最後まで 429 が解消しなければ、セグメントは
  30 秒後、次に 60 秒後に再試行されます。アカウントに利用権限のないモデルは、
  「ChatGPT アカウントで Codex を使用する場合、このモデルはサポートされていません」という 400 エラーを返します。
- API より遅く、文書が長くなるほど差が広がります。この README では、
  `gpt-5.6-sol` で言語あたりの中央値が 6 分 46 秒だったのに対し、
  `gemini-3.7-flash` では 36 秒でした。
- CI では拒否されます（`CI` または `GITHUB_ACTIONS` が設定されている場合）。サブスクリプションの認証には
  個人用のセッションファイルを使用するため、共有ランナーに
  置くべきではありません。
- 変数：`CODEX_BIN`、`CODEX_TIMEOUT`（セグメントあたりの秒数、既定値 600）。

### Grok サブスクリプション経由：`--use_grok_cli`

公式の Grok Build CLI でも同じ仕組みを使用し、SuperGrok または
X Premium+ サブスクリプションを利用します。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Codex より隔離が弱くなります。** Grok の OS サンドボックスは、
  最近の多くの Linux 環境では適用されません（AppArmor、コンテナ実行環境の
  ソケット）。適用できないプロファイルを指定すると、通知なしで隔離されずに
  起動します。そのため、このスクリプトは既定ではプロファイルを要求せず、その旨を表示し、
  CLI の `--deny` ルールと、すべてに一致する `*` に依存します。これは、
  保護を黙って解除する代わりに起動を拒否する唯一の
  層です。`GROK_TRANSLATE_SANDBOX=read-only` は OS サンドボックスを必須とし、
  環境が対応できなければ起動に失敗します。
- 利用枠は週単位で、Chat、Imagine、Voice と共有されます。また、
  残量を確認するコマンドはありません。バッチ処理によって、通知なしに会話用の
  利用枠が消費される可能性があります。
- 変数：`GROK_BIN`、`GROK_HOME`（CLI のディレクトリ、既定値 `~/.grok`）、
  `GROK_TIMEOUT`（既定値 900）、`GROK_TRANSLATE_SANDBOX`。

### Google サブスクリプション経由：`--use_antigravity`

Antigravity の公式 CLI である `agy` でも同じ仕組みを使用します。Google
AI Pro または Ultra の契約者は、トークン単位の課金ではなく、
サブスクリプションの利用枠から翻訳分が差し引かれます。この利用枠を使える経路はこれだけです。Gemini CLI は
2026 年 6 月 18 日以降、これらのアカウントへの対応を終了しています
（[発表](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)）。
また、Antigravity SDK が受け付けるのは API キーか Google Cloud プロジェクトのみです。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **有料課金につながる経路はすべて遮断されます。** agy に渡される環境変数は、
  `PATH`、言語とタイムゾーン、
  端末、ユーザー情報、プロキシと証明書、セッションバスという限定リストに含まれるものだけで、キーは一切渡されません。
  agy の変数には、呼び出し先を通知なしで切り替えるものが複数あるためです。実測では、
  文書を第三者のゲートウェイへ送る変数や、課金対象の
  Google Cloud プロジェクトへ送る変数があり、拒否リスト方式では見直しのたびに漏れが見つかりました。
  各セグメントの処理前に、利用枠を消費しない `agy -p /config` で、
  有料 AI クレジットが無効であり、API キーも Google Cloud プロジェクトもないことを
  確認する必要があります。設定が存在しない場合も拒否され、条件を満たさなければ何も翻訳されません。さらに、各
  呼び出しのログでサブスクリプションの使用（`authMethod=consumer`）を確認できなければ、
  応答は拒否されます。
- **隔離。** 各呼び出しは、非公開の使い捨てホームディレクトリ内で、
  ツールを持たない翻訳エージェントを使用して実行されます。agy の設定、ルール、
  プラグイン、MCP サーバー、フックは引き継がれず、履歴にも何も追加されません。
  ログイン情報はキーリング内に保持され、aipmt が読み込むことはありません。
  エージェントが見つからない場合、agy は通知なしでコーディング用エージェントと
  そのツールに切り替わります。そのため、ログの完全な 1 行で正しいエージェントの使用を確認する必要があり、
  文書中に同じメッセージが引用されていても代わりにはなりません。確認できなければ拒否されます。
- **対応プラットフォーム**：キーリングがあるセッション内の Linux（D-Bus セッションバス、
  Secret Service）。macOS も受け付けますが、実測はしていません。
  Windows では呼び出しを隔離するための変数を agy が読み込まないため拒否されます。
  セッションバスのない Linux（SSH セッション、コンテナ、サーバー）も拒否されます。こうした環境では agy が
  トークンを `~/.gemini` 内のファイルに保存しますが、隔離によってそのファイルが見えなくなるためです。
  ログインコードを 1 分間待つことなく、起動前に理由を示して
  拒否します。
- **モデル**：`agy models` にあるものを使用します。Gemini はモデル名に推論の強度を含みます
  （`gemini-3.8-flash-medium` など）。接尾辞のない名前は呼び出し前に拒否され、
  `--reasoning_effort` は無効です。既定値は `gemini-3.8-flash-medium`、
  `--eco` では `gemini-3.7-flash-low` です。これらの選定に用いた測定は
  [詳細な測定結果](#詳細な測定結果)に記載されています。Claude と GPT-OSS
  には独自の利用枠があり、はるかに小さくなっています。実測では 1 回の呼び出しにつき
  5 時間の利用枠の約 1 % を消費し、Flash では 0.05 % でした。
- **利用枠**：グループごとに 5 時間単位と週単位の枠があり、
  トークンのコストに比例して消費されます。著者のアカウントで測定したところ、
  ソース 100 万文字あたりの 5 時間枠の消費量は、
  `gemini-3.8-flash-medium` で約 16 ポイント、`gemini-3.7-flash-medium` で 14 ポイント、
  推論の強度が低い場合は 7～8 ポイントでした。したがって、40 000 文字の README は
  半ポイントを少し超える程度を消費します。一方、週単位の上限はプランによって異なります。再試行は
  agy が再試行可能と判断した場合に行われます。それ以外の場合、使い切った利用枠に対して
  再試行は行いません。`/usage` に表示されるリセット時刻まで、
  各ファイルの処理が失敗します。
- **API より低速**：測定に使用した情報量の多い記事では、言語あたりの
  中央値は `gemini-3.8-flash-medium` で 3 分 59 秒、
  `gemini-3.7-flash-medium` で 3 分 14 秒でした。これに対し、API 経由の Gemini 3.7 Flash では 1 分 18 秒でした。
- **中断**：Ctrl-C または端末を閉じる操作によって、コマンドとともに agy も停止し、
  利用枠を消費しながらターンを最後まで実行し続けることを防ぎます。
  Codex、Grok CLI、OpenCode も同様です。`nohup` では翻訳が続行されます。
- CI では拒否されます（`CI` または `GITHUB_ACTIONS` が設定されている場合）。ログイン情報は
  個人用のキーリング内にあります。ランナーでは `--use_gemini` と `GOOGLE_API_KEY` を使用してください。
- 変数：`AGY_BIN`（なければ `PATH`、次に `~/.local/bin/agy`）、
  `AGY_TIMEOUT`（起動時間を含むセグメントあたりの秒数、既定値 900）。

**利用規約：責任を負うのはご自身のアカウントです。**
[Antigravity の利用規約](https://antigravity.google/terms)（第 6 条）と
[よくある質問](https://antigravity.google/docs/faq/)では、Antigravity のログイン情報を使い、
第三者のソフトウェアからサービスにアクセスすることを禁止しています。Claude Code、
OpenClaw、OpenCode が例として挙げられており、違反するとアカウントが停止される可能性があります。aipmt は
トークンを読み込んだり再利用したりせず、Google が
スクリプトや CI 向けに説明している[ヘッドレスモード](https://antigravity.google/docs/cli/headless/)で
公式の実行ファイルを起動します。Google の担当者は、自分の作業のためにローカルスクリプトから
`agy -p` を起動することを「標準的」と評しています
（[公式フォーラム、2026 年 9 月 25 日、契約上の保証ではない回答](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）。
ただし、このように配布されるツールの扱いを明確に定めた文書はありません。

**公開文書のみを使用してください。** 同じ利用規約の第 5 条によると、
やり取り（プロンプト、応答、メタデータ）は Google の製品や
機械学習の改善に使用されたり、人間が確認したりする場合があります。
有料サブスクリプションでも同様です。除外するには
`enableTelemetry` の設定を使用しますが、効果は文書化されておらず、aipmt はこの設定を行いません。
agy の設定は隔離環境に引き継がれません。機密情報は一切渡さないでください。
### Claude のサブスクリプションで：`--use_claude_code`

Claude Code の公式 CLI である `claude` を `-p` モードで使う場合も同じ原則です。
Claude Pro または Max の利用者は、翻訳がトークン単位で課金される代わりに、
サブスクリプションの利用枠から差し引かれます。
従量課金の Anthropic API である `--use_claude` と混同しないでください。

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **従量課金につながる経路をすべて閉じ、呼び出しのたびにそれを確認します。** Claude
  Code に渡される環境変数は、あらかじめ限定されたものだけです。
  API キー、トークン、クラウドプロバイダーの情報、aipmt の起動元となった Claude Code
  セッションの識別情報はいずれも渡しません。最初のセグメントを処理する前に、`claude auth status` で
  Console キーを使わずにサブスクリプションで接続していることを表示し、利用枠を消費しない
  `/usage` でも確認する必要があります。各呼び出しも初期化イベントで同じことを
  証明し、確認できなければ応答を拒否します。
- **「追加使用」を無効にしてください**（claude.ai、設定 → 使用状況）。
  これで費用をゼロユーロに保てます。有効にすると、時間枠の利用枠を使い切った際に
  自動で切り替わり、エラーを表示せずに課金されます。aipmt は呼び出しの利用枠レポートに
  それが示されると翻訳を停止しますが、その呼び出し自体はすでに計上されています。
- **利用枠は Claude Code の各セッションと共有されます。** 各呼び出しは
  5 時間枠と週間枠の使用状況を報告します。80 % を超えると
  （`AIPMT_CLAUDE_MAX_UTILIZATION`）、作業に必要な利用枠を使い切らないよう、
  新たなセグメントの処理を開始しません。
- **隔離。** 各呼び出しはツールを使わず、専用の使い捨てディレクトリ内で、
  カスタマイズを無効にしたモードで実行されます。`CLAUDE.md`、プラグイン、
  フック、MCP サーバー、設定はいずれも読み込まれず、セッションの情報も保持されません。
  添付ファイルも無効です。文書内の `@chemin` は
  テキストのままで、ファイルを開くことはありません（実測済み）。
- **モデル**：既定は `sonnet`、推論の労力は `low` で、`--eco` でも同じです。
  この経路では `--eco` を指定しても変わりません。同じ文書で測定したところ、`haiku` は
  速度が半分でした。推論を止められないためで、費用はわずかに低いだけです。
  また、`opus` は生物学関連の内容を拒否します（次項）。
  どちらも `--model` で利用できます。これらのエイリアスは、各系列の
  最新モデルを指します。`fable` と `[1m]` の各派生モデルは、
  有料クレジットを消費するため拒否されます。`--reasoning_effort` は推論の労力を設定しますが、
  翻訳では効果がありません。実測された推論量はゼロか、ほぼゼロです。
- **Opus は一部の生物学関連の内容を拒否します。** 安全対策が
  Sonnet より厳しく、Anthropic のエラーメッセージでも
  「生物学研究に近い作業が検出対象になることがある」と警告しています。
  実測では、生成された 279 分子に関する短いニュース記事が原因で、記事全体が
  14 言語すべてで拒否されました。ファイルは一切書き込まれません。aipmt は途中で切れた
  応答を拒否し、安全対策が原因であることを示して `--model sonnet` を勧めます。
- CI（`CI` または `GITHUB_ACTIONS` が設定されている場合）と Windows（未測定）では拒否されます。
- 変数：`AIPMT_CLAUDE_BIN`（未指定なら `PATH`、次に `~/.local/bin/claude`）、
  `AIPMT_CLAUDE_TIMEOUT`（セグメントごとの秒数、既定値 900）、
  `AIPMT_CLAUDE_MAX_UTILIZATION`（既定値 0.8）、`CLAUDE_CONFIG_DIR`（Claude Code の
  アカウント。プロジェクトの `.env` からは取得しません）。作業ディレクトリは
  `XDG_CACHE_HOME/aipmt/claude-code` の下に作成されます（既定値 `~/.cache`）。

**利用規約：責任を負うのはご自身のアカウントです。**
[Claude Code の法的事項のページ](https://code.claude.com/docs/en/legal-and-compliance)は、
「エンドユーザーが、自分の Claude サブスクリプションを使い、改変されていない
Claude Code のバイナリにサインインすること」を妨げていません。
aipmt が行うのはまさにこれで、公式バイナリを起動し、トークンを読むことはありません。
ただし Anthropic は、「サードパーティーの開発者が、ユーザーに代わって
Free、Pro、Max プランの認証情報を通じてリクエストを中継すること」を認めず、
「オープンソースのプロジェクトを含む」サードパーティー製ツールには API キーの利用を推奨し、
その使用量を有料クレジットから差し引く権利を留保しています
（[Claude のヘルプ](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)）。
配布されるツールがバイナリを起動する場合について、明確な判断を示す記述はありません。

**データ**：Free、Pro、Max のアカウントでは、プライバシー設定で許可している場合、
Claude Code もモデルの学習対象になります
（[データに関するページ](https://code.claude.com/docs/en/data-usage)）。aipmt は
ローカルに会話記録を残しません（`--no-session-persistence`）。機密情報を
渡さないでください。

### 好きなプロバイダーへ：`--use_opencode`

[OpenCode](https://opencode.ai) はオープンソース（MIT）のコーディングエージェントで、
内部で設定されたプロバイダーに処理を振り分けます。API キー、サブスクリプション、
OpenCode Zen ゲートウェイ（無料モデル、アカウント不要）、ローカルモデルに対応します。
ここでは Zen と Ollama の 2 つの経路を最初から最後まで測定しました。

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

`--model` は必須です。指定しないと、OpenCode はやり取りが学習に使われる
可能性のある無料モデルに自動で切り替わります。この選択を利用者に代わって
行うことはありません。

各呼び出しでの隔離：

- 利用者の設定より優先されるインライン設定で、すべてのツールを拒否する
  （`permission: { "*": "deny" }`）エージェント `aipmt` を定義します。セッション共有は
  無効、`--pure` とし、`--auto` は使いません。
- 空の使い捨て作業ディレクトリを用意し、`OPENCODE_DISABLE_PROJECT_CONFIG` と
  `OPENCODE_DISABLE_CLAUDE_CODE` を設定します。これらがないと、OpenCode は現在のディレクトリの
  `AGENTS.md` と `~/.claude/CLAUDE.md` をプロンプトに挿入します。
  グローバルの `~/.config/opencode/AGENTS.md` は引き続き挿入されます。OpenCode では
  これを除外できません。
- 出力の条件：終了コードが 0、`error` イベントがないこと、ツール呼び出しが
  ないこと、最後のステップが `stop` であること、テキストが空でないこと、
  エージェント `aipmt` が実際に読み込まれていることです。不明な `--agent` を
  指定しても OpenCode は失敗せず、通知なしでコーディングエージェントに切り替わります。
- `aipmt` のキーは、OpenCode 自体のキーである `OPENCODE_API_KEY` を除き、
  一切渡されません。プロバイダーは OpenCode 内で設定します。
  `aipmt` の `.env` では設定しません。

留意点：

- Zen の無料モデルは入れ替わり、制限も文書化されていません。
  やり取りが学習に使われる可能性もあります。公開文書向けであり、非公開の内容には適しません。
- セグメントは最大 16 000 文字になるため、ローカルモデルには最低 16 k トークンの
  コンテキストが必要です。Ollama では 4 096 に設定されていることが多いため、
  `PARAMETER num_ctx 32768` を指定した `Modelfile` を使ってください。
- `--eco` は効果がありません。`--reasoning_effort` はそのまま
  OpenCode の `--variant` として渡されます。
- OpenCode は各セッションを `~/.local/share/opencode/` に記録します。
- 変数：`OPENCODE_BIN`（未指定なら `PATH`、次に `~/.opencode/bin/opencode`）、
  `OPENCODE_TIMEOUT`（セグメントごとの秒数、既定値 600）。`OPENCODE_CONFIG` は
  そのまま OpenCode に渡されます。

Ollama 経由でローカルモデルを使う例。`~/.config/opencode/opencode.json` 内に記述します：

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

`reasoningEffort: "none"` は、Ollama がこれらのモデルで既定で有効にする思考を無効にします。
これは Modelfile では無効にできません。6 語の文で測定したところ、
このオプションなしでは思考に 919 トークンと 68 秒を要し、指定すると 9 トークンでした。

### 400 以上のモデルへ：`--use_openrouter`

OpenRouter は、単一のクレジット残高で利用する従量課金のルーターで、
第三者がホストするモデルに接続します。ここで対応するほかのプロバイダーでは
提供されていない、中国のオープンモデルも含まれます。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` は必須です。課金が発生する前に事前検証を実行し、
ルーティングに関する 2 つの特性に対処します：

- **同じモデルが、上限の異なる数十のホスティング事業者から提供されています**。
  `z-ai/glm-5.3-flash` では 23 社あり、そのうち 1 社の出力上限は
  2 048 トークンでした。事前検証は `/api/v1/models/{modèle}/endpoints` を読み、
  出力上限が 8 000 トークン未満の事業者や稼働状況が悪化している事業者を除外し、
  残りを `allow_fallbacks: false` で固定します。
- **推論には出力と同じ料金がかかります**。`z-ai/glm-5.2` の
  「OK」という応答では、2 トークンに対して 107 トークンでした。既定では推論を
  無効にします。推論が必須のモデルには、受け付ける最も低い労力を指定します。
  カタログの既定値では、翻訳が終わる前に出力枠を使い切る可能性があるためです。
  `--reasoning_effort` の指定が常に優先されます。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- コンテキストウィンドウはカタログから取得します。16 400 トークン未満のモデルは、
  呼び出し前に拒否します。プロンプトとセグメントに 8 400、出力に最低
  8 000 トークンが必要です。
- スラッグがカタログに存在しない場合、カタログに接続できない場合、
  上限を満たすホスティング事業者がない場合は、コマンドを停止します。
- 出力が空の `finish_reason=length` は、推論で予算を使い切った状態であり、
  途中切れではありません。メッセージでこの違いを示します。
- `--eco` は効果がありません。
- 変数：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>）、
  `OPENROUTER_BASE_URL`（既定値 `https://openrouter.ai/api/v1`、`https://`
  必須）、`OPENROUTER_TIMEOUT`（既定値 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`
  （既定値 30）。

### 翻訳注記

`--add_translation_note` は、`bottom`（既定）、`top`（フロントマターの後）、
または `both`（`--note_position`）に注記を追加します。形式は `legacy`（太字の段落、
既定）または `marker`（`--note_format`）です。`marker` 形式は、
表示されない Markdown の参照定義
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`
の後に太字の引用を置きます。GitHub で読めるとともに、
ビルド時に remark プラグインで利用できます。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 詳細な測定結果

すべての測定は、`aipmt` を使って実際に実行した翻訳です。対象は
英語、スペイン語、ドイツ語、イタリア語、ポルトガル語、オランダ語、ポーランド語、スウェーデン語、ルーマニア語、日本語、韓国語、中国語、アラビア語、ヒンディー語の 14 言語です。
**書き込み済み**は検証を通過したファイル数、**差異なし**は
`scripts/compare_structure.py` が何も検出しなかったファイル数です。セクション、小見出し、リンク、
異なる URL、コードブロック、インラインコード、表の行、引用ブロック、
太字の語の数が同じであることを確認します。

「差異なし」は「何も検出されなかった」という意味で、「同一」という意味ではありません。
比較ツールは内容を読まずに要素の数を数えます。レベル 4 の見出しが削除された場合、
インラインコードの内容が置き換わった場合、国旗が入れ替わった場合、
内部リンクに余分な括弧が付いて `[texte]((#ancre))` となり、
どこにもつながらなくなった場合も検出しません。言語の判定もしません。

### 情報密度の高い動向記事、`--news` モード

[jls42.org の AI 動向](https://jls42.org/fr/news)のある号：
589 行、140 リンク、21 セクション、保護対象の英語の引用 3 件。
測定は 2026 年 9 月 4 日と 5 日に実施しました。

| モデル                                          | 利用経路              | 書き込み済み | 差異なし   | 言語ごとの中央値 |
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

Grok は 9 月 9 日、同じ動向記事の別の号（356 行）で再測定しました。
14 言語中 9 言語が書き込まれ、8 言語が差異なしでした。冒頭の表にはこの数値を
掲載しています。中断した 3 回の測定は記載していません。
`qwen3.5-27b`（9 言語）と `kimi-k2.6`（4 言語）はクレジット不足、
`z-ai/glm-5.3-flash` は 2 件の失敗が推論設定に起因しており、
現在のプロバイダーでは修正されているためです。OpenRouter の各行は、
`--use_openrouter` 導入前にルーターの既定設定で測定しました。`z-ai/glm-5.2` は、
提供されているプロバイダーで再測定しても同じ 14/14 でした。数値は
9 月 10 日に現在の比較ツールで再計算しました。`qwen3.8-flash` と
`qwen3.7-flash` は初回公開時よりそれぞれ 1 言語増え、ほかは変わっていません。

`--use_antigravity` の各行は、9 月 26 日に同じ記事で、
4 件の翻訳を並列実行して測定しました。午前に `gemini-3.7-flash-medium`、
午後に `gemini-3.8-flash-medium` を測定しました。英語では、それぞれが引用の下にある
フランス語訳の 3 行を自ら削除し、国旗を勝手に追加することもなく、
英語の引用もそのまま保持しました。予備の後処理は何もする必要がありませんでした。
`--eco`（`gemini-3.7-flash-low`）では、英語、日本語、アラビア語、ヒンディー語の
4 言語だけを測定し、4 言語中 4 言語が書き込まれ、すべて差異なし、
中央値は 1 min 52 s でした。同日、より新しい 9 月 25 日号
（438 行、英語の引用 2 件）でも検証しました。ブログの外で
`gemini-3.7-flash-medium` により翻訳し、14 言語中 14 言語が書き込まれ、
すべて差異なし、言語ごとの所要時間は 87〜128 s でした。

`--use_claude_code` の各行は、9 月 26 日に同じ記事で、
推論の労力を `low` に設定し、4 件の翻訳を並列実行して測定しました。
`sonnet` では、14 言語すべてで英語の引用がそのまま保持され、
英語ではモデル自身がフランス語訳の行を削除し、国旗を勝手に追加することもありませんでした。
`opus` はどの言語も書き込めませんでした。結合部位に向けて生成された
279 分子に関する短い記事が原因で、すべての言語で最後のセグメントの応答が
安全対策によって停止されました。この短い記事だけを送っても「生物学」カテゴリを理由に
拒否されます。`sonnet` はすべての言語に翻訳しました。`haiku` は
14 言語を書き込みましたが、3 言語（英語、ポーランド語、ルーマニア語）では、
セクション見出しがレベル 2 からレベル 1 に変わりました。推論を止めることができず、
出力トークンの 61 % を推論が占めたため、`sonnet` の 2 倍以上の時間がかかりました。

`claude-sonnet-5-5`、`claude-haiku-5-5`、`claude-haiku-4-5` の各行は、
10 月 18 日に Anthropic API を使い、同じ記事で、モデルごとに
4 件の翻訳を並列実行して測定しました。Sonnet 5.5 は思考の無効化を
受け付けません。aipmt は受け付ける最も低い設定を送り、応答には思考が
一切含まれていませんでした。14 言語を差異なしで書き込み、セグメントの再処理も
不要でした。英語ではフランス語訳の行を自ら削除し、国旗を勝手に追加することもなく、
英語の引用はすべての言語でそのまま保持されました。Haiku 5.5 は適応的な思考を
有効にして測定しています。思考を無効にすると、段落全体がフランス語のまま残り、
検証で拒否され、14 言語中 3 言語しか書き込まれませんでした。2 つの Haiku は
同じ短い記事でつまずきました。Haiku 5.5 は日本語、韓国語、中国語で
見出しのレベルを変えるか重複させ、Haiku 4.5 は 7 言語でレベル 1 に変え、
日本語ではフランス語のまま残しました。2 文書を 14 言語に翻訳した費用は、
Haiku 4.5 が 3,67 $、Haiku 5.5 が 0,57 $、Sonnet 5.5 が 9,21 $ でした。
### このプロジェクトの README、標準 Markdown

2026年9月9日に固定したリビジョン：785 行、285 個のインラインコード、40 個の
ブロック終端、89 行の表。4 件の翻訳を並列実行。

| モデル                                          | 出力済み | 差異なし | 言語ごとの中央値 | 差異の内容                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | なし                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | なし                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | 比較ツール上はなし；内部リンクの重複（en）                   |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | なし                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | なし                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | 太字の単語 1 個（ja）                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | 太字の単語 1 個（ko）                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | 表の 1 行が前の行に連結（ar）                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | リンク 1 個（sv）、太字の単語 1 個（zh）                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | 太字の単語 1 個（ar, ja）                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | 太字の単語 1 個（hi, ja, ko）                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | アラビア語でインラインコード 40 個が追加；太字（hi, ja, ko）                   |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2 言語が拒否（ar, hi）：返却時にインラインコードが欠落        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | セクション 1 個が欠落（ar, hi, ko）；コードブロックが追加（ja, ko, ro, zh） |

途中で中断された 2 回の測定は集計していません。Grok は 12 言語の後に CLI セッションが期限切れ
（うち 11 言語は差異なし）、`qwen3.8-flash` は 2 言語の後に
ホスティング事業者から HTTP 429 が返されました。`opencode/mimo-v2.5-free` と `ollama/gpt-oss-20b-32k` は
このリビジョンでは再測定していません。277 行短い 9月4日と5日のリビジョンでは、
それぞれ 14 言語中 9 言語の翻訳を出力し、そのうち差異がなかったのはそれぞれ 7 言語と
1 言語でした。

`--use_antigravity` と `--use_claude_code` の行は、
固定したリビジョンではなく、1.14.0 とともに公開されたリビジョンで 9月26日に測定しました。また、
`claude-sonnet-5-5`、`claude-haiku-5-5`、`claude-haiku-4-5` の行は 10月18日に
同じリビジョンで測定しました。600 行、257 個のインラインコード、30 個のブロック終端、85
行の表です。185 行
短いため、ほかの行とは同じ条件で比較できませんが、
これらの行同士は比較できます。比較ツールが
検査しない内部リンクについては、`gemini-3.8-flash-medium` は
14 言語すべてで維持し、`gemini-3.7-flash-medium` はイタリア語でリンクを壊しました。
`sonnet` と `opus` はすべてで維持し、`haiku` は
英語で重複させました。`claude-sonnet-5-5` と `claude-haiku-4-5` は
14 言語すべてで維持し、`claude-haiku-5-5` は出力した 12 言語すべてで維持しました。

### よく知られたプロジェクトの README 4 件

FastAPI、Ollama、tldr-pages、Vue.js を GitHub からそのまま取得しました。
前の 2 件よりも翻訳しやすい文書です。この測定は
問題のあったモデルを対象とし、Gemini を比較の基準としています。

| モデル                    | 対象範囲                  | 出力済み | 差異なし   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 プロジェクト × 14 言語     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 プロジェクト × 14 言語     | 55/56   | ❌ 47/56     |
| `grok-4.6` （サブスクリプション）   | 4 プロジェクト × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 プロジェクト × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### これらの測定の限界

- **網羅的なランキングではありません**：OpenRouter だけでも 400 を超える
  モデルが提供されていますが、測定したのは 15 程度です。
- **所要時間は目安です**：測定によって 3～6 件の翻訳を並列実行しており、
  提供事業者の処理速度も時間帯によって変動します。
- **特定時点での観測です**：モデルは同じ名前のまま変化し、皆さんの
  文書も私たちの文書とは異なります。

ご自身の文書で再測定するには、内容を固定したファイルのコピーを使って実行してください。

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

この 2 行は両方とも必要です。`pip install -e .` がないと、`python -m aipmt` は
`No module named aipmt` と応答します。

品質管理ツールは任意ですが、使用を推奨します。

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

リポジトリ内の 28 件の翻訳（README と CHANGELOG、14 言語）は、
`./regen_translations.sh --force` で再生成できます。既定では ChatGPT のサブスクリプションで Codex と `gpt-6.1-sol` を使い、
4 件を並列実行します。`REGEN_PROVIDER` と
`REGEN_MODEL` で利用経路を変更できます。`antigravity` は Google の
サブスクリプションを引き続き使用するため、例外指定なしで実行できます。従量課金の API（`openai`、`gemini`、
`grok`、`openrouter`）は `REGEN_ALLOW_PAID_API=1` がなければ拒否されます。
`REGEN_JOB_TIMEOUT` は各ジョブの実行時間に上限を設定します（600 s、Codex と
Antigravity では 1 800 s）。ツールの詳細は `CLAUDE.md` にあります。

## このスクリプトを利用しているプロジェクト

- **[jls42.org](https://jls42.org)** — 15 言語で公開されている個人ブログです。
  [日々の AI 動向レポート](https://jls42.org/fr/news)は、このツールで毎日
  翻訳され、上記の測定の基準文書として使われています。

## 著者

Julien LE SAUX
メール：contact@jls42.org

## ライセンス

GNU 一般公衆利用許諾書 第 3 版。[ライセンス](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)を参照してください。

## 注意事項

このプログラムは、GPL v3 の第 15 条および第 16 条に従い、
**一切の保証なし**で配布されます。「現状のまま」で提供され、商品性や
特定目的への適合性について保証するものではなく、使用によって生じた損害について
著者は責任を負いません。ライセンスの本文が
この要約に優先します。

- **公開前に読み直してください。** 保護対象はコードブロック、
  インラインコード、URL、アンカー、`--news` モードの引用です。
  見出し、表、フロントマター、文章の意味は保護されません。
- **文書は選択した提供事業者に送信され**、その利用規約と
  データポリシーが適用されます。一部の無料モデルでは、
  やり取りが学習に再利用されることがあります。また、Antigravity の規約では、
  有料サブスクリプションでも、Google によるやり取りの再利用と人間による確認が認められています。
  データを端末の外に一切出さない唯一の方法は、ローカルモデルを使うことです。
- **API 呼び出しの料金は利用者に請求されます。** このプログラムは
  支出に上限を設定しません。長い文書、失敗後の再試行、推論に多くの処理を費やす
  モデルでは費用が増えます。
- **公開されている測定結果は特定時点での観測であり**、保証ではありません。

記載されている製品名および企業名は、それぞれの権利者に帰属します。
このプロジェクトはいずれとも提携していません。

**gpt-6.1-solでフランス語から日本語に翻訳された記事。**
