# Tradutor de Markdown AI-Powered

🌍 [Français](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README.md) | [English](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-en.md) | [Español](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-es.md) | [中文](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-zh.md) | [Deutsch](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-de.md) | [日本語](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ja.md) | [한국어](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ko.md) | [العربية](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ar.md) | [हिन्दी](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-hi.md) | [Italiano](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-it.md) | [Nederlands](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-nl.md) | [Polski](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pl.md) | [Português](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-pt.md) | [Română](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-ro.md) | [Svenska](https://github.com/jls42/ai-powered-markdown-translator/blob/main/README-sv.md)

<h4 align="center">📊 Qualidade do código</h4>

<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=alert_status" alt="Quality Gate Status"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=security_rating" alt="Security Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=reliability_rating" alt="Reliability Rating"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_rating" alt="Maintainability Rating"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=coverage" alt="Coverage"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=vulnerabilities" alt="Vulnerabilities"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Bugs"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=code_smells" alt="Code Smells"></a>
</p>
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=duplicated_lines_density" alt="Duplicated Lines (%)"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=sqale_index" alt="Technical Debt"></a>
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=ncloc" alt="Lines of Code"></a>
</p>
<p align="center">
  <a href="https://app.codacy.com/gh/jls42/ai-powered-markdown-translator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/ae3e86bcb20643308c5eb5e1380e3b3c" alt="Codacy Badge"></a>
  <a href="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator"><img src="https://www.codefactor.io/repository/github/jls42/ai-powered-markdown-translator/badge" alt="CodeFactor"></a>
</p>

Traduz arquivos Markdown de um idioma para outro preservando a
estrutura: blocos de código, código em linha, URLs, âncoras, tabelas e front
matter. Onze maneiras de chamar um modelo — cinco APIs, quatro assinaturas sem
cobrança por uso, dois roteadores — e uma medição publicada do que cada
modelo realmente preserva.

## Em resumo

- **Onze caminhos de provedor**: APIs OpenAI, Mistral, Claude, Gemini e Grok;
  assinaturas ChatGPT (Codex), Grok, Google (Antigravity) e Claude (Claude
  Code) sem cobrança por uso; roteadores OpenCode (código aberto, gratuito ou local) e OpenRouter
  (mais de 400 modelos).
- **Nada corrompido por causa de um token perdido**: blocos de código, código em linha,
  URLs, âncoras e citações são substituídos por tokens antes da chamada e
  verificados no retorno. Se faltar algum, o arquivo não é gravado.
- **Documentos longos**: segmentação de acordo com a janela de contexto do modelo.
- **Modo `--news`**: citações em inglês protegidas e bandeiras gerenciadas por
  idioma, para artigos de curadoria.
- **Modo `--eco`**: modelos rápidos e mais baratos.
- **Nota de tradução** opcional, no topo, no rodapé ou em ambos.

## Instalação

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.11 ou mais recente. Para instalar a partir do repositório, consulte
[Contribuir](#contribuir).

## Configuração

As chaves são lidas em três locais, do mais prioritário ao menor; cada um apenas
preenche o que o anterior deixar vazio.

|     | Onde                                          | Para que                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variáveis de ambiente                         | CI, contêineres, sobreposição pontual |
| 2   | `.env` do diretório atual (ou de um pai) | uma chave específica de um projeto    |
| 3   | `~/.config/aipmt/.env`                        | instalado uma vez, válido em qualquer lugar |

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

`GEMINI_API_KEY` é aceito no lugar de `GOOGLE_API_KEY`. O arquivo do
usuário segue `XDG_CONFIG_HOME` (apenas caminho absoluto) e `%APPDATA%`
no Windows. Sem chave, o comando lista os três locais.

**O `.env` de um projeto não pode redirecionar chamadas nem escolher o programa
executado.** Ele fornece chaves, nunca um destino nem um binário: qualquer
variável em `_BASE_URL`, `_API_BASE`, `_ENDPOINT` ou `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, os proxies (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), os repositórios de certificados (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) e `XDG_CONFIG_HOME` /
`APPDATA` são ignorados nele, com um aviso. Um repositório clonado não deve
conseguir desviar sua chave, nem fazer você executar o próprio programa dele na
primeira tradução. Este arquivo também é lido sem interpolação:
`NOM=${OPENAI_API_KEY}` não copia a chave nele. Defina essas variáveis no
ambiente ou em `~/.config/aipmt/.env`.

Variáveis opcionais: `XAI_BASE_URL` (padrão `https://api.x.ai/v1`),
`CLAUDE_TIMEOUT` (segundos por chamada, padrão 900), `CODEX_BIN`, `CODEX_TIMEOUT`
(padrão 600), `GROK_BIN`, `GROK_HOME` (padrão `~/.grok`), `GROK_TIMEOUT`
(padrão 900), `GROK_TRANSLATE_SANDBOX`, `AGY_BIN`, `AGY_TIMEOUT` (padrão 900),
`OPENCODE_BIN`, `OPENCODE_TIMEOUT` (padrão 600), `OPENROUTER_BASE_URL`
(`https://` obrigatório), `OPENROUTER_TIMEOUT` (padrão 900),
`OPENROUTER_PREFLIGHT_TIMEOUT` (padrão 30). Cada uma é detalhada na
seção do seu provedor.

## Primeiros passos

```bash
# un fichier
aipmt --file document.md --target_dir out/ --source_lang fr --target_lang en

# un répertoire
aipmt --source_dir content/fr --target_dir content/en --source_lang fr --target_lang en

# un autre provider
aipmt --use_gemini --file document.md --target_dir out/ --target_lang ja
```

`document.md` traduzido para o espanhol resulta em `document-es.md` em `--target_dir`;
com `--include_model`, `document-es-gpt-6.1-terra.md`. A extensão sempre
se torna `.md` — `article.mdx` resulta em `article-en.md` — exceto com
`--keep_filename`, que mantém o nome original. Uma tradução já existente
é ignorada sem `--force`.

Códigos de saída: `0` se tudo foi concluído com sucesso ou ignorado, `1` se restar algum arquivo
com falha (lista na saída de erro), `2` se o problema for na configuração.
Um arquivo com falha nunca é gravado, mesmo se a própria gravação falhar:
o conteúdo é escrito ao lado e depois renomeado. Basta executar novamente.

## Qual modelo escolher

Medido em dois documentos reais, traduzidos para os mesmos catorze idiomas por
cada modelo. **O número é a quantidade de idiomas, de catorze, em que a
tradução é gravada e nada difere da fonte.**

| Modelo                | Como acessar                      | Artigo denso de curadoria | Este README  | O que difere e em quantos idiomas                                                                                                                                  |
| --------------------- | --------------------------------- | ------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash**  | assinatura Google (Antigravity)   | ✅ 14/14                  | ✅ 14/14     | nada, em nenhum dos dois documentos                                                                                                                                |
| **Claude Sonnet 5.5** | chave de API Anthropic            | ✅ 14/14                  | ✅ 14/14     | nada, em nenhum dos dois documentos                                                                                                                                |
| **Gemini 3.7 Flash**  | chave de API Google               | ✅ 14/14                  | ⚠️ 13/14     | 1 idioma em 14: uma palavra em negrito a mais (ja)                                                                                                                 |
| **Gemini 3.7 Flash**  | assinatura Google (Antigravity)   | ✅ 14/14                  | ⚠️ 13/14     | 1 idioma em 14: uma palavra em negrito a menos (ko)                                                                                                                |
| **GPT-5.6 Sol**       | assinatura ChatGPT ou chave OpenAI | ✅ 14/14                 | ⚠️ 12/14     | 2 idiomas em 14: uma palavra em negrito a menos (ar, ja)                                                                                                           |
| **GLM-5.2**           | chave OpenRouter                  | ✅ 14/14                  | ⚠️ 11/14     | 3 idiomas em 14: uma palavra em negrito a menos (hi, ja, ko)                                                                                                       |
| Claude Sonnet 5       | assinatura Claude (Claude Code)   | ⚠️ 13/14                  | ⚠️ 13/14     | 1 idioma em 14 no artigo: uma palavra em negrito a mais (zh); 1 neste README: uma linha de tabela colada à anterior, oculta na exibição (ar)                       |
| Claude Haiku 4.5      | assinatura Claude (Claude Code)   | ⚠️ 11/14                  | ✅ 14/14     | 3 idiomas no artigo: um título de seção alterado para nível 1 (en, pl, ro); neste README, nada para o comparador, mas os links internos foram duplicados em inglês |
| Claude Sonnet 5       | chave de API Anthropic            | ⚠️ 11/14                  | ⚠️ 12/14     | 3 idiomas no artigo: um bloco de código apareceu (es, de, hi); 2 neste README: um link sem a sua marcação (sv), uma palavra em negrito (zh)                         |
| Claude Haiku 4.5      | chave de API Anthropic            | ⚠️ 7/14                   | ✅ 14/14     | 7 idiomas no artigo: um título de seção alterado para nível 1 — em japonês, permaneceu em francês; nada neste README                                               |
| Claude Haiku 5.5      | chave de API Anthropic            | ⚠️ 11/14                  | ❌ 12/14     | 3 idiomas no artigo: um título de seção com nível alterado ou duplicado (ja, ko, zh); neste README, 2 idiomas recusados, códigos em linha perdidos (ar, hi)         |
| Qwen 3.7 Flash        | chave OpenRouter                  | ❌ 8/14                   | ⚠️ 10/14     | 1 idioma recusado no artigo, outros 5 divergiram; neste README, cerca de quarenta palavras colocadas em `code` (ar)                                       |
| Grok 4.6              | assinatura Grok                   | ❌ 8/14                   | não avaliado | 5 idiomas recusados em 14, por falta de códigos em linha e URLs retornados; o holandês diverge em tudo                                                            |
| GPT-OSS 20B           | modelo local (Ollama)             | ❌ 7/14                   | não remedido | 4 idiomas recusados em 14: o modelo deixava trechos em francês, o sistema de proteção os barrou                                                                   |
| MiMo v2.5 (gratuito)  | OpenCode Zen, sem conta           | ❌ 11/14                  | não remedido | 1 idioma recusado; uma seção perdida em polonês                                                                                                                    |
| Mistral Large         | chave de API Mistral              | ❌ 5/14                   | ❌ 1/14      | **uma seção inteira desaparece**: 1 idioma no artigo (hi), 3 neste README (ar, hi, ko) — e 3 idiomas recusados no artigo                                           |
| DeepSeek V4 Flash     | chave OpenRouter                  | ❌ 3/14                   | não remedido | 10 idiomas recusados em 14; 37 minutos por idioma                                                                                                                  |
| Claude Opus 5.5       | assinatura Claude (Claude Code)   | ❌ 0/14                   | ✅ 14/14     | o artigo foi recusado nos 14 idiomas pelos mecanismos de proteção do Opus, devido a uma nota sobre biologia; nada neste README                                    |

|     | O que o símbolo significa                                                                                                                                                                             |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | todos os catorze idiomas traduzidos e nada difere da fonte                                                                                                                                            |
| ⚠️  | todos os catorze idiomas traduzidos; o que difere é **marcação** — uma palavra em negrito, um `code`, um link que perde os colchetes. Nenhum texto, URL, bloco de código ou seção está faltando |
| ❌  | pelo menos um idioma não pôde ser traduzido — o arquivo é recusado, não gravado — **ou** falta conteúdo em um arquivo gravado                                                                       |

O que se deve ter em mente:

- **Uma tradução recusada não é uma tradução corrompida.** Quando um token
  falta no retorno, o arquivo não é gravado e o idioma conta como
  recusado. É o que acontece com o Grok no artigo: quatro códigos em linha e
  três URLs perdidos logo no primeiro segmento, nas cinco escritas não latinas.
- **Um modelo pode recusar um documento inteiro por causa de uma única frase.** O Opus 5.5
  traduz este README sem nenhuma divergência, mas nenhum artigo de curadoria: seus
  mecanismos de proteção interrompem a resposta em uma nota sobre biologia. O arquivo não é
  gravado, e o aipmt explica o motivo.
- **Esta rede de segurança não cobre títulos, tabelas, front matter nem o
  texto.** Um modelo que remove uma seção retorna um arquivo que a ferramenta grava
  sem hesitar — é o caso do Mistral. Esses elementos não podem ser
  substituídos por um token, e as proteções atuais não os verificam;
  `scripts/compare_structure.py` detecta uma seção perdida, mas somente a posteriori.
- **O Grok não tem avaliação neste README**: sua sessão CLI expirou após doze
  idiomas, sendo onze sem divergências. Uma campanha interrompida não recebe nota.
- **A densidade do documento conta mais do que o idioma.** O Grok dá conta de
  READMEs comuns e falha em um artigo carregado de links, inclusive em
  holandês.

Datas e documentos: a coluna «Este README» foi medida em 9 de setembro de 2026
em uma revisão congelada deste arquivo (785 linhas, 285 códigos em linha, 89 linhas
de tabela), modificada desde então — exceto as linhas Antigravity e Claude Code,
medidas em 26 de setembro na revisão publicada com a 1.14.0, mais curta
(600 linhas, 257 códigos em linha, 85 linhas de tabela), e as linhas Claude
Sonnet 5.5, Haiku 5.5 e Haiku 4.5 pela API, medidas em 18 de outubro na
mesma revisão. A coluna «Artigo denso de curadoria» vem da campanha de
4 e 5 de setembro em um artigo de 589 linhas, exceto a linha Grok, remedida em
9 de setembro em outra edição da mesma curadoria, as linhas Antigravity e
Claude Code, medidas em 26 de setembro no mesmo artigo, e essas três linhas
Claude, em 18 de outubro. As tabelas completas, as durações e o protocolo estão
em [Medições detalhadas](#medições-detalhadas).

## Todas as opções

| Opção                    | Descrição                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Arquivo Markdown único a traduzir (alternativa a `--source_dir`)                                             |
| `--source_dir`           | Diretório de origem contendo os arquivos Markdown (padrão: `content/posts`)                                   |
| `--target_dir`           | Diretório de saída para os arquivos traduzidos (padrão: `traductions_en`)                                    |
| `--source_lang`          | Idioma de origem (padrão: `fr`)                                                                                  |
| `--target_lang`          | Idioma de destino (padrão: `en`)                                                                                   |
| `--model`                | Modelo específico a usar                                                                                  |
| `--eco`                  | Usar modelos econômicos                                                                              |
| `--use_mistral`          | Usar a API Mistral AI                                                                                     |
| `--use_claude`           | Usar a API Claude                                                                                         |
| `--use_gemini`           | Usar a API Gemini                                                                                         |
| `--use_grok`             | Usar a API xAI (Grok) — requer `XAI_API_KEY`                                                           |
| `--use_codex`            | Usar a CLI Codex na cota da assinatura ChatGPT                                                    |
| `--use_grok_cli`         | Usar a CLI Grok na cota da assinatura Grok                                                        |
| `--use_antigravity`      | Usar a CLI Antigravity (`agy`) na cota da assinatura Google AI Pro ou Ultra                       |
| `--use_claude_code`      | Usar a CLI Claude Code (`claude -p`) na cota da assinatura Claude Pro ou Max                      |
| `--use_opencode`         | Usar OpenCode (código aberto) com o provedor configurado no OpenCode; exige `--model provider/modèle` |
| `--use_openrouter`       | Usar OpenRouter — requer `OPENROUTER_API_KEY` e `--model fournisseur/modèle`                          |
| `--force`                | Forçar retradução                                                                                       |
| `--keep_filename`        | Manter o nome de arquivo original                                                                          |
| `--news`                 | Modo notícias: protege citações em EN, gerencia bandeiras por idioma                                      |
| `--add_translation_note` | Adicionar uma nota de tradução                                                                                |
| `--note_position`        | Posição da nota: `top`, `bottom` (padrão) ou `both`                                                     |
| `--note_format`          | Formato da nota: `legacy` (padrão, parágrafo em negrito) ou `marker`                                            |
| `--include_model`        | Incluir o nome do modelo no arquivo de saída                                                            |
| `--reasoning_effort`     | Esforço de raciocínio GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh`                                         |

As nove flags `--use_*` são mutuamente exclusivas: combinar duas é
recusado.

## Provedores

### Por API: OpenAI, Mistral, Claude, Gemini, Grok

```bash
aipmt --source_dir content/fr --target_dir content/en --target_lang en             # OpenAI, défaut
aipmt --use_mistral --source_dir content/fr --target_dir content/es --target_lang es
aipmt --use_claude  --source_dir content/fr --target_dir content/de --target_lang de
aipmt --use_gemini  --source_dir content/fr --target_dir content/ja --target_lang ja
aipmt --use_grok    --source_dir content/fr --target_dir content/pt --target_lang pt
```

`--eco` alterna para o nível econômico de cada provedor.

| Provedor    | Qualidade (padrão)                                                   | Econômico (`--eco`)      |
| ----------- | -------------------------------------------------------------------- | ------------------------- |
| OpenAI      | `gpt-6.1-terra`                                                      | `gpt-6-luna`              |
| Claude      | `claude-sonnet-5-5`                                                  | `claude-haiku-5-5`        |
| Mistral     | `mistral-large-latest`                                               | `mistral-small-latest`    |
| Gemini      | `gemini-4-hydrogen`                                                  | `gemini-3.1-flash-lite`   |
| Codex       | `gpt-6.1-sol` (também `gpt-5.6-sol`, `terra` e `luna` por `--model`) | `gpt-5.6-luna`            |
| Grok API    | `grok-4.7`                                                           | `grok-4.3`                |
| Grok CLI    | `grok-4.7`                                                           | idem — `--eco` sem efeito |
| Antigravity | `gemini-3.8-flash-medium`                                            | `gemini-3.8-flash-low`    |
| Claude Code | `sonnet`, esforço `low`                                               | idem — `--eco` sem efeito |
| OpenCode    | `--model provider/modèle` obrigatório                                | idem — `--eco` sem efeito |
| OpenRouter  | `--model fournisseur/modèle` obrigatório                             | idem — `--eco` sem efeito |

Os padrões seguem a última geração de cada provedor, avaliada
antes de ser adotada: GPT-6 na OpenAI, Gemini 4 Hydrogen no Google,
Grok 4.7 na xAI desde a 1.19.0. Os modelos anteriores continuam aceitos
por `--model` (`gpt-5.6-terra`, `gemini-3.8-flash`, `grok-4.6`…), assim como
Gemini 4 Argon e Carbon, o topo de linha do Google. O aipmt ajusta por conta
própria o esforço de raciocínio dos GPT e dos Grok, desligado em `--eco`, e
`--reasoning_effort` o força; um Gemini recebe sempre o nível mais
baixo que aceitar.
Uma falha temporária da API Gemini (503, 429, tempo limite esgotado) repete
a chamada até três vezes, após 10, 20 e depois 40 segundos. Uma tentativa
que permaneça sem resposta é abandonada após 5 minutos e, em seguida, repetida
da mesma forma: um servidor mudo faz o segmento falhar em cerca de vinte minutos,
no máximo, em vez de bloquear indefinidamente.

### Na assinatura ChatGPT: `--use_codex`

Controla a CLI oficial do Codex: a tradução é debitada da cota da
assinatura ChatGPT, sem chave de API nem cobrança por uso.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- O binário é procurado em `CODEX_BIN`, depois no `PATH`, depois no pacote
  `openai-codex-cli-bin`. `~/.codex/auth.json` nunca é lido.
- `OPENAI_API_KEY` e `CODEX_API_KEY` são removidas do ambiente do
  subprocesso: uma chave presente nunca faz alternar para a API.
- Cada segmento custa pelo menos uma "mensagem" da janela de 5 horas — duas
  se a validação falhar e ele for repetido. A OpenAI anuncia, como
  estimativa, 250-2.000 mensagens/5 h para `gpt-5.6-luna` (`--eco`) e
  10-100 para `gpt-5.6-sol` em um plano Plus.
- `--model gpt-5.6-sol`, o padrão até a 1.16.3, `--model gpt-5.6-terra`
  e `--model gpt-5.6-luna` também funcionam pela assinatura.
- Um erro 429 do servidor não faz perder o arquivo: o Codex reconecta sozinho,
  o aipmt aguarda o fim do ciclo e, se o 429 persistir, o segmento
  recomeça após 30 e depois 60 segundos. Um modelo ao qual a conta não tem direito retorna um 400 "model is
  not supported when using Codex with a ChatGPT account".
- Mais lento que uma API, e a diferença aumenta com o tamanho do documento: neste README,
  6 min e 46 s por idioma em mediana com `gpt-5.6-sol`, contra 36 s para
  `gemini-3.7-flash`.
- Recusado em CI (`CI` ou `GITHUB_ACTIONS` definido): a assinatura autentica-se
  por um arquivo de sessão pessoal, que não deve estar em um runner
  compartilhado.
- Variáveis: `CODEX_BIN`, `CODEX_TIMEOUT` (segundos por segmento, padrão 600).

### Na assinatura Grok: `--use_grok_cli`

Mesmo princípio com a CLI oficial Grok Build, na assinatura SuperGrok ou
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
```

- **Isolamento mais fraco que o Codex.** O sandbox de SO do Grok não funciona
  em muitas máquinas Linux recentes (AppArmor, sockets de runtime
  de contêiner), e um perfil que não pode ser aplicado inicia sem confinamento em
  silêncio. Por isso, o script não solicita nenhum perfil por padrão, avisa sobre isso e
  apoia-se nas regras de `--deny` da CLI, incluindo o catch-all `*` — a única
  camada que se recusa a iniciar em vez de remover a proteção sem avisar.
  `GROK_TRANSLATE_SANDBOX=read-only` exige o sandbox de SO, e a inicialização
  falha se a máquina não puder atendê-lo.
- A cota é semanal, compartilhada com Chat, Imagine e Voice, e nenhum
  comando permite consultá-la: um lote pode consumir o uso conversacional
  sem aviso prévio.
- Variáveis: `GROK_BIN`, `GROK_HOME` (diretório da CLI, padrão `~/.grok`),
  `GROK_TIMEOUT` (padrão 900), `GROK_TRANSLATE_SANDBOX`.

### Na assinatura Google: `--use_antigravity`

Mesmo princípio com `agy`, a CLI oficial do Antigravity: para quem assina Google
AI Pro ou Ultra, a tradução é debitada da cota da assinatura em vez
de ser cobrada por token. Esse é o único caminho para essa cota: a Gemini CLI não
atende mais essas contas desde 18 de junho de 2026
([comunicado](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
e o SDK do Antigravity aceita apenas uma chave de API ou um projeto do Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Nenhuma via paga permanece aberta.** O agy recebe do seu
  ambiente apenas uma lista fechada de variáveis — `PATH`, idioma e fuso horário,
  terminal, identidade, proxies e certificados, barramento de sessão — e nenhuma chave:
  várias de suas variáveis alternam uma chamada sem exibir nada (medido:
  uma envia o documento para um gateway de terceiros, outra para um projeto
  faturado do Google Cloud), e uma lista de bloqueio sempre deixava passar algo a cada revisão.
  Antes de qualquer segmento, `agy -p /config`, que não consome cota, deve mostrar
  os créditos de IA pagos desativados, sem chave de API nem projeto do Google Cloud — uma
  configuração ausente é tratada como recusa —, caso contrário nada é traduzido; o log de cada
  chamada deve em seguida confirmar a assinatura (`authMethod=consumer`), sob pena de
  a resposta ser recusada.
- **Isolamento.** Cada chamada é executada em um diretório pessoal privado e
  descartável, com um agente de tradução sem ferramentas: suas configurações, regras,
  plugins, servidores MCP e hooks do agy não entram ali, nada é adicionado ao seu
  histórico e a conexão permanece no chaveiro, que o aipmt nunca lê.
  Um agente não encontrado faz o agy recorrer silenciosamente ao seu agente de programação
  e ferramentas: uma linha inteira do log deve confirmar o agente correto — um
  documento que cite essa mensagem não a substitui —, caso contrário haverá recusa.
- **Plataformas**: Linux, em uma sessão que possua um chaveiro (barramento de sessão
  D-Bus, Secret Service); macOS é aceito, embora não tenha sido medido lá. Recusado
  no Windows, onde o agy não lê as variáveis que isolam cada chamada, e
  no Linux sem barramento de sessão — sessão SSH, contêiner, servidor: nesses casos, o agy
  guarda seu token em um arquivo em `~/.gemini`, que o isolamento oculta. A
  recusa ocorre antes de qualquer inicialização, com sua justificativa, em vez de um minuto
  de espera por um código de login.
- **Modelos**: os de `agy models`. Os Gemini trazem o esforço no próprio nome
  (`gemini-3.8-flash-medium`…): um nome sem sufixo é recusado antes da chamada,
  e `--reasoning_effort` não tem efeito. Por padrão `gemini-3.8-flash-medium`,
  e `gemini-3.8-flash-low` em `--eco`, desde que o agy deixou de oferecer o Gemini 3.7
  Flash; a campanha que definiu o padrão está
  descrita em [Medições detalhadas](#medições-detalhadas). O Gemini 4 Hydrogen
  (`gemini-4-hydrogen-low`…) compartilha a cota do 3.8 Flash e consome
  mais: 0,95 ponto da janela de 5 horas para este README no esforço
  médio, contra 0,32. Claude e GPT-OSS
  possuem cota própria, bem menor: cerca de 1% da janela de
  5 horas por chamada medida, contra 0,05% no Flash. O Gemini 4 Argon tem a
  sua própria, semanal: este README consome 1,35% dela.
- **Cota**: por grupo, uma janela de 5 horas e uma semanal,
  proporcional ao custo em tokens. Medido na conta do autor: cerca de
  16 pontos da janela de 5 horas por milhão de caracteres de origem em
  `gemini-3.8-flash-medium`, 14 em `gemini-3.7-flash-medium` e 7 a 8 no
  esforço baixo — um README de 40.000 caracteres custa, portanto, pouco mais de meio
  ponto. O limite semanal, por sua vez, depende do nível da conta. As tentativas seguem
  o que o agy declara como passível de repetição; caso contrário, uma janela esgotada nunca
  é repetida: ela faz falhar cada arquivo até a reinicialização
  exibida por `/usage`.
- **Mais lento que a API**: no artigo denso de medições, 3 min e 59 s por
  idioma em mediana no `gemini-3.8-flash-medium` e 3 min e 14 s no
  `gemini-3.7-flash-medium`, contra 1 min e 18 s para o Gemini 3.7 Flash via API.
- **Interrupção**: Ctrl-C, ou fechar o terminal, encerra o agy junto com o
  comando em vez de deixá-lo concluir seu ciclo consumindo sua cota; o mesmo se
  aplica a Codex, Grok CLI e OpenCode. Sob o `nohup`, a tradução continua.
- Recusado em CI (`CI` ou `GITHUB_ACTIONS` definido): o login reside em um
  chaveiro pessoal. Em um runner, use `--use_gemini` com `GOOGLE_API_KEY`.
- Variáveis: `AGY_BIN` (caso contrário o `PATH`, depois `~/.local/bin/agy`),
  `AGY_TIMEOUT` (segundos por segmento, inicialização inclusa, padrão 900).

**Termos de uso: é a sua conta que está em jogo.** Os
[termos do Antigravity](https://antigravity.google/terms) (seção 6) e seu
[FAQ](https://antigravity.google/docs/faq/) proíbem o acesso ao serviço
por meio de software de terceiros utilizando o login do Antigravity — Claude Code,
OpenClaw e OpenCode são citados lá —, sob pena de suspensão da conta. O aipmt
não lê nem reutiliza o token: ele executa o binário oficial no
[modo headless](https://antigravity.google/docs/cli/headless/) que o Google
documenta para scripts e CI. Um membro do Google considerou "padrão"
executar o `agy -p` a partir de um script local para trabalho pessoal
([fórum oficial, 25 de setembro de 2026, resposta sem valor contratual](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
nenhum texto oficial define o caso de uma ferramenta distribuída como esta.

**Apenas documentos públicos.** De acordo com a seção 5 dos mesmos termos, as
interações — prompts, respostas, metadados — podem ser usadas para aprimorar os
produtos e o aprendizado de máquina do Google e podem ser revisadas por
humanos, mesmo em assinaturas pagas. A desativação é feita pela configuração
`enableTelemetry`, de efeito não documentado, que o aipmt não define; suas configurações
do agy não são levadas para o ambiente isolado. Não envie nada confidencial por aqui.

### Na assinatura Claude: `--use_claude_code`

Mesmo princípio com `claude`, a CLI oficial do Claude Code, no modo `-p`: para
quem paga o Claude Pro ou Max, a tradução é descontada da cota da
assinatura em vez de ser cobrada por token. Não confundir com
`--use_claude`, a API da Anthropic, cobrada por uso.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Nenhuma via paga permanece aberta, e cada chamada prova isso.** O Claude
  Code recebe do seu ambiente apenas uma lista fechada de variáveis — nenhuma
  chave de API, nenhum token, nenhum provedor de nuvem, nenhum marcador da sessão do Claude Code
  de onde o aipmt teria sido iniciado. Antes do primeiro segmento, `claude auth status` deve
  mostrar a conexão da assinatura, sem chave do Console, e `/usage`, que não consome
  cota, deve atestá-lo; cada chamada o atesta, por sua vez, em seu
  evento de inicialização, caso contrário a resposta é recusada.
- **Desative o «extra usage»** (claude.ai, Configurações → Uso) para
  que o custo zero se mantenha: ativado, ele assume o controle de uma janela esgotada e
  cobra sem exibir erro. O aipmt interrompe a tradução assim que o relatório
  de cota de uma chamada o sinaliza, mas essa chamada já terá sido contabilizada.
- **Cota compartilhada com suas sessões do Claude Code.** Cada chamada relata
  o uso das janelas de 5 horas e da semana; acima de 80%
  (`AIPMT_CLAUDE_MAX_UTILIZATION`), nenhum segmento adicional é iniciado, para
  não esgotar o que é necessário para o seu trabalho.
- **Isolamento.** Cada chamada é executada sem ferramentas, em um diretório privado e
  descartável, em modo sem personalização: nem seus `CLAUDE.md`, nem seus plugins,
  hooks, servidores MCP ou configurações são carregados, e nada é mantido da
  sessão. Os anexos são bloqueados: um `@chemin` em seu documento
  permanece como texto e não abre nenhum arquivo (medido).
- **Modelos**: `sonnet` por padrão, no esforço `low`, e também em `--eco`:
  `--eco` não muda nada neste caminho. Medidos nos mesmos documentos, `haiku`
  é duas vezes mais lento — ele raciocina sem que seja possível impedi-lo — por
  um custo ligeiramente menor, e `opus` recusa conteúdos de biologia (ponto
  seguinte). Ambos continuam acessíveis por `--model`; esses aliases acompanham o
  modelo mais recente de sua família. `fable` e as variantes `[1m]` são recusados,
  pois utilizam créditos pagos. `--reasoning_effort` ajusta o esforço,
  do qual uma tradução não aproveita nada: o raciocínio medido é nulo ou quase nulo.
- **O Opus recusa determinados conteúdos de biologia.** Suas proteções são mais
  rigorosas que as do Sonnet, e a mensagem de erro da Anthropic alerta que elas
  «can sometimes flag biology-research-adjacent work». Medido: uma nota de
  monitoramento sobre 279 moléculas geradas fez com que o artigo fosse recusado em todos os quatorze
  idiomas. Nada é gravado: o aipmt recusa a resposta truncada, identifica as
  proteções e recomenda `--model sonnet`.
- Recusado em CI (`CI` ou `GITHUB_ACTIONS` definido) e no Windows (não medido).
- Variáveis: `AIPMT_CLAUDE_BIN` (caso contrário, o `PATH`, depois `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (segundos por segmento, padrão 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (padrão 0.8), `CLAUDE_CONFIG_DIR` (a conta do
  Claude Code, nunca obtida de um `.env` de projeto); diretórios de trabalho sob
  `XDG_CACHE_HOME/aipmt/claude-code` (padrão `~/.cache`).

**Termos de uso: é a sua conta que está em jogo.** A
[página jurídica do Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
não impede «an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription»: é isso que o aipmt faz, ao executar o
binário oficial e nunca ler o token. No entanto, a Anthropic «does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users», prefere a chave de API para ferramentas
de terceiros, «including open-source projects», e reserva-se o direito de cobrar seu
uso em créditos pagos
([ajuda do Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Nenhum texto resolve o caso de uma ferramenta distribuída que executa o binário.

**Dados**: nas contas Free, Pro e Max, o treinamento dos modelos
também se aplica ao Claude Code quando a configuração de privacidade o autoriza
([página de dados](https://code.claude.com/docs/en/data-usage)). O aipmt não mantém
nenhuma transcrição local (`--no-session-persistence`). Não processe
nada confidencial por aqui.

### Para o provedor de sua escolha: `--use_opencode`

O [OpenCode](https://opencode.ai) é um agente de código de código aberto (MIT) que
roteia para os provedores configurados nele: chave de API, assinatura,
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

`--model` é obrigatório: sem ele, o OpenCode voltaria para um modelo gratuito
cujas mensagens podem ser usadas para treinamento, e essa escolha não é feita no
seu lugar.

Isolamento a cada chamada:

- uma configuração inline, com prioridade sobre a sua, define um agente `aipmt`
  cujas ferramentas são todas recusadas (`permission: { "*": "deny" }`), compartilhamento de
  sessão desativado, `--pure`, nunca `--auto`;
- diretório de trabalho descartável e vazio, com `OPENCODE_DISABLE_PROJECT_CONFIG` e
  `OPENCODE_DISABLE_CLAUDE_CODE` inseridos — sem eles, o OpenCode injeta no
  prompt o `AGENTS.md` do diretório atual e `~/.claude/CLAUDE.md`. O
  `~/.config/opencode/AGENTS.md` global continua sendo injetado, o OpenCode não permite
  ignorá-lo;
- contrato de saída: código de retorno 0, nenhum evento `error`, nenhuma chamada
  de ferramenta, última etapa em `stop`, texto não vazio, e o agente `aipmt`
  efetivamente carregado — um `--agent` desconhecido não faz o OpenCode falhar, ele
  simplesmente volta em silêncio para o agente de codificação;
- nenhuma chave de `aipmt` é transmitida, exceto `OPENCODE_API_KEY`, a própria chave
  do OpenCode. Os provedores são configurados no OpenCode, não no
  `.env` do `aipmt`.

Observações:

- Os modelos gratuitos do Zen são instáveis, com limites não documentados, e
  suas mensagens podem servir para treinamento: adequados para documentação
  pública, não para conteúdo privado.
- Um modelo local deve oferecer pelo menos 16 k tokens de contexto, já que os segmentos
  têm até 16.000 caracteres. O Ollama frequentemente configura 4.096: utilize
  um `Modelfile` com `PARAMETER num_ctx 32768`.
- `--eco` não tem efeito; `--reasoning_effort` é transmitido inalterado como
  `--variant` do OpenCode.
- O OpenCode registra cada sessão em `~/.local/share/opencode/`.
- Variáveis: `OPENCODE_BIN` (caso contrário, o `PATH`, depois `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (segundos por segmento, padrão 600). `OPENCODE_CONFIG`
  é repassado inalterado ao OpenCode.

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
modelos, e que um Modelfile não consegue desativar. Medido em uma frase de
seis palavras: 919 tokens de reflexão e 68 segundos sem a opção, 9 tokens com ela.

### Para mais de 400 modelos: `--use_openrouter`

O OpenRouter é um roteador cobrado por uso, com crédito unificado, diante de
modelos hospedados por terceiros — incluindo os modelos abertos chineses que nenhum
outro provedor disponibiliza aqui.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` é obrigatório. Um pré-voo, executado antes de qualquer cobrança, resolve
duas particularidades do roteamento:

- **Um mesmo modelo é servido por dezenas de provedores de hospedagem com limites
  diferentes** — no `z-ai/glm-5.3-flash`, são 23 provedores de hospedagem, incluindo um com limite de
  2.048 tokens de saída. O pré-voo lê `/api/v1/models/{modèle}/endpoints`,
  descarta os provedores abaixo de 8.000 tokens de saída ou com status degradado, e
  fixa os demais com `allow_fallbacks: false`.
- **O raciocínio é cobrado pela tarifa de saída** — 107 tokens contra 2 em
  uma resposta «OK» de `z-ai/glm-5.2`. Ele fica desativado por padrão; os modelos
  que o exigem recebem o menor nível de esforço que aceitarem, já que o padrão do
  catálogo pode saturar a saída antes do término da tradução.
  `--reasoning_effort` permanece prioritário.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- A janela de contexto vem do catálogo. Um modelo abaixo de 16.400 tokens é
  recusado antes de qualquer chamada: 8.400 para o prompt e o segmento, e no mínimo 8.000
  de saída.
- Um slug ausente do catálogo, um catálogo inacessível ou a ausência
  de um provedor que suporte o limite interrompem o comando.
- `finish_reason=length` com uma saída vazia representa um orçamento consumido pelo
  raciocínio, não um truncamento: a mensagem faz essa distinção.
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
seguida por uma citação em negrito: legível no GitHub, utilizável no build por um
plugin do remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Medições detalhadas

Todas as medições são traduções realmente executadas com `aipmt`, para
quatorze idiomas: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Gravados** conta os arquivos que as validações deixaram passar; **Sem
divergências** aqueles em que `scripts/compare_structure.py` não detecta nada — mesma quantidade de
seções, subtítulos, links, URLs distintas, blocos de código,
códigos inline, linhas de tabela, blocos de citação e palavras em negrito.

«Sem divergências» significa «nada detectado», e não «idêntico»: o comparador
conta elementos sem ler seu conteúdo. Ele não sinaliza um título de
nível 4 removido, nem o texto de um código inline substituído, nem uma bandeira
trocada, nem um link interno gerado com um parêntese a mais,
`[texte]((#ancre))`, que não leva a lugar nenhum — e não avalia o
idioma.

### Artigo de monitoramento denso, modo `--news`

Uma edição do [monitoramento de IA de jls42.org](https://jls42.org/fr/news):
589 linhas, 140 links, 21 seções, 3 citações em inglês protegidas. Campanha
de 4 e 5 de setembro de 2026.

| Modelo                                          | Acesso             | Gravados | Sem divergências | Mediana/idioma |
| ----------------------------------------------- | ------------------ | -------- | ---------------- | -------------- |
| `gemini-3.7-flash`                              | API Google         | 14/14    | ✅ **14/14**     | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | assinatura Google  | 14/14    | ✅ **14/14**     | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | assinatura Google  | 14/14    | ✅ **14/14**     | 3 min 14 s     |
| `claude-sonnet-5-5`                             | API Anthropic      | 14/14    | ✅ **14/14**     | 3 min 37 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | assinatura ChatGPT | 14/14    | ✅ **14/14**     | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14    | ✅ **14/14**     | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14    | ✅ **14/14**     | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | assinatura Claude  | 14/14    | ⚠️ 13/14         | 6 min 49 s     |
| `claude-sonnet-5`                               | API Anthropic      | 14/14    | ⚠️ 11/14         | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | assinatura Claude  | 14/14    | ⚠️ 11/14         | 15 min 54 s    |
| `claude-haiku-5-5`                              | API Anthropic      | 14/14    | ⚠️ 11/14         | 2 min 54 s     |
| `claude-haiku-4-5`                              | API Anthropic      | 14/14    | ⚠️ 7/14          | 6 min 00 s     |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14    | ❌ 11/14         | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14    | ❌ 8/14          | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | local              | 10/14    | ❌ 7/14          | 12 min 39 s    |
| `mistral-large-latest`                          | API Mistral        | 11/14    | ❌ 5/14          | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14     | ❌ 3/14          | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | assinatura Grok    | 1/14     | ❌ 1/14          | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | assinatura Claude  | 0/14     | ❌ 0/14          | —              |

O Grok foi remedido em 9 de setembro em outra edição do mesmo monitoramento
(356 linhas): 9 idiomas gravados de 14, 8 sem divergências. É esse número que
figura na tabela principal. Três campanhas interrompidas não foram
pontuadas: `qwen3.5-27b` (9 idiomas) e `kimi-k2.6` (4) por falta de créditos,
`z-ai/glm-5.3-flash` cujas duas falhas se originaram de uma configuração de raciocínio
que o provedor corrigiu desde então. As linhas do OpenRouter foram medidas com as
configurações padrão do roteador, antes de `--use_openrouter`; `z-ai/glm-5.2`,
remedido com o provedor fornecido, alcança o mesmo 14/14. Os números foram
recalculados em 10 de setembro com o comparador atual: `qwen3.8-flash` e
`qwen3.7-flash` ganham, cada um, um idioma em relação à primeira
publicação, os demais permanecem inalterados.

As linhas de `--use_antigravity` foram medidas em 26 de setembro no mesmo
artigo, quatro traduções em paralelo: `gemini-3.7-flash-medium` pela manhã,
`gemini-3.8-flash-medium` à tarde. Em inglês, cada um removeu por conta própria
as três linhas de tradução em francês sob as citações, sem inventar
bandeiras, e as citações em inglês permaneceram intactas: a limpeza de fallback não
precisou intervir. Em `--eco` (`gemini-3.7-flash-low`), em apenas quatro idiomas
(en, ja, ar, hi): 4 gravados de 4, todos sem divergências, com mediana de 1 min 52 s.
Contraprova no mesmo dia em uma edição mais recente do monitoramento,
a de 25 de setembro (438 linhas, 2 citações em inglês), traduzida fora do
blog pelo `gemini-3.7-flash-medium`: 14 gravados de 14, todos sem divergências, de 87 a
128 s por idioma.

As linhas de `--use_claude_code` foram medidas em 26 de setembro no mesmo
artigo, quatro traduções em paralelo, no esforço `low`. Com `sonnet`, as
citações em inglês permaneceram intactas nos quatorze idiomas e, em inglês, o
modelo removeu por conta própria as linhas de tradução em francês, sem inventar
bandeiras. O `opus` não gravou nenhum idioma: em cada um deles, suas proteções
interromperam a resposta no último segmento, por causa de uma nota sobre 279 moléculas
geradas para um sítio de ligação. Enviada isoladamente, essa nota é recusada ao
título da categoria «bio»; o `sonnet` traduziu-a em todos os casos. O `haiku` grava
os quatorze idiomas; em três deles (en, pl, ro), o título de uma seção mudou do
nível 2 para o nível 1. Ele raciocina sem que seja possível impedi-lo — 61% de
seus tokens de saída —, resultando em mais que o dobro do tempo de `sonnet`.

As linhas de `claude-sonnet-5-5`, `claude-haiku-5-5` e `claude-haiku-4-5` foram
medidas em 18 de outubro pela API da Anthropic, no mesmo artigo, quatro
traduções em paralelo por modelo. O Sonnet 5.5 recusa que se desative sua
reflexão: o aipmt envia-lhe a configuração mais baixa que ele aceita, e suas
respostas não trazem nenhuma. Ele grava os quatorze idiomas sem divergências e sem
reprocessar nenhum segmento; em inglês, removeu por conta própria as linhas de
tradução em francês, sem inventar bandeiras, e as citações em inglês permaneceram
intactas em toda parte. O Haiku 5.5 é medido com sua reflexão adaptativa: com a reflexão
desativada, ele deixava parágrafos inteiros em francês, o que a validação recusa —
3 idiomas gravados de 14. Ambos os modelos Haiku esbarram na mesma nota: o Haiku 5.5
altera o nível de seu título ou o duplica em japonês, coreano e
chinês; o Haiku 4.5 o muda para o nível 1 em sete idiomas e o mantém em
francês em japonês. O Haiku 4.5 custa 3,67 $ para os dois documentos nos
quatorze idiomas, o Haiku 5.5 0,57 $, e o Sonnet 5.5 9,21 $.

### README deste projeto, Markdown padrão

Revisão congelada em 9 de setembro de 2026: 785 linhas, 285 códigos inline, 40
fechamentos de blocos, 89 linhas de tabela. Quatro traduções em paralelo.

| Modelo                                          | Escritas | Sem desvios | Mediana/idioma | O que difere                                                             |
| ----------------------------------------------- | -------- | ----------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14    | ✅ 14/14    | 1 min 43 s     | nada                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14    | ✅ 14/14    | 1 min 48 s     | nada                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14    | ✅ 14/14    | 4 min 02 s     | nada para o comparador; links internos duplicados (en)                   |
| `claude-sonnet-5-5`                             | 14/14    | ✅ 14/14    | 1 min 18 s     | nada                                                                     |
| `claude-haiku-4-5`                              | 14/14    | ✅ 14/14    | 2 min 06 s     | nada                                                                     |
| `gemini-3.7-flash`                              | 14/14    | ⚠️ 13/14    | 36 s           | uma palavra em negrito (ja)                                              |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14    | ⚠️ 13/14    | 1 min 22 s     | uma palavra em negrito (ko)                                              |
| `sonnet` (`--use_claude_code`)                  | 14/14    | ⚠️ 13/14    | 2 min 20 s     | uma linha de tabela colada à anterior (ar)                               |
| `claude-sonnet-5`                               | 14/14    | ⚠️ 12/14    | 2 min 56 s     | um link (sv), uma palavra em negrito (zh)                               |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14    | ⚠️ 12/14    | 6 min 46 s     | uma palavra em negrito (ar, ja)                                          |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14    | ⚠️ 11/14    | 2 min 34 s     | uma palavra em negrito (hi, ja, ko)                                      |
| `qwen/qwen3.7-flash`                            | 14/14    | ⚠️ 10/14    | 2 min 17 s     | 40 códigos inline adicionados em árabe; negrito (hi, ja, ko)             |
| `claude-haiku-5-5`                              | 12/14    | ❌ 12/14    | 1 min 14 s     | 2 idiomas recusados (ar, hi): códigos inline perdidos no retorno         |
| `mistral-large-latest`                          | 14/14    | ❌ 1/14     | 2 min 44 s     | uma seção perdida (ar, hi, ko); blocos de código adicionados (ja, ko, ro, zh) |

Duas campanhas interrompidas não estão listadas: Grok, sessão de CLI expirada
após doze idiomas (onze sem desvios), e `qwen3.8-flash`, HTTP 429 do seu
provedor de hospedagem após dois. `opencode/mimo-v2.5-free` e `ollama/gpt-oss-20b-32k`
não foram remedidos nesta revisão; naquela de 4 e 5 de setembro,
277 linhas mais curta, cada um escreveu 9 traduções de 14, sendo 7
e 1 sem desvios.

As linhas `--use_antigravity` e `--use_claude_code` não foram medidas na
revisão congelada, mas em 26 de setembro na publicada com a 1.14.0 — e
as linhas `claude-sonnet-5-5`, `claude-haiku-5-5` e `claude-haiku-4-5` em 18 de
outubro, na mesma: 600 linhas, 257 códigos inline, 30 fechamentos de blocos, 85
linhas de tabela. Mais
curta em 185 linhas, ela não se compara termo a termo com as outras linhas;
essas linhas, por sua vez, comparam-se entre si. Nos links internos, que o
comparador não verifica, o `gemini-3.8-flash-medium` os manteve intactos nos
quatorze idiomas, o `gemini-3.7-flash-medium` os quebrou em italiano;
`sonnet` e `opus` os mantiveram intactos em todos, `haiku` os duplicou em
inglês; `claude-sonnet-5-5` e `claude-haiku-4-5` os mantiveram intactos nos
quatorze idiomas, `claude-haiku-5-5` nos doze que escreveu.

### Quatro READMEs de projetos conhecidos

FastAPI, Ollama, tldr-pages e Vue.js, obtidos diretamente do GitHub — documentos
mais fáceis do que os dois anteriores. A campanha visava os modelos
com dificuldades; o Gemini serve aqui como ponto de comparação.

| Modelo                    | Escopo                     | Escritas | Sem desvios  |
| ------------------------- | -------------------------- | -------- | ------------ |
| `gemini-3.7-flash`        | 4 projetos × 14 idiomas    | 56/56    | ✅ **55/56** |
| `opencode/mimo-v2.5-free` | 4 projetos × 14 idiomas    | 55/56    | ❌ 47/56     |
| `grok-4.6` (assinatura)   | 4 projetos × ar, hi, ja, zh| 16/16    | ❌ 14/16     |
| `ollama/gpt-oss-20b-32k`  | 4 projetos × ar, hi, ja, zh| 15/16    | ❌ 9/16      |

### O que estas medições não são

- **Não são uma classificação exaustiva**: apenas o OpenRouter oferece mais de quatrocentos
  modelos, dos quais cerca de quinze foram medidos.
- **Durações indicativas**: de três a seis traduções em paralelo dependendo
  das campanhas, e a taxa de transferência de um provedor varia ao longo do dia.
- **Observações datadas**: os modelos mudam sob o mesmo nome, e os seus
  documentos não são os nossos.

Para repetir a medição nos seus documentos, em uma cópia congelada do arquivo:

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
regeneradas com `./regen_translations.sh --force` — Codex e `gpt-6.1-sol` na
assinatura do ChatGPT por padrão, quatro em paralelo. `REGEN_PROVIDER` e
`REGEN_MODEL` mudam o caminho: `antigravity` permanece em uma assinatura, a
do Google, e passa sem exceção; uma API cobrada (`openai`, `gemini`,
`grok`, `openrouter`) é recusada sem `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` limita cada job (600 s, 1.800 s no Codex e
Antigravity). Os detalhes das ferramentas estão em `CLAUDE.md`.

## Projetos que utilizam este script

- **[jls42.org](https://jls42.org)** — blog pessoal publicado em 15 idiomas. O seu
  [monitoramento diário de IA](https://jls42.org/fr/news) é traduzido diariamente
  por esta ferramenta e serve como documento de referência para as medições acima.

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licença

GNU GENERAL PUBLIC LICENSE Versão 3. Consulte [LICENSE](https://github.com/jls42/ai-powered-markdown-translator/blob/main/LICENSE).

## Aviso legal

Este programa é distribuído **sem nenhuma garantia**, nos termos das
seções 15 e 16 da GPL v3: fornecido "no estado em que se encontra", sem garantia de
comercialização ou adequação a uma finalidade específica, e o seu autor não pode ser
responsabilizado por danos resultantes do seu uso. O texto da
licença prevalece sobre este resumo.

- **Revise antes de publicar.** As proteções cobrem blocos de código,
  código inline, URLs, âncoras e citações do modo `--news` — não os
  títulos, nem as tabelas, nem o front matter, nem o sentido das suas frases.
- **Os seus documentos são enviados para o provedor escolhido**, sob os seus termos
  de uso e política de dados. Alguns modelos gratuitos podem
  reutilizar as suas interações para treinamento, e os termos da Antigravity
  permitem que o Google as reutilize e as submeta à revisão humana,
  incluindo assinaturas pagas; um modelo local é a única forma de garantir
  que nenhum dado saia da sua máquina.
- **As chamadas de API são cobradas de você.** Este programa não limita os
  gastos: um documento longo, uma nova tentativa após falha ou um modelo que raciocina
  muito custam mais.
- **As medições publicadas são observações datadas**, não garantias.

Os nomes de produtos e empresas citados pertencem aos seus respectivos
proprietários. Este projeto não é afiliado a nenhum deles.

**Artigo traduzido do fr para o pt com gemini-3.8-flash-medium.**
