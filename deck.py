from random import randint
from strategy import *
import copy
from card import Card

class Deck:

    def __init__(self, cards):
        self.max_size = 7
        self.cards = []
        self.initial_cards = []
        i = 1000
        for card in cards:
            new_card = copy.deepcopy(card)
            new_card.id = i
            self.cards.append(new_card)
            self.initial_cards.append(copy.deepcopy(new_card))
            i += 1


    def alive_cards(self):
        return [c for c in self.cards if c.is_alive]


    def taunt_cards(self):
        return [c for c in self.alive_cards() if c.taunt]


    def find_card_index_by_id(self, searched_card_id):
        index = 0
        for card in self.cards:
            if card.id == searched_card_id:
                return index
            index += 1


    def get_new_id(self):
        if len([ c.id for c in self.cards ]) > 0:
            return max([ c.id for c in self.cards ]) + 1
        else:
            return 1000


    def insert_by_index(self, card, index):
        if index < 0:
            # Don't do anything
            pass
        elif index > self.max_size:
           pass
        else:
            self.cards.insert(index, card)


    def add(self, card, at_index):
        id = self.get_new_id()
        card.id = id
        self.insert_by_index(card, at_index)


    def remove(self, card):
        card_index = self.find_card_index_by_id(card.id)
        del self.cards[card_index]
        return card_index


    def get_attacker(self):
        return self.cards[0]


    def _defending_cards(self):
        if len(self.taunt_cards()) > 0:
            return self.taunt_cards()
        else:
            return self.alive_cards()


    def get_defender(self):
        index = randint(0, len(self._defending_cards()) - 1)
        return self._defending_cards()[index]


    def has_lost(self):
        return len(self.alive_cards()) == 0


    def get_deck_string(self, debug=False):
        return '  ||  '.join([ c.get_stats_str(debug) for c in self.alive_cards() ])


    def reset(self):
        self.cards = copy.deepcopy(self.initial_cards)
