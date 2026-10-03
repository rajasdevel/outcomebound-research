---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: local runtime
sources:
  - https://docs.vllm.ai/
  - https://github.com/vllm-project/vllm
  - https://github.com/vllm-project/vllm/releases
  - https://github.com/vllm-project/vllm/blob/main/docs/README.md
  - https://github.com/vllm-project/vllm/blob/main/docs/serving/online_serving/README.md
  - https://github.com/vllm-project/vllm/blob/main/docs/serving/online_serving/openai_compatible_server.md
  - https://github.com/vllm-project/vllm/blob/main/docs/features/tool_calling.md
  - https://github.com/vllm-project/vllm/blob/main/docs/features/reasoning_outputs.md
  - https://github.com/vllm-project/vllm/blob/main/docs/features/structured_outputs.md
  - https://github.com/vllm-project/vllm/blob/main/docs/features/automatic_prefix_caching.md
  - https://github.com/vllm-project/vllm/blob/main/docs/features/quantization/README.md
  - https://github.com/vllm-project/vllm/blob/main/docs/features/speculative_decoding/README.md
  - https://github.com/vllm-project/vllm/blob/main/docs/getting_started/installation/README.md
  - https://github.com/vllm-project/vllm/blob/main/docs/getting_started/installation/gpu.md
  - https://github.com/vllm-project/vllm/blob/main/docs/getting_started/installation/gpu.cuda.inc.md
  - https://github.com/vllm-project/vllm/blob/main/docs/models/supported_models.md
  - https://github.com/vllm-project/vllm/blob/main/docs/usage/security.md
  - https://github.com/vllm-project/vllm/blob/main/docs/usage/usage_stats.md
  - https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/chat_completion/protocol.py
  - https://github.com/vllm-project/vllm/blob/main/vllm/config/cache.py
  - https://github.com/vllm-project/vllm/blob/main/vllm/config/model.py
  - https://github.com/vllm-project/vllm/blob/main/vllm/engine/arg_utils.py
  - https://github.com/vllm-project/vllm/blob/main/docs/features/context_extension.md
---

# vLLM

local runtime

vLLM is an Apache-2.0 Python library and server for running open-weight models at high throughput on GPUs and other accelerators. It began in UC Berkeley's Sky Computing Lab and is now maintained by a community that its documentation puts at more than 2,000 contributors. It is aimed at serving many concurrent requests from one deployment, from a single GPU to multi-node clusters, rather than at a desktop chat window: it batches requests continuously, manages the attention cache in pages, and caches shared prompt prefixes. `vllm serve <model>` starts an HTTP server with OpenAI-compatible and Anthropic-compatible endpoints. On 2026-10-03 the latest release is v0.30.0 (2026-09-22), and minor releases have arrived about every two weeks (v0.25.0 on 2026-07-11 to v0.30.0 on 2026-09-22). [vl-readme, vl-rel, vl-repo]

## Models offered

vLLM runs models from Hugging Face or a local directory by the repository id, for more than 200 architectures: decoder-only and mixture-of-experts text models, hybrid attention and state-space models, multimodal models, and embedding, reward and classification models. The supported-models page lists architecture classes with example repositories; the release notes name the models added each time. [vl-readme, vl-models, vl-rel]

Models in this library that vLLM's pages or release notes name:

| Model file | What the vLLM sources say |
| --- | --- |
| [Gemma 4](../models/google/gemma-4-26b-a4b-it.md) ([31B](../models/google/gemma-4-31b-it.md), [E2B](../models/google/gemma-4-e2b-it.md) and others) | `Gemma4ForCausalLM` and two multimodal Gemma 4 classes are in the supported list, and a `gemma4` reasoning parser exists; reasoning is off unless `enable_thinking` or `reasoning_effort` is set |
| [gpt-oss 20B](../models/openai/gpt-oss-20b.md) and [120B](../models/openai/gpt-oss-120b.md) | `GptOssForCausalLM` is supported; tool parser `openai` |
| [Kimi K3](../models/moonshot/kimi-k3.md) | `KimiK3ForConditionalGeneration` is in the supported list; v0.27.0 (2026-08-10) added the model, v0.28.0 and v0.30.0 list performance work, and v0.29.0 added NVFP4 checkpoints; the documented tool parser `kimi_k2` is for Kimi K2 |
| [GLM-5.3-Flash](../models/zai/glm-5.3-flash.md), [GLM-5.2](../models/zai/glm-5.2.md) | v0.30.0 added GLM-5.3-Flash; `GlmMoeDsaForCausalLM` covers GLM-5 to 5.2; tool parser `glm47` |
| [DeepSeek V4.1-Flash](../models/deepseek/deepseek-flash.md), [DeepSeek V4-Pro](../models/deepseek/deepseek-v4-pro.md) | `DeepseekV4ForCausalLM` is supported; v0.30.0 added V4.1-Flash, with a KV cache stored in MXFP8 on one GPU generation |
| [MiniMax M3](../models/minimax/MiniMax-M3.md) | `MiniMaxM3SparseForCausalLM` is in the supported list |
| [Mistral Large 3](../models/mistral/mistral-large-3.md) | `MistralLarge3ForCausalLM` is supported |
| [Qwen3.8 27B](../models/alibaba/qwen3.8-27b.md) | its file lists vLLM as an access route; the supported-models page names Qwen3.5 classes, not Qwen3.8 |
| [Qwen3.8-Flash-Next](../models/alibaba/qwen3.8-flash-next.md) | v0.29.0 added it (BF16, FP8, NVFP4, MTP); v0.30.0 lists performance work |
| [Hy4-Preview](../models/other/hy4-preview.md) | v0.29.0 added it; `HYV4ForCausalLM` is in the supported list |
| [K2-Horizon](../models/other/k2-horizon-375b-a23b.md) | v0.30.0 added support |
| [Muse Glimmer 30B](../models/meta/muse-glimmer-30b.md) | `MuseGlimmerForCausalLM` and `MuseGlimmerForConditionalGeneration` are in the supported list (text, image and video input) |

[vl-rel, vl-models, vl-reason, vl-tools]

vLLM hosts no models itself and offers no hosted service. [vl-readme]

## API surface

- **OpenAI-compatible routes.** `/v1/completions` (no `suffix`), `/v1/chat/completions` (`user` is ignored, `image_url.detail` is not supported), a batch variant `/v1/chat/completions/batch`, `/v1/responses` (with `GET` and cancel by id), `/v1/embeddings`, and audio transcription and translation routes for speech models. Each text route applies only to text-generation models with a chat template. [vl-oai]
- **Other protocols.** Anthropic Messages at `/v1/messages` and `/v1/messages/count_tokens`; Cohere-compatible embed and rerank routes; pooling routes (`/classify`, `/score`, `/rerank`); and an optional gRPC interface on a separate port, which the security page calls insecure by default. [vl-serve, vl-sec]
- **Extra parameters.** vLLM-specific fields go in the request body (the OpenAI SDK's `extra_body`): `structured_outputs`, `chat_template_kwargs`, `priority` (also the `X-Vllm-Priority` header, needing priority scheduling), `include_reasoning` and `thinking_token_budget` among them. `X-Request-Id` is echoed when `--enable-request-id-headers` is set. [vl-oai, vl-proto]
- **Auth.** `--api-key` (or `VLLM_API_KEY`) is a bearer key, but the docs warn that it protects only the `/v1`, `/v2`, `/inference` and `/cohere` prefixes, and that other routes on the same server, notably `/invocations`, are not protected and expose the same inference capability. Deployments are told to put a reverse proxy in front. Node-to-node traffic in multi-node serving is unencrypted and unauthenticated, to be isolated by network design. [vl-oai, vl-sec]
- **SDKs.** A Python library with an offline `LLM` class and the server; no client SDK beyond the OpenAI and Anthropic SDKs pointed at the server. [vl-readme]
- **Model ids.** The Hugging Face repository id, or the name set with `--served-model-name`. [vl-oai, vl-args]
- **Startup flags that matter.** `--max-model-len`, `--gpu-memory-utilization` (default 0.92), `--tensor-parallel-size`, `--max-num-seqs`, `--max-num-batched-tokens`, `--kv-cache-dtype`, `--enable-auto-tool-choice`, `--tool-call-parser`, `--reasoning-parser` and `--generation-config`. [vl-args, vl-cache]

## Feature parity

Parity is against the makers' APIs and the OpenAI and Anthropic APIs that vLLM imitates. [vl-oai, vl-tools]

| Feature | What the docs and source say |
| --- | --- |
| Reasoning control | `reasoning_effort` accepts `none`, `minimal`, `low`, `medium`, `high`, `xhigh` and `max` (the source notes `max` is specific to the DeepSeek V4 series). When it is set, the server also sets `enable_thinking` to false for `none` and true for anything else, unless the request already supplies `enable_thinking`. `thinking_token_budget` caps reasoning tokens. A reasoning parser (named per model family) splits reasoning into a `reasoning` field. |
| Tools | `tool_choice` `auto` (needs `--enable-auto-tool-choice` and a `--tool-call-parser`), `required`, `none` and named functions; `required` and named calls use structured decoding, so the call parses but its quality is not guaranteed. With `none`, tool definitions stay in the prompt unless `--exclude-tools-when-tool-choice-none` is set. A `strict` flag on tools and a server-side strictness floor control schema enforcement under `auto`. `parallel_tool_calls` defaults to true, and parallel calls depend on the model. |
| Structured output | `structured_outputs` with `json`, `regex`, `choice`, `grammar` or `structural_tag`; `response_format` with a JSON schema; backends xgrammar or llguidance (`auto` by default). |
| Vision, audio, video | multimodal inputs for supported models; speech-to-text routes. |
| Prompt caching | automatic prefix caching, on by default in the configuration source; there are no explicit cache markers. The caching page says it shortens prompt processing only, not token generation. |
| Batch | `/v1/chat/completions/batch` on the server and offline batching in the library; a file-based batch service is not described on the pages read. |
| Long context | whatever the model supports up to `--max-model-len`; context extension through `--hf-overrides` with `rope_parameters` (the older `--rope-scaling` flag is gone). |
| Streaming | server-sent events; per-request metrics are documented. |
| Speculative decoding | EAGLE, multi-token prediction, draft models, parallel draft models, n-gram, suffix decoding and others; v0.29.0 added per-request acceptance statistics in API responses. |

Differences worth knowing. The reasoning output field is `reasoning`, renamed from `reasoning_content`; the docs warn that a client still reading the old name silently sees nothing. Older guided-decoding fields (`guided_json` and others) were removed in v0.12.0 in favour of `structured_outputs`. [vl-reason, vl-struct, vl-proto, vl-tools, vl-prefix, vl-ctx, vl-spec]

## Pricing

Free, open-source software; no charge, no plans and no cloud. The cost is hardware and operation. Hosted services that run vLLM (cloud and inference hosts) set their own prices and are covered in their own files. [vl-readme]

## Limits and data

- **Rate limits.** None from the software. Capacity is set by `--max-num-seqs`, `--max-num-batched-tokens` and available KV memory; requests beyond that wait in the scheduler, and priority scheduling can reorder them. [vl-args, vl-oai]
- **Regions.** Wherever the machine runs. [vl-readme]
- **Retention and training.** Prompts stay in the operator's deployment. vLLM does collect anonymous usage statistics by default; the page's example record, dated "as of v0.4.0", holds a random id, cloud provider, CPU and GPU type and counts, memory, model architecture name, vLLM version and configuration such as dtype and parallelism, and no prompt text, and the page says the data holds nothing sensitive and points to the source file for the current list. A subset is published in aggregate, and `~/.config/vllm/usage_stats.json` shows what was collected. Opt out with `VLLM_NO_USAGE_STATS=1`, `DO_NOT_TRACK=1`, or a file at `~/.config/vllm/do_not_track`. [vl-stats]
- **Hardware.** Linux only (Windows through WSL or community forks); Python 3.10 to 3.13. NVIDIA GPUs of compute capability 7.5 or higher (the install page says the default binaries use CUDA 12.9, with 12.8 and 13.0 builds also offered, while the v0.30.0 release notes list the PyPI wheel as CUDA 13.0), AMD ROCm, Intel XPU, x86, Arm, PowerPC and IBM Z CPUs, and Apple silicon through a separate vllm-metal plugin. Hardware plugins add TPUs, Gaudi, Ascend and others. Parallelism covers tensor, pipeline, data, expert and context parallel modes. [vl-install, vl-gpu, vl-cuda, vl-readme]
- **Formats and quantisation.** Hugging Face checkpoints, and GGUF appears in the quantisation support table (its own page was not read). Quantisation formats listed: FP8, MXFP8, MXFP4, NVFP4, INT8, INT4, GPTQ, AWQ, bitsandbytes (moved to an out-of-tree plugin in v0.28.0), compressed-tensors, NVIDIA Model Optimizer, TorchAO, AMD Quark and others, a quantised KV cache, online quantisation, and LLM Compressor for making checkpoints. [vl-quant, vl-readme, vl-rel]

## Notes for agents and harnesses

- **Tool calling is opt-in per model.** The page's `auto` mode needs `--enable-auto-tool-choice` and a matching `--tool-call-parser`, and several families also need a chat template file from the examples directory. With `auto`, the call is generated without a grammar unless a tool sets `strict: true` or the server sets `--tool-strict-level function` or `parameter`, which the page offers because most clients never set `strict`. The tool-calling page lists parsers per family, including `hermes` (also for Qwen), `mistral`, `llama3_json`, `deepseek_v3` and `deepseek_v31`, `openai` (gpt-oss), `kimi_k2`, `glm45` and `glm47`, `qwen3_xml`, `granite`, `internlm` and `cohere_command4`. For DeepSeek-V3.1, tool calling works in non-thinking mode. [vl-tools, vl-reason]
- **Forced tool choice is guaranteed to parse, not to be good.** Named and `required` calls are generated under a grammar; the docs advise stating the schema in the prompt as well, and note that the first use compiles the grammar and can take several seconds. [vl-tools]
- **Reasoning is a server flag plus a request flag.** A `--reasoning-parser` must be set for the `reasoning` field to appear; whether thinking is on by default differs by model (Gemma 4, Granite 3.2 and DeepSeek-V3.1 default off; Qwen3, Granite 4.2 and Holo2 default on), and `chat_template_kwargs` (`enable_thinking` or `thinking`) switches it. [vl-reason]
- **Sampling defaults come from the model.** `--generation-config auto` (the default) loads the generation config from the model path, so the sampling values a maker ships apply when a request omits them; `--generation-config vllm` uses vLLM's own defaults instead. A `max_new_tokens` value in a loaded generation config becomes a server-wide output cap. Results compared with a maker's own API therefore depend on which setting is in force. [vl-model]
- **Memory sizing.** `--gpu-memory-utilization` is a per-instance fraction (0.92 by default; two instances on one GPU each need their own share). `--max-model-len` defaults to the model's configured length; `-1` or `auto` picks the model's maximum if it fits in GPU memory and otherwise the largest length that does. [vl-cache, vl-model]
- **`--api-key` covers only some routes.** Because `--api-key` leaves some routes open (the security page names `/invocations`, `/pooling`, `/classify`, `/score` and `/rerank` among them), the documented recommendation is a reverse proxy that blocks every other route. Multi-node and gRPC traffic are not encrypted. [vl-sec]
- **Prefix caching and agent loops.** With caching on by default, a request that shares a prefix with an earlier one reuses its computed state; the caching page names long-document queries and multi-turn chat as the workloads that gain. Because reuse stops at the first differing token, text that changes early in a prompt, such as a timestamp, shortens the shared part. [vl-prefix, vl-cache]
- **Docs track the development branch.** The pages read are the `main` branch of the documentation, which the live site (`docs.vllm.ai`) labels a developer preview; a flag or default described there may not be in the v0.30.0 release. [vl-docs]
- **Version drift.** Each release adds several models and changes defaults (v0.28.0 raised `max_num_batched_tokens` from 8192 to 16384; v0.29.0 made Model Runner V2 the default for all models) and lists breaking changes. A test that depends on parser behaviour is only reproducible against a pinned release. [vl-rel]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| vl-docs | https://docs.vllm.ai/ | L | 2026-10-03 |
| vl-repo | https://github.com/vllm-project/vllm | L | 2026-10-03 |
| vl-rel | https://github.com/vllm-project/vllm/releases | L | 2026-10-03 |
| vl-readme | https://github.com/vllm-project/vllm/blob/main/docs/README.md | L | 2026-10-03 |
| vl-serve | https://github.com/vllm-project/vllm/blob/main/docs/serving/online_serving/README.md | L | 2026-10-03 |
| vl-oai | https://github.com/vllm-project/vllm/blob/main/docs/serving/online_serving/openai_compatible_server.md | L | 2026-10-03 |
| vl-tools | https://github.com/vllm-project/vllm/blob/main/docs/features/tool_calling.md | L | 2026-10-03 |
| vl-reason | https://github.com/vllm-project/vllm/blob/main/docs/features/reasoning_outputs.md | L | 2026-10-03 |
| vl-struct | https://github.com/vllm-project/vllm/blob/main/docs/features/structured_outputs.md | L | 2026-10-03 |
| vl-prefix | https://github.com/vllm-project/vllm/blob/main/docs/features/automatic_prefix_caching.md | L | 2026-10-03 |
| vl-quant | https://github.com/vllm-project/vllm/blob/main/docs/features/quantization/README.md | L | 2026-10-03 |
| vl-spec | https://github.com/vllm-project/vllm/blob/main/docs/features/speculative_decoding/README.md | L | 2026-10-03 |
| vl-install | https://github.com/vllm-project/vllm/blob/main/docs/getting_started/installation/README.md | L | 2026-10-03 |
| vl-gpu | https://github.com/vllm-project/vllm/blob/main/docs/getting_started/installation/gpu.md | L | 2026-10-03 |
| vl-cuda | https://github.com/vllm-project/vllm/blob/main/docs/getting_started/installation/gpu.cuda.inc.md | L | 2026-10-03 |
| vl-models | https://github.com/vllm-project/vllm/blob/main/docs/models/supported_models.md | L | 2026-10-03 |
| vl-sec | https://github.com/vllm-project/vllm/blob/main/docs/usage/security.md | L | 2026-10-03 |
| vl-stats | https://github.com/vllm-project/vllm/blob/main/docs/usage/usage_stats.md | L | 2026-10-03 |
| vl-proto | https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/chat_completion/protocol.py | L | 2026-10-03 |
| vl-cache | https://github.com/vllm-project/vllm/blob/main/vllm/config/cache.py | L | 2026-10-03 |
| vl-model | https://github.com/vllm-project/vllm/blob/main/vllm/config/model.py | L | 2026-10-03 |
| vl-args | https://github.com/vllm-project/vllm/blob/main/vllm/engine/arg_utils.py | L | 2026-10-03 |
| vl-ctx | https://github.com/vllm-project/vllm/blob/main/docs/features/context_extension.md | L | 2026-10-03 |
