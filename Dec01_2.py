#!/usr/bin/env python
# coding: utf-8

# In[19]:


import re
num_digits = list(range(1,10))
word_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits_lst = [str(d) for d in num_digits] + word_digits
digit_dict = dict(zip(word_digits, num_digits))
calib_sum = 0
with open("calib.txt") as fin:
    for line in fin:
        digits = re.findall(r"(?=("+'|'.join(digits_lst)+r"))", line)
        digit1 = int(digits[0]) if digits[0].isnumeric() else digit_dict[digits[0]]
        digit2 = int(digits[-1]) if digits[-1].isnumeric() else digit_dict[digits[-1]]
        calib_value = 10 * digit1 + digit2
        calib_sum += calib_value
    print('calib sum ', calib_sum)


# In[ ]:




