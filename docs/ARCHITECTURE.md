# Hadoop Data Quality Sentinel architecture

Scores Hadoop table partitions before downstream ML pipelines consume them.

```mermaid
flowchart LR
    N0["sample_partitions.csv"]
    N1["quality_sentinel.py"]
    N2["quality score / gate / partition report"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
