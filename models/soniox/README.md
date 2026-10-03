---
last_checked: 2026-10-04
volatility: MONITOR (lineage, guides and API behaviour change at each release; prices and limits are VOLATILE and are held in the model card)
sources:
  - https://soniox.com/docs/tts/models
  - https://soniox.com/docs/tts/concepts/emotion-and-tone
  - https://soniox.com/docs/tts/rt/limits-and-quotas
  - https://soniox.com/pricing
  - https://artificialanalysis.ai/text-to-speech
---

# Soniox

Soniox sells speech-to-text and text-to-speech APIs. This folder holds its real-time text-to-speech model. Everything here was read on 2026-10-04.

## Models and lineage

| Class | Model | Notes |
| --- | --- | --- |
| Soniox TTS Real-Time | [TTS Real-Time v2](tts-rt-v2.md) | `tts-rt-v2`, generally available 2026-08-11 [so-models] |

- `tts-rt-v1` reached preview on 2026-04-23 and general availability on 2026-04-29. It was removed on 2026-08-31. Requests to it now go to v2. It has no file [so-models].

## API surface

- **Endpoints.** A real-time WebSocket API with several streams per connection and a REST API for one-shot generation. Regions are US, EU, JP and IN [so-models] [so-rt].
- **Limits.** Defaults of 100 requests a minute and 3 concurrent streams or requests. Each stream or response holds at most 2 minutes of generated audio [so-limits-rt] [so-limits-rest].
- **Pricing.** Token pricing for text in and audio out [so-pricing].

## Prompting guides

Soniox publishes one page on emotion and tone (audio tags and text formatting), a page on speech speed and a page on voices and cloning [so-tone] [so-speed].

## System-card practice

Soniox publishes no system card in the pages read. Its models page carries a changelog with deprecation dates [so-models].

## Family-wide behaviour

- Audio tags are written in English even for other languages [so-tone].
- Artificial Analysis lists the model at a quality Elo of 1178.92 [aa-tts-board].

## Open questions

- A latency figure and the behaviour of tags outside the documented list.

## Sources

- [so-models] https://soniox.com/docs/tts/models (kind L, read 2026-10-04)
- [so-tone] https://soniox.com/docs/tts/concepts/emotion-and-tone (kind L, read 2026-10-04)
- [so-speed] https://soniox.com/docs/tts/concepts/speech-speed (kind L, read 2026-10-04)
- [so-rt] https://soniox.com/docs/tts/rt/real-time-generation (kind L, read 2026-10-04)
- [so-limits-rt] https://soniox.com/docs/tts/rt/limits-and-quotas (kind L, read 2026-10-04)
- [so-limits-rest] https://soniox.com/docs/tts/rest-api/limits-and-quotas (kind L, read 2026-10-04)
- [so-pricing] https://soniox.com/pricing (kind L, read 2026-10-04)
- [aa-tts-board] https://artificialanalysis.ai/text-to-speech (kind M, read 2026-10-04)
