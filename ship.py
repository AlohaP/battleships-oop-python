from square import Square
from ocean import Ocean


class Ship(Square):
    # "Carrier": 5, "Battleship": 4, "Cruiser": 3, "Submarine": 3,
    ships = {"Destroyer": 2}

    def __init__(self, name, vertical):
        self.coordinates = []
        self.is_sunk = False
        self.vertical = vertical
        self.name = name
        self.lenght = self.ships[name]

    def change_squares_to_ship(self):
        for square in self.coordinates:
            square.change_to_ship()

    def check_if_sunk(self):
        counter = 0

        for square in self.coordinates:
            if square.sign == "X":
                counter += 1

        if counter == self.lenght:
            for square in self.coordinates:
                square.is_sunk = True

            self.is_sunk = True

