from player import Player
from ocean import Ocean
from square import Square
from ship import Ship
from game import PlayBattleships
import random
import time


class PlayBattleshipsWithCPU(PlayBattleships):

    def __init__(self, player, cpu, difficulty):
        self.player1 = player
        self.cpu = cpu
        self.difficulty = difficulty
        self.last_shoot = 0
        self.shooted_cords = []
        self.hitted_and_not_sunk_cords = []
        self.chars = ["B", "C", "D", "E", "F", "G", "H", "I"]
        
    def get_random_cords(self):
        chars = self.chars
        cords = [random.choice(chars), str(random.randint(2, 9))]
        while True:
            if cords in self.shooted_cords:
                cords = [random.choice(chars), str(random.randint(2, 9))]
            else:
                break
        self.shooted_cords.append(cords)
        return "".join(cords)

    def computer_shoot(self):
        if self.difficulty == "easy":
            return self.get_random_cords()
        if self.difficulty == "medium":
            if self.hitted_and_not_sunk_cords:
                if self.player1.board.find_object(self.hitted_and_not_sunk_cords[0]).sunk is True:
                    self.hitted_and_not_sunk_cords = []
            shoot = self.get_random_cords()
            if self.player1.board.find_object(shoot).sign == "@":
                self.hitted_and_not_sunk_cords.append(shoot)
                self.hitted_and_not_sunk_cords = sorted(self.hitted_and_not_sunk_cords)
            if self.hitted_and_not_sunk_cords:
                if len(self.hitted_and_not_sunk_cords) == 1:
                    possible_shoots = [
                        [self.hitted_and_not_sunk_cords[0][0], str(int(self.hitted_and_not_sunk_cords[0][1]) + 1)],
                        [self.hitted_and_not_sunk_cords[0][0], str(int(self.hitted_and_not_sunk_cords[0][1]) - 1)],
                        [self.chars[self.chars.index(self.hitted_and_not_sunk_cords[0][0]) + 1], self.hitted_and_not_sunk_cords[0][1]],
                        [self.chars[self.chars.index(self.hitted_and_not_sunk_cords[0][0]) - 1], self.hitted_and_not_sunk_cords[0][1]]
                                    ]
                    while True:
                        shoot = random.choice(possible_shoots)
                        if shoot not in self.shooted_cords:
                            break
                    print(shoot)
                    
                if len(self.hitted_and_not_sunk_cords) > 1:
                    if self.hitted_and_not_sunk_cords[0][0] == self.hitted_and_not_sunk_cords[-1][0]:
                        shoot = [self.hitted_and_not_sunk_cords[0][0], str(int(self.hitted_and_not_sunk_cords[-1][1]) + 1)]
                        if shoot in self.shooted_cords:
                            shoot = [self.hitted_and_not_sunk_cords[0][0], str(int(self.hitted_and_not_sunk_cords[0][1]) - 1)]
                    elif self.hitted_and_not_sunk_cords[0][1] == self.hitted_and_not_sunk_cords[-1][1]:
                        shoot = [self.chars[self.chars.index(self.hitted_and_not_sunk_cords[0][0]) - 1], self.hitted_and_not_sunk_cords[-1][1]]
                        if shoot in self.shooted_cords:
                            shoot = [self.chars[self.chars.index(self.hitted_and_not_sunk_cords[-1][0]) + 1], self.hitted_and_not_sunk_cords[-1][1]]
                shoot = "".join(shoot)
            self.shooted_cords.append(shoot) 
            self.hitted_and_not_sunk_cords = list(set(self.hitted_and_not_sunk_cords))   
            return shoot
            

    def create_CPU_ships(self, cpu):
        ship_list = ["Destroyer", "Submarine", "Cruiser", 'Battleship', 'Carrier']
        for ship in reversed(ship_list):
            while ship_list:
                try:
                    ship_cord = self.get_random_cords()
                    true_or_false = [False, True]
                    cpu_ship = cpu.get_ship_coordinates(ship, ship_cord, random.choice([True, False]))
                    if not cpu.validate_if_ship_is_near(cpu_ship):
                        continue
                    else:
                        cpu_ship.change_squares_to_ship()
                        ship_list.remove(ship)
                        cpu.warships.append(cpu_ship)
                        break
                except IndexError:
                    continue
                except AttributeError:
                    continue
                
    def boards_setup(self):
        ready_check = input('{} press Enter if youre ready '.format(self.player1.name))
        self.create_player_ships(self.player1)
        self.change_ships_to_hidden(self.player1, self.cpu)

        self.create_CPU_ships(self.cpu)
        self.change_ships_to_hidden(self.cpu, self.player1)

    def turn_mechanics(self, player1, player2):
        self.clear()
        player1.print_boards()
        if player1.name == "CPU1":
            player_shoot = self.computer_shoot()
        else:
            ready_check = input('{} it is your turn!' .format(player1.name))
            player_shoot = input('Where you want to shoot ? ')
        player1.shoot_to_ship(player_shoot)
        player2.get_hit(player_shoot)

        for ship in player2.warships:
            ship.check_if_sunk()
            if ship.is_sunk is True:
                player2.warships.remove(ship)
        player1.print_boards()

        if not player2.warships:
            self.player_victory(player1)

        time.sleep(1)

    def player_victory(self, player):
        self.clear()
        print('{} YOU WON!!! '.format(player.name))
                
ja = Player("Prze")
cpu1 = Player("CPU1")                
play = PlayBattleshipsWithCPU(ja, cpu1, "medium")
play.boards_setup()
while True:
    play.turn_mechanics(ja, cpu1)
    play.turn_mechanics(cpu1, ja)
'''
for i in range(0,5):    
    cords = play.get_random_cords()
    play.turn_mechanics(cords)
    play.get_hit(cords)
cpu.print_boards()
cpu1.print_boards()
'''