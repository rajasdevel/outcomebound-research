---
last_checked: 2026-10-04
volatility: MONITOR (lineage, guides and API behaviour change at each release; prices and limits are VOLATILE and are held in the model cards)
sources:
  - https://docs.cartesia.ai/build-with-cartesia/tts-models/latest
  - https://docs.cartesia.ai/build-with-cartesia/tts-models/older-models
  - https://docs.cartesia.ai/build-with-cartesia/tts-models/api-changes
  - https://docs.cartesia.ai/build-with-cartesia/capability-guides/volume-speed-emotion
  - https://docs.cartesia.ai/build-with-cartesia/capability-guides/ssml-tags
  - https://docs.cartesia.ai/build-with-cartesia/capability-guides/prompting-tips
  - https://docs.cartesia.ai/changelog/2026
  - https://docs.cartesia.ai/changelog/2025
  - https://www.cartesia.ai/pricing
  - https://www.cartesia.ai/sonic
  - https://artificialanalysis.ai/text-to-speech
---

# Cartesia

Cartesia sells Sonic, a family of text-to-speech models, Ink, a speech-to-text model, and Managed Agents that run both with an LLM. This folder holds the two current Sonic generations, the models whose delivery a user can direct with inline tags. Everything here was read on 2026-10-04.

## Models and lineage

| Class | Model | Notes |
| --- | --- | --- |
| Cartesia Sonic | [Sonic 3.6](sonic-3.6.md) | Generally available 2026-08-27; 44 languages; update of 3.5 [cart-chlog26] |
| Cartesia Sonic | [Sonic 3.5](sonic-3.5.md) | Snapshot 2026-05-04; 42 languages; stable, older [cart-older] |

- Sonic 3 launched on 2025-10-27 with volume, speed and emotion controls and 42 languages. Its snapshot of that date stops on 2026-10-20, with `sonic-2` and `sonic-turbo`. A January 2026 snapshot of `sonic-3` stays stable. Sonic 3 has no file here, because this library keeps two generations [cart-chlog25] [cart-sunsets].
- The `sonic`, `sonic-english` and `sonic-multilingual` ids stopped on 2026-06-01 [cart-sunsets].
- Sonic is a directable class only in a limited sense. It has a fixed list of 58 emotions (English only, beta), `[laughter]`, and speed and volume guidance. It does not take free-form instructions.

## API surface

- **Endpoints.** Bytes (HTTP) at `https://api.cartesia.ai`, SSE and WebSocket. Only Bytes returns wav or mp3. The Bytes reference takes a `Cartesia-Version` header; the 2026-08-14 version cleaned up multilingual voice fields [cart-bytes] [cart-chlog26].
- **Model ids.** An alias per generation (`sonic-3.6`), dated snapshots that never change, and `sonic-preview` for the beta [cart-sonic36].
- **Voices.** 500+ built-in voices, instant and professional clones, and sharing of custom voices across organisations [cart-voices].
- **Pricing.** Credits, one per character, on monthly plans [cart-pricing].

## Prompting guides

Cartesia publishes pages on prompting tips (with a starter system prompt for LLM-written text), volume, speed and emotion, SSML-like tags, buffering and continuations, custom pronunciations and text normalisation. The common thread is that well-punctuated text in a normal written form needs little else, and that heavy pre-processing hurts. Controls are guidance that the model weighs against the text [cart-prompting] [cart-emotion].

## System-card practice

Cartesia publishes no system card or model card for Sonic in the pages read. It publishes a changelog by month with what changed and what customers must do to migrate [cart-chlog26].

## Family-wide behaviour

- Speed and volume were off on the April 2026 preview of 3.5 and back at general availability in May 2026 [cart-chlog26].
- Professional voice clones stay tied to the base model they were trained on, unless the maker says otherwise for a generation [cart-chlog26].
- Artificial Analysis lists Sonic 3.6 at a quality Elo of 1278.08 and Sonic 3.5 at 1190.35 [aa-tts-board].

## Open questions

- Which snapshots accept emotion tags, and in which languages.
- A latency figure for Sonic 3.6 with a stated method.

## Sources

- [cart-sonic36] https://docs.cartesia.ai/build-with-cartesia/tts-models/latest (kind L, read 2026-10-04)
- [cart-older] https://docs.cartesia.ai/build-with-cartesia/tts-models/older-models (kind L, read 2026-10-04)
- [cart-sunsets] https://docs.cartesia.ai/build-with-cartesia/tts-models/api-changes (kind L, read 2026-10-04)
- [cart-emotion] https://docs.cartesia.ai/build-with-cartesia/capability-guides/volume-speed-emotion (kind L, read 2026-10-04)
- [cart-prompting] https://docs.cartesia.ai/build-with-cartesia/capability-guides/prompting-tips (kind L, read 2026-10-04)
- [cart-voices] https://docs.cartesia.ai/build-with-cartesia/capability-guides/choosing-a-voice (kind L, read 2026-10-04)
- [cart-bytes] https://docs.cartesia.ai/api-reference/tts/bytes (kind L, read 2026-10-04)
- [cart-chlog26] https://docs.cartesia.ai/changelog/2026 (kind L, read 2026-10-04)
- [cart-chlog25] https://docs.cartesia.ai/changelog/2025 (kind L, read 2026-10-04)
- [cart-pricing] https://www.cartesia.ai/pricing (kind L, read 2026-10-04)
- [aa-tts-board] https://artificialanalysis.ai/text-to-speech (kind M, read 2026-10-04)
