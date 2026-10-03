---
last_checked: 2026-10-03
volatility: VOLATILE (catalogue, trial terms, container releases and feature support change often)
kind: inference host
sources:
  - https://docs.api.nvidia.com/nim/docs/product
  - https://docs.api.nvidia.com/nim/reference/llm-apis
  - https://build.nvidia.com/
  - https://docs.nvidia.com/nim/large-language-models/2.0.2/advanced-use-cases/tool-calling-and-mcp.html
  - https://docs.nvidia.com/nim/large-language-models/2.0.12/about-nim-llm/release-notes.html
  - https://docs.nvidia.com/nim/large-language-models/2.0.12/deployment/model-profiles-and-selection.html
  - https://docs.nvidia.com/nim/large-language-models/2.0.12/reference/api-reference.html
  - https://docs.nvidia.com/nim/large-language-models/2.0.12/about-nim-llm/overview.html
  - https://docs.nvidia.com/nim/large-language-models/2.0.12/ai-assistant-integrations/claude-code.html
  - https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf
---

# NVIDIA NIM

inference host

NVIDIA NIM is a family of prebuilt inference containers ("microservices"), part of NVIDIA AI Enterprise, offered in two ways. The NVIDIA API catalog at build.nvidia.com serves hosted NIM endpoints, run on DGX Cloud, for trial use. The containers can also be downloaded and run on the customer's own NVIDIA GPUs, which is the production route and needs an NVIDIA AI Enterprise licence. From release 2.0.12 the language-model containers are named NIM for Large Language Models and Vision Language Models, and come as "NIM" (fast access to new models) or "NIM Certified" (longer lifecycle, security patching, enterprise support). This file treats the hosted catalogue as an inference host and describes the self-hosted container where the two differ. [faq, catalog, ovw, notes]

## Models offered

The API catalog's front page on 2026-10-03 listed Moonshot's `kimi-k3`, DeepSeek's `deepseek-v4-pro-0813` and NVIDIA's Nemotron series (a `nemotron-3.5-lightning-30b-a3b` and a `nemotron-3-ultra-550b-a55b`). The LLM API reference lists models from more than 20 providers, including Meta Llama 2 and 3.x, Mistral models, NVIDIA's own Nemotron and NemoGuard safety models, Google Gemma, DeepSeek V4 and Qwen, with reasoning variants of some (for example `moonshotai/kimi-k2-thinking` and a Qwen3 Next thinking model); the exact count was not stated in a form that could be confirmed. Model files in scope: [Kimi K3](../models/moonshot/kimi-k3.md), [DeepSeek V4 Pro](../models/deepseek/deepseek-v4-pro.md) and [Nemotron 3 Ultra](../models/other/nemotron-3-ultra.md). Select models are also downloadable as container images with NVIDIA AI Enterprise support; release 2.0.12 added kimi-k2.6, mistral-small-4-119b-2603, a Nemotron 3 Nano Omni reasoning model and two Qwen3.5 models to the self-hosted support matrix, and a container variant for deepseek-v4-pro-0813. The catalogue changes without notice and was not enumerated here. [catalog, llm, notes]

## API surface

- **Protocol.** OpenAI-compatible chat completions at `https://integrate.api.nvidia.com/v1/chat/completions` for the hosted catalogue. A self-hosted 2.0.12 container exposes vLLM's server: `/v1/chat/completions`, `/v1/completions`, `/v1/responses`, an Anthropic-compatible `/v1/messages` with `/v1/messages/count_tokens`, `/v1/models` and tokenise endpoints, plus NIM management endpoints (health, metadata, manifest, Prometheus metrics). The product page says API conventions differ by microservice (OpenAPI for embeddings, for example). Whether the hosted catalogue also offers `/v1/messages` was not stated on the pages read. [llm, faq, apiref]
- **Auth.** For the hosted catalogue, an API key from build.nvidia.com as a bearer token (from third-party integration pages; the NVIDIA pages read did not state it). Self-hosted containers need NGC credentials to pull images; the Claude Code guide says the container does not validate the Anthropic API key. [llm, cc]
- **SDKs.** The OpenAI SDK with the base URL changed. [llm]
- **Model ids.** `maker/model-name`, for example `meta/llama-3.1-70b-instruct` or `nvidia/nemotron-3-ultra-550b-a55b`; in a container the served name follows `NIM_SERVED_MODEL_NAME` when set. [llm, apiref]
- **Self-hosted.** The 2.0 containers align directly with upstream engines; release 2.0.12 updated the backend to vLLM 0.27.1. Each container ships a manifest of profiles named `<backend>-<precision>-tp<N>-pp1[-lora]`, where the backend is `vllm`, `sglang` or `trtllm` (matching the container image) and the precision `bf16`, `fp8`, `mxfp4` or `nvfp4`. At start-up NIM picks one profile: `NIM_MODEL_PROFILE` can name it, otherwise a memory-aware selector drops profiles whose estimated VRAM exceeds the GPU and the manifest's criteria choose among the rest; `list-model-profiles` shows which fit. [notes, ovw, prof]

## Feature parity

Hosted and self-hosted NIM share an engine, but the hosted catalogue exposes what NVIDIA enables per model.

- **Reasoning and effort.** The catalogue includes thinking variants of Qwen and Moonshot models; no effort parameter or scale was found in the pages read, so a mapping is `UNVERIFIED`. Self-hosted containers accept the vLLM server's parameters. [llm, apiref]
- **Tools.** OpenAI-style `tools`. In 2.0 containers, tool calling is switched on by passing the vLLM arguments `--enable-auto-tool-choice` and `--tool-call-parser` (through `NIM_PASSTHROUGH_ARGS` on Kubernetes); without them models describe a call in text. Llama 3.1 and 3.3 use the `llama3_json` parser, and a custom parser plugin can be added. NIM does not connect to MCP servers; the client converts MCP tool definitions into OpenAI `tools`. The page warns that LangChain's `create_agent` with `ProviderStrategy` bypasses the tool loop, so the model describes calls instead of making them, and points to LangGraph's `create_react_agent`. The Claude Code guide notes that Claude Code needs a model with tool calling. [tc, cc]
- **Structured output.** The 2.0 API reference defers request parameters to the vLLM OpenAI-compatible server documentation, which was not read; structured-output support in current containers and in the hosted catalogue is `UNVERIFIED`. [apiref]
- **Prompt caching.** The 2.0.12 release notes mention vLLM prefix caching (a fix for hybrid Mamba models such as nemotron-3-ultra-550b-a55b); no cache pricing or control applies to the hosted catalogue in the pages read. [notes]
- **Batch.** Not described for the hosted catalogue. `UNVERIFIED`.
- **Responses API.** Self-hosted containers serve `/v1/responses`; the 2.0.12 notes list known output-correctness and response-format limitations on that endpoint for nemotron-3-nano. [apiref, notes]
- **Vision, long context, streaming.** From 2.0.12 the containers include vision-language models with image, audio and video input; chat completions stream; context follows the model and profile (several 2.0.12 known issues concern the default 131,072-token context not fitting in memory on smaller GPUs, worked around with `NIM_MAX_MODEL_LEN`). [notes, apiref]

## Pricing

Hosted catalogue: free access for NVIDIA Developer Program members, for prototyping, research, development and testing; members may also download and self-host NIM for those purposes on up to 16 GPUs. The trial terms say NVIDIA may give trial credits that are deducted per use; the number of credits is not stated in the pages read. Production use requires an NVIDIA AI Enterprise licence, which the product page prices from $4,500 per GPU a year, or about $1 per GPU-hour in the cloud, with a free 90-day trial licence. The 2.0 documentation has deployment guides for Google Cloud, AWS, Azure and Oracle; their terms were not read. [faq, trial, ovw]

## Limits and data

- **Rate limits.** The trial terms say use may be limited by number of API calls or by duration, at NVIDIA's discretion; no number is published in the pages read (third-party pages cite figures that were not relied on). Self-hosted throughput is bounded by the customer's hardware. [trial]
- **Retention.** The API trial terms say NVIDIA will not store or use user content or generated content at the end of each API session unless a service discloses otherwise; certain services, such as fine-tuning, keep uploaded content 30 days and generated fine-tuning content 90 days, and NVIDIA may log and store content to monitor security and prevent fraud or abuse. The terms also forbid sending confidential information, protected health information or personal data (unless a service permits it). Self-hosted NIM keeps data on the customer's infrastructure, which the product page gives as a reason to choose it. [trial, faq]
- **Training and regions.** Training use is not addressed in the passages read; regions for the hosted catalogue were not stated (it runs on DGX Cloud). [faq, trial]

## Notes for agents and harnesses

- **The hosted catalogue is a trial.** The terms exclude production use of the service and its output; serving end users needs a licensed deployment. [faq, trial]
- **Tool calling is off until enabled.** On self-hosted 2.0 containers a model that ignores tools may lack `--enable-auto-tool-choice` and a matching `--tool-call-parser`. [tc]
- **Profile choice decides precision and memory.** `NIM_MODEL_PROFILE` fixes the profile; without it NIM picks by memory and manifest, and `NIM_MAX_MODEL_LEN` lowers context when the default does not fit. [prof, notes]
- **Claude Code against a container.** The guide maps Claude Code's built-in aliases (`haiku`, `sonnet`, `opus` and the subagent model) to the served model name, because unmapped aliases produce 404 errors for Anthropic model ids. [cc]
- **OpenAI parity is per model.** The hosted endpoint is OpenAI-shaped for chat, but reasoning, effort and schema controls are model-specific and not documented in the pages read. [llm]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| faq | https://docs.api.nvidia.com/nim/docs/product | L | 2026-10-03 |
| llm | https://docs.api.nvidia.com/nim/reference/llm-apis | L | 2026-10-03 |
| catalog | https://build.nvidia.com/ | L | 2026-10-03 |
| tc | https://docs.nvidia.com/nim/large-language-models/2.0.2/advanced-use-cases/tool-calling-and-mcp.html | L | 2026-10-03 |
| notes | https://docs.nvidia.com/nim/large-language-models/2.0.12/about-nim-llm/release-notes.html | L | 2026-10-03 |
| prof | https://docs.nvidia.com/nim/large-language-models/2.0.12/deployment/model-profiles-and-selection.html | L | 2026-10-03 |
| apiref | https://docs.nvidia.com/nim/large-language-models/2.0.12/reference/api-reference.html | L | 2026-10-03 |
| ovw | https://docs.nvidia.com/nim/large-language-models/2.0.12/about-nim-llm/overview.html | L | 2026-10-03 |
| cc | https://docs.nvidia.com/nim/large-language-models/2.0.12/ai-assistant-integrations/claude-code.html | L | 2026-10-03 |
| trial | https://assets.ngc.nvidia.com/products/api-catalog/legal/NVIDIA%20API%20Trial%20Terms%20of%20Service.pdf | L | 2026-10-03 |
