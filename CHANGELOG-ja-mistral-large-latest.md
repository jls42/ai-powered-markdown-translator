### Changelog

- **1.0** 初期バージョン - OpenAI APIのサポート
- **1.1** Mistral AI APIのサポート追加
- **1.2** チェンジログの修正
- **1.3** 改善と新機能：
    - コードブロックの管理改善
    - 出力ファイルの管理改善
    - 既存ファイルの検出改善
    - 翻訳を強制するための `--force` オプション
    - 出力ファイル名におけるモデルと言語の逆転
- **1.4** 新機能：
    - AnthropicのClaude APIの翻訳サポート
    - プロンプトの最適化、明確性と効率の向上
    - コードのメンテナンスを改善するための細かい調整
- **1.5** 改善：
    - **APIキーとデフォルトモデルの更新：**
        - **OpenAI：** `DEFAULT_MODEL_OPENAI` を `"gpt-4o"` に更新。
        - **Mistral AI：** `DEFAULT_MODEL_MISTRAL` を `"mistral-large-latest"` に更新。
        - **AnthropicのClaude：** `DEFAULT_ANTHROPIC_API_KEY` の追加と `DEFAULT_MODEL_CLAUDE` を `"claude-3-5-sonnet-20240620"` に更新。
    - **翻訳プロンプトの最適化：**
        - 直接翻訳と翻訳メモのプロンプトが、明確性と効率を高めるために充実し、メタデータや特定のフォーマット要素の保持に関する詳細な指示が含まれる。
    - **コードのリファクタリング：**
        - `MistralClient` を `Mistral` クラスに置き換えて、Mistral AIクライアントの初期化。
        - インポートの再編成、可読性とメンテナンスの向上。
        - テキストのセグメントとコードブロックの管理を改善し、翻訳時に元のフォーマットを保持。
    - **出力ファイルの管理：**
        - 出力ファイル名におけるモデルと言語の逆転（例： `f"{base}-{args.target_lang}-{args.model}.md"`）、翻訳の整理と検索を容易に。
    - **その他の改善：**
        - 無駄な空行の削除によるコードのクリーンアップ。
        - スクリプトの構造と可読性を向上させるための細かい調整。

**Ce document a été traduit de la version fr vers la langue ja en utilisant le modèle mistral-large-latest. Pour plus d'informations sur le processus de traduction, consultez https://gitlab.com/jls42/ai-powered-markdown-translator**

