#!/usr/bin/env python
# coding: utf-8

import numpy as np
from pprint import pprint

def fix_smudge(arr):
    num_rows, num_cols = arr.shape
    # check horizontal symmetry
    for r in range(num_rows - 1):
        print('r: ', r)
        if r < num_rows // 2:
            print('0:', r+1, 'vs ', r+1, ':', 2*(r + 1))
            print(arr[0:r+1, :])
            print(np.flipud(arr[r+1: 2*(r + 1), :]))
            smudges = np.argwhere(arr[0:r+1, :] != np.flipud(arr[r+1: 2*(r + 1), :]))
            if smudges.size == 2:
                sm_r = smudges[0][0]
                sm_c = smudges[0][1]
                print('flip: ', sm_r, sm_c)
                if arr[sm_r, sm_c] == '.':
                    arr[sm_r, sm_c] = '#'
                else:
                    arr[sm_r, sm_c] = '.'
                print('row smudges:', smudges)
                return arr
                
        else:
            print(r+1 - (num_rows - (r+1)),':',r + 1, 'vs ', r+1, ':', num_rows)
            print(arr[r+1 - (num_rows - (r+1)):r + 1, :])
            print(np.flipud(arr[r+1: num_rows, :]))
            smudges = np.argwhere(arr[r+1 - (num_rows - (r+1)):r+1, :] != np.flipud(arr[r+1: num_rows, :]))
            if smudges.size == 2:
                sm_r = r+1 - (num_rows - (r+1)) + smudges[0][0]
                sm_c = smudges[0][1]
                print('flip: ', sm_r, sm_c)
                if arr[sm_r, sm_c] == '.':
                    arr[sm_r, sm_c] = '#'
                else:
                    arr[sm_r, sm_c] = '.'
                print('row smudges:', smudges)
                return arr
        
    for c in range(num_cols - 1):
        print('c: ', c)
        if c < num_cols // 2:
            print('0:', c+1, 'vs ', c+1, ':', 2*(c + 1))
            print(arr[:, 0:c+1])
            print(np.fliplr(arr[:, c+1: 2*(c + 1)]))
            smudges = np.argwhere(arr[:, 0:c+1] != np.fliplr(arr[:, c+1:2*(c+1)]))
            if smudges.size == 2:
                sm_r = smudges[0][0]
                sm_c = smudges[0][1]
                print('flip: ', sm_r, sm_c)
                if arr[sm_r, sm_c] == '.':
                    arr[sm_r, sm_c] = '#'
                else:
                    arr[sm_r, sm_c] = '.'
                print('col smudges:', smudges)
                return arr
        else:
            print(c+1 - (num_cols - (c+1)),':',c + 1, 'vs ', c+1, ':', num_cols)
            print(arr[:, c+1 - (num_cols - (c+1)):c + 1])
            print(np.fliplr(arr[:, c+1: num_cols]))
            smudges = np.argwhere(arr[:, c+1 - (num_cols - (c+1)):c+1,] != np.fliplr(arr[:, c+1: num_cols]))
            if smudges.size == 2:
                sm_r = smudges[0][0]
                sm_c = c+1 - (num_cols - (c+1)) + smudges[0][1]
                print('flip: ', sm_r, sm_c)
                if arr[sm_r, sm_c] == '.':
                    arr[sm_r, sm_c] = '#'
                else:
                    arr[sm_r, sm_c] = '.'
                print('col smudges:', smudges)
                return arr

    return (arr)

def find_sym(arr, skip_r, skip_c):
    num_rows, num_cols = arr.shape
    # check horizontal symmetry
    print('skip_r:', skip_r, 'skip_c:', skip_c)
    for r in range(num_rows - 1):
        #print('r: ', r)
        if r != skip_r:
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
        if c != skip_c:
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
            (skip_r, skip_c) = find_sym(ma, -1, -1)
            print('first run skip_r:', skip_r, 'skip_c:', skip_c)
            if skip_r > 0:
                skip_r -= 1
            else:
                skip_r = -1
            if skip_c > 0:
                skip_c -= 1
            else:
                skip_c = -1
            ma = fix_smudge(ma)
            print('calling find sym 2nd time with skip_r:', skip_r, 'skip_c:', skip_c)
            (r, c) = find_sym(ma, skip_r, skip_c)
            print('sym: ', r, c)
            if (r, c) != (-1, -1):
                total += (100 * r + c )
            mirrors.clear()

    ma = np.array(mirrors)
    #print (ma)
    (skip_r, skip_c) = find_sym(ma, -1, -1)
    print('first run skip_r:', skip_r, 'skip_c:', skip_c)
    if skip_r > 0:
        skip_r -= 1
    else:
        skip_r = -1
    if skip_c > 0:
        skip_c -= 1
    else:
        skip_c = -1
    ma = fix_smudge(ma)
    print('calling find sym 2nd time with skip_r:', skip_r, 'skip_c:', skip_c)
    (r, c) = find_sym(ma, skip_r, skip_c)
    if (r, c) != (-1, -1):
        total += (100 * r + c)
        
print('total: ', total)
