# AI 搭載 Markdown 翻訳ツール

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="コードの不吉な臭い"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="重複行 (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="技術的負債"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="コード行数"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy バッジ"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Markdown ファイルを、コードブロック、インラインコード、URL、アンカー、
表、フロントマターの構造を保持しながら、別の言語へ翻訳します。
モデルの呼び出し方法は 11 通り。5 つの API、従量課金のない 4 つの
サブスクリプション、2 つのルーターに対応し、各モデルが実際に
何を保持するかについての測定結果も公開しています。

## 概要

- **11 通りのプロバイダー経路**：OpenAI、Mistral、Claude、Gemini、Grok の API、
  従量課金のない ChatGPT（Codex）、Grok、Google（Antigravity）、Claude（Claude
  Code）のサブスクリプション、ルーターの OpenCode（オープンソース、無料またはローカル）と OpenRouter
  （400 以上のモデル）。
- **トークンの欠落による破損を防止**：コードブロック、インラインコード、
  URL、アンカー、引用を呼び出し前にトークンへ置き換え、
  応答時に確認します。1 つでも欠けていれば、ファイルは書き込みません。
- **長い文書**：モデルのコンテキストウィンドウに応じて分割します。
- **`--news` モード**：英語の引用を保護し、言語ごとに
  フラグを管理する、動向調査記事向けのモードです。
- **`--eco` モード**：高速で低価格なモデルを使用します。
- 任意の**翻訳注記**を、冒頭、末尾、または両方に追加できます。

## インストール

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 以降が必要です。リポジトリからインストールする方法は、
[貢献方法](#貢献する)を参照してください。

## 設定

キーは次の 3 か所から、優先度の高い順に読み込みます。各設定元は、
それ以前の設定元で未設定だった項目だけを補います。

|     | 場所                                            | 用途                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 環境変数                     | CI、コンテナ、一時的な上書き |
| 2   | 現在のディレクトリ（または親ディレクトリ）の `.env` | プロジェクト固有のキー            |
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

`GOOGLE_API_KEY` の代わりに `GEMINI_API_KEY` も使用できます。ユーザー設定ファイルは
`XDG_CONFIG_HOME`（絶対パスのみ）に従い、Windows では `%APPDATA%` に従います。
キーがない場合、コマンドは 3 つの場所を列挙します。

**プロジェクトの `.env` では、呼び出し先の変更も、実行するプログラムの選択も
できません。** 提供するのはキーだけで、接続先や実行ファイルではありません。
`_BASE_URL`、`_API_BASE`、`_ENDPOINT`、`_BIN` に該当するすべての変数（`CODEX_BIN`、
`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`）、`GROK_HOME`、プロキシ（`HTTP_PROXY`、
`HTTPS_PROXY`、`ALL_PROXY`）、証明書ストア（`SSL_CERT_FILE`、
`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）、および `XDG_CONFIG_HOME` /
`APPDATA` は、このファイル内では警告付きで無視されます。クローンしたリポジトリが、
最初の翻訳時にキーを盗用したり、独自のプログラムを実行させたり
できてはならないためです。また、このファイルは変数展開なしで読み込みます。
`NOM=${OPENAI_API_KEY}` によってキーがコピーされることはありません。これらの変数は、
環境変数または `~/.config/aipmt/.env` に設定してください。

任意の変数：`XAI_BASE_URL`（既定値 `https://api.x.ai/v1`）、
`CLAUDE_TIMEOUT`（呼び出しあたりの秒数、既定値 900）、`CODEX_BIN`、`CODEX_TIMEOUT`
（既定値 600）、`GROK_BIN`、`GROK_HOME`（既定値 `~/.grok`）、`GROK_TIMEOUT`
（既定値 900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（既定値 900）、
`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（既定値 600）、`OPENROUTER_BASE_URL`
（`https://` が必要）、`OPENROUTER_TIMEOUT`（既定値 900）、
`OPENROUTER_PREFLIGHT_TIMEOUT`（既定値 30）。それぞれの詳細は、
対応するプロバイダーの節で説明しています。

## はじめに

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` をスペイン語に翻訳すると、`--target_dir` 内に `document-es.md` が生成されます。
`--include_model` を指定すると、`document-es-gpt-5.6-terra.md` になります。拡張子は
常に `.md` になります。たとえば `article.mdx` は `article-en.md` になります。ただし、
`--keep_filename` を指定すると元の名前を保持します。既存の翻訳は、
`--force` を指定しない限りスキップします。

終了コード：すべて成功またはスキップした場合は `0`、失敗したファイルが
残っている場合は `1`（標準エラー出力に一覧を表示）、設定に問題がある場合は `2` です。
失敗したファイルは、書き込み処理そのものが失敗した場合も含め、書き込まれません。
内容を同じ場所の別ファイルに書き込んでから名前を変更します。再実行するだけで対応できます。

## モデルの選び方

実際の文書 2 件を各モデルで同じ 14 言語に翻訳して測定しました。
**数値は、14 言語のうち、翻訳が書き込まれ、かつ
原文との差異がなかった言語の数です。**

| モデル                | 利用方法                 | 情報量の多い動向調査記事 | この README    | 差異の内容と該当する言語数                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google サブスクリプション（Antigravity）   | ✅ 14/14                | ✅ 14/14     | 両文書とも差異なし                                                                                                                                 |
| **Claude Sonnet 5.5** | Anthropic API キー                 | ✅ 14/14                | ✅ 14/14     | 両文書とも差異なし                                                                                                                                 |
| **Gemini 3.7 Flash**  | Google API キー                    | ✅ 14/14                | ⚠️ 13/14     | 14 言語中 1 言語：太字の単語が 1 つ増加（ja）                                                                                                                      |
| **Gemini 3.7 Flash**  | Google サブスクリプション（Antigravity）   | ✅ 14/14                | ⚠️ 13/14     | 14 言語中 1 言語：太字の単語が 1 つ減少（ko）                                                                                                                     |
| **GPT-5.6 Sol**       | ChatGPT サブスクリプション、または OpenAI キー | ✅ 14/14                | ⚠️ 12/14     | 14 言語中 2 言語：太字の単語が 1 つ減少（ar、ja）                                                                                                                |
| **GLM-5.2**           | OpenRouter キー                    | ✅ 14/14                | ⚠️ 11/14     | 14 言語中 3 言語：太字の単語が 1 つ減少（hi、ja、ko）                                                                                                            |
| Claude Sonnet 5       | Claude サブスクリプション（Claude Code）   | ⚠️ 13/14                | ⚠️ 13/14     | 記事では 14 言語中 1 言語：太字の単語が 1 つ増加（zh）。この README では 1 言語：表の行が前の行に連結され、表示時に非表示（ar）            |
| Claude Haiku 4.5      | Claude サブスクリプション（Claude Code）   | ⚠️ 11/14                | ✅ 14/14     | 記事では 3 言語：節の見出しがレベル 1 に変更（en、pl、ro）。この README では比較ツール上の差異はないものの、内部リンクが英語で重複 |
| Claude Sonnet 5       | Anthropic API キー                 | ⚠️ 11/14                | ⚠️ 12/14     | 記事では 3 言語：コードブロックが出現（es、de、hi）。この README では 2 言語：リンクのマークアップが消失（sv）、単語が太字に変化（zh）                              |
| Claude Haiku 4.5      | Anthropic API キー                 | ⚠️ 7/14                 | ✅ 14/14     | 記事では 7 言語：節の見出しがレベル 1 に変更。日本語ではフランス語のまま。この README では差異なし                                              |
| Claude Haiku 5.5      | Anthropic API キー                 | ⚠️ 11/14                | ❌ 12/14     | 記事では 3 言語：節の見出しのレベル変更または重複（ja、ko、zh）。この README では 2 言語が拒否され、インラインコードが欠落（ar、hi）    |
| Qwen 3.7 Flash        | OpenRouter キー                    | ❌ 8/14                 | ⚠️ 10/14     | 記事では 1 言語が拒否され、ほかの 5 言語に差異。この README では約 40 語が `code` に変化（ar）                                                    |
| Grok 4.6              | Grok サブスクリプション                   | ❌ 8/14                 | 未評価     | インラインコードと URL が返されず、14 言語中 5 言語が拒否。オランダ語では全体に差異                                                               |
| GPT-OSS 20B           | ローカルモデル（Ollama）             | ❌ 7/14                 | 未再測定 | 14 言語中 4 言語が拒否：モデルが一部をフランス語のまま残し、保護機能が停止                                                                  |
| MiMo v2.5（無料）   | OpenCode Zen、アカウント不要         | ❌ 11/14                | 未再測定 | 1 言語が拒否。ポーランド語で節が 1 つ欠落                                                                                                                  |
| Mistral Large         | Mistral API キー                   | ❌ 5/14                 | ❌ 1/14      | **節全体が消失**：記事では 1 言語（hi）、この README では 3 言語（ar、hi、ko）。さらに記事では 3 言語が拒否                                |
| DeepSeek V4 Flash     | OpenRouter キー                    | ❌ 3/14                 | 未再測定 | 14 言語中 10 言語が拒否。1 言語あたり 37 分                                                                                                                 |
| Claude Opus 5.5       | Claude サブスクリプション（Claude Code）   | ❌ 0/14                 | ✅ 14/14     | 生物学の短報が原因で、Opus の保護機能が全 14 言語で記事を拒否。この README では差異なし                                               |

|     | 記号の意味                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14 言語すべてを翻訳し、原文との差異なし                                                                                                                                       |
| ⚠️  | 14 言語すべてを翻訳。差異は**マークアップ**のみ。単語の太字、`code`、角括弧が消えたリンクなど。文章、URL、コードブロック、節の欠落はなし |
| ❌  | 少なくとも 1 言語で翻訳できず、ファイルが拒否されて書き込まれなかった、**または**書き込まれたファイルに内容の欠落がある                                                                      |

結果から分かること：

- **翻訳の拒否は、翻訳の破損ではありません。** 応答にトークンが
  欠けていると、ファイルは書き込まれず、その言語は
  拒否として数えます。記事での Grok がこの例で、非ラテン文字を使う
  5 言語では、最初の分割部分からインラインコード 4 つと URL 3 つが欠落しました。
- **モデルは、たった 1 文を理由に文書全体を拒否することがあります。** Opus 5.5 は
  この README を差異なく翻訳しますが、動向調査記事は一切翻訳できません。
  生物学の短報で保護機能が応答を停止するためです。ファイルは
  書き込まれず、aipmt が理由を表示します。
- **この保護機能は、見出し、表、フロントマター、
  本文を対象にしていません。** モデルが節を削除しても、ツールは
  そのファイルをそのまま書き込みます。Mistral がこの例です。これらの要素は
  トークンに置き換えられず、現在の保護機能では検査しません。
  `scripts/compare_structure.py` は節の欠落を検出しますが、事後の検出です。
- **この README における Grok の評価はありません**。CLI セッションが 12 言語の
  処理後に期限切れとなり、そのうち 11 言語では差異がありませんでした。中断した測定は評価しません。
- **言語よりも、文書の情報密度が影響します。** Grok は通常の
  README には対応できますが、リンクの多い記事では、オランダ語を含めて
  対応できなくなります。

測定日と対象文書：「この README」列は、2026 年 9 月 9 日に、
このファイルの固定した版（785 行、インラインコード 285 個、表の行数 89）で測定しました。
その後、このファイルには修正が加えられています。ただし、Antigravity と Claude Code の行は、
9 月 26 日に、1.14.0 とともに公開された、より短い版
（600 行、インラインコード 257 個、表の行数 85）で測定し、API 経由の Claude
Sonnet 5.5、Haiku 5.5、Haiku 4.5 の行は、10 月 18 日に
同じ版で測定しました。「情報量の多い動向調査記事」列は、
9 月 4 日と 5 日に行った、589 行の記事の測定結果です。ただし、Grok の行は
9 月 9 日に同じ動向調査の別の号で再測定し、Antigravity と
Claude Code の行は 9 月 26 日に同じ記事で測定し、上記 3 つの
Claude の行は 10 月 18 日に測定しました。完全な表、所要時間、測定手順は
[詳細な測定結果](#詳細な実測結果)にあります。
## すべてのオプション

| オプション                   | 説明                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 翻訳する単一の Markdown ファイル（`--source_dir` の代替）                                             |
| `--source_dir`           | Markdown ファイルを含むソースディレクトリ（既定値：`content/posts`）                                   |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ（既定値：`traductions_en`）                                    |
| `--source_lang`          | 翻訳元の言語（既定値：`fr`）                                                                                  |
| `--target_lang`          | 翻訳先の言語（既定値：`en`）                                                                                   |
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
| `--use_opencode`         | OpenCode（オープンソース）を使用し、OpenCode に設定されたプロバイダーに接続；`--model provider/modèle` が必須 |
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

`--eco` は各プロバイダーの低コスト枠に切り替えます。

| プロバイダー    | 高品質（既定値）                                                     | 低コスト（`--eco`）      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol`（`--model` により `gpt-5.6-sol`、`terra`、`luna` も使用可能） | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | 同左 — `--eco` は無効 |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`、推論の強度 `low`                                               | 同左 — `--eco` は無効 |
| OpenCode    | `--model provider/modèle` が必須                                | 同左 — `--eco` は無効 |
| OpenRouter  | `--model fournisseur/modèle` が必須                             | 同左 — `--eco` は無効 |

### ChatGPT サブスクリプションでの利用：`--use_codex`

公式の Codex CLI を操作します。翻訳は ChatGPT サブスクリプションの
利用枠から差し引かれ、API キーや従量課金は不要です。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 実行ファイルは `CODEX_BIN`、次に `PATH`、最後にパッケージ
  `openai-codex-cli-bin` の順で検索されます。`~/.codex/auth.json` は一切読み取られません。
- `OPENAI_API_KEY` と `CODEX_API_KEY` は子プロセスの環境から
  削除されます。キーが存在していても API に切り替わることはありません。
- 各セグメントは、5 時間の利用枠で少なくとも 1「メッセージ」を消費します。
  検証に失敗して再試行されると 2 メッセージです。OpenAI が示す目安は、
  Plus プランで `gpt-5.6-luna`（`--eco`）が 250-2 000 メッセージ/5 h、
  `gpt-5.6-sol` が 10-100 メッセージです。
- 1.16.3 まで既定だった `--model gpt-5.6-sol`、`--model gpt-5.6-terra`、
  `--model gpt-5.6-luna` もサブスクリプション経由で利用できます。
- サーバーが 429 を返してもファイルは失われません。Codex は自動で再接続し、
  aipmt はターンの終了を待ちます。それでも 429 で終わった場合、セグメントは
  30 秒後、続いて 60 秒後に再試行されます。アカウントに使用権限のないモデルでは、
  400「ChatGPT アカウントで Codex を使用する場合、このモデルはサポートされていません」
  が返されます。
- API より遅く、文書が長くなるほど差が広がります。この README では、
  `gpt-5.6-sol` の言語あたりの中央値が 6 min 46 s だったのに対し、
  `gemini-3.7-flash` は 36 s でした。
- CI では拒否されます（`CI` または `GITHUB_ACTIONS` が設定されている場合）。
  サブスクリプションの認証には個人のセッションファイルを使用するため、
  共有ランナーに置くべきではありません。
- 変数：`CODEX_BIN`、`CODEX_TIMEOUT`（セグメントあたりの秒数、既定値 600）。

### Grok サブスクリプションでの利用：`--use_grok_cli`

公式の Grok Build CLI を使い、SuperGrok または
X Premium+ サブスクリプションで同じ仕組みを利用します。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Codex より隔離が弱い点に注意。** Grok の OS サンドボックスは、
  最近の多くの Linux 環境では適用されず（AppArmor、コンテナーランタイムの
  ソケット）、適用できないプロファイルは何も通知せず隔離なしで起動します。
  そのため、このスクリプトは既定ではプロファイルを要求せず、その旨を表示し、
  すべてに一致する `*` を含む CLI の `--deny` ルールに依存します。
  これは、保護を黙って解除する代わりに起動を拒否する唯一の層です。
  `GROK_TRANSLATE_SANDBOX=read-only` を指定すると OS サンドボックスが必須になり、
  マシンが要件を満たせなければ起動に失敗します。
- 利用枠は週単位で、Chat、Imagine、Voice と共有されます。残量を読み取る
  コマンドはありません。バッチ処理が通知なしに会話用の利用枠を
  消費する可能性があります。
- 変数：`GROK_BIN`、`GROK_HOME`（CLI のディレクトリ、既定値 `~/.grok`）、
  `GROK_TIMEOUT`（既定値 900）、`GROK_TRANSLATE_SANDBOX`。

### Google サブスクリプションでの利用：`--use_antigravity`

Antigravity の公式 CLI、`agy` で同じ仕組みを利用します。Google
AI Pro または Ultra の契約者は、トークン単位で課金される代わりに、
翻訳がサブスクリプションの利用枠から差し引かれます。この利用枠を使える経路はこれだけです。
Gemini CLI は 2026 年 6 月 18 日以降、これらのアカウントに対応しておらず
（[発表](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)）、
Antigravity SDK が受け付けるのは API キーまたは Google Cloud プロジェクトだけです。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **有料経路を一切残しません。** agy に渡される環境変数は、
  `PATH`、言語とタイムゾーン、端末、ユーザー識別情報、プロキシと証明書、
  セッションバスに関する限定された一覧だけで、キーは渡されません。
  agy の複数の変数は、何も表示せず呼び出し先を切り替えてしまいます
  （実測では、ある変数は文書を第三者のゲートウェイに送り、別の変数は課金対象の
  Google Cloud プロジェクトに送信しました）。拒否リスト方式では、見直すたびに
  漏れが見つかりました。各セグメントの処理前に、利用枠を消費しない `agy -p /config` で、
  有料 AI クレジットが無効で、API キーも Google Cloud プロジェクトもないことを
  確認できなければなりません。設定が存在しない場合も拒否され、条件を満たさなければ
  翻訳は行われません。さらに、各呼び出しのログでサブスクリプションの使用
  （`authMethod=consumer`）を確認できなければ、応答は拒否されます。
- **隔離。** 各呼び出しは、ツールを持たない翻訳エージェントを使い、
  非公開の使い捨てホームディレクトリで実行されます。ユーザーの agy の設定、ルール、
  プラグイン、MCP サーバー、フックは持ち込まれず、履歴にも追加されません。
  認証情報はキーリングに残り、aipmt がそれを読み取ることはありません。
  指定したエージェントが見つからないと、agy は何も通知せずコーディング用エージェントと
  そのツールに切り替わります。そのため、ログの完全な 1 行で正しいエージェントを
  確認できなければ拒否されます。文書内にそのメッセージが引用されていても代用にはなりません。
- **プラットフォーム**：キーリングを備えたセッション（D-Bus セッションバス、
  Secret Service）がある Linux。macOS も受け付けますが、実測はしていません。
  Windows では、各呼び出しを隔離する変数を agy が読み取らないため拒否されます。
  セッションバスのない Linux（SSH セッション、コンテナー、サーバー）でも拒否されます。
  こうした環境では、agy がトークンを `~/.gemini` 内のファイルに保存しますが、
  隔離によってそのファイルが見えなくなるためです。ログインコードを 1 分間待たせるのではなく、
  起動前に理由を示して拒否します。
- **モデル**：`agy models` に掲載されているもの。Gemini は名前に推論の強度を含みます
  （`gemini-3.8-flash-medium` など）。接尾辞のない名前は呼び出し前に拒否され、
  `--reasoning_effort` は無効です。既定値は `gemini-3.8-flash-medium`、
  `--eco` では `gemini-3.7-flash-low` です。これらの選定に使った一連の測定は
  [詳細な測定結果](#詳細な実測結果)に記載しています。Claude と GPT-OSS には、
  はるかに小さい独自の利用枠があります。実測では、1 回の呼び出しで 5 時間枠の
  約 1 % を消費するのに対し、Flash では 0,05 % です。
- **利用枠**：グループごとに 5 時間枠と週単位の枠があり、
  トークンコストに比例して消費されます。著者のアカウントでの実測では、
  ソース 100 万文字あたりの 5 時間枠の消費は `gemini-3.8-flash-medium` で約
  16 ポイント、`gemini-3.7-flash-medium` で 14 ポイント、推論の強度が低い場合は
  7～8 ポイントでした。したがって、40 000 文字の README は
  0.5 ポイント強を消費します。一方、週単位の上限は契約プランによって異なります。
  再試行は agy が再試行可能と示した場合に従います。それ以外では、
  枠を使い切った呼び出しを再試行しません。`/usage` に表示される
  リセット時刻まで、すべてのファイルの処理が失敗します。
- **API より低速**：測定に使った内容の密な記事では、言語あたりの中央値は
  `gemini-3.8-flash-medium` で 3 min 59 s、
  `gemini-3.7-flash-medium` で 3 min 14 s でした。API 経由の Gemini 3.7 Flash では 1 min 18 s です。
- **中断**：Ctrl-C を押すか端末を閉じると、agy もコマンドとともに停止し、
  利用枠を消費しながらターンを完了するまで動き続けることはありません。
  Codex、Grok CLI、OpenCode も同様です。`nohup` では翻訳が継続します。
- CI では拒否されます（`CI` または `GITHUB_ACTIONS` が設定されている場合）。
  認証情報は個人のキーリングに保存されます。ランナーでは、
  `--use_gemini` と `GOOGLE_API_KEY` を使用してください。
- 変数：`AGY_BIN`（なければ `PATH`、次に `~/.local/bin/agy`）、
  `AGY_TIMEOUT`（起動時間を含むセグメントあたりの秒数、既定値 900）。

**利用規約：責任を負うのはご自身のアカウントです。**
[Antigravity の利用規約](https://antigravity.google/terms)（第 6 条）と
[よくある質問](https://antigravity.google/docs/faq/)では、Antigravity の認証情報を使って
第三者のソフトウェアからサービスにアクセスすることを禁止しており、
Claude Code、OpenClaw、OpenCode が例として挙げられています。
違反するとアカウントが停止される可能性があります。aipmt はトークンを
読み取ったり再利用したりせず、Google がスクリプトや CI 向けに文書化している
[ヘッドレスモード](https://antigravity.google/docs/cli/headless/)で公式の実行ファイルを起動します。
Google のメンバーは、自分の作業のためにローカルスクリプトから
`agy -p` を起動することを「標準的」と述べています
（[公式フォーラム、2026 年 9 月 25 日、契約上の効力のない回答](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）。
ただし、このツールのように配布されるものの扱いを明確に定めた文書はありません。

**公開文書のみを対象にしてください。** 同じ規約の第 5 条によると、
やり取り（プロンプト、応答、メタデータ）は、有料サブスクリプションであっても、
Google の製品や機械学習の改善に使用され、人間によって確認される可能性があります。
利用を拒否するには `enableTelemetry` の設定を使いますが、その効果は文書化されておらず、
aipmt はこの設定を行いません。ユーザーの agy 設定は隔離環境に引き継がれません。
機密情報は一切送信しないでください。
### Claude サブスクリプションでの利用：`--use_claude_code`

Claude Code の公式 CLI である `claude` を `-p` モードで使う場合も同じ仕組みです。
Claude Pro または Max の契約者は、翻訳がトークン単位で課金される代わりに、
サブスクリプションの利用枠から差し引かれます。
従量課金の Anthropic API である `--use_claude` と混同しないでください。

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **有料の経路はすべて遮断され、呼び出しのたびにそれを確認します。** Claude
  Code に環境から渡される変数は、あらかじめ限定された一覧だけです。
  API キー、トークン、クラウドプロバイダー、aipmt の起動元となる Claude Code
  セッションの識別情報は渡されません。最初のセグメントの前に、`claude auth status` が
  Console キーを使わないサブスクリプション接続を示し、利用枠を
  消費しない `/usage` がそれを確認する必要があります。各呼び出しも
  初期化イベントで同じことを確認し、確認できなければ応答を拒否します。
- **「追加使用」を無効にしてください**（claude.ai、設定 → 使用量）。
  費用をゼロユーロに保つためです。有効にすると、時間枠の利用上限に達した後も
  エラーを表示せずに処理を続け、課金されます。aipmt は呼び出しの利用枠情報で
  それを検出すると翻訳を停止しますが、その呼び出し分はすでに計上されています。
- **利用枠は Claude Code セッションと共有されます。** 各呼び出しは
  5 時間枠と週間枠の使用状況を報告します。80 % を超えると
  （`AIPMT_CLAUDE_MAX_UTILIZATION`）、仕事に使う分を使い切らないように、
  次のセグメントは開始しません。
- **隔離。** 各呼び出しは、専用の使い捨てディレクトリ内で、
  ツールなし、カスタマイズなしのモードで実行されます。利用者の `CLAUDE.md`、プラグイン、
  フック、MCP サーバー、設定は読み込まれず、
  セッションの情報も保存されません。添付機能は無効です。文書内の `@chemin` は
  テキストのままで、ファイルを開きません（実測済み）。
- **モデル**：既定は `sonnet`、推論の強度は `low` で、`--eco` でも同じです。
  この経路では `--eco` は効果がありません。同じ文書で実測したところ、`haiku` は
  速度が半分で、推論を止めることもできず、
  費用もわずかに安いだけでした。`opus` は生物学の内容を拒否します（次の項目）。
  どちらも `--model` で利用できます。これらのエイリアスは、
  各系列の最新モデルを指します。`fable` と `[1m]` の派生モデルは、
  有料クレジットを使うため拒否されます。`--reasoning_effort` は推論の強度を設定しますが、
  翻訳では効果がなく、実測された推論量はゼロか、ほぼゼロです。
- **Opus は生物学の一部の内容を拒否します。** 安全対策が
  Sonnet より厳しく、Anthropic のエラーメッセージでも、
  「生物学研究に関連する作業が検出対象になることがある」と説明されています。実測では、
  生成された 279 個の分子を扱う短いニュースが原因で、14 言語すべてで記事が拒否されました。
  ファイルは書き込まれません。aipmt は途中で切れた応答を拒否し、
  安全対策による停止であることを明示して、`--model sonnet` を勧めます。
- CI（`CI` または `GITHUB_ACTIONS` が設定済み）および Windows では拒否されます（未実測）。
- 変数：`AIPMT_CLAUDE_BIN`（未指定なら `PATH`、次に `~/.local/bin/claude`）、
  `AIPMT_CLAUDE_TIMEOUT`（セグメントごとの秒数、既定値 900）、
  `AIPMT_CLAUDE_MAX_UTILIZATION`（既定値 0.8）、`CLAUDE_CONFIG_DIR`（Claude Code の
  アカウント。プロジェクトの `.env` からは取得しません）。作業ディレクトリは
  `XDG_CACHE_HOME/aipmt/claude-code` 配下です（既定値 `~/.cache`）。

**利用規約：責任を負うのは利用者のアカウントです。**
[Claude Code の法的事項ページ](https://code.claude.com/docs/en/legal-and-compliance)は、
「エンドユーザーが自分の Claude サブスクリプションを使って、
変更されていない Claude Code バイナリにサインインすること」を禁じていません。
aipmt はまさにこの方法で、公式バイナリを起動し、トークンを読み取ることはありません。
ただし Anthropic は、「第三者の開発者が、利用者に代わって
Free、Pro、Max プランの認証情報を使い、リクエストを転送することを許可していない」
とし、「オープンソースプロジェクトを含む」第三者ツールには API キーの使用を推奨し、
その利用分を有料クレジットから差し引く権利を留保しています
（[Claude ヘルプ](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)）。
配布されたツールがバイナリを起動する場合について、明確に判断できる記述はありません。

**データ**：Free、Pro、Max のアカウントでは、プライバシー設定で許可されている場合、
Claude Code もモデルの学習対象になります
（[データに関するページ](https://code.claude.com/docs/en/data-usage)）。aipmt は
ローカルに会話記録を残しません（`--no-session-persistence`）。機密情報を
送信しないでください。

### 任意のプロバイダーへの接続：`--use_opencode`

[OpenCode](https://opencode.ai) は、内部で設定されたプロバイダーに
リクエストを転送するオープンソースのコーディングエージェント（MIT）です。
API キー、サブスクリプション、OpenCode Zen ゲートウェイ（無料モデル、アカウント不要）、
ローカルモデルを利用できます。ここでは Zen と Ollama の 2 つの経路を、
最初から最後まで実測しました。

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

`--model` は必須です。これがないと、OpenCode はやり取りが学習に使われる可能性のある
無料モデルにフォールバックするため、その選択を利用者の代わりに
行うことはしません。

各呼び出しでの隔離：

- 利用者の設定より優先されるインライン設定で、すべてのツールを拒否する
  エージェント `aipmt` を定義します（`permission: { "*": "deny" }`）。セッション共有は
  無効にし、`--pure` を使い、`--auto` は決して使いません。
- 空の使い捨て作業ディレクトリを使い、`OPENCODE_DISABLE_PROJECT_CONFIG` と
  `OPENCODE_DISABLE_CLAUDE_CODE` を設定します。これらがないと、OpenCode は
  現在のディレクトリの `AGENTS.md` と `~/.claude/CLAUDE.md` をプロンプトに挿入します。
  グローバルの `~/.config/opencode/AGENTS.md` は引き続き挿入されます。OpenCode には
  これを除外する方法がありません。
- 出力の検証条件：終了コードが 0、`error` イベントがないこと、ツールの
  呼び出しがないこと、最後のステップが `stop`、テキストが空でないこと、
  エージェント `aipmt` が実際に読み込まれていることです。未知の `--agent` を指定しても
  OpenCode は失敗せず、通知なしでコーディングエージェントにフォールバックします。
- `aipmt` のキーは、OpenCode 自体のキーである `OPENCODE_API_KEY` を除き、
  渡されません。プロバイダーは OpenCode 内で設定し、
  `aipmt` の `.env` では設定しません。

留意点：

- Zen の無料モデルは入れ替わり、制限も文書化されていません。
  やり取りが学習に使われる可能性があるため、公開文書向けであり、
  非公開の内容には向きません。
- セグメントは最大 16 000 文字になるため、ローカルモデルには
  少なくとも 16 k トークンのコンテキストが必要です。Ollama では 4 096 に設定されていることが多いため、
  `PARAMETER num_ctx 32768` を指定した `Modelfile` を使ってください。
- `--eco` は効果がありません。`--reasoning_effort` は OpenCode の
  `--variant` として、そのまま渡されます。
- OpenCode は各セッションを `~/.local/share/opencode/` に記録します。
- 変数：`OPENCODE_BIN`（未指定なら `PATH`、次に `~/.opencode/bin/opencode`）、
  `OPENCODE_TIMEOUT`（セグメントごとの秒数、既定値 600）。`OPENCODE_CONFIG` は
  OpenCode にそのまま渡されます。

Ollama 経由でローカルモデルを使う例。`~/.config/opencode/opencode.json` 内に記述します。

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
無効にします。この推論は Modelfile では無効にできません。6 単語の文で
実測したところ、このオプションなしでは推論に 919 トークンと 68 秒を使い、指定すると 9 トークンでした。

### 400 を超えるモデルへの接続：`--use_openrouter`

OpenRouter は、単一のクレジット残高で利用する従量課金のルーターです。
第三者がホストするモデルに接続でき、ここで扱うほかのプロバイダーでは
利用できない中国のオープンモデルも含まれます。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` は必須です。課金が発生する前に事前チェックを実行し、
ルーティングに関する 2 つの特性に対応します。

- **同じモデルでも、提供するホスティング事業者が数十社あり、上限が
  異なります**。`z-ai/glm-5.3-flash` では 23 社あり、そのうち 1 社は
  出力が 2 048 トークンに制限されています。事前チェックは `/api/v1/models/{modèle}/endpoints` を読み、
  出力が 8 000 トークン未満の事業者や稼働状態が低下している事業者を除外し、
  残りを `allow_fallbacks: false` で固定します。
- **推論は出力と同じ単価で課金されます**。`z-ai/glm-5.2` の
  「OK」という応答では、2 トークンに対して 107 トークンでした。既定では無効にし、
  推論が必須のモデルには、受け付ける最も低い推論強度を指定します。
  カタログの既定値では、翻訳が終わる前に出力枠を使い切る可能性があるためです。
  `--reasoning_effort` が引き続き優先されます。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- コンテキスト長はカタログから取得します。16 400 トークン未満のモデルは、
  呼び出し前に拒否します。プロンプトとセグメントに 8 400、
  出力に最低 8 000 トークンが必要です。
- スラッグがカタログに存在しない、カタログに接続できない、または
  必要な上限を満たすホスティング事業者がない場合、コマンドを停止します。
- 出力が空の `finish_reason=length` は、推論によって予算を消費した状態であり、
  出力の切り捨てではありません。メッセージで両者を区別します。
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
と、その後に続く太字の引用で構成されます。GitHub で読むことができ、ビルド時には
remark プラグインで処理できます。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 詳細な実測結果

すべての実測は、`aipmt` を使って実際に実行した翻訳で、対象は
14 言語です：en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi。
**書き込み済み**は検証を通過したファイル数、**差異なし**は
`scripts/compare_structure.py` が何も検出しなかったファイル数です。セクション、小見出し、
リンク、重複を除いた URL、コードブロック、インラインコード、表の行、
引用ブロック、太字の語の数が同じであることを示します。

「差異なし」は「何も検出されなかった」という意味で、「同一」という意味ではありません。
比較処理は内容を読まず、要素の数だけを数えます。レベル 4 の見出しの削除、
インラインコードの内容の置換、旗の置換、
余分な閉じ括弧によってリンク先に移動できなくなった内部リンク
`[texte]((#ancre))` などは検出しません。
また、言語の正しさも判定しません。

### 情報量の多いニュース記事、`--news` モード

[jls42.org の AI ニュース](https://jls42.org/fr/news)の 1 回分です。
589 行、140 リンク、21 セクション、保護された英語の引用 3 件。
2026 年 9 月 4 日と 5 日に実施しました。

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

Grok は 9 月 9 日に、同じニュースの別の回
（356 行）で再測定しました。14 言語中 9 言語を書き込み、8 言語が差異なしでした。
冒頭の表にはこの数値を掲載しています。途中で中断した 3 回の測定は
掲載していません。`qwen3.5-27b`（9 言語）と `kimi-k2.6`（4 言語）はクレジット不足、
`z-ai/glm-5.3-flash` は推論設定が原因で 2 件失敗しましたが、
この設定はその後プロバイダー側で補正されるようになりました。OpenRouter の各行は、
`--use_openrouter` の導入前に、ルーターの既定設定で測定したものです。`z-ai/glm-5.2` は、
提供されているプロバイダー実装で再測定しても、同じ 14/14 でした。数値は
9 月 10 日に現在の比較処理で再計算しました。`qwen3.8-flash` と
`qwen3.7-flash` は初回公開時よりそれぞれ 1 言語増え、
ほかは変わっていません。

`--use_antigravity` の各行は、9 月 26 日に同じ記事を使い、
4 翻訳を並列実行して測定しました。午前に `gemini-3.7-flash-medium`、
午後に `gemini-3.8-flash-medium` を測定しました。英語では、どちらも引用の下にある
フランス語訳の 3 行を自ら削除し、旗を新たに作ることもなく、
英語の引用もそのままでした。フォールバックの後処理は
何もする必要がありませんでした。`--eco`（`gemini-3.7-flash-low`）では、4 言語
（en、ja、ar、hi）のみを測定し、4 言語中 4 言語を書き込み、すべて差異なし、
中央値は 1 min 52 s でした。同日、より新しい 9 月 25 日分のニュース
（438 行、英語の引用 2 件）でも確認しました。
ブログの外で `gemini-3.7-flash-medium` を使って翻訳した結果、14 言語中 14 言語を書き込み、
すべて差異なし、各言語 87～128 s でした。

`--use_claude_code` の各行は、9 月 26 日に同じ記事を使い、
推論の強度を `low` にして、4 翻訳を並列実行して測定しました。`sonnet` では、
14 言語すべてで英語の引用がそのまま保たれ、英語では
モデル自身がフランス語訳の行を削除し、旗を新たに作ることもありませんでした。
`opus` はどの言語も書き込みませんでした。すべての言語で、
結合部位に対して生成された 279 個の分子を扱う短いニュースが原因となり、
最後のセグメントで安全対策が応答を停止しました。この短いニュースだけを送っても、
「生物学」カテゴリとして拒否されます。`sonnet` はすべての言語で翻訳しました。`haiku` は
14 言語を書き込みましたが、3 言語（en、pl、ro）では、セクション見出しが
レベル 2 からレベル 1 に変わりました。推論は止めることができず、
出力トークンの 61 % を占めるため、`sonnet` の 2 倍以上の時間がかかりました。

`claude-sonnet-5-5`、`claude-haiku-5-5`、`claude-haiku-4-5` の各行は、
10 月 18 日に Anthropic API 経由で、同じ記事を使い、
モデルごとに 4 翻訳を並列実行して測定しました。Sonnet 5.5 は推論の
無効化を受け付けません。aipmt は受け付ける最も低い設定を送り、
応答には推論が含まれませんでした。セグメントを再試行せずに 14 言語を差異なしで
書き込みました。英語では、モデル自身がフランス語訳の
行を削除し、旗を新たに作ることもなく、英語の引用も
すべてそのまま保たれました。Haiku 5.5 は適応型推論を有効にして測定しました。
推論を無効にすると、段落全体をフランス語のまま残し、検証で拒否されました。
書き込めたのは 14 言語中 3 言語です。2 つの Haiku は同じ短いニュースでつまずきました。
Haiku 5.5 は日本語、韓国語、中国語で見出しのレベルを変えるか重複させ、
Haiku 4.5 は 7 言語でレベル 1 に変え、
日本語ではフランス語のまま残しました。2 つの文書を
14 言語に翻訳する費用は、Haiku 4.5 が 3,67 $、Haiku 5.5 が 0,57 $、Sonnet 5.5 が 9,21 $ でした。
### このプロジェクトの README、標準 Markdown

2026年9月9日に固定した版：785 行、285 個のインラインコード、40 個の
ブロック終端、89 行の表。4 件の翻訳を並列実行。

| モデル                                          | 作成済み | 差異なし | 言語ごとの中央値 | 差異の内容                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | なし                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | なし                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | 比較ツールでは差異なし；内部リンクの重複 (en)                   |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | なし                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | なし                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | 太字の単語 1 個 (ja)                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | 太字の単語 1 個 (ko)                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | 表の 1 行が前の行に結合 (ar)                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | リンク 1 個 (sv)、太字の単語 1 個 (zh)                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | 太字の単語 1 個 (ar, ja)                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | 太字の単語 1 個 (hi, ja, ko)                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | アラビア語でインラインコード 40 個が追加；太字 (hi, ja, ko)                   |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2 言語を拒否 (ar, hi)：返却時にインラインコードが欠落        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | セクション 1 個が欠落 (ar, hi, ko)；コードブロックの追加 (ja, ko, ro, zh) |

中断された 2 回の測定は集計に含めていません。Grok は 12 言語の処理後に CLI セッションが
期限切れとなり（うち 11 言語は差異なし）、`qwen3.8-flash` は 2 言語の処理後に
提供元から HTTP 429 が返されました。`opencode/mimo-v2.5-free` と `ollama/gpt-oss-20b-32k` は
この版で再測定していません。277 行短かった9月4日と5日の版では、
それぞれ 14 件中 9 件の翻訳を作成し、差異なしはそれぞれ 7 件と
1 件でした。

`--use_antigravity` と `--use_claude_code` の行は、固定版ではなく、
1.14.0 とともに公開された版を使って9月26日に測定しました。
`claude-sonnet-5-5`、`claude-haiku-5-5`、`claude-haiku-4-5` の行は10月18日に
同じ版で測定しました。600 行、257 個のインラインコード、30 個のブロック終端、85
行の表です。185 行
短いため、ほかの行と同じ条件で比較することはできませんが、
これらの行同士は比較できます。比較ツールが検査しない内部リンクについては、
`gemini-3.8-flash-medium` は 14 言語すべてで正常に保持し、
`gemini-3.7-flash-medium` はイタリア語でリンクを壊しました。
`sonnet` と `opus` はすべてで正常に保持し、`haiku` は
英語で重複させました。`claude-sonnet-5-5` と `claude-haiku-4-5` は
14 言語すべてで、`claude-haiku-5-5` は作成した 12 言語で正常に保持しました。

### 著名なプロジェクトの README 4 件

FastAPI、Ollama、tldr-pages、Vue.js を GitHub からそのまま取得しました。
前の 2 件よりも容易な文書です。この測定は苦戦していたモデルを対象とし、
Gemini を比較基準にしています。

| モデル                    | 対象範囲                  | 作成済み | 差異なし   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 プロジェクト × 14 言語     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 プロジェクト × 14 言語     | 55/56   | ❌ 47/56     |
| `grok-4.6` (サブスクリプション)   | 4 プロジェクト × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 プロジェクト × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### これらの測定が意味しないこと

- **網羅的なランキングではありません**：OpenRouter だけでも 400 を超える
  モデルが提供されていますが、測定したのは 15 種類ほどです。
- **所要時間は目安です**：測定ごとに 3〜6 件の翻訳を並列実行しており、
  提供元の処理速度も一日の中で変動します。
- **特定の時点での観測です**：同じ名前でもモデルは変化し、
  皆さんの文書は私たちの文書とは異なります。

ご自身の文書で測定を再現するには、ファイルの固定コピーで次を実行します。

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

両方の行が必要です。`pip install -e .` がないと、`python -m aipmt` は
`No module named aipmt` と応答します。

品質管理ツールは任意ですが、利用を推奨します。

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

リポジトリの 28 件の翻訳（README と CHANGELOG、14 言語）は
`./regen_translations.sh --force` で再生成できます。既定では ChatGPT サブスクリプション上の
Codex と `gpt-6.1-sol` を使用し、4 件を並列実行します。`REGEN_PROVIDER` と
`REGEN_MODEL` で利用経路を変更できます。`antigravity` は Google の
サブスクリプションを引き続き使用し、例外指定なしで実行できます。従量課金の API
（`openai`、`gemini`、
`grok`、`openrouter`）は `REGEN_ALLOW_PAID_API=1` なしでは拒否されます。
`REGEN_JOB_TIMEOUT` は各ジョブの時間上限を設定します（600 s、Codex と
Antigravity では 1 800 s）。ツールの詳細は `CLAUDE.md` にあります。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** — 15 言語で公開している個人ブログです。
  [日々の AI 動向](https://jls42.org/fr/news)はこのツールで毎日翻訳され、
  上記の測定の基準文書として使用されています。

## 作者

Julien LE SAUX
メール：contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE バージョン 3。[ライセンス](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)を参照してください。

## 注意事項

このプログラムは GPL v3 の第 15 条および第 16 条に基づき、**一切の保証なし**で
配布されます。「現状のまま」で提供され、商品性や特定目的への適合性の保証はなく、
使用によって生じた損害について作者は責任を負いません。
この要約よりもライセンス本文が優先されます。

- **公開前に読み直してください。** 保護対象はコードブロック、
  インラインコード、URL、アンカー、`--news` モードの引用です。
  見出し、表、フロントマター、文章の意味は保護対象に含まれません。
- **文書は選択した提供元に送信され**、その利用規約と
  データポリシーが適用されます。一部の無料モデルでは、やり取りが
  学習に再利用される場合があります。また、Antigravity の規約では、有料
  サブスクリプションも含め、Google がやり取りを再利用し、人間による確認を行うことが
  認められています。データを一切ご自身の端末から外に出さない唯一の方法は、
  ローカルモデルを使用することです。
- **API 呼び出しの料金は利用者に請求されます。** このプログラムは支出に
  上限を設けません。長い文書、失敗後の再試行、推論を多く行うモデルは、
  費用が高くなります。
- **公開された測定値は特定の時点での観測であり**、保証ではありません。

記載されている製品名と会社名は、それぞれの権利者に帰属します。
このプロジェクトはいずれとも提携していません。

**gpt-6.1-solでフランス語から日本語に翻訳された記事。**
