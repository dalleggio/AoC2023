#!/usr/bin/env python
# coding: utf-8

# In[82]:


import numpy as np


# In[83]:


def move(elem, r, c, dir, shape):
    if elem == '.':
        if dir == 'u':
            if r > 0:
                return [(r - 1, c, dir)]
            else:
                return None
        elif dir == 'd':
            if r < shape[0] - 1:
                return [(r + 1, c, dir)]
            else:
                return None
        elif dir == 'r':
            if c < shape[1] - 1:
                return [(r, c + 1, dir)]
            else:
                return None
        else:
            if c > 0:
                return [(r, c - 1, dir)]
            else:
                return None
    elif elem == '/':
        if dir == 'u':
            if c < shape[1] - 1:
                return [(r, c + 1, 'r')]
            else:
                return None
        elif dir == 'd':
            if c > 0:
                return [(r, c - 1, 'l')]
            else:
                return None
        elif dir == 'r':
            if r > 0:
                return [(r - 1, c, 'u')]
            else:
                return None
        else:
            if r < shape[0] - 1:
                return [(r + 1, c, 'd')]
            else:
                return None
    elif elem == '\\':
        if dir == 'u':
            if c > 0:
                return [(r, c - 1, 'l')]
            else:
                return None
        elif dir == 'd':
            if c < shape[1] - 1:
                return [(r, c + 1, 'r')]
            else:
                return None
        elif dir == 'r':
            if r < shape[0] - 1:
                return [(r + 1, c, 'd')]
            else:
                return None
        else:
            if r > 0:
                return [(r - 1, c, 'u')]
            else:
                return None
    elif elem == '-':
        if dir in ('u', 'd'):
            if c > 0:
                m1 = (r, c - 1, 'l')
            else:
                m1 = None
            if c < shape[1] - 1:
                m2 = (r, c + 1, 'r')
            else:
                m2 = None
            if m1 is not None and m2 is not None:
                return [m1, m2]
            elif m1 is not None:
                return [m1]
            else:
                return [m2]
        elif dir == 'r':
            if c < shape[1] - 1:
                return [(r, c + 1, dir)]
            else:
                return None
        else:
            if c > 0:
                return [(r, c - 1, dir)]
            else:
                return None
    else: 
        if dir in ('r', 'l'):
            if r > 0:
                m1 = (r - 1, c, 'u')
            else:
                m1 = None
            if r < shape[0] - 1:
                m2 = (r + 1, c, 'd')
            else:
                m2 = None
            if m1 is not None and m2 is not None:
                return [m1, m2]
            elif m1 is not None:
                return [m1]
            else:
                return [m2]
        elif dir == 'u':
            if r > 0:
                return [(r - 1, c, dir)]
            else:
                return None
        else:
            if r < shape[0] - 1:
                return [(r + 1, c, dir)]
            else:
                return None


# In[84]:


fn = "data/light.txt"

optics = []
with open(fn) as fin:
    for line in fin:
        optics.append(list(line.strip()))
    optics_arr = np.array(optics)

print (optics_arr)


# In[ ]:


stack = []
visited = []
num_rows, num_cols = optics_arr.shape
energized = np.zeros((num_rows, num_cols))
dir = 'r'
r = 0
c = 0
while True:
    energized[r][c] = 1
    elem = optics_arr[r][c]
    print('elem: ', elem)
    next_move = move(elem, r, c, dir, (num_rows, num_cols))
    print('next_move: ', next_move)
    v0 = False
    v1 = False
    if next_move is not None:
        if next_move[0] not in visited:
            r, c, dir = next_move[0]
            visited.append(next_move[0])
        else:
            v0 = True
        if len(next_move) > 1:
            if next_move[1] not in visited and next_move[1] not in stack:
                stack.append(next_move[1])
                print('push: ', next_move[1])
            else:
                v1 = True
        if v0 and v1:
            print('v0 and v1 true')
    if next_move is None or v0:
        if len(stack) == 0:
            break
        else:
            while len(stack) > 0:
                r, c, dir = stack.pop()
                if (r, c, dir) not in visited:
                    visited.append((r, c, dir))
                    print('pop: ', r, c, dir)
                    break
                print('popped visited: ', r, c, dir)

# count number of energized tiles
print('num energized tiles: ', int(np.sum(energized)))


# In[ ]:




