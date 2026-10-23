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
| Gemini      | `gemini-3.7-flash`                    | `gemini-3.1-flash-lite` |
| Codex       | `gpt-6.1-sol`                         | `gpt-5.6-luna`          |
| Grok API    | `grok-4.6`                            | `grok-4.3`              |
| Grok CLI    | `grok-4.7`                            | `grok-4.7` (sans effet) |
| Antigravity | `gemini-3.8-flash-medium`             | `gemini-3.7-flash-low`  |
| Claude Code | `sonnet` (effort `low`)               | `sonnet` (sans effet)   |
| OpenCode    | `--model provider/modèle` obligatoire | idem                    |

### Model lifecycle — dates to watch (audited 2026-08-29, Claude re-audited 2026-10-18)

| Échéance       | Impact                                                                                                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| ~~2026-10-15~~ | `claude-haiku-4-5` : date-plancher **passée sans retrait** — toujours « Active » le 2026-10-18, préavis d'au moins 60 jours avant tout retrait.  |
| **2027-06-30** | `claude-sonnet-5` : date-plancher de retrait (« not sooner than »). Comme Haiku 4.5, rangé parmi les « legacy models » depuis Claude 5.5.        |
| **2027-01-01** | Gemini 3.6/3.7 Flash : fin de la promo, prix **doublé** ($0.75/$3.75 → $1.50/$7.50).                                                             |
| —              | `claude-sonnet-5` : le tarif d'intro $2/$10 **est devenu** le prix standard ; la hausse prévue au 2026-09-01 n'aura pas lieu.                    |
| —              | Gemini 3.5 Pro **ne sortira jamais** (remplacé par Gemini 4) : `gemini-3.1-pro-preview` reste le seul Pro, et il est en preview depuis toujours. |

Audit du 2026-08-29 : les modèles par défaut des 7 providers sont les plus récents
disponibles chez chaque fournisseur. Aucune génération postérieure n'est GA
(GPT-5.7/6, Gemini 3.8/4, Sonnet 5.x, Haiku 5 = rumeurs ou pré-entraînement).
Dépassé depuis pour Gemini 3.8 (servi par Antigravity, cf.
`docs/providers/antigravity.md`) et pour Claude : réaudit Claude du 2026-10-18 par `GET /v1/models`
et la page des dépréciations — Opus 5.5 (2026-09-21), Sonnet 5.5 (2026-09-28)
et Haiku 5.5 (2026-10-07) sont servis, Sonnet 5 et Haiku 4.5 restent
« Active » mais passent « legacy » (cf. `docs/providers/claude.md`). Les autres
fournisseurs n'ont pas été réaudités.

> **Recommendation for long-form translations** : `--use_gemini` (default = `gemini-3.7-flash`) preserves markdown structure reliably on non-Latin scripts (PL, JA, ZH, AR, HI), including `--news` mode where placeholder fidelity matters. Measured on this README translated to Japanese: structure identical to `gemini-3.1-pro-preview` (21 lists, 18 code fences, 13 HTML links, 13 images, all URLs preserved) at ~6x lower latency. OpenAI remains the default for backward compatibility.
