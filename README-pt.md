# Tradutor de Markdown com IA

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Qualidade do código</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Status do Quality Gate"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Classificação de segurança"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Classificação de confiabilidade"></a>
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

Tradutor de arquivos Markdown que utiliza **OpenAI**, **Mistral AI**, **Claude (Anthropic)**, **Google Gemini** e **Grok (xAI)** — por API, usando a quota de uma assinatura ChatGPT (Codex) ou Grok sem cobrança por uso, ou por meio do **OpenCode**, o agente open source, com o fornecedor de sua escolha: modelo local (Ollama), gratuito, assinatura (GitHub Copilot…) ou chave.

Este script Python traduz arquivos Markdown de um idioma de origem para um idioma de destino, preservando a formatação, os blocos de código e os metadados front matter.

## Principais características

- **Multi-Provider**: 5 APIs (OpenAI, Mistral, Claude, Gemini, Grok) + 2 CLIs por assinatura, sem cobrança por uso — Codex (ChatGPT) e Grok — + OpenCode (open source, MIT) com qualquer fornecedor configurado no OpenCode, incluindo um modelo local
- **Modelos de 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Modo econômico**: opção `--eco` para utilizar modelos mais rápidos e econômicos
- **Arquivo único**: opção `--file` para traduzir um único arquivo
- **Segmentação inteligente**: gerenciamento de textos longos com limites de tokens por modelo
- **Preservação do código**: os blocos de código E o código inline (`` `...` ``) são preservados
- **Nome do arquivo**: opção `--keep_filename` para manter o nome original
- **Modo News**: opção `--news` para proteger citações em inglês e gerenciar bandeiras em artigos de atualidades
- **Configuração .env**: suporte ao arquivo `.env` para chaves de API
- **Nota de tradução**: adição opcional de uma nota no final do documento

## Instalação

### Para utilizar a ferramenta

```bash
pip install ai-powered-markdown-translator
```

O comando `aipmt` fica então disponível em qualquer lugar. Se o diretório de scripts
do Python não estiver no seu `PATH`, `python -m aipmt` faz exatamente a mesma
coisa. Requer Python 3.10 ou mais recente.

Para uma instalação isolada dos demais pacotes:

```bash
pipx install ai-powered-markdown-translator
```

### Para contribuir com o projeto

O repositório clonado continua sendo necessário para o desenvolvimento: é nele que ficam os testes,
as 28 traduções e todo o ferramental de qualidade.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` é um **lock totalmente fixado**, um reflexo exato do
ambiente testado. Os limites publicados em `pyproject.toml` são
deliberadamente mais amplos: eles não impõem nada aos seus outros pacotes.

### Ferramental de qualidade (opcional, mas recomendado)

O projeto utiliza [`pre-commit`](https://pre-commit.com) para impedir commits de código mal formatado, vulnerável ou que contenha algum segredo. Instalação:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hooks ativos: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexidade), detect-secrets (chaves de API), mypy (tipagem progressiva), Opengrep (SAST), pip-audit (CVE de dependências), unittest. Consulte a seção _Quality / pre-commit_ de `CLAUDE.md` para obter detalhes.

## Configuração

As chaves são procuradas em **três locais**, do mais prioritário ao menos prioritário.
Cada um apenas preenche aquilo que o anterior deixou vazio.

|     | Onde                                          | Para quê                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variáveis de ambiente                         | CI, contêineres, exceção pontual      |
| 2   | `.env` do diretório atual (ou de um diretório pai) | uma chave específica de um projeto    |
| 3   | `~/.config/aipmt/.env`                        | **instalado uma vez, válido em qualquer lugar** |

A opção mais simples após um `pip install` é a terceira:

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

Esse arquivo segue `XDG_CONFIG_HOME` quando a variável indica um caminho absoluto
(caso contrário, ela é ignorada, conforme determina a especificação), e `%APPDATA%`
no Windows.

A segunda opção continua sendo útil quando um repositório tem sua própria chave: um `.env` em sua raiz
tem então precedência sobre a configuração do usuário, sem modificá-la. E uma
variável já definida no ambiente tem precedência sobre ambas:

```bash
export OPENAI_API_KEY='une-clé-le-temps-d-une-commande'
```

Se nenhuma chave for encontrada, o comando não exibe nenhum stack trace: ele
lista os três locais com seus caminhos exatos.

`GEMINI_API_KEY` é aceito como alternativa a `GOOGLE_API_KEY` (convenção do AI
Studio). Variáveis opcionais: `XAI_BASE_URL` (endpoint xAI, padrão
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (segundos por chamada Anthropic, padrão
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
`GROK_TRANSLATE_SANDBOX` (consulte a seção Grok CLI), `OPENCODE_BIN` /
`OPENCODE_TIMEOUT` (consulte a seção OpenCode) e `OPENROUTER_BASE_URL` /
`OPENROUTER_TIMEOUT` / `OPENROUTER_PREFLIGHT_TIMEOUT` (consulte a seção
OpenRouter). Para
`regen_translations.sh`: `REGEN_PROVIDER` (padrão `codex`, por assinatura),
`REGEN_MODEL`, `REGEN_ALLOW_PAID_API` (exceção obrigatória para uma API
cobrada) e `REGEN_JOB_TIMEOUT` (limite por job, padrão de 600 s, 1.800 s no Codex).

## Utilização

### Traduzir um único arquivo

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

# Avec OpenRouter (routeur vers ~430 modèles ; --model obligatoire)
aipmt --use_openrouter --model 'z-ai/glm-5.2' --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec OpenCode (open source), vers le fournisseur de votre choix — ici un modèle local Ollama
aipmt --use_opencode --model ollama/qwen2.5:7b --file 'README.md' --target_dir . --target_lang 'nl'
```

### Traduzir usando sua assinatura ChatGPT (`--use_codex`)

Esse provider não consome nenhuma chave de API: ele controla o CLI oficial do Codex em modo
não interativo, portanto a tradução é descontada da quota da assinatura
ChatGPT (Plus, Pro, Business…) já paga. Esse é o único método documentado pela
OpenAI para esse uso — os tokens de `~/.codex/auth.json` não autenticam
as chamadas à Platform API e, além disso, nunca são lidos por este script.

**Pré-requisitos:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

O binário é procurado nesta ordem: a variável `CODEX_BIN`, o `PATH`
e, em seguida, o pacote Python `openai-codex-cli-bin`. Este último propositalmente
não está em `requirements.txt`: ele ocupa cerca de 250 MB, o que seria imposto a todos os
usuários por causa de um provider opcional.

**O que você precisa saber:**

- **Nenhuma chave de API é utilizada.** `OPENAI_API_KEY` e `CODEX_API_KEY` são
  removidas do ambiente do subprocesso, garantindo que uma chave
  presente em `.env` nunca faça a tradução mudar para cobrança por
  uso.
- **Um segmento = uma «mensagem local»** da janela de 5 horas do plano.
  Utilize `--eco` (modelo `gpt-5.6-luna`, 250–2.000 mensagens/5 h no Plus)
  em vez do modelo de qualidade (`gpt-5.6-sol`, 10–100 mensagens/5 h).
- **Mais lento** que uma chamada de API: conte com cerca de 45 s para um README completo, em comparação com
  alguns segundos em uma chamada direta.
- **Recusado em CI** (`CI` ou `GITHUB_ACTIONS` definido): a assinatura
  é autenticada por um arquivo de sessão pessoal, e levá-lo para um runner
  compartilhado equivale a depositar nele uma identidade reutilizável por tudo o que
  for executado ali. Utilize uma chave de API nesse caso.
- Variáveis de ambiente: `CODEX_BIN` (caminho explícito do binário) e
  `CODEX_TIMEOUT` (segundos por segmento, padrão `600`).

### Traduzir usando sua assinatura Grok (`--use_grok_cli`)

O mesmo princípio de `--use_codex`, com o CLI oficial **Grok Build**: a
tradução é descontada da assinatura Grok (SuperGrok / X Premium+), em vez
de ser cobrada por token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Confinamento — leia antes de usar.** Este provider é estruturalmente **mais
fraco** que `--use_codex`, e isso é assumido:

- O Codex é executado em `--sandbox read-only`, uma fronteira imposta pelo sistema.
- O sandbox do Grok **não pode ser aplicado** em muitas máquinas Linux
  recentes: o AppArmor bloqueia user namespaces sem privilégios desde o Ubuntu
  24.04, e a deny-list dos sockets de runtime de contêiner falha se
  `/run/podman` estiver em `0700`. No entanto, um perfil **integrado** que não possa
  ser aplicado inicia **sem confinamento, silenciosamente**.
- Portanto, o script não solicita nenhum perfil por padrão e **nunca faz fallback
  silenciosamente**: ele exibe um aviso. O confinamento depende das
  regras `--deny` do CLI (incluindo a catch-all `*`), a única camada considerada
  _fail-closed_ — uma regra desconhecida faz a inicialização ser recusada, em vez de
  remover a proteção sem avisar.
- Para **exigir** o sandbox do sistema operacional: `GROK_TRANSLATE_SANDBOX=read-only`. A
  inicialização falhará se a máquina não puder respeitá-lo, que é o
  comportamento esperado.

**Quota**: o pool do Grok é **semanal e compartilhado** com Chat, Imagine e
Voice, e nenhum comando permite consultá-lo. Portanto, um processamento em lote pode
consumir seu uso conversacional sem qualquer indicação — por isso há uma
concorrência limitada a 2 e um aviso em `regen_translations.sh`.

Outras variáveis: `GROK_BIN` (caminho do binário), `GROK_TIMEOUT` (padrão de 900 s).

Para regenerar as 28 traduções:

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
### Traduzir com OpenCode, para o fornecedor da sua escolha (`--use_opencode`)

[OpenCode](https://opencode.ai) é um agente de código **open source (MIT)** no
terminal. Não é um fornecedor de modelos, mas um **roteador** para aqueles
que você configurou no próprio OpenCode: uma chave API, uma assinatura,
o gateway OpenCode Zen — que fornece modelos gratuitos **sem conta** — ou
um modelo **local**. Este provider controla `opencode run` em modo não interativo e
limita a chamada a uma única interação, sem qualquer ferramenta.

Duas dessas opções foram medidas de ponta a ponta aqui: o **gateway Zen** e
o **Ollama** local. As outras anunciadas pelo OpenCode (GitHub Copilot, LM Studio,
llama.cpp) devem funcionar por construção, já que o provider se comunica
apenas com o OpenCode — mas não foram testadas, e este README só afirma aquilo
que foi verificado.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles disponibles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur ou un abonnement
```

`--model` é **obrigatório**, no formato `provider/modèle`. O OpenCode não é
um fornecedor, e nenhum padrão é escolhido por você: o fallback próprio
seria um modelo gratuito cujas interações podem ser usadas para treinamento.

```bash
# Gratuit, sans compte ni clé (passerelle Zen ; données utilisables pour l'entraînement)
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en

# Local, hors ligne, sans aucune clé (Ollama déclaré dans ~/.config/opencode/opencode.json)
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de

# Sur un abonnement déjà payé (après `opencode auth login`)
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

**Confinamento — o que o script faz em cada chamada:**

- Uma configuração inline (`OPENCODE_CONFIG_CONTENT`), com prioridade sobre a
  sua, define um agente `aipmt` no qual **todas as ferramentas são recusadas**
  (`permission: { "*": "deny" }`): o modelo não pode ler, escrever nem
  executar comandos — nas medições, ele nem sequer tenta. O compartilhamento da sessão
  fica desativado, `--pure` exclui plugins externos, nunca `--auto`.
- A chamada é executada em um **diretório descartável e vazio**, com as opções
  `OPENCODE_DISABLE_PROJECT_CONFIG` e `OPENCODE_DISABLE_CLAUDE_CODE`: sem
  elas, o OpenCode injeta em cada prompt o `AGENTS.md` do diretório atual
  e o seu `~/.claude/CLAUDE.md` — nas medições, uma instrução para «terminar cada resposta
  com BANANA», colocada em um `AGENTS.md`, era aplicada à tradução. Em
  contrapartida, as regras globais de `~/.config/opencode/AGENTS.md` continuam
  sendo aplicadas: o OpenCode não permite ignorá-las.
- O contrato de saída exige simultaneamente: código de retorno 0, nenhum evento
  `error`, nenhuma chamada de ferramenta, uma última etapa concluída em `stop`, texto não
  vazio e o agente efetivamente carregado — um `--agent` desconhecido não faz
  o OpenCode falhar; ele **volta silenciosamente** para o agente de codificação, com as ferramentas
  ativas. Um `exit 0` também não prova nada aqui.
- **Nenhuma chave do aipmt é transmitida** ao subprocesso (o mesmo filtro
  usado com Codex e Grok), com uma única exceção nominal: `OPENCODE_API_KEY`,
  a chave do próprio OpenCode (Zen, Go). Os fornecedores são configurados no
  OpenCode (`opencode auth login`, `opencode.json`), e não no `.env` do aipmt.

**O que você precisa saber:**

- **Os modelos gratuitos do Zen são modelos «stealth» ou de contribuidores**,
  variáveis, com limites não documentados, e suas interações podem ser usadas para
  treinamento: perfeitos para documentação pública, mas devem ser evitados para
  conteúdo privado. Nas medições, `opencode/mimo-v2.5-free` traduz este README em uma
  única passagem; `opencode/big-pickle` é mais lento, e duas solicitações simultâneas
  ficaram sem resposta.
- **Um modelo local deve oferecer pelo menos 16 k de contexto** — os segmentos chegam
  a 16.000 caracteres — enquanto o Ollama frequentemente configura 4.096 por
  padrão. Com o Ollama: um `Modelfile` com `PARAMETER num_ctx 32768`, seguido de
  `ollama create`. A qualidade depende do modelo: um 7B inverteu uma lista e
  danificou o fechamento de um bloco de código em um arquivo de teste, enquanto um modelo do
  gateway preservou tudo.
- `--eco` não tem efeito (o modelo é o de `--model`);
  `--reasoning_effort` é transmitido sem alterações como `--variant` do OpenCode e só deve
  ser solicitado se o modelo o reconhecer.
- As sessões são registradas pelo OpenCode em seu banco de dados
  (`~/.local/share/opencode/`), como qualquer sessão do OpenCode.
- Variáveis de ambiente: `OPENCODE_BIN` (caminho explícito do binário;
  caso contrário, o `PATH` e depois `~/.opencode/bin/opencode`) e `OPENCODE_TIMEOUT`
  (segundos por segmento, padrão `600`). Se `OPENCODE_CONFIG` for
  exportado, ele não será lido por `aipmt`: será transmitido sem alterações ao OpenCode, que o respeitará.

**Exemplo medido: um modelo local via Ollama** (RTX 3060 12 GB, 62 GB de RAM, Ollama 0.33.3)

```bash
curl -fsSL https://ollama.com/install.sh | sh   # conserve les modèles déjà téléchargés
ollama pull gpt-oss:20b                         # 13 Go, Apache 2.0 — le seul modèle local retenu ici

# Sous 24 Go de VRAM, Ollama plafonne le contexte à 4 096 tokens, et son API OpenAI-compatible
# ne permet pas de le régler par requête : on le fixe dans un Modelfile.
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
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

`reasoningEffort: "none"` não é um detalhe: o Ollama ativa o raciocínio por
padrão nesses modelos, e um Modelfile não consegue desativá-lo. Medido por
meio do OpenCode: sem a opção, «O gato dorme no tapete» consome 919 tokens
de raciocínio e 68 s; com ela, 9 tokens.

```bash
aipmt --use_opencode --model ollama/gpt-oss-20b-32k --news --keep_filename \
  --add_translation_note --file article.mdx --target_dir out/ --target_lang en
```

Resultados em um artigo de blog real com 589 linhas (140 links, 21 seções,
3 citações em inglês protegidas pelo modo `--news`), usando o mesmo comando em três
modelos:

| Modelo                                   | Duração       | Estrutura                                                  | Divergências                                                                                    |
| ---------------------------------------- | ----------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, gratuito) | 4 min 26 s  | idêntica à fonte                                      | nenhuma                                                                                     |
| `ollama/gemma4-12b-32k` (local)          | 10 min 10 s | links, URLs, tabelas, tags, negrito e código inline idênticos | uma linha de citação inventada (🇺🇸 + paráfrase), uma atribuição duplicada               |
| `ollama/qwen3.5-9b-32k` (local)          | 8 min 18 s  | links, URLs, tabelas e tags idênticos                    | uma linha de citação inventada, alguns negritos e códigos inline adicionados, um segmento processado novamente |

Esses dois modelos locais foram posteriormente **descartados**: uma liberdade por artigo
é suficiente para desqualificar um modelo para traduções publicadas. Outros cinco foram
descartados pelos mesmos motivos ou por excederem o tempo limite (`gemma4:26b-a4b`,
`qwen3.6:35b-a3b`, `ministral-3:14b`, `mistral-small3.2`, `hy-mt2:7b`). Apenas
`gpt-oss:20b` foi mantido — e até ele deixa trechos em francês em
um artigo denso; consulte a tabela de modelos recomendados.

Durante a tradução local: GPU a 98% e 170 W, 10 GB de VRAM ocupados
(modelo e cache de 32 k tokens, sem nada descarregado na RAM), 7,5 GB de RAM para o
servidor Ollama. Um modelo com 9 a 12 bilhões de parâmetros respeita a
estrutura, mas toma uma liberdade por artigo, enquanto o modelo do gateway
não tomou nenhuma: revise antes da publicação ou reserve-o para rascunhos.

### Traduzir via OpenRouter (`--use_openrouter`)

OpenRouter é um **roteador** para mais de 400 modelos hospedados por terceiros,
cobrado por uso a partir de um único crédito. Ele oferece acesso, com uma única chave, a modelos
que nenhum dos outros providers disponibiliza, especialmente modelos chineses abertos.

```bash
# --model est OBLIGATOIRE : aucun défaut n'est choisi à votre place
aipmt --use_openrouter --model 'z-ai/glm-5.2' --file README.md \
  --target_dir . --source_lang fr --target_lang en
```

Duas particularidades do roteamento determinaram a implementação, e ambas podem ser
medidas:

- **Um mesmo modelo é fornecido por dezenas de provedores de hospedagem com limites
  diferentes.** Em `z-ai/glm-5.3-flash`, há 23 provedores de hospedagem, incluindo um limitado a
  2.048 tokens de saída: sem precauções, uma tradução longa em cada 23 era
  truncada, ao acaso pelo roteamento e sem qualquer aviso. Um preflight consulta
  `/api/v1/models/{modèle}/endpoints`, descarta os provedores de hospedagem com menos de 8.000 tokens
  de saída ou com status degradado e fixa os demais com
  `allow_fallbacks: false` — sem isso, o roteador volta a usar um provedor de hospedagem
  descartado.
- **O raciocínio é cobrado pela tarifa de saída.** Na mesma solicitação com
  `z-ai/glm-5.2`, resposta «OK»: 107 tokens de conclusão com o padrão do modelo,
  2 com o raciocínio desativado. Por isso, ele fica desativado por padrão nos modelos
  que permitem isso. Aqueles que o exigem — `reasoning.mandatory`, 288 dos 431
  modelos do catálogo — recebem o **menor esforço que declaram
  aceitar**, e não sua configuração padrão: o de `z-ai/glm-5.3-flash` é
  `max`, e ele esgotava os 32.768 tokens de saída antes do fim da
  tradução. Aumentar o limite não mudaria nada, pois o esforço reserva uma
  porcentagem dele. `--reasoning_effort` continua tendo prioridade, e `none` em um modelo
  que exige raciocínio é sinalizado em vez de contornado.

O preflight é **fail-closed** e mostra o que selecionou:

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

Um slug ausente do catálogo, um catálogo inacessível ou a ausência de um provedor de hospedagem
que suporte o limite interrompem o comando antes de qualquer cobrança.

Outros pontos:

- A janela de contexto vem do catálogo, e não de uma constante: a
  segmentação se adapta de fato a ela, inclusive para modelos com 4.095 tokens.
- `--eco` não tem efeito (o modelo é o de `--model`).
- `finish_reason=length` com uma saída vazia não é um truncamento, mas um
  orçamento consumido pelo raciocínio; a mensagem deixa isso claro, pois os dois
  casos exigem ações opostas.
- Variáveis de ambiente: `OPENROUTER_API_KEY` (chave, em
  <https://openrouter.ai/keys>), `OPENROUTER_BASE_URL` (padrão
  `https://openrouter.ai/api/v1`, `https://` obrigatório), `OPENROUTER_TIMEOUT`
  (segundos por chamada, padrão `900`) e `OPENROUTER_PREFLIGHT_TIMEOUT`
  (padrão `30`).

### Modo econômico

Usa modelos mais rápidos e econômicos (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opções

| Opção                   | Descrição                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Um único arquivo Markdown a ser traduzido                                                                            |
| `--source_dir`           | Diretório de origem que contém os arquivos Markdown                                                             |
| `--target_dir`           | Diretório de saída para os arquivos traduzidos                                                               |
| `--source_lang`          | Idioma de origem (padrão: `fr`)                                                                                  |
| `--target_lang`          | Idioma de destino (padrão: `en`)                                                                                   |
| `--model`                | Modelo específico a ser usado                                                                                  |
| `--eco`                  | Usar os modelos econômicos                                                                              |
| `--use_mistral`          | Usar a API Mistral AI                                                                                     |
| `--use_claude`           | Usar a API Claude                                                                                         |
| `--use_gemini`           | Usar a API Gemini                                                                                         |
| `--use_codex`            | Usar o CLI Codex com a cota da assinatura ChatGPT                                                    |
| `--use_grok`             | Usar a API xAI (Grok) — requer `XAI_API_KEY`                                                           |
| `--use_openrouter`       | Usar OpenRouter — requer `OPENROUTER_API_KEY` e `--model fournisseur/modèle`                          |
| `--use_grok_cli`         | Usar o CLI Grok com a cota da assinatura Grok                                                        |
| `--use_opencode`         | Usar OpenCode (open source) com o fornecedor configurado no OpenCode; exige `--model provider/modèle` |
| `--force`                | Forçar uma nova tradução                                                                                       |
| `--keep_filename`        | Manter o nome original do arquivo                                                                          |
| `--news`                 | Modo de notícias: protege citações em inglês e gerencia as bandeiras por idioma                                      |
| `--add_translation_note` | Adicionar uma nota de tradução                                                                                |
| `--note_position`        | Posição da nota: `top`, `bottom` (padrão) ou `both`                                                     |
| `--note_format`          | Formato da nota: `legacy` (padrão, parágrafo em negrito) ou `marker`                                            |
| `--include_model`        | Incluir o nome do modelo no arquivo de saída                                                            |
| `--reasoning_effort`     | Esforço de raciocínio do GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

> **As oito flags de provider são mutuamente exclusivas.** Antes, combinar duas
> era aceito silenciosamente e resolvido usando a primeira testada: uma
> tradução solicitada com a cota da assinatura (`--use_codex`, `--use_grok_cli`)
> podia, assim, gerar cobrança por uso sem qualquer aviso.
> Agora, `argparse` recusa essa combinação.

### Nota de tradução: posições e formatos

Com `--add_translation_note`, o translator pode colocar a nota no início, no fim ou em ambos os locais, e apresentá-la em formato de texto simples (retrocompatível) ou em formato `marker`, que pode ser processado por um plugin Markdown.

**Posição** (`--note_position`):

- `bottom` (padrão): nota no final do arquivo, como historicamente.
- `top`: nota inserida **após o frontmatter YAML** (compatível com Astro Content Collections, gray-matter etc.).
- `both`: nota inserida no início E no fim (uma única chamada ao LLM, com o conteúdo reutilizado nas duas posições).

**Formato** (`--note_format`):

- `legacy` (padrão): parágrafo em negrito `**...**` — comportamento estritamente idêntico ao da v1.8, byte-for-byte. Compatível com Hugo, GitHub, GitLab e qualquer renderer Markdown.
- `marker`: link reference definition Markdown invisível (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), seguida de um blockquote em negrito. Legível nativamente no GitHub/GitLab e utilizável durante o build por um plugin remark no Astro para produzir um banner estilizado (consulte o blog jls42.org).

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

| Provider   | Qualidade (padrão)                         | Econômico (`--eco`)      |
| ---------- | ---------------------------------------- | ------------------------- |
| OpenAI     | `gpt-5.6-terra`                          | `gpt-5.6-luna`            |
| Claude     | `claude-sonnet-5`                        | `claude-haiku-4-5`        |
| Mistral    | `mistral-large-latest`                   | `mistral-small-latest`    |
| Gemini     | `gemini-3.7-flash`                       | `gemini-3.1-flash-lite`   |
| Codex      | `gpt-5.6-sol`                            | `gpt-5.6-luna`            |
| Grok API   | `grok-4.6`                               | `grok-4.3`                |
| Grok CLI   | `grok-4.6`                               | `grok-4.5`                |
| OpenCode   | `--model provider/modèle` obrigatório    | igual — `--eco` sem efeito |
| OpenRouter | `--model fournisseur/modèle` obrigatório | igual — `--eco` sem efeito |
## Quais modelos estão à altura

Um modelo que traduz bem um parágrafo não preserva necessariamente a estrutura
de um documento inteiro. Estas métricas provêm de **traduções realmente
executadas**, com o comando apresentado anteriormente, em três conjuntos de
documentos e catorze idiomas de destino: en, es, de, it, pt, nl, pl, sv, ro, ja,
ko, zh, ar, hi.

Duas colunas, e elas não dizem a mesma coisa. **Gravadas** contabiliza as
traduções concluídas — as proteções do script contra falhas silenciosas
permitem a passagem do ficheiro. **Sem divergências** contabiliza aquelas cuja
estrutura é idêntica à fonte: mesmas secções, mesmos links, mesmos URL, mesmos
blocos e códigos inline, mesmas tabelas, mesmas citações, mesmas flags.

### Artigo de blog denso, modo `--news`

589 linhas, 140 links, 21 secções, 3 citações em inglês protegidas. É o
documento mais exigente dos três: o modo `--news` acrescenta restrições de
flags e citações à estrutura Markdown.

| Modelo                            | Acesso              | Gravadas | Sem divergências | Mediana/idioma |
| --------------------------------- | ------------------- | -------- | ---------------- | -------------- |
| `gemini-3.7-flash`                | API Google          | 14/14    | **14/14**        | 1 min 18 s     |
| `gpt-5.6-sol` (`--use_codex`)     | subscrição ChatGPT | 14/14    | **14/14**        | 11 min 28 s    |
| `z-ai/glm-5.2`                    | OpenRouter          | 14/14    | **14/14**        | 5 min 37 s     |
| `qwen/qwen3.8-flash`              | OpenRouter          | 14/14    | 13/14            | 26 min 23 s    |
| `z-ai/glm-5.3-flash`              | OpenRouter          | 12/14    | 12/14            | 15 min 49 s    |
| `qwen/qwen3.5-27b`                | OpenRouter          | 7/9      | 7/9              | 20 min 33 s    |
| `claude-sonnet-5`                 | API Anthropic       | 14/14    | 11/14            | 6 min 31 s     |
| `opencode/mimo-v2.5-free`         | OpenCode Zen        | 13/14    | 11/14            | 9 min 27 s     |
| `qwen/qwen3.7-flash`              | OpenRouter          | 13/14    | 7/14             | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`          | local               | 10/14    | 7/14             | 12 min 39 s    |
| `mistral-large-latest`            | API Mistral         | 11/14    | 5/14             | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter          | 4/14     | 3/14             | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)     | subscrição Grok    | 1/14     | 1/14             | 23 min 11 s    |
| `moonshotai/kimi-k2.6`            | OpenRouter          | 1/4      | 1/4              | 23 min 00 s    |

Dois lotes foram **interrompidos por falta de crédito**, como mostram os seus
denominadores: `qwen3.5-27b` parou em nove idiomas, `kimi-k2.6` em quatro — este
último após um tempo limite excedido de quarenta minutos e duas recusas, a quase
0,33 $ por idioma.

Uma ressalva metodológica sobre as linhas do OpenRouter: foram medidas com as
configurações **predefinidas do router**, antes de `--use_openrouter` existir.
`z-ai/glm-5.2` foi medido novamente desde então com o provider fornecido, com o
raciocínio desativado, e apresenta exatamente o mesmo resultado de 14/14.
`z-ai/glm-5.3-flash` falhou duas vezes por esgotar o orçamento de saída com a
predefinição do router; agora, o provider solicita a estes modelos o menor
esforço que aceitam, e a contraprova nos idiomas problemáticos é bem-sucedida.

### README deste projeto, Markdown padrão

508 linhas, 219 códigos inline, 40 delimitadores de blocos, 45 linhas de tabela.
Não há modo `--news` aqui: a dificuldade vem da densidade de código.

| Modelo                        | Gravadas | Sem divergências | Mediana/idioma |
| ----------------------------- | -------- | ---------------- | -------------- |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14    | 11/14            | 1 min 22 s     |
| `gemini-3.7-flash`            | 14/14    | 13/14            | 21 s           |
| `gpt-5.6-sol` (`--use_codex`) | 14/14    | 12/14            | 2 min 04 s     |
| `opencode/mimo-v2.5-free`     | 9/14     | 7/14             | 3 min 25 s     |
| `ollama/gpt-oss-20b-32k`      | 9/14     | 1/14             | 3 min 38 s     |

### Quatro README de projetos conhecidos

FastAPI, Ollama, tldr-pages e Vue.js, obtidos sem alterações no GitHub. Estes
documentos são **mais fáceis** do que os dois anteriores, e a tabela mostra-o.

| Modelo                    | Âmbito                     | Gravadas | Sem divergências |
| ------------------------- | -------------------------- | -------- | ---------------- |
| `opencode/mimo-v2.5-free` | 4 projetos × 14 idiomas     | 55/56    | 47/56            |
| `grok-4.6` (subscrição)   | 4 projetos × ar, hi, ja, zh | 16/16    | 14/16            |
| `ollama/gpt-oss-20b-32k`  | 4 projetos × ar, hi, ja, zh | 15/16    | 9/16             |

### O que se pode concluir

- **Três modelos nunca perderam informação** nos dois documentos
  densos: `gemini-3.7-flash`, `gpt-5.6-sol` através da subscrição ChatGPT e
  `z-ai/glm-5.2` através do OpenRouter. As suas únicas divergências no modo padrão são
  um par de `**` não reproduzido num ou dois idiomas, nunca um URL, um bloco
  de código ou uma citação.
- **O fator determinante é a densidade do documento, não o modo `--news`.**
  O Grok por subscrição falha 13 vezes em 14 no artigo de blog e conclui com
  êxito 14 README públicos em 16: a causa das falhas é uma perda de continuidade
  num segmento longo, confirmada por contraprova — o trecho isolado é traduzido
  corretamente.
- **As escritas não latinas não constituem a divisão esperada.** `gpt-oss` deixa
  trechos em francês em árabe, japonês, polaco **e romeno**; Mistral e MiMo só
  perdem códigos inline nas escritas não latinas.
- **Desativar o raciocínio não reduz a qualidade.** `z-ai/glm-5.2` processa
  catorze idiomas sem uma única divergência nas duas condições — raciocínio
  ativo por predefinição do router e depois desativado por `--use_openrouter` — com
  dezoito vezes menos tokens de saída faturados. É a métrica que justifica a
  configuração predefinida do provider.
- **Um modelo lento não é um modelo seguro.** `deepseek-v4-flash-0731` demora 37
  minutos por idioma para 4 traduções em 14, `qwen3.8-flash` demora 26 minutos
  para um resultado quase perfeito e Gemini 1 minuto e 18 para um resultado sem
  falhas.

### O que esta tabela não é

- **Não é uma classificação exaustiva.** Só o OpenRouter disponibiliza mais de
  quatrocentos modelos; cerca de quinze foram medidos aqui. A ausência de um
  modelo nada diz sobre a sua qualidade, apenas que não foi testado.
- **Estas métricas têm uma data**: 4 e 5 de setembro de 2026. Os modelos mudam
  sob o mesmo nome, os fornecedores ajustam quantizações e limites, e novos
  modelos são lançados todas as semanas.
- **As durações não estabelecem nenhuma classificação.** O paralelismo variou
  entre 3 e 6 traduções simultâneas consoante as campanhas, e o débito de um
  fornecedor varia ao longo do dia. Dão uma ordem de grandeza, não uma
  comparação.
- **Um resultado depende tanto do documento como do modelo.** O mesmo modelo
  processa com êxito catorze idiomas num artigo e nove neste README. Os seus
  ficheiros não são os nossos.
- **A abordagem certa continua a ser medir no seu ambiente**: traduza um dos
  seus documentos para os seus idiomas de destino e depois compare a estrutura
  — número de secções, links, URL distintos, blocos de código, códigos inline e
  linhas de tabela. É exatamente isso que o protocolo acima faz, e cabe num
  único ciclo sobre `aipmt`.

## Projetos que utilizam este script

- **[jls42.org](https://jls42.org)** - Blog pessoal multilingue (15 idiomas)

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licença

GNU GENERAL PUBLIC LICENSE Version 3. Consulte [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artigo traduzido do francês para o português com gpt-5.6-sol.**
