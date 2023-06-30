#!/usr/bin/python3
from dis import dis

class MagicClass:
    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def circumference(self):
        return (2 * math.pi) * self.__radius

print(dis(MagicClass))
