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
                changed_direction = self.change_direction()

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

    def try_to_return_to_beginning_of_hit_sequence(self):
        """
        If the computer has established a subsequent hit,
        but hasn't sunk the ship then this function is called on
        to try to run the function to bring it to the original hit.
        """
        if len(self.hit_sequence) > 1:
            self.return_to_beginning_of_hit_sequence()
        else:
            self.get_random_guess()

    def return_to_beginning_of_hit_sequence(self):
        self.hit = self.hit_sequence[0]
        self.directions_tried.clear()
        self.direction = random.choice(["r", "l", "d", "u"])
        self.directions_tried.append(self.direction)
        self.hit_sequence.clear()
        self.hit_sequence.append(self.hit)

    def get_random_guess(self):
        # repeat of random guess function
        valid_guess = False
        while not valid_guess:

            guess_coordinate = (
                    random.randint(
                        0, self.size - 1), random.randint(
                        0, self.size - 1))

            previously_guessed = guess_coordinate in self.previous_guesses
            if previously_guessed:
                continue
            valid_guess = True

        self.directions_tried.clear()
        self.previous_guesses.append(guess_coordinate)
        self.hit_sequence.clear()
        self.hit = None

    def change_direction(self):
        # matches set against set to leave remaining untried directions
        possible_directions = set(["r", "l", "d", "u"]) ^ set(
                                  self.directions_tried)
        # randomises selection between remaining directions and adds
        # the chosen direction to list of those already tried.
        if len(possible_directions) > 0:
            self.direction = random.choice(list(possible_directions))
            self.directions_tried.append(self.direction)
            return True
        return False

    def valid_tile(self, guess):
        row = guess[0]
        column = guess[1]

        if (row < 0) | (row >= self.size) | (
                        column < 0) | (column >= self.size):
            self.change_direction()
            return False

        return True

    def update_hit(self, hit):
        self.hit = hit
        self.hit_sequence.append(hit)

    def has_valid_hit(self):
        # toggles if is in tracker mode
        if self.hit is None:
            return False
        return True
