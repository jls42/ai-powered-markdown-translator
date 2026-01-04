### 変更履歴

🌍 [英語](CHANGELOG-en.md) | [スペイン語](CHANGELOG-es.md) | [中国語](CHANGELOG-zh.md) | [ドイツ語](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [韓国語](CHANGELOG-ko.md) | [アラビア語](CHANGELOG-ar.md) | [ヒンディー語](CHANGELOG-hi.md) | [イタリア語](CHANGELOG-it.md) | [オランダ語](CHANGELOG-nl.md) | [ポーランド語](CHANGELOG-pl.md) | [ポルトガル語](CHANGELOG-pt.md) | [ルーマニア語](CHANGELOG-ro.md) | [スウェーデン語](CHANGELOG-sv.md)

- **1.7** 新機能:
    - 翻訳時に元のファイル名を保持するためのオプション `--keep_filename`
    - APIキーを自動的に読み込むためのファイル `.env` のサポート
    - **インラインコードの保護**：バックティック（`` `...` ``）が翻訳中に保護されるようになりました
    - システムプロンプトの改善：
        - YAML frontmatter 内の引用符の扱いが改善されました
        - テンプレート変数 `{variable}` の保護
        - 未依頼の翻訳者注の禁止
    - 364ファイルでのテストに成功（ブログ移行 jls42.org）
- **1.6** 新機能：
    - 翻訳のためのGoogle Gemini APIのサポート（`--use_gemini`）
    - 2026年デフォルトモデルの更新：
        - OpenAI：`gpt-5`（高品質）、`gpt-5-mini`（エコ）
        - Claude：`claude-sonnet-4-5`（高品質）、`claude-haiku-4-5`（エコ）
        - Gemini：`gemini-3-pro-preview`（高品質）、`gemini-3-flash-preview`（エコ）
    - より高速かつ低コストなモデルを使用するためのエコモード（`--eco`）
    - ディレクトリを走査せずに単一ファイルを翻訳する機能（`--file`）
    - 新しい簡素化されたネーミングパターン：`{base}-{lang}.md`
    - モデル名を含む従来のフォーマットを保持するためのオプション `--include_model`
    - リストにないモデルのサポート（デフォルトのトークン上限：128k）
    - READMEが14言語に翻訳されました
- **1.5** 改善点：
    - **APIキーとデフォルトモデルの更新：**
        - **OpenAI：** `DEFAULT_MODEL_OPENAI` から `"gpt-4o"` へ更新。
        - **Mistral AI：** `DEFAULT_MODEL_MISTRAL` から `"mistral-large-latest"` へ更新。
        - **Anthropic の Claude：** `DEFAULT_ANTHROPIC_API_KEY` を追加し、`DEFAULT_MODEL_CLAUDE` から `"claude-3-5-sonnet-20240620"` へ更新。
    - **翻訳プロンプトの最適化：**
        - 直接翻訳および翻訳ノート用のプロンプトが、明確性と効率を高めるために強化され、メタデータや特定のフォーマット要素の保持に関する詳細な指示が含まれるようになりました。
    - **コードのリファクタリング：**
        - Mistral AI クライアント初期化のために `MistralClient` をクラス `Mistral` に置き換えました。
        - 可読性と保守性向上のためにインポートを再編成しました。
        - 翻訳中に元のフォーマットを保持するため、テキストの分割とコードブロックの処理を改善しました。
    - **出力ファイルの管理：**
        - 出力ファイル名におけるモデルと言語の順序を逆にしました（例：`f"{base}-{args.target_lang}-{args.model}.md"`）。これにより翻訳の整理と検索が容易になります。
    - **その他の改善：**
        - 不要な空行を削除してコードをクリーンアップしました。
        - スクリプトの構造と可読性を向上させるための細かな調整。
- **1.4** 新機能：
    - 翻訳のためのAnthropicのClaude APIサポート
    - 明確性と効率を高めるためのプロンプトの最適化
    - コードの保守性を向上させるための細かな調整
- **1.3** 改善点と新機能：
    - コードブロックの管理強化
    - 出力ファイル管理の改善
    - 既存ファイル検出の改善
    - 翻訳を強制するオプション `--force`
    - 出力ファイル名におけるモデルと言語の順序の反転
- **1.2** チェンジログの修正
- **1.1** Mistral AI API のサポートを追加
- **1.0** 初期バージョン - OpenAI API サポート

**この文書は gpt-5-mini モデルを使用して fr 版から ja 言語へ翻訳されました。翻訳プロセスの詳細については https://gitlab.com/jls42/ai-powered-markdown-translator をご覧ください。**

