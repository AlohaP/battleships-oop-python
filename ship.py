from square import Square
from ocean import Ocean


class Ship(Square):

    ships = {"Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3, "Destroyer": 2}

    def __init__(self, name, vertical):
        self.coordinates = []
        self.is_sunk = False
        self.vertical = vertical
        self.name = name
        self.lenght = self.ships[name]

    def change_squares_to_ship(self):
        for square in self.coordinates:
            square.change_to_ship()
