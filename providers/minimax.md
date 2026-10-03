---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: first-party lab API
sources:
  - https://platform.minimax.io/docs/guides/text-generation
  - https://platform.minimax.io/docs/guides/models-intro
  - https://platform.minimax.io/docs/guides/pricing-paygo
  - https://platform.minimax.io/docs/guides/rate-limits
  - https://www.minimax.io/privacy-policy-v2.html
  - https://platform.minimax.io/protocol/privacy-policy
---

# MiniMax API

first-party lab API

MiniMax trains the MiniMax-M language models and the company's video, speech, image and music models, and sells them through the MiniMax Open Platform (platform.minimax.io, API host `api.minimax.io`). The language models are served over an Anthropic-compatible endpoint, which the company recommends, and an OpenAI-compatible one. The text-generation page asks for a Subscription Key from the console and says M Plan access is required for M3.1 Flash Preview; the maker README records that pay-as-you-go use takes a separate Open Platform key. [text, models-intro]

## Models offered

The models page names MiniMax-M3.1-Flash-Preview (multimodal, 1M context, tunable thinking depth, M Plan and MiniMax Code only), MiniMax-M3 (multimodal, 1M context), MiniMax-M2.7 and a faster MiniMax-M2.7-highspeed, with M2.5, M2.1 and M2 (and their highspeed builds) as legacy; the text-generation page gives M2.7 204,800 tokens of context. Other models are video (H3 and H3 Max), speech (speech-2.8 hd and turbo), image and music; the page says the paid music APIs close to new users from 2026-08-20 and the free music APIs are being discontinued. [models-intro, text]

| Model file | API id | Note |
| --- | --- | --- |
| [MiniMax-M3](../models/minimax/MiniMax-M3.md) | `MiniMax-M3` | 1M context; pay-as-you-go |
| [MiniMax-M3.1-Flash-Preview](../models/minimax/MiniMax-M3.1-Flash-Preview.md) | `MiniMax-M3.1-Flash-Preview` | subscription (M Plan) and MiniMax Code only |
| [MiniMax-M2.7](../models/minimax/MiniMax-M2.7.md) | `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` | 204,800 context |

Ids are mixed case. The lineage is in the [maker README](../models/minimax/README.md). [models-intro]

## API surface

- **Protocols.** Anthropic Messages at `https://api.minimax.io/anthropic` (recommended because it carries thinking blocks and interleaved thinking, per the text-generation page) and OpenAI Chat Completions at `https://api.minimax.io/v1`; both serve the same models. The maker README records an OpenAI Responses endpoint on the same host and a China endpoint, `api.minimax.cn`, named in the tool-use guide. [text]
- **Auth.** A key from the console; the text-generation page names a Subscription Key, and the maker README records a separate Open Platform key for pay-as-you-go. [text]
- **SDKs.** The documented clients are the Anthropic and OpenAI SDKs; no MiniMax SDK was found in the pages read. [text]
- **Token counting.** An endpoint exists for M3 and M3.1 Flash Preview on the Anthropic-compatible API (maker README).
- **Model ids.** Capitalised `MiniMax-` names with the version, and a `-highspeed` suffix for the faster build of M2.7. [text]

## Feature parity

First-party; the field-by-field reference is in the maker README. What the pages read establish: [text, pricing]

- **Reasoning and effort.** M3.1 Flash Preview thinks by default, returns a 400 if thinking is disabled, and takes an `effort` of `low`, `medium`, `high`, `xhigh` or `max`, defaulting to `max`. The maker README records that M3 thinks only when asked on the Anthropic and Responses endpoints, that M2.x models always think and ignore `disabled`, and that effort tunes depth for M3.1 Flash Preview only. [text]
- **Tools.** Supported on both protocols (maker README).
- **Structured output.** Not covered by the pages read.
- **Caching.** Automatic prefix caching with a 512-token minimum, plus explicit `cache_control` on the Anthropic endpoint (maker README).
- **Batch.** Not found in the pages read.
- **Priority.** A `priority` service tier costs 1.5 times standard. [pricing]
- **Long context.** 1M tokens on M3 and M3.1 Flash Preview, 204,800 on M2.7, and 200k with 128k output on the legacy M2. [text, models-intro]
- **Vision.** The models page calls M3 and M3.1 Flash Preview multimodal, and the text-generation page lists text, image and video input for M3.1 Flash Preview; the maker README records no image input on M2.x and no audio input. [models-intro, text]
- **Streaming.** Supported on both protocols (maker README).
- **Ignored fields.** On the Anthropic endpoint `top_k`, `stop_sequences`, `mcp_servers`, `context_management` and `container`; on the OpenAI endpoint the penalties and `logit_bias` (maker README).

## Pricing

Per token on pay-as-you-go with separate rates by model and context band: M3 lists $0.30 per million input tokens up to 512k and $0.60 above, with output from $1.20 to $2.40 and cache reads from $0.06 to $0.12, all shown after a "Permanent 50% off" discount; M2.7, M2.5 and M2.1 list $0.30 input. The priority tier multiplies rates by 1.5. Other services bill separately: web search at $0.01 per request, speech recognition at $0.38 per hour, text-to-speech from $60 to $100 per million characters, image generation per image and video from $0.08 to $0.13 per second. M3.1 Flash Preview has no pay-as-you-go price. Per-model prices are in the model files. [pricing, models-intro]

## Limits and data

- **Rate limits.** Requests and tokens per minute (input and output combined). On the page: MiniMax-M3 at 200 requests and 10 million tokens a minute; M2.7, M2.5, M2.1 and M2 (and highspeed builds) at 500 requests and 20 million tokens; speech models at 20 to 60 requests a minute, video from 20 to 300. The page offers a business-team email for higher limits. [limits]
- **Regions.** The international host `api.minimax.io`; the maker README records a China host, `api.minimax.cn`. No regional processing options were found. [text]
- **Retention and training.** The MiniMax API Privacy Policy (effective 2026-03-30, read in a browser because it renders by script) names Nanonoble Pte. Ltd. in Singapore as controller and says the personal data it covers is stored in a US data centre. It sets no fixed retention period (data is kept as long as needed or permitted by law) and says personal data is not used for training to profile or target consumers; it does not say whether API inputs and outputs are used to train models. No zero-data-retention option was found. [privacy, api-privacy]

## Notes for agents and harnesses

- **Anthropic endpoint for thinking.** MiniMax recommends it because it returns thinking blocks and interleaved thinking, and the full history, thinking included, must be kept across tool turns (maker README). [text]
- **Thinking switches differ by model.** `disabled` is an error on M3.1 Flash Preview, is ignored on M2.x and turns thinking off on M3; a harness that sends one setting to all three gets three behaviours. (Maker README.)
- **Effort.** Only M3.1 Flash Preview takes an effort level (five levels, `max` by default; the maker README records that `none` is rejected), and it is not on the pay-as-you-go API. [text]
- **Token limits include thinking.** A small `max_tokens` can end a reply with no text (maker README).
- **Plan keys differ.** The maker README records that a Subscription Key does not work as an Open Platform key, so a deployment that uses both plan-only and pay-as-you-go models holds two keys.
- **Training use of API content is unstated.** The API privacy policy covers personal data and gives no rule for training on prompts and outputs, and no zero-retention option was found. [api-privacy]
- **Rate limits are per model.** M3 has a much lower request limit than M2.x, so a fallback from M3 to M2.7 changes both quotas. [limits]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| text | https://platform.minimax.io/docs/guides/text-generation | L | 2026-10-03 |
| models-intro | https://platform.minimax.io/docs/guides/models-intro | L | 2026-10-03 |
| pricing | https://platform.minimax.io/docs/guides/pricing-paygo | L | 2026-10-03 |
| limits | https://platform.minimax.io/docs/guides/rate-limits | L | 2026-10-03 |
| privacy | https://www.minimax.io/privacy-policy-v2.html | L | 2026-10-03 |
| api-privacy | https://platform.minimax.io/protocol/privacy-policy | L | 2026-10-03 |
