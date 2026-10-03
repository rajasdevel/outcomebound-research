---
last_checked: 2026-10-03
volatility: VOLATILE (catalogue, preview status, limits and prices change often)
kind: inference host
sources:
  - https://console.groq.com/docs/overview
  - https://console.groq.com/docs/models
  - https://console.groq.com/docs/rate-limits
  - https://console.groq.com/docs/reasoning
  - https://console.groq.com/docs/structured-outputs
  - https://console.groq.com/docs/prompt-caching
  - https://console.groq.com/docs/batch
  - https://console.groq.com/docs/your-data
  - https://console.groq.com/docs/production-readiness/optimizing-latency
  - https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale
---

# Groq

inference host

Groq runs a small set of open-weight models on its own Language Processing Unit hardware and sells access as GroqCloud, with an OpenAI-compatible API. Its catalogue is short, lists a throughput figure for each model, and divides models into production and preview. It also serves speech-to-text, text-to-speech and content-safety models. On 2025-12-24 Groq announced a non-exclusive licensing agreement with Nvidia for its inference technology, under which some Groq leaders joined Nvidia; the announcement says Groq continues as an independent company and GroqCloud continues to operate without interruption. [overview, models, press]

## Models offered

Production models on the models page read: `llama-3.1-8b-instant` and `llama-3.3-70b-versatile` (131K-token context; 131K and 32K maximum output), OpenAI's [gpt-oss-120b](../models/openai/gpt-oss-120b.md) and [gpt-oss-20b](../models/openai/gpt-oss-20b.md) (131,072-token context; reasoning, browser search and code execution), and `whisper-large-v3` and `whisper-large-v3-turbo`. Preview models, which the page says are for evaluation only and may be discontinued at short notice: [Qwen 3.8 27B](../models/alibaba/qwen3.8-27b.md) (`qwen/qwen3.8-27b`), [MiniMax M2.7](../models/minimax/MiniMax-M2.7.md) (`minimaxai/minimax-m2.7`, 196K context), `openai/gpt-oss-safeguard-20b`, two Llama Prompt Guard models and Orpheus text-to-speech models. The page gives throughput figures from about 260 to 1,000 tokens a second depending on model; those are Groq's own numbers. The live list is `GET https://api.groq.com/openai/v1/models`. [models]

## API surface

- **Protocol.** OpenAI-compatible Chat Completions at `https://api.groq.com/openai/v1`, and a Responses API. No Anthropic-compatible endpoint was found in the pages read. [overview]
- **Auth.** A bearer key (`GROQ_API_KEY`). [overview]
- **SDKs.** Python and JavaScript clients; OpenAI-compatible libraries work with the base URL changed. [overview]
- **Model ids.** The maker's name where one exists, for example `openai/gpt-oss-20b`. [overview]
- **Built-in tools.** Browser search and code execution (for the gpt-oss models) and remote MCP tools are listed. [overview, models]
- **Service tiers.** `on_demand` (consistent low latency), `flex` (10 times the current rate limits as capacity allows, with rapid timeouts when resources are constrained), `auto` (on-demand limits first, then flex when they are exceeded) and `batch`. [tiers]

## Feature parity

- **Reasoning and effort.** `reasoning_effort` takes `low`, `medium` or `high` for gpt-oss models, and `none`, `default`, `low`, `medium` or `high` for Qwen 3.8 27B. `reasoning_format` (`parsed`, `raw` in `<think>` tags, or `hidden`) applies to non-gpt-oss models; gpt-oss models do not accept it. `include_reasoning` controls whether reasoning is returned and cannot be sent together with `reasoning_format`. gpt-oss models return reasoning in a `reasoning` field by default unless `include_reasoning: false` is sent. [reason]
- **Tools.** OpenAI-style tool use, plus the built-in tools above for gpt-oss; per-model tool support is shown on the models page. [overview, models]
- **Structured output.** `response_format` with `json_schema`: `strict: true` uses constrained decoding and guarantees schema conformity, but needs every field required and `additionalProperties: false`, and covers gpt-oss 20B and 120B and Qwen 3.8 27B. `strict: false` is best effort. JSON object mode gives syntactically valid JSON with no schema guarantee, for models without schema support. Structured outputs do not work with streaming or with tool use. [struct]
- **Prompt caching.** Automatic, no extra fee, for gpt-oss 20B, gpt-oss 120B and a gpt-oss safety model. Cached input tokens cost 50 percent less and do not count toward rate limits (the rate-limit page says the same). Entries expire after two hours without use and live only in volatile memory; minimum cacheable length is 128 to 1,024 tokens by model; `prompt_tokens_details.cached_tokens` reports hits. [cache]
- **Batch.** 50 percent off, a window of 24 hours to 7 days, up to 50,000 lines and 200 MB per file, for chat completions, transcription and translation, with rate limits separate from the standard API. It does not stack with the caching discount. Expired jobs bill only completed requests. [batch, tiers]
- **Vision, long context, streaming.** Vision, speech and moderation models are in the product list; context windows are per model and streaming is supported on the chat endpoint. [overview, models]
- **Not offered.** The catalogue read holds no closed-lab models (Claude, GPT, Gemini); every language model on it is open-weight. [models]

## Pricing

Per token for text models and per hour for speech recognition, with a lower price for cached input, a batch discount, and service tiers. The models page lists gpt-oss-20b at $0.075 input and $0.30 output and gpt-oss-120b at $0.15 and $0.60 per million tokens, Qwen 3.8 27B (preview) at $0.80 and $4.00, the two Llama models as enterprise pricing, and Whisper Large V3 and V3 Turbo at $0.111 and $0.04 per audio hour. A free plan and a Developer plan exist, and the Developer plan adds Batch and Flex. Prices change by model and are on Groq's pricing page. [models, rate]

## Limits and data

- **Rate limits.** Per organisation and model: requests and tokens per minute and per day, input and output tokens per minute, and audio seconds per hour and per day; the first limit reached applies. The free plan's example for `openai/gpt-oss-20b` is 30 requests a minute, 1,000 a day, 8,000 tokens a minute and 200,000 a day; the models page gives the Developer plan 250,000 tokens and 1,000 requests a minute for the gpt-oss models. Headers such as `x-ratelimit-limit-requests`, `x-ratelimit-remaining-tokens` and `x-ratelimit-reset-tokens` report capacity; `retry-after` appears only after a limit is hit, with a 429. [rate, models]
- **Retention.** By default Groq does not retain inference data, except temporary logs of up to 30 days for troubleshooting errors or investigating suspected abuse; usage metadata without inputs or outputs is collected. Batch files (30 days unless deleted) and fine-tuning weights and datasets (until deleted) are stored. A zero-data-retention toggle in Data Controls stops the reliability logging and disables features that need storage, such as batch. [data]
- **Regions.** Retained customer data is stored in Google Cloud buckets in the United States. No region selection was found in the page read. [data]
- **Training.** The data page does not state a training policy. [data]

## Notes for agents and harnesses

- **Effort vocabularies differ by model.** gpt-oss accepts three levels and no `none`; Qwen 3.8 27B accepts `none` and `default` as well. One fixed value sent to every model is not valid for all of them. [reason]
- **Reasoning display options depend on the family.** `reasoning_format` is not accepted by gpt-oss, and `include_reasoning` cannot be combined with it. [reason]
- **Strict JSON excludes streaming and tools.** A request that needs tools and a schema at the same time cannot use structured outputs here; the structured-output page names best-effort mode with validation and retries as the fallback. [struct]
- **Preview models can be withdrawn.** The models page says preview models may be discontinued at short notice and are for evaluation only. [models]
- **Caching only on gpt-oss.** Only the three gpt-oss models cache, so cached-rate cost estimates apply only to them. [cache]
- **Flex and auto trade reliability for capacity.** `auto` falls back to flex when on-demand limits are exceeded, at the cost of rapid timeouts when capacity is short. [tiers]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| overview | https://console.groq.com/docs/overview | L | 2026-10-03 |
| models | https://console.groq.com/docs/models | L | 2026-10-03 |
| rate | https://console.groq.com/docs/rate-limits | L | 2026-10-03 |
| reason | https://console.groq.com/docs/reasoning | L | 2026-10-03 |
| struct | https://console.groq.com/docs/structured-outputs | L | 2026-10-03 |
| cache | https://console.groq.com/docs/prompt-caching | L | 2026-10-03 |
| batch | https://console.groq.com/docs/batch | L | 2026-10-03 |
| data | https://console.groq.com/docs/your-data | L | 2026-10-03 |
| tiers | https://console.groq.com/docs/production-readiness/optimizing-latency | L | 2026-10-03 |
| press | https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale | L | 2026-10-03 |
