# AIを活用したMarkdown翻訳ツール

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 コード品質</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="品質ゲートのステータス"></a>
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

**OpenAI**、**Mistral AI**、**Claude（Anthropic）**、**Google Gemini**、**Grok（xAI）**をAPI経由で利用するMarkdownファイル翻訳ツールです。従量課金なしでChatGPT（Codex）またはGrokのサブスクリプション枠を利用できるほか、オープンソースエージェントの**OpenCode**を通じて、任意のプロバイダーにも接続できます。利用可能なプロバイダーには、ローカルモデル（Ollama）、無料プラン、サブスクリプション（GitHub Copilotなど）、APIキー方式があります。

このPythonスクリプトは、書式、コードブロック、front matterのメタデータを保持しながら、Markdownファイルをソース言語から対象言語へ翻訳します。

## 主な特徴

- **マルチプロバイダー**: 5つのAPI（OpenAI、Mistral、Claude、Gemini、Grok）と、従量課金なしのサブスクリプション対応CLI 2種類（Codex（ChatGPT）およびGrok）に加え、OpenCode（オープンソース、MIT）を通じて、ローカルモデルを含むOpenCodeで設定した任意のプロバイダーを利用可能
- **2026年モデル**: GPT-5.6 Terra、Claude Sonnet 5、Gemini 3.7 Flash
- **節約モード**: より高速で低コストなモデルを使用する `--eco` オプション
- **単一ファイル**: 1つのファイルだけを翻訳する `--file` オプション
- **スマート分割**: モデルごとのトークン制限に対応した長文処理
- **コードの保持**: コードブロックとインラインコード（`` `...` ``）を保持
- **ファイル名**: 元の名前を保持する `--keep_filename` オプション
- **Newsモード**: ニュース記事内の英語引用を保護し、国旗を処理する `--news` オプション
- **.env設定**: APIキー用の `.env` ファイルをサポート
- **翻訳メモ**: ドキュメント末尾へのメモ追加（任意）

## インストール

### ツールを使用する場合

```bash
pip install ai-powered-markdown-translator
```

これで `aipmt` コマンドをどこからでも利用できるようになります。Pythonのスクリプトディレクトリが `PATH` に含まれていない場合は、`python -m aipmt` でもまったく同じことができます。Python 3.10以降が必要です。

他のパッケージから分離してインストールする場合：

```bash
pipx install ai-powered-markdown-translator
```

### プロジェクトに貢献する場合

開発にはクローンしたリポジトリが引き続き必要です。テスト、28言語の翻訳、品質管理ツール一式はそこに置かれています。

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` は、テスト済み環境を正確に反映した**完全に固定されたlockファイル**です。`pyproject.toml` で公開されているバージョン範囲は意図的に広く設定されており、他のパッケージに制約を課しません。

### 品質管理ツール（任意ですが推奨）

このプロジェクトでは、形式の崩れたコード、脆弱性、秘密情報を含むコードのコミットを防ぐために [`pre-commit`](https://pre-commit.com) を使用しています。インストール：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

有効なフック：ruff（lint+format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（複雑度）、detect-secrets（APIキー）、mypy（段階的な型付け）、Opengrep（SAST）、pip-audit（依存関係のCVE）、unittest。詳細は `CLAUDE.md` の _Quality / pre-commit_ セクションを参照してください。

## 設定

キーは優先度の高い順に**3か所**から検索されます。
各場所は、前の場所で空いている部分だけを補います。

|     | 場所                                            | 用途                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 環境変数                     | CI、コンテナ、一時的な上書き |
| 2   | 現在のディレクトリ（または親）の `.env` | プロジェクト固有のキー            |
| 3   | `~/.config/aipmt/.env`                        | **一度インストールすれば、どこでも有効**   |

`pip install` の後は、3番目が最も簡単です：

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

このファイルは、変数が絶対パスを示している場合は `XDG_CONFIG_HOME` に従い（そうでない場合は仕様どおり無視されます）、Windowsでは `%APPDATA%` に従います。

2番目の方法は、リポジトリに独自のキーがある場合に便利です。ルートにある `.env` はユーザー設定より優先されますが、ユーザー設定自体は変更しません。また、環境ですでに定義されている変数は両方より優先されます。

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

キーが見つからない場合、コマンドは呼び出し履歴を表示せず、3つの場所とその正確なパスを列挙します。

`GEMINI_API_KEY` は `GOOGLE_API_KEY` の代替として使用できます（AI Studioの規約）。任意の変数：`XAI_BASE_URL`（xAIのエンドポイント、デフォルトは `https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（Anthropicの呼び出しごとの秒数、デフォルトは900）、`CODEX_BIN` / `CODEX_TIMEOUT`、`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`、`GROK_TRANSLATE_SANDBOX`（Grok CLIセクションを参照）、`OPENCODE_BIN` / `OPENCODE_TIMEOUT`（OpenCodeセクションを参照）。`regen_translations.sh` 側では、`REGEN_PROVIDER`、`REGEN_MODEL`、`REGEN_JOB_TIMEOUT`（ジョブごとの上限、デフォルトは600秒）があります。

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

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### ChatGPTのサブスクリプションで翻訳する（`--use_codex`）

このプロバイダーではAPIキーを一切消費しません。公式Codex CLIを非対話モードで操作するため、翻訳はすでに支払われているChatGPT（Plus、Pro、Businessなど）のサブスクリプション枠から差し引かれます。これは、この用途についてOpenAIが文書化している唯一の方法です。`~/.codex/auth.json` のトークンはPlatform APIの呼び出しを認証するものではなく、このスクリプトから読み取られることもありません。

**前提条件：**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

バイナリは、`CODEX_BIN` 変数、`PATH`、Pythonパッケージ `openai-codex-cli-bin` の順に検索されます。後者を `requirements.txt` に含めていないのは意図的です。約250MBあるため、任意のプロバイダーのためにすべてのユーザーへインストールを要求することになるからです。

**知っておくべきこと：**

- **APIキーは使用されません。** `OPENAI_API_KEY` と `CODEX_API_KEY` はサブプロセスの環境から削除されるため、`.env` に存在するキーが翻訳を従量課金へ切り替えることは決してありません。
- **1セグメント＝プランの5時間ウィンドウにおける「ローカルメッセージ」1件**です。Plusでは5時間あたり250～2,000メッセージの `--eco`（モデル `gpt-5.6-luna`）を、品質モデル（`gpt-5.6-sol`、5時間あたり10～100メッセージ）より優先して使用してください。
- **API呼び出しより低速**です。直接呼び出す場合の数秒に対し、完全なREADMEでは約45秒かかります。
- **CIでは拒否されます**（`CI` または `GITHUB_ACTIONS` が定義されている場合）。サブスクリプション認証は共有ランナー向けではなく、OpenAIも公開リポジトリでのこのワークフローを推奨していません。この経路ではAPIキーを使用してください。
- 環境変数：`CODEX_BIN`（バイナリの明示的なパス）および `CODEX_TIMEOUT`（セグメントごとの秒数、デフォルトは `600`）。

### Grokのサブスクリプションで翻訳する（`--use_grok_cli`）

`--use_codex` と同じ仕組みで、公式CLI **Grok Build**を使用します。トークン単位で課金される代わりに、翻訳はGrok（SuperGrok / X Premium+）のサブスクリプション枠から差し引かれます。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**隔離について — 使用前に必ず読んでください。** このプロバイダーは構造上、`--use_codex` より**弱く**なっており、それを前提としています。

- Codexは`--sandbox read-only`で動作します。これはシステムによって強制される境界です。
- Grokのサンドボックスは、最近のLinux環境の多くでは適用できません。Ubuntu 24.04以降ではAppArmorが非特権ユーザーネームスペースをブロックし、`/run/podman` が `0700` の場合、コンテナランタイムソケットの拒否リストも失敗します。しかし、**組み込み**プロファイルが適用できない場合、プロセスは**黙って非隔離状態で**起動します。
- そのためスクリプトはデフォルトでプロファイルを要求せず、**黙って代替することもありません**。警告を表示します。隔離はCLIの `--deny` ルール（catch-allの `*` を含む）に依存します。これは唯一の実測済みの _fail-closed_ 層であり、未知のルールがある場合は保護を知らせずに解除するのではなく、起動を拒否します。
- OSサンドボックスを**必須にする**には、`GROK_TRANSLATE_SANDBOX=read-only` を使用します。マシンがそれを適用できない場合は起動に失敗します。これが意図された動作です。

**クォータ**：Grokのプールは**週単位で、Chat、Imagine、Voiceと共有**されており、読み取るコマンドはありません。そのためバッチ処理によって、何も通知されないまま会話利用分を消費する可能性があります。これが同時実行数を2に制限し、`regen_translations.sh` に警告を表示する理由です。

その他の変数：`GROK_BIN`（バイナリのパス）、`GROK_TIMEOUT`（デフォルト900秒）。

28言語の翻訳を再生成する場合：

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### OpenCodeで、任意のプロバイダーを利用して翻訳する（`--use_opencode`）

[OpenCode](https://opencode.ai)は、ターミナルで動作する**オープンソース（MIT）**のコードエージェントです。モデルプロバイダーではなく、OpenCode自身で設定したプロバイダーへの**ルーター**です。APIキー、サブスクリプション（GitHub Copilot、ChatGPT、SuperGrok）、無料モデルを**アカウントなし**で提供するOpenCode Zenゲートウェイ、または**ローカル**モデル（Ollama、LM Studio、llama.cpp）を利用できます。このプロバイダーは `opencode run` を非対話モードで操作し、ツールを一切使用せず、1回の往復に限定します。

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` は `provider/modèle` 形式で**必須**です。OpenCodeはプロバイダーではなく、こちらでデフォルトを選択することもありません。OpenCode自身のフォールバックは無料モデルであり、やり取りが学習に利用される可能性があります。

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**隔離について — スクリプトが毎回の呼び出しで行うこと：**

- あなたの設定より優先されるインライン設定（`OPENCODE_CONFIG_CONTENT`）により、`aipmt` エージェントを定義します。このエージェントでは**すべてのツールが拒否**されます（`permission: { "*": "deny" }`）。モデルは読み取り、書き込み、コマンド実行のいずれもできず、実測上、試みることすらありません。セッション共有は無効化され、`--pure` により外部プラグインが除外されます。`--auto` は決して使用しません。
- 呼び出しは、`OPENCODE_DISABLE_PROJECT_CONFIG` および `OPENCODE_DISABLE_CLAUDE_CODE` スイッチとともに、**空の使い捨てディレクトリ**内で実行されます。これらがない場合、OpenCodeは各プロンプトに現在のディレクトリの `AGENTS.md` とあなたの `~/.claude/CLAUDE.md` を注入します。実測では、`AGENTS.md` に置いた「各回答をBANANAで終える」という指示が翻訳に適用されました。一方、`~/.config/opencode/AGENTS.md` のグローバルルールは引き続き適用されます。OpenCodeではそれらを除外できません。
- 出力契約は、戻り値0、`error` イベントなし、ツール呼び出しなし、最後のステップが `stop` で終了していること、空でないテキスト、そしてエージェントが実際に読み込まれていることをすべて要求します。未知の `--agent` ではOpenCodeは失敗せず、ツールが有効なコーディングエージェントへ**黙ってフォールバック**します。ここでは `exit 0` も何の証明にもなりません。
- **aipmtのキーはサブプロセスへ渡されません**（CodexおよびGrokと同じフィルタリング）。ただし、OpenCode自体のキー（Zen、Go）である `OPENCODE_API_KEY` だけは例外です。プロバイダーはOpenCode（`opencode auth login`、`opencode.json`）で設定し、aipmtの `.env` では設定しません。

**知っておくべきこと：**

- Zenの無料モデルは「stealth」またはコントリビューターのモデルであり、変更されるうえ、制限も文書化されていません。また、やり取りが学習に利用される可能性があります。公開ドキュメントには最適ですが、非公開コンテンツには避けてください。実測では、`opencode/mimo-v2.5-free` はこのREADMEを1回で翻訳しました。`opencode/big-pickle` はより低速で、同時に2件のリクエストを送ると応答がないままでした。
- **ローカルモデルには少なくとも16kのコンテキストが必要**です。セグメントは最大16,000文字になる一方、Ollamaではデフォルトで4,096に設定されていることが多いためです。Ollamaでは、`PARAMETER num_ctx 32768` を指定した `Modelfile` を使用し、その後 `ollama create` を実行してください。品質はモデルに依存します。テストファイルでは、7Bモデルはリストの順序を逆転させ、コードブロックの終了を壊しましたが、ゲートウェイのモデルはすべて保持しました。
- `--eco` は効果がありません（モデルは `--model` のものです）。`--reasoning_effort` はOpenCodeの `--variant` としてそのまま渡されるため、モデルが認識している場合にのみ指定してください。
- セッションは他のOpenCodeセッションと同様に、OpenCodeのデータベース（`~/.local/share/opencode/`）に記録されます。
- 環境変数：`OPENCODE_BIN`（バイナリの明示的なパス。指定しない場合は `PATH`、次に `~/.opencode/bin/opencode`）、および `OPENCODE_TIMEOUT`（セグメントごとの秒数、デフォルトは `600`）。`OPENCODE_CONFIG` はエクスポートされていれば尊重されます。

### 節約モード

より高速で低コストなモデル（gpt-5.6-luna、claude-haiku-4-5、gemini-3.1-flash-lite）を使用します。

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### オプション

| オプション | 説明 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file` | 翻訳する単一の Markdown ファイル |
| `--source_dir` | Markdown ファイルを含むソースディレクトリ |
| `--target_dir` | 翻訳済みファイルの出力ディレクトリ |
| `--source_lang` | 原文言語（デフォルト: `fr`） |
| `--target_lang` | 翻訳先言語（デフォルト: `en`） |
| `--model` | 使用する特定のモデル |
| `--eco` | 経済的なモデルを使用 |
| `--use_mistral` | Mistral AI API を使用 |
| `--use_claude` | Claude API を使用 |
| `--use_gemini` | Gemini API を使用 |
| `--use_codex` | ChatGPT サブスクリプションのクォータで Codex CLI を使用 |
| `--use_grok` | xAI（Grok）API を使用 — `XAI_API_KEY` が必要 |
| `--use_grok_cli` | Grok サブスクリプションのクォータで Grok CLI を使用 |
| `--use_opencode` | OpenCode で設定されたプロバイダーに対して OpenCode（オープンソース）を使用；`--model provider/modèle` が必要 |
| `--force` | 再翻訳を強制 |
| `--keep_filename` | 元のファイル名を保持 |
| `--news` | ニュースモード：英語の引用を保護し、言語ごとのフラグを処理 |
| `--add_translation_note` | 翻訳注記を追加 |
| `--note_position` | 注記の位置：`top`、`bottom`（デフォルト）、または `both` |
| `--note_format` | 注記の形式：`legacy`（デフォルト、太字段落）または `marker` |
| `--include_model` | 出力ファイルにモデル名を含める |
| `--reasoning_effort` | GPT-5.x の推論 effort：`none`/`low`/`medium`/`high`/`xhigh` |

> **7 つのプロバイダーフラグは相互排他的です。** 2 つを組み合わせても以前は黙って受け入れられ、最初に検査されたものが選択されていました。そのため、サブスクリプションのクォータ（`--use_codex`、`--use_grok_cli`）で要求した翻訳が、警告なしに従量課金へ回される可能性がありました。
> `argparse` は現在、この組み合わせを拒否します。

### 翻訳注記：位置と形式

`--add_translation_note` を使用すると、translator は注記を上部、下部、または両方に配置でき、単純なテキスト形式（後方互換）または Markdown プラグインで利用可能な `marker` 形式で出力できます。

**位置**（`--note_position`）：

- `bottom`（デフォルト）：従来どおり、ファイル末尾に注記を配置。
- `top`：**YAML frontmatter の後**に注記を挿入（Astro Content Collections、gray-matter などに安全）。
- `both`：上部と下部の両方に注記を挿入（LLM の呼び出しは 1 回のみで、内容を両方の配置に再利用）。

**形式**（`--note_format`）：

- `legacy`（デフォルト）：太字の段落 `**...**` — v1.8 と完全に同一の動作（byte-for-byte）。Hugo、GitHub、GitLab、およびあらゆる Markdown renderer に対応。
- `marker`：不可視の Markdown link reference definition（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）に続く太字の blockquote。GitHub/GitLab ではネイティブに表示でき、Astro 側の remark プラグインでビルド時に利用して、スタイル付きバナーを生成可能（jls42.org のブログを参照）。

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

### デフォルトモデル（2026 年）

| プロバイダー | 品質（デフォルト） | 経済的 (`--eco`) |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI | `gpt-5.6-terra` | `gpt-5.6-luna` |
| Claude | `claude-sonnet-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3.7-flash` | `gemini-3.1-flash-lite` |
| Codex | `gpt-5.6-sol` | `gpt-5.6-luna` |
| Grok API | `grok-4.6` | `grok-4.3` |
| Grok CLI | `grok-4.6` | `grok-4.5` |
| OpenCode | `--model provider/modèle` 必須 | 同じ — `--eco` は効果なし |

> **長文翻訳の推奨**：`--use_gemini`（デフォルト = `gemini-3.7-flash`）は、非ラテン文字のスクリプト（PL、JA、ZH、AR、HI）でも Markdown 構造を忠実に保持します。`--news` モードではプレースホルダーの忠実性も重要です。この README を日本語に翻訳した測定では、`gemini-3.1-pro-preview` と同一の構造（21 個のリスト、18 個のコードブロック、13 個の HTML リンク、13 個の画像、すべての URL を保持）を、レイテンシー約 6 分の 1 で実現しました。後方互換性のため、OpenAI は引き続きデフォルトです。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** - 多言語の個人ブログ（15 言語）

## 作者

Julien LE SAUX
メール：contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。詳しくは [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE) を参照してください。

**gpt-5.6-lunaでフランス語から日本語に翻訳された記事。**
