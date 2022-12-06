#!/usr/bin/env python3

import sys

def four_distinct_index(s):
    for i in range(len(s)):
        if len(set(s[i:i+4])) == 4:
            return i + 4

print(sum([four_distinct_index(line.rstrip()) for line in sys.stdin]))
