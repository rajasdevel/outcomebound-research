---
last_checked: 2026-11-03
volatility: VOLATILE (catalogue, limits and prices change often)
kind: inference host
sources:
  - https://inference-docs.cerebras.ai/introduction
  - https://inference-docs.cerebras.ai/models/overview
  - https://inference-docs.cerebras.ai/models/qwen-3.8-27b
  - https://inference-docs.cerebras.ai/models/openai-oss
  - https://inference-docs.cerebras.ai/support/rate-limits
  - https://inference-docs.cerebras.ai/capabilities/reasoning
  - https://inference-docs.cerebras.ai/capabilities/structured-outputs
  - https://inference-docs.cerebras.ai/capabilities/prompt-caching
  - https://inference-docs.cerebras.ai/capabilities/tool-use
  - https://www.cerebras.ai/pricing
  - https://inference-docs.cerebras.ai/capabilities/image-inputs
  - https://inference-docs.cerebras.ai/capabilities/batch
  - https://inference-docs.cerebras.ai/resources/openai
  - https://inference-docs.cerebras.ai/dedicated/overview
  - https://www.cerebras.ai/privacy-policy
  - https://www.cerebras.ai/terms-of-service
  - https://www.cerebras.ai/blog/cerebras-launches-worlds-fastest-deepseek-r1-llama-70b-inference
---

# Cerebras

inference host

Cerebras sells inference on its own wafer-scale hardware: a shared, pay-as-you-go service and a dedicated service with reserved capacity. Its API works with OpenAI's client libraries for many common workflows. The shared catalogue is short, and the models page gives a throughput figure for each model (about 3,000 tokens a second for gpt-oss-120b and 1,850 for Qwen 3.8 27B, Cerebras's own numbers). [intro, models, dedicated, compat] [as-of 2026-11-03]

## Models offered

The shared-inference catalogue page lists two shared models: [gpt-oss-120b](../models/openai/gpt-oss-120b.md) (`gpt-oss-120b`) and [Qwen 3.8 27B](../models/alibaba/qwen3.8-27b.md) (`qwen-3.8-27b`), with context of 65k tokens on the free tier and 131k on paid (gpt-oss-120b) and 64k and 128k (Qwen). The capability pages also name [Kimi K2.7 Code](../models/moonshot/kimi-k2.7-code.md) (`kimi-k2.7-code`) and [Gemma 4 31B](../models/google/gemma-4-31b-it.md) (`gemma-4-31b`) for Dedicated Inference. The reasoning page also lists Kimi K3 and GLM 5.3 Flash for Dedicated Inference. [as-of 2026-11-03] Cerebras states that shared models are the original unpruned versions, that it applies selective weight-only quantisation in storage while keeping sensitive layers, activations, attention and the KV cache at full precision, and that a future pruned variant would get its own id. Dedicated Inference supports additional model families. The model detail pages list maximum output of 32k tokens on Free Trial and 40k on paid for both shared models. [models, reason, tools, qwen-page, gpt-page]

## API surface

- **Protocol.** OpenAI-compatible Chat Completions at `https://api.cerebras.ai/v1`. No Anthropic-compatible endpoint was found in the pages read. [intro]
- **Auth.** A bearer key (`CEREBRAS_API_KEY`). [intro]
- **SDKs.** `cerebras.cloud.sdk` (Python) and `@cerebras/cerebras_cloud_sdk` (JavaScript or Node.js), or plain HTTP. [intro]
- **Model ids.** Shared inference uses ids such as `qwen-3.8-27b` and `gpt-oss-120b`. Dedicated inference uses the assigned endpoint id. [intro, models, compat] [as-of 2026-11-03]

## Feature parity

- **Reasoning and effort.** `reasoning_effort` values and defaults differ by model: `qwen-3.8-27b` accepts `none`, `low`, `medium` and `high` and defaults to `high`; `gpt-oss-120b` accepts `low`, `medium` and `high` and defaults to `medium`; `kimi-k2.7-code` always reasons and accepts but ignores the effort value; `gemma-4-31b` accepts `none` to `high` and defaults to `none` (reasoning off). Kimi K3 and GLM 5.3 Flash accept `low`, `high` and `max`, with `max` as the default. The `reasoning_format` options and their support vary by model. Qwen and GLM 5.3 Flash support `clear_thinking`; false or omitted keeps earlier reasoning. [as-of 2026-11-03] In parsed format, reasoning appears in `message.reasoning` or `delta.reasoning`; reasoning counts toward `max_completion_tokens`. [reason]
- **Tools.** Function calling with `parallel_tool_calls`, `tool_choice` (`none`, `auto`, `required` or a named function) and a strict mode using constrained decoding, on qwen-3.8-27b and gpt-oss-120b (shared), kimi-k2.7-code and gemma-4-31b (dedicated). Strict tool schemas need `additionalProperties: false`; the page says to give every function the same `strict` value (or none) with Kimi, and not to use `pattern`, `minLength` or `maxLength` in strict Qwen schemas. [tools]
- **Structured output.** `strict: true` uses constrained decoding on four models. Limits: counted schema text up to 5,000 characters across property names, definition names and enum or const strings, with descriptions excluded; depth 10, 500 object properties (the table does not specify the counting scope) and 500 enum values in total; recursive schemas, external references, `oneOf` and `allOf`, regex patterns and conditionals are unsupported. [as-of 2026-11-03] The docs warn against combining `tools` and `response_format` unless the model's contract documents it. [struct]
- **Prompt caching.** Automatic and on for all models, at standard input prices (no discount, no premium). The guaranteed life is 5 minutes, up to an hour under light load, in blocks of 128 tokens, and the prefix must match exactly. `usage.prompt_tokens_details.cached_tokens` shows hits. Cached tokens count toward the total-token rate limit but not the uncached one. Entries stay in memory, are never persisted and are never shared between organisations. [cache, rate]
- **Batch, vision, long context.** Image input is in public preview for Qwen on shared and dedicated inference and for certain dedicated models. The Batch API is in private preview; its documentation is under Dedicated Inference. Context is per model and tier. Streaming is supported. [vision, batch, reason] [as-of 2026-11-03]

## Pricing

Pay-as-you-go uses per-token rates. Cached and fresh input tokens have the same model-specific input rate, with no extra cache fee. The free trial requires a verified payment method and gives a one-time $5 credit that expires after 30 days; it does not renew. API access stops when it expires or is exhausted until credits are purchased. Dedicated pricing is by quote. The pricing page names AWS Marketplace, OpenRouter, Hugging Face and Vercel as partner routes. The rendered Developer pricing table lists gpt-oss-120b at $0.35 input and $0.75 output per million tokens, and Qwen 3.8 27B at $0.99 input and $1.49 output. The tier is for development, evaluation and experimentation, not production. Adding a payment method for the promotional credit does not automatically enroll the user in paid usage. [price, cache, rate, qwen-page, gpt-page] [as-of 2026-11-03]

## Limits and data

- **Rate limits.** Free Trial: 5 requests a minute for both shared models, 30,000 uncached and 90,000 total tokens a minute, and 1 million tokens an hour and a day. Developer (pay as you go), with no hourly or daily cap: `gpt-oss-120b` at 1,000 requests, 1 million uncached and 3 million total tokens a minute; `qwen-3.8-27b` at 300 requests, 150,000 uncached and 750,000 total tokens a minute (the total is marked as temporarily raised from three to five times the uncached figure). Enterprise is custom. Limits use two token buckets, uncached and total, refilled continuously, and a request is limited before processing if its estimate exceeds what is left. A 429 says which bucket was exceeded; the docs give no rate-limit headers. [rate] [as-of 2026-11-03]
- **Retention and training.** The privacy policy says Cerebras does not retain inputs and outputs for its inference, training and chatbot services, and deletes service logs when no longer needed to provide service. The policy excludes personal data processed for customers in Cerebras's role as processor or service provider. Its terms say the content-use clause does not grant Cerebras a right to train or fine-tune models on service content; third-party model terms can govern a conflicting model-related term. The cache is held in memory and is not shared between organisations. These documents do not establish all contract-specific exceptions or third-party terms. [privacy, terms, cache] [as-of 2026-11-03]
- **Regions.** A 2025 Cerebras post said its inference ran in US data centres at that time. Its current privacy policy says personal data covered by that policy may be stored and processed in the US and other countries, subject to separate agreement. Current inference region selection and residency guarantees remain `UNVERIFIED`. [location, privacy] [as-of 2026-11-03]

## Notes for agents and harnesses

- **Effort is not portable.** One model ignores the value, one accepts `none` and another does not, and defaults differ. [reason]
- **Reasoning counts toward the output cap.** Reasoning tokens count toward `max_completion_tokens`, so a small cap can cut the answer. [reason]
- **Cache hits raise throughput, not savings.** Cached tokens are billed at the normal rate but do not use the uncached-token limit; a hit needs an exactly matching prefix. [cache, rate]
- **Strict schemas have a narrow subset.** A schema with `oneOf`, `allOf`, regex patterns, conditionals or recursion is outside what strict mode supports. [struct]
- **Tools and `response_format` together.** The structured-output page warns against combining them unless the model's documentation supports the pair. [struct]
- **Context depends on tier.** Free-tier context is about half the paid figure (65k against 131k for gpt-oss-120b), so a long prompt that works on a paid key can fail on a trial key. [models]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| intro | https://inference-docs.cerebras.ai/introduction | L | 2026-11-03 |
| models | https://inference-docs.cerebras.ai/models/overview | L | 2026-11-03 |
| rate | https://inference-docs.cerebras.ai/support/rate-limits | L | 2026-11-03 |
| qwen-page | https://inference-docs.cerebras.ai/models/qwen-3.8-27b | L | 2026-11-03 |
| gpt-page | https://inference-docs.cerebras.ai/models/openai-oss | L | 2026-11-03 |
| reason | https://inference-docs.cerebras.ai/capabilities/reasoning | L | 2026-11-03 |
| struct | https://inference-docs.cerebras.ai/capabilities/structured-outputs | L | 2026-11-03 |
| cache | https://inference-docs.cerebras.ai/capabilities/prompt-caching | L | 2026-11-03 |
| tools | https://inference-docs.cerebras.ai/capabilities/tool-use | L | 2026-11-03 |
| vision | https://inference-docs.cerebras.ai/capabilities/image-inputs | L | 2026-11-03 |
| batch | https://inference-docs.cerebras.ai/capabilities/batch | L | 2026-11-03 |
| price | https://www.cerebras.ai/pricing | L | 2026-11-03 |
| compat | https://inference-docs.cerebras.ai/resources/openai | L | 2026-11-03 |
| dedicated | https://inference-docs.cerebras.ai/dedicated/overview | L | 2026-11-03 |
| privacy | https://www.cerebras.ai/privacy-policy | L | 2026-11-03 |
| terms | https://www.cerebras.ai/terms-of-service | L | 2026-11-03 |
| location | https://www.cerebras.ai/blog/cerebras-launches-worlds-fastest-deepseek-r1-llama-70b-inference | L | 2026-11-03 |
