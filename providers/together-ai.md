---
last_checked: 2026-10-03
volatility: VOLATILE (catalogue, prices, limits and feature support change often)
kind: inference host
sources:
  - https://docs.together.ai/docs/quickstart
  - https://docs.together.ai/docs/rate-limits
  - https://docs.together.ai/docs/inference-models
  - https://www.together.ai/pricing
  - https://docs.together.ai/docs/inference/chat/reasoning
  - https://docs.together.ai/docs/function-calling
  - https://docs.together.ai/docs/json-mode
  - https://docs.together.ai/docs/batch-inference
  - https://docs.together.ai/docs/privacy-and-security
  - https://docs.together.ai/docs/inference/pricing
---

# Together AI

inference host

Together AI runs open-weight and some partner models for API use on its own GPU cloud, and also sells dedicated endpoints, fine-tuning and GPU clusters. Serverless inference is per-token and best-effort; dedicated endpoints and clusters are billed by the GPU-hour. The serverless catalogue is mostly open-weight models from several makers, so the same model is often available from other hosts in this folder as well. [quick, rate, price]

## Models offered

Serverless chat, vision, image, video and audio models. The serverless catalogue read on 2026-10-03 lists, among others, DeepSeek (`deepseek-ai/DeepSeek-V4-Flash-0731`, `deepseek-ai/DeepSeek-V4-Pro-0813`, `deepseek-ai/DeepSeek-V4.1-Flash`), Moonshot (`moonshotai/Kimi-K3`), Z.ai (`zai-org/GLM-5.2`, `zai-org/GLM-5.3`, `zai-org/GLM-5.3-Flash`), MiniMax (`MiniMaxAI/MiniMax-M3`), OpenAI's open-weight `openai/gpt-oss-120b` (gpt-oss-20b is not listed), Meta (`meta-llama/Llama-3.3-70B-Instruct-Turbo`) and five Qwen models, among them `Qwen/Qwen3.8-2.4T-A95B` and `Qwen/Qwen3.8-Flash`. Model files in scope: [DeepSeek V4 Pro](../models/deepseek/deepseek-v4-pro.md), [DeepSeek Flash](../models/deepseek/deepseek-flash.md), [Kimi K3](../models/moonshot/kimi-k3.md), [GLM 5.3](../models/zai/glm-5.3.md), [GLM 5.2](../models/zai/glm-5.2.md), [MiniMax M3](../models/minimax/MiniMax-M3.md), [gpt-oss-120b](../models/openai/gpt-oss-120b.md), [Qwen3.8 2.4T A95B](../models/alibaba/qwen3.8-2.4t-a95b.md) and [Qwen3.8 Flash](../models/alibaba/qwen3.8-flash.md). The catalogue lists Qwen3.5 9B, MiniMax M3 and Kimi K3 as vision models. Embedding, rerank and moderation models are described as not offered serverless. Quantisation is stated per model and varies (for example FP4 for DeepSeek V4 Flash, NVFP4 for V4 Pro, MXFP4 for gpt-oss-120b, FP8 for Llama 3.3 70B). Chat context windows in the catalogue run from 32,768 tokens to 1,048,576 (DeepSeek V4 Flash and Pro, Kimi K3; GLM-5.3 is listed at 1,048,575 and MiniMax M3 at 524,288). The catalogue gives no retirement policy. [models, reason, price]

## API surface

- **Protocol.** OpenAI-compatible: `https://api.together.ai/v1`, usable with the OpenAI SDK by changing the base URL, plus Together's own REST API. No Anthropic-compatible endpoint was found in the pages read. [quick]
- **Auth.** A bearer key (`TOGETHER_API_KEY`, which the SDKs read). [quick]
- **SDKs.** `together` (Python) and `together-ai` (TypeScript). [quick]
- **Model ids.** `org/model`, taken from the Hugging Face style namespace, for example `MiniMaxAI/MiniMax-M3`, `openai/gpt-oss-120b` or `meta-llama/Llama-3.3-70B-Instruct-Turbo`. [quick, models]

## Feature parity

Parity is measured against each maker's own API; most models here are open-weight, so the maker often has no first-party API to compare with.

- **Reasoning and effort.** Hybrid models (DeepSeek V4 Pro 0813, GLM-5.2, Kimi K3, MiniMax M3) are toggled with `reasoning: {"enabled": true|false}`. gpt-oss models take `reasoning_effort` of `low`, `medium` (the recommended default) or `high`, and the page advises `max_tokens` of about 30,000 at `high`. An alternative is `chat_template_kwargs` with `thinking` or `enable_thinking`. Reasoning text comes back in a `reasoning` field for DeepSeek V4 Pro and gpt-oss, in `reasoning_content` for GLM-5.2, Kimi K3 and MiniMax M3, and inside `<think>` tags in `content` for DeepSeek-R1. Interleaved thinking between tool calls is the default; preserved thinking across turns needs `clear_thinking: false` in `chat_template_kwargs`, with earlier reasoning sent back. Reasoning tokens are billed as completion tokens and show in `usage.completion_tokens_details.reasoning_tokens`. [reason]
- **Tools.** OpenAI-style function calling, including parallel calls (one function several times, or several functions in one response) and tool use with images on vision-language models; support is per model and the page points to the catalogue. The `tool_choice` values and any strict mode are not described on the page read. [fc]
- **Structured output.** `response_format` with `type: "json_schema"`, plus a regex mode. The docs advise telling the model to answer only in JSON and putting a plain-text copy of the schema in the prompt, warn that output truncated by `max_tokens` is invalid JSON (`finish_reason: "length"`), and say a malformed example in a prompt is copied. It works with reasoning and vision models. [json]
- **Prompt caching.** Automatic and prefix-based (only the longest matching prefix counts) on the serverless chat models that show a cached-input price, with no header, parameter or toggle; the cache is shared across the fleet, entries are evicted as traffic shifts, hits are not guaranteed and retention cannot be set. The page points to dedicated endpoints for predictable caching. [price2, price]
- **Batch.** A Batch API takes JSONL with a `custom_id`, with a fixed, best-effort 24-hour completion window, up to 50,000 requests and 100 MB per file, 10 MB a line and 30B enqueued tokens per model, and a separate rate-limit pool. A 50 percent discount applies only to selected serverless models (the page names Llama 3.3 70B Instruct Turbo and Whisper large v3); dedicated-endpoint batches get none. [batch]
- **Vision, long context, streaming.** Vision models and image inputs are served; function calling also works with images. Streaming is supported. Context windows are per model. [quick, models, fc]

## Pricing

Serverless is per token, from about $0.0015 to $4.50 per million tokens depending on the model (the pricing page's range), with a separate cached-input rate on some models. Dedicated endpoints are per GPU-hour (the page lists $5.49 an hour for an H100 and $8.99 for a B200, on demand), fine-tuning is per token with a minimum charge of $4 to $100 by model and method, and GPU clusters are on demand or reserved in terms from 7 days upward at lower hourly prices (for example an H100 at $3.99 on demand, $3.69 for 7 to 30 days and $3.19 for 91 to 180 days). Code Sandbox (per vCPU-hour and GiB-hour) and Code Interpreter ($0.03 per 60-minute session) are billed separately. Per-model rates are on the model pages and are not repeated here. [price]

## Limits and data

- **Rate limits.** The rate-limit page gives no tier table or numbers. It says most users do not meet rate limits, that limits can apply at high traffic, that a 429 means lower the request rate and avoid bursts and a 503 means retry with backoff, and that serverless performance is best effort; provisioned throughput with an SLA is arranged through sales. [rate]
- **Retention and training.** By default Together stores prompts and responses and may use them for product improvement; it does not share them with third parties, and they can be deleted. Sharing data for training other models is opt-in and off by default. Turning off the "Store prompts and model responses" setting (on by default) enables zero data retention, under which request content is not persisted or used for any secondary purpose. [priv]
- **Regions.** Serverless endpoints have no region selection. Dedicated endpoints and EU-region deployments for enterprise customers are the route for residency. The page says third-party models hosted on Together run in its North American data centres. [priv]
- **Compliance.** The privacy page read does not state certifications. [priv]

## Notes for agents and harnesses

- **No shared effort scale.** gpt-oss uses three named levels and the hybrid models only toggle, so an OpenAI-style `reasoning_effort` sent to a Kimi or GLM model has no graded meaning there; the page documents `reasoning.enabled` for those models. [reason]
- **The reasoning field name differs by model.** A client that reads only `reasoning_content` misses the `reasoning` field that DeepSeek V4 Pro and gpt-oss use, and DeepSeek-R1 puts its reasoning inside `<think>` tags in `content`. [reason]
- **Output budget.** The reasoning page suggests about 30,000 `max_tokens` for gpt-oss at `high`; the JSON page notes that output cut off by `max_tokens` is invalid JSON with `finish_reason: "length"`. [reason, json]
- **Same model, different host.** A Together id and the maker's own model are not guaranteed to share quantisation, context length or tool-call parsing; the catalogue states quantisation per model. [models]
- **Best effort.** Serverless has no throughput guarantee; the rate-limit page points workloads that need one to provisioned throughput. [rate]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| quick | https://docs.together.ai/docs/quickstart | L | 2026-10-03 |
| rate | https://docs.together.ai/docs/rate-limits | L | 2026-10-03 |
| models | https://docs.together.ai/docs/inference-models | L | 2026-10-03 |
| price | https://www.together.ai/pricing | L | 2026-10-03 |
| price2 | https://docs.together.ai/docs/inference/pricing | L | 2026-10-03 |
| reason | https://docs.together.ai/docs/inference/chat/reasoning | L | 2026-10-03 |
| fc | https://docs.together.ai/docs/function-calling | L | 2026-10-03 |
| json | https://docs.together.ai/docs/json-mode | L | 2026-10-03 |
| batch | https://docs.together.ai/docs/batch-inference | L | 2026-10-03 |
| priv | https://docs.together.ai/docs/privacy-and-security | L | 2026-10-03 |
