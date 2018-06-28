#have subsequent rounds be casting each possible spell for each previous round in which:
# -player is alive AND boss is alive AND player has enough mana to cast a spell
from copy import deepcopy
import sys

#read input
lines = sys.stdin.read().split('\n')
boss_MAXHP = int(lines[0].split(': ')[1])
boss_DMG = int(lines[1].split(': ')[1])

player_MAXHP = 100
player_INITIALMANA = 500

spells = [
    'MagicMissile',
    'Drain',
    'Shield',
    'Poison',
    'Recharge'
]

class BattleOver(Exception):
    pass

class BattleRound:
    def __init__(self, player_HP, player_MANA, boss_HP):
        self.player_HP = player_HP
        self.player_MANA = player_MANA
        self.player_AMR = 0
        self.boss_HP = boss_HP
        self.effect_timers = {
            'shield': 0,
            'poison': 0,
            'recharge': 0,
        }
        self.total_mana_spent = 0

    def win(self):
        if (self.player_HP > 0) and (self.player_MANA > 0) and (self.boss_HP <= 0):
            return True
       
        return False

    def resolve_effects(self):
        #check shield
        if self.effect_timers['shield']:
            self.player_AMR = 7
            self.effect_timers['shield'] -= 1
        else:
            self.player_AMR = 0

        #check poison
        if self.effect_timers['poison']:
            self.damageBoss(3)
            self.effect_timers['poison'] -= 1

        #check recharge
        if self.effect_timers['recharge']:
            self.player_MANA += 101
            self.effect_timers['recharge'] -= 1

    def playerRound(self, spell):
        self.resolve_effects()
        getattr(self, 'cast' + spell)()

    def bossRound(self):
        self.resolve_effects()
        self.damagePlayer(max(boss_DMG - self.player_AMR, 1))

    def damageBoss(self, damage):
        self.boss_HP -= damage

        if self.boss_HP <= 0:
            raise BattleOver

    def damagePlayer(self, damage):
        self.player_HP -= damage

        if self.player_HP <= 0:
            raise BattleOver

    def spendMana(self, mana_cost):
        self.player_MANA -= mana_cost

        if self.player_MANA <= 0:
            raise BattleOver
        else:
            self.total_mana_spent += mana_cost

    def castMagicMissile(self):
        self.spendMana(53)
        self.damageBoss(4)

    def castDrain(self):
        self.spendMana(73)
        self.damageBoss(2)
        self.player_HP += 2

    def castShield(self):
        self.spendMana(113)
        self.effect_timers['shield'] = 6

    def castPoison(self):
        self.spendMana(173)
        self.effect_timers['poison'] = 6

    def castRecharge(self):
        self.spendMana(229)
        self.effect_timers['recharge'] = 5

previous_rounds = [BattleRound(player_MAXHP, player_INITIALMANA, boss_MAXHP)]
round_count = 0
finished = False
minimum_total_mana = 100000

while not finished:
    round_count += 1
    current_rounds = []

    for single_round in previous_rounds:
        for spell in spells:
            if single_round.effect_timers['shield'] and spell == 'Shield':
                continue
            if single_round.effect_timers['poison'] and spell == 'Poison':
                continue
            if single_round.effect_timers['recharge'] and spell == 'Recharge':
                continue
            try:
                new_round = deepcopy(single_round)
                new_round.playerRound(spell)
                new_round.bossRound()
                current_rounds.append(new_round)
            except BattleOver:
                if new_round.win():
                    minimum_total_mana = min(minimum_total_mana, single_round.total_mana_spent)

    previous_rounds = current_rounds
    print(round_count, len(current_rounds))
    
print(minimum_total_mana)