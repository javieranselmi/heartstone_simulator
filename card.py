from random import randint

class Card:
    def __init__(self, name, attack, hit_points,
    taunt=False, divine_shield=False, deathrattle=None):
        self.name = name
        self.attack = attack
        self.life = hit_points
        self.hit_points = hit_points
        self.is_alive = True
        self.taunt = taunt
        self.divine_shield = divine_shield
        self._deathrattle = deathrattle

    def make_attack(self, card):
            card.take_damage(self.attack)
            self.take_damage(card.attack)

    def take_damage(self, damage):
        if self.divine_shield:
            self.divine_shield = False
        elif damage >= self.life:
            self.life = 0
            self.is_alive = False
        else:
            self.life -= damage

    def get_stats_str(self):
        base_stats_str = f'({self.attack}, {self.life})'
        if self.taunt:
            base_stats_str = base_stats_str.replace('(', '[')
            base_stats_str = base_stats_str.replace(')', ']')

        if self.divine_shield:
            base_stats_str = base_stats_str + '*'

        return base_stats_str

    def deathrattle(self):
        return Card(**self._deathrattle)
