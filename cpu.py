from player import Player
from ocean import Ocean
from square import Square
from ship import Ship
from game import PlayBattleships
import random


class PlayBattleshipsWithCPU(PlayBattleships):

    def __init__(self, player, cpu):
        self.player = player
        self.cpu = cpu

    def get_random_cords(self):
        chars = ["B", "C", "D", "E", "F", "G", "H", "I"]
        cords = [random.choice(chars), str(random.randint(2, 9))]
        return "".join(cords)

    def create_CPU_ships(self, cpu):
        ship_list = ["Destroyer", "Submarine", "Cruiser", 'Battleship', 'Carrier']
        for ship in reversed(ship_list):
            while ship_list:
                try:
                    ship_cord = self.get_random_cords()
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
                
# cpu = Player("CPU")
# cpu1 = Player("CPU1")                
# play = PlayBattleshipsWithCPU(cpu, cpu1)

# play.create_CPU_ships(cpu)
# play.create_CPU_ships(cpu1)
# cpu.print_boards()
# cords = play.get_random_cords()
# player1 = Player('Player1')
# player2 = Player('PLayer2')

# cpu.shoot_to_ship(cords)
# cpu.print_boards()
