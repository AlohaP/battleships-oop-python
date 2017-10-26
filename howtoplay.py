def instructions_display():
    print('''
____    __    ____  _______  __        ______   ______   .___  ___.  _______    .___________.  ______   
\   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|   |           | /  __  \  
 \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__      `---|  |----`|  |  |  | 
  \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|         |  |     |  |  |  | 
   \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____        |  |     |  `--'  | 
    \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|       |__|      \______/    
    
                     ________  ________  _________  _________  ___       _______   ________  ___  ________  ________      
                    |\   __  \|\   __  \|\___   __'_'___   __' '  \     |\  ___ \ |\   ____\|\  \|\   __  \|\   ____\     
                    \ \  \|\ /\ \  \|\  \|___ \  \_\|___ \  \_\ \  \    \ \   __/|\ \  \___|\ \  \ \  \|\  \ \  \___|_    
                     \ \   __  \ \   __  \   \ \  \     \ \  \ \ \  \    \ \  \_|/_\ \_____  \ \  \ \   ____\ \_____  \   
                      \ \  \|\  \ \  \ \  \   \ \  \     \ \  \ \ \  \____\ \  \_|\ \|____|\  \ \  \ \  \___|\|____|\  \  
                       \ \_______\ \__\ \__\   \ \__\     \ \__\ \ \_______\ \_______\____\_\  \ \__\ \__\     ____\_\  \ 
                        \|_______|\|__|\|__|    \|__|      \|__|  \|_______|\|_______|\_________\|__|\|__|    |\_________'
                                                                                     \|_________|             \|_________''')
print('''1) How to play:

The object of this game is to try and sink all of the other player's before they sink all of your ships!
You have access to two boards, one displays your ships, other one shows your guesses.

2) Starting a New Game:

~ You have and option to play versus CPU with 3 difficulty levels or in old school Hot Seat manner Player vs Player
~ Each player places the 5 ships somewhere on their board.  
~ The 5 ships are:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).  
~ The ships can only be placed vertically or horizontally. 
~ Diagonal placement is not allowed. 
~ No part of a ship may hang off the edge of the board.  
~ Ships may not overlap each other.  
~ No ships may be placed on another ship. 

3) Game flow:

~ Players guess in turns, you will get information X if ship got hit, O if you hit an ocean, @ represents ship
~ When all of your ships got hit you lose!

             __    __       ___   ____    ____  _______     _______  __    __  .__   __.     __   __   __  
            |  |  |  |     /   \  \   \  /   / |   ____|   |   ____||  |  |  | |  \ |  |    |  | |  | |  | 
            |  |__|  |    /  ^  \  \   \/   /  |  |__      |  |__   |  |  |  | |   \|  |    |  | |  | |  | 
            |   __   |   /  /_\  \  \      /   |   __|     |   __|  |  |  |  | |  . `  |    |  | |  | |  | 
            |  |  |  |  /  _____  \  \    /    |  |____    |  |     |  `--'  | |  |\   |    |__| |__| |__| 
            |__|  |__| /__/     \__\  \__/     |_______|   |__|      \______/  |__| \__|    (__) (__) (__) 
                                                                                                                                         
''')
