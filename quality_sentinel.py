import csv
import sys


def quality_score(row):
    score = 100
    score -= float(row["null_rate"]) * 400
    score -= int(row["late_files"]) * 8
    score -= int(row["schema_errors"]) * 30
    return max(round(score), 0)


def gate(row):
    score = quality_score(row)
    if score < 70:
        return "block"
    if score < 85:
        return "review"
    return "pass"


def partition_report(rows):
    return [
        {"table": row["table"], "partition_date": row["partition_date"], "score": quality_score(row), "gate": gate(row)}
        for row in rows
    ]


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for item in partition_report(csv.DictReader(handle)):
            print(f'{item["gate"]}: {item["table"]}/{item["partition_date"]} score={item["score"]}')


if __name__ == "__main__":
    main(sys.argv[1])
