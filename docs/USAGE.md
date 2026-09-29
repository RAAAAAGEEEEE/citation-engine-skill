# Usage

Retour : [README](../README.md) · Voir aussi : [CONFIGURATION](CONFIGURATION.md),
[TROUBLESHOOTING](TROUBLESHOOTING.md).

## Lancer le skill
Dans Claude Code, ouvert dans le dépôt du projet :
```
/seo
```
Il n'existe pas de sous-commande : le skill lit `.citation-engine/state.json` et
décide seul de la phase suivante.

1. Aucun `state.json` valide : initialisation, puis les 8 phases.
2. `state.json` valide : reprise à la première phase de `pending_phases`.
3. Informations bloquantes : un seul message, 3 questions au maximum (l'URL
   canonique si elle est introuvable).

## Où sont les résultats
Sous `<racine du projet>/.citation-engine/` :

| Fichier | Contenu |
|---|---|
| `state.json` | Avancement, reprise, dernière erreur |
| `project.json` | Fiche projet (public, concurrents, domaines exclus) |
| `audit.md` | Audit en 9 sections |
| `opportunities.csv` | Opportunités notées sur 100 |
| `prospects.csv` | Prospects qualifiés |
| `assets/<slug>/` | `BRIEF.md`, `CONTENT.md`, `sources.csv`, `implementation.md` |
| `outreach/<date>.md` | Brouillons `BROUILLON — NON ENVOYÉ` |
| `reports/<date>.md` | Synthèse et prochaine action |

Schémas exacts : [references/output-schemas.md](../references/output-schemas.md).
Les fichiers de [assets/](../assets/) sont des exemples **fictifs** : les noms
de domaine, les chiffres et les organisations n'existent pas.

## Vérifier les fichiers produits
```bash
python scripts/check_outputs.py /chemin/vers/le/projet/.citation-engine
```
Le script contrôle, sans rien écrire :
- les champs obligatoires de `state.json` et `project.json`, et la cohérence
  des phases ;
- les en-têtes exacts des CSV ;
- pour `opportunities.csv` : `total_score` égal à la somme des critères et des
  pénalités, `status` valide, aucune ligne sous 40 qui ne soit `rejected`,
  aucun doublon ;
- pour `prospects.csv` : aucun doublon, raison éditoriale et preuve de
  personnalisation renseignées ;
- pour `sources.csv` : `confidence` valide.

Codes de sortie : 0 tout est valide, 1 au moins un problème, 2 rien à
contrôler. Exemple sur les fichiers fournis (exécuté le 2026-09-29) :
```bash
python scripts/check_outputs.py assets/state.example.json assets/project.example.json assets/opportunities.example.csv assets/prospects.example.csv assets/sources.example.csv
```
```
5/5 fichier(s) valide(s)
```
(précédé d'une ligne `OK` par fichier.)

## Cas courants
| Besoin | Action |
|---|---|
| Reprendre après une interruption | Relancer `/seo` |
| Repartir de zéro | Copier `state.json` (ex. `state.json.bak-2026-09-29`), renommer l'original, relancer `/seo`. Ne jamais le supprimer directement |
| Choisir une autre action P0 | Demander en clair à Claude de rouvrir la phase 4 et d'expliquer pourquoi dans `notes` |
| Suivre les résultats | Compléter à la main la section « Suivi » de `reports/<date>.md` (backlinks, citations IA, trafic, leads) |

Les autres fichiers (`audit.md`, `opportunities.csv`, etc.) sont fusionnés avec
l'existant aux lancements suivants, pas écrasés.

## Ce que le skill ne fait jamais tout seul
Envoyer un e-mail ou un message, remplir un formulaire, publier du contenu,
modifier le code applicatif, créer un commit, acheter ou échanger un lien,
inventer une statistique, un contact ou une citation, garantir un résultat.
Détail : [references/policies.md](../references/policies.md).
