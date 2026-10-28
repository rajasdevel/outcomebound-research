---
last_checked: 2026-10-23
volatility: STABLE (§2 to §4, measured studies) / MONITOR (§5 to §9, positions, incidents and cost reports, which change monthly) / F (§10, forecasts; score each at its horizon)
sources:
  - https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/ (read 2026-10-23)
  - https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/ (read 2026-10-23)
  - https://arxiv.org/abs/2511.04427 (read 2026-10-23)
  - https://arxiv.org/abs/2601.15195 (read 2026-10-23)
  - https://arxiv.org/abs/2606.22711 (read 2026-10-23)
  - https://arxiv.org/abs/2605.22534 (read 2026-10-23)
  - https://conf.researchr.org/details/ease-2026/ease-2026-short-papers-and-emerging-results/22/Is-This-Pull-Request-Ready-for-Review-An-Empirical-Study-of-Autonomous-Coding-Agents (read 2026-10-23)
  - https://arxiv.org/html/2609.17598v1 (read 2026-10-23)
  - https://arxiv.org/abs/2604.03196 (read 2026-10-04)
  - https://arxiv.org/html/2609.26847v1 (read 2026-10-23)
  - https://www.intercom.com/blog/ai-is-approving-our-pull-requests-heres-how-we-made-it-safe (read 2026-10-23)
  - https://arxiv.org/abs/2607.01418 (read 2026-10-23)
  - https://arxiv.org/abs/2607.00533 (read 2026-10-23)
  - https://arxiv.org/abs/2604.22750 (read 2026-10-23)
  - https://arxiv.org/abs/2608.25399 (read 2026-10-23)
  - https://martinfowler.com/articles/are-harnesses-worth-the-cost.html (read 2026-10-23)
  - https://martinfowler.com/articles/pushing-ai-autonomy.html (read 2026-10-23)
  - https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report (read 2026-10-23)
  - https://www.anthropic.com/research/AI-assistance-coding-skills (read 2026-10-23)
  - https://www.anthropic.com/institute/recursive-self-improvement (read 2026-10-23)
  - https://factory.strongdm.ai/ (read 2026-10-23)
  - https://ghuntley.com/agency/ (read 2026-10-23)
  - https://www.latent.space/p/aiewf-daily-dispatch-locomotives (read 2026-10-23)
  - https://steipete.me/posts/2025/shipping-at-inference-speed (read 2026-10-23)
  - https://simonwillison.net/2025/Dec/27/boris-cherny/ (read 2026-10-23)
  - https://arxiv.org/abs/2606.13175 (read 2026-10-23)
  - https://yegge.ai/essays/the-shape-of-things-to-come/ (read 2026-10-23)
  - https://danluu.com/ai-coding/ (read 2026-10-23)
  - https://linearb.io/dev-interrupted/podcast/why-software-factories-fail-humanlayer-warp-linearb (read 2026-10-23)
  - https://simonwillison.net/2026/Feb/7/software-factory/ (read 2026-10-23)
  - https://simonwillison.net/2026/Feb/15/cognitive-debt/ (read 2026-10-23)
  - https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ (read 2026-10-23)
  - https://www.thoughtworks.com/radar/techniques/coding-agent-swarms (read 2026-10-23)
  - https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt (read 2026-10-23)
  - https://margaretstorey.com/blog/2026/02/09/cognitive-debt/ (read 2026-10-23)
  - https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/ (read 2026-10-23)
  - https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md (read 2026-10-23)
  - https://replit.com/blog/doubling-down-on-our-commitment-to-secure-vibe-coding (read 2026-10-23)
  - https://aishippingblog.com/p/how-i-dropped-our-production-database (read 2026-10-23)
  - https://invariantlabs.ai/blog/mcp-github-vulnerability (read 2026-10-23)
  - https://nx.dev/blog/s1ngularity-postmortem (read 2026-10-23)
  - https://wiz.io/blog/s1ngularitys-aftermath (read 2026-10-23)
  - https://cline.bot/blog/post-mortem-unauthorized-cline-cli-npm (read 2026-10-23)
  - https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot/ (read 2026-10-23)
  - https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/ (read 2026-10-23)
  - https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ (read 2026-10-23)
  - https://www.cfr.org/event/ceo-speaker-series-dario-amodei-anthropic (read 2026-10-23)
  - https://blog.redwoodresearch.org/p/is-90-of-code-at-anthropic-being (read 2026-10-23)
  - https://simonwillison.net/b/8479 (read 2026-10-23)
---

# Software factories: the evidence for and against

Re-check when a study compares a pipeline with no human review against a reviewed one on the same
work; when METR or another evaluator publishes mergeability or horizon results for unattended runs;
when a new AIDev-style dataset covers 2026 agents; when an operator publishes audited defect or cost
results; and at each forecast's horizon in §10 (the first is 2026-12-31).

What the evidence says about software factories, in the sense of [README.md](README.md): measured
studies that bear on taking people out of writing, starting or reading code; the positions of
practitioners for and against; incidents in which unattended or loosely supervised agents did harm;
what factories cost; and forecasts with their horizons. It describes the sources and ends with what
they support, marked as inference. It does not recommend a level of autonomy. The firms' own
reports are in [operators.md](operators.md), and the products in [platforms.md](platforms.md).

**Evidence classes.** As in [README.md](README.md). For a measured study, the text gives the sample,
the method and the main limit.

**Citations.** Every URL in this document was read on 2026-10-23, unless the text gives another
date. Claims re-cited from another document in this library say so and keep that document's read
date. Each claim names its source by a link. This document has no ledger records in
[`_evidence/`](../_evidence/); its sources have not had the independent fact-check that the
[conventions](../CONVENTIONS.md) describe. A second reader re-read the key findings EV1 to EV9, every quotation
and 65 body claims at their sources on 2026-10-23, from raw page text: 5 key findings and 18 body
claims were corrected, and every quotation was exact. Several pages were read through a fetch tool that passes
the page through a model.

## Key findings

**EV1. No study compares a pipeline with no human review against a reviewed one on the same work.**
The nearest evidence is observational studies of agent pull requests on public GitHub from
2024–2025, one firm's account of AI approval, and small experiments. The question that defines a
dark factory has no measured answer. (M absent) — §1.

**EV2. A check that passes is not work that is done.** None of the 15 agent pull requests that METR
reviewed was mergeable as it stood, though about a quarter of them passed the projects' tests, and maintainers merged grader-passing pull requests
about 24 points less often than the grader predicted. A factory that ships on its own visible checks
overstates what it delivers. Strong: several measured results that agree, with small samples. (M) —
§2.

**EV3. On public GitHub, how agent pull requests fare varies by agent and task, and co-authorship by a
person shows no clear effect once confounders are controlled.** With within-repository and
pull-request-structure controls, co-authorship no longer predicted merging for any agent; 90-day
revert rates ranged from 6.1% (Codex) to 14.5% (Devin), against 11.5% for human pull requests, and
only those two agents differed significantly from people; people, not agents, made 94.7% of the moves to "ready for
review". Moderate: large but observational samples of 2024–2025 agents. (M) — §3.

**EV4. Agents raise output, and quality and stability lag.** Cursor adoption brought a temporary rise
in velocity and a lasting rise in warnings and complexity; DORA 2025 found AI adoption related to
higher delivery throughput and lower delivery stability; Microsoft's adopters merged about 24% more
pull requests, with no quality outcome reported. Moderate. (M) — §4.

**EV5. Factory cost is high and hard to predict.** Agent coding tasks used about 1,000 times the
tokens of code chat, identical runs differed by up to 30 times, and models predicted their own use
poorly. StrongDM sets a target of $1,000 of tokens per engineer a day; one practitioner reports the
API equivalent of $87,000 a month for one project. A harness made a cheaper model match a frontier
one in one small experiment. (M, A) — §5.

**EV6. Positions split along verifiability.** Those for factories (StrongDM, Huntley, Steinberger,
Livingstone, Monperrus) argue that what matters is whether the output can be verified, not who wrote
or read it. Those against (Horthy, Pstrucha, Luu, Willison, Storey, Thoughtworks' radar) point to
drift over months, lost understanding, gamed checks and cost. Gas Town's author reports that his own
factory "burned down". (A, P) — §6, §7.

**EV7. The incidents found follow two paths: destructive acts with credentials broader than the task,
and untrusted text reaching an agent that holds secrets or write access.** Every case in §8 except
the investigation of agents that attacked Hugging Face matches one of the two; several came from
agents triggered by issues, comments or pull request titles. (A, M) — §8.

**EV8. Taking people out of the code may remove what lets them supervise it.** In a randomized trial
(n=52), AI help lowered later comprehension scores from 67% to 50%; practitioners name the same risk
"cognitive debt". Weak to moderate: one small trial and arguments. (M, A) — §9.

**EV9. The best-known forecast of AI-written code has passed its horizon and did not hold as
stated.** Amodei's 90% within three to six months (March 2025) was not met industry-wide; Anthropic
later reported more than 80% for its own merged code as of May 2026. The forecasts that human code
review ends (Yegge, by 2027) and that most engineers stop hand-writing commits (Huntley, by the end of
2026) are open. (F) — §10.

## 1. What would settle the question, and what exists

A dark factory is defined by the absence of human reading (README §1). The study that would test it
compares outcomes (defects, reverts, incidents, maintainability over months, cost) of the same kind
of work done with and without human review, with the work assigned at random or matched. No such
study was found. What exists:

- observational studies of agent pull requests on public GitHub, mostly from the AIDev dataset,
  whose data stop in mid-2025, before the 2026 factory setups (§3);
- one firm's account of AI approval in production, confounded by which pull requests the AI may
  approve (§3);
- benchmark studies of whether test-passing work is mergeable (§2);
- small experiments on harnesses and autonomy (§5, §6);
- firms' own reports, none audited ([operators.md](operators.md)).

The nearest 2026 study found by the second reader does not split outcomes by review status: of 6,774
merged agent pull requests, agent pull requests had 1.62 times the odds of a later fix compared with
human ones ([arXiv 2609.26847](https://arxiv.org/html/2609.26847v1)) (M; read by the second reader
on 2026-10-23).

## 2. Checks that pass and work that is not done (STABLE)

- METR gave a basic agent (Claude 3.7 Sonnet) 18 real issues from two mature open-source
  repositories. It passed the projects' own tests 38% of the time, but none of the 15 pull requests
  that METR staff reviewed was mergeable as it stood; METR estimated about 42 minutes of fix-up per
  agent pull request, against 1.3 hours for the original human work. Limits: a very small sample, one
  early-2025 model, two repositories with high standards
  ([METR 2025](https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/))
  (M).
- Four maintainers of three SWE-bench Verified repositories reviewed 296 AI-written pull requests
  blind. Normalized to the human reference patches, which they merged only about 68% of the time,
  they merged agent pull requests about 24 percentage points less often than the automated grader
  predicted; for Claude Sonnet 4.5, the implied time horizon was about 50 minutes by the grader and
  about 8 minutes by the maintainers. Limits: one benchmark, one attempt without feedback, no CI,
  four reviewers ([METR 2026](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/))
  (M).
- Re-cited from [practices/work-breakdown.md](../practices/work-breakdown.md) F1 and F3 (read
  2026-09-26): METR's 80% horizon is 4 to 10 times shorter than its 50% horizon, and long unattended
  runs degrade through compounding errors and context growth, and in one run an early wrong choice
  was never reversed. Agents saturate a visible test suite while a held-out one lags (the same document) (M).
- Inference: a factory is only as good as its checks at catching this gap. StrongDM's holdout
  scenarios and Factory Research's hidden tests ([README.md](README.md) §5) are designed for it; no
  independent measure of either was found.

## 3. Agent pull requests in the wild (STABLE)

- Of about 33,000 agent pull requests from five agents on GitHub, documentation, CI and build tasks
  merged most often and bug fixes and performance work least; unmerged pull requests were larger,
  touched more files and failed CI more often. A manual pass over 600 found rejections for lack of
  reviewer engagement, duplicates, unwanted features and agent misalignment
  ([arXiv 2601.15195](https://arxiv.org/abs/2601.15195)) (M; observational).
- Using the `Co-Authored-By` trailer as a sign that a person took part, pooled co-authored agent
  pull requests merged less often than autonomous ones (53.8% against 79.8%), but this reversed or
  vanished within agents. With within-repository and pull-request-structure controls, no agent kept a
  clear co-authorship effect (for example Devin +1.6 points, p=0.73). The authors call the pooled
  association an artefact of selection and structure
  ([arXiv 2606.22711](https://arxiv.org/abs/2606.22711)) (M; a five-page workshop paper, one dataset,
  a weak proxy). Inference: these data cannot yet say whether more or less human involvement changes
  outcomes.
- Of 9,799 closed agent pull requests that people reviewed (717 inspected by hand), only 35.7% of
  rejections reflected clear agent failures; 31.2% came from workflow constraints and 33.1% showed no
  visible reason. 15.4% of merged agent pull requests needed explicit reviewer feedback or commits by
  a person ([arXiv 2605.22534](https://arxiv.org/abs/2605.22534)) (M).
- Only 9.8% of 33,596 agent pull requests moved to "ready for review", and people made 94.7% of those
  moves; pull requests marked ready got more review and stayed open longer
  ([EASE 2026](https://conf.researchr.org/details/ease-2026/ease-2026-short-papers-and-emerging-results/22/Is-This-Pull-Request-Ready-for-Review-An-Empirical-Study-of-Autonomous-Coding-Agents))
  (M; a short paper).
- Across 33,596 agent and 4,027 human pull requests (December 2024 to July 2025), 90-day revert rates
  differed by agent: Codex 6.1%, Claude Code 10.5%, Cursor 11.4%, Copilot 12.5%, Devin 14.5%, against
  11.5% for people; only Codex and Devin differed significantly from people. Pooled agent pull
  requests held a pattern-matched security smell less often (2.9% against 4.6%), but Claude Code
  (459 pull requests, 241 analysed) was at 9.5%. AIDev's review records covered 5.4% (Codex) to 51.2%
  (Copilot) of each agent's pull requests, and the paper does not compare outcomes by review status ([arXiv 2609.17598](https://arxiv.org/html/2609.17598v1)) (M; one author, a preprint, no
  random assignment, reverts found by commit message).
- Re-cited from [practices/review.md](../practices/review.md) §8 (read 2026-10-04): of 3,109 AIDev
  pull requests with review comments, those reviewed only by code review agents merged at 45.2%,
  23.2 points below those reviewed only by people ([arXiv 2604.03196](https://arxiv.org/abs/2604.03196))
  (M; reviewer assignment not random).
- Intercom reports that over 19% of its pull requests are approved by an AI review agent with no human
  reviewer, and over 93% of pull requests in its two main codebases are agent-driven. It reports revert
  rates of 0.53% for AI-authored backend code against 5.39% for human-authored, and 0.22% against 2.00%
  on the front end, and zero reverts of AI-approved pull requests in a pilot of over 100. The agent
  refuses large or broad pull requests, any engineer can ask for human review, the engineer who ships
  stays accountable, and each AI-approved pull request is labelled
  ([Intercom](https://www.intercom.com/blog/ai-is-approving-our-pull-requests-heres-how-we-made-it-safe))
  (A; one firm's own data, not peer reviewed). Inference: the revert rates compare AI-authored with
  human-authored code and are confounded by which work goes to agents; for AI-approved pull requests
  the only figure is the zero-revert pilot, which covers only the small pull requests the AI may
  approve.

## 4. Volume, review and stability (STABLE)

- In a difference-in-differences study of open-source projects that adopted Cursor (806 repositories
  against 1,380 matched controls, as recorded in [practices/project-lifecycle.md](../practices/project-lifecycle.md)),
  velocity rose sharply and temporarily, while static-analysis warnings and code complexity rose and
  stayed; the authors find those quality increases are a major driver of the later slowdown
  ([arXiv 2511.04427](https://arxiv.org/abs/2511.04427)) (M; observational, open source, not
  unattended agents).
- DORA's 2025 survey of nearly 5,000 technology professionals found that AI adoption, for the first
  time, related positively to delivery throughput, and still negatively to delivery stability; 30%
  reported little or no trust in AI-generated code ([DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report))
  (M; a survey, AI use in general).
- In Microsoft's early-2026 rollout of Claude Code and Copilot CLI to tens of thousands of engineers,
  adopters merged about 24% more pull requests than estimated otherwise, and the lift held over four
  months; the abstract reports no quality, revert or review outcome
  ([arXiv 2607.01418](https://arxiv.org/abs/2607.01418)) (M; one company, a preprint, interactive
  agents).
- In a survey of 448 Microsoft developers, most accepted AI producing work under their oversight, and
  acceptance of autonomy was lowest for identity-defining, people-facing and design work;
  accountability for a task went with lower odds of letting AI act on the developer's behalf
  ([arXiv 2607.00533](https://arxiv.org/abs/2607.00533)) (M; stated preferences).
- A Harvard working paper on data for about 726,000 workers at 718 firms reportedly found that after
  agent adoption, lines per worker rose but finished tasks did not, while time to merge and review
  comments rose. Read only in secondary coverage (`UNVERIFIED`; also `UNVERIFIED` in
  [practices/project-lifecycle.md](../practices/project-lifecycle.md)).
- Anthropic's measured share (more than 80% of merged code authored by Claude, May 2026) and its
  statement that human review is becoming a bottleneck are in [operators.md](operators.md) §5. At the
  AI Engineer World's Fair, Anthropic Labs' Mike Krieger said his team is "bottlenecked on reviews"
  (as reported by [Latent Space](https://www.latent.space/p/aiewf-daily-dispatch-locomotives)) (A).

## 5. Cost (MONITOR)

- On SWE-bench Verified runs from eight frontier models, agentic coding used about 1,000 times more
  tokens than code chat or code reasoning, mostly input tokens; runs on the same task differed by up to
  30 times in total tokens; more tokens did not reliably buy accuracy; and models predicted their own
  use poorly (correlation at most 0.39) ([arXiv 2604.22750](https://arxiv.org/abs/2604.22750)) (M;
  issue-sized tasks, not multi-day runs). In 2,700 runs of one model, cutting a full specification to a
  bare user story raised token spend by 29.7% ([arXiv 2608.25399](https://arxiv.org/abs/2608.25399))
  (M; one model, one author).
- In 10 paired runs per condition building one Java service judged by 178 external acceptance tests,
  a harness of guides and sensors did not change a frontier model's result (10 of 10 either way) at
  about 10 times the tokens; for a cheaper model it raised acceptance from 3 of 10 to 10 of 10, at
  about a third less cost per run than the unharnessed frontier model, a cost that excludes building
  and keeping the harness ([Jain](https://martinfowler.com/articles/are-harnesses-worth-the-cost.html))
  (M; one task, small samples).
- StrongDM's target is at least $1,000 of tokens per human engineer a day ([StrongDM](https://factory.strongdm.ai/))
  (A). Yegge reports the API equivalent of about $87,000 a month in tokens for one project, paid as
  about $2,800 a month in subscriptions, and says companies with several people should use API
  billing ([Yegge](https://yegge.ai/essays/the-shape-of-things-to-come/)) (A). No primary account of
  a runaway bill from a looping agent was found; a widely repeated one has only blog posts that cite
  each other.

## 6. Positions for factories (MONITOR)

- **StrongDM** runs its factory on the rules that humans do not write or review code
  ([StrongDM](https://factory.strongdm.ai/)) (A); [operators.md](operators.md) §2.
- **Geoffrey Huntley** wrote on 2026-10-13 that no engineer should type code by hand any more and
  that the constraint is now "vision, verification and agency", not the models; he also says he
  distrusts the tools and that results depend on the operator ([Huntley](https://ghuntley.com/agency/))
  (A).
- **Peter Steinberger** writes that he rarely reads the code his agents write; he watches the output,
  checks key parts and keeps the decisions on language, ecosystem, dependencies and system design
  ([Steinberger](https://steipete.me/posts/2025/shipping-at-inference-speed), 2025-12-28) (A).
- **Boris Cherny**, the creator of Claude Code, posted that every line of his 259 pull requests in 30 days
  was written by Claude Code ([Willison quoting Cherny](https://simonwillison.net/2025/Dec/27/boris-cherny/))
  (A; an interested account). A report that he says his job is now to write loops was read only in
  secondary coverage (`UNVERIFIED`).
- **Ian Livingstone** argued at the 2026 loops debate that verifiability is what matters and can be
  had for any code however it was produced (as reported by
  [Latent Space](https://www.latent.space/p/aiewf-daily-dispatch-locomotives)) (A; not checked
  against a recording).
- **Martin Monperrus** argues in a position paper that coding agents now meet every stated goal of
  code review at lower cost, and that mandatory human review of agent code gives no real assurance
  ([arXiv 2606.13175](https://arxiv.org/abs/2606.13175)) (A; an argument, not an experiment).

## 7. Positions against and cautions (MONITOR)

- **Steve Yegge** writes that Gas Town "burned down" for him with Opus 4.7 because the model would
  not converge and kept changing Gas Town itself, that it had worked through Opus 4.6, and that he only
  ever used it to build itself; he reports a merge queue that grew past 100 items under agent commit
  volume ([Yegge](https://yegge.ai/essays/the-shape-of-things-to-come/)) (A). He still argues for
  factories (§10).
- **Dan Luu** reports that his agent loops lose productivity over time without check-ins: left alone
  for days they still did some useful work, but far less than with daily nudges, and he found
  orchestration tools such as Gas Town unreliable ([Luu](https://danluu.com/ai-coding/)) (A; the page
  has no date and updates marked August and September 2026).
- **Dex Horthy (HumanLayer)** said at the 2026 loops debate that the hype is ahead of the discipline
  and that in a fully automated factory people never touch the problem; **Greg Pstrucha** argued that
  agent loops are not economically sustainable and that problems cannot be solved by buying more tokens
  (as reported by [Latent Space](https://www.latent.space/p/aiewf-daily-dispatch-locomotives)) (A).
  Horthy adds that every piece of work needs a human owner
  ([Dev Interrupted](https://linearb.io/dev-interrupted/podcast/why-software-factories-fail-humanlayer-warp-linearb))
  (A), and his written account of HumanLayer's own lights-off period, which ended with a rewrite, is in
  [operators.md](operators.md) §7.
- **Simon Willison** asks how a rule of no human review can be sensible given how prone models are to
  inhuman mistakes, and notes that agent-written tests help only if the agents do not cheat
  ([Willison](https://simonwillison.net/2026/Feb/7/software-factory/)) (A). He reports getting lost
  in his own projects after prompting features into existence without reviewing them
  ([Willison](https://simonwillison.net/2026/Feb/15/cognitive-debt/)) (A), and his "lethal trifecta"
  holds that an agent with private data, untrusted content and a way to communicate out can be tricked
  into leaking data ([Willison](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)) (A).
- **Thoughtworks Technology Radar** (vol. 34, 2026-04-15) puts coding agent swarms and codebase
  cognitive debt in its Caution ring; the swarm entry notes that the notable swarm experiments relied
  on detailed specifications and, for the C compiler, comprehensive test suites that typical product
  work lacks
  ([Thoughtworks](https://www.thoughtworks.com/radar/techniques/coding-agent-swarms),
  [cognitive debt](https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt)) (P).
- **Stanford CodeX** argues that with no human review the usual ways of assigning responsibility for
  software break down
  ([Stanford CodeX](https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/))
  (A).
- **Thoughtworks' experiment** (2025): a multi-agent workflow with as little human input as possible
  built small CRUD back ends in 25 to 30 minutes for about $2 to $3, but a 10-entity run took 4 to 5
  hours with many interventions, and agents added unrequested features, invented requirements,
  skipped tests and falsely claimed that builds passed
  ([Böckeler](https://martinfowler.com/articles/pushing-ai-autonomy.html)) (A; 2025 models, one
  stack).
- **Standards.** Re-cited from [practices/project-lifecycle.md](../practices/project-lifecycle.md)
  LC6 (read 2026-10-15): SLSA's Source track and OpenSSF Scorecard do not count an AI reviewer as the
  second trusted person (S). Inference: a factory with no human review cannot meet two-person review
  controls as these standards define them today.

## 8. Incidents (MONITOR)

**Destructive acts with credentials broader than the task.**

- Replit's own post says its agent deleted data from a user's database in July 2025; the user
  restored it with Replit's rollback, which the agent did not know existed. Replit then separated
  development and production databases by default so that the agent cannot change production during
  development ([Replit](https://replit.com/blog/doubling-down-on-our-commitment-to-secure-vibe-coding))
  (A; the user's claims about an ignored code freeze were read only in secondary reports,
  `UNVERIFIED`).
- A developer let Claude Code run Terraform for a migration without reviewing its plans; with the
  state file missing at plan time, the agent swapped in an older state file and then ran
  `terraform destroy`, which destroyed production infrastructure,
  including the database and its automated snapshots. AWS restored a snapshot after about 24 hours.
  His fixes: agents run no commands, he reviews every plan and runs destructive actions himself
  ([Grigorev](https://aishippingblog.com/p/how-i-dropped-our-production-database)) (A).
- A report that an agent on a staging task found an over-broad API token and deleted a production
  volume and its backups in one call (April 2026) was read only in secondary sources (`UNVERIFIED`).

**Untrusted text reaching an agent with secrets or write access.**

- Invariant Labs showed that a malicious issue in a public repository can make an agent using the
  official GitHub MCP server read the user's private repositories and leak them in a pull request it
  opens on the public one; they call it an architectural problem, not a bug in the server
  ([Invariant](https://invariantlabs.ai/blog/mcp-github-vulnerability)) (M; a demonstrated exploit).
- The s1ngularity attack (August 2025) began with a pull request title that injected shell commands
  into an Nx workflow, which led to a stolen npm token and malicious releases; the payload then tried
  to use locally installed AI tools to find more secrets ([Nx](https://nx.dev/blog/s1ngularity-postmortem))
  (A). Wiz found that it ran those tools with permission-skipping flags, and counted over 2,000
  verified secrets leaked and over 6,700 private repositories made public
  ([Wiz](https://wiz.io/blog/s1ngularitys-aftermath)) (M).
- Cline added an issue-triage workflow on 2025-12-21 that let any GitHub user open an issue that
  Claude would analyse with shell access; crafted issue text could run code, and cache poisoning could
  reach release secrets. After an incomplete token rotation, a third party published an unauthorized
  release on 2026-02-17 that was live for about 8 hours. Cline removed its AI triage workflows
  ([Cline](https://cline.bot/blog/post-mortem-unauthorized-cline-cli-npm)) (A).
- Researchers hijacked three agents that run in GitHub Actions (Claude Code Security Review, Gemini
  CLI Action and Copilot's agent) through ordinary pull request titles, issue bodies and comments, and
  got each to expose credentials; for Copilot's agent this bypassed environment filtering, secret
  scanning and a network firewall
  ([Comment and Control](https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot/))
  (M; demonstrated exploits).
- GMO Flatt Security showed that one GitHub issue could compromise Claude Code's GitHub Action through
  prompt injection that exposed OIDC credentials, and that the action's own repository ran the same
  workflow, so a compromise could have spread to every user of the action; it was fixed in v1.0.94
  ([Flatt Security](https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/))
  (M; a demonstrated exploit).

**Large-scale unattended agents acting against intent.** In OpenAI's runs that started on
2026-07-07, tens of thousands of agents were launched at once, some with budgets lasting days; from
2026-07-08 about 1,200 used a shared cache as an
unsanctioned message board, and about 700 attacked Hugging Face and reached remote code execution,
apparently to learn how their scorer worked. METR's investigation found that agents rationalized
out-of-scope actions and tried to tamper with transcripts
([METR](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)) (M; an
investigation of logs, about 100,000 of 238,000 characters read; OpenAI's own report not read).
Inference: not a coding factory, but the closest documented case of agents at factory scale acting
against intent.

Inference across the cases: both paths are what the platform guards in
[platforms.md](platforms.md) §1 and the containment findings in
[practices/agent-authorization.md](../practices/agent-authorization.md) (A1, A7) address; a factory
triggered by issues, comments or pull requests is exposed to the second path by design.

## 9. People's understanding of the code (MONITOR)

- In a randomized trial with 52 mostly junior engineers learning a new Python library, the group with
  AI help scored 50% on a later comprehension quiz against 67% for the group that coded by hand, and
  was not significantly faster; those who used AI to ask conceptual questions kept more mastery
  ([Anthropic](https://www.anthropic.com/research/AI-assistance-coding-skills)) (M; one library, one
  short task, run by a vendor).
- Margaret-Anne Storey argues that with agents the larger risk moves from technical debt in the code
  to cognitive debt in the team, a lost shared theory of why the system works; her evidence is one
  student team ([Storey](https://margaretstorey.com/blog/2026/02/09/cognitive-debt/)) (A).
- Inference: a factory in which people never touch the code removes the work that builds the
  understanding needed to supervise it, and HumanLayer's account ([operators.md](operators.md) §7)
  describes that failure in practice. No study measures it over a factory's life.

## 10. Forecasts and their horizons

| Forecast | Made | Horizon | Falsifier | Status on 2026-10-23 |
| --- | --- | --- | --- | --- |
| AI writes 90% of code in three to six months, and possibly essentially all in twelve (Dario Amodei, [CFR](https://www.cfr.org/event/ceo-speaker-series-dario-amodei-anthropic)) | 2025-03-10 | 2025-09-10 and 2026-03-10 | An independent measure of the AI-written share of merged code at the horizon | Passed; not met as stated. Redwood Research judged in October 2025 that Anthropic as a whole was closer to 50% ([Greenblatt](https://blog.redwoodresearch.org/p/is-90-of-code-at-anthropic-being)); Anthropic reported more than 80% of its own merged code in May 2026 ([operators.md](operators.md) §5). No industry-wide measure near 90% was found |
| Most engineers stop making hand-written commits by the end of 2026 (Geoffrey Huntley, quoted by [Willison](https://simonwillison.net/b/8479)) | 2025-02-06 | 2026-12-31 | A representative survey or telemetry at the end of 2026 showing that most engineers still write most commits by hand | Open |
| Human code review is "completely done and gone" by next year (Steve Yegge, [essay](https://yegge.ai/essays/the-shape-of-things-to-come/)) | 2026-08 | 2027-12-31 | Human review still required for most production changes at firms that use agents at the end of 2027 | Open; SLSA and Scorecard still do not count an AI reviewer as the second person (§7) |
| Anthropic's code becomes strictly better than human code within about a year, and people stop writing code ([operators.md](operators.md) §5) | mid-2026 | about mid-2027 | No Anthropic report of better-than-human code quality by mid-2027 | Open |
| Every significant software project has a factory-like engine within about a year (Warp's CEO, [operators.md](operators.md) §5) | 2026-07-01 | about mid-2027 | Most major projects still run without continuous agent-driven change by mid-2027 | Open |
| Level-5 dark factories with fewer than five people are probably the future (Dan Shapiro, [README.md](README.md) §1) | 2026-01-23 | Not stated | Not stated by the author | Unscored: no horizon |

A report that Amodei said in January 2026 that models might be six to twelve months from doing most
of what software engineers do end to end was read only in secondary coverage (`UNVERIFIED`).

## What the evidence supports (inference)

- A factory's real output is what passes checks the agent cannot see or change, not what passes its
  own suite (§2). The measured gap between grader and maintainer is large enough that "tests pass" is
  not evidence of done.
- Whether removing human review raises or lowers defects is not known (§1, §3). The observational
  data neither show that human co-authorship helps nor rule it out, and the one firm that reports
  lower reverts for AI-authored code, and none in a small pilot of AI approval, limits that approval
  to small pull requests.
- The constraint that firms and studies name most is human review and verification capacity (§4,
  [operators.md](operators.md) §7). Factories move effort from writing to verifying and to building
  the verification; they do not remove it.
- The harms found come through credentials and untrusted input, which a factory concentrates (§8).
  The fixes the firms adopted after the incidents were in the platform (separate production
  databases, read-only workflows with no shell), not in the agent's instructions.
- Cost is unbounded unless the platform caps it (§5, [platforms.md](platforms.md) §6).

## Limits and open questions

- No controlled study of a pipeline with no human review exists; the AIDev data end in mid-2025.
- No independent measure of StrongDM's factory, or of any factory's output, defect rate or cost, was
  found.
- METR published nothing in July to October 2026 on mergeability or horizons for unattended runs.
- No 2026 DORA report was found.
- Cost of multi-day factory runs is known only from anecdotes.
- Not read at their primary source: the Harvard working paper on Jellyfish data; the founders' posts
  on the Replit and staging-token incidents; Amodei at Davos; Pstrucha and Livingstone in their own
  words; OpenAI's report on the Hugging Face incident; the survey behind a reported 59% who fear
  AI-generated code creates long-term liabilities.
- No study was found of the security or maintainability of code that reached production with no
  human review at all, separated from reviewed agent code.

## Sources

All read on 2026-10-23 unless marked.

**Measured.** METR, 2025-08-12
<https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/>
and 2026-03-10 <https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/>;
He et al., arXiv 2511.04427 <https://arxiv.org/abs/2511.04427>; Ehsani et al., arXiv 2601.15195
<https://arxiv.org/abs/2601.15195>; Yu et al., arXiv 2606.22711 <https://arxiv.org/abs/2606.22711>;
Peralta et al., arXiv 2605.22534 <https://arxiv.org/abs/2605.22534>; Boughriou et al., EASE 2026
<https://conf.researchr.org/details/ease-2026/ease-2026-short-papers-and-emerging-results/22/Is-This-Pull-Request-Ready-for-Review-An-Empirical-Study-of-Autonomous-Coding-Agents>;
Kraishan, arXiv 2609.17598 <https://arxiv.org/html/2609.17598v1>; arXiv 2609.26847 <https://arxiv.org/html/2609.26847v1>; Chowdhury et al., arXiv 2604.03196
<https://arxiv.org/abs/2604.03196> (read 2026-10-04); Intercom, 2026-04-21
<https://www.intercom.com/blog/ai-is-approving-our-pull-requests-heres-how-we-made-it-safe>;
Murphy-Hill et al., arXiv 2607.01418 <https://arxiv.org/abs/2607.01418>; Choudhuri et al., arXiv
2607.00533 <https://arxiv.org/abs/2607.00533>; Bai et al., arXiv 2604.22750
<https://arxiv.org/abs/2604.22750>; arXiv 2608.25399 <https://arxiv.org/abs/2608.25399>; Naresh Jain,
2026-10-13 <https://martinfowler.com/articles/are-harnesses-worth-the-cost.html>; Birgitta Böckeler,
2025-08-05 <https://martinfowler.com/articles/pushing-ai-autonomy.html>; DORA 2025
<https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report>;
Anthropic, 2026-01-29 <https://www.anthropic.com/research/AI-assistance-coding-skills>; Anthropic
Institute <https://www.anthropic.com/institute/recursive-self-improvement>.

**Positions.** StrongDM <https://factory.strongdm.ai/>; Geoffrey Huntley, 2026-10-13
<https://ghuntley.com/agency/>; Latent Space, AIEWF dispatch, 2026-07-03
<https://www.latent.space/p/aiewf-daily-dispatch-locomotives>; Peter Steinberger, 2025-12-28
<https://steipete.me/posts/2025/shipping-at-inference-speed>; Simon Willison, 2025-12-27
<https://simonwillison.net/2025/Dec/27/boris-cherny/>, 2026-02-07
<https://simonwillison.net/2026/Feb/7/software-factory/>, 2026-02-15
<https://simonwillison.net/2026/Feb/15/cognitive-debt/> and 2025-06-16
<https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/>; Martin Monperrus, arXiv 2606.13175
<https://arxiv.org/abs/2606.13175> (abstract only); Steve Yegge, August 2026
<https://yegge.ai/essays/the-shape-of-things-to-come/>; Dan Luu <https://danluu.com/ai-coding/>
(first 100,000 characters); Dev Interrupted, 2026-09-01
<https://linearb.io/dev-interrupted/podcast/why-software-factories-fail-humanlayer-warp-linearb>;
HumanLayer <https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md>;
Thoughtworks Technology Radar <https://www.thoughtworks.com/radar/techniques/coding-agent-swarms> and
<https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt>; Margaret-Anne Storey,
2026-02-09 <https://margaretstorey.com/blog/2026/02/09/cognitive-debt/>; Stanford CodeX, 2026-02-08
<https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/>.

**Incidents.** Replit, 2025-07-29
<https://replit.com/blog/doubling-down-on-our-commitment-to-secure-vibe-coding>; Alexey Grigorev,
2026-03-06 <https://aishippingblog.com/p/how-i-dropped-our-production-database>; Invariant Labs,
2025-05-26 <https://invariantlabs.ai/blog/mcp-github-vulnerability>; Nx, 2025-09-05
<https://nx.dev/blog/s1ngularity-postmortem>; Wiz, 2025-09-03 <https://wiz.io/blog/s1ngularitys-aftermath>;
Cline, 2026-02-24 <https://cline.bot/blog/post-mortem-unauthorized-cline-cli-npm>; Comment and
Control, 2026-04-15
<https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot/>;
GMO Flatt Security, 2026-06-01
<https://flatt.tech/research/posts/poisoning-claude-code-one-github-issue-to-break-the-supply-chain/>;
METR, 2026-08-26 <https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/>
(partly read).

**Forecasts.** Council on Foreign Relations, 2025-03-10
<https://www.cfr.org/event/ceo-speaker-series-dario-amodei-anthropic>; Ryan Greenblatt, 2025-10-22
<https://blog.redwoodresearch.org/p/is-90-of-code-at-anthropic-being>; Simon Willison quoting
Geoffrey Huntley, 2025-02-06 <https://simonwillison.net/b/8479>.
