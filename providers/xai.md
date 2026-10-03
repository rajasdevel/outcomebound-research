---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: first-party lab API
sources:
  - https://docs.x.ai/developers/models
  - https://docs.x.ai/developers/models/grok-4.7
  - https://docs.x.ai/developers/pricing
  - https://docs.x.ai/docs/key-information/regions
  - https://docs.x.ai/docs/key-information/consumption-and-rate-limits
  - https://docs.x.ai/developers/faq/security
  - https://docs.x.ai/developers/model-capabilities/text/comparison
  - https://docs.x.ai/developers/model-capabilities/text/structured-outputs
  - https://gigazine.net/news/20260707-xai-change-spacexai/
---

# xAI API

first-party lab API

xAI trains the Grok models and serves them through its own API at `https://api.x.ai/v1`. Its current documentation pages name the company SpaceXAI (a press report dates the rename announcement on the company's X account to early July 2026 [rename]) and the docs have moved from `docs.x.ai/docs` to `docs.x.ai/developers`; the API host and the "xAI" name in the SDKs are unchanged. The API has a Responses endpoint it recommends and a Chat Completions endpoint it labels legacy, and it also serves image, video and voice models. [models, compare]

## Models offered

Only Grok models and the company's media models. On 2026-10-03 the models page names Grok 4.7 as its recommendation for code and chat, and lists these text models (context in tokens): `grok-4.7`, `grok-4.6` and `grok-4.5` (500k), `grok-4.3` and the `grok-4.20-0309` models (1M), `grok-build-0.1` (256k) and a multi-agent model (1M). Image models (Grok Imagine image), video models and voice models (speech-to-speech, speech-to-text, text-to-speech) are priced separately on the same page. [models, pricing]

| Model file | API id | Note |
| --- | --- | --- |
| [Grok 4.7](../models/xai/grok-4.7.md) | `grok-4.7` | 500k context; four effort levels, `high` by default |
| [Grok 4.6](../models/xai/grok-4.6.md) | `grok-4.6` | previous generation |
| [Grok 4.7 Fast](../models/xai/grok-4.7-fast.md) | none on the public API | the model files record it as offered only inside two products; not on the models page |
| [Grok Build 0.1](../models/xai/grok-build-0.1.md) | `grok-build-0.1` | coding model, 256k context |

Generic names point to the latest stable version, a `-latest` suffix to the newest features and a date suffix to a fixed snapshot. The 4.5, 4.3 and 4.20 models are listed on the page but have no file in the library (two generations per class). [models] The lineage is in the [maker README](../models/xai/README.md).

## API surface

- **Protocols.** The Responses API (`/v1/responses`) is the recommended interface. Chat Completions (`/v1/chat/completions`) is called legacy and deprecated; it keeps function calling, takes no encrypted reasoning content and has no native server-side tools. Moving from one to the other renames `messages` to `input` and `max_tokens` to `max_output_tokens`, and the response is an `output` array of typed items. Responses are stored 30 days and continue with `previous_response_id`. [compare]
- **OpenAI compatibility.** The OpenAI SDKs work with `base_url` set to `https://api.x.ai/v1`, on both endpoints. The migration page that would list unsupported parameters was not reachable (404), so the parameter-level differences below come from the maker README. No Anthropic-compatible endpoint was found in the docs read. [compare]
- **Auth.** An API key in the bearer header, created in the console; the same keys work on the regional endpoint. [regions]
- **SDKs.** A Python SDK (gRPC) from xAI, the OpenAI SDKs, and the Vercel AI SDK with an `xai.responses(...)` helper (all per the maker README). [compare]
- **Model ids.** Plain lower-case ids with a dot (`grok-4.7`). [models]

## Feature parity

First-party, so the differences are between the two endpoints and between models. [compare, grok-4.7]

- **Reasoning and effort.** `grok-4.7` has four effort levels, `low`, `medium`, `high` and `xhigh`, default `high`. The maker README records that reasoning cannot be turned off from Grok 4.5 on, that Chat Completions uses `reasoning_effort` and Responses `reasoning.effort`, and that `presencePenalty`, `frequencyPenalty` and `stop` error on reasoning models. [grok-4.7]
- **Tools.** Chat Completions offers function calling only. Server-side tools run only on Responses: the comparison page names search, code execution and MCP, and the pricing page bills web search, X search, code execution, attachment search and collections search. [compare, pricing]
- **Structured output.** `response_format` of type `json_schema` (or `json_object`), or tool arguments that are always validated against their schema. The schema subset accepts the JSON types, enums, non-circular `$ref` and `$defs`, `anyOf` and `oneOf`, and enforced formats (`date`, `time`, `date-time`, `email`, `uuid`, `ipv4`, `ipv6`, `uri`); `minLength` and `maxLength` up to 2,048, `minItems` and `maxItems` up to 256 and `minProperties` and `maxProperties` up to 64 are guaranteed; `not` and `if/then/else` are best effort. [structured]
- **Caching.** Automatic; on the pricing page cached input costs 25 percent of the input rate on Grok 4.7 and 4.6, 20 percent on Grok Build 0.1 and 16 percent on the 4.3 and 4.20 models. [pricing]
- **Batch.** A 20 percent discount, limited on the pricing page to `grok-4.3` and the 4.20 models; the Grok 4.7 page says Batch is unavailable. [pricing, grok-4.7]
- **Long context.** 500k on 4.7; prompts above 200k tokens pay higher rates on every token. [grok-4.7, pricing]
- **Vision.** Image input as jpg, jpeg or png up to 20 MiB, no stated count limit; audio and video are separate models. [models]
- **Streaming.** The structured-outputs page shows streamed JSON output; the maker README documents a WebSocket mode for Responses. [structured]

## Pricing

Per token, with two bands by prompt size (under or at least 200,000 tokens). Grok 4.7 and 4.6 list $2 to $4 input, $0.50 to $1 cached input and $6 to $12 output per million tokens; the older 4.3 and 4.20 models are cheaper and `grok-build-0.1` is cheaper still. Priority processing charges 2 times the token rates. The US regional endpoint adds 10 percent. Server-side tools bill per call on top of tokens: web search, X search, code execution and attachment search $5 per 1,000 calls each, collections search $2.50 per 1,000. File storage is $0.025 per GiB a day and collection storage $0.10 per GiB a day. A request that the system judges a violation and stops before generating is billed a $0.05 fee. Media models are priced per image, per second of video or per minute of voice. The page lists no free credit. Per-model prices are in the model files. [pricing]

## Limits and data

- **Rate limits.** Requests per second and tokens per minute, per model; tokens counted are prompt, completion, reasoning and cached prompt tokens. Tiers rise automatically with cumulative spend since 2026-01-01: Tier 0 at $0, Tier 1 at $50, Tier 2 at $250, Tier 3 at $1,000, Tier 4 at $5,000, and Enterprise on request; a tier is never lost once reached. Example at Tier 0: `grok-4.7` 150 requests per second and 50 million tokens a minute; `grok-4.3` 37 and 10 million. Image models are limited by requests (6 per second at Tier 0). Exceeding a limit returns 429. Personal limits show in the console's Models page. [rates, grok-4.7]
- **Regions.** The global endpoint routes by capacity. The US endpoint `https://us.api.x.ai/v1` guarantees US request handling, inference, safety moderation and stored output and metadata, costs 10 percent more and serves only `grok-4.7` and `grok-4.6` (others, including `grok-latest`, return 404). The US guarantee does not cover image, video and voice generation, Files, Collections or the server-side tools, which may process data outside the US, and the page warns that choosing the regional endpoint does not on its own meet every data-residency requirement. The model page lists hosting regions `us-east-1`, `us-west-2` and `us-central-1` for 4.7. [regions, grok-4.7]
- **Retention and training.** Requests and responses are kept encrypted for 30 days for abuse audit and then deleted; the company says it does not train on API inputs or outputs without explicit permission. Zero Data Retention is a team-level setting that disables the stateful Responses API, Files, Collections, the Batch API and deferred completions, and the docs advise most customers not to use it. SOC 2 Type 2 compliance is stated, HIPAA is available through a BAA questionnaire, and GDPR information is in the Trust Center, which needs an NDA. US processing is guaranteed only on the regional endpoint. [security]

## Notes for agents and harnesses

- **Responses is the recommended endpoint.** Chat Completions drops encrypted reasoning content and the server-side tools, so a client that keeps history itself loses the reasoning that carries across turns. Responses also stores state for 30 days, which ZDR switches off. [compare, security]
- **Effort mapping.** `high` is the default and Grok 4.5 and later cannot turn reasoning off, so a harness that sends a "no reasoning" setting to these models has no equivalent. A request for `xhigh` on a model that lacks it is treated as `high` on 4.5 (maker README). [grok-4.7]
- **Parameters that error.** `presence_penalty`, `frequency_penalty` and `stop` on reasoning models (maker README); a client library that sends them by default fails.
- **Regional endpoint limits.** On the US endpoint only two text models are served, and Files, Collections, server tools and media models fall outside the US processing guarantee. [regions]
- **Cost and limits.** The 200,000-token prompt threshold reprices every token; Batch is not offered for the current Grok. [pricing, grok-4.7]
- **Attribution.** `safety_identifier` carries a hash of an end-user id (the page says never an email, phone number or display name), so a policy violation is attributed to that user rather than to the whole API key. [security]
- **Name drift.** Docs paths, the company name and some product names changed in 2026, so links from older write-ups may 404. [models]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| models | https://docs.x.ai/developers/models | L | 2026-10-03 |
| grok-4.7 | https://docs.x.ai/developers/models/grok-4.7 | L | 2026-10-03 |
| pricing | https://docs.x.ai/developers/pricing | L | 2026-10-03 |
| regions | https://docs.x.ai/docs/key-information/regions | L | 2026-10-03 |
| rates | https://docs.x.ai/docs/key-information/consumption-and-rate-limits | L | 2026-10-03 |
| security | https://docs.x.ai/developers/faq/security | L | 2026-10-03 |
| compare | https://docs.x.ai/developers/model-capabilities/text/comparison | L | 2026-10-03 |
| structured | https://docs.x.ai/developers/model-capabilities/text/structured-outputs | L | 2026-10-03 |
| rename | https://gigazine.net/news/20260707-xai-change-spacexai/ | A | 2026-10-03 |
