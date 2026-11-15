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
- **Mode API : `grok-4.7` et effort envoyé, depuis le 2026-11-15.** Même prix
  que `grok-4.6` (2 $ et 6 $ par million de tokens, lus sur
  `GET /v1/language-models`, gratuit) ; l'éco reste `grok-4.3` (1,25 $ et
  2,50 $). Jusque-là, aipmt n'envoyait `reasoning_effort` qu'aux GPT-5 : un
  Grok raisonnait à son niveau par défaut sur chaque segment. Sonde sur un
  guide de 20 lignes, tokens de raisonnement pour une centaine de tokens de
  sortie :

  | Modèle     | sans paramètre | `none`     | `low` | `medium` | `high` |
  | ---------- | -------------- | ---------- | ----- | -------- | ------ |
  | `grok-4.7` | 695            | refusé 400 | 33    | 44       | 540    |
  | `grok-4.6` | 478            | refusé 400 | 279   | 415      | 493    |
  | `grok-4.3` | 373            | 0          | 404   | 696      | 504    |

  aipmt envoie désormais `low` hors `--eco` et `none` en `--eco`. Sur le README
  en japonais, `grok-4.7` rend une structure identique à `low` en 190 s et à
  `medium` en 711 s ; sans paramètre, l'essai a été arrêté après 17 minutes.
  `grok-4.3` en `--eco` : trois traductions écrites sur trois, en 176 à 201 s,
  une sans écart, deux avec un ou deux codes en ligne en trop. La 1.18.0
  installée, sans le paramètre, sur le même README : une sans écart en 310 s,
  une refusée par la garde des jetons (un code en ligne perdu).

- **Un refus de xAI ne se lit pas dans son message**, qui se réduit à « Error
  code: 400 » : le motif est dans le corps de l'erreur, sous deux graphies —
  « This model does not support `reasoning_effort` value `none`. » pour une
  valeur refusée, « does not support parameter reasoningEffort » pour un modèle
  sans raisonnement (`grok-4.20-0309-non-reasoning`). Le repli d'aipmt lit donc
  le corps : `none` refusé repart en `low`, puis sans le paramètre.
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
  Revalidé le 2026-11-15 sur le CLI 1.0.77 : `grok-4.7` reste le seul modèle
  du catalogue de l'abonnement, et un guide traduit garde sa structure.
- **Un `grok models` qui hérite de `XAI_API_KEY` liste le catalogue de l'API**
  (`auth_method: api_key` dans `~/.grok/models_cache.json`), pas celui de
  l'abonnement, et réécrit ce cache : vu le 2026-11-15 depuis un script qui
  avait importé `aipmt`, dont `config` charge le `.env`. aipmt retire les clés
  de l'environnement avant de lancer le CLI ; un diagnostic à la main doit en
  faire autant (`env -u XAI_API_KEY grok models`).
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
