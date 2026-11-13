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
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Emblema Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Traduz ficheiros Markdown de uma língua para outra, preservando a
estrutura: blocos de código, código em linha, URL, âncoras, tabelas e front
matter. Onze formas de chamar um modelo — cinco API, quatro subscrições sem
faturação por utilização, dois routers — e uma medição publicada do que cada
modelo realmente preserva.

## Em resumo

- **Onze vias de provider**: API OpenAI, Mistral, Claude, Gemini e Grok;
  subscrições ChatGPT (Codex), Grok, Google (Antigravity) e Claude (Claude
  Code) sem faturação por utilização; routers OpenCode (open source, gratuito ou local) e OpenRouter
  (mais de 400 modelos).
- **Nenhum resultado incorreto por causa de um token perdido**: blocos de código, código em linha,
  URL, âncoras e citações são substituídos por tokens antes da chamada e
  verificados no retorno. Se faltar algum, o ficheiro não é gravado.
- **Documentos longos**: segmentação de acordo com a janela do modelo.
- **Modo `--news`**: citações em inglês protegidas e flags geridas por
  língua, para artigos de acompanhamento.
- **Modo `--eco`**: modelos rápidos e mais baratos.
- **Nota de tradução** opcional, no início, no fim ou em ambos.

## Instalação

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 ou mais recente. Para instalar a partir do repositório, consulte
[Contribuir](#contribuir).

## Configuração

As chaves são lidas em três locais, por ordem decrescente de prioridade; cada um
preenche apenas o que o anterior deixou vazio.

|     | Onde                                            | Para quê                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variáveis de ambiente                     | CI, contentores, substituição pontual |
| 2   | `.env` do diretório atual (ou de um ascendente) | uma chave específica de um projeto            |
| 3   | `~/.config/aipmt/.env`                        | configurado uma vez, válido em todo o lado       |

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
do utilizador respeita `XDG_CONFIG_HOME` (apenas caminho absoluto) e `%APPDATA%`
no Windows. Sem chave, o comando enumera os três locais.

**O `.env` de um projeto não pode redirecionar chamadas nem escolher o programa
executado.** Fornece chaves, nunca um destino nem um binário: todas as
variáveis em `_BASE_URL`, `_API_BASE`, `_ENDPOINT` ou `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, os proxies (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), os repositórios de certificados (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) e `XDG_CONFIG_HOME` /
`APPDATA` são aí ignorados, com um aviso. Um repositório clonado não deve
poder desviar a sua chave nem fazê-lo executar o seu próprio programa na
primeira tradução. Este ficheiro também é lido sem interpolação:
`NOM=${OPENAI_API_KEY}` não copia a chave para aí. Defina estas variáveis no
ambiente ou em `~/.config/aipmt/.env`.

Variáveis opcionais: `XAI_BASE_URL` (predefinição `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (segundos por chamada, predefinição 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(predefinição 600), `GROK_BIN`, `GROK_HOME` (predefinição `~/.grok`), `GROK_TIMEOUT`
(predefinição 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (predefinição 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (predefinição 600), `OPENROUTER_BASE_URL`
(`https://` obrigatório), `OPENROUTER_TIMEOUT` (predefinição 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (predefinição 30). Cada uma é detalhada na
secção do respetivo provider.

## Primeiros passos

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` traduzido para espanhol resulta em `document-es.md` em `--target_dir`;
com `--include_model`, `document-es-gpt-5.6-terra.md`. A extensão passa a ser
sempre `.md` — `article.mdx` resulta em `article-en.md` — exceto com
`--keep_filename`, que mantém o nome original. Uma tradução já existente
é ignorada sem `--force`.

Códigos de saída: `0` se tudo tiver sido concluído ou ignorado, `1` se restar algum ficheiro
com falha (lista na saída de erro), `2` se a causa for a configuração.
Um ficheiro com falha nunca é gravado, mesmo se a própria gravação falhar:
o conteúdo é gravado num ficheiro adjacente e depois renomeado. Basta voltar a executar.

## Que modelo escolher

Medido em dois documentos reais, traduzidos para as mesmas catorze línguas por
cada modelo. **O número indica a quantidade de línguas, em catorze, em que a
tradução é gravada e nada difere da origem.**

| Modelo                | Como aceder                 | Artigo de acompanhamento denso | Este README    | O que difere e em quantas línguas                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | subscrição Google (Antigravity)   | ✅ 14/14                | ✅ 14/14     | nada, em nenhum dos dois documentos                                                                                                                                 |
| **Claude Sonnet 5.5** | chave API Anthropic                 | ✅ 14/14                | ✅ 14/14     | nada, em nenhum dos dois documentos                                                                                                                                 |
| **Gemini 3.7 Flash**  | chave API Google                    | ✅ 14/14                | ⚠️ 13/14     | 1 língua em 14: uma palavra a mais em negrito (ja)                                                                                                                      |
| **Gemini 3.7 Flash**  | subscrição Google (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 língua em 14: uma palavra a menos em negrito (ko)                                                                                                                     |
| **GPT-5.6 Sol**       | subscrição ChatGPT ou chave OpenAI | ✅ 14/14                | ⚠️ 12/14     | 2 línguas em 14: uma palavra a menos em negrito (ar, ja)                                                                                                                |
| **GLM-5.2**           | chave OpenRouter                    | ✅ 14/14                | ⚠️ 11/14     | 3 línguas em 14: uma palavra a menos em negrito (hi, ja, ko)                                                                                                            |
| Claude Sonnet 5       | subscrição Claude (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 1 língua em 14 no artigo: uma palavra a mais em negrito (zh); 1 neste README: uma linha de tabela unida à anterior, oculta na apresentação (ar)            |
| Claude Haiku 4.5      | subscrição Claude (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 3 línguas no artigo: um título de secção passou para o nível 1 (en, pl, ro); neste README, nada para o comparador, mas os links internos foram duplicados em inglês |
| Claude Sonnet 5       | chave API Anthropic                 | ⚠️ 11/14                | ⚠️ 12/14     | 3 línguas no artigo: surgiu um bloco de código (es, de, hi); 2 neste README: um link sem a sua marcação (sv), uma palavra em negrito (zh)                              |
| Claude Haiku 4.5      | chave API Anthropic                 | ⚠️ 7/14                 | ✅ 14/14     | 7 línguas no artigo: um título de secção passou para o nível 1 — em japonês, permaneceu em francês; nada neste README                                              |
| Claude Haiku 5.5      | chave API Anthropic                 | ⚠️ 11/14                | ❌ 12/14     | 3 línguas no artigo: um título de secção mudou de nível ou foi duplicado (ja, ko, zh); neste README, 2 línguas recusadas, código em linha perdido (ar, hi)    |
| Qwen 3.7 Flash        | chave OpenRouter                    | ❌ 8/14                 | ⚠️ 10/14     | 1 língua recusada no artigo, 5 outras apresentam desvios; neste README, cerca de quarenta palavras colocadas em `code` (ar)                                                    |
| Grok 4.6              | subscrição Grok                   | ❌ 8/14                 | não avaliado     | 5 línguas recusadas em 14, por não devolver o código em linha e os URL; o neerlandês diverge em tudo                                                               |
| GPT-OSS 20B           | modelo local (Ollama)             | ❌ 7/14                 | não medido novamente | 4 línguas recusadas em 14: o modelo deixava passagens em francês, e a proteção bloqueou-as                                                                  |
| MiMo v2.5 (gratuito)   | OpenCode Zen, sem conta         | ❌ 11/14                | não medido novamente | 1 língua recusada; uma secção perdida em polaco                                                                                                                  |
| Mistral Large         | chave API Mistral                   | ❌ 5/14                 | ❌ 1/14      | **uma secção inteira desaparece**: 1 língua no artigo (hi), 3 neste README (ar, hi, ko) — e 3 línguas recusadas no artigo                                |
| DeepSeek V4 Flash     | chave OpenRouter                    | ❌ 3/14                 | não medido novamente | 10 línguas recusadas em 14; 37 minutos por língua                                                                                                                 |
| Claude Opus 5.5       | subscrição Claude (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | o artigo foi recusado nas 14 línguas pelas proteções do Opus, devido a uma notícia breve de biologia; nada neste README                                               |

|     | O que significa o símbolo                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | as catorze línguas traduzidas, e nada difere da origem                                                                                                                                       |
| ⚠️  | as catorze línguas traduzidas; o que difere é a **marcação** — uma palavra em negrito, um `code`, um link que perde os parênteses retos. Não falta nenhum texto, URL, bloco de código ou secção |
| ❌  | pelo menos uma língua não pôde ser traduzida — o ficheiro é recusado, não é gravado — **ou** falta conteúdo num ficheiro gravado                                                                      |

O que reter destes resultados:

- **Uma tradução recusada não é uma tradução danificada.** Quando um token
  falta no retorno, o ficheiro não é gravado e a língua conta como
  recusada. É o que acontece ao Grok no artigo: quatro trechos de código em linha e
  três URL perdidos logo no primeiro segmento, nos cinco sistemas de escrita não latinos.
- **Um modelo pode recusar um documento inteiro por causa de uma única frase.** O Opus 5.5
  traduz este README sem qualquer desvio, mas não traduz nenhum artigo de acompanhamento: as suas
  proteções interrompem a resposta numa notícia breve de biologia. O ficheiro não é
  gravado, e o aipmt explica porquê.
- **Esta proteção não abrange os títulos, as tabelas, o front matter nem o
  texto.** Um modelo que elimina uma secção devolve um ficheiro que a ferramenta grava
  sem objeções — é o caso do Mistral. Estes elementos não podem ser
  substituídos por um token, e as proteções atuais não os verificam;
  `scripts/compare_structure.py` deteta uma secção perdida, mas só depois.
- **O Grok não tem avaliação neste README**: a sua sessão CLI expirou após doze
  línguas, das quais onze sem desvios. Uma campanha interrompida não recebe avaliação.
- **A densidade do documento conta mais do que a língua.** O Grok consegue lidar com
  README comuns e falha num artigo carregado de links, incluindo em
  neerlandês.

Datas e documentos: a coluna «Este README» foi medida em 9 de setembro de 2026
numa revisão fixa deste ficheiro (785 linhas, 285 trechos de código em linha, 89 linhas
de tabela), alterada desde então — exceto as linhas Antigravity e Claude Code,
medidas em 26 de setembro na revisão publicada com a 1.14.0, mais curta
(600 linhas, 257 trechos de código em linha, 85 linhas de tabela), e as linhas Claude
Sonnet 5.5, Haiku 5.5 e Haiku 4.5 pela API, medidas em 18 de outubro na
mesma revisão. A coluna «Artigo de acompanhamento denso» vem da campanha de
4 e 5 de setembro num artigo de 589 linhas, exceto a linha Grok, medida novamente em
9 de setembro noutra edição do mesmo acompanhamento, as linhas Antigravity e
Claude Code, medidas em 26 de setembro no mesmo artigo, e estas três linhas
Claude, em 18 de outubro. As tabelas completas, as durações e o protocolo estão
em [Medições detalhadas](#medições-detalhadas).
## Todas as opções

| Opção                   | Descrição                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Ficheiro Markdown único a traduzir (alternativa a `--source_dir`)                                             |
| `--source_dir`           | Diretório de origem que contém os ficheiros Markdown (predefinição: `content/posts`)                                   |
| `--target_dir`           | Diretório de saída para os ficheiros traduzidos (predefinição: `traductions_en`)                                    |
| `--source_lang`          | Idioma de origem (predefinição: `fr`)                                                                                  |
| `--target_lang`          | Idioma de destino (predefinição: `en`)                                                                                   |
| `--model`                | Modelo específico a utilizar                                                                                  |
| `--eco`                  | Utilizar os modelos económicos                                                                              |
| `--use_mistral`          | Utilizar a API Mistral AI                                                                                     |
| `--use_claude`           | Utilizar a API Claude                                                                                         |
| `--use_gemini`           | Utilizar a API Gemini                                                                                         |
| `--use_grok`             | Utilizar a API xAI (Grok) — requer `XAI_API_KEY`                                                           |
| `--use_codex`            | Utilizar o CLI Codex com a quota da subscrição ChatGPT                                                    |
| `--use_grok_cli`         | Utilizar o CLI Grok com a quota da subscrição Grok                                                        |
| `--use_antigravity`      | Utilizar o CLI Antigravity (`agy`) com a quota da subscrição Google AI Pro ou Ultra                       |
| `--use_claude_code`      | Utilizar o CLI Claude Code (`claude -p`) com a quota da subscrição Claude Pro ou Max                      |
| `--use_opencode`         | Utilizar OpenCode (open source) com o fornecedor configurado no OpenCode; requer `--model provider/modèle` |
| `--use_openrouter`       | Utilizar OpenRouter — requer `OPENROUTER_API_KEY` e `--model fournisseur/modèle`                          |
| `--force`                | Forçar uma nova tradução                                                                                       |
| `--keep_filename`        | Manter o nome original do ficheiro                                                                          |
| `--news`                 | Modo de notícias: protege as citações em EN, gere as bandeiras por idioma                                      |
| `--add_translation_note` | Adicionar uma nota de tradução                                                                                |
| `--note_position`        | Posição da nota: `top`, `bottom` (predefinição) ou `both`                                                     |
| `--note_format`          | Formato da nota: `legacy` (predefinição, parágrafo a negrito) ou `marker`                                            |
| `--include_model`        | Incluir o nome do modelo no ficheiro de saída                                                            |
| `--reasoning_effort`     | Esforço de raciocínio GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

As nove flags `--use_*` são mutuamente exclusivas: combinar duas é
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

`--eco` muda para o nível económico de cada fornecedor.

| Provider    | Qualidade (predefinição)                                                     | Económico (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (também `gpt-5.6-sol`, `terra` e `luna` através de `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | idem — `--eco` sem efeito |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, esforço `low`                                               | idem — `--eco` sem efeito |
| OpenCode    | `--model provider/modèle` obrigatório                                | idem — `--eco` sem efeito |
| OpenRouter  | `--model fournisseur/modèle` obrigatório                             | idem — `--eco` sem efeito |

### Com a subscrição ChatGPT: `--use_codex`

Controla o CLI Codex oficial: a tradução é descontada da quota da
subscrição ChatGPT, sem chave API nem faturação por utilização.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- O binário é procurado em `CODEX_BIN`, depois em `PATH` e, por fim, no package
  `openai-codex-cli-bin`. `~/.codex/auth.json` nunca é lido.
- `OPENAI_API_KEY` e `CODEX_API_KEY` são removidas do ambiente do
  subprocesso: a presença de uma chave nunca provoca a mudança para a API.
- Cada segmento custa pelo menos uma «mensagem» da janela de 5 horas — duas
  se a validação falhar e houver uma nova tentativa. A OpenAI anuncia, como
  estimativa, 250-2 000 mensagens/5 h para `gpt-5.6-luna` (`--eco`) e
  10-100 para `gpt-5.6-sol` num plano Plus.
- `--model gpt-5.6-sol`, a predefinição até à 1.16.3, `--model gpt-5.6-terra`
  e `--model gpt-5.6-luna` também utilizam a subscrição.
- Um 429 do servidor não causa a perda do ficheiro: o Codex volta a ligar-se sozinho,
  o aipmt aguarda o fim do turno e, se o 429 persistir, o segmento
  é reenviado após 30 e depois 60 segundos. Um modelo ao qual a conta não tem acesso devolve um 400 «model is
  not supported when using Codex with a ChatGPT account».
- Mais lento do que uma API, e a diferença aumenta com o documento: neste README,
  a mediana é de 6 min 46 s por idioma com `gpt-5.6-sol`, contra 36 s com
  `gemini-3.7-flash`.
- Recusado em CI (`CI` ou `GITHUB_ACTIONS` definido): a subscrição autentica-se
  através de um ficheiro de sessão pessoal, que não deve estar num runner
  partilhado.
- Variáveis: `CODEX_BIN`, `CODEX_TIMEOUT` (segundos por segmento, predefinição 600).

### Com a subscrição Grok: `--use_grok_cli`

O mesmo princípio com o CLI oficial Grok Build, na subscrição SuperGrok ou
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Confinamento mais fraco do que o do Codex.** O sandbox do SO do Grok não se aplica
  em muitas máquinas Linux recentes (AppArmor, sockets de runtime
  de contentores), e um perfil que não pode ser aplicado inicia sem confinamento,
  silenciosamente. Por isso, o script não solicita nenhum perfil por predefinição, informa disso e
  apoia-se nas regras `--deny` do CLI, incluindo a catch-all `*` — a única
  camada que recusa iniciar em vez de remover a proteção sem o
  dizer. `GROK_TRANSLATE_SANDBOX=read-only` exige o sandbox do SO, e o arranque
  falha se a máquina não conseguir respeitar essa exigência.
- A quota é semanal, partilhada com Chat, Imagine e Voice, e nenhum
  comando permite consultá-la: um lote pode consumir a quota de utilização das conversas
  sem qualquer aviso.
- Variáveis: `GROK_BIN`, `GROK_HOME` (diretório do CLI, predefinição `~/.grok`),
  `GROK_TIMEOUT` (predefinição 900), `GROK_TRANSLATE_SANDBOX`.

### Com a subscrição Google: `--use_antigravity`

O mesmo princípio com `agy`, o CLI oficial do Antigravity: para quem paga Google
AI Pro ou Ultra, a tradução é descontada da quota da subscrição em vez
de ser faturada por token. Esta é a única via para essa quota: o Gemini CLI já não
serve estas contas desde 18 de junho de 2026
([anúncio](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
e o SDK do Antigravity só aceita uma chave API ou um projeto Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Nenhuma via paga permanece aberta.** O agy recebe do seu
  ambiente apenas uma lista fechada de variáveis — `PATH`, idioma e fuso horário,
  terminal, identidade, proxies e certificados, bus de sessão — e nenhuma chave:
  várias das suas variáveis redirecionam uma chamada sem apresentar nada (medido:
  uma envia o documento para um gateway de terceiros, outra para um projeto
  Google Cloud faturado), e uma lista de bloqueio deixava sempre alguma de fora a cada revisão.
  Antes de qualquer segmento, `agy -p /config`, que não consome quota, tem de mostrar
  os créditos de IA pagos desativados, sem chave API nem projeto Google Cloud — uma
  definição ausente implica recusa —, caso contrário, nada é traduzido; o registo de cada
  chamada tem depois de confirmar a subscrição (`authMethod=consumer`), caso contrário, a
  resposta é recusada.
- **Confinamento.** Cada chamada é executada num diretório pessoal privado e
  descartável, com um agente de tradução sem ferramentas: as suas definições, regras,
  plugins, servidores MCP e hooks do agy não entram nele, nada é acrescentado ao seu
  histórico, e a sessão permanece no porta-chaves, que o aipmt nunca lê.
  Um agente não encontrado faz o agy recorrer, silenciosamente, ao seu agente de programação
  e às respetivas ferramentas: uma linha inteira do registo tem de confirmar o agente correto — um
  documento que cite essa mensagem não a substitui —, caso contrário, há recusa.
- **Plataformas**: Linux, numa sessão com porta-chaves (bus de sessão
  D-Bus, Secret Service); o macOS é aceite, sem ter sido avaliado. Recusado
  no Windows, onde o agy não lê as variáveis que isolam cada chamada, e
  no Linux sem bus de sessão — sessão SSH, contentor, servidor: aí, o agy
  guarda o seu token num ficheiro de `~/.gemini`, que o isolamento oculta. A
  recusa ocorre antes de qualquer execução, com a respetiva causa, em vez de um minuto
  à espera de um código de início de sessão.
- **Modelos**: os de `agy models`. Os Gemini incluem o esforço no nome
  (`gemini-3.8-flash-medium`…): um nome sem sufixo é recusado antes da chamada,
  e `--reasoning_effort` não tem efeito. Por predefinição, `gemini-3.8-flash-medium`,
  e `gemini-3.7-flash-low` com `--eco`; as campanhas que os determinaram estão
  descritas em [Medições detalhadas](#medições-detalhadas). Claude e GPT-OSS
  têm a sua própria quota, muito menor: cerca de 1 % da janela de
  5 horas por chamada medida, contra 0,05 % em Flash.
- **Quota**: por grupo, uma janela de 5 horas e uma semanal, em
  proporção ao custo em tokens. Medido na conta do autor: cerca de
  16 pontos da janela de 5 horas por milhão de caracteres de origem com
  `gemini-3.8-flash-medium`, 14 com `gemini-3.7-flash-medium` e 7 a 8 com
  esforço baixo — um README de 40 000 caracteres custa, portanto, um pouco mais de
  meio ponto. O limite semanal depende do nível. As novas tentativas seguem
  o que o agy declara como passível de repetição; caso contrário, uma janela esgotada nunca
  dá origem a uma nova tentativa: faz falhar cada ficheiro até à reposição
  indicada por `/usage`.
- **Mais lento do que a API**: no artigo denso das medições, a mediana é de 3 min 59 s por
  idioma com `gemini-3.8-flash-medium` e 3 min 14 s com
  `gemini-3.7-flash-medium`, contra 1 min 18 s para Gemini 3.7 Flash pela API.
- **Interrupção**: Ctrl-C ou o fecho do terminal param o agy juntamente com o
  comando, em vez de o deixarem terminar o turno consumindo a sua quota; o mesmo se aplica
  a Codex, Grok CLI e OpenCode. Com `nohup`, a tradução continua.
- Recusado em CI (`CI` ou `GITHUB_ACTIONS` definido): a sessão reside num
  porta-chaves pessoal. Num runner, `--use_gemini` com `GOOGLE_API_KEY`.
- Variáveis: `AGY_BIN` (caso contrário, `PATH`, depois `~/.local/bin/agy`),
  `AGY_TIMEOUT` (segundos por segmento, incluindo o arranque, predefinição 900).

**Condições de utilização: é a sua conta que está em jogo.** As
[condições do Antigravity](https://antigravity.google/terms) (secção 6) e a sua
[FAQ](https://antigravity.google/docs/faq/) proíbem o acesso ao serviço
através de software de terceiros usando a sessão Antigravity — Claude Code,
OpenClaw e OpenCode são aí citados —, sob pena de suspensão da conta. O aipmt
não lê nem reutiliza o token: executa o binário oficial no
[modo headless](https://antigravity.google/docs/cli/headless/) que a Google
documenta para scripts e CI. Um membro da Google considerou «normal»
executar `agy -p` a partir de um script local para o seu próprio trabalho
([fórum oficial, 25 de setembro de 2026, resposta não contratual](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
nenhum texto esclarece o caso de uma ferramenta distribuída como esta.

**Apenas documentos públicos.** Segundo a secção 5 das mesmas condições, as
trocas — prompts, respostas, metadados — podem servir para melhorar os
produtos e a aprendizagem automática da Google e ser revistas por
humanos, mesmo com uma subscrição paga. A exclusão é feita através da definição
`enableTelemetry`, cujo efeito não está documentado e que o aipmt não configura; as suas definições
do agy não são transferidas para o ambiente isolado. Não envie nada de confidencial por esta via.
### Na assinatura Claude: `--use_claude_code`

O mesmo princípio aplica-se a `claude`, o CLI oficial do Claude Code, no modo `-p`: para
quem paga Claude Pro ou Max, a tradução é descontada da quota da
assinatura em vez de ser faturada por token. Não confundir com
`--use_claude`, a API da Anthropic, faturada por utilização.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Nenhuma via paga permanece aberta, e cada chamada comprova isso.** O Claude
  Code recebe do seu ambiente apenas uma lista fechada de variáveis — sem
  chave API, token, fornecedor cloud ou marcador da sessão Claude Code
  a partir da qual o aipmt seria iniciado. Antes do primeiro segmento, `claude auth status` deve
  mostrar a ligação à assinatura, sem chave Console, e `/usage`, que não consome
  quota, deve confirmá-la; cada chamada confirma-a por sua vez no seu
  evento de inicialização, caso contrário a resposta é recusada.
- **Desative o «extra usage»** (claude.ai, Definições → Utilização) para
  que o custo se mantenha em zero euros: quando ativado, assume o consumo após o esgotamento de uma janela e
  cobra sem apresentar erro. O aipmt interrompe a tradução assim que o relatório
  de quota de uma chamada o indica, mas essa chamada já foi contabilizada.
- **Quota partilhada com as suas sessões Claude Code.** Cada chamada informa
  a utilização das janelas de 5 horas e da semana; acima de 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`), não é iniciado mais nenhum segmento, para não
  esgotar o que é necessário para o seu trabalho.
- **Confinamento.** Cada chamada é executada sem ferramentas, num diretório privado e
  descartável, no modo sem personalização: nem os seus `CLAUDE.md`, nem os seus plugins,
  hooks, servidores MCP ou definições são carregados, e nada é guardado da
  sessão. Os anexos são desativados: um `@chemin` no seu documento
  permanece texto e não abre nenhum ficheiro (medido).
- **Modelos**: `sonnet` por predefinição, com o esforço `low`, e também em `--eco`:
  `--eco` não altera nada nesta via. Medido nos mesmos documentos, `haiku`
  é duas vezes mais lento — raciocina sem que seja possível impedi-lo — por
  um custo apenas ligeiramente inferior, e `opus` recusa conteúdos de biologia (ponto
  seguinte). Ambos continuam acessíveis através de `--model`; estes aliases acompanham o
  modelo mais recente da respetiva família. `fable` e as variantes `[1m]` são recusados,
  porque passam a consumir créditos pagos. `--reasoning_effort` define o esforço,
  do qual uma tradução não beneficia: o raciocínio medido é nulo ou quase.
- **O Opus recusa certos conteúdos de biologia.** As suas salvaguardas são mais
  rigorosas do que as do Sonnet, e a mensagem de erro da Anthropic avisa que elas
  «podem, por vezes, sinalizar trabalhos próximos da investigação em biologia». Medido: uma notícia breve de
  monitorização sobre 279 moléculas geradas levou à recusa do artigo nas catorze
  línguas. Nada é escrito: o aipmt recusa a resposta interrompida, identifica as
  salvaguardas e recomenda `--model sonnet`.
- Recusado em CI (`CI` ou `GITHUB_ACTIONS` definido) e em Windows (não medido).
- Variáveis: `AIPMT_CLAUDE_BIN` (caso contrário, o `PATH`, depois `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (segundos por segmento, predefinição 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (predefinição 0.8), `CLAUDE_CONFIG_DIR` (a conta do
  Claude Code, nunca obtida de um `.env` do projeto); diretórios de trabalho em
  `XDG_CACHE_HOME/aipmt/claude-code` (predefinição `~/.cache`).

**Condições de utilização: é a sua conta que está em jogo.** A
[página legal do Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
não impede «um utilizador final de iniciar sessão no binário não modificado do Claude Code
com a sua própria assinatura Claude»: é isso que o aipmt faz, ao iniciar o
binário oficial sem nunca ler o token. Mas a Anthropic «não permite
que programadores terceiros […] encaminhem pedidos através de credenciais dos planos Free, Pro ou Max
em nome dos seus utilizadores», prefere a chave API para ferramentas
de terceiros, «incluindo projetos open source», e reserva-se o direito de descontar a sua
utilização dos créditos pagos
([ajuda do Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Nenhum texto resolve o caso de uma ferramenta distribuída que inicia o binário.

**Dados**: nas contas Free, Pro e Max, o treino dos modelos
também se aplica ao Claude Code quando a definição de privacidade o permite
([página de dados](https://code.claude.com/docs/en/data-usage)). O aipmt não guarda
nenhuma transcrição local (`--no-session-persistence`). Não faça passar por ele
nada de confidencial.

### Para o fornecedor à sua escolha: `--use_opencode`

[OpenCode](https://opencode.ai) é um agente de código open source (MIT) que
encaminha pedidos para os fornecedores nele configurados: chave API, assinatura,
gateway OpenCode Zen (modelos gratuitos, sem conta) ou modelo local. Duas
vias foram medidas de ponta a ponta aqui, Zen e Ollama.

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
cujas conversas podem servir para treino, e essa escolha não é feita em
seu nome.

Confinamento em cada chamada:

- uma configuração inline, com prioridade sobre a sua, define um agente `aipmt`
  cujas ferramentas são todas recusadas (`permission: { "*": "deny" }`), com a partilha de
  sessão desativada, `--pure`, nunca `--auto`;
- diretório de trabalho descartável e vazio, com `OPENCODE_DISABLE_PROJECT_CONFIG` e
  `OPENCODE_DISABLE_CLAUDE_CODE` definidos — sem eles, o OpenCode injeta no
  prompt o `AGENTS.md` do diretório atual e `~/.claude/CLAUDE.md`. O
  `~/.config/opencode/AGENTS.md` global continua a ser injetado, o OpenCode não permite
  excluí-lo;
- contrato de saída: código de retorno 0, nenhum evento `error`, nenhuma chamada
  de ferramenta, último passo em `stop`, texto não vazio e o agente `aipmt`
  efetivamente carregado — um `--agent` desconhecido não faz o OpenCode falhar, ele
  recorre silenciosamente ao agente de programação;
- nenhuma chave de `aipmt` é transmitida, exceto `OPENCODE_API_KEY`, a chave
  do próprio OpenCode. Os fornecedores são configurados no OpenCode, não
  no `.env` de `aipmt`.

A saber:

- Os modelos gratuitos do Zen mudam, têm limites não documentados, e
  as suas conversas podem servir para treino: para documentação
  pública, não para conteúdo privado.
- Um modelo local deve oferecer pelo menos 16 k tokens de contexto, pois os segmentos
  podem ter até 16 000 caracteres. O Ollama configura frequentemente 4 096: usar
  um `Modelfile` com `PARAMETER num_ctx 32768`.
- `--eco` não tem efeito; `--reasoning_effort` é transmitido tal como está como
  `--variant` do OpenCode.
- O OpenCode regista cada sessão em `~/.local/share/opencode/`.
- Variáveis: `OPENCODE_BIN` (caso contrário, o `PATH`, depois `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (segundos por segmento, predefinição 600). `OPENCODE_CONFIG`
  é transmitido tal como está ao OpenCode.

Exemplo de um modelo local através do Ollama, em `~/.config/opencode/opencode.json`:

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

`reasoningEffort: "none"` desativa a reflexão que o Ollama ativa por predefinição nestes
modelos e que um Modelfile não consegue desativar. Medido numa frase de
seis palavras: 919 tokens de reflexão e 68 segundos sem a opção, 9 tokens com ela.

### Para mais de 400 modelos: `--use_openrouter`

O OpenRouter é um router faturado por utilização, com um crédito único, que dá acesso a
modelos alojados por terceiros — incluindo os modelos chineses abertos que nenhum
outro provider disponibiliza aqui.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` é obrigatório. Um preflight, executado antes de qualquer faturação, resolve
duas particularidades do encaminhamento:

- **Um mesmo modelo é servido por dezenas de fornecedores de alojamento com limites
  diferentes** — em `z-ai/glm-5.3-flash`, 23 fornecedores de alojamento, um dos quais limitado a
  2 048 tokens de saída. O preflight lê `/api/v1/models/{modèle}/endpoints`,
  exclui os fornecedores com menos de 8 000 tokens de saída ou com estado degradado e
  fixa os restantes com `allow_fallbacks: false`.
- **O raciocínio é faturado à tarifa de saída** — 107 tokens contra 2 numa
  resposta «OK» de `z-ai/glm-5.2`. É desativado por predefinição; os modelos
  que o impõem recebem o menor esforço que aceitam, pois a predefinição do
  catálogo pode esgotar a saída antes do fim da tradução.
  `--reasoning_effort` mantém a prioridade.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- A janela de contexto vem do catálogo. Um modelo com menos de 16 400 tokens é
  recusado antes de qualquer chamada: 8 400 para o prompt e o segmento, 8 000 de saída
  no mínimo.
- Um slug ausente do catálogo, um catálogo inacessível ou a ausência
  de um fornecedor de alojamento que cumpra o limite interrompem o comando.
- `finish_reason=length` com uma saída vazia significa um orçamento consumido pelo
  raciocínio, não um truncamento: a mensagem faz essa distinção.
- `--eco` não tem efeito.
- Variáveis: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (predefinição `https://openrouter.ai/api/v1`, `https://`
  obrigatório), `OPENROUTER_TIMEOUT` (predefinição 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (predefinição 30).

### Nota de tradução

`--add_translation_note` acrescenta uma nota, em `bottom` (predefinição), `top` (após o
front matter) ou `both` (`--note_position`), no formato `legacy` (parágrafo em
negrito, predefinição) ou `marker` (`--note_format`). O formato `marker` é uma
definição de referência Markdown invisível,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
seguida de uma citação em negrito: legível no GitHub, utilizável no build por um
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Medições detalhadas

Todas as medições são traduções realmente executadas com `aipmt`, para
catorze línguas: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Escritas** conta os ficheiros que as verificações deixaram passar; **Sem
diferenças**, aqueles em que `scripts/compare_structure.py` não deteta nada — o mesmo número de
secções, subtítulos, ligações, URLs distintos, blocos de código,
códigos inline, linhas de tabela, blocos de citação e palavras em negrito.

«Sem diferenças» significa «nada detetado», não «idêntico»: o comparador
conta elementos sem ler o seu conteúdo. Não assinala um título de
nível 4 eliminado, nem o texto de um código inline substituído, nem uma bandeira
trocada, nem uma ligação interna apresentada com um parêntese a mais,
`[texte]((#ancre))`, que já não leva a lado nenhum — e não avalia a
língua.

### Artigo de monitorização denso, modo `--news`

Uma edição da [monitorização de IA de jls42.org](https://jls42.org/fr/news):
589 linhas, 140 ligações, 21 secções, 3 citações em inglês protegidas. Campanha
de 4 e 5 de setembro de 2026.

| Modelo                                          | Acesso             | Escritas | Sem diferenças | Mediana/língua |
| ----------------------------------------------- | ------------------ | ------- | ------------ | -------------- |
| `gemini-3.7-flash`                              | API Google         | 14/14   | ✅ **14/14** | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | assinatura Google  | 14/14   | ✅ **14/14** | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | assinatura Google  | 14/14   | ✅ **14/14** | 3 min 14 s     |
| `claude-sonnet-5-5`                             | API Anthropic      | 14/14   | ✅ **14/14** | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | assinatura ChatGPT | 14/14   | ✅ **14/14** | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14   | ✅ **14/14** | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14   | ✅ **14/14** | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | assinatura Claude  | 14/14   | ⚠️ 13/14     | 6 min 49 s     |
| `claude-sonnet-5`                               | API Anthropic      | 14/14   | ⚠️ 11/14     | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | assinatura Claude  | 14/14   | ⚠️ 11/14     | 15 min 54 s    |
| `claude-haiku-5-5`                              | API Anthropic      | 14/14   | ⚠️ 11/14     | 2 min 54 s     |
| `claude-haiku-4-5`                              | API Anthropic      | 14/14   | ⚠️ 7/14      | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14   | ❌ 11/14     | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14   | ❌ 8/14      | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | local              | 10/14   | ❌ 7/14      | 12 min 39 s    |
| `mistral-large-latest`                          | API Mistral        | 11/14   | ❌ 5/14      | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14    | ❌ 3/14      | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | assinatura Grok    | 1/14    | ❌ 1/14      | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | assinatura Claude  | 0/14    | ❌ 0/14      | —              |

O Grok foi medido novamente em 9 de setembro noutra edição da mesma monitorização
(356 linhas): 9 línguas escritas em 14, 8 sem diferenças. É este o número que
figura na tabela inicial. Três campanhas interrompidas não estão
registadas: `qwen3.5-27b` (9 línguas) e `kimi-k2.6` (4) por falta de crédito,
`z-ai/glm-5.3-flash` cujas duas falhas resultavam de uma definição de raciocínio
que o provider entretanto corrigiu. As linhas OpenRouter foram medidas com as
definições predefinidas do router, antes de `--use_openrouter`; `z-ai/glm-5.2`,
medido novamente com o provider incluído, apresenta o mesmo 14/14. Os números foram
recalculados em 10 de setembro com o comparador atual: `qwen3.8-flash` e
`qwen3.7-flash` ganham uma língua cada em relação à primeira
publicação, os restantes mantêm-se.

As linhas `--use_antigravity` foram medidas em 26 de setembro no mesmo
artigo, com quatro traduções em paralelo: `gemini-3.7-flash-medium` de manhã,
`gemini-3.8-flash-medium` à tarde. Em inglês, cada um removeu por si próprio
as três linhas de tradução francesa sob as citações, sem inventar uma
bandeira, e as citações em inglês estão intactas: a limpeza de recurso não
teve nada a fazer. Em `--eco` (`gemini-3.7-flash-low`), apenas em quatro línguas
(en, ja, ar, hi): 4 escritas em 4, todas sem diferenças, mediana de 1 min 52 s.
Contraprova no mesmo dia numa edição mais recente da monitorização,
a de 25 de setembro (438 linhas, 2 citações em inglês), traduzida fora do
blog por `gemini-3.7-flash-medium`: 14 escritas em 14, todas sem diferenças, 87 a
128 s por língua.

As linhas `--use_claude_code` foram medidas em 26 de setembro no mesmo
artigo, com quatro traduções em paralelo, com o esforço `low`. Com `sonnet`, as
citações em inglês estão intactas nas catorze línguas e, em inglês, o
modelo removeu por si próprio as linhas de tradução francesa, sem inventar uma
bandeira. `opus` não escreveu nenhuma língua: em cada uma, as suas salvaguardas
interromperam a resposta no último segmento, devido a uma notícia breve sobre 279 moléculas
geradas para um local de ligação. Enviada isoladamente, essa notícia é recusada
na categoria «bio»; `sonnet` traduziu-a em todas as línguas. `haiku` escreve
as catorze línguas; em três (en, pl, ro), um título de secção passa do
nível 2 para o nível 1. Raciocina sem que seja possível impedi-lo — 61 % dos
seus tokens de saída —, daí demorar mais do dobro do tempo de `sonnet`.

As linhas `claude-sonnet-5-5`, `claude-haiku-5-5` e `claude-haiku-4-5` foram
medidas em 18 de outubro através da API da Anthropic, no mesmo artigo, com quatro
traduções em paralelo por modelo. O Sonnet 5.5 recusa que se desative a sua
reflexão: o aipmt envia-lhe a definição mais baixa que aceita, e as suas
respostas não apresentam nenhuma. Escreve as catorze línguas sem diferenças e sem
repetir um segmento; em inglês, removeu por si próprio as linhas de
tradução francesa, sem inventar uma bandeira, e as citações em inglês estão
intactas em todas as línguas. O Haiku 5.5 é medido com a sua reflexão adaptativa: com a reflexão
desativada, deixava parágrafos inteiros em francês, que a verificação recusa —
3 línguas escritas em 14. Os dois Haiku tropeçam na mesma notícia breve: o Haiku 5.5
altera o nível do título ou duplica-o em japonês, coreano e
chinês, o Haiku 4.5 passa-o para o nível 1 em sete línguas e deixa-o em
francês na tradução japonesa. O Haiku 4.5 custa 3,67 $ para os dois documentos nas
catorze línguas, o Haiku 5.5 0,57 $, o Sonnet 5.5 9,21 $.
### README deste projeto, Markdown padrão

Revisão fixada em 9 de setembro de 2026: 785 linhas, 285 códigos em linha, 40
delimitadores de fecho de blocos, 89 linhas de tabela. Quatro traduções em paralelo.

| Modelo                                          | Escritas | Sem desvios | Mediana/idioma | O que difere                                                           |
| ----------------------------------------------- | ------- | ---------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14   | ✅ 14/14   | 1 min 43 s     | nada                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14   | ✅ 14/14   | 1 min 48 s     | nada                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14   | ✅ 14/14   | 4 min 02 s     | nada para o comparador; links internos duplicados (en)                   |
| `claude-sonnet-5-5`                             | 14/14   | ✅ 14/14   | 1 min 18 s     | nada                                                                     |
| `claude-haiku-4-5`                              | 14/14   | ✅ 14/14   | 2 min 06 s     | nada                                                                     |
| `gemini-3.7-flash`                              | 14/14   | ⚠️ 13/14   | 36 s           | uma palavra em negrito (ja)                                                      |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14   | ⚠️ 13/14   | 1 min 22 s     | uma palavra em negrito (ko)                                                      |
| `sonnet` (`--use_claude_code`)                  | 14/14   | ⚠️ 13/14   | 2 min 20 s     | uma linha de tabela colada à anterior (ar)                         |
| `claude-sonnet-5`                               | 14/14   | ⚠️ 12/14   | 2 min 56 s     | um link (sv), uma palavra em negrito (zh)                                        |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14   | ⚠️ 12/14   | 6 min 46 s     | uma palavra em negrito (ar, ja)                                                  |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14   | ⚠️ 11/14   | 2 min 34 s     | uma palavra em negrito (hi, ja, ko)                                              |
| `qwen/qwen3.7-flash`                            | 14/14   | ⚠️ 10/14   | 2 min 17 s     | 40 códigos em linha adicionados em árabe; negrito (hi, ja, ko)                   |
| `claude-haiku-5-5`                              | 12/14   | ❌ 12/14   | 1 min 14 s     | 2 idiomas recusados (ar, hi): códigos em linha perdidos na resposta        |
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | uma secção perdida (ar, hi, ko); blocos de código adicionados (ja, ko, ro, zh) |

Duas campanhas interrompidas não foram avaliadas: Grok, cuja sessão CLI expirou
após doze idiomas (onze sem desvios), e `qwen3.8-flash`, com HTTP 429 do seu
provedor de alojamento após dois. `opencode/mimo-v2.5-free` e `ollama/gpt-oss-20b-32k`
não foram medidos novamente nesta revisão; na de 4 e 5 de setembro,
mais curta em 277 linhas, cada um produzia 9 traduções de 14, das quais 7
e 1 sem desvios.

As linhas `--use_antigravity` e `--use_claude_code` não foram medidas na
revisão fixada, mas em 26 de setembro na publicada com a 1.14.0 — e
as linhas `claude-sonnet-5-5`, `claude-haiku-5-5` e `claude-haiku-4-5` em 18 de
outubro, na mesma: 600 linhas, 257 códigos em linha, 30 delimitadores de fecho de blocos, 85
linhas de tabela. Sendo
mais curta em 185 linhas, não é diretamente comparável às outras linhas;
estas linhas, por sua vez, são comparáveis entre si. Quanto aos links internos, que o
comparador não verifica, `gemini-3.8-flash-medium` manteve-os intactos nos
catorze idiomas, `gemini-3.7-flash-medium` quebrou-os em italiano;
`sonnet` e `opus` mantiveram-nos intactos em todos, `haiku` duplicou-os em
inglês; `claude-sonnet-5-5` e `claude-haiku-4-5` mantiveram-nos intactos nos
catorze idiomas, `claude-haiku-5-5` nos doze em que produziu traduções.

### Quatro README de projetos conhecidos

FastAPI, Ollama, tldr-pages e Vue.js, obtidos tal como estão no GitHub — documentos
mais fáceis do que os dois anteriores. A campanha visava os modelos
com dificuldades; o Gemini serve aqui como ponto de comparação.

| Modelo                    | Âmbito                  | Escritas | Sem desvios   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 projetos × 14 idiomas     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 projetos × 14 idiomas     | 55/56   | ❌ 47/56     |
| `grok-4.6` (subscrição)   | 4 projetos × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 projetos × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### O que estas medições não são

- **Não são uma classificação exaustiva**: só o OpenRouter disponibiliza mais de quatrocentos
  modelos; foram medidos cerca de quinze.
- **Durações indicativas**: de três a seis traduções em paralelo consoante
  as campanhas, e a taxa de processamento de um fornecedor varia ao longo do dia.
- **Observações datadas**: os modelos mudam sob o mesmo nome, e os seus
  documentos não são os nossos.

Para repetir a medição nos seus documentos, numa cópia fixada do ficheiro:

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

Ferramentas de qualidade, opcionais mas recomendadas:

```bash
pipx install pre-commit               # hors venv — absent des requirements
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # mypy, SAST, pip-audit, tests avant chaque push
```

As 28 traduções do repositório (README e CHANGELOG, catorze idiomas) são
regeneradas com `./regen_translations.sh --force` — Codex e `gpt-6.1-sol` com
a subscrição ChatGPT por predefinição, quatro em paralelo. `REGEN_PROVIDER` e
`REGEN_MODEL` alteram o caminho: `antigravity` continua a usar uma subscrição, a
da Google, e é aceite sem exceção; uma API faturada (`openai`, `gemini`,
`grok`, `openrouter`) é recusada sem `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` limita a duração de cada job (600 s, 1 800 s no Codex e
Antigravity). Os detalhes das ferramentas estão em `CLAUDE.md`.

## Projetos que utilizam este script

- **[jls42.org](https://jls42.org)** — blogue pessoal publicado em 15 idiomas. O seu
  [acompanhamento diário de IA](https://jls42.org/fr/news) é traduzido todos os dias
  por esta ferramenta e serve de documento de referência para as medições acima.

## Autor

Julien LE SAUX
Email: contact@jls42.org

## Licença

GNU GENERAL PUBLIC LICENSE Version 3. Consulte [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Aviso

Este programa é distribuído **sem qualquer garantia**, nos termos das
secções 15 e 16 da GPL v3: fornecido «tal como está», sem garantia de qualidade
comercial nem de adequação a uma finalidade específica, e o seu autor não pode ser
responsabilizado por danos resultantes da sua utilização. O texto da
licença prevalece sobre este resumo.

- **Releia antes de publicar.** As proteções abrangem os blocos de código, o
  código em linha, os URL, as âncoras e as citações do modo `--news` — não abrangem os
  títulos, as tabelas, o front matter nem o sentido das suas frases.
- **Os seus documentos são enviados ao fornecedor escolhido**, ao abrigo dos seus termos
  de utilização e da sua política de dados. Alguns modelos gratuitos podem
  reutilizar as suas conversas para treino, e os termos do Antigravity
  permitem à Google reutilizá-las e submetê-las a revisão humana,
  mesmo com uma subscrição paga; um modelo local é a única opção que não faz
  sair quaisquer dados da sua máquina.
- **As chamadas de API são-lhe faturadas.** Este programa não limita a
  despesa: um documento longo, uma nova tentativa após uma falha ou um modelo que raciocina
  muito custam mais.
- **As medições publicadas são observações datadas**, não são garantias.

Os nomes de produtos e empresas mencionados pertencem aos respetivos
titulares. Este projeto não está afiliado a nenhum deles.

**Artigo traduzido do francês para o português com gpt-6.1-sol.**
