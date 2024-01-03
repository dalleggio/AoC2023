#!/usr/bin/env python
# coding: utf-8

# In[25]:


import sys
import numpy as np
from pprint import pprint
from queue import PriorityQueue


# In[26]:


def get_neighbors(r, c, dir, rl, visited):
    #print('get neighbors params:', r, c, dir, rl, visited)
    neighbors = []
    if dir == 'U':
        # up neighbor
        if rl < 10 and r > 0 and (r - 1, c, 'U') not in visited:
            neighbors.append((r - 1, c, 'U', rl + 1))
        # left neighbor
        if rl >= 4 and c > 0 and (r, c - 1, 'L') not in visited:
            neighbors.append((r, c - 1, 'L', 1))
        # right neighbor
        if rl >= 4 and c < num_cols - 1 and (r, c + 1, 'R') not in visited:
            neighbors.append((r, c + 1, 'R', 1))
            
    elif dir == 'D':
        # down neighbor
        if rl < 10 and r < num_rows - 1 and (r + 1, c, 'D') not in visited:
            neighbors.append((r + 1, c, 'D', rl + 1))
        # left neighbor
        if rl >= 4 and c > 0 and (r, c - 1, 'L') not in visited:
            neighbors.append((r, c - 1, 'L', 1))
        # right neighbor
        if rl >= 4 and c < num_cols - 1 and (r, c + 1, 'R') not in visited:
            neighbors.append((r, c + 1, 'R', 1))

    elif dir == 'R':
        # right neighbor
        if rl < 10 and c < num_cols - 1 and (r, c + 1, 'R') not in visited:
            neighbors.append((r, c + 1, 'R', rl + 1))
        # up neighbor
        if rl >= 4 and r > 0 and (r - 1, c, 'U') not in visited:
            neighbors.append((r - 1, c, 'U', 1))
        # down neighbor
        if rl >= 4 and r < num_rows - 1 and (r + 1, c, 'D') not in visited:
            neighbors.append((r + 1, c, 'D', 1))

    elif dir == 'L':
        # left neighbor
        if rl < 10 and c > 0 and (r, c - 1, 'L') not in visited:
            neighbors.append((r, c - 1, 'L', rl + 1))
        # up neighbor
        if rl >= 4 and r > 0 and (r - 1, c, 'U') not in visited:
            neighbors.append((r - 1, c, 'U', 1))
        # down neighbor
        if rl >= 4 and r < num_rows - 1 and (r + 1, c, 'D') not in visited:
            neighbors.append((r + 1, c, 'D', 1))

    else: # dir not set (at start)
        neighbors = [(0, 1, 'R', 1), (1, 0, 'D', 1)]

    #print('get neighbors ret:', neighbors)
    return neighbors


# In[27]:


fn = "data/heat.txt"

heat = []
with open(fn) as fin:
    for line in fin:
        heat.append(list(map(int, line.strip())))
    ha = np.array(heat)

num_rows, num_cols = ha.shape
dest = (num_rows - 1, num_cols - 1)
print (ha)


# In[28]:


prio_q = PriorityQueue()
# Node data in queue: heat_loss/prio, r, c, dir, run_length)
prio_q.put((0, 0, 0, None, 0))
accum_cost = dict()
accum_cost[(0, 0, None, 0)] = 0
dir = None

while not prio_q.empty():
    hl, r, c, dir, rl = prio_q.get()
    #print('prio q get:', hl, r, c, dir, rl)
    
    if (r, c) == dest and rl >= 4:
        print('total heat loss:', hl)
        break

    neighbors = get_neighbors(r, c, dir, rl, accum_cost)
    #print('neighbors:', neighbors)
    
    for node in neighbors:
        nr, nc, ndir, nrl = node
        cost = accum_cost[(r, c, dir, rl)] + ha[nr, nc]
        if (nr, nc, ndir, nrl) in accum_cost:
            n_cost = accum_cost[(nr, nc, ndir, nrl)]
        else:
            n_cost = sys.maxsize
        #print('cost:', cost, 'n_cost:', n_cost)
        if cost < n_cost:
            accum_cost[(nr, nc, ndir, nrl)] = cost
            #print('prio q put: ', cost, nr, nc, ndir, nrl)
            prio_q.put((cost, nr, nc, ndir, nrl))


# In[ ]:




