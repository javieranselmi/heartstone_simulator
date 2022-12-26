from random import randint

class Card:
    def __init__(self, name, attack, hit_points,
    taunt=False, divine_shield=False, poisonous=False, deathrattle=None):
        self.id = None
        self.name = name
        self.attack = attack
        self.life = hit_points
        self.hit_points = hit_points
        self.is_alive = True
        self.taunt = taunt
        self.divine_shield = divine_shield
        self.deathrattle = deathrattle
        self.poisonous = poisonous

    def make_attack(self, card):
            card.take_damage(self.attack, self.poisonous)
            self.take_damage(card.attack, card.poisonous)

    def take_damage(self, damage, poison=False):
        if self.divine_shield:
            self.divine_shield = False
        elif damage >= self.life or poison:
            self.life = 0
            self.is_alive = False
        else:
            self.life -= damage

    def get_stats_str(self, debug=False):
        if debug:
            base_stats_str = f'({self.attack},{self.life}:{self.id})'
        else:
            base_stats_str = f'({self.attack},{self.life})'
        if self.taunt:
            base_stats_str = base_stats_str.replace('(', '[')
            base_stats_str = base_stats_str.replace(')', ']')

        if self.divine_shield:
            base_stats_str = base_stats_str + '*'

        if self.poisonous:
            base_stats_str = base_stats_str + 'P'

        if self.deathrattle:
            base_stats_str = base_stats_str + f'DTH<{self.deathrattle.get_description()}>'

        return base_stats_str


