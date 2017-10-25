from square import Square


class Ocean():

    W = '\033[0m'  # white (normal)
    R = '\033[1;31m' # red

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
                            element = Square(".", (board[counter + 1] + str(index - 1)))
                            line[counter] = element
                self.ocean_board.append(list(line))
                index += 1
        return self.ocean_board

    def print_board(self):
        for line in self.ocean_board:
            for element in line:

                if isinstance(element, Square) and element.sunk == True:
                    print('{}{}{}'.format(self.R, element.sign, self.W), end = " ")

                elif isinstance(element, Square):
                    print(" ".join(element.sign), end=" ")
                    
                else:
                    print(" ".join(element), end=" ")

    def find_object(self, coordinates):
        for line in self.ocean_board:
            for element in line:
                if isinstance(element, Square) and element.name == coordinates:
                    return element

