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
