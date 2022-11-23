# import random

# wins = 0
# draw = 0
# losts = 0

# # scores = {
# #     'wins':0,
# #     'draw':0,
# #     'losts':0
# # }

# class Game:    

#     def __init__(self):
#         # self.draw = 0
#         # self.wins = 0
#         # self.losts = 0
#         self.user = self.get_user_item()
#         self.computer = self.get_computer_item()

#     def get_wins(self):
#         return self.wins

#     def get_user_item(self):
#         user_input = []
#         x = input('Select (r)ock, (p)aper, or (s)cissors :')
#         if x == 'r':
#             user_input.append(x)
#         elif x == 'p':
#             user_input.append(x)
#         elif x == 's':
#             user_input.append(x)
#         else:
#             raise ValueError
            
#         return user_input

#     def get_computer_item(self):
#         y = ['r','p','s']
#         a = random.choice(y)
#         return a


#     def get_game_result(self):
#         point = 1
#         # global losts
#         # global wins
#         # global draw
#         if self.user == self.computer:
#             draw + point
#             return 'same, try again'
#         elif self.user == ['r'] and self.computer == 'p':
#             losts + point
#             return 'computer win'
#         elif self.user == ['p'] and self.computer == 's':
#             losts + point
#             return 'computer win'
#         elif self.user == ['s'] and self.computer == 'r':
#             losts + point
#             return 'computer win'
#         else: 
#             wins + point
#             return 'you win'
     
#         return get_game_result()
        
#     def play(self):
#         print (f'user choose {self.user} and the computer {self.computer} result:.')
#         return 
    
#     def print_results():
#      print(f'wins {wins} loss {losts}  draw {draw}')

     
    

import random

class Janken:


    def __init__(self):

        self.choices = ['rock', 'paper', 'scissors']
        self.player_wins = 0
        self.ai_wins = 0
        self.draws = 0
        self.total_games = 0
        self.playgame = self.playgame()

    def playgame(self):

        self.player_hand = input("Please choose between 'Rock', 'Paper' or 'Scissors: ").lower()
        ai_hand = random.choice(self.choices)
        
        if self.player_hand == 'rock':
            if ai_hand == 'rock':
                self.draws += 1
                print(f"You chose {self.player_hand} and the computer chose {ai_hand}. It's a draw!")
            elif ai_hand == 'scissors':
                self.player_wins += 1
                print(f"You chose {self.player_hand} and the computer chose {ai_hand}. You won!")
            else:
                self.ai_wins += 1
                print(f"You chose {self.player_hand} and the computer chose {ai_hand}. AI won!")
        elif self.player_hand == 'paper':

            if ai_hand == 'paper':
                self.draws += 1
                print(f"You chose {self.player_hand} and the computer chose {ai_hand}. It's a draw!")
            elif ai_hand == 'rock':
                self.player_wins += 1
                print(f"You chose {self.player_hand} and the computer chose {ai_hand}. You won!")
            else:
                self.ai_wins += 1
                print(f"You chose {self.player_hand} and the computer chose {ai_hand}. AI won!")
        elif self.player_hand == 'scissors':

            if ai_hand == 'scissors':
                self.draws += 1
                print(f"You chose {self.player_hand} and the computer chose {ai_hand}. It's a draw!")
            elif ai_hand == 'paper':
                self.player_wins += 1
                print(f"You chose {self.player_hand} and the computer chose {ai_hand}. You won!")
            else:
                self.ai_wins += 1
                print(f"You chose {self.player_hand} and the computer chose {ai_hand}. AI won!")
        else:
            print(f"{self.player_hand} is a valid input. Please choose between 'Rock', 'Paper' or 'Scissors'.")
            return self.player_hand
            playgame()

        self.total_games += 1
        self.playagain()

    def playagain(self):
        new_game = input("Would you like to play again? (Y/N): ").lower()
        if new_game == 'y':
            self.playgame()
        else:
            self.get_results()
            print("Thanks for playing!")

    def get_results(self):
        print(f"You have played {self.total_games} matches against the computer.\nPLAYER WINS: {self.player_wins}\nCOMPUTER WINS: {self.ai_wins}\nDRAWS: {self.draws}")

my_game = Janken()