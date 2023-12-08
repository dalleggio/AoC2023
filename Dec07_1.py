#!/usr/bin/env python
# coding: utf-8

from pprint import pprint
from collections import namedtuple
from enum import Enum

Game = namedtuple('Game', ['hand', 'bid'])
# List of card values
card_list = [str(x) for x in range(2,10)] + ['T', 'J', 'Q', 'K', 'A']

def is_stronger(hand_a, hand_b):
    for i in range(len(hand_a)):
        if card_list.index(hand_a[i]) != card_list.index(hand_b[i]):
            if card_list.index(hand_a[i]) > card_list.index(hand_b[i]):
                return True
            else:
                return False                
    return False
            
def insort(ranked_list, game):
    if len(ranked_list) == 0:
        ranked_list.append(game)
        return(ranked_list)
    for r in reversed(ranked_list):
        if is_stronger(game.hand, r.hand):
            ranked_list.insert(ranked_list.index(r) + 1, game)
            break;
    else:
        ranked_list.insert(0, game)
    return(ranked_list)

# List to hold the number of card values in each hand
card_num = [0] * len(card_list)
# Dict to associate card counts with card values
hand_dict = dict(zip(card_list, card_num))
# Enum for hand types
class Type(Enum):
    HIGH = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE = 3
    FULL_HOUSE = 4
    FOUR = 5
    FIVE = 6
# Poker hand rank dict
poker_hand_rank = {(5,) : Type.FIVE, (1,4) : Type.FOUR, (2,3) : Type.FULL_HOUSE, \
                   (1,1,3) : Type.THREE, (1,2,2) : Type.TWO_PAIR, (1,1,1,2) : Type.ONE_PAIR, (1,1,1,1,1) : Type.HIGH}
# List to hold ranked hands
games_ranked = [[] for _ in range(len(poker_hand_rank))]
games = []
with open("poker.txt") as fin:
    for line in fin:
        games.append(Game(line.strip().split()[0], line.strip().split()[1]))
    #pprint(games)

for game in games:
    # Clear dict values but keep keys
    hand_dict = {k: 0 for k, v in hand_dict.items()}
    # Count number of cards of each type and store in dict
    for card in game.hand:
        hand_dict[card] += 1
    # Get a list representation of the number of groupings of cards (1, 2, 3, 4, or 5)
    num_list = []
    for num in (num for num in hand_dict.values() if num != 0):
        num_list.append(num)
    print (game.hand, tuple(sorted(num_list)))
    hand_rank = poker_hand_rank[tuple(sorted(num_list))]
    #print ('hand rank: ', hand_rank)
    games_ranked[hand_rank.value] = insort(games_ranked[hand_rank.value], game)
pprint (games_ranked)

# Traverse games_ranked lists and calculate total winnings
k = 1
total_win = 0
for i in range(len(games_ranked)):
    for j in range(len(games_ranked[i])):
        total_win += k * int(games_ranked[i][j].bid)
        k += 1
print('k: ', k)
print('total winnings: ', total_win)