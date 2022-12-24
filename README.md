## Summary

I built a Heartstone simulator. You can use the Game class to simulate a game. You need to build an array of Card instances first, and then create two Player instances. You can assign a name and the array of Cards to the Player.

After that, you can create a Game and assign the two Players as player_1 and player_2.
Optionally, you can set verbose=True to see the progress of the game.

You can use the MultigameSimulator to run multiple games and gain statistics on which player won who.
This way you can perform statistical analysis on cards.

## Example
See simulation1.py to see a test in which I prove that statistically a player that puts its strongest cards first has more chance to win the game.

## Taunt
If you want a card to have Taunt (has to be attacked first before other cards can be attacked), instantiate the Card with taunt=True. It is an optional parameter and the default is False.

Note: When cards with Taunt are displayed on the Verbose mode when running a game, they will be shown with brackets. For example a (3,3) with Taunt will be shown as [3,3].

## Divine Shield
If you want a card to have Divine Shield (if the card is attacking or if it receives damage it will ignore damage taken but still inflict its attack as damage to the attacking card, and lose its shield), instantiate the Card with divine_shield=True. It is an optional parameter and the default is False.

Note: When cards with Divine Shield are displayed on the Verbose mode when running a game, they will be shown with a * after its card representation. For example a (3,3) with Divine Shield will be shown as (3,3)*.

## Deathrattle
If you want a card to have Deathrattle (deathrattle means it does something when it dies), instantiate the Card with deathrattle=<Card>. A Card instance must be passed in this parameter. It is an optional parameter and the default is None.
The only deathrattle currerntly supported is spawning another card.

Note: When cards with Deathrattle are displayed on the Verbose mode when running a game, they will be shown with a DTH<> after its card representation, with the spawned card inside the <>. For example a (3,3) with a Deathrattle that spawns a (2,2) will be shown as (3,3)DTH<(2,2)>.

## Cards with attack = 0
Card with attack = 0 will not work well. The feature is pending. Don't add cards with attack = 0.

## To run simulation
python3 simulation1.py
