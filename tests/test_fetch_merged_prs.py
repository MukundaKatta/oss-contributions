"""Tests for the merged-PR fetcher.

Network access is fully mocked: ``urlopen`` is replaced with a fake that
returns a canned GitHub search-API payload, so the response-parsing logic can
be verified deterministically and offline.
"""

from __future__ import annotations

import importlib.util
import io
import json
import sys
from pathlib import Path

import pytest


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"


def _load_fetcher():
    spec = importlib.util.spec_from_file_location(
        "fetch_merged_prs", SCRIPTS_DIR / "fetch_merged_prs.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def fetcher():
    module = _load_fetcher()
    yield module
    sys.modules.pop("fetch_merged_prs", None)


class _FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()
        return False


def test_requires_token(fetcher, monkeypatch):
    monkeypatch.delenv("GITHUB_TOKEN", raising=False)
    monkeypatch.delenv("GH_TOKEN", raising=False)

    with pytest.raises(RuntimeError, match="GITHUB_TOKEN or GH_TOKEN"):
        fetcher.fetch_recent_merged_prs()


def test_parses_search_items(fetcher, monkeypatch):
    monkeypatch.setenv("GITHUB_TOKEN", "fake-token")

    payload = {
        "items": [
            {
                "repository_url": "https://api.github.com/repos/octo/widget",
                "number": 7,
                "title": "fix the widget",
                "html_url": "https://github.com/octo/widget/pull/7",
                "updated_at": "2026-01-02T03:04:05Z",
            }
        ]
    }

    def fake_urlopen(request, timeout=None):  # noqa: ARG001 - signature parity
        assert timeout == fetcher.HTTP_TIMEOUT_SECONDS
        return _FakeResponse(json.dumps(payload).encode("utf-8"))

    monkeypatch.setattr(fetcher, "urlopen", fake_urlopen)

    result = fetcher.fetch_recent_merged_prs()

    assert result == [
        {
            "repo": "octo/widget",
            "number": 7,
            "title": "fix the widget",
            "url": "https://github.com/octo/widget/pull/7",
            "updated_at": "2026-01-02T03:04:05Z",
        }
    ]


def test_empty_items_returns_empty_list(fetcher, monkeypatch):
    monkeypatch.setenv("GH_TOKEN", "fake-token")

    def fake_urlopen(request, timeout=None):  # noqa: ARG001 - signature parity
        return _FakeResponse(json.dumps({"items": []}).encode("utf-8"))

    monkeypatch.setattr(fetcher, "urlopen", fake_urlopen)

    assert fetcher.fetch_recent_merged_prs() == []
