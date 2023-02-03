"""
This file holds the class for
instances of a "submarine" ship.

It imports the ship class in order to
give itself the inheritance of that class.
"""
from .ship import Ship


class Submarine(Ship):
    def __init__(self, start_coordinate, direction, coordinates, identifier):
        super().__init__(start_coordinate, direction, coordinates, identifier)
        self.name = "Submarine"
        self.length = 3
        self.symbol_list = ['\U00002693'] * self.length
        self.identifier_symbols = str(identifier) * self.length
