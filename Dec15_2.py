#!/usr/bin/env python
# coding: utf-8

# In[69]:


def hashmap(s):
    curr_val = 0
    for c in s:
        #print('c: ', c, 'curr_val: ', curr_val)
        curr_val += ord(c)
        curr_val = (17 * curr_val) % 256
    return curr_val


# In[67]:


fn = "data/hash.txt"

with open(fn) as fin:
    str = fin.readline().split(',')
#print (str)


# In[70]:


boxes = [{} for _ in range(256)]
sum = 0
for s in str:
    rmv = s.endswith('-')
    # label
    l = s[:-1] if rmv else s[:-2]
    # focal length
    if not rmv:
        fl = int(s[-1])
    b = hashmap(l)
    #print('box: ', b)
    # if not removing, replace or add new label
    if not rmv:
        boxes[b][l] = fl
    else:
        # remove label if it exists in box b
        boxes[b].pop(l, None)
#print(boxes)

# loop through boxes to calculate focusing power
for b in range(256):
    for i, l in enumerate(boxes[b]):
        sum += ((b + 1) * (i + 1) * boxes[b][l]) 
print('sum: ', sum)


# In[ ]:




