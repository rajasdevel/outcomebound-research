---
last_checked: 2026-10-03
volatility: VOLATILE (plans, prices, limits and feature support change often)
kind: router or gateway
sources:
  - https://portkey.ai/docs/introduction/what-is-portkey
  - https://portkey.ai/pricing
  - https://portkey.ai/docs/product/ai-gateway
  - https://portkey.ai/docs/api-reference/inference-api/introduction
  - https://portkey.ai/docs/product/ai-gateway/universal-api
  - https://portkey.ai/docs/product/ai-gateway/cache-simple-and-semantic
  - https://portkey.ai/docs/product/enterprise-offering/security-portkey
  - https://github.com/Portkey-AI/gateway
---

# Portkey

router or gateway

Portkey is an AI gateway sold as a hosted control plane with an open-source (MIT) gateway behind it. Applications send requests to one endpoint; Portkey translates between request formats, routes and retries across providers, applies guardrails and caching, and records logs and metrics. It can run as the managed service, in a hybrid arrangement, or fully self-hosted. It is a control layer rather than a model catalogue: the customer brings provider accounts, and the pages read describe no resale of tokens. [intro, repo, price]

## Models offered

Whatever the connected providers offer. Portkey describes support for "over 250 AI models" in its overview and "1,600+ LLMs" across language, vision, audio and image in the open-source repository's description; the two numbers come from different pages and are not reconciled. Providers named include OpenAI, Anthropic, Google Gemini and Azure; the docs also describe routing to privately hosted or local models through a custom host URL. Because routing is by provider slug, a maker in [../models/](../models/README.md) is reachable when its provider is one Portkey supports and the customer holds the account. [intro, repo, gw]

## API surface

- **Protocols.** The gateway accepts three request formats whatever the target provider and translates between them: OpenAI Chat Completions (`POST /v1/chat/completions`), OpenAI Responses (`/v1/responses`) and Anthropic Messages (`/v1/messages`), plus embeddings and other provider APIs such as reranking and video through the same endpoint. Hosted base URL: `https://api.portkey.ai/v1`. Locally, `npx @portkey-ai/gateway` serves `http://localhost:8787/v1` with a console at `/public/`. [uni, api, repo]
- **Auth.** The `x-portkey-api-key` header identifies the Portkey account; the provider is chosen by an `x-portkey-provider` header, a virtual key or the model string. Provider credentials are held by Portkey and referenced through virtual keys or provider slugs. [api, uni]
- **SDKs.** Portkey SDKs for Python and JavaScript, the OpenAI SDK with the base URL changed and Portkey headers added, or plain REST. [api]
- **Model ids.** `@provider-slug/model-name`, where the slug names a provider configured in the workspace (the docs' examples are `@openai-provider/gpt-4o`, `@anthropic-provider/claude-sonnet-4-5-20250514` and `@google-provider/gemini-2.0-flash`); changing the string switches provider with the rest of the call unchanged. [uni]
- **Configs.** Gateway behaviour (fallbacks, load balancing, retries, timeouts, conditional routing, canary tests, caching and usage limits) is defined in configuration files. [gw]

## Feature parity

The pages read describe breadth but give few per-feature details, so most items below are statements of what Portkey says it supports, not of how a parameter is mapped.

- **Reasoning and effort.** The universal-API page mentions thinking and extended-reasoning modes without listing parameters or a mapping table. How an effort level in one format becomes another maker's control is `UNVERIFIED`. [uni]
- **Tools and structured output.** The universal-API page lists function calling across providers; it does not address structured output, so structured-output translation is `UNVERIFIED`. [uni]
- **Prompt caching.** Pass-through of a provider's prompt-caching controls is not described on the pages read (`UNVERIFIED`). Portkey's own gateway cache has a simple mode (exact match on the request body, metadata headers and namespace) and a semantic mode (cosine similarity; the page says the system prompt is ignored, so changing it does not affect hits), with a TTL that defaults to 7 days (60 seconds to 90 days). The caching page says simple cache is on all plans, while the pricing page lists caching from the Production plan up; semantic cache needs a vector database (Milvus or Pinecone when self-hosted) and is limited to select Enterprise plans. This is a cache of whole responses, unlike a provider's prompt cache. [cache, price]
- **Batch.** Not described in the pages read; `UNVERIFIED`.
- **Vision, audio, long context, streaming.** Vision, audio (speech-to-text and text-to-speech) and streaming are listed as supported; context limits are the provider's. A gRPC transport option is offered for lower latency. [gw, uni]
- **Resilience.** Fallbacks across providers, retries, timeouts, load balancing over multiple keys, a per-strategy circuit breaker, conditional routing and canary tests. [gw]
- **Guardrails.** PII and other guardrails are part of the product (advanced guardrails on Enterprise per the pricing page). [intro, price]

## Pricing

Portkey prices its platform, not tokens: the pages read state no per-token charge or markup, and provider costs go to the customer's own provider accounts. The pricing page lists a free Developer plan (10,000 recorded logs a month, past which requests still run but are not logged; logs kept 3 days and metrics 30), a Production plan at $49 a month (100,000 recorded logs; $9 for each further 100,000 requests; logs kept 30 days and metrics 90; simple caching, guardrails, role-based access and service-account keys), and a custom Enterprise plan (more than 10 million logs a month, custom retention, semantic caching, SSO, private cloud or VPC hosting). The open-source gateway is free to self-host with a basic dashboard, routing and fallbacks. The overview page also describes a free plan with 10,000 monthly requests; the two pages differ on the unit (logs or requests). [price, intro]

## Limits and data

- **Rate limits.** Usage limits by spend or tokens and request or token limits per minute, hour or day are listed as features (granular budget and rate limits are an Enterprise item on the pricing page); Portkey states no platform rate limit in the pages read. Provider limits apply behind it. [gw, price]
- **Retention.** Log and metric retention depends on the plan (see Pricing). The security page describes minimal retention and anonymisation, and the overview says a feature can be turned on so that request and response bodies are not stored in Portkey's datastores or logs. The pages read give no statement on training use, and point to the privacy policy, a data processing agreement and a data protection officer; training use is `UNVERIFIED` here. [intro, sec]
- **Security.** The overview states ISO 27001 and SOC 2 certification and GDPR and HIPAA compliance; the security page gives TLS 1.2 or higher in transit and AES-256 at rest. [intro, sec]
- **Latency and scale.** The overview claims 20 to 40 ms of added latency from edge workers around the world, over 25 million requests a day and 99.99 percent uptime; the security page gives 99.995 percent uptime and 310 data centres. These are vendor figures and the two uptime numbers are not reconciled. [intro, sec]
- **Regions.** No region list or region choice was found in the pages read. Self-hosting or private-cloud hosting is the documented route for data-location control. [intro, price]

## Notes for agents and harnesses

- **Format and slug are separate choices.** A Claude-native client can call the Messages route and still reach a non-Anthropic model, with Portkey translating; how effort and thinking fields are translated is not documented in the pages read. [uni]
- **The gateway cache is not a prompt cache.** A simple-cache hit returns a stored response for an identical request and hides any variation between runs, and a semantic-cache hit can return the answer to a different question (the system prompt is ignored when matching). Both change what an evaluation or an agent loop sees. [cache]
- **Slugs are local to a workspace.** `@provider-slug` names an integration in one Portkey workspace, so the same string has no meaning in another workspace. [uni]
- **Hosted and self-hosted differ in features.** The open-source gateway runs locally with one command and carries routing, fallbacks and guardrails; the hosted plans add logs, caching and access control. The pages read do not state the hosted service's terms on training use, which are in Portkey's privacy policy and data processing agreement. [repo, price, sec]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| intro | https://portkey.ai/docs/introduction/what-is-portkey | L | 2026-10-03 |
| price | https://portkey.ai/pricing | L | 2026-10-03 |
| gw | https://portkey.ai/docs/product/ai-gateway | L | 2026-10-03 |
| api | https://portkey.ai/docs/api-reference/inference-api/introduction | L | 2026-10-03 |
| uni | https://portkey.ai/docs/product/ai-gateway/universal-api | L | 2026-10-03 |
| cache | https://portkey.ai/docs/product/ai-gateway/cache-simple-and-semantic | L | 2026-10-03 |
| sec | https://portkey.ai/docs/product/enterprise-offering/security-portkey | L | 2026-10-03 |
| repo | https://github.com/Portkey-AI/gateway | L | 2026-10-03 |
