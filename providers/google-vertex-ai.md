---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often; the product was renamed in 2026 and the documentation paths are still moving)
kind: cloud platform
sources:
  - https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps (read 2026-10-09)
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/use-claude
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/quotas
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/batch
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/structured-outputs
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/prompt-caching
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/grok
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/use-open-models
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/call-open-model-apis
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/capabilities/structured-output
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/capabilities/thinking
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/deepseek
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-gemma
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-pro
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/openai
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/api-keys
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/express-mode/overview
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/migrate-google-ai
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/consumption-options
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/standard-paygo
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/priority-paygo
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/flex-paygo
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/abuse-monitoring
  - https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing
  - https://cloud.google.com/vertex-ai
  - https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai
  - https://platform.claude.com/docs/en/build-with-claude/overview
  - https://platform.claude.com/docs/en/build-with-claude/prompt-caching
---

# Gemini Enterprise Agent Platform (formerly Vertex AI)

cloud platform; Google Cloud's model and agent service. Google's product page, read on 2026-10-03, has the title "Gemini Enterprise Agent Platform (formerly Vertex AI)" (class L). Google's documentation, console and SDK settings use the new name. Trade-press coverage dates the announcement to 2026-04-22 (class A; the press pages were not opened). This file keeps the file name `google-vertex-ai.md` and says "Vertex AI" for the earlier name. Older URLs, the `aiplatform.googleapis.com` host and the `vertex-` prefixes in some ids and headers keep the earlier name. The service hosts Google's own Gemini, Gemma and media models, partner models served as managed APIs (Anthropic, xAI, Mistral, Meta, AI21 Labs), and open models served as managed APIs or deployed from Model Garden. Everything below was read on 2026-10-03.

## Models offered

Google's partner page and open-model page list these (L). Availability varies by Region and endpoint type; each model page states it.

- **Google Gemini.** [Gemini 3.8 Flash](../models/google/gemini-3.8-flash.md) (generally available 2026-09-02, 1,048,576-token context, 65,536 output), [3.7 Flash](../models/google/gemini-3.7-flash.md), [3.5 Flash-Lite](../models/google/gemini-3.5-flash-lite.md), [3.1 Flash-Lite](../models/google/gemini-3.1-flash-lite.md) and [3.1 Pro (preview)](../models/google/gemini-3.1-pro-preview.md), with 3.6 Flash, 3.5 Flash, 3 Flash (preview), 2.5 Pro, Flash and Flash-Lite, image, live-audio, text-to-speech, video, music and embedding models. The Gemini 4 Argon preview in this library is not on Google's model list as read.
- **Anthropic.** [Claude Fable 5.1](../models/anthropic/claude-fable-5-1.md), [Fable 5](../models/anthropic/claude-fable-5.md), [Opus 5.5](../models/anthropic/claude-opus-5-5.md), [Opus 5](../models/anthropic/claude-opus-5.md), [Sonnet 5.5](../models/anthropic/claude-sonnet-5-5.md), [Sonnet 5](../models/anthropic/claude-sonnet-5.md) and [Haiku 4.5](../models/anthropic/claude-haiku-4-5.md), plus Opus 4.8 to 4 and earlier Sonnet models. Anthropic's model-id table also lists the Mythos models, marked limited availability; Google's own Claude list does not show them.
- **xAI.** [Grok 4.7](../models/xai/grok-4.7.md) (preview) and [Grok 4.6](../models/xai/grok-4.6.md), with Grok 4.3, 4.20 (reasoning and non-reasoning) and the 4.1 Fast models, which Google marks deprecated.
- **Meta.** [Muse Spark 1.3](../models/meta/muse-spark-1.3.md) (preview) as a partner model; Llama 4 Maverick, Llama 4 Scout and Llama 3.3 as managed open models.
- **Mistral and AI21 Labs (partner models).** Mistral Medium 3, Mistral Small 3.1, Codestral 2 and Mistral OCR; AI21 Jamba 1.5 Large and Mini (preview).
- **Open models as managed APIs (MaaS).** [gpt-oss-120b](../models/openai/gpt-oss-120b.md) and [gpt-oss-20b](../models/openai/gpt-oss-20b.md), [GLM 5.2](../models/zai/glm-5.2.md) (with GLM 5 and 4.7), [Gemma 4 26B A4B](../models/google/gemma-4-26b-a4b-it.md), DeepSeek V3.2, V3.1, R1-0528 and OCR, Kimi K2 Thinking, MiniMax M2, Qwen3 235B, Qwen3 Coder and Qwen3-Next 80B (instruct and thinking), and E5 embedding models. Google's Gemma page lists Gemma 4 [31B](../models/google/gemma-4-31b-it.md), 26B A4B, E4B and E2B in Model Garden for self-deployment; only 26B A4B is a managed API in the pages read, and no Gemma 4 12B appears on the page.
- **Not found on Google's lists:** DeepSeek V4, Kimi K3, MiniMax M3, GLM 5.3, Qwen3.8 and Nemotron 3 Ultra.

## API surface

- **Hosts.** `aiplatform.googleapis.com` is the global endpoint; `{location}-aiplatform.googleapis.com` is regional; `aiplatform.us.rep.googleapis.com` and `aiplatform.eu.rep.googleapis.com` are the US and EU multi-region endpoints (L).
- **Gemini models.** The native call is `generateContent` or `streamGenerateContent` on `.../projects/{project}/locations/{location}/publishers/google/models/{model}` with a model id such as `gemini-3.8-flash`. The `google-genai` SDK reaches it with the Vertex flag (the environment variable is `GOOGLE_GENAI_USE_ENTERPRISE`). An Interactions API (preview) exists. Google's comparison page lists the differences from the Gemini API at `generativelanguage.googleapis.com`: Google Cloud accounts and service accounts instead of Google accounts and keys, regional endpoints, enterprise terms and support, and access to Provisioned Throughput.
- **OpenAI compatibility for Gemini.** Chat Completions at `.../locations/{location}/endpoints/openapi` with the model written `google/gemini-3.5-flash`. Only Google Cloud authentication works with the OpenAI library there, not an API key. The page maps `reasoning_effort` `low`, `medium` and `high` to thinking budgets of 1K, 8K and 24K tokens (stated in the context of the 2.5 models) and offers `extra_body.google.thinking_config` for direct control.
- **Claude.** Anthropic's Messages shape with two changes: the model goes in the URL, not the body, and `anthropic_version` is set to `vertex-2023-10-16` in the body. The call is `rawPredict` or `streamRawPredict` on `.../publishers/anthropic/models/{model}`. Anthropic's SDKs support it (`AnthropicVertex`). Ids are `claude-opus-5-5`, `claude-sonnet-5-5`, `claude-fable-5-1`; older ones carry a date suffix, for example `claude-haiku-4-5@20251001`.
- **Other partner and open models.** Open models use an OpenAI Chat Completions endpoint at `.../locations/{location}/endpoints/openapi/chat/completions`, with ids shaped like `deepseek-ai/deepseek-v3.1-maas`. xAI models use names such as `grok-4.6` and are called through the same OpenAI-shaped surface (Chat Completions and a Responses API under `endpoints/openapi`). The Mistral and Llama partner pages carry their own request instructions, which were not read.
- **Auth.** Application default credentials, OAuth tokens and service accounts, with IAM roles (`roles/aiplatform.user` and others). A Google Cloud API key works for Gemini and is recommended by Google for testing only; the express-mode key has no project or location in the URL. Express mode is a preview sign-up for developers with a gmail.com Google Account that gives a 90-day free tier within quotas before billing is added.
- **Enabling partner models.** Each partner model is switched on from its Model Garden card, with Marketplace terms for Claude. Anthropic bars certain resellers; a billing account managed by one cannot accept the terms.

## Feature parity

For Gemini the comparison is with the Gemini API; for partner models, with the maker's own API.

- **Gemini reasoning controls.** Gemini 3.8 Flash accepts `thinking_level` of LOW, MEDIUM (default) or HIGH; MINIMAL returns a validation error for that model. Thought signatures and a thinking prompting guide are documented.
- **Gemini features.** Structured output, function calling, Google Search and Google Maps grounding, code execution, URL context, count tokens, RAG Engine, computer use (preview), implicit and explicit context caching, Provisioned Throughput and batch are listed for 3.8 Flash. Live API, tuning and fixed quota are not. Image, audio and video input are supported; output is text.
- **Context caching (Gemini).** Implicit caching is on for every project and gives a 90 percent discount on cached tokens. Explicit caching also gives 90 percent for Gemini 2.5 and later, with a default 60-minute lifetime and a storage charge. Minimum cacheable size is 4,096 tokens for the Gemini 3 family, with 6,144 on implicit caching for 3 Flash Preview, 3.1 Pro Preview, 3.7 Flash and 3.8 Flash, and 2,048 for Gemini 2. Cache-hit tokens are reported in `cachedContentTokenCount`.
- **Batch (Gemini).** At a 50 percent discount with a 24-hour target, up to 200,000 requests per job from Cloud Storage or BigQuery, with a 1 GB file limit for Cloud Storage input. Jobs can queue up to 72 hours; unfinished work after 24 hours of running is cancelled and only completed requests are billed. Batch excludes Provisioned Throughput, explicit caching and RAG, is outside the service-level objective, and is not available for tuned Gemini 3 models. The 90 percent cache discount does not stack with the batch discount.
- **Claude features.** Anthropic's overview lists thinking, adaptive thinking, effort, citations, PDF support, structured outputs, tool search, memory, bash and text editor tools, fine-grained tool streaming and prompt caching (5 minute and 1 hour) as available on Google Cloud. Web search and the browser-use tool are available there and not on Bedrock. Not available: code execution, web fetch, the advisor tool, Agent Skills, the MCP connector, programmatic tool calling, Files API and URL sources, Anthropic's Message Batches API, the Models, Admin and Usage APIs, Managed Agents and server-side fallback. Compaction and context editing are beta. Requests are capped at 30 MB.
- **Claude structured outputs.** Supported for Claude 4.5 and later, but switched off by default by an organization-policy constraint (`constraints/vertexai.allowedPartnerModelFeatures`) that must list `structured_outputs`.
- **Claude batch.** Google's own batch page lists Claude models for batch prediction from BigQuery or Cloud Storage in Anthropic's request schema, with four concurrent jobs per project by default and no global endpoint. Anthropic's list says its Message Batches API is unavailable on Google Cloud; the two statements describe different features.
- **Claude prompt caching.** Google says caches are scoped to the project; Anthropic's caching page says Google Cloud isolates caches per organization rather than per workspace. The 1-hour TTL is not offered for Claude 3.7 Sonnet, 3.5 Sonnet (both versions) and 3 Opus. Writes cost 25 percent more (5 minutes) or 100 percent more (1 hour) than base input; reads cost 90 percent less. Google treats the request hashes as service data rather than customer data, and a project can have explicit caching switched off through support, after which requests that enable it are rejected.
- **Claude context.** 1M-token windows for Fable 5.1 and 5, Opus 5.5 to 4.6, Sonnet 5.5, 5 and 4.6; 200K for the other Claude models, Sonnet 4.5 among them (Anthropic's page). The Google page caps images at 5 MB each and 100 per request.
- **Open and xAI models.** Function calling, thinking and structured output pages exist for managed open models; Google says all managed open models support structured output. DeepSeek R1 0528 returns reasoning inside `<think>` tags in the content field and has no separate reasoning field. Grok models are listed with reasoning, function calling, structured output and Responses pages.

## Pricing

- **Consumption options** (Google's list of five): Provisioned Throughput (fixed term of 1 week, 1 month, 3 months or 1 year), Standard PayGo (per token, the default), Priority PayGo (per token at a premium, for steadier performance), Flex PayGo (per token at a discount, preview) and batch inference (discounted). Prices sit on Google's pricing page, which separates global from non-global endpoints and standard from priority and flex or batch rates; they are not repeated here.
- **Flex.** A 50 percent discount on Standard PayGo, for Gemini models on the global endpoint only, with a request timeout up to 30 minutes and a 20 MB inline payload limit. Priority works on global, US and EU endpoints for most Gemini models.
- **Claude and other partners.** Pay as you go or Provisioned Throughput. Claude's global endpoint carries no premium and regional or multi-region endpoints cost 10 percent more (Anthropic's page, L).
- **Introductory pricing.** Google's pricing page gives Gemini 3.8, 3.7 and 3.6 Flash an introductory per-token price through 2026-12-31; from 2027-01-01 a standard price twice as high applies (the figures are on the model cards and the pricing page).
- **Spend-based tiers.** Standard PayGo throughput tiers depend on the organization's eligible spend over 30 days (see Limits and data).

## Limits and data

- **Standard PayGo throughput.** Tiers rise with 30-day spend across eligible services: Gemini Pro models run from 500,000 to 10 million tokens per minute and Flash and Flash-Lite from 2 million to 50 million, per model, with bursting above that on a best-effort basis; there is no separate per-minute request limit. A 429 means contention on a shared pool rather than a fixed quota; Google advises exponential backoff, the global endpoint and smoothed traffic. Usage tiers do not apply to preview models.
- **Claude quotas.** Models launched after 2026-05-26 share one quota bucket per lineage (opus, sonnet, haiku, fable) per location, with the global endpoint and each multi-region endpoint as separate buckets. Earlier models have per-model queries-per-minute and tokens-per-minute quotas. Grok quota is a single global bucket per base model.
- **Regions.** Gemini 3.8 Flash is on the global endpoint and the US and EU multi-regions; the page lists no single-region endpoints for it. In Google's Claude quota table, single-region endpoints (for example `us-east5`, `europe-west1`, `asia-southeast1`) appear for Opus 4.6, Sonnet 4.6 and older models; Opus 4.7 and later appear only on the global and multi-region endpoints. Anthropic's page says provisioned throughput needs a regional endpoint. Data-residency commitments need a regional or multi-region endpoint; the global endpoint does not give them.
- **Training use.** Google says it does not use customer data to train or fine-tune models without the customer's permission or instruction, for all managed models including pre-release ones.
- **Prompt logging for abuse monitoring.** For customers under the Google Cloud Platform Terms, prompts flagged by classifiers may be logged for up to 90 days in the project's region, outside customer-managed keys; customers on a Cloud Master Agreement are exempt by default, and others can request an exception. For models designated Advanced AI (all Claude Mythos and Fable models, and Opus 4.7 or later and Sonnet 5 or later when enrolled in Anthropic's cyber verification program), all prompts and responses are logged for up to 30 days, and zero retention may not be possible. Consent to Google's Advanced AI Safety Addendum is needed once per project before such a model can be enabled, and for Claude Fable 5 and Mythos 5 Google says the customer must also enable sharing of this data with Anthropic for abuse monitoring.
- **Other retention.** In-memory caching of Gemini inputs and outputs has a 24-hour lifetime, is isolated to the project, and can be switched off per project through a `cacheConfig` call. Grounding with Google Search keeps logs for up to 3 days with no off switch; grounding with Google Maps keeps prompts and outputs for 30 days. Request-response logging to BigQuery is off by default (Google's Claude page and Anthropic both recommend at least 30 days of logging for Claude). The Interactions API stores state unless `store` is false (the default is true), and the Deep Research agent keeps session data for 7 days with no off switch. Live API session resumption, off by default, caches for 24 hours.
- **Compliance.** Google states that Claude on this platform meets FedRAMP High requirements.

### Spend caps [as-of 2026-10-09]

Cloud Billing documents a monthly cap for one project and one eligible service: Gemini API,
Gemini Enterprise Agent Platform, Cloud Run or Cloud Run functions. Resellers, subscriptions and
budgets across services or projects are excluded. Cost estimates generally use list prices before
savings and credits. Enforcement is not instant and overages are billed. It blocks new usage;
in-flight requests finish and can incur charges. Fixed costs for persistent resources continue.
Data and resources are not deleted. L,
[documentation](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps), updated
2026-10-07, read 2026-10-09.

Caps reset and blocked services resume at the next monthly period. A manual lift stops further
enforcement for that period unless the amount is increased; services can take up to one hour to
return. Moving the project to another billing account deletes the old caps and lifts an enforced
cap, allowing new charges; the new account needs new caps. L, same source and read date.
Thus a configured cap is not an exact ceiling on the total bill (inference).
The spending-control distinction is in [releasing.md](../practices/releasing.md#10-evidence-after-deployment-and-paid-service-bounds-volatile-as-of-2026-10-09).

## Notes for agents and harnesses

- Model ids are shaped differently by route: Gemini ids are bare names in the URL, Claude ids are bare names in the URL with a date suffix on older models and no model field in the body, and open models use `publisher/name-maas` in the body.
- A Claude request that carries `output_config` is rejected until the organization-policy constraint allows structured outputs; the cause is policy rather than the model.
- `thinking_level` MINIMAL is rejected by Gemini 3.8 Flash. Earlier Flash models list different level sets on their own pages.
- Priority and Flex are chosen with a request header (`X-Vertex-AI-LLM-Shared-Request-Type` with `priority` or `flex`), and a second header, `X-Vertex-AI-LLM-Request-Type: shared`, makes the request skip Provisioned Throughput and use only the PayGo option (without it, available Provisioned Throughput is used first); the response reports the traffic type in `usageMetadata.trafficType`.
- Google manages quota in the console, and a 429 on Standard PayGo does not mean a fixed quota was hit.
- Anthropic's lifecycle dates on Google Cloud are set by Google and can differ from Anthropic's API schedule.

## Sources

Read 2026-10-03 (class L unless stated):

- Partner models for MaaS <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models>; Claude overview, request, quota, batch, structured-output and prompt-caching pages (URLs in the frontmatter)
- xAI Grok page; open models for MaaS, call-APIs, structured-output, thinking and DeepSeek pages; Gemma page (frontmatter)
- Google models list, Gemini 3.8 Flash and 3.1 Pro pages, OpenAI compatibility, API keys, express mode, Gemini API comparison page (frontmatter)
- Consumption options, Standard PayGo, Priority PayGo, Flex PayGo, Provisioned Throughput, batch inference, context caching (frontmatter)
- Zero data retention <https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention>; abuse monitoring <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/abuse-monitoring>
- Pricing <https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing> (read as plain HTML; its structure and the introductory-price dates are used, not per-model rates)
- Anthropic: Claude on Google Cloud <https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai>, features overview <https://platform.claude.com/docs/en/build-with-claude/overview> and prompt caching <https://platform.claude.com/docs/en/build-with-claude/prompt-caching>
- Product page <https://cloud.google.com/vertex-ai>, read 2026-10-03: its title gives the new name and "formerly Vertex AI" (class L)
- Rename announcement date (2026-04-22): trade-press coverage seen only as search-result summaries (class A); not opened
