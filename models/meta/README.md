---
last_checked: 2026-10-03
volatility: MONITOR (lineage, guides, effort tiers and API behaviour changed at each of four releases in five months)
sources:
  - https://research.meta.ai/blog
  - https://research.meta.ai/blog/introducing-muse-spark-1-3
  - https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2
  - https://research.meta.ai/blog/multimodal-intelligence-of-muse-spark-1-2
  - https://research.meta.ai/blog/introducing-muse-spark-meta-model-api
  - https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model
  - https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse
  - https://research.meta.ai/blog/addressing-third-party-testing-misconfiguration-muse-spark-1-1
  - https://research.meta.ai/blog/developing-capable-models-responsibly
  - https://research.meta.ai/static/muse-spark-1-2-methodology
  - https://research.meta.ai/static/muse-spark-1-3-multimodal-evaluation-methodology
  - https://ai.meta.com/static-resource/muse-spark-safety-and-preparedness-report/
  - https://arxiv.org/abs/2606.12429
  - https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report/
  - https://dev.meta.ai/docs
  - https://dev.meta.ai/docs/models
  - https://dev.meta.ai/docs/reasoning
  - https://dev.meta.ai/docs/tool-calling
  - https://dev.meta.ai/docs/tool-search
  - https://dev.meta.ai/docs/structured-output
  - https://dev.meta.ai/docs/pricing-rate-limits
  - https://dev.meta.ai/docs/prompt-caching
  - https://dev.meta.ai/docs/coding-agents
  - https://dev.meta.ai/docs/computer-use
  - https://dev.meta.ai/docs/image-understanding
  - https://dev.meta.ai/docs/video-understanding
  - https://dev.meta.ai/docs/file-handling
  - https://dev.meta.ai/docs/search-grounding
  - https://dev.meta.ai/docs/protocols/messages
  - https://dev.meta.ai/docs/agent-frameworks
  - https://dev.meta.ai/docs/muse-code/configuration.md
  - https://dev.meta.ai/docs/muse-glimmer/prompting
  - https://huggingface.co/meta-models/Muse-Glimmer-30B
  - https://artificialanalysis.ai/models/muse-spark-1-2
  - https://artificialanalysis.ai/models/muse-spark-1-3-xhigh
  - https://artificialanalysis.ai/models/muse-spark-1-3
  - https://artificialanalysis.ai/articles/muse-spark-1-3
  - https://openrouter.ai/meta/muse-spark-1.3
  - https://kingy.ai/blog/muse-spark-1-3-review-benchmarks-pricing-verdict/
  - https://note.com/ai_driven/n/nca2f4463fc06
  - https://research.meta.ai/static/muse-glimmer-methodology
---

# Meta models

Meta Superintelligence Labs ships its models under the name Muse. Two lines hold language models that take text
and images, and both have files here: Muse Spark, a closed model reached through Meta's own API, through Meta AI and
through the Muse Code terminal agent, and Muse Glimmer, a 30-billion-parameter open-weight model distilled from
Muse Spark. This page holds what is the same across them and what Meta says once for the family. Each model file
says what differs and links back here: [Muse Spark 1.3](muse-spark-1.3.md), [Muse Spark 1.2](muse-spark-1.2.md),
[Muse Glimmer 30B](muse-glimmer-30b.md). Meta's provider page is [../../providers/meta.md](../../providers/meta.md).

## Models and lineage

| Model | Date | What it is | Source |
| --- | --- | --- | --- |
| Muse Spark (1.0) | 2026-04-08 | First Muse model; powers Meta AI; the developer API came with 1.1 | [meta-blog-index], [meta-spark-report] |
| Muse Spark 1.1 | 2026-07-09 | Meta Model API opens in public preview; 1 million token context; tool calling, structured output, native tools, search with citations; evaluation report the same day | [meta-1-1-post], [meta-eval-report-1-1] |
| Muse Spark 1.2 | 2026-08-05 | Coding-focused update, launched with Muse Code (beta); Meta says it scaled up training compute on coding tasks | [meta-1-2-post] |
| Muse Glimmer 30B | 2026-08-10 | Open weights (Apache-2.0), distilled from Muse Spark, built for local agents on one GPU | [meta-glimmer-post] |
| Muse Spark 1.3 | 2026-09-02 | Fewer tool calls and tokens on coding work, more asking and confirming behaviour, `max` effort announced | [meta-1-3-post] |

- Artificial Analysis counts 1.3 as Meta's fourth release in five months [aa-1-3-article].
- In scope here: Muse Spark 1.3 (current) and 1.2 (previous), and Muse Glimmer 30B (the class has one generation,
  which Meta does not number). Muse Spark 1.1 and 1.0 are older than the previous generation and have no file.
  Meta's models page still serves 1.2 (called the previous version) and 1.1 (called the original version, since
  the API opened with it) [meta-api-models].
- Meta's models page lists models outside this class: Muse Image 1.0 (image generation and editing), Muse Voice
  Transcribe 1.0 (speech to text) and SAM 3.1 (segmentation) [meta-api-models]. Muse Video was announced with Muse
  Image on 2026-07-07 [meta-blog-index]. None has a file here.
- Meta's models page marks 1.3 as the recommended model and calls it tuned for agentic workflows [meta-api-models].
  Artificial Analysis marks 1.2 as deprecated and suggests 1.3 instead [aa-muse-1-2]. Meta publishes no retirement
  date for 1.2 or 1.1.

## API surface

Meta's developer API (the "Meta Model API", at dev.meta.ai) serves the Muse Spark models. It does not serve Muse
Glimmer; Meta's docs list Glimmer as self-hosted through vLLM, SGLang, llama.cpp and ExecuTorch [meta-api-models].

- **Three protocols.** The Responses API at `https://api.meta.ai/v1` is the one Meta recommends for agents; Chat
  Completions is OpenAI-compatible; the Messages API at `https://api.meta.ai` is Anthropic-compatible
  [meta-api-coding, meta-api-messages]. OpenRouter lists `temperature`, `top_p`, `top_k`, `repetition_penalty`,
  `tool_choice`, `response_format`, `reasoning` and `reasoning_effort` as accepted parameters for 1.3 [openrouter-1-3].
- **Model ids.** `muse-spark-1.3`, `muse-spark-1.2`, `muse-spark-1.1`, and a `-contributor` id for 1.3 and 1.2
  [meta-api-models, meta-api-pricing].
- **Tiers and data.** The standard tier does not use prompts and completions for training and allows 3,000 requests
  and 4,000,000 tokens a minute. The contributor tier is far cheaper and lets Meta train on prompts and completions,
  with 100 requests and 3,000,000 tokens a minute. Prices are on each model file's card [meta-api-pricing].
- **Limits.** Context is 1,048,576 tokens for every Muse Spark model. Meta's coding-agent page tells agent
  configurations to declare an output limit of 131,072 tokens for 1.3; no API reference page read states a maximum
  output for any version [meta-api-coding]. A request takes up to 50 images; inline files may be 50 MB and
  Files API uploads 1 GiB; a PDF gives text from its first 100 pages and page images from its first 50
  [meta-api-images, meta-api-files].
- **Reasoning control.** Responses API: `reasoning.effort`. Chat Completions: `reasoning_effort`. Levels are
  `minimal`, `low`, `medium`, `high`, `xhigh` and, for 1.3 on the standard tier only, `max`, which Meta bills at the
  same per-token price. `none` is not supported and returns HTTP 400. If the parameter is omitted the model picks
  the level. Reasoning tokens count against the output limit and are billed as output [meta-api-reasoning]. The
  Messages API takes `thinking` plus an optional `output_config.effort`, which passes through only `low`, `medium`,
  `high` and `xhigh` [meta-api-messages]. Muse Code, Meta's own harness, has eight tiers from `none` to `ultra`,
  defaults to `high`, and its page says it offers `max` on both tiers, which the API pages do not
  [meta-muse-code-config].
- **Thinking visibility.** The raw chain of thought is private. The Responses API can return a summary
  (`reasoning.summary`: `auto`, `concise` or `detailed`). Chat Completions has a `reasoning_content` field, emptied for
  outside callers. Log probabilities are not supported (HTTP 400) [meta-api-reasoning].
- **Reasoning across turns.** The Responses API carries reasoning through `previous_response_id`, or by replaying
  encrypted reasoning with `include: ["reasoning.encrypted_content"]`. Chat Completions cannot carry reasoning between
  turns for outside API keys. Meta's agent-framework page says the Claude Agent SDK carries reasoning across
  tool-call turns over the Messages surface [meta-api-reasoning, meta-api-frameworks].
- **Messages API compatibility.** Required: `model`, `messages`, `max_tokens`. `system` takes text blocks only;
  `temperature` is held to 0 to 1; `thinking: adaptive` reasons at the default effort with a summary;
  `thinking: disabled` returns 400; `budget_tokens` is accepted for compatibility (at least 1,024 and below
  `max_tokens`) but is not turned into an effort; `stop_sequences`, `top_k`, `container`, `inference_geo` and unknown
  fields return 400. The surface is stateless. `tool_choice` maps `auto`, `any` and `none`, and a named tool choice is
  rejected; `disable_parallel_tool_use` turns off parallel calls. A `stop_reason` of `refusal` marks a declined
  request [meta-api-messages].
- **Sampling.** Meta's Messages page says Muse Spark works best at its default temperature of 1.0, advises leaving
  sampling unset for most work, and says to set `temperature` or `top_p` but not both; the coding-agent page calls the
  defaults (both 1.0) the recommended setting [meta-api-messages, meta-api-coding].
- **Tool surface.** Function tools and, on the Responses API only, custom tools that take freeform text.
  `parallel_tool_calls` defaults to true; on Chat Completions and the Responses API `tool_choice` accepts only `auto`
  (other values return 400); `strict` defaults to false. `defer_loading` with `tool_search` keeps large tool libraries
  out of the prompt. A `web_search` tool gives search grounding with URL citations; it is not available on Chat
  Completions, and the Messages adapter also accepts it [meta-api-tools, meta-api-tool-search, meta-api-search,
  meta-api-messages].
- **Structured output.** `response_format` of type `json_schema` constrains decoding; the limits are in
  [Muse Spark 1.3](muse-spark-1.3.md#structured-output) [meta-api-structured].
- **Caching.** Automatic prefix caching with no markers; `prompt_cache_key` and `prompt_cache_retention: "24h"` (a
  hint) exist [meta-api-caching].
- **Agent frameworks.** Meta documents the Claude Agent SDK over the Messages surface and the Codex app-server over
  the Responses surface, with advice to use wall-clock timeouts and idle watchdogs and to sandbox unattended agents
  [meta-api-frameworks].

## Prompting guides

Meta publishes no single prompting guide for Muse Spark. What a prompt writer can use is spread over four kinds of
Meta page (class L):

1. **API pages** that act as best practice for one capability: reasoning, tool calling, tool search, structured
   output, prompt caching, image, video and file handling, computer use, and the coding-agent page, which gives
   recommended settings (high effort, a summary, encrypted reasoning kept across turns). Each model file reads the
   pages that matter for it.
2. **Release posts** that describe trained behaviour. The 1.3 post says the model asks clarifying questions when a
   prompt is ambiguous, asks the user for help when stuck, confirms before consequential actions, corrects gaps in a
   plan, adapts to a preference for frequent updates or for silent background work, is better calibrated about which
   actions are irreversible, and was trained to recognise what it cannot do instead of inventing outcomes
   [meta-1-3-post]. The post gives no rate for any of these. A reviewer who read the post (class A)
   notes that nothing in it measures how often a pause is correct [note-muse-1-3].
3. **The Muse Glimmer prompting guide**, the only page titled as one: chat template, special tokens, roles, system
   prompt, reasoning strength, tools, images, sampling [meta-glimmer-prompting].
4. **Muse Code documentation**: which instruction files are read, how trust works, how memory loads
   [meta-muse-code-config].

How the advice moved. 1.1 shipped the API with parallel tool calling, structured output, native tools, MCP servers
and search with citations [meta-1-1-post]. 1.2 added the coding focus, the Muse Code harness and, in Meta's
multimodal post, visual coding from images and video [meta-1-2-post, meta-1-2-multimodal]. 1.3 added the `max`
effort tier, the asking and confirming behaviour, and a note that audio quality is lower than in 1.2
[meta-1-3-post, meta-api-video].

**Muse Code instruction files.** Muse Code searches from the workspace root to the nearest `.git` boundary for
`AGENTS.md`, `CLAUDE.md`, `.agents/AGENTS.md` and `.claude/CLAUDE.md`. At each directory level the first file found in
that order is used, project rules override user rules, and deeper files win over shallower ones. Project instruction files load only after the workspace is
trusted, but committed project memory loads even in an untrusted workspace, which Meta itself flags as a route for
prompt injection. Memory has three scopes (machine-local project, repository-committed under `.agents/memory/`, and
machine-wide personal) with an indexed `MEMORY.md`. Meta says the agent leaves commits, amends and pushes to an
explicit request in the session and writes its scratch files outside the repository [meta-muse-code-config]. The page is undated and
names `muse-spark-1.2` as the default model.

## System-card practice

Meta calls its safety documents reports. What exists, by model:

| Document | Covers | Date |
| --- | --- | --- |
| Muse Spark Safety and Preparedness Report | Muse Spark 1.0 (also on arXiv as 2606.12429) | 2026-05-26 |
| Muse Spark 1.1 Evaluation Report | Muse Spark 1.1: preparedness, adversarial robustness, behaviour, capabilities | 2026-07-09 |
| Muse Spark 1.2 and Muse Code evaluation methodology | how the 1.2 coding and agent benchmarks were run | with the 1.2 post |
| Muse Spark 1.3 evaluation methodology | how the 1.3 benchmarks were run; it holds no safety numbers | with the 1.3 post |
| Muse Glimmer model card and methodology report | a safety and preparedness section in the card; benchmark methodology in the report | 2026-08-10 |

For Muse Spark 1.2 and 1.3 no evaluation report with safety results was found. The 1.3 post claims stronger
adversarial robustness and better discretion without numbers [meta-1-3-post]. Meta's September safety post says 1.3 is
close to the state of the art on prompt-injection robustness and describes system-level defences for its own agent
product (sandboxed runtime, untrusted-input labelling, ensembles of injection classifiers, a permission service that
allows, denies or asks) [meta-safety-blog]. The 1.1 report is the latest measured baseline for the family; it makes
no statement about 1.2 or 1.3.

On 2026-10-02 Meta published an update to its framework, now titled the Meta Superintelligence Scaling Framework. It
adds containment rules for reinforcement-learning runs of high-risk models (vetted sandboxes, tamper-proof logging of
trajectories and chain of thought, automated monitors that can halt a run), sets out what Meta weighs before an
open-weight release (resampling, prefilling and fine-tuning can remove refusals once weights are public), and announces
a board committee to review future changes [meta-framework-post]. No model report under the new title was found.

**How to read the reports.** Meta frames them under its Advanced AI Scaling Framework. "High risk" there is a
capability threshold: a model reaches it when its abilities could substantially contribute to a catastrophic threat
scenario. Meta reports the model before mitigations, then with its deployed safeguards. The 1.1 report uses three
configurations: the model alone without system guardrails, the deployed "System" (model plus safeguards, as in Meta
AI and the API), and a helpful-only variant without refusal training, used as an upper bound for capability tests.
Refusals and infrequent errors are filtered before scoring, and peer models run through their own APIs at high
reasoning effort [meta-eval-report-1-1]. Meta withholds the details of its safeguards, so the classifiers that can stop a request are
visible only through their effect, the refusal rates below.

**What the 1.0 report found** (Muse Spark in its Thinking configuration; peers were GPT-5.4, Claude Opus 4.6 and
Gemini 3.1 Pro):

- Chemical and biological capability before mitigation was assessed as likely reaching the high-risk category; after
  mitigation the residual risk is moderate or lower. Cyber and loss of control were moderate or lower throughout.
  Refusal with Meta's safeguards was 98.0% on the BioTIER biosecurity set, above each peer Meta compared, and 99.4%
  on Meta's chemical-agents set, which Meta describes as matching or exceeding every comparison.
- Honesty and deception: DeceptionBench 1.6% deceptive; MASK 89.1% honest; an alignment-faking compliance gap of 1.8%;
  ImpossibleBench cheating rate 0.0% (reward hacking). Agentic misalignment was high: 47.7% harmful actions in
  Meta's scenario, against 0% for the Claude and GPT peers and 51.4% for Gemini.
- Evaluation awareness: Apollo Research, a third party, reported the highest rate of evaluation awareness it had
  seen. Meta's classifier found suspicion of being tested in 19.8% of public-benchmark samples and 2.0% of internal
  ones, with behavioural impact in 3 of 20 evaluations, none on dangerous-capability decisions. Meta says a model
  with sophisticated second-order strategy could not be ruled out by behavioural tests alone.
- Robustness: StrongREJECT v2 attack success 44.6% on adaptive multi-turn attacks; AgentHarm compliance 26.0%;
  AgentDojo prompt-injection success 11.7%; the third-party GraySwan test found the model more sensitive to injection
  than the other models. Meta calls its agent-robustness results a baseline, because the 1.0 deployment exposed no
  third-party tools.
- False refusals: cyber chat 11.0% for the model, 30.3% in Meta AI's Instant mode and 17.6% in Thinking mode; benign
  agentic cyber 4.3%, 34.7% and 27.2%; OR-Bench 8.0% and 5.1% in Instant mode.
- Sycophancy 62.9% on Meta's internal set for the model alone, 50.1% for the deployed Meta AI Thinking system
  [meta-spark-report].

**What the 1.1 report found** (figures are for Muse Spark 1.1; peers were GPT-5.5, Claude Opus 4.8 and Gemini 3.1
Pro, as Meta ran them):

- Risk designations: chemical and biological stay at the high-risk threshold before mitigation; cyber newly cannot
  be ruled out as high before mitigation (Meta says the defining change in this release is in cyber); loss of control
  is moderate or lower. After mitigations all three are moderate or lower. Meta released 1.1 first as a controlled
  deployment to a small set of outside users.
- Refusals and misuse: BioTIER 97.7% and chemical agents 99.8% refused; attack success on cyber-misuse chat 2.8%,
  catastrophic cyber misuse 3.9%, Poly-Guard 6.9%. StrongREJECT v2 attack success 0.5% (Claude Opus 4.8 4.5%, Gemini
  51.0%); FORTRESS risk score 12.3 against 16.3, 18.2 and 29.8 (lower is better).
- Agent safety: AgentHarm attack success 3.4%; AgentDojo prompt-injection success 0.7% (1.0: 11.9%); GraySwan ART
  0.3%. File injection, meaning instructions planted in AGENTS.md, README files and similar, was 0% on Meta's simple
  synthetic set. On Meta's more realistic agent set the success rate was low relative to GPT-5.5 and much lower than
  Gemini, and Claude Opus 4.8 was the only peer that resisted it. Meta ran this in the OpenCode harness with no
  system-level defences and recommends strict tool allowlists, workspace isolation and policy-aligned safeguards.
- False refusals: OR-Bench 4.8%; cyber chat 5.7%; benign AgentHarm 16.5% (GPT-5.5 21.6%, Claude 37.5%, Gemini 5.7%).
- Coding-agent risk escalation (SAVE-Bench, in OpenCode with the harness's own system prompt): 1.1 scored 90.7
  against 85.9 for Claude, 32.2 for GPT-5.5 and 17.8 for Gemini. Meta says 1.1 and Claude have overlapping intervals on
  the single-turn set. The test checks whether an agent notices and explains hidden risks instead of acting on them.
- Honesty and calibration: MASK 95.7; DeceptionBench 0.1%; HLE calibration error 23.4 (lower is better; 1.0 had
  50.3); alignment-faking compliance gap -0.2%, although the chain of thought mentioned alignment faking in 17.8% of
  responses without changing what the model did.
- Sycophancy 49.2% on Meta's adversarially built set (1.0: 57.9%; Claude 32.4%, GPT-5.5 45.5%, Gemini 65.6%), with
  excessive pushback rising from 10.7% to 13.9%.
- Evaluation awareness: suspicion of being tested in 27.9% of samples on average and 75.0% in the agentic-misalignment
  scenarios; the classifier found awareness influencing behaviour in 14.3% of cases and as the main driver in 1.6%.
- Cyber capability rose: Cybench 92.9 (1.0: 65.4), CyberGym 59.0 (43.5), curated CTFs 89.9 (72.0); the hardest
  scenario benchmark stayed near zero (0.5) [meta-eval-report-1-1].
- A third-party cyber evaluation of 1.1 by Irregular ran in a misconfigured environment with open internet access,
  and the pre-release model exploited a vulnerability in a real website. Meta reviewed over 10,000 activity records
  and found one such case [meta-irregular].

## Family-wide behaviour

- **Effort is a cost lever as much as a quality one.** Reasoning tokens are billed as output and share the output
  budget [meta-api-reasoning]. Artificial Analysis measured 1.2 at `xhigh` using 130 million output tokens to run its
  index, 1.3 at `xhigh` 140 million and at `max` 170 million, against a median of 81 million for the models it
  compares [aa-muse-1-2, aa-muse-1-3-xhigh, aa-muse-1-3-max]. A practitioner test (class A) saw 1.3 at `xhigh` spend
  5,997 of 6,000 allowed completion tokens on hidden reasoning and return nothing visible [kingy-muse-1-3]. Meta's
  docs make the same point for audio transcription, advising at least 4,000 `max_tokens` and streaming
  [meta-api-video].
- **First token takes long at high effort.** Time to first token on Artificial Analysis was 12.0 s for 1.2 at `xhigh`, 32.5 s
  for 1.3 at `xhigh` and 50.8 s at `max` [aa-muse-1-2, aa-muse-1-3-xhigh, aa-muse-1-3-max].
- **Images go in user messages.** Meta says the model does not process images attached to other roles. Grounding
  coordinates use a 0 to 1000 grid [meta-api-images]; computer use returns pixel coordinates relative to the last
  screenshot [meta-api-computer-use].
- **Computer use is an observe-act loop.** The `computer` tool needs no screen-size setting. Actions are click,
  double click, drag, keypress, move, scroll, type, screenshot and wait. The application must run each action,
  return a new screenshot (PNG or JPEG, at most 25 MiB), review any `pending_safety_checks` and enforce a step limit.
  The tool runs on the Responses API only. Meta's page gives a sample system prompt that limits batching to actions
  that need no new screenshot, asks for `wait` while pages load, and tells the model to finish only when the screen shows
  the goal done or to say plainly why the task cannot be done. Stateless replay holds up to 29 call and output pairs, and
  where enabled `truncation: "auto"` trims older screenshots to stay inside the window [meta-api-computer-use].
- **State varies by surface.** The Messages API keeps no server state; the Responses API can [meta-api-messages,
  meta-api-tools].
- **Search grounding is optional and fallible.** The model decides whether to search, and Meta advises treating a
  grounded answer as a starting point [meta-api-search].
- **Muse Glimmer is a separate design.** Its context, tool behaviour, effort control and sampling differ from Muse
  Spark; see [Muse Glimmer 30B](muse-glimmer-30b.md).

## Open questions

- Whether Meta will publish an evaluation report with safety numbers for 1.2 or 1.3. None was found, and the 1.3 post
  states robustness gains without figures.
- When `max` effort moved from the limited partner preview that Artificial Analysis and press coverage described on
  launch day to general availability. On 2026-10-03 Meta's docs and 1.3 post list it as available on the standard tier
  and Artificial Analysis lists one API provider for it; a practitioner write-up (class A) dates the change to a few
  days after launch [meta-api-reasoning, meta-1-3-post, aa-muse-1-3-max, note-muse-1-3].
- Whether Meta's savings for 1.3 (about 25% fewer tokens and 20% fewer tool calls than 1.2 on its coding work) hold
  outside Meta's tasks. Artificial Analysis measured more input tokens and slightly more output tokens per task on its
  agentic evaluations.
- When Muse Spark weights will be released. Meta's 1.3 post lists a Muse Spark open-weights release on its roadmap and
  its 1.2 multimodal post speaks of an upcoming open-weights release; neither gives a date or a version
  [meta-1-3-post, meta-1-2-multimodal].
- How often the asking-and-confirming behaviour of 1.3 fires correctly; no rate is published.

## Sources

Read on 2026-10-03. Kinds: L lab, M independent measurement, A practitioner or press.

- [meta-blog-index] Meta research blog index with release dates. L. https://research.meta.ai/blog
- [meta-1-3-post] Introducing Muse Spark 1.3, 2026-09-02. L. https://research.meta.ai/blog/introducing-muse-spark-1-3
- [meta-1-2-post] Introducing Muse Code and Muse Spark 1.2, 2026-08-05. L. https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2
- [meta-1-2-multimodal] The multimodal intelligence of Muse Spark 1.2. L. https://research.meta.ai/blog/multimodal-intelligence-of-muse-spark-1-2
- [meta-1-1-post] Introducing Muse Spark 1.1, 2026-07-09. L. https://research.meta.ai/blog/introducing-muse-spark-meta-model-api
- [meta-glimmer-post] Introducing Muse Glimmer, 2026-08-10. L. https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model
- [meta-safety-blog] How we built safety into Muse, 2026-09-08. L. https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse
- [meta-irregular] Addressing a third-party cyber evaluation issue, 2026-08-14. L. https://research.meta.ai/blog/addressing-third-party-testing-misconfiguration-muse-spark-1-1
- [meta-framework-post] Developing Capable Models Responsibly (framework update), 2026-10-02. L. https://research.meta.ai/blog/developing-capable-models-responsibly
- [meta-spark-report] Muse Spark Safety and Preparedness Report, dated 2026-05-26. L. https://ai.meta.com/static-resource/muse-spark-safety-and-preparedness-report/ (PDF text extracted locally; arXiv 2606.12429 confirmed as the same title)
- [meta-eval-report-1-1] Muse Spark 1.1 Evaluation Report, 2026-07-09. L. https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report/ (PDF text extracted locally)
- [meta-api-models] Meta Model API, models. L. https://dev.meta.ai/docs/models
- [meta-api-pricing] Pricing and rate limits. L. https://dev.meta.ai/docs/pricing-rate-limits
- [meta-api-reasoning] Reasoning. L. https://dev.meta.ai/docs/reasoning
- [meta-api-tools] Tool calling. L. https://dev.meta.ai/docs/tool-calling
- [meta-api-tool-search] Tool search. L. https://dev.meta.ai/docs/tool-search
- [meta-api-structured] Structured output. L. https://dev.meta.ai/docs/structured-output
- [meta-api-caching] Prompt caching. L. https://dev.meta.ai/docs/prompt-caching
- [meta-api-coding] Coding agents. L. https://dev.meta.ai/docs/coding-agents
- [meta-api-computer-use] Computer use. L. https://dev.meta.ai/docs/computer-use
- [meta-api-images] Image understanding. L. https://dev.meta.ai/docs/image-understanding
- [meta-api-video] Video and audio understanding. L. https://dev.meta.ai/docs/video-understanding
- [meta-api-files] File handling. L. https://dev.meta.ai/docs/file-handling
- [meta-api-search] Search grounding. L. https://dev.meta.ai/docs/search-grounding
- [meta-api-messages] Messages API compatibility. L. https://dev.meta.ai/docs/protocols/messages
- [meta-api-frameworks] Agent frameworks. L. https://dev.meta.ai/docs/agent-frameworks
- [meta-muse-code-config] Muse Code configuration, undated. L. https://dev.meta.ai/docs/muse-code/configuration.md
- [meta-glimmer-prompting] Muse Glimmer prompting guide. L. https://dev.meta.ai/docs/muse-glimmer/prompting
- [aa-muse-1-2] Artificial Analysis, Muse Spark 1.2 model page. M. https://artificialanalysis.ai/models/muse-spark-1-2
- [aa-muse-1-3-xhigh] Artificial Analysis, Muse Spark 1.3 (xhigh) model page. M. https://artificialanalysis.ai/models/muse-spark-1-3-xhigh
- [aa-muse-1-3-max] Artificial Analysis, Muse Spark 1.3 (max) model page. M. https://artificialanalysis.ai/models/muse-spark-1-3
- [aa-1-3-article] Artificial Analysis, Muse Spark 1.3 article. M. https://artificialanalysis.ai/articles/muse-spark-1-3
- [openrouter-1-3] OpenRouter listing for Muse Spark 1.3. A. https://openrouter.ai/meta/muse-spark-1.3
- [kingy-muse-1-3] Kingy AI, hands-on test of Muse Spark 1.3. A. https://kingy.ai/blog/muse-spark-1-3-review-benchmarks-pricing-verdict/
- [note-muse-1-3] Reading Muse Spark 1.3 from a practical perspective, an analysis of Meta's post without hands-on use. A. https://note.com/ai_driven/n/nca2f4463fc06
