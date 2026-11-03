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
  - https://docs.speechify.ai/build/changelog/2026/10/18 (read 2026-10-31)
  - https://docs.speechify.ai/build/changelog/2026/10/20 (read 2026-10-31)
  - https://docs.speechify.ai/build/changelog/2026/10/21 (read 2026-10-31)
  - https://speechify.ai/blog/simba-3-5 (read 2026-10-31)
  - https://docs.speechify.ai/build/guides/text-to-speech/streaming-text-input (read 2026-10-31)
---

# Speechify

Speechify sells a text-to-speech API, called SpeechifyAI Build, on its Simba models. A separate consumer reader app, speechify.com, is a different product. [as-of 2026-10-31] This folder holds the two newest Simba generations, [Simba 3.5](simba-3.5.md) and [Simba 3.2](simba-3.2.md). They take SSML for pauses, rate, pitch, volume and substitution; they accept an emotion tag and do not apply it [sp-ssml-1031]. Claims without their own date were read on 2026-10-04.

## Models and lineage

| Class | Model | Notes |
| --- | --- | --- |
| Speechify Simba | [Simba 3.5](simba-3.5.md) | [as-of 2026-10-31] 48 languages under one id; the recommended model from 2026-10-18, launched 2026-10-21 [sp-chlog-1018] [sp-chlog-1021] |
| Speechify Simba | [Simba 3.2](simba-3.2.md) | English only; 56 ms median first byte per the maker [sp-models] [sp-latency] |
| Speechify Simba | Simba 3.0 (no file) | [as-of 2026-10-31] Six languages in seven locales; still the API default and not deprecated. Its file was removed under the two-generation rule when Simba 3.5 shipped [sp-models-1031] |

- The Simba 1.6 models (`simba-english` and `simba-multilingual`) stop being selectable from API version 2026-09-21. From 2026-11-21 their ids are served by current models, and the audio changes. They have no file [sp-models]. [as-of 2026-10-31] From that day `simba-multilingual` is served by Simba 3.5, and `simba-english` by Simba 3.2 for English and by Simba 3.5 for other languages [sp-models-1031].
- The maker's changelog makes `simba-3.0` available on 2026-05-09 and `simba-3.2` on 2026-07-08. From 2026-08-05 `simba-3.0` is the default when a request names no model. Artificial Analysis dates them 2026-02-19 and 2026-07-01 [sp-chlog-30] [sp-chlog-32] [sp-chlog-default] [aa-tts-board].
- `GET /v1/audio/models` also lists a dialogue model, Simba Dialogue 1.0 (`simba-dialogue-1.0`, English, endpoint `/v1/audio/dialogue`), that renders a speaker-attributed script as one conversation. The pages read do not document how to direct its delivery, so it has no file [sp-models].

## API surface

- **Endpoints.** `POST /v1/audio/speech` (2,000 characters), `POST /v1/audio/stream` and a stream with timestamps (20,000 characters), `GET /v1/audio/models` and voice cloning endpoints. Authentication is a Bearer key. API versions are dated and set by the `Speechify-Version` header [sp-limits] [sp-index]. [as-of 2026-10-31] A WebSocket input stream, `GET /v1/audio/stream/ws`, takes text in pieces for `simba-3.0`, `simba-3.5` and `simba-3.2`; it is server-side only. `GET /v1/audio/models` marks a `recommended` model apart from the `default` one, and lists `pronunciation_languages` for each model [sp-ws] [sp-models-1031].
- **Limits by plan.** Concurrent requests of 3, 15, 30, 60 and 100 from Free to Enterprise, shared by every synthesis endpoint [sp-limits].
- **Pricing [as-of 2026-10-31].** Per character from a plan balance, at a rate per plan and per model. Simba 3.2 and 3.0: US$10 per 1M characters on Starter, US$8 on Pro and US$6 on Scale. Simba 3.5 lists at twice that (US$20, US$16 and US$12) and bills at the lower rates until 2026-11-21. SSML tags are not billed [sp-pricing-1031] [sp-chlog-1021].

## Prompting guides

Speechify publishes pages on emotion control, SSML, latency, streaming, language support and cloning. [as-of 2026-10-31] Its emotion guide now says the 13 emotion values act only on the retired Simba 1.6 models, and that the current models speak the text without the style. A pronunciation guide covers the `pronunciations` list of Simba 3.5 [sp-emotion-1031] [sp-pron].

## System-card practice

Speechify publishes no system card in the pages read. It publishes dated API versions with deprecation windows and migration guides [sp-models].

## Family-wide behaviour

- Voice cloning on the Simba 3 models is zero-shot and needs a consent recording [sp-clone]. [as-of 2026-10-31] Simba 3.5 also takes clones, with the same voice id in each of its languages [sp-models-1031].
- **SSML on the current models [as-of 2026-10-31].** Simba 3.5, 3.2 and 3.0 apply `break`, `prosody` rate, pitch and volume, and `sub`. They accept `emphasis` and the `speechify:style` emotion tag, return `200`, and do not apply them. Pitch and volume are applied from 2026-10-20. Only the retired Simba 1.6 models apply emotion styles [sp-ssml-1031] [sp-emotion-1031] [sp-chlog-1020].
- Artificial Analysis lists Simba 3.2 at a quality Elo of 1249.46 and Simba 3.0 at 1116.65 on 2026-10-31 (1241.95 and 1124.54 on 2026-10-04). It does not list Simba 3.5 [aa-tts-board-1031].

## Open questions

- How to direct Simba Dialogue 1.0. [as-of 2026-10-31] Whether a current model will apply emotion styles; and independent measurements of Simba 3.5.

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

Sources added for the claims dated 2026-10-31:

- [sp-models-1031] https://docs.speechify.ai/build/guides/concepts/models (kind L, read 2026-10-31)
- [sp-chlog-1018] https://docs.speechify.ai/build/changelog/2026/10/18 (kind L, read 2026-10-31)
- [sp-chlog-1020] https://docs.speechify.ai/build/changelog/2026/10/20 (kind L, read 2026-10-31)
- [sp-chlog-1021] https://docs.speechify.ai/build/changelog/2026/10/21 (kind L, read 2026-10-31)
- [sp-ssml-1031] https://docs.speechify.ai/build/guides/text-to-speech/ssml (kind L, read 2026-10-31)
- [sp-emotion-1031] https://docs.speechify.ai/build/guides/text-to-speech/emotion-control (kind L, read 2026-10-31)
- [sp-pron] https://docs.speechify.ai/build/guides/text-to-speech/pronunciation (kind L, read 2026-10-31)
- [sp-ws] https://docs.speechify.ai/build/guides/text-to-speech/streaming-text-input (kind L, read 2026-10-31)
- [sp-pricing-1031] https://speechify.ai/pricing (kind L, read 2026-10-31)
- [aa-tts-board-1031] https://artificialanalysis.ai/text-to-speech (kind M, read 2026-10-31)
