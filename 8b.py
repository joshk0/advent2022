#!/usr/bin/env python

import sys

grid = [[int(x) for x in line.rstrip()] for line in sys.stdin]

def viewing_distance(seq, max_val):
    for i, item in enumerate(seq):
        if item >= max_val:
            return seq[:i+1] # include current tree
    return seq

max_score = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        # North viewing distance
        height = grid[y][x]

        north_trees = [row[x] for row in grid[:y]][::-1]
        north_score = len(viewing_distance(north_trees, height))

        south_trees = [row[x] for row in grid[y+1:]]
        south_score = len(viewing_distance(south_trees, height))
        
        east_trees = grid[y][x+1:]
        east_score = len(viewing_distance(east_trees, height))

        west_trees = grid[y][:x][::-1]
        west_score = len(viewing_distance(west_trees, height))

        score = north_score * south_score * west_score * east_score

        if score > max_score:
            max_score = score

print(max_score)
