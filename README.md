# seo (citation-engine-skill)

Skill Claude Code qui aide un développeur indépendant à gagner de la visibilité
**hors de son site** : audit du projet, recherche d'opportunités (listicles,
comparatifs, mentions sans lien, liens cassés), production d'un actif citable,
prospects qualifiés et brouillons d'outreach. Une seule commande : `/seo`.

**Statut : bêta.** Version 1.2.0 ([CHANGELOG.md](CHANGELOG.md)). Utilisé sur
quelques projets réels. Les 12 cas d'évaluation ([evals/evals.json](evals/evals.json))
décrivent le comportement attendu mais ne s'exécutent pas automatiquement ;
seul `scripts/check_outputs.py` est testé (7 tests hors ligne).

## Le problème
Publier une bonne page ne suffit pas : Google et les moteurs de réponse IA la
citent surtout si d'autres sites sérieux la mentionnent. Le travail (trouver
les listicles qui oublient votre produit, vérifier chaque source, écrire un
message qui ne ressemble pas à du spam) est long, et la tentation du raccourci
(échange de liens, chiffre inventé) est grande.

## Pour qui
Développeurs et fondateurs qui gèrent un ou plusieurs SaaS ou sites de contenu,
sans équipe marketing, et qui travaillent déjà avec Claude Code.

## Ce que le skill apporte
- **Un cycle en 8 phases, reprenable** : initialisation, audit, opportunités,
  scoring, actif citable, prospection, brouillons, rapport. L'état est dans
  `.citation-engine/state.json` : `/seo` reprend où il s'est arrêté.
- **Un score sur 100, avec pénalités** : une opportunité sous 40 est rejetée,
  un échange de liens ou un site spammy est écarté d'office
  ([references/scoring.md](references/scoring.md)).
- **Aucune donnée inventée** : `null`, `[]` ou `[À VÉRIFIER : ...]` plutôt
  qu'un chiffre plausible ; chaque affirmation chiffrée renvoie à une ligne de
  `sources.csv`.
- **Jamais d'envoi** : les brouillons portent `BROUILLON — NON ENVOYÉ`. Le
  skill ne publie rien et ne touche pas au code du site.

## Exemple de sortie
Fin d'une exécution sur un projet fictif (illustratif, pas une mesure) :
```
Phase atteinte : rapport (8/8)
Action P0 sélectionnée : page de statistiques propriétaire « Rendez-vous manqués chez les artisans » (score 82)
Fichiers produits : .citation-engine/assets/stats-rdv-artisans/{BRIEF.md,CONTENT.md,sources.csv,implementation.md},
  .citation-engine/outreach/2026-09-29.md (3 brouillons, BROUILLON — NON ENVOYÉ), reports/2026-09-29.md
Blocage éventuel : aucun ; 2 statistiques marquées [À VÉRIFIER] dans CONTENT.md
Prochaine action : publier l'actif (plan dans implementation.md), puis relancer /seo pour le suivi
```
Des fichiers d'exemple complets (fictifs) sont dans [assets/](assets/).

## Prérequis
- Claude Code, avec accès au dépôt du projet à traiter.
- Un outil de recherche web pour la phase 3 (sans lui, le skill continue avec
  les données locales et le dit).
- Python 3.10+ seulement pour `scripts/check_outputs.py` (bibliothèque standard).

## Installation
```bash
git clone https://github.com/RAAAAAGEEEEE/citation-engine-skill.git ~/.claude/skills/seo
```
Pour un seul projet : `.claude/skills/seo/` à la racine du projet. Détail :
[docs/INSTALLATION.md](docs/INSTALLATION.md).

## Démarrage rapide
1. Ouvrir Claude Code dans le dépôt du projet.
2. Lancer `/seo`.
3. Répondre aux éventuelles questions bloquantes (3 maximum).
4. Relancer `/seo` après toute interruption.

Contrôler ensuite les fichiers produits (depuis le dossier du skill) :
```bash
python scripts/check_outputs.py /chemin/vers/le/projet/.citation-engine
```

## Exemple minimal
Contrôler les fichiers d'exemple fournis, depuis le dossier du skill :
```bash
python scripts/check_outputs.py assets/state.example.json assets/opportunities.example.csv
```
Sortie attendue (exécutée sous Windows le 2026-09-29 ; sous Linux et macOS
les chemins s'affichent avec `/`) :
```
OK   assets\state.example.json
OK   assets\opportunities.example.csv
2/2 fichier(s) valide(s)
```

## Architecture
- `SKILL.md` : la procédure suivie par Claude.
- `references/` : workflow détaillé, barème, politiques, qualité des sources,
  schémas.
- `assets/` : gabarits et exemples fictifs.
- `scripts/check_outputs.py` : contrôle des fichiers produits.
- `evals/` et `tests/` : cas d'évaluation et tests.

Détail : [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Configuration
Aucune : pas de variable d'environnement, pas de clé, pas de compte. Le seul
réglage est propre au projet, dans `.citation-engine/project.json` (domaines à
exclure, validation humaine de l'outreach). Voir
[docs/CONFIGURATION.md](docs/CONFIGURATION.md).

## Sécurité et confidentialité
Le skill lit le dépôt courant et, avec un outil de recherche web, des pages
publiques. Il n'envoie ni e-mail, ni formulaire, ni publication, et n'appelle
aucune API payante. Les données de prospection restent dans `.citation-engine/`
(à ne pas publier). Voir [SECURITY.md](SECURITY.md) et
[docs/PRIVACY_AND_SECURITY.md](docs/PRIVACY_AND_SECURITY.md).

## Compatibilité
Le front-matter de [SKILL.md](SKILL.md) suit le format ouvert des Agent Skills
(`name`, `description`, `license`, `compatibility`, `metadata`). Un seul champ
est propre à Claude Code : `disable-model-invocation: true`. Il empêche Claude
de déclencher le skill de lui-même : il ne s'exécute que sur `/seo`. Il est
indispensable ici, car le skill enchaîne 8 phases et écrit dans le dépôt. Les
agents qui ne connaissent pas ce champ l'ignorent et pourraient charger le
skill de leur propre initiative.

Skill compagnon : [seo-geo-optimizer](https://github.com/RAAAAAGEEEEE/claude-skill-seo-geo-optimizer)
(audit technique et corrections dans le code du site).

## Limites
- Aucune garantie de backlink, de citation IA ou de gain de trafic.
- Pas de mesure directe des citations dans ChatGPT, Gemini ou Perplexity.
- La recherche dépend de l'outil web disponible : pages en 403, derrière un
  paywall ou rendues en JavaScript = « non vérifié ».
- Pas d'envoi, donc pas de suivi des réponses : le suivi des résultats est
  manuel.
- Les évaluations ne sont pas exécutées automatiquement.

Liste complète : [docs/LIMITATIONS.md](docs/LIMITATIONS.md).

## Feuille de route (non contractuelle)
- Exécuter les évaluations automatiquement avec le skill-creator d'Anthropic.
- Étendre `check_outputs.py` (dates ISO 8601, cohérence entre exécutions).

## Contribution
Voir [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence
MIT, voir [LICENSE](LICENSE).

## Documentation
- [SKILL.md](SKILL.md) : la procédure.
- [docs/](docs/) : installation, usage, configuration, architecture,
  dépannage, limites, sécurité, attributions.
- [references/](references/) : workflow, scoring, politiques, sources, schémas.
- [CHANGELOG.md](CHANGELOG.md) : les versions.
