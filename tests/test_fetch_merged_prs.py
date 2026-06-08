"""Tests for the merged-PR fetcher.

Network access is fully mocked: ``urlopen`` is replaced with a fake that
returns a canned GitHub search-API payload, so the response-parsing logic can
be verified deterministically and offline.

These tests use only the standard-library ``unittest`` framework and can be
run with ``python3 -m unittest discover -s tests``.
"""

from __future__ import annotations

import importlib.util
import io
import json
import sys
import unittest
from pathlib import Path
from unittest import mock


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"


def _load_fetcher():
    spec = importlib.util.spec_from_file_location(
        "fetch_merged_prs", SCRIPTS_DIR / "fetch_merged_prs.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class _FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()
        return False


class FetchMergedPrsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.fetcher = _load_fetcher()
        # Ensure a clean, deterministic environment for token-related tests.
        self._env_patch = mock.patch.dict("os.environ", {}, clear=False)
        self._env_patch.start()

    def tearDown(self) -> None:
        self._env_patch.stop()
        sys.modules.pop("fetch_merged_prs", None)

    def _set_token(self, name: str = "GITHUB_TOKEN", value: str = "fake-token") -> None:
        import os

        os.environ.pop("GITHUB_TOKEN", None)
        os.environ.pop("GH_TOKEN", None)
        os.environ[name] = value

    def test_requires_token(self) -> None:
        import os

        os.environ.pop("GITHUB_TOKEN", None)
        os.environ.pop("GH_TOKEN", None)

        with self.assertRaisesRegex(RuntimeError, "GITHUB_TOKEN or GH_TOKEN"):
            self.fetcher.fetch_recent_merged_prs()

    def test_parses_search_items(self) -> None:
        self._set_token("GITHUB_TOKEN")

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

        def fake_urlopen(request, timeout=None):
            self.assertEqual(timeout, self.fetcher.HTTP_TIMEOUT_SECONDS)
            return _FakeResponse(json.dumps(payload).encode("utf-8"))

        with mock.patch.object(self.fetcher, "urlopen", fake_urlopen):
            result = self.fetcher.fetch_recent_merged_prs()

        self.assertEqual(
            result,
            [
                {
                    "repo": "octo/widget",
                    "number": 7,
                    "title": "fix the widget",
                    "url": "https://github.com/octo/widget/pull/7",
                    "updated_at": "2026-01-02T03:04:05Z",
                }
            ],
        )

    def test_gh_token_is_accepted(self) -> None:
        self._set_token("GH_TOKEN")

        def fake_urlopen(request, timeout=None):
            return _FakeResponse(json.dumps({"items": []}).encode("utf-8"))

        with mock.patch.object(self.fetcher, "urlopen", fake_urlopen):
            self.assertEqual(self.fetcher.fetch_recent_merged_prs(), [])

    def test_empty_items_returns_empty_list(self) -> None:
        self._set_token("GH_TOKEN")

        def fake_urlopen(request, timeout=None):
            return _FakeResponse(json.dumps({"items": []}).encode("utf-8"))

        with mock.patch.object(self.fetcher, "urlopen", fake_urlopen):
            self.assertEqual(self.fetcher.fetch_recent_merged_prs(), [])

    def test_malformed_items_are_skipped(self) -> None:
        """A search result missing required fields must not raise KeyError."""
        self._set_token("GITHUB_TOKEN")

        payload = {
            "items": [
                {"title": "no urls or number here"},  # malformed -> skipped
                {
                    "repository_url": "https://api.github.com/repos/octo/widget",
                    "number": 9,
                    "html_url": "https://github.com/octo/widget/pull/9",
                    # title and updated_at intentionally omitted
                },
            ]
        }

        def fake_urlopen(request, timeout=None):
            return _FakeResponse(json.dumps(payload).encode("utf-8"))

        with mock.patch.object(self.fetcher, "urlopen", fake_urlopen):
            result = self.fetcher.fetch_recent_merged_prs()

        self.assertEqual(
            result,
            [
                {
                    "repo": "octo/widget",
                    "number": 9,
                    "title": "",
                    "url": "https://github.com/octo/widget/pull/9",
                    "updated_at": "",
                }
            ],
        )

    def test_repo_full_name_helper(self) -> None:
        self.assertEqual(
            self.fetcher._repo_full_name(
                "https://api.github.com/repos/octo/widget"
            ),
            "octo/widget",
        )
        # Trailing slash should not produce an empty trailing segment.
        self.assertEqual(
            self.fetcher._repo_full_name(
                "https://api.github.com/repos/octo/widget/"
            ),
            "octo/widget",
        )

    def test_http_error_is_wrapped(self) -> None:
        self._set_token("GITHUB_TOKEN")

        def fake_urlopen(request, timeout=None):
            raise self.fetcher.HTTPError(
                url="https://api.github.com",
                code=403,
                msg="rate limited",
                hdrs=None,
                fp=io.BytesIO(b""),
            )

        with mock.patch.object(self.fetcher, "urlopen", fake_urlopen):
            with self.assertRaisesRegex(RuntimeError, "HTTP 403") as ctx:
                self.fetcher.fetch_recent_merged_prs()

        # The wrapping RuntimeError chains the original HTTPError; close its
        # response body so it does not emit a spurious ResourceWarning on GC.
        cause = ctx.exception.__cause__
        if cause is not None:
            cause.close()


if __name__ == "__main__":
    unittest.main()
