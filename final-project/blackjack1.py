# FIRST GAME TRY
import random


# playerIn = True
# dealerIn = True


# deck of cards / player dealer hand

deck = [2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
playerHand = []
dealerHand = []


# deal the cards

def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)


# calculate the total of each hand

def total(turn):
    total = 0
    face = ['A', 'J', 'Q', 'K']
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total


# check for winner

def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]


# game loop

def game_loop():
    playerIn = True
    dealerIn = True

    for loop in range(2):
        dealCard(dealerHand)
        dealCard(playerHand)
    while playerIn or dealerIn:
        
        print(f"Dealer had {revealDealerHand()} and ?")
        print(f"You have {playerHand} for a total of {total(playerHand)}")
            
        if playerIn:
            stayOrHit = int(input("(1) Stay\n(2) Hit\n"))
        if total(dealerHand) > 16:
                dealerIn = False
        else:
            dealCard(dealerHand)
        if stayOrHit == 1:
            playerIn = False
        else:
            dealCard(playerHand)
        if total(playerHand) >= 21:
            break
        elif total(dealerHand) >= 21:
            break
        else:
            print("Please use a valid input.")
            clear_hand()
            game_loop()

    if total(playerHand) == 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Blackjack ! You win !")
        clear_hand()
        playAgain()

    elif total(dealerHand) == 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Blackjack ! Dealer wins !")
        clear_hand()
        playAgain()

    elif total(playerHand) > 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("You bust ! Dealer wins !")
        clear_hand()
        playAgain()

    elif total(dealerHand) > 21:
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Dealer busts ! You win !")
        clear_hand()
        playAgain()

    elif 21 - total(dealerHand) < 21 - total(playerHand):
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("Dealer wins !")
        clear_hand()
        playAgain()

    elif 21 - total(dealerHand) > 21 - total(playerHand):
        print(f"\nYou have {playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
        print("You win !")
        clear_hand()
        playAgain()


# delete the previous player hand for a new game:

def clear_hand():
    playerHand.clear()
    dealerHand.clear()



# loop for play again:

def playAgain():

    new_game = input("Would you like to play? Please write 'Y' or 'N': ").lower()

    if new_game == 'y':
        game_loop()
    elif new_game.lower() == 'n':
        print("Maybe next time then...")
    else:
        print("Please use a valid input.")
        playAgain()

playAgain()