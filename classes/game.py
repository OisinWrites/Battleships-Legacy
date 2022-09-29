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
import classes.utilities


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
        print("""
                 ______       __   __   __
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
        user = classes.utilities.name_input()
        size = classes.utilities.size_input()
        user = Player(user, size)
        computer = Player("Computer", size)
        self.play_game(user, computer)

    def play_game():
        """
        Initites the turn functions established in player class.
        Checks for game end conditions and give player a way to exit the game.
        """
        game_over = False
        while not game_over:
            player.take_turn(computer)
            # checks for win returns boolean
            game_over = computer.board.are_all_ships_sunk()
            # if win print and exit
            if game_over is True:
                self.display_both_boards(player, computer)
                print("Captain, we've won! With your infallible"
                      "battle strategy how could we have not succeeded?")
                input("Hit enter to voyage home.").strip(" ")
                self.restart_game(player, computer)
                break
            # offer human player a way to quit the round.
            user_input = input("Hit R and enter for a tactical retreat to the"
                               "Welcome Screen").strip(" ")
            if user_input.lower() == "R":
                self.restart_game(player, computer)
                break

            # repeats the above for the computer player
            computer.take_turn(player)
            game_over = player.board.are_all_ships_sunk()
            self.display_stats(player, computer)
            if game_over is True:
                self.display_both_boards(player, computer)
                print("We've lost Captain, all vessels are scuppered.")
                input("Hit enter to surrender..").strip(" ")
                self.restart_game(player, computer)
                break

    def display_both_boards(self, player, computer):
        """
        Prints player's and computer's boards in terminal
        """
        player.board.display()
        computer.board.display()

    def restart_game(self, player1, player2):
        """
        Deletes player object and their possessed ship, and boards
        Returns users back to the welcome screen
        """
        del (player1)
        del (player2)
        classes.utilities.clear_display()
        self.welcome_screen()
