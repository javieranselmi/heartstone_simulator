from strategy import Strategy
from deck import Deck


class Player:
    def __init__(self, name: str, cards: list, strategy: Strategy):
        self.name = name
        self.deck = Deck(strategy.sort_cards(cards))
        self.hand = Hand([])

    def has_lost(self):
        return len(self.deck.alive_cards()) == 0

    def attack(self, player):
        attacker = self.deck.get_next_attacker()
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

        if not defender.is_alive:
            index_of_defender = self.deck.remove(defender)
            if defender.deathrattle is not None:
                defender.deathrattle.execute(self.deck, index_of_defender)

    def __str__(self):
        return self.name
