#!/usr/bin/env python

import operator
import sys

elves = []
curr = 0

for line in sys.stdin:
    if line == '\n':
        elves.append(curr)
        curr = 0
    else:
        curr += int(line.rstrip())

print(sum([a[1] for a in sorted(enumerate(elves), key=operator.itemgetter(1))[-3:]]))
