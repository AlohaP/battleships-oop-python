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
        square.change_to_sunk()

    def put_ship_on_board(self, name, coordinates, vertical):
        cord = list(coordinates)
        cord[1] = int(cord[1])
        chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        ship = Ship(name, vertical)
        for i in range(0, ship.lenght):
            square = self.board.find_object("".join([cord[0], str(cord[1])]))
            ship.coordinates.append(square)
            if ship.vertical:
                cord[1] += 1
            else:
                index = chars.index(cord[0])
                cord[0] = chars[index + 1]
        return ship

    def check_if_square_sign_dot(self, square):
        if square.sign == ".":
            return True
        else:
            return False

    def validate_if_ship_is_near(self, ship):
        chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        check_if_place = []
        for coordinate in ship.coordinates:
            cord = list(coordinate.name)
            cord[1] = int(cord[1])
            index = chars.index(cord[0])
            for index in range(chars.index(cord[0])-1, chars.index(cord[0])+2):
                square = self.board.find_object("".join([chars[index], str(cord[1] + 1)]))
                square1 = self.board.find_object("".join([chars[index], str(cord[1] - 1)]))
                square2 = self.board.find_object("".join([chars[index], str(cord[1])]))
                check_if_place.append(self.check_if_square_sign_dot(square))
                check_if_place.append(self.check_if_square_sign_dot(square1))
                check_if_place.append(self.check_if_square_sign_dot(square2))
        return check_if_place
