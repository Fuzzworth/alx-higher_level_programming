#!/usr/bin/python3
from dis import dis

class MagicClass:
    def __init__(self, radius):
        self.__radius = 0
        type(self.__radius)

print(dis(MagicClass))
