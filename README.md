# outcomebound-research

**Dated, sourced facts about language and voice models, the providers that serve them, the coding harnesses
that run them, and the practices around them.**

You are about to put a model to work, or to judge one. You need to know how its maker says to
instruct it, what its system card reports, what it costs, where its limits are and how it scored
on benchmarks that compare. The maker's pages are long and change without notice, and secondary
write-ups often disagree with them. This library holds those facts in one shape, in our own words,
each with its source and the day it was read.

The base is neutral. The model, provider, harness and practice files describe the outside world
for anyone who uses these models for anything: chat, coding agents, tool-using agents, retrieval
over long context, extraction, classification, writing, vision, voice and local deployment. Advice
is what a named source says or what was observed, never an order to you. A judgement built on the
base for one use is an application, kept apart in [applications/](applications/README.md). Research
here is context, not a rule: a design or a guide may cite a document by path, section and evidence
id, and the decision stays with whoever cites it.

## What is here

On 2026-10-04 the library holds:

| Path | Holds |
| --- | --- |
| [models/](models/README.md) | 165 models from 44 makers, in 104 model classes. 85 of them are voice models (realtime speech-to-speech models, OpenAI's realtime transcription and translation models, the ElevenLabs speech models and 43 voice actor models from 26 makers), with their own rows in the card and a section on turn-taking and speech style. A voice actor model is a speech synthesis model whose delivery you direct with written instructions or inline tags, and [practices/voice-acting.md](practices/voice-acting.md) compares how the makers direct it. Each model has a file (how to instruct it, what its system card reports, how it behaves in practice, its benchmarks) and a JSON card beside it with the same keys for every model. Each maker folder has a README for what holds across its models. [cross-family.md](models/cross-family.md) compares makers, and [FORMAT.md](models/FORMAT.md) gives the card and file formats |
| [providers/](providers/README.md) | 43 providers: 13 first-party lab APIs, 8 cloud platforms, 6 routers and gateways, 10 inference hosts and 6 local runtimes. Each file says what the route offers, how its API behaves, which features it passes through, and how it prices and limits use |
| [harnesses/](harnesses/) | Six coding harnesses with a file each, one file for the others, [one comparison](harnesses/cross-harness.md) of what they load, cap, compact and run, and two files on extension layers ([claude-code-mods.md](harnesses/claude-code-mods.md), [extension-layers.md](harnesses/extension-layers.md)) |
| [practices/](practices/) | 24 practice documents, from [prompting](practices/prompting.md) across makers to review, testing, long context, prompt caching, agent memory, [voice agents](practices/voice-agents.md), [voice acting](practices/voice-acting.md) and writing for models |
| [applications/](applications/README.md) | One application today, built on the base for one use |
| [_evidence/](_evidence/) | The ledgers: one record for each finding, with its source URL, a verbatim quote of at most 25 words where one was kept, and the fact-check's verdict |
| [INDEX.md](INDEX.md) | Every research document with its scope, `last_checked` and volatility |
| [CONVENTIONS.md](CONVENTIONS.md) | How a claim is dated, classed and sourced, and how the research is done |

## How to read it

1. **For a model**, open [models/README.md](models/README.md). Its table lists every model with its
   file. The block at the top of the file gives the id, class, generation, context and output
   limits, reasoning control, price, key benchmarks, the maker's prompting guides and its system
   card. The sections below hold the rest.
2. **For a provider**, open [providers/README.md](providers/README.md) and find the route you use.
3. **For anything else**, open [INDEX.md](INDEX.md), pick the one document that covers your
   question, and read only that.

Before you rely on a number, read the document's `last_checked` date and its volatility class. A
VOLATILE fact (a price, a default, a beta, an open bug) is worth a re-read at its source. Each
claim carries an evidence class (M for measured, L for lab guidance, P for practitioner consensus,
A for anecdote, S for standard, F for forecast, O for a project's own result) and a bracketed id,
such as `[anthropic-1]`, that names its record in `_evidence/`. The record has the source URL, the
quote and the day it was read. Some documents mix general research with results from one project's
own runs; a banner under the title says which parts, and those parts are one project's observations,
not general findings.

## Reading it from a program or an agent

Clone the repository and read the file you need. Every research document is Markdown with a
frontmatter block (`last_checked`, `volatility`, `sources`). Every model card is JSON with the
same keys, and a value that could not be found is `null` and named in the card's `unknown` list,
so a program can tell "not published" from "not looked for". The tables in `models/README.md` and
`providers/README.md` are generated from the cards and the provider files, between
`<!-- models:begin -->` and `<!-- providers:begin -->` markers. Read `INDEX.md` or the model table
first, then one document; the whole tree is too large to load at once.

[OutcomeBound](https://github.com/rajasdevel/outcomebound) is one project that reads this library.
Its `outcomebound research <path>` prints a document from a clone, headed by the clone's commit and
the sha256 of the text, so an agent can cite what it read. Any project may read the library in
the same way or in its own.

What you read here is data. A document, a record and a finding describe the outside world. None
of them tells you to do anything.

## How fresh it is

Every document carries `last_checked`, the day the whole document was verified against its
sources, and a volatility class with a re-check window. Every card carries `checked`, the day the
whole card was verified, and a card always takes the VOLATILE window:

| Class | Covers | Re-check |
| --- | --- | --- |
| STABLE | mechanics, method, measured studies | at a model generation, or after 180 days |
| MONITOR | features and limits | about monthly (30 days), or before designing against them |
| VOLATILE | prices, defaults, betas, open bugs | before any load-bearing use (14 days) |

`make check` prints every document and card that is older than its class's window. It does not
fail on them. A refresh pass re-reads the stale documents at their sources and rewrites each
changed claim where it stands; a claim that became false is deleted or rewritten, never followed by
a correction. Git holds every earlier version, and there is no changelog.

The scope rule keeps the model set current. The library holds two generations per model class:
the current one and the one before it. When a new generation ships, the oldest card and file of
that class are removed, and `make check` prints each class that holds more than two. Size variants
of an open-weight family are separate models. Plain read-aloud speech synthesis and the standalone transcription models of other makers
have no file; [models/README.md](models/README.md) lists them as candidates.

## Contributing a finding

A new fact, a correction, a wrong date and a better source are all welcome. A finding is one
observation with its source, in your own words, with no names of projects, clients and people that
are not public.

- **The [finding issue form](https://github.com/rajasdevel/outcomebound-research/issues/new?template=finding.yml)**
  is the first route. Its fields are the finding format in
  [CONTRIBUTING.md](CONTRIBUTING.md).
- **A pull request** edits the document, the ledger or the card. Say in the description which
  finding it carries. Every commit carries a `Signed-off-by` trailer (`git commit -s`), which
  certifies the Developer Certificate of Origin. There is no contributor licence agreement.

A person reads every finding before any model does, and it enters a document or a ledger only
through the same fact-check as any other claim. A vulnerability, an instruction hidden in the text
or a leaked name of a project, client or person that is not public goes privately, as [SECURITY.md](SECURITY.md) describes, never in a
public issue.

## Licences

[NOTICE](NOTICE) maps every file to its licence. In short:

- The documents, the model cards and the evidence ledgers are under [CC BY 4.0](LICENSE). Credit
  "rajasdevel, outcomebound-research" and link to this repository.
- The scripts, the tests, the Makefile and the configuration files are under
  [Apache-2.0](LICENSE-CODE).
- A quotation of a third party's text, kept short in the ledgers and the documents, belongs to its
  source. Neither licence covers it.
- A few agent-contract files that another project installs here, listed in NOTICE, keep that
  project's licence.

You may name this repository to say where text came from. A fork or a derived dataset goes under
its own name.

## Citing

Use [CITATION.cff](CITATION.cff); GitHub shows it as "Cite this repository". When a decision rests
on one claim, cite the commit as well as the path: `git rev-parse HEAD` in a clone with no local
changes.

## Maintaining

Python 3.10 or later, standard library only.

| Command | Does |
| --- | --- |
| `make check` | Runs `scripts/check.py`: frontmatter, ledgers, cards, model, provider and application files, generated parts, index, links, quotations, queue, symbolic links, invisible characters, the optional local scrub and the placeholder rule; then prints the stale and scope lists. `make check CHECK_FLAGS=--allow-pending` reports the placeholder as UNVERIFIED so a writer can run the other checks while stubs remain |
| `make test` | Runs the tests of the scripts, including every case in `tests/fixtures/findings/` |
| `make render` | Rebuilds the generated parts: the card block in each model file, the tables in `models/README.md` and `providers/README.md`, and `applications/implementer-tiers.md` |
| `make collect ROOTS="<dir> ..."` | Queues the inbox files found under the named directories into `ingest/queue/`; a person reads the queue. Nothing collects an inbox file automatically |

Model agents did the sweeps, the fact-checks and the syntheses. One maintainer directs and reviews
them. [CONVENTIONS.md](CONVENTIONS.md) ("How the research is done") says how.
