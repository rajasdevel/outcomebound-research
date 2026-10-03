---
last_checked: 2026-10-04
volatility: MONITOR (lineage, guides and API behaviour change at each release; prices are VOLATILE)
sources:
  - https://docs.camb.ai/models
  - https://docs.camb.ai/choosing-a-model
  - https://docs.camb.ai/tutorials/emotional-voice-control
  - https://docs.camb.ai/api-reference/endpoint/create-tts-stream
  - https://www.camb.ai/blog-post/camb-ai-unveils-mars8-the-first-family-of-tts-models
  - https://www.camb.ai/pricing
---

# CAMB.AI

CAMB.AI sells a text-to-speech API on its MARS 8 family, plus translation and dubbing products, and publishes older open-source MARS models. This folder holds the one MARS 8 model that takes emotion and delivery direction. Everything here was read on 2026-10-04.

## Models and lineage

| Class | Model | Notes |
| --- | --- | --- |
| CAMB.AI MARS Instruct | [MARS-Instruct](mars-instruct.md) | `mars-instruct`, 1.2B parameters, offline, 142 locales [camb-models] |

- MARS 8 was announced on 2026-01-20 as a family of four models: Flash (real time), Pro (expressive dubbing), Instruct and Nano (50M parameters, on device) [camb-blog].
- Beta models `mars-8.1-flash-beta` and `mars-8.1-pro-beta` cover 312 languages and add six non-verbal tags and English phoneme overrides, with no emotion control. They have no file [camb-models] [camb-emotion].
- `mars-flash` and `mars-pro` have no emotion or prosody control [camb-choose].
- MARS 6 Turbo and MARS 5 are open-source and older [camb-open].

## API surface

- **Endpoint.** A streaming POST for text-to-speech with `speech_model`, a live WebSocket, voice-from-description and custom voice endpoints, and Python and TypeScript SDKs. A language the model does not support returns HTTP 422 with the allowed locales [camb-stream] [camb-index].
- **Pricing.** Credit plans [camb-pricing].

## Prompting guides

CAMB.AI publishes a tutorial on emotional voice control (tags, ladders, `user_instructions`, pauses) and a guide on choosing a model [camb-emotion] [camb-choose].

## System-card practice

CAMB.AI publishes no system card in the pages read.

## Family-wide behaviour

- `user_instructions` works only with `mars-instruct` [camb-models].
- Output formats differ by model [camb-stream].

## Open questions

- Adherence of tags and instructions, and the price per character.

## Sources

- [camb-models] https://docs.camb.ai/models (kind L, read 2026-10-04)
- [camb-choose] https://docs.camb.ai/choosing-a-model (kind L, read 2026-10-04)
- [camb-emotion] https://docs.camb.ai/tutorials/emotional-voice-control (kind L, read 2026-10-04)
- [camb-stream] https://docs.camb.ai/api-reference/endpoint/create-tts-stream (kind L, read 2026-10-04)
- [camb-open] https://docs.camb.ai/open-source (kind L, read 2026-10-04)
- [camb-index] https://docs.camb.ai/llms.txt (kind L, read 2026-10-04)
- [camb-pricing] https://www.camb.ai/pricing (kind L, read 2026-10-04)
- [camb-blog] https://www.camb.ai/blog-post/camb-ai-unveils-mars8-the-first-family-of-tts-models (kind L, read 2026-10-04)
