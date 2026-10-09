---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: first-party lab API
sources:
  - https://ai.google.dev/gemini-api/docs/models
  - https://ai.google.dev/gemini-api/docs/openai
  - https://ai.google.dev/gemini-api/docs/rate-limits
  - https://ai.google.dev/gemini-api/terms
  - https://ai.google.dev/gemini-api/docs/available-regions
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/docs/thinking
  - https://ai.google.dev/gemini-api/docs/structured-output
  - https://ai.google.dev/gemini-api/docs/libraries
  - https://ai.google.dev/gemini-api/docs/changelog
  - https://ai.google.dev/gemini-api/docs/latest-model
  - https://ai.google.dev/gemini-api/docs/models/gemini-3.5-live-translate-preview
  - https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe
  - https://ai.google.dev/gemini-api/docs/live-api/live-translate
  - https://ai.google.dev/gemini-api/docs/live-api/live-transcribe
  - https://ai.google.dev/gemini-api/docs/deprecations
---

# Google Gemini API and AI Studio

first-party lab API

Google DeepMind's models are sold to developers through the Gemini API (the Gemini Developer API, at ai.google.dev) and tried in a browser in Google AI Studio, both on one API key and one billing model. A second route to the same models, for customers who want Google Cloud controls, runs on Google's cloud platform (see [Google Vertex AI](google-vertex-ai.md)); this file covers the Developer API. [models, regions]

## Models offered

On 2026-10-03 the models page lists text and multimodal Gemini models, live audio models, text-to-speech models, a transcription model, image-generation models, a video model (Veo 3.1), a music model, a deep-research agent and an embeddings model. Gemma open-weight models do not appear on that page. Gemini 4 Argon is not on it either. [models]

| Model file | API id | Status on the models page |
| --- | --- | --- |
| [Gemini 3.8 Flash](../models/google/gemini-3.8-flash.md) | `gemini-3.8-flash` | stable |
| [Gemini 3.7 Flash](../models/google/gemini-3.7-flash.md) | `gemini-3.7-flash` | stable |
| [Gemini 3.5 Flash-Lite](../models/google/gemini-3.5-flash-lite.md) | `gemini-3.5-flash-lite` | stable |
| [Gemini 3.1 Flash-Lite](../models/google/gemini-3.1-flash-lite.md) | `gemini-3.1-flash-lite` | stable |
| [Gemini 3.1 Pro](../models/google/gemini-3.1-pro-preview.md) | `gemini-3.1-pro-preview` | preview |
| [Gemini 4 Argon](../models/google/gemini-4-argon.md) | none published | not on the page |

The page also lists 3.6 Flash and 3.5 Flash as stable and 3 Flash as a preview; they are older than the two generations the model files cover. The Gemma 4 files ([12B](../models/google/gemma-4-12b-it.md), [31B](../models/google/gemma-4-31b-it.md) and the other sizes) are open weights and are not served through this API according to the models page; the [maker README](../models/google/README.md) covers them. Google marks each id as stable, preview, latest (a moving alias) or experimental; the README gives the notice periods. [models]

### Dedicated speech inventory [as-of 2026-10-09]

| Model file | Selectable id | Catalogue status |
| --- | --- | --- |
| [Gemini 3.5 Live Translate](../models/google/gemini-3.5-live-translate-preview.md) | `gemini-3.5-live-translate-preview` | public preview; speech-to-speech translation |
| [Gemini 3.5 Transcribe](../models/google/gemini-3.5-transcribe.md) | `gemini-3.5-transcribe` | stable; file speech-to-text |
| [Gemini 3.5 Transcribe Live](../models/google/gemini-3.5-transcribe-live.md) | `gemini-3.5-transcribe-live` | stable; streaming speech-to-text |

The catalogue lists all three ids. These dedicated models now have full research files. No new general language model was found between the previous catalogue check and this check. Image and video coverage remains deferred: Nano Banana 2.1, Pro and 2 Lite, and Omni Flash have an explicit disposition in the [maker README](../models/google/README.md#recent-coverage-decisions-as-of-2026-10-09). The restricted 3.8 Flash Cyber variant is listed on Google's Cloud route, not this catalogue [L: models-october].

The API preview ids for 3.1 Flash Live, 3.1 Flash TTS and 2.5 Pro TTS have an earliest shutdown of 2026-11-17. The replacement ids are 3.8 Live for the Live model and either 3.8 TTS model for the speech synthesis routes. This does not retire the Cloud GA Pro TTS id [L: deprecations-october].

## API surface

- **Protocols.** Two native interfaces, generateContent and the newer Interactions API, which the [maker README](../models/google/README.md) records as storing conversation state on the server by default; the README describes both. Native endpoints sit on `generativelanguage.googleapis.com`. [openai]
- **Auth.** A Gemini API key, created in AI Studio. The OpenAI-compatible layer takes the key as the OpenAI `api_key`. [openai]
- **SDKs.** The Google GenAI SDK is the recommended client: Python `google-genai`, JavaScript and TypeScript `@google/genai`, Go `google.golang.org/genai`, Java `google-genai` and C# `Google.GenAI`. The earlier packages (`google-generativeai` for Python and others) are marked deprecated as of 2025-11-30. [libraries]
- **OpenAI-compatible endpoint.** Base URL `https://generativelanguage.googleapis.com/v1beta/openai/`. It supports chat completions with streaming, function calling, image, audio and video input, structured outputs, embeddings, a batch interface and image and video generation. Google still labels the compatibility support beta. The page maps `reasoning_effort` per model: on Gemini 3.1 Pro `minimal` and `low` both become the low thinking level, while on 3.1 Flash-Lite and 3 Flash `minimal` stays minimal; `medium` and `high` map to the same names. Its table does not list the 3.5 to 3.8 Flash models. `service_tier` selects the Flex and Priority tiers, and the `extra_body` field carries Gemini-specific settings such as thinking configuration, cached content and safety settings. [openai]
- **Model ids.** Plain lower-case ids with a dot in the version, such as `gemini-3.8-flash`; a `-preview` suffix marks preview ids. [models]

## Feature parity

This is the maker's own API, so parity means what each interface and route does. Items verified on the pages below; the README holds the Interactions details. [models, thinking, structured, openai]

- **Reasoning and effort.** `thinking_level` replaces numeric budgets. Defaults and levels on 2026-10-03: `gemini-3.8-flash` and `gemini-3.7-flash` default to medium and accept low, medium and high; `gemini-3.6-flash` and `gemini-3.5-flash` default to medium and also accept minimal; `gemini-3.5-flash-lite` defaults to minimal and accepts all four; `gemini-3.1-pro-preview` defaults to high and accepts low, medium and high. Google's migration guide for 3.8 Flash says `thinking_budget` is no longer used and is replaced by `thinking_level`, and that `minimal` returns an error on 3.8 Flash. [thinking, latest] Thought summaries are enabled with `thinking_summaries: "auto"`, thinking tokens bill with output tokens, and a thought block can carry only an opaque signature. In stateless use the full history with signatures goes back each turn. [thinking]
- **Sampling and prefill.** The changelog marks `temperature`, `top_p` and `top_k` deprecated on 2026-07-21, and the 3.8 Flash migration guide says to strip them from requests; neither page says what error a request that sets them receives. The same guide says to remove prefilled model turns, without naming an error code. It also says `candidate_count` is unsupported from Gemini 3 on. [changelog, latest]
- **Structured output.** A `response_format` with a JSON MIME type and a schema; Pydantic and Zod are supported in the SDKs. The page lists the supported types (string, number, integer, boolean, object, array, null) and properties such as `enum`, `format`, `required`, `items`, `minItems` and `maxItems`; very large or deeply nested schemas may be rejected. On Gemini 3 models structured output can be combined with search grounding, URL context, code execution, file search and function calling in one request, and streamed chunks are partial JSON. [structured]
- **Tools.** Hosted search grounding, maps grounding, code execution, URL context, file search and a preview computer-use tool, plus function calling (per the maker README).
- **Caching.** Context caching; cached input is billed at a tenth of the input price (for example $0.075 against $0.75 on 3.8 Flash), plus an hourly storage fee set per model. [pricing]
- **Batch.** A batch API at half price, with its own limits (below). [pricing, rate]
- **Long context.** Window sizes are on the model cards. Pro models above 200,000 tokens pay twice the input rate and one and a half times the output rate on the pricing page. [pricing]
- **Vision, audio, video.** Multimodal input on the lead models, and separate image, video, music, speech and transcription models. [models]
- **Streaming.** Supported on chat completions and in the native interfaces. [openai]
- **What the Cloud route changes.** The README records different image and PDF limits, fixed sampling values, Provisioned Throughput and regional endpoints on the Cloud platform, and a preview status for the Interactions API there.

### Dedicated speech controls [as-of 2026-10-09]

Live Translate uses a Live WebSocket with translation configuration instead of system instructions or tools. Its endpoint accepts only speech audio. Transcribe Live uses the same connection type for text transcript events; its ten-minute limit, VAD controls and lack of diarization or word timestamps are specific to transcription. Neither dedicated guide establishes the tool or reasoning parity of a conversational Live model [L: translate-october, transcribe-live-october, transcribe-model-october].

The full model files distinguish audio-input and text-output prices and capture missing token integers and source disagreements. The provider's general thinking and schema guidance above does not establish support for these dedicated endpoints.

## Pricing

Per token, with a free tier that exchanges data use for no charge, and a paid tier billed through a Cloud billing account. Four modes: Standard; Batch at 50 percent of the standard rate; Flex at 50 percent; Priority at 1.8 times. Context caching adds a storage fee set per model, for example $0.50 per million tokens per hour on 3.8 Flash (rising to $1.00 on 2027-01-01) and $4.50 on 3.1 Pro preview. Search grounding includes 5,000 free requests a month across Gemini 3.x models, then $14 per 1,000. Pro models charge more above 200,000 prompt tokens (on 3.1 Pro preview, 2 times the input rate and 1.5 times the output rate). Recent models carry introductory prices through 2026-12-31 that double on 2027-01-01. Per-model prices are in the model files. [pricing]

## Limits and data

- **Rate limits.** Counted in requests per minute, input tokens per minute and requests per day, per project and not per key; any one limit trips the error; daily quotas reset at midnight Pacific time. Tiers: Free (an active project), Tier 1 (active billing, $250 spend cap), Tier 2 ($100 spent and 3 days, $2,000 cap), Tier 3 ($1,000 spent and 30 days, $20,000 to $100,000 or more). Tiers 1 to 3 also have rolling 10-minute spend limits of $10, $50 and $200. Batch has 100 concurrent requests, a 2 GB input file and 20 GB storage, plus per-model enqueued-token limits. The exact per-model numbers are shown in AI Studio, not in the documentation. [rate]
- **Regions.** The regions page lists the countries and territories where the Developer API and AI Studio are offered, without a total, and points users elsewhere to the Gemini API on Google's cloud platform. It also says users must be 18 or over. It gives no regional endpoints or data-residency controls for the Developer API. [regions]
- **Retention and training.** On the free tier Google may use content to improve its products and humans may review it; on paid services it does not, and processes data under its Data Processing Addendum, keeping data only for a limited time to detect violations of its prohibited-use policy. Search and Maps grounding keep data 30 days. Users in the EEA, UK and Switzerland must use paid services when they make an API client available to others. The terms page describes no zero-data-retention option. [terms]

## Notes for agents and harnesses

- **Sampling and prefill.** `temperature`, `top_p` and `top_k` are deprecated, and Google's migration guide says to remove them and any prefilled model turn, so prefill-style requests written for other APIs need rework; the error a request receives is not stated. [changelog, latest]
- **Effort mapping.** The native control is `thinking_level` with per-model sets; the thinking page lists no `minimal` for 3.8 and 3.7 Flash, and the migration guide says `minimal` returns an error on 3.8 Flash. Through the compatibility layer `reasoning_effort: minimal` becomes `low` on 3.1 Pro, so a request for the smallest setting there runs at low thinking. [thinking, latest, openai]
- **Mixed effort fields.** The compatibility page says `reasoning_effort` cannot be sent together with `thinking_level` or `thinking_budget`. [openai]
- **Signatures.** The thinking page calls a thought signature an encrypted form of the model's reasoning state; in stateless use every thought block must be sent back exactly as received, and in stateful use the service manages them. A client that rebuilds history by hand can lose reasoning continuity. [thinking]
- **Schema limits.** A large or deeply nested schema can be rejected; the page gives no threshold. [structured]
- **Free versus paid.** A free-tier key sends content to Google for product improvement, and the paid terms say it does not. [terms]
- **Changing shapes.** The Interactions API changed its request and response schema in 2026 (`outputs` became `steps`; announced 2026-05-06, default from 2026-05-26, the old shape removed 2026-06-08). [changelog]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| models | https://ai.google.dev/gemini-api/docs/models | L | 2026-10-03 |
| openai | https://ai.google.dev/gemini-api/docs/openai | L | 2026-10-03 |
| rate | https://ai.google.dev/gemini-api/docs/rate-limits | L | 2026-10-03 |
| terms | https://ai.google.dev/gemini-api/terms | L | 2026-10-03 |
| regions | https://ai.google.dev/gemini-api/docs/available-regions | L | 2026-10-03 |
| pricing | https://ai.google.dev/gemini-api/docs/pricing | L | 2026-10-03 |
| thinking | https://ai.google.dev/gemini-api/docs/thinking | L | 2026-10-03 |
| structured | https://ai.google.dev/gemini-api/docs/structured-output | L | 2026-10-03 |
| libraries | https://ai.google.dev/gemini-api/docs/libraries | L | 2026-10-03 |
| changelog | https://ai.google.dev/gemini-api/docs/changelog | L | 2026-10-03 |
| latest | https://ai.google.dev/gemini-api/docs/latest-model | L | 2026-10-03 |
| models-october | https://ai.google.dev/gemini-api/docs/models | L | 2026-10-09 |
| deprecations-october | https://ai.google.dev/gemini-api/docs/deprecations | L | 2026-10-09 |
| translate-october | https://ai.google.dev/gemini-api/docs/live-api/live-translate | L | 2026-10-09 |
| transcribe-live-october | https://ai.google.dev/gemini-api/docs/live-api/live-transcribe | L | 2026-10-09 |
| transcribe-model-october | https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe | L | 2026-10-09 |
