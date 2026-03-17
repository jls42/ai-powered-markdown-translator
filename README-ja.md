# AI搭載 Markdown 翻訳ツール

🌍 [Français](README.md) | [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

**OpenAI**、**Mistral AI**、**Claude (Anthropic)**、**Google Gemini** を使用する Markdown ファイル翻訳ツールです。

この Python スクリプトは、書式、コードブロック、front matter メタデータを保持しながら、Markdown ファイルをソース言語からターゲット言語へ翻訳します。

## 主な特徴

- **マルチプロバイダー**: 4 つの API（OpenAI、Mistral、Claude、Gemini）に対応
- **2026年モデル**: GPT-5.4、Claude Sonnet 4.5、Gemini 3.1 Pro
- **低コストモード**: より高速で低コストなモデルを使用するための `--eco` オプション
- **単一ファイル**: 1 つのファイルだけを翻訳するための `--file` オプション
- **インテリジェントな分割**: モデルごとのトークン上限に対応した長文処理
- **コードの保持**: コードブロックとインラインコード（`` `...` ``）を保持
- **ファイル名**: 元の名前を保持するための `--keep_filename` オプション
- **News モード**: ニュース記事内の英語引用を保護し、フラグを処理するための `--news` オプション
- **.env 設定**: API キー用の `.env` ファイルをサポート
- **翻訳メモ**: 文書末尾に任意のメモを追加

## インストール

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

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

## 使い方

### 単一ファイルを翻訳する

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### ディレクトリを翻訳する

```bash
# Avec OpenAI (défaut: gpt-5.4)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### 低コストモード

より高速で低コストなモデル（gpt-5-mini、claude-haiku、gemini-flash）を使用します：

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### オプション

| オプション | 説明 |
|--------|-------------|
| `--file` | 翻訳対象の単一 Markdown ファイル |
| `--source_dir` | Markdown ファイルを含むソースディレクトリ |
| `--target_dir` | 翻訳済みファイルの出力ディレクトリ |
| `--source_lang` | ソース言語（デフォルト: `fr`） |
| `--target_lang` | ターゲット言語（デフォルト: `en`） |
| `--model` | 使用する特定のモデル |
| `--eco` | 低コストモデルを使用 |
| `--use_mistral` | Mistral AI API を使用 |
| `--use_claude` | Claude API を使用 |
| `--use_gemini` | Gemini API を使用 |
| `--force` | 再翻訳を強制 |
| `--keep_filename` | 元のファイル名を保持 |
| `--news` | ニュースモード: EN 引用を保護し、言語ごとにフラグを処理 |
| `--add_translation_note` | 翻訳メモを追加 |
| `--include_model` | 出力ファイルにモデル名を含める |

### デフォルトモデル（2026）

| Provider | 品質（デフォルト） | 低コスト (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** - 多言語個人ブログ（15言語）

## 作者

Julien LE SAUX  
Email : contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3. [LICENSE](LICENSE) を参照。