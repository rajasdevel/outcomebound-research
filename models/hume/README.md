---
last_checked: 2026-10-03
volatility: VOLATILE (the sunset notice, versions, prices and API behaviour change often)
sources:
  - https://dev.hume.ai/audio-decisions/docs/overview (read 2026-11-24)
  - https://dev.hume.ai/audio-decisions/changelog (read 2026-11-24)
  - https://dev.hume.ai/docs/speech-to-speech-evi/overview
  - https://dev.hume.ai/docs/speech-to-speech-evi/configuration/evi-version
  - https://dev.hume.ai/docs/speech-to-speech-evi/guides/prompting
  - https://dev.hume.ai/docs/speech-to-speech-evi/faq
  - https://dev.hume.ai/reference/speech-to-speech-evi/chat
  - https://dev.hume.ai/changelog
  - https://www.hume.ai/pricing
  - https://artificialanalysis.ai/speech-to-speech
  - https://dev.hume.ai/llms.txt
  - https://dev.hume.ai/docs/text-to-speech-tts/overview
  - https://dev.hume.ai/docs/text-to-speech-tts/acting-instructions
  - https://dev.hume.ai/docs/voice/voice-design
  - https://dev.hume.ai/docs/text-to-speech-tts/continuation
  - https://www.hume.ai/blog/octave-the-first-text-to-speech-model-that-understands-what-its-saying
---

# Hume AI

This folder records Hume's Empathic Voice Interface (EVI) and Octave text-to-speech models from before the scheduled API sunset. Hume announced on 2026-10-02 that both APIs were due to end on 2026-11-13. The model details below are from 2026-10-03, with the Octave text read on 2026-10-04.

The October notice gave 12:01 a.m. EST as the end of access and said account data would be
deleted after that date [hume-overview] [hume-changelog].

> **Note.** On 2026-11-24 the former [EVI overview](https://dev.hume.ai/docs/speech-to-speech-evi/overview)
> and [TTS overview](https://dev.hume.ai/docs/text-to-speech-tts/overview) both redirected to Hume's
> Audio Decisions API docs. Hume's new changelog dates that API's launch to 2026-11-02.
> The new documentation describes an API that accepts audio and can return probability estimates
> (L). Access to the former speech APIs
> after the scheduled sunset is `UNVERIFIED`.

## Models and lineage

| Class | Version | Model | Notes |
| --- | --- | --- | --- |
| Hume EVI | 4-mini | [Hume EVI 4-mini](evi-4-mini.md) | 2025-10-03. 11 languages, needs a supplemental language model, about 100 ms faster per response than EVI 3 [hume-changelog] [hume-evi-version] |
| Hume EVI | 3 | [Hume EVI 3](evi-3.md) | 2025-07-18 in the API. Native speech-language models `hume-evi-3` and `hume-evi-3-websearch`; the default version [hume-changelog] [hume-evi-version] |
| Hume Octave | 1 | [Hume Octave 1](octave-1.md) | 2025-02-26. English and Spanish; takes natural-language acting instructions in `description`; voice design needs this version [hume-blog-octave] [hume-tts-overview] [hume-voice-design] |

EVI 1 and EVI 2 ended support on 2025-08-30 and have no file. Octave is Hume's text-to-speech API. It synthesises speech only and holds no conversation, so Octave 1 is in this library as a voice actor model: a speech synthesis model whose delivery a user directs with natural-language instructions or inline tags. Octave 2 (preview since 2025-10-03; 11 languages, about 100 ms model latency) has no file, because Hume lists acting instructions for it as coming soon and its only delivery controls beyond the voice are `speed` and `trailing_silence`. Hume ends the TTS API with EVI on 2026-11-13 [hume-changelog] [hume-tts-overview] [hume-acting].

## API surface

- **Protocol.** A WebSocket at `wss://api.hume.ai/v0/evi/chat`. A config (versioned, with its `evi_version`, voice, system prompt, language model, tools, timeouts, turn detection and interruption settings) is chosen by `config_id` when a chat starts. Without a config, EVI 3 runs [hume-chat-ref] [hume-evi-version].
- **Resources.** Prompts, tools and configs are versioned resources in the API. Dynamic variables fill values into a prompt at run time. A control plane lets a trusted backend change session settings during a chat [hume-prompting] [hume-llms-index].
- **Language models.** EVI's own speech-language model, and supplemental models through partner APIs: Anthropic, OpenAI, Google and Fireworks per the overview; a changelog entry of 2025-07-18 adds Claude Sonnet 4, Llama 4 Maverick, Qwen3 32B, DeepSeek R1-Distill and Kimi K2 through SambaNova and Groq. The user may send their own provider key in the session settings [hume-overview] [hume-changelog] [hume-faq].
- **Audio.** Linear 16 PCM (with a `session_settings` message) or WebM, in; base64 WAV at 48 kHz, out. Mu-law is not supported [hume-audio-guide] [hume-chat-ref].
- **Integrations.** A Twilio guide covers phone calls. The documentation index lists SDK quickstarts for TypeScript, Next.js, Python and .NET [hume-llms-index].
- **Pricing.** By plan and month: Free (US$0, 5 EVI minutes), Starter (US$3, 40 minutes), Creator (US$7 for the first month, then US$14, 200 minutes), Pro (US$70, 1,200), Scale (US$200, 5,000), Business (US$500, 12,500) and Enterprise on request. The page shows a per-minute figure beside each paid plan (US$0.07, 0.07, 0.06, 0.05, 0.04) and a separate line for additional EVI 3 use (US$0.06, 0.05, 0.04 on the Pro, Scale and Business plans). The text read does not say how these figures relate. Concurrency limits depend on the plan [hume-pricing] [hume-faq].
- **Octave TTS API.** HTTP (`/v0/tts`, `/v0/tts/file`), streamed HTTP (`/v0/tts/stream/json` and `/stream/file`) and a WebSocket (`/v0/tts/stream/input`). A request lists `utterances` with `text`, `voice`, `description`, `speed` and `trailing_silence`, and picks Octave 1 or 2 with `version`. Limits are 5,000 characters of text and 1,000 characters of description per utterance and 5 generations per request. Formats are MP3, WAV and PCM. Plans sell characters: Free 10,000 up to Business 10,000,000 a month; additional characters cost US$0.15 per 1,000 on Creator down to US$0.05 on Business [hume-tts-overview] [hume-pricing].

## Prompting guides

Hume publishes a prompt engineering guide for EVI, a system-prompt page, and prompt examples (including the default prompts) on GitHub. The guide covers what prompts can and cannot do, general rules, writing for voice, expressive prompting that reacts to the user's vocal expression, dynamic variables, and latency-friendly prompts. It says to keep system prompts small because a supplemental model reads the whole prompt every turn [hume-prompting].

For Octave, Hume publishes an acting-instructions guide, a voice design guide with sample voice prompts, a voice cloning guide, a continuation guide and a timestamps guide. The acting-instructions guide advises short instructions of about 100 characters, precise emotions, an emotion paired with a delivery style, pacing words, a named audience, and the `speed` parameter instead of words for rate [hume-acting] [hume-voice-design] [hume-continuation].

## System-card practice

Hume publishes no system card or model card for EVI in the sources read. Its FAQ explains that expression labels are the confidence of its prosody model that a listener would hear that expression, and are not claims about what the speaker feels. The prompting guide says prompts cannot override the safety features of EVI or the supplemental model [hume-faq] [hume-prompting].

## Family-wide behaviour

- Both versions are interruptible and turn-based. They use VAD with tunable silence, threshold, padding and minimum-interruption settings. They do not describe themselves as full-duplex [hume-turn-detection] [hume-interruption].
- Both limit a chat to 1,800 seconds at most [hume-timeouts].
- EVI 3 requires a voice in the config and has no default voice. EVI 4-mini uses Octave 2 for speech, together with a supplemental language model [hume-evi-version] [hume-changelog].
- Artificial Analysis lists no Hume model on its Speech to Speech page (read 2026-10-03), so no independent number exists [aa-s2s].
- Octave 1 takes the `description` field and Octave 2 does not yet. Voices designed on Octave 1 work on Octave 2. A request with `version` 2 must name a voice [hume-acting] [hume-voice-design].
- Artificial Analysis lists Octave TTS (version 1) at a quality Elo of 1036.11 and Octave 2 at 1051.32 on its text-to-speech page (read 2026-10-04) [aa-tts-board].

## Open questions

- Whether any former EVI or TTS customers still have endpoint access after 2026-11-13.
- The languages of EVI 3: the pages disagree.
- Whether the historical Octave 2 preview ever added `description`.

## Sources

- [hume-overview] https://dev.hume.ai/docs/speech-to-speech-evi/overview (kind L, read 2026-10-03)
- [hume-evi-version] https://dev.hume.ai/docs/speech-to-speech-evi/configuration/evi-version (kind L, read 2026-10-03)
- [hume-prompting] https://dev.hume.ai/docs/speech-to-speech-evi/guides/prompting (kind L, read 2026-10-03)
- [hume-faq] https://dev.hume.ai/docs/speech-to-speech-evi/faq (kind L, read 2026-10-03)
- [hume-chat-ref] https://dev.hume.ai/reference/speech-to-speech-evi/chat (kind L, read 2026-10-03)
- [hume-audio-guide] https://dev.hume.ai/docs/speech-to-speech-evi/guides/audio (kind L, read 2026-10-03)
- [hume-turn-detection] https://dev.hume.ai/docs/speech-to-speech-evi/configuration/turn-detection (kind L, read 2026-10-03)
- [hume-interruption] https://dev.hume.ai/docs/speech-to-speech-evi/configuration/interruption (kind L, read 2026-10-03)
- [hume-timeouts] https://dev.hume.ai/docs/speech-to-speech-evi/configuration/timeouts (kind L, read 2026-10-03)
- [hume-changelog] https://dev.hume.ai/changelog (kind L, read 2026-10-03)
- [hume-pricing] https://www.hume.ai/pricing (kind L, read 2026-10-03)
- [hume-llms-index] https://dev.hume.ai/llms.txt (kind L, read 2026-10-03)
- [aa-s2s] https://artificialanalysis.ai/speech-to-speech (kind M, read 2026-10-03)
- [hume-tts-overview] https://dev.hume.ai/docs/text-to-speech-tts/overview (kind L, read 2026-10-04)
- [hume-acting] https://dev.hume.ai/docs/text-to-speech-tts/acting-instructions (kind L, read 2026-10-04)
- [hume-voice-design] https://dev.hume.ai/docs/voice/voice-design (kind L, read 2026-10-04)
- [hume-continuation] https://dev.hume.ai/docs/text-to-speech-tts/continuation (kind L, read 2026-10-04)
- [hume-blog-octave] https://www.hume.ai/blog/octave-the-first-text-to-speech-model-that-understands-what-its-saying (kind L, read 2026-10-04)
- [aa-tts-board] https://artificialanalysis.ai/text-to-speech (kind M, read 2026-10-04)
