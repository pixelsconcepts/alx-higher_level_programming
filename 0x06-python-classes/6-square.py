#!/usr/bin/python3
"""
A class Square that defines a square by

Private instance attribute: size
Instantiation with size (no type/value verification)
"""


class Square:
    """
    An object of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square (default is 0).
            position (tuple, optional): The position of the square
            (default is (0, 0)).

        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
        int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Args:
            value (tuple): The new position of the square as a tuple of
            two positive integers.

        Raises:
            TypeError: If the value is not a tuple of two positive integers.

        """

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(x, int) and x > 0 for x in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):

        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters.

        If the size is 0, it prints an empty line.

        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
