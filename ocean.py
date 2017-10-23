from square import Square

class Ocean():

    def __init__(self):
        self.ocean_board = []

    @staticmethod
    def read_board_from_file():
        with open('board.txt', 'r') as file:
            ocean = []
            for line in file:
                ocean.append(list(line))
        return ocean

    def convert_to_squares(self):
        ocean = read_board_from_file()
        for line in ocean:
            for element in line:
                if element == ".":
                    Square(element)

