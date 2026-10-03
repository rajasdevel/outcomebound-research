# Model card and model file format

This page is the reference for the files in `models/`. Use it when you add or change a card, a model
file or a maker README.

Each model that a person can select has three things in `models/<maker>/`, side by side:

- `<model-id>.json`, its card. The card is data in one uniform shape, and `scripts/check.py` checks
  it key by key.
- `<model-id>.md`, its model file. The model file says in prose how to instruct the model, what its
  system card reports, how it behaves in practice and how it scores.
- A block at the top of the model file. `make render` generates the block from the card, so each
  number is written once.

Each maker folder also has a `README.md`. It holds what is true across the models of that maker.

The tables of every model and every provider are generated. `scripts/check.py` enforces everything on
this page that a machine can check. To change a number, change the card and run `make render`.

All files in `models/` belong to the neutral base. They state facts and advice about the outside
world for any use of the models. They follow the base rules in [CONVENTIONS.md](../CONVENTIONS.md):

- no downstream vocabulary;
- no project that uses this repository, except to cite its public evaluation record as the source of
  an own result (O);
- no person, client or employer;
- advice only as what a named source says or what was observed.

A judgement that is built on them for one use is an application, in
[../applications/](../applications/README.md).

## Rules for a card

- Every key is present in every card. If you cannot find a value, set it to `null` (or `[]`). Then
  name the key in `unknown` with the reason, for example "max_output: not published by the maker".
  `retires` and `voice` need no entry when they are `null`: no retirement is announced, and a text model
  has no voice. If a price is `null`, `unknown` also needs an entry that starts with
  `pricing_usd_per_mtok`.
- Write all text in your own words. A verbatim quote appears only in `sources[].quote`. It has at
  most 25 words, and you use it only where a number or a claim needs it.
- Every number has a source in `sources`, with the date you read it. Prefer primary sources: the
  maker's model page, pricing page, model card or system card, and the API documentation. Prefer
  independent measurers. A number from a third-party reseller is class A.
- An id in square brackets in the text of a card, such as `[scale-swe-pro-v2]`, is a source id of the
  card or an evidence id in [../_evidence/](../_evidence/). If you use a ledger id, also give its URL
  in `sources`.
- One card describes one distinct model. Effort levels are inside the card. They are not separate
  cards. Size variants of an open-weight family are separate models, and each has its own card and
  file.
- Keep two generations of each model class, and nothing older: the current generation and the one
  before it. The current generation is generally available, or in public preview, on the `checked`
  date of the card. A model class is a maker's line of models, such as Claude Opus, GPT Sol, Gemini
  Flash, Qwen Max, Grok or Kimi K. The `class` key names the class without the generation. The
  `generation` key holds the generation. When a new generation ships, remove the oldest card of that
  class and its model file. `make check` prints each class that holds more than two generations. It
  does not fail on them.

## Keys of a card

| Key | Value |
| --- | --- |
| `id` | The API id of the maker where one exists, else a slug. It equals the file name without `.json` |
| `name`, `maker`, `family` | Text |
| `class` | The model class, as described above, without its generation |
| `generation` | The generation of that class, as the maker numbers it, as text. `null` where the maker numbers none |
| `released` | The ISO date of general or first public availability, or `null` |
| `status` | `ga`, `preview`, `deprecated` or `retiring` |
| `retires` | An ISO date, or `null` |
| `weights` | `"closed"` or `"open (<licence>)"` |
| `access` | A list of where the model is served: APIs, clouds and harnesses |
| `context_window`, `max_output` | Tokens, as positive integers, or `null` |
| `modalities` | `{"input": [...], "output": [...]}` |
| `voice` | `null` for a text model. For a voice model, an object. See the next table |
| `reasoning` | `control` is `effort`, `budget`, `toggle`, `always-on` or `none`. `levels` lists the levels from lowest to highest, and it is required for `effort`. `default` is one of the levels, or `null` |
| `pricing_usd_per_mtok` | `input`, `output` and `cached_input` as numbers or `null`, and `notes` as text or `null` |
| `benchmarks` | A list of objects. See the next table |
| `prompting_guides` | A list of URLs: the prompting guides and best-practice pages of the maker that cover this model |
| `system_card` | The URL of the system card or model card of the maker for this model, or `null` |
| `model_page` | The URL of the page of the maker for this model (documentation or release page), or `null` |
| `sources` | A list of `{id, url, read, kind, quote}`. See the next table |
| `checked` | The ISO date on which the whole card was last verified |
| `unknown` | A list of what you could not find. Each entry starts with the key name |

`weights`, `modalities`, `reasoning` and `pricing_usd_per_mtok` can also be `null` as a whole. Name them
in `unknown`, like any other empty key.

A voice model is a model that takes speech in and gives speech out, or a speech synthesis or
transcription model of a maker. Its `voice` object has exactly these keys. Each value can be `null`
(or `[]` for `languages`). Then `unknown` needs an entry that starts with `voice.<key>`, for example
"voice.latency: the maker publishes no figure".

| Key | Value |
| --- | --- |
| `duplex` | `full` (the model can listen and speak at the same time), `half` (it takes turns) or `none` (it does not hold a conversation, as a synthesis or transcription model) |
| `input_audio`, `output_audio` | Text: the audio formats and sample rates the model takes and gives |
| `voices` | A positive integer (the number of voices) or text, for example "custom cloning" |
| `languages` | A list of text |
| `turn_detection` | Text: what the API offers to find the end of a user turn |
| `interruption` | Text: whether and how the user can cut in on the model (barge-in) |
| `latency` | Text: the figures the maker or a measurer publishes, each with its source id. `null` when there are none |
| `session_limit` | Text: the longest session the API allows |

A price that is not per token (per character, per minute) goes in `pricing_usd_per_mtok.notes`. Set
`input` and `output` to `null`, and add an `unknown` entry that starts with `pricing_usd_per_mtok` and
says the unit differs. The generated block shows the notes in the price row of a voice card. The
generated block also shows each `voice` value in a row of its own, and the models table has a `Voice`
column.

A benchmark object has exactly these keys:

| Key | Value |
| --- | --- |
| `name` | The benchmark, with its version, subset or variant. Results that differ in these are not comparable |
| `score` | A number |
| `setting`, `harness` | How the run was set up, and which harness ran it |
| `measured_by` | `independent`, `maker` or `third-party-vendor` |
| `source` | A source id of the card |
| `read` | The ISO date on which you read the result |

The generated block shows the key benchmarks first, then the others. Each one has its qualifiers and a
link to its source.

A source object has exactly these keys:

| Key | Value |
| --- | --- |
| `id` | A name that is unique in the card |
| `url` | An http(s) address |
| `read` | The ISO date on which you read it |
| `kind` | `M` (independent measurement), `L` (lab or vendor), `P` (prior art or standard) or `A` (practitioner). These letters follow the evidence classes of [CONVENTIONS.md](../CONVENTIONS.md), except that `P` has the meaning given here |
| `quote` | `null`, or at most 25 words |

Try these benchmarks for every model:

- SWE-Bench Pro (Scale, public V2)
- Terminal-Bench 4.0
- the Artificial Analysis Intelligence Index
- the Artificial Analysis Coding Agent Index
- the METR 50% time horizon

Each one needs an entry in `benchmarks` or an entry in `unknown`. The name of the entry starts with
`SWE-Bench Pro`, `Terminal-Bench`, `Artificial Analysis Intelligence Index`,
`Artificial Analysis Coding Agent Index` or `METR`. `scripts/check.py` fails a card that has neither
entry for one of them. Other benchmarks can follow.

## The model file

The file opens with the frontmatter that [CONVENTIONS.md](../CONVENTIONS.md) describes
(`last_checked`, `volatility` and `sources`). Then it has a `# <Name>` title and the headings below.
Every heading is present and in this order. If a section has nothing known, say so in one line and
say why, for example that the maker publishes no system card. `scripts/check.py` fails a file that
lacks a heading or holds one out of order. A file can add headings of its own below these.

```text
# <Name>
Two to four sentences: what the model is, its class and generation, what it is for, what it replaced.

## At a glance
(The block between the card markers, generated from the card by `make render`. Never edit it.)

## How to instruct it
### Setting up the prompt
System prompt and role, how literally the model follows instructions and how far it infers, the
structure the maker recommends (XML tags, Markdown), examples, where long documents go.
### Reasoning and effort
The control, what each level is for, whether thinking is visible, budgets, interleaved thinking,
and what not to do (for example step-by-step prompting on a model that already reasons).
### Output: format, length, tone
Verbosity controls, formatting defaults, prefill, how the model stops.
### Tools and agents
Tool definitions, parallel calls, tool choice, persistence and long-horizon work, context
management, subagents, computer use.
### Coding
What the maker advises for coding and agentic coding; notes about harnesses.
### Long context and retrieval
The limits that matter, where to place material, caching, degradation.
### Structured output
JSON mode, schemas, strict tool calls.
### Images, audio, other inputs
Where the model takes them.
### Sampling and API parameters
Temperature and the rest; which are fixed or ignored on a reasoning model.
### Migrating from the previous generation
What changed that breaks or shifts an existing prompt.

## What the system card reports
What the card measures; the safety and alignment findings that change how the model is deployed
(refusal and over-refusal, reward hacking, test special-casing, sycophancy, deception or
sandbagging, agentic safety and prompt injection, cyber and biology policies and the classifiers
that can stop a request); the safeguards the maker names. Our words, the card's numbers.

## Behaviour observed in practice
Independent and practitioner observations, each with its evidence class and source id.

## Benchmarks
Independent measurements first; the maker's own marked as such; every qualifier kept.

## Open questions
What no source settles yet.

## Sources
Every source id used above, with its URL, kind (M, L, P, A, S, F or O) and read date.
```

A model file whose card lists `audio` in `modalities.output` has one more subsection under "How to
instruct it", right after "Images, audio, other inputs". Its heading is
`### Voice: turn-taking, interruption and speech style`. It holds instructions for speech: pacing,
tone, fillers, interruptions, the turn detection settings, and what the realtime or voice guide of
the maker advises. `scripts/check.py` fails an audio-output model file that lacks it or holds it out
of place. It also fails a model file that has it when the card lists no audio output.

Depth: a reader must be able to write a system prompt, choose an effort, wire tools or migrate a
prompt for this model. The reader learns from the model file what the guide and the system card of the
maker say, in our words, without opening them. Where a maker publishes one guide for a whole family,
the maker README holds it. Each model file then says what differs for that model and links up. It does
not repeat the README.

## The maker README

`models/<maker>/README.md` has the frontmatter, a `# <Maker>` title with a short introduction, and the
headings below. All headings are required, and they come in this order.

```text
## Models and lineage
The model classes, what replaced what, and which models are in scope.
## API surface
The maker's own API: protocol, model ids, SDKs, what is shared by every model.
## Prompting guides
The maker's guides, what each covers, and how the advice has moved from release to release.
## System-card practice
What the maker publishes for a release and how to read it.
## Family-wide behaviour
Behaviour and API rules that hold for every model of the maker.
## Open questions
## Sources
```

## Example card

```json
{
  "id": "example-model-1",
  "name": "Example Model 1",
  "maker": "Example Lab",
  "family": "Example",
  "class": "Example Pro",
  "generation": "1",
  "released": "2026-09-01",
  "status": "ga",
  "retires": null,
  "weights": "closed",
  "access": ["Example API", "Example CLI"],
  "context_window": 1000000,
  "max_output": 128000,
  "modalities": {"input": ["text", "image"], "output": ["text"]},
  "voice": null,
  "reasoning": {"control": "effort", "levels": ["low", "medium", "high"], "default": "medium"},
  "pricing_usd_per_mtok": {"input": 5.0, "output": 25.0, "cached_input": 0.5, "notes": "list price, standard tier"},
  "benchmarks": [
    {"name": "SWE-Bench Pro (Scale, public V2)", "score": 70.0, "setting": "high", "harness": "Example CLI",
     "measured_by": "independent", "source": "scale-swe-pro-v2", "read": "2026-10-03"}
  ],
  "prompting_guides": ["https://example.com/prompting"],
  "system_card": "https://example.com/system-card",
  "model_page": null,
  "sources": [
    {"id": "scale-swe-pro-v2", "url": "https://example.com/leaderboard", "read": "2026-10-03", "kind": "M", "quote": null}
  ],
  "checked": "2026-10-03",
  "unknown": [
    "model_page: none found in the sources this card cites",
    "METR 50% time horizon: no independent run",
    "Terminal-Bench 4.0: no independent run",
    "Artificial Analysis Intelligence Index: not yet listed",
    "Artificial Analysis Coding Agent Index: not yet listed"
  ]
}
```
