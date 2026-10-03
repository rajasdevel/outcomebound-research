---
last_checked: 2026-10-03
volatility: VOLATILE (a provider's catalogue, prices, limits and feature support change often)
kind: first-party lab API
sources:
  - https://elevenlabs.io/docs/eleven-agents/overview
  - https://elevenlabs.io/docs/eleven-agents/customization/llm
  - https://elevenlabs.io/docs/overview/models
  - https://elevenlabs.io/docs/api-reference/agents/create
  - https://elevenlabs.io/docs/eleven-agents/customization/voice/expressive-mode
  - https://elevenlabs.io/docs/api-reference/text-to-speech/convert
  - https://elevenlabs.io/pricing/api
  - https://elevenlabs.io/docs/overview/administration/data-residency
  - https://elevenlabs.io/docs/api-reference/authentication
  - https://elevenlabs.io/docs/eleven-api/guides/how-to/best-practices/security
  - https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/client-side-streaming
  - https://elevenlabs.io/docs/llms.txt
  - https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/tts-vs-ttd-websockets
  - https://elevenlabs.io/docs/changelog/2026/9/28
  - https://elevenlabs.io/docs/eleven-api/quickstart
  - https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-do-audio-tags-work-with-eleven-v3-and-v4
  - https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert
  - https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue
  - https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tdd
  - https://elevenlabs.io/docs/api-reference/text-to-dialogue/ttd-websocket
  - https://elevenlabs.io/docs/api-reference/speech-to-text/convert
  - https://elevenlabs.io/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime
  - https://elevenlabs.io/docs/eleven-api/concepts/audio-streaming
  - https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/multi-context-web-socket
  - https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/request-stitching
  - https://elevenlabs.io/docs/overview/capabilities/speech-to-text
  - https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/skip-turn
  - https://elevenlabs.io/docs/eleven-agents/best-practices/guardrails
  - https://elevenlabs.io/docs/overview/administration/billing
  - https://elevenlabs.io/pricing/agents
  - https://elevenlabs.io/docs/overview/administration/pay-as-you-go
  - https://elevenlabs.io/docs/eleven-agents/guides/burst-pricing
  - https://elevenlabs.io/docs/help-center/product/eleven-agents/how-much-does-eleven-agents-cost
  - https://elevenlabs.io/docs/eleven-agents/customization/llm/optimizing-costs
  - https://elevenlabs.io/docs/overview/capabilities/text-to-speech
  - https://artificialanalysis.ai/text-to-speech
  - https://elevenlabs.io/docs/changelog/2026/8/17
  - https://elevenlabs.io/docs/eleven-agents/customization/conversation-flow
  - https://elevenlabs.io/docs/eleven-api/resources/zero-retention-mode
  - https://elevenlabs.io/docs/help-center/legal/is-my-data-used-to-improve-eleven-labs-ai-models
  - https://elevenlabs.io/docs/eleven-agents/customization/privacy/retention
  - https://elevenlabs.io/docs/eleven-agents/customization/privacy/audio-saving
  - https://elevenlabs.io/docs/eleven-agents/customization/privacy/zrm
  - https://elevenlabs.io/docs/eleven-agents/legal/hipaa
  - https://elevenlabs.io/blog/introducing-scribe-v2
  - https://elevenlabs.io/docs/changelog/2026/9/7
  - https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tts
  - https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/transcripts-and-commit-strategies
  - https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices
  - https://elevenlabs.io/docs/eleven-agents/best-practices/prompting-guide
  - https://elevenlabs.io/docs/eleven-api/guides/how-to/best-practices/latency-optimization
  - https://elevenlabs.io/docs/eleven-api/concepts/latency
  - https://elevenlabs.io/docs/overview/capabilities/voices
  - https://elevenlabs.io/docs/eleven-agents/customization/voice
  - https://elevenlabs.io/docs/eleven-agents/customization/llm/custom-llm
  - https://elevenlabs.io/docs/eleven-agents/customization/llm/llm-cascading
---

# ElevenLabs

first-party lab API

ElevenLabs trains speech synthesis models (Eleven) and transcription models (Scribe). It sells them through its own API at `api.elevenlabs.io`, through a web app (ElevenCreative) and through a hosted agent platform (ElevenAgents). It does not train language models. The agent platform routes calls to language models of other makers and passes their cost through. This file covers the ElevenLabs API and platform as one route. Everything here was read on 2026-10-03 [el-agents-overview] [el-agents-llm].

## Models offered

The ten ElevenLabs models in this library, by class. The [maker README](../models/elevenlabs/README.md) holds the lineage.

| Model file | API id | Note |
| --- | --- | --- |
| [Eleven v4](../models/elevenlabs/eleven_v4.md) | `eleven_v4` | Expressive speech synthesis, 90+ languages. Text to Speech and Text to Dialogue [el-models] |
| [Eleven v4 Turbo](../models/elevenlabs/eleven_v4_turbo.md) | `eleven_v4_turbo` | Low-latency variant. Text to Dialogue WebSocket and ElevenAgents [el-models] |
| [Eleven v3](../models/elevenlabs/eleven_v3.md) | `eleven_v3` | Previous expressive generation. Not an agent speech model in the agent API enum [el-api-agents] |
| [Eleven v3 Conversational](../models/elevenlabs/eleven_v3_conversational.md) | `eleven_v3_conversational` | Low-latency v3, for agents and the Text to Dialogue WebSocket [el-agents-expressive] |
| [Eleven Flash v2.5](../models/elevenlabs/eleven_flash_v2_5.md) | `eleven_flash_v2_5` | 32 languages, about 75 ms [el-models] |
| [Eleven Flash v2](../models/elevenlabs/eleven_flash_v2.md) | `eleven_flash_v2` | English only; the default agent speech model [el-api-agents] |
| [Eleven Multilingual v2](../models/elevenlabs/eleven_multilingual_v2.md) | `eleven_multilingual_v2` | 29 languages; the default model of the Text to Speech endpoint [el-api-tts] |
| [Scribe v2](../models/elevenlabs/scribe_v2.md) | `scribe_v2` | Batch transcription [el-models] |
| [Scribe v2 Realtime](../models/elevenlabs/scribe_v2_realtime.md) | `scribe_v2_realtime` | Streaming transcription [el-models] |
| [Scribe v2 Medical](../models/elevenlabs/scribe_v2_medical.md) | `scribe_v2_medical` | Batch transcription for clinical audio [el-models] |

Other models on the platform have no file here. They are the deprecated `eleven_turbo_v2_5` and `eleven_turbo_v2`, and the voice changer models `eleven_multilingual_sts_v2` and `eleven_english_sts_v2`. They also include the voice design models `eleven_ttv_v3` and `eleven_multilingual_ttv_v2`, and `eleven_text_to_sound_v2`. The music models are `music_v2_5`, `music_v2` and the outclassed `music_v1`. The deprecated `scribe_v1` also has no file. So do dubbing, voice isolation, and the image and video models, many of which come from other makers [el-models] [el-pricing-api].

**Language models in ElevenAgents.** The agent page lists models of Google, OpenAI and Anthropic, and four hosted by ElevenLabs. Among the models that have a file in this library are [Claude Opus 5.5](../models/anthropic/claude-opus-5-5.md), [Claude Opus 5](../models/anthropic/claude-opus-5.md), [Claude Sonnet 5.5](../models/anthropic/claude-sonnet-5-5.md), [Claude Sonnet 5](../models/anthropic/claude-sonnet-5.md), [Claude Haiku 4.5](../models/anthropic/claude-haiku-4-5.md), [GPT-6 Astra](../models/openai/gpt-6-astra.md), [GPT-6.1 Sol](../models/openai/gpt-6.1-sol.md), [GPT-6 Sol](../models/openai/gpt-6-sol.md), [GPT-6 Luna](../models/openai/gpt-6-luna.md), [GPT-5.6 Terra](../models/openai/gpt-5.6-terra.md), [GPT-5.6 Luna](../models/openai/gpt-5.6-luna.md), [Gemini 3.8 Flash](../models/google/gemini-3.8-flash.md), [Gemini 3.7 Flash](../models/google/gemini-3.7-flash.md), [Gemini 3.5 Flash-Lite](../models/google/gemini-3.5-flash-lite.md), [Gemini 3.1 Pro (Preview)](../models/google/gemini-3.1-pro-preview.md), [Gemini 3.1 Flash-Lite](../models/google/gemini-3.1-flash-lite.md), [GLM-5.2](../models/zai/glm-5.2.md) and [Qwen3.6-35B-A3B](../models/alibaba/qwen3.6-35b-a3b.md). The page also lists "DeepSeek Flash 4.1", which may be the model of this library's DeepSeek V4.1-Flash file; the pages read do not confirm it [el-agents-llm].

## API surface

- **Protocol.** Its own REST and WebSocket API. No OpenAI-compatible speech endpoint was found in the pages read. Model ids are lower-case snake case, such as `eleven_v4`, `eleven_flash_v2_5` and `scribe_v2` [el-api-tts] [el-models].
- **Base hosts.** `api.elevenlabs.io` (global routing), `api.us.elevenlabs.io` (USA only), and for Enterprise isolated environments `api.eu.residency.elevenlabs.io`, `api.in.residency.elevenlabs.io` and `api.sg.residency.elevenlabs.io`. The WebSocket hosts follow the same names with `wss` [el-api-tts] [el-residency].
- **Auth.** An API key in `xi-api-key`. A key can carry endpoint scopes, a credit quota and an IP allowlist. User keys can expire between 15 minutes and 30 days. A single-use token (valid 15 minutes) serves a browser. The security guide advises service accounts for each environment and resource-level permissions in the customer's own backend for cloned voices [el-api-auth] [el-security] [el-stt-client].
- **Endpoints.** Text to Speech (HTTP, stream, WebSocket, multi-context WebSocket), Text to Dialogue (HTTP, stream, WebSocket), Speech to Text (batch with webhooks, realtime WebSocket), the agent platform (configuration API and a conversation WebSocket), Speech Engine, voices, pronunciation dictionaries, and others [el-llms] [el-ws-compare].
- **SDKs and tools.** Python and JavaScript clients, browser and React packages, React Native, Swift and Kotlin agent SDKs, a CLI, a hosted MCP server and an agent skill for coding assistants. The docs can be fetched as Markdown by adding `.md` to a page URL [el-changelog-v4] [el-agents-overview] [el-llms] [el-quickstart].

## Feature parity

For a first-party API, parity means differences between endpoints and between its own models. The pages read list no other route that serves ElevenLabs models.

| Endpoint | Models that work |
| --- | --- |
| Text to Speech (HTTP and stream) | `eleven_multilingual_v2` (default), the Flash models, `eleven_v3` and `eleven_v4` [el-api-tts] [el-tags-help] |
| Text to Speech WebSocket and multi-context WebSocket | The non-v3 and non-v4 models, such as Flash and Multilingual v2 [el-ws-compare] |
| Text to Dialogue (HTTP and stream) | `eleven_v3` (default) and `eleven_v4` [el-api-ttd] [el-ttd-overview] |
| Text to Dialogue WebSocket | Models whose id starts with `eleven_v3` or `eleven_v4`. The API reference says v3 models only, with `eleven_v3_conversational` as the default [el-ws-ttd] [el-api-ttd-ws] |
| ElevenAgents speech model | `eleven_flash_v2`, `eleven_flash_v2_5`, `eleven_multilingual_v2`, `eleven_v3_conversational`, `eleven_v4`, `eleven_v4_turbo` and the deprecated Turbo ids [el-api-agents] |
| Speech to Text | `scribe_v2`, `scribe_v2_medical` (batch); `scribe_v2_realtime` (WebSocket) [el-api-stt] [el-api-stt-rt] |

- **Streaming.** HTTP streaming when the text is ready. WebSockets when a language model feeds the speech model. A WebSocket counts toward concurrency only while it generates, but a Text to Dialogue WebSocket holds a session while open [el-audio-streaming] [el-models].
- **Barge-in.** The multi-context WebSocket (up to five contexts) closes one stream and opens another. No cancel message is described for the Text to Dialogue WebSocket [el-ws-multi] [el-ws-ttd].
- **Continuity across requests.** `previous_text`, `next_text` and request ids. Not available for `eleven_v3`, and not with Zero Retention Mode [el-stitching] [el-api-tts].
- **Batch and caching.** No batch discount and no cache were found for speech. Asynchronous transcription with webhooks exists [el-stt-overview].
- **Structured output and tools.** Not applicable to speech models. The agent platform has webhook, client, code and MCP tools, system tools such as end call, transfer and skip turn, a knowledge base with retrieval, and guardrails [el-agents-overview] [el-agents-skip] [el-agents-guardrails].
- **Long input.** Limits are in characters for synthesis (5,000 to 40,000 by model) and in hours for transcription (10) [el-models] [el-stt-overview].
- **Vision.** Not offered by the speech models.

## Pricing

ElevenLabs bills per unit of media, not per token, and the card of each model holds its price [el-pricing-api].

- **Units.** Speech synthesis: US dollars per 1,000 characters on the API, and credits on subscriptions. Transcription: US dollars per hour of audio, with extras for entity detection and keyterms. Agents and Speech Engine: US dollars per call minute. Music and sound effects: per generation or minute [el-pricing-api] [el-billing].
- **Credits.** The website draws credits. Credits were once called characters. The cost per character varies by model, plan and API or website use. Up to two months of unused credits roll over [el-billing].
- **Plans.** Free, Starter, Creator, Pro, Scale and Business, at US$0, 6, 22, 99, 299 and 990 a month, plus Enterprise (custom). Starter and Creator have first-month discounts. A plan sets included credits, included agent minutes, concurrency, custom voice slots and audio quality. Pay As You Go lets a self-serve account prepay a balance [el-pricing-api] [el-pricing-agents] [el-payg].
- **Promotions.** Until 2026-10-12, v4 and v4 Turbo are 72% off on the API price, and Creator plans and above include three times the credits. Starter has a first-month price until 2026-10-18 [el-pricing-api] [el-pricing-agents].
- **Agents.** Included minutes by plan, then US$0.08 for each additional minute and US$0.003 for each text message. Burst calls (up to three times the concurrency limit, or 300) cost twice the rate and get lower priority. Silence of more than 10 seconds in a voice call is billed at 5% of the rate. Language model cost is passed through, and telephony adds no ElevenLabs fee. A startup grant gives 12 months free [el-pricing-agents] [el-agents-burst] [el-agents-cost] [el-agents-opt] [el-agents-llm].
- **Rights.** Paid plans carry commercial rights to generated audio. On the free plan, use is non-commercial with attribution [el-tts-overview] [el-billing].
- **Third-party prices.** Artificial Analysis lists some ElevenLabs models at a higher price per million characters than the pricing page [aa-tts-board].

## Limits and data

- **Concurrency.** A plan sets simultaneous requests per model group, with a priority level from 3 (Free) to 6 (Enterprise). The README lists the numbers. Response headers `current-concurrent-requests` and `maximum-concurrent-requests` show usage. Queued requests add about 50 ms. Enterprise requests over the limit can still run, slower [el-models].
- **Agent calls.** Concurrent calls by plan: 4, 6, 10, 20, 30 and 40 (Free to Business). A wait queue can hold callers: `wait_timeout_seconds` is up to 1,800 and defaults to 180. A call lasts 600 seconds by default and 60 to 7,200 by setting [el-pricing-agents] [el-changelog-0817] [el-agents-flow].
- **Regions.** Standard storage is in the USA. Enterprise customers can store data in the EU, India or Singapore. Storage stays in the chosen place, but processing may happen elsewhere for support and moderation. In the EU, Zero Retention Mode with the API can keep processing in the EU, unless an optional integration needs another region. Dubbing is not available in isolated environments. Language model choice differs by region [el-residency].
- **Retention without Zero Retention Mode.** History is kept by default. A customer can delete generations through the API. Debugging and moderation logs may still keep data. Backups keep deleted items for up to 30 days. Deleting an account deletes its data [el-zrm].
- **Training.** ElevenLabs uses some customer data to improve its audio models. Any user can switch this off in the data-use settings. By default it does not train on Enterprise customer data. It has agreements that stop its language model providers from training on customer content [el-data-use] [el-zrm].
- **Zero Retention Mode.** For select Enterprise customers, API only. The request parameter is `enable_logging=false`. It covers speech and dialogue text and audio, voice changer audio, transcription audio and text, and all agent input and output. It does not cover music, image and video, voice cloning samples, dubbing or Studio. Support is limited, and ElevenLabs can restrict access for high-risk use [el-zrm].
- **Agents data.** Transcripts and audio are kept 2 years by default. Retention is settable in days, -1 (unlimited) or 0 (scheduled deletion), and audio saving can be off. Each agent can have its own Zero Retention Mode. Under it, Gemini, Claude and ElevenLabs-hosted Qwen models are available, and MCP is not [el-agents-retention] [el-agents-audio] [el-agents-zrm] [el-zrm].
- **Compliance.** HIPAA Business Associate Agreements for Enterprise customers, with Zero Retention Mode and restricted language models. The launch posts list SOC 2, ISO 27001, PCI DSS level 1 and GDPR [el-agents-hipaa] [el-blog-scribe2].

## Notes for agents and harnesses

- **Defaults differ.** The default model differs by endpoint: Multilingual v2 on Text to Speech, `eleven_v3` on Text to Dialogue, `eleven_flash_v2` for a new agent, and `eleven_v3` in the CLI (version 1.2.0) [el-api-tts] [el-api-ttd] [el-api-agents] [el-changelog-0907].
- **WebSocket and model.** The Text to Speech WebSocket rejects v3 and v4. The Text to Dialogue WebSocket needs a v3 or v4 id. One voice for `eleven_v4_turbo` and `eleven_v3_conversational`, up to 10 for `eleven_v4` [el-ws-compare] [el-api-ttd-ws].
- **Idle timeouts.** 20 seconds on the speech WebSockets (a space keeps the Text to Speech one open, `keep_alive` the dialogue one), 15 seconds on the realtime transcription socket [el-ws-tts] [el-ws-ttd] [el-stt-commit].
- **Text is spoken as written.** Older models read narrative cues aloud. v3 and v4 can read a tag as a sound effect. Small fast models misread numbers. The guides advise normalising text before it reaches the model, or setting the agent's `text_normalisation_type` [el-tts-practices] [el-agents-prompting].
- **Prompts steer behaviour, settings steer timing.** The agent guide says the system prompt controls conversation style and not turn-taking or the languages an agent speaks. Those are platform settings [el-agents-prompting].
- **Tool arguments.** Spoken forms of emails and numbers enter the context. The agent guide gives the exact format in each tool parameter description [el-agents-prompting].
- **Latency figures.** The ~75 ms and ~100 ms figures leave out network and application time. The `x-region` header names the serving cluster, and `api.us.elevenlabs.io` keeps traffic in the USA [el-latency-opt] [el-latency-concept].
- **Docs disagree.** See the README for normalisation, file limits, language and voice counts, and the Text to Dialogue WebSocket reference. A claim is only as good as its page and date [el-api-ttd-ws] [el-ws-ttd].
- **Voice ids expire.** Default voices end on 2026-12-31. Voice Library voices do not work through the API on the free plan. Voices with live moderation cannot run in agents [el-voices] [el-agents-voice].
- **Language model ids.** Agent configuration uses its own ids for language models, such as `gpt-6-sol`, `glm-52`, `deepseek-v41-flash`, `claude-opus-5` and `claude-opus-5-5` [el-changelog-v4].
- **Custom language models.** The endpoint must copy OpenAI's Chat Completions or Responses format and stream server-sent events. Reasoning must come in separate fields [el-agents-custom-llm].
- **Backup chain.** If the chosen language model fails, the platform tries a default list. The page lists Gemini 2.5 Flash, GPT-4o, Gemini 2.5 Flash Lite and Claude Sonnet 4.5, and says the list changes without notice. A strict-privacy mode filters it [el-agents-cascade].
- **Keys stay on the server.** The docs say never to expose an API key in client code, and give single-use tokens for browser clients [el-api-auth] [el-stt-client].

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| el-agents-overview | https://elevenlabs.io/docs/eleven-agents/overview | L | 2026-10-03 |
| el-agents-llm | https://elevenlabs.io/docs/eleven-agents/customization/llm | L | 2026-10-03 |
| el-models | https://elevenlabs.io/docs/overview/models | L | 2026-10-03 |
| el-api-agents | https://elevenlabs.io/docs/api-reference/agents/create | L | 2026-10-03 |
| el-agents-expressive | https://elevenlabs.io/docs/eleven-agents/customization/voice/expressive-mode | L | 2026-10-03 |
| el-api-tts | https://elevenlabs.io/docs/api-reference/text-to-speech/convert | L | 2026-10-03 |
| el-pricing-api | https://elevenlabs.io/pricing/api | L | 2026-10-03 |
| el-residency | https://elevenlabs.io/docs/overview/administration/data-residency | L | 2026-10-03 |
| el-api-auth | https://elevenlabs.io/docs/api-reference/authentication | L | 2026-10-03 |
| el-security | https://elevenlabs.io/docs/eleven-api/guides/how-to/best-practices/security | L | 2026-10-03 |
| el-stt-client | https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/client-side-streaming | L | 2026-10-03 |
| el-llms | https://elevenlabs.io/docs/llms.txt | L | 2026-10-03 |
| el-ws-compare | https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/tts-vs-ttd-websockets | L | 2026-10-03 |
| el-changelog-v4 | https://elevenlabs.io/docs/changelog/2026/9/28 | L | 2026-10-03 |
| el-quickstart | https://elevenlabs.io/docs/eleven-api/quickstart | L | 2026-10-03 |
| el-tags-help | https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-do-audio-tags-work-with-eleven-v3-and-v4 | L | 2026-10-03 |
| el-api-ttd | https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert | L | 2026-10-03 |
| el-ttd-overview | https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue | L | 2026-10-03 |
| el-ws-ttd | https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tdd | L | 2026-10-03 |
| el-api-ttd-ws | https://elevenlabs.io/docs/api-reference/text-to-dialogue/ttd-websocket | L | 2026-10-03 |
| el-api-stt | https://elevenlabs.io/docs/api-reference/speech-to-text/convert | L | 2026-10-03 |
| el-api-stt-rt | https://elevenlabs.io/docs/api-reference/speech-to-text/v-1-speech-to-text-realtime | L | 2026-10-03 |
| el-audio-streaming | https://elevenlabs.io/docs/eleven-api/concepts/audio-streaming | L | 2026-10-03 |
| el-ws-multi | https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/multi-context-web-socket | L | 2026-10-03 |
| el-stitching | https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/request-stitching | L | 2026-10-03 |
| el-stt-overview | https://elevenlabs.io/docs/overview/capabilities/speech-to-text | L | 2026-10-03 |
| el-agents-skip | https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/skip-turn | L | 2026-10-03 |
| el-agents-guardrails | https://elevenlabs.io/docs/eleven-agents/best-practices/guardrails | L | 2026-10-03 |
| el-billing | https://elevenlabs.io/docs/overview/administration/billing | L | 2026-10-03 |
| el-pricing-agents | https://elevenlabs.io/pricing/agents | L | 2026-10-03 |
| el-payg | https://elevenlabs.io/docs/overview/administration/pay-as-you-go | L | 2026-10-03 |
| el-agents-burst | https://elevenlabs.io/docs/eleven-agents/guides/burst-pricing | L | 2026-10-03 |
| el-agents-cost | https://elevenlabs.io/docs/help-center/product/eleven-agents/how-much-does-eleven-agents-cost | L | 2026-10-03 |
| el-agents-opt | https://elevenlabs.io/docs/eleven-agents/customization/llm/optimizing-costs | L | 2026-10-03 |
| el-tts-overview | https://elevenlabs.io/docs/overview/capabilities/text-to-speech | L | 2026-10-03 |
| aa-tts-board | https://artificialanalysis.ai/text-to-speech | M | 2026-10-03 |
| el-changelog-0817 | https://elevenlabs.io/docs/changelog/2026/8/17 | L | 2026-10-03 |
| el-agents-flow | https://elevenlabs.io/docs/eleven-agents/customization/conversation-flow | L | 2026-10-03 |
| el-zrm | https://elevenlabs.io/docs/eleven-api/resources/zero-retention-mode | L | 2026-10-03 |
| el-data-use | https://elevenlabs.io/docs/help-center/legal/is-my-data-used-to-improve-eleven-labs-ai-models | L | 2026-10-03 |
| el-agents-retention | https://elevenlabs.io/docs/eleven-agents/customization/privacy/retention | L | 2026-10-03 |
| el-agents-audio | https://elevenlabs.io/docs/eleven-agents/customization/privacy/audio-saving | L | 2026-10-03 |
| el-agents-zrm | https://elevenlabs.io/docs/eleven-agents/customization/privacy/zrm | L | 2026-10-03 |
| el-agents-hipaa | https://elevenlabs.io/docs/eleven-agents/legal/hipaa | L | 2026-10-03 |
| el-blog-scribe2 | https://elevenlabs.io/blog/introducing-scribe-v2 | L | 2026-10-03 |
| el-changelog-0907 | https://elevenlabs.io/docs/changelog/2026/9/7 | L | 2026-10-03 |
| el-ws-tts | https://elevenlabs.io/docs/eleven-api/guides/how-to/websockets/realtime-tts | L | 2026-10-03 |
| el-stt-commit | https://elevenlabs.io/docs/eleven-api/guides/how-to/speech-to-text/realtime/transcripts-and-commit-strategies | L | 2026-10-03 |
| el-tts-practices | https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices | L | 2026-10-03 |
| el-agents-prompting | https://elevenlabs.io/docs/eleven-agents/best-practices/prompting-guide | L | 2026-10-03 |
| el-latency-opt | https://elevenlabs.io/docs/eleven-api/guides/how-to/best-practices/latency-optimization | L | 2026-10-03 |
| el-latency-concept | https://elevenlabs.io/docs/eleven-api/concepts/latency | L | 2026-10-03 |
| el-voices | https://elevenlabs.io/docs/overview/capabilities/voices | L | 2026-10-03 |
| el-agents-voice | https://elevenlabs.io/docs/eleven-agents/customization/voice | L | 2026-10-03 |
| el-agents-custom-llm | https://elevenlabs.io/docs/eleven-agents/customization/llm/custom-llm | L | 2026-10-03 |
| el-agents-cascade | https://elevenlabs.io/docs/eleven-agents/customization/llm/llm-cascading | L | 2026-10-03 |
