---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, regions and API surface changed several times a month in 2026; Oracle's price list could not be read)
kind: cloud platform
sources:
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/overview.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/pretrained-models.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/model-endpoint-regions.htm
  - https://docs.oracle.com/en-us/iaas/releasenotes/services/generative-ai/
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/openai-compatible-api.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/oci-openai.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/chat-models.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/openai-gpt-oss-120b.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/x-ai-grok-4-7.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/xai-grok-4-6.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/xai-grok-4-3.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/cohere-command-a-reasoning-08-2025.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/meta-llama-4-maverick.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/google-gemini-2-5-pro.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/imported-models.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/data-handling.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/pay-on-demand.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/about-retirement.htm
  - https://docs.oracle.com/en-us/iaas/Content/generative-ai/limits.htm
  - https://www.oracle.com/artificial-intelligence/generative-ai/generative-ai-service/faq
---

# Oracle OCI Generative AI

cloud platform; Oracle Cloud Infrastructure's managed service for chat, embedding and rerank models, agents and model hosting, which Oracle's documentation now organises as Enterprise AI Models, Agents and Governance. It hosts some models itself (Cohere, Meta, OpenAI's open-weight gpt-oss), proxies others that run on the makers' own infrastructure (xAI's Grok, Google's Gemini), and hosts open-weight models that customers import onto dedicated GPU clusters. It has no Anthropic Claude models and no OpenAI GPT-5 or GPT-6 models in the pages read. Everything below was read on 2026-10-03 from Oracle documentation (class L), most of it as plain HTML.

## Models offered

- **Hosted chat models.** Cohere Command A (03-2025 build), Command A Reasoning (111B parameters, 256,000-token window, up to 32,000 output, capped at 4,000 per response on demand) and Command A Vision; Meta Llama 4 Maverick (512,000-token window, 4,000-token response cap on demand), Llama 4 Scout and Llama 3.3 70B; OpenAI [gpt-oss-120b](../models/openai/gpt-oss-120b.md) and [gpt-oss-20b](../models/openai/gpt-oss-20b.md); xAI [Grok 4.7](../models/xai/grok-4.7.md) (added 2026-09-25, 500K tokens), [Grok 4.6](../models/xai/grok-4.6.md) (added 2026-09-10, 500K), Grok 4.3 (1M tokens), Grok 4.20 and a multi-agent variant; Google Gemini 2.5 Pro, Flash and Flash-Lite (the 2.5 generation only). Cohere Embed 4 and Rerank 4 are the active embedding and rerank models; earlier Embed 3 and Rerank 3.5 models are marked deprecated. An xAI text-to-speech voice model is also listed.
- **Hosting differs by maker.** Oracle's regional table says Gemini calls go to Google locations in the matching geography and Grok calls go to xAI's infrastructure, both on demand only with no dedicated-cluster option; in Ashburn and Frankfurt Gemini is also reachable through Oracle Interconnect for Google Cloud. Grok is available in the three US commercial Regions only. Cohere has the widest Regional spread; Llama 4 is on demand only in Chicago and dedicated-cluster only elsewhere; gpt-oss and Llama 3.3 offer both modes in some Regions.
- **Imported open-weight models.** Customers can import supported architectures from Hugging Face or Object Storage and host them on dedicated AI clusters, with no 744 unit-hour minimum. Oracle's release notes list imports added in 2026 for Qwen3.8-27B, Qwen3.8 2.4T-A95B, Gemma 4 31B IT and 26B A4B IT, DeepSeek V4 Pro 0813, V4 Flash 0731 and V4.1 Flash, Kimi K3, GLM-5.3 and GLM-5.3-Flash, MiniMax M3, Xiaomi MiMo V2.5 Pro, NVIDIA Nemotron 3 Ultra and Nemotron 3.5 Lightning, and AI Singapore SEA-LION models. Library files exist for [Qwen3.8-27B](../models/alibaba/qwen3.8-27b.md), [Qwen3.8 2.4T-A95B](../models/alibaba/qwen3.8-2.4t-a95b.md), [MiniMax M3](../models/minimax/MiniMax-M3.md), [Nemotron 3 Ultra](../models/other/nemotron-3-ultra.md), [Gemma 4 31B](../models/google/gemma-4-31b-it.md), [Gemma 4 26B A4B](../models/google/gemma-4-26b-a4b-it.md), [DeepSeek V4 Pro](../models/deepseek/deepseek-v4-pro.md), [DeepSeek V4.1 Flash](../models/deepseek/deepseek-flash.md), [Kimi K3](../models/moonshot/kimi-k3.md), [GLM-5.3](../models/zai/glm-5.3.md) and [GLM-5.3-Flash](../models/zai/glm-5.3-flash.md). An imported model is the customer's responsibility to license; it does not mean Oracle serves it on demand. Compatible families named on the import page: SEA-LION, Qwen, DeepSeek, Gemma, OmniVoice, Llama, Phi, MiniMax, Mistral, Kimi, Nemotron, Whisper, gpt-oss, MiMo and GLM.
- **Retirements.** Cohere's `command-latest` and `command-plus-latest` aliases were retired on 2026-07-30. Oracle says a deprecated model stays usable for a defined time before retirement and that this time is longer in dedicated mode than on demand; the dates per model are on a separate page not read.

## API surface

- **OpenAI-compatible endpoint.** `https://inference.generativeai.{region}.oci.oraclecloud.com/openai/v1`, with the Responses API as the primary route (background mode since 2026-07-29), plus Conversations, Chat Completions, Files, Vector Stores and Containers APIs. Oracle's page does not list embeddings on this endpoint. Imported models can be called through the Responses API since 2026-09-06. The package `oci-genai-auth` (Python and Java) supplies OCI authentication for the OpenAI SDK.
- **Native Inference API.** A separate OCI-native endpoint for chat, embedding and rerank, reached through the Console, CLI and SDKs, with an `ApplyGuardrails` operation, a Management API for clusters and endpoints, and an NL2SQL API (L). Cohere Command A Reasoning works only with version 2 of the native chat API for Cohere (`CohereChatRequestV2`). Other request-format details of the native chat API were not read.
- **Auth.** OCI Generative AI API keys for testing and early development, or OCI IAM for production; both use OCI credentials. IAM policies can restrict access to a model through a `target.model.id` condition (added 2026-09-03).
- **Model ids.** `cohere.command-a-03-2025`, `cohere.command-a-reasoning`, `cohere.command-a-vision`, `meta.llama-4-maverick-17b-128e-instruct-fp8`, `meta.llama-3.3-70b-instruct`, `google.gemini-2.5-pro`, `xai.grok-4.7`, `openai.gpt-oss-120b`.
- **Agents and tools.** Enterprise agent features include Projects, hosted applications, MCP tools, a code interpreter, file search, function calling and vector stores. A smart model router and model discovery by Region arrived on 2026-09-23; the release note says the router sends on-demand requests across Regions within a regional scope the user selects. Its configuration was not read.

## Feature parity

Oracle describes features per model rather than in a parity table, so the cells below are what each model page states.

- **Reasoning and effort.** Grok 4.7 takes effort `low`, `medium`, `high` (default) or `xhigh` and cannot turn reasoning off; Grok 4.3 and Gemini 2.5 Pro are reasoning models, and Gemini 2.5 Pro's thinking cannot be turned off. Cohere Command A Reasoning accepts reasoning budgets. gpt-oss-120b reasons, is text only, has a 128,000-token window for prompt plus output, caps output at 16,000 tokens in the playground, and takes temperature 0 to 2 and top-p 0 to 1. The pages read do not name the request field that carries the effort level.
- **Tools.** Function calling, code interpreter, file search and MCP calling are listed for the OCI Responses API; function calling is listed on the Grok 4.7, Gemini 2.5 Pro and gpt-oss-120b pages. Cohere Command A Reasoning is described as built for tool use and multi-step reasoning.
- **Structured output.** Listed on the Grok 4.7, Grok 4.3 and Gemini 2.5 Pro pages.
- **Prompt caching.** Cached input tokens are reported (`cachedTokens`) and priced separately for Grok 4.7, 4.6 and 4.3; Gemini 2.5 Pro may cache input but the API does not control it.
- **Batch.** Not offered as an API in the pages read; the Gemini 2.5 Pro page marks batch prediction as unsupported.
- **Long context.** Grok 4.3 at 1M tokens, Grok 4.6 and 4.7 at 500K, Gemini 2.5 Pro at 1,048,576 input and 65,536 output, Llama 4 Maverick at 512K, Command A Reasoning at 256K, gpt-oss at 128K. On-demand Command A Reasoning and Llama 4 Maverick cap each response at 4,000 tokens.
- **Vision.** Gemini 2.5 models, Grok 4.3, Command A Vision, Command A Reasoning and Llama 4 take images; gpt-oss takes no images.
- **Streaming.** Referenced as a parameter for chat models.
- **Guardrails.** A guardrails feature with pinned versions (added 2026-05-26) and image moderation through `ApplyGuardrails` (2026-05-29); the checks themselves were not read.

## Pricing

- **On demand.** Oracle's billing page describes two units: character-based transactions (prompt plus response characters for chat, input characters for embeddings, one character per transaction, priced per 10,000) and, for other models, tokens priced per million. The gpt-oss and Grok pages price input and output tokens separately; Grok 4.6 has separate standard and priority rates, and from 200,000 prompt tokens its long-context rate applies to the whole request. Each model page names its price-list entry.
- **Dedicated AI clusters.** Billed per unit-hour, with a minimum commitment of 744 unit-hours (31 days) per cluster for hosting pretrained models. Imported models have no such minimum. Fine-tuning clusters are billed the same way. Hardware unit shapes differ per model and Region (for example A100, H100, H200 and B200 shapes for gpt-oss-120b).
- **Exact prices.** Oracle points to its price list and a cost estimator; the price list loads its figures by script and was not read.

## Limits and data

- **Rate limits.** On-demand mode uses dynamic throttling that Oracle adjusts per tenancy from model demand, capacity and the tenancy's past throughput; Oracle says the limits are undocumented and change, and advises exponential backoff. Model pages name a tokens-per-minute limit that can be raised by request (for example for Gemini 2.5 Pro and the Grok models). Service limits: dedicated AI clusters default to 0 per tenancy and need a limit increase; 50 model endpoints per cluster by default; up to 50 projects per tenancy; hosted applications, artifacts and replicas have separate adjustable limits.
- **Regions.** Oracle's model-by-Region page lists US East (Ashburn), US Midwest (Chicago), US West (Phoenix), US Gov West (Phoenix, added 2026-08-11), US DoD West, Brazil East (São Paulo), Germany Central (Frankfurt), EU Sovereign Central (Frankfurt), UK South (London), UK Gov South (London), Saudi Arabia Central (Riyadh), UAE Central (Abu Dhabi), UAE East (Dubai), India South (Hyderabad) and Japan Central (Osaka). Models vary by Region and government Regions have fewer.
- **Retention.** Oracle states that the service does not retain customer inference inputs and outputs, retains fine-tuning data only for the length of the job, and does not use training data to improve general services. It states that prompts, responses, training data and custom models are not shared with third-party model providers it names (Cohere, Meta, xAI, Google Vertex AI). Data in motion is encrypted with TLS 1.2; fine-tuning data is encrypted at rest with Oracle-managed AES-256 and optionally with customer-managed keys in OCI Vault.
- **Zero-retention endpoints.** Oracle's FAQ page says its managed access to other makers' models uses zero-data-retention endpoints. It does not say which models; a claim that Grok runs on xAI's zero-retention endpoints was seen only in a search-result summary and is unconfirmed.
- **Training use.** Covered above: no use of customer data for general improvement is stated for inference or fine-tuning data.

## Notes for agents and harnesses

- Oracle's model names carry the maker prefix and, for some models, a build suffix (`cohere.command-a-03-2025`); the `*-latest` Cohere aliases were removed on a stated date, after which requests naming them no longer resolve.
- The OpenAI-compatible Responses endpoint is the one documented for tools, memory and background work; embeddings are not listed on that endpoint, and Oracle points to the separate native Inference API for chat, embedding and rerank.
- On-demand throttling is not published, so headroom cannot be computed ahead of time; Oracle warns that rapid retries without backoff can lead to further rejections and temporary blocking.
- On-demand responses from Command A Reasoning and Llama 4 Maverick stop at 4,000 tokens however large `max_tokens` is; the playground default for maximum output on Grok 4.3 is 600 tokens.
- Gemini 2.5 and Grok models are processed outside OCI-hosted GPUs; a data-handling review may need Oracle's statements and the maker's terms side by side.
- An imported open-weight model runs on a dedicated cluster under vLLM or SGLang chosen by Oracle's Open Model Engine; throughput and cost depend on the cluster shape rather than on token pricing.
- OCI quota and endpoint details for the newest models change often; the release-notes page dates each addition.

## Sources

Read 2026-10-03 (class L), as plain HTML:

- Generative AI home and overview <https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm>, <https://docs.oracle.com/en-us/iaas/Content/generative-ai/overview.htm>
- Pretrained models, models by Region, release notes (frontmatter URLs)
- OpenAI-compatible endpoints and OCI Responses API (frontmatter URLs)
- Chat models; model pages for gpt-oss-120b, Grok 4.7, 4.6 and 4.3, Command A Reasoning, Llama 4 Maverick and Gemini 2.5 Pro; imported models (frontmatter URLs)
- Data handling, on-demand billing, model retirement, service limits (frontmatter URLs)
- Generative AI service FAQ <https://www.oracle.com/artificial-intelligence/generative-ai/generative-ai-service/faq>; the price list loads its figures by script and was not readable
