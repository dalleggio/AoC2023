#!/usr/bin/env python
# coding: utf-8

# In[24]:


num_scorecards = []
with open("cards.txt") as fin:
    for i, line in enumerate(fin):
        print('card ', i)
        all_nums = line.split(':')[1].split('|')
        winners = set(all_nums[0].split())
        card_nums = set(all_nums[1].split())
        num_matches = len(card_nums.intersection(winners))
        print('matches ', num_matches)
        # Add current card to count
        if len(num_scorecards) < i + 1:
            num_scorecards.append(1)
        else:
            num_scorecards[i] += 1
        print (i, num_scorecards[i])
        # Add counts to following cards according to number of matches for this card and its copies
        for j in range(num_matches):
            if len(num_scorecards) < i + j + 2:
                num_scorecards.append(num_scorecards[i])
            else:
                num_scorecards[i + j + 1] += num_scorecards[i]
            print (i + j + 1, num_scorecards[i + j + 1])
    total_cards = sum(num_scorecards)
    print ('total scorecards ', total_cards)


# In[ ]:




