"""Tests for the contribution-file generator.

The generator module computes its input/output paths at import time from
``__file__``.  These tests import the module and redirect those module-level
path constants at a temporary directory so the pure generation logic can be
exercised without touching the real repository files.

These tests use only the standard-library ``unittest`` framework and can be
run with ``python3 -m unittest discover -s tests``.
"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"


def _load_generator():
    spec = importlib.util.spec_from_file_location(
        "generate_contributions", SCRIPTS_DIR / "generate_contributions.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _entry(area, repo, pr, title):
    return {
        "area": area,
        "repo": repo,
        "pr": pr,
        "title": title,
        "url": f"https://github.com/{repo}/pull/{pr}",
    }


class GenerateContributionsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.module = _load_generator()
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp_path = Path(self._tmp.name)
        data_dir = self.tmp_path / "data"
        data_dir.mkdir()

        self.module.ROOT = self.tmp_path
        self.module.DATA_FILE = data_dir / "selected_prs.json"
        self.module.README_FILE = self.tmp_path / "README.md"
        self.module.CONTRIBUTIONS_FILE = self.tmp_path / "contributions.md"
        self.module.HIGHLIGHTS_FILE = self.tmp_path / "highlights.json"
        self.module.MERGED_PRS_FILE = self.tmp_path / "merged_prs.json"

    def tearDown(self) -> None:
        self._tmp.cleanup()
        sys.modules.pop("generate_contributions", None)

    def test_generates_all_files_with_grouped_sections(self) -> None:
        entries = [
            _entry("SDKs", "octo/one", 1, "first fix"),
            _entry("SDKs", "octo/two", 2, "second fix"),
            _entry("Research", "uni/three", 3, "third fix"),
        ]
        self.module.DATA_FILE.write_text(json.dumps(entries))

        self.module.main()

        readme = (self.tmp_path / "README.md").read_text()
        contributions = (self.tmp_path / "contributions.md").read_text()
        highlights = json.loads((self.tmp_path / "highlights.json").read_text())

        # Areas become section headings and entries become markdown bullets.
        self.assertIn("### SDKs", readme)
        self.assertIn("### Research", readme)
        self.assertIn(
            "[octo/one #1](https://github.com/octo/one/pull/1): first fix", readme
        )
        self.assertIn("## SDKs", contributions)
        self.assertIn(
            "[uni/three #3](https://github.com/uni/three/pull/3): third fix",
            contributions,
        )

        # Highlights mirror the curated entries (capped at six).
        self.assertEqual(
            [h["repo"] for h in highlights["highlights"]],
            ["octo/one", "octo/two", "uni/three"],
        )

    def test_highlights_capped_at_six(self) -> None:
        entries = [_entry("SDKs", f"octo/repo{i}", i, f"fix {i}") for i in range(10)]
        self.module.DATA_FILE.write_text(json.dumps(entries))

        self.module.main()

        highlights = json.loads((self.tmp_path / "highlights.json").read_text())
        self.assertEqual(len(highlights["highlights"]), 6)
        self.assertEqual(
            [h["pr"] for h in highlights["highlights"]], [0, 1, 2, 3, 4, 5]
        )

    def test_recent_merged_prs_appended_when_present(self) -> None:
        self.module.DATA_FILE.write_text(
            json.dumps([_entry("SDKs", "octo/one", 1, "first fix")])
        )
        self.module.MERGED_PRS_FILE.write_text(
            json.dumps(
                {
                    "recent_merged_prs": [
                        {
                            "repo": "big/proj",
                            "number": 42,
                            "title": "merged thing",
                            "url": "https://github.com/big/proj/pull/42",
                        }
                    ]
                }
            )
        )

        self.module.main()

        contributions = (self.tmp_path / "contributions.md").read_text()
        self.assertIn("## Recent Merged PRs", contributions)
        self.assertIn(
            "[big/proj #42](https://github.com/big/proj/pull/42): merged thing",
            contributions,
        )

    def test_recent_merged_prs_section_absent_without_file(self) -> None:
        self.module.DATA_FILE.write_text(
            json.dumps([_entry("SDKs", "octo/one", 1, "first fix")])
        )

        self.module.main()

        contributions = (self.tmp_path / "contributions.md").read_text()
        self.assertNotIn("## Recent Merged PRs", contributions)

    def test_empty_merged_prs_list_omits_section(self) -> None:
        self.module.DATA_FILE.write_text(
            json.dumps([_entry("SDKs", "octo/one", 1, "first fix")])
        )
        self.module.MERGED_PRS_FILE.write_text(
            json.dumps({"recent_merged_prs": []})
        )

        self.module.main()

        contributions = (self.tmp_path / "contributions.md").read_text()
        self.assertNotIn("## Recent Merged PRs", contributions)

    def test_main_is_idempotent(self) -> None:
        self.module.DATA_FILE.write_text(
            json.dumps([_entry("SDKs", "octo/one", 1, "first fix")])
        )

        self.module.main()
        first = (
            (self.tmp_path / "README.md").read_text(),
            (self.tmp_path / "contributions.md").read_text(),
        )
        self.module.main()
        second = (
            (self.tmp_path / "README.md").read_text(),
            (self.tmp_path / "contributions.md").read_text(),
        )

        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
