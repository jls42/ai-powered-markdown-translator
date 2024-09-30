# OpenAI、Mistral AI、AnthropicのClaudeを使用したAI駆動のMarkdownトランスレーター

このプロジェクトは、OpenAI、Mistral AI、またはAnthropicのClaudeのAPIを使用して、Markdownファイルをソース言語からターゲット言語に翻訳する高度なPythonスクリプトです。柔軟性が高く使いやすいように設計されており、翻訳ノートの追加、改善された出力ファイル管理、既存ファイルの検出、複数の言語とトランスレーションモデルのサポートなどの追加オプションを提供しています。

デモンストレーションと詳細な説明については、[jls42.org](https://jls42.org/)または翻訳版の[jls42.org English](https://jls42.org/traductions_en/)、[jls42.org Español](https://jls42.org/traductions_es/)、[jls42.org 中文](https://jls42.org/traductions_zh/)をご覧ください。

## 主な特徴

- **AI駆動の翻訳**: OpenAI、Mistral AI、またはAnthropicのClaudeを使用して、最新のAI技術でドキュメントを翻訳します。
- **多言語サポート**: 異なる言語モデルをサポートして、ドキュメントを複数の言語に翻訳します。
- **インテリジェントな分割**: 自動分割により長文を効率的に処理します。
- **翻訳ノート**: 使用されたプロセスについて読者に通知するために、自動的に翻訳ノートを追加します。
- **改善された出力ファイル管理**: 翻訳を開始する前に、既存の翻訳があるかどうかを確認します。
- **改善された既存ファイル検出**: 元のファイル名のベース名とターゲット言語に一致するファイルを検索します。
- **柔軟で拡張可能**: 新機能の追加が容易になるように構造化されたコード。

## 前提条件

- Python 3.6以降。
- OpenAI、Mistral AI、またはAnthropicのClaudeの有効なAPIキー。

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

必要なAPIキーの環境変数を設定して環境を構成します：

- **OpenAI**：
    ```
    export OPENAI_API_KEY='あなたのopenai-api-key'
    ```
- **Mistral AI**：
    ```
    export MISTRAL_API_KEY='あなたのmistral-api-key'
    ```
- **AnthropicのClaude**：
    ```
    export ANTHROPIC_API_KEY='あなたのanthropic-api-key'
    ```

## 使用方法

スクリプトは翻訳プロセスをカスタマイズするためのいくつかのオプションを提供します：

### 一般的なオプション

- `--source_dir`：翻訳するMarkdownファイルを含むディレクトリ。
- `--target_dir`：翻訳されたファイルの出力ディレクトリ。
- `--model`：使用する翻訳GPTモデル。デフォルトのモデルは選択されたAPIによって異なります。
- `--source_lang`：ドキュメントのソース言語。特に翻訳ノートの追加に重要です。
- `--target_lang`：翻訳のターゲット言語。デフォルトは英語です。
- `--force`：ファイルの翻訳が既に存在する場合でも翻訳を強制します。

### API固有のオプション

- `--use_mistral`：翻訳にMistral AIのAPIを使用します。
- `--use_claude`：翻訳にAnthropicのClaudeのAPIを使用します。
- `--add_translation_note`：翻訳されたコンテンツに、使用された方法とツールを指定する翻訳ノートを追加します。

### 使用例

- OpenAIを使用してフランス語から英語に翻訳し、翻訳ノートを追加する：
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Mistral AIを使用してフランス語からスペイン語に翻訳し、翻訳ノートを追加しない：
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## 作者

Julien LE SAUX  
メール：contact@jls42.org

## ライセンス

このプロジェクトはGNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007のもとでライセンスされています。詳細については[LICENSE](LICENSE)ファイルをご覧ください。

**このドキュメントはモデルclaude-3-5-sonnet-20240620を使用してfrバージョンからja言語に翻訳されました。翻訳プロセスの詳細については、https://gitlab.com/jls42/ai-powered-markdown-translatorを参照してください。**

