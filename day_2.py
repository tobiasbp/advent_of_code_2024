#!/usr/bin/env python3

from pathlib import Path

# Read the data
data = Path("data/day_2_1.txt").read_text().splitlines()


class Report:
    def __init__(self, levels: list[int]) -> None:
        self.levels = levels

    def _is_ascending(self, r: list[int]) -> bool:
        for i in range(len(r) - 1):
            if not 0 < (r[i + 1] - r[i]) < 4:
                return False

        return True

    def _is_descending(self, r: list[int]) -> bool:
        r.reverse()
        return self._is_ascending(r)

    def is_safe(self, dampner_enabled=False) -> bool:
        if not dampner_enabled:
            return self._is_ascending(self.levels) or self._is_descending(self.levels)

        # Evaluate variations of the levels with one entry removed
        for level_index_to_remove in range(len(self.levels)):
            levels = [
                l for i, l in enumerate(self.levels) if i != level_index_to_remove
            ]
            if self._is_ascending(levels) or self._is_descending(levels):
                return True

        return False


# Parse reports
reports: list[Report] = []
for line in data:
    reports.append(Report(list(int(n) for n in line.split())))

print("No of reports:", len(reports))


# Problem 1
no_of_safe_reports = 0
for r in reports:
    if r.is_safe(dampner_enabled=False):
        no_of_safe_reports += 1

assert no_of_safe_reports == 287, "Result 2,1 is wrong"
print("Result (2,1):", no_of_safe_reports)


# Problem 2
no_of_safe_reports = 0
for r in reports:
    if r.is_safe(dampner_enabled=True):
        no_of_safe_reports += 1

assert no_of_safe_reports == 354, "Result 2,2 is wrong"
print("Result (2,2):", no_of_safe_reports)
