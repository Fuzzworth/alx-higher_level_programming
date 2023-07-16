#!/usr/bin/python3
"""
Module Docs
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Docs
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Function Docs
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str: Function call"""

        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                                 self.x, self.y,
                                                                 self.width)

    @property
    def size(self):
        """
        Function Docs
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        Function Docs
        """

        self.width = value
        self.height = value
