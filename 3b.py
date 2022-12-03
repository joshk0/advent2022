#!/usr/bin/env python

import sys

def priority(c):
    if c >= 'a' and c <= 'z':
        return ord(c) - ord('a') + 1
    elif c >= 'A' and c <= 'Z':
        return ord(c) - ord('A') + 27
    else:
        raise RuntimeError(c)

def process(lines):
    sets = [set(c for c in line) for line in lines]
    intersect = sets[0]
    for s in sets[1:]:
        intersect = intersect & s
    return priority([c for c in intersect][0])

lines = [line.rstrip() for line in sys.stdin]
chunk_size = 3
chunked_lines = [lines[i:i+chunk_size] for i in range(0, len(lines), chunk_size)]
print(sum([process(line_chunk) for line_chunk in chunked_lines]))
