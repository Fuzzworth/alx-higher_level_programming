#!/usr/bin/python3
"""
Module docs
"""
import BaseGeometry

class Rectangle(BaseGeometry):
    """
    class docs
    """
    def __init__(self, width, height):
        """
        constructor docs
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
