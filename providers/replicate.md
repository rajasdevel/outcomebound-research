---
last_checked: 2026-10-03
volatility: VOLATILE (ownership, catalogue, prices and limits change often)
kind: inference host
sources:
  - https://replicate.com/docs
  - https://replicate.com/docs/reference/http
  - https://replicate.com/pricing
  - https://replicate.com/docs/topics/predictions/rate-limits
  - https://replicate.com/collections/language-models
  - https://replicate.com/blog/replicate-cloudflare
  - https://www.cloudflare.com/en-gb/press/press-releases/2025/cloudflare-to-acquire-replicate-to-build-the-most-seamless-ai-cloud-for-developers/
  - https://www.sec.gov/Archives/edgar/data/1477333/000147733326000016/cloud-20251231.htm
---

# Replicate

inference host

Replicate is a hosted API for running machine-learning models, mostly image, video, audio and other non-text models, with a smaller set of language models. Anyone can publish a model, so the catalogue mixes "official" models run by Replicate and a very large community set, all called through one predictions API. Ownership changed: Cloudflare announced on 2025-11-17 that it would acquire Replicate, and Cloudflare's annual report for 2025 states that it acquired all outstanding shares on 2025-12-01 for $57.4 million in cash. Replicate's own post of the same date says "The API isn't changing. The models you're using today will keep working." It says Replicate keeps its brand and that Workers AI users will gain a larger catalogue. The Cloudflare press release says Replicate's 50,000 or more models will become available to Cloudflare Workers AI users. The Replicate documentation pages read here do not mention Cloudflare. They are still served as of the read date. [rblog, cf, sec, docs]

## Models offered

Mostly generative image, video and speech models, plus a language-model collection. The collection page read on 2026-10-03 lists, as featured, `google/gemini-3.1-pro`, `anthropic/claude-opus-4.6` and `openai/gpt-5.2`, and among about 40 others `openai/gpt-5.6-luna`, `openai/gpt-5.6-terra` and `openai/gpt-5.6-sol`, `openai/gpt-oss-120b` and `openai/gpt-oss-20b`, `moonshotai/kimi-k2.5`, DeepSeek V3, V3.1 and R1, Claude 4.5 Sonnet and Haiku, and older GPT-4-era, Llama 3 and Gemma models. Model files in scope that it names: [GPT-5.6 Luna](../models/openai/gpt-5.6-luna.md), [GPT-5.6 Terra](../models/openai/gpt-5.6-terra.md), GPT-5.6 Sol, [gpt-oss-120b](../models/openai/gpt-oss-120b.md) and [gpt-oss-20b](../models/openai/gpt-oss-20b.md). The newest Claude and Gemini models in this library (for example [Claude Opus 5.5](../models/anthropic/claude-opus-5-5.md)) are not in the collection. How Replicate serves the closed-lab models (through the maker's API or otherwise) is not stated on the pages read. [lm]

## API surface

- **Protocol.** Replicate's own HTTP API at `https://api.replicate.com/v1`. A prediction is created with `POST /predictions`, `POST /models/{owner}/{name}/predictions` (official models) or `POST /deployments/{owner}/{name}/predictions` (deployments). `Prefer: wait=n` (1 to 60) blocks up to 60 seconds for completion; models that stream expose a server-sent-events `stream` URL; a `webhook` URL with `webhook_events_filter` (`start`, `output`, `logs`, `completed`) gives asynchronous delivery. No OpenAI-compatible or Anthropic-compatible chat endpoint was found in the pages read. [http, lm]
- **Auth.** A bearer API token (`REPLICATE_API_TOKEN`). [http]
- **SDKs.** Official clients for Python, Node.js and other languages. [docs]
- **Model ids.** `owner/name`, optionally with a version hash for community models. [docs, lm]
- **Files.** Inputs over 256 KB are passed as HTTP URLs, smaller ones may be data URLs; files served from `replicate.delivery` need the Authorization header. [http]

## Feature parity

Replicate exposes each model's own input schema through the predictions API rather than a unified chat schema, so parity with a maker's API depends on the model's wrapper.

- **Reasoning, effort, tools, structured output.** Not described on the pages read, and no unified parameter set was found; each model defines its inputs. `UNVERIFIED`. [docs]
- **Prompt caching and batch.** Not described on the pages read. `UNVERIFIED`.
- **Streaming.** Supported for models that offer it, by server-sent events, and by webhook events for logs and output. [http]
- **Vision and long context.** Per model. [lm]
- **Closed-lab models.** Claude, GPT and Gemini models appear in the collection; the pages read do not say whether requests go to the maker's API, so which data terms apply is `UNVERIFIED`. [lm]

## Pricing

Pay per use, in three forms: by execution time for most public models, at rates that depend on the hardware (the pricing page lists CPU Small at $0.000025 a second, about $0.09 an hour, up to 8 Nvidia H100 GPUs at $0.0122 a second, about $43.92 an hour); per input and output token for some language models (the page's DeepSeek R1 example is $3.75 per million input tokens and $0.01 per thousand output tokens); and per image or per second of video for generators (for example $0.04 an image for flux-1.1-pro, and $0.09 to $0.25 a second of video). No free tier was named on the pricing page. Enterprise plans add account management, priority support, higher GPU limits, SLAs and volume discounts. Prices per model are on the model pages. [price]

## Limits and data

- **Rate limits.** Creating predictions: 600 requests a minute; other endpoints: 3,000 a minute, with brief bursts allowed. Accounts that were granted credit but have no payment method are held to 1 request a second and 6 a minute. A throttled request returns 429 with a message that the limit resets in about 30 seconds. Limits tighten progressively as a balance falls, and the page suggests automatic reload to keep the balance above $20. [rl]
- **Retention.** For predictions created through the API, input parameters, output values and logs are removed after an hour by default, so outputs have to be saved by the caller. [http]
- **Training and regions.** The pages read do not state a training policy or a region. `UNVERIFIED`.

## Notes for agents and harnesses

- **Outputs expire after an hour.** Inputs, outputs and logs of API predictions are removed after an hour by default, so a client that polls late loses the result; `Prefer: wait` covers short jobs and a webhook covers long ones. [http]
- **No common chat schema.** Each model defines its own inputs, so a client written for chat-completions APIs needs a per-model adapter. [docs]
- **Ownership change.** Replicate's post says the API stays the same. No page read says how Replicate and Cloudflare Workers AI will relate in the long term. [rblog, cf]
- **Throttling follows balance.** An account with granted credit and no payment method is held to 6 requests a minute, and limits tighten as a balance falls. [rl]
- **Chat features are not documented here.** Unlike the open-weight hosts in this folder (for example [together-ai.md](together-ai.md) and [fireworks-ai.md](fireworks-ai.md)), the Replicate pages read describe no chat parameters, caching or batch. [lm, docs]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| docs | https://replicate.com/docs | L | 2026-10-03 |
| http | https://replicate.com/docs/reference/http | L | 2026-10-03 |
| price | https://replicate.com/pricing | L | 2026-10-03 |
| rl | https://replicate.com/docs/topics/predictions/rate-limits | L | 2026-10-03 |
| lm | https://replicate.com/collections/language-models | L | 2026-10-03 |
| rblog | https://replicate.com/blog/replicate-cloudflare | L | 2026-10-03 |
| cf | https://www.cloudflare.com/en-gb/press/press-releases/2025/cloudflare-to-acquire-replicate-to-build-the-most-seamless-ai-cloud-for-developers/ | L | 2026-10-03 |
| sec | https://www.sec.gov/Archives/edgar/data/1477333/000147733326000016/cloud-20251231.htm | L | 2026-10-03 |
