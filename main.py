import game


def high_score():
    print("elo")

def instruction():
    print("elo")



def main():
    while True:
        menu_select = input("""
                            1. Player vs CPU
                            2. Player vs Player
                            3. Hall of Fame
                            4. How to play
                            0. Quit
                            """)
        menu = {"0": quit, "1": game.create_player_ships, "2": game.player_vs_player, "3": high_score, "4": instruction}
        if menu_select not in menu:
            continue
        menu[menu_select]()


if __name__ == "__main__":
    main()