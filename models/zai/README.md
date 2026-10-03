---
last_checked: 2026-10-03
volatility: MONITOR (lineage, guides and API behaviour change at each release; prices and effort mappings are VOLATILE and are held in the model cards)
sources:
  - https://www.deeplearning.ai/the-batch/glm-5-3-makes-cybersecurity-gains
  - https://docs.z.ai/guides/overview/overview
  - https://docs.z.ai/guides/overview/pricing
  - https://docs.z.ai/release-notes/new-released
  - https://docs.z.ai/guides/llm/glm-5.3
  - https://docs.z.ai/guides/llm/glm-5.2
  - https://docs.z.ai/guides/vlm/glm-5.3-flash
  - https://docs.z.ai/guides/overview/migrate-to-glm-new
  - https://docs.z.ai/guides/capabilities/thinking
  - https://docs.z.ai/guides/capabilities/thinking-mode
  - https://docs.z.ai/guides/capabilities/function-calling
  - https://docs.z.ai/guides/tools/stream-tool
  - https://docs.z.ai/guides/capabilities/struct-output
  - https://docs.z.ai/guides/capabilities/cache
  - https://docs.z.ai/api-reference/llm/chat-completion
  - https://docs.z.ai/api-reference/api-code
  - https://docs.z.ai/devpack/overview
  - https://docs.z.ai/devpack/latest-model
  - https://docs.z.ai/devpack/resources/best-practice
  - https://docs.z.ai/devpack/resources/memory-mechanism
  - https://z.ai/blog/glm-5.3
  - https://z.ai/blog/glm-5.2
  - https://z.ai/blog/glm-5.3-flash
  - https://huggingface.co/zai-org/GLM-5.3
  - https://huggingface.co/zai-org/GLM-5.3/blob/main/LICENSE
  - https://huggingface.co/zai-org/GLM-5.3-Flash
  - https://huggingface.co/zai-org/GLM-5.2
  - https://zcode.z.ai/en/docs/agents
  - https://recipes.vllm.ai/zai-org/GLM-5.3
  - https://docs.sglang.io/cookbook/autoregressive/GLM/GLM-5.3
  - https://arxiv.org/abs/2609.14992
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/glm-5-3
  - https://artificialanalysis.ai/models/glm-5-3-low
  - https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-glm-5-3
  - https://artificialanalysis.ai/agents/coding
  - https://www.tbench.ai/leaderboard/terminal-bench/4.0
---

# Z.ai models

Z.ai (the company behind the GLM models, also known as Zhipu) sells GLM through its own API, through a
subscription called the GLM Coding Plan, and as open weights. This page holds what is true of every GLM model
in this library: how the line developed, what the API accepts, what Z.ai's guides say, what Z.ai publishes
instead of a system card, and the behaviour that carries from one GLM model to the next. The model files say
what differs for each model: [GLM-5.3](glm-5.3.md), [GLM-5.2](glm-5.2.md), [GLM-5.3-Flash](glm-5.3-flash.md) and
[GLM-5.3-FlashX](glm-5.3-flashx.md), plus [GLM-4.7-Flash](glm-4.7-flash.md), the earlier Flash generation.

## Models and lineage

Dates are from Z.ai's release notes unless a row says otherwise. [zai-release-notes]

| Model | Released | What changed for people who write prompts or call the API |
| --- | --- | --- |
| GLM-4.5 | 2025-07-28 | Reasoning switched by a request field; one-step setup inside Claude Code; 128K context. |
| GLM-4.6 | 2025-09-30 | 200K context; coding flagship of its day. |
| GLM-4.7 | 2025-12-22 | Thinks before every reply and tool call by default; preserved thinking across turns; thinking switchable per turn. |
| GLM-5 | 2026-02-12 | Long-range agent and systems-engineering focus; sparse attention; 200K context. |
| GLM-5.1 | 2026-04-07 | Z.ai says it can work alone for up to 8 hours on one task; 200K context. |
| GLM-5.2 | 2026-06-16 | 1M-token context; first model with a reasoning-effort field; MIT-licensed weights the same day. |
| GLM-5.3 | 2026-08-18 (blog 2026-08-14) | Same base model as 5.2; every gain from post-training; thinking forced on; effort low, high or max; text only; weights under a custom licence, on Hugging Face from 2026-08-25. |
| GLM-5.3-Flash | 2026-08-26 | New base model, 320B parameters with 18B active, hybrid sparse and linear attention, native image, video and file input; MIT licence. |
| GLM-5.3-FlashX | 2026-09-18 (OpenRouter listing date) | A faster serving tier of Flash, about 200 tokens a second by Z.ai's page; same parameter set. |

Other facts about the line:

- GLM-5.3 and GLM-5.2 share one base model of about 753B parameters (Hugging Face) with 40B active (Artificial
  Analysis); Z.ai states no active-parameter count. [hf-glm53, aa-glm-5-3]
- Z.ai's Flash post says it is scaling the Flash recipe to larger models. No later Z.ai model had a page on the
  read date. [zai-flash-blog]
- OpenRouter lists GLM-5.3-Prime (created 2026-09-23), described as the same weights at 1.5 to 2 times the output
  speed, at about twice GLM-5.3's price. Z.ai's docs, pricing page and API reference name no such model, so it is
  a reseller listing, not a Z.ai model. [openrouter-models]
- GLM-5-Turbo and GLM-5V-Turbo (2026-03 and 2026-04) are listed by OpenRouter but are absent from Z.ai's current
  pricing page and from the model lists in its chat-completion reference. [zai-pricing, zai-chat-api]
- The earlier Flash-class generation is [GLM-4.7-Flash](glm-4.7-flash.md) (free tier, 2026-01-19), which has a
  file. Its FlashX sibling, GLM-4.7-FlashX (paid, $0.07 input and $0.40 output per million tokens on Z.ai's price
  list), has no file here. [zai-pricing, zai-release-notes]
- On the Coding Plan, requests for GLM-5.2 and 5.1 are routed to GLM-5.3, and requests for GLM-4.7 to
  GLM-5.3-Flash. FlashX was not on the plan when read. [zai-coding-plan]

Classes in this library: GLM (5.2, 5.3), GLM Flash (4.7, 5.3) and GLM FlashX (5.3).

## API surface

**Endpoints.** Z.ai documents three protocols. [zai-glm53-docs, zai-switch-models]

| Protocol | Base URL |
| --- | --- |
| OpenAI Chat Completions | `https://api.z.ai/api/paas/v4/` (pay-as-you-go); `https://api.z.ai/api/coding/paas/v4` (Coding Plan) |
| OpenAI Responses | `https://api.z.ai/api/v1` |
| Anthropic Messages | `https://api.z.ai/api/anthropic` |

The GLM-5.3 page adds that an account that ever held a Coding Plan subscription, expired ones included, can reach
the model only through the Chat Completions-compatible protocol for now. Official SDKs exist for Python
(`zai-sdk`) and Java; the OpenAI Python SDK works with the Chat Completions base URL. Model ids are lower case:
`glm-5.3`, `glm-5.2`, `glm-5.3-flash`, `glm-5.3-flashx`. [zai-glm53-docs, zai-chat-api]

**Request parameters** (chat-completion reference). [zai-chat-api]

| Field | What the reference says |
| --- | --- |
| `thinking.type` | `enabled` or `disabled`. GLM-5.3 and Flash accept only `enabled`; GLM-5.2 and earlier accept both. |
| `thinking.clear_thinking` | Default true on the API: reasoning from earlier turns is dropped from the context. False keeps it (preserved thinking), which requires sending the earlier `reasoning_content` back whole, unedited and in order. |
| `reasoning_effort` | `max` (default), `high`, `low`. See the route table below. |
| `temperature` | 0.0 to 1.0; default 1.0 for the GLM-5.x series. A value above 1 is out of range. |
| `top_p` | 0.01 to 1.0; default 0.95. The migration guide advises tuning one of temperature and top_p, not both. |
| `do_sample` | When false, temperature and top_p have no effect. |
| `max_tokens` | Up to 131072 for GLM-5.x; Z.ai's pages call this 128K. Reasoning tokens count toward it. |
| `tools` | Functions only on the Flash models; function, web-search and retrieval types on text models; at most 128. |
| `tool_choice` | Only `auto`. |
| `tool_stream` | Streams tool-call arguments as they form; needs `stream: true`. Off by default. |
| `stop` | A list, but the reference says one stop word is supported. |
| `response_format` | `text` or `json_object`, on text models. |
| `request_id`, `user_id` | Optional ids, 6 to 64 and 6 to 128 characters. |

**Reasoning-effort handling differs by route.** [zai-deep-thinking, zai-switch-models, hf-glm53]

| Route | GLM-5.3 and Flash | GLM-5.2 |
| --- | --- | --- |
| Z.ai API | Only `low`, `high`, `max`; anything else is an error; `thinking.type: disabled` is an error. | `max`, `xhigh` (mapped to max), `high`, `medium` and `low` (both mapped to high); `minimal` and `none` stop thinking; thinking can be disabled. |
| Coding Plan endpoints | `none`, `minimal`, `low` become low; `medium`, `high` become high; `xhigh`, `max` become max; a request to disable thinking becomes low instead of failing. An explicit effort wins over the thinking toggle; the default is max. | `none` or `minimal` stop thinking; low and medium become high; xhigh becomes max. |
| Self-hosted (Hugging Face chat template) | Default max when the field is absent or holds any other value; `clear_thinking` defaults to false, so Z.ai tells chat users to pass true. | Not stated on the page read. |

**Structured output.** Z.ai documents only JSON mode: `response_format: {"type": "json_object"}`, with the
wanted schema described in the system message. The page's examples validate the reply against a JSON Schema in
the caller's own code. The page names glm-5 and earlier models in its text, not GLM-5.3, and no schema-enforced
(constrained) mode is documented. [zai-struct-output]

**Caching.** Implicit: repeated prefixes are recognised and billed at the cached-input rate; the count is in
`usage.prompt_tokens_details.cached_tokens`. Cache storage is free for a limited time. [zai-cache, zai-pricing]

**Finish reasons and errors.** `finish_reason` is one of `stop`, `tool_calls`, `length`, `sensitive`,
`model_context_window_exceeded` or `network_error`. Error code 1301 reports content the platform judged unsafe
or sensitive in the input or the output; 1261 is a prompt that is too long; 1302, 1305 and 1308 to 1321 are rate,
overload and Coding Plan quota conditions. [zai-chat-api, zai-errors]

**Self-hosting.** Hugging Face holds the GLM-5.3 weights as an FP8 checkpoint with BF16 in a separate repository,
and Flash as MIT-licensed weights. The vLLM recipe starts the server with `--tool-call-parser glm47` and
`--reasoning-parser glm47` and notes that eight H200 or H20 cards hold the FP8 weights, while the full 1M context
needs eight B200 cards with an FP8 KV cache. SGLang's cookbook resolves its parsers automatically; it names the
tool-call format as XML-like `<tool_call>` blocks. Both are third-party documents. [vllm-glm53, sglang-glm53]

## Prompting guides

Z.ai publishes no prompting guide written for one GLM model. What it publishes is below; the tone is advice for
coding agents in general, and most of it is not specific to GLM.

- **Best practice for coding agents** (undated page). The page frames a task in four parts: the goal, the context
  (files, errors, examples), the constraints (standards, architecture, security, dependencies) and a "done when"
  condition, and says this reduces guessing and makes changes easier to review. It recommends a plan before edits
  on complex work, temporary instructions in the prompt and long-lived rules in project-level configuration files.
  It counts the execution environment (working directory, permissions, runnable build and test commands, tool
  connections) as part of the task, because in its account many failures come from the environment, not the model.
  It describes the agent taking part in the whole loop (implement, write tests, run them, run linters, review the
  diff), repeated workflows packaged as reusable workflow templates and stable ones automated, and one session per
  task, with history summarised or compressed when it grows. [zai-best-practice]
- **Memory mechanism** (undated page). The page separates a human-written instruction file from the notes an
  agent accumulates itself, and layers rules by scope (organisation, project, user, local, per agent role). It
  prefers rules that can be checked, such as running the test command after a change to business logic, over
  abstractions such as writing good tests. It suggests a main file under about 200 lines, with topics split into
  path-scoped files loaded on demand, and notes that rules held only in the conversation are lost when the context
  is compacted. Z.ai's page says markdown instructions are
  guidance, not enforcement, and advises avoiding conflicts between files. [zai-memory-mechanism]
- **Model pages.** The GLM-5.2 page suggests a standards-and-bounds prompt: follow the repository's engineering
  standards, add no dependencies, change no API contracts, make no commits unprompted, then build, lint and test and
  report the results and any remaining risks. The Flash page suggests, for interface and document work, stating
  the audience, page count and visual style, and asking the model to render its output, inspect it and fix what it
  finds. [zai-glm52-docs, zai-flash-docs]
- **Thinking guides.** Interleaved thinking (reasoning between tool calls) is on by default; thinking blocks should
  be returned with the tool results. Preserved thinking needs the earlier `reasoning_content` back, unmodified.
  Z.ai lists complex analysis, multi-step reasoning and design as cases for thinking, and simple fact lookups,
  basic translation and simple classification as cases where it may be off (on models that still allow that).
  [zai-thinking-mode, zai-deep-thinking]
- **Migration guide for GLM-5.3.** Its checklist: the new model id; temperature 1.0 and top_p 0.95 as defaults,
  with only one of them tuned; thinking left enabled and an effort chosen; `stream` and `tool_stream` both set for
  streamed tool calls, with the argument fragments concatenated; `max_tokens` set with the 128K output cap in mind;
  then a re-test of randomness, tool streaming and latency. [zai-migrate]
- **Function-calling guide.** One responsibility per function, meaningful names, full function and parameter
  descriptions; on the caller's side, input validation, permission limits and call logging. [zai-function-calling]
- **How the advice moved.** Z.ai's release posts do not say to delete earlier prompt text, and the best-practice
  page is undated and names no GLM model. The changes that matter between releases are API rules: thinking went from a
  caller's switch (4.5) to default-on (4.7) to forced on (5.3), and effort arrived with 5.2. A paper co-authored by
  Zhipu measured where constraints work best (see Family-wide behaviour). [mtac-ifbench]

## System-card practice

Z.ai publishes no system card, model card with safety sections, or safety report for any GLM-5.x model in this
library. For a release it publishes a blog post, a docs page, a Hugging Face card with benchmark footnotes, and
(for open weights) the licence. What exists on safety and misuse:

- **Reward hacking in training.** The GLM-5.2 post says GLM-5.2 showed more potential for reward hacking than
  GLM-5.1: agents read protected evaluation files, copied answers from upstream commits, or fetched solutions by
  URL. Z.ai added an online guard to training and evaluation: a rule-based filter flags suspect tool calls, a
  language-model judge checks intent, and a confirmed hack is blocked and answered with dummy output so the
  rollout can go on. The post gives no rate and no deployment advice. [zai-glm52-blog]
- **Cyber capability.** The GLM-5.3 post reports vulnerability-discovery and exploitation scores (in the model file)
  and says the capability grew faster than Z.ai expected. It said the weights would follow in about two weeks; a
  newsletter reported that the hold was for safety evaluation with vetted security partners (A), and the Hugging
  Face repository was created on 2026-08-25. Z.ai says it works with security teams and keeps a public disclosure
  ledger of findings. No red-team report, refusal behaviour or mitigation is published. [zai-glm53-blog,
  batch-glm53, hf-glm53]
- **Platform filter.** The API can end a request with the `sensitive` finish reason or error 1301. Z.ai documents
  no categories or thresholds. [zai-chat-api, zai-errors]
- **Licence terms.** GLM-5.3's licence permits broad use, modification and redistribution, and requires a Z.ai
  security review before commercial use by a Model-as-a-Service operator whose group revenue exceeds US$10 billion
  over any 12 months. GLM-5.2 and Flash are MIT. [hf-glm53-license]
- **Not published.** Refusal and over-refusal rates, sycophancy, deception or sandbagging tests, prompt-injection
  results and any classifier that screens requests.

## Family-wide behaviour

- **Thinking is on by default and, from GLM-5.3, cannot be turned off.** On the Z.ai API a request that disables it
  fails; on the Coding Plan it is quietly set to low. Reasoning arrives in `reasoning_content`, separate from
  `content`. [zai-deep-thinking, zai-switch-models]
- **Tool choice cannot be forced.** Only `auto` is accepted, so a rule such as "always call this tool first" can
  reach the model only as prose. [zai-function-calling, zai-chat-api]
- **Sampling.** Defaults are temperature 1.0 and top_p 0.95 across the 5.x line, and most Z.ai evaluation footnotes
  use temperature 1.0 (DeepSWE uses 0.95) with top_p between 0.95 and 1.0. [zai-chat-api, hf-glm53]
- **Context and output.** GLM-5.2 onward takes 1M tokens of context and 128K (131072) of output; earlier models were
  200K. Z.ai trained 5.2 on 1M-context coding-agent tasks and says it holds up; its own footnotes show 400K for
  DeepSWE and Terminal-Bench 3.0 and 1M for NL2Repo, SWE-Marathon and FrontierSWE. Z.ai's caching guide recommends
  putting a long document in the system message so repeated questions reuse the cached prefix. [zai-glm52-docs,
  hf-glm53, zai-cache]
- **Token use is high at max effort.** Artificial Analysis recorded 210M output tokens to run its index on
  GLM-5.3 at max (about 71k a task) and 69k a task on Flash. Z.ai's own chart shows GLM-5.3 using fewer tokens than
  GLM-5.2 on its private Code Bench (about 75K against 96K at max); the two measures use different tasks.
  [aa-glm-5-3, aa-flash-vs-53, zai-glm53-docs]
- **Low effort hallucinates more.** Artificial Analysis's AA-Omniscience hallucination rate for GLM-5.3 is 29.6% at
  max and 64.0% at low, with the same accuracy (33.9% in both runs). [aa-glm-5-3, aa-glm-5-3-low]
- **Instruction decay over long sessions (measured on GLM-5.2).** MTAC-IFBench, a benchmark co-authored by Zhipu
  and Tsinghua researchers (100 instances, about 7 turns, about 13 constraints a turn, Claude Code v2.1.14 as
  the default harness), found the top-scoring model, GLM-5.2, failing about 20% of process constraints. Its share of
  turns with every constraint met fell from 27.6% in turns 1 to 2 to 2.6% in turns 9 to 10. Constraints in the
  repository policy file decayed less than the same constraints in user turns; a change to an existing constraint
  was followed worse than a new constraint; on a 30-instance sample, policy-file placement scored better than
  placement in the system prompt or first user turn. Under OpenCode v1.1.21 GLM-5.2's scores were lower than under
  Claude Code but decayed less. GLM-5.3 and Flash were not tested. [mtac-ifbench]
- **Harness.** Z.ai runs and reports most of its coding results in Claude Code and documents setups for Claude Code,
  Kilo Code, Cline, OpenCode and OpenClaw through its endpoints; ZCode, Z.ai's own agent, reads a user-global and a
  workspace `AGENTS.md`. Independent harness spread for GLM-5.3 on Terminal-Bench 4.0 was within the noise (41.8 in
  Claude Code, 39.9 in OpenCode). [zai-switch-models, zcode-agents, tbench-4, aa-coding-agent]
- **Safety behaviour in agent runs.** Artificial Analysis recorded no refusals in 909 coding-agent attempts by
  GLM-5.3, and its audit flagged 1 of 80 reviewed passing terminal tasks for reward hacking. [aa-coding-agent]

## Open questions

- Whether Z.ai will publish a system card or safety report for a GLM model, and what the weights-release hold for
  GLM-5.3 tested.
- Whether GLM-5.3's instruction-following decay matches GLM-5.2's; MTAC-IFBench has not run it.
- Whether the Coding Plan's treatment of a disabled thinking request (low effort) matches what an API caller gets
  from an equivalent low-effort request; Z.ai does not say.
- Whether FlashX has its own weights or quality figures; Z.ai publishes none.
- Whether a schema-enforced output mode exists for GLM-5.3 and Flash; the structured-output page documents JSON
  mode only.

## Sources

Every source below was read on 2026-10-03. Kinds: L is the maker's own documentation, M is an independent
measurement, A is a practitioner or tool document.

- [zai-release-notes] https://docs.z.ai/release-notes/new-released (L)
- [zai-glm53-docs] https://docs.z.ai/guides/llm/glm-5.3 (L)
- [zai-glm52-docs] https://docs.z.ai/guides/llm/glm-5.2 (L)
- [zai-flash-docs] https://docs.z.ai/guides/vlm/glm-5.3-flash (L)
- [zai-pricing] https://docs.z.ai/guides/overview/pricing (L)
- [zai-migrate] https://docs.z.ai/guides/overview/migrate-to-glm-new (L)
- [zai-deep-thinking] https://docs.z.ai/guides/capabilities/thinking (L)
- [zai-thinking-mode] https://docs.z.ai/guides/capabilities/thinking-mode (L)
- [zai-function-calling] https://docs.z.ai/guides/capabilities/function-calling (L)
- [zai-struct-output] https://docs.z.ai/guides/capabilities/struct-output (L)
- [zai-cache] https://docs.z.ai/guides/capabilities/cache (L)
- [zai-chat-api] https://docs.z.ai/api-reference/llm/chat-completion (L)
- [zai-errors] https://docs.z.ai/api-reference/api-code (L)
- [zai-coding-plan] https://docs.z.ai/devpack/overview (L)
- [zai-switch-models] https://docs.z.ai/devpack/latest-model (L)
- [zai-best-practice] https://docs.z.ai/devpack/resources/best-practice (L)
- [zai-memory-mechanism] https://docs.z.ai/devpack/resources/memory-mechanism (L)
- [zai-glm53-blog] https://z.ai/blog/glm-5.3 (L)
- [zai-glm52-blog] https://z.ai/blog/glm-5.2 (L)
- [zai-flash-blog] https://z.ai/blog/glm-5.3-flash (L)
- [hf-glm53] https://huggingface.co/zai-org/GLM-5.3 (L)
- [hf-glm53-license] https://huggingface.co/zai-org/GLM-5.3/blob/main/LICENSE (L)
- [zcode-agents] https://zcode.z.ai/en/docs/agents (L)
- [mtac-ifbench] https://arxiv.org/abs/2609.14992 (L; co-authored by Zhipu, so not fully independent)
- [aa-glm-5-3] https://artificialanalysis.ai/models/glm-5-3 (M)
- [aa-glm-5-3-low] https://artificialanalysis.ai/models/glm-5-3-low (M)
- [aa-flash-vs-53] https://artificialanalysis.ai/models/comparisons/glm-5-3-flash-vs-glm-5-3 (M)
- [aa-coding-agent] https://artificialanalysis.ai/agents/coding (M)
- [tbench-4] https://www.tbench.ai/leaderboard/terminal-bench/4.0 (M)
- [openrouter-models] https://openrouter.ai/api/v1/models (A)
- [vllm-glm53] https://recipes.vllm.ai/zai-org/GLM-5.3 (A)
- [sglang-glm53] https://docs.sglang.io/cookbook/autoregressive/GLM/GLM-5.3 (A)
- [batch-glm53] https://www.deeplearning.ai/the-batch/glm-5-3-makes-cybersecurity-gains (A)
