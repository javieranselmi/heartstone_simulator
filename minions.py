from card import Card
import random

class Minions:
    def __init__(self):
        self.minion_pool = [
            Card("allycat",  1, 1, deathrattle=Card("tabycat",1,1)),  #bc
            Card("swabbie", 2, 2),
            Card("chroma", 1, 4),
            Card("imprisoner", 2, 2, taunt=True),
            Card("micromummy", 1, 2, deathrattle=Card("micromummy", 1, 1)),  #rb
            Card("mini-myrmidon", 3, 3),
            Card("picky eater", 2, 3),  #?
            Card("pupbot", 2, 1, divine_shield=True),
            Card("geomancer", 3, 1),
            Card("red whelp", 2, 2),
            Card("anomally", 1, 4),
            Card("rockpool", 2, 3),
            Card("scallywag", 3, 1, deathrattle=Card("pirate",1,1)),
            Card("hyena", 2, 2),
            Card("sellemental", 2, 2),
            Card("shell collector", 3, 1),
            Card("sun beaconer", 1, 2),
            Card("swamp striker", 1, 4),
            Card("wrath weaver", 1, 3),
            Card("Tavern Tipper", 2, 2),
        ]

    def get_random_minion_set(self, minions_count):
        return [random.choice(self.minion_pool) for m in range(minions_count)]

    def get_strongest_first_random_minion_set(self, minions_count):
        return sorted(self.get_random_minion_set(minions_count), key=lambda m: m.attack + m.hit_points, reverse=True)

