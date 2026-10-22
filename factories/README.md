---
last_checked: 2026-10-23
volatility: MONITOR (new definitions, frameworks and product names appeared every month of 2026) / STABLE (§2, the earlier meanings of the term)
sources:
  - https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/ (read 2026-10-23)
  - https://factory.strongdm.ai/ (read 2026-10-23)
  - https://factory.strongdm.ai/techniques (read 2026-10-23)
  - https://factory.strongdm.ai/principles (read 2026-10-23)
  - https://simonwillison.net/2026/Feb/7/software-factory/ (read 2026-10-23)
  - https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/ (read 2026-10-23)
  - https://openai.com/index/harness-engineering/ (read 2026-10-23)
  - https://www.latent.space/p/harness-eng (read 2026-10-23)
  - https://factory.ai/news/software-factory (read 2026-10-23)
  - https://factory.ai/articles/what-is-a-software-factory (read 2026-10-23)
  - https://addyosmani.com/blog/software-factories/ (read 2026-10-23)
  - https://github.com/mattpocock/dictionary-of-ai-coding (read 2026-10-23)
  - https://posthog.com/newsletter/software-factories (read 2026-10-23)
  - https://xebia.com/articles/shining-some-light-in-dark-agentic-software-factories/ (read 2026-10-23)
  - https://bcgplatinion.com/insights/the-dark-software-factory (read 2026-10-23)
  - https://www.thoughtworks.com/content/dam/thoughtworks/documents/report/tw_future_of_software_engineering_europe_2026.pdf (read 2026-10-23)
  - https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/ (read 2026-10-23)
  - https://githubnext.com/projects/continuous-ai/ (read 2026-10-23)
  - https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/ (read 2026-10-23)
  - https://martinfowler.com/articles/harness-engineering.html (read 2026-10-23)
  - https://ai.engineer/talks/harness-engineering-is-not-enough-why-software-factories-fail (read 2026-10-23)
  - https://lukepm.com/blog/the-software-factory/ (read 2026-10-23)
  - https://sundaylettersfromsam.substack.com/p/i-have-seen-the-compounding-teams (read 2026-10-23)
  - https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04 (read 2026-10-23)
  - https://ghuntley.com/loop/ (read 2026-10-23)
  - https://dspace.mit.edu/handle/1721.1/47992 (read 2026-10-23)
  - https://www.cs.dartmouth.edu/~doug/components.txt (read 2026-10-23)
  - https://learn.microsoft.com/en-us/previous-versions/aa480032(v=msdn.10) (read 2026-10-23)
  - https://dodcio.defense.gov/Portals/0/Documents/Library/DoD%20Enterprise%20DevSecOps%20Fundamentals%20v2.5.pdf (read 2026-10-23)
  - https://www.gao.gov/assets/gao-23-105611.pdf (read 2026-10-23)
  - https://www.fanuc.co.jp/en/profile/production/index.html (read 2026-10-23)
---

# Software factories: what the term means, what a factory is made of, and where the library covers it

Re-check when a lab or a major platform publishes its own definition of a software factory or a dark
factory; when an operator publishes measured output, defect or cost results for a factory; when a
standards body or regulator addresses code that no person reviewed; or after 30 days. §2 (the
earlier meanings) changes only when a new historical source is read.

A software factory, in the sense this pillar covers, is a setup in which coding agents take work
from a trigger, a ticket or a spec to merged and sometimes deployed code, with less human writing,
starting or reading of the code than in attended agent work. A **dark factory** is one in which no
person reads the code. This page says how the term is defined and by whom, what it meant before
coding agents, which ladders of autonomy use it, what parts every description of a factory has, and
which other documents in this library cover each part. It describes the sources. It does not say
whether to build a factory.

The pillar has four documents:

| Document | Holds |
| --- | --- |
| This page | Definitions, earlier meanings, autonomy ladders, the parts of a factory, and links to the rest of the library |
| [operators.md](operators.md) | The organizations that publicly describe running a factory or a pipeline close to one: what they built, at what scale, with what human role and what checks, and what went wrong |
| [platforms.md](platforms.md) | The products and open orchestrators that provide factory machinery: intake, orchestration, verification, merge, and the guardrails each one enforces |
| [evidence.md](evidence.md) | The evidence for and against factories: measured studies, positions on both sides, incidents and forecasts |

**Evidence classes.** (M) measured: an experiment, telemetry or a counted observation; a vendor's
own measure of its own product is (M, vendor). (L) the documentation or guidance of a lab, a tool
vendor or a platform. (P) practitioner consensus. (A) one person's or one firm's account, or a
framework that its authors did not test against data. (S) the text of a standard, a law or a
government body. (F) forecast, with its falsifier and horizon. (O) own result; this pillar has none.
"Inference" marks a step that no source states in words. `UNVERIFIED` marks a claim read only in a
secondary source or a search summary, not at its primary source.

**Citations.** Every URL in this document was read on 2026-10-23, unless the text gives another
date. Each claim names its source by a link. This document has no ledger records in
[`_evidence/`](../_evidence/); its sources have not had the independent fact-check that the
[conventions](../CONVENTIONS.md) describe. A second reader re-read the key findings SF1 to SF7, every quotation
and the body's numbers and dates at their sources on 2026-10-23, together with those of
[platforms.md](platforms.md) (about 75 body claims across the two): 4 key findings and 6 body claims
in this document were corrected, and every quotation was exact.

## Key findings

**SF1. "Software factory" has no agreed criteria, and the 2026 definitions differ in what they take
the person out of.** Some remove the person from reading the code (Shapiro's level 5, StrongDM's two
rules, Osmani's and Pocock's "dark"). Pocock's dictionary removes the person only from starting
sessions. Factory, Osmani's "light factory", BCG Platinion and Thoughtworks describe a managed loop
with a range of autonomy that keeps human review where errors are expensive. PostHog says that the
term is a metaphor with no criteria. (A, L) — §1.

**SF2. "Dark" means that no person reads the code, and it comes from lights-out manufacturing.**
Shapiro takes "dark" from FANUC's robot factory and does not claim to coin the term. StrongDM's two
rules (humans do not write code; humans do not review code) are the most quoted form. Simon Willison
credits Shapiro with naming the approach. (A) — §1, §3.

**SF3. The term is more than fifty years old and still has a live meaning without agents.** Bemer
gave a first working definition in 1968, Hitachi named a real facility a factory in 1969, Microsoft
used the term in 2004 for development environments configured for one type of application, and the US DoD defines a software factory as
people, tools and processes that deliver software continuously; GAO counted 29 DoD factories in 2023.
Inference: in each of these meanings, people write and review the code. (A, L, S) — §2.

**SF4. The ladders of autonomy measure different things.** Shapiro's six levels (0 to 5) rank the
person's role from writing code to not reading it; Yegge's eight stages rank trust and parallelism;
Pocock and PostHog separate two axes (who starts the work, and how closely people read the output).
Thoughtworks' retreat report recommends choosing the level per system or component by risk,
reversibility and blast radius. (A, P) — §4.

**SF5. Every agentic description has intake, automated verification and a feedback loop; they
disagree on the review gate, on merge and on how to keep the agent from gaming its own checks.**
StrongDM often keeps its scenarios outside the codebase as a holdout set and runs them against clones of
third-party services; most other descriptions use conventional checks plus a review gate.
Inference from the sources compared in §5. (A, L) — §5.

**SF6. Only one team, StrongDM's AI team, claims a factory with no human writing and no human review
of code, and it has published no results.** Most operators that publish numbers run high
agent authorship with human review or human merge approval. Moderate: all figures are self-reported
and counted in different ways. (A, M vendor) — [operators.md](operators.md).

**SF7. Most products stop at a pull request that a person merges, but they enforce that stop in
different places.** GitHub enforces it in the platform; other products leave it to branch
protection, to the agent's prompt or to the person's own instruction. Since 2026-09-01 a Copilot
approval can satisfy a required review on GitHub, and Cursor documents an agent that approves
low-risk pull requests (its launch date was not found). (L) —
[platforms.md](platforms.md).

## 1. What the term means now (MONITOR)

**Origins in agent work, 2024 to February 2026.**

- Agentic uses of "software factory" came before the best-known posts. A post on LukePM.com
  (2024-12-24) forecast a factory of teams of AI agents in which speed would matter more than code
  quality ([LukePM](https://lukepm.com/blog/the-software-factory/)) (F; no horizon stated). Sam
  Schillace (2025-09-28) described "compounding teams" that do not write code, run 5 to 10 parallel
  processes and spend hundreds of dollars a day on API calls
  ([Sunday Letters](https://sundaylettersfromsam.substack.com/p/i-have-seen-the-compounding-teams))
  (A). Steve Yegge (2026-01-01) called his Gas Town orchestrator an industrialized coding factory
  ([Yegge](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)) (A), and Geoffrey
  Huntley (2026-01-17) equated a later level of autonomous loops that evolve products with a software
  factory ([Huntley](https://ghuntley.com/loop/)) (A).
- Dan Shapiro (2026-01-23) published a ladder of six levels, 0 to 5, modelled on the US NHTSA's 2013
  levels of driving automation. At level 5 the person writes specifications and the agent writes,
  tests and ships the code; Shapiro calls it "a black box that turns specs into software"
  ([Shapiro](https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/))
  (A). He says that level-5 teams are small (fewer than five people) and that this is probably the
  future (F; no horizon stated). The level names appear only in the post's images, and the images
  disagree: level 5 is "Software Factory" in one and "Dark Software Factory" in another. The page
  title says "Dark Factory" and the URL says "software-factory" (A; inference: the title changed
  after publication, not confirmed).
- StrongDM's AI team (2026-02-06) defines its Software Factory as non-interactive development in
  which specs and scenarios drive agents that write code, run harnesses and converge "without human
  review" ([StrongDM](https://factory.strongdm.ai/)) (A). It states two rules: humans must not write
  code, and humans must not review code. It sets a target, not a measured cost, of at least
  $1,000 of tokens per human engineer per day. Its techniques page treats the code as opaque, like
  the weights of a model, and judges it only by its observable behaviour
  ([StrongDM techniques](https://factory.strongdm.ai/techniques)) (A).
- Simon Willison wrote up StrongDM's approach (2026-02-07), worked out that the token target is about
  $20,000 a month per engineer, and said the patterns interest him much less at that cost unless they
  also work at lower spend ([Willison](https://simonwillison.net/2026/Feb/7/software-factory/)) (A).
  In his review of 2026 (2026-09-27) he credits Shapiro with naming the approach the Dark Factory and
  says that StrongDM's first rule, that humans write no code, sounded radical in February and now
  describes how many people work, while the second, no human review, is still much debated
  ([Willison](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/)) (A).
- OpenAI's "Harness engineering" post (February 2026; the day, 11 February, comes from a search
  summary only) reports an internal product built with no manually written code, in which "Humans may
  review pull requests, but aren’t required to"
  ([OpenAI](https://openai.com/index/harness-engineering/)) (A). The post does not use the word
  factory. Latent Space presented that team's practice of merging with no human review to "Dark
  Factory" fans on 2026-04-07
  ([Latent Space](https://www.latent.space/p/harness-eng)) (A). [operators.md](operators.md) gives
  the numbers.

**Definitions from vendors, consultants and practitioners, March to October 2026.**

| Source and date | What it calls a factory | What the person keeps |
| --- | --- | --- |
| BCG Platinion, 2026-03-26 ([BCG](https://bcgplatinion.com/insights/the-dark-software-factory)) (A) | An "Agentic Software Factory" in which agents build, test and ship around the clock; it reuses AWS's AI-DLC phases | Business intent and review of outcomes; it calls the change a relocation of human effort, not its absence |
| Factory, 2026-06-15 ([Factory 2.0](https://factory.ai/news/software-factory)) (L, vendor) | A loop: signals (bug reports, feedback, requirements) are triaged into planned changes that are built, tested, reviewed, secured, shipped and monitored, and monitoring makes new signals | A range of autonomy; it says that no organization starts with a fully autonomous factory |
| Factory, 2026-07-18 ([Factory article](https://factory.ai/articles/what-is-a-software-factory)) (L, vendor) | A managed model with repeatable inputs, standard tooling, measurable output and enough kept context to rebuild each change, with or without agents | Human review and release controls at the start |
| Thoughtworks retreat, 28–30 June 2026 ([report](https://www.thoughtworks.com/content/dam/thoughtworks/documents/report/tw_future_of_software_engineering_europe_2026.pdf)) (P) | Full automation at the "dark-factory" end of a scale that starts at human oversight | A risk tier chosen per system or component; verification, not generation, is the bottleneck |
| Dex Horthy, AI Engineer World's Fair talk, 29 June to 2 July 2026 ([AI Engineer](https://ai.engineer/talks/harness-engineering-is-not-enough-why-software-factories-fail)) (A) | The lights-off factory that he credits to Shapiro | He argues for turning review back on and moving decisions earlier ([evidence.md](evidence.md)) |
| Xebia, 2026-07-30 ([Xebia](https://xebia.com/articles/shining-some-light-in-dark-agentic-software-factories/)) (A) | An assembly line of planning, implementing and reviewing agents with deterministic stations | Optional human stations |
| Addy Osmani, 2026-07-20 ([Osmani](https://addyosmani.com/blog/software-factories/)) (A) | Many harnessed loops at once, fed by a work queue and drained through one review gate into production; a loop is one agent on one job, a harness is the sandbox, tools, memory and "done" gates around it | In a light factory, human judgment where errors are expensive, moved toward design; a dark factory ships code no person has read |
| PostHog, 2026-08-11 ([PostHog](https://posthog.com/newsletter/software-factories)) (A) | A metaphor with no criteria, placed on two axes: the share of code agents write and how closely people read it | It places PostHog, Ramp, Cursor and Uber between the ends |
| Matt Pocock's dictionary, entries first committed 2026-09-24 ([dictionary](https://github.com/mattpocock/dictionary-of-ai-coding)) (A) | Triggers (an issue, a schedule, a CI failure, another session ending) start agent sessions instead of a person | Anything else; a dark factory is an area where no person reads the output, and unattended sessions whose pull requests a person reviews are a factory but not a dark one |

**Framings that keep the person in the loop and do not use the word.**

- GitHub Next's "Continuous AI" (June 2025) is a category label, by analogy with CI/CD, for any
  automated use of AI in software collaboration; GitHub says it does not own the term and that such
  workflows usually involve human oversight ([GitHub Next](https://githubnext.com/projects/continuous-ai/))
  (L).
- AWS's AI-Driven Development Lifecycle (AI-DLC, 2025-07-31) is a method in which the AI plans, asks
  for clarification and leaves critical decisions to people, in phases of hours or days that AWS calls
  "bolts" ([AWS](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/)) (L).
- Birgitta Böckeler on martinfowler.com defines a harness as everything in an agent except the model,
  splits its outer part into guides and sensors, and frames the aim as less supervision, not the end
  of review; the article does not use "software factory"
  ([martinfowler.com](https://martinfowler.com/articles/harness-engineering.html)) (A).

**A critique of the definition itself.** Stanford CodeX (2026-02-08) argues that a dark factory
moves responsibility for software behaviour onto a system that law is not ready for, and that
StrongDM's LLM-judged satisfaction score has the same class of system write and judge the code
([Stanford CodeX](https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/))
(A). [practices/llm-as-judge.md](../practices/llm-as-judge.md) holds what is measured about model
judges.

## 2. Earlier meanings of the term (STABLE)

A reader who meets "software factory" outside agent work most likely meets one of these meanings.

- **Bemer, 1968.** Michael Cusumano's 1989 MIT working paper credits R. W. Bemer of General Electric
  with a 1968 paper that urged GE to build a "software factory" of standard tools, a computer-based
  environment and historical data for cost and schedule control, and calls it the industry's first
  working definition ([Cusumano](https://dspace.mit.edu/handle/1721.1/47992)) (A; Bemer's paper itself
  was not read).
- **McIlroy, 1968.** At the NATO software engineering conference (Garmisch, October 1968), M. D.
  McIlroy proposed mass-produced software components, made by a components industry, in a paper with
  a section titled "A Components Factory" ([McIlroy](https://www.cs.dartmouth.edu/~doug/components.txt))
  (A). Cusumano treats this reuse idea as separate from Bemer's tools-and-controls idea. Inference:
  the statement in Horthy's talk that the term was defined at the NATO conference merges the two.
- **Hitachi, 1969, and SDC, 1975–76.** Cusumano reports that Hitachi's Software Works (1969) was the
  first real software facility to carry the name factory, and that System Development Corporation set
  up the first US facility called a software factory in 1975–76 and copyrighted the name
  ([Cusumano](https://dspace.mit.edu/handle/1721.1/47992)) (A). His 1991 book *Japan's Software
  Factories* was not read (`UNVERIFIED`).
- **Microsoft, 2004.** Jack Greenfield and Keith Short's Software Factories are development
  environments configured for the rapid development of one type of application, built from patterns,
  models, frameworks and tools (inference: a product-line approach, a term the article uses only for
  other industries); Greenfield says software development will never become a purely
  mechanical process ([Greenfield](https://learn.microsoft.com/en-us/previous-versions/aa480032(v=msdn.10)))
  (L).
- **US Department of Defense, current.** The DoD CIO's DevSecOps Fundamentals v2.5 (approved
  2024-10-16) defines a software factory as people, tools and processes that deliver software
  continuously to a user community, with automation in place of manual steps
  ([DoD CIO](https://dodcio.defense.gov/Portals/0/Documents/Library/DoD%20Enterprise%20DevSecOps%20Fundamentals%20v2.5.pdf))
  (S). GAO-23-105611 (2023-04-05) reports 29 DoD software factories, among them the Air Force's
  Platform One and Kessel Run and the Army Software Factory
  ([GAO](https://www.gao.gov/assets/gao-23-105611.pdf)) (S). Inference from the definitions: in this
  meaning people write and review the code, and the factory automates delivery.

## 3. The lights-out analogy

FANUC's own page on its factories describes highly automated plants and long runs of continuous
unmanned machining, but it does not use the words "lights-out" or "dark" and gives no run length
([FANUC](https://www.fanuc.co.jp/en/profile/production/index.html)) (L, vendor). The figures often
repeated in factory writing, that FANUC robots build robots unattended for up to 30 days and have run
lights-out since 2001, were found only in secondary sources (`UNVERIFIED`).

Writers use the analogy for one specific removal. For Shapiro the person is not needed on the floor;
for Osmani the floor in software is the diff, so dark means no person reads the diff; for Pocock no
person reads the output. Factory, Xebia and BCG Platinion use the assembly line instead, for flow and
stations, not for the absence of people (inference from the sources in §1).

## 4. Ladders and axes of autonomy (MONITOR)

| Source | Steps | What it ranks |
| --- | --- | --- |
| Shapiro, 2026-01-23 | Six levels, 0 to 5: AI as search or completion; discrete tasks handed to AI; pairing with an AI-native tool; the person reviews every AI diff, where Shapiro says nearly everyone stops; the person acts as a product manager who writes specs and checks the tests after leaving the agent for hours; the dark factory | The person's role relative to the code: writing it, reviewing it, or neither ([Shapiro](https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/)) (A) |
| Yegge, 2026-01-01 | Eight stages: near-zero AI; an IDE agent with permissions; the same in YOLO mode; a wide IDE agent; one CLI agent in YOLO mode; 3 to 5 parallel CLI agents; 10 or more hand-managed agents; your own orchestrator | Trust in the agent and the number of agents run at once ([Yegge](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)) (A) |
| Pocock, 2026-09 | Two axes | Who starts the session (a person or a trigger), and who reads the output ([dictionary](https://github.com/mattpocock/dictionary-of-ai-coding)) (A) |
| PostHog, 2026-08-11 | Two axes | The share of code that agents write, and how closely people read it ([PostHog](https://posthog.com/newsletter/software-factories)) (A) |
| Thoughtworks retreat, 2026-06 | A tier per system or component, from oversight to full automation | Risk, reversibility and blast radius of the component ([report](https://www.thoughtworks.com/content/dam/thoughtworks/documents/report/tw_future_of_software_engineering_europe_2026.pdf)) (P) |

Inference: Shapiro's top level is defined by the person not reading code, and Yegge's top stage by
the person automating the management of agents; a setup can be high on one and low on the other.
Osmani's rule of back-pressure, to give a loop only as much autonomy as can be verified cheaply and
reliably ([Osmani](https://addyosmani.com/blog/software-factories/)) (A), and the Thoughtworks tiers
both tie the level to the cost of checking and of failing, not to the team.

## 5. The parts of a factory

Every agentic description read has intake from a trigger, a ticket or a spec, an automated
verification layer, and a loop that feeds results back. The table compares where they differ. Each
cell paraphrases what the source says; "not described" means the source does not name the part.
The table is an inference from the sources in §1 and from [platforms.md](platforms.md).

| Part | StrongDM | OpenAI harness team | Factory | Osmani, Horthy | Pocock | AWS AI-DLC | DoD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Intake | A "seed": a PRD, a spec, a few sentences, a screenshot or a codebase | A person's prompt; tickets on a Linear board in OpenAI's Symphony | Signals, triaged into a plan | A work queue fed by intent and production signals | Triggers: an issue, a schedule, a CI failure, a session ending | Inception phase, worked on in a group | User needs |
| Orchestration | Attractor, a graph of phases | Codex loops; Symphony | Droids, Automations, Missions | Harnessed loops | Sessions started by triggers | The AI plans and waits for validation | CI/CD pipelines |
| Verification | Scenarios kept outside the codebase, judged by a model, run against clones of third-party services | Agent review, driving the app, observability per worktree, linters and structural tests | Test and security stages | CI, tests and scanning; verification is the bottleneck | Automated checks | Generated tests that the team validates | Automated tests |
| Human review | Forbidden | Optional; mostly agent to agent | Kept at first | One review gate; removed in a dark factory | Allowed anywhere; none in a dark factory | Required at each step | People write and review |
| Merge | Converges without review | Agents often merge their own pull requests | Ship stage | After the review gate | Agents merge in a dark factory | The team | Release |
| Deploy | Not described | Not detailed | Ship stage | Into production | Not described | Operations phase | Delivery |
| Feedback | Loop until the holdout scenarios pass and keep passing | Clean-up and doc-gardening agents | Monitoring makes new signals | Monitoring makes new signals | Another session finishing | Operations context | Continuous feedback |

Sources for the columns: [StrongDM](https://factory.strongdm.ai/),
[StrongDM techniques](https://factory.strongdm.ai/techniques),
[StrongDM principles](https://factory.strongdm.ai/principles),
[OpenAI](https://openai.com/index/harness-engineering/), [Factory 2.0](https://factory.ai/news/software-factory),
[Osmani](https://addyosmani.com/blog/software-factories/),
[AI Engineer](https://ai.engineer/talks/harness-engineering-is-not-enough-why-software-factories-fail),
[dictionary](https://github.com/mattpocock/dictionary-of-ai-coding),
[AWS](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/),
[DoD CIO](https://dodcio.defense.gov/Portals/0/Documents/Library/DoD%20Enterprise%20DevSecOps%20Fundamentals%20v2.5.pdf).

Several sources (StrongDM, Osmani, Horthy, Stanford CodeX) say that checks the agent can see or
rewrite are not enough. StrongDM often keeps its scenarios outside the codebase because, it reports, agents
returned a constant true value to pass narrowly written tests ([StrongDM](https://factory.strongdm.ai/))
(A). Factory Research reports a similar design, a validator that writes hidden behavioural tests for
an implementer that never sees them ([platforms.md](platforms.md)) (M, vendor). Measured results on
hidden and visible checks are in [evidence.md](evidence.md) and in
[practices/work-breakdown.md](../practices/work-breakdown.md) (F3 and the section on independent
results on visible checks).

## 6. Where the rest of the library covers each part

A factory is built from parts that other documents here already cover for attended agent work. This
table maps them. The documents it names describe agents and practices in general; none of them was
written about factories.

| Factory concern | Document | What it holds that bears on a factory |
| --- | --- | --- |
| How large a unit of work an unattended agent can finish, who cuts it, and how long runs fail | [practices/work-breakdown.md](../practices/work-breakdown.md) | P1 (a ticket is an acceptance unit with milestones inside it), P5 (acceptance boundaries only where a person's judgment is needed), P6 and F9 (parallel writers cost reliability and tokens; Yegge's merge-queue problem), F3 (long unattended runs degrade: compounding errors, lock-in, test-passing work that reviewers would not merge), F4 (decomposition has moved inside the task: Factory Missions, Anthropic's planner harnesses, Ralph loops) |
| Which facts about a project set its lifecycle, and what agents change at each stage | [practices/project-lifecycle.md](../practices/project-lifecycle.md) | LC4 (agents raise the volume of code; measured delivery gains are small or short-lived), LC5 (review is the measured constraint), LC6 (standards bodies do not count an AI reviewer as the second person), LC7 (guards on irreversible acts sit in the platform), §1 on attended against unattended background work, §3 on what agents change from intake to deploy, §7 on regulation |
| Whether and how an AI reviewer can stand in for a person | [practices/review.md](../practices/review.md) | RV1 to RV3 (what a fresh second reader finds), RV9 and §8 (AI reviewers as a merge gate on GitHub) |
| What lets an unattended agent act, and how a grant is enforced | [practices/agent-authorization.md](../practices/agent-authorization.md) | A1 (containment over approval), A7 (untrusted content crossing the boundary), A9 (an agent under its person's account cannot give that person a second approval) |
| Where long runs keep their state and why they stall | [practices/agent-workspace.md](../practices/agent-workspace.md) | W6 (unattended runs stop where the process needs the person), W8 (state in files survives compaction), W9 (a delegate's report is a claim) |
| Tests the agent can see and tests it cannot | [practices/testing.md](../practices/testing.md), [practices/agent-evals.md](../practices/agent-evals.md) | What makes a test worth keeping; how to grade agent runs |
| A model that judges another model's output | [practices/llm-as-judge.md](../practices/llm-as-judge.md) | Validity and bias of model judges, which bear on LLM-scored scenarios |
| How a cloud session runs, what it reaches and how work leaves it | [harnesses/cloud-sessions.md](../harnesses/cloud-sessions.md), [harnesses/non-interactive-modes.md](../harnesses/non-interactive-modes.md) | The execution layer under a factory: setup, network, output, exit codes |
| Decomposing a long goal and keeping it on track | [practices/long-context-and-compaction.md](../practices/long-context-and-compaction.md) | What compaction keeps and loses over a long run |

## 7. Limits and open questions

- No lab, standards body or regulator has published a definition of a software factory or a dark
  factory in the agentic sense; every definition in §1 is a practitioner's, a vendor's or a
  consultant's.
- No primary FANUC source was found for "lights-out", the 30-day unattended run or the 2001 start
  date. Bemer's 1968 paper and Cusumano's 1991 book were not read; both are cited through Cusumano's
  1989 working paper.
- Whether Shapiro changed his post's title, and when, is not confirmed.
- The ladders in §4 are not tested against data. No source measures whether a team's level predicts
  its outcomes.
- "Background agent" was not traced to a primary definition.
- This page will change when an operator publishes measured factory results, when a platform lets an
  agent's own pull request merge with no human approval by default, or when a standard addresses code
  that no person reviewed.

## Sources

All read on 2026-10-23.

**The current meaning.** Dan Shapiro, The Five Levels, 2026-01-23
<https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/>;
StrongDM, Software Factories And The Agentic Moment, 2026-02-06 <https://factory.strongdm.ai/> and
Techniques <https://factory.strongdm.ai/techniques> and Principles
<https://factory.strongdm.ai/principles>; Simon Willison, 2026-02-07
<https://simonwillison.net/2026/Feb/7/software-factory/> and 2026-09-27
<https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/>; OpenAI, Harness engineering, February
2026 <https://openai.com/index/harness-engineering/> (read through a reader rendering, as the page
refused direct fetches); Latent Space, 2026-04-07 <https://www.latent.space/p/harness-eng>; LukePM,
2024-12-24 <https://lukepm.com/blog/the-software-factory/>; Sam Schillace, 2025-09-28
<https://sundaylettersfromsam.substack.com/p/i-have-seen-the-compounding-teams>; Steve Yegge,
2026-01-01 <https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04>; Geoffrey Huntley,
2026-01-17 <https://ghuntley.com/loop/>.

**Vendors, consultants and practitioners.** Factory, 2026-06-15
<https://factory.ai/news/software-factory> and 2026-07-18
<https://factory.ai/articles/what-is-a-software-factory>; BCG Platinion, 2026-03-26
<https://bcgplatinion.com/insights/the-dark-software-factory>; Thoughtworks, retreat findings, June
2026 <https://www.thoughtworks.com/content/dam/thoughtworks/documents/report/tw_future_of_software_engineering_europe_2026.pdf>;
Dex Horthy, AI Engineer World's Fair, 29 June to 2 July 2026
<https://ai.engineer/talks/harness-engineering-is-not-enough-why-software-factories-fail>; Addy
Osmani, 2026-07-20 <https://addyosmani.com/blog/software-factories/>; Xebia, 2026-07-30
<https://xebia.com/articles/shining-some-light-in-dark-agentic-software-factories/>; PostHog,
2026-08-11 <https://posthog.com/newsletter/software-factories>; Matt Pocock, Dictionary of AI Coding
<https://github.com/mattpocock/dictionary-of-ai-coding>; Stanford CodeX, 2026-02-08
<https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/>; GitHub Next,
Continuous AI, June 2025 <https://githubnext.com/projects/continuous-ai/>; AWS, AI-DLC, 2025-07-31
<https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/>; Birgitta Böckeler,
martinfowler.com <https://martinfowler.com/articles/harness-engineering.html>.

**Earlier meanings and the analogy.** Michael A. Cusumano, Factory Concepts and Practices in Software
Development, MIT Sloan working paper 3095-89, 1989 <https://dspace.mit.edu/handle/1721.1/47992>; M. D.
McIlroy, Mass Produced Software Components, 1968 <https://www.cs.dartmouth.edu/~doug/components.txt>;
Jack Greenfield, The Case for Software Factories, July 2004
<https://learn.microsoft.com/en-us/previous-versions/aa480032(v=msdn.10)>; DoD CIO, DoD Enterprise
DevSecOps Fundamentals v2.5, 2024
<https://dodcio.defense.gov/Portals/0/Documents/Library/DoD%20Enterprise%20DevSecOps%20Fundamentals%20v2.5.pdf>
and GAO-23-105611, 2023 <https://www.gao.gov/assets/gao-23-105611.pdf> (both read through a reader
rendering); FANUC, Factories <https://www.fanuc.co.jp/en/profile/production/index.html>.
