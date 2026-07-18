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
