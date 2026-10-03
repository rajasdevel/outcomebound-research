---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: first-party lab API
sources:
  - https://docs.cohere.com/docs/models
  - https://docs.cohere.com/v2/docs/chat-api
  - https://docs.cohere.com/docs/compatibility-api
  - https://docs.cohere.com/docs/structured-outputs
  - https://docs.cohere.com/docs/reasoning
  - https://docs.cohere.com/docs/rate-limits
  - https://docs.cohere.com/docs/how-does-cohere-pricing-work
  - https://docs.cohere.com/docs/cohere-works-everywhere
  - https://cohere.com/enterprise-data-commitments
  - https://cohere.com/pricing
---

# Cohere

first-party lab API

Cohere trains the Command language models, the Embed and Rerank retrieval models and the Aya multilingual models, and sells them through its own API (`https://api.cohere.ai`, Chat API v2) and through private deployments and cloud platforms. Its focus is enterprise retrieval, tool use and multilingual work. The library has no Cohere maker folder and no Cohere model files, so this file links none; it is here because the API is commonly used and offers features the other first-party APIs here do not (rerank, embeddings, citations). [models, chat]

## Models offered

On 2026-10-03 the models page lists, by family: Command (`command-a-plus-05-2026`, 128k context and 64k output, described as Cohere's first mixture-of-experts model; `command-a-03-2025`, 256k and 8k; `command-r7b-12-2024`, `command-r-08-2024` and `command-r-plus-08-2024`, 128k and 4k), the specialised `command-a-translate-08-2025` (8k and 8k, 23 languages), `command-a-reasoning-08-2025` (256k context, 32k output) and `command-a-vision-07-2025` (128k, 8k), Embed (`embed-v5.0-pro` and `embed-v5.0-fast`, `embed-v4.0`, with older v3 models as legacy), Rerank (`rerank-v4.0-pro` and `rerank-v4.0-fast`, `rerank-v3.5`) and Aya (`c4ai-aya-expanse-32b`, 128k; `c4ai-aya-vision-32b`, 16k; and four 3.35B Tiny Aya models, `tiny-aya-global`, `-earth`, `-fire` and `-water`, 8k; the 8B Aya models were retired on 2026-04-04). Older Command models, including `command-r-03-2024`, `command-r-plus-04-2024`, `command-light` and `command`, were deprecated on 2025-09-15. The page puts the Command models on the Chat endpoint and gives Embed, Rerank, Parse and the audio models their own endpoints. [models]

No model file in this library covers a Cohere model, so the table that other provider files carry is left out. [models]

## API surface

- **Protocol.** Its own Chat API v2 at `https://api.cohere.ai/v2/chat`, with roles `user`, `assistant`, `system` and `tool`, a response carrying a finish reason (`COMPLETE` or `MAX_TOKENS`) and billed-token counts, plus documents for retrieval-augmented answers with citations, tools and streaming. Embed, Rerank and Parse have their own endpoints. [chat, models]
- **OpenAI-compatible endpoint.** `https://api.cohere.ai/compatibility/v1` with chat completions, embeddings and audio transcriptions. Not supported: `store`, `logit_bias`, `n`, `parallel_tool_calls` and audio modalities; some audio file types (MP4, M4A, WEBM) are rejected; Cohere's own connectors, documents and citation options are unavailable through it. `response_format` and `tools` are supported, and `reasoning_effort` accepts only `none` and `high`, mapped to Cohere's thinking switch. [compat]
- **Auth.** A bearer API key (the examples read `CO_API_KEY`); trial and production keys differ in limits. [chat, rates]
- **SDKs.** TypeScript, Python, Go and Java; Go and Java are marked "soon" for Bedrock, SageMaker and OCI, and the compatibility page labels them beta. [compat, everywhere]
- **Model ids.** Family name, version and a month-year stamp (`command-a-03-2025`); the newest uses `command-a-plus-05-2026`. [models]

## Feature parity

First-party; the Cohere platform has the full feature set and the clouds subsets. [everywhere]

- **Reasoning and effort.** On reasoning models thinking is on by default, can be disabled with `thinking: {"type": "disabled"}` and takes a token budget; the page recommends 31K for maximum reasoning and leaving at least 1K tokens for the reply. The reasoning appears in separate thinking content blocks. The reasoning page names `command-a-reasoning-08-2025` and no effort parameter on the native API; the compatibility endpoint maps `reasoning_effort` `none` and `high` onto the thinking switch. [reasoning, compat]
- **Tools.** Function calling and `strict_tools`, which constrains tool names and parameters; at most 200 fields across all tools per call, every tool needs at least one required parameter, and strict tools work only in Chat API v2. [structured]
- **Structured output.** JSON mode and JSON schema mode. In schema mode the top-level type must be an object and every object needs at least one required field; schema-free JSON mode is capped at five levels of nesting, needs an explicit instruction to produce JSON, and does not work with RAG. The first few requests with a schema add latency until it is cached. Supported on Command A+, Command A, Command R+ and Command R. [structured]
- **Retrieval features.** Documents with citations on the native Chat API (not on the compatibility endpoint), plus Embed (text and image) and Rerank as separate endpoints. [chat, compat]
- **Caching.** Not found in the pages read.
- **Batch.** Not found in the pages read (a Datasets API exists).
- **Long context.** 256k on `command-a-03-2025` and `command-a-reasoning-08-2025`, 128k on Command A+, R, R+, R7B and Vision, and 8k to 16k on Translate, Aya Vision and Tiny Aya. [models]
- **Vision.** `command-a-vision-07-2025`, `c4ai-aya-vision-32b` and the multimodal embedding models. [models]
- **Streaming.** Supported. [chat]
- **On other platforms.** Bedrock, SageMaker and Azure lack `classify` and `summarize`; OCI lacks `generate`, `generate_stream` and `rerank`; chat and embed are consistent everywhere. [everywhere]

## Pricing

Per token for generative models with input and output priced separately, per search for Rerank and per embedded token for Embed. The page distinguishes billed tokens from total tokens, since some tokens Cohere adds internally are not charged. Trial keys are free but limited; production keys are pay-as-you-go; private deployments are a separate arrangement. The public pricing page read on 2026-10-03 shows rates only for legacy Command models in its FAQ and hourly or monthly Model Vault pricing for Embed and Rerank, with no per-token rates for current models, so none are given here. [pricing, models, price-page]

## Limits and data

- **Rate limits.** Trial keys: 20 requests a minute on chat models, 1,000 API calls a month in total, and lower limits on some endpoints (5 a minute for audio, 10 for rerank). Production keys: 500 requests a minute on the standard chat models (Command A, R+, R, R7B), no monthly cap; text Embed 2,000 inputs a minute on both key types; Rerank 1,000 requests a minute on production. For Command A+, A Reasoning, A Translate and A Vision, production keys work like trial keys until sales grants access. Higher limits go through support. [rates]
- **Regions.** The commitments page gives no data-residency or regional-hosting terms; they are left to the customer agreement. [commitments]
- **Retention and training.** On the SaaS platform, logged prompts and generations are deleted after 30 days unless law, contract or a suspected violation requires longer. By default prompts and generations may be used to train Cohere models; the page says a user can opt out at any time with the Data Controls toggle in the dashboard settings. Zero data retention (no logging of prompts or generations) can be requested by enterprise customers and needs additional usage commitments and Cohere's approval. Cohere offers a DPA for SaaS customers and states ISO 27001 and SOC 2 Type II certification. In private deployments (VPC or on-premises) and on third-party clouds, Cohere states it receives no prompts or generations. [commitments]

## Notes for agents and harnesses

- **Default is training on.** Unless the Data Controls toggle is switched off, prompts and generations on the SaaS platform may be used for training; Cohere states it receives no prompts or generations in private deployments or on third-party clouds. [commitments]
- **The compatibility endpoint drops retrieval features.** Documents, connectors and citations are unavailable through it, and they are much of what the native API adds. [compat]
- **Strict tools need V2 and a required parameter.** A tool with only optional parameters cannot be strict, and the 200-field cap spans all tools in one call. [structured]
- **Thinking budget.** Reasoning is a toggle plus a token budget, not a level, so an effort-style map has no direct target on the native API. [reasoning]
- **Trial limits are small.** 1,000 calls a month and 20 requests a minute on chat stop an agent quickly. [rates]
- **Retrieval models are separate.** Rerank and Embed have their own endpoints, prices and limits, apart from chat. [models, rates]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| models | https://docs.cohere.com/docs/models | L | 2026-10-03 |
| chat | https://docs.cohere.com/v2/docs/chat-api | L | 2026-10-03 |
| compat | https://docs.cohere.com/docs/compatibility-api | L | 2026-10-03 |
| structured | https://docs.cohere.com/docs/structured-outputs | L | 2026-10-03 |
| reasoning | https://docs.cohere.com/docs/reasoning | L | 2026-10-03 |
| rates | https://docs.cohere.com/docs/rate-limits | L | 2026-10-03 |
| pricing | https://docs.cohere.com/docs/how-does-cohere-pricing-work | L | 2026-10-03 |
| everywhere | https://docs.cohere.com/docs/cohere-works-everywhere | L | 2026-10-03 |
| commitments | https://cohere.com/enterprise-data-commitments | L | 2026-10-03 |
| price-page | https://cohere.com/pricing | L | 2026-10-03 |
