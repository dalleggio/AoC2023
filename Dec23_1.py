#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pprint import pprint
import numpy as np
from queue import Queue


# In[2]:


fn = "data/walk.txt"

walk = []
with open(fn) as fin:
    for line in fin:
        walk.append(list(line.strip()))

wa = np.array(walk)
print(wa)
num_rows, num_cols = wa.shape

start_c = np.where(wa[0,:] == '.')[0][0]
start = (0, start_c)
end_c = np.where(wa[num_rows-1,:] == '.')[0][0]
end = (num_rows-1, end_c)
print('start:', start, 'end:', end)


# In[3]:


path_q = Queue()
path_q.put((*start, 'D', 0))
len_list = []
visited = set()
while not path_q.empty():
    r, c, d, l = path_q.get()
    print('q get:', r, c, d, l)
    # walk in a direction until we hit the forest (#)
    while (r, c) not in visited:
        #print('s:', r, c, wa[r, c], d, l)
        visited.add((r,c))
        
        if (r, c) == end:
            len_list.append(l)
            visited.clear()
            break

        l += 1

        found_path = False
        
        if d == 'U':
            if r > 0 and wa[r-1,c] not in ('#', 'v'):
                r -= 1
                found_path = True
            if c > 0 and wa[r, c-1] not in ('#', '>'):
                if not found_path:
                    d = 'L'
                    c -= 1
                    found_path = True
                elif r > 0 and wa[r-1,c] not in ('#', 'v'):
                    print('q put:', (r, c - 1, 'L', l+1))
                    path_q.put((r, c - 1, 'L', l+1))
            if c < num_cols - 1 and wa[r, c+1] not in ('#', '<'):
                if not found_path:
                    d = 'R'
                    c += 1
                    found_path = True
                elif r > 0 and wa[r-1,c] not in ('#', 'v'):
                    print('q put:', (r, c + 1, 'R', l+1))
                    path_q.put((r, c + 1, 'R', l+1))
            if not found_path:
                break
            
        elif d == 'D':
            if r < num_rows - 1 and wa[r+1,c] not in ('#', '^'):
                r += 1
                found_path = True
            if c > 0 and wa[r, c-1] not in ('#', '>'):
                if not found_path:
                    d = 'L'
                    c -= 1
                    found_path = True
                elif r < num_rows - 1 and wa[r+1,c] not in ('#', '^'):
                    print('q put:', (r, c - 1, 'L', l+1))
                    path_q.put((r, c - 1, 'L', l+1))
            if c < num_cols - 1 and wa[r, c+1] not in ('#', '<'):
                if not found_path:
                    d = 'R'
                    c += 1
                    found_path = True
                elif r < num_rows - 1 and wa[r+1, c] not in ('#', '^'):
                    print('q put:', (r, c + 1, 'R', l+1))
                    path_q.put((r, c + 1, 'R', l+1))
            if not found_path:
                break;
            
        elif d == 'R':
            if c < num_cols - 1 and wa[r,c+1] not in ('#', '<'):
                c += 1
                found_path = True
            if r > 0 and wa[r - 1, c] not in ('#', 'v'):
                if not found_path:
                    d = 'U'
                    r -= 1
                    found_path = True
                elif c < num_cols - 1 and wa[r,c+1] not in ('#', '<'):
                    print('q put:', (r - 1, c, 'U', l+1))
                    path_q.put((r - 1, c, 'U', l+1))
            if r < num_rows - 1 and wa[r + 1, c] not in ('#', '^'):
                if not found_path:
                    d = 'D'
                    r += 1
                    found_path = True
                elif c < num_cols - 1 and wa[r,c+1] not in ('#', '<'):
                    print('q put:', (r + 1, c, 'D', l+1))
                    path_q.put((r + 1, c, 'D', l+1))
            if not found_path:
                break;

        else:
            if c > 0 and wa[r,c-1] not in ('#', '>'):
                c -= 1
                found_path = True
            if r > 0 and wa[r - 1, c] not in ('#', 'v'):
                if not found_path:
                    d = 'U'
                    r -= 1
                    found_path = True
                elif c > 0 and wa[r,c-1] not in ('#','>'):
                    print('q put:', (r - 1, c, 'U', l+1))
                    path_q.put((r - 1, c, 'U', l+1))
            if r < num_rows - 1 and wa[r + 1, c] not in ('#', '^'):
                if not found_path:
                    d = 'D'
                    r += 1
                    found_path = True
                elif c > 0 and wa[r,c-1] not in ('#','>'):
                    print('q put:', (r + 1, c, 'D', l+1))
                    path_q.put((r + 1, c, 'D', l+1))
            if not found_path:
                break

print('paths:', len_list)
print('max path:', max(len_list))

