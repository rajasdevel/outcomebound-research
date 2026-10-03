---
last_checked: 2026-10-03
volatility: MONITOR (lineage, guides and API behaviour change at each release)
sources:
  - https://media.x.ai/v1/website/4p7card-5eccc980.pdf
  - https://docs.x.ai/developers/models
  - https://docs.x.ai/developers/pricing
  - https://docs.x.ai/developers/migration/may-15-retirement.md
  - https://docs.x.ai/developers/release-notes
  - https://x.ai/news/grok-build-0-1
  - https://x.ai/news/grok-4-5
  - https://x.ai/news/grok-4-6
  - https://media.x.ai/v1/website/card-4p6-4cd2dc57.pdf
  - https://x.ai/news/grok-4-7
  - https://docs.x.ai/developers/grok-4-7
  - https://docs.x.ai/developers/model-capabilities/text/reasoning.md
  - https://docs.x.ai/developers/advanced-api-usage/regions
  - https://docs.x.ai/developers/models/grok-4.7
  - https://docs.x.ai/developers/models/grok-build-0.1
  - https://docs.x.ai/developers/model-capabilities/text/comparison
  - https://docs.x.ai/developers/model-capabilities/text/generate-text
  - https://docs.x.ai/developers/rest-api-reference/inference/responses
  - https://docs.x.ai/developers/rest-api-reference/inference/chat-completions
  - https://docs.x.ai/developers/tools/function-calling
  - https://docs.x.ai/developers/models/grok-4.6
  - https://docs.x.ai/developers/rate-limits
  - https://docs.x.ai/developers/faq/security
  - https://docs.x.ai/llms.txt
  - http://web.archive.org/web/20251118014240/https://docs.x.ai/docs/guides/grok-code-prompt-engineering
  - https://docs.x.ai/developers/advanced-api-usage/prompt-caching/best-practices
  - https://docs.x.ai/build/features/project-rules.md
  - https://raw.githubusercontent.com/xai-org/grok-build/main/crates/codegen/xai-grok-agent/templates/prompt.md
  - https://docs.x.ai/developers/community/microsoft-foundry.md
  - https://cursor.com/blog/improved-token-efficiency
  - https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf
  - https://data.x.ai/2025-08-26-grok-code-fast-1-model-card.pdf
  - https://docs.x.ai/developers/advanced-api-usage/prompt-caching/maximizing-cache-hits
  - https://docs.x.ai/developers/advanced-api-usage/prompt-caching/multi-turn.md
  - https://docs.x.ai/developers/advanced-api-usage/prompt-caching/usage-and-pricing
  - https://docs.x.ai/developers/model-capabilities/text/structured-outputs
  - https://docs.x.ai/developers/model-capabilities/images/understanding
  - https://artificialanalysis.ai/articles/grok-4-5-brings-spacexai-to-the-the-intelligence-frontier
  - https://artificialanalysis.ai/articles/benchmarking-grok-4-7
  - https://cursor.com/blog/joining-spacex
  - https://cursor.com/blog/how-cursor-router-works
  - https://cursor.com/docs/models/grok-4-5
  - https://cursor.com/blog/grok-4-5-model-card
  - https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing
  - https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech
  - https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech/prompting-guide
  - https://x.ai/news/grok-voice-think-fast-2
  - https://x.ai/news/grok-voice-think-fast-1
---

# xAI (SpaceXAI) models

SpaceXAI is the trading name that xAI LLC uses for its models and API; xAI's own model cards say the two names are interchangeable [xai-47-card]. The maker's models are the Grok text and multimodal models, the coding model `grok-build-0.1`, and the Grok Build terminal agent that runs them. The API is at `api.x.ai` and the documentation at `docs.x.ai` [xai-docs-models]. The five model files in this folder cover the two newest generations of the Grok class (4.7 and 4.6), the 4.7 Fast serving tier, the coding model, and the speech-to-speech voice model [grok-voice-think-fast-2.0](grok-voice-think-fast-2.0.md). Image and video models, and the speech-to-text and text-to-speech APIs, are outside this library.

## Models and lineage

Lineage, from the maker's release notes, release posts and model pages (L):

| Model | Released | What changed for a user |
| --- | --- | --- |
| Grok 4.3 | about 2026-04-30 | One slug with effort levels none, low, medium and high; 1M-token context; $1.25 in and $2.50 out per Mtok. Still priced on the pricing page; Artificial Analysis dates its launch article 2026-04-30 [xai-docs-pricing] [grok-migration-may15] [grok-f9]. |
| `grok-build-0.1` | early access 2026-05, API public beta 2026-05-29 | Coding model. It took over the retired `grok-code-fast-1` slug on 2026-05-15 [xai-release-notes] [xai-build01-news] [grok-migration-may15]. |
| Grok 4.5 | 2026-07 (Cursor's blog dates it 2026-07-08; the x.ai post shows 2026-07-16) | Reasoning cannot be turned off (low, medium, high; default high); context cut from 1M to 500k; $2 in and $6 out. The xAI post says it was trained alongside Cursor; Cursor's page describes continued training on Cursor data [xai-45-news] [xai-docs-models] [cursor-grok-45]. |
| Grok 4.6 | 2026-08-12 | Adds the `xhigh` effort level. Aimed at long-running agent work. Pretraining cutoff January 2026 [xai-46-news] [xai-46-card]. |
| Grok 4.7 | 2026-09-21 | Larger base model, longer reinforcement learning on multi-hour tasks, `reasoning.encrypted_content` always returned on the Responses API. Same price and context as 4.6. Pretraining cutoff June 2026 [xai-47-news] [xai-47-card] [xai-docs-47-overview]. |
| Grok Voice Think Fast 1.0 | 2026-04-23 (announcement) | Speech-to-speech voice model. The release notes list it in April. The docs now list only 2.0 as a choice and the page for 1.0 returns not found, so it has no file [xai-voice-release-notes] [xai-voice-announce-1]. |
| Grok Voice Think Fast 2.0 | 2026-07-29 (announcement) | The voice model with a file here. Priced per minute. The alias `grok-voice-latest` moved to it on 2026-08-05 [xai-voice-announce-2] [xai-voice-release-notes]. |
| Grok 4.7 Fast | 2026-09-21 | The same model on faster serving at twice the token price; offered only in Cursor and Grok Build, not on the public API [xai-docs-47-overview]. |

Scope in this library: the Grok class is two generations, 4.7 and 4.6, so Grok 4.5, 4.3 and 4.20 get no file even though the pricing page still lists them [xai-docs-pricing]. `grok-build-0.1` is the only generation of the Grok Build class. Grok 4.7 Fast has its own file because its price, availability and billing differ, although the maker says the model is the same. The multi-agent model `grok-4.20-multi-agent` is a different kind of product (its effort setting chooses how many agents work on a request, not how long one model thinks) and is not covered [grok-f10].

As of 2026-10-03 the models page lists no model newer than `grok-4.7`, and its "which model" section names Grok 4.7 for both code and chat [xai-docs-models]. Grok Build, the agent, uses Grok 4.7 as its default model [xai-47-card].

## API surface

- **Endpoints.** The global endpoint is `https://api.x.ai/v1`. The US endpoint `https://us.api.x.ai/v1` keeps request handling, inference, safety moderation and retained data in the United States, costs 10% more, serves only `grok-4.7` and `grok-4.6`, and does not cover Files, Collections or the server-side tools. A model that is not on its list returns 404 [xai-docs-regions]. Model pages list regions `us-east-1`, `us-west-2` and `us-central-1` for 4.7 and 4.6, and the first two for the coding model [xai-docs-47] [xai-docs-build01].
- **Which API.** The Responses API (`/v1/responses`) is the maker's recommended interface and gets new features first. The docs label Chat Completions (`/v1/chat/completions`) deprecated and legacy: it returns no reasoning content and supports function calling only [xai-docs-compare]. SDKs: the xAI Python SDK (gRPC), the OpenAI SDKs pointed at the base URL, and the Vercel AI SDK (use `xai.responses(...)` for the Responses API) [xai-docs-gen] [xai-docs-compare].
- **State.** On the Responses API a response is stored for 30 days by default and can be continued with `previous_response_id`; `store: false` turns that off. `instructions` (the system prompt) cannot be combined with `previous_response_id` [xai-docs-gen] [xai-docs-respref].
- **Output cap.** `max_output_tokens` (Chat Completions: `max_completion_tokens`) counts only visible output tokens, not reasoning or function-call tokens, and defaults to 128,000 when unset [xai-docs-respref] [xai-docs-chatref]. The model pages publish no maximum output [xai-docs-47].
- **Tools.** Up to 350 function tools per request. Server-side tools run on the maker's servers and are billed per call on top of tokens: web search $5 per 1k calls, X search $5 per 1k posts and $10 per 1k profiles, code execution $5 per 1k, collections search $2.50 per 1k, attachment search $5 per 1k; remote MCP tools are billed in tokens only [xai-docs-pricing] [xai-docs-fc].
- **Other API features.** Context compaction (`POST /v1/responses/compact`, since May 2026), WebSocket mode for the Responses API, deferred completions, Priority Processing (`service_tier: "priority"`, billed at 2x and only when the response confirms the tier), `safety_identifier` for attributing policy violations to an end user, a `cost_in_usd_ticks` field in usage, and `service_tier` values `default`, `priority` and `fast` [xai-release-notes] [xai-docs-pricing] [xai-docs-respref].
- **Batch.** The Batch API gives 20% off only for Grok 4.3 and the 4.20 models; the model pages for 4.7, 4.6 and `grok-build-0.1` say Batch is not supported [xai-docs-pricing] [xai-docs-47] [xai-docs-46] [xai-docs-build01].
- **Rate limits.** Limits are per model, as requests per second and tokens per minute, and rise automatically with cumulative spend since 2026-01-01 (tiers at $50, $250, $1,000 and $5,000). For 4.7 and 4.6 tier 0 is 150 requests per second and 50M tokens per minute; for `grok-build-0.1` it is 37 and 10M. Cached prompt tokens and reasoning tokens count toward the token limit [xai-docs-rates].
- **Data handling.** By default requests and responses are stored encrypted for 30 days for abuse audit and are not used for training without permission. Zero Data Retention is a team-wide setting that disables the stateful Responses API, Files, Collections, the Batch API and deferred completions; the maker does not recommend it for most customers [xai-docs-security].
- **Violation fee.** A request that the system judges to break the usage guidelines is still charged; one caught before generation on the Responses API costs $0.05 [xai-docs-pricing].

**Voice.** The voice API has its own endpoint, `wss://api.x.ai/v1/realtime`, which follows the shape of the OpenAI Realtime API, and its own pricing (US$0.08 per minute for speech-to-speech) and rate limits (concurrent sessions per tier, from 10 to 200). It also offers ephemeral client tokens, SIP phone routing and custom voices cloned from a short clip. See the model file [xai-voice-s2s] [xai-voice-pricing] [xai-voice-rates].

## Prompting guides

xAI publishes no prompting guide for a current text model. Its documentation index lists a prompting guide only for speech-to-speech voice [xai-docs-index]. What exists, and what each says:

- **The 2025 coding-model guide** for `grok-code-fast-1`, now removed from the live docs and kept only in an archive copy [grok-f15]. It advises giving specific context (file paths, the code at issue) and explicit goals rather than vague asks, refining a prompt by naming what failed, and using the model for agentic tasks rather than one-shot questions. For developers building agents on the API it advises native tool calling in place of XML-formatted tool calls, a detailed system prompt covering the task, expectations and edge cases, XML tags or Markdown headings to mark sections of context, and leaving earlier prompt history unchanged so the cache keeps hitting. That slug has redirected to `grok-build-0.1` since 2026-05-15, but nothing says the advice was re-validated for 4.x models [grok-migration-may15].
- **The Grok 4.7 overview page** gives three operating notes: set a `prompt_cache_key` so a conversation reaches the same server, use context compaction in long agent loops, and pass the returned reasoning items back unchanged [xai-docs-47-overview].
- **The reasoning page** tells what each effort level is for and lists the parameters that cause errors (see Family-wide behaviour) [grok-f10].
- **Prompt-caching pages** say to put system prompts, few-shot examples and reference documents first, never edit, remove or reorder earlier messages, and send the same conversation identifier on every request [xai-docs-cache-best].
- **The Grok Build documentation** says instruction files (`AGENTS.md`, `CLAUDE.md`, `.grok/rules/`, and, for compatibility, `.claude/rules/` and `.cursor/rules/`) are loaded in full with no size cap, deeper files win on conflict, and short, specific instructions are followed more reliably than long ones [grok-f1].
- **The Grok Build system prompt** is open source (Apache-2.0). Its current text is short, in labelled sections: reversibility and authorisation for risky actions, a work policy (keep every explicit requirement in view, claim success only when tool output supports it, keep changes to what was asked, comments short and factual), subagent launches when the user asks for them, a communication section (lead with the answer, plain words, no invented labels, write for a reader who has not seen the tool calls) and browser verification for web changes [xai-build-prompt]. It shows what the maker's own harness treats as failure modes; it is not a guide to prompt design.
- **A Microsoft Foundry integration page** on docs.x.ai lists generic tips: encourage step-by-step reasoning when needed, specify the output format, use clear tool schemas [grok-f11]. It sits among partner integration pages, not the core reasoning docs.

Movement over releases: the 2025 guidance asked for thorough prompts for a fast non-frontier coding model; the 2026 pages say little about prompt wording and spend their words on API behaviour (effort, caching, encrypted reasoning, compaction). Cursor, which ships these models in its agent, reports that it removed about two thirds of its own system prompt as models improved and that plain tool definitions work without long DO NOT lists, across model families [cursor-token-eff].

**Voice prompting.** xAI's speech-to-speech prompting guide advises a second-person prompt in Markdown with five sections in a fixed order (Role & Persona, Objective, Conversation Flow, Guardrails & Escalation, Voice & Communication Style), tools named only if they exist, business facts written in full, and a mandatory safety path for agents that may meet a person in crisis. The model file has the details [xai-voice-prompting].

## System-card practice

Grok 4.6 and 4.7 each have a dated PDF model card at `media.x.ai` (the 4.6 card was revised 2026-08-17); the official Grok 4.5 card was announced on Cursor's blog on 2026-07-14, and the 2025 `grok-code-fast-1` and April 2026 Grok 4.20 cards are PDFs at `data.x.ai` [xai-46-card] [xai-47-card] [cursor-grok-45-card] [xai-codefast-card] [grok-g7]. The cards are written to state capabilities in quantitative terms and then document safety domains: cyber, biological and chemical knowledge, jailbreaks and robustness, general output safety including refusals on weapons topics, mental health, and behaviours (honesty under pressure, sycophancy). Reading notes:

- Capability tests for cyber and biology run without the production safeguards, to measure the model's full ability. Refusal tests run with the standard safeguards. The same table can hold both kinds, so read each section's own statement [xai-47-card].
- Many coding and knowledge-work results come from outside parties (Datacurve, Harbor, Abundant AI, Proximal Labs, Vals AI, Atopile, Mecado, Mercor and others), run in Grok Build or in the evaluator's harness (mini-SWE-agent, Terminus-2, Proximus, Valkyrie, Cursor's agent); peers' numbers often come from their own cards or leaderboards. The card names the effort level of every row (`high`, `xhigh`, `max`) and the harness sometimes. Compare rows only at equal settings [xai-47-card].
- Announcement and card can differ: for Grok 4.7 the announcement gives Terminal-Bench 4.0 as 37.6% and EEBench as 64.0%, the card 38.0% and 66.0% [xai-47-news] [xai-47-card].
- The 4.6 and 4.7 cards contain no section on prompt injection or agentic hijacking, reward hacking or test special-casing, or sandbagging. The Grok 4.20 card (April 2026) did report an AgentDojo hijacking attack success rate of 0.33 and found that stronger system-prompt following also made the model easier to steer with a misuse system prompt (0.32 against 0.16 for Grok 4) [grok-g7]. The 4.6 card includes one agentic anecdote: an earlier checkpoint asked to speed up its own inference tried 297 candidate optimisations in five hours, dropped those without a measured end-to-end gain (several had passed microbenchmarks) and opened seven pull requests [xai-46-card].
- Safeguards are described as layered: safety fine-tuning, system prompts that push toward honesty and away from over-refusal on benign or hypothetical questions, and, on some deployment surfaces, runtime input and topical filters for CSAM, self-harm and biological or chemical weapons paths, plus cyber-specific safeguards. The cards say the models are not intended for autonomous high-stakes decisions in medicine, law, finance or safety-critical systems without human oversight [xai-47-card].
- Bio and chemical knowledge tests are treated as threshold tests under xAI's Frontier Artificial Intelligence Framework (dated 2026-06-30) [xai-47-card].
- No model card exists for `grok-build-0.1` or for the Fast tier. The 2025 card for `grok-code-fast-1` states that a fixed system-prompt prefix stating the safety policy was inserted in every evaluation and production deployment, and that training ranked the safety policy above the rest of the system prompt and the system prompt above user messages; whether any 4.x model gets such a prefix is not stated in the sources read [xai-codefast-card].

## Family-wide behaviour

- **Reasoning is always on** from Grok 4.5 on and cannot be disabled; `reasoning_effort` defaults to `high`; `xhigh` exists from 4.6 (on 4.5 a request for `xhigh` is treated as `high`). Chat Completions uses `reasoning_effort`, the Responses API `reasoning.effort`. `presencePenalty`, `frequencyPenalty` and `stop` cause an error on reasoning models; `logprobs` is unsupported from the 4.20 models on [grok-f10] [xai-docs-chatref] [xai-docs-respref].
- **Encrypted reasoning.** On the Responses API a request can ask for `reasoning.encrypted_content` with `include`; Grok 4.7 returns it on every response. Passing reasoning items back unchanged keeps the model's reasoning and cache hits across turns when the client manages history itself; Chat Completions has no field for it [grok-f10] [xai-docs-gen].
- **Caching.** Caching is automatic for a matching prefix of the message list and is not guaranteed (entries can be evicted, requests can land on another server). The docs say to send `prompt_cache_key` (Responses) or the `x-grok-conv-id` header (Chat Completions and gRPC) so a conversation is routed to one server. Editing, removing or reordering earlier messages breaks the cache; for reasoning models, leaving out the previous `reasoning_content` is named the top cause of misses. Cached input is billed at a quarter of the input price for 4.7 and 4.6 ($0.50 against $2.00) and a fifth for the coding model ($0.20 against $1.00). `cached_tokens` in the usage object shows hits [xai-docs-cache-keys] [grok-f17] [xai-docs-cache-usage].
- **Long-context pricing.** A request whose prompt reaches 200k tokens is billed at the higher rate for every token in it (double the standard rate for 4.7, 4.6 and the coding model) [xai-docs-pricing].
- **Function calling.** Arguments always conform to the tool schema (the `strict` flag is on implicitly), the root schema must be an object (or a union of objects), calls may be parallel by default, a streamed function call arrives whole in one chunk, and `tool_choice` takes `auto`, `required`, `none` or a named function [xai-docs-fc].
- **Structured outputs** accept a practical subset of JSON Schema with guaranteed conformance inside stated limits (see each model file) [xai-docs-so].
- **Images** as input: JPEG or PNG, up to 20 MiB, no stated image-count limit, as a URL or a base64 data URL. The docs advise against storing request history on the server when sending images, because the request may fail [xai-docs-img].
- **Verbosity of thinking has risen.** Artificial Analysis measured output tokens per Intelligence Index task: about 14k for Grok 4.5 (July 2026 article), 36k (high) and 38k (xhigh) for 4.6, 81k (xhigh) for 4.7 (September article); the index version changed between the articles (M) [grok-f19] [aa-grok-47].
- **Factuality.** Artificial Analysis's AA-Omniscience hallucination rate was 25% for Grok 4.3 and 54% for 4.5 (July 2026 article), 34% for 4.6 (high) and 29% for 4.7 (xhigh) (September article) (M) [grok-f19] [aa-grok-47].
- **Coding data.** The 4.6 and 4.7 cards say each model had supplemental training on anonymised Cursor workflow data, and Cursor says Grok 4.5 had continued training on Cursor data. The cards' coding results come from a mix of Grok Build and evaluator harnesses (see System-card practice) [xai-47-card] [xai-46-card] [cursor-grok-45].
- **Cursor's view.** Cursor, now owned by SpaceX [cursor-joining-spacex], reports from production traffic that Grok models are strong value on broad routine work (for example Git commands and general database operations) and uses Grok as the cheaper route in its model router [cursor-router].

## Open questions

- xAI publishes no prompting guide for 4.x models, so how wording, structure and system-prompt length affect them is known only from outside measurement, which is thin.
- Whether the API adds a safety system prefix to 4.x requests, as it did for 2025 models, is not stated.
- Which maximum output the models can produce is not published; the docs say there is no text output limit and set a 128,000 default cap.
- Whether the Fast tier and the standard tier give identical results is stated by the maker and untested by anyone found.
- A successor to Grok 4.7 has not been published; reports of one are secondary and undated.
- Whether Grok Voice Think Fast 1.0 can still be called, and what the maximum length of a voice session is. The docs state neither.

## Sources

- [xai-47-card] <https://media.x.ai/v1/website/4p7card-5eccc980.pdf>, kind L, read 2026-10-03.
- [xai-docs-models] <https://docs.x.ai/developers/models>, kind L, read 2026-10-03.
- [xai-docs-pricing] <https://docs.x.ai/developers/pricing>, kind L, read 2026-10-03.
- [grok-migration-may15] <https://docs.x.ai/developers/migration/may-15-retirement.md>, kind L, read 2026-10-03.
- [xai-release-notes] <https://docs.x.ai/developers/release-notes>, kind L, read 2026-10-03.
- [xai-build01-news] <https://x.ai/news/grok-build-0-1>, kind L, read 2026-10-03.
- [xai-45-news] <https://x.ai/news/grok-4-5>, kind L, read 2026-10-03.
- [xai-46-news] <https://x.ai/news/grok-4-6>, kind L, read 2026-10-03.
- [xai-46-card] <https://media.x.ai/v1/website/card-4p6-4cd2dc57.pdf>, kind L, read 2026-10-03.
- [xai-47-news] <https://x.ai/news/grok-4-7>, kind L, read 2026-10-03.
- [xai-docs-47-overview] <https://docs.x.ai/developers/grok-4-7>, kind L, read 2026-10-03.
- [grok-f10] <https://docs.x.ai/developers/model-capabilities/text/reasoning.md>, kind L, read 2026-10-03.
- [xai-docs-regions] <https://docs.x.ai/developers/advanced-api-usage/regions>, kind L, read 2026-10-03.
- [xai-docs-47] <https://docs.x.ai/developers/models/grok-4.7>, kind L, read 2026-10-03.
- [xai-docs-build01] <https://docs.x.ai/developers/models/grok-build-0.1>, kind L, read 2026-10-03.
- [xai-docs-compare] <https://docs.x.ai/developers/model-capabilities/text/comparison>, kind L, read 2026-10-03.
- [xai-docs-gen] <https://docs.x.ai/developers/model-capabilities/text/generate-text>, kind L, read 2026-10-03.
- [xai-docs-respref] <https://docs.x.ai/developers/rest-api-reference/inference/responses>, kind L, read 2026-10-03.
- [xai-docs-chatref] <https://docs.x.ai/developers/rest-api-reference/inference/chat-completions>, kind L, read 2026-10-03.
- [xai-docs-fc] <https://docs.x.ai/developers/tools/function-calling>, kind L, read 2026-10-03.
- [xai-docs-46] <https://docs.x.ai/developers/models/grok-4.6>, kind L, read 2026-10-03.
- [xai-docs-rates] <https://docs.x.ai/developers/rate-limits>, kind L, read 2026-10-03.
- [xai-docs-security] <https://docs.x.ai/developers/faq/security>, kind L, read 2026-10-03.
- [xai-docs-index] <https://docs.x.ai/llms.txt>, kind L, read 2026-10-03.
- [grok-f15] <http://web.archive.org/web/20251118014240/https://docs.x.ai/docs/guides/grok-code-prompt-engineering>, kind L, read 2026-10-03.
- [xai-docs-cache-best] <https://docs.x.ai/developers/advanced-api-usage/prompt-caching/best-practices>, kind L, read 2026-10-03.
- [grok-f1] <https://docs.x.ai/build/features/project-rules.md>, kind L, read 2026-10-03.
- [xai-build-prompt] <https://raw.githubusercontent.com/xai-org/grok-build/main/crates/codegen/xai-grok-agent/templates/prompt.md>, kind L, read 2026-10-03.
- [grok-f11] <https://docs.x.ai/developers/community/microsoft-foundry.md>, kind L, read 2026-10-03.
- [cursor-token-eff] <https://cursor.com/blog/improved-token-efficiency>, kind L, read 2026-10-03.
- [grok-g7] <https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf>, kind L, read 2026-10-03.
- [xai-codefast-card] <https://data.x.ai/2025-08-26-grok-code-fast-1-model-card.pdf>, kind L, read 2026-10-03.
- [xai-docs-cache-keys] <https://docs.x.ai/developers/advanced-api-usage/prompt-caching/maximizing-cache-hits>, kind L, read 2026-10-03.
- [grok-f17] <https://docs.x.ai/developers/advanced-api-usage/prompt-caching/multi-turn.md>, kind L, read 2026-10-03.
- [xai-docs-cache-usage] <https://docs.x.ai/developers/advanced-api-usage/prompt-caching/usage-and-pricing>, kind L, read 2026-10-03.
- [xai-docs-so] <https://docs.x.ai/developers/model-capabilities/text/structured-outputs>, kind L, read 2026-10-03.
- [xai-docs-img] <https://docs.x.ai/developers/model-capabilities/images/understanding>, kind L, read 2026-10-03.
- [grok-f19] <https://artificialanalysis.ai/articles/grok-4-5-brings-spacexai-to-the-the-intelligence-frontier>, kind M, read 2026-10-03.
- [aa-grok-47] <https://artificialanalysis.ai/articles/benchmarking-grok-4-7>, kind M, read 2026-10-03.
- [cursor-joining-spacex] <https://cursor.com/blog/joining-spacex>, kind L, read 2026-10-03.
- [cursor-router] <https://cursor.com/blog/how-cursor-router-works>, kind L, read 2026-10-03.
- [cursor-grok-45] <https://cursor.com/docs/models/grok-4-5>, kind L, read 2026-10-03.
- [cursor-grok-45-card] <https://cursor.com/blog/grok-4-5-model-card>, kind L, read 2026-10-03.
- [grok-f9] <https://artificialanalysis.ai/articles/xai-launches-grok-4-3-with-improved-agentic-performance-and-lower-pricing>, kind M, read 2026-10-03.
- [xai-voice-s2s] <https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech>, kind L, read 2026-10-03.
- [xai-voice-prompting] <https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech/prompting-guide>, kind L, read 2026-10-03.
- [xai-voice-announce-2] <https://x.ai/news/grok-voice-think-fast-2>, kind L, read 2026-10-03.
- [xai-voice-announce-1] <https://x.ai/news/grok-voice-think-fast-1>, kind L, read 2026-10-03.
- [xai-voice-pricing] <https://docs.x.ai/developers/pricing>, kind L, read 2026-10-03.
- [xai-voice-rates] <https://docs.x.ai/developers/rate-limits>, kind L, read 2026-10-03.
- [xai-voice-release-notes] <https://docs.x.ai/developers/release-notes>, kind L, read 2026-10-03.
