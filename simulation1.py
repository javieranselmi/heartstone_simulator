from minions import Minions
from game import Game
from card import Card
from player import Player
from strategy import RANDOM, HIGHEST_ATTACK_FIRST, GRATER_COMBINED_STATS_FIRST
from multigame_simulator import MultigameSimulator
import random


# Step 1: list the cards and their stats
minion_pool = Minions()
player1_cards = minion_pool.get_random_minion_list(3)
player2_cards = minion_pool.get_random_minion_list(3)

# Step 2: Set the players and their names.
player1 = Player("Fedex", player1_cards, HIGHEST_ATTACK_FIRST)
player2 = Player("Javi", player2_cards, GRATER_COMBINED_STATS_FIRST)

Game(player1,player2,verbose=True).print_board()

# Step 3: Run the multigame simulator
sim1 = MultigameSimulator(10000,
    Player("Fedex", player1_cards, HIGHEST_ATTACK_FIRST),
    Player("Javi", player2_cards, GRATER_COMBINED_STATS_FIRST),
)
sim2 = MultigameSimulator(10000,
    Player("Fedex", player2_cards, HIGHEST_ATTACK_FIRST),
    Player("Javi", player1_cards, GRATER_COMBINED_STATS_FIRST),
)

sim1.run_all_games()
sim2.run_all_games()

# OPTIONAL: If you want to only play one game, and see the output, uncomment the next line.
#Game(player1,player2,verbose=True).start_game()
