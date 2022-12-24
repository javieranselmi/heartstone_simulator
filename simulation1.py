from minions import Minions
from game import Game
from player import Player
from multigame_simulator import MultigameSimulator
import random


# Step 1: Set the cards and their stats
minion_pool = Minions()
player1_cards = minion_pool.get_strongest_first_random_minion_set(3)
print(player1_cards)
player2_cards = minion_pool.get_random_minion_set(3)
print(player2_cards)

# Step 2: Set the players and their names.
player1 = Player("Fedex", player1_cards)
player2 = Player("Javi", player2_cards)

# Step 3: Run the multigame simulator
#sim = MultigameSimulator(10000, player1, player2)
#sim.run_all_games()

# OPTIONAL: If you want to only play one game, and see the output, uncomment the next line.
Game(player1,player2,verbose=True).start_game()
