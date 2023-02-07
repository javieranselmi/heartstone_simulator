from strategy import Strategy
from deck import Deck
from attack_event import AttackEvent
from pre_attack_event import PreAttackEvent
from post_attack_event import PostAttackEvent


class Player:
    def __init__(self, name: str, cards: list, strategy: Strategy):
        self.name = name
        self.deck = Deck(strategy.sort_cards(cards))

    def has_lost(self):
        return len(self.deck.alive_cards()) == 0
    
    def has_minion(self, minion):
        return self.deck.has_minion(minion)
    
    def attack(self, player, game):
        attacker = self.deck.get_next_attacker()
        defender = player.get_defender()
        # Fases of the attack:
        game.react_to_event(PreAttackEvent(game, source=attacker, target=defender))
        game.react_to_event(AttackEvent(game, source=attacker, target=defender))
        game.react_to_event(PostAttackEvent(game, source=attacker, target=defender))
        self.deck.increase_attacker_index()

    def get_deck_string(self, debug=False):
        return self.deck.get_deck_string(debug)

    def reset_deck(self):
        self.deck.reset()
        
    def get_defender(self):
        return self.deck.get_defender()

    def __str__(self):
        return self.name
