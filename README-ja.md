# AI搭載Markdown翻訳ツール

🌍 [フランス語](README.md) | [英語](README-en.md) | [スペイン語](README-es.md) | [中国語](README-zh.md) | [ドイツ語](README-de.md) | [日本語](README-ja.md) | [韓国語](README-ko.md) | [アラビア語](README-ar.md) | [ヒンディー語](README-hi.md) | [イタリア語](README-it.md) | [オランダ語](README-nl.md) | [ポーランド語](README-pl.md) | [ポルトガル語](README-pt.md) | [ルーマニア語](README-ro.md) | [スウェーデン語](README-sv.md)

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

**OpenAI**、**Mistral AI**、**Claude (Anthropic)**、**Google Gemini**を使用するMarkdownファイル翻訳ツールです。

このPythonスクリプトは、書式、コードブロック、front matterメタデータを保持しながら、Markdownファイルを原文言語から対象言語へ翻訳します。

## 主な機能

- **マルチプロバイダー**：4つのAPI（OpenAI、Mistral、Claude、Gemini）と、ChatGPTサブスクリプションで利用できるCodex CLIに対応
- **2026年モデル**：GPT-5.6 Terra、Claude Sonnet 5、Gemini 3.7 Flash
- **エコノミーモード**：より高速で低コストなモデルを使用する`--eco`オプション
- **単一ファイル**：1つのファイルだけを翻訳する`--file`オプション
- **インテリジェントな分割**：モデルごとのトークン上限に対応した長文処理
- **コードの保持**：コードブロックとインラインコード（`` `...` ``）を保持
- **ファイル名**：元のファイル名を維持する`--keep_filename`オプション
- **ニュースモード**：英語の引用を保護し、ニュース記事内の旗を処理する`--news`オプション
- **.env設定**：APIキー用の`.env`ファイルに対応
- **翻訳注記**：文書末尾に注記を任意で追加

## インストール

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 品質管理ツール（任意ですが推奨）

このプロジェクトでは、書式が不適切なコード、脆弱なコード、またはシークレットを含むコードのコミットを防ぐために、[`pre-commit`](https://pre-commit.com)を使用しています。インストール方法：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

有効なフック：ruff（lint+format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（複雑度）、detect-secrets（APIキー）、mypy（段階的型付け）、Opengrep（SAST）、pip-audit（依存関係のCVE）、unittest。詳細は`CLAUDE.md`の「_Quality / pre-commit_」セクションを参照してください。

## 設定

プロジェクトのルートに`.env`ファイルを作成するか、環境変数を設定します：

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

`GEMINI_API_KEY`は`GOOGLE_API_KEY`の代替として使用できます（AI
Studioの規約）。任意の変数：`XAI_BASE_URL`（xAIエンドポイント、既定値
`https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（Anthropicの呼び出しごとの秒数、既定値
900）、`CODEX_BIN` / `CODEX_TIMEOUT`、`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`、
および`GROK_TRANSLATE_SANDBOX`（Grok CLIのセクションを参照）。

## 使用方法

### 単一ファイルを翻訳する

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### ディレクトリを翻訳する

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
python translate.py --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
python translate.py --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
python translate.py --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### ChatGPTサブスクリプションで翻訳する（`--use_codex`）

このプロバイダーはAPIキーを一切消費しません。公式Codex CLIを非対話
モードで操作するため、翻訳はすでに支払い済みのChatGPT
サブスクリプション（Plus、Pro、Businessなど）のクォータから差し引かれます。
これは、この用途についてOpenAIが文書化している唯一の方法です。
`~/.codex/auth.json`のトークンではAPI Platformの呼び出しを認証できず、
このスクリプトがそれらを読み取ることもありません。

**前提条件：**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

バイナリは、環境変数`CODEX_BIN`、`PATH`、
Pythonパッケージ`openai-codex-cli-bin`の順に検索されます。最後のパッケージは意図的に
`requirements.txt`に含まれていません。サイズが約250 MBあり、任意のプロバイダーのために
すべてのユーザーへ強制することになるためです。

**注意事項：**

- **APIキーは一切使用されません。** `OPENAI_API_KEY`と`CODEX_API_KEY`は
  サブプロセスの環境から削除されるため、`.env`にキーが存在しても、
  翻訳が従量課金へ切り替わることはありません。
- **1セグメント＝5時間枠の「ローカルメッセージ」1件です。**
  品質モデル（`gpt-5.6-sol`、Plusでは10～100メッセージ/5時間）ではなく、
  `--eco`（モデル`gpt-5.6-luna`、Plusでは250～2,000メッセージ/5時間）を使用してください。
- **APIの直接呼び出しより低速です。** README全体では、直接呼び出しなら
  数秒なのに対し、約45秒かかります。
- **CIでは拒否されます**（`CI`または`GITHUB_ACTIONS`が定義されている場合）。
  サブスクリプション認証は共有runner向けではなく、OpenAIも公開リポジトリで
  このワークフローを使用しないよう推奨しています。この経路ではAPIキーを使用してください。
- 環境変数：`CODEX_BIN`（バイナリの明示的なパス）および
  `CODEX_TIMEOUT`（セグメントごとの秒数、既定値`600`）。

### Grokサブスクリプションで翻訳する（`--use_grok_cli`）

`--use_codex`と同じ仕組みで、公式CLIの**Grok Build**を使用します。
翻訳料金はトークン単位で請求される代わりに、Grokサブスクリプション
（SuperGrok / X Premium+）のクォータから差し引かれます。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**隔離 — 使用前に必ずお読みください。** このプロバイダーは構造上、
`--use_codex`よりも**脆弱**であり、これは意図した仕様です：

- Codexは、システムによって強制される境界である`--sandbox read-only`内で動作します。
- Grokのsandboxは、最近の多くのLinux環境では**適用できません**。
  Ubuntu 24.04以降ではAppArmorが非特権user namespaceをブロックし、
  `/run/podman`が`0700`の場合、コンテナruntime socketのdeny-listが
  失敗するためです。また、適用できない**組み込み**プロファイルは、
  **隔離されていない状態で何も通知せずに**起動します。
- そのため、スクリプトは既定でプロファイルを要求せず、**黙って
  フォールバックすることもありません**。代わりに警告を表示します。
  隔離はCLIの`--deny`ルール（catch-allの`*`を含む）に依存します。
  これは、未知のルールがある場合に保護を黙って解除するのではなく、
  起動を拒否する、検証済みの唯一の_fail-closed_層です。
- OSのsandboxを**必須にする**には、`GROK_TRANSLATE_SANDBOX=read-only`を使用します。
  マシンが対応できない場合は起動に失敗しますが、これは意図した動作です。

**クォータ**：Grokのプールは**週単位で、Chat、Imagine、Voiceと共有**され、
確認するコマンドはありません。そのため、バッチ処理によって何の通知もないまま
会話での利用可能量が減る可能性があります。このため、同時実行数は2に制限され、
`regen_translations.sh`に警告が表示されます。

その他の変数：`GROK_BIN`（バイナリのパス）、`GROK_TIMEOUT`（既定値900秒）。

28言語の翻訳を再生成するには：

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
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### オプション

| オプション                   | 説明                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | 翻訳する単一のMarkdownファイル                                       |
| `--source_dir`           | Markdownファイルを含む原文ディレクトリ                        |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ                          |
| `--source_lang`          | 原文言語（既定値：`fr`）                                             |
| `--target_lang`          | 対象言語（既定値：`en`）                                              |
| `--model`                | 使用する特定のモデル                                             |
| `--eco`                  | エコノミーモデルを使用                                         |
| `--use_mistral`          | Mistral AI APIを使用                                                |
| `--use_claude`           | Claude APIを使用                                                    |
| `--use_gemini`           | Gemini APIを使用                                                    |
| `--use_codex`            | ChatGPTサブスクリプションのクォータでCodex CLIを使用               |
| `--use_grok`             | xAI API（Grok）を使用 — `XAI_API_KEY`が必要                      |
| `--use_grok_cli`         | GrokサブスクリプションのクォータでGrok CLIを使用                   |
| `--force`                | 再翻訳を強制                                                  |
| `--keep_filename`        | 元のファイル名を維持                                     |
| `--news`                 | ニュースモード：英語の引用を保護し、言語ごとの旗を処理 |
| `--add_translation_note` | 翻訳注記を追加                                           |
| `--note_position`        | 注記の位置：`top`、`bottom`（既定値）、または`both`                |
| `--note_format`          | 注記の形式：`legacy`（既定値、太字の段落）または`marker`       |
| `--include_model`        | 出力ファイルにモデル名を含める                       |
| `--reasoning_effort`     | GPT-5.xの推論エフォート：`none`/`low`/`medium`/`high`/`xhigh`     |

### 翻訳注記：位置と形式

`--add_translation_note`を使用すると、翻訳ツールは注記を先頭、末尾、または両方に配置でき、後方互換性のある単純なテキスト形式か、Markdownプラグインで利用可能な`marker`形式で出力できます。

**位置**（`--note_position`）：

- `bottom`（既定値）：従来どおり、ファイル末尾に注記を配置します。
- `top`：注記を**YAML frontmatterの後**に挿入します（Astro Content Collections、gray-matterなどとの安全性を確保）。
- `both`：注記を先頭と末尾の両方に挿入します（LLMの呼び出しは1回だけで、内容を両方の位置に再利用）。

**形式**（`--note_format`）：

- `legacy`（既定値）：太字の段落`**...**` — v1.8とバイト単位で完全に同一の動作です。Hugo、GitHub、GitLab、およびあらゆるMarkdown rendererと互換性があります。
- `marker`：非表示のMarkdown link reference definition（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）の後に、太字のblockquoteを配置します。GitHub/GitLabでそのまま読みやすく表示され、Astro側のremarkプラグインがビルド時に利用して、スタイル付きバナーを生成できます（blog jls42.orgを参照）。

```bash
# Compatibilité legacy (rien ne change vs v1.8)
python translate.py --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### 既定モデル（2026年）

| プロバイダー | 品質（既定値）       | エコノミー（`--eco`）    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **長文翻訳の推奨設定**：`--use_gemini`（既定値＝`gemini-3.7-flash`）は、非ラテン文字の言語（PL、JA、ZH、AR、HI）でもMarkdown構造を忠実に保持し、placeholderの忠実性が重要な`--news`モードにも対応します。このREADMEの日本語翻訳で測定した結果、`gemini-3.1-pro-preview`と同一の構造（21個のリスト、18個のコードブロック、13個のHTMLリンク、13個の画像、すべてのURLを保持）を、約6分の1のレイテンシで実現しました。後方互換性のため、既定のプロバイダーは引き続きOpenAIです。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** - 多言語対応の個人ブログ（15言語）

## 作者

Julien LE SAUX
メール：contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。[LICENSE](LICENSE)を参照してください。

**gpt-5.6-solを使用してフランス語から日本語に翻訳された記事。**
