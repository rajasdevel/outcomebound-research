---
last_checked: 2026-10-04
volatility: MONITOR (lineage, guides and API behaviour change at each release)
sources:
  - https://typesafe.ai/blog/introducing-system-one-models-and-jev
  - https://docs.typesafe.ai/concepts/system-one
  - https://docs.typesafe.ai/models
  - https://docs.typesafe.ai/api
  - https://docs.typesafe.ai/primitives
  - https://docs.typesafe.ai/concepts/how-to-build-with-system-one
  - https://docs.typesafe.ai/model-jaggedness/jev-1.13
  - https://docs.typesafe.ai/confidence
  - https://docs.typesafe.ai/llms.txt
  - https://docs.typesafe.ai/legal
  - https://typesafe.ai/legal/mca
  - https://typesafe.ai/legal/privacy-policy
  - https://typesafe.ai/legal/data-processing
  - https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook
  - https://evals.typesafe.ai/
  - https://status.typesafe.ai
  - https://www.latent.space/p/jev
  - https://typesafe.ai/blog/jev-1-14
  - https://docs.typesafe.ai/images.md
---

# TypeSafe AI

TypeSafe AI makes System One models: models that return typed decisions (a choice, a probability or
a score) about supplied text, not generated text; since 1.14 a preview Box type also returns a
bounding box in a supplied image [as-of 2026-10-27] [ts-jev114]. It names the class after the fast, intuitive
"System 1" of Kahneman's *Thinking, Fast and Slow* [ts-system-one]. Its first public model, Jev, was
announced in early access on 2026-09-15 by its founder and CEO, Diogo Almeida [ts-announcement]. What
decision models are, how they compare and how to use them is in
[../../practices/decision-models.md](../../practices/decision-models.md).

## Models and lineage

| Model | Released | Notes |
| --- | --- | --- |
| Jev 1.14 (`jev-1.14.0`) [as-of 2026-10-27] | 2026-10-14 | Behind both aliases; adds the preview Box type; [its file](jev-1.14.0.md) [ts-models-oct27] [ts-jev114] |
| Jev 1.13 (`jev-1.13.0`) | 2026-09-15, early access | The only model on the Models page on 2026-10-04, and still listed on 2026-10-27; [its file](jev-1.13.0.md) [ts-models] [ts-models-oct27] |

The cookbooks set `jev-1.12`, which TypeSafe does not list or describe [ts-extraction].
No smaller or larger Jev is documented. **[as-of 2026-10-27]** The aliases `jev-latest` (the most
recent stable release and the SDK default) and `jev-preview` both point to `jev-1.14.0`. The release of
2026-10-14 arrived as `jev-preview`, and the post announced that `jev-latest` would follow a week
later; both aliases pointed to `jev-1.14.0` when the Models page was read on 2026-10-27
[ts-models-oct27] [ts-jev114]. In an
interview TypeSafe's CEO said that new models will ship faster than people think and that long-term
support is not promised, though 1.13.0 might get it for a time [latent-space] (A). No model changelog
or deprecation policy is published; the changelogs on the docs site are for the SDKs only [ts-llms].
**[as-of 2026-10-27]** The 1.14 release post says TypeSafe intends to give 60 days' warning before
`jev-1.13.0` is formally deprecated and 30 days before `jev-1.14.0`, and to publish a deprecation
policy before those deadlines [ts-jev114].

## API surface

- **Endpoint.** `POST https://api.typesafe.ai/v1/systemone` with a bearer API key; `GET /v1/models`
  lists the aliases, and versioned ids are accepted even when not listed. The request shape is
  TypeSafe's own (`state`, `model`, `questions`); TypeSafe documents no OpenAI-compatible endpoint
  [ts-api] [ts-models].
- **SDKs.** Python (`typesafe-sdk`) and JavaScript/TypeScript (`@typesafe-ai/sdk`). Their retry
  timeouts differ: in JavaScript the timeout applies to each attempt with no total budget; in Python
  the 30 s timeout is a total budget for the call [ts-js-retry] [ts-py-retry].
- **Gateways.** TypeSafe documents base URLs for OpenRouter, Vercel AI Gateway and Pydantic AI Gateway
  [ts-gateways]. The provider page is [../../providers/typesafe.md](../../providers/typesafe.md).
- **No batch-job API.** "Batching" in the docs means many questions over one state in one request
  [ts-primitives].
- **No customer fine-tuning.** The docs say Jev is not fine-tuned or LoRA-adapted with customer data
  and the same weights serve every account; a customer shapes answers per request through `state`,
  `instructions` and `criteria` [ts-models].

## Prompting guides

TypeSafe's guidance is in its docs, not in one guide. Each page below was read on 2026-10-04 (L):

- **Primitives** and the Choice, Noul, Score and advanced pages: what each question type returns and
  how to write questions, options and levels [ts-primitives].
- **How to build with System One**: decomposition into one-second judgements, thresholds tested
  against your own data, and three bands (act, confirm or review, do not act) [ts-build].
- **State**: what to put in, how to name fields, and why unrelated content lowers accuracy.
- **Confidence**: the exact formulas, and that confidence describes an answer, not whether it is
  correct [ts-confidence].
- **Jaggedness, per version**: the known weaknesses of `jev-1.13` [ts-jagged].
- **Cookbooks and patterns**: speculative fan-out, confidence-gated routing, composite scoring,
  intent routing, reranking, extraction over pre-parsed candidates, guardrails, cascades to a
  reasoning model, and others [ts-llms].

The detailed advice, in our words, is in [jev-1.13.0.md](jev-1.13.0.md#how-to-instruct-it).

## System-card practice

TypeSafe publishes no system or model card, and by policy no public-benchmark scores; it says it will
run one-off evaluations at product updates instead [ts-announcement]. It publishes a per-version page
of weaknesses (the jaggedness page) and its own workflow evaluations, in which "accuracy" is agreement
with labels averaged from two frontier LLMs [ts-jagged] [typesafe-evals]. The jaggedness page is
edited in place: the review of 2026-10-02 removed a section and added one with no note of the change
(see [jev-1.13.0.md](jev-1.13.0.md#what-the-system-card-reports)), so a reading of it holds only for
its date. **[as-of 2026-10-27]** The docs index lists no weakness page for 1.14 [ts-llms-oct27].
**[as-of 2026-10-28]** The 1.14 post breaks with the no-scores policy in part: its charts, marked with a
warning not to trust benchmarks, give an internal intelligence measure (60.0 for 1.14, 58.9 for 1.13)
and a calibration error (1.6 and 1.8) against open-weight decision models, and the post calls the
measure a best guess that is likely biased towards TypeSafe's models [ts-jev114-charts].

## Family-wide behaviour

- Text input by default; English works best [ts-models]. **[as-of 2026-10-27]** Images (PNG or JPEG)
  are accepted by 1.13 and 1.14 as a preview behind the header `TypeSafe-Danger-Zone-Images: true`,
  and a long-context option behind `TypeSafe-Danger-Zone-Long-Context: true` raises both limits to
  262k tokens; TypeSafe calls neither ready for production [ts-images] [ts-models-oct27] [ts-jev114].
  The System One concept page still said on 2026-10-28 that Jev accepts text only
  [ts-system-one-oct28], so the pages conflict.
- Questions in one request are evaluated in parallel and independently: one answer is never context
  for another [ts-primitives].
- Choice and Score answers carry a `confidence` that summarises how concentrated the distribution is;
  Noul has none. TypeSafe says calibration is measured across groups of predictions and does not
  guarantee any single answer, that thresholds depend on the domain, and it advises testing them on
  the user's own data [ts-system-one] [ts-confidence].
- **Rate limits.** On 2026-10-04 the Models page listed 100K tokens a second and 80 requests a second,
  adjusted dynamically and changeable without notice. Wayback captures show 250,000 tokens a second
  and 1,200 requests a minute on 2026-09-26, and 100K tokens and 40 requests a second on 2026-10-02
  [ts-models]. **[as-of 2026-10-27]** The page no longer gives numbers: limits are set for each
  organization, shown in the developer console and measured in tokens and requests a second, with a
  429 error above either and higher limits on custom and enterprise plans [ts-models-oct27].
- **Data.** TypeSafe documents that it does not train on customer requests and offers zero data
  retention to enterprise customers [ts-legal]. No default retention period is stated: the privacy
  policy keeps personal data as long as reasonably necessary to provide the services "or otherwise in
  support of our business or commercial purposes", the processing terms say as long as necessary for
  the purpose, and the customer agreement lets TypeSafe derive telemetry from customer data "in
  perpetuity" and use data for training only with the customer's prior consent [ts-privacy] [ts-dpa]
  [ts-mca]. **[as-of 2026-10-27]** The customer agreement still carries the date 2026-09-23 and these
  terms [ts-mca-oct27]. The 1.14 post describes an opt-in that it says helps TypeSafe find issues and
  debug use cases, and repeats that queries are not used for training [ts-jev114]; its screenshot
  shows an organization-wide setting that lets TypeSafe read and analyse the organization's inputs and
  outputs to understand where the model is weak [as-of 2026-10-28] [ts-jev114-charts].
- **Availability.** The status page showed short incidents on 2026-09-21, 09-23 and 09-28 [ts-status].

## Open questions

- When `jev-1.13.0` will be retired, now that 1.14 has shipped, and what TypeSafe's promised
  deprecation policy will say [as-of 2026-10-27].
- What `jev-1.12` differed in, since the cookbooks' figures were measured on it.
- The exact context limit (64k per request in the docs; 32K on OpenRouter and Cloudflare).
- The default retention period for an account without zero data retention.

## Sources

- [ts-announcement] <https://typesafe.ai/blog/introducing-system-one-models-and-jev>, kind L, read
  2026-10-04.
- [ts-system-one] <https://docs.typesafe.ai/concepts/system-one>, kind L, read 2026-10-04.
- [ts-models] <https://docs.typesafe.ai/models>, kind L, read 2026-10-04; the rate limits of 2026-09-26
  from <https://web.archive.org/web/20260926155800id_/https://docs.typesafe.ai/models.md>, and those of
  2026-10-02 from a Wayback capture of the same page on that date (read by the first reader; the
  archive was offline at the second check).
- [ts-api] <https://docs.typesafe.ai/api>, kind L, read 2026-10-04.
- [ts-primitives] <https://docs.typesafe.ai/primitives>, kind L, read 2026-10-04.
- [ts-build] <https://docs.typesafe.ai/concepts/how-to-build-with-system-one>, kind L, read 2026-10-04.
- [ts-confidence] <https://docs.typesafe.ai/confidence>, kind L, read 2026-10-04.
- [ts-jagged] <https://docs.typesafe.ai/model-jaggedness/jev-1.13>, kind L, read 2026-10-04.
- [ts-llms] <https://docs.typesafe.ai/llms.txt>, kind L, read 2026-10-04.
- [ts-gateways] <https://docs.typesafe.ai/sdk/python/usage>, kind L, read 2026-10-04.
- [ts-js-retry] <https://docs.typesafe.ai/sdk/javascript/api/interfaces/RetryPolicy> and
  <https://docs.typesafe.ai/sdk/javascript/api/interfaces/RequestOptions>, kind L, read 2026-10-04.
- [ts-extraction] <https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook>, kind L,
  read 2026-10-04.
- [ts-py-retry] <https://docs.typesafe.ai/sdk/python/api/retries>, kind L, read 2026-10-04.
- [ts-legal] <https://docs.typesafe.ai/legal>, kind L, read 2026-10-04.
- [ts-mca] <https://typesafe.ai/legal/mca>, last updated 2026-09-23, kind L, read 2026-10-04.
- [ts-privacy] <https://typesafe.ai/legal/privacy-policy>, last updated 2025-11-19, kind L, read
  2026-10-04.
- [ts-dpa] <https://typesafe.ai/legal/data-processing>, last updated 2026-04-24, kind L, read
  2026-10-04.
- [typesafe-evals] <https://evals.typesafe.ai/>, kind L, read 2026-10-04.
- [ts-status] <https://status.typesafe.ai>, kind L, read 2026-10-04.
- [latent-space] <https://www.latent.space/p/jev>, 2026-09-21, kind A, read 2026-10-04.
- [ts-models-oct27] <https://docs.typesafe.ai/models>, kind L, read 2026-10-27.
- [ts-jev114] <https://typesafe.ai/blog/jev-1-14>, release post for Jev 1.14 dated 2026-10-14, kind
  L, read 2026-10-27.
- [ts-images] <https://docs.typesafe.ai/images.md>, kind L, read 2026-10-27.
- [ts-system-one-oct28] <https://docs.typesafe.ai/concepts/system-one>, kind L, read 2026-10-28.
- [ts-mca-oct27] <https://typesafe.ai/legal/mca>, last updated 2026-09-23, kind L, read 2026-10-27.
- [ts-llms-oct27] <https://docs.typesafe.ai/llms.txt>, kind L, read 2026-10-27.
- [ts-jev114-charts] <https://typesafe.ai/blog/jev-1-14>, the charts and the settings screenshot in the
  release post, kind L, images read 2026-10-28.
