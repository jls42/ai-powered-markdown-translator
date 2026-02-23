### Registro de alterações

🌍 [Francês](CHANGELOG.md) | [Inglês](CHANGELOG-en.md) | [Espanhol](CHANGELOG-es.md) | [Chinês](CHANGELOG-zh.md) | [Alemão](CHANGELOG-de.md) | [Japonês](CHANGELOG-ja.md) | [Coreano](CHANGELOG-ko.md) | [Árabe](CHANGELOG-ar.md) | [Hindi](CHANGELOG-hi.md) | [Italiano](CHANGELOG-it.md) | [Holandês](CHANGELOG-nl.md) | [Polonês](CHANGELOG-pl.md) | [Português](CHANGELOG-pt.md) | [Romeno](CHANGELOG-ro.md) | [Sueco](CHANGELOG-sv.md)

- **1.7** Novidades :
    - Opção `--keep_filename` para manter o nome do arquivo original durante a tradução
    - Suporte ao arquivo `.env` para carregar as chaves de API automaticamente
    - **Preservação do código inline** : os backticks (`` `...` ``) agora são protegidos durante a tradução
    - Aprimoramento do prompt do sistema :
        - Melhor tratamento das aspas no YAML frontmatter
        - Proteção das variáveis de template `{variable}`
        - Proibição de notas de tradutor não solicitadas
    - Testado com sucesso em 364 arquivos (migração do blog jls42.org)
- **1.6** Novidades :
    - Suporte da API Google Gemini para tradução (`--use_gemini`)
    - Atualização dos modelos padrão 2026 :
        - OpenAI : `gpt-5` (qualidade), `gpt-5-mini` (econômico)
        - Claude : `claude-sonnet-4-5` (qualidade), `claude-haiku-4-5` (econômico)
        - Gemini : `gemini-3-pro-preview` (qualidade), `gemini-3-flash-preview` (econômico)
    - Modo econômico (`--eco`) para usar modelos mais rápidos e menos caros
    - Tradução de arquivo único (`--file`) sem percorrer um diretório
    - Novo padrão de nomeação simplificado : `{base}-{lang}.md`
    - Opção `--include_model` para manter o formato antigo com o nome do modelo
    - Suporte a modelos não listados com limite de tokens padrão (128k)
    - README traduzido em 14 idiomas
- **1.5** Melhorias :
    - **Atualização das chaves de API e dos modelos padrão :**
        - **OpenAI :** Atualizado de `DEFAULT_MODEL_OPENAI` para `"gpt-4o"`.
        - **Mistral AI :** Atualizado de `DEFAULT_MODEL_MISTRAL` para `"mistral-large-latest"`.
        - **Claude da Anthropic :** Adição de `DEFAULT_ANTHROPIC_API_KEY` e atualização de `DEFAULT_MODEL_CLAUDE` para `"claude-3-5-sonnet-20240620"`.
    - **Otimização dos prompts de tradução :**
        - Os prompts para traduções diretas e notas de tradução foram enriquecidos para maior clareza e eficácia, incluindo instruções detalhadas sobre a preservação de metadados e elementos de formatação específicos.
    - **Refatoração do código :**
        - Substituição de `MistralClient` pela classe `Mistral` para a inicialização do cliente Mistral AI.
        - Reorganização dos imports para melhor legibilidade e manutenção.
        - Melhoria da segmentação dos textos e gerenciamento dos blocos de código para preservar a formatação original durante a tradução.
    - **Gerenciamento dos arquivos de saída :**
        - Inversão do modelo e do idioma no nome dos arquivos de saída (por exemplo, `f"{base}-{args.target_lang}-{args.model}.md"`), facilitando assim a organização e a busca pelas traduções.
    - **Aprimoramentos diversos :**
        - Limpeza do código removendo linhas vazias desnecessárias.
        - Ajustes menores para melhorar a estrutura e a legibilidade do script.
- **1.4** Novidades :
    - Suporte à API Claude da Anthropic para tradução
    - Otimização dos prompts para maior clareza e eficiência
    - Ajustes menores para melhorar a manutenção do código
- **1.3** Melhorias e novas funcionalidades :
    - Melhor gerenciamento dos blocos de código
    - Melhor gerenciamento dos arquivos de saída
    - Detecção de arquivos existentes melhorada
    - Opção `--force` para forçar a tradução
    - Inversão do modelo e do idioma no nome do arquivo de saída
- **1.2** Correção do changelog
- **1.1** Adição do suporte à API Mistral AI
- **1.0** Versão inicial - Suporte da API OpenAI

**Este documento foi traduzido da versão fr para a língua pt usando o modelo gpt-5-mini. Para mais informações sobre o processo de tradução, consulte https://gitlab.com/jls42/ai-powered-markdown-translator**

