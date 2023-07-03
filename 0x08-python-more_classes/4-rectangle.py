#!/usr/bin/python3
"""
Rectangle Module
"""


class Rectangle:
    """
    Write an empty class Rectangle that defines a rectangle:

    Args:
        width (int): int
        height (int): int

    Attributes:
        width (int): int
        height (int): int

    Raises:
        TypeError: not an integer
        ValueError: less than 0
    """

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """int: width"""
        return self.__width

    @property
    def height(self):
        """int: height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Args:
           value (int): int
        Raises:
            TypeError: not int
            ValueError: less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """
        Args:
            value (int): int
            Raises:
                TypeError: not int
                ValueError: less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        Area calculator

        Return:
            int: area
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Perimeter calculator

        Return:
            int: perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.height) * 2

    def __str__(self):
        """str:rectangle"""

        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for i in range(self.__height):
            rectangle += "#" * self.__width
            if i != (self.__height - 1):
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """str: Function call"""

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
