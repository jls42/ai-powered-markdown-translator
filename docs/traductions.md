# Traductions de ce dépôt : JAMAIS par une API facturée

**Décision du propriétaire, non négociable, formulée le 2026-09-04 :** les 28
traductions (README, CHANGELOG) se font sur **l'abonnement ChatGPT via Codex**,
avec son modèle qualité : **`gpt-6.1-sol`** depuis le 2026-10-19, choix du
propriétaire ce jour-là, après `gpt-5.6-sol` (cf. `docs/providers/codex.md`). L'abonnement a été pris exprès pour
ne pas payer de coûts API. Ce jour-là, `release.sh --auto` avait envoyé les 28
fichiers sur l'API OpenAI, puis le CHANGELOG hindi sur celle de Gemini, parce
que le regen auto-détectait `OPENAI_API_KEY` dans `.env` et ne faisait de Codex
qu'un opt-in.

**Complétée par le propriétaire le 2026-09-26 : Codex d'abord, et si Codex
n'est pas disponible, l'abonnement Google.** Quota de la fenêtre épuisé,
session expirée : la campagne passe par
`REGEN_PROVIDER=antigravity ./regen_translations.sh --force`
(`gemini-3.8-flash-medium`, cf. `docs/providers/antigravity.md`), sans attendre le
retour de Codex ni demander. Ce jour-là, le quota Codex était épuisé jusqu'au
lendemain, et les 28 traductions de la 1.15.0 sont passées par Antigravity.
Le repli reste un abonnement : jamais d'API facturée, dans un cas comme dans
l'autre.

## QUAND régénérer : une seule fois, juste avant le merge

**La régénération se lance quand le README et le CHANGELOG sont FIGÉS, pas à
chaque modification.** Mesuré le 2026-09-09 : huit campagnes lancées dans la
même journée pour 53 fichiers réellement conservés, parce que chaque retour de
revue changeait une phrase du CHANGELOG et que la régénération repartait
aussitôt. Sept campagnes sur huit sont parties à la poubelle, et le quota de la
fenêtre de cinq heures y est passé.

L'ordre correct, sur une PR qui touche la documentation :

1. le code, la revue et les correctifs, jusqu'à ce que plus aucun retour ne
   soit en attente ;
2. la dernière retouche du CHANGELOG et du README ;
3. **alors seulement** `./regen_translations.sh --force` ;
4. gate, commit des 28 traductions, push.

Pendant les étapes 1 et 2, la quatrième section du gate est rouge sur les
traductions divergentes : **c'est normal et il faut la laisser rouge**. Elle
signale un travail à faire à la fin, pas une urgence à traiter tout de suite.

**Une campagne couvre TOUTES les langues.** Quand le README ou le CHANGELOG
change, les quatorze sont refaites : en sauter une laisserait des traductions
sur deux versions différentes, et c'est justement ce que le compte 28/28 et le
contrôle de fraîcheur par contenu existent pour empêcher.

Ce qui se reprend, c'est une campagne INTERROMPUE, pas une sélection. Une
langue coupée en cours de traduction se refait depuis le début — il n'y a pas
de reprise partielle, l'outil traduit des fichiers entiers — puis les suivantes
s'enchaînent. Concrètement, après un quota épuisé à mi-parcours, relancer
nommément les langues qui n'ont pas abouti :

```bash
printf '%s\n' ja hi it ko nl pl pt ro sv zh | xargs -P 4 -I{} bash regen_one.sh {}
```

Celles déjà terminées portent le même contenu source : les refaire ne
changerait rien qu'une dépense.

**Le coût par campagne croît avec le CHANGELOG.** Il fait 111 000 caractères
avec l'entrée 1.15.0 (94 000 à la 1.14.1) et se découpe en huit segments —
compté par `segment_text` le 2026-09-26 —, soit huit tours Codex par langue et
112 tours pour les quatorze. La référence « 28 fichiers pour 70 tours, 1 point de la fenêtre »
notée plus bas date d'un fichier bien plus court : le coût par fichier a plus
que doublé depuis, et chaque release retraduit intégralement des entrées de
versions publiées il y a des mois. Archiver l'historique dans un
`CHANGELOG-archive.md` traduit une fois rendrait ce coût constant — décision du
propriétaire, non prise à sa place.

Ce que ça implique, et ce qui l'encode :

- `./regen_translations.sh --force` sans variable = Codex, `gpt-6.1-sol`, 4
  jobs. Plus aucune auto-détection de clé : une clé présente ne change rien.
  **Compter une heure** : mesuré le 2026-09-04 à 4 jobs avec `gpt-5.6-sol`, un README prend 3 à
  4 min et un CHANGELOG 10 à 14 min (effort de raisonnement `medium`, défaut
  de Sol hors `--eco`). Le plafond par job est à 1 800 s sur Codex : à 600 s,
  13 CHANGELOG sur 14 étaient tués sans une ligne d'erreur.
- **Avec `gpt-6.1-sol`, une campagne complète ne tient plus dans une fenêtre
  de 5 h** (plan Plus, quota lu par `codex app-server` avant et après chaque
  lot, cf. `docs/providers/codex.md`). Mesuré la nuit du 2026-10-19 au 20, sur la
  1.17.0 (README de 41 000 caractères, CHANGELOG de 9 segments) : un README
  coûte 2,4 points de la fenêtre et prend 155 à 181 s à 4 jobs ; un CHANGELOG
  environ 7 points et 464 à 599 s. Les 28 fichiers demanderaient donc quelque
  130 points : les 14 README et 3 CHANGELOG (hi, ja, it) sont passés par
  Codex, les 11 autres par Antigravity, le repli de la règle. La semaine n'a
  perdu que 8 points pour toute la nuit, sondes comprises. Lancer d'abord les
  README, courts, puis autant de CHANGELOG que la fenêtre en laisse : une
  fenêtre épuisée en cours de route jette les segments déjà payés.
- **Contrôler chaque traduction par `scripts/compare_structure.py`, quel que
  soit le provider.** Le même soir, Antigravity a rendu un CHANGELOG italien
  qui recopiait en double toute l'entrée 1.15.0 et ouvrait un bloc de code
  jamais fermé (474 lignes pour 411, 27 titres de version pour 26) : aucune
  garde d'aipmt ne l'a vu, et le journal était vierge. La section 4 du gate
  l'aurait refusé, puisqu'elle compte les clôtures et les éléments de liste,
  mais elle ne compte ni le gras ni le code en ligne : les deux gras perdus du
  CHANGELOG coréen, le même soir, lui échappaient. `compare_structure.py` voit
  les deux (« fences 1≠0; code 1159≠1043 », « gras 312≠314 »). L'italien a
  été relancé sur Codex, le coréen sur Antigravity.
- `REGEN_PROVIDER=openai|gemini|grok|openrouter` est **refusé** (exit 1, message
  qui cite cette règle) tant que `REGEN_ALLOW_PAID_API=1` n'est pas posé en plus.
  OpenRouter exige en outre un `REGEN_MODEL` : c'est un routeur, il n'a pas de
  défaut. Ne
  jamais poser cette dérogation sans demande explicite du propriétaire — pas
  même pour rattraper un fichier en échec : relancer Codex, ou `grok_cli`, ou
  `antigravity`.
- `REGEN_PROVIDER=antigravity` passe **sans** dérogation : c'est l'abonnement
  Google (AI Pro ou Ultra), décompté en quota, pas une API facturée — 4 jobs
  et 1 800 s par job, comme Codex (cf. `docs/providers/antigravity.md`). Le plafond est
  validé par la mesure du 2026-09-26 : le CHANGELOG entier en hindi — le
  fichier où Codex perd des placeholders — traduit sans écart en 273 s par
  `gemini-3.7-flash-medium`, marge ×6,5. Coût mesuré sur la régénération de la
  1.15.0, le 2026-09-26, en `gemini-3.8-flash-medium` : 27 fichiers sur 28 en
  29 min 39 s à 4 jobs, **36,4 points de la fenêtre Gemini de 5 h** et 6,1 de
  la semaine, sur le palier du compte du propriétaire — plus d'un tiers de la
  fenêtre (la même en `gemini-3.7-flash-medium`, le matin : 28 fichiers en
  21 min environ). Deux fichiers relancés seuls : le CHANGELOG hindi, bloqué
  par le filtre de contenu de Google (cf. `docs/providers/antigravity.md`), et le README
  italien, un lien interne doublé que la section 4 du gate a attrapé (cf.
  `docs/liens-internes.md`). Avant d'ouvrir les 28 jobs, le script valide `REGEN_MODEL` et
  lance une fois le préflight du module (version, connexion, voie de
  facturation) : un agy déconnecté ou réglé pour facturer n'en démarre aucun. Il ne remplace pas le défaut : Codex et
  son modèle qualité restent le premier chemin de ces traductions, Antigravity le
  repli quand Codex n'est pas disponible (cf. règle en tête).
- Un fichier qui échoue sur Codex (placeholder perdu, cas connu du hindi) se
  relance **seul, sur Codex** — sur Antigravity si Codex n'est plus
  disponible : `python -m aipmt --use_codex --file CHANGELOG.md
--target_lang hi --add_translation_note --force`.
- Les tests `TestDetectProvider` verrouillent le défaut, le refus et la
  dérogation.
