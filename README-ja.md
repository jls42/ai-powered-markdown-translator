# AI搭載 Markdown 翻訳ツール

🌍 [フランス語](README.md) | [英語](README-en.md) | [スペイン語](README-es.md) | [中国語](README-zh.md) | [ドイツ語](README-de.md) | [日本語](README-ja.md) | [韓国語](README-ko.md) | [アラビア語](README-ar.md) | [ヒンディー語](README-hi.md) | [イタリア語](README-it.md) | [オランダ語](README-nl.md) | [ポーランド語](README-pl.md) | [ポルトガル語](README-pt.md) | [ルーマニア語](README-ro.md) | [スウェーデン語](README-sv.md)

OpenAI、Mistral AI、Claude（Anthropic）、Google Geminiを利用するMarkdownファイルの翻訳ツール。

このPythonスクリプトは、フォーマット、コードブロック、フロントマターのメタデータを保持したまま、ソース言語からターゲット言語へMarkdownファイルを翻訳します。

## 主な特徴

- **マルチプロバイダー**: 4つのAPI（OpenAI、Mistral、Claude、Gemini）をサポート
- **2026年モデル**: GPT-5、Claude Sonnet 4.5、Gemini 3 Pro
- **エコノミーモード**: より高速で低コストなモデルを使用するオプション `--eco`
- **単一ファイル**: 単一ファイルを翻訳するオプション `--file`
- **スマートセグメンテーション**: モデルごとのトークン制限に対応した長文の処理
- **コードの保持**: コードブロックおよびインラインコード（`` `...` ``）は保持されます
- **ファイル名**: 元の名前を保持するオプション `--keep_filename`
- **ニュースモード**: 英語の引用を保護し、ニュース記事内のフラグを言語ごとに処理するオプション `--news`
- **.env 設定**: APIキー用のファイル `.env` をサポート
- **翻訳ノート**: ドキュメント末尾に翻訳ノートを任意で追加

## インストール

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## 設定

プロジェクトルートに `.env` ファイルを作成するか、環境変数を設定してください：

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

より高速で低コストなモデル（gpt-5-mini、claude-haiku、gemini-flash）を使用します：

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### オプション

| オプション | 説明 |
|--------|-------------|
| `--file` | 翻訳する単一のMarkdownファイル |
| `--source_dir` | Markdownファイルを含むソースディレクトリ |
| `--target_dir` | 翻訳後ファイルの出力ディレクトリ |
| `--source_lang` | ソース言語（デフォルト: `fr`） |
| `--target_lang` | ターゲット言語（デフォルト: `en`） |
| `--model` | 使用する特定のモデル |
| `--eco` | エコノミーモデルを使用 |
| `--use_mistral` | Mistral AI APIを使用 |
| `--use_claude` | Claude APIを使用 |
| `--use_gemini` | Gemini APIを使用 |
| `--force` | 再翻訳を強制 |
| `--keep_filename` | 元のファイル名を保持 |
| `--news` | ニュースモード：英語の引用を保護し、言語ごとにフラグを管理 |
| `--add_translation_note` | 翻訳ノートを追加 |
| `--include_model` | 出力ファイルにモデル名を含める |

### デフォルトモデル (2026)

| プロバイダー | 品質（デフォルト） | エコノミー（`--eco`） |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## 本スクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** - 多言語個人ブログ（15言語）

## 著者

Julien LE SAUX  
メール : contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE バージョン3。参照 [ライセンス](LICENSE).

**この文書は gpt-5-mini モデルを使用して fr バージョンから ja 言語へ翻訳されました。翻訳プロセスの詳細については、https://gitlab.com/jls42/ai-powered-markdown-translator をご覧ください。**

