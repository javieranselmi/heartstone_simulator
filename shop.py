from shop_inventory import ShopInventory
from player import Player

class Shop():

    def __init__(self, shop_inventory: ShopInventory, player: Player):

        self.shelf = []
        self.player = player
        self.shop_inventory = shop_inventory
        self.gold = 3
        self.level = 1
        self.shop_inventory.get_new_roll([], self.level)
        self.current_tier = 1
        self.turn = 1
        self.upgrade_base_cost = {
            2:	5,
            3:	7,
            4:	8,
            5:	9,
            6:	10
        }

    def get_roll(self):
        self.shop_inventory.get_new_roll(self.shelf, self.level)
    
    def can_upgrade(self):
        return self.current_tier < 6 and self.gold >= self.tier_upgrade_cost(self.current_tier + 1)

    def tier_upgrade_cost(self, tier):
        if tier in self.upgrade_base_cost:
            return self.upgrade_base_cost[tier]
        else:
            return None

    def upgrade(self):
        if self.can_upgrade():
            self.current_tier += 1
            self.decrease_gold(self.tier_upgrade_cost(self.current_tier+1))

    def can_buy(self, minion):
        return self.gold > minion.cost()

    def increase_gold(self, amount):
        self.gold += amount
    
    def decrease_gold(self, amount):
        self.gold -= amount

    def buy_minion(self, index):
        card = self.shelf[index]
        if self.can_buy(card):
            self.player.add_to_hand(card)
            del self.shelf[index]
            self.decrease_gold(card.cost())

    def sell_minion(self, index):
        card = self.player.get_card_from_hand(index)
        self.shop_inventory.add_minions(card)
        self.remove_from_hand(index)
        self.increase_gold(1)


