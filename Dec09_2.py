#!/usr/bin/env python
# coding: utf-8

from pprint import pprint
import numpy as np

fn = "data/histories.txt"

histories = []
with open(fn) as fin:
    for line in fin:
        histories.append(list(map(int, line.strip().split())))
    hist_array = np.array(histories)

sum_next_values = 0
for h in hist_array:
    d = h[1:] - h[:-1]
    w = len(h)
    # work stack
    a = h
    rounds = 0
    # Take diffs in a loop until we reach zeros
    while np.count_nonzero(d[rounds:w]) != 0:
        # add diff vector (pre-pended with zeros) to stack
        a = np.vstack((a, np.insert(d, 0, [0])))
        # Take new diff on last row
        d = a[-1][1:] - a[-1][:-1]
        rounds += 1
    # copy value in last row to the right
    a[rounds][rounds-1] = a[rounds][rounds]
    # Go from bottom row to top, adding one new number each row
    for r in range(rounds, 1, -1):
        a[r-1][r-2] = a[r-1][r-1] - a[r][r-1]
    #print('a after rounds: ', a)
    next_value = a[0][0] - a[1][0]
    print('next: ', next_value)
    sum_next_values += next_value
print('sum: ', sum_next_values)