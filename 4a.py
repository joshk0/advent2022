#!/usr/bin/env python3

import sys

def has_subset(r1, r2):
    if r1 == r2:
        return 1
    elif r1[0] >= r2[0] and r1[1] <= r2[1]: # r1 is fully part of r2
        return 1
    elif r2[0] >= r1[0] and r2[1] <= r1[1]: # r2 is fully part of r1
        return 1
    return 0

print(sum([has_subset(*[(int(p[0]), int(p[1])) for p in [pair.split('-', 1) for pair in line.rstrip().split(',', 1)]]) for line in sys.stdin]))
