---
name: seo
description: >-
  Moteur autonome SEO, GEO et digital PR pour SaaS : audite un projet, cherche et note des opportunités (listicles, comparatifs, mentions sans lien, liens cassés, besoins journalistiques), produit un actif citable (brief, contenu, sources, plan d'implémentation), qualifie des prospects et rédige des brouillons d'outreach sans jamais les envoyer. À lancer manuellement avec /seo dans le dépôt d'un projet. Ne modifie ni le code du site ni les comptes ; pour l'audit technique du site lui-même, voir le skill compagnon seo-geo-optimizer.
disable-model-invocation: true
license: MIT
compatibility: Aucun runtime requis pour le skill. Conçu pour Claude Code (le champ disable-model-invocation est propre à Claude Code). La phase de recherche d'opportunités demande un outil de recherche web ; sans lui le skill continue avec les données locales. Python 3.10+ uniquement pour scripts/check_outputs.py.
metadata:
  author: Anto1nx
  version: "1.2.0"
  repository: https://github.com/RAAAAAGEEEEE/citation-engine-skill
---

# seo (moteur de citations)

Version 1.2.0 (historique : [CHANGELOG.md](CHANGELOG.md)).

Moteur SEO/GEO multi-SaaS pour développeur indépendant. Une seule commande :
`/seo`. Objectif : maximiser le rapport impact/effort. Pas une fabrique à
backlinks, pas de spam, pas de réseau artificiel entre les produits d'un même
éditeur.

## Périmètre
- **Dans** : audit produit, éditorial et technique de surface (README, sitemap,
  robots.txt, métadonnées, contenu existant) ; recherche et notation
  d'opportunités ; production d'un actif citable sous forme de fichiers
  Markdown/CSV ; qualification de prospects ; brouillons d'outreach ; rapport.
- **Hors** :
  - modifier le code applicatif, publier une page, créer un commit : le skill
    livre du contenu et un plan d'implémentation, pas une exécution ;
  - envoyer un message, remplir un formulaire, publier sur un réseau ;
  - audit technique approfondi et corrections dans le code du site (maillage,
    schema, crawlers, Core Web Vitals) : skill compagnon
    [seo-geo-optimizer](https://github.com/RAAAAAGEEEEE/claude-skill-seo-geo-optimizer) ;
  - achat de lien, échange de liens, PBN, faux avis, fausse statistique.
- Sur un même projet : `seo-geo-optimizer` d'abord (site sain), `/seo` ensuite
  (visibilité externe).

## Quand l'utiliser
Manuellement, jamais de déclenchement automatique (`disable-model-invocation`) :
- premier passage sur un projet : audit et choix d'une action P0 ;
- relance après une interruption : reprise à la première phase incomplète ;
- préparer un actif citable (page de statistiques, benchmark, calculateur,
  comparatif) et les prospects qui pourraient le citer ;
- récupérer des mentions sans lien ou remplacer une ressource cassée.

## Modes d'exécution
Un seul point d'entrée, deux modes choisis d'après `state.json` :
1. **Initialisation** : aucun `.citation-engine/state.json` valide dans le
   dépôt courant. Le skill démarre à la phase 1.
2. **Reprise** : `state.json` valide. Le skill reprend à la première phase de
   `pending_phases` et ne refait jamais une phase de `completed_phases` sans
   raison écrite dans `last_error` ou `notes`.
   `state.json` invalide : rien n'est écrasé, l'erreur est notée et le skill
   propose de reprendre depuis la dernière phase valide.

À chaque lancement :
1. Résoudre le chemin absolu du dépôt courant.
2. Chercher `<racine>/.citation-engine/state.json`.
3. Examiner le projet AVANT de poser une question (README, package.json,
   config, sitemap, robots.txt, métadonnées, contenu existant).
4. Regrouper les informations bloquantes en UN SEUL message, 3 questions
   maximum. Si l'URL canonique est introuvable, c'est la seule question.
5. Enchaîner toutes les phases sans demander confirmation entre elles.
6. Mettre à jour `state.json` après chaque phase, en dernier, et jamais si les
   fichiers obligatoires de la phase manquent ou sont invalides.

Ne jamais inventer une donnée manquante : `null`, `[]` ou
`[À VÉRIFIER : description précise]`.

## Phases (ordre fixe)
1. **Initialisation** : arborescence `.citation-engine/`, `project.json`,
   `state.json`. [Détail](references/workflow.md#phase-1--initialisation)
2. **Audit** : produit, technique, éditorial, dans `audit.md`.
   [Détail](references/workflow.md#phase-2--audit)
3. **Recherche d'opportunités** : listicles, comparatifs, mentions sans lien,
   liens cassés, besoins journalistiques, dans `opportunities.csv`.
   [Détail](references/workflow.md#phase-3--recherche-dopportunités)
4. **Scoring et sélection** : note sur 100, rejet sous 40, UNE action P0.
   Barème : [references/scoring.md](references/scoring.md)
5. **Production de l'actif citable** : brief, contenu, sources, plan
   d'implémentation dans `assets/<slug>/`. Schémas :
   [references/output-schemas.md](references/output-schemas.md). Rédaction du
   contenu : skill `redaction` s'il est installé.
6. **Prospection** : `prospects.csv`, uniquement des cibles avec une raison
   éditoriale réelle et une preuve de personnalisation.
7. **Brouillons d'outreach** : `outreach/<date>.md`, jamais envoyés. Rédaction
   et relecture : skill `redaction` s'il est installé.
8. **Rapport** : `reports/<date>.md`, synthèse et prochaine action unique.

Déroulé complet, contenu exact des fichiers et critères de complétion :
[references/workflow.md](references/workflow.md).

## Entrées et sorties
- **Entrées** : le dépôt courant (lecture seule) et, si disponible, un outil de
  recherche web. Aucune variable d'environnement, aucun compte, aucune clé
  ([docs/CONFIGURATION.md](docs/CONFIGURATION.md)).
- **Sorties** : uniquement sous `<racine>/.citation-engine/` :
  `state.json`, `project.json`, `audit.md`, `opportunities.csv`,
  `prospects.csv`, `assets/<slug>/` (`BRIEF.md`, `CONTENT.md`, `sources.csv`,
  `implementation.md`), `outreach/<date>.md`, `reports/<date>.md`.
- Contrôle des sorties : `python scripts/check_outputs.py <dossier>`
  ([docs/USAGE.md](docs/USAGE.md#vérifier-les-fichiers-produits)).

## Garde-fous (à chaque phase)
- Pas de PBN, pas d'achat de lien dofollow, pas d'échange massif de liens, pas
  de réseau automatique entre les SaaS de l'utilisateur.
- Pas de faux avis, fausse citation, fausse statistique, fausse identité.
- Textes destinés à un lecteur (actif citable, brouillons d'outreach) : aucun
  tiret cadratin, aucun émoji, relecture séparée avant de les proposer ; règles
  détaillées dans le skill `redaction`
  ([claude-skill-redaction](https://github.com/RAAAAAGEEEEE/claude-skill-redaction)).
- Pas de génération massive de pages quasi identiques, pas de spam email ou
  formulaire.
- Pas de contournement de connexion, paywall, robots.txt ou anti-bot.
- Un lien entre deux projets de l'utilisateur n'est recommandé que s'il est
  utile au lecteur, contextuellement pertinent, et existerait même sans
  objectif SEO.
- Détail : [references/policies.md](references/policies.md).

## Niveaux de preuve
Ce skill ne pose pas d'étiquettes ESTABLISHED/SUPPORTED/CLAIMED. Il classe les
sources par fiabilité décroissante (source primaire officielle, documentation
officielle, publication scientifique, organisme public, données propriétaires
avec méthodologie, média citant sa source, étude sectorielle, source secondaire
vérifiable, opinion identifiée) et note un `confidence` (`high`, `medium`,
`low`) dans `sources.csv`. Contradiction entre sources : les deux sont
conservées, la source primaire l'emporte, l'incertitude reste visible.
Détail : [references/source-quality.md](references/source-quality.md).

## Scoring (résumé)
Positif (100 max) : pertinence thématique (25) + valeur éditoriale (20) +
probabilité d'obtention (15) + autorité de la source (15) + potentiel de
citation IA (15) + faible effort (10). Pénalités : réseau artificiel -50, site
spammy -50, hors sujet -30, donnée invérifiable -25, outreach générique -15,
contrepartie cachée -50, achat de lien dofollow -50, contenu quasi identique à
grande échelle -40. Rejet automatique sous 40. Détail et ordre de priorité à
score égal : [references/scoring.md](references/scoring.md).

## Replis et gestion d'erreurs
- Outil de recherche web indisponible : continuer avec les données locales,
  noter la limite dans `state.json.last_error` et dans `audit.md`, laisser
  `opportunities.csv` vide avec ses en-têtes plutôt que d'inventer des lignes.
- Page inaccessible (403, paywall, rendu JavaScript) : noter « non vérifié »,
  ne jamais prétendre l'avoir lue.
- URL canonique introuvable : la demander, seule.
- `state.json` invalide : ne pas l'écraser, voir « Modes d'exécution ».
- Écriture sûre : préparer, valider la structure, écrire, relire, mettre à jour
  `state.json` en dernier. En cas d'échec, garder les phases déjà terminées et
  relancer `/seo`.

## Sécurité et confidentialité
- Le skill lit le dépôt courant et, avec un outil de recherche web, des pages
  publiques. Il n'envoie rien : ni e-mail, ni formulaire, ni publication.
- Aucun appel à une API payante ou à un service tiers n'est codé dans le skill.
- Les prospects sont des organisations et des pages de contact publiques. Ne
  jamais collecter une adresse personnelle non publiée, ne jamais inventer un
  nom, une fonction ou un e-mail.
- `.citation-engine/` contient des données de travail du projet (concurrents,
  prospects) : à ne pas publier telles quelles.
- Détail : [docs/PRIVACY_AND_SECURITY.md](docs/PRIVACY_AND_SECURITY.md).

## Procédures PLAN / FIX / VERIFY
Le skill ne modifie pas le code du site : pas de phase FIX. Son équivalent :
- **PLAN** : `implementation.md` de l'actif (où publier, maillage, prérequis,
  checklist de mise en ligne), soumis au propriétaire.
- **Produire** : les fichiers de `.citation-engine/`, sans toucher au reste du
  dépôt.
- **VERIFY** : `python scripts/check_outputs.py .citation-engine` avant de
  clore une exécution ; sortie 0 exigée.

## Exemples d'invocation
- `/seo` dans le dépôt d'un projet sans `.citation-engine/` : initialisation
  puis les 8 phases.
- `/seo` après une interruption : reprise à la première phase incomplète.
- `/seo` dans un dépôt sans URL publique détectable : une seule question, l'URL
  canonique.

## Exemple de sortie (illustratif, données fictives)
Fin d'exécution sur un projet fictif `example.com` :
```
Phase atteinte : rapport (8/8)
Action P0 sélectionnée : page de statistiques propriétaire « Rendez-vous manqués chez les artisans » (score 82)
Fichiers produits : .citation-engine/assets/stats-rdv-artisans/{BRIEF.md,CONTENT.md,sources.csv,implementation.md},
  .citation-engine/outreach/2026-09-29.md (3 brouillons, BROUILLON — NON ENVOYÉ), reports/2026-09-29.md
Blocage éventuel : aucun ; 2 statistiques marquées [À VÉRIFIER] dans CONTENT.md
Prochaine action : publier l'actif (plan dans implementation.md), puis relancer /seo pour le suivi
```

## Sortie de fin d'exécution
Rester concis pendant l'exécution, sans récapitulatif long après chaque phase.
À la fin, afficher uniquement : phase atteinte, action P0 sélectionnée, fichiers
produits, blocage éventuel, prochaine action. Ne jamais annoncer qu'un backlink,
une citation IA ou un résultat SEO est garanti.

## Évaluations
[evals/evals.json](evals/evals.json) : 12 cas au format du skill-creator
d'Anthropic (`prompt`, `expected_output`, `expectations`, `files`). Les fichiers
d'entrée sont les exemples de [assets/](assets/). Ce sont des critères à faire
vérifier par un relecteur ou le skill-creator ; ils ne s'exécutent pas seuls.

## Installation
- Personnelle : `git clone https://github.com/RAAAAAGEEEEE/citation-engine-skill.git ~/.claude/skills/seo`
- Par projet : même commande vers `.claude/skills/seo/` à la racine du projet.

Détail et migration depuis l'ancienne commande `/SEO` :
[docs/INSTALLATION.md](docs/INSTALLATION.md).

## Versionnement
Versionnement sémantique, version dans le front-matter (`metadata.version`) et
dans [CHANGELOG.md](CHANGELOG.md). Un changement de schéma de `state.json` ou
des CSV incrémente `schema_version` et la version majeure ou mineure du skill.

## Références et attributions
- [references/workflow.md](references/workflow.md) : les 8 phases en détail.
- [references/scoring.md](references/scoring.md) : barème et priorité P0.
- [references/policies.md](references/policies.md) : politiques et interdictions.
- [references/source-quality.md](references/source-quality.md) : hiérarchie des sources.
- [references/output-schemas.md](references/output-schemas.md) : schémas exacts.
- [assets/](assets/) : gabarits et exemples fictifs.
- Attributions : [docs/LEGAL_AND_ATTRIBUTION.md](docs/LEGAL_AND_ATTRIBUTION.md).
