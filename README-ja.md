# AI搭載 Markdown 翻訳ツール

🌍 [フランス語](README.md) | [英語](README-en.md) | [スペイン語](README-es.md) | [中国語](README-zh.md) | [ドイツ語](README-de.md) | [日本語](README-ja.md) | [韓国語](README-ko.md) | [アラビア語](README-ar.md) | [ヒンディー語](README-hi.md) | [イタリア語](README-it.md) | [オランダ語](README-nl.md) | [ポーランド語](README-pl.md) | [ポルトガル語](README-pt.md) | [ルーマニア語](README-ro.md) | [スウェーデン語](README-sv.md)

<h4 align="center">📊 コード品質</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="品質ゲートの状態"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="セキュリティレーティング"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="信頼性レーティング"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="保守性レーティング"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="カバレッジ"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="脆弱性"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="バグ"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="コードスメル"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="重複行率 (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="技術的負債"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="コード行数"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy バッジ"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

**OpenAI**、**Mistral AI**、**Claude (Anthropic)**、**Google Gemini** を使用する Markdown ファイル翻訳ツール。

この Python スクリプトは、Markdown ファイルをソース言語からターゲット言語へ翻訳しつつ、書式、コードブロック、front matter メタデータを保持します。

## 主な機能

- **マルチプロバイダー**: 4 つの API（OpenAI、Mistral、Claude、Gemini）に対応
- **2026 年モデル**: GPT-5.5、Claude Sonnet 4.6、Gemini 3.1 Pro
- **省コストモード**: より高速で低コストなモデルを使うための `--eco` オプション
- **単一ファイル**: 1 つのファイルだけを翻訳するための `--file` オプション
- **インテリジェントな分割**: モデルごとのトークン上限を考慮した長文テキストの処理
- **コード保持**: コードブロックとインラインコード（`` `...` ``）を保持
- **ファイル名**: 元のファイル名を保持するための `--keep_filename` オプション
- **News モード**: 英語の引用文を保護し、ニュース記事で言語別の国旗を処理するための `--news` オプション
- **.env 設定**: API キー用の `.env` ファイルに対応
- **翻訳注記**: ドキュメント末尾にオプションの注記を追加

## インストール

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 品質ツール（オプションだが推奨）

このプロジェクトは、フォーマット不良、脆弱、またはシークレットを含むコードがコミットされるのを防ぐために [`pre-commit`](https://pre-commit.com) を使用します。インストール:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

有効なフック: ruff（lint+format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（複雑度）、detect-secrets（API キー）、mypy（段階的型付け）、Opengrep（SAST）、pip-audit（依存関係の CVE）、unittest。詳細は `CLAUDE.md` の _品質 / pre-commit_ セクションを参照してください。

## 設定

プロジェクトのルートに `.env` ファイルを作成するか、環境変数を定義してください:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## 使用方法

### 単一ファイルを翻訳する

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### ディレクトリを翻訳する

```bash
# Avec OpenAI (défaut: gpt-5.5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### 省コストモード

より高速で低コストなモデル（gpt-5.4-mini、claude-haiku、gemini-flash）を使用します:

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### オプション

| オプション                 | 説明                                                                 |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | 翻訳する単一の Markdown ファイル                                       |
| `--source_dir`           | Markdown ファイルを含むソースディレクトリ                               |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ                                      |
| `--source_lang`          | ソース言語（既定: `fr`）                                             |
| `--target_lang`          | ターゲット言語（既定: `en`）                                              |
| `--model`                | 使用する特定のモデル                                                   |
| `--eco`                  | 省コストモデルを使用                                                   |
| `--use_mistral`          | Mistral AI API を使用                                                  |
| `--use_claude`           | Claude API を使用                                                     |
| `--use_gemini`          | Gemini API を使用                                                     |
| `--force`                | 再翻訳を強制                                                        |
| `--keep_filename`        | 元のファイル名を保持                                                |
| `--news`                 | News モード: 英語の引用を保護し、言語ごとの国旗を処理           |
| `--add_translation_note` | 翻訳注記を追加                                           |
| `--note_position`        | 注記の位置: `top`, `bottom`（既定）、または `both`                |
| `--note_format`          | 注記の形式: `legacy`（既定、太字の段落）または `marker`       |
| `--include_model`        | 出力ファイルにモデル名を含める                       |

### 翻訳注記: 位置と形式

`--add_translation_note` を使うと、翻訳ツールは注記を上部、下部、または両方に配置でき、プレーンテキスト形式（旧互換）または Markdown プラグインで利用できる `marker` 形式のいずれかで出力できます。

**位置**（`--note_position`）:

- `bottom`（既定）: これまでどおり、注記をファイル末尾に配置。
- `top`: YAML frontmatter の後に注記を挿入（Astro Content Collections、gray-matter などの安全性）。
- `both`: 上部と下部の両方に注記を挿入（LLM 呼び出し 1 回、内容は両配置で再利用）。

**形式**（`--note_format`）:

- `legacy`（既定）: 太字の段落 `**...**` — v1.8 と byte-for-byte で厳密に同一の動作。Hugo、GitHub、GitLab、およびあらゆる Markdown レンダラーと互換。
- `marker`: Markdown の不可視なリンク参照定義 (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) に続く太字の blockquote。GitHub/GitLab ではそのまま読め、Astro 側では remark プラグインによってビルド時に利用し、スタイル付きバナーを生成できます（jls42.org のブログ参照）。

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

### 既定モデル（2026）

| プロバイダー | 品質（既定）         | 省コスト（`--eco`）            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **長文翻訳の推奨**: `--use_gemini`（既定 = `gemini-3.1-pro-preview` 品質、`--eco` = `gemini-3.1-flash-lite-preview`）は、非ラテン文字スクリプト（PL、JA、ZH、AR、HI）において Markdown の構造をよりよく保持する傾向があります。特に `--news` モードでは、プレースホルダーの忠実性が重要です。OpenAI は後方互換性のために既定のままです。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** - 多言語の個人ブログ（15 言語）

## 著者

Julien LE SAUX  
メール: contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。[LICENSE](LICENSE) を参照。

**fr から ja へ gpt-5.4-mini で翻訳された記事。**
