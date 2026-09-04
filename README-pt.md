# Tradutor de Markdown com IA

🌍 [Francês](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Inglês](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Espanhol](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Chinês](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Alemão](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japonês](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Coreano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Árabe](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Neerlandês](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polaco](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Romeno](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Sueco](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Qualidade do código</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Estado do Quality Gate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Classificação de segurança"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Classificação de fiabilidade"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Classificação de manutenibilidade"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Cobertura"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilidades"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Linhas duplicadas (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Dívida técnica"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Linhas de código"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Badge do Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Tradutor de ficheiros Markdown que utiliza **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** e **Grok (xAI)** — através de API, usando a quota de uma subscrição ChatGPT (Codex) ou Grok sem faturação por utilização, ou através do **OpenCode**, o agente open source, com o fornecedor da sua escolha: modelo local (Ollama), gratuito, subscrição (GitHub Copilot…) ou chave.

Este script Python traduz ficheiros Markdown de um idioma de origem para um idioma de destino, preservando simultaneamente a formatação, os blocos de código e os metadados de front matter.

## Principais características

- **Multi-Provider**: 5 APIs (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLIs por subscrição, sem faturação por utilização — Codex (ChatGPT) e Grok — + OpenCode (open source, MIT) para qualquer fornecedor configurado no OpenCode, incluindo um modelo local
- **Modelos de 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Modo económico**: Opção `--eco` para utilizar modelos mais rápidos e económicos
- **Ficheiro único**: Opção `--file` para traduzir um único ficheiro
- **Segmentação inteligente**: Gestão de textos longos com limites de tokens por modelo
- **Preservação do código**: Os blocos de código E o código inline (`` `...` ``) são preservados
- **Nome do ficheiro**: Opção `--keep_filename` para manter o nome original
- **Modo News**: Opção `--news` para proteger citações em inglês e gerir bandeiras em artigos noticiosos
- **Configuração .env**: Suporte do ficheiro `.env` para as chaves de API
- **Nota de tradução**: Adição opcional de uma nota no final do documento

## Instalação

### Para utilizar a ferramenta

```bash
pip install ai-powered-markdown-translator
```

O comando `aipmt` fica então disponível em todo o lado. Se o diretório dos scripts
do Python não estiver no seu `PATH`, `python -m aipmt` faz exatamente a mesma
coisa. Python 3.10 ou mais recente.

Para uma instalação isolada dos restantes pacotes:

```bash
pipx install ai-powered-markdown-translator
```

### Para contribuir para o projeto

O repositório clonado continua a ser necessário para desenvolver: é lá que se encontram os testes,
as 28 traduções e todas as ferramentas de qualidade.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` é um **lock totalmente fixado**, um reflexo exato do
ambiente testado. Os limites publicados em `pyproject.toml` são
deliberadamente mais amplos: não impõem nada aos seus outros pacotes.

### Ferramentas de qualidade (opcionais, mas recomendadas)

O projeto utiliza [`pre-commit`](https://pre-commit.com) para impedir commits de código mal formatado, vulnerável ou que contenha um segredo. Instalação:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hooks ativos: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexidade), detect-secrets (chaves de API), mypy (tipagem progressiva), Opengrep (SAST), pip-audit (CVE das dependências), unittest. Consulte a secção _Quality / pre-commit_ de `CLAUDE.md` para obter detalhes.

## Configuração

As chaves são procuradas em **três locais**, do mais prioritário para o menos prioritário.
Cada um apenas preenche o que o anterior deixou vazio.

|     | Onde                                          | Para quê                                  |
| --- | --------------------------------------------- | ----------------------------------------- |
| 1   | Variáveis de ambiente                         | CI, contentores, exceção pontual           |
| 2   | `.env` do diretório atual (ou de um diretório ascendente) | uma chave específica de um projeto        |
| 3   | `~/.config/aipmt/.env`                               | **instalado uma vez, funciona em todo o lado** |

A opção mais simples após um `pip install` é a terceira:

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

Este ficheiro segue `XDG_CONFIG_HOME` quando a variável indica um caminho absoluto
(caso contrário, é ignorada, conforme prescrito pela especificação), e `%APPDATA%`
no Windows.

A segunda continua a ser útil quando um repositório tem a sua própria chave: um `.env` na sua raiz
prevalece então sobre a configuração do utilizador, sem a modificar. E uma
variável já definida no ambiente prevalece sobre ambas:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Se nenhuma chave for encontrada, o comando não apresenta nenhum stack trace: ele
enumera os três locais com o respetivo caminho exato.

`GEMINI_API_KEY` é aceite como alternativa a `GOOGLE_API_KEY` (convenção do AI
Studio). Variáveis opcionais: `XAI_BASE_URL` (endpoint da xAI, predefinição
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (segundos por chamada Anthropic, predefinição
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (consulte a secção Grok CLI) e `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (consulte a secção OpenCode). Do lado de
`regen_translations.sh`: `REGEN_PROVIDER` (predefinição `codex`, por subscrição),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (exceção obrigatória para uma API
faturada) e `REGEN_JOB_TIMEOUT` (limite por job, predefinição de 600 s, 1 800 s no Codex).

## Utilização

### Traduzir um único ficheiro

```bash
aipmt --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traduzir um diretório

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

### Traduzir com a sua subscrição ChatGPT (`--use_codex`)

Este provider não consome nenhuma chave de API: controla o CLI oficial do Codex em modo
não interativo, pelo que a tradução é deduzida da quota da subscrição
ChatGPT (Plus, Pro, Business…) já paga. É a única via documentada pela
OpenAI para esta utilização — os tokens de `~/.codex/auth.json` não autenticam
as chamadas à API Platform e, além disso, nunca são lidos por este script.

**Pré-requisitos:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

O binário é procurado por esta ordem: a variável `CODEX_BIN`, o `PATH`,
e depois o pacote Python `openai-codex-cli-bin`. Este último não está deliberadamente
incluído em `requirements.txt`: ocupa ~250 MB, que seriam impostos a todos os
utilizadores por causa de um provider opcional.

**A ter em conta:**

- **Não é utilizada nenhuma chave de API.** `OPENAI_API_KEY` e `CODEX_API_KEY` são
  removidas do ambiente do subprocesso, o que garante que uma chave
  presente em `.env` nunca fará com que a tradução passe para faturação por
  utilização.
- **Um segmento = uma «mensagem local»** da janela de 5 horas do plano.
  Utilize `--eco` (modelo `gpt-5.6-luna`, 250-2 000 mensagens/5 h no Plus)
  em vez do modelo de qualidade (`gpt-5.6-sol`, 10-100 mensagens/5 h).
- **Mais lento** do que uma chamada de API: conte com ~45 s para um README completo, em comparação com
  alguns segundos de forma direta.
- **Recusado em CI** (`CI` ou `GITHUB_ACTIONS` definido): a autenticação por
  subscrição não foi concebida para um runner partilhado, e a OpenAI desaconselha este
  workflow em repositórios públicos. Utilize uma chave de API neste caso.
- Variáveis de ambiente: `CODEX_BIN` (caminho explícito do binário) e
  `CODEX_TIMEOUT` (segundos por segmento, predefinição `600`).

### Traduzir com a sua subscrição Grok (`--use_grok_cli`)

O mesmo princípio de `--use_codex`, com o CLI oficial **Grok Build**: a
tradução é deduzida da subscrição Grok (SuperGrok / X Premium+), em vez
de ser faturada por token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Confinamento — leia antes de utilizar.** Este provider é estruturalmente **mais
fraco** do que `--use_codex`, e isso é assumido:

- O Codex é executado em `--sandbox read-only`, uma fronteira imposta pelo sistema.
- O sandbox do Grok **não pode ser aplicado** em muitos computadores Linux
  recentes: o AppArmor bloqueia user namespaces sem privilégios desde o Ubuntu
  24.04, e a deny-list dos sockets de runtime do contentor falha se
  `/run/podman` estiver em `0700`. No entanto, um perfil **integrado** que não consiga
  ser aplicado arranca **sem confinamento e em silêncio**.
- Por isso, o script não solicita nenhum perfil por predefinição e **nunca recorre
  silenciosamente a uma alternativa**: apresenta um aviso. O confinamento assenta nas
  regras `--deny` do CLI (incluindo o catch-all `*`), a única camada medida
  como _fail-closed_ — uma regra desconhecida faz com que o arranque seja recusado, em vez de
  remover a proteção sem o indicar.
- Para **exigir** o sandbox do SO: `GROK_TRANSLATE_SANDBOX=read-only`. O
  arranque falhará se a máquina não conseguir respeitá-lo, que é o
  comportamento pretendido.

**Quota**: o pool do Grok é **semanal e partilhado** com Chat, Imagine e
Voice, e nenhum comando permite consultá-lo. Assim, um processamento em lote pode
reduzir a sua utilização para conversação sem qualquer aviso — daí uma
concorrência limitada a 2 e um aviso em `regen_translations.sh`.

Outras variáveis: `GROK_BIN` (caminho do binário), `GROK_TIMEOUT` (predefinição de 900 s).

Para regenerar as 28 traduções:

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

### Traduzir com o OpenCode, utilizando o fornecedor da sua escolha (`--use_opencode`)

O [OpenCode](https://opencode.ai) é um agente de código **open source (MIT)** para
terminal. Não é um fornecedor de modelos, mas sim um **router** para aqueles
que configurou no próprio OpenCode: uma chave de API, uma subscrição
(GitHub Copilot, ChatGPT, SuperGrok), o gateway OpenCode Zen — que disponibiliza
modelos gratuitos **sem conta** — ou um modelo **local** (Ollama, LM Studio,
llama.cpp). Este provider controla `opencode run` em modo não interativo e confina
a chamada a uma única interação, sem qualquer ferramenta.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` é **obrigatório**, no formato `provider/modèle`. O OpenCode não é
um fornecedor e nenhuma predefinição é escolhida por si: o seu próprio fallback
seria um modelo gratuito cujas interações podem ser utilizadas para treino.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Confinamento — o que o script faz em cada chamada:**

- Uma configuração inline (`OPENCODE_CONFIG_CONTENT`), que prevalece sobre a
  sua, define um agente `aipmt` no qual **todas as ferramentas são recusadas**
  (`permission: { "*": "deny" }`): o modelo não pode ler, escrever nem
  executar comandos — nas medições, nem sequer tenta fazê-lo. A partilha de sessões
  está desativada, `--pure` exclui os plugins externos, nunca `--auto`.
- A chamada é executada num **diretório temporário e vazio**, com os interruptores
  `OPENCODE_DISABLE_PROJECT_CONFIG` e `OPENCODE_DISABLE_CLAUDE_CODE`: sem
  eles, o OpenCode injeta em cada prompt o `AGENTS.md` do diretório atual
  e o seu `~/.claude/CLAUDE.md` — nas medições, uma instrução para «terminar cada resposta
  com BANANA» colocada num `AGENTS.md` era aplicada à tradução. No entanto, as
  regras globais de `~/.config/opencode/AGENTS.md` continuam a ser
  aplicadas: o OpenCode não permite excluí-las.
- O contrato de saída exige tudo em simultâneo: código de retorno 0, nenhum evento
  `error`, nenhuma chamada de ferramenta, um último passo concluído em `stop`, texto não
  vazio e o agente efetivamente carregado — um `--agent` desconhecido não faz
  o OpenCode falhar; este **recorre silenciosamente** ao agente de programação, com as ferramentas
  ativas. Um `exit 0` também não prova nada aqui.
- **Nenhuma chave do aipmt é transmitida** ao subprocesso (a mesma filtragem
  utilizada com o Codex e o Grok), exceto uma exceção nominal: `OPENCODE_API_KEY`,
  a chave do próprio OpenCode (Zen, Go). Os fornecedores são configurados no
  OpenCode (`opencode auth login`, `opencode.json`), e não no `.env` do aipmt.

**A ter em conta:**

- **Os modelos gratuitos do Zen são modelos «stealth» ou de contribuidores**,
  variáveis, com limites não documentados, e as suas interações podem ser utilizadas para
  treino: perfeitos para documentação pública, mas devem ser evitados para
  conteúdo privado. Nas medições: `opencode/mimo-v2.5-free` traduz este README numa
  só passagem; `opencode/big-pickle` é mais lento e duas solicitações simultâneas ficaram
  sem resposta.
- **Um modelo local deve oferecer pelo menos 16 k de contexto** — os segmentos têm
  até 16 000 caracteres — enquanto o Ollama costuma configurar 4 096 por
  predefinição. Com o Ollama: um `Modelfile` com `PARAMETER num_ctx 32768`, seguido de
  `ollama create`. A qualidade depende do modelo: um 7B inverteu uma lista e
  danificou o delimitador de um bloco de código num ficheiro de teste, enquanto um modelo do
  gateway preservou tudo.
- `--eco` não tem efeito (o modelo é o de `--model`);
  `--reasoning_effort` é transmitido tal como está como `--variant` do OpenCode, devendo ser
  solicitado apenas se o modelo o reconhecer.
- As sessões são registadas pelo OpenCode na sua base de dados
  (`~/.local/share/opencode/`), como qualquer sessão do OpenCode.
- Variáveis de ambiente: `OPENCODE_BIN` (caminho explícito do binário,
  caso contrário o `PATH` e depois `~/.opencode/bin/opencode`) e `OPENCODE_TIMEOUT`
  (segundos por segmento, predefinição `600`). `OPENCODE_CONFIG` é respeitado se o
  exportar.

**Exemplo medido: um modelo local através do Ollama** (RTX 3060 12 GB, 62 GB de RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # Ollama ≥ 0.30 pour gemma4 ; conserve les modèles déjà téléchargés
ollama pull gemma4:12b                          # 7,6 Go, Apache 2.0, 140+ langues
ollama pull qwen3.5:9b                          # 6,6 Go, Apache 2.0, 201 langues

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gemma4:12b\nPARAMETER num_ctx 32768\n' > gemma4-12b-32k.Modelfile
ollama create gemma4-12b-32k -f gemma4-12b-32k.Modelfile
```

Em seguida, o fornecedor em `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` não é um pormenor: o Ollama ativa a reflexão por
predefinição no Gemma 4 e no Qwen 3.5, e um Modelfile não consegue desativá-la. Medido
através do OpenCode: sem a opção, «O gato dorme no tapete» consome 919 tokens
de raciocínio e 68 s; com ela, 9 tokens.

```bash
aipmt --use_opencode --model ollama/gemma4-12b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Resultados num artigo de blogue real com 589 linhas (140 links, 21 secções,
3 citações em inglês protegidas pelo modo `--news`), o mesmo comando, três
modelos:

| Modelo                                   | Duração       | Estrutura                                                  | Diferenças                                                                                    |
| ---------------------------------------- | ------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, gratuito)          | 4 min 26 s    | idêntica à origem                                          | nenhuma                                                                                       |
| `ollama/gemma4-12b-32k` (local)                  | 10 min 10 s   | links, URLs, tabelas, tags, negrito e código inline idênticos | uma linha de citação inventada (🇺🇸 + paráfrase), uma atribuição duplicada                    |
| `ollama/qwen3.5-9b-32k` (local)                  | 8 min 18 s    | links, URLs, tabelas e tags idênticos                      | uma linha de citação inventada, alguns negritos e códigos inline adicionados, um segmento reprocessado |

Durante a tradução local: GPU a 98% e 170 W, 10 GB de VRAM ocupados
(modelo e cache de 32 k tokens, nada descarregado para a RAM), 7,5 GB de RAM para o
servidor Ollama. Um modelo com 9 a 12 mil milhões de parâmetros respeita a
estrutura, mas toma uma liberdade por artigo, enquanto o modelo do gateway
não tomou nenhuma: deve ser revisto antes da publicação ou reservado para rascunhos.

### Modo económico

Utiliza modelos mais rápidos e económicos (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```
### Opções

| Opção                   | Descrição                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Arquivo Markdown único a traduzir                                                                            |
| `--source_dir`           | Diretório de origem contendo os arquivos Markdown                                                             |
| `--target_dir`           | Diretório de saída para os arquivos traduzidos                                                               |
| `--source_lang`          | Idioma de origem (padrão: `fr`)                                                                                  |
| `--target_lang`          | Idioma de destino (padrão: `en`)                                                                                   |
| `--model`                | Modelo específico a utilizar                                                                                  |
| `--eco`                  | Utilizar os modelos econômicos                                                                              |
| `--use_mistral`          | Utilizar a API Mistral AI                                                                                     |
| `--use_claude`           | Utilizar a API Claude                                                                                         |
| `--use_gemini`           | Utilizar a API Gemini                                                                                         |
| `--use_codex`            | Utilizar o CLI Codex com a cota da assinatura ChatGPT                                                    |
| `--use_grok`             | Utilizar a API xAI (Grok) — requer `XAI_API_KEY`                                                           |
| `--use_grok_cli`         | Utilizar o CLI Grok com a cota da assinatura Grok                                                        |
| `--use_opencode`         | Utilizar o OpenCode (open source) com o fornecedor configurado no OpenCode; requer `--model provider/modèle` |
| `--force`                | Forçar uma nova tradução                                                                                       |
| `--keep_filename`        | Manter o nome original do arquivo                                                                          |
| `--news`                 | Modo notícias: protege as citações em inglês e gerencia os sinalizadores por idioma                                      |
| `--add_translation_note` | Adicionar uma nota de tradução                                                                                |
| `--note_position`        | Posição da nota: `top`, `bottom` (padrão) ou `both`                                                     |
| `--note_format`          | Formato da nota: `legacy` (padrão, parágrafo em negrito) ou `marker`                                            |
| `--include_model`        | Incluir o nome do modelo no arquivo de saída                                                            |
| `--reasoning_effort`     | Esforço de raciocínio do GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

> **Os sete sinalizadores de fornecedor são mutuamente exclusivos.** Anteriormente, combinar dois
> era aceito silenciosamente e resultava no primeiro testado: uma
> tradução solicitada usando a cota da assinatura (`--use_codex`, `--use_grok_cli`)
> podia, assim, acabar sendo cobrada por uso sem qualquer aviso.
> `argparse` agora recusa essa combinação.

### Nota de tradução: posições e formatos

Com `--add_translation_note`, o tradutor pode colocar a nota no início, no fim ou em ambos os lugares e renderizá-la em formato de texto simples (retrocompatível) ou no formato `marker`, utilizável por um plugin Markdown.

**Posição** (`--note_position`):

- `bottom` (padrão): nota no fim do arquivo, como tradicionalmente.
- `top`: nota inserida **após o front matter YAML** (compatibilidade com Astro Content Collections, gray-matter etc.).
- `both`: nota inserida no início E no fim (uma única chamada ao LLM, com o conteúdo reutilizado nos dois locais).

**Formato** (`--note_format`):

- `legacy` (padrão): parágrafo em negrito `**...**` — comportamento rigorosamente idêntico ao da v1.8, byte por byte. Compatível com Hugo, GitHub, GitLab e qualquer renderizador Markdown.
- `marker`: definição de referência de link Markdown invisível (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), seguida de um blockquote em negrito. Legível nativamente no GitHub/GitLab e utilizável durante o build por um plugin remark no Astro para produzir um banner estilizado (consulte o blog jls42.org).

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

### Modelos padrão (2026)

| Fornecedor | Qualidade (padrão)                      | Econômico (`--eco`)      |
| -------- | ------------------------------------- | ------------------------- |
| OpenAI   | `gpt-5.6-terra`                       | `gpt-5.6-luna`            |
| Claude   | `claude-sonnet-5`                     | `claude-haiku-4-5`        |
| Mistral  | `mistral-large-latest`                | `mistral-small-latest`    |
| Gemini   | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite`   |
| Codex    | `gpt-5.6-sol`                         | `gpt-5.6-luna`            |
| Grok API | `grok-4.6`                            | `grok-4.3`                |
| Grok CLI | `grok-4.6`                            | `grok-4.5`                |
| OpenCode | `--model provider/modèle` obrigatório | igual — `--eco` sem efeito |

> **Recomendação para traduções long-form**: `--use_gemini` (padrão = `gemini-3.7-flash`) preserva fielmente a estrutura Markdown em sistemas de escrita não latinos (PL, JA, ZH, AR, HI), inclusive no modo `--news`, no qual a fidelidade dos placeholders é importante. Medido neste README traduzido para japonês: estrutura idêntica à de `gemini-3.1-pro-preview` (21 listas, 18 blocos de código, 13 links HTML, 13 imagens, todas as URLs preservadas), com latência cerca de 6 vezes menor. A OpenAI continua sendo o padrão para garantir a retrocompatibilidade.

## Projetos que utilizam este script

- **[jls42.org](https://jls42.org)** - Blog pessoal multilíngue (15 idiomas)

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licença

GNU GENERAL PUBLIC LICENSE Versão 3. Consulte [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artigo traduzido do francês para o português com o gpt-5.6-sol.**
