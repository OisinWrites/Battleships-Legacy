"""
Contains the functions to initalise the
boards, declares their objects and methods.
A board for the player shows the players ships,
and updates to show the computers guesses.
A board for the computer, only marks the players
guesses, and the computer's ships are hidden.

Board will import random to give the program
the ability to give the computer's guesses
randomisation. It will call on the untilities class
to use the functions to clear the display, and
to verify that guesses are not being repeated.
Board calls on each subclass of ship;
carrier, destroyer, frigate, patrol, and submarine.
"""
from .carrier import Carrier
import random


class Board:
    """
    This class needs to initialise instances of boards
    for player and computer, and take in the adjustable size.
    It needs a function to print the board in the display.
    It needs to be able to identify which of the 'coordinates'
    in its display are associated with the tuples that are ship
    locations, so that it can visually reflect hits and misses,
    and show the player's ship locations.
    """

    def __init__(self, size, user):
        """
        Each instance of a board needs to take in its
        adjustable size, which will be set by the player,
        and whether it is the player's board or the
        computer's.
        The third object of "number of ships" will
        determine how many ships are to be placed
        in a board of variable size, and allow for
        scalability.
        """
        self.size = size
        self.user = user
        self.number_of_ships = int(size/2 + 1)

    def build_board(size):
        """
        Will create a square of '#'s scaling with size.
        """
        return [['#' for count in range(size)] for count in range(size)]

    def display_board(self):
        """
        Prints the users view of the boards in the terminal.
        Prints a header using the user's input name, and subheaders
        for each board, parted by " " spaces, calculated by the 80
        character board less characters used in string.
        """
        print((" ") * 30 + f"This is {self.user}'s board")
        print((" ") * 3 + "Friendly Waters" + (" ") * 44 + "Enemy Waters")

        # code to print top 'x axis' coordinates, scalable to size
        rowHeader = " "

        for i in range(self.size):
            rowHeader = rowHeader + str(i) + "  "

        print("   " + rowHeader + (" ") * (9) + rowHeader)
        """
        This code is to print a grid of rows, with
        as many rows as there are x ""columns"",
        with an index on the left and adequate spacing.
        """
        for index, row in enumerate(zip(self.ship_board, self.guess_board)):
            print(
                # number rows on friendly waters board
                f'{str(index) + " |":3s}',
                # print row by row with 3 spaces between
                ''.join(f'{str(x):3s}' for x in row[0]),
                # separate the two boards by 9 spaces
                ' ' * 9,
                # number rows on enemy waters board
                f'{str(index) + " |" :3s}',
                # print row by row with 3 spaces between
                ''.join(f'{str(x):3s}' for x in row[1]),
            )
        print("\n")

    def build_ships(self):
        """
        Function to build ships on boards,
        handles an array of the ship types,
        records the ships being used per instance of board,
        in that different size boards won't use all,
        and catalogues the coordinates of all used ships,

        """
        ship_types = [
            Carrier,
            Destroyer,
            Frigate,
            Patrol,
            Submarine
            ]

        ships = []
        ships_coordinates = []

        ship_type_index = 0
        for i in range(self.number_of_ships):
            # chooses random number between 0 and board size.
            random_start = (random.randint(0, self.size-1),
                            random.randint(0, self.size-1))
            # chooses random direction between vertical and horizontal.
            random_direction = random.choice(["v", "h"])

            ship_instance = ship_types[ship_type_index](
                random_start, random_direction, [])

            self.build_ship(ship_instance, ships_coordinates)
            ships_coordinates.append(ship_instance.coordinates)

            self.initial_placement(ship_instance)

            ships.append(ship_instance)
            ship_type_index = ship_type_index + 1
            if ship_type_index == len(ship_types):
                ship_type_index = 0

        if self.user != "Computer":
            self.display()
        return ships

    def build_ship(self, ship, occupied_tiles):
        """
        Function builds the ship in the chosen direction and advises user if
        the intended location is already occupied.

        If already occupied it generates randomly a new start coordinate, from
        which to build the ship.
        """
        placement_process = True

        while placement_process:
            # instance marked as temp while testing validity during process
            temp_ship = [ship.start_coordinate]
            # for each position of a ship, determined by its length,
            # repeat process of setting coordinates of each tile occupied
            for i in range(1, ship.length):
                # for vertical ships
                if ship.direction == "v":
                    next_tile = (
                        ship.start_coordinate[0] + i,
                        ship.start_coordinate[1]
                    )
                    index_to_increment = 0
                # for horizontal ships
                elif ship.direction == "h":
                    next_tile = (
                        ship.start_coordinate[0],
                        ship.start_coordinate[1] + i,
                    )
                    index_to_increment = 1

                # Check if ship will go over the board edge
                # and requests/generates new start coordinate if required
                if ship.start_coordinate[index_to_increment] + \
                        (ship.length - 1) > (self.size-1):

                    ship.start_coordinate = (
                        random.randint(
                            0, self.size-1), random.randint(
                            0, self.size-1))
                    ship.direction = random.choice(["h", "v"])
