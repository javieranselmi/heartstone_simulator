from deathrattle.deathrattle import Deathrattle
import copy

class Summon(Deathrattle):

    # TODO: Implement for multiple summoned minions.
    
    def __init__(self, card_to_summon, attack_immediately=False):
        self.card_to_summon = card_to_summon
        self.attack_immediately = attack_immediately # TODO: implement

    def execute(self, deck, index_of_defender):
        deck.add(card=copy.deepcopy(self.card_to_summon), at_index=index_of_defender)

    def get_description(self):
        return f'{self.card_to_summon.get_stats_str()}'