from minions import Minions

#One	    19
#Two	    27
#Three	    27
#Four	    24
#Five	    24
#Six	    21

class ShopInventory():

    def __init__(self):

            self.default_stocks =  {
                1: 15,
                2: 15,
                3: 13,
                4: 11,
                5: 9,
                6: 7
            }
            self.default_
            self.inventory = []
            minions =  Minions() 
            for m in Minions().minion_pool:
                for i in self.default_stocks[m.level]:
                    self.inventory.append(m)
        

    def purchased_minion(self, minion_name):
        index = [ x.name for x in self.inventory].index(minion_name)
        del self.inventory[index]
        return index

    def sold_minion(self, minion_name):
        card = Minions().get_card_by_name(minion_name)
        self.inventory.append(card)
