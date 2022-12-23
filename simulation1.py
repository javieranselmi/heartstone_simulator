from card import Card
from game import Game
from player import Player
from multigame_simulator import MultigameSimulator

player1_cards = [ Card(3,3),  Card(1,1), Card(2,2)]
player2_cards = [ Card(1,1),  Card(3,3), Card(2,2)]
player1 = Player("Fedex", player1_cards)
player2 = Player("Javi", player2_cards)
sim = MultigameSimulator(10000, player1, player2)
sim.run_all_games()
#Game(player1,player2,verbose=True).start_game()
