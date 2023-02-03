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
            classes.utilities.clear_display()
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

    def play_game(self, player, computer):
        """
        Initites the turn functions established in player class.
        Checks for game end conditions and give player a way to exit the game.
        """
        game_over = False
        while not game_over:
            player.take_turn(computer)
            # checks for win returns boolean
            game_over = computer.board.are_all_ships_sunk()
            computer.board.update_sunk_ships(player)
            # if win print and exit
            if game_over is True:
                print("Captain, we've won! With your infallible"
                      "battle strategy how could we have not succeeded?")
                input("Hit enter to voyage home.").strip(" ")
                self.restart_game(player, computer)
                break
            game_over = player.out_of_guesses()
            if game_over is True:
                print("You lose. \n"
                      "We've used up all of our missiles... \n")
                input("Hit any key to continue").strip(" ")
                self.restart_game(player, computer)
                break
            # offer human player a way to quit the round.
            user_input = input(
                            "Hit R and enter for a tactical retreat\n"
                            "to the Welcome Screen or hit enter\n"
                            "to stand your ground! \n"
                              ).strip(" ")
            if user_input.lower() == "r":
                self.restart_game(player, computer)
                break

            # repeats the above for the computer player
            computer.take_turn(player)
            game_over = player.board.are_all_ships_sunk()
            player.board.update_sunk_ships(computer)
            self.display_stats(player, computer)
            if game_over is True:
                print("We've lost Captain, all vessels are scuppered. \n")
                input("Hit enter to surrender..").strip(" ")
                self.restart_game(player, computer)
                break

    @staticmethod
    def display_stats(player, computer):
        print(player.name +
              " has " + str(player.turns_available) + " guesses left")
        print("Computer has "
              + str(computer.board.number_of_ships_remaining) + " of",
              str(computer.board.number_of_ships) + " ships left")
        print(player.name + " has "
              + str(player.board.number_of_ships_remaining) + " of",
              str(player.board.number_of_ships) + " ships left \n")

    @staticmethod
    def display_both_boards(player, computer):
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
