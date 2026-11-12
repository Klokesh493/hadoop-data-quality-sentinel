# Hadoop Data Quality Sentinel walkthrough

## Business problem

A malformed or incomplete Hadoop partition can propagate defects into training and reporting. Reviewers need a gate before consuming it.

## Reproduce the workflow

Run `python3 quality_sentinel.py sample_partitions.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
pass: user_events/2026-07-17 score=96
block: app_sessions/2026-07-17 score=6
review: purchase_events/2026-07-17 score=72
```

The sample supplies these fields. `table`, `partition_date`, `null_rate`, `late_files`, `schema_errors`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
