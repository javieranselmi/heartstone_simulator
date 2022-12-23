from random import randint

class Card:
    def __init__(self, name, attack, start_life, taunt=False, divine_shield=False):
        self.name = name
        self.attack = attack
        self.life = start_life
        self.start_life = start_life
        self.is_alive = True
        self.taunt = taunt

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
