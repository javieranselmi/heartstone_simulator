import uuid
from card import Card
from game_event import GameEvent

class PostAttackEvent(GameEvent):
    
    def __init__(self, game, source: Card, target: Card):
        self.name = 'post_attack'
        self.game = game
        self.source = source
        self.target = target
        
    def __str__(self):
        return f"{self.name} event: {self.source} to {self.target}"
    