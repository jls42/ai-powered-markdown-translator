# AI を活用した Markdown 翻訳ツール

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

**OpenAI**、**Mistral AI**、**Claude (Anthropic)**、**Google Gemini** を使用する Markdown ファイル翻訳ツールです。

この Python スクリプトは、Markdown ファイルをソース言語からターゲット言語へ翻訳し、書式、コードブロック、front matter のメタデータを保持します。

## 主な特徴

- **マルチプロバイダー**: 4 つの API（OpenAI、Mistral、Claude、Gemini）に対応
- **2026 年モデル**: GPT-5.5、Claude Sonnet 4.6、Gemini 3.1 Pro
- **低コストモード**: より高速で低コストなモデルを使用するための `--eco` オプション
- **単一ファイル**: 1 つのファイルだけを翻訳するための `--file` オプション
- **インテリジェントな分割**: モデルごとのトークン上限に応じて長文を処理
- **コードの保持**: コードブロックとインラインコード（`` `...` ``）を保持
- **ファイル名**: 元の名前を保持するための `--keep_filename` オプション
- **ニュースモード**: ニュース記事内の英語の引用を保護し、言語別のフラグを処理するための `--news` オプション
- **.env 設定**: API キー用の `.env` ファイルをサポート
- **翻訳メモ**: ドキュメント末尾に任意でメモを追加

## インストール

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 品質向上ツール（任意だが推奨）

このプロジェクトは、[`pre-commit`](https://pre-commit.com) を使用して、書式不良、脆弱性、または秘密情報を含むコードのコミットを防ぎます。インストール:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

有効なフック: ruff（lint+format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（複雑度）、detect-secrets（API キー）、mypy（段階的型付け）、Opengrep（SAST）、pip-audit（CVE 依存関係）、unittest。詳細は `CLAUDE.md` の _Quality / pre-commit_ セクションを参照してください。

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

### 低コストモード

より高速で低コストなモデル（gpt-5.4-mini、claude-haiku、gemini-flash）を使用します:

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### オプション

| オプション                | 説明                                                                   |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | 翻訳する単一の Markdown ファイル                                      |
| `--source_dir`           | Markdown ファイルを含むソースディレクトリ                               |
| `--target_dir`           | 翻訳後ファイルの出力先ディレクトリ                                       |
| `--source_lang`          | ソース言語（既定: `fr`）                                             |
| `--target_lang`          | ターゲット言語（既定: `en`）                                              |
| `--model`                | 使用する特定のモデル                                                |
| `--eco`                  | 低コストモデルを使用する                                         |
| `--use_mistral`          | Mistral AI API を使用する                                                |
| `--use_claude`           | Claude API を使用する                                                    |
| `--use_gemini`           | Gemini API を使用する                                                    |
| `--force`                | 再翻訳を強制する                                                  |
| `--keep_filename`        | 元のファイル名を保持する                                     |
| `--news`                 | ニュースモード: EN の引用を保護し、言語ごとのフラグを処理する |
| `--add_translation_note` | 翻訳メモを追加する                                           |
| `--include_model`        | 出力ファイルにモデル名を含める                       |

### デフォルトモデル（2026）

| Provider | 品質（既定）         | 低コスト（`--eco`）     |
| -------- | ------------------------ | ------------------------ |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`           |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5`       |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`   |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3-flash-preview` |

> **長文翻訳の推奨**: `--use_gemini`（既定 = 品質用 `gemini-3.1-pro-preview`、`--eco` = `gemini-3-flash-preview`）は、非ラテン文字のスクリプト（PL、JA、ZH、AR、HI）で Markdown 構造をよりよく保持する傾向があります。特に、プレースホルダーの忠実性が重要な `--news` モードで有効です。後方互換性のため、OpenAI が引き続き既定です。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** - 多言語パーソナルブログ（15 言語）

## 作者

Julien LE SAUX
Email : contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](LICENSE) を参照してください。

**この文書は、モデル gpt-5.4-mini を使用して fr 版から ja 言語へ翻訳されました。翻訳プロセスの詳細については、https://gitlab.com/jls42/ai-powered-markdown-translator をご覧ください。**

