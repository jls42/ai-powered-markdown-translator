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

**OpenAI**、**Mistral AI**、**Claude (Anthropic)**、**Google Gemini**、**Grok (xAI)** を使用するMarkdownファイル翻訳ツールです。API、従量課金なしのChatGPT（Codex）またはGrokサブスクリプション枠、あるいはオープンソースエージェントの **OpenCode** を通じて、ローカルモデル（Ollama）、無料サービス、サブスクリプション（GitHub Copilotなど）、APIキーといった任意のプロバイダーを利用できます。

このPythonスクリプトは、書式、コードブロック、front matterメタデータを維持しながら、Markdownファイルを原文言語から対象言語へ翻訳します。

## 主な機能

- **マルチプロバイダー**：5つのAPI（OpenAI、Mistral、Claude、Gemini、Grok）に加え、従量課金なしでサブスクリプションを利用する2つのCLIであるCodex（ChatGPT）とGrok、さらにOpenCodeで設定された任意のプロバイダー（ローカルモデルを含む）に対応するオープンソースのMITライセンス版OpenCode
- **2026年モデル**：GPT-5.6 Terra、Claude Sonnet 5、Gemini 3.7 Flash
- **エコノミーモード**：より高速で低コストなモデルを使用するための `--eco` オプション
- **単一ファイル**：1つのファイルのみを翻訳するための `--file` オプション
- **インテリジェントなセグメンテーション**：モデルごとのトークン制限に対応した長文処理
- **コードの保持**：コードブロックとインラインコード（`` `...` ``）を保持
- **ファイル名**：元の名前を維持するための `--keep_filename` オプション
- **ニュースモード**：ニュース記事内の英語の引用を保護し、国旗を処理するための `--news` オプション
- **.env設定**：APIキー用の `.env` ファイルをサポート
- **翻訳注記**：文書末尾への注記の追加に任意で対応

## インストール

### ツールを使用する場合

```bash
pip install ai-powered-markdown-translator
```

これで `aipmt` コマンドをどこからでも利用できます。Pythonのスクリプトディレクトリが
`PATH` に含まれていない場合でも、`python -m aipmt` でまったく同じことが
できます。Python 3.10以降が必要です。

ほかのパッケージから分離してインストールする場合：

```bash
pipx install ai-powered-markdown-translator
```

### プロジェクトに貢献する場合

開発にはクローンしたリポジトリが引き続き必要です。テスト、
28言語の翻訳、すべての品質管理ツールがここに含まれています。

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` は、テスト済み環境を正確に再現する、**すべてのバージョンが完全に固定されたlockファイル**です。
`pyproject.toml` で公開されているバージョン範囲は
意図的に広く設定されており、ほかのパッケージに制約を課しません。

### 品質管理ツール（任意ですが推奨）

このプロジェクトでは、書式が不適切なコード、脆弱なコード、またはシークレットを含むコードがcommitされるのを防ぐために、[`pre-commit`](https://pre-commit.com) を使用しています。インストール方法：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

有効なhook：ruff（lint+format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（複雑度）、detect-secrets（APIキー）、mypy（段階的型付け）、Opengrep（SAST）、pip-audit（依存関係のCVE）、unittest。詳細については、`CLAUDE.md` の _Quality / pre-commit_ セクションを参照してください。

## 設定

キーは優先度の高い順に、**3か所**から検索されます。
それぞれの場所では、それより前の場所で未設定だった値だけが補完されます。

|     | 場所                                            | 用途                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 環境変数                     | CI、コンテナ、一時的な上書き |
| 2   | 現在のディレクトリ（または親ディレクトリ）の `.env` | プロジェクト固有のキー            |
| 3   | `~/.config/aipmt/.env`                        | **一度インストールすれば、どこでも有効**   |

`pip install` の後では、3番目の方法が最も簡単です。

```bash
mkdir -p ~/.config/aipmt
cat > ~/.config/aipmt/.env <<'EOF'
OPENAI_API_KEY=votre-clé-api-openai
XAI_API_KEY=votre-clé-api-xai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
OPENROUTER_API_KEY=votre-clé-api-openrouter
EOF
chmod 600 ~/.config/aipmt/.env
```

環境変数が絶対パスを指定している場合、このファイルは `XDG_CONFIG_HOME` に従います
（それ以外の場合は、仕様の規定どおり無視されます）。Windowsでは `%APPDATA%`
に従います。

2番目の方法は、リポジトリに独自のキーがある場合に引き続き便利です。ルートにある `.env` が、
ユーザー設定を変更することなく優先されます。また、環境内ですでに定義されている
変数は、これら両方より優先されます。

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

キーが見つからない場合、コマンドは呼び出しのスタックトレースを表示せず、
3か所すべてを正確なパスとともに列挙します。

`GEMINI_API_KEY` は `GOOGLE_API_KEY` の代替として使用できます（AI
Studioの規約）。任意の変数：`XAI_BASE_URL`（xAIのendpoint、デフォルトは
`https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（Anthropic呼び出しごとの秒数、デフォルトは
900）、`CODEX_BIN` / `CODEX_TIMEOUT`、`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`、
`GROK_TRANSLATE_SANDBOX`（Grok CLIセクションを参照）、`OPENCODE_BIN` /
`OPENCODE_TIMEOUT`（OpenCodeセクションを参照）、および `OPENROUTER_BASE_URL` /
`OPENROUTER_TIMEOUT` / `OPENROUTER_PREFLIGHT_TIMEOUT`（OpenRouterセクションを参照）。
`regen_translations.sh` 側では、`REGEN_PROVIDER`（デフォルトは `codex`、サブスクリプション経由）、
`REGEN_MODEL`、`REGEN_ALLOW_PAID_API`（課金対象APIを使用する場合に必須の明示的な上書き）、
および `REGEN_JOB_TIMEOUT`（jobごとの上限、デフォルトは600秒、Codexでは1,800秒）を使用できます。

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

# Avec OpenRouter (routeur vers ~430 modèles ; --model obligatoire)
aipmt --use_openrouter --model 'z-ai/glm-5.2' --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### ChatGPTサブスクリプションで翻訳する（`--use_codex`）

このプロバイダーはAPIキーを一切使用しません。公式Codex CLIを非対話モードで
操作するため、翻訳分はすでに支払い済みのChatGPTサブスクリプション
（Plus、Pro、Businessなど）の利用枠から差し引かれます。これは、この用途について
OpenAIが文書化している唯一の方法です。`~/.codex/auth.json` のトークンでは
API Platformの呼び出しを認証できず、そもそもこのスクリプトがそれを読み取ることもありません。

**前提条件：**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

バイナリは、環境変数 `CODEX_BIN`、`PATH`、
Pythonパッケージ `openai-codex-cli-bin` の順に検索されます。最後のパッケージは意図的に
`requirements.txt` に含まれていません。サイズが約250 MBあり、任意のプロバイダーのために
すべてのユーザーへ負担を強いることになるためです。

**留意事項：**

- **APIキーは一切使用されません。** `OPENAI_API_KEY` と `CODEX_API_KEY` は
  サブプロセスの環境から削除されるため、`.env` にキーが存在していても、
  翻訳が従量課金へ切り替わることはありません。
- **1セグメントは、プランの5時間枠における1つの「ローカルメッセージ」に相当します。**
  品質重視モデル（`gpt-5.6-sol`、5時間あたり10～100メッセージ）ではなく、
  `--eco`（モデル `gpt-5.6-luna`、Plusでは5時間あたり250～2,000メッセージ）を使用してください。
- APIを直接呼び出す場合よりも**低速**です。README全体では、直接呼び出しなら数秒のところ、
  約45秒かかります。
- **CIでは拒否されます**（`CI` または `GITHUB_ACTIONS` が定義されている場合）。
  サブスクリプションの認証には個人用sessionファイルが使われるため、それを共有runnerへ
  配置すると、その環境で実行されるあらゆるものから再利用可能な認証情報を
  渡すことになります。この経路ではAPIキーを使用してください。
- 環境変数：`CODEX_BIN`（バイナリへの明示的なパス）および
  `CODEX_TIMEOUT`（セグメントごとの秒数、デフォルトは `600`）。

### Grokサブスクリプションで翻訳する（`--use_grok_cli`）

`--use_codex` と同じ仕組みで、公式の **Grok Build** CLIを使用します。
翻訳分はトークン単位で課金される代わりに、Grokサブスクリプション
（SuperGrok / X Premium+）の利用枠から差し引かれます。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**隔離 — 使用前に必ずお読みください。** このプロバイダーは構造上、
`--use_codex` よりも**脆弱**ですが、これは意図した仕様です。

- Codexは、システムによって強制される境界である `--sandbox read-only` 内で動作します。
- 最近の多くのLinux環境では、Grokのsandboxを**適用できません**。
  Ubuntu 24.04以降ではAppArmorが非特権user namespaceをブロックし、
  `/run/podman` が `0700` に設定されている場合、コンテナruntime socketの
  deny-listが失敗するためです。さらに、適用できない**組み込み**profileは、
  **警告なしで隔離されていない状態**で起動します。
- そのため、スクリプトはデフォルトではprofileを要求せず、**警告なしで
  fallbackすることもありません**。代わりに警告を表示します。隔離はCLIの
  `--deny` ルール（catch-allの `*` を含む）に依存します。これは、
  測定済みの唯一の _fail-closed_ レイヤーであり、未知のルールがある場合は、
  保護を無言で解除するのではなく起動を拒否します。
- OSのsandboxを**必須にする**には、`GROK_TRANSLATE_SANDBOX=read-only` を使用してください。
  マシンが要件を満たせない場合は起動に失敗します。これは意図された動作です。

**利用枠**：Grokのpoolは**週単位で、Chat、Imagine、Voiceと共有**されており、
それを確認するコマンドはありません。そのため、バッチ処理によって会話用途の利用枠が
通知なしに消費される可能性があります。このため、同時実行数は2に制限され、
`regen_translations.sh` に警告が表示されます。

その他の変数：`GROK_BIN`（バイナリへのパス）、`GROK_TIMEOUT`（デフォルトは900秒）。

28言語の翻訳を再生成する場合：

```bash
# Défaut : Codex sur l'abonnement ChatGPT, modèle qualité gpt-5.6-sol, 0 € à l'usage
./regen_translations.sh --force

# Le modèle éco de Codex, si le volume l'impose
REGEN_MODEL=gpt-5.6-luna ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Une API facturée (openai, gemini, grok, openrouter) est REFUSÉE sans cette dérogation nommée
REGEN_PROVIDER=openai REGEN_ALLOW_PAID_API=1 ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force

# Via OpenRouter : API facturée, donc dérogation ET modèle obligatoires
REGEN_PROVIDER=openrouter REGEN_ALLOW_PAID_API=1 REGEN_MODEL=z-ai/glm-5.2 ./regen_translations.sh --force
```
### OpenCode を使用し、任意のプロバイダーで翻訳する（`--use_opencode`）

[OpenCode](https://opencode.ai) は、ターミナルで動作する **オープンソース（MIT）** の
コーディングエージェントです。モデルプロバイダーではなく、OpenCode 自体に
設定したプロバイダーへの**ルーター**です。API キー、サブスクリプション、
アカウントなしで**無料**モデルを提供する OpenCode Zen ゲートウェイ、または
**ローカル**モデルを利用できます。この provider は `opencode run` を非対話モードで実行し、
ツールを一切使用せず、呼び出しを単一の往復処理に制限します。

ここでは、このうち **Zen ゲートウェイ**とローカルの
**Ollama** という2つの経路をエンドツーエンドで測定しました。OpenCode が対応を掲げる
その他の経路（GitHub Copilot、LM Studio、llama.cpp）も、provider は
OpenCode としか通信しない設計上、動作するはずです。ただし未検証であり、この README には
確認済みの内容のみを記載しています。

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` は**必須**で、形式は `provider/modèle` です。OpenCode は
プロバイダーではなく、デフォルト値も代わりに選択されません。OpenCode 自体のフォールバック先は、
やり取りが学習に利用される可能性のある無料モデルです。

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**隔離 — スクリプトが呼び出しごとに行うこと：**

- ユーザー設定より優先されるインライン設定（`OPENCODE_CONFIG_CONTENT`）により、
  **すべてのツールが拒否された** `aipmt` エージェント
  （`permission: { "*": "deny" }`）を定義します。モデルは読み取り、書き込み、
  コマンド実行のいずれもできず、測定上、それらを試みることさえありません。セッション共有は
  無効化され、`--pure` は外部プラグインを除外し、`--auto` は決して使用しません。
- 呼び出しは**空の使い捨てディレクトリ**内で、スイッチ
  `OPENCODE_DISABLE_PROJECT_CONFIG` と `OPENCODE_DISABLE_CLAUDE_CODE` を使用して実行されます。
  これらがない場合、OpenCode は各プロンプトにカレントディレクトリの `AGENTS.md` と
  ユーザーの `~/.claude/CLAUDE.md` を注入します。実測では、`AGENTS.md` に記述した
  「各回答を BANANA で終える」という指示が翻訳にも適用されました。一方、
  `~/.config/opencode/AGENTS.md` のグローバルルールは引き続き適用されます。
  OpenCode ではこれを除外できません。
- 出力契約では、終了コード 0、`error` イベントなし、ツール呼び出しなし、
  最終ステップが `stop` で完了、空でないテキスト、指定エージェントが実際にロード済み、
  という条件をすべて要求します。不明な `--agent` を指定しても
  OpenCode は失敗せず、ツールが有効なコーディングエージェントへ**黙ってフォールバック**
  します。ここでは `exit 0` も何の証明にもなりません。
- **aipmt のキーは一切サブプロセスへ渡されません**（Codex および Grok と同じ
  フィルタリング）。ただし、OpenCode 自体（Zen、Go）のキーである
  `OPENCODE_API_KEY` だけは明示的な例外です。プロバイダーは aipmt の
  `.env` ではなく、OpenCode（`opencode auth login`、`opencode.json`）で設定します。

**留意事項：**

- **Zen の無料モデルは「stealth」モデルまたはコントリビューターモデル**であり、
  頻繁に変更され、制限も文書化されておらず、やり取りが学習に使用される可能性があります。
  公開ドキュメントには最適ですが、非公開コンテンツには使用しないでください。実測では、
  `opencode/mimo-v2.5-free` はこの README を1回で翻訳しますが、
  `opencode/big-pickle` はより遅く、同時に送信した2件のリクエストが応答なしのままになりました。
- **ローカルモデルには最低でも 16 k のコンテキストが必要です**。セグメントは
  最大16,000文字ですが、Ollama はデフォルトで 4,096 に設定されることがよくあります。
  Ollama では、`PARAMETER num_ctx 32768` を含む `Modelfile` を用意し、その後
  `ollama create` を実行します。品質はモデル次第です。テストファイルでは、
  ゲートウェイのモデルがすべてを保持したのに対し、7B モデルはリストの順序を逆転させ、
  コードブロックの終了フェンスを壊しました。
- `--eco` は効果がありません（モデルは `--model` で指定します）。
  `--reasoning_effort` は OpenCode の `--variant` としてそのまま渡されるため、
  モデルが対応している場合にのみ指定してください。
- セッションは通常の OpenCode セッションと同様に、OpenCode のデータベース
  （`~/.local/share/opencode/`）へ記録されます。
- 環境変数：`OPENCODE_BIN`（バイナリへの明示的なパス。
  未指定の場合は `PATH`、次に `~/.opencode/bin/opencode`）と `OPENCODE_TIMEOUT`
  （セグメントごとの秒数、デフォルト `600`）。エクスポートされていれば
  `OPENCODE_CONFIG` も使用されます。

**測定例：Ollama 経由のローカルモデル**（RTX 3060 12 GB、RAM 62 GB、Ollama 0.33.3）

```bash
curl -fsSL https://ollama.com/install.sh | sh   # conserve les modèles déjà téléchargés
ollama pull gpt-oss:20b                         # 13 Go, Apache 2.0 — le seul modèle local retenu ici

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

次に `~/.config/opencode/opencode.json` でプロバイダーを指定します。

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": { "baseURL": "http://127.0.0.1:11434/v1" },
      "models": {
        "gpt-oss-20b-32k": {
          "name": "gpt-oss 20B (32k, sans réflexion)",
          "limit": { "context": 32768, "output": 8192 },
          "options": { "reasoningEffort": "none" }
        }
      }
    }
  }
}
```

`reasoningEffort: "none"` は些細な設定ではありません。Ollama はこれらのモデルで
デフォルトで推論を有効にし、Modelfile では無効化できません。OpenCode 経由の実測では、
「猫は敷物の上で眠っている」という文に、オプションなしでは919推論トークンと68秒を要しましたが、
オプションありでは9トークンでした。

```bash
aipmt --use_opencode --model ollama/gpt-oss-20b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

実際の589行のブログ記事（リンク140件、21セクション、
`--news` モードで保護された英語の引用3件）に対し、同じコマンドを
3つのモデルで実行した結果：

| モデル                                   | 所要時間       | 構造                                                  | 相違点                                                                                    |
| ---------------------------------------- | ----------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free`（Zen、無料） | 4分26秒  | 原文と同一                                      | なし                                                                                     |
| `ollama/gemma4-12b-32k`（ローカル）          | 10分10秒 | リンク、URL、表、タグ、太字、インラインコードが同一 | 捏造された引用行が1行（🇺🇸＋言い換え）、出典表記が1件重複               |
| `ollama/qwen3.5-9b-32k`（ローカル）          | 8分18秒  | リンク、URL、表、タグが同一                    | 捏造された引用行が1行、太字とインラインコードが数か所追加、1セグメントを再処理 |

その後、この2つのローカルモデルは**除外**されました。記事ごとに1か所でも
勝手な改変があれば、公開用翻訳モデルとしては失格です。他の5モデルも、
同じ理由またはタイムアウトにより除外されました（`gemma4:26b-a4b`、
`qwen3.6:35b-a3b`、`ministral-3:14b`、`mistral-small3.2`、`hy-mt2:7b`）。
採用されたのは `gpt-oss:20b` のみですが、このモデルですら密度の高い記事では
フランス語の箇所を残すことがあります。推奨モデルの表を参照してください。

ローカル翻訳中は、GPU 使用率98%、消費電力170 W、VRAM 使用量10 GB
（モデルと32 kトークンのキャッシュを格納し、RAM へのオフロードなし）、
Ollama サーバーの RAM 使用量は7.5 GBでした。90億～120億パラメータのモデルは
構造を保ちますが、ゲートウェイモデルが一切行わなかった勝手な改変を記事ごとに1か所行います。
公開前に見直すか、下書き専用にしてください。

### OpenRouter 経由で翻訳する（`--use_openrouter`）

OpenRouter は、サードパーティーがホストする400以上のモデルの前段に位置する
**ルーター**で、単一のクレジットから従量課金されます。他の provider が扱わないモデル、
特に中国のオープンモデルへ1つのキーでアクセスできます。

```bash
# --model est OBLIGATOIRE : aucun défaut n'est choisi à votre place
aipmt --use_openrouter --model 'z-ai/glm-5.2' --file README.md \
  --target_dir . --source_lang fr --target_lang en
```

ルーティングには実装方針を決めた2つの特徴があり、どちらも測定で確認できます。

- **同一モデルが、上限の異なる数十のホスティング事業者から提供されています。**
  `z-ai/glm-5.3-flash` には23の事業者があり、そのうち1つの出力上限は
  2,048トークンです。対策なしでは、23回に1回の割合で長い翻訳が
  ルーティングによって無作為に切り詰められ、何の通知もありません。プリフライトで
  `/api/v1/models/{modèle}/endpoints` を読み取り、出力上限が8,000トークン未満の事業者や
  ステータスが低下している事業者を除外した後、残りを `allow_fallbacks: false` で固定します。
  これを行わなければ、ルーターは除外済みの事業者へ再び振り分けます。
- **推論は出力と同じ単価で課金されます。** `z-ai/glm-5.2` に同じリクエストを送り、
  応答を「OK」とした場合、モデルのデフォルトでは完了に107トークン、
  推論を無効にすると2トークンでした。そのため、対応しているモデルではデフォルトで
  推論を無効にします。推論を必須とするモデル（`reasoning.mandatory`、カタログ431モデル中288モデル）には、
  デフォルト設定ではなく、**モデルが受け付けると宣言している最低限の effort** を指定します。
  `z-ai/glm-5.3-flash` のデフォルトは `max` であり、翻訳が完了する前に
  32,768出力トークンを使い切りました。上限を引き上げても、effort がその一定割合を
  割り当てるため解決しません。`--reasoning_effort` が引き続き優先され、推論必須モデルへの
  `none` の指定は回避せず、エラーとして通知されます。

プリフライトは **fail-closed** 方式で、選択内容を表示します。

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

カタログに存在しない slug、カタログへの接続失敗、または上限を満たす事業者が
存在しない場合は、課金が発生する前にコマンドを停止します。

その他の点：

- コンテキストウィンドウは定数ではなくカタログから取得されます。セグメンテーションは、
  4,095トークンのモデルも含め、実際の値に合わせて調整されます。
- `--eco` は効果がありません（モデルは `--model` で指定します）。
- `finish_reason=length` で出力が空の場合、切り詰めではなく、推論によって予算が
  消費されたことを意味します。この2つでは必要な対応が逆になるため、メッセージで明示されます。
- 環境変数：`OPENROUTER_API_KEY`（キー。取得先は
  <https://openrouter.ai/keys>）、`OPENROUTER_BASE_URL`（デフォルト
  `https://openrouter.ai/api/v1`、`https://` が必須）、`OPENROUTER_TIMEOUT`
  （呼び出しごとの秒数、デフォルト `900`）、および `OPENROUTER_PREFLIGHT_TIMEOUT`
  （デフォルト `30`）。

### エコノミーモード

より高速で低コストのモデル（gpt-5.6-luna、claude-haiku-4-5、gemini-3.1-flash-lite）を使用します。

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### オプション

| オプション                   | 説明                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 翻訳する単一の Markdown ファイル                                                                            |
| `--source_dir`           | Markdown ファイルを含むソースディレクトリ                                                             |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ                                                               |
| `--source_lang`          | 原文の言語（デフォルト：`fr`）                                                                                  |
| `--target_lang`          | 翻訳先の言語（デフォルト：`en`）                                                                                   |
| `--model`                | 使用する特定のモデル                                                                                  |
| `--eco`                  | エコノミーモデルを使用                                                                              |
| `--use_mistral`          | Mistral AI API を使用                                                                                     |
| `--use_claude`           | Claude API を使用                                                                                         |
| `--use_gemini`           | Gemini API を使用                                                                                         |
| `--use_codex`            | ChatGPT サブスクリプションのクォータで Codex CLI を使用                                                    |
| `--use_grok`             | xAI API（Grok）を使用 — `XAI_API_KEY` が必要                                                           |
| `--use_openrouter`       | OpenRouter を使用 — `OPENROUTER_API_KEY` と `--model fournisseur/modèle` が必要                          |
| `--use_grok_cli`         | Grok サブスクリプションのクォータで Grok CLI を使用                                                        |
| `--use_opencode`         | OpenCode（オープンソース）を使用し、OpenCode で設定されたプロバイダーへ接続。`--model provider/modèle` が必須 |
| `--force`                | 再翻訳を強制                                                                                       |
| `--keep_filename`        | 元のファイル名を維持                                                                          |
| `--news`                 | ニュースモード：英語の引用を保護し、言語別の旗を処理                                      |
| `--add_translation_note` | 翻訳注記を追加                                                                                |
| `--note_position`        | 注記の位置：`top`、`bottom`（デフォルト）、または `both`                                                     |
| `--note_format`          | 注記の形式：`legacy`（デフォルト、太字の段落）または `marker`                                            |
| `--include_model`        | 出力ファイルにモデル名を含める                                                            |
| `--reasoning_effort`     | GPT-5.x の推論 effort：`none`/`low`/`medium`/`high`/`xhigh`                                         |

> **7つの provider フラグは相互に排他的です。** 以前は2つを組み合わせても
> 警告なく受け付けられ、最初に検査されたものへ解決されていました。そのため、
> サブスクリプションのクォータを使うよう指定した翻訳（`--use_codex`、`--use_grok_cli`）が、
> 何の警告もなく従量課金へ送られる可能性がありました。
> 現在、`argparse` はこの組み合わせを拒否します。

### 翻訳注記：位置と形式

`--add_translation_note` を使用すると、translator は注記を上部、下部、または両方に配置でき、
単純なテキスト形式（後方互換）か、Markdown プラグインで処理可能な `marker`
形式で出力できます。

**位置**（`--note_position`）：

- `bottom`（デフォルト）：従来どおり、ファイル末尾に注記を配置します。
- `top`：**YAML frontmatter の後**に注記を挿入します（Astro Content Collections、
  gray-matter などに対して安全です）。
- `both`：上部と下部の両方に注記を挿入します（LLM の呼び出しは1回のみで、
  両方の配置に同じ内容を再利用します）。

**形式**（`--note_format`）：

- `legacy`（デフォルト）：太字の段落 `**...**`。v1.8 と
  バイト単位で完全に同一の動作です。Hugo、GitHub、GitLab、およびあらゆる Markdown renderer と互換性があります。
- `marker`：非表示の Markdown link reference definition（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）の後に、
  太字の blockquote を配置します。GitHub/GitLab でネイティブに読めるほか、Astro 側の
  remark プラグインによるビルド時の処理で、スタイル付きバナーを生成できます
  （blog jls42.org を参照）。

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

| Provider   | 品質重視（デフォルト）                         | エコノミー（`--eco`）      |
| ---------- | ---------------------------------------- | ------------------------- |
| OpenAI     | `gpt-5.6-terra`                          | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                        | `claude-haiku-4-5`        |
| Mistral    | `mistral-large-latest`                   | `mistral-small-latest`    |
| Gemini     | `gemini-3.7-flash`                       | `gemini-3.1-flash-lite`   |
| Codex      | `gpt-5.6-sol`                            | `gpt-5.6-luna`            |
| Grok API   | `grok-4.6`                               | `grok-4.3`                |
| Grok CLI   | `grok-4.6`                               | `grok-4.5`                |
| OpenCode   | `--model provider/modèle` が必須    | 同じ — `--eco` は効果なし |
| OpenRouter | `--model fournisseur/modèle` が必須 | 同じ — `--eco` は効果なし |
## 実用に耐えるモデル

段落をうまく翻訳できるモデルでも、文書全体の構造を保持できるとは限りません。これらの測定値は、上記のコマンドを使用して、3つの文書セットと14の対象言語（en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi）に対して**実際に実行した翻訳**に基づいています。

2つの列がありますが、意味は異なります。**書き出し成功**は、翻訳が完了し、スクリプトのサイレント障害防止チェックを通過してファイルが保存された件数です。**差異なし**は、ソースと構造が同一だった件数です。つまり、セクション、リンク、URL、ブロック、インラインコード、表、引用、フラグがすべて同じものを指します。

### 高密度なブログ記事、`--news` モード

589行、140リンク、21セクション、保護された英語の引用3件。3つの文書の中で最も難易度が高く、`--news` モードではMarkdown構造に加えて、フラグと引用に関する制約も課されます。

| モデル                            | アクセス方法              | 書き出し成功 | 差異なし | 言語別中央値 |
| --------------------------------- | ------------------ | ------- | ---------- | -------------- |
| `gemini-3.7-flash`                | Google API         | 14/14   | **14/14**  | 1分18秒     |
| `gpt-5.6-sol` (`--use_codex`)     | ChatGPTサブスクリプション | 14/14   | **14/14**  | 11分28秒    |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14   | **14/14**  | 5分37秒     |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14   | 13/14      | 26分23秒    |
| `z-ai/glm-5.3-flash`              | OpenRouter         | 12/14   | 12/14      | 15分49秒    |
| `qwen/qwen3.5-27b`                | OpenRouter         | 7/9     | 7/9        | 20分33秒    |
| `claude-sonnet-5`                 | Anthropic API      | 14/14   | 11/14      | 6分31秒     |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14   | 11/14      | 9分27秒     |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14   | 7/14       | 10分09秒    |
| `ollama/gpt-oss-20b-32k`          | ローカル              | 10/14   | 7/14       | 12分39秒    |
| `mistral-large-latest`            | Mistral API        | 11/14   | 5/14       | 5分32秒     |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14    | 3/14       | 37分27秒    |
| `grok-4.6` (`--use_grok_cli`)     | Grokサブスクリプション    | 1/14    | 1/14       | 23分11秒    |
| `moonshotai/kimi-k2.6`            | OpenRouter         | 1/4     | 1/4        | 23分00秒    |

2つのバッチは**クレジット不足により中断**されており、それが分母に反映されています。`qwen3.5-27b` は9言語で停止し、`kimi-k2.6` は4言語で停止しました。後者は40分のタイムアウトと2回の拒否が発生し、1言語あたり約0.33ドルでした。

OpenRouterの行については、測定方法に注意が必要です。これらは`--use_openrouter`が登場する前に、**ルーターのデフォルト設定**で測定されました。その後、`z-ai/glm-5.2`は同梱のproviderを使用し、推論を無効にして再測定されましたが、まったく同じ14/14という結果になりました。`z-ai/glm-5.3-flash`は、ルーターのデフォルト設定で出力予算を使い切ったため2回失敗しました。現在、providerはこれらのモデルに対して、受け付けられる範囲で最も低い推論努力を指定しており、失敗した言語での追試にも成功しています。

### このプロジェクトのREADME、標準Markdown

508行、219件のインラインコード、40件のブロック区切り、45行の表。ここでは`--news`モードを使用していません。難しさはコードの密度にあります。

| モデル                        | 書き出し成功 | 差異なし | 言語別中央値 |
| ----------------------------- | ------- | ---------- | -------------- |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14   | 11/14      | 1分22秒     |
| `gemini-3.7-flash`            | 14/14   | 13/14      | 21秒           |
| `gpt-5.6-sol` (`--use_codex`) | 14/14   | 12/14      | 2分04秒     |
| `opencode/mimo-v2.5-free`     | 9/14    | 7/14       | 3分25秒     |
| `ollama/gpt-oss-20b-32k`      | 9/14    | 1/14       | 3分38秒     |

### よく知られた4プロジェクトのREADME

FastAPI、Ollama、tldr-pages、Vue.jsをGitHubからそのまま取得しました。これらの文書は前述の2つよりも**簡単**であり、そのことが表にも表れています。

| モデル                    | 対象範囲                  | 書き出し成功 | 差異なし |
| ------------------------- | -------------------------- | ------- | ---------- |
| `opencode/mimo-v2.5-free` | 4プロジェクト × 14言語     | 55/56   | 47/56      |
| `grok-4.6`（サブスクリプション）   | 4プロジェクト × ar、hi、ja、zh | 16/16   | 14/16      |
| `ollama/gpt-oss-20b-32k`  | 4プロジェクト × ar、hi、ja、zh | 15/16   | 9/16       |

### ここから分かること

- **3つのモデルは、2つの高密度な文書で一度も情報を失いませんでした**。`gemini-3.7-flash`、ChatGPTサブスクリプション経由の`gpt-5.6-sol`、OpenRouter経由の`z-ai/glm-5.2`です。標準モードで見られた差異は、1つか2つの言語で一組の`**`が反映されなかったことだけで、URL、コードブロック、引用が失われたことはありません。
- **判別要因は`--news`モードではなく、文書の密度です。** サブスクリプション版Grokはブログ記事で14回中13回失敗する一方、公開READMEでは16件中14件に成功しています。失敗の原因は長いセグメントで処理が脱落することであり、追試でも確認されています。該当箇所だけを分離すると正しく翻訳されます。
- **非ラテン文字体系が、予想された分岐点ではありません。** `gpt-oss`では、アラビア語、日本語、ポーランド語、そして**ルーマニア語**でもフランス語の箇所が残ります。一方、MistralとMiMoがインラインコードを失うのは、非ラテン文字体系の場合だけです。
- **推論を無効にしても品質は低下しません。** `z-ai/glm-5.2`は、ルーターのデフォルトで推論を有効にした条件と、`--use_openrouter`で無効にした条件の両方で、14言語すべてを差異なく処理しました。そのうえ、課金対象の出力tokensは18分の1でした。この測定結果が、providerのデフォルト設定の根拠になっています。
- **遅いモデルが安全なモデルとは限りません。** `deepseek-v4-flash-0731`は1言語あたり37分を要しながら14件中4件しか翻訳できず、`qwen3.8-flash`はほぼ完璧な結果を得るために26分かかりました。一方、Geminiは1分18秒で完全な結果を出しました。

### この表が示していないこと

- **これは網羅的なランキングではありません。** OpenRouterだけでも400を超えるモデルを提供していますが、ここで測定したのは約15モデルです。モデルが掲載されていないことは、その品質について何も示しておらず、単に試していないというだけです。
- **これらの測定値には日付があります**。2026年9月4日と5日です。同じ名前のモデルでも内容は変化し、ホスティング事業者は量子化方式や上限を調整し、新しいモデルが毎週登場します。
- **所要時間は順位を示すものではありません。** キャンペーンによって同時翻訳数は3件から6件まで異なり、providerのスループットも時間帯によって変動します。所要時間は規模感の目安にすぎず、比較には使えません。
- **結果はモデルだけでなく、文書にも同じくらい左右されます。** 同じモデルが、ある記事では14言語すべてに成功し、このREADMEでは9言語にしか成功しませんでした。皆さんのファイルは、私たちのファイルとは異なります。
- **最善の方法は、各自の環境で測定することです**。自分の文書の1つを対象言語へ翻訳し、セクション数、リンク数、重複しないURL数、コードブロック数、インラインコード数、表の行数などの構造を比較してください。これはまさに上記のプロトコルが行っていることであり、`aipmt`上の1つのループだけで実行できます。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** - 多言語対応の個人ブログ（15言語）

## 作者

Julien LE SAUX
メール：contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。[LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)を参照してください。

**gpt-5.6-solでフランス語から日本語に翻訳された記事。**
