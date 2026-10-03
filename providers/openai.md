---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: first-party lab API
sources:
  - https://developers.openai.com/api/docs/models
  - https://developers.openai.com/api/docs/models/gpt-6-astra
  - https://developers.openai.com/api/docs/guides/latest-model
  - https://developers.openai.com/api/docs/guides/rate-limits
  - https://developers.openai.com/api/docs/guides/your-data
  - https://developers.openai.com/api/docs/pricing
  - https://developers.openai.com/api/docs/guides/batch
  - https://developers.openai.com/api/docs/guides/structured-outputs
  - https://developers.openai.com/api/docs/libraries
  - https://developers.openai.com/api/docs/models/gpt-oss-120b
  - https://developers.openai.com/api/docs/models/gpt-oss-20b
---

# OpenAI API

first-party lab API

OpenAI trains the GPT models and serves them through its own platform at developers.openai.com, with two text endpoints, Responses and Chat Completions, a Batch API, and separate model families for images, speech, embeddings and moderation. Chat Completions is the request shape that most other providers imitate when they call themselves OpenAI-compatible; here it is the original, and the Responses API is the one OpenAI steers reasoning models to. [models, latest]

## Models offered

The catalogue page lists three frontier text and code models as the lead entries: GPT-6 Astra, GPT-6.1 Sol and GPT-6 Luna, each with a 1,050,000-token window (922,000 input at most), 128,000 output tokens and image input. It also lists specialist models (a cybersecurity set and a life-sciences model, GPT-Rosalind), image generation, realtime, transcription and speech models; embeddings and moderation models are linked from the page's navigation. The two open-weight gpt-oss models are not on the catalogue page but have their own model pages. [models, astra, oss120, oss20]

| Model file | API id | Note |
| --- | --- | --- |
| [GPT-6 Astra](../models/openai/gpt-6-astra.md) | `gpt-6-astra` | $10 in, $1 cached, $50 out per Mtok on its page |
| [GPT-6.1 Sol](../models/openai/gpt-6.1-sol.md) | `gpt-6.1-sol` | listed on the catalogue as near-Astra at lower cost |
| [GPT-6 Sol](../models/openai/gpt-6-sol.md) | `gpt-6-sol` | has its own page; not among the three lead entries |
| [GPT-6 Luna](../models/openai/gpt-6-luna.md) | `gpt-6-luna` | the efficient, high-volume model |
| GPT-5.6 Sol | `gpt-5.6-sol` | previous generation |
| [GPT-5.6 Terra](../models/openai/gpt-5.6-terra.md) | `gpt-5.6-terra` | previous generation |
| [GPT-5.6 Luna](../models/openai/gpt-5.6-luna.md) | `gpt-5.6-luna` | previous generation |
| [gpt-oss-120b](../models/openai/gpt-oss-120b.md), [gpt-oss-20b](../models/openai/gpt-oss-20b.md) | `gpt-oss-120b`, `gpt-oss-20b` | each model page lists the Responses API as supported and Chat Completions as not supported (20b also lists Batch), a 131,072-token window and no price; whether these are billed hosted models was not established |

The lineage, knowledge cutoffs and the effort levels each model accepts are in the [maker README](../models/openai/README.md). [astra]

## API surface

- **Protocols.** Its own two: Responses (`/v1/responses`) and Chat Completions (`/v1/chat/completions`), plus Batch, Files, embeddings, moderation, image, audio and Realtime endpoints. The older Assistants endpoint still appears in the retention table. The GPT-6 models take Chat Completions, Responses and Batch, and not Realtime, Assistants or fine-tuning. [your-data, astra]
- **Endpoint limits by model.** In Chat Completions, GPT-6 Astra and GPT-6.1 Sol accept no tools, and GPT-6 Sol and GPT-6 Luna accept tools only with `reasoning_effort: "none"`. Tool calling with reasoning on needs the Responses API. [latest]
- **Auth.** An API key; the official SDKs read it from `OPENAI_API_KEY`. The libraries page names no organisation or project header. [libraries]
- **SDKs.** Official clients for JavaScript, Python, .NET, Java, Go and Ruby. Microsoft publishes separate Azure OpenAI client libraries for .NET, JavaScript, Java and Go. [libraries]
- **Model ids.** Plain names with no vendor prefix (`gpt-6-astra`, `gpt-6.1-sol`). The Astra page lists one snapshot and no dated id. [astra, models]

## Feature parity

For a first-party API, parity means differences between endpoints and between OpenAI's own models, and the maker README records what other routes (Amazon Bedrock, Microsoft Foundry) list. [latest]

- **Reasoning and effort.** Effort values `low`, `medium`, `high`, `xhigh` and `max` on Astra and 6.1 Sol (no `none`), and the same plus `none` on GPT-6 Sol and Luna. With effort above `none`, `temperature`, `top_p`, `top_logprobs` and `logprobs` must be removed. Summaries are opt-in and the raw reasoning is never returned. The maker README has the persisted-reasoning and `configuration_update` details. [latest]
- **Tools.** In the Responses API the model page lists web search, file search, image generation, code interpreter, hosted shell, apply patch, skills, computer use, MCP and tool search for Astra. The maker README describes programmatic tool calling, async tool calling and a multi-agent mode; the multi-agent support list does not cover every model. [astra]
- **Structured output.** `response_format: {type: "json_schema"}` in Chat Completions and `text.format` in Responses constrain output to a schema, and strict mode does the same for function calls. The first request with a new schema pays extra latency, a refusal arrives in a separate `refusal` field instead of schema-shaped text, and the page says some JSON Schema features are unavailable without listing them. Older JSON mode only guarantees valid JSON. [structured]
- **Caching.** Prompt caching is on the model page's feature list. Cached input is priced at 10 percent of the input rate on the pricing page, and the maker README records the cache-write, explicit-breakpoint and `ttl` details. [astra, pricing]
- **Batch.** The Batch API covers Responses, Chat Completions, legacy Completions, embeddings, moderation and image generation and edit requests at half price with a 24-hour completion window, up to 50,000 requests and 200 MB per file; output files are deleted 30 days after completion. [batch]
- **Long context.** 1.05M tokens (922,000 input at most); requests above 272,000 input tokens bill at the long-context rate (see Pricing). [pricing, astra]
- **Vision.** Image input on the three lead models; image generation as separate models. [models, astra]
- **Streaming.** Listed as supported on the Astra page. [astra]

## Pricing

Per token with five pricing modes on one pricing page: Standard; Batch and Flex at 50 percent off most models; Fast, which the page says was the renamed Priority processing from 2026-07-30 and which it prices per model (the Astra page gives 2 times the applicable rate); and Ultrafast at 6 times, limited to GPT-6 Astra. On Astra, requests above 272,000 input tokens pay 2 times the input and cached-input rates and 1.5 times the output rate. Cached input costs 10 percent of the input rate, and cache writes cost extra per model (Astra: $12.50 against $10 input). Regional processing, which the page also calls data residency, adds 10 percent for models released on or after 2026-03-05, and FedRAMP endpoints take the same 10 percent. Tools bill separately: web search $10 per 1,000 calls plus content tokens, file search $0.10 per GB-day (1 GB free) plus $2.50 per 1,000 calls, code interpreter containers $0.03 to $1.92 per 20-minute session depending on memory. The page mentions promotional pricing for GPT-5.6 Sol through 2026-11-21 and lists no general free tier or starter credit. Per-model prices are in the model files. [pricing]

## Limits and data

- **Rate limits.** Measured in requests, tokens and images per minute (and audio minutes per minute for some streaming audio models), plus requests and tokens per day on some models; whichever is hit first applies. Batch limits count queued input tokens per model in a separate pool. Some model families share one limit. Six usage tiers, promoted automatically by cumulative paid spend: Free (allowed geography, $100 a month), Tier 1 ($5 paid, $100), Tier 2 ($50, $500), Tier 3 ($100, $1,000), Tier 4 ($250, $5,000), Tier 5 ($1,000, $200,000). Astra's page gives 500 requests and 500,000 tokens a minute at Tier 1 and 15,000 requests and 40 million tokens at Tier 5. Responses carry `x-ratelimit-*` headers. [rate, astra]
- **Regions and residency.** Data at rest can be kept in 12 regions (including the US, Europe, Australia, Canada, Japan, India, Singapore, South Korea, the UK and the UAE); regional processing, not only storage, is offered in the US and Europe, and in the UAE for some models only. Non-US regions need an approved abuse-monitoring control. OpenAI's latest-model guide says fast mode is unavailable with EU data residency for GPT-6 Astra, GPT-6 Sol and GPT-6 Luna, and that Ultrafast runs only with US residency or global processing. [your-data, latest]
- **Retention and training.** Data sent to the API is not used for training unless the customer opts in. Abuse-monitoring logs are kept 30 days by default on Chat Completions, Responses, Files, Batch, Assistants and Realtime; Files, Batch outputs and Assistants state also persist until deleted. Zero Data Retention and Modified Abuse Monitoring both need prior approval; ZDR also forces `store` to false. [your-data]

## Notes for agents and harnesses

- **Tools with reasoning need Responses.** Chat Completions rejects tools on Astra and 6.1 Sol altogether, and on Sol and Luna unless effort is `none`, so the Chat Completions tool loop does not carry over to these models. [latest]
- **Sampling parameters and effort `none`.** OpenAI's page says `temperature`, `top_p`, `top_logprobs` (and `logprobs` on Chat Completions) are removed once effort is above `none`. Its effort lists give Astra and 6.1 Sol no `none` and no GPT-6 model a `minimal`, so an effort map that sends `none` or `minimal` for a cheap setting fails on those two. [latest]
- **Effort mapping.** OpenAI's pages name levels from `none` to `max`, and each model accepts a subset. A generic low, medium or high setting uses names that exist here, but the same name on another vendor's scale is not the same amount of work; no source compares them.
- **Reasoning tokens count against the output cap.** The maker README records that they occupy the window and bill as output, and that a response that hits `max_output_tokens` can end with status `incomplete` before any visible text.
- **Stateless use needs replay.** With `store: false` or under ZDR, reasoning items carry encrypted content that goes back with the other output items (maker README).
- **Cost steps up past 272,000 input tokens** because the whole request reprices at the higher rate. [pricing]
- **Batch is half price** and uses a separate rate pool; the 24-hour window is a maximum and not a promise of speed. [batch]
- **Other hosts copy Chat Completions, not Responses.** A client written to the Responses API does not run unchanged on a host that only copies Chat Completions; the other provider's parity section says which it offers. [models]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| models | https://developers.openai.com/api/docs/models | L | 2026-10-03 |
| astra | https://developers.openai.com/api/docs/models/gpt-6-astra | L | 2026-10-03 |
| latest | https://developers.openai.com/api/docs/guides/latest-model | L | 2026-10-03 |
| rate | https://developers.openai.com/api/docs/guides/rate-limits | L | 2026-10-03 |
| your-data | https://developers.openai.com/api/docs/guides/your-data | L | 2026-10-03 |
| pricing | https://developers.openai.com/api/docs/pricing | L | 2026-10-03 |
| batch | https://developers.openai.com/api/docs/guides/batch | L | 2026-10-03 |
| structured | https://developers.openai.com/api/docs/guides/structured-outputs | L | 2026-10-03 |
| libraries | https://developers.openai.com/api/docs/libraries | L | 2026-10-03 |
| oss120 | https://developers.openai.com/api/docs/models/gpt-oss-120b | L | 2026-10-03 |
| oss20 | https://developers.openai.com/api/docs/models/gpt-oss-20b | L | 2026-10-03 |
