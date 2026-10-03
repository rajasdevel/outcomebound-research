---
last_checked: 2026-10-03
volatility: MONITOR (lineage, guides and API behaviour change at each release)
sources:
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-system-prompts.html
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-sonic.html
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-sonic.html
  - https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonBedrock/current/index.json
  - https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-nova-sonic-speech-to-speech-conversations-bedrock/
  - https://docs.aws.amazon.com/ai/responsible-ai/nova-sonic/overview.html
  - https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-nova-2-sonic-real-time-conversational-ai
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/release-notes.html
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-chat-history.html
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-getting-started.html
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-integrations.html
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-input-events.html
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-output-events.html
  - https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html
  - https://docs.aws.amazon.com/ai/responsible-ai/nova-2-sonic/overview.html
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-cross-modal.html
  - https://aws.amazon.com/nova/pricing/
  - https://docs.aws.amazon.com/nova/latest/userguide/prompting-speech.html
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-tool-configuration.html
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-async-tools.html
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-barge-in.html
  - https://github.com/livekit/agents/issues/4887
  - https://repost.aws/questions/QUhD4OjsK5TWaZCmhkV44Glg/nova-sonic-inconsistent-tool-calling
  - https://artificialanalysis.ai/speech-to-speech
  - https://aws.amazon.com/blogs/machine-learning/how-loka-built-a-natural-low-latency-voice-agent-with-amazon-nova-2-sonic/
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-turn-taking.html
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-language-support.html
  - https://docs.aws.amazon.com/nova/latest/userguide/speech.html
  - https://docs.aws.amazon.com/nova/latest/userguide/available-voices.html
  - https://docs.aws.amazon.com/nova/latest/userguide/input-events.html
  - https://docs.aws.amazon.com/nova/latest/userguide/output-events.html
  - https://docs.aws.amazon.com/nova/latest/userguide/speech-errors.html
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html
  - https://docs.aws.amazon.com/nova/latest/nova2-userguide/doc-history.html
---

# Amazon

Amazon makes the Nova line of foundation models and sells them through Amazon Bedrock. This library holds the voice models of the line: Nova Sonic, the speech-to-speech models. This page holds what is true across them. It covers the lineage, the Bedrock bidirectional streaming API, what Amazon's prompting guides say, how Amazon reports safety, and behaviour that shows up across the generations. Each model file says only what differs for that model and links back here: [Nova 2 Sonic](nova-2-sonic.md) and [Nova Sonic](nova-sonic.md).

Evidence classes in this folder: L is Amazon's own documentation or announcement, M is an independent measurement, A is one practitioner's or one outlet's account. A tag such as [L: nova2-sonic-prompts] names the class and the source id. The ids are listed in the Sources section of this file. Facts are as of 2026-10-03 unless a date is given.

## Models and lineage

### Classes in this library

The library keeps two generations of each class: the current one and the one before it. Amazon calls the two models Amazon Nova Sonic and Amazon Nova 2 Sonic, and the cards record them as generations 1 and 2 of the class Nova Sonic.

| Class | Current generation | Previous generation | Status on 2026-10-03 |
| --- | --- | --- | --- |
| Nova Sonic | [Nova 2 Sonic](nova-2-sonic.md), generally available 2025-12-02 | [Nova Sonic](nova-sonic.md), released 2025-04-08 | Nova 2 Sonic is Active. The Bedrock card says end of life no sooner than 2026-12-02, with a legacy period of at least 6 months. Nova Sonic has been Legacy since 2026-03-13, and its end-of-life date of 2026-09-14 has passed, but AWS pages still list it [L: bedrock-card-nova-2-sonic, bedrock-lifecycle-legacy, bedrock-card-nova-sonic] |

Models that exist and have no file here: the other models of the Nova line, which are language, image, video and embedding models. The AWS price list names Nova 2.0 Lite, Nova 2.0 Pro, Nova 2.0 Omni, Nova Micro, Nova Lite, Nova Pro, Nova Premier, Nova Canvas, Nova Reel and Nova Multimodal Embeddings. Nova Premier, Nova Canvas and Nova Reel are in the Legacy table of Bedrock [L: aws-price-list, bedrock-lifecycle-legacy].

### Release timeline

| Date | Event | Change that affects how a voice application is built |
| --- | --- | --- |
| 2025-04-08 | Nova Sonic announced | Available in US East (N. Virginia) only. A new bidirectional streaming API in Bedrock launched with it [L: nova1-whats-new] |
| 2025-07-16 | Service card for Nova Sonic current | The card lists five languages and eleven voices [L: nova1-service-card] |
| 2025-12-02 | Nova 2 Sonic generally available | Adds Portuguese and Hindi, polyglot voices, a setting for turn-taking sensitivity, text input in a voice session, asynchronous tool calls and a context window of one million tokens [L: nova2-whats-new] |
| 2026-03 | Nova 2 Sonic refresh | Voices compatible with Amazon Polly, a cut of 150 ms in the 50th-percentile latency that users perceive, and better turn-taking on 8 kHz telephone speech [L: nova2-release-notes] |
| 2026-03-13 | Nova Sonic enters Legacy | End-of-life date 2026-09-14 [L: bedrock-lifecycle-legacy] |
| 2026-05-21 to 2026-05-28 | Second Nova 2 Sonic refresh | In-place update with no API change. AWS reports an 88 percent cut in speech generation hallucinations, 52 percent in speaker drift and 28 percent in critical errors, each on an internal data set [L: nova2-release-notes] |
| 2026-06-22 | Nova 2 Sonic guide updated | Chat history limits raised to 50 KB for a message and 200 KB in total [L: nova2-doc-history, nova2-sonic-chat-history] |

Both refreshes changed the model behind the same id. The id amazon.nova-2-sonic-v1:0 names the model before and after each refresh [L: nova2-release-notes].

## API surface

### The Bedrock bidirectional streaming API

Both models use one operation, InvokeModelWithBidirectionalStream, on the bedrock-runtime endpoint. Model ids are amazon.nova-sonic-v1:0 and amazon.nova-2-sonic-v1:0. The Bedrock cards list a model id only for bedrock-runtime, and list geo and global inference ids as not supported [L: bedrock-card-nova-2-sonic, bedrock-card-nova-sonic]. The inference page of the Nova 2 guide lists us. and global. ids for Nova 2 Sonic. The two pages disagree [L: nova2-core-inference].

- Authentication: the guide's sample signs requests with SigV4 and credentials from the environment. The Bedrock card's sample steps use a long-term Bedrock API key in AWS_BEARER_TOKEN_BEDROCK. AgentCore uses IAM and SigV4 [L: nova2-sonic-getting-started, bedrock-card-nova-2-sonic, nova2-sonic-integrations].
- SDK: the guide's Python sample uses the aws_sdk_bedrock_runtime package with a BedrockRuntimeClient. The sample steps on the Bedrock card name boto3 instead [L: nova2-sonic-getting-started, bedrock-card-nova-2-sonic].
- Event model: the client sends JSON events in this order: sessionStart (inference settings and, for Nova 2, turn detection), promptStart (output formats, voice, tools), contentStart, content and contentEnd for each of the system prompt, optional chat history and audio, then promptEnd and sessionEnd. Each prompt has a promptName and each content block a contentName. Content roles are SYSTEM, USER, ASSISTANT, TOOL and, for Nova 2, SYSTEM_SPEECH. Skipping the closing events can leave orphaned resources [L: nova2-sonic-input-events, nova2-sonic-getting-started].
- Output: the model sends completionStart, then in order a transcript of the user (ASR), optional toolUse, a speculative transcript of the planned answer, audio chunks, a final transcript of what was said, usage events and completionEnd [L: nova2-sonic-output-events].
- Audio: linear PCM, 16-bit, mono, base64. Sample rate 8,000, 16,000 or 24,000 Hz. Frames of about 32 ms [L: nova2-sonic-input-events].
- Connection: at most 8 minutes. The client renews it and sends saved chat history to continue. Chat history goes in once, after the system prompt and before audio, up to 200 KB in total and 50 KB for one text input [L: nova2-sonic-getting-started, nova2-sonic-chat-history].
- Concurrency: 20 sessions per AWS account in each Region for Nova 2 Sonic, and AWS says the quota cannot be raised. Nova Sonic allowed 20 concurrent connections for each customer [L: bedrock-card-nova-2-sonic, nova1-model-specs].
- Regions: Nova 2 Sonic in us-east-1, us-west-2, eu-north-1 and ap-northeast-1, and through Amazon Connect also in four more Regions. Nova Sonic in us-east-1, eu-north-1 and ap-northeast-1 [L: nova2-release-notes, bedrock-card-nova-sonic].

### Bedrock features

The Bedrock card for Nova 2 Sonic lists response streaming as supported. It lists intelligent prompt routing, abuse detection, Guardrails, prompt optimisation, count tokens, knowledge bases, model evaluation, prompt management, flows and agents as not supported [L: bedrock-card-nova-2-sonic]. The service card says Bedrock applies automated abuse detection, and says AWS offers Guardrails as a tool. It also says the safety filters of the model cannot be set or turned off [L: nova2-service-card]. The two pages are not in line.

### Integrations

The Nova 2 guide describes Strands Agents (a BidiAgent class), Amazon Bedrock AgentCore, LiveKit, Pipecat, and telephony through Twilio, Vonage and other SIP providers [L: nova2-sonic-integrations]. The announcement of 2025-12-02 names Amazon Connect, Vonage, Twilio, AudioCodes, LiveKit and Pipecat [L: nova2-whats-new]. The cross-modal page says Nova Sonic does not process DTMF tones, so a system must turn them into text first [L: nova2-sonic-cross-modal].

### Price structure

Amazon Bedrock bills speech tokens and text tokens at different rates. Speech tokens cover the audio in and out. AWS says text tokens apply to transcription, tool calls, grounding and chat history. Rates differ by Region. The card of each model gives the figures from the AWS price list [L: aws-price-list, nova-pricing-page].

## Prompting guides

The guides are one page for each generation. The Nova 2 page is "Voice conversation prompts" [L: nova2-sonic-prompts]. The Nova guide has a section "Amazon Nova Sonic prompting best practices" [L: nova1-prompting].

How the advice moved from generation 1 to 2:

- Both guides say the system prompt steers wording and style, and that it cannot change speech attributes such as accent and pitch. Nova Sonic v1 says the model picks those from the conversation. The service card of Nova 2 Sonic says developers cannot change pitch, tenor, accent or speaking rate [L: nova1-prompting, nova2-service-card].
- The v1 guide says to optimise for listening. Its advice: short replies, ellipses for pauses, spoken emphasis instead of bold type, spoken signposts such as "first" and "finally", shorter chains of thought, and confirmation before a tool acts. It says to avoid bullet lists, tables, code blocks, accents, sound effects and content that depends on being seen [L: nova1-prompting].
- The Nova 2 guide gives a baseline prompt: warm, professional, natural, direct and human, with 1 to 2 sentences first and 3 to 5 short sentences in total. It gives a longer version for detailed answers. It gives a language-mirroring rule and a rule that gender-specific languages (Hindi, Portuguese, French, Italian, Spanish, Russian and Polish) need the gender of the assistant in the prompt, to match the voice [L: nova2-sonic-prompts].
- Phrase lists: the Nova 2 guide says Nova 2 Sonic is more sensitive to phrase suggestions than v1. A list of filler or emphasis phrases leads the model to use them very often. AWS recommends one or two examples of the tone you want, and no explicit phrase lists, when you want natural variation [L: nova2-sonic-prompts].
- Speech prompts are new in Nova 2. They are fixed texts that control the script of Hindi transcription (Latin, Devanagari or mixed). They go in a SYSTEM_SPEECH block after the system prompt and must not be edited [L: nova2-sonic-prompts, nova2-sonic-input-events].
- Reasoning aloud: both guides give a prompt that sets rules for step-by-step explanation, and a short answer for simple questions [L: nova1-prompting, nova2-sonic-prompts].

## System-card practice

AWS publishes an AI service card for each model. The card for Nova Sonic applies to the release of 2025-07-16, and the card for Nova 2 Sonic to the release of 2025-12-02. The Nova 2 card was not updated for the 2026 refreshes in the text read [L: nova1-service-card, nova2-service-card].

What the Nova 2 Sonic card holds:

- Intended use: customer service automation, learning, conversational agents. Core features: low latency, speech understanding, expressive voices, dialog handling, cross-modal input, tool use and asynchronous tasks.
- Limits: official support only for English, Spanish, German, French, Italian, Portuguese and Hindi. No real-time speech translation. No pitch, accent or speed control. No fine-tuning. No defined knowledge cutoff. Safety filters cannot be set or turned off.
- Safety figures AWS gives, all on its own data sets: the model avoids harmful replies for more than 96 percent of harmful prompts, which AWS says is an improvement of more than 61 percent over Nova 1 Sonic. It deflects requests to clone a voice every time. End-to-end guardrails give safe replies to more than 95 percent of 8.5 thousand toxic prompts, and the model avoids biased replies on 97 percent of bias prompts.
- Privacy: Bedrock does not store or review prompts or speech. AWS does not use inputs or outputs to train the model. Session context is held in memory during a session.
- Transparency: an inaudible watermark in all generated audio.

[L: nova2-service-card]. The card names the evaluation methods (public data such as Multilingual LibriSpeech, FLEURS, VoiceBench IFEval and CommonEval, and a function-calling set converted to speech) and gives no scores for them in the text read [L: nova2-service-card].

## Family-wide behaviour

- A tool call needs a result. The model expects a toolResult after every toolUse, even for an error. If the client sends none, the model waits and can stop responding [L: nova2-sonic-tools].
- Asynchronous tool calls work with no setting in Nova 2 Sonic. The model keeps listening and speaking while a tool runs. If the user changes the request, the system does not cancel the pending call, and the result still reaches the model [L: nova2-sonic-async-tools].
- Barge-in: the model stops, keeps its context and sends a signal. Audio is generated faster than it plays, so the client clears its queue [L: nova2-sonic-barge-in].
- Save the final transcript, not the speculative one, to chat history [L: nova2-sonic-chat-history].
- Practitioner reports (A): a LiveKit issue of 2026-02-18 against amazon.nova-2-sonic-v1:0 says that, after a tool call, the model sometimes keeps generating speech. Each sentence made a new generation in the plugin, and the tool result stayed stuck until the user spoke. The report says the failure was intermittent, and the issue is marked closed [A: gh-livekit-4887]. An AWS re:Post question of 2025-08-15 says Nova Sonic gathered tool parameters and did not call the tool in about 25 percent of tests. It was asked before Nova 2 Sonic was released on 2025-12-02, so it concerns the first generation [A: repost-inconsistent-tools].
- Independent measurement: Artificial Analysis lists Nova 2 Sonic (March 2026 version) with speech reasoning 88, an arena preference Elo of 974, a task success rate of 57.1 and a time to first audio of 1.14 seconds. It lists no row for Nova Sonic v1 [M: aa-speech-to-speech].
- A consultancy's AWS-blog write-up compares both generations with its own LLM judge on one voice-agent task: overall 2.4 for v1 and 2.7 for v2 with the same baseline prompt. After two prompt revisions it reached 3.8. Its changes were templated variables, bullets under labelled headings, behaviour examples and a checklist before each reply [A: aws-blog-voice-agent].

## Open questions

- Whether Nova Sonic v1 still answers requests after its end-of-life date of 2026-09-14. AWS pages still list it as Legacy.
- Which model Amazon will offer after Nova 2 Sonic. The Bedrock card gives only a floor of 2026-12-02.
- How many voices Nova 2 Sonic has: the service card says eighteen and twenty-two in two sentences, and the language-support page lists 16 ids.
- Whether Bedrock Guardrails and abuse detection apply to Nova 2 Sonic.
- Whether the us. and global. inference ids of Nova 2 Sonic exist.
- What the pause durations of the sensitivity levels (1.5, 1.75 and about 2 seconds) measure, and why the highest sensitivity has the shortest pause.

## Sources

Each id below is used above, with its class, and was read on 2026-10-03.

- nova2-sonic-prompts (L): https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-system-prompts.html
- bedrock-card-nova-2-sonic (L): https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-2-sonic.html
- bedrock-lifecycle-legacy (L): https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html
- bedrock-card-nova-sonic (L): https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-nova-sonic.html
- aws-price-list (L): https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonBedrock/current/index.json
- nova1-whats-new (L): https://aws.amazon.com/about-aws/whats-new/2025/04/amazon-nova-sonic-speech-to-speech-conversations-bedrock/
- nova1-service-card (L): https://docs.aws.amazon.com/ai/responsible-ai/nova-sonic/overview.html
- nova2-whats-new (L): https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-nova-2-sonic-real-time-conversational-ai
- nova2-release-notes (L): https://docs.aws.amazon.com/nova/latest/nova2-userguide/release-notes.html
- nova2-sonic-chat-history (L): https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-chat-history.html
- nova2-sonic-getting-started (L): https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-getting-started.html
- nova2-sonic-integrations (L): https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-integrations.html
- nova2-sonic-input-events (L): https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-input-events.html
- nova2-sonic-output-events (L): https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-output-events.html
- nova1-model-specs (L): https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html
- nova2-service-card (L): https://docs.aws.amazon.com/ai/responsible-ai/nova-2-sonic/overview.html
- nova2-sonic-cross-modal (L): https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-cross-modal.html
- nova-pricing-page (L): https://aws.amazon.com/nova/pricing/
- nova1-prompting (L): https://docs.aws.amazon.com/nova/latest/userguide/prompting-speech.html
- nova2-sonic-tools (L): https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-tool-configuration.html
- nova2-sonic-async-tools (L): https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-async-tools.html
- nova2-sonic-barge-in (L): https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-barge-in.html
- gh-livekit-4887 (A): https://github.com/livekit/agents/issues/4887
- repost-inconsistent-tools (A): https://repost.aws/questions/QUhD4OjsK5TWaZCmhkV44Glg/nova-sonic-inconsistent-tool-calling
- aa-speech-to-speech (M): https://artificialanalysis.ai/speech-to-speech
- aws-blog-voice-agent (A): https://aws.amazon.com/blogs/machine-learning/how-loka-built-a-natural-low-latency-voice-agent-with-amazon-nova-2-sonic/
- nova2-core-inference (L): https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html
- nova2-doc-history (L): https://docs.aws.amazon.com/nova/latest/nova2-userguide/doc-history.html
