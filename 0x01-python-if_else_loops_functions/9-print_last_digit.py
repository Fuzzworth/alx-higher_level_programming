#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    if number == 0:
        last_digit = 0
    elif number > 0:
        last_digit = int(str(number)[-1])
    print("{:d}".format(last_digit), end="")
