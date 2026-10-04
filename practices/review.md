---
last_checked: 2026-10-01
volatility: MONITOR (lab guidance on verifiers and code review changes with model releases; the measured studies and the recorded runs do not) / VOLATILE (§8, which AI reviewers can count as a required approval)
sources:
  - https://arxiv.org/abs/2502.04313
  - https://arxiv.org/abs/2604.03196 (read 2026-10-04)
  - https://github.blog/changelog/2026-09-01-copilot-code-review-can-now-approve-pull-requests (read 2026-10-04)
  - https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-code-review (read 2026-10-04)
  - https://docs.github.com/en/copilot/concepts/agents/code-review (read 2026-10-04)
  - https://code.claude.com/docs/en/code-review (read 2026-10-04)
  - https://learn.chatgpt.com/docs/third-party/github (read 2026-10-04)
  - https://arxiv.org/abs/2404.13076
  - https://arxiv.org/abs/2006.14779
  - https://arxiv.org/abs/2602.14611
---

# Independent review of agent work

> **Own results.** Claims marked (O) are the maintainers' own observations of review in their own agent work (§§1-7). They are stated without model names or counts, are one project's observations rather than a sample, and the records are not published ([CONVENTIONS](../CONVENTIONS.md)). The rest summarises published studies and lab guidance.

When a second reader of an agent's work or of the spec it runs from adds signal, which reader to
use, how many rounds a large spec takes, and how to carry a review's findings until each is fixed
and shown fixed, and which AI reviewers can count as a required approval.

Re-check when a lab changes its guidance on fresh-context verifiers or code review, a study compares
same-family with cross-family review of code at equal effort, or a new model family joins the
reviewers in use, or GitHub, Anthropic or OpenAI changes whether its reviewer's approval can count
toward a merge requirement (§8). Evidence ledger records are as verified on 2026-09-25 and 2026-09-26.

This reference answers when an independent reader of work an agent did, or of a plan it will run
from, finds something no check found; whether that reader should come from the author's model
family or another; what a review's verdict does and does not establish; how many rounds a large,
decision-complete spec takes; what happens to findings deferred as minor; and how to verify that
the fixes a review accepted actually landed; and which AI reviewers' approvals a hosted repository
can count, with what review agents' measured signal is. It is for anyone who decides whether work needs a
second reader, chooses the reviewer and its instructions, runs review rounds on a spec, or keeps the
findings a review leaves. How large a change a reviewer can read well is in
[work-breakdown.md](work-breakdown.md) F8; judges that score evaluation runs are in
[llm-as-judge.md](llm-as-judge.md), [evaluations.md](https://github.com/rajasdevel/outcomebound/blob/main/docs/evaluations.md) and
[writing-for-models.md](writing-for-models.md) §9.

**Evidence classes.** (M) measured; (L) a lab's or vendor's guidance or its report about its own
product; (P) practitioner consensus; (A) one person's view or one uncontrolled report; (O) a result
observed in the maintainers' own agent work. Each key finding carries a strength: **strong**
(several independent measured results, or measurement plus convergent guidance), **moderate**
(guidance or own observations plus some independent measurement), **weak** (one source or
anecdote). `UNVERIFIED` marks what the evidence does not establish.

**Citations.** Bracketed ids resolve by `id` in [`_evidence/2026-09-25.jsonl`](../_evidence/2026-09-25.jsonl),
or in [`_evidence/2026-09-26.jsonl`](../_evidence/2026-09-26.jsonl) for `sizing-` ids. Papers and
pages without a record are cited by arXiv number or name and listed under Sources with the day
they were read. "The maintainers' runs" means agent work on tool repositories in September 2026,
in which Claude-family agents implemented work packages and tickets, a fresh-context Claude reviewer
read each, and OpenAI models through Codex reviewed adversarially and read-only.

## Key findings

**RV1. A fresh-context second reader finds what the author, the suite and self-review missed.**
Maintainers would not merge about half of the test-passing agent pull requests they read
[sizing-horizon-19]; Anthropic's long-run guidance prefers separate fresh-context verifiers, which
"tend to outperform self-critique" [sizing-trend-32]. In the maintainers' runs every reviewed
ticket needed a repair, and a command-line tool whose tests all passed drew Critical and
Important findings from an outside review. Strong: independent measurement, convergent guidance and
own observations. (M, L, O) — §1.

**RV2. When the author and its reviewers share a model family, a reviewer from another family adds
signal.** Judges favour models similar to themselves and the mistakes of capable models grow
more alike (arXiv 2502.04313). In the maintainers' runs, work every Claude reviewer had approved
drew several blocking defect groups from a review by a model of another family; most reproduced and
none was refuted. Moderate: no run held task text and effort equal across families, so the family's
share of that is `UNVERIFIED`. (M, O) — §2.

**RV3. A finding is a claim and a GO is one reader's reading.** Each finding was reproduced
before fixing; one reviewer's claim was false and reviewers withdrew some of their own. A
read-only scan of a plan that review rounds had passed as GO found conflicts and ambiguities in it.
Moderate. (O, M) — §3.

**RV4. A decision-complete spec for a smaller implementer takes many rounds, and each correction
pass opens new gaps.** A large multi-file spec drew NO-GO from an adversarial reviewer in many
consecutive rounds before it drew GO, and it grew by about a quarter on the way; most of the packages
built from it then needed at least one fix round. Such a spec needs its rounds budgeted, or its
ambition cut, before one review is relied on (inference). Weak: two review loops in one project's
work. (O) — §4.

**RV5. Findings deferred as minor go stale and hide defects, and re-verification against the tree
settles each.** Of the deferred items triaged one by one, a few let a shipped check pass over a
defect, about a fifth had already been fixed and one needed the person; the ledgers' own counts,
line citations and "already fixed" notes were wrong in places. Weak: one project's ledgers. (O) — §5.

**RV6. A pass aimed only at whether accepted fixes landed finds what the fix round broke or
missed.** Fix rounds introduce
new defects: a fresh probe of one fix round closed most findings, one only partly, and found new
ones; in a command-line tool, re-reviews of a long fix loop kept finding new Important defects in the
code the round before had written. Weak. (O) — §6.

**RV7. A review pointed at one lens, with what to check stated, produced reproducible findings.**
Three scoped rounds (code against contract, tests against claims, documents against source) returned findings, all reproduced;
rule-guided code review recovered 98% of required custom findings against a 58.3% baseline
[openai-25]. Moderate. (O, M, vendor) — §7.

**RV8. Both a review's yield and its cost grow with the scope of the change.** One vendor's
reviewer found issues on 84% of pull requests over 1,000 changed lines and 31% under 50
[sizing-review-23]; in the maintainers' runs a fresh-context review of one ticket's diff took
67k–152k tokens and of one larger work package 149k–252k. Moderate. (M, vendor; O) — §7.

**RV9. On GitHub, only Copilot's review can count as a required approval, in preview; the
measured signal of review agents is low.** Pull requests reviewed only by code review agents merged
at 45.20% against 68.37% for human-only review, and 12 of 13 agents had average signal ratios below
60% (arXiv 2604.03196). Copilot's approval counts only where an admin turns it on; Claude Code's
managed review never approves or blocks; Codex's review is advisory. Moderate: one independent
study, and vendor pages that change often. (M, L) [as-of 2026-10-04] — §8.

## 1. When a second reader adds signal

A reader adds signal where no runnable check covers the risk: a test that stays green with the
behaviour broken ([testing.md](testing.md) K1), a sentence that disagrees with the code or a
sibling document, a decision that exists only in code, a change of meaning in rewritten text, or a
plan whose packages leave a writer unowned. Where a command can decide the question, the command is
the better reader.

**Outside evidence.**

- Maintainers reviewing 296 agent-written SWE-bench Verified pull requests would not merge roughly
  half of those that passed the tests, about 24 points below the grader after normalizing to a 68%
  baseline for the original human patches [sizing-horizon-19] (M). On 18 real issues, Claude 3.7
  Sonnet passed the maintainers' tests 38% of the time, but none of 15 reviewed pull requests was
  mergeable as it stood [sizing-horizon-18] (M).
- Anthropic's long-run guidance makes verification explicit: "Separate, fresh-context verifier
  subagents tend to outperform self-critique" [sizing-trend-32, forward-12]; the longer an agent
  works unattended, "the more an independent check matters before you count the work as done"
  [sizing-lab-19] (L). OpenAI asks developers to review long-running Codex work before changes or
  deployment, with Codex review as an additional reviewer, not a replacement [sizing-trend-43] (L).
  Cognition finds that extra agents work best contributing intelligence, such as a clean-context
  reviewer, while writes stay single-threaded [sizing-review-34] (L).
- Anthropic reports that before agent review 16% of its pull requests got substantive review
  comments, and 54% after [sizing-review-24] (L, a vendor about its own product).
- Where a check can be run, give the check: Claude Code's guidance names a fresh-context reviewer
  as one way among several to gate stopping, beside a test loop, a session goal and a stop hook
  [anthropic-20, deterministic-8] (L); "ask it to write a script that verifies", not to verify
  [latent-space-20] (A).

**What independent reviews found in the maintainers' runs** (O). Every finding was checked
against the source, and most were reproduced as a failing test, before it was counted. Reviews of a
tool's spec, of its work packages, of the built tool, of an uncommitted implementation and of
rewritten model-facing text each returned accepted findings that the author, the suite and the
author's own review had not found. Among them were a policy check that a replacement plan running
`/usr/bin/true` passed, a baseline entry that accepted any number of identical new findings, an
optional new check that silently weakened an accepted gate, and disagreements inside audited text
that an earlier reader had recorded as agreeing. Most reviews of rewrites to a writing standard found
blocking changes of meaning, though the reviews of the most-read skill found none. Running a tool on
its own repository found defects that no test had caught. The per-ticket record is in
[work-breakdown.md](work-breakdown.md) §3: in those runs reviewed tickets and larger packages were
mostly accepted only with fixes.

**Where a reader adds little.** On pull requests under 50 changed lines, Anthropic's agent reviewer
found something on 31%, about 0.5 issues each, against 84% and 7.5 issues over 1,000 lines
[sizing-review-23] (M, vendor). A one-sentence change that an existing test proves is a floor case
for a check, not for a reader ([work-breakdown.md](work-breakdown.md) P3).

## 2. Same family against another family (STABLE)

**The maintainers' runs** (O, one pair of families):

- **After same-family approval.** Every package of one milestone of a rewrite of a command-line tool had been
  approved by a fresh Claude Opus reviewer after its fix rounds. A read-only review by an OpenAI
  model at high effort then reported several blocking defect groups. An independent Claude verifier
  reproduced most, found one to be a decision already on record, and refuted none.
- **At a later milestone.** Three scoped reviews by the same OpenAI model at medium effort (code against
  contract, tests against claims, documents against source) returned findings that all reproduced
  before any was fixed.
- **A second tool.** A command-line tool built by Claude-family implementers and passed by
  Claude-family reviewers drew Critical and Important findings from the OpenAI model at high effort,
  and again from a second pass after further fixes (§1).
- **Misreads.** On re-review, same-family reviewers withdrew some of their own findings as
  misreads.
- **Where two families agree.** Two reviews of one rewrite of a specification document, by models of different
  families, agreed on its blocking change of meaning and differed on whether input only the person
  can give stops the run or is batched while other work continues.

**Why a shared family shares blind spots** (M):

- Across judges and models, "LLM-as-a-judge scores favor models similar to the judge", and "model
  mistakes are becoming more similar with increasing capabilities, pointing to risks from correlated
  failures" (Goel et al., Great Models Think Alike and this Undermines AI Oversight, arXiv
  2502.04313, 2025).
- GPT-4 and Llama 2 distinguish their own outputs from others' with non-trivial accuracy, and
  self-recognition correlates linearly with the strength of self-preference (Panickssery, Bowman and
  Feng, arXiv 2404.13076, 2024).
- Practitioners advise watching a judge for self-preference toward its own family [evals-12] (P).

**What this does not show.** The cross-family reviews were adversarial, read-only, run at high or
maximum effort and briefed with named lenses; the same-family reviews were task reviews of one
package each. No run held the task text and the effort equal and changed only the family, so how much
of the difference the family explains is `UNVERIFIED`. The pair is Claude authors and OpenAI
reviewers; the reverse direction was not run.

## 3. Reading what a review returns (STABLE)

- **Findings were reproduced before action.** Every outside finding on the first
  tool, the scoped cross-family findings and the second-pass findings on the second tool were
  reproduced before a fix (§1, §2). Checking against the source caught one false claim
  (that `gh` lacks dependency flags; it has them), and same-family reviewers withdrew some findings
  as their own misreads on re-review (O).
- **A GO establishes that one reader found no blocker.** A review round that returned GO on a plan
  said itself that the verdict did not establish implemented correctness, model benefit or readiness
  for wider use. A read-only scan of the same plan by a Claude model found conflicts and ambiguities;
  the load-bearing ones were confirmed: an acceptance test the plan named did not exist, and some of
  the spec's files belonged to no package (O).
- **Two readers given the same prompt overlap only in part.** Two fresh-context reviewers of an
  instruction-audit method, with the same prompt and read-only access, raised many points in
  a first round and in a second, and each round's points were only partly the same; some
  second-round points reversed first-round dispositions (O). In one rewrite only the edits both of two
  reviews proposed were applied, and each review's lone proposals were left out (O).
- **A persuasive summary is not evidence.** In a study of people working with an AI's
  recommendations, explanations "increased the chance that humans will accept the AI's
  recommendation, regardless of its correctness" (Bansal et al., CHI 2021, arXiv 2006.14779) (M).
  A review's confident prose is weighed like any other claim.
- **A reviewer's severity label is its own.** Items filed as minor included defects that let a
  shipped check pass (§5).

## 4. Review rounds on a large or decision-complete spec (STABLE)

**A spec written so a smaller model decides nothing** (O). A multi-file specification for a rewrite of a command-line tool was written so that a weaker model
could implement its plan without inventing a decision. An adversarial reviewer from another family
reviewed it in repeated rounds, and after each round a model applied the corrections.

- Early rounds returned NO-GO. Each correction pass closed the findings named and exposed or
  introduced new blocking ones: contradictions between files, writers no package owned, sequencing
  gaps, and acceptance commands that could not pass as written. A later round returned GO.
- The set grew by about a quarter between the early rounds and the GO.
- Each round sampled rows that described existing code against the source; in each early round a
  share of the sampled rows was wrong.
- After the GO, the scan in §3 found conflicts and ambiguities in the plan.
- Built from that plan, one implementer at a time worked its packages from task texts that pointed into
  it, and a fresh reviewer read each result: most went back for at least one fix round, and one needed
  several, each closing one more way its grader could be fooled
  ([evaluations.md](https://github.com/rajasdevel/outcomebound/blob/main/docs/evaluations.md), lessons on graders); the cross-family review of §2 read the
  result.

**A review of a whole tree before a release** (O). Repeated adversarial loops, each
given the fixes since the last loop and the findings already accepted, returned NOT-READY with new
blocking findings in each early loop and READY only in the last.

**What follows (inference).** A plan reviewed to GO did not make first-pass implementation right,
and a spec that tries to settle every decision in prose for a weaker reader kept growing and kept
drawing blockers. A budget of rounds set before a loop starts, with a rule for when the budget runs
out, and a sample of the spec's claims about existing code checked against the source each round,
address that; so does the alternative the sizing evidence favours, charting only as far as
knowledge is stable and letting the implementer's plan carry the rest
([work-breakdown.md](work-breakdown.md) P7). Two loops in the maintainers'
work are the whole evidence; no source compares a spec reviewed to convergence with a shorter
spec and checkpoints inside the work.

## 5. Deferred findings (STABLE)

In the maintainers' runs, findings that reviews marked "minor (deferred)" were kept as prose: two
progress ledgers held dozens of such lines with no id and no status (O).

- **Triage against the current source.** Split into items for two tools
  and decided one by one against the source, by symbol: a few were not minor, each letting a shipped
  check pass over a defect (a destructive-SQL scanner split a statement at a `;` inside a quoted
  identifier, so `ALTER TABLE "t;u" DROP COLUMN x;` read clean; a list parameter rendered by joining
  with commas let one recorded acceptance stand for a different change); one was a question of intent
  for the person; about a fifth had already been fixed by later work; others became fixes; and the
  rest were kept or dropped with a reason.
- **The ledgers misled.** Their own counts did not match a mechanical count; cited line numbers had
  moved, or never resolved even at the commit that wrote them; two bullets from different review
  rounds were one defect, and two that read alike were two mechanisms; two items that said no test
  caught a change were caught by a test the ledger did not name. A second ledger had, in some
  packages, a triage note that an item was already fixed, or that a name no longer appeared, which
  was wrong when checked.
- **Re-verify before drafting.** Drafters who re-checked findings against the tree before
  turning them into tickets dropped some: one intended behaviour, one already fixed, one already
  ticketed.

A deferred finding therefore names its subject by path and symbol, says which verdict it could
change, and is re-verified against the tree before it becomes work or is closed. One that could let
a check pass over a broken subject, or let a report state something untrue, is not a minor. Turning
every later finding into its own ticket is the other failure: [work-breakdown.md](work-breakdown.md)
§3 records a batch of such tickets whose median diff was small.

## 6. Verifying that accepted fixes landed (STABLE)

- **A fix round needs its own reading.** After the outside findings on the first tool were
  fixed, a reader with fresh context re-ran the review's counter-examples as probes rather than
  trusting the new tests: most findings closed, one closed only partly, and new
  defects appeared, among them a page flag of `null` read as "no further page" (O).
- **Fix code is new code.** In the second tool the fix loop ran past its planned cap of
  rounds because each re-review found a new Important defect in the code the previous round had
  just written (O). One evaluation grader failed open in five ways before one filesystem walk held
  ([evaluations.md](https://github.com/rajasdevel/outcomebound/blob/main/docs/evaluations.md) E16).
- **A record of coverage is not a reading of meaning.** Rewrites that carried a sentence-by-sentence
  record of every earlier sentence still changed meaning where the record said "carried": a
  permission became a duty, a gate narrowed to one row of its table, a parenthesis created a new
  stop, a done-when became one no command could meet (O). A rewrite is best reviewed against its
  before text ([writing-for-models.md](writing-for-models.md) §8).
For each accepted finding, the pass described lists every place its claim appears, checks each one,
and re-runs the reviewer's own reproduction against the fixed tree.

## 7. Setting up a review

- **Fresh context, read-only, its own copy.** Every review above read with no memory of the work,
  in a worktree or detached copy, and changed nothing. A reviewer that must run checks needs a
  writable disposable copy: reviews run in Codex's read-only sandbox could not run the project's test
  suite or create temporary fixtures, so their acceptance re-runs read `UNVERIFIED` and their
  findings rested on reading the source and in-memory probes (O; the harness details are in
  [cross-harness.md](../harnesses/cross-harness.md#3-loading-harness-by-harness)).
- **One lens a round, and the question asked.** The three scoped rounds of §2 split the work by
  lens and every finding reproduced. OpenAI's guidance for Codex code-review rules: start with "a
  consequential, non-obvious invariant", scope rules to the code they govern, and remove guidance
  that keeps producing noise; rule-guided review recovered 98% of required custom findings against
  58.3% without [openai-25] (M, vendor; L). In human review, stating the type of feedback needed went
  with 64–72% higher merge odds across 80,000 pull requests (arXiv 2602.14611, correlational) (M).
- **The reviewer gets the before text and the ground truth.** A rewrite is read against what it
  replaced; a review of figures is given the source the figures come from (inference).
- **Effort is not a dial for quality.** On one vendor's code-review benchmark for Claude Opus 5.5,
  turning effort up "did not consistently produce a better review" [claude-f23] (M, vendor, one
  model).
- **Diff size.** For one small model (Claude Haiku 4.5), review F1 fell from 0.657 on diffs under 10
  lines to 0.043 over 150 lines [sizing-review-22] (M, 150 samples); a reviewable landing unit is a
  few hundred lines at most ([work-breakdown.md](work-breakdown.md) F8).

**What reviews and the fix rounds they send cost** (O, from recorded token counts unless a row says
otherwise):

| Review | Model | Tokens |
| --- | --- | --- |
| Review of one ticket's diff, fresh context | a larger Claude model | 67k–152k ([work-breakdown.md](work-breakdown.md) §3) |
| Review of one larger work package | a larger Claude model | 149k–252k |
| A fix round handed to a fresh delegate, which must re-read the work first | a larger Claude model | about 134k (A: one run whose record was not kept) |

## 8. AI reviewers as a merge gate (VOLATILE) [as-of 2026-10-04]

**Measured signal** (M). Chowdhury et al., From Industry Claims to Empirical Reality: An Empirical
Study of Code Review Agents in Pull Requests (MSR 2026, arXiv 2604.03196, submitted 2026-04-03),
studied 3,109 unique pull requests in commented review state, taken from 19,450 in the AIDev
dataset. Pull requests reviewed only by code review agents merged at 45.20%, 23.17 percentage
points below human-only pull requests (68.37%), and "12 of 13 CRAs exhibit average signal ratios
below 60%". The authors conclude that review agents "should augment rather than replace human
reviewers". A merge rate is an outcome of the whole pull request, so the study does not separate the
reviewer's effect from which pull requests got which reviewer (inference).

**Which reviewer's approval can count** (L, each page read 2026-10-04):

| Reviewer | Can its review satisfy a required approval? | What the vendor documents |
| --- | --- | --- |
| GitHub Copilot code review | Yes, in public preview since 2026-09-01; off by default | An admin turns on "Allow Copilot approvals to count toward merge requirements". Optional file-path globs (up to 15): an approval counts only where every changed file matches one. New commits dismiss the approval. Plans: Copilot Pro, Pro+, Max, Business and Enterprise. Each review costs AI credits plus GitHub Actions minutes |
| Claude Code Code Review (managed) | No | Findings "don't approve or block your PR"; the check run "always completes with a neutral conclusion". A project that wants a gate reads the severity counts from the check run's output in its own CI. Research preview for Team and Enterprise; a review averages $15-25 |
| Codex cloud code review | Advisory; whether its review can count as an approving review is `UNVERIFIED` | It "posts a standard GitHub code review" and flags only P0 and P1 issues; its rules "don't replace tests, branch protections, or required approvals" |

**Where the reviewer reads its instructions.** Copilot code review reads repository custom
instructions, agent instructions and skills from the pull request's head branch, not the base
branch (L). So a pull request can change the instructions that its own reviewer follows, and an
approval that counts is then shaped by the change it approves (inference). File-path globs that
leave out the instruction and gate files keep those changes for a human approver (inference).
Claude's page does not say from which branch it reads `CLAUDE.md` and `REVIEW.md`; for Codex the
branch is `UNVERIFIED`.

A pull request's author cannot approve it on GitHub, which bears on who else can approve when
agents work under the maintainer's account: see
[agent-authorization.md](agent-authorization.md) §9.

## What the evidence supports (inference)

These points are this reference's reading of the findings above. They are not orders.

1. A check the agent can run decides what it can; a second reader adds signal where none can:
   meaning, agreement between documents and code, tests that pass with the behaviour broken, plans
   with gaps (RV1).
2. An independent reader has fresh context, is read-only, works on its own copy, and has a writable
   disposable copy if it must run checks (§7).
3. Where the author and its reviewers share one model family, a reviewer from another family at the
   points that matter most (a milestone, a release, a spec before it is built) added signal (RV2).
4. One lens per review, and the question it must answer, with the before text or the source of
   truth beside it, gave reproducible findings (RV7).
5. A finding is reproduced before it is fixed; a GO is one reader finding no blocker; a severity
   label is the reviewer's opinion (RV3).
6. A spec review needs its rounds budgeted before it starts and the spec's claims about existing
   code sampled each round; a shorter spec with checkpoints inside the work is the alternative
   (RV4).
7. A deferred finding keeps its path, symbol and the verdict it could change, and is re-verified
   against the tree before it is decided or drafted (RV5).
8. After a fix round, a pass that checks only whether each accepted fix landed, everywhere its claim
   appears, with the reviewer's reproductions re-run, finds what the round missed (RV6).
9. Review effort scales with the change: a short focused review for a small change, a broad
   adversarial one before a release (RV8).
10. An AI review that counts as a required approval is, on the measured signal, a weak second
    party; on GitHub only Copilot's can count, and path globs can keep gate and instruction files
    for a human (RV9).

## Limits and open questions

- The own-run evidence is one set of repositories, September 2026, Claude-family authors and same-family
  reviewers against OpenAI reviewers through Codex.
- No source compares same-family with cross-family review of code at equal brief and effort, or a
  second same-family reviewer with a first cross-family one.
- Yields count reproduced findings, not escaped defects: what every review missed is known only
  where a later review found it.
- The outside measurements of review effectiveness predate agents or concern human maintainers
  ([work-breakdown.md](work-breakdown.md) F8); the measured agent-reviewer results are a vendor's
  own (Anthropic, CodeRabbit, OpenAI) or small (150 samples); the one independent study of review
  agents in pull requests (arXiv 2604.03196) measures merge rates and signal ratios, not escaped
  defects.
- Open: how many rounds a spec should get before its ambition is cut; whether a fix-landing pass
  catches as much as a full re-review at lower cost; whether agreement between two reviews of
  different families predicts a finding that holds.

## Sources

Evidence records: [sizing-horizon-18], [sizing-horizon-19], [sizing-trend-32], [forward-12],
[sizing-lab-19], [sizing-trend-43], [sizing-review-34], [sizing-review-24], [sizing-review-23],
[sizing-review-22], [anthropic-20], [deterministic-8], [latent-space-20], [evals-12], [openai-25],
[claude-f23].

Papers read 2026-10-01: Goel et al., Great Models Think Alike and this Undermines AI Oversight,
arXiv 2502.04313 (2025-02-06, revised 2025-06-12); Panickssery, Bowman and Feng, LLM Evaluators
Recognize and Favor Their Own Generations, arXiv 2404.13076 (2024-04-15); Bansal et al., Does the
Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance, CHI 2021,
arXiv 2006.14779. Cited from [work-breakdown.md](work-breakdown.md): arXiv 2602.14611.

Read 2026-10-04 (§8): Chowdhury et al., From Industry Claims to Empirical Reality: An Empirical
Study of Code Review Agents in Pull Requests, MSR 2026, <https://arxiv.org/abs/2604.03196>
(2026-04-03); GitHub changelog, Copilot code review can now approve pull requests (2026-09-01)
<https://github.blog/changelog/2026-09-01-copilot-code-review-can-now-approve-pull-requests>;
GitHub docs, configure code review
<https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-code-review>
and Copilot code review <https://docs.github.com/en/copilot/concepts/agents/code-review>; Claude
Code, Code Review <https://code.claude.com/docs/en/code-review>; Codex, GitHub integration
<https://learn.chatgpt.com/docs/third-party/github>.

The (O) claims rest on the maintainers' unpublished observations of September 2026.
