# AI搭載Markdown翻訳ツール

🌍 [フランス語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [英語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [スペイン語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中国語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [ドイツ語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [韓国語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [アラビア語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [ヒンディー語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [イタリア語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [オランダ語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [ポーランド語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [ポルトガル語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [ルーマニア語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [スウェーデン語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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

**OpenAI**、**Mistral AI**、**Claude (Anthropic)**、**Google Gemini**、**Grok (xAI)**を使用するMarkdownファイル翻訳ツールです。API、従量課金なしのChatGPT（Codex）またはGrokサブスクリプション枠、あるいはオープンソースエージェントの**OpenCode**を介して、ローカルモデル（Ollama）、無料サービス、サブスクリプション（GitHub Copilotなど）、APIキーといった任意のプロバイダーを利用できます。

このPythonスクリプトは、書式、コードブロック、front matterメタデータを保持したまま、Markdownファイルを原文言語から対象言語へ翻訳します。

## 主な機能

- **マルチプロバイダー**：5つのAPI（OpenAI、Mistral、Claude、Gemini、Grok）に加え、従量課金なしでサブスクリプションを利用する2つのCLI（Codex（ChatGPT）とGrok）、さらにOpenCodeで設定済みのあらゆるプロバイダー（ローカルモデルを含む）に接続できるオープンソース（MIT）のOpenCode
- **2026年モデル**：GPT-5.6 Terra、Claude Sonnet 5、Gemini 3.7 Flash
- **エコノミーモード**：より高速で低コストなモデルを使用するためのオプション`--eco`
- **単一ファイル**：単一ファイルを翻訳するためのオプション`--file`
- **インテリジェントな分割**：モデルごとのトークン上限に対応した長文処理
- **コードの保持**：コードブロックとインラインコード（`` `...` ``）を保持
- **ファイル名**：元の名前を維持するためのオプション`--keep_filename`
- **ニュースモード**：ニュース記事内の英語の引用を保護し、国旗を処理するためのオプション`--news`
- **.env設定**：APIキー用の`.env`ファイルをサポート
- **翻訳注記**：文書末尾への注記の追加に任意で対応

## インストール

### ツールを使用する場合

```bash
pip install ai-powered-markdown-translator
```

これにより、`aipmt`コマンドをどこからでも使用できます。Pythonのスクリプトディレクトリが
`PATH`に含まれていない場合も、`python -m aipmt`でまったく同じことが
できます。Python 3.10以降が必要です。

ほかのパッケージから分離してインストールする場合：

```bash
pipx install ai-powered-markdown-translator
```

### プロジェクトに貢献する場合

開発には、引き続きリポジトリのクローンが必要です。テスト、
28言語の翻訳、すべての品質管理ツールはここに含まれています。

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt`は、テスト済み環境を正確に反映した、バージョンが**完全に固定されたロックファイル**です。
`pyproject.toml`で公開されているバージョン範囲は
意図的に広く設定されており、ほかのパッケージに制約を課しません。

### 品質管理ツール（任意ですが推奨）

このプロジェクトでは、書式が不適切なコード、脆弱なコード、またはシークレットを含むコードのコミットを防ぐために、[`pre-commit`](https://pre-commit.com)を使用しています。インストール：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

有効なhook：ruff（lintとformat）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（複雑度）、detect-secrets（APIキー）、mypy（段階的型付け）、Opengrep（SAST）、pip-audit（依存関係のCVE）、unittest。詳細は`CLAUDE.md`の「_Quality / pre-commit_」セクションを参照してください。

## 設定

キーは優先度の高い順に、**3か所**から検索されます。
各場所では、それより優先度の高い場所で未設定の値だけを補います。

|     | 場所                                            | 用途                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 環境変数                     | CI、コンテナ、一時的なオーバーライド |
| 2   | 現在のディレクトリ（または親ディレクトリ）の`.env` | プロジェクト固有のキー            |
| 3   | `~/.config/aipmt/.env`                        | **一度インストールすれば、どこでも有効**   |

`pip install`の後では、3つ目の方法が最も簡単です。

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

このファイルは、変数が絶対パスを指している場合は`XDG_CONFIG_HOME`に従います
（それ以外の場合は仕様どおり無視されます）。Windowsでは`%APPDATA%`に従います。

2つ目の方法は、リポジトリに固有のキーがある場合に便利です。ルートにある`.env`が
ユーザー設定を変更することなく、ユーザー設定より優先されます。また、
環境ですでに定義されている変数は、これら両方より優先されます。

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

キーが見つからない場合、コマンドは呼び出しのトレースを表示せず、
3か所をそれぞれの正確なパスとともに列挙します。

`GEMINI_API_KEY`は`GOOGLE_API_KEY`の代替として使用できます（AI
Studioの規約）。任意の変数：`XAI_BASE_URL`（xAI endpoint、デフォルト
`https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（Anthropic呼び出しごとの秒数、デフォルト
900）、`CODEX_BIN` / `CODEX_TIMEOUT`、`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`、
`GROK_TRANSLATE_SANDBOX`（Grok CLIセクションを参照）、`OPENCODE_BIN` /
`OPENCODE_TIMEOUT`（OpenCodeセクションを参照）、および`OPENROUTER_BASE_URL` /
`OPENROUTER_TIMEOUT` / `OPENROUTER_PREFLIGHT_TIMEOUT`（OpenRouterセクションを参照）。
`regen_translations.sh`側では、`REGEN_PROVIDER`（デフォルトはサブスクリプション上の`codex`）、
`REGEN_MODEL`、`REGEN_ALLOW_PAID_API`（課金対象APIを使用する場合に必須のオーバーライド）、
および`REGEN_JOB_TIMEOUT`（ジョブごとの上限、デフォルト600秒、Codexでは1,800秒）です。

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

このプロバイダーはAPIキーを一切使用しません。公式Codex CLIを
非対話モードで操作するため、翻訳はすでに支払い済みのChatGPT
サブスクリプション（Plus、Pro、Businessなど）の利用枠から差し引かれます。
この用途についてOpenAIが文書化している唯一の方法です。`~/.codex/auth.json`のトークンは
API Platformの呼び出しを認証できず、このスクリプトから読み取られることもありません。

**前提条件：**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

バイナリは、環境変数`CODEX_BIN`、`PATH`、
Pythonパッケージ`openai-codex-cli-bin`の順に検索されます。最後のパッケージは意図的に
`requirements.txt`へ含めていません。サイズが約250 MBあり、任意のプロバイダーのために
すべてのユーザーへ負担を強いることになるためです。

**留意事項：**

- **APIキーは一切使用されません。** `OPENAI_API_KEY`と`CODEX_API_KEY`は
  サブプロセスの環境から削除されるため、`.env`にキーが
  存在していても、翻訳が従量課金へ切り替わることはありません。
- **1セグメント＝プランの5時間枠における1件の「ローカルメッセージ」**です。
  品質重視モデル（`gpt-5.6-sol`、Plusでは5時間あたり10～100メッセージ）ではなく、
  `--eco`（モデル`gpt-5.6-luna`、Plusでは5時間あたり250～2,000メッセージ）を使用してください。
- APIの直接呼び出しより**低速**です。README全体で約45秒かかりますが、
  直接呼び出す場合は数秒です。
- **CIでは拒否されます**（`CI`または`GITHUB_ACTIONS`が定義されている場合）。
  サブスクリプションは個人用セッションファイルで認証されるため、それを共有runnerへ
  配置すると、その上で実行されるすべてのものから再利用可能なIDを利用できる状態になります。
  この経路ではAPIキーを使用してください。
- 環境変数：`CODEX_BIN`（バイナリへの明示的なパス）と
  `CODEX_TIMEOUT`（セグメントごとの秒数、デフォルト`600`）。

### Grokサブスクリプションで翻訳する（`--use_grok_cli`）

`--use_codex`と同じ仕組みで、公式の**Grok Build** CLIを使用します。
翻訳料金はトークン単位で課金されず、Grokサブスクリプション
（SuperGrok / X Premium+）の利用枠から差し引かれます。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**隔離 — 使用前に必ずお読みください。** このプロバイダーは構造上、
`--use_codex`よりも**弱く**、これは意図されたものです。

- Codexは、システムによって強制される境界である`--sandbox read-only`内で動作します。
- 最近の多くのLinux環境では、Grokのsandboxを**適用できません**。
  Ubuntu 24.04以降ではAppArmorが非特権user namespaceをブロックし、
  `/run/podman`が`0700`の場合、コンテナruntimeのsocketに対するdeny-listが
  失敗するためです。さらに、適用できない**組み込み**プロファイルは、
  **警告なく隔離されていない状態で**起動します。
- そのため、スクリプトはデフォルトでプロファイルを要求せず、**警告なく
  フォールバックすることもありません**。代わりに警告を表示します。隔離は、
  CLIの`--deny`ルール（catch-allの`*`を含む）に依存します。
  これは測定済みの唯一の_fail-closed_層であり、不明なルールがある場合は、
  保護を黙って解除するのではなく起動を拒否します。
- OS sandboxを**必須にする**には、`GROK_TRANSLATE_SANDBOX=read-only`を使用します。
  マシンが要件を満たせない場合は起動に失敗しますが、これは意図された動作です。

**利用枠**：Grokのプールは**週単位で、Chat、Imagine、Voiceと共有**されており、
利用量を確認するコマンドはありません。そのため、バッチ処理によって通知なしに
会話用途の利用枠が消費される可能性があります。このため、同時実行数は2に制限され、
`regen_translations.sh`に警告が表示されます。

その他の変数：`GROK_BIN`（バイナリへのパス）、`GROK_TIMEOUT`（デフォルト900秒）。

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
コーディングエージェントです。モデルのプロバイダーではなく、OpenCode 自体に
設定したプロバイダーへの **ルーター** です。API キー、サブスクリプション、
アカウントなしで **無料** モデルを提供する OpenCode Zen ゲートウェイ、または
**ローカル** モデルを利用できます。この provider は `opencode run` を非対話モードで実行し、
ツールを一切使わず、呼び出しを単一の往復に制限します。

ここでは、そのうち **Zen ゲートウェイ** とローカルの **Ollama** という
2 つの経路をエンドツーエンドで測定しました。OpenCode が対応を表明している
その他の経路（GitHub Copilot、LM Studio、llama.cpp）も、provider が
OpenCode としか通信しない設計上、動作するはずです。ただし検証は行っておらず、
この README には確認済みの内容のみを記載しています。

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` は **必須** で、形式は `provider/modèle` です。OpenCode は
プロバイダーではなく、既定値が代わりに選択されることもありません。OpenCode 自体の
フォールバック先は、やり取りが学習に使用される可能性のある無料モデルです。

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**隔離 — スクリプトが呼び出しごとに行うこと：**

- ユーザー設定より優先されるインライン設定（`OPENCODE_CONFIG_CONTENT`）で、
  **すべてのツールを拒否**（`permission: { "*": "deny" }`）する `aipmt`
  エージェントを定義します。モデルは読み取り、書き込み、コマンド実行のいずれも
  行えず、測定時には試行すらしませんでした。セッション共有は無効化され、
  `--pure` は外部プラグインを除外し、`--auto` は決して使用しません。
- 呼び出しは **空の使い捨てディレクトリ** で、`OPENCODE_DISABLE_PROJECT_CONFIG` と
  `OPENCODE_DISABLE_CLAUDE_CODE` のスイッチを有効にして実行されます。これらがない場合、
  OpenCode は各プロンプトへ現在のディレクトリの `AGENTS.md` と
  ユーザーの `~/.claude/CLAUDE.md` を注入します。実測では、`AGENTS.md` に記述した
  「すべての応答を BANANA で終える」という指示が翻訳にも適用されました。
  一方、`~/.config/opencode/AGENTS.md` のグローバルルールは引き続き適用されます。
  OpenCode ではこれを除外できません。
- 出力契約では、終了コード 0、`error` イベントなし、ツール呼び出しなし、
  最後のステップが `stop` で完了、空でないテキスト、指定したエージェントが
  実際に読み込まれていることを、すべて同時に要求します。不明な `--agent` を
  指定しても OpenCode は失敗せず、ツールが有効なコーディングエージェントへ
  **暗黙にフォールバック** します。ここでは `exit 0` も何の証明にもなりません。
- **aipmt のキーは一切** サブプロセスへ渡されません（Codex および Grok と
  同じフィルタリング）。ただし、OpenCode 自体（Zen、Go）のキーである
  `OPENCODE_API_KEY` だけは、明示的な例外です。プロバイダーは aipmt の
  `.env` ではなく、OpenCode 内（`opencode auth login`、`opencode.json`）で設定します。

**留意事項：**

- **Zen の無料モデルは「stealth」モデルまたはコントリビューターモデル** であり、
  頻繁に変更され、制限も文書化されておらず、やり取りが学習に使用される可能性があります。
  公開ドキュメントには最適ですが、非公開コンテンツには使用しないでください。実測では、
  `opencode/mimo-v2.5-free` はこの README を 1 回で翻訳しました。`opencode/big-pickle` はより遅く、
  2 件の同時リクエストが応答のないまま停止しました。
- **ローカルモデルには少なくとも 16 k のコンテキストが必要です**。セグメントは
  最大 16,000 文字ですが、Ollama の既定値は多くの場合 4,096 です。Ollama では、
  `PARAMETER num_ctx 32768` を含む `Modelfile` を作成し、その後 `ollama create` を
  実行します。品質はモデル次第です。テストファイルでは、ゲートウェイのモデルが
  すべてを保持した一方、7B モデルはリストを逆順にし、コードブロックの閉じ記号を
  壊しました。
- `--eco` は効果がありません（モデルは `--model` で指定します）。
  `--reasoning_effort` は OpenCode の `--variant` としてそのまま渡されるため、
  モデルが対応している場合にのみ指定してください。
- セッションは、通常の OpenCode セッションと同様に OpenCode のデータベース
  （`~/.local/share/opencode/`）へ記録されます。
- 環境変数：`OPENCODE_BIN`（バイナリの明示的なパス。未指定時は
  `PATH`、次に `~/.opencode/bin/opencode`）および `OPENCODE_TIMEOUT`
  （セグメントごとの秒数、既定値 `600`）。`OPENCODE_CONFIG` が
  エクスポートされている場合、`aipmt` はそれを読み取りません。
  値はそのまま OpenCode に渡され、OpenCode が適用します。

**測定例：Ollama 経由のローカルモデル**（RTX 3060 12 GB、RAM 62 GB、Ollama 0.33.3）

```bash
curl -fsSL https://ollama.com/install.sh | sh   # conserve les modèles déjà téléchargés
ollama pull gpt-oss:20b                         # 13 Go, Apache 2.0 — le seul modèle local retenu ici

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

次に `~/.config/opencode/opencode.json` でプロバイダーを指定します：

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
推論を既定で有効にし、Modelfile から無効化することはできません。OpenCode
経由の実測では、このオプションなしで「猫は敷物の上で寝ている」を処理すると
推論に 919 tokens と 68 秒を要しましたが、オプションありでは 9 tokens でした。

```bash
aipmt --use_opencode --model ollama/gpt-oss-20b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

実際の 589 行のブログ記事（リンク 140 件、セクション 21 件、
`--news` モードで保護された英語の引用 3 件）に対し、同じコマンドを
3 つのモデルで実行した結果：

| モデル                                   | 所要時間       | 構造                                                  | 相違点                                                                                    |
| ---------------------------------------- | ----------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free`（Zen、無料） | 4 分 26 秒  | ソースと同一                                      | なし                                                                                     |
| `ollama/gemma4-12b-32k`（ローカル）          | 10 分 10 秒 | リンク、URL、表、タグ、太字、インラインコードが同一 | 捏造された引用 1 行（🇺🇸＋言い換え）、重複した帰属表記               |
| `ollama/qwen3.5-9b-32k`（ローカル）          | 8 分 18 秒  | リンク、URL、表、タグが同一                    | 捏造された引用 1 行、追加された太字とインラインコード数か所、再処理されたセグメント 1 件 |

この 2 つのローカルモデルは、その後 **除外** されました。記事ごとに 1 か所でも
原文から逸脱すれば、公開翻訳用モデルとしては不適格です。ほかの 5 つも、
同じ理由またはタイムアウトにより除外されました（`gemma4:26b-a4b`、
`qwen3.6:35b-a3b`、`ministral-3:14b`、`mistral-small3.2`、`hy-mt2:7b`）。
採用されたのは `gpt-oss:20b` だけですが、このモデルも密度の高い記事では
フランス語の文章を残します。推奨モデルの表を参照してください。

ローカル翻訳中は、GPU 使用率 98%、消費電力 170 W、VRAM 使用量 10 GB
（モデルと 32 k tokens のキャッシュ。RAM へのオフロードなし）、Ollama
サーバーの RAM 使用量は 7.5 GB でした。90 億〜120 億パラメーターのモデルは
構造を守りますが、記事ごとに 1 か所ほど原文から逸脱します。一方、
ゲートウェイのモデルには逸脱がありませんでした。公開前に校正するか、
下書き専用にしてください。

### OpenRouter 経由で翻訳する（`--use_openrouter`）

OpenRouter は、第三者がホストする 400 を超えるモデルの前段に置かれる
**ルーター** であり、単一のクレジットから従量課金されます。1 つのキーで、
ほかの provider が提供していないモデル、特に中国製のオープンモデルを利用できます。

```bash
# --model est OBLIGATOIRE : aucun défaut n'est choisi à votre place
aipmt --use_openrouter --model 'z-ai/glm-5.2' --file README.md \
  --target_dir . --source_lang fr --target_lang en
```

ルーティングには実装方針を決めた 2 つの特性があり、どちらも測定可能です：

- **同じモデルが、上限の異なる数十のホスティング事業者から提供されます。**
  `z-ai/glm-5.3-flash` には 23 のホスティング事業者があり、そのうち 1 つの
  出力上限は 2,048 tokens です。対策しなければ、長い翻訳はルーティング先次第で
  23 回に 1 回、何の通知もなく切り詰められました。プリフライトで
  `/api/v1/models/{modèle}/endpoints` を読み取り、出力上限が 8,000 tokens 未満または状態が
  劣化している事業者を除外し、残りを `allow_fallbacks: false` で固定します。
  これを行わなければ、ルーターは除外した事業者へ再び転送します。
- **推論は出力と同じ料金で課金されます。** `z-ai/glm-5.2` に同じ
  リクエストを送り「OK」と応答させると、モデルの既定設定では completion が
  107 tokens、推論を無効にすると 2 tokens でした。そのため、無効化を許可する
  モデルでは既定で推論を無効にします。推論を強制するモデル
  （`reasoning.mandatory`、カタログ掲載 431 モデル中 288 モデル）には、
  既定設定ではなく、モデルが対応すると宣言している **最小の effort** を指定します。
  `z-ai/glm-5.3-flash` の既定値は `max` で、翻訳が終わる前に
  32,768 tokens の出力上限へ達していました。上限を増やしても、effort が
  その一定割合を割り当てるため解決しません。`--reasoning_effort` は引き続き優先され、
  推論を強制するモデルに `none` を指定した場合は、回避せずエラーとして通知します。

プリフライトは **fail-closed** 方式で、選択内容を表示します：

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

カタログに存在しない slug、アクセスできないカタログ、または上限を満たす
ホスティング事業者がない場合は、課金が発生する前にコマンドを停止します。

その他のポイント：

- コンテキストウィンドウは定数ではなくカタログから取得します。そのため、
  4,095 tokens のモデルを含め、セグメンテーションが実際の値に適応します。
- `--eco` は効果がありません（モデルは `--model` で指定します）。
- `finish_reason=length` で出力が空の場合、切り詰めではなく推論が予算を使い切った
  状態です。両者では必要な対処が反対になるため、メッセージにその旨を明記します。
- 環境変数：`OPENROUTER_API_KEY`（キー、<https://openrouter.ai/keys> で取得）、
  `OPENROUTER_BASE_URL`（既定値 `https://openrouter.ai/api/v1`、`https://` が必須）、
  `OPENROUTER_TIMEOUT`（呼び出しごとの秒数、既定値 `900`）、
  `OPENROUTER_PREFLIGHT_TIMEOUT`（既定値 `30`）。

### エコノミーモード

より高速で低コストなモデル（gpt-5.6-luna、claude-haiku-4-5、gemini-3.1-flash-lite）を使用します：

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### オプション

| オプション                   | 説明                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | 翻訳する単一の Markdown ファイル                                                                            |
| `--source_dir`           | Markdown ファイルを含むソースディレクトリ                                                             |
| `--target_dir`           | 翻訳済みファイルの出力ディレクトリ                                                               |
| `--source_lang`          | 翻訳元言語（既定値：`fr`）                                                                                  |
| `--target_lang`          | 翻訳先言語（既定値：`en`）                                                                                   |
| `--model`                | 使用する特定のモデル                                                                                  |
| `--eco`                  | エコノミーモデルを使用                                                                              |
| `--use_mistral`          | Mistral AI API を使用                                                                                     |
| `--use_claude`           | Claude API を使用                                                                                         |
| `--use_gemini`           | Gemini API を使用                                                                                         |
| `--use_codex`            | ChatGPT サブスクリプションのクォータで Codex CLI を使用                                                    |
| `--use_grok`             | xAI API（Grok）を使用 — `XAI_API_KEY` が必要                                                           |
| `--use_openrouter`       | OpenRouter を使用 — `OPENROUTER_API_KEY` と `--model fournisseur/modèle` が必要                          |
| `--use_grok_cli`         | Grok サブスクリプションのクォータで Grok CLI を使用                                                        |
| `--use_opencode`         | OpenCode（オープンソース）を使用し、OpenCode で設定したプロバイダーへ接続。`--model provider/modèle` が必須 |
| `--force`                | 再翻訳を強制                                                                                       |
| `--keep_filename`        | 元のファイル名を維持                                                                          |
| `--news`                 | ニュースモード：英語の引用を保護し、言語ごとの国旗を処理                                      |
| `--add_translation_note` | 翻訳注記を追加                                                                                |
| `--note_position`        | 注記の位置：`top`、`bottom`（既定値）、または `both`                                                     |
| `--note_format`          | 注記の形式：`legacy`（既定値、太字段落）または `marker`                                            |
| `--include_model`        | 出力ファイルにモデル名を含める                                                            |
| `--reasoning_effort`     | GPT-5.x の推論 effort：`none`/`low`/`medium`/`high`/`xhigh`                                         |

> **8 つの provider フラグは相互排他的です。** 以前は 2 つを組み合わせても
> 暗黙に受け入れられ、最初に確認されたものが選択されていました。そのため、
> サブスクリプションのクォータ（`--use_codex`、`--use_grok_cli`）で
> 実行するよう指定した翻訳が、警告なしに従量課金へ回される可能性がありました。
> 現在は `argparse` がこの組み合わせを拒否します。

### 翻訳注記：位置と形式

`--add_translation_note` を指定すると、translator は注記を上部、下部、または
両方に配置し、後方互換性のあるプレーンテキスト形式か、Markdown プラグインで
処理可能な `marker` 形式で出力できます。

**位置**（`--note_position`）：

- `bottom`（既定値）：従来どおりファイル末尾に注記を配置します。
- `top`：注記を **YAML frontmatter の後** に挿入します
  （Astro Content Collections、gray-matter などで安全）。
- `both`：注記を上部と下部の両方に挿入します
  （LLM 呼び出しは 1 回のみで、両方の配置に同じ内容を再利用）。

**形式**（`--note_format`）：

- `legacy`（既定値）：太字段落 `**...**`。v1.8 と
  byte-for-byte で完全に同じ動作です。Hugo、GitHub、GitLab、および
  あらゆる Markdown renderer と互換性があります。
- `marker`：非表示の Markdown link reference definition
  （`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）の後に太字の blockquote を配置します。
  GitHub/GitLab でそのまま表示でき、Astro 側の remark プラグインで
  build 時に処理して、スタイル付きバナーを生成できます（blog jls42.org を参照）。

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

### 既定モデル（2026年）

| Provider   | 品質重視（既定値）                         | エコノミー（`--eco`）      |
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

段落をうまく翻訳できるモデルでも、文書全体の構造を維持できるとは限りません。これらの測定値は、上記のコマンドを使用して、3つの文書セットと14の対象言語（en、es、de、it、pt、nl、pl、sv、ro、ja、ko、zh、ar、hi）について**実際に実行した翻訳**から得たものです。

2つの列は、それぞれ異なることを示しています。**生成済み**は、翻訳が完了し、スクリプトのサイレント失敗防止チェックを通過したファイル数です。**完全一致**は、構造が原文と同一だったものの数です。つまり、セクション、リンク、URL、ブロック、インラインコード、表、引用、フラグがすべて一致しています。

### 情報量の多いブログ記事、`--news` モード

589行、140個のリンク、21セクション、保護された英語の引用3件。3つの中で最も難しい文書です。`--news` モードでは、Markdown構造に加えて、フラグと引用に関する制約も課されます。

| モデル                            | アクセス方法              | 生成済み | 完全一致 | 言語ごとの中央値 |
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

2つのバッチは**クレジット不足のため中断**され、そのことが分母に反映されています。`qwen3.5-27b` は9言語で、`kimi-k2.6` は4言語で停止しました。後者は40分のタイムアウトと2回の拒否が発生し、1言語あたり約0.33ドルかかりました。

OpenRouterの行については、測定方法に留意が必要です。これらは、`--use_openrouter` が登場する前に、**ルーターのデフォルト設定**で測定されました。その後、`z-ai/glm-5.2` は同梱のプロバイダーを使用し、推論を無効にして再測定されましたが、まったく同じ14/14という結果になりました。`z-ai/glm-5.3-flash` は、ルーターのデフォルト設定で出力予算を使い切ったため2回失敗しました。現在、プロバイダーはこれらのモデルに対して、対応可能な最低の推論強度を要求するようになっており、失敗した言語での再検証にも合格しています。

### このプロジェクトのREADME、標準Markdown

508行、219個のインラインコード、40個のブロック区切り、45行の表。ここでは `--news` モードを使用していません。難しさはコードの密度にあります。

| モデル                        | 生成済み | 完全一致 | 言語ごとの中央値 |
| ----------------------------- | ------- | ---------- | -------------- |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14   | 11/14      | 1分22秒     |
| `gemini-3.7-flash`            | 14/14   | 13/14      | 21秒           |
| `gpt-5.6-sol` (`--use_codex`) | 14/14   | 12/14      | 2分04秒     |
| `opencode/mimo-v2.5-free`     | 9/14    | 7/14       | 3分25秒     |
| `ollama/gpt-oss-20b-32k`      | 9/14    | 1/14       | 3分38秒     |

### 有名プロジェクト4件のREADME

FastAPI、Ollama、tldr-pages、Vue.jsのREADMEを、GitHubからそのまま取得しました。これらの文書は、先の2つよりも**簡単**であり、そのことは表にも表れています。

| モデル                    | 対象範囲                  | 生成済み | 完全一致 |
| ------------------------- | -------------------------- | ------- | ---------- |
| `opencode/mimo-v2.5-free` | 4プロジェクト × 14言語     | 55/56   | 47/56      |
| `grok-4.6` (サブスクリプション)   | 4プロジェクト × ar、hi、ja、zh | 16/16   | 14/16      |
| `ollama/gpt-oss-20b-32k`  | 4プロジェクト × ar、hi、ja、zh | 15/16   | 9/16       |

### ここから分かること

- **3つのモデルは、情報量の多い2つの文書で一度も情報を失いませんでした**。`gemini-3.7-flash`、ChatGPTサブスクリプション経由の `gpt-5.6-sol`、OpenRouter経由の `z-ai/glm-5.2` です。標準モードで生じた唯一の不一致は、1つか2つの言語で `**` の組が反映されなかったことだけで、URL、コードブロック、引用が失われたことは一度もありません。
- **結果を左右する要因は文書の密度であり、`--news` モードではありません。** サブスクリプション版Grokは、ブログ記事では14回中13回失敗した一方、公開READMEでは16件中14件に成功しました。失敗原因は長いセグメントでの脱落であり、再検証でも確認されています。問題の箇所だけを切り出すと、正しく翻訳されます。
- **非ラテン文字が、予想された分岐点というわけではありません。** `gpt-oss` は、アラビア語、日本語、ポーランド語、さらに**ルーマニア語**でもフランス語の箇所を残しています。一方、MistralとMiMoがインラインコードを失うのは、非ラテン文字の言語だけです。
- **推論を無効にしても品質は低下しません。** `z-ai/glm-5.2` は、ルーターのデフォルトで推論を有効にした条件と、`--use_openrouter` によって推論を無効にした条件の両方で、14言語すべてを不一致なく処理しました。しかも、課金対象の出力トークンは18分の1です。この測定結果が、プロバイダーのデフォルト設定を正当化しています。
- **遅いモデルが安全なモデルとは限りません。** `deepseek-v4-flash-0731` は1言語あたり37分かかっても14件中4件しか翻訳できず、`qwen3.8-flash` はほぼ完璧な結果を出すのに26分かかりました。一方、Geminiは1分18秒で完全な結果を出しました。

### この表が示していないこと

- **これは網羅的なランキングではありません。** OpenRouterだけでも400を超えるモデルを提供していますが、ここで測定したのは約15モデルです。掲載されていないモデルの品質については何も分かりません。単に試していないというだけです。
- **これらの測定値には日付があります**。2026年9月4日と5日です。同じ名前でもモデルは変化し、ホスティング事業者は量子化や上限を調整し、新しいモデルが毎週登場します。
- **所要時間はランキングを意味しません。** キャンペーンごとに3件から6件の翻訳を並列実行しており、プロバイダーのスループットも時間帯によって変動します。所要時間は規模の目安にすぎず、比較には使えません。
- **結果はモデルだけでなく、文書にも左右されます。** 同じモデルでも、ある記事では14言語に成功し、このREADMEでは9言語にしか成功しません。皆さんのファイルは、私たちのものとは異なります。
- **最善の方法は、実際の環境で測定することです**。手元の文書を対象言語に翻訳し、セクション数、リンク数、異なるURLの数、コードブロック数、インラインコード数、表の行数などの構造を比較してください。上記のプロトコルが行っているのはまさにこれであり、`aipmt` を使った1つのループで実行できます。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** - 多言語対応の個人ブログ（15言語）

## 作者

Julien LE SAUX
メール：contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。[LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE)を参照してください。

**gpt-5.6-solを使用してフランス語から日本語に翻訳された記事。**
