from player import Player
from ocean import Ocean
from square import Square
from ship import Ship


def clear():
    print(chr(27) + "[2J")


def player_vs_cpu():
    clear()
    player = Player(input("What's your name?\n"))
    ship_list = [("Destroyer", '2'), ("Submarine", '3'), ("Cruiser", '3'), ('Battleship', '4'), ('Carrier', '5')]
    clear()
    player.print_boards()
    for ship in reversed(ship_list):
        while True:
            clear()
            ship_cord = input("Where do you want to place {})?".format(" (".join(ship)))
            ship_orient = input("Do you want to place {}) horizontally or vertically ? Press h or v.".format(" (".join(ship)))
            # if ship_cord IndexError
            if ship_orient in ["H", "h"]:
                player.put_ship_on_board(ship[0], ship_cord.upper(), False)
                ship_list.remove(ship)
                print(ship_list)
                break
            elif ship_orient in ["V", "v"]:
                player.put_ship_on_board(ship, ship_cord.upper(), True)
                ship_list.remove(ship)
                print(ship_list)
                break
            else:
                continue
            if not ship_list:
                break

    input("")

player_vs_cpu()




        



def player_vs_player():
    print("elo")