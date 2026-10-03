---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: local runtime
sources:
  - https://docs.ollama.com/
  - https://docs.ollama.com/llms.txt
  - https://docs.ollama.com/api/introduction
  - https://docs.ollama.com/api/openai-compatibility
  - https://docs.ollama.com/api/anthropic-compatibility
  - https://docs.ollama.com/api/usage
  - https://docs.ollama.com/api/errors
  - https://docs.ollama.com/cloud
  - https://docs.ollama.com/context-length
  - https://docs.ollama.com/faq
  - https://docs.ollama.com/gpu
  - https://docs.ollama.com/import
  - https://docs.ollama.com/modelfile
  - https://docs.ollama.com/macos
  - https://docs.ollama.com/windows
  - https://docs.ollama.com/capabilities/structured-outputs
  - https://docs.ollama.com/capabilities/tool-calling
  - https://docs.ollama.com/capabilities/thinking
  - https://docs.ollama.com/capabilities/vision
  - https://docs.ollama.com/capabilities/streaming
  - https://docs.ollama.com/capabilities/web-search
  - https://docs.ollama.com/integrations/claude-code
  - https://ollama.com/pricing
  - https://ollama.com/library
  - https://ollama.com/library/gemma4
  - https://ollama.com/library/qwen3.8/tags
  - https://ollama.com/search?c=cloud
  - https://github.com/ollama/ollama
  - https://github.com/ollama/ollama/releases
---

# Ollama

local runtime

Ollama is a program that downloads open-weight models and serves them from the user's own machine, through a command-line tool, desktop apps for macOS and Windows, a Linux install script and a Docker image. The code is MIT-licensed. It exposes its own HTTP API on port 11434 and, on the same server, OpenAI-compatible and Anthropic-compatible endpoints. The same company also runs a hosted service, Ollama Cloud, that serves part of the catalogue through the same three API shapes at `ollama.com`, so one client can move between local and hosted models by changing a base URL and a key. On 2026-10-03 the latest stable release is v0.35.1 (2026-09-29), and a v0.40.0 release candidate (2026-09-25) runs supported models on Apple's MLX engine by default on Apple silicon. This file covers both modes and says which one a statement applies to. [ol-docs, ol-rel, ol-repo]

## Models offered

Ollama serves a catalogue it calls the library, of open-weight models that it packages itself; a model is pulled by name and tag, for example `gemma4:31b`. A tag carries the size, the quantisation or format (`q4_K_M`, `q8_0`, `bf16`, or an `-mlx` suffix for MLX builds), the context window and the input types. On 2026-10-03 the library's popularity list is led by older families (Llama 3.1 and 3.2, DeepSeek-R1, Qwen 2.5 and 3, Gemma 2 and 3); Gemma 4, Qwen 3.5, 3.6 and 3.8 and gpt-oss are among the newer entries. Cloud models are the entries tagged `cloud` in the library and returned by `/api/tags` on `ollama.com`. [ol-lib, ol-cloud, ol-qwen38, ol-gemma4]

Models in this library that Ollama lists, as of 2026-10-03:

| Model file | How Ollama lists it |
| --- | --- |
| [Gemma 4 E2B](../models/google/gemma-4-e2b-it.md), [E4B](../models/google/gemma-4-e4b-it.md), [12B](../models/google/gemma-4-12b-it.md), [26B-A4B](../models/google/gemma-4-26b-a4b-it.md), [31B](../models/google/gemma-4-31b-it.md) | `gemma4`, tags e2b, e4b, 12b, 26b, 31b, with `-mlx` builds; local and cloud; capability tags vision, tools, thinking and audio; 128K context on e2b and e4b, 256K on the larger sizes |
| [gpt-oss 20B](../models/openai/gpt-oss-20b.md) and [120B](../models/openai/gpt-oss-120b.md) | `gpt-oss`; local and cloud; tools and thinking |
| [Qwen3.8 27B](../models/alibaba/qwen3.8-27b.md) | `qwen3.8`, 27b; GGUF-quantised, MTP and MLX variants, about 18 GB at the default tag; vision, tools, thinking; 256K context |
| [Qwen3.8-Flash-Next](../models/alibaba/qwen3.8-flash-next.md) | `qwen3.8-flash-next`, local; vision, tools, thinking; described by Ollama as an experimental preview |
| [Muse Glimmer 30B](../models/meta/muse-glimmer-30b.md) | `muse-glimmer`, 30b, local; vision, tools, thinking |
| [GLM-5.3](../models/zai/glm-5.3.md), [GLM-5.3-Flash](../models/zai/glm-5.3-flash.md), [GLM-5.2](../models/zai/glm-5.2.md) | cloud |
| [Kimi K3](../models/moonshot/kimi-k3.md), [Kimi K2.7 Code](../models/moonshot/kimi-k2.7-code.md) | cloud |
| [DeepSeek V4.1-Flash](../models/deepseek/deepseek-flash.md), [DeepSeek V4-Pro](../models/deepseek/deepseek-v4-pro.md) | cloud (`deepseek-v4.1-flash`, `deepseek-v4-pro`) |
| [MiniMax M3](../models/minimax/MiniMax-M3.md) | cloud |
| [Nemotron 3 Ultra](../models/other/nemotron-3-ultra.md) | cloud |
| [Mistral Large 3](../models/mistral/mistral-large-3.md) | cloud; vision and tools |

[ol-cloud-list, ol-gemma4, ol-qwen38, ol-lib]

No Anthropic, closed OpenAI, Gemini or Grok model runs on Ollama; the compatibility endpoints let a client written for those APIs talk to open models. The library also holds embedding, OCR and vision models. Since v0.35.0 it holds "decision" models that return choices, probabilities or scores through `/v1/systemone` instead of text (v0.35.1 added two multimodal ones); the API introduction says this route needs a local server and is not yet on Ollama Cloud. [ol-docs-index, ol-rel, ol-api]

## API surface

- **Three shapes on one server.** Native: `/api/chat`, `/api/generate`, `/api/embed`, `/api/show`, `/api/tags`, `/api/ps`, `/api/pull` and the model-management calls. OpenAI-compatible: `/v1/chat/completions`, `/v1/completions`, `/v1/models`, `/v1/embeddings` and a stateless `/v1/responses`. Anthropic-compatible: `/v1/messages`. Local base URLs are `http://localhost:11434/api`, `http://localhost:11434/v1` and `http://localhost:11434`. Cloud base URLs are `https://ollama.com/api`, `https://ollama.com/v1` and `https://ollama.com`. [ol-api, ol-oai, ol-ant]
- **Auth.** The local server needs none and ignores any key the client sends; the OpenAI and Anthropic SDKs still want a placeholder. The cloud takes `Authorization: Bearer <OLLAMA_API_KEY>`, with keys created in account settings. The local server binds to 127.0.0.1 by default; `OLLAMA_HOST` exposes it, and the FAQ describes proxying it through Nginx, ngrok or Cloudflare Tunnel. No authentication on the local server is described. [ol-api, ol-faq, ol-cloud]
- **SDKs.** Official Python and JavaScript libraries; community SDKs exist for other languages. Streaming is on by default in the REST API and off by default in the SDKs. The native stream is newline-delimited JSON, and usage fields (`prompt_eval_count`, `prompt_eval_cached_count`, `eval_count`, durations in nanoseconds) arrive in the final chunk. [ol-api, ol-stream, ol-usage]
- **Model ids.** `name:tag` as in the library (`gemma4:31b`). In the app and CLI a cloud model is `name:cloud`; in a request to `ollama.com` it is the plain name from `/api/tags`. For clients that hard-code OpenAI model names such as `gpt-3.5-turbo`, `ollama cp` creates an alias. `ollama launch claude` (and `codex`, `opencode` and others) starts a coding agent already pointed at Ollama. [ol-cloud, ol-oai, ol-cc]
- **Errors.** Standard HTTP codes with `{"error": "..."}`: 429 for a rate limit and 502 when a cloud model cannot be reached. An error in the middle of a stream arrives as an `error` object inside the stream, after the status line has already gone out. [ol-err]
- **Custom models.** A Modelfile (`FROM`, `PARAMETER`, `TEMPLATE`, `SYSTEM`, `CAPABILITY` and others) builds a named variant; `FROM` accepts an existing model, a safetensors directory or a GGUF file. [ol-mf, ol-import]

## Feature parity

Parity here is against the makers' own APIs and against the OpenAI and Anthropic APIs that Ollama imitates. Ollama's pages call each compatibility layer a subset. [ol-oai, ol-ant]

| Feature | Native API | OpenAI-compatible | Anthropic-compatible |
| --- | --- | --- | --- |
| Reasoning control | `think`: `true`, `false`, `null` (model default) or a model-specific level string such as `low`, `medium`, `high`; `/api/show` lists the values and the default | `reasoning_effort` or `reasoning.effort`, with model-defined names and aliases; for a model with thinking metadata, a name it does not list resolves to its default | `thinking.type` `enabled` or `disabled` as an on/off switch, and `output_config.effort` names resolved like the OpenAI ones; `budget_tokens` is accepted but not enforced |
| Tools | yes, including parallel calls and streamed `tool_calls` | yes; `tool_choice` is not supported | yes; `tool_choice` is not supported |
| Structured output | `format`: `"json"` or a full JSON schema | JSON mode and schema | not listed |
| Vision | `images` array of base64 (the SDKs also take paths and URLs) | base64 only; URL images are not supported | base64 only |
| Prompt caching | automatic prefix reuse in the server, visible as `prompt_eval_cached_count`; no explicit cache controls (the cloud price table has a cached-input rate) | no cache controls | `cache_control` not supported |
| Batch API, token counting, citations, PDF | none | no batch API | not supported |
| Streaming | yes | yes | yes |

Details from the pages. The Responses endpoint is stateless: no `previous_response_id`, no `conversation`, no `truncation`. Chat Completions does not support `logprobs`, `logit_bias`, `n` or `user`; Completions also lacks `best_of` and `echo`; embeddings do not accept token arrays as input. The cloud API does not support stateful Responses, built-in web search through `/v1/responses`, or replay of custom tool calls, and the structured-outputs page says Ollama Cloud does not support that feature. Anthropic-compatible token counts are approximations; the cloud endpoint rejects an `anthropic-version` older than `2023-06-01` and needs `Authorization: Bearer` (an `x-api-key` header alone is not accepted); and an error during an Anthropic-format stream comes back as an HTTP status, not as an `error` event. [ol-oai, ol-ant, ol-struct, ol-vision]

Thinking. A `thinking` field is returned next to `content` in chat (and next to `response` in generate), and reasoning tokens stream before answer tokens. Since v0.34.3, `GET /api/show` reports each model's thinking levels and default: the release note's examples are a cloud GLM-5.3-Flash entry with values `low`, `high`, `max` and default `max`, and a local Gemma 4 with levels `false`, `true` and default `true`. [ol-think, ol-rel]

Structured output on thinking models. The v0.34.4 notes say it now applies in a single pass, which they call faster and more reliable. The structured-outputs page advises a low temperature, for example 0, for more deterministic output, and suggests also putting the JSON schema into the prompt as text so the model's answer is grounded in it. [ol-rel, ol-struct]

Web search. Ollama offers a hosted web-search REST API (`POST https://ollama.com/api/web_search`, needs an API key and a free account), and the v0.35.1 notes raise the number of searches a model may run in one response from three to ten. [ol-search, ol-rel]

Long context. The window is the tag's value (128K or 256K on the Gemma 4 tags), but what runs is set by a separate allocation; see the notes below. [ol-ctx, ol-gemma4]

## Pricing

Local use is free and unlimited on every plan. Ollama Cloud is billed as a subscription plus metered tokens. The pricing page lists Free ($0, starter credits, 1 concurrent request), Pro ($20 a month or $200 a year, $60 of monthly usage credits, 3 concurrent requests), Max ($100 a month, $300 of credits, 10 concurrent) and Team ($500 a month in early access, a shared $1,000 of credits, 10 concurrent). Unused credits do not roll over. Usage is metered per million input, cached-input and output tokens at each model's rate; plan credits are used first, then purchased credits, and every plan, Free included, can buy credits. Off-peak rates apply outside 12:00 to 18:00 UTC on weekdays and all day at weekends; on 2026-10-03 the table shows off-peak rows only for `deepseek-v4.1-flash` and `deepseek-v4-pro`, at half the standard rate. The pricing page carries the per-model table, which is not repeated here; per-model prices belong in the model cards. [ol-price]

## Limits and data

- **Rate limits.** Cloud limits are the concurrency numbers above plus credits; the pricing page says requests over the plan's concurrency are queued up to a fixed limit and rejected when that queue is full, and paid plans get an email at 90% of the included usage. No per-minute figures are published. A rate-limit hit returns 429. Locally there are no vendor limits: `OLLAMA_NUM_PARALLEL` (default 1 per model on the FAQ page), `OLLAMA_MAX_LOADED_MODELS` (3 per GPU, or 3 on CPU) and `OLLAMA_MAX_QUEUE` (512) bound concurrency; a request for a model that does not fit in memory waits until one is unloaded, and the FAQ says the server answers 503 once the queue is full. [ol-price, ol-faq, ol-err]
- **Regions.** Local runs wherever the machine is. For the cloud, the pricing page says data is mainly hosted in the United States with possible routing through Europe or Singapore; it gives no region selector or residency option. [ol-price]
- **Retention and training.** Locally, Ollama states it does not see prompts or data. For cloud models it says it processes prompts and responses to serve the request, does not store or log that content and never trains on it, and collects account details and limited usage metadata that exclude prompt and response content. The pricing page says models are hosted with NVIDIA Cloud Providers, from whom Ollama requires no-logging, no-training and zero-data-retention policies. No separate zero-retention option for customers is described, because the stated default is no storage or logging. Cloud models run native weights as released, and on recent NVIDIA hardware may use formats such as NVFP4. Cloud models can be retired; the usage settings list upcoming retirements for models a user has recently used, and downloaded local models are unaffected. [ol-faq, ol-cloud, ol-price]
- **Turning the cloud off.** `OLLAMA_NO_CLOUD=1`, or `disable_ollama_cloud` in `~/.ollama/server.json`, disables cloud features for local-only use, which also removes web search; after a restart the log shows `Ollama cloud disabled: true`. [ol-faq]
- **Hardware.** NVIDIA GPUs with compute capability 5.0 or higher (driver 570 or newer for 5.0 to 6.2, 550 or newer otherwise); AMD Radeon and Instinct through ROCm v7 on Linux and a narrower set on Windows; Apple GPUs through Metal; Intel and further AMD GPUs through Vulkan on Windows and Linux. macOS needs 14 (Sonoma) or newer and uses the GPU only on Apple silicon (Intel Macs run on CPU). Windows needs 10 22H2 or newer, with NVIDIA driver 551.61 or newer for NVIDIA cards. Models are stored under `~/.ollama/models` on macOS and `C:\Users\<name>\.ollama\models` on Windows, and `OLLAMA_MODELS` moves them. [ol-gpu, ol-mac, ol-win, ol-faq]
- **Formats and quantisation.** Library models are GGUF builds or, on Apple silicon, MLX builds. Import accepts safetensors directories and GGUF files; the import page states Ollama does not quantise GGUF files on import, so a file must be pre-quantised, for example with llama.cpp's `llama-quantize`. The KV cache can be quantised with `OLLAMA_KV_CACHE_TYPE` (the FAQ gives about half the cache memory of `f16` for `q8_0` and about a quarter for `q4_0`, with flash attention on); the setting is global to the server, and the FAQ says models with a high grouped-query-attention count, such as Qwen2, can lose more precision. [ol-import, ol-faq]

## Notes for agents and harnesses

- **Context length.** Two Ollama pages disagree on the default. The context-length page says it depends on VRAM: 4k tokens under 24 GiB, 32k from 24 to 48 GiB, 256k at 48 GiB or more. The FAQ says the default window is 4096 tokens, and the Modelfile page lists the `num_ctx` default as 2048. The pages do not say which applies to a given install; `ollama ps` shows the allocation in use. The context-length page recommends at least 64,000 tokens for web search, agents and coding tools and says a larger window needs more memory; the FAQ says memory scales with `OLLAMA_NUM_PARALLEL` times the context length (a 2K window with 4 parallel requests becomes 8K). A prompt longer than the allocated window is a configuration limit, not a model limit; the settings are `OLLAMA_CONTEXT_LENGTH`, the app slider, or `num_ctx` per request. Cloud models default to their maximum. [ol-ctx, ol-faq, ol-mf]
- **The compatibility endpoints cannot set the window.** The OpenAI page points to a Modelfile for context size, and `num_ctx` is a native-API option. A client that speaks only OpenAI or Anthropic format depends on the server-side setting. [ol-oai]
- **Parameter defaults.** The Modelfile page lists `temperature` 0.8, `top_k` 40, `top_p` 0.9, `repeat_penalty` 1.0, `num_predict` -1 and `seed` 0 as defaults; a library model may ship its own values. A client that omits sampling parameters gets the packaged defaults, not those of the maker's API. [ol-mf]
- **Effort mapping.** `reasoning_effort` names are model-defined. `/api/show` reports a model's accepted values (for example `low`, `high`, `max` for one cloud model, only `false` and `true` for another), and for a model with that metadata a name it does not list falls back to its default instead of returning an error. Models without metadata use fixed aliases (`minimal` to `low`, `xhigh` or `ultra` to `max`); gpt-oss maps `minimal` to `low` and `xhigh` or `ultra` to `high`; a boolean-only model maps any recognised effort to `true` and `none` to `false`. On the Anthropic endpoint, models without metadata map `xhigh` to `high`. A client that sends a level the model lacks therefore cannot tell from the response whether it took effect; reading `/api/show` first avoids the guess. [ol-think, ol-oai, ol-ant, ol-rel]
- **Tool use depends on the model's template.** The tool-calling page documents single, parallel and streamed calls, and says that when streaming, the thinking, content and `tool_calls` fragments are accumulated and sent back with the tool result. Not every library model carries the `tools` capability tag. Because `tool_choice` is unsupported on both compatibility endpoints, a client cannot force a tool call and has to handle a plain-text reply. [ol-tools, ol-oai, ol-ant, ol-lib]
- **Images.** Base64 works; URL images fail on the OpenAI and Anthropic endpoints. [ol-oai, ol-ant]
- **Cloud and local differ.** The cloud lacks structured outputs, stateful Responses and some tool-replay forms, so a test that passes against a local server can fail against `ollama.com`. [ol-oai, ol-struct]
- **Model swapping.** `OLLAMA_KEEP_ALIVE` unloads an idle model after 5 minutes by default, so the first request after a pause pays a load. Memory and `OLLAMA_MAX_LOADED_MODELS` decide whether two models stay resident; otherwise requests queue. [ol-faq]
- **Coding agents.** Ollama documents `ollama launch claude` through the Anthropic endpoint and equivalents for other agents; its Claude Code page suggests a context length of 64k or more for larger repositories and a cloud model that supports tools, and says hosted web search and advanced tool controls are not fully supported. That endpoint has no `tool_choice`, prompt caching or token counting, which an agent that relies on them has to tolerate. [ol-cc, ol-ant, ol-ctx]
- **Version drift.** The product ships often: the releases page lists 15 releases, one a release candidate, between 2026-08-14 and 2026-09-29. The v0.40.0 release candidate switches supported architectures to MLX by default on Apple silicon, which can change speed and feature support; a test that depends on behaviour needs a pinned version. [ol-rel]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| ol-docs | https://docs.ollama.com/ | L | 2026-10-03 |
| ol-docs-index | https://docs.ollama.com/llms.txt | L | 2026-10-03 |
| ol-api | https://docs.ollama.com/api/introduction | L | 2026-10-03 |
| ol-oai | https://docs.ollama.com/api/openai-compatibility | L | 2026-10-03 |
| ol-ant | https://docs.ollama.com/api/anthropic-compatibility | L | 2026-10-03 |
| ol-usage | https://docs.ollama.com/api/usage | L | 2026-10-03 |
| ol-err | https://docs.ollama.com/api/errors | L | 2026-10-03 |
| ol-cloud | https://docs.ollama.com/cloud | L | 2026-10-03 |
| ol-ctx | https://docs.ollama.com/context-length | L | 2026-10-03 |
| ol-faq | https://docs.ollama.com/faq | L | 2026-10-03 |
| ol-gpu | https://docs.ollama.com/gpu | L | 2026-10-03 |
| ol-import | https://docs.ollama.com/import | L | 2026-10-03 |
| ol-mf | https://docs.ollama.com/modelfile | L | 2026-10-03 |
| ol-mac | https://docs.ollama.com/macos | L | 2026-10-03 |
| ol-win | https://docs.ollama.com/windows | L | 2026-10-03 |
| ol-struct | https://docs.ollama.com/capabilities/structured-outputs | L | 2026-10-03 |
| ol-tools | https://docs.ollama.com/capabilities/tool-calling | L | 2026-10-03 |
| ol-think | https://docs.ollama.com/capabilities/thinking | L | 2026-10-03 |
| ol-vision | https://docs.ollama.com/capabilities/vision | L | 2026-10-03 |
| ol-stream | https://docs.ollama.com/capabilities/streaming | L | 2026-10-03 |
| ol-search | https://docs.ollama.com/capabilities/web-search | L | 2026-10-03 |
| ol-cc | https://docs.ollama.com/integrations/claude-code | L | 2026-10-03 |
| ol-price | https://ollama.com/pricing | L | 2026-10-03 |
| ol-lib | https://ollama.com/library | L | 2026-10-03 |
| ol-gemma4 | https://ollama.com/library/gemma4 | L | 2026-10-03 |
| ol-qwen38 | https://ollama.com/library/qwen3.8/tags | L | 2026-10-03 |
| ol-cloud-list | https://ollama.com/search?c=cloud | L | 2026-10-03 |
| ol-repo | https://github.com/ollama/ollama | L | 2026-10-03 |
| ol-rel | https://github.com/ollama/ollama/releases | L | 2026-10-03 |
