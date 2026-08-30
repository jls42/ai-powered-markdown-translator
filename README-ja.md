# AI 搭載 Markdown 翻訳ツール

🌍 [フランス語](README.md) | [英語](README-en.md) | [スペイン語](README-es.md) | [中国語](README-zh.md) | [ドイツ語](README-de.md) | [日本語](README-ja.md) | [韓国語](README-ko.md) | [アラビア語](README-ar.md) | [ヒンディー語](README-hi.md) | [イタリア語](README-it.md) | [オランダ語](README-nl.md) | [ポーランド語](README-pl.md) | [ポルトガル語](README-pt.md) | [ルーマニア語](README-ro.md) | [スウェーデン語](README-sv.md)

<h4 align="center">📊 コード品質</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="品質ゲートの状態"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="セキュリティ評価"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="信頼性評価"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="保守性評価"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="カバレッジ"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="脆弱性"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="バグ"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="コードスメル"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="重複行（%）"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="技術的負債"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="コード行数"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy バッジ"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

**OpenAI**、**Mistral AI**、**Claude (Anthropic)**、**Google Gemini**を使用する Markdown ファイル翻訳ツールです。

この Python スクリプトは、書式、コードブロック、front matter メタデータを維持しながら、Markdown ファイルを原文言語から対象言語へ翻訳します。

## 主な機能

- **マルチプロバイダー**：4つの API（OpenAI、Mistral、Claude、Gemini）と、ChatGPT サブスクリプションで利用する Codex CLI に対応
- **2026年モデル**：GPT-5.6 Terra、Claude Sonnet 5、Gemini 3.7 Flash
- **エコノミーモード**：より高速で低コストなモデルを使用する `--eco` オプション
- **単一ファイル**：1つのファイルだけを翻訳する `--file` オプション
- **インテリジェントな分割**：モデルごとのトークン上限に応じて長文を処理
- **コードの保持**：コードブロックとインラインコード（`` `...` ``）を保持
- **ファイル名**：元のファイル名を維持する `--keep_filename` オプション
- **ニュースモード**：ニュース記事内の英語引用文を保護し、国旗を処理する `--news` オプション
- **.env 設定**：API キー用の `.env` ファイルに対応
- **翻訳注記**：文書末尾に注記を任意で追加

## インストール

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 品質管理ツール（任意ですが推奨）

このプロジェクトでは、書式が不適切なコード、脆弱なコード、またはシークレットを含むコードがコミットされるのを防ぐため、[`pre-commit`](https://pre-commit.com) を使用しています。インストール方法：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

有効なフック：ruff（lint＋format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（複雑度）、detect-secrets（API キー）、mypy（段階的型付け）、Opengrep（SAST）、pip-audit（依存関係の CVE）、unittest。詳細については、`CLAUDE.md` の「_Quality / pre-commit_」セクションを参照してください。

## 設定

プロジェクトのルートに `.env` ファイルを作成するか、環境変数を設定します：

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

`GEMINI_API_KEY` は `GOOGLE_API_KEY` の代替として使用できます（AI
Studio の規約）。任意の変数：`XAI_BASE_URL`（xAI エンドポイント、デフォルト
`https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（Anthropic の1回の呼び出しあたりの秒数、デフォルト
900）、`CODEX_BIN` / `CODEX_TIMEOUT`、`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`、
および `GROK_TRANSLATE_SANDBOX`（Grok CLI セクションを参照）。`regen_translations.sh`
側では、`REGEN_PROVIDER`、`REGEN_MODEL`、
および `REGEN_JOB_TIMEOUT`（ジョブごとの上限、デフォルト600秒）を使用できます。

## 使用方法

### 単一ファイルを翻訳する

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### ディレクトリを翻訳する

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
python translate.py --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
python translate.py --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
python translate.py --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### ChatGPT サブスクリプションで翻訳する（`--use_codex`）

このプロバイダーは API キーを一切消費しません。公式 Codex CLI を非対話モードで
操作するため、翻訳量はすでに支払い済みの ChatGPT
サブスクリプション（Plus、Pro、Business など）の利用枠から差し引かれます。これは、この用途について
OpenAI が文書化している唯一の方法です。`~/.codex/auth.json` のトークンは
API Platform の呼び出しを認証せず、このスクリプトから読み取られることもありません。

**前提条件：**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

バイナリは、環境変数 `CODEX_BIN`、`PATH`、
Python パッケージ `openai-codex-cli-bin` の順に検索されます。最後のパッケージは意図的に
`requirements.txt` に含めていません。容量が約250 MBあり、任意のプロバイダーのために
すべての利用者へインストールを強制することになるためです。

**留意事項：**

- **API キーは一切使用されません。** `OPENAI_API_KEY` と `CODEX_API_KEY` は
  サブプロセスの環境から削除されるため、`.env` にキーが存在していても、翻訳が
  従量課金へ切り替わることはありません。
- **1セグメント＝プランの5時間枠における1件の「ローカルメッセージ」**です。
  高品質モデル（`gpt-5.6-sol`、Plus では5時間あたり10～100メッセージ）ではなく、
  `--eco`（モデル `gpt-5.6-luna`、Plus では5時間あたり250～2,000メッセージ）を使用してください。
- **API の直接呼び出しより低速**です。README 全体では、直接呼び出しなら
  数秒であるのに対し、約45秒かかります。
- **CI では拒否されます**（`CI` または `GITHUB_ACTIONS` が定義されている場合）。サブスクリプションによる
  認証は共有 runner 向けではなく、OpenAI も公開リポジトリでのこの
  ワークフローを推奨していません。この経路では API キーを使用してください。
- 環境変数：`CODEX_BIN`（バイナリへの明示的なパス）と
  `CODEX_TIMEOUT`（セグメントごとの秒数、デフォルト `600`）。

### Grok サブスクリプションで翻訳する（`--use_grok_cli`）

`--use_codex` と同じ原理で、公式 **Grok Build** CLI を使用します。
翻訳量はトークン単位で課金される代わりに、Grok サブスクリプション（SuperGrok / X Premium+）の
利用枠から差し引かれます。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**隔離について――使用前に必ずお読みください。** このプロバイダーは構造的に
`--use_codex` よりも**脆弱**であり、これは既知の仕様です：

- Codex は、システムによって強制される境界である `--sandbox read-only` 内で動作します。
- Grok の sandbox は、最近の多くの Linux 環境では**適用できません**。
  Ubuntu 24.04 以降では AppArmor が非特権 user namespace をブロックし、
  `/run/podman` が `0700` に設定されていると、コンテナランタイムの
  socket に対する deny-list が機能しません。さらに、適用できない**組み込み**プロファイルは
  **警告なく非隔離状態で起動します**。
- そのため、スクリプトはデフォルトでプロファイルを要求せず、**警告なしで
  フォールバックすることもありません**。代わりに警告を表示します。隔離は CLI の
  `--deny` ルール（包括的な `*` を含む）に依存します。これは、測定済みの唯一の
  _fail-closed_ レイヤーであり、未知のルールがある場合、保護を黙って
  解除するのではなく起動を拒否します。
- OS の sandbox を**必須にする**には、`GROK_TRANSLATE_SANDBOX=read-only` を使用してください。
  マシンが対応できない場合は起動に失敗します。これは意図した
  動作です。

**利用枠**：Grok のプールは**週単位で、Chat、Imagine、
Voice と共有**されます。また、その残量を確認するコマンドはありません。そのため、バッチ処理によって
会話での利用枠が気付かないうちに消費される可能性があります。このため、同時実行数を2に制限し、
`regen_translations.sh` に警告を表示しています。

その他の変数：`GROK_BIN`（バイナリへのパス）、`GROK_TIMEOUT`（デフォルト900秒）。

28件の翻訳を再生成するには：

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### エコノミーモード

より高速で低コストなモデル（gpt-5.6-luna、claude-haiku-4-5、gemini-3.1-flash-lite）を使用します：

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### オプション

| オプション                   | 説明                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | 翻訳する単一の Markdown ファイル                                       |
| `--source_dir`           | Markdown ファイルを含むソースディレクトリ                        |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ                          |
| `--source_lang`          | 原文言語（デフォルト：`fr`）                                             |
| `--target_lang`          | 対象言語（デフォルト：`en`）                                              |
| `--model`                | 使用する特定のモデル                                             |
| `--eco`                  | エコノミーモデルを使用                                         |
| `--use_mistral`          | Mistral AI API を使用                                                |
| `--use_claude`           | Claude API を使用                                                    |
| `--use_gemini`           | Gemini API を使用                                                    |
| `--use_codex`            | ChatGPT サブスクリプションの利用枠で Codex CLI を使用               |
| `--use_grok`             | xAI API（Grok）を使用 — `XAI_API_KEY` が必要                      |
| `--use_grok_cli`         | Grok サブスクリプションの利用枠で Grok CLI を使用                   |
| `--force`                | 再翻訳を強制                                                  |
| `--keep_filename`        | 元のファイル名を維持                                     |
| `--news`                 | ニュースモード：英語引用文を保護し、言語ごとに国旗を処理 |
| `--add_translation_note` | 翻訳注記を追加                                           |
| `--note_position`        | 注記の位置：`top`、`bottom`（デフォルト）、または `both`                |
| `--note_format`          | 注記の形式：`legacy`（デフォルト、太字段落）または `marker`       |
| `--include_model`        | 出力ファイルにモデル名を含める                       |
| `--reasoning_effort`     | GPT-5.x の推論労力：`none`/`low`/`medium`/`high`/`xhigh`    |

> **6つのプロバイダーフラグは相互排他的です。** 以前は2つを組み合わせても
> 警告なしで受け入れられ、最初に検査されたものへ解決されていました。そのため、
> サブスクリプション利用枠で要求した翻訳（`--use_codex`、`--use_grok_cli`）が
> 警告なしで従量課金される可能性がありました。
> 現在、`argparse` はこの組み合わせを拒否します。

### 翻訳注記：位置と形式

`--add_translation_note` を使用すると、翻訳ツールは注記を上部、下部、または両方に配置でき、後方互換性のある単純なテキスト形式か、Markdown プラグインで処理可能な `marker` 形式で出力できます。

**位置**（`--note_position`）：

- `bottom`（デフォルト）：従来どおりファイル末尾に注記を配置します。
- `top`：**YAML frontmatter の後**に注記を挿入します（Astro Content Collections、gray-matter などとの安全性を確保）。
- `both`：上部と下部の両方に注記を挿入します（LLM 呼び出しは1回のみで、内容を両方の位置に再利用します）。

**形式**（`--note_format`）：

- `legacy`（デフォルト）：太字段落 `**...**`。v1.8 とバイト単位で完全に同一の動作です。Hugo、GitHub、GitLab、およびあらゆる Markdown renderer と互換性があります。
- `marker`：非表示の Markdown link reference definition（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）に続けて、太字の blockquote を配置します。GitHub/GitLab でそのまま読めるほか、Astro 側の remark プラグインによってビルド時に処理し、スタイル付きバナーを生成できます（blog jls42.org を参照）。

```bash
# Compatibilité legacy (rien ne change vs v1.8)
python translate.py --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
python translate.py --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### デフォルトモデル（2026年）

| プロバイダー | 高品質（デフォルト）       | エコノミー（`--eco`）    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **長文翻訳の推奨設定**：`--use_gemini`（デフォルト＝`gemini-3.7-flash`）は、非ラテン文字の言語（PL、JA、ZH、AR、HI）でも Markdown 構造を忠実に維持し、placeholder の忠実性が重要な `--news` モードでも同様です。この README の日本語翻訳で測定した結果、`gemini-3.1-pro-preview` と同一の構造（21個のリスト、18個のコードブロック、13個の HTML リンク、13枚の画像、すべての URL を維持）を、約6分の1の待ち時間で実現しました。後方互換性のため、デフォルトは引き続き OpenAI です。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** - 多言語対応の個人ブログ（15言語）

## 作者

Julien LE SAUX
メール：contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。[LICENSE](LICENSE) を参照してください。

**gpt-5.6-solでフランス語から日本語に翻訳された記事。**
