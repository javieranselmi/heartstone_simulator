class Strategy:
    def sort_cards(self, cards: list):
        pass


class Random(Strategy):
    def sort_cards(self, cards: list):
        return cards


class HighestAttackFirst(Strategy):
    def sort_cards(self, cards: list):
        return sorted(cards, key=lambda m: m.attack, reverse=True)


class GraterCombinedStatsFirst(Strategy):
    def sort_cards(self, cards: list):
        return sorted(cards, key=lambda m: m.attack + m.hit_points, reverse=True)

RANDOM = Random()
HIGHEST_ATTACK_FIRST = HighestAttackFirst()
GRATER_COMBINED_STATS_FIRST = GraterCombinedStatsFirst()
