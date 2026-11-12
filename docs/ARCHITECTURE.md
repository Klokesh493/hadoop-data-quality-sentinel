# Hadoop Data Quality Sentinel architecture

Scores Hadoop table partitions before downstream ML pipelines consume them.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
