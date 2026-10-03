---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: first-party lab API
sources:
  - https://api-docs.deepseek.com/quick_start/pricing
  - https://api-docs.deepseek.com/quick_start/rate_limit
  - https://api-docs.deepseek.com/guides/anthropic_api
  - https://api-docs.deepseek.com/guides/thinking_mode
  - https://api-docs.deepseek.com/guides/json_mode
  - https://api-docs.deepseek.com/guides/responses_api/
  - https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html
---

# DeepSeek API

first-party lab API

DeepSeek, a Chinese lab, trains the DeepSeek models and sells them through a pay-as-you-go API at `https://api.deepseek.com`. One endpoint family serves both current models and speaks three request formats: Chat Completions, the OpenAI Responses format and the Anthropic Messages format. The weights are also published for self-hosting (see the model files). The company's privacy policy says user data is stored in the People's Republic of China, which is the main data-location fact for a buyer. [pricing, responses, anthropic, privacy]

## Models offered

Two ids on the pricing page: `deepseek-flash` (DeepSeek-V4.1-Flash, with vision, tool calls and JSON output) and `deepseek-v4-pro` (DeepSeek-V4-Pro-0813, no vision). Both have a 1M-token context and 384K maximum output. The older names `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` are still accepted and routed to Flash at Flash prices. [pricing]

| Model file | API id |
| --- | --- |
| [DeepSeek Flash (V4.1-Flash)](../models/deepseek/deepseek-flash.md) | `deepseek-flash` |
| [DeepSeek V4 Pro](../models/deepseek/deepseek-v4-pro.md) | `deepseek-v4-pro` |

The maker README records that `deepseek-chat` and `deepseek-reasoner` were announced for retirement after 2026-07-24 and are not on the pricing page, and that `deepseek-v4-flash` still resolves to the Flash model. The [maker README](../models/deepseek/README.md) has the lineage. [pricing]

## API surface

- **Chat Completions.** `https://api.deepseek.com`, OpenAI-shaped, stateless: the client sends the whole history each time (maker README). Beta features (strict tool schemas, prefix completion, fill-in-the-middle) use `https://api.deepseek.com/beta` (maker README).
- **Responses format.** The same base URL accepts the OpenAI Responses format, adapted for Codex. The guide names `deepseek-flash` as the supported model, while the API reference and the maker README name both ids. It supports streaming, image input, function tools (partly), `tool_choice`, `temperature`, `top_p`, `logprobs` and `effort`; it silently ignores unsupported fields and does not support `conversation`, `previous_response_id`, `store`, prompt-cache settings, file search, web search or the code interpreter. `summary` is accepted but no summary is generated, and only the `apply_patch` custom tool is accepted for Codex. [responses]
- **Anthropic format.** `https://api.deepseek.com/anthropic`, used by pointing `ANTHROPIC_BASE_URL` at it with a DeepSeek key. Supported: `max_tokens`, `stop_sequences`, `stream`, `system`, `temperature`, tool definitions and `tool_choice` (`none`, `auto`, `any`, `tool`). Partly supported: thinking (`budget_tokens` ignored), `top_p` (thinking mode only, 0.95 or more), `metadata` (only `user_id`) and `output_config` (only effort). Not supported: document content, redacted thinking, MCP tools, code-execution tools, `cache_control` and `top_k`. Claude model names are mapped: `claude-opus*` to `deepseek-v4-pro` at Pro prices, `claude-sonnet*` and `claude-haiku*` and any unknown name to `deepseek-flash`. [anthropic]
- **Auth.** An API key (on the Anthropic format, set as `ANTHROPIC_API_KEY`). A `user_id` field (letters, digits, `-` and `_`, up to 512 characters) separates end users under one account for content-safety, KV-cache and scheduling isolation. [ratelimit, anthropic]
- **SDKs.** No DeepSeek SDK was found in the pages read; the OpenAI and Anthropic SDKs are the documented clients. [anthropic, responses]
- **Model ids.** Plain names without a vendor prefix; the Pro id carries a version. [pricing]

## Feature parity

This is the maker's own API; parity here means what each format passes through. [anthropic, thinking, json]

- **Reasoning and effort.** Thinking is on by default at `high` effort and is switched with `thinking: {"type": "enabled" | "disabled"}`. Effort accepts `low`, `high` and `max`; other names are mapped (`minimal` and `low` to low, `medium`, `high` and `xhigh` to high, `max` and `ultra` to max). On the Anthropic format, `reasoning.effort: none` turns thinking off. In thinking mode `temperature`, `presence_penalty` and `frequency_penalty` have no effect and raise no error; `top_p` works only from 0.95 to 1.0, and a lower value is treated as 0.95. [thinking]
- **Reasoning content.** With a `tools` parameter in the request, all earlier `reasoning_content` must be sent back on every later request, including turns with no tool call; without tools it is ignored. [thinking]
- **Tools.** Function calling on all three formats; a mid-conversation tool call that the model did not write can be inserted only through the Anthropic and Responses formats (maker README). [anthropic]
- **Structured output.** `response_format: {"type": "json_object"}`; the prompt must contain the word json and an example, `max_tokens` must leave room, and the page warns that empty content can occasionally come back. The page does not describe JSON Schema output; strict tool schemas are a beta feature (maker README). [json]
- **Caching.** Automatic, priced as cache-hit and cache-miss input; the maker README describes it as best effort on disk. The Anthropic format does not support `cache_control`, and the Responses format manages the cache without parameters. [pricing, anthropic, responses]
- **Batch.** Not found in the pages read.
- **Long context.** 1M tokens in, 384K out. [pricing]
- **Vision.** On `deepseek-flash` only. [pricing]
- **Streaming.** Supported (the keep-alive rule below applies to it). [ratelimit]

## Pricing

Per million tokens, with separate rates for input cache hits, cache misses and output, and a second price by time of day: peak is 01:00 to 04:00 and 06:00 to 10:00 UTC on weekdays outside Chinese public holidays, and every other hour is off-peak at half the price. Cache hits cost a small fraction of cache misses on both models. Fees come out of a topped-up or granted balance, granted first. The page lists no per-seat or subscription plan. Per-model prices are in the model files. [pricing]

## Limits and data

- **Rate limits.** Concurrency, not tokens per minute: 2,500 concurrent requests for `deepseek-flash` and 500 for `deepseek-v4-pro` per account, with HTTP 429 above that. A request counts from submission until the model finishes. A capacity-expansion request is free. While a request waits, the server sends empty lines (non-streaming) or SSE keep-alive comments (streaming); a request that has not started inference after 10 minutes is closed. [ratelimit]
- **Regions.** One global service; the privacy policy says data is collected, processed and stored in the PRC, and may also be stored outside the user's own country. No regional endpoint was found. [privacy]
- **Retention and training.** The policy (updated 2026-02-10) gives account and input data retention "for as long as you have an account" and lists training its models as a stated purpose; it does not say outright whether API inputs and outputs are used for training. It grants a right to opt out of training and a deletion right, both by email. It also says that data collected from end users of applications that developers build on its open platform is not covered by the policy. No zero-data-retention option was found, and the pages read describe no API-specific data terms. [privacy]

## Notes for agents and harnesses

- **Data location is a gate.** A workload that cannot leave a jurisdiction cannot use this endpoint; self-hosting the published weights is the route the model files describe. [privacy]
- **Sampling is a no-op in thinking mode.** A harness that tunes `temperature` for a thinking run changes nothing, and no error shows. [thinking]
- **Reasoning content goes back with tools.** Dropping `reasoning_content` from history in a tool loop breaks the documented rule, so client libraries that strip unknown fields matter here. [thinking]
- **Effort mapping.** A four-or-five-level scale maps onto three real levels, so `medium`, `high` and `xhigh` all run as `high`; three levels in a sweep can run identically. [thinking]
- **Claude client against this endpoint.** Names beginning `claude-opus` bill at Pro prices, other names run on Flash, so the model a Claude-shaped client selects is not the one it names; document, MCP and code-execution blocks are not accepted. [anthropic]
- **Concurrency is the limit.** Requests above the per-model counts return 429, long waits show as keep-alive traffic and not as errors, and a request that has not started inference after 10 minutes is closed. [ratelimit]
- **Peak pricing.** Time of day changes price by a factor of two, off-peak being half. [pricing]
- **Empty JSON.** In JSON mode the page says content may occasionally come back empty. [json]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| pricing | https://api-docs.deepseek.com/quick_start/pricing | L | 2026-10-03 |
| ratelimit | https://api-docs.deepseek.com/quick_start/rate_limit | L | 2026-10-03 |
| anthropic | https://api-docs.deepseek.com/guides/anthropic_api | L | 2026-10-03 |
| thinking | https://api-docs.deepseek.com/guides/thinking_mode | L | 2026-10-03 |
| json | https://api-docs.deepseek.com/guides/json_mode | L | 2026-10-03 |
| responses | https://api-docs.deepseek.com/guides/responses_api/ | L | 2026-10-03 |
| privacy | https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html | L | 2026-10-03 |
