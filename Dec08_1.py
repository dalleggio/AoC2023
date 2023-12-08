#!/usr/bin/env python
# coding: utf-8

from pprint import pprint
from collections import namedtuple

Node = namedtuple('Node', ['left', 'right'])
network = {}

fn = "data/nodes.txt"
with open(fn) as fin:
    first_line = True
    for line in fin:
        new_line = line.strip()
        if first_line:
            instr = new_line
            print(instr)
            first_line = False
        else:
            if new_line:
                entry = new_line.split('=')
                #print(entry)
                node_name = entry[0].strip()
                network[node_name] = Node(*entry[1].replace(' ','').strip('()').split(','))
    pprint (network)

# Use instructions in a loop to traverse network
instr_ptr = 0
instr_len = len(instr)
next_node = 'AAA'
step_cntr = 0
while next_node != 'ZZZ':
    left, right = network[next_node]
    next_node = left if instr[instr_ptr] == 'L' else right
    instr_ptr = (instr_ptr + 1) % instr_len
    step_cntr += 1
    #print(next_node)
print('steps: ', step_cntr)