#!/usr/bin/env python3

import sys

def distinct_run_index(s, num_chars):
    for i in range(len(s)):
        if len(set(s[i:i+num_chars])) == num_chars:
            return i + num_chars

print(sum([distinct_run_index(line.rstrip(), 14) for line in sys.stdin]))
