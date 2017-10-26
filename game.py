import os
from player import Player
from ocean import Ocean
from square import Square
from ship import Ship
import random
import time

class PlayBattleships():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def placement_validation(self, ship_list, player, player_ship, ship):

        if not player.validate_if_ship_is_near(player_ship):
            os.system('clear')
            return False

        else:
            player_ship.change_squares_to_ship()
            player.warships.append(player_ship)
            ship_list.remove(ship)


    def create_player_ships(self, player):

        available_cord_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', "#"]
        available_cord_numbers = ['2', '3', '4', '5', '6', '7', '8', '9']

        os.system('clear')
        # , ("Submarine", '3'), ("Cruiser", '3'), ('Battleship', '4'), ('Carrier', '5')
        ship_list = [("Destroyer", '2')]
        os.system('clear')
        player.print_boards()

        for ship in reversed(ship_list):

            while True:

                if ship_list:

                    ship_cord = input("Where do you want to place {})? ".format(" (".join(ship)))

                    if len(ship_cord) != 2:
                        print('>>>>> Wrong input <<<<<')
                        continue

                    elif ship_cord[0].upper() not in available_cord_letters:
                        print('>>>>> Wrong input <<<<<')
                        continue

                    elif len(ship_cord[1]) > 1:
                        print('>>>>> Wrong input <<<<<')
                        continue

                    elif ship_cord[1] not in available_cord_numbers:
                        print(">>>>> Wrong input <<<<<")
                        continue

                    ship_orient = input("Do you want to place {}) horizontally or vertically ? Press h or v. ".format(" (".join(ship)))

                    if ship_orient in ["H", "h"]:
                        player_ship = player.get_ship_coordinates(ship[0], ship_cord.upper(), False)

                        if self.placement_validation(ship_list, player, player_ship, ship) is False:
                            player.print_boards()
                            print('>>>>> Wrong input <<<<<')
                            continue
                        break

                    elif ship_orient in ["V", "v"]:
                        player_ship = player.get_ship_coordinates(ship[0], ship_cord.upper(), True)

                        if self.placement_validation(ship_list, player, player_ship, ship) is False:
                            player.print_boards()
                            print('>>>>> Wrong input <<<<<')
                            continue
                        break

                    else:
                        continue
                break

    # def determine_first_turn(self):
    #     turn = random.randint(1, 2)
    #     if turn == 1:
    #         player_1_turn = True
    #         print('\n{} will go first.'.format(self.player1.name))
    #         return player_1_turn
    #     else:
    #         player_1_turn = False
    #         print('\n{} will go first.'.format(self.player2.name))
    #         return player_1_turn

    def change_ships_to_hidden(self, player1, player2):
        for ship in player1.warships:
            list_of_cords = ship.coordinates
            for square in list_of_cords:
                square = player2.view.find_object(square.name)
                square.hidden_ship = True

    def boards_setup(self, player1, player2):
        ready_check = input('{} press Enter if youre ready '.format(self.player1.name))
        self.create_player_ships(self.player1)
        self.change_ships_to_hidden(self.player1, self.player2)
        ready_check = input('{} press Enter if youre ready '.format(self.player2.name))
        self.create_player_ships(self.player2)
        self.change_ships_to_hidden(self.player2, self.player1)

    def turn_mechanics(self, player1, player2):

        os.system('clear')
        player1.print_boards()
        print('{} it is your turn!' .format(player1.name))
        time.sleep(1)
        player_shoot = input('Where you want to shoot ? ')
        player1.shoot_to_ship(player_shoot.upper())
        player2.get_hit(player_shoot.upper())

        for ship in player2.warships:
            ship.check_if_sunk()
            if ship.is_sunk is True:
                player2.warships.remove(ship)
        player1.print_boards()


    def player_victory(self, player):
        os.system('clear')
        player.highscore.append(player.name)
        player.highscore.append(len(player.warships))
        print('{} YOU WON!!! '.format(player.name))


    def check_if_warships_alive(self, player1, player2):

        if not player2.warships:
            return True

    def game_flow(self, player1, player2):

        self.turn_mechanics(player1, player2)

        self.turn_mechanics(player2, player1)

# player1 = Player('Player1')
# player2 = Player('PLayer2')

# game = PlayBattleships(player1, player2)
# game.boards_setup()
# while True:
# game.turn_mechanics(player1, player2)
# game.turn_mechanics(player2, player1)
