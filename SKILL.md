---
name: SEO
description: Moteur autonome SEO, GEO, digital PR, contenus citables, backlinks éditoriaux, listicles, comparatifs, mentions sans lien et prospection pour SaaS. À utiliser manuellement avec /SEO pour auditer un projet, rechercher et scorer les opportunités, produire un actif citable, trouver des prospects et préparer des brouillons d'outreach.
disable-model-invocation: true
---

# SEO

Moteur SEO/GEO multi-SaaS pour solopreneur. Une seule commande : `/SEO`.
Objectif : maximiser le rapport impact/effort — pas une fabrique à backlinks, pas de spam, pas de réseau artificiel entre les SaaS de l'utilisateur.

## Principe

À chaque lancement :

1. Résoudre le chemin absolu du dépôt courant.
2. Chercher `<racine>/.citation-engine/state.json`.
   - S'il existe et est valide : reprendre à la première phase incomplète (voir `completed_phases` / `pending_phases`).
   - S'il n'existe pas : initialiser (Phase 1).
3. Examiner le projet AVANT de poser une question (README, package.json, config, sitemap, robots.txt, métadonnées, contenu existant).
4. Regrouper les informations bloquantes en UN SEUL message, 3 questions maximum.
5. Continuer automatiquement toutes les phases sans demander confirmation entre elles.
6. Mettre à jour `state.json` après chaque phase (jamais marquer une phase terminée si ses fichiers obligatoires manquent ou sont invalides).

Si l'URL canonique ne peut pas être déterminée : demander uniquement celle-ci.
Si les outils de recherche web sont indisponibles : continuer avec les données locales, signaler la limite dans `state.json.last_error` et dans le rapport, produire ce qui peut l'être sans invention.

Ne jamais inventer une donnée manquante. Utiliser `null`, `[]`, ou la chaîne `[À VÉRIFIER : description précise]`.

## Phases (ordre fixe)

1. **Initialisation** — créer l'arborescence `.citation-engine/`, `project.json`, `state.json`. Détail : [references/workflow.md](references/workflow.md#phase-1)
2. **Audit** — analyser produit, technique, éditorial → `audit.md`. Détail : [references/workflow.md](references/workflow.md#phase-2)
3. **Recherche d'opportunités** — listicles, comparatifs, mentions sans lien, liens cassés, besoins journalistiques → `opportunities.csv`. Détail : [references/workflow.md](references/workflow.md#phase-3)
4. **Scoring et sélection** — noter chaque opportunité sur 100, rejeter < 40, choisir UNE action P0. Barème complet : [references/scoring.md](references/scoring.md)
5. **Production de l'actif citable** — brief, contenu, sources, plan d'implémentation dans `assets/<slug>/`. Schémas : [references/output-schemas.md](references/output-schemas.md)
6. **Prospection** — `prospects.csv`, uniquement des cibles avec raison éditoriale réelle et preuve de personnalisation.
7. **Brouillons d'outreach** — `outreach/<date>.md`, jamais envoyés automatiquement.
8. **Rapport** — `reports/<date>.md`, synthèse et prochaine action unique.

Workflow détaillé (contenu exact de chaque phase, fichiers, critères de complétion) : [references/workflow.md](references/workflow.md).

## Garde-fous (à respecter à chaque phase)

- Pas de PBN, pas d'achat de lien dofollow, pas d'échange massif de liens, pas de réseau automatique entre les SaaS de l'utilisateur.
- Pas de faux avis, fausse citation, fausse statistique, fausse identité.
- Pas de génération massive de pages quasi identiques, pas de spam email/formulaire.
- Pas de contournement de connexion, paywall, robots.txt ou anti-bot.
- Un lien entre deux projets de l'utilisateur n'est recommandé que s'il est utile au lecteur, contextuellement pertinent, et existerait même sans objectif SEO.
- Détail complet des politiques et interdictions : [references/policies.md](references/policies.md)
- Hiérarchie et exigences de qualité des sources : [references/source-quality.md](references/source-quality.md)

## Scoring — résumé

Positif (100 max) : pertinence thématique (25) + valeur éditoriale (20) + probabilité d'obtention (15) + autorité de la source (15) + potentiel de citation IA (15) + faible effort (10).
Pénalités : réseau artificiel -50, site spammy -50, hors sujet -30, donnée invérifiable -25, outreach générique -15, contrepartie cachée -50, achat de lien dofollow -50, contenu quasi identique à grande échelle -40.
Rejet automatique si score final < 40.
Détail et ordre de priorité à score égal : [references/scoring.md](references/scoring.md)

## Sortie de fin d'exécution

Rester concis pendant l'exécution — pas de récapitulatif long après chaque phase. À la fin d'un lancement, afficher uniquement :

```
Phase atteinte
Action P0 sélectionnée
Fichiers produits
Blocage éventuel
Prochaine action
```

Ne jamais annoncer qu'un backlink, une citation IA ou un résultat SEO est garanti.

## Références du skill

- [references/workflow.md](references/workflow.md) — déroulé complet des 8 phases, contenu exact des fichiers, critères de reprise.
- [references/scoring.md](references/scoring.md) — barème détaillé, pénalités, ordre de priorité P0.
- [references/policies.md](references/policies.md) — politiques Google, interdictions, conditions de lien inter-SaaS.
- [references/source-quality.md](references/source-quality.md) — hiérarchie des sources, gestion des contradictions.
- [references/output-schemas.md](references/output-schemas.md) — schémas exacts de `state.json`, `project.json`, CSV, assets.
- [assets/](assets/) — exemples et gabarits (project, state, opportunities, prospects, sources, outreach, report).
