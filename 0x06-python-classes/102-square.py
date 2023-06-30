#!/usr/bin/python3
"""
This is a module that Write a class Square
"""


class Square:
    """
    This is a module that Write a class Square

    Attributes:
        size (int): Human readable string describing the exception.
    """
    def __init__(self, size=0):
        """
        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            size (int): Description of `param1`.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        """
        Private instance attribute: size
        """
    def area(self):
        """
        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:

        Returns:
            Area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:

        Returns:
            Size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            value (int): value int
        Returns:
            Area
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, value):
        return self.__size < value.size

    def __le__(self, value):
        return self.__size <= value.size

    def __eq__(self, value):
        return self.__size == value.size

    def __ne__(self, value):
        return self.__size != value.size

    def __ge__(self, value):
        return self.__size >= value.size

    def __gt__(self, value):
        return self.__size > value.size
