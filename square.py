class Square():

    R = '\033[31m' # red
    W = '\033[0m'  # white (normal)

    def __init__(self, sign, name):
        self.sign = sign
        self.name = name
        self.sunk = False

    def __str__(self):
        return self.sign

    def change_to_ship(self):
        self.sign = '@'

    def change_to_miss(self):
        self.sign = 'O'

    def change_to_hit(self):
<<<<<<< HEAD
        if self.sing == "@":
            self.sign = 'X'
        else:
            self.sign = 'O'
=======
        self.sign = 'X'

    def change_to_sunk(self):
        self.sunk = True
>>>>>>> 4c9caddefdc5e46e4dcc6f13680730322b235f07
