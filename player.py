from random import randint
import copy
from card import Card

class Player:

    def __init__(self, name, cards):
        self.name = name
        self.cards = [Card(**c) for c in cards]
        self.initial_cards = cards

    def alive_cards(self):
        return [c for c in self.cards if c.is_alive]

    def taunt_cards(self):
        return [c for c in self.alive_cards() if c.taunt]

    def defending_cards(self):
        if len(self.taunt_cards()) > 0:
            return self.taunt_cards()
        else:
            return self.alive_cards()

    def has_lost(self):
        return len(self.alive_cards()) == 0

    def board_string(self):
        return '  ||  '.join([ c.get_stats_str() for c in self.alive_cards() ])

    def reset(self):
        self.cards = [Card(**c) for c in self.initial_cards]

    def attack(self, player):
        attacker = self.cards.pop(0)
        # print(f"attacker {attacker.name} {attacker.get_stats_str()}")

        player.defend(attacker)

        if attacker.is_alive:
             self.cards.append(attacker)
        else:
            # print(f"attacker died {attacker.name} {attacker.get_stats_str()}")
            if attacker._deathrattle:
                # print("deathrattle!")
                self.cards.insert(0, attacker.deathrattle())


    def defend(self, attacker):
        if self.has_lost():
            return None

        index = randint(0, len(self.defending_cards()) - 1)
        defender = self.defending_cards()[index]

        # print(f"defender {defender.name} {defender.get_stats_str()}")

        attacker.make_attack(defender)

        if not defender.is_alive:
            # print(f"defender died {defender.name} {defender.get_stats_str()}")
            self.cards.pop(index)
            if defender._deathrattle:
                # print("deathrattle!")
                self.cards.insert(index, defender.deathrattle())
