from game import *

def get_user_menu_choice():
    d = input('Would you like to (p)lay a new game OR Show score (w) OR (e)xit :')
    # print("d", d)
    return d 
    # and Game().play() and main()


# def print_results():
#     print(f'You win {scores["wins"]}, you loss {scores["losts"]}, {scores["draw"]}')



def main():
    choice = get_user_menu_choice()
    # print("choice", choice)
    while choice != '':
        if choice == 'p':
            # print("play , choice is :", choice)
            Game().play()
            # return
            # print("after play , choice is :", choice)
            # main()
            choice = get_user_menu_choice()   
            # main()
        elif choice == 'w':
            # print("in w , choice is :", choice)
            Game.print_results()
            # choice = ""
            break
        elif choice == 'e':
            # print("in e, choice is :", choice)
            print('Thank you for you playing, bye')
            # choice = ""
            break


        

main()