# AI搭載Markdown翻訳ツール

🌍 [英語](README-en.md) | [スペイン語](README-es.md) | [中国語](README-zh.md) | [ドイツ語](README-de.md) | [日本語](README-ja.md) | [韓国語](README-ko.md) | [アラビア語](README-ar.md) | [ヒンディー語](README-hi.md) | [イタリア語](README-it.md) | [オランダ語](README-nl.md) | [ポーランド語](README-pl.md) | [ポルトガル語](README-pt.md) | [ルーマニア語](README-ro.md) | [スウェーデン語](README-sv.md)

OpenAI、Mistral AI、Claude（Anthropic）、Google Gemini を使用する Markdown ファイル翻訳ツール。

この Python スクリプトは、ソース言語からターゲット言語へ Markdown ファイルを翻訳し、フォーマット、コードブロック、フロントマターのメタデータを保持します。

## 主な特徴

- **マルチプロバイダー**: 4つのAPIをサポート（OpenAI、Mistral、Claude、Gemini）
- **2026年モデル**: GPT-5、Claude Sonnet 4.5、Gemini 3 Pro
- **省コストモード**: より高速で安価なモデルを使用するためのオプション `--eco`
- **単一ファイル**: 1つのファイルを翻訳するためのオプション `--file`
- **スマート分割**: モデルごとのトークン制限に対応した長文処理
- **コードの保持**: コードブロックとインラインコード（`` `...` ``）は保持されます
- **ファイル名**: 元の名前を保持するためのオプション `--keep_filename`
- **.env 設定**: API キー用のファイル `.env` をサポート
- **翻訳注記**: ドキュメント末尾への注記の任意追加

## インストール

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## 設定

プロジェクトのルートに `.env` ファイルを作成するか、環境変数を設定してください :

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
# Avec OpenAI (défaut: gpt-5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### 省コストモード

より高速で安価なモデル（gpt-5-mini、claude-haiku、gemini-flash）を使用します :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### オプション

| オプション | 説明 |
|--------|-------------|
| `--file` | 翻訳する単一のMarkdownファイル |
| `--source_dir` | Markdownファイルを含むソースディレクトリ |
| `--target_dir` | 翻訳済みファイルの出力ディレクトリ |
| `--source_lang` | ソース言語（デフォルト: `fr`） |
| `--target_lang` | 対象言語（デフォルト: `en`） |
| `--model` | 使用する特定モデル |
| `--eco` | 省コストモデルを使用 |
| `--use_mistral` | Mistral AI API を使用 |
| `--use_claude` | Claude API を使用 |
| `--use_gemini` | Gemini API を使用 |
| `--force` | 再翻訳を強制 |
| `--keep_filename` | 元のファイル名を保持 |
| `--add_translation_note` | 翻訳注記を追加 |
| `--include_model` | 出力ファイルにモデル名を含める |

### デフォルトモデル（2026）

| プロバイダー | 品質（デフォルト） | 省コスト（`--eco`） |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** - 多言語個人ブログ（15言語）

## 作者

Julien LE SAUX  
メール : contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE バージョン 3。詳細は [ライセンス](LICENSE) を参照。

**この文書は gpt-5-mini モデルを使用して fr バージョンから ja 言語に翻訳されました。翻訳プロセスの詳細については https://gitlab.com/jls42/ai-powered-markdown-translator をご覧ください。**

