# Conventions

These are the rules for how this repository's documents, evidence ledgers, model cards and model
files are written, dated and kept current. This page is for two readers. A writer uses it to write a
claim that passes review. A careful reader uses it to judge how far to trust a claim.

`scripts/check.py` enforces what a machine can check. A person or an agent enforces the rest.

The short form:

1. Date every claim, and name its source.
2. Give every claim an evidence class: M, L, P, A, S, F or O.
3. Write in your own words. Put a verbatim quotation in quotation marks, at most 25 words.
4. Put no private name in any file. Write what was observed, not who observed it.
5. Move a document's `last_checked` only when you verified the whole document again.
6. Never edit generated text. Change its source and run `make render`.

## Two layers

The **neutral base** is `models/`, `providers/`, `harnesses/`, `practices/` and `_evidence/`. It holds
facts and advice about the outside world, sourced and dated, for anyone who uses these models for
any purpose. A base file never uses the vocabulary of one downstream use. It never names a project
that uses this repository, except to cite that project's public evaluation record as the source of an
own result (O). It never names a person, a client or an employer. It states advice as what
a named source says or as what was observed. It does not give orders to the reader.

An **application** is a file in `applications/`. It builds a judgement on the base for one use, and
it names the base files that it reads ([applications/README.md](applications/README.md)). The base
never refers to an application.

## Frontmatter

Every research document opens with the block below. A research document is a Markdown file in
`models/`, `harnesses/`, `providers/`, `practices/` or `applications/`. Four navigation and format
pages carry no frontmatter: `models/README.md`, `models/FORMAT.md`, `providers/README.md` and
`applications/README.md`.

```text
---
last_checked: 2026-10-01
volatility: MONITOR (defaults, removed controls and prices changed at each release)
sources:
  - https://example.com/the-primary-source
---
```

- `last_checked` is the day on which you verified the whole document against its sources. It is an
  ISO date.
- `volatility` starts with one class and then gives the reason. If a section has a different class
  from its document, the heading of that section says so. The class sets how soon to check again:
  - **STABLE**: mechanics, method and measured studies. Check again at a model generation, or after
    180 days.
  - **MONITOR**: features and limits. Check again about monthly, or before you design against them
    (30 days).
  - **VOLATILE**: prices, defaults, betas and open bugs. Check again before any load-bearing use
    (14 days).
- `sources` lists the primary URLs that the document rests on. A line can add a read date after the
  URL.
- A provider file also has a `kind` field: `first-party lab API`, `cloud platform`,
  `router or gateway`, `inference host` or `local runtime`.
- A model file's `sources` lists the URLs that it rests on. These include the URLs that its card cites.
- A generated file, `applications/implementer-tiers.md`, carries `generated: true`. Its `last_checked`
  is the date of the oldest card, or `none` while there are no cards.

`make check` prints every document whose `last_checked` is older than the window of its class. It
does the same for every card, which has a 14-day window like VOLATILE. It does not fail on them.

## Claims, evidence classes and dates

A claim has the `last_checked` date of its document, unless it carries its own `[as-of YYYY-MM-DD]`
tag or an evidence id that dates it.

A claim that rests on one source says which. Use one of three forms:

- a bracketed id into [`_evidence/`](_evidence/), such as `[anthropic-1]`;
- a `[chk-…]` id;
- a URL with the day you read it.

Each claim also carries its evidence class:

- **M**, measured: an experiment, a benchmark or a counted observation.
- **L**, lab guidance: the documentation or guidance of a model lab or a tool vendor.
- **P**, practitioner consensus: several independent practitioners who agree.
- **A**, anecdote: one person's account.
- **S**, standard: the text of a standards body.
- **F**, forecast: a prediction. State its falsifier and its horizon.
- **O**, own result: a result observed by this library's maintainers, dated and scoped where it
  appears. Unless a claim cites a numbered entry in a public evaluation record, the record behind it
  is not published, and the claim counts as one observation. `last_checked` dates the last reading
  of the claim, not the observation. If a document mixes such results with general research, a
  banner under its title says so.

A model card marks each of its sources with a `kind` of M, L, P or A
([models/FORMAT.md](models/FORMAT.md)). M, L and A match the classes above, and A covers a
practitioner's write-up. In a card, `P` marks prior art, such as a paper or a standard. A card does
not use S, F or O.

## Own words and quotations

- Write every claim in your own words. Do not copy the prose of a source.
- A verbatim quotation is at most **25 words**. Count the tokens that whitespace separates. A
  quotation comes with the URL of its source and the day you read it. If a source needs more words,
  quote the key phrase and paraphrase the rest.
- The 25-word limit is this repository's house rule for short quotations. It is not legal clearance.
  No word count makes a quotation allowed. Whether a quotation is allowed depends on the law that
  applies and on the terms of the owner.
- The limit applies to the `quote` of every ledger record and every card source. It also applies to
  every other quotation. These are the places: the prose of a document, any text field of a ledger
  record (`claim`, `detail`, `original_claim` and the others) and any text field of a model card.
  `scripts/check.py` fails each quotation that is over the limit.
- The check finds a quotation by its quotation marks. It knows these styles: straight double,
  curly double, straight single, curly single, guillemets, low-9 double and corner brackets. An
  apostrophe inside a word does not open or close a quotation.
- A verbatim excerpt that is set as a `>` blockquote has no marks. A blockquote of more than 25 words
  fails, unless it starts with a bold label such as `> **Note.**`, as the banners do. Start a block
  with a bold label only if the text is our own. Otherwise paraphrase the excerpt. The check cannot
  see a long passage that is copied with no marks at all, so do not copy one.
- A quotation stays the text of its source. The licences of this repository do not cover it. See
  [NOTICE](NOTICE).
- No claim holds the private name of a project, a client or a person. Write what was observed, not who
  observed it.

## Evidence ledgers

[`_evidence/`](_evidence/) holds one record for each finding that the research produced. A file is
named `<YYYY-MM-DD>.jsonl`, and each line is one JSON object. A record keeps the claim as verified, a
verbatim quote, its URL, the verdict of the fact-check and its evidence class. Most records also keep
the sweep reader's note. Nobody fact-checked that note. The file `<YYYY-MM-DD>-sources.json` lists the
sources that a sweep read, and the pages that it could not read, each with what was read instead.

A record has no read date of its own. The date in the name of its file is the day on which its source
was read, unless the text of the record says otherwise. A later file that repeats the id (a
re-verification) gives the later read date.

Quotations in a record follow [NOTICE](NOTICE). The `quote` field, and any text inside quotation marks
in another field, are the words of the source. Neither licence covers them.

| Field | Meaning | Required |
| --- | --- | --- |
| `id` | The name of the record. A bracket cites it. A prefix names the sweep, the family or the topic, then a number | always |
| `kind` | `practice`, `finding`, `generation` (the release record of one model) or `family-note` | always |
| `claim` | The finding, in our words | always |
| `quote` | Verbatim from the source, at most 25 words. `null` where none was kept | every kind but `family-note` |
| `url` | The http(s) address of the source | every kind but `family-note` |
| `verification` | `supported`, or `overstated` when the fact-check rewrote the claim | every kind but `family-note` |
| `source`, `by`, `published`, `type` | The title, author, date and type of the source. The types are `lab-official`, `research-paper`, `practitioner`, `tool-docs`, `aggregator` and `standard` | where known |
| `evidence` | The class, as a word: `measured`, `lab-guidance`, `practitioner-consensus`, `anecdote`, `standards`, `forecast` or `own-result` | where known |
| `stance` | The stance of the source: `recommend`, `observe`, `contested`, `outdated-with-newer-models`, `discourage` or `forecast` | where known |
| `detail` | The sweep reader's note | optional |
| `original_claim`, `original_evidence` | The first wording or class, kept where the fact-check changed it | where changed |
| `family`, `model`, `released` | The family, model and release date of a `generation` record. `family` is also on `finding` and `family-note` records | where they apply |

An id names one finding across all the files. A later file repeats an id only to verify that finding
again. The record then keeps the same URL, and the record in the earlier file stays. `scripts/check.py`
fails an id that repeats within one file, and an id that repeats with another URL. A new sweep
continues the numbering of each prefix from the highest id in any file.

## Model cards, model files, providers and applications

`models/<maker>/<id>.json` holds one uniform card for each model that a person can select.
`models/<maker>/<id>.md` is its model file. The format of the card, the template of the model file and
the template of the maker README are in [models/FORMAT.md](models/FORMAT.md). The template of a
provider file is in [providers/README.md](providers/README.md).

`scripts/render.py` (`make render`) writes the generated text, and `scripts/check.py` verifies it:

- the card block at the top of each model file;
- the table of every model in `models/README.md`;
- the table of every provider in `providers/README.md`;
- `applications/implementer-tiers.md`, from `applications/implementer-tiers.json`.

Never edit generated text by hand.

A new file that nobody has written yet is a stub. A stub has every heading of its template, and each
section holds one placeholder line (see `scripts/layout.py`). `make check` fails while any file holds
that line, so a stub cannot ship. `python3 scripts/check.py --allow-pending` reports the placeholder
as UNVERIFIED, so the other checks run while a writer fills the stubs.

`INDEX.md` has one row for each research document, with the title, `last_checked` and volatility
that the document carries. When the `last_checked` of a document moves, move its row.

## Re-verifying and correcting

When you verify a document again, `last_checked` moves, and you rewrite every changed claim where it
stands. Delete or rewrite a claim that became false where it stands. Never add a correction after
it. A pass that checks one section marks that section `[as-of <date>]`. Only a check of the whole
document moves the `last_checked` of the document.

A URL that opens proves only that it opens. It does not prove that the claim is true. Read the source
again. A ledger record keeps its first wording in `original_claim`. Git holds every earlier version.
There is no changelog.

A published path stays where it is. When a document must move, fix every link to it in the same change.

## Findings from projects

A finding is data, not an instruction. It reaches this repository as a GitHub issue or as a pull
request. Nothing collects an inbox file automatically. `make collect` (`scripts/collect.py`) queues
the inbox files under the directories that a person names, in `ingest/queue/`.

The script writes each new finding to `ingest/queue/<YYYYMMDD>-<64 hex digits>.json`. It skips a
finding that it has already seen. Git ignores the queue folder, so a queued finding is not
committed. A person reads a finding before any model does. A finding enters a document or
a ledger in the maintainer's own words, and only through the same fact-check as any other claim. Nothing
from a project is merged unread. [CONTRIBUTING.md](CONTRIBUTING.md) gives the finding format and its
field rules. [SECURITY.md](SECURITY.md) lists what the script refuses.

## How the research is done

1. **Sweeps.** Readers work in parallel, one for each topic or model family. They read primary
   sources: lab guidance and release posts, model cards, API documentation and changelogs, harness
   documents and source code, papers, standards and practitioners. Each finding is recorded with its
   claim, a verbatim quote, the URL, the date, the type of source, an evidence class and a stance.
2. **Fact-check.** An independent pass reads every source again against its record. It gives one of
   three verdicts: supported, overstated (the claim is corrected and the first wording is kept) or
   dropped. It also checks that a cited source is its current revision, not only that it exists.
3. **Completeness.** A critic reads the first synthesis for what it missed. Each gap that the critic
   names is swept in turn.
4. **Synthesis.** The records are distilled into the documents. Each claim gets its evidence class
   and, where it matters, the models that it covers.
5. **Adversarial critique.** An independent reviewer attacks each synthesis. The synthesis is revised,
   and disputed facts are checked again at their source.

A refresh pass (steps 1 to 5 on the stale list) is a model run. It happens when the maintainer asks
for one.

Refresh a document in these cases:

- A model or harness release that the document covers changes how text is loaded, capped or followed.
- A lab publishes new prompting guidance.
- The horizon of a forecast passes. Score the forecast as held, falsified or unscored.
- The window of the document has passed.

The section "Limits and open questions" of a document names what would change it and when to look
again.
