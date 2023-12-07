#!/usr/bin/env python
# coding: utf-8

# In[28]:


from math import sqrt, ceil, floor, prod

def solve_quad(a, b, c):
    dis = b**2 - 4*a*c
    sroot = sqrt(dis)
    return ((-b - sroot)/(2*a), (-b + sroot)/(2*a))
    
with open("races.txt") as fin:
    times = list(map(int, fin.readline().split(':')[1].split()))
    dists = list(map(int, fin.readline().split(':')[1].split()))
    print(times)
    print(dists)
    num_races = len(times)
    wins = [0] * num_races
    for race in range(num_races):
        (t1f, t2f) = ((solve_quad(-1, times[race], -dists[race])[0]), (solve_quad(-1, times[race], -dists[race])[1]))
        print(t1f, t2f)
        t1 = int(t1f) - 1 if t1f.is_integer() else floor(t1f)
        t2 = int(t2f) + 1 if t2f.is_integer() else ceil(t2f)
        print(t1, t2)
        win_interval = t1 - t2 + 1
        print (win_interval)
        wins[race] = win_interval
    print(wins)
    print('Total wins: ', prod(wins))


# In[ ]:




