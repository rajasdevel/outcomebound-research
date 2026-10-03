---
last_checked: 2026-10-03
volatility: VOLATILE (catalogue, prices, limits and feature support change often)
kind: inference host
sources:
  - https://docs.deepinfra.com/
  - https://docs.deepinfra.com/llms.txt
  - https://deepinfra.com/pricing
  - https://docs.deepinfra.com/account/data-privacy.md
  - https://docs.deepinfra.com/account/rate-limits.md
  - https://docs.deepinfra.com/chat/reasoning.md
  - https://docs.deepinfra.com/chat/structured-outputs.md
  - https://docs.deepinfra.com/chat/tool-calling.md
  - https://docs.deepinfra.com/chat/prompt-caching.md
  - https://docs.deepinfra.com/batch/introduction.md
  - https://docs.deepinfra.com/integrations/anthropic.md
---

# DeepInfra

inference host

DeepInfra hosts hundreds of open-weight models (its documentation says more than 100 language models) for API use, covering language, vision, embeddings, reranking, image and video generation, and speech, and rents GPUs for private deployments. Language models are billed per token, most other models by inference time. It offers an OpenAI-compatible API and an Anthropic-compatible one. [docs, price]

## Models offered

Open-weight models from many makers. The reasoning page lists five reasoning models: DeepSeek-V4-Flash-0731, DeepSeek-V4-Pro-0813, GLM-5.2, Kimi-K3 and Ling-3.0-flash; the tool-calling page highlights DeepSeek-V4-Flash and Kimi-K3. Model files in scope: [DeepSeek Flash](../models/deepseek/deepseek-flash.md), [DeepSeek V4 Pro](../models/deepseek/deepseek-v4-pro.md), [Kimi K3](../models/moonshot/kimi-k3.md) and [GLM 5.2](../models/zai/glm-5.2.md); other makers' files may also be available, and the live list is in the catalogue at deepinfra.com/models, which was not read here. Private deployments run on A100, H100, H200, B200 and B300 GPUs with autoscaling. [docs, reason, tools]

## API surface

- **Protocols.** OpenAI-compatible at `https://api.deepinfra.com/v1/openai`; an Anthropic-compatible endpoint at `https://api.deepinfra.com/anthropic` (Messages at `/anthropic/v1/messages`, plus `count_tokens`). [docs, anth]
- **Auth.** An API key from the dashboard as a bearer token (`DEEPINFRA_API_KEY`); the Anthropic route also accepts `x-api-key`. [docs, anth]
- **SDKs.** The OpenAI SDK with a changed base URL; the Anthropic SDK and Claude Code via the Anthropic route. [docs, anth]
- **Model ids.** `org/model-name` as on Hugging Face, with dated suffixes on some, such as `deepseek-ai/DeepSeek-V4-Flash-0731`, `zai-org/GLM-5.2` and `moonshotai/Kimi-K3`. [docs, anth]

## Feature parity

- **Reasoning and effort.** `reasoning_effort` takes `none`, `low`, `medium` or `high`; or a `reasoning` object with `effort` and a boolean `enabled` (`false` turns reasoning off, making the model act like a standard chat model). Reasoning models produce a trace by default; the page says higher effort means more output tokens and latency, and that `none` makes responses faster and cheaper. The page does not say which response field carries the trace. [reason]
- **Tools.** OpenAI-style `tools`. The page's support table lists `tool_choice` `auto` and `none`, so forcing a named function or `required` is not documented. Parallel calls are marked as supported with quality that "may vary", and nested calls as unsupported. The page advises avoiding system messages with tool calling and using temperatures below 1.0. [tools]
- **Structured output.** `json_object` (valid JSON, no schema) and `json_schema` with `strict: true`, which the page recommends for production. The docs warn that forced JSON can make some models invent values rather than say they do not know, most visibly for real-time data such as weather, and advise temperatures below 0.7 for consistent structure. Support is per model. [struct]
- **Prompt caching.** KV-cache reuse, automatic by default (a one-character difference in the prefix misses), or tagged with a `prompt_cache_key` (the page suggests a per-session key) to raise hit rates when prompts differ slightly. Cached input tokens are billed at a reduced rate. A retention option (`prompt_cache_options`) keeps a prefix for 5 minutes or 1 hour, billed at a cache-write premium up front. `prompt_tokens_details.cached_tokens` reports hits. [cache]
- **Batch.** 20 percent below real-time prices, results within 24 hours, JSONL of up to 50,000 requests and 200 MB per file, 100 concurrent batches per user, for `/v1/chat/completions`, `/v1/completions` and `/v1/embeddings` (not `/v1/responses`); all lines must use one model, and batch use does not count against real-time rate limits. [batch]
- **Anthropic route.** The page says message creation, streaming and token counting work, that not all Anthropic-specific features may be supported, and that the models are open models served through Anthropic's protocol, not Claude. `anthropic-version` and `anthropic-beta` headers can be passed. [anth]
- **Service tiers.** Standard (1 times the base price), Priority (1.5 times, faster at peak demand) and Flex (0.8 times, slower, for non-production work) are priced on the pricing page; how each is selected in a request was not found. [price]
- **Vision, long context, streaming.** Vision and OCR models are served; context windows are per model; streaming is supported. [docs, anth]

## Pricing

Per token for language models with separate input, cached-input and output rates (the pricing page lists DeepSeek-V4-Flash at $0.09 per million input tokens, $0.018 cached and $0.18 output), and inference-time billing for most other models. Service tiers scale the base price (Priority 1.5 times, Flex 0.8 times). Custom LLMs on dedicated GPUs cost from $0.89 per GPU-hour (A100 80GB) to $4.89 (B300). Embeddings are priced per input token ($0.005 to $0.01 per million). Accounts need prepayment or card verification; spending limits and monthly invoicing are available. Per-model rates are on the pricing page and are not repeated here. [price]

## Limits and data

- **Rate limits.** A concurrency limit, not a per-minute one: 200 concurrent requests per model by default, so two models allow 400. Throughput therefore depends on request length (about 12,000 requests a minute at one second each, 1,200 at ten seconds, 200 at 60 seconds). Excess requests get 429 with a `Rate limited` message; occasional 429s can also appear while a busy model auto-scales. Increases are requested in the dashboard. No tier table exists. [rate]
- **Retention.** During normal inference, inputs are not written to disk and live only in memory while the request runs, and outputs are deleted once returned. Bulk inference may keep encrypted data on disk for a short period after completion, and image-generation outputs are held briefly. DeepInfra logs metadata (request id, cost, sampling parameters) and not content. [privacy]
- **Training and sharing.** DeepInfra states it does not train on or share submitted data, except that requests to Google and Anthropic models are passed to those companies, whose own storage and training policies apply; Google logs prompts and responses for a limited period to detect violations of its use policy. [privacy]
- **Regions.** The data-privacy page has no region information. [privacy]

## Notes for agents and harnesses

- **Reasoning is on unless turned off.** Reasoning models produce a trace by default; `reasoning_effort: "none"` turns it off, which the page says is faster and cheaper. [reason]
- **Forced tool choice is not documented.** The support table lists only `auto` and `none`, so a request that must produce a tool call has no documented way to force it. [tools]
- **Tool-calling cautions.** The page advises no system message with tool calling and temperatures below 1.0, and marks nested calls unsupported. [tools]
- **Cache keys for sessions.** A per-session `prompt_cache_key` raises hit rates for growing conversations, and paid retention covers pauses of up to an hour. [cache]
- **Concurrency is the budget.** A client that runs many parallel calls to one model meets the 200-request cap; a sequential client does not. [rate]
- **The Anthropic route is for open models.** Claude-only features such as server tools are not among those the page says work. [anth]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| docs | https://docs.deepinfra.com/ | L | 2026-10-03 |
| index | https://docs.deepinfra.com/llms.txt | L | 2026-10-03 |
| price | https://deepinfra.com/pricing | L | 2026-10-03 |
| privacy | https://docs.deepinfra.com/account/data-privacy.md | L | 2026-10-03 |
| rate | https://docs.deepinfra.com/account/rate-limits.md | L | 2026-10-03 |
| reason | https://docs.deepinfra.com/chat/reasoning.md | L | 2026-10-03 |
| struct | https://docs.deepinfra.com/chat/structured-outputs.md | L | 2026-10-03 |
| tools | https://docs.deepinfra.com/chat/tool-calling.md | L | 2026-10-03 |
| cache | https://docs.deepinfra.com/chat/prompt-caching.md | L | 2026-10-03 |
| batch | https://docs.deepinfra.com/batch/introduction.md | L | 2026-10-03 |
| anth | https://docs.deepinfra.com/integrations/anthropic.md | L | 2026-10-03 |
