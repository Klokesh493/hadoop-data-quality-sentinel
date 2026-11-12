# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 quality_sentinel.py sample_partitions.csv
pass: user_events/2026-07-17 score=96
block: app_sessions/2026-07-17 score=6
review: purchase_events/2026-07-17 score=72
test_blocks_low_quality_partition (test_quality_sentinel.QualitySentinelTest) ... ok
test_reports_each_partition (test_quality_sentinel.QualitySentinelTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
````
