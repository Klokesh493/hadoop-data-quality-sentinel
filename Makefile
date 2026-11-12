PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) -B -m unittest discover -v
	$(PYTHON) quality_sentinel.py sample_partitions.csv

.PHONY: replay
replay:
	$(PYTHON) tools/replay_examples.py --report reports/replay.md
