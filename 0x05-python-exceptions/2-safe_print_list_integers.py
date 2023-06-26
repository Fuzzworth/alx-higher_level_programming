#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = index = 0
    try:
        while x > 0:
            if type(my_list[index]) is int:
                print("{:d}".format(my_list[index]), end="")
                count += 1
                x -= 1
            index += 1
        print("")
    except Exception:
        print("")
    return count
