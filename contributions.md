# Contribution Log

Curated PR log generated from `data/selected_prs.json`.

## AI SDKs and Tooling

- [openai/openai-node #1831](https://github.com/openai/openai-node/pull/1831): improved fallback handling for non-standard JSON error bodies
- [openai/tiktoken #529](https://github.com/openai/tiktoken/pull/529): added PyInstaller hooks for dynamic encoding plugins
- [googleapis/python-genai #2298](https://github.com/googleapis/python-genai/pull/2298): clarified response_schema vs response_json_schema
- [microsoft/playwright-mcp #1562](https://github.com/microsoft/playwright-mcp/pull/1562): clarified extension connection and tab-selection flow
- [anthropics/anthropic-sdk-python #1412](https://github.com/anthropics/anthropic-sdk-python/pull/1412): fixed async memory tool example docs

## Research / University Ecosystem

- [stanford-crfm/helm #4210](https://github.com/stanford-crfm/helm/pull/4210): fixed later-page deep links for run instances

## Personal Repos Improved In Public

- [MukundaKatta/MCPForge #4](https://github.com/MukundaKatta/MCPForge/pull/4): added the first MCPForge CLI scaffold and smoke-test flow
- [MukundaKatta/agentmem #4](https://github.com/MukundaKatta/agentmem/pull/4): added a SQLite backend plus tests and CI
- [MukundaKatta/TokenWise #4](https://github.com/MukundaKatta/TokenWise/pull/4): added pricing catalog versioning and budget tracking
- [MukundaKatta/AgentBench #4](https://github.com/MukundaKatta/AgentBench/pull/4): added async evaluation support and run artifacts
- [MukundaKatta/rnht #79](https://github.com/MukundaKatta/rnht/pull/79): added local setup validation and admin approval workflow
- [MukundaKatta/AgentRAG #4](https://github.com/MukundaKatta/AgentRAG/pull/4): scaffolded the core RAG interfaces and in-memory reference pipeline

## Recent Merged PRs

- [openclaw/openclaw #87933](https://github.com/openclaw/openclaw/pull/87933): fix(agents): suppress DeepSeek thinking for Foundry aliases
- [modelcontextprotocol/csharp-sdk #1531](https://github.com/modelcontextprotocol/csharp-sdk/pull/1531): perf(server): skip IdleTrackingBackgroundService timer in stateless mode
- [public-apis/public-apis #6087](https://github.com/public-apis/public-apis/pull/6087): Remove defunct API entries
- [PostHog/code #2340](https://github.com/PostHog/code/pull/2340): feat(worktree): use human-readable names for worktree branches
- [PostHog/code #2339](https://github.com/PostHog/code/pull/2339): fix(agent): show server name and exec context in MCP permission dialog
- [MukundaKatta/artigen #984](https://github.com/MukundaKatta/artigen/pull/984): test: useDebounce / useResponsive / useNetworkStatus tests
- [elastic/beats #50279](https://github.com/elastic/beats/pull/50279): fix: clear typos 'defauling' -> 'defaulting' and 'choosen' -> 'chosen'
- [openclaw/openclaw #87965](https://github.com/openclaw/openclaw/pull/87965): fix(whatsapp): restart channel when a per-account config field changes so disabled accounts are torn down
- [MukundaKatta/amogha-cafe #78](https://github.com/MukundaKatta/amogha-cafe/pull/78): cleanup: delete root-level /modules/ — 15k lines of dead code that nothing loads
- [MukundaKatta/amogha-cafe #77](https://github.com/MukundaKatta/amogha-cafe/pull/77): fix: port PR #72 (PIN strip) + PR #74 group.js fix to src/modules — the REAL production code
- [MukundaKatta/amogha-cafe #76](https://github.com/MukundaKatta/amogha-cafe/pull/76): sec(hosting): drop 'unsafe-eval' from CSP, add HSTS + frame-ancestors + upgrade-insecure-requests
- [MukundaKatta/amogha-cafe #75](https://github.com/MukundaKatta/amogha-cafe/pull/75): perf(functions): persist /order rate-limit state in Firestore (was bypassable on cold start)
- [MukundaKatta/amogha-cafe #73](https://github.com/MukundaKatta/amogha-cafe/pull/73): feat(admin): gate admin writes behind Firebase Auth custom claim
- [MukundaKatta/artigen #476](https://github.com/MukundaKatta/artigen/pull/476): test: useHaptics web/native dispatch (+7 tests)
- [MukundaKatta/artigen #475](https://github.com/MukundaKatta/artigen/pull/475): fix: 5 small bounded bug + tech-debt fixes
- [MukundaKatta/artigen #473](https://github.com/MukundaKatta/artigen/pull/473): test: render tests for 3 auth screens (+11 tests)
- [MukundaKatta/artigen #471](https://github.com/MukundaKatta/artigen/pull/471): test: render tests for 5 more components (+32 tests)
- [MukundaKatta/artigen #469](https://github.com/MukundaKatta/artigen/pull/469): perf: migrate 5 high-traffic FlatLists to FlashList
- [MukundaKatta/artigen #468](https://github.com/MukundaKatta/artigen/pull/468): test: component render tests for 6 components + RNTL setup
- [MukundaKatta/artigen #467](https://github.com/MukundaKatta/artigen/pull/467): a11y: critique-composer textarea label + hint + live char-count
