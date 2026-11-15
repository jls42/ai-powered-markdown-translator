# Modèles, constantes et usage recommandé

## Recommended Usage

**Pour les traductions de CE dépôt, voir `docs/traductions.md` : Codex + `gpt-6.1-sol`,
Antigravity en repli, jamais l'API.** Ce qui suit vaut pour un usage général de l'outil sur une clé API.

For batch translations (README, CHANGELOG, blog articles), use `--eco` mode:

```bash
aipmt --file README.md --target_dir . --source_lang fr --target_lang en --eco --add_translation_note
```

This uses faster/cheaper models (gpt-6-luna) which are sufficient for documentation translation.

## Key Constants

- `EXCLUDE_PATTERNS`: Paths containing these strings are skipped (`traductions_`, `venv`, `PRIVACY.md`)
- `MODEL_TOKEN_LIMITS`: Dict mapping model names to max token limits for segmentation

### Default Models (2026)

| Provider    | Quality (default)                     | Economic (`--eco`)      |
| ----------- | ------------------------------------- | ----------------------- |
| OpenAI      | `gpt-6.1-terra`                       | `gpt-6-luna`            |
| Claude      | `claude-sonnet-5-5`                   | `claude-haiku-5-5`      |
| Mistral     | `mistral-large-latest`                | `mistral-small-latest`  |
| Gemini      | `gemini-4-hydrogen`                   | `gemini-3.1-flash-lite` |
| Codex       | `gpt-6.1-sol`                         | `gpt-5.6-luna`          |
| Grok API    | `grok-4.7`                            | `grok-4.3`              |
| Grok CLI    | `grok-4.7`                            | `grok-4.7` (sans effet) |
| Antigravity | `gemini-3.8-flash-medium`             | `gemini-3.8-flash-low`  |
| Claude Code | `sonnet` (effort `low`)               | `sonnet` (sans effet)   |
| OpenCode    | `--model provider/modèle` obligatoire | idem                    |

### Model lifecycle — dates to watch (audited 2026-08-29, Claude re-audited 2026-10-18, all providers re-audited 2026-11-15)

| Échéance       | Impact                                                                                                                                                                     |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ~~2026-10-15~~ | `claude-haiku-4-5` : date-plancher **passée sans retrait** — toujours « Active » le 2026-10-18, préavis d'au moins 60 jours avant tout retrait.                            |
| **2027-06-30** | `claude-sonnet-5` : date-plancher de retrait (« not sooner than »). Comme Haiku 4.5, rangé parmi les « legacy models » depuis Claude 5.5.                                  |
| **2026-12-01** | Gemini 4 Argon et Carbon : prix **doublé** ($2/$10 → $4/$20). `gemini-2.5-pro` routé vers `gemini-3.8-flash`, `gemini-2.5-flash` vers `gemini-3.5-flash-lite`.             |
| **2027-01-01** | Gemini 3.6/3.8 Flash : fin du prix d'introduction, **doublé** ($0.75/$3.75 → $1.50/$7.50), soit le prix de Gemini 4 Hydrogen, défaut d'aipmt depuis la 1.19.0.             |
| **2027-04-30** | Mistral Large 3 (`mistral-large-2512`) et Medium 3.5 (`mistral-medium-3-5`) : **retrait**, dépréciés depuis le 2026-10-31, remplaçant Mistral Large 4.                     |
| **2027-05-07** | `gemini-3.1-flash-lite` (`--eco` de `--use_gemini`) : **arrêt**, remplaçant désigné `gemini-3.5-flash-lite`. Mesuré le 2026-11-15 : pas prêt, cf. « Tour complet ».        |
| ~~2026-10-08~~ | `gemini-3.7-flash` **déprécié** : retiré d'AI Studio, son endpoint route vers `gemini-3.8-flash`, sans date d'arrêt. Défaut d'aipmt depuis la 1.18.0 : `gemini-3.8-flash`. |
| —              | `claude-sonnet-5` : le tarif d'intro $2/$10 **est devenu** le prix standard ; la hausse prévue au 2026-09-01 n'aura pas lieu.                                              |
| —              | Gemini 3.5 Pro **ne sortira jamais** (remplacé par Gemini 4) : `gemini-3.1-pro-preview` reste le seul Pro, et il est en preview depuis toujours.                           |

Audit du 2026-08-29 : les modèles par défaut des 7 providers sont les plus récents
disponibles chez chaque fournisseur. Aucune génération postérieure n'est GA
(GPT-5.7/6, Gemini 3.8/4, Sonnet 5.x, Haiku 5 = rumeurs ou pré-entraînement).
Dépassé depuis pour Gemini 3.8 (servi par Antigravity, cf.
`docs/providers/antigravity.md`) et pour Claude : réaudit Claude du 2026-10-18 par `GET /v1/models`
et la page des dépréciations — Opus 5.5 (2026-09-21), Sonnet 5.5 (2026-09-28)
et Haiku 5.5 (2026-10-07) sont servis, Sonnet 5 et Haiku 4.5 restent
« Active » mais passent « legacy » (cf. `docs/providers/claude.md`).
Réaudit Gemini du 2026-11-15 par la page des dépréciations
(`aistudio.google.com/docs/deprecations`) : 3.7 Flash déprécié le 2026-10-08 et
routé vers 3.8 Flash, GA depuis le 2026-09-02, qui devient le défaut de
`--use_gemini` ; Gemini 4 sort (Hydrogen au niveau gratuit), sans dépréciation
de 3.8 Flash annoncée.

### Tour complet du 2026-11-15 (1.19.0)

Méthode : la liste que chaque API sert réellement (`GET /v1/models` d'OpenAI,
d'Anthropic, de Mistral et de xAI, `GET /v1beta/models` de Google, gratuits),
le catalogue de chaque CLI (`agy models`, `~/.codex/models_cache.json`,
`grok models`), les prix lus sur les pages officielles et recoupés par
`GET /v1/language-models` de xAI et par le catalogue public d'OpenRouter, puis
une mesure par candidat : ce README (62 Ko, 4 segments) traduit en japonais,
contrôlé par `scripts/compare_structure.py`.

| Fournisseur | Avant → après                                       | Prix par million (entrée / sortie)             | Mesure sur le README en japonais                                                                         |
| ----------- | --------------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| OpenAI      | `gpt-5.6-terra` → `gpt-6.1-terra`                   | $2 / $12 → $1 / $5                             | 4 sur 4 sans écart, 190 à 245 s ; `gpt-5.6-terra` 1 sur 1, 116 s                                         |
| OpenAI éco  | `gpt-5.6-luna` → `gpt-6-luna`                       | $0.20 / $1.20 → $0.10 / $0.50                  | 4 sur 4 sans écart, 125 s ; `gpt-5.6-luna` 5 sur 6 (un gras perdu), 118 s                                |
| Gemini      | `gemini-3.8-flash` → `gemini-4-hydrogen`            | $0.75 / $3.75 (jusqu'au 31/12) → $1.50 / $7.50 | 1 sur 1 sans écart, 72 s ; `gemini-3.8-flash` 1 sur 1, 108 s                                             |
| Gemini éco  | `gemini-3.1-flash-lite`, inchangé                   | $0.25 / $1.50                                  | 2 sur 3 sans écart, 45 s ; `gemini-3.5-flash-lite` ($0.30 / $2.50) : 0 sur 3, cf. ci-dessous             |
| Grok API    | `grok-4.6` → `grok-4.7`, effort `low`               | $2 / $6, inchangé                              | 1 sur 1 sans écart, 190 s à `low`, 711 s à `medium` ; `grok-4.6` à `medium` 372 s                        |
| Grok éco    | `grok-4.3`, inchangé, effort `none`                 | $1.25 / $2.50                                  | 3 écrites sur 3, 1 sans écart (un ou deux codes en ligne en trop), 176 à 201 s ; 1.18.0 : 1 écrite sur 2 |
| Codex éco   | `gpt-5.6-luna`, rétabli par la 1.19.1               | abonnement                                     | 2 sur 2 sans écart ; `gpt-6-luna` 3 sur 4, pour trois fois plus de quota (`docs/providers/codex.md`)     |
| Antigravity | éco `gemini-3.7-flash-low` → `gemini-3.8-flash-low` | abonnement                                     | l'ancien éco est refusé par agy ; cf. `docs/providers/antigravity.md`                                    |

Inchangés, vérifiés : Claude (`claude-sonnet-5-5` et `claude-haiku-5-5` restent
les derniers Sonnet et Haiku ; Fable 5.2, sorti le 2026-11-09, entre dans la
table des fenêtres), Mistral (les alias `-latest` suivent : `mistral-large-latest`
pointe désormais sur Mistral Large 4, $0.70 / $2.10, 1 048 576 tokens), Codex en
qualité (`gpt-6.1-sol`, toujours premier du catalogue), Grok CLI (`grok-4.7` seul au catalogue, revalidé sur la 1.0.77 par un appel réel).

Trois faits mesurés ce jour-là, qui valent au-delà des défauts :

- **`reasoning_effort` n'était envoyé qu'aux GPT-5.** Un GPT-6 ou un Grok par
  clé API raisonnait à son niveau par défaut sur chaque segment, `--eco`
  compris : 695 tokens de raisonnement pour 113 de sortie sur `grok-4.7`. Le
  premier banc de `gpt-6-luna`, sans le paramètre, a perdu un jeton de code et
  rendu deux écarts en sept essais ; avec `none`, quatre sur quatre.
- **Les trois Gemini 4 refusent `minimal`**, comme 3.8 Flash : la cascade passe
  à `low`. Argon et Carbon, le haut de gamme ($2 / $10, puis $4 / $20 au
  2026-12-01, absents du niveau gratuit, 32 768 tokens de sortie d'après
  l'API), ne sont proposés que par `--model`.
- **`gemini-3.5-flash-lite` n'est pas prêt à remplacer l'éco de Gemini.**
  Mesuré le même jour après la publication de la 1.19.0, trois README en
  japonais chacun, en `--eco` : `gemini-3.1-flash-lite` en rend deux sans
  écart et un avec deux gras en trop, en 45 s ; `gemini-3.5-flash-lite` en
  perd deux sur des codes en ligne supprimés (segment 3 sur 4, refusés par la
  garde des jetons après une relance) et rend le troisième avec deux codes et
  une ligne de tableau en trop. L'éco ne change donc pas. Plus de raisonnement
  n'y change rien : niveau imposé à `low` puis à `medium` (cache du niveau
  accepté rempli avant l'appel, `--reasoning_effort` n'étant pas lu par ce
  provider), trois README chacun, un seul sans écart à chaque niveau, un
  refusé, un avec un code ou un lien de différence. Son arrêt est annoncé au
  plus tôt le 2027-05-07, sans remplaçant validé à ce prix : les candidats
  restants, Gemini 3.8 Flash et Gemini 4 Hydrogen, coûtent de trois à six fois
  plus cher. À remesurer quand Google publiera un autre Flash Lite.
- **Un modèle plus récent n'est pas plus rapide** : `gpt-6.1-terra` met de 190
  à 245 s là où `gpt-5.6-terra` en met 116, à effort égal. Il est retenu pour son prix
  et sa structure, pas pour sa latence.

Le niveau gratuit de l'API Gemini compte **par projet et par modèle** : 20
requêtes par jour pour 3.8 Flash, 500 pour 3.1 et 3.5 Flash Lite (page Limite
de débit d'AI Studio, 2026-11-15). Un appel à un nom déprécié consomme le
quota du modèle qui le sert : le 2026-11-14, la page Limite de débit
comptait 24 requêtes sur 20 pour 3.8 Flash, et aucune ligne pour 3.7 Flash,
alors que trois seulement avaient été adressées à 3.8 Flash. Une mesure de défaut sur
quatorze langues ne tient donc pas dans une journée gratuite.

Sur ce niveau gratuit, 3.8 Flash est aussi **lent** quand Google le dit en
« high demand ». Le 2026-11-15, un fichier de 444 octets (un segment), traduit
par `--use_gemini` sans `--model`, structure identique les deux fois :

| Heure  | Durée du fichier | Déroulé                                                                                                              |
| ------ | ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| 9 h 20 | 245 s            | `minimal` refusé par un 400, `low` accepté ; relances éventuelles invisibles (avis de relance pas encore écrit)      |
| 9 h 31 | 502 s            | `minimal` refusé ; `low` coupé par « 504 DEADLINE_EXCEEDED » au bout de 298 s ; relance après 10 s, réussie en 194 s |

La veille à 23 h 45, `--eco` (3.1 Flash Lite) répondait en 1,14 s. Sur le niveau
payant, le même jour : ce README entier en 88 s le matin et, en japonais, en
108 s à 13 h, structure identique.

> **Recommendation for long-form translations** : `--use_gemini` (default = `gemini-3.7-flash` at the time, `gemini-3.8-flash` in 1.18.0, `gemini-4-hydrogen` since 1.19.0) preserves markdown structure reliably on non-Latin scripts (PL, JA, ZH, AR, HI), including `--news` mode where placeholder fidelity matters. Measured on this README translated to Japanese: structure identical to `gemini-3.1-pro-preview` (21 lists, 18 code fences, 13 HTML links, 13 images, all URLs preserved) at ~6x lower latency. That latency was measured on 3.7 Flash; on the free tier, 3.8 Flash is far slower (see above). OpenAI remains the default for backward compatibility.
