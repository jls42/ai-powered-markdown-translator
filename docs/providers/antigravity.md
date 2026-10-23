# Provider Antigravity (`--use_antigravity`) — quota d'abonnement Google

```bash
aipmt --use_antigravity --file README.md --target_dir . --target_lang en
aipmt --use_antigravity --eco --file README.md --target_dir . --target_lang ja
REGEN_PROVIDER=antigravity ./regen_translations.sh --force   # abonnement : sans dérogation
agy -p /usage --output-format json                            # quota restant, sans en consommer
```

Dixième chemin. Pilote `agy`, le CLI officiel d'Antigravity (binaire Go de
219 Mo, `~/.local/bin/agy`), en mode headless : la traduction est décomptée du
quota de l'abonnement Google AI Pro ou Ultra, pas facturée au token. **C'est le
seul chemin vers ce quota** : Gemini CLI ne sert plus les comptes Pro, Ultra ni
gratuits depuis le 2026-06-18
(<https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/>),
et le SDK Python Antigravity ne s'authentifie que par `GEMINI_API_KEY` ou
Vertex/ADC (<https://antigravity.google/docs/sdk/overview/>). Tout ce qui suit a
été **mesuré sur agy 1.2.11 le 2026-09-26**, pas déduit de la doc :

- **Binaire** : `AGY_BIN`, puis le `PATH`, puis `~/.local/bin/agy`, où il est
  installé sans que le `PATH` de la session le sache. **Jamais `antigravity`**,
  lanceur de l'IDE, qui ouvrirait l'éditeur. Plancher 1.2.11, vérifié au
  préflight : avant, un agent de projet pouvait rester introuvable en headless.
  Le chemin rendu est ABSOLU (`os.path.abspath`) : l'appel tourne avec pour
  `cwd` le répertoire privé, où un `AGY_BIN` ou une entrée de `PATH` relatifs
  étaient introuvables (reproduit par la revue sur un faux binaire). `AGY_BIN`
  n'est pas accepté d'un `.env` de projet (cf. `docs/environnement.md`).
- **Auth** : le compte Google de l'abonnement, rangé dans le trousseau du
  système (Secret Service, par D-Bus), **jamais lu par aipmt** — lancer `agy`
  une fois et s'y connecter suffit. Une session déconnectée (« Authentication
  required », « authentication failed or timed out », « not logged in ») donne
  `ANTIGRAVITY_LOGIN_HINT` : relancer `agy` dans un terminal de la session
  graphique pour se connecter ; sans trousseau joignable, agy range son jeton
  dans un fichier de `~/.gemini`, que l'isolation masque volontairement.
- **Plateformes : `_antigravity_check_platform()`**, appelée par
  `_init_antigravity_client` juste après le refus en CI, avant la validation
  du modèle et tout lancement d'agy. Refus en fermé :
  - `os.name == "nt"` → `ANTIGRAVITY_UNSUPPORTED_WINDOWS`. Go y lit
    `USERPROFILE`, `APPDATA`, `LOCALAPPDATA` et `TEMP`, pas `HOME` ni `TMPDIR`
    (doc de Go et chaînes du binaire ; non mesuré sous Windows) : rien n'y
    isolerait l'appel des réglages ni de l'historique, et sans session propre
    agy garderait la console pour y demander un code (changelog 1.1.2).
  - Linux sans bus de session → `ANTIGRAVITY_NO_SESSION_BUS`.
    `_antigravity_session_bus_reachable` accepte un `DBUS_SESSION_BUS_ADDRESS`
    non vide, sinon l'existence de `$XDG_RUNTIME_DIR/bus`, à défaut de
    `/run/user/<uid>/bus` — la socket par défaut que la bibliothèque D-Bus
    essaie seule (mesuré : un `env -i` sans aucune des deux variables
    s'authentifie quand même). Sans bus — SSH, conteneur, serveur —, agy range
    son jeton dans un FICHIER sous le HOME réel (changelog 1.1.3 : « bypasses
    the keyring when no D-Bus session bus is present »), que le HOME privé
    masque : le préflight y attendrait 60 s un code, comme dans le cas mesuré
    « bus masqué », puis conseillerait une reconnexion qui ne résout rien. Non
    mesuré de bout en bout sur un hôte sans bus.
  - macOS passe : trousseau du système, pas de D-Bus. L'isolation par HOME n'y
    est pas mesurée ; la garde de facturation, qui lit la configuration
    effective, y tient.
  - **Piège CI** : les runners GitHub (Linux) n'ont pas de bus de session. Tout
    test qui appelle `_init_antigravity_client` neutralise
    `_antigravity_check_platform` (ou `_antigravity_session_bus_reachable`) par
    un patch sur `aipmt.providers.antigravity` — sinon vert sur ce poste, rouge
    en CI.
- **Invocation** : `agy --output-format json --agent aipmt
--disable-slash-commands --log-file <journal> --model <slug>`, segment sur
  stdin, **sans `-p`** : avec `-p`, agy ignore stdin ; sans lui, stdin n'étant
  pas un terminal, il passe en mode print et lit stdin jusqu'à EOF. Un stdin
  vide ouvre la TUI (rc 0, erreur non JSON sur stdout). `translate()` ne
  transmet plus aucun segment blanc, à aucun provider : il le rend tel quel
  (`not segment.strip()`). La revue l'avait reproduit — 16 001 caractères
  terminés par « \n\n\n » donnent un second segment « \n\n », dont le refus
  faisait échouer le FICHIER après consommation du quota du premier.
  `_antigravity_attempt` garde son refus en dernier filet.
- **Isolation par appel** : HOME, TMPDIR et répertoire de travail privés
  (`tempfile`, 0700), effacés après l'appel avec le journal, qui contient
  l'adresse du compte. agy s'authentifie quand même, par le trousseau, et le
  jeton rafraîchi y est réécrit pour toutes les sessions. Rien n'est hérité de
  l'utilisateur : ni son `settings.json` (`permissions.allow`, qui laissait
  l'agent par défaut lancer `ls` et `git` sans rien demander ;
  `allowNonWorkspaceAccess` ; `modelProvider`), ni ses `GEMINI.md` et
  `AGENTS.md` globaux, plugins, MCP, hooks et skills. Rien n'est écrit dans son
  historique : chaque appel y laissait une conversation d'environ 200 Ko, texte
  traduit compris, et la campagne de sondes y avait laissé ~95 conversations et
  évincé 17 entrées du cache `implicit/`, plafonné à 100. Parmi les variables
  de session, seules `XDG_RUNTIME_DIR` et `DBUS_SESSION_BUS_ADDRESS` passent la
  liste d'autorisation (cf. Environnement) : c'est par le bus de session qu'agy
  atteint le trousseau (bus masqué : 60 s d'attente d'un code de connexion,
  puis échec). `XDG_CONFIG_HOME` et ses sœurs n'y sont pas, si bien que tout
  chemin dérivé tombe dans le HOME privé. Vérifié de bout en bout : aucun
  fichier écrit dans `~/.gemini/antigravity-cli`.
- **Agent confiné**, écrit dans le répertoire jetable :
  `.agents/agents/aipmt.md`, frontmatter `name`, `description`, `tools: []`,
  `excludeDefaultComponents: true`, `inheritCustomizations: false`, puis
  `# aipmt`, puis les instructions système et `ANTIGRAVITY_AGENT_CONTRACT`.
  Environ 800 tokens d'entrée au lieu de 12 400 avec l'agent par défaut.
  `excludeDefaultComponents` seul laisse les hooks du workspace exécuter leurs
  commandes et injecter leur texte ; `inheritCustomizations: false` les coupe.
- **Repli silencieux, démontré** : un agent introuvable donne rc 0, status
  `SUCCESS` et l'agent de codage, 57 outils actifs. À « Le chat dort. », il a
  répondu « Chut, ne le réveillons pas ! 🐱💤 Que puis-je faire pour vous
  aujourd'hui ? ». Aucune trace sur stdout ni stderr : **seul le journal le
  dit**. La garde refuse si le journal annonce le repli, et exige le marqueur
  POSITIF du chargement de l'agent — l'agent par défaut écrit `agent=false`. Ce
  ne sont que des lignes de log, pas un contrat : une évolution du format fait
  refuser la traduction au lieu de retirer la garde en silence.
- **Marqueurs ancrés sur une ligne ENTIÈRE, au format glog mesuré**
  (`_GLOG_LINE` : sévérité `[IWEF]`, date `MMJJ`, heure à la microseconde, fil,
  `fichier:ligne]`, en `re.MULTILINE`, fin de ligne comprise). Lignes réelles
  d'agy 1.2.11, à reprendre telles quelles dans les fixtures :

  ```text
  I0926 10:36:51.895710       1 conversation_manager.go:512] Starting new conversation (agent=true)
  I0926 10:36:08.477937       1 conversation_manager.go:512] Starting new conversation (agent=false)
  W0926 10:30:43.128362       1 session.go:94] Agent "agent-inexistant" not found, falling back to default
  I0926 10:36:47.628476       1 server_oauth.go:196] applyAuthResult: email=compte@example.com, authMethod=consumer, quotaProject=
  ```

  Pourquoi l'ancrage : le binaire contient aussi
  `HandleUserInput called with text: %q`, qui recopierait le segment dans le
  journal. Non ancré, un document qui cite ces messages satisfaisait la garde
  positive à la place d'agy (vérifié par la revue sur un journal synthétique).
  `%q` échappe les sauts de ligne : l'écho reste sur une seule ligne, que
  l'ancrage écarte. Mesuré le 2026-09-26 : aucun des 78 journaux réels des
  sondes ne porte cette ligne au niveau de log par défaut. Validé contre le vrai
  agy après correctif : agent forcé inexistant → « agy est retombé en silence
  sur son agent de codage », réponse refusée.

- **Voie de facturation attestée par appel** : le journal doit porter la ligne
  glog `applyAuthResult: … authMethod=consumer` (l'abonnement), sinon refus
  avec `ANTIGRAVITY_LOGIN_HINT`. Et toute occurrence de `authMethod=` ou
  `auth_method=` — les deux graphies figurent dans le binaire — portant une
  autre valeur que `consumer`, OÙ QU'ELLE SOIT dans le journal, fait refuser :
  même hors d'une ligne glog, puisque refuser est le côté sûr. Conséquence
  pour la documentation : ne jamais écrire dans le README ni le CHANGELOG, que
  ce chemin peut traduire, un exemple de `authMethod=` suivi d'une autre
  valeur ; un agy qui recopierait l'entrée ferait refuser le segment.
- **Environnement : une liste d'AUTORISATION** (`_antigravity_env_base`),
  préflight compris, dans cet ordre :

  1. ne passent que `ANTIGRAVITY_KEPT_ENV_VARS` — `PATH`, `LANG`, `LANGUAGE`,
     `TZ`, `TERM`, `USER`, `LOGNAME`, `XDG_RUNTIME_DIR`,
     `DBUS_SESSION_BUS_ADDRESS`, `HTTP_PROXY`, `HTTPS_PROXY`, `ALL_PROXY`,
     `NO_PROXY` et leurs minuscules, `SSL_CERT_FILE`, `SSL_CERT_DIR` — et le
     préfixe `LC_`. C'est ce dont un `env -i` a prouvé qu'agy a besoin. Tout le
     reste disparaît, dont `HOME`, `TMPDIR`, `XDG_CONFIG_HOME` et ses sœurs,
     `DISPLAY` et `BROWSER` (aucun navigateur ne doit s'ouvrir depuis un job de
     traduction), `OPENAI_BASE_URL` et toute variable `AGY_`, `GOOGLE_`,
     `GEMINI_`… ;
  2. `_strip_secret_env` (motifs `API_KEY`, `_TOKEN`, `SECRET`, `PASSWORD`,
     `CREDENTIALS`) passe quand même : un nom de la liste qui porterait un de
     ces motifs resterait refusé ;
  3. `AGY_CLI_DISABLE_AUTO_UPDATE=true` (`ANTIGRAVITY_ENV_OVERRIDES`) ;
  4. `HOME` et `TMPDIR` privés, propres à l'appel (`_antigravity_env`).

  Pourquoi une autorisation et non un refus : la première version retirait des
  familles de préfixes (`AGY_`, `ANTIGRAVITY_`, `JETSKI_`, `CLOUD_CODE_`,
  `CLOUDSDK_`, `GOOGLE_`, `GEMINI_`), et la revue du 2026-09-26 a trouvé dans
  les chaînes du binaire des surcharges d'endpoint qui la traversaient :
  `AICODE_ENDPOINT_URL` et ses variantes `BAICODE_*`, `UNLEASH_URL` (drapeaux
  de fonctionnalité), `GCE_METADATA_HOST` — leur effet sur agy n'est pas
  mesuré, et c'est justement le problème d'une liste de refus. Mesuré en
  revanche : `AGY_GATEWAY_URL` envoie le prompt à une passerelle tierce,
  `AGY_ADC_AUTH` bascule sur un projet Google Cloud facturé, `CLOUD_CODE_URL`
  détourne l'endpoint authentifié vers n'importe quelle URL ; `GEMINI_API_KEY`
  ne bascule sur l'API que si `settings.json` porte `modelProvider="gemini"`,
  ce que le HOME neuf n'a pas. Les proxies et certificats transmis ne peuvent
  venir que de l'environnement exporté ou de `~/.config/aipmt/.env` : le filtre
  de la couche projet les écarte (cf. `docs/environnement.md`).
  `AGY_CLI_DISABLE_AUTO_UPDATE` est posée APRÈS le filtrage : la valeur `1` est
  sans effet, `true` fait écrire « Auto-update disabled via environment
  variable » au journal. Sans elle, un HOME neuf lance à chaque appel le
  vérificateur de mise à jour, dans sa propre session, hors d'atteinte du
  `killpg`.

- **Préflight, zéro quota** (usage à zéro, mesuré) : `agy --version` ≥ 1.2.11,
  puis `agy -p /config --output-format json --log-file …` dans le même
  isolement. Refus si `useG1Credits` ne vaut pas `false` (crédits IA payants
  au-delà du quota), si `modelProvider` n'est pas vide (clé API), si `gcp`
  n'est pas nul (projet Google Cloud), ou si le journal n'atteste pas
  `authMethod=consumer`. **Un réglage ABSENT compte comme un problème, pour
  chacun des trois** (`_antigravity_billing_problems`, sentinelle
  `_ANTIGRAVITY_ABSENT` affichée « (absent de /config) », messages « doit
  valoir false / doit être vide / doit être nul ») : une version d'agy qui en
  renommerait un ne doit pas faire passer un contrôle qui n'a rien vérifié. La
  première version, par `.get()`, acceptait `{"useG1Credits": false}` seul, ou
  un `gcp` renommé en `gcpProject` (vérifié par la revue). Sur le compte du
  propriétaire le 2026-09-26 : `useG1Credits` false, 0 crédit restant,
  `modelProvider` vide, `gcp` null. `/config` prend de 2 à 11 s, sous un plafond de 120 s
  (`ANTIGRAVITY_CHECK_TIMEOUT`) : une session déconnectée y attend 60 s un code
  de connexion. Les deux commandes du préflight passent par
  `_antigravity_run_check`, un `subprocess.run` enveloppé dans
  `_kill_group_on_sigterm({})` : un `SIGTERM` ou un `SIGHUP` reçu pendant le
  contrôle lève `SystemExit`, `subprocess.run` tue agy, et le répertoire privé
  est effacé en remontant. Sans ce gestionnaire, Python mourait sans nettoyage
  et le répertoire restait sur le disque avec son journal (relevé par la
  revue ; le test appelle le gestionnaire au lieu d'envoyer un vrai signal au
  lanceur de tests).
- **Contrat de sortie**, dans cet ordre : rc 0 ET objet JSON ET
  `status == "SUCCESS"`, sinon échec — rc 3 = échec du modèle ou de l'agent,
  avec une ligne `AGY_ERROR: {json}` sur stderr (depuis la 1.2.6), lue par
  `json.JSONDecoder().raw_decode` juste après le marqueur
  (`_antigravity_agy_error_data` → dict ou None ; `_antigravity_agy_error` →
  chaîne compacte pour le message) : `raw_decode` s'arrête à la fin de l'objet,
  un code couleur ou un « } » écrits après ne s'y mêlent pas ; rc 1 = argument
  refusé, un modèle inconnu par exemple, sans repli silencieux depuis la 1.1.2 ;
  la réponse partielle que peut porter le JSON d'un échec n'est jamais lue.
  Puis la garde du journal (agent, `authMethod`). Puis
  `_antigravity_reject_non_answers` : refus si le JSON porte `denied_actions`,
  `command` ou `error`, ou si stderr contient « print timeout », « no output
  produced » ou « may be truncated ». Enfin `_antigravity_extract_answer` :
  `response` non vide, qui reprend la fin de ligne du SEGMENT —
  `text.rstrip("\n")`, plus `"\n"` si le segment finit par un saut de ligne.
  agy termine chaque réponse par un saut de ligne, que le segment en ait un ou
  non (mesuré sur les quatorze modèles) ; rendue telle quelle, la réponse
  insérait une ligne vide à la jonction d'une coupure en milieu de phrase et
  scindait le paragraphe — ou un tableau, sur une coupure dure (revue). Validé
  contre le vrai agy dans les deux sens.
- **Jamais `--print-timeout`** : à expiration, la sortie partielle sort en
  `SUCCESS`, rc 0. Le plafond est externe — `AGY_TIMEOUT`, 900 s par segment,
  démarrage compris, agy payant de 2 à 30 s d'appels réseau avant d'envoyer le
  message — et tue le groupe de processus, `SIGTERM` puis `SIGKILL`
  (`base._codex_run_process`, qui prend désormais un `cwd` : agy n'a pas
  d'option de répertoire de travail et y cherche l'agent). Ctrl-C et `SIGHUP`
  tuent aussi le groupe, puis le répertoire privé est effacé (cf. `docs/providers/codex.md`,
  « Le timeout doit tuer le groupe de process »).
- **Relance pilotée par `retryable`** :
  `_antigravity_is_rate_limited(text, agy_error)` reçoit le détail ET le dict
  d'`AGY_ERROR`, que le détail vienne ou non du champ `error` du JSON :

  - `AGY_ERROR` porte un booléen `retryable` → il décide SEUL. agy réessaie
    déjà lui-même, en processus, les 502, 503, 504 et les 429 par minute (son
    changelog), puis dit si l'échec restant l'est encore ;
  - sinon, aucune relance si le texte contient « exhausted » : chez Google,
    `RESOURCE_EXHAUSTED` porte le même 429 qu'une limite par minute, mais une
    fenêtre de 5 h épuisée ne se rendra pas en 90 s ;
  - sinon, relance sur « rate limit », « rate_limit », « too many requests »,
    `429` comme nombre, ou 502, 503 et 504 comme nombres — les pannes
    passagères qu'agy réessaie déjà lui-même (depuis la 1.17.1, cf. ci-dessous)
    —, cherchés dans le détail ET dans `AGY_ERROR`. « quota » seul n'est pas un
    marqueur, et 500 n'est pas relancé.

  3 tentatives, 30 puis 60 s d'attente. La première version, sur sous-chaînes,
  relançait trois fois une fenêtre épuisée (`\b429\b` captait son code) et
  jamais un 503 `retryable: true` (revue, sur des lignes `AGY_ERROR`
  synthétiques : le format réel d'un échec n'a pas été mesuré).
  **Format réel vu le 2026-10-20** : code 0, `status: ERROR`, « API error
  (attempt 2): UNAVAILABLE (code 503): The service is currently
  unavailable. » au segment 4/10 d'un CHANGELOG — agy avait déjà réessayé une
  fois. Rien n'y disait l'échec réessayable : aipmt l'a pris pour définitif et
  le fichier a échoué après avoir consommé les trois premiers segments ;
  relancé à la main, il est passé. **Relancé depuis la 1.17.1**
  (`_ANTIGRAVITY_HTTP_TRANSIENT_REGEX`). Validé de bout en bout par un faux agy
  qui rend ce message, dans le champ `error` du JSON, au premier appel de
  traduction, puis passe la main au vrai, préflight compris : relance après
  30 s, traduction aboutie, structure identique ; le code de la 1.17.0
  abandonnait le fichier en 8 s.
  L'avis de relance, commun aux CLI (`_retry_on_rate_limit`), cite désormais
  l'erreur : il annonçait « rate limit » pour tout, 503 compris, de quoi
  chercher la cause du côté du quota.

- **Filtre de contenu de Google** : agy peut rendre rc 0, `status: ERROR`,
  « Your previous response was blocked by content safety filters: … sensitive
  words that violate Google's Generative AI Prohibited Use policy » — une
  sortie refusée par Google, pas par aipmt. Vu une fois le 2026-09-26 à la
  régénération : segment 4/8 du CHANGELOG en hindi, en `gemini-3.8-flash-medium`
  (entrées 1.12.0 et 1.11.1, où figurent « kill », « SIGKILL », « injection »).
  Aléatoire : le même modèle avait traduit ce CHANGELOG une heure plus tôt, et
  la relance de la langue seule a abouti. Aucune relance automatique — le
  message n'est ni une limite de débit ni `retryable` — : le fichier échoue
  après avoir consommé le quota des segments précédents, et l'on relance la
  langue seule. Une relance unique sur ce message serait défendable ; non
  faite.
- **Injection** : grâce à `--disable-slash-commands`, un segment qui commence
  par `!commande`, `@fichier` ou `/commande` n'est ni exécuté, ni résolu, ni
  développé. Sans lui, un segment « /help » s'exécutait à la place d'être
  traduit.
- **Modèles** : les identifiants d'`agy models`, effort compris —
  `gemini-3.8-flash-{high,medium,low}`, `gemini-3.7-flash-{high,medium,low}`,
  `gemini-3.6-flash-{high,medium,low}`, `gemini-3.1-pro-{high,low}`,
  `claude-sonnet-4-6`, `claude-opus-4-6-thinking`, `gpt-oss-120b-medium` ; tous
  figurent dans `MODEL_TOKEN_LIMITS`. Un nom de base seul (`gemini-3.7-flash`)
  est refusé par agy : aipmt le refuse avant l'appel et propose les suffixes
  qui existent — `-high` ou `-low` pour un Pro, `-medium` ou `-low` pour un
  Flash (la première version proposait `gemini-3.1-pro-medium`, qu'agy
  refuse). Défauts **fixés par les mesures du 2026-09-26** (ci-dessous), écrits
  en toutes lettres et jamais alias de `DEFAULT_MODEL_GEMINI` :
  `DEFAULT_MODEL_ANTIGRAVITY` = `gemini-3.8-flash-medium`,
  `ECO_MODEL_ANTIGRAVITY` = `gemini-3.7-flash-low`. Le matin, le défaut était
  `gemini-3.7-flash-medium` et 3.8 medium écarté sur deux arguments ; la
  mesure de l'après-midi, demandée par le propriétaire, en a démenti un : les
  « 79 % de raisonnement » venaient d'une sonde isolée, et sur des documents
  3.8 medium raisonne autant que 3.7 medium (63 % contre 60 % des tokens de
  sortie). Reste qu'il est un quart plus lent. `--reasoning_effort` : sans
  effet, avertissement.
- **Quota** : deux groupes, Gemini et « Claude and GPT models », chacun avec une
  fenêtre de 5 h et une hebdomadaire, lisibles gratuitement par
  `agy -p /usage --output-format json` (`remaining_fraction`, `reset_time`).
  Texte officiel de `/usage` : le quota se décompte proportionnellement au coût
  des tokens, et la limite hebdomadaire dépend du palier de l'abonnement. Un
  appel Claude ou GPT-OSS a coûté environ 1 % de la fenêtre de 5 h, contre
  0,05 % en Flash : avertissement. Coût d'une traduction réelle, en points de
  la fenêtre de 5 h par million de caractères source (mesures ci-dessous) :
  16,2 en `gemini-3.8-flash-medium`, 14,2 en `gemini-3.7-flash-medium` (12 sur
  la campagne du matin), 7,6 en `gemini-3.7-flash-low`, 7,2 en
  `gemini-3.8-flash-low` ; la semaine en perd six fois moins.
  **`usage.output_tokens` du JSON d'agy INCLUT `thinking_tokens`** : le texte
  rendu vaut `output_tokens − thinking_tokens` (mesuré, rapport caractères par
  token constant d'un appel et d'un modèle à l'autre), et la part de
  raisonnement se lit `thinking / output`, pas `thinking / (thinking + output)`.
- **Parallélisme** : 4 appels simultanés mesurés sans erreur, chacun dans son
  HOME, puis les 45 traductions de la campagne du 2026-09-26 à 4 en parallèle,
  sans un échec. D'où `max_jobs=4` au regen. Le plafond de 1 800 s par job,
  repris de Codex, est validé par la mesure : le CHANGELOG entier en hindi
  (HEAD 1.14.1, 94 080 caractères) traduit en 273 s, marge ×6,5 ; celui de la
  1.15.0 (111 861 caractères) en 350 s par `gemini-3.8-flash-medium`, marge ×5.
- **Refusé en CI**, comme Codex et Grok CLI : l'auth par trousseau personnel
  n'est pas prévue pour un runner partagé. Repli proposé par le message :
  `--use_gemini` avec `GOOGLE_API_KEY` (`_CLI_PROVIDER_CI_FALLBACK`).
- **Câblage** : les CLI ont leur propre chaîne de dispatch
  (`_call_cli_provider` dans `registry`), une seule fonction dépassant ce que
  Codacy tolère ; un nom de CLI inconnu y lève au lieu de retomber sur un autre
  abonnement.
- **Bout en bout, 2026-09-26** : un guide Markdown (front matter, gras, lien à
  parenthèses, code en ligne, bloc de code indenté dans une liste, tableau,
  citation) traduit en anglais en 14 s préflight compris, structure identique,
  note de traduction ajoutée ; rien d'écrit dans `~/.gemini/antigravity-cli`.
  Revalidé après les correctifs de la revue, contre le vrai agy : le même guide
  en allemand, structure identique en 19 s, rien d'écrit dans `~/.gemini`.

**Campagne du 2026-09-26**, par `aipmt --use_antigravity` lui-même
(`--add_translation_note --force`, `--news` pour l'article), quatre traductions
en parallèle (`xargs -P 4`), chacune comparée à sa source par
`scripts/compare_structure.py`, quota lu par `agy -p /usage` avant et après
chaque phase. Sources : le README de HEAD, c'est-à-dire celui de la 1.14.0
(600 lignes, 39 075 caractères — pas la révision figée du 9 septembre des
autres lignes du tableau du README) ; le CHANGELOG de HEAD (1.14.1, 315 lignes, 94 080
caractères) ; l'article dense du tableau de compatibilité,
`ia-actualites-3-sep-2026.mdx` (589 lignes, 91 973 caractères).

| Phase    | Modèle                    | Document                          | Écrites · sans écart | Durée par langue                 |
| -------- | ------------------------- | --------------------------------- | -------------------- | -------------------------------- |
| Pilote   | `gemini-3.7-flash-medium` | README (ja, ar, hi)               | 3/3 · 3/3            | 72 à 84 s                        |
| Pilote   | `gemini-3.7-flash-low`    | README (ja, ar, hi)               | 3/3 · 3/3            | 42 à 56 s                        |
| Pilote   | `gemini-3.8-flash-low`    | README (ja, ar, hi)               | 3/3 · 3/3            | 54 à 58 s                        |
| Pilote   | `gemini-3.8-flash-medium` | README (ja, ar, hi)               | 3/3 · 3/3            | 103 à 128 s                      |
| Pilote   | `gemini-3.7-flash-medium` | CHANGELOG entier (hi)             | 1/1 · 1/1            | 273 s                            |
| Complète | `gemini-3.7-flash-medium` | article `--news`, 14 langues      | 14/14 · 14/14        | médiane 3 min 14 s (162 à 259 s) |
| Complète | `gemini-3.7-flash-medium` | README, 14 langues                | 14/14 · 13/14        | médiane 1 min 22 s (59 à 110 s)  |
| Complète | `gemini-3.7-flash-low`    | article `--news` (en, ja, ar, hi) | 4/4 · 4/4            | médiane 1 min 52 s (85 à 139 s)  |
| Rejouée  | `gemini-3.8-flash-medium` | article `--news`, 14 langues      | 14/14 · 14/14        | médiane 3 min 59 s (191 à 272 s) |
| Rejouée  | `gemini-3.8-flash-medium` | README, 14 langues                | 14/14 · 14/14        | médiane 1 min 43 s (73 à 154 s)  |

- **Choix des défauts** : le matin, aucun écart de structure ne départageait
  les quatre Flash du pilote, et le défaut qualité est resté dans la famille
  qui avait le plus de preuves, Gemini 3.7 Flash ; 3.8 medium était écarté
  sur la foi d'une sonde (cf. Modèles). L'après-midi, le propriétaire a
  demandé 3.8 Flash, le modèle que l'interface d'agy propose ; les mesures
  ci-dessous l'ont départagé : même structure sur un lot commun, puis la
  campagne rejouée sans aucun écart sur l'article ni sur le README, là où
  3.7 medium perdait un gras en coréen, et les liens internes intacts dans
  les quatorze README, que 3.7 medium cassait en italien. Défaut qualité :
  `gemini-3.8-flash-medium`. L'éco reste `gemini-3.7-flash-low` : aucun des
  deux Flash en `-low` ne raisonne (0 token) et chacun coûte moitié moins,
  mais 3.8 low a doublé en hindi les trois liens internes d'un README et
  perdu un gras dans le CHANGELOG.
- **Le seul écart du matin** : le README en coréen, « gras 36≠37 », un mot en
  gras de moins, en `gemini-3.7-flash-medium`. La campagne rejouée en 3.8
  n'en a aucun.
- **Mode `--news` en anglais** : les trois lignes `> 🇫🇷 _…_` absentes de la
  sortie, aucun 🇺🇸 ni 🇬🇧 inventé — l'échec qui a disqualifié Gemma 4 et
  Qwen 3.5 —, les trois citations anglaises verbatim. C'est le modèle qui les a
  retirées : aucun journal de la campagne ne porte la ligne « (cleanup) » que
  `_cleanup_source_flag_for_en` imprime quand il agit. Même résultat en
  `gemini-3.7-flash-low` et en `gemini-3.8-flash-medium`.
- **Quota** (`remaining_fraction` du groupe Gemini) : la campagne complète —
  32 traductions, 2,20 millions de caractères source — a fait passer la
  fenêtre de 5 h de 88,87 % à 62,61 % (26,3 points) et la semaine de 91,05 % à
  86,67 % (4,4 points) ; le pilote — 13 traductions, 0,56 million de
  caractères — 6,2 et 1,0 point. Le groupe « Claude and GPT models » n'a pas
  bougé. Soit environ 12 points de la fenêtre de 5 h par million de
  caractères : un README de 40 000 caractères ≈ 0,5 point, une régénération
  des 28 traductions de ce dépôt ≈ un quart de la fenêtre. Valable pour le
  palier du compte du propriétaire : `/usage` dit que la limite hebdomadaire
  dépend du palier. La campagne rejouée en `gemini-3.8-flash-medium`, 28
  traductions et 1,83 million de caractères : 24,5 points de la fenêtre de
  5 h (88,55 % → 64,02 %) et 4,1 de la semaine (77,37 % → 73,28 %), soit
  13,4 points par million.

**Mesures de l'après-midi du 2026-09-26**, demandées par le propriétaire
(« Gemini 3.8 Flash, ça serait mieux »). Par `aipmt` lui-même, l'usage de
chaque appel lu dans le JSON d'agy par un espion posé sur
`_antigravity_parse_payload`, le quota par `/usage` entre deux modèles, lancés
l'un après l'autre pour que l'écart soit attribuable. Lot commun : le README
de la 1.15.0 en anglais, japonais et hindi, le CHANGELOG en hindi, 254 031
caractères, quatre traductions en parallèle.

| Modèle                    | Écrites · sans écart | Segments repassés | Quota 5 h | Raisonnement | README / CHANGELOG |
| ------------------------- | -------------------- | ----------------- | --------- | ------------ | ------------------ |
| `gemini-3.7-flash-medium` | 4/4 · 4/4            | 0                 | 3,6 pts   | 60 %         | 94–132 s / 287 s   |
| `gemini-3.8-flash-medium` | 4/4 · 4/4            | 1                 | 4,1 pts   | 63 %         | 125–171 s / 350 s  |
| `gemini-3.8-flash-low`    | 3/4 · 2/4            | 2                 | 1,8 pt    | 0 %          | 75–96 s / 216 s    |
| `gemini-3.7-flash-low`    | 3/4 · 3/4            | 3                 | 1,9 pt    | 0 %          | 68–85 s / 157 s    |

- Les segments repassés et les deux README refusés tiennent tous au même
  jeton, `#ANCHOR2#`, celui d'un lien placé entre parenthèses (cf.
  `docs/liens-internes.md`). L'écart de 3.8 low : un gras de moins dans le CHANGELOG hindi.
- Le coût par million de caractères varie avec le contenu : 16,2 points pour
  3.8 medium sur ce lot, chargé en hindi, 13,4 sur la campagne rejouée.
- Qualité du texte, lue sur des passages du README anglais : les trois
  modèles se valent ; 3.7 medium ajoute parfois ce que la source ne dit pas
  (« explicitly mentioned », « no official text »), 3.8 medium colle un peu
  plus au sens. Une lecture, pas une mesure.

**Conditions d'utilisation, que le README dit sans les adoucir.** Les CGU
d'Antigravity (section 6, <https://antigravity.google/terms>) et la FAQ
(<https://antigravity.google/docs/faq/>) interdisent l'accès au service par un
logiciel tiers sur le login Antigravity — Claude Code, OpenClaw et OpenCode y
sont cités —, sous peine de suspension du compte. aipmt ne réutilise jamais le
jeton : il lance le binaire officiel en mode headless, que Google documente pour
les scripts et la CI (<https://antigravity.google/docs/cli/headless/>). Un
membre de Google a jugé « standard », sur le forum officiel le 2026-09-25, de
lancer `agy -p` depuis un script local pour son propre workflow (réponse non
contractuelle :
<https://discuss.ai.google.dev/t/is-using-the-official-agy-cli-through-a-local-mcp-server-with-third-party-ai-agents-permitted/184829>).
Aucun texte ne tranche le cas d'un outil distribué : l'utilisateur engage son
compte.

**Données** : CGU section 5, les Interactions (prompts, réponses, métadonnées)
peuvent servir à améliorer les produits et le ML de Google et être relues par
des humains, sans distinction entre l'offre gratuite et Pro/Ultra. Le retrait
passe par le réglage `enableTelemetry`, dont l'effet exact n'est pas documenté.
D'où la consigne du README : documents publics (README, articles), jamais de
confidentiel. **Non mesuré** : si `enableTelemetry` vit dans `settings.json`,
comme les réglages que le HOME privé écarte, le retrait posé par l'utilisateur
ne suit pas dans les appels d'aipmt — `agy -p /config` lancé dans le même
isolement le trancherait.
