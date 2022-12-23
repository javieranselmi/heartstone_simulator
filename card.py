from random import randint

class Card:
    def __init__(self, attack, start_life):
        self.attack = attack
        self.life = start_life
        self.start_life = start_life
        self.is_alive = True
    
    def make_attack(self, card):
        card.take_damage(self.attack)
        self.take_damage(card.attack)

    def take_damage(self, damage):
        if damage >= self.life:
            self.life = 0
            self.is_alive = False
        else:
            self.life -= damage

    def get_stats_str(self):
        return f'({self.attack}, {self.life})'
