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
from .boards import Board


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
