# 1.) Calculate lowest stats needed to win
#     -Cheapest gear correlates to least stat bonuses
#     a.) Most possible rounds is min(playerHP, bossHP) 
#     b.) # of rounds is min(boss_HP / (player_DMG - boss_AMR), player_HP / (boss_DMG - player_AMR))
#     c.) Player wins if rounds * (player_DMG - boss_AMR) >= boss_HP
#         AND if (rounds - 1) * (boss_DMG - player_AMR) < player_HP
# 2.) Calculate cheapest gear set to achieve calculated stats

#After viewing reddit solution, probably simpler to calculate all possible gear combos and pick most expensive losing one

from math import ceil
from itertools import product
import sys

def win(player_MAXHP, player_DMG, player_AMR, boss_MAXHP, boss_DMG, boss_AMR):
    if ceil(boss_MAXHP / (max(player_DMG - boss_AMR, 1))) <= ceil(player_MAXHP / (max(boss_DMG - player_AMR, 1))):
        #player wins
        return True
    else:
        return False

def set_stats(equipment_set):
    cost = sum([item[1] for item in equipment_set])
    dam  = sum([item[2] for item in equipment_set])
    amr  = sum([item[3] for item in equipment_set])

    return (cost, dam, amr)

#key: (cost, dmg, amr)
weapon = [
    ('Dagger',       8  , 4, 0),
    ('Shortsword',   10 , 5, 0),
    ('Warhammer',    25 , 6, 0),
    ('Longsword',    40 , 7, 0),
    ('Greataxe',     74 , 8, 0)
]

armor = [
    ('No Armor',         0  , 0, 0),
    ('Leather',      13 , 0, 1),
    ('Chainmail',    31 , 0, 2),
    ('Splintmail',   53 , 0, 3),
    ('Bandedmail',   75 , 0, 4),
    ('Platemail',    102, 0, 5)
]

ring = [
    ('Damage +1',     25 , 1, 0),
    ('Damage +2',     50 , 2, 0),
    ('Damage +3',     100, 3, 0),
    ('Defense +1',    20 , 0, 1),
    ('Defense +2',    40 , 0, 2),
    ('Defense +3',    80 , 0, 3),
    ('Bare R Hand',   0  , 0, 0),
    ('Bare L Hand',   0  , 0, 0)
]

MAX_player_DMG = 13
MAX_player_AMR = 10

player_MAXHP = 100

parsed_input = [item.split(': ') for item in sys.stdin.read().split('\n')]
boss_MAXHP = int(parsed_input[0][1])
boss_DMG = int(parsed_input[1][1])
boss_AMR = int(parsed_input[2][1])

#generate all possible armor sets, with right hand ring not equal to left hand ring
equipment_sets = [x for x in list(product(weapon, armor, ring, ring)) if x[2] != x[3]]

max_set_cost = 0
for equipment_set in equipment_sets:
    set_cost, player_DMG, player_AMR = set_stats(equipment_set)

    if not win(player_MAXHP, player_DMG, player_AMR, boss_MAXHP, boss_DMG, boss_AMR):
        if set_cost > max_set_cost:
            max_set_cost = set_cost

print(max_set_cost)