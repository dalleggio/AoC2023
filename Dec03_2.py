#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pprint import pprint
from collections import namedtuple
from math import prod

Dims = namedtuple('dims', ['x', 'y'])

def getCenterGear(row, x):
    start = x
    end = x + 1
    while row[start - 1].isnumeric() and start - 1 >= 0:
        start -= 1
    while end <= len(row) - 1:
        if row[end].isnumeric():
            end += 1
        else:
            break
    return int(row[start:end])
               
def getLeftGear(row, x):
    if row[x-1].isnumeric():
        end = x
        start = x - 1
        # Look back for start of digits
        while row[start-1].isnumeric() and start - 1 >= 0:
            start = start - 1
        return int(row[start:end])
    else:
        return None

def getRightGear(row, x):
    if row[x+1].isnumeric():
        start = x + 1
        end = start + 1
        # Look forward for end of digits
        while end <= len(row) - 1:
            if row[end].isnumeric():
                end = end + 1
            else:
                break
        return int(row[start:end])
    else:
        return None

def getTopGears(row, x):
    gears = []
    # Check directly above (center)
    if row[x].isnumeric():
        gears.append(getCenterGear(row, x))
    else:
        if row[x - 1].isnumeric() and x > 0:
            gears.append(getLeftGear(row, x))
        if row[x + 1].isnumeric() and x < len(row) - 1:
            gears.append(getRightGear(row, x))
    return gears

def getBottomGears(row, x):
    gears = []
    # Check directly below (center)
    if row[x].isnumeric():
        gears.append(getCenterGear(row, x))
    else:
        if row[x - 1].isnumeric() and x > 0:
            gears.append(getLeftGear(row, x))
        if x < len(row) - 1:
            if row[x + 1].isnumeric():
                gears.append(getRightGear(row, x))
    return gears
    
def getGears(schem, dims, r, c):
    # Go around (x, y) location and look for digits
    gears = []
    tg = getTopGears(schem[r - 1], c) if r > 0 else []
    g = getLeftGear(schem[r], c) if c > 0 else None
    lg = [g] if g is not None else []
    g = getRightGear(schem[r], c) if c < dims.x - 1 else None
    rg = [g] if g is not None else []
    bg = getBottomGears(schem[r + 1], c) if r < dims.y - 1 else []
    for g in tg + lg + rg + bg:
        gears.append(g)
    print('get gears: ', gears)
    return gears
    
def getGearRatio (schem, dims, r, c):
    gears = getGears(schem, dims, r, c)
    print('get gear ratio: ', prod(gears) if len(gears) == 2 else 0)
    return (prod(gears) if len(gears) == 2 else 0)
    
schem = []
sum_gear_ratios = 0
with open("data/parts.txt") as fin:
    for line in fin:
        schem.append(line.strip())
    pprint(schem)
    # Use last line to determine row length
    row_len = len(line.strip())
    col_len = len(schem)
    dims = Dims(row_len, col_len)
    print('dims: ', dims)
    for row in range(col_len):
        print('row ', row)
        col = 0
        start = -1
        end = -1
        while col < row_len:
            # Determine start and end of each sequence of digits
            if schem[row][col] == '*':
                print("found gear at: ", row, col)
                sum_gear_ratios += getGearRatio(schem, dims, row, col)
                
            col += 1
                       
print('sum gear ratios: ', sum_gear_ratios)         


# In[ ]:





# In[ ]:




