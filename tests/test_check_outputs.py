"""Tests for scripts/check_outputs.py (offline, standard library only)."""
import contextlib
import csv
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import check_outputs  # noqa: E402

ASSETS = ROOT / "assets"


def run(*paths):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = check_outputs.main([str(p) for p in paths])
    return code, out.getvalue()


class ExamplesAreValid(unittest.TestCase):
    def test_all_shipped_examples_pass(self):
        code, out = run(ASSETS / "state.example.json", ASSETS / "project.example.json",
                        ASSETS / "opportunities.example.csv", ASSETS / "prospects.example.csv",
                        ASSETS / "sources.example.csv")
        self.assertEqual(code, 0, out)
        self.assertIn("5/5 fichier(s) valide(s)", out)


class EvalsAreWellFormed(unittest.TestCase):
    def test_evals_follow_the_skill_creator_schema(self):
        data = json.loads((ROOT / "evals" / "evals.json").read_text(encoding="utf-8"))
        self.assertEqual(data["skill_name"], "seo")
        ids = [e["id"] for e in data["evals"]]
        self.assertEqual(ids, sorted(set(ids)))
        self.assertGreaterEqual(len(ids), 3)
        for e in data["evals"]:
            self.assertTrue(e["prompt"].strip() and e["expected_output"].strip() and e["expectations"])
            for f in e["files"]:
                self.assertTrue((ROOT / f).is_file(), f)

    def test_frontmatter_declares_the_portable_fields(self):
        head = (ROOT / "SKILL.md").read_text(encoding="utf-8").split("---")[1]
        for field in ("name: seo", "description:", "license: MIT", "compatibility:", "metadata:", "  version:"):
            self.assertIn(field, head)


class DetectsProblems(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def test_missing_state_field(self):
        data = json.loads((ASSETS / "state.example.json").read_text(encoding="utf-8"))
        del data["next_action"]
        p = self.tmp / "state.json"
        p.write_text(json.dumps(data), encoding="utf-8")
        code, out = run(p)
        self.assertEqual(code, 1)
        self.assertIn("next_action", out)

    def test_low_score_must_be_rejected(self):
        with (ASSETS / "opportunities.example.csv").open(encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh))
        rows[2]["status"] = "candidate"  # opp-003 has a final score below 40
        p = self.tmp / "opportunities.csv"
        with p.open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=check_outputs.OPPORTUNITY_HEADERS)
            w.writeheader()
            w.writerows(rows)
        code, out = run(p)
        self.assertEqual(code, 1)
        self.assertIn("< 40", out)

    def test_wrong_headers(self):
        p = self.tmp / "sources.csv"
        p.write_text("id,url\n1,https://example.com\n", encoding="utf-8")
        code, out = run(p)
        self.assertEqual(code, 1)
        self.assertIn("en-têtes", out)

    def test_folder_scan_and_nothing_to_check(self):
        code, _ = run(self.tmp)
        self.assertEqual(code, 2)
        shutil.copy(ASSETS / "state.example.json", self.tmp / "state.json")
        code, out = run(self.tmp)
        self.assertEqual(code, 0, out)


if __name__ == "__main__":
    unittest.main()
