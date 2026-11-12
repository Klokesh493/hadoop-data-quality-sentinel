# Hadoop Data Quality Sentinel

Scores Hadoop table partitions before downstream ML pipelines consume them.

Focus: Hadoop, data quality, feature pipelines, SRE release gates.

Portfolio framing: Apple-scale client-style data platform project using synthetic data only.

## Run

```bash
python3 quality_sentinel.py sample_partitions.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Business problem

A malformed or incomplete Hadoop partition can propagate defects into training and reporting. Reviewers need a gate before consuming it.

## Project walkthrough

```mermaid
flowchart LR
    A["Hadoop partition quality export"]
    B["Deduct penalties for nulls, late files, and schema errors"]
    C["Compare partition score to gate thresholds"]
    D["Block or review low scores"]
    E["Pass score of at least 85"]
    A --> B --> C
    C --> D
    C --> E
```

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 quality_sentinel.py sample_partitions.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.

## Development and security

See the [developer setup, tool roles, and security checks](docs/DEVELOPMENT.md).

[Local check results](reports/devsecops.md)

## Runbook

[Run, verify, and troubleshoot this project](docs/RUNBOOK.md)
