#!/usr/bin/python3
"""
    A class representing a rectangle
"""


class Rectangle:
    """
    A rectangle object
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
        int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle, raising errors for invalid values.

        Parameters:
        - value (int): The new width value.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
        int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle, raising errors for invalid values.

        Parameters:
        - value (int): The new height value.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an intege")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
        float: The perimeter of the rectangle.
        """
        if self.width == 0 and self.height == 0:
            return 0
        return 2 * (self.width + self.height)
