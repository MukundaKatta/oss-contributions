# OSS Contributions

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

### AI SDKs and Tooling

- [openai/openai-node #1831](https://github.com/openai/openai-node/pull/1831): improved fallback handling for non-standard JSON error bodies
- [openai/tiktoken #529](https://github.com/openai/tiktoken/pull/529): added PyInstaller hooks for dynamic encoding plugins
- [googleapis/python-genai #2298](https://github.com/googleapis/python-genai/pull/2298): clarified response_schema vs response_json_schema
- [microsoft/playwright-mcp #1562](https://github.com/microsoft/playwright-mcp/pull/1562): clarified extension connection and tab-selection flow
- [anthropics/anthropic-sdk-python #1412](https://github.com/anthropics/anthropic-sdk-python/pull/1412): fixed async memory tool example docs

### Research / University Ecosystem

- [stanford-crfm/helm #4210](https://github.com/stanford-crfm/helm/pull/4210): fixed later-page deep links for run instances

### Personal Repos Improved In Public

- [MukundaKatta/MCPForge #4](https://github.com/MukundaKatta/MCPForge/pull/4): added the first MCPForge CLI scaffold and smoke-test flow
- [MukundaKatta/agentmem #4](https://github.com/MukundaKatta/agentmem/pull/4): added a SQLite backend plus tests and CI
- [MukundaKatta/TokenWise #4](https://github.com/MukundaKatta/TokenWise/pull/4): added pricing catalog versioning and budget tracking
- [MukundaKatta/AgentBench #4](https://github.com/MukundaKatta/AgentBench/pull/4): added async evaluation support and run artifacts
- [MukundaKatta/rnht #79](https://github.com/MukundaKatta/rnht/pull/79): added local setup validation and admin approval workflow
- [MukundaKatta/AgentRAG #4](https://github.com/MukundaKatta/AgentRAG/pull/4): scaffolded the core RAG interfaces and in-memory reference pipeline

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

