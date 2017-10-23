def create_ocean(filename):
    with open(filename, 'r') as file:
        ocean = []
        for line in file:
            ocean.append(list(line))
    return ocean


def print_ocean(ocean):
    for row in ocean:
        for i in row:
            print(i, end='')

