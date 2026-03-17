# Tradutor de Markdown com IA

🌍 [Francês](README.md) | [Inglês](README-en.md) | [Espanhol](README-es.md) | [Chinês](README-zh.md) | [Alemão](README-de.md) | [Japonês](README-ja.md) | [Coreano](README-ko.md) | [Árabe](README-ar.md) | [Hindi](README-hi.md) | [Italiano](README-it.md) | [Holandês](README-nl.md) | [Polonês](README-pl.md) | [Português](README-pt.md) | [Romeno](README-ro.md) | [Sueco](README-sv.md)

Tradutor de arquivos Markdown usando **OpenAI**, **Mistral AI**, **Claude (Anthropic)** e **Google Gemini**.

Este script Python traduz arquivos Markdown de um idioma de origem para um idioma de destino, preservando a formatação, os blocos de código e os metadados front matter.

## Principais Funcionalidades

- **Multi-Provider**: Suporte a 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **Modelos 2026**: GPT-5.4, Claude Sonnet 4.5, Gemini 3.1 Pro
- **Modo Econômico**: Opção `--eco` para usar modelos mais rápidos e mais baratos
- **Arquivo Único**: Opção `--file` para traduzir um único arquivo
- **Segmentação Inteligente**: Tratamento de textos longos com limites de tokens por modelo
- **Preservação do Código**: Os blocos de código E o código inline (`` `...` ``) são preservados
- **Nome do Arquivo**: Opção `--keep_filename` para manter o nome original
- **Modo News**: Opção `--news` para proteger citações em inglês e gerenciar bandeiras em artigos de notícias
- **Configuração .env**: Suporte ao arquivo `.env` para as chaves de API
- **Nota de Tradução**: Adição opcional de uma nota no final do documento

## Instalação

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

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

### Traduzir um arquivo único

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traduzir um diretório

```bash
# Avec OpenAI (défaut: gpt-5.4)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### Modo econômico

Usa modelos mais rápidos e mais baratos (gpt-5-mini, claude-haiku, gemini-flash) :

```bash
python translate.py --eco --source_dir 'content/fr' --target_dir 'content/en'
```

### Opções

| Opção | Descrição |
|--------|-------------|
| `--file` | Arquivo Markdown único a traduzir |
| `--source_dir` | Diretório de origem contendo os arquivos Markdown |
| `--target_dir` | Diretório de saída para os arquivos traduzidos |
| `--source_lang` | Idioma de origem (padrão: `fr`) |
| `--target_lang` | Idioma de destino (padrão: `en`) |
| `--model` | Modelo específico a usar |
| `--eco` | Usar os modelos econômicos |
| `--use_mistral` | Usar a API Mistral AI |
| `--use_claude` | Usar a API Claude |
| `--use_gemini` | Usar a API Gemini |
| `--force` | Forçar a retradução |
| `--keep_filename` | Manter o nome original do arquivo |
| `--news` | Modo notícias: protege citações EN, gerencia bandeiras por idioma |
| `--add_translation_note` | Adicionar uma nota de tradução |
| `--include_model` | Incluir o nome do modelo no arquivo de saída |

### Modelos padrão (2026)

| Provider | Qualidade (padrão) | Econômico (`--eco`) |
|----------|--------------------|--------------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Projetos que usam este script

- **[jls42.org](https://jls42.org)** - Blog pessoal multilíngue (15 idiomas)

## Autor

Julien LE SAUX
Email : contact@jls42.org

## Licença

GNU GENERAL PUBLIC LICENSE Version 3. Veja [LICENSE](LICENSE).