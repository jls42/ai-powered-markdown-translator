# Provider OpenRouter (`--use_openrouter`) — routeur payant, `--model` obligatoire

```bash
aipmt --use_openrouter --model z-ai/glm-5.2 --file README.md --target_dir . --target_lang en
```

Neuvième chemin. OpenRouter est un routeur devant ~430 modèles hébergés par des
tiers, sur un crédit unique. Il donne accès aux modèles chinois ouverts (Kimi,
Qwen, DeepSeek, Z.ai) qu'aucun autre provider n'expose ici. Tout ce qui suit a
été **mesuré sur l'API le 2026-09-05**, pas lu dans la doc :

- **Un même slug est servi par des dizaines d'hébergeurs aux plafonds de sortie
  différents.** 33 pour `z-ai/glm-5.2`, 23 pour `glm-5.3-flash` — dont un à
  **2 048 tokens**. Sans épinglage, une traduction longue sur 23 partait
  tronquée, au hasard du routage. Le préflight lit
  `/api/v1/models/{slug}/endpoints`, écarte les plafonds sous 8 000 et les
  statuts négatifs, puis épingle le reste. `provider.only` **sans**
  `allow_fallbacks: false` n'est qu'une préférence : le routeur repart vers un
  hébergeur écarté. Les deux formes de `only` sont acceptées, nom nu
  (`deepinfra`) ou tag (`deepinfra/fp4`) ; on envoie le tag, plus précis.
- **Le raisonnement est facturé au tarif de sortie**, et il est actif par défaut
  sur beaucoup de modèles. Même requête sur `z-ai/glm-5.2`, réponse « OK » :
  **107 tokens de complétion contre 2** avec `reasoning: {"enabled": false}`.
  D'où la coupure par défaut. 288 des 431 modèles l'imposent
  (`reasoning.mandatory`) et répondent 400 « Reasoning is mandatory for this
  endpoint and cannot be disabled ». Pour ceux-là on demande le **plus bas
  effort déclaré** dans `supported_efforts` : ne rien envoyer laisse le défaut
  du catalogue, qui vaut `max` sur `glm-5.3-flash` et **tronque la sortie à
  32 768 tokens** avant la fin de la traduction. Monter l'enveloppe n'y change
  rien — l'effort en alloue un POURCENTAGE, que le raisonnement consomme en
  premier. Contre-épreuve : la langue qui échouait passe, structure identique.
- **`finish_reason=error` est une panne de l'hébergeur amont**, pas une fin
  anormale du modèle : `native_finish_reason` est nul, et deux langues ont été
  coupées à 750 s exactement. Message distinct, sinon on cherche le défaut dans
  le document.
- **Le catalogue n'a pas d'endpoint unitaire** : `/api/v1/models/{slug}` répond
  404, seul `/api/v1/models` (714 Ko) porte `reasoning` et `context_length`.
- **`finish_reason=length` avec un texte vide n'est pas une troncature** mais un
  budget mangé par le raisonnement (mesuré : 15 850 tokens de raisonnement pour
  148 utiles). Les deux cas appellent des gestes opposés, le message les
  distingue.
- **Le routeur répond 200 avec un corps ne portant qu'une erreur** quand
  l'hébergeur amont échoue : `choices[0]` levait un TypeError opaque, une garde
  lit `error` avant.
- **La fenêtre de contexte vient du préflight**, écrite dans
  `MODEL_TOKEN_LIMITS` : `DEFAULT_TOKEN_LIMIT` est faux pour 44 modèles du
  catalogue, dont deux plafonnés à 4 095 tokens.
- **Le slug est interpolé dans l'URL de préflight** : sa forme est validée
  avant tout réseau, et le segment `..` refusé — la regex namespacée commune
  aux deux routeurs accepte `a/b/..`.
