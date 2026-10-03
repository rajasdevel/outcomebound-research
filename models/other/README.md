---
last_checked: 2026-10-03
volatility: MONITOR (lineage, guides and API behaviour change at each release)
sources:
  - https://huggingface.co/tencent/Hy4-preview
  - https://huggingface.co/tencent/Hy3/raw/main/README.md
  - https://huggingface.co/tencent/Hy3-preview/raw/main/README.md
  - https://rits.shanghai.nyu.edu/ai/tencent-releases-hy3-295b-open-moe-model-under-apache-2-0/
  - https://technode.com/2026/08/28/tencent-open-sources-hy4-preview-with-770b-parameters-and-a-1m-token-context/
  - https://www.orcarouter.ai/blog/tencent-hy4-preview-vllm-day-zero
  - https://thinkingmachines.ai/inkling/
  - https://thinkingmachines.ai/model-card/inkling/
  - https://thinkingmachines.ai/model-card/inkling-small/
  - https://huggingface.co/thinkingmachines/Inkling
  - https://huggingface.co/thinkingmachines/Inkling-Small
  - https://huggingface.co/blog/thinkingmachines-inkling
  - https://analyticsvidhya.com/blog/2026/07/thinking-machines-inkling
  - https://tinker-docs.thinkingmachines.ai/cookbook/inkling/
  - https://tinker-docs.thinkingmachines.ai/cookbook/inkling/thinking-effort/
  - https://tinker-docs.thinkingmachines.ai/tinker/models/models_and_pricing/
  - https://huggingface.co/IFM/K2-Horizon-375B-A23B
  - https://huggingface.co/IFM
  - https://rits.shanghai.nyu.edu/ai/ifm-releases-k2-horizon-six-open-models/
  - https://kyodonewsprwire.jp/release/202601283158
  - https://www.tbench.ai/news/leaderboard-integrity-update
  - https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL
  - https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL
  - https://mimo.mi.com/models/en-US/mimo-v2.6-pro
  - https://mimo.mi.com/models/en-US/mimo-v2.6-flash
  - https://mimo.mi.com/docs/en-US/quick-start/summary/model
  - https://mimo.mi.com/docs/en-US/quick-start/usage-guide/text-generation/deep-thinking
  - https://mimo.mi.com/docs/zh-CN/quick-start/usage-guide/text-generation/deep-thinking
  - https://mimo.mi.com/docs/zh-CN/quick-start/summary/first-api-call
  - https://mimo.mi.com/docs/en-US/quick-start/usage-guide/text-generation/structured-output
  - https://mimo.mi.com/docs/en-US/quick-start/usage-guide/multimodal-understanding/image-understanding
  - https://mimo.mi.com/docs/en-US/quick-start/usage-guide/multimodal-understanding/audio-understanding
  - https://mimo.mi.com/docs/en-US/quick-start/usage-guide/multimodal-understanding/video-understanding
  - https://docs.litellm.ai/blog/mimo_v2_6
  - https://help.aliyun.com/en/model-studio/mimo
  - https://datanorth.ai/news/xiaomi-releases-mimo-v2-6-pro-and-flash
  - https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/
  - https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16
  - https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf
  - https://catalog.ngc.nvidia.com/orgs/nim/nvidia/models/nemotron-3-ultra-550b-a55b/-/model-card/explainability
  - https://docs.dynamo.nvidia.com/dynamo/dev/recipes/nemotron-3-ultra.md
  - https://artificialanalysis.ai/models/open-source
  - https://artificialanalysis.ai/models/mimo-v2-6-pro
  - https://artificialanalysis.ai/models/mimo-v2-6-flash
  - https://artificialanalysis.ai/models/k2-horizon-375b-a23b
  - https://artificialanalysis.ai/models/inkling
  - https://artificialanalysis.ai/models/inkling-small
  - https://artificialanalysis.ai/models/nvidia-nemotron-3-ultra-550b-a55b
  - https://labs.scale.com/leaderboard/swe_bench_pro_public_v2
  - https://metr.org/time-horizons/
  - https://cloudprice.net/models/tencent/hy4-preview
  - https://www.orcarouter.ai/blog/tencent-hy4-preview-open-source
  - https://the-decoder.com/ex-openai-cto-muratis-thinking-machines-drops-inkling-a-975b-parameter-model-that-leads-us-labs-but-trails-china/
  - https://developers.cloudflare.com/ai/models/thinkingmachines/inkling/
  - https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/MiMo_V2_6_technical_report.pdf
  - https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16/raw/main/README.md
  - https://artificialanalysis.ai/agents/coding-agents
  - https://huggingface.co/nvidia/personaplex-7b-v1
  - https://github.com/NVIDIA/personaplex
  - https://huggingface.co/nvidia/NVIDIA-NemotronLabs-VoiceChat-11B
  - https://artificialanalysis.ai/speech-to-speech
---

# Models from other makers

This folder holds the models of five makers that have no folder of their own: Tencent (Hy), Thinking Machines Lab (Inkling), the Institute of Foundation Models at MBZUAI (K2 Horizon), Xiaomi (MiMo) and
NVIDIA (Nemotron and its speech models). All ten models are open-weight. None of the makers publishes a family-wide prompting guide, so the detail sits in the model files; this page gives each
maker's lineage, the API and guide facts that hold across its models, and what its documents do and do not report. Everything was read on 2026-10-03.

## Models and lineage

**Models in scope** (one file each in this folder):

| Maker | Class | Generation | Model | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| Tencent | Tencent Hy | 3 | [Hy3](hy3.md) | GA, open weights | 295B total, 21B active, 256K context, text only; the generation before Hy4 |
| Tencent | Tencent Hy | 4 | [Hy4 preview](hy4-preview.md) | preview, open weights | 770B total, 49B active, 1M context, text only; follows Hy3 |
| Thinking Machines Lab | Inkling | none numbered | [Inkling](inkling.md) | GA, open weights | 975B total, 41B active; text, image and audio in |
| Thinking Machines Lab | Inkling | none numbered | [Inkling-Small](inkling-small.md) | GA, open weights | 276B total, 12B active; same inputs |
| Institute of Foundation Models (MBZUAI) | K2 Horizon | none numbered | [K2 Horizon 375B-A23B](k2-horizon-375b-a23b.md) | GA, open weights | 512K context, text only; fully open data and code |
| Xiaomi | MiMo Pro | 2.6 | [MiMo-V2.6-Pro](mimo-v2.6-pro.md) | GA, open weights | 1.02T total, 42B active; text, image, video and audio in |
| Xiaomi | MiMo Flash | 2.6 | [MiMo-V2.6-Flash](mimo-v2.6-flash.md) | GA, open weights | 309B total, 15B active |
| NVIDIA | Nemotron Ultra | 3 | [Nemotron 3 Ultra](nemotron-3-ultra.md) | GA, open weights | 550B total, 55B active, hybrid Mamba and attention |
| NVIDIA | PersonaPlex | 1 | [PersonaPlex-7B-v1](personaplex-7b-v1.md) | GA, open weights (gated) | full-duplex speech-to-speech, 7B, built on Kyutai's Moshiko weights; text and voice prompts [nvidia-card-personaplex] |
| NVIDIA | Nemotron VoiceChat | 1 | [NemotronLabs VoiceChat 11B](nemotron-voicechat-11b.md) | GA, open weights | full-duplex speech-to-speech with tool calling, 11B, hybrid Mamba and Transformer [nvidia-card-voicechat] |

**Without a file** (seen on the sources read; no file was created here): Tencent Hy3-preview (2026-04-23, older than the two generations in scope); the other K2 Horizon sizes (0.9B, 3.7B, 7B, 32B, 36B-A4B);
Xiaomi's MiMo-V2.5-Pro and MiMo-V2.5, the previous generation, which Xiaomi's API retires on 2026-10-21 (inside the three-week window, so they are let lapse); the Xiaomi model id `mimo-v2.6-pro-ultraspeed`, a faster Pro; Nemotron 3 Super and Nano. Kyutai's gated `personaplex-rl-seamless` fine-tune is listed in the [Kyutai README](../kyutai/README.md).

**How each line got here** (dates are those on the sources named):

- **Tencent.** Hy3-preview was released on 2026-04-23 as a 295B model with 21B active, 256K context and the maker's community licence, with direct answers as the default [hf-hy3-preview]. Hy3 replaced it on 2026-07-06 under Apache-2.0; Tencent's
  Hy3 card says hallucination on an internal test fell from 12.5% to 5.4% and the multi-turn issue rate from 17.4% to 7.9% [nyu-hy3] [hf-hy3]. Hy4 preview followed on 2026-08-28 with 770B total, 49B active, 1M context and thinking as the default [hf-hy4].
- **Thinking Machines Lab.** Inkling is the lab's first model (2026-07-15); Inkling-Small was previewed alongside it and its model card dates its release 2026-07-30 [tml-model-card] [tml-model-card-small] [the-decoder-inkling]. The lab numbers no generation.
- **IFM (MBZUAI).** The K2 line began with open foundation models and reasoning systems: K2-V2, a foundation model of late 2025 (not read on a page), and the 70B reasoning system K2 Think V2 built on it, released on 2026-01-28 [kyodo-k2-think]. K2 Horizon followed on 2026-09-03 as six Apache-2.0 models from
  0.9B to 375B with data, code, logs and intermediate checkpoints [mbzuai-k2-nyu].
- **Xiaomi.** MiMo-V2-Pro (2026-03-18) and MiMo-V2.5-Pro (2026-04-22, with MiMo-V2.5) came before MiMo-V2.6, released on 2026-09-21; the V2.5 models are deprecated on Xiaomi's API at 10:00 Beijing time on 2026-10-21 [mimo-docs-models] [datanorth-mimo]. The two earlier dates are the release dates in Artificial Analysis's model list, which marks both models deprecated [aa-coding-agents].
- **NVIDIA.** The Nemotron 3 family has Nano, Super (2026-03-11) and Ultra (2026-06-04); NVIDIA's Ultra launch post says Nemotron releases are moving to the OpenMDW-1.1 licence [hf-nemotron-super] [hf-nemotron] [nvidia-nemotron-blog]. An Ultra-class model of an earlier family generation, if it exists, has no file here. NVIDIA's speech line is separate: PersonaPlex-7B-v1 (2026-01-15) is a fine-tune of Kyutai's Moshiko weights with text and voice prompts, and NemotronLabs VoiceChat 11B (2026-08-03) is a new hybrid Mamba and Transformer model that adds tool calling and lists PersonaPlex data among its training data [nvidia-card-personaplex] [nvidia-card-voicechat].

## API surface

There is no shared protocol; each maker serves differently.

- **Tencent.** Hy4 preview is served by Tencent Cloud's TokenHub, the CodeBuddy and WorkBuddy products, and aggregators (OpenRouter, Aihubmix, Vercel AI Gateway), and self-hosted through vLLM and SGLang with parsers named `hy_v4` and `auto`. The reasoning setting is `reasoning_effort` inside
  `chat_template_kwargs`, `high` (default) or `no_think` [hf-hy4] [tencent-hy4-news] [cloudprice-hy4]. Price: TechNode relays 0.834 in and 2.501 out per million tokens, and OrcaRouter relays
  Tencent's yuan list as 6 in, 18 out and 0.3 on cache hits; an aggregator lists 0.042 for cached input [tencent-hy4-news] [orcarouter-hy4] [cloudprice-hy4].
- **Thinking Machines Lab.** The lab's own route is the Tinker API, a fine-tuning and sampling service documented at tinker-docs.thinkingmachines.ai, with the `tml-renderers` package turning OpenAI-style or typed messages into model tokens; the weights are also on Hugging Face and hosted by
  Together AI, Fireworks, Modal, Databricks and Baseten (per a launch write-up) [av-inkling]. Tinker sells a 64K and a 256K context option for both models for fine-tuning and sampling, and runs a
  serverless inference beta for both (256K, NVFP4: Inkling 1.00 in and 4.05 out, Inkling-Small 0.30 and 1.20 per million tokens) [tinker-pricing] [tinker-using-inkling]. Cloudflare lists Inkling through
  Tinker's beta Anthropic Messages-compatible endpoint at 64K [cloudflare-inkling]. Effort is a float from 0.0 up to, not including, 1.0 (named presets in the Inkling file).
- **IFM (MBZUAI).** Open weights on Hugging Face with vLLM, SGLang and Transformers recipes; the maker's pages name hosted partners that the fetcher could not confirm. Effort `low`, `medium` or `high` goes in `chat_template_kwargs` [hf-k2-horizon].
- **Xiaomi.** A first-party API on the MiMo platform, in two protocols: OpenAI Chat Completions at `https://api.xiaomimimo.com/v1` and Anthropic Messages at `https://api.xiaomimimo.com/anthropic`; a separate batch endpoint; token plans on their own hosts; the key goes in an `api-key` header, with prefixes `sk-` for
  pay-as-you-go and `tp-` and `ttp-` for personal and team plans [mimo-docs-first-call]. Model ids `mimo-v2.6-pro`, `mimo-v2.6-flash`, `mimo-v2.6-pro-ultraspeed`; all three have 1M context and 128K output, and the Pro and Flash a rate limit of 100 requests and 10M tokens per
  minute, while the ultraspeed model is offered as a customised service [mimo-docs-models].
  Weights are also on Hugging Face; OpenRouter lists the models, and LiteLLM supports them as an OpenAI-compatible provider [litellm-mimo].
- **NVIDIA.** build.nvidia.com, the NIM microservice, AWS SageMaker JumpStart, Google Cloud, Microsoft Foundry, Oracle Cloud, OpenRouter, Together AI, Fireworks, DeepInfra, Baseten, Ollama cloud, Tinker and others, plus vLLM, SGLang and TensorRT-LLM self-hosting, with an NVFP4 checkpoint that NVIDIA says runs on
  Hopper, Blackwell and Ampere GPUs [nvidia-nemotron-blog] [hf-nemotron] [tinker-pricing]. The two speech models have no hosted API in the sources read: PersonaPlex runs from the `NVIDIA/personaplex` repository (PyTorch, gated weights on Hugging Face), and VoiceChat runs from its Hugging Face checkpoint or from an NVIDIA inference container with a WebSocket interface (Triton and vLLM) [nvidia-gh-personaplex] [nvidia-card-voicechat].

## Prompting guides

None of the five makers publishes a guide on system prompts, roles, structure, examples or output control for its model. What exists:

| Maker | What is published | What it covers |
| --- | --- | --- |
| Tencent | the Hugging Face cards of Hy4 preview, Hy3 and Hy3-preview | reasoning switch, sampling (0.9 and 1.0), parsers, serving |
| Thinking Machines Lab | Tinker cookbook pages (using Inkling, renderers, thinking effort, images, audio) and a Hugging Face launch post | effort scale, message rendering, media inputs, a note that question wording changes reasoning length |
| IFM | the "Best Practices" section of the card | effort `high`, sampling, tool-call formats, parsers |
| Xiaomi | the Hugging Face cards, the MiMo docs (deep thinking, structured output, image, audio, video) and the V2.6 technical report | thinking switch, fixed sampling, reasoning-content rule, JSON mode, media limits; the report covers training harnesses and reward-hacking safeguards |
| NVIDIA | the Hugging Face card (Quick Start, budget-controlled reasoning) and the Dynamo serving recipe; for the speech models, the PersonaPlex repository README and the VoiceChat card | three reasoning modes, budget, tool-call parser, known serving defects; for PersonaPlex, prompt patterns for three kinds of role; for VoiceChat, a rendered system prompt with a tool-use decision process and an ASCII-only rule |

How the advice has moved: Tencent's default flipped from direct answers (Hy3) to thinking (Hy4 preview) [hf-hy3] [hf-hy4]; Xiaomi's docs treat V2.5 and V2.6 alike (thinking on by default, sampling fixed while thinking is on) [mimo-docs-thinking]; the others have a single release.
Nothing in this folder compares guides across releases beyond that.

## System-card practice

No maker here publishes a system card with measured refusal, injection, sycophancy or sabotage results of the kind the large closed labs publish. What each does publish:

- **Thinking Machines Lab** a model card for each model, with a safety section in words (the evaluation areas, a residual risk of role-play compliance, a recommendation to layer a moderation model) and three numbers (StrongREJECT, FORTRESS adversarial and benign) [tml-model-card] [tml-model-card-small].
- **NVIDIA** a Hugging Face model card, NGC safety and explainability subcards (training-data screening, an instruction-following-versus-injection caveat), and a technical report; no refusal or injection numbers [ngc-nemotron-explain] [nvidia-tech-report]. The two speech models have a Hugging Face card with an ethics paragraph that points to subcards, plus a paper; neither gives a refusal result [nvidia-card-personaplex] [nvidia-card-voicechat].
- **Tencent, IFM and Xiaomi** a Hugging Face model card with benchmarks and serving settings; Tencent adds a known-limitations paragraph, and Xiaomi a 44-page technical report whose
  reward-hacking section reports a confirmed-hack share below 2% during RL. No refusal, jailbreak or injection evaluation in any [hf-hy4] [hf-k2-horizon] [hf-mimo-pro] [mimo-tech-report].

How to read the benchmark tables the makers publish: comparison models are usually the maker's own runs; settings, harnesses and turn limits are in footnotes (Tencent's appendix is the fullest, naming harness, turn budget and timeout per benchmark); two makers have corrected their own scores (IFM lowered Terminal-Bench 2.1 from 70.2 to 66.9 after a
reward-hacking audit; Tencent restated some Hy3 numbers after harness and anti-hacking changes) [mbzuai-k2-nyu] [hf-hy4-page]. Terminal-Bench's own notice says its leaderboard now runs an agent judge over passing trials and zeroes trials judged to be reward hacking [tbench-integrity].

## Family-wide behaviour

- **Reasoning controls.** Hy4 preview, Xiaomi's V2.6 pair and Nemotron 3 Ultra document thinking as the default, and Inkling does at Tinker's default (K2 Horizon's card states no default); the controls differ: a two-value switch (Hy4 `reasoning_effort`, Xiaomi `thinking.type`), a float (Inkling), three named levels (K2 Horizon) or three modes with a budget (Nemotron).
- **Xiaomi (both models).** While thinking is on, the API ignores custom `temperature` and `top_p` (fixed at 1.0 and 0.95). With thinking on and tool calls in the history, each assistant message with tool calls must carry its full `reasoning_content` or the call fails with a 400. `max_completion_tokens` caps thinking and answer together. JSON mode is
  `json_object`, which guarantees syntax only. Media: image URL or base64 up to 50 MB (JPEG, PNG, GIF, WebP, BMP); video with `fps` 0.1 to 10 (default 2) and `media_resolution` default or max, up to 300 MB by URL; audio (MP3, WAV, FLAC, M4A, OGG) at about 6.25 tokens per second, up to 100 MB by URL; no local file upload [mimo-docs-thinking]
  [mimo-docs-thinking-zh] [mimo-docs-structured] [mimo-docs-image] [mimo-docs-video] [mimo-docs-audio]. LiteLLM needs `thinking` passed explicitly [litellm-mimo]. An Alibaba Model Studio page documents only the previous `mimo-v2.5-pro`, with different parameter ranges and no multimodal input [aliyun-mimo].
- **Thinking Machines Lab (both models).** The renderer, not the caller, inserts the effort control; hosted context options are 64K and 256K; the safety wording is shared; audio length guidance differs (20 minutes for Inkling, 2 for Small) [tinker-thinking-effort] [tinker-pricing].
- **Speech models (NVIDIA).** Both are full-duplex and have no turn-detection setting. Artificial Analysis lists PersonaPlex at 91.0% and VoiceChat at 52.9% on conversational dynamics, and 19.1% and 27.0% on speech reasoning (read 2026-10-03); NVIDIA's own VoiceChat interruption result is far higher than the independent one, and the pages do not explain the gap [aa-s2s] [nvidia-card-voicechat].
- **Self-hosting.** Each model has its own parser names (`hy_v4`, `inkling`, `k2_horizon`, `mimo`, and `qwen3_coder` with `nemotron_v3` for NVIDIA) and needs a tensor-parallel multi-GPU setup; Nemotron's Dynamo recipe notes that, with the vLLM bundled in Dynamo 1.4.0, JSON-constrained output with reasoning on can return malformed JSON and forced tool choice can
  return plain content [dynamo-nemotron].
- **Artificial Analysis Intelligence Index v4.3.2** (independent; reasoning variants; read on the open-weights board and each model's own page): MiMo-V2.6-Pro 46, MiMo-V2.6-Flash 38, K2 Horizon 375B 31, Inkling-Small 26, Inkling 25 (xhigh), Hy3 25, Nemotron 3 Ultra 23; no Hy4 entry [aa-open-weights-board] [aa-model-pages]. Older index versions give very different numbers for the same model (Inkling 41 on v4.1,
  Nemotron 47.7 on an earlier version), so scores are only comparable within one version.
- **Independent coding coverage.** Scale's SWE-Bench Pro V2 table lists Inkling only (89.88 on the full set, 56.9 on the HARD tab); Artificial Analysis's Coding Agent Index lists none of
  these models, and METR lists none (latest update shown 2026-05-08) [scale-swe-pro-v2] [aa-coding-agents] [metr-horizons].

## Open questions

- Independent runs for Hy4 preview, K2 Horizon, the MiMo pair and Nemotron 3 Ultra on current coding and agent benchmarks.
- Whether any of these makers will publish a system card with refusal and injection measurements.
- How Inkling's effort scale applies to Inkling-Small.
- Whether Hy4 preview's reasoning-length and over-verification issues are fixed in its release.
- Hosted-API availability and list prices for K2 Horizon.
- Whether NVIDIA will host its speech models, and why its interruption results differ from the independent ones.

## Sources

- [hf-hy4] https://huggingface.co/tencent/Hy4-preview (kind L, read 2026-10-03)
- [hf-hy4-page] https://huggingface.co/tencent/Hy4-preview (kind L, read 2026-10-03)
- [hf-hy3] https://huggingface.co/tencent/Hy3/raw/main/README.md (kind L, read 2026-10-03)
- [hf-hy3-preview] https://huggingface.co/tencent/Hy3-preview/raw/main/README.md (kind L, read 2026-10-03)
- [nyu-hy3] https://rits.shanghai.nyu.edu/ai/tencent-releases-hy3-295b-open-moe-model-under-apache-2-0/ (kind A, read 2026-10-03)
- [tencent-hy4-news] https://technode.com/2026/08/28/tencent-open-sources-hy4-preview-with-770b-parameters-and-a-1m-token-context/ (kind A, read 2026-10-03)
- [tml-model-card] https://thinkingmachines.ai/model-card/inkling/ (kind L, read 2026-10-03)
- [tml-model-card-small] https://thinkingmachines.ai/model-card/inkling-small/ (kind L, read 2026-10-03)
- [av-inkling] https://analyticsvidhya.com/blog/2026/07/thinking-machines-inkling (kind A, read 2026-10-03)
- [tinker-using-inkling] https://tinker-docs.thinkingmachines.ai/cookbook/inkling/ (kind L, read 2026-10-03)
- [tinker-thinking-effort] https://tinker-docs.thinkingmachines.ai/cookbook/inkling/thinking-effort/ (kind L, read 2026-10-03)
- [tinker-pricing] https://tinker-docs.thinkingmachines.ai/tinker/models/models_and_pricing/ (kind L, read 2026-10-03)
- [hf-k2-horizon] https://huggingface.co/IFM/K2-Horizon-375B-A23B (kind L, read 2026-10-03)
- [mbzuai-k2-nyu] https://rits.shanghai.nyu.edu/ai/ifm-releases-k2-horizon-six-open-models/ (kind A, read 2026-10-03)
- [kyodo-k2-think] https://kyodonewsprwire.jp/release/202601283158 (kind A, read 2026-10-03)
- [tbench-integrity] https://www.tbench.ai/news/leaderboard-integrity-update (kind M, read 2026-10-03)
- [hf-mimo-pro] https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL (kind L, read 2026-10-03)
- [mimo-docs-models] https://mimo.mi.com/docs/en-US/quick-start/summary/model (kind L, read 2026-10-03)
- [mimo-docs-thinking] https://mimo.mi.com/docs/en-US/quick-start/usage-guide/text-generation/deep-thinking (kind L, read 2026-10-03)
- [mimo-docs-thinking-zh] https://mimo.mi.com/docs/zh-CN/quick-start/usage-guide/text-generation/deep-thinking (kind L, read 2026-10-03)
- [mimo-docs-first-call] https://mimo.mi.com/docs/zh-CN/quick-start/summary/first-api-call (kind L, read 2026-10-03)
- [mimo-docs-structured] https://mimo.mi.com/docs/en-US/quick-start/usage-guide/text-generation/structured-output (kind L, read 2026-10-03)
- [mimo-docs-image] https://mimo.mi.com/docs/en-US/quick-start/usage-guide/multimodal-understanding/image-understanding (kind L, read 2026-10-03)
- [mimo-docs-audio] https://mimo.mi.com/docs/en-US/quick-start/usage-guide/multimodal-understanding/audio-understanding (kind L, read 2026-10-03)
- [mimo-docs-video] https://mimo.mi.com/docs/en-US/quick-start/usage-guide/multimodal-understanding/video-understanding (kind L, read 2026-10-03)
- [litellm-mimo] https://docs.litellm.ai/blog/mimo_v2_6 (kind A, read 2026-10-03)
- [aliyun-mimo] https://help.aliyun.com/en/model-studio/mimo (kind L, read 2026-10-03)
- [datanorth-mimo] https://datanorth.ai/news/xiaomi-releases-mimo-v2-6-pro-and-flash (kind A, read 2026-10-03)
- [nvidia-nemotron-blog] https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/ (kind L, read 2026-10-03)
- [hf-nemotron] https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16 (kind L, read 2026-10-03)
- [nvidia-tech-report] https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf (kind L, read 2026-10-03)
- [ngc-nemotron-explain] https://catalog.ngc.nvidia.com/orgs/nim/nvidia/models/nemotron-3-ultra-550b-a55b/-/model-card/explainability (kind L, read 2026-10-03)
- [dynamo-nemotron] https://docs.dynamo.nvidia.com/dynamo/dev/recipes/nemotron-3-ultra.md (kind L, read 2026-10-03)
- [aa-open-weights-board] https://artificialanalysis.ai/models/open-source (kind M, read 2026-10-03)
- [aa-model-pages] https://artificialanalysis.ai/models/inkling and the other five Artificial Analysis model pages listed in the frontmatter (kind M, read 2026-10-03)
- [scale-swe-pro-v2] https://labs.scale.com/leaderboard/swe_bench_pro_public_v2 (kind M, read 2026-10-03)
- [metr-horizons] https://metr.org/time-horizons/ (kind M, read 2026-10-03)
- [cloudprice-hy4] https://cloudprice.net/models/tencent/hy4-preview (kind A, read 2026-10-03)
- [orcarouter-hy4] https://www.orcarouter.ai/blog/tencent-hy4-preview-open-source (kind A, read 2026-10-03)
- [the-decoder-inkling] https://the-decoder.com/ex-openai-cto-muratis-thinking-machines-drops-inkling-a-975b-parameter-model-that-leads-us-labs-but-trails-china/ (kind A, read 2026-10-03)
- [cloudflare-inkling] https://developers.cloudflare.com/ai/models/thinkingmachines/inkling/ (kind A, read 2026-10-03)
- [mimo-tech-report] https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL/blob/main/MiMo_V2_6_technical_report.pdf (kind L, read 2026-10-03)
- [hf-nemotron-super] https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16/raw/main/README.md (kind L, read 2026-10-03)
- [aa-coding-agents] https://artificialanalysis.ai/agents/coding-agents (kind M, read 2026-10-03)
- [nvidia-card-personaplex] https://huggingface.co/nvidia/personaplex-7b-v1 (kind L, read 2026-10-03)
- [nvidia-gh-personaplex] https://github.com/NVIDIA/personaplex (kind L, read 2026-10-03)
- [nvidia-card-voicechat] https://huggingface.co/nvidia/NVIDIA-NemotronLabs-VoiceChat-11B (kind L, read 2026-10-03)
- [aa-s2s] https://artificialanalysis.ai/speech-to-speech (kind M, read 2026-10-03)
