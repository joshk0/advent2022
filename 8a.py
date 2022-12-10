#!/usr/bin/env python

import sys

grid = [[int(x) for x in line.rstrip()] for line in sys.stdin]

for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        this_height = grid[y][x]
