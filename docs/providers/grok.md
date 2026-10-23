# Providers Grok (`--use_grok` API / `--use_grok_cli` abonnement)

```bash
aipmt --use_grok --file README.md --target_dir . --target_lang pt      # clé XAI_API_KEY
aipmt --use_grok_cli --file README.md --target_dir . --target_lang pl
REGEN_PROVIDER=grok_cli ./regen_translations.sh --force
```

- **Mode API** : endpoint compatible OpenAI (`https://api.x.ai/v1`), donc le
  client et `_call_openai` sont réutilisés tels quels ; seul le `base_url`
  change. Une seule adaptation a été nécessaire : xAI émet `finish_reason:
end_turn` là où OpenAI émet `stop`.
- **Mode CLI : `grok-4.7` seul depuis le 2026-10-21.** Le CLI 1.0.52 refuse
  `grok-4.6` et `grok-4.5`, ses défauts jusqu'à la 1.17.0 (« Couldn't set
  model 'grok-4.6': Invalid params: "unknown model id" », code 1, au premier
  segment), alors que l'API les sert encore — liste lue le même jour par
  `GET /v1/models`, gratuit ; `grok-4.3`, palier éco de l'API, n'y a jamais
  été. Défaut et éco : `grok-4.7`, `--eco` sans effet. Le 19, `grok-4.6`
  traduisait encore. Le catalogue servi au compte se lit sans quota par
  `grok models`, et son cache, `~/.grok/models_cache.json`, donne la fenêtre
  (`context_window` 256 000) et l'effort par défaut (`high`). Jeu d'essai de la
  1.17.0 rejoué en `grok-4.7` : guide → en et brève `--news` → de, structure
  identique ; → en, le même écart attendu que tous les fournisseurs (la ligne
  française d'une citation, retirée, emporte son code en ligne).
- **« You are not authenticated. » n'est pas toujours une déconnexion.**
  L'appel de `grok models` qui rafraîchit un jeton expiré répond lui-même par
  ce message, et le suivant passe. Vu le 2026-10-19 (`~/.grok/auth.json`
  réécrit à la seconde de l'échec), reproduit le 2026-10-21 : appel de
  01:23:40 refusé, `auth.json` réécrit à 01:23:41, tous les suivants « logged
  in ». `_grok_preflight` repose donc la question après
  `GROK_AUTH_RECHECK_DELAY` (5 s) avant de conseiller `grok login` ; un
  `grok models` en échec, lui, échoue tout de suite. Validé de bout en bout par
  un faux `grok` qui rend ce message au premier appel puis passe la main au
  vrai : avis, seconde question, traduction aboutie ; le code de la 1.17.0
  conseillait `grok login` en 2 s.
- **`exit 0` ne prouve rien** : non authentifié, refus ou dépassement de tours
  sortent tous en 0. Le contrat de sortie exige les quatre : code retour 0, pas
  de `{"type":"error"}` sur stdout, `stopReason == end_turn`, texte non vide.
- **Le prompt part par fichier** (`--prompt-file`) : le CLI ne lit pas stdin, et
  un segment en argv serait visible dans `ps`.
- **Confinement plus faible que Codex, et c'est assumé.** Le sandbox OS de Grok
  ne s'applique pas sur beaucoup de postes Linux (AppArmor + deny-list
  runtime-socket sur `/run/podman` en 0700), et un profil **intégré** qui échoue
  démarre **non confiné en silence**. On ne demande donc aucun profil par
  défaut, sans jamais retomber silencieusement : la protection repose sur
  `--deny` (catch-all `*` inclus), seule couche mesurée fail-closed. Opt-in
  strict via `GROK_TRANSLATE_SANDBOX`.
- **`--max-turns 1` est à proscrire** : le compteur est incrémenté après le tour
  d'outils, la sortie serait tronquée. Le plancher mesuré est 2.
- **Quota non mesurable** : pool hebdomadaire partagé avec Chat, Imagine et
  Voice, aucune commande ne l'expose. D'où `max_jobs=2` au regen.
