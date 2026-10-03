---
last_checked: 2026-10-03
volatility: MONITOR (lineage, guides and API behaviour change at each release)
sources:
  - https://github.com/kyutai-labs/moshi
  - https://github.com/kyutai-labs/moshi-rag
  - https://huggingface.co/kyutai/moshiko-pytorch-bf16
  - https://huggingface.co/kyutai/moshika-rag-pytorch-bf16
  - https://arxiv.org/abs/2410.00037
  - https://arxiv.org/abs/2604.12928
  - https://huggingface.co/api/models?author=kyutai&sort=lastModified&direction=-1&limit=60
  - https://artificialanalysis.ai/speech-to-speech
  - https://arxiv.org/abs/2606.11167
---

# Kyutai

Kyutai is a research lab that publishes open speech models. Its full-duplex dialogue models, Moshi and MoshiRAG, are in this folder. Kyutai runs no hosted API for them that was found. A person runs the weights on their own hardware. Everything here was read on 2026-10-03.

## Models and lineage

| Class | Model | Notes |
| --- | --- | --- |
| Moshi | [Moshi](moshi.md) (Moshiko and Moshika) | September 2024. The first open full-duplex speech-to-speech model. About 7 billion parameters in its main transformer, built on Kyutai's Helium text model, with the Mimi audio codec. English only [kyutai-card-moshiko] [kyutai-gh-moshi]. |
| Moshi | [MoshiRAG](moshirag.md) | 2026. A Moshika-based full-duplex front end with a separate retrieval back end that looks up facts while the model keeps talking. Paper dated 2026-04-14 [kyutai-card-moshirag] [kyutai-moshirag-paper]. |

Kyutai numbers no generations. The class Moshi holds these two models as its two generations.

Models and artifacts of Kyutai that have no file, with the reason (names, dates and pipeline tags come from Kyutai's Hugging Face listing) [hf-kyutai-list]:

- **Hibiki and Hibiki-Zero** (2025-02 and 2026-02). Streaming speech-to-speech translation, not conversation. Left out because the scope is conversational speech models.
- **Kyutai STT, Kyutai TTS and Pocket TTS** (2025 and 2026). Speech recognition and synthesis models, not full-duplex products.
- **`moshika-rl-seamless` and `personaplex-rl-seamless`** (2026-06). Gated research checkpoints. Their tags name fine-tunes of Moshika (licence CC-BY-NC 4.0) and of NVIDIA's PersonaPlex (licence "other") on Meta's Seamless Interaction data. They name a paper on reinforcement learning for interactive behaviour, such as turn-taking, in full-duplex models [kyutai-rl-paper]. The files need access approval and were not read, so these checkpoints have no file.
- **`glm-4-voice-of-reason-9b` and the stitch variant** (2026-08 and 2026-09). Research fine-tunes of Z.ai's GLM-4-Voice under that model's licence. The card describes reasoning by reinforcement learning on math problems. They are not Moshi models, and the card does not describe a full-duplex mode [kyutai-card-glm-voice].
- Moshi builds with vision (`moshika-vis`, 2025) and several quantized builds of Moshi (MLX, Candle, int8) are variants of the files above.

## API surface

There is no hosted API. The code is at `kyutai-labs/moshi`. The Python and web-client code is under the MIT licence and the Rust backend under Apache. The weights are under CC-BY 4.0 [kyutai-gh-moshi].

- **PyTorch.** `python -m moshi.server` starts a web server with a browser client. The README says the PyTorch version does not support quantization and needs a GPU with a large memory (24 GB); it also lists an experimental int8 PyTorch build. A `--gradio-tunnel` option gives access from a remote machine. Browsers need HTTPS to open the microphone [kyutai-gh-moshi].
- **MLX.** `moshi_mlx` runs on a Mac with weights quantized to 4 or 8 bits, tested on a MacBook Pro M3 [kyutai-gh-moshi].
- **Rust and Candle.** A Rust server and Candle builds of the weights (bf16 and int8) exist [kyutai-gh-moshi].
- **Builds.** Both voices (Moshiko, Moshika) come in PyTorch, MLX and Candle formats on Hugging Face [kyutai-gh-moshi].
- **Audio.** 24 kHz mono. The Mimi codec runs at 12.5 frames per second and about 1.1 kbit/s [kyutai-card-moshiko].

## Prompting guides

Kyutai publishes no prompting guide. The released Moshi builds take no system prompt. The card for Moshi says the model suits casual conversation and has limited ability for complex tasks. NVIDIA's PersonaPlex, built on the Moshiko weights, added text and voice prompts. See [PersonaPlex](../other/personaplex-7b-v1.md) [kyutai-card-moshiko].

## System-card practice

Kyutai publishes a Hugging Face model card for each model and a paper. The Moshi card lists intended and out-of-scope use, a short risk section, training data and compute (127 DGX nodes with 1,016 H100 GPUs, per the card). The Moshi paper has a safety part with toxicity, regurgitation, voice consistency and watermarking checks. The MoshiRAG card adds that the safety of its answers depends on the retrieval back end [kyutai-card-moshiko] [kyutai-moshi-paper] [kyutai-card-moshirag].

## Family-wide behaviour

- Both models are full-duplex. They have no turn detector and no interruption setting. They decide for themselves when to speak [kyutai-moshi-paper].
- Both are English only, with one fixed voice per build. Kyutai's cards say the models are trained to produce one voice only, to avoid impersonation [kyutai-card-moshiko] [kyutai-card-moshirag].
- Both are for research use. Kyutai's cards say not to use them for advice or professional duty [kyutai-card-moshiko].
- Artificial Analysis lists Moshi at 4.4% on speech reasoning and 61.0% on conversational dynamics (read 2026-10-03). It lists no MoshiRAG row [aa-s2s].
- The command-line clients have no echo cancellation. The web client has it [kyutai-gh-moshi].

## Open questions

- Whether Kyutai will publish a hosted API or a model with a larger language backbone. None was found.
- Which build Artificial Analysis ran for Moshi.
- The exact release dates of both models.

## Sources

- [kyutai-card-moshiko] https://huggingface.co/kyutai/moshiko-pytorch-bf16 (kind L, read 2026-10-03)
- [kyutai-gh-moshi] https://github.com/kyutai-labs/moshi (kind L, read 2026-10-03)
- [kyutai-moshi-paper] https://arxiv.org/abs/2410.00037 (kind P, read 2026-10-03)
- [kyutai-card-moshirag] https://huggingface.co/kyutai/moshika-rag-pytorch-bf16 (kind L, read 2026-10-03)
- [kyutai-moshirag-paper] https://arxiv.org/abs/2604.12928 (kind P, read 2026-10-03)
- [kyutai-card-glm-voice] https://huggingface.co/kyutai/glm-4-voice-of-reason-9b (kind L, read 2026-10-03)
- [hf-kyutai-list] https://huggingface.co/api/models?author=kyutai&sort=lastModified&direction=-1&limit=60 (kind L, read 2026-10-03)
- [aa-s2s] https://artificialanalysis.ai/speech-to-speech (kind M, read 2026-10-03)
- [kyutai-rl-paper] https://arxiv.org/abs/2606.11167 (kind P, read 2026-10-03)
