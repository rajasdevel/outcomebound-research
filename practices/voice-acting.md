---
last_checked: 2026-10-04
volatility: MONITOR (model ids, tag lists, limits, consent rules and benchmark standings change at each release) / STABLE (the SSML standard and the evaluation methods)
sources:
  - https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices
  - https://elevenlabs.io/docs/overview/models
  - https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4
  - https://elevenlabs.io/blog/emotional-text-to-speech-with-eleven-v4
  - https://elevenlabs.io/blog/eleven-v4-turbo-in-elevenagents
  - https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue
  - https://elevenlabs.io/docs/eleven-api/concepts/voice-cloning
  - https://elevenlabs.io/docs/eleven-creative/voices/voice-design
  - https://elevenlabs.io/docs/eleven-agents/customization/voice/expressive-mode
  - https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/request-stitching
  - https://elevenlabs.io/docs/eleven-agents/customization/voice/pronunciation-dictionary
  - https://elevenlabs.io/safety
  - https://elevenlabs.io/docs/eleven-creative/audio-tools/audio-detector
  - https://ai.google.dev/gemini-api/docs/speech-generation
  - https://ai.google.dev/gemini-api/docs/voice-design
  - https://ai.google.dev/gemini-api/docs/voice-replication
  - https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/
  - https://developers.openai.com/api/docs/guides/text-to-speech
  - https://developers.openai.com/api/docs/guides/custom-voices
  - https://developers.openai.com/api/docs/deprecations
  - https://dev.hume.ai/docs/text-to-speech-tts/acting-instructions
  - https://dev.hume.ai/docs/text-to-speech-tts/overview
  - https://www.hume.ai/blog/introducing-the-hume-voice-controllability-leaderboard
  - https://docs.inworld.ai/tts/capabilities/steering
  - https://docs.inworld.ai/tts/best-practices/prompting-for-tts-2
  - https://docs.cartesia.ai/build-with-cartesia/capability-guides/volume-speed-emotion.md
  - https://docs.cartesia.ai/build-with-cartesia/capability-guides/ssml-tags.md
  - https://www.cartesia.ai/legal/disclosure-requirements
  - https://platform.minimax.io/docs/api-reference/speech-t2a-http
  - https://docs.fish.audio/developer-guide/core-features/emotions
  - https://docs.fish.audio/resources/best-practices/voice-cloning
  - https://docs.x.ai/developers/model-capabilities/audio/text-to-speech
  - https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice
  - https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/custom-neural-voice/limited-access-custom-neural-voice
  - https://www.w3.org/TR/speech-synthesis11/
  - https://mimo.xiaomi.com/mimo-v2-5-tts
  - https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign
  - https://www.alibabacloud.com/help/en/model-studio/qwen3-tts-instruct-flash
  - https://docs.mistral.ai/capabilities/audio/text_to_speech
  - https://huggingface.co/ResembleAI/chatterbox-turbo
  - https://artificialanalysis.ai/methodology/text-to-speech
  - https://arxiv.org/abs/2505.23009
  - https://arxiv.org/abs/2506.16381
  - https://arxiv.org/abs/2604.17958
  - https://arxiv.org/abs/2506.05984
  - https://arxiv.org/abs/2608.00545
  - https://arxiv.org/abs/2607.14846
  - https://hume.ai/blog/octave-2-launch
  - https://www.hume.ai/blog/newly-released-google-s-gemini-3-8-flash-tts-tops-hume-s-real-world-voiceeq-leaderboard
  - https://docs.x.ai/developers/model-capabilities/audio/custom-voices
  - https://docs.fish.audio/resources/best-practices/text-to-speech
  - https://docs.inworld.ai/tts/tts-models
  - https://docs.cartesia.ai/build-with-cartesia/tts-models/latest
  - https://elevenlabs.io/docs/changelog/2026/9/28
  - https://elevenlabs.io/docs/eleven-agents/best-practices/prompting-guide
  - https://www.itu.int/rec/T-REC-P.800-199608-I
  - https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview
  - https://docs.fcc.gov/public/attachments/FCC-24-17A1.pdf
  - https://artificialintelligenceact.eu/article/50/
  - https://huggingface.co/bosonai/higgs-tts-3-4b
  - https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html
---

# Voice acting with speech synthesis models

Re-check when a maker ships a new speech synthesis model, changes its tag syntax or consent rules, or
when a benchmark changes its method. In any case re-check the ids, limits and consent rules by
2026-10-18, and the rest by 2027-04-01.

How makers say to direct the delivery of synthetic speech, and what independent measurers found. A
*voice actor model* is a speech synthesis model whose delivery can be directed with natural-language
instructions or with tags in the text, beyond the choice of a voice. Delivery means emotion, tone,
pace, accent, character and non-verbal sounds. The page compares four ways to direct delivery. It
covers voice design and cloning, emotion limits, consistency across lines, multi-speaker scenes,
non-verbal sounds, pronunciation, the cost of low latency and the ways to evaluate the result. It ends
with disclosure, watermarks and the consent rules of makers. For anyone who writes scripts for a
speech model, picks one, or builds a pipeline around one.

Models that hold a live conversation are in [voice-agents.md](voice-agents.md). Turn-taking, barge-in
and session limits do not apply to a synthesis model, so this page leaves them out. The files of the
models are in the maker folders: [ElevenLabs](../models/elevenlabs/README.md),
[Google](../models/google/README.md), [OpenAI](../models/openai/README.md),
[Hume](../models/hume/README.md), [Alibaba](../models/alibaba/README.md),
[MiniMax](../models/minimax/README.md), [Boson AI](../models/boson/README.md) and [xAI](../models/xai/README.md). General rules for
prompts are in [prompting.md](prompting.md) and [writing-for-models.md](writing-for-models.md). Rules
for judges that score output are in [llm-as-judge.md](llm-as-judge.md).

**Evidence classes**, as in [the conventions](../CONVENTIONS.md): M measured; L maker or vendor
documentation or guidance; S standard or law; P practitioner consensus; A anecdote or one
uncontrolled report. **Citations.** Bracketed `[vd-…]` ids are pages read on 2026-10-04. They are
listed under Sources. Most claims here are a maker that describes its own product (L). Where a maker
names a feature, this page says what the maker documents. It does not say that the feature works well.
Model names change fast. The names here are the names on the maker pages on 2026-10-04.

**What this page leaves out.** A model that offers only a choice of voices is not a voice actor
model. A model that offers only SSML rate and pitch is not one either. Mistral's Voxtral TTS is an
example of a third kind: it takes a reference clip and copies its delivery, with no tags and no
instruction field [vd-mistral]. Amazon Polly is an example of the SSML kind: its generative voices take
SSML for pauses, prosody, pronunciation and language, and its only style element (a newscaster style)
is for some neural voices only [vd-polly].

## Key findings

**VD1. Makers document four ways to direct delivery, and most models mix two or more.** The ways are a
free-text instruction (Google, Hume, Inworld, Alibaba, Xiaomi, OpenAI), inline tags (ElevenLabs, Google,
Fish Audio, xAI, MiniMax, Microsoft, Xiaomi, Boson AI), named parameters or SSML elements (Microsoft, Cartesia) and a
reference clip (Mistral, and every cloning product). Section 1 gives the table [vd-g-tts, vd-hume-act,
vd-inw-steer, vd-qwen-ali, vd-mimo, vd-oai-tts, vd-el-bp, vd-fish-emo, vd-xai-tts, vd-mm-t2a, vd-ms-ssml,
vd-cart-vse, vd-mistral, vd-higgs]. L.

**VD2. No tag syntax is shared.** ElevenLabs, Fish Audio and Inworld use square brackets. Google uses
angle brackets for sounds and a metadata field for style. MiniMax uses round brackets. xAI uses square
brackets for sounds and paired angle-bracket tags for style. Google says a stage direction left in the
transcript is read aloud. Inworld says older models may read its tags aloud [vd-g-tts, vd-inw-steer,
vd-mm-t2a, vd-xai-tts]. L.

**VD3. The guides agree on five points.** The direction has to fit the words. One segment carries one
emotion. The transcript reads as people speak. A voice finds it easier to do a delivery that it has
already learned. Tags need a test with the voice that ships. The guides differ on where the direction
goes, on how long a tag lasts and on whether a persona belongs in the prompt or in a saved voice
[vd-el-bp, vd-el-blog-emo, vd-inw-prompt, vd-fish-emo, vd-g-tts, vd-cart-ssml]. L.

**VD4. Direction works less well than the maker pages suggest.** In a vendor-run test of voice models,
age control scored 51.8 percent on average, and six of seven models scored lower when inline tags were
combined than when each was tested alone. An independent audit of three open models found a success rate of 4.8 percent for a
single sample when the target change had to leave other traits alone [vd-hume-lb, vd-attr-audit]. M.

**VD5. Makers give up control to gain speed.** Inworld says its fast model ignores instruction tags.
ElevenLabs sells separate models for expressive work and for real-time work. xAI documents a quality
cost at its lowest-latency setting. ElevenLabs says one fast model skips number normalisation to save
time [vd-inw-steer, vd-el-models, vd-xai-tts]. L.

**VD6. Consent rules differ in strength.** Google, OpenAI and Microsoft require a recorded statement
from the voice owner. ElevenLabs uses a voice-captcha check and says it cannot prove who owns a
recording. Fish Audio states its rules in guidance text. The xAI page and the Cartesia pages read state
no consent rule for a cloned voice [vd-g-repl, vd-oai-voices, vd-ms-limited, vd-el-clone, vd-fish-clone,
vd-cart-disc, vd-xai-voices]. L.

**VD7. Marking of synthetic audio is part of the product at three makers.** Google says every clip from
its audio models carries a SynthID watermark. ElevenLabs watermarks its own output and offers a detector.
Its older speech classifier, which the detector falls back to, is rated at 99 percent precision and
80 percent recall on unmodified files. Resemble's open model
embeds a watermark in each file. OpenAI and Microsoft require the customer to tell users that the voice
is synthetic [vd-g-blog, vd-el-detector, vd-chatterbox, vd-oai-tts, vd-ms-limited]. L.

**VD8. Evaluation is split between listener preference, instruction-following judges and
intelligibility checks.** Each answers a different question. A model that wins a preference arena can
still fail an instruction test, and the reverse [vd-aa-method, vd-instructtts, vd-emergent, vd-mint]. M.

## 1. Four ways to direct delivery (MONITOR)

| Way | Who documents it on 2026-10-04 | Form |
| --- | --- | --- |
| Free-text instruction for the whole request or turn | Google (`speech_metadata.style`), Hume Octave 1 (`description`), OpenAI (`instructions`), Alibaba (Qwen3-TTS-Instruct-Flash), Inworld (request-level `instruction` field), Xiaomi (MiMo-V2.5-TTS) | A sentence or a page of text, kept apart from the spoken text |
| Tags inside the text, free-form or from a fixed list | Free-form: Inworld (square brackets that last until `[reset]`), Fish Audio S2 (square brackets), ElevenLabs v3 and v4 (audio tags). Free-form tags are also in Xiaomi MiMo-V2.5-TTS. Fixed list: Google (sound tags in angle brackets), MiniMax (interjection tags in round brackets), xAI (inline and paired tags), Microsoft HD voices (style markers and paralinguistic tags), Boson AI Higgs TTS 3 (`<\|category:value\|>` tags), Chatterbox Turbo (three named tags "and more") | A short phrase or a listed tag at the point where it applies |
| Named parameters and SSML elements | Microsoft (`mstts:express-as` with a style, a degree and a role), Cartesia (an emotion setting, speed and volume), MiniMax (an emotion value), Hume (`speed`) | Values the maker defines per voice or per model |
| Reference clip | Mistral Voxtral TTS (delivery copied from the clip), every cloning product | Audio, from 2 seconds to 120 seconds across the docs read |

[vd-g-tts, vd-hume-act, vd-oai-tts, vd-qwen-ali, vd-inw-steer, vd-mimo, vd-fish-emo, vd-el-bp, vd-mm-t2a,
vd-xai-tts, vd-ms-ssml, vd-higgs, vd-chatterbox, vd-cart-vse, vd-mistral]. L.

- **Natural-language direction.** Google separates two scopes. Sustained delivery goes in a style field
  with phrases such as `whispered urgently`, `out of breath` or `sarcastic`. Momentary events go in the
  transcript as angle-bracket tags, for example `<sigh>` or `<short pause>`. Google says that a change of
  emotion in the middle of a speech needs a new turn with its own style [vd-g-tts]. Hume says to name
  precise emotions ("melancholy" in place of "sad"), to combine two elements such as `excited but
  whispering`, to name the audience, and to use the `speed` field for pace [vd-hume-act]. Inworld says that
  a layered instruction that holds mood, manner and intent works better than one word
  [vd-inw-prompt]. L.
- **Inline tags.** ElevenLabs describes square-bracket tags for emotion, whispers, laughs, accents and
  sound effects. It says that v4 follows tags that are outside the training data of a voice, but with
  uneven results [vd-el-bp]. Fish Audio S2 takes free-form text in square brackets. Its page lists 49
  emotions, 6 tone markers and 11 sound effects, and it takes free text beyond those lists [vd-fish-emo].
  xAI separates inline tags such as `[laugh]` from paired tags such as `<whisper>text</whisper>`. It says to
  wrap whole phrases, not single words [vd-xai-tts]. Boson AI's Higgs TTS 3 writes every tag as
  `<|category:value|>`, for example `<|emotion:relief|>`. Its card lists 21 emotions, 3 styles, 9 sound
  effects and prosody values for speed, pauses, pitch and expressiveness. The weights are under a research
  and non-commercial licence [vd-higgs]. L.
- **Parameters and SSML.** SSML 1.1 is a W3C Recommendation of 2010-09-07. It defines prosody (pitch,
  rate, volume), emphasis, breaks, `say-as`, `phoneme`, `sub` and lexicons. The word emotion does
  not occur in the Recommendation, and it has no element for emotion [vd-w3c-ssml]. Microsoft adds `mstts:express-as`. The style is voice-specific, and a missing
  or invalid style makes the service ignore the whole element. A degree from 0.01 to 2 sets the strength
  [vd-ms-ssml]. Cartesia lists 58 emotion values, such as angry, sad and scared, and ranges of 0.6 to 1.5 for speed
  and 0.5 to 2.0 for volume. It marks emotion control as beta in one page and as highly experimental when
  emotion changes within one generation [vd-cart-vse, vd-cart-ssml]. L.
- **Reference audio.** Mistral says its model follows the intonation, rhythm and emotion of the voice
  clip, so it needs no emotion tags. The clip can be as short as 2 to 3 seconds [vd-mistral]. ElevenLabs
  says that a delivery that exists in the training data of a voice is easier to reproduce, and that the
  pace of a voice depends on the audio that made it [vd-el-bp]. L.
- **SSML in the newer ElevenLabs models.** The v4 page says SSML is no longer supported and that the
  Style and Speed sliders are gone. The guide says v4 and v3 do not take SSML break tags, and that
  SSML phoneme tags work only with `eleven_flash_v2` [vd-el-v4, vd-el-bp]. L.

## 2. What the guides agree on and where they differ (MONITOR)

**Where the guides agree.**

- **The transcript is a script.** Google says the text field holds only the words to speak, and that
  direction inside it is read aloud. It advises natural spoken transcripts with disfluencies such as
  `Oh uh yeah I think... hm`. Inworld advises numbers as words, natural contractions and organic filler
  words [vd-g-tts, vd-inw-prompt]. L.
- **Direction must fit the words.** Inworld says a sad tag on a celebratory line degrades the output.
  Cartesia says an emotion setting pushes the model only when the emotion fits the transcript. Fish Audio
  lists conflicting emotion combinations as a failure [vd-inw-prompt, vd-cart-vse, vd-fish-emo]. L.
- **One direction at a time.** ElevenLabs advises one emotion per phrase and warns that contrasting
  emotions may give a less accurate result. Inworld warns that opposing directions in one tag, such as a
  whisper with `[very loud]`, give unpredictable results [vd-el-blog-emo, vd-inw-prompt]. L.
- **Pace through the dedicated control.** Hume says to use `speed` and not the description to set pace.
  Google puts pace in the style field and pauses in tags or punctuation. ElevenLabs says that ellipses
  slow a line and dashes cut a speaker off [vd-hume-act, vd-g-tts, vd-el-blog-emo]. L.
- **Stress through capitals.** Google, Inworld and ElevenLabs each say that capital letters add emphasis
  [vd-g-tts, vd-inw-prompt, vd-el-bp]. L.
- **Tags in English.** Google says to keep its sound tags in English for best results when the transcript is in another language.
  Inworld says its instructions must be in English even when the text is in another language
  [vd-g-tts, vd-inw-steer]. L.
- **Test with the target voice.** ElevenLabs says to test tags with the chosen voice, and says
  experimental tags vary across voices. Cartesia says emotions work reliably only with voices that it
  tags as emotive [vd-el-bp, vd-cart-ssml]. L.

**Where the guides differ.**

| Topic | What the makers say |
| --- | --- |
| Where the persona lives | Google says to build a character once in voice design and to keep the style field short or empty. ElevenLabs offers voice design and says professional clones suit production. Hume says that without instructions the model infers delivery from the voice description and the text [vd-g-tts, vd-el-design, vd-hume-act] |
| How long a tag lasts | Inworld: until `[reset]` or the next tag. Microsoft HD voices: until a `[Neutral]` marker, but a line break, a paragraph tag or an automatic sentence boundary also returns to the default style, and a break tag does not. ElevenLabs agents: about the next 4 to 5 words. Google: sound tags are momentary and the style field covers one turn [vd-inw-steer, vd-ms-ssml, vd-el-expr, vd-g-tts] |
| Whether to repeat the direction | Inworld says that an instruction on every sentence lowers continuity. Google says that extra text asking to keep a voice steady increases drift [vd-inw-steer, vd-g-tts] |
| Who writes the tags | Inworld describes a system prompt that makes a language model write steering tags. ElevenLabs agents add tags from a prompt. Google keeps sustained direction in a metadata field apart from the text [vd-inw-prompt, vd-el-expr, vd-g-tts] |
| Sound-effect tags | ElevenLabs lists sound effects such as `[applause]` and `[gunshot]` as tags. Google's migration advice removes sound-effect tags and keeps only vocal events [vd-el-bp, vd-g-tts] |

L.

**How the advice moved.** The ElevenLabs guide gives SSML break tags for the older models only, and SSML
phoneme tags for `eleven_flash_v2` only.
For v3 and v4 it gives square-bracket tags and punctuation. For v4 (2026-09-28) it adds IPA between
slashes, and the v4 page says SSML and the Style and Speed sliders are gone [vd-el-bp, vd-el-v4]. For Google, the earlier Gemini 3.1 Flash TTS preview (April 2026) used audio tags. Google now
calls it a legacy preview and tells new work to use Gemini 3.8 Flash TTS or Flash-Lite TTS. The 3.8 guide
moves sustained direction from inline text to a metadata field and keeps angle-bracket tags for vocal
events [vd-g-31, vd-g-model, vd-g-tts]. L.

## 3. Voice design and voice cloning (MONITOR)

### Voice design from a description

- **Google.** A prompted voice is created with `voices.create()` and saved. The call returns a voice id
  and a preview. A project can hold 200 voices, and each voice lives one year. The page lists age, gender,
  accent, timbre and delivery style as attributes. It advises fixed traits such as age, gender, timbre and
  accent at creation and the style field for situational emotion only [vd-g-design]. L.
- **ElevenLabs.** A design prompt yields three previews. The docs suggest a prompt with language, gender,
  age range, quality, persona, emotion and a note on timbre and pace. They say longer preview texts tend to
  give more stable and expressive results, and they call the feature experimental. A guidance setting
  trades prompt adherence against audio quality. On v4 a designed voice may be less performative than on
  earlier models [vd-el-design, vd-el-v4]. L.
- **Others.** Hume Octave 2 offers voice design in English, with more languages listed as coming [vd-hume-ov].
  Xiaomi offers a design model that needs no reference audio and sets age, accent, timbre and temperament
  from text [vd-mimo]. Alibaba's Qwen3-TTS has a VoiceDesign variant that takes an instruction for timbre,
  emotion and prosody under the Apache 2.0 licence [vd-qwen-hf]. L.
- **Measured.** In the Hume leaderboard, voice design is one of four dimensions. The top overall accent
  accuracy in the voice design tab is 45.4 percent (ElevenLabs v3), where chance is 17 to 33 percent by task. Age control averages 51.8 percent
  across models. Hume sells a competing model until its text-to-speech API ends on 2026-11-13, and it says unreleased Hume
  systems are hidden but still count in the matches [vd-hume-lb, vd-hume-ov]. M (vendor-run).

### Voice cloning

- **Two kinds.** ElevenLabs separates instant cloning (audio as a conditioning signal, under two minutes
  of audio) from professional cloning (parameter tuning on about 30 minutes of audio). It says the
  professional kind is more consistent across emotion and style, and that instant clones vary more across
  speech styles [vd-el-clone]. L.
- **Sample length.** Google asks for 10 to 30 seconds of clean speech and a consent recording from
  the same speaker. OpenAI takes at most 30 seconds. Fish Audio asks for at least 10 seconds, suggests 30 to 60 seconds when a
  clone sounds robotic, and says the sample should keep a steady tone and volume. xAI takes at most 120 seconds and says clips under 30 seconds may
  lack detail. Mistral says 2 to 3 seconds can work [vd-g-repl, vd-oai-voices, vd-fish-clone,
  vd-xai-voices, vd-mistral]. L.
- **Delivery control on a clone.** ElevenLabs says the agent mode with expressive tags does not keep the
  identity of a professional clone, and v3 gives lower clone quality for professional clones. Cartesia says
  request-time speed changes do not apply to its professional clones [vd-el-expr, vd-el-bp, vd-cart-vse]. L.

### Consent rules and policies

| Maker | What the page says on 2026-10-04 |
| --- | --- |
| Google | Two recordings from the same adult speaker: a reference clip and a spoken consent statement, read in one of 30 languages. The statement says the speaker owns the voice and consents to its use. The page says both recordings should use the same microphone and room so that the speaker check succeeds. Stateful voices live 1 year. Stateless keys live 7 days [vd-g-repl] |
| OpenAI | Custom voices are for eligible customers, and an organization can hold 20. The speaker reads a given consent phrase. A change of wording fails the check. The phrases exist in 16 languages [vd-oai-voices] |
| Microsoft | Custom neural voice is a Limited Access feature by registration, and only for customers managed by Microsoft. The customer must hold written permission from the voice performer. The performer records a statement, and Microsoft reserves the right to check it against the training audio with speaker recognition. The customer must disclose the synthetic nature of the voice and give users a feedback channel [vd-ms-limited] |
| ElevenLabs | Both clone types use voice-captcha verification. The page says verification cannot prove that a recording belongs to the requester. The responsibility for authorised use stays with the creator. The safety page names a block on cloning celebrity and other high-risk voices [vd-el-clone, vd-el-safety] |
| Fish Audio | The docs say to clone one's own voice or a voice with written permission, and not to clone public-figure voices or voices from the internet without permission [vd-fish-clone] |
| Cartesia | The pages read state no consent rule for a cloned voice. The disclosure page asks developers to tell users before any interaction that they talk to an AI and that the conversation may be recorded and shared [vd-cart-disc] |
| xAI | The custom voice page read states no consent check. It limits the feature to the United States except Illinois, and the API to Enterprise teams. Each team can hold 30 voices [vd-xai-voices] |
| Mistral | The page read states no consent or legal requirement [vd-mistral] |

L. In the United States, an FCC ruling (adopted 2024-02-02, released 2024-02-08) says that the TCPA rules on an artificial voice cover
current AI technologies that generate human voices. Calls that use them need the prior express consent
of the called party, unless an emergency or an exemption applies [vd-fcc]. S.

## 4. Emotion range and its limits (MONITOR)

- **A named list or no list.** Cartesia names six primary emotions, the ones with the most data (`neutral`,
  `calm`, `angry`, `content`, `sad` and `scared`), and a full list of 58. Its emotion control covers English only. MiniMax offers `happy`, `sad`, `angry`,
  `fearful`, `disgusted`, `surprised` and `calm`, and two more values for its 2.6 models. Microsoft lists 62
  styles for HD voices and 61 for HD Omni voices. The page says styles work on English content, and paralinguistic tags work
  in all languages. Fish Audio and Inworld take free text, so no list bounds them
  [vd-cart-vse, vd-mm-t2a, vd-ms-ssml, vd-fish-emo, vd-inw-steer]. L.
- **The words come first.** Microsoft says its styles adapt to the meaning of the text. Cartesia says its
  default is to read the emotional subtext of the transcript. Hume says the model infers delivery from the
  text when no instruction exists. Hume's launch post for Octave 2 says the model infers when to whisper
  or shout from the script [vd-ms-ssml, vd-cart-latest, vd-hume-act, vd-hume-o2]. L.
- **Mid-line changes are weak.** Cartesia calls emotion shifts inside one generation highly
  experimental, and advises a separate generation for each emotion. Google advises a new turn with its
  own style. ElevenLabs advises one emotion per segment [vd-cart-ssml, vd-g-tts, vd-el-blog-emo]. L.
- **Voices limit the range.** ElevenLabs says experimental tags vary across voices. Cartesia says only
  voices tagged emotive carry emotion reliably [vd-el-bp, vd-cart-ssml]. L.
- **Results vary by use.** The Hume leaderboard reports that one model scored 82 percent on motivational
  voices and 6 percent on meditation voices. It reports large differences by language and accent. Its top
  tone-instruction score was 90.2 percent for Google's Gemini 3.1 Flash [vd-hume-lb]. M (vendor-run).
- **Instruction-following benchmarks find room to grow.** MINT-Bench (April 2026, revised August 2026)
  says compositional and paralinguistic controls are significant barriers across ten languages. It reports
  that commercial systems lead overall and that open models are competitive in some languages, such as
  Chinese. InstructTTSEval (June 2025) says its tests of accessible systems show much room to improve
  [vd-mint, vd-instructtts]. M.

## 5. Keeping a character consistent across lines and in long-form (MONITOR)

- **Save the voice, keep the style short.** Google says to design a persona once and to reuse the saved
  voice id. For turn-by-turn dialogue it advises one request per turn, with an empty or constant short
  style. It advises against instructions that ask the model to hold the voice steady, since extra text
  increases drift [vd-g-tts]. L.
- **Chain the requests.** ElevenLabs request stitching passes the ids of earlier requests so that prosody
  continues across chunks. It does not work with `eleven_v3`, an id must be under two hours old, and a
  streamed response must be read to the end before its id can be used [vd-el-stitch]. The Text to
  Dialogue endpoints take `previous_text`, `future_text` and request ids [vd-el-changelog-v4]. Hume says
  its continuation feature keeps emotional consistency across paragraphs by using earlier utterances as
  context [vd-hume-ov]. L.
- **Chunk size.** ElevenLabs lists 5,000 characters per request for v3 and 10,000 for v4 and Multilingual
  v2. MiniMax limits one request to 10,000 characters and advises streaming above 3,000. Fish Audio's
  chunk length runs from 100 to 300 characters with a default of 200. xAI allows 60,000 characters in one
  request [vd-el-models, vd-mm-t2a, vd-fish-tts, vd-xai-tts]. L.
- **Seeds and regeneration.** ElevenLabs says output is not deterministic. A `seed` gives a best effort,
  and regeneration fixes about half of the quality faults [vd-el-ttd]. L.
- **Reference audio sets pace and tone.** ElevenLabs says the pace of a voice depends on the audio that
  made it. Fish Audio asks for a reference with a steady tone and volume, and pauses of about half a
  second [vd-el-bp, vd-fish-clone]. L.
- **Tags that persist.** Inworld says its instruction tags last until a reset. It says applying an
  instruction to every sentence reduces continuity, and mixing the request-level field with inline tags
  needs care [vd-inw-steer]. L.
- **Measured.** Hume's Real-World VoiceEQ results list long-form stability as a separate dimension
  [vd-hume-eq]. The RW-Voice-EQ paper, by Hume's researchers, says naturalness, expressiveness, identity stability and reliability
  act independently in speech synthesis, so a high score on one says little about the others
  [vd-hume-eqp]. The audit of three open models found
  that a change aimed at one attribute often moved others [vd-attr-audit]. M.

## 6. Multi-speaker dialogue (MONITOR)

- **ElevenLabs.** Text to Dialogue takes a list of turns, each with text and a voice id. The page says
  the number of speakers is not limited. It advises at most 2,000 characters in total per request for
  reliable results, and says longer scripts need splitting and joining. It works with v4 (90+
  languages) and v3 (70+). An interruption is written with a dash and a tag such as `[jumping in]`,
  ellipses mark a trailing line, and the output is not deterministic [vd-el-ttd]. L.
- **Google.** One request takes at most 2 speakers, with prebuilt voices and a `speaker` label on each
  turn. Custom voices need one request per turn, and the page says to request raw PCM or strip the WAV
  header before joining files. Listener reactions go between pipe characters inside a turn, for example
  `|oh hmm|`, and the page says overlapping speech works best on `gemini-3.8-flash-tts` [vd-g-tts]. L.
- **Microsoft.** Multi-talker HD voices take an `mstts:dialog` element with one `mstts:turn` for each
  speaker. Microsoft says single-talker models synthesise each turn alone, and that the multi-talker
  voices keep context across turns [vd-ms-ssml]. L.
- **Xiaomi.** MiMo-V2.5-TTS takes a screenplay-style input with separate layers for character, scene and
  direction [vd-mimo]. L.
- **What the pages leave open.** None of the pages reports a measured rate for speaker mix-ups or for
  overlap errors. A reader who needs them has to run a test on their own scripts.

## 7. Non-verbal sounds: laughs, sighs and breaths (MONITOR)

| Maker | Sounds the page lists |
| --- | --- |
| ElevenLabs | Tags such as `[laughs]`, `[sighs]`, `[exhales]`, `[clears throat]`, `[gulps]`, plus sound effects [vd-el-bp] |
| Google | 35 entries (40 spellings), including `<breath>`, `<cough>`, `<gasp>`, `<laugh>`, `<sigh>`, `<yawn>`, `<short pause>` and `<long pause>` [vd-g-tts] |
| Inworld | 50 recognised sounds. The page names `[laugh]`, `[breathe]`, `[clear throat]`, `[sigh]`, `[cough]` and `[yawn]` as the most reliable. The fast model still honours these tags [vd-inw-steer] |
| MiniMax | 19 tags, for example `(laughs)`, `(sighs)`, `(breath)`, `(gasps)`. Only `speech-2.8-hd` and `speech-2.8-turbo` [vd-mm-t2a] |
| xAI | `[pause]`, `[long-pause]`, `[laugh]`, `[giggle]`, `[chuckle]`, `[cry]`, `[tsk]`, `[tongue-click]`, `[lip-smack]`, `[hum-tune]`, `[breath]`, `[inhale]`, `[exhale]`, `[sigh]` [vd-xai-tts] |
| Microsoft HD | Laughter, coughing, throat clearing, breathing, sighing and yawning [vd-ms-ssml] |
| Fish Audio | 11 sound effects, such as laughing, sobbing, sighing and throat clearing [vd-fish-emo] |
| Cartesia | `[laughter]` [vd-cart-vse] |
| Boson AI Higgs TTS 3 | Nine sound effects, such as `cough`, `laughter`, `crying`, `sigh` and `sneeze`, written as `<\|sfx:...\|>` [vd-higgs] |
| Chatterbox Turbo | `[laugh]`, `[chuckle]`, `[cough]` "and more" [vd-chatterbox] |

L, as of 2026-10-04.

- **One at a time.** xAI advises a tag next to punctuation, for example `Really? [laugh]`, over stacked
  tags. Inworld says a non-verbal tag gives one sound and does not persist. Both place the tag where the
  sound would come in speech [vd-xai-tts, vd-inw-steer]. L.
- **Sparing use.** Fish Audio lists overuse of tags in short text as a failure [vd-fish-emo]. L.
  [voice-agents.md](voice-agents.md) reports a framework guide that caps non-verbal sounds at one per
  turn.
- **Wrong reading.** ElevenLabs says a tag can come out as a sound effect and not as delivery. Its tag
  guide covers v3 and v4, so the behaviour applies to those [vd-el-bp]. L.
- **Quality of the sound.** The independent benchmarks reviewed here score paralinguistics as a category.
  EmergentTTS-Eval has paralinguistics among six categories, and MINT-Bench names paralinguistic control as a
  weak area [vd-emergent, vd-mint]. M.

## 8. Pronunciation and text normalisation (MONITOR)

- **Normalisation is a setting that differs by model.** The ElevenLabs guide says normalisation is on for
  all models. The models page says Flash v2.5 does not normalise numbers by default, to keep latency low,
  and that Multilingual v2 does better with numbers. The two pages disagree in wording
  [vd-el-bp, vd-el-models]. xAI has a `text_normalization` setting that expands numbers, abbreviations
  and symbols, and says it does not affect IPA. MiniMax has a Chinese and English normalisation switch
  that costs a little latency. Fish Audio has a `normalize` setting [vd-xai-tts, vd-mm-t2a, vd-fish-tts]. L.
- **Write the spoken form.** ElevenLabs lists phone numbers, currency, dates, times, URLs and
  abbreviations as problem areas. It notes that `01/02/2023` can read as two different dates. It says to
  tell a language model to write numbers as words, or to use code such as an inflection library. Its agent
  guide gives two modes: a prompt rule, which is fast but sometimes fails and leaves written-out numbers in
  transcripts, and a normaliser after the model, which is more reliable and adds a small delay
  [vd-el-bp, vd-el-prompt]. Inworld advises numbers as words, dates spelled out and no markdown or
  emoji [vd-inw-prompt]. L.
- **Explicit phonemes.** ElevenLabs v4 takes IPA between forward slashes, with stress marks, and says
  results can differ by voice and phrase. SSML phoneme tags work only with `eleven_flash_v2`. Its pronunciation
  dictionaries take `.pls` files with phoneme or alias rules, and the phoneme rules work with `eleven_v4`,
  `eleven_flash_v2` and `eleven_v3` [vd-el-bp, vd-el-pron]. MiniMax takes a dictionary with IPA, pinyin
  and kana. Cartesia offers a `spell` tag for codes and names. Hume's Octave 2 launch post (2025-10-01) says
  phoneme editing is coming [vd-mm-t2a, vd-cart-ssml, vd-hume-o2]. W3C SSML defines `phoneme`, `sub` and lexicon
  elements [vd-w3c-ssml]. L, S.
- **Pauses.** ElevenLabs says many `<break>` tags in one generation can cause instability, and that dashes
  and ellipses are less consistent. MiniMax marks pauses as `<#x#>`, with a duration between 0.01 and
  99.99 seconds, and not twice in a row. Cartesia says a break splits the generation, so the speech can
  sound less natural. Hume uses `[pause]` inside text and `trailing_silence` after an utterance
  [vd-el-bp, vd-mm-t2a, vd-cart-ssml, vd-hume-act]. L.
- **Measured.** Artificial Analysis scores pronunciation robustness with human reviewers in four
  categories: contextual disambiguation, text normalisation, sequence fidelity and term pronunciation
  [vd-aa-method]. M.

## 9. Latency against expressiveness (MONITOR)

- **Separate models for separate jobs.** The ElevenLabs changelog points `eleven_v4` at content
  creation and longer audio, and `eleven_v4_turbo` at agents and interactive use. The models page lists
  v4 Turbo at a median inference latency of about 100 ms, v3 Conversational (the realtime version of v3)
  at about 280 ms, and Flash v2.5 at about 75 ms. It lists no latency for v4 or v3. Flash v2.5 does not
  normalise numbers by default [vd-el-models, vd-el-changelog-v4]. L.
- **Speed can remove the control.** Inworld says `inworld-tts-2-flash` ignores instruction tags, and the
  non-verbal tags still work. Its docs list 100 ms time to first byte for TTS-2 and 20 ms for the Flash
  model [vd-inw-steer, vd-inw-models]. Google offers Flash-Lite TTS for volume and cost. Its
  launch post names expressive voice agents as a use and says the model keeps fine control of tone and
  pacing. The pages read give no latency figure [vd-g-blog, vd-g-model]. L.
- **Streaming has its own cost.** xAI's lowest-latency setting shrinks the first chunk and carries what
  it calls a more noticeable quality tradeoff. Hume's instant mode, about 200 ms to the first audio, is
  off for voice design and for multiple candidates. Cartesia says a speed or volume tag read token by token
  needs buffering, or it is read aloud [vd-xai-tts, vd-hume-ov, vd-cart-ssml]. L.
- **Expressiveness in the live agent.** ElevenLabs' expressive mode pairs Eleven v3 Conversational,
  directed by tags and rules in the system prompt, with a turn-taking system that uses signals from its
  realtime transcription model, including emotional cues. It says a tag affects about the next
  4 to 5 words, and the mode does not keep the identity of a professional clone [vd-el-expr]. L.
- **What the maker figures cover.** The ElevenLabs figures are inference time and leave out the network
  [vd-el-models]. Hume's two pages differ: its launch post says under 200 ms for Octave 2, and its docs
  table says about 100 ms for Octave 2 and about 200 ms for Octave 1 [vd-hume-o2, vd-hume-ov]. Latency
  for a whole voice-agent turn is in [voice-agents.md](voice-agents.md). L.

## 10. Evaluating expressive speech (STABLE)

| Method | What it answers | Limit |
| --- | --- | --- |
| Listener scores (mean opinion score) | How natural a clip sounds | ITU-T P.800 (approved 1996-08-30) is the recommendation on subjective quality tests. Mean opinion score studies follow this family of methods (inferred; the page read gave only the title and date). A score does not say whether the delivery followed the direction [vd-itu-p800] |
| Preference arenas | Which of two clips listeners prefer | See below |
| Instruction-following benchmarks | Whether the speech matches a written direction | A judge model scores most of them |
| Intelligibility and pronunciation checks | Whether the right words were spoken | Say nothing about delivery |
| Attribute-preservation audits | Whether a change in one trait left the others alone | Few systems tested so far |

- **Arenas.** Artificial Analysis ranks models by blind pairwise votes with a Bradley-Terry fit. Its
  prompts come in four categories and include numeric sequences. The controlled arena uses eight recorded
  reference voices for all models, which removes voice preference from the score. The provider arena uses
  the native voices of each provider. Its pronunciation reviewers are a paid panel that is screened for
  native English, and a reviewer who misses attention checks is excluded [vd-aa-method]. M.
- **Instruction-following benchmarks.** InstructTTSEval has 6,000 cases in English and Chinese across three
  tasks (acoustic parameters, descriptive style, role play) and uses Gemini as the judge. EmergentTTS-Eval
  has 1,645 cases in six categories (emotions, paralinguistics, foreign words, syntactic complexity,
  complex pronunciation, questions) and uses an audio language model as the judge. The authors report a
  high correlation with human preference. MINT-Bench covers ten languages with a hierarchical hybrid
  protocol that scores content, instruction adherence and perceptual quality [vd-instructtts, vd-emergent,
  vd-mint]. M.
- **How far a model judge can go.** A 2025 study of audio language models as judges of speaking style
  reports that the agreement between Gemini and human judges is comparable to the agreement between two
  humans. The same study finds that the speech models it tested still lack precise style control
  [vd-allm-judge]. M. The limits in [llm-as-judge.md](llm-as-judge.md) apply.
- **Word error rate.** The Artificial Analysis methodology page names no word error rate measure for
  text-to-speech. It uses human review of pronunciation. A maker that reports word error rate gives it as a separate figure: the
  Qwen3-TTS model card lists 0.77 for Chinese and 1.24 for English on the Seed-TTS test set, for its 1.7B
  Base model. A word error
  rate from a speech recognition model flags dropped or invented words. It does not score tone (inferred)
  [vd-aa-method, vd-qwen-hf]. M, L.
- **Controllability leaderboards from a vendor.** Hume publishes a controllability leaderboard with four
  dimensions (voice design, voice instruction, inline tags and role fit) and a Real-World VoiceEQ
  benchmark. Raters are blind to the model, and the test set is held out. Hume sells a competing model, and the
  VoiceEQ post says Hume has a non-exclusive licensing agreement with Google.
  Its page says unreleased Hume systems are hidden, and the matches against them still count
  [vd-hume-lb, vd-hume-eq]. M (vendor-run).
- **Attribute preservation.** An audit of three open models (August 2026) measured whether a prompt that
  changes one trait leaves the others stable. It reports a single-sample success rate of 4.8 percent, and
  about 14 percent with a three-candidate pool and a selection policy [vd-attr-audit]. M.
- **Maker preference claims.** ElevenLabs reports that about 75 percent of listeners preferred v4 in blind
  head-to-head tests. The test asked which clip was more expressive and which sounded more natural, with
  ties as half. The comparison set was Cartesia Sonic 3.6, Inworld TTS-2 and Google models, in September
  2026. No raw data was seen [vd-el-blog-turbo]. L.
- **Standings differ by benchmark.** In a vendor-run benchmark of 2026-09-24, Google's Gemini 3.8 Flash TTS ranks
  first with an expressivity-and-reliability score of 0.920 and the Flash-Lite model second at 0.914. In
  the same benchmark, ElevenLabs v3 scored higher than Gemini Flash on young-adult voice accuracy (68.1
  against 34.0 percent) and Inworld scored higher on a volume-control pass rate (88.9 against 56.9
  percent). A ranking on one benchmark does not carry to another. The post discloses a non-exclusive licensing
  agreement between Hume and Google [vd-hume-eq]. M (vendor-run).

## 11. Disclosure, watermarking and misuse safeguards (MONITOR)

| Maker | Safeguard on the page read |
| --- | --- |
| Google | A SynthID watermark in every clip from its audio models. C2PA credentials. Consent verification for voice replication [vd-g-blog, vd-g-repl] |
| ElevenLabs | An inaudible watermark in its output, and a detector that falls back to a classifier. The page says the detector sees only ElevenLabs watermarks, that third-party models on the platform are generally not marked, and that modified files can be missed. Support for C2PA. Blocks on celebrity and high-risk voices. Monitoring with classifiers and reviewers under a prohibited-use policy. Bans for serious or repeated violations [vd-el-detector, vd-el-safety] |
| Resemble (Chatterbox Turbo, MIT licence) | A Perth watermark in every generated file. The model card says it survives MP3 compression and common edits [vd-chatterbox] |
| OpenAI | Its usage policies require clear disclosure to end users that the voice is AI-generated. Custom voices are limited to eligible customers [vd-oai-tts, vd-oai-voices] |
| Microsoft | Limited Access registration, a written-permission warranty, a recorded performer statement checked against training audio, and a duty to disclose the synthetic nature of the voice [vd-ms-limited] |
| Cartesia | Developers must tell users that they talk to an AI, and that calls may be recorded and shared, before the interaction [vd-cart-disc] |

L.

- **The two ElevenLabs numbers.** The detector page gives 99 percent precision and 80 percent recall for
  its older AI speech classifier on unmodified ElevenLabs audio. It gives no figure for the watermark check
  [vd-el-detector]. L.
- **Gaps.** The statement on SynthID was found on the Google launch post and not on the three Google
  documentation pages [vd-g-tts, vd-g-design, vd-g-repl, vd-g-blog]. The xAI, Mistral and MiniMax pages
  read give no watermark statement [vd-xai-tts, vd-mistral, vd-mm-t2a]. L.
- **European Union.** Article 50 of the AI Act says that people must be told when they interact with an AI
  system, unless this is obvious. It says providers of systems that generate synthetic audio must mark the
  output in a machine-readable form that is detectable, where this is technically feasible. It applies from
  2026-08-02. Deployers of deepfakes must disclose them, with limited duties for artistic work
  [vd-euai]. S.
- **United States.** See the FCC ruling in section 3 [vd-fcc]. S.
- **Laws on voice likeness** and rules on recording consent differ by place and are not covered here. No
  primary source on them was read.

## What the evidence supports (inference)

1. The four ways to direct delivery do not replace each other. Free text sets the scene, tags place
   events, and a saved voice or clip sets identity. This follows from the tables in sections 1 to 3.
2. A script written for one model cannot move to another by search and replace. The syntax, the scope of a
   tag and the language of the direction all differ (sections 1 and 2).
3. The makers' own pages give guidance and no measured strength of effect. The measured figures that exist
   are low for combined or fine control (section 4), and most come from a vendor that sells a rival model.
4. Low latency models cost control. Inworld and xAI say so on their pages, and ElevenLabs sells separate
   models (section 9).
5. Consent checks differ in strength between makers. ElevenLabs says its check cannot prove that a
   recording belongs to the requester (section 3).
6. A preference score, an instruction-following score and a word error rate answer three questions. A
   report on one does not stand in for the others (section 10).

## Limits and open questions

- Maker pages change often. Tag lists, ids and limits come from pages read on 2026-10-04. The first
  reading used a tool that summarises pages. A second check on the same day re-read most pages as raw
  Markdown or text. The text names the gaps that it found.
- ElevenLabs pages disagree on number normalisation for some models (section 8). The Cartesia docs
  describe emotion control as beta, as experimental and, for Sonic 3.6, as not needing markup. One
  Cartesia documentation URL redirected to a login page on 2026-10-04, so the Markdown versions of the
  pages were read.
- The Hume overview page says its text-to-speech and conversation APIs end on 2026-11-13. Octave 2 is a
  preview, and the `description` field works only on Octave 1. The Hume maker page,
  [the Hume folder](../models/hume/README.md), tracks the end date [vd-hume-ov].
- OpenAI lists its text-to-speech models, including `gpt-4o-mini-tts`, for removal on 2027-01-06 and
  names `gpt-realtime-2.1-mini` as the replacement. The OpenAI guide on custom voices was read, and its
  limits may change [vd-oai-dep, vd-oai-voices].
- No source read gives a tag-by-tag reliability rate for any model.
- The FCC ruling is a US rule on calls. The page covers no other law on voice likeness.
- Doubao and Seed-TTS from ByteDance, Sesame, Kyutai's speech synthesis model and the OpenAI
  prompting cookbook for voices were not read as primary sources. Secondary pages say Doubao's Seed-TTS 2.0
  takes natural-language directives.
- Vendor-run benchmarks (Hume) and maker preference claims (ElevenLabs) are class L or M with a stated
  conflict of interest. An independent re-run would settle the order of the models.

## Sources

Read 2026-10-04. Ids in brackets are used in the text above.

ElevenLabs

- [vd-el-bp] ElevenLabs, text to speech best practices
  <https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices>.
- [vd-el-models] ElevenLabs, models <https://elevenlabs.io/docs/overview/models>.
- [vd-el-v4] ElevenLabs, Eleven v4 page
  <https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4>.
- [vd-el-changelog-v4] ElevenLabs, changelog 2026-09-28 <https://elevenlabs.io/docs/changelog/2026/9/28>.
- [vd-el-blog-emo] ElevenLabs, emotional text to speech with Eleven v4, 2026-09-28
  <https://elevenlabs.io/blog/emotional-text-to-speech-with-eleven-v4>.
- [vd-el-blog-turbo] ElevenLabs, Eleven v4 Turbo in ElevenAgents, 2026-09-28, updated 2026-10-01
  <https://elevenlabs.io/blog/eleven-v4-turbo-in-elevenagents>.
- [vd-el-ttd] ElevenLabs, Text to Dialogue
  <https://elevenlabs.io/docs/overview/capabilities/text-to-dialogue>.
- [vd-el-clone] ElevenLabs, voice cloning <https://elevenlabs.io/docs/eleven-api/concepts/voice-cloning>.
- [vd-el-design] ElevenLabs, Voice Design <https://elevenlabs.io/docs/eleven-creative/voices/voice-design>.
- [vd-el-expr] ElevenLabs, expressive mode
  <https://elevenlabs.io/docs/eleven-agents/customization/voice/expressive-mode>.
- [vd-el-stitch] ElevenLabs, request stitching
  <https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/request-stitching>.
- [vd-el-pron] ElevenLabs, pronunciation dictionaries for agents
  <https://elevenlabs.io/docs/eleven-agents/customization/voice/pronunciation-dictionary>.
- [vd-el-prompt] ElevenLabs, agent prompting guide
  <https://elevenlabs.io/docs/eleven-agents/best-practices/prompting-guide>.
- [vd-el-safety] ElevenLabs, safety <https://elevenlabs.io/safety>.
- [vd-el-detector] ElevenLabs, audio detector
  <https://elevenlabs.io/docs/eleven-creative/audio-tools/audio-detector>.

Google

- [vd-g-tts] Google, text-to-speech generation in the Gemini API, updated 2026-10-01
  <https://ai.google.dev/gemini-api/docs/speech-generation>.
- [vd-g-design] Google, voice design <https://ai.google.dev/gemini-api/docs/voice-design>.
- [vd-g-repl] Google, voice replication <https://ai.google.dev/gemini-api/docs/voice-replication>.
- [vd-g-model] Google, Gemini 3.8 Flash TTS model page
  <https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash-tts>.
- [vd-g-31] Google, Gemini 3.1 Flash TTS model page
  <https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview>.
- [vd-g-blog] Google, Gemini 3.8 Flash TTS and Flash-Lite TTS, 2026-09-23
  <https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/>.

OpenAI

- [vd-oai-tts] OpenAI, text to speech <https://developers.openai.com/api/docs/guides/text-to-speech>.
- [vd-oai-voices] OpenAI, custom voices <https://developers.openai.com/api/docs/guides/custom-voices>.
- [vd-oai-dep] OpenAI, deprecations <https://developers.openai.com/api/docs/deprecations>.

Other makers

- [vd-hume-act] Hume, acting instructions
  <https://dev.hume.ai/docs/text-to-speech-tts/acting-instructions>.
- [vd-hume-ov] Hume, text-to-speech overview <https://dev.hume.ai/docs/text-to-speech-tts/overview>.
- [vd-hume-o2] Hume, Octave 2 launch, 2025-10-01 <https://hume.ai/blog/octave-2-launch>.
- [vd-inw-steer] Inworld, steering <https://docs.inworld.ai/tts/capabilities/steering>.
- [vd-inw-prompt] Inworld, prompting for TTS 2
  <https://docs.inworld.ai/tts/best-practices/prompting-for-tts-2>.
- [vd-inw-models] Inworld, TTS models <https://docs.inworld.ai/tts/tts-models>.
- [vd-cart-vse] Cartesia, volume, speed and emotion
  <https://docs.cartesia.ai/build-with-cartesia/capability-guides/volume-speed-emotion.md>.
- [vd-cart-ssml] Cartesia, SSML tags
  <https://docs.cartesia.ai/build-with-cartesia/capability-guides/ssml-tags.md>.
- [vd-cart-latest] Cartesia, Sonic 3.6 <https://docs.cartesia.ai/build-with-cartesia/tts-models/latest>.
- [vd-cart-disc] Cartesia, disclosure requirements
  <https://www.cartesia.ai/legal/disclosure-requirements>.
- [vd-mm-t2a] MiniMax, speech T2A HTTP API reference
  <https://platform.minimax.io/docs/api-reference/speech-t2a-http>.
- [vd-fish-emo] Fish Audio, emotion control
  <https://docs.fish.audio/developer-guide/core-features/emotions>.
- [vd-fish-tts] Fish Audio, text to speech best practices
  <https://docs.fish.audio/resources/best-practices/text-to-speech>.
- [vd-fish-clone] Fish Audio, voice cloning best practices
  <https://docs.fish.audio/resources/best-practices/voice-cloning>.
- [vd-xai-tts] xAI, text to speech
  <https://docs.x.ai/developers/model-capabilities/audio/text-to-speech>.
- [vd-xai-voices] xAI, custom voices
  <https://docs.x.ai/developers/model-capabilities/audio/custom-voices>.
- [vd-ms-ssml] Microsoft, voice and sound with SSML, updated 2026-08-18
  <https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice>.
- [vd-ms-limited] Microsoft, Limited Access for custom neural voice, updated 2026-08-26
  <https://learn.microsoft.com/en-us/legal/cognitive-services/speech-service/custom-neural-voice/limited-access-custom-neural-voice>.
- [vd-mimo] Xiaomi, MiMo-V2.5-TTS series <https://mimo.xiaomi.com/mimo-v2-5-tts>.
- [vd-qwen-hf] Alibaba Qwen, Qwen3-TTS-12Hz-1.7B-VoiceDesign model card
  <https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign>.
- [vd-qwen-ali] Alibaba Cloud, Qwen3-TTS-Instruct-Flash, updated 2026-09-28
  <https://www.alibabacloud.com/help/en/model-studio/qwen3-tts-instruct-flash>.
- [vd-mistral] Mistral, text to speech <https://docs.mistral.ai/capabilities/audio/text_to_speech>.
- [vd-chatterbox] Resemble AI, Chatterbox-Turbo model card <https://huggingface.co/ResembleAI/chatterbox-turbo>.
- [vd-higgs] Boson AI, Higgs TTS 3 model card <https://huggingface.co/bosonai/higgs-tts-3-4b>.
- [vd-polly] Amazon Web Services, Amazon Polly supported SSML tags
  <https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html>.

Standards, laws and measurers

- [vd-w3c-ssml] W3C, Speech Synthesis Markup Language 1.1, Recommendation of 2010-09-07
  <https://www.w3.org/TR/speech-synthesis11/>.
- [vd-itu-p800] ITU-T, recommendation P.800, approved 1996-08-30 (title and date read only)
  <https://www.itu.int/rec/T-REC-P.800-199608-I>.
- [vd-fcc] FCC, declaratory ruling FCC 24-17, adopted 2024-02-02, released 2024-02-08
  <https://docs.fcc.gov/public/attachments/FCC-24-17A1.pdf>.
- [vd-euai] EU AI Act, Article 50 <https://artificialintelligenceact.eu/article/50/>.
- [vd-aa-method] Artificial Analysis, text to speech benchmarking methodology
  <https://artificialanalysis.ai/methodology/text-to-speech>.
- [vd-emergent] EmergentTTS-Eval, arXiv 2505.23009, 2025-05-29 <https://arxiv.org/abs/2505.23009>.
- [vd-instructtts] InstructTTSEval, arXiv 2506.16381, 2025-06-19 <https://arxiv.org/abs/2506.16381>.
- [vd-mint] MINT-Bench, arXiv 2604.17958, 2026-04-20, revised 2026-08-20
  <https://arxiv.org/abs/2604.17958>.
- [vd-allm-judge] Audio-aware large language models as judges for speaking styles, arXiv 2506.05984,
  2025-06-06 <https://arxiv.org/abs/2506.05984>.
- [vd-attr-audit] Beyond prompt adherence, arXiv 2608.00545, 2026-08-01 <https://arxiv.org/abs/2608.00545>.
- [vd-hume-lb] Hume, voice controllability leaderboard, 2026-09-17
  <https://www.hume.ai/blog/introducing-the-hume-voice-controllability-leaderboard>.
- [vd-hume-eq] Hume, Real-World VoiceEQ results for Gemini 3.8 Flash TTS, 2026-09-24
  <https://www.hume.ai/blog/newly-released-google-s-gemini-3-8-flash-tts-tops-hume-s-real-world-voiceeq-leaderboard>.
- [vd-hume-eqp] RW-Voice-EQ Bench, arXiv 2607.14846, 2026-07-16 <https://arxiv.org/abs/2607.14846>.
