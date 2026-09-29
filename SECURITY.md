# Politique de sécurité

## Surface
Le skill ne contient aucun code réseau et n'utilise aucun secret. Sa surface est
celle d'un agent qui lit du contenu web tiers et écrit des fichiers dans le
dépôt du projet : injection d'instructions par une page lue, écriture hors de
`.citation-engine/`, envoi non voulu d'un message. Détail :
[docs/PRIVACY_AND_SECURITY.md](docs/PRIVACY_AND_SECURITY.md).

## Versions suivies
Seule la dernière version publiée (voir [CHANGELOG.md](CHANGELOG.md)) reçoit des
correctifs.

## Signaler une vulnérabilité
Ne pas ouvrir d'issue publique avec les détails. Utiliser le signalement privé
de GitHub (onglet **Security** > **Report a vulnerability**) sur ce dépôt. Si ce
canal n'est pas activé, ouvrir une issue qui demande seulement un contact,
**sans** détail technique.

Exemples de sujets à signaler :
- un cas où le skill envoie, publie ou remplit un formulaire sans validation
  humaine ;
- une page web lue qui parvient à modifier le comportement ou les garde-fous du
  skill ;
- une écriture hors de `.citation-engine/` ;
- un secret ou une donnée personnelle recopié dans un fichier produit.

## Bonnes pratiques d'utilisation
- Garder `approval_required_for_outreach` à `true`.
- Ne pas publier `.citation-engine/` (concurrents, prospects).
- Relire chaque brouillon et chaque chiffre avant tout envoi ou publication.
