---
last_checked: 2026-10-03
volatility: MONITOR (lineage, guides and API behaviour change at each release)
sources:
  - https://api-docs.deepseek.com/updates
  - https://api-docs.deepseek.com/quick_start/pricing
  - https://api-docs.deepseek.com/news/news260424
  - https://api-docs.deepseek.com/news/news260910
  - https://api-docs.deepseek.com/api/create-chat-completion
  - https://api-docs.deepseek.com/guides/thinking_mode
  - https://api-docs.deepseek.com/guides/tool_calls
  - https://api-docs.deepseek.com/guides/json_mode
  - https://api-docs.deepseek.com/guides/vision
  - https://api-docs.deepseek.com/guides/responses_api
  - https://api-docs.deepseek.com/guides/anthropic_api
  - https://api-docs.deepseek.com/guides/kv_cache
  - https://api-docs.deepseek.com/quick_start/rate_limit
  - https://api-docs.deepseek.com/quick_start/error_codes
  - https://api-docs.deepseek.com/quick_start/agent_integrations/claude_code
  - https://api-docs.deepseek.com/quick_start/agent_integrations/codex
  - https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813
  - https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
  - https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/encoding/README.md
  - https://arxiv.org/html/2606.19348v1
  - https://arxiv.org/html/2609.19969
  - https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro
  - https://www.far.ai/blog/security-stress-test-deepseek-v4-pros-safeguards
  - https://arxiv.org/abs/2608.16393
  - https://artificialanalysis.ai/models/deepseek-v4-1-flash
  - https://artificialanalysis.ai/models/deepseek-v4-pro
  - https://github.com/anomalyco/opencode/issues/24122
  - https://forum.cursor.com/t/deepseek-v4-pro-error-report/159983
---

# DeepSeek models

DeepSeek is a Chinese laboratory that publishes the weights of its models under the MIT licence and also serves them through its own API. On 2026-10-03 three of its models are in scope for this library: [DeepSeek V4-Pro (0813)](deepseek-v4-pro.md), a text-only model, [DeepSeek V4.1-Flash](deepseek-flash.md), a smaller model that also reads images, and [DeepSeek V4-Flash (0731)](deepseek-v4-flash.md), the retired text-only Flash model whose weights stay public. This page holds what is true of all three: how the line developed, the API they share, what DeepSeek publishes to guide prompting and safety, and the behaviour that does not change between them. Each model file says only what differs for that model.

## Models and lineage

What the change log and the news posts record, oldest first ([deepseek-changelog], [deepseek-news-260424], [deepseek-news-260910]):

| Date | Release | What changed |
| --- | --- | --- |
| 2025-08-21 | V3.1 | One model with a thinking mode and a non-thinking mode. `deepseek-chat` and `deepseek-reasoner` named the two modes. |
| 2025-12-01 | V3.2 | Same two names upgraded. The tool-calls guide dates tool use inside thinking mode from this release. A temporary V3.2-Speciale endpoint without tool calls ran until 2025-12-15. |
| 2026-04-24 | V4 (Preview) | Two models: V4-Pro, 1.6T parameters with 49B active, and V4-Flash, 284B with 13B active. A 1M-token context became standard on every official service. The two old names became aliases of V4-Flash's non-thinking and thinking modes until their retirement on 2026-07-24. |
| 2026-07-31 | [V4-Flash-0731](deepseek-v4-flash.md) | Same size and architecture as the Preview, post-trained again. Native Responses API for Codex. |
| 2026-08-13 | V4-Pro-0813 (general availability) | Replaced the Preview under the same API id. Three effort levels (low, high, max) for both V4 models. Peak and off-peak pricing from 2026-08-16 16:00 UTC. |
| 2026-08-21 | V4-Flash-Vision-Exp | Experimental vision variant of V4-Flash. |
| 2026-09-10 | V4.1-Flash | A 552B-parameter backbone that uses 8B parameters per token while reading a prompt and 16B while writing; reads images. Replaced V4-Flash and V4-Flash-Vision-Exp, which DeepSeek calls retired. Lower prices. |

How the models are classed here:

- **DeepSeek Pro, generation 4.** V4-Pro (0813) is the only model of the class. The 2026-09-10 news post says DeepSeek is phasing V4-Pro out and routing its requests to V4.1-Flash at Flash prices from 2026-09-14 until a V4.1-Pro launches. The change log entry of the same date says that, because of user demand, V4-Pro stays available after 2026-09-14 at unchanged billing, and the pricing page read on 2026-10-03 still lists `deepseek-v4-pro` as DeepSeek-V4-Pro-0813 at its own prices. The statements disagree; this library follows the pricing page and the change log and marks the point as open. No V4.1-Pro has been announced with a date, a size or a price.
- **DeepSeek Flash, generation 4.1.** V4.1-Flash is the current model. The generation before it, V4-Flash (generation 4), is retired from the API; its weights remain on Hugging Face as V4-Flash-0731 and stay in scope for local use, so [it has a file](deepseek-v4-flash.md).
- Both current models are mixture-of-experts models with a 1M-token window. Parameter counts come from DeepSeek's posts and reports: 1.6T total and 49B active for V4-Pro (Hugging Face counts about 1.65T in the 0813 repository's weight files), and a 552B backbone plus 196B conditional-memory parameters for V4.1-Flash (Hugging Face counts 763B in the repository's weight files; the model card does not break that total down).
- Older lines (V3.x, R1) are out of scope.

## API surface

One API serves both models. This section is from DeepSeek's documentation read on 2026-10-03 ([deepseek-pricing], [deepseek-chat-api], [deepseek-responses], [deepseek-anthropic-api]).

**Endpoints and ids**

- Chat Completions at `https://api.deepseek.com`; the OpenAI Responses format at the same base URL (stateless, built for Codex); the Anthropic Messages format at `https://api.deepseek.com/anthropic`. Beta features (strict tool schemas, assistant-prefix completion, fill-in-the-middle) need the base URL `https://api.deepseek.com/beta`.
- Ids: `deepseek-flash` (V4.1-Flash) and `deepseek-v4-pro` (V4-Pro-0813). The retired names `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` are still accepted and are served by V4.1-Flash at Flash prices. `deepseek-chat` and `deepseek-reasoner` were announced for retirement after 2026-07-24 15:59 UTC and are not on the pricing page.
- On the Anthropic endpoint, model names that start with `claude-opus` map to `deepseek-v4-pro` (billed at Pro prices), names that start with `claude-sonnet` or `claude-haiku` map to `deepseek-flash`, and any other unknown name also falls back to `deepseek-flash`.

**Limits and defaults**

- Context window 1M tokens; maximum output 384K tokens, which the API reference gives as 393,216 for `max_tokens`. When `max_tokens` is not set the default is 8K without thinking, 64K with thinking and 128K with thinking at max effort.
- Concurrent requests per account: 2,500 for `deepseek-flash`, 500 for `deepseek-v4-pro`; above that the API answers HTTP 429. A `user_id` field (letters, digits, hyphen and underscore, up to 512 characters) separates end users for cache isolation, scheduling and safety handling. During long waits the connection stays open with empty lines or SSE keep-alive comments, and a request that has not started inference after ten minutes is closed ([deepseek-rate-limit]).
- Error codes: 400 format, 401 key, 402 balance, 422 parameters, 429 rate, 500 server, 503 overload ([deepseek-error-codes]). The finish reasons are `stop`, `length`, `content_filter`, `tool_calls`, `insufficient_system_resource` and `aborted`.
- Stop sequences: up to 16. Log probabilities: up to 20 per position. The API is stateless: the client sends the whole history each time.

**Roles and fields**

- Chat Completions accepts `system`, `user`, `assistant` and `tool` messages and has no `developer` role; system messages may appear in the middle of a conversation. The Responses format treats a `developer` message as a user message. Tool calls that the model did not write can be inserted mid-conversation only through the Anthropic and Responses formats ([deepseek-tool-calls]).
- The Responses format ignores `parallel_tool_calls` (parallel calls are always on), `max_tool_calls`, `truncation` and the caching keys; does not support `previous_response_id`, `store`, `background` or `conversation`; accepts `text.verbosity` and `reasoning.summary` without effect; and supports `reasoning.effort`. A request that exceeds the window returns 400 instead of being truncated.
- The Anthropic format ignores `cache_control`, `top_k`, `service_tier`, `container`, `mcp_servers` and `disable_parallel_tool_use`; honours `thinking` but not `budget_tokens`; honours only `effort` inside `output_config`; and does not support document, search-result, redacted-thinking, code-execution or MCP content blocks.

**Prices and caching**

- Peak hours are 01:00-04:00 and 06:00-10:00 UTC on weekdays, excluding Chinese public holidays; every other hour is off-peak, at half the peak price. Prices for each model are in its card.
- Context caching is on for every account. DeepSeek stores prefix units on disk at request boundaries, at points where requests overlap, and at fixed token intervals; a later request hits the cache only if it matches a whole stored unit. The cache is best effort, entries last hours to days, and `usage` reports `prompt_cache_hit_tokens` and `prompt_cache_miss_tokens` ([deepseek-context-caching]).

**Other surfaces**

- JSON output, strict tool schemas and prefix completion are described in the model files. The Files API and a fill-in-the-middle endpoint (non-thinking mode only) also exist.
- Integration pages exist for Claude Code, Codex and others. DeepSeek's Claude Code page sets `CLAUDE_CODE_EFFORT_LEVEL` to max, an auto-compact window of 786,432 tokens and the 1M-context suffix on the main model, and sends the sonnet, opus and main slots to V4.1-Flash. Its Codex page offers a script that writes a model catalogue for V4.1-Flash or V4-Pro. The V4.1 post names WorkBuddy (with CodeBuddy) and OpenCode as official partners ([deepseek-claude-code], [deepseek-codex]).
- Weights and self-hosting: no Jinja chat template is shipped. A Python reference encoder in each repository's `encoding` folder and the `deepseek-recipe` library turn OpenAI-style messages into the model's prompt format; vLLM and SGLang are listed as runtimes. DeepSeek recommends temperature 1.0, top-p 0.95 for agents and 1.0 otherwise, and a large output limit (see the model files).

## Prompting guides

DeepSeek publishes no prompt-writing guide for the V4 series. What exists, and what each document covers:

| Document | What it says that bears on prompts |
| --- | --- |
| Thinking-mode guide | How to switch thinking and effort in the three API formats; which sampling fields are ignored; the rules for sending `reasoning_content` back. |
| Tool-calls guide | Tool format, strict mode and its schema subset, inserting tool calls mid-conversation. |
| JSON-output guide | Enabling JSON mode; the prompt must ask for JSON and show an example; set `max_tokens` high enough. |
| Vision guide | Image formats, limits and token cost (V4.1-Flash only). |
| Context-caching guide | How prefix caching behaves. |
| `encoding` folders on Hugging Face | The exact prompt format: roles, reasoning blocks, tool-call markup, the effort line. |
| Technical reports | Training and evaluation settings, including the effort prompts, the context windows used for each effort level and a recommendation about agent frameworks. |

Advice that DeepSeek states, collected from those documents:

- Effort: low for simple tasks, high for everyday agent work, max for the hardest problems (change log, 2026-08-13). In the V4 report the max mode was trained with a longer context and a weaker length penalty than high, and DeepSeek prepends a long instruction to the system prompt in that mode ([open-weight-f16]).
- Sampling: temperature 1.0; top-p 0.95 for agentic use, 1.0 otherwise (Hugging Face model cards).
- Agent frameworks that simulate tool use through user messages do not trigger the path that keeps reasoning between turns; the V4 report keeps its V3.2 recommendation of non-thinking mode for them ([open-weight-f16]).
- JSON mode: put the word json in the prompt, show the shape wanted, and leave room for it in `max_tokens` ([deepseek-json]).
- The V4.1 report adds that its effort control was trained with an effort number written into the system prompt, and that values between the three API presets exist only in self-hosted use ([deepseek-v41-paper]).

How the guidance moved: V3.2 let thinking mode call tools but discarded reasoning at each new user message; the V4 series keeps all reasoning across user messages whenever the request carries tools and still discards it in plain chat ([open-weight-f16]); the 2026-08-13 release gave both V4 models three API effort levels; V4.1 turned effort into a number from 1 to 100 in the weights, with 50, 75 and 100 as the API presets, and changed the tool-call markup (a space after the DSML tag name) ([hf-v41-encoding]).

## System-card practice

DeepSeek publishes no system card for any V4 model. For each release it provides:

- a change-log entry or news post with a benchmark table, self-run and mostly made with its own DeepSeek Harness in minimal mode at max effort, temperature 1.0 and top-p 0.95;
- a Hugging Face model card with the weights, a table against other models, the run settings and the encoding folder;
- a technical report: [the V4 report](https://arxiv.org/html/2606.19348v1) covers the Preview, and [the V4.1 report](https://arxiv.org/html/2609.19969) covers V4.1-Flash.

Neither report has a safety, alignment, refusal, jailbreak, prompt-injection, biology or cyber-policy section ([open-weight-f16], [deepseek-v41-paper]). The V4.1 report has a limitations section about architecture (untested boundary cases, described in the V4.1-Flash file) and a note that its CyberGym and exploit scores are dual-use. No dangerous-capability thresholds, refusal rates or classifier descriptions are published.

Reading DeepSeek's tables: some rows are internal sets marked with a dagger (DSBench-FullStack, DSBench-Hard); and one model can carry different numbers in two documents (for V4-Pro, AutomationBench is 31.8 in the 2026-08-13 change log and 43.2 in the 2026-09-10 Hugging Face table, with no reason given; V4.1-Flash's NL2Repo is 65.4 in the change log and 64.0 on the model card). Everything about safety below therefore comes from outside evaluators.

## Family-wide behaviour

**Thinking and `reasoning_content`.** Thinking is on by default at high effort; the answer arrives as `content` and the reasoning as `reasoning_content`. A request that carries `tools` must send back the `reasoning_content` of every earlier assistant message, including turns that made no tool call; leaving it out returns HTTP 400. A request without `tools` may send it, and the API ignores it. Two coding clients (OpenCode through an OpenAI-compatible adapter, and Cursor) were reported in April and May 2026 to hit that error in multi-turn tool use because they dropped the field; the OpenCode report's workaround was DeepSeek's Anthropic endpoint, whose SDK keeps thinking blocks (class A, one report each) ([opencode-issue], [cursor-forum]).

**Switches.** On Chat Completions, `thinking: {type: disabled}` or `reasoning_effort: none` turns thinking off and `low`, `high` and `max` turn it on. The Anthropic format uses the same `thinking` switch and sets the level with `output_config.effort`. The Responses format uses `reasoning.effort` with `none`, `low`, `high` or `max`, where `none` turns thinking off. `minimal` is read as low; `medium` and `xhigh` as high; `ultra` as max. The OpenAI SDK needs `extra_body` to send `thinking`.

**Sampling.** In thinking mode `temperature`, `presence_penalty` and `frequency_penalty` are accepted and ignored, and a `top_p` below 0.95 is raised to 0.95. Without thinking, `temperature` works from 0 to 2 (default 1) and `top_p` is fixed at 1.0. The two penalties are deprecated everywhere.

**Tool choice.** `required` and a named function are not supported in thinking mode and return 400; thinking has to be disabled to use them.

**Tool-call markup.** The V4 series replaced JSON arguments in the prompt with an XML-style block built on a DSML token; DeepSeek says this reduced escaping failures and tool-call errors ([open-weight-f16]).

**Safety as measured by others.** FAR.AI tested V4-Pro through the official API in May 2026, before the 0813 release: direct harmful requests were blocked in every domain it tried, and three jailbreaks then succeeded in 99.6% to 100% of attempts, including one first published for V3.2 that worked unchanged; FAR.AI notes that a deployed open-weight checkpoint cannot be patched after release ([far-ai-v4-pro]). NIST's CAISI evaluated the same Preview; its post reports capability and cost only, with no safety results ([nist-caisi-v4-pro]). An indirect prompt-injection study of DeepSeek Harness with V4-Flash as the backend counted full attack success in 5.6% of 14,560 runs under a rule-based judge ([ipi-dsh-paper]). The model files give the details and the limits of each study.

**Token use.** Artificial Analysis counted about 250M output tokens for V4.1-Flash and about 160M for V4-Pro across its Intelligence Index run, so the model with the lower per-token price emitted more tokens per task ([aa-flash], [aa-pro]).

## Open questions

- Whether `deepseek-v4-pro` is answered by V4-Pro-0813 or by V4.1-Flash today, and when a V4.1-Pro ships. The sources conflict, and an API call that returns the served model would settle the first.
- Whether the maker will publish a system card or a safety evaluation; nothing in the V4 or V4.1 documents indicates one.
- Whether 1M means 1,000,000 or 1,048,576 tokens. The output limit of 384K is exactly 393,216, which suggests binary units, but the window is never given as an exact number.
- No independent run of either model on SWE-Bench Pro (Scale) or the METR time horizon was found, and Artificial Analysis's coding-agent index showed no DeepSeek entry.
- Which cloud marketplaces serve these models; none was confirmed on DeepSeek's own pages.

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| deepseek-changelog | https://api-docs.deepseek.com/updates | L | 2026-10-03 |
| deepseek-pricing | https://api-docs.deepseek.com/quick_start/pricing | L | 2026-10-03 |
| deepseek-news-260424 | https://api-docs.deepseek.com/news/news260424 | L | 2026-10-03 |
| deepseek-news-260910 | https://api-docs.deepseek.com/news/news260910 | L | 2026-10-03 |
| deepseek-chat-api | https://api-docs.deepseek.com/api/create-chat-completion | L | 2026-10-03 |
| deepseek-thinking-mode | https://api-docs.deepseek.com/guides/thinking_mode | L | 2026-10-03 |
| deepseek-tool-calls | https://api-docs.deepseek.com/guides/tool_calls | L | 2026-10-03 |
| deepseek-json | https://api-docs.deepseek.com/guides/json_mode | L | 2026-10-03 |
| deepseek-vision | https://api-docs.deepseek.com/guides/vision | L | 2026-10-03 |
| deepseek-responses | https://api-docs.deepseek.com/guides/responses_api | L | 2026-10-03 |
| deepseek-anthropic-api | https://api-docs.deepseek.com/guides/anthropic_api | L | 2026-10-03 |
| deepseek-context-caching | https://api-docs.deepseek.com/guides/kv_cache | L | 2026-10-03 |
| deepseek-rate-limit | https://api-docs.deepseek.com/quick_start/rate_limit | L | 2026-10-03 |
| deepseek-error-codes | https://api-docs.deepseek.com/quick_start/error_codes | L | 2026-10-03 |
| deepseek-claude-code | https://api-docs.deepseek.com/quick_start/agent_integrations/claude_code | L | 2026-10-03 |
| deepseek-codex | https://api-docs.deepseek.com/quick_start/agent_integrations/codex | L | 2026-10-03 |
| hf-v4-pro-0813 | https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813 | L | 2026-10-03 |
| hf-v41-flash | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | L | 2026-10-03 |
| hf-v41-encoding | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/encoding/README.md | L | 2026-10-03 |
| open-weight-f16 | https://arxiv.org/html/2606.19348v1 | L | 2026-10-03 |
| deepseek-v41-paper | https://arxiv.org/html/2609.19969 | L | 2026-10-03 |
| nist-caisi-v4-pro | https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro | M | 2026-10-03 |
| far-ai-v4-pro | https://www.far.ai/blog/security-stress-test-deepseek-v4-pros-safeguards | M | 2026-10-03 |
| ipi-dsh-paper | https://arxiv.org/abs/2608.16393 | M | 2026-10-03 |
| aa-flash | https://artificialanalysis.ai/models/deepseek-v4-1-flash | M | 2026-10-03 |
| aa-pro | https://artificialanalysis.ai/models/deepseek-v4-pro | M | 2026-10-03 |
| opencode-issue | https://github.com/anomalyco/opencode/issues/24122 | A | 2026-10-03 |
| cursor-forum | https://forum.cursor.com/t/deepseek-v4-pro-error-report/159983 | A | 2026-10-03 |
