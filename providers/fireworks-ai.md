---
last_checked: 2026-10-03
volatility: VOLATILE (catalogue, prices, limits and feature support change often)
kind: inference host
sources:
  - https://docs.fireworks.ai/getting-started/introduction
  - https://docs.fireworks.ai/guides/quotas_usage/rate-limits
  - https://fireworks.ai/pricing
  - https://docs.fireworks.ai/guides/querying-text-models
  - https://docs.fireworks.ai/guides/reasoning
  - https://docs.fireworks.ai/guides/prompt-caching
  - https://docs.fireworks.ai/guides/security_compliance/data_handling
  - https://docs.fireworks.ai/structured-responses/structured-response-formatting
  - https://docs.fireworks.ai/tools-sdks/anthropic-compatibility
  - https://docs.fireworks.ai/guides/batch-inference
  - https://fireworks.ai/models
---

# Fireworks AI

inference host

Fireworks AI hosts open-weight models (and models customers fine-tune) behind an API, with serverless per-token inference, on-demand dedicated GPU deployments, managed fine-tuning and a batch service. Its documentation lists more than 100 models across text, vision, audio, image and embeddings. Besides an OpenAI-compatible endpoint it offers an Anthropic-compatible Messages endpoint. [intro, anth]

## Models offered

Open-weight families from several makers. The model library read on 2026-10-03 shows, among others, Kimi K3, Kimi K2.7 Code, MiniMax M3, GLM-5.3 and GLM 5.3 Flash, DeepSeek V4 Pro, V4 Flash and V4.1 Flash, gpt-oss-120b and Qwen3.8 models (Flash Next, Max, 27B, 2.4T-A95B). Model files in scope: [Kimi K3](../models/moonshot/kimi-k3.md), [Kimi K2.7 Code](../models/moonshot/kimi-k2.7-code.md), [MiniMax M3](../models/minimax/MiniMax-M3.md), [GLM 5.3](../models/zai/glm-5.3.md), [GLM 5.3 Flash](../models/zai/glm-5.3-flash.md), [DeepSeek V4 Pro](../models/deepseek/deepseek-v4-pro.md), [DeepSeek Flash](../models/deepseek/deepseek-flash.md), [gpt-oss-120b](../models/openai/gpt-oss-120b.md), [Qwen3.8 Flash Next](../models/alibaba/qwen3.8-flash-next.md), [Qwen3.8 Max](../models/alibaba/qwen3.8-max.md), [Qwen3.8 27B](../models/alibaba/qwen3.8-27b.md) and [Qwen3.8 2.4T A95B](../models/alibaba/qwen3.8-2.4t-a95b.md). Fine-tuned and custom models can be deployed on-demand. Router ids (for example `accounts/fireworks/routers/firerouter/opus`, short form `firerouter/opus`) exist alongside plain model ids. [intro, text, lib]

## API surface

- **Protocols.** OpenAI-compatible chat completions (and a completions API) at `https://api.fireworks.ai/inference/v1`; a Responses API; and an Anthropic-compatible `POST /v1/messages` reached by giving the Anthropic SDK the base URL `https://api.fireworks.ai/inference` and a Fireworks key. [text, anth]
- **Auth.** A Fireworks API key (`FIREWORKS_API_KEY`) as a bearer token. [text, anth]
- **SDKs.** The OpenAI and Anthropic SDKs, plus Fireworks' own Python SDK; the reasoning page recommends the alpha version (installed with `pip install --pre fireworks-ai`) for reasoning features. LiteLLM integration is documented. [reason, intro]
- **Model ids.** Resource paths: `accounts/fireworks/models/<name>` (for example `deepseek-v3p1`), with `accounts/<account>/...` for a customer's own deployments; the Anthropic endpoint also needs a Fireworks path in `model` (the page's example is `accounts/fireworks/models/kimi-k2p5`). [intro, anth, text]
- **Defaults.** When temperature, top_k, top_p, min_p or typical_p are not set, the service takes them from the model's Hugging Face `generation_config.json`. [text]

## Feature parity

- **Reasoning and effort.** `reasoning_effort` accepts `low`, `medium` or `high`. An Anthropic-style `thinking` object with `budget_tokens` (minimum 1,024) is also accepted, and one request may not set both. `reasoning_history: "preserved"` keeps reasoning across user turns. Reasoning text arrives in `reasoning_content` (in each chunk's delta when streaming); for tool-calling agents the page says earlier turns' `reasoning_content` must be sent back so that the model can think between tool calls. On the Anthropic endpoint the controls are `output_config.effort` (`low`, `medium`, `high`, `max`) or `thinking.budget_tokens`, which is converted to an effort band. [reason, anth]
- **Tools.** OpenAI-style tool calling is documented; on the Anthropic endpoint client-side tools work (with tool search and deferred loading) and server-side tools (code execution, web search, memory, web fetch) do not. [text, anth]
- **Structured output.** `response_format` with `json_schema` (most of JSON Schema 2020-12, including `$ref` and `anyOf`) or `json_object`, and a grammar mode taking a custom BNF grammar. Schemas with `properties` are treated as if `unevaluatedProperties: false` were set. The docs say to ask for JSON in the prompt as well, or the model may emit whitespace until the token limit, and to watch for `finish_reason: "length"`. With a reasoning model, `response_format` with `json_schema` turns the reasoning output off; the page's way to keep both is the schema in the prompt and no `response_format`. Regex patterns are compiled on a best-effort basis and unsupported constructs fall back to unconstrained strings. The Anthropic endpoint takes `output_config.format`. [struct, anth]
- **Prompt caching.** On by default for all models and deployments. Serverless cached tokens are discounted, 50 percent by default and varying by model. An `x-session-affinity` header or the `user` field groups related requests for better hit rates. On dedicated deployments, response headers `fireworks-prompt-tokens` and `fireworks-cached-prompt-tokens` report usage. The page advises static content (instructions, examples) first and variable content last, and no timestamps in the system prompt, since one changed token invalidates the cache from that point on. [cache]
- **Batch.** 50 percent off serverless prices, with a further 50 percent off cached tokens, JSONL with `custom_id` and `body`, inputs to 80 GiB and outputs to 8 GB, and a window of 12, 24, 48 or 72 hours, with finished rows billed even if the job expires. Any model that supports on-demand deployment works. On the Anthropic endpoint, `/v1/messages/batches` and `count_tokens` are not supported. [batch, anth]
- **Anthropic endpoint gaps.** `max_tokens` is required (a 400 error without it), `anthropic-version` is ignored, document and PDF blocks and `source.type: "file"` images are unsupported, `output_config.speed` is unsupported, and streaming usage appears only on the final `message_delta`. Vision works with compatible models, with base64 and URL images. Cache hits are reported as `cache_read_input_tokens`. [anth]
- **Long context and streaming.** Per model (the library lists 1,048,576 tokens for DeepSeek V4 Pro and Flash and 262,144 for several others); streaming is supported, with usage in the final chunk and a `perf_metrics_in_response` option. [text, lib]

## Pricing

Serverless is per token with rates by model size class, a cached-input discount, optional auto-reload and monthly spending limits. On-demand deployments are billed per GPU-second with no start-up charge: the page quotes $0.134 a minute ($8 an hour) for an H100 or H200, $0.217 ($13) for a B200 and $0.250 to $0.334 ($15 to $20) for B300 and GB300, and a 1.5 times premium for region-restricted deployments. Fine-tuning is per million tokens by model size and method (supervised LoRA from $0.50 below 16B parameters to $10 above 300B), and a serverless training API bills prefill, sampling and training tokens separately. Batch is half the serverless rate. Enterprise deals add higher limits. Per-model prices are on the model library and are not repeated here. [price, batch]

## Limits and data

- **Rate limits.** Spend tiers (four plus an unlimited tier) set monthly spend caps: tier 1 needs a payment method and caps monthly spend at $50, tier 4 (reached at $5,000 spent or added) at $50,000. Accounts with no payment method or no credits are limited to 10 requests a minute; accounts with a payment method and credit reach at most 6,000 requests a minute, account-wide across serverless and on-demand. Serverless also has adaptive token-per-minute limits. On-demand deployments have GPU quotas per placement (16 GPUs by default for H100, H200, B200 and B300 in global regions) and are not bound by the adaptive serverless token limits; a 429 on them usually means the GPUs are saturated. [rate]
- **Retention.** For open models, Fireworks does not log or store prompt or generation data without the user opting in; it logs metadata such as token counts. The exception is the Responses API, which stores conversations (prompts, responses and tool calls) for 30 days when `store` is true, the default; `store: false` or a DELETE call avoids or ends that. Prompt caching may hold prompt data and KV caches in volatile memory for several minutes. Enterprise admins can enforce a policy that rejects requests that would persist content. The data-handling page does not address training use or regions. [data]
- **Regions.** Not addressed in the data-handling page; the pricing page's region-restricted deployments suggest an option for dedicated deployments. [data, price]

## Notes for agents and harnesses

- **`thinking` and `reasoning_effort` are exclusive.** A request with both fails validation. [reason]
- **`response_format` can switch reasoning off.** With a reasoning model, a `json_schema` response format suppresses the reasoning output; the structured-output page gives the schema-in-prompt route for clients that want both. [struct]
- **Reasoning must be sent back on tool turns.** For interleaved or preserved thinking, hand-built assistant messages need their `reasoning_content`. [reason]
- **Cache hits depend on affinity and prefix stability.** Caching is on by default, but the hit rate depends on routing related requests together (`x-session-affinity` or `user`) and on an unchanged prefix. [cache]
- **The Anthropic endpoint is partial.** A Claude-native client gets text, thinking, client tools, structured output and caching, not server tools, PDFs, batches or token counting, and the model must be a Fireworks id, not a Claude id. [anth]
- **The Responses API stores by default.** Conversations are kept 30 days unless `store` is false. [data]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| intro | https://docs.fireworks.ai/getting-started/introduction | L | 2026-10-03 |
| rate | https://docs.fireworks.ai/guides/quotas_usage/rate-limits | L | 2026-10-03 |
| price | https://fireworks.ai/pricing | L | 2026-10-03 |
| text | https://docs.fireworks.ai/guides/querying-text-models | L | 2026-10-03 |
| reason | https://docs.fireworks.ai/guides/reasoning | L | 2026-10-03 |
| cache | https://docs.fireworks.ai/guides/prompt-caching | L | 2026-10-03 |
| data | https://docs.fireworks.ai/guides/security_compliance/data_handling | L | 2026-10-03 |
| struct | https://docs.fireworks.ai/structured-responses/structured-response-formatting | L | 2026-10-03 |
| anth | https://docs.fireworks.ai/tools-sdks/anthropic-compatibility | L | 2026-10-03 |
| batch | https://docs.fireworks.ai/guides/batch-inference | L | 2026-10-03 |
| lib | https://fireworks.ai/models | L | 2026-10-03 |
