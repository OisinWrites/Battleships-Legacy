"""
Contains the functions to initalise the
boards, declares their objects and methods.
A board for the player shows the players ships,
and updates to show the computers guesses.
A board for the computer, only marks the players
guesses, and the computer's ships are hidden.

Board will import random to give the program
the ability to give the computer's guesses
randomisation. It will call on the untilities class
to use the functions to clear the display, and
to verify that guesses are not being repeated.
Board calls on each subclass of ship;
carrier, destroyer, frigate, patrol, and submarine.
"""
