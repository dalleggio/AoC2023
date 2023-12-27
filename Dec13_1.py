#!/usr/bin/env python
# coding: utf-8

import numpy as np
from pprint import pprint

def find_sym(arr):
    num_rows, num_cols = arr.shape
    # check horizontal symmetry
    for r in range(num_rows - 1):
        #print('r: ', r)
        if r < num_rows // 2:
            #print('0:', r+1, 'vs ', r+1, ':', 2*(r + 1))
            #print(arr[0:r+1, :])
            #print(np.flipud(arr[r+1: 2*(r + 1), :]))
            if np.all(arr[0:r+1, :] == np.flipud(arr[r+1: 2*(r + 1), :])):
                print('sym1 r: ', r + 1)
                return (r + 1, 0)
        else:
            #print(r+1 - (num_rows - (r+1)),':',r + 1, 'vs ', r+1, ':', num_rows)
            #print(arr[r+1 - (num_rows - (r+1)):r + 1, :])
            #print(np.flipud(arr[r+1: num_rows, :]))
            if np.all(arr[r+1 - (num_rows - (r+1)):r+1, :] == np.flipud(arr[r+1: num_rows, :])):
                print('sym2 r: ', r + 1)
                return (r + 1, 0)                
        
    for c in range(num_cols - 1):
        #print('c: ', c)
        if c < num_cols // 2:
            #print('0:', c+1, 'vs ', c+1, ':', 2*(c + 1))
            #print(arr[0:c+1, :])
            #print(np.flipud(arr[c+1: 2*(c + 1), :]))
            if np.all(arr[:, 0:c+1] == np.fliplr(arr[:, c+1:2*(c+1)])):
                print('sym1 c: ', c + 1)
                return (0, c + 1)
        else:
            #print(c+1 - (num_cols - (c+1)),':',c + 1, 'vs ', c+1, ':', num_cols)
            #print(arr[c+1 - (num_cols - (c+1)):c + 1, :])
            #print(np.flipud(arr[c+1: num_cols, :]))
            if np.all(arr[:, c+1 - (num_cols - (c+1)):c+1,] == np.fliplr(arr[:, c+1: num_cols])):
                print('sym2 c: ', c + 1)
                return (0, c + 1)                

    return (-1, -1)

fn = "data/mirrors.txt"
mirrors = []
total = 0
with open(fn) as fin:
    for line in fin:
        if line.strip() != '' and line:
            mirrors.append(list(line.strip()))
        else:
            ma = np.array(mirrors)
            print (ma)
            (r, c) = find_sym(ma)
            print('sym: ', r, c)
            if (r, c) != (-1, -1):
                total += (100 * r + c )
            mirrors.clear()

    ma = np.array(mirrors)
    print (ma)
    (r, c) = find_sym(ma)
    if (r, c) != (-1, -1):
        total += (100 * r + c)
        
print('total: ', total)