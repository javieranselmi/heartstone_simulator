import uuid
class GameEvent:
    
    def __init__(self, name: str, game):
        self.name = name
        self.game = game
        
    def __str__(self):
        return self.name
    