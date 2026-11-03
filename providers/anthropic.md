---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: first-party lab API
sources:
  - https://www.anthropic.com/claude/mythos
  - https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide
  - https://www.anthropic.com/claude-haiku-5-5
  - https://platform.claude.com/docs/en/models/haiku-5-5/overview
  - https://platform.claude.com/docs/en/api/overview
  - https://platform.claude.com/docs/en/api/rate-limits
  - https://platform.claude.com/docs/en/api/service-tiers
  - https://platform.claude.com/docs/en/api/supported-regions
  - https://platform.claude.com/docs/en/about-claude/models/overview
  - https://platform.claude.com/docs/en/about-claude/pricing
  - https://platform.claude.com/docs/en/build-with-claude/effort
  - https://platform.claude.com/docs/en/build-with-claude/overview
  - https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
  - https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai
  - https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry
  - https://platform.claude.com/docs/en/cli-sdks-libraries/overview
  - https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk
  - https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
  - https://platform.claude.com/docs/en/manage-claude/data-residency
  - https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training
  - https://platform.claude.com/docs/en/build-with-claude/thinking
  - https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback
  - https://platform.claude.com/docs/en/models/opus-5-5/migration-guide
  - https://platform.claude.com/docs/en/release-notes/overview (read 2026-10-31)
  - https://platform.claude.com/docs/en/api/migration-2026-10-21 (read 2026-10-31)
  - https://platform.claude.com/docs/en/build-with-claude/fast-mode (read 2026-10-31)
  - https://platform.claude.com/docs/en/build-with-claude/structured-outputs (read 2026-11-03)
  - https://platform.claude.com/docs/en/build-with-claude/batch-processing (read 2026-11-03)
  - https://platform.claude.com/docs/en/build-with-claude/files (read 2026-11-03)
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool (read 2026-11-03)
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool (read 2026-11-03)
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool (read 2026-11-03)
  - https://platform.claude.com/docs/en/agents-and-tools/mcp-connector (read 2026-11-03)
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling (read 2026-11-03)
  - https://platform.claude.com/docs/en/build-with-claude/message-threads (read 2026-11-03)
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming (read 2026-11-03)
  - https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions (read 2026-11-03)
  - https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/ruby (read 2026-11-03)
  - https://www.anthropic.com/claude-fable-and-mythos-5-1 (read 2026-11-03)
  - https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy (read 2026-11-03)
  - https://platform.claude.com/docs/en/build-with-claude/prompt-caching (read 2026-11-03)
  - https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed (read 2026-11-03)
---

# Anthropic API

first-party lab API

Anthropic trains the Claude models and sells them through its own HTTP API, which its documentation calls the Claude API (`https://api.anthropic.com`, with a console at platform.claude.com). The native surface is the Messages API. Anthropic also operates Claude Platform on AWS, Anthropic-managed Claude Models on Google Cloud and Claude in Microsoft Foundry; Amazon Bedrock and Google-managed Google Cloud offer partner-operated routes. [as-of 2026-11-03] (L) [ov-nov3] This file covers the direct API and says where the other routes differ; each route has its own file. [ov, feat]

## Models offered

Only Claude models, in four public classes. Haiku 5.5 replaces Haiku 4.5 as current after its 2026-10-07
release; Fable 5.1, Opus 5.5 and Sonnet 5.5 remain the other current models. [as-of 2026-10-09] (L)
[haiku-page] Earlier generations remain in the catalogue; the maker README records their lineage.
Mythos 5 and 5.1 have restricted access through verified organizations, outside this library's
GA/public-preview card scope. Anthropic describes Mythos 5.1 and Fable 5.1 as the same underlying model with different safeguards; those configurations can differ on blocked tasks. [as-of 2026-11-03] (L) [fable-release-nov3]

| Model file | API id | List price in / out per Mtok |
| --- | --- | --- |
| [Claude Fable 5.1](../models/anthropic/claude-fable-5-1.md) | `claude-fable-5-1` | $10 / $50 |
| [Claude Fable 5](../models/anthropic/claude-fable-5.md) | `claude-fable-5` | $10 / $50 |
| [Claude Opus 5.5](../models/anthropic/claude-opus-5-5.md) | `claude-opus-5-5` | $4 / $20 |
| [Claude Opus 5](../models/anthropic/claude-opus-5.md) | `claude-opus-5` | $5 / $25 |
| [Claude Sonnet 5.5](../models/anthropic/claude-sonnet-5-5.md) | `claude-sonnet-5-5` | $2 / $10 |
| [Claude Sonnet 5](../models/anthropic/claude-sonnet-5.md) | `claude-sonnet-5` | $2 / $10 |
| [Claude Haiku 5.5](../models/anthropic/claude-haiku-5-5.md) | `claude-haiku-5-5` | $0.10 / $0.50 up to 100k prompt tokens; $0.50 / $2.50 above |
| [Claude Haiku 4.5](../models/anthropic/claude-haiku-4-5.md) | `claude-haiku-4-5-20251001`, alias `claude-haiku-4-5` | $1 / $5 |

The price rows were checked on 2026-11-03 (L) [price-nov3]. Haiku 5.5 prompt length includes uncached input and cache reads/writes. [as-of 2026-11-03] (L) [price-nov3]

From the 4.6 generation on, every id is a pinned snapshot with no date suffix; Haiku 4.5 keeps a dated id and a dateless alias that resolves to it. The Models API (`GET /v1/models`) returns `max_input_tokens`, `max_tokens` and a `capabilities` object for each model, so a client can read limits instead of hard-coding them. Anthropic states retirement floors for its own platforms as "not sooner than" a date: Fable 5.1 2027-09-01, Opus 5.5 2027-09-22, Sonnet 5.5 2027-09-28, Haiku 4.5 2026-10-15. Haiku 5.5's floor is 2027-10-07 [as-of 2026-10-09] (L) [haiku-page]. Bedrock and Google Cloud set their own dates. The overview recommends starting with Opus 5.5 for most workloads and Fable 5.1 for demanding long-horizon work. The class lineage is in the [maker README](../models/anthropic/README.md). [models]

## API surface

- **Protocol.** Its own: `POST /v1/messages`, with content blocks, a separate top-level `system`, and tool use as `tool_use` and `tool_result` blocks. Other endpoints are Message Batches, Token Counting, Models, Files and Skills; Agents, Sessions and Environments (for Claude Managed Agents) are in beta. [ov] **Request size [as-of 2026-10-31].** On the first-party API, the limit for Messages and Token Counting rose from 32 MB to 128 MB on 2026-10-28. Batches stay at 256 MB, Files at 500 MB, and Sessions, Agents and Environments at 32 MB. A larger request gets a 413 `request_too_large` error. On 2026-10-31 the reported limit was 32 MB for Messages and Token Counting on Claude Platform on AWS, Claude Models on Google Cloud (Anthropic managed) and Microsoft Foundry. The current limit on those routes is UNVERIFIED. Google-managed Google Cloud lists a 30 MB request limit, and Bedrock lists 20 MB for the legacy integration. [as-of 2026-11-03] (L) [vtx-nov3, bed-legacy-nov3] L [ov-oct31, relnotes-oct31]
- **Auth.** `Authorization: Bearer <token>` or the legacy `x-api-key` header, plus `anthropic-version` and `content-type`. **[as-of 2026-10-31]** The page's example version is now `2026-10-21`, released on 2026-10-21. The new major SDK versions (Python 2.0.0, TypeScript 1.0.0, C# 13.0.0, Go 2.0.0, Java 3.0.0, PHP 1.0.0, Ruby 2.0.0) and `ant` CLI 2.0.0 send it by default, and earlier versions send `2023-06-01`. In `2026-10-21`, `temperature`, `top_p` and `top_k` return a 400 even at their default values, a `document` block placed directly in an assistant message returns a 400, and a user text block with a non-empty `citations` array returns a 400. The same rules apply to token counting and to each request in a Message Batch. On Bedrock the new version works only for Claude 4.7 and later models. The new SDKs also send the key as `Authorization: Bearer` in place of `x-api-key` (the Foundry clients still send `x-api-key`), and they are licensed under Apache 2.0 in place of MIT. L [ov-oct31, relnotes-oct31, mig-oct21] A key can be tied to one workspace; a multi-workspace key also sends `anthropic-workspace-id`. Workload Identity Federation exchanges a short-lived token through `POST /v1/oauth/token`. Beta features are switched on with an `anthropic-beta` header that carries a dated name. [ov]
- **Message threads [as-of 2026-11-03].** In beta since 2026-11-02 with `message-threads-2026-08-12`, the API keeps conversation state so later requests can send only new messages. The thread expires 5 minutes after its last request and is deleted within 1 hour after last use. It is available on the Claude API, Claude Platform on AWS, Anthropic-managed Google Cloud and Foundry. It is not eligible for ZDR or HIPAA readiness; its contents are held encrypted in memory and are not written to durable storage. L [threads-nov3, relnotes-nov3, ret-nov3]
- **Usage and cost reporting [as-of 2026-10-31].** The Usage and Cost Analytics API (`/v1/organizations/analytics/usage` and `/v1/organizations/analytics/cost`) went into beta on 2026-10-29 with the `analytics-usage-cost-2026-08-24` header. It can filter and group by model, workspace, API key and the user or service account behind a request. The older Usage and Cost API is now legacy but still supported. L [relnotes-oct31]
- **SDKs.** Official clients for Python, TypeScript, C#, Go, Java, PHP and Ruby, and an `ant` command-line tool. Cloud support uses a platform-specific package or client class; on Foundry, for example, Python has an `AnthropicFoundry` class in the main package, TypeScript a separate `@anthropic-ai/foundry-sdk` package, and the Ruby SDK has no Foundry support yet. [as-of 2026-11-03] (L) [sdk-nov3, fdy-nov3, ruby-nov3]
- **OpenAI-compatible endpoint [as-of 2026-11-03].** `https://api.anthropic.com/v1/` accepts OpenAI SDK chat-completions calls. Anthropic describes it as a route for testing and evaluating Claude. It ignores `reasoning_effort`, `strict` on function tools, `logprobs`, `seed` and the penalties; prompt caching is not supported. It accepts `response_format` only for `json_schema` with `strict: true`; other values return 400. It joins system and developer messages into one top-level system string; `n` must be 1. Audio and file input parts return 400. Thinking can be enabled through an extra body field, but thinking content is not returned; `thinking: {type: "adaptive"}` returns 400 on this route. L [oai-nov3]
- **Model ids on other routes.** On Claude Platform on AWS and Anthropic-managed Google Cloud, use the Claude API model ID; on Foundry send the deployment name, whose default is the model ID. On Google-managed Google Cloud, 4.6 and later IDs match the Claude API, while older models replace the hyphen before the snapshot date with `@` (for example `claude-haiku-4-5@20251001`). Bedrock base model IDs have an `anthropic.` prefix; inference profile IDs can add a `global.` or regional prefix, and older models also use a version suffix. [bed-legacy-nov3] [as-of 2026-11-03] (L) [ids-nov3, fdy-nov3, vtx-nov3, google-managed-nov3]

## Feature parity

Anthropic now lists platform support on each feature page. The following differences apply to the
Messages API [as-of 2026-11-03] (L):

- **Structured outputs** are listed on all supported platforms. The current Bedrock Messages guide
  also lists them; the older claim that only `InvokeModel` supports them is no longer supported.
  [structured-nov3, bed-nov3]
- **Message Batches** are available on the direct API, Claude Platform on AWS and
  Anthropic-managed Google Cloud. A batch has at most 100,000 requests or 256 MB. It expires if it has not finished
  processing within 24 hours; its results remain available for 29 days from creation. Fast mode and server-side
  fallback cannot be batched. [batch-nov3]
- **Files and code execution** are available on the direct API, Claude Platform on AWS,
  Anthropic-managed Google Cloud and Foundry hosted on Anthropic. **Web fetch** is also available
  on Foundry hosted on Azure, with the older tool version and reduced features. **Web search** is
  available on these routes and Google-managed Google Cloud; the latter and Foundry hosted on
  Azure use the basic tool without dynamic filtering. [files-nov3, code-nov3, fetch-nov3, search-nov3]
- **MCP connector** is in beta on the direct API, Claude Platform on AWS, Anthropic-managed Google
  Cloud and Foundry. **Programmatic tool calling** is listed on the direct API, Claude Platform on
  AWS and Foundry hosted on Anthropic; Haiku 4.5 does not support it. [mcp-nov3, program-nov3]
- **Server-side fallback** is in beta on the direct API and Anthropic-managed Google Cloud. Other
  routes can use client-side fallback. Haiku 5.5 does not support server-side fallback. [refuse-nov3]

Individual pages state model and route restrictions; availability on one route does not establish
availability on another. [feat-nov3]

Reasoning and effort. The 5-series models think adaptively and take `output_config.effort` with `low`, `medium`, `high`, `xhigh` and `max`; Haiku 4.5 has no effort control and uses manual extended thinking with a token budget. Defaults on the API are `high` for Fable 5.1, Fable 5, Opus 5, Sonnet 5.5 and Sonnet 5, and `medium` for Opus 5.5 and Haiku 5.5 [as-of 2026-10-09] (L) [effort-current]. Anthropic says effort changes thinking, text and tool-call volume together, and that it steers behaviour rather than enforcing a token count. A per-message effort change that keeps the prompt cache needs a beta header. It is supported on Fable 5.1, Opus 5.5, Opus 5, Sonnet 5.5 and Haiku 5.5 on the Claude API, Claude Platform on AWS and both Google Cloud routes; Bedrock supports it on Fable 5.1 and Opus 5.5. Sonnet 5.5 with `between_tools` and Haiku 5.5 with `disabled` cannot change effort per message; adaptive thinking permits the change. [as-of 2026-11-03] (L) [effort-nov3] Changing the top-level value between requests invalidates cached message blocks and can also invalidate tool and system caches, depending on the model; explicitly setting the default is equivalent to omitting it. [as-of 2026-11-03] (L) [cache-nov3] The thinking settings each model accepts, and the fixed-sampling rules, are in the [maker README](../models/anthropic/README.md). [effort, models]

Long context. Every 5-series model has 1M context and 128k synchronous output; Haiku 4.5 has 200k.
Haiku 5.5 raises prices above 100,000 prompt tokens; the other 5-series models use one rate across the
window. Batch output reaches 300k with a beta header on Opus 5.5, Opus 5, Sonnet 5.5, Sonnet 5 and
Haiku 5.5. [as-of 2026-10-09] (L) [haiku-page, price-current]

Vision and documents. Image and PDF input on every current model; no model produces images, audio or video. Other routes vary on URL and Files API sources; see the feature-specific pages above. [models, feat]

Streaming [as-of 2026-11-03]. The Messages API uses server-sent events. Anthropic lists fine-grained tool streaming on the Claude API, Claude Platform on AWS, Bedrock, Google-managed Google Cloud and Foundry; its availability list does not name Anthropic-managed Google Cloud. (L) [stream-nov3]

## Pricing

Per token. Accounts are funded by card or, for enterprise, by invoice, and new accounts get a small free credit. Input and output are priced per million tokens by model. A 5-minute cache write costs 1.25 times the input price, a 1-hour write 2 times, and a cache read 0.1 times, except 0.025 times on Fable 5.1 and 0.05 times on Opus 5.5 and Sonnet 5.5. Sonnet 5.5's
cache reads fell to $0.10 per Mtok on 2026-10-07 [as-of 2026-10-09] (L) [haiku-release]. The Batch API takes 50 percent off input and output. The 1M window carries no long-context surcharge except on Haiku 5.5: prompts over 100,000 tokens
pay the higher tier for the entire request, including cached input. [as-of 2026-10-09] (L) [price-current] `inference_geo: "us"` adds a factor of 1.1 to every category on Claude 4.6 and later models. Fast mode costs more per token and cannot be batched. On Opus 5.5 it costs $8 / $40 per million input / output tokens; on Opus 5 and Opus 4.8 it costs $10 / $50. Cache and data residency multipliers also apply. [as-of 2026-11-03] (L) [fast-nov3] **[as-of 2026-10-31]** On Opus 5.5 it left research preview on 2026-10-15 and needs no beta header; it runs on the Claude API, on Claude Models on Google Cloud (Anthropic managed) and on Microsoft Foundry for deployments hosted on Azure. On the Claude API, Evaluation-tier organisations need to move to Start, Build or Scale to use it. [as-of 2026-11-03] (L) [fast-nov3] On Opus 5 and Opus 4.8 it stays a research preview on the Claude API only, with the `fast-mode-2026-02-01` header. Fast mode on Opus 4.8 is deprecated and is removed on 2026-11-30; after that date, `speed: "fast"` on `claude-opus-4-8` returns an error. L [fast-oct31, relnotes-oct31] Server tools add their own charges: web search is $10 per 1,000 searches, web fetch has no fee beyond tokens, and code execution is free when the request includes `web_search_20260209` or later, or `web_fetch_20260209` or later, and otherwise billed by container time [as-of 2026-11-03] (L) [price-nov3] ($0.05 per container-hour after 1,550 free hours a month per organisation, with a 5-minute minimum). When files are included, container time is billed even if the tool is not called. [as-of 2026-11-03] (L) [price-nov3] Claude Managed Agents adds $0.08 per running session-hour. On Claude Platform on AWS and Foundry, usage is metered hourly to the cloud marketplace in Claude Consumption Units at $0.01 each, with no prepaid balance. Anthropic notes that Claude 4.7 and later models use a tokenizer that yields about 30 percent more tokens for the same text, so a price per token does not compare across that boundary. The model files also list per-model prices. [price]

## Limits and data

- **Rate limits.** Set per organisation and per model class, as requests, input tokens and output tokens per minute, refilled as a token bucket, so a short burst can trip a limit that a per-minute average would not. Tiers are Start, Build, Scale and Custom, with monthly spend caps of $500, $1,000 and $200,000 on the first three; new organisations may begin on a lower Evaluation tier. On 2026-10-03 the Start tier listed 1,000 requests, 2,000,000 input and 400,000 output tokens per minute for each of Opus 5.5, Opus 5, Sonnet 5.5, Sonnet 5 and Haiku 4.5, and one shared bucket of 1,000, 500,000 and 100,000 for Fable 5.1 and Fable 5 together. On 2026-11-03 the Start-tier page lists 4,000 requests per minute for the Fable 5.x shared bucket, Opus 5.5, Sonnet 5.5 and Haiku 5.5; the input and output limits are 500,000 / 100,000 for Fable and 2,000,000 / 400,000 for the other three. (L) [rl-nov3] Uncached input and cache writes count towards the input limit; cache reads do not, on every current model. Reaching a spend cap returns a 429 with no `retry-after`; reaching a cap you set yourself returns a 400. Limits are shared across `inference_geo` values, and a Rate Limits API reads the configured values. Priority Tier capacity is no longer sold. The page excludes Fable 5.1, Haiku 5.5, Opus 5.5, Opus 5, Sonnet 5.5 and Sonnet 5 from Priority Tier, among other models. [as-of 2026-11-03] (L) [st-nov3] [rl, st]
- **Regions.** A published list of supported countries and territories (over 150; Ukraine excludes Crimea, Donetsk and Luhansk; the list changes, so read it before relying on it). Inference runs globally by default. `inference_geo: "us"` pins it to US infrastructure on Claude 4.6 and later models, and a workspace can fix `allowed_inference_geos` and `default_inference_geo`. Workspace geo, which sets where data at rest and some tool processing sit, offers only `us`. [reg, dr]
- **Retention and training.** Conversation content is not retained by default, and Anthropic states that it does not train on commercial inputs and outputs unless the customer explicitly sends feedback or otherwise permits that use. [as-of 2026-11-03] (L) [train-nov3] Content flagged by its safety systems may be kept up to 2 years even under zero retention. Zero data retention is an agreement made per organisation through sales; it does not cover the Console, Managed Agents, the Batch API, the Files API, code execution, Agent Skills or the MCP connector, among others. Fable 5.1, Fable 5, Mythos 5.1 and Mythos 5 are "Covered Models" that need 30-day retention and are not available under ZDR unless Anthropic authorises it; an organisation under ZDR can turn on 30-day retention for a single workspace. A HIPAA-ready arrangement with a signed Anthropic BAA covers eligible direct API features and Foundry deployments hosted on Anthropic or Azure when the Azure subscription has the required HIPAA configuration; Claude Platform on AWS is not covered. The API generally rejects ineligible features with a 400, but the eligibility table names client-side tool exceptions that are accepted outside HIPAA readiness. [as-of 2026-11-03] (L) [ret-nov3] JSON schemas used for structured outputs are cached for up to 24 hours and must not hold health information. [ret, train, feat]
- **Other routes.** On Bedrock and Google-managed Google Cloud the cloud operator is the data processor, and retention and ZDR follow that operator's terms. Anthropic is the data processor on Claude Platform on AWS, Anthropic-managed Google Cloud and Foundry. Claude Platform on AWS and Anthropic-managed Google Cloud follow the direct API's retention policy, with ZDR on request. The present source does not state the previously listed Azure-hosted prompt and metadata exceptions; those details are UNVERIFIED. [as-of 2026-11-03] (L) [ret-nov3, fdy-nov3]

## Notes for agents and harnesses

- **Sampling parameters and prefill.** The Opus 5.5 migration guide says a non-default `temperature`, `top_p` or `top_k` returns a 400 on Opus 4.7 and later Opus models, and an assistant prefill returns a 400 on Opus 4.6 and later Opus models; the maker README records the same rules for the other 5-series models. **[as-of 2026-10-31]** That rule is for API version `2023-06-01`. In `2026-10-21` any value of the three parameters returns a 400 on every model, so a client that always sends `temperature: 1` breaks when it moves to the new SDK or header. A request that needs a non-default value on an older model that still accepts one can only stay on `2023-06-01`. L [mig-oct21] The OpenAI-compatible page still lists `temperature` as accepted from 0 to 1 (values above 1 are capped); it does not say how the two reconcile, and this was not tested. [mig, oai]
- **Effort mapping.** The 5-series has no token-count knob for thinking. `output_config.effort` is the control, and `max_tokens` is the hard ceiling that thinking tokens also count towards. Anthropic advises a large `max_tokens` at `high` and above, suggesting 64k as a start for `xhigh` and `max` on some models and 128k for agentic coding on Sonnet 5.5. It says a level name does not mean the same amount of thinking on two models and asks for a fresh sweep per model. An OpenAI-style client that sends `reasoning_effort` to the compatibility endpoint changes nothing, because the field is dropped. [effort, oai]
- **Thinking cannot always be turned off.** Fable 5.1, Fable 5 and Opus 5.5 reject `thinking: disabled` at any effort. Opus 5 and Haiku 5.5 accept it at `high` effort or below and return a 400 at `xhigh` and `max`
[as-of 2026-10-09] (L) [effort-current]. Sonnet 5.5 rejects `disabled` and offers `between_tools` as its lowest setting, valid up to `high` effort. [think, effort]
- **Thinking is hidden by default.** On the 5-series models and Opus 5.5 the `display` setting defaults to `omitted`, so thinking blocks arrive with an empty text field and only an encrypted `signature`; `display: "summarized"` returns a summary, and no setting returns the raw reasoning. Thinking blocks that go back in later turns must be sent unchanged. [think]
- **Forced tool choice** (`any` or `tool`) returns a 400 on Opus 5.5, including on the token-counting endpoint, and the migration guide points to `auto` with `strict: true` tools or structured outputs instead. The maker README records the same for Fable 5.1 and Sonnet 5.5. [mig]
- **A refusal is an HTTP 200.** Fable 5.1, Fable 5, Opus 5.5, Opus 5, Sonnet 5.5 and Haiku 5.5 carry safety classifiers
[as-of 2026-10-09] (L) [refuse-current]; a declined request returns `stop_reason: "refusal"` with `stop_details.category`, so a harness that checks only the status code treats it as success. Server-side fallback (the `fallbacks` parameter) is a beta on the direct API and Anthropic-managed Google Cloud [as-of 2026-11-03] (L) [refuse-nov3]; the SDK middleware and manual retry are client-side options on other routes. Haiku 5.5 has no
server-side fallback and no fallback credit; a retry after its refusal writes the fallback cache at full price.
[as-of 2026-10-09] (L) [refuse-current] [refuse, feat]
- **Features differ by route [as-of 2026-11-03].** Batch, Files, code execution, web fetch and the MCP connector differ by route. Anthropic lists structured outputs for the Bedrock Messages integration. [batch-nov3, files-nov3, code-nov3, fetch-nov3, mcp-nov3, bed-nov3]
- **Caching and throughput.** Cache reads do not count against the input-token limit, so a long shared prefix raises effective throughput. Changes to definitions in the top-level `tools` array invalidate the full prefix; changes to the system prompt invalidate its level and later messages. Changes to thinking settings or top-level effort invalidate message blocks, and can also invalidate tool and system caches depending on the model. An explicit default effort is equivalent to omission. [as-of 2026-11-03] (L) [cache-nov3]
- **Headers differ by route.** The direct API sends `anthropic-ratelimit-*` headers and may send `retry-after`; not every 429 has that header, and the spend-cap 429 does not. Foundry does not send Anthropic rate-limit headers. [as-of 2026-11-03] (L) [rl-nov3, fdy-nov3]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| ov | https://platform.claude.com/docs/en/api/overview | L | 2026-10-03 |
| rl | https://platform.claude.com/docs/en/api/rate-limits | L | 2026-10-03 |
| st | https://platform.claude.com/docs/en/api/service-tiers | L | 2026-10-03 |
| reg | https://platform.claude.com/docs/en/api/supported-regions | L | 2026-10-03 |
| models | https://platform.claude.com/docs/en/about-claude/models/overview | L | 2026-10-03 |
| price | https://platform.claude.com/docs/en/about-claude/pricing | L | 2026-10-03 |
| effort | https://platform.claude.com/docs/en/build-with-claude/effort | L | 2026-10-03 |
| feat | https://platform.claude.com/docs/en/build-with-claude/overview | L | 2026-10-03 |
| bed | https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock | L | 2026-10-03 |
| vtx | https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai | L | 2026-10-03 |
| fdy | https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry | L | 2026-10-03 |
| sdk | https://platform.claude.com/docs/en/cli-sdks-libraries/overview | L | 2026-10-03 |
| oai | https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk | L | 2026-10-03 |
| ret | https://platform.claude.com/docs/en/manage-claude/api-and-data-retention | L | 2026-10-03 |
| dr | https://platform.claude.com/docs/en/manage-claude/data-residency | L | 2026-10-03 |
| train | https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training | L | 2026-10-03 |
| think | https://platform.claude.com/docs/en/build-with-claude/thinking | L | 2026-10-03 |
| refuse | https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback | L | 2026-10-03 |
| mig | https://platform.claude.com/docs/en/models/opus-5-5/migration-guide | L | 2026-10-03 |

The sources below were read on 2026-10-09 for the corrected claims. The document was not fully re-verified.

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| haiku-page | https://platform.claude.com/docs/en/models/haiku-5-5/overview | L | 2026-10-09 |
| haiku-release | https://www.anthropic.com/claude-haiku-5-5 | L | 2026-10-09 |
| haiku-migration | https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide | L | 2026-10-09 |
| mythos-access | https://www.anthropic.com/claude/mythos | L | 2026-10-09 |
| price-current | https://platform.claude.com/docs/en/about-claude/pricing | L | 2026-10-09 |
| effort-current | https://platform.claude.com/docs/en/build-with-claude/effort | L | 2026-10-09 |
| refuse-current | https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback | L | 2026-10-09 |

The sources below were read on 2026-10-31 for the corrected claims. The document was not fully re-verified.

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| ov-oct31 | https://platform.claude.com/docs/en/api/overview | L | 2026-10-31 |
| relnotes-oct31 | https://platform.claude.com/docs/en/release-notes/overview | L | 2026-10-31 |
| mig-oct21 | https://platform.claude.com/docs/en/api/migration-2026-10-21 | L | 2026-10-31 |
| fast-oct31 | https://platform.claude.com/docs/en/build-with-claude/fast-mode | L | 2026-10-31 |

The sources below were read on 2026-11-03 for the corrected claims. The document was not fully re-verified.

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| oai-nov3 | https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk | L | 2026-11-03 |
| feat-nov3 | https://platform.claude.com/docs/en/build-with-claude/overview | L | 2026-11-03 |
| bed-nov3 | https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock | L | 2026-11-03 |
| structured-nov3 | https://platform.claude.com/docs/en/build-with-claude/structured-outputs | L | 2026-11-03 |
| batch-nov3 | https://platform.claude.com/docs/en/build-with-claude/batch-processing | L | 2026-11-03 |
| files-nov3 | https://platform.claude.com/docs/en/build-with-claude/files | L | 2026-11-03 |
| search-nov3 | https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool | L | 2026-11-03 |
| fetch-nov3 | https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool | L | 2026-11-03 |
| code-nov3 | https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool | L | 2026-11-03 |
| mcp-nov3 | https://platform.claude.com/docs/en/agents-and-tools/mcp-connector | L | 2026-11-03 |
| program-nov3 | https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling | L | 2026-11-03 |
| refuse-nov3 | https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback | L | 2026-11-03 |
| effort-nov3 | https://platform.claude.com/docs/en/build-with-claude/effort | L | 2026-11-03 |
| fast-nov3 | https://platform.claude.com/docs/en/build-with-claude/fast-mode | L | 2026-11-03 |
| price-nov3 | https://platform.claude.com/docs/en/about-claude/pricing | L | 2026-11-03 |
| ret-nov3 | https://platform.claude.com/docs/en/manage-claude/api-and-data-retention | L | 2026-11-03 |
| train-nov3 | https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training | L | 2026-11-03 |
| relnotes-nov3 | https://platform.claude.com/docs/en/release-notes/overview | L | 2026-11-03 |
| threads-nov3 | https://platform.claude.com/docs/en/build-with-claude/message-threads | L | 2026-11-03 |
| stream-nov3 | https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming | L | 2026-11-03 |
| rl-nov3 | https://platform.claude.com/docs/en/api/rate-limits | L | 2026-11-03 |
| st-nov3 | https://platform.claude.com/docs/en/api/service-tiers | L | 2026-11-03 |
| ids-nov3 | https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions | L | 2026-11-03 |
| ruby-nov3 | https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/ruby | L | 2026-11-03 |
| fable-release-nov3 | https://www.anthropic.com/claude-fable-and-mythos-5-1 | L | 2026-11-03 |
| bed-legacy-nov3 | https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy | L | 2026-11-03 |
| cache-nov3 | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | L | 2026-11-03 |
| ov-nov3 | https://platform.claude.com/docs/en/api/overview | L | 2026-11-03 |
| sdk-nov3 | https://platform.claude.com/docs/en/cli-sdks-libraries/overview | L | 2026-11-03 |
| fdy-nov3 | https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry | L | 2026-11-03 |
| vtx-nov3 | https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai | L | 2026-11-03 |
| google-managed-nov3 | https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed | L | 2026-11-03 |
