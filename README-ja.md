# AI搭載Markdown翻訳ツール

🌍 [英語](README-en.md) | [スペイン語](README-es.md) | [中国語](README-zh.md) | [ドイツ語](README-de.md) | [日本語](README-ja.md) | [韓国語](README-ko.md) | [アラビア語](README-ar.md) | [ヒンディー語](README-hi.md) | [イタリア語](README-it.md) | [オランダ語](README-nl.md) | [ポーランド語](README-pl.md) | [ポルトガル語](README-pt.md) | [ルーマニア語](README-ro.md) | [スウェーデン語](README-sv.md)

OpenAI、Mistral AI、Claude（Anthropic）、Google Gemini を利用した Markdown ファイルの翻訳ツール。

この Python スクリプトは、ソース言語からターゲット言語へ Markdown ファイルを翻訳し、フォーマット、コードブロック、フロントマターのメタデータを保持します。

## 主な機能

- **マルチプロバイダー**: 4つの API をサポート（OpenAI、Mistral、Claude、Gemini）
- **2026年モデル**: GPT-5、Claude Sonnet 4.5、Gemini 3 Pro
- **省コストモード**: より高速で低コストなモデルを使用するためのオプション `--eco`
- **単一ファイル**: 単一ファイルを翻訳するオプション `--file`
- **スマート分割**: 各モデルのトークン制限に対応した長文の分割管理
- **コードの保持**: コードブロックとインラインコード（`` `...` ``）の両方を保持
- **ファイル名**: オリジナルのファイル名を保持するオプション `--keep_filename`
- **.env 設定**: APIキー用の `.env` ファイルをサポート
- **翻訳ノート**: ドキュメント末尾にオプションで翻訳ノートを追加

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

### 省コストモード

より高速で低コストなモデル（gpt-5-mini、claude-haiku、gemini-flash）を使用します：

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### オプション

| オプション | 説明 |
|--------|-------------|
| `--file` | 翻訳する単一の Markdown ファイル |
| `--source_dir` | ソースの Markdown ファイルが入ったディレクトリ |
| `--target_dir` | 翻訳後のファイルを出力するディレクトリ |
| `--source_lang` | ソース言語（デフォルト: `fr`） |
| `--target_lang` | ターゲット言語（デフォルト: `en`） |
| `--model` | 使用する特定のモデル |
| `--eco` | 省コストモデルを使用 |
| `--use_mistral` | Mistral AI API を使用 |
| `--use_claude` | Claude API を使用 |
| `--use_gemini` | Gemini API を使用 |
| `--force` | 再翻訳を強制 |
| `--keep_filename` | 元のファイル名を保持 |
| `--add_translation_note` | 翻訳ノートを追加 |
| `--include_model` | 出力ファイルにモデル名を含める |

### デフォルトモデル（2026）

| プロバイダー | 品質（デフォルト） | 省コスト（`--eco`） |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## このスクリプトを使用したプロジェクト

- **[jls42.org](https://jls42.org)** - 15言語に翻訳された個人ブログ

## 作成者

Julien LE SAUX  
メール : contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE バージョン 3。詳細は [ライセンス](LICENSE) を参照。

**この文書はフランス語（fr）版から日本語（ja）へgpt-5-miniモデルを使用して翻訳されました。翻訳プロセスの詳細については、https://gitlab.com/jls42/ai-powered-markdown-translator をご覧ください。**

