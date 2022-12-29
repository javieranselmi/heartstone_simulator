from random import randint
from game import Game

class MultigameSimulator:

    def __init__(self, amount_of_games, player1, player2):
        self.amount_of_games = amount_of_games
        self.games_results = []
        self.player1 = player1
        self.player2 = player2


    def run_all_games(self):
        for x in range(1, self.amount_of_games + 1):
            # print("Playing game", x)
            result = Game([self.player1, self.player2], verbose=False).start_game()
            self.games_results.append(result)
        self.print_statistics()


    def print_statistics(self):
        games_won_player_1 = 0
        games_won_player_2 = 0
        ties = 0
        for x in range(0, len(self.games_results)):
            if self.games_results[x]['winner'] == self.player1.name:
                games_won_player_1 += 1
            elif self.games_results[x]['winner'] == self.player2.name:
                games_won_player_2 += 1
            elif self.games_results[x]['game_status'] == 'tie':
                ties += 1
            else:
                raise Exception('Unexpected result')

        print(f"{self.player1.name} won {games_won_player_1} games ({ games_won_player_1 * 100/self.amount_of_games}% of games)")
        print(f"{self.player2.name} won {games_won_player_2} games ({ games_won_player_2 * 100/self.amount_of_games}% of games)")
        print(f"{ties} games ended in tie ({ ties * 100/self.amount_of_games}% of games).")


    def has_lost(self):
        return len(self.alive_cards()) == 0


    def get_next_attacker(self):
        if self.has_lost():
            return None
        else:
            return self.alive_cards()[0]


    def get_next_defender(self):
        if self.has_lost():
            return None
        else:
            index = randint(0, len(self.alive_cards()) - 1)
            return self.alive_cards()[index]


    def deck_string(self):
        return '  ||  '.join([ c.get_stats_str() for c in self.alive_cards() ])
