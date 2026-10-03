# Applications

An application is a judgement that is built on the base files for one use.

The base is the model files, the providers, the harnesses, the practices and the evidence ledgers. It
says what is true of the outside world, and what its sources advise, for any use. An application takes
that and decides one thing for one purpose. It names the base files that it reads. When one of those
files changes, you can see which applications to read again. A base file never refers to an
application.

Read this page if you want to know what an application is, or if you want to add one.

## The applications today

There is one.

| Application | Decides | Reads | Data |
| --- | --- | --- | --- |
| [implementer-tiers.md](implementer-tiers.md) | Which tier of OutcomeBound's hand-off an implementer sits in, by model and effort | The card of each model at `models/<maker>/<id>.json` (`name`, `reasoning.levels`), the model file beside the card, and the evidence ledgers that its notes cite | [implementer-tiers.json](implementer-tiers.json) |

## Change the data of an application

`implementer-tiers.md` is generated from `implementer-tiers.json` by `scripts/render.py`. Change the
data, then run `make render`. Never edit the Markdown file by hand.

The data has this shape:

```text
{"version": 1, "placements": {"<model-id>": {"placements": [{"effort": ..., "tier": ..., "confidence": ...}],
                                              "basis": "why, citing source ids or saying it is inferred",
                                              "notes": ["behaviour that matters to this use only"]}}}
```

- The key `<model-id>` is the id of a card. `make check` fails a key that has no card.
- A model that has no entry takes the spec tier. The matching rules in `implementer-tiers.md` call
  this the default rule.
- `make check` also fails an entry in these cases:
  - Its text cites a source id that is neither a source of the card nor a ledger id.
  - Its text holds a quotation of more than 25 words.
  - Its wording points to something that a public reader cannot reach.

## What goes in a note

A note belongs in an application when it matters to this one use. A fact or an observation about the
model that holds for every use goes in the file of the model.

## Add an application

An application is its own file in this folder. It opens with the frontmatter that
[CONVENTIONS.md](../CONVENTIONS.md) describes, and it has a row in `INDEX.md`. It states in a few
sentences what it decides, and it names the base files that it reads. Examples that may follow are
the choice of a model for a task and the sizing of a local model.
