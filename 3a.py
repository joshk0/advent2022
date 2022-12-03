#!/usr/bin/env python

import sys

def priority(c):
    if c >= 'a' and c <= 'z':
        return ord(c) - ord('a') + 1
    elif c >= 'A' and c <= 'Z':
        return ord(c) - ord('A') + 27
    else:
        raise RuntimeError(c)

def process(line):
    half = int(len(line)/2)
    left, right = line[:half], line[half:]
    set_left = set([c for c in left])
    intersect = [c for c in right if c in set_left]
    return priority(intersect[0])

print(sum([process(line.rstrip()) for line in sys.stdin]))
    
