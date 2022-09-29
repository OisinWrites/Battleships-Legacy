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

    def build_ships():
