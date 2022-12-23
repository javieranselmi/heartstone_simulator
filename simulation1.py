from card import Card
from game import Game
from player import Player
from multigame_simulator import MultigameSimulator

# Step 1: Set the cards and their stats
player1_cards = [ Card(3,3, taunt=True),  Card(1,1), Card(2,2)]
player2_cards = [ Card(1,1),  Card(3,3), Card(2,2, taunt=True, divine_shield=True)]

# Step 2: Set the players and their names.
player1 = Player("Fedex", player1_cards)
player2 = Player("Javi", player2_cards)

# Step 3: Run the multigame simulator
#sim = MultigameSimulator(10000, player1, player2)
#sim.run_all_games()

# OPTIONAL: If you want to only play one game, and see the output, uncomment the next line.
Game(player1,player2,verbose=True).start_game()
