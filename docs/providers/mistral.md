# Provider Mistral (`--use_mistral`) — plafonds bas, propres à chaque modèle

Audit du 2026-09-17, **mesuré sur l'API**, pas lu dans la doc :

- **Résolution des alias**, publiée par `GET /v1/models` (champ `aliases`) :
  `mistral-large-latest` → `mistral-large-2512` (Large 3, décembre 2025),
  `mistral-medium-latest` → `mistral-medium-2604` (Medium 3.5),
  `mistral-small-latest` → `mistral-small-2603` (Small 4). Aucune date de retrait
  annoncée pour les trois.
- **Plafonds par modèle, sur ce compte** (en-têtes `x-ratelimit-*`) : Large 3
  **15 requêtes/min** (400 000 tokens) ; Small 4 100 requêtes et **100 000
  tokens/min** ; Medium 3.5 1 000 requêtes et 500 000 tokens. **Le 429 ne porte
  aucun `Retry-After`.** Le SDK ne réessayant rien par défaut,
  `MISTRAL_RETRY_CONFIG` (backoff de 2 à 60 s, abandon à 5 min) est ce qui
  empêche un 429 de perdre le fichier : 20 appels d'affilée sur Large 3 passent
  tous, le 16ᵉ après 33 s. Paralléliser au-delà du plafond n'accélère rien, ça
  fait attendre ; pour une campagne qui mesure des durées, 1 ou 2 traductions
  simultanées par modèle.
- **Raisonnement** : aucun des trois ne raisonne par défaut (18 tokens de sortie
  sur une phrase). Large 3 refuse `reasoning_effort` (HTTP 400) ; Small 4 et
  Medium 3.5 l'acceptent, et en `high` la réponse devient une liste de blocs
  `thinking` + `text` (5 189 tokens de sortie pour une phrase sur Medium 3.5).
  `_mistral_text` écarte ces blocs. `--reasoning_effort` n'est pas transmis à
  Mistral.
- **Prix** (doc officielle, entrée / sortie par million) : Large 3 $0.5 / $1.5,
  Medium 3.5 **$1.5 / $7.5**, Small 4 $0.15 / $0.6.

**Campagne du 2026-09-17** : 14 langues, l'article dense du tableau de
compatibilité (`ia-actualites-3-sep-2026.mdx`, dans le dépôt du blog) en
`--news`, et le README de la 1.14.0 — pas la révision figée du 9 septembre, qui
n'est plus sur le poste. Deux traductions simultanées par modèle et par
document ; les cinq tombées sur un 429 ont été relancées une à une.

| Modèle     | Article : écrites / sans écart | README : écrites / sans écart |
| ---------- | ------------------------------ | ----------------------------- |
| Large 3    | 10/14 · 6/14                   | 14/14 · 10/14                 |
| Medium 3.5 | 13/14 · 1/14                   | 14/14 · 6/14                  |
| Small 4    | 12/14 · 8/14                   | 13/14 · 8/14                  |

Medium 3.5 perd ou change de niveau des sous-titres `###` dans 9 langues sur
l'article, et coûte 3 fois Large 3 en entrée, 5 fois en sortie : **modèles par
défaut inchangés**, décision du 2026-09-17. Les refus de Large et Small sont
tous des gardes qui mordent — citation `NEWSQUOTE` restaurée deux fois, code en
ligne ou URL perdus —, aucun n'est dû à l'infrastructure.
