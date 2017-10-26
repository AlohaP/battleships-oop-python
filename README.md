# Battleship in the OOP way

## The story
    Enemy ships incoming! The battleships is the one of most popular games in the world.
    Now you can play with your friends without internet connection.
    If you want you can play with super inteligent CPU at one of three difficulty levels.
    Have fun.

## Specification


### `__main.py__`

`print_program_menu(menu_commands)`
    prints program menu

`highscore_creation(game, player, start_time)`
    create highscore

`high_score_export(player, filename='highscores.txt', mode = 'ab')`
    export highscore

`high_score_presentation(filename='highscores.txt', mode='rb')`
    show highscore


### `__square.py__`

### Class Square


__Instance Methods__


##### `__init__(self, sign, name)`

  Constructs a Square object

##### `__str__(self)`

  Returns a square sign.

##### `change_to_ship(self)`

  Changes squares sign to "@"

##### `change_to_hit(self)`

  Changes hitted squares to "X" or "O"

##### `change_to_sunk(self)`

  Changes sunk atribute to True

__Instance Attributes__


* `sign`
  - data: string
  - description: sign representation of square object

* `name`
  - data: string
  - description: string representation of coordinates

* `sunk`
  - data: bool
  - description: if is True the square is part of sunk ship

* `hidden_ship`
  - data: bool
  - description: if is True the square contains ship wich is hidden for enemy


### `__game.py__`

### Class PlayBattleships


__Instance Methods__

##### `__init__(self, player1, player2)`

  Constructs new game object

##### `placement_validation(self, ship_list, player, player_ship, ship)`

    Check if ship can be putted here

##### `create_player_ships(self, player)`

    Allow player to put his ships

##### `change_ships_to_hidden(self, player1, player2)`

    Change all ships to hidden

##### `boards_setup(self, player1, player2)`

    Board creation wizard

##### `turn_mechanics(self, player1, player2)`

    Makes everything what is needed in turn

##### `player_victory(self, player)`

    Prints victory string

##### `check_if_warships_alive(self, player1, player2)`

    Checks if any of warships alive

##### `game_flow(self, player1, player2)`

    Changes turns of players


__Instance Attributes__

* `player1`
  - data: object
  - description: stores a player object

* `player2`
  - data: object
  - description: stores a player object


### `__ship.py__`


### Class Ship(Square)


__Class Attributes__

* `ships`
  - data: dictionary
  - description: stores ship names and lenght

__Instance Methods__

##### `__init__(self, name, vertical)`

    Constructs a new ship object

##### `change_squares_to_ship(self)`

    Change all signs of squares belgongs to ship to "@"

##### `check_if_sunk(self)`

    Checks if ship is sunk

__Instance Attributes__


* `coordinates`
  - data: list
  - description: stores coordinates of all squares belongs to ship

* `is_sunk`
  - data: bool
  - description: if ship is sunk value is True

* `vertical`
  - data: bool
  - description: if ship is vertical value is True

* `name`
  - data: string
  - description: stores a name of ship

* `lenght`
  - data: integer
  - description: stores a lenght of ship


### `__ocean.py__`


### Class Ocean

__Class Attributes__

* `W`
  - data: string
  - description: stores white color string

* `R`
  - data: string
  - description: stores red color string


__Instance Methods__

##### `__init__(self)`

  Creates a new board

##### `read_board_from_file(self)`

  Creates list of lists from *board.txt*

##### `print_board(self)`

  Show board

##### `find_object(self, coordinates)`

  Returns object with declared coordinates

__Class Attributes__


* `ocean_board`
  - data: list
  - description: stores list of lists with board


### Class Player

This is the file cointains Players data and methods

__atributes__

*    `warships`

    - data: list
    - description: stores ships

*    `highscore`

    - data: list
    - description: stores highscore data

*    `name`

    - data: string
    - description: player name

*    `board`

    - data: Ocean() object
    - description: creates board (Ocean object)

*    `view`

    - data: Ocean() object
    - description: creates opponent board (Ocean object)

__Instance methods__

* ##### `__init__(self, name)`

    construcs player object

* `print_boards(self)`

    print players board

* `shoot_to_ship(self, coordinates)`

    changes squares object to look hitted

* `get_hit(self, coordinates)`

    changes your ship squares object to look hitted

* `get_ship_coordinates(self, name, coordinates, vertical)`

    create ship object and returns it

* `check_if_square_sign_dot(self, square)`

    check if sign of board is element of ocean and return True or False

* `validate_if_ship_is_near(self, ship)`

    checks all squares next to ship if it is a any ship near

* `check_if_validate_positive(self, validation_table)`

    checks all squares next to ship if it is a any ship near


### `__cpu.py__`

### class PlayBattleshipsWithCPU(PlayBattleships)

    This is the file cointaing AI logic

__atributes__

*    `cpu`

    - data: Player object
    - description: creates player object

*    `difficulty`

    - data: string
    - description: stores information about difficulty

*    `shooted_cords`

    - data: empty list
    - description: stores shooted coordinates 

*    `hitted_and_not_sunk_cords`

    - data: empty list
    - description: stored hitted but not sunk coordinates

*    `chars`

    - data: list
    - description: stores available chars (to coordinate)

__Instance methods__

* ##### `__init__(self, player, cpu, difficulty) `

    construcs PlayBattleshipsWithCPU object

* `get_random_cords(self, for_placement)`

    return random coordinates for AI
    if for_placement is True not stores cords as shoots

* `aim_in_cross(self)`

    aims in 4 directions from previous shoot

* `computer_shoot(self)`

    returns coordinates of computer shoot

* `aim_in_line(self)`

    aim in two directions if two coordinates of ship is known

* `create_CPU_ships(self, cpu)`

    puts CPU ships on board

* `boards_setup(self)`

    boards setup wizard

* `turn_mechanics(self, player1, player2)`

    makes everything what is need in turn

* `player_victory(self, player)`

    print victory string

### `__howtoplay.py__`

__Instance methods__

* `instructions_display()`

    prints instructions of game
