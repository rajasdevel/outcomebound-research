---
last_checked: 2026-10-04
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: first-party lab API
sources:
  - https://docs.typesafe.ai/models
  - https://docs.typesafe.ai/api
  - https://docs.typesafe.ai/sdk/python/usage
  - https://docs.typesafe.ai/sdk/javascript/api/interfaces/RequestOptions
  - https://docs.typesafe.ai/sdk/javascript/api/interfaces/RetryPolicy
  - https://docs.typesafe.ai/sdk/python/api/retries
  - https://docs.typesafe.ai/legal
  - https://typesafe.ai/legal/mca
  - https://status.typesafe.ai
  - https://typesafe.ai/blog/introducing-system-one-models-and-jev
  - https://openrouter.ai/typesafe/jev-1.13
  - https://community.vercel.com/t/typesafe-ai-jev-requests-shed-with-429-and-providerattemptcount-0-per-team-throttling/49779
  - https://typesafe.ai/blog/jev-1-14
  - https://docs.typesafe.ai/images.md
---

# TypeSafe API

first-party lab API

TypeSafe AI's own API serves its System One decision model, Jev. A request sends a text state and
typed questions and gets back typed answers with probabilities; there is no chat or completion
endpoint. The maker folder is [../models/typesafe/README.md](../models/typesafe/README.md), and the
category is described in [../practices/decision-models.md](../practices/decision-models.md). [models, api]

## Models offered

| Model | File |
| --- | --- |
| Jev 1.14 (`jev-1.14.0`, aliases `jev-latest` and `jev-preview`) [as-of 2026-10-27] | [../models/typesafe/jev-1.14.0.md](../models/typesafe/jev-1.14.0.md) |
| Jev 1.13 (`jev-1.13.0`; behind no alias on 2026-10-27) | [../models/typesafe/jev-1.13.0.md](../models/typesafe/jev-1.13.0.md) |

[models] [models-oct27] [jev114]. TypeSafe intends to give 60 days' warning before `jev-1.13.0` is
formally deprecated and 30 days before `jev-1.14.0`, and to publish a deprecation policy first
[as-of 2026-10-27] [jev114].

## API surface

- **Protocol.** TypeSafe's own: `POST https://api.typesafe.ai/v1/systemone` with `state`, `model` and
  a map of `questions` (types `choice`, `score`, `noul`); `GET /v1/models` lists the aliases. TypeSafe
  documents no OpenAI- or Anthropic-compatible endpoint. [api, models]
- **Auth.** `Authorization: Bearer <key>`; the SDKs read `TYPESAFE_API_KEY`. [api]
- **SDKs.** Python `typesafe-sdk` and JavaScript `@typesafe-ai/sdk`. The Python SDK takes a base URL,
  so the same SDK can call a gateway. [gateways]
- **Errors.** 401, 422 (validation), 429 (rate limit) and 529 (overloaded); TypeSafe advises
  exponential backoff on 429 and 529. [api]
- **Gateways.** TypeSafe documents OpenRouter (model `~typesafe/jev-latest`), Vercel AI Gateway (a
  TypeSafe-compatible API) and Pydantic AI Gateway. OpenRouter serves Jev through its own
  decisions endpoint, not chat completions. [gateways, openrouter] **[as-of 2026-10-27]** Netlify's
  AI Gateway also serves `jev-1.14.0`, with usage billed to Netlify credits. [netlify]

## Feature parity

First-party, so the full feature set. Against a generative API, much does not exist:

- **Reasoning and effort.** None.
- **Tools.** None; function choice is done by asking a Choice over the function names. [api]
- **Structured output.** Every answer is typed by design.
- **Caching.** None documented, and no cached price.
- **Batch.** No batch-job API. Many questions over one state in one request is the documented
  batching. [api]
- **Long context.** 64k tokens per request for the state plus every question, and 32k for the state
  plus the longest question; OpenRouter lists 32K. [models, openrouter] **[as-of 2026-10-27]** The
  header `TypeSafe-Danger-Zone-Long-Context: true` raises both limits to 262k tokens at the same price;
  TypeSafe says it is slower and less accurate. [models-oct27]
- **Vision, audio.** **[as-of 2026-10-27]** Images (PNG or JPEG) are accepted by 1.13 and 1.14 as a
  preview behind the header `TypeSafe-Danger-Zone-Images: true`, and 1.14 adds a preview Box question;
  TypeSafe calls neither ready for production. The System One concept page still says text only. No
  audio. [images, jev114, system-one-oct28]
- **Streaming.** Not found in the pages read.

## Pricing

Per input token only; output tokens are reported but free. No pricing page exists (the docs' Models
page holds the price), no free tier is documented, and no per-question fee or minimum was found. The
customer agreement describes prepaid credits that expire after 12 months or at the end of the term,
whichever comes first, and promotional credits at TypeSafe's discretion. The price is on the card. [models, mca]

## Limits and data

- **Rate limits.** 100K tokens a second and 80 requests a second on 2026-10-04, "adjusting
  dynamically" and changeable without notice; higher limits on custom plans. Wayback captures show other
  figures on 2026-09-26 and 2026-10-02 (see the maker README). [models] **[as-of 2026-10-27]** The page
  no longer gives numbers: limits are set for each organization and shown in the developer console,
  and a request over either limit gets a 429. [models-oct27]
- **Through gateways.** From 2026-09-26, some Vercel AI Gateway teams got 429 errors with no provider
  attempt; Vercel staff said access to Jev may be limited for some accounts to protect service
  reliability. [vercel-429] (A)
- **Availability.** Short incidents on 2026-09-21, 09-23 and 09-28 on the status page. [status]
- **Training and retention.** No training on customer requests is documented; zero data retention is
  offered to enterprise customers. No default retention period is stated, and the customer agreement
  lets TypeSafe derive telemetry from customer data in perpetuity. [legal, mca] **[as-of 2026-10-27]**
  The agreement still carries the date 2026-09-23 and these terms. [mca-oct27]
- **Regions.** The announcement says the service is based on the US West Coast; no region choice is
  documented. [announcement]

## Notes for agents and harnesses

- A Jev answer is a probability, not a verdict. TypeSafe advises setting thresholds from the user's
  own data and pinning a versioned id once they are tuned, because the aliases move when a release
  ships; on 2026-10-27 both aliases had moved to `jev-1.14.0`. [models, models-oct27]
- The JavaScript SDK's timeout is per attempt, with 2 retries by default and no total budget, so the
  worst case is several timeouts plus backoff; the SDK accepts an `AbortSignal`, and only the
  application's own deadline bounds the total wait. The Python SDK's 30 s timeout is a total budget
  for the call. [js-retry, py-retry]
- Jev is not a coding-agent model and cannot sit behind a harness's chat endpoint.

## Sources

- [models] <https://docs.typesafe.ai/models>, read 2026-10-04.
- [api] <https://docs.typesafe.ai/api>, read 2026-10-04.
- [gateways] <https://docs.typesafe.ai/sdk/python/usage>, read 2026-10-04.
- [js-retry] <https://docs.typesafe.ai/sdk/javascript/api/interfaces/RetryPolicy> and
  <https://docs.typesafe.ai/sdk/javascript/api/interfaces/RequestOptions>, read 2026-10-04.
- [py-retry] <https://docs.typesafe.ai/sdk/python/api/retries>, read 2026-10-04.
- [legal] <https://docs.typesafe.ai/legal>, read 2026-10-04.
- [mca] <https://typesafe.ai/legal/mca>, last updated 2026-09-23, read 2026-10-04.
- [status] <https://status.typesafe.ai>, read 2026-10-04.
- [announcement] <https://typesafe.ai/blog/introducing-system-one-models-and-jev>, read 2026-10-04.
- [openrouter] <https://openrouter.ai/typesafe/jev-1.13>, read 2026-10-04.
- [vercel-429] <https://community.vercel.com/t/typesafe-ai-jev-requests-shed-with-429-and-providerattemptcount-0-per-team-throttling/49779>,
  forum thread opened 2026-09-26, read 2026-10-04.
- [models-oct27] <https://docs.typesafe.ai/models>, read 2026-10-27.
- [jev114] <https://typesafe.ai/blog/jev-1-14>, release post for Jev 1.14 dated 2026-10-14, read
  2026-10-27.
- [images] <https://docs.typesafe.ai/images.md>, read 2026-10-27.
- [system-one-oct28] <https://docs.typesafe.ai/concepts/system-one>, read 2026-10-28.
- [mca-oct27] <https://typesafe.ai/legal/mca>, last updated 2026-09-23, read 2026-10-27.
- [netlify] <https://netlify.com/changelog/typesafe-jev-1-14-0-ai-gateway>, page updated 2026-10-27,
  read 2026-10-28.
