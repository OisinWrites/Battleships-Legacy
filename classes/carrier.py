"""
This file holds the class for
instances of a "carrier" ship.

It imports the ship class in order to
give itself the inheritance of that class.
"""
from .ship import Ship


class Carrier(Ship):
    def __init__(self, start_coordinate, direction, coordinates, identifier):
        super().__init__(start_coordinate, direction, coordinates, identifier)
        self.name = "Carrier"
        self.length = 5
        self.symbol_list = ["C"] * self.length
        self.identifier_symbols = str(identifier) * self.length
