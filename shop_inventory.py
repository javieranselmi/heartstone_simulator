from minions import Minions
from collections import Counter
import random

class ShopInventory():

    def __init__(self):

        self.default_stocks =  {
            1: 15, # level 1 gets 15 copies of each minion
            2: 15, # level 2 gets 15 copies of each minion... and so on
            3: 13,
            4: 11,
            5: 9,
            6: 7
        }
        self.default_minions_per_level =  {
            1: 3, # level 1 gets 3 minions when roll
            2: 4, # level 2 gets 4 minions when roll... and so on
            3: 4,
            4: 5,
            5: 5,
            6: 6
        }
        self.minion_pool = Minions()
        self.inventory = []
        for m in self.minion_pool.minion_pool:
            for i in range(self.default_stocks[m.level]):
                self.inventory.append(m)
    

    def remove_minions(self, minion_names):
        for minion_name in minion_name:
            index = [ x.name for x in self.inventory].index(minion_name)
            del self.inventory[index]
        return

    def add_minions(self, minion_names):
        for minion_name in minion_names:
            card = Minions.get_card_by_name(minion_name)
            self.inventory.append(card)
        return

    def print_inventory(self):
        count_dict = dict(Counter(map(lambda x:x.name, self.inventory)))
        output = ''
        for key in count_dict:
            output += f'{key}: {count_dict[key]}\n'
        print(output)

    def get_new_roll(self, previous_minions, current_level, override_amount=None ):
        amount_to_retrieve = self.default_minions_per_level[current_level] if override_amount is None else override_amount
        self.add_minions(self, [ m.name for m in previous_minions ])
        available_minions = [m for m in self.inventory if m.level <= current_level]
        minions = [random.choice(available_minions) for m in range(amount_to_retrieve)]
        self.remove_minions(self, [ m.name for m in minions ])
        
