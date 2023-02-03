"""
This file holds the class for
instances of a "patrol" ship.

It imports the ship class in order to
give itself the inheritance of that class.
"""
from .ship import Ship


class Patrol(Ship):
    def __init__(self, start_coordinate, direction, coordinates, identifier):
        super().__init__(start_coordinate, direction, coordinates, identifier)
        self.name = "Patrol"
        self.length = 2
        self.symbol_list = ['\U0001F6A4'] * self.length
        self.identifier_symbols = str(identifier) * self.length
