---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: local runtime
sources:
  - https://docs.sglang.io/
  - https://github.com/sgl-project/sglang
  - https://github.com/sgl-project/sglang/releases
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/get-started/install.mdx
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/basic_usage/openai_api_completions.mdx
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/basic_usage/anthropic_api.mdx
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/basic_usage/ollama_api.mdx
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/basic_usage/overview.mdx
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/advanced_features/server_arguments.mdx
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/advanced_features/structured_outputs.mdx
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/advanced_features/structured_outputs_for_reasoning_models.mdx
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/advanced_features/tool_parser.mdx
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/advanced_features/separate_reasoning.mdx
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/advanced_features/sgl_model_gateway.mdx
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/apple_metal.mdx
  - https://github.com/sgl-project/sglang/blob/main/docs/docs/references/faq.mdx
  - https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/entrypoints/openai/protocol.py
  - https://github.com/sgl-project/sglang/tree/main/docs/docs/supported-models
---

# SGLang

local runtime

SGLang is an Apache-2.0 inference framework for large language, vision-language and diffusion models, hosted by the non-profit LMSYS. Like vLLM it is a server for many concurrent requests on accelerators. Its prefix cache, which the server-argument page calls RadixAttention (switched off by `--disable-radix-cache`), reuses the computed attention state of a shared prompt prefix across requests; v0.5.21 moved it to a Rust core by default. The README names agent workloads, reinforcement-learning rollouts and large-scale serving as its targets, and each recent release note opens with a table of the models it adds. `sglang serve` (or `python -m sglang.launch_server`) starts an HTTP server with OpenAI-compatible, Anthropic-compatible and Ollama-compatible routes on 127.0.0.1:30000 by default. On 2026-10-03 the latest release is v0.5.21 (2026-10-02); releases have come about every two weeks (v0.5.17 on 2026-08-08 to v0.5.21). [sg-readme, sg-rel, sg-args]

## Models offered

SGLang runs models from Hugging Face or disk by repository path (`--model-path`). Its documentation site carries a "cookbook" of verified launch commands per model, hardware and quantisation, and a supported-models section for text, multimodal, embedding, reward, rerank, classification and decision models, plus a Transformers fallback page for architectures without a native implementation. It hosts no models and has no service. [sg-readme, sg-rel, sg-models]

Models in this library that SGLang's release notes or parser lists name:

| Model file | What the SGLang sources say |
| --- | --- |
| [DeepSeek V4.1-Flash](../models/deepseek/deepseek-flash.md) | added in v0.5.21, with a cookbook page |
| [GLM-5.3-Flash](../models/zai/glm-5.3-flash.md), [GLM-5.2](../models/zai/glm-5.2.md) | GLM-5.3-Flash added in v0.5.20; the Anthropic-route tutorial uses a GLM-5.2 FP8 launch with `glm45` and `glm47` parsers |
| [MiMo-V2.6-Pro](../models/other/mimo-v2.6-pro.md) (the note says "MiMo-V2.6 / MiMo-V2.6-Pro"; whether that covers [MiMo-V2.6-Flash](../models/other/mimo-v2.6-flash.md) is not stated) | added in v0.5.21, with a cookbook page; `mimo` reasoning and tool-call parsers exist |
| [Hy4-Preview](../models/other/hy4-preview.md) | added in v0.5.20 |
| [Qwen3.8 2.4T-A95B](../models/alibaba/qwen3.8-2.4t-a95b.md), [Qwen3.8 27B](../models/alibaba/qwen3.8-27b.md), [Qwen3.8-Flash-Next](../models/alibaba/qwen3.8-flash-next.md) | added in v0.5.19 (the first two) and v0.5.20 |
| [Muse Glimmer 30B](../models/meta/muse-glimmer-30b.md) | added in v0.5.18; parsers `muse` |
| [Kimi K3](../models/moonshot/kimi-k3.md) | parsers `kimi_k3` for tool calls and reasoning |
| [MiniMax M3](../models/minimax/MiniMax-M3.md) | parsers `minimax-m3` |
| [Gemma 4](../models/google/gemma-4-26b-a4b-it.md) | `gemma4` reasoning and tool-call parsers |
| [gpt-oss 20B](../models/openai/gpt-oss-20b.md) and [120B](../models/openai/gpt-oss-120b.md) | a `gpt-oss` tool parser, with a documented caveat below |
| [K2-Horizon](../models/other/k2-horizon-375b-a23b.md) | added in v0.5.20, with a cookbook page; `k2_horizon` reasoning and tool-call parsers |
| [Nemotron 3 Ultra](../models/other/nemotron-3-ultra.md), [Mistral Large 3](../models/mistral/mistral-large-3.md), [Inkling](../models/other/inkling.md) | reasoning parsers named `nemotron_3`, `mistral` and `inkling` (the last two also as tool-call parsers); whether `nemotron_3` and `mistral` cover these exact models is not stated |

[sg-rel, sg-args, sg-tools, sg-reason]

## API surface

- **OpenAI-compatible routes.** Chat completions, completions, embeddings and vision input are documented; the protocol source also defines request models for responses, classification, reranking, scoring, tokenisation, transcription and decision models, which the pages read did not describe. The server applies the chat template from the Hugging Face tokenizer unless `--chat-template` names another. [sg-oai, sg-args, sg-proto]
- **Anthropic-compatible route.** `POST /v1/messages` and `/v1/messages/count_tokens` are registered on every server with no flag; they reuse the model, chat template and the same reasoning and tool-call parsers, with streaming and tool use. The server does not check the request's `model` field and serves the model it loaded, so a client can send any name. [sg-ant]
- **Ollama-compatible route.** `/api/chat`, `/api/generate`, `/api/tags`, `/api/show` and a health check at `/`, so the Ollama CLI and Python library can use SGLang as the backend; the model name must match the launch name exactly. [sg-ollama]
- **Native routes.** A native generate API with its own sampling parameters, an offline engine API in Python, Prometheus metrics (`--enable-metrics`), and a model gateway ("SMG") that balances traffic across workers over HTTP, gRPC and OpenAI-compatible protocols, with its own rate limiting, TLS and mutual TLS to workers. [sg-overview, sg-args, sg-gateway]
- **Auth.** `--api-key` sets a key for the server and the OpenAI-compatible routes, and `--admin-api-key` guards administrative routes (weight updates, cache flush, `/server_info`). Default none. `--host` and `--port` set the bind address (defaults 127.0.0.1 and 30000). `--allowed-media-domains` restricts remote image, video and audio URLs for a multimodal server that takes untrusted input. [sg-args]
- **SDKs.** The Python package and an offline `Engine`; no client SDK beyond the OpenAI and Anthropic SDKs. [sg-overview, sg-readme]
- **Model ids.** The path used at start; `--served-model-name` overrides what `/v1/models` returns. [sg-args]
- **Install.** Docker (`lmsysorg/sglang`, CUDA 13 images; the last CUDA 12 tag is v0.5.19-cu129), `uv pip install --prerelease=allow sglang` with Python 3.10 or newer and CUDA 13, or source. [sg-install, sg-readme]

## Feature parity

Parity is against the makers' APIs and the OpenAI and Anthropic APIs SGLang imitates. [sg-oai, sg-ant]

| Feature | What the docs and source say |
| --- | --- |
| Reasoning control | `reasoning_effort` on chat completions accepts `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, `max` or a float from 0.0 to 0.99; `none` defaults `thinking` and `enable_thinking` to false in `chat_template_kwargs`; the source says it is not supported on the harmony (gpt-oss) path. `chat_template_kwargs` such as `enable_thinking` (Qwen3) or `thinking` (DeepSeek-V3) works per request or as a server default (`--default-chat-template-kwargs`, which applies to Chat Completions, Responses and Anthropic requests but not the Ollama route); a per-request value wins. The docs say the reasoning parser only separates reasoning text; it does not turn reasoning on. |
| Tools | OpenAI-style tool use with a per-family `--tool-call-parser` (or `auto`, detected from the template); the Anthropic route shares the parsers. `parallel_tool_calls` defaults to true in the request schema. |
| Structured output | JSON schema, regular expression or EBNF constraints, one per request, with xgrammar as the default backend, or outlines (no EBNF) or llguidance; `response_format` with a JSON schema on the OpenAI route. For reasoning models, a `--reasoning-parser` lets the model think freely before the grammar applies. |
| Vision, audio | vision-language input on the OpenAI route, with media-domain limits and a 64 MiB default cap per remote media download; the protocol source defines a transcription request model for speech. |
| Prompt caching | RadixAttention prefix caching, on unless `--disable-radix-cache` is set; `--enable-cache-report` returns cached-token counts in `usage.prompt_tokens_details`; HiCache adds cache levels in host memory and external storage. No explicit cache markers. |
| Batch | no batch API described in the pages read (the protocol source defines OpenAI-style file and batch request models); continuous batching and `--max-running-requests`. |
| Long context | `--context-length` (default: the model's configuration), chunked prefill (`--chunked-prefill-size`), context and prefill parallelism, and a quantised KV cache (`fp8_e4m3`, `fp8_e5m2`, `nvfp4`, `fp4_mx_block16`). |
| Streaming | server-sent events on the OpenAI and Anthropic routes. |
| Speculative decoding | EAGLE and others, set by `--speculative-num-steps`, `--speculative-eagle-topk` and `--speculative-num-draft-tokens` (the Anthropic guide's GLM-5.2 example uses EAGLE with 5 steps, top-k 1 and 6 draft tokens). |

The OpenAI-compatible reasoning output in the documentation's example is `message.reasoning_content`; `separate_reasoning` defaults to true, and false keeps the reasoning in `content`. Qwen3-Thinking models always reason and ignore `enable_thinking`. `logit_bias` is supported on chat completions and completions, with values from -100 to 100. [sg-reason, sg-oai, sg-struct, sg-structr, sg-proto, sg-args, sg-ant]

## Pricing

Free, open-source software; no charge, plans or cloud. Cost is hardware and operation. Enterprise support and consulting are offered by contact to the project's address, with no published price. [sg-readme]

## Limits and data

- **Rate limits.** None from the server by default. Capacity is set by `--max-running-requests`, `--max-queued-requests`, the KV memory pool (`--mem-fraction-static`, computed from GPU memory when unset, or 0.88 when it cannot be detected) and chunked-prefill size; requests beyond capacity queue. The gateway adds optional concurrency and token-rate limits with a FIFO queue, returning 429 when the queue is full and 408 when a queued request times out. [sg-args, sg-faq, sg-gateway]
- **Regions.** Wherever the machine runs. [sg-readme]
- **Retention and training.** Prompts stay in the operator's deployment. The pages read describe no usage reporting, and the source was not audited for network calls. The gateway's "Storage and Privacy" section says conversation and response history for `/v1/responses`, MCP sessions and the conversation APIs is kept at the router tier, in memory, nowhere, Oracle ATP or PostgreSQL, so it need not be sent to upstream vendors. [sg-gateway]
- **Hardware.** NVIDIA (A100, H100/H200/H800/H20, B200/B300/GB200/GB300, some RTX parts, DGX Spark and Jetson Orin), AMD Instinct (MI300X to MI355X), Google TPU (v6e, v7), Intel Arc GPUs and Xeon CPUs, Apple silicon through MLX on macOS 14 or newer with MLX 0.32.0 or newer (with `SGLANG_USE_MLX=1`; without it SGLang falls back to `torch.mps`), Huawei Ascend and Moore Threads; others are in progress. [sg-readme, sg-apple]
- **Formats and quantisation.** Hugging Face checkpoints, with `--quantization` choices that include awq, fp8, mxfp8, gptq, gguf, bitsandbytes, modelopt variants, mxfp4, NVFP4 variants, compressed-tensors, quark and MLX 4-bit and 8-bit; `--modelopt-quant` quantises with NVIDIA Model Optimizer at launch (fp8, int4_awq, w4a8_awq, nvfp4, nvfp4_awq). [sg-args]

## Notes for agents and harnesses

- **Parsers decide structure.** Reasoning and tool calls come back structured only when `--reasoning-parser` and `--tool-call-parser` suit the model; `auto` detects them from the chat template. The Anthropic guide says that without a tool-call parser the tool schemas are still accepted but tool calls come back as raw text, which a client such as Claude Code cannot execute. [sg-args, sg-tools, sg-reason, sg-ant]
- **gpt-oss tool parser drops the analysis channel.** The tool parser filters out analysis-channel events and keeps only normal text, which can leave `content` empty when the model's explanation went to the analysis channel; the docs describe a workaround on the same page. [sg-tools]
- **Reasoning effort is two mechanisms.** `reasoning_effort` and `chat_template_kwargs` are separate paths, and the docs say to set `reasoning_effort` in either the server defaults or the request, not both. [sg-oai]
- **Prefix-cache reuse depends on the prompt's first differing token.** For Claude Code through the Anthropic route, SGLang's guide says the client puts a per-request hash at the start of the system prompt, so the radix cache reuses only a short prefix and re-processes the whole history each turn; setting `CLAUDE_CODE_ATTRIBUTION_HEADER=0` removes the line. The same guide notes that `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` does not remove it, and that a `[1m]` model-name suffix is a client-side hint for the 1M-context beta that the server ignores. It also raises `API_TIMEOUT_MS` because long reasoning turns exceed the client's default timeout. [sg-ant]
- **Memory tuning.** The FAQ's advice for out-of-memory errors is to lower `--chunked-prefill-size` (to 4096 or 2048) for prefill failures, `--max-running-requests` for decode failures and `--mem-fraction-static` for both; requesting input logprobs for a long prompt is a common cause, avoided by `logprob_start_len`. [sg-faq, sg-args]
- **Not deterministic at temperature 0.** The FAQ says repeated identical requests can differ slightly even at temperature 0, and attributes about 95% of this to dynamic batching and the rest to prefix caching; `--disable-radix-cache` with one request at a time makes output mostly deterministic, and `--enable-deterministic-inference` is a separate mode. [sg-faq]
- **Schema in the prompt too.** The structured-outputs page advises describing the wanted format in the prompt in addition to constraining it, for output quality. For reasoning models, the native API needs `require_reasoning` set to true for the model to think before the constrained output; chat completions do not. [sg-struct, sg-structr]
- **Docs moved.** The old `docs.sglang.ai` address redirects to `docs.sglang.io`, which is where the project's README now points. [sg-docs, sg-readme]
- **Version drift.** Each release adds models and parsers, and the install page itself recommends a specific release or dated nightly tag for reproducible deployments; a test that relies on parser behaviour is only reproducible against one. [sg-rel, sg-install]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| sg-docs | https://docs.sglang.io/ | L | 2026-10-03 |
| sg-readme | https://github.com/sgl-project/sglang | L | 2026-10-03 |
| sg-rel | https://github.com/sgl-project/sglang/releases | L | 2026-10-03 |
| sg-install | https://github.com/sgl-project/sglang/blob/main/docs/docs/get-started/install.mdx | L | 2026-10-03 |
| sg-oai | https://github.com/sgl-project/sglang/blob/main/docs/docs/basic_usage/openai_api_completions.mdx | L | 2026-10-03 |
| sg-ant | https://github.com/sgl-project/sglang/blob/main/docs/docs/basic_usage/anthropic_api.mdx | L | 2026-10-03 |
| sg-ollama | https://github.com/sgl-project/sglang/blob/main/docs/docs/basic_usage/ollama_api.mdx | L | 2026-10-03 |
| sg-overview | https://github.com/sgl-project/sglang/blob/main/docs/docs/basic_usage/overview.mdx | L | 2026-10-03 |
| sg-args | https://github.com/sgl-project/sglang/blob/main/docs/docs/advanced_features/server_arguments.mdx | L | 2026-10-03 |
| sg-struct | https://github.com/sgl-project/sglang/blob/main/docs/docs/advanced_features/structured_outputs.mdx | L | 2026-10-03 |
| sg-structr | https://github.com/sgl-project/sglang/blob/main/docs/docs/advanced_features/structured_outputs_for_reasoning_models.mdx | L | 2026-10-03 |
| sg-tools | https://github.com/sgl-project/sglang/blob/main/docs/docs/advanced_features/tool_parser.mdx | L | 2026-10-03 |
| sg-reason | https://github.com/sgl-project/sglang/blob/main/docs/docs/advanced_features/separate_reasoning.mdx | L | 2026-10-03 |
| sg-gateway | https://github.com/sgl-project/sglang/blob/main/docs/docs/advanced_features/sgl_model_gateway.mdx | L | 2026-10-03 |
| sg-apple | https://github.com/sgl-project/sglang/blob/main/docs/docs/hardware-platforms/apple_metal.mdx | L | 2026-10-03 |
| sg-faq | https://github.com/sgl-project/sglang/blob/main/docs/docs/references/faq.mdx | L | 2026-10-03 |
| sg-proto | https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/entrypoints/openai/protocol.py | L | 2026-10-03 |
| sg-models | https://github.com/sgl-project/sglang/tree/main/docs/docs/supported-models | L | 2026-10-03 |
