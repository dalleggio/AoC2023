#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pprint import pprint
from collections import namedtuple
games = []
possible_games = []
Game = namedtuple("Game", ["red", "green", "blue"])
bag = Game(12, 13, 14)
#pprint(bag)
with open("games.txt") as fin:
    for line in fin:
        games.append(line.split(':')[1].strip().split(';'))
    for game in games:
        print(games.index(game))
        print(game)
        possible = True
        for grab in game:
            rnum = 0
            gnum = 0
            bnum = 0
            pprint(grab)
            cubes = grab.split(',')
            pprint (cubes)
            for cube in cubes:
                [num, color] = cube.split()
                print(num, color)
                if color == 'red':
                    rnum = int(num)
                elif color == 'green':
                    gnum = int(num)
                else:
                    bnum = int(num)
            grab_tpl = Game(red=rnum, green=gnum, blue=bnum)
            pprint(grab_tpl)
            if grab_tpl[0] > bag[0] or grab_tpl[1] > bag[1] or grab_tpl[2] > bag[2]:
                possible = False
                print('impossible: ', grab_tpl)
                break
        if possible:
            possible_games.append(games.index(game) + 1)
            print(possible_games)
    print('possible games sum: ', sum(possible_games))


# In[ ]:




