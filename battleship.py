
import random

HIT_CHAR = 'x'
MISS_CHAR = 'o'
BLANK_CHAR = '.'
HORIZONTAL = 'h'
VERTICAL = 'v'
MAX_MISSES = 20
SHIP_SIZES = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}
NUM_ROWS = 10
NUM_COLS = 10
ROW_IDX = 0
COL_IDX = 1
MIN_ROW_LABEL = 'A'
MAX_ROW_LABEL = 'J'


def get_random_position():
    """Generates a random location on a board of NUM_ROWS x NUM_COLS."""

    row_choice = chr(
                    random.choice(
                        range(
                            ord(MIN_ROW_LABEL),
                            ord(MIN_ROW_LABEL) + NUM_ROWS
                        )
                    )
    )

    col_choice = random.randint(0, NUM_COLS - 1)

    return (row_choice, col_choice)


def play_battleship():
    """Controls flow of Battleship games including display of
    welcome and goodbye messages.

    :return: None
    """

    print("Let's Play Battleship!\n")

    game_over = False

    while not game_over:

        game = Game()
        game.display_board()

        while not game.is_complete():
            pos = game.get_guess()
            result = game.check_guess(pos)
            game.update_game(result, pos)
            game.display_board()

        game_over = end_program()

    print("Goodbye.")

### DO NOT EDIT ABOVE (with the exception of MAX_MISSES) ###


class Ship:

    def __init__(self, name, start_position, orientation):
        """Creates a new ship with the given name, placed at start_position in the
    provided orientation. The number of positions occupied by the ship is determined
    by looking up the name in the SHIP_SIZE dictionary.
    :param name: the name of the ship
    :param start_position: tuple representing the starting position of ship on the board
    :param orientation: the orientation of the ship ('v' - vertical, 'h' - horizontal)
    :return: None
    """
        self.name = name
        self.positions = {}
        self.orientation = orientation
        self.sunk = False

        if self.orientation == VERTICAL:
            for position in range(SHIP_SIZES[self.name]):
                self.positions[(chr(ord(start_position[0]) + position)), start_position[1]] = False
        else:
            for position in range(SHIP_SIZES[self.name]):
                self.positions[(start_position[0], start_position[1] + position)] = False



class Game:

    def __init__(self, max_misses = MAX_MISSES):
        """ Creates a new game with max_misses possible missed guesses.
        The board is initialized in this function and ships are randomly
        placed on the board.
        :param max_misses: maximum number of misses allowed before game ends
        """
        self.max_misses = max_misses
        self.ships = []
        self.guesses = []
        self.board = {}
        self.initialize_board()
        self.create_and_place_ships()

    def initialize_board(self):
        """Sets the board to it's initial state with each position occupied by
        a period ('.') string.
        :return: None
        """

        for position in range(NUM_COLS):
            self.board[(chr(ord(MIN_ROW_LABEL) + position))] = [BLANK_CHAR] * NUM_COLS

    def in_bounds(self, start_position, ship_size, orientation):
        """Checks that a ship requiring ship_size positions can be placed at start position.
        :param start_position: tuple representing the starting position of ship on the board
        :param ship_size: number of positions needed to place ship
        :param orientation: the orientation of the ship ('v' - vertical, 'h' - horizontal)
        :return status: True if ship placement inside board boundary, False otherwise


"""
        if orientation == VERTICAL:
            for position in range(ship_size):
                if chr(ord(start_position[0]) + position) not in self.board:
                #if (chr(ord(start_position[0]) + position) > MAX_ROW_LABEL) or (ord(start_position[0]) + position) < ord(MIN_ROW_LABEL):
                    return False
            return True
        else:
            for position in range(ship_size):
                if start_position[1] + position >= NUM_COLS:
                    return False
            return True



    def overlaps_ship(self, start_position, ship_size, orientation):
        """Checks for overlap between previously placed ships and a potential new ship
        placement requiring ship_size positions beginning at start_position in the
        given orientation.
        :param start_position: tuple representing the starting position of ship on the board
        :param ship_size: number of positions needed to place ship
        :param orientation: the orientation of the ship ('v' - vertical, 'h' - horizontal)
        :return status: True if ship placement overlaps previously placed ship, False otherwise
        """

        if orientation == VERTICAL:
            for position in range(ship_size):
                new_position = (chr(ord(start_position[0]) + position), start_position[1])
                for j in range(len(self.ships)):
                    if new_position in self.ships[j].positions:
                        return True
            return False
        else:
            for position in range(ship_size):
                new_position = (start_position[0], start_position[1] + position)
                for j in range(len(self.ships)):
                    if new_position in self.ships[j].positions:
                        return True
            return False


    def place_ship(self, start_position, ship_size):
        """Determines if placement is possible for ship requiring ship_size positions placed at
        start_position. Returns the orientation where placement is possible or None if no placement
        in either orientation is possible.
        :param start_position: tuple representing the starting position of ship on the board
        :param ship_size: number of positions needed to place ship
        :return orientation: 'h' if horizontal placement possible, 'v' if vertical placement possible,
            None if no placement possible
        """

        if self.in_bounds(start_position, ship_size, HORIZONTAL) is True and self.overlaps_ship(start_position, ship_size, HORIZONTAL) is False:
            return HORIZONTAL
        elif self.in_bounds(start_position, ship_size, VERTICAL) is True and self.overlaps_ship(start_position, ship_size, VERTICAL) is False:
            return VERTICAL
        else:
            return None

    def create_and_place_ships(self):
        """Instantiates ship objects with valid board placements.
        :return: None
        """

        for ship in self._ship_types:
            random_pos = get_random_position()
            placement = self.place_ship(random_pos, SHIP_SIZES[ship])
            while placement is None:
                random_pos = get_random_position()
                placement = self.place_ship(random_pos, SHIP_SIZES[ship])

            ship = Ship(ship, random_pos, placement)
            self.ships.append(ship)

    def get_guess(self):
        """Prompts the user for a row and column to attack. The
        return value is a board position in (row, column) format
        :return position: a board position as a (row, column) tuple
        """

        running = True
        row = input("Enter a row: ")
        while running is True:
            if ord(row) in range(ord('A'), ord('K')):
                col = int(input("Enter a column: "))
                if col in range(9):
                    running = False
                    return row, col
            else:
                row = input("Enter a row: ")


    def check_guess(self, position):
        """Checks whether or not position is occupied by a ship. A hit is
        registered when position occupied by a ship and position not hit
        previously. A miss occurs otherwise.
        :param position: a (row,column) tuple guessed by user
        :return: guess_status: True when guess results in hit, False when guess results in miss
        """

        sunks = False
        for ship in self.ships:
            if position in ship.positions and ship.positions.get(position) is False:
                ship.positions[position] = True
                sunks = True
            elif position not in ship.positions or ship.positions.get(position) is True:
                return sunks

            counter = 0
            for position in ship.positions:
                if ship.positions.get(position) is True:
                    counter += 1
            if counter == len(ship.positions):
                ship.sunk = True
                print("You sunk the " + ship.name + '!')
                sunks = True
        return sunks

    def update_game(self, guess_status, position):
        """Updates the game by modifying the board with a hit or miss
        symbol based on guess_status of position.
        :param guess_status: True when position is a hit, False otherwise
        :param position:  a (row,column) tuple guessed by user
        :return: None
        """

        if self.board[position[ROW_IDX]][position[COL_IDX]] == BLANK_CHAR:
            if guess_status is False:
                self.board[position[ROW_IDX]][position[COL_IDX]] = MISS_CHAR
            else:
                self.board[position[ROW_IDX]][position[COL_IDX]] = HIT_CHAR
        if guess_status is False:
            self.guesses.append(position)

    def is_complete(self):
        """Checks to see if a Battleship game has ended. Returns True when the game is complete
        with a message indicating whether the game ended due to successfully sinking all ships
        or reaching the maximum number of guesses. Returns False when the game is not
        complete.
        :return: True on game completion, False otherwise
        """

        sunk_ship = 0
        for ship in self.ships:
            if ship.sunk is True:
                sunk_ship += 1

        if sunk_ship == len(self.ships):
            print("YOU WIN!")
            return True
        elif len(self.guesses) == MAX_MISSES:
            print("SORRY! NO GUESSES LEFT.")
            return True
        else:
            return False



    ########## DO NOT EDIT #########
    
    _ship_types = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
    
    
    def display_board(self):
        """ Displays the current state of the board."""

        print()
        print("  " + ' '.join('{}'.format(i) for i in range(len(self.board))))
        for row_label in self.board.keys():
            print('{} '.format(row_label) + ' '.join(self.board[row_label]))
        print()

    ########## DO NOT EDIT #########


def end_program():
    """Prompts the user with "Play again (Y/N)?" The question is repeated
    until the user enters a valid response (Y/y/N/n). The function returns
    False if the user enters 'Y' or 'y' and returns True if the user enters
    'N' or 'n'.

    :return response: boolean indicating whether to end the program
    """

    answers = ('Y', 'y', 'N', 'n')
    user = ''
    while user not in answers:
        user = input("Play again (Y/N)? ")
    print()

    if user == 'N' or user == 'n':
        return True
    else:
        return False


def main():
    """Executes one or more games of Battleship."""

    play_battleship()


if __name__ == "__main__":
    main()
