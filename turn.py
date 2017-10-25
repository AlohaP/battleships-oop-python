While play_again:
        winner = None
        player_health = 100
        computer_health = 100

        # determine whose turn it is
        turn = random.randint(1,2) # heads or tails
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("\nPlayer will go first.")
        else:
            player_turn = False
            computer_turn = True
            print("\nComputer will go first.")