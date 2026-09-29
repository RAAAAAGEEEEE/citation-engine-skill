#!/usr/bin/env python3
"""Validate the files written by the skill against references/output-schemas.md.

Usage:
    python scripts/check_outputs.py <file-or-folder> [<file-or-folder> ...]

A folder is scanned for the standard names (state.json, project.json,
opportunities.csv, prospects.csv, assets/<slug>/sources.csv). A file is
classified by its name: it must contain "state", "project", "opportunities",
"prospects" or "sources".

Exit code: 0 = every file is valid, 1 = at least one problem, 2 = nothing to check.
Standard library only. Nothing is written and no network access is made.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

STATE_FIELDS = [
    "schema_version", "project", "repository_path", "canonical_url", "current_phase",
    "completed_phases", "pending_phases", "blockers", "selected_opportunity", "files_created",
    "opportunities_count", "rejected_opportunities_count", "prospects_count", "drafts_count",
    "started_at", "updated_at", "last_completed_at", "last_error", "next_action",
]
PROJECT_FIELDS = [
    "project_name", "canonical_url", "repository_path", "language", "countries",
    "product_category", "one_sentence_value_proposition", "target_audiences", "buyer_questions",
    "competitors", "proof_assets", "existing_statistics", "existing_integrations",
    "excluded_domains", "approval_required_for_outreach", "created_at", "updated_at",
]
PHASES = ["initialisation", "audit", "recherche_opportunites", "scoring_et_selection",
          "production_actif", "prospection", "outreach", "rapport"]
OPPORTUNITY_HEADERS = [
    "id", "type", "title", "source_url", "source_domain", "target_url", "competitor",
    "editorial_reason", "evidence", "relevance_score", "editorial_value_score",
    "probability_score", "authority_score", "ai_citation_score", "effort_score", "penalties",
    "total_score", "status", "verified_at", "notes",
]
PROSPECT_HEADERS = [
    "id", "domain", "source_url", "organization", "contact_name", "contact_role",
    "public_contact_url", "opportunity_type", "competitor_mentioned", "target_asset",
    "editorial_reason", "personalization_evidence", "score", "status", "verified_at", "notes",
]
SOURCE_HEADERS = [
    "id", "title", "url", "publisher", "author", "published_at", "accessed_at", "claim_used",
    "source_type", "confidence", "notes",
]
OPPORTUNITY_STATUS = {"candidate", "selected", "rejected", "archived"}
CONFIDENCE = {"high", "medium", "low"}
REJECT_BELOW = 40


def check_json(path: Path, fields: list[str], label: str) -> list[str]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"{path}: JSON illisible ({exc})"]
    if not isinstance(data, dict):
        return [f"{path}: un objet JSON est attendu"]
    problems = [f"{path}: champ obligatoire absent : {f}" for f in fields if f not in data]
    if label == "state":
        for key in ("completed_phases", "pending_phases"):
            for phase in data.get(key) or []:
                if phase not in PHASES:
                    problems.append(f"{path}: phase inconnue dans {key} : {phase}")
        both = set(data.get("completed_phases") or []) & set(data.get("pending_phases") or [])
        if both:
            problems.append(f"{path}: phase à la fois terminée et en attente : {sorted(both)}")
    return problems


def read_csv(path: Path, headers: list[str]) -> tuple[list[dict], list[str]]:
    try:
        with path.open(encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh)
            if reader.fieldnames != headers:
                return [], [f"{path}: en-têtes différents de ceux du schéma (attendu : {','.join(headers)})"]
            return list(reader), []
    except (OSError, UnicodeDecodeError, csv.Error) as exc:
        return [], [f"{path}: CSV illisible ({exc})"]


def to_int(value: str) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def check_opportunities(path: Path) -> list[str]:
    rows, problems = read_csv(path, OPPORTUNITY_HEADERS)
    seen: set[tuple] = set()
    for i, row in enumerate(rows, start=2):
        where = f"{path}:{i}"
        key = (row["type"], row["source_domain"], row["source_url"], row["target_url"])
        if key in seen:
            problems.append(f"{where}: doublon (type + domaine + URL source + URL cible)")
        seen.add(key)
        if row["status"] not in OPPORTUNITY_STATUS:
            problems.append(f"{where}: status invalide : {row['status']!r}")
        parts = [to_int(row[c]) for c in ("relevance_score", "editorial_value_score", "probability_score",
                                           "authority_score", "ai_citation_score", "effort_score", "penalties")]
        total = to_int(row["total_score"])
        if None in parts or total is None:
            problems.append(f"{where}: scores non numériques")
            continue
        if sum(parts) != total:
            problems.append(f"{where}: total_score {total} différent de la somme {sum(parts)}")
        if total < REJECT_BELOW and row["status"] != "rejected":
            problems.append(f"{where}: score {total} < {REJECT_BELOW} mais status = {row['status']}")
    return problems


def check_prospects(path: Path) -> list[str]:
    rows, problems = read_csv(path, PROSPECT_HEADERS)
    seen: set[tuple] = set()
    for i, row in enumerate(rows, start=2):
        key = (row["domain"], row["source_url"])
        if key in seen:
            problems.append(f"{path}:{i}: doublon (domaine + URL source)")
        seen.add(key)
        if not row["editorial_reason"].strip() or not row["personalization_evidence"].strip():
            problems.append(f"{path}:{i}: raison éditoriale ou preuve de personnalisation vide")
    return problems


def check_sources(path: Path) -> list[str]:
    rows, problems = read_csv(path, SOURCE_HEADERS)
    for i, row in enumerate(rows, start=2):
        if row["confidence"] not in CONFIDENCE:
            problems.append(f"{path}:{i}: confidence invalide : {row['confidence']!r}")
    return problems


def classify(path: Path) -> str | None:
    name = path.name.lower()
    for label in ("state", "project", "opportunities", "prospects", "sources"):
        if label in name:
            return label
    return None


def expand(target: Path) -> list[Path]:
    if not target.is_dir():
        return [target]
    found = [target / n for n in ("state.json", "project.json", "opportunities.csv", "prospects.csv")]
    found += sorted((target / "assets").glob("*/sources.csv")) if (target / "assets").is_dir() else []
    return [p for p in found if p.exists()]


def check(path: Path) -> list[str]:
    label = classify(path)
    if label is None:
        return [f"{path}: type de fichier non reconnu"]
    if not path.exists():
        return [f"{path}: fichier introuvable"]
    if label == "state":
        return check_json(path, STATE_FIELDS, "state")
    if label == "project":
        return check_json(path, PROJECT_FIELDS, "project")
    if label == "opportunities":
        return check_opportunities(path)
    if label == "prospects":
        return check_prospects(path)
    return check_sources(path)


def main(argv: list[str]) -> int:
    targets = [p for arg in argv for p in expand(Path(arg))]
    if not targets:
        print("Aucun fichier à vérifier.", file=sys.stderr)
        return 2
    bad = 0
    for path in targets:
        problems = check(path)
        print(f"{'FAIL' if problems else 'OK  '} {path}")
        for problem in problems:
            print(f"     {problem}")
        bad += bool(problems)
    print(f"{len(targets) - bad}/{len(targets)} fichier(s) valide(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
