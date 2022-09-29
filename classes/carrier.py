"""
This file holds the class for
instances of a "carrier" ship.

It imports the ship class in order to
give itself the inheritance of that class.
"""
from .ship import Ship


class Carrier(Ship):
    """
    The Carrier class is the largest ship
    at length of 5 tiles on the board, or
    5 coordinates. On the players board it will
    be mapped using a straight line
    of 5 of the letter 'C'.
    The Ship class has been imported from .ships so
    that the Carrier class can use it as an argument,
    giving this class inheritance of the former.
    """
    def __init__(self, start_coordinate, direction, coordinates, identifier):
        super().__init__(start_coordinate, direction, coordinates, identifier)
        self.name = "Carrier"
        self.length = 5
        self.symbol_list = ["C"] * self.length
        self.identifier_symbols = str(identifier) * self.length
