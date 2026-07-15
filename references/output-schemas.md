# Schémas de sortie — SEO

Voir [SKILL.md](../SKILL.md) pour le résumé. Exemples complets dans [assets/](../assets/).

## state.json

Champs obligatoires :

- `schema_version`
- `project`
- `repository_path`
- `canonical_url`
- `current_phase`
- `completed_phases` (liste)
- `pending_phases` (liste)
- `blockers` (liste)
- `selected_opportunity` (objet ou null)
- `files_created` (liste)
- `opportunities_count`
- `rejected_opportunities_count`
- `prospects_count`
- `drafts_count`
- `started_at` (ISO 8601)
- `updated_at` (ISO 8601)
- `last_completed_at` (ISO 8601 ou null)
- `last_error` (string ou null)
- `next_action`

Exemple : [assets/state.example.json](../assets/state.example.json).

## project.json

Champs obligatoires :

- `project_name`
- `canonical_url`
- `repository_path`
- `language`
- `countries`
- `product_category`
- `one_sentence_value_proposition`
- `target_audiences`
- `buyer_questions`
- `competitors`
- `proof_assets`
- `existing_statistics`
- `existing_integrations`
- `excluded_domains`
- `approval_required_for_outreach`
- `created_at` (ISO 8601)
- `updated_at` (ISO 8601)

Valeur manquante non inventée : `null`, `[]`, ou `"[À VÉRIFIER : description précise de l'information manquante]"`.

Exemple : [assets/project.example.json](../assets/project.example.json).

## opportunities.csv

En-têtes fixes (ordre exact) :

```
id,type,title,source_url,source_domain,target_url,competitor,editorial_reason,evidence,relevance_score,editorial_value_score,probability_score,authority_score,ai_citation_score,effort_score,penalties,total_score,status,verified_at,notes
```

Déduplication par : type + source_domain + source_url + target_url.

`status` ∈ {`candidate`, `selected`, `rejected`, `archived`}. `verified_at` en ISO 8601.

Exemple : [assets/opportunities.example.csv](../assets/opportunities.example.csv).

## prospects.csv

En-têtes fixes (ordre exact) :

```
id,domain,source_url,organization,contact_name,contact_role,public_contact_url,opportunity_type,competitor_mentioned,target_asset,editorial_reason,personalization_evidence,score,status,verified_at,notes
```

Exclure les domaines listés dans `project.json.excluded_domains`. Ne jamais inventer `contact_name`, `contact_role` ou une adresse email — privilégier `public_contact_url`.

Exemple : [assets/prospects.example.csv](../assets/prospects.example.csv).

## sources.csv (par actif)

En-têtes fixes (ordre exact) :

```
id,title,url,publisher,author,published_at,accessed_at,claim_used,source_type,confidence,notes
```

`source_type` suit la hiérarchie de [source-quality.md](source-quality.md). `confidence` ∈ {`high`, `medium`, `low`}.

Exemple : [assets/sources.example.csv](../assets/sources.example.csv).

## Assets (`.citation-engine/assets/<slug>/`)

### BRIEF.md
Résumé de l'action P0 : type d'actif, objectif, audience cible, mots-clés/intentions visés, angle de citabilité, lien avec l'audit et le scoring.

### CONTENT.md
Selon le type d'actif, inclure au minimum les éléments applicables :
- title, meta description, URL slug proposée
- H1, structure H2/H3
- introduction, contenu principal, tableaux
- méthodologie, limites
- auteur ou organisation, date de publication proposée, date de mise à jour
- CTA
- plan de maillage interne
- JSON-LD pertinent si réellement applicable
- plan de maintenance, fréquence de mise à jour
- éléments visuels recommandés
- moyens de rendre la page facilement citable (résumé en tête, données structurées, chiffres clés isolés, ancre de citation)

Pour pages de statistiques/études/benchmarks/datasets : séparer explicitement données externes et données propriétaires ; méthodologie précise ; aucun chiffre inventé ; toute extrapolation signalée comme telle.

### sources.csv
Voir ci-dessus.

### implementation.md
Plan d'implémentation prêt à l'emploi : où publier, comment intégrer au maillage interne existant, prérequis techniques, checklist de mise en ligne. Ne modifie pas le code applicatif — c'est un plan, pas une exécution.

## outreach/<date-ISO>.md

Chaque brouillon contient : prospect visé, URL concernée, preuve de personnalisation, corps du message (≤120 mots par défaut), mention explicite `BROUILLON — NON ENVOYÉ`.

Gabarit : [assets/outreach-template.md](../assets/outreach-template.md).

## reports/<date-ISO>.md

Contenu obligatoire : projet, URL canonique, date, phase atteinte, action P0 sélectionnée et raison, fichiers créés, nombre d'opportunités (total et rejetées), nombre de prospects, nombre de brouillons, sources principales, limites, éléments à vérifier, blocages, prochaine action unique. Section de suivi distinguant backlinks gagnés, mentions sans lien, citations IA observées, trafic référent, impressions/clics Search Console, leads, conversions, revenus.

Gabarit : [assets/report-template.md](../assets/report-template.md).
