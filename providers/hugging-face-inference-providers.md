---
last_checked: 2026-11-03
volatility: VOLATILE (the partner list, credits and per-provider support change often)
kind: router or gateway
sources:
  - https://huggingface.co/docs/inference-providers/index
  - https://huggingface.co/docs/inference-providers/pricing
  - https://huggingface.co/docs/inference-providers/tasks/chat-completion
  - https://huggingface.co/docs/inference-providers/security
  - https://huggingface.co/docs/inference-providers/guides/responses-api
  - https://huggingface.co/docs/inference-providers/integrations/claude-code
---

# Hugging Face Inference Providers

router or gateway

Inference Providers is a Hugging Face Hub feature that routes requests to partner inference services through one Hugging Face token. Hugging Face can bill routed requests; a custom provider key lets the provider bill directly. The service also includes `hf-inference`, previously called the serverless Inference API, which the pricing page says focused mainly on CPU inference as of July 2025. [index, price]

## Models offered

The index lists partners for language, vision-language, image, video and speech tasks. Its chat-completion table includes Baseten, Cerebras, Cohere, DeepInfra, Featherless AI, Fireworks, Groq, HF Inference, Novita, Nscale, OVHcloud AI Endpoints, Public AI, Scaleway, Together and Z.ai. The set of served models changes; `openai/gpt-oss-120b` is an example in the index. The pricing page describes more than 200 models. [index, price]

The index says `hf models ls --warm` lists models served by at least one provider, and `--json` gives machine-readable output. It says `GET https://router.huggingface.co/v1/models` lists models with per-provider pricing, context length, latency and throughput when available. These commands and live availability were not tested. [index]

## API surface

- **Protocols.** The router has an OpenAI-compatible Chat Completions API at `https://router.huggingface.co/v1`. Its Responses API is beta and documents event streaming, structured outputs and remote MCP tools. The index describes Chat Completions as chat-only and points to the Hugging Face clients for other tasks such as embeddings, image generation and speech. The Responses guide separately documents image input. Full parity and Responses state storage are `UNVERIFIED`. [index, responses]
- **Claude Code.** The integration guide sets `ANTHROPIC_BASE_URL` to `https://router.huggingface.co` and uses a Hugging Face token, or configures the agent with the `hf-claude` extension. Anthropic API feature parity is `UNVERIFIED`. [claude-code]
- **Clients and auth.** The Python `huggingface_hub` and JavaScript `@huggingface/inference` clients format requests for the selected provider. The OpenAI SDK can use the router as its base URL. The documentation calls for a fine-grained Hugging Face token with Inference Providers permission. [index]
- **Model ids.** A Hub id such as `openai/gpt-oss-120b` can have a suffix: `:fastest` chooses the highest throughput, `:cheapest` the lowest output-token price, and `:preferred` the first available provider in the account's preferred order. A provider suffix such as `:groq` selects that provider. In the clients, `provider="auto"` selects the fastest available provider by default, and a named provider selects that provider. [index]

## Feature parity

The chat schema lists text and image message parts, function tools, `tool_choice`, JSON response formats with `strict`, `reasoning_effort`, streaming, usage, log probabilities, seed and sampling fields. The schema describes strict JSON schema adherence, but enforcement for each model and provider was not tested. [chat]

- **Reasoning.** The schema lists `none`, `minimal`, `low`, `medium`, `high` and `xhigh` as common `reasoning_effort` values. Support and defaults depend on the model and provider; the mapping to each provider's own controls is `UNVERIFIED`. [chat]
- **Tools and structured output.** Function tools, `tool_choice` including `required`, and JSON schema are in the chat schema. Support and enforcement for a selected route are `UNVERIFIED`. [chat]
- **Prompt caching and batch.** These were not documented in the router pages read. Provider caching and pass-through controls are `UNVERIFIED`.
- **Failover.** With `provider="auto"`, the index says the service selects an alternative when its validation system flags the primary provider unavailable. [index]
- **Vision, streaming and context.** The chat schema permits image input and streaming; model and provider support can differ. The model listing can show per-provider context lengths. [chat, index]

## Pricing

Hugging Face says routed usage has no markup over provider rates. Free users have no included monthly credits and must buy credits or upgrade to use Inference Providers. PRO users receive $2 monthly; Team and Enterprise organisations receive $2 per seat monthly, shared among members. These credits also apply to other Hugging Face compute such as Inference Endpoints, Spaces hardware and Jobs. Additional usage is pay-as-you-go from purchased credits. [price]

Routed billing uses the Hugging Face account and eligible credits; a custom provider key makes the provider bill directly and credits do not apply. Team and Enterprise users can bill an organisation using `X-HF-Bill-To` or the client `bill_to` option. Enterprise users can attribute costs to a resource group if their token is a member. Organisation administrators can set a spending limit and disable providers. `hf-inference` is billed by compute time multiplied by the underlying hardware price per second. [price]

## Limits and data

- **Rate limits.** The pages read give no Inference Providers rate-limit numbers; current limits are `UNVERIFIED`.
- **Retention and training.** Hugging Face says it does not store the request body or response when routing, keeps debug logs for up to 30 days without user data or tokens, and does not store user data for training. It directs readers to each provider's data policies. [security]
- **Security.** Hugging Face says the Hub is SOC 2 Type 2 certified, external providers are responsible for their own security, and routing uses TLS. [security]
- **Regions.** The pages read do not establish inference regions; these are `UNVERIFIED`.

## Notes for agents and harnesses

- **The default route can change.** The fastest available provider is selected by default; a provider suffix or named `provider` selects a specific provider. Feature support and context can vary by route. [index, chat]
- **API formats differ.** Chat Completions is for chat; the Responses API is beta. Claude Code can use the router with its documented base URL. The index points other tasks to the Hugging Face clients. [index, responses, claude-code]
- **Billing depends on the key.** A custom provider key is billed by the provider; Hugging Face billing applies eligible credits to routed requests. Provider data policies still apply. [price, security]
- **Free accounts have no included credit.** A free user must buy credits or upgrade to use Inference Providers. [price]

## Sources

| Id | URL | Kind | Read |
| --- | --- | --- | --- |
| index | https://huggingface.co/docs/inference-providers/index | L | 2026-11-03 |
| price | https://huggingface.co/docs/inference-providers/pricing | L | 2026-11-03 |
| chat | https://huggingface.co/docs/inference-providers/tasks/chat-completion | L | 2026-11-03 |
| security | https://huggingface.co/docs/inference-providers/security | L | 2026-11-03 |
| responses | https://huggingface.co/docs/inference-providers/guides/responses-api | L | 2026-11-03 |
| claude-code | https://huggingface.co/docs/inference-providers/integrations/claude-code | L | 2026-11-03 |
