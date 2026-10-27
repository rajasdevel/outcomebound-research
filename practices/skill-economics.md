---
last_checked: 2026-10-27
volatility: VOLATILE (§1 listing budgets, settings and commands; §2 multipliers) / MONITOR (§3 selection evidence, §5 measurement tools) / STABLE (§2 arithmetic, §4 structure rules)
sources:
  - https://code.claude.com/docs/en/skills
  - https://code.claude.com/docs/en/memory
  - https://code.claude.com/docs/en/costs
  - https://code.claude.com/docs/en/prompt-caching
  - https://learn.chatgpt.com/docs/build-skills
  - https://learn.chatgpt.com/docs/agent-configuration/agents-md
  - https://developers.openai.com/api/docs/guides/prompt-caching
  - https://developers.openai.com/api/docs/guides/function-calling
  - https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
  - https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool
  - https://www.anthropic.com/engineering/advanced-tool-use
  - https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
  - https://agentskills.io/specification
  - https://agentskills.io/skill-creation/optimizing-descriptions
  - https://agentskills.io/skill-creation/evaluating-skills
  - https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
  - https://cursor.com/blog/dynamic-context-discovery
  - https://arxiv.org/abs/2602.11988
  - https://arxiv.org/html/2505.03275v1
  - https://arxiv.org/abs/2603.22455
  - https://arxiv.org/abs/2603.02176
  - https://arxiv.org/abs/2607.06283
---

# Skill economics: what always-loaded text and skills cost, and what cuts the cost

What a token of always-loaded guidance costs over a session, what drives that cost, and what
published evidence says lowers it without lowering task success.

Re-check when a harness changes its listing budget or its loading rules, when a provider changes
cache prices or lifetimes, or when a new study measures skill selection; in any case by 2026-11-27
(the VOLATILE sections).

This document is for anyone who sizes a skill set, an `AGENTS.md` or a `CLAUDE.md`, and wants the
cost side of the trade-off. It adds to, and does not repeat, three documents: what helps and harms
in a skill, and the SkillsBench and Vercel figures, are in [skills.md](skills.md); the provider
cache rules, minimums and prices are in [prompt-caching.md](prompt-caching.md); the loading limits
of each harness are in [cross-harness.md](../harnesses/cross-harness.md#3-loading-harness-by-harness),
[codex.md](../harnesses/codex.md#3-skills) and [claude-code.md](../harnesses/claude-code.md).
Evidence classes are those of [the conventions](../CONVENTIONS.md): M measured, L lab or vendor
documentation, P practitioner consensus, A anecdote. Every source was read on 2026-10-27 unless a
claim says otherwise. Claims cite their source by link. "Computed" marks arithmetic done here from
published multipliers, not a measurement.

## Key findings

1. **Always-loaded text is billed on every model call, but at the cached rate once the prefix is
   warm.** A harness re-sends the whole context on each call; Claude Code says so for the system
   prompt, project context and every earlier message. With a cache, the repeat cost of a stable
   prefix is a fraction (0.1 times, or less, of the input price on the lines checked) of its first
   cost. The cost that remains is the write, every rebuild after a cache break, and the context
   space the text occupies. L [Claude Code caching](https://code.claude.com/docs/en/prompt-caching),
   [OpenAI caching](https://developers.openai.com/api/docs/guides/prompt-caching).
2. **A skill's body costs about the same as always-loaded text once invoked early; the saving from
   on-demand loading is the sessions in which the skill is never invoked.** The body stays in the
   conversation on later calls and is not re-read from disk. Computed from the multipliers (§2).
3. **The listing of names and descriptions is the always-loaded part of every skill, and every
   harness caps it.** Claude Code sizes the listing at 1% of the context window and drops
   descriptions of the least-used skills first; Codex uses 2% of the window (8,000 characters if the
   window is unknown), shortens descriptions first, and may omit skills. Both let the user change
   the budget. L (§1).
4. **Selection accuracy falls as the catalog grows, and the makers' numbers put the knee between
   20 and 50 items.** OpenAI suggests fewer than 20 functions at the start of a turn; Anthropic says
   selection degrades past 30 to 50 tools. One paper's stress test found failures dominating beyond
   about 100 candidates. L, M (§3).
5. **Deferring detail until it is needed cut tokens 46.9% (one vendor A/B test, tool descriptions)
   and about 85% (vendor figure, tool definitions) without a reported loss.** The first reports no
   accuracy result; the second reports accuracy gains on its own evals. L, M-vendor (§3, §4).
6. **A trigger description is tested with labelled should-trigger and should-not-trigger prompts,
   repeated, with a held-out split; near-miss negatives are the informative ones.** No source found
   measures the effect of an explicit "not for X" clause. L; the clause's effect is `UNVERIFIED` (§3).
7. **A short always-loaded file is cheaper and no worse; a long one raised cost over 20% on average
   with no general success gain.** One study of repository context files; the makers of the two
   harnesses checked set the size target at 200 lines (Claude Code) and a 32 KiB cap (Codex). M, L
   (§4).
8. **A script's output, not its text, enters the context.** A bundled script that is run adds only
   what it prints; a reference file adds its text when read. L (§4).
9. **Both cost and use can be attributed from the harness.** Claude Code reports the listing's size
   in `/context`, a per-skill cost and use report in `/skill-doctor`, and cache hits and misses in
   `/usage`; the skill-evaluation guidance stores tokens and time per run beside the pass rate, with
   and without the skill. L (§5).

## 1. What each harness loads, and what caps it (VOLATILE)

Read 2026-10-27. Only differences from, and additions to, the existing harness documents are listed.

**Claude Code** ([skills](https://code.claude.com/docs/en/skills),
[memory](https://code.claude.com/docs/en/memory)) (L):

- The listing always holds every skill's name. When it overflows its character budget, descriptions
  are dropped, least-invoked skills first. The budget scales at 1% of the model's context window.
  `skillListingBudgetFraction` (for example `0.02`) or the `SLASH_COMMAND_TOOL_CHAR_BUDGET`
  environment variable (a fixed character count) raises it; `skillListingMaxDescChars` changes the
  1,536-character cap on each entry's combined `description` and `when_to_use`.
- `skillOverrides` sets a skill to `"on"`, `"name-only"` (listed without a description),
  `"user-invocable-only"` or `"off"`. `disable-model-invocation: true` removes the description from
  context entirely; the skill is then run only by the user.
- The `Skills` row in `/context` reports the listing after the budget is applied; before v2.1.196 it
  counted every description in full and could read several times larger than the budget.
- An invoked skill enters the conversation once and stays; the file is not re-read on later turns.
  Invoking it again with identical rendered content adds only a short note. After compaction, the
  most recent invocation of each skill is re-attached, first 5,000 tokens each, 25,000 in all.
- Supporting files and scripts are not loaded up front; a script is executed, not loaded.
- `CLAUDE.md` is read at session start and delivered as a user message after the system prompt, not as
  part of it. The docs set a target under 200 lines per file and say longer files consume more context
  and reduce adherence. Subdirectory `CLAUDE.md` files and `paths:`-scoped rules load only when
  Claude reads or edits a matching file; the root file is re-read from disk after `/compact`. An
  `AGENTS.md` is read only when no `CLAUDE.md` exists in or above the working directory, unless the
  project-instructions setting is changed (v2.1.277 or later).
- The listing's position in the cache layers (system prompt, project context, conversation) is not
  stated on the pages read. `UNVERIFIED`.

**Codex** ([skills](https://learn.chatgpt.com/docs/build-skills),
[AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)) (L):

- At start the list carries each skill's name, description and file path; the full `SKILL.md` loads
  when the model decides to use the skill. The list takes at most 2% of the context window, or 8,000
  characters when the window size is unknown. `skills.max_context_tokens` raises the budget, up to
  10,000 tokens. With many skills, descriptions are shortened first; a large set may lose entries
  from the list, with a warning.
- `allow_implicit_invocation = false` stops the model from using a skill unprompted; explicit
  `$skill` use still works. The page does not say whether such a skill is left out of the list.
  `UNVERIFIED`.
- The instruction chain from `AGENTS.md` is built once per run, concatenated from the global file
  down to the working directory, capped by `project_doc_max_bytes` (32 KiB). The page does not say
  whether the text is re-sent each call; model APIs re-send the whole prefix each call (§2).

**Agent Skills standard** ([specification](https://agentskills.io/specification)) (L): about 100
tokens of metadata per skill at startup, instructions recommended under 5,000 tokens, `SKILL.md`
under 500 lines, resources loaded as needed, references one level deep from `SKILL.md`, and a
reference file kept small because "smaller files mean less use of context".

**Not re-checked in this pass:** the listing rules of the other harnesses in
[cross-harness.md](../harnesses/cross-harness.md#6-skills-discovery-and-listing) §6 (ZCode, Gemini
CLI, Antigravity, Grok Build and others).

## 2. What a token of always-loaded text costs (VOLATILE multipliers, STABLE arithmetic)

**The mechanism.** Each model call carries the whole context again. Claude Code states it plainly:
it re-sends the system prompt, the project context, every earlier message and tool result, and the
new message, and the provider caches the unchanged prefix ([Claude Code caching](https://code.claude.com/docs/en/prompt-caching)). L. Cache
rules, minimums, lifetimes and prices by provider are in [prompt-caching.md](prompt-caching.md);
the multipliers used below are from there and from
[OpenAI's caching guide](https://developers.openai.com/api/docs/guides/prompt-caching) (a 30-minute
write at 1.25 times the input price, reads at about 0.1 times, 0.05 times on the newest tiers).

**Computed cost of a prefix of S tokens over N calls**, in multiples of S times the plain input
price, with write multiplier w and read multiplier r:

| Case | Cost | Example, w = 1.25, r = 0.1, N = 40 |
| --- | --- | --- |
| Cache never hits | N | 40 |
| Warm for the whole session | w + r(N − 1) | 5.15 (12.9% of uncached) |
| Each extra rebuild (compaction, model switch, idle past lifetime, edited prefix) | adds w − r | +1.15 each |
| Cache hits worth having | from the second call (w + r < 2) | |

Two consequences follow, both computed:

- A stable always-loaded prefix is cheap per call but not free, and its cost is dominated by how
  often the cache breaks, not by its length alone. A prefix that changes every call costs the write
  premium each time and more than no cache at the OpenAI write rate (the premium is on top of the
  input price) [prompt-caching.md](prompt-caching.md).
- A skill body of B tokens first read at call k costs about B(w + r(N − k)), because it is appended
  once and then read from cache. For B = 3,000, k = 5 and N = 40 that is about 14,250 token-price
  units; the same 3,000 tokens always loaded cost about 15,450. Loading on demand saves little when
  the skill is invoked early in most sessions, and saves nearly the whole cost when it is rarely
  invoked. The break-even is the share of sessions that invoke the skill, which only a count of
  invocations gives (§5).

**What the price does not include.**

- Caching does not shorten the context: cached tokens still occupy the window. Anthropic frames the
  window as a finite attention budget and calls recall loss as the window fills "context rot"
  ([context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). L.
- A listing entry is paid on every call whether or not the skill is used. Claude Code's own cost page
  says each listed skill adds to context every turn [skills](https://code.claude.com/docs/en/skills). L.
- Claude Code's cache lifetime defaults to one hour for the main conversation on a subscription within
  plan usage, and five minutes on an API key, a cloud provider or usage credits; subagents, workflows,
  compaction and other helper requests default to five minutes, so a subagent pays the
  write on its own first call [Claude Code caching](https://code.claude.com/docs/en/prompt-caching). L.
- Skill and plugin additions, plan mode and output-style changes are appended as conversation
  messages and keep the cache. Switching model (including through a skill's `model` frontmatter),
  fast mode, an MCP server change when tool definitions load up front, compaction and an upgrade
  rebuild it. Editing `CLAUDE.md` mid-session does not break the cache and does not apply until
  `/clear`, `/compact` or a restart (same page). L.
- Agent teams use roughly 7 times the tokens of a standard session when teammates run in plan mode,
  because each has its own context; teammates load `CLAUDE.md`, MCP servers and skills on their own
  [costs](https://code.claude.com/docs/en/costs). L. Every always-loaded token is paid once per
  agent.

## 3. How a model chooses a skill or tool (MONITOR)

- **The description is the whole trigger.** The Agent Skills guidance says the agent sees only name
  and description until it decides to load a skill, and recommends imperative wording ("use this
  skill when"), user intent rather than implementation, listing contexts the user may not name, and
  a few sentences, with a hard limit of 1,024 characters
  ([optimizing descriptions](https://agentskills.io/skill-creation/optimizing-descriptions)). L.
  Codex asks for the key use case and trigger words at the front so matching survives shortening
  ([Codex skills](https://learn.chatgpt.com/docs/build-skills)). L. Anthropic asks for third-person
  text stating what the skill does and when to use it, and says the model picks from potentially 100
  or more skills by it ([best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)). L.
- **Agents often skip a skill they could do without.** The Agent Skills guidance notes that agents
  mostly consult a skill for work beyond what they can do alone, so a simple request may not trigger
  a matching skill (L). In the Vercel eval a default skill went unused in 56% of cases (M, vendor;
  [skills.md](skills.md) §2 holds the full figures). Whether this changes with newer models is
  open.
- **Catalog size.** OpenAI: aim for fewer than 20 functions at the start of a turn, a soft
  suggestion to test against the application's own accuracy
  ([function calling](https://developers.openai.com/api/docs/guides/function-calling)). L. Anthropic:
  tool-selection ability "degrades once you exceed 30–50" tools; tool search is advised from 10
  tools or 10,000 tokens of definitions
  ([tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)). L.
  A stress test of one retrieval method, with one correct tool among N candidates on 20 tasks per N
  and the qwen-max model, found success above 90% below about 30 candidates, intermittent failure
  from 31 to 70, and failures dominating beyond about 100; retrieving the likely tool first lifted
  success from 13.62% to 43.13% and cut prompt tokens by about 49% ([RAG-MCP](https://arxiv.org/html/2505.03275v1)). M, one paper, an older
  model, a judge model whose identity the paper states two ways. These are tool schemas, not
  `SKILL.md` listings; whether skill descriptions follow the same curve is `UNVERIFIED`.
- **Tool search with deferred definitions.** Anthropic reports definitions of about 77,000 tokens
  before and 8,700 after tool search, and accuracy on its MCP evals from 49% to 74% (Opus 4) and
  79.5% to 88.1% (Opus 4.5) ([advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use),
  2025-11-24). L, vendor-run. It advises keeping the three to five most-used tools always loaded and
  writing descriptions with the words users use, with consistent name prefixes so one search finds a
  group ([tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)). L.
- **Routing over a large pool.** In an 80,000-skill pool, hiding a skill's body lowered routing
  accuracy by 37 to 44 points across the retrieval methods tried, so name and description alone
  carry less signal than the full text ([SkillRouter](https://arxiv.org/abs/2603.22455), 2026-03). M, retrieval by a ranker, not by
  a coding agent reading a listing; it does not measure what a model does with a listing, which
  contains no body. Another paper reports that a tree-based retrieval over 200 to 200,000 skills
  approaches an oracle choice ([AgentSkillOS](https://arxiv.org/abs/2603.02176)), and a third that
  decomposing a task before choosing skills lowered token use against baselines
  ([SkillReranker](https://arxiv.org/abs/2607.06283)); the abstracts give no token figures. M,
  abstracts only.
- **Keyword versus situation wording.** The standard's guidance favours the user's intent over the
  skill's mechanics. Skills.md holds the one test that supports it (66.7% to 100% over about 20 cases,
  anecdote). No source found compares the two wordings across many skills. `UNVERIFIED`.
- **Negative triggers.** The standard advises that a description that triggers too broadly should say
  what the skill does not do, and OpenAI advises stating in the system prompt when to use and when
  not to use each function. No source found measures the effect of a "not for X" clause on false
  loads. `UNVERIFIED`.
- **Testing a description.** About 20 prompts, 8 to 10 that should trigger and 8 to 10 near-miss
  prompts that should not; each run about 3 times, a trigger rate above 0.5 counts as a trigger; a
  roughly 60/40 train and validation split; about five rounds; pick the round with the best
  validation pass rate ([optimizing descriptions](https://agentskills.io/skill-creation/optimizing-descriptions)). L. Claude Code lists
  `claude plugin eval` with a `tool_used: Skill` grader for a plugin's skills
  ([skills](https://code.claude.com/docs/en/skills)). L.

## 4. Structure for economy (STABLE)

- **Progressive disclosure is the main lever, and the levels are fixed by the standard.** Metadata
  always; body when the skill is chosen; resources when read. Anthropic: "the context window is a
  public good" shared with the system prompt, history and other skills' metadata
  ([best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)). L.
- **Lengths the makers give.** `SKILL.md` under 500 lines (Anthropic, the standard, Claude Code);
  instructions under 5,000 tokens (the standard); a reference file over 100 lines opens with a
  contents list so a partial read still shows its scope; references one level deep, because nested
  references may be read in part (`head`). A reference file read in full costs its whole text, so
  files are split by use, for example by domain, and the skill file points to each. L.
- **Split by stage or domain, not by size.** Anthropic's pattern for a multi-domain skill is a short
  overview that names the file for each domain, so a request about one domain reads only that file.
  L. The SkillsBench figures in [skills.md](skills.md) (focused skills of two or three modules beat
  exhaustive bundles) give the outcome side. M.
- **Scripts in place of prose.** A utility script is more reliable than model-written code, saves the
  tokens of its source, and only its output enters the context. The instruction says whether to run
  or to read it. Claude Code's cost page gives a hook that filters a log to the error lines as an
  example of tens of thousands of tokens becoming hundreds. L
  ([best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices),
  [costs](https://code.claude.com/docs/en/costs)).
- **Always-loaded versus on-demand.** The Vercel eval found a compressed 8 KB index in `AGENTS.md`
  beat a default skill and an instructed skill on one framework's API tasks (100%, 53% and 79%); the
  index was cut from about 40 KB to 8 KB (80%) ([Vercel](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals), 2026-01-27). M, vendor, one
  framework, a suite revised during the study. It shows that a small always-loaded index can
  outperform a skill that is not loaded; it does not show that a large always-loaded file is cheaper.
  Claude Code's cost page says the opposite for specialised workflow text: instructions for a few
  tasks belong in skills, because `CLAUDE.md` tokens are present on unrelated work, with the target
  under 200 lines ([costs](https://code.claude.com/docs/en/costs)). L. The two fit together: index
  or facts that most tasks need go in the always-loaded file, and text for a named workflow goes in
  a skill (inference).
- **Long always-loaded files cost and do not generally help.** Repository context files raised
  inference cost by over 20% on average, and generally did not raise success; agents followed the
  instructions, repository overviews did not help, and the authors found such files useful for
  non-standard practice ([arXiv 2602.11988](https://arxiv.org/abs/2602.11988), v3 2026-09-29). M. Other results on the same
  topic are in [agent-workspace.md](agent-workspace.md).
- **Description text is paid on every call and needs a ceiling of its own.** The caps differ by
  harness (1,024 characters in the standard, 1,536 in Claude Code's listing, 250 in the menu and in
  ZCode's injection), and both Claude Code and Codex shorten descriptions when the budget is short, so
  the use case goes first. L (§1; [cross-harness.md](../harnesses/cross-harness.md#6-skills-discovery-and-listing)).
- **Tool lists follow the same rule.** Keep the small, frequently used set loaded and defer the
  rest; the Claude Code docs prefer a command-line tool with no per-tool listing over an MCP server
  for the same job ([costs](https://code.claude.com/docs/en/costs)). L.

## 5. Measuring cost and outcome (MONITOR)

- **In Claude Code.** `/context` shows what fills the window, with a Skills row that matches the
  budgeted listing; `/doctor` estimates the listing's context cost and biggest contributors;
  `/skill-doctor` shows each skill's cost and how often it is used and proposes candidates to turn
  off; `/usage` shows token counts by model, the share of input served from cache, misses with a
  likely cause, and, on plans, a breakdown by skill, subagent, plugin and MCP server with
  recommendations that name an instruction file and its tokens per request. Claude Code OpenTelemetry
  export reports cache read and creation tokens by user and session; a status line script reads the
  same numbers ([costs](https://code.claude.com/docs/en/costs), [caching](https://code.claude.com/docs/en/prompt-caching)). L. The attribution
  figures are approximate and computed from local history.
- **In the provider's response.** `cache_read_input_tokens` and `cache_creation_input_tokens`
  (Anthropic), `cached_tokens` and `cache_write_tokens` (OpenAI): a high read-to-write ratio means
  the prefix is stable ([prompt-caching.md](prompt-caching.md)). L.
- **Cost against outcome for a skill.** Run each test case with the skill and without it (or against
  the previous version), in a clean context, and record tokens and duration beside the pass rate; the
  benchmark file holds mean and spread for each configuration and the difference. The guidance reads
  the difference as the price: 13 seconds for 50 points is probably worth it, and doubled tokens for 2
  points might not be. It asks to drop assertions that pass in both configurations, which show no
  value, and to read transcripts for wasted steps ([evaluating skills](https://agentskills.io/skill-creation/evaluating-skills)). L.
- **Lean by deletion.** The same guide says that if pass rates plateau while rules are added, the skill
  may be over-constrained, and to try removing instructions and see whether results hold. L.
- **Cost in a published study.** The context-file study reports cost with success on the same tasks
  ([arXiv 2602.11988](https://arxiv.org/abs/2602.11988)); Cursor reports total agent tokens in runs that called an MCP tool,
  46.9% fewer with dynamic discovery, a significant effect with high variance by the number of MCP
  servers installed and with no accuracy measure ([Cursor](https://cursor.com/blog/dynamic-context-discovery), 2026-01-06). M, vendor.

## Gaps in the sources

- No source found measures the token or success effect of the Claude Code or Codex listing budget as
  its size changes, or of dropping descriptions to names only. `UNVERIFIED`.
- No source found measures how many installed skills a current model can choose among with the
  listing alone. The tool-count thresholds above are for tool schemas.
- The per-skill invocation rate in ordinary use is not published; the break-even in §2 needs it.
- Whether Codex re-sends `AGENTS.md` and the skill list on each call is not stated by the Codex
  pages; the provider API behaviour implies it. `UNVERIFIED` for the Codex harness itself.
