from card import Card
from deathrattle.summon import Summon
import random
import json
import copy

class Minions:

    def card_from_json(self, card_json):

        if "deathrattle" in card_json:
            deathrattle_type = card_json["deathrattle"]["type"]
            if deathrattle_type == "summon":
                card = card_json["deathrattle"]["card"]
                deathrattle = Summon(self.card_from_json(card))
                del card_json["deathrattle"]
            else:
                raise Exception("Deathrattle not implemented")
        else:
            deathrattle = None

        return Card(**card_json, deathrattle=deathrattle)


    def __init__(self):

        f = open('minions.json')
        minion_data = json.loads(f.read())
        self.minion_pool = [ self.card_from_json(card_json) for card_json in minion_data['cards'] ]
        f.close()


    def get_random_minion_list(self, minions_count, max_level=None):
        minion_pool = [m for m in self.minion_pool if m.level <= max_level] if max_level else self.minion_pool
        return [random.choice(minion_pool) for m in range(minions_count)]

    def get_card_list_by_name(self, name_array):
        card_list = []
        for name in name_array:
            self.get_card_by_name(name)
        return card_list

    def get_card_by_name(self, name):
            for minion in self.minion_pool:
                if name == minion.name:
                    return copy.deepcopy(minion)

    
        
