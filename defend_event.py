import uuid
from game_event import GameEvent

class DefendEvent(GameEvent):
    
    def __init__(self, game, source, target):
        self.name = 'defend'
        self.game = game
        self.source = source
        self.target = target
        
    def __str__(self):
        return f"{self.name} event: {self.target} from {self.source}"
    