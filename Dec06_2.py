#!/usr/bin/env python
# coding: utf-8

# In[16]:


from math import sqrt, ceil, floor, prod

def solve_quad(a, b, c):
    dis = b**2 - 4*a*c
    sroot = sqrt(dis)
    return ((-b - sroot)/(2*a), (-b + sroot)/(2*a))
    
with open("races.txt") as fin:
    time_info = fin.readline().split(':')[1].split()
    time_str = ''
    for s in time_info:
        time_str += s.strip()
    time = int(time_str)
    print(time)
    dist_info = fin.readline().split(':')[1].split()
    dist_str = ''
    for s in dist_info:
        dist_str += s.strip()
    dist = int(dist_str)

    print(dist)
    (t1f, t2f) = (solve_quad(-1, time, -dist)[0], solve_quad(-1, time, -dist)[1])
    print(t1f, t2f)
    t1 = int(t1f) - 1 if t1f.is_integer() else floor(t1f)
    t2 = int(t2f) + 1 if t2f.is_integer() else ceil(t2f)
    print(t1, t2)
    win_interval = t1 - t2 + 1
    print (win_interval)

    print('Total win: ', win_interval)


# In[ ]:





# In[ ]:





# In[ ]:




