---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: local runtime
sources:
  - https://github.com/ml-explore/mlx-lm
  - https://github.com/ml-explore/mlx-lm/blob/main/README.md
  - https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md
  - https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/server.py
  - https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/convert.py
  - https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md
  - https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/MANAGE.md
  - https://github.com/ml-explore/mlx-lm/tree/main/mlx_lm/models
  - https://github.com/ml-explore/mlx-lm/tree/main/mlx_lm/tool_parsers
  - https://github.com/ml-explore/mlx-lm/releases
  - https://pypi.org/project/mlx-lm/
  - https://github.com/ml-explore/mlx-lm/commits/main
  - https://github.com/ml-explore/mlx
  - https://huggingface.co/mlx-community
---

# MLX and mlx-lm

local runtime

MLX is an array framework for machine learning from Apple's machine-learning research group, designed around Apple silicon's unified memory (arrays live in memory shared by the CPU and GPU). `mlx-lm` is a Python package built on it, under the same GitHub organisation and MIT-licensed, that generates text, serves an HTTP API, quantises and converts models, and fine-tunes them with LoRA or full fine-tuning. Ollama (MLX builds of library models, and MLX by default for supported architectures in its v0.40.0 release candidate) and LM Studio also use MLX as an engine on Apple silicon (see [Ollama](ollama.md) and [LM Studio](lm-studio.md)), and SGLang can run on it. On 2026-10-03 the latest release is mlx-lm 0.32.0 (PyPI, 2026-10-01), which requires Python 3.11 or newer and mlx 0.32.2 or newer on macOS. MLX itself also installs with a CUDA backend or a CPU build on Linux. [mx-readme, ml-readme, ml-pypi]

## Models offered

`mlx-lm` runs any Hugging Face repository or local directory whose architecture it implements, in MLX format or from an original Hugging Face repository (the README's command-line example generates directly from one). Some tokenizers need `--trust-remote-code`. The README points to the `mlx-community` organisation on Hugging Face, where thousands of converted and quantised models are published, and uses `mlx-community/Llama-3.2-3B-Instruct-4bit` as the default model for the generate and chat commands. The repository's `models` directory has 135 files on 2026-10-03, most of them one architecture each and a few shared helpers. [ml-readme, ml-models]

Models in this library whose architecture module or tool parser is named in the repository on 2026-10-03:

| Model file | What the repository shows |
| --- | --- |
| [Gemma 4](../models/google/gemma-4-26b-a4b-it.md) family | modules `gemma4` and `gemma4_text`, and a `gemma4` tool parser |
| [gpt-oss 20B](../models/openai/gpt-oss-20b.md) and [120B](../models/openai/gpt-oss-120b.md) | module `gpt_oss` |
| [Kimi K3](../models/moonshot/kimi-k3.md) | module `kimi_k3`, with a `kimi_k3` tool parser |
| [DeepSeek V4.1-Flash](../models/deepseek/deepseek-flash.md) | module `deepseek_v41`, added on the main branch on 2026-09-29; a 2026-10-01 commit credits DeepSeek for the V4.1 support; whether the 0.32.0 package includes it was not checked |
| [MiniMax M3](../models/minimax/MiniMax-M3.md) | module `minimax_m3_vl`; a `minimax_m2` tool parser |
| [Muse Glimmer 30B](../models/meta/muse-glimmer-30b.md) | module `muse_glimmer` |
| [GLM-5.2](../models/zai/glm-5.2.md) | module `glm_moe_dsa` and a `glm47` tool parser; whether that module is the one GLM-5.2 uses was not checked against the model's configuration |
| [MiMo-V2.6-Flash](../models/other/mimo-v2.6-flash.md) | module `mimo_v2_flash`; the version match was not checked |
| [Qwen3.8](../models/alibaba/qwen3.8-27b.md) | the repository has `qwen3_5`, `qwen3_next` and `qwen3_vl` modules and a `qwen3_coder` tool parser; no Qwen3.8 module name was found, and whether Qwen3.8 loads through one of these was not verified |

[ml-models, ml-tp, ml-commits]

There is no hosted service. Models come from the user's disk or Hugging Face. [ml-readme]

## API surface

- **Python API.** `load`, `generate`, `stream_generate`, batch generation, `convert` for quantising and uploading, and a prompt-cache API; the models are called after applying the tokenizer's chat template. [ml-readme]
- **Command line.** `mlx_lm.generate`, `mlx_lm.chat`, `mlx_lm.server`, `mlx_lm.convert`, `mlx_lm.cache_prompt`, `mlx_lm.manage` (scan and delete cached models), `mlx_lm.evaluate`, `mlx_lm.benchmark`, and fine-tuning and fusing commands. [ml-readme, ml-manage, ml-lora]
- **HTTP server.** `mlx_lm.server --model <repo or path>` listens on 127.0.0.1:8080. Routes in the source: `POST /v1/chat/completions` (also `/chat/completions`), `POST /v1/completions`, `GET /v1/models` and `GET /health`. The server page calls the API "similar" to OpenAI's chat API and says the server is not recommended for production because it implements only basic security checks. There is no Anthropic-compatible route, no Responses route and no embeddings route in the source. [ml-server-md, ml-server]
- **Auth.** None in the source (no key option appeared in the argument list or request handler); `--allowed-origins` defaults to `*`. The server binds to localhost unless `--host` is changed. [ml-server]
- **Model ids.** The `model` field in a request is a Hugging Face repository id or a local path relative to the server's working directory, and a request may name a different model from the launch model, which the server then loads. A request without one uses the launch model. `GET /v1/models` lists the models available locally. [ml-server-md, ml-server]
- **Request fields in the source.** `messages`, `stream` and `stream_options.include_usage`, `max_tokens` (or `max_completion_tokens`), `temperature`, `top_p`, `top_k`, `min_p`, `stop`, `seed`, `logit_bias`, `logprobs` and `top_logprobs`, repetition, presence and frequency penalties with context sizes, XTC sampling, `adapters` (a LoRA path), `draft_model` and `num_draft_tokens` for speculative decoding, `chat_template_kwargs`, `role_mapping` for models without a chat template, and `tools`. [ml-server, ml-server-md]

## Feature parity

Parity is against the makers' APIs and the OpenAI API the server imitates. The server page and source are the only documentation, and they are brief; what they do not mention is unverified, not confirmed absent. [ml-server-md, ml-server]

| Feature | What the repository shows |
| --- | --- |
| Reasoning control | no `reasoning_effort` field was found; thinking is switched through the chat template, either per request with `chat_template_kwargs` or server-wide with `--chat-template-args` (for example `{"enable_thinking": false}`). The server separates reasoning text from the answer and returns it in a `reasoning` field of the message or delta. |
| Tools | `tools` are given to the chat template, and tool-call output is parsed by per-family parsers (JSON, pythonic, Mistral, Qwen3-Coder, Kimi K2 and K3, GLM 4.7, MiniMax M2, Gemma 4 and others). A 2026-04 release fixed parallel tool-call handling in the server and in MiniMax M2. No `tool_choice` handling was found. When tools are sent to a model whose tokenizer reports no tool-calling support, the server logs a warning and still passes them to the template. |
| Structured output | no `response_format`, JSON-schema or grammar option appeared in the server source. |
| Vision | vision-language modules exist for some architectures (for example `qwen3_vl`, `pixtral`, `gemma3`); how images are passed through the server route was not checked. |
| Prompt caching | an in-memory LRU cache of prompt KV states (`--prompt-cache-size`, default 10 entries; `--prompt-cache-bytes`), and `usage.prompt_tokens_details.cached_tokens` in responses. A `mlx_lm.cache_prompt` command saves a prompt's cache to a file. No explicit cache markers. |
| Batch | continuous batching of batchable requests (`--decode-concurrency` default 32, `--prompt-concurrency` default 8); the source treats a request as unbatchable when it sets a seed, when a draft model is loaded, when the model's cache type cannot be merged, or when the KV cache is quantised, and such requests run one at a time. |
| Long context | the model's window, with `--max-kv-size` for a rotating fixed-size cache in the CLI, a quantised KV cache (`--kv-bits`, `--kv-group-size`, `--quantized-kv-start` default 5000), and `--prefill-step-size` (default 2048) to bound peak memory while reading a prompt. |
| Streaming | yes (`stream: true`), with optional usage in the final chunk. |
| Speculative decoding | a draft model (`--draft-model`, `--num-draft-tokens` default 3). |

[ml-server-md, ml-server, ml-readme, ml-rel]

## Pricing

Free, open-source software (MIT for both MLX and mlx-lm); no charge, plans or cloud. The cost is a Mac, or a Linux machine with a supported GPU. [ml-readme, mx-readme]

## Limits and data

- **Rate limits.** None from the software. The batch and prompt concurrency flags and available unified memory set the capacity; further requests wait. [ml-server]
- **Regions.** Wherever the machine runs. [ml-readme]
- **Retention and training.** Prompts stay on the machine; the cache holds prompt state in memory unless `mlx_lm.cache_prompt` writes it to a file. The pages read mention no usage reporting and the source was not audited for network calls; the documented network use is downloading models from Hugging Face. [ml-readme, ml-manage]
- **Hardware.** Apple silicon Macs (the Python package installs on macOS and Linux; the MLX CUDA and CPU builds are Linux packages, offered as `cuda12`, `cuda13` and `cpu` extras). Unified memory size decides which models fit: the converted file and the KV cache must both fit, and the quantised KV cache can lower the second. The README says a model that is large relative to RAM can be slow; on macOS 15 or newer mlx-lm wires the model's memory, and raising the `iogpu.wired_limit_mb` system limit can help a model that fits in RAM. [ml-pypi, mx-readme, ml-readme]
- **Formats and quantisation.** Safetensors weights in MLX layout. `mlx_lm.convert` downloads a Hugging Face model, optionally quantises it (`-q`, with `--q-bits`, `--q-group-size`, and `--q-mode` of `affine`, `mxfp4`, `nvfp4` or `mxfp8`, and mixed-precision recipes that its source compares to llama.cpp's Q4_K_M) and can upload it. The LoRA page documents `mlx_lm.fuse --export-gguf`, which writes a fused model to GGUF for Mistral, Mixtral and Llama-style models in fp16 only. LoRA, QLoRA and full fine-tuning and distributed inference through `mx.distributed` are documented. [ml-convert, ml-readme, ml-lora]

## Notes for agents and harnesses

- **Sampling defaults are greedy and short.** The server defaults to `temperature` 0.0, `top_p` 1.0, `top_k` 0 (off), and `max_tokens` 512 unless the launch flags or the request change them. A client that omits `max_tokens` can see a reasoning model cut off mid-thought, and a client that relies on a maker's recommended sampling must send those values or set `--temp`, `--top-p`, `--top-k` and `--min-p` at launch. [ml-server-md, ml-server]
- **No effort control and no schema enforcement.** A client written for `reasoning_effort` or `response_format` gets neither: thinking is switched on or off through `chat_template_kwargs`, and the server source shows no constrained decoding, so JSON validity rests on the prompt and on the client's own checking. [ml-server]
- **Tool calling depends on the template and the parser.** A model without a matching tool parser returns tool calls as text. The parsers listed in the repository cover specific families; a model outside them has to be checked. The April 2026 release notes record fixes for parallel tool calls, so an older install can mishandle them. [ml-tp, ml-rel]
- **Quantised KV cache serialises requests.** `--kv-bits` saves memory on long contexts but disables batching, so concurrency falls to one request at a time; the server page also warns that attention on a quantised cache is not fused, so a large `--prefill-step-size` can cost more memory than the cache saves. [ml-server-md]
- **Exposure.** The server page says it is not recommended for production because it implements only basic security checks; the source shows no authentication and CORS open to every origin by default, and it binds to 127.0.0.1 unless `--host` changes it. [ml-server-md, ml-server]
- **Model downloads happen on first request.** The server downloads a named Hugging Face model if it is not cached, and a request can name a model other than the launch model, which then loads and takes memory. [ml-server-md, ml-server]
- **Release notes lag the code.** GitHub release notes stop at 0.31.3 (2026-04-22) and the 0.32.0 package is a tag and PyPI upload without release notes read, while the main branch receives commits daily. A pinned package version can differ from the main branch in model support. [ml-rel, ml-pypi, ml-commits]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| ml-readme | https://github.com/ml-explore/mlx-lm/blob/main/README.md | L | 2026-10-03 |
| ml-repo | https://github.com/ml-explore/mlx-lm | L | 2026-10-03 |
| ml-server-md | https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/SERVER.md | L | 2026-10-03 |
| ml-server | https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/server.py | L | 2026-10-03 |
| ml-convert | https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/convert.py | L | 2026-10-03 |
| ml-lora | https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md | L | 2026-10-03 |
| ml-manage | https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/MANAGE.md | L | 2026-10-03 |
| ml-models | https://github.com/ml-explore/mlx-lm/tree/main/mlx_lm/models | L | 2026-10-03 |
| ml-tp | https://github.com/ml-explore/mlx-lm/tree/main/mlx_lm/tool_parsers | L | 2026-10-03 |
| ml-rel | https://github.com/ml-explore/mlx-lm/releases | L | 2026-10-03 |
| ml-pypi | https://pypi.org/project/mlx-lm/ | L | 2026-10-03 |
| ml-commits | https://github.com/ml-explore/mlx-lm/commits/main | L | 2026-10-03 |
| mx-readme | https://github.com/ml-explore/mlx | L | 2026-10-03 |
