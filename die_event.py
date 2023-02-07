from game_event import GameEvent

class DieEvent(GameEvent):
    
    def __init__(self, game, target):
        self.name = 'die'
        self.target = target
        self.game = game
        
    def __str__(self):
        return f"{self.name} event: {self.target}"
    