---
last_checked: 2026-10-15
volatility: MONITOR (maker guidance on agents, platform features and the status of drafts change monthly) / STABLE (§2, the measured studies and surveys) / VOLATILE (§6, plan costs on GitHub; §7, dates of laws, drafts and editions)
sources:
  - https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report (read 2026-10-15)
  - https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model (read 2026-10-15)
  - https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report (read 2026-10-15)
  - https://dora.dev/capabilities/working-in-small-batches/ (read 2026-10-15)
  - https://dora.dev/capabilities/trunk-based-development/ (read 2026-10-15)
  - https://dora.dev/capabilities/documentation-quality/ (read 2026-10-15)
  - https://dora.dev/capabilities/streamlining-change-approval/ (read 2026-10-15)
  - https://dora.dev/guides/dora-metrics-four-keys/ (read 2026-10-15)
  - https://dora.dev/publications/pdf/state-of-devops-2019.pdf (read 2026-10-15)
  - https://sre.google/sre-book/embracing-risk/ (read 2026-10-15)
  - https://sre.google/sre-book/release-engineering/ (read 2026-10-15)
  - https://abseil.io/resources/swe-book/html/ch01.html (read 2026-10-15)
  - https://abseil.io/resources/swe-book/html/ch09.html (read 2026-10-15)
  - https://abseil.io/resources/swe-book/html/ch16.html (read 2026-10-15)
  - https://rebels.cs.uwaterloo.ca/confpaper/2014/05/30/the-impact-of-code-review-coverage-and-code-review-participation-on-software-quality.html (read 2026-10-15)
  - https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ (read 2026-10-15)
  - https://metr.org/blog/2026-02-24-uplift-update/ (read 2026-10-15)
  - https://arxiv.org/abs/2511.04427 (read 2026-10-15)
  - https://arxiv.org/abs/2601.15195 (read 2026-10-15)
  - https://arxiv.org/abs/2607.07980 (read 2026-10-15)
  - https://arxiv.org/abs/2602.11988 (read 2026-10-15)
  - https://arxiv.org/abs/1609.04886 (read 2026-10-15)
  - https://arxiv.org/abs/1604.06766 (read 2026-10-15)
  - https://arxiv.org/abs/1906.08058 (read 2026-10-15)
  - https://code.claude.com/docs/en/best-practices (read 2026-10-15)
  - https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations (read 2026-10-15)
  - https://github.blog/changelog/2026-09-01-copilot-code-review-can-now-approve-pull-requests (read 2026-10-15)
  - https://www.anthropic.com/engineering/claude-code-auto-mode (read 2026-10-15)
  - https://csrc.nist.gov/projects/ssdf/publications (read 2026-10-15)
  - https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218r1.ipd.pdf (read 2026-10-15)
  - https://slsa.dev/spec/v1.2/build-track-basics (read 2026-10-15)
  - https://slsa.dev/spec/v1.2/source-requirements (read 2026-10-15)
  - https://github.com/ossf/scorecard/blob/main/docs/checks.md (read 2026-10-15)
  - https://baseline.openssf.org/versions/2026-08-28 (read 2026-10-15)
  - https://docs.github.com/en/get-started/learning-about-github/githubs-plans (read 2026-10-15)
  - https://digital-strategy.ec.europa.eu/en/policies/cra-summary (read 2026-10-15)
  - https://digital-strategy.ec.europa.eu/en/policies/cra-open-source (read 2026-10-15)
  - https://artificialintelligenceact.eu/article/4/ (read 2026-10-15)
  - https://artificialintelligenceact.eu/article/17/ (read 2026-10-15)
  - https://webstore.iec.ch/en/publication/6792 (read 2026-10-15)
  - https://www.enisa.europa.eu/sites/default/files/2026-09/ENISA%20Technical%20Advisory-AI-assisted-software-development-draft.pdf (read 2026-10-15)
---

# Project lifecycles: what should change with a project's situation, and with coding agents

Re-check when DORA publishes a new report; METR or another group publishes a controlled study of
agent-assisted delivery; NIST publishes the final SSDF 1.2; IEC 62304 edition 2 is published; the
EU sets new dates for the AI Act's high-risk duties; the CRA's main obligations apply
(11 December 2027); or GitHub changes which plans carry branch protection, secret scanning or AI
approvals (§6, §7). The VOLATILE sections are worth a new reading at the source before any
load-bearing use.

Which facts about a software project change the delivery lifecycle it needs, what measured studies
say about delivery practice, what coding agents change at each stage, how review works when agents
write the code, which practices the sources support at every scale, what supply-chain basics cost,
and where standards and laws apply.

This reference is for anyone who designs, chooses or judges a lifecycle for a software project:
which facts about the project the sources treat as drivers, what measured delivery evidence and
agent-era evidence say, what the makers of coding agents and the standards bodies require or
advise, and what the evidence does not cover. It describes the sources. It does not choose a
lifecycle. Review of agent work in more depth is in [review.md](review.md); the size of a unit of
agent work is in [work-breakdown.md](work-breakdown.md); instruction files are in
[writing-for-models.md](writing-for-models.md); permissions and sandboxes are in
[agent-authorization.md](agent-authorization.md).

**Evidence classes.** (M) measured: an experiment, telemetry, repository mining or a survey with a
counted sample; a vendor's own measure of its own product is (M, vendor), and a survey's results
are associations, not causes. (L) the guidance or documentation of a model lab, a tool vendor or a
platform, including Google's books on its own engineering practice and DORA's advice. (P)
practitioner consensus. (A) one person's or one firm's account, or a framework that its authors did
not test against data. (S) the text of a standard, a law or a regulator's or public agency's
guidance; a law read through an unofficial copy says so. (F) forecast. (O) own result; this
document has none. "Inference" marks a step that no source states in words. `UNVERIFIED` marks a
claim that was read only in a secondary source or a search summary, not at its primary source.

**Citations.** Every URL in this document was read on 2026-10-15, unless the text gives another
date. Each claim names its source by a link. This document has no ledger records in
[`_evidence/`](../_evidence/); its sources have not had the independent fact-check that the
[conventions](../CONVENTIONS.md) describe.

## Key findings

**LC1. The sources that describe how a lifecycle should vary use several independent facts, not
one scale.** Cockburn uses team size and criticality; Boehm uses seven home-ground axes; Clarke and
O'Connor list 44 situational factors. Under 15% of 556 survey data points ran a purely traditional
or purely agile method, and the choice of practices affected agility more than the choice of method.
Weak to moderate: the frameworks are not tested against data; one survey. (A, M) — §1.

**LC2. Industry and company size are weak selectors.** DORA's 2019 survey found no effect of
industry on delivery performance except retail, which did better; organizations with more than
5,000 employees did worse. Respondents who needed approval from an external body were 2.6 times more
likely to be low performers, with no evidence of a lower change fail rate. Moderate: a large survey,
correlational. (M) — §1, §2.

**LC3. Dependants and maintainers are separate facts.** 65% of 133 popular GitHub projects had a
truck factor of 2 or less, and 16% of 1,932 popular projects lost their core developers. Google's
engineering book ties the cost of a change to the number of users of an interface and to the
expected life of the code. Moderate. (M, L) — §1.

**LC4. Coding agents raise the volume of code; measured delivery gains are small, short-lived or not
significant, and self-reports overstate them.** In METR's 2025 trial, developers took 19% longer
with AI and believed they were 20% faster. In 807 repositories that adopted Cursor, velocity rose
and did not last, while warnings and complexity rose and stayed. Moderate: several measured
sources, mostly observational and on open source, some vendor-run. (M) — §2.

**LC5. Review and quality assurance are the measured constraint when agents write code.** Agent
pull requests that were not merged were larger, touched more files and failed CI more often. Small
batches amplify the effect of AI in DORA's data. Makers and one cloud vendor's office of the CTO
state the same. Moderate. (M, L, A) — §2, §4.

**LC6. Standards bodies do not count an AI reviewer as the second party; one platform now lets an
AI approval count.** SLSA's Source track and OpenSSF Scorecard both say so in words. Since
1 September 2026, in public preview, GitHub lets a Copilot code review approval count toward
required approvals when an admin turns it on. (S, L) — §4.

**LC7. In maker practice, the guards on irreversible acts sit in the platform, not in the
instructions.** Copilot's cloud agent cannot approve or merge its own pull request and pushes to one
branch; OS-level sandboxing cut Anthropic's permission prompts by 84%. In one reported incident, a
code freeze that only the agent's instructions enforced did not hold. Moderate. (L, A) — §3.

**LC8. Most supply-chain basics are free on public GitHub repositories; several need a paid plan on
private ones.** Protected branches, required reviewers and code owners in private repositories need
Pro or Team; secret scanning on private organization repositories needs a paid product. (L,
VOLATILE) — §6.

**LC9. The EU Cyber Resilience Act applies by commercial placement on the EU market, not by team
size.** Its reporting duties have applied since 11 September 2026 and its main obligations apply
from 11 December 2027. Microenterprises and small enterprises get support and a simpler
documentation form, not an exemption. (S, partly through an unofficial copy of the law) — §7.

**LC10. Assurance standards scale rigour by the harm a failure can cause, and no source read
qualifies an AI coding agent as a tool in a safety lifecycle.** The FDA's software assurance
guidance is risk-based; IEC 62304 and DO-178C set levels by harm. (S, A) — §7.

**LC11. The sources reward the quality of documents, not their number.** DORA links documentation
quality to the effect of every technical capability; one controlled study found that context files
such as `AGENTS.md` usually did not raise agent success and raised cost by over 20%; ADRs in 921
repositories had mostly small correlations with quality measures. Moderate. (M, A) — §2, §5.

## 1. Facts that choose a lifecycle

The sources name the facts below as drivers of how much process, review, assurance and
documentation a project needs. Each fact is listed with what the evidence says about it.

**Frameworks that combine the facts.**

- Cockburn's Crystal framework places a project on two axes: the number of people and the
  criticality of a defect (loss of comfort, discretionary money, essential money, life). It says
  each added method element costs much, so the lightest method the project's point allows is the
  aim, and life-critical work needs more evidence and testing. It is a framework from experience,
  not a measured result ([c2.com](https://c2.com/xp/MinimalMethodologies.html)) (A). The colour
  bands and their team sizes differ between secondary sources; `UNVERIFIED`.
- Boehm (2002) gives home grounds for agile and plan-driven methods along developers, customers,
  requirements, architecture, refactoring cost, size and primary objective (rapid value or high
  assurance), and recommends a combined approach outside each home ground. His risk-exposure curves
  are illustrations with a few cited data points
  ([Boehm](https://wwwbroy.in.tum.de/misc/perlen/perlen-materialien/beneken_agil/Boehm_AgileMethoden.pdf))
  (A). The later book with Turner uses five factors (personnel, criticality, size, culture,
  dynamism); `UNVERIFIED`, read in secondary summaries only.
- Clarke and O'Connor (2012) built a reference framework of 44 situational factors in 8 classes from
  earlier research. The abstract reports no validation study
  ([DORAS](https://doras.dcu.ie/16823/)) (A).
- A survey with 556 data points found that under 15% of participants ran projects in a purely
  traditional or purely agile way; the choice of practices affected agility more than the choice of
  method ([arXiv 2109.11435](https://arxiv.org/abs/2109.11435))
  (M).

**Dependants: how many people or systems rely on the code.**

- Google's engineering book defines software engineering as "programming integrated over time", and
  gives Hyrum's law: the more users an interface has, the more of its observable behaviour they
  depend on. The number of dependants and the expected life therefore change the cost of a change
  ([SWE book ch. 1](https://abseil.io/resources/swe-book/html/ch01.html)) (L).
- 65% of 133 popular GitHub projects had a truck factor of 2 or less: many widely used projects
  depend on one or two people ([arXiv 1604.06766](https://arxiv.org/abs/1604.06766)) (M).
- The OpenSSF OSPS Baseline sets its levels by maintainers and users: Level 1 for any project, Level
  2 for code projects with at least two maintainers and a small steady user base, Level 3 for code
  projects with many steady users ([OSPS Baseline 2026.08.28](https://baseline.openssf.org/versions/2026-08-28))
  (S).

**Maintainers and team size.**

- Of 1,932 popular GitHub projects, 315 (16%) lost their core developers; 128 of those (41%)
  survived because new core developers took over, and difficulty in getting push access was a main
  barrier ([arXiv 1906.08058](https://arxiv.org/abs/1906.08058)) (M).
- On Windows Vista, organizational metrics predicted failure-prone binaries better than churn,
  complexity, coverage, dependencies or pre-release bug counts
  ([Microsoft Research](https://www.microsoft.com/en-us/research/publication/the-influence-of-organizational-structure-on-software-quality-an-empirical-case-study/))
  (M).
- A case survey of 86 start-ups found the most technical debt in testing, and more difficulty
  controlling debt in larger teams ([arXiv 2309.12434](https://arxiv.org/abs/2309.12434)) (M).
- OpenSSF Scorecard's documentation says that required review of every change is infeasible for a
  project with one active participant, and that small projects sometimes aim for review of a share
  of changes ([Scorecard checks](https://github.com/ossf/scorecard/blob/main/docs/checks.md)) (L).
- A certification body's ISMS scheme manager says that where a small team cannot segregate duties,
  compensating controls must exist (management oversight, peer review, logging and alerts, or dual
  authorization for critical changes), that auditors do not accept team size as an excuse, and that
  the exception and its risk must be documented
  ([TÜV NORD](https://www.tuv-nord.com/uk/en/navigating-iso-27001-annex-a-control-a53/)) (A).

**Criticality and harm.**

- Google sets a reliability target for each service from user expectations, revenue impact, free or
  paid use, and consumer or enterprise customers; the error budget (the gap to 100%) decides when the
  team may release and when it must work on reliability. The book says "100% is probably never the
  right reliability target" ([SRE book](https://sre.google/sre-book/embracing-risk/)) (L).
- Google's example error budget policy stops all releases except urgent and security fixes when the
  service has been over budget for four weeks; an incident that uses more than 20% of the budget
  needs a postmortem; disputes go to the CTO
  ([SRE workbook](https://sre.google/workbook/error-budget-policy/)) (L).
- Medical, aviation and FDA guidance set levels of rigour by harm (§7).

**Reversibility and the cost of rework.**

- Refactoring cost is one of Boehm's home-ground axes (above) (A).
- In 171 projects from 2006 to 2014, issues fixed in a later phase did not cost consistently or
  substantially more than issues fixed early; the delayed-issue effect varied by project
  ([arXiv 1609.04886](https://arxiv.org/abs/1609.04886)) (M).
- In a reported incident in July 2025, an agent deleted a user's production database during a code
  freeze that only the agent's instructions enforced; Replit then added automatic separation of
  development and production databases, a plan-only mode and one-click restore. `UNVERIFIED` at
  Replit's own post; read through
  [eWeek](https://www.eweek.com/news/replit-ai-coding-assistant-failure/) (A).
- Anthropic's auto-mode classifier blocks scope escalation, credential hunting, external sends and
  bypassed deploy checks; on 52 real over-eager actions its false-negative rate was 17%, and the
  page calls it "not a drop-in replacement for careful human review on high-stakes infrastructure"
  ([Anthropic](https://www.anthropic.com/engineering/claude-code-auto-mode)) (M, vendor).

**Expected life.**

- Code that lives for minutes needs different practice from code that lives for decades
  ([SWE book ch. 1](https://abseil.io/resources/swe-book/html/ch01.html)) (L).
- In repositories that adopted Cursor, static-analysis warnings and complexity rose and stayed up
  ([arXiv 2511.04427](https://arxiv.org/abs/2511.04427)) (M); a vendor's trend analysis reports more
  duplicated and churned code since 2023 (§2) (M, vendor, `UNVERIFIED`).
- The CRA asks for a support period of at least five years, or the expected use if shorter, and for
  technical documentation kept for at least ten years (§7) (S, unofficial copy).

**Review capacity.**

- DORA advises against very large pull requests of AI-generated code because reviewing them carries
  a high cognitive load ([DORA small batches](https://dora.dev/capabilities/working-in-small-batches/))
  (L).
- Measured review time and load rose with agent adoption, and one developer opened as many agent
  pull requests in three days as in the three years before (§2) (M; the second is one report).
- ENISA's draft advisory names insufficient review capacity among the governance risks of
  AI-assisted development (§7) (S, draft).

**Agent autonomy: attended work against unattended background work.**

- All the major makers ship background agents that work on a branch and open a pull request
  (Copilot cloud agent with a 59-minute session cap, Codex cloud, Jules, Cursor cloud agents, Claude
  Code on the web), and run parallel local agents in separate Git worktrees
  ([GitHub](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations),
  [Jules](https://jules.google/docs/), [Cursor](https://cursor.com/blog/agent-best-practices),
  [Anthropic](https://code.claude.com/docs/en/best-practices)) (L).
- GitHub's controls for unattended agents differ from those for attended work: an outbound firewall
  with an allowlist by default, Actions workflows on an agent's pull request that wait for approval
  by a person with write access, and agentic workflows that are read-only by default with writes
  only through pre-approved outputs (§3) (L).
- ENISA's draft asks a team to set who reviews or approves AI-assisted output by the component's
  sensitivity, the change's scope and the agent's autonomy (§7) (S, draft).

**Requirement and priority stability.**

- The 2024 DORA report found that unstable organizational priorities lower productivity and raise
  burnout, and that strong leaders, good documentation and a user-centred approach do not remove the
  effect ([DORA 2024](https://dora.dev/research/2024/dora-report/),
  [announcement](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report))
  (M, survey).
- The NaPiRE survey covered 228 companies in 10 countries and 21 requirements problems
  ([arXiv 1611.10288](https://arxiv.org/abs/1611.10288)) (M). `UNVERIFIED`, secondary only:
  incomplete or hidden requirements was the most frequent problem, and moving targets the problem
  most linked to project failure.
- Dynamism is one of Boehm and Turner's five factors (`UNVERIFIED`, above) (A).
- `UNVERIFIED`, search summaries only: Jørgensen (IST 2016) surveyed Norwegian professionals on the
  client and provider sides. On time, on budget and to specification were weak predictors of client
  benefit; fixed-price contracts and choice of provider by low price went with less benefit; agile
  projects without flexible scope or without frequent delivery to the client did worse than
  average; benefits management went with success (M, small survey).

**Commercial sale in the EU.**

- The CRA's trigger is placing a product with digital elements on the EU market in a commercial
  activity, not the size of the team; free software that is not monetised is generally out of scope
  ([Commission, CRA and open source](https://digital-strategy.ec.europa.eu/en/policies/cra-open-source),
  page last updated 15 October 2026) (S). The duties and dates are in §7.

**Facts the evidence found weak or did not separate.**

- Industry: no effect on delivery performance except retail, in DORA's 2019 survey of almost 1,000
  respondents that year, including financial services and government
  ([State of DevOps 2019](https://dora.dev/publications/pdf/state-of-devops-2019.pdf)) (M, survey).
- Company size: organizations with more than 5,000 employees performed worse; DORA attributes this
  to heavyweight process and controls and tightly coupled architecture (same source) (M, survey;
  the cause is DORA's reading).
- Implementer capability: personnel is a factor in Boehm's framework (A), and METR's trial measured
  experienced developers in their own repositories (§2) (M). No source measures the capability of a
  model and harness as a lifecycle factor.

## 2. Measured delivery evidence (STABLE)

Limits first. DORA is a yearly, self-selected survey with correlational analysis; most respondents
work in technology companies, and the data does not separate solo developers or prototypes. No
source read measures a whole lifecycle for projects that coding agents build; the AI evidence
measures teams of people who use AI tools, mostly on open-source repositories, often with tools
one or two generations old. Several measured sources sell tools that the result favours.

**DORA and delivery practice.**

- DORA now uses five delivery metrics: change lead time, deployment frequency and failed deployment
  recovery time (throughput), and change fail rate and deployment rework rate (instability). It
  states "speed and stability are not tradeoffs", and says to compare the metrics only within one
  application ([DORA metrics](https://dora.dev/guides/dora-metrics-four-keys/)) (M, survey; L).
- In the 2025 report (nearly 5,000 respondents), AI adoption went with higher throughput and product
  performance but still with lower delivery stability; DORA calls AI an amplifier of an
  organization's existing strengths and weaknesses
  ([DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report))
  (M, survey). About 90% used AI; that figure was read through
  [InfoQ](https://www.infoq.com/news/2026/03/ai-dora-report/) (secondary).
- The 2025 AI Capabilities Model names seven capabilities that increase the benefit of AI: a clear
  and communicated AI stance, healthy data ecosystems, AI-accessible internal data, strong version
  control, small batches, a user-centric focus and quality internal platforms. Frequent commits and
  frequent rollback went with better results for AI-assisted teams; without a user-centric focus, AI
  adoption could lower team performance
  ([DORA AI Capabilities Model](https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model))
  (M, survey).
- In the 2024 report, a 25% rise in AI adoption went with 7.5% higher documentation quality, 3.4%
  higher code quality and 3.1% faster code review, and with an estimated 1.5% fall in throughput and
  7.2% fall in stability. DORA says better development does not improve delivery without basics
  such as small batches and robust testing
  ([DORA 2024](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report))
  (M, survey).
- Small batches, with related capabilities, predict delivery and organizational performance, and
  increase the positive effect of AI on product performance
  ([DORA small batches](https://dora.dev/capabilities/working-in-small-batches/)) (M, survey).
- DORA defines trunk-based development as three or fewer active branches, a merge to trunk at least
  once a day and no code freezes, on its 2016 and 2017 survey data. It also says heavy review with
  many approvals pushes developers to large batches. The page does not discuss team size
  ([DORA trunk-based development](https://dora.dev/capabilities/trunk-based-development/)) (M,
  survey; L).
- Documentation quality increased the effect of every technical capability on organizational
  performance: for trunk-based development the lift was 36% with below-average documentation and
  1525% with above-average documentation. DORA measures quality (clarity, findability,
  reliability), not quantity
  ([DORA documentation quality](https://dora.dev/capabilities/documentation-quality/)) (M, survey).
- In 2019, respondents who needed approval from an external body (a change advisory board or a
  senior manager) were 2.6 times more likely to be low performers, with no evidence that this
  approval lowered the change fail rate; respondents with a clear change process were 1.8 times more
  likely to be elite performers. DORA recommends peer review, recorded in the platform, to satisfy
  segregation of duties ([State of DevOps 2019](https://dora.dev/publications/pdf/state-of-devops-2019.pdf))
  (M, survey; L). DORA's change-approval guidance adds: send high-risk changes to more review instead
  of giving every change the same process, make the normal process fast enough for emergencies, and
  confirm the approach with the compliance function
  ([DORA change approval](https://dora.dev/capabilities/streamlining-change-approval/)) (L).
- `UNVERIFIED`, secondary only: in the 2024 DORA clusters, medium performers had a lower change fail
  rate than high performers ([Octopus](https://octopus.com/blog/2024-devops-performance-clusters))
  (M, survey, if true).
- No 2026 DORA report was found; the newest edition on [dora.dev](https://dora.dev/research/) is
  2025. The page also links a report on the return on investment of AI-assisted development, which
  was not read.

**Google release engineering.**

- Google's release engineering uses self-service and frequent releases, hermetic builds, access
  controls on releases and code review for almost all changes; the chapter says companies of every
  size have these problems. Releases usually come from a tested mainline revision, with fixes
  cherry-picked to a release branch
  ([SRE book](https://sre.google/sre-book/release-engineering/)) (L).
- Long-lived development branches are not a good default: fewer than 10 of about 1,000 teams in the
  monorepo keep one. Release branches are acceptable for a fixed release cadence with few
  cherry-picks ([SWE book ch. 16](https://abseil.io/resources/swe-book/html/ch16.html)) (L).

**Code review before agents.**

- At Microsoft (observation, interviews, surveys and classified review comments), developers
  expected review to find defects, and it found fewer than they expected; it gave knowledge transfer,
  team awareness and alternative solutions, and understanding the change was the main difficulty
  ([Microsoft Research](https://www.microsoft.com/en-us/research/publication/expectations-outcomes-and-challenges-of-modern-code-review/))
  (M).
- A later Microsoft paper says code reviews often do not find functional problems that must block a
  change, and that review is often the slowest step of integration; its abstract gives no sample
  size ([Microsoft Research](https://www.microsoft.com/en-us/research/publication/code-reviews-do-not-find-bugs-how-the-current-code-review-best-practice-slows-us-down/))
  (A, experience with some data).
- A Google study used 12 interviews, a survey of 44 respondents and logs of 9 million reviewed
  changes ([Google Research](https://research.google/pubs/modern-code-review-a-case-study-at-google/))
  (M). `UNVERIFIED`, secondary only: the median review took under 4 hours, most changes were small,
  and most had one reviewer.
- Google's engineering book says most reviews have exactly one reviewer because more add little value
  and add cost; it asks for changes of about 200 lines on one issue, and approval from an owner of
  the code ([SWE book ch. 9](https://abseil.io/resources/swe-book/html/ch09.html)) (L).
- In Qt, VTK and ITK, components with low review coverage had up to two more post-release defects,
  and components with low review participation up to five more
  ([Waterloo](https://rebels.cs.uwaterloo.ca/confpaper/2014/05/30/the-impact-of-code-review-coverage-and-code-review-participation-on-software-quality.html))
  (M).
- `UNVERIFIED`, secondary only: Mäntylä and Lassenius (IEEE TSE 2009) found that most defects found
  in review are evolvability defects, about 75% in secondary sources, not functional defects (M, if
  true).

**Speed with AI tools.**

- METR's randomized trial (10 July 2025): 16 experienced open-source developers did 246 issues in
  their own large repositories; with AI tools allowed (early 2025), they took 19% longer. They
  expected a 24% speed-up and afterwards believed in about 20%. METR now marks the result as out of
  date ([METR 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)) (M).
- METR's update (24 February 2026): 57 developers and more than 800 tasks; estimates of −18% (CI −38%
  to +9%) for returning developers and −4% (CI −15% to +9%) for new ones, where negative means faster
  with AI. METR calls the data unreliable: developers refused to work without AI, held back 30–50% of
  tasks and ran agents at the same time ([METR 2026](https://metr.org/blog/2026-02-24-uplift-update/))
  (M, weak by METR's own account).
- A Google randomized trial (October 2024) of 96 engineers on one enterprise task found AI features
  cut the time by about 21%, with a wide confidence interval
  ([arXiv 2410.12944](https://arxiv.org/abs/2410.12944)) (M; read in a search result only).
- Echoes of AI (v3, 26 February 2026), 151 participants: in phase 1, AI use went with a 30.7% median
  time cut; in the randomized phase 2, other developers changed the AI-assisted code with no
  significant change in time or quality ([arXiv 2507.00788](https://arxiv.org/abs/2507.00788)) (M).

**Quality, complexity and security of agent-written code.**

- He et al. (v3, 26 January 2026), a difference-in-differences study of 807 repositories that adopted
  Cursor against 1,380 matched ones: velocity rose sharply and did not last; static-analysis warnings
  and complexity rose and stayed up and explain much of the later slow-down. The authors call quality
  assurance the main bottleneck ([arXiv 2511.04427](https://arxiv.org/abs/2511.04427)) (M,
  observational, open source).
- GitClear 2026, 623M changes from 2023 to 2026: duplicated blocks up 81%, copy and paste within a
  commit up 41%, two-week churn up 15%, cross-file calls down 35%. `UNVERIFIED`: the page returned
  403 and was read through search summaries; AI use is inferred, and the vendor sells the measuring
  tool ([GitClear](https://gitclear.com/the_ai_code_quality_maintainability_gap)) (M, vendor).
- CodeRabbit (17 December 2025), 470 open-source pull requests: AI co-authored pull requests had
  10.83 issues each against 6.45 for human-only ones (about 1.7 times); authorship was inferred, the
  sample is small, and the vendor sells AI review
  ([CodeRabbit](https://coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report)) (M,
  vendor).
- Veracode 2026 (28 July 2026): models without a security prompt passed the security check on about
  56% of tasks, about the same as in 2025, and coding-specific models were no better. Models were
  tested without agents, tools or review, and the vendor sells security scanning; read as a press
  report ([SD Times](https://sdtimes.com/agentic-security/veracode-finds-ai-generated-code-security-has-barely-improved-since-last-year/))
  (M, vendor).
- 1,293 security-related agent pull requests, about 4% of agent activity, merged less often and
  waited longer for review; complexity and length predicted rejection more than the security topic
  did ([arXiv 2601.00477](https://arxiv.org/abs/2601.00477), v2, 3 September 2026) (M).

**Agent pull requests and review load.**

- AIDev (20 July 2025), 456k agent pull requests over 61k repositories: agent pull requests are
  accepted less often than human ones; one developer opened as many pull requests in three days as in
  the three years before ([arXiv 2507.15003](https://arxiv.org/abs/2507.15003)) (M). Acceptance of
  35–64% by agent is `UNVERIFIED` (search summaries only).
- Of 654 rejected agent pull requests in AIDev, 67.9% had no explicit reviewer feedback
  ([arXiv 2602.04226](https://arxiv.org/abs/2602.04226)) (M).
- Failed agentic pull requests (MSR 2026), 33k pull requests: docs, CI and build tasks merged most
  often, bug-fix and performance tasks least. Pull requests that were not merged were larger, touched
  more files and failed CI more often. Reasons for rejection: no reviewer engagement, duplicates,
  unwanted features and agent misalignment ([arXiv 2601.15195](https://arxiv.org/abs/2601.15195))
  (M).
- 22–29% of 128k GitHub projects show agent traces, likely a lower bound, and agent commits are
  larger than human ones ([arXiv 2601.18341](https://arxiv.org/abs/2601.18341)) (M).
- Agarwal et al. (8 July 2026): on GitHub, agent pull requests are reviewed less, discussed less and
  merged faster, but the direction of these trends reverses under other defensible analysis choices.
  Their theory, built from 3,100 practitioner documents, places review as the control point that
  decides whether agents help or harm ([arXiv 2607.07980](https://arxiv.org/abs/2607.07980)) (M; the
  theory is A).
- `UNVERIFIED`, read through secondary coverage only: Chen and Stratton (Harvard working paper,
  version of 4 August 2026), Jellyfish data for 725,938 workers at 718 firms. After agent adoption,
  lines per worker rose about 30%, finished tasks did not rise significantly, time from pull request
  to merge rose 49% and review comments per pull request rose 35%
  ([AI Weekly](https://aiweekly.co/alerts/harvard-study-ai-coding-agents-lift-code-30-shipped-output-flat))
  (M).
- Faros telemetry from 10,000 developers in 1,255 teams: developers completed about twice as many
  code changes, but company-level metrics stayed flat ([Faros](https://www.faros.ai/ai-productivity-paradox))
  (M, vendor). The often-cited figures of 98% more merged pull requests, 91% longer review and 154%
  larger pull requests are `UNVERIFIED`: the primary page does not show them, and Faros's own FAQ
  gives other numbers.

**Surveys and maker telemetry.**

- Stack Overflow 2025: 84% use or plan to use AI; trust in accuracy fell to about 29–33%; the top
  frustration is answers that are "almost right"; about 31% use agents. `UNVERIFIED`: read through
  search results only
  ([Stack Overflow](https://stackoverflow.blog/2025/07/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here))
  (M, survey).
- Fast and Spurious (v2, 5 April 2026), 415 practitioners: heavy AI users report faster work, offset
  by a heavier review load and the mental load of checking output
  ([arXiv 2510.24265](https://arxiv.org/abs/2510.24265)) (M, self-report).
- Anthropic internal (2 December 2025), 132 surveyed, 53 interviews and about 200k transcripts:
  Claude is used in about 60% of work; self-reported productivity is +50%; the longest run of
  consecutive tool calls rose 116%; most can fully delegate only 0–20% of their work
  ([Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)) (M,
  vendor).
- Anthropic Economic Index (28 April 2025): 79% of Claude Code conversations are automation against
  49% on Claude.ai; startups are about 33% of Claude Code use and enterprises 13–24% (the page gives
  both figures) ([Anthropic](https://www.anthropic.com/research/impact-software-development)) (M,
  vendor).
- Anthropic's 2026 Agentic Coding Trends Report lists eight trends, among them a change in the
  development lifecycle and scaling human oversight. `UNVERIFIED`: the content is behind a form and
  its text could not be extracted ([Anthropic](https://resources.anthropic.com/2026-agentic-coding-trends-report))
  (L).

**The cost of process: specs, design documents and decision records.**

- In 171 projects, late fixes did not cost consistently more than early fixes (§1)
  ([arXiv 1609.04886](https://arxiv.org/abs/1609.04886)) (M).
- At Microsoft, controlled experiments showed about one third of ideas improved the target metric,
  one third had no significant effect and one third made it worse
  ([Kohavi tutorial](https://ai.stanford.edu/~ronnyk/2009-06-28KDDTutorialT4part1.pdf)) (M, reported
  in a tutorial).
- A Google engineer's account says a design document is useful when there are real trade-offs; when
  the solution is clear it becomes an implementation manual and writing the code is better, and rapid
  prototyping can also make it less useful. It says "Writing design docs is overhead."
  ([Industrial Empathy](https://www.industrialempathy.com/posts/design-docs-at-google/)) (A).
- 921 GitHub repositories with about 5,800 ADRs showed mostly small correlations between ADR traits
  and code smells or issue resolution time; about 63% of ADRs were created already marked accepted,
  so they did not record a deliberation
  ([ICSA 2026](https://conf.researchr.org/details/icsa-2026/icsa-2026-papers/34/Architecture-Decision-Records-Adoption-Impact-and-Developer-Engagement-in-Open-Sou))
  (M). An earlier mining study (IEEE Access 2023) found low adoption and one to five records in about
  half of the repositories that have ADRs; `UNVERIFIED`, search summary only
  ([DOAJ](https://doaj.org/article/f838f2a538ea48e7a3b15ce99befe612)).
- Michael Nygard proposed the ADR format in 2011 as a practitioner proposal, not a measured practice.
  `UNVERIFIED`: the original article was not reached; read about through
  [martinfowler.com](https://www.martinfowler.com/bliki/ArchitectureDecisionRecord.html) search
  results (A).
- Context files such as `AGENTS.md` usually did not raise coding-agent task success and raised
  inference cost by over 20%, for files written by models and by developers. The agents followed the
  instructions, but repository overviews did not help; the authors say such files help for
  non-standard practices and recommend only requirements that the agent cannot infer (Gloaguen et
  al., ICLR 2026, v3 29 September 2026, [arXiv 2602.11988](https://arxiv.org/abs/2602.11988)) (M).

## 3. What coding agents change at each stage (MONITOR)

| Stage | What the sources report | Sources |
| --- | --- | --- |
| Intake | GitHub's guide treats an issue given to its agent as a prompt with a problem statement, acceptance criteria and pointers, and keeps some tasks from the agent: security, PII, authentication, production-critical work, incident response and vague tasks. Outside agent pull requests arrive as a new kind of intake, with duplicates and unwanted features. | [GitHub](https://docs.github.com/en/copilot/tutorials/coding-agent/get-the-best-results) (L); [arXiv 2601.15195](https://arxiv.org/abs/2601.15195) (M) |
| Spec | Makers advise a plan or spec first for multi-file work and skipping it when one sentence describes the diff. Spec tools were found heavy for small work, and agents still ignored parts of specs. | below (L, A) |
| Slicing | Small batches amplify AI's effect; large agent pull requests stall; one cloud vendor's office of the CTO advises chunks a person can review; parallel agents run in separate worktrees. | [DORA](https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model) (M); [arXiv 2601.15195](https://arxiv.org/abs/2601.15195) (M); [Google Cloud](https://cloud.google.com/transform/when-ai-writes-the-code-who-reviews-it-cto-google-cloud) (A); §1 (L) |
| Build | The agent writes; the makers' guides put first a check the agent can run, and set the sandbox and permissions around it. They treat context as limited: short instruction files, fresh sessions, subagents. | below (L) |
| Review | Practice is moving to layers: an AI pass on pull requests, a fresh-context agent reviewer, and human review aimed at architecture and risk. Human approval still gates by default (§4). | §4 |
| Land | CI and branch protection apply to agents; agent workflows can wait for a person's approval before they run; commits carry agent attribution and a link to session logs. | below (L); [arXiv 2601.15195](https://arxiv.org/abs/2601.15195) (M) |
| Release | Little agent-specific guidance was found. Anthropic's auto-mode classifier blocks a bypassed deploy check. | [Anthropic](https://www.anthropic.com/engineering/claude-code-auto-mode) (L) |
| Deploy | Separation of development from production by the platform after an incident in which an instruction-only freeze failed; makers keep agents from broad access. | §1 (A); [Anthropic](https://www.anthropic.com/engineering/claude-code-auto-mode) (L); [Willison](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (A) |
| Operate | Agents run in CI for triage, CI-failure analysis and docs upkeep, read-only with gated writes; GitHub keeps incident response with people. | below (L) |
| Retire | No agent-specific source was found. One cloud vendor's piece mentions removing deprecated agents. | [Google Cloud](https://cloud.google.com/transform/when-ai-writes-the-code-who-reviews-it-cto-google-cloud) (A, weak) |

**Instruction files.**

- Anthropic says to keep `CLAUDE.md` short, with only what the agent cannot infer (commands,
  non-default style, gotchas); to prune it like code; to move rare knowledge to skills that load on
  demand; and to put a rule that must hold every time in a hook. It warns: "Bloated CLAUDE.md files
  cause Claude to ignore your actual instructions!"
  ([Anthropic](https://code.claude.com/docs/en/best-practices)) (L).
- Codex joins `AGENTS.md` files from the repository root down to the working directory, and the
  nearer file wins; content past a size cap (`project_doc_max_bytes`, default 32 KiB) is dropped
  without a warning. The page leaves format and lint rules to CI
  ([OpenAI](https://learn.chatgpt.com/docs/agent-configuration/agents-md)) (L). OpenAI's
  best-practice guide says to add a rule only after a repeated mistake, keep the file short, put task
  detail in other files, and reference a `code_review.md` for consistent review
  ([OpenAI](https://learn.chatgpt.com/guides/best-practices)) (L).
- GitHub Copilot reads `.github/copilot-instructions.md`, path-scoped instruction files and
  `AGENTS.md`, `CLAUDE.md` and `GEMINI.md`
  ([GitHub](https://docs.github.com/en/copilot/tutorials/coding-agent/get-the-best-results)) (L).
  GitHub's study of more than 2,500 `AGENTS.md` files (19 November 2025) advises commands first,
  examples over prose, and boundaries in three tiers (always, ask first, never)
  ([GitHub blog](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/))
  (L, a vendor's analysis, not a controlled measure).
- Gemini CLI loads `GEMINI.md` at global, workspace and just-in-time levels and can read `AGENTS.md`
  by a setting; on 18 June 2026, Antigravity CLI replaced Gemini CLI for unpaid and Google One users
  ([Gemini CLI](https://geminicli.com/docs/cli/gemini-md/)) (L). Kiro has steering files (product,
  tech, structure) with four inclusion modes and reads `AGENTS.md`
  ([Kiro](https://kiro.dev/docs/steering/), page updated 6 October 2026) (L). Cursor (9 January
  2026) advises short rules for commands and conventions, added only after a repeated mistake
  ([Cursor](https://cursor.com/blog/agent-best-practices)) (L).
- OpenSSF's guide to instructions for AI code assistants (1 August 2025) says to keep them short,
  specific and relevant, and warns that irrelevant security rules can make the assistant write
  extraneous or wrong code; its basis is expert opinion. Read in search results
  ([OpenSSF](https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions))
  (A).

**Specs and plans.**

- Anthropic: explore, then plan, then code; for larger features the agent interviews the user and
  writes a spec, and a fresh session implements it; skip the plan when one sentence can describe the
  diff ([Anthropic](https://code.claude.com/docs/en/best-practices)) (L).
- OpenAI: Plan mode, an interview, or a `PLANS.md` ExecPlan for multi-hour work, a living design
  document reviewed before the work starts. `UNVERIFIED` at the page; reached through a search result
  ([OpenAI cookbook](https://developers.openai.com/cookbook/articles/codex_exec_plans)) (L).
- GitHub Spec Kit: a constitution once per project, then specify, plan, tasks and implement; the
  current README also lists a converge step and opt-in extensions for bug fixes and idea intake
  ([Spec Kit](https://github.com/github/spec-kit)) (L). Kiro specs have requirements, design and
  tasks files; a Quick Spec mode writes all three in one pass with no approval gates; bugfix specs
  record current, expected and unchanged behaviour ([Kiro](https://kiro.dev/docs/specs/), page
  updated 2 October 2026) (L). Jules makes a plan that the user approves before any code changes
  ([Jules](https://jules.google/docs/)) (L).
- Böckeler (Thoughtworks, 15 October 2025) tried Kiro, Spec Kit and Tessl: the workflows were too
  heavy for small and mid-sized changes, the Markdown was tedious to review, and agents still ignored
  parts of the spec. "I'd rather review code than all these markdown files."
  ([martinfowler.com](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)) (A).

**Verification and CI as the gate.**

- Anthropic's first practice is a check the agent can run (tests, a build, a screenshot); a Stop hook
  can make it a deterministic gate; and the guide says not to ship work that cannot be verified
  ([Anthropic](https://code.claude.com/docs/en/best-practices)) (L). Hooks are deterministic and
  instructions advisory (same source) (L); Kiro hooks fire on file save, before and after a tool and
  at stop, and run a command or an agent prompt ([Kiro](https://kiro.dev/docs/hooks/), page updated 10 October 2026) (L).
- Cursor: commit failing tests first, then have the agent make them pass without changing them; a
  stop hook can loop the agent until the tests pass
  ([Cursor](https://cursor.com/blog/agent-best-practices)) (L).
- Anthropic, long-running agents (26 November 2025): a feature list with every item failing at the
  start, a progress file, frequent commits, one feature at a time and end-to-end verification; the
  failure mode is an agent that declares the work done too early
  ([Anthropic](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents))
  (L).
- GitHub: a `copilot-setup-steps.yml` installs dependencies so the agent can build and test in its
  Actions environment, and branch protections and required checks apply to the agent
  ([GitHub](https://docs.github.com/en/copilot/tutorials/coding-agent/get-the-best-results),
  [GitHub](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations))
  (L).
- OpenAI's harness engineering report (11 February 2026): a small team shipped an internal product
  of about 1M lines with no hand-written code in five months; structural tests, linters and CI
  enforce layer rules, and a docs directory is the agents' source of truth. `UNVERIFIED`: openai.com
  returned 403; read through [InfoQ](https://www.infoq.com/news/2026/02/openai-harness-engineering-codex),
  21 February 2026 (L, a vendor's report on its own work).
- Anthropic on evaluations (9 January 2026): start with 20–50 tasks from real failures, keep
  regression evaluations near 100% and capability evaluations low, and run them in CI on every agent
  change and model upgrade. The guidance is for products that have agent or model behaviour, not for
  ordinary code ([Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents))
  (L).
- Willison (7 October 2025) says agents reward existing good practice: tests, plans, docs, version
  control, CI, a review culture, manual QA and preview environments
  ([Willison](https://simonwillison.net/2025/Oct/7/vibe-engineering/)) (A).

**Background agents, sandboxes and irreversible acts.**

- GitHub Agentic Workflows (technical preview, 13 February 2026) run agents in Actions from Markdown
  workflows: read-only by default, sandboxed, network-isolated, with dependencies pinned by SHA and
  writes only through pre-approved safe outputs. Uses include triage, CI-failure analysis, docs
  upkeep and compliance monitoring
  ([GitHub changelog](https://github.blog/changelog/2026-02-13-github-agentic-workflows-are-now-in-technical-preview/))
  (L).
- Anthropic (20 October 2025): OS-level sandboxing of the file system and network cut permission
  prompts by 84% internally; frequent prompts cause approval fatigue; the sandbox also limits what a
  prompt injection can take ([Anthropic](https://www.anthropic.com/engineering/claude-code-sandboxing))
  (M, vendor). Under auto mode (25 March 2026), users had approved about 93% of permission prompts
  ([Anthropic](https://www.anthropic.com/engineering/claude-code-auto-mode)) (M, vendor).
- OpenAI treats approval policy and sandbox mode as two separate controls, and says to start tight
  and loosen only for trusted repositories ([OpenAI](https://learn.chatgpt.com/guides/best-practices))
  (L). Copilot's cloud agent has an outbound firewall with an allowlist by default
  ([GitHub](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations))
  (L).
- Willison's lethal trifecta (16 June 2025): private data, untrusted content and an outbound channel
  together let an attacker take data out
  ([Willison](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)) (A).
- OWASP published a Top 10 for Agentic Applications (9 December 2025). The item names were not
  reached at the source; secondary sources list goal hijack, tool misuse, identity, supply chain,
  code execution, memory poisoning, inter-agent messages, cascading failures, human trust
  exploitation and rogue agents (`UNVERIFIED`)
  ([OWASP](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)) (S).
- The Five Eyes agencies' guidance on adopting agentic AI services (1 May 2026) says never to give
  agents broad or unrestricted access and to start with low-risk, non-sensitive tasks; the UK NCSC's
  summary adds least privilege, meaningful human oversight and humans who stay accountable. Neither
  text read mentions coding agents. The NCSC blog was read; the guidance itself timed out
  ([NCSC](https://www.ncsc.gov.uk/blogs/thinking-carefully-before-adopting-agentic-ai), 15 May 2026)
  (S).

## 4. Review when agents write the code (MONITOR)

**What the platforms enforce.**

- GitHub's Copilot cloud agent cannot mark its pull request ready, approve it or merge it; the
  user who asked for the pull request cannot approve it; Actions workflows on its pull requests do
  not run until a person with write access approves them; it pushes to one branch only
  ([GitHub](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations))
  (L).
- Since 20 March 2026, each commit from the Copilot coding agent carries an `Agent-Logs-Url` trailer
  linking to the session logs; Copilot is the author and the user who asked is the co-author
  ([GitHub changelog](https://github.blog/changelog/2026-03-20-trace-any-copilot-coding-agent-commit-to-its-session-logs))
  (L).
- Since 1 September 2026, in public preview, Copilot code review can submit an approval that counts
  toward required approvals. It is off by default, admins can limit it to file paths, and a new
  commit dismisses it
  ([GitHub changelog](https://github.blog/changelog/2026-09-01-copilot-code-review-can-now-approve-pull-requests))
  (L). [review.md](review.md) §8 covers which AI reviewers can count as an approval.
- Since 7 August 2026, turning on Code Quality no longer creates a ruleset that requests a Copilot
  review on every pull request; a team that wants automatic AI review sets the ruleset itself.
  `UNVERIFIED` at the page; search result only
  ([GitHub changelog](https://github.blog/changelog/2026-08-07-github-code-quality-no-longer-adds-copilot-as-a-reviewer))
  (L).

**What standards say about an AI reviewer.**

- SLSA's Source track: L1 is version control; L2 is continuous, retained history with no force
  pushes; L3 is continuously enforced technical controls on protected branches; L4 needs two trusted
  persons to agree to each change. A trusted person is a human; automation is a separate trusted
  robot role and never counts toward the two parties
  ([SLSA source requirements](https://slsa.dev/spec/v1.2/source-requirements)) (S).
- Scorecard's Code-Review check does not count review by bots, AI and ML bots included, because a
  bot gives no second person who understands the change
  ([Scorecard checks](https://github.com/ossf/scorecard/blob/main/docs/checks.md)) (L).
- No standard or regulator text found says that an AI agent can be the second party in a review, and
  no source certifies or qualifies an AI coding agent as a development tool for a safety lifecycle
  (inference from the sources in this section and §7).

**What makers report and advise.**

- Anthropic Code Review (9 March 2026): code output per Anthropic engineer grew 200% in a year and
  review became the bottleneck; internally, pull requests with substantive review comments went from
  16% to 54%; engineers marked fewer than 1% of findings wrong; a review costs $15–25 on average. "It
  won't approve PRs — that's still a human call." ([Anthropic](https://claude.com/blog/code-review))
  (M, vendor; no method published).
- OpenAI says Codex reviews all of OpenAI's pull requests
  ([OpenAI](https://learn.chatgpt.com/guides/best-practices)) (L, a claim with no method).
- Anthropic advises a writer and reviewer split, with a fresh-context subagent that reviews the diff
  against the plan and reports only gaps in correctness or requirements, because a reviewer asked for
  gaps finds some and this causes over-engineering
  ([Anthropic](https://code.claude.com/docs/en/best-practices)) (L).
- Jules has a critic that reviews each patch before submission (August 2025). `UNVERIFIED` at the
  page; search result only
  ([Google Developers Blog](https://developers.googleblog.com/en/meet-jules-sharpest-critic-and-most-valuable-ally/))
  (L).
- GitHub says to review an agent pull request as a teammate's
  ([GitHub](https://docs.github.com/en/copilot/tutorials/coding-agent/get-the-best-results)) (L).
- Google Cloud's office of the CTO (29 April 2026): review is now the constraint; split agent work
  into chunks a person can review, put people on architecture rather than style, add an AI summary
  and risk note to each pull request, and watch for approval fatigue. "AI eliminated the code
  production bottleneck."
  ([Google Cloud](https://cloud.google.com/transform/when-ai-writes-the-code-who-reviews-it-cto-google-cloud))
  (A).

**What was measured.** Review time and comments rose with agent adoption (`UNVERIFIED`, Chen and
Stratton); agent pull requests may be reviewed less, with a direction that depends on analysis
choices; many rejected agent pull requests had no reviewer feedback; review coverage and
participation went with fewer post-release defects before agents (all in §2) (M).

**Audits and segregation of duties.**

- SOC 2 criterion CC8.1 asks that changes are authorized, designed, developed, configured,
  documented, tested, approved and implemented; its points of focus include approval before
  deployment, testing, emergency changes and a baseline configuration. Segregation of duties is not a
  named point of focus under CC8.1. The AICPA document was not reached; this is from control-library
  copies ([cyberday](https://cyberday.ai/requirement/soc-2-cc8-1-change-management-procedures)) (A).
- No AICPA or audit-firm guidance on agent-written code was found. Practitioner writing says CC8.1
  does not care who or what wrote a change, only whether the evidence exists
  ([Scalr](https://scalr.com/learning-center/can-ai-agents-change-infrastructure-and-stay-compliant))
  (A). One author argues that the control assumes the approver understood the change, so an approver
  who did not read agent-written code may not meet its intent
  ([tianpan.co](https://tianpan.co/blog/2026-05-05-ai-generated-code-compliance-attestation-gap)) (A).
- With one maintainer, required review of every change is infeasible in Scorecard's words, and an
  ISMS certifier asks for documented compensating controls (§1) (L, A).
- On GitHub, branch protection binds administrators only when bypassing is disallowed; by default,
  admin permissions bypass the rules
  ([GitHub](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches))
  (L).

## 5. Practices the sources support at every scale

None of the sources below limits these practices by industry or company size (DORA 2019, §1; the
Google release engineering chapter, §2). Most of the evidence comes from teams and organizations,
not from one-person projects or prototypes (§8).

- **Version control, frequent commits and a known way to roll back.** DORA's AI capabilities model
  (strong version control, frequent commits, frequent rollback); Google's release engineering;
  Anthropic's long-running agent guidance (frequent commits) (§2, §3) (M, survey; L).
- **Small batches and short-lived branches merged to trunk.** DORA small batches and trunk-based
  development; Google's view of long-lived branches; large agent pull requests stall (§2) (M; L).
- **Automated tests and fast feedback.** DORA's basics that make AI's gains reach delivery; every
  maker puts a check the agent can run first (§2, §3) (M, survey; L).
- **Automated, repeatable deployment and fast recovery.** DORA measures recovery time and rework;
  Google uses self-service releases from a tested mainline (§2) (M, survey; L).
- **Light peer review of small changes, recorded in the platform, where a reviewer exists.** DORA
  2019; the Microsoft and Google review studies; the Qt, VTK and ITK study (§2) (M; L).
- **An independent check of agent output before it counts as done.** The makers' fresh-context
  reviewers and critics (§4) (L); the measured review evidence (§2) (M).
- **A clear change process that people can predict.** 1.8 times more likely to be elite (DORA 2019,
  §2) (M, survey).
- **The quality of documentation, not its quantity, and minimal instruction files.** DORA
  documentation quality; the `AGENTS.md` study; the makers' advice on short instruction files (§2,
  §3) (M; L).
- **Guards on irreversible acts in the platform, not in instructions.** Sandbox, network limits,
  single-branch push, no self-approval, workflow approval, development separated from production
  (§3, §4) (L; A).
- **Stable priorities and a user-centric focus.** DORA 2024 and the AI capabilities model (§1, §2) (M,
  survey).

Evaluations as a CI gate appear in the sources only for products that have model or agent behaviour
(Anthropic, §3) (L).

## 6. Supply-chain basics and their cost by plan and visibility (VOLATILE) [as-of 2026-10-15]

**Frameworks and their levels.**

- NIST SSDF 1.1 (SP 800-218, February 2022) gives secure development practices that fit any
  lifecycle model ([NIST](https://csrc.nist.gov/pubs/sp/800/218/final)) (S). The SSDF 1.2 initial
  public draft (17 December 2025) is outcome-based and risk-based, says it applies "regardless of
  size", and says not every practice applies to every use case. Its PS.1.1 gives commit signing,
  code-owner review of changes by others, and accountability for each change to an individual
  account as examples; PW.7 lets the organization choose code review, code analysis or both by the
  stage of the software. Each is an example, not a requirement
  ([SSDF 1.2 draft](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-218r1.ipd.pdf))
  (S).
- SLSA's Build track: L1 needs provenance only and needs no change to the build workflow; L2 needs a
  hosted build platform that signs the provenance; L3 needs isolated runs and a signing secret that
  build steps cannot reach, and usually large changes to the build platform
  ([SLSA build track](https://slsa.dev/spec/v1.2/build-track-basics)) (S). SLSA 1.2 (24 November
  2025) added the Source track and is backwards compatible with 1.1; the announcement was seen in
  search results, and the [spec index](https://slsa.dev/spec/) names version 1.2 (S).
- Scorecard's Branch-Protection check is tiered: tier 1 (3/10) no force push and no branch deletion;
  tier 2 (6/10) adds one required reviewer; tier 3 (8/10) adds one required status check; tier 4
  (9/10) adds two reviewers and code-owner review; tier 5 (10/10) adds stale-review dismissal and
  rules that also bind administrators. Signed-Releases gives 8/10 for a signature on each recent
  release and 10/10 only with SLSA provenance attached; Pinned-Dependencies asks for hash pins in
  workflows, Dockerfiles and scripts; Token-Permissions asks for read-only top-level workflow
  permissions ([Scorecard checks](https://github.com/ossf/scorecard/blob/main/docs/checks.md)) (L).
- OSPS Baseline (2026.08.28): Level 1 includes MFA for sensitive repository actions, no direct
  commits to the primary branch, no unencrypted secrets in version control, a list of direct
  dependencies and published security contacts. Level 2 adds required status checks with an
  automated test suite, signed releases or a signed manifest of hashes, a change log and a
  vulnerability disclosure policy. Level 3 adds approval by at least one non-author human, an SBOM on
  compiled releases, SAST and SCA policies, and threat modelling. It has no explicit pinned-dependency
  control ([OSPS Baseline](https://baseline.openssf.org/versions/2026-08-28)) (S).

**What GitHub charges for them.**

- Protected branches, required reviewers and code owners in private repositories come with Pro
  (personal) or Team (organization), not Free; public repositories on Free get the full feature set
  ([GitHub plans](https://docs.github.com/en/get-started/learning-about-github/githubs-plans)) (L).
- Secret scanning is free for public repositories; for private organization repositories it needs
  the paid GitHub Secret Protection. User push protection is on by default for personal accounts and
  stops pushes of secrets to public repositories
  ([secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning),
  [push protection](https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection))
  (L).
- Since 15 August 2025, an Actions policy can require every action to be pinned to a full commit SHA,
  and an unpinned action then fails the workflow; seen in search results only, detail `UNVERIFIED`
  at the page
  ([GitHub changelog](https://github.blog/changelog/2025-08-15-github-actions-policy-now-supports-blocking-and-sha-pinning-actions/))
  (L). Since 28 October 2025, immutable releases are generally available: tags and assets cannot
  change after publication, and each release gets a signed attestation
  ([GitHub changelog](https://github.blog/changelog/2025-10-28-immutable-releases-are-now-generally-available/))
  (L).
- GitHub says its artifact attestations alone give SLSA Build L2 and, with reusable workflows, can
  meet Build L3. Public repositories sign through the Sigstore public-good instance and private ones
  through GitHub's own; which plans let private repositories use it is `UNVERIFIED`
  ([GitHub](https://docs.github.com/en/actions/concepts/security/artifact-attestations)) (L).
- GitHub's 2026 Actions security roadmap (26 March 2026) says attackers now target CI/CD automation
  itself and names the tj-actions, Nx and trivy-action incidents. Workflow dependency locking, scoped
  secrets and an egress firewall were planned, not shipped, at that date; their status on 2026-10-15
  is `UNVERIFIED`
  ([GitHub blog](https://github.blog/news-insights/product-news/whats-coming-to-our-github-actions-2026-security-roadmap/))
  (L).

| Control | Where the sources place it | Public repository on GitHub | Private repository on GitHub |
| --- | --- | --- | --- |
| CI on every change, as a required status check | OSPS L2; Scorecard tier 3 | free minutes | minutes are metered (`UNVERIFIED` at the pricing page); the required check needs Pro or Team |
| No force push, no branch deletion | Scorecard tier 1; SLSA Source L2 | free | Pro or Team |
| No direct commits to the primary branch | OSPS L1 | free | Pro or Team |
| Required human review | Scorecard tier 2; OSPS L3; SLSA Source L4 (two persons) | free | Pro or Team |
| Code-owner review | Scorecard tier 4; an SSDF 1.2 draft example | free | Pro or Team |
| Rules that also bind administrators | Scorecard tier 5 | free | Pro or Team |
| Actions pinned to a commit SHA; read-only default token | Scorecard Pinned-Dependencies and Token-Permissions | free; an organization policy can enforce pins | free |
| Secret scanning | OSPS L1 (no unencrypted secrets) | free | paid Secret Protection for organization repositories |
| MFA on the account | OSPS L1 | an account setting | an account setting |
| Signed or immutable releases | OSPS L2; Scorecard Signed-Releases 8/10 | one setting | one setting |
| Build provenance (artifact attestations) | SLSA Build L2; Scorecard Signed-Releases 10/10 | free | plan limits `UNVERIFIED` |
| SBOM | OSPS L3 (compiled releases); CRA Annex I | not costed in the sources read | not costed in the sources read |
| Security contacts and disclosure policy | OSPS L1 and L2; CRA Annex I | a file in the repository | a file in the repository |

## 7. Regulation and standards: where they apply (VOLATILE for dates) [as-of 2026-10-15]

Access limits on the reading of 2026-10-15: EUR-Lex returned an empty page for the CRA, so its
articles were read in an unofficial copy of the Official Journal text and on the Commission's pages;
the copy matches the Commission's summary where both speak, but the exact wording is `UNVERIFIED`
against EUR-Lex. iso.org, faa.gov and the AICPA criteria document were not reachable, so ISO/IEC
27001, SOC 2 and DO-178C wording comes from practitioner sources only. Most of the ENISA draft's body
text could not be extracted; only its tables were read.

**NIST SSDF in the United States.**

- SSDF 1.1 is still the last final version; the 1.2 draft's comments closed 30 January 2026, and no
  final version was found on 2026-10-15 ([NIST](https://csrc.nist.gov/projects/ssdf/publications))
  (S). NIST had planned the final 1.2 for 31 March 2026; the draft adds PO.6, a continuous
  process-improvement plan, and PS.4, robust and reliable software updates that are tested and
  responsibly delivered
  ([NIST presentation](https://csrc.nist.gov/csrc/media/presentations/2026/ssdf-and-devsecops-project/1.5a-ssdf_update-booth.pdf))
  (S).
- The 1.2 draft has no text on AI, AI-generated code or coding assistants (a text search found none).
  SP 800-218A (July 2024, final) is an SSDF profile for producers of generative AI models; its page
  does not mention AI coding assistants, and whether the full PDF covers them is `UNVERIFIED`
  ([NIST](https://csrc.nist.gov/pubs/sp/800/218/a/final)) (S).
- OMB memo M-26-05 (23 January 2026) rescinded M-22-18 and M-23-16: federal agencies no longer must
  collect the SSDF self-attestation form from suppliers, though each agency may still ask for it or
  for an SBOM. Read in law-firm summaries only, not the memo
  ([Inside Government Contracts](https://www.insidegovernmentcontracts.com/2026/02/omb-rescinds-the-common-form-secure-software-attestation-requirement/))
  (A).

**EU Cyber Resilience Act (Regulation (EU) 2024/2847).**

- The CRA entered into force on 10 December 2024. Chapter IV (notified bodies) applied from 11 June
  2026, the reporting duties of Article 14 from 11 September 2026, and the main obligations apply from
  11 December 2027 ([Commission](https://digital-strategy.ec.europa.eu/en/policies/cra-summary), page
  last updated 3 December 2025) (S).
- The reporting duty covers every in-scope product on the EU market, including products placed there
  before December 2027: an early warning within 24 hours, a notification within 72 hours and a final
  report, through the single reporting platform (same page (S);
  [Jones Day](https://www.jonesday.com/en/insights/2026/07/eu-cyber-resilience-act-24hour-reporting-duties-start-september-11-2026),
  a law-firm summary seen in search results (A)).
- Scope follows commercial placement on the EU market, not team size. Free software that is not
  monetised is generally out of scope, and a developer who only contributes code to a project they are
  not responsible for is out of scope
  ([Commission](https://digital-strategy.ec.europa.eu/en/policies/cra-open-source)) (S).
- Article 13 requires a documented cybersecurity risk assessment kept up to date, due diligence on
  third-party components including free software, a support period of at least five years (or the
  expected use, if shorter), and technical documentation kept for at least ten years
  ([unofficial copy, Article 13](https://www.european-cyber-resilience-act.com/Cyber_Resilience_Act_Article_13.html))
  (S, unofficial copy).
- Annex I Part II requires an SBOM in a common machine-readable format, covering "at the very least
  the top-level dependencies", a coordinated vulnerability disclosure policy, a reporting contact,
  regular security testing, free security updates without delay, and public advisories once a fix is
  out. Part I requires delivery without known exploitable vulnerabilities and a secure-by-default
  configuration ([unofficial copy, Annex I](https://www.european-cyber-resilience-act.com/Cyber_Resilience_Act_Annex_1.html))
  (S, unofficial copy).
- Microenterprises and small enterprises get no exemption from the essential requirements. They get
  support, sandboxes and a simplified form of technical documentation (Article 33), and no fine for
  missing only the 24-hour early-warning deadline (Article 64(10)(a))
  ([Article 33](https://www.european-cyber-resilience-act.com/Cyber_Resilience_Act_Article_33.html),
  [Article 64](https://www.european-cyber-resilience-act.com/Cyber_Resilience_Act_Article_64.html))
  (S, unofficial copy).
- An open-source software steward (a legal person that supports free software meant for commercial
  use, without placing it on the market itself) must keep a documented cybersecurity policy,
  cooperate with market surveillance authorities and report actively exploited vulnerabilities;
  stewards get no administrative fines (Article 64(10)(b))
  ([Article 24](https://www.european-cyber-resilience-act.com/Cyber_Resilience_Act_Article_24.html),
  unofficial copy; [Commission](https://digital-strategy.ec.europa.eu/en/policies/cra-open-source))
  (S).
- Most products may use self-assessment (module A). Important class I products may self-assess only
  with harmonised standards or a certification scheme; class II and critical products need a third
  party. Free software in classes I and II may self-assess if its technical documentation is public.
  The Commission issued non-binding guidance on 27 July 2026
  ([Commission summary](https://digital-strategy.ec.europa.eu/en/policies/cra-summary),
  [Commission CRA page](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act), last
  updated 7 September 2026) (S).

**EU AI Act, where it reaches development practice.**

- Article 4 (AI literacy) has applied since 2 February 2025 to providers and deployers of AI systems.
  As amended by the Digital Omnibus, it asks them to take measures for their staff's AI literacy "to
  their best extent" and no longer requires a set level
  ([Article 4](https://artificialintelligenceact.eu/article/4/), consolidated text on an unofficial
  site) (S, unofficial copy).
- A deployer is anyone who uses an AI system under its authority, except for personal
  non-professional use ([Article 3](https://artificialintelligenceact.eu/article/3/)) (S, unofficial
  copy). On that definition, a business or a professional working alone who uses coding agents in the
  EU would be a deployer with the Article 4 duty (inference; no source read applies Article 4 to
  coding agents in words).
- The Digital AI Omnibus (reported as Regulation (EU) 2026/1744, in force 27 July 2026) moved the
  high-risk duties to 2 December 2027 for Annex III systems and 2 August 2028 for systems in Annex I
  products; general-purpose model duties were not delayed. The Official Journal text was not reached;
  the regulation number and dates are `UNVERIFIED` at the source
  ([Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/),
  27 May 2026, before adoption, and search-result summaries of adoption) (A).
- A provider of a high-risk AI system needs a quality management system (Article 17): design control,
  development and quality-assurance methods, testing before, during and after development, change
  management, record keeping and named accountability. The text makes it proportionate to the size of
  the provider but keeps the "degree of rigour" the law requires. It reaches projects whose product is
  a high-risk AI system, not projects that only use AI to write code
  ([Article 17](https://artificialintelligenceact.eu/article/17/)) (S, unofficial copy).

**SOC 2 and ISO/IEC 27001.**

- SOC 2 is an examination that a CPA performs and reports on; AICPA does not call it a certification,
  and its guide is titled "Examination of Controls at a Service Organization"
  ([AICPA](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2))
  (S). CC8.1 is in §4.
- ISO/IEC 27001:2022 Annex A has the controls 5.3 (segregation of duties), 8.4 (access to source
  code), 8.25 (secure development life cycle), 8.31 (separation of development, test and production)
  and 8.32 (change management); the current edition and any 2024 amendment are `UNVERIFIED` at
  iso.org, which returned 403 ([Open Security Architecture](https://opensecurityarchitecture.org/frameworks/iso-27001-2022),
  seen in search results) (A).
- ISO does not certify organizations; accredited certification bodies audit an ISMS and issue the
  certificate. Read in search summaries; iso.org returned 403
  ([soc2auditors.org](https://soc2auditors.org/insights/iso-27001-certifying-body/)) (A).

**Safety-critical and medical lifecycles.**

- The FDA's final guidance on computer software assurance for production and quality system software
  (current version February 2026) is risk-based and puts more rigour where risk is higher
  ([FDA](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/computer-software-assurance-production-and-quality-management-system-software))
  (S). `UNVERIFIED`, secondary only: it divides functions into "high process risk" and "not high
  process risk".
- The FDA's 2023 guidance on premarket submissions for device software functions is final
  ([FDA](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/content-premarket-submissions-device-software-functions))
  (S). `UNVERIFIED`, secondary only: it has two documentation levels, Basic and Enhanced, and Enhanced
  applies where a failure could cause a probable risk of death or serious injury.
- The current IEC 62304 is edition 1 (2006) with Amendment 1 (2015); its stability date is 2028
  ([IEC webstore](https://webstore.iec.ch/en/publication/6792)) (S). Under edition 1, the safety class
  comes top-down from risk management: class A needs software requirements, release and (since 2015)
  system tests; class B adds architecture and verification; class C adds detailed design;
  unclassified software counts as class C
  ([Johner Institute](https://blog.johner-institute.com/iec-62304-medical-software/safety-class-iec-62304/),
  rewritten 15 October 2025) (A). That planning, configuration management and problem resolution apply
  to every class is `UNVERIFIED` here.
- Edition 2 was still a working draft on 22 July 2026, with a second committee draft expected in
  August 2026 and requirements that may still change. It replaces classes A, B and C with two process
  rigour levels, widens the scope to health software, and gives AI and agile informative annexes only.
  Other sources claimed an FDIS or an August 2026 publication; no published edition 2 was found
  ([VDE](https://www.vde.com/topics-de/health/fachwissen/iec-62304-edition-2-aenderungen)) (A).
- DO-178C has 71 objectives at level A, 69 at B, 62 at C, 26 at D and none at E. An authority judges
  compliance at four stages of involvement against plans such as the PSAC, SDP, SVP, SCMP and SQAP. A
  tool whose output is not verified must be qualified under DO-330
  ([Rapita Systems](https://www.rapitasystems.com/do178)) (A). Under DO-330, a tool whose output
  becomes part of the airborne software and could insert an error is criteria 1, the most rigorous
  class; no FAA, EASA or RTCA text on LLM code generators was found, and the counts of objectives that
  need independence differ between sources (`UNVERIFIED`) ([AFuzion](https://afuzion.com/?p=358)) (A).

**Guidance on AI coding agents in a controlled lifecycle.**

- ENISA's draft Technical Advisory on AI-assisted software development (version 0.4, September 2026;
  feedback was reported to close on 15 October 2026) maps AI-assisted activities onto lifecycle stages
  and names governance risks: unclear accountability, uncontrolled autonomy, weak traceability,
  insufficient review capacity and unsupported security claims
  ([ENISA draft](https://www.enisa.europa.eu/sites/default/files/2026-09/ENISA%20Technical%20Advisory-AI-assisted-software-development-draft.pdf))
  (S, draft).
- For each AI-assisted activity, the draft asks the team to define who reviews or approves the output
  by the component's sensitivity, the change's scope and the agent's autonomy, and which checks and
  evidence to record (tests, SBOM updates, scans, approvals). Its STRIDE table counts unlogged prompts,
  tool actions and approvals as a repudiation risk. Claims beyond its tables are `UNVERIFIED` (same
  source) (S, draft).
- The Five Eyes guidance on agentic AI is in §3.

**Claims that a template or a repository setting cannot support.** The sources above show why each
of these is outside what a template, a workflow file or a repository setting can establish:

1. A SOC 2 status. SOC 2 is a CPA's examination of an organization's controls, not a certification,
   and a repository has none (AICPA, above).
2. ISO/IEC 27001 certification or compliance. Certification is of an organization's ISMS, by an
   accredited body (above; read in search summaries).
3. CRA conformity, CE readiness or meeting Annex I. Conformity is the manufacturer's assessment and
   declaration, sometimes with a notified body. Delivery "without known exploitable vulnerabilities"
   is not something a template can know (CRA, above).
4. SSDF conformance or satisfying the attestation form. The SSDF is risk-based and gives examples,
   not a prescribed method, and an attestation is the producer's own signed statement (§6, above).
5. A SLSA level as such. Build levels belong to a build platform and Source levels to a source
   control system; GitHub documents its artifact attestations as Build L2 (§6).
6. That an AI review counts as code review, or that an agent is the second reviewer. SLSA and
   Scorecard say it does not (§4).
7. Segregation of duties with one maintainer, or with an admin token in the agent's reach. Scorecard
   calls required review infeasible with one participant, and admin permissions bypass branch
   protection unless bypassing is disallowed (§1, §4).
8. An IEC 62304 safety class, a DO-178C level or a qualified tool. These need a quality management
   system, risk management, plans an authority agrees, and tool qualification (above).
9. AI Act compliance. Article 4 is a duty of effort on the organization, and Article 17 applies only
   to high-risk AI products (above).
10. A fixed date for a law, standard or draft that moved recently (the AI Act high-risk dates, the
    final SSDF 1.2, IEC 62304 edition 2) without the day it was checked.

## 8. Limits and open questions

What the evidence does not cover:

- No source read measures a whole lifecycle for projects that coding agents build. The AI evidence
  measures people who use AI tools, mostly in open-source repositories and often with tools from
  2024–2025. The only series of randomized trials on speed (METR) calls its newest data unreliable.
  The numbers here show a direction, not a size.
- DORA is a self-selected, correlational survey that does not separate solo developers or
  prototypes. The review studies come from Microsoft, Google and large open-source projects and say
  little about a project with one maintainer. Whether review by a model can stand in for a human
  reviewer in a one-person project is not measured.
- No measured study of throwaway prototypes was found, nor of how often prototypes are kept, nor of
  agent-built prototypes.
- No large study of agent-built client work was found, and no maker or study source on client
  contracts and AI use. The client-side evidence (Jørgensen) is `UNVERIFIED`.
- No agent-specific source covers release or retirement beyond the few items in §3.
- Several measured sources sell the tools their results favour (GitClear, CodeRabbit, Faros,
  Veracode), and makers sell the agents whose practice they recommend.
- The capability of the implementing model and harness is a likely factor (Boehm's personnel axis,
  METR's experienced developers), but no source measures it as a lifecycle factor.
- Maker features move monthly: Copilot approvals arrived in September 2026, the default AI review
  ruleset went in August 2026, and Gemini CLI was replaced for some users in June 2026. The regulation
  texts were read partly through unofficial copies and summaries (§7).

Open: whether an AI first-pass review lowers escaped defects in agent pull requests; how review
capacity should be measured against agent output; whether the agent-era drop in stability that DORA
reports persists with newer tools; how auditors will treat approval of agent-written code under SOC 2
and ISO/IEC 27001.

## Sources

All sources were read on 2026-10-15. Each is linked where its claim stands. The main ones:

- DORA: the 2019 State of DevOps report, the 2024 and 2025 reports and their announcements, the AI
  Capabilities Model, and the capability pages on small batches, trunk-based development,
  documentation quality, change approval and the delivery metrics.
- Google: the SRE book (embracing risk, release engineering), the SRE workbook (error budget policy),
  Software Engineering at Google (chapters 1, 9 and 16), and the modern code review case study.
- Measured studies: METR (2025 and 2026); arXiv 2410.12944, 2507.00788, 2511.04427, 2601.00477,
  2507.15003, 2602.04226, 2601.15195, 2601.18341, 2607.07980, 2510.24265, 2602.11988, 1609.04886,
  1611.10288, 2109.11435, 1604.06766, 1906.08058 and 2309.12434; the Microsoft code review and
  organizational structure studies; the Qt, VTK and ITK review study; the ICSA 2026 ADR study; vendor
  reports by GitClear, CodeRabbit, Veracode, Faros and Anthropic.
- Frameworks: Cockburn (c2.com), Boehm (2002), Clarke and O'Connor (2012).
- Makers' guidance: Anthropic, OpenAI, GitHub, Google (Gemini CLI, Jules), Cursor and Kiro pages
  linked in §3 and §4.
- Standards and regulation: NIST SSDF 1.1, the 1.2 draft and SP 800-218A; SLSA 1.2; OpenSSF
  Scorecard and the OSPS Baseline; GitHub's plan, secret scanning, branch protection and attestation
  pages; the Commission's CRA pages and an unofficial copy of the CRA; an unofficial consolidated text
  of the AI Act; AICPA; the IEC webstore; FDA guidance; the ENISA draft advisory; the UK NCSC blog.
- Practitioner sources, each one account (A): law firms, certification bodies and consultancies
  linked in §4 and §7; Willison; Böckeler; Industrial Empathy; Google Cloud's office of the CTO.
