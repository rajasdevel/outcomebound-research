---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: local runtime
sources:
  - https://github.com/ggml-org/llama.cpp
  - https://github.com/ggml-org/llama.cpp/releases
  - https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md
  - https://github.com/ggml-org/llama.cpp/blob/master/docs/function-calling.md
  - https://github.com/ggml-org/llama.cpp/blob/master/docs/multimodal.md
  - https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md
---

# llama.cpp

local runtime

llama.cpp is an MIT-licensed C and C++ inference engine, built on the ggml tensor library, that runs quantised language and vision-language models on CPUs and many kinds of GPU. It reads and writes the GGUF file format, which Ollama and LM Studio also load, and it ships a command-line chat tool, an HTTP server (`llama-server`) that offers OpenAI-compatible and Anthropic-compatible endpoints with a web interface, and a quantisation tool. The README's quick start now uses the commands `llama cli` and `llama serve`; the server and quantisation pages still use the binary names `llama-server` and `llama-quantize`. There are no release numbers in the usual sense: the repository publishes a build per merged change, tagged `b<N>` (b11378, published at 15:00 UTC on 2026-10-03, when this file was checked), alongside a separate `v` tag series (v0.1.0 to v0.5.0). This file covers the server, since that is the part an application calls. [lc-readme, lc-rel, lc-server]

## Models offered

llama.cpp serves any model whose architecture it implements and whose weights are in GGUF. `-hf <user>/<model>[:quant]` downloads a GGUF from Hugging Face (the quant defaults to `Q4_K_M`, or the first file in the repository if that quant is absent, and a multimodal projector is fetched automatically when one exists). `-m` loads a local file, and `convert_hf_to_gguf.py` makes a GGUF from a Hugging Face checkpoint. The documentation's own examples use Qwen3.5 (README), Gemma 3 (multimodal page) and Gemma 4 (quantisation page). Function-calling documentation lists native handlers for Llama 3.1, 3.2 and 3.3, Functionary v3.1 and v3.2, Hermes 2 and 3, Qwen 2.5 and Qwen 2.5 Coder, Mistral Nemo, Firefunction v2, Command R7B, DeepSeek R1 (marked work in progress) and gpt-oss (Harmony format), with a generic handler for every other template. [lc-server, lc-readme, lc-mm, lc-quant, lc-fc]

Models in this library whose files name llama.cpp as a route:

| Model file | Source |
| --- | --- |
| [Gemma 4](../models/google/gemma-4-26b-a4b-it.md) family ([E2B](../models/google/gemma-4-e2b-it.md), [E4B](../models/google/gemma-4-e4b-it.md), [31B](../models/google/gemma-4-31b-it.md)) | the models' cards list llama.cpp; the quantisation guide uses `gemma-4-E2B-it` as its worked example |
| [Qwen3.8 27B](../models/alibaba/qwen3.8-27b.md) | its card lists llama.cpp as an access route |
| [Muse Glimmer 30B](../models/meta/muse-glimmer-30b.md) | its file cites a llama.cpp page in Meta's developer docs |
| [gpt-oss 20B](../models/openai/gpt-oss-20b.md) and [120B](../models/openai/gpt-oss-120b.md) | handled by the native Harmony tool-call format |
| [Inkling](../models/other/inkling.md) | its file lists llama.cpp among access routes |

[lc-fc, lc-quant]

llama.cpp has no hosted service and sells nothing; every model comes from the user's disk or Hugging Face. [lc-readme]

## API surface

- **Native routes.** `/completion`, `/tokenize`, `/detokenize`, `/apply-template`, `/embedding`, `/reranking`, `/infill`, `/props`, `/slots` (with save, restore and erase of per-slot prompt caches), `/metrics` (Prometheus, off unless `--metrics`), `/lora-adapters` and `/health`. [lc-server]
- **OpenAI-compatible routes.** `/v1/models`, `/v1/completions`, `/v1/chat/completions`, `/v1/responses`, `/v1/embeddings` and token counting at `/v1/responses/input_tokens` and `/v1/chat/completions/input_tokens`. The README says it makes no strong claim of full compatibility. A control route, `/v1/chat/completions/control`, can end a running reasoning block early. [lc-server]
- **Anthropic-compatible routes.** `POST /v1/messages` (with `max_tokens` defaulting to 4096) and `/v1/messages/count_tokens`; tool use there needs `--jinja`. A `/v1/systemone` route answers typed questions with a decision model, compatible with TypeSafe's System One API. [lc-server]
- **Auth.** None by default. `--api-key` (a comma-separated list, or `--api-key-file`) turns on key checking; errors use OpenAI's format, and the README's example is a 401 `authentication_error`. The server listens on 127.0.0.1:8080 by default (`--host`, `--port`). By default CORS reflects any origin with credentials allowed; with `--tools` or `--agent` (or MCP servers configured) the CORS origin defaults to localhost because those expose file access. [lc-server]
- **Model ids.** A single-model server ignores the `model` field's value (the README's examples send `gpt-3.5-turbo`). A router mode, started by running `llama-server` with no model, serves several models from the Hugging Face cache, a directory (`--models-dir`) or an INI preset file, and routes by the request's `model`; at most 4 stay loaded by default (`--models-max`). [lc-server]
- **SDKs.** None official. Clients use the OpenAI or Anthropic SDKs against the server, or HTTP directly. [lc-server]

## Feature parity

Parity is against the makers' APIs and the OpenAI and Anthropic APIs the server imitates. The server's own text lists what it supports; it publishes no list of unsupported fields. [lc-server]

| Feature | What the server documents |
| --- | --- |
| Reasoning control | `reasoning_effort` on a request (`none` turns reasoning off; any other value is passed to the Jinja template), `--reasoning on\|off\|auto`, `--reasoning-effort` (`minimal` up to `max`), and `--reasoning-budget` (tokens; -1 unlimited, 0 ends thinking at once). `reasoning_format` chooses whether thought text is returned in `reasoning_content`, left in `content`, or kept with its tags. `chat_template_kwargs` such as `{"enable_thinking": false}` reaches the template. |
| Tools | OpenAI-style function calling, with `--jinja` (the parameter table lists it as on by default; the endpoint text still says the flag is needed). Native parsers per template family and a generic fallback, which the function-calling page says can use more tokens. `parallel_tool_calls` works on some models only and is off unless the request sets it to true. On the Anthropic route `tool_choice` takes `auto`, `any` or a named tool. |
| Structured output | `response_format` of `json_object` or a JSON schema, a `--json-schema` server flag, and GBNF-style grammars (`--grammar`, `--grammar-file`). |
| Vision, audio, video | through the multimodal library (`libmtmd`) on `/v1/chat/completions`, with a projector file; the multimodal page lists image, audio and video input. The server page calls multimodal support experimental. |
| Prompt caching | automatic reuse of the prompt shared with an earlier request in a slot, on by default (`--cache-prompt`); a RAM cache for idle slots (`--cache-ram`, 8,192 MiB by default); `usage.prompt_tokens_details.cached_tokens` and a `timings.cache_n` field report reuse. No explicit cache markers. |
| Batch | no batch API; continuous batching across parallel slots (`--parallel`, auto by default). |
| Long context | `-c`/`--ctx-size` (0 means the model's trained value) with a `--fit` step that shrinks unset values to fit memory; K and V cache types can be quantised (`q8_0`, `q4_0` and others). Context shift is off by default. |
| Streaming | server-sent events on all chat routes. |
| Speculative decoding | `--spec-type` selects among a draft model, EAGLE-3, MTP, DFlash and several n-gram methods (default none); a draft model comes from `--model-draft` or `--hf-repo-draft`, and drafts 3 tokens per step by default. |

[lc-server, lc-fc]

## Pricing

Free, open-source software with no vendor charge for use, including commercial use under the MIT licence. Costs are the user's hardware, power and any hosted machine. No cloud, credits or plans exist. [lc-readme]

## Limits and data

- **Rate limits.** None imposed by software. Concurrency is the slot count (`--parallel`); further requests wait. The default socket timeout is 3,600 seconds (`--timeout`). [lc-server]
- **Regions.** Wherever the server runs. [lc-server]
- **Retention and training.** The pages read describe a local server and state nothing either way about telemetry or data collection; the source was not audited for network calls. Prompt state lives in memory and, if the operator sets `--slot-save-path`, in slot-save files. Network use that the pages do document is downloading models from Hugging Face when `-hf` is used, and the optional web interface's MCP CORS proxy, which the server page labels experimental and says not to enable in untrusted environments. An optional idle sleep (`--sleep-idle-seconds`) unloads the model and its KV cache from memory until the next request. [lc-server]
- **Security of optional agent features.** `--tools` (file read, write, glob and grep search, shell execution, edit and an info tool) and `--agent` expose file access and command execution to whoever can reach the API; the server page marks the tools experimental and not for untrusted environments, and `--tools-runtime` can run them in a Docker or Podman container or on a remote host over SSH. MCP servers declared in a JSON file run as child processes with the server's privileges. [lc-server]
- **Hardware.** CPU (AVX, AVX2, AVX512 and AMX on x86, NEON on Arm, RISC-V vector extensions, BLAS and BLIS, ZenDNN for AMD CPUs); NVIDIA through CUDA, AMD through HIP, Moore Threads through MUSA, Apple silicon through Metal, plus Vulkan, SYCL (Intel GPUs), OpenCL (Adreno), Ascend CANN, Snapdragon Hexagon, IBM zDNN, VirtGPU, WebGPU and an OpenVINO backend marked in progress. CPU and GPU hybrid inference is supported for models larger than VRAM, and the backend table also lists an RPC backend. [lc-readme]
- **Formats and quantisation.** GGUF with 1.5-bit to 8-bit integer quantisation, plus high-precision files (the quantisation page names F32 and BF16 as typical inputs). `llama-quantize` converts a high-precision GGUF to a quantised one (for example `Q4_K_M`) and takes an importance-matrix file; the tool's page says quantisation may lose accuracy, usually measured in perplexity or KL divergence, and that an importance matrix can reduce the loss. Requantising an already quantised file can reduce quality severely. A multimodal model needs a second GGUF for its projector, which the quantisation page says is usually kept at BF16 or Q8 because a smaller projector saves little and can cost quality. [lc-quant, lc-mm]

## Notes for agents and harnesses

- **Chat template decides tool and reasoning behaviour.** Tool calls and reasoning are parsed according to the model's Jinja template. When the template is not recognised the server logs `Chat format: Generic` and falls back to a format that uses more tokens and is less efficient. The documentation suggests `--chat-template-file` with a better template, and `--chat-template chatml` as a last resort. Tool calls that arrive as plain text are consistent with the generic path, and the log line shows which format was chosen. [lc-fc, lc-server]
- **Parallel slots and context.** The server page documents a unified KV buffer shared across slots (on when the slot count is automatic), a per-slot limit (`--kv-unified-per-slot`) and `n_ctx` per slot in the `/slots` output, but does not say in prose how `-c` is shared among slots. A harness that runs many concurrent requests can read the per-slot `n_ctx` from `/slots`. The `timings` object gives `prompt_n + cache_n + predicted_n` as the context in use. [lc-server]
- **`--fit` can change an unset context.** Because fitting is on by default and shrinks unset arguments to fit device memory (not below `--fit-ctx`, default 4,096), a server started without `-c` on a small GPU may run with a smaller window than the model supports. An explicit `-c` is a set argument, so fitting does not shrink it. [lc-server]
- **Sampling defaults come from the request or the server flags.** A client that sends nothing gets llama.cpp's sampler defaults (the flag table lists temperature 0.80, `top_k` 40 and `top_p` 0.95), not the maker's recommended settings, so values from a model card must be passed explicitly. `/completion`-specific options such as `mirostat` are also accepted on the chat route. [lc-server]
- **`max_tokens` on the Anthropic route.** The default is 4096, a low ceiling for a thinking model, so a harness that omits it can see a cut-off answer. [lc-server]
- **Preserved reasoning.** `--reasoning-preserve` (on by default) keeps earlier reasoning in the history for templates that declare support, such as the Z.ai preserved-thinking mode; templates without it ignore the setting. [lc-server]
- **Exposure.** Binding to `0.0.0.0` without `--api-key` exposes the whole server, including the slot save and props routes if enabled. For a public deployment the server page's table recommends an API key and a reverse proxy, with `--cors-origins` optional; for a local network it recommends setting `--cors-origins` to the front end's origin. [lc-server]
- **Build drift.** Several builds land each day (five on the morning of 2026-10-03 alone), and recent build notes show model-specific parser fixes (for example, b11377 makes one family's chat parser honour `response_format` JSON schemas, which it had left unconstrained). A test that depends on tool-call parsing, structured output or reasoning extraction is only reproducible against a pinned build number. [lc-rel]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| lc-readme | https://github.com/ggml-org/llama.cpp | L | 2026-10-03 |
| lc-rel | https://github.com/ggml-org/llama.cpp/releases | L | 2026-10-03 |
| lc-server | https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md | L | 2026-10-03 |
| lc-fc | https://github.com/ggml-org/llama.cpp/blob/master/docs/function-calling.md | L | 2026-10-03 |
| lc-mm | https://github.com/ggml-org/llama.cpp/blob/master/docs/multimodal.md | L | 2026-10-03 |
| lc-quant | https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md | L | 2026-10-03 |
