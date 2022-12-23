from random import randint
import copy

class Player:

    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.initial_cards = copy.deepcopy(cards)

    def alive_cards(self):
        return [c for c in self.cards if c.is_alive ]

    def taunt_cards(self):
        return [c for c in self.alive_cards() if c.taunt ]
    
    def defending_cards(self):
        if len(self.taunt_cards()) > 0:
            return self.taunt_cards()
        else:
            return self.alive_cards()

    def has_lost(self):
        return len(self.alive_cards()) == 0

    def get_next_attacker(self):
        if self.has_lost():
            return None
        else: 
            return self.alive_cards()[0]

    def get_next_defender(self):
        if self.has_lost():
            return None
        else:
            index = randint(0, len(self.defending_cards()) - 1)
            return self.defending_cards()[index]

    def board_string(self):
        return '  ||  '.join([ c.get_stats_str() for c in self.alive_cards() ])

    def reset(self):
        self.cards = copy.deepcopy(self.initial_cards)

