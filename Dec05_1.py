#!/usr/bin/env python
# coding: utf-8

# In[2]:


from collections import namedtuple
from operator import attrgetter
from bisect import bisect, insort
from pprint import pprint
maps = []
map_idx = -1
Range_tuple = namedtuple('Range', ('dest', 'source', 'length'))
by_source = attrgetter('source')

# Load mapping data into tables
with open("maps.txt") as fin:
    for line in fin:
        if line.startswith('seeds:'):
            seeds = list(map(int, line.split(':')[1].split()))
            pprint (seeds)
        elif line.strip().endswith('map:'):
            # Start of new mapping section
            map_idx += 1
            maps.append([])
        elif line.strip() != '':
            # Load contents of mapping section while sorting by Source
            insort(maps[map_idx], Range_tuple(*list(map(int, line.split()))), key=by_source)
num_maps = len(maps)
dest = 0
locs = []

# Take seeds through mapping tables to find locations
for seed in seeds:
    print(seed)
    for m in range(num_maps):
        print('map: ', m)
        source = seed if m == 0 else dest
        s = bisect(maps[m], source, key=by_source)
        print('bisect: ', s)
        print('source range: ', maps[m][s-1][1], '-', maps[m][s-1][1] + maps[m][s-1][2])
        print('dest   range: ', maps[m][s-1][0], '-', maps[m][s-1][0] + maps[m][s-1][2])
        if s > 0:
            delta = source - maps[m][s-1][1]
            if delta < maps[m][s-1][2]:
                dest = maps[m][s-1][0] + delta
            else:
                dest = source
        else:
            dest = source
        print('delta: ', delta)
        print('dest: ', dest)
    locs.append(dest)
    print('locs: ', locs)
    print('closest loc: ', min(locs))


# In[ ]:




