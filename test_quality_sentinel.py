import unittest

from quality_sentinel import gate, partition_report


class QualitySentinelTest(unittest.TestCase):
    def test_blocks_low_quality_partition(self):
        row = {"null_rate": "0.08", "late_files": "4", "schema_errors": "1"}
        self.assertEqual(gate(row), "block")

    def test_reports_each_partition(self):
        rows = [{"table": "t", "partition_date": "2026-07-17", "null_rate": "0", "late_files": "0", "schema_errors": "0"}]
        self.assertEqual(partition_report(rows)[0]["gate"], "pass")


if __name__ == "__main__":
    unittest.main()
