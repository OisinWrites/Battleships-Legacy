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

    def __init__(self,)

    def build_board()

    def build_ships()