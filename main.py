
from square import Square
from player import Player
from game import PlayBattleships
from cpu import PlayBattleshipsWithCPU
from ship import Ship
from ocean import Ocean


menu_commands = ["Player vs Player", "Player vs CPU", "How to play",
                "Hall of Fame", "Exit"]

difficulty = ["Easy", "Medium", "Hard"]


def print_program_menu(menu_commands):

    for option in menu_commands:
        print(str(menu_commands.index(option)) + "----->" + option)


def main():

    while True:

        print_program_menu(menu_commands)

        option = input("Select an option: ")

        if option == "0":

            player1 = Player(input("Please enter your name: "))
            player2 = Player(input("Please enter player 2 name: "))

            game = PlayBattleships(player1, player2)
            game.boards_setup(player1, player2)

            while True:

                game.turn_mechanics(player1, player2)

                game_result = game.check_if_warships_alive(player1, player2)

                if game_result is True:
                    print('{} YOU WON!!! '.format(player1.name))
                    break

                game.turn_mechanics(player2, player1)

                game_result = game.check_if_warships_alive(player2, player1)

                if game_result is True:
                    print('{} YOU WON!!! '.format(player2.name))
                    break
        
        elif option == "1":

            player1 = Player(input("Please enter your name: "))

            while True:

                print_program_menu(difficulty)

                difficulty_option = input("Select an difficulty")

                if difficulty_option == "0":

                    pass                                #There will be easy game here

                elif difficulty_option == "1":

                    pass                                #There will be medium here

                elif difficulty_option == "2":

                    pass                                #Hard

                else:
                    print("Wrong input")
                    continue






def high_score():

    print("elo")

def instruction():

    print("elo")

if __name__ == "__main__":
    main()