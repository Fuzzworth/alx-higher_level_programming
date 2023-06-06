#!/usr/bin/python3
for number in range(100):
    if number != 99:
        print("{num:#d}".format(num=number), end=", ")
    else:
        print("{num:#d}".format(num=number), end="\n")
