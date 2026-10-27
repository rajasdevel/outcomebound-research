---
last_checked: 2026-10-27
volatility: STABLE (statistical methods and measured studies; the benchmark readings change only when a paper is revised)
sources:
  - https://export.arxiv.org/abs/2301.09633
  - https://export.arxiv.org/abs/2311.01453
  - https://export.arxiv.org/abs/2406.04291
  - https://arxiv.org/abs/2306.04746
  - https://arxiv.org/abs/2408.15204
  - https://ideas.repec.org/a/sae/somere/v54y2025i3p1074-1109.html
  - https://cran.r-universe.dev/mixedsubjects
  - https://export.arxiv.org/abs/2603.16041
  - https://arxiv.org/html/2605.31278v1
  - https://arxiv.org/html/2610.03935
  - https://export.arxiv.org/abs/2311.01449
  - https://export.arxiv.org/abs/2404.12259
  - https://arxiv.org/html/2412.13678
  - https://journal.computationalcommunication.org/article/view/9248
  - https://arxiv.org/html/2601.17658v2
  - https://arxiv.org/html/2506.05690
  - https://arxiv.org/html/2602.02053v2
  - https://arxiv.org/html/2510.26205
  - https://arxiv.org/html/2408.14717
  - https://arxiv.org/html/2603.11991
---

# Counting with model labels: valid estimates, theme discovery and aggregation questions

Re-check when a method paper gives new sample-size guidance for estimates from model labels, when a
study measures the run-to-run stability of a theme-discovery method, or when one of the benchmarks in
§6 or §7 is revised; in any case by 2027-04-25.

A model can label every item in a large collection of short texts: a sentiment level, a category, a
yes/no property. People then want counts and proportions from those labels: how many items carry a
category, what share has a property, how a share differs between groups. This page covers what the
research says about turning model labels into such numbers with honest uncertainty, how many
labels from people that needs, how themes are found before they are counted, and what benchmarks show
about answering corpus-wide counting questions by retrieval. It is for anyone who reports a number
that a model's labels produced. Which model to label with is a separate question: decision models
are in [decision-models.md](decision-models.md), model judges in [llm-as-judge.md](llm-as-judge.md),
and evaluation statistics in [agent-evals.md](agent-evals.md).

**Evidence classes**, as in [the conventions](../CONVENTIONS.md): M measured; L maker or vendor
documentation; P practitioner consensus; A anecdote or one uncontrolled report; F forecast.
**Citations.** Bracketed `[chk-…]` ids are sources read on 2026-10-27, listed under Sources. For some
papers only the abstract was read; the Sources list says which. Most papers here are preprints, not
peer reviewed, unless the Sources list names a venue.

## Key findings

**CL1. Model labels used directly in counts give biased numbers and false confidence.** The DSL
paper reports substantial bias and invalid confidence intervals when surrogate labels go straight into
a downstream analysis, even at 80 to 90% labeller accuracy [chk-dsl]. A benchmark of decision models
reports two separate results [as-of 2026-10-28]: Jev overstated the probability of the answer it
picked on items with a known distribution, and in an election simulation the authors' own
SII-Decision-27B had vote-share errors about twice those of the original pipeline [chk-arxiv-gdm]. M.

**CL2. A small labelled sample can correct the whole set, with valid intervals.** Prediction-powered
inference (PPI) combines a small sample labelled by people with model predictions on everything, and
gives valid confidence intervals for means, quantiles and regression coefficients with no assumption
about how good the model is; better predictions give narrower intervals [chk-ppi]. PPI++ tunes how far
it leans on the predictions, and its authors state that its intervals improve on classical intervals
from the labelled sample alone [chk-ppipp]. **[as-of 2026-10-28]** Freedom from assumptions about the
model's quality is not freedom from all assumptions: one PPI library states that the labelled and
unlabelled items are drawn i.i.d. from one distribution and that the predictor is fixed and trained on
data disjoint from both, and it describes PPI++'s gain over the classical estimator as holding in the
limit of large samples, with normal-theory intervals that degrade at small sample sizes [chk-glide]. Stratified PPI gives tighter intervals when the labeller's quality
differs between strata [chk-stratppi]. M.

**CL3. Design-based supervised learning (DSL) stays valid with arbitrarily biased labels, if the
sampling is designed.** Its guarantee needs the probability that each item is chosen for labelling to
be controlled by the analyst [chk-dsl]. M.

**CL4. Choosing which items people label can save labels.** Confidence-driven inference uses the
model's confidence to choose the items for people to label, and cut the labels needed by more than
25% on each of three tasks (politeness, stance and bias) while keeping valid intervals [chk-cdi]. M.

**CL5. How many labels depends on how well the model predicts the label.** A power analysis for PPI
gives closed-form sample sizes; its rule of thumb is that the labelled sample needed shrinks by about
the R² between predictions and true labels [chk-pppower]. **[as-of 2026-10-28]** The rule holds for
PPI++ with its variance-optimal tuning and an unlabelled pool much larger than the labelled sample;
the paper's exact formula depends on the pool size, and plain PPI's variance depends on the variance
of the residual between label and prediction instead [chk-pppower]. In one library's case study, 100 expert
labels gave the precision of about 143 to 157 labels used alone; the library switches from
normal-theory to bootstrap intervals below 50 labels per stratum, a rule of thumb [chk-glide]. The
mixed subjects design derives PPI's effective sample size and a power analysis for choosing between
labels from people and model predictions [chk-mixed]. M; the 50-label switch is L.

**CL6. Every one of these methods assumes the labelled items represent the items counted.** The
labelled sample is drawn at random from the same collection, or by a design with known inclusion
probabilities. One PPI library states that it does not yet handle covariate or label shift between
the labelled and unlabelled sets [chk-glide]; DSL's guarantee rests on the designed sampling
[chk-dsl]. L, M.

**CL7. Clustering embeddings was more stable between runs than an LLM topic pipeline; LLM methods
matched categories that people wrote better.** On one corpus, three runs of BERTopic agreed at an
Adjusted Rand Index of 0.873, an LLM prompt pipeline at 0.533 and LDA at 0.135 [chk-doan]. TopicGPT
scored 0.74 harmonic-mean purity against categories that people annotated, against 0.64 for the best
baseline [chk-topicgpt]. A pipeline that embeds, clusters and has a model name the clusters rebuilt
known categories in synthetic transcripts with 94% accuracy [chk-clio]. M.

**CL8. Retrieval that reads the top few passages cannot answer questions over a whole corpus.** On
counting, extremum, sorting and top-k questions over a corpus, the best retrieval baseline averaged
an F1 of about 1.5 (0 to 100 scale), and the authors' own method reached 6.63 [chk-globalqa]. On
80 queries over tables, plain RAG answered none of the 60 scored queries; aggregation queries were
not scored [chk-tag]. M.

**CL9. Graph retrieval helps some question shapes and not others.** **[as-of 2026-10-28]** In
GraphRAG-Bench its effect on simple fact lookup depended on the corpus: on the novel corpus plain
retrieval with reranking scored highest, while on the medical corpus HippoRAG2 led plain retrieval
with or without reranking; graph methods led on complex reasoning and summarisation on both corpora
[chk-graphrag-bench]; on WildGraphBench it led on multi-fact questions that gather evidence from many
documents, and plain retrieval had the best summary F1 [chk-wildgraph]. M.

**CL10. Zero-shot sentiment is easy and zero-shot emotion is hard.** On BTZSC's 22 datasets, the best
NLI cross-encoder, reranker, embedding model and instruction-tuned LLM reached sentiment macro F1 of
0.88 to 0.92, and the best plain base encoder 0.38 [as-of 2026-10-28]; the best emotion macro F1 was
0.44 to 0.51, and instruction-tuned LLMs reached at most 0.37 on emotion [chk-btzsc]. M.

## 1. Why model labels bias counts (STABLE)

A count from model labels is the true count plus the model's errors, and the errors are seldom
balanced: a model that mislabels one category more often than another moves the share. DSL's authors
show that bias and undercoverage appear even when surrogate accuracy is 80 to 90% [chk-dsl]. Summing
probabilities instead of labels does not remove the problem when the probabilities are not
calibrated on the same data. **[as-of 2026-10-28]** A benchmark of decision models reports two
separate results. On prior-probability items, Jev put on average 89.35% of the probability on the
true mode, whose true share averaged 35.60% (§5.1 of the paper). In an election simulation, the
authors' own SII-Decision-27B called 47 of 51 states, one more than the original pipeline, but its
vote-share errors were about twice as large (§5.4.3) [chk-arxiv-gdm] (M). Calibration measured on one dataset
does not carry over to another; see [decision-models.md](decision-models.md#2-confidence-and-calibration-stable).

## 2. Estimators that use a small labelled sample (STABLE)

| Method | What it needs | What it gives | Source |
| --- | --- | --- | --- |
| PPI | A small sample labelled by people, predictions on all items, both drawn from one distribution, and a predictor not fitted on these items | Valid intervals for means, quantiles and regression coefficients, with no assumption about the model's quality | [chk-ppi] [chk-glide] |
| PPI++ | As PPI | Tuned reliance on the predictions; the authors state the intervals improve on the labelled sample alone, a gain one library describes as holding in the limit of large samples; cheap to compute | [chk-ppipp] [chk-glide] |
| Stratified PPI | As PPI, plus strata (for example groups, or levels of the label) | Tighter valid intervals when the labeller's quality differs by stratum | [chk-stratppi] |
| DSL | Labelled items chosen with probabilities the analyst controls | Asymptotically unbiased estimates and valid intervals even when the labels are arbitrarily biased | [chk-dsl] |
| Confidence-driven inference | Model confidence for each item | A choice of which items to label; more than 25% fewer labels on three tasks, no worse than labels from people alone | [chk-cdi] |
| Mixed subjects design | Labels from people and model predictions | PPI's effective sample size, a "PPI correlation" for how interchangeable the two are, and a power analysis | [chk-mixed] |

All are M. The R package `mixedsubjects` implements PPI++ and six other estimators, among them
difference-in-means, GREG and difference-in-predictions [chk-mixedsubjects-pkg] (L); the
power-analysis paper publishes calculators [chk-pppower]; the GLIDE library implements PPI++,
stratified PPI++, a bootstrap variant for small samples and an inverse-probability-weighted estimator
[chk-glide] (L).

## 3. How many labels from people (STABLE)

- **The rule of thumb.** The labelled sample needed shrinks by about R², the share of the true label's
  variance that the predictions explain [chk-pppower] (M). **[as-of 2026-10-28]** The paper derives
  the rule for PPI++ with its variance-optimal tuning, on the assumption that the unlabelled pool is
  much larger than the labelled sample; its exact sample-size formula keeps the pool size, and can ask
  for more labels than a small pool holds. Plain PPI, without the tuning, has a variance set by the
  residual between label and prediction, so the rule does not apply to it directly [chk-pppower] (M).
- **A worked example (inference from [chk-pppower], under the conditions above).** With labels from
  people alone, a share near 50% needs about 384 random items for a 95% interval of ±5 points, and
  100 items give about ±10 points. With tuned PPI++ and a large unlabelled pool, the need is about
  (1 − R²) × 384: about 140 items when the correlation between label and prediction is 0.8, and
  about 75 when it is 0.9.
- **Small strata.** One library uses normal-theory intervals from 50 labels per stratum and a
  bootstrap below that, and calls the threshold a rule of thumb [chk-glide] (L).
- **What the correction is worth.** In that library's case study, 100 expert labels with PPI++ gave
  the interval width of about 143 labels used alone, and stratified PPI++ about 157 [chk-glide] (M,
  one case study).
- **Rare categories.** A category held by a few percent of items needs many random labels for a
  useful relative error; choosing items by model confidence, with the inclusion probabilities kept,
  keeps DSL or stratified estimates valid [chk-dsl] [chk-cdi] (inference).
- **A model is not ground truth.** The corrected methods assume the labelled sample holds true labels;
  labels from another model are predictions, not the gold standard (inference from [chk-ppi]
  [chk-mixed]).
- **A predictor fitted on the labels.** The library cited above assumes a predictor trained on data
  disjoint from both samples [chk-glide]; a model tuned or calibrated on the same labelled items that
  then correct its counts does not meet that assumption, so the tuning set and the correction set are
  kept apart (inference).

## 4. The same-population assumption (STABLE)

The labelled sample stands for the items counted only when it is drawn from them: at random, or by a
design whose inclusion probabilities are recorded [chk-dsl]. A sample from another period, another
source or another label set measures a different population. One library states that it does not
handle covariate or label shift between the labelled and unlabelled sets [chk-glide] (L). A new model
version or a new mix of inputs changes the predictions, so a labelled sample is scored again with the
new model before its correction is reused (inference).

## 5. Theme discovery and run-to-run stability (STABLE)

- **Stability.** On 12,747 posts with 50 topics, three independent runs agreed at an Adjusted Rand
  Index of 0.873 for BERTopic, 0.533 for an LLM pipeline (PromptTopic with gpt-4o-mini) and 0.135 for
  LDA [chk-doan] (M, one corpus).
- **Agreement with categories that people wrote.** TopicGPT scored 0.74 harmonic-mean purity on
  Wikipedia topics that people annotated, against 0.64 for the best baseline, which the abstract does
  not name [chk-topicgpt] (M).
- **Concept induction.** LLooM's authors report concepts of higher quality and coverage than topic
  models, which return keywords; the abstract gives no numbers [chk-lloom] (M, abstract only).
- **A hybrid pipeline.** Clio extracts facets with a model, embeds one facet, clusters with k-means,
  has a model title and summarise each cluster, and builds a hierarchy with k-means and prompting. On
  19,476 synthetic multilingual transcripts it rebuilt the known categories with 94% accuracy,
  against 5% for random assignment [chk-clio] (M, the maker's own evaluation).
- **Comparisons across contexts.** A study of LDA, BERTopic, TopicGPT and LLooM on social media posts,
  party platforms and bills found TopicGPT best for precise categorisation and LLooM for concept
  induction. Its annotators found that models surface rich themes but condense them poorly into
  short labels. The abstract reports no stability results [chk-wang-chen] (M, abstract only).

What follows (inference): embedding and clustering gives the more repeatable grouping, and a model is
better at naming groups and at assigning items to named themes. Repeated runs with a stability score
such as ARI show whether a set of themes holds before it is counted.

## 6. Questions that aggregate over a whole corpus (STABLE)

| Benchmark | What it tests | What it shows | Source |
| --- | --- | --- | --- |
| GlobalQA | Counting, extremum, sorting and top-k questions over a document collection | The best baseline (plain RAG) averaged F1 1.56, 1.43 and 1.51 on Qwen2.5 3B, 7B and 14B; all baselines averaged 0.09 to 1.56, with single tasks from 0.00 to 2.73. The authors' GlobalRAG reached 6.63 on 14B. Only these small backbones were tested | [chk-globalqa] |
| TAG-Bench | 80 questions over tables that need world knowledge or reasoning: 20 each of match-based, comparison, ranking and aggregation | Exact match overall: plain RAG 0.00, Text2SQL 0.17, Text2SQL with a model 0.13, hand-written TAG pipelines 0.55. RAG scored 0.00 on each scored type. Aggregation answers were not scored (the table marks them N/A); the authors analyse them by example and leave measurement to later work | [chk-tag] |
| GraphRAG-Bench | Fact retrieval, complex reasoning, contextual summarisation and creative generation, on a novel corpus and a medical corpus | [as-of 2026-10-28] Fact retrieval depended on the corpus and on reranking: on the novel corpus plain RAG scored 58.76, or 60.92 with reranking, against HippoRAG2 60.14 and MS-GraphRAG 49.29; on the medical corpus HippoRAG2 scored 66.28 against plain RAG 63.72, or 64.73 with reranking. Graph methods led on complex reasoning (novel: HippoRAG2 53.38 against 41.35, or 42.93 with reranking; medical: HippoRAG2 61.98 against 58.64 with reranking) and on summarisation accuracy (novel: MS-GraphRAG 64.40 against 50.08, or 51.30 with reranking; medical: Fast-GraphRAG 67.88 against 65.75 with reranking). No counting task | [chk-graphrag-bench] |
| WildGraphBench | 1,100 questions across 12 top-level Wikipedia topics: single-fact, multi-fact and section-level summaries | NaiveRAG 66.87 on single facts against HippoRAG2 71.51; on multi-fact questions MS GraphRAG (global) led at 47.64 against NaiveRAG 35.08; NaiveRAG had the best summary F1 (15.84) | [chk-wildgraph] |

All are M. What follows (inference): a corpus-wide count is not a retrieval question. The measured
alternatives either compute it over every item (a label or a query per item, then counting in code)
or use a structured store; graph retrieval helped multi-document questions in one benchmark but was
not tested on counting.

## 7. Zero-shot classification baselines (STABLE)

BTZSC compares 38 checkpoints on 22 public datasets of sentiment, topic, intent and emotion
classification, with no training on the tasks [chk-btzsc] (M):

- The best overall was a reranker, Qwen3-Reranker-8B, at macro F1 0.72; instruction-tuned LLMs of
  4B to 12B reached up to 0.67; embedding models gave the best accuracy for their latency.
- **Sentiment:** the best NLI cross-encoder, reranker, embedding model and instruction-tuned LLM
  reached 0.88 to 0.92; the best plain base encoder (bert-large-uncased) reached 0.38
  [as-of 2026-10-28].
- **Emotion:** the hardest family. The best models reached 0.44 to 0.51 (Qwen3-Embedding-8B 0.51,
  e5-mistral-7b-instruct 0.50, Qwen3-Reranker-8B 0.49, deberta-v3-large-nli 0.44); NLI
  cross-encoders ranged from 0.24 to 0.44 and instruction-tuned LLMs from 0.04 to 0.37.

No decision model is in BTZSC. On a 28-label emotion set (GoEmotions) in another benchmark, the best
model reached 45% accuracy, Jev 31% and GPT-6 Luna without thinking 34.5% [chk-arxiv-gdm]; see
[decision-models.md](decision-models.md) for that comparison.

## What the evidence supports (inference)

- A count or share from model labels is reported with a correction from a labelled sample and its
  interval, not as the raw count; this holds whatever model produced the labels.
- The size of the labelled sample follows from the interval the number needs and from how well the
  model predicts the label; a few hundred random items is the order of size the formulas give for
  ±5 points near 50%.
- A labelled sample is valid only for the population and the model version it was scored against.
- Theme discovery that people will compare over time needs a stability check between runs.
- Questions that count over a corpus are answered by computing over every item, not by retrieving a
  few passages.

## Limits and open questions

- No study read measures these estimators on short free-text labels from a decision model; the
  method papers use other tasks.
- The worked example in §3 applies the power-analysis rule of thumb; it is not a measurement.
- Run-to-run stability was measured on one corpus; TopicGPT and LLooM were not in that comparison.
- Several sources were read as abstracts only (LLooM, the comparison across political contexts, and
  the PPI, PPI++, stratified PPI, DSL, confidence-driven inference and power-analysis papers); their
  conditions and proofs were not checked here.
- The benchmark figures hold for the backbones and versions each paper ran.

## Sources

Read 2026-10-27, and read again on 2026-10-28 where marked. M unless marked. Claims tagged
`[as-of 2026-10-28]` were corrected against the sources read again on that day.

Estimators and label counts

- [chk-ppi] Angelopoulos, Bates, Fannjiang, Jordan and Zrnic, Prediction-Powered Inference, v4
  2023-11-09, abstract <https://export.arxiv.org/abs/2301.09633>.
- [chk-ppipp] Angelopoulos, Duchi and Zrnic, PPI++: Efficient Prediction-Powered Inference, v2
  2024-03-26, abstract <https://export.arxiv.org/abs/2311.01453>.
- [chk-stratppi] Fisch, Maynez, Hofer, Dhingra, Globerson and Cohen, Stratified Prediction-Powered
  Inference for Hybrid Language Model Evaluation, v2 2024-12-03, abstract
  <https://export.arxiv.org/abs/2406.04291>.
- [chk-dsl] Egami, Hinck, Stewart and Wei, Using Imperfect Surrogates for Downstream Inference:
  Design-based Supervised Learning for Social Science Applications of Large Language Models, NeurIPS
  2023, v3 2024-01-14, abstract <https://arxiv.org/abs/2306.04746>.
- [chk-cdi] Gligorić, Zrnic, Lee, Candès and Jurafsky, Can Unconfident LLM Annotations Be Used for
  Confident Conclusions?, NAACL 2025, v2 2025-02-08, abstract <https://arxiv.org/abs/2408.15204>.
- [chk-mixed] Broska, Howes and van Loon, The Mixed Subjects Design: Treating Large Language Models as
  Potentially Informative Observations, Sociological Methods & Research 54(3), 1074–1109, 2025,
  abstract <https://ideas.repec.org/a/sae/somere/v54y2025i3p1074-1109.html>.
- [chk-mixedsubjects-pkg] The R package `mixedsubjects` 1.0.0, package page
  <https://cran.r-universe.dev/mixedsubjects>, read 2026-10-28. L.
- [chk-pppower] Chen, Guo and Li, Power Analysis for Prediction-Powered Inference, 2026-03-17,
  abstract <https://export.arxiv.org/abs/2603.16041>; Propositions 1 and 3 and Corollary 4 read again
  on 2026-10-28 in <https://arxiv.org/html/2603.16041>.
- [chk-glide] Martinon, Merad and Raki, Industrializing Prediction-Powered Inference: The GLIDE
  Library, v1 2026-05-29 <https://arxiv.org/html/2605.31278v1> (M for the case study, L for the
  library's rules); section 2 read again on 2026-10-28.
- [chk-arxiv-gdm] Duan et al., General Decision Models: Benchmarking and Insights Beyond Jev, v2
  2026-10-12 <https://arxiv.org/html/2610.03935>; sections 5.1 and 5.4.3 read again on 2026-10-28.

Theme discovery

- [chk-topicgpt] Pham, Hoyle, Sun, Resnik and Iyyer, TopicGPT: A Prompt-based Topic Modeling
  Framework, NAACL 2024, abstract <https://export.arxiv.org/abs/2311.01449>.
- [chk-lloom] Lam, Teoh, Landay, Heer and Bernstein, Concept Induction: Analyzing Unstructured Text
  with High-Level Concepts Using LLooM, CHI 2024, abstract <https://export.arxiv.org/abs/2404.12259>.
- [chk-clio] Tamkin et al., Clio: Privacy-Preserving Insights into Real-World AI Use, 2024-12-18
  <https://arxiv.org/html/2412.13678>.
- [chk-wang-chen] Wang and Chen, Beyond Keywords: Comparing LLM-Assisted Topic Modeling Approaches
  Across Political Communication Contexts, Computational Communication Research 8(2), 2026-08-25,
  abstract <https://journal.computationalcommunication.org/article/view/9248>.
- [chk-doan] Doan, De Francisci Morales and Russo, Beyond the Rabbit Hole: Mapping the Relational
  Harms of QAnon Radicalization, v2, appendix A.2 <https://arxiv.org/html/2601.17658v2>.

Aggregation and classification benchmarks

- [chk-globalqa] Luo, Li, Fan, Chen and Qiu, Towards Global Retrieval Augmented Generation: A
  Benchmark for Corpus-Level Reasoning, v2 2025-11-04, Table 2 <https://arxiv.org/html/2510.26205>.
- [chk-tag] Biswal, Patel, Jha, Kamsetty, Liu, Gonzalez, Guestrin and Zaharia, Text2SQL is Not
  Enough: Unifying AI and Databases with TAG, 2024-08-27, Tables 1 and 2
  <https://arxiv.org/html/2408.14717>.
- [chk-graphrag-bench] Xiang, Wu, Zhang, Chen, Hong, Huang and Su, When to use Graphs in RAG: A
  Comprehensive Analysis for Graph Retrieval-Augmented Generation (GraphRAG-Bench), v3 2026-02-22,
  Table 2 read again on 2026-10-28,
  <https://arxiv.org/html/2506.05690>.
- [chk-wildgraph] Wang, Xu, Zhang, Wang, Du, Zhu and Mao, WildGraphBench: Benchmarking GraphRAG with
  Wild-Source Corpora, v2 2026-02-03, Table 2 <https://arxiv.org/html/2602.02053v2>.
- [chk-btzsc] Aarab, BTZSC: A Benchmark for Zero-Shot Text Classification Across Cross-Encoders,
  Embedding Models, Rerankers and LLMs, ICLR 2026, Table 2 read again on 2026-10-28
  <https://arxiv.org/html/2603.11991>.
