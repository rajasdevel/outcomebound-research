---
last_checked: 2026-10-03
volatility: VOLATILE (the hosted model list, prices, rate limits and the Workers AI and AI Gateway billing rules changed repeatedly in 2026)
kind: cloud platform
sources:
  - https://developers.cloudflare.com/workers-ai/
  - https://developers.cloudflare.com/workers-ai/models/
  - https://developers.cloudflare.com/ai/models/
  - https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/
  - https://developers.cloudflare.com/workers-ai/features/prompt-caching/
  - https://developers.cloudflare.com/workers-ai/features/batch-api/
  - https://developers.cloudflare.com/workers-ai/features/json-mode/
  - https://developers.cloudflare.com/workers-ai/features/function-calling/
  - https://developers.cloudflare.com/workers-ai/features/reject-if-busy/
  - https://developers.cloudflare.com/workers-ai/platform/pricing/
  - https://developers.cloudflare.com/workers-ai/platform/limits/
  - https://developers.cloudflare.com/workers-ai/platform/data-usage/
  - https://developers.cloudflare.com/workers-ai/changelog/
  - https://developers.cloudflare.com/ai-gateway/features/unified-billing/
  - https://developers.cloudflare.com/changelog/post/2026-09-01-billing-and-model-names/
  - https://developers.cloudflare.com/workers-ai/models/gpt-oss-120b/
  - https://developers.cloudflare.com/workers-ai/models/glm-5.3/
  - https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/
  - https://developers.cloudflare.com/workers-ai/models/gemma-4-26b-a4b-it/
  - https://developers.cloudflare.com/ai-gateway/usage/providers/
---

# Cloudflare Workers AI

cloud platform; Cloudflare's serverless inference service, which runs open-weight models on GPUs in Cloudflare's network and is called from Workers, Pages or the Cloudflare REST API. Since 2026 Cloudflare presents it with AI Gateway as one surface: the same `env.AI.run()` binding and `/ai/v1` REST routes reach models Cloudflare hosts (Workers AI proper) and third-party models from OpenAI, Anthropic, Google, xAI and others that the gateway proxies and bills through Cloudflare credits. Cloudflare labels the two groups "Cloudflare-hosted" and "Third-party" in its model catalogue. The Workers AI catalogue lists 69 Cloudflare-hosted entries across all task types (speech, image, embeddings and text), the unified catalogue 233 (the Workers AI overview page still says 50+ open-source models). Workers AI in its older sense, models on GPUs that Cloudflare runs, corresponds to the hosted rows only, so the service combines the properties of an inference host and a gateway. Everything below was read on 2026-10-03 from Cloudflare documentation (class L).

## Models offered

Text-generation rows from the catalogues, which also list speech, image, video and embedding models.

- **Cloudflare-hosted (Workers AI).** OpenAI [gpt-oss-120b](../models/openai/gpt-oss-120b.md) and [gpt-oss-20b](../models/openai/gpt-oss-20b.md); Moonshot [Kimi K2.7 Code](../models/moonshot/kimi-k2.7-code.md) and K2.6; Z.ai [GLM-5.3](../models/zai/glm-5.3.md), [GLM-5.3-Flash](../models/zai/glm-5.3-flash.md), [GLM-5.2](../models/zai/glm-5.2.md) and GLM-4.7-Flash; Google [Gemma 4 26B A4B](../models/google/gemma-4-26b-a4b-it.md); Alibaba Qwen [Qwen3.8-27B](../models/alibaba/qwen3.8-27b.md), QwQ 32B, Qwen3 30B A3B and Qwen2.5 Coder; DeepSeek V4 Pro 0813, V4 Flash 0731 and R1 distill 32B; NVIDIA Nemotron 3 120B A12B; Meta Llama 4 Scout, Llama 3.3 70B, 3.2 and 3.1 builds and Llama Guard 3; Mistral Small 3.1; IBM Granite 4.0 H Micro; Swiss AI Apertus; two Cloudflare-authored text models named Clef and Clef Flash; and regional-language models.
- **Third-party through the unified catalogue.** Anthropic Claude (Fable 5.1 and 5, Opus 5.5 and 5, Sonnet 5, Haiku 4.5 and earlier Opus and Sonnet, with no Sonnet 5.5 row); OpenAI (GPT-6 Astra, Sol and Luna, GPT-5.6 Sol, Terra and Luna, GPT-5.5, 5.4, 5.1, 5, GPT-4.1, GPT-4o, o3 and o4-mini); Google Gemini (3.8 Flash, 3.7 Flash, 3.6 Flash, 3.5 Flash, 3.5 Flash-Lite, 3.1 Pro, 3.1 Flash-Lite, 3 Flash and 2.5); xAI Grok (4.7, 4.6, 4.5, 4.3, 4.20); Moonshot Kimi K3; MiniMax M3 and M2.7; Alibaba Qwen3.8 Max, 3.7 Plus, 3.7 Max, Qwen3 Max and Qwen3.5 397B; DeepSeek V4 Pro; Thinking Machines Inkling (with a 256K variant). Library files exist for [Claude Fable 5.1](../models/anthropic/claude-fable-5-1.md), [Fable 5](../models/anthropic/claude-fable-5.md), [Opus 5.5](../models/anthropic/claude-opus-5-5.md), [Opus 5](../models/anthropic/claude-opus-5.md), [Sonnet 5](../models/anthropic/claude-sonnet-5.md), [Haiku 4.5](../models/anthropic/claude-haiku-4-5.md), [GPT-6 Astra](../models/openai/gpt-6-astra.md), [GPT-6 Sol](../models/openai/gpt-6-sol.md), [GPT-6 Luna](../models/openai/gpt-6-luna.md), GPT-5.6 Sol, [Terra](../models/openai/gpt-5.6-terra.md), [Luna](../models/openai/gpt-5.6-luna.md), [Gemini 3.8 Flash](../models/google/gemini-3.8-flash.md), [3.7 Flash](../models/google/gemini-3.7-flash.md), [3.5 Flash-Lite](../models/google/gemini-3.5-flash-lite.md), [3.1 Flash-Lite](../models/google/gemini-3.1-flash-lite.md), [3.1 Pro](../models/google/gemini-3.1-pro-preview.md), [Grok 4.7](../models/xai/grok-4.7.md), [Grok 4.6](../models/xai/grok-4.6.md), [Kimi K3](../models/moonshot/kimi-k3.md), [MiniMax M3](../models/minimax/MiniMax-M3.md), [MiniMax M2.7](../models/minimax/MiniMax-M2.7.md), [Qwen3.8 Max](../models/alibaba/qwen3.8-max.md), [Qwen3.7 Plus](../models/alibaba/qwen3.7-plus.md), [DeepSeek V4 Pro](../models/deepseek/deepseek-v4-pro.md) and [Inkling](../models/other/inkling.md).
- **Not found in the catalogues:** GPT-6.1 Sol, Claude Sonnet 5.5, Qwen3.8 Flash, Mistral Large 3 and Nemotron 3 Ultra. The card here for Grok 4.6 names Cloudflare as a route, which matches the third-party rows only.
- **Deprecations.** A 2026-05-30 sweep removed many older Llama, Mistral, Gemma and Phi builds and aliased Kimi K2.5 to K2.6, which costs more (changelog).

## API surface

- **Routes.** The native `ai/run/{model}` REST route and the `env.AI.run()` binding; OpenAI-compatible endpoints at `https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1`, with `/chat/completions` for most text models and `/embeddings` for embedding models. A Responses route (`/v1/responses`) exists for gpt-oss only, non-streaming. For the gpt-oss models `ai/run` also detects a Chat Completions, legacy Completions or Responses body (changelog, 2026-02-17). The endpoints work with AI Gateway features such as caching, retries and fallback, and the Vercel AI SDK has a provider.
- **Auth.** A Cloudflare API token as a bearer token and the account id in the path. For third-party models the gateway resolves credentials in order: a provider key on the request, then a stored key (BYOK), then Cloudflare-managed credentials billed to credits. A gateway setting can block that fall-through.
- **Model ids.** Hosted models are `@cf/<maker>/<model>` (for example `@cf/openai/gpt-oss-120b`, `@cf/moonshotai/kimi-k2.7-code`, `@cf/zai-org/glm-5.3`), with a few `@hf/` entries. Third-party models are `provider/model` such as `openai/gpt-4.1-mini` or `anthropic/claude-haiku-4.5`; a September 2026 change standardised model names in logs and invoices on that pattern.
- **Provider-native passthrough** through AI Gateway covers OpenAI, Anthropic, Google AI Studio, Google Vertex AI, xAI and Groq, authenticated with `cf-aig-authorization`.

## Feature parity

For hosted models, against each maker's own API; most cells are per-model page facts.

- **Reasoning and effort.** Model pages list their own controls: gpt-oss `low`, `medium` (default) and `high`; GLM-5.3 `low`, `high` and `max` (default), with `none`, `minimal`, `medium` and `xhigh` aliased to `max` and reasoning not disableable; Kimi K2.7 Code reasoning always on. Kimi K2.6 uses `chat_template_kwargs.thinking` to control reasoning and returns it in a `reasoning` field (changelog).
- **Tools.** Function calling in an OpenAI-like shape, with parallel calls on supported models. Cloudflare also documents an embedded form where an `@cloudflare/ai-utils` helper runs the tool code alongside the inference call, and a traditional form. Model pages mark function calling per model.
- **Structured output.** JSON mode with `response_format` (`json_object` or `json_schema`) for a short list of older models; it does not stream, and Cloudflare says it cannot guarantee schema adherence and returns an error when the schema cannot be met. Newer model pages (Kimi K2.7 Code, GLM-5.3) describe structured outputs as a model capability without the same list.
- **Prompt caching.** Prefix caching is on by default for selected models, reported as a discounted cached-input rate. The `x-session-affinity` header routes a session to the same model instance to raise hit rates; a one-token difference ends the cached prefix.
- **Batch.** An asynchronous Batch API: requests are queued, the call returns a request id to poll, and the total payload must stay under 10 MB; Cloudflare says batch requests are fulfilled eventually instead of failing for lack of capacity. Supported models are tagged in the catalogue (the gpt-oss-120b and Gemma 4 26B pages list Batch).
- **Long context.** Per model: gpt-oss-120b 128,000 tokens, Gemma 4 26B A4B 256,000, Kimi K2.7 Code 262,144, GLM-5.3 1,048,576, GLM-5.2 262,144 (changelog).
- **Vision.** Per model: Kimi K2.7 Code, Gemma 4 26B and Llama 3.2 11B Vision accept images.
- **Streaming.** Supported on chat endpoints; Responses requests must set `stream: false`.
- **Capacity control.** A `rejectIfBusy` option (in `options` on REST and Chat Completions, in the third argument of `env.AI.run()`) makes a synchronous request fail with HTTP 429 and internal code 3040 instead of waiting in a capacity queue.

## Pricing

- **Neurons.** Workers AI bills in neurons, a measure of GPU work, at $0.011 per 1,000 above a free allocation of 10,000 neurons per day on both the Free and Paid Workers plans; the pricing page shows per-model prices in tokens (or other units) and in neurons, which are equivalent, and the numbers are not repeated here. Allocation resets at 00:00 UTC.
- **Paid-only models.** Some hosted models (Kimi K2.6 and K2.7 Code, the GLM-5 builds, DeepSeek V4 Flash 0731 and V4 Pro 0813 as listed) need the Workers Paid plan or prepaid AI Gateway credits.
- **AI Gateway credits (Unified Billing).** Prepaid credits that fund third-party models and, since 2026, Workers AI too. Cloudflare charges a 5 percent fee on credit purchases and passes provider token prices through without markup. Machine Payments with a stablecoin wallet is an alternative. Spend-limit rules can cap spend by model, provider or metadata.
- **Invoices.** Since 2026-09-01 AI Gateway monthly invoices show one total per model instead of separate input and output lines.

## Limits and data

- **Rate limits.** Default per task type in requests per minute: text generation 300, text embeddings 3,000 (bge-large 1,500), summarization 1,500, text classification 2,000, image classification and object detection 3,000, speech recognition, image-to-text, text-to-image and translation 720. Paid-only models have 20 requests per minute per account and model, or 50 with prepaid AI Gateway credits. Local-mode Wrangler runs count against the limits. Custom limits and private models go through a requirements form.
- **Regions.** Models run on Cloudflare's global network; the pages read do not let a customer choose a Region or give a residency commitment.
- **Data use.** Cloudflare says it neither creates nor trains the models; customer content (inputs, outputs, embeddings, training data) is the customer's, is not made available to other customers, and is not used to train models on Workers AI or to improve Cloudflare or third-party services without explicit consent. It is stored only if the customer also uses a storage product such as R2, KV, Durable Objects or Vectorize.
- **Zero data retention for third-party models.** Unified Billing traffic can be routed through provider endpoints that do not retain prompts or responses; this applies only to requests using Cloudflare-managed credentials, depends on the model, and does not stop AI Gateway's own logging, which is a separate setting.
- **Third-party data handling.** For proxied models the provider's terms and retention rules apply beyond the points above; the pages read do not summarise them per provider.

## Notes for agents and harnesses

- Cloudflare says prefix caching works only when a request reaches the instance holding the cached prefix, and that a stable identifier in `x-session-affinity` raises the chance of that; requests without it may miss the cache and the discount.
- Accepted effort values differ by model page: GLM-5.3 maps `none`, `minimal`, `medium` and `xhigh` to `max`, so a request that sends `medium` runs at the highest level without an error.
- JSON mode and structured outputs differ by model, and JSON mode cannot stream; streaming with schema output depends on what the model page lists.
- Default text-generation limits are 300 requests a minute, and 20 per account and model for the paid-only models; prepaid credits raise the paid-model cap to 50.
- A request without provider credentials to a third-party model can fall through to Unified Billing and charge credits; the `Require provider credentials` gateway setting or the `cf-aig-no-wholesale` header prevents that.
- Hosted and third-party models share routes but not guarantees: a third-party id goes through a gateway to the maker's service, while an `@cf/` id runs on Cloudflare GPUs.
- `rejectIfBusy` makes a request fail at once instead of queueing; Cloudflare notes that OpenAI clients which strip unknown fields never send it.

## Sources

Read 2026-10-03 (class L, Cloudflare documentation; URLs in the frontmatter):

- Workers AI overview, models, unified AI catalogue
- OpenAI-compatible endpoints, prompt caching, Batch API, JSON mode, function calling, reject-if-busy
- Pricing, limits, data usage, changelog
- AI Gateway unified billing and the 2026-09-01 invoice and model-name change
- Model pages for gpt-oss-120b, GLM-5.3, Kimi K2.7 Code and Gemma 4 26B A4B; AI Gateway provider list
