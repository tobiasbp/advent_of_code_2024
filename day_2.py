#!/usr/bin/env python3

from pathlib import Path

# Read the data
data = Path("data/day_2_1_example.txt").read_text().splitlines()
# data = Path("data/day_2_1.txt").read_text().splitlines()


class Report:
    def __init__(self, levels: list[int]) -> None:
        # self.levels = levels
        self._is_safe = self._is_ascending(levels) or self._is_descending(levels)

    def _is_ascending(self, r: list[int]) -> bool:
        for i in range(len(r) - 1):
            if not 0 < (r[i + 1] - r[i]) < 4:
                return False

        return True

    def _is_descending(self, r: list[int]) -> bool:
        r.reverse()
        return self._is_ascending(r)

    @property
    def is_safe(self) -> bool:
        return self._is_safe


reports = []

# Parse reports
for line in data:
    reports.append(Report(list(int(n) for n in line.split())))

print("No of reports:", len(reports))

# Problem 1
no_of_safe_reports = 0
for r in reports:
    if r.is_safe:
        no_of_safe_reports += 1

print("Result (2,1):", no_of_safe_reports)

# Problem 2
