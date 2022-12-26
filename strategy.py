from deck import Deck

class Strategy:
    def sort_cards(self, deck: Deck):
        pass


class Random(Strategy):
    def sort_cards(self, deck: Deck):
        return deck


class HighestAttackFirst(Strategy):
    def sort_cards(self, deck: Deck):
        deck.cards = sorted(deck.cards, key=lambda m: m.attack, reverse=True)
        return deck


class GraterCombinedStatsFirst(Strategy):
    def sort_cards(self, deck: Deck):
        deck.cards = sorted(deck.cards, key=lambda m: m.attack + m.hit_points, reverse=True)
        return deck

RANDOM = Random()
HIGHEST_ATTACK_FIRST = HighestAttackFirst()
GRATER_COMBINED_STATS_FIRST = GraterCombinedStatsFirst()
