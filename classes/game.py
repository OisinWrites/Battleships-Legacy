"""
This file holds the logic for how the game
operates. It is the file called on by run.py,
and it calls on the other classes.
It will call on the other classes and functions
to handle the display, the player and
computer turns, and control game end conditions.

Game imports utilities to clear display. It imports
player so that it can call on the functions that
intialise a player, which in turn is handling the
board class, which handles the varied ship subclasses,
wherein the overarching ship class is nested at the
very bottom of the chain.
"""
