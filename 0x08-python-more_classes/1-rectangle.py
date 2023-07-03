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
        self.__width = width
        self.__height = height

        @property
        def __width(self):
            """int: width"""
            return self.__width

        @property
        def __height(self):
            """int: height"""
            return self.__height

        @__height.setter
        def __height(self, value):
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

        @__width.setter
        def __width(self, value):
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
