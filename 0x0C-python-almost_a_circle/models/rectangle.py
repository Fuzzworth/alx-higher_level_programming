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
        self.all_checks("width", value)
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

        self.all_checks("height", value)
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

        self.all_checks("x", value)
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

        self.all_checks("y", value)
        self.__y = value

    def all_checks(self, attribute, value):
        """
        Function docs
        """

        self.type_int_check(attribute, value)
        self.zero_check(attribute, value)

    def attribute_check(self, attribute):
        """
        Function doc
        """

        if type(attribute) is not str:
            raise TypeError("attribute must be of type str")

        if len(attribute) == 0:
            raise ValueError("attribute cannot be an empty string")

    def zero_check(self, attribute, value):
        """
        Function doc
        """

        self.attribute_check(attribute)
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute))

    def type_int_check(self, attribute, value):
        """
        Function doc
        """

        self.attribute_check(attribute)
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))

    def area(self):
        """
        Area calculator

        Return:
            int: area
        """

        return self.width * self.height

    def display(self):
        """
        Function doc
        """

        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for i in range(self.__height):
            rectangle += "#" * self.__width
            if i != (self.__height - 1):
                rectangle += "\n"
        print(rectangle)

    def __str__(self):
        """str: Function call"""

        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(Base.id,
                                                                 self.x, self.y,
                                                                 self.width, self.height)
