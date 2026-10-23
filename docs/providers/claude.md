# Provider Claude (`--use_claude`) — API Anthropic, réflexion coupée modèle par modèle

Audit et campagne du 2026-10-18, **mesurés** — `GET /v1/models`, page des
dépréciations, appels réels :

- **Le réglage qui coupe la réflexion dépend du modèle.** Sonnet 5, Haiku 4.5
  et Haiku 5.5 acceptent `thinking: {"type": "disabled"}`. **Sonnet 5.5 le
  refuse par un HTTP 400** (« To turn thinking off on this model, send
  "thinking": {"type": "between_tools"} instead ») : `between_tools` coupe sa
  réflexion préalable, et la réponse ne porte aucun bloc `thinking`. Opus 5.5
  et Fable 5.x refusent les deux et n'acceptent que la réflexion adaptative,
  c'est-à-dire aucun champ `thinking`. Avant la 1.17.0,
  `--use_claude --model claude-sonnet-5-5` échouait au premier segment.
- **Source de vérité : `capabilities.thinking.types` de
  `GET /v1/models/{id}`**, gratuit, un `supported` par réglage — la doc demande
  de lire ces capacités plutôt que de déduire du nom. `_CLAUDE_THINKING_BY_MODEL`
  fige le réglage des modèles mesurés — Haiku 5.5 compris, qui accepte
  `disabled` mais y gagne d'être laissé en réflexion adaptative (point
  suivant) ; un modèle absent descend
  `_CLAUDE_THINKING_CASCADE` (`disabled`, `between_tools`, aucun champ) au
  premier 400 qui parle de `thinking`, et le réglage accepté est mémorisé dans
  `_CLAUDE_ACCEPTED_THINKING`, comme pour Gemini. Toute autre erreur remonte.
  Sans la table, le modèle par défaut repaierait un 400 et un avertissement au
  premier segment de chaque exécution.
- **Débit du compte** (en-têtes `anthropic-ratelimit-*`) : 5 000 requêtes,
  5 M de tokens d'entrée et 1 M de sortie par minute — huit traductions en
  parallèle sans un 429.
- **Prix** (page Pricing, par million de tokens, entrée / sortie) : Sonnet 5
  et Sonnet 5.5 2 $ / 10 $ ; Haiku 4.5 1 $ / 5 $ ; Haiku 5.5 0,10 $ / 0,50 $
  pour un prompt de moins de 100 000 tokens, 0,50 $ / 2,50 $ au-delà — et son
  tokenizer compte environ 30 % de tokens de plus que celui d'Haiku 4.5.
- **Haiku 5.5 sans réflexion laisse des paragraphes en français.** La garde
  « Output contains untranslated source excerpt » refuse alors le fichier :
  11 articles sur 14, 8 README sur 14. Avec sa réflexion adaptative (effort par
  défaut `medium`), il traduit tout ; restent des titres changés de niveau et
  des jetons de code perdus en arabe et en hindi.

**Campagne**, par `aipmt --use_claude` lui-même, sur les deux documents des
mesures du README — l'article dense en `--news` et le README de la 1.14.0 —,
quatorze langues chacun, quatre traductions en parallèle par modèle ; l'usage
de chaque appel est lu dans sa réponse par un espion posé sur une copie du code.

| Modèle (réflexion)                    | Article : écrites · sans écart | README : écrites · sans écart  | Médianes article / README | Coût   |
| ------------------------------------- | ------------------------------ | ------------------------------ | ------------------------- | ------ |
| `claude-sonnet-5-5` (`between_tools`) | 14/14 · 14/14                  | 14/14 · 14/14                  | 3 min 37 s / 1 min 18 s   | 9,21 $ |
| `claude-haiku-5-5` (`disabled`)       | 3/14 · 2/14                    | 6/14 · 6/14                    | 2 min 00 s / 50 s         | 0,41 $ |
| `claude-haiku-5-5` (adaptative)       | 14/14 · 11/14 (ja, ko, zh)     | 12/14 · 12/14 (ar, hi refusés) | 2 min 54 s / 1 min 14 s   | 0,57 $ |
| `claude-haiku-4-5` (`disabled`)       | 14/14 · 7/14                   | 14/14 · 14/14                  | 6 min 00 s / 2 min 06 s   | 3,67 $ |

**Défauts du 2026-10-18** : `claude-sonnet-5-5` en qualité, sans discussion ;
`claude-haiku-5-5`, réflexion adaptative, en `--eco` à la place de
`claude-haiku-4-5`. Les deux Haiku butent sur le même passage de l'article, la
brève « Réouverture des inscriptions Business et Enterprise » : Haiku 4.5 passe
son titre `###` au niveau 1 dans 7 langues — en japonais, il le laisse même en
français, ce qu'aucune garde ne voit —, Haiku 5.5 le change de niveau ou le
dédouble dans 3. Haiku 5.5 écrit moins de fichiers (26 contre 28 : deux README
refusés en arabe et en hindi, jetons de code perdus, que les gardes ont
arrêtés), mais plus sans écart (23 contre 21), deux fois plus vite, pour 6,4
fois moins cher ; Haiku 4.5 est « legacy ». Un refus se relance ; un titre
déplacé passe en silence.

Sonnet 5.5 n'a repassé aucun segment — 98 appels pour l'article, six segments
et la note de traduction par langue — et a gardé les liens internes des quatorze
README. En anglais, il a retiré lui-même les lignes `> 🇫🇷 _…_`, sans inventer
de drapeau ni laisser travailler le nettoyage de repli, et les trois citations
anglaises sont recopiées telles quelles dans les quatorze langues.

## Version d'API `2026-10-21` (SDK `anthropic` 2.x) — mesurée le 2026-10-23

Le SDK `anthropic` 2.x envoie `anthropic-version: 2026-10-21` par défaut, là où
le 1.x envoyait `2023-06-01`. Une installation depuis PyPI le prend depuis le
2026-10-21 : la borne de `pyproject.toml` est un `>=`. Ne concerne que
`--use_claude` : `--use_claude_code` passe par le CLI de Claude Code, qui gère
sa propre version d'API.

**Ce que la version refuse par un 400**, d'après le guide de migration :

- `temperature`, `top_p` et `top_k`, même à leur valeur par défaut — sur tous
  les modèles, dans les lots comme dans le comptage de tokens. Ne jamais en
  ajouter à la requête : le SDK 2 ne les connaît d'ailleurs plus ;
- un bloc `document` placé directement dans un message `assistant` ;
- des `citations` non vides sur un bloc `text` d'un message `user`.

aipmt n'envoie rien de tout ça. Sa requête — `model`, `max_tokens`, `messages`
en dict, `thinking` selon `_CLAUDE_THINKING_BY_MODEL` — porte les mêmes champs
et les mêmes valeurs sous les deux SDK : requête interceptée par un faux
transport HTTP (`httpx2.MockTransport`), sans appel réseau.

**Les deux changements du SDK 2 qui touchent aipmt**, sans rien casser :

- **la clé part en `Authorization: Bearer`**, plus en `X-Api-Key`. L'API
  accepte les deux, mais un proxy placé derrière `ANTHROPIC_BASE_URL` qui ne
  lit que `X-Api-Key` ne verra plus la clé. La parade, une fonction `auth` sur
  le client HTTP, est dans le guide, § « If a proxy or gateway reads
  `X-Api-Key` » ;
- **un client ne porte plus qu'une identité** : deux identités passées au
  constructeur lèvent `ValueError`. aipmt passe la clé explicitement : elle
  reste la seule envoyée, sans erreur, même avec `ANTHROPIC_AUTH_TOKEN` et une
  autre `ANTHROPIC_API_KEY` exportés (mesuré par le même faux transport).

Le reste du SDK 2 ne touche pas aipmt : `MessageParam` devenu une union par
rôle (un message écrit en dict ne change pas), `betas` retiré des méthodes
Models non bêta (aipmt ne les appelle pas). La garde du SDK qui exige le
streaming au-delà de dix minutes présumées existe toujours ; le `timeout`
explicite de l'appel continue de l'en dispenser.

**Validation**, selon la règle des majeures de SDK (un appel réel) :

- lock reconstruit comme le job « Fermeture et tests du lock », dans un venv
  jetable : 41 épinglages, ni trou ni orphelin, `pip check` propre — les
  dépendances du SDK 2.1.0 sont celles du 1.15.0 ;
- tests 746 + 53 verts sur 2.1.0, comme sur 1.15.0 ;
- deux traductions réelles d'un guide (front matter, lien à parenthèses, bloc
  de code dans une liste, tableau, citation) en anglais, quatre requêtes en
  tout, toutes en HTTP 200 sur `2026-10-21` avec la clé en `Bearer` :
  Sonnet 5.5 (`between_tools`, aucun bloc `thinking`) et Haiku 5.5 (réflexion
  adaptative, bloc `thinking` écarté) ; structure identique à la source pour
  les deux (`scripts/compare_structure.py`), note de traduction et saut de
  ligne final compris ; 0,011 $ en tout.

Le SDK 2 passe sous licence Apache 2.0 (MIT avant), compatible avec la
GPL-3.0-or-later d'aipmt ; le dépôt ne tient pas de liste des licences de ses
dépendances.

Sources : le guide de migration,
<https://platform.claude.com/docs/en/api/migration-2026-10-21>, et les notes
de version de la plateforme,
<https://platform.claude.com/docs/en/release-notes/overview>.
