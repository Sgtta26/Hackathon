# MULTIPLAYER PART

from utils import refresh_deck
import random

# deal the cards for the computer

def dealCard_computer(computer_turn, deck):
    card = random.choice(deck)
    computer_turn.append(card)
    deck.remove(card)

# save the player name and his cards

class Player:

    def __init__(self, name, is_house=False):
        self.name = name
        self.cards = []
        self.is_house = is_house
        self.scores = []
        
    def total(self): 
        """Calculate total score for player's card""" 
        total_player = 0
        face = ['J', 'Q', 'K']
        face2 = ['A']

        if not self.scores:
            cards = self.cards
        else:
            cards = [self.cards[-1]]

        for card in cards:
            if card in range(1,11):
                total_player += card
            elif card in face:
                total_player += 10
            elif card in face2 and total_player > 11:
                total_player += 1
            elif card in face2 and total_player <= 11:
                if not self.is_house:
                    print(f"You have {self.cards}")
                    question = int(input('You have the possibility to choose 1 or 11 :'))
                    if question == 1:
                        total_player += 1
                    if question == 11:
                        total_player += 11

                else:
                    if total_player >= 11:
                        total_player += 1
                    else:
                        total_player += 11 

            turn = len(self.scores)+1

            self.scores.append((turn, total_player)) # (turn=1, total=5)

            return total_player

    @property
    def total_score(self): 
        """calculate total score for all turns"""
        # self.scores = [(1,5), (2, 6)]
        total = 0
        for score in self.scores:
            total += score[1]
        return total

    def __str__(self):
        return self.name

# take the variable name and number of player that we already have from the input of the begging
class BlackJack:

    def __init__(self, number_of_players: int, *names):
        self.number_of_players = number_of_players
        self.players = [Player(name) for name in names]
        self.house = Player('House', is_house=True)
        self.deck = refresh_deck()

    # distribute cards for players
    def dealCard_player(self, player: Player):
        card = random.choice(self.deck)
        player.cards.append(card)
        self.deck.remove(card)

    # distribute base on the amount of player (how many player we choose in the beginning)
    def deal_cards(self):
        for player in self.players:
            self.dealCard_player(player) 

        self.dealCard_player(self.house) # Deal one card to house

     # check all the possibility for know who is the winner:
    @staticmethod
    def check_win_lose(player):

        if player.total_score == 21:
            print(f"\{player} has {player.cards} for a total of {player.total_score}")
            print("Blackjack ! You win !")
            return "W"

        elif player.total_score > 21:
            print(f"\{player} has {player.cards} for a total of {player.total_score}")
            print("You bust ! ")
            return "L"

        else:
            return player.total_score

    def calculate_winner(self):

        win_lose = {}

        for player in self.players:
            win_lose[player] = BlackJack.check_win_lose(player)
        
        win_lose[self.house] = BlackJack.check_win_lose(self.house)

        return win_lose


            # elif total_computer(dealerHand) == 21:
            #     print(f"\nYou have {playerHand} for a total of {player_score} and the dealer has {dealerHand} for a total of {total_computer(dealerHand)}")
            #     print("Blackjack ! Dealer wins !")
            #     clear_hand()
            #     playAgain()

            # elif total_computer(dealerHand) > 21:
            #     print(f"\nYou have {playerHand} for a total of {player_score} and the dealer has {dealerHand} for a total of {total_computer(dealerHand)}")
            #     print("Dealer busts ! You win !")
            #     clear_hand()
            #     playAgain()

            # elif 21 - total_computer(dealerHand) < 21 - player_score:
            #     print(f"\nYou have {playerHand} for a total of {player_score} and the dealer has {dealerHand} for a total of {total_computer(dealerHand)}")
            #     print("Dealer wins !")
            #     clear_hand()
            #     playAgain()

            # elif 21 - total_computer(dealerHand) > 21 - player_score:
            #     print(f"\nYou have {playerHand} for a total of {player_score} and the dealer has {dealerHand} for a total of {total_computer(dealerHand)}")
            #     print("You win !")
            #     clear_hand()
            #     playAgain()


# say for all the player which card he got
    def __str__(self):
        output = ""
        players = [str(player) for player in self.players]
        cards = [player.cards for player in self.players]

    # player1 : K|7 // player1 : 10|3 == it takes the results from the str and make it "more organized"
        for player, card in zip(players, cards):
            card = list(map(str, card))
            output += f"{player}: {'|'.join(card)}\n"

        house_cards = list(map(str, self.house.cards))
        output += f"\n{self.house}: {'|'.join(house_cards)}"
        return output 



def main():
    game = BlackJack(2, 'Sarah','Yossi')
    game.deal_cards()
    

    for player in game.players:
        player.total()
        print(player.total_score)
    game.house.total()

    game.deal_cards()
    for player in game.players:
        player.total()
        print(player.total_score)
    game.house.total()

    game.deal_cards()
    for player in game.players:
        player.total()
        print(player.total_score)
    game.house.total()

    print(game.calculate_winner())

if __name__ == '__main__':
    main()



