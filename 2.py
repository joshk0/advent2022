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

def compare_second(t1, t2):
    if t1[1] < t2[1]:
        return -1
    elif t1[1] == t2[1]:
        return 0
    else:
        return 1

print(sum([a[1] for a in sorted(enumerate(elves), key=operator.itemgetter(1))[-3:]]))
