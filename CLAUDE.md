# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Google Ads MCP Server — a Python MCP (Model Context Protocol) server providing 40+ tools for Google Ads API v21 campaign automation. All tools are fully implemented (not stubs).

## Commands

```bash
# Install (dev mode with dev dependencies)
pip install -e ".[dev]"

# Run the server
python run_server.py

# Run with debug logging
LOG_LEVEL=DEBUG python run_server.py

# Tests
pytest tests/
pytest tests/test_campaigns.py          # single test file

# Formatting, linting, type checking
black src/
ruff check src/
mypy src/
```

## Architecture

The server is a layered system: MCP protocol handling → tool dispatch → specialized tool modules → Google Ads API client.

**Entry points:** `run_server.py` calls `src/__main__.py` which starts the MCP server defined in `src/server.py`.

**Core flow:** `server.py` receives MCP tool calls → dispatches to `tools_complete.py` (central registry) → routes to the appropriate `tools_*.py` module → each module uses `auth.py` to get an authenticated Google Ads client and calls the API.

### Key modules

| Module | Role |
|---|---|
| `src/server.py` | MCP server setup, tool/resource handlers |
| `src/tools_complete.py` | Central tool registry and dispatch for all 40+ tools |
| `src/auth.py` | OAuth2 + Service Account auth with TTL-cached clients |
| `src/error_handler.py` | Retry logic (tenacity), Google Ads error parsing |
| `src/validation.py` | Input validation, GAQL injection prevention, enum checks |
| `src/utils.py` | Currency micros conversion, date parsing, resource name helpers |

### Tool modules (11 files, `src/tools_*.py`)

Each tool module follows the same pattern: functions accept a `customer_id` and tool-specific params, get an authenticated client via `auth.get_google_ads_client()`, build API requests, and return structured results. The modules are: `campaigns`, `keywords`, `ads`, `extensions`, `bidding`, `ad_groups`, `audiences`, `assets`, `budgets`, `geography`, `reporting`.

**Adding a new tool:** Create the function in the appropriate `tools_*.py` module, then register it in `tools_complete.py`'s `TOOL_REGISTRY` dict and add its metadata to `get_all_tools()`.

## Important Patterns

- **Google Ads API v21**: Uses modern `AssetService` for extensions (not deprecated `ExtensionFeedItemService`). FieldMask handling must be v21-compatible.
- **Currency values**: Google Ads API uses micros (1 dollar = 1,000,000 micros). Use `utils.py` helpers for conversion.
- **Resource names**: Constructed as `customers/{id}/campaigns/{id}` etc. Use `utils.build_resource_name()`.
- **Proto-plus**: `use_proto_plus=True` by default. Affects how protobuf objects are constructed — some tools have smart fallback handling between proto-plus and raw protobuf styles.
- **Authentication**: Supports both OAuth2 (client_id/secret/refresh_token) and Service Account (JSON key file with optional impersonation). Clients are cached with 1-hour TTL via `cachetools`.
- **Error handling**: `error_handler.py` wraps API calls with exponential backoff retry. Distinguishes retryable errors (rate limits, transient) from permanent errors (invalid input, auth).
- **GAQL injection**: `validation.py` sanitizes user input used in Google Ads Query Language queries.

## Configuration

Credentials come from either `config.json` (see `config.example.json`) or environment variables prefixed with `GOOGLE_ADS_`. The env vars take precedence. Key required vars: `GOOGLE_ADS_DEVELOPER_TOKEN` plus OAuth2 or Service Account credentials.

## Code Style

- Python 3.10+, line length 88 (black)
- Ruff rules: E, F, I, N, W
- mypy with `disallow_untyped_defs = true` — all functions need type annotations
- Async functions throughout (MCP server is async)

## Client: CURA Medical Specialists

- **Customer ID:** `4611756192`
- **Website:** https://curaspecialists.com.au
- **Practice:** Neurology specialists in Sydney — Drummoyne, Nepean/Penrith, Gregory Hills

### Campaign Hierarchy (updated 2026-02-24)

#### Enabled Campaigns ($75/day total)

| Campaign | ID | Budget | Bidding | Purpose |
|---|---|---|---|---|
| Appointment Bookings | 22432832085 | $25/day | TARGET_CPA $5 | General booking intent |
| NCS Sydney | 23016371425 | $15/day | MAX_CONV | Nerve conduction studies |
| Near Me | 23578008459 | $5/day | MAX_CONV | Local "near me" searches (reduced from $20, 0 conv) |
| Migraine | 23578226562 | $15/day | MAX_CONV | Migraine-specific keywords |
| Tension Cluster | 23583571415 | $10/day | MAX_CONV | Tension & cluster headaches |
| Cervicogenic | 23588213188 | $5/day | MAX_CONV | Cervicogenic headaches |

#### Paused Campaigns

| Campaign | ID | Budget | Reason Paused |
|---|---|---|---|
| Emma Harrison Penrith | 22644007845 | $3/day | Low volume / optimization |
| Migraine Ads | 23081715570 | $3/day | High CPA ($197, 0 conversions) |
| Local Near Me - High Intent | 23588589252 | $10/day | 0 impressions — low search volume, keywords to be moved to Appointment Bookings |

### Account-Wide Settings

- **Call extensions:** 0279068356 (AU) on all 9 campaigns
- **Audience signals (OBSERVATION):** 90400 (Affinity), 80144 (In-Market) on all campaigns
- **Negative keywords (all campaigns):** how to, cost, price, salary, course, training, jobs, free, diy, bronwyn jenkins neurologist, neurologist open today, naturopath for migraines, naturopath, mri, mri scan, neurosurgeon, neuropsychological, brain mapping, pediatric, paediatric, yoga, acupuncture, physio, physiotherapy, cefaly, emgality, nurtec, nerve decompression surgery, rami haddad, geriatrician, spinal neurologist, online consultation, ssri, best ssri, endone, simon rowe, miriam welgampola, welgampola, maitland, campbelltown, hotdoc, headaches
- **Near Me campaign-level negative:** cervicogenic (prevents cannibalization with Cervicogenic campaign)
- **Near Me paused keyword:** "neurologist headache near me" (BROAD) — $39.95 wasted, 0 conversions

### Common URL Mistakes (always validate against sitemap)

- `/specialists` does NOT exist → use `/doctors`
- `/medicare-rebates` does NOT exist → use `/fees`
- `/locations/penrith` does NOT exist → use `/locations/nepean-penrith`

### Optimization Review Criteria (Week 2+)

- Pause campaign if CPA > $20 after 14 days
- Reduce budget 50% if 0 conversions after 14 days
- Star search term: "private neurologist sydney" ($0.93 CPA, 200% conv rate)
