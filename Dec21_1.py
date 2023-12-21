#!/usr/bin/env python
# coding: utf-8
om pprint import pprint
import numpy as np

fn = "data/steps.txt"

garden = []
with open(fn) as fin:
    for line in fin:
        garden.append(list(line.strip()))

ga = np.array(garden)
pprint(ga)
dimx, dimy = ga.shape

num_steps = 64
s_rc = np.where(ga == 'S')
s = (s_rc[0][0], s_rc[1][0])
print('start: ', s)

step_list = [[] * n for n in range(num_steps)]
for i in range(num_steps):
    if i == 0:
        px = s[0]
        py = s[1]
        # replace S with '.' so we can count it
        ga[px, py] = '.'
        # go up
        if ga[px, py - 1] == '.':
            step_list[0].append((px, py - 1))
        # go down
        if ga[px, py + 1] == '.':
            step_list[0].append((px, py + 1))
        # go right
        if ga[px + 1, py] == '.':
            step_list[0].append((px + 1, py ))
        # go down
        if ga[px - 1, py] == '.':
            step_list[0].append((px - 1, py))
    else:
        for j in range(len(step_list[i - 1])):
            px = step_list[i - 1][j][0]
            py = step_list[i - 1][j][1]
            # go up
            if py > 0:
                if ga[px, py - 1] == '.' and (px, py - 1) not in step_list[i]:
                    step_list[i].append((px, py - 1))
            # go down
            if py < dimy - 1:
                if ga[px, py + 1] == '.' and (px, py + 1) not in step_list[i]:
                    step_list[i].append((px, py + 1))
            # go right
            if px < dimx - 1:
                if ga[px + 1, py] == '.' and (px + 1, py) not in step_list[i]:
                    step_list[i].append((px + 1, py ))
            # go down
            if px > 0:
                if ga[px - 1, py] == '.' and (px - 1, py) not in step_list[i]:
                    step_list[i].append((px - 1, py))
#print(step_list)

print ('num plots reached: ', len(step_list[num_steps - 1]))