#!/usr/bin/env python
# coding: utf-8

# In[65]:


from pprint import pprint
from collections import namedtuple
import numpy as np


# In[66]:


Point = namedtuple('Point', ['x', 'y'])
Tile = namedtuple('Dir', ['d', 'x', 'y'])

pipe_dict = {'|':{'N':Tile('N',  0, -1), 'S':Tile('S',  0,  1)},
             '-':{'E':Tile('E',  1,  0), 'W':Tile('W', -1,  0)},
             'L':{'S':Tile('E',  1,  0), 'W':Tile('N',  0, -1)},
             'J':{'S':Tile('W', -1,  0), 'E':Tile('N',  0, -1)},
             '7':{'N':Tile('W', -1,  0), 'E':Tile('S',  0,  1)},
             'F':{'N':Tile('E',  1,  0), 'W':Tile('S',  0,  1)}}


# In[67]:


fn = "data/pipes.txt"
pipes = []
with open(fn) as fin:
    for line in fin:
        pipes.append(list(line.strip()))
    pa = np.array(pipes)
    pprint(pa)


# In[68]:


# find start position
s = np.argwhere(pa == 'S')
p = Point(s[0][1], s[0][0])
print('start: ', p)


# In[69]:


# Go around start point and pick a direction with a valid pipe
np = None
for d in ('N', 'S', 'E', 'W'):
    if d == 'N':
        np = pa[p.y - 1][p.x]
        print('N', np)
        if np in ('|', '7', 'F'):
            break
    elif d == 'S':
        np = pa[p.y + 1][p.x] 
        print('S', np)
        if np in ('|', 'J', 'L'):
            break
    elif d == 'E':
        np = pa[p.y][p.x - 1]
        print('E', np)
        if np in ('-', '7', 'J'):
            break
    else:
        np = pa[p.y][p.x + 1]
        print('W', np)
        if np in ('-', 'F', 'L'):
            break
if np is None:
    print('No valid direction of travel found')
    exit()

print ('dir: ', d, 'next pt: ', np)


# In[70]:


vertices = [(p.x,p.y)]
b = 0
while np != 'S' and b < 1000000:
    if np in "7FJL":
        vertices.append((p.x, p.y))
    #print('x:', p.x, 'y:', p.y)
    #print ('cur dir: ', d, 'cur pipe: ', np)
    t = pipe_dict[np][d]
    d = t.d
    p = Point(p.x + t.x, p.y + t.y)
    np = pa[p.y][p.x]
    b += 1
#print(vertices)
print('b:', b)


# In[71]:


# calculate area using Shoelace
A = 0
for i in range(len(vertices)):
    A += (vertices[i][0] * vertices[(i+1) % len(vertices)][1] - vertices[(i+1) % len(vertices)][0] * vertices[i][1])
A = abs(A) // 2
print('A =', A)


# In[72]:


# use Pick's theorem to get internal area: i = A - b/2 + 1
area = A - (b//2) + 1
print('area = ', area)


# In[ ]:




