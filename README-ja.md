# AI搭載Markdown翻訳ツール

🌍 [フランス語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [英語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [スペイン語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中国語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [ドイツ語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [韓国語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [アラビア語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [ヒンディー語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [イタリア語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [オランダ語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [ポーランド語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [ポルトガル語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [ルーマニア語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [スウェーデン語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacyバッジ"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

**OpenAI**、**Mistral AI**、**Claude（Anthropic）**、**Google Gemini**、**Grok（xAI）**を使用するMarkdownファイル翻訳ツールです。API経由、または従量課金なしでChatGPT（Codex）やGrokのサブスクリプション枠を利用できます。

このPythonスクリプトは、書式、コードブロック、front matterのメタデータを保持したまま、Markdownファイルを原文言語から対象言語へ翻訳します。

## 主な特徴

- **マルチプロバイダー**: 5つのAPI（OpenAI、Mistral、Claude、Gemini、Grok）＋サブスクリプション向けCLI 2つ。従量課金なしでCodex（ChatGPT）とGrokを利用可能
- **2026年モデル**: GPT-5.6 Terra、Claude Sonnet 5、Gemini 3.7 Flash
- **エコノミーモード**: より高速で低コストのモデルを使用する `--eco` オプション
- **単一ファイル**: 1つのファイルだけを翻訳する `--file` オプション
- **スマート分割**: モデルごとのトークン上限に対応した長文処理
- **コードの保持**: コードブロックとインラインコード（`` `...` ``）を保持
- **ファイル名**: 元の名前を保持する `--keep_filename` オプション
- **ニュースモード**: 英語の引用を保護し、ニュース記事内の国旗を処理する `--news` オプション
- **.env設定**: APIキー用の `.env` ファイルをサポート
- **翻訳注記**: 文書末尾への注記追加（任意）

## インストール

### ツールを使用する場合

```bash
pip install ai-powered-markdown-translator
```

これで `aipmt` コマンドをどこからでも使用できます。Pythonのスクリプトディレクトリが `PATH` に含まれていない場合は、`python -m aipmt` でもまったく同じことができます。Python 3.10以降が必要です。

他のパッケージから分離してインストールする場合：

```bash
pipx install ai-powered-markdown-translator
```

### プロジェクトに貢献する場合

開発にはクローンしたリポジトリが引き続き必要です。テスト、28種類の翻訳、品質管理用ツール一式はそこにあります。

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` は**完全に固定されたlock**で、テスト済み環境を正確に再現します。`pyproject.toml` に公開されているバージョン範囲は意図的に広く設定されており、他のパッケージに何も強制しません。

### 品質管理ツール（任意ですが推奨）

このプロジェクトでは、書式が崩れているコード、脆弱なコード、秘密情報を含むコードのコミットを防ぐために [`pre-commit`](https://pre-commit.com) を使用します。インストール：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

有効なフック：ruff（lint＋format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（複雑度）、detect-secrets（APIキー）、mypy（段階的な型付け）、Opengrep（SAST）、pip-audit（依存関係のCVE）、unittest。詳細は `CLAUDE.md` の _Quality / pre-commit_ セクションを参照してください。

## 設定

キーは**優先度の高い順に3か所**から検索されます。
それぞれ、前の場所で空いている部分を補うだけです。

|     | 場所                                            | 用途                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 環境変数                     | CI、コンテナ、一時的な上書き |
| 2   | 現在のディレクトリ（または親ディレクトリ）の `.env` | プロジェクト固有のキー            |
| 3   | `~/.config/aipmt/.env`                        | **一度インストールすれば、どこでも有効**   |

`pip install` の後では、3番目が最も簡単です：

```bash
mkdir -p ~/.config/aipmt
cat > ~/.config/aipmt/.env <<'EOF'
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
EOF
chmod 600 ~/.config/aipmt/.env
```

このファイルは、変数が絶対パスを指している場合は `XDG_CONFIG_HOME` に従い（そうでない場合は仕様の規定どおり無視されます）、Windowsでは `%APPDATA%` に従います。

2番目の方法は、リポジトリに独自のキーがある場合に便利です。ルートにある `.env` はユーザー設定より優先されますが、ユーザー設定自体は変更しません。また、環境ですでに定義されている変数は両方より優先されます：

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

キーが見つからない場合、コマンドは呼び出しのトレースを表示せず、3つの場所と正確なパスを一覧表示します。

`GEMINI_API_KEY` は `GOOGLE_API_KEY` の代替として使用できます（AI Studioの慣例）。任意の変数：`XAI_BASE_URL`（xAIのエンドポイント、デフォルトは `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（Anthropicの呼び出し間隔を秒単位で指定、デフォルトは900）、`CODEX_BIN` / `CODEX_TIMEOUT`、`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`、および `GROK_TRANSLATE_SANDBOX`（Grok CLIセクションを参照）。`regen_translations.sh` 側では、`REGEN_PROVIDER`、`REGEN_MODEL`、`REGEN_JOB_TIMEOUT`（ジョブごとの上限、デフォルト600秒）があります。

## 使用方法

### 単一ファイルを翻訳する

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### ディレクトリを翻訳する

```bash
# Avec OpenAI (défaut: gpt-5.6-terra)
aipmt --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
aipmt --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
aipmt --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
aipmt --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'

# Avec Codex (sur le quota de l'abonnement ChatGPT, sans facturation à l'usage)
aipmt --use_codex --eco --file 'README.md' --target_dir . --target_lang 'it'

# Avec Grok par l'API xAI (nécessite XAI_API_KEY, facturé à l'usage)
aipmt --use_grok --source_dir 'content/fr' --target_dir 'content/pt' --target_lang 'pt'

# Avec Grok sur le quota de l'abonnement Grok (nécessite `grok login`)
aipmt --use_grok_cli --eco --file 'README.md' --target_dir . --target_lang 'pl'
```

### ChatGPTのサブスクリプション（`--use_codex`）で翻訳する

このプロバイダーはAPIキーを消費しません。公式Codex CLIを非対話モードで操作するため、翻訳はすでに支払い済みのChatGPTサブスクリプション（Plus、Pro、Business…）の枠から差し引かれます。これはOpenAIがこの用途について文書化している唯一の方法です。`~/.codex/auth.json` のトークンはPlatform APIの呼び出しを認証するものではなく、このスクリプトから読み取られることもありません。

**前提条件：**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

バイナリは、`CODEX_BIN` 変数、`PATH`、その後にPythonパッケージ `openai-codex-cli-bin` の順で検索されます。後者を `requirements.txt` に含めていないのは意図的です。約250MBあるため、任意のプロバイダーのためにすべてのユーザーへ負担させることになるからです。

**知っておくべきこと：**

- **APIキーは使用されません。** `OPENAI_API_KEY` と `CODEX_API_KEY` はサブプロセスの環境から削除されるため、`.env` にキーが存在していても、翻訳が従量課金に切り替わることはありません。
- **1セグメント＝プランの5時間ウィンドウ内の「ローカルメッセージ」1件**です。品質モデル（`gpt-5.6-sol`、5時間あたり10～100メッセージ）ではなく、`--eco`（モデル `gpt-5.6-luna`、Plusでは5時間あたり250～2,000メッセージ）を使用してください。
- **API呼び出しより低速**です。直接実行なら数秒で済むところ、README全体で約45秒かかります。
- **CIでは拒否されます**（`CI` または `GITHUB_ACTIONS` が定義されている場合）。サブスクリプション認証は共有ランナー向けではなく、OpenAIも公開リポジトリでのこのワークフローを推奨していません。この経路ではAPIキーを使用してください。
- 環境変数：`CODEX_BIN`（バイナリの明示的なパス）および `CODEX_TIMEOUT`（セグメントあたりの秒数、デフォルトは `600`）。

### Grokのサブスクリプション（`--use_grok_cli`）で翻訳する

`--use_codex` と同じ原理で、公式の **Grok Build** CLIを使用します。翻訳はトークン単位で課金されるのではなく、Grokサブスクリプション（SuperGrok / X Premium+）の枠から差し引かれます。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**サンドボックスについて――使用前に必ず読んでください。** このプロバイダーは構造上、`--use_codex` より**弱い**ものであり、それを前提としています：

- Codexは、システムによって強制される境界である `--sandbox read-only` で動作します。
- Grokのサンドボックスは、最近のLinux環境の多くでは適用できません。Ubuntu 24.04以降では、AppArmorが非特権ユーザーネームスペースをブロックし、`/run/podman` が `0700` の場合は、コンテナランタイムソケットのdeny-listが失敗します。その結果、**組み込み**プロファイルが適用できない場合、**無防備な状態で、しかも無言のまま**起動します。
- そのため、スクリプトはデフォルトでプロファイルを要求せず、**無言でフォールバックすることもありません**。警告を表示します。隔離はCLIの `--deny` ルール（catch-allである `*` を含む）に依存します。これは実測された唯一の _fail-closed_ 層であり、未知のルールがある場合は保護を黙って外すのではなく、起動を拒否します。
- OSサンドボックスを**必須にする**には `GROK_TRANSLATE_SANDBOX=read-only` を使用します。マシンがそれを適用できない場合は起動に失敗します。これが意図された動作です。

**クォータ**：GrokのプールはChat、Imagine、Voiceと**共有される週次クォータ**であり、読み取るコマンドはありません。そのため、一括処理によって何も通知されないまま会話での利用枠が消費される可能性があります。これが同時実行数を2に制限し、`regen_translations.sh` に警告を表示する理由です。

その他の変数：`GROK_BIN`（バイナリのパス）、`GROK_TIMEOUT`（デフォルト900秒）。

28種類の翻訳を再生成するには：

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### エコノミーモード

より高速で低コストのモデル（gpt-5.6-luna、claude-haiku-4-5、gemini-3.1-flash-lite）を使用します：

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### オプション

| オプション                   | 説明                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | 翻訳する単一のMarkdownファイル                                       |
| `--source_dir`           | Markdownファイルを含むソースディレクトリ                        |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ                          |
| `--source_lang`          | 原文言語（デフォルト：`fr`）                                             |
| `--target_lang`          | 対象言語（デフォルト：`en`）                                              |
| `--model`                | 使用する特定のモデル                                             |
| `--eco`                  | エコノミーモデルを使用                                         |
| `--use_mistral`          | Mistral AI APIを使用                                                |
| `--use_claude`           | Claude APIを使用                                                    |
| `--use_gemini`           | Gemini APIを使用                                                    |
| `--use_codex`            | ChatGPTサブスクリプション枠でCodex CLIを使用               |
| `--use_grok`             | xAI（Grok）APIを使用 — `XAI_API_KEY` が必要                      |
| `--use_grok_cli`         | Grokサブスクリプション枠でGrok CLIを使用                   |
| `--force`                | 再翻訳を強制                                                  |
| `--keep_filename`        | 元のファイル名を保持                                     |
| `--news`                 | ニュースモード：英語の引用を保護し、言語ごとに国旗を処理 |
| `--add_translation_note` | 翻訳注記を追加                                           |
| `--note_position`        | 注記の位置：`top`、`bottom`（デフォルト）、または `both`                |
| `--note_format`          | 注記の形式：`legacy`（デフォルト、太字段落）または `marker`       |
| `--include_model`        | 出力ファイルにモデル名を含める                       |
| `--reasoning_effort`     | GPT-5.xの推論努力：`none`/`low`/`medium`/`high`/`xhigh`    |

> **6つのプロバイダーフラグは相互排他的です。** 以前は2つを組み合わせても無言で受け付けられ、最初に検査されたものが選択されていました。そのため、サブスクリプション枠での翻訳（`--use_codex`、`--use_grok_cli`）が要求されても、警告なしに従量課金へ切り替わる可能性がありました。`argparse` は現在、この組み合わせを拒否します。

### 翻訳注記：位置と形式

`--add_translation_note` を使用すると、translatorは注記を上部、下部、または両方に配置でき、単純なテキスト形式（後方互換）またはMarkdownプラグインで利用できる `marker` 形式にできます。

**位置**（`--note_position`）：

- `bottom`（デフォルト）：従来どおり、ファイル末尾に注記を配置。
- `top`：**YAML frontmatterの後**に注記を挿入（Astro Content Collections、gray-matterなどに安全）。
- `both`：上部と下部の両方に注記を挿入（LLMの呼び出しは1回のみで、内容を両方の位置に再利用）。

**形式**（`--note_format`）：

- `legacy`（デフォルト）：太字段落 `**...**`。v1.8と完全に同一の動作で、byte-for-byteで互換。Hugo、GitHub、GitLab、およびあらゆるMarkdownレンダラーに対応。
- `marker`：非表示のMarkdownリンク参照定義（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）に続いて太字のblockquoteを配置。GitHub/GitLabでネイティブに読み取れるほか、Astro側のremarkプラグインでビルド時に利用し、スタイル付きバナーを生成できます（jls42.orgのブログを参照）。

```bash
# Compatibilité legacy (rien ne change vs v1.8)
aipmt --file article.mdx --target_lang en --add_translation_note

# Format marker, note en haut uniquement (Astro)
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position top

# Format marker en haut ET en bas
aipmt --file article.mdx --target_lang en \
    --add_translation_note --note_format marker --note_position both
```

### デフォルトモデル（2026年）

| プロバイダー | 品質（デフォルト）       | エコノミー（`--eco`）    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **長文翻訳への推奨**：`--use_gemini`（デフォルト＝`gemini-3.7-flash`）は、ラテン文字以外のスクリプト（PL、JA、ZH、AR、HI）でもMarkdownの構造を忠実に保持します。`--news` モードではプレースホルダーの忠実性も維持されます。このREADMEを日本語に翻訳した際の測定では、`gemini-3.1-pro-preview` と同一の構造（21個のリスト、18個のコードブロック、13個のHTMLリンク、13個の画像、すべてのURLを保持）を、約6分の1のレイテンシーで実現しました。後方互換性のため、OpenAIが引き続きデフォルトです。

## このスクリプトを使用するプロジェクト

- **[jls42.org](https://jls42.org)** - 多言語対応の個人ブログ（15言語）

## 作者

Julien LE SAUX  
メール：contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。[LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)を参照してください。

**記事はgpt-5.6-lunaを使ってフランス語から日本語に翻訳されました。**
