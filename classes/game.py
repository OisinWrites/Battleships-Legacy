"""
This file holds the logic for how the game
operates. It is the file called on by run.py,
and it calls on the other classes.
It will call on the other classes and functions
to handle the display, the player and
computer turns, and control game end conditions.

Game imports utilities to clear display. It imports
player so that it can call on the functions that
intialise a player, which in turn is handling the
board class, which handles the varied ship subclasses,
wherein the overarching ship class is nested at the
very bottom of the chain.
"""
from .player import Player


class Game:
    """
    Calls in all other class, objects, and methods, and
    assembles into one chain of logic.
    """

    def __init__(self):
        self.welcome_screen()

    def welcome_screen(self):
        """
        Function displays welcome screen with ASCII art
        """
        print("""______       __   __   __
                |   __ .---.-|  |_|  |_|  .-----.
                |   __ |  _  |   _|   _|  |  -__|
                |______|___._|____|____|__|_____|
                           __    __
                    .-----|  |--|__.-----.-----.
                    |__ --|     |  |  _  |__ --|
                    |_____|__|__|__|   __|_____|
                                   |__|
        """
              )
