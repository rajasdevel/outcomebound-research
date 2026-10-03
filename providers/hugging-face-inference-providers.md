---
last_checked: 2026-10-03
volatility: VOLATILE (the partner list, credits and per-provider support change often)
kind: router or gateway
sources:
  - https://huggingface.co/docs/inference-providers/index
  - https://huggingface.co/docs/inference-providers/pricing
  - https://huggingface.co/docs/inference-providers/tasks/chat-completion
  - https://huggingface.co/docs/inference-providers/security
---

# Hugging Face Inference Providers

router or gateway

Inference Providers is a feature of the Hugging Face Hub that routes a request for a Hub model to one of several partner inference companies behind a single Hugging Face token and a single bill. It is a router rather than a host: the models run at the partners (Baseten, Cerebras, DeepInfra, Fireworks, Groq, Together and others) or at Hugging Face's own `hf-inference` service, which was called the serverless Inference API before this feature existed and now concentrates on CPU models such as embedding, ranking and classification. The kind is listed as a router or gateway, although the partner list itself contains the hosts described in the neighbouring files. [index, price]

## Models offered

Models on the Hub that at least one partner serves, found with `hf models ls --warm` or the models page filtered by inference provider, and listed with per-provider price, context length, latency and throughput by `GET https://router.huggingface.co/v1/models`. The index page's partner table on 2026-10-03 listed chat-completion (language) support for Baseten, Cerebras, Cohere, DeepInfra, Featherless AI, Fireworks, Groq, HF Inference, Novita, Nscale, OVHcloud AI Endpoints, Public AI, Scaleway, Together and Z.ai, with vision-language chat for most of them, and image, video and speech partners (Fal AI, Replicate, WaveSpeedAI) besides. [SambaNova](sambanova.md) and Nebius ([Token Factory](nebius-token-factory.md)), both described in this folder, are not in that table. Examples on the pages are openai/gpt-oss-120b ([model file](../models/openai/gpt-oss-120b.md)), `zai-org/GLM-5.3` ([model file](../models/zai/glm-5.3.md)) and GLM-5.3-Flash, `deepseek-ai/DeepSeek-V4.1-Flash`, `Qwen/Qwen3.8-27B` ([model file](../models/alibaba/qwen3.8-27b.md)) and `XiaomiMiMo/MiMo-V2.6-Pro-RL` (served by Novita); which in-scope model files are served on a given day changes. The pricing page gives the catalogue as more than 200 models. Every model shown is a Hub model; no closed-lab model (Claude, GPT, Gemini) appears. [index, chat, price]

## API surface

- **Protocols.** An OpenAI-compatible chat completions endpoint at `https://router.huggingface.co/v1` (chat only; the docs say other tasks such as image generation, embeddings and speech need the Hugging Face clients), and the `huggingface_hub` (Python) and `@huggingface/inference` (JavaScript) `InferenceClient` classes, which format the request for the chosen provider. The proxy passes each partner's own request format, so the exact HTTP request can differ between providers when called without the clients. No Anthropic-compatible endpoint is documented on the pages read, though the index lists setup guides for coding agents (OpenCode, Pi, Codex, Claude Code and Hermes Agent). [index]
- **Auth.** A Hugging Face fine-grained access token with the permission to call Inference Providers, as a bearer token (`HF_TOKEN`). [index]
- **SDKs.** The two Hugging Face clients, or the OpenAI SDK with the base URL changed. [index]
- **Model ids.** The Hub id, `org/model`, with an optional suffix: `:fastest` (the default; highest throughput in tokens per second), `:cheapest` (lowest price per output token), `:preferred` (the provider order set in the account settings), or a provider name such as `openai/gpt-oss-120b:groq`. In the clients, `provider="auto"` is the default and a named provider forces one. [index]

## Feature parity

Parity depends on the partner behind the request, which the router chooses unless told, so every feature below is "as the selected partner supports it". The router's chat schema lists these request fields: `messages` (text and image parts), `tools` (functions only), `tool_choice` (`auto`, `none`, `required` or a named function), `response_format` (`text`, `json_object` or `json_schema` with `strict`), `reasoning_effort`, `stream` with `stream_options.include_usage`, `logprobs`, `seed`, `stop`, the usual sampling fields, and a `tool_prompt` (text placed before the tool list). The page says the API supports grammars, constraints and tools. [chat]

- **Reasoning and effort.** `reasoning_effort` with common values `none`, `minimal`, `low`, `medium`, `high` and `xhigh`; the schema says support and defaults depend on provider and model. How it maps to each partner's own control is not described, so see the partner files ([together-ai.md](together-ai.md), [fireworks-ai.md](fireworks-ai.md), [groq.md](groq.md), [cerebras.md](cerebras.md), [deepinfra.md](deepinfra.md), [baseten.md](baseten.md)). [chat]
- **Tools and structured output.** Present in the schema; whether a given partner enforces strict schemas or honours `tool_choice: required` varies, as the partner files show (for example Groq's strict mode excludes streaming and tools). [chat]
- **Prompt caching and batch.** Not part of the router's documented interface; whatever caching a partner does applies behind the router. `UNVERIFIED` for pass-through of cache controls.
- **Failover.** With automatic selection, a request is rerouted when the primary provider is flagged unavailable by Hugging Face's validation system. [index]
- **Vision, streaming, long context.** Vision-language chat is supported through image parts for models and partners that offer it; streaming is supported; context is per partner and model. [index, chat]

## Pricing

Hugging Face states it passes provider rates through with no markup. Every account receives monthly credits that apply to routed requests: $0.10 for free users (marked as subject to change), $2.00 for PRO and $2.00 per seat for Team and Enterprise (shared among members, and usable on other Hugging Face compute such as Inference Endpoints, Spaces hardware and Jobs for the paid plans), after which usage is pay-as-you-go from purchased credits. Two billing modes exist: routed by Hugging Face (billed to your account, credits apply, no partner account needed) or a custom provider key set in the account settings (the partner bills the customer directly and credits do not apply). Team and Enterprise organisations can bill an organisation (or, for Enterprise, a resource group) with the `X-HF-Bill-To` header or the `bill_to` client option, and their administrators can set spending limits and disable particular providers. `hf-inference` is billed by compute time multiplied by the hardware's price per second. [price]

## Limits and data

- **Rate limits.** The pages read give no rate-limit numbers for Inference Providers. A search result of an older Inference API page gives 1,000 requests a day for signed-up users and 20,000 for PRO and Enterprise, which predates this feature's credit model and is not relied on. Limits at the partner also apply. `UNVERIFIED`.
- **Retention and training.** Hugging Face says it does not store the request body or response when routing, keeps logs for up to 30 days for debugging with no user data or tokens in them, and does not store user data for training. It directs you to each provider's data policies, which differ. [security]
- **Security.** The Hub is SOC 2 Type 2 certified; external providers are responsible for their own security; routing uses TLS. [security]
- **Regions.** Not stated on the pages read; a partner's region follows that partner's service. [security]

## Notes for agents and harnesses

- **The default route is the fastest provider, not a fixed one.** The same model id can be served by different partners over time, with different quantisation, context length and feature support; a provider suffix (`:groq`) or a named `provider` fixes the route. [index]
- **Model discovery.** `GET /v1/models` on the router shows per-provider price, context, latency and throughput; `hf models ls --warm --json` lists served models for scripts. [index]
- **The OpenAI endpoint is chat only.** Embeddings, images and speech go through the Hugging Face clients. [index]
- **Strictness is a partner property.** Whether `strict: true` or `tool_choice: required` is enforced depends on the partner that serves the request. [chat]
- **Billing mode changes the contract party.** With a custom key the partner bills directly; with routed billing Hugging Face bills, and the partner still processes the request under its own policy. [price, security]
- **Free credits are small.** A free account's monthly credit is $0.10, so sustained use needs purchased credits. [price]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| index | https://huggingface.co/docs/inference-providers/index | L | 2026-10-03 |
| price | https://huggingface.co/docs/inference-providers/pricing | L | 2026-10-03 |
| chat | https://huggingface.co/docs/inference-providers/tasks/chat-completion | L | 2026-10-03 |
| security | https://huggingface.co/docs/inference-providers/security | L | 2026-10-03 |
