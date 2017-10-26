
from square import Square
from player import Player
from game import PlayBattleships
from cpu import PlayBattleshipsWithCPU
from ship import Ship
from ocean import Ocean
import time
import pickle
import howtoplay

menu_commands = ["Player vs Player", "Player vs CPU", "How to play",
                "Hall of Fame", "Exit"]

difficulty = ["Easy", "Medium", "Hard"]


def print_program_menu(menu_commands):

    for option in menu_commands:
        print(str(menu_commands.index(option)) + "----->" + option)


def highscore_creation(game, player, start_time):
    end_time = time.time()
    elapsed_time = round(end_time - start_time)
    player.highscore.append(elapsed_time)
    game.player_victory(player)
    highscore = abs(17 * len(player.warships) + 100 - elapsed_time) * 1000
    player.highscore.append(highscore)
    high_score_export(player)
    print(player.highscore)  # testowy print


def main():

    while True:

        print_program_menu(menu_commands)

        option = input("Select an option: ")

        if option == "0":

            player1 = Player(input("Please enter your name: "))
            player2 = Player(input("Please enter player 2 name: "))

            game = PlayBattleships(player1, player2)
            game.boards_setup(player1, player2)
            start_time = time.time()

            while True:
                game.turn_mechanics(player1, player2)
                game_result = game.check_if_warships_alive(player1, player2)
                if game_result is True:
                    highscore_creation(game, player1, start_time)
                    break

                game.turn_mechanics(player2, player1)
                game_result = game.check_if_warships_alive(player2, player1)
                if game_result is True:
                    highscore_creation(game, player2, start_time)
                    break
        
        elif option == "1":

            player1 = Player(input("Please enter your name: "))
            cpu1 = Player("CPU1")
            difficulty_levels = ["easy", "medium", "hard"]
            while True:

                print_program_menu(difficulty)

                difficulty_option = input("Select an difficulty")

                if difficulty_option in ["0", "1", "2"]:
                    game = PlayBattleshipsWithCPU(player1, cpu1, difficulty_levels[int(difficulty_option)])
                    game.boards_setup()
                    start_time = time.time()
                    while True:
                        game.turn_mechanics(player1, cpu1)
                        game_result = game.check_if_warships_alive(player1, cpu1)
                        if game_result is True:
                            highscore_creation(game, player1, start_time)
                            break

                        game.turn_mechanics(cpu1, player1)
                        game_result = game.check_if_warships_alive(cpu1, player1)
                        if game_result is True:
                            highscore_creation(game, cpu1, start_time)
                            break

                else:
                    print("Wrong input")
                    continue
        if option == '2':
            howtoplay.instruction_display()
        if option == '3':
            high_score_presentation()





def high_score_export(player, filename='highscores.txt', mode = 'ab'):
        with open(filename, mode) as exporting_file:
            pickle.dump(player.highscore, exporting_file)

def high_score_presentation(filename='highscores.txt', mode='rb'):
    imported_hs = []
    with open(filename, mode) as openfile:
        while True:
            try:
                imported_hs.append(pickle.load(openfile))
            except EOFError:
                break
    imported_hs = sorted(imported_hs, reverse=False)[:10]
    print('The best Captains currently on our waters are: \n')
    for result in imported_hs:
        print('| Total highscore: {} | Ships left: {} | Username: {}  | Time: {} seconds '.format(result[3], result[2], result[1], result[0]))

def instruction():

    print("elo")

if __name__ == "__main__":
    main()