#!/usr/bin/env python

import sys

grid = [[int(x) for x in line.rstrip()] for line in sys.stdin]
visibilities = {}

def is_edge(y, x):
    return y == 0 or y == len(grid) - 1 or x == 0 or x == len(grid[0]) - 1

visible_trees = 0
s = ''
for y in range(len(grid)):
    for x in range(len(grid[0])):
        visible = False
        height = grid[y][x]
        if is_edge(y, x):
            visible = True
        elif max(row[x] for row in grid[:y]) < height:
            visible = True
        elif max(row[x] for row in grid[y+1:]) < height:
            visible = True
        elif max(grid[y][:x]) < height:
            visible = True
        elif max(grid[y][x+1:]) < height:
            visible = True
        if visible:
            s += 'V'
            visible_trees += 1
        else:
            s += 'X'
    s += '\n'

print(visible_trees)
