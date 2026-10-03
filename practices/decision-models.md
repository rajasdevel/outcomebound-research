---
last_checked: 2026-10-04
volatility: VOLATILE (products, prices, limits, versions and vendor benchmarks change weekly in a category weeks old) / STABLE (calibration, the division of work between model and code, and the evaluation method)
sources:
  - https://docs.typesafe.ai/concepts/system-one
  - https://docs.typesafe.ai/primitives
  - https://docs.typesafe.ai/confidence
  - https://docs.typesafe.ai/models
  - https://docs.typesafe.ai/model-jaggedness/jev-1.13
  - https://docs.typesafe.ai/concepts/how-to-build-with-system-one
  - https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook
  - https://typesafe.ai/blog/introducing-system-one-models-and-jev
  - https://www.latent.space/p/jev
  - https://simonwillison.net/2026/sep/21/jev/
  - https://arcturus-labs.com/blog/2026/09/21/will-openai-eat-jevs-lunch/
  - https://www.entagl.com/blog/typesafe-jev-benchmark-ai-decision-models
  - https://www.distillabs.ai/blog/jev-or-a-fine-tuned-small-model-we-built-a-pipeline-with-both-to-see-the-real-difference/
  - https://www.alexmolas.com/2026/09/23/jev-cant-be-calibrated.html
  - https://arxiv.org/abs/2609.26758
  - https://kantahayashiai.github.io/posts/jev-does-not-play-dice/
  - https://vercel.com/blog/ai-gateway-jev-model-launch
  - https://www.nobodywho.ai/posts/jev-in-25-lines/
  - https://benchmarkheaven.com/jev-models
  - https://github.com/browser-use/jev-ultrafast/blob/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/docs/performance.md
  - https://github.com/jaredpalmer/kev/blob/84847f0a883d900f7de5b7a57eaa341ca7f9a6b4/docs/releases/kev-1.0.md
  - https://github.com/TianyuCodings/NanoJev/blob/76fdfc9ecdca45a9bcef17991a07d3041a87685a/docs/MODEL_EDGE_RESULTS.md
  - https://github.com/dabit3/jev-experiments/tree/c469e5bfdc73eb3e1999bba2569e66b579a970fd/agent-assist
  - https://github.com/dzhng/jevgrep/blob/703aba1a36a3b854be405244ea748f607cd630c0/README.md
  - https://blog.cloudflare.com/clef-decision-models/
  - https://developers.cloudflare.com/workers-ai/models/clef/
  - https://github.com/strands-labs/strands-decider
  - https://community.openai.com/t/devday-2026-announcements-and-developer-resources/1402006
  - https://cookbook.openai.com/examples/using_logprobs
---

# Decision models (System One models)

Re-check when a decision model ships or changes version, a major provider's decision API leaves
preview, or an independent benchmark of the class is published; in any case by 2026-10-18 for
products, prices and limits, and by 2027-04-01 for the rest.

A decision model reads supplied text and answers a typed question with probabilities: which of these
options, how far along this scale, how likely is this yes/no statement. It writes no text. TypeSafe
AI named the class "System One models" when it announced Jev on 2026-09-15 [chk-ts-announcement];
"decision models" is the neutral name that later products and writers use [chk-willison]
[chk-cloudflare-clef]. This page covers what the class is, when it fits, how far its probabilities can
be trusted, the patterns that hold up in published builds, the evidence for and against, who offers
one, and forecasts. It is for anyone who designs software that classifies, routes, ranks or gates
with a model. Jev's request-writing guidance and known weaknesses are in
[../models/typesafe/jev-1.13.0.md](../models/typesafe/jev-1.13.0.md). Rules for model judges, which
overlap, are in [llm-as-judge.md](llm-as-judge.md); evaluation method is in
[agent-evals.md](agent-evals.md).

**Evidence classes**, as in [the conventions](../CONVENTIONS.md): M measured; L maker or vendor
documentation; P practitioner consensus; A anecdote or one uncontrolled report; F forecast.
**Citations.** Bracketed `[chk-…]` ids are pages read on 2026-10-04, listed under Sources. The class
is three weeks old. Most numbers come from vendors measuring their own product or a competitor's; this
page says so at each one. A repository's star count measures attention, not use or quality.

## Key findings

**DM1. A decision model returns a typed answer with a probability, not text.** Jev's three question
types are Choice (one of up to 255 supplied options, a probability for each and a confidence), Score
(a probability over 2 to 10 described levels and their expected value) and Noul (the probability that
a statement is true) [chk-ts-primitives]. TypeSafe says the models are trained so that probabilities
reflect uncertainty, and that all probabilities come out at once rather than token by token
[chk-ts-system-one] [chk-ts-announcement]. Cloudflare's Clef, AWS's Strands Decider and the open Kev
family copy the three types and the `/v1/systemone` request shape [chk-cloudflare-clef]
[chk-strands] [chk-kev-release]. L.

**DM2. The documented split is: the model judges language, code does everything else.** TypeSafe's
own guidance keeps arithmetic, counting, date comparison and control flow in code, and splits any
judgement that needs reasoning into one-second questions combined in code [chk-ts-build]
[chk-ts-jagged]. The three builds cited here follow the split: business eligibility computed in code
with the model choosing a reply macro [chk-agent-assist]; game timing projected in code with the model
choosing a controller macro [chk-mario]; a browser agent that offers the model only an indexed list of
actions legal now and rechecks page freshness before acting [chk-ultrafast]. L for the guidance; A
for each build.

**DM3. Confidence is not correctness, and calibration belongs to the user's data.** TypeSafe says calibration
is measured across groups of predictions and does not guarantee any single answer, and it advises testing
thresholds on the user's own data [chk-ts-system-one] [chk-ts-confidence]. A critic argues that one fixed
output cannot be calibrated for every customer's base rates, and that the outputs are better used as
rankings and recalibrated on a few hundred labels [chk-molas]. A practitioner found Jev 83% sure on
average about a fair die it got right 19% of the time [chk-hayashi]. L, A.

**DM4. Option names steer answers more than the definitions bound to them.** On hosted Jev, binding
"yes" and "no" to each other's definition flipped 32.5% of 1,200 decisions and cut AUC from 0.815 to
0.581; neutral names (0/1, A/B) or random strings moved about 2% [chk-arxiv-typesafe]. TypeSafe's own
weakness list adds a lean toward the first Choice option [chk-ts-jagged]. M (one preprint, one point in
time), L.

**DM5. In one replay, missing state caused the regression, not the model.** In a replay of 402 real
routing decisions, Jev beat the original frontier setup at deciding what to do with a message but lost
about 7 and 14 points at choosing a specialist; the vendor traces this to state that left out who
owned the chat [chk-entagl]. A.

**DM6. A fallback is a policy to test whole, not a safety net.** In the same replay, gating Jev at
confidence 0.90 brought specialist choice back to within 1 point of the original in one workspace
(97.1% against 98.1%) and above it in the other (98.9% against 97.8%), but made one message decision
worse (93.0% to 86.7%); the vendor's explanation is that the fallback was the original system's
weakest path [chk-entagl]. On authored
cases, every answer at confidence 0.97 or more was right, and a gate at 0.85 sent 12% of cases to the
backup [chk-entagl]. A.

**DM7. Narrow semantic triage is the strong case; ordered rules and arithmetic are the weak one.**
Jev scored 200 of 200 on synthetic inbox triage and 0.75 to 0.84 on invoice pay-or-hold decisions that
need matching and arithmetic. Distil reports that every model answering in one pass stopped near
0.8 on that task (Jev 0.79, GPT-5.6 Luna without reasoning 0.81), while a fine-tuned 4B model that
writes a short reasoning step scored 0.98 and Luna with high reasoning 1.00 [chk-distil]. A (a
competing vendor's synthetic task).

**DM8. The speed claims are vendor figures on favourable tasks.** TypeSafe gives 70 to 500 ms end to
end, measured from laptops near its service, and calls its 193.6x faster, 444.6x cheaper workflow
figures likely "on the higher end of real world gains" [chk-ts-announcement]. No controlled comparison
of Jev against a generative model in a real application was found. The one controlled comparison
read held the models fixed (both arms used Jev) and changed only the code: three pairs on one browser
task cut median time 25% (9.450 s to 7.092 s), and the authors say three pairs support no strong claim
[chk-ultrafast]. L, M (small).

**DM9. The class became a market in two weeks.** OpenAI announced a Decisions API in limited preview
at DevDay on 2026-09-29 (its own page could not be read) [chk-openai-forum], a week after a
practitioner argued that OpenAI could replicate Jev quickly if it could replicate the training
[chk-arcturus]; Cloudflare released
open-weight Clef models with a Jev-compatible API on 2026-10-01 [chk-cloudflare-clef]; AWS released
Strands Decider 2B the same day [chk-strands]; open replicas such as Kev ship under Apache-2.0
[chk-kev-release]. L.

**DM10. Older tools give the same interface.** Reading the log-probabilities of class labels from a
generative API gives per-class probabilities for thresholds [chk-oai-logprobs]; rerankers sort
documents by relevance [chk-cohere-rerank]; on the arithmetic-heavy task in DM7, a fine-tuned 4B
model that writes a short reasoning step scored 0.98, within noise of reasoning LLMs (1.00 and 0.96)
[chk-distil]. Commenters on the launch thread put what the decision models add as a general
classifier that needs no training data, behind one typed interface (forum opinion). L, A.

## 1. What a decision model is (STABLE)

TypeSafe defines System One models as a class built for fast, structured decisions that software uses
directly; they do not write replies, produce code or explain their reasoning [chk-ts-system-one]. The
name borrows Kahneman's fast, intuitive System 1, and TypeSafe says its probabilities are optimised
against outcomes to reflect uncertainty [chk-ts-system-one]. Cloudflare says it uses Reinforcement
Learning for Calibrated Decisions (RLCD) as a secondary training objective for Clef, beside a Brier
loss [chk-cloudflare-clef]. L.

The interface, as Jev defines it and its followers copy it [chk-ts-primitives]:

| Type | You supply | You get back |
| --- | --- | --- |
| Choice | Up to 255 options, each with an optional description | The top option, a probability per option (summing to 1), a confidence |
| Score | 2 to 10 described levels, low to high | A probability per level, the probability-weighted score, a confidence |
| Noul | A statement or yes/no question | The probability of yes; no confidence |

Every question in a request sees the same state and is answered independently: one answer is never
context for another. A question that depends on an earlier answer needs a second request, with code
in between [chk-ts-primitives]. L.

**What it is not.** It cannot generate a value (so extraction is a Choice over candidates found by
code), does not do arithmetic or counting reliably [chk-ts-jagged], and does not reason in steps. Jev reads text only [chk-ts-models]; Clef
also reads images [chk-cloudflare-clef]. Simon Willison's summary of the trade: whatever text goes
in, what comes back is a floating-point number, so which signals drove it is hard to inspect
[chk-willison]. L, A.

**When it fits** (from the vendors' cookbooks, L, and the builds read, A): classification into a known
set; routing to code, a specialist model or a person; reranking retrieved passages; guardrails on
model input and output; choosing among actions or functions that code has already found legal;
choosing what to keep in an agent's context [chk-ts-llms] [chk-fast-compaction] [chk-jevgrep]. It
does not fit when the answer must be produced rather than chosen, when the decision rests on numbers
or ordered rules, or when the reasons must be shown.

## 2. Confidence and calibration (STABLE)

**What the numbers are.** Jev's `confidence` is a fixed function of the answer's own probabilities:
for Choice, how far the top probability is above uniform; for Score, how concentrated the
distribution is around its mode. TypeSafe calls it one reasonable summary, not the only one, and
suggests the top probability or the ratio of the top two as alternatives [chk-ts-confidence]. It says
calibration describes groups of predictions, not any single answer [chk-ts-system-one]. L.

**Calibration depends on the data, not only the model.** Calibration means that among answers given
probability p, a fraction p are right, and that fraction depends on the inputs a user sends. One fixed
output for a given input cannot be calibrated for every user's base rates at once. The remedy offered
is to recalibrate on your own labels (a few hundred, with Platt scaling) and to treat the outputs as
ranking scores until then [chk-molas]. A, consistent with the standard definition.

**What the measurements show.**

- On a hidden fair die, Jev picked "1" in all 400 trials, at a mean probability of 83% and a hit rate
  of 19% [chk-hayashi]. A (code and data public).
- On Entagl's authored cases, the 986 answers at confidence 0.97 or more were all right; answers under
  0.60 were 73.2% right [chk-entagl]. A.
- The Kev project separates a temperature fitted on the same rows from one fitted out of fold on
  disjoint groups [chk-kev-calibrate]. Its cards record a refit that improved calibration without
  improving accuracy or coverage [chk-kev-9b-card], and a refit that improved held-out sets but
  worsened the trained task families, so it was not adopted [chk-kev-08b-card]. A, for open models,
  not Jev.
- An independent benchmark gives Jev a calibration sub-score of 88.0 [chk-jevbench]. M.

**What follows** (inference from the above). A threshold is supported only by accuracy measured at
that threshold on labelled cases from the same traffic, reported beside coverage (the share of cases
acted on); TypeSafe's build guide advises plotting confidence against accuracy on the user's own data
[chk-ts-build]. A round number such as 0.9 carries no evidence of its own. The measurement holds for
one model version and one input mix.

## 3. Failure modes that change a design (MONITOR)

From TypeSafe's weakness page for `jev-1.13` [chk-ts-jagged] (L) and the measurements above:

- **Literal reading and indirection.** Negations, scope words and multi-hop questions are taken at
  face value or answered less reliably; TypeSafe advises stating the exact condition.
- **Numbers, counts and dates.** Not reliable; TypeSafe advises keeping them in code.
- **Unrelated state.** Accuracy falls as irrelevant material grows; TypeSafe advises filtering first.
- **Adversarial state.** Jev does not treat state as hostile by default; text inside the state can
  move an answer. A decision model used as a guardrail can itself be steered by what it guards.
- **Names and order.** Option names carry meaning the definitions do not override (DM4), and Choice
  can lean toward the first option. TypeSafe suggests reordering options to check an answer; the
  preprint's authors suggest neutral option names with the meaning in the definitions.
- **Consistency between questions.** Until 2026-09-29 TypeSafe warned that separately asked
  questions need not obey logical identities (0.72 for a statement and 0.47 for its negation, in its
  example). The 2026-10-02 revision removed the warning without a reason
  ([chk-ts-jagged], earlier text in a Wayback capture). The removal does not show that answers in
  one request are now consistent; TypeSafe documents them as evaluated independently
  [chk-ts-primitives].
- **Run-to-run movement.** The preprint measured at most 1.33% change between identical runs on 300
  questions [chk-arxiv-typesafe]; Distil Labs saw 2 to 3 points between identical runs of its whole
  task [chk-distil]. M, A.

## 4. Patterns that hold up (MONITOR)

Each pattern is documented by a vendor (L) or appears in a published build (A, unless marked); none is
measured across builds.

- **Offer only legal choices.** Code computes the actions or values that are valid now and hands them
  to the model as indexed options; the model chooses; code acts. The browser agent rechecks freshness
  and keeps action and request budgets in code [chk-ultrafast]; the support assistant computes refund
  eligibility before the model picks a macro [chk-agent-assist].
- **Find candidates in code, choose with the model.** For extraction, a candidate finder tuned to
  over-find supplies spans, the model picks the span with the role, code copies and normalises it, and
  a `none` option covers misses [chk-ts-extraction]. L. Since the answer is always one of the
  offered spans, a value the finder misses cannot come back (inference).
- **Ask everything about one state in one request.** Questions run in parallel, so extra questions add
  little time but do add input tokens; speculative questions can be asked too, and code ignores what it does
  not need, as TypeSafe's fan-out pattern does [chk-ts-primitives]. For 13 questions in one call against 13 calls, TypeSafe reports 11.5x
  lower cost and 9.6x less time on one page [chk-ts-primitives] and 12.2x and 10.0x in the cookbook
  that page cites [chk-ts-parallel]. L.
- **Check that the state holds what the decision needs.** The Entagl regression (DM5) came from
  state, not from the model; a list of the fields a person would need to answer each question is one
  way to catch such a gap (inference).
- **Test the fallback as a whole policy.** Only the gated system measured end to end showed the
  regression in DM6; a larger model is not guaranteed to fix the cases the small one finds hard.
- **Compare against a control, not against nothing.** In NanoJev's maze runs, a constant-probability
  control also finished every maze, because the code around the model did much of the work; the
  authors say so [chk-nanojev]. A baseline that keeps the same code and replaces the model with rules
  or a constant shows what the model adds. M (small).
- **A total deadline belongs to the application.** Jev's JavaScript SDK times out per attempt and
  retries twice by default, with no total budget, so the worst case is several timeouts plus backoff;
  only the application's own cancellation bounds the wait [chk-ts-js-retry]. The Python SDK's timeout is a
  total budget [chk-ts-py-retry]. L.
- **Pinned versions.** TypeSafe says aliases move when a release ships and advises pinning the
  versioned id once thresholds are tuned [chk-ts-models]. A labelled test set is what shows whether a
  new version still meets them (inference). L.

## 5. Speed and cost: what the figures show (VOLATILE)

- **Vendor figures.** Jev: 70 to 500 ms end to end, evaluations run from laptops on the US West Coast
  near the service [chk-ts-announcement]; most queries about 100 ms [chk-ts-build]; $0.042 per million
  input tokens and free output [chk-ts-models]. TypeSafe also says it cannot prove the price is not
  subsidised and expects it to fall [chk-ts-announcement]. L.
- **Third-party measurements.** Entagl measured a median of 329 ms (p95 436 ms) against 1,598 ms (p95
  2,765 ms) for an unnamed Gemini model at low effort, at about 25x lower cost [chk-entagl]. JevBench
  lists 0.62 s and $0.032 per 1,000 decisions [chk-jevbench]. A, M.
- **What changes application time.** The browser-agent comparison fixed the models and changed the
  orchestration: requests fell from 22 to 17 and browser protocol calls from 1,092 to 101, for 25%
  lower median time over three pairs [chk-ultrafast]. A code-search tool built on Jev reports 28.6%
  lower agent cost on 10 tasks, excluding Jev's cost; a later rerun measured 25.8% lower total cost
  including Jev, with 8 of 10 solved both times [chk-jevgrep]. M (small, self-measured).
- **Where a decision call sits.** Replacing a call that already waits on a generative model can save
  time; adding a decision call in front of something that was a local rule adds a network round trip;
  a call made while other work runs adds nothing to the wait but its answer arrives late. TypeSafe's
  "40x-200x faster" [chk-ts-announcement] compares only the first case. Inference.

## 6. Who offers decision models (VOLATILE)

Read 2026-10-04. Vendor claims are L; every benchmark below is run by the vendor named unless marked.

| Offer | Maker | Weights | Released | Notes |
| --- | --- | --- | --- | --- |
| Jev 1.13 | TypeSafe AI | closed | 2026-09-15, early access | Text only; served by TypeSafe, OpenRouter, Vercel AI Gateway, Pydantic AI Gateway; [file](../models/typesafe/jev-1.13.0.md) [chk-ts-models] |
| Decisions API | OpenAI | closed | 2026-09-29, limited preview | On a version of GPT-6 Luna; text, and images by second-hand reports [chk-arcturus]; classify, route or choose from predefined answers. Docs and price not read: OpenAI's pages returned 403 or 404 [chk-openai-forum] |
| Clef (27B) and Clef-flash (9B) | Cloudflare | open, Apache-2.0 | 2026-10-01 | LoRA and a routing head on Qwen bases; image input; 65,536 tokens; Clef $0.24 per M input on Workers AI; claims full Jev-API compatibility [chk-cloudflare-clef] [chk-cloudflare-model] |
| Strands Decider 2B | AWS (Strands Labs) | open, Apache-2.0 | 2026-10-01 | LoRA on Qwen3.5-2B-Base; local server binds to localhost with no authentication [chk-strands] |
| Kev 1.0 (0.8B, 4B, 9B, 27B) | an independent open project | open, Apache-2.0 | 2026-10-01 | LoRA adapters on Qwen3.5 bases and full weights on Qwen3.8-27B; text only, English [chk-kev-release]; llama.cpp merged a `/v1/systemone` server for Kev and other open decision models on 2026-10-02 [chk-llama-cpp] |

The Kev project's own index puts Kev-27B at 52.3 against Jev's 54.0 and its MMLU-Pro at 0.675
against Jev's 0.840; its release notes give date arithmetic as weakest below 27B [chk-kev-release]
(A, a competitor's measurement). Cloudflare reports a Clef model ahead of Jev on 8 of the 10
benchmarks it ran, with Jev ahead on When2Call and BRIGHT, and Clef ahead on 3 of TypeSafe's 4
workflows [chk-cloudflare-clef] (L, every column run by Cloudflare). JevBench, an independent
benchmark, puts Jev first on its capability score (80.0) among systems within 2x of Jev's cost and
latency, and third on its official four-axis ranking; Clef-Flash scores 70.3 [chk-jevbench] (M). A comparison of the vendor pages found no independent
replication of Cloudflare's or AWS's tables by 2026-10-03 [chk-digital-applied]. No decision-model
product from Anthropic or Google was found in searches on 2026-10-04.

**Adoption.** Vercel reports that nearly 13% of its paid AI Gateway teams used Jev within 24 hours,
more than twice any earlier launch, and adds that the next test is whether use lasts
[chk-vercel-launch] (L, a reseller's own data). TypeSafe's CEO has claimed a trillion tokens a day
[chk-latent-space] (A, his statement only). Some Vercel teams were throttled from 2026-09-26
([../providers/typesafe.md](../providers/typesafe.md)).

**Imitations of the interface.** A post reading the option logits of a 0.6B local model reproduces
the request shape in 25 lines; it calls itself a parody and reports no accuracy, latency or
calibration comparison [chk-nobodywho]. That the interface is easy to copy and the training is not is
the view of the launch-thread commenters and of [chk-arcturus] (A).

## 7. Data handling (VOLATILE)

A decision model is another external service that sees the state. TypeSafe documents no training on
customer requests and zero data retention for enterprise customers, but states no default retention
period, and its customer agreement allows telemetry derived from customer data in perpetuity
([../models/typesafe/README.md](../models/typesafe/README.md)). A practitioner demo logs an excerpt of
each input in its server route [chk-shapeshift], and the `llm` CLI plugin logs prompts and answers as
`llm` does for any model [chk-llm-typesafe]. Open-weight models can run locally; Strands Decider's local server binds to localhost and has no
authentication [chk-strands], and Kev's server is open unless `KEV_API_KEY` is set
[chk-kev-08b-card]. L, A.

## 8. Forecasts (F)

Each forecast is ours, made 2026-10-04, with a horizon of 2027-03-31 unless stated. Score each as held,
falsified or unscored at its horizon.

1. **Typed decision interfaces will be available from at least three of the large API providers**
   (OpenAI, Anthropic, Google, AWS, Microsoft) in general availability. Falsified if fewer than three
   are generally available by the horizon.
2. **Hosted decision-model versions will keep changing faster than once a quarter**, without
   long-term support for the first versions. Falsified if TypeSafe publishes a deprecation policy with
   at least six months' support for `jev-1.13.0`, or ships no new version by the horizon.
3. **An open-weight decision model under 10B total parameters will match Jev 1.13 on an independent
   benchmark** of the class: a capability score no more than 1.0 below Jev's on JevBench or a
   successor. Falsified if none does by the horizon. Horizon 2026-12-31. (On 2026-10-04 the nearest
   open models within 1 point were 12B dense or 26B with about 4B active [chk-jevbench].)
4. **Faster generative models will narrow the speed gap on decisions** enough that at least one
   independent comparison finds a generative model with logprobs or a decisions mode within 2x of
   Jev's median latency at equal accuracy. Falsified if no such comparison exists by the horizon.
5. **No decision model will be shown calibrated across users' data out of the box**: independent
   evaluations will keep finding that thresholds need local labels. Falsified by an independent study
   showing ECE under 0.05 on at least five unrelated customer-style distributions without refitting.

## What the evidence supports (inference)

- The fit is best where a person would answer in a second from text, the set of answers is known,
  and code can check whatever the answer triggers.
- Every source read keeps numbers, dates, eligibility and irreversible actions in code and leaves the
  meaning of language to the model.
- A probability from these models works as a score until it is calibrated on labels from the same
  traffic; accuracy at a threshold means little without coverage beside it.
- Option names and order moved answers in every test that varied them; designs that were not tested
  with renamed and reordered options carry that risk untested.
- Suppliers, versions and prices changed within three weeks of launch; a small decision interface and
  a labelled test set owned by the user are what survive a change of supplier.

## Limits and open questions

- Almost every number here is from a vendor measuring itself or a competitor; there is one
  independent benchmark and one preprint. Small samples throughout (3 pairs, 10 tasks, 100 invoices).
- OpenAI's Decisions API is known only from a forum summary and the press; its docs, model and price
  were not read.
- Whether Jev's separately asked questions are consistent with each other after TypeSafe removed its
  warning.
- What "calibrated" means across products: TypeSafe, Cloudflare and Kev each fit or report it
  differently.
- Whether any of this improves an end-to-end product outcome, as opposed to a decision accuracy; no
  study read measures that.
- Re-check after the next Jev version, when OpenAI's Decisions API publishes documentation, or when a
  second independent benchmark appears.

## Sources

Read 2026-10-04 unless dated otherwise. Ids in brackets are used in the text above.

TypeSafe (vendor)

- [chk-ts-announcement] TypeSafe, introducing System One models and Jev, 2026-09-15
  <https://typesafe.ai/blog/introducing-system-one-models-and-jev>.
- [chk-ts-system-one] TypeSafe, System One concepts <https://docs.typesafe.ai/concepts/system-one>.
- [chk-ts-primitives] TypeSafe, primitives <https://docs.typesafe.ai/primitives>.
- [chk-ts-confidence] TypeSafe, confidence <https://docs.typesafe.ai/confidence>.
- [chk-ts-models] TypeSafe, models <https://docs.typesafe.ai/models>.
- [chk-ts-jagged] TypeSafe, Jev 1.13 jaggedness, last reviewed 2026-10-02
  <https://docs.typesafe.ai/model-jaggedness/jev-1.13>; the earlier text in
  <https://web.archive.org/web/20260929101607id_/https://docs.typesafe.ai/model-jaggedness/jev-1.13.md>.
- [chk-ts-build] TypeSafe, how to build with System One
  <https://docs.typesafe.ai/concepts/how-to-build-with-system-one>.
- [chk-ts-extraction] TypeSafe, pre-parsed value extraction cookbook
  <https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook>.
- [chk-ts-llms] TypeSafe, docs index of cookbooks and patterns <https://docs.typesafe.ai/llms.txt>.
- [chk-ts-js-retry] TypeSafe, JavaScript SDK retry policy and request options
  <https://docs.typesafe.ai/sdk/javascript/api/interfaces/RetryPolicy> and
  <https://docs.typesafe.ai/sdk/javascript/api/interfaces/RequestOptions>.
- [chk-ts-parallel] TypeSafe, parallel questions cookbook (results section), linked from
  <https://docs.typesafe.ai/llms.txt>.
- [chk-ts-py-retry] TypeSafe, Python SDK retries <https://docs.typesafe.ai/sdk/python/api/retries>.

Other vendors

- [chk-cloudflare-clef] Cloudflare, Clef decision models, 2026-10-01
  <https://blog.cloudflare.com/clef-decision-models/>.
- [chk-cloudflare-model] Cloudflare, Workers AI Clef model page
  <https://developers.cloudflare.com/workers-ai/models/clef/>.
- [chk-strands] AWS Strands Labs, Strands Decider <https://github.com/strands-labs/strands-decider>
  and <https://huggingface.co/StrandsAgents/strands-decider-2B-hobson-v19>.
- [chk-openai-forum] OpenAI Developer Community, DevDay 2026 announcements (a community leader's
  summary), 2026-09-29
  <https://community.openai.com/t/devday-2026-announcements-and-developer-resources/1402006>; also
  The Decoder, 2026-09-29
  <https://the-decoder.com/openai-expands-codex-and-its-api-at-devday-with-security-scans-a-decisions-api-and-ultrafast/>.
- [chk-vercel-launch] Vercel, Jev is the fastest-adopted model in AI Gateway history, 2026-09-18
  <https://vercel.com/blog/ai-gateway-jev-model-launch>.
- [chk-oai-logprobs] OpenAI Cookbook, using logprobs <https://cookbook.openai.com/examples/using_logprobs>.
- [chk-cohere-rerank] Cohere, Rerank overview <https://docs.cohere.com/docs/rerank-overview>.

Measurements, practitioners and critics

- [chk-jevbench] Benchmark Heaven, JevBench v1.5.6 <https://benchmarkheaven.com/jev-models>.
- [chk-arxiv-typesafe] Sun, Xu, Shi and Yang, Type-Safe Is Not Error-Free, preprint, v2 2026-09-23
  <https://arxiv.org/abs/2609.26758>.
- [chk-entagl] Entagl, TypeSafe Jev vs Gemini on 1,759 decisions, 2026-09-23
  <https://www.entagl.com/blog/typesafe-jev-benchmark-ai-decision-models> (read through a reader proxy;
  the page returns 403 to direct fetches).
- [chk-distil] Distil Labs, Jev or a fine-tuned small model, 2026-09-22
  <https://www.distillabs.ai/blog/jev-or-a-fine-tuned-small-model-we-built-a-pipeline-with-both-to-see-the-real-difference/>.
- [chk-molas] Alex Molas, Jev can't be calibrated, 2026-09-23
  <https://www.alexmolas.com/2026/09/23/jev-cant-be-calibrated.html>.
- [chk-hayashi] Kanta Hayashi, Jev does not play dice, 2026-09-19
  <https://kantahayashiai.github.io/posts/jev-does-not-play-dice/>.
- [chk-willison] Simon Willison, Jev introduces a new shape of LLM, 2026-09-21
  <https://simonwillison.net/2026/sep/21/jev/>.
- [chk-latent-space] Latent Space, interview with TypeSafe's CEO, 2026-09-21 <https://www.latent.space/p/jev>.
- [chk-arcturus] John Berryman, Will OpenAI eat Jev's lunch?, 2026-09-21, with a later addendum
  <https://arcturus-labs.com/blog/2026/09/21/will-openai-eat-jevs-lunch/>.
- [chk-nobodywho] NobodyWho, Jev in 25 lines of Python, 2026-09-22
  <https://www.nobodywho.ai/posts/jev-in-25-lines/>.
- [chk-digital-applied] Digital Applied, open decision models compared, 2026-10-03
  <https://www.digitalapplied.com/blog/open-decision-models-compared-clef-decider-jev>.

Repositories, at the commits read

- [chk-ultrafast] browser-use/jev-ultrafast, performance report
  <https://github.com/browser-use/jev-ultrafast/blob/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/docs/performance.md>,
  README <https://github.com/browser-use/jev-ultrafast/blob/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/README.md>
  and agent loop <https://github.com/browser-use/jev-ultrafast/blob/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/jev_ultrafast/agent.py>.
- [chk-agent-assist] dabit3/jev-experiments, agent-assist
  <https://github.com/dabit3/jev-experiments/tree/c469e5bfdc73eb3e1999bba2569e66b579a970fd/agent-assist>.
- [chk-mario] fhshaik/typesafe-mario
  <https://github.com/fhshaik/typesafe-mario/tree/ca22449ed187118d19326d1f54b01b6636578aa4>.
- [chk-fast-compaction] tamaratran/fast-jev-compaction
  <https://github.com/tamaratran/fast-jev-compaction/tree/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0>.
- [chk-jevgrep] dzhng/jevgrep
  <https://github.com/dzhng/jevgrep/blob/703aba1a36a3b854be405244ea748f607cd630c0/README.md>.
- [chk-nanojev] TianyuCodings/NanoJev, model-edge results
  <https://github.com/TianyuCodings/NanoJev/blob/76fdfc9ecdca45a9bcef17991a07d3041a87685a/docs/MODEL_EDGE_RESULTS.md>.
- [chk-kev-release] jaredpalmer/kev, Kev 1.0 release notes and model cards
  <https://github.com/jaredpalmer/kev/blob/84847f0a883d900f7de5b7a57eaa341ca7f9a6b4/docs/releases/kev-1.0.md>.
- [chk-kev-9b-card] jaredpalmer/kev, Kev-9B model card at the pinned commit
  <https://github.com/jaredpalmer/kev/blob/58d94380d4441d2d9fbb7e5e6d30d9a5b93578ae/docs/model-cards/kev-9b.md>.
- [chk-kev-08b-card] jaredpalmer/kev, Kev-0.8B model card
  <https://github.com/jaredpalmer/kev/blob/84847f0a883d900f7de5b7a57eaa341ca7f9a6b4/docs/model-cards/kev-0.8b.md>.
- [chk-llama-cpp] ggml-org/llama.cpp, pull request 29818, merged 2026-10-02
  <https://github.com/ggml-org/llama.cpp/pull/29818>.
- [chk-kev-calibrate] jaredpalmer/kev, calibration report
  <https://github.com/jaredpalmer/kev/blob/58d94380d4441d2d9fbb7e5e6d30d9a5b93578ae/kev/calibrate.py>.
- [chk-shapeshift] anishfn/shapeshift, intent route
  <https://github.com/anishfn/shapeshift/blob/5e24166dcbde6e794f0bd5b1b4bd395aaee5fc19/src/app/api/intent/route.ts>.
- [chk-llm-typesafe] simonw/llm-typesafe
  <https://github.com/simonw/llm-typesafe/tree/225932cfde461ee6e38ae2b612040c50c086db8c>.
