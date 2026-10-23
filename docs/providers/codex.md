# Provider Codex (`--use_codex`) — quota d'abonnement ChatGPT

Cinquième provider : pilote le binaire `codex` officiel en sous-processus au lieu
d'appeler une API. La traduction est décomptée du quota de l'abonnement ChatGPT,
pas facturée à l'usage.

```bash
aipmt --use_codex --eco --file README.md --target_dir . --target_lang it
./regen_translations.sh --force                         # Codex est le défaut : gpt-6.1-sol
REGEN_MODEL=gpt-5.6-luna ./regen_translations.sh --force   # éco, si le propriétaire le demande
```

Coût réel mesuré : régénérer les 28 traductions (70 turns) avec `gpt-5.6-sol` a
consommé **1 point de pourcentage** de la fenêtre de 5 h sur un plan Plus, et
rien sur la fenêtre hebdomadaire. La fourchette officielle « 10-100 messages »
est calibrée sur des sessions agentiques longues, pas sur des appels one-shot.

Points à connaître avant de toucher à ce code :

- **Le binaire vient de `CODEX_BIN`, du `PATH`, ou du package pip
  `openai-codex-cli-bin`** (officiel OpenAI, ~250 Mo, hors `requirements.txt`
  car le provider est optionnel). Pas besoin de npm.
- **Ne jamais lire ni écrire `~/.codex/auth.json`.** Le `refresh_token` est
  rotatif et à usage unique : toute manipulation externe casse la session
  `codex login` de l'utilisateur. L'auth est déléguée au CLI, point.
- **`codex exec` lit stdin même quand le prompt est en argv.** Sans
  `communicate(input=...)` (ou `</dev/null`), la commande attend jusqu'au
  timeout sans jamais appeler le modèle.
- **Le timeout doit tuer le groupe de process.** Le `codex` de npm est un shim
  Node ; le vrai binaire Rust est un petit-fils qui survit à
  `subprocess.run(timeout=)` et continue à consommer du quota. D'où
  `Popen(start_new_session=True)` + `os.killpg`. La contrepartie de la session
  propre, pour les quatre CLI : l'agent ne reçoit ni le `SIGINT` d'un Ctrl-C ni
  le `SIGHUP` d'un terminal fermé. Vérifié par la revue du 2026-09-26 sur un
  faux binaire : il survivait à Python et finissait son tour sur le quota —
  `Popen.__exit__` n'attend que 0,25 s sur `KeyboardInterrupt`, et `SIGHUP`
  tuait Python sans exécuter aucun `finally`, laissant le répertoire privé
  d'Antigravity sur le disque, journal compris. D'où, dans
  `_codex_run_process`, `except BaseException: _codex_kill_group(proc); raise`
  (Ctrl-C et `SystemExit`), et `_kill_group_on_sigterm`, qui couvre `SIGTERM`
  ET `SIGHUP` — sortie en 128 + signal —, sauf un `SIGHUP` déjà ignoré
  (`SIG_IGN`, lancement par `nohup`, choix de l'utilisateur), et qui restaure
  `SIG_DFL` quand le gestionnaire précédent était `None` (posé hors de Python,
  impossible à reposer).
- **Exit code 0 ne veut pas dire succès** : inspecter la fin du tour dans la
  sortie JSONL — `turn.completed` ou `turn.failed` — et l'existence du
  fichier `-o`.
- **Un événement `error` n'est pas un échec.** `codex exec --json` y écrit
  aussi ses avis de relance, « Reconnecting... 2/5 », émis juste avant
  d'attendre puis de relancer le flux (`will_retry: true` ; vérifié dans le
  source de rust-v0.162.1, `core/src/responses_retry.rs` et
  `exec/src/event_processor_with_jsonl_output.rs`), et le tour peut ensuite
  aboutir. Jusqu'à la 1.16.3, aipmt échouait sur le premier `error` et jetait
  la traduction terminée : 3 des 14 échecs de la campagne du 2026-10-19
  portaient ce message. `_codex_terminal_event` ne retient plus un `error` que
  si le flux s'arrête sans fin de tour. Le 429 qui a épuisé les relances du
  CLI n'existe que sous forme de texte (« exceeded retry limit, last status:
  429 Too Many Requests », `RetryLimitReachedError`) : `CODEX_RETRY_LIMIT_429`
  le fait relancer après 30 puis 60 s. Le quota épuisé du forfait
  (`UsageLimitReachedError`, « You've hit your usage limit ») reste définitif.
- **Un 429 n'est pas un quota épuisé : le lire avant de conclure.** Le soir du
  2026-10-19, les 14 CHANGELOG à 4 jobs ont échoué (429 et segments tués à
  600 s) alors que le compte n'avait consommé que 34 % de sa fenêtre de 5 h et
  27 % de sa semaine. La lecture ne coûte rien : `codex app-server` en JSON-RPC
  sur stdin, `initialize` (avec `clientInfo`), puis `account/rateLimits/read`,
  dont `rateLimits.primary` et `secondary` portent `usedPercent`, et
  `rateLimitReachedType` la limite atteinte s'il y en a une.
- **Les clés API sont retirées de l'env du sous-processus.** C'est la garantie
  que le mode abonnement ne bascule pas silencieusement en facturation à
  l'usage — verrouillé par `test_env_strips_api_keys`.
- **Allowlist de modèles côté serveur** : les familles `gpt-5.6-*` et `gpt-6*`
  sont communes au CLI et à l'API Platform, mais un compte ChatGPT n'y a pas
  forcément droit à tout. Un modèle refusé donne un 400 « model is not
  supported when using Codex with a ChatGPT account », sans validation locale
  préalable — `CODEX_MODEL_PREFIXES` ne fait qu'avertir. Le catalogue servi au
  compte se lit sans quota dans `~/.codex/models_cache.json` (slug, `priority`,
  `context_window`). Mesuré sur ce compte le 2026-09-09 : `gpt-5.6-sol`,
  `terra` et `luna` répondent tous les trois par `codex exec -m`.
- **Défaut : `gpt-6.1-sol` depuis le 2026-10-19**, décision du propriétaire.
  C'est le premier modèle du catalogue (`priority` 1, 500 000 tokens de
  contexte), quand `gpt-5.6-sol` n'y venait plus qu'en sixième. Mesuré ce
  soir-là, le CHANGELOG entier (9 segments) en allemand, une traduction par
  modèle lancées en même temps : `gpt-6.1-sol` en 527 s, segments de 46 à
  70 s, note de traduction en 3,7 s ; `gpt-5.6-sol` en 906 s, segments de 36
  à 211 s, note en 182 s ; aucun événement d'erreur, structure identique pour
  les deux. `gpt-5.6-sol` reste disponible
  par `--model` ; l'éco reste `gpt-5.6-luna`, non remesuré.
- **Quota** : un segment consomme grosso modo un « message » de la fenêtre 5 h,
  mais OpenAI ne publie AUCUNE équivalence comptable — l'assimilation vient
  d'une observation locale, pas d'un contrat. Sur Plus, les fourchettes
  annoncées sont 250-2 000 msg/5 h pour Luna contre 10-100 pour Sol, et ce sont
  des estimations variables, pas des plafonds → toujours `--eco` en batch.
  Quota lisible en direct via `codex app-server` (RPC `account/rateLimits/read`).
- **Refusé en CI** : l'auth par abonnement n'est pas prévue pour un runner
  partagé : l'auth passe par un fichier de session personnel, qu'OpenAI
  déconseille d'injecter sur un runner. La mise en garde vise ce dépôt de
  secret, pas le caractère public du dépôt de code.
