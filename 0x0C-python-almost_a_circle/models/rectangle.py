#!/usr/bin/python3
"""
Module doc
"""
from models.base import Base


class Rectangle(Base):
    """
    Class docs
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Function docs
        """

        self.__width = self.width(width)
        self.__height = self.height(height)
        self.__x = self.x(x)
        self.__y = self.y(y)

        super().__init__(id)

    @property
    def width(self):
        """
        Function doc
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Function Doc
        """

        self.__width = value

    @property
    def height(self):
        """
        Function Doc
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Function doc
        """

        self.__height = value

    @property
    def x(self):
        """
        Function doc
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        Function doc
        """

        self.__x = value

    @property
    def y(self):
        """
        Function doc
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        Function doc
        """

        self.__y = value
