from random import randint
import copy
from card import Card
from game_event import GameEvent

class Deck:
    def __init__(self, cards):
        self.max_size = 7
        self.cards = []
        self.initial_cards = []
        self.attacker_index = 0

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
    
    def has_card(self, card:Card):
        return card in self.cards
    
    def react_to_event(self, event: GameEvent):
        target_card = event.target
        if self.has_card(target_card):
            target_card.react_to_event(event)
        for card in [c for c in self.cards if c != target_card ]:
            card.react_to_event(event)

    def add(self, card, at_index):
        if len(self.cards) <= self.max_size - 1:
            self.cards = self.cards[:at_index] + [card] + self.cards[at_index:]

    def remove(self, card: Card):
        self.cards.remove(card)
        
    def index_of(self, card: Card):
        return self.cards.index(card)

    def has_minion(self, minion):
        return minion in self.cards
    
    def get_next_attacker(self) -> Card:
        if self.has_lost():
            raise Exception("the player has lost")
        if self.attacker_index + 1 > len(self.cards):
            return self.cards[-1]
        else:
            return self.cards[self.attacker_index]
    
    def increase_attacker_index(self):
        if self.attacker_index > len(self.cards):
                self.attacker_index = (self.attacker_index + 1) % len(self.cards)
        else:
            self.attacker_index += 1

    def defending_cards(self):
        if len(self.taunt_cards()) > 0:
            return self.taunt_cards()
        else:
            return self.alive_cards()

    def get_defender(self) -> Card:
        index = randint(0, len(self.defending_cards()) - 1)
        return self.defending_cards()[index]

    def has_lost(self):
        return len(self.alive_cards()) == 0

    def get_deck_string(self, debug=False):
        return '  ||  '.join([ c.get_stats_str(debug) for c in self.cards ])
    
    def __str__(self) -> str:
        return self.get_deck_string()

    def reset(self):
        self.cards = copy.deepcopy(self.initial_cards)
