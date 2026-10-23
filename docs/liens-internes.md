# Liens internes : le jeton d'ancre avale ses parenthèses

**Mesuré le 2026-09-26, sur le README de la 1.15.0.** `_protect_anchors`
(`placeholders.py`) remplace `(#fragment)` PARENTHÈSES COMPRISES par
`#ANCHORn#` : le modèle reçoit `[Mesures détaillées]#ANCHOR2#`, un lien
d'apparence cassée, et il lui arrive de le « réparer ». Deux effets :

- **Un lien cassé que rien ne voit.** Réparé en `[…](#ANCHOR2#)`, le lien
  devient à la restauration `[…]((#fragment))`, qui ne mène nulle part. Ni la
  validation des jetons (le jeton est là), ni `compare_structure.py` (il compte
  un lien), ni la section 4 du gate avant ce jour ne l'attrapaient. Constaté
  dans les README espagnol et coréen de la régénération Antigravity, et dans
  les mesures de l'après-midi sur tous les modèles essayés, 3.7 comme 3.8.
- **Un segment refusé.** Quand le modèle réécrit le jeton au lieu de le
  recopier, la garde refuse le segment : les 8 pertes de jeton de la mesure de
  l'après-midi portaient toutes sur `#ANCHOR2#`, et chacun des deux Flash en
  `-low` y a perdu un README entier.

Le déclencheur était un lien placé entre parenthèses —
`(cf. [Mesures détaillées](#mesures-détaillées))` —, ajouté par la 1.15.0 :
sur le README 1.14.0, sans lui, les quatre Flash passaient 3 sur 3. Mais le
défaut est général : 3.8 low a aussi doublé en hindi les deux liens qui ne
sont pas entre parenthèses.

Ce qui est en place : la section 4 du gate compte les liens internes intacts
(`](#…)`) de chaque traduction contre la source, et le README n'écrit plus de
lien entre parenthèses. Et le correctif de fond : `_anchor_token` laisse les
parenthèses d'un lien Markdown hors du jeton — le modèle reçoit
`[texte](#ANCHOR0#)`, un lien valide qu'il n'a plus de raison de réparer —,
et `_restore_anchors` restaure le jeton entre ses parenthèses, puis un jeton
nu en lien complet. Les ancres HTML et `<a name>` gardent un jeton nu. Trois
tests de `TestHeadingAnchors` échouent sur l'ancien code. Validé de bout en
bout : le README d'avant la reformulation, lien entre parenthèses compris,
traduit par `gemini-3.8-flash-low` en japonais, hindi et anglais — refusé,
trois liens doublés et un segment repassé sans le correctif ; avec lui, trois
liens intacts sur trois partout, aucune reprise, structure identique. Le
défaut ne tenait pas qu'aux parenthèses : même après la reformulation, les
régénérations de la 1.15.0 et de la 1.16.0 avaient encore doublé un lien, en
italien puis en allemand.

**Corollaire pour la documentation : jamais de jeton littéral dans le README
ni le CHANGELOG** — ni `#ANCHOR0#`, ni `#INLINECODE0#`, ni leurs cousins,
même entre accents graves. `_validate_no_code_placeholder_leftover` cherche ce
motif dans la traduction RESTAURÉE : le code en ligne y revient tel quel, et
chaque langue serait refusée (vérifié sur la fonction). Une première rédaction
de l'entrée 1.15.0 en citait un ; la relecture l'a retiré avant la campagne.
Même famille de piège que `authMethod=` (cf. `docs/providers/antigravity.md`).
