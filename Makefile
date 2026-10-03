# Targets for the research repository. Python 3.10 or later, standard library only.
PYTHON ?= python3
ROOTS ?=
CHECK_FLAGS ?=

.PHONY: check render collect test

# Every check, then the stale and scope lists (printed, not gated). While stubs remain, pass
# CHECK_FLAGS=--allow-pending to report the placeholder as UNVERIFIED instead of FAIL.
check:
	$(PYTHON) scripts/check.py $(CHECK_FLAGS)

# Rebuild the generated parts: the card blocks, the model and provider tables, the tier placements.
render:
	$(PYTHON) scripts/render.py

# Queue findings from the inboxes under ROOTS, for example: make collect ROOTS="../a ../b"
collect:
	@test -n "$(ROOTS)" || { echo "name the directories to search: make collect ROOTS=\"<dir> ...\""; exit 2; }
	$(PYTHON) scripts/collect.py $(foreach root,$(ROOTS),--root $(root))

test:
	$(PYTHON) -m unittest discover -s tests -t .
