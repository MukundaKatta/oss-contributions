from __future__ import annotations

import json
import os
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = ROOT / "merged_prs.json"
API_URL = "https://api.github.com/search/issues"


def fetch_recent_merged_prs() -> list[dict]:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN or GH_TOKEN is required to fetch merged PR metadata.")

    query = "author:MukundaKatta is:pr is:merged sort:updated-desc"
    params = urlencode({"q": query, "per_page": 20})
    request = Request(f"{API_URL}?{params}")
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("Authorization", f"Bearer {token}")
    request.add_header("X-GitHub-Api-Version", "2022-11-28")

    with urlopen(request) as response:  # noqa: S310
        payload = json.loads(response.read().decode("utf-8"))

    items = []
    for item in payload.get("items", []):
        repo = "/".join(item["repository_url"].split("/")[-2:])
        items.append(
            {
                "repo": repo,
                "number": item["number"],
                "title": item["title"],
                "url": item["html_url"],
                "updated_at": item["updated_at"],
            }
        )
    return items


def main() -> None:
    OUTPUT_FILE.write_text(json.dumps({"recent_merged_prs": fetch_recent_merged_prs()}, indent=2) + "\n")


if __name__ == "__main__":
    main()
