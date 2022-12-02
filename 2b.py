#!/usr/bin/env python

import sys

opp_choice_mapping = {'A': 'R', 'B': 'P', 'C': 'S'}
choice_values = {'R': 1, 'P': 2, 'S': 3}
outcome_values = {'X': 0, 'Y': 3, 'Z': 6}
RPS = ('R', 'P', 'S')

# To get a win, play index+1. To get a draw, play the same. To lose, play index-1.
# Must wrap around.
desired_outcome_offsets = {'X': -1, 'Y': 0, 'Z': 1}

def score_rps(opp_crypt, desired_outcome):
    index = RPS.index(opp_choice_mapping[opp_crypt])
    your_choice = RPS[(index + desired_outcome_offsets[desired_outcome]) % 3]
    return choice_values[your_choice] + outcome_values[desired_outcome]

print(sum([score_rps(*line.rstrip().split(' ', 2)) for line in sys.stdin]))
