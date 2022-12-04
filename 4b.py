#!/usr/bin/env python3

import sys

def has_overlap(r1, r2):
    if r1 == r2:
        return 1
    elif r1[0] >= r2[0] and r1[0] <= r2[1]: # left point in r1 is within the r2 range
        return 1
    elif r1[1] >= r2[0] and r1[1] <= r2[1]: # right point in r1 is within the r2 range
        return 1
    elif r2[0] >= r1[0] and r2[0] <= r1[1]: # left point in r2 is within the r1 range
        return 1
    elif r2[1] >= r1[0] and r2[1] <= r1[1]: # right point in r2 is within the r1 range
        return 1
    return 0

print(sum([has_overlap(*[(int(p[0]), int(p[1])) for p in [pair.split('-', 1) for pair in line.rstrip().split(',', 1)]]) for line in sys.stdin]))
