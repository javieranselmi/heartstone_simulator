from card import Card
from game_event import GameEvent

class SummonEvent(GameEvent):
    
    def __init__(self, game, source: Card, card:Card, at_index: int):
        self.name = 'summon'
        self.game = game
        self.source = source
        self.target = card
        self.card = source
        self.at_index = at_index
        
    def __str__(self):
        return f"{self.name} event: {self.card} at {self.at_index}"
    