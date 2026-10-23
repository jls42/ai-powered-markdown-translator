# Provider OpenCode (`--use_opencode`) — routeur open source, `--model` obligatoire

```bash
aipmt --use_opencode --model opencode/mimo-v2.5-free --file README.md --target_dir . --target_lang en
aipmt --use_opencode --model ollama/qwen2.5:7b --file README.md --target_dir . --target_lang de
REGEN_PROVIDER=opencode REGEN_MODEL=ollama/qwen2.5:7b ./regen_translations.sh --force
REGEN_PROVIDER=openrouter REGEN_ALLOW_PAID_API=1 REGEN_MODEL=z-ai/glm-5.2 ./regen_translations.sh --force
```

Huitième chemin. OpenCode (MIT) n'est pas un fournisseur mais un routeur vers
ceux que l'utilisateur a configurés dans OpenCode lui-même : clé, abonnement
(GitHub Copilot, ChatGPT, SuperGrok — Claude Pro/Max est interdit par
Anthropic depuis la 1.3.0), passerelle Zen (modèles gratuits SANS compte) ou
modèle local (Ollama, LM Studio, llama.cpp). Tout ce qui suit a été **mesuré
sur opencode 1.18.27**, pas déduit de la doc :

- **`--model provider/modèle` est obligatoire**, `--eco` sans effet. Sans
  `--model`, OpenCode retombe sur `opencode/big-pickle`, modèle gratuit
  « stealth » dont les échanges peuvent servir à l'entraînement : ce choix ne
  se fait pas à la place de l'utilisateur. Le « / » du modèle est remplacé
  avant toute interpolation dans un nom de fichier (`_model_filename_label`),
  et la garde anti-traversée contrôle la valeur INTERPOLÉE, plus la valeur
  brute — `..` seul reste refusé.
- **Un `--agent` inconnu ne fait pas échouer `opencode run`** : avertissement
  sur stderr et repli silencieux sur l'agent de codage, outils actifs. Le
  contrat de sortie vérifie donc l'absence de ce message, en plus de : rc 0,
  aucun événement `error`, aucun `tool_use`, dernier `step_finish` en `stop`,
  texte non vide.
- **Le JSON d'erreur est opaque** (« Unexpected server error », `ref`) : la
  cause réelle (`ProviderModelNotFoundError`, `ProviderAuthError`…) n'est que
  dans les logs `--print-logs`, d'où `--print-logs --log-level ERROR` et la
  lecture du champ `error="…"` de stderr.
- **Confinement par config inline** (`OPENCODE_CONFIG_CONTENT`, dernière
  dans l'ordre de fusion) : agent `aipmt` avec `permission: {"*": "deny"}` —
  aucun outil n'est même proposé au modèle —, `share: disabled`, pas de
  `--auto`, `--pure`. Répertoire de travail jetable et vide.
- **Contexte injecté à l'insu de l'appelant** : sans
  `OPENCODE_DISABLE_CLAUDE_CODE`, `~/.claude/CLAUDE.md` entre dans chaque
  prompt (515 tokens d'entrée au lieu de 186) ; sans
  `OPENCODE_DISABLE_PROJECT_CONFIG`, l'`AGENTS.md` du cwd aussi (une consigne
  « finir par BANANA » y a été suivie). Le `~/.config/opencode/AGENTS.md`
  global reste injecté, aucun interrupteur ne l'écarte : documenté au lieu
  d'être contourné par un `XDG_CONFIG_HOME` détourné, qui masquerait aussi les
  fournisseurs de l'utilisateur.
- **`--title` évite un appel LLM** : sans lui, OpenCode génère un titre de
  session par un tour supplémentaire sur le `small_model`.
- **stdin est lu jusqu'à EOF** et concaténé après l'argument : le segment
  part par stdin, jamais par argv, et `communicate()` ferme toujours.
- **Secrets** : même filtrage par motif que Codex/Grok, à une exception
  nominative près, `OPENCODE_API_KEY` (clé d'OpenCode lui-même, Zen/Go).
- **Modèles gratuits Zen** : `mimo-v2.5-free` traduit ce README en une passe
  (49 s, structure identique) ; `big-pickle` met 40 s pour 200 mots et deux
  requêtes simultanées y restent sans réponse 5 minutes ; `nemotron-3.5-lightning-free`
  n'a rien répondu en 3 minutes. D'où `max_jobs=2` au regen.
- **Modèle local** : Ollama configure souvent 4 096 tokens de contexte, les
  segments font jusqu'à 16 000 caractères → `PARAMETER num_ctx 32768` dans un
  Modelfile. Un 7B (qwen2.5) a abîmé une clôture de bloc de code sur un
  fichier d'essai, là où le modèle de la passerelle a tout préservé.
- **Pas de refus en CI** : contrairement aux CLI d'abonnement, une clé API ou
  un modèle auto-hébergé sur un runner sont des usages légitimes.
- OpenCode écrit `~/.config/opencode/` (config vide, `node_modules` de son
  runtime de plugins) et journalise chaque session dans sa base SQLite
  `~/.local/share/opencode/opencode.db`.

**Poste local (installé et mesuré le 2026-09-04)** — RTX 3060 12 Go, 62 Go de RAM :

- Ollama 0.33.3, mis à jour par le script officiel (`curl -fsSL
https://ollama.com/install.sh | sh`, sudo sans mot de passe sur ce poste).
  Le script réécrit l'unité systemd mais pas le drop-in
  `/etc/systemd/system/ollama.service.d/override.conf`, qui place le magasin
  sur `OLLAMA_MODELS=/mnt/msi/ollama` (NVMe de 916 Go). Il ne touche pas aux
  modèles téléchargés.
- Modèles : `gemma4:12b` (7,6 Go, Apache 2.0, 140+ langues) et `gpt-oss:20b`
  (13 Go, Apache 2.0), plus leurs variantes `gemma4-12b-32k` et `gpt-oss-20b-32k`
  créées depuis `~/ollama/*.Modelfile` : sous 24 Go de VRAM, Ollama plafonne le
  contexte à 4 096 par défaut, et l'API OpenAI-compatible n'a aucun moyen de le
  régler par requête — d'où `PARAMETER num_ctx 32768`. `qwen3.5:9b` a été
  supprimé après le tableau ci-dessous.
- `~/.config/opencode/opencode.jsonc` déclare le fournisseur `ollama`
  (`@ai-sdk/openai-compatible`, `http://127.0.0.1:11434/v1`) avec, sur chaque
  modèle, `options.reasoningEffort: "none"`. Indispensable et mesuré : Ollama
  active la réflexion par défaut sur Qwen 3.5 et Gemma 4, un Modelfile ne
  peut pas la couper ; sans l'option, « Le chat dort sur le tapis » coûte 919
  tokens de raisonnement et 68 s, avec elle 9 tokens.
- Écartés après recherche : GLM 5.3 Flash et tous les Kimi n'existent sur
  Ollama qu'en `:cloud` (320 B et ~1 T de paramètres) ; Qwen 3.6/3.8 font 18 à
  23 Go ; `translategemma` est limité à 2 K tokens d'entrée.

**Matrice des modèles testés sur un article réel du blog** (589 lignes, 140
liens, 3 citations EN protégées, mode `--news`, cible `en`, même commande) — le
barème du propriétaire est « aussi bien que gpt-5.6-luna / gpt-5.4-mini », et
les modèles qui échouent sont supprimés du poste :

| Modèle                                   | Poids  | Répartition           | Durée         | Résultat                                                                                                                                                                                                                     | Verdict                                |
| ---------------------------------------- | ------ | --------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `opencode/mimo-v2.5-free` (Zen, hébergé) | —      | —                     | 4 min 26 s    | structure identique, 0 écart                                                                                                                                                                                                 | référence                              |
| `ollama/gemma4-12b-32k`                  | 7,6 Go | 100 % GPU, 10 Go VRAM | 10 min 10 s   | liens/URL/tableaux/gras/code identiques ; 1 ligne de citation inventée (🇺🇸 + paraphrase), 1 attribution dupliquée                                                                                                            | insuffisant, le plus proche — conservé |
| `ollama/qwen3.5-9b-32k`                  | 6,6 Go | 100 % GPU             | 8 min 18 s    | idem citation inventée + gras/code ajoutés, 1 segment repassé                                                                                                                                                                | échec — supprimé                       |
| `ollama/qwen3.6-35b-a3b-32k`             | 22 Go  | 65 % CPU / 35 % GPU   | échec à 3 min | segment 1 : placeholder perdu, puis à la reprise un JSON `{"error": true, "message": "Translation contract violation…"}` à la place de la traduction                                                                         | échec — supprimé                       |
| `ollama/gpt-oss-20b-32k`                 | 13 Go  | 37 % CPU / 63 % GPU   | 11 min 28 s   | **structure identique** ; a retiré lui-même la ligne 🇫🇷 sous 2 citations sur 3, la 3ᵉ laissée intacte a été enlevée par `_cleanup_source_flag_for_en` (garde du mode news depuis février 2026, commune à tous les providers) | conservé                               |

Le point de rupture n'est ni la traduction ni la structure, mais **une seule
consigne** : « pour une cible anglaise, supprimer la ligne `> 🇫🇷 _…_` sous
chaque citation ». Deux façons de la rater, très inégales :

- **Omettre** (gpt-oss) : la ligne source reste telle quelle, avec son drapeau
  d'origine. `_cleanup_source_flag_for_en` la retire, comme elle le fait depuis
  février 2026 pour tous les providers — ce n'est pas un rattrapage ajouté pour
  un modèle, c'est le contrat du mode news.
- **Inventer** (Gemma 12B, Qwen 3.5) : produire `> 🇺🇸 _paraphrase anglaise_`,
  un drapeau qui n'existe nulle part dans le contrat. Aucune garde ne l'attrape,
  et le contenu publié est faux.

**Règle du propriétaire, formulée le 2026-09-04 : pas de rattrapage.** Un modèle
qui ne tient pas la consigne n'est pas utilisé ; on n'ajoute pas de
post-traitement et on ne raccourcit pas les segments pour lui plaire. Le prompt
news est déjà explicite (`REMOVE the whole source-translation line

> 🇫🇷 _..._`) : il n'y a rien à clarifier sans dégrader le reste.
