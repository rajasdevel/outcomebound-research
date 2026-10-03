---
last_checked: 2026-10-03
volatility: VOLATILE (catalogue, prices, limits and feature support change often)
kind: inference host
sources:
  - https://nebius.com/newsroom/nebius-launches-nebius-token-factory-to-deliver-production-ai-inference-at-scale
  - https://docs.tokenfactory.nebius.com/
  - https://docs.tokenfactory.nebius.com/llms.txt
  - https://docs.tokenfactory.nebius.com/switch.md
  - https://docs.tokenfactory.nebius.com/ai-models-inference/overview.md
  - https://docs.tokenfactory.nebius.com/ai-models-inference/rate-limits.md
  - https://docs.tokenfactory.nebius.com/ai-models-inference/json.md
  - https://docs.tokenfactory.nebius.com/ai-models-inference/function-calling.md
  - https://docs.tokenfactory.nebius.com/other-capabilities/billing-new.md
  - https://docs.tokenfactory.nebius.com/api-reference/examples/list-of-models.md
  - https://docs.tokenfactory.nebius.com/legal/legal-quick-guide.md
  - https://docs.tokenfactory.nebius.com/public-serverless.md
  - https://docs.tokenfactory.nebius.com/august-2026-deprecation-notice.md
---

# Nebius Token Factory

inference host

Nebius Token Factory is Nebius's hosted inference service for open-weight models. Its former name was Nebius AI Studio. Nebius announced on 2025-11-05 that Token Factory is "the next evolution of Nebius AI Studio" and that existing users would move to it automatically. The old documentation address now redirects to `docs.tokenfactory.nebius.com`, and the Token Factory documentation read does not mention AI Studio. The service offers a pay-per-token inference API on shared ("public serverless") endpoints, dedicated endpoints in a chosen region, fine-tuning, a data lab and sandboxes for software-engineering agents. Nebius is a cloud company with its own data centres. [launch, docs, index]

## Models offered

Open-weight models from several makers, in text-to-text, embedding and vision groups. The launch announcement says more than 60 open-source models across text, code and vision (naming DeepSeek, Llama, OpenAI models, NVIDIA Nemotron and Qwen) and that customers can host their own models; dedicated endpoints accept custom weights. The documentation does not list the catalogue; its examples and notices name, among others, `moonshotai/Kimi-K2.5` (the switch guide's example), `deepseek-ai/DeepSeek-V4-Flash-0731`, `MiniMaxAI/MiniMax-M3`, `nvidia/Nemotron-3_5-Lightning`, `nvidia/nemotron-3-super-120b-a12b` and `Qwen/Qwen3.5-397B-A17B`, as replacements for models removed from serverless on 2026-08-31 (Llama 3.3 70B, MiniMax M2.5, Qwen3-32B and others). Model files in scope that those pages name: [DeepSeek Flash](../models/deepseek/deepseek-flash.md) and [MiniMax M3](../models/minimax/MiniMax-M3.md); the live list is `GET /v1/models`, which returns per model the id, context length, architecture, prompt and completion price and rate limits (`?verbose=true` gives more). Each model has a base flavour and a "fast" flavour (`-fast` suffix) that the overview says gives identical outputs with smaller batches, more compute and speculative decoding, at a different price. The overview says its optimisations (quantisation, KV and context caching, speculative decoding, among others) keep about 99 percent of the original model's quality, a vendor figure. Not every model supports structured output; model cards carry a "JSON mode" tag. [launch, ovw, switch, deprec, models, json]

## API surface

- **Protocol.** OpenAI-compatible at `https://api.tokenfactory.nebius.com/v1/`, with chat completions, completions, a Responses endpoint, embeddings and reranking in the API reference. No Anthropic-compatible endpoint is listed in the documentation index. [switch, index]
- **Auth.** An API key from tokenfactory.nebius.com, in the docs as `NEBIUS_API_KEY`, used as a bearer token through the OpenAI client. [switch, models]
- **SDKs.** The OpenAI SDK in Python and JavaScript, or cURL; the API accepts the full vLLM parameter set, the Playground a subset. [docs, ovw]
- **Model ids.** `org/model-name` as on Hugging Face, for example `deepseek-ai/DeepSeek-V4-Flash-0731`, with `-fast` for the fast flavour. [deprec, ovw]
- **Endpoints.** Public serverless endpoints are shared and show the region "Global"; the documentation says they suit testing and non-critical work, and that a region-specific base URL can stop working when the processing region changes. Dedicated endpoints run in a fixed region chosen by the customer. [serverless, legal]

## Feature parity

The documentation index has no pages on reasoning controls, prompt caching or batch, so those rows rest on passing mentions. [index]

- **Reasoning and effort.** No reasoning-control page exists in the index; parameters for reasoning models are `UNVERIFIED`. [index]
- **Tools.** OpenAI-format function calling, including MCP servers connected by the client. `tool_choice` is documented as `auto` (default) or an explicit function; `required` and `none` are not described, and parallel calls are not addressed. The page stresses that the model only emits the call and the client runs it. Examples use a Llama 3.1 8B fast model. [fc]
- **Structured output.** `response_format` with `json_schema` or `json_object`. The docs advise giving the schema in the prompt as well as in the parameter, and testing several models because support differs. [json]
- **Prompt caching.** The overview lists KV and context caching among its inference optimisations; no page describes cache pricing, controls or usage fields, so caching as a billed feature is `UNVERIFIED`. [ovw, index]
- **Batch.** The rate-limits page refers to a Batch API with significantly higher limits for asynchronous work, without describing it. [rate]
- **Vision, long context, streaming.** Vision models form their own group and the API reference has a vision example; context length is per model in the models endpoint. [ovw, index, models]

## Pricing

Prepaid credits debited in real time. A bank card is required at sign-up; the card is charged at the start of a month if the balance is negative or when a set threshold is reached, and a failed charge suspends the account. Companies can pay by bank transfer against monthly invoices. New accounts get a $1 trial credit valid for 30 days. Prices are per token per model, shown in the models endpoint and console, with fast flavours priced separately. The billing page says nothing on batch or cache pricing, and dedicated endpoints have their own billing-policy page, which was not read. [billing, models, ovw, index]

## Limits and data

- **Rate limits.** Requests and tokens per minute, with defaults shown in the console (the page's worked example starts at 60 requests and 400,000 tokens a minute). Limits adapt in rolling 15-minute windows: average use at or above 80 percent raises the next window's limit by 20 percent, use at or below 50 percent lowers it by a third, up to 20 times the base without an Enterprise agreement, which removes the soft caps and adds dedicated capacity and an SLA. `x-ratelimit-*` headers report limits, remaining capacity, resets and the dynamic scale; `x-ratelimit-over-limit: yes` marks a request served over the limit from spare capacity at lower priority; exceeding limits gives 429 with `Retry-After`. [rate]
- **Retention.** By default inputs and outputs are kept to train the speculative-decoding draft models, and that stored data is held in Finland (EU) wherever the request was processed. Zero data retention, set at organisation level on the account profile, stops all storage beyond in-flight processing and stops that use. The legal guide says content is not used to train any model in either mode. [legal]
- **Regions.** Public endpoints have no region commitment and can move without notice. Dedicated endpoints process data only in the region chosen, as a contractual commitment under the data processing agreement, with no failover to other regions. Fine-tuning data is stored in the EU for all customers (US customers' jobs are processed in the US). [legal, serverless]
- **Compliance.** The legal guide lists ISO 27001, ISO 27701 and SOC 2 Type II, HIPAA support, GDPR, a DPA in the terms of service, and EU-US Data Privacy Framework certification; the launch announcement adds ISO 27799 and a 99.9 percent uptime commitment. These are vendor statements. [legal, launch]

## Notes for agents and harnesses

- **The service was renamed.** Old AI Studio addresses redirect to Token Factory, whose API base is `api.tokenfactory.nebius.com`. [launch, docs]
- **Limits grow with steady load.** A client that starts with a burst can meet the starting limit before the 15-minute windows raise it; the page names the Batch API for asynchronous work, and the over-limit header is an early warning. [rate]
- **JSON support is per model.** The "JSON mode" tag on the model card marks support. [json]
- **Reasoning and caching controls are undocumented.** No page in the index describes effort parameters or cache billing. [index]
- **Default retention is on.** Without zero data retention, prompts and outputs are stored in the EU for speculative decoding. [legal]
- **Serverless models are retired on notice.** The August 2026 notice removed ten serverless models with no automatic rerouting; dedicated endpoints were unaffected. [deprec]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| launch | https://nebius.com/newsroom/nebius-launches-nebius-token-factory-to-deliver-production-ai-inference-at-scale | L | 2026-10-03 |
| docs | https://docs.tokenfactory.nebius.com/ | L | 2026-10-03 |
| index | https://docs.tokenfactory.nebius.com/llms.txt | L | 2026-10-03 |
| switch | https://docs.tokenfactory.nebius.com/switch.md | L | 2026-10-03 |
| ovw | https://docs.tokenfactory.nebius.com/ai-models-inference/overview.md | L | 2026-10-03 |
| rate | https://docs.tokenfactory.nebius.com/ai-models-inference/rate-limits.md | L | 2026-10-03 |
| json | https://docs.tokenfactory.nebius.com/ai-models-inference/json.md | L | 2026-10-03 |
| fc | https://docs.tokenfactory.nebius.com/ai-models-inference/function-calling.md | L | 2026-10-03 |
| billing | https://docs.tokenfactory.nebius.com/other-capabilities/billing-new.md | L | 2026-10-03 |
| models | https://docs.tokenfactory.nebius.com/api-reference/examples/list-of-models.md | L | 2026-10-03 |
| legal | https://docs.tokenfactory.nebius.com/legal/legal-quick-guide.md | L | 2026-10-03 |
| serverless | https://docs.tokenfactory.nebius.com/public-serverless.md | L | 2026-10-03 |
| deprec | https://docs.tokenfactory.nebius.com/august-2026-deprecation-notice.md | L | 2026-10-03 |
