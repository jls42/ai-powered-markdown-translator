# AI 搭載 Markdown 翻訳ツール

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
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy バッジ"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

**OpenAI**、**Mistral AI**、**Claude (Anthropic)**、**Google Gemini**、**Grok (xAI)** を使用する Markdown ファイル翻訳ツールです。API、従量課金なしの ChatGPT（Codex）または Grok サブスクリプション枠、あるいはオープンソースエージェントの **OpenCode** を介して、ローカルモデル（Ollama）、無料サービス、サブスクリプション（GitHub Copilot など）、API キーといった任意のプロバイダーを利用できます。

この Python スクリプトは、書式、コードブロック、front matter メタデータを維持しながら、Markdown ファイルを原文言語から対象言語へ翻訳します。

## 主な機能

- **複数プロバイダー対応**：5 つの API（OpenAI、Mistral、Claude、Gemini、Grok）に加え、従量課金なしでサブスクリプションを利用する 2 つの CLI（Codex（ChatGPT）と Grok）、さらにローカルモデルを含む OpenCode で設定済みの任意のプロバイダーに接続できる OpenCode（オープンソース、MIT）に対応
- **2026 年モデル**：GPT-5.6 Terra、Claude Sonnet 5、Gemini 3.7 Flash
- **エコノミーモード**：より高速で低コストなモデルを使用する `--eco` オプション
- **単一ファイル**：1 ファイルのみを翻訳する `--file` オプション
- **インテリジェントな分割**：モデルごとのトークン上限に応じて長文を処理
- **コードの保持**：コードブロックとインラインコード（`` `...` ``）を保持
- **ファイル名**：元の名前を保持する `--keep_filename` オプション
- **ニュースモード**：ニュース記事内の英語の引用を保護し、国旗を処理する `--news` オプション
- **.env 設定**：API キー用の `.env` ファイルをサポート
- **翻訳注記**：文書末尾への注記の追加に任意で対応

## インストール

### ツールを使用する場合

```bash
pip install ai-powered-markdown-translator
```

これで `aipmt` コマンドをどこからでも使用できます。Python のスクリプトディレクトリが
`PATH` に含まれていない場合も、`python -m aipmt` でまったく同じことが
できます。Python 3.10 以降が必要です。

ほかのパッケージから分離してインストールするには：

```bash
pipx install ai-powered-markdown-translator
```

### プロジェクトに貢献する場合

開発には、引き続きリポジトリのクローンが必要です。テスト、
28 言語への翻訳、すべての品質管理ツールがそこに含まれています。

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` は、テスト済み環境を正確に反映した、**すべてのバージョンが固定されたロックファイル**です。
`pyproject.toml` で公開されているバージョン範囲は
意図的に広く設定されており、ほかのパッケージに制約を課しません。

### 品質管理ツール（任意、ただし推奨）

このプロジェクトでは、書式が不正なコード、脆弱なコード、シークレットを含むコードのコミットを防ぐために [`pre-commit`](https://pre-commit.com) を使用しています。インストール方法：

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

有効なフック：ruff（lint＋format）、shellcheck（bash）、prettier（markdown/yaml/json）、Lizard（複雑度）、detect-secrets（API キー）、mypy（段階的型付け）、Opengrep（SAST）、pip-audit（依存関係の CVE）、unittest。詳細は `CLAUDE.md` の _品質 / pre-commit_ セクションを参照してください。

## 設定

キーは、優先度の高い順に**3 か所**から検索されます。
各場所は、それより前の場所で未設定だった項目だけを補完します。

|     | 場所                                            | 用途                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | 環境変数                     | CI、コンテナ、一時的な上書き |
| 2   | 現在のディレクトリ（または親ディレクトリ）の `.env` | プロジェクト固有のキー            |
| 3   | `~/.config/aipmt/.env`                        | **一度インストールすれば、どこでも有効**   |

`pip install` の後では、3 番目の方法が最も簡単です：

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

環境変数が絶対パスを示す場合、このファイルは `XDG_CONFIG_HOME` に従います
（それ以外の場合は仕様どおり無視されます）。Windows では `%APPDATA%`
に従います。

リポジトリ固有のキーがある場合は、2 番目の方法が引き続き便利です。ルートにある `.env` が、
ユーザー設定を変更することなく優先されます。また、環境ですでに定義されている
変数は、両方より優先されます：

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

キーが見つからない場合、コマンドは呼び出しトレースを表示せず、
3 つの場所とそれぞれの正確なパスを列挙します。

`GEMINI_API_KEY` は `GOOGLE_API_KEY` の代替として受け付けられます（AI
Studio の規約）。任意の変数：`XAI_BASE_URL`（xAI の endpoint、既定値
`https://api.x.ai/v1`）、`CLAUDE_TIMEOUT`（Anthropic の呼び出しごとの秒数、既定値
900）、`CODEX_BIN` / `CODEX_TIMEOUT`、`GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`、
`GROK_TRANSLATE_SANDBOX`（Grok CLI セクションを参照）、`OPENCODE_BIN` /
`OPENCODE_TIMEOUT`（OpenCode セクションを参照）。`regen_translations.sh` 側では：
`REGEN_PROVIDER`（既定値 `codex`、サブスクリプション経由）、
`REGEN_MODEL`、`REGEN_ALLOW_PAID_API`（有料 API を使用する場合に必須の明示的な上書き）、
`REGEN_JOB_TIMEOUT`（ジョブごとの上限、既定値 600 秒、Codex では 1,800 秒）。

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

### ChatGPT サブスクリプションで翻訳する（`--use_codex`）

このプロバイダーは API キーを使用しません。公式 Codex CLI を
非対話モードで操作するため、翻訳はすでに支払い済みの
ChatGPT サブスクリプション（Plus、Pro、Business など）の利用枠から差し引かれます。
この用途について OpenAI が文書化している唯一の方法です。`~/.codex/auth.json` のトークンでは
API Platform の呼び出しを認証できず、このスクリプトがそれらを読み取ることもありません。

**前提条件：**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

バイナリは、環境変数 `CODEX_BIN`、`PATH`、
Python パッケージ `openai-codex-cli-bin` の順に検索されます。最後のパッケージは意図的に
`requirements.txt` に含めていません。容量が約 250 MB あり、任意のプロバイダーのために
すべてのユーザーへ負担を強いることになるためです。

**注意事項：**

- **API キーは一切使用されません。** `OPENAI_API_KEY` と `CODEX_API_KEY` は
  サブプロセスの環境から削除されるため、`.env` にキーが
  存在していても、翻訳が従量課金へ切り替わることはありません。
- **1 セグメント＝5 時間枠における 1 件の「ローカルメッセージ」**です。
  品質重視モデル（`gpt-5.6-sol`、Plus では 10～100 メッセージ / 5 時間）ではなく、
  `--eco`（モデル `gpt-5.6-luna`、Plus では 250～2,000 メッセージ / 5 時間）を使用してください。
- API を直接呼び出す場合より**低速**です。README 全体で約 45 秒かかるのに対し、
  直接呼び出す場合は数秒です。
- **CI では拒否されます**（`CI` または `GITHUB_ACTIONS` が定義されている場合）。
  サブスクリプション認証は共有 runner 向けではなく、OpenAI も
  公開リポジトリでのこの workflow を推奨していません。この経路では API キーを使用してください。
- 環境変数：`CODEX_BIN`（バイナリへの明示的なパス）と
  `CODEX_TIMEOUT`（セグメントごとの秒数、既定値 `600`）。

### Grok サブスクリプションで翻訳する（`--use_grok_cli`）

`--use_codex` と同じ原理で、公式の **Grok Build** CLI を使用します。
翻訳料金はトークン単位で請求されず、Grok サブスクリプション（SuperGrok / X Premium+）の
利用枠から差し引かれます。

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**隔離 — 使用前に必ずお読みください。** このプロバイダーは構造上、
`--use_codex` よりも**弱い**ものですが、これは意図した設計です：

- Codex は、システムによって強制される境界である `--sandbox read-only` 内で動作します。
- 最近の多くの Linux 環境では、Grok の sandbox を**適用できません**。
  Ubuntu 24.04 以降では AppArmor が非特権 user namespace をブロックし、
  `/run/podman` が `0700` にある場合は、コンテナ runtime socket の
  deny-list が機能しないためです。しかも、適用できない**組み込み**プロファイルは、
  **隔離されていない状態で警告なく**起動します。
- そのため、スクリプトは既定ではプロファイルを要求せず、**警告なしで
  フォールバックすることもありません**。代わりに警告を表示します。隔離は CLI の
  `--deny` ルール（catch-all の `*` を含む）に依存します。これは実測上、
  _fail-closed_ となる唯一の層です。不明なルールがある場合、保護を黙って
  解除するのではなく、起動を拒否します。
- OS の sandbox を**必須にする**には：`GROK_TRANSLATE_SANDBOX=read-only`。
  マシンが対応できない場合は起動に失敗します。これは意図した動作です。

**利用枠**：Grok のプールは**週単位で、Chat、Imagine、Voice と共有**されており、
その残量を確認できるコマンドはありません。そのため、バッチ処理が何の通知もなく
会話での利用枠を消費する可能性があります。これを踏まえ、同時実行数は 2 に制限され、
`regen_translations.sh` に警告が表示されます。

その他の変数：`GROK_BIN`（バイナリのパス）、`GROK_TIMEOUT`（既定値 900 秒）。

28 言語への翻訳を再生成するには：

```bash
# Défaut : Codex sur l'abonnement ChatGPT, modèle qualité gpt-5.6-sol, 0 € à l'usage
./regen_translations.sh --force

# Le modèle éco de Codex, si le volume l'impose
REGEN_MODEL=gpt-5.6-luna ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force

# Une API facturée (openai, gemini, grok) est REFUSÉE sans cette dérogation nommée
REGEN_PROVIDER=openai REGEN_ALLOW_PAID_API=1 ./regen_translations.sh --force

# Via OpenCode, vers le modèle de son choix (REGEN_MODEL obligatoire, 2 jobs en parallèle)
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
```

### OpenCode を介して任意のプロバイダーで翻訳する（`--use_opencode`）

[OpenCode](https://opencode.ai) は、ターミナルで動作する**オープンソース（MIT）**の
コーディングエージェントです。モデルプロバイダーそのものではなく、OpenCode 内で
設定したプロバイダーへの**ルーター**です。API キー、サブスクリプション
（GitHub Copilot、ChatGPT、SuperGrok）、**アカウント不要**で無料モデルを提供する
OpenCode Zen ゲートウェイ、または**ローカル**モデル（Ollama、LM Studio、
llama.cpp）を利用できます。このプロバイダーは `opencode run` を非対話モードで操作し、
ツールを一切使わない 1 回だけの往復処理に呼び出しを制限します。

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` は**必須**で、形式は `provider/modèle` です。OpenCode は
プロバイダーではないため、既定値が代理で選択されることはありません。OpenCode 自体の
フォールバック先は、やり取りが学習に使用される可能性のある無料モデルだからです。

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**隔離 — スクリプトが各呼び出しで行う処理：**

- ユーザー設定より優先されるインライン設定（`OPENCODE_CONFIG_CONTENT`）で、
  **すべてのツールが拒否される**（`permission: { "*": "deny" }`）エージェント
  `aipmt` を定義します。モデルは読み取り、書き込み、コマンド実行の
  いずれもできず、実測では試行すらしません。セッション共有は無効化され、
  `--pure` は外部プラグインを除外しますが、`--auto` は決して使用しません。
- 呼び出しは、**使い捨ての空ディレクトリ**内で、`OPENCODE_DISABLE_PROJECT_CONFIG` と
  `OPENCODE_DISABLE_CLAUDE_CODE` の切り替えを有効にして実行されます。これらがない場合、
  OpenCode は現在のディレクトリの `AGENTS.md` とユーザーの `~/.claude/CLAUDE.md` を
  各プロンプトへ挿入します。実測では、`AGENTS.md` に記述した
  「すべての応答を BANANA で終える」という指示が翻訳にも適用されました。
  一方、`~/.config/opencode/AGENTS.md` のグローバルルールは引き続き適用されます。
  OpenCode ではこれらを除外できません。
- 出力契約では、終了コード 0、`error` イベントなし、ツール呼び出しなし、
  最後のステップが `stop` で完了、空でないテキスト、指定したエージェントが
  実際に読み込まれたことのすべてを要求します。不明な `--agent` を指定しても
  OpenCode は失敗せず、ツールが有効なコーディングエージェントへ**警告なく
  フォールバック**します。ここでは `exit 0` も証明にはなりません。
- aipmt の**キーは一切サブプロセスへ渡されません**（Codex および Grok と
  同じフィルタリング）。唯一、明示的な例外となるのは OpenCode 自体（Zen、Go）の
  キーである `OPENCODE_API_KEY` です。プロバイダーは aipmt の `.env` ではなく、
  OpenCode（`opencode auth login`、`opencode.json`）で設定します。

**注意事項：**

- **Zen の無料モデルは「stealth」モデルまたは貢献者提供モデル**であり、
  頻繁に変更され、上限も文書化されていません。また、やり取りが学習に
  使用される可能性があります。公開文書には最適ですが、非公開コンテンツには
  適しません。実測では、`opencode/mimo-v2.5-free` はこの README を 1 回で翻訳します。
  `opencode/big-pickle` はより遅く、同時に送信した 2 件のリクエストが応答なしのままになりました。
- **ローカルモデルには少なくとも 16 k のコンテキストが必要**です。セグメントは
  最大 16,000 文字ですが、Ollama の既定値は多くの場合 4,096 です。
  Ollama では、`PARAMETER num_ctx 32768` を指定した `Modelfile` を作成し、
  その後 `ollama create` を実行します。品質はモデルに依存します。テストファイルでは、
  ゲートウェイのモデルがすべてを保持した一方、7B モデルはリストの順序を逆転させ、
  コードブロックのフェンスを壊しました。
- `--eco` は効果がありません（モデルは `--model` で指定されます）。
  `--reasoning_effort` は OpenCode の `--variant` としてそのまま渡されるため、
  モデルが対応している場合にのみ指定してください。
- セッションは通常の OpenCode セッションと同様に、OpenCode のデータベース
  （`~/.local/share/opencode/`）へ記録されます。
- 環境変数：`OPENCODE_BIN`（バイナリへの明示的なパス。
  未指定の場合は `PATH`、次に `~/.opencode/bin/opencode`）と `OPENCODE_TIMEOUT`
  （セグメントごとの秒数、既定値 `600`）。`OPENCODE_CONFIG` を
  エクスポートしている場合は、その値が尊重されます。

**実測例：Ollama 経由のローカルモデル**（RTX 3060 12 GB、RAM 62 GB、Ollama 0.33.3）

```bash
curl -fsSL https://ollama.com/install.sh | sh   # Ollama ≥ 0.30 pour gemma4 ; conserve les modèles déjà téléchargés
ollama pull gemma4:12b                          # 7,6 Go, Apache 2.0, 140+ langues
ollama pull qwen3.5:9b                          # 6,6 Go, Apache 2.0, 201 langues

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gemma4:12b\nPARAMETER num_ctx 32768\n' > gemma4-12b-32k.Modelfile
ollama create gemma4-12b-32k -f gemma4-12b-32k.Modelfile
```

続いて `~/.config/opencode/opencode.json` 内でプロバイダーを設定します：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": { "baseURL": "http://127.0.0.1:11434/v1" },
      "models": {
        "gemma4-12b-32k": {
          "name": "Gemma 4 12B (32k, sans réflexion)",
          "limit": { "context": 32768, "output": 8192 },
          "options": { "reasoningEffort": "none" }
        }
      }
    }
  }
}
```

`reasoningEffort: "none"` は些細な設定ではありません。Ollama は Gemma 4 と
Qwen 3.5 で推論を既定で有効にしており、Modelfile では無効化できません。
OpenCode 経由の実測では、このオプションなしで「猫は敷物の上で眠っている」を
処理すると、推論に 919 トークンと 68 秒かかりましたが、有効にすると 9 トークンでした。

```bash
aipmt --use_opencode --model ollama/gemma4-12b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

実際の 589 行のブログ記事（リンク 140 件、セクション 21 件、
`--news` モードで保護された英語の引用 3 件）に対し、同じコマンドを
3 つのモデルで実行した結果：

| モデル                                   | 所要時間       | 構造                                                  | 差異                                                                                    |
| ---------------------------------------- | ----------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free`（Zen、無料） | 4 分 26 秒  | 原文と同一                                      | なし                                                                                     |
| `ollama/gemma4-12b-32k`（ローカル）          | 10 分 10 秒 | リンク、URL、表、タグ、太字、インラインコードが同一 | 捏造された引用行 1 件（🇺🇸＋言い換え）、重複した帰属表記 1 件               |
| `ollama/qwen3.5-9b-32k`（ローカル）          | 8 分 18 秒  | リンク、URL、表、タグが同一                    | 捏造された引用行 1 件、追加された太字とインラインコードが数件、再処理されたセグメント 1 件 |

ローカル翻訳中は GPU 使用率 98%、消費電力 170 W、VRAM 使用量 10 GB
（モデルと 32 k トークンのキャッシュ。RAM へのオフロードなし）、
Ollama サーバーの RAM 使用量は 7.5 GB でした。90 億～120 億パラメータのモデルは
構造を守る一方で、記事ごとに一度は独自の変更を加えましたが、ゲートウェイモデルには
そのような変更が一切ありませんでした。公開前に確認するか、下書き専用にしてください。

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
| `--source_lang`          | 翻訳元の言語（デフォルト：`fr`）                                                                                  |
| `--target_lang`          | 翻訳先の言語（デフォルト：`en`）                                                                                   |
| `--model`                | 使用する特定のモデル                                                                                  |
| `--eco`                  | 低コストモデルを使用                                                                              |
| `--use_mistral`          | Mistral AI API を使用                                                                                     |
| `--use_claude`           | Claude API を使用                                                                                         |
| `--use_gemini`           | Gemini API を使用                                                                                         |
| `--use_codex`            | ChatGPT サブスクリプションのクォータで Codex CLI を使用                                                    |
| `--use_grok`             | xAI API（Grok）を使用 — `XAI_API_KEY` が必要                                                           |
| `--use_grok_cli`         | Grok サブスクリプションのクォータで Grok CLI を使用                                                        |
| `--use_opencode`         | OpenCode で設定されたプロバイダーに接続（オープンソース）。`--model provider/modèle` が必要 |
| `--force`                | 再翻訳を強制                                                                                       |
| `--keep_filename`        | 元のファイル名を保持                                                                          |
| `--news`                 | ニュースモード：英語の引用を保護し、言語別のフラグを処理                                      |
| `--add_translation_note` | 翻訳注記を追加                                                                                |
| `--note_position`        | 注記の位置：`top`、`bottom`（デフォルト）、または `both`                                                     |
| `--note_format`          | 注記の形式：`legacy`（デフォルト、太字の段落）または `marker`                                            |
| `--include_model`        | 出力ファイルにモデル名を含める                                                            |
| `--reasoning_effort`     | GPT-5.x の推論労力：`none`/`low`/`medium`/`high`/`xhigh`                                         |

> **7つのプロバイダーフラグは相互排他的です。** 以前は2つを組み合わせても
> 暗黙に受け入れられ、最初に検査されたものが選択されていました。そのため、
> サブスクリプションのクォータで要求した翻訳（`--use_codex`、`--use_grok_cli`）が、
> 警告なしに従量課金で実行される可能性がありました。
> `argparse` は現在、この組み合わせを拒否します。

### 翻訳注記：位置と形式

`--add_translation_note` を使用すると、translator は注記を上部、下部、またはその両方に配置でき、単純なテキスト形式（後方互換）または Markdown プラグインで処理可能な `marker` 形式で出力できます。

**位置**（`--note_position`）：

- `bottom`（デフォルト）：従来どおり、ファイル末尾に注記を配置します。
- `top`：注記を **YAML frontmatter の後** に挿入します（Astro Content Collections、gray-matter などに対して安全です）。
- `both`：注記を上部と下部の両方に挿入します（LLM の呼び出しは1回のみで、内容を両方の位置に再利用します）。

**形式**（`--note_format`）：

- `legacy`（デフォルト）：太字の段落 `**...**` — v1.8 とバイト単位で完全に同一の動作です。Hugo、GitHub、GitLab、およびあらゆる Markdown renderer と互換性があります。
- `marker`：非表示の Markdown リンク参照定義（`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`）の後に、太字の blockquote を配置します。GitHub/GitLab ではそのまま読め、Astro 側の remark プラグインでビルド時に処理して、スタイル付きバナーを生成できます（jls42.org のブログを参照）。

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

| プロバイダー | 品質（デフォルト）                      | 低コスト（`--eco`）      |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI   | `gpt-5.6-terra`                       | `gpt-5.6-luna`            |
| Claude   | `claude-sonnet-5`                     | `claude-haiku-4-5`        |
| Mistral  | `mistral-large-latest`                | `mistral-small-latest`    |
| Gemini   | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite`   |
| Codex    | `gpt-5.6-sol`                         | `gpt-5.6-luna`            |
| Grok API | `grok-4.6`                            | `grok-4.3`                |
| Grok CLI | `grok-4.6`                            | `grok-4.5`                |
| OpenCode | `--model provider/modèle` が必須 | 同じ — `--eco` は無効 |

> **長文翻訳の推奨設定**：`--use_gemini`（デフォルト = `gemini-3.7-flash`）は、非ラテン文字を使用する言語（PL、JA、ZH、AR、HI）でも Markdown 構造を忠実に保持します。プレースホルダーの忠実性が重要となる `--news` モードも含まれます。日本語に翻訳したこの README での測定では、`gemini-3.1-pro-preview` と同一の構造（21個のリスト、18個のコードブロック、13個の HTML リンク、13枚の画像、すべての URL を保持）を維持しながら、レイテンシは約6分の1でした。後方互換性のため、デフォルトは引き続き OpenAI です。

## このスクリプトを使用しているプロジェクト

- **[jls42.org](https://jls42.org)** - 多言語対応の個人ブログ（15言語）

## 作者

Julien LE SAUX
メール：contact@jls42.org

## ライセンス

GNU GENERAL PUBLIC LICENSE Version 3。[LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE) を参照してください。

**gpt-5.6-solでフランス語から日本語に翻訳された記事。**
