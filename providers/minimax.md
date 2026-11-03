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
  - https://platform.minimax.io/docs/faq/models (read 2026-10-31)
  - https://www.minimax.io/blog/minimax-m31f (read 2026-10-31)
  - https://platform.minimax.io/docs/api-reference/text-openai-api (read 2026-10-31)
---

# MiniMax API

first-party lab API

MiniMax trains the MiniMax-M language models and the company's video, speech, image and music models, and sells them through the MiniMax Open Platform (platform.minimax.io, API host `api.minimax.io`). The language models are served over an Anthropic-compatible endpoint, which the company recommends, and an OpenAI-compatible one. The text-generation page asks for a Subscription Key from the console; the maker README records that pay-as-you-go use takes a separate Open Platform key. [as-of 2026-10-31] M3.1 Flash, which replaced the M Plan-only M3.1 Flash Preview on 2026-10-19, is on pay-as-you-go as well as M Plan. [text-1031, launch]

## Models offered

[as-of 2026-10-31] The model list names two language models, MiniMax-M3.1-Flash (multimodal, 1M context, tunable thinking depth) and MiniMax-M3 (multimodal, 1M context). It says the M2.5 and M2.7 families closed to new users on 2026-10-19 and retire on 2026-11-18, and its table already marks M2.7, M2.5, M2.1, M2, their highspeed builds and M2-her as retired. [model-list] Other models are video (H3 and H3 Max), speech (speech-2.8 hd and turbo), image and music; the page says the paid music APIs close to new users from 2026-08-20 and the free music APIs are being discontinued. [models-intro, text]

| Model file | API id | Note |
| --- | --- | --- |
| [MiniMax-M3.1-Flash](../models/minimax/MiniMax-M3.1-Flash.md) | `MiniMax-M3.1-Flash` | 1M context; pay-as-you-go, M Plan and MiniMax Code; the retired preview id is served by this model |
| [MiniMax-M3](../models/minimax/MiniMax-M3.md) | `MiniMax-M3` | 1M context; pay-as-you-go |
| [MiniMax-M2.7](../models/minimax/MiniMax-M2.7.md) | `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` | 204,800 context; existing users only; retires 2026-11-18 |

Ids are mixed case. The lineage is in the [maker README](../models/minimax/README.md). [models-intro]

## API surface

- **Protocols.** Anthropic Messages at `https://api.minimax.io/anthropic` (recommended because it carries thinking blocks and interleaved thinking, per the text-generation page) and OpenAI Chat Completions at `https://api.minimax.io/v1`; both serve the same models. The maker README records an OpenAI Responses endpoint on the same host and a China endpoint, `api.minimax.cn`, named in the tool-use guide. [text]
- **Auth.** A key from the console; the text-generation page names a Subscription Key, and the maker README records a separate Open Platform key for pay-as-you-go. [text]
- **SDKs.** The documented clients are the Anthropic and OpenAI SDKs; no MiniMax SDK was found in the pages read. [text]
- **Token counting.** An endpoint existed for M3 and M3.1 Flash Preview on the Anthropic-compatible API on 2026-10-03 (maker README).
- **Model ids.** Capitalised `MiniMax-` names with the version, and a `-highspeed` suffix for the faster build of M2.7. [text]

## Feature parity

First-party; the field-by-field reference is in the maker README. What the pages read establish: [text, pricing]

- **Reasoning and effort.** M3.1 Flash (like the preview before it) thinks by default, returns a 400 if thinking is disabled, and takes an `effort` of `low`, `medium`, `high`, `xhigh` or `max`, defaulting to `max`. The maker README records that M3 thinks only when asked on the Anthropic and Responses endpoints, that M2.x models always think and ignore `disabled`, and that effort tunes depth for M3.1 Flash only. [text, text-1031]
- **Tools.** Supported on both protocols (maker README).
- **Structured output.** Not covered by the pages read.
- **Caching.** Automatic prefix caching with a 512-token minimum, plus explicit `cache_control` on the Anthropic endpoint (maker README).
- **Batch.** Not found in the pages read.
- **Priority.** A `priority` service tier costs 1.5 times standard. [pricing] [as-of 2026-10-31] M3.1 Flash does not support it. [openai-ref-1031]
- **Sampling.** [as-of 2026-10-31] On M3.1 Flash and M3, `temperature` and `top_p` have no effect; the models always use 1 and 0.95. [openai-ref-1031]
- **Long context.** 1M tokens on M3.1 Flash and M3 [as-of 2026-10-31], and 204,800 on the retiring M2.7. [text-1031, text]
- **Vision.** The models page calls M3 and M3.1 Flash multimodal, and the text-generation page lists text, image and video input for M3.1 Flash [as-of 2026-10-31]; the maker README records no image input on M2.x and no audio input. [models-intro, text]
- **Streaming.** Supported on both protocols (maker README).
- **Ignored fields.** On the Anthropic endpoint `top_k`, `stop_sequences`, `mcp_servers`, `context_management` and `container`; on the OpenAI endpoint the penalties and `logit_bias` (maker README).

## Pricing

Per token on pay-as-you-go with separate rates by model and context band: M3 lists $0.30 per million input tokens up to 512k and $0.60 above, with output from $1.20 to $2.40 and cache reads from $0.06 to $0.12, all shown after a "Permanent 50% off" discount. [as-of 2026-10-31] M3.1 Flash lists a flat $0.15 input, $0.60 output and $0.015 cache read, with no context band; the page no longer lists M2.7, M2.5 or M2.1. The priority tier multiplies rates by 1.5. Other services bill separately: web search at $0.01 per request, speech recognition at $0.38 per hour, text-to-speech from $60 to $100 per million characters, image generation per image and video from $0.08 to $0.13 per second. Per-model prices are in the model files. [pricing, pricing-1031, models-intro]

## Limits and data

- **Rate limits.** Requests and tokens per minute (input and output combined). [as-of 2026-10-31] On the page: MiniMax-M3.1-Flash and MiniMax-M3 at 200 requests and 10 million tokens a minute; the M2.x models are no longer listed; speech models at 20 to 60 requests a minute, video from 20 to 300. The page offers a business-team email for higher limits. [limits, limits-1031]
- **Regions.** The international host `api.minimax.io`; the maker README records a China host, `api.minimax.cn`. No regional processing options were found. [text]
- **Retention and training.** The MiniMax API Privacy Policy (effective 2026-03-30, read in a browser because it renders by script) names Nanonoble Pte. Ltd. in Singapore as controller and says the personal data it covers is stored in a US data centre. It sets no fixed retention period (data is kept as long as needed or permitted by law) and says personal data is not used for training to profile or target consumers; it does not say whether API inputs and outputs are used to train models. No zero-data-retention option was found. [privacy, api-privacy]

## Notes for agents and harnesses

- **Anthropic endpoint for thinking.** MiniMax recommends it because it returns thinking blocks and interleaved thinking, and the full history, thinking included, must be kept across tool turns (maker README). [text]
- **Thinking switches differ by model.** `disabled` is an error on M3.1 Flash, is ignored on M2.x and turns thinking off on M3; a harness that sends one setting to all three gets three behaviours. (Maker README.)
- **Effort.** Only M3.1 Flash takes an effort level (five levels, `max` by default; `none` is rejected). [as-of 2026-10-31] It is on the pay-as-you-go API as well as M Plan. [text-1031]
- **Token limits include thinking.** A small `max_tokens` can end a reply with no text (maker README).
- **Plan keys differ.** The maker README records that a Subscription Key does not work as an Open Platform key, so a deployment that uses both plan-only and pay-as-you-go models holds two keys.
- **Training use of API content is unstated.** The API privacy policy covers personal data and gives no rule for training on prompts and outputs, and no zero-retention option was found. [api-privacy]
- **M2.7 is going away.** [as-of 2026-10-31] A fallback to M2.7 stops working on 2026-11-18, and plan traffic to M2.7 already goes to M3.1 Flash, so a harness that pins M2.7 on a plan gets a different model under the same name. [model-list]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| text | https://platform.minimax.io/docs/guides/text-generation | L | 2026-10-03 |
| models-intro | https://platform.minimax.io/docs/guides/models-intro | L | 2026-10-03 |
| pricing | https://platform.minimax.io/docs/guides/pricing-paygo | L | 2026-10-03 |
| limits | https://platform.minimax.io/docs/guides/rate-limits | L | 2026-10-03 |
| privacy | https://www.minimax.io/privacy-policy-v2.html | L | 2026-10-03 |
| api-privacy | https://platform.minimax.io/protocol/privacy-policy | L | 2026-10-03 |
| text-1031 | https://platform.minimax.io/docs/guides/text-generation | L | 2026-10-31 |
| pricing-1031 | https://platform.minimax.io/docs/guides/pricing-paygo | L | 2026-10-31 |
| limits-1031 | https://platform.minimax.io/docs/guides/rate-limits | L | 2026-10-31 |
| model-list | https://platform.minimax.io/docs/faq/models | L | 2026-10-31 |
| launch | https://www.minimax.io/blog/minimax-m31f | L | 2026-10-31 |
| openai-ref-1031 | https://platform.minimax.io/docs/api-reference/text-openai-api | L | 2026-10-31 |
