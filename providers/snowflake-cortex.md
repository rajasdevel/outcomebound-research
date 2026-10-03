---
last_checked: 2026-10-03
volatility: VOLATILE (the model list, preview status, rate limits and routing rules change monthly; the REST model table and the SQL model table disagree on some models)
kind: cloud platform
sources:
  - https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql
  - https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api
  - https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql-regional-availability
  - https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql-cost
  - https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql-caching
  - https://docs.snowflake.com/en/user-guide/snowflake-cortex/aisql-privileges-and-access
  - https://docs.snowflake.com/en/user-guide/snowflake-cortex/cross-region-inference
  - https://docs.snowflake.com/en/user-guide/snowflake-cortex/provisioned-throughput
  - https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-ai-gateway
  - https://docs.snowflake.com/en/user-guide/snowflake-cortex/governance-and-availability
  - https://docs.snowflake.com/en/guides-overview-ai-features
---

# Snowflake Cortex

cloud platform; the generative-AI layer of Snowflake's data platform. Models from Anthropic, OpenAI, Google, xAI, Meta, Mistral, DeepSeek, Moonshot, Z.ai and Qwen run inside Snowflake's security and governance perimeter unless the customer chooses otherwise, and are called three ways: as SQL functions over table columns (Cortex AI Functions such as `AI_COMPLETE`, `AI_CLASSIFY`, `AI_EXTRACT`), through a REST API that follows the OpenAI Chat Completions and Anthropic Messages shapes, and inside Cortex Agents. Billing is in Snowflake credits. Everything below was read on 2026-10-03 from Snowflake's documentation (class L).

## Models offered

Snowflake keeps two model tables, one for the SQL functions and one for the REST API; they overlap but are not identical. A star marks public preview and two stars private preview in the REST table. Availability depends on the account's Region and on cross-region inference.

- **Anthropic.** [Claude Opus 5.5](../models/anthropic/claude-opus-5-5.md) (public preview in both tables), [Opus 5](../models/anthropic/claude-opus-5.md), [Sonnet 5](../models/anthropic/claude-sonnet-5.md), [Sonnet 5.5](../models/anthropic/claude-sonnet-5-5.md) (public preview, REST table), [Haiku 4.5](../models/anthropic/claude-haiku-4-5.md), with Opus 4.8 to 4.5 and Sonnet 4.6 and 4.5. [Fable 5.1](../models/anthropic/claude-fable-5-1.md) and [Fable 5](../models/anthropic/claude-fable-5.md) are private preview in the REST table only.
- **OpenAI.** In the REST table, [GPT-6 Astra](../models/openai/gpt-6-astra.md) and GPT-5.6 Sol, [Terra](../models/openai/gpt-5.6-terra.md) and [Luna](../models/openai/gpt-5.6-luna.md) are marked available and [GPT-6 Sol](../models/openai/gpt-6-sol.md) and [GPT-6 Luna](../models/openai/gpt-6-luna.md) are public preview. GPT-5.5 is private preview. GPT-5.4 (public preview), 5.2, 5.1, 5, GPT-5 mini and nano and GPT-4.1 also appear. The SQL table lists GPT-5, 5.1, GPT-5 mini and nano, GPT-4.1 and GPT-5.4 mini and nano (400,000 tokens), but not GPT-6 or GPT-5.6.
- **Google (SQL table).** [Gemini 3.8 Flash](../models/google/gemini-3.8-flash.md), [3.7 Flash](../models/google/gemini-3.7-flash.md), [3.1 Flash-Lite](../models/google/gemini-3.1-flash-lite.md) and 3.5 Flash, each at 1,000,000 tokens context and 64,000 output, and [Gemini 3.1 Pro](../models/google/gemini-3.1-pro-preview.md) in public preview. Snowflake says Gemini 3.1 Pro and some OpenAI models require cross-region inference.
- **Mistral.** [Mistral Large 3](../models/mistral/mistral-large-3.md) (`mistral-large3`, 256,000 tokens context, 32,768 output) and Mistral Large 2 and 7B.
- **Open and other.** [Kimi K3](../models/moonshot/kimi-k3.md) and [GLM-5.3](../models/zai/glm-5.3.md) (private preview, REST table), a `deepseek-v4-flash` entry (private preview; Snowflake does not say whether it is the V4.1-Flash build in [this file](../models/deepseek/deepseek-flash.md)), DeepSeek R1, Llama 4 Maverick and Llama 3.1 and 3.3 builds, Qwen3 models, Snowflake's own Llama 3.3 build and embedding, extraction and document models.
- **xAI (SQL table).** [Grok 4.6](../models/xai/grok-4.6.md) (`grok-4.6`) in public preview for `AI_COMPLETE`, through cross-region inference only (the Cross Cloud and AWS US columns). Grok 4.7 is in neither table.
- **Not found in either table:** Grok 4.7, MiniMax and the Gemma family.
- **Lifecycle.** Models pass through a legacy stage, after which only accounts that already used the model can call it, and then end of life. `SHOW CORTEX BASE MODELS` shows each model's lifecycle status and dates.

## API surface

- **SQL.** Cortex AI Functions run in queries and in Python. A role needs the account-level `USE AI FUNCTIONS` privilege and one of the `CORTEX_USER` or `AI_FUNCTIONS_USER` database roles; both `USE AI FUNCTIONS` and `CORTEX_USER` are granted to `PUBLIC` by default. Snowflake recommends the SQL functions for large tables and REST for interactive use.
- **Cortex REST API.** Base URL `https://<account-identifier>.snowflakecomputing.com/api/v2/cortex/v1`. Chat Completions at `/chat/completions` serves every model and works with the OpenAI SDKs; the Messages endpoint at `/messages` serves Claude models only and follows the Anthropic spec. Both share auth, catalogue and rate limits. Separate Complete, Embed and Agents APIs exist.
- **Auth.** A Snowflake programmatic access token, key-pair JWT or OAuth token as a bearer token. The caller's default role must hold `SNOWFLAKE.CORTEX_USER` or the narrower `SNOWFLAKE.CORTEX_REST_API_USER`; the Anthropic SDK needs a custom `Authorization` header because it sends `x-api-key` by default.
- **Model ids.** Snowflake's own names: `claude-opus-5-5`, `openai-gpt-6-astra`, `openai-gpt-5.6-sol`, `llama4-maverick`, `mistral-large2`, `kimi-k3`, `gemini-3.8-flash` (SQL), `snowflake-llama-3.3-70b`.
- **Other surfaces.** Cortex Agents, Cortex Code (with a CLI that supports MCP), and Cortex AI Gateway (preview, AWS commercial Regions except New Zealand, Malaysia and Spain): one governed endpoint for coding agents, third-party clients and SDKs, with traces, budgets, per-user quotas and spend attribution.

## Feature parity

Compared with each maker's own API, from Snowflake's REST documentation.

- **Reasoning and effort.** Chat Completions takes a `reasoning` object for Claude (`reasoning.effort` or `reasoning.max_tokens`) and `reasoning_effort` (`none`, `minimal`, `low`, `medium`, `high`) for OpenAI reasoning models; no `xhigh` or `max` is listed. Only Claude returns reasoning details. The Messages endpoint supports adaptive thinking (`type: adaptive`) for Claude Opus 4.6 and newer and Sonnet 4.6, with `output_config.effort` of `low`, `medium`, `high` (default) or `max`. `temperature` is ignored for Claude Opus 4.7.
- **Tools.** Tool calling works for OpenAI and Claude models only, and for Claude only function tools in Chat Completions. Audio is not supported. Images work for OpenAI and Claude models (20 per conversation, 20 MiB per request).
- **Structured output.** Both endpoints support JSON-schema output (`response_format` on Chat Completions, `output_config` on Messages); Claude models accept only the `json_schema` type, OpenAI models others too.
- **Prompt caching.** OpenAI models cache implicitly for prompts of 1,024 tokens or more. Claude caching is explicit with `cache_control` of the ephemeral type only, a 5-minute lifetime and at most four breakpoints; the 1-hour option is not offered. Other models ignore `cache_control`. Separately, `AI_COMPLETE` reuses identical results within one query for 24 hours when settings are deterministic and the input is text; cache hits are not billed.
- **Batch.** No batch API as such: set-based SQL over many rows is the batch path, and Snowflake says the functions are tuned for throughput.
- **Limits of the compatibility layer.** `max_tokens` is deprecated in favour of `max_completion_tokens` (default 4,096; 131,072 is the stated theoretical maximum, and each model has its own lower limit); the Messages endpoint has no `service_tier` (no flex or priority) and accepts only Bedrock-compatible `anthropic-beta` header values, and Snowflake's list of supported values includes interleaved thinking, 128K output, context management, effort and tool search; error messages come from Snowflake, not the maker.
- **Long context.** In the SQL table, Claude Opus 5.5 to 4.6 and Sonnet 5 and 4.6 list 1,000,000 tokens (Opus models up to 128,000 output, Sonnet up to 64,000), Haiku 4.5, Sonnet 4.5 and Opus 4.5 list 200,000, Gemini 1,000,000 with 64,000 output, GPT-5.4 mini and nano 400,000, Mistral Large 3 256,000, Llama 3.x 128,000. Output cannot exceed the room left in the window, and input over the window is an error.
- **Streaming.** Supported on both endpoints.

## Pricing

- **Credits per token.** Cortex AI Functions and the REST API consume credits per million tokens at rates in Snowflake's Service Consumption Table; the table is not repeated here. Generation functions bill input and output tokens; embedding functions bill input only; `AI_PARSE_DOCUMENT` bills per page; `AI_EXTRACT` counts each page as 970 tokens; audio counts as 50 tokens per second; a classify call counts its labels and examples as input for every row.
- **Warehouse.** The warehouse that runs a query keeps billing while it waits; Snowflake advises no larger than MEDIUM.
- **Provisioned Throughput.** Reserved capacity in provisioned throughput units (PTUs), for a one-month term that does not renew by itself, charged in credits per PTU-hour whether used or not. It was documented for Mistral Large 2, Llama 3.1 and Snowflake's Llama builds only, with minimum sizes of 64 to 512 PTUs.
- **Cross-region inference** can change what a request costs; Snowflake lists the any-region setting as the lowest-cost option.
- **Usage views.** Per-function views and a REST-API usage view exist. Snowflake's cost page says granular usage cannot be had for REST requests while the REST page describes a view with request ids and token counts per request; the two statements conflict.

## Limits and data

- **Rate limits.** Defaults are per account and per model, in tokens per minute and requests per minute, with a 16,384-token output ceiling in the table. Examples: `claude-opus-4-7` 3,000,000 tokens and 10,000 requests; `claude-sonnet-4-6` 6,000,000 and 10,000; `openai-gpt-5.2` 1,200,000 and 3,000; `llama3.1-70b` 400,000 and 400. The table lists no row for the 5.x Claude models or the GPT-6 and GPT-5.6 models. Cross-region inference raises limits for some models. A sliding-window counter enforces them and a 429 means either limit was exceeded; `CORTEX_REST_API_RATE_LIMIT_POLICIES` shows the limits applied to an account. A budget overrun returns 402, and an expired session token can return HTTP 200 with error code 390112.
- **Regions and routing.** Models are served from the account's Region where available. Cross-region inference lets the service process a request elsewhere: any region and cloud (`ANY_REGION`), one or more clouds (`AWS_GLOBAL`, `AZURE_GLOBAL`, `GCP_GLOBAL`), a geography (`AWS_US`, `AWS_EU`, `AWS_APJ`, `AWS_JP`, `AWS_AU`, `AZURE_US`, `AZURE_EU`, `GCP_US`) or `DISABLED`. Stored customer data stays in the account's Region; the prompt and response travel to the processing region for the length of processing and are not persisted there. Accessing frontier models needs the setting enabled; accounts in new organisations created after 2026-03-09 in commercial regions default to `ANY_REGION`.
- **Privacy.** Snowflake states that, except where the customer elects otherwise, its AI models run inside its security and governance perimeter, that data is not available to other customers or model developers, and that it never uses customer data to train models offered to its customer base. In the legal table, inputs are Usage Data and outputs are Customer Data, and generally available functions are Covered AI Features while preview functions are Preview AI Features.
- **Retention and abuse monitoring.** Not stated on the pages read; no zero-retention option is named.
- **Access control.** Role-based; model-level access control exists, and the `SNOWFLAKE.CORTEX_USER` role and the `USE AI FUNCTIONS` privilege can be revoked from `PUBLIC` to narrow access. Cortex AI Gateway's single `SNOWFLAKE` gateway object is usable by `PUBLIC` by default.

## Notes for agents and harnesses

- The same model can have different names and availability in the SQL and REST tables; availability on one surface says nothing about the other.
- Preview models are marked as not suitable for production workloads; Snowflake sets that status per model.
- Compared with Anthropic's own API, the Messages endpoint lacks the flex and priority tiers, offers only the 5-minute cache lifetime, lists effort only up to `max` without `xhigh`, and accepts only a restricted set of beta headers.
- Tool calling, image input and reasoning details are limited to OpenAI and Claude models on the REST API, so a request routed to a Llama, Mistral or DeepSeek model through Chat Completions has no tool calling.
- A large `max_completion_tokens` still meets the 16,384-token output ceiling shown in the REST rate-limit table for the models listed there; 131,072 is only the theoretical maximum.
- An expired Snowflake session token can return HTTP 200 with error code 390112 and no work done; key-pair, OAuth and programmatic access tokens avoid this.
- Authentication uses the account URL and a role; the default role of the token's user, not the role set in a session, decides authorization.

## Sources

Read 2026-10-03 (class L, Snowflake documentation; URLs in the frontmatter):

- Cortex AI Functions overview, Cortex REST API (model availability, features, limitations, rate limits, known issues)
- Models and regional availability, cost considerations, caching, privileges and model access
- Cross-region inference, Provisioned Throughput, Cortex AI Gateway, governance and availability
- Snowflake AI features overview (privacy principles)
