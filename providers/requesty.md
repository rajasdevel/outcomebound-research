---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: router or gateway
sources:
  - https://docs.requesty.ai/
  - https://docs.requesty.ai/quickstart
  - https://docs.requesty.ai/features/reasoning
  - https://docs.requesty.ai/features/auto-caching
  - https://docs.requesty.ai/features/api-limits
  - https://docs.requesty.ai/features/fallback-policies
  - https://docs.requesty.ai/features/eu-routing
  - https://www.requesty.ai/pricing
  - https://www.requesty.ai/security
---

# Requesty

router or gateway

Requesty is a hosted gateway with a single endpoint in front of several hundred models from many providers. It adds routing policies (fallback, load balancing, latency-based), provider prompt-caching help, spend limits, analytics and an EU-hosted endpoint. Applications call it with an OpenAI-compatible or Anthropic-compatible client. Its documentation is shorter than [openrouter.md](openrouter.md)'s, and its data-privacy and routing-policy overview pages could not be read (see Sources). [docs, quick]

## Models offered

The documentation says 300 or more models; the pricing page says 600 or more from more than 20 providers, and the figures are not reconciled. Models come from providers such as OpenAI, Anthropic, Google (including through Vertex) and DeepSeek, per the examples in the reasoning and caching pages. The catalogue is live in the console; no list was read, so which model files in [../models/](../models/README.md) are available is `UNVERIFIED`. [docs, price, reason]

## API surface

- **Protocols.** OpenAI-compatible Chat Completions at `https://router.requesty.ai/v1`, a Responses endpoint (the caching page names `/v1/responses`), and Anthropic Messages at `https://router.requesty.ai/anthropic/v1/messages`. Every SDK that speaks OpenAI is said to work, and the quickstart names LangChain, the Vercel AI SDK, LlamaIndex, Haystack and Pydantic AI. [quick, cache]
- **Auth.** A bearer API key created in the dashboard (`REQUESTY_API_KEY` in the docs). Optional `HTTP-Referer` and `X-Title` headers feed analytics. Response headers (`x-requesty-provider`, `x-requesty-cache`, `x-requesty-latency-ms`, `x-requesty-request-id`) report the serving provider, cache status, latency and request id. [quick, docs]
- **Model ids.** `provider/model`, for example `openai/gpt-4o`; EU-hosted variants carry a region suffix (for example `@eu-central-1` on Bedrock or `@eu` on Vertex). A routing policy is addressed as `policy/<name>` (the docs' example is `policy/sonnet-with-fallback`), so routing changes in the dashboard without a code change. [docs, quick, fb, eu]
- **Usage.** Non-streaming responses carry usage and cost by default; streaming needs `stream_options: {"include_usage": true}` to get usage. [quick]

## Feature parity

- **Reasoning and effort.** A `reasoning_effort` field takes `low`, `medium`, `high`, `xhigh`, `max`, `min` or `none`. The page's mapping: for OpenAI models `max` becomes `high` (not `xhigh`), `none` and `min` become `low`, and `xhigh` passes through where the model supports it; for Anthropic, efforts become token budgets (1,024 for `min`, `none` and `low`, 8,192 for `medium`, 16,384 for `high`, and for `max` the model's maximum less one, for example 63,999 for Sonnet 3.7); for Vertex and Gemini, `min` or `none` gives 0 (Flash) or 128 (Pro) tokens, `low` 1,024, `medium` 8,192, `high` 24,576 and `max` the maximum output; Google AI Studio follows OpenAI's approach. The examples on that page are older models (`openai/o3-mini`, `anthropic/claude-sonnet-4-0`, `vertex/google/gemini-2.5-pro`), so whether current Claude models, which use adaptive thinking on Anthropic's API, receive an effort field or a budget is `UNVERIFIED`. OpenAI does not return reasoning text; Anthropic and DeepSeek return it as `reasoning_content`. [reason]
- **Prompt caching.** `"requesty": {"auto_cache": true}` in the body, on Chat Completions and Responses. Providers that cache implicitly (OpenAI, DeepSeek, Google Gemini) need nothing; for Anthropic, Requesty adds breakpoints to the largest content blocks of the request. Minimum prefix lengths of the provider apply (the page's examples are 1,024 tokens for Anthropic and 2,048 for Claude 3.5 Haiku). The page says savings of up to 90 percent; the overview says up to 80 percent; both are vendor claims. The console shows cache hit rates. [cache, docs]
- **Tools, structured output, vision, batch.** Not described on the pages read; the docs imply standard OpenAI parity, which is not a statement of support. `UNVERIFIED`. [quick]
- **Routing.** Fallback policies try the next model in a chain on a timeout, rate limit or error, with 0 to 10 retries per model and exponential backoff (500 ms, 1 s, 2 s, 4 s, with jitter); non-retryable errors such as an invalid request fail over at once, and the page says failed attempts are not billed. Load-balancing policies split traffic by custom weights, and latency-based routing is a third policy type. [fb, quick, rate]
- **Guardrails and access.** Guardrails and role-based access are listed, with SSO, full role-based access and audit logs on the Enterprise plan. [docs, price]

## Pricing

The sources disagree. The overview page says there is no token markup and users pay provider rates, with bring-your-own-key keeping any provider discounts. The pricing page says pay-as-you-go carries a 5 percent markup (a $10 per million tokens model costs $10.50), a free plan offers 200 daily requests on free models, and Enterprise is custom, with BYOK on pay-as-you-go and Enterprise, EU data residency on every plan, and no per-seat price or minimum. The pricing page is the more specific of the two; which one reflects current billing is not settled by the pages read. Monthly spend caps can be set per API key and per service account. [docs, price, rate]

## Limits and data

- **Rate limits.** Requesty does not limit requests per minute; it limits how many requests are in flight at once. Upstream 429 errors are handled by a routing policy that retries elsewhere. No numbers are given. [rate]
- **Retention.** By default prompts and outputs are logged and kept for up to 30 days, encrypted, in the EU; this can be turned off per API key, after which only metadata (time, user, model, tokens, cost) is kept. An organisation-wide zero-retention mode, available on written request, stores no content and turns off Requesty's own caching, leaving audit metadata. Encryption is TLS 1.2 or higher in transit and AES-256 at rest. The security page states no policy on training use by Requesty and does not address what model providers keep. [sec]
- **Regions.** An EU endpoint, `https://router.eu.requesty.ai/v1`, hosted in Frankfurt (AWS eu-central-1), keeps routing, logging, caching and analytics in the EU. The EU-routing page says inference stays in the EU only if an EU-region model is also chosen (Bedrock, Vertex and Azure models with region suffixes, or Mistral). [sec, eu]
- **Compliance.** The security page says a SOC 2 Type II programme is in progress, with status at trust.requesty.ai, and that a GDPR Article 28 data processing agreement is signed on request. [sec]

## Notes for agents and harnesses

- **Policy ids hide the model.** A request sent to `policy/<name>` can be answered by any model in the policy; the `x-requesty-provider` header and the response body record which one served it. [fb, docs]
- **The same effort word is not the same amount of thinking.** `max` becomes `high` for OpenAI, and Anthropic and Gemini efforts become fixed budgets, so one effort value gives different reasoning across routes; the reasoning-token count in usage is the evidence of what ran. [reason]
- **Claude caching needs the flag.** Claude prompts are cached through Requesty only when `auto_cache` is set or breakpoints are added by hand. [cache]
- **Streaming usage is off by default.** It needs `stream_options.include_usage`. [quick]
- **Concurrency, not rate.** A client that fans out many parallel calls meets the in-flight limit rather than a per-minute one; with a fallback policy, upstream 429s are retried elsewhere and do not reach the client. [rate, fb]
- **Markup is stated two ways.** The documentation overview and the pricing page differ on whether a markup applies, so the bill is the only settled evidence. [docs, price]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| docs | https://docs.requesty.ai/ | L | 2026-10-03 |
| quick | https://docs.requesty.ai/quickstart | L | 2026-10-03 |
| reason | https://docs.requesty.ai/features/reasoning | L | 2026-10-03 |
| cache | https://docs.requesty.ai/features/auto-caching | L | 2026-10-03 |
| rate | https://docs.requesty.ai/features/api-limits | L | 2026-10-03 |
| fb | https://docs.requesty.ai/features/fallback-policies | L | 2026-10-03 |
| eu | https://docs.requesty.ai/features/eu-routing | L | 2026-10-03 |
| price | https://www.requesty.ai/pricing | L | 2026-10-03 |
| sec | https://www.requesty.ai/security | L | 2026-10-03 |
