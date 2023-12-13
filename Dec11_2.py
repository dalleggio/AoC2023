#!/usr/bin/env python
# coding: utf-8

from pprint import pprint
from collections import namedtuple
import numpy as np
from bisect import bisect

Point = namedtuple('Point', ['x', 'y'])
Tile = namedtuple('Dir', ['d', 'x', 'y'])

fn = "data/galaxies.txt"
galaxies = []
with open(fn) as fin:
    for line in fin:
        galaxies.append(list(line.strip()))
    ga = np.array(galaxies)
    print(ga)

# Determine rows that have no galaxies
empty_rows = []
for r in range(len(ga)):
    if '#' not in ga[r]:
        empty_rows.append(r)
print('empty_rows: ', empty_rows)
#ga = np.insert(ga, empty_rows, ['.'], axis=0)
#print(ga)
# Determine columns that have no galaxies
empty_cols = []
for c in range(len(ga.T)):
    if '#' not in ga.T[c]:
        empty_cols.append(c)
print('empty_cols: ', empty_cols)
#ga = np.insert(ga, empty_cols, ['.'], axis=1)
#print(ga)

# Get positions of galaxies
g = np.argwhere(ga == '#')
print('g: ', g)
# Calculate distance between pairs of galaxies and sum them
sum = 0
for i in range(len(g)):
    for j in range(i + 1, len(g)):
        dist = (abs(g[j][0] - g[i][0]) + abs(g[j][1] - g[i][1]))
        #print('dist: ', dist)
        # Determine number of empty columns we are crossing between the two galaxies
        index_coli = bisect(empty_cols, g[i][1])
        index_rowi = bisect(empty_rows, g[i][0])
        index_colj = bisect(empty_cols, g[j][1])
        index_rowj = bisect(empty_rows, g[j][0])
        col_diff = abs(index_colj - index_coli) * (1000000 - 1)
        row_diff = abs(index_rowj - index_rowi) * (1000000 - 1)
        sum += (dist + row_diff + col_diff)
print(sum)