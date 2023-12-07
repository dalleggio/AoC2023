#!/usr/bin/env python
# coding: utf-8

# In[7]:


import re
calib_sum = 0
with open("calib.txt") as fin:
    for line in fin:
        digit1 = int(re.search(r'\d', line).group())
        digit2 = int(re.search(r'\d', line[::-1]).group())
        calib_value = 10 * digit1 + digit2
        calib_sum += calib_value
    print('calib sum ', calib_sum)


# In[ ]:




