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

- [vercel/next.js #92809](https://github.com/vercel/next.js/pull/92809): docs: add documentation for no-typos ESLint rule
- [open-telemetry/opentelemetry-python #5149](https://github.com/open-telemetry/opentelemetry-python/pull/5149): fix(ci): stabilize tracecontext job
- [googleapis/google-cloud-python #16808](https://github.com/googleapis/google-cloud-python/pull/16808): ci: add pylint presubmit on golden files (closes #16393)
- [getsentry/XcodeBuildMCP #350](https://github.com/getsentry/XcodeBuildMCP/pull/350): fix(device): stop suggesting unsupported --device-id
- [supabase/supabase-js #2269](https://github.com/supabase/supabase-js/pull/2269): docs(auth): surface global-scope warning on signOut JSDoc
- [cloudflare/cloudflare-docs #30210](https://github.com/cloudflare/cloudflare-docs/pull/30210): docs(wrangler/deprecations): 'wrangler deploy' -> 'wrangler publish' in publish deprecation section
- [unjs/unimport #529](https://github.com/unjs/unimport/pull/529): fix(toExports): dedupe duplicate identifiers for class/enum declarations
- [googleapis/python-genai #2345](https://github.com/googleapis/python-genai/pull/2345): fix(retry): retry on httpx.TimeoutException with HttpRetryOptions
- [apache/druid #19318](https://github.com/apache/druid/pull/19318): fix: correct typo in SeekableStreamIndexTaskRunner log message
- [fossasia/badgemagic-firmware #138](https://github.com/fossasia/badgemagic-firmware/pull/138): docs(readme): fix debugging-section typos (DEUBG, debuging)
- [Azure/Azure-Sentinel #14120](https://github.com/Azure/Azure-Sentinel/pull/14120): docs: fix three 'Microsoft' typos across playbook READMEs
- [mne-tools/mne-nirs #683](https://github.com/mne-tools/mne-nirs/pull/683): docs: swap red/green in Filter Neural Signal tutorial comment
- [PrefectHQ/fastmcp #4001](https://github.com/PrefectHQ/fastmcp/pull/4001): docs: add best practices for custom telemetry spans
- [dmachard/DNS-collector #1203](https://github.com/dmachard/DNS-collector/pull/1203): docs(afpacket): fix IP-defrag option name 'enable-fragment-support' -> 'enable-defrag-ip'
- [MukundaKatta/amogha-cafe #68](https://github.com/MukundaKatta/amogha-cafe/pull/68): fix(pos): screenOrientation fullSensor — rotate even when auto-rotate is OFF
- [MukundaKatta/amogha-cafe #67](https://github.com/MukundaKatta/amogha-cafe/pull/67): fix(pos): unlock screen orientation — was hard-locked to landscape
- [MukundaKatta/amogha-cafe #66](https://github.com/MukundaKatta/amogha-cafe/pull/66): ci: auto-fetch POS APK artifact before deploy so /pos-latest.apk survives
- [MukundaKatta/amogha-cafe #65](https://github.com/MukundaKatta/amogha-cafe/pull/65): hosting: serve .apk with Android MIME for on-device POS install
- [MukundaKatta/amogha-cafe #64](https://github.com/MukundaKatta/amogha-cafe/pull/64): fix(pos): granular login error messages + offline guard + 12s timeout
- [MukundaKatta/amogha-cafe #63](https://github.com/MukundaKatta/amogha-cafe/pull/63): fix(pos): native app Connection error — CORS didn't allow capacitor://
