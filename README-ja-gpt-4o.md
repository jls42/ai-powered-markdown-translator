# OpenAI、Mistral AI、およびAnthropicのClaudeを使用したMarkdown AIパワード翻訳者

このプロジェクトは、高度なPythonスクリプトで、OpenAI、Mistral AI、またはAnthropicのClaude APIを使用してMarkdownファイルをソース言語からターゲット言語へ翻訳します。柔軟で使いやすく、翻訳ノートの追加、出力ファイルの管理の改善、既存ファイルの検出、複数の言語と翻訳モデルのサポートなどの追加オプションを提供します。

デモンストレーションと詳細な説明については、[jls42.org](https://jls42.org/)または翻訳版を参照してください: [jls42.org English](https://jls42.org/traductions_en/), [jls42.org Español](https://jls42.org/traductions_es/) および [jls42.org 中文](https://jls42.org/traductions_zh/)。

## 主な特徴

- **AIパワード翻訳**: 最新のAI技術を使用して、OpenAI、Mistral AI、またはAnthropicのClaudeでドキュメントを翻訳します。
- **多言語サポート**: 複数の言語に対応し、異なる言語モデルをサポートしています。
- **インテリジェントなセグメンテーション**: 自動セグメンテーションにより、長文を効率的に管理します。
- **翻訳ノート**: 使用したプロセスに関する読者への情報を自動的に追加します。
- **出力ファイルの管理の改善**: 翻訳が既に存在するかどうかを確認してから翻訳を開始します。
- **既存ファイルの検出の改善**: 元のファイルのベースネームとターゲット言語に一致するファイルを検索します。
- **柔軟性と拡張性**: 新機能の追加が容易になるように構造化されています。

## 必要条件

- Python 3.6以降
- 有効なOpenAI、Mistral AI、またはAnthropicのClaude APIキー

## インストール

1. Gitリポジトリをクローンします：
```
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
```
2. 必要な依存関係をインストールします：
```
pip install -r requirements.txt
```

## 設定

必要なAPIキーのために環境変数を設定して環境を構成します：

- **OpenAI** :
    ```
    export OPENAI_API_KEY='あなたの-openai-api-key'
    ```
- **Mistral AI** :
    ```
    export MISTRAL_API_KEY='あなたの-mistral-api-key'
    ```
- **Claude d'Anthropic** :
    ```
    export ANTHROPIC_API_KEY='あなたの-anthropic-api-key'
    ```

## 使用方法

スクリプトは、翻訳プロセスをカスタマイズするための複数のオプションを提供します：

### 一般オプション

- `--source_dir` : 翻訳対象のMarkdownファイルを含むディレクトリ。
- `--target_dir` : 翻訳されたファイルの出力ディレクトリ。
- `--model` : 使用するGPT翻訳モデル。デフォルトモデルは選択されたAPIに依存します。
- `--source_lang` : ドキュメントのソース言語。翻訳ノートの追加に特に重要です。
- `--target_lang` : 翻訳のターゲット言語。デフォルトは英語です。
- `--force` : ファイルに既に翻訳が存在する場合でも、強制的に翻訳します。

### API特定のオプション

- `--use_mistral` : 翻訳にMistral AI APIを使用します。
- `--use_claude` : 翻訳にAnthropicのClaude APIを使用します。
- `--add_translation_note` : 使用された方法とツールを指定する翻訳ノートを翻訳内容に追加します。

### 使用例

- OpenAIを使用してフランス語から英語に翻訳し、翻訳ノートを追加する：
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Mistral AIを使用してフランス語からスペイン語に翻訳し、翻訳ノートを追加しない：
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## 著者

Julien LE SAUX  
Email : contact@jls42.org

## ライセンス

このプロジェクトはGNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007の下でライセンスされています。詳細については[LICENSE](LICENSE)ファイルを参照してください。

**このドキュメントは、fr バージョンから ja 言語に gpt-4o モデルを使用して翻訳されました。 翻訳プロセスの詳細については、https://gitlab.com/jls42/ai-powered-markdown-translator をご覧ください。**

