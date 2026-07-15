# Workflow détaillé — SEO

Ce fichier détaille les 8 phases exécutées par `/SEO`. Voir [SKILL.md](../SKILL.md) pour le résumé et les principes d'exécution globaux.

## Reprise

À chaque lancement :

1. Chemin absolu du dépôt courant = racine.
2. Si `<racine>/.citation-engine/state.json` existe :
   - valider le JSON ;
   - si invalide ou corrompu, enregistrer `last_error`, ne pas écraser le fichier, informer l'utilisateur et proposer de reprendre depuis la dernière phase confirmée valide ;
   - sinon reprendre à la première phase listée dans `pending_phases`.
3. Sinon, initialiser un nouveau `state.json` (Phase 1) avec `current_phase: "initialisation"`.

Ne jamais recommencer une phase déjà dans `completed_phases` sans raison documentée dans `state.json.last_error` ou `notes`.

## Phase 1 — Initialisation

Créer dans le dépôt courant :

```
.citation-engine/
  state.json
  project.json
  audit.md
  opportunities.csv
  prospects.csv
  assets/
  outreach/
  reports/
```

Ne pas écraser un travail existant. Avant de modifier un fichier déjà rempli : le lire, préserver les données utiles, fusionner les nouvelles informations, mettre à jour `updated_at`.

`project.json` doit contenir au minimum les champs listés dans [output-schemas.md](output-schemas.md#projectjson). Ne jamais inventer une valeur manquante — utiliser `null`, `[]`, ou `[À VÉRIFIER : description précise]`.

Détection automatique avant toute question : README, package.json, fichiers de config, documentation, routes publiques, pages marketing, sitemap, robots.txt, métadonnées, données structurées, contenus existants.

Si l'URL canonique publique ne peut pas être déterminée depuis le dépôt : c'est la seule information à demander explicitement si aucune autre donnée bloquante n'existe. Sinon, regrouper toutes les informations bloquantes en un seul message, 3 questions maximum.

Phase terminée quand `project.json` et `state.json` existent et sont valides (JSON bien formé, champs obligatoires présents même si `null`).

## Phase 2 — Audit

Analyser : produit, proposition de valeur, cibles, intentions de recherche, questions des acheteurs, concurrents, preuves existantes, contenu existant, pages indexables, maillage interne, sitemap, robots.txt, canonical URLs, titles/meta descriptions, H1, données structurées, présence de contenu textuel accessible, pages de comparaison, statistiques/études/datasets/calculateurs existants, éléments citables par journalistes ou moteurs IA.

Produire `audit.md` avec :
- résumé du produit
- état technique
- état éditorial
- actifs citables existants
- lacunes
- risques
- opportunités rapides
- informations à vérifier
- recommandations P0, P1, P2

Chaque constat doit être relié à un fichier, une URL ou une preuve identifiable — pas de liste générique.

Phase terminée quand `audit.md` existe et contient les 9 sections ci-dessus.

## Phase 3 — Recherche d'opportunités

Si les outils de recherche web sont disponibles, rechercher (dans la langue et les pays du projet) :

1. comparatifs/listicles citant les concurrents
2. pages "best tools" / "alternatives" / "software" / "apps" et équivalents
3. backlinks éditoriaux reproductibles des concurrents
4. mentions de la marque/du fondateur sans lien
5. liens cassés pointant vers des ressources concurrentes
6. liens vers des ressources obsolètes
7. pages de statistiques faibles, anciennes ou peu sourcées
8. journalistes/blogs/médias recherchant experts ou données
9. resource pages pertinentes
10. opportunités de citation issues de données originales
11. questions complexes déclenchant AI Mode ou comparaison
12. contenus tiers déjà utilisés comme sources sur le sujet

Contraintes strictes : pas de contournement de connexion, paywall, robots.txt ou anti-bot ; pas de collecte d'adresse personnelle non publiée pour usage professionnel ; ne jamais prétendre avoir consulté une page inaccessible ; dater chaque vérification (ISO 8601) ; conserver les URL sources ; distinguer fait observé et hypothèse.

Si les outils de recherche web sont indisponibles : signaler la limite dans `state.json.last_error` et dans `audit.md`, ne pas produire `opportunities.csv` inventé — le laisser vide avec ses en-têtes, ou ne le créer que lorsque des données réelles existent.

Écrire/mettre à jour `opportunities.csv` avec les en-têtes fixes (voir [output-schemas.md](output-schemas.md#opportunitiescsv)). Dédupliquer par type + domaine + URL source + URL cible.

Phase terminée quand `opportunities.csv` existe avec en-têtes corrects (même vide, avec une note dans `state.json` si aucune donnée n'a pu être trouvée).

## Phase 4 — Scoring et sélection

Voir [scoring.md](scoring.md) pour le barème complet.

Scorer chaque ligne de `opportunities.csv`. Rejeter (statut `rejected`) si score total < 40. Sélectionner UNE action P0 principale selon l'ordre de priorité documenté dans scoring.md à score comparable.

Enregistrer `selected_opportunity` dans `state.json` avec : impact attendu, effort, preuve, risques, raison de la priorité sur les autres candidats.

Phase terminée quand `state.json.selected_opportunity` est renseigné et que `opportunities.csv` contient une colonne `total_score` et `status` remplies pour chaque ligne évaluée.

## Phase 5 — Production de l'actif citable

Créer `.citation-engine/assets/<slug>/` avec au minimum :
- `BRIEF.md`
- `CONTENT.md`
- `sources.csv` (en-têtes : voir [output-schemas.md](output-schemas.md#sourcescsv))
- `implementation.md`

Contenu selon le type d'actif (voir [output-schemas.md](output-schemas.md#assets) pour le détail complet) : title, meta description, slug, H1, structure H2/H3, intro, contenu principal, tableaux, méthodologie, limites, auteur/organisation, dates de publication/mise à jour, CTA, plan de maillage interne, JSON-LD si applicable, plan de maintenance, fréquence de mise à jour, éléments visuels recommandés, facteurs de citabilité.

Pour pages de statistiques/études/benchmarks/datasets : séparer données externes et propriétaires, méthodologie précise, jamais de chiffre inventé ou extrapolé sans le signaler, chaque source documentée dans `sources.csv`.

Le skill ne modifie pas le code applicatif ni ne publie la page — uniquement du contenu et un plan d'implémentation prêts à l'emploi.

Phase terminée quand les 4 fichiers de l'actif existent et que `sources.csv` a les en-têtes corrects.

## Phase 6 — Prospection

Identifier des prospects pertinents pour l'actif produit. Mettre à jour `prospects.csv` (en-têtes : voir [output-schemas.md](output-schemas.md#prospectscsv)).

Pour chaque prospect : raison éditoriale spécifique, preuve de personnalisation, actif cible proposé, date de vérification, pas de doublon, exclusion des domaines listés dans `project.json.excluded_domains`, aucun nom/fonction/email inventé — privilégier une page de contact professionnelle publique.

Ne pas conserver un prospect sans raison éditoriale réelle.

Phase terminée quand `prospects.csv` existe avec en-têtes corrects (vide accepté si aucun prospect valide trouvé, avec note).

## Phase 7 — Brouillons d'outreach

Créer `.citation-engine/outreach/<date-ISO>.md`. Brouillons uniquement — jamais d'envoi, de remplissage de formulaire, de publication automatique.

Interdits : prétendre avoir lu une page non consultée, inventer relation/citation/statistique, proposer échange de liens ou paiement caché, fausse urgence, message trompeur.

Chaque brouillon : personnalisé, ≤120 mots par défaut, preuve précise liée à la page du destinataire, valeur réelle pour le lecteur, une seule action claire, ton naturel sans jargon SEO, prospect et URL identifiés, marqué `BROUILLON — NON ENVOYÉ`.

Si aucune personnalisation crédible n'est possible pour un prospect : ne pas générer de brouillon pour lui.

Phase terminée quand le fichier outreach du jour existe (même avec 0 brouillon si aucun prospect qualifié).

## Phase 8 — Rapport

Créer `.citation-engine/reports/<date-ISO>.md` avec : projet, URL canonique, date, phase atteinte, action P0 sélectionnée et raison, fichiers créés, nombre d'opportunités (total/rejetées), nombre de prospects, nombre de brouillons, sources principales, limites, éléments à vérifier, blocages, prochaine action unique.

Distinguer dans le suivi : backlinks gagnés, mentions sans lien, citations IA observées, trafic référent, impressions/clics Search Console, leads, conversions, revenus. Ne jamais attribuer automatiquement une variation de trafic/revenu à une action SEO sans preuve suffisante.

Phase terminée quand le rapport du jour existe et que `state.json.completed_phases` contient les 8 phases.

## Écriture sûre des fichiers

1. préparer le contenu ;
2. valider sa structure (JSON parseable, CSV avec en-têtes attendus) ;
3. écrire le fichier ;
4. vérifier qu'il est lisible ;
5. mettre à jour `state.json` en dernier.

En cas d'erreur : enregistrer dans `last_error`, conserver les phases déjà terminées, indiquer le blocage, permettre la reprise via `/SEO`.
