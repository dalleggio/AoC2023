#!/usr/bin/env python
# coding: utf-8

# In[1]:


score = 0
with open("cards.txt") as fin:
    for line in fin:
        all_nums = line.split(':')[1].split('|')
        winners = set(all_nums[0].split())
        card_nums = set(all_nums[1].split())
        num_matches = len(card_nums.intersection(winners))
        score += (2**(num_matches - 1) if num_matches > 0 else 0)
    print (score)


# In[ ]:




