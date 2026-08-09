"""Regenerate the human-readable contribution files from curated data.

``data/selected_prs.json`` is the curated source of truth for featured
contributions. This module groups those entries by ``area`` and renders:

* ``README.md`` — the "Selected Contributions" section, from a template.
* ``contributions.md`` — the full contribution log, optionally appended with
  the recently merged PRs produced by :mod:`fetch_merged_prs`.
* ``highlights.json`` — the first six curated entries, for downstream embeds.

The generator is deterministic and idempotent: running it twice against the
same inputs produces byte-identical output.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "selected_prs.json"
README_FILE = ROOT / "README.md"
CONTRIBUTIONS_FILE = ROOT / "contributions.md"
HIGHLIGHTS_FILE = ROOT / "highlights.json"
MERGED_PRS_FILE = ROOT / "merged_prs.json"


README_TEMPLATE = """# OSS Contributions

A public hub for my open-source work across AI SDKs, MCP tooling, eval frameworks, agent infrastructure, and developer-experience improvements.

## Snapshot

- Focus: AI SDKs, MCP, evals, agents, and DX
- Style: small, practical, mergeable contributions
- Typical fixes: docs clarity, typed SDK fixes, developer workflow cleanup, agent-tooling improvements

## Why This Repo Exists

Most of my contributions are small, practical fixes spread across many repositories. This repo makes that work easier to browse by showing:

- where I contribute
- what kinds of problems I usually fix
- selected PRs with real-world developer impact
- the open-source niche I am intentionally building around

## Core Themes

- AI SDKs and typed developer tooling
- Model Context Protocol integrations
- eval and benchmark infrastructure
- agent tooling
- docs and DX fixes that unblock users fast

## Selected Contributions

{selected_sections}

## Contribution Log

See [contributions.md](./contributions.md) for a running list of selected PRs.

## Repository Layout

| Path | Purpose |
| --- | --- |
| `data/selected_prs.json` | Curated source of truth for featured contributions (hand-edited). |
| `scripts/fetch_merged_prs.py` | Calls the GitHub search API and writes `merged_prs.json`. |
| `scripts/generate_contributions.py` | Renders `README.md`, `contributions.md`, and `highlights.json`. |
| `merged_prs.json` | Generated: the most recent merged PRs authored upstream. |
| `highlights.json` | Generated: the first six curated entries, for downstream embeds. |
| `tests/` | Standard-library `unittest` tests for both scripts. |

## How It Works

`data/selected_prs.json` is the only file edited by hand. Each entry groups under
an `area` and the generator turns those groups into the **Selected Contributions**
section above and the full log in `contributions.md`. If a `merged_prs.json` file
is present, its entries are appended to `contributions.md` under
**Recent Merged PRs**. The generator is deterministic and idempotent, so running
it twice produces identical output.

### Data Schema

Each object in `data/selected_prs.json` has the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `area` | string | Section heading the entry is grouped under. |
| `repo` | string | `owner/name` of the upstream repository. |
| `pr` | integer | Pull-request number. |
| `title` | string | Short description of the contribution. |
| `url` | string | Link to the merged pull request. |

## Running Locally

No third-party dependencies are required to regenerate the contribution files:

```bash
# Optional: refresh the recent merged-PR log (needs a GitHub token).
GITHUB_TOKEN=ghp_... python3 scripts/fetch_merged_prs.py

# Always safe to run; rewrites README.md, contributions.md, highlights.json.
python3 scripts/generate_contributions.py
```

`fetch_merged_prs.py` requires `GITHUB_TOKEN` (or `GH_TOKEN`); the GitHub search
API rejects the query when unauthenticated.

## Tests

The test suite uses only the Python standard library (`unittest`) and needs no
installs:

```bash
python3 -m unittest discover -s tests -v
```

## Connect

- GitHub: https://github.com/MukundaKatta
- LinkedIn: https://www.linkedin.com/in/mukunda-katta-728155220/
- X: https://x.com/katta_mukunda
"""


def main() -> None:
    """Read the curated data and (re)write all generated contribution files."""
    entries = json.loads(DATA_FILE.read_text())
    by_area: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        by_area[entry["area"]].append(entry)

    section_lines: list[str] = []
    contribution_lines = [
        "# Contribution Log",
        "",
        "Curated PR log generated from `data/selected_prs.json`.",
        "",
    ]
    highlights = []

    for area, area_entries in by_area.items():
        section_lines.append(f"### {area}")
        section_lines.append("")
        contribution_lines.append(f"## {area}")
        contribution_lines.append("")
        for entry in area_entries:
            label = f"{entry['repo']} #{entry['pr']}"
            bullet = f"- [{label}]({entry['url']}): {entry['title']}"
            section_lines.append(bullet)
            contribution_lines.append(bullet)
        section_lines.append("")
        contribution_lines.append("")

    for entry in entries[:6]:
        highlights.append(
            {
                "repo": entry["repo"],
                "pr": entry["pr"],
                "title": entry["title"],
                "url": entry["url"],
            }
        )

    if MERGED_PRS_FILE.exists():
        merged = json.loads(MERGED_PRS_FILE.read_text()).get("recent_merged_prs", [])
        if merged:
            contribution_lines.extend(["## Recent Merged PRs", ""])
            for entry in merged:
                contribution_lines.append(
                    f"- [{entry['repo']} #{entry['number']}]({entry['url']}): {entry['title']}"
                )
            contribution_lines.append("")

    README_FILE.write_text(
        README_TEMPLATE.format(selected_sections="\n".join(section_lines).rstrip())
        + "\n"
    )
    CONTRIBUTIONS_FILE.write_text("\n".join(contribution_lines).rstrip() + "\n")
    HIGHLIGHTS_FILE.write_text(json.dumps({"highlights": highlights}, indent=2) + "\n")


if __name__ == "__main__":
    main()
