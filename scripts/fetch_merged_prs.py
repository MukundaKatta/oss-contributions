"""Fetch the most recently merged pull requests authored by the repo owner.

The script queries the GitHub search API for merged PRs and writes a compact
JSON summary to ``merged_prs.json`` so that :mod:`generate_contributions` can
fold the results into the human-readable contribution log.

A ``GITHUB_TOKEN`` (or ``GH_TOKEN``) environment variable is required; the
GitHub search API rejects unauthenticated requests for this query.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


HTTP_TIMEOUT_SECONDS = 30


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = ROOT / "merged_prs.json"
API_URL = "https://api.github.com/search/issues"


def _repo_full_name(repository_url: str) -> str:
    """Derive ``owner/name`` from a GitHub API ``repository_url``.

    Example: ``https://api.github.com/repos/octo/widget`` -> ``octo/widget``.
    """
    return "/".join(repository_url.rstrip("/").split("/")[-2:])


def fetch_recent_merged_prs() -> list[dict[str, Any]]:
    """Return a list of recently merged PRs authored by ``MukundaKatta``.

    Each entry is a dict with ``repo``, ``number``, ``title``, ``url`` and
    ``updated_at`` keys. Items missing the fields needed to build a useful
    contribution-log entry are skipped rather than raising, so a single
    malformed search result cannot break the whole sync.

    Raises:
        RuntimeError: if no auth token is configured or the API call fails.
    """
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        raise RuntimeError(
            "GITHUB_TOKEN or GH_TOKEN is required to fetch merged PR metadata."
        )

    query = "author:MukundaKatta is:pr is:merged sort:updated-desc"
    params = urlencode({"q": query, "per_page": 20})
    request = Request(f"{API_URL}?{params}")
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("Authorization", f"Bearer {token}")
    request.add_header("X-GitHub-Api-Version", "2022-11-28")

    try:
        with urlopen(request, timeout=HTTP_TIMEOUT_SECONDS) as response:  # noqa: S310
            payload = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        raise RuntimeError(
            f"GitHub search API returned HTTP {exc.code}: {exc.reason}"
        ) from exc
    except URLError as exc:
        raise RuntimeError(f"Failed to reach GitHub search API: {exc.reason}") from exc

    items: list[dict[str, Any]] = []
    for item in payload.get("items", []):
        repository_url = item.get("repository_url")
        number = item.get("number")
        html_url = item.get("html_url")
        if not repository_url or number is None or not html_url:
            # Skip malformed search results instead of raising KeyError.
            continue
        items.append(
            {
                "repo": _repo_full_name(repository_url),
                "number": number,
                "title": item.get("title", ""),
                "url": html_url,
                "updated_at": item.get("updated_at", ""),
            }
        )
    return items


def main() -> None:
    """Fetch merged PRs and write them to ``merged_prs.json``."""
    OUTPUT_FILE.write_text(
        json.dumps({"recent_merged_prs": fetch_recent_merged_prs()}, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
