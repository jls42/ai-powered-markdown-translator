"""Providers de traduction : un module par chemin d'appel.

API à clé (OpenAI, Mistral, Claude, Gemini, Grok, OpenRouter), CLI d'abonnement
(Codex, Grok) et routeur open source (OpenCode) partagent le socle de `base` ;
`registry` les résout et les dispatche. Ce fichier reste vide de code : tout
import d'un provider l'exécute d'abord, et il n'a rien à y faire.
"""
