from square import Square
from ocean import Ocean


class Ship(Square):

    ships = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}

    def __init__(self, name, sign="@"):
        self.is_sunk = False
        self.vertical = True
        self.name = self.ships[name]
        self.sign = sign
        self.lenght = 5



ocean = Ocean()
#ocean.read_board_from_file()
ocean.print_board()