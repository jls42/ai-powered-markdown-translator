# Tradutor de Markdown com IA

🌍 [Francês](README.md) | [Inglês](README-en.md) | [Espanhol](README-es.md) | [Chinês](README-zh.md) | [Alemão](README-de.md) | [Japonês](README-ja.md) | [Coreano](README-ko.md) | [Árabe](README-ar.md) | [Hindi](README-hi.md) | [Italiano](README-it.md) | [Holandês](README-nl.md) | [Polonês](README-pl.md) | [Português](README-pt.md) | [Romeno](README-ro.md) | [Sueco](README-sv.md)

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
  <a href="https://sonarcloud.io/summary/new_code?id=jls42_ai-powered-markdown-translator"><img src="https://sonarcloud.io/api/project_badges/measure?project=jls42_ai-powered-markdown-translator&metric=bugs" alt="Erros"></a>
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

Tradutor de arquivos Markdown usando **OpenAI**, **Mistral AI**, **Claude (Anthropic)** e **Google Gemini**.

Este script Python traduz arquivos Markdown de um idioma de origem para um idioma de destino, preservando a formatação, os blocos de código e os metadados front matter.

## Características Principais

- **Multi-provedor**: suporte a 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **Modelos 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Modo econômico**: opção `--eco` para usar modelos mais rápidos e mais baratos
- **Arquivo único**: opção `--file` para traduzir um único arquivo
- **Segmentação inteligente**: gerenciamento de textos longos com limites de tokens por modelo
- **Preservação do código**: os blocos de código E o código inline (`` `...` ``) são preservados
- **Nome do arquivo**: opção `--keep_filename` para manter o nome original
- **Modo notícias**: opção `--news` para proteger as citações em inglês e gerenciar as bandeiras por idioma em artigos de notícias
- **Configuração .env**: suporte ao arquivo `.env` para as chaves de API
- **Nota de tradução**: adição opcional de uma nota no fim do documento

## Instalação

```bash
git clone https://github.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Ferramentas de qualidade (opcional, mas recomendado)

O projeto usa [`pre-commit`](https://pre-commit.com) para evitar fazer commit de código mal formatado, vulnerável ou que contenha um segredo. Instalação:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hooks ativos: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexidade), detect-secrets (chaves de API), mypy (tipagem progressiva), Opengrep (SAST), pip-audit (CVE deps), unittest. Veja `CLAUDE.md` na seção _Quality / pre-commit_ para detalhes.

## Configuração

Crie um arquivo `.env` na raiz do projeto ou defina as variáveis de ambiente:

```bash
# Fichier .env (recommandé)
OPENAI_API_KEY=votre-clé-api-openai
MISTRAL_API_KEY=votre-clé-api-mistral
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google

# Ou via export
export OPENAI_API_KEY='votre-clé-api-openai'
```

## Uso

### Traduzir um único arquivo

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traduzir um diretório

```bash
# Avec OpenAI (défaut: gpt-5.5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### Modo econômico

Usa modelos mais rápidos e mais baratos (gpt-5.4-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opções

| Opção                    | Descrição                                                             |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Arquivo Markdown único a traduzir                                       |
| `--source_dir`           | Diretório de origem contendo os arquivos Markdown                        |
| `--target_dir`           | Diretório de saída para os arquivos traduzidos                          |
| `--source_lang`          | Idioma de origem (padrão: `fr`)                                             |
| `--target_lang`          | Idioma de destino (padrão: `en`)                                              |
| `--model`                | Modelo específico a ser usado                                             |
| `--eco`                  | Usar os modelos econômicos                                         |
| `--use_mistral`          | Usar a API Mistral AI                                                |
| `--use_claude`           | Usar a API Claude                                                    |
| `--use_gemini`           | Usar a API Gemini                                                    |
| `--force`                | Forçar a retradução                                                  |
| `--keep_filename`        | Manter o nome original do arquivo                                     |
| `--news`                 | Modo notícias: protege citações em inglês, gerencia bandeiras por idioma |
| `--add_translation_note` | Adicionar uma nota de tradução                                           |
| `--note_position`        | Posição da nota: `top`, `bottom` (padrão), ou `both`                |
| `--note_format`          | Formato da nota: `legacy` (padrão, parágrafo em negrito) ou `marker`       |
| `--include_model`        | Incluir o nome do modelo no arquivo de saída                       |

### Nota de tradução: posições e formatos

Com `--add_translation_note`, o tradutor pode colocar a nota no topo, no rodapé ou em ambos os lugares, e apresentá-la seja em formato de texto simples (retrocompatível) seja em formato `marker` consumível por um plugin Markdown.

**Posição** (`--note_position`) :

- `bottom` (padrão) : nota no fim do arquivo, como historicamente.
- `top` : nota inserida **após o frontmatter YAML** (segurança do Astro Content Collections, gray-matter, etc.).
- `both` : nota inserida no topo E no fim (uma única chamada ao LLM, conteúdo reutilizado para os dois posicionamentos).

**Formato** (`--note_format`) :

- `legacy` (padrão) : parágrafo em negrito `**...**` — comportamento estritamente idêntico ao v1.8, byte a byte. Compatível com Hugo, GitHub, GitLab e qualquer renderer Markdown.
- `marker` : definição invisível de referência de link Markdown (`[ai-translation-note-<placement>]: <> "v=1 source=… target=… model=… date=…"`) seguida de um blockquote em negrito. Legível nativamente no GitHub/GitLab, e utilizável no build por um plugin remark do lado do Astro para produzir um banner estilizado (cf. blog jls42.org).

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

### Modelos padrão (2026)

| Provedor | Qualidade (padrão)         | Econômico (`--eco`)            |
| -------- | ------------------------ | ------------------------------- |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`                  |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5-20251001`     |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`          |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3.1-flash-lite-preview` |

> **Recomendação para traduções long-form** : `--use_gemini` (padrão = `gemini-3.1-pro-preview` qualidade, `--eco` = `gemini-3.1-flash-lite-preview`) tende a preservar melhor a estrutura markdown em scripts não latinos (PL, JA, ZH, AR, HI), especialmente no modo `--news`, em que a fidelidade dos placeholders conta. OpenAI continua sendo o padrão para a retrocompatibilidade.

## Projetos que usam este script

- **[jls42.org](https://jls42.org)** - Blog pessoal multilíngue (15 idiomas)

## Autor

Julien LE SAUX
E-mail: contact@jls42.org

## Licença

GNU GENERAL PUBLIC LICENSE Versão 3. Veja [LICENSE](LICENSE).

**Artigo traduzido do fr para o pt com gpt-5.4-mini.**
