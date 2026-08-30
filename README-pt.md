# Tradutor de Markdown com IA

🌍 [Francês](README.md) | [Inglês](README-en.md) | [Espanhol](README-es.md) | [Chinês](README-zh.md) | [Alemão](README-de.md) | [Japonês](README-ja.md) | [Coreano](README-ko.md) | [Árabe](README-ar.md) | [Hindi](README-hi.md) | [Italiano](README-it.md) | [Neerlandês](README-nl.md) | [Polonês](README-pl.md) | [Português](README-pt.md) | [Romeno](README-ro.md) | [Sueco](README-sv.md)

<h4 align="center">📊 Qualidade do código</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Estado do Quality Gate"></a>
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

Tradutor de ficheiros Markdown que utiliza **OpenAI**, **Mistral AI**, **Claude (Anthropic)** e **Google Gemini**.

Este script Python traduz ficheiros Markdown de um idioma de origem para um idioma de destino, preservando simultaneamente a formatação, os blocos de código e os metadados front matter.

## Principais Características

- **Multi-Provider**: Suporte para 4 APIs (OpenAI, Mistral, Claude, Gemini) + o CLI Codex com subscrição ChatGPT
- **Modelos 2026**: GPT-5.6 Terra, Claude Sonnet 5, Gemini 3.7 Flash
- **Modo Económico**: Opção `--eco` para utilizar modelos mais rápidos e económicos
- **Ficheiro Único**: Opção `--file` para traduzir um único ficheiro
- **Segmentação Inteligente**: Gestão de textos longos com limites de tokens por modelo
- **Preservação do Código**: Os blocos de código E o código inline (`` `...` ``) são preservados
- **Nome do Ficheiro**: Opção `--keep_filename` para manter o nome original
- **Modo Notícias**: Opção `--news` para proteger as citações em inglês e gerir as bandeiras nos artigos de atualidade
- **Configuração .env**: Suporte para o ficheiro `.env` para as chaves de API
- **Nota de Tradução**: Adição opcional de uma nota no fim do documento

## Instalação

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Ferramentas de qualidade (opcionais, mas recomendadas)

O projeto utiliza [`pre-commit`](https://pre-commit.com) para impedir commits de código mal formatado, vulnerável ou que contenha um segredo. Instalação:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hooks ativos: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexidade), detect-secrets (chaves de API), mypy (tipagem progressiva), Opengrep (SAST), pip-audit (CVE das dependências), unittest. Consulte a secção _Quality / pre-commit_ de `CLAUDE.md` para obter detalhes.

## Configuração

Crie um ficheiro `.env` na raiz do projeto ou defina as variáveis de ambiente:

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

`GEMINI_API_KEY` é aceite como alternativa a `GOOGLE_API_KEY` (convenção do AI
Studio). Variáveis opcionais: `XAI_BASE_URL` (endpoint xAI, predefinição
`https://api.x.ai/v1`), `CLAUDE_TIMEOUT` (segundos por chamada Anthropic, predefinição
900), `CODEX_BIN` / `CODEX_TIMEOUT`, `GROK_BIN` / `GROK_HOME` / `GROK_TIMEOUT`,
e `GROK_TRANSLATE_SANDBOX` (consulte a secção Grok CLI). Para
`regen_translations.sh`: `REGEN_PROVIDER`, `REGEN_MODEL` e
`REGEN_JOB_TIMEOUT` (limite por job, predefinição 600 s).

## Utilização

### Traduzir um único ficheiro

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traduzir um diretório

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

### Traduzir com a sua subscrição ChatGPT (`--use_codex`)

Este provider não consome nenhuma chave de API: controla o CLI Codex oficial em modo
não interativo, pelo que a tradução é descontada da quota da subscrição
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

O binário é procurado nesta ordem: a variável `CODEX_BIN`, o `PATH`,
e depois o package Python `openai-codex-cli-bin`. Este último não está deliberadamente
em `requirements.txt`: pesa ~250 MB, o que seria imposto a todos os
utilizadores para um provider opcional.

**Informações importantes:**

- **Nenhuma chave de API é utilizada.** `OPENAI_API_KEY` e `CODEX_API_KEY` são
  removidas do ambiente do subprocesso, garantindo que uma chave
  presente em `.env` nunca fará a tradução passar para faturação por
  utilização.
- **Um segmento = uma «mensagem local»** da janela de 5 horas do plano.
  Utilize `--eco` (modelo `gpt-5.6-luna`, 250-2 000 mensagens/5 h no Plus)
  em vez do modelo de qualidade (`gpt-5.6-sol`, 10-100 mensagens/5 h).
- **Mais lento** do que uma chamada à API: conte com ~45 s para um README completo, contra
  alguns segundos diretamente.
- **Recusado em CI** (`CI` ou `GITHUB_ACTIONS` definido): a autenticação por
  subscrição não foi concebida para um runner partilhado, e a OpenAI desaconselha este
  workflow em repositórios públicos. Utilize uma chave de API neste caso.
- Variáveis de ambiente: `CODEX_BIN` (caminho explícito do binário) e
  `CODEX_TIMEOUT` (segundos por segmento, predefinição `600`).

### Traduzir com a sua subscrição Grok (`--use_grok_cli`)

O mesmo princípio que `--use_codex`, com o CLI oficial **Grok Build**: a
tradução é descontada da subscrição Grok (SuperGrok / X Premium+) em vez
de ser faturada por token.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # le binaire `grok`
grok login                                      # ou `grok login --device-code`
```

**Confinamento — leia antes de utilizar.** Este provider é estruturalmente **mais
fraco** do que `--use_codex`, e isso é assumido:

- O Codex é executado em `--sandbox read-only`, uma fronteira imposta pelo sistema.
- O sandbox do Grok **não pode ser aplicado** em muitas máquinas Linux
  recentes: o AppArmor bloqueia os user namespaces não privilegiados desde o Ubuntu
  24.04, e a deny-list dos sockets de runtime de contentores falha se
  `/run/podman` estiver em `0700`. Porém, um perfil **integrado** que não possa
  ser aplicado inicia **sem confinamento e em silêncio**.
- Por isso, o script não solicita nenhum perfil por predefinição e **nunca recua
  silenciosamente**: apresenta um aviso. O confinamento baseia-se nas
  regras `--deny` do CLI (incluindo o catch-all `*`), a única camada medida
  como _fail-closed_ — uma regra desconhecida faz com que o arranque seja recusado, em vez de
  remover a proteção sem o informar.
- Para **exigir** o sandbox do sistema operativo: `GROK_TRANSLATE_SANDBOX=read-only`. O
  arranque falhará se a máquina não puder respeitá-lo, que é o
  comportamento pretendido.

**Quota**: o pool do Grok é **semanal e partilhado** com Chat, Imagine e
Voice, e nenhum comando permite consultá-lo. Um processamento em lote pode, portanto,
consumir a sua utilização conversacional sem qualquer aviso — daí uma
concorrência limitada a 2 e um aviso em `regen_translations.sh`.

Outras variáveis: `GROK_BIN` (caminho do binário), `GROK_TIMEOUT` (predefinição 900 s).

Para a regeneração das 28 traduções:

```bash
REGEN_PROVIDER=codex ./regen_translations.sh --force

# Sur un modèle précis plutôt que le défaut --eco du provider
REGEN_PROVIDER=codex REGEN_MODEL=gpt-5.6-sol ./regen_translations.sh --force

# Sur le quota de l'abonnement Grok
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

### Modo económico

Utiliza modelos mais rápidos e económicos (gpt-5.6-luna, claude-haiku-4-5, gemini-3.1-flash-lite):

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opções

| Opção                   | Descrição                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Único ficheiro Markdown a traduzir                                       |
| `--source_dir`           | Diretório de origem que contém os ficheiros Markdown                        |
| `--target_dir`           | Diretório de saída para os ficheiros traduzidos                          |
| `--source_lang`          | Idioma de origem (predefinição: `fr`)                                             |
| `--target_lang`          | Idioma de destino (predefinição: `en`)                                              |
| `--model`                | Modelo específico a utilizar                                             |
| `--eco`                  | Utilizar os modelos económicos                                         |
| `--use_mistral`          | Utilizar a API Mistral AI                                                |
| `--use_claude`           | Utilizar a API Claude                                                    |
| `--use_gemini`           | Utilizar a API Gemini                                                    |
| `--use_codex`            | Utilizar o CLI Codex com a quota da subscrição ChatGPT               |
| `--use_grok`             | Utilizar a API xAI (Grok) — requer `XAI_API_KEY`                      |
| `--use_grok_cli`         | Utilizar o CLI Grok com a quota da subscrição Grok                   |
| `--force`                | Forçar uma nova tradução                                                  |
| `--keep_filename`        | Manter o nome original do ficheiro                                     |
| `--news`                 | Modo notícias: protege as citações EN e gere as bandeiras por idioma |
| `--add_translation_note` | Adicionar uma nota de tradução                                           |
| `--note_position`        | Posição da nota: `top`, `bottom` (predefinição) ou `both`                |
| `--note_format`          | Formato da nota: `legacy` (predefinição, parágrafo em negrito) ou `marker`       |
| `--include_model`        | Incluir o nome do modelo no ficheiro de saída                       |
| `--reasoning_effort`     | Esforço de raciocínio GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`    |

> **Os seis flags de provider são mutuamente exclusivos.** Anteriormente, combinar dois
> era aceite em silêncio e resolvia para o primeiro testado: uma
> tradução solicitada com a quota da subscrição (`--use_codex`, `--use_grok_cli`)
> podia, assim, passar para faturação por utilização sem qualquer aviso.
> `argparse` recusa agora essa combinação.

### Nota de tradução: posições e formatos

Com `--add_translation_note`, o translator pode colocar a nota no topo, no fim ou em ambos os locais, e apresentá-la em formato de texto simples (retrocompatível) ou no formato `marker`, que pode ser utilizado por um plugin Markdown.

**Posição** (`--note_position`):

- `bottom` (predefinição): nota no fim do ficheiro, como historicamente.
- `top`: nota inserida **após o frontmatter YAML** (segurança do Astro Content Collections, gray-matter etc.).
- `both`: nota inserida no topo E no fim (uma única chamada LLM, conteúdo reutilizado para ambas as posições).

**Formato** (`--note_format`):

- `legacy` (predefinição): parágrafo em negrito `**...**` — comportamento rigorosamente idêntico à v1.8, byte-for-byte. Compatível com Hugo, GitHub, GitLab e qualquer renderer Markdown.
- `marker`: definição de referência de link Markdown invisível (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`), seguida de um blockquote em negrito. Legível nativamente no GitHub/GitLab e utilizável durante o build por um plugin remark no Astro para produzir um banner estilizado (cf. blog jls42.org).

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

### Modelos predefinidos (2026)

| Provider | Qualidade (predefinição)       | Económico (`--eco`)    |
| -------- | ---------------------- | ----------------------- |
| OpenAI   | `gpt-5.6-terra`        | `gpt-5.6-luna`          |
| Claude   | `claude-sonnet-5`      | `claude-haiku-4-5`      |
| Mistral  | `mistral-large-latest` | `mistral-small-latest`  |
| Gemini   | `gemini-3.7-flash`     | `gemini-3.1-flash-lite` |
| Codex    | `gpt-5.6-sol`          | `gpt-5.6-luna`          |
| Grok API | `grok-4.6`             | `grok-4.3`              |
| Grok CLI | `grok-4.6`             | `grok-4.5`              |

> **Recomendação para traduções long-form**: `--use_gemini` (predefinição = `gemini-3.7-flash`) preserva fielmente a estrutura Markdown em scripts não latinos (PL, JA, ZH, AR, HI), incluindo no modo `--news`, no qual a fidelidade dos placeholders é importante. Medido neste README traduzido para japonês: estrutura idêntica a `gemini-3.1-pro-preview` (21 listas, 18 blocos de código, 13 links HTML, 13 imagens, todos os URLs preservados), com uma latência ~6x menor. A OpenAI continua a ser a opção predefinida para garantir a retrocompatibilidade.

## Projetos que utilizam este script

- **[jls42.org](https://jls42.org)** - Blog pessoal multilingue (15 idiomas)

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licença

GNU GENERAL PUBLIC LICENSE Version 3. Consulte [LICENSE](LICENSE).

**Artigo traduzido do francês para o português com o gpt-5.6-sol.**
