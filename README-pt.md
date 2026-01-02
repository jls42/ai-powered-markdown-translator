# Tradutor de Markdown com IA

🌍 [English](README-en.md) | [Español](README-es.md) | [中文](README-zh.md) | [Deutsch](README-de.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md) | [हिन्दी](README-hi.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [Português](README-pt.md) | [Română](README-ro.md) | [Svenska](README-sv.md)

Tradutor de arquivos Markdown utilizando **OpenAI**, **Mistral AI**, **Claude (Anthropic)** e **Google Gemini**.

Este script Python traduz arquivos Markdown de um idioma de origem para um idioma de destino preservando a formatação, os blocos de código e os metadados front matter.

## Características Principais

- **Multi-provedor**: Suporte a 4 APIs (OpenAI, Mistral, Claude, Gemini)
- **Modelos 2026**: GPT-5, Claude Sonnet 4.5, Gemini 3 Pro
- **Modo Econômico**: Opção `--eco` para usar modelos mais rápidos e menos caros
- **Arquivo Único**: Opção `--file` para traduzir um único arquivo
- **Segmentação Inteligente**: Gerenciamento de textos longos com limites de tokens por modelo
- **Preservação do Código**: Os blocos de código não são traduzidos
- **Nota de Tradução**: Adição opcional de uma nota no final do documento

## Instalação

```bash
git clone https://gitlab.com/jls42/ai-powered-markdown-translator.git
cd ai-powered-markdown-translator
pip install -r requirements.txt
```

## Configuração

Defina a variável de ambiente para a API que você deseja usar :

```bash
export OPENAI_API_KEY='votre-clé-api-openai'
export MISTRAL_API_KEY='votre-clé-api-mistral'
export ANTHROPIC_API_KEY='votre-clé-api-anthropic'
export GOOGLE_API_KEY='votre-clé-api-google'
```

## Uso

### Traduzir um arquivo único

```bash
python translate.py --file 'document.md' --target_dir 'output/' --target_lang 'en'
```

### Traduzir um diretório

```bash
# Avec OpenAI (défaut: gpt-5)
python translate.py --source_dir 'content/fr' --target_dir 'content/en' --source_lang 'fr' --target_lang 'en'

# Avec Mistral AI
python translate.py --use_mistral --source_dir 'content/fr' --target_dir 'content/es' --target_lang 'es'

# Avec Claude
python translate.py --use_claude --source_dir 'content/fr' --target_dir 'content/de' --target_lang 'de'

# Avec Gemini
python translate.py --use_gemini --source_dir 'content/fr' --target_dir 'content/ja' --target_lang 'ja'
```

### Modo econômico

Utiliza modelos mais rápidos e menos caros (gpt-5-mini, claude-haiku, gemini-flash) :

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
| `--model` | Modelo específico a utilizar |
| `--eco` | Usar os modelos econômicos |
| `--use_mistral` | Usar a API Mistral AI |
| `--use_claude` | Usar a API Claude |
| `--use_gemini` | Usar a API Gemini |
| `--force` | Forçar a re-tradução |
| `--add_translation_note` | Adicionar uma nota de tradução |

### Modelos padrão (2026)

| Provedor | Qualidade (padrão) | Econômico (`--eco`) |
|----------|------------------|----------------------|
| OpenAI | `gpt-5` | `gpt-5-mini` |
| Claude | `claude-sonnet-4-5` | `claude-haiku-4-5` |
| Mistral | `mistral-large-latest` | `mistral-small-latest` |
| Gemini | `gemini-3-pro-preview` | `gemini-3-flash-preview` |

## Autor

Julien LE SAUX
Email : contact@jls42.org

## Licença

GNU GENERAL PUBLIC LICENSE Versão 3. Ver [LICENSE](LICENSE).