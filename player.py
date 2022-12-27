from random import randint
from strategy import Strategy
import copy
from card import Card
from deck import Deck

class Player:
    def __init__(self, name: str, cards: list, strategy: Strategy):
        self.name = name
        self.deck = Deck(strategy.sort_cards(deck))


    def has_lost(self):
        return len(self.deck.alive_cards()) == 0


    def attack(self, player):
        attacker = self.deck.get_first()
        player.defend(attacker)

        if not attacker.is_alive:
            index_of_attacker = self.deck.remove(attacker)
            if attacker.deathrattle is not None:
                attacker.deathrattle.execute(self.deck, index_of_attacker)


    def get_deck_string(self, debug=False):
        return self.deck.get_deck_string(debug)


    def reset_deck(self):
        self.deck.reset()


    def defend(self, attacker):
        defender = self.deck.get_defender()
        attacker.make_attack(defender)

        if not defender_minion.is_alive:
            index_of_defender = self.deck.remove(defender)
            if defender_minion.deathrattle is not None:
                defender_minion.deathrattle.execute(self.deck, index_of_defender)
