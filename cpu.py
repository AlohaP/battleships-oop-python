from player import Player
from ocean import Ocean
from square import Square
from ship import Ship
import random


def get_random_cords():
    chars = ["B", "C", "D", "E", "F", "G", "H", "I"]
    cords = [random.choice(chars), str(random.randint(2, 9))]
    return "".join(cords)


def create_CPU_ships():
    ship_list = ["Destroyer", "Submarine", "Cruiser", 'Battleship', 'Carrier']
    for ship in reversed(ship_list):
        while ship_list:
            try:
                ship_cord = get_random_cords()
                true_or_false = [False, True]
                cpu_ship = cpu.get_ship_coordinates(ship, ship_cord, random.choice([True, False]))
                if not cpu.validate_if_ship_is_near(cpu_ship):
                    continue
                else:
                    cpu_ship.change_squares_to_ship()
                    ship_list.remove(ship)
                    break
            except IndexError:
                continue
            except AttributeError:
                continue

cpu = Player("CPU")
create_CPU_ships()
cpu.print_boards()
