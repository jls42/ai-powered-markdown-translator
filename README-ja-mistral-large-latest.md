# AI搭載マークダウン翻訳ツール、OpenAI、Mistral AI、およびAnthropicのClaude

このプロジェクトは、OpenAI、Mistral AI、またはAnthropicのClaudeのAPIを使用して、マークダウンファイルをソース言語からターゲット言語に翻訳する高度なPythonスクリプトです。フレキシブルで使いやすく、翻訳ノートの追加、出力ファイルの管理の向上、ファイルの存在検出、複数の言語と翻訳モデルのサポートなどの追加オプションを提供します。

詳細なデモと説明については、[jls42.org](https://jls42.org/)または翻訳版：[jls42.org English](https://jls42.org/traductions_en/)、[jls42.org Español](https://jls42.org/traductions_es/)、[jls42.org 中文](https://jls42.org/traductions_zh/)を訪問してください。

## 主な特徴

- **AI搭載翻訳**：OpenAI、Mistral AI、またはAnthropicのClaudeを使用して、最新のAI技術でドキュメントを翻訳します。
- **多言語対応**：複数の言語でドキュメントを翻訳し、さまざまな言語モデルに対応します。
- **スマートセグメンテーション**：自動セグメント化により、長いテキストを効率的に管理します。
- **翻訳ノート**：翻訳プロセスに使用された方法とツールについて読者に知らせるために、自動的に翻訳ノートを追加します。
- **出力ファイルの管理の向上**：翻訳を開始する前に、翻訳が既に存在するかどうかを確認します。
- **ファイル存在検出の向上**：元のファイルのベース名とターゲット言語に一致するファイルを検索します。
- **フレキシブルで拡張性のある**：コードは新しい機能を追加しやすく構成されています。

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

必要なAPIキーの環境変数を設定して、環境を構成します：

- **OpenAI**：
    ```
    export OPENAI_API_KEY='votre-clé-api-openai'
    ```
- **Mistral AI**：
    ```
    export MISTRAL_API_KEY='votre-clé-api-mistral'
    ```
- **AnthropicのClaude**：
    ```
    export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
    ```

## 使用方法

スクリプトは、翻訳プロセスをカスタマイズするためのさまざまなオプションを提供します：

### 一般的なオプション

- `--source_dir`：翻訳するマークダウンファイルが含まれているディレクトリ。
- `--target_dir`：翻訳されたファイルの出力ディレクトリ。
- `--model`：使用するGPT翻訳モデル。デフォルトのモデルは選択されたAPIに依存します。
- `--source_lang`：ドキュメントのソース言語。翻訳ノートの追加に特に重要です。
- `--target_lang`：翻訳のターゲット言語。デフォルトは英語です。
- `--force`：ファイルに既に翻訳が存在している場合でも翻訳を強制します。

### API固有のオプション

- `--use_mistral`：Mistral AI APIを翻訳に使用します。
- `--use_claude`：AnthropicのClaude APIを翻訳に使用します。
- `--add_translation_note`：翻訳されたコンテンツに翻訳ノートを追加し、使用された方法とツールを指定します。

### 使用例

- OpenAIを使用して、翻訳ノートを追加してフランス語から英語に翻訳する：
    ```
    python translate.py --source_dir 'content/fr' --target_dir 'content/en' --add_translation_note --source_lang 'fr'
    ```
- Mistral AIを使用して、翻訳ノートなしでフランス語からスペイン語に翻訳する：
    ```
    python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'
    ```

## 著者

Julien LE SAUX
メール：contact@jls42.org

## ライセンス

このプロジェクトは、GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007のライセンスの下にあります。詳細については、[LICENSE](LICENSE)ファイルを参照してください。

**Ce document a été traduit de la version fr vers la langue ja en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator.**

