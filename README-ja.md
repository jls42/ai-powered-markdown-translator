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

Markdown ファイルを別の言語に翻訳しながら、
コードブロック、インラインコード、URL、アンカー、表、フロントマターの
構造を保持します。モデルの呼び出し方法は 11 通り。5 つの API、従量課金のない
4 つのサブスクリプション、2 つのルーターに対応し、各モデルが実際に
何を保持できるかを測定した結果を公開しています。

## 概要

- **11 通りのプロバイダー経路**：OpenAI、Mistral、Claude、Gemini、Grok の API、
  従量課金のない ChatGPT（Codex）、Grok、Google（Antigravity）、Claude（Claude
  Code）のサブスクリプション、OpenCode（オープンソース、無料またはローカル）と OpenRouter
  （400 以上のモデル）のルーター。
- **トークンの欠落による破損を防止**：コードブロック、インラインコード、
  URL、アンカー、引用を呼び出し前にトークンへ置き換え、
  応答後に検証します。1 つでも欠けていれば、ファイルは書き込みません。
- **長い文書**：モデルのコンテキストウィンドウに応じて分割します。
- **`--news` モード**：情報収集記事向けに、英語の引用を保護し、
  言語ごとにフラグを管理します。
- **`--eco` モード**：高速で低料金のモデルを使用します。
- 任意の**翻訳注記**を、冒頭、末尾、または両方に追加できます。

## インストール

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 以降が必要です。リポジトリからインストールする場合は、
[貢献方法](#貢献)を参照してください。

## 設定

キーは次の 3 か所から優先順位順に読み込みます。各設定元は、
それより優先度の高い設定元で未設定の項目のみを補います。

|     | 場所                                            | 用途                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 環境変数                     | CI、コンテナー、一時的な上書き |
| 2   | 現在のディレクトリ（または親ディレクトリ）の `.env` | プロジェクト専用のキー            |
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
`XDG_CONFIG_HOME`（絶対パスのみ）に従い、Windows では `%APPDATA%`
に従います。キーがない場合、コマンドは 3 つの設定場所を列挙します。

**プロジェクトの `.env` では、呼び出し先の変更も、実行するプログラムの選択も
できません。** このファイルが提供するのはキーだけで、接続先や実行ファイルではありません。
`_BASE_URL`、`_API_BASE`、`_ENDPOINT`、`_BIN` に該当する変数（`CODEX_BIN`、
`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`）、`GROK_HOME`、プロキシ（`HTTP_PROXY`、
`HTTPS_PROXY`、`ALL_PROXY`）、証明書ストア（`SSL_CERT_FILE`、
`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）、`XDG_CONFIG_HOME` /
`APPDATA` はすべて無視され、警告が表示されます。クローンしたリポジトリが
キーを盗み取ったり、最初の翻訳時に独自のプログラムを実行させたり
できてはなりません。このファイルは変数展開なしで読み込みます。
`NOM=${OPENAI_API_KEY}` によってキーがコピーされることもありません。これらの変数は
環境変数または `~/.config/aipmt/.env` に設定してください。

任意の変数：`XAI_BASE_URL`（既定値 `https://api.x.ai/v1`）、
`CLAUDE_TIMEOUT`（呼び出しあたりの秒数、既定値 900）、`CODEX_BIN`、`CODEX_TIMEOUT`
（既定値 600）、`GROK_BIN`、`GROK_HOME`（既定値 `~/.grok`）、`GROK_TIMEOUT`
（既定値 900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（既定値 900）、
`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（既定値 600）、`OPENROUTER_BASE_URL`
（`https://` が必須）、`OPENROUTER_TIMEOUT`（既定値 900）、
`OPENROUTER_PREFLIGHT_TIMEOUT`（既定値 30）。それぞれの詳細は、
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

`document.md` をスペイン語に翻訳すると、`--target_dir` 内に `document-es.md` が生成されます。
`--include_model` を指定すると、`document-es-gpt-5.6-terra.md` になります。拡張子は
常に `.md` になります。たとえば `article.mdx` は `article-en.md` になります。ただし、
`--keep_filename` を指定すると、元の名前を保持します。翻訳済みのファイルは、
`--force` を指定しない限りスキップします。

終了コード：すべて成功またはスキップした場合は `0`、失敗したファイルが
残っている場合は `1`（標準エラー出力に一覧を表示）、設定に問題がある場合は `2` です。
失敗したファイルは、書き込み自体が失敗した場合も含めて、決して書き込まれません。
内容を同じ場所の別ファイルに書き込んでから、名前を変更します。再実行するだけで対応できます。

## モデルの選び方

実際の文書 2 本を使い、各モデルで同じ 14 言語へ翻訳して測定しました。
**数値は、14 言語のうち、翻訳ファイルが書き込まれ、
原文との差異がまったくなかった言語数です。**

| モデル                | 利用方法                 | 情報密度の高い情報収集記事 | この README    | 差異の内容と対象言語数                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Google サブスクリプション（Antigravity）   | ✅ 14/14                | ✅ 14/14     | どちらの文書にも差異なし                                                                                                                                 |
| **Claude Sonnet 5.5** | Anthropic API キー                 | ✅ 14/14                | ✅ 14/14     | どちらの文書にも差異なし                                                                                                                                 |
| **Gemini 3.7 Flash**  | Google API キー                    | ✅ 14/14                | ⚠️ 13/14     | 14 言語中 1 言語：太字の単語が 1 つ増加（ja）                                                                                                                      |
| **Gemini 3.7 Flash**  | Google サブスクリプション（Antigravity）   | ✅ 14/14                | ⚠️ 13/14     | 14 言語中 1 言語：太字の単語が 1 つ減少（ko）                                                                                                                     |
| **GPT-5.6 Sol**       | ChatGPT サブスクリプション、または OpenAI キー | ✅ 14/14                | ⚠️ 12/14     | 14 言語中 2 言語：太字の単語が 1 つ減少（ar、ja）                                                                                                                |
| **GLM-5.2**           | OpenRouter キー                    | ✅ 14/14                | ⚠️ 11/14     | 14 言語中 3 言語：太字の単語が 1 つ減少（hi、ja、ko）                                                                                                            |
| Claude Sonnet 5       | Claude サブスクリプション（Claude Code）   | ⚠️ 13/14                | ⚠️ 13/14     | 記事では 14 言語中 1 言語：太字の単語が 1 つ増加（zh）。この README では 1 言語：表の行が直前の行に連結され、表示されなくなった（ar）            |
| Claude Haiku 4.5      | Claude サブスクリプション（Claude Code）   | ⚠️ 11/14                | ✅ 14/14     | 記事では 3 言語：節の見出しがレベル 1 に変更（en、pl、ro）。この README では比較ツール上の差異はないものの、内部リンクが英語で重複 |
| Claude Sonnet 5       | Anthropic API キー                 | ⚠️ 11/14                | ⚠️ 12/14     | 記事では 3 言語：コードブロックが追加（es、de、hi）。この README では 2 言語：リンクのマークアップが欠落（sv）、太字の単語に差異（zh）                              |
| Claude Haiku 4.5      | Anthropic API キー                 | ⚠️ 7/14                 | ✅ 14/14     | 記事では 7 言語：節の見出しがレベル 1 に変更。日本語ではフランス語のまま残存。この README では差異なし                                              |
| Claude Haiku 5.5      | Anthropic API キー                 | ⚠️ 11/14                | ❌ 12/14     | 記事では 3 言語：節の見出しのレベル変更または重複（ja、ko、zh）。この README では 2 言語が拒否され、インラインコードが欠落（ar、hi）    |
| Qwen 3.7 Flash        | OpenRouter キー                    | ❌ 8/14                 | ⚠️ 10/14     | 記事では 1 言語が拒否され、ほかの 5 言語に差異。この README では約 40 語が `code` に変更（ar）                                                    |
| Grok 4.6              | Grok サブスクリプション                   | ❌ 8/14                 | 未評価     | 14 言語中 5 言語がインラインコードと URL の欠落により拒否。オランダ語では全体に差異                                                               |
| GPT-OSS 20B           | ローカルモデル（Ollama）             | ❌ 7/14                 | 未再測定 | 14 言語中 4 言語が拒否：モデルがフランス語の文章を残したため、保護機構が処理を停止                                                                  |
| MiMo v2.5（無料）   | OpenCode Zen、アカウント不要         | ❌ 11/14                | 未再測定 | 1 言語が拒否。ポーランド語では節が 1 つ欠落                                                                                                                  |
| Mistral Large         | Mistral API キー                   | ❌ 5/14                 | ❌ 1/14      | **節全体が消失**：記事で 1 言語（hi）、この README で 3 言語（ar、hi、ko）。さらに記事では 3 言語が拒否                                |
| DeepSeek V4 Flash     | OpenRouter キー                    | ❌ 3/14                 | 未再測定 | 14 言語中 10 言語が拒否。1 言語あたり 37 分                                                                                                                 |
| Claude Opus 5.5       | Claude サブスクリプション（Claude Code）   | ❌ 0/14                 | ✅ 14/14     | 生物学の短い記事が原因で、Opus の保護機構が全 14 言語で記事を拒否。この README では差異なし                                               |

|     | 記号の意味                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 全 14 言語を翻訳し、原文との差異なし                                                                                                                                       |
| ⚠️  | 全 14 言語を翻訳。差異は**マークアップ**のみで、太字の単語、`code`、角括弧が失われたリンクなど。本文、URL、コードブロック、節の欠落はなし |
| ❌  | 少なくとも 1 言語を翻訳できず、ファイルが拒否され書き込まれなかった、**または**書き込まれたファイルに内容の欠落がある                                                                      |

結果からわかること：

- **拒否された翻訳は、壊れた翻訳ではありません。** 応答でトークンが
  欠落していれば、ファイルは書き込まれず、その言語は
  拒否として数えられます。記事に対する Grok の結果がこれに該当します。非ラテン文字の
  5 言語で、最初の分割部分からインラインコード 4 つと
  URL 3 つが欠落しました。
- **たった 1 文のために、モデルが文書全体を拒否することがあります。** Opus 5.5 は
  この README を差異なく翻訳しますが、情報収集記事は翻訳できません。
  生物学の短い記事で保護機構が応答を停止するためです。ファイルは
  書き込まれず、aipmt がその理由を表示します。
- **この保護機構は、見出し、表、フロントマター、
  本文を対象にしていません。** モデルが節を削除しても、ツールは
  そのファイルを問題なく書き込みます。Mistral がその例です。これらの要素は
  トークンに置き換えられず、現在の保護機構でも検証しません。
  `scripts/compare_structure.py` は節の欠落を検出しますが、それは処理後です。
- **この README に対する Grok の評価はありません**：CLI セッションが 12 言語の処理後に
  期限切れとなりました。そのうち 11 言語では差異がありませんでした。中断された測定は評価しません。
- **言語よりも文書の情報密度が影響します。** Grok は通常の
  README では対応できますが、リンクの多い記事では
  オランダ語も含めて対応できなくなります。

日付と文書：「この README」列は、2026 年 9 月 9 日に
このファイルの固定版（785 行、インラインコード 285 個、表 89 行）で測定しました。
その後、このファイルには修正が加えられています。ただし、Antigravity と Claude Code の行は
9 月 26 日に、1.14.0 とともに公開された、より短い版
（600 行、インラインコード 257 個、表 85 行）で測定しました。また、API 経由の Claude
Sonnet 5.5、Haiku 5.5、Haiku 4.5 の行は、10 月 18 日に
同じ版で測定しました。「情報密度の高い情報収集記事」列は、
9 月 4 日と 5 日に行った、589 行の記事による測定の結果です。ただし、Grok の行は
9 月 9 日に同じ情報収集記事の別の版で再測定し、Antigravity と
Claude Code の行は 9 月 26 日に同じ記事で測定、前述の Claude の 3 行は
10 月 18 日に測定しました。完全な表、所要時間、測定手順は
[詳細な測定結果](#詳細な測定結果)に記載しています。
## すべてのオプション

| オプション                   | 説明                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 翻訳する単一の Markdown ファイル（`--source_dir` の代替）                                             |
| `--source_dir`           | Markdown ファイルを含む入力ディレクトリ（デフォルト: `content/posts`）                                   |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ（デフォルト: `traductions_en`）                                    |
| `--source_lang`          | 翻訳元の言語（デフォルト: `fr`）                                                                                  |
| `--target_lang`          | 翻訳先の言語（デフォルト: `en`）                                                                                   |
| `--model`                | 使用する特定のモデル                                                                                  |
| `--eco`                  | 低コストのモデルを使用                                                                              |
| `--use_mistral`          | Mistral AI API を使用                                                                                     |
| `--use_claude`           | Claude API を使用                                                                                         |
| `--use_gemini`           | Gemini API を使用                                                                                         |
| `--use_grok`             | xAI（Grok）API を使用 — `XAI_API_KEY` が必要                                                           |
| `--use_codex`            | ChatGPT サブスクリプションの利用枠で Codex CLI を使用                                                    |
| `--use_grok_cli`         | Grok サブスクリプションの利用枠で Grok CLI を使用                                                        |
| `--use_antigravity`      | Google AI Pro または Ultra サブスクリプションの利用枠で Antigravity CLI（`agy`）を使用                       |
| `--use_claude_code`      | Claude Pro または Max サブスクリプションの利用枠で Claude Code CLI（`claude -p`）を使用                      |
| `--use_opencode`         | OpenCode で設定されたプロバイダーに接続して OpenCode（オープンソース）を使用；`--model provider/modèle` が必要 |
| `--use_openrouter`       | OpenRouter を使用 — `OPENROUTER_API_KEY` と `--model fournisseur/modèle` が必要                          |
| `--force`                | 再翻訳を強制                                                                                       |
| `--keep_filename`        | 元のファイル名を維持                                                                          |
| `--news`                 | ニュースモード：英語の引用を保護し、言語ごとのフラグを管理                                      |
| `--add_translation_note` | 翻訳注記を追加                                                                                |
| `--note_position`        | 注記の位置：`top`、`bottom`（デフォルト）、または `both`                                                     |
| `--note_format`          | 注記の形式：`legacy`（デフォルト、太字の段落）または `marker`                                            |
| `--include_model`        | 出力ファイルにモデル名を含める                                                            |
| `--reasoning_effort`     | GPT-5.x の推論労力：`none`/`low`/`medium`/`high`/`xhigh`                                         |

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

| プロバイダー    | 高品質（デフォルト）                                                     | 低コスト（`--eco`）      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol`（`--model` により `gpt-5.6-sol`、`terra`、`luna` も使用可能） | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | 同じ — `--eco` は効果なし |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`、推論労力 `low`                                               | 同じ — `--eco` は効果なし |
| OpenCode    | `--model provider/modèle` が必須                                | 同じ — `--eco` は効果なし |
| OpenRouter  | `--model fournisseur/modèle` が必須                             | 同じ — `--eco` は効果なし |

### ChatGPT サブスクリプション経由：`--use_codex`

公式の Codex CLI を操作します。翻訳は ChatGPT サブスクリプションの
利用枠から差し引かれ、API キーも従量課金も不要です。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- 実行ファイルは `CODEX_BIN`、次に `PATH`、最後にパッケージ
  `openai-codex-cli-bin` の順に検索されます。`~/.codex/auth.json` は読み込まれません。
- `OPENAI_API_KEY` と `CODEX_API_KEY` は子プロセスの
  環境から除去されます。キーが存在しても API に切り替わることはありません。
- 各セグメントは、5 時間の利用枠で少なくとも 1「メッセージ」を消費します。
  検証に失敗して再試行すると 2 メッセージになります。OpenAI が示す
  推定値では、Plus プランで `gpt-5.6-luna`（`--eco`）は 5 時間あたり 250-2 000 メッセージ、
  `gpt-5.6-sol` は 10-100 メッセージです。
- 1.16.3 までのデフォルトだった `--model gpt-5.6-sol`、`--model gpt-5.6-terra`、
  `--model gpt-5.6-luna` もサブスクリプション経由で利用できます。
- サーバーから 429 が返ってもファイルは失われません。Codex は自動で再接続し、
  aipmt はターンの終了を待ちます。最終的に 429 が解消しなければ、セグメントは
  30 秒後、次に 60 秒後に再試行されます。アカウントに利用権限のないモデルでは、
  「ChatGPT アカウントで Codex を使用する場合、このモデルはサポートされていません」という 400 エラーが返されます。
- API より遅く、文書が長くなるほど差が広がります。この README では、
  `gpt-5.6-sol` の言語あたりの中央値が 6 分 46 秒だったのに対し、
  `gemini-3.7-flash` は 36 秒でした。
- CI では拒否されます（`CI` または `GITHUB_ACTIONS` が設定されている場合）。
  サブスクリプションの認証には個人のセッションファイルを使うため、
  共有ランナーに置くべきではありません。
- 変数：`CODEX_BIN`、`CODEX_TIMEOUT`（セグメントあたりの秒数、デフォルト 600）。

### Grok サブスクリプション経由：`--use_grok_cli`

公式の Grok Build CLI を使い、SuperGrok または
X Premium+ サブスクリプションで同様に動作します。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Codex より隔離が弱くなります。** Grok の OS サンドボックスは
  最近の多くの Linux 環境で適用できず（AppArmor、コンテナーランタイムの
  ソケット）、適用できないプロファイルを指定すると、通知なしで隔離されずに起動します。
  そのため、スクリプトはデフォルトではプロファイルを要求せず、その旨を表示し、
  CLI の `--deny` ルールに依存します。すべてに一致する `*` もその一つで、
  これは保護を黙って解除する代わりに起動を拒否する唯一の層です。
  `GROK_TRANSLATE_SANDBOX=read-only` は OS サンドボックスを必須とし、
  マシンが対応できなければ起動に失敗します。
- 利用枠は週単位で、Chat、Imagine、Voice と共有されます。
  残量を確認するコマンドはないため、バッチ処理が通知なしに会話用の利用枠を
  消費することがあります。
- 変数：`GROK_BIN`、`GROK_HOME`（CLI のディレクトリ、デフォルト `~/.grok`）、
  `GROK_TIMEOUT`（デフォルト 900）、`GROK_TRANSLATE_SANDBOX`。

### Google サブスクリプション経由：`--use_antigravity`

公式の Antigravity CLI である `agy` を使い、同様に動作します。Google
AI Pro または Ultra の契約者は、トークン単位で課金される代わりに、
サブスクリプションの利用枠から翻訳分が差し引かれます。この利用枠を使う経路はこれだけです。
Gemini CLI は 2026 年 6 月 18 日以降、これらのアカウントに対応しておらず
（[告知](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)）、
Antigravity SDK は API キーまたは Google Cloud プロジェクトしか受け付けません。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **有料の経路はすべて閉じられます。** agy に渡される環境変数は、
  `PATH`、言語とタイムゾーン、ターミナル、ユーザー情報、プロキシと証明書、
  セッションバスという限定された一覧だけで、キーは一切渡されません。
  複数の環境変数が通知なしに呼び出し先を切り替えるためです。実測では、
  ある変数は文書を第三者のゲートウェイへ送り、別の変数は課金対象の
  Google Cloud プロジェクトへ送ります。拒否リスト方式では、見直すたびに漏れが見つかりました。
  各セグメントの処理前に、利用枠を消費しない `agy -p /config` で、
  有料の AI クレジットが無効であり、API キーも Google Cloud プロジェクトもないことを
  確認する必要があります。設定が存在しない場合も拒否され、確認できなければ翻訳は行われません。
  さらに各呼び出しのログでサブスクリプションの利用（`authMethod=consumer`）を
  確認できなければ、応答は拒否されます。
- **隔離。** 各呼び出しは、非公開の使い捨てホームディレクトリ内で、
  ツールを持たない翻訳エージェントを使って実行されます。利用者の agy の設定、ルール、
  プラグイン、MCP サーバー、フックは引き継がれず、履歴にも何も追加されません。
  認証情報はキーリング内にとどまり、aipmt が読み取ることはありません。
  指定したエージェントが見つからないと、agy は通知なしにコーディングエージェントと
  そのツールへ切り替わります。そのため、ログの完全な 1 行で正しいエージェントを確認する必要があります。
  文書内にそのメッセージが引用されていても代わりにはならず、確認できなければ拒否されます。
- **プラットフォーム**：キーリングを備えたセッション（D-Bus セッションバス、
  Secret Service）上の Linux。macOS も受け付けますが、実測はしていません。
  Windows では各呼び出しを隔離する環境変数を agy が読み取らないため拒否されます。
  セッションバスのない Linux（SSH セッション、コンテナー、サーバー）でも拒否されます。
  これらの環境では agy がトークンを `~/.gemini` 内のファイルに保存しますが、
  隔離によってそのファイルが見えなくなるためです。ログインコードを 1 分間待たせる代わりに、
  起動前に理由を示して拒否します。
- **モデル**：`agy models` のモデルを使用します。Gemini は名前に推論労力を含みます
  （`gemini-3.8-flash-medium` など）。接尾辞のない名前は呼び出し前に拒否され、
  `--reasoning_effort` は効果がありません。デフォルトは `gemini-3.8-flash-medium`、
  `--eco` では `gemini-3.7-flash-low` です。これらを決めるための一連の測定は、
  [詳細な測定結果](#詳細な測定結果)で説明しています。Claude と GPT-OSS には
  独自の、はるかに小さい利用枠があります。実測では、呼び出し 1 回あたり 5 時間枠の約 1 % を
  消費するのに対し、Flash は 0.05 % です。
- **利用枠**：グループごとに 5 時間枠と週間枠があり、
  トークンのコストに応じて消費されます。著者のアカウントでの実測では、原文 100 万文字あたり、
  5 時間枠を `gemini-3.8-flash-medium` で約 16 ポイント、
  `gemini-3.7-flash-medium` で 14 ポイント、低い推論労力で 7〜8 ポイント消費します。
  したがって、40 000 文字の README は半ポイント強を消費します。
  週間の上限はプランによって異なります。再試行は agy が再試行可能と示した場合に従います。
  そうでなければ、利用枠を使い切った状態で再試行することはありません。
  `/usage` が示すリセット時刻まで、各ファイルの処理が失敗します。
- **API より低速**：測定に使った情報密度の高い記事では、言語あたりの中央値が
  `gemini-3.8-flash-medium` で 3 分 59 秒、
  `gemini-3.7-flash-medium` で 3 分 14 秒だったのに対し、API 経由の Gemini 3.7 Flash は 1 分 18 秒でした。
- **中断**：Ctrl-C またはターミナルを閉じると、agy もコマンドとともに停止し、
  利用枠を消費しながらターンを完了することはありません。Codex、Grok CLI、OpenCode も同様です。
  `nohup` では翻訳が続行されます。
- CI では拒否されます（`CI` または `GITHUB_ACTIONS` が設定されている場合）。
  認証情報が個人のキーリング内にあるためです。ランナーでは `--use_gemini` と `GOOGLE_API_KEY` を使用してください。
- 変数：`AGY_BIN`（なければ `PATH`、次に `~/.local/bin/agy`）、
  `AGY_TIMEOUT`（起動を含むセグメントあたりの秒数、デフォルト 900）。

**利用規約：責任を負うのはご自身のアカウントです。**
[Antigravity の利用規約](https://antigravity.google/terms)（第 6 条）と
[よくある質問](https://antigravity.google/docs/faq/)では、Antigravity の認証情報を使って
第三者のソフトウェアからサービスへアクセスすることを禁じています。Claude Code、
OpenClaw、OpenCode が例として挙げられており、違反するとアカウントが停止される可能性があります。
aipmt はトークンを読み取ったり再利用したりせず、Google がスクリプトと CI 向けに
説明している[ヘッドレスモード](https://antigravity.google/docs/cli/headless/)で
公式の実行ファイルを起動します。Google の関係者は、自分の作業のためにローカルスクリプトから
`agy -p` を起動することを「標準的」としています
（[公式フォーラム、2026 年 9 月 25 日、契約上の効力を持たない回答](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）。
ただし、このように配布されるツールの場合を明確に判断する記述はありません。

**公開文書のみを対象にしてください。** 同じ利用規約の第 5 条によると、
やり取り（プロンプト、応答、メタデータ）は、Google の製品や
機械学習の改善に利用され、人間によって確認される場合があります。
これは有料サブスクリプションでも同じです。利用を拒否するには
`enableTelemetry` の設定が必要ですが、その効果は文書化されておらず、aipmt は設定しません。
隔離環境には利用者の agy の設定が引き継がれません。機密情報は一切送信しないでください。
### Claude のサブスクリプションで利用：`--use_claude_code`

Claude Code の公式 CLI である `claude` を `-p` モードで使う場合も同じ仕組みです。
Claude Pro または Max の契約者は、翻訳がトークン単位で課金される代わりに、
サブスクリプションの利用枠から差し引かれます。
従量課金の Anthropic API である `--use_claude` とは異なります。

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **従量課金につながる経路はすべて閉じられ、各呼び出しでそれが確認されます。** Claude
  Code に渡される環境変数は、明示的に許可されたものだけです。API キー、
  トークン、クラウドプロバイダーの設定、aipmt の起動元となる Claude Code
  セッションの識別情報は渡されません。最初のセグメントの前に、`claude auth status` が
  Console キーを使わないサブスクリプション接続を示し、利用枠を消費しない `/usage` が
  それを確認する必要があります。各呼び出しも初期化イベントで同じことを確認し、確認できなければ応答は拒否されます。
- **「追加使用」を無効にしてください**（claude.ai の設定 → 使用量）。
  費用をゼロユーロに保つためです。有効だと、期間内の利用枠を使い切った際に
  自動的に切り替わり、エラーを表示せず課金されます。aipmt は呼び出しの利用枠レポートで
  それを検出すると翻訳を停止しますが、その呼び出し分はすでに計上されています。
- **利用枠は Claude Code のセッションと共有されます。** 各呼び出しは
  5 時間枠と週間枠の使用量を報告します。80 % を超えると
  （`AIPMT_CLAUDE_MAX_UTILIZATION`）、仕事で使う枠を使い切らないよう、
  次のセグメントを開始しません。
- **隔離。** 各呼び出しはツールなしで、専用の使い捨てディレクトリ内で
  カスタマイズを無効にして実行されます。`CLAUDE.md`、プラグイン、
  フック、MCP サーバー、設定は読み込まれず、セッションの情報も保存されません。
  添付ファイルも無効です。文書内の `@chemin` は
  テキストのままで、ファイルを開きません（実測済み）。
- **モデル**：既定は `sonnet`、推論の強度は `low` で、`--eco` でも同じです。
  この経路では `--eco` を指定しても変わりません。同じ文書で測定したところ、`haiku` は
  処理時間が 2 倍でした。推論を止めることができず、
  費用の低下もわずかです。また、`opus` は生物学関連の内容を拒否します（次項）。
  どちらも `--model` から利用できます。これらのエイリアスは、
  各系統の最新モデルを指します。`fable` と `[1m]` の各種は、
  有料クレジットを使うため拒否されます。`--reasoning_effort` は推論の強度を設定しますが、
  翻訳には効果がなく、実測した推論量はゼロかほぼゼロです。
- **Opus は生物学関連の一部の内容を拒否します。** 安全措置が
  Sonnet より厳しく、Anthropic のエラーメッセージでも
  「生物学研究に関連する作業が検出対象になることがある」と説明されています。実測では、
  生成された 279 個の分子についての短報が原因で、記事全体が 14 言語すべてで拒否されました。
  ファイルは書き込まれません。aipmt は途中で切れた応答を拒否し、安全措置が原因であることを示して、
  `--model sonnet` を勧めます。
- CI（`CI` または `GITHUB_ACTIONS` が定義されている場合）と Windows（未測定）では拒否されます。
- 変数：`AIPMT_CLAUDE_BIN`（未指定なら `PATH`、次に `~/.local/bin/claude`）、
  `AIPMT_CLAUDE_TIMEOUT`（セグメントあたりの秒数、既定値 900）、
  `AIPMT_CLAUDE_MAX_UTILIZATION`（既定値 0.8）、`CLAUDE_CONFIG_DIR`（Claude Code のアカウント。
  プロジェクトの `.env` からは取得しません）。作業ディレクトリは
  `XDG_CACHE_HOME/aipmt/claude-code` 配下です（既定値 `~/.cache`）。

**利用規約：利用責任はアカウント所有者にあります。**
[Claude Code の法的事項ページ](https://code.claude.com/docs/en/legal-and-compliance)
は、「エンドユーザーが、自分の Claude サブスクリプションを使って、変更されていない Claude Code バイナリに
ログインすること」を妨げていません。aipmt はまさにこの方法を使い、
公式バイナリを起動し、トークンを読み取ることはありません。ただし Anthropic は、
「サードパーティーの開発者が［…］ユーザーに代わって Free、Pro、Max プランの認証情報で
リクエストを中継することを認めていない」とし、「オープンソースのプロジェクトを含む」
外部ツールには API キーの使用を推奨しています。また、その利用分を
有料クレジットから差し引く権利を留保しています
（[Claude ヘルプ](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)）。
配布されるツールがバイナリを起動する場合について、明確に判断できる規定はありません。

**データ**：Free、Pro、Max のアカウントでは、プライバシー設定で許可されている場合、
Claude Code の内容もモデルの学習に使われます
（[データに関するページ](https://code.claude.com/docs/en/data-usage)）。aipmt は
ローカルに会話記録を保存しません（`--no-session-persistence`）。機密情報は
入力しないでください。

### 好みのプロバイダーへ：`--use_opencode`

[OpenCode](https://opencode.ai) はオープンソース（MIT）のコーディングエージェントで、
内部で設定されたプロバイダーにリクエストを振り分けます。API キー、サブスクリプション、
OpenCode Zen ゲートウェイ（アカウント不要の無料モデル）、ローカルモデルが利用できます。
ここでは Zen と Ollama の 2 経路を、最初から最後まで実測しました。

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

`--model` は必須です。指定しないと、OpenCode はやり取りが学習に使われる可能性のある
無料モデルに切り替わります。その選択を利用者に代わって行うことはありません。

各呼び出しの隔離：

- 利用者の設定より優先されるインライン設定で、すべてのツールを拒否する
  エージェント `aipmt` を定義します（`permission: { "*": "deny" }`）。セッション共有は
  無効にし、`--pure` を使い、`--auto` は使いません。
- 空の使い捨て作業ディレクトリを使い、`OPENCODE_DISABLE_PROJECT_CONFIG` と
  `OPENCODE_DISABLE_CLAUDE_CODE` を設定します。これらがないと、OpenCode は
  現在のディレクトリの `AGENTS.md` と `~/.claude/CLAUDE.md` をプロンプトに挿入します。
  グローバルの `~/.config/opencode/AGENTS.md` は引き続き挿入されます。OpenCode には
  これを除外する方法がありません。
- 出力の条件：終了コードが 0、`error` イベントがないこと、ツール呼び出しが
  ないこと、最後のステップが `stop` であること、テキストが空でないこと、
  エージェント `aipmt` が実際に読み込まれていることです。未知の `--agent` を指定しても
  OpenCode は失敗せず、黙ってコーディングエージェントに切り替わります。
- `aipmt` のキーは渡しません。ただし OpenCode 自体のキーである
  `OPENCODE_API_KEY` は例外です。プロバイダーは OpenCode 内で設定し、
  `aipmt` の `.env` では設定しません。

留意点：

- Zen の無料モデルは随時変わり、制限は文書化されていません。また、
  やり取りが学習に使われる可能性があります。公開文書向けであり、
  非公開の内容には適していません。
- セグメントは最大 16 000 文字になるため、ローカルモデルには少なくとも 16 k トークンの
  コンテキストが必要です。Ollama では 4 096 に設定されていることが多いため、
  `PARAMETER num_ctx 32768` を指定した `Modelfile` を使ってください。
- `--eco` は無効です。`--reasoning_effort` は OpenCode の
  `--variant` としてそのまま渡されます。
- OpenCode は各セッションを `~/.local/share/opencode/` に記録します。
- 変数：`OPENCODE_BIN`（未指定なら `PATH`、次に `~/.opencode/bin/opencode`）、
  `OPENCODE_TIMEOUT`（セグメントあたりの秒数、既定値 600）。`OPENCODE_CONFIG` は
  そのまま OpenCode に渡されます。

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

`reasoningEffort: "none"` は、これらのモデルに対して Ollama が既定で有効にする推論を
無効にします。この推論は Modelfile では無効にできません。6 単語の文で
測定したところ、このオプションなしでは推論に 919 トークン、68 秒かかり、指定すると 9 トークンでした。

### 400 以上のモデルへ：`--use_openrouter`

OpenRouter は、共通のクレジット残高から従量課金されるルーターで、
外部事業者がホストするモデルへ接続します。ここで扱う他のプロバイダーでは
提供されていない中国のオープンモデルも含まれます。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` は必須です。課金が発生する前に事前確認を行い、
ルーティングに特有の 2 つの点に対処します。

- **同じモデルが、上限の異なる数十のホスティング事業者から提供されます**
  — `z-ai/glm-5.3-flash` では 23 社あり、そのうち 1 社の出力上限は
  2 048 トークンです。事前確認では `/api/v1/models/{modèle}/endpoints` を読み取り、
  出力上限が 8 000 トークン未満の事業者や稼働状況が低下している事業者を除外し、
  残りを `allow_fallbacks: false` で固定します。
- **推論は出力と同じ単価で課金されます** — `z-ai/glm-5.2` の
  「OK」という応答では、2 トークンに対して 107 トークンでした。推論は既定で無効です。
  推論が必須のモデルには、受け付ける最も低い強度を指定します。カタログの既定値では、
  翻訳が終わる前に出力上限を使い切る可能性があります。
  `--reasoning_effort` の指定が優先されます。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- コンテキストウィンドウはカタログから取得します。16 400 トークン未満のモデルは
  呼び出し前に拒否されます。プロンプトとセグメントに 8 400、
  出力に最低 8 000 トークンが必要です。
- カタログにないスラッグ、カタログへの接続不能、必要な上限を満たす
  ホスティング事業者がない場合は、コマンドを停止します。
- `finish_reason=length` で出力が空の場合は、推論が予算を使い切ったことを示し、
  途中切断ではありません。メッセージではこの違いを明示します。
- `--eco` は無効です。
- 変数：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>）、
  `OPENROUTER_BASE_URL`（既定値 `https://openrouter.ai/api/v1`、`https://`
  必須）、`OPENROUTER_TIMEOUT`（既定値 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`
  （既定値 30）。

### 翻訳注記

`--add_translation_note` は、`bottom`（既定）、`top`（フロントマターの
後）、または `both`（`--note_position`）に注記を追加します。形式は `legacy`（太字の
段落、既定）または `marker`（`--note_format`）です。`marker` 形式は、
表示されない Markdown の参照定義
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`
に続けて、太字の引用を置きます。GitHub 上で読めるほか、ビルド時に
remark プラグインで利用できます。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 詳細な測定結果

測定はすべて、`aipmt` を使って実際に翻訳を実行したもので、対象は
14 言語です：en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi。
**書き込み済み**は検証を通過したファイル数、**差異なし**は
`scripts/compare_structure.py` が何も検出しなかったファイル数です。セクション、見出し、リンク、
異なる URL、コードブロック、インラインコード、表の行、
引用ブロック、太字の語句の数が一致しています。

「差異なし」は「何も検出されなかった」という意味で、「同一」という意味ではありません。
比較ツールは内容を読まず、要素の数を数えます。レベル 4 の見出しの削除、
インラインコードの内容の置き換え、旗の差し替え、閉じ括弧が 1 つ多いために
どこにも移動できなくなった内部リンク
`[texte]((#ancre))` は検出しません。また、言語の判定もしません。

### 情報量の多い動向記事、`--news` モード

[jls42.org の AI 動向記事](https://jls42.org/fr/news)の 1 回分：
589 行、140 リンク、21 セクション、保護された英語の引用 3 件。
2026 年 9 月 4 日と 5 日に測定しました。

| モデル                                          | 利用経路              | 書き込み済み | 差異なし   | 言語あたりの中央値 |
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

Grok は 9 月 9 日、同じ動向記事の別の回
（356 行）で再測定しました。14 言語中 9 言語を書き込み、8 言語で差異がありませんでした。
冒頭の表には、この数値を載せています。途中で中断した 3 回の測定は
掲載していません。`qwen3.5-27b`（9 言語）と `kimi-k2.6`（4 言語）はクレジット不足、
`z-ai/glm-5.3-flash` は推論設定が原因で 2 回失敗しましたが、
その設定は以後プロバイダー側で修正されています。OpenRouter の各行は、
`--use_openrouter` の導入前に、ルーターの既定設定で測定しました。`z-ai/glm-5.2` は
提供されるプロバイダー実装で再測定しても、同じ 14/14 でした。数値は
9 月 10 日に現在の比較ツールで再計算しました。`qwen3.8-flash` と
`qwen3.7-flash` は初回公開時よりそれぞれ 1 言語増え、ほかは
変わっていません。

`--use_antigravity` の各行は、9 月 26 日に同じ記事で、
4 件の翻訳を並列実行して測定しました。`gemini-3.7-flash-medium` は午前、
`gemini-3.8-flash-medium` は午後です。英語では、どちらも引用の下にある
フランス語訳 3 行を自ら削除し、旗を勝手に追加せず、
英語の引用もそのまま保持しました。補助の除去処理は何もする必要が
ありませんでした。`--eco`（`gemini-3.7-flash-low`）では、4 言語のみ
（en、ja、ar、hi）で測定し、4 言語中 4 言語を書き込み、すべて差異なし、中央値は
1 min 52 s でした。同日、より新しい 9 月 25 日の動向記事
（438 行、英語の引用 2 件）でも確認しました。ブログ外で
`gemini-3.7-flash-medium` により翻訳したところ、14 言語中 14 言語を書き込み、
すべて差異なし、言語あたり 87～128 s でした。

`--use_claude_code` の各行は、9 月 26 日に同じ記事で、
4 件の翻訳を並列実行し、推論の強度を `low` にして測定しました。`sonnet` では、
14 言語すべてで英語の引用がそのまま保持され、英語では
モデル自身がフランス語訳の行を削除し、旗を勝手に追加しませんでした。
`opus` はどの言語も書き込めませんでした。すべての言語で、
結合部位向けに生成された 279 個の分子についての短報が原因となり、
安全措置によって最後のセグメントで応答が止まりました。この短報を単独で送っても、
「生物学」カテゴリとして拒否されます。`sonnet` はすべての言語で翻訳できました。`haiku` は
14 言語を書き込みましたが、3 言語（en、pl、ro）でセクション見出しが
レベル 2 からレベル 1 に変わりました。推論を止めることができず、出力トークンの
61 % を推論が占めたため、`sonnet` の 2 倍以上の時間がかかりました。

`claude-sonnet-5-5`、`claude-haiku-5-5`、`claude-haiku-4-5` の各行は、
10 月 18 日に Anthropic API を通じ、同じ記事で、
モデルごとに 4 件の翻訳を並列実行して測定しました。Sonnet 5.5 は推論の無効化を
受け付けません。aipmt は受け付ける最も低い設定を送り、
応答には推論が含まれていませんでした。セグメントの再処理なしで、14 言語すべてを
差異なく書き込みました。英語では、フランス語訳の行を自ら削除し、
旗を勝手に追加せず、すべての言語で英語の引用を
そのまま保持しました。Haiku 5.5 は適応型推論を使って測定しました。推論を
無効にすると、段落全体がフランス語のまま残り、検証で拒否されました。
書き込めたのは 14 言語中 3 言語です。2 つの Haiku は同じ短報でつまずきました。Haiku 5.5 は
日本語、韓国語、中国語で見出しのレベルを変えるか見出しを重複させ、
Haiku 4.5 は 7 言語でレベル 1 に変え、日本語では
フランス語のまま残しました。2 文書を 14 言語に翻訳した費用は、Haiku 4.5 が
3,67 $、Haiku 5.5 が 0,57 $、Sonnet 5.5 が 9,21 $ でした。
### このプロジェクトのREADME、標準Markdown

2026年9月9日に固定した版：785行、285個のインラインコード、40個の
ブロック終端、89行の表。4件の翻訳を並列実行。

| モデル                                          | 出力数 | 差異なし | 言語ごとの中央値 | 差異の内容                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | なし                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | なし                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | 比較ツールでは差異なし；内部リンクが二重化（en）                   |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | なし                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | なし                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | 太字の単語1個（ja）                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | 太字の単語1個（ko）                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | 表の1行が前の行と連結（ar）                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | リンク1個（sv）、太字の単語1個（zh）                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | 太字の単語1個（ar, ja）                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | 太字の単語1個（hi, ja, ko）                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | アラビア語でインラインコード40個が追加；太字（hi, ja, ko）                   |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2言語を却下（ar, hi）：返された出力でインラインコードが欠落        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | セクション1個が欠落（ar, hi, ko）；コードブロックが追加（ja, ko, ro, zh） |

中断した2回の測定は集計に含めていません。Grokは12言語の完了後にCLIセッションが期限切れとなり
（うち11言語は差異なし）、`qwen3.8-flash`は2言語の完了後に
ホスティング提供元からHTTP 429が返されました。`opencode/mimo-v2.5-free`と`ollama/gpt-oss-20b-32k`は
この版では再測定していません。277行短い9月4日と5日の版では、
それぞれ14件中9件の翻訳を出力し、差異がなかったのはそれぞれ7件と
1件でした。

`--use_antigravity`と`--use_claude_code`の行は、
固定した版ではなく、9月26日に1.14.0とともに公開された版で測定しました。
`claude-sonnet-5-5`、`claude-haiku-5-5`、`claude-haiku-4-5`の行も10月18日に
同じ版で測定しています。600行、257個のインラインコード、30個のブロック終端、85行の
表です。こちらは
185行短いため、ほかの行とは条件をそろえて比較できませんが、
これらの行同士は比較できます。比較ツールが
検査しない内部リンクについては、`gemini-3.8-flash-medium`は
14言語すべてで保持し、`gemini-3.7-flash-medium`はイタリア語で壊しました。
`sonnet`と`opus`はすべての言語で保持し、`haiku`は
英語で二重化しました。`claude-sonnet-5-5`と`claude-haiku-4-5`は
14言語すべてで保持し、`claude-haiku-5-5`は出力した12言語で保持しました。

### 著名なプロジェクトのREADME 4件

FastAPI、Ollama、tldr-pages、Vue.jsをGitHubからそのまま取得しました。
前の2件よりも簡単な文書です。この測定は
苦戦しているモデルを対象とし、Geminiを比較の基準にしています。

| モデル                    | 対象範囲                  | 出力数 | 差異なし   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4プロジェクト × 14言語     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4プロジェクト × 14言語     | 55/56   | ❌ 47/56     |
| `grok-4.6`（サブスクリプション）   | 4プロジェクト × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4プロジェクト × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### これらの測定の限界

- **網羅的なランキングではありません**：OpenRouterだけでも400を超える
  モデルがありますが、測定したのは15程度です。
- **所要時間は目安です**：測定ごとに3～6件の翻訳を並列実行しており、
  提供元の処理速度も時間帯によって変動します。
- **特定時点での観測です**：同じ名前でもモデルは変化し、皆さんの
  文書と私たちの文書は異なります。

ご自身の文書で測定を再現するには、内容を固定したファイルのコピーを使います。

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

この2行は両方とも必要です。`pip install -e .`がないと、`python -m aipmt`は
`No module named aipmt`と応答します。

品質管理ツールの導入は任意ですが、推奨します。

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

リポジトリ内の28件の翻訳（READMEとCHANGELOG、14言語）は
`./regen_translations.sh --force`で再生成できます。既定ではChatGPTのサブスクリプションで
Codexと`gpt-6.1-sol`を使用し、4件を並列実行します。`REGEN_PROVIDER`と
`REGEN_MODEL`で利用経路を変更できます。`antigravity`はGoogleの
サブスクリプションを引き続き使用するため、例外指定なしで実行できます。従量課金のAPI（`openai`、`gemini`、
`grok`、`openrouter`）は`REGEN_ALLOW_PAID_API=1`がなければ拒否されます。
`REGEN_JOB_TIMEOUT`は各ジョブの実行時間に上限を設けます（600 s、Codexと
Antigravityでは1 800 s）。ツールの詳細は`CLAUDE.md`にあります。

## このスクリプトを利用しているプロジェクト

- **[jls42.org](https://jls42.org)** — 15言語で公開している個人ブログ。
  [毎日のAI動向](https://jls42.org/fr/news)はこのツールで毎日
  翻訳され、上記の測定で参照文書として使用されています。

## 著者

Julien LE SAUX
メール：contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE バージョン3。[ライセンス](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)を参照してください。

## 注意事項

このプログラムは、GPL v3の第15条および第16条の規定に従い、
**一切の保証なし**で配布されます。「現状のまま」提供され、商品性
または特定目的への適合性について保証せず、その使用に起因する損害について
著者は責任を負いません。ライセンス本文が
この要約に優先します。

- **公開前に読み直してください。** 保護の対象はコードブロック、
  インラインコード、URL、アンカー、および`--news`モードの引用です。
  見出し、表、フロントマター、文の意味は保護されません。
- **文書は選択した提供元に送信され**、その利用規約と
  データポリシーが適用されます。一部の無料モデルでは、
  やり取りが学習に再利用される場合があります。また、Antigravityの規約では、
  有料サブスクリプションを含め、Googleがやり取りを再利用し、人間による確認を行うことが
  認められています。マシンからデータを一切外部に出さない唯一の方法は、
  ローカルモデルを使用することです。
- **APIの呼び出しには料金が発生します。** このプログラムは
  支出に上限を設けません。長い文書、失敗後の再試行、推論量の多い
  モデルでは費用が増えます。
- **公開された測定結果は特定時点での観測であり**、保証ではありません。

記載されている製品名および会社名は、それぞれの権利者に帰属します。
このプロジェクトは、いずれとも提携していません。

**gpt-6.1-solでフランス語から日本語に翻訳された記事。**
