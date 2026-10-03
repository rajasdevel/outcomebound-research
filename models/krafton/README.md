---
last_checked: 2026-10-03
volatility: MONITOR (lineage, guides and API behaviour change at each release)
sources:
  - https://huggingface.co/KRAFTON/Raon-SpeechChat-9B
  - https://github.com/krafton-ai/Raon-Speech
  - https://arxiv.org/abs/2605.23912
  - https://huggingface.co/api/models?author=KRAFTON&limit=40&sort=lastModified&direction=-1
  - https://artificialanalysis.ai/speech-to-speech
  - https://huggingface.co/KRAFTON/A.X-K2-Raon-Speech-21B-A3B
---

# KRAFTON

KRAFTON publishes the Raon family of open speech models. This folder holds its full-duplex model, Raon-SpeechChat-9B. KRAFTON runs no hosted API for it that was found. A person runs the weights on their own hardware. Everything here was read on 2026-10-03.

## Models and lineage

| Class | Model | Notes |
| --- | --- | --- |
| Raon SpeechChat | [Raon-SpeechChat-9B](raon-speechchat-9b.md) | Full-duplex extension of Raon-Speech-9B; English; weights under CC BY-NC 4.0 [raon-card-chat] |

KRAFTON numbers no generation. Models of the maker that have no file, with the reason (names, dates and sizes come from KRAFTON's Hugging Face listing) [hf-krafton-list]:

- **Raon-Speech-9B and its quantized builds** (2026-03-30). The offline speech language model for speech recognition, synthesis, spoken and text questions. It is not full-duplex.
- **A.X-K2-Raon-Speech-21B-A3B** (2026-07-27). A bilingual English and Korean speech language model (about 21.2B total and 3.5B active parameters) for speech recognition, synthesis, spoken questions and turn-based chat, under CC BY-NC 4.0. Its card describes no full-duplex mode [raon-card-ax21b].
- **Raon-OpenTTS-1B and -0.3B**, and **Raon-VisionEncoder**. Speech synthesis and vision parts, not conversation models.

## API surface

There is no hosted API. The code is at `krafton-ai/Raon-Speech`. The model loads through Hugging Face Transformers with `trust_remote_code=True`. The repository gives Python 3.11 or newer and a CUDA GPU. A Docker demo repository runs the full-duplex model in a browser [raon-gh] [raon-card-chat].

## Prompting guides

KRAFTON publishes no prompting guide. The SpeechChat card lists 17 personas, system prompts, context injection and a persona catalogue [raon-card-chat].

## System-card practice

KRAFTON publishes a Hugging Face card for each model and a technical report (dated 2026-04-08). The SpeechChat card has no safety section [raon-card-chat] [raon-paper].

## Family-wide behaviour

- The base model reads English and Korean. The SpeechChat card says English [raon-gh] [raon-card-chat].
- The weights of SpeechChat are under CC BY-NC 4.0, which bars commercial use [raon-card-chat].
- Artificial Analysis lists Raon SpeechChat at 57.5% on speech reasoning and 86.2% on conversational dynamics (read 2026-10-03) [aa-s2s].

## Open questions

- Sample rate and echo handling of the realtime audio.

## Sources

- [raon-card-chat] https://huggingface.co/KRAFTON/Raon-SpeechChat-9B (kind L, read 2026-10-03)
- [raon-gh] https://github.com/krafton-ai/Raon-Speech (kind L, read 2026-10-03)
- [raon-paper] https://arxiv.org/abs/2605.23912 (kind P, read 2026-10-03)
- [hf-krafton-list] https://huggingface.co/api/models?author=KRAFTON&limit=40&sort=lastModified&direction=-1 (kind L, read 2026-10-03)
- [aa-s2s] https://artificialanalysis.ai/speech-to-speech (kind M, read 2026-10-03)
- [raon-card-ax21b] https://huggingface.co/KRAFTON/A.X-K2-Raon-Speech-21B-A3B (kind L, read 2026-10-03)
