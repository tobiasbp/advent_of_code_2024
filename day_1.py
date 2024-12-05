#!/usr/bin/env python3

from pathlib import Path

# Read the data
data = Path('data/day_1_1.txt').read_text().splitlines()

l_1 = []
l_2 = []

for d in data:
    id1, id2 = d.split()
    l_1.append(int(id1))
    l_2.append(int(id2))


ls_1 = sorted(l_1)
ls_2 = sorted(l_2)

sum = 0
for i in range(len(ls_1)):
  sum += abs(ls_1[i] - ls_2[i])

print("Result (1,1):", sum)
