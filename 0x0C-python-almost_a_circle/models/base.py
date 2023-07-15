#!/usr/bin/python3
"""
Module Docs
"""


class Base:
    """
    Class Docs
    """

    __nb_objects = 0
    def __init__(self, id=None):
        """
        Function Docs
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
