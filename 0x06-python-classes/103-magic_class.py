#!/usr/bin/python3
from dis import dis

class MagicClass:
    def __init__(self):
        MagicClass.radius = 0

print(dis(MagicClass))
