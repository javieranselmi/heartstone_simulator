from card import Card
from deathrattle.summon import Summon
import random

class Minions:
    def __init__(self):
        self.minion_pool = [
            Card("allycat",  1, 1, deathrattle=Summon(Card("tabycat",1,1))),  #bc
            Card("swabbie", 2, 2),
            Card("chroma", 1, 4),
            Card("imprisoner", 2, 2, taunt=True),
            Card("micromummy", 1, 2, deathrattle=Summon(Card("micromummy", 1, 1))),  #rb
            Card("mini-myrmidon", 3, 3),
            Card("picky eater", 2, 3),  #?
            Card("pupbot", 2, 1, divine_shield=True),
            Card("geomancer", 3, 1),
            Card("red whelp", 2, 2),
            Card("anomally", 1, 4),
            Card("rockpool", 2, 3),
            Card("scallywag", 3, 1, deathrattle=Summon(Card("pirate",1,1))),
            Card("hyena", 2, 2),
            Card("sellemental", 2, 2),
            Card("shell collector", 3, 1),
            Card("sun beaconer", 1, 2),
            Card("swamp striker", 1, 4),
            Card("wrath weaver", 1, 3),
            Card("Tavern Tipper", 2, 2),
        ]


    def get_random_minion_list(self, minions_count):
        return [random.choice(self.minion_pool) for m in range(minions_count)]

    def get_card_list_by_name(self, name_array):
        card_list = []
        for name in name_array:
            for minion in self.minion_pool:
                if name == minion.name:
                    card_list.append(minion)
                    break
        return card_list
