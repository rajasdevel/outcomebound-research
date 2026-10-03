---
last_checked: 2026-10-04
volatility: MONITOR (lineage, tags and licences change at each release)
sources:
  - https://github.com/resemble-ai/chatterbox
  - https://huggingface.co/ResembleAI/chatterbox-turbo
  - https://huggingface.co/ResembleAI/chatterbox-nano
  - https://huggingface.co/ResembleAI/Dramabox
  - https://huggingface.co/ResembleAI/Dramabox/raw/main/LICENSE
  - https://huggingface.co/api/models?author=ResembleAI&sort=lastModified&direction=-1&limit=15
---

# Resemble AI

Resemble AI makes voice products and publishes open-weight speech synthesis models. This folder holds the three open models that direct delivery by tags or by prose: Chatterbox-Turbo, Chatterbox-Nano and Dramabox. Everything here was read on 2026-10-04.

## Models and lineage

| Class | Model | Notes |
| --- | --- | --- |
| Chatterbox Turbo | [Chatterbox-Turbo](chatterbox-turbo.md) | 350M, English, square-bracket tags, MIT, released 2025-12-02 [hf-cb-turbo] |
| Chatterbox Turbo | [Chatterbox-Nano](chatterbox-nano.md) | 110M, same design in a smaller package for CPU use, MIT, released 2026-04-14 [hf-cb-nano] |
| Dramabox | [Dramabox](dramabox.md) | 3.3B diffusion transformer driven by scene prose, LTX-2 Community License, released 2026-04-17 [hf-dramabox] |

Chatterbox is a family of five lines. The original Chatterbox (500M, English, 2025-04-24) and Chatterbox Multilingual V3 (23 languages, 2026-06-10, with a pack of six single-language finetunes) steer expression with an exaggeration value and a guidance weight. They take no tags. They are not voice actor models and have no file. Chatterbox-Flash (2026-05-28) is a block-diffusion model for speed; its card shows no tags, so it has no file either [gh-cb] [hf-cb-flash].

## API surface

Resemble AI ships the weights with a Python package, `chatterbox-tts`, and a repository. It also sells a hosted text-to-speech service that the README links and says has latency under 200 ms. The hosted model ids and prices were not read [gh-cb].

## Prompting guides

Resemble AI publishes no prompting guide. The Chatterbox README gives tips for the original model. The default exaggeration is 0.5 and the default guidance weight is 0.5. For dramatic speech, try a guidance weight near 0.3 and an exaggeration of 0.7 or more. A higher exaggeration speeds speech up [gh-cb]. The Dramabox card has a full prompt-format section, summarised in its file [hf-dramabox].

## System-card practice

None. Resemble AI publishes no system cards. Every Chatterbox output carries the Perth neural watermark, and the README gives an extraction script. Dramabox adds the same watermark by default, and a flag turns it off [gh-cb] [hf-dramabox].

## Family-wide behaviour

- **Licences differ.** The Chatterbox models are MIT. Dramabox uses the LTX-2 Community License because it is adapted from a Lightricks model [hf-dramabox].
- **Watermark.** On for all outputs of the Chatterbox models; on by default for Dramabox [gh-cb] [hf-dramabox].
- **Tags.** The Turbo and Nano models use square-bracket tags; Dramabox uses stage directions in prose, with sounds written as words inside quotes [hf-cb-turbo] [hf-dramabox].

## Open questions

- A documented tag list for Turbo and Nano.
- The use restrictions of the LTX-2 Community License. Its commercial threshold is known: an entity with annual revenue of US$10,000,000 or more needs a paid licence [hf-dramabox-license].
- Independent measures of tag and direction control for all three models.

## Sources

- [gh-cb] https://github.com/resemble-ai/chatterbox (kind L, read 2026-10-04)
- [hf-cb-turbo] https://huggingface.co/ResembleAI/chatterbox-turbo (kind L, read 2026-10-04)
- [hf-cb-nano] https://huggingface.co/ResembleAI/chatterbox-nano (kind L, read 2026-10-04)
- [hf-cb-flash] https://huggingface.co/ResembleAI/chatterbox-flash (kind L, read 2026-10-04)
- [hf-dramabox] https://huggingface.co/ResembleAI/Dramabox (kind L, read 2026-10-04)
- [hf-dramabox-license] https://huggingface.co/ResembleAI/Dramabox/raw/main/LICENSE (kind L, read 2026-10-04)
