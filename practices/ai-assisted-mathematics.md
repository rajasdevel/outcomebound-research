---
last_checked: 2026-11-24
volatility: MONITOR (proof status, revised statements, and independent verification)
sources:
  - https://www.nature.com/articles/s41586-023-06924-6 (read 2026-11-24)
  - https://www.erdosproblems.com/304 (read 2026-11-24)
  - https://www.erdosproblems.com/static/UnitFractions.pdf (read 2026-11-24)
  - https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae (read 2026-11-24)
  - https://github.com/openai/math/blob/main/README.md (read 2026-11-24)
  - https://github.com/openai/math/blob/main/history.md (read 2026-11-24)
  - https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf (read 2026-11-24)
  - https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/003.md (read 2026-11-24)
  - https://alpo.ge/remark.pdf (read 2026-11-24)
  - https://x.com/ElliotGlazer/status/2123792743503933774 (read 2026-11-24 via X syndication)
  - https://1stproof.org/third-batch.html (read 2026-11-24 and 2026-11-25)
  - https://1stproof.org/third-batch-press-release.html (read 2026-11-24 and 2026-11-25)
  - https://arxiv.org/html/2610.08144v1 (read 2026-11-24)
  - https://openai.com/index/navier-stokes-solution/ (read 2026-11-24)
  - https://github.com/openai/NavierStokesAndEuler/blob/f9e8bc5b38b6e212696e8a30e3e91517af887bbd/NavierStokes/SmoothFamilyTorusInverse.lean#L1059-L1080 (read 2026-11-24)
  - https://www.anthropic.com/research/formal-verification (read 2026-11-24 and 2026-11-25)
---

# AI-assisted mathematics

A model can suggest a construction, an analogy, or a proof. Each output needs an acceptance
statement that says exactly what the evidence establishes. This practice is for people who design
these searches or review their results.

Sources were read on 2026-11-24. **M** marks a reported measurement, including a computed
construction or a graded benchmark. **L** marks a lab's report or documentation. **A** marks an
author's or observer's account. **Inference** marks a practice drawn from the cases. Proof replays
and independent mathematical validation are outside the evidence of this reading.

## Cases and what they establish

- **FunSearch — published construction (M).** The Nature paper reports a set of 512 points in
  eight dimensions over the field with three elements, with no three distinct points on a line.
  Researchers supplied the greedy construction and evaluator. The model proposed priority
  functions, and the researchers simplified the winning program into an explicit construction.
  They also used symmetries in generated programs to guide a further search, which raised the
  reported lower bound on cap set capacity to 2.2202. A check of the 512 points can establish a
  lower bound. An optimality claim would also need a matching upper bound. [Nature paper, Figures
  4–5](https://www.nature.com/articles/s41586-023-06924-6)
- **Erdős problem #304 — public proof and human exposition (A).** The problem page records the
  result that every rational number `a/b` between zero and one is a sum of at most
  `O(log log b)` distinct unit fractions. The known lower bound gives the order of growth for
  the worst numerator. Thomas Bloom and Wouter van Doorn report that OpenAI's proofs had Lean
  formalizations. The two authors extracted a shorter argument from another result in the same
  manuscript, simplified it, and wrote their own exposition. They used ChatGPT Astra early to
  help explain the source and report that they left the redundant longer argument unread in
  detail. The exposition gives a human-checkable route to the result. Its scope is the arguments
  it presents. [Problem page](https://www.erdosproblems.com/304) ·
  [Exposition, Theorem 1 and §6](https://www.erdosproblems.com/static/UnitFractions.pdf)
- **OpenAI's October collection — selected manuscripts with mixed verification (L).** The
  October 30 snapshot lists 721 manuscripts in 373 families from an evaluation that posed
  approximately 4,000 problems to an unreleased model. OpenAI reports about three hours of
  thinking compute per result on average for its usual procedure and lists exceptions. The lab
  grouped and selected output for significance and edited the separate `Re(s) > 11/12` writeup
  for readability. The catalogue read on November 24 lists 722 manuscripts in 374 families.
  The release history records withdrawals and repairs. Manuscripts, families,
  and attempted problems are different units, and the reported compute per result does not
  estimate total selection cost. [October snapshot](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae) ·
  [Catalogue](https://github.com/openai/math/blob/main/README.md) ·
  [Release history](https://github.com/openai/math/blob/main/history.md)
- **Quasi-Riemann hypothesis — manuscript claim with a scoped Lean artifact (L).** The
  September 30 manuscript in that collection claims a zero-free region `Re(s) > 7/8` for
  all Dirichlet L-functions, including the Riemann zeta function, and for finite-order Hecke
  L-functions over `Q(√−3)`, with the principal pole at `s = 1` allowed. This fixed
  half-plane leaves open where zeros outside it lie. RH and the Dirichlet form of GRH require
  the nontrivial zeros to lie on `Re(s) = 1/2`. The lab's Lean notes list formalized versions
  of the headline bounds and exclude the manuscript's later applications. The notes describe
  a separate result that excludes real zeros within a logarithmic distance of 1, with an
  unspecified constant. The gap result alone leaves real zeros elsewhere possible. Independent
  replay and expert validation of the manuscript are unverified here. [Manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf) ·
  [Lean scope](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/003.md)
- **Alpöge's RH and GRH announcement — independent proof validation unverified (A).** Levent
  Alpöge announced proposed proofs of RH and GRH with Claude and released a Lean archive.
  He describes bringing together two ideas in a simpler setting and directing the work
  toward an analogous setting. He credits Claude with a step in the resulting argument and
  planned a readable account. On November 20, Elliot Glazer
  reported that the formal statement in the release was GRH and that compilation was still in
  progress at the time of the post. This corroborates the scope of the announcement.
  [Alpöge's statement](https://alpo.ge/remark.pdf) ·
  [Glazer's report](https://x.com/ElliotGlazer/status/2123792743503933774)
- **First Proof, third batch — held-out research evaluation (M).** Mathematicians set ten
  unpublished problems with known human solutions of at most 12 pages. Five systems each had
  one submission opportunity per problem, with a 24-hour window per system and no human input
  during testing. About 30 expert referees graded anonymized answers for correctness, exposition,
  and attribution. Organizers report 9/10 correct for ProofCouncil, a harness that uses GPT-6
  Astra alongside other models, and 7/10 for a direct GPT-6 Astra run. Reported costs were
  $1,888 and $36 respectively. The scores describe these systems on this
  batch. The problems already had solutions, and a correct answer could still score poorly for
  exposition or attribution. [Batch procedure and artifacts](https://1stproof.org/third-batch.html) ·
  [Scores and costs](https://1stproof.org/third-batch-press-release.html)
- **Navier–Stokes — lab claim and independent translation critique (L, A).** OpenAI reported
  forced breakdown results for three-dimensional flow in whole space and on the periodic torus,
  the C and D alternatives in the Clay problem statement. The lab chose problem variants and
  allocated search resources. It released a written proof and Lean code. The October critique
  compared the written argument with a pinned version of the code. In one example the written
  estimate uses derivatives through order `m + 4`, and the cited Lean estimate needs derivatives
  through order `m + 5`. The critique also describes a difference in a pressure-flux argument.
  Its authors limit their conclusions to fidelity of the translation. The correctness of the
  written proof requires its own mathematical review. [Lab announcement](https://openai.com/index/navier-stokes-solution/) ·
  [Pinned Lean estimate](https://github.com/openai/NavierStokesAndEuler/blob/f9e8bc5b38b6e212696e8a30e3e91517af887bbd/NavierStokes/SmoothFamilyTorusInverse.lean#L1059-L1080) ·
  [Critique, §3](https://arxiv.org/html/2610.08144v1)
- **Anthropic and Theorem — reported Rocq checks on selected binaries (L, M).** The collaborators
  report proving normal exit without memory-safety errors or failed assertions for 239
  developer-written fuzz entry points in 123 OSS-Fuzz libraries. The result covers inputs
  under 64 MB and every modeled Linux response and memory layout, for single-threaded static
  RISC-V binaries linked to musl libc, with a fixed memory budget. The report says Claude
  patched bugs it found before it proved the property. The teams built the verification
  pipeline around the existing entry points. Claude wrote proof code, and the Rocq kernel
  checked it against the specification. The guarantee depends
  on the exact theorem and binary, the RISC-V and Linux models, and the proof checker and its
  execution environment. The report releases a subset of the proofs. Coverage of other entry
  points, architectures, and properties falls outside the claim. [Anthropic and Theorem report](https://www.anthropic.com/research/formal-verification)

## Workflow

1. **An exact acceptance statement.** A statement records the object, quantifiers, hypotheses,
   and conclusion before search. For a construction, it gives the constraints and the value to
   improve. For a theorem or software proof, it also gives the formal statement and the model of
   the system it covers. A reviewer checks whether the formal statement means what the intended
   claim says, including units, boundary cases, and any weaker intermediate target. (Inference
   from [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) and the
   [translation critique](https://arxiv.org/html/2610.08144v1).)
2. **Toy cases and a separate evaluator.** Small cases with known answers can check the search
   setup and make useful patterns visible. A deliberately invalid candidate tests rejection.
   Where validity is cheap to decide, the model can propose a small part of a construction and
   a fixed evaluator can reject invalid output before scoring value. For a proposed proof,
   a toy example can test an analogy or expose a false lemma. The general step still needs proof.
   (Inference from [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) and
   [Alpöge's account](https://alpo.ge/remark.pdf).)
3. **Replay and assumptions.** A retained result includes the candidate, a checker and its inputs
   or the proof source, and pinned versions of the toolchain and dependencies. Independent replay
   records the exact checked statement, any admitted steps, the axioms used by the theorem and
   its dependencies, and the build result. A subject expert checks the statement against the
   intended claim. If validation also covers a written proof, that review traces its major
   steps to the formal argument or checks the written steps directly. (Inference from the
   [translation critique](https://arxiv.org/html/2610.08144v1) and the
   [Rocq case](https://www.anthropic.com/research/formal-verification).)
4. **Explanation, sources, and cost.** A readable account identifies the key idea, the lemmas
   it depends on, and which steps come from prior work, human contributors, or model output.
   A run record includes attempted problems, candidate attempts including discarded ones, how
   winners were selected, compute and elapsed time, and human review effort. For an evaluation,
   keeping correctness, exposition, and attribution scores distinct preserves what each score
   measures. (Inference from the [unit-fraction exposition](https://www.erdosproblems.com/static/UnitFractions.pdf),
   [October snapshot](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae),
   and [First Proof](https://1stproof.org/third-batch.html).)

## Limits and open questions

These cases support transfer to tasks with an exact specification and affordable checks. Where
evaluation requires expensive expert judgment, the cost of selecting and validating results can
dominate the cost of generating them. A construction check covers its witness, a benchmark score
covers its batch, and a proof checker covers the theorem it checks under its assumptions.
Each new domain needs evidence for its own acceptance statement. Recheck the cases when a
manuscript or formal statement changes, an independent referee or replay publishes a result, or a
new held-out batch changes the evidence about performance and cost. (Inference from
[FunSearch](https://www.nature.com/articles/s41586-023-06924-6),
[First Proof](https://1stproof.org/third-batch.html), and the
[translation critique](https://arxiv.org/html/2610.08144v1).)
