# Models

This folder has one file for each model that a person can select, grouped by maker. It is the
neutral base: facts and advice about the models, sourced and dated, for any use of them. Use it
to write a prompt for a model, to choose a reasoning effort, to wire tools, to move to a new
generation or to learn what a system card says.

## Find your model

1. Look for the maker in the [Makers](#makers) table, and open its folder.
2. Or look for the model in the table [Every model](#every-model), and open its file.
3. If the model is not in the table, it has no file (see [Scope](#scope)).

## What each part of a model file answers

| You want to know | Read |
| --- | --- |
| The id, limits, reasoning control, price, key benchmarks and the maker's own guides | The block at the top of the file. It is generated from the card of the model |
| How to write the system prompt, choose an effort, wire tools or move from the last generation | "How to instruct it" |
| How a voice model handles turns, interruption and speech, and what the maker says about prompting for speech | The Voice rows of the block, and the section "Voice: turn-taking, interruption and speech style" in "How to instruct it". [../practices/voice-agents.md](../practices/voice-agents.md) compares makers |
| What the maker's safety tests found that changes how you deploy the model | "What the system card reports" |
| What independent people saw when they used it | "Behaviour observed in practice". Each item has its evidence class |
| How it scores | "Benchmarks". Independent results come first, and each result keeps its qualifiers |
| What no source settles yet | "Open questions" |

A model file says what is different for its own model. It does not repeat what holds across the
maker's models. That text is in the `README.md` of the maker, in the same folder. It covers the
lineage, the API surface, the prompting guides, the system-card practice and the family-wide
behaviour.

Two more pages help you read across makers. [cross-family.md](cross-family.md) compares makers.
[../practices/prompting.md](../practices/prompting.md) says how to instruct current models in general,
by topic.

Every model file carries `last_checked` and `volatility`, like every research document. Check them
before you rely on a number. [FORMAT.md](FORMAT.md) says how a card and a model file are built.
A judgement that is built on these files for one use is an application. It lives in
[../applications/](../applications/README.md), not here.

## Scope

This library covers language models and voice models. It keeps two generations of each model class.
It has a file for the current generation and a file for the generation before it. A model that is
older has no file.

- A model class is a maker's line of models, for example Claude Opus or Gemini Flash. The `class` and
  `generation` of each card name them.
- Size variants of an open-weight family are separate models. Each has its own card and file.
- A voice model is a full-duplex or realtime speech-to-speech model of any maker, for example the
  realtime models of OpenAI, the Live models of Google, Amazon Nova Sonic, the Qwen realtime models
  and the open full-duplex models. Its card has a `voice` object, and its file has a section on
  turn-taking, interruption and speech style.
- ElevenLabs is the one maker whose speech synthesis and transcription models all have files,
  because the maker sells voice models only.
- OpenAI's realtime transcription and translation models have files, because OpenAI serves them
  through its Realtime API next to its realtime models. The standalone speech-to-text models of
  other makers do not.
- Out of scope: the standalone text-to-speech and speech-to-text models of other makers, and speech
  models that do not hold a conversation (voice changers, dubbing, music, sound effects).
  [../practices/voice-agents.md](../practices/voice-agents.md) names some of them when it describes
  the chained architecture.

### Speech models without a file (candidates for a later decision)

The writers of the voice files found these models and did not write a file. Each line gives the
reason. A decision to add one is a decision to widen the scope above, or to add a class or a maker.
The list is as of 2026-10-03.

| Maker | Model | Reason it has no file |
| --- | --- | --- |
| Alibaba | Qwen-Audio ASR and TTS, CosyVoice, Fun-ASR | Speech synthesis or recognition only |
| Alibaba | Qwen Livetranslate (3, 3.5 and 3.8) | Interpretation products |
| Amazon | Amazon Polly, Amazon Transcribe | Other services, not Nova models |
| Boson AI | Higgs TTS 3 | Speech synthesis only |
| ByteDance | SeedRealtime, Doubao end-to-end realtime dialogue | No public API at launch per secondary sources; the maker page could not be read |
| Cofe AI, VITA | FLM-Audio, Freeze-Omni | Older research models; no maker page read |
| Deepslate | Opal | A platform with no separate model id or price; audio output depends on the configured speech synthesis provider |
| ElevenLabs | `eleven_multilingual_sts_v2`, `eleven_english_sts_v2` | Voice changers; they convert a recording and do not hold a conversation |
| ElevenLabs | `turn_v2`, `turn_v3` (agent turn-taking settings) | Only the setting names are published; no description, no price |
| ElevenLabs | Multilingual v1, Monolingual v1, Scribe v1 | Removal date passed or set; removal not confirmed with a key |
| Google | Gemini 3.8 Flash TTS and Flash-Lite TTS | Speech synthesis only |
| Google | Gemini 3.5 Transcribe and Transcribe Live | Speech-to-text only |
| Google | Gemini 3.5 Live Translate (preview) | Speech-to-speech translation; a candidate if translation models count as voice models |
| Google | Gemini 2.5 Flash native audio preview | Older generation of the Live class |
| Kyutai | Hibiki, Hibiki-Zero, STT, TTS, Pocket TTS | Translation, recognition or synthesis only |
| Meta | Muse Voice Transcribe | Speech-to-text only; no Meta speech-to-speech model was found |
| Microsoft, Cartesia, Inworld, Deepgram, AssemblyAI | Speech synthesis and transcription models | Cascade parts, not conversation models |
| Mistral | Voxtral | Speech-to-text and text-to-speech cascade parts |
| OpenAI | `gpt-realtime-1.5` (third generation of the Realtime class), `gpt-realtime`, GPT-Live-1 mini | Older than two generations, or ChatGPT only |
| OpenAI | `gpt-audio-1.5`, `gpt-audio-mini` | Chat Completions audio, not realtime |
| OpenAI | `gpt-4o-mini-tts`, `tts-1`, `tts-1-hd`, `gpt-4o-mini-transcribe`, `gpt-4o-transcribe-diarize`, `whisper-1` | Standalone speech synthesis or recognition; OpenAI removes the speech synthesis models on 2027-01-06 |
| Sesame | CSM-1B | Speech generation, not speech-to-speech; no public API found |
| StepFun | Step-Audio R1.1 (Realtime), `step-audio-2`, `step-1o-audio`, `step-audio-r1.5`, StepAudio 3 TTS and ASR | No StepFun page or realtime guide found, older, or not speech-to-speech |
| xAI | Grok Voice Think Fast 1.0, Grok Voice Fast 1.0 | The docs list only 2.0; no xAI page for the earlier models was found |
| Z.ai | GLM-Realtime (`glm-realtime-flash`, `glm-realtime-air`) | Documented only on the Chinese platform docs; no release date, no independent test. A page that supports a card was read |

## Makers

| Folder | Holds |
| --- | --- |
| [alibaba/](alibaba/README.md) | The Qwen models of Alibaba, with the Qwen Omni and Qwen-Audio realtime voice models |
| [amazon/](amazon/README.md) | The Nova Sonic voice models of Amazon |
| [anthropic/](anthropic/README.md) | The Claude models of Anthropic |
| [boson/](boson/README.md) | The Higgs Realtime voice model of Boson AI |
| [cursor/](cursor/README.md) | The own models of Cursor |
| [deepseek/](deepseek/README.md) | The models of DeepSeek |
| [elevenlabs/](elevenlabs/README.md) | The speech synthesis and transcription models of ElevenLabs |
| [google/](google/README.md) | The Gemini and Gemma models of Google, with the Gemini Live voice models |
| [hume/](hume/README.md) | The EVI voice models of Hume AI |
| [krafton/](krafton/README.md) | The Raon-SpeechChat voice model of KRAFTON |
| [kyutai/](kyutai/README.md) | The Moshi voice models of Kyutai |
| [meta/](meta/README.md) | The Muse models of Meta |
| [minimax/](minimax/README.md) | The models of MiniMax |
| [mistral/](mistral/README.md) | The models of Mistral |
| [moonshot/](moonshot/README.md) | The Kimi models of Moonshot |
| [openai/](openai/README.md) | The GPT and gpt-oss models of OpenAI, with its realtime, GPT-Live, translation and transcription voice models |
| [other/](other/README.md) | Models of makers that have a few models in scope, including the NVIDIA voice models |
| [stepfun/](stepfun/README.md) | The StepAudio realtime voice models of StepFun |
| [xai/](xai/README.md) | The Grok models of xAI (the cards name the maker SpaceXAI), with Grok Voice |
| [zai/](zai/README.md) | The GLM models of Z.ai (the cards name the maker Zhipu) |

## Every model

The table is generated. `scripts/render.py` builds it from the cards. Do not edit it. Change a card
and run `make render`.

<!-- models:begin -->
| Model | Maker | Class | Generation | Status | Released | Voice | File |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Qwen3.8-Omni-Flash-Realtime | Alibaba (Qwen) | Qwen Omni Realtime | 3.8 | ga | 2026-09-21 | full-duplex voice | [alibaba/qwen3.8-omni-flash-realtime.md](alibaba/qwen3.8-omni-flash-realtime.md) |
| Qwen-Audio-3.1-Realtime-Plus | Alibaba (Qwen) | Qwen Audio Realtime | 3.1 | ga | 2026-09-20 | full-duplex voice | [alibaba/qwen-audio-3.1-realtime-plus.md](alibaba/qwen-audio-3.1-realtime-plus.md) |
| Qwen3.8-Omni-Flash | Alibaba (Qwen) | Qwen Omni | 3.8 | ga | 2026-09-18 | - | [alibaba/qwen3.8-omni-flash.md](alibaba/qwen3.8-omni-flash.md) |
| Qwen3.8-Flash-Next | Alibaba (Qwen) | Qwen Flash | 3.8 | preview | 2026-08-27 | - | [alibaba/qwen3.8-flash-next.md](alibaba/qwen3.8-flash-next.md) |
| Qwen3.8-Flash | Alibaba (Qwen) | Qwen Flash | 3.8 | ga | 2026-08-26 | - | [alibaba/qwen3.8-flash.md](alibaba/qwen3.8-flash.md) |
| Qwen3.8-27B | Alibaba (Qwen) | Qwen open weights | 3.8 | ga | 2026-08-14 | - | [alibaba/qwen3.8-27b.md](alibaba/qwen3.8-27b.md) |
| Qwen3.8-2.4T-A95B | Alibaba (Qwen) | Qwen open weights | 3.8 | ga | 2026-08-13 | - | [alibaba/qwen3.8-2.4t-a95b.md](alibaba/qwen3.8-2.4t-a95b.md) |
| Qwen-Audio-3.0-Realtime-Flash | Alibaba (Qwen) | Qwen Audio Realtime Flash | 3.0 | ga | 2026-08-10 | full-duplex voice | [alibaba/qwen-audio-3.0-realtime-flash.md](alibaba/qwen-audio-3.0-realtime-flash.md) |
| Qwen-Audio-3.0-Realtime-Plus | Alibaba (Qwen) | Qwen Audio Realtime | 3.0 | ga | 2026-08-10 | full-duplex voice | [alibaba/qwen-audio-3.0-realtime-plus.md](alibaba/qwen-audio-3.0-realtime-plus.md) |
| Qwen3.8-Max | Alibaba (Qwen) | Qwen Max | 3.8 | ga | 2026-08-03 | - | [alibaba/qwen3.8-max.md](alibaba/qwen3.8-max.md) |
| Qwen3.7-Flash | Alibaba (Qwen) | Qwen Flash | 3.7 | ga | 2026-07-25 | - | [alibaba/qwen3.7-flash.md](alibaba/qwen3.7-flash.md) |
| Qwen3.7-Plus | Alibaba (Qwen) | Qwen Plus | 3.7 | ga | 2026-06-01 | - | [alibaba/qwen3.7-plus.md](alibaba/qwen3.7-plus.md) |
| Qwen3.7-Max | Alibaba (Qwen) | Qwen Max | 3.7 | ga | 2026-05-21 | - | [alibaba/qwen3.7-max.md](alibaba/qwen3.7-max.md) |
| Qwen3.6-27B | Alibaba (Qwen) | Qwen open weights | 3.6 | ga | 2026-04-22 | - | [alibaba/qwen3.6-27b.md](alibaba/qwen3.6-27b.md) |
| Qwen3.6-35B-A3B | Alibaba (Qwen) | Qwen open weights | 3.6 | ga | 2026-04-16 | - | [alibaba/qwen3.6-35b-a3b.md](alibaba/qwen3.6-35b-a3b.md) |
| Qwen3.6-Plus | Alibaba (Qwen) | Qwen Plus | 3.6 | ga | 2026-04-02 | - | [alibaba/qwen3.6-plus.md](alibaba/qwen3.6-plus.md) |
| Qwen3.5-Omni-Flash | Alibaba (Qwen) | Qwen Omni | 3.5 | ga | 2026-03-30 | half-duplex voice | [alibaba/qwen3.5-omni-flash.md](alibaba/qwen3.5-omni-flash.md) |
| Qwen3.5-Omni-Plus-Realtime | Alibaba (Qwen) | Qwen Omni Realtime | 3.5 | ga | 2026-03-30 | half-duplex voice | [alibaba/qwen3.5-omni-plus-realtime.md](alibaba/qwen3.5-omni-plus-realtime.md) |
| Qwen3-Coder-Next | Alibaba (Qwen) | Qwen Coder | 3 | retiring (retires 2026-10-10) | 2026-02-03 | - | [alibaba/qwen3-coder-next.md](alibaba/qwen3-coder-next.md) |
| Amazon Nova 2 Sonic | Amazon | Nova Sonic | 2 | ga | 2025-12-02 | full-duplex voice | [amazon/nova-2-sonic.md](amazon/nova-2-sonic.md) |
| Amazon Nova Sonic | Amazon | Nova Sonic | 1 | retired 2026-09-14 | 2025-04-08 | full-duplex voice | [amazon/nova-sonic.md](amazon/nova-sonic.md) |
| Claude Sonnet 5.5 | Anthropic | Claude Sonnet | 5.5 | ga | 2026-09-28 | - | [anthropic/claude-sonnet-5-5.md](anthropic/claude-sonnet-5-5.md) |
| Claude Opus 5.5 | Anthropic | Claude Opus | 5.5 | ga | 2026-09-22 | - | [anthropic/claude-opus-5-5.md](anthropic/claude-opus-5-5.md) |
| Claude Fable 5.1 | Anthropic | Claude Fable | 5.1 | ga | 2026-09-01 | - | [anthropic/claude-fable-5-1.md](anthropic/claude-fable-5-1.md) |
| Claude Opus 5 | Anthropic | Claude Opus | 5 | ga | 2026-07-24 | - | [anthropic/claude-opus-5.md](anthropic/claude-opus-5.md) |
| Claude Sonnet 5 | Anthropic | Claude Sonnet | 5 | ga | 2026-06-30 | - | [anthropic/claude-sonnet-5.md](anthropic/claude-sonnet-5.md) |
| Claude Fable 5 | Anthropic | Claude Fable | 5 | ga | 2026-06-09 | - | [anthropic/claude-fable-5.md](anthropic/claude-fable-5.md) |
| Claude Haiku 4.5 | Anthropic | Claude Haiku | 4.5 | ga | 2025-10-15 | - | [anthropic/claude-haiku-4-5.md](anthropic/claude-haiku-4-5.md) |
| Higgs Realtime | Boson AI | Higgs Realtime | unknown | ga | unknown | full-duplex voice | [boson/higgs-realtime.md](boson/higgs-realtime.md) |
| Composer 2.5 | Cursor | Cursor Composer | 2.5 | ga | 2026-05-18 | - | [cursor/composer-2.5.md](cursor/composer-2.5.md) |
| DeepSeek V4.1-Flash | DeepSeek | DeepSeek Flash | 4.1 | ga | 2026-09-10 | - | [deepseek/deepseek-flash.md](deepseek/deepseek-flash.md) |
| DeepSeek V4-Pro (0813) | DeepSeek | DeepSeek Pro | 4 | ga | 2026-08-13 | - | [deepseek/deepseek-v4-pro.md](deepseek/deepseek-v4-pro.md) |
| DeepSeek V4-Flash (0731) | DeepSeek | DeepSeek Flash | 4 | retired 2026-09-10 | 2026-07-31 | - | [deepseek/deepseek-v4-flash.md](deepseek/deepseek-v4-flash.md) |
| Eleven v4 | ElevenLabs | Eleven Expressive | 4 | ga | 2026-09-28 | voice, no duplex | [elevenlabs/eleven_v4.md](elevenlabs/eleven_v4.md) |
| Eleven v4 Turbo | ElevenLabs | Eleven Realtime | 4 | ga | 2026-09-28 | voice, no duplex | [elevenlabs/eleven_v4_turbo.md](elevenlabs/eleven_v4_turbo.md) |
| Scribe v2 Medical | ElevenLabs | Scribe Medical | 2 | ga | 2026-09-11 | voice, no duplex | [elevenlabs/scribe_v2_medical.md](elevenlabs/scribe_v2_medical.md) |
| Eleven v3 Conversational | ElevenLabs | Eleven Realtime | 3 | ga | 2026-02-09 | voice, no duplex | [elevenlabs/eleven_v3_conversational.md](elevenlabs/eleven_v3_conversational.md) |
| Scribe v2 | ElevenLabs | Scribe | 2 | ga | 2026-01-09 | voice, no duplex | [elevenlabs/scribe_v2.md](elevenlabs/scribe_v2.md) |
| Scribe v2 Realtime | ElevenLabs | Scribe Realtime | 2 | ga | 2025-11-11 | voice, no duplex | [elevenlabs/scribe_v2_realtime.md](elevenlabs/scribe_v2_realtime.md) |
| Eleven v3 | ElevenLabs | Eleven Expressive | 3 | ga | 2025-06-03 | voice, no duplex | [elevenlabs/eleven_v3.md](elevenlabs/eleven_v3.md) |
| Eleven Flash v2 | ElevenLabs | Eleven Flash | 2 | ga | 2024-12-18 | voice, no duplex | [elevenlabs/eleven_flash_v2.md](elevenlabs/eleven_flash_v2.md) |
| Eleven Flash v2.5 | ElevenLabs | Eleven Flash | 2.5 | ga | 2024-12-18 | voice, no duplex | [elevenlabs/eleven_flash_v2_5.md](elevenlabs/eleven_flash_v2_5.md) |
| Eleven Multilingual v2 | ElevenLabs | Eleven Multilingual | 2 | ga | 2023-08-22 | voice, no duplex | [elevenlabs/eleven_multilingual_v2.md](elevenlabs/eleven_multilingual_v2.md) |
| Gemini 4 Argon | Google | Gemini Argon | 4 | preview | 2026-09-30 | - | [google/gemini-4-argon.md](google/gemini-4-argon.md) |
| Gemini 3.8 Live | Google | Gemini Live | 3.8 | ga | 2026-09-15 | full-duplex voice | [google/gemini-3.8-live.md](google/gemini-3.8-live.md) |
| Gemini 3.8 Live Extended Thinking | Google | Gemini Live Extended Thinking | 3.8 | ga | 2026-09-15 | full-duplex voice | [google/gemini-3.8-live-extended-thinking.md](google/gemini-3.8-live-extended-thinking.md) |
| Gemini 3.8 Flash | Google | Gemini Flash | 3.8 | ga | 2026-09-02 | - | [google/gemini-3.8-flash.md](google/gemini-3.8-flash.md) |
| Gemini 3.7 Flash | Google | Gemini Flash | 3.7 | ga | 2026-08-13 | - | [google/gemini-3.7-flash.md](google/gemini-3.7-flash.md) |
| Gemini 3.5 Flash-Lite | Google | Gemini Flash-Lite | 3.5 | ga | 2026-07-21 | - | [google/gemini-3.5-flash-lite.md](google/gemini-3.5-flash-lite.md) |
| Gemma 4 12B (instruction-tuned, unified) | Google | Gemma | 4 | ga | 2026-06-03 | - | [google/gemma-4-12b-it.md](google/gemma-4-12b-it.md) |
| Gemma 4 26B A4B (instruction-tuned) | Google | Gemma | 4 | ga | 2026-04-02 | - | [google/gemma-4-26b-a4b-it.md](google/gemma-4-26b-a4b-it.md) |
| Gemma 4 31B (instruction-tuned) | Google | Gemma | 4 | ga | 2026-04-02 | - | [google/gemma-4-31b-it.md](google/gemma-4-31b-it.md) |
| Gemma 4 E2B (instruction-tuned) | Google | Gemma | 4 | ga | 2026-04-02 | - | [google/gemma-4-e2b-it.md](google/gemma-4-e2b-it.md) |
| Gemma 4 E4B (instruction-tuned) | Google | Gemma | 4 | ga | 2026-04-02 | - | [google/gemma-4-e4b-it.md](google/gemma-4-e4b-it.md) |
| Gemini 3.1 Flash Live Preview | Google | Gemini Live | 3.1 | preview | 2026-03-26 | full-duplex voice | [google/gemini-3.1-flash-live-preview.md](google/gemini-3.1-flash-live-preview.md) |
| Gemini 3.1 Flash-Lite | Google | Gemini Flash-Lite | 3.1 | ga (retires 2027-05-07) | 2026-03-03 | - | [google/gemini-3.1-flash-lite.md](google/gemini-3.1-flash-lite.md) |
| Gemini 3.1 Pro (Preview) | Google | Gemini Pro | 3.1 | preview | 2026-02-19 | - | [google/gemini-3.1-pro-preview.md](google/gemini-3.1-pro-preview.md) |
| Gemma 3 270M (instruction-tuned) | Google | Gemma | 3 | ga | 2025-08-14 | - | [google/gemma-3-270m-it.md](google/gemma-3-270m-it.md) |
| Gemma 3n E2B (instruction-tuned) | Google | Gemma | 3 | ga | 2025-06-26 | - | [google/gemma-3n-e2b-it.md](google/gemma-3n-e2b-it.md) |
| Gemma 3n E4B (instruction-tuned) | Google | Gemma | 3 | ga | 2025-06-26 | - | [google/gemma-3n-e4b-it.md](google/gemma-3n-e4b-it.md) |
| Gemma 3 12B (instruction-tuned) | Google | Gemma | 3 | ga | 2025-03-10 | - | [google/gemma-3-12b-it.md](google/gemma-3-12b-it.md) |
| Gemma 3 1B (instruction-tuned) | Google | Gemma | 3 | ga | 2025-03-10 | - | [google/gemma-3-1b-it.md](google/gemma-3-1b-it.md) |
| Gemma 3 27B (instruction-tuned) | Google | Gemma | 3 | ga | 2025-03-10 | - | [google/gemma-3-27b-it.md](google/gemma-3-27b-it.md) |
| Gemma 3 4B (instruction-tuned) | Google | Gemma | 3 | ga | 2025-03-10 | - | [google/gemma-3-4b-it.md](google/gemma-3-4b-it.md) |
| Hume EVI 4-mini | Hume AI | Hume EVI | 4-mini | retiring (retires 2026-11-13) | 2025-10-03 | half-duplex voice | [hume/evi-4-mini.md](hume/evi-4-mini.md) |
| Hume EVI 3 | Hume AI | Hume EVI | 3 | retiring (retires 2026-11-13) | 2025-07-18 | half-duplex voice | [hume/evi-3.md](hume/evi-3.md) |
| K2 Horizon 375B-A23B | Institute of Foundation Models (MBZUAI) | K2 Horizon | unknown | ga | 2026-09-03 | - | [other/k2-horizon-375b-a23b.md](other/k2-horizon-375b-a23b.md) |
| Raon-SpeechChat-9B | KRAFTON | Raon SpeechChat | unknown | ga | 2026-04-01 | full-duplex voice | [krafton/raon-speechchat-9b.md](krafton/raon-speechchat-9b.md) |
| Moshi (Moshiko and Moshika) | Kyutai | Moshi | unknown | ga | unknown | full-duplex voice | [kyutai/moshi.md](kyutai/moshi.md) |
| MoshiRAG | Kyutai | Moshi | unknown | ga | unknown | full-duplex voice | [kyutai/moshirag.md](kyutai/moshirag.md) |
| Muse Spark 1.3 | Meta | Muse Spark | 1.3 | ga | 2026-09-02 | - | [meta/muse-spark-1.3.md](meta/muse-spark-1.3.md) |
| Muse Glimmer 30B | Meta | Muse Glimmer | unknown | ga | 2026-08-10 | - | [meta/muse-glimmer-30b.md](meta/muse-glimmer-30b.md) |
| Muse Spark 1.2 | Meta | Muse Spark | 1.2 | ga | 2026-08-05 | - | [meta/muse-spark-1.2.md](meta/muse-spark-1.2.md) |
| MiniMax M3.1 Flash Preview | MiniMax | MiniMax M Flash | 3.1 | preview | 2026-09-27 | - | [minimax/MiniMax-M3.1-Flash-Preview.md](minimax/MiniMax-M3.1-Flash-Preview.md) |
| MiniMax M3 | MiniMax | MiniMax M | 3 | ga | 2026-06-01 | - | [minimax/MiniMax-M3.md](minimax/MiniMax-M3.md) |
| MiniMax M2.7 | MiniMax | MiniMax M | 2.7 | ga | 2026-03-18 | - | [minimax/MiniMax-M2.7.md](minimax/MiniMax-M2.7.md) |
| Mistral Medium 3.5 | Mistral | Mistral Medium | 3.5 | ga | 2026-04-28 | - | [mistral/mistral-medium-3-5.md](mistral/mistral-medium-3-5.md) |
| Mistral Small 4 | Mistral | Mistral Small | 4 | ga | 2026-03-16 | - | [mistral/mistral-small-2603.md](mistral/mistral-small-2603.md) |
| Mistral Large 3 | Mistral | Mistral Large | 3 | ga | 2025-12-02 | - | [mistral/mistral-large-3.md](mistral/mistral-large-3.md) |
| Kimi K2.7 Code | Moonshot (Kimi) | Kimi K Code | 2.7 | ga | unknown | - | [moonshot/kimi-k2.7-code.md](moonshot/kimi-k2.7-code.md) |
| Kimi K3 | Moonshot (Kimi) | Kimi K | 3 | ga | 2026-07-16 | - | [moonshot/kimi-k3.md](moonshot/kimi-k3.md) |
| Kimi K2.6 | Moonshot (Kimi) | Kimi K | 2.6 | ga | 2026-04-20 | - | [moonshot/kimi-k2.6.md](moonshot/kimi-k2.6.md) |
| NVIDIA NemotronLabs VoiceChat 11B | NVIDIA | Nemotron VoiceChat | 1 | ga | 2026-08-03 | full-duplex voice | [other/nemotron-voicechat-11b.md](other/nemotron-voicechat-11b.md) |
| NVIDIA Nemotron 3 Ultra | NVIDIA | Nemotron Ultra | 3 | ga | 2026-06-04 | - | [other/nemotron-3-ultra.md](other/nemotron-3-ultra.md) |
| PersonaPlex-7B-v1 | NVIDIA | PersonaPlex | 1 | ga | 2026-01-15 | full-duplex voice | [other/personaplex-7b-v1.md](other/personaplex-7b-v1.md) |
| GPT-6.1 Sol | OpenAI | GPT Sol | 6.1 | ga | 2026-09-29 | - | [openai/gpt-6.1-sol.md](openai/gpt-6.1-sol.md) |
| GPT-6 Luna | OpenAI | GPT Luna | 6 | ga | 2026-09-22 | - | [openai/gpt-6-luna.md](openai/gpt-6-luna.md) |
| GPT-6 Sol | OpenAI | GPT Sol | 6 | ga | 2026-09-22 | - | [openai/gpt-6-sol.md](openai/gpt-6-sol.md) |
| GPT-Live 1 | OpenAI | GPT Live | 1 | ga | 2026-09-10 | full-duplex voice | [openai/gpt-live-1.md](openai/gpt-live-1.md) |
| GPT-6 Astra | OpenAI | GPT Astra | 6 | ga | 2026-09-03 | - | [openai/gpt-6-astra.md](openai/gpt-6-astra.md) |
| GPT-Live-Transcribe | OpenAI | GPT Realtime Transcribe | 2 | ga | 2026-07-28 | voice, no duplex | [openai/gpt-live-transcribe.md](openai/gpt-live-transcribe.md) |
| GPT-Transcribe | OpenAI | GPT Transcribe | 2 | ga | 2026-07-28 | voice, no duplex | [openai/gpt-transcribe.md](openai/gpt-transcribe.md) |
| GPT-5.6 Luna | OpenAI | GPT Luna | 5.6 | ga | 2026-07-09 | - | [openai/gpt-5.6-luna.md](openai/gpt-5.6-luna.md) |
| GPT-5.6 Terra | OpenAI | GPT Terra | 5.6 | ga | 2026-07-09 | - | [openai/gpt-5.6-terra.md](openai/gpt-5.6-terra.md) |
| GPT-Realtime-2.1 | OpenAI | GPT Realtime | 2.1 | ga | 2026-07-06 | half-duplex voice | [openai/gpt-realtime-2.1.md](openai/gpt-realtime-2.1.md) |
| GPT-Realtime-2.1 Mini | OpenAI | GPT Realtime Mini | 2.1 | ga | 2026-07-06 | half-duplex voice | [openai/gpt-realtime-2.1-mini.md](openai/gpt-realtime-2.1-mini.md) |
| GPT-Realtime-2 | OpenAI | GPT Realtime | 2 | ga | 2026-05-07 | half-duplex voice | [openai/gpt-realtime-2.md](openai/gpt-realtime-2.md) |
| GPT-Realtime-Translate | OpenAI | GPT Realtime Translate | 1 | ga | 2026-05-07 | voice, no duplex | [openai/gpt-realtime-translate.md](openai/gpt-realtime-translate.md) |
| GPT-Realtime-Whisper | OpenAI | GPT Realtime Transcribe | 1 | ga | 2026-05-07 | voice, no duplex | [openai/gpt-realtime-whisper.md](openai/gpt-realtime-whisper.md) |
| GPT-Realtime Mini | OpenAI | GPT Realtime Mini | 1 | deprecated (retires 2027-01-20) | 2025-10-06 | half-duplex voice | [openai/gpt-realtime-mini.md](openai/gpt-realtime-mini.md) |
| gpt-oss-120b | OpenAI | gpt-oss | unknown | ga | 2025-08-05 | - | [openai/gpt-oss-120b.md](openai/gpt-oss-120b.md) |
| gpt-oss-20b | OpenAI | gpt-oss | unknown | ga | 2025-08-05 | - | [openai/gpt-oss-20b.md](openai/gpt-oss-20b.md) |
| GPT-4o Transcribe | OpenAI | GPT Transcribe | 1 | deprecated (retires 2027-02-26) | 2025-03-20 | voice, no duplex | [openai/gpt-4o-transcribe.md](openai/gpt-4o-transcribe.md) |
| Grok 4.7 | SpaceXAI | Grok | 4.7 | ga | 2026-09-21 | - | [xai/grok-4.7.md](xai/grok-4.7.md) |
| Grok 4.7 Fast | SpaceXAI | Grok Fast | 4.7 | ga | 2026-09-21 | - | [xai/grok-4.7-fast.md](xai/grok-4.7-fast.md) |
| Grok 4.6 | SpaceXAI | Grok | 4.6 | ga | 2026-08-12 | - | [xai/grok-4.6.md](xai/grok-4.6.md) |
| Grok Voice Think Fast 2.0 | SpaceXAI | Grok Voice Think Fast | 2.0 | ga | 2026-07-29 | full-duplex voice | [xai/grok-voice-think-fast-2.0.md](xai/grok-voice-think-fast-2.0.md) |
| Grok Build 0.1 | SpaceXAI | Grok Build | 0.1 | preview | 2026-05-29 | - | [xai/grok-build-0.1.md](xai/grok-build-0.1.md) |
| StepAudio 3 Realtime (preview) | StepFun | StepAudio Realtime | 3 | preview | 2026-09-15 | full-duplex voice | [stepfun/stepaudio-3-realtime-preview.md](stepfun/stepaudio-3-realtime-preview.md) |
| StepAudio 2.5 Realtime | StepFun | StepAudio Realtime | 2.5 | ga | 2026-05-24 | half-duplex voice | [stepfun/stepaudio-2.5-realtime.md](stepfun/stepaudio-2.5-realtime.md) |
| Tencent Hy4 preview | Tencent | Tencent Hy | 4 | preview | 2026-08-28 | - | [other/hy4-preview.md](other/hy4-preview.md) |
| Tencent Hy3 | Tencent | Tencent Hy | 3 | ga | 2026-07-06 | - | [other/hy3.md](other/hy3.md) |
| Inkling-Small | Thinking Machines Lab | Inkling | unknown | ga | 2026-07-30 | - | [other/inkling-small.md](other/inkling-small.md) |
| Inkling | Thinking Machines Lab | Inkling | unknown | ga | 2026-07-15 | - | [other/inkling.md](other/inkling.md) |
| Jev 1.13 | TypeSafe AI | Jev | 1.13 | preview | 2026-09-15 | - | [typesafe/jev-1.13.0.md](typesafe/jev-1.13.0.md) |
| MiMo-V2.6-Flash | Xiaomi | MiMo Flash | 2.6 | ga | 2026-09-21 | - | [other/mimo-v2.6-flash.md](other/mimo-v2.6-flash.md) |
| MiMo-V2.6-Pro | Xiaomi | MiMo Pro | 2.6 | ga | 2026-09-21 | - | [other/mimo-v2.6-pro.md](other/mimo-v2.6-pro.md) |
| GLM-5.3-FlashX | Zhipu (GLM) | GLM FlashX | 5.3 | ga | 2026-09-18 | - | [zai/glm-5.3-flashx.md](zai/glm-5.3-flashx.md) |
| GLM-5.3-Flash | Zhipu (GLM) | GLM Flash | 5.3 | ga | 2026-08-26 | - | [zai/glm-5.3-flash.md](zai/glm-5.3-flash.md) |
| GLM-5.3 | Zhipu (GLM) | GLM | 5.3 | ga | 2026-08-18 | - | [zai/glm-5.3.md](zai/glm-5.3.md) |
| GLM-5.2 | Zhipu (GLM) | GLM | 5.2 | ga | 2026-06-16 | - | [zai/glm-5.2.md](zai/glm-5.2.md) |
| GLM-4.7-Flash | Zhipu (GLM) | GLM Flash | 4.7 | ga | 2026-01-19 | - | [zai/glm-4.7-flash.md](zai/glm-4.7-flash.md) |
<!-- models:end -->
