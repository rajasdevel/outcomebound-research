---
last_checked: 2026-10-23
volatility: MONITOR (operators publish new self-reported shares and volumes every few months)
sources:
  - https://factory.strongdm.ai/ (read 2026-10-23)
  - https://factory.strongdm.ai/products (read 2026-10-23)
  - https://factory.strongdm.ai/weather-report (read 2026-10-23)
  - https://simonwillison.net/2026/Feb/7/software-factory/ (read 2026-10-23)
  - https://openai.com/index/harness-engineering/ (read 2026-10-23)
  - https://github.com/openai/symphony (read 2026-10-23)
  - https://www.anthropic.com/research/building-c-compiler (read 2026-10-23)
  - https://www.anthropic.com/institute/recursive-self-improvement (read 2026-10-23)
  - https://x.com/bcherny/status/2004887829252317325 (read 2026-10-23)
  - https://cursor.com/blog/scaling-agents (read 2026-10-23)
  - https://cursor.com/blog/self-driving-codebases (read 2026-10-23)
  - https://cursor.com/blog/self-hosted-machines (read 2026-10-23)
  - https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents (read 2026-10-23)
  - https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2 (read 2026-10-23)
  - https://engineering.atspotify.com/2026/6/code-with-claude-coding-is-no-longer-the-constraint (read 2026-10-23)
  - https://engineering.atspotify.com/2026/9/ai-changed-how-spotify-builds-what-we-learned-and-fixed-about-quality-at-higher-velocity (read 2026-10-23)
  - https://builders.ramp.com/post/why-we-built-our-background-agent (read 2026-10-23)
  - https://shopify.engineering/under-the-river (read 2026-10-23)
  - https://shopify.engineering/river-vulnerability-remediation (read 2026-10-23)
  - https://www.uber.com/us/en/blog/efficient-software-factory/ (read 2026-10-23)
  - https://ai.engineer/talks/17-YSUHo6Lk-agentic-sdlc-at-uber-building-blocks-ubers (read 2026-10-23)
  - https://www.uber.com/us/en/blog/ai-code-cleanup/ (read 2026-10-23)
  - https://www.coinbase.com/blog/interviewing-engineers-in-the-ai-era-lessons-from-a-year-of-rebuilding (read 2026-10-23)
  - https://www.coinbase.com/blog/coding-had-a-concurrency-problem-how-mux-helped-solve-it (read 2026-10-23)
  - https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/ (read 2026-10-23)
  - https://devblogs.microsoft.com/dotnet/ten-months-with-cca-in-dotnet-runtime/ (read 2026-10-23)
  - https://www.aboutamazon.com/news/company-news/amazon-outage-ai-financial-times-correction (read 2026-10-23)
  - https://www.latent.space/p/notion (read 2026-10-23)
  - https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md (read 2026-10-23)
  - https://workos.com/blog/project-horizon (read 2026-10-23)
  - https://www.latent.space/p/software-factories (read 2026-10-23)
---

# Software factory operators: who runs one, at what scale, with what checks

Re-check when an operator publishes measured output, defect, revert or cost results for its factory;
when StrongDM publishes results; when a firm in the table reports a new share or a return to human
review; or after 30 days.

Which organizations publicly describe running a software factory, or a pipeline close to one, in
which agents write and land most or all of the code; what each built, at what scale, with what
human role and what checks; and what went wrong. The definitions are in [README.md](README.md); the
products these firms build on or sell are in [platforms.md](platforms.md); studies and positions
are in [evidence.md](evidence.md). This page describes what the firms say about themselves. It
does not rank them.

**Evidence classes.** As in [README.md](README.md). A firm's report of its own internal results is
(A), one firm's account, unless it describes how it counted; a counted figure with a stated method
is (M, vendor) when the firm sells the tool and (M, own count) otherwise. No figure on this page is
audited.

**Citations.** Every URL in this document was read on 2026-10-23, unless the text gives another
date. Each claim names its source by a link. This document has no ledger records in
[`_evidence/`](../_evidence/); its sources have not had the independent fact-check that the
[conventions](../CONVENTIONS.md) describe. A second reader re-read the key findings OP1 to OP7, both quotations
and about 75 body claims, the table in §1 included, at their sources on 2026-10-23: 4 key findings
and 13 body claims were corrected, and both quotations were exact.

## Key findings

**OP1. One team claims a dark factory, and it has published no results.** StrongDM's AI team, three
people in October 2025, says it writes no code and reviews no code by hand, and it still published
updates on which models run its factory through 2026-09-28. It has published no output, quality or cost figures.
(A) — §2.

**OP2. One lab made human review optional for one product.** OpenAI's harness team reports about
1,500 merged pull requests and about one million lines in five months with no hand-written code;
agents reviewed each other and often merged their own pull requests. OpenAI says that the agent's
end-to-end autonomy depends on that repository's tooling. (A) — §3.

**OP3. Most published operators run high agent authorship with human review or human merge
approval.** Stripe (over 1,300 agent-produced pull requests merged a week, each reviewed by people),
Coinbase (about 100% AI-generated code, all reviewed by people), Google (75% of new code AI-generated
and approved by engineers), Microsoft's dotnet/runtime, Shopify and WorkOS keep a person at review or
merge; Ramp's and Uber's posts point the same way without stating a rule for every pull request. Weak
for any comparison: the firms count "authored", "attributed",
"created", "coauthored" and "generated" differently. (A, M) — §5.

**OP4. Merge with no person in the loop is published mainly for routine maintenance.** Spotify has
merged more than 2.5 million automated maintenance pull requests, most of them merged automatically,
but that count includes scripted changes and the share made by its agent is not stated. (A) — §6.

**OP5. The largest fully autonomous builds are demonstrations, not products.** Anthropic's 16
parallel agents wrote a 100,000-line C compiler for just under $20,000; Cursor's agents wrote over a
million lines of a web browser in about a week. Anthropic's author lists what the compiler cannot do;
Cursor says the browser was not for external use and was expected to have imperfections. (A) — §4.

**OP6. The firms that report problems report the same ones: review capacity, drift and failures
that the checks passed.** HumanLayer went fully lights-off in July 2025 and put human review back
after repeated incidents; OpenAI's team spent a fifth of each week cleaning up agent output before it
automated the clean-up; at Spotify an automated dependency upgrade passed its checks and failed in
production. Several firms name human review as the new bottleneck. (A) — §7.

**OP7. The verification the operators describe goes beyond a test suite.** It includes scenarios kept
outside the codebase, clones of third-party services, an app booted per worktree and driven by the
agent, selected CI with a cap on rounds, screenshots compared with the design, and a revert rate or
cost per merged pull request tracked per agent. (A) — §8.

## 1. The operators at a glance

| Organization | What runs | Scale the firm reports (date) | Human role | Source |
| --- | --- | --- | --- | --- |
| StrongDM | Software Factory; Attractor | No output figures; model roster updated to 2026-09-28 | No code writing, no code review | §2 |
| OpenAI (one team) | An internal product built with Codex; Symphony | About 1,500 merged pull requests and about 1M lines in five months, 3 then 7 engineers (2026-02) | Prompts, priorities, acceptance criteria; review optional | §3 |
| Anthropic | Company codebase; a C compiler demonstration | Over 80% of merged code authored by Claude (May 2026); the compiler at about 100,000 lines | An automated Claude reviewer reads changes before merge; engineers direct and review | §4, §5 |
| Cursor | Long-running agent builds; cloud agents | Over 60% of internally merged pull requests created by cloud agents (2026-09-02) | Review rule not stated | §4, §5 |
| Stripe | Minions | Over 1,300 merged pull requests a week (2026-02-19) | The requester and a second engineer review each one | §5 |
| Spotify | Fleet Management; Honk | Over 2.5M automated maintenance pull requests merged, most automatically (2026-06-03) | None for most fleet changes; agent share not stated | §6 |
| Shopify | River | One in eight merged pull requests coauthored by River; 3,536 in 30 days (2026-05-28) | Owners review and merge | §5 |
| Ramp | Inspect | About 30% of pull requests merged to its frontend and backend repositories (2026-01-12) | Not stated; pull requests are opened so that no one can approve their own change | §5 |
| Uber | "Software Factory" programme; AutoClean | Over 70% of pull requests attributed to agents (2026-08-27) | Human review and escalation | §5 |
| Coinbase | Background agents; Mux | About 100% of merged code AI-generated (2026-07-13) | People review all code | §5 |
| Google | Company codebase | 75% of new code AI-generated and approved by engineers (2026-04-22) | Engineer approval | §5 |
| Microsoft (dotnet/runtime) | Copilot cloud agent | 535 merged of 878 agent pull requests in ten months (2026-03-23) | A maintainer requests each; merged ones are reviewed | §5 |
| WorkOS | Horizon | No figures | People review issues and approve every merge | §5 |
| Warp | A factory on its open-source repository | No figures | Not stated for its own repository; the product's default is a person approving the spec and merging ([platforms.md](platforms.md)) | §5 |
| HumanLayer | A lights-off factory, July to November 2025 | No figures | None, then human review again | §7 |

## 2. The one claimed dark factory: StrongDM

- StrongDM's AI team was founded on 2025-07-14 by its CTO, Justin McCarthy, with Jay Taylor and Navan
  Chauhan. Its rules are that humans do not write code and do not review code, and its cost guide is at least
  $1,000 of tokens per human engineer per day ([StrongDM](https://factory.strongdm.ai/)) (A).
- Its main check is a set of "scenarios", end-to-end user stories often kept outside the codebase and
  judged by a model, scored as "satisfaction", the share of observed runs that likely satisfy the
  user. The scenarios run against a "Digital Twin Universe" of behavioural clones of Okta, Jira, Slack,
  Google Docs, Google Drive and Google Sheets, at thousands of scenarios an hour. The stated reason is
  that agents gamed narrow tests, for example by returning true
  ([StrongDM](https://factory.strongdm.ai/)) (A).
- StrongDM lists Attractor, a non-interactive coding agent built as a graph of phases, as a product of
  the factory ([StrongDM products](https://factory.strongdm.ai/products)) (L); the public repository
  holds natural-language specifications only, not code ([Attractor](https://github.com/strongdm/attractor))
  (L). [platforms.md](platforms.md) has
  more.
- Its "Weather Report" page lists which models play which roles in the factory, with entries from
  2026-02-06 to 2026-09-28 ([StrongDM weather report](https://factory.strongdm.ai/weather-report))
  (A). Inference: the factory still ran in late September 2026. StrongDM has published no output,
  quality or cost results.
- Simon Willison visited the team in October 2025, when it had three people and about three months
  of work, and saw demos of the harness, the twins of about six services and simulated test agents.
  He questions the economics of the token target and names proof of correctness, when agents write
  both the code and the tests, as the central open question
  ([Willison](https://simonwillison.net/2026/Feb/7/software-factory/)) (A).

## 3. Review made optional: OpenAI's harness team

- An OpenAI team built an internal beta product with no manually written code, from a first commit in
  late August 2025 over about five months: about one million lines (application, tests, CI, docs,
  tooling) and about 1,500 merged pull requests, by three engineers and later seven, or 3.5 pull
  requests per engineer per day. OpenAI estimates that this took about a tenth of the time of writing
  it by hand ([OpenAI](https://openai.com/index/harness-engineering/)) (A).
- People prompted, set priorities, wrote acceptance criteria and checked outcomes. Human review of
  pull requests was optional; most review was agent to agent, agents often squashed and merged their
  own pull requests, and merge gates were few (a flaky test was often re-run instead of blocking).
  OpenAI says this depends heavily on that repository's structure and tooling
  ([OpenAI](https://openai.com/index/harness-engineering/)) (A).
- The checks: the app boots per git worktree; the agent drives the UI through the Chrome DevTools
  Protocol; each worktree gets its own short-lived logs and metrics; custom linters and structural
  tests enforce a fixed layering; a "doc-gardening" agent fixes stale docs. Human QA capacity became
  the bottleneck, agents copied poor patterns, and the team spent every Friday on clean-up until it
  encoded its rules and ran recurring clean-up agents. OpenAI says long-term architectural coherence
  is unknown ([OpenAI](https://openai.com/index/harness-engineering/)) (A).
- OpenAI's public Symphony repository (created 2026-02-26) watches a Linear board, starts a Codex
  agent per task, attaches proof of work (CI status, review feedback, walkthrough videos), and lands
  the pull request when a person accepts the work ([Symphony](https://github.com/openai/symphony))
  (L). [platforms.md](platforms.md) has its limits.

## 4. Long autonomous builds as demonstrations

- **Anthropic's C compiler.** Nicholas Carlini ran 16 parallel Claude Opus 4.6 agents without active
  human intervention to write a C compiler in Rust: nearly 2,000 Claude Code sessions over about two
  weeks, 2 billion input and 140 million output tokens, just under $20,000, about 100,000 lines. It
  builds Linux 6.9 on x86, ARM and RISC-V. The person built the test harness, CI, task locks in git
  files and used GCC as a known-good oracle. The author says it is not a drop-in replacement, its
  output is less efficient than GCC with optimizations off, it still uses GCC for 16-bit boot code
  and for assembling and linking, and new features often broke old ones
  ([Anthropic](https://www.anthropic.com/research/building-c-compiler)) (A). He warns that for
  autonomous systems "it is easy to see tests pass and assume the job is done, when this is rarely the
  case" (A).
- **Cursor's browser and other runs.** Hundreds of concurrent agents (planners that create tasks,
  workers that only do tasks, a judge each cycle) ran for close to a week and wrote over a million
  lines across 1,000 files of a web browser; other runs, still running when the post was written,
  were building a Java language server, a Windows 7 emulator and a spreadsheet, and one migrated part
  of Cursor's own code, which passed CI but still needed careful review. Shared locks cut 20 agents to the throughput of two or three, and agents drifted and
  needed fresh starts ([Cursor](https://cursor.com/blog/scaling-agents)) (A). A follow-up reports a
  peak of about 1,000 commits an hour over 10 million tool calls in one week with no human
  intervention and a deliberately accepted small error rate, and proposes a final "green" branch where
  an agent fixes up before release; Cursor says the browser was not for external use
  ([Cursor](https://cursor.com/blog/self-driving-codebases)) (A).

## 5. High agent authorship with a person at review or merge

- **Anthropic.** As of May 2026, more than 80% of the code merged into Anthropic's codebase was
  authored by Claude, counted by a pipeline that attributes lines merged to production; Anthropic says
  this is more conservative than its leadership's public figure of 90% or more, which includes scripts
  and experimental code. An automated Claude reviewer reads proposed changes before they merge. A
  retrospective found that a Claude review of every change would have caught about a third of the bugs
  behind past claude.ai incidents. In the second quarter of 2026 the typical engineer merged 8 times as
  many lines a day as in 2024, which Anthropic says almost certainly overstates the gain
  ([Anthropic Institute](https://www.anthropic.com/institute/recursive-self-improvement)) (M, own
  count; the page shows an update note dated 2026-09-18, and its first publication date, 2026-06-04,
  is from secondary coverage, `UNVERIFIED`). Anthropic expects Claude's code to be better than human
  code within the year, and says that once quality reaches parity, which it puts at roughly today,
  people will stop writing code and only review it (F; falsifier: no Anthropic report of
  better-than-human code quality by mid-2027; horizon about mid-2027). Boris Cherny, who created
  Claude Code, posted that in the 30 days before 2025-12-27 he landed 259 pull requests, every line
  written by Claude Code ([Cherny](https://x.com/bcherny/status/2004887829252317325)) (A).
- **Stripe.** Minions are unattended agents that take a task from a Slack message to a pull request
  that passes CI. Over 1,000 merged pull requests a week were fully agent-produced (2026-02-09), rising
  to over 1,300 (2026-02-19); each is reviewed by the requesting engineer and then a second engineer.
  Lints run on each push in under five seconds; CI runs selected tests from over three million and
  returns failures to the agent, with at most two CI rounds
  ([Stripe](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents),
  [Stripe part 2](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2))
  (A).
- **Shopify.** River, an agent that works in public Slack channels, coauthored one in eight merged
  pull requests about two months after launch; in one 30-day window it ran 59,918 sessions and
  coauthored 3,536 merged pull requests, counted from a table River writes every session
  ([Shopify](https://shopify.engineering/under-the-river)) (M, own count). For vulnerability fixes it
  re-checks each finding at the repository head, re-runs CI and hands owners a short decision; owners
  review and merge. The open dependency-vulnerability backlog fell about 70% in the first 11 days
  ([Shopify](https://shopify.engineering/river-vulnerability-remediation)) (A).
- **Ramp.** Inspect runs each session in a sandboxed VM with Ramp's full stack and checks its work
  with tests, telemetry, feature flags and, for front-end work, screenshots. About 30% of pull requests
  merged to the front-end and back-end repositories were written by Inspect. It opens pull requests
  with the requesting user's GitHub token so that no one can approve their own unreviewed change
  ([Ramp](https://builders.ramp.com/post/why-we-built-our-background-agent)) (A).
- **Uber.** Uber calls its programme a Software Factory. More than 70% of pull requests are
  attributed to local or cloud agents; total AI spend has been roughly flat since April 2026 while use
  grew; each managed agent is tracked by an outcome cost (for example cost per merged pull request)
  and a quality signal (for example revert rate) that fit its job, with human reviews and escalations ([Uber](https://www.uber.com/us/en/blog/efficient-software-factory/)) (A).
  The conference page of Uber's talk, which carries its transcript, describes an agent that stops at
  a draft pull request without sending it to CI, so that inner-loop checks (a screenshot compared with
  the Figma design, the backend run in staging) run first, then self-healing CI and two AI review
  stages, and names reviewer attention as a limit separate from compute
  ([AI Engineer](https://ai.engineer/talks/17-YSUHo6Lk-agentic-sdlc-at-uber-building-blocks-ubers))
  (A). AutoClean has removed more than 16,000 stale feature
  flags and over a million lines over several years, with a person in the owning team making the final decision
  ([Uber](https://www.uber.com/us/en/blog/ai-code-cleanup/)) (A).
- **Coinbase.** AI-generated code rose from 5.7% of merged code in the first quarter of 2025 to
  roughly 100%, and people still review all of it; the counting method is not described
  ([Coinbase](https://www.coinbase.com/blog/interviewing-engineers-in-the-ai-era-lessons-from-a-year-of-rebuilding))
  (A). Its multi-agent tool Mux gives each agent its own worktree; in one month its users merged 39.6
  pull requests per engineer against a baseline of 11.4, and Coinbase warns that its users were likely
  already high-output ([Coinbase](https://www.coinbase.com/blog/coding-had-a-concurrency-problem-how-mux-helped-solve-it))
  (A).
- **Google.** Google's CEO said on 2026-04-22 that 75% of all new code at Google is AI-generated and
  approved by engineers, up from 50% in autumn 2025
  ([Google](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/))
  (A).
- **Microsoft, dotnet/runtime.** From 2025-05-19 to 2026-03-22 the Copilot cloud agent opened 878 pull
  requests and 535 merged, 22.2% of Microsoft-originated pull requests by count. Its success rate was
  67.9% against 87.1% for Microsoft's human pull requests; 3 of 535 merged agent pull requests were
  reverted (0.6%) against 33 of 4,251 others (0.8%), a difference the author calls not meaningful. A
  maintainer requested every agent pull request
  ([Microsoft](https://devblogs.microsoft.com/dotnet/ten-months-with-cca-in-dotnet-runtime/)) (M,
  vendor; counted from public GitHub data).
- **WorkOS.** Horizon, its "autonomous code factory", has a person write requirements in Linear, a
  planning agent split them into issues that a person reviews, and implementing agents run in
  sandboxes; every merge needs explicit human approval, which WorkOS says makes people the bottleneck
  ([WorkOS](https://workos.com/blog/project-horizon)) (A).
- **Warp and Notion.** Warp's CEO says Warp runs a factory on its own open-source repository with its
  factory platform, and forecasts that within about a year every significant software project will
  have a factory-like engine ([Latent Space](https://www.latent.space/p/software-factories)) (A; F,
  falsifier: by mid-2027 most major projects still run without continuous agent-driven change). Warp
  sells that platform. Notion's cofounder Simon Last said Notion is trying many approaches, aiming for
  as little human intervention as possible while keeping key invariants, with a human-readable spec
  layer and strong self-verification; he gave no figures ([Latent Space](https://www.latent.space/p/notion))
  (A).

## 6. Merge with no person: Spotify's fleet changes

Spotify's Fleet Management has merged more than 2.5 million automated maintenance pull requests, "the
vast majority auto-merged with no human in the loop"; the count includes deterministic scripted
changes, not only those of Honk, its background coding agent, which runs Claude in Kubernetes pods and
checks changes with CI builds on several operating systems. Spotify reports more than 99% weekly use
of AI tools and a 76% rise in pull request frequency, and so 76% more pull requests to review
([Spotify](https://engineering.atspotify.com/2026/6/code-with-claude-coding-is-no-longer-the-constraint))
(A). The share of automatic merges made by the agent is not stated.

## 7. What went wrong

- **HumanLayer.** An essay signed "Dex" in HumanLayer's public repository (Dex Horthy gave the talk of
  the same name, [README.md](README.md) §1) says that the company went fully lights-off in July 2025:
  people read only specs and tickets, and background agents did small and medium work. Agents then hit
  problems they could not solve in code no one had read for months, with site downtime; after about
  the third case, in November 2025, the team rewrote from scratch, and it has since put human code
  review back. The essay
  argues that an agent-built codebase starts to struggle after three to six months. HumanLayer sells
  tools for people and agents working together
  ([HumanLayer](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md))
  (A; the only first-hand account found of a lights-off factory that was stopped).
- **OpenAI.** The harness team spent every Friday, 20% of the week, cleaning up low-quality agent
  output before it automated the clean-up ([OpenAI](https://openai.com/index/harness-engineering/))
  (A).
- **Spotify.** Merged changes more than doubled year over year by August 2026 (about 8,100 to 17,000
  a month by its own classification). Monthly incident reviews found AI-written code was not a
  material direct cause, but change volume grew faster than some verification controls, and an
  automated dependency upgrade passed its checks and still failed in production. Spotify says it is
  adding safeguards and rollback capacity and moving automated changes into the owning teams' working
  hours
  ([Spotify](https://engineering.atspotify.com/2026/9/ai-changed-how-spotify-builds-what-we-learned-and-fixed-about-quality-at-higher-velocity))
  (A).
- **Amazon.** Amazon disputes Financial Times reports that AI-written code caused several Amazon.com
  outages: it says one recent incident involved an AI tool, through wrong advice drawn from an
  outdated wiki, none involved AI-written code, and it added no new approval rule
  ([Amazon](https://www.aboutamazon.com/news/company-news/amazon-outage-ai-financial-times-correction))
  (A). The Financial Times reports were not read (`UNVERIFIED`).
- **Review as the bottleneck.** OpenAI (human QA capacity), Spotify (76% more pull requests to
  review), WorkOS (every merge needs a person) and Uber (reviewer attention separate from compute) each
  name it (sources above) (A). [practices/project-lifecycle.md](../practices/project-lifecycle.md)
  LC5 holds the measured studies on the same constraint.

## 8. How operators verify

Inference: a grouping of the checks described in §2 to §7; no operator measured one check against
another.

| Check | Who describes it |
| --- | --- |
| Scenarios kept outside the codebase, judged by a model | StrongDM |
| Clones of third-party services to test against | StrongDM |
| The app booted per worktree and driven by the agent; logs and metrics per worktree | OpenAI |
| Custom linters and structural tests for the architecture | OpenAI |
| A known-good oracle to compare against (GCC) | Anthropic's compiler |
| Selected tests from a very large suite, with a cap of two CI rounds | Stripe |
| Screenshots compared with the design; the backend run in staging | Uber (talk page) |
| Screenshots and live previews for front-end work; telemetry and feature flags | Ramp |
| An automated reviewer before merge | Anthropic, Uber |
| An outcome cost and a quality signal per agent (for example cost per merged pull request, revert rate) | Uber |
| Re-checking each finding at the repository head before a fix | Shopify |

## 9. Limits and open questions

- No figure here is audited, and the firms count differently ("authored by", "attributed to",
  "created by", "coauthored", "AI-generated and approved"). Only Anthropic, Shopify and Microsoft's
  dotnet/runtime team describe how they counted. The numbers do not compare across firms.
- No operator has published a maintainability result over 12 months or more for an agent-written
  codebase; OpenAI says it does not know. Cost per merged pull request in money is not published by
  any operator.
- Cursor's posts do not say who reviews or merges its internal cloud-agent pull requests.
- Read only in secondary sources, so left out of the findings (`UNVERIFIED`): Ramp's "three of every
  four pull requests" in a Linear customer story; a Spotify co-CEO remark on the 2026-02-10 earnings
  call that top developers had written no code since December; a Coinbase interview figure of 95% to
  100% of code written by or with LLMs; Financial Times reports on Amazon; a Pragmatic Engineer figure
  of 11% of Uber pull requests opened by agents, which may count differently from Uber's 70%.
- Meta, Microsoft company-wide, Amazon's internal share and Airbnb in 2026 were not found or not
  checked.

## Sources

All read on 2026-10-23.

**StrongDM.** Software Factories And The Agentic Moment, 2026-02-06 <https://factory.strongdm.ai/>;
Products <https://factory.strongdm.ai/products>; Weather Report
<https://factory.strongdm.ai/weather-report>; Simon Willison, 2026-02-07
<https://simonwillison.net/2026/Feb/7/software-factory/>.

**OpenAI.** Harness engineering, February 2026 <https://openai.com/index/harness-engineering/> (read
in a browser, as the page refused direct fetches); Symphony repository
<https://github.com/openai/symphony>.

**Anthropic.** Building a C compiler with a team of parallel Claudes, 2026-02-05
<https://www.anthropic.com/research/building-c-compiler>; When AI builds itself
<https://www.anthropic.com/institute/recursive-self-improvement>; Boris Cherny, 2025-12-27
<https://x.com/bcherny/status/2004887829252317325>.

**Cursor.** Scaling long-running autonomous coding, 2026-01-14 <https://cursor.com/blog/scaling-agents>;
Towards self-driving codebases, 2026-02-05 <https://cursor.com/blog/self-driving-codebases>; Run cloud
agents on machines you manage, 2026-09-02 <https://cursor.com/blog/self-hosted-machines>.

**Others.** Stripe, 2026-02-09
<https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents> and 2026-02-19
<https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2>; Spotify,
2026-06-03 <https://engineering.atspotify.com/2026/6/code-with-claude-coding-is-no-longer-the-constraint>
and 2026-09-16
<https://engineering.atspotify.com/2026/9/ai-changed-how-spotify-builds-what-we-learned-and-fixed-about-quality-at-higher-velocity>;
Ramp, 2026-01-12 <https://builders.ramp.com/post/why-we-built-our-background-agent>; Shopify,
2026-05-28 <https://shopify.engineering/under-the-river> and 2026-09-02
<https://shopify.engineering/river-vulnerability-remediation>; Uber, 2026-08-27
<https://www.uber.com/us/en/blog/efficient-software-factory/>, the AI Engineer talk page
<https://ai.engineer/talks/17-YSUHo6Lk-agentic-sdlc-at-uber-building-blocks-ubers> and 2026-10-20
<https://www.uber.com/us/en/blog/ai-code-cleanup/>; Coinbase, 2026-07-13
<https://www.coinbase.com/blog/interviewing-engineers-in-the-ai-era-lessons-from-a-year-of-rebuilding>
and 2026-05-11 <https://www.coinbase.com/blog/coding-had-a-concurrency-problem-how-mux-helped-solve-it>;
Google, 2026-04-22
<https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/>;
Microsoft, 2026-03-23 <https://devblogs.microsoft.com/dotnet/ten-months-with-cca-in-dotnet-runtime/>;
Amazon, 2026-03-11
<https://www.aboutamazon.com/news/company-news/amazon-outage-ai-financial-times-correction>; Notion on
Latent Space, 2026-04-15 <https://www.latent.space/p/notion>; HumanLayer, Why Software Factories Fail,
2026-07
<https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md>;
WorkOS, 2026-05-06 <https://workos.com/blog/project-horizon>; Warp's CEO on Latent Space, 2026-07-01
<https://www.latent.space/p/software-factories>.
