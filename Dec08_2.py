#!/usr/bin/env python
# coding: utf-8

from pprint import pprint
from collections import namedtuple
from math import lcm

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
instr_len = len(instr)
# Get list of nodes ending with 'A'
next_nodes = [n for n in network.keys() if n.endswith('A')]
print(next_nodes)
steps_to_xxz = []
for i in range(len(next_nodes)):
    instr_ptr = 0
    step_cntr = 0
    while not next_nodes[i].endswith('Z')  and step_cntr < 1000000:
        if instr[instr_ptr] == 'L':
            next_nodes[i] = network[next_nodes[i]].left
        else:
            next_nodes[i] = network[next_nodes[i]].right
        instr_ptr = (instr_ptr + 1) % instr_len
        step_cntr += 1
    #print(next_nodes)
    print('steps: ', step_cntr)
    steps_to_xxz.append(step_cntr)
print(steps_to_xxz)
print(lcm(*steps_to_xxz))