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
        self.deal = ''
        self.lost = False

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
                    question = int(input(f'{self.name}, you have the possibility to choose 1 or 11 :'))
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

    def __repr__(self):
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
        if player.is_house and player.total_score > 16:
            pass
        else:
            card = random.choice(self.deck)
            player.cards.append(card)
            player.total()
            self.deck.remove(card)

    # distribute base on the amount of player (how many player we choose in the beginning)
    def deal_cards(self, initial=False):
        if initial:
            for _ in range(2):
                for player in self.players:
                    self.dealCard_player(player)
                self.dealCard_player(self.house)
        else:
            deal_card = lambda p: input(f"{p.name}: (1) Stay here\n(2) Hit a new card\n")
            for player in self.players:
                if player.lost or player.deal == '1':
                    continue
                player.deal = deal_card(player)
                if player.deal == '2':
                    self.dealCard_player(player)
            self.dealCard_player(self.house) # Deal one card to house

     # check all the possibility for know who is the winner:
    @staticmethod
    def check_win_lose(player):

        if player.total_score == 21:
            return "B"
        elif player.total_score > 21:
            player.lost = True
            return "L"
        else:
            return player.total_score

    def calculate_winner(self):

        win_lose = {}

        for player in self.players:
            win_lose[player] = BlackJack.check_win_lose(player)
        
        win_lose[self.house] = BlackJack.check_win_lose(self.house)

        return win_lose

    def check_winner(self):

        players_final = self.calculate_winner()
        blackjacks = [player for player in players_final if players_final[player] == 'B']
        losers = [player for player in players_final if players_final[player] == 'L']
        winners = []

        if not blackjacks:
            winners = [(player, score) for player, score in players_final.items()
                       if player not in [*blackjacks, *losers]]
            winners.sort(key=lambda p: p[1], reverse=True)

            winner = winners[0]
            for player in winners:
                if player[1] == winner[1]:
                    pass
                else:
                    losers.append(player[0])

        else:
            losers = [player for player in players_final if player not in blackjacks]

        return blackjacks, losers, winners

    def print_winlose(self):

        blackjack_message = lambda player: f"{player} has BLACKJACK!"
        lose_message = lambda player: f"{player} LOST!!"
        win_message = lambda player: f"{player} WON!!"

        blackjacks, losers, winners = self.check_winner()

        if blackjacks:
            for player in blackjacks:
                print(blackjack_message(player))
            for player in losers:
                print(lose_message(player))
        else:
            winner = ('', 0)  # ("Sarah", 18)
            for player in winners:
                if player[1] >= winner[1]:
                    print(win_message(player[0]))
                else:
                    break
                winner = player

            for player in losers:
                print(lose_message(player))

    def check_finish(self):

        blackjacks, losers, winners = self.check_winner()

        if blackjacks:
            self.print_winlose()
            return blackjacks

        if self.house.total_score > 21:
            # print("House LOST")
            print(f"HOUSE GOT {self.house.total_score}")
            self.print_winlose()
            return winners

        if len([player for player in self.players if player.lost]) == len(self.players):
            # print("ALL PLAYERS LOST. HOUSE WINS")
            self.print_winlose()
            return self.house

        deals = [player.deal for player in self.players if not player.lost]
        if all(map(lambda deal: True if deal == '1' else False, deals)):
            # print("ALL PLAYERS STAYED. COMPARING")
            self.print_winlose()
            return winners

        else:
            return

# say for all the player which card he got
    def __str__(self):
        output = ""
        players = [player for player in self.players]
        cards = [player.cards for player in self.players]

    # player1 : K|7 // player1 : 10|3 == it takes the results from the str and make it "more organized"
        for player, card in zip(players, cards):
            card = list(map(str, card))
            output += f"{player}: {'|'.join(card)} for total of {player.total_score}\n"

        house_cards = list(map(str, self.house.cards))
        house_cards[-1] = '?'
        output += f"\n{self.house}: {'|'.join(house_cards)}"
        return output 




def main():
    new_game = ''

    while new_game != 'n':
        new_game = input("Would you like to play? Please write 'Y' or 'N': ").lower()

        if new_game == 'y':
            rename = []
            regame = int(input('How many player you are :'))
            x = range(regame)
            for n in x:
                add_name = input(f'What the name of Player {n + 1} :')
                rename.append(add_name)

            game = BlackJack(regame, *rename)
            game.deal_cards(initial=True)

            while True:
                print(game)
                game.deal_cards()
                result = game.check_finish()
                if result is not None:
                    break

        elif new_game.lower() == 'n':
            print("Maybe next time then...")
        else:
            print("Please use a valid input.")
            main()

# it is for that the game work just in this file
if __name__ == '__main__':
    main()
