# Changelog

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).

## [1.2.0] - 2026-09-29

Préparation à la publication communautaire.

### Modifié (rupture mineure)
- Le skill s'appelle `seo` (commande `/seo`) au lieu de `SEO` (`/SEO`), pour
  respecter le nommage portable des Agent Skills (minuscules). Le schéma des
  fichiers ne change pas : les `.citation-engine/` existants restent valides.
  Migration : [docs/INSTALLATION.md](docs/INSTALLATION.md#migration-depuis-seo-versions-antérieures-à-120).
- Front-matter de `SKILL.md` : ajout de `license`, `compatibility`, `metadata`
  (auteur, version, dépôt). `disable-model-invocation` est conservé et documenté
  dans le README (section Compatibilité).
- `SKILL.md` : périmètre et hors-périmètre, modes d'exécution, entrées et
  sorties, replis, sécurité, PLAN/FIX/VERIFY, exemples, installation.
- Anonymisation : exemples propres à l'auteur remplacés par des exemples neutres
  dans `references/policies.md`.
- `assets/sources.example.csv` : statistiques d'exemple marquées
  `[EXEMPLE FICTIF]`.

### Ajouté
- `LICENSE` (MIT), `CONTRIBUTING.md`, `SECURITY.md`.
- `docs/` : architecture, installation, usage, configuration, dépannage,
  limites, confidentialité et sécurité, mentions légales.
- `scripts/check_outputs.py` : contrôle des fichiers produits (champs,
  en-têtes, somme des scores, seuil de rejet, doublons) et
  `tests/test_check_outputs.py` (7 tests).
- `evals/evals.json` converti au format du skill-creator d'Anthropic, avec un
  `prompt` et des fichiers d'entrée par cas (12 cas).

## [1.1.0] - 2026-09-28

### Ajouté
- Renvoi vers le skill `redaction` pour rédiger l'actif citable (phase 5)
  et les brouillons d'outreach (phase 7).
- Garde-fou : textes destinés à un lecteur sans tiret cadratin ni émoji,
  relus par une passe séparée.

## [1.0.0] - 2026-07-15

Première version.
