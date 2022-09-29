"""
The utilities file is where functions are stored
to clear the display, return error messages for
invalid inputs.
The inputs to be handled are:
1) Player name
2) Board size
3) Player's ship placement

Utilities will import os to identify the current
operating system for purposes of identifying
relevant close or clear command.
"""
import os


def size_input():
    # Take and validate size
    valid_size = False
    while not valid_size:
        size = input("How many knots from the coast?")
        if len(size.strip(" ")) == 0:
            print("Surely we haven't run aground?")
            continue


def name_input():
    # Take and validate name
    valid_name = False
    while not valid_name:
        name = input("To whom do we report, sir?")
        if len(name.strip(" ")) == 0:
            print("Apologies sir, the missiles have left me half deaf."
                  "Could you repeat that, please?")
            continue

        elif name.lower() == "computer":
            print("But sir, that would make you the enemy!?")
            continue

        name = string.capwords(name)
        print(f"Welcome Captain {name}! We await your orders")
        return name


def duplicate_tile_check():
    # Checks if tile is already occupied
def coord_input_validator():
    # Validates coordinates, and returns errpr msg function if not
def coord_error_msg():
    # Error message to retry entering coords
def clear_display():
    # Clears console. Handles for different operating systems thanks to import os
