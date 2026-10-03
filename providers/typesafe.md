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
| Jev 1.13 (`jev-1.13.0`, aliases `jev-latest` and `jev-preview`) | [../models/typesafe/jev-1.13.0.md](../models/typesafe/jev-1.13.0.md) |

[models]

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
  decisions endpoint, not chat completions. [gateways, openrouter]

## Feature parity

First-party, so the full feature set. Against a generative API, much does not exist:

- **Reasoning and effort.** None.
- **Tools.** None; function choice is done by asking a Choice over the function names. [api]
- **Structured output.** Every answer is typed by design.
- **Caching.** None documented, and no cached price.
- **Batch.** No batch-job API. Many questions over one state in one request is the documented
  batching. [api]
- **Long context.** 64k tokens per request for the state plus every question, and 32k for the state
  plus the longest question; OpenRouter lists 32K. [models, openrouter]
- **Vision, audio.** None; text only. [models]
- **Streaming.** Not found in the pages read.

## Pricing

Per input token only; output tokens are reported but free. No pricing page exists (the docs' Models
page holds the price), no free tier is documented, and no per-question fee or minimum was found. The
customer agreement describes prepaid credits that expire after 12 months or at the end of the term,
whichever comes first, and promotional credits at TypeSafe's discretion. The price is on the card. [models, mca]

## Limits and data

- **Rate limits.** 100K tokens a second and 80 requests a second on 2026-10-04, "adjusting
  dynamically" and changeable without notice; higher limits on custom plans. Wayback captures show other
  figures on 2026-09-26 and 2026-10-02 (see the maker README). [models]
- **Through gateways.** From 2026-09-26, some Vercel AI Gateway teams got 429 errors with no provider
  attempt; Vercel staff said access to Jev may be limited for some accounts to protect service
  reliability. [vercel-429] (A)
- **Availability.** Short incidents on 2026-09-21, 09-23 and 09-28 on the status page. [status]
- **Training and retention.** No training on customer requests is documented; zero data retention is
  offered to enterprise customers. No default retention period is stated, and the customer agreement
  lets TypeSafe derive telemetry from customer data in perpetuity. [legal, mca]
- **Regions.** The announcement says the service is based on the US West Coast; no region choice is
  documented. [announcement]

## Notes for agents and harnesses

- A Jev answer is a probability, not a verdict. TypeSafe advises setting thresholds from the user's
  own data and pinning `jev-1.13.0` once they are tuned, because the aliases move when a release
  ships. [models]
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
