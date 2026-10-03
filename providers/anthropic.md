---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: first-party lab API
sources:
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
---

# Anthropic API

first-party lab API

Anthropic trains the Claude models and sells them through its own HTTP API, which its documentation calls the Claude API (`https://api.anthropic.com`, with a console at platform.claude.com). The native surface is the Messages API. The same company also runs Claude Platform on AWS and Claude in Microsoft Foundry, and Amazon and Google sell the models on Amazon Bedrock and Google Cloud. This file covers the direct API and says where the other routes differ; each route has its own file. [ov, feat]

## Models offered

Only Claude models, in four classes. The overview lists Claude Fable 5.1, Claude Opus 5.5, Claude Sonnet 5.5 and Claude Haiku 4.5 as current, and Fable 5, Opus 5 and Sonnet 5 (and older Opus 4.x and Sonnet 4.6) as legacy. Mythos 5.1, Mythos 5 and Mythos Preview appear on the pricing page as invitation-only (Project Glasswing) and have no model file. [models, price]

| Model file | API id | List price in / out per Mtok |
| --- | --- | --- |
| [Claude Fable 5.1](../models/anthropic/claude-fable-5-1.md) | `claude-fable-5-1` | $10 / $50 |
| [Claude Fable 5](../models/anthropic/claude-fable-5.md) | `claude-fable-5` | $10 / $50 |
| [Claude Opus 5.5](../models/anthropic/claude-opus-5-5.md) | `claude-opus-5-5` | $4 / $20 |
| [Claude Opus 5](../models/anthropic/claude-opus-5.md) | `claude-opus-5` | $5 / $25 |
| [Claude Sonnet 5.5](../models/anthropic/claude-sonnet-5-5.md) | `claude-sonnet-5-5` | $2 / $10 |
| [Claude Sonnet 5](../models/anthropic/claude-sonnet-5.md) | `claude-sonnet-5` | $2 / $10 |
| [Claude Haiku 4.5](../models/anthropic/claude-haiku-4-5.md) | `claude-haiku-4-5-20251001`, alias `claude-haiku-4-5` | $1 / $5 |

From the 4.6 generation on, every id is a pinned snapshot with no date suffix; Haiku 4.5 keeps a dated id and a dateless alias that resolves to it. The Models API (`GET /v1/models`) returns `max_input_tokens`, `max_tokens` and a `capabilities` object for each model, so a client can read limits instead of hard-coding them. Anthropic states retirement floors for its own platforms as "not sooner than" a date: Fable 5.1 2027-09-01, Opus 5.5 2027-09-22, Sonnet 5.5 2027-09-28, Haiku 4.5 2026-10-15. Bedrock and Google Cloud set their own dates. The overview recommends starting with Opus 5.5 for most workloads and Fable 5.1 for demanding long-horizon work. The class lineage is in the [maker README](../models/anthropic/README.md). [models]

## API surface

- **Protocol.** Its own: `POST /v1/messages`, with content blocks, a separate top-level `system`, and tool use as `tool_use` and `tool_result` blocks. Other endpoints are Message Batches, Token Counting, Models, Files and Skills; Agents, Sessions and Environments (for Claude Managed Agents) are in beta. Request size limits are 32 MB for Messages, 256 MB for Batches and 500 MB for Files. [ov]
- **Auth.** `Authorization: Bearer <token>` or the legacy `x-api-key` header, plus `anthropic-version` (the page's example is `2023-06-01`) and `content-type`. A key can be tied to one workspace; a multi-workspace key also sends `anthropic-workspace-id`. Workload Identity Federation exchanges a short-lived token through `POST /v1/oauth/token`. Beta features are switched on with an `anthropic-beta` header that carries a dated name. [ov]
- **SDKs.** Official clients for Python, TypeScript, C#, Go, Java, PHP and Ruby, and an `ant` command-line tool. Each SDK reaches the cloud routes through a platform-specific package or client class; on Foundry, for example, Python has an `AnthropicFoundry` class in the main package, TypeScript a separate `@anthropic-ai/foundry-sdk` package, and the Ruby SDK has no Foundry support yet. [sdk, fdy]
- **OpenAI-compatible endpoint.** `https://api.anthropic.com/v1/` accepts the OpenAI SDK's chat-completions calls. Anthropic describes it as meant for testing and comparing models and not as a long-term production route. It ignores `reasoning_effort`, `response_format`, `strict` on tools, `logprobs`, `seed`, the penalties and prompt caching; it hoists every system and developer message into one system string; `n` must be 1; audio input is dropped; thinking can be switched on with an extra `thinking` body field but the thinking content is not returned. [oai]
- **Model ids on other routes.** The same id on Claude Platform on AWS, Microsoft Foundry (where the deployment name is what is sent, by default the id) and Google Cloud (`claude-haiku-4-5@20251001` for Haiku); Bedrock prefixes `anthropic.`. [models, bed, vtx, fdy]

## Feature parity

This is the maker's own API, so parity here means what the same models lose on the other routes. Anthropic's feature table is the source; the direct API column is the full feature set. [feat]

| Feature | Claude API | Amazon Bedrock (Messages endpoint) | Google Cloud | Microsoft Foundry |
| --- | --- | --- | --- | --- |
| Messages API, adaptive thinking, effort, caching (5 minute and 1 hour), citations, token counting | yes | yes | yes | yes |
| Structured outputs (`output_config.format`, `strict` tools) | yes | no (only on the older InvokeModel integration, for 4.x models) | yes | yes |
| Batch API (50 percent discount) | yes | no | no | no |
| Files API and URL sources for images and documents | yes | no | no | Hosted on Anthropic only |
| Web search tool | yes | no | yes | yes (basic version when hosted on Azure) |
| Code execution tool | yes | no | no | Hosted on Anthropic only |
| Web fetch tool | yes | no | no | yes (basic version when hosted on Azure) |
| MCP connector (beta), Agent Skills, programmatic tool calling | yes | no | no | MCP beta yes; Skills and programmatic calling on Anthropic hosting only |
| Server-side fallback on refusal (beta) | yes | no (client-side pattern) | no (client-side pattern) | no (client-side pattern) |
| Data residency | `inference_geo` parameter | by endpoint chosen | by endpoint chosen | Data Zone deployment |
| Claude Managed Agents | yes | no | no | no |

Reasoning and effort. The 5-series models think adaptively and take `output_config.effort` with `low`, `medium`, `high`, `xhigh` and `max`; Haiku 4.5 has no effort control and uses manual extended thinking with a token budget. Defaults on the API are `high` for Fable 5.1, Fable 5, Opus 5, Sonnet 5.5 and Sonnet 5, and `medium` for Opus 5.5. Anthropic says effort changes thinking, text and tool-call volume together, and that it steers behaviour rather than enforcing a token count. A per-message effort change that keeps the prompt cache needs a beta header and is limited to Fable 5.1, Opus 5.5, Opus 5 and Sonnet 5.5; changing the top-level value between requests restarts the cache. The thinking settings each model accepts, and the fixed-sampling rules, are in the [maker README](../models/anthropic/README.md). [effort, models]

Long context. A 1M-token window at one per-token price on every 5-series model, and 200k for Haiku 4.5. Output is 128k on the synchronous API, and up to 300k on the Batch API for Opus 5.5, Opus 5, Sonnet 5.5 and Sonnet 5 with a beta header. [models, price]

Vision and documents. Image and PDF input on every current model; no model produces images, audio or video. Other routes vary on URL and Files API sources (table above). [models, feat]

Streaming. Server-sent events on the Messages API; fine-grained streaming of tool inputs is listed on all five routes. [feat]

## Pricing

Per token. Accounts are funded by card or, for enterprise, by invoice, and new accounts get a small free credit. Input and output are priced per million tokens by model. A 5-minute cache write costs 1.25 times the input price, a 1-hour write 2 times, and a cache read 0.1 times, except 0.025 times on Fable 5.1 and 0.05 times on Opus 5.5. The Batch API takes 50 percent off input and output. The 1M window carries no long-context surcharge. `inference_geo: "us"` adds a factor of 1.1 to every category on Claude 4.6 and later models. Fast mode (research preview; Opus 5.5, Opus 5 and Opus 4.8; direct API only) costs more per token and cannot be batched. Server tools add their own charges: web search is $10 per 1,000 searches, web fetch has no fee beyond tokens, and code execution is free alongside current web search or fetch and otherwise billed by container time ($0.05 per container-hour after 1,550 free hours a month per organisation, with a 5-minute minimum). Claude Managed Agents adds $0.08 per running session-hour. On Claude Platform on AWS and Foundry, usage is metered hourly to the cloud marketplace in Claude Consumption Units at $0.01 each, with no prepaid balance. Anthropic notes that Claude 4.7 and later models use a tokenizer that yields about 30 percent more tokens for the same text, so a price per token does not compare across that boundary. Per-model prices are on the model files, not repeated here. [price]

## Limits and data

- **Rate limits.** Set per organisation and per model class, as requests, input tokens and output tokens per minute, refilled as a token bucket, so a short burst can trip a limit that a per-minute average would not. Tiers are Start, Build, Scale and Custom, with monthly spend caps of $500, $1,000 and $200,000 on the first three; new organisations may begin on a lower Evaluation tier. On 2026-10-03 the Start tier listed 1,000 requests, 2,000,000 input and 400,000 output tokens per minute for each of Opus 5.5, Opus 5, Sonnet 5.5, Sonnet 5 and Haiku 4.5, and one shared bucket of 1,000, 500,000 and 100,000 for Fable 5.1 and Fable 5 together. Uncached input and cache writes count towards the input limit; cache reads do not, on every current model. Reaching a spend cap returns a 429 with no `retry-after`; reaching a cap you set yourself returns a 400. Limits are shared across `inference_geo` values, and a Rate Limits API reads the configured values. Priority Tier capacity is no longer sold, and the page lists Fable 5.1, Opus 5.5, Opus 5, Sonnet 5.5 and Sonnet 5 as not covered by it. [rl, st]
- **Regions.** A published list of supported countries and territories (over 150; Ukraine excludes Crimea, Donetsk and Luhansk; the list changes, so read it before relying on it). Inference runs globally by default. `inference_geo: "us"` pins it to US infrastructure on Claude 4.6 and later models, and a workspace can fix `allowed_inference_geos` and `default_inference_geo`. Workspace geo, which sets where data at rest and some tool processing sit, offers only `us`. [reg, dr]
- **Retention and training.** Conversation content is not retained by default, and Anthropic states that it does not train on commercial inputs and outputs, except feedback a user chooses to send. Content flagged by its safety systems may be kept up to 2 years even under zero retention. Zero data retention is an agreement made per organisation through sales; it does not cover the Console, Managed Agents, the Batch API, the Files API, code execution, Agent Skills or the MCP connector, among others. Fable 5.1, Fable 5, Mythos 5.1 and Mythos 5 are "Covered Models" that need 30-day retention and are not available under ZDR unless Anthropic authorises it; an organisation under ZDR can turn on 30-day retention for a single workspace. A HIPAA-ready arrangement with a signed BAA exists for the direct API only (not Claude Platform on AWS or Foundry), and it rejects features outside the eligible list with a 400. JSON schemas used for structured outputs are cached for up to 24 hours and must not hold health information. [ret, train, feat]
- **Other routes.** On Bedrock and Google Cloud the cloud operator is the data processor, and retention and ZDR follow that operator's terms. On Claude Platform on AWS and Foundry Anthropic's data terms apply: Claude Platform on AWS follows the direct API's retention policy with ZDR on request, and on Foundry Anthropic acts as an independent processor for Microsoft, with prompts and completions of Azure-hosted deployments kept within Azure except flagged content and usage metadata. [ret, fdy]

## Notes for agents and harnesses

- **Sampling parameters and prefill.** The Opus 5.5 migration guide says a non-default `temperature`, `top_p` or `top_k` returns a 400 on Opus 4.7 and later Opus models, and an assistant prefill returns a 400 on Opus 4.6 and later Opus models; the maker README records the same rules for the other 5-series models. The OpenAI-compatible page still lists `temperature` as accepted from 0 to 1 (values above 1 are capped); it does not say how the two reconcile, and this was not tested. [mig, oai]
- **Effort mapping.** The 5-series has no token-count knob for thinking. `output_config.effort` is the control, and `max_tokens` is the hard ceiling that thinking tokens also count towards. Anthropic advises a large `max_tokens` at `high` and above, suggesting 64k as a start for `xhigh` and `max` on some models and 128k for agentic coding on Sonnet 5.5. It says a level name does not mean the same amount of thinking on two models and asks for a fresh sweep per model. An OpenAI-style client that sends `reasoning_effort` to the compatibility endpoint changes nothing, because the field is dropped. [effort, oai]
- **Thinking cannot always be turned off.** Fable 5.1, Fable 5 and Opus 5.5 reject `thinking: disabled` at any effort. Opus 5 accepts it at `high` effort or below and returns a 400 at `xhigh` and `max`. Sonnet 5.5 rejects `disabled` and offers `between_tools` as its lowest setting, valid up to `high` effort. [think, effort]
- **Thinking is hidden by default.** On the 5-series models and Opus 5.5 the `display` setting defaults to `omitted`, so thinking blocks arrive with an empty text field and only an encrypted `signature`; `display: "summarized"` returns a summary, and no setting returns the raw reasoning. Thinking blocks that go back in later turns must be sent unchanged. [think]
- **Forced tool choice** (`any` or `tool`) returns a 400 on Opus 5.5, including on the token-counting endpoint, and the migration guide points to `auto` with `strict: true` tools or structured outputs instead. The maker README records the same for Fable 5.1 and Sonnet 5.5. [mig]
- **A refusal is an HTTP 200.** Fable 5.1, Fable 5, Opus 5.5, Opus 5 and Sonnet 5.5 carry safety classifiers; a declined request returns `stop_reason: "refusal"` with `stop_details.category`, so a harness that checks only the status code treats it as success. Server-side fallback (the `fallbacks` parameter) is a beta on the direct API only; the SDK middleware and a manual retry with fallback credit work on every route. [refuse, feat]
- **Features differ by route.** Batch, Files, code execution, web fetch, the MCP connector and structured outputs differ by cloud (table above). A harness that moves from the direct API to Bedrock loses the Batch API and structured outputs. [feat, bed]
- **Caching and throughput.** Cache reads do not count against the input-token limit, so a long shared prefix raises effective throughput. The cache restarts when the system prompt, the tools, the thinking settings or top-level effort change. [rl, effort]
- **Headers differ by route.** The direct API sends `anthropic-ratelimit-*` headers and `retry-after`; Foundry does not send the Anthropic rate-limit headers. [rl, fdy]

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
