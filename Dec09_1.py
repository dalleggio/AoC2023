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
    while np.count_nonzero(d[:w-rounds-1]) != 0:
        # add diff vector (appended with zeros) to stack
        a = np.vstack((a, np.append(d, [0]*(w - len(d)))))
        # Take new diff on last row
        d = a[-1][1:] - a[-1][:-1]
        rounds += 1
        #print('round: ', rounds)
        # copy value in last row to the right
        a[rounds][w - rounds] = a[rounds][w - rounds - 1]
        # Go from bottom row to top, adding one new number each row
        for r in range(rounds, 1, -1):
            a[r-1][w-r+1] = a[r-1][w-r] + a[r][w-r]
    next_value = a[0][w-1] + a[1][w-1]
    print('next: ', next_value)
    sum_next_values += next_value
print('sum: ', sum_next_values)