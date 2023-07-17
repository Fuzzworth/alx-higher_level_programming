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
        s = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return s.format(self.id, self.x, self.y, self.width)

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

    def update(self, *args, **kwargs):
        """
        Function doc
        """

        if args and len(args) != 0:
            if len(args) >= 1:
                    self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            valid_attributes = ['id', 'size', 'x', 'y']
            for key, value in kwargs.items():
                if key in valid_attributes:
                    exec("self.{} = {}".format(key, value))

    def to_dictionary(self):
        """
        Function Doc
        """

        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
