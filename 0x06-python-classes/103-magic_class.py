#!/usr/bin/python3
from dis import dis

class MagicClass:
    def __init__(self, radius):
        self.radius = radius

print(dis(MagicClass))
