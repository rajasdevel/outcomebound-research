---
last_checked: 2026-10-03
volatility: MONITOR (lineage, guides and API behaviour change at each release)
sources:
  - https://docs.boson.ai/models/higgs-realtime/overview
  - https://docs.boson.ai/models/higgs-realtime/migrate-an-existing-integration
  - https://docs.boson.ai/pricing
  - https://docs.boson.ai/llms.txt
  - https://cryptobriefing.com/boson-ai-higgs-realtime-voice-model/
  - https://artificialanalysis.ai/speech-to-speech
  - https://docs.boson.ai/models/higgs-tts/overview
  - https://docs.boson.ai/models/higgs-tts/tags
  - https://huggingface.co/bosonai/higgs-tts-3-4b
  - https://www.boson.ai/blog/higgs-audio-v3-tts
---

# Boson AI

Boson AI sells the Higgs APIs: Higgs Realtime (speech-to-speech), Higgs TTS 3 (text-to-speech) and Higgs Avatar (talking-head video). This folder holds Higgs Realtime and Higgs TTS 3. Everything here was read on 2026-10-03, except the Higgs TTS text, which was read on 2026-10-04.

## Models and lineage

| Class | Model | Notes |
| --- | --- | --- |
| Higgs Realtime | [Higgs Realtime](higgs-realtime.md) | Full-duplex speech-to-speech over WebSocket, billed by token; the only realtime model of the maker [boson-overview] [boson-pricing] |
| Higgs TTS | [Higgs TTS 3](higgs-tts-3.md) | Text-to-speech with 43 inline control tags (emotion, style, sound effects, prosody) and zero-shot cloning; open weights (4B, research and non-commercial licence) and a hosted API at US$0.015 per 1,000 characters; released 2026-06-04; a voice actor model [boson-blog-tts3] [boson-pricing] |

Boson numbers no generation of Higgs Realtime. The documentation index lists Higgs Avatar, a talking-head video model; it is not a speech model and has no file. Higgs TTS 3 is a text-to-speech model that takes control tags, so it has a file. The generation before it, Higgs TTS 2 (Hugging Face `bosonai/higgs-tts-2-3b-base`, 2025-07-01, renamed from Higgs Audio v2), has no delivery tags or instruction in its card (a `scene` message sets only the recording setting and each speaker's gender), so it has no file [boson-tts-overview] [hf-higgs2]. The same index lists `higgs-stt-3.1`, a speech-to-text model that the realtime API can use for input transcription [boson-index] [cryptobriefing-higgs].

## API surface

- **Endpoint.** `wss://api.boson.ai/v1/realtime?model=higgs-realtime` with a bearer key, or an ephemeral key (prefix `bai-eph-`) in the `bai-client-secret.<key>` WebSocket subprotocol [boson-sessions].
- **Protocol.** Compatible with the GA OpenAI Realtime API, with listed differences: WebSocket only (WebRTC is in progress), no SIP or MCP, one output modality per response, and extra events for context summaries and session limits [boson-migrate].
- **Integrations.** A community Pipecat service (`pipecat-boson`); the docs list a LiveKit page with its support status [boson-index] [pipecat-boson].
- **Pricing.** Prepaid and usage-based: US$0.75 per million input tokens, US$0.25 cached input, US$4.50 output; US$10 of trial credit for new accounts [boson-pricing].
- **Text-to-speech.** `POST https://api.boson.ai/v1/audio/speech` with model `higgs-tts-3`, a Bearer key, an `input` of up to 5,000 characters (about 300 recommended), a preset `voice` or a `ref_audio` with `ref_text`, and an output format of mp3, opus, pcm, wav, aac or flac; streaming needs pcm. The same route runs on the open weights through SGLang-Omni or vLLM-Omni [boson-api-speech] [hf-higgs3].

## Prompting guides

Boson publishes pages on sessions, audio and voices, turn detection, tool use and migration. It publishes no separate guide on prompt wording. Its migration page advises a short, direct prompt, and its audio page says delivery (pace, tone, energy) is set through `instructions` [boson-migrate] [boson-audio]. For Higgs TTS 3, Boson publishes a tags page and a short prompting file with the weights. They list the 43 tags, say which tags colour a whole sentence and which are positional, and say to write the sound after each sound-effect tag [boson-tts-tags] [hf-higgs3-prompting].

## System-card practice

Boson publishes no system card or model card for Higgs Realtime in the pages read.

## Family-wide behaviour

- Server limits cannot change in `session.update`: an idle timeout after 5 minutes without user speech, a maximum session duration, a concurrency limit (close code 1013) and quota refusals (close code 4429) [boson-migrate] [boson-limits].
- Artificial Analysis lists Higgs Realtime at 68.6% on speech reasoning, 92.8% on conversational dynamics and 18.6% on tau-Voice (read 2026-10-03) [aa-s2s].
- The Higgs TTS 3 weights are free for research and non-commercial use; production, hosted or embedded use needs a separate licence, and a creator grant allows monetised content with credit to Boson [hf-higgs3].

## Open questions

- The release date of Higgs Realtime and its maximum session length.
- Which languages the realtime model supports.
- Time to first audio of the hosted Higgs TTS 3 API, and whether it is the same checkpoint as the open weights.

## Sources

- [boson-overview] https://docs.boson.ai/models/higgs-realtime/overview (kind L, read 2026-10-03)
- [boson-sessions] https://docs.boson.ai/models/higgs-realtime/guides/connections-and-sessions (kind L, read 2026-10-03)
- [boson-audio] https://docs.boson.ai/models/higgs-realtime/guides/audio-and-voices (kind L, read 2026-10-03)
- [boson-migrate] https://docs.boson.ai/models/higgs-realtime/migrate-an-existing-integration (kind L, read 2026-10-03)
- [boson-pricing] https://docs.boson.ai/pricing (kind L, read 2026-10-03)
- [boson-limits] https://docs.boson.ai/account-billing/usage-and-limits (kind L, read 2026-10-03)
- [boson-index] https://docs.boson.ai/llms.txt (kind L, read 2026-10-03)
- [pipecat-boson] https://docs.pipecat.ai/api-reference/server/services/s2s/boson (kind A, read 2026-10-03)
- [cryptobriefing-higgs] https://cryptobriefing.com/boson-ai-higgs-realtime-voice-model/ (kind A, read 2026-10-03)
- [aa-s2s] https://artificialanalysis.ai/speech-to-speech (kind M, read 2026-10-03)
- [boson-tts-overview] https://docs.boson.ai/models/higgs-tts/overview (kind L, read 2026-10-04)
- [boson-tts-tags] https://docs.boson.ai/models/higgs-tts/tags (kind L, read 2026-10-04)
- [boson-api-speech] https://docs.boson.ai/api-reference/audio/create-a-speech (kind L, read 2026-10-04)
- [boson-blog-tts3] https://www.boson.ai/blog/higgs-audio-v3-tts (kind L, read 2026-10-04)
- [hf-higgs3] https://huggingface.co/bosonai/higgs-tts-3-4b (kind L, read 2026-10-04)
- [hf-higgs3-prompting] https://huggingface.co/bosonai/higgs-tts-3-4b/raw/main/PROMPTING.md (kind L, read 2026-10-04)
- [hf-higgs2] https://huggingface.co/bosonai/higgs-tts-2-3b-base (kind L, read 2026-10-04)
