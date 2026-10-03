---
last_checked: 2026-10-03
volatility: MONITOR (lineage, guides and API behaviour change at each release)
sources:
  - https://platform.stepfun.ai/docs/en/guides/models/audio
  - https://platform.stepfun.ai/docs/en/guides/models/stepaudio-3-realtime
  - https://platform.stepfun.ai/docs/en/guides/models/stepaudio-2.5-realtime
  - https://platform.stepfun.ai/docs/en/api-reference/realtime/chat
  - https://platform.stepfun.ai/docs/en/guides/pricing/details
  - https://platform.stepfun.ai/docs/en/guides/model-migration
  - https://arxiv.org/abs/2609.14005
  - https://arxiv.org/abs/2605.23463
  - https://runtimewire.com/article/stepfun-stepaudio-3-five-audio-models
  - https://artificialanalysis.ai/speech-to-speech
---

# StepFun

StepFun is a Shanghai AI lab. It sells text, vision, image and audio models through its Open Platform. This folder holds its realtime speech-to-speech models. StepFun's text and image models are outside this library. Everything here was read on 2026-10-03.

## Models and lineage

| Class | Generation | Model | Notes |
| --- | --- | --- | --- |
| StepAudio Realtime | 3 | [StepAudio 3 Realtime (preview)](stepaudio-3-realtime-preview.md) | Full-duplex, think-while-speaking, voice agent layer; free during the preview; the preview name will retire [step-model-page-3] |
| StepAudio Realtime | 2.5 | [StepAudio 2.5 Realtime](stepaudio-2.5-realtime.md) | End-to-end speech-to-speech over WebSocket; billed by token [step-25-realtime] [step-pricing] |

StepFun released five StepAudio 3 models on about 2026-09-15: realtime, ASR, TTS, a unified audio generation model and a music model. The StepAudio 2.5 family came earlier in 2026 with TTS, ASR, chat and realtime models, and its technical report is dated 2026-05-22. A trade report gives the StepAudio 3 date [runtimewire-step] [step-audio-models] [step-paper-25].

Models without a file, with the reason:

- **StepAudio 3 and 2.5 TTS, ASR, Gen and Music, and the Chat models.** They synthesise or transcribe speech, generate audio, or take speech and return text. They are not speech-to-speech conversation models [step-audio-models].
- **`step-audio-2`, `step-1o-audio` and `step-audio-r1.5`.** The pricing page bills them by token under speech models. No realtime guide for them was found, and they are older than the two generations in scope [step-pricing].
- **Step-Audio R1.1 (Realtime).** Artificial Analysis lists it with 97.6% on speech reasoning and 1.53 seconds to first audio, and with prices per hour of audio. No StepFun page for it was found on the documentation index (read 2026-10-03), so its status as a model that a person can select is not confirmed [aa-s2s].

## API surface

- **Endpoint.** `wss://api.stepfun.ai/v1/realtime?model=<id>`, with `Authorization: Bearer <key>`. The model ids are `stepaudio-3-realtime-preview` and `stepaudio-2.5-realtime` [step-realtime-api].
- **Events.** The event names follow the OpenAI Realtime pattern: `session.update`, `input_audio_buffer.append`, `.commit` and `.clear`, `conversation.item.create` and `.delete`, `response.create` and `response.cancel`, and server events such as `response.audio.delta`. StepFun adds `response.thinking.delta` and `.done`. `modalities` is fixed to text and audio [step-realtime-api].
- **Audio.** `pcm16` in both directions. The 2.5 page states 24 kHz mono [step-realtime-api] [step-25-realtime].
- **Open reference client.** StepFun links an open-source console, `Step-Realtime-Console`, on GitHub [step-realtime-api] [step-model-page-3].
- **Pricing.** Realtime sessions are billed by token. The 2.5 model costs US$1.50 input, US$0.30 cached input and US$10.00 output per million tokens. The 3 preview is free for a limited time [step-pricing].
- **Rate limits.** The Open Platform API has tiers V0 to V4 set by cumulative cash top-up, with concurrency from 5 to 130. The pricing page does not say whether the tiers apply to the Realtime API [step-pricing].

## Prompting guides

StepFun publishes no prompting guide for its realtime models. The API reference describes `instructions` as the system message and says it can guide the content and format of replies and audio behaviour, for example speaking quickly or putting emotion in the voice, with no guarantee. The model pages describe use cases and capabilities [step-realtime-api] [step-model-page-3] [step-25-realtime].

## System-card practice

StepFun publishes technical reports on arXiv for the 2.5 family (2026-05-22) and for StepAudio 3 Realtime (2026-09-12, revised 2026-09-19). It publishes no model card or system card with safety results for these models. The API reference warns that Artificial Analysis leaderboard figures come from internal parameter configurations, that actual API behaviour may differ, and that the settings will be opened up in later API versions [step-paper-3] [step-paper-25] [step-realtime-api].

## Family-wide behaviour

- Real-time conversation supports Chinese and English only. StepFun labels other languages as preview for its speech synthesis and recognition models. The 2.5 model page says English only [step-audio-models] [step-realtime-api] [step-25-realtime].
- Both models share seven system voices. The API reference also accepts cloned voices; the 2.5 model page says only the seven listed IDs are valid for that model. The voice must be set before the model speaks and cannot change after. A value outside the list gives a 400 error [step-realtime-api] [step-25-realtime].
- Server VAD is off by default, with a silence setting of 100 ms [step-realtime-api].
- A preview model name retires when its paid version arrives [step-model-page-3].
- StepFun's lifecycle page lists retirements on 2026-07-08 (text, vision and image models) and a scheduled retirement on 2026-10-10 (image models). It lists no retirement of a speech model [step-lifecycle].
- Artificial Analysis lists StepAudio 3 Realtime at 99.7% on speech reasoning and 98.9% on conversational dynamics, with 8.83 seconds to first audio [aa-s2s].

## Open questions

- The price of the paid StepAudio 3 Realtime and the name of the production model.
- Whether Step-Audio R1.1 (Realtime) can be selected through the API.
- Which languages the 2.5 model supports.

## Sources

- [step-model-page-3] https://platform.stepfun.ai/docs/en/guides/models/stepaudio-3-realtime (kind L, read 2026-10-03)
- [step-25-realtime] https://platform.stepfun.ai/docs/en/guides/models/stepaudio-2.5-realtime (kind L, read 2026-10-03)
- [step-realtime-api] https://platform.stepfun.ai/docs/en/api-reference/realtime/chat (kind L, read 2026-10-03)
- [step-audio-models] https://platform.stepfun.ai/docs/en/guides/models/audio (kind L, read 2026-10-03)
- [step-pricing] https://platform.stepfun.ai/docs/en/guides/pricing/details (kind L, read 2026-10-03)
- [step-lifecycle] https://platform.stepfun.ai/docs/en/guides/model-migration (kind L, read 2026-10-03)
- [step-paper-3] https://arxiv.org/abs/2609.14005 (kind P, read 2026-10-03)
- [step-paper-25] https://arxiv.org/abs/2605.23463 (kind P, read 2026-10-03)
- [runtimewire-step] https://runtimewire.com/article/stepfun-stepaudio-3-five-audio-models (kind A, read 2026-10-03)
- [aa-s2s] https://artificialanalysis.ai/speech-to-speech (kind M, read 2026-10-03)
