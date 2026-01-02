# AI搭載のMarkdown翻訳ツール

🌍 [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

**OpenAI**、**Mistral AI**、**Claude（Anthropic）**、**Google Gemini** を利用するMarkdownファイル翻訳ツール。

このPythonスクリプトは、書式、コードブロック、フロントマターのメタデータを保持しながら、ソース言語からターゲット言語へMarkdownファイルを翻訳します。

## 主な機能

- **マルチプロバイダー**: 4つのAPIに対応（OpenAI、Mistral、Claude、Gemini）
- **2026年モデル**: GPT-5、Claude Sonnet 4.5、Gemini 3 Pro
- **エコノミーモード**: より高速で低コストなモデルを使用するための `--eco` オプション
- **単一ファイル**: 1つのファイルのみを翻訳する `--file` オプション
- **スマート分割**: モデルごとのトークン制限に合わせた長文の分割処理
- **コード保護**: コードブロックは翻訳しません
- **翻訳ノート**: ドキュメント末尾にノートを任意で追加

## インストール

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## 設定

使用したいAPIの環境変数を設定してください：

```bash
export OPENAI_API_KEY='votre-clé-api-openai'
export MISTRAL_API_KEY='votre-clé-api-mistral'
export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
export GOOGLE_API_KEY='votre-clé-api-google'
```

## 使い方

### 単一ファイルを翻訳

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### ディレクトリを翻訳

```bash
# Avec OpenAI (défaut: gpt-5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### エコノミーモード

より高速で低コストなモデルを使用します（gpt-5-mini、claude-haiku、gemini-flash）：

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### オプション

| オプション | 説明 |
|--------|-------------|
| `--file` | 翻訳する単一のMarkdownファイル |
| `--source_dir` | Markdownファイルを含むソースディレクトリ |
| `--target_dir` | 翻訳結果の出力ディレクトリ |
| `--source_lang` | ソース言語（デフォルト: `fr`） |
| `--target_lang` | ターゲット言語（デフォルト: `en`） |
| `--model` | 使用する特定のモデル |
| `--eco` | エコノミーモデルを使用する |
| `--use_mistral` | Mistral AI APIを使用する |
| `--use_claude` | Claude APIを使用する |
| `--use_gemini` | Gemini APIを使用する |
| `--force` | 再翻訳を強制する |
| `--add_translation_note` | 翻訳ノートを追加する |

### デフォルトのモデル（2026）

| Provider | 品質（デフォルト） | エコノミー（`--eco`） |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## 著者

Julien LE SAUX
メール: contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。 [LICENSE](LICENSE) を参照。