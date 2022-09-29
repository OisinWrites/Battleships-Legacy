class Ship:
    """
    Creates share properties of the ship class
    which used by the subclasses to initialise
    a ship object.
    """
    def __init__(self, start_coordinate, direction, coordinates):
        """
        Each ship on intialisation of its instance must establish its
        starting point: the primary coordinates,
        direction: horizontal or vertical to the board
        coordinates: the list of coordinates it occupies, including the
        start coordinate, determined by the subclasses' length object
        and relevant function.
        Each ship will essentially be this set of coordinates.

        EAch instance must then handle how many of its coordinates
        have been targeted with valid hits by the opponent, and
        check whether it is sunk where the damaged tile set equals
        the coordinates set.
        """
        self.start_coordinate = start_coordinate
        self.direction = direction
        self.coordinates = coordinates
        self.number_of_damaged_tiles = 0
        self.is_sunk = False
