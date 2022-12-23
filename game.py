from random import randint

class Game:

    def __init__(self, player_1, player_2, verbose=False):
        self.player_1 = player_1
        self.player_2 = player_2
        self.turn = randint(0, 1) + 1
        self.game_status = 'ongoing'
        self.winner = None
        self.verbose = verbose

    def switch_turns(self):
        self.turn = 2 if self.turn == 1 else 1

    def make_attack(self):

        if (self.turn == 1):
            attacker_player =  self.player_1
            defender_player =  self.player_2
        else:
            attacker_player =  self.player_2
            defender_player =  self.player_1

        attacker = attacker_player.get_next_attacker()
        defender = defender_player.get_next_defender()

        if self.verbose:
            self.print_board_with_attack(
                attacker_player.name, 
                defender_player.name, 
                attacker.get_stats_str(), 
                defender.get_stats_str()
            )

        attacker.make_attack(defender)
        self.switch_turns()

        if attacker_player.has_lost() and defender_player.has_lost():
            self.game_status = 'tie'
        elif attacker_player.has_lost():
            self.game_status = 'winner'
            self.winner = defender_player.name
        elif defender_player.has_lost():
            self.game_status = 'winner'
            self.winner = attacker_player.name

    def print_board_with_attack(self, attacker_name, defender_name, attacker_card_stats, defender_card_stats):
        self.print_board()
        print(f"{attacker_name} will attack with {attacker_card_stats} card to {defender_name}'s {defender_card_stats}")
        print('\n')

    def print_board(self):
        print(f"Player 1 ({self.player_1.name}) board: ", self.player_1.board_string())
        print(f"Player 2 ({self.player_2.name}) board: ", self.player_2.board_string())

    def ended(self):
        return self.game_status in ["tie", "winner"]

    def print_winner(self):
        print(f'Game ended in {self.game_status} and winner is {self.winner}')

    def game_reset(self):
        self.player_1.reset()
        self.player_2.reset()
        
    def start_game(self):
        play = self.make_attack()
        round = 1
        while not self.ended():
            if self.verbose:
                print(f"Playing round {round}:")
            play = self.make_attack()
            round +=1

        if self.verbose:
            print(f"Final board:")
            self.print_board()
            self.print_winner()
        
        self.game_reset()
        return { "winner": self.winner, "game_status": self.game_status }
