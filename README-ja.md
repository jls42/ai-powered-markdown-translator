# AI搭載 Markdown 翻訳ツール

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

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

**OpenAI**、**Mistral AI**、**Claude (Anthropic)**、**Google Gemini** を使用した Markdown ファイル翻訳ツール。

この Python スクリプトは、書式設定、コードブロック、front matter メタデータを保持しながら、Markdown ファイルをソース言語からターゲット言語へ翻訳します。

## 主な機能

- **マルチプロバイダー**: 4 つの API（OpenAI、Mistral、Claude、Gemini）に対応
- **2026 年モデル**: GPT-5.5、Claude Sonnet 4.6、Gemini 3.1 Pro
- **エコノミーモード**: `--eco` オプションで、より高速で低コストなモデルを使用
- **単一ファイル**: `--file` オプションで 1 つのファイルを翻訳
- **インテリジェントな分割**: モデルごとのトークン制限に合わせて長文を処理
- **コードの保持**: コードブロックとインラインコード（`` `...` ``）を保持
- **ファイル名**: `--keep_filename` オプションで元の名前を保持
- **ニュースモード**: `--news` オプションで英語の引用を保護し、ニュース記事内のフラグを処理
- **.env 設定**: API キー用の `.env` ファイルに対応
- **翻訳メモ**: ドキュメント末尾に任意でメモを追加

## インストール

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 品質ツール（任意だが推奨）

このプロジェクトでは、整形不良、脆弱性、秘密情報を含むコードのコミットを防ぐために [`pre-commit`](https://pre-commit.com) を使用します。インストール:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

有効なフック: ruff（lint+format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（複雑度）、detect-secrets（API キー）、mypy（段階的型付け）、Opengrep（SAST）、pip-audit（CVE 依存関係）、unittest。詳細は `CLAUDE.md` の _Quality / pre-commit_ セクションを参照してください。

## 設定

プロジェクトのルートに `.env` ファイルを作成するか、環境変数を設定してください:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## 使い方

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

### エコノミーモード

より高速で低コストなモデル（gpt-5.4-mini、claude-haiku、gemini-flash）を使用します:

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### オプション

| オプション               | 説明                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | 翻訳する単一の Markdown ファイル                                       |
| `--source_dir`           | Markdown ファイルを含むソースディレクトリ                        |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ                          |
| `--source_lang`          | ソース言語（デフォルト: `fr`）                                             |
| `--target_lang`          | ターゲット言語（デフォルト: `en`）                                              |
| `--model`                | 使用する特定のモデル                                             |
| `--eco`                  | エコノミーモデルを使用する                                         |
| `--use_mistral`          | Mistral AI API を使用する                                                |
| `--use_claude`           | Claude API を使用する                                                    |
| `--use_gemini`           | Gemini API を使用する                                                    |
| `--force`                | 再翻訳を強制する                                                  |
| `--keep_filename`        | 元のファイル名を保持する                                     |
| `--news`                 | ニュースモード: EN の引用を保護し、言語ごとのフラグを処理 |
| `--add_translation_note` | 翻訳メモを追加                                           |
| `--note_position`        | メモの位置: `top`、`bottom`（デフォルト）、または `both`                |
| `--note_format`          | メモの形式: `legacy`（デフォルト、太字の段落）または `marker`       |
| `--include_model`        | 出力ファイルにモデル名を含める                       |

### 翻訳メモ: 位置と形式

`--add_translation_note` を使うと、translator はメモを上部、下部、または両方に配置でき、プレーンテキスト形式（従来互換）または Markdown プラグインで利用できる `marker` 形式のいずれかにできます。

**位置** (`--note_position`) :

- `bottom`（デフォルト）: これまでどおり、ファイル末尾にメモを配置。
- `top` : メモを **YAML frontmatter の後** に挿入（Astro Content Collections、gray-matter などの安全性）。
- `both` : メモを先頭と末尾の両方に挿入（LLM 呼び出しは 1 回、内容は両方の配置で再利用）。

**形式** (`--note_format`) :

- `legacy`（デフォルト）: 太字の段落 `**...**` — v1.8 と byte-for-byte で厳密に同一の挙動。Hugo、GitHub、GitLab、その他すべての Markdown レンダラーに対応。
- `marker` : Markdown の非表示リンク参照定義 `[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"` に続く太字の blockquote。GitHub/GitLab ではネイティブに読め、Astro 側では remark プラグインによってビルド時に利用して、スタイリッシュなバナーを生成できます（jls42.org のブログを参照）。

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

| プロバイダー | 品質（デフォルト）         | エコノミー (`--eco`)            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **長文翻訳の推奨**: `--use_gemini`（デフォルト = `gemini-3.1-pro-preview` 品質、`--eco` = `gemini-3.1-flash-lite-preview`）は、非ラテン文字スクリプト（PL、JA、ZH、AR、HI）で Markdown 構造をよりよく保持する傾向があります。特にプレースホルダーの忠実性が重要な `--news` モードで有効です。後方互換性のため、OpenAI が引き続きデフォルトです。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** - 多言語の個人ブログ（15 言語）

## 作者

Julien LE SAUX
Email : contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](LICENSE) を参照。

**gpt-5.4-mini によって fr から ja に翻訳された記事。**
