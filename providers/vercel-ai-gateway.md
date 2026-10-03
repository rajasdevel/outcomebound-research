---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: router or gateway
sources:
  - https://vercel.com/docs/ai-gateway
  - https://vercel.com/docs/ai-gateway/models-and-providers
  - https://vercel.com/docs/ai-gateway/pricing
  - https://vercel.com/docs/ai-gateway/security-and-compliance/zdr
  - https://vercel.com/docs/ai-gateway/models-and-providers/reasoning
  - https://vercel.com/docs/ai-gateway/models-and-providers/automatic-caching
  - https://vercel.com/docs/ai-gateway/rate-limits
  - https://vercel.com/docs/ai-gateway/sdks-and-apis
---

# Vercel AI Gateway

router or gateway

Vercel AI Gateway is a managed gateway, run by Vercel, that sits in front of many model providers and gives an application one key, one bill, request logs, spend budgets and provider failover. It can be called from any infrastructure, not only from Vercel deployments, and is available on all Vercel plans. It is one of the managed counterparts to the self-run proxy in [litellm.md](litellm.md) and the marketplace-style router in [openrouter.md](openrouter.md). [home]

## Models offered

The catalogue covers many makers, and a model can be served by several providers, including its own maker, a cloud and an inference host. The docs give `anthropic/claude-opus-5`, `anthropic/claude-sonnet-5` and `openai/gpt-6-astra` as example ids, and the ZDR changelog links name Claude Opus 5.5 and Sonnet 5.5 as available. Makers in this library that the pages read name or imply include [Anthropic](../models/anthropic/README.md), [OpenAI](../models/openai/README.md), [Google](../models/google/README.md), [xAI](../models/xai/README.md), [DeepSeek](../models/deepseek/README.md), [Alibaba](../models/alibaba/README.md), [Moonshot](../models/moonshot/README.md), [MiniMax](../models/minimax/README.md), [Meta](../models/meta/README.md) and [Mistral](../models/mistral/README.md). The pages also use `spacexai/grok-4.5` as an example id, and list "SpaceXAI" as a provider; whether that is a new name for xAI is not stated in the pages read. The live list is `GET https://ai-gateway.vercel.sh/v1/models`, which needs no key and returns ids, context windows, prices and reasoning controls; `GET /v1/models/{creator}/{model}/endpoints` returns per-provider price, supported parameters, uptime, throughput and latency. The gateway also serves image, video, speech, transcription, realtime, embedding and reranking models. [models, home, zdr]

## API surface

- **Protocols.** Several formats share one key, one set of model ids and one routing layer: the AI SDK (`@ai-sdk/gateway`, and Vercel's Python AI SDK in public beta), OpenAI Chat Completions (`https://ai-gateway.vercel.sh/v1/chat/completions`), the OpenAI Responses API and the provider-neutral OpenResponses format (both at `/v1/responses`), Anthropic Messages (`/v1/messages`, base URL `https://ai-gateway.vercel.sh`), and a Cohere-compatible Rerank API. Embeddings use `/v1/embeddings`. [sdk]
- **Auth.** An AI Gateway API key as a bearer token (the Messages format also accepts `x-api-key`), or, on Vercel deployments, an OpenID Connect token. Your own provider keys can be added (BYOK). [sdk, home]
- **Model ids.** `creator/model-name`, for example `anthropic/claude-sonnet-5`. [models]
- **Gateway options.** Gateway-specific settings travel in `providerOptions.gateway` in the request body (an `extra_body` field in the OpenAI and Anthropic Python SDKs); the TypeScript OpenAI SDK needs the field spread in because its types do not declare it. Examples are `zeroDataRetention`, `caching` and provider ordering. [sdk, zdr]
- **Agents.** A Vercel CLI command (`vercel ai-gateway setup`) configures supported coding agents to route through the gateway. [sdk]

## Feature parity

Which features pass depends on the request format, and the pages say to check per-model support in the catalogue rather than assume it. [sdk]

- **Reasoning and effort.** The catalogue's `reasoning_options` field lists, per model, an effort list, a token-budget range or a toggle; a missing entry means unspecified, not unsupported. Each format has its own field: AI SDK 7 `reasoning` (which does not accept `max`), Chat Completions `reasoning_effort` or a nested `reasoning` object (the nested one wins when both are sent), Messages `thinking` plus `output_config.effort`, Responses `reasoning.effort`. The gateway translates across makers. For OpenAI reasoning models the shared translation maps `max` to `xhigh`. For Claude 4.7 and later it sets adaptive thinking, mapping `minimal` to `low` and `max` to `xhigh`; for Claude 4.6 `minimal` becomes `low` and `xhigh` and `max` become `max`; for Claude 4.5 and earlier (budget-based) the effort becomes a share of maximum output tokens (about 10 percent for `minimal`, 20 for `low`, 50 for `medium` and 80 for both `high` and `xhigh`), clamped to 1,024 to 64,000 tokens; for Gemini 3 and later `low` stays `low` and every other level becomes `high`; for Gemini 2.5 fixed budgets apply (0 for `none`, the model's minimum for `minimal`, 1,024 for `low`, 8,192 for `medium`, 24,576 for `high`, `xhigh` and `max`). A token-budget request to an OpenAI reasoning model is turned into a named effort, so no exact cap is enforced, and Claude 4.7 and later do not accept token budgets. Setting `output_config.effort` or `providerOptions.anthropic.effort` bypasses the shared translation and keeps native `max`. Provider-specific options override a top-level `reasoning` value and are never merged with it. The page says a successful request does not prove the effort level was honoured, and that a positive reasoning-token count shows only that reasoning happened. [reason]
- **Tools, structured output, vision.** Tool calling, structured output (`output` in the AI SDK, `response_format`, `output_config.format` or `text.format`, by format) and image input are available on each format, with different payload shapes that must not be copied between formats. Whether a given model supports them is in the catalogue. [sdk]
- **Prompt caching.** With `caching: 'auto'` the gateway adds `cache_control` markers for explicit-cache providers (Anthropic direct, via Vertex and via Bedrock; MiniMax; Alibaba): on the last message and on the message before the last user message, plus an optional anchor (`cache_anchor_items`, Responses format). Without it, requests pass unmodified, so Anthropic needs `caching: 'auto'` or manual markers. OpenAI, Google and DeepSeek cache implicitly. Anthropic's default lifetime is five minutes; `cache_ttl: '1h'` on the Responses format selects one hour, at 2 times the base input price to write against 1.25 times for five minutes. An `x-session-affinity` header, forwarded on all compatibility formats, asks providers to keep cache locality; it does not change routing or guarantee a hit. [cache]
- **Batch.** No batch API appears in the pages read; whether one exists is `UNVERIFIED`.
- **Long context and streaming.** Context windows are per model in the catalogue. Streaming (server-sent events) is available on all compatible endpoints. [sdk, models]
- **Web search.** The gateway lists a web-search option under models and providers; its behaviour was not read. [models]

## Pricing

The gateway states no markup and no platform fee on tokens, including for BYOK: the customer pays the provider's list price from prepaid AI Gateway Credits, with auto top-up available. The payment processor's fees are the customer's; enterprise teams can be invoiced. Some models are priced below list for all teams, and custom volume discounts exist. Every team gets a monthly free credit that applies to a subset of models, with lower per-model rate limits; buying credits moves the team to the paid tier and ends the free credit. BYOK needs the paid tier, and a failed BYOK request that falls back to Vercel's credentials is billed to credits. Add-on charges apply when a capability is enabled: custom reporting ($0.075 per 1,000 tag, user or quota-entity writes and $5 per 1,000 queries), a team-wide provider allowlist ($0.10 per 1,000 successful requests, Pro and Enterprise), team-wide zero data retention ($0.10 per 1,000 requests, charged only on successful responses that return usage; per-request ZDR costs nothing extra; both Pro and Enterprise only), and trace drains ($0.05 per 1,000 traces and $0.50 per GB of egress, Pro and Enterprise, billed as Drains usage on the plan rather than from credits). Budgets can cap spend per team, project, key or member; a hit budget returns 402 with `quota_for_entity_exceeded`. Budgets cover spend on Vercel's own credentials only (BYOK spend is metered separately), and the overview calls them soft caps. Prices per model are on the catalogue and a model page shows differences between providers. [price, rate, home]

## Limits and data

- **Rate limits.** The free tier has a lower, per-model limit; the paid tier has none from the gateway, so only the upstream provider's limits apply, also with BYOK. A 429 may come from either side and may carry the provider's own body; some carry `retry-after`. The page gives no numbers and says limits change, and custom limits are available on request. A BYOK request that fails can fall back to the gateway's own credentials, which are rate-limited and billed to credits. [rate]
- **Retention and training.** The gateway says it keeps no prompts or outputs and deletes data once a request completes. By default it does not route on a provider's retention policy. ZDR is available on Pro and Enterprise only. With `zeroDataRetention: true` per request or a team-wide toggle (either one enforces it, and it also applies to fallbacks), requests go only to providers with which Vercel has zero-retention agreements, and an unknown provider counts as non-compliant; a request with no eligible provider fails with `no_providers_available` (HTTP 400). ZDR is a superset of disallowing prompt training. BYOK keys are skipped under ZDR unless marked compliant by you, who then takes responsibility for the contract. Per the page, one Claude model (`claude-fable-5`) has no ZDR option on any provider because Anthropic keeps prompts and completions for 30 days for misuse detection, and does not train on them. Provider caching is ZDR-compliant only as far as the provider is, and where a provider's ZDR policy excludes certain models or tools, the gateway does not fail those requests. The ZDR list read on 2026-10-03 names, among others, Anthropic, Azure, Baseten, Bedrock, DeepInfra, Fireworks, Google Vertex AI, Groq, Mistral, Nebius, OpenAI, Together AI and xAI. [zdr]
- **Regions.** The docs index mentions regional inference under security and compliance; the page was not read, so region options are `UNVERIFIED`. [home]

## Notes for agents and harnesses

- **Format follows the client.** The SDKs page points Claude Code and Anthropic SDK users to the Messages format for native feature support, and OpenAI SDK users to Chat Completions or Responses. The reasoning, cache and structured-output fields differ between formats, and the page says payloads are not to be copied between them. [sdk]
- **Effort translation is lossy.** The shared translation collapses Gemini 3 efforts to `low` or `high` and maps `max` to `xhigh` for OpenAI models and Claude 4.7 and later. The reasoning page names the native option (`output_config.effort` or `providerOptions.anthropic.effort`) as the way to keep an exact level, and a provider-options entry per provider for requests that can fall back to another provider. [reason]
- **Claude caching is off unless asked for.** Without `caching: 'auto'` or manual markers, Anthropic prompts are not cached through the gateway. The automatic markers sit at the tail, so a client that rewrites the middle of the prompt (summarising or pruning) loses cache reads unless it sets an anchor, and the caching page says a strictly one-shot workload pays the write premium with no read to recover it. [cache]
- **Routing is visible in the response.** The overview describes setting a provider order and reading the response metadata to see which provider served a request; under ZDR the `planningReasoning` field also shows how providers were filtered. [home, zdr]
- **Usage shows that reasoning happened, not how much was asked for.** Anthropic counts thinking tokens as output tokens with no separate breakdown. [reason]
- **Budgets are soft caps.** The overview links to soft-cap budget semantics for cases that need zero overshoot, and BYOK spend does not count toward budgets. [home]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| home | https://vercel.com/docs/ai-gateway | L | 2026-10-03 |
| models | https://vercel.com/docs/ai-gateway/models-and-providers | L | 2026-10-03 |
| price | https://vercel.com/docs/ai-gateway/pricing | L | 2026-10-03 |
| zdr | https://vercel.com/docs/ai-gateway/security-and-compliance/zdr | L | 2026-10-03 |
| reason | https://vercel.com/docs/ai-gateway/models-and-providers/reasoning | L | 2026-10-03 |
| cache | https://vercel.com/docs/ai-gateway/models-and-providers/automatic-caching | L | 2026-10-03 |
| rate | https://vercel.com/docs/ai-gateway/rate-limits | L | 2026-10-03 |
| sdk | https://vercel.com/docs/ai-gateway/sdks-and-apis | L | 2026-10-03 |
