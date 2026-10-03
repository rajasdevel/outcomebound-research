# Security policy

This repository holds research text, three scripts (`check.py`, `render.py` and `collect.py`) and
two helper modules that they share (`layout.py` and `safefs.py`). The scripts use only the Python
standard library. Agents read the text. For this reason, four kinds of problem are security
problems here: an instruction hidden in the text, a leaked private name, a flaw in a script and a
weakness in the workflow.

## What to report privately

- **An instruction hidden in the text.** Research text is data for agents. It describes the outside
  world. Sometimes it says what to do about a research subject, such as how to write an instruction
  file or how to size a task. Then it names a source or a measurement. It never tells the model or
  agent that reads it what to do about that reader's own work. Report text that does this and asks
  the reader to act beyond the research question. The act can be to ignore or change its
  instructions, to run a command, to visit an address, to reveal something or to stay silent. Report
  hidden text too: zero-width, bidirectional-control and other invisible characters, text in a comment
  or an unrendered element, and an encoded payload.
- **A leaked private name or secret.** This is the private name of a person, a client or a project,
  an internal address, a credential, or any other data that must not be public. It can be in a
  document, a ledger record, a card, an inbox file or the history.
- **A flaw in a script.** A script in `scripts/` is at fault if it does one of these things:
  - It writes outside this repository.
  - It reads outside the directories it was given. The one intended read outside them is the
    optional local scrub list, which is only read and whose terms are never printed.
  - It follows a symbolic link out of them when it writes, or when `collect.py` reads an inbox file.
    `check.py` fails on a committed symbolic link (its `symlinks` check), and its scrub, placeholder
    and invisible-character checks do not read through one. Its other checks and `render.py` read the
    repository's own files without a test for links, so a link that `make check` misses is a report
    too.
  - It runs something it read.
  - It lets a hostile inbox file reach `ingest/queue/` without the scrub.

  The scripts never run in a consumer. A project that runs them runs its own copy.
- **A weakness in the workflow** `.github/workflows/check.yml`. Examples are a permission wider than
  `contents: read` and an action that is not pinned.

## How to report

Report privately through GitHub. On the repository's **Security** tab, choose **Report a
vulnerability** (<https://github.com/rajasdevel/outcomebound-research/security/advisories/new>). The
report, and the work on a fix, stay between you and the maintainer until an advisory is published.

A report is easy to act on when it gives these facts:

- the path and the line;
- what a reader would do;
- what it exposes.

Do not open a public issue, pull request or discussion about it. Do not publish a reproduction before
the fix. Keep real credentials and private data out of the report. Say where they are.

## What happens next

The maintainer reads reports as time allows and sets no fixed response time. A fix removes the text
from the current version. Git history cannot be erased. If a name or a secret leaked, the
owner must also rotate or rename what leaked.

## What is not a security report

A wrong fact, a stale date or a broken link is an ordinary correction. Use the
[finding issue form](https://github.com/rajasdevel/outcomebound-research/issues/new?template=finding.yml).
[CONTRIBUTING.md](CONTRIBUTING.md) says how.

## Supported versions

This repository has no releases and no tags. The current `main` branch is the only supported version.

## How the scripts treat a finding from a project

This section tells you what the scripts already guard against, so that you can judge a report.
[CONVENTIONS.md](CONVENTIONS.md) describes the queue.

`scripts/collect.py` refuses each of these:

- a symbolic link;
- a file over 16 KiB;
- a file that is not UTF-8 JSON of the finding format (the field rules are in
  [CONTRIBUTING.md](CONTRIBUTING.md));
- text with a control or invisible character, or an unpaired surrogate;
- a URL that it cannot parse, or that has a user name or password;
- anything that the optional local scrub list matches (the list is never stored in this repository).

One refused file does not stop the others.

The scripts write only inside this repository. `scripts/render.py` and `scripts/collect.py` refuse a
symbolic link at a destination file or at any folder above it. They open each step without following
a link. They never overwrite a queue file that holds other text. A person reads each queued finding
before any model does, and a finding is data at every step.
