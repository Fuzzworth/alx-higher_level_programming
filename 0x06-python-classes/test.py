#!/usr/bin/python3
MagicClass = __import__('103-magic_class').MagicClass

mc = MagicClass(12)
print("{:.2f}".format(mc.circumference()))
mc = MagicClass()
print("{:.2f}".format(mc.circumference()))
mc = MagicClass("3")
print("{:.2f}".format(mc.circumference()))
mc = MagicClass(10)
print("{:.2f}".format(mc.area()))
mc = MagicClass(12)
print("{:.2f}".format(mc.circumference()))
