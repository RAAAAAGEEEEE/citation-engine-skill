# Installation

Retour : [README](../README.md) · Suite : [USAGE](USAGE.md).

## Prérequis
- Claude Code, avec accès au dépôt du projet à traiter.
- Git, pour cloner.
- Python 3.10 ou plus récent, seulement pour `scripts/check_outputs.py`
  (bibliothèque standard, aucun `pip install`). Vérifié avec 3.11 le
  2026-09-29.

## Installation personnelle (tous les projets)
```bash
git clone https://github.com/RAAAAAGEEEEE/citation-engine-skill.git ~/.claude/skills/seo
```
Le dossier doit s'appeler `seo` : c'est le champ `name` du front-matter, et la
commande est `/seo`.

## Installation par projet
Cloner ou copier le dépôt dans `.claude/skills/seo/` à la racine du projet :
```bash
git clone https://github.com/RAAAAAGEEEEE/citation-engine-skill.git .claude/skills/seo
```

## Vérifier l'installation
Depuis le dossier du skill :
```bash
python -m unittest discover -s tests
```
Résultat attendu : `Ran 7 tests` puis `OK`. Aucune requête réseau. Dans Claude
Code, la commande `/seo` doit apparaître dans la liste des commandes.

Vérification faite le 2026-09-29 dans un dossier vide : clone du dépôt, puis
les 7 tests, OK.

## Mise à jour
```bash
cd ~/.claude/skills/seo && git pull
```
Lire [CHANGELOG.md](../CHANGELOG.md) avant : les ruptures y sont signalées.

## Migration depuis `/SEO` (versions antérieures à 1.2.0)
Jusqu'à la version 1.1.0 le skill s'appelait `SEO` (commande `/SEO`). Depuis la
1.2.0, `name: seo` (commande `/seo`). Les données déjà produites dans
`.citation-engine/` restent valides : le schéma n'a pas changé. Si votre
dossier local s'appelle encore `SEO`, il fonctionne, mais le nom du dossier
devrait correspondre au champ `name`.

## Désinstallation
Supprimer le dossier `~/.claude/skills/seo` (ou `.claude/skills/seo`). Les
dossiers `.citation-engine/` des projets sont conservés : ce sont vos données.
