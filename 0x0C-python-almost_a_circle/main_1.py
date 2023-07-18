#!/usr/bin/python3
""" Check """
from models.rectangle import Rectangle
import os
import json


file_path = "Rectangle.json"
if os.path.exists(file_path):
    os.remove(file_path)

list_objs = [Rectangle(3, 4), Rectangle(5, 8, 1), Rectangle(9, 1, 3, 2)]
Rectangle.save_to_file(list_objs)

if not os.path.exists(file_path):
    print("save_to_file doesn't create a file {}".format(file_path))
    exit(1)

res = Rectangle.load_from_file()

if res is None:
    print("load_from_file doesn't load objects from file")
    exit(1)

if type(res) is not list:
    print("load_from_file doesn't return a list")
    exit(1)

print("OK", end="")
