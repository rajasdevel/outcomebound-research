---
last_checked: 2026-10-04
volatility: MONITOR (lineage, guides and API behaviour change at each release; prices and limits are VOLATILE and are held in the model card)
sources:
  - https://docs.inworld.ai/tts/tts
  - https://docs.inworld.ai/tts/tts-models
  - https://docs.inworld.ai/tts/capabilities/steering
  - https://docs.inworld.ai/release-notes/tts
  - https://docs.inworld.ai/portal/billing
  - https://inworld.ai/pricing
  - https://artificialanalysis.ai/text-to-speech
  - https://replicate.com/inworld/tts-1.5-max
---

# Inworld

Inworld sells Realtime TTS (text to speech), Realtime STT, a Realtime speech-to-speech API and a router for LLMs. This folder holds the one Inworld speech model that can be directed with natural-language instructions. Everything here was read on 2026-10-04.

## Models and lineage

| Class | Model | Notes |
| --- | --- | --- |
| Inworld Realtime TTS | [Realtime TTS-2](inworld-tts-2.md) | `inworld-tts-2`, released 2026-05-05; natural-language steering, 200+ languages [iw-release] |

- **Realtime TTS-2 Flash** (`inworld-tts-2-flash`, 2026-08-09) is the fast model of the same generation. It ignores steering instructions and plays non-verbal tags only, so it has no file [iw-release] [iw-steering].
- **TTS 1.5** (`inworld-tts-1.5-max` and `-mini`, 2026-01-21) is the previous generation. Inworld lists it as deprecated and not recommended for new projects. It has no steering. A Replicate model page for `tts-1.5-max` (class A) lists bracket markups (six emotions, `[laughing]`, `[whispering]` and six non-verbal sounds), but the maker's audio-markups page now redirects to a login, so no public maker page documents them. It has no file [iw-models] [replicate-iw15]. `inworld-tts-1` and `inworld-tts-1-max` were discontinued on 2026-06-15, and requests to them are routed to newer models [iw-release] [iw-models].

## API surface

- **Endpoints.** Unary (2,000 characters), streaming over HTTP (4,000), WebSocket with contexts, async and batch jobs (preview) and an OpenAI-compatible `POST /v1/audio/speech` (since 2026-09-11) [iw-release].
- **Voices.** Built-in voices, instant and professional cloning, voice design, sharing and export [iw-intro].
- **Pricing.** Per million characters, by plan [iw-pricing].
- **Neighbouring products.** The Realtime API for speech-to-speech uses TTS-2 for speech. Its guide on naturalness shows the settings Inworld pairs with steering [iw-natural].

## Prompting guides

Inworld publishes a steering guide, a guide on generating natural speech (voice choice, writing for the ear, steering, context, normalisation, LLM prompting), voice design, pause controls, inline pronunciation and verbatim tags [iw-steering] [iw-guide].

## System-card practice

Inworld publishes no system card in the pages read. It publishes dated release notes that name behaviour changes and the migration step [iw-release].

## Family-wide behaviour

- Steering applies only on `inworld-tts-2`. Non-verbal tags work on both TTS-2 models [iw-steering].
- Artificial Analysis lists Realtime TTS-2 at a quality Elo of 1251.26 [aa-tts-board].

## Open questions

- Whether Inworld will extend steering to TTS-2 Flash.

## Sources

- [iw-intro] https://docs.inworld.ai/tts/tts (kind L, read 2026-10-04)
- [iw-models] https://docs.inworld.ai/tts/tts-models (kind L, read 2026-10-04)
- [iw-steering] https://docs.inworld.ai/tts/capabilities/steering (kind L, read 2026-10-04)
- [iw-guide] https://docs.inworld.ai/tts/best-practices/generating-speech (kind L, read 2026-10-04)
- [iw-natural] https://docs.inworld.ai/realtime/usage/naturalness (kind L, read 2026-10-04)
- [iw-release] https://docs.inworld.ai/release-notes/tts (kind L, read 2026-10-04)
- [iw-pricing] https://inworld.ai/pricing (kind L, read 2026-10-04)
- [aa-tts-board] https://artificialanalysis.ai/text-to-speech (kind M, read 2026-10-04)
- [replicate-iw15] https://replicate.com/inworld/tts-1.5-max (kind A, read 2026-10-04)
