#!/usr/bin/python3
"""
A class that defines a square.
"""


class Square:
    """
    A class that defines a square.

    Private instance attribute:
    __size: The size of the square.

    Instantiation:
    __init__(self, size)
    Initializes a new Square instance with the given size.

    Attributes:
    __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        """
        self.__size = size
