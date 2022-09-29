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
    name = "Carrier"
    length = 5
    symbol_list = ["C"] * length
