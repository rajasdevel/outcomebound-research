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
---

# Boson AI

Boson AI sells the Higgs APIs: Higgs Realtime (speech-to-speech), Higgs TTS 3 (text-to-speech) and Higgs Avatar (talking-head video). This folder holds Higgs Realtime. Everything here was read on 2026-10-03.

## Models and lineage

| Class | Model | Notes |
| --- | --- | --- |
| Higgs Realtime | [Higgs Realtime](higgs-realtime.md) | Full-duplex speech-to-speech over WebSocket, billed by token; the only realtime model of the maker [boson-overview] [boson-pricing] |

Boson numbers no generation. The documentation index lists Higgs TTS 3, which a trade article dates 2026-06-04, and Higgs Avatar; neither is a speech-to-speech model, so neither has a file. The same index lists `higgs-stt-3.1`, a speech-to-text model that the realtime API can use for input transcription [boson-index] [cryptobriefing-higgs].

## API surface

- **Endpoint.** `wss://api.boson.ai/v1/realtime?model=higgs-realtime` with a bearer key, or an ephemeral key (prefix `bai-eph-`) in the `bai-client-secret.<key>` WebSocket subprotocol [boson-sessions].
- **Protocol.** Compatible with the GA OpenAI Realtime API, with listed differences: WebSocket only (WebRTC is in progress), no SIP or MCP, one output modality per response, and extra events for context summaries and session limits [boson-migrate].
- **Integrations.** A community Pipecat service (`pipecat-boson`); the docs list a LiveKit page with its support status [boson-index] [pipecat-boson].
- **Pricing.** Prepaid and usage-based: US$0.75 per million input tokens, US$0.25 cached input, US$4.50 output; US$10 of trial credit for new accounts [boson-pricing].

## Prompting guides

Boson publishes pages on sessions, audio and voices, turn detection, tool use and migration. It publishes no separate guide on prompt wording. Its migration page advises a short, direct prompt, and its audio page says delivery (pace, tone, energy) is set through `instructions` [boson-migrate] [boson-audio].

## System-card practice

Boson publishes no system card or model card for Higgs Realtime in the pages read.

## Family-wide behaviour

- Server limits cannot change in `session.update`: an idle timeout after 5 minutes without user speech, a maximum session duration, a concurrency limit (close code 1013) and quota refusals (close code 4429) [boson-migrate] [boson-limits].
- Artificial Analysis lists Higgs Realtime at 68.6% on speech reasoning, 92.8% on conversational dynamics and 18.6% on tau-Voice (read 2026-10-03) [aa-s2s].

## Open questions

- The release date of Higgs Realtime and its maximum session length.
- Which languages the realtime model supports.

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
