---
last_checked: 2026-10-03
volatility: MONITOR (the makers' guides change at each model release)
sources:
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1
  - https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5
  - https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5
  - https://platform.claude.com/docs/en/build-with-claude/effort
  - https://platform.claude.com/docs/en/build-with-claude/thinking
  - https://platform.claude.com/docs/en/build-with-claude/structured-outputs
  - https://platform.claude.com/docs/en/build-with-claude/prompt-caching
  - https://platform.claude.com/docs/en/build-with-claude/vision
  - https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence
  - https://developers.openai.com/api/docs/guides/latest-model
  - https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6
  - https://developers.openai.com/api/docs/guides/reasoning
  - https://developers.openai.com/api/docs/guides/reasoning-best-practices
  - https://developers.openai.com/api/docs/guides/function-calling
  - https://developers.openai.com/api/docs/guides/structured-outputs
  - https://developers.openai.com/api/docs/guides/prompt-caching
  - https://ai.google.dev/gemini-api/docs/prompting-strategies
  - https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5
  - https://ai.google.dev/gemini-api/docs/thinking
  - https://ai.google.dev/gemini-api/docs/function-calling
  - https://ai.google.dev/gemini-api/docs/long-context
  - https://ai.google.dev/gemini-api/docs/files
  - https://ai.google.dev/gemini-api/docs/image-understanding
  - https://ai.google.dev/gemini-api/docs/latest-model
  - https://web.archive.org/web/20260802003901/https://ai.google.dev/gemini-api/docs/latest-model
  - https://docs.x.ai/developers/model-capabilities/text/reasoning
  - https://docs.x.ai/developers/advanced-api-usage/prompt-caching/best-practices
  - https://api-docs.deepseek.com/guides/thinking_mode
  - https://platform.kimi.ai/docs/guide/prompt-best-practice
  - https://platform.kimi.ai/docs/guide/kimi-k3-quickstart
  - https://platform.kimi.ai/docs/guide/kimi-k3-tool-calling-best-practice
  - https://platform.kimi.ai/docs/guide/use-tool-choice
  - https://platform.kimi.ai/docs/api/models-overview
  - https://www.kimi.ai/blog/kimi-k3
  - https://docs.qwencloud.com/developer-guides/text-generation/thinking
  - https://docs.z.ai/guides/capabilities/thinking-mode
  - https://docs.z.ai/devpack/resources/best-practice
  - https://platform.minimax.io/docs/guides/text-m3-function-call
  - https://docs.mistral.ai/capabilities/completion/prompting_capabilities/
  - https://docs.mistral.ai/capabilities/reasoning/
  - https://research.meta.ai/blog/introducing-muse-spark-1-3
  - https://cursor.com/blog/improved-token-efficiency
  - https://cursor.com/docs/rules.md
  - https://artificialanalysis.ai/models/gpt-6-astra
---

# How to instruct current models

This page collects what the makers of current language models say about how to write instructions for them. It covers system prompts and roles, effort and thinking controls, output format, tools and agents, coding, long inputs, structured output, images, sampling and migration. The page is organised by topic, not by maker. Each topic says where the makers agree, where they differ and where to read more.

The page reports what named sources say. It is not a standard. Most sources are the guides of the makers (class L). A few measured results are marked M. Each guide describes one model on one date. Anthropic says a technique that names a model was measured on that model and needs a new test on another one [cl-bp]. OpenAI offers its GPT-6 prompts as a start to evaluate on the model in use [oa-latest]. This page keeps those limits. Bracketed ids resolve in [Sources](#sources). Every fact was read on 2026-10-03 unless a date is given. The maker pages and model files hold the detail. Each maker README holds the lineage and the API rules. Each model file has one section for each topic below.

**Who publishes what.** Only some makers publish prompt-writing guidance. For the others, the advice below comes from API documents and model cards.

| Maker | Prompting guidance published (as of 2026-10-03) | Detail |
| --- | --- | --- |
| Anthropic | One general page and one guide for each 5-series model. Haiku 4.5 has no guide of its own. | [README](../models/anthropic/README.md#prompting-guides) |
| OpenAI | A guide for GPT-5.6, a guide for GPT-6 written from GPT-6 Astra, a blog post on Astra, reasoning pages, an older o-series page, and the harmony format for gpt-oss. | [README](../models/openai/README.md#prompting-guides) |
| Google | Guidance for the Gemini family: prompt strategies, a 3.5 migration page, thinking, function calling. No guide for one Gemini model. Gemma has format pages. | [README](../models/google/README.md#prompting-guides) |
| Mistral | A general prompting page, a reasoning page and model cards. | [README](../models/mistral/README.md#prompting-guides) |
| Moonshot | A general prompt guide, K3 tool and effort pages, and a launch note with two cautions. | [README](../models/moonshot/README.md#prompting-guides) |
| Alibaba | A general prompt-design page that names no model, and best practices on the model cards. | [README](../models/alibaba/README.md#prompting-guides) |
| Meta | No guide for Muse Spark. API pages and release posts. One guide for Muse Glimmer. | [README](../models/meta/README.md#prompting-guides) |
| xAI | No guide for the 4.x models. A removed 2025 coding guide, caching pages and a reasoning page. | [README](../models/xai/README.md#prompting-guides) |
| DeepSeek, Z.ai, MiniMax | No model prompting guide. API guides for thinking and tools. Z.ai adds a coding-agent page. | [DeepSeek](../models/deepseek/README.md#prompting-guides), [Z.ai](../models/zai/README.md#prompting-guides), [MiniMax](../models/minimax/README.md#prompting-guides) |
| Tencent, Thinking Machines, IFM, Xiaomi, NVIDIA | Model cards and serving documents only. | [README](../models/other/README.md#prompting-guides) |
| Cursor | Guidance for its agent harness. No model guide. | [README](../models/cursor/README.md#prompting-guides) |

## What the makers' guides agree on

1. **The guides ask for a complete brief.** Anthropic suggests a test: would a colleague with minimal context on the task be confused by this prompt [cl-bp]. Mistral asks for prompts that a reader with no context can follow [mi-prompt]. Z.ai frames a task as goal, context, constraints and a done condition [zai-bp]. OpenAI lists success criteria and stop rules in its prompt layout [oa-g56]. Google asks for precise, direct wording [g-prompt]. See [Setting up the prompt](#setting-up-the-prompt).
2. **The guides move toward fewer rules and less emphasis.** Anthropic says forceful wording written for older models now makes tools over-trigger [cl-bp]. OpenAI says leaner prompts scored about 10 to 15 percent higher in its own coding evaluations. OpenAI calls the figure directional [oa-g56]. Google says long techniques built for older models can make a Gemini 3 model over-analyse [g-35]. Cursor removed about 66 percent of its system prompt for the same reason [cur-tok]. The older general pages of Moonshot, Mistral and Alibaba still advise writing the steps out. No source checked those pages against the current models.
3. **Effort or thinking level is the main control for depth.** Every maker with a reasoning model offers one control. Anthropic, Google and Moonshot each say to lower the level first, before prompt text is added, when thinking is too long or tool use is too heavy. Level names do not map across models. See [Reasoning and effort](#reasoning-and-effort).
4. **The guides say the reasoning goes back with the tool results.** Anthropic, OpenAI, Google, xAI, DeepSeek, Moonshot, Z.ai, MiniMax, Mistral and Alibaba each say the earlier reasoning must go back to the model in a tool loop. Some APIs return an error when it is missing. See [Tools and agents](#tools-and-agents).
5. **The guides put unchanging text first.** Anthropic, OpenAI, Google, xAI, Moonshot, MiniMax, Z.ai and Meta each say to put unchanging text first and changing text last. xAI says to never edit earlier messages [x-cache]. See [Long context and retrieval](#long-context-and-retrieval).
6. **Sampling controls are fixed, ignored or removed on reasoning models.** See [Sampling and API parameters](#sampling-and-api-parameters).
7. **The guides prefer schemas to prefill or prose for output shape, and say code still validates.** Google, Alibaba, Z.ai and xAI each tell the reader to validate output in application code. See [Structured output](#structured-output).
8. **The guides favour small, well described tool sets.** OpenAI says fewer than about 20 functions at the start of a turn, as a soft target [oa-fc]. Google says 10 to 20 [g-fc]. See [Tools and agents](#tools-and-agents).
9. **The guides say to test on the user's own tasks after each model change.** Anthropic, OpenAI and Moonshot each say a setting, a prompt or a level from one model does not carry over without a test. See [Migrating from the previous generation](#migrating-from-the-previous-generation).
10. **The guides place hard rules in code, not in the prompt.** Anthropic says a confirmation step for risky actions stays the job of the harness [cl-o55]. OpenAI advises human approval for consequential actions, because its misalignment monitoring runs after the fact [OpenAI GPT-6 Astra file](../models/openai/gpt-6-astra.md#tools-and-agents). Cursor calls its run modes best-effort guardrails, not a security boundary [Cursor README](../models/cursor/README.md#system-card-practice).

## Where the guides differ

| Question | Positions | Section |
| --- | --- | --- |
| How many examples | Anthropic: 3 to 5, relevant and varied [cl-bp]. Google: include examples, but too many cause overfitting [g-prompt]. OpenAI: try none first on reasoning models [oa-rbp]. | [Setting up](#setting-up-the-prompt) |
| Tell the model to think | Anthropic: general instructions often beat a hand-written plan [cl-bp], and "think carefully" lines can go from chat prompts on Opus 5.5 [cl-o55]. Sonnet 5.5 gets the opposite line for JSON tasks [cl-s55]. OpenAI: avoid chain-of-thought prompts on o-series models [oa-rbp]. Google: generally not needed [g-prompt]. | [Reasoning](#reasoning-and-effort) |
| Can thinking be off | Not on Claude Fable 5.1, Fable 5 or Opus 5.5, GPT-6 Astra, Grok 4.5 and later, GLM-5.3 or Kimi K3. Yes on GPT-6 Sol and Luna, MiniMax M3, DeepSeek and the hosted Qwen3.8 models. | [Reasoning](#reasoning-and-effort) |
| Forced tool choice | Removed on three Claude models. Only `auto` on Z.ai and Meta. Not allowed with thinking on DeepSeek and Qwen. Kept elsewhere. | [Tools](#tools-and-agents) |
| Prefilled reply | Rejected by Claude 4.6 and later and by Gemini 3.6 and later. Offered in beta by DeepSeek, as partial mode by Moonshot, and by Mistral. | [Output](#output-format-length-tone) |
| Where the question goes | Anthropic and Google: documents first, question last. Alibaba: instructions and key material at the start or end. Most other makers give no rule. | [Long context](#long-context-and-retrieval) |
| Image before or after text | Anthropic: image first. Google: its own pages disagree. Alibaba: depends on the number of images and questions. | [Images](#images-audio-other-inputs) |
| How far the model acts alone | Some guides push toward action (OpenAI for Astra). Others push toward limits (Moonshot for K3, Anthropic for Opus 5). The direction changed between releases. | [Tools](#tools-and-agents) |

## By topic

### Setting up the prompt

**System prompt and role.** The makers agree on a short role and a clear task in the system prompt.

- Anthropic says even one sentence of role focuses behaviour and tone [cl-bp]. Moonshot says to give the model a role in the system message [km-guide]. Mistral opens its prompts with a role line and says to fold it into the user turn when the developer cannot set a system prompt [mi-prompt]. Google puts role, constraints and output format in the system instruction or at the start of the user prompt [g-prompt].
- OpenAI offers an outline for complex GPT-5.6 prompts: role, personality, goal, success criteria, constraints, tools, output and stop rules. It says detail belongs only where it changes behaviour [oa-g56].
- Role handling differs for open-weight models. The gpt-oss model keeps a fixed identity line in the system message and takes instructions in a developer message. See [gpt-oss-120b](../models/openai/gpt-oss-120b.md#setting-up-the-prompt). Gemma 4 has a system role, which Gemma 3 lacked. See [Gemma 4 31B](../models/google/gemma-4-31b-it.md#setting-up-the-prompt).

**State the goal, the limits and the done condition.** Z.ai names four parts: goal, context, constraints and "done when" [zai-bp]. Mistral asks for hierarchical sections, objective wording and counts supplied as input, because models count words and characters poorly [mi-prompt]. Anthropic says to ask outright for "above and beyond" behaviour, because the model does not infer it from a vague prompt [cl-bp]. Anthropic also says to give the reason behind a rule. Its example is a rule against ellipses that works better when the prompt says a speech engine reads the reply aloud [cl-bp].

**Less emphasis, fewer rules, no contradictions.**

- OpenAI says GPT-5-class models follow the prompt closely, so conflicting rules cause more instability than missing detail. It keeps capital-letter absolutes for true invariants, such as safety rules and required fields [oa-g56].
- Anthropic says Claude Opus 4.5 and 4.6 over-trigger tools on aggressive wording, and advises plainer language [cl-bp].
- Mistral advises decision trees to settle conflicting rules [mi-prompt]. Google's agentic template sets an order for resolving conflicts [g-prompt].
- Anthropic's Fable guides say one short instruction steers most behaviours as well as a list of cases, and that older instruction files are often too prescriptive. See [Fable 5.1](../models/anthropic/claude-fable-5-1.md#setting-up-the-prompt).
- Moonshot and Mistral still advise writing the steps out [km-guide] [mi-prompt]. OpenAI says to describe the destination and to state decision criteria where the right value is implicit [oa-g56]. These positions differ, and each applies to its own models.

**How literally the model reads.** The makers describe different styles. Each statement is about one model on one date.

| Model | What the maker says | Source |
| --- | --- | --- |
| Claude Sonnet 5 | Reads literally. Does not carry a rule from one item to the next. State the scope of each rule. | [cl-s5] |
| Claude Opus 5 | Can add steps nobody asked for. A scope block tells it to deliver what was asked. | [cl-o5] |
| Claude Sonnet 5.5 | Adds supporting files at every effort level. At low and medium it can stop to check in. | [cl-s55] |
| GPT-5.6 family | Works best when the prompt states the outcome, the constraints, the evidence and the completion bar, and leaves the path to the model. | [oa-g56] |
| GPT-6 Astra | Asks a question more often when the answer could change the result. More sensitive to files in context. | [oa-latest] |
| Muse Spark 1.3 | Asks clarifying questions, confirms before consequential actions, and adapts to a stated wish for updates or silence. | [meta-13] |
| Kimi K3 | May decide for the user on minor problems or unclear intent. Moonshot suggests explicit limits in the system prompt or AGENTS.md. | [Kimi K3](../models/moonshot/kimi-k3.md#setting-up-the-prompt) |
| GLM-5.3 | Trained to own substantial work end to end. | [GLM-5.3](../models/zai/glm-5.3.md#setting-up-the-prompt) |
| Gemini 3.8 Flash | Takes small reasoning steps and checks its own work. Google says to lower the effort for everyday tasks to use fewer tokens. | [Gemini 3.8 Flash](../models/google/gemini-3.8-flash.md#setting-up-the-prompt) |
| Grok 4.7 | No source says how literally it reads. | [Grok 4.7](../models/xai/grok-4.7.md#setting-up-the-prompt) |

The same fix can push two models in opposite directions. OpenAI wrote prompts that lean toward action for Astra, and shorter prompts with fewer approval lines for GPT-5.6 [oa-latest] [oa-g56]. A line that fixes one model can break another.

**Structure and delimiters.** Most makers say to separate instructions, context, examples and input with one consistent style.

- Anthropic: XML tags with consistent names, nested where the content nests [cl-bp]. Google: XML-style tags or Markdown headings, one style in a prompt [g-prompt]. Mistral: Markdown or XML-style tags [mi-prompt]. Moonshot: triple quotes, XML tags or headings [km-guide]. OpenAI, for reasoning models: Markdown, XML tags and section titles [oa-rbp].
- Alibaba names a six-part checklist with `#Name#` headings and rare separators such as `###` [Alibaba README](../models/alibaba/README.md#prompting-guides).
- Meta, MiniMax, DeepSeek, Z.ai, NVIDIA and xAI (for 4.x) give no preference.

**Examples.**

- Anthropic says examples steer format and tone well. It advises 3 to 5, in `<example>` tags [cl-bp].
- Google says to include few-shot examples with one shared format, and warns that too many cause overfitting [g-prompt].
- Mistral shows examples as made-up user and assistant turns [mi-prompt]. Moonshot says to show examples of the wanted output [km-guide].
- OpenAI says reasoning models often need none, and advises a zero-shot try first [oa-rbp]. Its function-calling guide notes that examples may hurt reasoning models [oa-fc].

**Untrusted text inside the prompt.** Anthropic gives one pattern for text a user pastes. The application wraps each block in tags that both carry the same short random id. The system prompt says to follow instructions inside the tags only where the user's own message asks. Anthropic calls this one guardrail among several, because the tags are plain text that an attacker can copy [cl-o55]. Google marks the user material as context and the request as task, and says the model treats context as data [g-prompt].

**Instruction files and skill files.** OpenAI says GPT-6 Astra follows long instructions better and reacts more to what is in context. An unclear or conflicting line in a skill file can make it pause and block work. OpenAI advises a line that puts the user's instructions above a skill [oa-latest]. Cursor says to keep each rule under 500 lines [cur-rules]. Z.ai suggests a main file under about 200 lines with checkable rules [Z.ai README](../models/zai/README.md#prompting-guides). For more see [writing-for-models.md](writing-for-models.md) and [cross-harness.md](../harnesses/cross-harness.md).

### Reasoning and effort

**The controls.** Every maker with a current reasoning model offers a control. The values, the defaults and the option to turn thinking off differ.

| Maker (models) | Control and values | Default | Thinking off |
| --- | --- | --- | --- |
| Anthropic (Fable 5.1, Fable 5, Opus 5.5, Sonnet 5.5, Opus 5, Sonnet 5) | `output_config.effort`: low, medium, high, xhigh, max [cl-effort] | high. Opus 5.5: medium. | No on Fable 5.1, Fable 5 and Opus 5.5. Sonnet 5.5 has `between_tools`. Opus 5 allows it up to high. Sonnet 5 allows it [cl-think]. |
| Anthropic (Haiku 4.5) | No effort. Manual thinking budget of at least 1,024 tokens | off | Yes |
| OpenAI (GPT-6, GPT-5.6) | none, minimal, low, medium, high, xhigh, max. Each model accepts a subset [oa-reason] | medium on GPT-6 Sol, Luna and 6.1 Sol | Astra rejects `none`. 6.1 Sol rejects `none` and `minimal`. |
| OpenAI (gpt-oss) | `Reasoning: low`, `medium` or `high` in the system message | medium | No |
| Google (Gemini 3.x) | `thinking_level`: minimal, low, medium, high [g-think] | medium on 3.7 and 3.8 Flash, high on 3.1 Pro, minimal on 3.5 Flash-Lite | Not offered. 3.7 and 3.8 Flash reject `minimal`. |
| xAI (Grok 4.5 and later) | low, medium, high, and xhigh from Grok 4.6 [x-reason] | high | No |
| DeepSeek (V4.1-Flash, V4-Pro) | thinking switch, and effort low, high or max [ds-think] | on, at high | Yes |
| Moonshot (K3) | `reasoning_effort`: low, high, max [km-k3] | max | No |
| Z.ai (GLM-5.3) | `reasoning_effort`: low, high, max | max | No. A request to disable fails on the Z.ai API. |
| Alibaba (hosted Qwen3.8) | `reasoning_effort`: low, medium, xhigh, or a thinking budget [qw-think] | xhigh | Yes on most hosted models |
| Mistral (Small 4, Medium 3.5) | `reasoning_effort`: none or high [mi-reason] | not stated | Yes |
| Meta (Muse Spark 1.3) | minimal, low, medium, high, xhigh, and max on the standard tier [Muse Spark 1.3](../models/meta/muse-spark-1.3.md#reasoning-and-effort) | the model chooses | No. `none` returns an error. |
| MiniMax (M3) | `thinking`: adaptive or disabled. No effort field. | depends on the endpoint | Yes |

Other open-weight models use their own controls. Inkling takes a number from 0 to below 1 ([file](../models/other/inkling.md#reasoning-and-effort)). Nemotron 3 Ultra has three modes and a budget ([file](../models/other/nemotron-3-ultra.md#reasoning-and-effort)). gpt-oss and Muse Glimmer take a line in the system prompt ([gpt-oss](../models/openai/gpt-oss-120b.md#reasoning-and-effort), [Glimmer](../models/meta/muse-glimmer-30b.md#reasoning-and-effort)). Gemma 4 has an on and off switch only ([file](../models/google/gemma-4-31b-it.md#reasoning-and-effort)).

**Where the makers agree.**

- **Level names do not map between models.** Anthropic repeats this in its guides and asks for a new sweep on each move to a new model [cl-effort]. OpenAI's Codex documentation says efforts do not map exactly between generations [GPT-6 Astra](../models/openai/gpt-6-astra.md#reasoning-and-effort). Anthropic's default differs by model [cl-effort]. Google changed its default from high to medium with Gemini 3.5 [g-35].
- **Effort is a tuning control, not the first fix for quality.** OpenAI calls it "a tuning knob, not the primary way to recover quality" [oa-reason]. It asks first whether the prompt lacks a success criterion, a dependency rule, a tool rule or a check [oa-g56].
- **To reduce thinking, lower the level.** Anthropic says a prompt that asks the model to think less does not reliably reduce thinking on Sonnet 5.5, and lowering effort does [cl-s55]. Google gives the same first fix for too many tool calls, and a system instruction only if the problem stays [g-35]. Moonshot gives it for slow reasoning [km-k3].
- **Start from the default or from medium, then test.** Anthropic starts at the default level, and at medium for well-specified agentic coding on Sonnet 5.5 [cl-s55]. OpenAI tests the old setting and one level lower [oa-g56]. Google recommends medium for most tasks [g-35]. Z.ai recommends max for coding [GLM-5.3](../models/zai/glm-5.3.md#reasoning-and-effort).
- **Thinking tokens share the output limit.** Anthropic calls `max_tokens` a hard limit on thinking plus reply [cl-effort]. OpenAI advises reserving at least 25,000 tokens for reasoning and output while testing [oa-reason]. Google says a small cap can end a reply before any answer, with the thinking still billed [g-think]. Moonshot, MiniMax, Z.ai and Meta say the same on their pages. See the [Moonshot](../models/moonshot/README.md#family-wide-behaviour), [MiniMax](../models/minimax/README.md#family-wide-behaviour), [Z.ai](../models/zai/README.md#api-surface) and [Meta](../models/meta/README.md#family-wide-behaviour) READMEs.
- **Visibility differs.** Anthropic omits thinking text by default and can return a summary [cl-think]. OpenAI returns summaries on request and never the raw reasoning [oa-reason]. Google returns summaries only when asked [g-think]. DeepSeek, Moonshot, Z.ai and Alibaba return reasoning in a separate field. OpenAI says the raw reasoning of gpt-oss is not for end users ([file](../models/openai/gpt-oss-120b.md#reasoning-and-effort)).

**What the makers advise against.**

- Anthropic says not to ask for the reasoning in the reply on five Claude models. Its classifiers can decline such a request with `reasoning_extraction`. This covers prompts, instruction files, tool descriptions and schema fields that ask for reasoning [cl-so] [Anthropic README](../models/anthropic/README.md#family-wide-behaviour).
- OpenAI advises against chain-of-thought prompts for o-series models. It says "think step by step" may not help and can sometimes hinder [oa-rbp]. No OpenAI page read says whether this still holds for GPT-6.
- OpenAI advises against prescribing every step. It says to give the task, the constraints and the output format [oa-reason].
- Anthropic advises against changing the top-level effort in a cached conversation, because it restarts the cache. Per-message effort keeps the cache on Fable 5.1, Opus 5.5, Opus 5 and Sonnet 5.5 [cl-effort]. OpenAI offers `configuration_update` items for the same purpose [oa-reason]. Moonshot says to set effort before the conversation starts [km-tools].
- Anthropic advises against carrying a prompt line across a model change without a test. It says "think carefully" lines in chat prompts can go on Opus 5.5, and removing one made replies start sooner with no clear loss [cl-o55]. For Sonnet 5.5 Anthropic adds an end-of-prompt line, "Think the problem through before you answer", for tasks that need working out but return JSON [cl-s55].
- Some open-weight makers write the effort setting as text in the prompt. Qwen, DeepSeek and Moonshot do so. See [Qwen3.8-27B](../models/alibaba/qwen3.8-27b.md#reasoning-and-effort), [DeepSeek V4.1-Flash](../models/deepseek/deepseek-flash.md#reasoning-and-effort) and [Kimi K3](../models/moonshot/kimi-k3.md#setting-up-the-prompt).

**Cost does not rise in step with effort.** Anthropic's own study found that Opus 5.5 at its default solved 92.8 percent of a coding subset, against 92.3 percent for Fable 5.1 at its default. Opus 5.5 cost about a fifth as much for each solved task. On a research benchmark, Fable 5.1 at low effort scored 10 points above Sonnet 5, at about four times the cost for each task, because it ran a longer research loop [cl-optim]. Artificial Analysis measured GPT-6 Astra on its Intelligence Index (v4.3.2) at 46 with low effort, at $0.82 for each index task and 10 million output tokens for the whole run. At max effort it measured 53, at $3.26 for each task and 60 million tokens (M) [aa-astra]. Anthropic advises comparing the cost for each completed task on the reader's own traffic [cl-optim].

### Output: format, length, tone

**Defaults move between releases.** The makers say so in their guides.

- Anthropic: Fable 5.1 uses bold, headers and lists less than earlier Claude models, so anti-formatting rules written for them can strip structure the content needs [cl-f51]. Opus 5 replies run longer, and changing effort does not reliably shorten them [cl-o5]. The latest Claude models write more tersely and may skip a summary after tool work, so a summary must be requested [cl-bp].
- OpenAI: GPT-5.6 is terser than GPT-5.5 by default, and `text.verbosity` sets the default detail level [oa-g56]. GPT-6 Astra leans toward lists, tables and Markdown and repeats phrases. OpenAI publishes prompts for plain paragraphs and for a list of stock phrases to avoid, written from Astra [oa-latest].
- Google: Gemini 3 answers directly and efficiently, and a chatty or detailed answer must be requested [g-prompt]. Its example asks for "a friendly, talkative assistant" [g-35].

**Control by prompt.**

- Anthropic says to state what to do, not what to avoid. It says to match the prompt style to the wanted output style, and to mark output sections with XML tags [cl-bp]. It adds that the latest models default to LaTeX for maths, so plain text must be requested if wanted [cl-bp].
- OpenAI says to describe tone as concrete writing choices, not adjectives such as friendly. For short answers it says to list what must stay in the answer [oa-g56].
- Moonshot says to ask for length in paragraphs or bullets, because word counts are imprecise [km-guide]. Mistral says to supply counts as input and to ask only for the output needed [mi-prompt].
- Anthropic's Opus 5 guide says a brevity instruction should repeat in a short block near the end of a long prompt [cl-o5].
- For prose style, Anthropic's Fable 5.1 guide defines "mannered prose" with an example pair and puts the definition in a user message [cl-f51].
- With sampling controls removed, Anthropic's Sonnet 5 guide says to use system-prompt instructions to guide tone and variety [cl-s5].

**Prefill and stop sequences.**

- Anthropic rejects a prefilled assistant turn on Claude 4.6 and later. It lists replacements: structured outputs or an enum tool for format and classification, a direct instruction for preambles, and the user turn for continuations and reminders [cl-bp]. Haiku 4.5 still accepts prefill when thinking is off ([file](../models/anthropic/claude-haiku-4-5.md#output-format-length-tone)).
- Google returns an error for a request whose last turn is a model turn, from Gemini 3.6 Flash on, and says this holds for future releases [g-latest-arch] [g-latest].
- DeepSeek offers prefix completion in beta, Moonshot offers partial mode and Mistral lists prefix completion. Inkling does not support prefill ([file](../models/other/inkling.md#output-format-length-tone)).
- xAI returns an error for `stop` on reasoning models [x-reason]. Z.ai supports one stop word ([README](../models/zai/README.md#api-surface)).

**Progress notes and narration.** Anthropic says Fable 5.1 writes fewer user-facing updates, and Opus 5 narrates readily. On Opus 5.5 and Sonnet 5.5 the notes between tool calls arrive as thinking blocks that are empty at the default display. A client that shows only text looks silent [cl-f51] [cl-o55] [cl-s55]. OpenAI suggests a short preamble before tool use and sparse updates at phase changes [oa-g56]. Meta says Muse Spark 1.3 adapts to a stated wish for frequent updates or silent work [meta-13].

### Tools and agents

**Definitions.**

- OpenAI says a tool description should state its purpose, when to call it, what it returns and how it fails. It advises exposing only the tools the task needs [oa-g56]. It advises enums, removal of arguments the code already knows, and merging functions that are always called together [oa-fc].
- Google asks for clear names without spaces, strongly typed parameters, validation before execution and error handling [g-fc]. Z.ai asks for one responsibility for each function ([README](../models/zai/README.md#prompting-guides)).
- Set sizes differ. OpenAI: fewer than about 20 at the start of a turn, as a soft target, with tool search for more [oa-fc]. Google: 10 to 20 [g-fc]. Alibaba: no more than 20, with a routing layer for more ([README](../models/alibaba/README.md#api-surface)). Meta: namespaces of fewer than 10 functions ([README](../models/meta/README.md#api-surface)). Moonshot: a search tool and a few core tools, with dynamic loading of the rest [km-tools].
- Wording matters. Anthropic says the latest models act on explicit direction. "Can you suggest some changes" can return suggestions, and "make these edits" returns edits [cl-bp]. OpenAI says, in its GPT-6 prompts, to read "can you" and "help me" requests as instructions to act [oa-latest]. Anthropic's Sonnet 5.5 guide says to remove lines such as "minimize tool calls" if search is wanted [cl-s55].

**Parallel calls.**

| Maker | What the source says |
| --- | --- |
| Anthropic | Parallel by default. A prompt block pushes toward all-parallel or toward sequential [cl-bp]. Fable 5.1 may issue one call a turn in coding loops, and Anthropic gives a fix [cl-f51]. |
| OpenAI | Independent reads in parallel, dependent steps in sequence [oa-g56]. `parallel_tool_calls: false` allows at most one call [oa-fc]. |
| Google | Parallel and chained calls are supported. Each function response needs the call id and name, with one response for each call [g-35]. |
| xAI, Mistral, Meta | On by default. Meta says every result of a batch must return before the next request. See the maker READMEs. |
| Muse Glimmer | The guide says one call a turn. The vLLM recipe says several can arrive. See [the file](../models/meta/muse-glimmer-30b.md#tools-and-agents). |

**Forced tool choice.** Anthropic rejects `tool_choice` of type `any` or `tool` on Claude Fable 5.1, Opus 5.5 and Sonnet 5.5. It says a forced call would skip thinking. It names `strict: true` on tools or structured outputs, plus a prompt that says when a tool applies [cl-think] [cl-f51-new]. Z.ai accepts only `auto`. Qwen and DeepSeek accept `auto` and `none` with thinking on (see the [Alibaba](../models/alibaba/README.md#family-wide-behaviour) and [DeepSeek](../models/deepseek/README.md#family-wide-behaviour) READMEs). Moonshot K3 accepts `required` [km-k3], and a named function returns HTTP 400 with thinking on [km-choice]. OpenAI offers `allowed_tools` to restrict the callable set without changing the tool list, which keeps the cache [oa-fc]. See the [Z.ai](../models/zai/README.md#family-wide-behaviour) and [Moonshot](../models/moonshot/README.md#family-wide-behaviour) pages.

**Reasoning in tool loops.** All nine makers in the table below say the same thing.

| Maker | What goes back | What the source says happens otherwise |
| --- | --- | --- |
| Anthropic | Thinking blocks, unchanged | Blocks are bound to the conversation. For accounts created on or after 2026-08-31 a replay after an edit returns an error [cl-think]. |
| OpenAI | Reasoning items from the last function call, strongly recommended | The model continues its reasoning less well and uses more tokens [oa-reason]. |
| Google | The full history, thought signatures included | Reasoning does not carry over [g-think]. |
| DeepSeek | `reasoning_content` of every earlier assistant message when the request has tools | HTTP 400 [ds-think]. |
| Moonshot | The whole assistant message, reasoning and tool calls [km-k3] | Moonshot says quality can become unstable [km-blog]. |
| Z.ai | Earlier `reasoning_content`, unedited and in order, for preserved thinking | Performance may degrade and cache hits fall [zai-think]. |
| MiniMax | The full response, thinking included | The chain of reasoning breaks [mm-fc]. |
| Mistral | The full assistant message, including the thinking chunk | Mistral says performance degrades [mi-reason]. |
| Alibaba | `reasoning_content`, or `preserve_thinking` | Accuracy falls [qw-think]. |

Alibaba's advice reversed. Qwen3 and Qwen3.5 said to leave earlier thinking out. Qwen3.8 keeps it by default in the open-weight templates and on some hosted models ([README](../models/alibaba/README.md#prompting-guides)). Gemma 4 differs. Google says the thoughts of earlier turns are removed, except in a turn with tool calls ([file](../models/google/gemma-4-31b-it.md#reasoning-and-effort)).

**Autonomy and persistence.** The makers publish opposite fixes, because their models lean in opposite directions.

- Anthropic gives an unattended-run block for Fable 5.1. It says the user is not watching, to proceed on reversible actions and to stop only for destructive actions or real scope changes [cl-f51]. For Opus 5.5 it advises treating a text-only end of turn as a report, not as completion, and keeping a checklist the model updates [cl-o55].
- OpenAI proposes one short policy for GPT-5.6: report on review requests, make in-scope local edits without asking, and confirm external writes, destructive steps and purchases [oa-g56]. For Astra it supplies paragraphs that push toward acting [oa-latest].
- Google's agentic template covers risk assessment, persistence with a retry limit, and not acting before the reasoning is done [g-prompt].
- Moonshot suggests explicit limits for K3 in the system prompt or AGENTS.md [km-blog].
- Moonshot also gives a fix for repeated calls. The client counts identical consecutive calls and adds a reminder to the system prompt after 3 repeats, and a stronger one after 5 and 8 ([README](../models/moonshot/README.md#prompting-guides)).

**Context management.**

- Compaction. OpenAI suggests compaction after milestones and treats compacted items as opaque [oa-g56]. xAI offers a compact endpoint for long agent loops ([README](../models/xai/README.md#prompting-guides)). Anthropic gives a six-point summary instruction for client-side compaction and says to keep history append-only [cl-f51]. See [long-context-and-compaction.md](long-context-and-compaction.md).
- Context awareness. Anthropic says models that track their remaining window, such as Sonnet 5 and Haiku 4.5, may wrap up early unless the prompt says the harness compacts or saves state [cl-bp]. Sonnet 5.5 can read a token countdown after every tool result as an injection [cl-s55].
- Keep user words out of tool results. Anthropic says to never put user text inside a `tool_result` block, and to deliver mid-turn user input as a user turn [cl-s55].

**Subagents.** Anthropic says Opus 5 delegates readily, and gives an instruction to delegate only large, independent work [cl-o5]. OpenAI says Astra delegates less than may be wanted, and gives a prompt to delegate when parallel work helps [oa-latest]. OpenAI's multi-agent beta suits independent workstreams and adds tokens ([README](../models/openai/README.md#api-surface)). Cursor removed prompting that pushed subagents for exploration, because models learned the habit in training [cur-tok].

**Computer use and untrusted content.** Google calls its computer-use tool a preview, advises a sandboxed machine and supervision, and offers an opt-in scan for hidden instructions ([README](../models/google/README.md#tools-and-agents)). OpenAI recommends the code route (a script for a browser library) for Astra ([file](../models/openai/gpt-6-astra.md#tools-and-agents)). Anthropic says to keep untrusted content out of records an agent searches, because it acts on what it finds [cl-o55]. Meta recommends strict tool allowlists and workspace isolation ([README](../models/meta/README.md#system-card-practice)).

### Coding

Much of the current guidance is about coding. Most of it repeats the sections above. This section lists the points that are specific to coding.

- **Checks.** OpenAI advises giving the model tools that can validate its output, and saying which check counts. Its example list is targeted tests, type or lint checks, a build and a smoke test, plus an explanation when a check cannot run [oa-g56]. Anthropic's Sonnet 5.5 guide gives a paragraph. It says to run a real check before saying done, that a syntax-only check does not count, and to install declared dependencies with the project's own manager [cl-s55]. Z.ai counts the working directory, the permissions and the runnable test commands as part of the task [zai-bp].
- **Instructions that repeat what the model does alone.** Anthropic says Opus 5 verifies unprompted, and that an instruction such as "include a final verification step" causes over-verification [cl-o5]. OpenAI says Astra tests on its own, so older run-the-tests lines cause redundant testing. It supplies a testing prompt sized to the change [oa-latest].
- **Bounds.** Anthropic's guides give scope paragraphs for Opus 5, Sonnet 5.5 and Fable 5.1 [cl-o5] [cl-s55] [cl-f51]. Z.ai suggests: follow the repository standards, add no dependencies, change no API contracts, make no commits unprompted, then build, lint and test and report ([GLM-5.2](../models/zai/glm-5.2.md#coding)).
- **Review prompts are read literally.** Anthropic says a prompt such as "only report high-severity issues" can lower recall on Sonnet 5, because the model finds the bug and then withholds it. Anthropic advises asking for every finding with confidence and severity, and filtering in a second step [cl-s5].
- **Frontend work.** Anthropic says a generic counter-instruction such as "avoid a generic AI look" swaps one default for another. It says to name specific patterns or give a concrete specification [cl-o55]. OpenAI lists: keep existing design tokens, add no unrequested features or decoration, keep responsive behaviour, and render and inspect the result [oa-g56].
- **Harness and instruction files.** Moonshot says Kimi Code is the framework K3 works best with [Kimi K3](../models/moonshot/kimi-k3.md#coding). Anthropic, Mistral, Meta, xAI and Cursor each describe their own format for project instructions. See [cross-harness.md](../harnesses/cross-harness.md). Scores of one model differ by harness. See [DeepSeek V4.1-Flash](../models/deepseek/deepseek-flash.md#coding).
- **Safeguards can stop benign work.** Anthropic names three triggers on Fable 5.1: compile-check phrasing, lesser-known languages without documentation, and base64 in tool output ([file](../models/anthropic/claude-fable-5-1.md#coding)). OpenAI asks applications to send a stable `safety_identifier`, and says safeguards can interrupt legitimate dual-use work ([README](../models/openai/README.md#system-card-practice)).

### Long context and retrieval

**Window sizes.** Most current flagship models list a window of about one million tokens. Examples are the Claude 5 series, GPT-6, Gemini 3.x, Kimi K3, Muse Spark and GLM-5.3. Exceptions include Mistral at 256k, Grok 4.7 at 500k, Claude Haiku 4.5 at 200k and gpt-oss at 131,072. The card block at the top of each model file holds the number and its source.

**Placement.**

- Anthropic says to put long documents first and the question last. In its tests, ending with the query improved quality by up to 30 percent on multi-document input [cl-bp].
- Google says the same: supply all context first, and put the instruction at the end [g-prompt] [g-long].
- Anthropic adds source metadata on each document, and a request to quote the relevant passages before the answer [cl-bp].
- Alibaba puts instructions and key reference material at the start or end, because material in the middle may get less attention ([README](../models/alibaba/README.md#prompting-guides)).
- Z.ai puts a long document in the system message so repeated questions reuse the cache ([README](../models/zai/README.md#family-wide-behaviour)).
- OpenAI, xAI, Meta, DeepSeek, MiniMax and Moonshot give no placement rule for answer quality. Several give one for caching.

**Grounding.** Google offers a strict-grounding clause: answer only from the supplied context, do not infer, and say when the context lacks the answer [g-prompt]. OpenAI advises one broad search first, more retrieval only for a missing fact, citations only to retrieved sources, and inference labelled as such [oa-g56].

**Accuracy at length.** Google says single-fact retrieval can reach about 99 percent, and accuracy drops when several facts must be found. It says tokens that are not needed are best left out [g-long]. Other makers publish long-context results of their own. See the model files.

**Caching.** All the makers in the table cache a stable prefix. The details differ and change often.

| Maker | Minimum prefix | Read price against input | Notes |
| --- | --- | --- | --- |
| Anthropic | 512 tokens on Fable 5.1, Fable 5, Opus 5.5, Opus 5 and Sonnet 5.5. 1,024 on Sonnet 5. | 0.1 times, and less on Fable 5.1 and Opus 5.5 | A breakpoint looks back at most 20 blocks [cl-cache]. |
| OpenAI | 1,024 tokens from GPT-5.6 | 0.1 times, and 0.05 on GPT-6.1 Sol | Writes cost 1.25 times the input rate [oa-cache]. |
| xAI | Automatic | See the README | Send a conversation id. Never edit, remove or reorder earlier messages [x-cache]. |
| Google | 4,096 for implicit caching on 3.1 Pro and 3.5 to 3.8 Flash | One tenth | Put shared content first ([README](../models/google/README.md#long-context-and-retrieval)). |

For the other makers, see the maker pages. For the mechanism, for what breaks a cache in an agent loop and for how to check, see [prompt-caching.md](prompt-caching.md). Moonshot says to keep timestamps and random ids out of the prefix ([README](../models/moonshot/README.md#family-wide-behaviour)).

### Structured output

| Maker | What the source says |
| --- | --- |
| Anthropic | `output_config.format` constrains output to a JSON schema. `strict: true` constrains tool inputs. No recursive schemas. `additionalProperties` must be false. A refusal or a `max_tokens` stop can break the schema [cl-so]. |
| OpenAI | Structured Outputs is preferred to JSON mode. JSON mode gives valid JSON without schema adherence. A refusal appears as an explicit item [oa-so]. |
| Google | A JSON Schema subset. Google advises clear descriptions and validation, because valid JSON can still be wrong ([README](../models/google/README.md#structured-output)). |
| Mistral | JSON mode gives valid JSON, but the prompt must still ask for JSON and describe the format. Custom schemas are recommended ([README](../models/mistral/README.md#family-wide-behaviour)). |
| Moonshot | `json_schema` with `strict: true`. Parse only `content` ([README](../models/moonshot/README.md#family-wide-behaviour)). |
| DeepSeek | JSON mode only. The prompt must say json and show the shape. Leave room in `max_tokens` ([README](../models/deepseek/README.md#prompting-guides)). |
| Alibaba | JSON Object needs the word JSON in a message. Schema mode on selected models. Leave `max_tokens` unset, because truncation breaks the JSON ([README](../models/alibaba/README.md#api-surface)). |
| Z.ai | JSON mode only. The schema goes in the system message and the code validates ([README](../models/zai/README.md#api-surface)). |
| Meta, xAI | `json_schema` constrains decoding. See the READMEs for the limits. |
| MiniMax | No JSON mode or schema field is documented for M3 ([file](../models/minimax/MiniMax-M3.md#structured-output)). |

Points that repeat across makers:

- **Validation in code.** Google, Alibaba, Z.ai and xAI each say to check output against the schema in application code.
- **Room for thinking.** Thinking tokens count toward the output limit. A small `max_tokens` can end the reply inside the reasoning and break the schema. Anthropic says to treat a response with `stop_reason` of `max_tokens` as failed, even if the JSON parses [cl-s55].
- **Working lost to a schema.** Anthropic says Sonnet 5.5 often answers a reasoning task without thinking when the reply must be JSON only. Its fixes are the "Think the problem through" line, a higher effort, and parsing the last JSON value in the text [cl-s55].
- **Reasoning fields.** Anthropic says a property that asks for the model's reasoning can draw a `reasoning_extraction` refusal [cl-so].
- **Serving support.** An NVIDIA serving recipe warns that JSON-constrained output with reasoning on can return malformed JSON on one runtime ([Nemotron 3 Ultra](../models/other/nemotron-3-ultra.md#structured-output)).

### Images, audio, other inputs

**Order.** Anthropic says Claude works best when images come before text [cl-vision]. Google's pages disagree. The image-understanding page says to put the text before a single image. The multimodal prompting page says to put the image first [g-img] [g-files]. Moonshot's benchmark runs put images before text, and the Amazon Bedrock page for K3 says the best order depends on the prompt ([Kimi K3](../models/moonshot/kimi-k3.md#images-audio-other-inputs)). Alibaba says to put the text first when one question covers many images, and the image first when many questions cover one image ([README](../models/alibaba/README.md#prompting-guides)). Meta says the model does not process images attached to roles other than user ([README](../models/meta/README.md#family-wide-behaviour)).

**Resolution and cost.** Anthropic says Claude 4.7 and later models see up to 2,576 pixels on the long edge and 4,784 visual tokens, and other models 1,568 pixels and 1,568 visual tokens [cl-vision]. OpenAI offers detail levels low, high, original and auto, and advises `original` for dense, small-text or coordinate-sensitive images ([GPT-6 Astra](../models/openai/gpt-6-astra.md#images-audio-other-inputs)). Google sets media resolution for each item ([README](../models/google/README.md#images-audio-video-documents)). Alibaba and Moonshot say larger input costs time and may not improve understanding ([Alibaba](../models/alibaba/README.md#api-surface), [Moonshot](../models/moonshot/README.md#family-wide-behaviour)).

**Dense images.** Anthropic says crop, zoom or code tools add accuracy on dense charts and technical drawings, and that on charts tools help more than higher effort. It suggests a crop tool, or a container with image libraries, and publishes a recipe [cl-o55] [cl-s55]. Meta advises asking for one output shape and listing the objects when asking for coordinates on a 0 to 1000 grid ([README](../models/meta/README.md#family-wide-behaviour)).

**Audio and video.** Support differs by model. Gemini accepts text, image, video, audio and PDF in one request, and Google offers static and agentic video modes ([Gemini 3.8 Flash](../models/google/gemini-3.8-flash.md#images-audio-other-inputs)). MiniMax M3 takes image and video. Xiaomi MiMo takes audio and video. Meta says audio in Muse Spark 1.3 is weaker than in 1.2 ([Muse Spark 1.3](../models/meta/muse-spark-1.3.md#images-audio-other-inputs)). The Claude, GPT-6, Grok 4.7, DeepSeek V4.1-Flash and Mistral models checked here take text and images only.

**Known weak spots.** OpenAI lists specialised medical images, non-Latin text, rotated text, panoramic and fisheye images, approximate counting and precise spatial localisation ([GPT-6 Astra](../models/openai/gpt-6-astra.md#images-audio-other-inputs)). Anthropic says Claude counts approximately and cannot name people in images ([README](../models/anthropic/README.md#api-surface)). Google says image segmentation is not supported in Gemini 3.x ([README](../models/google/README.md#images-audio-video-documents)).

### Sampling and API parameters

| Maker | Rule for reasoning models |
| --- | --- |
| Anthropic (5-series) | A non-default `temperature`, `top_p` or `top_k` returns HTTP 400 on every request [cl-think]. Haiku 4.5 accepts `temperature` or `top_p`, not both. |
| OpenAI (GPT-6) | Remove `temperature`, `top_p` and `top_logprobs` when effort is not `none` [oa-latest]. Astra and 6.1 Sol have no `none`. |
| Google (Gemini 3.x) | Leave the defaults. From 3.6 Flash the parameters are ignored, and Google says an error will follow in later models [g-latest-arch] [g-prompt]. |
| xAI | `presencePenalty`, `frequencyPenalty` and `stop` return an error [x-reason]. |
| DeepSeek | In thinking mode `temperature` and the penalties are ignored. A `top_p` below 0.95 is raised [ds-think]. |
| Moonshot (K3) | Temperature 1.0 and `top_p` 0.95 are fixed. Other values return an error [km-params]. |
| Z.ai (GLM-5.3) | Defaults 1.0 and 0.95. Tune one, not both ([README](../models/zai/README.md#api-surface)). |
| MiniMax | Temperature 1.0 is recommended. Penalties are ignored ([README](../models/minimax/README.md#api-surface)). |
| Mistral | Temperature 0.0 to 0.7, and `temperature` or `top_p`, not both ([README](../models/mistral/README.md#api-surface)). |
| Meta (Muse Spark) | Defaults of 1.0. `temperature` or `top_p`, not both ([README](../models/meta/README.md#api-surface)). |
| Alibaba (open weights) | Thinking mode: temperature 1.0, `top_p` 0.95, `top_k` 20. Hosted Flash defaults to 0.6 ([README](../models/alibaba/README.md#prompting-guides)). |

The pattern: closed APIs reject or ignore sampling controls, and open-weight makers publish one recommended setting, usually temperature 1.0 and `top_p` 0.95. Where sampling gave variety, Anthropic moves variety into the prompt [cl-s5]. For repeatable output, Google points to a system instruction with explicit rules ([README](../models/google/README.md#sampling-and-api-parameters)). Other parameters follow a similar pattern. Logprobs are unsupported on several APIs, and `n` is fixed at 1 on some.

### Migrating from the previous generation

**What the makers agree on.**

- The order is the same in the guides: change the model first, keep the prompt, then run the same evaluations. Anthropic says prompts written for the previous generation should perform well unchanged [cl-f51] [cl-o55]. OpenAI orders the work: switch the model with effort unchanged, test one level lower, and only then edit prompts [oa-g56].
- OpenAI advises removing prompt text one group at a time. It warns against rewriting a working prompt stack at once, so that a change in behaviour can be traced [oa-g56].
- Anthropic asks for a new effort sweep, because level names do not carry over [cl-effort].
- The breaks in 2026 were mostly parameters and thinking rules, not wording.

**Breaking changes seen between June and October 2026.** Each row comes from the migration list of one maker.

| Move | What breaks or shifts | Source |
| --- | --- | --- |
| Claude Sonnet 5 to 5.5 | `disabled` thinking becomes `between_tools`. Forced tool use returns an error. Thinking blocks are bound to the conversation. Effort levels are recalibrated. | [cl-s55] [cl-effort] |
| Claude Opus 5 to 5.5 | Thinking cannot be disabled. Forced tool use returns an error. The default effort falls from high to medium. | [cl-effort] [cl-o55] |
| Claude Opus 4.8 to 5 | Thinking is on by default. Replies, narration and files run longer. | [cl-o5] |
| GPT-5.6 to GPT-6 | `none` effort maps to `low` on Astra. Tools need the Responses API. Sampling parameters go. Lists and Markdown are the default style. | [oa-latest] |
| GPT-5.5 to GPT-5.6 | Replies are terser. Cache writes cost 1.25 times input. Persisted reasoning is the default. | [oa-g56] [oa-cache] |
| Gemini 2.5 to 3.x | `thinking_level` replaces `thinking_budget`. Remove `candidate_count`. Test PDF and video token use. | [g-35] |
| Gemini 3.5 to 3.6 and later | Sampling parameters are deprecated. A prefilled model turn returns an error. The `minimal` level fails on 3.7 and 3.8 Flash. | [g-latest-arch] [g-latest] |
| GLM-5.2 to 5.3 | A request to disable thinking fails. Effort accepts only low, high and max. | [GLM-5.3](../models/zai/glm-5.3.md#migrating-from-the-previous-generation) |
| Kimi K2.6 to K3 | `reasoning_effort` replaces the `thinking` object. The whole assistant message must go back. | [Moonshot README](../models/moonshot/README.md#prompting-guides) |
| Qwen3.5 to 3.8 | Prompt switches became an API parameter. Preserved thinking is the default in the open-weight templates and on some hosted models. | [Alibaba README](../models/alibaba/README.md#prompting-guides) |
| MiniMax M2.7 to M3 | Thinking is no longer always on. The default depends on the endpoint. | [MiniMax M3](../models/minimax/MiniMax-M3.md#migrating-from-the-previous-generation) |
| DeepSeek V4 to V4.1 | Effort is numeric in the weights. The tool-call markup changed. | [DeepSeek V4.1-Flash](../models/deepseek/deepseek-flash.md#migrating-from-the-previous-generation) |

**Reversals.** Advice reversed within about one year. Telling a model to think hard became removing "think carefully" lines. A request for thorough testing became a cause of unnecessary testing. An instruction to persist became a cause of over-caution on one OpenAI model. See [cross-family.md](../models/cross-family.md#2-direction-of-travel) for the dated list. Behaviour also shifts with no code change. Token use, formatting, narration and autonomy changed between releases at several makers. Artificial Analysis measured about 30 percent more output tokens for each task for Gemini 3.8 Flash than for 3.7 Flash ([Gemini 3.8 Flash](../models/google/gemini-3.8-flash.md#migrating-from-the-previous-generation)).

## Open questions

- How far a prompt written from one model carries to its siblings. OpenAI wrote its GPT-6 prompts from Astra and publishes no per-model test. Google publishes family guidance only.
- Whether the o-series advice (no chain-of-thought prompts, zero-shot first) still holds for GPT-6. The OpenAI pages read do not say.
- Whether XML or Markdown, the number of examples and the placement of documents matter on the current models. The sources are maker advice. No independent cross-maker measurement of these choices was found.
- Whether level names can be mapped between makers. Each maker says its own names change between models.
- How to prompt the models of makers that publish no guide: xAI 4.x, DeepSeek, Z.ai, MiniMax, Alibaba (model-specific), NVIDIA, Tencent, IFM and Xiaomi. For these the page rests on API documents and third-party measurements.
- Inconsistencies inside one maker. Google's prompt guide advises few-shot examples and also short prompts. It ends one template with a step-by-step line, and it says elsewhere that such lines are generally not needed. Anthropic recommends Opus 5.5 at the start of its overview and Opus 5 on the Fable 5.1 pages ([README](../models/anthropic/README.md#models-and-lineage)).

## Sources

Every source below was read on 2026-10-03. Kinds: L is the maker's own page, M is an independent measurement. The maker READMEs and the model files carry their own source lists.

| Id | URL | Kind |
| --- | --- | --- |
| cl-bp | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices | L |
| cl-f51 | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1 | L |
| cl-f51-new | https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1 | L |
| cl-o55 | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5 | L |
| cl-o5 | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5 | L |
| cl-s55 | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5 | L |
| cl-s5 | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5 | L |
| cl-effort | https://platform.claude.com/docs/en/build-with-claude/effort | L |
| cl-think | https://platform.claude.com/docs/en/build-with-claude/thinking | L |
| cl-so | https://platform.claude.com/docs/en/build-with-claude/structured-outputs | L |
| cl-cache | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | L |
| cl-vision | https://platform.claude.com/docs/en/build-with-claude/vision | L |
| cl-optim | https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence | L |
| oa-latest | https://developers.openai.com/api/docs/guides/latest-model | L |
| oa-g56 | https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6 | L |
| oa-reason | https://developers.openai.com/api/docs/guides/reasoning | L |
| oa-rbp | https://developers.openai.com/api/docs/guides/reasoning-best-practices | L |
| oa-fc | https://developers.openai.com/api/docs/guides/function-calling | L |
| oa-so | https://developers.openai.com/api/docs/guides/structured-outputs | L |
| oa-cache | https://developers.openai.com/api/docs/guides/prompt-caching | L |
| g-prompt | https://ai.google.dev/gemini-api/docs/prompting-strategies | L |
| g-35 | https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.5 | L |
| g-think | https://ai.google.dev/gemini-api/docs/thinking | L |
| g-fc | https://ai.google.dev/gemini-api/docs/function-calling | L |
| g-long | https://ai.google.dev/gemini-api/docs/long-context | L |
| g-files | https://ai.google.dev/gemini-api/docs/files | L |
| g-img | https://ai.google.dev/gemini-api/docs/image-understanding | L |
| g-latest | https://ai.google.dev/gemini-api/docs/latest-model | L |
| g-latest-arch | https://web.archive.org/web/20260802003901/https://ai.google.dev/gemini-api/docs/latest-model (the same page as of 2026-08-02, when it covered 3.6 Flash) | L |
| x-reason | https://docs.x.ai/developers/model-capabilities/text/reasoning | L |
| x-cache | https://docs.x.ai/developers/advanced-api-usage/prompt-caching/best-practices | L |
| ds-think | https://api-docs.deepseek.com/guides/thinking_mode | L |
| km-guide | https://platform.kimi.ai/docs/guide/prompt-best-practice | L |
| km-k3 | https://platform.kimi.ai/docs/guide/kimi-k3-quickstart | L |
| km-tools | https://platform.kimi.ai/docs/guide/kimi-k3-tool-calling-best-practice | L |
| km-choice | https://platform.kimi.ai/docs/guide/use-tool-choice | L |
| km-params | https://platform.kimi.ai/docs/api/models-overview | L |
| km-blog | https://www.kimi.ai/blog/kimi-k3 | L |
| qw-think | https://docs.qwencloud.com/developer-guides/text-generation/thinking | L |
| zai-think | https://docs.z.ai/guides/capabilities/thinking-mode | L |
| zai-bp | https://docs.z.ai/devpack/resources/best-practice | L |
| mm-fc | https://platform.minimax.io/docs/guides/text-m3-function-call | L |
| mi-prompt | https://docs.mistral.ai/capabilities/completion/prompting_capabilities/ | L |
| mi-reason | https://docs.mistral.ai/capabilities/reasoning/ | L |
| meta-13 | https://research.meta.ai/blog/introducing-muse-spark-1-3 | L |
| cur-tok | https://cursor.com/blog/improved-token-efficiency | L |
| cur-rules | https://cursor.com/docs/rules.md | L |
| aa-astra | https://artificialanalysis.ai/models/gpt-6-astra, and the pages of the same name that end in -low, -medium and -high | M |
