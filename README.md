# SEO

Moteur SEO/GEO/digital PR autonome pour solopreneur gérant plusieurs SaaS. Améliore la visibilité Google Search, l'éligibilité aux AI Overviews/AI Mode, les citations dans Gemini/ChatGPT/Perplexity, les mentions éditoriales et backlinks pertinents, et la présence dans les comparatifs/listicles — sans fabrique à backlinks, sans spam, sans réseau artificiel entre projets.

**Emplacement absolu :** `~/.claude/skills/SEO/`

## Lancer le skill

Depuis n'importe quel dépôt de SaaS, dans Claude Code :

```
/SEO
```

1. Ouvrir Claude Code dans le dépôt du SaaS.
2. Lancer `/SEO`.
3. Répondre uniquement si des informations bloquantes sont demandées (3 questions maximum).
4. Laisser le skill dérouler les 8 phases automatiquement.
5. Relancer `/SEO` après toute interruption — il reprend à la première phase incomplète.

Une seule commande existe. Il n'y a pas de sous-commandes (`audit`, `plan`, `prospects`, etc.) — le skill détermine seul la phase suivante à partir de `.citation-engine/state.json`.

## Où sont enregistrés les résultats

Dans le dépôt courant, sous `.citation-engine/` :

- `state.json` — état d'avancement, reprise
- `project.json` — fiche projet
- `audit.md` — audit SEO/GEO
- `opportunities.csv` — opportunités scorées
- `prospects.csv` — prospects qualifiés
- `assets/<slug>/` — actif citable produit (brief, contenu, sources, plan d'implémentation)
- `outreach/<date>.md` — brouillons d'outreach
- `reports/<date>.md` — rapports de synthèse

## Ce que le skill ne fait jamais automatiquement

- envoyer un email, un message ou un formulaire ;
- publier du contenu en ligne ;
- modifier le code applicatif du dépôt ;
- créer un commit Git ;
- acheter un lien ou proposer un échange de liens ;
- inventer une statistique, une citation, un contact ou une identité ;
- garantir un résultat SEO, un backlink ou une citation IA.

Voir [references/policies.md](references/policies.md) pour le détail des garde-fous.

## Réinitialiser un projet

Ne jamais supprimer `.citation-engine/state.json` directement. À la place :

1. sauvegarder le fichier (copie) ;
2. le renommer, par exemple `state.json.bak-<date>` ;
3. relancer `/SEO`, qui initialisera un nouveau workflow.

Les autres fichiers (`audit.md`, `opportunities.csv`, etc.) sont fusionnés avec les données existantes lors des prochains lancements, pas écrasés.

## Références

Voir [SKILL.md](SKILL.md) pour le détail des 8 phases, du scoring, des schémas de sortie et des politiques appliquées.
