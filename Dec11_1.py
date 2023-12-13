#!/usr/bin/env python
# coding: utf-8

from pprint import pprint
from collections import namedtuple
import numpy as np

Point = namedtuple('Point', ['x', 'y'])
Tile = namedtuple('Dir', ['d', 'x', 'y'])

n = "data/galaxies.txt"
galaxies = []
with open(fn) as fin:
    for line in fin:
        galaxies.append(list(line.strip()))
    ga = np.array(galaxies)
    #print(ga)

# Double rows that have no galaxies
empty_rows = []
for r in range(len(ga)):
    if '#' not in ga[r]:
        empty_rows.append(r)
ga = np.insert(ga, empty_rows, ['.'], axis=0)
#print(ga)
# Double columns that have no galaxies
empty_cols = []
for c in range(len(ga.T)):
    if '#' not in ga.T[c]:
        empty_cols.append(c)
ga = np.insert(ga, empty_cols, ['.'], axis=1)
#print(ga)

# Get positions of galaxies
g = np.argwhere(ga == '#')
print('g: ', g)
# Calculate distance between pairs of galaxies and sum them
sum = 0
for i in range(len(g)):
    for j in range(i + 1, len(g)):
        sum += (abs(g[j][0] - g[i][0]) + abs(g[j][1] - g[i][1]))
print(sum)