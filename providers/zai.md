---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: first-party lab API
sources:
  - https://docs.z.ai/guides/overview/overview
  - https://docs.z.ai/guides/overview/pricing
  - https://docs.z.ai/guides/llm/glm-5.3.md
  - https://docs.z.ai/api-reference/llm/chat-completion.md
  - https://docs.z.ai/guides/capabilities/struct-output.md
  - https://docs.z.ai/legal-agreement/privacy-policy.md
  - https://docs.z.ai/llms.txt
---

# Z.ai (Zhipu) API

first-party lab API

Zhipu AI, trading under the name Z.ai, trains the GLM models and sells them through its own platform (z.ai, API at `https://api.z.ai/api`). The platform serves text, vision, speech, image and video models over three request protocols, and sells a separate GLM Coding Plan subscription for coding tools alongside pay-as-you-go API access. The privacy policy says its group companies and service providers are typically located in Singapore, where the services are generally provided. [models, privacy, glm53]

## Models offered

The overview page names GLM-5.3 as the flagship (1M-token context, 128K output) and GLM-5.3-Flash (a native multimodal model) with a faster GLM-5.3-FlashX at about 200 tokens a second. It also lists GLM-5.2 (1M), GLM-5.1, GLM-5, GLM-4.7 and GLM-4.6 (200K), GLM-4.5 (128K), free GLM-4.7-Flash and GLM-4.5-Flash, the GLM-4.6V vision model, GLM-OCR, the GLM-ASR-2512 speech model, and image and video generators (GLM-Image, CogView-4, CogVideoX-3). [models]

| Model file | API id | Note |
| --- | --- | --- |
| [GLM-5.3](../models/zai/glm-5.3.md) | `glm-5.3` | 1M context, 128K output, reasoning always on |
| [GLM-5.3-Flash](../models/zai/glm-5.3-flash.md) | `glm-5.3-flash` | native multimodal |
| [GLM-5.3-FlashX](../models/zai/glm-5.3-flashx.md) | `glm-5.3-flashx` | faster serving tier |
| [GLM-5.2](../models/zai/glm-5.2.md) | `glm-5.2` | previous generation, 1M context; on the overview and in the chat reference |

The maker README says the Coding Plan routes requests for GLM-5.2 and GLM-5.1 to GLM-5.3. The lineage and licences are in the [maker README](../models/zai/README.md). Model ids are lower case. [models, chat-ref]

## API surface

- **Protocols.** Three, per the GLM-5.3 page: OpenAI Chat Completions (shown there at `https://api.z.ai/api/coding/paas/v4`), OpenAI Responses (`https://api.z.ai/api/v1`) and Anthropic Messages (`https://api.z.ai/api/anthropic`). The chat reference gives the base `https://api.z.ai/api`, and the maker README records `https://api.z.ai/api/paas/v4/` as the pay-as-you-go Chat Completions path and the `coding` path as the Coding Plan one. [glm53, chat-ref]
- **Auth.** An API key from the platform. [glm53]
- **SDKs.** An official Python SDK (`zai-sdk`) and a Java SDK; the OpenAI Python SDK works against the Chat Completions base URL. [glm53]
- **Reasoning parameters.** `thinking.type` of `enabled` or `disabled` (default `enabled`; GLM-5.3 and GLM-5.3-Flash accept only `enabled`) and `reasoning_effort`. [chat-ref]
- **Model ids.** Lower-case with the version (`glm-5.3`, `glm-5.3-flash`). [models]

## Feature parity

First-party; the chat reference is the main source. [chat-ref]

- **Reasoning and effort.** GLM-5.3 and GLM-5.3-Flash take `low`, `high` and `max` (default `max`) and always think; GLM-5.2 maps `none` and `minimal` to no thinking, `low` and `medium` to `high` and `xhigh` to `max`; other models accept the longer list. The maker README adds that on the Coding Plan endpoints a request to disable thinking on GLM-5.3 becomes `low` instead of failing, and that the API default `clear_thinking` drops earlier reasoning from context. [chat-ref, glm53]
- **Tools.** Up to 128 functions per request; `tool_choice` accepts only `auto`; `tool_stream` (streaming of tool-call arguments) works on the GLM-5.3, 5.2, 5.1, 5, 4.7 and 4.6 series, and is off by default. The maker README says the Flash models take functions only and text models also take web-search and retrieval tool types. [chat-ref]
- **Structured output.** `response_format: {"type": "json_object"}` on text models, with the schema described in the system message; the page lists glm-5, 4.7, 4.6 and 4.5 as supporting it and describes validating the result in your own code afterwards. No constrained schema mode is documented. [struct]
- **Caching.** Implicit; cached input is typically 80 percent cheaper, and cache storage is free for a limited time. [pricing]
- **Batch.** Not found in the pages read.
- **Long context.** 1M tokens on GLM-5.3, GLM-5.3-Flash and FlashX; `max_tokens` up to 131,072 with reasoning counted. [models, chat-ref]
- **Vision.** GLM-5.3-Flash is multimodal and the GLM-5.3 page says it takes text input only for now; separate vision, OCR and speech models exist. [models, glm53]
- **Streaming.** Supported, including tool-argument streaming. [glm53, chat-ref]
- **Sampling.** `temperature` 0.0 to 1.0, default 1.0 on the GLM-5.x series. [chat-ref]

## Pricing

Per million tokens, with a free tier for two small models (GLM-4.7-Flash and GLM-4.5-Flash) and cheap Flash variants (GLM-4.7-FlashX from $0.07 per million input tokens); GLM-5.3 lists $1.40 per million input tokens on the page. Cached input is typically 80 percent off standard. Web search costs $0.01 per use. Vision, OCR, speech, image and video models bill per token, per unit or per output at fixed rates. The GLM Coding Plan is a subscription with a points-based quota, where off-peak use of GLM-5.3 counts as half points. Per-model prices are in the model files. [pricing, glm53]

## Limits and data

- **Rate limits.** The rate-limit page redirects to a console page that returned only navigation text, so per-model and per-tier numbers were not read. The maker README lists error codes 1302, 1305 and 1308 to 1321 as rate-related. [llms]
- **Regions.** The privacy policy says services are generally provided from Singapore, and no regional endpoints were found in the pages read. [privacy]
- **Retention and training.** For API services the policy states the company does not store the content customers or their end users provide or generate; data is processed in real time and not kept on its servers. Account personal data is retained as long as the account exists, and API customers' data is deleted after the terms end unless law requires otherwise. Data transfers follow legally recognised mechanisms without naming countries beyond Singapore. The policy mentions training on publicly available internet data and says nothing about training on customer content beyond the no-storage statement. No separate zero-retention programme is described, since the default statement already says content is not stored. [privacy]

## Notes for agents and harnesses

- **Effort mapping.** The chat reference gives GLM-5.3 and GLM-5.3-Flash only `low`, `high` and `max`; the maker README records that `medium` or `xhigh` gets an error on the pay-as-you-go API while the Coding Plan endpoints map those names, so the same field behaves differently across the two routes. [chat-ref]
- **Thinking cannot be disabled on GLM-5.3 or GLM-5.3-Flash** via the API; sending `disabled` is an error there. [chat-ref]
- **Preserved thinking.** `clear_thinking` defaults to true on the API, so earlier reasoning is dropped; keeping it means returning earlier `reasoning_content` whole and unedited (maker README).
- **Tool choice.** Only `auto` is accepted, so a forced tool call needs another mechanism such as a prompt or application-side schema. [chat-ref]
- **JSON output is not enforced.** The platform documents prompting for a schema and validating the reply in the caller's own code. [struct]
- **Coding Plan versus API.** The GLM-5.3 page says users with a GLM Coding Plan subscription can for now reach the model only through the Chat Completions protocol; plan base URLs differ from the pay-as-you-go ones. [glm53]
- **Docs move.** Several documentation paths redirect or return 404; `llms.txt` is the index. [llms]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| models | https://docs.z.ai/guides/overview/overview | L | 2026-10-03 |
| pricing | https://docs.z.ai/guides/overview/pricing | L | 2026-10-03 |
| glm53 | https://docs.z.ai/guides/llm/glm-5.3.md | L | 2026-10-03 |
| chat-ref | https://docs.z.ai/api-reference/llm/chat-completion.md | L | 2026-10-03 |
| struct | https://docs.z.ai/guides/capabilities/struct-output.md | L | 2026-10-03 |
| privacy | https://docs.z.ai/legal-agreement/privacy-policy.md | L | 2026-10-03 |
| llms | https://docs.z.ai/llms.txt | L | 2026-10-03 |
