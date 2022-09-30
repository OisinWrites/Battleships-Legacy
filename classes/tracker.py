"""
In this file I am attempting to give the computer's turn
some intelligent decision making. Some games of battleship
I've seen the computer continue to make random guesses after
it finds a ship. Here I'm trying to get it to hunt the rest of
the ship down, before resuming its random guesses.
"""
import random


class Tracker:
    def __init__(self, hit, size, previous_guesses):
        self.hit = hit
        self.size = size
        self.direction = random.choice(["r", "l", "d", "u"])
        self.previous_guesses = previous_guesses
        self.directions_tried = []
        self.hit_sequence = []
        self.hit_sequence.append(hit)
        self.directions_tried.append(self.direction)

    def get_guess(self):
        row = self.hit[0]
        column = self.hit[1]
        next_guess = None
        valid_guess = False

        while not valid_guess:
            # makes a random choice around its original hit
            if self.direction == "d":
                next_guess = (
                    row + 1,
                    column)
            elif self.direction == "r":
                next_guess = (
                    row,
                    column + 1)
            elif self.direction == "u":
                next_guess = (
                    row - 1,
                    column)
            elif self.direction == "l":
                next_guess = (
                    row,
                    column + -1)
            """
            If the computer has followed a line of succesful hits, and
            misses without the boat being sunk, it must start again at
            beginning of sequence and go in the opposite direction.
            """
            previously_guessed = next_guess in self.previous_guesses
            if previously_guessed:
                changed_direction = self.change_direction_on_duplicate()

                if changed_direction is True:
                    next_guess = self.hit
                    continue
                else:
                    if len(self.hit_sequence) > 1:
                        self.return_to_beginning_of_hit_sequence()
                    else:
                        self.get_random_guess()

            if self.valid_tile(next_guess) is False:
                next_guess = self.hit
                if len(self.directions_tried) < 4:
                    continue
                else:
                    if len(self.hit_sequence) > 1:
                        self.return_to_beginning_of_hit_sequence()
                    else:
                        self.get_random_guess()

            valid_guess = True

        return next_guess