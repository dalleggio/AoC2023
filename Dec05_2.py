#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
            seed_data = list(map(int, line.split(':')[1].split()))
            seed_tuples = [(seed_data[i], seed_data[i+1]) for i in range(0, len(seed_data), 2)]
            pprint (seed_tuples)
        elif line.strip().endswith('map:'):
            # Start of new mapping section
            map_idx += 1
            maps.append([])
        elif line.strip() != '':
            # Load contents of mapping section while sorting by Source
            insort(maps[map_idx], Range_tuple(*list(map(int, line.split()))), key=by_source)
num_maps = len(maps)
dest = 0
locs = [None] * len(seed_tuples)

# Take seeds through mapping tables to find locations
for seed_tuple in seed_tuples:
    seed_tuple_idx = seed_tuples.index(seed_tuple)
    for seed in range(seed_tuple[0], sum(seed_tuple) + 1):
        for m in range(num_maps):
            source = seed if m == 0 else dest
            s = bisect(maps[m], source, key=by_source)
            if s > 0:
                delta = source - maps[m][s-1][1]
                if delta < maps[m][s-1][2]:
                    dest = maps[m][s-1][0] + delta
                else:
                    dest = source
            else:
                dest = source
        if locs[seed_tuple_idx] == None or dest < locs[seed_tuple_idx]:
            locs[seed_tuple_idx] = dest
            print('idx: ', seed_tuple_idx, dest)
            
    print('locs: ', locs)
print('closest loc: ', min(locs))


# In[ ]:





# In[ ]:




