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

        os.system('clear')
        ship_list = [("Destroyer", '2'), ("Submarine", '3'), ("Cruiser", '3'), ('Battleship', '4'), ('Carrier', '5')]
        os.system('clear')

        for ship in reversed(ship_list):

            while True:
                
                os.system('clear')
                player.print_boards()

                if ship_list:

                    ship_cord = input("Where do you want to place {})? ".format(" (".join(ship)))
                    ship_orient = input("Do you want to place {}) horizontally or vertically ? Press h or v. ".format(" (".join(ship)))

                    if ship_orient in ["H", "h"]:
                        try:
                            player_ship = player.get_ship_coordinates(ship[0], ship_cord.upper(), False)
                            if self.placement_validation(ship_list, player, player_ship, ship) is False:
                                print('>>>>> Wrong input <<<<<')
                                continue
                        except IndexError or ValueError:
                            print('>>>>> Wrong input <<<<<')
                            continue
                        break

                    elif ship_orient in ["V", "v"]:
                        try:
                            player_ship = player.get_ship_coordinates(ship[0], ship_cord.upper(), True)
                            if self.placement_validation(ship_list, player, player_ship, ship) is False:
                                print('>>>>> Wrong input <<<<<')
                                continue
                        except IndexError or ValueError:
                            print('>>>>> Wrong input <<<<<')
                            continue
                        break

                    else:
                        continue
                break

    def change_ships_to_hidden(self, player1, player2):
        for ship in player1.warships:
            list_of_cords = ship.coordinates
            for square in list_of_cords:
                square = player2.view.find_object(square.name)
                square.hidden_ship = True

    def boards_setup(self):
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

    def check_if_warships_alive(self, player2):

        if not player2.warships:
            return True

    def game_flow(self, player1, player2):

        self.turn_mechanics(player1, player2)

        self.turn_mechanics(player2, player1)
