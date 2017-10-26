import game
from square import Square
from player import Player
from game import PlayBattleships
from cpu import PlayBattleshipsWithCPU
from ship import Ship
from ocean import Ocean


menu_commands = ["Player vs Player", "Player vs CPU", "How to play",
                "Hall of Fame", "Exit"] 


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

                game.game_flow(player1, player2)

                if game.game_flow == True:
                    print("You won")
                    break





def high_score():

    print("elo")

def instruction():

    print("elo")

if __name__ == "__main__":
    main()