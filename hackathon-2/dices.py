import random

def dice():

    new_game = input("Would you like to play? Please write 'Y' or 'N': ")

    if new_game.lower() == 'y':
        print("Roll the dice! If you roll a SIX, you win! You only have 3 chances!")
        playgame()
    elif new_game.lower() == 'n':
        print("Maybe next time then...")
    else:
        print("Please use a valid input.")
        dice()


def playgame():

    total_tries = 1

    while total_tries <= 3:
        rolled_number = random.randint(1, 6)

        if rolled_number == 6:
            print('''|o   o|\n|o   o|\n|o   o|''')
            print(f"You rolled a SIX! You won! Total tries: {total_tries}/3.")
            total_tries += 1
            break

        elif rolled_number == 1:
            print('''|     |\n|  o  |\n|     |''')
            print(f"You rolled a ONE. Try again. Total tries: {total_tries}/3")
            total_tries += 1

        elif rolled_number == 2:
            print('''|o    |\n|     |\n|    o|''')
            print(f"You rolled a TWO. Try again. Total tries: {total_tries}/3")
            total_tries += 1

        elif rolled_number == 3:
            print('''|o    |\n|  o  |\n|    o|''')
            print(f"You rolled a THREE. Try again. Total tries: {total_tries}/3")
            total_tries += 1

        elif rolled_number == 4:
            print('''|o   o|\n|     |\n|o   o|''')
            print(f"You rolled a FOUR. Try again. Total tries: {total_tries}/3")
            total_tries += 1

        elif rolled_number == 5:
            print('''|o   o|\n|  o  |\n|o   o|''')
            print(f"You rolled a FIVE. Try again. Total tries: {total_tries}/3")
            total_tries += 1

    else:
        print(f"Out of tries! You lose. Total tries: {total_tries -1}/3. Better luck next time!")
        dice()


dice()