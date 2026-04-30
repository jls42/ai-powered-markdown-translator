# AI搭載 Markdown 翻訳ツール

🌍 [フランス語](README.md) | [英語](README-en.md) | [スペイン語](README-es.md) | [中国語](README-zh.md) | [ドイツ語](README-de.md) | [日本語](README-ja.md) | [韓国語](README-ko.md) | [アラビア語](README-ar.md) | [ヒンディー語](README-hi.md) | [イタリア語](README-it.md) | [オランダ語](README-nl.md) | [ポーランド語](README-pl.md) | [ポルトガル語](README-pt.md) | [ルーマニア語](README-ro.md) | [スウェーデン語](README-sv.md)

**OpenAI**、**Mistral AI**、**Claude (Anthropic)**、**Google Gemini** を使用する Markdown ファイル翻訳ツールです。

この Python スクリプトは、書式設定、コードブロック、front matter のメタデータを保持しながら、Markdown ファイルをソース言語からターゲット言語へ翻訳します。

## 主な機能

- **マルチプロバイダー**: 4 つの API（OpenAI、Mistral、Claude、Gemini）に対応
- **2026 年モデル**: GPT-5.5、Claude Sonnet 4.6、Gemini 3.1 Pro
- **省コストモード**: より高速で低コストのモデルを使用するための `--eco` オプション
- **単一ファイル**: 1 つのファイルを翻訳するための `--file` オプション
- **スマートな分割**: モデルごとの token 上限に応じた長文処理
- **コードの保持**: コードブロックとインラインコード（`` `...` ``）を保持
- **ファイル名**: 元の名前を保持するための `--keep_filename` オプション
- **News モード**: 記事内の英語の引用を保護し、言語ごとの旗を扱うための `--news` オプション
- **.env 設定**: API キー用の `.env` ファイルをサポート
- **翻訳メモ**: 文書末尾に任意のメモを追加

## インストール

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 品質向上ツール（任意ですが推奨）

このプロジェクトでは、[`pre-commit`](https://pre-commit.com) を使って、整形不良、脆弱、または秘密情報を含むコードのコミットを防ぎます。インストール方法：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

有効なフック: ruff（lint+format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（複雑度）、detect-secrets（API キー）、mypy（段階的型付け）、Opengrep（SAST）、pip-audit（CVE 依存関係）、unittest。詳細は `CLAUDE.md` の _Quality / pre-commit_ セクションを参照してください。

## 設定

プロジェクトのルートに `.env` ファイルを作成するか、環境変数を設定してください：

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

### 単一ファイルの翻訳

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### ディレクトリの翻訳

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

より高速で低コストのモデル（gpt-5.4-mini、claude-haiku、gemini-flash）を使用します：

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### オプション

| オプション                | 説明                                                                 |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | 翻訳する単一の Markdown ファイル                                      |
| `--source_dir`           | Markdown ファイルを含むソースディレクトリ                              |
| `--target_dir`           | 翻訳済みファイルの出力先ディレクトリ                                    |
| `--source_lang`          | ソース言語（既定: `fr`）                                     |
| `--target_lang`          | ターゲット言語（既定: `en`）                                  |
| `--model`                | 使用する特定のモデル                                                |
| `--eco`                  | 省コストモデルを使用する                                            |
| `--use_mistral`          | Mistral AI API を使用する                                            |
| `--use_claude`           | Claude API を使用する                                                |
| `--use_gemini`          | Gemini API を使用する                                                |
| `--force`                | 再翻訳を強制する                                                  |
| `--keep_filename`        | 元のファイル名を保持する                                           |
| `--news`                 | ニュースモード: EN の引用を保護し、言語別の旗を処理する             |
| `--add_translation_note` | 翻訳メモを追加する                                                     |
| `--include_model`        | 出力ファイル名にモデル名を含める                                    |

### 既定モデル（2026）

| Provider | 品質（既定）         | 省コスト（`--eco`）     |
| -------- | ------------------------ | ------------------------ |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`           |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5`       |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`   |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3-flash-preview` |

> **長文翻訳の推奨**: `--use_gemini`（既定 = `gemini-3.1-pro-preview` 品質、`--eco` = `gemini-3-flash-preview`）は、非ラテン文字のスクリプト（PL、JA、ZH、AR、HI）において markdown 構造をよりよく保持する傾向があります。特に `--news` モードではプレースホルダの忠実性が重要です。下位互換性のため、OpenAI が引き続き既定です。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** - 多言語の個人ブログ（15 言語）

## 作者

ジュリアン・ル・ソー
メール: contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](LICENSE) を参照してください。

**この文書は、gpt-5.4-mini モデルを使用して fr 版から ja 言語へ翻訳されました。翻訳プロセスの詳細については、https://github.com/jls42/ai-powered-markdown-translator をご覧ください。**
