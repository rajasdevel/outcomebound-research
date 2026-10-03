---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: first-party lab API
sources:
  - https://www.alibabacloud.com/help/en/model-studio/models
  - https://www.alibabacloud.com/help/en/model-studio/regions
  - https://www.alibabacloud.com/help/en/model-studio/rate-limit
  - https://www.alibabacloud.com/help/en/model-studio/privacy-notice
  - https://docs.qwencloud.com/developer-guides/getting-started/first-api-call
  - https://docs.qwencloud.com/developer-guides/getting-started/pricing
---

# Alibaba Cloud Model Studio

first-party lab API

Alibaba trains the Qwen models and sells them through Model Studio, its model-serving service on Alibaba Cloud, and through QwenCloud, a second site (qwencloud.com, docs at docs.qwencloud.com) that serves the same hosted models. The two documentation sites agree on most facts and differ in places, so this file names the site behind each fact. Besides Qwen, the Model Studio catalogue also carries models from other labs. You pick a region and a deployment scope, and the key is held in an environment variable named `DASHSCOPE_API_KEY`. [models, regions, first-call]

## Models offered

The Model Studio models page (updated 2026-09-28) lists flagship text models `qwen3.8-max`, `qwen3.7-plus` and `qwen3.8-flash`; omni models (`qwen3.8-omni-flash`, a realtime variant and `qwen3.5-omni-plus`); image and video generation models; speech synthesis, recognition and speech-to-speech models; embeddings and a reranker; and third-party text models: `deepseek-v4-pro-0813`, `deepseek-v4.1-flash`, `glm-5.2`, a GLM-5.3 entry, `kimi-k3` and `MiniMax-M2.5`. The open-weight Qwen models (the 2.4T and 27B 3.8 models, Flash-Next, Coder-Next) have model files but the page lists no hosted id for the 2.4T and Flash-Next weights; the maker README says QwenCloud hosts a 27B model and says Coder-Next's hosted endpoint retires on 2026-10-10. [models]

| Model file | Served here as |
| --- | --- |
| [Qwen3.8-Max](../models/alibaba/qwen3.8-max.md) | `qwen3.8-max`; dated snapshot `qwen3.8-max-0902` on QwenCloud |
| [Qwen3.7-Plus](../models/alibaba/qwen3.7-plus.md) | `qwen3.7-plus` |
| [Qwen3.8-Flash](../models/alibaba/qwen3.8-flash.md) | `qwen3.8-flash` |
| [Qwen3.8-Omni-Flash](../models/alibaba/qwen3.8-omni-flash.md) | `qwen3.8-omni-flash` |
| [Qwen3.8-27B](../models/alibaba/qwen3.8-27b.md) | hosted on QwenCloud per the maker README; not on the Model Studio page read |
| [Qwen3-Coder-Next](../models/alibaba/qwen3-coder-next.md) | hosted endpoint retires 2026-10-10 per the maker README |
| [Qwen3.8-2.4T-A95B](../models/alibaba/qwen3.8-2.4t-a95b.md), [Qwen3.8-Flash-Next](../models/alibaba/qwen3.8-flash-next.md) | open weights; no hosted id found on the page read |
| [DeepSeek V4 Pro](../models/deepseek/deepseek-v4-pro.md) | `deepseek-v4-pro-0813` |
| [DeepSeek Flash](../models/deepseek/deepseek-flash.md) | `deepseek-v4.1-flash` |
| [Kimi K3](../models/moonshot/kimi-k3.md) | `kimi-k3` |

The maker README records that a bare id is an alias and a dated id a snapshot, and that the bare `qwen3.8-max` moved to the 0902 snapshot on 2026-09-05; the Model Studio page, updated 2026-09-28, shows only the bare name and says nothing about aliases. The lineage is in the [maker README](../models/alibaba/README.md). [models]

## API surface

- **Protocols.** An OpenAI-compatible Chat Completions endpoint, `https://maas.qwencloudapi.com/compatible-mode/v1` on QwenCloud. The maker README records that the service also speaks the OpenAI Responses protocol, Alibaba's native DashScope protocol and an Anthropic Messages endpoint at `https://maas.qwencloudapi.com/apps/anthropic`, which offers only `/v1/messages` and no model-list call. [first-call]
- **Endpoints by site.** Model Studio documents three endpoint types: a workspace-dedicated host (`{WorkspaceId}.{region}.maas.aliyuncs.com`, advised for production because of higher concurrency), the DashScope host (`dashscope-intl.aliyuncs.com`, described as legacy, with no new features after 2026-09-30) and a trial host not meant for production. The page gives the workspace host a 3,600-second timeout against 600 seconds on the DashScope host. [regions]
- **Auth.** An API key from the console, exported as `DASHSCOPE_API_KEY`; QwenCloud keys start `sk-ws-`. [first-call]
- **SDKs.** The QwenCloud quick start shows the OpenAI SDKs in Python and Node.js and plain HTTP, and says other languages (Java, Go, PHP, C#) can use the compatible endpoint with standard HTTP clients. [first-call]
- **Regions.** Six: China (Beijing, `cn-beijing`), Singapore (`ap-southeast-1`), Germany (Frankfurt, `eu-central-1`), Japan (Tokyo, `ap-northeast-1`), China (Hong Kong, `cn-hongkong`) and US (Virginia, `us-east-1`). Beijing is mainland-only, Singapore international-only, and the other four offer a Global scope and a regional one. [regions]
- **Model ids.** Lower-case family and version (`qwen3.8-max`), with a date or `-0902` style suffix for snapshots. [models]

## Feature parity

First-party; the points below are what the sites document, with the long list in the maker README. [first-call, rate]

- **Reasoning and effort.** `enable_thinking` switches thinking on hybrid models, `thinking_budget` caps reasoning tokens, and `reasoning_effort` (low, medium, xhigh) is listed for Max on QwenCloud but, per the maker README, only for Omni-Flash on Model Studio's page. In thinking mode `max_tokens` is capped at 32,768 and counts only the reply, while `max_completion_tokens` covers reasoning plus reply. Thinking tokens bill as output. (Maker README.)
- **Tools.** OpenAI-format function calling, with built-in web search, web extractor, code interpreter, image search, PDF parsing and web fetch switched on with `enable_search` or a `tools` entry; `required` tool choice is not supported in thinking mode (maker README).
- **Structured output.** JSON Object mode everywhere; strict JSON Schema mode on a short list (Max and Flash among them), and a model in thinking mode may not produce valid JSON (maker README).
- **Caching.** Implicit caching is automatic; explicit caching takes `cache_control` blocks, at least 1,024 tokens, five minutes from the last hit (maker README). [pricing]
- **Batch.** A 50 percent discount for asynchronous work, on certain models; batch calls bypass real-time rate limits though queuing applies. [pricing, rate]
- **Long context.** 1M tokens and 131,072 output on the 3.8 models (maker README).
- **Vision, audio, video.** Image and video input on the lead models, and separate generation and speech models. [models]
- **Streaming.** Advised to avoid timeouts; some models require it (maker README).

## Pricing

Per million tokens with input and output priced separately, and tiered pricing that bills every token in a request at the tier its size matches, not incrementally. Image models bill per image, video per second, speech per character or second, and embeddings per million input tokens. Batch is 50 percent off, context caching discounts reused prompts by a model-specific amount, and the two discounts cannot be combined on one request. Failed calls are not charged and do not use free quota. New users get a free quota; the pricing guide read does not give its size or duration. Top-ups do not raise rate limits. Per-model prices are in the model files. [pricing, rate]

## Limits and data

- **Rate limits.** Counted per primary account, so all sub-accounts, workspaces and API keys add up; each model has its own requests-per-minute and tokens-per-minute quotas, with per-second smoothing and a burst guard ("request rate increased too quickly") that can reject traffic under both caps. Recovery is typically within a minute. Limits for the 3.8 Max and Flash models are "dynamic" in the Singapore and Beijing rows, and 30,000 requests and 5,000,000 tokens per minute each in the US (Virginia) Global row (Flash has the same figure in the Frankfurt Global row). Topping up does not change limits; a higher quota is requested through a business manager or the console. [rate]
- **Regions and residency.** The region sets where the service is accessed and where static data (including inputs and outputs) is stored; the deployment scope sets where inference runs, so storage and compute can differ. [regions]
- **Retention and training.** Alibaba states it will never use customer data for model training. It stores data from model and application calls in line with regulations and points to the service agreement for retention periods, which the notice does not give. SOC 2 compliance with an unqualified opinion is stated. No zero-data-retention option was found. [privacy]

## Notes for agents and harnesses

- **Two doc sites.** Parameter support can differ between Model Studio and QwenCloud (the `reasoning_effort` example above), so a result read on one site does not establish behaviour on the other's endpoint.
- **Aliases move.** A bare id can move to a new snapshot on a stated date, so a measurement or pipeline that names the bare id spans different weights before and after. (Maker README.)
- **Thinking switches.** `enable_thinking` goes at the top level of the body on QwenCloud, via `extra_body` in the OpenAI SDK; the open-weight cards show it inside `chat_template_kwargs`, which is the self-hosted form (maker README).
- **Effort and budget do not combine** for `qwen3.8-max` on QwenCloud (maker README).
- **Anthropic-format clients.** The endpoint has no model-list route, so a client that discovers models needs ids supplied by hand, and temperature is accepted up to but not including 2 (maker README).
- **Account-wide limits.** Because every key under one account shares a quota, one noisy job can starve another; the burst guard can trip below the stated numbers. [rate]
- **Scope and residency.** A Global deployment scope may run inference outside the storage region. [regions]
- **Other labs' models.** DeepSeek, Zhipu, Moonshot and MiniMax models run here under Alibaba's terms and limits, not those labs' own, so their API behaviour and data terms need checking on this route. [models, privacy]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| models | https://www.alibabacloud.com/help/en/model-studio/models | L | 2026-10-03 |
| regions | https://www.alibabacloud.com/help/en/model-studio/regions | L | 2026-10-03 |
| rate | https://www.alibabacloud.com/help/en/model-studio/rate-limit | L | 2026-10-03 |
| privacy | https://www.alibabacloud.com/help/en/model-studio/privacy-notice | L | 2026-10-03 |
| first-call | https://docs.qwencloud.com/developer-guides/getting-started/first-api-call | L | 2026-10-03 |
| pricing | https://docs.qwencloud.com/developer-guides/getting-started/pricing | L | 2026-10-03 |
