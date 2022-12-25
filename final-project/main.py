# RELATED TO BOTH PARTS (MULTIPLAYER & SINGLE)
from blackjack2 import *
from blackjack3 import *


game_type = input("Single player[S] / multiplier[M]?")

if game_type == 's':
    playAgain()
elif game_type == 'm':
    main()