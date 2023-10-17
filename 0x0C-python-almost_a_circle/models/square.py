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

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
        self.width = value
        self.height = value

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

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        Args:
            *args: List of arguments (non-keyworded).
                1st argument should be the id attribute.
                2nd argument should be the size attribute.
                3rd argument should be the x attribute.
                4th argument should be the y attribute.
            **kwargs: Dictionary of keyworded arguments.
                Each key represents an attribute to the instance.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the rectangle.
        Returns:
        dict: The dictionary representation of the rectangle.
        """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
