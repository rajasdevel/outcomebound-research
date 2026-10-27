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
  - https://developers.openai.com/api/docs/guides/decisions
  - https://developers.openai.com/api/reference/python/resources/decisions/methods/create
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/reference/python/resources/decisions/methods/create.md
  - https://typesafe.ai/blog/jev-1-14
  - https://docs.typesafe.ai/images.md
  - https://docs.typesafe.ai/primitives/box.md
  - https://typesafe.ai/legal/mca
  - https://netlify.com/changelog/typesafe-jev-1-14-0-ai-gateway
  - https://docs.perplexity.ai/docs/decisions/quickstart
  - https://docs.perplexity.ai/docs/resources/changelog
  - https://ai-sdk.dev/docs/ai-sdk-core/decisions
  - https://pydantic.dev/docs/ai/models/decision/
  - https://pydantic.dev/docs/ai/api/models/openai_decisions/
  - https://github.com/pydantic/pydantic-ai/pull/8696
  - https://api.github.com/repos/jaredpalmer/kev/releases
  - https://github.com/jaredpalmer/kev/commit/e7ae8fd5fda9d40865d3a9de90f074feb0735985
  - https://huggingface.co/perplexity-ai/pplx-decider-v1.2
  - https://arxiv.org/html/2610.03935
  - https://arxiv.org/abs/2610.21244
  - https://arxiv.org/html/2610.06625v1
  - https://arxiv.org/abs/2610.17205
  - https://builder.aws.com/content/3KRx3G8JMf1G06ZFu2dDEdE2DLw/benchmarking-strands-decider-llm-classifiers-and-bedrock-routing-for-model-routing
  - https://vincentvandeth.nl/blog/openai-decisions-api-explained-jev-haiku
  - https://dev.classmethod.jp/en/articles/devio2026-tokyo-decision-model-report/
---

# Decision models (System One models)

Re-check when a decision model ships or changes version, a major provider's decision API leaves
preview, or an independent benchmark of the class is published; in any case by 2026-11-10 for
products, prices and limits, and by 2027-04-01 for the rest. The whole page was last verified on
2026-10-04. Claims and sections marked `[as-of 2026-10-27]` were checked again against their
sources on that date: the offers, prices and limits of §6, the data terms of §7, and the studies
and tests added to the key findings and to §2 to §5.

A decision model reads supplied text and answers a typed question with probabilities: which of these
options, how far along this scale, how likely is this yes/no statement. It writes no text. TypeSafe
AI named the class "System One models" when it announced Jev on 2026-09-15 [chk-ts-announcement];
"decision models" is the neutral name that later products and writers use [chk-willison]
[chk-cloudflare-clef]. This page covers what the class is, when it fits, how far its probabilities can
be trusted, the patterns that hold up in published builds, the evidence for and against, who offers
one, and forecasts. It is for anyone who designs software that classifies, routes, ranks or gates
with a model. Jev's request-writing guidance and known weaknesses are in
[../models/typesafe/jev-1.13.0.md](../models/typesafe/jev-1.13.0.md), and what changed in Jev 1.14 is
in [../models/typesafe/jev-1.14.0.md](../models/typesafe/jev-1.14.0.md). Rules for model judges, which
overlap, are in [llm-as-judge.md](llm-as-judge.md); evaluation method is in
[agent-evals.md](agent-evals.md); turning model labels into counts with valid intervals is in
[model-labels-for-counts.md](model-labels-for-counts.md).

**Evidence classes**, as in [the conventions](../CONVENTIONS.md): M measured; L maker or vendor
documentation; P practitioner consensus; A anecdote or one uncontrolled report; F forecast.
**Citations.** Bracketed `[chk-…]` ids are pages read on 2026-10-04, listed under Sources, unless the
Sources list gives another read date. The class was three weeks old on 2026-10-04. Until October 2026
most numbers came from vendors measuring their own product or a competitor's; this page says so at
each one. A repository's star count measures attention, not use or quality.

## Key findings

**DM1. A decision model returns a typed answer with a probability, not text.** Jev's three question
types are Choice (one of up to 255 supplied options, a probability for each and a confidence), Score
(a probability over 2 to 10 described levels and their expected value) and Noul (the probability that
a statement is true) [chk-ts-primitives]. TypeSafe says the models are trained so that probabilities
reflect uncertainty, and that all probabilities come out at once rather than token by token
[chk-ts-system-one] [chk-ts-announcement]. Cloudflare's Clef, AWS's Strands Decider and the open Kev
family copy the three types and the `/v1/systemone` request shape [chk-cloudflare-clef]
[chk-strands] [chk-kev-release]. **[as-of 2026-10-27]** Perplexity's Decisions API asks the same three
types about a `state` at `/v1/decisions` [chk-pplx-quickstart]. Jev 1.14 adds a fourth type, Box,
which returns one bounding box in an image with a confidence; TypeSafe calls it a preview that is not
ready for production [chk-ts-box] [chk-ts-jev114]. L.

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
average about a fair die it got right 19% of the time [chk-hayashi]. L, A. **[as-of 2026-10-27]** Two
independent studies found decision models better calibrated than generative models' written or token
probabilities, but calibration still varies by dataset: on one benchmark Jev's expected calibration
error (ECE) was 0.053 overall and 0.306 on 28-label emotion classification [chk-arxiv-gdm]
[chk-arxiv-polisci]. M (preprints).

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
figures likely "on the higher end of real world gains" [chk-ts-announcement]. Up to 2026-10-04 no
controlled comparison of Jev against a generative model in a real application was found. The one
controlled comparison read then held the models fixed (both arms used Jev) and changed only the code:
three pairs on one browser task cut median time 25% (9.450 s to 7.092 s), and the authors say three
pairs support no strong claim [chk-ultrafast]. **[as-of 2026-10-27]** Across seven replications of
published text-annotation studies, Jev 1.13 took 0.09 to 0.27 s a decision, against 0.75 to 1.04 s
for GPT-6 Luna with token probabilities [chk-arxiv-polisci]; a benchmark of 92k questions puts the
largest System-1 models at about a quarter of the latency of fast closed LLMs [chk-arxiv-s1arena].
On a 2-vCPU CPU micro-VM, the open Strands Decider 2B took 11 to 13 s a decision [chk-aws-routing].
L, M, A.

**DM9. The class became a market in two weeks.** OpenAI announced a Decisions API in limited preview
at DevDay on 2026-09-29 [chk-openai-forum], a week after a practitioner argued that OpenAI could
replicate Jev quickly if it could replicate the training [chk-arcturus]. The
API entered public beta on October 6 with `gpt-6-luna`, and became generally available on October 22. Its guide documents text, images and JSON, typed answers and endpoint pricing [as-of 2026-10-27] [chk-openai-decisions-oct27] [chk-openai-changelog-oct27]. Cloudflare released open-weight Clef models with a Jev-compatible API
on 2026-10-01 [chk-cloudflare-clef]; AWS released Strands Decider 2B the same day [chk-strands]; open
replicas such as Kev ship under Apache-2.0 [chk-kev-release]. **[as-of 2026-10-27]** TypeSafe released
Jev 1.14 on 2026-10-14 [chk-ts-jev114]. Perplexity launched a Decisions API in October 2026 and shipped
three model versions that month [chk-pplx-changelog]. No typed decision API from Anthropic, Google or
Microsoft was found on 2026-10-27 [chk-aisdk-decisions]. L; the practitioner forecast is A.

**DM10. Older tools give the same interface.** Reading the log-probabilities of class labels from a
generative API gives per-class probabilities for thresholds [chk-oai-logprobs]; rerankers sort
documents by relevance [chk-cohere-rerank]; on the arithmetic-heavy task in DM7, a fine-tuned 4B
model that writes a short reasoning step scored 0.98, within noise of reasoning LLMs (1.00 and 0.96)
[chk-distil]. Commenters on the launch thread put what the decision models add as a general
classifier that needs no training data, behind one typed interface (forum opinion). L, A.
**[as-of 2026-10-27]** Open instruction-tuned models with a decision head read from the language-model
head, fine-tuned with LoRA, beat Jev by about 4.4 capability points on JevBench v1.7 at 31B parameters;
without fine-tuning, Gemma 4 31B scored 79.6 against Jev's 80.1 on OpenDecisions, the authors' own
evaluation set [chk-arxiv-inner-jev]. M (preprint).

**DM11. In independent comparisons, accuracy depends on the task and calibration favours decision
models.** **[as-of 2026-10-27]** On JEVal (11,257 items from 36 datasets), Jev scored 78.38% with ECE
0.053, and GPT-6 Luna without thinking 80.93% with ECE 0.116 from probabilities it wrote out. The
best decision models, among them the authors' own SII-Decision models, matched thinking models on
accuracy and beat every generative model tested on calibration. They trailed the best generative
model by 3 to 6 points in medicine, finance and law, and Jev trailed Luna on CLINC150 intent
classification (86.5% against 92.0%) [chk-arxiv-gdm]. Across seven replications of published
annotation studies, scored as eight tasks with categorical human labels, Jev 1.13 had lower ECE than
Luna's token probabilities on all eight, but not consistently lower than
Qwen3.8-27B's. Its accuracy was lower on tweet relevance (76.2% against 84.2% on the 2023 set) and
its correlation with experts lower on tweet sentiment (0.740 against 0.816), and it led on party
positions and democracy indicators [chk-arxiv-polisci]. The largest System-1 models matched or beat
fast closed LLMs on decisions outside agent loops; small ones rarely succeeded in closed-loop
environments [chk-arxiv-s1arena]. M (preprints, not peer reviewed).

**DM12. A decision model can find the most likely answer and still overstate its probability.**
**[as-of 2026-10-27]** On prior-probability items, where the true distribution is known, Jev put on
average 89.35% of the probability on the true mode, whose true share averaged 35.60% (§5.1 and
Figure 5(a) of the paper). In a separate election simulation, the authors' own SII-Decision-27B
called 47 of 51 states, one more than the original pipeline, but its vote-share errors were about
twice as large (§5.4.3) [chk-arxiv-gdm]. M. Counts built from such answers need a correction against labelled items; see
[model-labels-for-counts.md](model-labels-for-counts.md).

**DM13. The cost lead depends on the price tier.** **[as-of 2026-10-27]** At OpenAI's Batch prices,
GPT-6 Luna cost less than Jev on six of seven annotation tasks; at standard prices Jev cost less on
six of seven [chk-arxiv-polisci]. OpenAI's guide gives no batch tier for its Decisions API, and
TypeSafe documents no batch-job API [chk-openai-decisions-oct27] [chk-ts-models-oct27]. M, L.

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

In Jev, every question in a request sees the same state and is answered independently: one answer is
never context for another. A question that depends on an earlier answer needs a second request, with
code in between [chk-ts-primitives]. L. **[as-of 2026-10-27]** This is not true of every backend that
copies the interface. Perplexity's 27B decider answers all questions of a request together, each
question sees the others, and the same question can score differently with different neighbours; its
4B Flash model answers each question on its own [chk-pplx-quickstart]. L.

**[as-of 2026-10-28]** TypeSafe's primitives page, read again, states no maximum number of options or
levels and no limit on the number of questions other than the context length [chk-ts-primitives-oct28];
the limits of 255 options and 2 to 10 levels in the table come from the subpages read on 2026-10-04
and were not read again.

**What it is not.** It cannot generate a value (so extraction is a Choice over candidates found by
code), does not do arithmetic or counting reliably [chk-ts-jagged], and does not reason in steps. A
default Jev request is text only [chk-ts-models]. **[as-of 2026-10-27]** TypeSafe's images page says
Jev 1.13 and 1.14 accept PNG or JPEG images when the request sends the header
`TypeSafe-Danger-Zone-Images: true`, and calls image input not ready for production [chk-ts-images]
[chk-ts-jev114]; its System One concept page still said on 2026-10-28 that Jev accepts text only
[chk-ts-system-one-oct28]. The two pages conflict. Clef, OpenAI Decisions and Perplexity's deciders
also read images [chk-cloudflare-clef] [chk-openai-decisions-oct27] [chk-pplx-quickstart]. Simon
Willison's summary of the trade: whatever text goes
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
- **[as-of 2026-10-27]** On JEVal's 10,938 choice and yes/no items, ECE was 0.015 for
  SII-Decision-27B (the authors' own model), 0.036 for Kev-27B and 0.053 for Jev. The best-calibrated generative model,
  GLM-5.3-Flash with thinking, had 0.078, GPT-6 Luna without thinking 0.116 and Qwen3.5-4B without
  thinking 0.253; the generative models wrote their probabilities out. On 28-label emotion
  classification, Jev's ECE was 0.306 [chk-arxiv-gdm]. M.
- **[as-of 2026-10-27]** Across seven annotation replications, scored as eight tasks with categorical
  labels, Jev 1.13's ECE was lower than GPT-6 Luna's token probabilities on all eight and not
  consistently lower than
  Qwen3.8-27B's; the study did not test recalibration on labels [chk-arxiv-polisci]. M.
- **[as-of 2026-10-27]** On about 600 choice questions over 450 short Dutch business texts, a
  practitioner found Jev the best calibrated of Jev, OpenAI Decisions and Claude Haiku 5.5 (which
  gives no per-answer probability). OpenAI's choice answers were right 95% of the time at a mean top
  probability of 0.90 [chk-vandeth]. On 107 labelled value pairs, Jev's answers at 0.9 or more, or 0.1
  or less, were right in 80 of 81 cases; the 14 answers from 0.2 to 0.8 were right in 7; a further 11
  answers that the author calls slightly uncertain were right 73% of the time, and the post does not
  give their bin edges. Gemini 3.8 Flash returned exactly 0 or 1 in 93 cases [chk-classmethod]. A.
- **[as-of 2026-10-27]** Strands Decider's repository says answers at confidence 0.9 or more were right
  about 95% of the time on short classification tasks it had not seen [chk-strands-oct27]. L (the
  vendor's own run).

**What follows** (inference from the above). A threshold is supported only by accuracy measured at
that threshold on labelled cases from the same traffic, reported beside coverage (the share of cases
acted on); TypeSafe's build guide advises plotting confidence against accuracy on the user's own data
[chk-ts-build]. A round number such as 0.9 carries no evidence of its own. The measurement holds for
one model version and one input mix. The October 2026 studies fit this reading: a low ECE across a
whole benchmark did not hold on each dataset in it (inference from [chk-arxiv-gdm]).

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
  task [chk-distil]. M, A. **[as-of 2026-10-27]** A practitioner re-ran Jev two weeks later and got
  the same answer on 594 of 600 questions [chk-vandeth]. Another found that re-asking one version
  after four weeks barely moved the probabilities, but that the upgrade from 1.13 to 1.14 changed the
  threshold routing of 6 of 107 cases [chk-classmethod]. Perplexity says identical requests can differ
  in the second decimal place [chk-pplx-quickstart]. A, L.

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
  that page cites [chk-ts-parallel]. L. **[as-of 2026-10-27]** The pattern rests on two properties of
  Jev, independent answers and a state billed once, and not every backend has both. Perplexity's 27B
  decider bills the state once per request (once per group when the API splits a large request), but
  its questions see one another, so a question's score depends on what it is grouped with; the page
  advises keeping the grouping fixed when comparing runs or tuning thresholds, and sending one
  candidate per request when unsure. Its 4B Flash model answers each question on its own but bills the
  state again for every question: three questions about a 10,000-token state bill about 30,000 input
  tokens, so with three or more questions the 27B model usually costs less [chk-pplx-quickstart]. L.
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
  new version still meets them (inference). L. **[as-of 2026-10-27]** Both of TypeSafe's aliases now
  point to `jev-1.14.0`; TypeSafe says it intends to give 60 days' warning before `jev-1.13.0` is
  formally deprecated and 30 days before `jev-1.14.0`, and to publish a deprecation policy first
  [chk-ts-models-oct27] [chk-ts-jev114]. A versioned id does not hold at every provider: Perplexity
  routes requests for its older decider ids to `pplx-decider-v1.2`, at that model's price
  [chk-pplx-quickstart] [chk-pplx-changelog]. Pydantic AI's guide advises pinning once tuned, and
  says a threshold tuned on one backend does not carry over to another [chk-pydantic-decision]. L.

## 5. Speed and cost: what the figures show (VOLATILE)

- **Vendor figures.** Jev: 70 to 500 ms end to end, evaluations run from laptops on the US West Coast
  near the service [chk-ts-announcement]; most queries about 100 ms [chk-ts-build]; $0.042 per million
  input tokens and free output [chk-ts-models]. TypeSafe also says it cannot prove the price is not
  subsidised and expects it to fall [chk-ts-announcement]. L.
- **Third-party measurements.** Entagl measured a median of 329 ms (p95 436 ms) against 1,598 ms (p95
  2,765 ms) for an unnamed Gemini model at low effort, at about 25x lower cost [chk-entagl]. JevBench
  lists 0.62 s and $0.032 per 1,000 decisions [chk-jevbench]. A, M.
- **Prices [as-of 2026-10-27].** Jev 1.13.0 and 1.14.0 both cost $0.042 per million input tokens,
  with free output [chk-ts-models-oct27]. Perplexity charges $0.02 for `pplx-decider-v1.2` (27B) and
  $0.01 for `pplx-decider-flash-v1.2` (4B), with free output; its first 27B model cost $0.04
  [chk-pplx-quickstart] [chk-pplx-changelog]. Flash bills the state once for each question, so its
  lower token price does not give a lower price per decision when a request asks several questions
  (§4) [chk-pplx-quickstart]. Clef's Workers AI price is unchanged at $0.24
  [chk-cloudflare-model-oct27]. OpenAI's is in §6. L.
- **Independent and practitioner measurements [as-of 2026-10-27].** Across seven annotation tasks, Jev
  1.13 took 0.09 to 0.27 s a decision, GPT-6 Luna 0.75 to 1.04 s and Qwen3.8-27B 0.39 to 0.87 s; the
  cost result at Batch and standard prices is in DM13 [chk-arxiv-polisci] (M). One practitioner's
  costs per 1,000 decisions on short texts: Jev $0.011 to $0.016, OpenAI Decisions $0.024 to $0.031,
  Claude Haiku 5.5 without thinking $0.036 to $0.049; OpenAI's median was 179 ms a text, measured
  through OpenRouter with all questions in one call [chk-vandeth] (A). Another put 107 decisions at $0.0023
  on Jev against $0.0429 on Gemini 3.8 Flash, with Jev at under half Gemini's response time
  [chk-classmethod] (A). Self-hosted, Strands Decider 2B took 11 to 13 s a decision on a 2-vCPU CPU
  micro-VM [chk-aws-routing] (A).
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

Read 2026-10-04; rows and paragraphs marked `[as-of 2026-10-27]` were checked again on that date.
Vendor claims are L; every benchmark below is run by the vendor named unless marked.

| Offer | Maker | Weights | Released | Notes |
| --- | --- | --- | --- | --- |
| Jev 1.14 [as-of 2026-10-27] | TypeSafe AI | closed | 2026-10-14 | Released as `jev-preview`, with `jev-latest` announced to follow a week later; both pointed to it on 2026-10-27; $0.042 per M input, free output; 64k tokens per request and 32k per question, 262k with an opt-in header; image input and the Box type as previews behind an opt-in header; also on Netlify AI Gateway; TypeSafe's own charts give it 60.0 against 58.9 for 1.13 on an internal intelligence measure and a calibration error of 1.6 against 1.8 [chk-ts-jev114-charts]; [file](../models/typesafe/jev-1.14.0.md) [chk-ts-models-oct27] [chk-ts-jev114] [chk-netlify-jev114] |
| Jev 1.13 | TypeSafe AI | closed | 2026-09-15, early access | Still listed on 2026-10-27, no longer behind an alias [as-of 2026-10-27]; text, and images behind an opt-in header [as-of 2026-10-27]; served by TypeSafe, OpenRouter, Vercel AI Gateway, Pydantic AI Gateway; [file](../models/typesafe/jev-1.13.0.md) [chk-ts-models] [chk-ts-models-oct27] [chk-ts-images] |
| Decisions API | OpenAI | closed | 2026-10-22, generally available [as-of 2026-10-27] | `gpt-6-luna`; text, images and JSON; predicate, choice and score; $0.10 per M uncached input, standard Luna cache read and write rates, no output charge; long-context and regional multipliers apply [chk-openai-decisions-oct27] [chk-openai-changelog-oct27] |
| Decisions API: `pplx-decider-v1.2` (27B) and `pplx-decider-flash-v1.2` (4B) [as-of 2026-10-27] | Perplexity | closed: the Hugging Face repository for v1.2 is private, though its card names Apache-2.0 and a Qwen3.8-27B base [chk-pplx-hf] | October 2026 (three versions that month) | `/v1/decisions`; yes/no, choice and score; text and images; 256K context; 1 to 128 questions; $0.02 and $0.01 per M input, free output; requests for older ids route to v1.2 [chk-pplx-quickstart] [chk-pplx-changelog] |
| Clef (27B) and Clef-flash (9B) | Cloudflare | open, Apache-2.0 | 2026-10-01 | LoRA and a routing head on Qwen bases; image input; 65,536 tokens; Clef $0.24 per M input on Workers AI; claims full Jev-API compatibility [chk-cloudflare-clef] [chk-cloudflare-model]; the Workers AI page showed no newer version or changelog [as-of 2026-10-27] [chk-cloudflare-model-oct27] |
| Strands Decider 2B | AWS (Strands Labs) | open, Apache-2.0 | 2026-10-01 | LoRA on Qwen3.5-2B-Base; local server binds to localhost with no authentication [chk-strands]. [as-of 2026-10-27] A v1 set adds a 2B Qwen3.5 reference model and Gemma 4 E2B, E4B, 12B and 26B-A4B variants; the repository reports accuracy 0.779 and ECE 0.072 for the 2B v1 on its own 231-task JevBench run, and documents no hosted Bedrock API [chk-strands-oct27] |
| Kev 1.0 (0.8B, 4B, 9B, 27B) | an independent open project | open, Apache-2.0 | 2026-10-01 | LoRA adapters on Qwen3.5 bases and full weights on Qwen3.8-27B; text only, English [chk-kev-release]; llama.cpp merged a `/v1/systemone` server for Kev and other open decision models on 2026-10-02 [chk-llama-cpp]; no release after Kev 1.0 (2026-10-01) [as-of 2026-10-28] [chk-kev-releases]; the repository's code kept changing, with fixes to the fine-tuning scripts and tests on 2026-10-22 [chk-kev-commit] |

The Kev project's own index puts Kev-27B at 52.3 against Jev's 54.0 and its MMLU-Pro at 0.675
against Jev's 0.840; its release notes give date arithmetic as weakest below 27B [chk-kev-release]
(A, a competitor's measurement). Cloudflare reports a Clef model ahead of Jev on 8 of the 10
benchmarks it ran, with Jev ahead on When2Call and BRIGHT, and Clef ahead on 3 of TypeSafe's 4
workflows [chk-cloudflare-clef] (L, every column run by Cloudflare). JevBench, an independent
benchmark, puts Jev first on its capability score (80.0) among systems within 2x of Jev's cost and
latency, and third on its official four-axis ranking; Clef-Flash scores 70.3 [chk-jevbench] (M).
**[as-of 2026-10-28]** The charts in TypeSafe's 1.14 post, marked with a warning not to trust
benchmarks, score its internal intelligence measure as 60.0 for Jev 1.14, 58.9 for Jev 1.13, 46.7 for
Kev-27B, 46.0 for `pplx-decider-v1.1-27b`, 44.3 for Clef and 38.8 for Clef-flash, and its calibration
error (units not stated) as 1.6, 1.8, 17.8, 35.0, 11.2 and 19.1 for the same models; the post says the
measure is a best guess, likely biased towards TypeSafe's models, and covers only open-weight
comparisons [chk-ts-jev114-charts] [chk-ts-jev114] (L, a competitor's measurement for every model
but Jev). A comparison of the vendor pages found no independent
replication of Cloudflare's or AWS's tables by 2026-10-03 [chk-digital-applied]. No decision-model
product from Anthropic or Google was found in searches on 2026-10-04. **[as-of 2026-10-27]** Searches
on 2026-10-27 found none from Anthropic, Google or Microsoft either. The Vercel AI SDK lists native
decisions for TypeSafe, OpenAI and Perplexity, and emulates them for Anthropic and Google with
structured output: there the yes/no probability is an estimate the model is prompted to give, and
Choice and Score answers carry no distribution [chk-aisdk-decisions]. L. The JevBench page could not
be read on 2026-10-27 (it exceeded the fetch size limit), so its figures above are those of
2026-10-04; a later preprint cites JevBench v1.7 [chk-arxiv-inner-jev].

**Adoption.** Vercel reports that nearly 13% of its paid AI Gateway teams used Jev within 24 hours,
more than twice any earlier launch, and adds that the next test is whether use lasts
[chk-vercel-launch] (L, a reseller's own data). TypeSafe's CEO has claimed a trillion tokens a day
[chk-latent-space] (A, his statement only). Some Vercel teams were throttled from 2026-09-26
([../providers/typesafe.md](../providers/typesafe.md)).

**Imitations of the interface.** A post reading the option logits of a 0.6B local model reproduces
the request shape in 25 lines; it calls itself a parody and reports no accuracy, latency or
calibration comparison [chk-nobodywho]. That the interface is easy to copy and the training is not is
the view of the launch-thread commenters and of [chk-arcturus] (A).

### OpenAI Decisions [as-of 2026-10-27]

The guide and API reference establish the public interface, not calibration or speed on a caller's
traffic. `POST /v1/decisions` takes a `model`, shared `input` and named `questions`; only
`gpt-6-luna` is supported. The three types are `predicate` (probability of a condition), `choice`
(a supplied category and distribution) and `score` (a probability-weighted average of ordered
level indices). Choice and score also return confidence. An answer can instead have type `refusal`.
L [chk-openai-decisions-oct09] [chk-openai-decisions-ref-oct09].

The current guide permits inline image data or public HTTP(S) image URLs, but not `file_id`. It also permits images in question instructions and JSON input. It supports up to 400 questions per request and caching for shared input. The reusable shared prefix must reach 1,024 tokens; questions, including their images, are outside that prefix. Cache-read and write counts are included in `input_tokens` and must not be added again. Live behavior was not tested. L [chk-openai-decisions-oct27] [chk-openai-changelog-oct27].

General extraction into a custom JSON schema and function calling use Responses rather than this
endpoint. Independent questions can share one request; questions that depend on an earlier answer
need another request. L [chk-openai-decisions-oct09].

OpenAI recommends observable question criteria and labelled application examples to set thresholds,
with false-positive and false-negative costs taken into account. Its roughly 10x speed claim against
Responses has no workload or independent replication in the guide. The endpoint supports ZDR and
HIPAA for eligible customers, and US/European residency and processing subject to the documented
requirements. L [chk-openai-decisions-oct09].

Up to 2026-10-27 the changelog has no Decisions entry after general availability on October 22; on
October 15 OpenAI added a native Decisions integration in GPT-Live. The guide gives no Batch, flex or
priority tier for Decisions and no rate limits, and it makes no calibration claim. L
[chk-openai-changelog-oct27] [chk-openai-decisions-oct27]. No independent study of the endpoint's
calibration was found. In one practitioner test during the beta, its choice answers were
under-confident (right 95% of the time at a mean top probability of 0.90), and on one yes/no question a
cut at 0.5 was 84% correct; the post does not say whether over all emails or over the 77 that needed
no person [chk-vandeth]. A.

### Perplexity Decisions [as-of 2026-10-27]

`POST https://api.perplexity.ai/v1/decisions` takes a `state`, a `model` and named `questions` of type
yes/no ("noul"), choice or score. A yes/no answer is a probability; choice and score answers carry a
`confidence` computed from the distribution. Both current models take text and PNG, JPEG or WebP data
URLs (the API fetches no image URLs), with a 256K-token context, 1 to 128 questions, up to 255 options
and up to 10 levels. The default rate limit is 10 requests a second per organization. The aliases
`pplx-decider-latest` and `pplx-decider-flash-latest` can move to newer versions, and the page asks
callers to revalidate thresholds when they do. It claims no measured accuracy and advises running
both models on the caller's own labelled data. The 27B model answers the questions of a request
together, so grouping changes scores; Flash answers each alone but bills the state per question (§4).
L [chk-pplx-quickstart]. The changelog lists the
launch with `pplx-decider-v1-27b` at $0.04, then `v1.1-27b` at $0.02, then v1.2 and the 4B Flash
model, all in October 2026 [chk-pplx-changelog]. L.

### Framework support [as-of 2026-10-27]

Pydantic AI runs decision models as agent models through three classes: `TypeSafeModel`
(`typesafe:jev-latest`), `SystemOneModel` (`system-one:<model>`, for any server with the
`/v1/systemone` API, such as a local one) and `OpenAIDecisionsModel` (`openai-decisions:gpt-6-luna`).
The agent's output type becomes the questions: a `bool` is a yes/no question, a `Literal` or `Enum`
a choice, an `IntEnum` of described levels a score, a bounded `float` the probability itself, and a
`list` or `dict` of options one yes/no question per option. `provider_details` returns the
probabilities, the scores and a `confidence` that the guide calls a margin, not the probability of
being right. `decision_boolean_threshold` defaults to 0.5, and `decision_route_threshold` raises
`UnsureRoute` below it. The guide advises tuning thresholds on a few hundred texts from real traffic,
storing the probabilities and sweeping thresholds offline, and watching how often work passes to a
language model. L [chk-pydantic-decision]. `OpenAIDecisionsModel` defaults `max_questions` to 200,
while OpenAI's generally available API accepts 400 [chk-pydantic-openai-decisions]
[chk-openai-decisions-oct27]. The pages give no Pydantic AI version for any of the three; the pull
request that added the shared `DecisionModel` base merged on 2026-09-24 [chk-pydantic-pr8696]. L.

## 7. Data handling (VOLATILE)

A decision model is another external service that sees the state. TypeSafe documents no training on
customer requests and zero data retention for enterprise customers, but states no default retention
period, and its customer agreement allows telemetry derived from customer data in perpetuity
([../models/typesafe/README.md](../models/typesafe/README.md)). A practitioner demo logs an excerpt of
each input in its server route [chk-shapeshift], and the `llm` CLI plugin logs prompts and answers as
`llm` does for any model [chk-llm-typesafe]. Open-weight models can run locally; Strands Decider's local server binds to localhost and has no
authentication [chk-strands], and Kev's server is open unless `KEV_API_KEY` is set
[chk-kev-08b-card]. L, A.

**[as-of 2026-10-27]** TypeSafe's customer agreement still carries the date 2026-09-23 and the same
terms: telemetry derived from customer data in perpetuity, no duty to retain customer data, and no
training on customer data without prior consent [chk-ts-mca-oct27]. The 1.14 post describes an opt-in
that it says helps TypeSafe find issues and debug use cases, and repeats that queries are not used
for training [chk-ts-jev114]; its screenshot shows the setting as an organization-wide switch that
lets TypeSafe read and analyse the organization's inputs and outputs to understand where the model
is weak [as-of 2026-10-28] [chk-ts-jev114-charts]. OpenAI's guide lists zero data retention and HIPAA support for eligible
customers, and processing in the United States or Europe [chk-openai-decisions-oct27]. Perplexity's
quickstart states no retention terms [chk-pplx-quickstart]. L.

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

**Status on 2026-10-27** [as-of 2026-10-27]. This is a reading of the evidence so far, not a score: each
forecast is scored as held, falsified or unscored only at its horizon.

| Forecast | Reading | Why |
| --- | --- | --- |
| 1. Three large providers | At risk | Of the five named, only OpenAI offers a generally available typed decision API; none was found from Anthropic, Google or Microsoft, and AWS's decider is an open model with no hosted API documented [chk-openai-changelog-oct27] [chk-aisdk-decisions] [chk-strands-oct27] |
| 2. Versions faster than quarterly | Cadence holding; support open | Jev 1.14 shipped a month after 1.13, and Perplexity shipped three versions in October and routes old ids to the newest [chk-ts-jev114] [chk-pplx-changelog]. TypeSafe's 60 and 30 days are intended warning before deprecation, not a support lifetime, so the six-month support part stays open until its policy is published |
| 3. Open model under 10B matches Jev | No reading | JevBench could not be read; the sub-10B figures found are vendor-run on other task sets [chk-strands-oct27] |
| 4. Generative model within 2x of Jev's latency | No reading | The one independent latency comparison (DM8, §5) found GPT-6 Luna with token probabilities still slower than Jev; OpenAI Decisions' median in §5 is one practitioner's beta test |
| 5. No out-of-the-box calibration across users' data | Holding | Jev's ECE on one benchmark differed by dataset by a factor of about six (DM3, §2) |

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
- **[as-of 2026-10-27]** The independent studies of October 2026 show calibration as the class's most
  consistent lead and accuracy as dependent on the task; whether a decision model or a generative
  model labels a given task better is a measurement on labelled items from that task, not a property
  of the class.
- **[as-of 2026-10-27]** Counts and shares built from model answers, decision or generative, need a
  correction against a labelled sample ([model-labels-for-counts.md](model-labels-for-counts.md)).

## Limits and open questions

- Up to 2026-10-04 almost every number here was from a vendor measuring itself or a competitor, with
  one independent benchmark and one preprint. **[as-of 2026-10-27]** Four independent preprints of
  October 2026 now compare the class with generative models or with Jev (DM10 to DM13); none is peer
  reviewed, and two were read as abstracts only. Small samples throughout (3 pairs, 10 tasks, 100
  invoices, 107 value pairs).
- OpenAI documents its generally available Decisions API [as-of 2026-10-27] [chk-openai-decisions-oct27]. Independent calibration,
  speed and end-to-end comparisons against other decision APIs were not verified in this update.
- Whether Jev's separately asked questions are consistent with each other after TypeSafe removed its
  warning.
- What "calibrated" means across products: TypeSafe, Cloudflare and Kev each fit or report it
  differently.
- Whether any of this improves an end-to-end product outcome, as opposed to a decision accuracy; no
  study read measures that.
- Whether TypeSafe's image input, now a preview behind a header, leaves preview, and which of its two
  pages (images, or the System One concept page) it will correct [as-of 2026-10-27].
- Re-check after the next Jev version or TypeSafe's deprecation policy, when OpenAI changes the
  Decisions interface, when Anthropic, Google or Microsoft ships a decision API, or when JevBench can
  be read again.

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

OpenAI general-availability sources, read 2026-10-27 (L):

- [chk-openai-decisions-oct27] <https://developers.openai.com/api/docs/guides/decisions>.
- [chk-openai-changelog-oct27] <https://developers.openai.com/api/docs/changelog>.

Refresh of 2026-10-27, read on that date unless marked

- [chk-ts-models-oct27] TypeSafe, models <https://docs.typesafe.ai/models>. L.
- [chk-ts-jev114] TypeSafe, release post for Jev 1.14, dated 2026-10-14
  <https://typesafe.ai/blog/jev-1-14>. L.
- [chk-ts-images] TypeSafe, images <https://docs.typesafe.ai/images.md>. L.
- [chk-ts-box] TypeSafe, Box questions <https://docs.typesafe.ai/primitives/box.md>, read 2026-10-28. L.
- [chk-ts-system-one-oct28] TypeSafe, System One concepts
  <https://docs.typesafe.ai/concepts/system-one>, read 2026-10-28. L.
- [chk-ts-mca-oct27] TypeSafe, master customer agreement, last updated 2026-09-23
  <https://typesafe.ai/legal/mca>. L.
- [chk-netlify-jev114] Netlify changelog, Jev 1.14.0 in AI Gateway, page updated 2026-10-27
  <https://netlify.com/changelog/typesafe-jev-1-14-0-ai-gateway>, read 2026-10-28. L.
- [chk-pplx-quickstart] Perplexity, Decisions API quickstart
  <https://docs.perplexity.ai/docs/decisions/quickstart>. L.
- [chk-pplx-changelog] Perplexity, API changelog, October 2026 entries
  <https://docs.perplexity.ai/docs/resources/changelog>. L.
- [chk-cloudflare-model-oct27] Cloudflare, Workers AI Clef model page
  <https://developers.cloudflare.com/workers-ai/models/clef/>. L.
- [chk-strands-oct27] AWS Strands Labs, Strands Decider repository README
  <https://github.com/strands-labs/strands-decider>. L.
- [chk-kev-releases] jaredpalmer/kev, release list through the GitHub API
  <https://api.github.com/repos/jaredpalmer/kev/releases>, read 2026-10-28. L.
- [chk-kev-commit] jaredpalmer/kev, commit e7ae8fd5fda9d40865d3a9de90f074feb0735985 of 2026-10-22
  <https://github.com/jaredpalmer/kev/commit/e7ae8fd5fda9d40865d3a9de90f074feb0735985>, with its date
  from the GitHub API, read 2026-10-28. L.
- [chk-pplx-hf] Hugging Face, `perplexity-ai/pplx-decider-v1.2`
  <https://huggingface.co/perplexity-ai/pplx-decider-v1.2>, read 2026-10-28. L.
- [chk-ts-primitives-oct28] TypeSafe, primitives <https://docs.typesafe.ai/primitives>, read
  2026-10-28. L.
- [chk-ts-jev114-charts] TypeSafe, the charts and the settings screenshot in the Jev 1.14 release post
  <https://typesafe.ai/blog/jev-1-14>, images read 2026-10-28. L.
- [chk-aisdk-decisions] Vercel AI SDK, decisions <https://ai-sdk.dev/docs/ai-sdk-core/decisions>. L.
- [chk-pydantic-decision] Pydantic AI, decision models
  <https://pydantic.dev/docs/ai/models/decision/>. L.
- [chk-pydantic-openai-decisions] Pydantic AI, `pydantic_ai.models.openai_decisions` API reference
  <https://pydantic.dev/docs/ai/api/models/openai_decisions/>. L.
- [chk-pydantic-pr8696] pydantic/pydantic-ai, pull request 8696, merged 2026-09-24
  <https://github.com/pydantic/pydantic-ai/pull/8696>. L.
- [chk-arxiv-gdm] Duan, Lin, Wang, Xiang, Wu, Zhang, Yan, Wang and Wei, General Decision Models:
  Benchmarking and Insights Beyond Jev, v2 2026-10-12 <https://arxiv.org/html/2610.03935>. M.
- [chk-arxiv-s1arena] Chen, Liu, An, Wang and Zhou, System1-Arena: Which Decisions Can Be Left to
  System 1?, 2026-10-15, abstract only <https://arxiv.org/abs/2610.21244>. M.
- [chk-arxiv-polisci] Denney and DiGiuseppe, JEV versus LLMs: Accuracy, Cost and Calibration on Seven
  Political Science Replications, 2026-10-05 <https://arxiv.org/html/2610.06625v1>. M.
- [chk-arxiv-inner-jev] Geuter, Cheng and Alvarez-Melis, Releasing the Inner Jev: A Simple Recipe for
  Open Decision Models, 2026-10-12, abstract only <https://arxiv.org/abs/2610.17205>. M.
- [chk-aws-routing] AWS Builder Center, Benchmarking Strands Decider, LLM classifiers and Bedrock
  routing for model routing, 2026-10-09
  <https://builder.aws.com/content/3KRx3G8JMf1G06ZFu2dDEdE2DLw/benchmarking-strands-decider-llm-classifiers-and-bedrock-routing-for-model-routing>.
  A (one practitioner, 107 held-out requests).
- [chk-vandeth] Vincent van Deth, OpenAI Decisions API explained, test run 2026-10-09
  <https://vincentvandeth.nl/blog/openai-decisions-api-explained-jev-haiku>. A.
- [chk-classmethod] Classmethod DevelopersIO, report of a DevelopersIO 2026 Tokyo talk on decision
  models, 2026-10-24 <https://dev.classmethod.jp/en/articles/devio2026-tokyo-decision-model-report/>. A.

OpenAI public-beta correction sources, read 2026-10-09 (L):

- [chk-openai-decisions-oct09] <https://developers.openai.com/api/docs/guides/decisions>.
- [chk-openai-decisions-ref-oct09] <https://developers.openai.com/api/reference/python/resources/decisions/methods/create>.
- [chk-openai-changelog-oct09] <https://developers.openai.com/api/docs/changelog>, October 6 entry.
- [chk-openai-decisions-ref-md-oct09] Python reference Markdown representation, <https://developers.openai.com/api/reference/python/resources/decisions/methods/create.md> (L, read 2026-10-09).
