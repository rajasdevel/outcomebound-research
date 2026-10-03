---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: first-party lab API
sources:
  - https://platform.kimi.ai/docs/overview
  - https://platform.kimi.ai/docs/guide/kimi-k3-quickstart
  - https://platform.kimi.ai/docs/pricing/limits
  - https://platform.kimi.ai/docs/pricing/chat
  - https://platform.kimi.ai/docs/guide/zero-data-retention
  - https://platform.kimi.ai/docs/agreement/modeluse
  - https://www.kimi.com/help/kimi-api/api-data-security
---

# Moonshot (Kimi) API

first-party lab API

Moonshot AI trains the Kimi models and sells them through the Kimi Open Platform (platform.kimi.ai, also reached as platform.moonshot.ai), with a base URL of `https://api.moonshot.ai/v1`. The API speaks the OpenAI format and the Anthropic Messages format, and the K3 page describes K3 as an open-source model. The Terms of Service name Moonshot AI PTE. LTD. as the contracting party, and the company's consumer product, Kimi, is a separate service with its own terms. [overview, terms]

## Models offered

The overview names three: Kimi K3 (the flagship, 1M-token context), Kimi K2.7 Code (256K, built for programming) and Kimi K2.6 (general purpose, 256K). Text, image and video go in; the pages list streaming, tool calling, JSON mode and reasoning modes. [overview]

| Model file | API id | Note |
| --- | --- | --- |
| [Kimi K3](../models/moonshot/kimi-k3.md) | `kimi-k3` | 1M context; thinking always on |
| [Kimi K2.7 Code](../models/moonshot/kimi-k2.7-code.md) | `kimi-k2.7-code` | 256K context |

Kimi K2.6 is on the overview but has no file in the library (two generations per class). The maker README lists a `kimi-k2.7-code-highspeed` id as the same model served faster, and records retirements: the `kimi-k2` series on 2026-05-25 and `kimi-k2.5` and `moonshot-v1` on 2026-08-31, now returning 404. The lineage is in the [maker README](../models/moonshot/README.md). [overview]

## API surface

- **Protocols.** OpenAI Chat Completions at `https://api.moonshot.ai/v1`, a Responses API option and an Anthropic Messages-compatible interface; the maker README places the Anthropic format at `/anthropic`. The overview asks for the OpenAI SDK 1.0.0 or later in Python and Node.js. The OpenAI SDK needs `extra_body` for Kimi's own `thinking` field (maker README). [overview]
- **Auth.** An API key, read in the examples from `MOONSHOT_API_KEY`. Access to K3 needs a first top-up of at least $1. [overview, k3]
- **SDKs.** No Moonshot SDK was found in the pages read; the OpenAI and Anthropic SDKs are the documented route. [overview]
- **Model ids.** Lower-case with a dot or hyphen as the product names them (`kimi-k3`, `kimi-k2.7-code`); Claude Code reaches K3 through an alias `kimi-k3[1m]` on the Anthropic endpoint (maker README). [overview]

## Feature parity

First-party. Details from the K3 page unless noted. [k3]

- **Reasoning and effort.** K3 always thinks and takes a `reasoning_effort` of `low`, `high` or `max`. Temperature (1.0), `top_p` (0.95), `n` (1) and the penalty parameters (0) are fixed and cannot be changed. [k3]
- **Tools.** Custom tools, dynamic tool loading and `tool_choice: "required"` on K3. Official tools come from a Formula `/tools` endpoint whose definitions go into the `tools` field, and the K3 page says web search is being updated and is not recommended for near-term production use; the maker README adds a web-search API launched in September 2026. [k3]
- **Structured output.** JSON Schema with strict mode on K3; JSON mode generally. [k3, overview]
- **Caching.** Automatic context caching on K3 with a 5-minute or 1-hour lifetime, charged as separate writes, hits and misses; K2 models use a simpler hit and miss rate. [pricing, k3]
- **Batch.** A Batch API exists (maker README); the pricing page names no batch discount. [pricing]
- **Long context.** 1,048,576 tokens on K3; `max_completion_tokens` defaults to 131,072 and can reach 1,048,576. [k3]
- **Vision.** Base64 images and video uploads; no public URLs. [k3]
- **Streaming.** Supported. [overview]
- **Partial mode.** A final assistant message with `partial=True` carries a prefix that the model continues. [k3]

## Pricing

Per token, with separate rates for input, output and, on K3, cache writes (5-minute or 1-hour), cache hits and cache misses. The pricing page names no batch discount, long-context surcharge, free-credit tier or tool price, and says file extraction and storage are temporarily free while extracted content still counts as tokens. Access starts with a $1 minimum top-up, and a $5 cumulative recharge brings a $5 voucher. Per-model prices are in the model files. [pricing, limits, k3]

## Limits and data

- **Rate limits.** Tiers follow cumulative recharge, from Tier 0 ($1) to Tier 5 ($3,000). Five dimensions: concurrency (1 to 100 by tier), requests per minute, tokens per minute, tokens per day and a separate web-search queries-per-second quota. Tier 0 is 1 concurrent request, 3 requests and 500,000 tokens a minute and 1.5 million tokens a day; Tier 5 is 100, 300 requests, 5 million tokens a minute and unlimited daily tokens. The page names no process for raising limits other than recharging. [limits]
- **Regions.** One global host (`api.moonshot.ai`); no regional endpoints were found in the pages read. The maker README notes that Amazon Bedrock hosts K3 with cross-Region profiles. [overview]
- **Retention and training.** The sources disagree. The platform's data-security help page (in Chinese) says API inputs and outputs are not used to train or improve Kimi models and serve only the current request, while the Terms of Service say Moonshot may use Content to provide, maintain, develop and improve the services unless otherwise agreed in writing, and point customers who want training restrictions to enterprise arrangements or separate written agreements. Zero Data Retention is for enterprise customers, by request through sales: content is deleted once the response is returned and is not used for training, and it excludes images and videos from direct file uploads, operational data such as security logs and billing, and third-party models, connectors and plugins; safety review still applies, and abuse can end the ZDR service. [datasecurity, terms, zdr]

## Notes for agents and harnesses

- **Sampling is fixed.** A harness that sets `temperature`, `top_p`, `n` or penalties on K3 changes nothing; K3's page says they cannot be modified. [k3]
- **Effort mapping.** Three levels (`low`, `high`, `max`) and thinking cannot be switched off on K3, so a "no reasoning" setting has no equivalent. [k3]
- **Training terms conflict.** The Terms of Service and the data-security help page say different things about default use of API content; only the enterprise arrangement is stated to restrict it. [terms, datasecurity]
- **Rate limits start very low.** Tier 0 allows one concurrent request and 3 requests a minute, so a fresh account cannot run parallel agents until it is recharged. [limits]
- **Images by upload only.** K3 takes base64 or uploaded images and video, not public URLs. [k3]
- **Anthropic-format clients.** The `kimi-k3[1m]` alias exists for Claude Code, so a client that appends a context suffix works against the Anthropic endpoint (maker README).
- **Retired ids return 404.** Pipelines that still name `kimi-k2` or `moonshot-v1` ids fail. (Maker README.)

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| overview | https://platform.kimi.ai/docs/overview | L | 2026-10-03 |
| k3 | https://platform.kimi.ai/docs/guide/kimi-k3-quickstart | L | 2026-10-03 |
| limits | https://platform.kimi.ai/docs/pricing/limits | L | 2026-10-03 |
| pricing | https://platform.kimi.ai/docs/pricing/chat | L | 2026-10-03 |
| zdr | https://platform.kimi.ai/docs/guide/zero-data-retention | L | 2026-10-03 |
| terms | https://platform.kimi.ai/docs/agreement/modeluse | L | 2026-10-03 |
| datasecurity | https://www.kimi.com/help/kimi-api/api-data-security | L | 2026-10-03 |
