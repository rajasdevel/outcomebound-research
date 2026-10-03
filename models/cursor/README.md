---
last_checked: 2026-10-03
volatility: MONITOR (lineage, guides and API behaviour change at each release)
sources:
  - https://cursor.com/blog/joining-spacex
  - https://cursor.com/docs/models-and-pricing
  - https://cursor.com/blog/composer
  - https://cursor.com/blog/composer-1-5
  - https://cursor.com/blog/composer-2
  - https://cursor.com/blog/composer-2-5
  - https://cursor.com/blog
  - https://cursor.com/llms.txt
  - https://artificialanalysis.ai/articles/cursor-composer-2-5-coding-agent-index
  - https://cursor.com/docs/models/cursor-composer-2-5
  - https://cursor.com/docs/agent/overview
  - https://cursor.com/docs/agent/prompting
  - https://cursor.com/docs/rules.md
  - https://cursor.com/blog/agent-best-practices
  - https://cursor.com/blog/improved-token-efficiency
  - https://cursor.com/cursorbench
  - https://cursor.com/docs/agent/security
  - https://cursor.com/docs/models/grok-4-7
---

# Cursor models

Cursor is the AI code editor and agent from Anysphere. It serves models from several makers and also trains its own: the Composer line, built for its agent harness. Cursor completed its acquisition by SpaceX on 2026-08-14 and now sits beside SpaceXAI [cursor-joining-spacex]. This folder covers Cursor's own model class, Composer. The Grok models Cursor lists in its "Cursor Models" pool (Grok 4.7, 4.6, 4.5) are SpaceXAI models trained jointly with Cursor and are covered in [the xAI folder](../xai/README.md) [cursor-pricing].

## Models and lineage

Composer, from Cursor's own posts (L):

| Model | Released | What changed |
| --- | --- | --- |
| Composer | 2025-10-29 (first agentic coding model) | A mixture-of-experts model trained by reinforcement learning on the tools of Cursor's own agent, tuned for speed [cursor-composer-1-blog]. |
| Composer 1.5 | 2026-02-09 | The same pretrained model with reinforcement learning scaled 20x further. A thinking model that thinks briefly on easy tasks and longer on hard ones, and was trained to summarise its own context when the window runs out [cursor-composer-15-blog]. |
| Composer 2 | 2026-03-19 | First continued-pretraining run; built on Moonshot's open Kimi K2.5 (named in the Composer 2.5 post); $0.50 input and $2.50 output per Mtok, Fast tier $1.50 and $7.50 and the default [cursor-composer-2-blog] [cursor-composer-25-blog]. |
| Composer 2.5 | 2026-05-18 | Same open checkpoint as Composer 2, with more training compute, 25x more synthetic tasks and targeted textual feedback; Fast tier $3 and $15 [cursor-composer-25-blog]. |

Cursor's own table gives, for Composer 1, 1.5 and 2: CursorBench 38.0, 44.2 and 61.3; Terminal-Bench 2.0 40.0, 47.9 and 61.7; SWE-bench Multilingual 56.9, 65.9 and 73.7 (maker-reported, with Cursor's benchmark versions of the time) [cursor-composer-2-blog]. Composer 2.5 is described in [its file](composer-2.5.md).

Scope in this library: two generations of the Composer class, 2.5 (current) and 2 (previous), with a model that is no longer sold let lapse. Composer 2 has no file here because it is absent from Cursor's current price list, and Cursor does not state its status there [cursor-pricing]. Cursor says it is training a significantly larger model from scratch with SpaceXAI on 10x more total compute; none had shipped as of 2026-10-03 [cursor-composer-25-blog]. A third-party site lists a "Composer 3" under a rumour tracker; the posts on the first page of Cursor's blog index (August to September 2026) show no such release, and Cursor's docs list no Composer newer than 2.5 [cursor-blog-index] [cursor-docs-index].

## API surface

- **No public API for Composer.** Composer 2.5 is available only inside Cursor: the IDE and the CLI (Artificial Analysis states there is no external API) [aa-composer-25] [cursor-composer-25-docs].
- **Access and billing.** Individual plans: Pro $20 a month, Pro Plus $60, Ultra $200; Start (India only) ₹649. Pro and above have two usage pools. The "Cursor Models" pool holds Grok 4.7, 4.6, 4.5 and Composer 2.5 with more included usage; the "Other Models" pool covers third-party models, charged at the model's API price. Start covers the Cursor Models pool only, runs those models at standard speed, and fixes Grok models at medium effort. Teams and Enterprise plans have Cursor Router, which picks a model for each Auto request. Regional data residency adds 10% to eligible models. Max Mode exists only on legacy request-based plans [cursor-pricing].
- **Prices (Composer 2.5):** standard $0.50 input, $0.20 cached input, $2.50 output per Mtok; Fast $3.00, $0.50, $15.00, and Fast is the default [cursor-pricing].
- **Cursor surfaces:** agent in the editor, Agents window, CLI (interactive, headless, ACP), cloud agents, Projects (a coordinator agent delegating to others), SDKs for TypeScript and Python [cursor-agent-overview] [cursor-docs-index].
- **Agent tools.** Search files and folders, web search, fetch rules, read files (including images for vision-capable models), edit files, shell commands, browser control, image generation and asking questions; no limit on the number of tool calls per task [cursor-agent-overview].

## Prompting guides

Cursor publishes no model-specific prompting guide for Composer. Its guidance is about the agent and applies to every model it serves:

- **Cursor's agent overview** says the agent has three parts, instructions, tools and the model, and that Cursor tunes instructions and tools separately for every frontier model; a user prompt therefore sits on top of a model-specific harness prompt that the user does not see [cursor-agent-overview].
- **The prompting page** covers `@` mentions (files, folders, terminals, earlier chats, git diffs, browser); to attach only what is known to matter and let the agent search otherwise; custom modes from skills; image and voice input; and the context ring, which breaks the window down into system prompt, tools, rules, skills, MCP, subagents, summarised and live conversation. When the window nears full, older turns are compressed into a summary [cursor-docs-prompting].
- **The rules documentation** describes four rule kinds (project rules in `.cursor/rules` as `.mdc` files, user rules, team rules, and `AGENTS.md` with nested files), their order (team, then project, then user), and best practice: focused rules under 500 lines, references to files instead of copies, no pasted style guides, only rules that fix a repeated mistake [cursor-harness-doc].
- **The agent best-practices post** (January 2026) recommends planning first (Plan Mode, plans saved as Markdown), letting the agent find context instead of tagging every file, starting a new conversation when the task changes or the agent seems confused (long conversations lose focus after many summarisations), test-first work, and trying several models on the same hard problem in separate worktrees [cursor-best-practices].
- **The token-efficiency post** (September 2026) reports that Cursor cut about 66% of its system prompt because plain tool definitions work without long lists of DO NOT and MUST, that it loads most built-in tools only when needed, shows line numbers only on every tenth line of file reads, and removed prompting that pushed subagents for exploration because models learned the habit in training [cursor-token-eff].

## System-card practice

Cursor publishes no system or model cards. A release is a blog post and a docs page. The Composer 2.5 post gives a benchmark table, effort-versus-cost charts, training methods and one safety-relevant disclosure: reward hacking found during training (see [the Composer 2.5 file](composer-2.5.md)) [cursor-composer-25-blog]. Its benchmark of record is CursorBench, built from real Cursor sessions, with a public leaderboard that Cursor runs; versions are not comparable (v3.1 and 4.0 give very different scores for the same model) [cursor-bench-board]. For deployment risk, the agent security page lists the default guardrails: terminal commands need approval unless a run mode allows them, MCP connections and each MCP tool call need approval, file edits apply immediately except to configuration files, network requests go only to GitHub, direct links and web search providers. Cursor calls its run modes (an allowlist up to an auto-review classifier, which let commands run without a prompt) best-effort guardrails and not a hard security boundary [cursor-agent-security]. A blog index entry reports that Cursor earned an AIUC-1 certification for agent security and reliability on 2026-08-13 [cursor-blog-index].

## Family-wide behaviour

- Composer models are trained on, and tuned for, Cursor's own tools: file edits, search and terminal use. Their behaviour in other harnesses is not measured, and none is available elsewhere [cursor-composer-25-docs].
- Fast is the default speed tier for Composer and for Grok models on Pro and higher plans; Fast is the same model at a higher token price [cursor-composer-25-docs] [cursor-pricing].
- Cursor's effort levels exist for Grok models (low to xhigh); Composer shows a single point on Cursor's effort charts and no published levels [cursor-grok-47] [cursor-composer-25-blog].
- Cursor says it A/B tests harness changes on live traffic and reports token savings of 7% from harness changes with no loss of agent quality; cold cache misses fell 20% after reorganising what sits at the front of each request [cursor-token-eff].

## Open questions

- Composer 2.5's context window, input types and reasoning controls are not published.
- Whether Composer models perform the same outside Cursor is untested; they cannot be run elsewhere.
- Composer 2's current availability.
- When the larger model trained with SpaceXAI will ship.

## Sources

- [cursor-joining-spacex] <https://cursor.com/blog/joining-spacex>, kind L, read 2026-10-03.
- [cursor-pricing] <https://cursor.com/docs/models-and-pricing>, kind L, read 2026-10-03.
- [cursor-composer-1-blog] <https://cursor.com/blog/composer>, kind L, read 2026-10-03.
- [cursor-composer-15-blog] <https://cursor.com/blog/composer-1-5>, kind L, read 2026-10-03.
- [cursor-composer-2-blog] <https://cursor.com/blog/composer-2>, kind L, read 2026-10-03.
- [cursor-composer-25-blog] <https://cursor.com/blog/composer-2-5>, kind L, read 2026-10-03.
- [cursor-blog-index] <https://cursor.com/blog>, kind L, read 2026-10-03.
- [cursor-docs-index] <https://cursor.com/llms.txt>, kind L, read 2026-10-03.
- [aa-composer-25] <https://artificialanalysis.ai/articles/cursor-composer-2-5-coding-agent-index>, kind M, read 2026-10-03.
- [cursor-composer-25-docs] <https://cursor.com/docs/models/cursor-composer-2-5>, kind L, read 2026-10-03.
- [cursor-agent-overview] <https://cursor.com/docs/agent/overview>, kind L, read 2026-10-03.
- [cursor-docs-prompting] <https://cursor.com/docs/agent/prompting>, kind L, read 2026-10-03.
- [cursor-harness-doc] <https://cursor.com/docs/rules.md>, kind L, read 2026-10-03.
- [cursor-best-practices] <https://cursor.com/blog/agent-best-practices>, kind L, read 2026-10-03.
- [cursor-token-eff] <https://cursor.com/blog/improved-token-efficiency>, kind L, read 2026-10-03.
- [cursor-bench-board] <https://cursor.com/cursorbench>, kind L, read 2026-10-03.
- [cursor-agent-security] <https://cursor.com/docs/agent/security>, kind L, read 2026-10-03.
- [cursor-grok-47] <https://cursor.com/docs/models/grok-4-7>, kind L, read 2026-10-03.
