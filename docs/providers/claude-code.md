# Provider Claude Code (`--use_claude_code`) — quota d'abonnement Claude

```bash
aipmt --use_claude_code --file README.md --target_dir . --target_lang en   # sonnet, effort low
aipmt --use_claude_code --eco --file README.md --target_dir . --target_lang ja   # sonnet aussi : --eco sans effet
REGEN_PROVIDER=claude_code ./regen_translations.sh --force   # abonnement : sans dérogation, 4 jobs
```

Onzième chemin. Pilote `claude -p`, le CLI officiel de Claude Code, sur le quota
de l'abonnement Claude (Pro ou Max). Contrat **mesuré sur Claude Code 2.1.283 le
2026-09-26** (phase 0 du plan, sondes une à une par l'environnement du module,
`~/.claude.json` sauvegardé, jeton surveillé par `stat` seulement) :

- **Invocation** : `claude -p --output-format stream-json --verbose
--include-hook-events --model <alias> --system-prompt-file <privé> --tools ""
--safe-mode --restricted --strict-mcp-config --disable-slash-commands
--no-session-persistence --permission-prompts none --no-chrome --max-turns 1
--settings '{"disableAllHooks":true,"crossSessionInbound":"refuse","fastMode":false}'`
  (+ `--effort`, sauf pour haiku qui l'ignore) ; toutes ces options passent
  ensemble. Segment sur stdin **précédé d'un saut de ligne** : sous
  `--disable-slash-commands`, un message qui commence par `/` n'atteint pas le
  modèle — réponse synthétique « /usage isn't available in this environment. »,
  `success`, `num_turns: 0`, `modelUsage: {}`. `#`, `##`, `!` et `@` en tête
  passent normalement. Le saut de ligne ne change pas la sortie ; les bords du
  segment sont restitués à l'identique.
- **Environnement : liste d'AUTORISATION** (`CLAUDE_CODE_KEPT_ENV_VARS`), puis
  `_strip_secret_env`, puis `CLAUDE_CODE_ENV_OVERRIDES`. Mesuré : une session
  Claude Code exporte quinze variables (`CLAUDECODE`, `CLAUDE_CODE_SESSION_ID`,
  `CLAUDE_CODE_MESSAGING_SOCKET`, `CLAUDE_CODE_MESSAGING_TOKEN`,
  `CLAUDE_CODE_CHILD_SESSION`, `CLAUDE_PID`, `CLAUDE_CODE_EFFORT_LEVEL`…) qu'un
  `claude -p` hériterait. **`CLAUDE_CODE_DISABLE_ATTACHMENTS=1` est
  indispensable** : sans lui, un `@chemin` du document devient une pièce
  jointe (+214 tokens d'entrée) et le modèle rend `{"file_path": …}` au lieu de
  traduire. `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` fait annoncer
  `analyticsDisabled: true` par `auth status` et `analytics_disabled: true` par
  l'`init` : la preuve que l'environnement forcé est arrivé.
- **Préflight, zéro quota** : version ≥ 2.1.283, aucun réglage géré
  (`/etc/claude-code/managed-settings*`), `claude auth status --json`
  (`loggedIn`, `authMethod: claude.ai`, `apiProvider: firstParty`,
  `analyticsDisabled: true`, `subscriptionType ∈ {max, pro}`, **aucune clé
  `apiKeySource`**, `configDirectory` attendu ; identité jamais affichée), puis
  `claude -p /usage --output-format json` SANS `--disable-slash-commands` :
  réponse locale (`num_turns: 0`, `modelUsage: {}`, `local_command: usage`) qui
  commence par « You are currently using your subscription to power your Claude
  Code usage ».
- **Attestation par appel** : `system/init` → `apiKeySource` vaut `none` (encore
  émis en 2.1.283, contrairement à une rumeur), modèle de la famille de l'alias
  (`opus` → `claude-opus-5-5`, `sonnet` → `claude-sonnet-5`, `haiku` →
  `claude-haiku-4-5-20251001`), `fast_mode_state: off`, version = préflight,
  `tools`/`mcp_servers`/`skills`/`slash_commands` vides, plugins intégrés
  seulement (`agents-md@builtin` figure même sous `--safe-mode`, sans rien
  charger) ; `result` → `success`, `is_error` faux, `num_turns: 1`,
  `stop_reason: end_turn`, `permission_denials` vide, `modelUsage` = {modèle
  d'init} exactement ; aucun événement `hook_*`. `rate_limit_event` →
  `isUsingOverage`/`overageInUse`/type `overage`/`status: rejected` arrêtent
  tout sans relance ; `unifiedWindows.<fenêtre>.utilization` est gardé et
  vérifié avant chaque segment (plafond `AIPMT_CLAUDE_MAX_UTILIZATION`, 0,8).
- **Échecs mesurés** : session déconnectée (config dir vide) → `auth status`
  `loggedIn: false, authMethod: none` ; `-p` → assistant `error:
authentication_failed`, `result` `is_error: true` « Not logged in · Please run
  /login » — sous un `subtype: success` : c'est `is_error` qui fait foi. Sortie
  plafonnée (`CLAUDE_CODE_MAX_OUTPUT_TOKENS=8`) → rc 1, `is_error: true`,
  `num_turns: 4` (le CLI relance seul), `terminal_reason: api_error`.
- **Garde-fous d'Opus 5.5, mesurés le 2026-09-26 : le piège du `success`.**
  Dans les quatorze langues de l'article de veille, le dernier segment revenait
  en `success`, `is_error: false`, `stop_reason: end_turn`, `num_turns: 2`, avec
  pour texte « I can't continue this translation. Only the part delivered before
  the stop is available… ». Le flux le dit : un `system/informational` « Opus
  5.5's safeguards stopped the response above · continuing once with that
  noted », puis un message `user` synthétique (« stopped by a safety
  classifier »), puis le refus du modèle. **Seul `num_turns == 1` l'arrêtait.**
  Déclencheur isolé : la brève « 279 liants VHL sans proline », seule →
  `system/model_refusal_no_fallback` avec `api_refusal_category: "bio"` (c'est
  `CLAUDE_CODE_NO_MODEL_FALLBACK` qui empêche le repli silencieux vers un autre
  modèle), `result` `is_error: true`, `stop_reason: refusal`, texte « API Error:
  Opus 5.5's safeguards flagged this session (…/legal/aup)… can sometimes flag
  biology-research-adjacent work… change your model ». La brève voisine
  (aquarelle) passe ; `sonnet` a traduit l'article entier dans les quatorze
  langues. `_claude_code_check_refusal` nomme désormais les garde-fous et leur
  catégorie, sans relance, et conseille `--model sonnet`. **Chaque déclenchement
  est un signalement sur le compte du propriétaire** (16 ce soir-là, campagne et
  sondes comprises) : ne pas rejouer ce contenu sur Opus pour « vérifier ».
- **Isolation** : 14 sondes, chacune dans son répertoire temporaire → aucune
  entrée ajoutée à `~/.claude.json` (44 projets avant et après), aucun fichier
  dans `~/.claude`, jeton jamais rafraîchi, aucun processus restant. Même sans
  `--safe-mode`, `CLAUDE.md` et `AGENTS.md` canaris du répertoire de travail ne
  sont pas chargés (`--restricted` et le prompt système remplacé) : les gardes
  restent, ceinture et bretelles. Le socket de messagerie s'ouvre quand même en
  `-p` ; `crossSessionInbound: refuse` jette ce qui y arrive.
- **Bout en bout** : un guide Markdown (front matter, gras, lien, code en ligne,
  bloc indenté dans une liste, tableau, citation) traduit en anglais par
  `aipmt --use_claude_code --model sonnet --eco`, structure identique, note de
  traduction comprise, en 4,3 s ; répertoire de travail effacé.
- **Quota partagé avec les sessions interactives** : le `rate_limit_event` de la
  première sonde annonçait la semaine du propriétaire à **98 %** (99 % une heure
  plus tard), réinitialisation le mercredi 30 septembre à 18 h. `/usage` en `-p`
  détaille l'origine : 96 % des dernières 24 h viennent de sessions lourdes en
  sous-agents, 88 % à plus de 150 000 tokens de contexte. D'où le plafond avant
  segment. Les mesures ont attendu la réinitialisation, le soir même.
- **Défauts mesurés le 2026-09-26** : `sonnet` à l'effort `low`, en `--eco`
  aussi (`--eco` sans effet). Lot préalable (README en/ja/hi + CHANGELOG hi de
  la 1.15.0, 2 jobs), quatre réglages : `sonnet low` 4/4 sans écart,
  `sonnet medium` 3/4, `opus low` et `opus medium` 3/4 — le même gras scindé
  par l'ordre des mots hindi. Raisonnement 0 token pour `sonnet`, 1 % de la sortie pour
  `opus medium` : **l'effort ne sert à rien pour traduire**, d'où `low` partout.
  Puis les campagnes (article dense `--news` + README 1.14.0, quatorze langues,
  4 jobs) :

  | Modèle         | Article : écrites · sans écart         | README : écrites · sans écart       | Médianes article / README | Équivalent API |
  | -------------- | -------------------------------------- | ----------------------------------- | ------------------------- | -------------- |
  | `sonnet` (low) | 14/14 · 13/14 (zh : gras +1)           | 14/14 · 13/14 (ar : tableau)        | 409 s / 140 s             | 10,48 $        |
  | `opus` (low)   | 0/14 (garde-fous, cf. ci-dessus)       | 14/14 · 14/14                       | — / 107,5 s               | 20,02 $        |
  | `haiku`        | 14/14 · 11/14 (titre ## → #, en/pl/ro) | 14/14 · 14/14 (liens doublés en en) | 953,5 s / 242 s           | 9,00 $         |

  `haiku` ignore `--effort` mais raisonne quand même : 61 % de ses tokens de
  sortie (888 000 sur 1,46 million), d'où deux fois le temps de `sonnet` et une
  économie réduite à 14 % en équivalent API. Couper ce raisonnement n'a pas été
  essayé. Ses trois écarts ne perdent aucun contenu : les 41 titres sont là, un
  `##` devenu `#`.

  En arabe, `sonnet` a collé la ligne ❌ de la légende des symboles à la fin de
  la ligne ⚠️ (saut de ligne perdu) : le texte est là, mais un rendu GFM ignore
  les cellules en trop — la ligne disparaît à l'affichage. Liens internes
  intacts partout (28/28 pour `sonnet` et pour `opus`), citations anglaises
  verbatim, en anglais aucune ligne 🇫🇷 ni drapeau inventé. Quota de la campagne
  `sonnet` : 9 points de la fenêtre de 5 h, 2 de la semaine (majorant : la
  session qui pilotait puise dans le même quota ; l'« équivalent API » est
  `total_cost_usd`, que Claude Code calcule même sur abonnement, et se prête
  mieux à la comparaison). Aucun segment repassé, aucune relance, aucun
  « extra usage » pour `sonnet`. Quatre appels simultanés n'ont produit aucune erreur de débit
  ni de verrou de connexion : d'où `max_jobs=4` au regen.

- **Refus** : CI, Windows, alias hors `{opus, sonnet, haiku}` (`fable` et `best`
  facturent en crédits en `-p`, `[1m]` aussi, un identifiant complet se fige).
- **Conditions** : la page légale admet l'utilisateur qui se connecte « to the
  unmodified Claude Code binary with their own Claude subscription », mais
  interdit aux développeurs tiers de « route requests through Free, Pro, or Max
  plan credentials on behalf of their users » ; l'aide Claude préfère la clé API
  pour les outils tiers « including open-source projects » et se réserve
  d'imputer leur usage sur les crédits. Citations vérifiées sur les pages
  brutes le 2026-09-26. Le README le dit sans l'adoucir.
