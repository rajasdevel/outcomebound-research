---
last_checked: 2026-10-04
volatility: MONITOR (lineage, guides and API behaviour change at each release; prices and limits are VOLATILE and are held in the model cards)
sources:
  - https://docs.speechify.ai/build/guides/concepts/models
  - https://docs.speechify.ai/build/guides/text-to-speech/emotion-control
  - https://docs.speechify.ai/build/guides/text-to-speech/ssml
  - https://docs.speechify.ai/build/guides/text-to-speech/latency
  - https://docs.speechify.ai/llms.txt
  - https://speechify.ai/pricing
  - https://docs.speechify.ai/build/changelog/2026/5/9
  - https://docs.speechify.ai/build/changelog/2026/7/8
  - https://docs.speechify.ai/build/changelog/2026/8/5
  - https://artificialanalysis.ai/text-to-speech
---

# Speechify

Speechify sells a text-to-speech API, called SpeechifyAI Build, on its Simba models. A separate consumer reader app, speechify.com, is a different product. This folder holds the two live Simba models, which take an emotion tag in SSML. Everything here was read on 2026-10-04.

## Models and lineage

| Class | Model | Notes |
| --- | --- | --- |
| Speechify Simba | [Simba 3.2](simba-3.2.md) | English only; recommended for English; 56 ms median first byte per the maker [sp-models] [sp-latency] |
| Speechify Simba | [Simba 3.0](simba-3.0.md) | Six languages in seven locales; the API default [sp-models] |

- The Simba 1.6 models (`simba-english` and `simba-multilingual`) stop being selectable from API version 2026-09-21. From 2026-11-21 their ids are served by current models, and the audio changes. They have no file [sp-models].
- The maker's changelog makes `simba-3.0` available on 2026-05-09 and `simba-3.2` on 2026-07-08. From 2026-08-05 `simba-3.0` is the default when a request names no model. Artificial Analysis dates them 2026-02-19 and 2026-07-01 [sp-chlog-30] [sp-chlog-32] [sp-chlog-default] [aa-tts-board].
- `GET /v1/audio/models` also lists a dialogue model, Simba Dialogue 1.0 (`simba-dialogue-1.0`, English, endpoint `/v1/audio/dialogue`), that renders a speaker-attributed script as one conversation. The pages read do not document how to direct its delivery, so it has no file [sp-models].

## API surface

- **Endpoints.** `POST /v1/audio/speech` (2,000 characters), `POST /v1/audio/stream` and a stream with timestamps (20,000 characters), `GET /v1/audio/models` and voice cloning endpoints. Authentication is a Bearer key. API versions are dated and set by the `Speechify-Version` header [sp-limits] [sp-index].
- **Limits by plan.** Concurrent requests of 3, 15, 30, 60 and 100 from Free to Enterprise, shared by every synthesis endpoint [sp-limits].
- **Pricing.** Per character from a plan balance, one rate per plan: US$10 per 1M characters on Starter, US$8 on Pro and US$6 on Scale after the included characters; Free includes 500K characters a month [sp-pricing].

## Prompting guides

Speechify publishes pages on emotion control, SSML, latency, streaming, language support and cloning. Its emotion guide gives 13 emotions and four tips: match the words to the emotion, keep sentences short, use punctuation, combine with prosody and breaks [sp-emotion].

## System-card practice

Speechify publishes no system card in the pages read. It publishes dated API versions with deprecation windows and migration guides [sp-models].

## Family-wide behaviour

- Voice cloning on both models is zero-shot and needs a consent recording [sp-clone].
- The models page lists full support for SSML and emotion control on both Simba 3.2 and Simba 3.0 [sp-models].
- Artificial Analysis lists Simba 3.2 at a quality Elo of 1241.95 and Simba 3.0 at 1124.54 [aa-tts-board].

## Open questions

- How strongly each emotion tag acts, and how to direct Simba Dialogue 1.0.

## Sources

- [sp-models] https://docs.speechify.ai/build/guides/concepts/models (kind L, read 2026-10-04)
- [sp-emotion] https://docs.speechify.ai/build/guides/text-to-speech/emotion-control (kind L, read 2026-10-04)
- [sp-latency] https://docs.speechify.ai/build/guides/text-to-speech/latency (kind L, read 2026-10-04)
- [sp-limits] https://docs.speechify.ai/build/guides/concepts/api-limits (kind L, read 2026-10-04)
- [sp-clone] https://docs.speechify.ai/build/guides/voice-cloning/overview (kind L, read 2026-10-04)
- [sp-index] https://docs.speechify.ai/llms.txt (kind L, read 2026-10-04)
- [sp-pricing] https://speechify.ai/pricing (kind L, read 2026-10-04)
- [sp-chlog-30] https://docs.speechify.ai/build/changelog/2026/5/9 (kind L, read 2026-10-04)
- [sp-chlog-32] https://docs.speechify.ai/build/changelog/2026/7/8 (kind L, read 2026-10-04)
- [sp-chlog-default] https://docs.speechify.ai/build/changelog/2026/8/5 (kind L, read 2026-10-04)
- [aa-tts-board] https://artificialanalysis.ai/text-to-speech (kind M, read 2026-10-04)
