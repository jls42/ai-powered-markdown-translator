# Tradutor de Markdown AI-Powered

🌍 [Francês](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Inglês](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Espanhol](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Alemão](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Neerlandês](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polaco](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Romeno](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Sueco](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

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

Traduz ficheiros Markdown de um idioma para outro, preservando a
estrutura: blocos de código, código inline, URLs, âncoras, tabelas e front
matter. Nove formas de chamar um modelo — cinco APIs, duas subscrições sem
faturação por utilização, dois routers — e uma medição publicada do que cada
modelo realmente preserva.

## Em resumo

- **Nove caminhos de provider**: APIs OpenAI, Mistral, Claude, Gemini e Grok;
  subscrições ChatGPT (Codex) e Grok sem faturação por utilização; routers
  OpenCode (open source, gratuito ou local) e OpenRouter (mais de 400 modelos).
- **Nada incorreto devido à perda de um token**: blocos de código, código inline,
  URLs, âncoras e citações são substituídos por tokens antes da chamada e
  verificados no retorno. Se faltar algum, o ficheiro não é escrito.
- **Documentos longos**: segmentação de acordo com a janela do modelo.
- **Modo `--news`**: citações em inglês protegidas e bandeiras geridas por
  idioma, para artigos de monitorização.
- **Modo `--eco`**: modelos rápidos e mais baratos.
- **Nota de tradução** opcional, no início, no fim ou em ambos.

## Instalação

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 ou mais recente. Para instalar a partir do repositório, consulte
[Contribuir](#contribuir).

## Configuração

As chaves são lidas em três locais, do mais prioritário para o menos prioritário;
cada um apenas preenche o que o anterior deixou vazio.

|     | Onde                                          | Para quê                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variáveis de ambiente                         | CI, contentores, substituição pontual |
| 2   | `.env` do diretório atual (ou de um diretório pai) | uma chave específica de um projeto    |
| 3   | `~/.config/aipmt/.env`                        | instalado uma vez, válido em todo o lado |

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

`GEMINI_API_KEY` é aceite em vez de `GOOGLE_API_KEY`. O ficheiro
do utilizador segue `XDG_CONFIG_HOME` (apenas caminho absoluto) e `%APPDATA%`
no Windows. Sem uma chave, o comando enumera os três locais.

**O `.env` de um projeto não pode redirecionar as chamadas.** Fornece chaves,
nunca um destino: qualquer variável em `_BASE_URL`, `_API_BASE` ou
`_ENDPOINT`, os proxies (`HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`), os
repositórios de certificados (`SSL_CERT_FILE`, `SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`,
`CURL_CA_BUNDLE`) e `XDG_CONFIG_HOME` / `APPDATA` são aí ignorados, com um
aviso. Um repositório clonado não deve poder desviar a sua chave. Este
ficheiro também é lido sem interpolação: `NOM=${OPENAI_API_KEY}` não copia
a chave para aí. Defina estas variáveis no ambiente ou em
`~/.config/aipmt/.env`.

Variáveis opcionais: `XAI_BASE_URL` (predefinição `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (segundos por chamada, predefinição 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(predefinição 600), `GROK_BIN`, `GROK_HOME` (predefinição `~/.grok`), `GROK_TIMEOUT`
(predefinição 900), `GROK_TRANSLATE_SANDBOX`, `OPENCODE_BIN`, `OPENCODE_TIMEOUT`
(predefinição 600), `OPENROUTER_BASE_URL` (`https://` obrigatório), `OPENROUTER_TIMEOUT`
(predefinição 900), `OPENROUTER_PREFLIGHT_TIMEOUT` (predefinição 30). Cada uma é detalhada
na secção do respetivo provider.

## Primeiros passos

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` traduzido para espanhol dá `document-es.md` em `--target_dir`;
com `--include_model`, `document-es-gpt-5.6-terra.md`. A extensão passa
sempre a ser `.md` — `article.mdx` dá `article-en.md` — exceto com
`--keep_filename`, que mantém o nome original. Uma tradução já existente
é ignorada sem `--force`.

Códigos de saída: `0` se tudo tiver sido concluído ou ignorado, `1` se ainda houver um ficheiro
com falha (lista na saída de erro), `2` se o problema estiver na configuração.
Um ficheiro com falha nunca é escrito, mesmo que a própria escrita falhe:
o conteúdo é escrito ao lado e depois renomeado. Basta executar novamente.

## Que modelo escolher

Medido em dois documentos reais, traduzidos para os mesmos catorze idiomas por
cada modelo. **O número representa a quantidade de idiomas, entre catorze, em que a
tradução é escrita e nada difere da fonte.**

| Modelo               | Como aceder                       | Artigo de monitorização denso | Este README  | O que difere e em quantos idiomas                                                                                                     |
| -------------------- | --------------------------------- | ----------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Gemini 3.7 Flash** | chave da API Google               | ✅ 14/14                      | ⚠️ 13/14     | 1 idioma em 14: uma palavra adicional em negrito (ja)                                                                                 |
| **GPT-5.6 Sol**      | subscrição ChatGPT ou chave OpenAI | ✅ 14/14                     | ⚠️ 12/14     | 2 idiomas em 14: uma palavra a menos em negrito (ar, ja)                                                                              |
| **GLM-5.2**          | chave OpenRouter                  | ✅ 14/14                      | ⚠️ 11/14     | 3 idiomas em 14: uma palavra a menos em negrito (hi, ja, ko)                                                                          |
| Claude Sonnet 5      | chave da API Anthropic            | ⚠️ 11/14                      | ⚠️ 12/14     | 3 idiomas no artigo: surgiu um bloco de código (es, de, hi); 2 neste README: um link sem a respetiva marcação (sv), uma palavra em negrito (zh) |
| Qwen 3.7 Flash       | chave OpenRouter                  | ❌ 8/14                       | ⚠️ 10/14     | 1 idioma recusado no artigo, outros 5 divergem; neste README, cerca de quarenta palavras colocadas em `code` (ar)              |
| Grok 4.6             | subscrição Grok                   | ❌ 8/14                       | não avaliado | 5 idiomas recusados em 14 por falta de código inline e URLs devolvidos; o neerlandês diverge em tudo                                  |
| GPT-OSS 20B          | modelo local (Ollama)             | ❌ 7/14                       | não medido novamente | 4 idiomas recusados em 14: o modelo deixava passagens em francês e a proteção impediu-as                                              |
| MiMo v2.5 (gratuito) | OpenCode Zen, sem conta           | ❌ 11/14                      | não medido novamente | 1 idioma recusado; uma secção perdida em polaco                                                                                       |
| Mistral Large        | chave da API Mistral              | ❌ 5/14                       | ❌ 1/14      | **desaparece uma secção inteira**: 1 idioma no artigo (hi), 3 neste README (ar, hi, ko) — e 3 idiomas recusados no artigo               |
| DeepSeek V4 Flash    | chave OpenRouter                  | ❌ 3/14                       | não medido novamente | 10 idiomas recusados em 14; 37 minutos por idioma                                                                                     |

|     | O que significa o símbolo                                                                                                                                                                             |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | os catorze idiomas traduzidos e nada difere da fonte                                                                                                                                                  |
| ⚠️  | os catorze idiomas traduzidos; o que difere é a **marcação** — uma palavra em negrito, um `code`, um link que perde os colchetes. Não falta texto, URL, bloco de código ou secção |
| ❌  | pelo menos um idioma não pôde ser traduzido — o ficheiro é recusado, não escrito — **ou** falta conteúdo num ficheiro escrito                                                                          |

O que deve reter:

- **Uma tradução recusada não é uma tradução danificada.** Quando falta um token
  no retorno, o ficheiro não é escrito e o idioma conta como
  recusado. É o que acontece com o Grok no artigo: quatro códigos inline e
  três URLs perdidos logo no primeiro segmento, nos cinco sistemas de escrita não latinos.
- **Esta rede de segurança não abrange títulos, tabelas, front matter nem
  texto.** Um modelo que elimina uma secção devolve um ficheiro que a ferramenta escreve
  sem protestar — é o caso do Mistral. Estes elementos não podem ser
  substituídos por um token e as proteções atuais não os verificam;
  `scripts/compare_structure.py` deteta uma secção perdida, mas apenas posteriormente.
- **O Grok não tem classificação neste README**: a sua sessão CLI expirou após doze
  idiomas, onze dos quais sem diferenças. Uma campanha interrompida não é avaliada.
- **A densidade do documento importa mais do que o idioma.** O Grok funciona em
  README comuns e falha num artigo carregado de links, inclusive em
  neerlandês.

Datas e documentos: a coluna «Este README» foi medida em 9 de setembro de 2026
numa revisão fixa deste ficheiro (785 linhas, 285 códigos inline, 89 linhas
de tabela), entretanto modificada. A coluna «Artigo de monitorização denso» provém da
campanha de 4 e 5 de setembro num artigo com 589 linhas, exceto a linha
do Grok, medida novamente em 9 de setembro noutra edição da mesma monitorização. As
tabelas completas, as durações e o protocolo encontram-se em
[Medições detalhadas](#medições-detalhadas).

## Todas as opções

| Opção                    | Descrição                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`           | Ficheiro Markdown único a traduzir (alternativa a `--source_dir`)                                             |
| `--source_dir`           | Diretório de origem que contém os ficheiros Markdown (predefinição: `content/posts`)                           |
| `--target_dir`           | Diretório de saída dos ficheiros traduzidos (predefinição: `traductions_en`)                                    |
| `--source_lang`           | Idioma de origem (predefinição: `fr`)                                                              |
| `--target_lang`           | Idioma de destino (predefinição: `en`)                                                             |
| `--model`           | Modelo específico a utilizar                                                                                 |
| `--eco`           | Utilizar os modelos económicos                                                                               |
| `--use_mistral`           | Utilizar a API Mistral AI                                                                                    |
| `--use_claude`           | Utilizar a API Claude                                                                                        |
| `--use_gemini`           | Utilizar a API Gemini                                                                                        |
| `--use_grok`           | Utilizar a API xAI (Grok) — requer `XAI_API_KEY`                                                            |
| `--use_codex`           | Utilizar o CLI Codex com a quota da subscrição ChatGPT                                                       |
| `--use_grok_cli`           | Utilizar o CLI Grok com a quota da subscrição Grok                                                           |
| `--use_opencode`           | Utilizar OpenCode (open source) com o provider configurado no OpenCode; requer `--model provider/modèle`                 |
| `--use_openrouter`           | Utilizar OpenRouter — requer `OPENROUTER_API_KEY` e `--model fournisseur/modèle`                                                 |
| `--force`           | Forçar uma nova tradução                                                                                     |
| `--keep_filename`           | Manter o nome original do ficheiro                                                                           |
| `--news`           | Modo de notícias: protege citações em inglês e gere as bandeiras por idioma                                  |
| `--add_translation_note`           | Adicionar uma nota de tradução                                                                               |
| `--note_position`           | Posição da nota: `top`, `bottom` (predefinição) ou `both`                             |
| `--note_format`           | Formato da nota: `legacy` (predefinição, parágrafo em negrito) ou `marker`                        |
| `--include_model`           | Incluir o nome do modelo no ficheiro de saída                                                                |
| `--reasoning_effort`           | Esforço de raciocínio GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`   |

Os oito flags `--use_*` são mutuamente exclusivos: combinar dois é
recusado.

## Providers

### Por API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` muda para o nível económico de cada provider.

| Provider   | Qualidade (predefinição)                            | Económico (`--eco`)      |
| ---------- | --------------------------------------------------- | ------------------------------- |
| OpenAI     | `gpt-5.6-terra`                                     | `gpt-5.6-luna`                 |
| Claude     | `claude-sonnet-5`                                     | `claude-haiku-4-5`                 |
| Mistral    | `mistral-large-latest`                                     | `mistral-small-latest`                 |
| Gemini     | `gemini-3.7-flash`                                     | `gemini-3.1-flash-lite`                 |
| Codex      | `gpt-5.6-sol` (também `terra` e `luna` através de `--model`) | `gpt-5.6-luna` |
| Grok API   | `grok-4.6`                                     | `grok-4.3`                 |
| Grok CLI   | `grok-4.6`                                     | `grok-4.5`                 |
| OpenCode   | `--model provider/modèle` obrigatório                         | igual — `--eco` sem efeito |
| OpenRouter | `--model fournisseur/modèle` obrigatório                         | igual — `--eco` sem efeito |
### Sobre a assinatura ChatGPT: `--use_codex`

Controla o CLI Codex oficial: a tradução é descontada da cota da
assinatura ChatGPT, sem chave de API nem cobrança por uso.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- O binário é procurado em `CODEX_BIN`, depois no `PATH` e, em seguida, no package
  `openai-codex-cli-bin`. `~/.codex/auth.json` nunca é lido.
- `OPENAI_API_KEY` e `CODEX_API_KEY` são removidas do ambiente do
  subprocesso: a presença de uma chave nunca faz alternar para a API.
- Cada segmento custa pelo menos uma «mensagem» da janela de 5 horas — duas
  se a validação falhar e ele for tentado novamente. A OpenAI anuncia, a título
  de estimativa, 250-2 000 mensagens/5 h para `gpt-5.6-luna` (`--eco`) e
  10-100 para `gpt-5.6-sol` em um plano Plus.
- `--model gpt-5.6-terra` e `--model gpt-5.6-luna` também passam pela
  assinatura. Um modelo ao qual a conta não tem direito retorna um erro 400 «model is
  not supported when using Codex with a ChatGPT account».
- Mais lento que uma API, e a diferença aumenta com o documento: neste README,
  6 min 46 s por idioma na mediana com `gpt-5.6-sol`, contra 36 s para
  `gemini-3.7-flash`.
- Recusado em CI (`CI` ou `GITHUB_ACTIONS` definido): a assinatura autentica-se
  por meio de um arquivo de sessão pessoal, que não deve estar em um runner
  compartilhado.
- Variáveis: `CODEX_BIN`, `CODEX_TIMEOUT` (segundos por segmento, padrão 600).

### Sobre a assinatura Grok: `--use_grok_cli`

O mesmo princípio com o CLI oficial Grok Build, na assinatura SuperGrok ou
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Confinamento mais fraco que o do Codex.** O sandbox do SO do Grok não se aplica
  em muitas máquinas Linux recentes (AppArmor, sockets de runtime de
  contêiner), e um perfil que não pode ser aplicado inicia silenciosamente sem
  confinamento. Por isso, o script não solicita nenhum perfil por padrão, informa
  isso e se baseia nas regras `--deny` do CLI, incluindo a catch-all `*` — a única
  camada que se recusa a iniciar em vez de remover a proteção sem
  avisar. `GROK_TRANSLATE_SANDBOX=read-only` exige o sandbox do SO, e a inicialização
  falha se a máquina não puder garanti-lo.
- A cota é semanal, compartilhada com Chat, Imagine e Voice, e nenhum
  comando permite consultá-la: um lote pode consumir o uso conversacional
  sem nenhum aviso.
- Variáveis: `GROK_BIN`, `GROK_HOME` (diretório do CLI, padrão `~/.grok`),
  `GROK_TIMEOUT` (padrão 900), `GROK_TRANSLATE_SANDBOX`.

### Para o fornecedor de sua escolha: `--use_opencode`

[OpenCode](https://opencode.ai) é um agente de código open source (MIT) que
encaminha para os fornecedores configurados nele: chave de API, assinatura,
gateway OpenCode Zen (modelos gratuitos, sem conta) ou modelo local. Duas
opções foram medidas de ponta a ponta aqui, Zen e Ollama.

```bash
curl -fsSL https://opencode.ai/install | bash   # ou : npm install -g opencode-ai
opencode models                                 # les modèles, au format provider/modèle
opencode auth login                             # facultatif : brancher un fournisseur

# gratuit, sans compte ni clé — données utilisables pour l'entraînement
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en
# local, hors ligne
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de
# sur un abonnement déjà payé
aipmt --use_opencode --model github-copilot/gpt-5 --file README.md --target_dir . --target_lang ja
```

`--model` é obrigatório: sem ele, o OpenCode recorreria a um modelo gratuito
cujas interações podem ser usadas para treinamento, e essa escolha não é feita
em seu lugar.

Confinamento em cada chamada:

- uma configuração inline, com prioridade sobre a sua, define um agente `aipmt`
  no qual todas as ferramentas são recusadas (`permission: { "*": "deny" }`), o compartilhamento de
  sessão é desativado, `--pure`, nunca `--auto`;
- diretório de trabalho descartável e vazio, com `OPENCODE_DISABLE_PROJECT_CONFIG` e
  `OPENCODE_DISABLE_CLAUDE_CODE` definidos — sem eles, o OpenCode injeta no
  prompt o `AGENTS.md` do diretório atual e `~/.claude/CLAUDE.md`. O
  `~/.config/opencode/AGENTS.md` global continua sendo injetado, pois o OpenCode não permite
  excluí-lo;
- contrato de saída: código de retorno 0, nenhum evento `error`, nenhuma chamada
  de ferramenta, último passo em `stop`, texto não vazio e o agente `aipmt`
  efetivamente carregado — um `--agent` desconhecido não faz o OpenCode falhar; ele
  recorre silenciosamente ao agente de codificação;
- nenhuma chave de `aipmt` é transmitida, exceto `OPENCODE_API_KEY`, a chave
  do próprio OpenCode. Os fornecedores são configurados no OpenCode, não no
  `.env` de `aipmt`.

O que você precisa saber:

- Os modelos gratuitos do Zen mudam, têm limites não documentados e
  suas interações podem ser usadas para treinamento: servem para documentação
  pública, não para conteúdo privado.
- Um modelo local deve oferecer pelo menos 16 k tokens de contexto, pois os segmentos
  podem ter até 16 000 caracteres. O Ollama frequentemente configura 4 096: use
  um `Modelfile` com `PARAMETER num_ctx 32768`.
- `--eco` não tem efeito; `--reasoning_effort` é transmitido sem alterações como
  `--variant` do OpenCode.
- O OpenCode registra cada sessão em `~/.local/share/opencode/`.
- Variáveis: `OPENCODE_BIN` (caso contrário, o `PATH`, depois `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (segundos por segmento, padrão 600). `OPENCODE_CONFIG`
  é passado sem alterações ao OpenCode.

Exemplo de um modelo local via Ollama, em `~/.config/opencode/opencode.json`:

```bash
ollama pull gpt-oss:20b
printf 'FROM gpt-oss:20b\nPARAMETER num_ctx 32768\n' > gpt-oss-20b-32k.Modelfile
ollama create gpt-oss-20b-32k -f gpt-oss-20b-32k.Modelfile
```

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

`reasoningEffort: "none"` desativa o raciocínio que o Ollama ativa por padrão nesses
modelos e que um Modelfile não pode desativar. Medição em uma frase de
seis palavras: 919 tokens de raciocínio e 68 segundos sem a opção, 9 tokens com ela.

### Para mais de 400 modelos: `--use_openrouter`

O OpenRouter é um roteador cobrado por uso, com um crédito único, diante de
modelos hospedados por terceiros — incluindo os modelos chineses abertos que nenhum
outro provider disponibiliza aqui.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` é obrigatório. Um preflight, executado antes de qualquer cobrança, trata
duas particularidades do roteamento:

- **Um mesmo modelo é fornecido por dezenas de provedores de hospedagem com limites
  diferentes** — em `z-ai/glm-5.3-flash`, 23 provedores, incluindo um limitado a
  2 048 tokens de saída. O preflight lê `/api/v1/models/{modèle}/endpoints`,
  descarta os provedores com menos de 8 000 tokens de saída ou com status degradado e
  fixa os demais com `allow_fallbacks: false`.
- **O raciocínio é cobrado pela tarifa de saída** — 107 tokens contra 2 em
  uma resposta «OK» de `z-ai/glm-5.2`. Ele é desativado por padrão; os modelos
  que o exigem recebem o menor esforço que aceitam, pois o padrão do
  catálogo pode saturar a saída antes do fim da tradução.
  `--reasoning_effort` continua tendo prioridade.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- A janela de contexto vem do catálogo. Um modelo com menos de 16 400 tokens é
  recusado antes de qualquer chamada: 8 400 para o prompt e o segmento, no mínimo
  8 000 de saída.
- Um slug ausente do catálogo, um catálogo inacessível ou a ausência
  de um provedor que suporte o limite interrompem o comando.
- `finish_reason=length` com uma saída vazia é um orçamento consumido pelo
  raciocínio, não um truncamento: a mensagem faz essa distinção.
- `--eco` não tem efeito.
- Variáveis: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (padrão `https://openrouter.ai/api/v1`, `https://`
  exigido), `OPENROUTER_TIMEOUT` (padrão 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (padrão 30).

### Nota de tradução

`--add_translation_note` adiciona uma nota, em `bottom` (padrão), `top` (após o
front matter) ou `both` (`--note_position`), no formato `legacy` (parágrafo em
negrito, padrão) ou `marker` (`--note_format`). O formato `marker` é uma
definição de referência Markdown invisível,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
seguida de uma citação em negrito: legível no GitHub, utilizável durante o build por um
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Medições detalhadas

Todas as medições são traduções realmente executadas com `aipmt`, para
quatorze idiomas: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Escritas** conta os arquivos que passaram pelas proteções; **Sem
diferença**, aqueles em que `scripts/compare_structure.py` não detecta nada — mesmo número de
seções, subtítulos, links, URLs distintas, blocos de código,
códigos inline, linhas de tabela, blocos de citação e palavras em negrito.

«Sem diferença» significa «nada detectado», não «idêntico»: o comparador
conta elementos sem ler seu conteúdo. Ele não detecta um título de
nível 4 removido, nem o texto de um código inline substituído, nem uma flag
trocada, e não avalia o idioma.

### Artigo denso de monitoramento, modo `--news`

Uma edição do [monitoramento de IA do jls42.org](https://jls42.org/fr/news):
589 linhas, 140 links, 21 seções, 3 citações em inglês protegidas. Campanha
de 4 e 5 de setembro de 2026.

| Modelo                            | Acesso             | Escritas | Sem diferença | Mediana/idioma |
| --------------------------------- | ------------------ | -------- | ------------- | -------------- |
| `gemini-3.7-flash`                | API Google         | 14/14    | ✅ **14/14**  | 1 min 18 s     |
| `gpt-5.6-sol` (`--use_codex`)     | assinatura ChatGPT | 14/14    | ✅ **14/14**  | 11 min 28 s    |
| `z-ai/glm-5.2`                    | OpenRouter         | 14/14    | ✅ **14/14**  | 5 min 37 s     |
| `qwen/qwen3.8-flash`              | OpenRouter         | 14/14    | ✅ **14/14**  | 26 min 23 s    |
| `claude-sonnet-5`                 | API Anthropic      | 14/14    | ⚠️ 11/14      | 6 min 31 s     |
| `opencode/mimo-v2.5-free`         | OpenCode Zen       | 13/14    | ❌ 11/14      | 9 min 27 s     |
| `qwen/qwen3.7-flash`              | OpenRouter         | 13/14    | ❌ 8/14       | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`          | local              | 10/14    | ❌ 7/14       | 12 min 39 s    |
| `mistral-large-latest`            | API Mistral        | 11/14    | ❌ 5/14       | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731` | OpenRouter         | 4/14     | ❌ 3/14       | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)     | assinatura Grok    | 1/14     | ❌ 1/14       | 23 min 11 s    |

O Grok foi medido novamente em 9 de setembro em outra edição do mesmo monitoramento
(356 linhas): 9 idiomas escritos de 14, 8 sem diferença. É esse número que
aparece na tabela inicial. Três campanhas interrompidas não foram
registradas: `qwen3.5-27b` (9 idiomas) e `kimi-k2.6` (4) por falta de crédito,
`z-ai/glm-5.3-flash`, cujas duas falhas vieram de uma configuração de raciocínio
que o provider está corrigindo. As linhas do OpenRouter foram medidas com as
configurações padrão do roteador, antes de `--use_openrouter`; `z-ai/glm-5.2`,
medido novamente com o provider fornecido, produz o mesmo 14/14. Os números foram
recalculados em 10 de setembro com o comparador atual: `qwen3.8-flash` e
`qwen3.7-flash` ganham cada um um idioma em relação à primeira
publicação; os demais permanecem inalterados.

### README deste projeto, Markdown padrão

Revisão fixada em 9 de setembro de 2026: 785 linhas, 285 códigos inline, 40
fechamentos de blocos, 89 linhas de tabela. Quatro traduções em paralelo.

| Modelo                        | Escritas | Sem diferença | Mediana/idioma | O que difere                                                              |
| ----------------------------- | -------- | ------------- | -------------- | ------------------------------------------------------------------------- |
| `gemini-3.7-flash`            | 14/14    | ⚠️ 13/14       | 36 s           | uma palavra em negrito (ja)                                               |
| `claude-sonnet-5`             | 14/14    | ⚠️ 12/14       | 2 min 56 s     | um link (sv), uma palavra em negrito (zh)                                 |
| `gpt-5.6-sol` (`--use_codex`) | 14/14    | ⚠️ 12/14       | 6 min 46 s     | uma palavra em negrito (ar, ja)                                           |
| `z-ai/glm-5.2` (OpenRouter)   | 14/14    | ⚠️ 11/14       | 2 min 34 s     | uma palavra em negrito (hi, ja, ko)                                       |
| `qwen/qwen3.7-flash`          | 14/14    | ⚠️ 10/14       | 2 min 17 s     | 40 códigos inline adicionados em árabe; negrito (hi, ja, ko)              |
| `mistral-large-latest`        | 14/14    | ❌ 1/14         | 2 min 44 s     | uma seção perdida (ar, hi, ko); blocos de código adicionados (ja, ko, ro, zh) |

Duas campanhas interrompidas não foram registradas: Grok, sessão do CLI expirada
após doze idiomas (onze sem diferença), e `qwen3.8-flash`, HTTP 429 de seu
provedor de hospedagem após dois. `opencode/mimo-v2.5-free` e `ollama/gpt-oss-20b-32k`
não foram medidos novamente nesta revisão; na de 4 e 5 de setembro,
277 linhas mais curta, cada um escrevia 9 traduções de 14, sendo 7
e 1 sem diferença.

### Quatro README de projetos conhecidos

FastAPI, Ollama, tldr-pages e Vue.js, usados tal como estão no GitHub — documentos
mais fáceis que os dois anteriores. A campanha teve como alvo os modelos
com dificuldades; o Gemini serve como ponto de comparação.

| Modelo                    | Escopo                     | Escritas | Sem diferença |
| ------------------------- | -------------------------- | -------- | ------------- |
| `gemini-3.7-flash`        | 4 projetos × 14 idiomas    | 56/56    | ✅ **55/56**  |
| `opencode/mimo-v2.5-free` | 4 projetos × 14 idiomas    | 55/56    | ❌ 47/56      |
| `grok-4.6` (assinatura)   | 4 projetos × ar, hi, ja, zh | 16/16    | ❌ 14/16      |
| `ollama/gpt-oss-20b-32k`  | 4 projetos × ar, hi, ja, zh | 15/16    | ❌ 9/16       |

### O que estas medições não são

- **Não são uma classificação exaustiva**: só o OpenRouter oferece mais de quatrocentos
  modelos; cerca de quinze foram medidos.
- **São durações indicativas**: de três a seis traduções em paralelo, dependendo
  das campanhas, e a vazão de um fornecedor varia ao longo do dia.
- **São observações datadas**: os modelos mudam sob o mesmo nome, e seus
  documentos não são os nossos.

Para repetir a medição em seus documentos, usando uma cópia fixa do arquivo:

```bash
aipmt --file reference.md --target_dir out/ --source_lang fr --target_lang ja --use_gemini --force
aipmt --file veille.mdx   --target_dir out/ --source_lang fr --target_lang ja --use_gemini --news --force
python scripts/compare_structure.py reference.md out/reference-ja.md
# « structure identique », ou la liste des écarts — sortie 0 si identique, 1 sinon
```

## Contribuir

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # les dépendances, lock entièrement épinglé
pip install -e .                  # le paquet lui-même, en mode éditable
```

As duas linhas são necessárias: sem `pip install -e .`, `python -m aipmt`
responde `No module named aipmt`.

Ferramentas de qualidade, opcionais, mas recomendadas:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

As 28 traduções do repositório (README e CHANGELOG, quatorze idiomas) são
regeneradas com `./regen_translations.sh --force` — Codex e `gpt-5.6-sol` na
assinatura ChatGPT por padrão, quatro em paralelo. `REGEN_PROVIDER` e
`REGEN_MODEL` alteram o caminho; uma API cobrada (`openai`, `gemini`,
`grok`, `openrouter`) é recusada sem `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` limita cada job (600 s, 1 800 s no Codex). Os detalhes
das ferramentas estão em `CLAUDE.md`.

## Projetos que utilizam este script

- **[jls42.org](https://jls42.org)** — blog pessoal publicado em 15 idiomas. Seu
  [monitoramento diário de IA](https://jls42.org/fr/news) é traduzido todos os dias
  por esta ferramenta e serve como documento de referência para as medições acima.

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licença

GNU GENERAL PUBLIC LICENSE Version 3. Consulte [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Aviso

Este programa é distribuído **sem nenhuma garantia**, nos termos das
seções 15 e 16 da GPL v3: fornecido «no estado em que se encontra», sem garantia de qualidade
comercial nem de adequação a uma finalidade específica, e seu autor não pode ser
responsabilizado por danos decorrentes de seu uso. O texto da
licença prevalece sobre este resumo.

- **Revise antes de publicar.** As proteções abrangem os blocos de código, o
  código inline, as URLs, as âncoras e as citações do modo `--news` — não os
  títulos, as tabelas, o front matter nem o sentido de suas frases.
- **Seus documentos são enviados ao fornecedor escolhido**, de acordo com seus termos
  de uso e sua política de dados. Alguns modelos gratuitos podem
  reutilizar suas interações para treinamento; um modelo local é a única
  opção que não envia nenhum dado para fora de sua máquina.
- **As chamadas de API são cobradas de você.** Este programa não limita a
  despesa: um documento longo, uma retomada após uma falha ou um modelo que raciocina
  muito custam mais.
- **As medições publicadas são observações datadas**, não garantias.

Os nomes de produtos e empresas mencionados pertencem a seus respectivos
proprietários. Este projeto não é afiliado a nenhum deles.

**Artigo traduzido do francês para o português com o gpt-5.6-sol.**
