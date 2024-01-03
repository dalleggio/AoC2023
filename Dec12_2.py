#!/usr/bin/env python
# coding: utf-8

# In[1]:


memo = {}

def count_arr(springs, broken):
    #print('count arr springs:', springs, 'broken:', broken)

    if springs == '':
        if broken == ():
            return 1
        else:
            return 0
            
    if broken == ():
        if '#' not in springs:
            return 1
        else:
            return 0

    if ((springs, broken)) in memo:
        return memo[(springs, broken)]
        
    result = 0
    if springs[0] in '.?':
        result += count_arr(springs[1:], broken)

    if springs[0] in '#?':
        if len(springs) >= broken[0] and not '.' in springs[:broken[0]] and (len(springs) == broken[0] or springs[broken[0]] != '#'):
            result += count_arr(springs[broken[0] + 1:], broken[1:])

    memo[(springs, broken)] = result
    #print(memo)
    return result


# In[2]:


fn = "data/springs.txt"

total_arr = 0
with open(fn) as fin:
    for line in fin:
        springs, broken_str = line.strip().split()
        broken = tuple(map(int, broken_str.split(',')))

        springs = '?'.join([springs] * 5)
        broken = broken * 5
        print('springs: ', springs, 'broken:', broken)

        arr = count_arr(springs, broken)
        print('num arr:', arr)
        total_arr += arr
        
    print('total num arr:', total_arr)


# In[ ]:





# In[ ]:




