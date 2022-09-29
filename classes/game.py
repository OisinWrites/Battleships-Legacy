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
import utilities


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
        options_menu = True
        while options_menu:
            options = input('Hit enter to begin')
            options_menu = False
            self.create_players()

    def create_players(self):
        """"
        Takes player name and creates player and computer objects.
        """
        user = utilities.name_input()
        size = utilities.size_input()
        user = Player(user, size)
        computer = Player("Computer", size)
        self.play_game(user, computer)


    def play_game():
        """
        Initites the turn functions established in player class.
        """

    def display_both_boards():
        """
        Prints player's and computer's boards in terminal
        """

    def restart_game():
        """
        Deletes all objects and refreshes to welcome screen.
        """
