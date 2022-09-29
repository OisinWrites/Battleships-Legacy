"""
This file holds the class for
instances of a "frigate" ship.

It imports the ship class in order to
give itself the inheritance of that class.
"""
from ship import Ship


class Frigate(Ship):
    def __init__(self, start_coordinate, direction, coordinates, identifier):
        super().__init__(start_coordinate, direction, coordinates, identifier)
        self.name = "Frigate"
        self.length = 4
        self.symbol_list = ["F"] * self.length
        self.identifier_symbols = str(identifier) * self.length
