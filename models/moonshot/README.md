---
last_checked: 2026-10-03
volatility: MONITOR (lineage, guides and API behaviour change at each release)
sources:
  - https://platform.kimi.ai/docs/models
  - https://platform.kimi.ai/docs/platform-changelog
  - https://platform.kimi.ai/docs/api/overview
  - https://platform.kimi.ai/docs/api/models-overview
  - https://platform.kimi.ai/docs/pricing/chat
  - https://platform.kimi.ai/docs/pricing/limits
  - https://platform.kimi.ai/docs/guide/kimi-k3-quickstart
  - https://platform.kimi.ai/docs/guide/kimi-k3-tool-calling-best-practice
  - https://platform.kimi.ai/docs/guide/kimi-k2-7-code-quickstart
  - https://platform.kimi.ai/docs/guide/kimi-k2-6-quickstart
  - https://platform.kimi.ai/docs/guide/use-reasoning-effort
  - https://platform.kimi.ai/docs/guide/use-thinking-models
  - https://platform.kimi.ai/docs/guide/use-tool-choice
  - https://platform.kimi.ai/docs/guide/use-dynamic-tool-loading
  - https://platform.kimi.ai/docs/guide/tool-call-repeat
  - https://platform.kimi.ai/docs/guide/response_format
  - https://platform.kimi.ai/docs/guide/use-partial-mode-feature-of-kimi-api
  - https://platform.kimi.ai/docs/guide/use-kimi-vision-model
  - https://platform.kimi.ai/docs/guide/context-caching
  - https://platform.kimi.ai/docs/guide/prompt-best-practice
  - https://platform.kimi.ai/docs/guide/benchmark-best-practice
  - https://platform.kimi.ai/docs/guide/claude-code-kimi
  - https://platform.kimi.ai/docs/guide/zero-data-retention
  - https://platform.kimi.ai/docs/guide/troubleshooting
  - https://platform.kimi.ai/docs/api/messages
  - https://www.kimi.ai/blog/kimi-k3
  - https://www.kimi.ai/blog/kimi-vendor-verifier
  - https://www.kimi.ai/blog
  - https://huggingface.co/moonshotai/Kimi-K3
  - https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE
  - https://huggingface.co/moonshotai/Kimi-K2.7-Code
  - https://huggingface.co/moonshotai/Kimi-K2.6
  - https://www.kimi.com/blog/kimi-k2-6.html
  - https://arxiv.org/html/2607.24653
  - https://www.aisi.gov.uk/blog/preliminary-assessment-of-kimi-k3s-cyber-capabilities
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-moonshot-ai-kimi-k3.html
---

# Moonshot Kimi models

Moonshot AI is a Chinese laboratory that serves the Kimi models through the Kimi API platform and publishes their weights. On 2026-10-03 three of its models have files here: [Kimi K3](kimi-k3.md), its flagship, [Kimi K2.6](kimi-k2.6.md), the general model of the generation before it, and [Kimi K2.7 Code](kimi-k2.7-code.md), a coding model built on K2.6. This page holds what is true of all three: the lineage, the API they share, the guides Moonshot publishes, what its releases include on safety, and behaviour that does not change between them. Each model file says what differs for that model.

## Models and lineage

What Moonshot's changelog, model list, blog and model cards record ([kimi-changelog], [kimi-models], [kimi-blog-index]):

| Date | Release | Notes |
| --- | --- | --- |
| 2025-07 | Kimi K2 | Open-weight mixture-of-experts model; a `0905` revision followed in 2025-09. |
| 2025-11 | K2 Thinking | A reasoning model; the `kimi-k2` ids were retired on 2026-05-25. |
| 2026-01 | K2.5 | Retired from the API on 2026-08-31, together with the `moonshot-v1` models. |
| 2026-04-20 | [K2.6](kimi-k2.6.md) | General model with text, image and video input, thinking on by default and switchable, 256K context; 1T total parameters and 32B active. Still served. |
| 2026-06 | K2.7 Code | Coding-focused model built on K2.6; thinking always on; a `kimi-k2.7-code-highspeed` id serves the same weights faster at twice the price. Public weights first appeared on 2026-06-11. |
| 2026-07-16 | K3 | 2.8T total parameters, 104B active, 1M-token context, native vision; weights published 2026-07-27. On Amazon Bedrock from 2026-09-18. |

How the models are classed here:

- **Kimi K, generation 3.** K3 is the current model. The generation before it is K2.x; its newest general model, [K2.6](kimi-k2.6.md), is still served and has a file. Older K2 ids are retired and out of scope.
- **Kimi K Code, generation 2.7.** K2.7 Code has no successor: Moonshot has not released a K3 coding variant, and its pages describe K3 itself as the model for long-horizon coding.
- **Architecture.** K2.6 and K2.7 Code are one-trillion-parameter models with 384 experts, 8 chosen per token, and multi-head latent attention. K3 changes the attention (Kimi Delta Attention, a linear-attention layer, in 69 of 93 layers with gated latent attention in the rest) and uses 896 experts with 16 chosen per token. K3's weights are trained for 4-bit weights with 8-bit activations (MXFP4/MXFP8); K2.7 Code uses 4-bit integer weights [kimi-k3-hf] [kimi-k27-code-hf].
- **Licences.** K2.7 Code (and K2.6) use a modified MIT licence that adds one condition: a product with more than 100 million monthly users or more than $20 million a month in revenue must show the model's name in its interface. The K3 licence is custom: it allows use, copying, modification and resale, keeps the same name-display condition, and adds a rule for "Model as a Service" businesses (offering third parties meaningful control over inference or fine-tuning) with more than $20 million in revenue over twelve months, which must sign a separate agreement; internal use and use through Moonshot's own products or certified inference partners is exempt. This is a summary, not legal advice [kimi-k3-license].

## API surface

All from Moonshot's documentation read on 2026-10-03 ([kimi-api-overview], [kimi-model-params], [kimi-k3-quickstart]).

**Endpoints and ids**

- Base URL `https://api.moonshot.ai`. OpenAI Chat Completions and the OpenAI Responses format at `/v1`; the Anthropic Messages format at `/anthropic`. Authentication is a bearer key from the Kimi platform console.
- Ids: `kimi-k3`, `kimi-k2.7-code`, `kimi-k2.7-code-highspeed` (same model as the previous, faster), `kimi-k2.6`. Retired and returning 404: the `kimi-k2` series (2026-05-25), `kimi-k2.5` and `moonshot-v1` (2026-08-31). Claude Code reaches K3 through the alias `kimi-k3[1m]` on the Anthropic endpoint [kimi-claude-code].
- K3 is unlocked after a first top-up of at least one dollar; rate limits follow cumulative top-ups, from 1 concurrent request and 3 requests a minute at the lowest level to 100 and 300 at the top [kimi-limits].

**Limits and defaults**

- Context windows: 1,048,576 tokens for K3 and 262,144 for K2.7 Code and K2.6. Output is bounded by the window minus the prompt; K3's `max_completion_tokens` defaults to 131,072 and can reach 1,048,576 [kimi-troubleshooting].
- Sampling is fixed, as the [model-parameter rules below](#family-wide-behaviour) set out. The OpenAI SDK needs `extra_body` for the Kimi-specific `thinking` field; `partial` is a flag on an assistant message, not a top-level field [kimi-api-overview].
- Prices per million tokens: K3 $3.00 input, $15.00 output, $0.30 cached input, with cache writes at $3.00 for a five-minute lifetime or $6.00 for one hour. K2.7 Code $0.95, $4.00 and $0.19. K2.6 $0.95, $4.00 and $0.16. There are no context-length surcharges [kimi-pricing].

**Features**

- Context caching is automatic for repeated prefixes. K3 entries live five minutes by default or one hour when the request asks for it (`prompt_cache_options.ttl` on Chat Completions and Responses, a top-level `cache_control` on the Messages format, where a request without it only reads the cache and writes nothing); each hit refreshes the entry; caches are isolated per organisation and cannot be cleared by hand. Separately billed cache writes apply to K3 only; Moonshot's caching FAQ says K2.7 Code and K2.6 do not support them [kimi-context-caching].
- Tool calling with `tool_choice` (`auto`, `none`, `required` on K3), dynamic tool loading (K3 only), official tools through a Formula endpoint, and a web-search API launched in September 2026. Moonshot says the older built-in web search is being updated and is not recommended for the near term [kimi-k3-quickstart].
- Files API for text extraction, images and videos (referenced as `ms://<file id>`); a Batch API; Zero Data Retention for enterprise customers, which does not cover images or videos sent as direct file uploads. The ZDR page says enterprise data is not used for training by default and that automated content-safety review applies to all traffic [kimi-zdr].
- Self-hosting: vLLM, SGLang and (K3) TokenSpeed are listed runtimes; K3's weights need large accelerator groups, and Moonshot recommends supernode deployments of 64 or more accelerators [kimi-k3-hf] [kimi-k3-blog].
- Third-party hosting: Amazon Bedrock lists K3 (global and US cross-Region profiles, 1M context, explicit prompt caching with at least 30-minute retention, priority and flex service levels at 1.75 and 0.5 times the standard price) and recommends its OpenAI-compatible APIs over Converse [aws-bedrock-kimi-k3].

## Prompting guides

Moonshot's guides, and what each says:

| Guide | Content |
| --- | --- |
| Best practices for prompts | A general, model-independent guide: give details, assign a role, separate parts with delimiters such as XML tags or triple quotes, write the steps, show examples, ask for lengths in paragraphs or bullets rather than word counts, supply reference text, split complex tasks and summarise long chats. |
| Kimi K3 tool-calling best practices | For large tool inventories: declare a search tool plus a few core tools, force the first turn with `tool_choice: required`, inject definitions as they are found, set the effort level before the conversation starts. |
| Reasoning effort, thinking models | Effort values and defaults; preserved thinking; keep `reasoning_content`; set `max_tokens` high; stream. |
| Tool choice, dynamic tool loading | How `tool_choice` works, and how appending tool definitions keeps the prefix cache. |
| How to fix repeated tool calls | Check the message layout first; detect identical consecutive calls on the client and add a reminder to the system prompt after 3 repeats and a stronger one after 5 and 8. |
| Structured output, partial mode, vision, context caching | Request formats, limits and cost behaviour. |
| Benchmarking best practices | Temperature 1.0, top-p 0.95 and streaming for any unlisted benchmark; at least 500 to 1,000 samples for reasoning benchmarks; 128K output tokens for reasoning and 256K for coding; 16K to 64K or more for agent tasks. Written for K2.6, and the page's table lists K2.6 settings. |
| Launch blog's limitations note (K3) | Two cautions in Moonshot's words: quality can become unstable when a harness does not pass thinking back or a session is switched to K3 mid-way, and K3 can make unexpected decisions on the user's behalf when it meets small problems or ambiguity, so it suggests explicit behavioural limits in the system prompt or AGENTS.md. |

Moonshot names its own Kimi Code command-line tool as the framework each model works best with, and its report trained K3 with environments that can instantiate Kimi Code, Claude Code, Codex, OpenClaw and Hermes [kimi-k3-hf] [kimi-k3-report].

How the advice has moved from K2.6 to K3: K2.6 leaves `reasoning_content` optional across turns (it keeps it when `thinking.keep` is `all`); K2.7 Code made keeping it mandatory; K3 requires the whole assistant message, reasoning and tool calls included, and replaced the `thinking` object with a top-level `reasoning_effort` field that has three levels and a maximum default. Moonshot added a required-tool choice and dynamic tool loading with K3 only.

## System-card practice

For a release Moonshot publishes a blog post, a Hugging Face model card with a benchmark table and footnotes, and for K3 a technical report (on arXiv and GitHub). Documents differ by model:

- **K3.** The blog, the card and the [report](https://arxiv.org/html/2607.24653) give per-benchmark settings and harnesses and say which rows are internal or cited from others. The report has an internal cyber-security evaluation (vulnerability discovery, and an exploit suite of 36 tasks) and cites an independent UK AISI and CAISI assessment. It has no alignment, refusal, over-refusal, sycophancy or prompt-injection evaluation and no deployment-safeguard section ([kimi-k3-report], [uk-aisi-caisi-k3]).
- **K2.7 Code.** The Hugging Face card only: a six-row table against GPT-5.5 and Claude Opus 4.8 and the run settings. No report, no safety content [kimi-k27-code-hf].
- **K2.6.** The Hugging Face card and the tech blog only: a benchmark table against GPT-5.4, Claude Opus 4.6 and Gemini 3.1 Pro, the run settings, and deployment notes. No system card, no safety content [kimi-k26-hf].

Moonshot's own tables disclose some run caveats that are useful to read: for K3's in-house coding benchmark it lists the refusals and fallbacks that competing models hit (for example 10 of 80 tasks entering one competitor's cyber guard), and it excludes those models from its cyber suite because they refuse the tasks [kimi-k3-hf] [kimi-k3-report]. Rows marked in-house (Kimi Code Bench, Kimi Claw 24/7 Bench, Kimi Webdev Bench) have no outside check, and some competitor numbers are cited from other leaderboards rather than rerun.

## Family-wide behaviour

**Thinking and preserved reasoning.** K3 and K2.7 Code always think; K2.6 thinks by default and can be switched off. Reasoning comes back as `reasoning_content`, ahead of `content` in a stream, and counts against `max_tokens`. K3 and K2.7 Code are trained with earlier reasoning kept in the conversation: the whole assistant message from every turn must be sent back unchanged. Moonshot warns that a harness that drops it, or a session moved to K3 from another model, can make generation quality highly unstable [kimi-thinking-models] [kimi-k3-blog].

**Fixed parameters.** `temperature` is fixed at 1.0 (K2.6 uses 0.6 without thinking), `top_p` at 0.95, `n` at 1 and both penalties at 0; sending any other value returns an error, so Moonshot says to leave them out. For self-hosted K3 the report recommends top-p 0.95 for reasoning and knowledge work and 1.0 for coding and agents, which the hosted API cannot do [kimi-model-params] [kimi-k3-report].

**Effort.** Only K3 has `reasoning_effort` (low, high, max; default max). Changing it in the middle of a conversation invalidates the prefix cache [kimi-model-params].

**Tool choice.** `required` works on K3 and returns an error on K2.7 Code and K2.6. Forcing one named function is incompatible with thinking and returns 400, so it is unavailable for K3 and K2.7 Code [kimi-tool-choice].

**Multi-step tool use.** For K2.7 Code and K2.6, Moonshot says to keep all reasoning from the current task in the context, set `max_tokens` to at least 16,000, stream, and leave `temperature` alone; for K3 its rule is to return each complete assistant message unchanged [kimi-thinking-models] [kimi-k3-quickstart].

**Vision.** `content` must be an array of parts, never a serialised string. No Kimi vision model takes public image URLs: use base64 or an uploaded file id. Videos go through uploaded ids. Moonshot advises images up to 4K (4096 by 2160) and video up to full HD, since larger input costs time without improving understanding. SVG is rejected; animated GIF or WebP may be decoded and billed as video. The request body may not exceed 100 MB [kimi-vision].

**Structured output.** `response_format` takes `json_object` or `json_schema`; set `strict` to true and keep schemas inside Moonshot's JSON Schema subset. K3 supports nested objects, arrays and `anyOf`. Parse only `content`, never `reasoning_content`. In partial mode with thinking, the previous `reasoning_content` goes back with the prefix, and a small `max_tokens` can end a reply inside the reasoning [kimi-response-format] [kimi-partial-mode].

**Third-party deployments.** Moonshot found that scores from other providers' hosted copies of its models, from K2 Thinking on, differed from its own API, and published a Vendor Verifier alongside K2.6 (April 2026) that checks parameter enforcement, image and long-output behaviour and tool-call accuracy, and it enforces the fixed sampling values and the reasoning-passback check on its own API for the same reason. On Bedrock, K3's Converse API fails when earlier reasoning blocks are sent; Bedrock advises its OpenAI-compatible APIs [kimi-vendor-verifier] [aws-bedrock-kimi-k3].

**Safeguards as measured by others.** The UK AI Security Institute and CAISI, in a joint preliminary assessment of K3 (2026-07-23), found that its safeguards did not stop it attempting exploit development or offensive cyber operations, and that its cyber capability sat well below the leading US models ([uk-aisi-caisi-k3], with the figures in the [K3 file](kimi-k3.md#what-the-system-card-reports)).

## Open questions

- Whether Moonshot will publish an alignment, refusal or prompt-injection evaluation for K3; the report has only a cyber section.
- K2.6's exact release day and how long the API keeps serving it; Moonshot's pages say only April 2026 and now point to K3.
- K2.7 Code's exact release day; the changelog gives only June 2026.
- Independent results for K3 on the METR time horizon and Artificial Analysis's coding-agent index, neither of which listed it.
- Whether a K3 coding variant or a K3 minor release will follow.

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| kimi-models | https://platform.kimi.ai/docs/models | L | 2026-10-03 |
| kimi-changelog | https://platform.kimi.ai/docs/platform-changelog | L | 2026-10-03 |
| kimi-api-overview | https://platform.kimi.ai/docs/api/overview | L | 2026-10-03 |
| kimi-model-params | https://platform.kimi.ai/docs/api/models-overview | L | 2026-10-03 |
| kimi-pricing | https://platform.kimi.ai/docs/pricing/chat | L | 2026-10-03 |
| kimi-limits | https://platform.kimi.ai/docs/pricing/limits | L | 2026-10-03 |
| kimi-k3-quickstart | https://platform.kimi.ai/docs/guide/kimi-k3-quickstart | L | 2026-10-03 |
| kimi-thinking-models | https://platform.kimi.ai/docs/guide/use-thinking-models | L | 2026-10-03 |
| kimi-tool-choice | https://platform.kimi.ai/docs/guide/use-tool-choice | L | 2026-10-03 |
| kimi-response-format | https://platform.kimi.ai/docs/guide/response_format | L | 2026-10-03 |
| kimi-partial-mode | https://platform.kimi.ai/docs/guide/use-partial-mode-feature-of-kimi-api | L | 2026-10-03 |
| kimi-vision | https://platform.kimi.ai/docs/guide/use-kimi-vision-model | L | 2026-10-03 |
| kimi-context-caching | https://platform.kimi.ai/docs/guide/context-caching | L | 2026-10-03 |
| kimi-troubleshooting | https://platform.kimi.ai/docs/guide/troubleshooting | L | 2026-10-03 |
| kimi-claude-code | https://platform.kimi.ai/docs/guide/claude-code-kimi | L | 2026-10-03 |
| kimi-zdr | https://platform.kimi.ai/docs/guide/zero-data-retention | L | 2026-10-03 |
| kimi-k3-blog | https://www.kimi.ai/blog/kimi-k3 | L | 2026-10-03 |
| kimi-vendor-verifier | https://www.kimi.ai/blog/kimi-vendor-verifier | L | 2026-10-03 |
| kimi-blog-index | https://www.kimi.ai/blog | L | 2026-10-03 |
| kimi-k3-hf | https://huggingface.co/moonshotai/Kimi-K3 | L | 2026-10-03 |
| kimi-k3-license | https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE | L | 2026-10-03 |
| kimi-k27-code-hf | https://huggingface.co/moonshotai/Kimi-K2.7-Code | L | 2026-10-03 |
| kimi-k26-hf | https://huggingface.co/moonshotai/Kimi-K2.6 | L | 2026-10-03 |
| kimi-k3-report | https://arxiv.org/html/2607.24653 | L | 2026-10-03 |
| uk-aisi-caisi-k3 | https://www.aisi.gov.uk/blog/preliminary-assessment-of-kimi-k3s-cyber-capabilities | M | 2026-10-03 |
| aws-bedrock-kimi-k3 | https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-moonshot-ai-kimi-k3.html | L | 2026-10-03 |
