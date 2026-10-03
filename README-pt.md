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

Traduz arquivos Markdown de um idioma para outro preservando a estrutura:
blocos de código, código inline, URLs, âncoras, tabelas e front matter. Onze
formas de chamar um modelo — cinco APIs, quatro assinaturas sem cobrança por
uso, dois roteadores — e uma medição publicada do que cada modelo realmente
preserva.

## Em resumo

- **Onze caminhos de provedor**: APIs da OpenAI, Mistral, Claude, Gemini e Grok;
  assinaturas do ChatGPT (Codex), Grok, Google (Antigravity) e Claude (Claude
  Code) sem cobrança por uso; roteadores OpenCode (código aberto, gratuito ou local) e OpenRouter
  (mais de 400 modelos).
- **Nada corrompido por causa de um token perdido**: blocos de código, código
  inline, URLs, âncoras e citações são substituídos por tokens antes da chamada
  e verificados no retorno. Se faltar algum, o arquivo não é gravado.
- **Documentos longos**: segmentação de acordo com a janela de contexto do modelo.
- **Modo `--news`**: citações em inglês protegidas e sinalizadores gerenciados
  por idioma, para artigos de monitoramento.
- **Modo `--eco`**: modelos rápidos e mais econômicos.
- **Nota de tradução** opcional, no topo, no rodapé ou em ambos.

## Instalação

```bash
pip install ai-powered-markdown-translator     # ou : pipx install ai-powered-markdown-translator
aipmt --help                                   # ou : python -m aipmt --help
```

Python 3.10 ou mais recente. Para instalar a partir do repositório, consulte
[Contribuir](#contribuir).

## Configuração

As chaves são lidas em três locais, do de maior prioridade ao de menor; cada um
apenas preenche o que o anterior deixa vazio.

|     | Onde                                          | Para que                              |
| --- | --------------------------------------------- | ------------------------------------- |
| 1   | Variáveis de ambiente                         | CI, contêineres, substituição pontual |
| 2   | `.env` do diretório atual (ou de um pai) | uma chave específica de um projeto    |
| 3   | `~/.config/aipmt/.env`                        | instalado uma vez, vale para tudo     |

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

`GEMINI_API_KEY` é aceito no lugar de `GOOGLE_API_KEY`. O arquivo do usuário
segue `XDG_CONFIG_HOME` (apenas caminho absoluto) e `%APPDATA%` no
Windows. Sem chave, o comando lista os três locais.

**O `.env` de um projeto não pode redirecionar chamadas nem escolher o programa
executado.** Ele fornece chaves, nunca um destino ou binário: qualquer
variável em `_BASE_URL`, `_API_BASE`, `_ENDPOINT` ou `_BIN` (`CODEX_BIN`,
`GROK_BIN`, `OPENCODE_BIN`, `AGY_BIN`), `GROK_HOME`, proxies (`HTTP_PROXY`,
`HTTPS_PROXY`, `ALL_PROXY`), repositórios de certificados (`SSL_CERT_FILE`,
`SSL_CERT_DIR`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`) e `XDG_CONFIG_HOME` /
`APPDATA` são ignorados nele, com um aviso. Um repositório clonado não deve
ser capaz de desviar sua chave, nem fazer você executar seu próprio programa na
primeira tradução. Este arquivo também é lido sem interpolação:
`NOM=${OPENAI_API_KEY}` não copia a chave ali. Defina essas variáveis no
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

`document.md` traduzido para espanhol resulta em `document-es.md` em `--target_dir`;
com `--include_model`, `document-es-gpt-5.6-terra.md`. A extensão sempre
se torna `.md` — `article.mdx` resulta em `article-en.md` — exceto com
`--keep_filename`, que preserva o nome original. Uma tradução já existente
é ignorada sem `--force`.

Códigos de saída: `0` se tudo foi concluído com sucesso ou ignorado, `1` se restar algum arquivo
com falha (lista na saída de erro), `2` se o problema for na configuração.
Um arquivo com falha nunca é gravado, mesmo que a própria gravação falhe:
o conteúdo é gravado ao lado e depois renomeado. Basta executar novamente.

## Qual modelo escolher

Medido em dois documentos reais, traduzidos para os mesmos catorze idiomas por
cada modelo. **O número representa a quantidade de idiomas, de catorze, em que a
tradução é gravada e nada difere da fonte.**

| Modelo               | Como acessar                      | Artigo de monitoramento denso | Este README  | O que difere e em quantos idiomas                                                                                                                                  |
| -------------------- | --------------------------------- | ----------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Gemini 3.8 Flash** | assinatura do Google (Antigravity)| ✅ 14/14                      | ✅ 14/14     | nada, em nenhum dos dois documentos                                                                                                                                |
| **Gemini 3.7 Flash** | chave de API do Google            | ✅ 14/14                      | ⚠️ 13/14     | 1 idioma de 14: uma palavra a mais em negrito (ja)                                                                                                                 |
| **Gemini 3.7 Flash** | assinatura do Google (Antigravity)| ✅ 14/14                      | ⚠️ 13/14     | 1 idioma de 14: uma palavra a menos em negrito (ko)                                                                                                                |
| **GPT-5.6 Sol**      | assinatura do ChatGPT ou chave da OpenAI | ✅ 14/14               | ⚠️ 12/14     | 2 idiomas de 14: uma palavra a menos em negrito (ar, ja)                                                                                                           |
| **GLM-5.2**          | chave do OpenRouter               | ✅ 14/14                      | ⚠️ 11/14     | 3 idiomas de 14: uma palavra a menos em negrito (hi, ja, ko)                                                                                                       |
| Claude Sonnet 5      | assinatura do Claude (Claude Code)| ⚠️ 13/14                      | ⚠️ 13/14     | 1 idioma de 14 no artigo: uma palavra a mais em negrito (zh); 1 neste README: uma linha de tabela colada à anterior, oculta na exibição (ar)                        |
| Claude Haiku 4.5     | assinatura do Claude (Claude Code)| ⚠️ 11/14                      | ✅ 14/14     | 3 idiomas no artigo: um título de seção alterado para o nível 1 (en, pl, ro); neste README, nada para o comparador, mas links internos duplicados em inglês         |
| Claude Sonnet 5      | chave de API da Anthropic         | ⚠️ 11/14                      | ⚠️ 12/14     | 3 idiomas no artigo: um bloco de código surgiu (es, de, hi); 2 neste README: um link sem a formatação (sv), uma palavra em negrito (zh)                           |
| Qwen 3.7 Flash       | chave do OpenRouter               | ❌ 8/14                       | ⚠️ 10/14     | 1 idioma recusado no artigo, outros 5 divergiram; neste README, cerca de quarenta palavras colocadas em `code` (ar)                                       |
| Grok 4.6             | assinatura do Grok                | ❌ 8/14                       | não avaliado | 5 idiomas de 14 recusados, por falta de códigos inline e URLs retornados; o holandês diverge em tudo                                                               |
| GPT-OSS 20B          | modelo local (Ollama)             | ❌ 7/14                       | não remedido | 4 idiomas de 14 recusados: o modelo deixou trechos em francês neles, a proteção os interrompeu                                                                     |
| MiMo v2.5 (gratuito) | OpenCode Zen, sem conta           | ❌ 11/14                      | não remedido | 1 idioma recusado; uma seção perdida em polonês                                                                                                                    |
| Mistral Large        | chave de API da Mistral           | ❌ 5/14                       | ❌ 1/14      | **uma seção inteira desaparece**: 1 idioma no artigo (hi), 3 neste README (ar, hi, ko) — e 3 idiomas recusados no artigo                                           |
| DeepSeek V4 Flash    | chave do OpenRouter               | ❌ 3/14                       | não remedido | 10 idiomas de 14 recusados; 37 minutos por idioma                                                                                                                  |
| Claude Opus 5.5      | assinatura do Claude (Claude Code)| ❌ 0/14                       | ✅ 14/14     | o artigo foi recusado em todos os 14 idiomas pelos mecanismos de proteção do Opus, devido a uma nota sobre biologia; nada neste README                                  |

|     | O que o símbolo significa                                                                                                                                                                             |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✅  | os quatorze idiomas traduzidos e nada difere da fonte                                                                                                                                                 |
| ⚠️  | os quatorze idiomas traduzidos; o que difere é a **marcação** — uma palavra em negrito, um `code`, um link que perde os colchetes. Nenhum texto, nenhuma URL, nenhum bloco de código, nenhuma seção está faltando |
| ❌  | pelo menos um idioma não pôde ser traduzido — o arquivo foi recusado, não gravado — **ou** falta conteúdo em um arquivo gravado                                                                      |

O que você precisa saber:

- **Uma tradução recusada não é uma tradução corrompida.** Quando falta um token
  no retorno, o arquivo não é gravado e o idioma conta como recusado. É o que
  acontece com o Grok no artigo: quatro códigos inline e três URLs perdidos logo
  no primeiro segmento, nas cinco escritas não latinas.
- **Um modelo pode recusar um documento inteiro por causa de uma única frase.**
  O Opus 5.5 traduz este README sem nenhuma discrepância, mas nenhum artigo de
  monitoramento: seus mecanismos de segurança interrompem a resposta por causa
  de uma nota sobre biologia. O arquivo não é gravado, e o aipmt explica o motivo.
- **Essa rede de proteção não cobre títulos, tabelas, front matter nem o
  texto.** Um modelo que remove uma seção retorna um arquivo que a ferramenta
  grava sem hesitar — é o caso do Mistral. Esses elementos não podem ser
  substituídos por um token, e as proteções atuais não os verificam;
  `scripts/compare_structure.py` detecta uma seção perdida, mas após o fato.
- **O Grok não tem avaliação neste README**: sua sessão CLI expirou após doze
  idiomas, sendo onze sem discrepâncias. Uma execução interrompida não recebe
  avaliação.
- **A densidade do documento importa mais do que o idioma.** O Grok funciona
  bem em READMEs normais, mas falha em um artigo repleto de links, inclusive em
  holandês.

Datas e documentos: a coluna "Este README" foi medida em 9 de setembro de 2026
em uma revisão congelada deste arquivo (785 linhas, 285 códigos inline, 89
linhas de tabela), modificada desde então — exceto as linhas do Antigravity e do
Claude Code, medidas em 26 de setembro na revisão lançada com a versão 1.14.0,
mais curta (600 linhas, 257 códigos inline, 85 linhas de tabela). A coluna
"Artigo de monitoramento denso" é proveniente dos testes de 4 e 5 de setembro em
um artigo de 589 linhas, exceto a linha do Grok, medida novamente em 9 de
setembro em outra edição do mesmo monitoramento, e as linhas do Antigravity e
Claude Code, medidas em 26 de setembro no mesmo artigo. As tabelas completas,
as durações e o protocolo estão em [Medições detalhadas](#medições-detalhadas).

## Todas as opções

| Opção                    | Descrição                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- |
| `--file`                 | Arquivo Markdown único a traduzir (alternativa a `--source_dir`)                                              |
| `--source_dir`           | Diretório de origem contendo os arquivos Markdown (padrão: `content/posts`)                                   |
| `--target_dir`           | Diretório de saída para os arquivos traduzidos (padrão: `traductions_en`)                                        |
| `--source_lang`          | Idioma de origem (padrão: `fr`)                                                                     |
| `--target_lang`          | Idioma de destino (padrão: `en`)                                                                    |
| `--model`                | Modelo específico a utilizar                                                                                  |
| `--eco`                  | Utilizar os modelos econômicos                                                                                |
| `--use_mistral`          | Utilizar a API Mistral AI                                                                                     |
| `--use_claude`           | Utilizar a API Claude                                                                                         |
| `--use_gemini`           | Utilizar a API Gemini                                                                                         |
| `--use_grok`             | Utilizar a API xAI (Grok) — requer `XAI_API_KEY`                                                             |
| `--use_codex`            | Utilizar a CLI Codex na cota da assinatura do ChatGPT                                                         |
| `--use_grok_cli`         | Utilizar a CLI Grok na cota da assinatura do Grok                                                             |
| `--use_antigravity`      | Utilizar a CLI Antigravity (`agy`) na cota da assinatura do Google AI Pro ou Ultra                    |
| `--use_claude_code`      | Utilizar a CLI Claude Code (`claude -p`) na cota da assinatura do Claude Pro ou Max                       |
| `--use_opencode`         | Utilizar o OpenCode (código aberto) com o provedor configurado no OpenCode; requer `--model provider/modèle`             |
| `--use_openrouter`       | Utilizar o OpenRouter — requer `OPENROUTER_API_KEY` e `--model fournisseur/modèle`                                                |
| `--force`                | Forçar a retradução                                                                                           |
| `--keep_filename`        | Manter o nome do arquivo original                                                                             |
| `--news`                 | Modo notícias: protege citações em EN, gerencia bandeiras por idioma                                          |
| `--add_translation_note` | Adicionar uma nota de tradução                                                                                |
| `--note_position`        | Posição da nota: `top`, `bottom` (padrão) ou `both`                                    |
| `--note_format`          | Formato da nota: `legacy` (padrão, parágrafo em negrito) ou `marker`                            |
| `--include_model`        | Incluir o nome do modelo no arquivo de saída                                                                  |
| `--reasoning_effort`     | Esforço de raciocínio GPT-5.x: `none`/`low`/`medium`/`high`/`xhigh` |

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

| Provedor    | Qualidade (padrão)                                    | Econômico (`--eco`) |
| ----------- | ----------------------------------------------------- | --------------------------- |
| OpenAI      | `gpt-5.6-terra`                                       | `gpt-5.6-luna`             |
| Claude      | `claude-sonnet-5`                                       | `claude-haiku-4-5`             |
| Mistral     | `mistral-large-latest`                                       | `mistral-small-latest`             |
| Gemini      | `gemini-3.7-flash`                                       | `gemini-3.1-flash-lite`             |
| Codex       | `gpt-5.6-sol` (também `terra` e `luna` via `--model`) | `gpt-5.6-luna`             |
| Grok API    | `grok-4.6`                                       | `grok-4.3`             |
| Grok CLI    | `grok-4.6`                                       | `grok-4.5`             |
| Antigravity | `gemini-3.8-flash-medium`                                       | `gemini-3.7-flash-low`             |
| Claude Code | `sonnet`, esforço `low`              | idem — `--eco` sem efeito |
| OpenCode    | `--model provider/modèle` obrigatório                           | idem — `--eco` sem efeito |
| OpenRouter  | `--model fournisseur/modèle` obrigatório                           | idem — `--eco` sem efeito |

### Na assinatura do ChatGPT: `--use_codex`

Controla a CLI oficial do Codex: a tradução é deduzida da cota da
assinatura do ChatGPT, sem chave de API nem cobrança por uso.

```bash
pip install openai-codex-cli-bin   # package officiel OpenAI (~250 Mo), ou : npm install -g @openai/codex
codex login
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
```

- O binário é procurado em `CODEX_BIN`, depois no `PATH`, e em seguida no pacote
  `openai-codex-cli-bin`. `~/.codex/auth.json` nunca é lido.
- `OPENAI_API_KEY` e `CODEX_API_KEY` são removidas do ambiente do
  subprocesso: uma chave presente nunca alterna para a API.
- Cada segmento custa pelo menos uma "mensagem" da janela de 5 horas — duas
  se a validação falhar e houver uma nova tentativa. A OpenAI anuncia, a título
  de estimativa, 250–2.000 mensagens/5 h para `gpt-5.6-luna` (`--eco`) e
  10–100 para `gpt-5.6-sol` em um plano Plus.
- `--model gpt-5.6-terra` e `--model gpt-5.6-luna` também passam pela
  assinatura. Um modelo ao qual a conta não tem direito retorna um erro 400 "model is
  not supported when using Codex with a ChatGPT account".
- Mais lento que uma API, e a diferença aumenta com o tamanho do documento: neste README,
  6 min e 46 s por idioma em mediana com `gpt-5.6-sol`, contra 36 s para
  `gemini-3.7-flash`.
- Recusado em CI (`CI` ou `GITHUB_ACTIONS` definido): a assinatura é autenticada
  por um arquivo de sessão pessoal, que não deve estar em um runner
  compartilhado.
- Variáveis: `CODEX_BIN`, `CODEX_TIMEOUT` (segundos por segmento, padrão 600).

### Na assinatura do Grok: `--use_grok_cli`

Mesmo princípio com a CLI oficial Grok Build, na assinatura SuperGrok ou
X Premium+.

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login                                      # ou : grok login --device-code
aipmt --use_grok_cli --eco --file README.md --target_dir . --target_lang pl
```

- **Isolamento mais fraco que o Codex.** A sandbox de SO do Grok não se aplica
  a muitas máquinas Linux recentes (AppArmor, sockets de runtime
  de contêiner), e um perfil que não pode ser aplicado inicia sem confinamento em
  silêncio. Por isso, o script não solicita nenhum perfil por padrão, avisa sobre isso e
  apoia-se nas regras `--deny` da CLI, incluindo o catch-all `*` — a única
  camada que se recusa a iniciar em vez de remover a proteção sem
  avisar. `GROK_TRANSLATE_SANDBOX=read-only` exige a sandbox de SO, e a inicialização
  falha se a máquina não puder cumpri-la.
- A cota é semanal, compartilhada com Chat, Imagine e Voice, e nenhum
  comando permite consultá-la: um lote pode consumir o uso conversacional
  sem qualquer aviso.
- Variáveis: `GROK_BIN`, `GROK_HOME` (diretório da CLI, padrão `~/.grok`),
  `GROK_TIMEOUT` (padrão 900), `GROK_TRANSLATE_SANDBOX`.

### Na assinatura do Google: `--use_antigravity`

Mesmo princípio com `agy`, a CLI oficial do Antigravity: para quem assina o Google
AI Pro ou Ultra, a tradução é deduzida da cota da assinatura em vez
de ser cobrada por token. Este é o único caminho para essa cota: a Gemini CLI não
atende mais a essas contas desde 18 de junho de 2026
([comunicado](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)),
e o SDK do Antigravity aceita apenas uma chave de API ou um projeto Google Cloud.

```bash
# agy 1.2.11 ou plus récent : https://antigravity.google/docs/cli/install/
agy                                  # une fois : se connecter avec le compte de l'abonnement
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
agy -p /usage --output-format json   # quota restant, sans en consommer
```

- **Nenhuma via paga permanece aberta.** agy recebe do seu
  ambiente apenas uma lista restrita de variáveis — `PATH`, idioma e fuso horário,
  terminal, identidade, proxies e certificados, barramento de sessão — e nenhuma chave:
  várias de suas variáveis desviam uma chamada sem exibir nada (medido:
  uma envia o documento para um gateway de terceiros, outra para um projeto
  Google Cloud tarifado), e uma lista de bloqueio esquecia algumas a cada revisão.
  Antes de qualquer segmento, `agy -p /config`, que não consome cota, deve mostrar
  os créditos de IA pagos desativados, sem chave de API nem projeto Google Cloud — uma
  configuração ausente equivale a recusa —, caso contrário nada é traduzido; o log de cada
  chamada deve em seguida atestar a assinatura (`authMethod=consumer`), caso contrário a
  resposta é recusada.
- **Isolamento.** Cada chamada é executada em um diretório pessoal privado e
  descartável, com um agente de tradução sem ferramentas: suas configurações, regras,
  plugins, servidores MCP e hooks do agy não entram nele, nada é adicionado ao seu
  histórico e a autenticação permanece no chaveiro, que o aipmt nunca lê.
  Um agente não encontrado faz o agy recorrer silenciosamente ao seu agente de programação
  e às suas ferramentas: uma linha inteira do log deve confirmar o agente correto — um
  documento que cite essa mensagem não a substitui —, caso contrário haverá recusa.
- **Plataformas**: Linux, em uma sessão que possua chaveiro (barramento de sessão
  D-Bus, Secret Service); macOS é aceito, sem ter sido medido nele. Recusado
  no Windows, onde o agy não lê as variáveis que isolam cada chamada, e
  no Linux sem barramento de sessão — sessão SSH, contêiner, servidor: o agy
  armazena seu token em um arquivo de `~/.gemini`, que o isolamento oculta. A
  recusa ocorre antes de qualquer execução, com o seu motivo, em vez de esperar um minuto
  por um código de autenticação.
- **Modelos**: os do `agy models`. Os modelos Gemini trazem o esforço no próprio nome
  (`gemini-3.8-flash-medium`…): um nome sem sufixo é recusado antes da chamada,
  e `--reasoning_effort` não tem efeito. Por padrão `gemini-3.8-flash-medium`,
  e `gemini-3.7-flash-low` em `--eco`; as campanhas que os definiram estão
  descritas em [Medições detalhadas](#medições-detalhadas). Claude e GPT-OSS
  têm sua própria cota, muito menor: cerca de 1% da janela de
  5 horas por chamada medida, contra 0,05% no Flash.
- **Cota**: por grupo, uma janela de 5 horas e uma semanal, de forma
  proporcional ao custo em tokens. Medido na conta do autor: cerca de
  16 pontos da janela de 5 horas por milhão de caracteres de origem no
  `gemini-3.8-flash-medium`, 14 no `gemini-3.7-flash-medium` e 7 a 8 no
  esforço baixo — um README de 40.000 caracteres custa, portanto, pouco mais de meio
  ponto. O limite semanal depende do plano. A retentativa segue
  o que o agy declara como passível de nova tentativa; caso contrário, uma janela esgotada nunca
  é tentada novamente: ela faz cada arquivo falhar até a reinicialização
  exibida por `/usage`.
- **Mais lento que a API**: no artigo denso de medições, 3 min e 59 s por
  idioma em mediana no `gemini-3.8-flash-medium` e 3 min e 14 s no
  `gemini-3.7-flash-medium`, contra 1 min e 18 s para o Gemini 3.7 Flash via API.
- **Interrupção**: Ctrl-C ou um terminal fechado encerram o agy junto com o
  comando em vez de deixá-lo terminar sua execução consumindo sua cota; o mesmo se
  aplica a Codex, Grok CLI e OpenCode. Sob o `nohup`, a tradução continua.
- Recusado em CI (`CI` ou `GITHUB_ACTIONS` definido): a autenticação reside em um
  chaveiro pessoal. Em um runner, use `--use_gemini` com `GOOGLE_API_KEY`.
- Variáveis: `AGY_BIN` (caso contrário, o `PATH`, depois `~/.local/bin/agy`),
  `AGY_TIMEOUT` (segundos por segmento, inicialização inclusa, padrão 900).

**Termos de uso: sua conta é a responsável.** Os
[termos do Antigravity](https://antigravity.google/terms) (seção 6) e seu
[FAQ](https://antigravity.google/docs/faq/) proíbem o acesso ao serviço
por meio de software de terceiros utilizando a autenticação do Antigravity — Claude Code,
OpenClaw e OpenCode são citados nominalmente —, sob pena de suspensão da conta. O aipmt
não lê nem reutiliza o token: ele executa o binário oficial no
[modo headless](https://antigravity.google/docs/cli/headless/) que o Google
documenta para scripts e CI. Um membro do Google considerou "padrão"
executar `agy -p` a partir de um script local para o próprio trabalho
([fórum oficial, 25 de setembro de 2026, resposta sem valor contratual](https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829));
nenhum texto decide explicitamente o caso de uma ferramenta distribuída como esta.

**Apenas documentos públicos.** De acordo com a seção 5 dos mesmos termos, as
interações — prompts, respostas, metadados — podem ser usadas para melhorar os
produtos e o aprendizado de máquina do Google e ser revisadas por
humanos, mesmo na assinatura paga. A desativação é feita pela configuração
`enableTelemetry`, de efeito não documentado, que o aipmt não define; suas configurações
do agy não são transferidas para o seu ambiente isolado. Não passe nada confidencial por aqui.

### Na assinatura do Claude: `--use_claude_code`

Mesmo princípio com o `claude`, a CLI oficial do Claude Code, em modo `-p`: para
quem paga o Claude Pro ou Max, a tradução é descontada da cota da
assinatura em vez de ser faturada por token. Não confundir com
o `--use_claude`, a API da Anthropic, faturada por uso.

```bash
claude                                   # une fois : /login avec le compte de l'abonnement
aipmt --use_claude_code --file README.md --target_dir . --target_lang en
```

- **Nenhuma via paga permanece aberta, e cada chamada prova isso.** O Claude
  Code só recebe do seu ambiente uma lista fechada de variáveis — nenhuma
  chave de API, nenhum token, nenhum provedor de nuvem, nenhum marcador da sessão do Claude Code
  a partir da qual o aipmt teria sido iniciado. Antes do primeiro segmento, `claude auth status` deve
  mostrar a conexão da assinatura, sem chave do Console, e `/usage`, que não consome
  cota alguma, deve atestar isso; cada chamada atesta isso, por sua vez, em seu
  evento de inicialização, caso contrário a resposta é recusada.
- **Desative o "extra usage"** (claude.ai, Configurações → Uso) para
  garantir que o custo zero se mantenha: se ativado, ele assume o controle quando uma janela é esgotada e
  fatura sem exibir nenhum erro. O aipmt interrompe a tradução assim que o relatório
  de cota de uma chamada sinaliza isso, mas essa chamada específica já foi contabilizada.
- **Cota compartilhada com suas sessões do Claude Code.** Cada chamada informa
  o uso das janelas de 5 horas e semanal; acima de 80%
  (`AIPMT_CLAUDE_MAX_UTILIZATION`), nenhum segmento adicional é iniciado, para
  não esgotar o que é necessário para o seu trabalho.
- **Isolamento.** Cada chamada é executada sem ferramentas, em um diretório privado e
  descartável, em modo sem personalização: nem os seus `CLAUDE.md`, nem seus plugins,
  hooks, servidores MCP ou configurações são carregados, e nada é mantido da
  sessão. Os anexos são desativados: um `@chemin` no seu documento
  continua sendo texto e não abre nenhum arquivo (medido).
- **Modelos**: `sonnet` por padrão, com esforço `low`, e em `--eco` também:
  `--eco` não altera nada nesse caminho. Medidos nos mesmos documentos, `haiku`
  é duas vezes mais lento — ele raciocina sem que seja possível impedi-lo — para
  um custo quase idêntico, e `opus` recusa conteúdos de biologia (ponto
  seguinte). Ambos permanecem acessíveis via `--model`; esses aliases seguem o
  modelo mais recente de sua família. `fable` e as variantes `[1m]` são recusados,
  porque consomem créditos pagos. `--reasoning_effort` ajusta o esforço,
  do qual uma tradução não tira proveito: o raciocínio medido é nulo ou quase nulo.
- **O Opus recusa determinados conteúdos de biologia.** Suas salvaguardas são mais
  estritas do que as do Sonnet, e a mensagem de erro da Anthropic avisa que elas
  "can sometimes flag biology-research-adjacent work". Medido: uma nota informativa de
  monitoramento sobre 279 moléculas geradas fez com que o artigo fosse recusado nos quatorze
  idiomas. Nada é gravado: o aipmt recusa a resposta truncada, identifica as
  salvaguardas e recomenda `--model sonnet`.
- Recusado em CI (`CI` ou `GITHUB_ACTIONS` definido) e no Windows (não medido).
- Variáveis: `AIPMT_CLAUDE_BIN` (caso contrário, o `PATH`, depois `~/.local/bin/claude`),
  `AIPMT_CLAUDE_TIMEOUT` (segundos por segmento, padrão 900),
  `AIPMT_CLAUDE_MAX_UTILIZATION` (padrão 0.8), `CLAUDE_CONFIG_DIR` (a conta do
  Claude Code, nunca obtida de um `.env` de projeto); diretórios de trabalho sob
  `XDG_CACHE_HOME/aipmt/claude-code` (padrão `~/.cache`).

**Termos de uso: é a sua conta que está em jogo.** A
[página legal do Claude Code](https://code.claude.com/docs/en/legal-and-compliance)
não impede "an end user from signing in to the unmodified Claude Code binary
with their own Claude subscription": é exatamente isso que o aipmt faz, iniciando o
binário oficial e nunca lendo o token. Mas a Anthropic "does not permit
third-party developers […] to route requests through Free, Pro, or Max plan
credentials on behalf of their users", prefere a chave de API para ferramentas
de terceiros, "including open-source projects", e reserva-se o direito de debitar o
uso dos créditos pagos
([ajuda do Claude](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)).
Nenhum texto define categoricamente o caso de uma ferramenta distribuída que executa o binário.

**Dados**: nas contas Free, Pro e Max, o treinamento de modelos
também se aplica ao Claude Code quando a configuração de privacidade o autoriza
([página de dados](https://code.claude.com/docs/en/data-usage)). O aipmt não armazena
nenhuma transcrição local (`--no-session-persistence`). Não processe
nada confidencial por meio dele.

### Para o provedor de sua escolha: `--use_opencode`

O [OpenCode](https://opencode.ai) é um agente de código open source (MIT) que
roteia para os provedores configurados nele: chave de API, assinatura,
gateway OpenCode Zen (modelos gratuitos, sem conta) ou modelo local. Dois
caminhos foram medidos de ponta a ponta aqui: Zen e Ollama.

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
cujas conversas podem ser usadas para treinamento, e essa escolha não deve ser feita
por você.

Isolamento em cada chamada:

- uma configuração inline, com prioridade sobre a sua, define um agente `aipmt`
  cujas ferramentas são todas recusadas (`permission: { "*": "deny" }`), compartilhamento de
  sessão desativado, `--pure`, nunca `--auto`;
- diretório de trabalho descartável e vazio, `OPENCODE_DISABLE_PROJECT_CONFIG` e
  `OPENCODE_DISABLE_CLAUDE_CODE` definidos — sem eles, o OpenCode injeta no
  prompt o `AGENTS.md` do diretório atual e `~/.claude/CLAUDE.md`. O
  `~/.config/opencode/AGENTS.md` global continua sendo injetado; o OpenCode não permite
  descartá-lo;
- contrato de saída: código de retorno 0, nenhum evento `error`, nenhuma chamada
  de ferramenta, último passo em `stop`, texto não vazio e o agente `aipmt`
  efetivamente carregado — um `--agent` desconhecido não faz o OpenCode falhar, ele
  recorre silenciosamente ao agente de codificação;
- nenhuma chave do `aipmt` é transmitida, exceto `OPENCODE_API_KEY`, a chave
  do próprio OpenCode. Os provedores são configurados no OpenCode, não no
  `.env` do `aipmt`.

Importante saber:

- Os modelos gratuitos do Zen são voláteis, têm limites não documentados e
  suas conversas podem ser usadas para treinamento: use para documentação
  pública, não para conteúdo privado.
- Um modelo local deve oferecer pelo menos 16k tokens de contexto, já que os segmentos
  chegam a até 16.000 caracteres. O Ollama frequentemente configura 4.096: utilize
  um `Modelfile` com `PARAMETER num_ctx 32768`.
- `--eco` não tem efeito; `--reasoning_effort` é repassado diretamente como
  `--variant` do OpenCode.
- O OpenCode registra logs de cada sessão em `~/.local/share/opencode/`.
- Variáveis: `OPENCODE_BIN` (caso contrário, o `PATH`, depois `~/.opencode/bin/opencode`),
  `OPENCODE_TIMEOUT` (segundos por segmento, padrão 600). O `OPENCODE_CONFIG`
  é repassado diretamente ao OpenCode.

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
modelos, e que um Modelfile não consegue desativar. Medido em uma frase de
seis palavras: 919 tokens de reflexão e 68 segundos sem a opção, 9 tokens com ela.

### Para mais de 400 modelos: `--use_openrouter`

O OpenRouter é um roteador faturado por uso, em um saldo único de créditos, diante de
modelos hospedados por terceiros — incluindo modelos abertos chineses que nenhum
outro provedor disponibiliza aqui.

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

`--model` é obrigatório. Uma verificação preliminar, executada antes de qualquer faturamento, resolve
duas particularidades do roteamento:

- **Um mesmo modelo é fornecido por dezenas de provedores de hospedagem com limites
  diferentes** — no `z-ai/glm-5.3-flash`, 23 provedores, incluindo um limitado a
  2.048 tokens de saída. A verificação preliminar lê o `/api/v1/models/{modèle}/endpoints`,
  descarta provedores com menos de 8.000 tokens de saída ou em estado degradado, e
  fixa os demais com `allow_fallbacks: false`.
- **O raciocínio é faturado pela tarifa de saída** — 107 tokens contra 2 em
  uma resposta "OK" do `z-ai/glm-5.2`. Ele é desativado por padrão; os modelos
  que o exigem recebem o menor esforço que aceitam, já que o padrão do
  catálogo pode saturar a saída antes do término da tradução.
  `--reasoning_effort` continua tendo prioridade.

```
→ OpenRouter : 30 hébergeur(s) épinglé(s) sur 33, contexte 1048576 tokens,
  sortie plafonnée à 32768, raisonnement coupé
```

- A janela de contexto vem do catálogo. Um modelo com menos de 16.400 tokens é
  recusado antes de qualquer chamada: 8.400 para o prompt e o segmento, 8.000 de saída
  no mínimo.
- Um slug ausente no catálogo, um catálogo inacessível ou a ausência
  de um provedor que suporte o limite interrompem o comando.
- `finish_reason=length` com uma saída vazia significa orçamento consumido pelo
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
plugin remark.

```bash
aipmt --file article.mdx --target_lang en --add_translation_note --note_format marker --note_position top
```

## Medições detalhadas

Todas as medições são de traduções realmente executadas com `aipmt`, para
quatorze idiomas: en, es, de, it, pt, nl, pl, sv, ro, ja, ko, zh, ar, hi.
**Gravadas** conta os arquivos que passaram pelas salvaguardas; **Sem
discrepâncias** aqueles em que o `scripts/compare_structure.py` não detecta nada — mesma quantidade de
seções, subtítulos, links, URLs distintas, blocos de código,
códigos inline, linhas de tabela, blocos de citação e palavras em negrito.

"Sem discrepâncias" significa "nada detectado", não "idêntico": o comparador
conta elementos sem ler o conteúdo deles. Ele não sinaliza um título de
nível 4 excluído, nem o texto de um código inline substituído, nem uma flag
trocada, nem um link interno renderizado com um parêntese a mais,
`[texte]((#ancre))`, que não leva a lugar nenhum — e não avalia o
idioma.

### Artigo de monitoramento denso, modo `--news`

Uma edição do [monitoramento de IA de jls42.org](https://jls42.org/fr/news):
589 linhas, 140 links, 21 seções, 3 citações em inglês protegidas. Campanha
de 4 e 5 de setembro de 2026.

| Modelo                                          | Acesso             | Gravadas | Sem discrepâncias | Mediana/idioma |
| ----------------------------------------------- | ------------------ | -------- | ----------------- | -------------- |
| `gemini-3.7-flash`                              | API Google         | 14/14    | ✅ **14/14**      | 1 min 18 s     |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | assinatura Google  | 14/14    | ✅ **14/14**      | 3 min 59 s     |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | assinatura Google  | 14/14    | ✅ **14/14**      | 3 min 14 s     |
| `gpt-5.6-sol` (`--use_codex`)                   | assinatura ChatGPT | 14/14    | ✅ **14/14**      | 11 min 28 s    |
| `z-ai/glm-5.2`                                  | OpenRouter         | 14/14    | ✅ **14/14**      | 5 min 37 s     |
| `qwen/qwen3.8-flash`                            | OpenRouter         | 14/14    | ✅ **14/14**      | 26 min 23 s    |
| `sonnet` (`--use_claude_code`)                  | assinatura Claude  | 14/14    | ⚠️ 13/14          | 6 min 49 s     |
| `claude-sonnet-5`                               | API Anthropic      | 14/14    | ⚠️ 11/14          | 6 min 31 s     |
| `haiku` (`--use_claude_code`)                   | assinatura Claude  | 14/14    | ⚠️ 11/14          | 15 min 54 s    |
| `opencode/mimo-v2.5-free`                       | OpenCode Zen       | 13/14    | ❌ 11/14          | 9 min 27 s     |
| `qwen/qwen3.7-flash`                            | OpenRouter         | 13/14    | ❌ 8/14           | 10 min 09 s    |
| `ollama/gpt-oss-20b-32k`                        | local              | 10/14    | ❌ 7/14           | 12 min 39 s    |
| `mistral-large-latest`                          | API Mistral        | 11/14    | ❌ 5/14           | 5 min 32 s     |
| `deepseek/deepseek-v4-flash-0731`               | OpenRouter         | 4/14     | ❌ 3/14           | 37 min 27 s    |
| `grok-4.6` (`--use_grok_cli`)                   | assinatura Grok    | 1/14     | ❌ 1/14           | 23 min 11 s    |
| `opus` (`--use_claude_code`)                    | assinatura Claude  | 0/14     | ❌ 0/14           | —              |

O Grok foi medido novamente em 9 de setembro em outra edição do mesmo monitoramento
(356 linhas): 9 idiomas gravados de 14, 8 sem discrepâncias. É esse número que
consta na tabela principal. Três campanhas interrompidas não foram
incluídas: `qwen3.5-27b` (9 idiomas) e `kimi-k2.6` (4) por falta de crédito,
`z-ai/glm-5.3-flash` cujas duas falhas decorreram de uma configuração de raciocínio
que o provedor já corrigiu desde então. As linhas do OpenRouter foram medidas com as
configurações padrão do roteador, antes do `--use_openrouter`; o `z-ai/glm-5.2`,
medido novamente com o provedor fornecido, obtém os mesmos 14/14. Os números foram
recalculados em 10 de setembro com o comparador atual: `qwen3.8-flash` e
`qwen3.7-flash` ganham um idioma a mais cada em relação à primeira
publicação, os demais permaneceram inalterados.

As linhas do `--use_antigravity` foram medidas em 26 de setembro no mesmo
artigo, com quatro traduções em paralelo: `gemini-3.7-flash-medium` pela manhã,
`gemini-3.8-flash-medium` à tarde. Em inglês, cada um removeu por conta própria
as três linhas de tradução francesa sob as citações, sem inventar
bandeira, e as citações em inglês ficaram intactas: a limpeza de fallback não
precisou atuar. Em `--eco` (`gemini-3.7-flash-low`), em apenas quatro idiomas
(en, ja, ar, hi): 4 gravadas de 4, todas sem discrepâncias, mediana de 1 min 52 s.
Contraprova no mesmo dia em uma edição mais recente do monitoramento,
a de 25 de setembro (438 linhas, 2 citações em inglês), traduzida fora do
blog por `gemini-3.7-flash-medium`: 14 gravadas de 14, todas sem discrepâncias, 87 a
128 s por idioma.

As linhas do `--use_claude_code` foram medidas em 26 de setembro no mesmo
artigo, com quatro traduções em paralelo, no nível de esforço `low`. Com o `sonnet`, as
citações em inglês ficaram intactas nos quatorze idiomas e, em inglês, o
modelo removeu por conta própria as linhas de tradução francesa, sem inventar
bandeira. O `opus` não gravou nenhum idioma: em todos eles, suas salvaguardas
interromperam a resposta no último segmento, por causa de uma nota sobre 279 moléculas
geradas para um sítio de ligação. Enviada isoladamente, essa nota é recusada com base
na categoria "bio"; o `sonnet` a traduziu em todos os idiomas. O `haiku` gravou
os quatorze idiomas; em três (en, pl, ro), um título de seção mudou do
nível 2 para o nível 1. Ele raciocina sem que seja possível impedi-lo — 61% dos
seus tokens de saída —, resultando em mais que o dobro do tempo do `sonnet`.

### README deste projeto, Markdown padrão

Revisão congelada em 9 de setembro de 2026: 785 linhas, 285 códigos inline, 40
fechamentos de blocos, 89 linhas de tabela. Quatro traduções em paralelo.

| Modelo                                          | Escritas | Sem divergência | Mediana/idioma | O que difere                                                             |
| ----------------------------------------------- | -------- | --------------- | -------------- | ------------------------------------------------------------------------ |
| `gemini-3.8-flash-medium` (`--use_antigravity`) | 14/14    | ✅ 14/14        | 1 min 43 s     | nada                                                                     |
| `opus` (`--use_claude_code`)                    | 14/14    | ✅ 14/14        | 1 min 48 s     | nada                                                                     |
| `haiku` (`--use_claude_code`)                   | 14/14    | ✅ 14/14        | 4 min 02 s     | nada para o comparador; links internos duplicados (en)                   |
| `gemini-3.7-flash`                              | 14/14    | ⚠️ 13/14        | 36 s           | uma palavra em negrito (ja)                                              |
| `gemini-3.7-flash-medium` (`--use_antigravity`) | 14/14    | ⚠️ 13/14        | 1 min 22 s     | uma palavra em negrito (ko)                                              |
| `sonnet` (`--use_claude_code`)                  | 14/14    | ⚠️ 13/14        | 2 min 20 s     | uma linha de tabela colada à anterior (ar)                               |
| `claude-sonnet-5`                               | 14/14    | ⚠️ 12/14        | 2 min 56 s     | um link (sv), uma palavra em negrito (zh)                                |
| `gpt-5.6-sol` (`--use_codex`)                   | 14/14    | ⚠️ 12/14        | 6 min 46 s     | uma palavra em negrito (ar, ja)                                          |
| `z-ai/glm-5.2` (OpenRouter)                     | 14/14    | ⚠️ 11/14        | 2 min 34 s     | uma palavra em negrito (hi, ja, ko)                                      |
| `qwen/qwen3.7-flash`                            | 14/14    | ⚠️ 10/14        | 2 min 17 s     | 40 códigos inline adicionados em árabe; negrito (hi, ja, ko)             |
| `mistral-large-latest`                          | 14/14    | ❌ 1/14         | 2 min 44 s     | uma seção perdida (ar, hi, ko); blocos de código adicionados (ja, ko, ro, zh) |

Duas campanhas interrompidas não estão listadas: Grok, sessão CLI expirada
após doze idiomas (onze sem divergência), e `qwen3.8-flash`, HTTP 429 de sua
hospedagem após dois. `opencode/mimo-v2.5-free` e `ollama/gpt-oss-20b-32k`
não foram remedidos nesta revisão; naquela de 4 e 5 de setembro,
277 linhas mais curta, eles escreveram cada um 9 traduções de 14, sendo 7
e 1 sem divergência.

As linhas `--use_antigravity` e `--use_claude_code` não foram medidas na
revisão congelada, mas em 26 de setembro na publicada com a 1.14.0: 600
linhas, 257 códigos inline, 30 fechamentos de blocos, 85 linhas de tabela. Sendo
185 linhas mais curta, ela não se compara termo a termo com as outras linhas;
estas linhas, no entanto, comparam-se entre si. Nos links internos, que o
comparador não verifica, `gemini-3.8-flash-medium` os manteve intactos em
todos os quatorze idiomas, `gemini-3.7-flash-medium` os quebrou em italiano;
`sonnet` e `opus` os mantiveram intactos em todos os lugares, `haiku` os duplicou em
inglês.

### Quatro READMEs de projetos conhecidos

FastAPI, Ollama, tldr-pages e Vue.js, obtidos diretamente do GitHub — documentos
mais fáceis do que os dois anteriores. A campanha visava os modelos
com dificuldades; o Gemini serve aqui como ponto de comparação.

| Modelo                    | Escopo                     | Escritas | Sem divergência |
| ------------------------- | -------------------------- | -------- | --------------- |
| `gemini-3.7-flash`        | 4 projetos × 14 idiomas    | 56/56    | ✅ **55/56**    |
| `opencode/mimo-v2.5-free` | 4 projetos × 14 idiomas    | 55/56    | ❌ 47/56        |
| `grok-4.6` (assinatura)   | 4 projetos × ar, hi, ja, zh | 16/16    | ❌ 14/16        |
| `ollama/gpt-oss-20b-32k`  | 4 projetos × ar, hi, ja, zh | 15/16    | ❌ 9/16         |

### O que estas medições não são

- **Não é uma classificação exaustiva**: apenas o OpenRouter oferece mais de quatrocentos
  modelos; cerca de quinze foram medidos.
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

As duas linhas são necessárias: sem `pip install -e .`, o `python -m aipmt`
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
assinatura do ChatGPT por padrão, quatro em paralelo. `REGEN_PROVIDER` e
`REGEN_MODEL` alteram o caminho: `antigravity` permanece em uma assinatura, a
do Google, e passa sem exceção; uma API tarifada (`openai`, `gemini`,
`grok`, `openrouter`) é recusada sem `REGEN_ALLOW_PAID_API=1`;
`REGEN_JOB_TIMEOUT` limita cada tarefa (600 s, 1.800 s no Codex e
Antigravity). Os detalhes das ferramentas estão em `CLAUDE.md`.

## Projetos que utilizam este script

- **[jls42.org](https://jls42.org)** — blog pessoal publicado em 15 idiomas. Seu
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
comercialização ou adequação a uma finalidade específica, e seu autor não pode ser
responsabilizado por quaisquer danos resultantes de seu uso. O texto da
licença prevalece sobre este resumo.

- **Revise antes de publicar.** As proteções cobrem blocos de código,
  código inline, URLs, âncoras e citações do modo `--news` — não os
  títulos, tabelas, front matter ou o significado das suas frases.
- **Seus documentos são enviados para o provedor escolhido**, sob seus termos
  de uso e política de dados. Alguns modelos gratuitos podem
  reutilizar suas interações para treinamento, e os termos do Antigravity
  permitem que o Google os reutilize e os faça revisar por humanos,
  incluindo assinaturas pagas; um modelo local é a única forma que não permite
  que nenhum dado saia da sua máquina.
- **As chamadas de API são cobradas de você.** Este programa não limita os
  gastos: um documento longo, uma retomada após falha ou um modelo que raciocina
  muito custam mais.
- **As medições publicadas são observações datadas**, não garantias.

Os nomes de produtos e empresas citados pertencem aos seus respectivos
proprietários. Este projeto não é afiliado a nenhum deles.

**Artigo traduzido do fr para o pt com gemini-3.8-flash-medium.**
