---
last_checked: 2026-10-03
volatility: VOLATILE (model list, effort values, quotas and gateway naming changed through September 2026; Databricks pages carry dates from 2026-09-11 to 2026-10-02)
kind: cloud platform
sources:
  - https://docs.databricks.com/aws/en/machine-learning/model-serving/
  - https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/
  - https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/supported-models
  - https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/limits
  - https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/api-reference
  - https://docs.databricks.com/aws/machine-learning/foundation-model-apis/compliance
  - https://docs.databricks.com/aws/en/machine-learning/model-serving/query-chat-models
  - https://docs.databricks.com/aws/en/machine-learning/model-serving/query-reason-models
  - https://docs.databricks.com/aws/en/machine-learning/retired-models-policy
  - https://www.databricks.com/product/pricing/foundation-model-serving
---

# Databricks Mosaic AI Model Serving

cloud platform; the model-serving part of the Databricks data and AI platform, which runs on AWS, Azure and Google Cloud. It serves custom models and agents packaged with MLflow, hosts open and partner foundation models through "Foundation Model APIs" with a preconfigured endpoint per model, proxies external providers through "external models", and gives SQL access to all of these through `ai_query` and task-specific AI Functions. In September 2026 its pages describe the governed front door as Unity Gateway (the sidebar entry on one page says AI Gateway), where models appear as model services named like `system.ai.claude-sonnet-4-5` next to the older `databricks-` serving endpoints. Everything below was read on 2026-10-03 from Databricks documentation (class L) unless it says otherwise.

## Models offered

Databricks' supported-models page (updated 2026-10-02) lists these pay-per-token model endpoints; availability differs by cloud and Region.

- **Anthropic.** [Claude Fable 5.1](../models/anthropic/claude-fable-5-1.md) (text and image), [Fable 5](../models/anthropic/claude-fable-5.md) (text only), [Opus 5.5](../models/anthropic/claude-opus-5-5.md), [Opus 5](../models/anthropic/claude-opus-5.md), [Sonnet 5.5](../models/anthropic/claude-sonnet-5-5.md), [Sonnet 5](../models/anthropic/claude-sonnet-5.md), [Haiku 4.5](../models/anthropic/claude-haiku-4-5.md), with Opus 4.8 to 4.1 and Sonnet 4.6 to 4.
- **OpenAI.** [GPT-6.1 Sol](../models/openai/gpt-6.1-sol.md), [GPT-6 Sol](../models/openai/gpt-6-sol.md), [GPT-6 Luna](../models/openai/gpt-6-luna.md), [GPT-6 Astra](../models/openai/gpt-6-astra.md), GPT-5.6 Sol, [Terra](../models/openai/gpt-5.6-terra.md) and [Luna](../models/openai/gpt-5.6-luna.md), GPT-5.5 and 5.5 Pro, 5.4 (with mini and nano), 5.3 Codex, 5.2, 5.1, 5 (with mini and nano), and [gpt-oss-120b](../models/openai/gpt-oss-120b.md) and [gpt-oss-20b](../models/openai/gpt-oss-20b.md).
- **Google.** [Gemini 3.8 Flash](../models/google/gemini-3.8-flash.md), [3.7 Flash](../models/google/gemini-3.7-flash.md), [3.5 Flash-Lite](../models/google/gemini-3.5-flash-lite.md), [3.1 Flash-Lite](../models/google/gemini-3.1-flash-lite.md), [3.1 Pro Preview](../models/google/gemini-3.1-pro-preview.md), 3.6 Flash, 3.5 Flash, 3 Flash, two image models and Gemma 3 12B. Gemini 2.5 Pro and 2.5 Flash were due to retire on 2026-10-02. The Gemini endpoints are hosted on a global endpoint and need cross-geography routing enabled.
- **xAI.** [Grok 4.7](../models/xai/grok-4.7.md) (input types not stated) and [Grok 4.6](../models/xai/grok-4.6.md) (text input, 500,000-token window).
- **Zhipu / Z.ai.** [GLM 5.3](../models/zai/glm-5.3.md), [GLM 5.3 Flash](../models/zai/glm-5.3-flash.md) and [GLM 5.2](../models/zai/glm-5.2.md).
- **Moonshot AI.** [Kimi K3](../models/moonshot/kimi-k3.md) (2.8 trillion parameters, 1M context, image input).
- **DeepSeek.** [DeepSeek V4.1 Flash](../models/deepseek/deepseek-flash.md) (text and image), [DeepSeek V4 Pro (0813)](../models/deepseek/deepseek-v4-pro.md) (retiring on 2026-10-30) and DeepSeek V4 Flash (0731).
- **Others.** Alibaba Qwen3.5 122B A10B and Qwen3-Next 80B A3B Instruct (both preview) with a Qwen3 embedding model, an OpenJev judge model built on Qwen3.5 4B, Meta Llama 4 Maverick, Llama 3.3 70B and Llama 3.1 8B, GTE and BGE embedding models, and [Inkling](../models/other/inkling.md) (public preview; Databricks says its endpoint retires on 2026-10-30).
- **Provisioned throughput** serves any model of a supported architecture, including fine-tuned or custom-weight variants registered in Unity Catalog.
- **External models** are providers Databricks does not host (OpenAI, Anthropic and others), reached through the same governed endpoints.

## API surface

- **Protocol.** OpenAI-compatible REST for most models: Chat Completions, Embeddings and text completions through `POST /serving-endpoints/{name}/invocations`, a native Responses API passthrough for OpenAI models, and an Open Responses API that gives the Responses request format for Claude, Gemini and Databricks-hosted open models. Claude models also take the Anthropic Messages format (the reasoning table uses `thinking` and `output_config.effort` with it). The gateway path for the OpenAI client from outside a workspace is `https://<workspace>/ai-gateway/mlflow/v1`.
- **Clients.** The OpenAI SDK (and a `databricks_openai` helper), the MLflow Deployments SDK, the Databricks Python SDK, the Foundation Model APIs Python SDK, LangChain, SQL `ai_query`, the serving UI and AI Playground. GPT-6.1 Sol, GPT-6 Sol and GPT-6 Luna are not supported in AI Playground and are used through the Responses API.
- **Auth.** A Databricks personal access token, or OAuth machine-to-machine tokens for production. Unity Catalog permissions control who can query a model service or endpoint.
- **Names.** Endpoints are `databricks-claude-opus-5-5`, `databricks-gpt-6-sol`, `databricks-gemini-3-8-flash`, `databricks-kimi-k3`, `databricks-glm-5-3`, `databricks-grok-4-7`. Model services use `system.ai.<model>`. Provisioned-throughput and custom endpoints take a name the customer chooses.

## Feature parity

- **Reasoning and effort.** Databricks documents the accepted values per model, and they differ from each maker's own API. Claude Opus 5.5 and Fable 5.1 use adaptive thinking only, with `output_config.effort` of `low`, `medium`, `high`, `xhigh` or `max`; Databricks defaults Opus 5.5 to `medium`, Fable 5.1 has no Databricks default (Anthropic uses `high`), and disabled thinking and manual budgets are rejected. Older Claude models take `thinking` with `budget_tokens`. GPT-6.1 Sol takes `none`, `low`, `medium`, `high`, `xhigh` and `max` (no default stated); GPT-6 Sol and Luna take the same set with a Databricks default of `medium`; GPT-6 Astra takes `low` to `max` and rejects `none` and `minimal`; GPT-5.5 defaults to `medium`, GPT-5.1 and 5.2 to `none`, GPT-5 to `minimal`; gpt-oss takes `low`, `medium` (default) and `high`, with `minimal` mapped to `low`, `xhigh` and `max` mapped to `high`, and `none` treated as unset. Gemini 3.8 and 3.7 Flash take `low`, `medium` (default) and `high` and not `minimal`; other Gemini 3 models take `minimal`, `low` (default), `medium` and `high`. Grok 4.6 takes `low` to `xhigh`. Kimi K3, GLM-5.2 and the DeepSeek V4 builds default to `max`; Kimi K3 accepts `low`, `high` and `max`, GLM-5.2 accepts `high` and `max`, V4 Pro and V4 Flash 0731 accept `low`, `high` and `max`, and all four fall back to `max` for other values. V4.1 Flash accepts `low`, `high`, `xhigh` and `max`, maps `minimal` to `low` and `medium` to `high`, turns reasoning off at `none` or `disabled`, and rejects other values. GLM-5.3 accepts `low`, `high` and `max`, runs at `max` when the field is omitted or set to `minimal`, `medium` or `xhigh`, and rejects `none`; GLM-5.3-Flash takes the same three values (default `max`) and errors on `none`. Inkling accepts `minimal` to `max` (default `high`), maps `minimal` and `low` to one tier and `xhigh` and `max` to another, and treats `none` as its lowest effort.
- **Tools and structured output.** Function calling and structured outputs are documented for the OpenAI-compatible endpoints; individual models state their own support (for example GLM-5.3 lists parallel tool calls and structured output).
- **Prompt caching.** `cache_control` parameters cache text, reasoning, images and tool definitions on supported models. Claude endpoints return `cache_read_input_tokens` and `cache_creation_input_tokens` as top-level usage fields; usage also reports `reasoning_tokens`.
- **Batch.** AI Functions and `ai_query` run batch inference over tables, and a batch-inference price list exists for selected open models; Databricks also lists "AI Functions optimized" models for this.
- **Long context.** Databricks says context windows and maximum output for OpenAI, Gemini and Anthropic models match the maker's published values. Kimi K3, GLM-5.2 and Inkling list 1M tokens, GLM-5.3 and GLM-5.3-Flash 1,048,576 (GLM-5.3 up to 65,536 output), gpt-oss 128K. The Gemini 2.5 rate-limit rows carry a footnote limiting requests to under 200K input tokens or 400 KB.
- **Vision.** Per model: Fable 5.1, Opus 5.5, the GPT-6 models, Gemini, Kimi K3 and GLM-5.3-Flash accept images; Fable 5, Grok 4.6, GLM-5.3 and GLM-5.2 are listed as text input. Other rows were not checked.
- **Not at parity.** Data-residency handling uses Databricks Geos and cross-geography routing instead of the makers' regional endpoints; the Anthropic-specific server tools and Message Batches API were not described on the pages read.

## Pricing

- **Pay per token.** Billed in Databricks Units (DBUs) per million input, output and cache-read tokens, with the DBU price depending on cloud, plan and Region. Databricks says pay as you go with a 14-day free trial, and committed-use discounts on request. Rates are not repeated here.
- **Priority pay per token.** An opt-in per request with `service_tier` set to `priority`, admitted ahead of standard best-effort traffic, at a higher per-token rate; Databricks recommends it for latency-sensitive production work.
- **Provisioned throughput.** Hourly, per 50 model units, billed per minute: on demand (no commitment), or reserved for 1 or 3 months; in the price table the 3-month rate is below the 1-month rate, and some models offer only on-demand or only reserved capacity. Databricks recommends it for production, fine-tuned models and compliance needs beyond HIPAA.
- **Batch inference.** DBU per hour for selected open models.
- **Regional processing.** Models marked on the price page carry a 10 percent DBU uplift when regional processing (data residency) is on, for example Kimi K3.
- **Azure.** Azure Databricks is a first-party Azure service with Microsoft billing.

## Limits and data

- **Rate limits.** Pay-per-token endpoints have input tokens per minute, output tokens per minute and queries per hour limits, and the tightest applies. Eligible latest-generation partner models start at Tier 1 (1,000,000 input and 100,000 output tokens per minute) and can be raised to Tier 2 (5 million and 500,000) or Tier 3 (10 million and 1 million) through a quota request; older partner models stay at 200,000 and 20,000 (for example GPT-5.6, Opus 4.8 and Sonnet 4.6 in the table). Queries per hour is 360,000 for the GPT, Claude, Gemini and Grok rows and 7,200 for the GLM rows, DeepSeek V4.1 Flash and V4 Pro (0813), and Inkling; the Kimi K3 and DeepSeek V4 Flash (0731) rows give no figure. Enforcement uses a token bucket with a sliding window. `max_tokens` is reserved against the output limit before admission and the unused part is credited back; Claude Sonnet 4 defaults to 1,000 output tokens when `max_tokens` is unset. Databricks' example 429 body names the limit, the current usage and a suggested `retry_after` in seconds.
- **Regions.** Pay-per-token and provisioned-throughput regions are separate lists. Foundation Model APIs are a Databricks Designated Service, using Databricks Geos for data residency; Databricks says it may process data outside the originating region and cloud, and a workspace outside a US or EU Model Serving region needs cross-Geo processing enabled. Compliance support is listed for both modes: HIPAA in all regions, and PCI-DSS, FedRAMP, IRAP, CCCS and UK Cyber Essentials Plus in some regions; pay-per-token needs the Compliance Security Profile enabled.
- **Retention.** For Claude Fable 5.1 and Fable 5, prompts and responses are retained for 30 days for trust and safety, may be flagged for human review, are deleted after 30 days barring investigations or legal duties, and customers who opt out of data retention cannot use these models. The Model Serving overview adds that this applies to Fable 5 and future Mythos-class models for all customers, and that OpenAI may retain classifier-flagged content from GPT-5.5, GPT-5.5 Pro and later models for customers who build coding or model-routing services for third parties.
- **Training and abuse storage.** Databricks' Model Serving overview says that for paid accounts inputs and outputs are not used to train any model or improve Databricks services; that Foundation Model APIs may temporarily store inputs and outputs to detect abuse, isolated per customer, in the workspace's region for up to 30 days; that partner model providers may retain data for safety; and that all Model Serving data is encrypted at rest (AES-256) and in transit (TLS 1.2 or later). Container build logs are kept up to 30 days and metrics up to 14 days.
- **Lifecycle.** A deprecated model gets a retirement date 30 or 90 days out and stays available only to workspaces already using it.

## Notes for agents and harnesses

- The same setting has different accepted values by model, and several models substitute rather than reject: GLM-5.2, GLM-5.3, GLM-5.3-Flash, Kimi K3, DeepSeek V4 Pro (0813) and V4 Flash (0731) fall back to `max` for unlisted values, gpt-oss maps `xhigh` and `max` to `high`, while DeepSeek V4.1 Flash, GPT-6 Astra and Claude Opus 5.5 reject values they do not list. One effort name forwarded to every model therefore yields silent substitutions on some and a 400 on others.
- A large `max_tokens` is reserved at admission and can trip a 429 before any tokens are generated; setting none for Claude Sonnet 4 produces a 1,000-token cut-off.
- Model names exist in two shapes, `databricks-<model>` serving endpoints and `system.ai.<model>` model services, and the documentation says to swap one for the other.
- Gemini endpoints require cross-geography routing, which conflicts with strict data-residency settings.
- Endpoint retirements can come with 30 days' notice (Inkling's and DeepSeek V4 Pro (0813)'s are dated 2026-10-30), and only workspaces already using a deprecated model keep it.
- Responses-format clients reach Claude, Gemini and open models through the Open Responses API and not through the OpenAI passthrough, which is for OpenAI models.

## Sources

Read 2026-10-03 (class L, Databricks documentation; URLs in the frontmatter):

- Model Serving overview; Foundation Model APIs overview (updated 2026-10-02); supported models; limits and quotas; REST API reference; compliance
- Query a chat model (2026-09-11) and query reasoning models (2026-09-29); retired-models policy
- Foundation Model Serving price page <https://www.databricks.com/product/pricing/foundation-model-serving>; read as plain HTML, it lists DBU rates for Databricks-hosted models only; its structure, the regional uplift note and the trial terms are used, not the rates
- The training, abuse-storage and partner-retention statements come from the Model Serving overview <https://docs.databricks.com/aws/en/machine-learning/model-serving/> (updated 2026-09-11)
