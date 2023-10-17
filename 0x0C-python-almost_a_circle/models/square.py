#!/usr/bin/python3
"""Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square (default is 0).
            y (int, optional): The y-coordinate of the square (default is 0).
            id (int, optional): An optional argument representing the unique
            identifier.
                If not provided, a new identifier will be generated based on
                the Base class attribute __nb_objects.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Return the string representation of the Square.

        Returns:
            str: The string representation of the Square.
        """
        aid = self.id
        ax = self.x
        ay = self.y
        return "[Square] ({}) {}/{} - {}".format(aid, ax, ay, self.size)
