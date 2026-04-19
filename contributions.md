# Contribution Log

Use this file to keep a simple running list of notable contributions.

## Suggested Entry Format

```md
### YYYY-MM-DD — repo/name#123

- Type: docs | fix | tests | DX
- Summary: one-line summary
- Why it mattered: one-line impact
- Link: PR URL
```

## Recent Entries

### 2026-04-19 — stanford-crfm/helm#4210

- Type: fix, test
- Summary: fixed deep-link pagination behavior for instance pages
- Why it mattered: later-page instance links now open on the correct page
- Link: https://github.com/stanford-crfm/helm/pull/4210

### 2026-04-19 — googleapis/python-genai#2298

- Type: docs
- Summary: clarified when to use `response_schema` vs `response_json_schema`
- Why it mattered: reduces structured-output documentation confusion
- Link: https://github.com/googleapis/python-genai/pull/2298

### 2026-04-19 — microsoft/playwright-mcp#1562

- Type: docs
- Summary: clarified the initial extension connection flow and tab-selection behavior
- Why it mattered: reduces confusion around `--extension` and `browser_tabs`
- Link: https://github.com/microsoft/playwright-mcp/pull/1562

### 2026-04-19 — openai/tiktoken#529

- Type: build
- Summary: added PyInstaller hooks for dynamic encoding plugins
- Why it mattered: improves bundling support for real-world apps
- Link: https://github.com/openai/tiktoken/pull/529

### 2026-04-19 — openai/openai-node#1831

- Type: fix
- Summary: added fallback handling for top-level JSON error bodies
- Why it mattered: better compatibility and better error messages for OpenAI-compatible APIs
- Link: https://github.com/openai/openai-node/pull/1831
