#!/usr/bin/python3
"""
Magic class module
"""
import math


class MagicClass:
    """
    Magic class

    Attributes:
        radius (int): integer
    """
    def __init__(self, radius=0):
        """
        init

        Args:
            radius (int): integer

        Raises:
            TypeError: not an int
        """

        self.__radius = 0
        if type(radius) is not int:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """float: area"""

        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """float: circumference"""

        return (2 * math.pi) * self.__radius
