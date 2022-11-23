import random

wins = 0
draw = 0
losts = 0

# scores = {
#     'wins':0,
#     'draw':0,
#     'losts':0
# }

class Game:    

    def __init__(self):
        # self.draw = 0
        # self.wins = 0
        # self.losts = 0
        self.user = self.get_user_item()
        self.computer = self.get_computer_item()

    def get_wins(self):
        return self.wins

    def get_user_item(self):
        user_input = []
        x = input('Select (r)ock, (p)aper, or (s)cissors :')
        if x == 'r':
            user_input.append(x)
        elif x == 'p':
            user_input.append(x)
        elif x == 's':
            user_input.append(x)
        else:
            raise ValueError
            
        return user_input

    def get_computer_item(self):
        y = ['r','p','s']
        a = random.choice(y)
        return a


    def get_game_result(self):
        point = 1
        # global losts
        # global wins
        # global draw
        if self.user == self.computer:
            draw + point
            return 'same, try again'
        elif self.user == ['r'] and self.computer == 'p':
            losts + point
            return 'computer win'
        elif self.user == ['p'] and self.computer == 's':
            losts + point
            return 'computer win'
        elif self.user == ['s'] and self.computer == 'r':
            losts + point
            return 'computer win'
        else: 
            wins + point
            return 'you win'
     
        return get_game_result()
        
    def play(self):
        print (f'user choose {self.user} and the computer {self.computer} result:.')
        return 
    
    def print_results():
     print(f'wins {wins} loss {losts}  draw {draw}')

     
    

