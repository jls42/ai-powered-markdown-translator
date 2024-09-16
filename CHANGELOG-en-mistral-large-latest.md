### Changelog

- **1.0** Version initiale - Support de l'API OpenAI
- **1.1** Ajout du support de l'API Mistral IA
- **1.2** Fix du changelog
- **1.3** Améliorations et nouvelles fonctionnalités :
    - Gestion améliorée des blocs de code
    - Gestion améliorée des fichiers de sortie
    - Détection de fichiers existants améliorée
    - Option `--force` pour forcer la traduction
    - Inversion du modèle et de la langue dans le nom du fichier de sortie
- **1.4** Nouveautés :
    - Support de l'API Claude d'Anthropic pour la traduction
    - Optimisation des prompts pour une clarté et efficacité accrues
    - Ajustements mineurs pour améliorer la maintenance du code
- **1.5** Améliorations :
    - **Mise à jour des clés API et des modèles par défaut :**
        - **OpenAI :** Mise à jour de `DEFAULT_MODEL_OPENAI` à `"gpt-4o"`.
        - **Mistral AI :** Mise à jour de `DEFAULT_MODEL_MISTRAL` à `"mistral-large-latest"`.
        - **Claude d'Anthropic :** Ajout de `DEFAULT_ANTHROPIC_API_KEY` et mise à jour de `DEFAULT_MODEL_CLAUDE` à `"claude-3-5-sonnet-20240620"`.
    - **Optimisation des prompts de traduction :**
        - Les prompts pour les traductions directes et les notes de traduction ont été enrichis pour une meilleure clarté et efficacité, incluant des instructions détaillées sur la préservation des métadonnées et des éléments de formatage spécifiques.
    - **Refactorisation du code :**
        - Remplacement de `MistralClient` par la classe `Mistral` pour l'initialisation du client Mistral AI.
        - Réorganisation des imports pour une meilleure lisibilité et maintenance.
        - Amélioration de la segmentation des textes et gestion des blocs de code pour préserver le formatage original lors de la traduction.
    - **Gestion des fichiers de sortie :**
        - Inversion du modèle et de la langue dans le nom des fichiers de sortie (par exemple, `f"{base}-{args.target_lang}-{args.model}.md"`), facilitant ainsi l'organisation et la recherche des traductions.
    - **Améliorations diverses :**
        - Nettoyage du code en supprimant les lignes vides inutiles.
        - Ajustements mineurs pour améliorer la structure et la lisibilité du script.

**This document has been translated from the fr version to the en language using the mistral-large-latest model. For more information about the translation process, see https://gitlab.com/jls42/ai-powered-markdown-translator.**

