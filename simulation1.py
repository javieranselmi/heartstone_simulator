from minions import Minions
from game import Game
from card import Card
from player import Player
from deck import Deck
from strategy import RANDOM, HIGHEST_ATTACK_FIRST, GRATER_COMBINED_STATS_FIRST
from multigame_simulator import MultigameSimulator
import random


# Step 1: list the cards and their stats
minion_pool = Minions()

player1_deck = Deck(minion_pool.get_random_minion_list(3))
player2_deck = Deck(minion_pool.get_random_minion_list(3))

# Step 2: Set the players and their names.
player1 = Player("Fedex", player1_deck, HIGHEST_ATTACK_FIRST)
player2 = Player("Javi", player2_deck, GRATER_COMBINED_STATS_FIRST)

Game(player1,player2,verbose=True).print_board()
Game(player1,player2,verbose=True).start_game()

# Step 3: Run the multigame simulator
sim1 = MultigameSimulator(10000, player1, player2)

sim1.run_all_games()

# OPTIONAL: If you want to only play one game, and see the output, uncomment the next line.
#Game(player1,player2,verbose=True).start_game()
