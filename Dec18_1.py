#!/usr/bin/env python
# coding: utf-8

# In[15]:


fn = "data/lava.txt"
x = 0
y = 0
trench = [(0,0)]
trench_len = 0
with open(fn) as fin:
    for line in fin:
        dir, len_str, _ = line.strip().split()
        length = int(len_str)
        trench_len += length
        # get vertices of perimeter
        if dir == 'U':
            y -= length
        elif dir == 'D':
            y += length
        elif dir == 'R':
            x += length
        else:
            x -= length
        trench.append((x, y))

# Use Shoelace formula to get the area including half of the perimeter trench
area_sl = abs(sum((trench[i][0] * (trench[i+1][1] - trench[i-1][1])) for i in range(len(trench) - 1))) // 2

# Use Pick's theorem to substract the boundary and get the internal points
# Then add the full length of perimeter
area = area_sl - (trench_len // 2) + 1 + trench_len

print('lagoon vol:', area)



# In[ ]:




