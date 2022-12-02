#!/usr/bin/env python

import sys

your_choice_mapping = {'X': 'R', 'Y': 'P', 'Z': 'S'}
opp_choice_mapping = {'A': 'R', 'B': 'P', 'C': 'S'}
choice_values = {'X': 1, 'Y': 2, 'Z': 3}
win_combos = set([
    ('R', 'S'),
    ('P', 'R'),
    ('S', 'P'),
])

def score_rps(opp_crypt, your_crypt):
    outcome = play_rps(your_choice_mapping[your_crypt], opp_choice_mapping[opp_crypt])
    return outcome + choice_values[your_crypt]

def play_rps(your_choice, opp_choice):
    if your_choice == opp_choice:
        return 3
    elif (your_choice, opp_choice) in win_combos:
        return 6
    elif (opp_choice, your_choice) in win_combos:
        return 0

print(sum([score_rps(*line.rstrip().split(' ', 2)) for line in sys.stdin]))
