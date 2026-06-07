"""Tests for the contribution-file generator.

The generator module computes its input/output paths at import time from
``__file__``.  These tests import the module and redirect those module-level
path constants at a temporary directory so the pure generation logic can be
exercised without touching the real repository files.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"


def _load_generator():
    spec = importlib.util.spec_from_file_location(
        "generate_contributions", SCRIPTS_DIR / "generate_contributions.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def generator(tmp_path, monkeypatch):
    module = _load_generator()
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(module, "DATA_FILE", data_dir / "selected_prs.json")
    monkeypatch.setattr(module, "README_FILE", tmp_path / "README.md")
    monkeypatch.setattr(module, "CONTRIBUTIONS_FILE", tmp_path / "contributions.md")
    monkeypatch.setattr(module, "HIGHLIGHTS_FILE", tmp_path / "highlights.json")
    monkeypatch.setattr(module, "MERGED_PRS_FILE", tmp_path / "merged_prs.json")
    return module


def _entry(area, repo, pr, title):
    return {
        "area": area,
        "repo": repo,
        "pr": pr,
        "title": title,
        "url": f"https://github.com/{repo}/pull/{pr}",
    }


def test_generates_all_files_with_grouped_sections(generator, tmp_path):
    entries = [
        _entry("SDKs", "octo/one", 1, "first fix"),
        _entry("SDKs", "octo/two", 2, "second fix"),
        _entry("Research", "uni/three", 3, "third fix"),
    ]
    generator.DATA_FILE.write_text(json.dumps(entries))

    generator.main()

    readme = (tmp_path / "README.md").read_text()
    contributions = (tmp_path / "contributions.md").read_text()
    highlights = json.loads((tmp_path / "highlights.json").read_text())

    # Areas become section headings and entries become markdown bullets.
    assert "### SDKs" in readme
    assert "### Research" in readme
    assert "[octo/one #1](https://github.com/octo/one/pull/1): first fix" in readme
    assert "## SDKs" in contributions
    assert (
        "[uni/three #3](https://github.com/uni/three/pull/3): third fix"
        in contributions
    )

    # Highlights mirror the curated entries (capped at six).
    assert [h["repo"] for h in highlights["highlights"]] == [
        "octo/one",
        "octo/two",
        "uni/three",
    ]


def test_highlights_capped_at_six(generator, tmp_path):
    entries = [_entry("SDKs", f"octo/repo{i}", i, f"fix {i}") for i in range(10)]
    generator.DATA_FILE.write_text(json.dumps(entries))

    generator.main()

    highlights = json.loads((tmp_path / "highlights.json").read_text())
    assert len(highlights["highlights"]) == 6
    assert [h["pr"] for h in highlights["highlights"]] == [0, 1, 2, 3, 4, 5]


def test_recent_merged_prs_appended_when_present(generator, tmp_path):
    generator.DATA_FILE.write_text(
        json.dumps([_entry("SDKs", "octo/one", 1, "first fix")])
    )
    generator.MERGED_PRS_FILE.write_text(
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

    generator.main()

    contributions = (tmp_path / "contributions.md").read_text()
    assert "## Recent Merged PRs" in contributions
    assert (
        "[big/proj #42](https://github.com/big/proj/pull/42): merged thing"
        in contributions
    )


def test_recent_merged_prs_section_absent_without_file(generator, tmp_path):
    generator.DATA_FILE.write_text(
        json.dumps([_entry("SDKs", "octo/one", 1, "first fix")])
    )

    generator.main()

    contributions = (tmp_path / "contributions.md").read_text()
    assert "## Recent Merged PRs" not in contributions


def test_main_is_idempotent(generator, tmp_path):
    generator.DATA_FILE.write_text(
        json.dumps([_entry("SDKs", "octo/one", 1, "first fix")])
    )

    generator.main()
    first = (
        (tmp_path / "README.md").read_text(),
        (tmp_path / "contributions.md").read_text(),
    )
    generator.main()
    second = (
        (tmp_path / "README.md").read_text(),
        (tmp_path / "contributions.md").read_text(),
    )

    assert first == second


@pytest.fixture(autouse=True)
def _cleanup_module():
    yield
    sys.modules.pop("generate_contributions", None)
