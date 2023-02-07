import uuid
from card import Card
from game_event import GameEvent

class AttackEvent(GameEvent):
    
    def __init__(self, game, source: Card, target: Card):
        self.name = 'attack'
        self.game = game
        self.source = source
        self.target = target
        
    def __str__(self):
        return f"{self.name} event: {self.source} to {self.target}"
    