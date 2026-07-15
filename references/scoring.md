# Scoring — SEO

Voir [SKILL.md](../SKILL.md) pour le résumé. Ce fichier détaille le barème utilisé en Phase 4.

## Barème positif (100 points max)

| Critère | Points |
|---|---|
| Pertinence thématique | 0–25 |
| Valeur éditoriale réelle | 0–20 |
| Probabilité d'obtention | 0–15 |
| Autorité et crédibilité de la source | 0–15 |
| Potentiel de citation par les moteurs IA | 0–15 |
| Faible effort | 0–10 |

## Pénalités

| Motif | Points |
|---|---|
| Échange ou réseau artificiel de liens | -50 |
| Site manifestement spammy | -50 |
| Opportunité hors sujet | -30 |
| Donnée impossible à vérifier | -25 |
| Outreach générique | -15 |
| Contrepartie cachée | -50 |
| Achat de lien dofollow | -50 |
| Contenu quasi identique à grande échelle | -40 |

Le score final = somme des points positifs + somme des pénalités (négatives). Toute opportunité avec un score final < 40 est automatiquement rejetée (`status = rejected` dans `opportunities.csv`).

## Sélection de l'action P0

Une seule action P0 principale est sélectionnée par cycle. À score comparable entre plusieurs candidats, appliquer cet ordre de priorité (du plus prioritaire au moins prioritaire) :

1. page de statistiques propriétaire
2. benchmark original
3. calculateur utile
4. dataset original
5. comparatif honnête et documenté
6. récupération de mentions sans lien
7. remplacement d'une ressource cassée ou obsolète
8. réponse à un besoin journalistique
9. prospection de listicles pertinents

La sélection doit être enregistrée dans `state.json.selected_opportunity` avec :
- impact attendu
- effort estimé
- preuve (URL, capture, donnée)
- risques identifiés
- raison pour laquelle cette action passe avant les autres candidats du même score
