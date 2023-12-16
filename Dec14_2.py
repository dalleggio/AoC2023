#!/usr/bin/env python
# coding: utf-8

# In[224]:


import numpy as np  


# In[225]:


def roll_north(ra):
    num_rows, num_cols = ra.shape
    for c in range(num_cols):
        col = ra[:, c]
        cube_locs = [i for i, x in enumerate(col) if x == '#']
        #print(cube_locs)
        # count number of round rocks between North (row 0 and first cube rock
        if cube_locs:
            rounds = np.count_nonzero(col[:cube_locs[0]] == 'O')
            col[:rounds] = ['O'] * rounds
            col[rounds:cube_locs[0]] = '.' * (cube_locs[0] - rounds)
        else:
            rounds = np.count_nonzero(col == 'O')
            col[:rounds] = ['O'] * rounds
            col[rounds:] = '.' * (num_rows - rounds)
            continue
    
        # count number of round rocks between cube rocks
        for i in range(len(cube_locs) - 1):
            rounds = np.count_nonzero(col[cube_locs[i]:cube_locs[i+1]] == 'O')
            col[cube_locs[i] + 1:cube_locs[i] + rounds + 1] = ['O'] * rounds
            col[cube_locs[i] + rounds + 1:cube_locs[i+1]] = '.' * (cube_locs[i+1] - cube_locs[i] - rounds - 1)

        # count number of round rocks between last cube rock and South (last row)
        rounds = np.count_nonzero(col[cube_locs[-1]:num_rows] == 'O')
        col[cube_locs[-1] + 1:cube_locs[-1] + rounds + 1] = ['O'] * rounds
        col[cube_locs[-1] + rounds + 1:] = '.'  * (num_rows - cube_locs[-1] - rounds -1)

    return ra


# In[226]:


def calc_load(ra):
    num_rows, num_cols = ra.shape
    # calculate load
    load = 0
    for c in range(num_cols):
        col = ra[:, c]
        round_locs = [i for i, x in enumerate(col) if x == 'O']
        load += sum(num_rows - round_locs[i] for i in range(len(round_locs)))
    return load


# In[227]:


fn = "data/rocks.txt"
rocks = []
with open(fn) as fin:
    for line in fin:
        rocks.append(list(line.strip()))
    ra = np.array(rocks)

print (ra)


# In[228]:


cycles = 1000
for i in range(cycles):
    for j in range(4):
        ra = roll_north(ra)
        ra = np.rot90(ra, 1, axes=(1, 0))

    load = calc_load(ra)
    print(i, load)


# In[ ]:





# In[ ]:




