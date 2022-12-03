#!/usr/bin/env python

import functools
import sys

def priority(c):
    if c >= 'a' and c <= 'z':
        return ord(c) - ord('a') + 1
    elif c >= 'A' and c <= 'Z':
        return ord(c) - ord('A') + 27
    else:
        raise RuntimeError(c)

def process(sets):
    return priority([c for c in functools.reduce(lambda a, b: a & b, sets)][0])

sets = [set([c for c in line.rstrip()]) for line in sys.stdin]
chunked_sets = [sets[i:i+3] for i in range(0, len(sets), 3)]
print(sum([process(set_chunk) for set_chunk in chunked_sets]))
