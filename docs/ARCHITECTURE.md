# Architecture

Retour : [README](../README.md) · Voir aussi : [USAGE](USAGE.md),
[CONFIGURATION](CONFIGURATION.md).

## Vue d'ensemble
Le skill n'est pas un programme : c'est une procédure (`SKILL.md`) que Claude
suit dans le dépôt d'un projet, avec des références chargées à la demande et un
petit script de contrôle.

| Élément | Rôle |
|---|---|
| [SKILL.md](../SKILL.md) | Procédure : périmètre, modes, 8 phases, garde-fous, replis |
| [references/workflow.md](../references/workflow.md) | Contenu exact de chaque phase et critères de complétion |
| [references/scoring.md](../references/scoring.md) | Barème sur 100, pénalités, priorité P0 |
| [references/policies.md](../references/policies.md) | Politiques Google et interdictions |
| [references/source-quality.md](../references/source-quality.md) | Hiérarchie des sources, contradictions |
| [references/output-schemas.md](../references/output-schemas.md) | Schémas de `state.json`, `project.json`, CSV, actifs |
| [assets/](../assets/) | Gabarits et exemples fictifs |
| [scripts/check_outputs.py](../scripts/check_outputs.py) | Contrôle des fichiers produits (bibliothèque standard) |
| [evals/evals.json](../evals/evals.json) | 12 cas d'évaluation (format skill-creator) |
| [tests/](../tests/) | 7 tests hors ligne de `check_outputs.py`, des évaluations et du front-matter |

## Flux de données
```
dépôt courant (lecture) ──> Claude + SKILL.md ──> <racine>/.citation-engine/
        recherche web publique (optionnelle) ──>      state.json, project.json, audit.md,
                                                     opportunities.csv, prospects.csv,
                                                     assets/<slug>/, outreach/, reports/
```
Le skill n'écrit que sous `.citation-engine/`. Il ne modifie pas le reste du
dépôt, ne crée pas de commit et n'envoie rien vers l'extérieur.

## Machine à états
`state.json` porte `completed_phases`, `pending_phases` et `current_phase`. Les
phases, dans l'ordre : `initialisation`, `audit`, `recherche_opportunites`,
`scoring_et_selection`, `production_actif`, `prospection`, `outreach`,
`rapport`. Une phase n'est marquée terminée que si ses fichiers obligatoires
existent et sont valides ; `state.json` est mis à jour en dernier
(écriture sûre : préparer, valider, écrire, relire, puis état).

## Choix de conception
- **Un seul point d'entrée** (`/seo`, sans sous-commande) : l'état décide de la
  suite, pas l'utilisateur.
- **Invocation manuelle seulement** (`disable-model-invocation: true`) : le
  skill écrit dans le dépôt et enchaîne 8 phases, il ne doit pas se lancer par
  déduction.
- **Fichiers plats (Markdown, CSV, JSON)** : lisibles, versionnables, sans
  base de données. Les en-têtes CSV sont fixes pour permettre le contrôle.
- **Brouillon uniquement** : la limite entre préparer et envoyer est un choix de
  sécurité, pas une fonction manquante.
