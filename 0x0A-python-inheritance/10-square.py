#!/usr/bin/python3
"""
Module docs
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class docs
    """
    def __init__(self, size):
        """
        constructor docs
        """
        self.__size = size
        super().__init__(self, size, size)

    def area(self):
        """
        area
        """
        return self.__size * self.__size
