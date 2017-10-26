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

    def clear(self):
        print(chr(27) + "[2J")

    def placement_validation(self, ship_list, player, player_ship, ship):
        if not player.validate_if_ship_is_near(player_ship):
            print('zła pozycja')
            print(ship_list)

        else:
            player_ship.change_squares_to_ship()
            player.warships.append(player_ship)
            ship_list.remove(ship)

    # , ("Submarine", '3'), ("Cruiser", '3'), ('Battleship', '4'), ('Carrier', '5')
    def create_player_ships(self, player):
        self.clear()
        ship_list = [("Destroyer", '2')]
        self.clear()
        player.print_boards()

        for ship in reversed(ship_list):

            while True:

                if ship_list:

                    ship_cord = input("Where do you want to place {})? ".format(" (".join(ship)))
                    self.clear()
                    ship_orient = input("Do you want to place {}) horizontally or vertically ? Press h or v. ".format(" (".join(ship)))

                    if ship_orient in ["H", "h"]:
                        player_ship = player.get_ship_coordinates(ship[0], ship_cord.upper(), False)
                        self.placement_validation(ship_list, player, player_ship, ship)
                        player.print_boards()
                        print(ship_list)
                        break

                    elif ship_orient in ["V", "v"]:
                        player_ship = player.get_ship_coordinates(ship[0], ship_cord.upper(), True)
                        self.placement_validation(ship_list, player, player_ship, ship)
                        player.print_boards()
                        print(ship_list)
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

        self.clear()
        player1.print_boards()
        ready_check = input('{} it is your turn!' .format(player1.name))
        player_shoot = input('Where you want to shoot ? ')
        player1.shoot_to_ship(player_shoot.upper())
        player2.get_hit(player_shoot.upper())

        for ship in player2.warships:
            ship.check_if_sunk()
            if ship.is_sunk is True:
                player2.warships.remove(ship)
        player1.print_boards()

        if not player2.warships:
            self.player_victory(player1)

        time.sleep(3)

    def player_victory(self, player):
        self.clear()
        print('{} YOU WON!!! '.format(player.name))


# player1 = Player('Player1')
# player2 = Player('PLayer2')

# game = PlayBattleships(player1, player2)
# game.boards_setup()
# while True:
# game.turn_mechanics(player1, player2)
# game.turn_mechanics(player2, player1)
