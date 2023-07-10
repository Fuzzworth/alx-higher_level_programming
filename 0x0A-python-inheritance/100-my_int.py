#!/usr/bin/python3
"""
Module doc
"""


class MyInt(int):
    """
    class doc
    """

    def __eq__(self, other):
        """
        naughty
        """
        return self != other

    def __ne__(self, other):
        """
        naughty
        """
        return self == other
