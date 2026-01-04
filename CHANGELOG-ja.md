### 更新履歴

🌍 [英語](CHANGELOG-en.md) | [スペイン語](CHANGELOG-es.md) | [中国語](CHANGELOG-zh.md) | [ドイツ語](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [韓国語](CHANGELOG-ko.md) | [アラビア語](CHANGELOG-ar.md) | [ヒンディー語](CHANGELOG-hi.md) | [イタリア語](CHANGELOG-it.md) | [オランダ語](CHANGELOG-nl.md) | [ポーランド語](CHANGELOG-pl.md) | [ポルトガル語](CHANGELOG-pt.md) | [ルーマニア語](CHANGELOG-ro.md) | [スウェーデン語](CHANGELOG-sv.md)

- **1.7** 新機能：
    - 翻訳時に元のファイル名を保持するオプション `--keep_filename`
    - APIキーを自動で読み込むためのファイル `.env` のサポート
    - **インラインコードの保持** : les backticks (`` `...` ``) sont maintenant protégés pendant la traduction
    - システムプロンプトの改善：
        - YAML frontmatter内の引用符の管理が改善
        - テンプレート変数 `{variable}` の保護
        - 要求されていない翻訳者の注釈を禁止
    - jls42.org ブログの移行で 364 ファイルに対して正常にテスト済み
- **1.6** 新機能：
    - 翻訳のための Google Gemini API のサポート（`--use_gemini`）
    - 2026年デフォルトモデルの更新：
        - OpenAI：`gpt-5`（高品質）、`gpt-5-mini`（エコ）
        - Claude：`claude-sonnet-4-5`（高品質）、`claude-haiku-4-5`（エコ）
        - Gemini：`gemini-3-pro-preview`（高品質）、`gemini-3-flash-preview`（エコ）
    - より高速で低コストなモデルを使用するための省エネモード（`--eco`）
    - ディレクトリを走査せずに単一ファイルを翻訳する機能（`--file`）
    - 新しい簡略化された命名パターン：`{base}-{lang}.md`
    - モデル名を含む旧フォーマットを保持するオプション `--include_model`
    - リストにないモデルのサポート（デフォルトのトークン上限：128k）
    - README を14言語に翻訳
- **1.5** 改良点：
    - **APIキーとデフォルトモデルの更新：**
        - **OpenAI：** `DEFAULT_MODEL_OPENAI` から `"gpt-4o"` へ更新。
        - **Mistral AI：** `DEFAULT_MODEL_MISTRAL` から `"mistral-large-latest"` へ更新。
        - **Anthropic の Claude：** `DEFAULT_ANTHROPIC_API_KEY` の追加と `DEFAULT_MODEL_CLAUDE` から `"claude-3-5-sonnet-20240620"` への更新。
    - **翻訳プロンプトの最適化：**
        - 直接翻訳および翻訳注記用のプロンプトが、メタデータや特定のフォーマット要素の保持に関する詳細な指示を含め、より明確かつ効率的になるよう強化されました。
    - **コードのリファクタリング：**
        - Mistral AI クライアントの初期化において `MistralClient` をクラス `Mistral` に置換。
        - 可読性と保守性向上のためインポートの再編成。
        - 翻訳時に元のフォーマットを維持するためのテキスト分割とコードブロックの取り扱いを改善。
    - **出力ファイルの管理：**
        - 出力ファイル名でモデルと言語の順序を逆に（例：`f"{base}-{args.target_lang}-{args.model}.md"`）、翻訳の整理と検索を容易にしました。
    - **その他の改善：**
        - 不要な空行を削除してコードをクリーンアップしました。
        - スクリプトの構造と可読性を向上させるための小規模な調整。
- **1.4** 新機能：
    - 翻訳のための Anthropic Claude API のサポート
    - 明確さと効率を高めるためのプロンプト最適化
    - コード保守性を向上させるための小さな調整
- **1.3** 改良と新機能：
    - コードブロックの取り扱いの改善
    - 出力ファイル管理の改善
    - 既存ファイル検出の改善
    - 翻訳を強制するオプション `--force`
    - 出力ファイル名でモデルと言語の順序を逆にする変更
- **1.2** 変更履歴の修正
- **1.1** Mistral AI API サポートの追加
- **1.0** 初期版 - OpenAI API のサポート

**この文書は gpt-5-mini モデルを使用して fr バージョンから ja 言語に翻訳されました。翻訳プロセスの詳細については https://gitlab.com/jls42/ai-powered-markdown-translator をご覧ください。**

