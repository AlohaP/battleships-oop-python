from player import Player
from ocean import Ocean
from square import Square
from ship import Ship


def clear():
    print(chr(27) + "[2J")


def create_player_ships():
    clear()
    player = Player(input("What's your name?\n"))
    ship_list = [("Destroyer", '2'), ("Submarine", '3'), ("Cruiser", '3'), ('Battleship', '4'), ('Carrier', '5')]
    clear()
    player.print_boards()
    for ship in reversed(ship_list):
        while True:
            if ship_list:
                clear()
                ship_cord = input("Where do you want to place {})?".format(" (".join(ship)))
                ship_orient = input("Do you want to place {}) horizontally or vertically ? Press h or v.".format(" (".join(ship)))
                if ship_orient in ["H", "h"]:
                    player_ship = player.get_ship_coordinates(ship[0], ship_cord.upper(), False)
                    if not player.validate_if_ship_is_near(player_ship):
                        print('zła pozycja')
                        print(ship_list)
                        continue
                    else:
                        player_ship.change_squares_to_ship()
                        ship_list.remove(ship)
                    player.print_boards()
                    print(ship_list)
                    break
                elif ship_orient in ["V", "v"]:
                    player_ship = player.get_ship_coordinates(ship[0], ship_cord.upper(), True)
                    if not player.validate_if_ship_is_near(player_ship):
                        print('zła pozycja')
                        print(ship_list)
                        continue
                    else:
                        player_ship.change_squares_to_ship()
                        ship_list.remove(ship)
                    player.print_boards()
                    print(ship_list)
                    break
                else:
                    continue
            break


    input("")

create_player_ships()




        



def player_vs_player():
    print("elo")