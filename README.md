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

