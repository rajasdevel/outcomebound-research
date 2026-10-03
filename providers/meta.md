---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: first-party lab API
sources:
  - https://dev.meta.ai/docs
  - https://dev.meta.ai/docs/models
  - https://dev.meta.ai/docs/pricing-rate-limits
  - https://letsdatascience.com/news/meta-unveils-muse-spark-11-opens-developer-preview-4e60d164
---

# Meta API

first-party lab API

Meta trains the Muse Spark models and sells them through the Meta Model API: developer site dev.meta.ai, base URL `https://api.meta.ai/v1`, opened as a developer preview in July 2026 according to a press report. The same API also serves an image model, a speech-to-text model and a segmentation model. Muse Glimmer, the open-weight Muse model, is not served by this API; Meta's docs describe it as something you self-host. Meta's earlier Llama models are not part of this API and are out of scope for this library. [docs, models]

## Models offered

The models page names Muse Spark (the agentic model, in versions 1.3, 1.2 and 1.1, with 1.3 the latest; input of text, image, video, PDF and, with a qualifier, audio; a 1,048,576-token context), Muse Image (`muse-image-1.0`, generation and editing), Muse Voice Transcribe (`muse-voice-transcribe-1.0`, speech to text in 25 languages) and SAM 3.1 (segmentation returning boxes and masks). A `GET /v1/models` call lists what the key can use. [models, docs]

| Model file | API id | Note |
| --- | --- | --- |
| [Muse Spark 1.3](../models/meta/muse-spark-1.3.md) | `muse-spark-1.3` | latest; a cheaper `-contributor` id exists |
| [Muse Spark 1.2](../models/meta/muse-spark-1.2.md) | `muse-spark-1.2` | previous generation |
| [Muse Glimmer 30B](../models/meta/muse-glimmer-30b.md) | none | open weights, self-hosted only |

Muse Spark 1.1 is still listed on the models page and has no file here. The pricing page offers `-contributor` ids for 1.3 and 1.2 only. The [maker README](../models/meta/README.md) has the lineage and records that Meta publishes no retirement date for 1.2 or 1.1. [models, pricing]

## API surface

- **Protocols.** Three, per the overview: the Responses API at `https://api.meta.ai/v1` (recommended for agentic, multi-step work), an OpenAI-compatible Chat Completions endpoint and an Anthropic-compatible Messages API; the maker README records the Messages base as `https://api.meta.ai`. [docs]
- **Auth.** A bearer token, kept in `MODEL_API_KEY`, sent to the base URL. [docs]
- **SDKs.** The overview calls the API drop-in compatible with the OpenAI SDK, the Anthropic SDK and OpenAI-compatible agent CLIs; no Meta SDK was found. Meta also ships Muse Code, a terminal and CI coding agent built for Muse Spark. [docs]
- **Model ids.** Lower-case `muse-spark-` plus the version, with `-contributor` for the discounted tier. [models, maker README]
- **Compatibility limits.** The maker README records, for the Messages surface, that `thinking: disabled` returns 400, that `top_k`, `stop_sequences`, `container` and `inference_geo` return 400, that a named `tool_choice` is rejected, and that the surface is stateless.

## Feature parity

First-party, so the points are what the Meta API itself provides; the field-level detail is in the maker README. [docs, pricing]

- **Reasoning and effort.** `reasoning.effort` (Responses), `reasoning_effort` (Chat Completions), or `thinking` and `output_config.effort` (Messages); levels `minimal` to `xhigh`, plus `max` for 1.3 on the standard tier; `none` returns HTTP 400 (maker README).
- **Tools.** Function tools, custom tools and a `web_search` grounding tool on Responses, with `tool_choice` limited to `auto` (maker README). Web search grounding costs $2.50 per 1,000 queries. [pricing]
- **Structured output.** `response_format` of type `json_schema` (maker README).
- **Caching.** Prefix caching is automatic, with a cached-input rate on both tiers. [pricing]
- **Batch.** Not found in the pages read.
- **Long context.** 1,048,576 tokens; the overview says maximum output varies by model, and the maker README gives 131,072 tokens. [docs, models]
- **Vision.** Image, video and PDF input on Muse Spark (audio is listed with a qualifier), with a separate image generator. [models]
- **Streaming.** Streaming tool-call arguments through the three protocols. [docs]

## Pricing

Per token, in two tiers that also set data terms. The standard tier lists $1.25 per million input tokens, $0.15 cached and $4.25 output on the page read (these standard figures also appear on model files). The contributor tier is far cheaper, at $0.10 input, $0.002 cached and $0.20 output, in exchange for letting Meta train on prompts and completions. Web search grounding adds $2.50 per 1,000 queries. Other models bill per unit: Muse Image $0.01 per image, Muse Voice Transcribe $0.18 per audio hour, SAM 3.1 $2.50 per 1,000 images or $0.20 per 1,000 video frames. Injected steering tokens are not billed. A press report from the July launch said new accounts received $20 in free credit; the pricing page read does not mention credit. Per-model prices are in the model files. [pricing, launch]

## Limits and data

- **Rate limits.** Per team: the standard tier allows 3,000 requests and 4,000,000 tokens a minute; the contributor tier 100 requests and 3,000,000 tokens a minute. Muse Image has its own 150 requests a minute, background submissions 600 a minute, and Muse Voice Transcribe 128 concurrent streams and 16,000 streams an hour. [pricing]
- **Regions.** A press report on the July launch (not Meta's docs) said the preview was open to U.S. developers; the docs read on 2026-10-03 name no country restriction and call Spark, Image, Voice Transcribe and SAM production-ready, but whether access is still limited by country was not verified. No regional endpoint was found. [launch, docs]
- **Retention and training.** On the standard tier Meta says prompts and completions are not used to train Meta models. On the contributor tier Meta may use them for training future models. The pages read do not state how long prompts and completions are retained, where they are stored, or whether a zero-retention option exists. [pricing]

## Notes for agents and harnesses

- **The cheap id changes the data terms.** `-contributor` models allow Meta to train on prompts and completions, so a harness that picks the cheapest id for cost sends private content under training terms; the standard id is the one without that term. [pricing]
- **Effort mapping.** Seven named levels exist for Muse Spark, `none` is rejected, and `max` is standard-tier only on 1.3, so a setting that works on the standard id can fail on the contributor id. (Maker README.)
- **Messages-format clients.** Disabling thinking returns 400, a named `tool_choice` is rejected and `stop_sequences` return 400, so a client library that sends these by default will not run unchanged. (Maker README.)
- **Different rate limits per tier.** The contributor tier allows 100 requests a minute against 3,000 on standard, so bulk jobs on the cheap tier hit the request limit first. [pricing]
- **Local alternative.** Muse Glimmer runs through vLLM, SGLang, llama.cpp or ExecuTorch rather than this API, with the Apache-2.0 weights. [models]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| docs | https://dev.meta.ai/docs | L | 2026-10-03 |
| models | https://dev.meta.ai/docs/models | L | 2026-10-03 |
| pricing | https://dev.meta.ai/docs/pricing-rate-limits | L | 2026-10-03 |
| launch | https://letsdatascience.com/news/meta-unveils-muse-spark-11-opens-developer-preview-4e60d164 | A | 2026-10-03 |
