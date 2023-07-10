#!/usr/bin/python3
"""
Module docs
"""


class BaseGeometry():
    """
    My docs
    """

    def area(self):
        """
        Function

        Raises:
            Exception: all the time
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function doc

        Args:
            name (str): string
            value (int): intger

        Raises:
            TypeError: when not int
            ValueError: when below 1
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
