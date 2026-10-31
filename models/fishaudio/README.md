---
last_checked: 2026-10-04
volatility: VOLATILE (the free tier, prices and model lineup change often)
sources:
  - https://docs.fish.audio/developer-guide/models-pricing/models-overview
  - https://docs.fish.audio/developer-guide/models-pricing/pricing-and-rate-limits
  - https://docs.fish.audio/developer-guide/core-features/emotions
  - https://docs.fish.audio/api-reference/openapi.json
  - https://fish.audio/blog/s2-1-pro-free-api/
  - https://huggingface.co/fishaudio/s2-pro
  - https://artificialanalysis.ai/text-to-speech
  - https://huggingface.co/fishaudio/drama-3 (read 2026-10-31)
  - https://huggingface.co/fishaudio/drama-3/blob/main/LICENSE (read 2026-10-31)
  - https://huggingface.co/api/models/fishaudio/drama-3/commits/main (read 2026-10-31)
  - https://docs.fish.audio/features/text-to-speech/drama-3 (read 2026-10-31)
  - https://docs.fish.audio/api-reference/openapi.json (read 2026-10-31)
---

# Fish Audio

Fish Audio sells a text-to-speech API, a speech-to-text API (`transcribe-1-pro` and `transcribe-1`), voice cloning, voice design and a voice-agent platform. This folder holds the two S2 text-to-speech models, which a user directs with natural-language cues in square brackets. Everything here was read on 2026-10-04.

## Models and lineage

| Class | Model | Notes |
| --- | --- | --- |
| Fish Audio S Pro | [S2.1 Pro](s2.1-pro.md) | Hosted; 2026-06-23; recommended production model; 83 languages [fish-models] [fish-blog-s21] |
| Fish Audio S Pro | [S2 Pro](s2-pro.md) | 2026-03-09; open weights under a research licence; 80+ languages [fish-hf-s2] |

- `s2.1-pro-free` is the same model as `s2.1-pro` at no cost for development. It has no latency or data-processing guarantees [fish-models].
- S1 (`s1`) uses parenthesis cues, a fixed list of 64+ expressions and no multi-speaker mode. It stays available for existing integrations and has no file here [fish-models].
- **Drama 3 [as-of 2026-10-31].** `drama-3` is now a hosted model with its own docs page, and the OpenAPI schema lists it in the `model` header values; `drama-3-preview` no longer appears there. Drama 3 takes plain-language directions in square brackets, paired word tags such as `<whisper>` and `<emphasis>`, phoneme tags and speaker tags. It costs US$50 per million UTF-8 bytes, with a launch price of US$10 until 2026-11-12 17:00 UTC [fish-drama3-docs] [fish-openapi-1031]. Its weights are on Hugging Face as `fishaudio/drama-3`: a mixture of experts with 35B parameters and 3B active per token, and speaker tags for up to 16 characters in one text. Hugging Face shows the repository created on 2026-10-01; its commit history starts on 2026-10-13, and the weights were uploaded again on 2026-10-29. The card metadata names the `fish-audio-research-license`, but the LICENSE file is the Fish Audio Community License 1.0 (2026-10-13). That licence allows research and non-commercial use, allows commercial use while annual revenue is below US$500,000, and requires a separate licence for a hosted speech service [hf-drama3] [hf-drama3-commits] [hf-drama3-license]. It has no file yet.

## API surface

- **Endpoint.** `POST /v1/tts` with a Bearer key and the model in a `model` header, not in the body. A missing or unknown header value serves `s2.1-pro`. A WebSocket live endpoint takes `start`, `text`, `flush` and `stop` events [fish-openapi].
- **Voices.** Saved voice models, inline references (MessagePack), a voice library, and voice design candidates [fish-openapi] [fish-voice-design].
- **Pricing and limits.** Per million UTF-8 bytes. Concurrent request limits of 5, 15 and 50 unlock at US$100 and US$1,000 of prepaid spend [fish-pricing].

## Prompting guides

Fish Audio publishes an emotion control page (tags, placement rules, layering, dos and don'ts), a fine-grained control page (phonemes, pause words, effects), a models overview and a voice design guide [fish-emotions] [fish-fine].

## System-card practice

Fish Audio publishes a model card and an arXiv report for the open S2 Pro model. It publishes no system card for the hosted S2.1 Pro in the pages read [fish-hf-s2].

## Family-wide behaviour

- Brackets for S2 models and parentheses for S1 [fish-models].
- Artificial Analysis lists S2.1 Pro at a quality Elo of 1141.15 and S2 Pro at 1117.15 [aa-tts-board].

## Open questions

- The text limit per request. [as-of 2026-10-31] Which licence governs the Drama 3 weights when the card metadata and the LICENSE file differ.

## Sources

- [fish-models] https://docs.fish.audio/developer-guide/models-pricing/models-overview (kind L, read 2026-10-04)
- [fish-emotions] https://docs.fish.audio/developer-guide/core-features/emotions (kind L, read 2026-10-04)
- [fish-fine] https://docs.fish.audio/developer-guide/core-features/fine-grained-control (kind L, read 2026-10-04)
- [fish-openapi] https://docs.fish.audio/api-reference/openapi.json (kind L, read 2026-10-04)
- [fish-pricing] https://docs.fish.audio/developer-guide/models-pricing/pricing-and-rate-limits (kind L, read 2026-10-04)
- [fish-voice-design] https://docs.fish.audio/features/voice-design (kind L, read 2026-10-04)
- [fish-blog-s21] https://fish.audio/blog/s2-1-pro-free-api/ (kind L, read 2026-10-04)
- [fish-drama3-docs] https://docs.fish.audio/features/text-to-speech/drama-3 (kind L, read 2026-10-31)
- [fish-openapi-1031] https://docs.fish.audio/api-reference/openapi.json (kind L, read 2026-10-31)
- [hf-drama3] https://huggingface.co/fishaudio/drama-3 (kind L, read 2026-10-31)
- [hf-drama3-commits] https://huggingface.co/api/models/fishaudio/drama-3/commits/main (kind L, read 2026-10-31)
- [hf-drama3-license] https://huggingface.co/fishaudio/drama-3/blob/main/LICENSE (kind L, read 2026-10-31)
- [fish-hf-s2] https://huggingface.co/fishaudio/s2-pro (kind L, read 2026-10-04)
- [aa-tts-board] https://artificialanalysis.ai/text-to-speech (kind M, read 2026-10-04)
