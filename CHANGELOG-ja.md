### 変更履歴

🌍 [フランス語](CHANGELOG.md) | [英語](CHANGELOG-en.md) | [スペイン語](CHANGELOG-es.md) | [中国語](CHANGELOG-zh.md) | [ドイツ語](CHANGELOG-de.md) | [日本語](CHANGELOG-ja.md) | [韓国語](CHANGELOG-ko.md) | [アラビア語](CHANGELOG-ar.md) | [ヒンディー語](CHANGELOG-hi.md) | [イタリア語](CHANGELOG-it.md) | [オランダ語](CHANGELOG-nl.md) | [ポーランド語](CHANGELOG-pl.md) | [ポルトガル語](CHANGELOG-pt.md) | [ルーマニア語](CHANGELOG-ro.md) | [スウェーデン語](CHANGELOG-sv.md)

- **1.7** 新機能 :
    - オプション `--keep_filename` により翻訳時に元のファイル名を保持
    - `.env` ファイルのサポートにより API キーを自動読み込み
    - **インラインコードの保持** : バックティック（`` `...` ``）は翻訳中に保護されます
    - システムプロンプトの改善 :
        - YAML フロントマター内の引用符の扱いの改善
        - テンプレート変数 `{variable}` の保護
        - 要求されていない翻訳者注の禁止
    - 364 ファイルでのテストに成功（ブログ移行 jls42.org）
- **1.6** 新機能 :
    - 翻訳用 Google Gemini API のサポート（`--use_gemini`）
    - 2026 年デフォルトモデルの更新 :
        - OpenAI : `gpt-5`（高品質）、`gpt-5-mini`（エコ）
        - Claude : `claude-sonnet-4-5`（高品質）、`claude-haiku-4-5`（エコ）
        - Gemini : `gemini-3-pro-preview`（高品質）、`gemini-3-flash-preview`（エコ）
    - 省コストモード（`--eco`）によりより高速で低コストなモデルを使用
    - ディレクトリを走査せずに単一ファイルを翻訳（`--file`）
    - 新しい簡素化された命名パターン : `{base}-{lang}.md`
    - モデル名を含む旧形式を保持するオプション : `--include_model`
    - デフォルト（128k）のトークン制限で未リストのモデルをサポート
    - README を 14 言語に翻訳
- **1.5** 改善 :
    - **API キーとデフォルトモデルの更新 :**
        - **OpenAI :** `DEFAULT_MODEL_OPENAI` から `"gpt-4o"` へ更新。
        - **Mistral AI :** `DEFAULT_MODEL_MISTRAL` から `"mistral-large-latest"` へ更新。
        - **Anthropic の Claude :** `DEFAULT_ANTHROPIC_API_KEY` を追加し、`DEFAULT_MODEL_CLAUDE` を `"claude-3-5-sonnet-20240620"` に更新。
    - **翻訳プロンプトの最適化 :**
        - 直接翻訳および翻訳メモのプロンプトを明確さと効率のために強化し、メタデータや特定のフォーマット要素の保持に関する詳細な指示を含めました。
    - **コードのリファクタリング :**
        - Mistral AI クライアント初期化で `MistralClient` をクラス `Mistral` に置換。
        - 可読性と保守性を向上させるための import 再編成。
        - 翻訳時に元のフォーマットを保持するためのテキスト分割とコードブロック管理の改善。
    - **出力ファイルの管理 :**
        - 出力ファイル名でモデルと言語の順序を逆に（例：`f"{base}-{args.target_lang}-{args.model}.md"`）、翻訳の整理と検索を容易に。
    - **その他の改善 :**
        - 不要な空行の削除によるコードのクリーンアップ。
        - スクリプトの構造と可読性を向上させるための小さな調整。
- **1.4** 新機能 :
    - Anthropic の Claude API を翻訳にサポート
    - 明確さと効率を高めるためのプロンプトの最適化
    - 保守性向上のための小さな調整
- **1.3** 改善と新機能 :
    - コードブロックの管理を改善
    - 出力ファイルの管理を改善
    - 既存ファイルの検出機能を改善
    - 強制翻訳オプション `--force`
    - 出力ファイル名でモデルと言語の順序を逆に
- **1.2** チェンジログの修正
- **1.1** Mistral AI API のサポートを追加
- **1.0** 初期バージョン - OpenAI API のサポート

**この文書は gpt-5-mini モデルを使用して fr バージョンから ja 言語に翻訳されました。翻訳プロセスの詳細については https://gitlab.com/jls42/ai-powered-markdown-translator をご覧ください。**

