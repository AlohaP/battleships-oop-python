from ocean import Ocean
from square import Square

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


player1 = Player('player1')

player1.print_boards()
player1.shoot_to_ship("A2")
player1.print_boards()