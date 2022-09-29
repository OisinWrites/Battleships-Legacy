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
import string


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


def duplicate_tile_check(ship, occupied_tiles, next_tile):
    # Checks if tile is already occupied
    for list in occupied_tiles:
        for _ in list:
            if next_tile in list:
                return True
            elif ship.start_coordinate in list:
                return True


def coord_input_validator(user_input):
    # Validates coordinates, and returns error msg function if not
    # Handles different acceptable input formats e.g. 34 & 3,4.
    valid_input = False
    while not valid_input:
        try:

            if len(user_input) < 2 or len(user_input) > 3:
                raise ValueError
            elif len(user_input) == 2:
                user_input = (tuple(int(i) for i in user_input))
                return user_input

            elif len(user_input) < 4:
                if "," in user_input:
                    user_input = user_input.split(",")
                    user_input = (tuple(int(i) for i in user_input))
                    return user_input
                else:
                    user_input = coord_error_msg()
                    continue

        except ValueError:
            user_input = coord_error_msg()


def coord_error_msg():
    # Error message to retry entering coords
    """"
    Advices input is invalid,
    Requests new input and offers guidance on
    what qualifies as a valid input
    """
    new_guess = input(f"Captain {name}, my tinnitus must be affecting"
                      "my hearing again. Surely you meant to target"
                      "coordinates in the sea?"
                      "(e.g. 4,5 or 45): \n").strip(" ")
    return new_guess


def clear_display():
    # Clears console. Handles for different operating systems thanks
    # to import os
    """"
    Clears the console
    """
    command = 'clear'
    if os.name in (
            'nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
