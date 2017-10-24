from square import Square


class Ocean():

    def __init__(self):
        self.ocean_board = []

    def read_board_from_file(self):
        index = 0
        board = ['0', '1', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        with open('board.txt', 'r') as file:
            for line in file:
                counter = 0
                line = list(line)
                if index in range(2, 12):
                    line[counter] = '#'
                    for element in line:
                        if element == ".":
                            counter += 1
                            element = Square(".", (board[index] + str(counter)))
                            line[counter] = element
                self.ocean_board.append(list(line))
                index += 1
        return self.ocean_board

    def print_board(self):
        for line in self.ocean_board:
            for element in line:
                if isinstance(element, Square):
                    print(" ".join(element.sign),end=" ")
                else:
                    print(" ".join(element),end=" ")

    def find_object(self, coordinates):
        for line in self.ocean_board:
            for element in line:
                if isinstance(element, Square) and element.name == coordinates:
                    element.change_to_ship()


ocean = Ocean()
ocean.read_board_from_file()
ocean.print_board()
ocean.find_object("A1")
ocean.print_board()

