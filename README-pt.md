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
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Distintivo Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Tradutor de arquivos Markdown usando **OpenAI**, **Mistral AI**, **Claude (Anthropic)** e **Google Gemini**.

Este script Python traduz arquivos Markdown de um idioma de origem para um idioma de destino, preservando a formatação, os blocos de código e os metadados front matter.

## Principais características

- **Multi-Provider**: Suporte a 4 APIs (OpenAI, Mistral, Claude, Gemini) + a CLI Codex com assinatura ChatGPT
- **Modelos 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Modo econômico**: Opção `--eco` para usar modelos mais rápidos e baratos
- **Arquivo único**: Opção `--file` para traduzir um único arquivo
- **Segmentação inteligente**: Gerenciamento de textos longos com limites de tokens por modelo
- **Preservação do código**: Os blocos de código E o código inline (`` `...` ``) são preservados
- **Nome do arquivo**: Opção `--keep_filename` para manter o nome original
- **Modo News**: Opção `--news` para proteger citações em inglês e gerenciar bandeiras em artigos de notícias
- **Configuração .env**: Suporte ao arquivo `.env` para chaves de API
- **Nota de tradução**: Adição opcional de uma nota ao final do documento

## Instalação

### Para usar a ferramenta

```bash
pip install ai-powered-markdown-translator
```

O comando `aipmt` fica então disponível em qualquer lugar. Se o diretório dos scripts
do Python não estiver no seu `PATH`, `python -m aipmt` faz exatamente a mesma
coisa. Python 3.10 ou mais recente.

Para uma instalação isolada do restante dos seus pacotes:

```bash
pipx install ai-powered-markdown-translator
```

### Para contribuir com o projeto

O repositório clonado continua sendo necessário para desenvolver: é nele que ficam os testes,
as 28 traduções e todas as ferramentas de qualidade.

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

`requirements.txt` é um **lock totalmente fixado**, um reflexo exato do
ambiente testado. Os limites publicados em `pyproject.toml` são
intencionalmente mais amplos: eles não impõem nada aos seus outros pacotes.

### Ferramentas de qualidade (opcional, mas recomendado)

O projeto usa [`pre-commit`](https://pre-commit.com) para impedir o commit de código mal formatado, vulnerável ou contendo um segredo. Instalação:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hooks ativos: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexidade), detect-secrets (chaves de API), mypy (tipagem progressiva), Opengrep (SAST), pip-audit (CVE deps), unittest. Consulte a seção _Quality / pre-commit_ de `CLAUDE.md` para obter detalhes.

## Configuração

Crie um arquivo `.env` **no diretório a partir do qual você executa o
comando** (ele é procurado nesse local e, depois, nos diretórios pais), ou
defina as variáveis de ambiente:

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

`GEMINI_API_KEY` é aceito como alternativa a `GOOGLE_API_KEY` (convenção AI
Studio). Variáveis opcionais: `XAI_BASE_URL` (endpoint xAI, padrão
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (segundos por chamada Anthropic, padrão
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
e `GROK_TRANSLATE_SANDBOX` (consulte a seção Grok CLI). No lado do
`regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL` e
`REGEN_JOB_TIMEOUT` (limite por job, padrão 600 s).

## Uso

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
```

### Traduzir usando sua assinatura ChatGPT (`--use_codex`)

Este provider não consome nenhuma chave de API: ele controla a CLI Codex oficial em modo
não interativo; portanto, a tradução é descontada da cota da assinatura
ChatGPT (Plus, Pro, Business…) já paga. Este é o único caminho documentado pela
OpenAI para esse uso — os tokens de `~/.codex/auth.json` não autenticam
chamadas à API Platform e, além disso, nunca são lidos por este script.

**Pré-requisitos:**

```bash
# Le binaire `codex`, au choix :
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo)
npm install -g @openai/codex       # ou l'installation npm globale

codex login                        # connexion avec le compte ChatGPT
```

O binário é procurado nesta ordem: a variável `CODEX_BIN`, o `PATH`,
e depois o pacote Python `openai-codex-cli-bin`. Este último não está
intencionalmente em `requirements.txt`: ele ocupa ~250 MB, o que seria imposto a todos os
usuários por um provider opcional.

**É importante saber:**

- **Nenhuma chave de API é usada.** `OPENAI_API_KEY` e `CODEX_API_KEY` são
  removidas do ambiente do subprocesso, garantindo que uma chave presente em
  `.env` nunca faça a tradução mudar para cobrança por uso.
- **Um segmento = uma «mensagem local»** da janela de 5 horas do plano.
  Use `--eco` (modelo `gpt-5.6-luna`, 250–2 000 mensagens/5 h no Plus)
  em vez do modelo de qualidade (`gpt-5.6-sol`, 10–100 mensagens/5 h).
- **Mais lento** que uma chamada de API: conte ~45 s para um README completo, contra
  alguns segundos diretamente.
- **Recusado em CI** (`CI` ou `GITHUB_ACTIONS` definido): a autenticação por
  assinatura não foi projetada para um runner compartilhado, e a OpenAI desaconselha esse
  fluxo de trabalho em repositórios públicos. Use uma chave de API nesse caminho.
- Variáveis de ambiente: `CODEX_BIN` (caminho explícito do binário) e
  `CODEX_TIMEOUT` (segundos por segmento, padrão `600`).

### Traduzir usando sua assinatura Grok (`--use_grok_cli`)

O mesmo princípio de `--use_codex`, com a CLI oficial **Grok Build**: a
tradução é descontada da assinatura Grok (SuperGrok / X Premium+) em vez de
ser cobrada por token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Isolamento — leia antes de usar.** Este provider é estruturalmente **mais
fraco** que `--use_codex`, e isso é assumido:

- O Codex é executado em `--sandbox read-only`, uma fronteira imposta pelo sistema.
- O sandbox do Grok **não pode ser aplicado** em muitos sistemas Linux
  recentes: o AppArmor bloqueia user namespaces não privilegiados desde o Ubuntu
  24.04, e a deny-list dos sockets de runtime de contêiner falha quando
  `/run/podman` está em `0700`. Porém, um perfil **integrado** que não pode
  ser aplicado inicia **sem isolamento, silenciosamente**.
- Por isso, o script não solicita nenhum perfil por padrão e **nunca recua silenciosamente**:
  ele exibe um aviso. O isolamento depende das regras `--deny` da CLI (incluindo o catch-all
  `*`), a única camada medida _fail-closed_ — uma regra desconhecida faz a inicialização
  ser recusada em vez de remover a proteção sem informar.
- Para **exigir** o sandbox do sistema operacional: `GROK_TRANSLATE_SANDBOX=read-only`. A
  inicialização falhará se a máquina não puder respeitá-lo, que é o
  comportamento desejado.

**Cota**: o pool do Grok é **semanal e compartilhado** com Chat, Imagine e
Voice, e nenhum comando permite consultá-lo. Portanto, um processamento em lote pode
consumir seu uso conversacional sem que nada indique isso — daí a
concorrência limitada a 2 e um aviso em `regen_translations.sh`.

Outras variáveis: `GROK_BIN` (caminho do binário), `GROK_TIMEOUT` (padrão 900 s).

Para regenerar as 28 traduções:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### Modo econômico

Usa modelos mais rápidos e baratos (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
aipmt --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opções

| Opção                   | Descrição                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Arquivo Markdown único a ser traduzido                                       |
| `--source_dir`           | Diretório de origem contendo os arquivos Markdown                        |
| `--target_dir`           | Diretório de saída dos arquivos traduzidos                          |
| `--source_lang`          | Idioma de origem (padrão: `fr`)                                             |
| `--target_lang`          | Idioma de destino (padrão: `en`)                                              |
| `--model`                | Modelo específico a ser usado                                             |
| `--eco`                  | Usar modelos econômicos                                         |
| `--use_mistral`          | Usar a API Mistral AI                                                |
| `--use_claude`                  | Usar a API Claude                                                    |
| `--use_gemini`                  | Usar a API Gemini                                                    |
| `--use_codex`             | Usar a CLI Codex com a cota da assinatura ChatGPT               |
| `--use_grok`             | Usar a API xAI (Grok) — requer `XAI_API_KEY`                      |
| `--use_grok_cli`         | Usar a CLI Grok com a cota da assinatura Grok                   |
| `--force`                | Forçar a retradução                                                  |
| `--keep_filename`        | Manter o nome original do arquivo                                     |
| `--news`                 | Modo notícias: protege citações EN e gerencia bandeiras por idioma |
| `--add_translation_note` | Adicionar uma nota de tradução                                           |
| `--note_position`        | Posição da nota: `top`, `bottom` (padrão) ou `both`                |
| `--note_format`          | Formato da nota: `legacy` (padrão, parágrafo em negrito) ou `marker`       |
| `--include_model`        | Incluir o nome do modelo no arquivo de saída                       |
| `--reasoning_effort`     | Esforço de raciocínio GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`    |

> **As seis flags de provider são mutuamente exclusivas.** Combinar duas
> anteriormente era aceito silenciosamente e resolvia para a primeira testada: uma
> tradução solicitada usando a cota da assinatura (`--use_codex`, `--use_grok_cli`)
> poderia assim ser cobrada por uso sem qualquer aviso.
> `argparse` agora recusa a combinação.

### Nota de tradução: posições e formatos

Com `--add_translation_note`, o translator pode colocar a nota no topo, na parte inferior ou em ambos os locais, e renderizá-la em formato de texto simples (retrocompatível) ou no formato `marker` consumível por um plugin Markdown.

**Posição** (`--note_position`):

- `bottom` (padrão): nota no final do arquivo, como historicamente.
- `top`: nota inserida **após o frontmatter YAML** (segurança para Astro Content Collections, gray-matter etc.).
- `both`: nota inserida no topo E na parte inferior (uma única chamada LLM, conteúdo reutilizado para os dois locais).

**Formato** (`--note_format`):

- `legacy` (padrão): parágrafo em negrito `**...**` — comportamento estritamente idêntico ao da v1.8, byte por byte. Compatível com Hugo, GitHub, GitLab e qualquer renderer Markdown.
- `marker`: definição invisível de referência de link Markdown (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) seguida de um blockquote em negrito. Legível nativamente no GitHub/GitLab e utilizável durante o build por um plugin remark no Astro para produzir um banner estilizado (cf. blog jls42.org).

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

| Provider | Qualidade (padrão)       | Econômico (`--eco`)    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **Recomendação para traduções long-form**: `--use_gemini` (padrão = `gemini-3.7-flash`) preserva fielmente a estrutura Markdown em scripts não latinos (PL, JA, ZH, AR, HI), inclusive no modo `--news`, em que a fidelidade dos placeholders é importante. Medido neste README traduzido para japonês: estrutura idêntica à de `gemini-3.1-pro-preview` (21 listas, 18 blocos de código, 13 links HTML, 13 imagens, todas as URLs preservadas) com cerca de 6 vezes menos latência. OpenAI continua sendo o padrão por compatibilidade retroativa.

## Projetos que usam este script

- **[jls42.org](https://jls42.org)** - Blog pessoal multilíngue (15 idiomas)

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licença

GNU GENERAL PUBLIC LICENSE Versão 3. Consulte [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

**Artigo traduzido do francês para o português com gpt-5.6-luna.**
