# Dépannage

Retour : [README](../README.md) · Voir aussi : [USAGE](USAGE.md),
[LIMITATIONS](LIMITATIONS.md).

| Symptôme | Cause probable | Action |
|---|---|---|
| `/seo` n'apparaît pas dans Claude Code | Skill mal placé ou dossier mal nommé | Vérifier `~/.claude/skills/seo/SKILL.md` (ou `.claude/skills/seo/`), puis redémarrer Claude Code. Voir [INSTALLATION](INSTALLATION.md) |
| Claude ne lance pas le skill de lui-même | Voulu : `disable-model-invocation: true` | Taper `/seo` |
| Le skill pose une question sur l'URL | Aucune URL publique détectée dans le dépôt | Répondre avec l'URL canonique ; c'est la seule question attendue |
| `opportunities.csv` vide, avec seulement les en-têtes | Pas d'outil de recherche web, ou aucune opportunité réelle trouvée | Lire `state.json.last_error` et `audit.md` ; ajouter un outil de recherche web puis relancer `/seo` |
| Une page est marquée « non vérifié » | 403, paywall, connexion ou rendu JavaScript | Normal : le skill ne contourne pas ces restrictions. Vérifier la page à la main |
| `state.json` invalide | Fichier modifié à la main ou écriture interrompue | Le skill ne l'écrase pas. Restaurer une copie, ou renommer en `state.json.bak-<date>` et relancer |
| `check_outputs.py` renvoie `total_score ... différent de la somme` | Score mal additionné | Corriger le total dans `opportunities.csv` (critères + pénalités) |
| `check_outputs.py` renvoie `score ... < 40 mais status = ...` | Une opportunité sous le seuil n'est pas rejetée | Passer `status` à `rejected` |
| `check_outputs.py` renvoie `en-têtes différents` | Colonnes modifiées ou réordonnées | Rétablir les en-têtes de [output-schemas.md](../references/output-schemas.md) |
| Caractères accentués illisibles dans la console Windows | Page de code de la console | Sans effet sur les fichiers, écrits en UTF-8 ; utiliser `chcp 65001` ou Windows Terminal |

Si le problème persiste, ouvrir une issue avec la sortie de
`python scripts/check_outputs.py <dossier>`, **sans** joindre le contenu de
`.citation-engine/` (données de prospection : voir
[PRIVACY_AND_SECURITY](PRIVACY_AND_SECURITY.md)).
