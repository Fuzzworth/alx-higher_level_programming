#!/usr/bin/python3
def print_last_digit(number):
    if number == 0 or number == None:
        last_digit = 0
    else:
        last_digit = int(str(number)[-1])
    print("{:d}".format(last_digit), end="")
