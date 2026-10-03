# Providers

A provider is a route to a model: an API, a cloud service, a gateway or a program on your own
machine. The same model can behave differently on each route. A route can rename a control, leave out
a feature, change the price or keep your data for a different time. Use this folder when you must
choose a route, or when you must know what a route changes.

The model files in [../models/](../models/README.md) describe a model as its maker serves it. A
provider file says what is different on its route.

## Choose a kind of provider

Every provider file has one of these five kinds, in its `kind` field.

| Kind | Meaning | Look first at |
| --- | --- | --- |
| first-party lab API | The API of the lab that trains the model | "API surface" |
| cloud platform | A cloud vendor's model service, which serves the models of several makers | "Feature parity" and "Limits and data" |
| router or gateway | One endpoint in front of many providers, with routing, fallback or a proxy | "Notes for agents and harnesses" |
| inference host | A company that hosts open-weight and other models for API use | "Pricing" and "Limits and data" |
| local runtime | Software that runs a model on your own hardware | "Feature parity" and "API surface" |

A provider that no longer exists, or that you cannot check against its own pages, has no file.

## What a provider file holds

The file opens with the frontmatter that [CONVENTIONS.md](../CONVENTIONS.md) describes, plus a `kind`
field. Then it has a `# <Provider>` title, a paragraph that says what the provider is, and these
headings. Every heading is present, in this order. `scripts/check.py` fails a file that lacks one.

```text
## Models offered
The model classes and makers it serves, linking the model files in scope.
## API surface
The protocol (its own, OpenAI-compatible or Anthropic-compatible), authentication, SDKs and how
model ids are named.
## Feature parity
Against the maker's own API: reasoning and effort controls, tools, structured output, caching,
batch, long context, vision and streaming; what is missing or renamed.
## Pricing
The pricing model: per token, provisioned, a markup over list, free tiers. No price table that
repeats a card.
## Limits and data
Rate limits, regions, data retention, use for training and zero-retention options.
## Notes for agents and harnesses
Parameter and effort mapping, and the traps.
## Sources
```

A provider file does not repeat the price of a model. The card of the model holds the price. The
section "Pricing" says how the provider charges.

## Every provider

The table is generated. `scripts/render.py` builds it from the files in this folder. The kind comes
from the `kind` field of the file, or from the first line under its title. Do not edit the table.

<!-- providers:begin -->
| Provider | Kind | File |
| --- | --- | --- |
| Alibaba Cloud Model Studio | first-party lab API | [alibaba-model-studio.md](alibaba-model-studio.md) |
| Anthropic API | first-party lab API | [anthropic.md](anthropic.md) |
| Cohere | first-party lab API | [cohere.md](cohere.md) |
| DeepSeek API | first-party lab API | [deepseek.md](deepseek.md) |
| ElevenLabs | first-party lab API | [elevenlabs.md](elevenlabs.md) |
| Google Gemini API and AI Studio | first-party lab API | [google-gemini-api.md](google-gemini-api.md) |
| Meta API | first-party lab API | [meta.md](meta.md) |
| MiniMax API | first-party lab API | [minimax.md](minimax.md) |
| Mistral API | first-party lab API | [mistral.md](mistral.md) |
| Moonshot (Kimi) API | first-party lab API | [moonshot.md](moonshot.md) |
| OpenAI API | first-party lab API | [openai.md](openai.md) |
| TypeSafe API | first-party lab API | [typesafe.md](typesafe.md) |
| xAI API | first-party lab API | [xai.md](xai.md) |
| Z.ai (Zhipu) API | first-party lab API | [zai.md](zai.md) |
| Amazon Bedrock | cloud platform | [amazon-bedrock.md](amazon-bedrock.md) |
| Cloudflare Workers AI | cloud platform | [cloudflare-workers-ai.md](cloudflare-workers-ai.md) |
| Databricks Mosaic AI Model Serving | cloud platform | [databricks-mosaic-ai.md](databricks-mosaic-ai.md) |
| Gemini Enterprise Agent Platform (formerly Vertex AI) | cloud platform | [google-vertex-ai.md](google-vertex-ai.md) |
| IBM watsonx.ai | cloud platform | [ibm-watsonx-ai.md](ibm-watsonx-ai.md) |
| Microsoft Foundry | cloud platform | [microsoft-foundry.md](microsoft-foundry.md) |
| Oracle OCI Generative AI | cloud platform | [oracle-oci-generative-ai.md](oracle-oci-generative-ai.md) |
| Snowflake Cortex | cloud platform | [snowflake-cortex.md](snowflake-cortex.md) |
| Hugging Face Inference Providers | router or gateway | [hugging-face-inference-providers.md](hugging-face-inference-providers.md) |
| LiteLLM | router or gateway | [litellm.md](litellm.md) |
| OpenRouter | router or gateway | [openrouter.md](openrouter.md) |
| Portkey | router or gateway | [portkey.md](portkey.md) |
| Requesty | router or gateway | [requesty.md](requesty.md) |
| Vercel AI Gateway | router or gateway | [vercel-ai-gateway.md](vercel-ai-gateway.md) |
| Baseten | inference host | [baseten.md](baseten.md) |
| Cerebras | inference host | [cerebras.md](cerebras.md) |
| DeepInfra | inference host | [deepinfra.md](deepinfra.md) |
| Fireworks AI | inference host | [fireworks-ai.md](fireworks-ai.md) |
| Groq | inference host | [groq.md](groq.md) |
| Nebius Token Factory | inference host | [nebius-token-factory.md](nebius-token-factory.md) |
| NVIDIA NIM | inference host | [nvidia-nim.md](nvidia-nim.md) |
| Replicate | inference host | [replicate.md](replicate.md) |
| SambaNova | inference host | [sambanova.md](sambanova.md) |
| Together AI | inference host | [together-ai.md](together-ai.md) |
| llama.cpp | local runtime | [llama-cpp.md](llama-cpp.md) |
| LM Studio | local runtime | [lm-studio.md](lm-studio.md) |
| MLX and mlx-lm | local runtime | [mlx-lm.md](mlx-lm.md) |
| Ollama | local runtime | [ollama.md](ollama.md) |
| SGLang | local runtime | [sglang.md](sglang.md) |
| vLLM | local runtime | [vllm.md](vllm.md) |
<!-- providers:end -->
