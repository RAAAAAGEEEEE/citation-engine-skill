# Confidentialité et sécurité

Retour : [README](../README.md) · Voir aussi : [SECURITY.md](../SECURITY.md),
[LIMITATIONS](LIMITATIONS.md).

## Quelles données sortent, et vers où
| Donnée | Destination | Quand |
|---|---|---|
| Contenu du dépôt courant (README, config, pages) | Le modèle Claude, comme tout ce que Claude Code lit | À chaque lancement, selon les règles de votre environnement |
| Requêtes de recherche (nom du produit, concurrents, thèmes) | L'outil de recherche web de votre environnement | Phases 3 et 6, seulement si un outil de recherche est disponible |
| Rien d'autre | Aucun envoi d'e-mail, de formulaire, de publication, aucune API tierce codée dans le skill | Jamais |

Le skill ne contient aucun code réseau. `scripts/check_outputs.py` lit des
fichiers locaux et n'écrit rien.

## Données de prospection
`.citation-engine/prospects.csv` et `outreach/` contiennent des noms
d'organisations et des pages de contact publiques, parfois un nom de
contact public. Règles appliquées par le skill :
- pas d'adresse personnelle non publiée, pas de nom, de fonction ou d'e-mail
  inventé (préférer `public_contact_url`) ;
- pas de contournement de connexion, paywall, robots.txt ou anti-bot ;
- chaque vérification est datée (`verified_at`).

Ne publiez pas `.citation-engine/` tel quel (liste de concurrents et de
prospects) : ajoutez-le à `.gitignore` si le dépôt du projet est public.
N'y joignez jamais de secret : le skill n'en a pas besoin et ne les lit pas
volontairement.

## Garde-fous contre les abus
Le skill refuse par conception : PBN, achat ou échange massif de liens, faux
avis, fausse citation, fausse statistique, fausse identité, génération massive
de pages quasi identiques, spam par e-mail ou formulaire. Liste complète :
[references/policies.md](../references/policies.md).

## Envoi : décision humaine
Les brouillons sont marqués `BROUILLON — NON ENVOYÉ`.
`approval_required_for_outreach` reste `true`. Toute future fonction d'envoi
exigerait une validation explicite, prospect par prospect.

## Injection de contenu
Le skill lit des pages web tierces. Une page peut contenir du texte adressé à un
agent (« ignore tes règles », « envoie un e-mail à... »). Ce texte est une
donnée, pas une instruction : il ne change ni le périmètre du skill, ni ses
garde-fous. Signalez un cas contraire via [SECURITY.md](../SECURITY.md).

## Vérification
`python scripts/check_outputs.py <dossier>` détecte un fichier mal formé, pas un
secret ni une donnée personnelle : relisez `.citation-engine/` avant de le
partager.
