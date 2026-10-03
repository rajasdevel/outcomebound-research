---
last_checked: 2026-10-03
volatility: VOLATILE (Model API catalogue, limits and prices change often)
kind: inference host
sources:
  - https://docs.baseten.co/
  - https://docs.baseten.co/llms.txt
  - https://docs.baseten.co/inference/model-apis/overview.md
  - https://docs.baseten.co/inference/model-apis/pricing-and-limits.md
  - https://docs.baseten.co/inference/model-apis/reasoning.md
  - https://docs.baseten.co/inference/structured-outputs.md
  - https://docs.baseten.co/inference/function-calling.md
  - https://docs.baseten.co/inference/async.md
  - https://docs.baseten.co/observability/security.md
  - https://docs.baseten.co/deployment/regional-deployments.md
---

# Baseten

inference host

Baseten is a platform for running models on managed GPU infrastructure. It has two sides. Model APIs are shared, hosted endpoints for a small set of curated models, billed per token. Dedicated Inference runs open-source, fine-tuned or custom models on dedicated GPUs that the customer configures, scales and releases, with Truss packaging, specialised inference engines, training, and a self-hosted option inside the customer's own cloud account. This file mainly covers the Model APIs. [home, ma]

## Models offered

The Model APIs overview lists 11 models: DeepSeek V4 Pro 0813, V4 Flash 0731 and V4.1 Flash; GLM 5.2, 5.2 Fast, 5.3, 5.3 Fast and 5.3 Flash; Kimi K3; `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B`; and `openai/gpt-oss-120b`. Context windows run from 128k (gpt-oss-120b) through 202k (Nemotron) to about 1,048k tokens, and maximum output from 128k to 384k (DeepSeek V4 Flash 0731); the page says these reflect the current serving configuration and can differ from a model's advertised maximum. Model files in scope: [DeepSeek V4 Pro](../models/deepseek/deepseek-v4-pro.md), [DeepSeek Flash](../models/deepseek/deepseek-flash.md), [Kimi K3](../models/moonshot/kimi-k3.md), [GLM 5.3](../models/zai/glm-5.3.md), [GLM 5.3 Flash](../models/zai/glm-5.3-flash.md), [GLM 5.2](../models/zai/glm-5.2.md), [Nemotron 3 Ultra](../models/other/nemotron-3-ultra.md) and [gpt-oss-120b](../models/openai/gpt-oss-120b.md). "Fast" variants use the same weights with dedicated capacity, separate slugs, prices and rate limits, and fall back to base-model capacity when Fast capacity is unavailable. Eight of the 11 accept image input (not DeepSeek V4 Pro, V4 Flash 0731, Nemotron or gpt-oss-120b). Dedicated Inference can run any compatible open model. [ma]

## API surface

- **Protocols.** OpenAI-compatible Chat Completions at `https://inference.baseten.co/v1/chat/completions`, and an Anthropic Messages endpoint at `https://inference.baseten.co/v1/messages`, which the docs mark beta ("behavior may change before general availability"). The OpenAI endpoint is recommended for production. [ma]
- **Auth.** A Baseten API key, read from the `Authorization` header; with the Anthropic SDK, which sends `x-api-key` by default, the docs override the default headers. [ma]
- **SDKs.** The OpenAI SDK against the base URL; Baseten's CLI and the Truss library for dedicated deployments. [home]
- **Model ids.** `org/model` slugs, for example `deepseek-ai/DeepSeek-V4-Pro-0813` or `zai-org/GLM-5.3-Fast`; `/v1/models` lists the current set. [ma]
- **Inference engines (dedicated).** Engine-Builder-LLM (compiles dense models with TensorRT-LLM), BIS-LLM (large mixture-of-experts models with distributed inference) and BEI (embeddings, reranking and classification); vLLM and SGLang also run, and models are packaged with Truss. [home, struct, index]

## Feature parity

- **Reasoning and effort.** Most models reason by default; GLM 5.2 and Nemotron Ultra need opting in through `chat_template_args`. `reasoning_effort` values differ by model: DeepSeek V4 Pro, V4.1 Flash and Kimi K3 accept `none`, `low`, `high` and `max` (Kimi defaults to `max`, V4.1 Flash to `high`); DeepSeek V4 Flash 0731 and gpt-oss-120b accept `none`, `minimal`, `low`, `medium`, `high`, `xhigh` and `max` (defaults `high` and `medium`); GLM 5.2 and 5.2 Fast accept `none`, `high` and `max`; the GLM 5.3 family defaults to `high`. Thinking is always on for GLM 5.3: GLM 5.3 and 5.3 Flash treat `none` as low reasoning, and GLM 5.3 Fast rejects it with a 400. DeepSeek V4 Pro also needs `thinking: {"type": "enabled"}` with `reasoning_effort`. Reasoning arrives in `reasoning_content`, the answer in `content`, and reasoning tokens count in `completion_tokens`. `max_tokens` caps the whole completion; `reasoning.max_tokens` limits reasoning on DeepSeek V4 Flash 0731 only, which stops reasoning at 4,096 tokens by default, even at `max`. [reason]
- **Tools.** All Model API models support tool calling. `tool_choice` takes `auto` (default), `required`, `none` or a named function. Server-side web search, run by Baseten inside the same request, is in early access on enabled workspaces and models. The page advises small single-purpose tools and treating model-supplied arguments as untrusted input; `parallel_tool_calls` and `strict` are not discussed. [ma, fc]
- **Structured output.** `response_format` with a JSON schema (the docs show Pydantic with `beta.chat.completions.parse`) on every Model API model, and JSON mode. On dedicated engines it is unavailable with Lookahead speculative decoding (Engine-Builder-LLM) and in some BIS-LLM configurations, such as with the overlap scheduler. The docs advise two to three levels of nesting, basic types, temperature 0.1 to 0.3, and the schema with few-shot examples in the prompt. [ma, struct]
- **Prompt caching.** Prompt tokens served from the KV cache when a request reuses a prefix are billed at a discount, automatically and with no flag. An `x-session-affinity` header routes a conversation to one replica for better hit rates; the page says Claude Code, Codex and OpenCode send session ids that Baseten recognises. [price]
- **Batch.** Async inference queues requests for dedicated deployments, with webhooks, priorities 0 to 2 (0 first, and the default), retries, and a queue time that defaults to 10 minutes and can extend to 72 hours; it is not available on Model APIs, has no stated discount, and does not store outputs, so a webhook that fails after all retries loses the result. No batch API for Model APIs was found. [async]
- **Anthropic endpoint.** Beta; details of unsupported fields were not read. [ma]
- **Long context and streaming.** Per model, as above; sampling parameters (temperature, top_p, top_k, stop) depend on the model. [ma]

## Pricing

Model APIs are billed per million input and output tokens, by model, with a discount for cached prompt tokens; Fast variants have their own prices. Dedicated deployments are billed for the GPU resources they use (the pages read give no rates). A monthly workspace budget can send alerts or, if enforced, reject Model API requests once reached. Usage is available by key, user and model, and cost also by service tier, through the CLI, REST API and Prometheus metrics; usage data is kept for 92 days. [price]

## Limits and data

- **Rate limits.** Model APIs: an unverified Basic account gets 15 requests and 100,000 tokens a minute, a verified Basic account 120 and 500,000, Pro 120 and 1,000,000; Enterprise is custom. Limits replenish continuously. Split limits (uncached input and output separately, with cached input counting toward neither) are in early access, starting with DeepSeek V4.1 Flash; elsewhere cached and uncached input both count. `x-ratelimit-*` headers show limits and remaining capacity; a 429 means over limit (retry with backoff) and a 529 means no serving capacity, even within limits. Increases are requested on the website. For async on dedicated deployments the organisation cap is 12,000 requests a minute on the predict endpoint. [price, async]
- **Retention.** Zero data retention for synchronous inference: inputs, outputs and weights are not stored by default. Async inference keeps inputs until processing completes and does not store outputs. Existing users can keep data in hosted Postgres tables and delete it at any time. [sec]
- **Compliance and isolation.** SOC 2 Type II and HIPAA; GPUs never shared across users; a Kubernetes namespace per customer; annual third-party penetration tests; self-hosted deployment in the customer's VPC with Baseten running the control plane. A compliance policy, set by Baseten, fixes allowed frameworks and regions, and a deployment cannot go outside it. [sec]
- **Regions.** `us` and `eu` for GPU model deployments of verified organisations (CLI, REST API or dashboard), each served from a regional endpoint; not for shared CPU instances, chains or training jobs. Capacity is not reserved, so a deployment fails if it cannot be scheduled there, and a region cannot be changed in place. Without a region or policy, placement is global. Whether Model APIs themselves can be pinned to a region was not stated on the pages read. [region]
- **Training.** Not stated in the pages read. [sec]

## Notes for agents and harnesses

- **Reasoning is on by default for most models.** `none` asks for a direct answer on most of them, but the GLM 5.3 family always thinks (and GLM 5.3 Fast rejects `none`), while GLM 5.2 and Nemotron Ultra are off until opted in. [reason]
- **DeepSeek V4 Pro needs two fields.** `thinking` accompanies `reasoning_effort`. [reason]
- **`max_tokens` includes reasoning.** The page says to set it above the reasoning budget so that room is left for the answer. [reason]
- **The Anthropic route is beta.** The docs recommend the OpenAI endpoint for production. [ma]
- **Async results are not stored.** Outputs reach the caller only through the webhook or a status call, so a webhook failure after retries loses them. [async]
- **Model APIs and dedicated deployments differ in control.** Model APIs serve a fixed catalogue; fine-tuned weights, region choice and isolation come with dedicated deployments. [home, region]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| home | https://docs.baseten.co/ | L | 2026-10-03 |
| index | https://docs.baseten.co/llms.txt | L | 2026-10-03 |
| ma | https://docs.baseten.co/inference/model-apis/overview.md | L | 2026-10-03 |
| price | https://docs.baseten.co/inference/model-apis/pricing-and-limits.md | L | 2026-10-03 |
| reason | https://docs.baseten.co/inference/model-apis/reasoning.md | L | 2026-10-03 |
| struct | https://docs.baseten.co/inference/structured-outputs.md | L | 2026-10-03 |
| fc | https://docs.baseten.co/inference/function-calling.md | L | 2026-10-03 |
| async | https://docs.baseten.co/inference/async.md | L | 2026-10-03 |
| sec | https://docs.baseten.co/observability/security.md | L | 2026-10-03 |
| region | https://docs.baseten.co/deployment/regional-deployments.md | L | 2026-10-03 |
