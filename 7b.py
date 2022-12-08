#!/usr/bin/env python3

import operator
import os
import sys

# Mutated by Dir constructor
all_dirs = {}

class Node(object):
    def __init__(self, name):
        self.name = name

    def size(self):
        raise NotImplementedError

class Dir(Node):
    def __init__(self, name):
        Node.__init__(self, name)
        self.contents = {}
        all_dirs[name] = self

    def add(self, node):
        self.contents[node.name] = node

    def size(self):
        return sum([n.size() for n in self.contents.values()])

    def __str__(self):
        s = f'begin dir {self.name}\n'
        for _, n in self.contents.items():
            s += str(n) + '\n'
        s += f'end dir {self.name}\n'
        return s

class File(Node):
    def __init__(self, name, size):
        Node.__init__(self, name)
        self._size = size

    def size(self):
        return self._size

    def __str__(self):
        return f'{self.size} {self.name}'

cwd = '/'
root = Dir('/')
cwd_obj = root
in_ls = False

for line in sys.stdin:
    if line[0] == '$':
        args = line.rstrip().split(' ')[1:]
        in_ls = False
        if args[0] == 'cd':
            if args[1] == '..':
                cwd = os.path.dirname(cwd)
            else:
                cwd = os.path.join(cwd, args[1])
                cwd_obj = all_dirs[cwd]
        elif args[0] == 'ls':
            in_ls = True
    elif in_ls:
        args = line.rstrip().split(' ')
        fname = os.path.join(cwd, args[1])
        if args[0] == 'dir':
            node = Dir(fname)
        else:
            node = File(fname, int(args[0]))
        cwd_obj.add(node)
    else:
        raise RuntimeError(f'unexpected: {line}')

deletion_goal = 30000000 - (70000000 - root.size())
print(sorted([d.size() for d in all_dirs.values() if d.size() >= deletion_goal])[0])
