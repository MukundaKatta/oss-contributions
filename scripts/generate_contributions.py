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

## Automation

This repo now treats `data/selected_prs.json` as the curated source of truth for featured contributions, and `merged_prs.json` as the generated source for the recent merged PR log. Run:

```bash
python3 scripts/fetch_merged_prs.py   # requires GITHUB_TOKEN
python3 scripts/generate_contributions.py
```

to refresh `README.md`, `contributions.md`, `highlights.json`, and `merged_prs.json`.

## Connect

- GitHub: https://github.com/MukundaKatta
- LinkedIn: https://www.linkedin.com/in/mukunda-katta-728155220/
- X: https://x.com/katta_mukunda
"""


def main() -> None:
    entries = json.loads(DATA_FILE.read_text())
    by_area: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        by_area[entry["area"]].append(entry)

    section_lines: list[str] = []
    contribution_lines = ["# Contribution Log", "", "Curated PR log generated from `data/selected_prs.json`.", ""]
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

    recent_lines: list[str] = []
    if MERGED_PRS_FILE.exists():
        merged = json.loads(MERGED_PRS_FILE.read_text()).get("recent_merged_prs", [])
        if merged:
            contribution_lines.extend(["## Recent Merged PRs", ""])
            for entry in merged:
                contribution_lines.append(
                    f"- [{entry['repo']} #{entry['number']}]({entry['url']}): {entry['title']}"
                )
            contribution_lines.append("")
            recent_lines = [
                "## Recent Merged PRs",
                "",
                "The contribution log below is refreshed from recent merged PR metadata when the sync workflow runs.",
                "",
            ]

    README_FILE.write_text(README_TEMPLATE.format(selected_sections="\n".join(section_lines).rstrip()) + "\n")
    CONTRIBUTIONS_FILE.write_text("\n".join(contribution_lines).rstrip() + "\n")
    HIGHLIGHTS_FILE.write_text(json.dumps({"highlights": highlights}, indent=2) + "\n")


if __name__ == "__main__":
    main()
