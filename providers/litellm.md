---
last_checked: 2026-10-03
volatility: VOLATILE (the project ships several releases a week; what it forwards, drops or rewrites changes per release)
kind: router or gateway
sources:
  - https://docs.litellm.ai/docs/
  - https://docs.litellm.ai/docs/completion/drop_params
  - https://docs.litellm.ai/docs/proxy/forward_client_headers
  - https://docs.litellm.ai/docs/completion/prompt_caching
  - https://docs.litellm.ai/docs/providers/anthropic
  - https://docs.litellm.ai/docs/routing
  - https://docs.litellm.ai/docs/batches
  - https://docs.litellm.ai/docs/proxy/virtual_keys
  - https://docs.litellm.ai/docs/anthropic_unified
  - https://docs.litellm.ai/release_notes
  - https://api.github.com/repos/BerriAI/litellm/releases
  - https://github.com/BerriAI/litellm/issues/25957
  - https://github.com/BerriAI/litellm/issues/22963
  - https://github.com/BerriAI/litellm/releases/tag/v1.94.0
  - https://docs.litellm.ai/docs/providers/azure/azure_anthropic
  - https://docs.litellm.ai/docs/proxy/custom_pricing
---

# LiteLLM

router or gateway

LiteLLM is an open-source project (MIT licence, with some features behind an Enterprise licence) that offers one interface to more than a hundred model providers, in two forms: a Python SDK, and a self-hosted proxy server, which its documentation calls an AI gateway, that any OpenAI-compatible client can call. It is software you run, not a hosted service, so it has no catalogue, price list or data policy of its own: those belong to the providers behind it. What it adds is translation between request shapes, routing and fallback, spend tracking and key management. The hosted counterpart is [openrouter.md](openrouter.md). The older document about what the proxy forwards for Claude on Microsoft Foundry is folded in here and in [microsoft-foundry.md](microsoft-foundry.md). [docs]

## Models offered

Whatever the configured providers offer. The proxy is configured with a list of deployments, each a `model_name` the client sees plus the provider model and credentials behind it. The documentation's examples use ids such as `openai/gpt-5.6-terra` and `anthropic/claude-sonnet-5`. Provider routes named in the pages read include OpenAI, Anthropic, Google AI Studio, Vertex AI, Bedrock, Azure, DeepSeek, xAI, Mistral and vLLM; release notes add an OCI Generative AI provider (v1.87.0, 2026-05-23) and a rebuilt Together AI integration (v1.100.0, 2026-09-06). Model support lands in releases: Claude Opus 5 in v1.95.0 (2026-08-01) and 408 new catalogue entries in v1.103.0 (2026-09-27), so a model newer than the installed release may need a configuration entry or an upgrade. Every maker in [../models/](../models/README.md) is reachable if its provider is. [docs, notes]

## API surface

- **Protocols.** The proxy serves OpenAI-compatible endpoints (chat completions, embeddings, batches and files, and others) and a unified `/v1/messages` endpoint that follows Anthropic's Messages format and routes to any supported provider, including OpenAI, Bedrock, Vertex AI, Gemini and Azure. The Anthropic SDK can point at the proxy by changing its base URL (the page's example is `http://0.0.0.0:4000`). The `/v1/messages` page gives the valid `temperature` range as greater than 0 and less than 1. [docs, msgs]
- **Auth.** Clients present a virtual key. A master key (`LITELLM_MASTER_KEY`) administers the proxy, and virtual-key management needs a PostgreSQL database (`DATABASE_URL`). Provider credentials are held by the proxy; since v1.82 a `forward_llm_provider_auth_headers` setting lets a client bring its own provider key, and the proxy's own `Authorization` header is never forwarded. [vkeys, hdr]
- **SDKs.** The Python SDK (`litellm.completion()` and siblings) and, for the proxy, any OpenAI or Anthropic SDK. [docs]
- **Model ids.** `provider/model` in the SDK (`anthropic/claude-sonnet-5`); on the proxy the client uses the configured `model_name`, and one name can map to several deployments for load balancing. The Foundry route for Claude is the `azure_ai/` prefix. [docs, routing]

## Feature parity

LiteLLM's contract is the OpenAI chat-completions shape, translated per provider; features with no equivalent either pass as provider-specific parameters, ride the native `/v1/messages` route, or are dropped.

- **Unsupported parameters.** By default LiteLLM raises an exception when a model does not support a parameter. `drop_params=True` (globally, per request, or `drop_params: true` under `litellm_settings` in the proxy configuration) silently drops it instead; `additional_drop_params` names more, including nested paths such as `tools[*].input_examples`; `allowed_openai_params` does the reverse for a model that would otherwise reject a parameter. A request that works with `drop_params` on may therefore have lost a control. [drop]
- **Reasoning and effort.** For Anthropic models the page says `reasoning_effort` becomes a thinking setting: for older models (the page names Claude 3.5 and Opus 4.1) `low`, `medium` and `high` map to budgets of 1,024, 2,048 and 4,096 tokens; for Claude 4.6 and later, Opus 4.5 and later and Haiku 4.5 and later any value other than `none` turns on adaptive thinking plus `output_config.effort`, with the values `low`, `medium`, `high`, `xhigh` and `max`. On the `/v1/messages` route the page says a thinking `summary` value is preserved and forwarded even when the route goes to a non-Anthropic model. An issue opened 2026-04-17 reported that LiteLLM's own validation accepted `effort="max"` only for Opus 4.6 and refused it for Opus 4.7, which Anthropic's API accepts; it was closed as not planned on 2026-07-25. The current page lists `max` for the newer models, but whether a given release accepts it for a given model was not tested, so it is `UNVERIFIED`. [anth, msgs, issue]
- **Provider-specific parameters.** A parameter that is not an OpenAI parameter is passed to the provider in the request body. The Anthropic page gives `thinking`, `context_management` and `container` as native parameters forwarded this way. A Claude parameter such as `output_config` can therefore reach a provider that does not know it: an issue opened 2026-03-06 reported Claude Code's `output_config` rejected as an unknown parameter when sent through the proxy to a non-Anthropic model (v1.81.14). It was closed as completed on 2026-03-18, after the reporter confirmed that three merged pull requests removed the error. [drop, anth, i22963]
- **Claude on Microsoft Foundry.** The `azure_ai/` prefix (for example `azure_ai/claude-sonnet-5`) with the base `https://<resource>.services.ai.azure.com/anthropic`; both `/chat/completions` and `/anthropic/v1/messages` serve it, with an `api-key` header or an Azure AD bearer token. The documented parameters are `stream`, `stop`, `temperature`, `top_p`, `max_tokens`, `max_completion_tokens`, `tools`, `tool_choice`, `extra_headers`, `parallel_tool_calls`, `response_format`, `user`, `thinking` and `reasoning_effort`. The page is silent on `cache_control`, `output_config` and structured outputs for this route. The provider side is in [microsoft-foundry.md](microsoft-foundry.md). [foundry]
- **Tools.** Parallel tool calling, MCP tools and Anthropic's hosted tools (computer use, text editor, web search, memory) are listed for the Anthropic route. [anth]
- **Structured output.** For Claude Sonnet 4.5 and later, Opus 4.5 and later and Haiku 4.5, `response_format` is converted to Anthropic's native `output_format` and the `structured-outputs-2025-11-13` beta header is added; older models fall back to forced tool calling. [anth]
- **Prompt caching.** Documented for OpenAI, Anthropic, Google AI Studio, Vertex AI, Bedrock, DeepSeek and xAI, with provider minimums between 512 and 4,096 tokens; below the minimum, caching is skipped with no error. `cache_control` blocks are translated between Anthropic, Google and Bedrock's `cachePoint` form. `cache_control_injection_points` adds breakpoints automatically. Responses report `cached_tokens` and, for Anthropic, `cache_creation_input_tokens`. The v1.94.0 release notes (2026-07-28) add an `enable_anthropic_prompt_caching` flag for automatic `cache_control` injection; the caching page read here does not mention it. The Foundry route's page does not mention `cache_control`, so caching on that route is `UNVERIFIED`. [cache, v194, foundry]
- **Batch.** The proxy's `/v1/files` and `/v1/batches` cover OpenAI, Azure, Vertex, Bedrock, Mistral, vLLM and xAI. Anthropic is not in the list. Automated batch cost tracking is marked Enterprise-only. [batch]
- **Long context, vision, streaming.** Streaming works for every provider on `/v1/messages`. Pre-call checks can filter deployments by context window. Vision and context limits are the provider's. [msgs, routing]

## Pricing

The software is free (MIT licence). An Enterprise licence is required for some features; the pages read name key rotation and automated batch cost tracking, and v1.95.0's notes list SAML 2.0 SSO. No Enterprise price was read. All inference cost is the provider's, billed to your own account. The proxy's spend figures come from LiteLLM's bundled price map, which can lag or differ from a provider's bill: release notes record price-map updates after launch (for example a GPT-5.6 price cut in v1.96.0, 2026-08-09), and custom prices in the proxy configuration override the bundled map. [docs, vkeys, notes, pricing]

## Limits and data

- **Rate limits.** Whatever the providers allow, plus the proxy's own: per-key and per-team `rpm_limit`, `tpm_limit` and `max_budget` with `budget_duration` resets, and per-deployment `rpm`, `tpm` and `max_parallel_requests` (over-limit requests fail at once with 429). [vkeys, routing]
- **Reliability.** Strategies: simple shuffle (default, weighted), latency-based, usage-based (needs Redis), least-busy, cost-based and custom. `order` prioritises deployments (a lower value first), `num_retries` sets retries, and `allowed_fails` (failures a minute) with `cooldown_time` takes an unhealthy deployment out for a while. With `session_affinity` on in the pre-call checks, an `x-litellm-session-id` header pins a conversation to the deployment that served its first request. [routing]
- **Data and regions.** Prompts go to whichever provider serves the deployment, under that provider's retention and training terms; with a self-hosted proxy, spend logs are stored in the operator's own database. Pre-call checks can restrict routing to deployments in a named region (`region_name`). LiteLLM publishes no zero-retention option of its own, because it holds no data on a provider's side. The data policy of the project's own telemetry was not found in the pages read. [vkeys, routing]
- **Releases.** On 2026-10-03 the repository's newest stable tag was v1.103.2 (published 2026-10-01), with v1.104.0-rc.2 and v1.105.0-dev.2 (2026-10-02) also out; patch releases of older lines (v1.101.4, v1.102.2) appear the same days. The notes say the project is moving to Rust, and v1.95.0 lists a Rust `/v1/messages`. [releases, notes]

## Notes for agents and harnesses

- **Headers do not pass by default.** Client headers are not forwarded to the provider. `forward_client_headers_to_llm_api` (in `general_settings` for all models, or per model group under `litellm_settings: model_group_settings`) forwards headers beginning `x-` (but not `x-stainless-*`) and `anthropic-beta`; headers prefixed `x-pass-` are always forwarded with the prefix removed. Without either, a client's `anthropic-beta` header does not reach the provider. [hdr]
- **`max_tokens` is filled in.** The Anthropic page says LiteLLM sends 4,096 when the client gives none, so a request that relies on a provider default reaches the provider with a different cap. [anth]
- **Parameters can vanish without an error.** With `drop_params` on, a dropped `reasoning_effort`, `response_format` or `output_config` produces no error; the provider's usage fields are the evidence of what took effect. [drop]
- **The native route for Anthropic-only features.** Claude features with no chat-completions equivalent need `/v1/messages`; the chat route cannot carry a block type the OpenAI shape lacks (an inference from the two formats). [msgs, anth]
- **Guardrails differ for streaming.** For a streamed response a guardrail can only stop the output; edits to the text, such as masking, take effect only when the response is not streamed. [msgs]
- **Behaviour is per release.** Releases come several times a week, and support for a parameter or model can change between them; the release notes record such changes, and the bundled price map can differ from a provider's bill. [notes, releases]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| docs | https://docs.litellm.ai/docs/ | L | 2026-10-03 |
| drop | https://docs.litellm.ai/docs/completion/drop_params | L | 2026-10-03 |
| hdr | https://docs.litellm.ai/docs/proxy/forward_client_headers | L | 2026-10-03 |
| cache | https://docs.litellm.ai/docs/completion/prompt_caching | L | 2026-10-03 |
| anth | https://docs.litellm.ai/docs/providers/anthropic | L | 2026-10-03 |
| routing | https://docs.litellm.ai/docs/routing | L | 2026-10-03 |
| batch | https://docs.litellm.ai/docs/batches | L | 2026-10-03 |
| vkeys | https://docs.litellm.ai/docs/proxy/virtual_keys | L | 2026-10-03 |
| msgs | https://docs.litellm.ai/docs/anthropic_unified | L | 2026-10-03 |
| notes | https://docs.litellm.ai/release_notes | L | 2026-10-03 |
| releases | https://api.github.com/repos/BerriAI/litellm/releases | L | 2026-10-03 |
| issue | https://github.com/BerriAI/litellm/issues/25957 | A | 2026-10-03 |
| i22963 | https://github.com/BerriAI/litellm/issues/22963 | A | 2026-10-03 |
| v194 | https://github.com/BerriAI/litellm/releases/tag/v1.94.0 | L | 2026-10-03 |
| foundry | https://docs.litellm.ai/docs/providers/azure/azure_anthropic | L | 2026-10-03 |
| pricing | https://docs.litellm.ai/docs/proxy/custom_pricing | L | 2026-10-03 |
