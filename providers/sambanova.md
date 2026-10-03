---
last_checked: 2026-10-03
volatility: VOLATILE (catalogue, preview status, limits and prices change often)
kind: inference host
sources:
  - https://docs.sambanova.ai/cloud/docs/get-started/overview
  - https://docs.sambanova.ai/cloud/docs/get-started/supported-models
  - https://docs.sambanova.ai/docs/en/models/rate-limits
  - https://docs.sambanova.ai/docs/en/features/function-calling
  - https://sambanova.ai/blog/sambacloud-now-supports-the-anthropic-messages-api
  - https://sambanova.ai/blog/prompt-caching-on-sambacloud-faster-cheaper-inference
  - https://community.sambanova.ai/t/privacy-data-use-in-developer-tier/899
  - https://cloud.sambanova.ai/plans/pricing
  - https://docs.sambanova.ai/docs/en/build/reasoning.md
  - https://docs.sambanova.ai/docs/_llms/v2-2-3.md
---

# SambaNova

inference host

SambaNova sells access to open-weight models served on its own chips. SambaCloud is the hosted API (`api.sambanova.ai/v1`); SambaStack is a second product that the overview says is built with the same technologies, with some feature differences. The hosted catalogue is short and divides models into production and preview. [overview, models]

## Models offered

Production models on the page read: [MiniMax-M2.7](../models/minimax/MiniMax-M2.7.md) (192k-token context), [gpt-oss-120b](../models/openai/gpt-oss-120b.md) (128k), Meta-Llama-3.3-70B-Instruct (128k) and DeepSeek-V3.1 (128k). Preview models, which the page says are for evaluation and experimentation only and not for production: [MiniMax-M3](../models/minimax/MiniMax-M3.md) (1M tokens, text only; image and video input not accepted), DeepSeek-V3.2 (32k, text only) and [gemma-4-31B-it](../models/google/gemma-4-31b-it.md) (128k; text, image and video input, no audio). The function-calling page also lists Qwen3-235B-A22B-Instruct-2507, which is not in the models table read, so it is probably not currently served on SambaCloud. Llama 3.3 and the DeepSeek V3 line are not in the model files of this library. [models, fc]

## API surface

- **Protocols.** OpenAI-compatible Chat Completions at `https://api.sambanova.ai/v1` (the OpenAI client is the documented way in). An Anthropic Messages implementation, announced on 2026-07-01, is reached by setting `ANTHROPIC_BASE_URL` to `https://api.sambanova.ai` with a SambaNova key and model id. [overview, anth]
- **Auth.** An API key from the SambaNova platform; the Anthropic setup uses three environment variables (base URL, key, model id). [anth]
- **SDKs.** The OpenAI and Anthropic SDKs; the documentation index has integration guides for LiteLLM and Instructor. No native SDK was named on the pages read. [overview, anth, index]
- **Model ids.** The model's own name without a namespace, such as `MiniMax-M2.7` or `gpt-oss-120b`, with the capitalisation shown. [models]

## Feature parity

- **Reasoning and effort.** The function-calling page says to set `reasoning_effort` to `high` for better tool-calling quality with gpt-oss-120b; no page read lists effort values for the other models, so that list is `UNVERIFIED`. The reasoning guide is written for DeepSeek-R1, which is not in the current catalogue: it advises minimal system prompts, no added chain-of-thought instructions, zero-shot or single-instruction prompts, and temperature 0.6 with top-p 0.95 for general reasoning (0.7 and 1.0 for maths). Through the Anthropic Messages API, reasoning-capable models return a thinking block with no extra parameter. [fc, reasonpg, anth]
- **Tools.** `tool_choice` accepts `auto` (default), `required`, `none` or a named function. Models listed as supporting function calling: Llama 3.3 70B, Qwen3-235B-A22B-Instruct-2507, gpt-oss-120b, DeepSeek-V3.1 and V3.2, MiniMax-M2.7 and M3, and gemma-4-31B-it. Parallel calls are not addressed on the page. The reasoning guide notes that DeepSeek-R1's function calling was unstable (looped calls or empty responses). On the Anthropic endpoint, tool use works, but server-side tools (web search, code execution) do not. [fc, anth]
- **Structured output.** `response_format` with a JSON schema; the `strict` field is accepted, but only `false` (best-effort matching) is enforced, per the page read. A JSON mode (`response_format: json_object`) gives valid JSON with no schema. [fc]
- **Prompt caching.** Announced 2026-07-16, automatic, for MiniMax-M2.7 only (the post says other models return `cached_tokens: 0`), once the stable prefix reaches 4,096 tokens, up to a 192,000-token prefix; cached tokens cost 90 percent less ($0.06 against $0.60 per million for M2.7). Entry life depends on traffic. Usage returns `cached_tokens` and `cache_creation_tokens` in `prompt_tokens_details`. The pricing page read on 2026-10-03 shows a $0.06 cached-input price for MiniMax-M3 instead and has no M2.7 row, so which model caches today is not settled. [cache, price]
- **Batch.** Not found in the pages read; `UNVERIFIED`.
- **Vision, long context, streaming.** Vision is model-specific (gemma-4-31B-it takes images and video). On the Anthropic endpoint, images must be base64, not URLs, and PDF document blocks are unsupported. The Messages implementation has typed server-sent events and a `count_tokens` endpoint. Context windows are in the model table. [models, anth]

## Pricing

Per token by model, with a cached-input price for one MiniMax model (see Prompt caching). The pricing page read on 2026-10-03 gives, per million input and output tokens, MiniMax-M3 at $0.60 and $2.40 (cached input $0.06), DeepSeek-V3.1 and V3.2 at $3.00 and $4.50, gemma-4-31B-it at $0.38 and $1.15, gpt-oss-120b at $0.22 and $0.59 and Llama 3.3 70B at $0.60 and $1.20. The rate-limit page describes a free tier, a Developer tier with higher limits and an Enterprise tier with custom limits through sales. [price, rate]

## Limits and data

- **Rate limits.** Free tier: 20 requests a minute, 20 a day and 200,000 tokens a day per model for DeepSeek-V3.1, Llama 3.3 70B and gpt-oss-120b. Developer tier: 240 requests a minute and 48,000 a day for Llama 3.3 70B, 60 and 12,000 for MiniMax-M2.7, DeepSeek-V3.1 and gpt-oss-120b, and 20 million tokens a day across all models. Preview models DeepSeek-V3.2 and gemma-4-31B-it have the same free-tier figures and 60 and 12,000 on Developer. Enterprise limits are custom. Past a limit the API returns an error; responses carry `x-ratelimit-limit-requests`, `x-ratelimit-remaining-requests` and `x-ratelimit-reset-requests`, and day-level equivalents ending `-day`. [rate]
- **Retention and training.** A staff answer in the developer community (February 2025; last post April 2025) quotes the terms of service: SambaNova processes customer content only as needed to provide the service, may collect usage logs but not customer content, and staff access is limited by confidentiality agreements. In the same thread the question was passed to the legal team, no new privacy-policy wording had appeared by the last post, and no way to mark prompts as confidential was identified. No retention period or zero-retention option for prompts was found on a SambaNova documentation page. [priv]
- **Regions.** The reasoning guide's FAQ says SambaNova hosts models (it answers this for DeepSeek-R1) mainly in US data centres, with some in Japan; no region choice for SambaCloud was found. [reasonpg]

## Notes for agents and harnesses

- **Caching is narrow.** One model caches at a time (the blog and the pricing page disagree on which), so cost models that assume cached rates elsewhere do not hold. [cache, price]
- **Strict schemas are not enforced.** The function-calling page says `strict: false` is the only value enforced today, so `strict: true` gives best-effort matching, not guaranteed conformity. [fc]
- **Two wire formats, one host.** The OpenAI client uses `https://api.sambanova.ai/v1`; the Anthropic setup sets `ANTHROPIC_BASE_URL` to `https://api.sambanova.ai` and lets the SDK add the path. [overview, anth]
- **Preview models are for evaluation.** The models page says preview models are not for production. [models]
- **Effort affects tool calls on gpt-oss-120b.** The function-calling page ties higher reasoning effort to better tool-call quality on that model. [fc]
- **The free tier is small.** 20 requests and 200,000 tokens a day per model limit how far an agent loop can run on it. [rate]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| overview | https://docs.sambanova.ai/cloud/docs/get-started/overview | L | 2026-10-03 |
| models | https://docs.sambanova.ai/cloud/docs/get-started/supported-models | L | 2026-10-03 |
| rate | https://docs.sambanova.ai/docs/en/models/rate-limits | L | 2026-10-03 |
| fc | https://docs.sambanova.ai/docs/en/features/function-calling | L | 2026-10-03 |
| anth | https://sambanova.ai/blog/sambacloud-now-supports-the-anthropic-messages-api | L | 2026-10-03 |
| cache | https://sambanova.ai/blog/prompt-caching-on-sambacloud-faster-cheaper-inference | L | 2026-10-03 |
| priv | https://community.sambanova.ai/t/privacy-data-use-in-developer-tier/899 | A | 2026-10-03 |
| price | https://cloud.sambanova.ai/plans/pricing | L | 2026-10-03 |
| reasonpg | https://docs.sambanova.ai/docs/en/build/reasoning.md | L | 2026-10-03 |
| index | https://docs.sambanova.ai/docs/_llms/v2-2-3.md | L | 2026-10-03 |
