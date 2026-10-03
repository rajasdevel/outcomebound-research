---
last_checked: 2026-10-04
volatility: MONITOR (lineage, guides and API behaviour change at each release)
sources:
  - https://learn.microsoft.com/azure/ai-services/speech-service/mai-voices
  - https://learn.microsoft.com/en-us/azure/ai-services/speech-service/high-definition-voices
  - https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice
  - https://learn.microsoft.com/en-us/azure/ai-services/speech-service/text-to-speech
  - https://microsoft.ai/models/mai-voice-2-1/
  - https://microsoft.ai/news/mai-voice-2/
  - https://ai.azure.com/catalog/models/MAI-Voice-2.1
  - https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/-/4481288
  - https://artificialanalysis.ai/text-to-speech/leaderboard/provider-voice
---

# Microsoft models

Microsoft sells speech synthesis through Azure Speech in Microsoft Foundry. This folder holds the Microsoft models that take direction for delivery, beyond a choice of voice: the Dragon HD voice models of Azure Speech. Microsoft has no other model in this library. The MAI-Voice models of Microsoft AI have no file (see below), but this page keeps what was read about them, because they share the API. The page holds what is true across these models: the lineage, the API, Microsoft's guides, behaviour that shows up across the family and the open questions. Each model file says what differs for its model. Facts are as of 2026-10-04 unless a date is given. Evidence classes: L is Microsoft's own page, M is an independent measurement, A is one outlet's or one person's account.

> **Note.** Dragon HD gives less free direction than the other speech models in this library. It takes a style keyword or a bracket tag from a fixed list, and its Omni model claims style prediction from natural-language descriptions that the pages read do not show in use. It takes no free instruction string. The files say so in their Voice sections.

## Models and lineage

| Class | Current generation | Previous generation | Status on 2026-10-04 |
| --- | --- | --- | --- |
| Dragon HD Omni | [Dragon HD Omni](dragon-hd-omni.md), preview announced 2026-01-07 | none | The announcement says preview; the later Learn page shows no banner [L: ms-tc-omni, ms-hd] |
| Dragon HD | [Dragon HD](dragon-hd.md) | none | Voices listed as generally available, with some in preview [L: ms-hd] |

Models that exist and have no file here. MAI-Voice-2.1 and MAI-Voice-2.1-Flash (versions dated 2026-09-19), MAI-Voice-2 (launched 2026-06-02) and MAI-Voice-2-Flash (version dated 2026-07-22) take a style name from a list that differs per voice, set with SSML `mstts:express-as`. That is the same per-voice preset mechanism as the Azure neural voices below, so they are not voice actor models. The MAI-Voice-2 launch post claims emotion tags, but the Learn page read shows only the SSML styles [L: ms-mai-voices, ms-blog-voice2]. MAI-Voice-1 (catalog version 2025-12-18, in the arena data from April 2026) is older than the two generations in scope. The Azure neural voices of earlier years take SSML speaking styles per voice. They are a fixed preset list with no tags and no free text, and they are not voice actor models. Azure OpenAI voices take a different SSML subset, and Microsoft says the Azure Speech SSML table does not apply to them. Azure Speech HD Flash voices speak zh-CN and en-US text only. Microsoft's Voice Live API is a conversation product that can use these voices for speech output. It has no file in this folder.

The names of Dragon HD and Dragon HD Omni are Microsoft's names for two base models. Microsoft gives neither a generation number. This library treats them as two classes of one model each, and not as a current and a previous generation of one class [L: ms-hd].

## API surface

- **One route for every model.** SSML or plain text goes to the `cognitiveservices/v1` endpoint of an Azure Speech resource, through the Speech SDK (.NET, Python, Java, JavaScript, C++), the Speech CLI or REST. The MAI models use the same Azure Speech API and SDK as the neural and HD voices [L: ms-mai-voices].
- **The voice name selects the model.** The pattern is `voicename:model`: for example `en-US-Ava:DragonHDLatestNeural`, `en-us-ava:DragonHDOmniLatestNeural` and `en-US-Harper:MAI-Voice-2.1-Flash`. `LatestNeural` follows the newest base model [L: ms-hd, ms-mai-voices].
- **Output.** The HD voice page lists opus, mp3, pcm and truesilk at 8, 16, 24 and 48 kHz. The MAI examples request 24 kHz mono MP3. HD voices run in real time only and are cloud only [L: ms-hd, ms-mai-voices].
- **Regions.** MAI-Voice-2.1 and 2.1-Flash are served from 14 listed regions and routed. The Omni preview began in four regions [L: ms-mai-voices, ms-tc-omni].
- **Custom voices.** Personal voice, called instant voice cloning for MAI, is gated. It needs a Limited Access review, a consent recording and a prompt recording. Microsoft says only authorised, consented voices can be used in production [L: ms-mai-voices, ms-blog-voice2].
- **Price.** Per character. The maker's page lists US$22 per 1M characters for MAI-Voice-2.1 and US$15 for 2.1-Flash. The Azure retail price API lists US$22 for Neural HD text to speech and no MAI meter [L: ms-mai-page, azure-retail].

## Prompting guides

Microsoft's direction guidance is in reference pages and not in a prompting guide.

| Page | Covers |
| --- | --- |
| High-definition voices | The two HD base models, 53 style keywords for Dragon HD and 61 for Omni, six paralinguistic tags, Omni parameters (temperature, top_p, top_k and cfg_scale), the pronunciation switch, which SSML elements each model accepts [L: ms-hd] |
| SSML voice and sound | `mstts:express-as` with `style`, `styledegree` (0.01 to 2) and `role` for neural voices; the three ways to give an HD style (express-as, bracket markers inside SSML, bracket markers in plain text); multi-talker dialogue [L: ms-ssml-voice] |
| MAI-Voice in Azure Speech | The two MAI-Voice-2.1 models, SSML examples, regions, a table of 97 managed voices with the styles each accepts [L: ms-mai-voices] |
| Dragon HD Omni announcement | 700+ voices, automatic style prediction from natural-language descriptions, word boundary events, parameter tuning [L: ms-tc-omni] |
| MAI-Voice-2 launch post | Emotion tags, role-play voices, 15 languages, code-switching [L: ms-blog-voice2] |

**How the advice has moved.** The older neural voices needed per-voice style tuning. Dragon HD (HD voices) moved to a model that reads the text and picks emotion on its own. Omni added a larger voice set with style keywords and paralinguistic tags, and the announcement says it predicts style from natural-language descriptions. MAI-Voice-2 added a launch-post claim of emotion tags and role voices. MAI-Voice-2.1 documents SSML styles per voice [L: ms-hd, ms-tc-omni, ms-blog-voice2, ms-mai-voices].

## System-card practice

Microsoft links a model card memo, as a PDF, for MAI-Voice-2.1 and for 2.1-Flash on the page of Microsoft AI, and the Foundry catalog has Responsible AI and licence tabs. The text of the two PDFs could not be extracted on 2026-10-04, so no fact in this folder rests on them. Dragon HD has no model card in the pages read. Microsoft's safeguards that the pages state: gated voice cloning with consent audio, a Code of Conduct for text to speech, and a note that usage must not be inconsistent with it [L: ms-mai-page, ms-catalog-21].

## Family-wide behaviour

- **Style results follow the text.** Microsoft says HD style results are strongly relevant to the input content, because the model adapts the style to the meaning of the text [L: ms-hd].
- **A style marker lasts.** In HD voices a bracket style marker applies to all later sentences until you reset it with a neutral marker. A line break, a paragraph tag and an automatic sentence boundary also reset it. A break tag does not [L: ms-ssml-voice].
- **Styles on all English text; paralinguistics in every language.** The six paralinguistic tags are laughter, coughing, throat clearing, breathing, sighing and yawning [L: ms-hd].
- **An invalid style is dropped.** For neural voices, a missing or invalid `style` makes the service ignore the whole `express-as` element and use neutral speech [L: ms-ssml-voice].
- **HD voices accept part of SSML.** Prosody, emphasis, silence and bookmarks are not accepted by either HD model. Both accept lexicon (alias only), say-as and sub. Dragon HD also accepts phoneme and break, and Omni accepts neither [L: ms-hd].
- **Randomness.** HD voices have a temperature setting. Omni also has top_p, top_k and cfg_scale. Higher values give more varied emotion and lower values give more stable speech [L: ms-hd].

## Open questions

- Whether MAI-Voice-2 and 2-Flash stay on sale. The catalog lists them and the Learn page does not.
- The Azure price of the MAI-Voice models. The Azure pages read show no figure.
- Whether Dragon HD accepts `express-as` and bracket styles. One Learn section says yes and another says no.
- Whether Omni's natural-language style descriptions exist in a form a reader can use.
- What the model card memos for MAI-Voice-2.1 say.

## Sources

- [ms-mai-voices] https://learn.microsoft.com/azure/ai-services/speech-service/mai-voices (kind L, read 2026-10-04)
- [ms-hd] https://learn.microsoft.com/en-us/azure/ai-services/speech-service/high-definition-voices (kind L, read 2026-10-04)
- [ms-ssml-voice] https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice (kind L, read 2026-10-04)
- [ms-mai-page] https://microsoft.ai/models/mai-voice-2-1/ (kind L, read 2026-10-04)
- [ms-blog-voice2] https://microsoft.ai/news/mai-voice-2/ (kind L, read 2026-10-04)
- [ms-catalog-21] https://ai.azure.com/catalog/models/MAI-Voice-2.1 (kind L, read 2026-10-04)
- [ms-catalog-2] https://ai.azure.com/catalog/models/MAI-Voice-2 (kind L, read 2026-10-04)
- [ms-tc-omni] https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/-/4481288 (kind L, read 2026-10-04)
- [azure-retail] https://prices.azure.com/api/retail/prices (kind L, read 2026-10-04)
