#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value is None:
            raise ValueError
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
