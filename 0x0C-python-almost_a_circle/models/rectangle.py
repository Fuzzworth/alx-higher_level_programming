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
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        self.type_int_check("width", value)
        self.zero_check("width", value)
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
        self.type_int_check("height", value)
        self.zero_check("height", value)

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

        self.zero_check("x", value)
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

        self.zero_check("y", value)
        self.__y = value

    def zero_check(self, attribute, value):
        """
        Function doc
        """

        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute))

    def type_int_check(self, attribute, value):
        """
        Function doc
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))
