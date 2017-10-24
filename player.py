from ocean import Ocean
from square import Square
from ship import Ship


class Player:

    def __init__(self, name):
        self.name = name

        self.board = Ocean()
        self.board.read_board_from_file()

        self.view = Ocean()
        self.view.read_board_from_file()

    def print_boards(self):

        print("      ENEMY BOARD")
        self.view.print_board()            # view = opponent board
        print("      YOUR BOARD")
        self.board.print_board()           # board = your board

    def shoot_to_ship(self, coordinates):

        square = self.view.find_object(coordinates)
        square.change_to_hit()

    def put_ship_on_board(self, coordinates):
        ship = Ship("Carrier")
        prow = self.board.find_object(coordinates)
        for line in self.board.ocean_board:
            if prow in line:
                line_index = self.board.ocean_board.index(line)
                index = line.index(prow)
                if not ship.vertical:
                    for i in range(index, index + ship.lenght):
                        line[i] = ship
                else:
                    for i in range(line_index, line_index + ship.lenght):
                        self.board.ocean_board[i][index] = ship


player1 = Player('player1')
player1.put_ship_on_board("C2")
player1.shoot_to_ship("C2")
player1.print_boards()

"""


player1.print_boards()
player1.shoot_to_ship("A2")
player1.print_boards()
player1.put_ship_on_board("A2")
player1.print_boards()
"""
