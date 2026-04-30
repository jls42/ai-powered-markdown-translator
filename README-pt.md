# Tradutor de Markdown com IA

🌍 [Francês](README.md) | [Inglês](README-en.md) | [Espanhol](README-es.md) | [Chinês](README-zh.md) | [Alemão](README-de.md) | [Japonês](README-ja.md) | [Coreano](README-ko.md) | [Árabe](README-ar.md) | [Hindi](README-hi.md) | [Italiano](README-it.md) | [Holandês](README-nl.md) | [Polonês](README-pl.md) | [Português](README-pt.md) | [Romeno](README-ro.md) | [Sueco](README-sv.md)

Tradutor de arquivos Markdown usando **OpenAI**, **Mistral AI**, **Claude (Anthropic)** e **Google Gemini**.

Este script Python traduz arquivos Markdown de um idioma de origem para um idioma de destino, preservando a formatação, os blocos de código e os metadados do front matter.

## Funcionalidades Principais

- **Multi-Provider**: Suporte a 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **Modelos 2026**: GPT-5.5, Claude Sonnet 4.6, Gemini 3.1 Pro
- **Modo Econômico**: Opção `--eco` para usar modelos mais rápidos e menos caros
- **Arquivo Único**: Opção `--file` para traduzir um único arquivo
- **Segmentação Inteligente**: Gestão de textos longos com limites de tokens por modelo
- **Preservação do Código**: Os blocos de código E o código inline (`` `...` ``) são preservados
- **Nome do Arquivo**: Opção `--keep_filename` para manter o nome original
- **Modo Notícias**: Opção `--news` para proteger citações em inglês e gerenciar bandeiras em artigos de notícias
- **Configuração .env**: Suporte ao arquivo `.env` para as chaves de API
- **Nota de Tradução**: Adição opcional de uma nota no final do documento

## Instalação

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Ferramentas de qualidade (opcional, mas recomendado)

O projeto usa [`pre-commit`](https://pre-commit.com) para impedir o commit de código mal formatado, vulnerável ou contendo um segredo. Instalação:

```bash
pip install -r requirements-dev.txt   # detect-secrets, pip-audit, mypy, lizard
pre-commit install                    # hooks rapides à chaque commit
pre-commit install --hook-type pre-push  # hooks lourds avant chaque push
```

Hooks ativos: ruff (lint+format), shellcheck (bash), prettier (markdown/yaml/json), Lizard (complexidade), detect-secrets (chaves API), mypy (tipagem progressiva), Opengrep (SAST), pip-audit (CVE deps), unittest. Veja a seção `CLAUDE.md` _Quality / pre-commit_ para os detalhes.

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

## Utilização

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

Usa modelos mais rápidos e menos caros (gpt-5.4-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opções

| Opção                    | Descrição                                                              |
| ------------------------ | ------------------------------------------------------------------------ |
| `--file`                 | Arquivo Markdown único a traduzir                                        |
| `--source_dir`           | Diretório de origem contendo os arquivos Markdown                        |
| `--target_dir`           | Diretório de saída para os arquivos traduzidos                          |
| `--source_lang`          | Idioma de origem (padrão: `fr`)                                             |
| `--target_lang`          | Idioma de destino (padrão: `en`)                                              |
| `--model`                | Modelo específico a ser usado                                            |
| `--eco`                  | Usar os modelos econômicos                                               |
| `--use_mistral`          | Usar a API Mistral AI                                                   |
| `--use_claude`           | Usar a API Claude                                                       |
| `--use_gemini`           | Usar a API Gemini                                                       |
| `--force`                | Forçar a retradução                                                     |
| `--keep_filename`        | Manter o nome original do arquivo                                       |
| `--news`                 | Modo notícias: protege citações EN, gerencia bandeiras por idioma        |
| `--add_translation_note` | Adicionar uma nota de tradução                                           |
| `--include_model`        | Incluir o nome do modelo no arquivo de saída                            |

### Modelos padrão (2026)

| Provedor | Qualidade (padrão)         | Econômico (`--eco`)     |
| -------- | ------------------------ | ------------------------ |
| OpenAI   | `gpt-5.5`                | `gpt-5.4-mini`           |
| Claude   | `claude-sonnet-4-6`      | `claude-haiku-4-5`       |
| Mistral  | `mistral-large-latest`   | `mistral-small-latest`   |
| Gemini   | `gemini-3.1-pro-preview` | `gemini-3-flash-preview` |

> **Recomendação para traduções long-form** : `--use_gemini` (padrão = `gemini-3.1-pro-preview` qualidade, `--eco` = `gemini-3-flash-preview`) tende a preservar melhor a estrutura markdown em scripts não latinos (PL, JA, ZH, AR, HI), especialmente no modo `--news` onde a fidelidade dos placeholders importa. OpenAI continua sendo o padrão por compatibilidade retroativa.

## Projetos usando este script

- **[jls42.org](https://jls42.org)** - Blog pessoal multilíngue (15 idiomas)

## Autor

Julien LE SAUX
Email : contact@jls42.org

## Licença

GNU GENERAL PUBLIC LICENSE Version 3. Veja [LICENSE](LICENSE).

**Este documento foi traduzido da versão fr para o idioma pt usando o modelo gpt-5.4-mini. Para mais informações sobre o processo de tradução, consulte https://gitlab.com/jls42/ai-powered-markdown-translator**

