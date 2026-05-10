# AI搭載 Markdown 翻訳ツール

🌍 [フランス語](README.md) | [英語](README-en.md) | [スペイン語](README-es.md) | [中国語](README-zh.md) | [ドイツ語](README-de.md) | [日本語](README-ja.md) | [韓国語](README-ko.md) | [アラビア語](README-ar.md) | [ヒンディー語](README-hi.md) | [イタリア語](README-it.md) | [オランダ語](README-nl.md) | [ポーランド語](README-pl.md) | [ポルトガル語](README-pt.md) | [ルーマニア語](README-ro.md) | [スウェーデン語](README-sv.md)

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="コードの悪臭"></a>
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

**OpenAI**、**Mistral AI**、**Claude（Anthropic）**、**Google Gemini** を使用する Markdown ファイル翻訳ツール。

この Python スクリプトは、Markdown ファイルをソース言語からターゲット言語へ翻訳しつつ、書式、コードブロック、front matter のメタデータを保持します。

## 主な機能

- **マルチプロバイダー**: 4つのAPI（OpenAI、Mistral、Claude、Gemini）をサポート
- **2026年モデル**: GPT-5.5、Claude Sonnet 4.6、Gemini 3.1 Pro
- **エコモード**: より高速で低コストなモデルを使うための `--eco` オプション
- **単一ファイル**: 1つのファイルだけを翻訳するための `--file` オプション
- **インテリジェントな分割**: モデルごとのトークン上限に対応した長文テキスト処理
- **コードの保持**: コードブロックとインラインコード（`` `...` ``）を保持
- **ファイル名**: 元の名前を保持するための `--keep_filename` オプション
- **News モード**: 英語の引用文を保護し、ニュース記事内の国旗を処理する `--news` オプション
- **.env 設定**: APIキー用の `.env` ファイルをサポート
- **翻訳ノート**: 文末に任意のノートを追加可能

## インストール

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 品質ツール（任意だが推奨）

このプロジェクトでは、フォーマット不備・脆弱性・秘密情報を含むコードのコミットを防ぐために [`pre-commit`](https://pre-commit.com) を使用しています。インストール:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

有効なフック: ruff（lint+format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（複雑性）、detect-secrets（APIキー）、mypy（段階的型付け）、Opengrep（SAST）、pip-audit（CVE 依存関係）、unittest。詳細は `CLAUDE.md` の _Quality / pre-commit_ セクションを参照してください。

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

### エコモード

より高速で低コストなモデル（gpt-5.4-mini、claude-haiku、gemini-flash）を使用します:

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### オプション

| オプション                 | 説明                                                                   |
| -------------------------- | ---------------------------------------------------------------------- |
| `--file`                 | 翻訳する単一の Markdown ファイル                                       |
| `--source_dir`           | Markdown ファイルを含むソースディレクトリ                              |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ                                      |
| `--source_lang`          | ソース言語（既定: `fr`）                                      |
| `--target_lang`          | ターゲット言語（既定: `en`）                                  |
| `--model`                | 使用する特定のモデル                                                   |
| `--eco`                  | エコモデルを使用する                                                   |
| `--use_mistral`          | Mistral AI API を使用する                                              |
| `--use_claude`           | Claude API を使用する                                                 |
| `--use_gemini`           | Gemini API を使用する                                                 |
| `--force`                | 再翻訳を強制する                                                       |
| `--keep_filename`        | 元のファイル名を保持する                                               |
| `--news`                 | News モード: EN 引用を保護し、言語ごとの国旗を処理                     |
| `--add_translation_note` | 翻訳ノートを追加する                                                   |
| `--note_position`        | ノートの位置: `top`、`bottom`（既定）、または `both` |
| `--note_format`          | ノートの形式: `legacy`（既定、太字段落）または `marker`    |
| `--include_model`        | 出力ファイルにモデル名を含める                                         |

### 翻訳ノート: 位置と形式

`--add_translation_note` を使うと、translator はノートを上部、下部、または両方に配置でき、形式はプレーンテキスト（旧互換）または Markdown プラグインで利用できる `marker` 形式のどちらかにできます。

**位置** (`--note_position`) :

- `bottom`（既定）: これまでどおり、ファイル末尾にノートを配置。
- `top`: ノートを **YAML frontmatter の後** に挿入（Astro Content Collections、gray-matter などの安全性対策）。
- `both`: ノートを先頭と末尾の両方に挿入（LLM 呼び出しは1回、内容は両方の配置に再利用）。

**形式** (`--note_format`) :

- `legacy`（既定）: 太字の `**...**` 段落 — v1.8 とバイト単位で完全に同一の動作。Hugo、GitHub、GitLab、その他すべての Markdown レンダラーと互換。
- `marker`: 可視化されない Markdown の link reference definition (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) に続く太字の blockquote。GitHub/GitLab ではネイティブに読め、Astro 側では remark プラグインでビルド時に利用してスタイライズされたバナーを生成可能（cf. blog jls42.org）。

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

| Provider | 品質（既定）         | エコ（`--eco`）            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **長文翻訳の推奨**: `--use_gemini`（既定 = 品質 `gemini-3.1-pro-preview`、`--eco` = `gemini-3.1-flash-lite-preview`）は、非ラテン文字のスクリプト（PL、JA、ZH、AR、HI）で Markdown 構造をよりよく保持する傾向があります。特にプレースホルダーの忠実性が重要な `--news` モードでは顕著です。後方互換性のため、OpenAI が引き続き既定です。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** - 多言語の個人ブログ（15言語）

## 著者

Julien LE SAUX  
Email : contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。 [LICENSE](LICENSE) を参照してください。

**gpt-5.4-miniによってfrからjaへ翻訳された記事。**
