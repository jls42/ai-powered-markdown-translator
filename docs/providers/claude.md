# Provider Claude (`--use_claude`) — mesures de référence

Détail des mesures du provider Claude par l'API Anthropic, cité par CLAUDE.md.
À lire avant de toucher à la requête de `src/aipmt/providers/anthropic.py` ou
de monter le SDK `anthropic` d'une version majeure.

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
