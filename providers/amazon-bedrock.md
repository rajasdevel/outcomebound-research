---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often; the retention rules and the endpoint split are new in 2026 and still moving)
kind: cloud platform
sources:
  - https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
  - https://docs.aws.amazon.com/bedrock/latest/userguide/apis.md
  - https://docs.aws.amazon.com/bedrock/latest/userguide/endpoints.md
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.md
  - https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.md
  - https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.md
  - https://docs.aws.amazon.com/bedrock/latest/userguide/structured-output.md
  - https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.md
  - https://docs.aws.amazon.com/bedrock/latest/userguide/service-tiers-inference.md
  - https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.md
  - https://docs.aws.amazon.com/bedrock/latest/userguide/quotas-mantle.md
  - https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.md
  - https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.md
  - https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.md
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-openai-gpt-6-astra.md
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-xai-grok-4-6.md
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-moonshot-ai-kimi-k3.md
  - https://docs.aws.amazon.com/bedrock/latest/userguide/web-search.md
  - https://aws.amazon.com/bedrock/pricing/
  - https://aws.amazon.com/bedrock/faqs/
  - https://platform.claude.com/docs/en/build-with-claude/prompt-caching
  - https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock
  - https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws
  - https://platform.claude.com/docs/en/build-with-claude/overview
---

# Amazon Bedrock

cloud platform; Amazon Web Services' managed model service. Since 2026 it has two regional request endpoints, `bedrock-runtime` and `bedrock-mantle`. Both run on the same AWS inference engine, which AWS calls Mantle, and AWS describes its design as zero operator access: no operator of the service can see model inputs or outputs. The Bedrock-native APIs (`InvokeModel`, `Converse`) exist on `bedrock-runtime` only; the OpenAI-shaped and Anthropic-shaped APIs exist on both endpoints, with different feature sets. Models come from Anthropic, OpenAI, xAI, Moonshot AI, DeepSeek, MiniMax, Mistral, Qwen, Google (Gemma), NVIDIA, Z.ai, Amazon (Nova, Titan), Meta, Cohere, AI21, Writer, Stability and TwelveLabs. Everything below was read on 2026-10-03 from AWS and Anthropic documentation (class L) unless it says otherwise.

## Models offered

AWS's overview page says Bedrock supports more than 100 foundation models. The text and reasoning models that have a file in this library are listed below. A model on Bedrock is not always on both endpoints or in every Region, so the model's own card page on AWS decides (L).

- **Anthropic.** [Claude Fable 5.1](../models/anthropic/claude-fable-5-1.md), [Fable 5](../models/anthropic/claude-fable-5.md), [Opus 5.5](../models/anthropic/claude-opus-5-5.md), [Opus 5](../models/anthropic/claude-opus-5.md), [Sonnet 5.5](../models/anthropic/claude-sonnet-5-5.md), [Sonnet 5](../models/anthropic/claude-sonnet-5.md) and [Haiku 4.5](../models/anthropic/claude-haiku-4-5.md) are on the Messages-API integration (which Anthropic's page scopes to Opus 4.7 and later), with Opus 4.8 and 4.7; older Claude models (Opus 4.6 back to Claude 3 Haiku) stay in the AWS catalogue on the native APIs. Anthropic lists the Mythos models as invitation only; for Opus 5.5, Opus 5 and Sonnet 5.5 it points to the AWS console for the access criteria, and it lists the others as open to all Bedrock customers.
- **OpenAI.** [GPT-6 Astra](../models/openai/gpt-6-astra.md) (launched on Bedrock 2026-09-08), [GPT-6.1 Sol](../models/openai/gpt-6.1-sol.md), [GPT-6 Sol](../models/openai/gpt-6-sol.md), [GPT-6 Luna](../models/openai/gpt-6-luna.md), GPT-5.6 Sol, [Terra](../models/openai/gpt-5.6-terra.md) and [Luna](../models/openai/gpt-5.6-luna.md), plus GPT-5.5, GPT-5.4, two cyber-focused GPT-5.6 variants (named "Daybreak Red" and "Daybreak Blue" in AWS's list), two gpt-oss-safeguard models and the open-weight [gpt-oss-120b](../models/openai/gpt-oss-120b.md) and [gpt-oss-20b](../models/openai/gpt-oss-20b.md).
- **xAI.** [Grok 4.7](../models/xai/grok-4.7.md), [Grok 4.6](../models/xai/grok-4.6.md) and Grok 4.3.
- **Moonshot AI.** [Kimi K3](../models/moonshot/kimi-k3.md) (launched on Bedrock 2026-09-18), with K2.5 and K2 Thinking.
- **Mistral.** [Mistral Large 3](../models/mistral/mistral-large-3.md), plus Devstral 2, Magistral Small, Ministral and Pixtral.
- **Google.** Gemma 4 [31B](../models/google/gemma-4-31b-it.md), [26B-A4B](../models/google/gemma-4-26b-a4b-it.md) and [E2B](../models/google/gemma-4-e2b-it.md).
- **Alibaba.** [Qwen3-Coder-Next](../models/alibaba/qwen3-coder-next.md) and several earlier Qwen3 models.
- **Listed without a file here.** DeepSeek V3.2, V3.1 and R1; MiniMax M2.5, M2.1 and M2; Z.ai GLM 5, 4.7 and 4.7 Flash; NVIDIA Nemotron 3 Super and Nano; Meta Llama 3 and 4; Cohere Command R and R+, Embed and Rerank; Amazon Nova 2 Lite, Nova Premier, Pro, Lite, Micro, Canvas, Reel and Sonic; AI21 Jamba 1.5; Writer Palmyra; image, video and embedding models.
- **Not in the catalogue page on this date:** Gemini models, DeepSeek V4, MiniMax M3, Kimi K2.7 Code, GLM 5.2 and later, and Meta's Muse models.

Claude Platform on AWS is a different route. Anthropic operates it on AWS infrastructure and bills through AWS Marketplace, and it exposes the Claude API unchanged. On Bedrock, AWS operates the inference. Workspaces on Claude Platform on AWS created before 2026-09-18 may run outside AWS (Anthropic's page, L).

## API surface

AWS describes five API patterns on two regional endpoints (L).

| Endpoint | Host pattern | APIs |
| --- | --- | --- |
| `bedrock-runtime` (the one AWS recommends for new work) | `bedrock-runtime.{region}.amazonaws.com` | `InvokeModel`, `Converse` and `ConverseStream`, Chat Completions and Responses under `/openai/v1`, Anthropic Messages |
| `bedrock-mantle` | `bedrock-mantle.{region}.api.aws` | Responses and Chat Completions (both under `/openai/v1`), Anthropic Messages (under `/anthropic/v1/messages`) |

- **Auth.** AWS SigV4 on both endpoints, or a Bedrock API key sent as a bearer token. Short-term keys last up to 12 hours (or the session) and are the recommended kind. Long-term keys create an IAM user and AWS recommends them for exploration only. The environment variable is `AWS_BEARER_TOKEN_BEDROCK`. A key does not grant access by itself: the IAM principal still needs `bedrock:InvokeModel` (runtime) or `bedrock-mantle:CreateInference` (Mantle). Anthropic's page adds IAM assumed roles (12-hour maximum) and a Bedrock service role for the Messages integration.
- **SDKs.** AWS SDKs (for example boto3 `bedrock-runtime`) for the native APIs. The OpenAI SDK works after changing the base URL and key. Anthropic's SDKs have Mantle classes (`AnthropicBedrockMantle` and equivalents in TypeScript, C#, Go, Java, PHP and Ruby) for SigV4; the plain Anthropic client works with a bearer token only. A token-generator package exists for Python, JavaScript and Java.
- **Model ids.** Claude models on the Messages integration use `anthropic.claude-opus-5-5`. Older Claude models keep versioned ids such as `anthropic.claude-haiku-4-5-20251001-v1:0` on the native APIs. Other makers use `openai.gpt-6-astra`, `xai.grok-4.6` and `moonshotai.kimi-k3`. An inference profile adds a prefix: `global.`, `us.`, `eu.`, `jp.` or `au.` (for example `global.openai.gpt-5.6-sol`). Some models have no in-Region id on `bedrock-runtime` and must be called through a profile; the cards for GPT-6 Astra, Grok 4.6 and Kimi K3 say so.
- **Which endpoint serves a model** differs per model. GPT-6 Astra and Grok 4.6 are on both. Kimi K3 is on `bedrock-runtime` only; its card recommends the Chat Completions API, and the OpenAI-shaped APIs in general over Converse.

## Feature parity

Against each maker's own API. The Claude items come from Anthropic's features overview and its Bedrock page; the rest from AWS pages and model cards (L).

- **Reasoning and effort.** Claude's thinking, adaptive thinking and effort are listed as available on Bedrock. For OpenAI and xAI models the Responses API carries a `reasoning` object. Grok 4.6 accepts effort `low` (default), `medium`, `high` and `xhigh`. Its encrypted reasoning comes back only when the request lists `reasoning.encrypted_content` in `include`, and Chat Completions returns no reasoning tokens for it. Kimi K3 called through `Converse` fails with an internal error when reasoning blocks from earlier turns are sent back, and Converse also rejects attached PDF and HTML documents for it; AWS says the first problem affects LangChain and Strands Agents in their default settings.
- **Tools.** Client-side tool calling works on both endpoints. Server-side and pre-configured tools exist on Mantle only. The one AWS documents is its own Web Search tool, through the Responses API, for GPT-5.6 Sol, Terra and Luna, GPT-5.5 and GPT-5.4 in US East (N. Virginia), US East (Ohio) and US West (Oregon), and for a subset in GovCloud; the page names no GPT-6 model for it. For Claude, these are not available on Bedrock: code execution, web search, web fetch, the advisor tool, Agent Skills, the MCP connector, programmatic tool calling, the Files API and URL sources, Message Batches, the Models, Admin, Compliance and Usage and Cost APIs, Claude Managed Agents and server-side fallback. The `computer_toolset_20260801` and `browser_toolset_20260801` toolsets are not available either, while the beta computer-use versions are (Anthropic's page).
- **Structured output.** AWS supports JSON-schema output on `Converse` (`outputConfig.textFormat`) and on `InvokeModel` (`output_config.format` for Claude, `response_format` for open-weight models), plus strict tool use (`strict: true`). It accepts a subset of JSON Schema 2020-12: no recursion, no `minimum` or `maximum`, no string-length limits, `additionalProperties` only `false`, `minItems` only 0 or 1. A new schema is compiled first, which AWS says can take up to a few minutes, and compiled grammars are cached for 24 hours. The Anthropic Messages API on Mantle rejects `output_config.format` with HTTP 400. On Claude it does not combine with citations (HTTP 400), and some geographic profiles lack it for some models (AWS names Claude Haiku 4.5 through the India profile). For Claude the sources fit together once the integration is named: Anthropic's Bedrock page lists structured outputs as unsupported on the Messages integration, its features overview says they exist on Bedrock only through the legacy `InvokeModel` integration and only for Opus 4.6, Sonnet 4.6, Sonnet 4.5, Opus 4.5 and Haiku 4.5, and AWS describes them for Claude on `Converse` and `InvokeModel` without a model list. No source read confirms them for the 5.x Claude models on Bedrock. The Grok 4.6 card lists structured outputs as unsupported on `bedrock-runtime` and supported on Mantle, the reverse of the Claude case. The GPT-6 Astra card documents JSON schema on `bedrock-runtime` and says the Converse call also needs `additionalModelRequestFields.text.format.strict` set to true.
- **Prompt caching.** Two kinds: implicit (best effort, no request change) and explicit (checkpoints or breakpoints). Minimum prefix per checkpoint for Claude is 512 tokens for Opus 5.5, Opus 5, Sonnet 5.5 and the Fable models, 1,024 for Sonnet 5 and Opus 4.8, and 4,096 for Opus 4.7 and Haiku 4.5. At most four checkpoints, in `tools`, `system` and `messages`, with a TTL of 5 minutes or 1 hour. GPT-5.6 models take `prompt_cache_breakpoint` blocks with a minimum 30-minute lifetime, cache writes at 1.25 times the input rate and reads at a 90 percent discount; `cache_write_tokens` is a usage field. Caching does not work with batch inference. Cached tokens read from the cache do not count against the input-token quota. Anthropic's caching page says caches on Bedrock are isolated per organization, not per workspace as on Anthropic's own API.
- **Batch.** Bedrock batch inference reads JSONL from S3 and writes to S3, in InvokeModel or Converse format; the pricing page states a 50 percent lower price than on-demand for select models, and an OpenAI Batch API page exists as well. AWS's batch page says tool calling and structured output are not supported in batch, while its structured-output page says batch works without setup. The two were not reconciled. Anthropic's Message Batches API is not available on Bedrock.
- **Long context.** Anthropic's features overview lists context windows as available on Bedrock; the pages read give no Bedrock-specific Claude limit, so each model file's window is the reference. GPT-6 Astra is listed at 1,050,000 tokens with 128,000 output, Grok 4.6 at 500K and Kimi K3 at 1M. Astra's long-context price applies to the whole request once input passes 272,000 tokens.
- **Vision.** Per model. Kimi K3 accepts images (the `detail` setting is honoured only on Chat Completions) and rejects video. Claude accepts images and PDFs. Grok 4.6 accepts images.
- **Streaming.** Supported. Anthropic's page says the Messages endpoint on Mantle uses standard server-sent events, unlike the `InvokeModel`-based integration.
- **Other differences.** Guardrails, intelligent prompt routing and cross-Region profiles exist on `bedrock-runtime` only. Background (asynchronous) Responses requests, Projects and Workspaces exist on Mantle only. The GPT-6 Astra and Grok 4.6 cards list count-tokens as unsupported.

## Pricing

- **On demand, per token.** Input and output are billed separately, and per-token prices for one model are identical on both endpoints (AWS). Prices live on each model card page and the pricing page; they are not repeated here.
- **Service tiers**, set with `service_tier`: Standard (default); Priority (a 75 percent premium over Standard, stated on the pricing page and on the Grok 4.6 and Kimi K3 cards); Flex (a 50 percent discount, stated in the same places); and Reserved (capacity bought for 1 or 3 months at a fixed price per 1K tokens per minute, billed monthly, overflowing into Standard, with a minimum of 100,000 input and 10,000 output tokens per minute, arranged through the AWS account team). Not every model has every tier; the Kimi K3 card says only its Responses and Chat Completions APIs accept a tier. GPT-6 Astra has Standard and a speed tier called Ultrafast that AWS prices at six times Standard, and has no Priority, Flex or Reserved.
- **Regional premium.** For Claude, global endpoints carry no premium and regional endpoints cost 10 percent more. For GPT-6 Astra, in-Region and geographic profiles include a 10 percent premium over OpenAI's rates and the global profile matches them. AWS's cross-Region page says global profiles cost roughly 10 percent less than geographic ones and that routing adds no charge.
- **Other meters.** Batch at a discount; Provisioned Throughput with no commitment or on 1-month or 6-month terms (not available through inference profiles); Guardrails per 1,000 text units; intelligent prompt routing per 1,000 requests; web search per query; customization by training tokens plus storage.

## Limits and data

- **Quotas.** `bedrock-runtime` has fixed per-model RPM and TPM with increases on request; the GPT-6 Astra card says each output token counts ten times against the TPM quota. `bedrock-mantle` has separate input and output tokens-per-minute quotas per model and Region, no RPM limit, and published defaults only for Claude Opus 4.7 (20 million input, 4 million output); other models are throttled by internal capacity. A Mantle request is admitted against the input quota using the prompt size plus `max_tokens` (or the model maximum when unset), and the unused part is returned afterwards. Mantle increases go through an AWS Support case, not Service Quotas. For Claude the default is 2 million input tokens per minute, with up to 5 million input and 500,000 output available without extra Anthropic approval.
- **Regions.** Claude on Bedrock lists 27 Regions, all with the global endpoint, some with US, EU, JP or AU profiles and some with in-region-only routing; Fable 5.1 regional endpoints exist in `us-east-1` only. GPT-6 Astra on Mantle is in `us-east-1` and `us-west-2`, and on `bedrock-runtime` it is reached through US geographic and global profiles. Grok 4.6 on Mantle is in `us-west-2` and GovCloud East. Kimi K3 is reached through a US geographic profile and a global profile that covers most commercial Regions.
- **Operator access and storage.** AWS states a zero-operator-access design and a default of not storing inputs or outputs. Model makers cannot read Bedrock logs or customer prompts, because the model software runs in AWS-owned deployment accounts. For abuse detection AWS may retain data for some models. For the OpenAI models it names (GPT-6 Astra, Sol and Luna, GPT-5.6 Sol, Terra and Luna, GPT-5.5, GPT-5.4 and the two Daybreak variants; GPT-6.1 Sol is not in the list), classifier-flagged traffic is kept up to 30 days, and eligible customers can ask the AWS account team for full zero retention. For Claude Fable 5 and 5.1, all traffic is kept up to 30 days and flagged traffic may get human review by AWS. Customers in the Enterprise Frontier Safeguards program get zero retention through 2026-12-31. Retained data is stored in the Region that processed the request, which under cross-Region inference is the destination Region. AWS may also scan image inputs for child sexual abuse material and reject a request with HTTP 400.
- **Retention modes (new in 2026).** A per-Region setting at account or project level: `none` (zero retention; Responses `store` defaults to false), `default` (the model's own policy), `aws_review` (retention up to 30 days inside AWS for the human review some makers require, with nothing sent to the maker) and a legacy `provider_data_share` that AWS says shares nothing today. Claude Fable 5 and 5.1 need `aws_review` or the legacy mode; below that they show as unavailable (Mantle) or return a validation error (runtime). Zero retention for such models is a per-account, per-model request to the AWS account manager, and for Claude, eligibility is managed by Anthropic. Setting `store=false` on Responses does not by itself guarantee zero retention. At launch the settings had no console control and were set by API.
- **Training use.** The Bedrock FAQ says neither AWS nor the third-party model providers use Bedrock inputs or outputs to train Amazon Nova, Amazon Titan or any third-party model, and that inputs and outputs are not made available to the model providers. The user-guide data-protection pages contain no sentence on training.
- **Logging.** CloudWatch and CloudTrail; Anthropic recommends keeping activity logs on at least a rolling 30-day basis.

## Notes for agents and harnesses

- Anthropic's page says Claude Code 2.1.255 or later is needed for Fable 5.1 on Bedrock and 2.1.280 or later for Opus 5.5.
- A request that names an application inference profile is rejected with HTTP 400 on the Responses and Chat Completions APIs; geographic and global profiles work. On `bedrock-runtime` Responses, the caller also needs `bedrock:InvokeModel` on the account's default project in addition to the profile (the Grok 4.6 card). Responses on `bedrock-runtime` are always synchronous, and `background=true` returns 400.
- Effort and thinking follow the maker's own parameters on the Messages and Responses surfaces. The native `Converse` surface wraps maker-specific fields in `additionalModelRequestFields`, so one setting is spelled differently by endpoint.
- A large `max_tokens` on Mantle consumes input-quota headroom at admission; an unset one is charged at the model maximum.
- Data-retention gates can make a model disappear from the model list without any access error elsewhere. The `status` and `data_retention` fields of the Mantle model endpoint show why.
- AWS's batch page and structured-output page disagree on whether batch accepts structured output, and structured-output support for Claude depends on the integration and model, so only a probe on the exact endpoint, model and Region settles it. AWS names the model card as the authority.

## Sources

Read 2026-10-03; all class L (AWS or Anthropic documentation):

- What is Amazon Bedrock <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html>
- APIs <https://docs.aws.amazon.com/bedrock/latest/userguide/apis.md> and endpoints <https://docs.aws.amazon.com/bedrock/latest/userguide/endpoints.md>
- Models at a glance <https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.md>, and the model cards for GPT-6 Astra, Grok 4.6 and Kimi K3 (URLs in the frontmatter)
- API keys <https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.md>
- Prompt caching, structured output, batch inference, service tiers, cross-Region inference, Mantle quotas and Web Search (URLs in the frontmatter)
- Data protection, data retention and abuse detection (URLs in the frontmatter); Bedrock FAQ <https://aws.amazon.com/bedrock/faqs/> for the training-use statement
- Pricing <https://aws.amazon.com/bedrock/pricing/>; used for its structure and its stated tier and batch percentages, not for per-model rates
- Claude in Amazon Bedrock <https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock>, Claude Platform on AWS <https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws>, the features overview <https://platform.claude.com/docs/en/build-with-claude/overview> and prompt caching <https://platform.claude.com/docs/en/build-with-claude/prompt-caching>
