#!/usr/bin/env python
# coding: utf-8

# In[166]:


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# In[167]:


def get_edges(wa, node, graph):
    #print('get edges: node:', node, 'graph:', graph)
    edges = []
    q = [(*node, 0)]
    visited = {node}
    while q:
        r, c, l = q.pop()

        if l != 0 and (r, c) in graph:
            edges.append({(node, (r, c)) : l})
            continue
            
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = np.add((r, c), d)
            if 0 <= nr < len(wa) and 0 <= nc < len(wa[0]) and wa[nr, nc] != '#' and (nr, nc) not in visited:
                q.append((nr, nc, l + 1))
                visited.add((nr, nc))


    return edges


# In[168]:


fn = "data/walk.txt"

walk = []
with open(fn) as fin:
    for line in fin:
        walk.append(list(line.strip()))

wa = np.array(walk)
#print(wa)
num_rows, num_cols = wa.shape

start_c = np.where(wa[0,:] == '.')[0][0]
start = (0, start_c)
end_c = np.where(wa[num_rows-1,:] == '.')[0][0]
end = (num_rows-1, end_c)
print('start:', start, 'end:', end)


# In[169]:


G = nx.Graph()
dirs = {'dirs' : []}
lengths = {'lengths' : []}
nx.set_node_attributes(G, dirs)
#nx.set_edge_attributes(G, lengths)
G.add_nodes_from([start, end])
G.nodes[start]['dirs'] = [(1, 0)]
G.nodes[end]['dirs'] = []

# scan the walk and add node were the path splits
for r in range(num_rows):
    for c in range(num_cols):
        if wa[r,c] == '#':
            continue
        neighbors = 0
        dirs = []
        for nr, nc in [(r-1,c), (r+1,c), (r, c-1), (r,c+1)]:
            if 0 <= nr < num_rows - 1 and 0 <= nc < num_cols - 1 and wa[nr,nc] != '#':
                dirs.append(tuple(np.subtract((nr, nc), (r, c))))
                neighbors += 1
        if neighbors >= 3:
            G.add_node((r,c))
            G.nodes[(r,c)]['dirs'] = dirs

print(G.nodes)


# In[ ]:


# Find edges and their length
for node in G.nodes:
    if len(G.nodes[node]['dirs']) > 0:
        edges = get_edges(wa, node, G.nodes)
        for edge in edges:
            #print('edge:', edge)
            e = list(edge.keys())[0]
            if e not in G.edges:
                G.add_edge(*e)
                G.edges[e]['lengths'] = list(edge.values())[0]
            
        #print('node:', node, 'edges:', edges)
#nx.draw_networkx(G)
path_len_list = []
for path in nx.all_simple_edge_paths(G, start, end):
    path_len = 0
    for edge in path:
        path_len += G.edges[edge]['lengths']
    path_len_list.append(path_len)

print('longest path: ', max(path_len_list))
nx.draw_networkx(G)


# In[ ]:




