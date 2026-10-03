---
last_checked: 2026-10-03
volatility: VOLATILE (catalogue, limits and prices change often)
kind: inference host
sources:
  - https://inference-docs.cerebras.ai/introduction
  - https://inference-docs.cerebras.ai/models/overview
  - https://inference-docs.cerebras.ai/support/rate-limits
  - https://inference-docs.cerebras.ai/capabilities/reasoning
  - https://inference-docs.cerebras.ai/capabilities/structured-outputs
  - https://inference-docs.cerebras.ai/capabilities/prompt-caching
  - https://inference-docs.cerebras.ai/capabilities/tool-use
  - https://www.cerebras.ai/pricing
---

# Cerebras

inference host

Cerebras sells inference on its own wafer-scale hardware: a shared, pay-as-you-go service and a dedicated service with reserved capacity. Its API is described as mostly compatible with OpenAI's client libraries. The shared catalogue is short, and the models page gives a throughput figure for each model (about 3,000 tokens a second for gpt-oss-120b and 1,850 for Qwen 3.8 27B, Cerebras's own numbers). [intro, models]

## Models offered

The shared-inference catalogue page lists two production models: [gpt-oss-120b](../models/openai/gpt-oss-120b.md) (`gpt-oss-120b`) and [Qwen 3.8 27B](../models/alibaba/qwen3.8-27b.md) (`qwen-3.8-27b`), with context of 65k tokens on the free tier and 131k on paid (gpt-oss-120b) and 64k and 128k (Qwen). The capability pages also name [Kimi K2.7 Code](../models/moonshot/kimi-k2.7-code.md) (`kimi-k2.7-code`), which the tool-use page marks as customer trials only, and [Gemma 4 31B](../models/google/gemma-4-31b-it.md) (`gemma-4-31b`), marked as Dedicated Inference; neither is in the shared catalogue. Cerebras states that shared models are the original unpruned versions, that it applies selective weight-only quantisation in storage while keeping sensitive layers, activations, attention and the KV cache at full precision, and that any compressed variant would get its own id. Dedicated Inference supports additional model families. Maximum output tokens are not stated in the catalogue. [models, reason, tools]

## API surface

- **Protocol.** OpenAI-compatible Chat Completions at `https://api.cerebras.ai/v1`. No Anthropic-compatible endpoint was found in the pages read. [intro]
- **Auth.** A bearer key (`CEREBRAS_API_KEY`). [intro]
- **SDKs.** `cerebras.cloud.sdk` (Python) and `@cerebras/cerebras_cloud_sdk` (JavaScript or Node.js), or plain HTTP. [intro]
- **Model ids.** Short lowercase ids such as `qwen-3.8-27b` and `gpt-oss-120b`. [intro, models]

## Feature parity

- **Reasoning and effort.** `reasoning_effort` values and defaults differ by model: `qwen-3.8-27b` accepts `none`, `low`, `medium` and `high` and defaults to `high`; `gpt-oss-120b` accepts `low`, `medium` and `high` and defaults to `medium`; `kimi-k2.7-code` always reasons and accepts but ignores the effort value; `gemma-4-31b` accepts `none` to `high` and defaults to `none` (reasoning off). `reasoning_format` takes `parsed` (reasoning in a separate field), `raw` (prepended to the content), `hidden` (generated but not shown) or `none` (default behaviour). `clear_thinking`, for Qwen only, decides whether earlier reasoning stays in the prompt across turns (false or omitted keeps it). Reasoning appears in `message.reasoning` or `delta.reasoning`, and counts toward `max_completion_tokens`. [reason]
- **Tools.** Function calling with `parallel_tool_calls`, `tool_choice` (`none`, `auto`, `required` or a named function) and a strict mode using constrained decoding, on qwen-3.8-27b and gpt-oss-120b (shared), kimi-k2.7-code (customer trials) and gemma-4-31b (dedicated). Strict tool schemas need `additionalProperties: false`; the page says to give every function the same `strict` value (or none) with Kimi, and not to use `pattern`, `minLength` or `maxLength` in strict Qwen schemas. [tools]
- **Structured output.** `strict: true` uses constrained decoding on four models. Limits: schema text up to 5,000 characters, depth 10, 500 properties per object and 500 enum values in total; recursive schemas, external references, `oneOf` and `allOf`, regex patterns and conditionals are unsupported. The docs warn against combining `tools` and `response_format` unless the model's contract documents it. [struct]
- **Prompt caching.** Automatic and on for all models, at standard input prices (no discount, no premium). The guaranteed life is 5 minutes, up to an hour under light load, in blocks of 128 tokens, and the prefix must match exactly. `usage.prompt_tokens_details.cached_tokens` shows hits. Cached tokens count toward the total-token rate limit but not the uncached one. Entries stay in memory, are never persisted and are never shared between organisations. [cache, rate]
- **Batch, vision, long context.** No batch API or vision input was found in the pages read; both are `UNVERIFIED`. Context is per model and tier. Streaming is supported (the reasoning docs show streaming deltas). [reason]

## Pricing

Per token on pay-as-you-go, with different prices by model and no cached-token discount (the caching page says cached and fresh input tokens are billed at the same rate); a free tier; a one-time $5 promotional credit when a payment method is added, which expires 30 days after activation; custom Enterprise plans, with Dedicated Inference for reserved capacity. The pricing page lists partner routes (AWS Marketplace, OpenRouter, Hugging Face, Vercel) as other ways to buy, and does not mention a batch discount. Per-model prices were not shown in the pricing page as read. [price, cache, intro]

## Limits and data

- **Rate limits.** Free Trial: 5 requests a minute for both production models, 30,000 uncached and 90,000 total tokens a minute, and 1 million tokens an hour and a day. Developer (pay as you go), with no hourly or daily cap: `gpt-oss-120b` at 1,000 requests, 1 million uncached and 3 million total tokens a minute; `qwen-3.8-27b` at 300 requests, 150,000 uncached and 750,000 total tokens a minute (the total is marked as temporarily raised from three to five times the uncached figure). Enterprise is custom. Limits use two token buckets, uncached and total, refilled continuously, and a request is limited before processing if its estimate exceeds what is left. A 429 says which bucket was exceeded; the docs give no rate-limit headers. [rate]
- **Retention.** The documentation pages read have no data-handling section, the data-privacy URL tried returned 404, and the pricing and introduction pages make no retention statement, so retention of prompts and outputs, training use and zero-retention options are not published in the pages read. The only stated handling is the cache's: in memory, never persisted, per organisation. [cache, price, intro]
- **Regions.** Not stated in the pages read. [intro, price]

## Notes for agents and harnesses

- **Effort is not portable.** One model ignores the value, one accepts `none` and another does not, and defaults differ; the reasoning-token count shows what ran. [reason]
- **Reasoning counts toward the output cap.** Reasoning tokens count toward `max_completion_tokens`, so a small cap can cut the answer. [reason]
- **Cache hits raise throughput, not savings.** Cached tokens are billed at the normal rate but do not use the uncached-token limit; a hit needs an exactly matching prefix. [cache, rate]
- **Strict schemas have a narrow subset.** A schema with `oneOf`, `allOf`, regex patterns, conditionals or recursion is outside what strict mode supports. [struct]
- **Tools and `response_format` together.** The structured-output page warns against combining them unless the model's documentation supports the pair. [struct]
- **Context depends on tier.** Free-tier context is about half the paid figure (65k against 131k for gpt-oss-120b), so a long prompt that works on a paid key can fail on a trial key. [models]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| intro | https://inference-docs.cerebras.ai/introduction | L | 2026-10-03 |
| models | https://inference-docs.cerebras.ai/models/overview | L | 2026-10-03 |
| rate | https://inference-docs.cerebras.ai/support/rate-limits | L | 2026-10-03 |
| reason | https://inference-docs.cerebras.ai/capabilities/reasoning | L | 2026-10-03 |
| struct | https://inference-docs.cerebras.ai/capabilities/structured-outputs | L | 2026-10-03 |
| cache | https://inference-docs.cerebras.ai/capabilities/prompt-caching | L | 2026-10-03 |
| tools | https://inference-docs.cerebras.ai/capabilities/tool-use | L | 2026-10-03 |
| price | https://www.cerebras.ai/pricing | L | 2026-10-03 |
