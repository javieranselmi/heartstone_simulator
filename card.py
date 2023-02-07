from defend_event import DefendEvent
from die_event import DieEvent

class Card:
    def __init__(self, name, level, attack, hit_points,
    taunt=False, divine_shield=False, poisonous=False, deathrattle=None):
        self.id = None
        self.name = name
        self.level = level
        self.attack = attack
        self.life = hit_points
        self.hit_points = hit_points
        self.is_alive = True
        self.taunt = taunt
        self.divine_shield = divine_shield
        self.deathrattle = deathrattle
        self.poisonous = poisonous
        self.played_index = None

    def react_to_event(self, event):
        # print("CARD", self.get_stats_str(), "REACTING TO EVENT", event)
        event_list = {
            'attack': self.react_to_attack,
            'defend': self.react_to_defend,
            'die': self.react_to_die,
            'remove': self.react_to_remove,
            'summon': self.react_to_summon,
            'pre_attack': self.react_to_pre_attack,
            'post_attack': self.react_to_post_attack
        }
        event_list[event.name](event)
        
    def is_dead(self):
        return self.life <= 0

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
            base_stats_str = base_stats_str + f'DTH<{self.deathrattle.get_stats_str()}>'

        return base_stats_str
    
    # Event reactions
    def __str__(self):
        return self.get_stats_str()

    def react_to_attack(self, event):
        if event.target == self:
            print(f"{event.source} -> {self}")
            event.game.react_to_event(DefendEvent(event.game, source=event.source, target=self))
            event.game.react_to_event(DefendEvent(event.game, source=self, target=event.source))
    
    def react_to_defend(self, event):
        if event.target == self:
            base_damage = event.source.attack
            if self.divine_shield:
                self.divine_shield = False
            elif base_damage >= self.life or event.source.poisonous:
                self.life = 0
                self.is_alive = False
            else:
                self.life -= base_damage
                
    def react_to_pre_attack(self, event):
        pass
    
    def react_to_post_attack(self, event):
        if self.is_dead():
            event.game.react_to_event(DieEvent(event.game, target=self))
          
    def react_to_die(self, event):
        if event.target == self:
            player, at_index = event.game.remove(self)
            if self.deathrattle is not None:
                event.game.summon(self, self.deathrattle, player, at_index)
                
    def react_to_summon(self, event):
        pass
    
    def react_to_remove(self, event):
        pass
            
