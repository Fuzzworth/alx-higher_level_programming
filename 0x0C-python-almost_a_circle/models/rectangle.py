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
        if attribute == 'x' or attribute == 'y':
            self.negative_check(attribute, value)
        else:
            self.zero_and_negative_check(attribute, value)

    def attribute_check(self, attribute):
        """
        Function doc
        """

        if type(attribute) is not str:
            raise TypeError("attribute must be of type str")

    def zero_and_negative_check(self, attribute, value):
        """
        Function doc
        """

        self.attribute_check(attribute)
        if value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def negative_check(self, attribute, value):
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
        for y in range(self.y):
            rectangle += "\n"
        for i in range(self.__height):
            rectangle += (" " * self.x) + ("#" * self.width)
            if i != (self.height - 1):
                rectangle += "\n"
        print(rectangle)

    def __str__(self):
        """str: Function call"""
        str_s = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return str_s.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Function doc
        """

        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            valid_attributes = ['id', 'width', 'height', 'x', 'y']
            for key, value in kwargs.items():
                if key in valid_attributes:
                    exec("self.{} = {}".format(key, value))

    def to_dictionary(self):
        """
        Function Doc
        """

        return {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }

    def __eq__(self, other):
        """
        Function Doc
        """

        return self.area() == other.area()

    def __ne__(self, other):
        """
        Function Doc
        """

        return self.area() != other.area()

    def __lt__(self, other):
        """
        Function Doc
        """

        return self.area() < other.area()

    def __le__(self, other):
        """
        Function Doc
        """

        return self.area() <= other.area()

    def __ge__(self, other):
        """
        Function Doc
        """

        return self.area() >= other.area()

    def __gt__(self, other):
        """
        Function Doc
        """

        return self.area() > other.area()
