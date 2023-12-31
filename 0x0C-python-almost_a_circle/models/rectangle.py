#!/usr/bin/python3
""" Ractangle class """
from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class

    This class represents a rectangle and inherits from the Base class.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Class constructor for initializing Rectangle instances.
        width (int):
            The width property of the rectangle.
        height (int):
            The height property of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle.
            y (int, optional): The y-coordinate of the rectangle.
            id (int, optional): An optional argument representing the unique
            identifier.
                If not provided, a new identifier will be generated based on
                the Base class attribute __nb_objects.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Get the x-coordinate of the rectangle.

        Returns:
        int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the rectangle.

        Args:
        value (int): The new x-coordinate value.

        Raises:
        ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Get the y-coordinate of the rectangle.

        Returns:
        int: The y-coordinate of the rectangle.
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the x-coordinate of the rectangle.

        Args:
        value (int): The new y-coordinate value.

        Raises:
        ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Display the rectangle using the character #.
        Takes into account x and y coordinates.
        """
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Return the string representation of the Rectangle.

        Returns:
            str: The string representation of the Rectangle.
        """
        aid = self.id
        bx = self.__x
        cy = self.__y
        dw = self.__width
        eh = self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(aid, bx, cy, dw, eh)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Args:
            *args: Variable number of arguments.
                1st argument should be the id attribute.
                2nd argument should be the width attribute.
                3rd argument should be the height attribute.
                4th argument should be the x attribute.
                5th argument should be the y attribute.
                **kwargs: Variable number of keyword arguments.
                Each key in this dictionary represents an attribute to
                the instance.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
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
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
