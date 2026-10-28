---
last_checked: 2026-10-23
volatility: VOLATILE (most features are in preview or beta, limits and prices change at each release, and products were renamed or sold in October 2026)
sources:
  - https://factory.com/news/missions (read 2026-10-23)
  - https://factory.com/news/what-it-takes-for-coding-agents-to-complete-large-software-tasks (read 2026-10-23)
  - https://factory.com/news/automations (read 2026-10-23)
  - https://factory.com/news/droids-now-have-a-fleet-of-sandboxes (read 2026-10-23)
  - https://factory.com/news/opencompute (read 2026-10-23)
  - https://factory.com/pricing (read 2026-10-23)
  - https://docs.devin.ai/work-with-devin/advanced-capabilities (read 2026-10-23)
  - https://docs.devin.ai/release-notes/2026 (read 2026-10-23)
  - https://devin.ai/pricing (read 2026-10-23)
  - https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations (read 2026-10-23)
  - https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent (read 2026-10-23)
  - https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations (read 2026-10-23)
  - https://github.blog/changelog/2026-08-03-trigger-copilot-automations-with-comments/ (read 2026-10-23)
  - https://github.blog/changelog/2026-09-01-copilot-code-review-can-now-approve-pull-requests/ (read 2026-10-23)
  - https://docs.github.com/en/copilot/concepts/agents/code-review (read 2026-10-23)
  - https://github.github.com/gh-aw/ (read 2026-10-23)
  - https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview (read 2026-10-23)
  - https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents (read 2026-10-23)
  - https://github.com/openai/symphony (read 2026-10-23)
  - https://github.com/openai/symphony/blob/main/SPEC.md (read 2026-10-23)
  - https://learn.chatgpt.com/docs/changelog (read 2026-10-23)
  - https://learn.chatgpt.com/docs/third-party/linear (read 2026-10-23)
  - https://code.claude.com/docs/en/routines (read 2026-10-23)
  - https://code.claude.com/docs/en/claude-projects (read 2026-10-23)
  - https://code.claude.com/docs/en/workflows (read 2026-10-23)
  - https://code.claude.com/docs/en/agents (read 2026-10-23)
  - https://code.claude.com/docs/en/agent-teams (read 2026-10-23)
  - https://github.com/anthropics/claude-code-action/blob/main/docs/security.md (read 2026-10-23)
  - https://github.com/anthropics/claude-code-action/blob/main/docs/faq.md (read 2026-10-23)
  - https://code.claude.com/docs/en/code-review (read 2026-10-23)
  - https://cursor.com/docs/cloud-agent/automations (read 2026-10-23)
  - https://cursor.com/docs/approval-agents (read 2026-10-23)
  - https://jules.google/docs/changelog/ (read 2026-10-23)
  - https://jules.google/docs/usage-limits/ (read 2026-10-23)
  - https://docs.warp.dev/factories/ (read 2026-10-23)
  - https://docs.warp.dev/factories/how-factories-work/ (read 2026-10-23)
  - https://docs.warp.dev/platform/harnesses/ (read 2026-10-23)
  - https://docs.warp.dev/platform/transitioning-from-oz/ (read 2026-10-23)
  - https://factory.com/ (read 2026-10-23)
  - https://www.harness.io/blog/harness-acquires-augment-code-cosmos (read 2026-10-23)
  - https://www.augmentcode.com/blog/augment-code-next-chapter (read 2026-10-23)
  - https://docs.openhands.dev/openhands/usage/cloud/github-installation (read 2026-10-23)
  - https://docs.openhands.dev/openhands/usage/automations/overview (read 2026-10-23)
  - https://github.com/strongdm/attractor (read 2026-10-23)
  - https://factory.strongdm.ai/products/attractor (read 2026-10-23)
  - https://github.com/gastownhall/gastown (read 2026-10-23)
  - https://github.com/gastownhall/gascity (read 2026-10-23)
  - https://yegge.ai/essays/the-shape-of-things-to-come/ (read 2026-10-23)
  - https://ghuntley.com/ralph/ (read 2026-10-23)
  - https://github.com/ghuntley/overalls (read 2026-10-23)
  - https://ampcode.com/news/agents-in-orbs (read 2026-10-23)
  - https://ampcode.com/news/assign-it-to-amp (read 2026-10-23)
---

# Software factory platforms: what queues, runs, checks and merges the work

Re-check before any load-bearing use (14 days): most features here are previews or betas. Re-check
at once when GitHub documents whether a Copilot approval can count on a pull request that Copilot's
own agent wrote; when any product documents merging an agent's pull request with no human approval
by default; when Symphony or the Codex app server leaves preview; or when Jules publishes a status
after March 2026.

Which products and open orchestrators provide the factory layer: the parts that take work in from a
trigger or a tracker, run many agents, check their output, and merge or deploy it; where each one
needs a person; which guardrails each one enforces and where; and its limits and status. How a cloud
session runs its setup, what network it has and how work leaves it is in
[harnesses/cloud-sessions.md](../harnesses/cloud-sessions.md); this page does not repeat it. The
firms that run factories on these products are in [operators.md](operators.md).

**Evidence classes.** As in [README.md](README.md). Product documentation is (L). A vendor's
measure of its own product is (M, vendor).

**Citations.** Every URL in this document was read on 2026-10-23, unless the text gives another
date. Each claim names its source by a link. This document has no ledger records in
[`_evidence/`](../_evidence/); its sources have not had the independent fact-check that the
[conventions](../CONVENTIONS.md) describe. A second reader re-read the key findings PL1 to PL7, every quotation
and the body's numbers, dates, limits and prices at their sources on 2026-10-23, together with those
of [README.md](README.md): 3 key findings and 11 body claims in this document were corrected, and
two exact quotations that were cited to the wrong page now cite the right one.

## Key findings

**PL1. Most products stop at a pull request that a person merges.** Factory, Devin, Cursor,
OpenHands, Jules and Copilot's cloud agent document opening a pull request, Codex hands a person a
link to create one, and Amp's posts do not say; none of the docs
read documents the platform merging its own agent's work with no human approval by default. Only
GitHub's cloud agent, Warp Factories and the Claude Code GitHub Action state a rule against merging.
(L) — §1.

**PL2. Where the stop is enforced differs, and that decides how strong it is.** GitHub enforces it
in the platform: Copilot's cloud agent cannot approve or merge its own pull request, and the person
who asked for it cannot approve it. Warp Factories leaves it to repository permissions and branch
protection. The Claude Code GitHub Action enforces it in Claude's system prompt. In Claude Code
Projects a "Merge it" button sends the instruction to the agent. Inference: only a platform rule or
branch protection holds if the agent misreads its instructions;
[practices/project-lifecycle.md](../practices/project-lifecycle.md) LC7 has the same finding for
irreversible acts. (L) — §1, §2.

**PL3. Paths for an AI to approve a pull request now exist.** Since 2026-09-01, in public preview and
off by default, a Copilot code review approval can satisfy a required review on GitHub; Cursor's PR
Routing & Approval can approve low-risk pull requests below a risk threshold (its launch date was not
found). No source
read says whether a Copilot approval counts on a pull request that Copilot's cloud agent wrote. (L)
— §2.

**PL4. Intake from triggers is now standard.** Schedules, issue and pull request events, comments,
tracker assignment (Linear, Jira), Slack and incident tools (PagerDuty, Sentry) start agent sessions
in Copilot automations, Cursor Automations, Factory Automations, Devin, Claude Code's scheduled tasks,
Jules, OpenHands and Amp. (L) — §3.

**PL5. The open orchestrators are specifications or previews.** OpenAI's Symphony is a preview for
trusted environments that relies on a Codex interface OpenAI labels experimental; StrongDM's Attractor
repository holds specifications only; Gas Town's author stopped using it in August 2026, although its
repository is still active. (L, A) — §4.

**PL6. Three products are now sold under the factory name.** Factory ("Build your software
factory"), Warp Factories, and Harness's Cosmos Software Factory Agent, which Harness bought from
Augment Code on 2026-10-08. (L) — §5.

**PL7. No product read documents deploying to production as one of its own steps.** Harness says
its delivery agents take Cosmos's work toward production; that part was not read. (L) — §6.

## 1. Who merges, and what enforces it (VOLATILE)

| Product | Intake | Orchestration | Who merges by default | What enforces it | Status |
| --- | --- | --- | --- | --- | --- |
| GitHub Copilot cloud agent | Issues, automations, comments, Linear | One agent, one branch, one pull request per task | A person with write access; the requester cannot approve | The platform | Generally available; automations and some integrations newer |
| GitHub Agentic Workflows | Schedules and repository events, in Actions | One agent per workflow, read-only by default | A person; the project site says to review changes before merging | Writes only through declared outputs, applied by a separate job | Public preview since 2026-06-11 |
| Warp Factories | Slack, GitHub, Linear, Jira | A foreman agent routes work through triage, spec, implement and review agents | A person | Repository permissions and branch protection | Launch date and stage not found |
| Factory (Missions, Automations) | A goal; schedules, Slack, GitHub, webhooks; Linear and Jira tickets | An orchestrator splits a mission into milestones and features, a fresh worker per feature | Not described; pull requests opened for review | Not described | Automations generally available since 2026-09-30 |
| Devin | Linear, Slack, schedules, PagerDuty | A coordinator session starts child sessions | A person; users who may bypass repository rules can merge a blocked pull request from Devin Review after confirming | Repository rules | Generally available |
| Cursor Automations | Schedules, webhooks, GitHub, GitLab, Bitbucket, Linear, Slack, Sentry, PagerDuty | Cloud agents | Not described; an approval agent can approve low-risk pull requests | The approval criteria the team sets | Generally available |
| OpenAI Codex (Linear) | Assignment or mention in Linear | One cloud task | A person creates the pull request from Codex's link | Codex does not open the pull request | Generally available |
| OpenAI Symphony | A Linear board | A service that starts one Codex run per ticket, 10 at once by default | Agents land the pull request after a person accepts the work | The tracker state the team defines | Engineering preview |
| Claude Code scheduled tasks | Schedules, API calls, GitHub events | One cloud session per run | Not described; runs push to `claude/` branches | Branch protection | Research preview |
| Claude Code Projects | A long conversation | Parallel cloud threads, each with its own pull request | The person, by an instruction to the thread | The instruction only; branch protection is the enforceable gate (inference) | Public beta |
| Claude Code GitHub Action | `@claude` mentions, workflow events | One run | A person; the action pushes a branch and links the page to open a pull request | Claude's system prompt | Generally available |
| OpenHands Cloud | An issue label or a mention | One conversation | Not described | Not described | Stage not stated |
| Gas Town | Work split by a "Mayor" agent | Workers in git worktrees, state in the Beads tracker | A merge queue that merges green batches | The queue's verification gates | Repository active; its author stopped using it (§4) |

Sources: [GitHub risks](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations),
[GitHub agentic workflows](https://github.github.com/gh-aw/), [Warp](https://docs.warp.dev/factories/how-factories-work/),
[Factory](https://factory.com/news/automations), [Devin release notes](https://docs.devin.ai/release-notes/2026),
[Cursor](https://cursor.com/docs/cloud-agent/automations), [Codex in Linear](https://learn.chatgpt.com/docs/third-party/linear),
[Symphony](https://github.com/openai/symphony), [Claude Code scheduled tasks](https://code.claude.com/docs/en/routines),
[Claude Code Projects](https://code.claude.com/docs/en/claude-projects),
[claude-code-action FAQ](https://github.com/anthropics/claude-code-action/blob/main/docs/faq.md),
[OpenHands](https://docs.openhands.dev/openhands/usage/cloud/github-installation),
[Gas Town](https://github.com/gastownhall/gastown) (all L).

**Details of the guardrails.**

- **GitHub.** Only users with write access can start Copilot's cloud agent; it pushes only to one
  branch under the existing branch protection; it cannot mark its pull request ready, approve it or
  merge it; the person who asked for the pull request cannot approve it; where approvals are required,
  a pull request attributed to the agent needs one extra approval; Actions workflows do not run on its
  changes until a user with write access approves them, unless an admin allows automatic runs; its
  internet access goes through a firewall; and CodeQL, secret scanning and dependency checks run by
  default ([GitHub risks](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations))
  (L). Third-party agents on GitHub (Claude and Codex, both in public preview) have
  the same protections and limits ([GitHub third-party agents](https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents))
  (L).
- **GitHub Agentic Workflows.** A workflow is a Markdown file that `gh aw compile` turns into
  hardened Actions YAML. The agent runs read-only in a sandbox behind a firewall; writes happen only
  through declared "safe outputs", applied by a separate job with its own permissions; a
  threat-detection job scans the proposed outputs; and cost caps and a dry-run mode exist
  ([GitHub agentic workflows](https://github.github.com/gh-aw/),
  [changelog](https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview))
  (L).
- **Warp Factories.** By default a person approves the spec, answers open questions and merges. Spec
  approval is an instruction to the foreman that a team can edit; the review agent's verdict is
  advisory. The docs state: "The factory never merges on your behalf. Repository permissions and
  branch protection control approval and merge access."
  ([Warp](https://docs.warp.dev/factories/how-factories-work/), [Warp overview](https://docs.warp.dev/factories/))
  (L).
- **Claude Code GitHub Action.** It checks that the triggering user has write access (except for
  schedule and dispatch events) and restores Claude's configuration files from the base branch. Its FAQ
  says that it does not merge, rebase or force-push, and that this is enforced in Claude's system
  prompt ([claude-code-action security](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md),
  [FAQ](https://github.com/anthropics/claude-code-action/blob/main/docs/faq.md)) (L). Anthropic's
  managed Code Review posts findings and a check run; "A review never approves or blocks the pull
  request, so the decision to merge stays with your team"
  ([Claude Code review](https://code.claude.com/docs/en/code-review)) (L).
- **Claude Code Projects and scheduled tasks.** In Projects, buttons such as "Merge it" send that
  instruction to the thread as a message from the user, and cloud threads do not apply a repository's
  `.claude/settings.json` permission rules; they rely on auto mode and approvals inside the thread
  ([Claude Code Projects](https://code.claude.com/docs/en/claude-projects)) (L). A scheduled task acts
  as its owner's GitHub identity and starts in auto mode, and its docs say that the fired prompt is not
  live user input and cannot count as approval for actions during the run
  ([Claude Code scheduled tasks](https://code.claude.com/docs/en/routines)) (L).
  [practices/agent-authorization.md](../practices/agent-authorization.md) A9 holds the related rule
  that an agent working under its person's account cannot give that person a second approval.

## 2. AI approval of a pull request (VOLATILE) [as-of 2026-10-23]

- Since 2026-09-01, in public preview, Copilot code review can submit an approving review that
  satisfies a repository's required-approval rule, when approvals are turned on at repository,
  organization and enterprise level. It is off by default; admins can limit it to file paths; new
  commits dismiss the approval ([changelog](https://github.blog/changelog/2026-09-01-copilot-code-review-can-now-approve-pull-requests/),
  [GitHub code review](https://docs.github.com/en/copilot/concepts/agents/code-review)) (L). No
  source read says whether it can approve a pull request that Copilot's cloud agent wrote, or how it
  meets the rules that the requester cannot approve and that agent pull requests need one extra
  approval. Inference: this decides whether a factory built only from GitHub features can merge with
  no person. [practices/review.md](../practices/review.md) RV9 and §8 cover the same feature.
- Cursor's PR Routing & Approval routes pull requests to reviewers and can approve low-risk ones when
  the team's criteria are met. It does not approve above a set risk threshold, while its Bugbot or
  Security Agents report findings that need human review, and it waits for those enabled checks on
  the latest commit; a check that a reviewer has not started or has skipped is left out of its
  decision. Cursor says
  it does not replace a full code review ([Cursor approval](https://cursor.com/docs/approval-agents))
  (L).
- Devin's release notes (2026-10-21) let users who can bypass repository rules merge a blocked pull
  request from Devin Review after confirming ([Devin release notes](https://docs.devin.ai/release-notes/2026))
  (L).
- One firm's measured account of AI approval in production is in [evidence.md](evidence.md).

## 3. Intake and orchestration (VOLATILE)

- **Factory.** A Mission holds a planning conversation; after the person approves the plan, an
  orchestrator splits the work into milestones and features, each feature gets a fresh worker session,
  workers hand off through git, and each milestone ends with validation that includes launching the app
  and clicking through flows ([Factory Missions](https://factory.com/news/missions)) (L). Factory
  reports a median run of about 2 hours, 14% of runs longer than 24 hours and a longest run of 16
  days, and says serial execution with targeted parallelism worked better than broad parallelism (M,
  vendor; the page prints the date 2025-02-26, but its content suggests 2026). Factory Research
  compared one agent with three roles (a validator that writes hidden behavioural tests, an
  implementer that never sees them, an orchestrator that decides when to ship) on 24 hard tasks;
  median scores rose for all three models tried, at about 14 times the credits on one task, from
  single runs with no variance estimate ([Factory Research](https://factory.com/news/what-it-takes-for-coding-agents-to-complete-large-software-tasks))
  (M, vendor). Automations (generally available from 2026-09-30) pick ready tickets from Linear or Jira,
  implement them and open a pull request, and others review pull requests, fix review comments and fix
  failing CI ([Factory Automations](https://factory.com/news/automations)) (L). Environments
  (2026-10-12) give each run a fresh sandbox from the last validated image, with admin-set network and
  command rules; OpenCompute (private preview, 2026-10-14) runs those sandboxes on the customer's own
  infrastructure ([Factory sandboxes](https://factory.com/news/droids-now-have-a-fleet-of-sandboxes),
  [OpenCompute](https://factory.com/news/opencompute)) (L).
- **Devin.** A session can coordinate "managed Devins", child sessions each in its own VM with its
  own limits; by default the coordinator starts child sessions without asking, and a setting can turn
  that off ([Devin](https://docs.devin.ai/work-with-devin/advanced-capabilities)) (L). The 2026
  release notes add automations triggered by schedules, Slack and PagerDuty incidents, Linear-triggered
  sessions that start child sessions, and merge-queue state on pull requests
  ([Devin release notes](https://docs.devin.ai/release-notes/2026)) (L; only the entries from
  2026-08-21 to 2026-10-21 were read).
- **GitHub.** Copilot automations run the cloud agent hourly, daily or weekly, on issue or pull
  request events and, since 2026-08-03, on comments. They act in one repository, are billed to and
  attributed to the user who created them, ignore events from users without write access by default,
  and are not available in public repositories
  ([GitHub automations](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations),
  [changelog](https://github.blog/changelog/2026-08-03-trigger-copilot-automations-with-comments/))
  (L).
- **Cursor.** Automations start cloud agents on schedules, webhooks and events from GitHub, GitLab,
  Bitbucket, Linear, Slack (public channels only), Sentry and PagerDuty; opening pull requests is on by
  default; pull request triggers do not run on pull requests from forks
  ([Cursor](https://cursor.com/docs/cloud-agent/automations)) (L).
- **OpenAI.** Codex in Linear starts a cloud task when an issue is assigned to it or it is mentioned;
  Linear's triage rules can assign new issues to Codex, and those tasks run as the issue's creator;
  Codex posts a summary and a link so that a person can create the pull request
  ([Codex in Linear](https://learn.chatgpt.com/docs/third-party/linear)) (L).
- **Claude Code.** Scheduled tasks run a saved prompt on Anthropic's cloud on a schedule (at most
  hourly), an API call or GitHub events ([scheduled tasks](https://code.claude.com/docs/en/routines))
  (L). Projects run parallel cloud threads, each usually with its own pull request that it watches and
  fixes ([Projects](https://code.claude.com/docs/en/claude-projects)) (L). Dynamic workflows run a
  script that fans out subagents; `/batch` splits one large change into 5 to 30 worktree-isolated
  subagents ([workflows](https://code.claude.com/docs/en/workflows),
  [agents](https://code.claude.com/docs/en/agents)) (L). Agent teams, experimental and off by default,
  let a lead session start teammates that share a task list; hooks can block a task's completion as a
  quality gate ([agent teams](https://code.claude.com/docs/en/agent-teams)) (L).
- **Jules.** Scheduled tasks, proactively suggested tasks, a CI fixer for Jules's own pull requests
  (2026-02-19), parallel tasks from the CLI and an alpha REST API. The newest changelog entry is
  2026-03-09 ([Jules changelog](https://jules.google/docs/changelog/)) (L); its status after that is
  `UNVERIFIED`.
- **OpenHands.** OpenHands Cloud starts work when an issue gets the `openhands` label or a comment
  starts with `@openhands`, and opens a pull request only if it judges the issue resolved; automations
  run a full conversation on a schedule as the creating user
  ([OpenHands](https://docs.openhands.dev/openhands/usage/cloud/github-installation),
  [OpenHands automations](https://docs.openhands.dev/openhands/usage/automations/overview)) (L).
- **Amp.** "Orbs" are machines per thread where agents run without supervision (2026-06-30);
  assigning a Linear issue to Amp starts an agent session in an orb (2026-10-19). Neither post says
  whether Amp opens or merges pull requests ([Amp orbs](https://ampcode.com/news/agents-in-orbs),
  [Amp and Linear](https://ampcode.com/news/assign-it-to-amp)) (L).

## 4. Open orchestrators and techniques

- **OpenAI Symphony.** An open specification (Apache-2.0) and an Elixir reference implementation: a
  long-running service polls a tracker such as Linear, makes a workspace per issue and runs Codex in
  it. Defaults: 10 agents at once, retries with exponential backoff, a stalled run stopped after 5
  minutes, up to 20 turns a run. The specification has no approval gate and no merge step; a run can
  end at a state the team defines, such as human review, and people stop a run by moving its ticket.
  The README says: "Symphony is a low-key engineering preview for testing in trusted environments."
  ([Symphony](https://github.com/openai/symphony), [spec](https://github.com/openai/symphony/blob/main/SPEC.md))
  (L). It relies on the Codex app server, which OpenAI's changelog (2026-09-05) labels experimental
  and not supported for production workloads ([Codex changelog](https://learn.chatgpt.com/docs/changelog))
  (L). OpenAI's post on Symphony, with a reported 500% rise in landed pull requests for some internal
  teams, refused direct fetches and was read only through a search summary (`UNVERIFIED`).
- **StrongDM Attractor.** The repository (Apache-2.0, last commit 2026-03-17) holds three
  natural-language specifications (Attractor, a coding-agent loop, a unified LLM client) to be fed to
  a coding agent, and no code. Attractor walks a graph of phases until it converges. StrongDM's
  product page says that the edges between nodes are written in natural language and judged by the
  model, while the specification routes on a small boolean expression over node outcomes and labels,
  to keep routing deterministic ([Attractor](https://github.com/strongdm/attractor),
  [StrongDM](https://factory.strongdm.ai/products/attractor)) (L; the two sources disagree). Its specification also describes
  nodes that pause for a human decision, which StrongDM's own rule of no human review does not use
  (inference).
- **Gas Town, Gas City and Beads.** Gas Town (MIT) coordinates many agents (Claude Code, Copilot,
  Codex, Gemini): a "Mayor" agent splits work, workers run in git worktrees, and work state lives in
  Beads, a tracker kept in git. Finished work goes through the "Refinery", a bisecting merge queue
  that runs verification gates on a batch and merges green batches; workers never push to main. The
  README claims it scales to 20 to 30 agents ([Gas Town](https://github.com/gastownhall/gastown)) (L).
  In an August 2026 essay Yegge writes that "Gas Town effectively burned down" for him with Opus 4.7,
  after working through Opus 4.6, because the model kept changing Gas Town instead of doing the work;
  he moved to a closed-source orchestrator and calls Beads the core of all three
  ([Yegge](https://yegge.ai/essays/the-shape-of-things-to-come/)) (A). The repository is not archived
  (last push 2026-10-21). A Latent Space news digest of 2026-09-17, cited in this library's evidence
  ledger, reported that he shut Gas Town down; his own essay supports "stopped using it", not a
  shutdown of the project. Gas City (MIT) is an SDK built from Gas Town's reusable parts
  ([Gas City](https://github.com/gastownhall/gascity)) (L).
- **Ralph loop.** A technique, not a product: a shell loop that feeds the same prompt to a coding
  agent again and again, one task per loop with fresh context, picking the next item from a plan file;
  tests, type checkers and static analysis push back after each change, and passing builds are
  committed. People write the specs, watch the output and reset the plan when it goes wrong
  ([Huntley](https://ghuntley.com/ralph/)) (A). Huntley's later repository, Overalls, is a self-hosted
  platform of persistent microVMs whose agent threads keep running with the laptop closed; its README
  calls it a research preview launching on 3 November 2026
  ([Overalls](https://github.com/ghuntley/overalls)) (L). Inference: it is execution infrastructure,
  not a queue that checks and merges.

## 5. Products sold under the factory name

- **Factory** calls itself an agent-native software development platform and brands its product
  "Build your software factory" ([Factory](https://factory.com/)) (L). Its own
  definitions are in [README.md](README.md) §1.
- **Warp Factories** routes each work item through a foreman agent and triage, spec, implement and
  review agents and hands back a pull request ([Warp](https://docs.warp.dev/factories/)) (L); each
  agent can run on a harness such as Claude Code or Codex ([Warp harnesses](https://docs.warp.dev/platform/harnesses/))
  (L). Scorers flag failed runs, and self-improvement runs propose fixes to the code or to the
  factory's definition as pull requests for review ([Warp](https://docs.warp.dev/factories/how-factories-work/))
  (L). Warp documents a move from its Oz tools to Factories for teams; Oz stays for standalone cloud
  agents ([Warp transition](https://docs.warp.dev/platform/transitioning-from-oz/)) (L). Its launch date
  and release stage were not found.
- **Harness Cosmos Software Factory Agent.** On 2026-10-08 Harness bought Augment Code's Cosmos,
  Auggie CLI and Context Engine; neither post states the terms. In Harness's description, agents plan a
  change, write code and tests, open a pull request and answer feedback, and then Harness's delivery,
  security and cost agents take it toward production; teams define what agents may do alone and where
  people review or approve ([Harness](https://www.harness.io/blog/harness-acquires-augment-code-cosmos),
  [Augment](https://www.augmentcode.com/blog/augment-code-next-chapter)) (L).

## 6. Limits and prices (VOLATILE) [as-of 2026-10-23]

| Product | Limit | Source |
| --- | --- | --- |
| Copilot cloud agent | One repository, one branch and one pull request per task; GitHub-hosted repositories only; "Each Copilot cloud agent session has a maximum execution time of 59 minutes." | [GitHub](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent) (L) |
| Symphony | 10 agents at once by default; 20 turns a run; a stalled run stopped after 5 minutes | [spec](https://github.com/openai/symphony/blob/main/SPEC.md) (L) |
| Claude Code scheduled tasks | 100 scheduled runs an hour per account; 30 manual or API runs an hour per task; GitHub events above hourly caps are dropped | [scheduled tasks](https://code.claude.com/docs/en/routines) (L) |
| Claude Code Projects | 200 new threads a day across all projects | [Projects](https://code.claude.com/docs/en/claude-projects) (L) |
| Claude Code dynamic workflows | 16 agents at once by default (1 to 256 settable); 1,000 agents a run | [workflows](https://code.claude.com/docs/en/workflows) (L) |
| Claude Code agent teams | One team per session; no nested teams; interactive sessions only; the docs suggest 3 to 5 teammates | [agent teams](https://code.claude.com/docs/en/agent-teams) (L) |
| Jules | Per rolling 24 hours: 15 tasks and 3 at once (free), 100 and 15 (Pro), 300 and 60 (Ultra) | [Jules limits](https://jules.google/docs/usage-limits/) (L) |
| Devin | Sessions can be resumed for 14 days after sleep; concurrency of "Up to 10" or "Unlimited" by plan, with the mapping to plans `UNVERIFIED` | [Devin release notes](https://docs.devin.ai/release-notes/2026), [Devin pricing](https://devin.ai/pricing) (L) |
| Gas Town | The README claims 20 to 30 agents | [Gas Town](https://github.com/gastownhall/gastown) (L) |

Inference: the 59-minute cap on Copilot's cloud agent is shorter than the reliable horizons and the
multi-hour runs in [practices/work-breakdown.md](../practices/work-breakdown.md) F1 and F4, so long
work on that agent is cut into separate tasks. [practices/project-lifecycle.md](../practices/project-lifecycle.md)
§1 marks this cap `UNVERIFIED` because the page it cites does not state it; the page above does.

**Prices.** Factory lists Pro at $20 a month, Plus at $100, Max at $200, Teams at $60 a month per team
plus $40 per seat, and custom Business and Enterprise plans ([Factory pricing](https://factory.com/pricing))
(L); the Missions post says that Missions started for Enterprise and Max plan users
([Factory Missions](https://factory.com/news/missions)) (L). Devin lists Free, Pro at $20 a month,
Max at $200, Teams at $80 a month plus $40 per seat, and custom Enterprise, with extra usage at API
prices ([Devin pricing](https://devin.ai/pricing)) (L). Copilot automations bill Actions minutes and
AI credits to the user who created them ([GitHub automations](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations))
(L). Prices for Cursor cloud agents, Amp orbs, Warp Factories, Harness Cosmos and OpenHands Cloud were
not read.

## 7. Limits and open questions

- Whether a Copilot approval can count on a pull request that Copilot's cloud agent wrote is not
  documented. A direct test on a repository, or a new reading of GitHub's docs, would settle it.
- Devin, Factory, Cursor and OpenHands document opening pull requests; most neither
  describe nor forbid the platform merging on its own. "Not described" in §1 means the docs read are
  silent, not that the product cannot merge.
- No product read documents a deploy to production as its own step.
- Jules's status after March 2026, Warp Factories' launch date and stage, the true date of Factory's
  Missions post, and Devin's concurrency by plan are
  `UNVERIFIED`.
- Not covered for lack of primary sources: Kilo Code's cloud agents, Conductor, Imbue Sculptor and
  Terragon. Ona (Gitpod), Tembo and Linear's own agent features were not searched.
- Every number here is the vendor's own. No independent study of a platform's throughput or defect
  rate was found.

## Sources

All read on 2026-10-23.

**Factory.** Introducing Missions <https://factory.com/news/missions>; What it Takes for Coding
Agents to Complete Large Software Tasks, 2026-08-27
<https://factory.com/news/what-it-takes-for-coding-agents-to-complete-large-software-tasks>;
Automations, 2026-09-30 <https://factory.com/news/automations>; sandboxes, 2026-10-12
<https://factory.com/news/droids-now-have-a-fleet-of-sandboxes>; OpenCompute, 2026-10-14
<https://factory.com/news/opencompute>; pricing <https://factory.com/pricing>.

**Cognition.** Devin advanced capabilities
<https://docs.devin.ai/work-with-devin/advanced-capabilities>; 2026 release notes (first 100,000
characters) <https://docs.devin.ai/release-notes/2026>; pricing <https://devin.ai/pricing>.

**GitHub.** Risks and mitigations
<https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations>; about the
cloud agent <https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent>;
automations <https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations> and
changelog 2026-08-03
<https://github.blog/changelog/2026-08-03-trigger-copilot-automations-with-comments/>; Copilot
approvals, changelog 2026-09-01
<https://github.blog/changelog/2026-09-01-copilot-code-review-can-now-approve-pull-requests/> and docs
<https://docs.github.com/en/copilot/concepts/agents/code-review>; Agentic Workflows
<https://github.github.com/gh-aw/> and changelog 2026-06-11
<https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview>;
third-party agents <https://docs.github.com/en/copilot/concepts/agents/about-third-party-coding-agents>.

**OpenAI.** Symphony <https://github.com/openai/symphony> and spec
<https://github.com/openai/symphony/blob/main/SPEC.md> (the last part of the spec was not read);
changelog (first 100,000 characters) <https://learn.chatgpt.com/docs/changelog>; Codex in Linear
<https://learn.chatgpt.com/docs/third-party/linear>.

**Anthropic.** Scheduled tasks <https://code.claude.com/docs/en/routines>; Projects
<https://code.claude.com/docs/en/claude-projects>; workflows <https://code.claude.com/docs/en/workflows>;
agents <https://code.claude.com/docs/en/agents>; agent teams
<https://code.claude.com/docs/en/agent-teams>; claude-code-action security
<https://github.com/anthropics/claude-code-action/blob/main/docs/security.md> and FAQ
<https://github.com/anthropics/claude-code-action/blob/main/docs/faq.md>; Code Review
<https://code.claude.com/docs/en/code-review>.

**Others.** Cursor Automations <https://cursor.com/docs/cloud-agent/automations> and PR Routing &
Approval <https://cursor.com/docs/approval-agents>; Jules changelog <https://jules.google/docs/changelog/>
and limits <https://jules.google/docs/usage-limits/>; Warp Factories <https://docs.warp.dev/factories/>
and <https://docs.warp.dev/factories/how-factories-work/> (read through Warp's text export),
<https://docs.warp.dev/platform/harnesses/> and <https://docs.warp.dev/platform/transitioning-from-oz/>;
Factory home page <https://factory.com/>; Harness,
2026-10-08 <https://www.harness.io/blog/harness-acquires-augment-code-cosmos>; Augment Code
<https://www.augmentcode.com/blog/augment-code-next-chapter>; OpenHands
<https://docs.openhands.dev/openhands/usage/cloud/github-installation> and
<https://docs.openhands.dev/openhands/usage/automations/overview>; StrongDM Attractor
<https://github.com/strongdm/attractor> and <https://factory.strongdm.ai/products/attractor>; Gas Town
<https://github.com/gastownhall/gastown>; Gas City <https://github.com/gastownhall/gascity>; Steve
Yegge, The Shape of Things to Come, August 2026 <https://yegge.ai/essays/the-shape-of-things-to-come/>;
Geoffrey Huntley, Ralph, 2025-07-14 <https://ghuntley.com/ralph/>; Overalls
<https://github.com/ghuntley/overalls>; Amp, 2026-06-30 <https://ampcode.com/news/agents-in-orbs> and
2026-10-19 <https://ampcode.com/news/assign-it-to-amp>.
