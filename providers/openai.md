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
  - https://developers.openai.com/api/docs/models/chat-latest
  - https://developers.openai.com/api/docs/guides/decisions
  - https://developers.openai.com/api/docs/guides/ultrafast-mode
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/models/gpt-6.1-sol
  - https://developers.openai.com/api/docs/guides/fast-mode
  - https://developers.openai.com/api/docs/deprecations
  - https://developers.openai.com/api/docs/guides/chatgpt-api-credits (read 2026-10-31)
  - https://developers.openai.com/api/docs/models/all (read 2026-11-03)
  - https://developers.openai.com/api/docs/guides/tools-connectors-mcp (read 2026-11-03)
  - https://developers.openai.com/blog/designing-failover-across-openai-model-providers (read 2026-11-03)
  - https://developers.openai.com/api/reference/overview (read 2026-11-03)
  - https://developers.openai.com/api/reference/workload-identity-federation (read 2026-11-03)
  - https://developers.openai.com/api/reference/resources/uploads/methods/create (read 2026-11-03)
---

# OpenAI API

first-party lab API

OpenAI trains the GPT models and serves them through its own platform at developers.openai.com, with two generative text endpoints, Responses and Chat Completions, a Batch API, and separate model families for images, speech, embeddings and moderation. Chat Completions is the request shape that most other providers imitate when they call themselves OpenAI-compatible; here it is the original, and the Responses API is the one OpenAI steers reasoning models to. [models, latest]

## Models offered

The GPT-6 guide lists Astra, GPT-6.1 Sol, GPT-6.1 Terra and GPT-6 Luna as current options [as-of 2026-10-27] L [guide-oct27]. Terra has a 1,050,000-token window, 128,000 maximum output tokens and image input [terra-oct27]. The model catalogue also lists specialist models (a cybersecurity set and a life-sciences model, GPT-Rosalind), image generation, realtime, transcription and speech models; embeddings and moderation models are linked from the page's navigation. The main model overview does not list the two open-weight gpt-oss models; the all-models catalogue lists both [as-of 2026-11-03] L [models-all-nov03]. They also have their own model pages. [models, astra, oss120, oss20]

| Model file | API id | Note |
| --- | --- | --- |
| [GPT-6 Astra](../models/openai/gpt-6-astra.md) | `gpt-6-astra` | $10 in, $1 cached, $50 out per Mtok on its page |
| [GPT-6.1 Sol](../models/openai/gpt-6.1-sol.md) | `gpt-6.1-sol` | listed on the catalogue as near-Astra at lower cost |
| [GPT-6.1 Terra](../models/openai/gpt-6.1-terra.md) | `gpt-6.1-terra` | visual reasoning, computer use and writing [as-of 2026-10-27] L [terra-oct27] |
| [GPT-6 Sol](../models/openai/gpt-6-sol.md) | `gpt-6-sol` | has its own page; not among the current guide's lead entries |
| [GPT-6 Luna](../models/openai/gpt-6-luna.md) | `gpt-6-luna` | the efficient, high-volume model; Decisions is generally available [as-of 2026-10-27] [decisions-oct27] |
| [Chat Latest](../models/openai/chat-latest.md) | `chat-latest` | rolling Instant alias; October 7 update has no numbered generation [as-of 2026-10-09] [chat-oct09, changelog-oct09] |
| GPT-5.6 Sol | `gpt-5.6-sol` | previous generation |
| [GPT-5.6 Terra](../models/openai/gpt-5.6-terra.md) | `gpt-5.6-terra` | previous generation |
| [GPT-5.6 Luna](../models/openai/gpt-5.6-luna.md) | `gpt-5.6-luna` | previous generation |
| [gpt-oss-120b](../models/openai/gpt-oss-120b.md), [gpt-oss-20b](../models/openai/gpt-oss-20b.md) | `gpt-oss-120b`, `gpt-oss-20b` | open-weight models with a 131,072-token window and no price on their model pages; hosted availability and endpoint support are UNVERIFIED [as-of 2026-11-03] L [oss120-nov03, oss20-nov03] |

The lineage, knowledge cutoffs and the effort levels each model accepts are in the [maker README](../models/openai/README.md). [astra]

## API surface

- **Protocols.** Its own two: Responses (`/v1/responses`) and Chat Completions (`/v1/chat/completions`), plus Batch, Files, embeddings, moderation, image, audio and Realtime endpoints. The Assistants API shut down on 2026-08-26; the replacements are Responses and Conversations. Its entries in the retention table are historical. [as-of 2026-10-09] L [deprecations-oct09, changelog-oct09] The GPT-6 models take Chat Completions, Responses and Batch, and not Realtime, Assistants or fine-tuning. [your-data, astra]
- **Endpoint limits by model.** In Chat Completions, GPT-6 Astra, GPT-6.1 Sol and GPT-6.1 Terra accept no tools [as-of 2026-10-27] L [guide-oct27], and GPT-6 Sol and GPT-6 Luna accept tools only with `reasoning_effort: "none"`. Tool calling with reasoning on needs the Responses API. [latest]
- **Decisions [as-of 2026-10-27].** Generally available at `POST /v1/decisions`, currently with `gpt-6-luna`; it supports up to 400 questions and shared-input caching. L [decisions-oct27].
  Shared text/image input is judged through `predicate`, `choice` and `score` questions. It returns
  typed answers, including possible refusals; a generated JSON object or tool request uses Responses
  instead. L [decisions-oct09]. See [decision models](../practices/decision-models.md).
- **Responses MCP [as-of 2026-11-03].** OpenAI says `connector_id` is deprecated for models released after 2026-09-01; existing models retain connector support. In Responses, use `server_url` for a remote MCP server or `tunnel_id` for a private server through Secure MCP Tunnel. OpenAI requests approval before data is shared by default. For authenticated servers, Responses does not retain the supplied `authorization` value; send it on each creation request. L [mcp-nov03].
- **Auth [as-of 2026-11-03].** The API accepts a bearer API key or a short-lived workload identity federation token. The API reference documents `OpenAI-Organization` and `OpenAI-Project` headers for users with multiple organisations or legacy user keys that access projects. Federation tokens use a mapped service account and cannot call Admin API endpoints. L [api-overview-nov03, federation-nov03].
- **SDKs.** Official clients for JavaScript, Python, .NET, Java, Go and Ruby. Microsoft publishes separate Azure OpenAI client libraries for .NET, JavaScript, Java and Go. [libraries]
- **Model ids.** Plain names with no vendor prefix (`gpt-6-astra`, `gpt-6.1-sol`). The Astra page lists one snapshot and no dated id. [astra, models]

## Feature parity

For a first-party API, parity means differences between endpoints and between OpenAI's own models, and the maker README records what other routes (Amazon Bedrock, Microsoft Foundry) list. [latest]

- **Reasoning and effort [as-of 2026-11-03].** Astra and 6.1 Sol support `low`, `medium`, `high`, `xhigh` and `max`, but not `none`; 6.1 Terra, GPT-6 Sol and Luna also support `none`. With effort above `none`, remove `temperature`, `top_p` and `top_logprobs`, also `logprobs` in Chat Completions or `message.output_text.logprobs` from `include` in Responses. Reasoning summaries are opt-in; the reasoning guide says raw reasoning is not returned for its reasoning models. The maker README has the persisted-reasoning and `configuration_update` details. L [guide-nov03, reasoning-nov03]
- **Tools.** In the Responses API the model page lists web search, file search, image generation, code interpreter, hosted shell, apply patch, skills, computer use, MCP and tool search for Astra. The maker README describes programmatic tool calling, async tool calling and a multi-agent mode; the multi-agent support list does not cover every model. [astra]
- **Structured output [as-of 2026-11-03].** `response_format: {type: "json_schema"}` in Chat Completions and `text.format` in Responses use a supported JSON Schema subset; strict mode also constrains function calls. The guide's `response_format` section says first use of a schema adds latency for fine-tuned models and not for other models; other examples in the same guide state the first-use latency without that qualification. Runtime behaviour is UNVERIFIED. Refusals and incomplete responses need separate handling. JSON mode aims for valid JSON rather than schema adherence. L [structured-nov03]
- **Caching [as-of 2026-11-03].** Cached input costs 10 percent of input on Astra and Luna and 5 percent on GPT-6.1 Sol and Terra. For GPT-5.6 and later in Responses, `ttl` selects a minimum cache lifetime of 30 minutes or 12 hours, not a deletion deadline. Explicit mode writes only selected eligible breakpoints; without one it neither reads nor writes the cache. Implicit mode selects an eligible message ending and can also use explicit breakpoints. L [pricing-nov03, cache-nov03]. The maker README has more cache details.
- **Batch [as-of 2026-11-03].** The Batch API covers Responses, Chat Completions, legacy Completions, embeddings, moderation and image generation and edit requests at half price with a 24-hour completion window, up to 50,000 requests and 200 MB per file. Unfinished requests in an expired batch are cancelled; output files are deleted 30 days after completion. L [batch-nov03]
- **Long context [as-of 2026-11-03].** The Astra page lists a 1,050,000-token context window and 128,000 maximum output tokens; it does not state 922,000 as a universal input limit. Requests above 272,000 input tokens bill at the long-context rate (see Pricing). L [astra-nov03, pricing-nov03]
- **Vision.** Image input on the lead models; image generation as separate models. [models, astra]
- **Streaming.** Listed as supported on the Astra page. [astra]

## Pricing

Per token with five pricing modes on one pricing page: Standard; Batch and Flex at 50 percent off most models; Fast, which the page says was the renamed Priority processing from 2026-07-30 and which it prices per model (the Astra page gives 2 times the applicable rate); and Ultrafast. **[as-of 2026-10-09]** Ultrafast costs 6 times Standard on both GPT-6 Astra and GPT-6.1 Sol. Sol short-context prices per Mtok are $12 input, $0.60 cached input, $15 cache write and $60 output; long-context prices are $24, $1.20, $30 and $90. L [pricing-oct09, ultrafast-oct09]. On Astra, requests above 272,000 input tokens pay 2 times the input and cached-input rates and 1.5 times the output rate. **[as-of 2026-10-27]** Cached input costs 10 percent of input on Astra and Luna and 5 percent on GPT-6.1 Sol and Terra. On supported Responses models, 30-minute writes cost 1.25 times input and 12-hour writes 2.5 times input, as total rates [pricing-oct27, cache-oct27]. Regional processing, which the page also calls data residency, adds 10 percent for models released on or after 2026-03-05, and FedRAMP endpoints take the same 10 percent from 2026-11-01 [as-of 2026-11-03] L [pricing-nov03]. Tools bill separately: web search $10 per 1,000 calls plus content tokens, file search $0.10 per GB-day (1 GB free) plus $2.50 per 1,000 calls, Hosted Shell and Code Interpreter containers $0.03 to $1.92 per 20-minute equivalent, depending on memory. Eligible container sessions bill per minute with a 5-minute minimum [as-of 2026-10-09] L [pricing-oct09]. The page mentions promotional pricing for GPT-5.6 Sol through 2026-11-21 and lists no general free tier or starter credit. Per-model prices are in the model files. [pricing]

**API credits for ChatGPT subscribers [as-of 2026-11-03].** From 2026-10-28, an owner of an eligible, paid ChatGPT Pro or Business subscription can link it to an API organization that the same person owns and claim monthly API credits. The subscription must be at least seven days old and the linked accounts must use the same email address. The amounts are $100, $200 or $500 for the three Pro tiers, and $20 per paid Business Standard seat or $100 per paid Business Premium seat, with a pooled cap of $500 for each Business workspace each month. Unused credits expire at the end of the billing cycle. The first grant is prorated; a Business workspace that pays annually upfront receives a full year in one grant that expires at the end of the annual billing cycle, with a $6,000 cap per annual cycle. L [credits-nov03] The credits do not cover Codex use through API keys. When no free or purchased credit remains, requests fail with HTTP 429 and code `credit_balance_exhausted`. This is a subscription benefit, not a free API tier. L [changelog-oct31, credits-oct31]

**Legal configuration [as-of 2026-11-03].** The pricing page lists `gpt-6-astra-law` as a legal model configuration at $10 input, $1 cached input and $50 output per million tokens. It says the promotional price lasts at least through 2026-12-31. The listing does not establish its access, API compatibility, release date or whether it is a separate model. L [pricing-nov03].

**Decisions pricing [as-of 2026-10-27].** `/v1/decisions` with GPT-6 Luna costs $0.10 per Mtok of uncached input. Cache reads and writes use the standard Luna cache rates; output is not charged. Long-context input and regional processing multipliers apply. L [decisions-oct27].

## Limits and data

- **Rate limits [as-of 2026-10-09].** Limits use requests, tokens or images per minute, with other
  time units for some models. Batch counts queued input tokens in a separate pool; some families
  share limits. The October 6 change replaces five numbered paid tiers with Build, Launch and Grow,
  reached after $5, $100 and $500 in total credit purchases. Their monthly usage ceilings are $500,
  $5,000 and $200,000. The rate guide also lists a Free usage ceiling of $100 for allowed geographies;
  this is not a grant of free credits or proof that a selected model supports Free. Standard Astra/Sol
  limits are 5,000/10,000/15,000 RPM and 1/4/40 million TPM. Ultrafast has a separate pool: Astra
  0.5/1/5 million TPM, Sol 1/4/40 million TPM. Organization limits and response headers are the
  operational source for a caller. L [rate-oct09, changelog-oct09, ultrafast-oct09].
- **Regions and residency [as-of 2026-11-03].** The data guide lists storage in the US, Europe, Australia, Canada, Japan, India, Singapore, South Korea, the UK and the UAE. It lists regional processing in the US and Europe, and in the UAE for selected endpoints and models. Non-US regions need approved abuse-monitoring controls and a Modified Retention amendment; the UAE requires additional approval. L [data-nov03]. Fast mode supports EU data residency on GPT-6.1 Sol, GPT-6.1 Terra and GPT-6 Luna, and not on Astra or GPT-6 Sol. Ultrafast supports US residency or global processing on Astra, and US/EU residency or global processing on GPT-6.1 Sol. Eligibility and contractual requirements still apply. L [fast-oct09, ultrafast-oct09]
- **Retention and training [as-of 2026-11-03].** API data is not used for training unless the customer opts in. Default abuse-monitoring logs are retained up to 30 days, with stated exceptions. Responses application state is retained for at least 30 days by default or with `store: true`; it is distinct from abuse logs. The Batch guide says output files are deleted 30 days after completion. The upload reference says `purpose=batch` files expire after 30 days by default and other uploaded files persist until deleted, unless an expiration policy is set. Zero Data Retention and Modified Abuse Monitoring need prior approval; ZDR forces `store` to false, but endpoint and feature exceptions apply. Data sent to an MCP server follows that server's retention policy. L [data-nov03, batch-nov03, uploads-nov03]. The retention table still has entries for Assistants logs and state, but that API is retired [as-of 2026-10-09] L [deprecations-oct09, changelog-oct09].

## Notes for agents and harnesses

- **Tools with reasoning need Responses [as-of 2026-11-03].** Tool calling on Astra, 6.1 Sol and 6.1 Terra requires Responses. GPT-6 Sol and Luna support function calling in Chat Completions only with effort `none`. L [guide-nov03]
- **Sampling parameters and effort `none`.** OpenAI's page says `temperature`, `top_p`, `top_logprobs` (and `logprobs` on Chat Completions) are removed once effort is above `none`. Its effort lists give Astra and 6.1 Sol no `none` and no GPT-6 model a `minimal`, so an effort map that sends `none` or `minimal` for a cheap setting fails on those two. [latest]
- **Effort mapping.** OpenAI's pages name levels from `none` to `max`, and each model accepts a subset. A generic low, medium or high setting uses names that exist here, but the same name on another vendor's scale is not the same amount of work; no source compares them.
- **Reasoning tokens count against the output cap.** The maker README records that they occupy the window and bill as output, and that a response that hits `max_output_tokens` can end with status `incomplete` before any visible text.
- **Stateless use needs replay.** With `store: false` or under ZDR, reasoning items carry encrypted content that goes back with the other output items (maker README).
- **Cost steps up past 272,000 input tokens** because the whole request reprices at the higher rate. [pricing]
- **Batch is half price** and uses a separate rate pool; the 24-hour window is a maximum and not a promise of speed. [batch]
- **Other hosts copy Chat Completions, not Responses.** A client written to the Responses API does not run unchanged on a host that only copies Chat Completions; the other provider's parity section says which it offers. [models]

**Provider failover [as-of 2026-11-03].** OpenAI advises testing each approved route for the needed model, API, tools, region, data controls, capacity and behaviour before failover. A switch does not itself resume an Agents API session or reconcile earlier actions. Retry only when the operation can be repeated safely; resolve uncertain tool actions before a restart. Its guidance excludes automatic switching for access errors, refusals, exhausted quota or credits, and unknown errors. These are vendor recommendations, not a measured availability guarantee. L [failover-nov03].

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

Partial correction sources:

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| chat-oct09 | https://developers.openai.com/api/docs/models/chat-latest | L | 2026-10-09 |
| decisions-oct09 | https://developers.openai.com/api/docs/guides/decisions | L | 2026-10-09 |
| ultrafast-oct09 | https://developers.openai.com/api/docs/guides/ultrafast-mode | L | 2026-10-09 |
| pricing-oct09 | https://developers.openai.com/api/docs/pricing | L | 2026-10-09 |
| rate-oct09 | https://developers.openai.com/api/docs/guides/rate-limits | L | 2026-10-09 |
| changelog-oct09 | https://developers.openai.com/api/docs/changelog | L | 2026-10-09 |
| fast-oct09 | https://developers.openai.com/api/docs/guides/fast-mode | L | 2026-10-09 |
| deprecations-oct09 | https://developers.openai.com/api/docs/deprecations | L | 2026-10-09 |
| terra-oct27 | https://developers.openai.com/api/docs/models/gpt-6.1-terra | L | 2026-10-27 |
| decisions-oct27 | https://developers.openai.com/api/docs/guides/decisions | L | 2026-10-27 |
| guide-oct27 | https://developers.openai.com/api/docs/guides/latest-model | L | 2026-10-27 |
| pricing-oct27 | https://developers.openai.com/api/docs/pricing | L | 2026-10-27 |
| cache-oct27 | https://developers.openai.com/api/docs/guides/prompt-caching | L | 2026-10-27 |
| changelog-oct31 | https://developers.openai.com/api/docs/changelog | L | 2026-10-31 |
| credits-oct31 | https://developers.openai.com/api/docs/guides/chatgpt-api-credits | L | 2026-10-31 |
| models-all-nov03 | https://developers.openai.com/api/docs/models/all | L | 2026-11-03 |
| mcp-nov03 | https://developers.openai.com/api/docs/guides/tools-connectors-mcp | L | 2026-11-03 |
| pricing-nov03 | https://developers.openai.com/api/docs/pricing | L | 2026-11-03 |
| failover-nov03 | https://developers.openai.com/blog/designing-failover-across-openai-model-providers | L | 2026-11-03 |
| credits-nov03 | https://developers.openai.com/api/docs/guides/chatgpt-api-credits | L | 2026-11-03 |
| structured-nov03 | https://developers.openai.com/api/docs/guides/structured-outputs | L | 2026-11-03 |
| api-overview-nov03 | https://developers.openai.com/api/reference/overview | L | 2026-11-03 |
| federation-nov03 | https://developers.openai.com/api/reference/workload-identity-federation | L | 2026-11-03 |
| data-nov03 | https://developers.openai.com/api/docs/guides/your-data | L | 2026-11-03 |
| batch-nov03 | https://developers.openai.com/api/docs/guides/batch | L | 2026-11-03 |
| uploads-nov03 | https://developers.openai.com/api/reference/resources/uploads/methods/create | L | 2026-11-03 |
| cache-nov03 | https://developers.openai.com/api/docs/guides/prompt-caching | L | 2026-11-03 |
| guide-nov03 | https://developers.openai.com/api/docs/guides/latest-model | L | 2026-11-03 |
| astra-nov03 | https://developers.openai.com/api/docs/models/gpt-6-astra | L | 2026-11-03 |
| oss120-nov03 | https://developers.openai.com/api/docs/models/gpt-oss-120b | L | 2026-11-03 |
| oss20-nov03 | https://developers.openai.com/api/docs/models/gpt-oss-20b | L | 2026-11-03 |
| reasoning-nov03 | https://developers.openai.com/api/docs/guides/reasoning | L | 2026-11-03 |
