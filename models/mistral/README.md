---
last_checked: 2026-10-03
volatility: MONITOR (lineage, guides, aliases and API behaviour changed at each of three releases in five months; older models were retired on a published schedule)
sources:
  - https://docs.mistral.ai/getting-started/models/models_overview/
  - https://docs.mistral.ai/getting-started/changelog
  - https://docs.mistral.ai/inference/model-lifecycle
  - https://docs.mistral.ai/models/mistral-medium-3-5-26-04
  - https://docs.mistral.ai/models/mistral-small-4-0-26-03
  - https://docs.mistral.ai/models/mistral-large-3-25-12
  - https://docs.mistral.ai/api/endpoint/chat
  - https://docs.mistral.ai/capabilities/reasoning/
  - https://docs.mistral.ai/capabilities/function_calling/
  - https://docs.mistral.ai/capabilities/structured_output/
  - https://docs.mistral.ai/capabilities/structured_output/custom/
  - https://docs.mistral.ai/capabilities/structured_output/json_mode/
  - https://docs.mistral.ai/capabilities/completion/prompting_capabilities/
  - https://docs.mistral.ai/capabilities/completion/sampling/
  - https://docs.mistral.ai/capabilities/vision/
  - https://docs.mistral.ai/capabilities/batch/
  - https://docs.mistral.ai/capabilities/guardrailing/
  - https://docs.mistral.ai/capabilities/document_ai/document_qna/
  - https://docs.mistral.ai/models/deployment/cloud-deployments/azure
  - https://docs.mistral.ai/vibe/
  - https://mistral.ai/pricing
  - https://mistral.ai/news/mistral-3
  - https://mistral.ai/news/mistral-small-4
  - https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5
  - https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512
  - https://huggingface.co/mistralai/Mistral-Medium-3.5-128B
  - https://huggingface.co/mistralai/Mistral-Small-4-119B-2603
  - https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/blob/main/LICENSE
  - https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md
  - https://aws.amazon.com/about-aws/whats-new/2025/12/mistral-large-3-ministral-3-family-available-amazon-bedrock
  - https://recipes.vllm.ai/mistralai/Mistral-Small-4-119B-2603
  - https://artificialanalysis.ai/models/comparisons/mistral-large-3-vs-mistral-small-4
  - https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-mistral-medium-3-5
  - https://docs.mistral.ai/inference/deployment/cloud-deployments/amazon_bedrock
  - https://docs.mistral.ai/models/deployment/cloud-deployments/vertex
  - https://legal.mistral.ai/ai-governance/models
  - https://legal.mistral.ai/documents/Mistral%20Large%203%20-%20Technical%20Documentation%20for%20Downstream%20Providers.pdf
  - https://legal.mistral.ai/documents/For%20Dowstream%20Providers%20only%20-%20Technical%20Documentation%20Mistral%20Small%204.pdf
  - https://legal.mistral.ai/ai-governance/models/mistral-medium-3
---

# Mistral models

Mistral AI, a French lab, publishes both closed (Premier) and open-weight models. Three open-weight general models
have files here: [Mistral Large 3](mistral-large-3.md), a non-reasoning mixture of experts; [Mistral Small
4](mistral-small-2603.md), a mixture of experts that merges instruct, reasoning and coding; and [Mistral Medium
3.5](mistral-medium-3-5.md), a dense model that does the same at a larger size. This page holds what is shared and
what Mistral says once; each model file says what differs. Mistral's provider page is
[../../providers/mistral.md](../../providers/mistral.md).

## Models and lineage

| Model | Released | API id (Mistral's docs) | Licence | What it replaced |
| --- | --- | --- | --- | --- |
| Mistral Large 3 (v25.12) | 2025-12-02 | `mistral-large-2512` | Apache-2.0 | Large 2.0, whose listed alternative is Large 3; Large 2.1 (retired 2026-05-31) lists Medium 3.5 |
| Mistral Small 4 (v26.03) | 2026-03-16 | `mistral-small-2603` | Apache-2.0 | Small 3.2 and the Magistral Small line |
| Mistral Medium 3.5 (v26.04) | 2026-04-28 | `mistral-medium-3-5` | modified MIT | Medium 3.1, Magistral Medium, Devstral 2 |

Sources: [mistral-models-overview], [mistral-changelog], [mistral-deprecations], [mistral-small-post],
[mistral-3-post].

- **Merged lines.** Small 4 folds Mistral's instruct, reasoning (Magistral) and Devstral lines into one model, and
  Medium 3.5 does the same for Medium 3.1, Magistral and Devstral 2; Medium 3.5 replaced Devstral 2 in the Vibe coding
  agent [hf-small-4, hf-medium-3-5]. There is no separate reasoning or coding model left in these sizes.
- **Retired predecessors.** Mistral's deprecation table lists Medium 3.1 (deprecated 2026-05-22, retired 2026-08-31),
  Small 3.2 (retired 2026-07-31), Devstral 2 (retired 2026-07-31), Magistral Small and Medium 1.2 (retired 2026-07-31)
  and Large 2.1 (retired 2026-05-31) [mistral-deprecations]. This is why the previous generation of each class has no
  file: Mistral retired it.
- **Scope.** Large 3, Small 4 and Medium 3.5 are each the current generation of their class. Other current Mistral
  models have no file: Ministral 3 in 3B, 8B and 14B sizes (v25.12, Apache-2.0, with base, instruct and reasoning
  variants per Mistral's December post), Codestral (v25.08), the OCR 4.1, Voxtral, embedding and moderation models, and
  the third-party Z.ai GLM models the platform now hosts [mistral-models-overview, mistral-3-post].
- **No newer general model.** Mistral's changelog shows no general language model after Medium 3.5 (2026-04-28); its
  later entries are OCR, Leanstral, Vibe and third-party model changes through 2026-09-29 [mistral-changelog].
- **Reasoning version of Large 3.** The December 2025 post said one was coming; none is listed on the models page
  [mistral-3-post, mistral-models-overview].

## API surface

- **Endpoints.** `POST /v1/chat/completions`, `/v1/conversations`, `/v1/agents`, `/v1/batch`, `/v1/moderations`, `/v1/ocr`
  and others. Each of the three model pages lists structured outputs, function calling, document question answering,
  prefix completion, batching, agents and conversations, chat completions and built-in tools; Medium 3.5 and Small 4
  add predicted outputs [mistral-chat-api, mistral-medium-docs, mistral-small-docs, mistral-large-docs].
- **Chat parameters** (API reference): `temperature` (the recommended range is 0.0 to 0.7; the default varies by model;
  alter it or `top_p`, not both), `top_p`, `max_tokens` (prompt plus `max_tokens` cannot exceed the context), `stop`,
  `random_seed`, `response_format` (`text`, `json_object`, `json_schema`), `tools`, `tool_choice` (`auto`, `none`,
  `any`, `required` or a named tool), `parallel_tool_calls` (default true), `presence_penalty`, `frequency_penalty`,
  `n` (input billed once), `prediction`, `prompt_cache_key`, `prompt_mode`, `service_tier` (`auto` or
  `standard_only`), `safe_prompt` (default false, injects a safety prompt), `reasoning_effort` and `guardrails`. Tool types include
  functions, web search, code interpreter, image generation, document library and custom connectors
  [mistral-chat-api]. Mistral's sampling page notes that Large 3 does not support `n` [mistral-sampling-docs].
- **Reasoning control.** `reasoning_effort`. For Small 4 and Medium 3.5 the accepted values are `none` and `high`. The API
  reference's enum is longer (`none`, `minimal`, `low`, `medium`, `high`, `xhigh`) and is not split by model; the reasoning
  page says the hosted Z.ai GLM 5.3 takes `low`, `high` and `max` [mistral-reasoning-docs, mistral-chat-api,
  vllm-small-4-recipe].
- **Model ids and aliases.** Production ids follow `name-major-minor` (`mistral-medium-3-5`); `-latest` and `-major` aliases
  point at the newest General Availability model and can change behaviour and price silently, so Mistral advises pinning
  a major-minor id. Older date-style ids exist (`mistral-small-2603`, `mistral-large-2512`) [mistral-lifecycle].
- **Lifecycle.** General Availability models get no silent updates and six months' notice before retirement; Public
  Preview, Labs and third-party models get one month, and Preview and Labs models may change silently. A retired id
  returns 404 [mistral-lifecycle]. In practice Medium 3.1, deprecated on 2026-05-22, retired on 2026-08-31
  [mistral-deprecations].
- **Pricing and discounts.** Per-token list prices are on each card. Batch requests are 50% cheaper [mistral-pricing,
  mistral-batch-docs]; a batch holds one model and up to a million requests [mistral-batch-docs]. The pricing page says
  cached input tokens cost up to 90% less, and the API reference says cached tokens are billed at 10% of the input price
  and that a shared `prompt_cache_key` raises cache hits for requests with a common prefix [mistral-pricing,
  mistral-chat-api].
- **Clouds.** Mistral's Azure page lists Medium 3.5 and Large 3 (25.12) among the models available [mistral-azure-docs].
  Its Amazon Bedrock page lists Large 3 but not Medium 3.5 or Small 4, and AWS announced Large 3 on Bedrock on 2025-12-02
  [mistral-bedrock-docs, aws-large-3]. Its Vertex AI page lists none of the three [mistral-vertex-docs]. Medium 3.5 and
  Small 4 are on NVIDIA's endpoints and NIM containers [mistral-vibe-post, mistral-small-post].
- **Moderation and guardrails.** A separate moderation model, Mistral Moderation 2 (`mistral-moderation-2603`), covers about
  ten categories (including PII and jailbreaking) with a 128k context. A `guardrails` block on a chat request can
  set thresholds per category and block a request before it reaches the model; a blocked call returns HTTP 403 with
  the scores. Shieldstral 1.0, an Apache-2.0 multimodal moderation model, is also listed
  [mistral-guardrailing-docs, mistral-models-overview].

## Prompting guides

Mistral's guidance is spread over five places, all its own (class L):

1. **Prompting capabilities page.** It recommends a system prompt that opens with a role ("You are a <role>, your task is
   to <task>"), folded into the user turn when the developer cannot set the system prompt; sections marked with Markdown
   or XML-style tags, which it calls ideal; few-shot examples as made-up user and assistant turns; prompts clear and
   complete enough for a reader with no context, in hierarchical sections; objective wording in place of vague words;
   counts passed in rather than asking the model to count words or characters; output limited to what is needed;
   worded rating scales instead of numeric ones; decision trees to resolve conflicting rules; and iterating on prompts as
   on code [mistral-prompting-docs].
2. **Model cards.** Each Hugging Face card has "recommended settings" (temperature, reasoning level), a `SYSTEM_PROMPT.txt` and
   serving commands. The system prompt files identify the model as the engine of Le Chat, carry `{today}` and `{yesterday}`
   placeholders, tell it to use tools when information may be stale or missing, and say it reads images but not audio or
   video; the Small 4 and Large 3 files also tell it to ask for clarification when a request lacks context; the files state knowledge cut-offs of 2024-11-01 for
   Medium 3.5 and Small 4 and 2023-10-01 for Large 3 [hf-medium-3-5, hf-small-4, hf-large-3, system-prompts].
3. **Reasoning page.** `reasoning_effort` values, the thinking chunk and the rule to replay it [mistral-reasoning-docs].
4. **Function-calling and structured-output pages.** Tool format, `tool_choice`, parallel calls; JSON mode and custom
   schemas [mistral-function-calling-docs, mistral-structured-docs].
5. **Vibe documentation.** Instruction files, trust and permissions in Mistral's coding agent [mistral-vibe-readme].

How the advice moved. Large 3 (December 2025) is a non-reasoning model; its card recommends a temperature below 0.1 in
production, a system prompt that states the use case and how each tool is to be used, a small tool set and image aspect
ratios near 1:1 [hf-large-3].
Small 4 (March 2026) introduced the per-request `none` or `high` switch and temperatures of 0.0 to 0.7 or 0.7
[hf-small-4]. Medium 3.5 (April 2026) kept the switch, added a top-p of 0.95 for `high`, and recommends `high` for
complex and agentic work [hf-medium-3-5]. Mistral publishes no coding-agent prompting guide for any of the three.

**Vibe, Mistral's coding agent.** Vibe reads `~/.vibe/AGENTS.md` and project `AGENTS.md` files from the working directory up to
the trust root; these instructions override the default system prompt and load only for trusted folders. It discovers
skill folders in `.agents/skills/` and `.vibe/skills/` (project, trusted only) and in `~/.vibe/skills/` and
`~/.agents/skills/`. Tool permissions are set per tool (the README's examples use `ask` and `always`; bash also takes
allowlists and denylists), with agent profiles `ask`, `plan`,
`accept-edits` (the default) and `auto-approve`. Subagents run independently (a read-only `explore` subagent is built
in), and MCP servers use `http`, `streamable-http` or `stdio` transports [mistral-vibe-readme]. Medium 3.5 is the default
model in Vibe and Le Chat, and Mistral's remote agents run coding sessions in isolated cloud sandboxes, in parallel,
and can open pull requests; Le Chat asks for approval before sensitive actions [mistral-vibe-post]. On 2026-05-28 Mistral
renamed the product: Vibe is now its unified agent at chat.mistral.ai, with Work, Code and Chat modes, the last keeping
the earlier Le Chat experience [mistral-changelog].

## System-card practice

Mistral publishes no system card or safety report for any of these three models. For each release it publishes a launch
post, a Hugging Face model card (usage settings, serving commands, benchmark charts that are mostly images, a licence)
and a docs model page (id, price, context, capability list). Under the EU AI Act it also keeps an AI governance hub that
classes each model as a general-purpose AI model (not one with systemic risk) and, for Large 3 and Small 4, posts
technical documentation for downstream providers and a public summary of training content; the Medium 3 family page,
which lists Medium 3.5 as a version released on 2026-04-29, links no such file [mistral-governance-models,
mistral-td-large-3, mistral-td-small-4, mistral-governance-medium-3]. The technical documentation gives input and output
limits, intended, restricted and prohibited uses, hardware needs and a general account of training data, and holds no
evaluation results. None of these documents reports refusal or over-refusal rates, reward hacking, sycophancy,
deception, sandbagging, prompt-injection results or cyber and biology evaluations. The only lab-side safety
material is the separate moderation tooling above. Independent signals therefore come from measurers: Artificial
Analysis's AA-Omniscience index, which penalises wrong answers, scored Large 3 at -40, Small 4 at -30 and Medium 3.5 at -37
on its v4.3.2 run [aa-compare-large-small, aa-compare-1-3-max-vs-medium]. The launch posts carry claims, not safety
evidence.

## Family-wide behaviour

- **Reasoning is a per-request toggle.** On Small 4 and Medium 3.5, `reasoning_effort="high"` returns the answer as a list of
  chunks, a thinking chunk followed by a text chunk; `none` returns a plain string. While streaming, `delta.content` changes
  shape in three phases (thinking list, a transition, plain string). Mistral says to replay the whole assistant message,
  thinking chunk included, into the history and warns that stripping it degrades performance
  [mistral-reasoning-docs]. Under vLLM, `--reasoning-parser mistral` puts thinking in `message.reasoning`
  [hf-medium-3-5].
- **Tool calls.** Each call has an `id` that the tool message must echo as `tool_call_id`; `parallel_tool_calls` defaults to
  true. With vLLM, enable `--enable-auto-tool-choice --tool-call-parser mistral` [mistral-function-calling-docs,
  hf-medium-3-5].
- **JSON.** JSON mode guarantees valid JSON but Mistral still says to ask for JSON and describe the format in the prompt;
  custom schemas (a Pydantic class through `client.chat.parse`) are described as more reliable and recommended; the SDK
  prepends a schema instruction, the docs advise adding more explanation to the system prompt, and the example runs at
  temperature 0 [mistral-structured-docs].
- **Self-hosting needs current libraries.** Large 3 needs vLLM and `mistral_common` of recent versions; Medium 3.5 needs vLLM
  nightly with `mistral_common` 1.11.1 or later and Transformers 5.4 or later, and its Transformers config once held a wrong
  entry that degraded long-context quality (GGUF files made before the fix are affected); Small 4 needs vLLM 0.20.0 or later
  for tool and reasoning parsing [hf-large-3, hf-medium-3-5, vllm-small-4-recipe]. Mistral recommends its API when local
  serving underperforms [hf-medium-3-5].
- **Hardware.** Large 3 (675 billion parameters, 41 billion active) runs in FP8 on one node of H200 or B200 GPUs, in NVFP4 on
  H100 or A100 nodes [hf-large-3]. Small 4 (119 billion, about 6.5 billion active) needs two H200, B200 or MI300X GPUs, or one
  B200 with the NVFP4 build; at 256k context on two H200 an out-of-memory error can occur and the vLLM recipe suggests
  131,072 tokens or NVFP4 [vllm-small-4-recipe]. Mistral's own technical documentation gives a minimum of four H100, two
  H200 or one B200 for Small 4, and 16 H200 for standard Large 3 inference with at least eight for FP8
  [mistral-td-small-4, mistral-td-large-3]. Medium 3.5 (128 billion dense) is documented with eight-way tensor
  parallelism in its card and "as few as four GPUs" in the launch post [hf-medium-3-5, mistral-vibe-post].
- **Context.** All three advertise 256k tokens; Artificial Analysis gives 256k on its comparison pages and 260k in its
  model-page summaries, and OpenRouter 262,144. Small 4 reaches it by YaRN scaling from an 8k base [vllm-small-4-recipe].
  Mistral's technical documentation for Large 3 and Small 4 gives 256k tokens as the maximum size of both text input and
  text output, so no separate output cap is published [mistral-td-large-3, mistral-td-small-4].
- **Images.** All three take image and text input and return text. Large 3's card asks for aspect ratios close to 1:1 and says it
  trails vision-first models. The vision page of the docs lists Large 3, Medium 3.1, Small 3.2 and Ministral 3, which predates
  Medium 3.5 and Small 4, so rely on the model pages and cards for those [hf-large-3, mistral-vision-docs].
- **Licences.** Large 3 and Small 4 are Apache-2.0. Medium 3.5 is a modified MIT licence: free for commercial and
  non-commercial use, but its rights do not apply where the user's company (or employer) had global consolidated revenue
  above $20 million in the preceding month; such users can ask Mistral for a commercial licence or use Mistral's hosted
  services. The condition extends to derivatives [mistral-medium-license].
- **Aliases move.** `mistral-medium-latest` and other aliases can switch to a newer model and change price silently
  [mistral-lifecycle].

## Open questions

- Whether Mistral will publish a system card or any safety evaluation for these models.
- Which benchmark numbers Mistral measured for Large 3, whose card has only charts.
- Whether Medium 3.5 is generally available or in public preview: the docs page says GA and the governance hub lists it as
  active, while the 2026-05-22 launch post calls it public preview.
- The default `reasoning_effort` on the API when the parameter is omitted for Small 4 and Medium 3.5.
- A maximum output length separate from the context window for any of the three.
- Whether Large 3 will get its announced reasoning version.

## Sources

Read on 2026-10-03. Kinds: L lab, M independent measurement, A practitioner or press.

- [mistral-models-overview] Models overview, including the deprecation table. L. https://docs.mistral.ai/getting-started/models/models_overview/
- [mistral-deprecations] Deprecated and retired models (a section of the overview). L. https://docs.mistral.ai/getting-started/models/models_overview/
- [mistral-changelog] Changelog. L. https://docs.mistral.ai/getting-started/changelog
- [mistral-lifecycle] Model lifecycle policy. L. https://docs.mistral.ai/inference/model-lifecycle
- [mistral-medium-docs] Mistral Medium 3.5 model page. L. https://docs.mistral.ai/models/mistral-medium-3-5-26-04
- [mistral-small-docs] Mistral Small 4 model page. L. https://docs.mistral.ai/models/mistral-small-4-0-26-03
- [mistral-large-docs] Mistral Large 3 model page. L. https://docs.mistral.ai/models/mistral-large-3-25-12
- [mistral-chat-api] Chat completions API reference. L. https://docs.mistral.ai/api/endpoint/chat
- [mistral-reasoning-docs] Reasoning. L. https://docs.mistral.ai/capabilities/reasoning/
- [mistral-function-calling-docs] Function calling. L. https://docs.mistral.ai/capabilities/function_calling/
- [mistral-structured-docs] Structured output, custom schemas and JSON mode. L. https://docs.mistral.ai/capabilities/structured_output/custom/ and https://docs.mistral.ai/capabilities/structured_output/json_mode/
- [mistral-prompting-docs] Prompting capabilities. L. https://docs.mistral.ai/capabilities/completion/prompting_capabilities/
- [mistral-sampling-docs] Sampling. L. https://docs.mistral.ai/capabilities/completion/sampling/
- [mistral-vision-docs] Vision. L. https://docs.mistral.ai/capabilities/vision/
- [mistral-batch-docs] Batch. L. https://docs.mistral.ai/capabilities/batch/
- [mistral-guardrailing-docs] Moderation and guardrailing. L. https://docs.mistral.ai/capabilities/guardrailing/
- [mistral-azure-docs] Azure deployment page. L. https://docs.mistral.ai/models/deployment/cloud-deployments/azure
- [mistral-bedrock-docs] Amazon Bedrock deployment page. L. https://docs.mistral.ai/inference/deployment/cloud-deployments/amazon_bedrock
- [mistral-vertex-docs] Vertex AI deployment page. L. https://docs.mistral.ai/models/deployment/cloud-deployments/vertex
- [mistral-governance-models] AI governance hub, models list. L. https://legal.mistral.ai/ai-governance/models
- [mistral-governance-medium-3] AI governance hub, Medium 3 family page. L. https://legal.mistral.ai/ai-governance/models/mistral-medium-3
- [mistral-td-large-3] Mistral Large 3 technical documentation for downstream providers, 2025-12-02. L. https://legal.mistral.ai/documents/Mistral%20Large%203%20-%20Technical%20Documentation%20for%20Downstream%20Providers.pdf
- [mistral-td-small-4] Mistral Small 4 technical documentation for downstream providers, 2026-03-16. L. https://legal.mistral.ai/documents/For%20Dowstream%20Providers%20only%20-%20Technical%20Documentation%20Mistral%20Small%204.pdf
- [mistral-pricing] Pricing page (the page read gives general discounts; per-model rows are on the model pages). L. https://mistral.ai/pricing
- [mistral-3-post] Introducing Mistral 3, 2025-12-02. L. https://mistral.ai/news/mistral-3
- [mistral-small-post] Introducing Mistral Small 4, 2026-03-16. L. https://mistral.ai/news/mistral-small-4
- [mistral-vibe-post] Remote agents in Vibe, powered by Mistral Medium 3.5, 2026-05-22. L. https://mistral.ai/news/vibe-remote-agents-mistral-medium-3-5
- [mistral-vibe-readme] Mistral Vibe README. L. https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md
- [mistral-medium-license] Medium 3.5 licence. L. https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/blob/main/LICENSE
- [hf-large-3] Mistral Large 3 model card. L. https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512
- [hf-small-4] Mistral Small 4 model card. L. https://huggingface.co/mistralai/Mistral-Small-4-119B-2603
- [hf-medium-3-5] Mistral Medium 3.5 model card. L. https://huggingface.co/mistralai/Mistral-Medium-3.5-128B
- [system-prompts] The `SYSTEM_PROMPT.txt` files in the three model repositories. L. https://huggingface.co/mistralai/Mistral-Medium-3.5-128B/raw/main/SYSTEM_PROMPT.txt (and the Small 4 and Large 3 repositories)
- [vllm-small-4-recipe] vLLM recipe for Small 4. L. https://recipes.vllm.ai/mistralai/Mistral-Small-4-119B-2603
- [aws-large-3] AWS announcement of Large 3 on Bedrock, 2025-12-02. L. https://aws.amazon.com/about-aws/whats-new/2025/12/mistral-large-3-ministral-3-family-available-amazon-bedrock
- [aa-compare-large-small] Artificial Analysis, Large 3 against Small 4. M. https://artificialanalysis.ai/models/comparisons/mistral-large-3-vs-mistral-small-4
- [aa-compare-1-3-max-vs-medium] Artificial Analysis, Muse Spark 1.3 (max) against Medium 3.5. M. https://artificialanalysis.ai/models/comparisons/muse-spark-1-3-vs-mistral-medium-3-5
