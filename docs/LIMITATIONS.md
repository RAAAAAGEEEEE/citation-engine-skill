# Limites

Retour : [README](../README.md) · Voir aussi : [TROUBLESHOOTING](TROUBLESHOOTING.md).

## Résultats
- Aucune garantie de backlink, de mention, de citation par une IA ou de gain de
  trafic. Le skill augmente la probabilité d'obtenir des mentions éditoriales, il
  ne les produit pas.
- Aucune mesure directe des citations dans ChatGPT, Gemini, Perplexity ou
  Claude. Les « citations IA observées » du rapport sont saisies à la main.
- Le suivi (backlinks gagnés, trafic, leads, revenus) est manuel. Une variation
  n'est jamais attribuée automatiquement à une action SEO.

## Recherche
- Dépend de l'outil de recherche web disponible : sans lui, pas de recherche
  d'opportunités (le skill le dit et n'invente rien).
- Les pages en 403, derrière un paywall ou une connexion, ou rendues en
  JavaScript sont « non vérifiées ».
- Une opportunité vérifiée à une date donnée peut changer : chaque ligne porte
  `verified_at`.

## Comportement du skill
- Le skill ne modifie pas le code du site, ne publie pas, ne crée pas de commit :
  il livre un plan d'implémentation.
- Il n'envoie aucun message. Il n'y a pas de suivi des réponses des prospects.
- Le barème de scoring est une heuristique, pas une mesure : il aide à trier, il
  ne prédit pas un résultat.
- Le contenu de l'actif est un brouillon à relire : chaque chiffre doit être
  vérifié par un humain avant publication.

## Qualité du dépôt
- Les 12 cas de [evals/evals.json](../evals/evals.json) décrivent le
  comportement attendu mais ne s'exécutent pas automatiquement : seul
  `scripts/check_outputs.py` est couvert par des tests.
- `check_outputs.py` contrôle la forme des fichiers (champs, en-têtes, somme des
  scores, doublons), pas la véracité du contenu.
- Rédigé et testé pour des projets francophones ; d'autres langues ne sont pas
  évaluées.
