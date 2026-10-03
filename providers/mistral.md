---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: first-party lab API
sources:
  - https://docs.mistral.ai/getting-started/models/models_overview/
  - https://docs.mistral.ai/getting-started/clients/
  - https://docs.mistral.ai/inference/regional-inference
  - https://docs.mistral.ai/inference/priority-tier
  - https://docs.mistral.ai/admin/billing-usage/usage-limits
  - https://help.mistral.ai/en/articles/698531-why-am-i-hitting-api-rate-limits-and-how-do-i-increase-them
  - https://help.mistral.ai/en/articles/347617-do-you-use-my-user-data-to-train-your-artificial-intelligence-models
  - https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training
  - https://help.mistral.ai/en/articles/347628-how-long-do-you-store-my-data
  - https://help.mistral.ai/en/articles/347629-where-do-you-store-my-data-or-my-organization-s-data
  - https://docs.mistral.ai/admin/monitor-comply/zero-data-retention
  - https://mistral.ai/pricing
---

# Mistral API

first-party lab API

Mistral AI, a French company, trains its own models and sells them through its hosted API (its docs now say Mistral Studio; older URLs say La Plateforme) at `api.mistral.ai`, with a free plan, pay-as-you-go tiers and enterprise terms. Data is stored in the European Union by default, and regional endpoints exist for the EU and the US. The same weights, where open, are also published for self-hosting, and several of the models are resold on clouds. [models, where]

## Models offered

On 2026-10-03 the models overview lists Mistral Medium 3.5 (version 26.04, licence label "Modified MIT"), Mistral Small 4 (26.03, Apache 2.0), Mistral Large 3 (25.12, Apache 2.0), Ministral 3 in 14B, 8B and 3B sizes (Apache 2.0), a third-party open-weight Z.ai GLM 5.3 text model with a 1M window, OCR 4.1 and OCR 3, Voxtral text-to-speech and transcription models, Codestral and Codestral Embed, Mistral Embed, and two safety models (Shieldstral 1.0 and Mistral Moderation 2). The page gives no context sizes for most of them. [models]

| Model file | Overview entry |
| --- | --- |
| [Mistral Medium 3.5](../models/mistral/mistral-medium-3-5.md) | Medium 3.5, version 26.04, Modified MIT licence label |
| [Mistral Large 3](../models/mistral/mistral-large-3.md) | Large 3, version 25.12, Apache 2.0 |
| [Mistral Small 4](../models/mistral/mistral-small-2603.md) | Small 4, version 26.03, Apache 2.0 (the file uses the date-style id) |

Production ids follow `name-major-minor`; `-latest` and `-major` aliases follow the newest generally available model and can change behaviour and price without notice, and Mistral advises pinning a major-minor id (per the maker README). Models that are not in scope (Ministral, Codestral, OCR, Voxtral, embeddings) have no file. The lineage and lifecycle rules are in the [maker README](../models/mistral/README.md).

## API surface

- **Protocol.** Its own REST API whose chat endpoint `POST /v1/chat/completions` is shaped like OpenAI's. The maker README lists `/v1/conversations`, `/v1/agents`, `/v1/batch`, `/v1/moderations` and `/v1/ocr`, and further endpoints for FIM (fill-in-the-middle) completions, embeddings, moderations, classifications, OCR, audio speech and transcriptions appear in the zero-retention page's list. The pages read do not call the API OpenAI-compatible, so a client built for another vendor's chat shape should be tested rather than assumed. [zdr, models]
- **Auth.** An API key, which the SDK examples read from `MISTRAL_API_KEY`. [clients]
- **SDKs.** Official Python (`pip install mistralai`, client class `Mistral`) and TypeScript SDKs; the docs strongly recommend them over raw HTTP and mention third-party SDKs for other languages. The `server` parameter (`server="eu"`) selects a regional endpoint from SDK v2.70 on. [clients, regional]
- **Endpoints by region.** Default global host `api.mistral.ai`; regional hosts `api.eu.mistral.ai` and `api.us.mistral.ai`. [regional]
- **Reasoning control.** `reasoning_effort`; for Small 4 and Medium 3.5 the maker README lists `none` and `high` as the accepted values.

## Feature parity

First-party, so this is what the API itself offers; the parameter and tool list is in the maker README. [models]

- **Tools.** Function calling everywhere. The maker README lists web search, code interpreter, image generation, document library and custom connectors as built-in tools, with agents and conversations as stateful objects. On regional endpoints only function calling works among the tools, and Agents, Batch and the Files API are not available there. [regional]
- **Structured output.** `response_format` of `text`, `json_object` or `json_schema` (maker README).
- **Caching.** Cached input tokens cost up to 90 percent less. [pricing]
- **Batch.** A 50 percent discount; batch files are not covered by zero data retention. [pricing, zdr]
- **Priority.** Priority Tier routes requests through a priority queue at 1.75 times list price; it needs an entitlement and custom limits set with an account executive, and `service_tier: "auto"` falls back to standard when capacity runs out. [priority]
- **Long context, vision.** Per model card; Medium 3.5 and Large 3 are described as multimodal and Small 4 as a hybrid instruct, reasoning and coding model. [models]
- **Streaming.** Not covered by the pages read.
- **Moderation.** A separate moderation model and a `guardrails` block that can reject a request with HTTP 403 (maker README).

## Pricing

Per token, with input and output counted separately, plus separate units for OCR (per 1,000 pages), speech (per minute) and tool calls. Batch is 50 percent cheaper, cached input up to 90 percent cheaper, regional endpoints cost 1.1 times list on tokens and cache operations, and Priority Tier costs 1.75 times. A free plan includes a monthly API credit (the pricing page says $10) and limited Vibe access. A monthly spend cap can be set per organisation and per workspace, and reaching the organisation cap can suspend API access until the next month or until an admin raises it. Per-model list prices are on the model cards. [pricing, regional, priority, limits]

## Limits and data

- **Rate limits.** Three dimensions: requests per second, tokens per minute (input plus output) and tokens per month. Limits are per model. Tiers unlock on cumulative billed usage, not on prepaid credit: Free by default, Tier 1 on enabling pay-as-you-go, Tier 2 above 20 euros or dollars billed, Tier 3 above 100, Tier 4 above 500, and custom limits above 2,000 by contacting support. The help page says rate limits are set for the organisation and apply across all its workspaces, and that adding prepaid credit does not raise them. Audio has limits in audio seconds per minute and per month, and OCR in pages per minute. [tiers, limits]
- **Regions.** Data is stored in the EU by default; the EU and US regional endpoints process inference within that geography at a 10 percent premium, while control-plane data (account, keys, billing, analytics) stays outside the chosen region. Some features cause temporary transfers outside the EU (the help page points to the Trust Center for the subprocessor list), and Enterprise customers can ask for some of them to be switched off. [where, regional]
- **Retention and training.** On the free plans, inputs and outputs may be used to train models by default; paid accounts can opt out in the Admin panel under Privacy (the API and Vibe toggles are separate), and the help page does not state the paid default. Retention periods are set by the privacy policy and the help pages list account and technical data periods rather than a prompt-retention figure. Zero data retention is available on paid plans for stateless calls (chat completions, FIM, embeddings, moderations, classifications, OCR, speech and transcription), on request and at Mistral's discretion, and does not cover agents, conversations, libraries, the Files API or batch files, nor Labs models. Thumbs-up or thumbs-down feedback authorises use of the rated input and output on every plan. ZDR and the training opt-out are separate controls. [train, optout, retention, zdr]

## Notes for agents and harnesses

- **Free plan data use.** Content sent on a free key can be used for training by default; a paid account and the Admin-panel opt-out are the controls. [train]
- **Aliases move.** A `-latest` alias follows each new generally available model, so a harness that stores it can change behaviour and cost between runs; Mistral advises a major-minor id. (Maker README.)
- **Effort mapping.** The accepted `reasoning_effort` values depend on the model: two values on Small 4 and Medium 3.5, so a three-level scale from another vendor needs a map. (Maker README.)
- **Regional trade-off.** Choosing the EU or US endpoint removes Agents, Batch, Files and every built-in tool except function calling. [regional]
- **Spend cap.** A monthly cap can switch the API off until the next month, and the errors that follow are not transient. [limits]
- **Priority fallback.** With `service_tier: "auto"` the usage object reports which tier served the call. [priority]
- **Stateless ZDR.** Zero retention applies to stateless calls only, so an agent or conversation design that stores state on Mistral's side is outside it. [zdr]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| models | https://docs.mistral.ai/getting-started/models/models_overview/ | L | 2026-10-03 |
| clients | https://docs.mistral.ai/getting-started/clients/ | L | 2026-10-03 |
| regional | https://docs.mistral.ai/inference/regional-inference | L | 2026-10-03 |
| priority | https://docs.mistral.ai/inference/priority-tier | L | 2026-10-03 |
| limits | https://docs.mistral.ai/admin/billing-usage/usage-limits | L | 2026-10-03 |
| tiers | https://help.mistral.ai/en/articles/698531-why-am-i-hitting-api-rate-limits-and-how-do-i-increase-them | L | 2026-10-03 |
| train | https://help.mistral.ai/en/articles/347617-do-you-use-my-user-data-to-train-your-artificial-intelligence-models | L | 2026-10-03 |
| optout | https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training | L | 2026-10-03 |
| retention | https://help.mistral.ai/en/articles/347628-how-long-do-you-store-my-data | L | 2026-10-03 |
| where | https://help.mistral.ai/en/articles/347629-where-do-you-store-my-data-or-my-organization-s-data | L | 2026-10-03 |
| zdr | https://docs.mistral.ai/admin/monitor-comply/zero-data-retention | L | 2026-10-03 |
| pricing | https://mistral.ai/pricing | L | 2026-10-03 |
