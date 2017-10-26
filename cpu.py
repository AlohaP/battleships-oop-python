from player import Player
from ocean import Ocean
from square import Square
from ship import Ship
from game import PlayBattleships
import random
import time
import os


class PlayBattleshipsWithCPU(PlayBattleships):

    def __init__(self, player, cpu, difficulty):
        self.player1 = player
        self.cpu = cpu
        self.difficulty = difficulty
        self.shooted_cords = []
        self.hitted_and_not_sunk_cords = []
        self.chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        
    def get_random_cords(self, for_placement):
        chars = self.chars
        if not for_placement:
            
            cords = [random.choice(chars), str(random.randint(2, 9))]
            while True:
                if "".join(cords) in self.shooted_cords:
                    cords = [random.choice(chars), str(random.randint(2, 9))]
                else:
                    break
            self.shooted_cords.append("".join(cords))
            return "".join(cords)
        else:
            return "".join([random.choice(chars), str(random.randint(2, 9))])

    def aim_in_cross(self):
        possible_shoots = [
            [self.hitted_and_not_sunk_cords[0][0], str(int(self.hitted_and_not_sunk_cords[0][1]) + 1)],
            [self.hitted_and_not_sunk_cords[0][0], str(int(self.hitted_and_not_sunk_cords[0][1]) - 1)],
            [self.chars[self.chars.index(self.hitted_and_not_sunk_cords[0][0]) + 1], self.hitted_and_not_sunk_cords[0][1]],
            [self.chars[self.chars.index(self.hitted_and_not_sunk_cords[0][0]) - 1], self.hitted_and_not_sunk_cords[0][1]]
                                ]
        while True:
            shoot = random.choice(possible_shoots)
            shoot = "".join(shoot)
            if shoot not in self.shooted_cords:
                break
        if self.player1.board.find_object(shoot).sign == "@":
            self.hitted_and_not_sunk_cords.append(shoot)
            self.hitted_and_not_sunk_cords = sorted(self.hitted_and_not_sunk_cords)
        self.shooted_cords.append(shoot)
        return shoot

        def aim_in_line(self):
            while True:
                if self.hitted_and_not_sunk_cords[0][0] == self.hitted_and_not_sunk_cords[-1][0]:
                    shoot = [self.hitted_and_not_sunk_cords[0][0], str(int(self.hitted_and_not_sunk_cords[0][1]) - 1)]
                    shoot = "".join(shoot)
                    if shoot in self.shooted_cords:
                        shoot = [self.hitted_and_not_sunk_cords[0][0], str(int(self.hitted_and_not_sunk_cords[-1][1]) + 1)]
                elif self.hitted_and_not_sunk_cords[0][1] == self.hitted_and_not_sunk_cords[-1][1]:
                    shoot = [self.chars[self.chars.index(self.hitted_and_not_sunk_cords[0][0]) - 1], self.hitted_and_not_sunk_cords[0][1]]
                    shoot = "".join(shoot)
                    if shoot in self.shooted_cords:
                        shoot = [self.chars[self.chars.index(self.hitted_and_not_sunk_cords[-1][0]) + 1], self.hitted_and_not_sunk_cords[0][1]]
                shoot = "".join(shoot)
                if shoot not in self.shooted_cords:
                    break
            if self.player1.board.find_object(shoot).sign == "@":
                self.hitted_and_not_sunk_cords.append(shoot)
                self.hitted_and_not_sunk_cords = sorted(self.hitted_and_not_sunk_cords)
            self.shooted_cords.append(shoot)
            return shoot

    def computer_shoot(self):
        if self.hitted_and_not_sunk_cords:
            if self.player1.board.find_object(self.hitted_and_not_sunk_cords[0]).sunk:
                self.hitted_and_not_sunk_cords = []
        if self.difficulty == "easy":
            return self.get_random_cords(False)
        if self.difficulty == "medium" or self.difficulty == "hard":
            if not self.hitted_and_not_sunk_cords:
                if self.difficulty == "medium":
                    shoot = self.get_random_cords(False)
                    if self.player1.board.find_object(shoot).sign == "@":
                        self.hitted_and_not_sunk_cords.append(shoot)
                        self.hitted_and_not_sunk_cords = sorted(self.hitted_and_not_sunk_cords)
                    return shoot
                elif self.difficulty == "hard":
                    while True:
                        shoot = self.get_random_cords(False)
                        if self.player1.board.find_object(shoot).sign == "@":
                            self.hitted_and_not_sunk_cords.append(shoot)
                            self.hitted_and_not_sunk_cords = sorted(self.hitted_and_not_sunk_cords)
                            return shoot
            elif len(self.hitted_and_not_sunk_cords) == 1:
                return self.aim_in_cross()

            elif len(self.hitted_and_not_sunk_cords) > 1:
                return self.aim_in_line()

    def create_CPU_ships(self, cpu):
        ship_list = ["Destroyer", "Submarine", "Cruiser", 'Battleship', 'Carrier']
        for ship in reversed(ship_list):
            while ship_list:
                try:
                    ship_cord = self.get_random_cords(True)
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
        os.system("clear")
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

        time.sleep(0)

    def player_victory(self, player):
        os.system("clear")
        print('{} YOU WON!!! '.format(player.name))
