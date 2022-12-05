#!/usr/bin/env python3

import sys

def process_crate_input(lines, num_cols):
    crates = [[] for _ in range(num_cols)]
    for i, line in enumerate(crate_row_lines):
        for j in range(num_cols):
            c = line[(4*j)+1]
            if c != ' ':
                crates[j].append(line[(4*j)+1])
    return crates

def move(crates, line):
    _move, crates_to_move, _from, move_from, _to, move_to = line.split(' ', 5)
    crates_to_move, move_from, move_to = int(crates_to_move), int(move_from) - 1, int(move_to) - 1
    load = crates[move_from][:crates_to_move]
    crates[move_from] = crates[move_from][crates_to_move:]
    crates[move_to] = load + crates[move_to]
    print(f'AFTER {line}')
    pretty_print(crates, len(crates))

def pretty_print(stacks, cols):
    lines = []
    row = 0

    while True:
        s = []
        present = False

        for stack in crates:
            if len(stack) > row:
                present = True
                s.append(f'[{stack[::-1][row]}]')
            else:
                s.append('   ')

        if not present:
            break

        lines.insert(0, ' '.join(s))
        row += 1

    print('\n'.join(lines))
    print(' ' .join([f' {i} ' for i in range(1, cols+1)]))

crate_row_lines = []
crates = None

for line in sys.stdin:
    if line.startswith('['): # Row of crates
        crate_row_lines.append(line.rstrip('\n'))
    elif line.startswith(' 1'): # Crate layout legend
        crate_columns = int(line.rstrip().split(' ')[-1])
        crates = process_crate_input(crate_row_lines, crate_columns)
        pretty_print(crates, crate_columns)
    elif line.startswith('move'): # Instruction
        move(crates, line.rstrip())

print(''.join([col[0] for col in crates]))
