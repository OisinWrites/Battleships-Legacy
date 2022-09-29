"""
This file holds the class to iniatilise an
instance of the player and the computer as
a player.
The class allows them to take turns by guessing
coordinates and then stores those guesses
so as not to be repeated.

Player imports Board,
and utilities to use
the function of validating coordinates.
"""
from .board import Board
import random
import classes.utilities


class Player:
    def __init__(self, name, size):
        """
        An instance of a player takes in the name given
        by user input, or otherwise 'Computer'. It also
        takes in the size of the board given by user input.
        These inputs are then placed as arguments for the
        Board function.
        Attached to each player is an array of previously
        guessed coordinates, to be used to handle repeated
        guess coordinates, especially against the computers
        random guess function, rather than just human error.
        """
        self.name = name
        self.size = size
        self.board = Board(size, name)
        self.previous_guesses = []

    def make_guess(self):
        """
        This is the function that translates the user's
        input coordinates as tuples relating to ship
        locations.
        It prompts the user for coordinate input.
        It prints an error messages for repeated guesses.
        """
        valid_guess = False
        # valid_guess begins as False and returns when True
        while not valid_guess:
            # begins loop to create valid guess of coordinates
            if self.name == "Computer":
                # gives computer random choice to create tuple of coords
                guess_coordinate = (
                    random.randint(
                        0, self.board.size - 1), random.randint(
                        0, self.board.size - 1))
                # checks if random guess has been made already
                previously_guessed = guess_coordinate in self.previous_guesses
                # repeats loop if guess was made already until new guess made
                if previously_guessed:
                    continue
                # adds guess tp list of made guesses and then makes guess valid
                # for return
                self.previous_guesses.append(guess_coordinate)
                valid_guess = True
            else:
                # when name is not computer, it is the player's guess
                # prompts input from player for coordinates
                guess_coordinate = input(
                    'Select coordinates for'
                    f'missile launch, Captain {self.user}!'
                    '(e.g. 3,4 or 34: ) \n'
                ).strip(" ")

                guess_coordinate = classes.utilities.coord_input
                _validator(guess_coordinate)
                previously_guessed = guess_coordinate in self.previous_guesses

                if previously_guessed:
                    print(
                        f"But Captain {self.user}, we've already"
                        "hit that location, we haven't missiles to spare!"
                        "Surely there's another location the enemy"
                        "could be hiding?"
                    )
                    continue
                else:
                    self.board.display()
                    self.previous_guesses.append(guess_coordinate)
                    valid_guess = True

        return guess_coordinate

    def take_turn(self, opponent):
        """
        This function takes in the logic of the guess function
        and defines the turns between player and computer.
        The relevant board is then updated with the result.
        """
        print(f"{self.name}'s turn")
        guess = self.make_guess()
        guess_hit_check = opponent.board.guess_checker(guess)
        if (guess_hit_check is True) & (self.name == "Computer"):
            print(guess_hit_check)
        self.board.update_board(guess, guess_hit_check, opponent)
        if self.name != "Computer":
            self.board.display()

        else:
            opponent.board.display()
