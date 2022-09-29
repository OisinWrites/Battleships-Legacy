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
        self.number_of_ships = int(5 * size/10)
        self.number_of_ships_per_category = 5

        if self.number_of_ships_per_category < 1:
            self.number_of_ships_per_category = 1

        self.ship_board = self.build_board(size)
        self.guess_board = self.build_board(size)
        self.ships = self.build_ships()
        self.ship_map = self.create_ships_coords_map()

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

                # If next tile is unoccupied, add the coordinate to
                # a temporay list and if list is equal to the
                # ship length it is returned to the calling function
                elif not duplicate_tile:
                    temp_ship.append(next_tile)
                    if len(temp_ship) == ship.length:
                        ship.coordinates = temp_ship
                        placement_process = False
                        return ship.coordinates

                # If any tile in the process is occupied a new start coordinate
                # is requested/generated and the process starts again
                else:
                    ship.start_coordinate = (
                        random.randint(
                            0, self.size-1), random.randint(
                            0, self.size-1))
                    ship.direction = random.choice(["r", "d"])
                    break

        return ship.coordinates

    def create_ships_coords_map(self):
        """"
        Creates a dictionary of the fleets coordinates,
        so that damaged ship tiles can be matched against
        locations for game end condition.
        Key = coordinate
        Value = Ship symbol to identify which ship was hit
        """
        ship_log = {}
        for i in range(self.number_of_ships):
            ship_log.update(
                dict(zip(self.ships[i].coordinates,
                         self.ships[i].symbol_list)))
        return ship_log

    def guess_checker(self, guess):
        """
        Checks guess against fleet dictionary.
        Calls method to update ship damage
        """
        result = self.ship_map
        result = result.get(guess)
        ship = None
        self.last_hit_sunk_ship = False
        if result:
            for i in range(self.number_of_ships):
                ship = self.ships[i]
                if result is self.ships[i].symbol_list[0]:
                    self.update_ship_damage(ship)
                    return True
        else:
            return False

    def update_ship_damage(self, ship):
        """"
        Checks through the ships damage tiles and updates as required
        """
        ship.number_of_damaged_tiles = ship.number_of_damaged_tiles + 1
        if ship.number_of_damaged_tiles == ship.length:
            self.sink_ship()

    def sink_ship(self):
        """
        Reduces number of ships by one.
        """
        print(f"{self.user} destroyed a ship!!")

        self.number_of_ships -= 1
        return self.number_of_ships
