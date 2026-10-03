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
- A voice model is one of two kinds, from any maker, hosted or open-weight:
  - A full-duplex or realtime speech-to-speech model, for example the realtime models of OpenAI,
    the Live models of Google, Amazon Nova Sonic, the Qwen realtime models and the open full-duplex
    models. Its card has a `voice` object, and its file has a section on turn-taking, interruption
    and speech style.
  - A voice actor model: a speech synthesis model whose delivery (emotion, tone, pace, accent,
    character, non-verbal sounds) can be directed with natural-language instructions or inline tags
    in the text, beyond choosing a voice. A model that offers only a choice of voice, only SSML rate
    and pitch, or only a request-level preset is not one, and has no file. Like every class, a voice
    actor class keeps two generations. Its card has a `voice` object with `duplex` set to `none`.
    The section on speech style in its file holds the directing guidance and says that turn-taking
    does not apply. [../practices/voice-acting.md](../practices/voice-acting.md) compares how the
    makers direct delivery.
- ElevenLabs is the one maker whose speech synthesis and transcription models all have files,
  because the maker sells voice models only.
- OpenAI's realtime transcription and translation models have files, because OpenAI serves them
  through its Realtime API next to its realtime models. The standalone speech-to-text models of
  other makers do not.
- Out of scope: plain read-aloud speech synthesis (the text-to-speech models of other makers that
  are not voice actor models), the standalone speech-to-text models of other makers, and other speech
  models that neither hold a conversation nor take direction for delivery (voice changers, dubbing,
  music, sound effects).
  [../practices/voice-agents.md](../practices/voice-agents.md) names some of them when it describes
  the chained architecture.

### Speech models without a file (candidates for a later decision)

The writers of the voice files found these models and did not write a file. Each line gives the
reason. A decision to add one is a decision to widen the scope above, or to add a class or a maker.
A row that says "a candidate" names a model that may meet the scope above but has no card,
because its pages were not read in depth or because no rule settles it yet. The list is as of
2026-10-04.

| Maker | Model | Reason it has no file |
| --- | --- | --- |
| Alibaba | Qwen-Audio ASR, Fun-ASR | Speech-to-text |
| Alibaba | Qwen Livetranslate (3, 3.5 and 3.8) | Interpretation products |
| Alibaba | Qwen-Audio TTS (hosted, such as Qwen-Audio-3.0-TTS-Plus), Qwen3-TTS-Instruct-Flash, Qwen3-TTS-VD and Qwen3-TTS-VC (hosted), the hosted CosyVoice v3 and v3.5 models, Fun-AudioGen-VD (hosted voice design for CosyVoice) | Hosted speech synthesis. Qwen3-TTS-Instruct-Flash takes an `instructions` field, but these hosted models were read only for the API facts in the Alibaba README, and no page says whether a hosted model is the open weights; a candidate |
| Alibaba | Qwen3-TTS-12Hz 0.6B CustomVoice, the 0.6B and 1.7B Base models, CosyVoice 1.0 | No instruction control in Alibaba's model table, or older than two generations |
| Amazon | Amazon Polly (generative, neural, standard and long-form engines), Amazon Transcribe | Not Nova models. Polly's generative engine infers emotion from the text, and its documentation shows no instruction, tag or style input; Transcribe is speech-to-text |
| Bilibili | IndexTTS 1.0 and 1.5 | Older than two generations; the README names no emotion input |
| Bland | Bland Speech (`BTTS_V3`, `BTTS_V2`) | The API pages document two scalar controls; the dashboard guide shows bracket performance tags in two examples and gives no tag list; revisit when a list is published |
| Boson AI | Higgs TTS 2 (`bosonai/higgs-tts-2-3b-base`) | The card documents no delivery tags or instruction; a `scene` message sets only the recording setting and each speaker's gender; the generation before Higgs TTS 3 |
| BreezeBlue | Breeze TTS 1 | The generation before Breeze TTS 2: a hosted instruction-following service with no open weights. Its pages were not read in depth; a candidate |
| ByteDance | SeedRealtime, Doubao end-to-end realtime dialogue | No public API at launch per secondary sources; the maker page could not be read |
| ByteDance | Doubao Seed-TTS 2.0 (Volcano Engine) | Secondary pages say it takes natural-language directives and inline descriptors; no primary page could be read on 2026-10-04; a candidate |
| CAMB.AI | `mars-8.1-flash-beta`, `mars-8.1-pro-beta` | Six non-verbal tags and English phoneme overrides only; no emotion control |
| CAMB.AI | `mars-flash`, `mars-pro`, `mars-nano` | No emotion or prosody control |
| Cartesia | Sonic 3 (`sonic-3`) | Older than the two generations kept (3.6 and 3.5); the 2025-10-27 snapshot, `sonic-2` and `sonic-turbo` stop on 2026-10-20 |
| Cofe AI, VITA | FLM-Audio, Freeze-Omni | Older research models; no maker page read |
| Deepgram | Flux TTS, Aura-2, Aura | Voice choice, speed, pauses and pronunciation; Flux TTS alone adds one beta `expressivity` integer from -2 to 2; no tags or instructions |
| Deepgram, AssemblyAI | Transcription models | Speech-to-text; cascade parts, not conversation models |
| Deepslate | Opal | A platform with no separate model id or price; audio output depends on the configured speech synthesis provider |
| ElevenLabs | `eleven_multilingual_sts_v2`, `eleven_english_sts_v2` | Voice changers; they convert a recording and do not hold a conversation |
| ElevenLabs | `turn_v2`, `turn_v3` (agent turn-taking settings) | Only the setting names are published; no description, no price |
| ElevenLabs | Multilingual v1, Monolingual v1, Scribe v1 | Removal date passed or set; removal not confirmed with a key |
| Fish Audio | S1, S1 mini (OpenAudio S1 mini), `drama-3-preview` | S1 and S1 mini take parenthesis cues and are older than the two generations of their class (S2.1 Pro and S2 Pro have files in `fishaudio/`); `drama-3-preview` appears only in the OpenAPI schema |
| Google | Gemini 3.5 Transcribe and Transcribe Live | Speech-to-text only |
| Google | Gemini 3.5 Live Translate (preview) | Speech-to-speech translation; a candidate if translation models count as voice models |
| Google | Gemini 2.5 Flash native audio preview | Older generation of the Live class |
| Google | Gemini 2.5 Flash TTS (`gemini-2.5-flash-tts`, `gemini-2.5-flash-preview-tts`) | A third generation of the Flash TTS class (3.8, 3.1, then 2.5) |
| Google | Chirp 3: HD voices (Cloud Text-to-Speech) | Pace, pause and pronunciation controls; no emotion or style direction |
| Gradium | Gradium TTS | Voice design, speed and temperature only |
| Hugging Face (Parler-TTS) | Parler-TTS Mini v1.1, Large v1 and the multilingual model; Indic Parler-TTS | A written description sets speaking rate, pitch, expressiveness and recording quality, so the definition is met. No file was written, because the weights were last changed in October and November 2024 and no newer model exists. The scope rule counts generations, not age, so this waits on a decision about age; a candidate. The Indic Parler-TTS card is gated and was not read |
| Hume AI | Octave 2 (preview) | Hume documents the `description` acting-instruction field for Octave 1 only, and lists it as coming soon for Octave 2; the delivery controls of Octave 2 are `speed` and `trailing_silence`. The TTS API ends on 2026-11-13 |
| Hume AI | TADA 1B and 3B-ml | A speech-language model; no delivery direction in the card |
| Inworld | Realtime TTS-2 Flash (`inworld-tts-2-flash`) | Ignores steering instructions; plays non-verbal tags only |
| Inworld | TTS 1.5 Max and Mini | Deprecated and not recommended for new projects; no steering. A Replicate page lists fixed bracket markups (six emotions, whispering, laughing, six sounds), but the maker's markup page now needs a login |
| Kyutai | Hibiki, Hibiki-Zero, STT, TTS 1.6B, TTS 0.75B, Pocket TTS | Translation or recognition; the TTS models offer voice choice only, with no style direction in the README |
| LMNT | Speech models | The site says the service has ended |
| Maya Research | Maya 2 Native, Global and Flash, Maya Calyx, Veena | Maya 2 and Calyx: voice, language and speed only in the Pipecat documentation; Veena has no direction |
| Meituan | LongCat-AudioDiT 1B and 3.5B | The card read describes zero-shot voice cloning and names no delivery direction |
| Meta | Muse Voice Transcribe | Speech-to-text only; no Meta speech-to-speech model was found |
| Microsoft | MAI-Voice-2.1, MAI-Voice-2.1-Flash, MAI-Voice-2, MAI-Voice-2-Flash, Azure neural voices with SSML speaking styles, Azure OpenAI voices, Dragon HD Flash voices, the Voice Live API, MAI-Voice-1 | Fixed per-voice style presets in SSML (MAI-Voice and the Azure neural voices; the MAI-Voice-2 launch post claims emotion tags that the documentation read does not show), a conversation product that uses these voices, or older than two generations (MAI-Voice-1); Dragon HD and Dragon HD Omni take inline style and sound tags and have files |
| Microsoft | VibeVoice 1.5B, 7B and Realtime | No delivery direction documented |
| MiniMax | Speech 2.6 HD and Turbo, Speech-02, Speech-01 | An `emotion` request field only, with no inline tags (2.6), or older |
| Mistral | Voxtral speech-to-text models, Voxtral TTS (hosted) and Voxtral-4B-TTS-2603 (open weights, CC BY-NC) | Speech-to-text; the TTS model has 20 preset voices and adaptation from a reference clip, with no instruction or tags |
| Murf | Falcon 2, Gen2 | Per-voice style presets chosen by name; no tags or instructions |
| Nari Labs | Dia2 (1B and 2B), the first Dia-1.6B revision | Dia2 documents speaker tags only, no non-verbal or delivery tags; the first revision is superseded by Dia-1.6B (0626), which has a file |
| nineninesix | KaniTTS2 | Real-time speech; the card names emotion only as a fine-tuning use; no direction |
| 2Noise | ChatTTS (CC BY-NC 4.0 weights, AGPLv3+ code) | Inline tags for laughter and breaks, and numbered oral, laugh and break levels, meet the definition. No file was written, because the weights were last changed in October 2024; the same decision about age; a candidate |
| NVIDIA | Magpie TTS Multilingual 357M | Voices with emotional tones by voice choice; no instruction or tags |
| OpenAI | `gpt-realtime-1.5` (third generation of the Realtime class), `gpt-realtime`, GPT-Live-1 mini | Older than two generations, or ChatGPT only |
| OpenAI | `gpt-audio-1.5`, `gpt-audio-mini` | Chat Completions audio, not realtime |
| OpenAI | `tts-1`, `tts-1-hd`, `gpt-4o-mini-transcribe`, `gpt-4o-transcribe-diarize`, `whisper-1` | Standalone speech synthesis without an instructions field (`tts-1`, `tts-1-hd`) or speech recognition; OpenAI removes the speech synthesis models on 2027-01-06 |
| OpenBMB | VoxCPM 0.5B and VoxCPM1.5 | No voice design or style control, per the maker's version table |
| OpenMOSS | MOSS-TTS 1.0, v1.5, Local, Nano, TTSD and Realtime, MOSS-SoundEffect | Pause and duration markers, pronunciation control, dialogue or sound only; no emotion or style direction in the v1.5 card; MOSS-VoiceGenerator has a file |
| Play.ht (PlayAI) | PlayDialog and earlier | Service ended after the Meta acquisition; the API and the sites did not answer on 2026-10-04 |
| Resemble AI | Chatterbox (original), Chatterbox Multilingual V2 and V3, the Single Language Pack, Chatterbox-Flash | An exaggeration value and a guidance weight only, or no tags in the card |
| Resemble AI | Resemble Ultra | Powered by xAI and takes xAI's expressive tags, so it belongs with the xAI models; the older Chatterbox models of the Resemble API are end of life |
| Rime | Coda, Mist v3, Mist v2 | Voice choice, speed, pauses and spelling only |
| Rumik Intelligence | Rumik-OSS-1 (3B open weights, Indic, 2026-09-08) | Only a news summary was read (pace, accent, tone and inline tags); no primary page read; a candidate |
| Sesame | CSM-1B | Speech generation steered by earlier speech and text segments only; no instruction or tags; no public API found |
| Smallest.ai | Lightning v3.1 and v3.1 Pro | Voice choice and speed only |
| SparkAudio | Spark-TTS 0.5B | Attribute levels for gender, pitch and speed only; no update since March 2025 |
| Speechify | Simba Dialogue 1.0 (`simba-dialogue-1.0`) | A multi-speaker model listed by the models endpoint; no public page says how to direct its delivery |
| StepFun | Step-Audio R1.1 (Realtime), `step-audio-2`, `step-1o-audio`, `step-audio-r1.5`, StepAudio 3 ASR | No StepFun page or realtime guide found, older, or not speech-to-speech |
| StepFun | StepAudio 2.5 TTS, StepAudio 3 TTS (hosted), Step-Audio-TTS-3B | The hosted models may take direction in natural language, but their StepFun pages were not read (a candidate); Step-Audio-TTS-3B is older than two generations; Step-Audio-EditX has a file |
| Suno | Bark (MIT) | Bracket cues for non-speech sounds such as laughs meet the definition. No file was written, because the weights were last changed in October 2023 and the maker calls it a research and demo model; the same decision about age; a candidate |
| Typecast | `ssfm-v30`, `ssfm-v21` | Request-level emotion presets and a context-based Smart Emotion; no inline tags, no instructions, no SSML |
| VUI Labs | Luna-TTS | A research page and an arXiv report (2608.11593) describe emotion and non-verbal control, and the maker sells an Expressive TTS model, but the API docs host did not connect on 2026-10-04 and no public page says how to direct delivery; no open weights were found; revisit |
| xAI | Grok Voice Think Fast 1.0, Grok Voice Fast 1.0 | The docs list only 2.0; no xAI page for the earlier models was found |
| xAI | Grok text to speech (`/v1/tts`) | Inline tags and paired style tags meet the definition ([../practices/voice-acting.md](../practices/voice-acting.md) describes them); no card was written; a candidate |
| Xiaomi | MiMo-Audio-7B-Instruct | A general audio language model; its card claims instruct-TTS results but gives no syntax; not read in depth |
| Xiaomi | MiMo-V2.5-TTS, MiMo-V2.5-TTS-VoiceDesign, MiMo-V2.5-TTS-VoiceClone (hosted) | Instructions, free-form inline tags and screenplay-style input meet the definition ([../practices/voice-acting.md](../practices/voice-acting.md)); Artificial Analysis lists MiMo-V2.5-TTS, and BreezeBlue's direction benchmark scores it 3.76 of 5; the maker pages were not read in depth; a candidate |
| Z.ai | GLM-Realtime (`glm-realtime-flash`, `glm-realtime-air`) | Documented only on the Chinese platform docs; no release date, no independent test. A page that supports a card was read |
| Zhipu (Z.ai) | GLM-TTS (1.5B, MIT, 2025-12-10) | The card describes emotion expression by reinforcement learning and gives no instruction or tag syntax |
| Zyphra | Zonos v0.1 | Emotion, rate and pitch by a numeric conditioning vector, not by text instruction or tags; no update since June 2025 |
| Several makers | Kokoro, XTTS v2, OpenVoice v2, StyleTTS 2, MetaVoice, NeuTTS Air, Soprano, Marvis, Llasa | No delivery direction known, or older; named in roundups or in the Artificial Analysis list; not read in depth |

## Makers

| Folder | Holds |
| --- | --- |
| [alibaba/](alibaba/README.md) | The Qwen models of Alibaba, with the Qwen Omni and Qwen-Audio realtime voice models and the open Qwen3-TTS and CosyVoice voice actor models |
| [amazon/](amazon/README.md) | The Nova Sonic voice models of Amazon |
| [anthropic/](anthropic/README.md) | The Claude models of Anthropic |
| [boson/](boson/README.md) | The Higgs Realtime voice model and the Higgs TTS 3 voice actor model of Boson AI |
| [cambai/](cambai/README.md) | The MARS-Instruct voice actor model of CAMB.AI |
| [cartesia/](cartesia/README.md) | The Sonic voice actor models of Cartesia |
| [cursor/](cursor/README.md) | The own models of Cursor |
| [deepseek/](deepseek/README.md) | The models of DeepSeek |
| [elevenlabs/](elevenlabs/README.md) | The speech synthesis and transcription models of ElevenLabs |
| [fishaudio/](fishaudio/README.md) | The S2 voice actor models of Fish Audio |
| [google/](google/README.md) | The Gemini and Gemma models of Google, with the Gemini Live voice models and the Gemini TTS voice actor models |
| [hume/](hume/README.md) | The EVI voice models and the Octave 1 voice actor model of Hume AI |
| [inworld/](inworld/README.md) | The Realtime TTS-2 voice actor model of Inworld |
| [krafton/](krafton/README.md) | The Raon-SpeechChat voice model of KRAFTON |
| [kyutai/](kyutai/README.md) | The Moshi voice models of Kyutai |
| [meta/](meta/README.md) | The Muse models of Meta |
| [microsoft/](microsoft/README.md) | The Dragon HD voice actor models of Microsoft |
| [minimax/](minimax/README.md) | The models of MiniMax, with the Speech 2.8 voice actor models |
| [mistral/](mistral/README.md) | The models of Mistral |
| [moonshot/](moonshot/README.md) | The Kimi models of Moonshot |
| [openai/](openai/README.md) | The GPT and gpt-oss models of OpenAI, with its realtime, GPT-Live, translation and transcription voice models and the GPT-4o mini TTS voice actor model |
| [other/](other/README.md) | Models of makers that have a few models in scope, including the NVIDIA voice models and the open-weight voice actor models of eleven makers |
| [resemble-ai/](resemble-ai/README.md) | The Chatterbox-Turbo, Chatterbox-Nano and Dramabox voice actor models of Resemble AI |
| [soniox/](soniox/README.md) | The TTS Real-Time v2 voice actor model of Soniox |
| [speechify/](speechify/README.md) | The Simba voice actor models of Speechify |
| [stepfun/](stepfun/README.md) | The StepAudio realtime voice models of StepFun, with the open Step-Audio-EditX voice actor model |
| [typesafe/](typesafe/README.md) | The Jev models of TypeSafe AI |
| [xai/](xai/README.md) | The Grok models of xAI (the cards name the maker SpaceXAI), with Grok Voice |
| [zai/](zai/README.md) | The GLM models of Z.ai (the cards name the maker Zhipu) |

## Every model

The table is generated. `scripts/render.py` builds it from the cards. Do not edit it. Change a card
and run `make render`.

<!-- models:begin -->
| Model | Maker | Class | Generation | Status | Released | Voice | File |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CosyVoice2-0.5B | Alibaba (FunAudioLLM) | CosyVoice | 2 | ga | unknown | voice, no duplex | [alibaba/cosyvoice2-0.5b.md](alibaba/cosyvoice2-0.5b.md) |
| Fun-CosyVoice3-0.5B-2512 | Alibaba (FunAudioLLM) | CosyVoice | 3 | ga | 2025-12-11 | voice, no duplex | [alibaba/fun-cosyvoice3-0.5b-2512.md](alibaba/fun-cosyvoice3-0.5b-2512.md) |
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
| Qwen3-TTS-12Hz-1.7B-CustomVoice | Alibaba (Qwen) | Qwen TTS | 3 | ga | 2026-01-22 | voice, no duplex | [alibaba/qwen3-tts-12hz-1.7b-customvoice.md](alibaba/qwen3-tts-12hz-1.7b-customvoice.md) |
| Qwen3-TTS-12Hz-1.7B-VoiceDesign | Alibaba (Qwen) | Qwen TTS | 3 | ga | 2026-01-22 | voice, no duplex | [alibaba/qwen3-tts-12hz-1.7b-voicedesign.md](alibaba/qwen3-tts-12hz-1.7b-voicedesign.md) |
| Amazon Nova 2 Sonic | Amazon | Nova Sonic | 2 | ga | 2025-12-02 | full-duplex voice | [amazon/nova-2-sonic.md](amazon/nova-2-sonic.md) |
| Amazon Nova Sonic | Amazon | Nova Sonic | 1 | retired 2026-09-14 | 2025-04-08 | full-duplex voice | [amazon/nova-sonic.md](amazon/nova-sonic.md) |
| Claude Sonnet 5.5 | Anthropic | Claude Sonnet | 5.5 | ga | 2026-09-28 | - | [anthropic/claude-sonnet-5-5.md](anthropic/claude-sonnet-5-5.md) |
| Claude Opus 5.5 | Anthropic | Claude Opus | 5.5 | ga | 2026-09-22 | - | [anthropic/claude-opus-5-5.md](anthropic/claude-opus-5-5.md) |
| Claude Fable 5.1 | Anthropic | Claude Fable | 5.1 | ga | 2026-09-01 | - | [anthropic/claude-fable-5-1.md](anthropic/claude-fable-5-1.md) |
| Claude Opus 5 | Anthropic | Claude Opus | 5 | ga | 2026-07-24 | - | [anthropic/claude-opus-5.md](anthropic/claude-opus-5.md) |
| Claude Sonnet 5 | Anthropic | Claude Sonnet | 5 | ga | 2026-06-30 | - | [anthropic/claude-sonnet-5.md](anthropic/claude-sonnet-5.md) |
| Claude Fable 5 | Anthropic | Claude Fable | 5 | ga | 2026-06-09 | - | [anthropic/claude-fable-5.md](anthropic/claude-fable-5.md) |
| Claude Haiku 4.5 | Anthropic | Claude Haiku | 4.5 | ga | 2025-10-15 | - | [anthropic/claude-haiku-4-5.md](anthropic/claude-haiku-4-5.md) |
| VoiceSculptor-VD | ASLP-lab | VoiceSculptor | unknown | ga | 2026-01-06 | voice, no duplex | [other/voicesculptor-vd.md](other/voicesculptor-vd.md) |
| IndexTTS-2.5 | Bilibili (IndexTeam) | IndexTTS | 2.5 | ga | 2026-08-10 | voice, no duplex | [other/indextts-2.5.md](other/indextts-2.5.md) |
| IndexTTS-2 | Bilibili (IndexTeam) | IndexTTS | 2 | ga | 2025-09-08 | voice, no duplex | [other/indextts-2.md](other/indextts-2.md) |
| Higgs Realtime | Boson AI | Higgs Realtime | unknown | ga | unknown | full-duplex voice | [boson/higgs-realtime.md](boson/higgs-realtime.md) |
| Higgs TTS 3 | Boson AI | Higgs TTS | 3 | ga | 2026-06-04 | voice, no duplex | [boson/higgs-tts-3.md](boson/higgs-tts-3.md) |
| Breeze TTS 2 | BreezeBlue | Breeze TTS | 2 | ga | 2026-08-25 | voice, no duplex | [other/breeze-tts-2.md](other/breeze-tts-2.md) |
| CAMB.AI MARS-Instruct | CAMB.AI | CAMB.AI MARS Instruct | 8 | ga | 2026-01-20 | voice, no duplex | [cambai/mars-instruct.md](cambai/mars-instruct.md) |
| Orpheus 3B 0.1 finetuned | Canopy Labs | Orpheus | 0.1 | ga | 2025-03-17 | voice, no duplex | [other/orpheus-3b-0.1-ft.md](other/orpheus-3b-0.1-ft.md) |
| Cartesia Sonic 3.6 | Cartesia | Cartesia Sonic | 3.6 | ga | 2026-08-27 | voice, no duplex | [cartesia/sonic-3.6.md](cartesia/sonic-3.6.md) |
| Cartesia Sonic 3.5 | Cartesia | Cartesia Sonic | 3.5 | ga | 2026-05-04 | voice, no duplex | [cartesia/sonic-3.5.md](cartesia/sonic-3.5.md) |
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
| Fish Audio S2.1 Pro | Fish Audio | Fish Audio S Pro | 2.1 | ga | 2026-06-23 | voice, no duplex | [fishaudio/s2.1-pro.md](fishaudio/s2.1-pro.md) |
| Fish Audio S2 Pro | Fish Audio | Fish Audio S Pro | 2 | ga | 2026-03-09 | voice, no duplex | [fishaudio/s2-pro.md](fishaudio/s2-pro.md) |
| Gemini 2.5 Flash-Lite Preview TTS | Google | Gemini Flash-Lite TTS | 2.5 | preview | unknown | voice, no duplex | [google/gemini-2.5-flash-lite-preview-tts.md](google/gemini-2.5-flash-lite-preview-tts.md) |
| Gemini 4 Argon | Google | Gemini Argon | 4 | preview | 2026-09-30 | - | [google/gemini-4-argon.md](google/gemini-4-argon.md) |
| Gemini 3.8 Flash-Lite TTS | Google | Gemini Flash-Lite TTS | 3.8 | ga | 2026-09-22 | voice, no duplex | [google/gemini-3.8-flash-lite-tts.md](google/gemini-3.8-flash-lite-tts.md) |
| Gemini 3.8 Flash TTS | Google | Gemini Flash TTS | 3.8 | ga | 2026-09-22 | voice, no duplex | [google/gemini-3.8-flash-tts.md](google/gemini-3.8-flash-tts.md) |
| Gemini 3.8 Live | Google | Gemini Live | 3.8 | ga | 2026-09-15 | full-duplex voice | [google/gemini-3.8-live.md](google/gemini-3.8-live.md) |
| Gemini 3.8 Live Extended Thinking | Google | Gemini Live Extended Thinking | 3.8 | ga | 2026-09-15 | full-duplex voice | [google/gemini-3.8-live-extended-thinking.md](google/gemini-3.8-live-extended-thinking.md) |
| Gemini 3.8 Flash | Google | Gemini Flash | 3.8 | ga | 2026-09-02 | - | [google/gemini-3.8-flash.md](google/gemini-3.8-flash.md) |
| Gemini 3.7 Flash | Google | Gemini Flash | 3.7 | ga | 2026-08-13 | - | [google/gemini-3.7-flash.md](google/gemini-3.7-flash.md) |
| Gemini 3.5 Flash-Lite | Google | Gemini Flash-Lite | 3.5 | ga | 2026-07-21 | - | [google/gemini-3.5-flash-lite.md](google/gemini-3.5-flash-lite.md) |
| Gemma 4 12B (instruction-tuned, unified) | Google | Gemma | 4 | ga | 2026-06-03 | - | [google/gemma-4-12b-it.md](google/gemma-4-12b-it.md) |
| Gemini 3.1 Flash TTS Preview | Google | Gemini Flash TTS | 3.1 | preview | 2026-04-15 | voice, no duplex | [google/gemini-3.1-flash-tts-preview.md](google/gemini-3.1-flash-tts-preview.md) |
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
| Gemini 2.5 Pro TTS | Google | Gemini Pro TTS | 2.5 | ga | 2025-05-20 | voice, no duplex | [google/gemini-2.5-pro-tts.md](google/gemini-2.5-pro-tts.md) |
| Gemma 3 12B (instruction-tuned) | Google | Gemma | 3 | ga | 2025-03-10 | - | [google/gemma-3-12b-it.md](google/gemma-3-12b-it.md) |
| Gemma 3 1B (instruction-tuned) | Google | Gemma | 3 | ga | 2025-03-10 | - | [google/gemma-3-1b-it.md](google/gemma-3-1b-it.md) |
| Gemma 3 27B (instruction-tuned) | Google | Gemma | 3 | ga | 2025-03-10 | - | [google/gemma-3-27b-it.md](google/gemma-3-27b-it.md) |
| Gemma 3 4B (instruction-tuned) | Google | Gemma | 3 | ga | 2025-03-10 | - | [google/gemma-3-4b-it.md](google/gemma-3-4b-it.md) |
| Hume EVI 4-mini | Hume AI | Hume EVI | 4-mini | retiring (retires 2026-11-13) | 2025-10-03 | half-duplex voice | [hume/evi-4-mini.md](hume/evi-4-mini.md) |
| Hume EVI 3 | Hume AI | Hume EVI | 3 | retiring (retires 2026-11-13) | 2025-07-18 | half-duplex voice | [hume/evi-3.md](hume/evi-3.md) |
| Hume Octave 1 | Hume AI | Hume Octave | 1 | retiring (retires 2026-11-13) | 2025-02-26 | voice, no duplex | [hume/octave-1.md](hume/octave-1.md) |
| Ming-omni-tts 0.5B | inclusionAI (Ant Group) | Ming-omni-tts | unknown | ga | 2026-02-11 | voice, no duplex | [other/ming-omni-tts-0.5b.md](other/ming-omni-tts-0.5b.md) |
| Ming-omni-tts 16.8B-A3B | inclusionAI (Ant Group) | Ming-omni-tts | unknown | ga | 2026-02-11 | voice, no duplex | [other/ming-omni-tts-16.8b-a3b.md](other/ming-omni-tts-16.8b-a3b.md) |
| K2 Horizon 375B-A23B | Institute of Foundation Models (MBZUAI) | K2 Horizon | unknown | ga | 2026-09-03 | - | [other/k2-horizon-375b-a23b.md](other/k2-horizon-375b-a23b.md) |
| Inworld Realtime TTS-2 | Inworld | Inworld Realtime TTS | 2 | ga | 2026-05-05 | voice, no duplex | [inworld/inworld-tts-2.md](inworld/inworld-tts-2.md) |
| OmniVoice | k2-fsa (Next-gen Kaldi) | OmniVoice | unknown | ga | 2026-03-30 | voice, no duplex | [other/omnivoice.md](other/omnivoice.md) |
| Raon-SpeechChat-9B | KRAFTON | Raon SpeechChat | unknown | ga | 2026-04-01 | full-duplex voice | [krafton/raon-speechchat-9b.md](krafton/raon-speechchat-9b.md) |
| Moshi (Moshiko and Moshika) | Kyutai | Moshi | unknown | ga | unknown | full-duplex voice | [kyutai/moshi.md](kyutai/moshi.md) |
| MoshiRAG | Kyutai | Moshi | unknown | ga | unknown | full-duplex voice | [kyutai/moshirag.md](kyutai/moshirag.md) |
| Maya1 | Maya Research | Maya | 1 | ga | 2025-10-18 | voice, no duplex | [other/maya1.md](other/maya1.md) |
| Muse Spark 1.3 | Meta | Muse Spark | 1.3 | ga | 2026-09-02 | - | [meta/muse-spark-1.3.md](meta/muse-spark-1.3.md) |
| Muse Glimmer 30B | Meta | Muse Glimmer | unknown | ga | 2026-08-10 | - | [meta/muse-glimmer-30b.md](meta/muse-glimmer-30b.md) |
| Muse Spark 1.2 | Meta | Muse Spark | 1.2 | ga | 2026-08-05 | - | [meta/muse-spark-1.2.md](meta/muse-spark-1.2.md) |
| Dragon HD | Microsoft | Dragon HD | unknown | ga | unknown | voice, no duplex | [microsoft/dragon-hd.md](microsoft/dragon-hd.md) |
| Dragon HD Omni | Microsoft | Dragon HD Omni | unknown | preview | unknown | voice, no duplex | [microsoft/dragon-hd-omni.md](microsoft/dragon-hd-omni.md) |
| MiniMax M3.1 Flash Preview | MiniMax | MiniMax M Flash | 3.1 | preview | 2026-09-27 | - | [minimax/MiniMax-M3.1-Flash-Preview.md](minimax/MiniMax-M3.1-Flash-Preview.md) |
| MiniMax M3 | MiniMax | MiniMax M | 3 | ga | 2026-06-01 | - | [minimax/MiniMax-M3.md](minimax/MiniMax-M3.md) |
| MiniMax M2.7 | MiniMax | MiniMax M | 2.7 | ga | 2026-03-18 | - | [minimax/MiniMax-M2.7.md](minimax/MiniMax-M2.7.md) |
| MiniMax Speech 2.8 HD | MiniMax | MiniMax Speech HD | 2.8 | ga | 2026-01-23 | voice, no duplex | [minimax/speech-2.8-hd.md](minimax/speech-2.8-hd.md) |
| MiniMax Speech 2.8 Turbo | MiniMax | MiniMax Speech Turbo | 2.8 | ga | 2026-01-23 | voice, no duplex | [minimax/speech-2.8-turbo.md](minimax/speech-2.8-turbo.md) |
| Mistral Medium 3.5 | Mistral | Mistral Medium | 3.5 | ga | 2026-04-28 | - | [mistral/mistral-medium-3-5.md](mistral/mistral-medium-3-5.md) |
| Mistral Small 4 | Mistral | Mistral Small | 4 | ga | 2026-03-16 | - | [mistral/mistral-small-2603.md](mistral/mistral-small-2603.md) |
| Mistral Large 3 | Mistral | Mistral Large | 3 | ga | 2025-12-02 | - | [mistral/mistral-large-3.md](mistral/mistral-large-3.md) |
| Kimi K2.7 Code | Moonshot (Kimi) | Kimi K Code | 2.7 | ga | unknown | - | [moonshot/kimi-k2.7-code.md](moonshot/kimi-k2.7-code.md) |
| Kimi K3 | Moonshot (Kimi) | Kimi K | 3 | ga | 2026-07-16 | - | [moonshot/kimi-k3.md](moonshot/kimi-k3.md) |
| Kimi K2.6 | Moonshot (Kimi) | Kimi K | 2.6 | ga | 2026-04-20 | - | [moonshot/kimi-k2.6.md](moonshot/kimi-k2.6.md) |
| Dia 1.6B (0626) | Nari Labs | Dia | 1 | ga | 2025-06-26 | voice, no duplex | [other/dia-1.6b-0626.md](other/dia-1.6b-0626.md) |
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
| GPT-4o mini TTS | OpenAI | GPT-4o mini TTS | unknown | deprecated (retires 2027-01-06) | 2025-03-20 | voice, no duplex | [openai/gpt-4o-mini-tts.md](openai/gpt-4o-mini-tts.md) |
| GPT-4o Transcribe | OpenAI | GPT Transcribe | 1 | deprecated (retires 2027-02-26) | 2025-03-20 | voice, no duplex | [openai/gpt-4o-transcribe.md](openai/gpt-4o-transcribe.md) |
| VoxCPM2 | OpenBMB | VoxCPM | 2 | ga | 2026-04-03 | voice, no duplex | [other/voxcpm2.md](other/voxcpm2.md) |
| MOSS-VoiceGenerator | OpenMOSS (MOSI.AI) | MOSS-VoiceGenerator | unknown | ga | 2026-02-08 | voice, no duplex | [other/moss-voicegenerator.md](other/moss-voicegenerator.md) |
| Dramabox | Resemble AI | Dramabox | 1 | ga | 2026-04-17 | voice, no duplex | [resemble-ai/dramabox.md](resemble-ai/dramabox.md) |
| Chatterbox-Nano | Resemble AI | Chatterbox Turbo | 1 | ga | 2026-04-14 | voice, no duplex | [resemble-ai/chatterbox-nano.md](resemble-ai/chatterbox-nano.md) |
| Chatterbox-Turbo | Resemble AI | Chatterbox Turbo | 1 | ga | 2025-12-02 | voice, no duplex | [resemble-ai/chatterbox-turbo.md](resemble-ai/chatterbox-turbo.md) |
| Soniox TTS Real-Time v2 | Soniox | Soniox TTS Real-Time | 2 | ga | 2026-08-11 | voice, no duplex | [soniox/tts-rt-v2.md](soniox/tts-rt-v2.md) |
| SoulX-Podcast-1.7B | Soul AI Lab | SoulX-Podcast | unknown | ga | 2025-10-27 | voice, no duplex | [other/soulx-podcast-1.7b.md](other/soulx-podcast-1.7b.md) |
| SoulX-Podcast-1.7B-dialect | Soul AI Lab | SoulX-Podcast | unknown | ga | 2025-10-27 | voice, no duplex | [other/soulx-podcast-1.7b-dialect.md](other/soulx-podcast-1.7b-dialect.md) |
| Grok 4.7 | SpaceXAI | Grok | 4.7 | ga | 2026-09-21 | - | [xai/grok-4.7.md](xai/grok-4.7.md) |
| Grok 4.7 Fast | SpaceXAI | Grok Fast | 4.7 | ga | 2026-09-21 | - | [xai/grok-4.7-fast.md](xai/grok-4.7-fast.md) |
| Grok 4.6 | SpaceXAI | Grok | 4.6 | ga | 2026-08-12 | - | [xai/grok-4.6.md](xai/grok-4.6.md) |
| Grok Voice Think Fast 2.0 | SpaceXAI | Grok Voice Think Fast | 2.0 | ga | 2026-07-29 | full-duplex voice | [xai/grok-voice-think-fast-2.0.md](xai/grok-voice-think-fast-2.0.md) |
| Grok Build 0.1 | SpaceXAI | Grok Build | 0.1 | preview | 2026-05-29 | - | [xai/grok-build-0.1.md](xai/grok-build-0.1.md) |
| Speechify Simba 3.2 | Speechify | Speechify Simba | 3.2 | ga | 2026-07-08 | voice, no duplex | [speechify/simba-3.2.md](speechify/simba-3.2.md) |
| Speechify Simba 3.0 | Speechify | Speechify Simba | 3.0 | ga | 2026-05-09 | voice, no duplex | [speechify/simba-3.0.md](speechify/simba-3.0.md) |
| StepAudio 3 Realtime (preview) | StepFun | StepAudio Realtime | 3 | preview | 2026-09-15 | full-duplex voice | [stepfun/stepaudio-3-realtime-preview.md](stepfun/stepaudio-3-realtime-preview.md) |
| StepAudio 2.5 Realtime | StepFun | StepAudio Realtime | 2.5 | ga | 2026-05-24 | half-duplex voice | [stepfun/stepaudio-2.5-realtime.md](stepfun/stepaudio-2.5-realtime.md) |
| Step-Audio-EditX | StepFun | Step-Audio EditX | unknown | ga | 2025-11-12 | voice, no duplex | [stepfun/step-audio-editx.md](stepfun/step-audio-editx.md) |
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
