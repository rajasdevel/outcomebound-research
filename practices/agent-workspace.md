---
last_checked: 2026-09-29
volatility: STABLE (the studies behind W0, W2, W3 and W5, and the recorded runs) / VOLATILE (harness facts in §1, §2, §4 and §7)
sources:
  - https://arxiv.org/abs/2602.11988
  - https://arxiv.org/abs/2601.20404
  - https://arxiv.org/abs/2609.13800
  - https://arxiv.org/abs/2606.22953
  - https://pmc.ncbi.nlm.nih.gov/articles/mid/NIHMS2080290
  - https://code.claude.com/docs/en/worktrees
  - https://learn.chatgpt.com/docs/environments/git-worktrees
  - https://cursor.com/docs/configuration/worktrees
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
  - https://openai.com/index/harness-engineering/
  - https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/
  - https://arxiv.org/abs/2607.14611
  - https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/dechand
  - https://docs.temporal.io/activity-definition
---

# Agent workspace and long runs

> **Own results.** Claims marked (O) record observations the maintainers made in their own long runs (§§2-3, §7). They are one project's observations, not a sample, and the records are not published ([CONVENTIONS](../CONVENTIONS.md)). The harness documentation and the cited studies are general.

Re-check when a harness changes where it places, sweeps or isolates worktrees, how it stores
sessions or memory, or how it stops or resumes a long run.

Where coding agents keep their work, sessions and what they learn, how work passes between
sessions and delegates, and what keeps a long autonomous run moving.

This reference covers where agents keep their work and what they learn, and what keeps a long
autonomous run moving: worktrees and working files inside the repository, one-page session
handoffs, memory and session history kept on one machine, digests in steps a person reads, and the
causes of stalls in unattended runs with the remedies the sources and the runs point to. It is for anyone who sets
up a repository where several agents work, hands work between sessions, or starts an agent on a
goal meant to run for hours without the person. What lets an agent act (permission layers,
classifiers, approvals and recorded grants) is in [agent-authorization.md](agent-authorization.md); research on agent
memory itself (poisoning, confabulation, portability across tools) is in
[agent-memory.md](agent-memory.md).

**Evidence classes.** M measured; L lab or vendor report or documentation; S standard; P
practitioner consensus; A anecdote or one uncontrolled report; O an observation from
the maintainers' own runs. **Citations.** Sources are linked inline; bracketed ids resolve in
[`_evidence/2026-09-25.jsonl`](../_evidence/2026-09-25.jsonl), or in
[`_evidence/2026-09-26.jsonl`](../_evidence/2026-09-26.jsonl) for `sizing-` ids. "The maintainers'
runs" means observations from unattended runs where agents implemented work items
for many hours, and from multi-day sessions.

## Key findings

**W0. Always-loaded text has a price.** Context files did not generally raise task success and
raised inference use by more than 20%; an `AGENTS.md` went with 28.6% lower median runtime and 16.6%
fewer output tokens. Guidance an agent needs only at some moments is reached by a pointer with a
condition, not loaded every session. M.

**W1. Worktrees and working files kept inside the repository, in a git-ignored folder, with a
sweep: moderately supported.** Three coding harnesses document worktrees for parallel agents, each
under its own directory with its own sweep; no study compares worktree isolation with none, or
working files in the repository with a temporary directory. Temporary and session directories are
cleared without warning. Without a sweep of its own, one checkout held dozens of worktrees
after a week (O). Codex's default sandbox makes a `.agents/` folder read-only: a write there failed
under codex-cli 0.159.2 and succeeded once the folder was added with `--add-dir` (one probe each
way). A folder's name therefore matters: a name on a harness's protected list makes it read-only
there. L, A, O.

**W2. A one-page handoff that keeps accepted choices, realised effects and open obligations is
weakly supported for agents, by analogy and lab practice.** Structured shift handoffs cut medical
errors 23%; evicting the plan from context cut success by 34.7 points; labs keep progress files and
checked-in plans. A model-handoff pipeline that carries the same three things (CFRC: a contract
built from accepted progress, a checked continuation graph, execution admitted only on live
evidence) reached comparable macro accuracy at 22.0–34.6% of strong full-task agents' inference
cost, across five environments and two same-provider model pairs; it measures that whole pipeline,
not a handoff file. No agent study compares a handoff file with none, and a handoff is only as good
as its checked claims. M, L.

**W3. Memory shared across sessions is contested: benefits are measured mostly by vendors, harms
independently.** What separates the two is a source per fact, a date, a check against the source at
use, expiry, and no authority. Harness memory and session history live on one machine, keyed by the
repository's path. M, L, S.

**W4. Recorded grants for one irreversible act are weakly supported.** Approval fatigue is well
measured; standing policies written by users let more overreach through than per-action approval,
and no study tests a narrow, dated, expiring grant for one named act. The nearest evidence favours a
grant a tool checks and consumes over one a model reads ([agent-authorization.md](agent-authorization.md) A1, A5). M.

**W5. Digests in steps a person reads are error-prone: supported.** Of 1,047 people comparing key
fingerprints, hexadecimal was the most error-prone format, and near-matching strings were missed
more often than words or numbers. Steps that name a version, branch, tag or path avoid the problem
(inference). M.

**W6. Unattended runs stop where the process needs the person, not where the work does.** In the
maintainers' unattended runs, the critical path ran through gates routed to the person, finished
work waited on clerical acts, and a per-item ceremony took a large share of the run. Most of the
questions an overnight run left for the person were not theirs to answer, and many decisions went
to the person that the run could have made and recorded. A stop on size that the person did not set
ended a later run early, and runs that required answers before the start did not start. O.

**W7. Authority must be recorded where the harness's permission layer reads it.** Claude Code's
auto-mode classifier reads the person's messages and the commands the agent runs, not their output,
so a goal file, a memory or a relayed decision is invisible to it, and a boundary stated in
conversation can be lost when compaction removes the message. Acts the person approved in general
words were refused. The mechanism is in [agent-authorization.md](agent-authorization.md) §2. L, O.

**W8. State kept only in the conversation does not survive compaction; state in files does.**
Conversation-only rules are lost at compaction; path-scoped rules and nested instruction files are summarised away with the
rest of the history; compaction summaries have been observed instructing the model to invent missing
data and hide failures. L, M.

**W9. A delegate's report is a claim; a fixed shape that carries its evidence lets the orchestrator
check it.** Reports that name
each check's command and verdict, the red run, every departure and a mutation control let the
orchestrator verify without redoing the work. Self-reports of "all closed" and counts copied
between documents were wrong when checked. P, A, O.

## 1. Always-loaded text (W0)

- Context files did not generally raise task success and raised inference use by more than 20%;
  repository overviews did not help. M, 2026-02 (v2 2026-06),
  [arXiv 2602.11988](https://arxiv.org/abs/2602.11988)
- An `AGENTS.md` went with 28.6% lower median runtime and 16.6% fewer output tokens (10 repositories,
  124 pull requests). M, 2026-01, [arXiv 2601.20404](https://arxiv.org/abs/2601.20404)
- Claude Code loads the first 200 lines or 25 KB of its `MEMORY.md` index, whichever comes first, at
  the start of every conversation; content past that is not loaded [harness-loading-coverage-6]. L
  (VOLATILE), read 2026-09-25.
- Path-scoped rules and nested instruction files load into message history when their trigger file
  is read, so compaction summarises them away; a guardrail that must survive a long session goes in
  the project-root file or an unscoped rule [harness-loading-coverage-7]. L (VOLATILE), read
  2026-09-25.

Guidance an agent needs only at some moments can be reached by a pointer with a condition, not
loaded every session.

## 2. Worktrees and working files (W1) (VOLATILE)

| Harness | Where its worktrees live | What its sweep removes | Source |
| --- | --- | --- | --- |
| Claude Code | `.claude/worktrees/<name>/`, or wherever a `WorktreeCreate` hook puts it; edits and git redirects into the main checkout are blocked; entering a worktree outside that folder asks for approval, which a permission rule cannot suppress (only `bypassPermissions` skips it) | a subagent's worktree when the subagent finishes without changes; worktrees it made for subagents and background sessions once older than `cleanupPeriodDays` (30 days by default) and holding no work; never one made with `git worktree add` or by a hook | [docs](https://code.claude.com/docs/en/worktrees) [as-of 2026-10-01] |
| Codex | `$CODEX_HOME/worktrees` | keeps the 15 most recent, deletes older ones after a snapshot | [docs](https://learn.chatgpt.com/docs/environments/git-worktrees), read 2026-09-29 |
| Cursor | managed per machine | keeps at most 25 per machine, cleaning up every 6 hours | [docs](https://cursor.com/docs/configuration/worktrees), read 2026-09-29 |

- OpenAI's harness team runs one application instance per change, each in a git worktree. L,
  2026-02-11, [Harness engineering](https://openai.com/index/harness-engineering/) (read through a
  verbatim mirror; the page returned 403).
- All three vendors default elsewhere and sweep automatically, so a vendor-neutral folder inside the
  repository trades an approval prompt in one harness for durability. The rule against temporary
  directories rests on anecdote: they are cleared without warning, taking any work kept there (A).
- **A harness can make the folder read-only.** Codex's default `workspace-write` sandbox protects
  `<writable_root>/.agents` as read-only, recursively, when it exists as a directory, along with
  `.git` (and a linked worktree's resolved Git directory) and `.codex` (approvals and security page
  [as-of 2026-10-01]; no version stated). An agent running in Codex with the repository as its
  writable root therefore cannot write working files, handoffs or worktrees kept under a `.agents/`
  folder, nor commit, unless those paths are added as writable directories; a folder under another
  name is not on the documented list. Under codex-cli 0.159.2's default `workspace-write` sandbox,
  writing `.agents/work` failed with "Operation not permitted"; started with
  `--add-dir <repository>/.agents`, the same write succeeded (O, 2026-10-01, one probe each way). The protected paths differ by harness, so a write test in each
  harness the project uses shows whether a folder name works ([codex.md](../harnesses/codex.md#1-instruction-files-and-precedence)
  §3, Codex). L.
- **Placing harness worktrees in a project folder.** A Claude Code `WorktreeCreate` hook replaces its
  `git worktree` creation for `--worktree`, for subagents with `isolation: "worktree"` and for
  background sessions: it receives a name and prints the directory to use, so a project can place
  harness worktrees in its own folder. With the hook, `.worktreeinclude` is not processed (copy
  files such as `.env` inside the hook); since v2.1.216 an absolute path with `.` or `..` segments,
  or any path through a symlink below the repository root, is refused. `WorktreeRemove` is the
  cleanup counterpart; a non-zero exit from `WorktreeCreate` aborts creation, and one from
  `WorktreeRemove` fails the removal if the directory is still there. L, hooks reference
  [as-of 2026-10-01]; not tried.
- **Check the base.** Claude Code's subagent worktrees branch from the repository's default branch,
  not from the parent session's `HEAD`, unless `worktree.baseRef` is set to `"head"` (L
  [as-of 2026-10-01]). In the maintainers' runs, a worktree cut from the default branch rather than from the base the
  orchestrator dispatched from put a delegate on the wrong base, and each task description then
  carried a base-commit check (A).
- **A removed worktree ends the delegate.** Claude Code removes a subagent's isolated worktree when
  the subagent stops with no changes (L, sub-agents page [as-of 2026-10-01]), and in one
  repository's runs an agent whose worktree was gone could not be resumed (A); worktrees the
  orchestrator makes itself, kept while their agent might still be needed, avoid that.
- **Worktrees accumulate.** Without a sweep, one checkout held dozens of worktrees after a
  week of multi-agent work, gigabytes in all. Some had been created by the harness
  for its own subagents and were still inside its 30-day retention; some held git-ignored
  evaluation results, which had to be copied out before removal. Most had their commits on the main
  branch, some held commits not on it, and a few had uncommitted changes; a sweep limited to
  worktrees whose commits are on the main branch and that hold no uncommitted change would have
  removed most of them, most of the space, and lost nothing (O; the last claim an inference from the
  listing). A sweep that loses nothing would record each
  worktree's branch, tracked and untracked changes, ignored content and whether its commits are
  reachable from a kept branch, copy or commit what is not kept elsewhere, and only then remove
  it (inference).
- **Moving a worktree** is one `git worktree move`, but other things hold its path: containers that
  bind-mount it, editor windows and agent sessions working in it, and a harness's session history
  keyed by the path (§4). In one case six idle worktrees moved with their uncommitted files
  intact; the one with mounted containers and open sessions waited for a pause the person chose, and
  its session history was carried to the new path (A).
- **One orchestrator per working tree.** A second orchestrator session opened on the same checkout
  reviewed the same range, replaced the first session's review file and wrote lines into its record;
  the first found edits it had not made and stopped until ownership was settled (A, the maintainers'
  runs).
- **Tools write into the working tree.** The Playwright MCP server saved browser console logs and
  page snapshots in a `.playwright-mcp/` folder in the working directory (many console logs over two
  sessions); such folders surface as untracked files unless they are ignored or the tool's output is
  pointed elsewhere (O, 2026-09-25 and 2026-09-29).
- A repository's own discovery and checks exclude harness worktrees inside the checkout, which
  otherwise read as project components and are scanned (A, the maintainers' runs).
- A git-ignored folder is shared by the agents on one machine, not by other clones or cloud
  sessions, so a handoff that another machine will read has to travel in the ticket or the pull
  request, and a fact every clone needs in committed guidance (inference). Ignoring the folder
  through `.git/info/exclude` keeps the rule local to one clone, so a file placed there on purpose
  needs `git add -f`.
- **Open.** No measured study compares worktree isolation with none, or working files in the
  repository with a temporary directory.

## 3. One-page handoffs (W2)

- Structured shift handoffs (I-PASS) cut medical errors 23% (24.5 to 18.8 per 100 admissions) and
  preventable adverse events 30% (4.7 to 3.3), P<0.001, over 10,740 admissions at 9 sites. M, NEJM
  2014-11-06. A 2025-09-18 systematic review rates I-PASS certainty moderate (raised from low) and
  SBAR low, and notes two null trials (Argentine paediatric intensive care; an orthopaedic
  adaptation). The figures are read from that review
  ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/mid/NIHMS2080290)); the journal and PubMed did not
  open.
- Commitment-Frontier Residual Completion (CFRC), a pipeline for handing a stateful task from one
  model to another, freezes a residual contract from the accepted progress (accepted choices,
  realised effects, unfinished obligations), closes the successor's continuation into an
  evidence-linked graph that is checked before it may act, and admits execution only when the
  remainder is covered, with live receipts discharging obligations. Across five environments and two
  same-provider model pairs it reached comparable macro accuracy to strong full-task agents at
  22.0–34.6% of their mean per-surface inference cost (cost, not tokens), with further
  cross-provider results. The result is for that whole pipeline; it does not establish that a
  one-page handoff file helps. M, 2026-09-12, [arXiv 2609.13800](https://arxiv.org/abs/2609.13800)
  (abstract [as-of 2026-10-01])
- Evicting the plan from an agent's context cut ALFWorld success by 34.7 points: agents do not hold
  plans internally. M, 2026-06-22, [arXiv 2606.22953](https://arxiv.org/abs/2606.22953)
- Anthropic's long-running harness reads the git log and a progress file (`claude-progress.txt`) at
  every session start, because "each new session begins with no memory"; no metric is reported. L,
  2025-11-26, [Effective harnesses](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents).
  In its multi-agent research system, a lead nearing 200,000 tokens saves its plan to memory, and
  subagents store outputs externally and pass references back. L, 2025-06-13,
  [Multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- OpenAI keeps "execution plans with progress and decision logs that are checked into the
  repository", because "anything it can't access in-context … effectively doesn't exist". L,
  2026-02-11, [Harness engineering](https://openai.com/index/harness-engineering/)
- Cognition: "Actions carry implicit decisions", and compressing history into key decisions "is hard
  to get right". A/L, 2025-06-12, [Don't build multi-agents](https://cognition.com/blog/dont-build-multi-agents)
- Architecture decision records, action research at one company (7 interviews over 3 months): three
  of four challenge types were addressed, and "where documentation is stored has a massive influence
  on its perceived usefulness". M (small), ECSA 2024,
  [paper](https://rebekkaa.github.io/files/2024_ECSA.pdf)
- **Open.** No agent study compares a handoff file with none. Agents misreport progress unless a
  claim is checked against a tool result (see [work-breakdown.md](work-breakdown.md) F3), so a
  handoff is as good as its checked claims.

**Contents the sources point to.** Progress with each check's verdict, work in flight, the next step,
the choices made and the obligations still open: the same three things that the CFRC pipeline
carries (accepted choices, realised effects, open obligations). The sources set no length or
format; one page is this reference's reading of the lab practice above (inference).

**Between an orchestrator and its delegates (W9).** A delegate's final report is all the
orchestrator sees, and it is a claim. The report shape that let an orchestrator verify without
redoing the work, in the maintainers' runs (P/A):

1. The commit, the branch, and the files changed with line counts.
2. The red run: the named test failing before the change.
3. Each check's exact command and its result as PASS, FAIL or UNVERIFIED, with its last lines.
4. Every departure from the brief, and every place the brief was unclear, wrong or silent.
5. One mutation control per core rule, made in a scratch copy, with the tree byte-identical after,
   checked by comparing file contents and modes (and symlink targets, staged entries and the
   untracked files that existed before); `git status --porcelain` alone prints the same line for two
   different contents of an already-modified file (O, git 2.56.0, 2026-10-01; see
   [git.md](git.md)).
6. The real output of any command or surface the change affects, verbatim.
7. Anything the delegate stopped on.

Why the shape matters, from the maintainers' runs (O): a delegate's report that every open item
was closed did not hold, since an independent reader then found several still open; a review that
reproduced the behaviour and ran the suite green still found completeness claims that did not hold,
including two counts copied between documents that were both wrong; and a ledger's summary counts
did not match a recount of its own rows. A recount from the source caught each of these.

Every run also needed procedural facts that no task description carried: the worktree path, the
`PATH` line that makes the tools resolve, a list of what not to do (run the whole suite, push,
touch the tracker), and the commit convention. They repeat across tasks, so they fit a document the
delegate loads better than each task description (inference). A fix round handed to a fresh
delegate, which must first re-read the work, took about 134,000 tokens in one run (A; only the
total was recorded).

## 4. Memory and session history on one machine (W3)

Benefits are measured mostly by vendors; harms are measured independently.

- GitHub Copilot's memory raised the pull-request merge rate from 83% to 90% and positive review
  feedback from 75% to 77% (A/B, p<0.00001). Each memory cites code that is checked against the
  current branch when it is used; seeded false memories were caught and corrected; unused memories
  expire after 28 days; only users with write access create them; memory is shared across Copilot's
  agents. L, 2026-01-15,
  [GitHub blog](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/),
  [docs](https://docs.github.com/en/copilot/concepts/agents/copilot-memory).
- Memory tool plus context editing: +39% on an internal agentic-search evaluation (context editing
  alone +29%), with 84% fewer tokens. L, 2025-09-29, [Anthropic](https://claude.com/blog/context-management)
- A pre-registered SWE-bench Verified repeat-mistake test went from 67.3% to 77.6% with memory (49
  pairs, single trial); the multi-seed effect was +0.24 per instance, 95% CI [0, 0.47]. M (weak, one
  author), 2026-06-24, [repository](https://github.com/SaravananJaichandar/coding-agent-memory-benchmark)
- DreamBench-SWE: no memory 0.117 against 0.456–0.539 with memory; memory systems still used stale
  items 20% of the time and imported irrelevant ones 47%. M (one author), 2026-08-21,
  [arXiv 2608.20664](https://arxiv.org/html/2608.20664)
- Cross-domain memory for coding agents gained 3.7%; high-level lessons transfer between tasks, while
  low-level traces "often induce negative transfer". M, 2026-04-15,
  [arXiv 2604.14004](https://arxiv.org/abs/2604.14004)
- Payloads planted in memory files attacked current and later sessions of two coding agents (Claude
  Code and Codex); getting an agent to write them from untrusted content was hard. M, 2026-07-16,
  [arXiv 2607.14611](https://arxiv.org/abs/2607.14611). The same study advises explicit review of any
  change to high-impact persistent files such as `CLAUDE.md` and `AGENTS.md`, permission boundaries
  on memory updates, and validating memory files at every session start
  [instruction-file-security-authority-12].
- Poisoning carried through shared artifacts reached 60–80% of agents in chains of up to eight hops.
  M, 2026-09-28, [arXiv 2609.35576](https://arxiv.org/abs/2609.35576). Query-only memory injection
  (MINJA) succeeded 98.2% of the time, with 76.8% attack success. M, 2025-03-05 (v5 2026-02-12),
  [arXiv 2503.03704](https://arxiv.org/abs/2503.03704)
- In a four-agent pipeline, shared-memory poisoning reached execution in every undefended trial;
  authorization enforced by structure held unsafe actions at 0%. M, 2026-09-15,
  [arXiv 2609.17648](https://arxiv.org/abs/2609.17648v1)
- OWASP lists memory and context poisoning as ASI06 ("Memory should be treated as part of the attack
  surface"). S, 2025-12-09 and 2026-05-13,
  [Top 10 for Agentic Applications](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/),
  [ASI06 note](https://genai.owasp.org/2026/05/13/memory-is-a-feature-it-is-also-an-attack-surface/).
  OWASP's guidance also says to scan every memory write before it is committed and not to re-ingest
  an agent's own outputs as trusted memory [instruction-file-security-authority-4]. P.
- Lab guidance on memory: record only durable, project-specific facts the agent could get wrong from
  general knowledge, load an index and read topic files on demand, and treat repository-committed
  memory as a prompt-injection surface [other-labs-27] (L); keep human-written instruction memory
  separate from agent-accumulated learning, so experience notes do not gradually pollute the core
  rules [glm-f6] (L).
- **Where a harness keeps it (VOLATILE).** Claude Code's auto memory lives at
  `~/.claude/projects/<project>/memory/`, where `<project>` is derived from the git repository, so
  all worktrees and subdirectories of one repository share one memory directory; it is
  machine-local and not shared across machines or cloud sessions. The session transcripts sit
  beside it, under `~/.claude/projects/<project>/`, and a retention sweep deletes them once older
  than `cleanupPeriodDays` (30 days by default; 1 is the minimum and 0 is refused). L, memory and
  directory pages [as-of 2026-10-01]. Moving or renaming the repository's folder starts an empty key:
  the earlier sessions and memory stay under the old one until copied across, while Codex's threads
  stayed at their old paths (O, 2026-10-01). Neither is a durable record, so what the next session
  needs has to be in the repository's files (inference).

**What the sources imply for memory entries (inference).** One fact per file, with its source and
the day it was checked; re-checked against its source before use; deleted when wrong; never a grant
of authority; read by the same security checks as instruction files. A git-ignored folder is shared
by one machine's agents, not by other clones, so a fact every clone needs is committed.

## 5. Grants and the permission layer (W4, W7)

The evidence on approval and its decay, how Claude Code's auto-mode classifier and Codex's automatic
reviewer decide, what a grant for one irreversible act needs, and the field's authorization patterns
are in [agent-authorization.md](agent-authorization.md). For a workspace, the evidence points to
three things (inference): a grant written as the person's own words naming the acts it covers, how
many uses and an end, kept in a file the enforcing tool reads and not only in the conversation; the
harness's own permission rules (in Claude Code, an `ask` or `deny` rule in user or managed
settings) holding the edge whatever files say; and an end-of-run digest that keeps what needs the
person apart from what was done on the grant.

## 6. Digests in steps a person reads (W5)

- Of 1,047 people comparing key fingerprints, hexadecimal was the most error-prone format;
  near-matching strings were missed more often than words or numbers. M, 2016,
  [Dechand et al., USENIX Security](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/dechand)

Steps that name a version, branch, tag or path avoid the problem; a digest can stay in reports that
a tool writes and reads (inference).

## 7. What stalls long autonomous runs (W6–W8)

Observed in the maintainers' unattended runs (O, one project; no counts are given):

| Cause | What was observed | What removed or would remove it |
| --- | --- | --- |
| More work than the window, one item at a time | A queue of work items worked by one agent at a time, each taking an hour or more; in nine hours, only a minority finished | Sizing the whole plan against the window before starting, as an estimate. A later run showed that a stop at about twice the stated size does not help: see the size-stop row below |
| Per-item ceremony | A fresh review, per-sentence coverage records and a full verification after each item took a large share of each item's time and of the run | Running the suite once per integration or phase, not per item; keeping the review for what a check cannot catch |
| Missing tooling | The parallel test plugin was absent from the environment the agents ran in, so verification ran serially; the type checker was installed in only one virtual environment, so every floor call needed a `PATH` prefix or read UNVERIFIED | Tools on the path the harness uses; one interpreter for the build |
| The critical path ran through the person | Most drafted work items routed a stop condition to the person; an item parked on its stop condition (a size bar, one file outside its bounds) held the chain of items behind it; most questions an overnight run left the person were not theirs to answer; the person received many decisions a day (O) | A stop that names only an act outside the granted authority; a path beyond an item's advisory file list, within that authority, named in the commit and not stopped on |
| Finished work parked on clerical acts | A finished change waited on a routine re-run of a tool whose change was graded "none"; another waited days for a person to confirm a CI step a command had already read as passed; reversible choices went to the person anyway | Reversible choices decided in the run, each recorded in one line with its undo; observations turned into command checks |
| The harness refused acts approved in general words | A permission layer that reads only the person's messages refused tracker writes and records that followed from an instruction given in general words | Authority recorded where the harness reads it ([agent-authorization.md](agent-authorization.md) §2) |
| A size stop and answers required before the start | In a later night of the maintainers' unattended runs, a stop at twice the estimated changed lines ended one run after under an hour of work; most counted lines were earlier work committed unchanged, and the run held every remaining item on that one stop. The hour estimates of the runs that finished were five to seven times longer than the runs took. Three runs whose hand-off asked for several answers before the start did not start; one run held all its work on a decision only a conditional sub-step needed, because the decision was put in the turn's final message (O) | No stop on size, count or duration that the person did not set; a stop that holds only the item that meets it, recorded where the person reads it, while the run continues with items that do not depend on it; a run that starts without answers, each unanswered decision holding only the work that waits on it |
| Oversized inputs | Task descriptions generated for delegates ran to thousands of words, and some drafts to over ten thousand, because each quoted every cited section verbatim; one draft exceeded the tracker's body limit | A path and section cited; only what the implementer must copy quoted |

**Harness facts (VOLATILE).** Claude Code's auto-mode classifier reads the person's messages and the commands
the agent runs, not their output; a boundary stated in conversation is re-read from the transcript
on each check and can be lost at compaction; a blocked action clears only when the person's message
names that action and its specifics; and `autoMode` counts only in user, `--settings` or managed
settings. The full mechanism, the built-in rules and the hooks that touch
the classifier are in [agent-authorization.md](agent-authorization.md) §2. A session can outlive many compactions, so a boundary stated once in conversation does not
last.

**Remedies the sources and the runs point to (inference).**

- A goal started in a fresh session whose first message is the goal's text is read by both the
  permission layer and the model; acts that recur can go into the harness's allow configuration.
- Durable rules and progress kept in files survive compaction: conversation-only rules disappear
  at compaction
  [glm-f5] (L); compaction summaries in reinforcement-learning runs included instructions to invent
  missing data and hide failures, which were often followed (flagged in 2.15% of one model's
  summaries and 0.27% of another's) [openai-f16] (M, training runs, not deployment). A progress file
  whose claims are checked against tool results survives both. A Claude Code `PostCompact` hook
  receives each summary, so a run can keep them for checking against the files it relies on
  ([cross-harness.md](../harnesses/cross-harness.md#7-compaction-and-long-sessions) §7).
- Tools can be put on the harness's path from a hook: in Claude Code a `SessionStart`, `Setup`,
  `CwdChanged` or `FileChanged` hook can append `export` lines to the file named by
  `CLAUDE_ENV_FILE`, and they apply to the session's later Bash commands (from `SessionStart` and
  `Setup` for the whole session; from `CwdChanged` and `FileChanged` until the next directory
  change), for example a `PATH` entry that puts the project's tools first; other hook events do not
  receive the variable. L, hooks reference [as-of 2026-10-01]; not tried here.
- In the maintainers' runs, a request for a person ended that item's turn and not the run: the
  agent took the next ready item. A stop condition was met, a request raised, a one-line answer
  relayed, the blocker worked and the original resumed (A). Claude
  Code offers this at the tool level for a calling program: in `-p` mode a `PreToolUse` hook may
  return `permissionDecision: "defer"`, the process exits with `stop_reason: "tool_deferred"` and
  the pending call in `deferred_tool_use`, the caller asks the person through its own interface, and
  `claude -p --resume <session-id>` fires the hook again, which can then allow the call with the
  answer in `updatedInput`. It works only when the turn made one tool call, has no timeout (the
  session waits on disk, subject to the retention sweep), and the resumed `-p` run does not restore
  the stored permission mode. L, hooks reference [as-of 2026-10-01].
- External effects that are safe to repeat. Workflow engines treat a step that touches the outside world
  as possibly executed more than once: Temporal's activities "may be retried" and so "executed more
  than once"; a completed one is not re-run when a workflow replays, one that never reported is
  retried, and each should be idempotent (L, [Temporal](https://docs.temporal.io/activity-definition) [as-of 2026-10-01]). The
  practice that the engines' documentation implies for agent runs: a checkpoint of the conversation is not durable execution;
  give each external effect an idempotency key derived from the step; journal a model's output and
  replay it on recovery rather than sampling again; a pause for a person waits with a timeout and
  ignores a duplicate resume; an external write has a compensating action; and a crash in the middle
  of a tool call is the case to test (P, workflow-engine documentation [as-of 2026-08-19]). The measured
  case for it is in [agent-authorization.md](agent-authorization.md) §4: after a timeout or a lost acknowledgement,
  agents re-proposed an already-approved action in 46–58% of trajectories.
- Costly loops are bounded, for example one or two CI rounds before handing back [deterministic-18] (A,
  Stripe: over 1,300 merged pull requests a week with no human-written code, each reviewed by a
  person; rule files scoped to subdirectories rather than global, so rules do not fill the window; a
  lint loop run locally before the first push; after the second push and CI run the branch goes back
  to its operator; each agent gets a curated "smaller box" of tools; post [as-of 2026-10-01]);
  OpenAI's ExecPlan template tells the agent not to ask for next steps between milestones
  [sizing-lab-45] (L). Harness stall guards: Codex CLI 0.155.0 blocks a goal after three empty
  automatic continuation turns (L, release notes of 2026-09-17 [as-of 2026-10-01]); that Claude Code
  returns control after several turns without tool use, and that Codex counts nested subagents'
  tokens against the root goal's budget, were found on no page read and are `UNVERIFIED`.
- Landing rules from the maintainers' runs (A): integration checks run fail-fast and commit only
  on a clean exit; a check is not piped in a landing script, since a pipe loses its exit status;
  after any history edit, `git log` and `git show --stat` are read; integration happens only from a
  worktree the integrator owns, with the branch checked before committing.

## What the evidence supports (inference)

These points are this reference's reading of the findings above. They are not orders.

1. Agent work kept in one git-ignored folder in the repository, with a worktree and a working-file
   folder per task, avoids the temporary and session directories that are cleared without warning.
   A sweep on a schedule that keeps work, and one orchestrator per working tree, address the
   accumulation and collision seen in the runs (W1).
2. A one-page handoff at the end of each session, kept in that folder, is the practice the lab
   sources describe; one that another machine will read has to travel in the ticket or pull request
   (W2).
3. Shared memory as one fact per file with source and date, re-checked before use, never a grant and
   scanned like instruction files, is what the sources describe. Harness memory and session history
   stay on one machine and are swept, so what every clone needs is committed (W3).
4. A grant for an irreversible act recorded as the person's words with an end, and backed by a
   harness permission rule where one exists, is the pattern the evidence favours
   ([agent-authorization.md](agent-authorization.md)) (W4, W7).
5. Steps a person performs that name versions, tags, branches and paths avoid the digest errors
   (W5).
6. For an unattended run, the stall causes in §7 point to sizing the whole plan as an estimate with no stop on size, a goal started as
   the first message of a fresh session, recurring acts allowed in the harness, the tools on the
   path, requests that end an item's turn and not the run, and external effects that are safe to
   repeat (W6–W8).
7. Delegates' reports in the fixed shape above let an orchestrator check the claims that matter
   (W9).

## Limits and open questions

- The workspace sweep was one reader on one day; the I-PASS figures come from a review, and the
  habituation study from its abstract. Several agent results are single-author preprints.
- The stall causes, the worktree observations and the delegate-claim evidence come from the maintainers'
  runs; the harness facts are from documentation, and whether the suggested allow entries clear the
  observed denials was not tested.
- Nothing here measures the practices themselves: whether a resuming agent reads a handoff without
  being told to, or whether a goal record reduces stops, is untested.

## Sources

Read 2026-09-28 to 2026-09-29 unless dated otherwise: Claude Code docs on worktrees, memory, context
window, permission modes and auto mode (worktrees, memory, hooks, sub-agents and the `.claude`
directory page re-read 2026-10-01); Codex and Cursor worktree docs; Codex's approvals and security
page (2026-10-01); OpenAI, Harness engineering
(2026-02-11, via mirror); Anthropic, Effective harnesses for long-running agents (2025-11-26), How
we built our multi-agent research system (2025-06-13), Context management (2025-09-29); Cognition,
Don't build multi-agents (2025-06-12); GitHub, Building an agentic memory system for GitHub Copilot
(2026-01-15) and Copilot memory docs; OWASP Top 10 for Agentic Applications (2025-12-09) and the
ASI06 note (2026-05-13); I-PASS via the 2025 systematic review (PMC); Dechand et al., USENIX
Security 2016; ECSA 2024 on decision records; Stripe, Minions part 2 (2026-02-19); Z.ai memory
mechanism docs; Meta Muse Code configuration docs; Temporal, activity definition
<https://docs.temporal.io/activity-definition> (2026-10-01); arXiv 2602.11988, 2601.20404,
2609.13800 (abstract re-read 2026-10-01), 2606.22953, 2608.20664, 2604.14004, 2607.14611,
2609.35576, 2503.03704, 2609.17648; the
coding-agent-memory-benchmark repository (2026-06-24); Codex CLI 0.155.0 release notes
<https://github.com/openai/codex/releases/tag/rust-v0.155.0> (2026-09-17, read 2026-10-01); OpenAI's
report on deception in compaction summaries (2026-09-16). The (O) claims rest on the maintainers' unpublished observations; one write probe each way under codex-cli 0.159.2
(2026-10-01).
