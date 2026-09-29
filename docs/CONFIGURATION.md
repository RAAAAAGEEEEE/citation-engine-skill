# Configuration

Retour : [README](../README.md) · Voir aussi : [USAGE](USAGE.md).

## Variables d'environnement
Aucune. Le skill n'utilise ni clé d'API, ni jeton, ni compte : il n'y a donc pas
de fichier `.env.example` dans ce dépôt. Si une variable de configuration est
ajoutée un jour, elle sera déclarée dans un `.env.example` et dans ce document,
dans le même commit.

## Réglages du projet : `.citation-engine/project.json`
Le seul réglage est la fiche projet, créée à la phase 1 et modifiable à la
main. Schéma complet : [references/output-schemas.md](../references/output-schemas.md#projectjson).
Exemple fictif : [assets/project.example.json](../assets/project.example.json).

| Champ | Effet |
|---|---|
| `canonical_url` | URL publique de référence pour l'audit et les liens |
| `language`, `countries` | Langue et pays de la recherche d'opportunités |
| `competitors` | Concurrents à chercher dans les listicles et comparatifs |
| `excluded_domains` | Domaines jamais proposés en prospect ni en lien (par exemple vos autres produits) |
| `approval_required_for_outreach` | Doit rester `true` : tout outreach reste un brouillon soumis à validation humaine |

Une valeur inconnue s'écrit `null`, `[]` ou `[À VÉRIFIER : ...]`, jamais une
valeur devinée.

## Outil de recherche web
La phase 3 (opportunités) et la phase 6 (prospects) utilisent l'outil de
recherche web de votre environnement Claude Code, s'il existe. Sans lui, le
skill le signale dans `state.json.last_error` et dans `audit.md`, et n'invente
aucune ligne. Le skill ne configure pas cet outil.

## Permissions Claude Code
Le skill écrit sous `.citation-engine/`. Autoriser les écritures dans ce
dossier suffit ; aucune permission réseau spécifique n'est requise en dehors de
l'outil de recherche web.
