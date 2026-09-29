# Politiques et garde-fous — SEO

Voir [SKILL.md](../SKILL.md) pour le résumé. Ce fichier détaille les règles appliquées à chaque phase.

## Principes

Le skill doit :

- respecter les politiques Google contre le link spam ;
- respecter les règles contre le scaled content abuse ;
- respecter les règles contre le site reputation abuse ;
- privilégier le contenu people-first ;
- produire du contenu original, vérifiable et utile ;
- rechercher des mentions et liens éditorialement justifiables ;
- éviter toute optimisation destinée uniquement à manipuler le classement ;
- traiter les backlinks comme un résultat éditorial, jamais comme une métrique à fabriquer.

## Interdictions strictes

- aucun PBN (private blog network) ;
- aucun achat de lien dofollow ;
- aucun échange massif de liens ;
- aucun réseau automatique entre les SaaS de l'utilisateur ;
- aucun faux avis ;
- aucune fausse citation ;
- aucune fausse statistique ;
- aucun faux journaliste ;
- aucune fausse identité ;
- aucune génération massive de pages quasi identiques ;
- aucun spam par email ;
- aucun spam par formulaire ;
- aucun contournement de restrictions techniques (connexion, paywall, robots.txt, anti-bot).

## Liens entre les SaaS de l'utilisateur

Un lien entre deux projets de l'utilisateur (ex. deux produits SaaS d'un même éditeur) ne peut être recommandé que si toutes ces conditions sont réunies :

- il est directement utile au lecteur ;
- il est contextuellement pertinent ;
- il pourrait exister même sans objectif SEO ;
- la relation entre les produits est transparente (pas de dissimulation d'affiliation).

Si une de ces conditions n'est pas remplie, ne pas recommander le lien — le signaler explicitement comme rejeté dans `opportunities.csv` avec la pénalité "réseau artificiel" (-50) si l'intention était principalement SEO.

## Outreach

Toute future fonction d'envoi automatique nécessitera une validation humaine explicite, prospect par prospect. Le skill ne dépasse jamais le stade du brouillon (`BROUILLON — NON ENVOYÉ`).

Interdits en outreach : prétendre avoir lu une page non consultée, inventer une relation, inventer une citation, inventer une statistique, proposer un échange de liens, proposer un paiement caché, utiliser une fausse urgence, rédiger un message trompeur.
