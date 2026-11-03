---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: router or gateway
sources:
  - https://openrouter.ai/docs/quickstart
  - https://openrouter.ai/docs/features/provider-routing
  - https://openrouter.ai/docs/api-reference/limits
  - https://openrouter.ai/docs/features/privacy-and-logging
  - https://openrouter.ai/docs/features/zdr
  - https://openrouter.ai/docs/guides/best-practices/reasoning-tokens
  - https://openrouter.ai/docs/guides/best-practices/prompt-caching
  - https://openrouter.ai/docs/guides/features/structured-outputs
  - https://openrouter.ai/docs/guides/features/tool-calling
  - https://openrouter.ai/docs/guides/overview/models
  - https://openrouter.ai/docs/api-reference/overview
  - https://openrouter.ai/docs/api-reference/responses/overview
  - https://openrouter.ai/docs/guides/coding-agents/claude-code-integration
  - https://openrouter.ai/docs/faq
  - https://openrouter.ai/pricing
  - https://openrouter.ai/collections/free-models/
  - https://openrouter.ai/blog/announcements/batch-api/
---

# OpenRouter

router or gateway

OpenRouter is a hosted service with one HTTP endpoint in front of many model providers. A request names a model, and OpenRouter picks one of the providers that serve it, falls back to another if that one fails, and bills the account once. The catalogue spans the closed-model makers and the open-weight hosts, so one key reaches models that would otherwise need a key per maker. This file covers the hosted service; the self-run gateway of a similar shape is in [litellm.md](litellm.md). [quick, routing]

## Models offered

OpenRouter does not host models itself in the sense of a lab: each model is served by one or more upstream "providers" (the maker's own API, a cloud, or an inference host), and the model page lists those endpoints with their own price, context length and supported parameters. Makers in the library that appear in the catalogue include [Anthropic](../models/anthropic/README.md), [OpenAI](../models/openai/README.md), [Google](../models/google/README.md), [xAI](../models/xai/README.md), [Mistral](../models/mistral/README.md), [DeepSeek](../models/deepseek/README.md), [Alibaba](../models/alibaba/README.md), [Moonshot](../models/moonshot/README.md) and [MiniMax](../models/minimax/README.md). Which of the individual model files in scope is available at a given moment is a property of the live catalogue, which `GET /api/v1/models` returns; this file does not list it, because the set changes without notice. The models guide gives the catalogue as more than 400 models and notes that a model can appear before its documentation is complete. [models, quick]

Catalogue entries carry the fields an integrator needs to select a route: `context_length`, `supported_parameters`, `pricing`, input and output modalities, the top provider's own limits and an optional `expiration_date` for a model being retired. Filters on the models page and the API cover output type (text, image, video, audio, embeddings) and supported parameters. [models]

**GPT-6.1 Terra [as-of 2026-11-03].** OpenRouter's model page lists standard rates of $1 input, $0.05 cache read, $1.25 cache write and $5 output per million tokens. Its batch page lists $0.50, $0.025, $0.625 and $2.50 respectively. The model page lists EU in-region routing through Azure at $1.20 input and $6 output per million tokens on Business or Enterprise. These are catalog figures; route-specific terms and account access were not tested. L [terra-nov03] [terra-batch-nov03].

## API surface

- **Protocols.** The primary surface is OpenAI-compatible: `POST /api/v1/chat/completions` at `https://openrouter.ai/api/v1`, usable with the OpenAI SDK by changing the base URL. A Responses-style endpoint is documented as a drop-in alternative; it is stateless, and a request that sets `store: true` or `previous_response_id` is rejected. OpenRouter also accepts input in the Anthropic Messages format: its Claude Code guide sets `ANTHROPIC_BASE_URL` to `https://openrouter.ai/api` so that Claude Code talks to it in its own protocol, with no local proxy. [quick, resp, cc]
- **Auth.** A bearer token (`Authorization: Bearer <key>`). Optional headers `HTTP-Referer` and `X-OpenRouter-Title` attribute traffic to an application. Keys can carry their own spending cap. [quick, limits]
- **SDKs.** OpenRouter publishes `@openrouter/sdk` (TypeScript), `openrouter` (Python) and an agent SDK, `@openrouter/agent`, for tool loops and state; the OpenAI SDK also works. [quick]
- **Model ids.** The form is `author/slug` (the single-model lookup is `GET /api/v1/model/{author}/{slug}`). A leading tilde (`~openai/gpt-sol-latest` in the quickstart) is a "latest" alias that resolves to the newest model in that family. Deprecated names redirect to their replacements. A suffix selects a variant. Catalogue variants such as `:free` are separate entries with their own price and limits; routing variants such as `:nitro` (sort by throughput, request the priority service tier) and `:floor` (sort by price, request the flex tier) change only provider selection. A `:batch` variant exists for the Batch API, which the pages read here do not describe. [quick, models, routing, faq]
- **Request extras.** A `models` array gives an ordered fallback list. A `plugins` array enables web search, PDF parsing, response healing and context compression. Assistant-role prefill is accepted. `finish_reason` is normalised to `tool_calls`, `stop`, `length`, `content_filter` or `error`, with the provider's own value in `native_finish_reason`. `GET /api/v1/generation` returns token counts and cost for a past request. [api]

## Feature parity

OpenRouter's pages describe features it normalises; the maker's own API is the reference for what each one means. Support is per endpoint, not per model, so the same model can differ between providers behind OpenRouter. [routing, tools, so]

- **Reasoning and effort [as-of 2026-11-03].** A unified `reasoning` object expresses reasoning controls on Chat Completions and Responses; the Messages API also accepts native `thinking` and `output_config.effort` fields. It takes `effort` (`max`, `xhigh`, `high`, `medium`, `low`, `minimal`, `none`), `max_tokens` (a token budget), `exclude` (Chat Completions only: reason but do not return the reasoning; the tokens are still billed) and `enabled`. For OpenAI models the effort level passes through; for Claude, the reasoning budget is a share of `max_tokens` (about 95 percent for `max` and `xhigh`, 80 for `high`, 50 for `medium`, 20 for `low` and 10 for `minimal`), with a floor of 1,024 and a ceiling of 128,000 tokens; for Gemini 3 the effort becomes a `thinkingLevel` of the same name, except that `xhigh` becomes `high`. `enabled: true` alone uses default parameters; the model catalogue may give the default effort. [reason-nov03] The response's `reasoning_details` array holds summaries, encrypted content or raw text; for tool use the page says to pass back either `message.reasoning` or the whole `reasoning_details` array, with the sequence of reasoning blocks unchanged. [reason]
- **Tools.** OpenAI-style function calling for models whose endpoints support it; `tool_choice` accepts `auto`, `none` or a named function, and `parallel_tool_calls` defaults to true for most models and can be set false. Support depends on the endpoint (`supported_parameters=tools` filters the catalogue). Each provider shows a tool-call error rate on its model page, which also feeds an "Auto Exacto" routing option. [tools]
- **Structured output.** `response_format` with `type: "json_schema"` and `strict`. Enforcement varies: some providers constrain decoding, others treat the schema as a hint. Setting `require_parameters: true` routes only to endpoints that support every parameter in the request. A response-healing plugin repairs malformed JSON in non-streaming requests. [so]
- **Prompt caching.** Automatic for OpenAI, Grok, Moonshot, Groq, DeepSeek, Z.AI and Google Gemini 2.5; explicit `cache_control` for Anthropic Claude, Alibaba Qwen and other Gemini models. Anthropic's default life is five minutes, with a one-hour option (`"ttl": "1h"`) at a higher write price. OpenRouter uses sticky routing, sending later requests to the endpoint that holds the cache, but only where that provider's cache-read price is below its normal prompt price; a sticky session ends after 10 minutes without a request. A `session_id` (up to 256 characters, in the body or an `x-session-id` header) turns sticky routing on from the first successful request. Usage reports `cached_tokens`, `cache_write_tokens` and `cache_discount` under `prompt_tokens_details`. [cache]
- **Batch [as-of 2026-11-03].** The asynchronous Batch API accepts chat completions, Responses, Messages and embeddings request shapes. Each batch uses one provider, selected by default from eligible batch endpoints by price. Batch inputs and results are kept for 30 days or until the batch is deleted. Images and files must be public URLs; audio, video and OpenRouter web-search plugin requests are not supported. [batch-nov03]
- **Long context, vision, streaming.** Context limits are per endpoint in the catalogue. Text, images and PDFs (as URLs or base64) are accepted as input on models that support them. Streaming is supported on the chat endpoint, including with structured output. [faq, so, models]
- **Not passed through as the maker defines it.** Reasoning is expressed in OpenRouter's schema, not the maker's, and the Claude Code guide itself says the tool is built for Anthropic models and may not work correctly with others; its fast mode applies only to specific Opus versions on Anthropic's own provider. [reason, cc]

## Pricing

[as-of 2026-11-03]

OpenRouter states that it passes through each provider's price with no markup on inference. The pricing page lists platform fees on credit purchases of 5.5 percent for Standard, 8 percent for Business and custom rates for Enterprise. [pricing-nov03] Bring-your-own-key use is free up to a monthly allowance and then costs 5 percent of the standard price; the FAQ gives the allowance as $25,000 for pay-as-you-go accounts. New accounts get a small free allowance, and `:free` model variants cost nothing but are rate-limited and described as not suited to production. Price differs per endpoint, and a routing sort (`price`, `throughput`, `latency`) or `max_price` constrains it. Default routing compares price, throughput, latency and reliability using recent traffic. [faq, routing-nov03]

## Limits and data

- **Rate limits [as-of 2026-11-03].** Free variants: 20 requests a minute and 50 a day, rising to 1,000 a day after buying $10 in credits; the higher cap starts at $9 to account for fees, and failed attempts count. [free-nov03] For paid models the limit is the account's credit balance, an optional per-key cap and an in-flight hold on the estimated cost of running requests; a negative balance blocks everything, including free models. A 402 credit error can carry a reason: `in_flight_budget_exhausted` (retry after `Retry-After`), `weight_exceeds_budget` (the single request's estimated cost exceeds the whole budget; the page suggests a lower `max_tokens` or more credits). The limits page gives HTTP 403 for an exhausted key, workspace or guardrail budget, with `openrouter_key_limit` identifying a key limit. [limits-nov03] A 429 can come from OpenRouter, in which case it carries `X-RateLimit-*` headers, or from the upstream provider. `GET /api/v1/key` reports remaining credit and the free-model day counter. [limits]
- **Retention and training.** OpenRouter shows each provider's retention and training policy and lets an account or a request filter by them; it does not itself apply the policy by default, and says provider policies do not bind what OpenRouter does with prompts. Account settings control routing to providers that may train on data, separately for paid and free models. `data_collection: "deny"` restricts a request to providers that do not store or train. [privacy, routing]
- **Zero data retention [as-of 2026-11-03].** `zdr: true` in the request's provider preferences can also permit Safety Retention endpoints unless account privacy settings or a guardrail require ZDR only. Safety Retention endpoints can retain prompts and responses to prevent abuse, but do not train on them. The policy applies to model inference endpoints; a list of ZDR endpoints is at `/api/v1/endpoints/zdr`. [routing-nov03] It covers inference routing only, not plugins or tools such as web search. Batch inputs and results are retained for 30 days or until deleted. [batch-nov03] In-memory prompt caching does not disqualify an endpoint. [zdr]
- **Regions.** Business and Enterprise plans can use `eu.openrouter.ai` or `us.openrouter.ai`, which the documentation says keep prompts and completions inside the region; model availability varies by region. [privacy]

## Notes for agents and harnesses

- **Route choice changes behaviour [as-of 2026-11-03].** The default weighs price, throughput, latency and reliability across endpoints that may run different quantisations and support different parameters. [routing-nov03] The routing page offers `quantizations`, `only`, `ignore`, `order` and `allow_fallbacks: false` to fix the choice, and `require_parameters: true` so that a request is not sent to an endpoint that would drop a parameter such as `response_format` or a reasoning control. [routing, so]
- **One effort field, translated per maker.** OpenRouter's `reasoning.effort` is translated differently for each maker, and for Claude it becomes a share of `max_tokens`. A request whose `max_tokens` leaves little room after the reasoning share can return a short or empty answer (an inference from the budget rule, not a documented case). [reason]
- **Reasoning must be returned on tool turns.** The reasoning page says the reasoning blocks are to be passed back unchanged between tool calls; a client that drops them loses the model's reasoning state for models that use it. [reason]
- **`exclude` hides reasoning but not its cost [as-of 2026-11-03].** On Chat Completions, excluded reasoning tokens are billed and generally count against the output limit. [reason-nov03]
- **Cache hits depend on staying on one endpoint.** Sticky routing applies only where cache reads are cheaper; a changed provider order or a fallback starts a new cache. `cache_write_tokens` shows the write cost. [cache]
- **The Responses endpoint is stateless.** A client built on `previous_response_id` or stored responses gets a 400 error here. [resp]
- **Fallback lists can change the model.** With a `models` array the answer can come from a model other than the first one named; the response's model field records which one served it. [api]
- **Aliases move.** A `~...-latest` alias resolves to a newer model without any change on the client side, so runs that must repeat use an exact id. [quick]
- **Claude Code setup.** The guide sets `ANTHROPIC_AUTH_TOKEN` to the OpenRouter key and `ANTHROPIC_API_KEY` to an empty string, and says a cached Anthropic login must be removed with `/logout` first. [cc]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| quick | https://openrouter.ai/docs/quickstart | L | 2026-10-03 |
| routing | https://openrouter.ai/docs/features/provider-routing | L | 2026-10-03 |
| limits | https://openrouter.ai/docs/api-reference/limits | L | 2026-10-03 |
| privacy | https://openrouter.ai/docs/features/privacy-and-logging | L | 2026-10-03 |
| zdr | https://openrouter.ai/docs/features/zdr | L | 2026-10-03 |
| reason | https://openrouter.ai/docs/guides/best-practices/reasoning-tokens | L | 2026-10-03 |
| cache | https://openrouter.ai/docs/guides/best-practices/prompt-caching | L | 2026-10-03 |
| so | https://openrouter.ai/docs/guides/features/structured-outputs | L | 2026-10-03 |
| tools | https://openrouter.ai/docs/guides/features/tool-calling | L | 2026-10-03 |
| models | https://openrouter.ai/docs/guides/overview/models | L | 2026-10-03 |
| api | https://openrouter.ai/docs/api-reference/overview | L | 2026-10-03 |
| resp | https://openrouter.ai/docs/api-reference/responses/overview | L | 2026-10-03 |
| cc | https://openrouter.ai/docs/guides/coding-agents/claude-code-integration | L | 2026-10-03 |
| faq | https://openrouter.ai/docs/faq | L | 2026-10-03 |

Partial check, read 2026-10-27 (L):

- [terra-oct27] <https://openrouter.ai/openai/gpt-6.1-terra>.
- [terra-batch-oct27] <https://openrouter.ai/openai/gpt-6.1-terra:batch>.

Partial check, read 2026-11-03 (L):

- [terra-nov03] <https://openrouter.ai/openai/gpt-6.1-terra>.
- [terra-batch-nov03] <https://openrouter.ai/openai/gpt-6.1-terra:batch>.
- [pricing-nov03] <https://openrouter.ai/pricing>.
- [free-nov03] <https://openrouter.ai/collections/free-models/>.
- [batch-nov03] <https://openrouter.ai/blog/announcements/batch-api/>.
- [limits-nov03] <https://openrouter.ai/docs/api_reference/limits>.
- [reason-nov03] <https://openrouter.ai/docs/guides/best-practices/reasoning-tokens>.
- [routing-nov03] <https://openrouter.ai/docs/guides/routing/provider-selection>.
