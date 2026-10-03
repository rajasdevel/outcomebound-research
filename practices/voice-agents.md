---
last_checked: 2026-10-03
volatility: VOLATILE (limits, defaults, prices, model names and benchmark scores change at each release) / STABLE (the architecture choice, the turn-taking mechanics and the published evaluation methods)
sources:
  - https://developers.openai.com/api/docs/guides/voice-agents
  - https://developers.openai.com/api/docs/guides/live-prompting
  - https://developers.openai.com/api/docs/guides/live-conversations
  - https://developers.openai.com/api/docs/guides/live-delegation
  - https://developers.openai.com/api/docs/guides/realtime-vad
  - https://developers.openai.com/api/docs/guides/realtime-conversations
  - https://developers.openai.com/api/docs/guides/realtime-models-prompting
  - https://developers.openai.com/api/docs/guides/your-data
  - https://ai.google.dev/gemini-api/docs/live-api/best-practices
  - https://ai.google.dev/gemini-api/docs/live-api/capabilities
  - https://ai.google.dev/gemini-api/docs/live-api/session-management
  - https://docs.cloud.google.com/vertex-ai/generative-ai/docs/live-api/troubleshooting
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-turn-taking.html
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-barge-in.html
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-system-prompts.html
  - https://www.alibabacloud.com/help/en/model-studio/realtime
  - https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech.md
  - https://elevenlabs.io/docs/eleven-agents/customization/conversation-flow
  - https://docs.livekit.io/agents/logic/turns/tuning
  - https://arxiv.org/abs/2410.00037
  - https://arxiv.org/abs/2503.04721
  - https://arxiv.org/abs/2603.13686
  - https://artificialanalysis.ai/methodology/speech-to-speech-benchmarking
---

# Voice agents

Re-check when a maker changes its realtime or voice API, a new voice model ships, or a benchmark
changes its method; in any case by 2026-10-17 for the figures and limits, and by 2027-04-01 for the
rest.

How to build a voice agent with the models and platforms that makers publish today. The page covers
the choice between one speech-to-speech model and a chain of speech-to-text, language model and
text-to-speech. It covers turn detection, interruption and where the time goes. It covers how makers
say to prompt for speech, what goes wrong in live calls, session limits and tools during a call. It
ends with evaluation and audio data. For anyone who designs a voice product, writes a voice system
prompt or chooses a voice model.
Each voice model has its own file: [OpenAI](../models/openai/README.md),
[Google](../models/google/README.md), [Amazon](../models/amazon/README.md),
[Kyutai](../models/kyutai/README.md) and [ElevenLabs](../models/elevenlabs/README.md). Voice models
of Alibaba are in [the Alibaba folder](../models/alibaba/README.md). xAI's voice model is in
[grok-voice-think-fast-2.0.md](../models/xai/grok-voice-think-fast-2.0.md), and its API is in
[../providers/xai.md](../providers/xai.md). General rules for prompts are in
[prompting.md](prompting.md) and [writing-for-models.md](writing-for-models.md). Rules for judges that
score conversations are in [llm-as-judge.md](llm-as-judge.md). Text-only agent evaluation is in
[agent-evals.md](agent-evals.md). How to direct the delivery of synthetic speech (emotion, tags, voice
design, cloning, non-verbal sounds) is in [voice-acting.md](voice-acting.md).

**Evidence classes**, as in [the conventions](../CONVENTIONS.md): M measured; L maker or vendor
documentation or guidance; S standard or law; P practitioner consensus; A anecdote or one
uncontrolled report; F forecast. **Citations.** Bracketed `[chk-…]` ids are pages read on 2026-10-03.
They are listed under Sources. Most claims here are a maker describing its own product (L). Where a
maker names a feature, this page says what the maker documents. It does not say that the feature
works well. Model names change fast. The names here are the names on the maker pages on 2026-10-03.

## Key findings

**VA1. Makers document three architectures, and each trades control for speed.** OpenAI names them
in one table. GPT-Live is full duplex, with a separate backend for reasoning and tools. The Realtime
API is one model that hears, reasons and speaks. The chained pipeline (speech-to-text, agent,
text-to-speech) gives "control over each speech and text stage" [chk-oai-voice-agents]. Amazon,
Google, xAI and Alibaba serve single speech-to-speech endpoints. ElevenLabs and Kyutai's Unmute
serve chains [chk-el-flow, chk-el-prompting, chk-unmute]. L.

**VA2. Turn detection is a setting that every maker exposes in a different form.** OpenAI offers
`server_vad` and `semantic_vad`. Google offers automatic, hybrid and manual activity detection.
Amazon offers three sensitivity levels with fixed pause lengths. ElevenLabs offers three eagerness
levels. The values are not comparable across makers. Each page trades a fast reply against a risk of
cutting the user off [chk-oai-vad, chk-g-capabilities, chk-aws-turn, chk-el-flow]. L.

**VA3. Barge-in needs work in the client.** Google, Amazon and OpenAI (on WebSocket) all say that the
server stops generating when the user speaks, and that the client must stop playback and clear its
audio queue. Without that step the user hears the old answer to the end. On OpenAI's WebRTC and SIP
connections the server truncates the unplayed audio itself [chk-g-best, chk-aws-barge,
chk-oai-rt-conv]. L.

**VA4. Silence after the user stops is part of the response time.** Makers publish the wait as a
setting: 500 to 800 ms for Google, 1.5 to 2 s for Amazon, a default of 800 ms for Alibaba. An
independent measurer lists time to first audio from 0.04 s to 8.83 s across the models it lists on
2026-10-03. Seven configurations of OpenAI, Google, Amazon and xAI that this page selected lie between
0.70 s and 1.35 s. Other configurations of the same makers are slower, up to 4.28 s. The questions
are short and use no tools [chk-g-capabilities, chk-aws-turn, chk-ali-client-events,
chk-aa-board]. L, M.

**VA5. Makers disagree on filler words.** OpenAI's guide lists "Hmm" and "Let me think" as phrases to
avoid and asks for one short sentence that names the action. ElevenLabs ships a soft timeout that
speaks such a filler. LiveKit shows prompts that add fillers with pauses. Amazon says its newer model
repeats listed phrases very often. OpenAI, LiveKit and Amazon each say that sample or listed phrases
get repeated [chk-oai-rt-prompting, chk-el-flow, chk-lk-prompting, chk-aws-prompts]. L.

**VA6. The failures that makers document are mostly playback, turn and session failures.** Audio
keeps playing after an interruption. Injected context cuts a reply off. Silence follows a slow tool
call. The model hears its own echo as the user. Digits come back wrong, the language switches and
speech speeds up in long turns. Sessions end at a time limit [chk-g-vertex-trouble, chk-g-capabilities,
chk-g-model38, chk-oai-rt-prompting, chk-oai-live-sessions, chk-ali-python-sdk, chk-moshi-readme]. L.

**VA7. Session limits run from 8 minutes to 120 minutes, and each maker has its own way to continue.**
Amazon limits a connection to 8 minutes. Google limits a connection to about 10 minutes and offers
resumption handles. OpenAI Realtime limits a session to 60 minutes. Alibaba allows 120 minutes. The
long-session fix is summaries or compression, and the makers say that details can be lost
[chk-aws-s2s, chk-g-session, chk-oai-rt-conv, chk-ali-realtime, chk-oai-live-sessions]. L.

**VA8. On one task benchmark, voice agents score well below a text agent.** In τ-voice, GPT-5 with
reasoning, as a text reference, scored 85 percent. Voice agents scored 31 to 51 percent in clean audio
and 26 to 38 percent with noise and accents, which the authors give as 30 to 45 percent of text
capability. They traced 79 to 90 percent of failures to agent behavior [chk-tauvoice]. M.

**VA9. Audio retention and disclosure differ by maker.** OpenAI keeps no application state for
Realtime and 30 days for a stored GPT-Live session. ElevenLabs keeps transcripts and audio for 2
years by default. Google uses content sent to its unpaid services to improve its products. In the United States, the FCC treats
AI-generated voices as artificial voices under the TCPA. The EU AI Act asks for disclosure that a
person talks to an AI system [chk-oai-data, chk-el-retention, chk-g-terms, chk-fcc, chk-euai]. L, S.

## 1. Architectures: speech-to-speech, full duplex and the chain (MONITOR)

- **Three shapes.** A *chained* pipeline runs speech-to-text, a text model and text-to-speech in
  sequence. A *speech-to-speech* model takes audio in and gives audio out in one model. A
  *full-duplex* model also listens while it speaks. OpenAI describes GPT-Live as a model that "can
  listen and speak at the same time" and that hands reasoning and tools to a separate backend
  [chk-oai-live, chk-oai-voice-agents]. L.
- **What the chain offers.** OpenAI says to use the chain when each stage must be visible or
  replaceable. Its examples are to store the transcript, run policy checks before the text agent
  answers, and speak only after the workflow approves the answer [chk-oai-voice-agents]. LiveKit says
  that in a chain the language model "has no built-in understanding of its own position in a voice
  pipeline", so the prompt must tell it that its output is spoken [chk-lk-prompting]. L.
- **What speech-to-speech offers.** Google says its native audio models keep the conversation as raw
  audio tokens "to preserve acoustic nuance and tone", and that this raises cost as a session grows
  [chk-g-best]. Amazon lists adaptive speech that follows the prosody of the input, and polyglot
  voices [chk-aws-s2s]. L.
- **A split between voice and brain.** GPT-Live keeps speaking behavior in the live model's prompt and
  business rules in the backend prompt. The backend can run in OpenAI's Responses API or in the
  application's own agent, and the application checks permissions and confirmations
  [chk-oai-live, chk-oai-live-delegation]. Google's Gemini 3.8 Live Extended Thinking does background
  reasoning while it streams audio [chk-g-model38-et]. L.
- **Open models show both shapes.** Kyutai's Moshi is a full-duplex model with a 7-billion-parameter
  temporal transformer. The authors report 160 ms theoretical and 200 ms practical latency on an L4
  GPU. Kyutai's Unmute is a chain around any text model, with a streaming speech-to-text model that
  predicts whether the user has finished [chk-moshi-paper, chk-moshi-readme, chk-unmute, chk-kyutai-stt]. L, M
  (author-reported).
- **Evidence on the trade.** The independent speech-to-speech index scores native audio models on
  speech reasoning, agentic tasks, human preference and task success. It reports conversational
  dynamics as a separate score. On 2026-10-03 it shows
  Moshi at 4 percent on speech reasoning and 61.0 percent on conversational dynamics. It shows
  GPT-Realtime-2 (high) at 97 percent, Gemini 3.8 Live at 92 percent and Nova 2.0 Sonic at 88 percent
  on speech reasoning. A score depends on the configuration that was tested, such as the reasoning
  level [chk-aa-board]. M.
- **Cost units differ.** The unit sets what a long call costs:

| Maker and product | Unit on 2026-10-03 | What else bills |
| --- | --- | --- |
| OpenAI GPT-Live (`gpt-live-1`) | $0.05 per minute of session, billed per second; WebRTC start bills 15 s, credited to the running time [chk-oai-live-model, chk-oai-cost] | Backend model and tool tokens, separately |
| OpenAI Realtime (`gpt-realtime-2`) | Audio tokens: $32 per million in, $64 per million out, $0.40 cached in. One input token is 100 ms of audio and one output token is 50 ms [chk-oai-rt2-model, chk-oai-cost] | Text tokens; reasoning raises output tokens |
| Google Gemini Live | Tokens, about 25 per second of audio. Each turn bills the whole retained context again, so cost per turn grows until compression trims it [chk-g-best] | Transcription text tokens, if on |
| Amazon Nova 2 Sonic | Per token; the Bedrock model card links to the pricing page without figures [chk-aws-card] | Not read |
| ElevenLabs Agents | $0.08 per additional call minute, with text-to-speech and speech-to-text included [chk-el-pricing] | Language model usage, billed on top |

  L. Chained pipelines bill each stage in its own unit. No maker page compares a chain with a native
  model for the same call.

## 2. Latency and where the time goes (VOLATILE)

- **Parts of the delay.** In a chain, the delay is the end-of-turn wait, speech-to-text finalization,
  the language model's first output, the first audio from text-to-speech, and the network. One
  speech-to-text vendor's page of 2026-07-02 gives illustrative ranges. The end-of-turn wait is 200
  to 400 ms, finalization 50 to 150 ms, the first token 300 to 500 ms, first audio 100 to 200 ms and
  the network 100 to 200 ms. Its sequential example uses 350, 120, 400, 150 and 160 ms, which add up
  to 1,180 ms. The page says that an 800 ms budget is met only when the stages overlap. It names the
  end-of-turn wait as often the largest item [chk-soniox]. A (vendor, illustrative).
- **Human timing.** A study of ten languages found that speakers avoid overlap and keep the silence
  between turns short. The average gap per language was within 250 ms of the cross-language mean
  [chk-stivers]. M.
- **Overlap in the chain.** LiveKit starts the language model as soon as a final transcript arrives,
  before the turn is confirmed. It can also start text-to-speech early, at the cost of wasted work when
  the user keeps talking. Its page says that this does not always reduce latency and that metrics
  should confirm it. ElevenLabs says its agent starts to speak after "enough words and a comma" from
  the model, not after a full sentence [chk-lk-tuning, chk-el-flow]. L.
- **Setup time and early audio.** xAI says to open the WebSocket and the microphone in parallel and to
  buffer the first audio until the socket opens. OpenAI's cost page lists parallel tool runs, closing
  idle sessions and speculative lookups as ways to cut backend delay and billed time
  [chk-xai-s2s, chk-oai-cost]. L.
- **A measured case.** A 2025 packet analysis of OpenAI's WebRTC Realtime API measured response
  delays of 1.76 to 1.86 s on three speaker switches on 2025-01-04. The author found that every audio
  packet from the server set the RTP marker bit, which tells the jitter buffer to flush. He says results
  improved later, in particular the STUN round trip [chk-webrtchacks]. M, old.
- **Time to first audio on one benchmark.** The independent leaderboard gives the average time to the
  first audio token over the Big Bench Audio questions. Values on 2026-10-03:

| Model on the leaderboard | Time to first audio |
| --- | --- |
| xAI Grok Voice Think Fast 2.0 High (listed under SpaceXAI) | 0.70 s |
| OpenAI GPT-Realtime-2.1 (minimal) | 0.97 s |
| Amazon Nova 2.0 Sonic (March 2026) | 1.14 s |
| OpenAI GPT-Realtime-2 (high) | 1.14 s |
| Google Gemini 3.8 Live | 1.18 s |
| OpenAI GPT-Live-1 (Sol backend, low effort) | 1.24 s |
| Google Gemini 3.8 Live Extended Thinking (high) | 1.35 s |

  M. The questions are short and use no tools. The leaderboard changes. A value depends on the
  reasoning level that was set. The figures include no tool calls, and OpenAI says to time the backend
  stages apart from the spoken answer [chk-aa-board, chk-aa-method, chk-oai-voice-agents].
- **How OpenAI says to measure.** Measure the wait for a useful spoken answer. Report the median and
  the 95th percentile over similar calls. Keep caller, recording, backend, prompt and transport fixed.
  Time the acknowledgment such as "I'm checking" apart from the answer. For GPT-Live, record
  delegation receipt, backend start, first useful result, tool start and end, result submission,
  audio arrival and client playback [chk-oai-voice-agents]. L.

## 3. Turn detection and endpointing (MONITOR)

*Endpointing* is the decision that the user has finished. The simplest form is a silence timer after
voice activity detection (VAD). A semantic form also reads the words or the intonation. A third form
leaves the decision to the application, as in push-to-talk.

| Maker or framework | What the docs offer |
| --- | --- |
| OpenAI Realtime | `server_vad` with `threshold`, `prefix_padding_ms` and `silence_duration_ms` (the page example uses 0.5, 300 and 500). `semantic_vad` with `eagerness` of low, medium, high or auto, where auto equals medium. The VAD page names `server_vad` as the default. `turn_detection: null` turns VAD off for push-to-talk. `create_response` and `interrupt_response` can each be false, to keep VAD events but decide replies in code [chk-oai-vad, chk-oai-rt-conv] |
| OpenAI GPT-Live | Full duplex. The session pages list microphone mute and unmute events and no VAD setting [chk-oai-live-sessions] |
| Google Gemini Live | Automatic VAD by default, with `prefixPaddingMs`, `silenceDurationMs` and start and end sensitivity. Hybrid VAD keeps server detection of speech start and lets the client send `audioStreamEnd` when its own detector hears the end. Manual mode uses `activityStart` and `activityEnd` and removes the server buffering [chk-g-capabilities] |
| Amazon Nova 2 Sonic | `endpointingSensitivity` of HIGH (pause 1.5 s), MEDIUM (1.75 s) or LOW (2 s) in `turnDetectionConfiguration` [chk-aws-turn] |
| Alibaba Qwen Omni realtime | `server_vad` (default) or `semantic_vad` on Qwen3.8-Omni-Flash and Qwen3.5-Omni; `threshold` 0.5 and `silence_duration_ms` 800 (range 200 to 6000) by default; `turn_detection: null` hands control to the client [chk-ali-client-events, chk-ali-python-sdk] |
| xAI speech-to-speech | `server_vad`, or `null` for manual turns, plus `idle_timeout_ms` [chk-xai-s2s] |
| ElevenLabs Agents | Turn eagerness of eager, normal or patient, and a "take turn after silence" timeout of 1 to 30 s. These are platform settings. The prompt does not control them [chk-el-flow, chk-el-prompting] |
| LiveKit Agents (framework) | A turn-detector model on top of VAD (the default for chains). Other modes: the realtime model's own detection, VAD only, speech-to-text endpointing and manual. Endpointing defaults to a 0.5 s minimum and 3.0 s maximum delay [chk-lk-turns, chk-lk-tuning] |
| Kyutai Unmute | The `stt-1b-en_fr` speech-to-text model has a built-in semantic VAD that predicts whether the user paused or finished. Kyutai says that, so far, only its Rust server includes this detector [chk-kyutai-stt, chk-unmute] |

L.

- **What the makers say each mode is for.** OpenAI: server VAD splits turns at silence, and a shorter
  silence window detects the end of a turn faster. Semantic VAD "is less likely to interrupt the user"
  and waits longer after a trailing-off phrase [chk-oai-vad]. Amazon: HIGH for quick question and answer, LOW for
  people who pause while they think, including "elderly or speech-impaired users" [chk-aws-turn].
  ElevenLabs: patient for collecting detailed information [chk-el-flow]. L.
- **Too short a silence window.** Google says that 100 to 200 ms splits one utterance into fragments
  and lowers transcription and response quality. It recommends 500 to 800 ms. A client-side detector
  in manual mode needs at least 500 ms of silence, since the server adds no tolerance there. Too long
  a window (2,000 ms and up) adds delay [chk-g-capabilities]. L.
- **Push-to-talk.** OpenAI describes it as a button gate on audio with VAD off. On press, cancel the
  response, stop playback and clear the buffer. On release, append, commit and request a response. It
  says this "avoids VAD failures" and feels quick since no VAD timeout runs [chk-oai-rt-conv]. L.
- **Noise.** OpenAI says a higher server-VAD threshold may do better in noisy places. LiveKit shows a
  telephony setting of threshold 0.7 and a 400 ms silence window, and lists voice isolation, noise
  suppression and a telephony-tuned model as steps before VAD [chk-oai-vad, chk-lk-turns, chk-lk-tuning].
  Google says to check microphone quality, background noise and the audio format when the model
  misunderstands [chk-g-vertex-trouble]. L.
- **Measured turn behavior.** The independent index uses two turn behaviors from Full-Duplex-Bench v1:
  pause handling (the model must not speak during a natural pause) and turn taking (it must speak
  when the turn ends). It adds two from v1.5: handling of a user interruption and handling of a
  backchannel. On 2026-10-03 the conversational-dynamics scores of the current Google, OpenAI and xAI
  configurations in its table range from 71.6 to 97.3 percent. Two older Gemini 2.5 previews score
  30.3 and 44.0 percent, and Moshi scores 61.0 percent [chk-aa-method, chk-aa-board]. M.

## 4. Barge-in and interruption handling (MONITOR)

- **OpenAI Realtime.** With VAD on, the API detects speech, cancels the response and starts a new one.
  On WebRTC and SIP the server holds an output buffer, so it knows what was played and truncates the
  rest. On WebSocket the client stops playback and sends `conversation.item.truncate` with
  `audio_end_ms`. The call removes the unplayed audio and the transcript of the unplayed part. OpenAI
  says the model cannot align transcript and audio exactly, so the call does not give a truncated
  transcript [chk-oai-rt-conv]. L.
- **OpenAI GPT-Live.** The model "can listen and speak at the same time". The prompt template says to
  stop and listen when the user interrupts. The guide separates two requests: "Stop talking" asks the
  assistant to yield, and "Cancel my booking" asks the backend to act. Stopping speech leaves backend
  work running, and the application decides whether to finish or cancel it. A brief listening sound
  differs from taking over the turn, and a rule that forbids all overlap can remove backchannels.
  Text that the application appends can itself interrupt speech [chk-oai-live-prompting,
  chk-oai-live-delegation, chk-oai-live-sessions]. L.
- **Google.** VAD cancels the generation. Only what the server already sent stays in the history. The
  server drops pending function calls and reports their ids. The client "must immediately discard"
  its audio buffer when `interrupted` is true. The Vertex page lists a missing buffer flush, audio
  not streamed to the server, and a faulty custom VAD as the causes of a model that cannot be
  interrupted [chk-g-capabilities, chk-g-best, chk-g-vertex-trouble]. L.
- **Amazon.** The server stops, keeps the context and signals the client. Audio generates faster than
  it plays, so audio is already queued. The client must detect the signal, stop playback, clear the
  queue and play the new audio [chk-aws-barge]. L.
- **ElevenLabs.** Interruption is a switch under client events. The docs say to disable it when the
  whole message must be heard, such as legal text or safety information [chk-el-flow]. xAI has a
  `force_message` item with `interruptible: false` for scripted lines such as "This call is being
  recorded"; caller audio is dropped until playback ends [chk-xai-s2s]. L.
- **Telling a real interruption from a backchannel.** LiveKit's adaptive mode uses an audio model to
  separate interruptions from acknowledgments such as "uh-huh". Its defaults count speech of 0.5 s,
  call an interruption false after 2 s with no transcript, and resume the speech [chk-lk-tuning]. L.
- **Measured behavior.** Full-Duplex-Bench v1.5 (2025-07-30) tests four overlap cases: user
  interruption, backchannel, talk to others and background speech. It benchmarks five agents and
  finds two strategies, responsive ones that answer fast, and floor-holding ones that filter overlap
  [chk-fdb15]. FD-Bench (2025-07-25) ran 293 simulated conversations with 1,200 interruptions on
  three open systems. It reports that all three failed to respond to some interruptions, under
  frequent interruptions and in noise [chk-fdbench]. M.

## 5. Prompting for speech (MONITOR)

What the makers' guides say. They share a base: the prompt controls what is said, and the platform
controls how the voice sounds. xAI says so directly, and tells prompt writers to turn rules about
speaking rate, emotion or the sound of the voice into rules about the words produced
[chk-xai-prompting]. L.

### Structure and length

- OpenAI's Realtime guide lists labeled sections: role and objective, personality and tone, language,
  reasoning, message channels, preambles, verbosity, tools, unclear audio, entity capture, long
  context behavior and escalation. It says to start with a minimal prompt, run evaluations and add
  rules only for failures. It says small word changes can change behavior a lot [chk-oai-rt-prompting].
  L.
- The GPT-Live prompt is shorter. It holds a persona, a backchannel policy, an interruption policy and
  a delegation policy. OpenAI says to describe the behavior and "let GPT-Live choose the wording" for
  ordinary replies. It says to keep procedures in the backend prompt [chk-oai-live-prompting]. L.
- Google orders a system instruction as persona, conversational rules, tool calls in distinct
  sentences, then guardrails. It separates one-time steps from loops, advises one prompt per persona,
  and suggests the word "unmistakably" where precision is low. It says the model performs best on
  tasks with single function calls [chk-g-best]. L.
- xAI uses five sections in a fixed order: role and persona, objective, conversation flow, guardrails
  and escalation, voice and communication style. The greeting is a separate field [chk-xai-prompting].
  L.
- ElevenLabs separates instructions into sections for personality, goal, guardrails, tone and tools.
  It says the prompt does not control turn-taking [chk-el-prompting]. LiveKit recommends Markdown
  sections for identity, output formatting, tools, goals, guardrails and user information
  [chk-lk-prompting]. L.

### Sounding human: pace, length, fillers and variety

- **Length.** The LiveKit, Amazon, OpenAI and xAI guides all ask for short replies. LiveKit: "one to
  three sentences" and one question at a time. Amazon's baseline for its newer model: 1 to 2 sentences
  first, then 3 to 5 short sentences in total. OpenAI says to define "concise" per task, for example 1
  to 2 sentences for a direct answer and one step at a time for troubleshooting. xAI's template asks
  for 1 to 2 short sentences per turn [chk-lk-prompting, chk-aws-prompts, chk-oai-rt-prompting,
  chk-xai-prompting]. L.
- **Pace.** OpenAI says the `speed` setting changes only playback rate. It suggests an instruction
  such as "Deliver your audio response fast, but do not sound rushed" [chk-oai-rt-prompting]. xAI has
  `audio.output.speed` from 0.7 to 1.5 [chk-xai-s2s]. Google lists a speech rate that rises during
  turns longer than 60 s, and says to keep chunks under 100 words or 50 s of audio [chk-g-vertex-trouble].
  L.
- **Fillers and preambles.** OpenAI: a preamble is one short sentence that names the action, such as
  "I'll check that order now". It lists "Let me think...", "Hmm..." and "One moment while I process
  that..." as phrases to avoid, and says to skip the preamble for direct answers, confirmations,
  unclear audio and background noise. ElevenLabs does the opposite on purpose: its soft timeout speaks
  a filler such as "Hmm..." once per turn when the language model is slow, and not at all if the
  answer arrives in time. LiveKit teaches fillers by example, with `<break>` tags, for chains, and
  says tag-based techniques do not render in realtime speech models. Amazon's older guide suggested
  "Well", "You know" and laughter words, and its newer guide says a phrase list "will use them very
  frequently" and that one or two example exchanges give more natural variety [chk-oai-rt-prompting,
  chk-el-flow, chk-lk-prompting, chk-aws-v1-prompting, chk-aws-prompts]. L.
- **Variety.** OpenAI adds a rule not to repeat a sentence and to vary replies, since the model follows
  sample phrases closely and can overuse them. LiveKit says to rotate openers such as "Sure" and "Got
  it" across turns [chk-oai-rt-prompting, chk-lk-prompting]. L.
- **Emotion and non-verbal sounds.** LiveKit says to set a calm baseline, to switch emotion rarely and
  not inside a sentence, and to cap non-verbal sounds at one per turn. Tag syntax such as `[laughs]`
  is provider-specific [chk-lk-prompting]. [voice-acting.md](voice-acting.md) compares the tag syntax
  of the makers. Amazon's older guide lists "visual formatting like bullet
  points", voice changes such as accent, age or singing, sound effects, and content that relies on
  being seen as things to leave out [chk-aws-v1-prompting]. L.
- **Persona.** OpenAI says its `gpt-realtime-1.5` model can "enact the specified role more reliably
  than earlier realtime preview models". LiveKit says to define personality as audible behaviors, such
  as how sentences start and how confusion is handled, not as adjectives. xAI says a persona
  statement keeps the model in character and in scope [chk-oai-rt-prompting, chk-lk-prompting,
  chk-xai-prompting]. L.

### Numbers, lists, names and language

- **Read digits one at a time.** OpenAI says to read identifiers back digit by digit with pauses, to
  convert spoken numbers to digits ("one nineteen" becomes 119), to ask for email addresses character by
  character and to confirm exact identifiers before a tool call. Amazon's older guide asks for one
  piece of information at a time and a character-by-character read-back of a booking code. Google's
  Vertex page says the model can repeat a digit sequence with wrong or missing digits and advises a
  read-back one digit at a time [chk-oai-rt-prompting, chk-aws-v1-prompting, chk-g-vertex-trouble]. L.
- **Written forms.** In a chain, the text-to-speech model reads symbols badly. ElevenLabs normalizes
  numbers and symbols to words, in the prompt by default or with its own normalizer that adds a small
  delay and keeps clean transcripts. LiveKit's output rules say to spell out numbers, phone numbers
  and email addresses, and to omit "https://" from a spoken URL [chk-el-prompting, chk-lk-prompting].
  xAI has a `replace` map for pronunciation and key terms to bias transcription [chk-xai-s2s]. L.
- **Lists.** Amazon's guides say to avoid bullets, tables and code, and to give one point at a time
  with signposts such as "first", "second" and "finally". LiveKit says to answer in plain text with
  no lists or markdown. Amazon's newer sample prompt says to avoid formatted lists or numbering and
  to keep output as a spoken transcript [chk-aws-v1-prompting, chk-lk-prompting, chk-aws-prompts]. L.
- **Language and accent.** OpenAI says to pin one output language. Its list of rules that are too broad
  includes "Mirror the user". It says to switch only on a clear request or a substantive utterance in
  another language, and to control accent apart from language. Google's Gemini API pages say the
  native audio models detect the language and take no language code, so the system instruction names
  the language. Google Cloud's page says to set a `language_code` hint and to state the language in
  the instruction, since the model can switch on its own. Amazon says gender agreement in some
  languages needs a gender line in the prompt that matches the chosen voice [chk-oai-rt-prompting,
  chk-g-best, chk-g-capabilities, chk-g-vertex-trouble, chk-aws-prompts]. L.

### Unclear audio, silence and staying in character

- **Unclear audio.** OpenAI says to ask a short clarification and not to guess, call tools, reason or
  give a preamble on unclear audio. It says not to repeat the same clarification twice. Its note on
  wording: changing "inaudible" to "unintelligible" improved noisy input handling [chk-oai-rt-prompting].
  L.
- **Audio that is not for the assistant.** OpenAI's Realtime 2 guide gives a no-op tool,
  `wait_for_user`, for silence, hold music, television and side talk. The tool gives the model a valid
  action that is not speech. Google's proactive audio lets the model decide not to answer irrelevant
  content, and Gemini 3.8 Live keeps it on all the time [chk-oai-rt-prompting, chk-g-capabilities,
  chk-g-model38]. L.
- **Rule conflicts.** OpenAI says that `gpt-realtime-2` follows instructions more literally than
  earlier models. It says to drop overlapping "always", "never", "only" and "must" rules, and to scope
  a rule narrowly. Its example: confirm before writes, not before every action [chk-oai-rt-prompting].
  xAI says to use capitals for key rules and to turn symbolic logic into plain English [chk-xai-prompting].
  L.
- **Stay on topic.** Google's sample prompt tells the model to bring an off-track client back to the
  workflow. OpenAI's guide shows an example that swaps short instructions per conversation state
  through `session.update`; its last state ends the call politely [chk-g-best, chk-oai-rt-prompting].
  L.

### Ending a call

- ElevenLabs gives agents an `end_call` system tool with a required `reason` and an optional farewell
  message. The agent calls it when the task is done and the user is content, when both agree the
  conversation ended, or when the user asks to end it. The dashboard adds it by default; an agent made
  through the API needs it added [chk-el-endcall]. L.
- OpenAI's SIP guide gives hang-up and transfer (`refer`) endpoints for GPT-Live calls and for
  Realtime calls. For a clean end, OpenAI says to send `session.close` and wait
  for `session.closed` to read final usage. Its Realtime prompt guide lists escalation triggers: safety
  risk, a request for a human, severe dissatisfaction, repeated failure (two failed tool attempts on
  one task or three consecutive no-match or no-input events) and out-of-scope topics [chk-oai-sip, chk-oai-live-sessions,
  chk-oai-rt-prompting]. L.

## 6. Tools during a call (MONITOR)

- **Synchronous and asynchronous.** In Gemini 3.8 Live the default function mode is non-blocking.
  Scheduling can be `SILENT`, `WHEN_IDLE` or `INTERRUPTED`, so the model uses a result without
  speaking, after it finishes, or at once. Gemini 3.8 Live Extended Thinking supports only
  non-blocking calls, and its `turnComplete` no longer means the server is idle; the page tells
  clients to read `interaction_status` [chk-g-model38, chk-g-model38-et]. Amazon's Nova 2 Sonic is
  asynchronous by default. It keeps listening during a tool call, always passes a tool result to the
  model even if the user changed the request, and does not cancel pending calls [chk-aws-async]. L.
- **Delegation.** GPT-Live sends reasoning and tools to a backend. Updates go back through three
  events: `session.instructions.append` for system-level direction, `session.thinking.append` for
  quiet context, and `session.commentary.append` for text to say aloud. Each holds up to 500 tokens.
  OpenAI says to match spoken updates to the verified task state, to wait for the backend before a
  price, a booking confirmation or a completion report, and to check whether an action already
  happened before a retry. It tracks changed requests with a task revision and discards results for
  outdated ones [chk-oai-live-delegation, chk-oai-live-prompting]. L.
- **Preambles.** OpenAI says to speak one short sentence before a slow tool call. It sets tool
  behavior per risk: call read-only tools when intent is clear, confirm high-precision identifiers
  first, and summarize and confirm before writes or account changes. It adds rules for tool failures
  and for tool lists that change [chk-oai-rt-prompting]. L.
- **Overlapping audio.** xAI says its server sends all audio first and then the function-call events.
  A client that sends the result and `response.create` at once gets overlapping audio. xAI advises
  waiting for playback to end before `response.create` and showing a thinking cue meanwhile
  [chk-xai-s2s]. L.
- **Spoken-input errors.** Amazon's older guide says to design tool calls for speech recognition
  errors, since users cannot see the tools, and to confirm verbally when a tool is consulted
  [chk-aws-v1-prompting]. ElevenLabs says to write tool descriptions with exact parameter formats,
  to say when each tool applies and to write a section on tool failures [chk-el-prompting]. L.
- **Limits.** Alibaba says web search and tool calling cannot be used together in one session
  [chk-ali-realtime]. Google says the Live API has no automatic tool-response handling; the client
  must send each response [chk-g-tools]. L.
- **One practitioner report.** A March 2026 forum post on Gemini Live on Vertex AI (A) reports that,
  without client-side audio gating, the model narrated about 40 percent of tool calls despite silent
  scheduling. It says the Vertex AI protobuf strips the `SILENT` scheduling flag. It also reports that
  context sent with `turnComplete` true cut the model off mid-sentence, and that the fix was to buffer
  context until the model turn and its playback ended [chk-forum-gemini]. A.

## 7. Failure modes in live calls (MONITOR)

| Symptom | What makers' docs say | Practitioner reports |
| --- | --- | --- |
| The agent cuts the user off | Raise the silence window or use semantic detection. Google: 500 to 800 ms. OpenAI: semantic VAD with lower eagerness. Amazon: LOW sensitivity. LiveKit: turn-detector model, higher `min_delay`, voice isolation if noise fires VAD [chk-g-capabilities, chk-oai-vad, chk-aws-turn, chk-lk-tuning] | One report on Gemini Live found that VAD sensitivity changes traded hanging sessions for repetition [chk-forum-gemini] (A) |
| Short acknowledgments stop the agent | LiveKit: adaptive interruption mode, a minimum word count or duration, and resume after silent false positives. OpenAI GPT-Live: a backchannel policy line [chk-lk-tuning, chk-oai-live-prompting] | None read |
| The agent keeps talking after the user speaks | Flush the playback buffer on the interrupt signal (Google, Amazon). Stream audio in 20 to 40 ms chunks, or the model sends no interrupt signal (Google) [chk-g-vertex-trouble, chk-aws-barge] | None read |
| A reply stops mid-sentence | Google: `turn_complete` true unconditionally interrupts generation. OpenAI: appended instructions and moderation can cut speech, and a moderation cut sends an `error` event without ending the session [chk-g-model38, chk-oai-live-sessions] | A Gemini Live post reports context injection that cut the model off [chk-forum-gemini] (A) |
| Long silence, no reply | Google: with VAD off the model waits for `activityStart` and `activityEnd`. OpenAI: a tool call or backend task shows as silence, so speak a preamble. Idle re-engagement settings exist at xAI (`idle_timeout_ms`), Alibaba (5 to 30 s, Qwen3.5-Omni realtime models in server VAD mode only) and ElevenLabs (turn timeout, 1 to 30 s) [chk-g-vertex-trouble, chk-oai-rt-prompting, chk-xai-s2s, chk-ali-client-events, chk-el-flow] | None read |
| The agent answers hold music or side talk | OpenAI: the `wait_for_user` tool. Google: proactive audio [chk-oai-rt-prompting, chk-g-capabilities] | None read |
| The agent hears itself (echo) | Alibaba says to use headphones, so echo does not trigger interruption. Kyutai says its web client adds echo cancellation and its command-line clients do not. LiveKit lists WebRTC echo cancellation and noise suppression [chk-ali-python-sdk, chk-moshi-readme, chk-lk-nc] | A 2024 OpenAI forum thread reports the model answering itself on a speaker and microphone setup. Replies suggest echo cancellation and muting input while the model speaks [chk-forum-oai-echo] (A) |
| Wrong digits or names | Read back one digit at a time and ask for repeats (Google, OpenAI, Amazon). OpenAI says to confirm identifiers before tool calls [chk-g-vertex-trouble, chk-oai-rt-prompting, chk-aws-v1-prompting] | None read |
| The language changes | Pin the language in the prompt and hint it in the setup (OpenAI, Google) [chk-oai-rt-prompting, chk-g-vertex-trouble] | None read |
| Speech speeds up, or the voice changes for one turn | Google documents both. It says to cap turns at about 50 s or 100 words and to return control to the user [chk-g-vertex-trouble] | None read |
| Drift or lost instructions in a long session | OpenAI and Google summarize or compress, and say that details can be lost. OpenAI says to mark current and stale facts in structured context. The application should keep confirmed facts and task state [chk-oai-live-sessions, chk-g-vertex-trouble, chk-oai-rt-prompting] | One post reports that injected context left the window within 10 to 15 minutes, answered by session cycling [chk-forum-gemini] (A) |
| The connection drops | Google lists codes 1000 and 1006. Its causes are no context compression, no resumption logic and a weak network. Its steps are to enable compression and session resumption, and to handle GoAway [chk-g-vertex-trouble, chk-g-best] | One Gemini Live post reports code 1011 on the first user turn after the greeting. Its recovery steps were filler audio, a resume handle and transcription of the buffered audio [chk-forum-gemini] (A) |

L unless marked A. The table gives each maker's stated step. The sources do not rank the steps.

## 8. Session limits, long sessions and reconnection (VOLATILE)

| Maker | Limit | How to continue |
| --- | --- | --- |
| OpenAI Realtime | A session lasts at most 60 minutes. `gpt-realtime-2` has a 128,000-token context window, about 1 to 2 hours of dense audio by OpenAI's estimate [chk-oai-rt-conv, chk-oai-rt-prompting] | The pages read give no resume handle. The context can be rebuilt from saved items |
| OpenAI GPT-Live | A duration limit ends a session with reason `expired` (no figure on the pages read). Context is 128,000 tokens [chk-oai-live-sessions] | Above 90 percent of context, GPT-Live prepares a replacement engine in the same session with the original instructions and up to 8,192 tokens of recent history and a summary. After an end, fork a stored recording (kept 30 days) or start a new session with saved text history of up to 128 messages and 8,192 tokens |
| Google Gemini Live | Without compression: 15 minutes for audio-only and 2 minutes for audio and video. A connection lasts about 10 minutes. Context is 128,000 tokens for native audio models [chk-g-session, chk-g-capabilities] | Context window compression lifts the session limit. Resumption handles from `SessionResumptionUpdate` stay valid 2 hours after the session ends. A GoAway message gives `timeLeft` before a connection closes |
| Amazon Nova 2 Sonic | A connection lasts 8 minutes. The model card lists a 1-million-token context window [chk-aws-s2s, chk-aws-card] | The Nova pages point to code samples for connection renewal and session continuation. The pages read give no resume handle |
| Alibaba Qwen Omni realtime | A WebSocket session lasts up to 120 minutes. When the history limit is exceeded, the oldest history is discarded [chk-ali-realtime] | New session |
| xAI speech-to-speech | History is lost when the socket closes unless resumption is on | Opt in with `resumption.enabled` and pass the `conversation_id` on reconnect. History expires after 30 minutes of inactivity [chk-xai-s2s] |
| ElevenLabs Agents | The maximum call length defaults to 600 s and ranges from 60 to 7,200 s [chk-el-flow] | New conversation |

L.

- **After a drop, check the work first.** OpenAI says to keep task state outside the voice session.
  After a lost connection, check what the backend finished, restore the state, and route late results
  to the new session so they cannot overwrite newer work. A closed session cannot listen, so a restart
  needs a button, push-to-talk or a local trigger, and the first words of the caller need buffering
  [chk-oai-live-sessions]. L.
- **Closing idle sessions.** OpenAI says to close a GPT-Live session during long gaps and to pick an
  idle timeout by comparing avoided minutes with the cost and delay of a new session. Muting the
  microphone does not stop the session [chk-oai-live-sessions, chk-oai-cost]. L.
- **Compression has a cost.** Google says compression "might impact the quality of the conversation"
  since the model drops early history. OpenAI says older details "may be summarized or omitted" and
  that important facts and current task state belong in the application [chk-g-vertex-trouble,
  chk-oai-live-sessions]. L.
- **Benchmarks agree.** MTR-DuplexBench (2025-11-13) reports that full-duplex models do not keep
  consistent performance over several rounds and several measures. Full-Duplex-Bench-v2 (2025-10-09)
  reports confusion when people talk at the same time, trouble with corrections, and lost track of
  who or what is discussed [chk-mtr, chk-fdb2]. M.

## 9. Evaluating voice agents (STABLE)

**What makers say to test.** OpenAI says to test the conversation and the finished task: for a
booking agent, listen to the confirmation and check that the correct appointment was saved. It says
to save the audio, events, tool results and application state, and to tell a failed run from a valid
run in which the agent fails. It names four GPT-Live dimensions: task and tool outcomes,
conversational timing (audible response time, silence, overlap, yielding), speech and language
(accents, noise, names, numbers) and session reliability (dropped audio, timeouts). It adds human
listening for pronunciation and pacing. It suggests three stages: synthetic speech for fixed
single-turn requests, replay of human recordings, then an independent simulated caller for
multi-turn calls with interruptions and changed requirements [chk-oai-voice-agents]. L.

**Other makers' test tools.** ElevenLabs offers simulation tests (multi-turn, with a simulated user),
next-reply tests and tool-call tests, and it can turn a real conversation into a test case. It says to
change one thing at a time and to re-run the same cases. LiveKit offers behavioral tests, beta
simulations with an LLM-driven user and session observability [chk-el-testing, chk-el-prompting,
chk-lk-prompting]. L.

**Published benchmarks.**

| Benchmark | Date | What it measures | What it reports |
| --- | --- | --- | --- |
| Full-Duplex-Bench v1 [chk-fdb1] | 2025-03-06 | Pause handling, backchanneling, turn taking, interruption management, with automatic metrics | Method. The abstract names no scores |
| Full-Duplex-Bench v1.5 [chk-fdb15] | 2025-07-30 | Four overlap cases (interruption, backchannel, talk to others, background speech): behavior class, stop and response latency, prosody | Two strategies across five agents: responsive and floor-holding |
| Full-Duplex-Bench-v2 [chk-fdb2] | 2025-10-09 | Multi-turn tasks (daily, correction, entity tracking, safety) with an automated examiner at two paces | Confusion on simultaneous talk, weak corrections, lost entities |
| MTR-DuplexBench [chk-mtr] | 2025-11-13 | Multi-round conversation: turn features, dialogue quality, instruction following, safety | Inconsistent performance across rounds |
| FD-Bench [chk-fdbench] | 2025-07-25 | Interruptions, delays and robustness with a pipeline of LLM, TTS and ASR | Three open systems failed some interruptions, more so under noise |
| τ-voice [chk-tauvoice] | 2026-03-14 | Task completion on 278 customer-service tasks with a simulated caller, accents and noise | Voice agents 31 to 51 percent clean, 26 to 38 percent noisy, text reference 85 percent |
| Big Bench Audio (Artificial Analysis) [chk-aa-method] | method read 2026-10-03 | 1,000 spoken reasoning questions from Big Bench Hard, scored by a judge model | See the leaderboard |

M. All but the last are research papers.

- **Independent index.** Artificial Analysis combines four equal parts: speech reasoning (Big Bench
  Audio), agentic performance (τ-voice, run by Artificial Analysis in airline, retail and telecom
  domains with three trials per task), a human arena preference and a task success rate. Its
  conversational-dynamics figures use subsets of Full-Duplex-Bench v1 and v1.5. On 2026-10-03 the
  agentic scores of the listed models range from 15 to 69 percent, and one OpenAI GPT-Live
  configuration scores 67.9 percent [chk-aa-method, chk-aa-board]. M.
- **Judge limits.** Big Bench Audio answers are scored by a judge model, so the limits in
  [llm-as-judge.md](llm-as-judge.md) apply [chk-aa-method]. τ-voice runs its user simulator apart from
  wall-clock time, so a strong language model can play the caller. The authors say the failures it
  found come from the agent's behavior under their setup [chk-tauvoice]. M.

## 10. Audio data, retention and consent (VOLATILE)

| Maker and product | What the docs say on 2026-10-03 |
| --- | --- |
| OpenAI GPT-Live | Not used for training. 30 days of abuse-monitoring retention. No application state, or 30 days if `store` is true. Zero Data Retention (ZDR) is available, and then `store` counts as false and forking is not available. US and EU data residency. Recordings are stereo WAV, input on the left channel. No public delete endpoint for stored sessions [chk-oai-data, chk-oai-live-sessions] |
| OpenAI Realtime | Not used for training. 30 days of abuse-monitoring retention. No application state. ZDR eligible. Tracing is not EU data-residency compliant [chk-oai-data] |
| Google Gemini API | Unpaid services: content can improve Google products, and human reviewers may read it after it is disconnected from the account. The terms say not to send sensitive, confidential or personal information to unpaid services. Paid services: no product training; prompts and responses are logged for a limited time to detect abuse. The page lists files such as images and video; it does not name Live audio [chk-g-terms] |
| ElevenLabs Agents | Transcripts and audio kept 2 years by default. The setting accepts a number of days, -1 for unlimited and 0 for scheduled deletion, for transcripts and audio apart. An audio-saving switch controls whether recordings are kept. Redaction of sensitive entities (replaced by placeholders in text and a bleep in audio) is for enterprise clients only [chk-el-retention, chk-el-privacy] |
| Amazon Nova 2 Sonic | Not read for this page. The Bedrock model card lists abuse detection and guardrails as not supported for this model [chk-aws-card] |

L.

- **Disclosure lines.** OpenAI shows a first-turn disclosure through `session.instructions.append`
  (for example "This call may be recorded for quality and training purposes"). It says the instruction
  acknowledgment shows only that the text was accepted, so check the audio, and for exact wording play
  a verified recording [chk-oai-live-sessions]. xAI's `force_message` speaks a fixed line as text to
  speech and can be made uninterruptible [chk-xai-s2s]. L.
- **United States.** The FCC adopted a declaratory ruling on 2024-02-02, released 2024-02-08. It
  confirms that the TCPA restriction on an "artificial or prerecorded voice" covers current AI
  technologies that generate human voices, including voice cloning. Such calls need the prior express
  consent of the called party, unless an emergency or an exemption applies, and must carry the
  identification and disclosure information that the rules require [chk-fcc]. S. This covers calls
  placed by the caller's side. It is not a general rule on recording consent.
- **European Union.** Article 50 of the AI Act says providers must make sure that people are informed
  that they interact with an AI system, unless that is obvious from the context. It also says providers
  of systems that generate synthetic audio must mark outputs in a machine-readable way. The text
  applies from 2026-08-02. A law-firm note of 2026-08-03 says providers of systems already on the
  market have until 2026-12-02 for the marking duty [chk-euai, chk-eu-note]. S, with a law-firm note
  (A).
- **Rules on recording consent** differ by place and are not covered here. No primary source on them
  was read.

## What the evidence supports (inference)

1. The three architectures differ mainly in who controls the next step. A chain exposes text between
   stages. A single model hides it. GPT-Live splits voice from reasoning and gives the application the
   task state. This follows from the maker pages in section 1.
2. A turn setting has no neutral default. The values in section 3 are not comparable across makers.
   Evidence for a value comes from a trial on real calls with the maker's own settings and a metric
   such as pause handling.
3. Every maker puts the playback buffer in the client. Interruption failures that are not about VAD
   are buffer failures, according to the Google, Amazon and OpenAI pages.
4. The makers' prompt guides agree on length, plain spoken text, one question at a time and digit
   read-back. They disagree on fillers. A reader who needs both can read sections 5 and 6 together.
5. Long sessions lose detail by design: summaries, compression and discarded history. The guides
   agree that the application should hold the facts that matter.
6. Benchmarks that run whole tasks (τ-voice, Full-Duplex-Bench-v2) show larger gaps than single
   questions (Big Bench Audio). This follows from the figures in sections 2 and 9.

## Limits and open questions

- Maker pages change often. Section 8 limits and section 1 prices come from pages read on 2026-10-03.
  GPT-Live, Gemini 3.8 Live and Nova 2 Sonic have documentation that says it covers more than one
  model name, and some Google pages still describe earlier Live models. Where two Google pages
  differ, this page follows the Gemini 3.8 Live model page.
- The OpenAI VAD page names `server_vad` as the default. Examples elsewhere set `semantic_vad`
  explicitly. The default should be read from the API reference before a design relies on it.
- Amazon's prompting pages for Nova 2 Sonic are shorter than the pages for the first model. This page
  cites the first model's guide where it says so.
- No maker publishes a latency figure for a whole call with tools. The only independent figures are
  for short questions with no tools.
- The cost of a chain against a single model for the same call is not published by any source read.
- The OpenAI Cookbook voice-evaluation harness and the OpenAI Realtime evaluation guide were named by
  OpenAI and not read.
- Practitioner reports (class A) are single posts from forums. They show what can happen. They do not
  show how often.
- Pipecat, Vapi, Twilio and Deepgram pages were not read. Telephony details (SIP, codecs, DTMF) are
  covered only where a maker page named them.
- Speech synthesis and transcription models of other makers are outside this page, except as the
  speech side of the chains described above. The synthesis models that take direction for emotion,
  tone and character are compared in [voice-acting.md](voice-acting.md).

## Sources

Read 2026-10-03 unless dated otherwise. Ids in brackets are used in the text above.

OpenAI

- [chk-oai-voice-agents] OpenAI, voice agents <https://developers.openai.com/api/docs/guides/voice-agents>.
- [chk-oai-live] OpenAI, getting started with GPT-Live <https://developers.openai.com/api/docs/guides/live>.
- [chk-oai-live-prompting] OpenAI, prompting GPT-Live
  <https://developers.openai.com/api/docs/guides/live-prompting>.
- [chk-oai-live-sessions] OpenAI, managing GPT-Live sessions
  <https://developers.openai.com/api/docs/guides/live-conversations>.
- [chk-oai-live-delegation] OpenAI, delegation and tools in GPT-Live
  <https://developers.openai.com/api/docs/guides/live-delegation>.
- [chk-oai-cost] OpenAI, cost optimization <https://developers.openai.com/api/docs/guides/voice-latency-cost?api=live>.
- [chk-oai-vad] OpenAI, voice activity detection <https://developers.openai.com/api/docs/guides/realtime-vad>.
- [chk-oai-rt-conv] OpenAI, Realtime conversations
  <https://developers.openai.com/api/docs/guides/realtime-conversations>.
- [chk-oai-rt-prompting] OpenAI, prompting Realtime models
  <https://developers.openai.com/api/docs/guides/realtime-models-prompting>.
- [chk-oai-live-model] OpenAI, GPT-Live 1 model page <https://developers.openai.com/api/docs/models/gpt-live-1>.
- [chk-oai-rt2-model] OpenAI, GPT-Realtime-2 model page
  <https://developers.openai.com/api/docs/models/gpt-realtime-2>.
- [chk-oai-sip] OpenAI, telephony and SIP <https://developers.openai.com/api/docs/guides/voice-sip>.
- [chk-oai-data] OpenAI, data controls <https://developers.openai.com/api/docs/guides/your-data>.

Google

- [chk-g-best] Google, Live API best practices
  <https://ai.google.dev/gemini-api/docs/live-api/best-practices>.
- [chk-g-capabilities] Google, Live API capabilities
  <https://ai.google.dev/gemini-api/docs/live-api/capabilities>.
- [chk-g-session] Google, Live API session management
  <https://ai.google.dev/gemini-api/docs/live-api/session-management>.
- [chk-g-tools] Google, Live API tool use <https://ai.google.dev/gemini-api/docs/live-api/tools>.
- [chk-g-model38] Google, Gemini 3.8 Live, latest update September 2026
  <https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live>.
- [chk-g-model38-et] Google, Gemini 3.8 Live Extended Thinking
  <https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking>.
- [chk-g-vertex-trouble] Google Cloud, troubleshooting Gemini Live API, updated 2026-10-01
  <https://docs.cloud.google.com/vertex-ai/generative-ai/docs/live-api/troubleshooting>.
- [chk-g-terms] Google, Gemini API additional terms <https://ai.google.dev/gemini-api/terms>.

Amazon

- [chk-aws-turn] Amazon, Nova 2 turn-taking controllability
  <https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-turn-taking.html>.
- [chk-aws-barge] Amazon, Nova 2 barge-in
  <https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-barge-in.html>.
- [chk-aws-async] Amazon, Nova 2 asynchronous tool calling
  <https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-async-tools.html>.
- [chk-aws-s2s] Amazon, Nova 2 Sonic speech-to-speech overview
  <https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html>.
- [chk-aws-prompts] Amazon, Nova 2 voice conversation prompts
  <https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-system-prompts.html>.
- [chk-aws-v1-prompting] Amazon, Nova Sonic (first model) prompting guides
  <https://docs.aws.amazon.com/nova/latest/userguide/prompting-speech-best-practices.html>,
  <https://docs.aws.amazon.com/nova/latest/userguide/prompting-speech-bp-speech.html>,
  <https://docs.aws.amazon.com/nova/latest/userguide/prompting-speech-bp-tools.html> and
  <https://docs.aws.amazon.com/nova/latest/userguide/prompting-speech-bp-avoid.html>.
- [chk-aws-card] Amazon Bedrock, Nova 2 Sonic model card
  <https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-sonic.html>.

Other makers and frameworks

- [chk-ali-realtime] Alibaba Cloud, Qwen Omni realtime guide
  <https://www.alibabacloud.com/help/en/model-studio/realtime>.
- [chk-ali-client-events] Alibaba Cloud, realtime client events
  <https://www.alibabacloud.com/help/en/model-studio/client-events>.
- [chk-ali-python-sdk] Alibaba Cloud, Omni realtime Python SDK
  <https://help.aliyun.com/en/model-studio/omni-realtime-python-sdk>.
- [chk-xai-s2s] xAI, speech to speech <https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech.md>.
- [chk-xai-prompting] xAI, speech-to-speech prompting guide
  <https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech/prompting-guide.md>.
- [chk-el-flow] ElevenLabs, conversation flow
  <https://elevenlabs.io/docs/eleven-agents/customization/conversation-flow>.
- [chk-el-prompting] ElevenLabs, prompting guide
  <https://elevenlabs.io/docs/eleven-agents/best-practices/prompting-guide>.
- [chk-el-retention] ElevenLabs, retention
  <https://elevenlabs.io/docs/eleven-agents/customization/privacy/retention>.
- [chk-el-privacy] ElevenLabs, privacy <https://elevenlabs.io/docs/eleven-agents/customization/privacy>.
- [chk-el-endcall] ElevenLabs, end call tool
  <https://elevenlabs.io/docs/eleven-agents/customization/tools/system-tools/end-call>.
- [chk-el-testing] ElevenLabs, agent testing
  <https://elevenlabs.io/docs/eleven-agents/customization/agent-testing>.
- [chk-el-pricing] ElevenLabs, agents pricing <https://elevenlabs.io/pricing/agents>.
- [chk-lk-turns] LiveKit, turn detection and interruptions <https://docs.livekit.io/agents/logic/turns>.
- [chk-lk-tuning] LiveKit, turn-taking tuning <https://docs.livekit.io/agents/logic/turns/tuning>.
- [chk-lk-prompting] LiveKit, prompting guide <https://docs.livekit.io/agents/start/prompting>.
- [chk-lk-nc] LiveKit, noise and echo cancellation
  <https://docs.livekit.io/transport/media/noise-cancellation>.
- [chk-moshi-readme] Kyutai, Moshi repository README <https://github.com/kyutai-labs/moshi>.
- [chk-unmute] Kyutai, Unmute repository README <https://github.com/kyutai-labs/unmute>.
- [chk-kyutai-stt] Kyutai, Kyutai STT <https://kyutai.org/stt>.

Research and measurement

- [chk-moshi-paper] Défossez, Mazaré, Orsini, Royer, Pérez and others, Moshi: a speech-text foundation
  model for real-time dialogue, submitted 2024-09-17 <https://arxiv.org/abs/2410.00037>.
- [chk-fdb1] Lin and others, Full-Duplex-Bench, 2025-03-06 <https://arxiv.org/abs/2503.04721>.
- [chk-fdb15] Lin and others, Full-Duplex-Bench v1.5, 2025-07-30 <https://arxiv.org/abs/2507.23159>.
- [chk-fdb2] Lin and others, Full-Duplex-Bench-v2, 2025-10-09 <https://arxiv.org/abs/2510.07838>.
- [chk-mtr] Zhang and others, MTR-DuplexBench, 2025-11-13 <https://arxiv.org/abs/2511.10262>.
- [chk-fdbench] Peng and others, FD-Bench, 2025-07-25 <https://arxiv.org/abs/2507.19040>.
- [chk-tauvoice] Ray, Dhandhania, Barres, Narasimhan and others, τ-voice, 2026-03-14
  <https://arxiv.org/abs/2603.13686>.
- [chk-aa-method] Artificial Analysis, speech to speech benchmarking methodology
  <https://artificialanalysis.ai/methodology/speech-to-speech-benchmarking>.
- [chk-aa-board] Artificial Analysis, speech to speech leaderboard, read 2026-10-03
  <https://artificialanalysis.ai/speech-to-speech>.
- [chk-stivers] Stivers and others, Universals and cultural variation in turn-taking in conversation,
  PNAS 2009, abstract read through Europe PMC <https://doi.org/10.1073/pnas.0903616106>.
- [chk-webrtchacks] Hancke, measuring the response latency of OpenAI's WebRTC-based Realtime API,
  published 2025-04-01 (measured 2025-01-04)
  <https://webrtchacks.com/measuring-the-response-latency-of-openais-webrtc-based-real-time-api/>.
- [chk-soniox] Soniox, voice agent latency budget, 2026-07-02 <https://soniox.com/wiki/voice-agent-latency-budget>.
- [chk-forum-gemini] Google AI developer forum, hard-won patterns for building voice apps with Gemini
  Live, posts of 2026-03-03 and 2026-03-20
  <https://discuss.ai.google.dev/t/hard-won-patterns-for-building-voice-apps-with-gemini-live-march-2026/128155>.
- [chk-forum-oai-echo] OpenAI developer forum, Realtime API starts to answer itself with a microphone
  and speaker setup, 2024-10-13
  <https://community.openai.com/t/realtime-api-starts-to-answer-itself-with-mic-speaker-setup/977801>.

Law

- [chk-fcc] FCC, declaratory ruling FCC 24-17, adopted 2024-02-02, released 2024-02-08
  <https://docs.fcc.gov/public/attachments/FCC-24-17A1.pdf>, text of the ruling read 2026-10-03.
- [chk-euai] EU AI Act, Article 50, text on <https://artificialintelligenceact.eu/article/50/>.
- [chk-eu-note] Cooley, EU AI Act transparency obligations take effect 2 August 2026, 2026-08-03
  <https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026>.
