# AI搭載Markdown翻訳ツール

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 コード品質</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Quality Gate ステータス"></a>
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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="重複行 (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="技術的負債"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="コード行数"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy バッジ"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

コードブロック、インラインコード、URL、アンカー、テーブル、フロントマターなどの構造を保持したまま、Markdownファイルをある言語から別の言語へと翻訳します。モデルの呼び出し方法は11通り（5つのAPI、従量課金なしの4つのサブスクリプション、2つのルーター）あり、各モデルが実際に何を保持できるかの測定結果も公開しています。

## 概要

- **11種類のプロバイダーパス**：OpenAI、Mistral、Claude、Gemini、GrokのAPI、従量課金なしのChatGPT（Codex）、Grok、Google（Antigravity）、Claude（Claude Code）サブスクリプション、OpenCode（オープンソース、無料またはローカル）およびOpenRouter（400以上のモデル）ルーター。
- **トークンの欠落による破損なし**：コードブロック、インラインコード、URL、アンカー、引用は呼び出し前にトークンへ置き換えられ、戻り時に検証されます。1つでも欠落している場合、ファイルは書き込まれません。
- **長文ドキュメント**：モデルのコンテキストウィンドウに応じた自動分割。
- **`--news`モード**：英語の引用を保護し、言語ごとに国旗を管理。技術ウォッチ記事向け。
- **`--eco`モード**：高速で安価なモデルを使用。
- **オプションの翻訳注記**：上部、下部、またはその両方に配置可能。

## インストール

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11以降。リポジトリからのインストールについては、[貢献](#コントリビューション)を参照してください。

## 設定

キーは優先度の高い順に3つの場所から読み取られ、先行する場所で設定されていない値のみが後続の場所で補完されます。

|     | 場所                                          | 用途                                  |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 環境変数                                       | CI、コンテナ、一時的な上書き          |
| 2   | カレントディレクトリ（または親）の `.env` | プロジェクト固有のキー                |
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

`GOOGLE_API_KEY` の代わりに `GEMINI_API_KEY` も受け入れられます。ユーザーファイルは `XDG_CONFIG_HOME`（絶対パスのみ）に従い、Windowsでは `%APPDATA%` に従います。キーが見つからない場合、コマンドはこれら3つの場所を列挙します。

**プロジェクトの `.env` は、呼び出し先をリダイレクトしたり実行するプログラムを選択したりすることはできません。** キーを提供するのみで、送信先やバイナリを指定することは決してありません。`_BASE_URL`、`_API_BASE`、`_ENDPOINT`、`_BIN`（`CODEX_BIN`、`GROK_BIN`、`OPENCODE_BIN`、`AGY_BIN`）、`GROK_HOME`、プロキシ（`HTTP_PROXY`、`HTTPS_PROXY`、`ALL_PROXY`）、証明書ストア（`SSL_CERT_FILE`、`SSL_CERT_DIR`、`REQUESTS_CA_BUNDLE`、`CURL_CA_BUNDLE`）、および `XDG_CONFIG_HOME` / `APPDATA` で始まる変数はすべて無視され、警告が表示されます。クローンしたリポジトリがキーを傍受したり、初回翻訳時に独自のプログラムを実行させたりするのを防ぐためです。また、このファイルは補間なしで読み取られるため、`NOM=${OPENAI_API_KEY}` によってキーがコピーされることもありません。これらの変数は環境変数または `~/.config/aipmt/.env` に設定してください。

オプションの変数：`XAI_BASE_URL`（デフォルト `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（呼び出しあたりの秒数、デフォルト 900）、`CODEX_BIN`、`CODEX_TIMEOUT`（デフォルト 600）、`GROK_BIN`、`GROK_HOME`（デフォルト `~/.grok`）、`GROK_TIMEOUT`（デフォルト 900）、`GROK_TRANSLATE_SANDBOX`、`AGY_BIN`、`AGY_TIMEOUT`（デフォルト 900）、`OPENCODE_BIN`、`OPENCODE_TIMEOUT`（デフォルト 600）、`OPENROUTER_BASE_URL`（`https://` 必須）、`OPENROUTER_TIMEOUT`（デフォルト 900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（デフォルト 30）。各変数の詳細は各プロバイダーのセクションで説明されています。

## はじめに

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` をスペイン語に翻訳すると、`--target_dir` 内に `document-es.md` が生成されます。`--include_model` を指定すると `document-es-gpt-6.1-terra.md` になります。元の名前を保持する `--keep_filename` を除き、拡張子は常に `.md` になります（`article.mdx` は `article-en.md` になります）。既存の翻訳は `--force` が指定されていない限りスキップされます。

終了コード：すべて成功またはスキップされた場合は `0`、失敗したファイルが残っている場合は `1`（標準エラー出力に一覧表示）、設定に問題がある場合は `2`。失敗したファイルが書き込まれることはありません。書き込み処理自体が失敗した場合でも、内容は一時ファイルに書き込まれてからリネームされます。再実行するだけで対応できます。

## どのモデルを選ぶべきか

2つの実際のドキュメントを使用し、各モデルで同一の14言語に翻訳して測定しました。**数値は、14言語中、翻訳が出力され、かつソースとの間に差異が一切生じなかった言語の数です。**

| モデル                | アクセス方法                      | 稠密な技術ウォッチ記事 | このREADME    | 差異の内容と該当言語数                                                                                                                                             |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | Googleサブスクリプション（Antigravity） | ✅ 14/14                | ✅ 14/14     | 両ドキュメントとも差異なし                                                                                                                                         |
| **Claude Sonnet 5.5** | Anthropic APIキー                 | ✅ 14/14                | ✅ 14/14     | 両ドキュメントとも差異なし                                                                                                                                         |
| **Gemini 3.7 Flash**  | Google APIキー                    | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語：太字が1単語増加（ja）                                                                                                                               |
| **Gemini 3.7 Flash**  | Googleサブスクリプション（Antigravity） | ✅ 14/14                | ⚠️ 13/14     | 14言語中1言語：太字が1単語減少（ko）                                                                                                                               |
| **GPT-5.6 Sol**       | ChatGPTサブスクリプションまたはOpenAIキー | ✅ 14/14                | ⚠️ 12/14     | 14言語中2言語：太字が1単語減少（ar、ja）                                                                                                                           |
| **GLM-5.2**           | OpenRouterキー                    | ✅ 14/14                | ⚠️ 11/14     | 14言語中3言語：太字が1単語減少（hi、ja、ko）                                                                                                                       |
| Claude Sonnet 5       | Claudeサブスクリプション（Claude Code） | ⚠️ 13/14                | ⚠️ 13/14     | 記事で14言語中1言語：太字が1単語増加（zh）、このREADMEで1言語：表の行が前の行と結合し表示上不可視に（ar）                                                        |
| Claude Haiku 4.5      | Claudeサブスクリプション（Claude Code） | ⚠️ 11/14                | ✅ 14/14     | 記事で3言語：セクション見出しがレベル1に変更（en、pl、ro）、このREADMEでは比較ツール上は差異なしだが内部リンクが英語で重複                                          |
| Claude Sonnet 5       | Anthropic APIキー                 | ⚠️ 11/14                | ⚠️ 12/14     | 記事で3言語：余分なコードブロックが出現（es、de、hi）、このREADMEで2言語：リンクのマークアップ脱落（sv）、太字が1単語（zh）                                       |
| Claude Haiku 4.5      | Anthropic APIキー                 | ⚠️ 7/14                 | ✅ 14/14     | 記事で7言語：セクション見出しがレベル1に変更（日本語ではフランス語のまま残存）、このREADMEでは差異なし                                                           |
| Claude Haiku 5.5      | Anthropic APIキー                 | ⚠️ 11/14                | ❌ 12/14     | 記事で3言語：セクション見出しのレベル変更または重複（ja、ko、zh）、このREADMEで2言語が拒絶、インラインコードの欠落（ar、hi）                                      |
| Qwen 3.7 Flash        | OpenRouterキー                    | ❌ 8/14                 | ⚠️ 10/14     | 記事で1言語が拒絶、他5言語で乖離、このREADMEで約40語が `code` 化（ar）                                                                                     |
| Grok 4.6              | Grokサブスクリプション            | ❌ 8/14                 | 評価なし     | 14言語中5言語が拒絶（インラインコードやURLの出力欠落による）、オランダ語は全面的に乖離                                                                            |
| GPT-OSS 20B           | ローカルモデル（Ollama）          | ❌ 7/14                 | 再測定なし   | 14言語中4言語が拒絶：フランス語の文章がそのまま残されガードにより停止                                                                                             |
| MiMo v2.5（無料）     | OpenCode Zen（アカウント不要）    | ❌ 11/14                | 再測定なし   | 1言語が拒絶、ポーランド語で1セクションが欠落                                                                                                                       |
| Mistral Large         | Mistral APIキー                   | ❌ 5/14                 | ❌ 1/14      | **セクション全体が消失**：記事で1言語（hi）、このREADMEで3言語（ar、hi、ko）、さらに記事で3言語が拒絶                                                             |
| DeepSeek V4 Flash     | OpenRouterキー                    | ❌ 3/14                 | 再測定なし   | 14言語中10言語が拒絶、言語あたり37分                                                                                                                              |
| Claude Opus 5.5       | Claudeサブスクリプション（Claude Code） | ❌ 0/14                 | ✅ 14/14     | 生物学の短い記事が原因でOpusのセーフガードにより記事は全14言語で拒絶、このREADMEでは差異なし                                                                      |

|     | 記号の意味                                                                                                                                                                            |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | 14言語すべてが翻訳され、ソースとの差異が一切ない                                                                                                                                      |
| ⚠️  | 14言語すべてが翻訳されたが、差異は**マークアップ**（太字の単語、`code`、角括弧を失ったリンクなど）に限られる。テキスト、URL、コードブロック、セクションの欠落はない          |
| ❌  | 少なくとも1言語で翻訳に失敗（ファイルが拒絶され書き込まれなかった）、**または**書き込まれたファイルでコンテンツが欠落している                                                      |

注意点：

- **拒絶された翻訳は、破損した翻訳ではありません。** 返却時にトークンが欠落している場合、ファイルは書き込まれず、その言語は拒絶としてカウントされます。これは記事翻訳時のGrokに発生したもので、5つの非ラテン文字体系において最初のセグメントから4つのインラインコードと3つのURLが失われました。
- **モデルは、たった1文を理由にドキュメント全体を拒絶することがあります。** Opus 5.5はこのREADMEを完全に翻訳しますが、技術ウォッチ記事は一切翻訳できませんでした。生物学の短い記事に対してセーフガードが作動し応答を停止したためです。ファイルは書き込まれず、aipmtがその理由を出力します。
- **この安全網は、見出し、表、フロントマター、本文のテキストを対象としていません。** セクションを削除してしまうモデルが出力した場合でも、ツールはそのままファイルを書き込みます（Mistralがこれに該当します）。これらの要素はトークンに置き換えられず、現在のガードでは検査されません。`scripts/compare_structure.py` は消失したセクションを検出しますが、事後チェックになります。
- **GrokはこのREADMEでのスコアがありません**：CLIセッションが12言語終了後に期限切れとなったためです（そのうち11言語は差異なし）。中断されたテストは評価対象外としています。
- **言語よりもドキュメントの密度が影響します。** Grokは一般的なREADMEでは持ちこたえますが、オランダ語を含め、リンクが多用された記事では脱落します。

日付と対象ドキュメント：「このREADME」列は、2026年9月9日に本ファイルの固定リビジョン（785行、インラインコード285個、表89行。以降修正あり）で測定されました。ただしAntigravityとClaude Codeの行は9月26日に1.14.0と共に公開された短いリビジョン（600行、インラインコード257個、表85行）で測定され、API経由のClaude Sonnet 5.5、Haiku 5.5、Haiku 4.5の行は10月18日に同一リビジョンで測定されました。「稠密な技術ウォッチ記事」列は、9月4日・5日に実施された589行の記事に対するテスト結果に基づきます。ただしGrokの行は9月9日に同ウォッチ記事の別版で再測定され、AntigravityおよびClaude Codeの行は9月26日に同じ記事で測定され、これらClaudeの3行は10月18日に測定されました。完全な表、所要時間、プロトコルについては[詳細な測定結果](#詳細な測定結果)を参照してください。

## すべてのオプション

| オプション               | 説明                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 翻訳する単一のMarkdownファイル（`--source_dir` の代替）                                                     |
| `--source_dir`           | Markdownファイルが含まれるソースディレクトリ（デフォルト: `content/posts`）                                   |
| `--target_dir`           | 翻訳後ファイルの出力先ディレクトリ（デフォルト: `traductions_en`）                                             |
| `--source_lang`          | ソース言語（デフォルト: `fr`）                                                                      |
| `--target_lang`          | ターゲット言語（デフォルト: `en`）                                                                  |
| `--model`                | 使用する特定のモデル                                                                                          |
| `--eco`                  | エコノミーモデルを使用する                                                                                    |
| `--use_mistral`          | Mistral AI APIを使用する                                                                                      |
| `--use_claude`           | Claude APIを使用する                                                                                          |
| `--use_gemini`           | Gemini APIを使用する                                                                                          |
| `--use_grok`             | xAI（Grok）APIを使用する — `XAI_API_KEY` が必要                                                              |
| `--use_codex`            | ChatGPTサブスクリプションのクォータ上でCodex CLIを使用する                                                    |
| `--use_grok_cli`         | Grokサブスクリプションのクォータ上でGrok CLIを使用する                                                        |
| `--use_antigravity`      | Google AI ProまたはUltraサブスクリプションのクォータ上でAntigravity CLI（`agy`）を使用する          |
| `--use_claude_code`      | Claude ProまたはMaxサブスクリプションのクォータ上でClaude Code CLI（`claude -p`）を使用する              |
| `--use_opencode`         | OpenCode（オープンソース）を使用し、OpenCode内で設定されたプロバイダーに送信する。`--model provider/modèle` が必須       |
| `--use_openrouter`       | OpenRouterを使用する — `OPENROUTER_API_KEY` および `--model fournisseur/modèle` が必要                                            |
| `--force`                | 強制的に再翻訳する                                                                                            |
| `--keep_filename`        | 元のファイル名を保持する                                                                                      |
| `--news`                 | ニュースモード：英語の引用を保護し、言語ごとのフラグを管理する                                                |
| `--add_translation_note` | 翻訳注記を追加する                                                                                            |
| `--note_position`        | 注記の位置：`top`、`bottom`（デフォルト）、または `both`                               |
| `--note_format`          | 注記の形式：`legacy`（デフォルト、太字落段）または `marker`                                     |
| `--include_model`        | 出力ファイルにモデル名を含める                                                                                |
| `--reasoning_effort`     | GPT-5.xの推論エフォート：`none`/`low`/`medium`/`high`/`xhigh`    |

9つの `--use_*` フラグは相互に排他的です。2つを同時に組み合わせることは
拒否されます。

## プロバイダー

### API経由：OpenAI、Mistral、Claude、Gemini、Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` は、各プロバイダーのエコノミープランに切り替えます。

| プロバイダー | 品質（デフォルト）                                                   | エコノミー（`--eco`）     |
| ------------ | -------------------------------------------------------------------- | --------------------------------- |
| OpenAI       | `gpt-6.1-terra`                                                      | `gpt-6-luna`                   |
| Claude       | `claude-sonnet-5-5`                                                      | `claude-haiku-5-5`                   |
| Mistral      | `mistral-large-latest`                                                      | `mistral-small-latest`                   |
| Gemini       | `gemini-4-hydrogen`                                                      | `gemini-3.1-flash-lite`                   |
| Codex        | `gpt-6.1-sol`（`--model` により `gpt-5.6-sol`、`terra`、`luna` も可） | `gpt-5.6-luna`                   |
| Grok API     | `grok-4.7`                                                      | `grok-4.3`                   |
| Grok CLI     | `grok-4.7`                                                      | 同様 — `--eco` は効果なし |
| Antigravity  | `gemini-3.8-flash-medium`                                                      | `gemini-3.8-flash-low`                   |
| Claude Code  | `sonnet`、エフォート `low`                          | 同様 — `--eco` は効果なし |
| OpenCode     | `--model provider/modèle` が必須                                               | 同様 — `--eco` は効果なし |
| OpenRouter   | `--model fournisseur/modèle` が必須                                               | 同様 — `--eco` は効果なし |

デフォルトは各プロバイダーの最新世代に追従しており、採用前に測定されています：OpenAIではGPT-6、GoogleではGemini 4 Hydrogen、xAIでは1.19.0以降のGrok 4.7です。以前のモデルも `--model`（`gpt-5.6-terra`、`gemini-3.8-flash`、`grok-4.6`…）で引き続き受け入れられており、GoogleのハイエンドであるGemini 4 ArgonやCarbonも同様です。aipmtはGPTおよびGrokの推論エフォートを独自に調整し、`--eco` では無効化され、`--reasoning_effort` で強制されます。Geminiは常に受け入れ可能な最低レベルを受け取ります。
Gemini APIの一時的な障害（503、429、タイムアウト）が発生した場合、10秒、20秒、40秒の間隔を空けて最大3回まで呼び出しが再試行されます。応答のない試行は5分で中止され、同様に再試行されます。サーバーが無応答の場合でも、無期限にブロックされることなく、最大20分程度でセグメントが失敗します。

### ChatGPTサブスクリプション経由：`--use_codex`

公式のCodex CLIを制御します。翻訳はAPIキーや従量課金なしで、ChatGPTサブスクリプションのクォータから差し引かれます。

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- バイナリは `CODEX_BIN`、次いで `PATH`、そして `openai-codex-cli-bin` パッケージから検索されます。`~/.codex/auth.json` が読み取られることはありません。
- `OPENAI_API_KEY` と `CODEX_API_KEY` はサブプロセスの環境から削除されます。キーが存在していてもAPIに切り替わることはありません。
- 各セグメントは5時間のウィンドウから少なくとも1「メッセージ」を消費します。検証に失敗して再試行された場合は2メッセージになります。OpenAIの公表値（推定）では、Plusプランの場合、`gpt-5.6-luna`（`--eco`）で250〜2,000メッセージ/5時間、`gpt-5.6-sol` で10〜100メッセージ/5時間です。
- 1.16.3までのデフォルトであった `--model gpt-5.6-sol`、ならびに `--model gpt-5.6-terra` と `--model gpt-5.6-luna` もサブスクリプション経由で動作します。
- サーバーから429が返されてもファイルが失われることはありません。Codexが自動的に再接続し、aipmtはターンの終了を待ちます。429が解消されない場合、セグメントは30秒後、次いで60秒後に再試行されます。アカウントに権限のないモデルの場合は、400「model is not supported when using Codex with a ChatGPT account」が返されます。
- APIよりも低速であり、ドキュメントが大きくなるにつれてその差は広がります。このREADMEでは、`gemini-3.7-flash` の36秒に対し、`gpt-5.6-sol` では言語あたり中央値で6分46秒かかります。
- CI環境（`CI` または `GITHUB_ACTIONS` が定義されている場合）では拒否されます。サブスクリプションの認証には個人のセッションファイルが使用されるため、共有ランナーに配置すべきではありません。
- 変数：`CODEX_BIN`、`CODEX_TIMEOUT`（セグメントあたりの秒数、デフォルト600）。

### Grokサブスクリプション経由：`--use_grok_cli`

SuperGrokまたはX Premium+のサブスクリプションを利用し、公式のGrok Build CLIでも同様の原則が適用されます。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Codexよりも限定的な分離環境。** GrokのOSサンドボックスは、近年の多くのLinuxマシン（AppArmor、コンテナランタイムソケット）には適用されず、適用できないプロファイルは通知なく非サンドボックス状態で起動します。そのためスクリプトはデフォルトでプロファイルを要求せず、それを告知した上で、CLIの `--deny` ルール（告知なしに保護を解除するのではなく起動を拒否する唯一の層であるキャッチオール `*` を含む）に依存します。`GROK_TRANSLATE_SANDBOX=read-only` はOSサンドボックスを要求し、マシンが対応できない場合は起動に失敗します。
- クォータは週間単位でChat、Imagine、Voiceと共有されており、それを確認するコマンドは存在しません。バッチ処理を行うと、気付かないうちに会話用の利用枠を消費する可能性があります。
- 変数：`GROK_BIN`、`GROK_HOME`（CLIディレクトリ、デフォルト `~/.grok`）、`GROK_TIMEOUT`（デフォルト900）、`GROK_TRANSLATE_SANDBOX`。

### Googleサブスクリプション経由：`--use_antigravity`

Antigravityの公式CLIである `agy` でも同様の原則が適用されます。Google AI ProまたはUltraの契約者の場合、翻訳はトークン課金ではなくサブスクリプションのクォータから差し引かれます。これがこのクォータを利用する唯一の方法です。Gemini CLIは2026年6月18日以降これらのアカウントをサポートしておらず（[告知](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)）、AntigravityのSDKはAPIキーまたはGoogle Cloudプロジェクトのみを受け付けます。

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **有料経路は一切開かれたままになりません。** agyは環境から限定された変数のリスト（`PATH`、言語とタイムゾーン、ターミナル、ID、プロキシと証明書、セッションバス）のみを受け取り、キーは一切受け取りません。いくつかの変数は何も表示せずに呼び出し先を切り替えてしまい（検証結果：ドキュメントをサードパーティのゲートウェイに送信するものや、課金対象のGoogle Cloudプロジェクトに送信するものがありました）、除外リストでは見直しごとに漏れが生じていました。全セグメントの実行前に、クォータを消費しない `agy -p /config` によって有料AIクレジットが無効化され、APIキーもGoogle Cloudプロジェクトも存在しないことを確認する必要があります（設定が存在しない場合は拒否とみなされます）。そうでない場合、翻訳は一切行われません。さらに、各呼び出しのログでサブスクリプションが証明されなければならず（`authMethod=consumer`）、そうでなければ応答は拒否されます。
- **サンドボックス化。** 各呼び出しはツールを持たない翻訳エージェントとともに、使い捨てのプライベートなホームディレクトリで実行されます。ユーザーの設定、ルール、プラグイン、MCPサーバー、agyフックがそこに侵入することはなく、履歴に追加されることもありません。また、ログイン情報はキーリング内に保持され、aipmtがそれを読み取ることは決してありません。エージェントが見つからない場合、agyは暗黙のうちにコーディングエージェントとそのツールにフォールバックします。そのため、ログの完全な1行で正しいエージェントが確認されなければならず（ドキュメント内にそのメッセージが引用されていても代替にはなりません）、確認できない場合は拒否されます。
- **プラットフォーム**：Linux（キーリングを持つセッション環境：D-Busセッションバス、Secret Service）。macOSもサポートされますが、測定は行われていません。各呼び出しを分離する変数をagyが読み取らないWindowsや、セッションバスのないLinux（SSHセッション、コンテナ、サーバーなど。この場合agyはトークンを `~/.gemini` のファイルに保存しますが、分離によって隠蔽されます）では拒否されます。ログインコードの待機に1分費やすのではなく、起動前に原因とともに拒否されます。
- **モデル**：`agy models` のモデル群。Geminiは名前にエフォートが含まれており（`gemini-3.8-flash-medium`…）、サフィックスのない名前は呼び出し前に拒否され、`--reasoning_effort` は効果を持ちません。agyがGemini 3.7 Flashの提供を終了して以降、デフォルトは `gemini-3.8-flash-medium`、`--eco` では `gemini-3.8-flash-low` です。デフォルトを決定した検証については、[詳細な測定結果](#詳細な測定結果)で説明されています。Gemini 4 Hydrogen（`gemini-4-hydrogen-low`…）は3.8 Flashとクォータを共有しますが、消費量はより多くなります。このREADMEの中程度エフォートでは、0.32に対して5時間ウィンドウの0.95ポイントを消費します。ClaudeとGPT-OSSは独自のクォータを持ち、はるかに小さくなります。測定された呼び出しあたり、Flashの0.05%に対して5時間ウィンドウの約1%を消費します。Gemini 4 Argonには独自の週間クォータがあり、このREADMEではその1.35%を消費します。
- **クォータ**：グループごとに、トークンコストに応じた5時間ウィンドウと週間ウィンドウがあります。作成者のアカウントでの測定値：`gemini-3.8-flash-medium` でソース文字100万字あたり5時間ウィンドウの約16ポイント、`gemini-3.7-flash-medium` で14ポイント、低エフォートで7〜8ポイントです。したがって、40,000文字のREADMEのコストは0.5ポイント強となります。週間上限はプランによって異なります。再試行はagyがリトライ可能と宣言したものに従います。それ以外の場合、使い切ったウィンドウで再試行されることはなく、`/usage` が表示するリセット時刻まで各ファイルが失敗します。
- **APIよりも低速**：測定用の長文記事では、API経由のGemini 3.7 Flashの1分18秒に対し、`gemini-3.8-flash-medium` で中央値3分59秒、`gemini-3.7-flash-medium` で3分14秒かかります。
- **中断**：Ctrl-Cやターミナルの切断を行うと、agyはクォータを消費してターンを終了するのではなく、コマンドとともに停止します。Codex、Grok CLI、OpenCodeも同様です。`nohup` の下では、翻訳が継続します。
- CI環境（`CI` または `GITHUB_ACTIONS` が定義されている場合）では拒否されます。ログイン情報は個人のキーリングに存在します。ランナー上では、`GOOGLE_API_KEY` を指定した `--use_gemini` を使用してください。
- 変数：`AGY_BIN`（未設定の場合は `PATH`、次いで `~/.local/bin/agy`）、`AGY_TIMEOUT`（起動時間を含むセグメントあたりの秒数、デフォルト900）。

**利用規約：ご自身のアカウントが対象となります。** [Antigravityの利用規約](https://antigravity.google/terms)（セクション6）およびその[FAQ](https://antigravity.google/docs/faq/)では、Antigravityのログインを利用してサードパーティのソフトウェア経由でサービスにアクセスすることを禁止しており（Claude Code、OpenClaw、OpenCodeが言及されています）、アカウント停止の対象となります。aipmtはトークンを読み取ったり再利用したりしません。GoogleがスクリプトやCI向けに文書化している[ヘッドレスモード](https://antigravity.google/docs/cli/headless/)で公式バイナリを起動します。Googleの担当者は、個人の作業のためにローカルスクリプトから `agy -p` を起動することを「標準的」と見なしていますが（[公式フォーラム、2026年9月25日、法的拘束力のない回答](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829)）、本作のような分散ツールの場合を明確に裁定した文書はありません。

**公開ドキュメント専用。** 同じ規約のセクション5によると、有料サブスクリプションを含め、やり取り（プロンプト、応答、メタデータ）はGoogleの製品や機械学習の改善に使用されたり、人間によって確認されたりする可能性があります。除外には未文書の効果を持つ設定 `enableTelemetry` を使用しますが、aipmtはこれを設定しません。agyの設定はその分離環境には引き継がれません。機密情報は一切渡さないでください。

### Claudeサブスクリプション経由：`--use_claude_code`

Claude Code公式CLIである`claude`を`-p`モードで使用する場合も同じ原理です。Claude ProまたはMaxの有料ユーザーの場合、翻訳はトークン単位で課金されるのではなく、サブスクリプションのクォータから差し引かれます。従量課金制であるAnthropicのAPI、`--use_claude`と混同しないでください。

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **有料ルートは一切開かれたままにならず、各呼び出しがそれを証明します。** Claude Codeは、環境から限定された変数のリストのみを受け取ります。APIキー、トークン、クラウドプロバイダー、aipmtが起動されたClaude Codeセッションの識別子のいずれも受け取りません。最初のセグメントの前に、`claude auth status`がConsoleキーのないサブスクリプション接続を表示しなければならず、クォータを一切消費しない`/usage`がそれを証明する必要があります。各呼び出しも初期化イベントで順次それを証明し、証明されない場合、応答は拒否されます。
- **「extra usage」を無効化してください**（claude.aiの 設定 → 使用状況）。0ユーロを維持するためです。有効になっている場合、枠を使い果たした際に引き継がれ、エラーを表示することなく課金されます。aipmtは、呼び出しのクォータレポートがそれを検知すると直ちに翻訳を停止しますが、その呼び出し自体はすでにカウントされています。
- **Claude Codeセッションと共有されるクォータ。** 各呼び出しは、5時間ウィンドウおよび週間ウィンドウの使用状況を報告します。80%（`AIPMT_CLAUDE_MAX_UTILIZATION`）を超えると、普段の作業に使う分を使い果たさないよう、それ以上のセグメントは開始されません。
- **隔離環境。** 各呼び出しはツールなしで、プライベートで使い捨てのディレクトリ内において、カスタマイズなしのモードで実行されます。`CLAUDE.md`、プラグイン、フック、MCPサーバー、設定はいずれも読み込まれず、セッションからは何も保持されません。添付ファイルは遮断されます。ドキュメント内の`@chemin`はテキストのまま維持され、ファイルを開くことはありません（測定済み）。
- **モデル**：デフォルトは`sonnet`、エフォートは`low`、`--eco`でも同様です。このパスでは`--eco`は何の影響も与えません。同じドキュメントで測定したところ、`haiku`は2倍遅く（防ぎようのない思考を行います）、コストはわずかに低い程度であり、`opus`は生物学のコンテンツを拒否します（次の項目を参照）。どちらも`--model`経由で引き続きアクセス可能です。これらのエイリアスは、それぞれのファミリの最新モデルに追従します。`fable`および`[1m]`バリアントは、有料クレジットに移行するため拒否されます。`--reasoning_effort`はエフォートを調整しますが、翻訳では何の効果も得られず、測定された思考はゼロまたはほぼゼロです。
- **Opusは一部の生物学コンテンツを拒否します。** そのガードレールはSonnetのものよりも厳格であり、Anthropicのエラーメッセージでは「生物学研究に関連する作業にフラグが立つことがある（can sometimes flag biology-research-adjacent work）」と警告されています。実測結果：生成された279個の分子に関するウォッチ記事の短報によって、14言語すべてで記事が拒否されました。何も書き込まれません。aipmtは途切れた応答を拒否し、ガードレール名を挙げ、`--model sonnet`を推奨します。
- CI環境（`CI`または`GITHUB_ACTIONS`が定義されている場合）およびWindows環境（未測定）では拒否されます。
- 変数：`AIPMT_CLAUDE_BIN`（指定がない場合は`PATH`、次に`~/.local/bin/claude`）、`AIPMT_CLAUDE_TIMEOUT`（セグメントあたりの秒数、デフォルトは900）、`AIPMT_CLAUDE_MAX_UTILIZATION`（デフォルトは0.8）、`CLAUDE_CONFIG_DIR`（Claude Codeのアカウント、プロジェクトの`.env`からは取得されません）。作業ディレクトリは`XDG_CACHE_HOME/aipmt/claude-code`配下（デフォルトは`~/.cache`）。

**利用規約：責任はお客様のアカウントに帰属します。** [Claude Codeの法的情報ページ](https://code.claude.com/docs/en/legal-and-compliance)では、「エンドユーザーが自身のClaudeサブスクリプションを使用して、変更されていないClaude Codeバイナリにサインインすること」は禁止されていません。これは公式バイナリを起動し、トークンを決して読み取らないaipmtが行っていることです。しかし、Anthropicは「サードパーティの開発者が […] ユーザーに代わってFree、Pro、またはMaxプランの認証情報を通じてリクエストをルーティングすることを許可しておらず」、「オープンソースプロジェクトを含む」サードパーティツールに対してはAPIキーを推奨しており、その使用を有料クレジットから差し引く権利を留保しています（[Claudeヘルプ](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)）。バイナリを起動する配布ツールに関する事例を明確に判断した文書はありません。

**データ**：Free、Pro、Maxアカウントでは、プライバシー設定で許可されている場合、モデルのトレーニングがClaude Codeにも適用されます（[データページ](https://code.claude.com/docs/en/data-usage)）。aipmtはローカルにトランスクリプトを一切保持しません（`--no-session-persistence`）。機密情報は通さないでください。

### 好みのプロバイダーへ：`--use_opencode`

[OpenCode](https://opencode.ai)は、内部で設定されたプロバイダー（APIキー、サブスクリプション、アカウント不要の無料モデルを提供するOpenCode Zenゲートウェイ、またはローカルモデル）へとルーティングするオープンソース（MIT）のコードエージェントです。ここではZenとOllamaの2つの経路がエンドツーエンドで測定されました。

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

`--model`は必須です。これがないと、OpenCodeはやり取りがトレーニングに使用される可能性のある無料モデルへとフォールバックしてしまいますが、そのような選択を勝手に行うことはありません。

各呼び出し時の隔離環境：

- 独自設定より優先されるインライン設定により、すべてのツールが拒否された（`permission: { "*": "deny" }`）`aipmt`エージェントを定義し、セッション共有は無効化、`--pure`、`--auto`は不可。
- 空の使い捨て作業ディレクトリに`OPENCODE_DISABLE_PROJECT_CONFIG`と`OPENCODE_DISABLE_CLAUDE_CODE`を配置。これらがないと、OpenCodeは現在のディレクトリの`AGENTS.md`と`~/.claude/CLAUDE.md`をプロンプトに注入します。グローバルの`~/.config/opencode/AGENTS.md`は注入されたままとなり、OpenCodeではこれを除外できません。
- 出力規約：リターンコード0、`error`イベントなし、ツール呼び出しなし、最終ステップが`stop`、空でないテキスト、および`aipmt`エージェントが実際に読み込まれていること。未知の`--agent`があってもOpenCodeは失敗せず、コーディングエージェントへと暗黙的にフォールバックします。
- OpenCode自体のキーである`OPENCODE_API_KEY`を除き、`aipmt`のキーは一切渡されません。プロバイダーは`aipmt`の`.env`ではなく、OpenCode内で設定します。

知っておくべきこと：

- Zenの無料モデルは変動しやすく、制限も文書化されておらず、やり取りがトレーニングに使用される可能性があります。パブリックなドキュメント向けであり、プライベートなコンテンツ向けではありません。
- セグメントは最大16,000文字になるため、ローカルモデルは少なくとも16kトークンのコンテキストを提供する必要があります。Ollamaは4,096に設定されていることが多いため、`PARAMETER num_ctx 32768`を指定した`Modelfile`を経由してください。
- `--eco`は無効です。`--reasoning_effort`はOpenCodeの`--variant`としてそのまま渡されます。
- OpenCodeは各セッションを`~/.local/share/opencode/`にログ出力します。
- 変数：`OPENCODE_BIN`（指定がない場合は`PATH`、次に`~/.opencode/bin/opencode`）、`OPENCODE_TIMEOUT`（セグメントあたりの秒数、デフォルトは600）。`OPENCODE_CONFIG`はOpenCodeにそのまま渡されます。

`~/.config/opencode/opencode.json`でのOllamaを介したローカルモデルの例：

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

`reasoningEffort: "none"`は、Ollamaがこれらのモデルでデフォルトで有効にしており、Modelfileでは無効化できない思考を遮断します。6単語の文での実測結果：オプションなしでは919思考トークンおよび68秒、オプションありでは9トークンでした。

### 400以上のモデルへ：`--use_openrouter`

OpenRouterは、サードパーティがホストするモデル（ここでは他のどのプロバイダーも提供していないオープンな中国製モデルを含みます）の前段に位置し、単一のクレジットで従量課金されるルーターです。

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model`は必須です。課金が発生する前に実行されるプリフライトチェックにより、ルーティングの2つの特殊性が処理されます。

- **同一モデルが、上限の異なる数十のホストから提供されている点** — `z-ai/glm-5.3-flash`では23のホストが存在し、そのうちの1つは出力が2,048トークンに制限されています。プリフライトは`/api/v1/models/{modèle}/endpoints`を読み取り、出力が8,000トークン未満またはステータスが低下しているホストを除外し、その他のホストを`allow_fallbacks: false`で固定します。
- **思考が出力料金で課金される点** — `z-ai/glm-5.2`の「OK」という応答に対して、通常2トークンのところ107トークン消費されます。デフォルトではオフになっています。思考を強制するモデルには、受け入れ可能な最も低いエフォートが送られます。カタログのデフォルト設定では翻訳が完了する前に出力が飽和する可能性があるためです。`--reasoning_effort`が引き続き優先されます。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- コンテキストウィンドウはカタログから取得されます。16,400トークン未満のモデルは、呼び出し前に拒否されます。プロンプトとセグメントに8,400、出力に最低8,000が必要です。
- カタログに存在しないスラッグ、カタログに接続できない場合、または上限を満たすホストが存在しない場合は、コマンドが停止します。
- 出力が空の`finish_reason=length`は、切り捨てではなく思考によって予算が消費されたことを意味します。メッセージによって区別されます。
- `--eco`は無効です。
- 変数：`OPENROUTER_API_KEY`（<https://openrouter.ai/keys>）、`OPENROUTER_BASE_URL`（デフォルトは`https://openrouter.ai/api/v1`、`https://`が必須）、`OPENROUTER_TIMEOUT`（デフォルトは900）、`OPENROUTER_PREFLIGHT_TIMEOUT`（デフォルトは30）。

### 翻訳ノート

`--add_translation_note`は、`bottom`（デフォルト）、`top`（フロントマターの後）、または`both`（`--note_position`）に、`legacy`（太字の段落、デフォルト）または`marker`（`--note_format`）形式でノートを追加します。`marker`形式は、不可視のMarkdown参照定義である`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`に続いて太字の引用を配置するもので、GitHub上で可読性があり、ビルド時にremarkプラグインで活用できます。

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## 詳細な測定結果

すべての測定は、`aipmt`を使用して14言語（en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi）に向けて実際に実行された翻訳です。**書き込み**はガードを通過したファイル数をカウントし、**差異なし**は`scripts/compare_structure.py`が何も検知しなかったもの（セクション数、小見出し、リンク、個別URL、コードブロック、インラインコード、テーブル行、ブロック引用、太字の単語数が同一であること）をカウントします。

「差異なし」は「検知されなかった」ことを意味し、「同一」を意味するわけではありません。コンパレータは内容を読まずに要素をカウントします。レベル4の見出しの削除、インラインコード内のテキストの置換、フラグの入れ替わり、余分な括弧が付いてどこにも繋がらなくなった内部リンク（`[texte]((#ancre))`）などは報告されず、言語の質を判定することもありません。

### 密度の高いウォッチ記事、`--news`モード

[jls42.orgのAIウォッチ](https://jls42.org/fr/news)の1号分：589行、140リンク、21セクション、保護された3つの英語引用。2026年9月4日および5日のテスト。

| モデル | アクセス | 書き込み | 差異なし | 中央値/言語 |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash` | Google API | 14/14 | ✅ **14/14** | 1分18秒 |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | Google サブスクリプション | 14/14 | ✅ **14/14** | 3分59秒 |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | Google サブスクリプション | 14/14 | ✅ **14/14** | 3分14秒 |
| `claude-sonnet-5-5` | Anthropic API | 14/14 | ✅ **14/14** | 3分37秒 |
| `gpt-5.6-sol` (`--use_codex`) | ChatGPT サブスクリプション | 14/14 | ✅ **14/14** | 11分28秒 |
| `z-ai/glm-5.2` | OpenRouter | 14/14 | ✅ **14/14** | 5分37秒 |
| `qwen/qwen3.8-flash` | OpenRouter | 14/14 | ✅ **14/14** | 26分23秒 |
| `sonnet` (`--use_claude_code`) | Claude サブスクリプション | 14/14 | ⚠️ 13/14 | 6分49秒 |
| `claude-sonnet-5` | Anthropic API | 14/14 | ⚠️ 11/14 | 6分31秒 |
| `haiku` (`--use_claude_code`) | Claude サブスクリプション | 14/14 | ⚠️ 11/14 | 15分54秒 |
| `claude-haiku-5-5` | Anthropic API | 14/14 | ⚠️ 11/14 | 2分54秒 |
| `claude-haiku-4-5` | Anthropic API | 14/14 | ⚠️ 7/14 | 6分00秒 |
| `opencode/mimo-v2.5-free` | OpenCode Zen | 13/14 | ❌ 11/14 | 9分27秒 |
| `qwen/qwen3.7-flash` | OpenRouter | 13/14 | ❌ 8/14 | 10分09秒 |
| `ollama/gpt-oss-20b-32k` | ローカル | 10/14 | ❌ 7/14 | 12分39秒 |
| `mistral-large-latest` | Mistral API | 11/14 | ❌ 5/14 | 5分32秒 |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter | 4/14 | ❌ 3/14 | 37分27秒 |
| `grok-4.6` (`--use_grok_cli`) | Grok サブスクリプション | 1/14 | ❌ 1/14 | 23分11秒 |
| `opus` (`--use_claude_code`) | Claude サブスクリプション | 0/14 | ❌ 0/14 | — |

Grokは9月9日に同じウォッチの別の版（356行）で再測定されました。14言語中9言語が書き込まれ、8言語で差異なしでした。冒頭の表に記載されているのはこの数値です。中断された3つのテストは記載されていません。クレジット不足による`qwen3.5-27b`（9言語）と`kimi-k2.6`（4言語）、そして2件の失敗が思考設定に起因していた`z-ai/glm-5.3-flash`（プロバイダーがその後修正）です。OpenRouterの行は、`--use_openrouter`導入前のルーターのデフォルト設定で測定されました。提供されているプロバイダーで再測定された`z-ai/glm-5.2`は、同様に14/14を返します。数値は現在のコンパレータを使用して9月10日に再計算されました。初出時と比較して`qwen3.8-flash`と`qwen3.7-flash`はそれぞれ1言語増加し、その他は変更ありません。

`--use_antigravity`の行は9月26日に同じ記事で測定され、4つの翻訳が並行して実行されました。午前中に`gemini-3.7-flash-medium`、午後に`gemini-3.8-flash-medium`です。英語では、それぞれがフラグを捏造することなく引用文の下にある3行のフランス語訳を自ら削除し、英語の引用文はそのまま残されたため、フォールバックのクリーンアップ処理は何も行う必要がありませんでした。`--eco`（`gemini-3.7-flash-low`）では、4言語のみ（en, ja, ar, hi）で実施：4件中4件書き込み完了、すべて差異なし、中央値は1分52秒でした。同日、ウォッチのより新しい版である9月25日の記事（438行、英語の引用2点）で、ブログ外から`gemini-3.7-flash-medium`によって翻訳された対照試験：14件中14件書き込み完了、すべて差異なし、言語あたり87〜128秒でした。

`--use_claude_code`の行は9月26日に同じ記事で測定され、エフォート`low`にて4つの翻訳が並行して実行されました。`sonnet`では、英語の引用は14言語すべてでそのまま維持され、英語ではモデルがフラグを捏造することなくフランス語訳の行を自ら削除しました。`opus`は1言語も書き込めませんでした。結合部位向けに生成された279分子に関する短いニュースが原因で、各言語において最後のセグメントでガードレールによって応答が停止されました。単体で送信された場合、この短報は「生物（bio）」カテゴリに該当するとして拒否されますが、`sonnet`はすべて翻訳しました。`haiku`は14言語すべてを書き込みました。そのうち3言語（en, pl, ro）で、セクションのタイトルがレベル2からレベル1に変更されました。防ぎようのない思考を行い（出力トークンの61%）、その結果、`sonnet`の2倍以上の時間がかかりました。

`claude-sonnet-5-5`、`claude-haiku-5-5`、および`claude-haiku-4-5`の行は、10月18日にAnthropic APIを通じて同じ記事で測定され、モデルごとに4つの翻訳が並行して実行されました。Sonnet 5.5は思考を遮断することを拒否します。aipmtは受け入れ可能な最低の設定を送信し、その応答には思考が一切含まれません。差異なく、セグメントのやり直しもなしに14言語を書き込みました。英語では、フラグを捏造することなくフランス語訳の行を自ら削除し、英語の引用はどこでもそのまま維持されました。Haiku 5.5は適応的な思考（adaptive thinking）を有効にして測定されました。思考を遮断するとフランス語の段落が丸ごと残され、ガードによって拒否されました（14言語中3言語書き込み完了）。両方のHaikuが同じ短報で行き詰まりました。Haiku 5.5は日本語、韓国語、中国語でそのタイトルのレベルを変更するか重複させ、Haiku 4.5は7つの言語でレベル1に変更し、日本語ではフランス語のまま残しました。2つのドキュメントを14言語に翻訳した場合のコストは、Haiku 4.5が3.67ドル、Haiku 5.5が0.57ドル、Sonnet 5.5が9.21ドルでした。

### 本プロジェクトのREADME、標準Markdown

2026年9月9日時点の固定リビジョン：785行、インラインコード285個、コードブロックの閉じ記号40個、表の行89行。4並行で翻訳を実施。

| モデル                                          | 生成完了 | 差異なし | 中央値/言語 | 差異の内容                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1分43秒     | なし                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1分48秒     | なし                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4分02秒     | 比較ツール上は差異なし。内部リンクの重複（en）                   |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1分18秒     | なし                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2分06秒     | なし                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36秒           | 太字が1単語（ja）                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1分22秒     | 太字が1単語（ko）                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2分20秒     | 表の行が直前の行と結合（ar）                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2分56秒     | リンクが1件（sv）、太字が1単語（zh）                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6分46秒     | 太字が1単語（ar、ja）                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2分34秒     | 太字が1単語（hi、ja、ko）                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2分17秒     | アラビア語でインラインコードが40個追加、太字（hi、ja、ko）                   |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1分14秒     | 2言語で拒否（ar、hi）：戻り値でインラインコードが欠落        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2分44秒     | セクションの欠落（ar、hi、ko）、コードブロックの追加（ja、ko、ro、zh） |

中断された2つの測定は記載していません：Grok（12言語完了後にCLIセッションが期限切れ、うち11言語で差異なし）と、`qwen3.8-flash`（2言語完了後にホスティング側でHTTP 429が発生）。`opencode/mimo-v2.5-free`および`ollama/gpt-oss-20b-32k`は今回のリビジョンでは再測定していません。277行短かった9月4日〜5日のリビジョンでは、それぞれ14言語中9言語を出力し、差異なしは7言語と1言語でした。

行の`--use_antigravity`および`--use_claude_code`は固定リビジョンではなく、9月26日に1.14.0で公開されたリビジョンで測定されました。行の`claude-sonnet-5-5`、`claude-haiku-5-5`、`claude-haiku-4-5`は10月18日に同じリビジョン（600行、インラインコード257個、コードブロックの閉じ記号30個、表の行85行）で測定されています。185行短いため、他の行と単純に直接比較することはできませんが、これらの行同士では比較可能です。比較ツールでは検証されない内部リンクについて、`gemini-3.8-flash-medium`は14言語すべてで正常に保持し、`gemini-3.7-flash-medium`はイタリア語で破損させました。`sonnet`と`opus`はすべての言語で正常に保持し、`haiku`は英語で重複させました。`claude-sonnet-5-5`と`claude-haiku-4-5`は14言語すべてで正常に保持し、`claude-haiku-5-5`は出力した12言語で保持しました。

### 著名プロジェクトの4つのREADME

FastAPI、Ollama、tldr-pages、Vue.jsをGitHubからそのまま取得したもので、前の2つのドキュメントよりも扱いやすいものです。この測定は課題のあるモデルを対象としており、Geminiを比較基準として使用しています。

| モデル                    | 対象範囲                  | 生成完了 | 差異なし   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4プロジェクト × 14言語     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4プロジェクト × 14言語     | 55/56   | ❌ 47/56     |
| `grok-4.6` (サブスクリプション)   | 4プロジェクト × ar、hi、ja、zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4プロジェクト × ar、hi、ja、zh | 15/16   | ❌ 9/16      |

### これらの測定に含まれないもの

- **網羅的なランキングではありません**：OpenRouterだけでも400以上のモデルを提供しており、測定されたのはそのうちの約15モデルです。
- **所要時間はあくまで目安です**：キャンペーンに応じて3〜6件の並行翻訳を行っており、プロバイダーのスループットは時間帯によって変動します。
- **特定時点での観測結果です**：同じ名前のままでもモデルは更新されますし、あなたのドキュメントは私たちのものとは異なります。

ご自身のドキュメントで、ファイルの固定コピーに対して再測定を行うには：

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

両方の行が必要です：`pip install -e .`がない場合、`python -m aipmt`は`No module named aipmt`と返答します。

品質管理ツール（任意ですが推奨）：

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

リポジトリの28の翻訳（READMEおよびCHANGELOG、14言語）は`./regen_translations.sh --force`で再生成されます。デフォルトではChatGPTサブスクリプション上のCodexおよび`gpt-6.1-sol`を使用し、4並行で実行されます。`REGEN_PROVIDER`と`REGEN_MODEL`でパスを変更できます：`antigravity`はGoogleのサブスクリプションのままであり、追加設定なしでパスします。従量課金制API（`openai`、`gemini`、`grok`、`openrouter`）は`REGEN_ALLOW_PAID_API=1`がないと拒否されます。`REGEN_JOB_TIMEOUT`は各ジョブに上限時間を設定します（600秒、CodexおよびAntigravityでは1,800秒）。ツールの詳細は`CLAUDE.md`に記載されています。

## 本スクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** — 15言語で公開されている個人ブログ。その[日次AI動向ウォッチ](https://jls42.org/fr/news)は本ツールによって毎日翻訳されており、上記の測定における参照ドキュメントとして機能しています。

## 著者

Julien LE SAUX
メール：contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。詳細は[LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)を参照してください。

## 免責事項

本プログラムは、GPL v3の第15条および第16条の規定に基づき、**いかなる保証もなしに**配布されます。「現状のまま」提供され、商品性や特定目的への適合性の保証はなく、その作者は使用から生じたいかなる損害についても責任を負いません。本要約よりもライセンスの原文が優先されます。

- **公開前に必ず再確認してください。** 保護対象となるのはコードブロック、インラインコード、URL、アンカー、および`--news`モードの引用であり、見出し、表、フロントマター、文の意味は保護されません。
- **ドキュメントは選択したプロバイダーに送信されます。** 利用規約およびデータポリシーは各社に準拠します。一部の無料モデルはやり取りを学習に再利用する場合があり、Antigravityの規約では、有料サブスクリプションであってもGoogleによる再利用や人間によるレビューが許可されています。マシンからデータを一切外部に出さない唯一の方法は、ローカルモデルを使用することです。
- **API呼び出しには料金が発生します。** 本プログラムは支出の上限を設けていません。長いドキュメント、失敗後のリトライ、あるいは推論を多く行うモデルは、より多くのコストがかかります。
- **公開されている測定結果は特定時点での観測値であり**、保証ではありません。

記載されている製品名および会社名は、それぞれの所有者の商標です。本プロジェクトはそれらのいずれとも提携していません。

**gemini-3.8-flash-mediumでフランス語から日本語へ翻訳された記事。**
