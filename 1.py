#!/usr/bin/env python

import sys

elf = 1
curr = 0
max_elf = None
max_food = 0
for line in sys.stdin:
    if line == '\n':
        print(f'Elf {elf} has food {curr}')
        if curr > max_food:
            max_food = curr
            max_elf = elf
        curr = 0
        elf += 1
    else:
        curr += int(line.rstrip())

print(f'Max elf is {max_elf} with food {max_food}')
