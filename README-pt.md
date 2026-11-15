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
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Distintivo Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Traduz ficheiros Markdown de uma língua para outra, preservando a
estrutura: blocos de código, código em linha, URL, âncoras, tabelas e front
matter. Onze formas de chamar um modelo — cinco API, quatro subscrições sem
faturação por utilização, dois routers — e uma medição publicada do que cada
modelo realmente preserva.

## Em poucas palavras

- **Onze vias de acesso a providers**: API OpenAI, Mistral, Claude, Gemini e Grok;
  subscrições ChatGPT (Codex), Grok, Google (Antigravity) e Claude (Claude
  Code) sem faturação por utilização; routers OpenCode (open source, gratuito ou local) e OpenRouter
  (mais de 400 modelos).
- **Sem erros causados por um token perdido**: blocos de código, código em linha,
  URL, âncoras e citações são substituídos por tokens antes da chamada e
  verificados no retorno. Se faltar algum, o ficheiro não é escrito.
- **Documentos longos**: segmentação de acordo com a janela do modelo.
- **Modo `--news`**: citações em inglês protegidas e opções geridas por
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
| 2   | `.env` do diretório atual (ou de um diretório superior) | uma chave específica de um projeto            |
| 3   | `~/.config/aipmt/.env`                        | instalado uma vez, válido em todo o lado       |

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
no Windows. Sem chave, o comando enumera os três locais.

**O `.env` de um projeto não pode redirecionar as chamadas nem escolher o programa
executado.** Fornece chaves, nunca um destino ou um binário: qualquer
variável em `_BASE_URL`, `_API_BASE`, `_ENDPOINT` ou `_BIN` (`CODEX_BIN`,
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
com `--include_model`, `document-es-gpt-5.6-terra.md`. A extensão passa
sempre a `.md` — `article.mdx` resulta em `article-en.md` — exceto com
`--keep_filename`, que mantém o nome original. Uma tradução já existente
é ignorada sem `--force`.

Códigos de saída: `0` se tudo tiver sido concluído ou ignorado, `1` se restar um ficheiro
com falha (lista na saída de erro), `2` se o problema estiver na configuração.
Um ficheiro com falha nunca é escrito, mesmo que a própria escrita falhe:
o conteúdo é escrito num ficheiro adjacente e depois renomeado. Basta executar novamente.

## Que modelo escolher

Medido com dois documentos reais, traduzidos para as mesmas catorze línguas por
cada modelo. **O número indica em quantas das catorze línguas a
tradução é escrita sem que nada difira da origem.**

| Modelo                | Como aceder                 | Artigo de acompanhamento denso | Este README    | O que difere e em quantas línguas                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | subscrição Google (Antigravity)   | ✅ 14/14                | ✅ 14/14     | nada, em nenhum dos dois documentos                                                                                                                                 |
| **Claude Sonnet 5.5** | chave API Anthropic                 | ✅ 14/14                | ✅ 14/14     | nada, em nenhum dos dois documentos                                                                                                                                 |
| **Gemini 3.7 Flash**  | chave API Google                    | ✅ 14/14                | ⚠️ 13/14     | 1 língua em 14: uma palavra a mais em negrito (ja)                                                                                                                      |
| **Gemini 3.7 Flash**  | subscrição Google (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 língua em 14: uma palavra a menos em negrito (ko)                                                                                                                     |
| **GPT-5.6 Sol**       | subscrição ChatGPT ou chave OpenAI | ✅ 14/14                | ⚠️ 12/14     | 2 línguas em 14: uma palavra a menos em negrito (ar, ja)                                                                                                                |
| **GLM-5.2**           | chave OpenRouter                    | ✅ 14/14                | ⚠️ 11/14     | 3 línguas em 14: uma palavra a menos em negrito (hi, ja, ko)                                                                                                            |
| Claude Sonnet 5       | subscrição Claude (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 1 língua em 14 no artigo: uma palavra a mais em negrito (zh); 1 neste README: uma linha de tabela colada à anterior, oculta na apresentação (ar)            |
| Claude Haiku 4.5      | subscrição Claude (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 3 línguas no artigo: um título de secção passou para o nível 1 (en, pl, ro); neste README, nada para o comparador, mas os links internos foram duplicados em inglês |
| Claude Sonnet 5       | chave API Anthropic                 | ⚠️ 11/14                | ⚠️ 12/14     | 3 línguas no artigo: surgiu um bloco de código (es, de, hi); 2 neste README: um link sem a sua marcação (sv), uma palavra em negrito (zh)                              |
| Claude Haiku 4.5      | chave API Anthropic                 | ⚠️ 7/14                 | ✅ 14/14     | 7 línguas no artigo: um título de secção passou para o nível 1 — em japonês, permaneceu em francês; nada neste README                                              |
| Claude Haiku 5.5      | chave API Anthropic                 | ⚠️ 11/14                | ❌ 12/14     | 3 línguas no artigo: um título de secção mudou de nível ou foi duplicado (ja, ko, zh); neste README, 2 línguas recusadas, códigos em linha perdidos (ar, hi)    |
| Qwen 3.7 Flash        | chave OpenRouter                    | ❌ 8/14                 | ⚠️ 10/14     | 1 língua recusada no artigo, 5 outras apresentam diferenças; neste README, cerca de quarenta palavras colocadas em `code` (ar)                                                    |
| Grok 4.6              | subscrição Grok                   | ❌ 8/14                 | sem avaliação     | 5 línguas recusadas em 14, por falta de códigos em linha e de URL devolvidos; o neerlandês diverge em tudo                                                               |
| GPT-OSS 20B           | modelo local (Ollama)             | ❌ 7/14                 | sem nova medição | 4 línguas recusadas em 14: o modelo deixava passagens em francês, a verificação de proteção bloqueou-as                                                                  |
| MiMo v2.5 (gratuito)   | OpenCode Zen, sem conta         | ❌ 11/14                | sem nova medição | 1 língua recusada; uma secção perdida em polaco                                                                                                                  |
| Mistral Large         | chave API Mistral                   | ❌ 5/14                 | ❌ 1/14      | **uma secção inteira desaparece**: 1 língua no artigo (hi), 3 neste README (ar, hi, ko) — e 3 línguas recusadas no artigo                                |
| DeepSeek V4 Flash     | chave OpenRouter                    | ❌ 3/14                 | sem nova medição | 10 línguas recusadas em 14; 37 minutos por língua                                                                                                                 |
| Claude Opus 5.5       | subscrição Claude (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | o artigo foi recusado nas 14 línguas pelas salvaguardas do Opus, devido a uma breve notícia de biologia; nada neste README                                               |

|     | O que significa o símbolo                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | as catorze línguas traduzidas, sem que nada difira da origem                                                                                                                                       |
| ⚠️  | as catorze línguas traduzidas; o que difere é a **marcação** — uma palavra em negrito, um `code`, um link que perde os parênteses retos. Não falta nenhum texto, URL, bloco de código ou secção |
| ❌  | pelo menos uma língua não pôde ser traduzida — o ficheiro é recusado, não é escrito — **ou** falta conteúdo num ficheiro escrito                                                                      |

O que se deve reter:

- **Uma tradução recusada não é uma tradução danificada.** Quando falta um token
  no retorno, o ficheiro não é escrito e a língua conta como
  recusada. É o que acontece com o Grok no artigo: quatro códigos em linha e
  três URL perdidos logo no primeiro segmento, nos cinco sistemas de escrita não latinos.
- **Um modelo pode recusar um documento inteiro por causa de uma única frase.** O Opus 5.5
  traduz este README sem qualquer diferença, mas nenhum artigo de acompanhamento: as suas
  salvaguardas interrompem a resposta numa breve notícia de biologia. O ficheiro não
  é escrito, e o aipmt explica porquê.
- **Esta proteção não abrange títulos, tabelas, front matter nem
  texto.** Um modelo que elimina uma secção devolve um ficheiro que a ferramenta escreve
  sem protestar — é o caso do Mistral. Estes elementos não podem ser
  substituídos por um token, e as verificações atuais não os controlam;
  `scripts/compare_structure.py` deteta uma secção perdida, mas só depois.
- **O Grok não tem avaliação neste README**: a sua sessão CLI expirou após doze
  línguas, das quais onze sem diferenças. Uma campanha interrompida não recebe avaliação.
- **A densidade do documento conta mais do que a língua.** O Grok dá conta de
  README comuns e falha num artigo carregado de links, incluindo em
  neerlandês.

Datas e documentos: a coluna «Este README» foi medida em 9 de setembro de 2026
numa revisão fixa deste ficheiro (785 linhas, 285 códigos em linha, 89 linhas
de tabela), entretanto alterada — exceto as linhas Antigravity e Claude Code,
medidas em 26 de setembro na revisão publicada com a 1.14.0, mais curta
(600 linhas, 257 códigos em linha, 85 linhas de tabela), e as linhas Claude
Sonnet 5.5, Haiku 5.5 e Haiku 4.5 pela API, medidas em 18 de outubro na
mesma revisão. A coluna «Artigo de acompanhamento denso» vem da campanha de
4 e 5 de setembro, com um artigo de 589 linhas, exceto a linha Grok, medida novamente em
9 de setembro noutra edição do mesmo acompanhamento, as linhas Antigravity e
Claude Code, medidas em 26 de setembro com o mesmo artigo, e estas três linhas
Claude, em 18 de outubro. As tabelas completas, os tempos e o protocolo estão
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
| `--use_opencode`         | Utilizar OpenCode (open source) com o fornecedor configurado no OpenCode; exige `--model provider/modèle` |
| `--use_openrouter`       | Utilizar OpenRouter — requer `OPENROUTER_API_KEY` e `--model fournisseur/modèle`                          |
| `--force`                | Forçar a retradução                                                                                       |
| `--keep_filename`        | Manter o nome original do ficheiro                                                                          |
| `--news`                 | Modo de notícias: protege as citações em EN, gere as bandeiras por idioma                                      |
| `--add_translation_note` | Adicionar uma nota de tradução                                                                                |
| `--note_position`        | Posição da nota: `top`, `bottom` (predefinição) ou `both`                                                     |
| `--note_format`          | Formato da nota: `legacy` (predefinição, parágrafo em negrito) ou `marker`                                            |
| `--include_model`        | Incluir o nome do modelo no ficheiro de saída                                                            |
| `--reasoning_effort`     | Esforço de raciocínio GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

Os nove flags `--use_*` são mutuamente exclusivos: combinar dois é
recusado.

## Fornecedores

### Por API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` muda para o nível económico de cada fornecedor.

| Fornecedor    | Qualidade (predefinição)                                                     | Económico (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.8-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (também `gpt-5.6-sol`, `terra` e `luna` através de `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | igual — `--eco` sem efeito |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, esforço `low`                                               | igual — `--eco` sem efeito |
| OpenCode    | `--model provider/modèle` obrigatório                                | igual — `--eco` sem efeito |
| OpenRouter  | `--model fournisseur/modèle` obrigatório                             | igual — `--eco` sem efeito |

Gemini 3.7 Flash, a predefinição até à 1.17.1, está obsoleto: a Google disponibiliza
Gemini 3.8 Flash no seu lugar, e `--model gemini-3.7-flash` continua a ser aceite.
Uma falha temporária da API Gemini (503, 429, tempo limite excedido) repete
a chamada até três vezes, após 10, 20 e depois 40 segundos. Uma tentativa
sem resposta é abandonada ao fim de 5 minutos e depois repetida da
mesma forma: um servidor sem resposta faz o segmento falhar em cerca de vinte minutos
no máximo, em vez de bloquear indefinidamente.

### Com a subscrição ChatGPT: `--use_codex`

Controla o CLI Codex oficial: a tradução é descontada da quota da
subscrição ChatGPT, sem chave API nem faturação por utilização.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- O binário é procurado em `CODEX_BIN`, depois no `PATH` e depois no package
  `openai-codex-cli-bin`. `~/.codex/auth.json` nunca é lido.
- `OPENAI_API_KEY` e `CODEX_API_KEY` são removidas do ambiente do
  subprocesso: uma chave presente nunca provoca a mudança para a API.
- Cada segmento custa pelo menos uma «mensagem» da janela de 5 horas — duas
  se a validação falhar e houver uma nova tentativa. A OpenAI anuncia, como
  estimativa, 250-2 000 mensagens/5 h para `gpt-5.6-luna` (`--eco`) e
  10-100 para `gpt-5.6-sol` num plano Plus.
- `--model gpt-5.6-sol`, a predefinição até à 1.16.3, `--model gpt-5.6-terra`
  e `--model gpt-5.6-luna` também utilizam a subscrição.
- Um 429 do servidor não faz perder o ficheiro: o Codex volta a ligar-se sozinho,
  o aipmt aguarda o fim do turno e, se o 429 persistir, o segmento
  é repetido após 30 e depois 60 segundos. Um modelo ao qual a conta não tem acesso devolve um 400 «o modelo
  não é suportado ao utilizar o Codex com uma conta ChatGPT».
- Mais lento do que uma API, e a diferença aumenta com o documento: neste README,
  6 min 46 s por idioma em mediana com `gpt-5.6-sol`, contra 36 s para
  `gemini-3.7-flash`.
- Recusado em CI (`CI` ou `GITHUB_ACTIONS` definido): a subscrição autentica-se
  através de um ficheiro de sessão pessoal, que não deve estar num runner
  partilhado.
- Variáveis: `CODEX_BIN`, `CODEX_TIMEOUT` (segundos por segmento, predefinição 600).

### Com a subscrição Grok: `--use_grok_cli`

O mesmo princípio com o CLI oficial Grok Build, com a subscrição SuperGrok ou
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Isolamento mais fraco do que o Codex.** O sandbox do SO do Grok não se aplica
  em muitos computadores Linux recentes (AppArmor, sockets do runtime
  de contentores), e um perfil que não pode ser aplicado arranca sem isolamento,
  silenciosamente. Por isso, o script não pede nenhum perfil por predefinição, informa disso e
  apoia-se nas regras `--deny` do CLI, incluindo o catch-all `*` — a única
  camada que se recusa a arrancar em vez de retirar a proteção sem o
  dizer. `GROK_TRANSLATE_SANDBOX=read-only` exige o sandbox do SO, e o arranque
  falha se a máquina não o conseguir aplicar.
- A quota é semanal, partilhada com Chat, Imagine e Voice, e nenhum
  comando permite consultá-la: um lote pode consumir a quota de utilização de conversação
  sem aviso.
- Variáveis: `GROK_BIN`, `GROK_HOME` (diretório do CLI, predefinição `~/.grok`),
  `GROK_TIMEOUT` (predefinição 900), `GROK_TRANSLATE_SANDBOX`.

### Com a subscrição Google: `--use_antigravity`

O mesmo princípio com `agy`, o CLI oficial do Antigravity: para quem paga Google
AI Pro ou Ultra, a tradução é descontada da quota da subscrição em vez
de ser faturada por token. É a única via para essa quota: o Gemini CLI já não
serve estas contas desde 18 de junho de 2026
([anúncio](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
e o SDK do Antigravity só aceita uma chave API ou um projeto Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Nenhuma via paga fica aberta.** O agy recebe do seu
  ambiente apenas uma lista fechada de variáveis — `PATH`, idioma e fuso horário,
  terminal, identidade, proxies e certificados, bus de sessão — e nenhuma chave:
  várias das suas variáveis redirecionam uma chamada sem mostrar nada (verificado:
  uma envia o documento para um gateway de terceiros, outra para um projeto
  Google Cloud faturado), e uma lista de bloqueio deixava escapar algumas em cada revisão.
  Antes de qualquer segmento, `agy -p /config`, que não consome quota, tem de mostrar
  os créditos de IA pagos desativados, sem chave API nem projeto Google Cloud — uma
  definição ausente implica recusa —, caso contrário nada é traduzido; o registo de cada
  chamada tem depois de comprovar a subscrição (`authMethod=consumer`), caso contrário a
  resposta é recusada.
- **Isolamento.** Cada chamada é executada num diretório pessoal privado e
  descartável, com um agente de tradução sem ferramentas: as suas definições, regras,
  plugins, servidores MCP e hooks do agy não entram nele, nada é acrescentado ao seu
  histórico, e a autenticação permanece no porta-chaves, que o aipmt nunca lê.
  Um agente não encontrado faz o agy recorrer, silenciosamente, ao seu agente de programação
  e às respetivas ferramentas: uma linha inteira do registo tem de confirmar o agente correto — um
  documento que cite essa mensagem não a substitui —, caso contrário há recusa.
- **Plataformas**: Linux, numa sessão com porta-chaves (bus de sessão
  D-Bus, Secret Service); o macOS é aceite, embora não tenha sido avaliado. Recusado
  no Windows, onde o agy não lê as variáveis que isolam cada chamada, e
  no Linux sem bus de sessão — sessão SSH, contentor, servidor: aí o agy
  guarda o seu token num ficheiro de `~/.gemini`, que o isolamento oculta. A
  recusa ocorre antes de qualquer execução, com a respetiva causa, em vez de um minuto
  de espera por um código de autenticação.
- **Modelos**: os de `agy models`. Os Gemini incluem o esforço no nome
  (`gemini-3.8-flash-medium`…): um nome sem sufixo é recusado antes da chamada,
  e `--reasoning_effort` não tem efeito. Por predefinição `gemini-3.8-flash-medium`,
  e `gemini-3.7-flash-low` com `--eco`; as campanhas que os determinaram estão
  descritas em [Medições detalhadas](#medições-detalhadas). Claude e GPT-OSS
  têm a sua própria quota, muito mais pequena: cerca de 1 % da janela de
  5 horas por chamada medida, contra 0,05 % em Flash.
- **Quota**: por grupo, uma janela de 5 horas e uma semanal, em
  proporção ao custo em tokens. Medido na conta do autor: cerca de
  16 pontos da janela de 5 horas por milhão de caracteres de origem com
  `gemini-3.8-flash-medium`, 14 com `gemini-3.7-flash-medium` e 7 a 8 com
  esforço baixo — um README de 40 000 caracteres custa, portanto, um pouco mais de
  meio ponto. O limite semanal, por sua vez, depende do nível. A repetição segue
  o que o agy declara passível de nova tentativa; caso contrário, uma janela esgotada nunca
  é repetida: faz falhar cada ficheiro até à reposição
  apresentada por `/usage`.
- **Mais lento do que a API**: no artigo denso das medições, 3 min 59 s por
  idioma em mediana com `gemini-3.8-flash-medium` e 3 min 14 s com
  `gemini-3.7-flash-medium`, contra 1 min 18 s para Gemini 3.7 Flash pela API.
- **Interrupção**: Ctrl-C, ou o fecho do terminal, param o agy juntamente com o
  comando, em vez de o deixarem terminar o turno consumindo a sua quota; o mesmo acontece com
  Codex, Grok CLI e OpenCode. Com `nohup`, a tradução continua.
- Recusado em CI (`CI` ou `GITHUB_ACTIONS` definido): a autenticação reside num
  porta-chaves pessoal. Num runner, `--use_gemini` com `GOOGLE_API_KEY`.
- Variáveis: `AGY_BIN` (caso contrário, o `PATH`, depois `~/.local/bin/agy`),
  `AGY_TIMEOUT` (segundos por segmento, incluindo o arranque, predefinição 900).

**Termos de utilização: é a sua conta que está em causa.** Os
[termos do Antigravity](https://antigravity.google/terms) (secção 6) e a sua
[FAQ](https://antigravity.google/docs/faq/) proíbem o acesso ao serviço
através de software de terceiros utilizando a autenticação do Antigravity — Claude Code,
OpenClaw e OpenCode são aí citados —, sob pena de suspensão da conta. O aipmt
não lê nem reutiliza o token: executa o binário oficial no
[modo headless](https://antigravity.google/docs/cli/headless/) que a Google
documenta para scripts e CI. Um membro da Google considerou «normal»
executar `agy -p` a partir de um script local para o seu próprio trabalho
([fórum oficial, 25 de setembro de 2026, resposta não contratual](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
nenhum texto esclarece o caso de uma ferramenta distribuída como esta.

**Apenas documentos públicos.** Segundo a secção 5 dos mesmos termos, as
interações — prompts, respostas, metadados — podem ser utilizadas para melhorar os
produtos e a aprendizagem automática da Google e ser revistas por
humanos, mesmo com uma subscrição paga. A exclusão passa pela definição
`enableTelemetry`, cujo efeito não está documentado e que o aipmt não configura; as suas definições
do agy não são transferidas para o ambiente isolado. Não envie por esta via nada de confidencial.
### Com a assinatura Claude: `--use_claude_code`

O mesmo princípio com `claude`, o CLI oficial do Claude Code, no modo `-p`: para
quem paga pelo Claude Pro ou Max, a tradução é descontada da quota da
assinatura em vez de ser cobrada por token. Não confundir com
`--use_claude`, a API da Anthropic, cobrada conforme o uso.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Nenhuma via paga fica aberta, e cada chamada comprova isso.** O Claude
  Code recebe do seu ambiente apenas uma lista fechada de variáveis — nenhuma
  chave API, nenhum token, nenhum provedor cloud, nem marcador da sessão Claude Code
  a partir da qual o aipmt seria iniciado. Antes do primeiro segmento, `claude auth status` deve
  mostrar a conexão pela assinatura, sem chave Console, e `/usage`, que não consome
  quota, deve confirmar isso; cada chamada também confirma isso no seu
  evento de inicialização, caso contrário a resposta é recusada.
- **Desative o «extra usage»** (claude.ai, Configurações → Uso) para
  manter o custo em zero euros: quando ativado, ele assume quando uma janela se esgota e
  cobra sem apresentar erro. O aipmt interrompe a tradução assim que o relatório
  de quota de uma chamada indica isso, mas essa chamada já foi contabilizada.
- **Quota compartilhada com as suas sessões Claude Code.** Cada chamada informa
  o uso das janelas de 5 horas e da semana; acima de 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`), nenhum novo segmento é iniciado, para não
  esgotar o que serve ao seu trabalho.
- **Isolamento.** Cada chamada é executada sem ferramentas, num diretório privado e
  descartável, no modo sem personalização: nem os seus `CLAUDE.md`, nem os seus plugins,
  hooks, servidores MCP ou configurações são carregados, e nada da
  sessão é guardado. Os anexos são desativados: um `@chemin` no seu documento
  continua sendo texto e não abre nenhum arquivo (verificado).
- **Modelos**: `sonnet` por padrão, com esforço `low`, e em `--eco` também:
  `--eco` não altera nada nesta via. Medidos nos mesmos documentos, `haiku`
  é duas vezes mais lento — raciocina sem que seja possível impedi-lo — por
  um custo apenas ligeiramente inferior, e `opus` recusa conteúdos de biologia (ponto
  seguinte). Ambos continuam acessíveis por `--model`; esses aliases seguem o
  modelo mais recente da respectiva família. `fable` e as variantes `[1m]` são recusados,
  porque usam créditos pagos. `--reasoning_effort` ajusta o esforço,
  do qual uma tradução não tira proveito: o raciocínio medido é nulo ou quase.
- **O Opus recusa certos conteúdos de biologia.** As suas salvaguardas são mais
  rigorosas que as do Sonnet, e a mensagem de erro da Anthropic avisa que elas
  «às vezes podem sinalizar trabalhos relacionados à pesquisa em biologia». Verificado: uma nota de
  monitoramento sobre 279 moléculas geradas fez com que o artigo fosse recusado nos quatorze
  idiomas. Nada é gravado: o aipmt recusa a resposta interrompida, identifica as
  salvaguardas e recomenda `--model sonnet`.
- Recusado em CI (`CI` ou `GITHUB_ACTIONS` definido) e no Windows (não testado).
- Variáveis: `AIPMT_CLAUDE_BIN` (caso contrário, o `PATH`, depois `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (segundos por segmento, padrão 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (padrão 0.8), `CLAUDE_CONFIG_DIR` (a conta do
  Claude Code, nunca obtida de um `.env` de projeto); diretórios de trabalho em
  `XDG_CACHE_HOME/aipmt/claude-code` (padrão `~/.cache`).

**Termos de uso: é a sua conta que está em jogo.** A
[página jurídica do Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
não impede «um usuário final de iniciar sessão no binário não modificado do Claude Code
com a sua própria assinatura Claude»: é isso que o aipmt faz, ao iniciar o
binário oficial sem nunca ler o token. Mas a Anthropic «não permite
que desenvolvedores terceiros […] encaminhem solicitações por meio das credenciais
dos planos Free, Pro ou Max em nome dos seus usuários», prefere a chave API para ferramentas
de terceiros, «incluindo projetos open source», e reserva-se o direito de descontar o
uso delas dos créditos pagos
([ajuda do Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Nenhum texto resolve o caso de uma ferramenta distribuída que inicia o binário.

**Dados**: nas contas Free, Pro e Max, o treinamento dos modelos
também se aplica ao Claude Code quando a configuração de privacidade o permite
([página sobre dados](https://code.claude.com/docs/en/data-usage)). O aipmt não guarda
nenhuma transcrição local (`--no-session-persistence`). Não envie por ele
nada confidencial.

### Para o provedor de sua escolha: `--use_opencode`

[OpenCode](https://opencode.ai) é um agente de código open source (MIT) que
encaminha solicitações para os provedores configurados nele: chave API, assinatura,
gateway OpenCode Zen (modelos gratuitos, sem conta) ou modelo local. Duas
vias foram testadas de ponta a ponta aqui, Zen e Ollama.

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
cujas conversas podem servir para treinamento, e essa escolha não é feita
por você.

Isolamento em cada chamada:

- uma configuração inline, com prioridade sobre a sua, define um agente `aipmt`
  com todas as ferramentas bloqueadas (`permission: { "*": "deny" }`), compartilhamento de
  sessão desativado, `--pure`, nunca `--auto`;
- diretório de trabalho descartável e vazio, `OPENCODE_DISABLE_PROJECT_CONFIG` e
  `OPENCODE_DISABLE_CLAUDE_CODE` definidos — sem eles, o OpenCode injeta no
  prompt o `AGENTS.md` do diretório atual e `~/.claude/CLAUDE.md`. O
  `~/.config/opencode/AGENTS.md` global continua sendo injetado, o OpenCode não permite
  excluí-lo;
- contrato de saída: código de retorno 0, nenhum evento `error`, nenhuma chamada
  de ferramenta, último passo em `stop`, texto não vazio e o agente `aipmt`
  efetivamente carregado — um `--agent` desconhecido não faz o OpenCode falhar, ele
  recorre silenciosamente ao agente de programação;
- nenhuma chave de `aipmt` é transmitida, exceto `OPENCODE_API_KEY`, a chave
  do próprio OpenCode. Os provedores são configurados no OpenCode, não no
  `.env` de `aipmt`.

Convém saber:

- Os modelos gratuitos do Zen mudam, têm limites não documentados e
  as suas conversas podem servir para treinamento: para documentação
  pública, não para conteúdo privado.
- Um modelo local deve oferecer pelo menos 16 k tokens de contexto, pois os segmentos
  chegam a 16 000 caracteres. O Ollama costuma configurar 4 096: use
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

`reasoningEffort: "none"` desativa a reflexão que o Ollama ativa por padrão nesses
modelos e que um Modelfile não consegue desativar. Medido numa frase de
seis palavras: 919 tokens de reflexão e 68 segundos sem a opção, 9 tokens com ela.

### Para mais de 400 modelos: `--use_openrouter`

O OpenRouter é um roteador cobrado conforme o uso, com um saldo único de créditos, para
modelos hospedados por terceiros — incluindo os modelos chineses abertos que nenhum
outro provider disponibiliza aqui.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` é obrigatório. Um preflight, executado antes de qualquer cobrança, resolve
duas particularidades do roteamento:

- **Um mesmo modelo é servido por dezenas de provedores de hospedagem com limites
  diferentes** — no `z-ai/glm-5.3-flash`, 23 provedores, um deles limitado a
  2 048 tokens de saída. O preflight lê `/api/v1/models/{modèle}/endpoints`,
  exclui os provedores com menos de 8 000 tokens de saída ou com estado degradado e
  fixa os demais com `allow_fallbacks: false`.
- **O raciocínio é cobrado à tarifa de saída** — 107 tokens contra 2 numa
  resposta «OK» de `z-ai/glm-5.2`. Ele é desativado por padrão; os modelos
  que o impõem recebem o menor esforço que aceitam, pois o padrão do
  catálogo pode esgotar a saída antes do fim da tradução.
  `--reasoning_effort` continua tendo prioridade.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- A janela de contexto vem do catálogo. Um modelo com menos de 16 400 tokens é
  recusado antes de qualquer chamada: 8 400 para o prompt e o segmento, 8 000 de saída
  no mínimo.
- Um slug ausente do catálogo, um catálogo inacessível ou a ausência
  de um provedor de hospedagem que cumpra o limite interrompem o comando.
- `finish_reason=length` com uma saída vazia indica um orçamento consumido pelo
  raciocínio, não um truncamento: a mensagem distingue os casos.
- `--eco` não tem efeito.
- Variáveis: `OPENROUTER_API_KEY` (<https://openrouter.ai/keys>),
  `OPENROUTER_BASE_URL` (padrão `https://openrouter.ai/api/v1`, `https://`
  obrigatório), `OPENROUTER_TIMEOUT` (padrão 900), `OPENROUTER_PREFLIGHT_TIMEOUT`
  (padrão 30).

### Nota de tradução

`--add_translation_note` adiciona uma nota, em `bottom` (padrão), `top` (após o
front matter) ou `both` (`--note_position`), no formato `legacy` (parágrafo em
negrito, padrão) ou `marker` (`--note_format`). O formato `marker` é uma
definição de referência Markdown invisível,
`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`,
seguida de uma citação em negrito: legível no GitHub, utilizável no build por um
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Medições detalhadas

Todas as medições são traduções realmente executadas com `aipmt`, para
quatorze idiomas: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Gravados** conta os arquivos que as verificações de proteção deixaram passar; **Sem
divergências**, aqueles em que `scripts/compare_structure.py` não aponta nada — mesmo número de
seções, subtítulos, links, URLs distintas, blocos de código,
códigos inline, linhas de tabela, blocos de citação e palavras em negrito.

«Sem divergências» significa «nada detectado», não «idêntico»: o comparador
conta elementos sem ler o conteúdo. Não sinaliza um título de
nível 4 removido, nem o texto de um código inline substituído, nem uma bandeira
trocada, nem um link interno apresentado com um parêntese a mais,
`[texte]((#ancre))`, que já não leva a lugar nenhum — e não avalia o
idioma.

### Artigo denso de monitoramento, modo `--news`

Uma edição do [monitoramento de IA de jls42.org](https://jls42.org/fr/news):
589 linhas, 140 links, 21 seções, 3 citações em inglês protegidas. Campanha
de 4 e 5 de setembro de 2026.

| Modelo                                          | Acesso             | Gravados | Sem divergências | Mediana/idioma |
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

O Grok foi medido novamente em 9 de setembro com outra edição do mesmo monitoramento
(356 linhas): 9 idiomas gravados em 14, 8 sem divergências. É esse número que
consta na tabela inicial. Três campanhas interrompidas não foram
registradas: `qwen3.5-27b` (9 idiomas) e `kimi-k2.6` (4) por falta de crédito,
`z-ai/glm-5.3-flash` cujas duas falhas vinham de uma configuração de raciocínio
que o provider passou a corrigir desde então. As linhas OpenRouter foram medidas com as
configurações padrão do roteador, antes de `--use_openrouter`; `z-ai/glm-5.2`,
medido novamente com o provider fornecido, apresenta os mesmos 14/14. Os números foram
recalculados em 10 de setembro com o comparador atual: `qwen3.8-flash` e
`qwen3.7-flash` ganham um idioma cada em relação à primeira
publicação, os demais permanecem inalterados.

As linhas `--use_antigravity` foram medidas em 26 de setembro com o mesmo
artigo, quatro traduções em paralelo: `gemini-3.7-flash-medium` de manhã,
`gemini-3.8-flash-medium` à tarde. Em inglês, cada um removeu por conta própria
as três linhas de tradução francesa sob as citações, sem inventar
bandeira, e as citações em inglês estão intactas: a limpeza de contingência não
precisou fazer nada. Em `--eco` (`gemini-3.7-flash-low`), em apenas quatro idiomas
(en, ja, ar, hi): 4 gravados em 4, todos sem divergências, 1 min 52 s de
mediana. Contraprova no mesmo dia com uma edição mais recente do monitoramento,
a de 25 de setembro (438 linhas, 2 citações em inglês), traduzida fora do
blog por `gemini-3.7-flash-medium`: 14 gravados em 14, todos sem divergências, 87 a
128 s por idioma.

As linhas `--use_claude_code` foram medidas em 26 de setembro com o mesmo
artigo, quatro traduções em paralelo, com esforço `low`. Com `sonnet`, as
citações em inglês estão intactas nos quatorze idiomas e, em inglês, o
modelo removeu por conta própria as linhas de tradução francesa, sem inventar
bandeira. `opus` não gravou nenhum idioma: em cada um, as suas salvaguardas
interromperam a resposta no último segmento, por causa de uma nota sobre 279 moléculas
geradas para um sítio de ligação. Enviada isoladamente, essa nota é recusada
na categoria «bio»; `sonnet` traduziu-a em todos os idiomas. `haiku` grava
os quatorze idiomas; em três (en, pl, ro), um título de seção passa do
nível 2 para o nível 1. Ele raciocina sem que seja possível impedi-lo — 61 % dos
seus tokens de saída —, daí levar mais do dobro do tempo de `sonnet`.

As linhas `claude-sonnet-5-5`, `claude-haiku-5-5` e `claude-haiku-4-5` foram
medidas em 18 de outubro pela API da Anthropic, com o mesmo artigo, quatro
traduções em paralelo por modelo. O Sonnet 5.5 recusa a desativação da sua
reflexão: o aipmt envia-lhe a configuração mais baixa que ele aceita, e as suas
respostas não apresentam nenhuma. Ele grava os quatorze idiomas sem divergências e sem
reprocessar nenhum segmento; em inglês, removeu por conta própria as linhas de
tradução francesa, sem inventar bandeira, e as citações em inglês estão
intactas em todos os idiomas. O Haiku 5.5 é medido com a sua reflexão adaptativa: com a reflexão
desativada, deixava parágrafos inteiros em francês, que a verificação de proteção recusa —
3 idiomas gravados em 14. Os dois Haiku esbarram na mesma nota: o Haiku 5.5
altera o nível do título dela ou duplica-o em japonês, coreano e
chinês, o Haiku 4.5 passa-o para o nível 1 em sete idiomas e deixa-o em
francês na tradução japonesa. O Haiku 4.5 custa 3,67 $ para os dois documentos nos
quatorze idiomas, o Haiku 5.5 0,57 $, o Sonnet 5.5 9,21 $.
### README deste projeto, Markdown padrão

Revisão fixada em 9 de setembro de 2026: 785 linhas, 285 códigos em linha, 40
fechamentos de blocos, 89 linhas de tabela. Quatro traduções em paralelo.

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
| `mistral-large-latest`                          | 14/14   | ❌ 1/14    | 2 min 44 s     | uma seção perdida (ar, hi, ko); blocos de código adicionados (ja, ko, ro, zh) |

Duas campanhas interrompidas não foram avaliadas: Grok, sessão CLI expirada
após doze idiomas (onze sem desvios), e `qwen3.8-flash`, HTTP 429 do seu
provedor de hospedagem após dois. `opencode/mimo-v2.5-free` e `ollama/gpt-oss-20b-32k`
não foram medidos novamente nesta revisão; na de 4 e 5 de setembro,
277 linhas mais curta, cada um produzia 9 traduções de 14, das quais 7
e 1 sem desvios.

As linhas `--use_antigravity` e `--use_claude_code` não foram medidas na
revisão fixada, mas em 26 de setembro na publicada com a 1.14.0 — e
as linhas `claude-sonnet-5-5`, `claude-haiku-5-5` e `claude-haiku-4-5` em 18 de
outubro, na mesma: 600 linhas, 257 códigos em linha, 30 fechamentos de blocos, 85
linhas de tabela. Por ser
185 linhas mais curta, ela não pode ser comparada ponto a ponto com as outras linhas;
essas linhas, por sua vez, podem ser comparadas entre si. Quanto aos links internos, que o
comparador não verifica, `gemini-3.8-flash-medium` os manteve intactos nos
quatorze idiomas, `gemini-3.7-flash-medium` os quebrou em italiano;
`sonnet` e `opus` os mantiveram intactos em todos, `haiku` os duplicou em
inglês; `claude-sonnet-5-5` e `claude-haiku-4-5` os mantiveram intactos nos
quatorze idiomas, `claude-haiku-5-5` nos doze em que produziu traduções.

### Quatro README de projetos conhecidos

FastAPI, Ollama, tldr-pages e Vue.js, obtidos sem alterações do GitHub — documentos
mais fáceis que os dois anteriores. A campanha visava os modelos
com dificuldades; Gemini serve de ponto de comparação.

| Modelo                    | Escopo                  | Escritas | Sem desvios   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 projetos × 14 idiomas     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 projetos × 14 idiomas     | 55/56   | ❌ 47/56     |
| `grok-4.6` (assinatura)   | 4 projetos × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 projetos × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### O que estas medições não são

- **Não são uma classificação exaustiva**: só o OpenRouter oferece mais de quatrocentos
  modelos, cerca de quinze foram medidos.
- **Durações indicativas**: de três a seis traduções em paralelo conforme
  as campanhas, e a taxa de processamento de um fornecedor varia ao longo do dia.
- **Observações datadas**: os modelos mudam mantendo o mesmo nome, e os seus
  documentos não são os nossos.

Para repetir a medição nos seus documentos, numa cópia fixa do arquivo:

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

As 28 traduções do repositório (README e CHANGELOG, quatorze idiomas) são
geradas novamente com `./regen_translations.sh --force` — Codex e `gpt-6.1-sol` na
assinatura ChatGPT por padrão, quatro em paralelo. `REGEN_PROVIDER` e
`REGEN_MODEL` alteram o caminho: `antigravity` continua numa assinatura, a
do Google, e prossegue sem exceção; uma API cobrada (`openai`, `gemini`,
`grok`, `openrouter`) é recusada sem `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` limita a duração de cada job (600 s, 1 800 s no Codex e
Antigravity). Os detalhes das ferramentas estão em `CLAUDE.md`.

## Projetos que utilizam este script

- **[jls42.org](https://jls42.org)** — blog pessoal publicado em 15 idiomas. Seu
  [acompanhamento diário de IA](https://jls42.org/fr/news) é traduzido todos os dias
  por esta ferramenta e serve de documento de referência para as medições acima.

## Autor

Julien LE SAUX
Email: contact@jls42.org

## Licença

GNU GENERAL PUBLIC LICENSE Version 3. Consulte [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Aviso

Este programa é distribuído **sem qualquer garantia**, nos termos das
seções 15 e 16 da GPL v3: fornecido «no estado em que se encontra», sem garantia de qualidade
comercial nem de adequação a uma finalidade específica, e seu autor não pode ser
responsabilizado por danos resultantes de sua utilização. O texto da
licença prevalece sobre este resumo.

- **Revise antes de publicar.** As proteções abrangem blocos de código,
  código em linha, URLs, âncoras e citações do modo `--news` — não abrangem
  títulos, tabelas, front matter nem o sentido das suas frases.
- **Seus documentos são enviados ao fornecedor escolhido**, sob seus termos
  de utilização e sua política de dados. Alguns modelos gratuitos podem
  reutilizar suas conversas para treinamento, e os termos do Antigravity
  permitem que o Google as reutilize e as submeta à revisão por humanos,
  inclusive com uma assinatura paga; um modelo local é a única opção que não faz
  nenhum dado sair da sua máquina.
- **As chamadas de API são cobradas de você.** Este programa não limita os
  gastos: um documento longo, uma nova tentativa após uma falha ou um modelo que raciocina
  muito custam mais.
- **As medições publicadas são observações datadas**, não garantias.

Os nomes de produtos e empresas citados pertencem aos seus respectivos
titulares. Este projeto não é afiliado a nenhum deles.

**Artigo traduzido do francês para o português com gpt-6.1-sol.**
