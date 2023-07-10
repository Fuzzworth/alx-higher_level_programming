#!/usr/bin/python3
"""
Module docs
"""
import "7-base_geometry"


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
