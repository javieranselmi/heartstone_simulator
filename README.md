## Summary

I built a heartstone simulator. You can use the Game class to simulate a game. You need to build an array of Card instances first, and then create two Player instances. You can assign a name and the array of Cards to the Player.

After that, you can create a Game and assign the two Players as player_1 and player_2.
Optionally, you can set verbose=True to see the progress of the game.

You can use the MultigameSimulator to run multiple games and gain statistics on which player won who.
This way you can perform statistical analysis on cards.

## Example
See simulation1.py to see a test in which I prove that statistically a player that puts its strongest cards first has more chance to win the game.

## To run simulation
python3 simulation1.py
