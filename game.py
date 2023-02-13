from random import randint
from game_event import GameEvent
from remove_event import RemoveEvent
from summon_event import SummonEvent

class Game:

    def __init__(self, players, verbose=False):
        self.players = players
        self.turn = 0
        self.decider = randint(0, 1)
        self.game_status = 'ongoing'
        self.game_event_pile = []
        self.winner = None
        self.verbose = verbose
    
    def react_to_event(self, event: GameEvent):
        target_minion = event.target
        if self.players[0].has_minion(target_minion):
            self.players[0].deck.react_to_event(event)
            self.players[1].deck.react_to_event(event)
        else:
            self.players[1].deck.react_to_event(event)
            self.players[0].deck.react_to_event(event)
            
    def remove(self, card):
        if self.players[0].has_minion(card):
            at_index = self.players[0].deck.index_of(card)
            player = self.players[0]
        else:
            at_index = self.players[1].deck.index_of(card)
            player = self.players[1]
        player.deck.remove(card)
        self.react_to_event(RemoveEvent(self, target=card))
        return player, at_index
        
    def summon(self, source, card, player, at_index):
        player.deck.add(card, at_index)
        self.react_to_event(SummonEvent(self, source, card, at_index))

    def play_turn(self):
        self.turn += 1
        self.decider = (self.decider + 1) % 2

        attacker_player = self.players[self.decider]
        defender_player = self.players[(self.decider + 1) % 2]

        if self.verbose:
            print(f"{attacker_player.name} will attack {defender_player.name}")
            self.print_board()
            
        attacker_player.attack(defender_player, self)
        self.check_game_status()

    def check_game_status(self):
        if self.players[0].has_lost() and self.players[1].has_lost():
            self.game_status = 'tie'
        elif self.players[0].has_lost():
            self.game_status = 'winner'
            self.winner = self.players[1].name
        elif self.players[1].has_lost():
            self.game_status = 'winner'
            self.winner = self.players[0].name

    def print_board_with_attack(self, attacker_name, defender_name, attacker_card_stats, defender_card_stats):
        self.print_deck()
        print(f"{attacker_name} will attack with {attacker_card_stats} card to {defender_name}'s {defender_card_stats}")
        print('\n')

    def print_board(self, debug=False):
        print(f"Player 1 ({self.players[0].name}) deck: ", self.players[0].get_deck_string(debug))
        print(f"Player 2 ({self.players[1].name}) deck: ", self.players[1].get_deck_string(debug))

    def ended(self):
        return self.game_status in ["tie", "winner"]

    def print_winner(self):
        print(f'Game ended in {self.game_status} and winner is {self.winner}')

    def game_reset(self):
        for player in self.players:
            player.reset_deck()

    def start_game(self):
        while not self.ended():
            if self.verbose:
                print(f"\nPlaying round {self.turn}:")
            self.play_turn()

        if self.verbose:
            print(f"\nFinal board:")
            self.print_board()
            self.print_winner()

        self.game_reset()
        return { "winner": self.winner, "game_status": self.game_status }
