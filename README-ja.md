# AI搭載Markdown翻訳ツール

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 コード品質</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="品質ゲートのステータス"></a>
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

**OpenAI**、**Mistral AI**、**Claude (Anthropic)**、**Google Gemini**を使用したMarkdownファイル翻訳ツールです。

このPythonスクリプトは、書式、コードブロック、front matterメタデータを保持しながら、Markdownファイルを原文言語から対象言語へ翻訳します。

## 主な特徴

- **マルチプロバイダー**: 4つのAPI（OpenAI、Mistral、Claude、Gemini）と、ChatGPTサブスクリプションのCodex CLIをサポート
- **2026年モデル**: GPT-5.6 Terra、Claude Sonnet 5、Gemini 3.7 Flash
- **エコノミーモード**: より高速で低コストなモデルを使用する `--eco` オプション
- **単一ファイル**: 1つのファイルだけを翻訳する `--file` オプション
- **インテリジェントな分割**: モデルごとのトークン制限に対応した長文処理
- **コードの保持**: コードブロックとインラインコード（`` `...` ``）を保持
- **ファイル名**: 元の名前を維持する `--keep_filename` オプション
- **ニュースモード**: 英語の引用符を保護し、ニュース記事内の国旗を処理する `--news` オプション
- **.env設定**: APIキー用の `.env` ファイルをサポート
- **翻訳注記**: 文書末尾への注記追加（任意）

## インストール

### ツールを使用する場合

```bash
pip install ai-powered-markdown-translator
```

これで `aipmt` コマンドをどこからでも使用できます。Pythonのスクリプトディレクトリが
`PATH` に含まれていない場合は、`python -m aipmt` でもまったく同じことができます。Python 3.10以降が必要です。

他のパッケージから分離してインストールする場合：

```bash
pipx install ai-powered-markdown-translator
```

### プロジェクトに貢献する場合

開発にはクローンしたリポジトリが必要です。テスト、28種類の翻訳、品質管理ツールはすべてそこにあります。

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` は**完全に固定されたlock**で、テスト済み環境を正確に反映しています。`pyproject.toml` で公開されている範囲は意図的に広く設定されており、他のパッケージに制約を課しません。

### 品質管理ツール（任意ですが推奨）

このプロジェクトでは、書式が不正なコード、脆弱なコード、秘密情報を含むコードのコミットを防ぐために [`pre-commit`](https://pre-commit.com) を使用します。インストール：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

有効なフック：ruff（lint+format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（複雑度）、detect-secrets（APIキー）、mypy（段階的な型付け）、Opengrep（SAST）、pip-audit（CVE deps）、unittest。詳細は `CLAUDE.md` の _Quality / pre-commit_ セクションを参照してください。

## 設定

`.env` ファイルを**コマンドを実行するディレクトリに**作成してください（まずそこを検索し、次に親ディレクトリを検索します）。または、環境変数を定義してください：

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

`GEMINI_API_KEY` は `GOOGLE_API_KEY` の代替として使用できます（AI Studioの規約）。任意の変数：`XAI_BASE_URL`（xAIエンドポイント、デフォルトは `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（Anthropicの呼び出し間隔、秒、デフォルトは
900）、`CODEX_BIN` / `CODEX_TIMEOUT`、`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`、
および `GROK_TRANSLATE_SANDBOX`（Grok CLIセクションを参照）。`regen_translations.sh` 側では、`REGEN_PROVIDER`、`REGEN_MODEL`、
`REGEN_JOB_TIMEOUT`（ジョブごとの上限、デフォルトは600秒）を使用できます。

## 使用方法

### 単一ファイルを翻訳する

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### ディレクトリを翻訳する

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
aipmt --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
aipmt --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
aipmt --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
aipmt --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
aipmt --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
aipmt --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
aipmt --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### ChatGPTサブスクリプションで翻訳する（`--use_codex`）

このプロバイダーはAPIキーを一切消費しません。公式Codex CLIを非対話モードで操作するため、翻訳はすでに支払い済みのChatGPTサブスクリプション（Plus、Pro、Businessなど）のクォータから差し引かれます。これはOpenAIがこの用途について文書化している唯一の方法です。`~/.codex/auth.json` のトークンはPlatform APIへの呼び出しを認証せず、このスクリプトから読み取られることもありません。

**前提条件：**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

バイナリは次の順序で検索されます：変数 `CODEX_BIN`、`PATH`、続いてPythonパッケージ `openai-codex-cli-bin`。後者を `requirements.txt` に含めていないのは意図的です。約250 MBあり、任意のプロバイダーのためにすべてのユーザーへ負担させることになるためです。

**知っておくべきこと：**

- **APIキーは使用されません。** `OPENAI_API_KEY` と `CODEX_API_KEY` はサブプロセスの環境から削除されます。これにより、`.env` にキーが存在していても、翻訳が従量課金へ切り替わることはありません。
- **1セグメント＝プランの5時間ウィンドウ内の「ローカルメッセージ」1件。** 品質モデル（`gpt-5.6-sol`、5時間あたり10～100メッセージ）ではなく、`--eco`（モデル `gpt-5.6-luna`、Plusでは5時間あたり250～2,000メッセージ）を使用してください。
- **API呼び出しより低速**です。直接実行なら数秒のところ、README全体で約45秒かかります。
- **CIでは拒否されます**（`CI` または `GITHUB_ACTIONS` が定義されている場合）。サブスクリプション認証は共有runner向けではなく、OpenAIも公開リポジトリでのこのワークフローを推奨していません。この経路ではAPIキーを使用してください。
- 環境変数：`CODEX_BIN`（バイナリの明示的なパス）および `CODEX_TIMEOUT`（セグメントごとの秒数、デフォルトは `600`）。

### Grokサブスクリプションで翻訳する（`--use_grok_cli`）

`--use_codex` と同じ仕組みですが、公式の **Grok Build** CLIを使用します。翻訳はトークン単位で請求されるのではなく、Grokサブスクリプション（SuperGrok / X Premium+）の利用分から差し引かれます。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**隔離について—使用前にお読みください。** このプロバイダーは構造上、`--use_codex` より**弱く**、それを前提としています。

- Codexは `--sandbox read-only` で動作します。これはシステムによって強制される境界です。
- Grokのサンドボックスは、最近のLinux環境の多くでは適用できません。Ubuntu 24.04以降ではAppArmorが権限のないuser namespaceをブロックし、`/run/podman` が `0700` の場合、コンテナランタイムのソケットdeny-listも失敗します。しかも、適用できない**組み込み**プロファイルは、隔離されていない状態で黙って起動します。
- そのためスクリプトはデフォルトでプロファイルを要求せず、決して黙ってフォールバックしません。警告を表示します。隔離はCLIの `--deny` ルール（catch-allの `*` を含む）に依存します。これは唯一、_fail-closed_ が測定された層です。不明なルールがある場合、保護を黙って解除するのではなく、起動を拒否します。
- OSサンドボックスを**必須にする**には `GROK_TRANSLATE_SANDBOX=read-only` を使用します。マシンがそれを実行できない場合は起動に失敗します。これが意図された動作です。

**クォータ**：GrokのプールはChat、Imagine、Voiceと**週単位で共有**され、読み取るコマンドはありません。そのため、バッチ処理が何も通知せずに会話での使用量を消費する可能性があります。これが同時実行数を2に制限し、`regen_translations.sh` に警告を表示する理由です。

その他の変数：`GROK_BIN`（バイナリのパス）、`GROK_TIMEOUT`（デフォルト900秒）。

28種類の翻訳を再生成するには：

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### エコノミーモード

より高速で低コストなモデル（gpt-5.6-luna、claude-haiku-4-5、gemini-3.1-flash-lite）を使用します：

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### オプション

| オプション | 説明 |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file` | 翻訳する単一のMarkdownファイル |
| `--source_dir` | Markdownファイルを含むソースディレクトリ |
| `--target_dir` | 翻訳済みファイルの出力ディレクトリ |
| `--source_lang` | 原文言語（デフォルト: `fr`） |
| `--target_lang` | 対象言語（デフォルト: `en`） |
| `--model` | 使用する特定のモデル |
| `--eco` | エコノミーモデルを使用 |
| `--use_mistral` | Mistral AI APIを使用 |
| `--use_claude` | Claude APIを使用 |
| `--use_gemini` | Gemini APIを使用 |
| `--use_codex` | ChatGPTサブスクリプションのクォータでCodex CLIを使用 |
| `--use_grok` | xAI（Grok）APIを使用 — `XAI_API_KEY` が必要 |
| `--use_grok_cli` | GrokサブスクリプションのクォータでGrok CLIを使用 |
| `--force` | 再翻訳を強制 |
| `--keep_filename` | 元のファイル名を維持 |
| `--news` | ニュースモード：英語の引用を保護し、言語ごとに国旗を処理 |
| `--add_translation_note` | 翻訳注記を追加 |
| `--note_position` | 注記の位置：`top`、`bottom`（デフォルト）、または `both` |
| `--note_format` | 注記の形式：`legacy`（デフォルト、太字段落）または `marker` |
| `--include_model` | 出力ファイルにモデル名を含める |
| `--reasoning_effort` | GPT-5.xの推論強度：`none`/`low`/`medium`/`high`/`xhigh` |

> **6つのプロバイダーフラグは相互排他的です。** 以前は2つを組み合わせても黙って受け入れられ、最初に検査されたものが選択されていました。そのため、サブスクリプションのクォータ（`--use_codex`、`--use_grok_cli`）での翻訳を要求しても、警告なしに従量課金へ移行する可能性がありました。`argparse` は現在、この組み合わせを拒否します。

### 翻訳注記：位置と形式

`--add_translation_note` を使用すると、translatorは注記を上部、下部、または両方に配置でき、単純なテキスト形式（後方互換）またはMarkdownプラグインで利用可能な `marker` 形式で出力できます。

**位置**（`--note_position`）：

- `bottom`（デフォルト）：従来どおり、ファイル末尾に注記を追加。
- `top`：**YAML frontmatterの後**に注記を挿入（Astro Content Collections、gray-matterなどに対する安全性）。
- `both`：上部と下部の両方に注記を挿入（LLM呼び出しは1回のみで、内容を両方の位置に再利用）。

**形式**（`--note_format`）：

- `legacy`（デフォルト）：太字の段落 `**...**` — v1.8と完全に同一の動作で、byte-for-byte。Hugo、GitHub、GitLab、その他すべてのMarkdown rendererに対応。
- `marker`：不可視のMarkdown link reference definition（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）に続いて太字のblockquoteを配置。GitHub/GitLabではネイティブに表示でき、Astro側のremarkプラグインでビルド時に利用してスタイル付きバナーを生成できます（jls42.orgのブログを参照）。

```bash
# Compatibilité legacy (rien ne change vs v1.8)
aipmt --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### デフォルトモデル（2026年）

| プロバイダー | 品質（デフォルト） | エコノミー（`--eco`） |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **長文翻訳の推奨**：`--use_gemini`（デフォルト = `gemini-3.7-flash`）は、ラテン文字以外のスクリプト（PL、JA、ZH、AR、HI）でもMarkdown構造を忠実に保持します。`--news` モードではプレースホルダーの忠実性も維持されます。このREADMEを日本語に翻訳して測定した結果、`gemini-3.1-pro-preview` と同一の構造（21個のリスト、18個のコードブロック、13個のHTMLリンク、13個の画像、すべてのURLを保持）で、遅延は約6分の1でした。後方互換性のため、OpenAIをデフォルトのままにしています。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** - 多言語個人ブログ（15言語）

## 作者

Julien LE SAUX
メール：contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。詳しくは[LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)を参照してください。

**gpt-5.6-lunaでフランス語から日本語に翻訳された記事。**
