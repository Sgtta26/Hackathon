# SINGLE PART

import random
from utils import refresh_deck

# playerIn = True
# dealerIn = True


# deck of cards / player and dealer hand

# deck = [2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 
#         'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']

# deck = [2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 
#     'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A',
#     2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 
#     'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']

refresh_deck()

playerHand = []
dealerHand = []



# deal the cards

def dealCard_computer(computer_turn, deck):
    card = random.choice(deck)
    computer_turn.append(card)
    deck.remove(card)

def dealCard_player(player_turn, deck):
    card = random.choice(deck)
    player_turn.append(card)
    deck.remove(card)


# calculate the total of each hand + possibility to choose 1 or 10 for A

def total_computer(computer_turn):
    total_computers = 0
    face = ['J', 'Q', 'K']
    face3 = ['A']
    for card in computer_turn:
        if card in range(1,11):
            total_computers += card
        elif card in face:
            total_computers += 10
        elif card in face3 and total_computers > 11:
            total_computers += 1
        else:
            if total_computers >= 11:
                total_computers += 1
            else:
                total_computers += 11
        
    return total_computers


def total(player_turn):
    global total_player 
    
    total_player = 0
    face = ['J', 'Q', 'K']
    face2 = ['A']
    for card in player_turn:
        if card in range(1,11):
            total_player += card
        elif card in face:
            total_player += 10
        elif card in face2 and total_player > 11:
            total_player += 1
        elif card in face2 and total_player <= 11:
            print(f"You have {playerHand}")
            question = int(input('You have the possibility to choose 1 or 11 :'))
            if question == 1:
                total_player += 1
            if question == 11:
                total_player += 11
    # print(f"total of {total_player}")
    return total_player

# check for winner

def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]


# game loop

def game_loop(deck, player_score):

    playerIn = True
    dealerIn = True
    turn = 1

    for loop in range(2):
        dealCard_computer(dealerHand, deck)
        dealCard_player(playerHand, deck)
    while playerIn or dealerIn:
        
        print(f"Dealer had {revealDealerHand()} and ?")
        
        if turn == 1:
            player_score += total(playerHand)

        print(f"You have {playerHand} for a total of {player_score}")
            
        if playerIn:
            stayOrHit = input("(1) Stay here\n(2) Hit a new card\n")
        if total_computer(dealerHand) > 16:
            dealerIn = False
        else:
            dealCard_computer(dealerHand, deck)
        if stayOrHit == '1':
            playerIn = False
        elif stayOrHit == '2':
            dealCard_player(playerHand, deck)
            player_score += total([playerHand[-1]])

            turn += 1

            if player_score >= 21: 
                break 
            
        if player_score >= 21:
            break
        elif total_computer(dealerHand) >= 21:
            break

        # else:
        #     print("Please use a valid input.")
        #     clear_hand()
        #     game_loop()

    if player_score == 21:
        print(f"\nYou have {playerHand} for a total of {player_score} and the dealer has {dealerHand} for a total of {total_computer(dealerHand)}")
        print("Blackjack ! You win !")
        clear_hand()
        playAgain()

    elif total_computer(dealerHand) == 21:
        print(f"\nYou have {playerHand} for a total of {player_score} and the dealer has {dealerHand} for a total of {total_computer(dealerHand)}")
        print("Blackjack ! Dealer wins !")
        clear_hand()
        playAgain()

    elif player_score > 21:
        print(f"\nYou have {playerHand} for a total of {player_score} and the dealer has {dealerHand} for a total of {total_computer(dealerHand)}")
        print("You bust ! Dealer wins !")
        clear_hand()
        playAgain()

    elif total_computer(dealerHand) > 21:
        print(f"\nYou have {playerHand} for a total of {player_score} and the dealer has {dealerHand} for a total of {total_computer(dealerHand)}")
        print("Dealer busts ! You win !")
        clear_hand()
        playAgain()

    elif 21 - total_computer(dealerHand) < 21 - player_score:
        print(f"\nYou have {playerHand} for a total of {player_score} and the dealer has {dealerHand} for a total of {total_computer(dealerHand)}")
        print("Dealer wins !")
        clear_hand()
        playAgain()

    elif 21 - total_computer(dealerHand) > 21 - player_score:
        print(f"\nYou have {playerHand} for a total of {player_score} and the dealer has {dealerHand} for a total of {total_computer(dealerHand)}")
        print("You win !")
        clear_hand()
        playAgain()


# delete the previous player hand for a new game:
def clear_hand():
    playerHand.clear()
    dealerHand.clear()



# loop for play again:
def playAgain():
    global player_score 

    new_game = input("Would you like to play? Please write 'Y' or 'N': ").lower()

    if new_game == 'y':
        deck = refresh_deck()
        player_score = 0
        game_loop(deck, player_score)
    elif new_game == 'n':
        print("Maybe next time then...")
    else:
        print("Please use a valid input.")


        playAgain()

if __name__ == '__main__':
    playAgain()