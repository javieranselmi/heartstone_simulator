from card import Card
from game_event import GameEvent

class RemoveEvent(GameEvent):
    
    def __init__(self, game, target: Card):
        self.name = 'remove'
        self.game = game
        self.target = target
        
    def __str__(self):
        return f"{self.name} event: {self.target}"
    