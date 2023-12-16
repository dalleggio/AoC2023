#!/usr/bin/env python
# coding: utf-8

# In[33]:


def hashmap(s):
    curr_val = 0
    for c in s:
        #print('c: ', c, 'curr_val: ', curr_val)
        curr_val += ord(c)
        curr_val = (17 * curr_val) % 256
    return curr_val


# In[34]:


fn = "data/hash.txt"

with open(fn) as fin:
    str = fin.readline().split(',')
#print (str)


# In[35]:


sum = 0
for s in str:
    #print(s)
    hm = hashmap(s)
    sum += hm
print('sum: ', sum)


# In[ ]:




