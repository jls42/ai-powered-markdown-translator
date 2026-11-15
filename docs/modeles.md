# Modèles, constantes et usage recommandé

## Recommended Usage

**Pour les traductions de CE dépôt, voir `docs/traductions.md` : Codex + `gpt-6.1-sol`,
Antigravity en repli, jamais l'API.** Ce qui suit vaut pour un usage général de l'outil sur une clé API.

For batch translations (README, CHANGELOG, blog articles), use `--eco` mode:

```bash
aipmt --file README.md --target_dir . --source_lang fr --target_lang en --eco --add_translation_note
```

This uses faster/cheaper models (gpt-5.6-luna) which are sufficient for documentation translation.

## Key Constants

- `EXCLUDE_PATTERNS`: Paths containing these strings are skipped (`traductions_`, `venv`, `PRIVACY.md`)
- `MODEL_TOKEN_LIMITS`: Dict mapping model names to max token limits for segmentation

### Default Models (2026)

| Provider    | Quality (default)                     | Economic (`--eco`)      |
| ----------- | ------------------------------------- | ----------------------- |
| OpenAI      | `gpt-5.6-terra`                       | `gpt-5.6-luna`          |
| Claude      | `claude-sonnet-5-5`                   | `claude-haiku-5-5`      |
| Mistral     | `mistral-large-latest`                | `mistral-small-latest`  |
| Gemini      | `gemini-3.8-flash`                    | `gemini-3.1-flash-lite` |
| Codex       | `gpt-6.1-sol`                         | `gpt-5.6-luna`          |
| Grok API    | `grok-4.6`                            | `grok-4.3`              |
| Grok CLI    | `grok-4.7`                            | `grok-4.7` (sans effet) |
| Antigravity | `gemini-3.8-flash-medium`             | `gemini-3.7-flash-low`  |
| Claude Code | `sonnet` (effort `low`)               | `sonnet` (sans effet)   |
| OpenCode    | `--model provider/modèle` obligatoire | idem                    |

### Model lifecycle — dates to watch (audited 2026-08-29, Claude re-audited 2026-10-18)

| Échéance       | Impact                                                                                                                                                                     |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ~~2026-10-15~~ | `claude-haiku-4-5` : date-plancher **passée sans retrait** — toujours « Active » le 2026-10-18, préavis d'au moins 60 jours avant tout retrait.                            |
| **2027-06-30** | `claude-sonnet-5` : date-plancher de retrait (« not sooner than »). Comme Haiku 4.5, rangé parmi les « legacy models » depuis Claude 5.5.                                  |
| **2027-01-01** | Gemini 3.6/3.7/3.8 Flash : fin de la promo, prix **doublé** ($0.75/$3.75 → $1.50/$7.50) ; la promo court jusqu'au 2026-12-31 inclus.                                       |
| **2027-05-07** | `gemini-3.1-flash-lite` (`--eco` de `--use_gemini`) : **arrêt**, remplaçant désigné `gemini-3.5-flash-lite`. Mesurer celui-ci avant de basculer.                           |
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
de 3.8 Flash annoncée. Les autres fournisseurs n'ont pas été réaudités.

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

La veille à 23 h 45, `--eco` (3.1 Flash Lite) répondait en 1,14 s. Le niveau payant
n'est pas mesuré.

> **Recommendation for long-form translations** : `--use_gemini` (default = `gemini-3.7-flash` at the time, `gemini-3.8-flash` since 1.18.0) preserves markdown structure reliably on non-Latin scripts (PL, JA, ZH, AR, HI), including `--news` mode where placeholder fidelity matters. Measured on this README translated to Japanese: structure identical to `gemini-3.1-pro-preview` (21 lists, 18 code fences, 13 HTML links, 13 images, all URLs preserved) at ~6x lower latency. That latency was measured on 3.7 Flash; on the free tier, 3.8 Flash is far slower (see above). OpenAI remains the default for backward compatibility.
