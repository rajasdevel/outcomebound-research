---
last_checked: 2026-10-03
volatility: MONITOR (lineage, guides and API behaviour change at each release; prices, plans and thinking defaults are VOLATILE and are held in the model cards)
sources:
  - https://platform.minimax.io/docs/guides/models-intro
  - https://platform.minimax.io/docs/guides/text-generation
  - https://platform.minimax.io/docs/api-reference/text-anthropic-api
  - https://platform.minimax.io/docs/api-reference/text-openai-api
  - https://platform.minimax.io/docs/api-reference/text-chat-openai
  - https://platform.minimax.io/docs/api-reference/responses-create
  - https://platform.minimax.io/docs/guides/text-m3-function-call
  - https://platform.minimax.io/docs/guides/text-m2-agent-generalization
  - https://platform.minimax.io/docs/api-reference/text-prompt-caching
  - https://platform.minimax.io/docs/api-reference/anthropic-api-compatible-cache
  - https://platform.minimax.io/docs/guides/rate-limits
  - https://platform.minimax.io/docs/guides/pricing-paygo
  - https://platform.minimax.io/docs/guides/pricing-token-plan
  - https://platform.minimax.io/docs/release-notes/models
  - https://platform.minimax.io/docs/m-plan/intro
  - https://platform.minimax.io/docs/m-plan/token-plan-notice
  - https://platform.minimax.io/docs/m-plan/claude-code
  - https://platform.minimax.io/docs/m-plan/codex
  - https://platform.minimax.io/docs/guides/local-deploy-m3
  - https://www.minimax.io/blog/minimax-m3
  - https://www.minimax.io/models/text/m3
  - https://www.minimax.io/news/minimax-m27-en
  - https://www.minimax.io/news/minimax-m21
  - https://platform.minimax.io/docs/llms-full.txt
  - https://agent.minimax.io/tools/m3-1-flash-preview
  - https://huggingface.co/MiniMaxAI/MiniMax-M3
  - https://huggingface.co/MiniMaxAI/MiniMax-M3/blob/main/LICENSE
  - https://huggingface.co/MiniMaxAI/MiniMax-M2.7
  - https://huggingface.co/MiniMaxAI/MiniMax-M2.7/blob/main/LICENSE
  - https://github.com/MiniMax-AI/MiniMax-M2.7/blob/main/docs/tool_calling_guide.md
  - https://arxiv.org/abs/2606.13392
  - https://arxiv.org/abs/2601.10343
  - https://openrouter.ai/api/v1/models
  - https://artificialanalysis.ai/models/minimax-m3
  - https://artificialanalysis.ai/models/minimax-m2-7
  - https://artificialanalysis.ai/agents/coding
  - https://datanorth.ai/news/minimax-releases-m3-1-flash-preview
  - https://startupfortune.com/minimax-slips-a-new-coding-model-into-its-agent-tool-without-a-price-tag/
  - https://platform.minimax.io/docs/api-reference/speech-t2a-http
  - https://platform.minimax.io/docs/guides/speech-t2a-websocket
  - https://platform.minimax.io/docs/api-reference/voice-design-design
  - https://www.minimax.io/news/minimax-speech-28
  - https://www.minimax.io/news/minimax-speech-26
  - https://artificialanalysis.ai/text-to-speech
---

# MiniMax models

MiniMax publishes its M series of language models through its own API, through subscription plans used in its own
agent application and in third-party coding tools, and (for M2.7 and M3) as open weights. This page holds what is true
of every MiniMax model in this library: the lineage, the API surface, the guidance MiniMax publishes, what it publishes
instead of a system card, and behaviour that carries across models. The model files say what differs for each:
[MiniMax M3](MiniMax-M3.md), [MiniMax M2.7](MiniMax-M2.7.md) and
[MiniMax M3.1 Flash Preview](MiniMax-M3.1-Flash-Preview.md). MiniMax also sells speech synthesis models (Speech 2.8 and Speech 2.6) through the same platform. Two of them, Speech 2.8 HD and Speech 2.8 Turbo, are in this library as voice actor models, and their files are [MiniMax Speech 2.8 HD](speech-2.8-hd.md) and [MiniMax Speech 2.8 Turbo](speech-2.8-turbo.md).

## Models and lineage

Dates are from MiniMax's release notes unless a row says otherwise. [minimax-release-notes]

| Model | Released | What changed for people who write prompts or call the API |
| --- | --- | --- |
| M2 | 2025-10-27 | Reasons between tool calls (interleaved thinking); the full history, thinking included, must be kept; 204,800-token context. |
| M2.1 | 2025-12-22 | Coding focus; MiniMax says replies and thought chains are more concise than M2's, results are stable in Claude Code, Droid, Cline, Kilo Code, Roo Code and BlackBox, and it supports Skill.md, Claude.md and agent.md files, cursor rules and slash commands. |
| M2.5 | 2026-02 | Programming, tool calling and search, office work; still listed as a legacy model. |
| M2.7 | 2026-03-18 | Agent teams, skills and dynamic tool search; thinking always on; a faster `-highspeed` id of the same model; open weights from 2026-04-09. |
| M3 | 2026-06-01 | About 428B parameters (23B active), native image and video input, 1M-token context from a sparse-attention design, thinking switchable; open weights from 2026-06-02. |
| M3.1 Flash Preview | 2026-09-27 (press date) | Always-on thinking with five effort levels; offered only through the M Plan subscription and MiniMax Code; no pay-as-you-go API, no weights, no price. |
| Speech 2.6 | 2025-10-29 (release notes; the launch page says 2025-10-30) | Speech synthesis, HD and Turbo: an `emotion` request field with `fluent` and `whisper` values, pause markers and inline respelling; under 250 ms end to end per MiniMax. No inline sound tags, so it has no file here. [mm-release-notes, mm-news-26, mm-t2a-http] |
| Speech 2.8 | 2026-01-23 (release notes; Artificial Analysis dates it 2026-02-14) | Speech synthesis, HD and Turbo: adds 19 interjection tags in parentheses (laughs, sighs, breath and others); the `emotion` field loses `fluent` and `whisper`. Files: [HD](speech-2.8-hd.md), [Turbo](speech-2.8-turbo.md). [mm-release-notes, mm-t2a-http] |

Other facts about the line:

- A dialogue model, MiniMax-M2-her (64K context, replies of up to 2,048 tokens, role-play and character chat), is
  listed among the legacy language models and has no file here. [minimax-models-intro, openrouter-models]
- Classes in this library: MiniMax M (M2.7 and M3) and MiniMax M Flash (M3.1 Flash Preview). MiniMax's pages call the
  preview "the latest M-series language model", so it could be read as the 3.1 generation of the M class, which would
  leave M2.7 outside the two-generation scope; the card keeps it as a separate Flash class because its id says Flash and
  no non-Flash M3.1 exists. [minimax-text-generation]
- Artificial Analysis marks M2.7 deprecated and M3 current. MiniMax's pages still list and price M2.7 and publish no
  retirement date. [aa-minimax-m2-7, minimax-pricing]
- The M3 and M2.7 licences both carry a prohibited-use appendix; M2.7's licence is non-commercial, M3's allows commercial
  use under conditions. See the model files. [minimax-m3-license, minimax-m27-license]
- Classes in this library for speech: MiniMax Speech HD and MiniMax Speech Turbo, both at generation 2.8. Speech 2.6 and earlier (Speech-02, Speech-01) have no file. Pay-as-you-go lists US$100 per 1M characters for HD and US$60 for Turbo. [mm-paygo, mm-t2a-http]

## API surface

**Endpoints.** The Anthropic-compatible endpoint is the one MiniMax recommends, because it carries thinking blocks and
interleaved thinking. [minimax-text-generation]

| Protocol | Base URL |
| --- | --- |
| Anthropic Messages (recommended) | `https://api.minimax.io/anthropic` (a China endpoint, `api.minimax.cn`, is named in the tool-use guide) |
| OpenAI Chat Completions | `https://api.minimax.io/v1` |
| OpenAI Responses | `https://api.minimax.io/v1/responses` |

Pay-as-you-go uses an Open Platform API key; the M Plan and Token Plan use a Subscription Key. Model ids:
`MiniMax-M3.1-Flash-Preview` (M Plan only), `MiniMax-M3`, `MiniMax-M2.7`, `MiniMax-M2.7-highspeed`, and the legacy
`MiniMax-M2.5`, `-M2.1` and `-M2` ids with their `-highspeed` siblings. A token-counting endpoint exists for M3 and
M3.1 Flash Preview on the Anthropic-compatible API. [minimax-text-generation, minimax-anthropic-api, minimax-models-intro]

**Parameters** (Anthropic-compatible and OpenAI-compatible references). [minimax-anthropic-api, minimax-openai-api,
minimax-chat-openai-ref]

| Field | What the references say |
| --- | --- |
| `temperature` | 0 to 2, recommended 1 (the Responses reference gives a range of 0 to 1). |
| `top_p` | 0 to 1; default 0.95 for M3 and M3.1 Flash Preview, 0.9 for the M2.x models. |
| `max_tokens` / `max_completion_tokens` | Thinking tokens count toward the limit; a value that is too small yields `stop_reason: max_tokens` or `finish_reason: length` with no text. For M3 and M3.1 Flash Preview the recommended `max_completion_tokens` is 131072 and the maximum 524288; for the others 65536 and 204800. |
| `thinking` | `adaptive` or `disabled`; the effect depends on the model (see below). |
| `output_config.effort` / `reasoning_effort` / `reasoning.effort` | Thinking depth for M3.1 Flash Preview only: `low`, `medium`, `high`, `xhigh`, `max`; default `max`; `none` returns HTTP 400. |
| `reasoning_split` | OpenAI-compatible: true returns thinking in a separate field; false leaves it inside `content` in `<think>` tags (M3.1 Flash Preview supports only true). |
| `service_tier` | `standard` or `priority`; priority costs 1.5 times the standard price and is admitted first. |
| `tools`, `tool_choice` | Supported on both protocols. |
| Ignored | On the Anthropic endpoint: `top_k`, `stop_sequences`, `mcp_servers`, `context_management`, `container`. On the OpenAI endpoint: `presence_penalty`, `frequency_penalty`, `logit_bias`; `n` must be 1; `function_call` is unsupported. |

**Thinking by model.** [minimax-anthropic-api, minimax-openai-api, minimax-responses-ref]

| Model | thinking omitted | `adaptive` | `disabled` |
| --- | --- | --- | --- |
| M3.1 Flash Preview | on | on | HTTP 400 (error code 2013) |
| M3 | off on the Anthropic and Responses endpoints; enabled on the OpenAI Chat Completions endpoint | on | off |
| M2.x (including M2.7) | on | on | accepted and ignored; thinking stays on |

On the Responses endpoint M3 thinks only when `effort` is set to a value other than none; effort does not tune its depth.

**Multimodal input** (M3 and M3.1 Flash Preview only). Images: JPEG, PNG, GIF or WEBP, URL or base64, up to 10 MB. Video: MP4,
AVI, MOV or MKV, up to 50 MB inline, or up to 512 MB through the Files API and an `mm_file://` id; frame rate
defaults to 1 and accepts 0.2 to 5. The request body may reach 64 MB. A `detail` field (`low`, `default`, `high`)
steers image tokens, roughly a few hundred, one to three thousand, and several thousand or more. Audio input is
unsupported. M2.x models take text and tool blocks only. [minimax-anthropic-api, minimax-openai-api]

**Caching.** Automatic prefix caching needs at least 512 input tokens and builds the prefix in the order tool list,
system prompt, user messages; MiniMax advises putting static content first and dynamic content last. The Anthropic
endpoint also supports explicit `cache_control` blocks. Hits show in `cache_read_input_tokens` or
`prompt_tokens_details.cached_tokens`. [minimax-prompt-caching, minimax-explicit-cache]

**Rate limits.** M3: 200 requests and 10M tokens a minute; M2.x: 500 requests and 20M tokens a minute. [minimax-rate-limits]

**Plans and prices.** Pay-as-you-go prices are in the cards. Token Plan (Plus US$22, Max US$55, Ultra US$132 a month)
is closed to new purchases; existing subscribers may keep it. Its successor, M Plan, has tiers Go, Explore and Build
and serves M3.1 Flash Preview. Prepaid Credits are also sold. [minimax-pricing, minimax-token-plan-pricing,
minimax-token-plan-notice, minimax-m-plan]

**Self-hosting.** M3 (about 444 GB as MXFP8, about 854 GB as BF16) is documented for SGLang on eight B200 cards as the
reference baseline, labelled experimental as of 2026-08-26 and running on a development image; the Hugging Face card
also names vLLM, Transformers, KTransformers and others. M2.7 is documented for SGLang, vLLM and Transformers, and
MiniMax strongly recommends the engines' own tool-call parsers because M2-series tool calls use an XML-style format.
Recommended sampling: temperature 1.0 and top_p 0.95 (M2.7 adds top_k 40 and a default system prompt naming the model).
[minimax-m3-local-deploy, minimax-m3-hf-readme, minimax-m27-hf-readme, minimax-m27-tool-guide]

**Speech endpoints.** Synchronous text to speech is `POST https://api.minimax.io/v1/t2a_v2` (up to 10,000 characters; streaming advised above 3,000), with a WebSocket and a bidirectional WebSocket on `wss://api.minimax.io/ws/v1/t2a_v2` and `/t2a_v2_bidi`, and an asynchronous job for up to 1M characters. `api-uw.minimax.io` is advised for US West. Model ids are `speech-2.8-hd`, `speech-2.8-turbo`, `speech-2.6-hd`, `speech-2.6-turbo`, `speech-02-hd`, `speech-02-turbo`, `speech-01-hd` and `speech-01-turbo`. The rate limit is 60 requests a minute. Voice design costs US$3 and rapid cloning US$1.5 per voice. [mm-t2a-http, mm-ws-guide, mm-limits, mm-paygo]

## Prompting guides

MiniMax publishes no prompting guide for its language models. A page once cited as one (a "prompting best practices" page under
the Token Plan docs) returns 404 now and has no replacement, so nothing from it is used here. The guidance that exists:

- **Agent post for M2 ("Aligning to What?").** M2 depends on interleaved thinking: the context is the model's memory, so
  the full session history, thinking steps included, should be kept; MiniMax says much of the reported underperformance
  came from harnesses that discard it. The post says the team trained against perturbations in every part of a run (the
  tool set, system prompt, user prompt, environment and tool responses), not only new tools, so that results hold across
  scaffolds. [minimax-agent-generalization]
- **Tool use and interleaved thinking guide (M3).** The key rule is to return the model's full response every turn:
  on the Anthropic protocol append the whole `response.content` list (thinking, text and tool-use blocks); on the OpenAI
  protocol append the full assistant message, including `tool_calls`, and the thinking field (`<think>` text in
  `content`, or `reasoning_details` / `reasoning_content` when it is split out; the pages name the field
  differently). The model reflects on tool output before each next action. [minimax-m3-function-call]
- **M3 launch post.** Thinking on for complex reasoning, agent work and long collaboration; off for latency-sensitive
  chat and completion, with the same price; M3 was trained against a simulated user so that it clarifies, accepts
  correction and switches tasks within a session. [minimax-m3-blog]
- **Caching page.** The page advises static or repeated content first and dynamic content last, and watching the cache
  counters in `usage`. [minimax-prompt-caching]
- **Coding-tool setup pages (M Plan).** For M3.1 Flash Preview in Claude Code or Codex, the pages set the client's
  context window and automatic-compaction threshold to 512K (524,288) for everyday work and keep 1M for tasks that need
  long retention; in a 200-task ProgramBench comparison MiniMax reports similar performance and about 20% lower
  estimated cost at 512K.
  [minimax-m-plan-codex, minimax-m-plan-claude-code]
- **Dialogue model page (M2-her).** The page recommends defining the model's role with `system` and the user's with
  `user_system`, giving one to three example exchanges, keeping the full history, and sizing `max_completion_tokens`
  (up to 2,048). [minimax-llms-full]
- **How the advice moved.** M2: keep thinking in history. M2.1: claims support for other tools' instruction files [minimax-m21-news]. M2.7:
  skills (97% adherence over 40 skills of more than 2,000 tokens in MiniMax's own set). M3: a thinking toggle and
  clarifying behaviour. M3.1 Flash Preview: thinking cannot be removed, and MiniMax points to a lower effort to save
  tokens and time.
  [minimax-m27-news, minimax-text-generation]

For speech, MiniMax documents its controls in the API reference only: the `emotion` field, interjection tags (2.8 only), pause markers of the form `<#x#>`, inline respelling, `voice_modify` sliders and `language_boost`. It publishes no separate guide on writing text for the speech models. [mm-t2a-http]

## System-card practice

MiniMax publishes no system card, safety report or model card with safety sections for any model in this library. A
release brings a blog or news post with benchmark rows and an evaluation-methods list, a short Hugging Face card, and
the licence. The "technical report" link on M3's Hugging Face card is the paper on MiniMax Sparse Attention (arXiv
2606.13392), an architecture paper whose experiments use a 109B-parameter multimodal model and whose abstract has no
safety, refusal or red-team content. [minimax-m3-msa-paper]
What exists on safety and misuse:

- **Licences.** M3's licence is free for non-commercial use; commercial use needs a "Built with MiniMax M3" notice and a
  one-time notice to MiniMax, or prior written authorization above US$20 million yearly revenue. Its appendix prohibits
  use for content banned by law, any military purpose, harming minors, harmful disinformation and discrimination. M2.7's
  licence is non-commercial (personal, non-profit and research use free) with commercial use by prior authorization, and has
  the same prohibited-use appendix. [minimax-m3-license, minimax-m27-license]
- **Not published.** Refusal and over-refusal rates, sycophancy, deception or sandbagging tests, reward-hacking or
  test-special-casing findings, prompt-injection results, cyber or biology evaluations and any request classifier.
  M3 can operate a desktop application, by MiniMax's account, and no agentic-safety evaluation of that is published.
- **Independent signals.** Artificial Analysis's AA-Omniscience hallucination rate (wrong answers given in place of
  declining) is 18.4% for M3 and 35.6% for M2.7. No independent coding-agent safety audit of a MiniMax model was found.
  [aa-minimax-m3, aa-minimax-m2-7]

## Family-wide behaviour

- **Return the thinking.** Every MiniMax model since M2 reasons between tool calls; dropping thinking blocks from the
  history is the failure MiniMax names most. This holds on both protocols. [minimax-agent-generalization,
  minimax-m3-function-call]
- **Thinking budget shares the output limit.** Thinking tokens count toward `max_tokens`; too small a value ends the reply
  with no text. [minimax-anthropic-api]
- **Defaults differ across endpoints and models** (see the thinking table); a request that omits `thinking` behaves
  differently on the Anthropic and OpenAI endpoints for M3. [minimax-anthropic-api, minimax-openai-api]
- **Sampling.** Temperature 1.0 is the recommendation for every model; top_p is 0.95 for M3-class and 0.9 or 0.95 for M2.x
  depending on the page. Penalties are ignored. [minimax-openai-api, minimax-m27-hf-readme]
- **Context.** M3-class models take 1M tokens; MiniMax's M3 page says the API guarantees at least 512K, and OpenRouter
  lists 1,048,576 for M3; M2.x models take 204,800. [minimax-m3-page, openrouter-models]
- **Instruction following across harnesses (measured on earlier models).** OctoBench, co-authored by MiniMax and a Fudan
  team, tested eight models of January 2026 including MiniMax-M2 and M2.1 in three coding harnesses: per-check compliance
  was 79.75% to 85.64% for all models, but the share of tasks satisfying every check was only 9.66% to 28.11% (M2.1:
  18.15%); skill-file constraints were a persistent bottleneck (M2.1 12.33%, the top-scoring model 58.45%); in conflicts, a system
  prompt beat project documentation and a user query beat project documentation, while system prompt against user query
  varied by model. M3 and M2.7 were not tested. [octobench]
- **Hallucination and verbosity (Artificial Analysis).** On its index run M3 had an AA-Omniscience hallucination rate of
  18.4% (M2.7: 35.6%) and generated about 117M output tokens (M2.7: about 92M). [aa-minimax-m3, aa-minimax-m2-7]

## Open questions

- Whether MiniMax will publish a system card or safety report, or a prompting guide, for M3 or its successor.
- Whether M3.1 Flash Preview will get weights, a price and pay-as-you-go access, and under what class and name.
- How M3 behaves when thinking is adaptive and the harness hides or drops thinking blocks.
- Whether the three endpoints' different M3 thinking defaults are intended; the docs describe them without explaining.
- Instruction-following results for M2.7, M3 and M3.1 Flash Preview on OctoBench or a similar benchmark.
- A latency figure for Speech 2.8, and how strongly the emotion field and the interjection tags change delivery.

## Sources

Every source below was read on 2026-10-03, except the speech sources with the prefix `mm-` and `aa-tts-board`, which were read on 2026-10-04. Kinds: L is the maker's own page, M an independent measurement, P a paper or
standard, A a practitioner, reseller or press document.

- [minimax-models-intro] https://platform.minimax.io/docs/guides/models-intro (L)
- [minimax-text-generation] https://platform.minimax.io/docs/guides/text-generation (L)
- [minimax-anthropic-api] https://platform.minimax.io/docs/api-reference/text-anthropic-api (L)
- [minimax-openai-api] https://platform.minimax.io/docs/api-reference/text-openai-api (L)
- [minimax-chat-openai-ref] https://platform.minimax.io/docs/api-reference/text-chat-openai (L)
- [minimax-responses-ref] https://platform.minimax.io/docs/api-reference/responses-create (L)
- [minimax-m3-function-call] https://platform.minimax.io/docs/guides/text-m3-function-call (L)
- [minimax-agent-generalization] https://platform.minimax.io/docs/guides/text-m2-agent-generalization (L)
- [minimax-prompt-caching] https://platform.minimax.io/docs/api-reference/text-prompt-caching (L)
- [minimax-explicit-cache] https://platform.minimax.io/docs/api-reference/anthropic-api-compatible-cache (L)
- [minimax-rate-limits] https://platform.minimax.io/docs/guides/rate-limits (L)
- [minimax-pricing] https://platform.minimax.io/docs/guides/pricing-paygo (L)
- [minimax-token-plan-pricing] https://platform.minimax.io/docs/guides/pricing-token-plan (L)
- [minimax-token-plan-notice] https://platform.minimax.io/docs/m-plan/token-plan-notice (L)
- [minimax-m-plan] https://platform.minimax.io/docs/m-plan/intro (L)
- [minimax-m-plan-claude-code] https://platform.minimax.io/docs/m-plan/claude-code (L)
- [minimax-m-plan-codex] https://platform.minimax.io/docs/m-plan/codex (L)
- [minimax-release-notes] https://platform.minimax.io/docs/release-notes/models (L)
- [minimax-m3-local-deploy] https://platform.minimax.io/docs/guides/local-deploy-m3 (L)
- [minimax-m3-blog] https://www.minimax.io/blog/minimax-m3 (L)
- [minimax-m3-page] https://www.minimax.io/models/text/m3 (L)
- [minimax-m27-news] https://www.minimax.io/news/minimax-m27-en (L)
- [minimax-m21-news] https://www.minimax.io/news/minimax-m21 (L)
- [minimax-m3-hf-readme] https://huggingface.co/MiniMaxAI/MiniMax-M3 (L)
- [minimax-m3-license] https://huggingface.co/MiniMaxAI/MiniMax-M3/blob/main/LICENSE (L)
- [minimax-m27-hf-readme] https://huggingface.co/MiniMaxAI/MiniMax-M2.7 (L)
- [minimax-m27-license] https://huggingface.co/MiniMaxAI/MiniMax-M2.7/blob/main/LICENSE (L)
- [minimax-m27-tool-guide] https://github.com/MiniMax-AI/MiniMax-M2.7/blob/main/docs/tool_calling_guide.md (L)
- [minimax-llms-full] https://platform.minimax.io/docs/llms-full.txt (L; the dialogue-model page is inside this file)
- [octobench] https://arxiv.org/abs/2601.10343 (P; co-authored by MiniMax, so not fully independent)
- [minimax-m3-msa-paper] https://arxiv.org/abs/2606.13392 (P)
- [aa-minimax-m3] https://artificialanalysis.ai/models/minimax-m3 (M)
- [aa-minimax-m2-7] https://artificialanalysis.ai/models/minimax-m2-7 (M)
- [openrouter-models] https://openrouter.ai/api/v1/models (A)
- [mm-t2a-http] https://platform.minimax.io/docs/api-reference/speech-t2a-http (L)
- [mm-ws-guide] https://platform.minimax.io/docs/guides/speech-t2a-websocket (L)
- [mm-limits] https://platform.minimax.io/docs/guides/rate-limits (L)
- [mm-paygo] https://platform.minimax.io/docs/guides/pricing-paygo (L)
- [mm-release-notes] https://platform.minimax.io/docs/release-notes/models (L)
- [mm-news-26] https://www.minimax.io/news/minimax-speech-26 (L)
- [mm-news-28] https://www.minimax.io/news/minimax-speech-28 (L)
- [aa-tts-board] https://artificialanalysis.ai/text-to-speech (M)
