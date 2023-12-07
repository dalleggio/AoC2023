#!/usr/bin/env python
# coding: utf-8

# In[5]:


from pprint import pprint
from collections import namedtuple
games = []
possible_games = []
Game = namedtuple("Game", ["red", "green", "blue"])
bag = Game(12, 13, 14)
power = 0
#pprint(bag)
with open("games.txt") as fin:
    for line in fin:
        games.append(line.split(':')[1].strip().split(';'))
    for game in games:
        print(games.index(game))
        print(game)
        rnum = 0
        gnum = 0
        bnum = 0
        for grab in game:
            pprint(grab)
            cubes = grab.split(',')
            pprint (cubes)
            for cube in cubes:
                [num, color] = cube.split()
                print(num, color)
                if color == 'red':
                    rnum = max(rnum, int(num))
                elif color == 'green':
                    gnum = max(gnum, int(num))
                else:
                    bnum = max(bnum, int(num))
        print('max: ', rnum, gnum, bnum, 'p: ', rnum*gnum*bnum)
        power += (rnum * gnum * bnum)
        print('total power: ', power)


# In[ ]:




