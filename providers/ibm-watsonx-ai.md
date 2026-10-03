---
last_checked: 2026-10-03
volatility: VOLATILE (the model library, plans and regions change often; IBM's documentation pages did not load for automated readers, so several points rest on the product pages, the API reference and the Python SDK documentation)
kind: cloud platform
sources:
  - https://www.ibm.com/products/watsonx-ai
  - https://www.ibm.com/products/watsonx-ai/foundation-models
  - https://www.ibm.com/watsonx/pricing
  - https://cloud.ibm.com/apidocs/watsonx-ai
  - https://ibm.github.io/watsonx-ai-python-sdk/v1.7.1/index.html
  - https://ibm.github.io/watsonx-ai-python-sdk/v1.7.1/setup_cloud.html
  - https://ibm.github.io/watsonx-ai-python-sdk/v1.7.1/rate_limit.html
  - https://ibm.github.io/watsonx-ai-python-sdk/v1.7.1/model_gateway.html
  - https://ibm.github.io/watsonx-ai-python-sdk/v1.7.1/fm_deploy_on_demand.html
  - https://ibm.github.io/watsonx-ai-python-sdk/v1.7.1/fm_model_inference.html
---

# IBM watsonx.ai

cloud platform; IBM's studio and runtime for building and serving machine-learning and generative models, offered as a service on IBM Cloud and on AWS, and as software for on-premises or hybrid installation. For language models it combines IBM's own Granite family with open-weight models from Meta, Mistral, OpenAI, NVIDIA and others, served in two modes, shared pay-as-you-go endpoints and dedicated deploy-on-demand hardware. It does not list Anthropic, Google Gemini or OpenAI's closed GPT models in the library page read. Read on 2026-10-03 (class L: IBM's product pages, API reference and SDK documentation). IBM's main documentation site returned HTTP 403 or empty shells to automated readers, so the pages on security, plan limits and the supported-models detail were not read directly.

## Models offered

IBM's foundation-model library page lists each model with its availability, either pay as you go (shared, per token), deploy on demand (a dedicated deployment billed by the hour) or both (L).

- **IBM Granite.** The 4.1 generation (granite-4-1 in 3B, 8B and 30B, a 4B vision model and a 2B speech model) is listed as new and deploy on demand only; granite-4h-small is both; earlier Granite 4, 3.x, code, multilingual and Guardian safety models remain. Granite reasoning models from 3.2 onward take control messages that switch enhanced reasoning in chat (SDK documentation).
- **OpenAI.** [gpt-oss-120b](../models/openai/gpt-oss-120b.md) on both modes and [gpt-oss-20b](../models/openai/gpt-oss-20b.md) deploy on demand only.
- **Mistral.** [Mistral Large 3](../models/mistral/mistral-large-3.md) (listed as `mistral-large-2512`) on both modes and [Mistral Medium 3.5](../models/mistral/mistral-medium-3-5.md) (`mistral-medium-3-5-0`, new, deploy on demand), with Devstral, Ministral, Small and earlier Large and Medium builds.
- **NVIDIA.** [Nemotron 3 Ultra](../models/other/nemotron-3-ultra.md) as a quantized build listed under Red Hat (deploy on demand), plus Nemotron 3 Super, Nemotron Nano VL and Llama-3.1 Nemotron Ultra.
- **Meta.** Llama 4 Maverick (both modes) and Scout, Llama 3.3 70B (both modes), 3.2 vision, 3.1 and earlier, Llama Guard 3 vision.
- **Others.** DeepSeek R1 distill models, SDAIA ALLaM, EuroLLM, BigScience mT0, Poro; embedding models from IBM (Granite embedding, Slate) and Microsoft and Intel.
- **Via the Model Gateway (beta, IBM Cloud only).** A proxy in which a customer registers external providers such as OpenAI, Azure OpenAI and Anthropic and calls them through one SDK interface, with load balancing, token-bucket rate limits per tenant, provider or model, and access policies (SDK documentation). Those are the customer's provider accounts, not models IBM hosts.

## API surface

- **Protocol.** IBM's own REST API under `{region-url}/ml/v1/...`, with a required `version=YYYY-MM-DD` query parameter on each call. Routes include `text/chat` and `text/chat_stream`, an OpenAI-style `chat/completions`, `text/generation`, `text/embeddings`, `text/rerank`, `text/tokenization`, `text/detection` (hate, abuse and personal-data checks), batches with a files route, deployments, fine-tuning and time-series forecast (API reference). Calls name a project or deployment space.
- **Region URLs.** `us-south` (Dallas), `eu-de` (Frankfurt), `eu-gb` (London), `jp-tok` (Tokyo), `au-syd` (Sydney) and `ca-tor` (Toronto) at `https://{region}.ml.cloud.ibm.com`, and two AWS-hosted instances, Mumbai (`ap-south-1.aws.wxai.ibm.com`) and US East (`us-east-1.aws.wxai.ibm.com`) (SDK documentation).
- **Auth.** An IBM Cloud IAM API key or a bearer token; AWS-hosted instances take an API key generated in that environment.
- **SDKs.** The `ibm-watsonx-ai` Python library (with LangChain and LlamaIndex extensions, an async interface and a built-in retry mechanism) and the REST API. A separate API reference covers the software edition.
- **Model ids.** Library names in IBM's catalogue are lowercase with hyphens (`granite-4-1-30b`, `llama-3-3-70b-instruct`); the SDK's examples use maker-prefixed ids such as `ibm/granite-13b-chat-v2-curated`. The prefix for each current model was not checked.

## Feature parity

Few parity statements were retrievable, so this section is deliberately short.

- **Reasoning and effort.** Granite reasoning control messages are documented. No page read describes how effort levels for gpt-oss or other reasoning models are passed.
- **Tools.** `chat` accepts `tools`, `tool_choice` (a forced function) and `tool_choice_option` (`none`, `auto` or `required`) in the SDK, in an OpenAI-like shape.
- **Structured output.** Not found in the pages read. IBM's schema-related routes (`text/schemas/...`) are for document-schema extraction, not for constraining model output.
- **Prompt caching.** Not found in the pages read.
- **Batch.** A batches API with a files route exists in the API reference; supported models and discounts were not read.
- **Guardrails.** Generation calls accept guardrail options for hate, abuse and profanity, personal-data detection and Granite Guardian checks.
- **Long context, vision and streaming.** Vision models are in the library (Llama vision, Granite vision, Nemotron Nano VL); streaming exists for chat and generation. Context lengths per model were not read.
- **Other.** Fine-tuning routes (`fine_tunings`, `tuning`) are in the API reference. IBM's library page notes that the context length a provider supports can be larger than the length the platform allows, without listing the platform limits there.

## Pricing

- **Plans.** A free tier (the pricing page lists up to 300,000 foundation-model tokens a month, 20 compute-unit hours and 100 documents), an Essentials pay-as-you-go plan starting at no monthly fee, and a Standard plan with a monthly fee for enterprise production.
- **Shared models.** Priced per million tokens. IBM's library page says inference is billed in Resource Units of 1,000 tokens with input and output at the same rate, while its pricing page shows separate input and output rates for some models (for example granite-4h-small) and one rate for others; the two pages do not agree for every model. Embedding models carry one flat per-million-token rate.
- **Deploy on demand.** Billed per hour by GPU configuration while the deployment runs. IBM lists "Not available" for the shared per-token rate on deploy-on-demand-only models.
- **Compute-unit hours** (CUH) meter other machine-learning activity, not foundation-model inference.
- **Prices.** Indicative, vary by country and are on IBM's pricing page; they are not repeated here.

## Limits and data

- **Rate limits.** A per-instance limit on API calls per second, returning HTTP 429 with limit information in headers. The Python SDK retries up to 10 times by default: 429 waits for the next free slot, while 503, 504 and 520 back off exponentially from 0.5 seconds to at most 8 seconds. The numeric limits per plan were not read.
- **Regions.** Dallas, Frankfurt, London, Tokyo, Sydney, Toronto, Mumbai and US East (AWS), per the SDK. Which models run in which region is shown in the product catalogue, not read here.
- **Data handling (secondary).** A search-result excerpt of IBM's page on security and privacy for foundation models (dataplatform.cloud.ibm.com, `fm-security`) reports: IBM cannot access prompts or tuned models, does not monitor or log model input or output, does not use the customer's work to improve IBM models, does not store prompts or outputs unless the customer saves them, hosts the models in IBM Cloud and does not send prompts to third-party platforms. The page loads its text by script and could not be read directly, so this is unconfirmed. By design, calls routed through the Model Gateway go to the external provider the customer registered, so that provider's terms apply.
- **Deploy on demand** places the model on dedicated hardware for the exclusive use of the customer's organization (SDK documentation).
- **IP indemnity.** IBM's library page says it gives its standard contractual IP indemnification, uncapped, for IBM-developed models (the Granite and Slate families); the page does not extend this to third-party models.

## Notes for agents and harnesses

- The `version` date parameter is required on each call and pins the API behaviour to a date.
- Requests need a project or space id as well as credentials, which differs from key-only providers.
- Models that are deploy-on-demand only have no shared endpoint: using one means creating a deployment, which is billed by the hour while it exists, and calling it by deployment id (`/ml/v1/deployments/{id_or_name}/text/chat`). The SDK documentation says only online deployments are supported and that task credentials are needed on IBM Cloud to create one.
- The `chat/completions` route follows the OpenAI shape, but the SDK and the native `text/chat` route are the documented first-class paths; parameter coverage of the OpenAI-shaped route was not compared.
- A large shared catalogue entry does not imply a current model: many listed builds are older Llama, Mistral and Granite versions.

## Sources

Read 2026-10-03 (class L unless noted):

- watsonx.ai product page <https://www.ibm.com/products/watsonx-ai> and foundation-model library <https://www.ibm.com/products/watsonx-ai/foundation-models>
- Pricing page <https://www.ibm.com/watsonx/pricing>; the library page's footnotes for the Resource Unit and context-length statements
- API reference <https://cloud.ibm.com/apidocs/watsonx-ai> (route list and region URLs)
- Python SDK 1.7.1 documentation: setup for IBM Cloud, rate limits, Model Gateway, deploy on demand, `ModelInference` (frontmatter URLs)
- Not read: IBM's supported-models, plan and security pages (HTTP 403, or text loaded by script); the security excerpt came from a search-result summary (class A) of <https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-security.html?context=wx>
