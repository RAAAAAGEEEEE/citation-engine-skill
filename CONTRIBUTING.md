# Contribuer

Merci de votre intérêt. Issues et pull requests sont bienvenues.

## Avant d'ouvrir une pull request
1. `python -m unittest discover -s tests` doit passer (7 tests hors ligne à la
   version 1.2.0).
2. Un changement de comportement du skill met à jour, **dans le même commit** :
   - `SKILL.md` si la procédure change ;
   - [references/](references/) pour le détail (workflow, scoring, schémas) ;
   - [evals/evals.json](evals/evals.json) (format du skill-creator d'Anthropic :
     `prompt`, `expected_output`, `files`, `expectations`) ;
   - `CHANGELOG.md` dans tous les cas.
3. Un changement de schéma (`state.json`, `project.json`, CSV) met à jour
   [references/output-schemas.md](references/output-schemas.md),
   `scripts/check_outputs.py`, les exemples de [assets/](assets/) et les tests.
4. Les exemples de `assets/` restent **fictifs** : `example.com` ou `.example`,
   aucune vraie organisation, aucune vraie statistique.
5. Aucun secret, aucune donnée personnelle, aucun contenu réel de
   `.citation-engine/` dans le dépôt.
6. Toute commande documentée doit avoir été exécutée.

## Garde-fous à ne pas affaiblir
Les interdictions de [references/policies.md](references/policies.md) (PBN,
achat ou échange de liens, faux avis, fausse statistique, envoi automatique)
sont le cœur du skill. Une contribution qui les assouplit sera refusée.

## Style
- Français pour les textes destinés aux utilisateurs. Termes techniques en
  anglais acceptés, expliqués au premier usage.
- Python 3.10+, bibliothèque standard uniquement.
- Aucune promesse chiffrée sans source citée.

## Signaler une faille
Voir [SECURITY.md](SECURITY.md).
