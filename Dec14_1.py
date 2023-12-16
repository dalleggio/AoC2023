#!/usr/bin/env python
# coding: utf-8

# In[81]:


import numpy as np  


# In[82]:


fn = "data/rocks.txt"
rocks = []
with open(fn) as fin:
    for line in fin:
        rocks.append(list(line.strip()))
    ra = np.array(rocks)

print (ra)


# In[83]:


load = 0
num_rows, num_cols = ra.shape
for c in range(num_cols):
    col = ra[:, c]
    cube_locs = [i for i, x in enumerate(col) if x == '#']
    print(cube_locs)
    # count number of round rocks between North (row 0 and first cube rock
    if cube_locs:
        rounds = np.count_nonzero(col[:cube_locs[0]] == 'O')
        load += sum(num_rows - r for r in range(rounds))
    else:
        rounds = np.count_nonzero(col == 'O')
        load += sum(num_rows - r for r in range(rounds))
        continue
    
    # count number of round rocks between cube rocks
    for i in range(len(cube_locs) - 1):
        rounds = np.count_nonzero(col[cube_locs[i]:cube_locs[i+1]] == 'O')
        load += sum((num_rows - cube_locs[i] - 1 - r) for r in range(rounds))

    # count number of round rocks between last cube rock and South (last row)
    rounds = np.count_nonzero(col[cube_locs[-1]:num_rows] == 'O')
    load += sum((num_rows - cube_locs[-1] - 1 - r) for r in range(rounds))
print('load: ', load)


# In[ ]:




