# Tradutor de Markdown com AI

🌍 [Francês](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [Inglês](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Espanhol](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [Chinês](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Alemão](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [Japonês](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [Coreano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [Árabe](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [Hindi](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Neerlandês](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polonês](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Romeno](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Sueco](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Qualidade do código</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Estado do controle de qualidade"></a>
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
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Selo Codacy"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Traduz arquivos Markdown de um idioma para outro preservando a
estrutura: blocos de código, código inline, URLs, âncoras, tabelas e front
matter. Onze formas de chamar um modelo — cinco APIs, quatro assinaturas sem
cobrança por uso, dois roteadores — e uma medição publicada do que cada
modelo realmente preserva.

## Em resumo

- **Onze opções de provider**: APIs OpenAI, Mistral, Claude, Gemini e Grok;
  assinaturas ChatGPT (Codex), Grok, Google (Antigravity) e Claude (Claude
  Code) sem cobrança por uso; roteadores OpenCode (open source, gratuito ou local) e OpenRouter
  (mais de 400 modelos).
- **Nenhum erro causado por um token perdido**: blocos de código, código inline,
  URLs, âncoras e citações são substituídos por tokens antes da chamada e
  verificados no retorno. Se faltar algum, o arquivo não é gravado.
- **Documentos longos**: segmentação conforme a janela do modelo.
- **Modo `--news`**: citações em inglês protegidas e flags gerenciadas por
  idioma, para artigos de acompanhamento de novidades.
- **Modo `--eco`**: modelos rápidos e mais baratos.
- **Nota de tradução** opcional, no início, no final ou em ambos.

## Instalação

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 ou mais recente. Para instalar a partir do repositório, consulte
[Contribuir](#contribuir).

## Configuração

As chaves são lidas em três locais, da maior para a menor prioridade; cada um
preenche apenas o que o anterior deixou vazio.

|     | Onde                                            | Para quê                             |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variáveis de ambiente                     | CI, contêineres, substituição pontual |
| 2   | `.env` do diretório atual (ou de um diretório pai) | uma chave específica de um projeto            |
| 3   | `~/.config/aipmt/.env`                        | configurado uma vez, vale em qualquer lugar       |

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

`GEMINI_API_KEY` é aceito no lugar de `GOOGLE_API_KEY`. O arquivo
do usuário segue `XDG_CONFIG_HOME` (apenas caminho absoluto) e `%APPDATA%`
no Windows. Sem chave, o comando lista os três locais.

**O `.env` de um projeto não pode redirecionar chamadas nem escolher o programa
executado.** Ele fornece chaves, nunca um destino ou um binário: qualquer
variável em `_BASE_URL`, `_API_BASE`, `_ENDPOINT` ou `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, os proxies (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), os repositórios de certificados (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) e `XDG_CONFIG_HOME` /
`APPDATA` são ignorados nesse arquivo, com um aviso. Um repositório clonado não deve
poder desviar sua chave nem fazer você executar o próprio programa dele na
primeira tradução. Esse arquivo também é lido sem interpolação:
`NOM=${OPENAI_API_KEY}` não copia a chave nele. Defina essas variáveis no
ambiente ou em `~/.config/aipmt/.env`.

Variáveis opcionais: `XAI_BASE_URL` (padrão `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (segundos por chamada, padrão 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(padrão 600), `GROK_BIN`, `GROK_HOME` (padrão `~/.grok`), `GROK_TIMEOUT`
(padrão 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (padrão 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (padrão 600), `OPENROUTER_BASE_URL`
(`https://` obrigatório), `OPENROUTER_TIMEOUT` (padrão 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (padrão 30). Cada uma é detalhada na
seção do respectivo provider.

## Primeiros passos

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` traduzido para espanhol gera `document-es.md` em `--target_dir`;
com `--include_model`, `document-es-gpt-5.6-terra.md`. A extensão sempre passa a ser
`.md` — `article.mdx` gera `article-en.md` — exceto com
`--keep_filename`, que mantém o nome original. Uma tradução já existente
é ignorada sem `--force`.

Códigos de saída: `0` se tudo foi concluído ou ignorado, `1` se ainda houver um arquivo
com falha (lista na saída de erro), `2` se a causa for a configuração.
Um arquivo com falha nunca é gravado, mesmo se a própria gravação falhar:
o conteúdo é gravado ao lado e depois renomeado. Basta executar novamente.

## Qual modelo escolher

Medição em dois documentos reais, traduzidos para os mesmos quatorze idiomas por
cada modelo. **O número indica a quantidade de idiomas, entre quatorze, em que a
tradução é gravada e nada difere da fonte.**

| Modelo                | Como acessá-lo                 | Artigo denso de acompanhamento de novidades | Este README    | O que difere e em quantos idiomas                                                                                                                          |
| --------------------- | --------------------------------- | ----------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | assinatura Google (Antigravity)   | ✅ 14/14                | ✅ 14/14     | nada, em nenhum dos dois documentos                                                                                                                                 |
| **Claude Sonnet 5.5** | chave API Anthropic                 | ✅ 14/14                | ✅ 14/14     | nada, em nenhum dos dois documentos                                                                                                                                 |
| **Gemini 3.7 Flash**  | chave API Google                    | ✅ 14/14                | ⚠️ 13/14     | 1 idioma em 14: uma palavra em negrito a mais (ja)                                                                                                                      |
| **Gemini 3.7 Flash**  | assinatura Google (Antigravity)   | ✅ 14/14                | ⚠️ 13/14     | 1 idioma em 14: uma palavra em negrito a menos (ko)                                                                                                                     |
| **GPT-5.6 Sol**       | assinatura ChatGPT ou chave OpenAI | ✅ 14/14                | ⚠️ 12/14     | 2 idiomas em 14: uma palavra em negrito a menos (ar, ja)                                                                                                                |
| **GLM-5.2**           | chave OpenRouter                    | ✅ 14/14                | ⚠️ 11/14     | 3 idiomas em 14: uma palavra em negrito a menos (hi, ja, ko)                                                                                                            |
| Claude Sonnet 5       | assinatura Claude (Claude Code)   | ⚠️ 13/14                | ⚠️ 13/14     | 1 idioma em 14 no artigo: uma palavra em negrito a mais (zh); 1 neste README: uma linha de tabela colada à anterior, oculta na exibição (ar)            |
| Claude Haiku 4.5      | assinatura Claude (Claude Code)   | ⚠️ 11/14                | ✅ 14/14     | 3 idiomas no artigo: um título de seção passou para o nível 1 (en, pl, ro); neste README, nada para o comparador, mas os links internos foram duplicados em inglês |
| Claude Sonnet 5       | chave API Anthropic                 | ⚠️ 11/14                | ⚠️ 12/14     | 3 idiomas no artigo: surgiu um bloco de código (es, de, hi); 2 neste README: um link sem sua marcação (sv), uma palavra em negrito (zh)                              |
| Claude Haiku 4.5      | chave API Anthropic                 | ⚠️ 7/14                 | ✅ 14/14     | 7 idiomas no artigo: um título de seção passou para o nível 1 — em japonês, permaneceu em francês; nada neste README                                              |
| Claude Haiku 5.5      | chave API Anthropic                 | ⚠️ 11/14                | ❌ 12/14     | 3 idiomas no artigo: um título de seção mudou de nível ou foi duplicado (ja, ko, zh); neste README, 2 idiomas rejeitados, códigos inline perdidos (ar, hi)    |
| Qwen 3.7 Flash        | chave OpenRouter                    | ❌ 8/14                 | ⚠️ 10/14     | 1 idioma rejeitado no artigo, 5 outros divergem; neste README, cerca de quarenta palavras colocadas em `code` (ar)                                                    |
| Grok 4.6              | assinatura Grok                   | ❌ 8/14                 | sem avaliação     | 5 idiomas rejeitados em 14, por falta de códigos inline e URLs na resposta; o neerlandês diverge em tudo                                                               |
| GPT-OSS 20B           | modelo local (Ollama)             | ❌ 7/14                 | sem nova medição | 4 idiomas rejeitados em 14: o modelo deixava trechos em francês, a proteção os bloqueou                                                                  |
| MiMo v2.5 (gratuito)   | OpenCode Zen, sem conta         | ❌ 11/14                | sem nova medição | 1 idioma rejeitado; uma seção perdida em polonês                                                                                                                  |
| Mistral Large         | chave API Mistral                   | ❌ 5/14                 | ❌ 1/14      | **uma seção inteira desaparece**: 1 idioma no artigo (hi), 3 neste README (ar, hi, ko) — e 3 idiomas rejeitados no artigo                                |
| DeepSeek V4 Flash     | chave OpenRouter                    | ❌ 3/14                 | sem nova medição | 10 idiomas rejeitados em 14; 37 minutos por idioma                                                                                                                 |
| Claude Opus 5.5       | assinatura Claude (Claude Code)   | ❌ 0/14                 | ✅ 14/14     | o artigo foi recusado nos 14 idiomas pelas proteções do Opus, por causa de uma notícia breve de biologia; nada neste README                                               |

|     | O que o símbolo indica                                                                                                                                                                                 |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | os quatorze idiomas traduzidos, e nada difere da fonte                                                                                                                                       |
| ⚠️  | os quatorze idiomas traduzidos; o que difere é a **marcação** — uma palavra em negrito, um `code`, um link que perde seus colchetes. Não falta nenhum texto, URL, bloco de código ou seção |
| ❌  | pelo menos um idioma não pôde ser traduzido — o arquivo é rejeitado e não é gravado — **ou** falta conteúdo em um arquivo gravado                                                                      |

O que se deve reter:

- **Uma tradução rejeitada não é uma tradução danificada.** Quando falta um token
  no retorno, o arquivo não é gravado e o idioma conta como
  rejeitado. É o que acontece com o Grok no artigo: quatro códigos inline e
  três URLs perdidos já no primeiro segmento, nos cinco sistemas de escrita não latinos.
- **Um modelo pode recusar um documento inteiro por uma única frase.** O Opus 5.5
  traduz este README sem nenhum desvio, mas não traduz nenhum artigo de acompanhamento de novidades: suas
  proteções interrompem a resposta em uma notícia breve de biologia. O arquivo não é
  gravado, e o aipmt informa o motivo.
- **Essa rede de proteção não cobre títulos, tabelas, front matter nem o
  texto.** Um modelo que elimina uma seção retorna um arquivo que a ferramenta grava
  sem objeções — é o caso do Mistral. Esses elementos não podem ser
  substituídos por um token, e as proteções atuais não os verificam;
  `scripts/compare_structure.py` detecta uma seção perdida, mas só depois.
- **O Grok não tem avaliação neste README**: sua sessão CLI expirou após doze
  idiomas, dos quais onze sem desvios. Uma campanha interrompida não recebe avaliação.
- **A densidade do documento conta mais que o idioma.** O Grok dá conta de
  READMEs comuns e falha em um artigo carregado de links, inclusive em
  neerlandês.

Datas e documentos: a coluna « Este README » foi medida em 9 de setembro de 2026
em uma revisão fixa deste arquivo (785 linhas, 285 códigos inline, 89 linhas
de tabela), alterada desde então — exceto as linhas Antigravity e Claude Code,
medidas em 26 de setembro na revisão publicada com a 1.14.0, mais curta
(600 linhas, 257 códigos inline, 85 linhas de tabela), e as linhas Claude
Sonnet 5.5, Haiku 5.5 e Haiku 4.5 via API, medidas em 18 de outubro na
mesma revisão. A coluna « Artigo denso de acompanhamento de novidades » vem da campanha de
4 e 5 de setembro em um artigo de 589 linhas, exceto a linha Grok, medida novamente em
9 de setembro em outra edição do mesmo boletim de novidades, as linhas Antigravity e
Claude Code, medidas em 26 de setembro no mesmo artigo, e essas três linhas
Claude, em 18 de outubro. As tabelas completas, as durações e o protocolo estão
em [Medições detalhadas](#medições-detalhadas).
## Todas as opções

| Opção                   | Descrição                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Arquivo Markdown único a traduzir (alternativa a `--source_dir`)                                             |
| `--source_dir`           | Diretório de origem que contém os arquivos Markdown (padrão: `content/posts`)                                   |
| `--target_dir`           | Diretório de saída para os arquivos traduzidos (padrão: `traductions_en`)                                    |
| `--source_lang`          | Idioma de origem (padrão: `fr`)                                                                                  |
| `--target_lang`          | Idioma de destino (padrão: `en`)                                                                                   |
| `--model`                | Modelo específico a utilizar                                                                                  |
| `--eco`                  | Utilizar os modelos econômicos                                                                              |
| `--use_mistral`          | Utilizar a API Mistral AI                                                                                     |
| `--use_claude`           | Utilizar a API Claude                                                                                         |
| `--use_gemini`           | Utilizar a API Gemini                                                                                         |
| `--use_grok`             | Utilizar a API xAI (Grok) — requer `XAI_API_KEY`                                                           |
| `--use_codex`            | Utilizar o CLI Codex com a cota da assinatura ChatGPT                                                    |
| `--use_grok_cli`         | Utilizar o CLI Grok com a cota da assinatura Grok                                                        |
| `--use_antigravity`      | Utilizar o CLI Antigravity (`agy`) com a cota da assinatura Google AI Pro ou Ultra                       |
| `--use_claude_code`      | Utilizar o CLI Claude Code (`claude -p`) com a cota da assinatura Claude Pro ou Max                      |
| `--use_opencode`         | Utilizar OpenCode (open source) com o provedor configurado no OpenCode; exige `--model provider/modèle` |
| `--use_openrouter`       | Utilizar OpenRouter — requer `OPENROUTER_API_KEY` e `--model fournisseur/modèle`                          |
| `--force`                | Forçar a retradução                                                                                       |
| `--keep_filename`        | Manter o nome original do arquivo                                                                          |
| `--news`                 | Modo de notícias: protege as citações EN, gerencia as bandeiras por idioma                                      |
| `--add_translation_note` | Adicionar uma nota de tradução                                                                                |
| `--note_position`        | Posição da nota: `top`, `bottom` (padrão) ou `both`                                                     |
| `--note_format`          | Formato da nota: `legacy` (padrão, parágrafo em negrito) ou `marker`                                            |
| `--include_model`        | Incluir o nome do modelo no arquivo de saída                                                            |
| `--reasoning_effort`     | Esforço de raciocínio GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

As nove flags `--use_*` são mutuamente exclusivas: combinar duas é
recusado.

## Providers

### Via API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` muda para o nível econômico de cada provedor.

| Provider    | Qualidade (padrão)                                                     | Econômico (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-5.6-terra`                                                      | `gpt-5.6-luna`            |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-3.7-flash`                                                   | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (também `gpt-5.6-sol`, `terra` e `luna` via `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.6`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.6`                                                           | `grok-4.5`                |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.7-flash-low`    |
| Claude Code | `sonnet`, esforço `low`                                               | idem — `--eco` sem efeito |
| OpenCode    | `--model provider/modèle` obrigatório                                | idem — `--eco` sem efeito |
| OpenRouter  | `--model fournisseur/modèle` obrigatório                             | idem — `--eco` sem efeito |

### Com a assinatura ChatGPT: `--use_codex`

Controla o CLI Codex oficial: a tradução é descontada da cota da
assinatura ChatGPT, sem chave de API nem cobrança por uso.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- O binário é procurado em `CODEX_BIN`, depois no `PATH`, depois no pacote
  `openai-codex-cli-bin`. `~/.codex/auth.json` nunca é lido.
- `OPENAI_API_KEY` e `CODEX_API_KEY` são removidas do ambiente do
  subprocesso: a presença de uma chave nunca provoca a mudança para a API.
- Cada segmento custa pelo menos uma «mensagem» da janela de 5 horas — duas
  se a validação falhar e houver uma nova tentativa. A OpenAI anuncia, como
  estimativa, 250-2 000 mensagens/5 h para `gpt-5.6-luna` (`--eco`) e
  10-100 para `gpt-5.6-sol` em um plano Plus.
- `--model gpt-5.6-sol`, o padrão até a 1.16.3, `--model gpt-5.6-terra`
  e `--model gpt-5.6-luna` também usam a assinatura.
- Um 429 do servidor não causa a perda do arquivo: o Codex se reconecta sozinho,
  o aipmt aguarda o fim do turno e, se o 429 persistir, o segmento
  é reenviado após 30 e depois 60 segundos. Um modelo ao qual a conta não tem acesso retorna um 400 «model is
  not supported when using Codex with a ChatGPT account».
- Mais lento que uma API, e a diferença aumenta com o documento: neste README,
  a mediana é de 6 min 46 s por idioma com `gpt-5.6-sol`, contra 36 s para
  `gemini-3.7-flash`.
- Recusado em CI (`CI` ou `GITHUB_ACTIONS` definido): a assinatura se autentica
  por um arquivo de sessão pessoal, que não deve estar em um runner
  compartilhado.
- Variáveis: `CODEX_BIN`, `CODEX_TIMEOUT` (segundos por segmento, padrão 600).

### Com a assinatura Grok: `--use_grok_cli`

Mesmo princípio com o CLI oficial Grok Build, com a assinatura SuperGrok ou
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Isolamento mais fraco que o do Codex.** O sandbox do SO do Grok não se aplica
  em muitas máquinas Linux recentes (AppArmor, sockets de runtime
  de contêiner), e um perfil que não pode ser aplicado inicia sem isolamento,
  silenciosamente. Por isso, o script não solicita nenhum perfil por padrão, informa isso e
  se apoia nas regras `--deny` do CLI, incluindo a catch-all `*` — a única
  camada que se recusa a iniciar em vez de remover a proteção sem
  avisar. `GROK_TRANSLATE_SANDBOX=read-only` exige o sandbox do SO, e a inicialização
  falha se a máquina não puder aplicá-lo.
- A cota é semanal, compartilhada com Chat, Imagine e Voice, e nenhum
  comando permite consultá-la: um lote pode consumir o uso conversacional
  sem aviso.
- Variáveis: `GROK_BIN`, `GROK_HOME` (diretório do CLI, padrão `~/.grok`),
  `GROK_TIMEOUT` (padrão 900), `GROK_TRANSLATE_SANDBOX`.

### Com a assinatura Google: `--use_antigravity`

Mesmo princípio com `agy`, o CLI oficial do Antigravity: para quem paga Google
AI Pro ou Ultra, a tradução é descontada da cota da assinatura em vez
de ser cobrada por token. É o único caminho para essa cota: o Gemini CLI já não
atende essas contas desde 18 de junho de 2026
([anúncio](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
e o SDK do Antigravity aceita apenas uma chave de API ou um projeto Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Nenhuma via paga permanece aberta.** O agy recebe do seu
  ambiente apenas uma lista fechada de variáveis — `PATH`, idioma e fuso horário,
  terminal, identidade, proxies e certificados, barramento de sessão — e nenhuma chave:
  várias de suas variáveis redirecionam uma chamada sem exibir nada (medido:
  uma envia o documento a um gateway de terceiros, outra a um projeto
  Google Cloud com cobrança), e uma lista de bloqueio deixava algumas de fora a cada revisão.
  Antes de qualquer segmento, `agy -p /config`, que não consome cota, deve mostrar
  os créditos de IA pagos desativados, sem chave de API nem projeto Google Cloud — uma
  configuração ausente implica recusa —, caso contrário, nada é traduzido; o log de cada
  chamada deve então comprovar o uso da assinatura (`authMethod=consumer`), caso contrário, a
  resposta é recusada.
- **Isolamento.** Cada chamada é executada em um diretório pessoal privado e
  descartável, com um agente de tradução sem ferramentas: suas configurações, regras,
  plugins, servidores MCP e hooks do agy não entram nele, nada é adicionado ao seu
  histórico, e a autenticação permanece no chaveiro, que o aipmt nunca lê.
  Quando um agente não é encontrado, o agy recorre silenciosamente ao seu agente de programação
  e às suas ferramentas: uma linha inteira do log deve confirmar o agente correto — um
  documento que cite essa mensagem não a substitui —, caso contrário, há recusa.
- **Plataformas**: Linux, em uma sessão que tenha um chaveiro (barramento de sessão
  D-Bus, Secret Service); macOS é aceito, sem ter sido medido nessa plataforma. Recusado
  no Windows, onde o agy não lê as variáveis que isolam cada chamada, e
  no Linux sem barramento de sessão — sessão SSH, contêiner, servidor: nesses casos, o agy
  armazena seu token em um arquivo de `~/.gemini`, que o isolamento oculta. A
  recusa ocorre antes de qualquer inicialização, com a causa informada, em vez de um minuto
  de espera por um código de login.
- **Modelos**: os de `agy models`. Os Gemini incluem o esforço no nome
  (`gemini-3.8-flash-medium`…): um nome sem sufixo é recusado antes da chamada,
  e `--reasoning_effort` não tem efeito. Por padrão, `gemini-3.8-flash-medium`,
  e `gemini-3.7-flash-low` em `--eco`; as campanhas que os definiram estão
  descritas em [Medições detalhadas](#medições-detalhadas). Claude e GPT-OSS
  têm sua própria cota, muito menor: cerca de 1 % da janela de
  5 horas por chamada medida, contra 0,05 % em Flash.
- **Cota**: por grupo, uma janela de 5 horas e uma semanal,
  proporcionais ao custo em tokens. Medido na conta do autor: cerca de
  16 pontos da janela de 5 horas por milhão de caracteres de origem em
  `gemini-3.8-flash-medium`, 14 em `gemini-3.7-flash-medium` e 7 a 8 com
  esforço baixo — um README de 40 000 caracteres custa, portanto, um pouco mais de
  meio ponto. Já o limite semanal depende do nível. As novas tentativas seguem
  o que o agy declara como passível de nova tentativa; na ausência dessa indicação, uma janela esgotada nunca
  gera nova tentativa: ela faz cada arquivo falhar até a redefinição
  exibida por `/usage`.
- **Mais lento que a API**: no artigo denso das medições, a mediana é de 3 min 59 s por
  idioma em `gemini-3.8-flash-medium` e 3 min 14 s em
  `gemini-3.7-flash-medium`, contra 1 min 18 s para Gemini 3.7 Flash via API.
- **Interrupção**: Ctrl-C ou o fechamento do terminal encerram o agy junto com o
  comando, em vez de deixá-lo terminar o turno consumindo sua cota; o mesmo vale
  para Codex, Grok CLI e OpenCode. Em `nohup`, a tradução continua.
- Recusado em CI (`CI` ou `GITHUB_ACTIONS` definido): a autenticação fica em um
  chaveiro pessoal. Em um runner, `--use_gemini` com `GOOGLE_API_KEY`.
- Variáveis: `AGY_BIN` (caso contrário, o `PATH`, depois `~/.local/bin/agy`),
  `AGY_TIMEOUT` (segundos por segmento, incluindo a inicialização, padrão 900).

**Termos de uso: é a sua conta que está em jogo.** Os
[termos do Antigravity](https://antigravity.google/terms) (seção 6) e sua
[FAQ](https://antigravity.google/docs/faq/) proíbem acessar o serviço
por software de terceiros usando a autenticação do Antigravity — Claude Code,
OpenClaw e OpenCode são citados —, sob pena de suspensão da conta. O aipmt
não lê nem reutiliza o token: ele executa o binário oficial no
[modo headless](https://antigravity.google/docs/cli/headless/) que o Google
documenta para scripts e CI. Um membro do Google considerou «padrão»
executar `agy -p` a partir de um script local para o próprio trabalho
([fórum oficial, 25 de setembro de 2026, resposta sem caráter contratual](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
nenhum texto esclarece o caso de uma ferramenta distribuída como esta.

**Somente documentos públicos.** Segundo a seção 5 dos mesmos termos, as
interações — prompts, respostas, metadados — podem servir para melhorar os
produtos e o aprendizado de máquina do Google e ser revisadas por
humanos, mesmo com assinatura paga. A desativação desse uso passa pela configuração
`enableTelemetry`, cujo efeito não é documentado e que o aipmt não define; suas configurações
do agy não são transferidas para o ambiente isolado. Não envie nada confidencial por essa via.
### Com a assinatura Claude: `--use_claude_code`

O mesmo princípio com `claude`, o CLI oficial do Claude Code, no modo `-p`: para
quem paga Claude Pro ou Max, a tradução é descontada da quota da
assinatura em vez de ser cobrada por token. Não confundir com
`--use_claude`, a API da Anthropic, cobrada por utilização.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Nenhuma via paga fica aberta, e cada chamada comprova isso.** O Claude
  Code recebe do seu ambiente apenas uma lista fechada de variáveis — sem
  chave de API, token, fornecedor cloud ou marcador da sessão Claude Code
  a partir da qual o aipmt seria iniciado. Antes do primeiro segmento, `claude auth status` deve
  mostrar a ligação por assinatura, sem chave Console, e `/usage`, que não consome
  quota, deve confirmá-la; cada chamada confirma-a também no seu
  evento de inicialização, caso contrário a resposta é recusada.
- **Desative o «extra usage»** (claude.ai, Definições → Utilização) para
  garantir o custo de zero euros: quando ativado, assume o consumo de uma janela esgotada e
  cobra sem apresentar erro. O aipmt interrompe a tradução assim que o relatório
  de quota de uma chamada o indica, mas essa chamada já foi contabilizada.
- **Quota partilhada com as suas sessões Claude Code.** Cada chamada indica
  a utilização das janelas de 5 horas e da semana; acima de 80 %
  (`AIPMT_CLAUDE_MAX_UTILIZATION`), não é iniciado mais nenhum segmento, para não
  esgotar o que usa no seu trabalho.
- **Isolamento.** Cada chamada é executada sem ferramentas, num diretório privado e
  descartável, em modo sem personalização: nem os seus `CLAUDE.md`, nem os seus plugins,
  hooks, servidores MCP ou definições são carregados, e nada da
  sessão é guardado. Os anexos estão desativados: um `@chemin` no seu documento
  permanece texto e não abre nenhum ficheiro (verificado por medição).
- **Modelos**: `sonnet` por predefinição, com esforço `low`, e em `--eco` também:
  `--eco` não altera nada nesta via. Medidos nos mesmos documentos, `haiku`
  é duas vezes mais lento — raciocina sem que seja possível impedi-lo — por
  um custo apenas ligeiramente inferior, e `opus` recusa conteúdos de biologia (ponto
  seguinte). Ambos continuam acessíveis por `--model`; estes aliases seguem o
  modelo mais recente da sua família. `fable` e as variantes `[1m]` são recusados,
  porque passam a consumir créditos pagos. `--reasoning_effort` define o esforço,
  do qual uma tradução não beneficia: o raciocínio medido é nulo ou quase.
- **Opus recusa determinados conteúdos de biologia.** As suas salvaguardas são mais
  rigorosas do que as do Sonnet, e a mensagem de erro da Anthropic avisa que
  «podem, por vezes, sinalizar trabalhos relacionados com investigação em biologia». Verificado por medição: uma breve notícia de
  acompanhamento sobre 279 moléculas geradas levou à recusa do artigo nas catorze
  línguas. Nada é escrito: o aipmt recusa a resposta interrompida, identifica as
  salvaguardas e recomenda `--model sonnet`.
- Recusado em CI (`CI` ou `GITHUB_ACTIONS` definido) e no Windows (não medido).
- Variáveis: `AIPMT_CLAUDE_BIN` (caso contrário, o `PATH`, depois `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (segundos por segmento, predefinição 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (predefinição 0.8), `CLAUDE_CONFIG_DIR` (a conta do
  Claude Code, nunca obtida de um `.env` do projeto); diretórios de trabalho em
  `XDG_CACHE_HOME/aipmt/claude-code` (predefinição `~/.cache`).

**Condições de utilização: é a sua conta que está em jogo.** A
[página legal do Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
não impede «um utilizador final de iniciar sessão no binário Claude Code não modificado
com a sua própria assinatura Claude»: é isso que o aipmt faz, ao iniciar o
binário oficial sem nunca ler o token. Mas a Anthropic «não permite
que programadores terceiros […] encaminhem pedidos através de credenciais
dos planos Free, Pro ou Max em nome dos seus utilizadores», prefere a chave de API para ferramentas
de terceiros, «incluindo projetos open source», e reserva-se o direito de descontar a sua
utilização dos créditos pagos
([ajuda Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Nenhum texto resolve o caso de uma ferramenta distribuída que inicia o binário.

**Dados**: nas contas Free, Pro e Max, o treino dos modelos
também se aplica ao Claude Code quando a definição de privacidade o permite
([página sobre dados](https://code.claude.com/docs/en/data-usage)). O aipmt não guarda
nenhuma transcrição local (`--no-session-persistence`). Não faça passar por ele
nada confidencial.

### Para o fornecedor à sua escolha: `--use_opencode`

[OpenCode](https://opencode.ai) é um agente de código open source (MIT) que
encaminha pedidos para os fornecedores nele configurados: chave de API, assinatura,
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
cujas trocas podem servir para treino, e essa escolha não é feita em
seu nome.

Isolamento em cada chamada:

- uma configuração inline, com prioridade sobre a sua, define um agente `aipmt`
  cujas ferramentas são todas recusadas (`permission: { "*": "deny" }`), com partilha de
  sessão desativada, `--pure`, nunca `--auto`;
- diretório de trabalho descartável e vazio, com `OPENCODE_DISABLE_PROJECT_CONFIG` e
  `OPENCODE_DISABLE_CLAUDE_CODE` definidos — sem eles, o OpenCode injeta no
  prompt o `AGENTS.md` do diretório atual e `~/.claude/CLAUDE.md`. O
  `~/.config/opencode/AGENTS.md` global continua a ser injetado, pois o OpenCode não permite
  excluí-lo;
- contrato de saída: código de retorno 0, nenhum evento `error`, nenhuma chamada
  de ferramenta, último passo em `stop`, texto não vazio, e o agente `aipmt`
  efetivamente carregado — um `--agent` desconhecido não faz o OpenCode falhar, ele
  recorre silenciosamente ao agente de programação;
- nenhuma chave de `aipmt` é transmitida, exceto `OPENCODE_API_KEY`, a chave
  do próprio OpenCode. Os fornecedores são configurados no OpenCode, não no
  `.env` do `aipmt`.

A saber:

- Os modelos gratuitos do Zen mudam, têm limites não documentados, e
  as suas trocas podem servir para treino: para documentação
  pública, não para conteúdo privado.
- Um modelo local deve oferecer pelo menos 16 k tokens de contexto, pois os segmentos
  podem ter até 16 000 caracteres. O Ollama configura frequentemente 4 096: usar
  um `Modelfile` com `PARAMETER num_ctx 32768`.
- `--eco` não tem efeito; `--reasoning_effort` é transmitido tal como está como
  `--variant` do OpenCode.
- O OpenCode regista cada sessão em `~/.local/share/opencode/`.
- Variáveis: `OPENCODE_BIN` (caso contrário, o `PATH`, depois `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (segundos por segmento, predefinição 600). `OPENCODE_CONFIG`
  é passado tal como está ao OpenCode.

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

`reasoningEffort: "none"` desativa a reflexão que o Ollama ativa por predefinição nestes
modelos, e que um Modelfile não consegue desativar. Medido numa frase de
seis palavras: 919 tokens de reflexão e 68 segundos sem a opção, 9 tokens com ela.

### Para mais de 400 modelos: `--use_openrouter`

O OpenRouter é um router cobrado por utilização, com um crédito único, que dá acesso a
modelos alojados por terceiros — incluindo os modelos chineses abertos que nenhum
outro provider disponibiliza aqui.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` é obrigatório. Um preflight, executado antes de qualquer cobrança, resolve
duas particularidades do encaminhamento:

- **O mesmo modelo é servido por dezenas de fornecedores de alojamento com limites
  diferentes** — no `z-ai/glm-5.3-flash`, 23 fornecedores de alojamento, um deles limitado a
  2 048 tokens de saída. O preflight lê `/api/v1/models/{modèle}/endpoints`,
  exclui os fornecedores de alojamento com menos de 8 000 tokens de saída ou com estado degradado, e
  fixa os restantes com `allow_fallbacks: false`.
- **O raciocínio é cobrado à tarifa de saída** — 107 tokens contra 2 numa
  resposta «OK» de `z-ai/glm-5.2`. É desativado por predefinição; os modelos
  que o impõem recebem o menor esforço que aceitam, pois a predefinição do
  catálogo pode saturar a saída antes do fim da tradução.
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
- `finish_reason=length` com uma saída vazia corresponde a um orçamento consumido pelo
  raciocínio, não a um truncamento: a mensagem faz essa distinção.
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
desvios**, aqueles em que `scripts/compare_structure.py` não deteta nada — o mesmo número de
secções, subtítulos, links, URLs distintos, blocos de código,
códigos inline, linhas de tabela, blocos de citação e palavras em negrito.

«Sem desvios» significa «nada detetado», não «idêntico»: o comparador
conta elementos sem ler o seu conteúdo. Não sinaliza um título de
nível 4 eliminado, nem o texto de um código inline substituído, nem uma bandeira
trocada, nem um link interno apresentado com um parêntese a mais,
`[texte]((#ancre))`, que já não leva a lado nenhum — e não avalia a
língua.

### Artigo denso de acompanhamento, modo `--news`

Uma edição do [acompanhamento de IA do jls42.org](https://jls42.org/fr/news):
589 linhas, 140 links, 21 secções, 3 citações em inglês protegidas. Campanha
de 4 e 5 de setembro de 2026.

| Modelo                                          | Acesso              | Escritas | Sem desvios   | Mediana/língua |
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

O Grok foi medido novamente a 9 de setembro noutra edição do mesmo acompanhamento
(356 linhas): 9 línguas escritas em 14, 8 sem desvios. É este o valor que
figura na tabela inicial. Três campanhas interrompidas não estão
registadas: `qwen3.5-27b` (9 línguas) e `kimi-k2.6` (4) por falta de crédito,
`z-ai/glm-5.3-flash` cujas duas falhas resultavam de uma definição de raciocínio
que o provider passou entretanto a corrigir. As linhas OpenRouter foram medidas com as
definições predefinidas do router, antes de `--use_openrouter`; `z-ai/glm-5.2`,
medido novamente com o provider distribuído, apresenta os mesmos 14/14. Os valores foram
recalculados a 10 de setembro com o comparador atual: `qwen3.8-flash` e
`qwen3.7-flash` ganham uma língua cada um em relação à primeira
publicação, os restantes mantêm-se.

As linhas `--use_antigravity` foram medidas a 26 de setembro no mesmo
artigo, com quatro traduções em paralelo: `gemini-3.7-flash-medium` de manhã,
`gemini-3.8-flash-medium` à tarde. Em inglês, cada um removeu por si próprio
as três linhas de tradução francesa sob as citações, sem inventar uma
bandeira, e as citações em inglês estão intactas: a limpeza de recurso não
teve nada a fazer. Em `--eco` (`gemini-3.7-flash-low`), apenas em quatro línguas
(en, ja, ar, hi): 4 escritas em 4, todas sem desvios, 1 min 52 s de
mediana. Contraprova no mesmo dia numa edição mais recente do acompanhamento,
a de 25 de setembro (438 linhas, 2 citações em inglês), traduzida fora do
blog por `gemini-3.7-flash-medium`: 14 escritas em 14, todas sem desvios, 87 a
128 s por língua.

As linhas `--use_claude_code` foram medidas a 26 de setembro no mesmo
artigo, com quatro traduções em paralelo, com esforço `low`. Com `sonnet`, as
citações em inglês estão intactas nas catorze línguas e, em inglês, o
modelo removeu por si próprio as linhas de tradução francesa, sem inventar uma
bandeira. `opus` não escreveu nenhuma língua: em todas, as suas salvaguardas
interromperam a resposta no último segmento, devido a uma breve notícia sobre 279 moléculas
geradas para um local de ligação. Enviada isoladamente, essa notícia é recusada
na categoria «bio»; `sonnet` traduziu-a em todas as línguas. `haiku` escreve
as catorze línguas; em três (en, pl, ro), um título de secção passa do
nível 2 para o nível 1. Raciocina sem que seja possível impedi-lo — 61 % dos
seus tokens de saída —, daí demorar mais do dobro do tempo de `sonnet`.

As linhas `claude-sonnet-5-5`, `claude-haiku-5-5` e `claude-haiku-4-5` foram
medidas a 18 de outubro pela API da Anthropic, no mesmo artigo, com quatro
traduções em paralelo por modelo. O Sonnet 5.5 recusa que se desative a sua
reflexão: o aipmt envia-lhe a definição mais baixa que aceita, e as suas
respostas não apresentam reflexão. Escreve as catorze línguas sem desvios e sem
repetir nenhum segmento; em inglês, removeu por si próprio as linhas de
tradução francesa, sem inventar uma bandeira, e as citações em inglês estão
intactas em todas as línguas. O Haiku 5.5 é medido com a sua reflexão adaptativa: com a reflexão
desativada, deixava parágrafos inteiros em francês, que a verificação recusa —
3 línguas escritas em 14. Os dois Haiku tropeçam na mesma notícia: o Haiku 5.5
altera o nível do seu título ou duplica-o em japonês, coreano e
chinês, o Haiku 4.5 passa-o para o nível 1 em sete línguas e deixa-o em
francês na tradução para japonês. O Haiku 4.5 custa 3,67 $ para os dois documentos nas
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

Duas campanhas interrompidas não são avaliadas: Grok, sessão CLI expirada
após doze idiomas (onze sem desvios), e `qwen3.8-flash`, HTTP 429 do seu
fornecedor de alojamento após dois. `opencode/mimo-v2.5-free` e `ollama/gpt-oss-20b-32k`
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
catorze idiomas, `claude-haiku-5-5` nos doze em que escreveu.

### Quatro README de projetos conhecidos

FastAPI, Ollama, tldr-pages e Vue.js, obtidos tal como estão no GitHub — são
documentos mais fáceis do que os dois anteriores. A campanha visava os modelos
com dificuldades; Gemini serve aqui como ponto de comparação.

| Modelo                    | Âmbito                  | Escritas | Sem desvios   |
| ------------------------- | -------------------------- | ------- | ------------ |
| `gemini-3.7-flash`        | 4 projetos × 14 idiomas     | 56/56   | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 projetos × 14 idiomas     | 55/56   | ❌ 47/56     |
| `grok-4.6` (subscrição)   | 4 projetos × ar, hi, ja, zh | 16/16   | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 projetos × ar, hi, ja, zh | 15/16   | ❌ 9/16      |

### O que estas medições não são

- **Não são uma classificação exaustiva**: só o OpenRouter oferece mais de quatrocentos
  modelos; foram medidos cerca de quinze.
- **Durações indicativas**: de três a seis traduções em paralelo, consoante
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
geradas novamente com `./regen_translations.sh --force` — Codex e `gpt-6.1-sol` na
subscrição ChatGPT por predefinição, quatro em paralelo. `REGEN_PROVIDER` e
`REGEN_MODEL` alteram o caminho: `antigravity` continua numa subscrição, a
da Google, e é permitido sem exceção; uma API faturada (`openai`, `gemini`,
`grok`, `openrouter`) é recusada sem `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` limita cada job (600 s, 1 800 s no Codex e no
Antigravity). Os detalhes das ferramentas estão em `CLAUDE.md`.

## Projetos que utilizam este script

- **[jls42.org](https://jls42.org)** — blogue pessoal publicado em 15 idiomas. A sua
  [monitorização diária de IA](https://jls42.org/fr/news) é traduzida todos os dias
  por esta ferramenta e serve de documento de referência para as medições acima.

## Autor

Julien LE SAUX
Email: contact@jls42.org

## Licença

GNU GENERAL PUBLIC LICENSE Versão 3. Consulte [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Aviso

Este programa é distribuído **sem qualquer garantia**, nos termos das
secções 15 e 16 da GPL v3: fornecido «tal como está», sem garantia de qualidade
comercial nem de adequação a uma finalidade específica, e o seu autor não pode ser
responsabilizado por danos resultantes da sua utilização. O texto da
licença prevalece sobre este resumo.

- **Reveja antes de publicar.** As proteções abrangem os blocos de código, o
  código em linha, os URL, as âncoras e as citações do modo `--news` — não abrangem os
  títulos, as tabelas, o front matter nem o sentido das suas frases.
- **Os seus documentos são enviados ao fornecedor escolhido**, sujeitos às suas condições
  de utilização e à sua política de dados. Alguns modelos gratuitos podem
  reutilizar as suas conversas para treino, e as condições do Antigravity
  permitem à Google reutilizá-las e submetê-las a revisão humana,
  incluindo com uma subscrição paga; um modelo local é a única opção que não faz
  sair quaisquer dados da sua máquina.
- **As chamadas de API são-lhe faturadas.** Este programa não limita a
  despesa: um documento longo, uma nova tentativa após uma falha ou um modelo que raciocine
  muito têm um custo maior.
- **As medições publicadas são observações datadas**, não são garantias.

Os nomes dos produtos e das empresas mencionados pertencem aos respetivos
titulares. Este projeto não está afiliado a nenhum deles.

**Artigo traduzido do francês para o português com gpt-6.1-sol.**
