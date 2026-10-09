---
last_checked: 2026-10-03
volatility: MONITOR (lineage, guides and API behaviour change at each release; prices, defaults and beta headers are VOLATILE)
sources:
  - https://platform.claude.com/docs/en/models/overview
  - https://www.anthropic.com/claude-haiku-5-5
  - https://platform.claude.com/docs/en/models/haiku-5-5/overview
  - https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5
  - https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5
  - https://www.anthropic.com/claude/mythos
  - https://www.anthropic.com/document/claude-haiku-5-5-system-card
  - https://platform.claude.com/docs/en/about-claude/models/overview
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
  - https://platform.claude.com/docs/en/about-claude/pricing
  - https://platform.claude.com/docs/en/release-notes/overview
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5
  - https://platform.claude.com/docs/en/models/fable-5-1/overview
  - https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1
  - https://platform.claude.com/docs/en/models/fable-5/overview
  - https://platform.claude.com/docs/en/models/fable-5/introducing-claude-fable-5-and-claude-mythos-5
  - https://platform.claude.com/docs/en/models/opus-5-5/overview
  - https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5
  - https://platform.claude.com/docs/en/models/opus-5/overview
  - https://platform.claude.com/docs/en/models/sonnet-5-5/overview
  - https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5
  - https://platform.claude.com/docs/en/models/sonnet-5/overview
  - https://platform.claude.com/docs/en/models/haiku-4-5/overview
  - https://platform.claude.com/docs/en/models/haiku-4-5/migration-guide
  - https://platform.claude.com/docs/en/build-with-claude/effort
  - https://platform.claude.com/docs/en/build-with-claude/thinking
  - https://platform.claude.com/docs/en/build-with-claude/extended-thinking
  - https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback
  - https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - https://platform.claude.com/docs/en/build-with-claude/vision
  - https://platform.claude.com/docs/en/build-with-claude/context-windows
  - https://platform.claude.com/docs/en/build-with-claude/prompt-caching
  - https://platform.claude.com/docs/en/build-with-claude/task-budgets
  - https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages
  - https://platform.claude.com/docs/en/manage-claude/api-and-data-retention
  - https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence
  - https://code.claude.com/docs/en/model-config
  - https://www.anthropic.com/claude-fable-and-mythos-5-1
  - https://www.anthropic.com/claude-opus-5-5
  - https://www.anthropic.com/claude-sonnet-5-5
  - https://www.anthropic.com/news/redeploying-fable-5
  - https://www.anthropic.com/claude-fable-5-1-mythos-5-1-system-card
  - https://www.anthropic.com/claude-fable-5-mythos-5-system-card
  - https://www.anthropic.com/claude-opus-5-5-system-card
  - https://www.anthropic.com/claude-opus-5-system-card
  - https://www.anthropic.com/document/claude-sonnet-5-5-system-card
  - https://www.anthropic.com/claude-sonnet-5-system-card
  - https://www.anthropic.com/claude-haiku-4-5-system-card
  - https://artificialanalysis.ai/articles/claude-sonnet-5-5
  - https://labs.scale.com/leaderboard/swe_bench_pro_public_v2
  - https://www.tbench.ai/leaderboard/terminal-bench/4.0
  - https://artificialanalysis.ai/agents/coding
  - https://metr.org/time-horizons/
---

# Anthropic models

Anthropic's Claude models are served through its own API (the Messages API), through Amazon Bedrock,
Google Cloud, Microsoft Foundry and Claude Platform on AWS, and through Anthropic's apps and Claude Code.
This folder holds eight models in the current and previous generation of four classes: Fable, Opus,
Sonnet and Haiku. This page carries what holds for all of them: the lineage, the API surface, what
the maker's prompting guides say, how to read a system card, and the behaviour the models share. Each
model file says what differs for its model and links back here.

## Models and lineage

Anthropic sells four classes, from the largest to the smallest. Fable is the frontier class, and its
weights are the same as those of Mythos, a second configuration with fewer safeguards that Anthropic
offers only to verified organizations. Mythos 5 and 5.1 have no cards here because restricted access is
outside the general-availability/public-preview rule, not because those configurations have no users.
Fable and Mythos share weights but have different safeguards; that difference can change results.
[as-of 2026-10-09] (L) [mythos-current] Opus is
the class for long-running agentic coding and knowledge work. Sonnet pairs speed with capability. Haiku is
the small, fast class. [models-overview, ann-fable51]

| Model (file) | API id | Released | Status at stated check | Retirement commitment | Context / max output | List price in / out per Mtok | Default effort |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Claude Fable 5.1](claude-fable-5-1.md) | `claude-fable-5-1` | 2026-09-01 | active, latest Fable | not sooner than 2027-09-01 | 1M / 128k | $10 / $50 | `high` |
| [Claude Fable 5](claude-fable-5.md) | `claude-fable-5` | 2026-06-09 | active, legacy | not sooner than 2027-06-09 | 1M / 128k | $10 / $50 | `high` |
| [Claude Opus 5.5](claude-opus-5-5.md) | `claude-opus-5-5` | 2026-09-22 | active, latest Opus | not sooner than 2027-09-22 | 1M / 128k | $4 / $20 | `medium` |
| [Claude Opus 5](claude-opus-5.md) | `claude-opus-5` | 2026-07-24 | active, legacy | not sooner than 2027-07-24 | 1M / 128k | $5 / $25 | `high` |
| [Claude Sonnet 5.5](claude-sonnet-5-5.md) | `claude-sonnet-5-5` | 2026-09-28 | active, latest Sonnet | not sooner than 2027-09-28 | 1M / 128k | $2 / $10 | `high` on the API |
| [Claude Sonnet 5](claude-sonnet-5.md) | `claude-sonnet-5` | 2026-06-30 | active, legacy | not sooner than 2027-06-30 | 1M / 128k | $2 / $10 | `high` |
| [Claude Haiku 5.5](claude-haiku-5-5.md) | `claude-haiku-5-5` | 2026-10-07 | active, latest Haiku (2026-10-09) | not sooner than 2027-10-07 | 1M / 128k | $0.10 / $0.50 up to 100k input; $0.50 / $2.50 above | `medium` |
| [Claude Haiku 4.5](claude-haiku-4-5.md) | `claude-haiku-4-5-20251001` (alias `claude-haiku-4-5`) | 2025-10-15 | previous Haiku (2026-10-09) | not sooner than 2026-10-15 | 200k / 64k | $1 / $5 | no effort parameter |

The Haiku 5.5 row and the previous-generation status of Haiku 4.5 are checked on 2026-10-09 (L)
[page-haiku55, ann-haiku55]. Other rows retain the document's 2026-10-03 check date.

What replaced what, from Anthropic's release notes, model pages and deprecation page [relnotes,
deprecations]:

- **Fable.** Fable 5 (and Mythos 5) came out on 2026-06-09 above Opus 4.8. Three days later the US
  government applied export controls to both models and Anthropic suspended access for all users;
  the controls were lifted on 2026-06-30 and access returned on 2026-07-01. Fable 5.1 followed on
  2026-09-01 at the same list prices with cache reads cut to a quarter of the Fable 5 rate. [redeploy]
- **Opus.** Opus 5 (2026-07-24) replaced Opus 4.8 at $5 / $25. Opus 5.5 (2026-09-22) replaced Opus 5 at
  $4 / $20, with a cache-read price 60 percent lower than Opus 5's. Anthropic calls it the first model of its
  Claude 5.5 family. [ann-opus55]
- **Sonnet.** Sonnet 5 (2026-06-30) replaced Sonnet 4.6 at $2 / $10; the launch price was announced as
  introductory, and on 2026-08-10 Anthropic made it the standard price and cancelled the planned rise to $3 / $15.
  Sonnet 5.5 (2026-09-28) replaced Sonnet 5 at the same input/output prices. Cache reads fell from $0.20
  to $0.10 per Mtok on 2026-10-07 [as-of 2026-10-09] (L) [ann-haiku55]. [pricing, relnotes]
- **Haiku.** Haiku 4.5 (2025-10-15) replaced Haiku 3.5, which was retired on 2026-02-19 (Haiku 3 was retired
  on 2026-04-20). [deprecations] Haiku 5.5 shipped on 2026-10-07 with adjustable effort, adaptive thinking,
  1M context and 128k output. It replaces 4.5 as current; 4.5 remains the previous generation in this
  folder. [as-of 2026-10-09] (L) [ann-haiku55, page-haiku55]

Older Claude models (Opus 4.5 to 4.8, Sonnet 4.5 and 4.6, Mythos Preview) are outside this folder's scope.
Sonnet 4.5 was deprecated on 2026-09-30, with retirement set for 2026-11-30. [deprecations]

Anthropic's own recommendation on its models overview is to start with Opus 5.5 for most workloads, to use
Fable 5.1 for demanding reasoning and long-horizon agentic work or where Opus 5.5 at higher effort still falls
short, and to treat Haiku 5.5 as the fastest current model at standard speed
[as-of 2026-10-09] (L) [models-current, ann-haiku55]. The Fable 5.1 "what's new" and overview pages still say to
start with Claude Opus 5 (they predate Opus 5.5), so two pages of the same site disagree. [models-overview,
page-fable51]

"Legacy" is Anthropic's word for an older model that is still active, will not be updated and may be deprecated
later. No in-scope model has a deprecation announced. The retirement column is a "not sooner than" floor on
Anthropic-operated platforms; Bedrock and Google Cloud set their own dates, and Anthropic promises at least 60
days' notice for a public model. Haiku 4.5's floor is 12 days after the check date for this folder. [deprecations]

## API surface

**Protocol and ids.** Everything uses the Messages API. Since the 4.6 generation, each model id is a pinned
snapshot with no date suffix; Haiku 4.5 keeps a dated id and a dateless alias that resolves to it. The Claude
API, Claude Platform on AWS, Microsoft Foundry and Google Cloud use the same id (`claude-opus-5-5`); Amazon
Bedrock prefixes it (`anthropic.claude-opus-5-5`); Haiku 4.5 on Google Cloud is `claude-haiku-4-5@20251001`.
[models-overview] Anthropic's apps set their own effort defaults: Fable 5.1 runs at medium in Claude Cowork and
on claude.ai, and Opus 5.5 and Sonnet 5.5 default to medium in Claude Code. [ann-fable51, claude-code-config]

**Limits shared by the 5-series.** The 1M-token window is the default and maximum; synchronous output is
128k. Haiku 5.5's rate rises above 100,000 prompt tokens, including cached tokens; the other 5-series
models retain one rate across the window. Batch output reaches 300k with a beta header on Opus 5.5,
Opus 5, Sonnet 5.5, Sonnet 5 and Haiku 5.5 (Fable has no batch extension). Haiku 4.5 has 200k and 64k.
[as-of 2026-10-09] (L) [page-haiku55, pricing-current]
Requests may carry up to 600 images or PDF pages (100 for the 200k-window model). On the current tokenizer,
introduced with Opus 4.7, the same text produces about 30 percent more tokens than on older models, so token
limits and prices cannot be compared per token across that boundary. [models-overview, context-windows, pricing]

**Thinking.** All 5-series models think adaptively: the model decides when and how long to think, steered by
the effort parameter (`output_config.effort`: `low`, `medium`, `high`, `xhigh`, `max`). What a request may
send differs by model, and an unsupported value is a 400 error [thinking]:

| Model | no `thinking` field | `disabled` | manual `enabled` + `budget_tokens` |
| --- | --- | --- | --- |
| Fable 5.1, Fable 5, Opus 5.5 | adaptive | 400 | 400 |
| Sonnet 5.5 | adaptive | 400; use `between_tools` at `high` effort or below | 400 |
| Opus 5 | adaptive | accepted at `high` or below, 400 at `xhigh` and `max` | 400 |
| Haiku 5.5 | adaptive | accepted at `high` or below, 400 at `xhigh` and `max` | 400 |
| Sonnet 5 | adaptive | accepted | 400 |
| Haiku 4.5 | off | accepted | accepted, budget at least 1,024 tokens and below `max_tokens` |

Haiku 5.5's thinking row is checked on 2026-10-09 (L) [haiku55-new]; other rows keep their earlier dates.

`thinking.display` defaults to `omitted` on every 5-series model: thinking blocks come back with an empty text
field (still billed, still required in later turns), `summarized` returns a summary, and `updates` (beta header
`thinking-display-updates-2026-08-18`) keeps reasoning empty and returns a short summary of each progress note the
model writes between tool calls (Fable 5.1, Fable 5, Opus 5.5 and Sonnet 5.5 write such notes). The raw chain of thought is never returned. Thinking tokens count toward `max_tokens`. Effort
is a soft behavioural signal; `max_tokens` is the hard ceiling. [thinking, effort] Haiku 4.5 uses manual
extended thinking with a token budget, has no effort parameter, and does not interleave thinking between tool
calls. [extended-thinking, models-overview]

**Effort in practice.** Effort changes thinking, tool-call count, explanation length and code-comment
volume together; lower levels batch operations into fewer tool calls and answer with less preamble. A level
name does not mean the same amount of thinking on two models: Anthropic repeats this in every guide, and asks
for a fresh sweep when moving between generations. Changing the top-level effort between requests invalidates the
prompt cache. Fable 5.1, Opus 5.5, Opus 5 and Sonnet 5.5 accept a per-message change (beta header
`mid-conversation-output-config-2026-07-01`: a `role: "system"` message with empty content and the new level),
which keeps the cache; Fable 5, Sonnet 5 and Haiku 4.5 do not. [effort] Haiku 5.5 also accepts it with
adaptive thinking on the Claude API and Google Cloud; changing effort with thinking disabled returns 400.
[as-of 2026-10-09] (L) [effort-current]

**Sampling, prefill and tool choice.** Any non-default `temperature`, `top_p` or `top_k` returns a 400 on every
5-series model. Prefilling the assistant turn returns a 400 on the 5-series (and on all models from the 4.6
generation); Haiku 4.5 still accepts both a prefill and `temperature` or `top_p` (not both together), but not a
prefill while extended thinking is on. `tool_choice` of type `any` or `tool` returns a 400 on Fable 5.1, Opus 5.5
and Sonnet 5.5, with `auto` and `none` unchanged; Fable 5, Opus 5, Sonnet 5, Haiku 5.5 and Haiku 4.5 accept forced
tool use (on Haiku 4.5 not together with manual extended thinking). Anthropic's replacement is `strict: true` on
tools, or structured outputs, plus a prompt that says when a tool applies. Haiku 5.5's forced call omits
pre-tool thinking [as-of 2026-10-09] (L) [haiku55-migration]. [thinking, whats-new-fable51,
whats-new-opus55, whats-new-sonnet55, best-practices]

**Structured output.** `output_config.format` with a JSON schema constrains decoding; `strict: true` constrains
tool names and inputs. Limits: no recursive schemas, no numeric or string-length constraints, `additionalProperties`
must be `false`, `minItems` only 0 or 1, at most 20 strict tools, 24 optional parameters and 16 union-typed
parameters per request; a schema that compiles too large returns a 400 and compilation times out at 180 seconds.
The first use of a schema pays compile latency; grammars are cached for 24 hours. Required properties are emitted
before optional ones. Citations and prefill are incompatible with it, a refusal or a `max_tokens` stop can break
the schema, and enum values may come back differing in capitalisation. A schema property that asks for the model's
reasoning can trigger the `reasoning_extraction` refusal (below). All eight models are listed as supported [as-of 2026-10-09] (L) [structured-current] on the
Claude API, Platform on AWS, Google Cloud and Foundry; on Amazon Bedrock the feature is documented only for the
legacy Bedrock integration (which serves Haiku 4.5 and 4.x models), not for Claude in Amazon Bedrock. [structured-outputs]

**Images and documents.** Images go in as base64, URL or Files API ids, JPEG, PNG, GIF or WebP, up to 8000 x 8000
pixels and 10 MB base64 on the Claude API (5 MB on Bedrock and Google Cloud), 600 per request; above 20 images
each image is held to a stricter dimension limit (2000 px keeps a request safe everywhere). Models from 4.7 onward,
which includes the whole 5-series, see up to 2576 px on the long edge and 4,784 visual tokens; Haiku 4.5 sees
1,568 px and 1,568 tokens. Cost is about one token per 28 x 28 patch. Anthropic advises placing images before the
text that refers to them. Claude cannot name people in images, counts approximately, and returns pixel coordinates
in the resized image's space. No model outputs images, audio or video. [vision]

**Caching.** Minimum cacheable prompt: 512 tokens on Fable 5.1, Fable 5, Opus 5.5, Opus 5 and Sonnet 5.5;
512 on Haiku 5.5 [as-of 2026-10-09] (L) [cache-current]; 1,024 on Sonnet 5; 4,096 on Haiku 4.5. A five-minute write costs 1.25x the input price, a one-hour write 2x, a read
0.1x, except 0.025x on Fable 5.1 and 0.05x on Opus 5.5 and Sonnet 5.5
[as-of 2026-10-09] (L) [cache-current]. Changing the system prompt, tools, thinking configuration
or top-level effort restarts the cache from that point. [prompt-caching, pricing]

**Context management and long runs.** Server-side compaction and context editing trim history without
counting as edits to earlier turns. Compact on demand (beta header `compact-2026-09-04`) returns a signed summary
block. Task budgets (beta header `task-budgets-2026-03-13`) give the model a live token countdown for a whole
agentic loop; supported on Fable 5.1, Fable 5, Opus 5.5, Opus 5 and Sonnet 5.5, not on Sonnet 5 or Haiku 4.5.
Mid-conversation system messages (to add an instruction without editing `system`) and turn-scoped system messages
(header `mid-conversation-system-clear-at-2026-08-21`, cleared when the next user message arrives) exist on
Fable 5.1, Fable 5, Opus 5.5, Opus 5 and Sonnet 5.5, not on Sonnet 5 or Haiku 4.5. In-message tool definitions
(beta header `inline-tools-2026-09-15`) work on the same models. [task-budgets, mid-conversation, relnotes]
Haiku 5.5 also supports task budgets and mid-conversation system messages. Task budgets are advisory,
not provider-enforced spend caps. [as-of 2026-10-09] (L) [budgets-current, mid-current]

**Tools.** Computer use is the `computer_toolset_20260801` toolset (batch actions, zoom on by default, about 4,500
tokens of definition overhead); on the Claude API and Google Cloud, Opus 5.5 and Sonnet 5.5 reject the earlier
`computer_20251124` tool (Bedrock still accepts it). A browser use toolset exists beside it. Fast mode (research
preview, Claude API only) exists for Opus 5.5 and Opus 5 at higher prices. Server-side web search costs $10 per 1,000
searches; web fetch has no fee beyond tokens; code execution is free when it accompanies the 2026-02-09 versions
of web search or web fetch. [whats-new-opus55, pricing, relnotes]

**Data handling and residency.** Fable 5.1, Fable 5 and their Mythos twins are "Covered Models": they need
30-day data retention and are not available under zero data retention unless Anthropic expressly authorizes it
(Anthropic's launch post says eligible customers may use Fable 5.1 under zero retention until a customer-hosted
safeguard scheme arrives later in 2026; the documentation still states the restriction). Opus 5.5, Opus 5, the
Sonnets and Haiku are not on that list. `inference_geo: "us"` adds 1.1x to every price category on the Claude
API and Platform on AWS. Text from Fable 5.1 carries a statistical watermark on every platform; Anthropic's Fable
5.1 post says the watermark is added to the outputs of models released after 2026-08-02 (to meet the EU AI Act),
and its Opus 5.5 post says Opus 5.5 carries it too. [retention, pricing, ann-fable51, whats-new-fable51, ann-opus55]

**Refusals and fallback.** Fable 5.1, Fable 5, Opus 5.5, Opus 5, Sonnet 5.5 and Haiku 5.5 run safety
classifiers [as-of 2026-10-09] (L) [refusals-current]. A decline is
a successful HTTP 200 with `stop_reason: "refusal"` and a `stop_details.category` of `cyber`, `bio`, `frontier_llm`,
`reasoning_extraction` or `general_harms`, depending on the model; any partial output should be discarded. Declines before any output in
`bio`, `frontier_llm` and `reasoning_extraction` are billed as normal requests (since 2026-09-24); the others are
not. Fallback retries the request on another model: `fallbacks: "default"` (beta header
`server-side-fallback-2026-07-01`) on the Claude API, an SDK middleware elsewhere, or a manual retry with
fallback credit that refunds the cache-write cost of the switch. `reasoning_extraction` declines are never retried
by the default routing. Anthropic's permitted fallbacks: Opus 4.8 and Opus 5 for Fable 5.1; Opus 4.8 for cyber
declines and Opus 5 for biology and frontier-model-development declines on Opus 5.5; Sonnet 5 for `cyber` and
`frontier_llm` declines on Sonnet 5.5, with `bio`, `reasoning_extraction` and `general_harms` declines left standing. Classifiers
that guard against distillation, and the ones for conventional weapons and explosives, have no fallback.
Anthropic's system cards say all blocks are transparent and "do not covertly change model responses".
[refusals, whats-new-fable51, sc-opus55, sc-sonnet55] Haiku 5.5 has no server-side fallback and provides
no fallback credit; a manual model switch writes a new cache at full price. [as-of 2026-10-09] (L)
[refusals-current]

## Prompting guides

Anthropic publishes one general page and one guide per model. The general page,
[Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices),
is organised as model-specific notes first, then techniques for all current models, then migration notes; it
tells the reader to treat a technique that names a model as measured on that model and to re-check it on another.
Haiku 4.5 has no guide of its own, so this page is its guide. [best-practices] Haiku 5.5 has a dedicated
guide linked from its [model file](claude-haiku-5-5.md), with search, verification, JSON/tool and user-message
handling notes. [as-of 2026-10-09] (L) [guide-haiku55]

What the general page says, in outline (L):

- **Be direct and explicit.** The page says to state the output wanted, to ask for "above and beyond" behaviour outright, and
  to explain why a rule exists, because the model generalises from the reason (its example: a rule against ellipses works better
  when the prompt says the reply will be read aloud by a text-to-speech engine). Its test: would a colleague with no context be confused by this prompt.
- **Examples** steer format and tone better than description. Three to five, relevant, varied, wrapped in
  `<example>` tags inside `<examples>`.
- **Structure with XML tags** (consistent names, nested when the content nests) for prompts that mix
  instructions, context, examples and inputs. Give the model a role in the system prompt, even in one sentence.
- **Long documents go first and the question last.** The page puts documents above the instructions; in Anthropic's tests
  ending with the query improved quality by up to 30 percent on multi-document input. Wrap each document with
  source metadata, and for analysis tasks ask the model to quote the relevant passages before answering.
- **Format control.** The page prefers saying what to do over what not to do, and matching the prompt's own style to the style
  wanted (a prompt free of markdown yields less markdown); XML tags can mark a section of the output. Current models
  default to LaTeX for maths; ask for plain text if that is wrong. They write more tersely and may skip summaries
  after tool calls; ask for one if wanted.
- **Prefill is gone from the 4.6 generation on.** The page lists replacements: structured outputs or an enum tool
  for format and classification, a direct instruction for preambles, the user turn for continuations and context
  reminders.
- **Tools.** The models follow tool instructions literally: asking "can you suggest some changes" gets suggestions.
  Say "make these edits" or add a standing instruction to act by default; the opposite instruction (do not
  change files until told) is also given. The page notes that Opus 4.5 and 4.6 can over-trigger tools on
  aggressive wording written for older models ("CRITICAL: You MUST use this tool") and advises plainer language. Parallel calls are the default and can be pushed towards 100
  percent with an instruction, or damped with an instruction to run sequentially.
- **Thinking.** Adaptive thinking drove better results than manual budgets in Anthropic's internal evaluations.
  General instructions ("think thoroughly") beat a hand-written plan; worked examples shape the model's
  reasoning; when thinking is off, step-by-step prompting with the answer in tags still works, except that on
  the models that screen reasoning extraction (Fable 5.1, Fable 5, Opus 5.5, Opus 5, Sonnet 5.5) asking the model to
  write its reasoning in the reply can be declined. Asking for a final self-check helps on coding and maths, but
  Opus 5 over-verifies if it is asked.
- **Agentic work.** Models with context awareness (Sonnet 5 and Haiku 4.5 among these eight) track their own
  remaining window, so a prompt for them should say when the harness will compact or save state, or they
  wrap up early. For work across several windows: use a different first-window prompt that sets up tests and
  scripts, keep tests in a structured file, keep progress notes as free text, use git as the state log, prefer
  a fresh window that rediscovers state over lossy compaction when the filesystem holds the state, and give
  verification tools (computer use, browser use). For risky actions, tell the model to take local reversible steps
  freely and confirm destructive, hard-to-reverse or shared-system actions. For research, give success criteria
  and ask for competing hypotheses and a notes file. Subagents are used readily, sometimes too readily, so state
  when delegation is worth it. Coding add-ons the page gives: a scope-limiting block against over-engineering, an
  instruction to clean up temporary files, a block against hard-coding to pass tests, and one that forbids claims
  about code the model has not opened.
- **Vision and frontend.** A crop or zoom tool lifts image scores consistently (Anthropic publishes a recipe).
  Without design direction, models fall back on generic patterns; the page offers an aesthetics block naming what to
  avoid. The Opus 5.5 and Sonnet 5 guides add that a generic counter-instruction (the Opus 5.5 guide's example is
  "avoid a generic AI look") mostly swaps one default style for another, and that naming specific patterns or giving a
  concrete specification works better.

How the guides moved, release by release (L): the Opus 4.5 and 4.6 notes told writers to dial down forceful tool
language and to damp subagent and over-engineering tendencies. The Fable 5 guide (June 2026) says one short
instruction steers most behaviours as well as a list of cases, that older instruction files are often too prescriptive,
and that the reasoning-echo refusal exists. The Sonnet 5 guide (June) stresses literal reading of instructions and
that temperature is gone. The Opus 5 guide (July) tells writers to delete verification and double-check
instructions, cap subagent spawning, and ask for brevity explicitly because effort does not shorten replies. The
Fable 5.1 guide (September) describes behaviour that moved since Fable 5: fewer progress updates, less formatting, one
tool call per turn in some loops and unmarked quotation each need a prompt fix, and anti-formatting rules written for
older models can now strip structure the content needs. The
Opus 5.5 and Sonnet 5.5 guides (September) are about effort recalibration, silent progress updates, early stops in
unattended loops, pasted-text injection and thinking that cannot be turned off. Each model file summarises its
own guide.

## System-card practice

Anthropic publishes a system card for each release, linked from the model page. The Fable and Opus cards in this
folder run from 198 to 317 pages and the Sonnet cards to 146 and 148; the Sonnet 5.5 card says it was deliberately
condensed and that non-frontier cards will be condensed from now on; the Haiku 4.5 card is 39 pages. The recent structure is: a summary; Responsible Scaling
Policy and Frontier Compliance Framework evaluations (chemical and biological risk at a lower threshold
"CB-1" and a higher "CB-2"; AI research and development; an alignment-risk update); cyber; safeguards and
harmlessness; agentic safety; an alignment assessment; model welfare; capabilities. [sc-fable51, sc-sonnet55,
sc-haiku45]

How to read the numbers (L):

- **Which configuration was tested.** A card for a Fable or Mythos release reports some results on the version
  without safeguards (Mythos) and some on the deployed version; cyber results for Fable are not reported because
  its classifiers divert nearly all cyber work to an older model. Harmlessness tests use the API with no system
  prompt and, separately, claude.ai with its production system prompt; the system prompt raises harmless-response
  rates and raises over-refusal slightly.
- **Capability tables use one standard setting**: adaptive thinking at max effort, default sampling, averaged over
  five trials, unless a row says otherwise. Terminal-Bench rows say which effort and harness (Claude Code in bare
  mode). Where production safeguards were on, requests they caught were answered by the fallback model, which
  Anthropic says likely lowers the score. Figures for other vendors' models are copied from their reports or
  leaderboards.
- **Alignment evidence has stated limits.** The automated behavioural audit runs about 4,100 sessions per model,
  graded by other models; Anthropic lists blind spots (thin coverage of multi-agent work and very long runs,
  rare behaviours, impossible tasks) and records that external testers sometimes found worse behaviour than the
  internal audit. Several cards report that the model often suspects it is being tested, up to 36 percent of
  transcripts for Opus 5.5 by white-box measurement.
- **Prompt injection** is reported on an external benchmark run by Gray Swan (37 scenarios, 1,804 attacks;
  attack success after 1, 10 and 15 attempts) and on Anthropic's adaptive-attacker tests for coding, computer use
  and browser use, always without the product-level injection probes.
- **Reward hacking** is measured by classifiers over training episodes; cards compare rates only on shared
  environments because each model trained on a different mix.

Earlier practice: the Haiku 4.5 card (October 2025) uses the older AI Safety Level labels and reports Haiku 4.5
as released under the lower level (ASL-2) after "rule-out" tests; the 2026 cards use the CB-1 and CB-2 thresholds
and cite an August 2026 Risk Report that is not model-specific. [sc-haiku45, sc-fable51]

## Family-wide behaviour

These hold across the 5-series unless the model file says otherwise (L, from the guides, what's-new pages and system
cards listed in Sources):

1. **Thinking is on and mostly hidden.** On Fable 5.1, Fable 5, Opus 5.5 and Sonnet 5.5, progress notes between tool
   calls arrive as `thinking` blocks that are empty at the default display; a client that renders only `text` blocks
   looks silent. On every 5-series model a response can begin with a `thinking` block. Select content blocks by
   type, not position. Pass thinking blocks back unchanged.
2. **Thinking blocks are bound.** Each block records its model and, on Fable 5.1, Opus 5.5 and Sonnet 5.5, the
   conversation prefix that preceded it. For accounts created on or after 2026-08-31 a request that replays a
   block after the system prompt, tools or an earlier message changed returns a 400
   ("bound to a different conversation"); older accounts can opt in with
   `thinking.block_binding.prefix_mismatch_behavior` (`drop_block` drops instead of failing; beta header
   `thinking-binding-controls-2026-08-01`). Keep history append-only; per-turn reminders go in turn-scoped system
   messages, instruction changes in mid-conversation system messages, trimming to server-side compaction or
   context editing. Reading across models is one-way: Fable 5.1 reads blocks from Opus 5, Fable 5 and earlier models, and from
   Opus 5.5 on the Claude API; Opus 5.5 reads Opus 5 and earlier Opus, Sonnet and Haiku blocks and, on the Claude API and Google
   Cloud, Sonnet 5.5's, but not Fable's; Sonnet 5.5 reads Sonnet 5, Opus 4.8 and Haiku 4.5 blocks and not Opus 5 or
   later; no earlier model reads Fable 5.1's. A dropped block is not billed. Sonnet 5.5's blocks also work only in the
   account that produced them or a linked one.
3. **Instruction following is literal and scope-sensitive.** Sonnet 5 does not carry an instruction from one item to
   another; Fable 5 and Fable 5.1 add unrequested tidying, fixes, tests or documentation, more at higher effort; Opus 5
   expands scope; Sonnet 5.5 adds supporting files at every level. Anthropic's main fixes are scope sentences in the
   system prompt.
4. **Review prompts are taken literally.** "Only report high-severity issues" lowers recall because the model finds
   the bug and then withholds it; ask for everything with confidence and severity, and filter in a second step
   (Sonnet 5 and Opus 5 guides).
5. **Lower effort changes behaviour, not only depth.** Fable 5.1 searches less at `low`; Sonnet 5.5 pauses to check in
   at `low` and `medium` and can skip verification at `low`; Sonnet 5 under-thinks moderate tasks at `low`. At
   `xhigh` and `max`, Sonnet 5.5 starts its own review rounds and Fable 5.1 may draft a long deliverable in its
   thinking and then again in the reply.
6. **Effort and cost are not monotone.** In Anthropic's cost study, Opus 5.5 at its default matched Fable 5.1 at its
   default on a saturated coding subset for about a fifth of the cost per solved task, while on long research
   loops Fable 5.1 cost more for no gain above `low`; Artificial Analysis measured Sonnet 5.5 at max effort as the
   highest output-token use it had recorded for any model (about 193k tokens per index task). Anthropic's advice is to
   compare cost per completed task on one's own traffic. [optim, aa-sonnet55]
7. **Classifier behaviour.** False positives still occur: Anthropic names compile-check phrasing ("does this
   compile") over "are there bugs", lesser-known languages without documentation, and base64 in tool output as
   triggers on Fable 5.1. Source-level vulnerability discovery is allowed on Fable 5.1, Opus 5.5, Opus 5 and
   Sonnet 5.5; vulnerability discovery in compiled binaries is blocked. Anthropic offers a Life Sciences
   Verification Program for biology and a Cyber Verification Program for security work.
8. **Prompt injection.** The models are trained to treat instructions in tool results as untrusted, which has
   side effects: Sonnet 5.5 can read a genuine user message placed inside or right after a tool result, or a
   harness countdown after every result, as an injection. Opus 5.5 went the other way for text a user pastes into
   a message (see its file). Mark pasted text and keep user words out of `tool_result` blocks.
9. **Reasoning echo is declined.** Prompts, instruction files and tool descriptions that ask the model to write out
   its reasoning, or schemas with a `reasoning` field, can return `reasoning_extraction` on models that screen that category. Ask for a short explanation or a summary of actions and read summarized thinking instead.
10. **Safety posture.** The Fable, Opus and Sonnet 5-series cards read for this page report near-zero
    over-refusal of benign sensitive requests on the API
    (0 to 0.6 percent) while the single-turn harmless-response rate without a system prompt sits at 94.5 to 96.9
    percent; the claude.ai system prompt lifts it to about 99 percent. Several cards flag acceptance of unverifiable
    claims of authority and of professional or fictional framings as a weak point, and rare internal cases of
    working around classifiers or broken permission hooks (under 0.01 percent of monitored completions).

## Open questions

- Anthropic's own pages disagree in places (the Fable 5.1 pages recommend Opus 5, the overview recommends Opus 5.5;
  the launch post says eligible customers can use Fable 5.1 under zero data retention while the retention page
  says no). Which wording governs is not stated.
- No independent time-horizon measurement of any in-scope model exists on METR's page, which was last updated
  2026-05-08.
- Haiku 5.5's new [model file](claude-haiku-5-5.md) records benchmark and behavior limitations. Its
  automated audit over-refusal result differs from its single-turn benign result; these should not be
  merged into one general refusal rate. [as-of 2026-10-09] (L) [sc-haiku55]
- Artificial Analysis's Sonnet 5.5 runs used a pre-release deployment with a structured-output bug that Anthropic
  says may understate scores; a re-run is planned.
- Whether the effort-level recalibrations seen across 5.1 and 5.5 continue (each guide says a level name is not
  stable across models) is unknown.

## Sources

Old ids below retain their 2026-10-03 read date. The second table holds only sources read on 2026-10-09; the document was not fully re-verified.

| Id | URL | Kind |
| --- | --- | --- |
| models-overview | https://platform.claude.com/docs/en/about-claude/models/overview | L |
| deprecations | https://platform.claude.com/docs/en/about-claude/model-deprecations | L |
| pricing | https://platform.claude.com/docs/en/about-claude/pricing | L |
| relnotes | https://platform.claude.com/docs/en/release-notes/overview | L |
| best-practices | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices | L |
| thinking | https://platform.claude.com/docs/en/build-with-claude/thinking | L |
| effort | https://platform.claude.com/docs/en/build-with-claude/effort | L |
| extended-thinking | https://platform.claude.com/docs/en/build-with-claude/extended-thinking | L |
| refusals | https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback | L |
| structured-outputs | https://platform.claude.com/docs/en/build-with-claude/structured-outputs | L |
| vision | https://platform.claude.com/docs/en/build-with-claude/vision | L |
| context-windows | https://platform.claude.com/docs/en/build-with-claude/context-windows | L |
| prompt-caching | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | L |
| task-budgets | https://platform.claude.com/docs/en/build-with-claude/task-budgets | L |
| mid-conversation | https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages | L |
| retention | https://platform.claude.com/docs/en/manage-claude/api-and-data-retention | L |
| optim | https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence | L |
| claude-code-config | https://code.claude.com/docs/en/model-config | L |
| page-fable51 | https://platform.claude.com/docs/en/models/fable-5-1/overview | L |
| whats-new-fable51 | https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1 | L |
| whats-new-opus55 | https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5 | L |
| whats-new-sonnet55 | https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5 | L |
| ann-fable51 | https://www.anthropic.com/claude-fable-and-mythos-5-1 | L |
| ann-opus55 | https://www.anthropic.com/claude-opus-5-5 | L |
| ann-sonnet55 | https://www.anthropic.com/claude-sonnet-5-5 | L |
| redeploy | https://www.anthropic.com/news/redeploying-fable-5 | L |
| sc-fable51 | https://www.anthropic.com/claude-fable-5-1-mythos-5-1-system-card | L |
| sc-opus55 | https://www.anthropic.com/claude-opus-5-5-system-card | L |
| sc-sonnet55 | https://www.anthropic.com/document/claude-sonnet-5-5-system-card | L |
| sc-haiku45 | https://www.anthropic.com/claude-haiku-4-5-system-card | L |
| aa-sonnet55 | https://artificialanalysis.ai/articles/claude-sonnet-5-5 | M |

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| ann-haiku55 | https://www.anthropic.com/claude-haiku-5-5 | L | 2026-10-09 |
| page-haiku55 | https://platform.claude.com/docs/en/models/haiku-5-5/overview | L | 2026-10-09 |
| haiku55-new | https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5 | L | 2026-10-09 |
| haiku55-migration | https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide | L | 2026-10-09 |
| guide-haiku55 | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5 | L | 2026-10-09 |
| mythos-current | https://www.anthropic.com/claude/mythos | L | 2026-10-09 |
| models-current | https://platform.claude.com/docs/en/models/overview | L | 2026-10-09 |
| pricing-current | https://platform.claude.com/docs/en/about-claude/pricing | L | 2026-10-09 |
| cache-current | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | L | 2026-10-09 |
| effort-current | https://platform.claude.com/docs/en/build-with-claude/effort | L | 2026-10-09 |
| structured-current | https://platform.claude.com/docs/en/build-with-claude/structured-outputs | L | 2026-10-09 |
| refusals-current | https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback | L | 2026-10-09 |
| budgets-current | https://platform.claude.com/docs/en/build-with-claude/task-budgets | L | 2026-10-09 |
| mid-current | https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages | L | 2026-10-09 |
| sc-haiku55 | https://www.anthropic.com/document/claude-haiku-5-5-system-card | L | 2026-10-09 |
