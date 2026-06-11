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

- [MukundaKatta/amogha-cafe #106](https://github.com/MukundaKatta/amogha-cafe/pull/106): ci(ios): set up Ruby before build step so cap sync's pod install finds gems
- [MukundaKatta/amogha-cafe #105](https://github.com/MukundaKatta/amogha-cafe/pull/105): ci(ios): commit ios/App/Gemfile.lock to unblock TestFlight build
- [MukundaKatta/amogha-cafe #104](https://github.com/MukundaKatta/amogha-cafe/pull/104): ci: bump release-ios and release-android to Node 22 (fixes TestFlight build)
- [MukundaKatta/amogha-cafe #103](https://github.com/MukundaKatta/amogha-cafe/pull/103): test: fix CI auth-test flake (crypto.subtle.digest races fake timers)
- [MukundaKatta/amogha-cafe #102](https://github.com/MukundaKatta/amogha-cafe/pull/102): Add in-app account deletion link (Apple 5.1.1(v))
- [MukundaKatta/amogha-cafe #69](https://github.com/MukundaKatta/amogha-cafe/pull/69): fix(pos): silence "No printer name configured" toast on every bill print
- [MukundaKatta/amogha-cafe #82](https://github.com/MukundaKatta/amogha-cafe/pull/82): fix(security): escape menu names in combo selector + meal plan (missed by #77)
- [MukundaKatta/amogha-cafe #81](https://github.com/MukundaKatta/amogha-cafe/pull/81): ux(pwa): add apple-touch-icon to qr/track/loyalty + preconnect to loyalty
- [MukundaKatta/amogha-cafe #80](https://github.com/MukundaKatta/amogha-cafe/pull/80): sec: add rel='noopener noreferrer' to all target=_blank links (reverse tabnabbing)
- [MukundaKatta/amogha-cafe #79](https://github.com/MukundaKatta/amogha-cafe/pull/79): ux(a11y): add inputmode=numeric to all 10-digit phone inputs
- [MukundaKatta/amogha-cafe #71](https://github.com/MukundaKatta/amogha-cafe/pull/71): fix(kitchen): show orders placed after IST midnight on KOT board
- [MukundaKatta/amogha-cafe #70](https://github.com/MukundaKatta/amogha-cafe/pull/70): fix(security): escape menu item names in cart/qr/kiosk to close XSS holes
- [MukundaKatta/amogha-cafe #84](https://github.com/MukundaKatta/amogha-cafe/pull/84): Fix session-clear bug in setCurrentUser + add test CI workflow
- [MukundaKatta/amogha-cafe #83](https://github.com/MukundaKatta/amogha-cafe/pull/83): chore: repo hardening round 2 (Dependabot config)
- [AcademySoftwareFoundation/OpenCue #2330](https://github.com/AcademySoftwareFoundation/OpenCue/pull/2330): [cueweb] Add frame state filter chips
- [AcademySoftwareFoundation/OpenCue #2331](https://github.com/AcademySoftwareFoundation/OpenCue/pull/2331): [cueweb] Add job progress tooltip
- [openclaw/openclaw #87933](https://github.com/openclaw/openclaw/pull/87933): fix(agents): suppress DeepSeek thinking for Foundry aliases
- [modelcontextprotocol/csharp-sdk #1531](https://github.com/modelcontextprotocol/csharp-sdk/pull/1531): perf(server): skip IdleTrackingBackgroundService timer in stateless mode
- [public-apis/public-apis #6087](https://github.com/public-apis/public-apis/pull/6087): Remove defunct API entries
- [PostHog/code #2340](https://github.com/PostHog/code/pull/2340): feat(worktree): use human-readable names for worktree branches
