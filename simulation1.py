from minions import Minions
from game import Game
from card import Card
from player import Player
from deck import Deck
from multigame_simulator import MultigameSimulator
import random

# Step 1: Set the cards and their stats

minion_pool = Minions()
player1_cards = minion_pool.get_strongest_first_random_minion_set(3)
player2_cards = minion_pool.get_random_minion_set(3)
#player1_cards = minion_pool.get_card_list_by_name(["allycat", "micromummy"])
#player2_cards = minion_pool.get_card_list_by_name(["micromummy", "micromummy", 'micromummy'])

# Step 2: Set the players and their names.
player1 = Player("Fedex", Deck(player1_cards))
player2 = Player("Javi", Deck(player2_cards))

Game(player1,player2,verbose=True).print_board()
Game(player1,player2,verbose=True).start_game()

# Step 3: Run the multigame simulator

sim = MultigameSimulator(1000, player1, player2)
sim.run_all_games()

# OPTIONAL: If you want to only play one game, and see the output, uncomment the next line.
# Game(player1,player2,verbose=True).start_game()
