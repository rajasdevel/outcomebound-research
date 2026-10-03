---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: local runtime
sources:
  - https://lmstudio.ai/
  - https://lmstudio.ai/docs/developer
  - https://lmstudio.ai/docs/developer/openai-compat
  - https://lmstudio.ai/docs/app/system-requirements
  - https://lmstudio.ai/changelog
  - https://lmstudio.ai/models
  - https://lmstudio.ai/pricing
  - https://lmstudio.ai/privacy
  - https://lmstudio.ai/terms
  - https://github.com/lmstudio-ai/docs/blob/main/1_developer/3_openai-compat/index.mdx
  - https://github.com/lmstudio-ai/docs/blob/main/1_developer/3_openai-compat/chat-completions.md
  - https://github.com/lmstudio-ai/docs/blob/main/1_developer/3_openai-compat/responses.md
  - https://github.com/lmstudio-ai/docs/blob/main/1_developer/3_openai-compat/structured-output.md
  - https://github.com/lmstudio-ai/docs/blob/main/1_developer/3_openai-compat/tools.mdx
  - https://github.com/lmstudio-ai/docs/blob/main/1_developer/4_anthropic-compat/index.mdx
  - https://github.com/lmstudio-ai/docs/blob/main/1_developer/2_rest/index.mdx
  - https://github.com/lmstudio-ai/docs/blob/main/1_developer/2_rest/chat.md
  - https://github.com/lmstudio-ai/docs/blob/main/1_developer/2_rest/load.md
  - https://github.com/lmstudio-ai/docs/blob/main/1_developer/api-changelog.md
  - https://github.com/lmstudio-ai/docs/blob/main/1_developer/0_core/authentication.mdx
  - https://github.com/lmstudio-ai/docs/blob/main/1_developer/0_core/headless.md
  - https://github.com/lmstudio-ai/docs/blob/main/1_developer/0_core/ttl-and-auto-evict.md
  - https://github.com/lmstudio-ai/docs/blob/main/1_developer/0_core/0_server/serve-on-network.mdx
  - https://github.com/lmstudio-ai/docs/blob/main/0_app/5_advanced/parallel-requests.md
  - https://github.com/lmstudio-ai/docs/blob/main/0_app/5_advanced/speculative-decoding.md
  - https://github.com/lmstudio-ai/docs/blob/main/0_app/5_advanced/import-model.md
  - https://github.com/lmstudio-ai/docs/blob/main/0_app/1_basics/lmstudio-vs-llmster-vs-lms.md
  - https://github.com/lmstudio-ai/docs/blob/main/0_app/0_root/offline.mdx
  - https://github.com/lmstudio-ai/docs/blob/main/4_integrations/claude-code.mdx
  - https://github.com/lmstudio-ai/docs/blob/main/5_lmlink/index.md
  - https://github.com/lmstudio-ai/docs/blob/main/0_app/3_modelyaml/index.md
  - https://github.com/lmstudio-ai/docs/blob/main/_configuration/lm-runtimes.md
  - https://github.com/lmstudio-ai/lms
  - https://github.com/lmstudio-ai/lmstudio-js
---

# LM Studio

local runtime

LM Studio is a desktop application, from Element Labs, for downloading open-weight models and running them on the user's own computer, with a built-in chat window and a local API server. On 2026-10-03 the site and changelog present the application as "LM Studio Bionic" (version 1.1.x): the same product plus an agent (documents, coding, computer control) and optional paid cloud inference. The runtime underneath is llama.cpp for GGUF files and MLX for Apple silicon, packaged as separately downloaded "runtimes" that the offline page says can be swapped without a full app update; release 1.1.5 (2026-09-19) adds a further Mac-only engine, Splash, for Qwen3.8. A headless daemon, `llmster`, and the `lms` command-line tool run the same server without the interface. The application is closed-source software under Element Labs' terms of use; the `lms` CLI and the JavaScript SDK are MIT-licensed repositories. On 2026-10-03 the latest release is Bionic 1.1.7 (2026-10-01). [lm-home, lm-change, lm-offline, lm-terms, lm-vs, lm-cli-repo, lm-js-repo]

## Models offered

LM Studio serves whatever the user downloads: GGUF and MLX files from Hugging Face through its catalogue (`lmstudio.ai/models`), files imported from disk (`lms import` for GGUF, or placing them in `~/.lmstudio/models/<publisher>/<model>/`), and, on paid plans, models hosted in "LM Studio Cloud". The catalogue marks each entry "Available to download", "Available in LM Studio Cloud" or both. A model is addressed by its `publisher/model` identifier, for example `openai/gpt-oss-20b`. [lm-models, lm-import, lm-price]

Models in this library that the catalogue lists on 2026-10-03:

| Model file | How the catalogue lists it |
| --- | --- |
| [Qwen3.8 27B](../models/alibaba/qwen3.8-27b.md) | download (1.3 million downloads); vision-language; 262K context; configurable reasoning |
| [Muse Glimmer 30B](../models/meta/muse-glimmer-30b.md) | download (30B; about 273,000 downloads) |
| [DeepSeek V4.1-Flash](../models/deepseek/deepseek-flash.md) | LM Studio Cloud only |
| [DeepSeek V4-Pro](../models/deepseek/deepseek-v4-pro.md) | LM Studio Cloud only |
| [GLM-5.3](../models/zai/glm-5.3.md), [GLM-5.3-Flash](../models/zai/glm-5.3-flash.md), [GLM-5.2](../models/zai/glm-5.2.md) | LM Studio Cloud only |
| [Kimi K3](../models/moonshot/kimi-k3.md) | LM Studio Cloud only |
| [gpt-oss 20B](../models/openai/gpt-oss-20b.md) and [120B](../models/openai/gpt-oss-120b.md) | download (`gpt-oss`, 20B and 120B); the 20B is the model LM Studio's own docs use for examples, and `reasoning.effort` on `/v1/responses` was first announced for it |
| [Gemma 4](../models/google/gemma-4-26b-a4b-it.md) (and the [E2B](../models/google/gemma-4-e2b-it.md), [E4B](../models/google/gemma-4-e4b-it.md), [12B](../models/google/gemma-4-12b-it.md) and [31B](../models/google/gemma-4-31b-it.md) sizes) | download (`Gemma 4`, sizes listed as 5.1B, 7.9B, 12B, 26B and 31B; about 8.7 million downloads); vision input; Bionic 1.1.6 (2026-09-23) fixed default load settings for Gemma 4 vision models |

[lm-models, lm-change, lm-resp, lm-apichange]

The catalogue also lists other open models that have no file here (for example DeepSeek V4 Flash 0731, offered both as a download and in LM Studio Cloud, Laguna S 2.1, and Bonsai 27B, 1-bit and ternary builds of Qwen3.6 27B). No Anthropic, closed OpenAI, Gemini or Grok model is available; compatible endpoints let clients written for those APIs talk to local models. [lm-models]

## API surface

- **Four inference shapes on one local server** (default port 1234). LM Studio's own v1 REST API at `/api/v1/*` (chat, model list, load, unload, download and download status), which LM Studio recommends over the older v0 routes. OpenAI-compatible: `/v1/models`, `/v1/responses`, `/v1/chat/completions`, `/v1/embeddings` and `/v1/completions`. Anthropic-compatible: `POST /v1/messages` (added in 0.4.1). The docs' comparison table says `/api/v1/chat` and `/v1/responses` are stateful and can use MCP servers, and that custom tools work on `/v1/responses`, `/v1/chat/completions` and `/v1/messages` but not on `/api/v1/chat`. [lm-rest, lm-oai-index, lm-ant, lm-apichange]
- **Auth.** Off by default. Version 0.4.0 added API tokens; with "Require Authentication" on, every REST, Python-SDK and TypeScript-SDK request needs a token, sent as `Authorization: Bearer` (and `x-api-key` is also accepted on the Anthropic endpoint). Tokens have per-token permissions. The server listens on localhost until "Serve on Local Network" or `lms server start --bind 0.0.0.0` widens it, and the docs recommend enabling authentication before doing so. [lm-auth, lm-net, lm-ant]
- **SDKs.** `@lmstudio/sdk` (TypeScript) and `lmstudio` (Python) for chat, structured responses, tool calling and model management; the `lms` CLI (`lms get`, `load`, `ls`, `server start`, `chat`, `log stream`); the OpenAI and Anthropic SDKs by changing the base URL. [lm-dev, lm-vs]
- **Model ids.** The identifier shown in LM Studio, not an OpenAI or Anthropic name. [lm-oai-index]
- **Headless.** `llmster` (installed by `curl -fsSL https://lmstudio.ai/install.sh | bash` or a PowerShell script, started with `lms daemon up`) runs the server on Linux servers, cloud instances, GPU machines without a display and CI/CD pipelines without the interface, and the docs link a separate Linux startup-task page (not read). The app can also run as a login service. [lm-headless, lm-vs]
- **LM Link.** An end-to-end encrypted network between a user's own devices, built with Tailscale, so that a model loaded on one machine can be used from another (a laptop, or an iPhone through a third-party app) through the CLI, the REST API and coding tools; up to 5 devices on the free plan. [lm-link, lm-price]
- **JIT loading and TTL.** With just-in-time loading (on by default) the first request to a model loads it and `/v1/models` lists every downloaded model; idle models unload after 60 minutes by default for JIT loads, with `ttl` settable per request, and Auto-Evict keeps one JIT model loaded at a time. Models loaded with `lms load` have no TTL unless `--ttl` is given. [lm-headless, lm-ttl]

## Feature parity

Parity is against the makers' APIs and the OpenAI and Anthropic APIs LM Studio imitates. LM Studio's pages list supported fields and do not publish a list of unsupported ones, so an absent field is unverified, not confirmed unsupported. [lm-chat, lm-resp]

| Feature | What the docs say |
| --- | --- |
| Reasoning control | `/v1/responses` accepts `reasoning.effort` (the docs' example is `low` on gpt-oss-20b); the native `/api/v1/chat` takes `reasoning` as `off`, `low`, `medium`, `high` or `on` and errors if the model cannot do it. Chat Completions has no documented effort parameter. For DeepSeek R1 models a setting in App Settings > Developer returns reasoning in a separate `reasoning_content` field (0.3.9). For gpt-oss, reasoning text comes back in `message.reasoning` (and `delta.reasoning` when streaming), moved out of `content` in 0.3.23. |
| Tools | `/v1/chat/completions`, `/v1/responses` and `/v1/messages` accept tool definitions. "Native" tool use needs a chat template with tool support and a parser LM Studio knows (shown as a hammer badge in the app); other models get a "default" format injected through the system prompt. Streamed tool-call arguments for compatible local and LM Link models arrived in Bionic 1.1.4, and images in tool results in 1.1.0. On the OpenAI-style API, 0.3.15 added `tool_choice` `none`, `auto` and `required` (`required` on the llama.cpp engine only); `tool_choice` `any` is shown on the Anthropic endpoint. MCP servers can be used by the app and by `/api/v1/chat` and `/v1/responses` when enabled. |
| Structured output | `response_format` with `json_schema` on `/v1/chat/completions`, in OpenAI's format; the result is a JSON string in `choices[0].message.content`. `response_format.type` `text` is accepted since 0.3.18. |
| Vision | image input on Chat Completions and in the SDKs for vision models; the exact image-input forms are in the SDK pages, not read here. |
| Prompt caching | no per-request cache controls described; Bionic 1.1.0 added MLX prompt disk-cache controls in the advanced model settings. |
| Batch | none; parallel requests by continuous batching (Max Concurrent Predictions, default 4) on the llama.cpp engine, with MLX listed as coming. |
| Long context | set when a model loads (`context_length` on `/api/v1/models/load` and `/api/v1/chat`; the OpenAI-style endpoints cannot set it per request). |
| Streaming | SSE on all four shapes; `/api/v1/chat` also streams model-load and prompt-processing events. |
| Speculative decoding | a draft model with the same vocabulary, chosen in the app or with `draft_model` in an API request (0.3.10); Bionic 1.1.3 extended multi-token-prediction (MTP) speculative decoding to more models. |

The Chat Completions page lists supported payload parameters as `model`, `top_p`, `top_k`, `messages`, `temperature`, `max_tokens`, `stream`, `stop`, `presence_penalty`, `frequency_penalty`, `logit_bias`, `repeat_penalty` and `seed`. [lm-chat, lm-resp, lm-struct, lm-tools, lm-rest, lm-restchat, lm-parallel, lm-spec, lm-apichange, lm-change]

## Pricing

The app is free to download and run with local models, including the agent, MLX and llama.cpp runtimes, offline voice transcription and LM Link for up to 5 devices, with limited web search. Paid plans add hosted inference: Bionic+ at $20 a month (US-hosted open-source models such as Kimi K3, GLM 5.3 and DeepSeek V4 Flash, discounted bulk tokens, web search and page extraction) and Pro at $100 a month (5 times the usage limits, early access). Cloud credits cover use beyond a plan's allowance. Organisations can create an account with centralised billing; team subscription plans are described as coming. The pricing page does not address commercial use; the app terms of use govern use of the software and carry the version date 2026-08-23. No per-token cloud price table is published on the pages read. [lm-price, lm-terms]

## Limits and data

- **Rate limits.** Locally there are none beyond hardware and the Max Concurrent Predictions setting. Cloud usage limits are plan allowances (Pro gives five times the Bionic+ usage limits), with no per-minute figures on the pages read. [lm-price, lm-parallel]
- **Regions.** Cloud inference is described as US-hosted. [lm-price]
- **Retention and training.** The privacy policy (effective June 2026) says messages, chat histories and documents are not transmitted from the user's system when local models are used, and that the application has no telemetry or user-specific tracking. Update checks send app version and build, operating system and an IP address (added by the CDN provider), and model searches and downloads send anonymised search queries. For paid cloud services (cloud models and web search), the policy says requests are processed transiently, not kept after the request completes and not used for training, and that every party processing them works under zero-data-retention "or substantially equivalent terms"; the home and pricing pages call the cloud services zero-data-retention, and the pricing page adds that web content itself carries privacy risk. [lm-priv, lm-price, lm-home]
- **Offline.** Chat, document chat (RAG) and the local server work without internet once the files and runtimes are present; model search, downloads, the catalogue's live statistics, runtime downloads and update checks need a connection. [lm-offline]
- **System requirements.** macOS 14 or newer on Apple silicon (Intel Macs unsupported), 16 GB or more RAM recommended; Windows x64 with AVX2 or ARM (Snapdragon X), 16 GB RAM and 4 GB or more VRAM recommended; Linux x64 or ARM64 on Ubuntu 20.04 or newer, as an AppImage. [lm-sysreq]
- **Formats.** GGUF and MLX. LM Studio's `model.yaml` draft specification describes a model and all its variants in one file, hiding the underlying format. Models in the catalogue are implemented as `model.yaml` entries, which can also carry load and inference options. Quantisation is whatever the downloaded file carries; the pages read describe no quantisation tool. [lm-import, lm-modelyaml]

## Notes for agents and harnesses

- **Load-time settings decide behaviour.** Context length, flash attention, GPU offload and parallel slots are set when the model is loaded, from the app, `lms load` or `/api/v1/models/load`. The OpenAI-compatible and Anthropic-compatible endpoints do not take them per request, so a client on those endpoints inherits whatever the model was loaded with; the docs do not state the default window. `lms load --estimate-only <model>` prints the estimated GPU and total memory first (0.3.27). [lm-load, lm-oai-index, lm-apichange]
- **Context for agent work.** For Claude Code, LM Studio's guide says to use a model and settings with more than about 25,000 tokens of context because such tools use a lot of it. The guide's setup also sets `CLAUDE_CODE_ATTRIBUTION_HEADER=0` without giving a reason; SGLang's guide sets the same variable and explains it as keeping the start of the system prompt stable between requests (see [SGLang](sglang.md)). Base URL `http://localhost:1234` and a placeholder token are all the Anthropic endpoint needs unless authentication is on. [lm-cc]
- **Reasoning text is not in `content` for gpt-oss.** A client that reads only `message.content` from Chat Completions sees the answer without the reasoning and has to read `reasoning` for it. [lm-apichange]
- **Tool-call quality tracks template support.** "Native" and "default" tool use are different mechanisms: default format rewrites tool-role messages as user messages and injects a custom system prompt, and the docs say results vary by model. The tools page says `lms log stream` shows the default format a model receives, so it shows which mechanism a model got; native support is shown by a hammer badge in the app. [lm-tools, lm-chat]
- **Structured output returns a string.** LM Studio's page says the JSON schema goes in `response_format.json_schema`, that all other Chat Completions parameters are honoured, and that the result arrives as a JSON string to parse; its example sets `strict` to the string `"true"`. [lm-struct]
- **Sampling defaults.** `temperature` 0.7 appears in the docs' examples; the docs do not state a server default, and a model's packaged preset may apply. [lm-chat]
- **Idle behaviour.** JIT-loaded models unload after the TTL, so a long pause costs a reload; a model loaded from the CLI stays until unloaded. Auto-evict keeps one JIT model resident, which means two clients addressing two models can thrash. [lm-ttl]
- **The product is moving.** The application changed name and scope in 2026 (Bionic), ships almost weekly with llama.cpp runtime packs (2.41.0, 2.43.0 and 2.48.0 are named in recent notes), and the docs repository still carries stub pages (the LM Runtimes page is placeholder text). A test that depends on behaviour is only reproducible against a pinned app and runtime version. [lm-change, lm-docs-runtimes]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| lm-home | https://lmstudio.ai/ | L | 2026-10-03 |
| lm-dev | https://lmstudio.ai/docs/developer | L | 2026-10-03 |
| lm-sysreq | https://lmstudio.ai/docs/app/system-requirements | L | 2026-10-03 |
| lm-change | https://lmstudio.ai/changelog | L | 2026-10-03 |
| lm-models | https://lmstudio.ai/models | L | 2026-10-03 |
| lm-price | https://lmstudio.ai/pricing | L | 2026-10-03 |
| lm-priv | https://lmstudio.ai/privacy | L | 2026-10-03 |
| lm-terms | https://lmstudio.ai/terms | L | 2026-10-03 |
| lm-oai-index | https://github.com/lmstudio-ai/docs/blob/main/1_developer/3_openai-compat/index.mdx | L | 2026-10-03 |
| lm-chat | https://github.com/lmstudio-ai/docs/blob/main/1_developer/3_openai-compat/chat-completions.md | L | 2026-10-03 |
| lm-resp | https://github.com/lmstudio-ai/docs/blob/main/1_developer/3_openai-compat/responses.md | L | 2026-10-03 |
| lm-struct | https://github.com/lmstudio-ai/docs/blob/main/1_developer/3_openai-compat/structured-output.md | L | 2026-10-03 |
| lm-tools | https://github.com/lmstudio-ai/docs/blob/main/1_developer/3_openai-compat/tools.mdx | L | 2026-10-03 |
| lm-ant | https://github.com/lmstudio-ai/docs/blob/main/1_developer/4_anthropic-compat/index.mdx | L | 2026-10-03 |
| lm-rest | https://github.com/lmstudio-ai/docs/blob/main/1_developer/2_rest/index.mdx | L | 2026-10-03 |
| lm-restchat | https://github.com/lmstudio-ai/docs/blob/main/1_developer/2_rest/chat.md | L | 2026-10-03 |
| lm-load | https://github.com/lmstudio-ai/docs/blob/main/1_developer/2_rest/load.md | L | 2026-10-03 |
| lm-apichange | https://github.com/lmstudio-ai/docs/blob/main/1_developer/api-changelog.md | L | 2026-10-03 |
| lm-auth | https://github.com/lmstudio-ai/docs/blob/main/1_developer/0_core/authentication.mdx | L | 2026-10-03 |
| lm-headless | https://github.com/lmstudio-ai/docs/blob/main/1_developer/0_core/headless.md | L | 2026-10-03 |
| lm-ttl | https://github.com/lmstudio-ai/docs/blob/main/1_developer/0_core/ttl-and-auto-evict.md | L | 2026-10-03 |
| lm-net | https://github.com/lmstudio-ai/docs/blob/main/1_developer/0_core/0_server/serve-on-network.mdx | L | 2026-10-03 |
| lm-parallel | https://github.com/lmstudio-ai/docs/blob/main/0_app/5_advanced/parallel-requests.md | L | 2026-10-03 |
| lm-spec | https://github.com/lmstudio-ai/docs/blob/main/0_app/5_advanced/speculative-decoding.md | L | 2026-10-03 |
| lm-import | https://github.com/lmstudio-ai/docs/blob/main/0_app/5_advanced/import-model.md | L | 2026-10-03 |
| lm-vs | https://github.com/lmstudio-ai/docs/blob/main/0_app/1_basics/lmstudio-vs-llmster-vs-lms.md | L | 2026-10-03 |
| lm-offline | https://github.com/lmstudio-ai/docs/blob/main/0_app/0_root/offline.mdx | L | 2026-10-03 |
| lm-cc | https://github.com/lmstudio-ai/docs/blob/main/4_integrations/claude-code.mdx | L | 2026-10-03 |
| lm-link | https://github.com/lmstudio-ai/docs/blob/main/5_lmlink/index.md | L | 2026-10-03 |
| lm-modelyaml | https://github.com/lmstudio-ai/docs/blob/main/0_app/3_modelyaml/index.md | L | 2026-10-03 |
| lm-docs-runtimes | https://github.com/lmstudio-ai/docs/blob/main/_configuration/lm-runtimes.md | L | 2026-10-03 |
| lm-cli-repo | https://github.com/lmstudio-ai/lms | L | 2026-10-03 |
| lm-js-repo | https://github.com/lmstudio-ai/lmstudio-js | L | 2026-10-03 |
