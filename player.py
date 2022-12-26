from random import randint
from strategy import *
import copy
from card import Card

class Player:


    def __init__(self, name, deck):
        self.name = name
        self.deck = deck


    def has_lost(self):
        return len(self.deck.alive_cards()) == 0


    def attack(self, player):
        attacker = self.deck.get_first()
        defender = player.deck.get_defender()
        attacker.make_attack(defender)
        player.defend(attacker_minion=attacker, defender_minion=defender, attacker_player=self)
        
        if not attacker.is_alive:
            index_of_attacker = self.deck.remove(attacker)
            if attacker.deathrattle is not None:
                attacker.deathrattle.execute(self.deck, index_of_attacker)

    def get_deck_string(self, debug=False):
        return self.deck.get_deck_string(debug)

    def reset_deck(self):
        self.deck.reset()

    def defend(self, attacker_minion, defender_minion, attacker_player):
        if not defender_minion.is_alive:
            index_of_defender = self.deck.remove(defender_minion)
            if defender_minion.deathrattle is not None:
                defender_minion.deathrattle.execute(self.deck, index_of_defender)



