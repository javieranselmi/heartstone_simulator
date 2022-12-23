from minions import minions
from game import Game
from player import Player
from multigame_simulator import MultigameSimulator
import random

minions_count = 3

# Step 1: Set the cards and their stats
player1_cards = [random.choice(minions) for m in range(minions_count)]
player1_cards.sort(key= lambda m: m.attack, reverse=True)
player2_cards = [random.choice(minions) for m in range(minions_count)]

# Step 2: Set the players and their names.
player1 = Player("Fedex", player1_cards)
player2 = Player("Javi", player2_cards)

# Step 3: Run the multigame simulator
#sim = MultigameSimulator(10000, player1, player2)
#sim.run_all_games()

# OPTIONAL: If you want to only play one game, and see the output, uncomment the next line.
Game(player1,player2,verbose=True).start_game()
