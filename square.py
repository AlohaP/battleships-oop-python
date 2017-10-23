class Square():

    def __init__(self, sign, name):
        self.sign = sign
        self.name = name

    def __str__(self):
        return self.sign

    def change_to_ship(self):
        self.sign = '@'

    def change_to_miss(self):
        self.sign = 'O'

    def change_to_hit(self):
        self.sign = 'X'